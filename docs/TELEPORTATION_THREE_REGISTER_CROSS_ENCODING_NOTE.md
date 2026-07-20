# Teleportation Three-Register Cross-Encoding Note

**Date:** 2026-04-25
**Type:** bounded_theorem
**Runner:** `scripts/frontier_teleportation_three_register_cross_encoding.py`

This is author-side exact support source material for a finite ideal logical
algebra. It declares no audit verdict; audit status remains pipeline-derived
after independent review.

## Scope

This note records the next bounded artifact for the native taste-qubit
teleportation lane: three independently chosen encodings for the input,
Alice's Bell-resource half, and Bob's Bell-resource half.

```text
A = Alice unknown input encoding
R = Alice Bell-resource-half encoding
B = Bob Bell-resource-half encoding
```

The stated surface remains the Kogut-Susskind cell/taste factorization:

```text
C^(side^dim) = C^((side/2)^dim cells) tensor C^(2^dim tastes)
```

This is only the ideal finite-dimensional logical teleportation identity. It
does not claim a physical teleportation implementation, apparatus or resource
preparation, Hamiltonian or matter transport, noise tolerance, durable-record
production, an unbounded-lattice result, mass, charge, or energy transfer,
object transport, or faster-than-light signaling.

## Map Requirements

The two-register cross-encoding artifact assumed Alice's input register and
Alice's resource half used the same encoding.  This runner removes that
assumption and classifies three requirements for each surveyed `(A, R, B)`
triple.

```text
A->R map:
  Needed when Alice's input support differs from Alice's resource-half support.
  The site-basis partial isometry is |0_R><0_A| + |1_R><1_A|.

Adapted Bell measurement:
  Needed when A/R require cross-register Bell pairing or when either A or R
  does not admit the current fixed last-axis pair-hop X as logical X.

R->B resource map:
  Needed when Alice's resource-half support differs from Bob's resource-half
  support.  The intended first-artifact logical coefficient map is identity;
  the site-basis partial isometry is |0_B><0_R| + |1_B><1_R|.
```

The intended surface uses canonical logical Pauli operators in each ordered
logical basis, an explicit A/R Bell pairing, an identity logical resource map,
and axis-adapted Bob corrections.  The failure controls remove one requirement
at a time.

## Closed Logical Derivation

The finite survey below is not the load-bearing proof that unsampled triples
should pass.  The exact reason is the two-dimensional teleportation identity
conjugated by the three encoding isometries. Its premises factor by register,
so they can be checked exhaustively on the
`1 + 2 + 4 + 16 + 12 + 96 = 131` individual default encodings instead of
sampling the
`1^3 + 2^3 + 4^3 + 16^3 + 12^3 + 96^3 = 890633` ordered triples.

For any valid encoding `E in {A, R, B}` on this surface, let

```text
V_E : C^2 -> H_E
V_E |j> = |e_j>, j=0,1
P_E = V_E V_E^dag
```

where `|e_0>, |e_1>` are the ordered site-basis support vectors selected by
the runner.  The canonical logical operators are

```text
Z_E = V_E Z V_E^dag
X_E = V_E X V_E^dag
```

on `H_E`.  The runner's sign canonicalization makes the restricted matrices
exactly the standard Pauli `Z` and the axis-adapted Pauli `X` in this ordered
logical basis.  Site conversion between two encodings is the partial isometry

```text
M_{F<-E} = V_F V_E^dag,
M_{F<-E}^dag M_{F<-E} = P_E,
M_{F<-E} M_{F<-E}^dag = P_F.
```

Thus the explicit `A->R` Bell-pairing map and `R->B` resource map reduce to
the identity matrix after both sides are expressed in their ordered logical
bases.

The adapted Alice Bell projectors are

```text
pi_zx = (1/4) (I + (-1)^x Z tensor Z) (I + (-1)^z X tensor X)
Pi_zx^AR = (V_A tensor V_R) pi_zx (V_A^dag tensor V_R^dag)
```

