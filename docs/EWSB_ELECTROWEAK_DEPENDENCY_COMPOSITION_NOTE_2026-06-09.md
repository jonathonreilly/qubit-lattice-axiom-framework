# Electroweak Dependency-Composition Note (source proposal)

**Date:** 2026-06-09
**Claim type:** bounded_theorem (dependency-structure composition over
audit-pending electroweak source proposals and their imported SM-convention
forms).
**Kind:** source proposal — dependency structure + cross-note composition over
three existing electroweak source proposals on current `main`.
**Status authority:** independent audit lane only. This source note authors
**no** audit status for itself or for any note it cites. Nothing here should be
read as a grade, as a claim that any note is retained/promoted, or as preparing
any note for audit.

---

## 0. Purpose

Three electroweak source proposals on current `main` form a small derivation DAG:

```
        HIGGS_Y_FROM_LHCM_AND_YUKAWA_STRUCTURE_NOTE_2026-05-02   (Higgs in (1,2)_{Y=+1})
                                  |
                                  v
        EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02                (Q = T3 + Y/2)        [parent]
                 /                              \
                v                                v
  EM_COUPLING_FROM_EWSB_NOTE_2026-05-02   W_Z_MASS_RATIO_FROM_EWSB_NOTE_2026-05-02
       (e = g sin th = g' cos th)              (MW^2/MZ^2 = cos^2 th,  rho = 1)
            [child A]                                   [child B]
```

This note (i) records the dependency edges with verbatim citations, (ii) re-verifies each
node's central identity with exact rational arithmetic, and (iii) makes explicit a
**composition identity** that ties the two children together through their shared parent
and that appears in **none** of the three individual notes.

The paired runner `scripts/frontier_ewsb_electroweak_dependency_composition_2026_06_09.py`
re-checks every assertion below (`TOTAL: PASS=56 FAIL=0`). No PDG or fitted value is
consumed as an input; all checks are exact rational identities over arbitrary rational
gauge-coupling instantiations.

---

## 1. Nodes (central identities re-verified)

**Parent — [`EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02`](EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md).**
The unbroken `U(1)_em` generator from the Higgs `Y_H = +1` VEV
`⟨H⟩ = (0, v/√2)` is

```
Q = T3 + Y/2 .
```

Re-verified: `Q = T3 + Y/2` reproduces the electric charge of all standard chiral content
plus the two Higgs-doublet components (`u_L, d_L, ν_L, e_L, u_R, d_R, e_R, ν_R, H+, H0`);
`(T3 + ½Y)` annihilates the neutral VEV (unbroken photon) while the orthogonal `(T3 − ½Y)`
direction acts non-trivially (the broken `Z`-direction).

**Child A — [`EM_COUPLING_FROM_EWSB_NOTE_2026-05-02`](EM_COUPLING_FROM_EWSB_NOTE_2026-05-02.md).**

```
e = g sin th_W = g' cos th_W ,   equivalently   1/e^2 = 1/g^2 + 1/g'^2 ,
```

with `tan th_W = g'/g`. Re-verified as an exact identity over the coupling instantiations.

**Child B — [`W_Z_MASS_RATIO_FROM_EWSB_NOTE_2026-05-02`](W_Z_MASS_RATIO_FROM_EWSB_NOTE_2026-05-02.md).**

```
MW^2/MZ^2 = g^2/(g^2 + g'^2) = cos^2 th_W ,   rho := (MW^2/MZ^2)/cos^2 th_W = 1 .
```

Re-verified as an exact identity over the coupling instantiations (including extreme and
non-trivial rational ratios, and the `g' → 0` no-mixing limit).

---

## 2. Edges (verbatim citations)

