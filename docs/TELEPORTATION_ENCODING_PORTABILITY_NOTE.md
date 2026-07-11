# Taste-Qubit Encoding Portability Note

**Date:** 2026-04-25
**Type:** bounded_theorem
**Status:** `proposed_retained` for the finite ideal operator-targeting theorem;
independent audit is required before any effective retained status
**Runner:** `scripts/frontier_teleportation_encoding_portability.py`

## Scope

This note records a finite portability audit for the encoded taste-qubit
teleportation artifact.  It uses the same Kogut-Susskind cell/taste surface as
`scripts/frontier_teleportation_protocol.py` and
`scripts/frontier_bell_inequality.py`:

```text
C^(side^dim) = C^((side/2)^dim cells) tensor C^(2^dim tastes)
```

Only even side lengths in dimensions 1, 2, and 3 are audited.  The audit checks
every available cell, every spectator taste assignment, and every logical taste
axis for the requested geometries.

This remains ordinary quantum state teleportation on ideal encoded taste-qubit
registers.  It is not matter teleportation, mass transfer, charge transfer, or
faster-than-light transport.

## Operator Sets

The runner compares two operator sets.

```text
current_fixed_x:
  Z = sublattice parity = I_cells tensor xi_5
  X = row-major pair-hop = I_cells tensor sigma_x on the last taste axis

axis_adapted_x:
  Z = sublattice parity
  X = I_cells tensor sigma_x on the selected logical taste axis
```

The second set is a control: it shows what works if the taste `X` operator is
retargeted to the selected logical axis.  It is not a claim that the current
fixed pair-hop gate already implements every logical axis.

## Finite Operator-Targeting Theorem

For every audited dimension `d in {1,2,3}`, even side length
`L in {2,4,6,8}`, cell, spectator assignment, and selected logical taste axis
`a`, the following statements hold:

1. sublattice parity restricts to a signed logical `Z`;
2. the row-major pair-hop restricts to logical `X` with zero leakage if and
   only if `a=d-1`;
3. for `a != d-1`, its restriction is zero and its Frobenius leakage is
   exactly `sqrt(2)`;
4. the axis-adapted taste flip restricts to logical `X` with zero leakage for
   every `a`.

Consequently, the fixed operator passes exactly `470` of the `1330` audited
encodings and fails the other `860`, whereas the adapted operator passes all
`1330`. This is a theorem about the declared finite ideal operator surface,
not a theorem about physical teleportation apparatus or dynamics.

### Proof

For a fixed cell `c`, selected logical taste axis `a`, and spectator taste bits
`s_k` on all axes `k != a`, the checked two-dimensional encoded subspace is

```text
|0_L> = |c> tensor |eta_a=0, eta_k=s_k for k != a>
|1_L> = |c> tensor |eta_a=1, eta_k=s_k for k != a>.
```

The sublattice-parity operator gives

```text
Z |b_L> = (-1)^(b + sum_{k != a} s_k) |b_L>,
```

so the restricted operator is `(+/-) Z_logical` for every checked cell, axis,
and spectator choice.  The spectator-dependent sign is the sign-count effect
reported below; it is not a portability obstruction.

It remains to derive which taste bit the current row-major pair-hop flips.
With the runner's coordinate order, the row-major index of
`x_j = 2 c_j + eta_j` is

```text
r(x) = sum_{j=0}^{d-1} x_j L^(d-1-j).
```

Because `L` is even, every `L^(d-1-j)` with `j<d-1` is even. Separating the
last coordinate therefore gives

```text
r(2c+eta) = 2 q(c, eta_0,...,eta_{d-2}) + eta_{d-1},

q = sum_{j<d-1} c_j L^(d-1-j)
    + sum_{j<d-1} eta_j L^(d-1-j)/2
    + c_{d-1}.
```

Here `q` is an integer independent of `eta_{d-1}`. The runner's pair-hop
exchanges row-major basis indices `2q` and `2q+1`; hence it preserves `c` and
all earlier taste bits and flips only `eta_{d-1}`. Thus

```text
X_fixed |c> tensor |eta_0,...,eta_{d-1}>
  = |c> tensor |eta_0,...,1 - eta_{d-1}>.
```

