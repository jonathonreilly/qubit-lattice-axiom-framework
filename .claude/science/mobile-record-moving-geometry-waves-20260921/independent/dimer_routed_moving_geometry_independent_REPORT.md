# Independent review of continuing geometric motion

2026-09-21. Bounded mathematical source review, not a formal audit or retention
decision. The complete supplied extension was reconstructed before opening its
author checker and results. The earlier routed and preparation proofs were reused
at their previously checked identities. No dynamic aggregate analysis was opened.

**Disposition:** the conditional-history proof, microscopic rotation, additional
drift estimate, preparation transfer and stationary geometric-field bound
reconstruct under the stated hypotheses. One scope finding, F1, was identified
and is now closed by an exact one-paragraph correction. No unresolved mathematical
finding remains in this bounded review. The finite controls support the proof;
their passing does not substitute for the arguments below.

## Source boundary and F1

The originally reviewed `DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md` was 13,508
bytes, SHA-256
`d7e0ed4f6dfc8ef8e5ccd6c9382643a2df5013ba4cb9c73f47bcb23b40dbade3`.
It remains byte-preserved in
`../dimer_routed_moving_geometry_f1_fix/DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.before.md`.
The final note is 13,647 bytes, SHA-256
`e1a78183bb39d13b87fd449135ebb9e67cfbf080c06c9c68fd84f6d4b2f2aeca`.
`F1_CORRECTION_ACK.json` verifies both forward and inverse replacement of the
single declared paragraph. Every other byte agrees.

F1 concerned the original Section 1 scalar speed and four-propagating/nine-static
claim following an arbitrary full-support color law. Those counts require the
orbit-isotropic specialization. An exact independent countercontrol takes
gamma=1, Q in direction e3, p(A+x)=3/28, p(A-x)=1/28 and every other color
probability 1/14. Both orbit masses equal those of the uniform law, but the
13-dimensional tangent symbol has monic characteristic polynomial

    z^5 (14z-1)^2 (14z+1)^2 (196z^2-17) (1372z^2-103) / 10330523392.

There are eight nonzero modes and five zero modes. The isotropic 1/14 law instead
has `z^9 (7z-2)^2 (7z+2)^2 / 2401`. These use Q=e3; the permissible Fourier
Q=2pi e3 scales the eigenvalues but changes neither count. The exact symbolic
calculation also checks entropy symmetry `A C = C A^T`.

The final paragraph explicitly retains the arbitrary-p propagation matrix and
restricts the scalar speed and four/nine count to p_A=rho_A/6 and p_B=rho_B/8,
nonzero gamma and nonzero Q. Both orbit masses are positive by the unchanged
full-support premise. At gamma=0 all thirteen modes remain static. Thus the
correction closes exactly the demonstrated issue, without weakening the valid
arbitrary-p matrix theorem.

## Conditional-history argument

Fix even N>=8, the full perfect matching, finite bounded nu>=0, and the existing
strictly positive routed exchange floor. Each clockwise and counterclockwise
immutable four-record rotation has rate nu. Their geometry projection is a
plaquette flip at rate 2nu independent of colors and fine keys. On the two black
sites one sense transposes colors and the other is the identity; the antipodally
even code makes this statement independent of which record of a pair is black.
Every record itself moves one nearest-neighbor step and the inverse rotation
recovers its identity. Equal rotation rates are consequential.

Condition on the complete geometry history and its rotation marks. Between its
finitely many jumps, colors have generators L_m preserving the same product
measure pi_p and every uniform count sector. At each jump colors undergo a
specified site permutation preserving those measures. Starting with pi_p, their
conditional one-time law is therefore pi_p at every time. This is not independence
of the color trajectory from the geometry trajectory. The geometry history is
independent of the initial colors and of the routed-clock randomness, which is
the independence actually required.

The new estimate is, for interval observables F_m centered in every count sector,

    E |sum_m integral_[a_m,b_m] F_m(X_s) ds|^2
        <= 2 sum_m (b_m-a_m) ||F_m||_{-1,S_m}^2,

where S_m is the symmetric part of L_m. Solve -S_m f_m=F_m in each sector. The
forward Dynkin increment is delta f_m minus the L_m integral. The backward
increment is minus delta f_m minus the L_m^* integral. The reversed conditional
chain indeed has these adjoints and inverse boundary permutations, because all
intervals and boundary maps preserve the same reference law. Summed forward
increments are martingale differences; summed backward increments are reverse
martingale differences. Their second moments each equal twice the sum of the
interval lengths times the H-minus-one norms. Their sum is twice the desired
integral. Cauchy-Schwarz yields the displayed constant 2.

