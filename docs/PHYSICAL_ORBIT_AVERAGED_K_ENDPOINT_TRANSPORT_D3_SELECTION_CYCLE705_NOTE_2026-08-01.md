# Orbit-averaged K-endpoint transport and the derived D3 selection rule (Cycle 705)

Date: 2026-08-01
Claim type: bounded_theorem
Status: unaudited (fresh note, paired runner below).

## Dependencies

Landed and unaudited:

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700 operational source-response-readout chain](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [Cycle 696 joined compiler tournament](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)

Backticked context only, with no links: the compiler module
`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py` and its own
dependency `c576`, from which the 24 proper cubic frames are taken; and the open,
unlanded `Cycle 701`, `Cycle 702`, `Cycle 703`, `Cycle 704`.

## Setting

The Cycle-696 compiler executes one chain end to end: a supplied source is turned into
a response, the response into a site metric `I + h`, the metric into a site coframe by
the principal symmetric square root, the coframe into per-axis open finite-difference
parts, the parts into the declared trace `K`, and `K` into an endpoint Hamiltonian whose
one-excitation unitary is read out per site. Every stage used below is that landed
function; nothing in the chain is reimplemented here.

Cycle 700 measured that this chain does not carry one covariance scope but two. Its
carrier table reads

> | coframe carrier | 6 of 24 | 18 explicit out-of-scope witnesses |

against, for the scalar prediction carrier,

> | scalar six-neighbour carrier | 24 of 24 | anisotropic spread `0.05650461860052066` |

and it identified the smaller scope explicitly:

> The Cycle-696 compiler's well-posed covariance scope of six frames is exactly the
> body-diagonal stabilizer D3, isomorphic to S3: the six frames are
> `[1, 4, 9, 15, 18, 23]`, they are closed under product and inverse, their orders are
> `{1:2, 4:2, 9:2, 15:3, 18:3, 23:1}`, [...]

Quoted from an open, unlanded PR, the Cycle-702 boundary names the opening executed
here:

> (f) This cycle does not reunify Cycle 700's two carriers, and it does not re-derive any Cycle-696 prediction row through an averaged carrier.

This cycle does not reunify those carriers either. What it does is locate the split: it
pushes the orbit-averaged carrier through the remainder of the landed chain and shows
that the six-frame restriction is not a property of the carrier at all, but of one
declared contraction downstream of it, and that the six frames which survive are forced.

## Construction

Let `R` be one of the 24 proper cubic frames, a signed permutation with determinant
`+1`. Read its ROW form

    R[i, a] = s_i * delta_{a, p(i)},   p a permutation of {0, 1, 2},  s_i in {+1, -1},

so `p[i] = argmax_a |R[i, a]|` and `s[i] = R[i, p[i]]`. Let `sigma(x) = R (x - c) + c` be
the site map about the box centre `c = ((L - 1) / 2, ...)`, which is a lattice map only
for odd `L`. Pushing a metric field is `(push_R h)(sigma(x)) = R h(x) R^T`, and pulling
back along frame `i` is `pull_i(h)(x) = R_i^T h(sigma_i(x)) R_i`.

The averaged carrier is the centred pullback average over the whole rotation group,

    X24(dom)(x) = (1 / 24) sum_{i = 0}^{23} pull_i( h[ frame_i . dom ] )(x),

rebuilt here from landed exports only. It is then chained through the landed machinery
unchanged: per site `e(x)` is the principal symmetric square root of `I + X24(x)`, the
per-axis parts `P_i(x)` and the declared trace `K(x) = sum_i P_i(x)` come from the landed
parts routine applied to that coframe, and the endpoint Hamiltonian, unitary and
per-site readout are the landed endpoint construction at the supplied sign and scale.

Two sources are run at each box side: the executed source, whose supplied charge is
exactly invariant under all 24 frames (its orbit has one member), and an edited source
with one link decoration changed, whose orbit has six members. The insertion amplitude
is `0.20` at both `L = 3` and `L = 7`; no fallback amplitude was needed, and no clipped
site enters any transport or endpoint row.

## Theorem

**Claim 1 (parts law, exact, all 24 frames).** Through the averaged carrier the per-axis
parts obey the signed-permutation transport law in ROW form,

    P'_i(sigma(x)) = s_i * P_{p(i)}(x)

for every axis `i`, every site `x` and every one of the 24 frames, where `P'` is the same
chain applied to the rotated domain. Three facts compose to give it. `X24` is exactly
equivariant by construction, because pulling back the average along a frame permutes the
group sum. The principal symmetric square root commutes with orthogonal conjugation, so
the coframe inherits that equivariance exactly rather than approximately. And the open
one-sided difference is exactly mirror-covariant under a signed site remap: a step of
`+1` along axis `i` at `sigma(x)` is a step of `s_i` along axis `p(i)` at `x`, and the low
and high one-sided stencils at the boundary are mirror images of each other. The law
holds on the executed and on the edited source alike, so it is not an artifact of source
symmetry. The COLUMN reading of `(p, s)` is the wrong convention and is kept as a
rejector: it breaks at order the field amplitude on every frame with off-diagonal
permutation content.

**Claim 2 (trace dichotomy, exact, source-independent).** Summing Claim 1 over the axes
gives `K'(sigma(x)) = sum_i s_i P_{p(i)}(x)` with no further input, so the declared trace
is covariant exactly when the sign vector is constant. Among the constant-sign frames,
determinant `+1` forces the classification: a constant sign vector is all-positive if and
only if the permutation is even, and all-negative if and only if the permutation is odd
(for constant sign `s`, `det = s^3 sgn(p) = +1` pins `s` to `sgn(p)`). Mixed-sign frames
of either parity exist and are exactly the frames outside the dichotomy. Hence `K` is
exactly a SCALAR on
the three all-positive frames (the identity and the two three-cycles), it is exactly ODD
on the three all-negative frames (the three transpositions), and on the remaining 18
mixed-sign frames it is genuinely broken at order the field amplitude. Both identities
are law identities: they hold on the edited source at the same floors as on the executed
one. The residual scope restriction of the `K` rows therefore sits entirely in the
declared trace contraction, that is, in the sign content of the frame. It does not sit in
the carrier, which is exactly all-24 at the parts level, and it does not sit in the
triangulation.

**Claim 3 (endpoint selection rule).** The landed endpoint Hamiltonian is block
two-by-two per site on the one-excitation sector, so the excitation readout is
`p_excited(x) = sin(ETA * sigma * kappa * T_ACT * K(x))^2`, verified here against the
closed form as an external anchor. That readout is EVEN in `K`. Composing it with the
dichotomy of Claim 2, the endpoint excitation row through the averaged carrier is
invariant under exactly the six-element group

    D3 = {all-positive even permutations} u {all-negative transpositions}
       = frames `[1, 4, 9, 15, 18, 23]`,

the stabilizer of the body diagonal, and is broken on all 18 mixed frames. These are the
same six frames Cycle 700 measured as its coframe carrier; here they are derived, as the
exact invariance group of the endpoint excitation row, from the parity structure of the
frames plus the evenness of the readout. The quadrature readout is ODD in `K` and
separates the group further: it is invariant under the three-cycles and sign-flipped
under the three order-two frames, and broken on the mixed frames. The unaveraged
single-complex chain satisfies the same D3 invariance only approximately, its defect
sitting four to five orders above the averaged one at the same amplitude, so the average
sharpens the D3 covariance of the endpoint row from approximate to exact. The two-carrier
split of Cycle 700 is thereby accounted for by one mechanism, with all-24 covariance
living at the carrier and parts level and the D3 restriction coming from the declared
trace contraction together with the evenness of the excitation readout.

**Claim 4 (positivity structure, landed anchor).** At the spec-literal amplitude `1.0`,
the single-complex chain at `L = 3` reproduces the landed failure exactly: coframe
positivity fails on 6 of 27 sites and the minimum perturbed length is negative. This is
reported, not repaired and not rescaled away. Through the averaged carrier at the same
amplitude the failure count measures zero, and the whole positivity margin field is
invariant under all 24 site maps, as exact equivariance of `X24` on the frame-invariant
executed source requires; the fail set is therefore closed under the group for the
trivial reason that it is empty, and the invariance of the margin field is the
discriminating statement. At the declared working amplitude `0.20` the averaged carrier
is positive definite everywhere at both box sides.

**Claim 5 (rejector battery).** Four independent rejectors fire, each at order the field
amplitude, and one guards the implementation. The column-convention transport law fails.
The single-complex chain violates the transport law at a mixed frame. A proper subset
average over the six D3 frames alone does NOT satisfy the all-24 transport law, so the
full 24-frame average is load-bearing rather than decorative. The edited source moves the
carrier field while both sources continue to satisfy the law. And recomputing one frame's
averaged carrier with the domain cache switched off agrees to the last bit, which is what
licenses the cache used to make `L = 7` tractable.

## Measured

Insertion amplitude `0.20`, executed source unless the row says edited. Values are the
runner's own prints at the precision it emitted.

| quantity | `L = 3` | `L = 7` |
|---|---|---|
| averaged coframe positivity margin | `0.41984471373012233` | `0.44721752738115417` |
| clipped sites, any chain in the law rows | `0` | `0` |
| row-form parts law, max over 24 frames | `8.881784197001252e-16` | `2.886579864025407e-15` |
| row-form parts law, edited source | `2.220446049250313e-15` | `4.218847493575595e-15` |
| column-form parts law (rejector) | `0.30485815587167875` | `0.3317884290184846` |
| carrier equivariance of `X24` | `8.326672684688674e-17` | `1.1102230246251565e-16` |
| trace scalar on the three all-positive frames | `1.7763568394002505e-15` | `2.55351295663786e-15` |
| trace odd on the three all-negative frames | `1.1102230246251565e-15` | `2.6645352591003757e-15` |
| trace, minimum break over the 18 mixed frames | `0.30485815587167836` | `0.3317884290184838` |
| trace scalar, edited source | `2.00e-15` | `3.774758283725532e-15` |
| trace odd, edited source | `2.00e-15` | `4.773959005888173e-15` |
| trace mixed break, edited source | `0.4429750018353683` | `0.394436836969876` |
| excitation row, D3 defect | `2.0643209364124004e-16` | `2.1163626406917047e-16` |
| excitation row, minimum mixed-frame break | `0.008540305089554697` | `0.0036547365855677237` |
| quadrature scalar on the three-cycles | `3.552713678800501e-15` | `5.093148125467906e-15` |
| quadrature sign flip on the order-two frames | `2.2213134109883015e-15` | `5.3273357947247746e-15` |
| quadrature, minimum mixed-frame break | `0.6003157491985265` | `0.6514688777012956` |
| closed-form excitation anchor | `1.0408340855860843e-17` | `1.0408340855860843e-17` |
| one-excitation norm defect | `1.1102230246251565e-16` | `2.220446049250313e-16` |
| single-complex excitation D3 defect | `4.24966659084980e-12` | `4.0190836769760097e-11` |
| ratio, single-complex to averaged | `20586.268907563026` | `1.90e+05` |
| single-complex carrier equivariance break | `0.2809215446349391` | `0.6498797142773745` |
| single-complex parts law break, mixed frame | `0.04570357231269362` | `0.23664416925776133` |
| six-frame subset average, non-member defect | `0.0457035723080389` | `0.23664416924177956` |
| carrier movement, edited against executed | `3.16830100e-01` | `0.18572110376590484` |
| cache-off recomputation defect | `0.0` | `0.0` |
| excitation shift at the centre site | `-4.279293191420088e-22` | `-6.337736865315878e-22` |
| excitation shift, maximum over sites | `1.706600101400e-02` | `0.0704241139583106` |

At amplitude `1.0`, `L = 3`: single-complex positivity fails on `6` sites with minimum
perturbed length `-0.44222284059860884`, matching the landed row; through the averaged
carrier the failure count is `0`, the positivity margin is `0.025104532061362428`, and
the margin field is invariant under all 24 site maps to `2.220446049250313e-16`.

Supplied source orbits: the executed source has orbit size `1` under the 24 frames and
the edited source has orbit size `6`, at both box sides.

## What this does not do

No all-24 K-endpoint row is claimed. The trace contraction stays the landed declared
form, and its mixed-frame breaking is measured, not repaired. Even contractions of the
parts, which the transport law of Claim 1 would carry at all 24 frames, are named here as
a next route and are not adopted: adopting one would be a new declared observable and is
outside this cycle. No dynamics and no field equation appear anywhere; the endpoint is a
fixed-time unitary on a supplied Hamiltonian. The supplied sign and scale conventions of
the endpoint construction, and the insertion amplitudes, remain supplied. The
spec-literal amplitude `1.0` positivity failure is reported as structure and is not
rescaled away. Box side `L = 6` is out of reach for this construction, because the
centred pullback is a lattice map only at odd box sides. The four-complex mixture is
untouched. Nothing here reunifies Cycle 700's two carriers; it locates their difference in
one contraction and derives which six frames survive it.

A generator entry is not a rate.
This is not gravity; no field equation is claimed.

## Paired runner

`scripts/physical_orbit_averaged_k_endpoint_transport_d3_selection_cycle705_2026_08_01.py`

Reproduce with:

    python3 scripts/physical_orbit_averaged_k_endpoint_transport_d3_selection_cycle705_2026_08_01.py
