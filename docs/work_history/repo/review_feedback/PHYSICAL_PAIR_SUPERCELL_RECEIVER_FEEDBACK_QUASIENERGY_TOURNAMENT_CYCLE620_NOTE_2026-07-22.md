# Cycle 620 — physical pair supercell, receiver feedback, and quasienergy tournament

Date: 2026-07-22

Authority: none

Audit: unset
Constitutional effect: none

## Frozen question and route boundary

Cycle 620 tests three separate live routes from Cycle 615. Route A asks whether
the resource-to-cubic-neutral-pair involution and the supplied distinct `+/-`
charge sectors can be lowered into the accepted Cycle 610 support-two
nearest-neighbor K=129 supercell with one common E, clean-work return, exact
inverse, constant overhead, all 24 proper-cubic frames, all 576 products, and
L3/L6/L7 held-size controls. The candidate negative sector is not derived
antimatter. Route B asks whether a local physical Cycle 608/612 endpoint bit can
cause feedback in the joined gauge-Regge action and select one response without
a host sign or a hardwired 3/4 target. Route C independently probes a full-unitary
quasiphase/coframe-variation representative. The open-boundary and periodic
real-space seam is preserved.

The criteria were frozen before evaluating signs. No route failure is promoted
to a shared substrate obstruction. Wrapped phase is not energy, a generator
element is not a rate, the feedback carrier is not physical stress, and no
update schedule is time.

## Route A — common-E support-two pair and sector compiler

The common E uses one neutral resource M2, six positive occupation M2s, and six
negative occupation M2s. Its seven active words are the resource word and the
six point-counterpoint pair words; all other 8185 local words receive the
identity extension. A five-Givens word W maps one pair branch to the normalized
cubic six-branch scalar. The target involution is exactly

`G_pair = W X_resource,pair0 W^dagger`.

The five supplied angles have exact sines `1/sqrt(6)`, `1/sqrt(5)`,
`1/sqrt(4)`, `1/sqrt(3)`, and `1/sqrt(2)`. Each two-level operation is converted
to a Gray path. Every Gray conditional includes the physical Cycle 610 one-hot
orientation predicate, twelve data controls, twelve clean conjunction roles,
and an exact Toffoli/controlled-one-M2 lowering. All two-M2 endpoints are routed
by the literal Cycle 610 Hamiltonian bus with move/apply/restore. The B
occupation rails, predicate work, conjunction work, role orientation, and the
neutral resource excitation are supplied clean at encoding.

The two charge sectors use separate A/B occupation rails. For each charge and
direction, the scatter and clear remote CNOTs use disjoint source and target
radial paths and one cross-face nearest-neighbor edge; a local A/B swap completes
the stream. The schedule is serialized by charge and direction and is constant,
not a time variable. The positive coin and supplied conjugate negative coin are
followed by this charge-blind stream and two separate same-g contacts with no
cross contact. Thus the accepted subsequence remains `coin -> stream -> contact`.

The runner tests the common-E intertwiner on a seeded coherent vector, clean
inverse, code leakage, the identity extension, deletion of each W/swap stage,
every clean conjunction truth row, literal bus endpoints, all 24 and all 576,
every translated L3/L6/L7 cross edge and wrap seam, stream inverse and factor
deletions, full-Fock +/- unitarity and order reversal, and the inherited
one-particle mass fixture.

The final common-E residual is `3.78e-16`, inverse residual `3.62e-16`, and
leakage zero. The compiled word contains 75 Gray conditionals, 1,800 exact
Toffoli calls, 17,846 one-M2 gates, and 10,875 two-M2 gates before literal bus
routing. Each branch also reuses the pinned 721-gate Cycle 610 orientation
predicate and its inverse, for 1,442 additional support-two gates with clean
predicate return. It exhausts 307,200 clean conjunction rows with zero
failures. Across the 24 orientation branches, 261,000 actual support-two
endpoint pairs pass the bus coordinate/inverse audit; the pair-conditional
route-return debit, separate from the inherited predicate routing debit, is
322,346,002,656 SWAPs per coarse cell. The added role upper bound is 313 M2 per
coarse cell: 25 resource/A/B data roles plus the 288-member orbit of twelve
clean conjunction roles. The two-charge stream uses 4,980 two-M2 gates per cell
before the inherited orientation-control wrapper. This is a deliberately large
feasibility upper bound, not a minimal or economical compiler.

For L3/L6/L7 the physical stream checks 7,776/62,208/98,784 all-frame
cross-face edges with no nearest-neighbor, wrap, source-target conflict,
inverse, or B-buffer-leakage failure. The inherited one-particle mass residual
is `8.62e-14`; the charge-conjugate spectrum pairing residual is zero. The
accepted physical factor-order reversal signal is `0.520279`, with nonzero
coin, stream, and contact deletions.

