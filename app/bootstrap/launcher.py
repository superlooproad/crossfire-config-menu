"""Application entry point for crossfire-config-menu.

Responsible for early environment checks, wiring the core engine to
the Qt application object, and handing control over to the splash
sequence before the main menu window is shown.
"""
from __future__ import annotations

import sys

from PyQt5.QtWidgets import QApplication

from app.bootstrap.splash import show_splash
from app.core.engine import MenuEngine
from app.utils.logger import get_logger
from app.utils.paths import ensure_runtime_dirs

log = get_logger(__name__)


def _check_platform() -> None:
    if sys.platform != "win32":
        raise RuntimeError(
            "crossfire-config-menu targets Windows desktops only "
            "(the CrossFire client itself is Windows-only)."
        )


def main() -> int:
    _check_platform()
    ensure_runtime_dirs()

    log.info("Starting crossfire-config-menu v%s", "0.4.2")

    qt_app = QApplication(sys.argv)
    engine = MenuEngine()

    show_splash(qt_app, on_ready=engine.start)

    return qt_app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())