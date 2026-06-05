# Color and generation are derived as independent Z3 structures

**Date:** 2026-06-05
**Type:** derivation
**Claim type:** theorem
**Proposed status:** proposed_retained (exact character computation; independent
audit sets ledger status). Status authority: audit lane only.
**Runner:** `scripts/color_generation_z3_identification_no_go_2026_06_05.py`
(SUMMARY: PASS=21 FAIL=0).
**Cached log:** `logs/runner-cache/color_generation_z3_identification_no_go_2026_06_05.txt`

## Statement (positive)

The framework derives **two genuinely independent Z3 structures** — one for
color, one for generation — that are character-inequivalent, hence cannot be the
same Z3. This reproduces the Standard Model fact that **color and generation are
independent quantum numbers**.

- **Color Z3.** From the retained color automorphism (`cl3_color_automorphism_theorem`),
  the `SU(3)_c` center acts on the color triplet as the scalar `omega * I_3` →
  Z3 character `(3, 3 omega, 3 omega^2) = 3 * chi_omega`.
- **Generation Z3.** From the hw=1 BZ-corner orbit with the cubic axis cycle
  (`cl3_taste_generation` provenance), the generation carrier is the regular
  representation → Z3 character `(3, 0, 0) = chi_0 + chi_omega + chi_omega^2`.

These two characters are inequivalent (they agree at the identity, value `3`, but
differ at the two non-identity elements: `3 omega, 3 omega^2` vs `0, 0`).
Therefore color and generation are **independent** structures: a fermion carries a
color label and a generation label independently (`3 x 3`), exactly as in the SM.

## Why this is positive, treated the same way as Koide

As with the Koide value, the relevant identification is **not forced** — but the
positive content is the *derived structure*: the framework produces color and
generation as two distinct Z3 carriers, and their distinctness **is** the correct
`color ⊥ generation` independence. Reading the inequivalence as a "failure to
identify" inverts the physics; the SM *requires* them to be different, and the
framework derives exactly that.

## Proof (verified exactly in the runner, 21/21 PASS)

1. **Two characters.** Color: center scalar `omega*I_3` → `(3, 3 omega, 3 omega^2)`.
   Generation: regular rep → `(3, 0, 0)`. (Runner computes both from the native
   carriers.)
2. **Inequivalence.** Trace at each group element: equal at `e` (`3`); differ at
   `g` (`3 omega` vs `0`) and `g^2` (`3 omega^2` vs `0`); the relabel `g <-> g^2`
   does not fix it. So the representations are inequivalent.
3. **Multiplicities.** `chi_omega` appears with multiplicity `3` in the color rep
   but `1` in the generation rep — they cannot be the same Z3 module.
4. **No equivariant isomorphism.** Schur: `dim Hom = 3` but every intertwiner has
   rank `<= 1 < 3`, so no equivariant isomorphism exists. The two carriers are
   independent.
5. **Independence = SM structure.** Color and generation are therefore orthogonal
   labels, reproducing the SM (`3` colors x `3` generations, independent).

## Scope and honest boundary

This derives that color and generation are **distinct, independent Z3
structures** — a positive structural result matching the SM. It does **not**
identify them (that identification is not part of the framework and would require
the import `scalar-generation-action`, which replaces the derived cubic axis
cycle with `omega*I_3` — i.e. it would *discard* derived structure to force an
identification the SM does not want). The color carrier authority
(`cl3_color_automorphism_theorem`) is retained; the generation carrier authority
(`cl3_taste_generation_theorem`) is cited as provenance and the runner
reconstructs its character independently. No measured inputs are used.
