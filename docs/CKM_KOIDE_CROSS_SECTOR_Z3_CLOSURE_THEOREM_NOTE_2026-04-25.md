# Cross-Sector N_gen = N_color = 3 Source-Equality Boundary

**Date:** 2026-04-25

**Status:** bounded-support / authority-boundary. This note is not a positive
cross-sector closure claim on the current authority surface.

**Primary runner:**
`scripts/frontier_ckm_koide_cross_sector_z3_closure.py`

## Purpose

This note preserves the exact arithmetic equality

```text
N_gen = 3
N_color = 3
N_gen = N_color = 3
```

while removing the old positive-closure framing. The equality is useful
bounded support, but the current source authorities do not certify it as
retained-positive cross-sector closure.

## Source Reading

The runner reads:

```text
R1: N_gen = 3      from THREE_GENERATION_STRUCTURE_NOTE
R2: N_color = 3    from CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25
R3: N_gen = N_color = 3 by direct arithmetic equality
```

`THREE_GENERATION_STRUCTURE_NOTE` is only used at its current bounded status.
`CKM_MAGNITUDES_STRUCTURAL_COUNTS` is treated as a source text with an exposed
authority boundary unless and until it becomes retained-positive. The runner
does not promote either source.

## Auxiliary Z^3 Reading

The CL3 color/taste notes remain explanatory support only:

```text
CL3_COLOR_AUTOMORPHISM_THEOREM: Z^3/color-axis motif
CL3_TASTE_GENERATION_THEOREM: hw=1 taste/generation-candidate motif
```

Those motifs are consistent with the value `3`, but they are not used as
load-bearing proof of physical `N_gen = 3`, physical `N_color = 3`, charged
lepton Koide, PMNS closure, or any stronger unification claim.

## What Is Preserved

The PR should preserve the exact bounded result:

```text
N_GEN_N_COLOR_EQUALITY_ARITHMETIC_SUPPORT = True
```

The result has value because it gives a clean source-equality checkpoint for
later CKM/Koide bridge work, with no hidden support-tier promotion.

## What Is Not Claimed

This note does not:

- close the cross-sector `N_gen = N_color` identification on retained-positive
  authorities;
- upgrade generation candidates to physical generations;
- promote CL3 support-tier notes, Koide bridge notes, or CKM source notes;
- derive charged-lepton Koide, PMNS closure, or a physical generation/color
  mechanism beyond the exact equality of the two extracted source values;
- alter audit verdicts or repo-wide authority surfaces.

If future review/audit promotes the source authorities, this note provides the
minimal equality check that can be rerun. Until then, it is bounded source
support with explicit authority boundaries.
