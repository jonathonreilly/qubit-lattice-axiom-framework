# Hypercharge Chain Boundary Firewall Handoff

## Target

Source-side repair for `docs/HYPERCHARGE_IDENTIFICATION_NOTE.md`, the
hypercharge identification row that has historically been audit-blocked by
carrier-renaming and normalization-import ambiguity.

## Change

- Replaces the stale top-level `proposed chain claim` source status with
  `bounded/conditional chain assembly`.
- Adds primary runner and cache metadata to the source header.
- Makes the parent conditional on the narrow ratio theorem, the LHCM
  matter-assignment row, and the alpha=1/3 normalization bridge/admission
  boundary.
- Adds a runner source-boundary firewall so stale proposed-retained or
  proposed-chain language fails before the numerical checks run.

## Honest Boundary

This does not make the row retained. It only makes the source row cleaner
for independent re-audit. The parent still does not internally derive:

- the `(Sym^2, Anti^2)` to `(SU(3)-fundamental, SU(3)-singlet)` matter
  assignment;
- the physical SM naming convention;
- the absolute `alpha = 1/3` normalization inside this parent note;
- the Gell-Mann--Nishijima readout from framework primitives.

## Verification

Run:

```bash
python3 scripts/frontier_hypercharge_identification.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_hypercharge_identification.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_hypercharge_identification.py
python3 -m py_compile scripts/frontier_hypercharge_identification.py
git diff --check
```
