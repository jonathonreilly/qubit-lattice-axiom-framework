# Area-Law Conditional Clifford–CAR Algebraic Equivalence Note

**Date:** 2026-04-25
**Repair date:** 2026-07-16
**Stable claim ID:** `area_law_native_car_semantics_tightening_note_2026-04-25`
**Status:** conditional / bounded algebraic equivalence only; no substrate-native
carrier or coframe-response claim
**Runner:** `scripts/frontier_area_law_native_car_semantics_tightening.py`

## Claim boundary

This note proves one finite-dimensional conditional equivalence:

> On a supplied four-dimensional complex Hilbert space `K`, a supplied
> irreducible Hermitian `Cl_4(C)` / Majorana representation is equivalent to a
> two-mode complex CAR Fock representation.

It does **not** derive any of the following:

- invariance of `K=P_A H_cell` under the retained event-cell substrate action;
- four Clifford generators on `P_A H_cell` induced by that substrate;
- a preferred Majorana basis, coframe, parity, normal/tangent orbital pairing,
  dispersion, or Widom carrier;
- the area-law coefficient `1/4` from rank four or from CAR algebra alone.

The historical path and stable claim ID retain the phrase `native_car`, but
the repaired claim is not a native-semantics theorem.

## Conditional algebraic equivalence

Let `K` be a complex Hilbert space with `dim_C K=4`. Assume four supplied
Hermitian operators `gamma_1,...,gamma_4` satisfy

```text
{gamma_i,gamma_j}=2 delta_ij I_K
```

and act irreducibly on `K`. Define

```text
c_1=(gamma_1+i gamma_2)/2,
c_2=(gamma_3+i gamma_4)/2.
```

Then

```text
{c_a,c_b}=0,
{c_a,c_b^dagger}=delta_ab I_K.
```

Conversely, two supplied complex CAR annihilators on `F(C^2)` give four
Hermitian Majoranas by

```text
gamma_1=c_1+c_1^dagger,
gamma_2=-i(c_1-c_1^dagger),
gamma_3=c_2+c_2^dagger,
gamma_4=-i(c_2-c_2^dagger).
```

Their Clifford words span `M_4(C)`. Thus the supplied irreducible
`Cl_4(C)` representation and the supplied two-mode CAR representation are
unitarily equivalent as finite `*`-representations.

This is representation equivalence, not uniqueness of physical response.
Unitary rotations and changes of Majorana pairing produce many valid
generating sets. Nothing here selects one as the substrate coframe or assigns
the two modes to physical edge channels.

## Retained-surface obstruction to the clean bridge

The clean-retention route was tested before narrowing this claim. The exact
obstruction is recorded in
[PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md](./PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md)
and independently replayed by
`scripts/frontier_planck_primitive_clifford_substrate_descent_obstruction.py`.

On the supplied event-cell surface:

```text
P_A H_cell under spatial substrate SU(2): 1 + 3,
irreducible Cl_4(C) module under spatial bivectors: 2 + 2.
```

The simultaneous equivariant intertwiner space has dimension zero. Moreover,
the canonical wedge-plus-contraction Clifford generators on the full exterior
cell do not preserve `P_A`; their compression satisfies

```text
P_A gamma_i P_A = 0
```

while the generators leak out of `P_A H_cell`. Number-preserving bilinears do
generate `M_4(C)` on the active block and can host a `Cl_4(C)` basis, but they
do not select a metric, orientation, phase, coframe basis, or action unit.

Therefore an invariant `P_A` carrier and induced `Cl_4(C)` generators are not
derivable from the currently supplied substrate representation. A positive
theorem needs a changed representation premise or an additional intrinsic
active-block response law.

## Consequence for the area-law packet

This algebraic equivalence can be used only after the Clifford or CAR carrier
has been supplied. In particular, the implication

```text
rank(P_A)=4
  -> supplied irreducible Cl_4(C) response
  <-> supplied F(C^2) CAR response
```

ends at the algebra. It does not imply

```text
normal channel + self-dual tangent channel
```

and it does not imply `c_Widom=1/4`. Those statements require the separate
edge-channel and dispersion axioms made explicit in
[AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md](./AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md).

## Exact open bridges

One of the following would be required for a non-conditional repair:

1. a retained substrate theorem giving a reducing rank-four block whose
   spatial action matches the `2+2` restriction of an irreducible
   `Cl_4(C)` module;
2. an intrinsic active-block theorem selecting a metric-compatible Clifford
   coframe from the available `M_4(C)` bilinear algebra;
3. a retained physical law selecting the Majorana pairing and mapping the two
   CAR modes to the normal and tangent edge dispersions.

None is currently supplied.

## Safe wording

> Conditional on a supplied irreducible `Cl_4(C)` response on a
> four-dimensional active block, the response is algebraically equivalent to
> two-mode complex CAR. The retained event-cell substrate does not presently
> derive that response or the physical edge-channel assignment.

Unsafe wording includes any statement that the rank-four primitive packet is
therefore natively fermionic, that the substrate forces the CAR carrier, or
that this equivalence by itself derives the area-law coefficient.

## Verification

Run:

```bash
python3 scripts/frontier_area_law_native_car_semantics_tightening.py
```

The runner checks the CAR/Clifford equivalence, parity and full-matrix
generation, non-CAR rank-four controls, failure of the natural full-cell odd
Clifford action to reduce to `P_A`, and source-wording firewalls. It exits
nonzero on any failed algebraic or status-boundary check.