**Edge `child A ← parent`.** `EM_COUPLING_FROM_EWSB_NOTE`, Section 0 (Given #1):

> "EWSB pattern Q = T_3 + Y/2 from `EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md` (cycle 18, PR #281)"

**Edge `child B ← parent`.** `W_Z_MASS_RATIO_FROM_EWSB_NOTE`, Section 0 (Given #1):

> "EWSB pattern Q = T_3 + Y/2 from `EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md` (cycle 18, PR #281)"

**Edge `child B ← HIGGS_Y` (direct).** `W_Z_MASS_RATIO_FROM_EWSB_NOTE`, Section 0 (Given #2):

> "Higgs in (1,2)_{Y=+1} with VEV ⟨H⟩ = (0, v/√2)^T from `HIGGS_Y_FROM_LHCM_AND_YUKAWA_STRUCTURE_NOTE_2026-05-02.md` (cycle 15)"

There is **no** edge between the two children: `em_coupling` and `w_z_mass_ratio` are
independent children of the same parent. Both are governed by the **same** mixing angle
`th_W` (defined by `tan th_W = g'/g`), inherited through the EWSB pattern.

---

## 3. Composition (the load-bearing payload)

Because both children are governed by the **one** mixing angle `th_W`, the two child
identities supply

```
sin^2 th_W = e^2/g^2        (from child A:  e = g sin th_W)
cos^2 th_W = MW^2/MZ^2      (from child B)
```

and the Pythagorean closure `sin^2 + cos^2 = 1` gives the **cross-child relation**

```
e^2/g^2 + MW^2/MZ^2 = 1 ,   equivalently   MW^2/MZ^2 = 1 − e^2/g^2 .
```

This relation is the content carried by the dependency structure itself: it requires
**both** children **and** their shared parent, and it appears in **none** of the three
individual notes (each child knows only its own face of `th_W`). It states that the
electromagnetic coupling and the `W/Z` mass ratio are not independent electroweak
outputs — they are two readings of a single mixing angle fixed by the EWSB pattern.

The runner includes a **negative control**: substituting a spurious `MW^2/MZ^2` not equal
to `cos^2 th_W` breaks `e^2/g^2 + MW^2/MZ^2 = 1`, confirming the relation is non-vacuous
(the edge carries genuine content, not a tautology of notation).

A cross-node consistency illustration the child notes themselves record (kept symbolic,
no PDG input): at a hypothetical `sin^2 th_W = 3/8`, child B gives `MW^2/MZ^2 = 5/8` and
the composition `e^2/g^2 + MW^2/MZ^2 = 1` closes.

---

## 4. What this does NOT close

- The **absolute scales** `v`, `g`, `g'` and the **scale-dependent value** of `th_W` (or
  `sin^2 th_W`) are external observables; nothing here derives them. The composition is a
  relation among them, not a determination of any one.
- The imported **SM-convention forms** each cited note carries remain imported:
  the Higgs potential `V = −μ² H†H + λ(H†H)²` (parent), the photon–fermion
  coupling form `e Q ψ̄γ^μ ψ A_μ` (child A), and the Higgs kinetic term
  `(D_μ H)†(D^μ H)` (child B).
- The parent's own dependence on the cycle-15
  [`Y_H = +1` derivation](HIGGS_Y_FROM_LHCM_AND_YUKAWA_STRUCTURE_NOTE_2026-05-02.md),
  which itself rests on imported SM Yukawa structure, is inherited unchanged.
- Loop corrections to `rho` (which depend on the full SM particle content) are outside the
  tree-level identities re-verified here.
- This note authors **no** audit status. It does not assert any cited note is
  retained, promoted, or ready for audit; it re-checks the cited identities and records
  their composition only. The independent audit lane sets all statuses.

---

## 5. Paired runner

`scripts/frontier_ewsb_electroweak_dependency_composition_2026_06_09.py` —
class-A, exact `Fraction` arithmetic, `TOTAL: PASS=56 FAIL=0`. Cached output:
`logs/runner-cache/frontier_ewsb_electroweak_dependency_composition_2026_06_09.txt`.
