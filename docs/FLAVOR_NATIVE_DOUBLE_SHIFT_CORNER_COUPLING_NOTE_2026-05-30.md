# Flavor — the corner coupling is native (double-shift), correcting the (π,π,0) label

**Date:** 2026-05-30
**Claim type:** bridge-gap attack move 1 / capstone correction + native derivation
of the corner-coupling FORM (NOT a derivation of the value). Imports nothing.
**Runner:** `scripts/flavor_native_double_shift_corner_coupling_2026_05_30.py`
(+ cache). Grounded by the frontier-map workflow (`wf_338eaf49`), which flagged
that the session capstone's `(π,π,0)` label is *not a within-triplet operator*
and recommended this zero-import computation as the decisive first move.

## The correction (my capstone was imprecise)
The session capstone said `b≠0` requires "a staggered condensate at `(π,π,0)`."
A **single** π-shift `S_μ` (bit-flip `μ` on the `(Z₂)³` corner cube) projects to
**zero** on the hw=1 generation triplet — it maps `(1,0,0)→(0,0,0)` (hw1→hw0)
and `(0,1,0),(0,0,1)→hw2`, leaving the triplet entirely. So a literal single
`(π,π,0)` shift is **not** a within-triplet operator, and cannot be the
generation breaker the retained chain
(`s3_mass_matrix_no_go`, `generation_degeneracy_minimal_symmetry_breaking`
2026-05-23) requires (a *within-triplet* S₃→subgroup operation).

## The native operator (derivable, retained kinematics)
The **double** shift `S_μS_ν` (flip two bits) projected to the triplet is a
partial transposition; the S₃-symmetric **sum** over the three double-shifts
projects to **exactly `J−I`** (the three transpositions):
```
P (S_yz + S_zx + S_xy) Pᵀ = J − I     (verified)
```
So the off-diagonal generation coupling `b` **is native kinematics**: a
distance-2 (double π-shift) hop on the corner cube, `b·(J−I)`, carrying a
momentum transfer of **`(π,π,0)`-type** (two simultaneous π-shifts). That is what
the capstone's intuition meant — now correctly an **S₃-symmetric bilinear
projected to the triplet**, built from the *retained* cube-shift intertwiner
(`site_phase_cube_shift_intertwiner`, retained: `Φ†P_μΦ = S_μ`), not a single
shift. **This derives the existence and form of `b` from retained kinematics** —
independent of the fermion vacuum (which won't supply it) and of any import.

## The sharpening (the value gate is now one concrete ratio)
With `Y = aI + b(J−I)`: √-masses `{a+2b, a−b, a−b}` — only **2 distinct**
(S₃-symmetric, doublet degenerate), and `Q = 1/3 + (2/3)r`, `r = b²/a²`. So:

- **The value `Q=2/3` needs *only* the symmetric, native `b`:** `b/a = 1/√2`.
  This reduces the entire Koide value to **one magnitude ratio of concrete native
  operators** — the (distance-2 double-shift coupling `b`) / (distance-0 diagonal
  mass `a`) on the action's corner cube.
- **The 3-distinct splitting (`e≠μ`) is a separate, Q-orthogonal import.** Every
  product of real shifts is a real permutation → projects to a real symmetric
  operator → `b` real → at most 2 distinct masses. The oriented complex part
  `i(C−C²)` (3 distinct masses, the Brannen phase) **cannot** be made from real
  shift-products; it needs a chirality/orientation = the
  `koide_z3_equivariant_anticommuting_no_go` twin gate (retained_bounded), the
  single user-approval-gated import — and it is exactly Q-orthogonal, so it does
  **not** affect `Q=2/3`.

## Net — where the bridge-gap frontier now stands
This cleanly **separates** the problem the retained surface left fused:
1. **Value `Q=2/3` ⟺ `b/a = 1/√2`** — a magnitude ratio of native operators
   (distance-2 / distance-0 coupling on the corner cube). The *form* is now
   derived; the open piece is the **coefficient ratio set by the derived
   `g_bare=1` action**. This is the genuine, concrete next target (and it is the
   heat-kernel time in disguise: `b/a = tanh²(t)`, but now an action-coefficient
   ratio, not a free `t`).
2. **The `e≠μ` 3-distinct spectrum** — a separate, Q-orthogonal chiral import
   (the C₃-orbit orientation), the one user-approval-gated piece, which the
   workflow need not entangle with the value.

No false closure; no claim that `b/a=1/√2` is derived. The contribution is a
correction (single shift → double-shift bilinear), a native derivation of the
coupling *form*, and a clean split of the value gate (a native operator-ratio)
from the chiral import (Q-orthogonal, e–μ only).
