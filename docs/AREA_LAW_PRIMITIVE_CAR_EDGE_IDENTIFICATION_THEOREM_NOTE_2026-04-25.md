# Area-Law Conditional Primitive-CAR Edge-Axiom Coefficient Theorem Note

**Date:** 2026-04-25
**Repair date:** 2026-07-16
**Stable claim ID:** `area_law_primitive_car_edge_identification_theorem_note_2026-04-25`
**Status:** conditional support inside supplied primitive-CAR edge axioms; no
substrate descent, channel forcing, or global carrier-uniqueness claim
**Runner:** `scripts/frontier_area_law_primitive_car_edge_identification.py`

## Claim boundary

This note proves the following bounded implication:

> If the rank-four active block, its two-mode CAR interpretation, one normal
> edge channel, and one self-dual tangent-Laplacian edge channel are supplied,
> then the average crossing count is `3` and the Widom coefficient is exactly
> `1/4`.

Only the rank-to-mode count and the coefficient/measure calculation are
derived. The substrate does not derive the CAR interpretation, and CAR algebra
does not derive the normal/tangent channel assignment or their dispersions.

## Supplied primitive-CAR edge axioms

Let

```text
H_cell ~= C^2_t otimes C^2_x otimes C^2_y otimes C^2_z ~= C^16
```

and let `P_A` be the Hamming-weight-one packet with `rank(P_A)=4`. For a
selected face with normal `e_x`, supply all of:

1. **Exact active support.** The entropy carrier is exactly `P_A H_cell`, with
   no active spectator sector.
2. **Complex-CAR interpretation.** The active algebra is represented as
   `F(C^m)`.
3. **Normal-channel axiom.** One CAR mode is assigned the dispersion
   `epsilon_0(k)=cos(k_x)`, giving two crossings on every transverse fiber.
4. **Tangent-channel axiom.** The other CAR mode is assigned
   `epsilon_1(k)=cos(k_x)+Delta_perp(q)` and is active on the self-dual low
   sheet `Delta_perp(q)<1`.
5. **Tangent-symbol ansatz.** Within the even, tangent-axis-permutation
   symmetric, nearest-neighbor affine-cosine class normalized to range
   `[0,2]`,

   ```text
   Delta_perp(q)=1-(1/n_perp) sum_j cos(q_j).
   ```

These are carrier axioms, not consequences of the current minimal retained
substrate.

## Derived rank-to-CAR statement

Under axioms 1 and 2,

```text
dim F(C^m)=2^m=rank(P_A)=4,
```

so `m=2`. This conclusion is conditional on the complex-CAR interpretation.
A four-dimensional Hilbert space alone also supports ququart and two-qubit
semantics.

The result `m=2` does not label either orbital as normal or tangent. A unitary
rotation of the two CAR orbitals preserves the CAR algebra while changing that
labeling. Axioms 3 and 4 supply the physical assignment.

## Derived half-zone measure

The all-tangent half-period map

```text
tau(q)=q+pi(1,...,1)
```

preserves Haar measure and obeys

```text
Delta_perp(tau q)=2-Delta_perp(q).
```

It exchanges the low and high sheets. The threshold set
`Delta_perp=1` is the zero set of the nonzero real-analytic function
`sum_j cos(q_j)` and therefore has Haar measure zero. Hence

```text
mu{Delta_perp<1}=mu{Delta_perp>1}=1/2.
```

This is exact for the supplied tangent symbol. It is not selected by CAR
algebra itself.

## Derived coefficient

Under the supplied channel axioms:

```text
normal average crossings  = 2,
tangent average crossings = 2*(1/2)=1,
<N_x>                     = 3.
```

Therefore the flat-cut free-fermion Widom coefficient is

```text
c_Widom=<N_x>/12=3/12=1/4.
```

It numerically equals the separate primitive trace

```text
c_cell=Tr((I_16/16)P_A)=4/16=1/4.
```

The equality does not turn one quantity into a derivation of the other.

## Limited classification statements

Among only the four enumerated crossing patterns

```text
normal+empty,
normal+normal,
tangent+tangent,
normal+tangent,
```

with crossing averages `0`, `2`, and `1` assigned as above, only
`normal+tangent` yields `1/4`. This is an enumerated-pattern check, not a
uniqueness theorem over all two-mode CAR Hamiltonians.

Likewise, the displayed `Delta_perp` is unique only inside the supplied
normalized tangent-symmetric nearest-neighbor affine-cosine ansatz. Longer
range symbols, anisotropic symbols, additional pockets, other thresholds, and
orbital mixing are outside that statement.

Indeed, if a second supplied mode is active on a transverse fraction `p`, then

```text
c(p)=(2+2p)/12.
```

CAR algebra permits the family; `c(p)=1/4` only when the additional physical
selector fixes `p=1/2`.

## Retained-surface obstruction and open bridges

The clean substrate bridge fails on the currently supplied event-cell
representation, as established in
[PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md](./PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md):

- `P_A H_cell` carries spatial substrate content `1+3`, whereas an irreducible
  `Cl_4(C)` carrier restricts as `2+2`;
- the exact equivariant intertwiner nullity is zero;
- the canonical full-cell odd Clifford generators leak out of `P_A` and
  compress to zero;
- the intrinsic bilinear algebra can host many Clifford bases but does not
  select one or assign physical dispersions.

Thus the exact remaining gaps are:

1. substrate-to-`P_A` forcing for a compatible Clifford/CAR response, or a
   changed retained representation premise;
2. an intrinsic law selecting a coframe/Majorana pairing on the active block;
3. a physical edge theorem deriving the normal and self-dual tangent
   dispersions, including the half-zone selector, from retained dynamics.

Until those gaps close, `1/4` is valid only inside the supplied primitive-CAR
edge axioms above.

## Relation to the algebraic companion

[AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md](./AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md)
now states only the conditional finite-algebra equivalence

```text
irreducible Cl_4(C) on C^4 <-> two-mode complex CAR.
```

It supplies no substrate-native implication and no channel assignment.

## Safe wording

> Inside the explicitly supplied primitive-CAR support, normal-channel,
> tangent-channel, and tangent-symbol axioms, the rank-four block has two CAR
> modes and the Widom coefficient is exactly `1/4`. The substrate-to-carrier
> and carrier-to-dispersion bridges remain open.

Unsafe wording includes any claim that rank four or CAR alone forces the
normal-plus-tangent carrier, that the displayed carrier is globally unique, or
that the current retained substrate derives the coefficient.

## Verification

Run:

```bash
python3 scripts/frontier_area_law_primitive_car_edge_identification.py
```

The runner checks the conditional rank count, exact half-zone involution,
finite-grid pair controls, coefficient calculation, alternative selector
fractions and channel patterns, and source-wording firewalls. It exits nonzero
on any failed mathematical or claim-boundary check.