for `z,x in {0,1}`.  The two joint observables `Z tensor Z` and `X tensor X`
are commuting Hermitian involutions: the two local Pauli anticommutations
cancel in their tensor product. The four explicit Bell vectors defined below
form an orthonormal basis with the four displayed joint-eigenvalue pairs, so
the four `pi_zx` are rank-one orthogonal projectors summing to `I_4`. The
embedded projectors therefore sum to
`P_A tensor P_R` and are the correct Bell measurement on the two encoded
Alice-side supports.

Let the standard logical Bell vector be

```text
|Phi> = (1/sqrt(2)) sum_{j=0}^1 |j> tensor |j>.
```

The intended identity logical resource is its `R,B` encoding,

```text
|Phi_I>_RB = (V_R tensor V_B)|Phi>
           = (1/sqrt(2)) sum_{j=0}^1 V_R |j> tensor V_B |j>.
```

Define the normalized logical Bell vector

```text
|beta_zx> = (I tensor X^x Z^z) |Phi>.
```

For an arbitrary input `|psi> = alpha |0> + beta |1>`, direct contraction of
the Alice-side Bell bra gives the branch map

```text
(<beta_zx|_AR tensor I_B)
  (|psi>_A tensor |Phi>_RB)
  = (1/2) X^x Z^z |psi>_B,

(Pi_zx^AR tensor I_B) (V_A |psi> tensor |Phi_I>_RB)
  = (1/2) (V_A tensor V_R)|beta_zx> tensor V_B X^x Z^z |psi>.
```

For `(z,x)=(1,1)`, reversing the displayed Pauli order changes only a global
minus sign. Each Bell branch therefore has probability `1/4`. Bob's
axis-adapted correction

```text
C_zx^B = V_B Z^z X^x V_B^dag
```

maps the normalized branch density to

```text
V_B |psi><psi| V_B^dag.
```

Indeed `Z^z X^x X^x Z^z = I`; hence the corrected branch map is exactly
`I/2` before normalization, independently of `A`, `R`, and `B`.

Before Alice's two classical bits are received, Bob's branch-averaged state is
the Pauli twirl

```text
sum_{z,x} (1/4) V_B X^x Z^z |psi><psi| Z^z X^x V_B^dag
  = V_B (I/2) V_B^dag,
```

which is independent of the input.  Bob's pre-measurement marginal is the same
`V_B (I/2) V_B^dag` because `|Phi_I>_RB` is maximally entangled on the logical
`R,B` coordinates.

The full `2 x 2` operator space is a four-dimensional complex vector space
with matrix-unit basis `|j><k|`; density matrices form a convex subset of that
space. Checking each Bell branch channel, its correction, and the Pauli twirl
on those four units therefore proves the density-operator statements for
every mixed input as well as every pure input. No random-state completeness
assumption is used.

This proves the intended ideal protocol for every valid ordered `(A,R,B)`
encoding triple produced by the runner's KS taste-qubit encoding definition on
the stated geometry surface. The runner separately exhausts all 131 default
encoding isometries and canonical logical-Pauli pairs, checks the logical Bell
projectors, branch channels, corrections, and twirl on a spanning operator
basis, and reports the 890633-triple Cartesian-product coverage. The 1609
sampled triple trials remain replayable telemetry for the enumerator,
projector construction, no-signaling metrics, and negative controls; the
512-triple cap is not the derivation boundary for the axis-adapted logical
protocol.

The control boundaries follow by removing one premise from the derivation:

- without the explicit `A->R` partial isometry, different Alice-side supports
  do not have a site-basis Bell pairing;
- with fixed last-axis Bell `X`, the Bell projectors are correct only on
  encodings where that fixed operator restricts to the canonical logical `X`
  on both Alice-side registers;
- with fixed Bob `X`, the correction is correct only when that operator
  restricts to Bob's canonical logical `X`;
- with a wrong logical `R->B` resource map, the no-message Bob marginal is
  still input-independent, but the post-message state is the wrong logical
  image of `|psi>`.

## Default Run

Command:

```bash
python3 scripts/frontier_teleportation_three_register_cross_encoding.py
```

Default audit surface:

```text
dimensions: 1, 2, 3
side lengths: 2, 4
valid KS geometries: 6
encoding supports: 131
possible A/R/B triples: 890633
surveyed A/R/B triples: 1609
random trials per surveyed triple: 4
max triples per geometry: 512
tolerance: 1e-12
```

Exhaustive factorized structural certificate:

```text
encoding supports enumerated from the closed-form count: 131/131
ordered encoding isometries certified: 131/131
distinct ordered encoding supports certified: 131/131
canonical logical Pauli pairs certified: 131/131
ordered A/R/B triples covered by the factorized theorem: 890633/890633
max V_E^dag V_E-I error: 0.000e+00
max P_E^2-P_E error: 0.000e+00
max canonical Z_E-Z error: 0.000e+00
max canonical X_E-X error: 0.000e+00
max logical Pauli square error: 0.000e+00
max logical Pauli anticommutator error: 0.000e+00
rank-one logical Bell projectors certified: 4/4
max logical Bell-projector resolution error: 0.000e+00
max logical Bell-projector idempotence error: 0.000e+00
max logical Bell-projector orthogonality error: 0.000e+00
max logical Bell-projector outer-product error: 1.110e-16
max logical Bell-branch map error: 1.110e-16
max logical branch-channel error on the matrix-unit basis: 1.110e-16
max corrected logical branch-map error: 1.110e-16
max corrected channel error on the matrix-unit basis: 1.110e-16
max Pauli-twirl error on the matrix-unit basis: 0.000e+00
```

The algebraic residuals are zero except where a normalized Bell vector
contributes the binary floating-point representation of `1/sqrt(2)`. Those
`1.110e-16` residuals are roundoff; the contractions above give the exact
coefficients `1` and `1/2`.

Geometry counts:

```text
dim=1 side=2: 1 encodings, 1/1 triples surveyed
dim=1 side=4: 2 encodings, 8/8 triples surveyed
dim=2 side=2: 4 encodings, 64/64 triples surveyed
dim=2 side=4: 16 encodings, 512/4096 triples surveyed
dim=3 side=2: 12 encodings, 512/1728 triples surveyed
dim=3 side=4: 96 encodings, 512/884736 triples surveyed
```

Requirement classification over the surveyed triples:

```text
A input -> R Alice-resource-half:
  no site conversion needed: 330
  explicit A->R site maps needed: 1279
  in-cell retaste: 809
  relocation plus retaste: 391
  relocation only, same taste pair: 79

R Alice-resource-half -> B Bob-resource-half:
  no site conversion needed: 321
  explicit R->B resource site maps needed: 1288
  in-cell retaste: 807
  relocation plus retaste: 387
  relocation only, same taste pair: 94

Bell-measurement adaptation:
  cross-register A/R Bell pairing required: 1279
  axis-adapted Bell X required: 1267
  adapted Bell measurement required by either condition: 1485
  fixed last-axis Bell X sufficient: 342

Combined site maps:
  no A->R or R->B site maps needed: 131
  both A->R and R->B site maps needed: 1089
  max partial-isometry error: 0.000e+00
```

## Numerical Results

Axis-adapted three-register maps:

```text
teleportation/no-signaling pass: 1609/1609
minimum corrected-state fidelity: 0.9999999999999996
maximum infidelity: 6.661e-16
max branch probability error from 1/4: 2.220e-16
max total probability error from 1: 8.882e-16
max Bob trace distance to I/2 before Alice measurement: 4.441e-16
max Bob trace distance to I/2 after Alice measurement before message: 4.163e-16
max pairwise pre-message Bob-state distance across inputs: 4.718e-16
max corrected-state trace error: 2.220e-16
Bell outcomes seen: Phi+, Phi-, Psi+, Psi-
```

Missing A->R conversion control:

