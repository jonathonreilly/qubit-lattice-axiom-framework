# Checked outcome of the direct constrained-dynamics attempt

Parent author, October 12, 2026. The parent read the complete independent
report after doing the derivation and running both diagnostic versions.

The specified preferred-time action keeps the fitted static equations and
has positive constrained field energy. Eliminating its auxiliary potential
produces a nonpolynomial spatial evolution operator on anisotropic homogeneous
backgrounds. This fails the chosen finite-support propagation requirement.
Changing only constant two-field time-quadratic coefficients cannot meet
both selected stability and propagation targets within the stated ansatz.

All statements retain DIRECT_DYNAMICS.md's domains. This is a successful
calculation of a candidate limitation, not a successful fundamental gravity
model, a rejection of its static fits, or a general no-go for gravity.
No physical light speed, tensor-wave identification, observation test or
new fit enters this block.

| Frozen response | Approximate infimum D | Maximum group speed / c_s |
|---|---:|---:|
| Original D joint | 0.5676243959545038 | 1.3273011590171178 |
| Interior D joint | 0.2336790394432096 | 2.6146366982056386 |

The displayed numbers are rounded diagnostics. Exact rational series bounds
certify D>0 for both the frozen decimal tokens and their exact binary64 values.
The independent calculation certifies the simple conservative bounds D>0.5676
and D>0.2336 respectively. The group maxima are limiting local mode ratios,
not finite wavefront speeds. At the actual fitted external E both candidates
have N=D, phase/group ratios 0.8635751855737414 and 0.8506198429869628, and a
zero homogeneous off-source tail.

The nonzero tail on active-ramp backgrounds is physically nonconstant under
the stipulated scalar-force definition. On z>0, differentiating equation
(10) gives force-acceleration kernel

    -30 c_s^2 (N-D)^2 / (pi N^3 z^6).

The parent checked this derivative separately in
evidence_v2/FORCE_TAIL_CHECK.json. The independent reviewer also derived it
from a different general matrix Green-function differentiation and checked
smooth-bump convolutions. Thus the scoped failure concerns the stipulated
force as well as the potential, while a larger gauge/observable cancellation
remains a concrete untested escape.

Independent verification used a different exact logarithm decomposition,
all forty ramp limits, direct constant-flux solutions instead of the parent's
finite L-BFGS-B optimization, and a separate matrix derivation. The two finite
scaled energies agree within 6.2e-14. The review covers constraints, regularity
at knots, zero modes, D→0, the isotropic exception, and all constant kinetic
rank cases. It found no material equation correction.

Source identity:
- DIRECT_DYNAMICS.md: 6fbaf6b91561d3ce5a51b154a364e98d1fafedd1b94119f725df8df4219648d8
- Current runner: 69e3ce25c55898fa32ea513ffee13d8a4a5ecd153de9659c8ff8d88597efba8c
- Current result: b29424dc8a8e0c0aea9f3985cf24e1766833c83843488a33449d7ef198601db9
- Frozen weight input: 1dae3e3888f82c2ced9e07253dcf520bcf744e43e5a31c9e9849618703c90b1f
- Independent receipt: 3107b4fd9e8393b350dce6c995247973fe428ee6f67e59ba637882556b87ffd5

See independent_review/INDEPENDENT_DYNAMICS_REVIEW.md and its receipt for
full coverage. Original source/output snapshots remain under evidence_v1;
v2 corrects a rounded stdout lower-bound phrase and adds exact binary64
positivity checks. No original arithmetic was silently replaced.

The broad five-family no-go packet remains FAIL because only one genuine
kinetic family was attempted. This does not contradict the proved scoped
identities. Preserve partial-attempt-with-named-untested-routes and the
campaign's NO_GO_LEDGER entry. Metric/vector constraints, matter reciprocity,
different derivative structures, or an explicitly nonrelativistic effective
interpretation remain live. No formal audit or retained status was applied.