Therefore, when the selected logical axis is the last axis `a=d-1`,
`X_fixed |0_L> = |1_L>` and `X_fixed |1_L> = |0_L>`, giving the required
logical `X`.  When `a != d-1`, the last taste bit is a spectator.  Then

```text
X_fixed |b_L>
  = |c> tensor |eta_a=b, eta_{d-1}=1-s_{d-1},
                eta_k=s_k for k != a,d-1>,
```

which is orthogonal to the selected encoded subspace because the spectator
assignment has changed while the logical bit has not.  Hence the restricted
operator is exactly

```text
P_encoded X_fixed P_encoded = 0
```

for every non-last-axis encoding in dimensions 2 and 3. More explicitly,
`X_fixed` is unitary and maps both orthonormal encoded basis columns into the
orthogonal spectator sector, so

```text
||(I-P_encoded) X_fixed P_encoded||_F^2
  = Tr(P_encoded X_fixed^dagger (I-P_encoded) X_fixed P_encoded)
  = Tr(P_encoded) = 2.
```

The leakage diagnostic is therefore exactly `sqrt(2)`. With the restricted
`X` equal to zero, the Bell-projector candidates collapse to duplicated
half-projectors:

```text
P_zx = (1/4) (I + (-1)^x Z tensor Z),
```

because the `X tensor X` stabilizer factor vanishes. Writing
`A_x = I + (-1)^x Z tensor Z`, one has `A_x^2=2A_x`, and therefore
`P_zx^2-P_zx=-A_x/8`. Since the nonzero diagonal entries of `A_x` are `2`,
the maximum-entry idempotence error is `1/4`. The two candidates with the same
`x` are identical, so their product also has maximum entry `1/4`; this is the
duplicate-branch orthogonality error reported by the runner.

Retargeting `X` to `I_cells tensor sigma_x` on the selected axis replaces the
last-bit flip in the displayed formula by an `a`-bit flip.  It therefore maps
`|0_L>` and `|1_L>` into each other for every checked cell, spectator, and
logical axis. This accounts for the finite-surface operator-targeting result
surveyed here without claiming that the current fixed pair-hop implements every
logical axis.

Finally, the enumeration is fixed by the declared audit surface. For dimension
`d` and side `L`, there are `(L/2)^d` cells, `d` logical axes, and `2^(d-1)`
spectator assignments. Summing over `L=2,4,6,8` gives

```text
d=1: 10 cases,
d=2: 120 cases = 60 per axis,
d=3: 1200 cases = 400 per axis,
total: 1330 cases.
```

Exactly one axis per dimension is the last axis, so the fixed-hop pass count
is `10 + 60 + 400 = 470`, leaving `1330 - 470 = 860` non-last-axis failures.
The adapted flip passes every term in the same count. This proves the stated
finite classification; the runner supplies an independent matrix-level replay
of each case. □

## Default Run

Command:

```bash
python3 scripts/frontier_teleportation_encoding_portability.py
```

Default audit surface:

```text
dimensions: 1, 2, 3
side lengths: 2, 4, 6, 8
valid KS geometries: 12
skipped geometries: 0
cell sets across geometries: 140
encoding cases: 1330
random teleportation trials per accepted encoding: 8
tolerance: 1e-12
```

Pass counts by dimension and logical axis:

```text
dim axis  current_fixed_x  axis_adapted_x
1   0     10/10            10/10
2   0     0/60             60/60
2   1     60/60            60/60
3   0     0/400            400/400
3   1     0/400            400/400
3   2     400/400          400/400
```

Aggregate results:

```text
current_fixed_x:
  logical Pauli pass: 470/1330
  Bell-projector gate pass: 470/1330
  teleportation/no-signaling pass: 470/470 run
  skipped before teleportation: 860
  failure cause: current_pair_hop_x_flips_last_axis_not_logical_axis=860
  zero X-restriction failures: 860
  exact non-last-axis obstruction certificates: 860/860
  max failed-case X leakage: 1.414e+00
  max failed-case Bell-projector idempotence/orthogonality error: 2.500e-01
  minimum corrected-state fidelity on accepted encodings: 0.9999999999999996
  maximum infidelity on accepted encodings: 8.882e-16
  max Bob pre-message pairwise trace distance: 4.441e-16

axis_adapted_x:
  logical Pauli pass: 1330/1330
  Bell-projector gate pass: 1330/1330
  teleportation/no-signaling pass: 1330/1330
  failure causes: none
  max Z leakage: 0.000e+00
  max X leakage: 0.000e+00
  minimum corrected-state fidelity: 0.9999999999999996
  maximum infidelity: 8.882e-16
  max Bob pre-message pairwise trace distance: 4.996e-16
```