The endpoints cancel within each interval. There is no derivative of the Poisson
solution across geometry jumps, no growth with the number of jumps and no need
for one common Poisson solution. Real and imaginary parts give the complex
version. The common kernel is the count-sector kernel: the contracted routing
graph remains connected for every perfect matching. Reference color stationarity
is essential. Our separate two-state countercontrol from a nonstationary color
entrance gives second moment 0.1801625794 against the incorrectly reused
stationary bound 0.0099009901. The note does not make that extension.

The earlier fixed-block replacement estimates are uniform in the matching and
have sector-centered residuals. They therefore apply on these intervals. Their
equal-time estimates use the conditional product law; time integration needs only
Cauchy-Schwarz. With fixed block size first, their integrated error remains of
the form

    C_T [A_l l^3/N + 1/l + C_l/N^2].

The existing variable-direction cancellation is pointwise in the matching, so
using fixed physical black-site Fourier coordinates introduces no new coordinate
derivative. Taking N to infinity and then l to infinity is the stated order.

## Additional color drift and martingale

For a fixed matching M, the color part of rotation drift on a Fourier observable
F is K_M F, with one transposition at rate nu per flippable square. The other
physical rotation contributes zero color increment, not an extra transposition.
The color-only K_M is an auxiliary operator for this drift calculation, not the
actual joint geometry generator.

A black diagonal identifies at most one elementary square for N>=8, and its
transposition is present in the contracted routed graph. With the source's
symmetric routed rate k0/2 per channel,

    D_{K_M} <= a D_{S_M},             a=2nu/k0.

The estimate is conservative; our explicit flippable cases have two routed
channels on that diagonal. Form Cauchy-Schwarz gives

    ||K_M F||_{-1,S_M}^2 <= a D_{K_M}(F).

For the K^(-1/2)-normalized field and fixed Fourier Q, the transposition increment
is the product of a phase difference O(|Q|/N), a bounded color difference and
K^(-1/2). There are O(K) squares. Thus

    D_{K_M}(F) <= C nu |Q|^2/N^2,
    ||K_M F||_{-1,S_M}^2 <= C nu^2 |Q|^2/(k0 N^2).

The conditional-history estimate over microscopic time Nt makes the integrated
extra drift mean square O(t nu^2 |Q|^2/(k0 N)). The actual joint-process
martingale, taken before conditioning, has bracket O(1/N): every color jump is
O(1/(N sqrt(K))) and the microscopic total rate is O(K). One must not substitute
a conditioned deterministic-jump process into that martingale decomposition.
The source uses the conditioning only for the additive-functional estimate.

These estimates retain the arbitrary-p finite-mode matrix conclusion uniformly
over the initial matching law. They require fixed modes, a fixed finite time
list/horizon, fixed p with full support, fixed finite rates and the autonomous
equal-sense geometry mechanism. They are not a hydrodynamic theorem for arbitrary
nonstationary color profiles or color-dependent geometry rates.

## Preparation and geometric-field boundary

The previously checked preparation gap is uniform in M. Conditional on a geometry
history, each interval contracts a mean-zero sector density in L2 at that gap,
and each intervening site permutation is an L2 isometry. Multiplying interval
contractions therefore gives the same total-time estimate. Birth color counts
are multinomial and independent of the autonomous geometry history. Mixing each
sector and then mixing those counts yields pi_p independent of the geometry at
the end of preparation.

The comparison reference consequently uses the law of the matching at
`tau_fill + t_prep`, not the frozen completion matching. Strong Markov conditioning
and total-variation contraction by the subsequent joint path kernel give the
transfer. The normalized squared field residual is bounded by C K; with the
previously specified epsilon_N=N^-4 and K=N^3/2, its error is O(N^-1). This does
not assert that the growing color law is product or provide a volume-uniform
completion-time bound. The old positive filling paths remain possible after
adding finite-rate conservative rotations, so on a fixed finite graph they
still exclude nonfull closed classes of the geometry chain.

For the separate geometric field

    B_i(x)=sigma_x [n_i(x)-1/6],

the backward lattice divergence is exactly zero at a perfect matching. For an
i-to-j square flip with base x, its edge-midpoint Fourier increment is

    (2i sigma_x/sqrt(V)) exp[-ik.(x+(e_i+e_j)/2)]
        [-sin(k_j/2)e_i + sin(k_i/2)e_j].

Its discrete divergence vanishes and its squared norm is
`4[sin^2(k_i/2)+sin^2(k_j/2)]/V`, at most `|Q|^2/(N^2 V)` when k=Q/N.
At geometric rate 2nu per flippable square the Dirichlet form is O(nu/N^2).
Under a stationary reversible class law, or a mixture of such laws,

    E |F(M_t)-F(M_0)|^2 <= 2t D_geo(F).