## Route B — endpoint-controlled feedback family

The actual matter-caused control is the Cycle 608 word

`P_d(pointer); Toffoli(pointer,binder,opportunity); P_d(pointer)`.

The opportunity bit is used locally and uncomputed. The candidate feedback is

`A_fb = (sigma*kappa/2) sum_x b_x |D_x[e] - rho_x|^2`,

where D is the raw local proper-cubic sum of Regge deficits and rho is the local
gauge occupation. This is state-dependent coframe feedback, not merely routing
a supplied response-sign bit. The positive square, its 1/2 coefficient, the
relative scaling of D and rho, and the nonnegative-feedback-Hessian criterion
are candidate-law inputs; no pinned approved surface forces them.

The runner therefore audits both the positive square and the equally local
negative square, kappa in `{1/2,1,2}`, both lambda signs and relative magnitudes
`{1,2}`, and improvement coefficient `{-1,0,1}` on every L3/L6/L7 fixture. For
each fixed feedback sign and scale the exact surviving family is

`R(lambda,c) = R_fb + lambda (R0 + c Rimp)`.

All signs and scales preserve the tested U(1) Gauss neutrality, Regge Ward
identity, stationary equation, exact finite-state inverse, and all 24/all 576
covariance controls. Deleting the matter predicate or endpoint vetoes the
feedback, while deleting the density cross term changes the response.
All 72 members of the frozen finite grid happen to have positive receiver
values. That does not select a receiver: no numerical-response-to-Cycle612-word
map is derived, and the grid does not exhaust the retained candidate
`lambda,c` parameters. For every fixed feedback sign/scale and every fixture,
the runner extracts the nonconstant affine family and constructs explicit
opposite-sign parameter witnesses. The positive-square analytic family also
has both signs. Unrestricted lambda is a retained candidate-law parameter, not
a derived physical law. The exact family and the inherited `{3/4,5/4}` class
therefore do not collapse. Mapping a numerical response sign through a supplied
Cycle 612 convention is not a derived receiver law and is not selection.

## Route C — full-unitary coframe generator

Route C uses the actual full 64-dimensional Fock update

`U(e,k) = Contact Gamma(Stream(e,k) Coin)`

in the accepted `coin -> stream -> contact` order. For the six spatial symmetric
coframe components it constructs

`K_ab = i U^dagger partial U / partial e_ab`.

K is estimated from the centered relative unitary
`U(-epsilon)^dagger U(+epsilon)` and its eigenphases, then rerun at half step.
It is Hermitian by unitary construction; the maximum half-step convergence
residual is `7.52e-9`. K is a generator representative. It is not a rate and is
not called unique physical stress. At generic periodic Bloch points for
L3/L6/L7, every nondegenerate eigenbranch is matched by overlap at positive and
negative coframe displacement. Its locally unwrapped quasiphase derivative
agrees with the corresponding K expectation to `2.07e-9`. The maximum all-24
generator-tensor covariance residual is `5.19e-7`, the finite coframe-update
covariance residual is `2.50e-15`, and all 576 representation products pass.

A constant global rephasing places the most responsive branch on the principal
quasiphase seam without changing the quantum channel or K. The principal
wrapped value then jumps by almost `2*pi`, while the locally unwrapped step and
K remain continuous. This is why wrapped phase is not energy. Degenerate branch
transport is not claimed. Route C remains a periodic Bloch/full-unitary probe;
it is not silently joined to the Route B/open-boundary real-space apparatus.

The single-Bloch onsite contact/diagonal-stream commutator is correctly zero,
about `2.23e-15`; it is a valid reduced-block diagnostic, not an order-deletion
failure. The order-sensitive control is separately evaluated on an explicit
two-cell 4,096-dimensional real-space full-Fock word. Its stream permutation is
bijective, norm residual is zero, contact deletion signal is `1.538`, and
`coin -> stream -> contact` differs from contact-first by `0.488`. This
two-cell order witness is not conflated with the L3/L6/L7 Bloch generator.

## Supplied, derived, and open

Supplied: the K=129 one-hot orientation/predicate/bus fabric; blank B and work
roles; the candidate negative-charge copy, conjugate coin, separate same-g
contact, and absence of cross contact; the five Givens angles and resource
excitation; the Cycle 608 binder/path/chart and Cycle 612 endpoint-use program;
the feedback square, coefficient convention, D/rho scale and sign/scale family;
the Cycle 576 Regge complex, raw deficit, pseudoinverse, lambda and periodic
fixtures; and the diagnostic response-to-word convention.