The restricted `Z` operator is a signed logical Pauli on all surveyed
encodings.  The sign depends on spectator parity:

```text
Z sign counts across all cases: -1=660, +1=670
```

That sign does not break the same-encoding teleportation gates because it
cancels in the two-register Bell stabilizers and contributes at most a global
phase to the corresponding Pauli correction.

## Interpretation

The current fixed-cell encoding generalizes in these bounded senses:

- the fixed 3D side-4 cell `(0,0,0)` case extends to every surveyed cell;
- spectator taste bits need not be fixed to zero;
- the same fixed pair-hop `X` works in each surveyed dimension and side length
  when the logical taste axis is the last axis;
- the accepted encodings pass logical-Pauli restrictions, Bell-projector
  gates, corrected-state teleportation, and Bob pre-message no-signaling gates
  to numerical precision.

The current fixed-cell encoding fails in this bounded sense:

- in dimensions 2 and 3, selecting a non-last logical taste axis while keeping
  the current row-major pair-hop `X` does not produce a logical `X`;
- the pair-hop flips the last taste bit instead of the selected logical bit;
- for those 860 cases, the `X` restriction to the selected two-dimensional
  encoded subspace is zero and the operator leaks out of the subspace with
  norm `sqrt(2)`;
- the resulting Bell-projector candidates are not valid projectors, with
  worst idempotence and orthogonality errors `2.500e-01`.

The axis-adapted control shows that this is an operator-targeting failure, not
a cell or spectator obstruction: using `I_cells tensor sigma_x` on the selected
logical taste axis passes all 1330 surveyed encodings.

## Limitations

This is a finite algebraic audit.  It does not cover odd side lengths, because
the audited KS cell/taste factorization requires even side length.

The default run covers only dimensions 1, 2, and 3 and side lengths 2, 4, 6,
and 8.  Larger even lattices are not claimed by this run.

Each test uses the same encoding for Alice's input register, Alice's Bell-half
register, and Bob's Bell-half register.  The audit does not test cross-cell,
cross-axis, or cross-spectator teleportation maps.

The Bell resource, Bell measurement, and correction gates are ideal logical
objects.  The audit does not derive a physical measurement apparatus, durable
record channel, resource-preparation channel, Hamiltonian transport, noise
model, or readout error model.

No matter, mass, charge, energy, or object is teleported.  Only an unknown
quantum state on Bob's already-present encoded taste-qubit register is
reconstructed after the classical Bell record is available.

## Coordinated Algebraic Closure (2026-05-07)

The finite operator-targeting result documented above is now subsumed by a
single algebraic theorem (T5 in the companion closure note):

  current_fixed_x in RALA(a) iff a = d - 1.

See [`TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md`](TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md)
(runner `scripts/frontier_teleportation_retained_axis_operator_algebra_closure.py`)
for the proof. The closure note supplies bounded algebraic theorem support
for the finite operator-targeting content of this note rather than only a
case-by-case audit; the
physical-implementation gate (apparatus, noise, durable record, dynamical
preparation) remains open.

## Downstream Boundary Alignment (2026-06-13)

The runner reports the audited downstream teleportation boundary stack as
non-gating context. Those rows include the retained-axis operator-algebra
closure, cross-encoding maps, three-register cross-encoding, no-signaling,
3D-operator, conclusion, measurement, resource, and causal-channel anchors
needed by the broader planning stack. Their status does not enter this
standalone theorem's exit code: the finite operator-targeting result depends
only on the displayed algebra and its matrix replay, not on whether physical
implementation or cross-encoding consumers have themselves closed.

This alignment keeps the result bounded. It supports finite even-side encoding
portability and operator targeting on the audited state-teleportation surface,
but it still does not derive odd-side behavior, a physical apparatus,
resource-preparation dynamics, durable records, matter transport, or
nature-grade closure.