Microscopic t=Nt_macro yields O(1/N). This bound does not require a positive
spectral gap or a lower structure factor. It is an absolute mean-square statement,
not a relative decorrelation estimate. Stationarity/reversibility are essential
here even though the color theorem allows arbitrary initial geometry. Winding
or frozen classes and nonergodicity cause no contradiction. The geometric Gauss
field has not been identified with the propagating color fields.

## Independent controls and author comparison

`PRE_COMPARISON_DERIVATION.md` and the initial controls were sealed before author
access in `PRE_COMPARISON_SEAL.json`, SHA-256
`d22a62f0714607208448c3a54c4fa1908ff6066615aa6099c3a9f7da0bce8f61`.
The seal binds 12 artifacts and eight reused dependencies. It remains unchanged.

`independent_check.py` supplies separately assembled controls:

- Three noncommuting four-state generators with exact interval H-minus-one norms
  19/20, 1387/1494 and 1/5. One, two, nine and 37 intervals with deterministic
  boundary permutations independently track both forward/backward martingale
  moments and the additive integral. Pairing errors are at most 5.6e-16. A
  separate nonstationary-entrance countercontrol records the hypothesis failure.
- All 64 square record-orientation/parity/sense cases give 32 identity and 32
  transposition color projections, preserving immutable records and their
  nearest-neighbor inverse moves.
- Independently generated winding, columnar and irregular N=8 matchings check
  edgewise Dirichlet coefficients, with 0, 512 and 148 flippable squares. A
  numerical one-marker-sector Poisson solve separately verifies the H-minus-one
  form estimate for the nontrivial geometries.
- Ninety-six Fourier increment cases on N=8 and N=10, including wraparound bases,
  all three planes, both flip orientations and multiple modes, check the exact
  increment formula. Maximum floating evaluation error is below 3e-16. A
  two-state reversible geometric chain checks the factor 2 in the increment
  bound.
- `mode_scope_countercontrol.py` supplies the exact rational characteristic
  polynomials behind F1, not a floating eigenvalue threshold.

The full 193-line author checker was read after sealing. Its SHA-256 is
`ac77dead111c72e25d5d1121622a9e94c27c84c4b35b5bfbf89f8a86c8712df9`.
Its inherited routing helper remains at the previously reviewed SHA-256
`98aa5259d58a5355a2aa9283e19bad869160bd9432882d589db8bbb2e0f15921`.
The complete combined result is SHA-256
`892c8210d509b3ec3f69676b7bc99d56957c7e482eacfea7d4920fcf1f9149fe`.
One truncated display of that result was repaired by reading every row and all
interval witnesses in a compact projection; it was not treated as a completed
read before that repair.

The author implementation checks nine geometry cases and 40 numerical switched
energy cases. Its square projection, coefficient normalization and finite-moment
ODE agree with the reconstructed arguments. The separate group JSON payloads
match the combined result exactly. `compare_author_and_correction.py`
authenticates all five author source bindings, using the preserved original note
for its historical binding. It independently recomputes all 40 displayed energy
bounds/ratios from interval witnesses and all nine geometric normalization/count
relations. The nonzero geometric maxima equal
`[sin(pi/N)/(pi/N)]^2`; the largest saved energy ratio is 0.7417173523988206.
The complete author log has two completion lines and empty stderr.

This comparison did not rerun the author's randomized matrices or geometry
generation for more PASS counts. Our separately assembled controls and the
proof reconstruction supply the independent evidence. No scientific execution
attempt failed in this packet; the excluded-hypothesis countercontrols are
intentional successes. No production trajectory, dynamic aggregate, new sharper
path-comparison source or unrelated campaign argument was inspected.

## Reproduction and limitations

Run `python3 independent_check.py`, `python3 mode_scope_countercontrol.py` and
`python3 compare_author_and_correction.py` from this directory in a reproduction
copy. They write only here. The first two are the pre-comparison scientific
controls; the third is post-comparison authentication/arithmetic. Their original
full stdout, stderr and execution receipts are preserved. The exact current and
historical source identities, reused dependency identities, author evidence and
every local review artifact are listed in `FINAL_SEAL.json`.

The proof is conditional on the previously checked routed replacement theorem
and preparation theorem, whose unchanged identities are reauthenticated. This
review does not optimize their rates or prove a thermodynamic equilibrium phase,
microscopic quantum realization, geometric photon identity, uniform completion
time, arbitrary-mode/time limit, or arbitrary biased geometry extension. It is
a scientific source review and correction acknowledgment, not an audit verdict.
