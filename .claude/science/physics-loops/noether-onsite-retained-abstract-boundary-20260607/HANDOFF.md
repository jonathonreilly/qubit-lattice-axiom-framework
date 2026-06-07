# Handoff

This PR repairs the onsite/internal Noether conditional row by splitting
authority:

- retained abstract bilinear continuity theorem supplies the carrier-free
  finite matrix-unit identities;
- this note supplies bounded carrier-specific support for the onsite U(1)
  staggered/Kawamoto-Smit sign and locality checks;
- the staggered carrier, physical density/readout bridge, and site-mixing
  current theorem remain outside the claim.

Changed files:

- `docs/AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md`
- `scripts/audit_companion_lattice_noether_onsite_internal_2026_06_05.py`
- `logs/runner-cache/audit_companion_lattice_noether_onsite_internal_2026_06_05.txt`

Verification:

```sh
PYTHONPATH=scripts python3 scripts/audit_companion_lattice_noether_onsite_internal_2026_06_05.py
```

Expected result: `TOTAL: 14 PASS / 0 FAIL` and boundary guard `PASS`.

No `docs/audit/**` files are changed.
