"""Lightweight splash sequence shown while the core engine warms up
(loads the active profile, verifies the CrossFire process is present,
and pre-builds the overlay window)."""
from __future__ import annotations

from typing import Callable

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap, QColor

from app.utils.logger import get_logger

log = get_logger(__name__)

_SPLASH_DURATION_MS = 1200


def show_splash(qt_app: QApplication, on_ready: Callable[[], None]) -> None:
    pixmap = QPixmap(420, 240)
    pixmap.fill(QColor("#101014"))

    splash = QSplashScreen(pixmap)
    splash.showMessage(
        "crossfire-config-menu — loading profile...",
        alignment=0x84,  # bottom-center-ish
        color=QColor("#e0e0e0"),
    )
    splash.show()
    qt_app.processEvents()

    def _finish() -> None:
        log.debug("Splash finished, handing off to MenuEngine.start()")
        splash.close()
        on_ready()

    QTimer.singleShot(_SPLASH_DURATION_MS, _finish)