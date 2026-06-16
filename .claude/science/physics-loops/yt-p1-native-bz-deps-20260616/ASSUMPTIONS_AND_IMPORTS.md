# Assumptions And Imports

- Parent plaquette value: `P = 0.5934` is consumed only through
  `PLAQUETTE_SELF_CONSISTENCY_NOTE.md`; this block does not derive it.
- Canonical helper: `scripts/canonical_plaquette_surface.py` supplies the
  repo helper constants checked by the new arithmetic certificate.
- Native BZ quadrature: `YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md`
  remains a source-side numerical certificate pending independent audit.
- Literature bracket: the old `I_S in [4,10]` bracket remains parallel context
  and is not load-bearing for the native path.
