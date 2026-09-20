# Security Policy

## Scope

`crossfire-config-menu` is a client-side configuration/overlay menu
skeleton for the CrossFire desktop client. This repository intentionally
ships **without** working memory offsets, signatures, or bypass logic.
`app/services/memory_service.py` is a stub that documents the interface
a real implementation would need, and raises `NotImplementedError` by
default.

## Reporting a vulnerability

If you find a security issue in the code that *is* present here (e.g.
unsafe deserialization in `ConfigService`, path traversal in
`utils/paths.py`, insecure hotkey registration), please open a private
report rather than a public issue:

- Email: security@example-crossfire-tools.invalid
- Include reproduction steps and the commit hash.
- We aim to acknowledge within 5 business days.

## Out of scope

- Requests to add working game-memory offsets, anti-cheat evasion, or
  packet manipulation code will not be accepted or reviewed.
- This project does not condone violating the CrossFire Terms of
  Service. Anything you build on top of this scaffolding is your own
  responsibility, including account bans and detection risk.

## Supported versions

Only the latest tagged release on `main` receives security fixes for
the scaffolding/UI/config layers.