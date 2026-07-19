# Proper-cubic hard-core many-field reservoir vertex — Cycle 421

Date: 2026-07-19
Authority: none
Audit: unset

## Construction

Cycle 421 replaces the Cycle-418 vacuum-only creation operator by the hard-core scalar ladder

```text
A^dagger = (1/sqrt(6)) sum_d sigma_d^+,
A = (A^dagger)^dagger.
```

On each of the six field M2s, `sigma_d^+` creates only when that directional bit is blank. Therefore `A^dagger` acts nontrivially on **every nonsaturated computational field occupation**, from field number zero through five; `A` acts nontrivially on every nonvacuum computational occupation, from one through six. Creation vanishes exactly at saturation and annihilation vanishes exactly at vacuum.

With one reservoir M2, the **fixed seven-M2 Hermitian generator** is

```text
H_hc = sigma_R^- A^dagger + sigma_R^+ A,
G_hc(theta) = exp(-i theta H_hc),
theta = 0.36272452333990834.
```

Each summand is a two-M2 reservoir/direction exchange; the fixed finite gate has a bounded seven-M2 union. Primitive synthesis of the noncommuting star exponential remains supplied/open.

## Exact controls

The generator commutes with **reservoir-plus-field excitation number** `Q=R+F`. The runner checks Hermiticity, the finite unitary and adjoint inverse on **all 128 basis states**, the operator identity

```text
G_hc^dagger F G_hc - F + G_hc^dagger R G_hc - R = 0,
```

and number expectation on every computational occupation. It separately checks emission from each reservoir-occupied, nonsaturated field state and absorption from each reservoir-empty, nonvacuum field state. Saturated emission and vacuum absorption vanish.

Coupling deletion (`theta=0`) is exact identity. Deleting one directional ladder term visibly breaks both the scalar seed and a frame that moves that direction.

## Cycle-418 seed preservation

On the two-dimensional subspace

```text
|R=1,F=000000>,  -|R=0,s_F>,
s_F=(1/sqrt(6)) sum_d |1_d>,
```

the new generator is exactly the Cycle-418 exchange generator. Thus the signed Cycle-418 vacuum seed, `E G_416 = G_hc E` intertwiner, adjoint inverse, zero leakage, and transfer `sin^2(theta)=0.1258992161287138` are preserved. This is tested directly rather than inferred from the vacuum result.

The equal-weight ladder is invariant under permutations of the six directions. Its generator and finite gate commute with all 24 proper-cubic frames.

## Two independent vertices and prior seam comparison

Two independent copies start in

```text
|R=1,F=0> tensor |R=1,F=0>,
Q_total=2.
```

Applying `G_hc tensor G_hc` produces a genuine two-field sector with weight

```text
sin^4(theta) = 0.01585061262182459,
```

zero `Q_total=2` leakage, and an exact adjoint inverse. This sector contains simultaneous hard-core field excitations in two independent blocks and is not a global zero/one-field blockade.

The earlier two-tick candidate reported two-field weight `0.002201473975253681` and missing conjugate source coordinate `-0.15248255286187232`. The present independent-vertex weight is larger by `0.013649138646570908`, a ratio of approximately `7.2`. This is an explicit diagnostic comparison, not a match: the preparations and schedules differ. Cycle 421 contains no carried source coordinate, so the prior missing source-coordinate seam is not closed here.

## M64 spectator/contact join

One complete M64 matter cell is joined as an identity spectator, giving an 8,192-state matter-reservoir-field operator. The runner checks sparse unitarity on that complete basis, zero matter-block leakage, and exact commutation with the intrinsic contact phase

```text
exp[i g N(N-1)/2].
```

This tests compatibility with the contact fixture. It does not create matter control, recoil, or source work.

## Supplied, derived, and open

Supplied:

1. the Cycle-418 signed vacuum seed and fixed angle;
2. one reservoir M2 and six ordinary hard-core directional field M2;
3. the equal-weight permutation-scalar hard-core raising convention;
4. one M64 matter spectator, intrinsic contact phases, and proper-cubic representations;
5. two independently prepared reservoir excitations for the `Q_total=2` control.

Derived:

1. a fixed Hermitian seven-M2 generator acting on every creatable or annihilable computational occupation;
2. exact all-basis unitarity/inverse and the `R+F` number ledger;
3. preservation of the Cycle-418 vacuum seed/intertwiner/transfer;
4. occupation, saturation, deletion, and all-24-frame controls;
5. genuine two-field output from two independent vertices.

Open:

1. normalization or selection of this ladder as a physical source law;
2. field coin/stream, carried reservoir, repeated same-block history, matter recoil, and source work;
3. closure of the prior missing source coordinate and reconciliation with its different two-tick schedule;
4. energy/stress/gravity interpretation, actual Records, physical time, and metric response.

The conserved coordinate is number, **not energy, stress, or a gravity source**. No generator is called a rate; no schedule is called time; no coherent label is called a Record. This is a constructive candidate with no negative, minimum-content, shared-obstruction, or axiom-pressure claim.
