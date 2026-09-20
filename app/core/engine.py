"""Core engine that owns the running session, wires up feature
handlers, and drives the main menu window lifecycle."""
from __future__ import annotations

from app.core.session_state import SessionState
from app.handlers.aim_handler import AimHandler
from app.handlers.esp_handler import EspHandler
from app.handlers.hotkey_handler import HotkeyHandler
from app.handlers.loadout_handler import LoadoutHandler
from app.services.config_service import ConfigService
from app.services.memory_service import MemoryService
from app.services.overlay_service import OverlayService
from app.utils.logger import get_logger

log = get_logger(__name__)


class MenuEngine:
    """Top-level coordinator for the config/overlay menu.

    Owns the long-lived services (config, memory, overlay) and the
    per-feature handlers. The engine does not know about UI widgets
    directly — handlers report state changes back through
    ``SessionState`` and the overlay/config services persist or
    render as needed.
    """

    def __init__(self) -> None:
        self.config_service = ConfigService()
        self.memory_service = MemoryService()
        self.overlay_service = OverlayService()
        self.session = SessionState()

        self.aim_handler = AimHandler(self.session, self.memory_service)
        self.esp_handler = EspHandler(self.session, self.overlay_service)
        self.loadout_handler = LoadoutHandler(self.session, self.config_service)
        self.hotkey_handler = HotkeyHandler(self.session, self)

    def start(self) -> None:
        log.info("MenuEngine starting")
        profile = self.config_service.load_active_profile()
        self.session.apply_profile(profile)

        self.hotkey_handler.register_defaults()
        self.esp_handler.sync_overlay()
        log.info("MenuEngine ready with profile '%s'", profile.name)

    def toggle_feature(self, feature_key: str) -> None:
        """Dispatch a toggle request to the handler that owns it."""
        if feature_key.startswith("aim_"):
            self.aim_handler.toggle(feature_key)
        elif feature_key.startswith("esp_"):
            self.esp_handler.toggle(feature_key)
        elif feature_key.startswith("loadout_"):
            self.loadout_handler.apply(feature_key)
        else:
            log.warning("Unknown feature key requested: %s", feature_key)

    def shutdown(self) -> None:
        log.info("MenuEngine shutting down, persisting profile")
        self.config_service.save_active_profile(self.session.to_profile())
        self.overlay_service.teardown()