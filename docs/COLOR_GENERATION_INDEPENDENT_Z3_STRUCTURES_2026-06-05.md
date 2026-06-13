# Abstract color-carrier and generation-candidate Z3 actions are inequivalent

**Date:** 2026-06-05
**Type:** derivation
**Claim type:** bounded theorem / abstract algebraic inequivalence.
**Status authority:** independent audit lane only. This note does not set or
predict the ledger outcome.
**Runner:** `scripts/color_generation_z3_identification_no_go_2026_06_05.py`
(SUMMARY: PASS=21 FAIL=0).
**Cached log:** `logs/runner-cache/color_generation_z3_identification_no_go_2026_06_05.txt`
**Scope guard:** `scripts/frontier_color_generation_z3_scope_guard_2026_06_12.py`
(SUMMARY: PASS=8 FAIL=0).
**Scope guard cache:** `logs/runner-cache/frontier_color_generation_z3_scope_guard_2026_06_12.txt`

## Statement (abstract)

Given the cited abstract carrier actions, the two native Z3 representations are
character-inequivalent and therefore cannot be the same Z3 representation.
This is an abstract finite-representation statement only. It does **not** by
itself identify the color carrier with physical SM color, identify the hw=1
orbit with physical generations, or prove a physical `3 x 3` product-label
structure.

- **Abstract color-center Z3.** From the cited color automorphism
  ([`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)),
  the stipulated center action on the abstract triplet carrier is the scalar
  `omega * I_3` -> Z3 character `(3, 3 omega, 3 omega^2) = 3 * chi_omega`.
- **Abstract generation-candidate Z3.** From the hw=1 BZ-corner orbit with the cubic axis cycle
  ([`CL3_TASTE_GENERATION_THEOREM.md`](CL3_TASTE_GENERATION_THEOREM.md) provenance), the generation carrier is the regular
  representation -> Z3 character `(3, 0, 0) = chi_0 + chi_omega + chi_omega^2`.

These two characters are inequivalent (they agree at the identity, value `3`, but
differ at the two non-identity elements: `3 omega, 3 omega^2` vs `0, 0`).
Therefore the two cited abstract Z3 actions are distinct. Any physical
SM-color, physical-generation, or `3 x 3` product-label conclusion requires
additional bridge theorems and is outside this note's load-bearing claim.

## Why this is not a physical SM bridge

The positive content is the structural calculation: the cited abstract carriers
give distinct Z3 representations. The note does not use that calculation as a
retained bridge to physical SM labels. The following remain missing if a future
row wants a physical independence theorem:

1. a retained bridge identifying the abstract color-center carrier with
   physical SM color;
2. a retained bridge identifying the hw=1 cubic-axis orbit with physical
   generations;
3. a retained product/commuting-label bridge proving that the two physical
   labels coexist as a `3 x 3` carrier structure.

## Proof (verified exactly in the runner, 21/21 PASS)

1. **Two characters.** Abstract color-center action: center scalar `omega*I_3`
   -> `(3, 3 omega, 3 omega^2)`. Abstract generation-candidate action:
   regular rep -> `(3, 0, 0)`. (Runner computes both from the cited abstract
   carriers.)
2. **Inequivalence.** Trace at each group element: equal at `e` (`3`); differ at
   `g` (`3 omega` vs `0`) and `g^2` (`3 omega^2` vs `0`); the relabel `g <-> g^2`
   does not fix it. So the representations are inequivalent.
3. **Multiplicities.** `chi_omega` appears with multiplicity `3` in the color rep
   but `1` in the generation rep — they cannot be the same Z3 module.
4. **No equivariant isomorphism.** Schur: `dim Hom = 3` but every intertwiner has
   rank `<= 1 < 3`, so no equivariant isomorphism exists. The two carriers are
   abstractly inequivalent.
5. **No physical-label conclusion.** The character obstruction does not prove
   physical SM color, physical generation, or the product `3 x 3` carrier
   without the three bridge theorems listed above.

## Scope and honest boundary

This shows only that the cited abstract carriers are **inequivalent Z3
representations**. It does **not** identify either carrier with a physical SM
label and does **not** prove a physical `3 colors x 3 generations` product
structure. The color carrier authority (`cl3_color_automorphism_theorem`) and
the generation-candidate authority (`cl3_taste_generation_theorem`) are cited as
bounded provenance; their effective audit statuses are left to the ledger. The
runner reconstructs the character comparison independently. No measured inputs
are used.