Derived or executed: common-E pair lowering, exact Gray/conjunction and
support-two bus word, clean return, inverse, leakage, deletion, all24/all576,
two-sector L3/L6/L7 occupation streams, preserved coin -> stream -> contact and
mass fixture, endpoint-controlled feedback variation with Gauss/Ward/inverse
controls, the surviving affine response family, and the full-unitary K tensor
with tracked nondegenerate quasiphase derivatives and seam control.

Open: physical antiparticle identity; autonomous role/work/binder/path/chart
genesis; selection of the feedback law, sign, scale, lambda, or improvement;
an operational metric and derived Regge-response-to-Cycle612 receiver map; one
receiver word; one joint open-boundary real-space Regge apparatus; physical
stress, energy, gravity, causal time, event/Record formation, and Born
probability.

## Full N1–N8 no-go discipline

N1 — Seven normalized mechanism families are separated: positive feedback
square, negative feedback square, feedback scale orbit, normalized-deficit
feedback, nonlinear bounded feedback, the full-unitary coframe generator, and
an open real-space feedback apparatus. The normalized, nonlinear, and joint
open routes remain live untested alternatives, so a broad negative must fail.

N2 — The collapsed walls are feedback-law choice, continuous lambda/improvement,
receiver map, domain join, stress identity, and supplied genesis. All fifteen
pairs are audited; no closure is inferred between them.

N3 — The hidden-wall scan exposes one-hot orientation, clean work/B buffers,
the Givens angles and pivot order, candidate negative sector and contacts,
binder/path/chart, every feedback coefficient and criterion, raw Regge and
pseudoinverse inputs, the response-word convention, finite-difference epsilon,
and nondegenerate fixtures. The only literal phrase-scan hit is “Registered
primitives”; it is classified as cited retained authority after reading the
machine registry and all current primitive source notes, not as a hidden
condition.

N4 — Residual matching is exact and scoped. Cycle 615 Route A witnesses the
physical pair/full-sector lowering residual; Cycle 610 witnesses the physical
fabric; Cycle 615 Route C witnesses the same lambda/c and two-word residual;
Cycle 612 witnesses the supplied delay/advance map; Cycle 576 witnesses the
Regge sign/normalization/metric/domain terminals.

N5 — “Physical pair compiler” means the declared common seven-word code, clean
work and orientation sector. “Not derived antimatter” is local candidate-sector
language, not a universal particle theorem. “Feedback is not selection” is
restricted to the audited square family. K is a finite periodic generator
representative, not physical stress, energy, or a rate.

N6 — Registered primitives retain only their approved scale, kinetic-form, and
pointwise evaluation roles. Live partial closures are a retained positivity
theorem, normalized or nonlinear local feedback, a direct K-to-endpoint
coupling, and a joint open real-space flux/Regge compiler.

N7 — Steelman: a hostile reviewer should reject any broad selection no-go. A
normalized local deficit scalar, a bounded nonlinear feedback potential with a
unique fixed point, or a direct coupling of K to the physical endpoint could
remove the lambda/c/sign orbit. Each has a concrete terminal: strict locality,
covariance, clean endpoint return, Gauss/Ward/inverse, and one held receiver
word without refit.

N8 — The cross-cycle echo weighs against foreclosure. Cycle 610 turned a host
packing residual into a bounded compiler; Cycle 612 turned detector pointers
into matter-caused endpoint bits; Cycle 615 explicitly left feedback and
full-unitary routes live; Cycle 576 constructed Regge while preserving its
sign, normalization, metric, and domain seams.

Broad negative gate: FAIL / DO NOT SHIP. The narrow result is that the audited
linear feedback-square family does not select a unique response. There is no
minimum-content claim, no route-independent shared obstruction, and no axiom
pressure.

## Dependency ledger and next route

- `C_ref`: advanced by physical all-frame pair/sector lowering; role genesis,
  endpoint chart/path, and receiver mapping remain.
- `C_num`: sharpened by exact Givens angles and the explicit affine feedback
  family; feedback and response normalizations remain.
- `C_wrap`: advanced by the tracked full-unitary quasiphase derivative and
  explicit branch seam; no phase is called energy.
- `C_int`: advanced across pair/sector, endpoint feedback, Regge variation, and
  full-unitary probes; the joint open real-space apparatus remains.
- `C_local`: advanced by the constant-overhead support-two pair and occupation
  stream compiler; economical packing and autonomous clean-role genesis remain.
- `C_source`: sharpened by genuine matter-caused feedback, but its discretionary
  law family leaves both receiver words and does not establish gravity.

The optimal next campaign is to test normalized and nonlinear feedback and a
direct K-to-endpoint coupling, while compiling the open flux boundary and Regge
carrier into one physical real-space apparatus. Require one receiver word with
no host sign, refit, hardwired 3/4 target, or added stability postulate.