```text
expected pass cases: 330/1609
teleportation/no-signaling pass: 330/330 run
skipped before teleportation: 1279
failure cause: missing_explicit_a_to_r_site_conversion=1279
minimum corrected-state fidelity on runnable cases: 0.9999999999999998
maximum infidelity on runnable cases: 6.661e-16
```

Non-adapted Bell-measurement control:

```text
expected pass cases: 342/1609
teleportation/no-signaling pass: 342/342 run
skipped before teleportation: 1267
failure causes:
  a_and_r_bell_x_not_axis_adapted=673
  a_bell_x_not_axis_adapted=282
  r_bell_x_not_axis_adapted=312
minimum corrected-state fidelity on runnable cases: 0.9999999999999996
maximum infidelity on runnable cases: 6.661e-16
```

Non-adapted Bob-correction control:

```text
expected pass cases: 642/1609
teleportation/no-signaling pass: 642/1609
failure cause: bob_fixed_pairhop_x_zero_on_encoding=967
minimum corrected-state fidelity: 0.0000000000000000
maximum infidelity: 1.000e+00
max corrected-state trace error: 1.000e+00
Bob pre-message input-independence still holds to 5.274e-16
```

Wrong B resource-conversion control:

```text
expected pass cases: 0/1609
teleportation/no-signaling pass: 0/1609
failure cause: wrong_b_resource_conversion_map=1609
minimum corrected-state fidelity: 0.0000000134850124
maximum infidelity: 1.000e+00
max corrected-state trace error: 2.220e-16
Bob pre-message input-independence still holds to 4.996e-16
```

The runner reported `PASS` for:

- exhaustive encoding-isometry premises;
- distinct ordered encoding supports;
- exhaustive canonical logical-Pauli premises;
- logical Bell-projector algebra;
- logical branch and correction channels on the matrix-unit basis;
- the logical Pauli twirl on the matrix-unit basis;
- factorized coverage of all default ordered encoding triples;
- axis-adapted three-register maps;
- all four Bell outcomes represented;
- Bob pre-message reduced-state input-independence;
- missing A->R conversion control;
- non-adapted Bell-measurement boundary;
- non-adapted Bob-correction control;
- wrong B resource-conversion control.

## Interpretation

On the stated default encoding family, the obstruction is not three-register
cross-encoding itself. The factorized certificate covers all 890633 ordered
triples. The sampled telemetry agrees: the intended logical protocol passes
when the A/R Bell measurement is explicitly adapted to the two Alice-side
encodings and Bob's corrections are adapted to Bob's chosen encoding.

The first new requirement is A->R Bell pairing.  If Alice's unknown input and
Alice's resource half occupy different encoded site supports, the Bell
measurement needs an explicit site partial isometry to define which ordered
logical basis states are paired.

The second requirement is Bell-measurement adaptation.  The current fixed
pair-hop X remains a last-axis convention.  It is sufficient only when both A
and R use encodings where the fixed pair-hop restricts to logical X.

The third requirement is the R->B resource map.  If R and B differ, the Bell
resource must be prepared with the matching site partial isometry.  The wrong
B-side bit-swap control shows that Bob can still see an input-independent
pre-message state while post-message fidelity fails.

## Limitations

This is a finite algebraic theorem over dimensions 1, 2, and 3 with side
lengths 2 and 4 by default. The closed logical derivation and exhaustive
per-encoding structural certificate cover every valid ordered encoding triple
generated by the runner's definition on this surface. The default numerical
trial layer still caps the three-register product at 512 triples per geometry,
so its printed requirement classifications and failure-control telemetry are a
deterministic bounded survey rather than an exhaustive count over all 890633
possible default triples. Use `--max-triples-per-geometry 0` for exhaustive
telemetry when the requested geometry set is small enough.

Odd side lengths remain outside the stated KS cell/taste factorization.
Larger even lattices can be requested but are not claimed by the default run.

The Bell resource, Bell measurement, conversion maps, and Bob corrections are
ideal logical objects.  The runner does not derive a physical resource
preparation channel, measurement apparatus, durable record, Hamiltonian
transport, noise model, readout model, physical teleportation implementation,
or unbounded-lattice result.
