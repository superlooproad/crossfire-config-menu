"""In-memory session state shared across handlers for the current
menu run (not persisted directly — see ConfigService for that)."""
from __future__ import annotations

from dataclasses import dataclass, field

from app.models.cheat_profile import CheatProfile
from app.models.menu_state import MenuState


@dataclass
class SessionState:
    """Mutable runtime state for the active menu session."""

    menu: MenuState = field(default_factory=MenuState)
    active_profile_name: str =