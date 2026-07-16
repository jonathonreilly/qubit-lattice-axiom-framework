# DM Leptogenesis PMNS Sole-Axiom Boundary (Finite-Sample Rescope)

**Claim ID:** `dm_leptogenesis_pmns_sole_axiom_boundary_note_2026-04-16`
**Date:** 2026-04-16 (revised 2026-07-16)
**Type:** bounded_theorem
**Status:** bounded support note — exact finite supplied-sample algebra plus a
conditional supplied-map diagnostic
**Script:** `scripts/frontier_dm_leptogenesis_pmns_sole_axiom_boundary.py`

## Question

What does the current packet actually prove after removing the two unsupported
moves in the former note:

1. treating two hand-supplied equal-mean arrays as framework-admissible active
   microscopic points; and
2. treating an imported transport computation against a hard-coded physical
   target as an axiom-level consequence?

## Bottom line

The current packet does not derive an admissible active-source family from the
framework, so it cannot establish a sole-axiom nonuniqueness boundary.

The strongest honest result is narrower:

1. on the finite supplied-sample set `{A,B}`, the exact mean-seed map is
   non-injective;
2. the exact seed-relative five-coordinate map distinguishes and reconstructs
   `A` and `B`;
3. conditional on one explicitly supplied matrix construction, a
   permutation/rephasing-invariant numerical spectral diagnostic differs
   between `A` and `B`.

This is an exact finite supplied-sample algebraic statement and a conditional
downstream numerical-map lemma. It is not a theorem that the historical
`Cl(3)` on `Z^3` phrase, the current four-axiom framework, or the approved
primitive registry supplies either sample.

## Historical versus current axiom scope

The 2026-04-16 version used “sole axiom” to mean the historical `Cl(3)` on
`Z^3` framework phrase. This historical `Cl(3)` on `Z^3` wording does not name
the current foundation surface.

The current framework surface is instead the four named axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

- Lattice;
- Qubit;
- Admissibility;
- Record.

`Cl(3,0)` is now equivalent local-algebra language for the Qubit axiom, not a
separate axiom or a supplier of a PMNS source law. The current memo explicitly
withholds dynamics, transfer operators, source/action identification,
state-selection rules, physical-observable bridges, and selectors.

The three approved primitives are also irrelevant to the missing bridge:

- scale reference supplies units conversion only;
- kinetic isotropy supplies only `c_t = c_s`;
- realized state permits pointwise evaluation at a supplied law-admissible
  state but supplies neither the state nor its contingent values.

Therefore neither the historical wording nor the current four-axiom/approved-
primitive surface supplies the sample arrays, a physical active carrier, a
fixed physical seed pair, a transport law, transport constants, a flavor
selector, a target value, or a physical `eta` readout.

## Exact finite-sample theorem

The runner supplies two rational sample tuples:

```text
A:
  x = (115/100, 82/100, 95/100)
  y = ( 41/100, 28/100, 54/100)
  delta = 63/100

B:
  x = (105/100, 97/100, 90/100)
  y = ( 60/100,  9/100, 54/100)
  delta = 63/100
```

Define the seed map

```text
s(x,y,delta) = (mean(x), mean(y)).
```

Then exact rational arithmetic gives

```text
s(A) = s(B) = (73/75, 41/100).
```

Define the seed-relative five-coordinate encoding

```text
b(x,y,delta)
  = (x1-xbar, x2-xbar, y1-ybar, y2-ybar, delta).
```

The two exact outputs are

```text
b(A) = (53/300, -23/150, 0,      -13/100, 63/100)
b(B) = (23/300,  -1/300, 19/100,   -8/25, 63/100).
```

They are unequal. Moreover, `s` and `b` reconstruct all three coordinates of
`x` and `y` exactly because the third deviations are minus the sums of the
first two. The runner also verifies that `A` and `B` are not related by a
simultaneous coordinate permutation.

Hence the restriction

```text
s | {A,B}
```

is non-injective.

That is the complete unconditional theorem. It proves a fact about the two
supplied samples only. It does not prove that `{A,B}` is contained in a
framework-admissible active-source family.

## Conditional supplied numerical-map lemma

