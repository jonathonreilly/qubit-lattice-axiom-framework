# Trace Gate

## Source Files

- `docs/HYPERCHARGE_IDENTIFICATION_NOTE.md`
- `scripts/frontier_hypercharge_identification.py`
- `logs/runner-cache/frontier_hypercharge_identification.txt`

## Forbidden Surfaces

This PR must not edit:

- `docs/audit/**`
- `docs/repo/FRONT_DOOR_STATUS.md`
- generated publication/effective-status files

## Runner Gate

`scripts/frontier_hypercharge_identification.py` fails if:

- the source note returns to `**Status:** proposed chain claim`;
- proposed-retained wording appears;
- primary runner/cache metadata is removed;
- the source-side boundary firewall text is removed;
- the note no longer states that the ledger/audit verdict is not retagged by
  this source repair.
