# Contributing to crossfire-config-menu

Thanks for your interest in improving `crossfire-config-menu`, a desktop
configuration/overlay menu built for tinkering with CrossFire client-side
display and loadout settings.

## Ground rules

1. This project targets **Windows 10/11** desktops. PRs that add
   platform-specific code must be guarded appropriately
   (`app/utils/paths.py` is the canonical place for OS path handling).
2. Keep feature toggles inside `app/handlers/`. Handlers should stay
   thin and delegate real state work to `app/services/`.
3. Any code that touches process memory (`app/services/memory_service.py`)
   must ship with a clear `NotImplementedError` fallback and a comment
   explaining what reversed data would be required. We do not merge
   working offsets/signatures into this repository — see `SECURITY.md`.
4. New menu options belong in `config/menu_layout.json`, not hardcoded
   in the UI layer.

## Workflow

- Fork, branch off `main`, keep commits scoped to one handler/service.
- Run `pytest` before opening a PR.
- Add or update a model in `app/models/` whenever you introduce a new
  persisted setting so `ConfigService` can (de)serialize it safely.
- Describe manual test steps in the PR description (which build of the
  launcher you ran, what profile you loaded).

## Style

- Python 3.11+, type hints required on public functions.
- Prefer dataclasses for models (`app/models/cheat_profile.py`,
  `app/models/menu_state.py`).
- Logging goes through `app/utils/logger.py`, never `print()`.

## Reporting issues

Use the issue tracker for crashes, UI bugs, or config serialization
problems. Do not open issues requesting working memory offsets or
detection bypasses — those will be closed. See `SECURITY.md`.