For a separate diagnostic, supply the matrix construction

```text
C = [[0,1,0],
     [0,0,1],
     [1,0,0]]

Y(x,y,delta)
  = diag(x)
    + diag(y1, y2, y3 exp(i delta)) C,

H = Y Y^dagger.
```

No axiom-derived or physical-carrier status is assigned to this construction
here.

Define the normalized spectral diagnostic

```text
Phi(Y) = sort(eigenvalues(H)) / Tr(H).
```

The runner obtains

```text
Phi(A) ~= (0.15596488, 0.23124027, 0.61279486)
Phi(B) ~= (0.12301808, 0.27574837, 0.60123356).
```

Thus `Phi(A) != Phi(B)` under the supplied map. The runner independently
checks that `Phi` is unchanged by:

- simultaneous basis permutation of the carrier matrix;
- arbitrary left/right diagonal rephasing; and
- repeating the identical supplied sample.

The first two invariances hold for every permutation matrix `P` and diagonal
unitaries `L,R`, not only for the representative controls in the runner:

```text
(P Y P^dagger)(P Y P^dagger)^dagger = P H P^dagger,
(L Y R)(L Y R)^dagger               = L H L^dagger.
```

Both transformations preserve the eigenvalues and trace of `H`.

This guards the displayed separation against a raw basis-label or phase
artifact. It still gives no PMNS column selector, no transport functional, and
no physical `eta` readout.

## Hostile controls

The verifier rejects each of the following as a witness for the exact
finite-sample theorem:

- a wrong-seed pair;
- an equal-source duplicate;
- a same-source pair obtained by shifting all `x` and `y` coordinates, because
  its seed changes;
- a pure simultaneous coordinate permutation, because it is a relabeling.

The runner also inspects its own abstract syntax tree and verifies:

- no project-local physics module is imported;
- no load-bearing check uses literal `True`;
- none of the former physical eta constants or hard-coded eta targets is
  referenced.

## Premise and import audit

| Item | Role | Class | Load-bearing? | Disposition |
|---|---|---|---:|---|
| Current Lattice/Qubit/Admissibility/Record axioms | foundation boundary | approved axiom premise | no for the finite algebra; yes if a framework-active interpretation were claimed | do not enlarge; they supply no source/action, carrier, selector, or target |
| Scale-reference primitive | units conversion | approved primitive | no | irrelevant; supplies no dimensionless source or mixing data |
| Kinetic-isotropy primitive | kinetic-form ratio | approved primitive | no | irrelevant; supplies no PMNS source, phase, or selector |
| Realized-state primitive | pointwise evaluation interface | approved primitive | no for the algebra; insufficient for sample admission | supplies neither a state nor the values of `A` or `B` |
| Samples `A` and `B` | witness set | supplied finite data | yes | explicit fixtures; not axiom-derived and not physically admitted |
| Mean and seed-relative maps | exact theorem | elementary rational algebra | yes | derived exactly in the runner |
| Matrix construction `Y` | conditional diagnostic carrier | supplied numerical map | yes only for the conditional lemma | no physical-carrier interpretation |
| NumPy Hermitian eigensolver | numerical evaluation of `Phi` | computation tool | yes only for the conditional lemma | checked with permutation/rephasing controls |
| Transport constants, flavor selector, eta target/readout | former downstream interpretation | unsupported imports | no longer present | removed completely |

## What remains open

A future sole/current-axiom boundary claim would still need all of:

1. a retained derivation from the current four axioms and approved primitives
   to a physically typed active carrier and source family;
2. a proof that two equal-seed, unequal-source points are law-admissible members
   of that derived family rather than supplied fixtures;
3. a retained physical transport law and all required transport constants;
4. a retained flavor-column or other physical selector;
5. a retained target/readout bridge if a physical baryon-asymmetry or `eta`
   statement is intended.

Until those bridges exist, this stable claim row should be read only at the
finite supplied-sample and conditional supplied-map scope above.

## Verification

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_sole_axiom_boundary.py
python3 scripts/frontier_dm_leptogenesis_pmns_sole_axiom_boundary.py --intentional-failure-probe
```

The first command must exit `0`. The intentional failure probe must exit
nonzero.
