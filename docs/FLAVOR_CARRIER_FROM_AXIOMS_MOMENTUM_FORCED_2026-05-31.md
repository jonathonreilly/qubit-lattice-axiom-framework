# Flavor Carrier Conditional Integration Map: Finite Translation Characters and Open Physical Identifications

**Date:** 2026-05-31
**Type:** open_gate
**Claim boundary:** conditional integration map. The exact finite-cell input is
the positive construction in
[`FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md`](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md).
This parent keeps the physical `hw=1` locus, `r=1/2`, and readout
identifications explicitly open.
**Status:** source-note proposal awaiting independent audit; audit and effective
status are pipeline-owned.
**Runner:**
[`scripts/flavor_carrier_from_axioms_momentum_forced_2026_05_31.py`](../scripts/flavor_carrier_from_axioms_momentum_forced_2026_05_31.py)
**Cache:**
[`logs/runner-cache/flavor_carrier_from_axioms_momentum_forced_2026_05_31.txt`](../logs/runner-cache/flavor_carrier_from_axioms_momentum_forced_2026_05_31.txt)

The historical filename remains unchanged for graph stability. Its former
forcing language is not part of this reader-facing claim.

## 2026-07-18 positive-scope repair

This parent now consumes the 2026-06-15 row only for these exact statements on
the supplied periodic `2 x 2 x 2` cell:

- the three translations are commuting unitary permutations;
- the eight `Z_2^3` characters form an orthonormal simultaneous eigenbasis;
- the supplied `hw=1` subset has three distinct joint characters in one
  transitive `C_3[111]` orbit;
- every character has position probability profile `(1/8,...,1/8)` and
  symbolic diagonal expectation `(1/8) sum_n w_n`;
- the rank-one character projectors are orthogonal idempotents resolving the
  identity, with expectation matrix `delta_(kq)`.

These equalities carry no physical carrier, generation, flavor, observable, or
readout assignment. In particular, this parent no longer cites the finite-cell
row for a position-versus-momentum necessity statement.

## Conditional integration question

How can the exact finite translation-character construction be placed beside
the separate physical-locus, Koide-basepoint, and readout-identification work
without granting any of those identifications by notation?

## Layer A — exact finite translation-character input

On the supplied finite representative, the character vectors are

```text
psi_k(n) = (-1)^(k.n) / sqrt(8),
```

and the `hw=1` labels are `(1,0,0)`, `(0,1,0)`, and `(0,0,1)`. Their joint
translation-character triples are pairwise distinct, the coordinate cycle
acts transitively, their profiles are uniformly `1/8`, and their rank-one
projector expectation matrix is `I_3`. The split theorem supplies exactly
these positive finite equalities and nothing about physical interpretation.

## Layer B — physical-locus identification remains open

The supplied `hw=1` subset is an abstract finite locus in Layer A. This parent
contains a conditional staggered/Kawamoto-Smit route for a possible physical
identification. The route's named inputs are single-mode Grassmann
fermionization and chiral anticommutation
`{epsilon,D}=0`, with `epsilon=(-1)^(x+y+z)`, as recorded in
[`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md).
That source describes compatibility under its supplied operator class; this
parent does not promote the operator class or identify its locus with physical
generations.

Two finite comparison formulas remain useful as conditional-route context:

- `sum_mu sin^2(k_mu)` is zero at all eight corners of `{0,pi}^3`, with
  Hamming multiplicities `(1,3,3,1)`;
- the displayed Wilson second-difference comparison has the Hamming-weight
  staircase `(0,2r,4r,6r)`.

They are comparisons between supplied operator constructions, not an
exhaustion of possible physical routes. The relationship to the abstract
chirality-gate surfaces remains bookkeeping context through
[`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md)
and
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md).
Those rows retain their own scopes and classifications.

## Koide basepoint and density formulas

The runner independently checks the finite cyclotomic density equality

```text
L_3(1,2) = 2/9
```

and, for the displayed real symmetric circulant family
`F=aI+b(J-I)` with real `a != 0` and `b`,

```text
Tr(F) = 3a,
Tr(F^2) = 3a^2 + 6b^2,
Q(F) = Tr(F^2)/Tr(F)^2 = 1/3 + (2/3)r,
r = b^2/a^2.
```

The points `r=1/2` and `Q=2/3` obey the displayed algebraic relation. Physical
selection of `r`, use of the density as a readout, and assignment of the
circulant spectrum to charged-lepton data remain outside this map's supplied
authority.

## Net standing

1. **Finite character data:** the exact profiles, expectations, orbit, and
   projector matrices above are supplied by the positive 2026-06-15 theorem.
2. **Physical locus:** no physical generation locus is selected here; the
   staggered/KS construction is a named conditional route with its own inputs.
3. **Basepoint:** `r=1/2` is an algebraically distinguished input value, with
   no physical selector supplied here.
4. **Readout:** `L_3(1,2)=2/9` is an exact finite density equality, with no
   physical readout identification supplied here.

This open-gate parent is an integration map, not a physical carrier closure.
It adds no axiom, approved primitive, physical selector, convention, or
imported value.

## Verification

Run:

```bash
python3 scripts/flavor_carrier_from_axioms_momentum_forced_2026_05_31.py
```

Expected:

```text
SCORECARD PASS=15 FAIL=0
```
