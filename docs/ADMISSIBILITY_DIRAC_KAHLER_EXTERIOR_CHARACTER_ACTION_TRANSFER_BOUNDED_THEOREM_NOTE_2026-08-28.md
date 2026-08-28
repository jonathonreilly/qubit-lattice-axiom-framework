---
claim_id: admissibility_dirac_kahler_exterior_character_action_transfer_bounded_theorem_note_2026-08-28
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md
claim_type: bounded_theorem
claim_scope: "Exact finite classification of the parent connection-curvature note's positive plaquette defect as the O(3) character of the full exterior representation; the ordered local link equation and flat covariant-curl Hessian for an explicitly supplied plaquette-action family; exact improper-sector and topology boundaries; zero endpoint coframe/metric response only at fixed orthogonal links, constant weights, and fixed measure; reflection positivity and gauge-projected transfer positivity only for nonnegative crossing couplings; injectivity only when every crossing coupling is strictly positive and only on the gauge-invariant Hilbert space or before gauge projection in temporal gauge; and the corresponding support-qualified self-adjoint logarithm. The action, coupling map and signs, Haar measure, temporal extension, gauge carrier/projection, metric/source extensions, and every physical interpretation are explicit inputs rather than framework-selected consequences."
runner: scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py
independent_checker: scripts/admissibility_dirac_kahler_exterior_character_action_transfer_independent_2026_08_28.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_plaquette_holonomy_connection_curvature_bounded_theorem_note_2026-08-27
target_blocker_text: "derive or discriminate a framework-native local selection/dynamics law for the orthogonal edge factors, then test the resulting same-action operator at the OS/Lorentzian interface"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Attempt to derive an equivariant reversible edge transport from the actual neighbor-conditioned M2(C) conditional law; the supplied action and temporal measure here are consistency tests, not a selection theorem."
conditional_surface_status: "conditional on the cited parent science chain and on a supplied action, couplings, Haar measure, temporal extension, and gauge carrier"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the exterior-character, variation, Hessian, finite RP, transfer, topology, and metric-response statements are exact bounded theorems for a disclosed finite family, while physical selection and identification remain open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exterior-character plaquette action and finite transfer boundary

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Exact target

The [plaquette-holonomy connection-curvature parent](ADMISSIBILITY_DIRAC_KAHLER_PLAQUETTE_HOLONOMY_CONNECTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-08-27.md)
constructed an orthogonal plaquette product `W_p`, its full exterior lift, and
the positive defect

```text
Q_p = 16 - Tr Lambda(W_p) - Tr Lambda(W_p^-1).
```

This note asks what follows if that diagnostic is inserted into a disclosed
finite local action.  It proves the exact character classification, local
equation, flat Hessian, finite reflection-positive transfer construction, and
its topology and source-response boundaries.  It also tests whether those
properties select one action.

The result is deliberately conditional.  The [four framework axioms](MINIMAL_AXIOMS_2026-06-29.md)
supply spatial cubic adjacency and a neighbor-conditioned local probability
distribution, but not the displayed action, its coefficient values, Haar link
measure, temporal links, or a physical connection interpretation.  The
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies OS0 graining form only.  It supplies none of those dynamical inputs.

## Imports and open boundaries

| Input | Role in this note | Provenance | Open boundary |
|---|---|---|---|
| orthogonal edge factors `R_e`, plaquette words `W_p`, and defects `Q_p` | finite connection/curvature carrier | [plaquette-holonomy connection-curvature parent](ADMISSIBILITY_DIRAC_KAHLER_PLAQUETTE_HOLONOMY_CONNECTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-08-27.md) on its conditional parent chain | physical selection of `R_e` remains the connection wall |
| action form `f_n` and finite spatial half-action | object tested by variation, RP, and transfer | supplied definition (1)–(2) in this note | physical action selection remains the action-form wall |
| real plaquette/crossing couplings `kappa_p`, including their map, magnitudes, and signs | weights in the field equation and seam kernel | supplied coefficients; sign hypotheses are stated separately for every theorem | the coupling map and signs are not derived |
| normalized product Haar link measure on `O(3)` | finite integration measure used in RP and transfer | supplied mathematical measure | the measure wall and any physical or metric-dependent measure remain open |
| temporal vertex links, link reflection, seam assignment, and reflected spatial half-actions | finite Euclidean temporal extension | supplied construction (21), (25) | the temporal-seam wall and physical time evolution remain open |
| `O(3)` gauge carrier, temporal-link gauge averaging `P`, and choice of `L^2` versus `H_phys` | projection and Hilbert-space domain | supplied finite gauge construction (26)–(27) | the gauge-space wall and physical state-space identification remain open |
| fixed independent `R_e`, constant weights, fixed measure, and no matter/Record source | domain of the endpoint stress calculation | explicit fixed-family hypothesis in (16)–(17) | the geometry and reciprocal-source walls remain open |
| OS0 graining form | structural equality of time/space kinetic graining only | [approved kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | supplies no action, coupling, measure, Hamiltonian, clock, or Lorentz theorem |
| physical reading of `-log T_hat` | none; expressly excluded from the mathematical reconstruction | no supplying authority | the Hamiltonian-identification and clock/Lorentz walls remain open |

## Supplied finite action family

Let `X` be a finite oriented cubical cell complex, let `R_e in O(3)` be one
matrix on each stored edge with `R_bar(e)=R_e^-1`, and let `W_p` be the ordered
plaquette word.  Define the full-exterior representation

```text
rho = Lambda^* R^3 = direct_sum_(k=0)^3 Lambda^k R^3,
chi(W) = Tr rho(W).
```

For each integer `n>=1`, define

```text
f_n(Q) = 2 [8^n - (8-Q/2)^n] / [n 8^(n-1)].       (1)
```

The disclosed action is

```text
S_(n,kappa)[R] = sum_p kappa_p f_n(Q_p).           (2)
```

The linear member is `f_1(Q)=Q`.  The first nonlinear member is

```text
f_2(Q)=Q-Q^2/32.                                   (3)
```

The variational statements below allow real `kappa_p`.  Minimum and positive
transfer statements name their nonnegative or strictly positive coefficient
hypotheses explicitly.

## Full-exterior character and the two components of O(3)

For every `3 x 3` matrix `W`, the traces on the exterior degrees are its
elementary symmetric polynomials.  Therefore

```text
Tr Lambda(W)
 = 1 + Tr W + Tr Lambda^2(W) + det W
 = det(I+W).                                        (4)
```

For `W in O(3)`, put `delta=det W`.  Orthogonality gives

```text
Tr Lambda^2(W) = delta Tr(W^-1) = delta Tr W,
chi(W) = (1+delta)(1+Tr W).                         (5)
```

The character is real and `chi(W^-1)=chi(W)`.  Hence

```text
Q(W) = 16 - 2 chi(W)
     = { 4(3-Tr W)=8(1-cos theta),  delta=+1,
       { 16,                           delta=-1.     (6)
```

Thus the defect is Wilson-type on `SO(3)`.  It is constant throughout the
improper component because every improper three-dimensional orthogonal matrix
has eigenvalue `-1` and hence `det(I+W)=0`.

Equation (6) also supplies two necessary fences.  The value `Q=16` is not a
determinant-sector classifier: a proper pi rotation has the same value.  And a
function of `Q` alone resolves no conjugacy data within the improper component.
Neither statement rules out a separate determinant term or another character.

## Ordered local Euler-Lagrange equation

Use the left variation

```text
R_e(t)=exp(t X_e) R_e,       X_e in so(3).           (7)
```

Every occurrence of the stored edge must retain its word position.  If a
forward occurrence is

```text
W_p = C R_e D,
U_(p,e)=R_e D C,
epsilon_(p,e)=+1,
```

and an inverse occurrence is

```text
W_p = C R_e^-1 D,
U_(p,e)=D C R_e^-1,
epsilon_(p,e)=-1,
```

then cyclicity gives

```text
delta Tr W_p = epsilon_(p,e) Tr[U_(p,e) X_e].       (8)
```

Repeated occurrences are counted with multiplicity.  Put

```text
eta_p = (1+det W_p)/2.                              (9)
```

Equation (6) and the fact that determinant components are disconnected give

```text
delta Q_p = -4 eta_p epsilon_(p,e)
              Tr[U_(p,e) X_e].                     (10)
```

With `skw U=(U-U^T)/2` and
`<A,B>=-Tr(AB)/2` on `so(3)`, the exact equation at an unfrozen link is

```text
sum_(p,e occurrences)
  eta_p epsilon_(p,e) kappa_p f_n'(Q_p)
  skw U_(p,e) = 0.                                  (11)
```

The cyclic re-basing in (11) is load-bearing: adding untransported plaquette
matrices from different link frames is not covariant.  Improper plaquettes
have `eta_p=0` and produce no infinitesimal connected-component force.  A
proper pi rotation also has `skw U=0`, so it is stationary at `Q=16`.
True orientation reversal replaces the word by its inverse; it is not a raw
reversal of the displayed factor order.

## Flat Hessian and topology

Let `R^0` be a flat background with every `W_p[R^0]=I`, and let
`d_(R^0)` be the covariant linearized plaquette curl.  For a plaquette word
`L_1...L_m`, it is the ordered sum

```text
(d_(R^0) a)_p
 = sum_j Ad_(L_1^0...L_(j-1)^0) Y_j,
Y_j = a_e                              if L_j=R_e,
Y_j = -Ad_(R_e^-1) a_e                 if L_j=R_e^-1. (12)
```

At the identity background this is the ordinary signed cubical curl.  The
small-field character formula gives

```text
Q_p(t)=4 t^2 ||(d_(R^0)a)_p||^2 + O(t^3).           (13)
```

Since every member (1) obeys `f_n(0)=0` and `f_n'(0)=1`,

```text
D^2 S_(n,kappa)|_(R^0)(a,b)
 = 8 sum_p kappa_p
     <(d_(R^0)a)_p,(d_(R^0)b)_p>.                  (14)
```

The flat Hessian is therefore identical for every `n`.  For strictly positive
weights its kernel is `ker d_(R^0)`.  Gauge variations lie in this kernel, but
topology can add more.  At the identity background the linearized kernel
quotient by infinitesimal gauge variations is

```text
H^1(X;R) tensor so(3).                              (15)
```

A contractible open box has no additional linearized topological modes.  A
three-torus has nine.  Some noncommuting combinations may be lifted beyond
quadratic order.  Zero plaquette weights add untested directions, and mixed
signs can make the flat Hessian indefinite.

An exact global witness is a periodic torus with an improper matrix
`F=diag(-1,1,1)` on every stored x-edge crossing one chosen x-seam and identity
elsewhere.  Every elementary plaquette word is identity, but the
noncontractible x holonomy is `F`; it is not periodically gauge-equivalent to
the trivial connection.  Local `Q=0` therefore does not select a global flat
sector.  Conversely, a fixed boundary whose plaquette product is a proper pi
rotation forces `Q=16`, so the identity minimum is not available in every
boundary sector.

The determinant of the seam holonomy in this witness is a
`pi_0(O(3))=Z_2` component datum.  It is not the distinct
`pi_1(SO(3))=Z_2` spin-lift class, and the witness does not infer a spin,
bundle, or instanton classification from one plaquette holonomy.

## Endpoint coframe and metric response

The plaquette-holonomy connection-curvature parent gives

```text
H_A = E_0^-1 W_p E_0,
H_U = Lambda(H_A).
```

Character invariance removes the coframe exactly:

```text
Q_p = 16 - chi(W_p) - chi(W_p^-1).                  (16)
```

For the action (2), with the supplied `R_e`, `kappa_p`, and measure held fixed,
every partial derivative with respect to every endpoint coframe, metric, or
volume is therefore zero:

```text
partial S_(n,kappa)/partial E_s |_R,kappa = 0.       (17)
```

This is the requested stress calculation for the disclosed compatible
variables.  It does not license an unrestricted off-domain variation at fixed
tangent maps: changing endpoint metrics arbitrarily can violate the cited
parent chain's metric-compatibility domain.  Metric-dependent plaquette weights or volumes, a
metric-dependent measure, a derived relation `R(E)`, or matter/source terms
can all produce nonzero reciprocal response.  Equation (17) says only that the
pure fixed-`R`, constant-weight character action supplies none.

## Reflection positivity for the same action family

Let `G=O(3)`.  From `chi=8-Q/2`, equation (1) is

```text
f_n(Q) = 16/n - 2 chi^n/[n 8^(n-1)].                (18)
```

Because `chi^n` is the character of `rho^tensor n`, one crossing-plaquette
Boltzmann factor has the exact expansion

```text
w_(n,kappa)(g)
 = exp[-kappa f_n(Q(g))]
 = exp[-16 kappa/n]
   sum_(m>=0) [2 kappa/(n 8^(n-1))]^m/m!
     chi_(rho^tensor nm)(g).                        (19)
```

For `kappa>=0`, every irreducible coefficient in (19) is nonnegative.  This is
a direct representation-ring proof, not an inference from pointwise
positivity.  It also proves the expected linear-member identity

```text
e^(-kappa Q)=e^(-16 kappa)e^(2 kappa chi).           (20)
```

For `kappa>0`, every `O(3)` irreducible coefficient is strictly positive.
Indeed

```text
rho = 1 direct_sum det direct_sum V direct_sum (det tensor V),
```

tensor powers of `V` contain every integer angular momentum, the determinant
factor supplies either inversion parity, and the trivial summand pads a
required tensor degree to a multiple of `n`.  Strict full representation
support, rather than nonnegativity alone, is what supplies convolution
injectivity.

Here is the full finite reflection statement.  Take a finite open temporal
slab with a link reflection `theta` through a seam, no temporal wraparound,
and a decomposition

```text
S = S_+ + theta S_+ + S_cross.                     (21)
```

Every crossing plaquette is included exactly once in `S_cross`; product Haar
measure is normalized and reflection invariant; the two copies of `S_+` have
the same real couplings; and all crossing couplings are nonnegative.  For a
bounded observable `F` of positive-half links define the antilinear reflection

```text
(Theta F)(R) = overline(F(theta R)).
```

In temporal gauge at the seam, expand every crossing factor by (19).  A
multi-index `A` records all representation and matrix-entry labels.  Unitary
matrix-coefficient completeness gives a uniformly convergent factorization

```text
exp(-S_cross) = sum_A c_A
  overline(Phi_A(theta R_-)) Phi_A(R_+),     c_A>=0. (22)
```

Absorb `F exp(-S_+)` and `Phi_A` into the positive-half integral.  For any
finite family of bounded positive-half observables and complex coefficients,
or equivalently for their linear combination `F`, the reflected form is

```text
<Theta F,F>_S
 = Z^-1 integral (Theta F) F exp(-S) dmu
 = Z^-1 sum_A c_A
     | integral_+ F exp(-S_+) Phi_A dmu_+ |^2
 >= 0.                                                (23)
```

The partition function `Z` is strictly positive.  Restoring temporal vertex
links Haar-averages the seam by the orthogonal gauge projector `P`; because
the central crossing convolution commutes with `P`, the projected seam form
is still positive.  Thus (23) proves reflection positivity for bounded
gauge-invariant positive-half observables (and proves the temporal-gauge form
before projection).  Periodic time is not asserted; spatial topology may be
open or periodic because it remains within each reflected half.

For a negative crossing coupling, choose a relative holonomy
`r=diag(-1,-1,1) in SO(3)`.  Since `Q(I)=0` and `f_n(Q(r))=16/n`, the exact
two-history Gram is

```text
G = [[1, exp(-16 kappa/n)],
     [exp(-16 kappa/n), 1]].                        (24)
```

Its antisymmetric eigenvalue is `1-exp(-16 kappa/n)<0` for `kappa<0`.
For example, `kappa=-n log(2)/16` gives the exact rational matrix
`[[1,2],[2,1]]` with eigenvalues `3,-1`.  Thus a negative crossing sign fails
the local positive-type test.  Gauge projection can remove that mode on a
degenerate topology, so (24) is not a claim that every projected finite graph
is indefinite.

## Gauge-projected transfer and logarithm

Let a finite spatial graph have vertices `V`, stored edges `E`, and slice
configuration space `G^E` with normalized product Haar measure.  Supply
temporal vertex links `h_v`.  A crossing plaquette on edge `e` reduces to

```text
W_e = h_(s(e)) U'_e h_(t(e))^-1 U_e^-1.             (25)
```

Let `C` be the tensor product of the edge convolutions with kernels (19), let
`P` be Haar averaging over the vertex gauge action, and split the spatial
action symmetrically with

```text
m(U)=exp[-S_spatial(U)/2].
```

The exact one-step operator is

```text
T = M_m P C M_m = M_m C P M_m.                     (26)
```

Centrality gives `[C,P]=0`; gauge invariance gives `[M_m,P]=0`.  On a finite
graph the kernel is continuous on a compact space.  Hence `T` is bounded,
compact, and self-adjoint.  If every crossing coupling is nonnegative, (19)
gives `T>=0` for open or periodic finite spatial topology, provided every
crossing plaquette is included once and the two spatial half-actions are
reflections of each other.

Temporal-link Haar integration is a genuine qualification: on the unreduced
kinematic space, `ker P` lies in `ker T`.  Therefore an unqualified claim that
positive coupling makes the gauge-projected operator injective on all of
`L^2(G^E)` is false.  On the gauge-invariant Hilbert space

```text
H_phys = P L^2(G^E),                                (27)
```

or in the disclosed temporal-gauge construction before inserting `P`, strict
positivity of every crossing coupling and the full representation support
above make `C`, and hence `T`, injective.  Multiplication by `m` is boundedly
invertible because the finite spatial action is continuous on a compact
configuration space.

At zero coupling an edge convolution is projection onto the trivial
representation.  Uniform zero coupling is rank one on the raw configuration
space.  On the source-free gauge-invariant space it is injective only when the
spatial graph is a forest, whose gauge quotient is a point.  If the graph has a
cycle, its gauge-invariant space has dimension greater than one, so the
rank-one transfer has a nonzero kernel.  A Wilson-loop observable certifies the
extra dimension; after multiplication by `m`, a transfer-orthogonalized
combination, rather than necessarily the bare loop itself, is the kernel
vector.  More generally, a zero-coupling edge is harmless only when no
admissible nonconstant spin network can label it nontrivially.

On any Hilbert space where `T` is positive and injective, let
`lambda_0=||T||>0`, set `T_hat=T/lambda_0`, and define by spectral calculus

```text
H = -log T_hat.                                     (28)
```

Then `H` is a densely defined nonnegative self-adjoint operator and
`T_hat=e^-H`.  If `mu_psi` is the spectral measure of `T`, its exact domain is

```text
Dom H = {psi : integral_(0,||T||]
                   log^2(||T||/lambda) dmu_psi(lambda) < infinity}. (29)
```

Injectivity makes this domain dense.  Because `T` is generally compact with
zero as an accumulation point, `H` is generally unbounded above.  If `T` has a
kernel, no self-adjoint operator on the whole space can exponentiate to it; one
must restrict to its support or take the OS null quotient.  The normalization
in (28) fixes only an additive spectral zero.

Equations (25)–(29) are a finite mathematical reconstruction.  They do not
identify `H` as the framework's physical Hamiltonian, derive a clock, prove
Lorentz covariance, or supply gravity dynamics.

## Why the tests do not select the action

On `O(3)`, `0<=chi<=8`.  Hence every member (1) is nonnegative, has the same
unique unconstrained plaquette minimum `Q=0`, and satisfies

```text
f_n(0)=0,       f_n'(0)=1.                          (30)
```

Every member therefore has the same locality, conjugation and orientation
symmetry, the same flat Hessian (14), and the positive character expansion
(19).  Yet `f_1` and `f_2` differ at finite curvature.  For example,
`f_1(16)=16` while `f_2(16)=8`.

They also give different finite-curvature equations.  Let two proper
plaquettes incident on one link have cyclically rebased matrices about the
same axis with `(cos(theta),sin(theta))=(3/5,4/5)` and angles `theta` and
`pi+theta`, with equal orientation signs and couplings.  Their `skw` terms
cancel for `f_1`.  Their defects are `16/5` and `64/5`, while
`f_2'(Q)=1-Q/16`; hence their `f_2`-weighted residual in (11) is exactly

```text
(12/25) J != 0,    J=[[0,-1,0],[1,0,0],[0,0,0]].   (31)
```

Thus equal flat Hessians do not imply equal nonlinear stationarity equations.

This exact family proves only nonselection by the listed criteria.  A derived
Admissibility law, a semigroup or strong-curvature condition, determinant
data, metric/source coupling, or another framework-native criterion could
distinguish the members.  No broad action-selection no-go is asserted.

## Proof-obligation graph

| Obligation | Disposition |
|---|---|
| plaquette-holonomy compatible holonomy and defect | supplied by the linked parent and independently rechecked |
| exterior character and `O(3)` sectors | proved by (4)–(6) |
| ordered local link equation | proved by (7)–(11) |
| flat Hessian and null space | proved by (12)–(15), with explicit topology controls |
| fixed-connection metric response | proved exactly by (16)–(17) |
| positive crossing character coefficients | proved by (18)–(20) |
| full finite-slab reflection positivity | proved by the reflected Gram (21)–(23) |
| negative-sign falsifier | proved by (24) |
| gauge-projected transfer positivity | proved by (25)–(27) |
| injective logarithmic construction | proved on the explicitly qualified support by (28)–(29) |
| uniqueness of the action | falsified for the listed criteria by (30)–(31), not asserted as a global no-go |
| physical action, measure, temporal law, and Hamiltonian identification | open imports, not renamed as conclusions |

The proof graph is acyclic.  The generic compact-group Wilson transfer method
already appears on `origin/main`; the new scientific content is the
parent-specific exterior-character classification, ordered variation and
Hessian, improper/topological/metric discriminators, exact nonlinear
reflection-positive family, and the corrected injectivity scope.

## No-Go Discipline Gate

The note contains exact negative boundaries inside a positive bounded theorem,
so N1–N8 are recorded even though no `no_go` claim type is proposed.

### N1 — alternative routes

| Route | Attempt and result | Exact anchor | Marker |
|---|---|---|---|
| determinant or other-character action | Adding `det W` or another `O(3)` character distinguishes data that `Q` identifies, but changes the supplied action and therefore does not refute the classification of that action. | This note, (6) and the two fences immediately below it: `Q=16` identifies both the improper component and proper pi rotations. | `ATTEMPTED` |
| global Wilson-loop or boundary term | Such a term can select a noncontractible flat sector; it confirms that the topology witness is only about the plaquette-local family (2). | This note, the exact seam-holonomy and fixed-boundary witnesses following (15). | `ATTEMPTED` |
| metric-dependent weights or measure | These can generate coframe stress; they are absent from the constant-weight derivative, so the shipped statement stays at fixed `R,kappa,measure`. | This note, (16)–(17) and their explicit off-family list. | `ATTEMPTED` |
| matter or Record source coupling | A reciprocal source term can generate stress and backreaction, but is a different action family and does not refute the fixed-source-free derivative (17). | [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md), lines 175–187, place source/action and observable identification outside the axioms; this note, (17), fixes the source-free family. | `ATTEMPTED` |
| Admissibility-derived selector | A completed neighbor-conditioned probability law could distinguish `f_n`; its extensional form and values are not fixed, so this route defeats a broad selection no-go but not the narrow same-diagnostics witness. | [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md), lines 205–213; this note, (30)–(31). | `ATTEMPTED` |
| restrict to `SO(3)` | A disclosed sector restriction removes improper holonomies but is a different supplied domain; it does not change the `O(3)` classification proved here. | This note, (6), including the proper pi-rotation collision immediately below it. | `ATTEMPTED` |
| support/OS quotient | Passing to the gauge-invariant space or OS support removes projector null modes and is exactly the qualified injective route, not a counterexample to the support-qualified theorem. | This note, (26)–(29), including `ker P` and the explicit spectral domain. | `ATTEMPTED` |

All seven routes were evaluated in this cycle.  Because several remain live
for stronger physical claims, the note ships only the quantified boundaries.

### N2 — wall independence

The actual imported wall set is not collapsed into composite labels:

| Scientific label | Independently closable wall |
|---|---|
| connection | physical selection of the orthogonal edge connection `R_e` |
| action-form | physical selection of the plaquette action form `f` |
| couplings | coupling map, magnitudes, and signs |
| measure | normalized link integration measure (Haar is supplied here) |
| temporal-seam | temporal links, seam action, and reflection extension |
| gauge-space | gauge carrier/projection and choice of physical state space |
| geometry | metric-dependent weights, geometry family, or a derived `R(E)` relation |
| source | matter/Record source coupling and reciprocal variation |
| Hamiltonian-identification | identification of the support logarithm as a physical Hamiltonian |
| clock/Lorentz | physical clock and Lorentzian/Lorentz-covariant interpretation |

For every unordered pair below, `I` means that closing either member does not
automatically close the other; equivalently both directed closure questions
have answer `no`.  The diagonal is omitted as `--`.

| | connection | action-form | couplings | measure | temporal-seam | gauge-space | geometry | source | Hamiltonian-identification | clock/Lorentz |
|---|---|---|---|---|---|---|---|---|---|---|
| connection | -- | I | I | I | I | I | I | I | I | I |
| action-form | I | -- | I | I | I | I | I | I | I | I |
| couplings | I | I | -- | I | I | I | I | I | I | I |
| measure | I | I | I | -- | I | I | I | I | I | I |
| temporal-seam | I | I | I | I | -- | I | I | I | I | I |
| gauge-space | I | I | I | I | I | -- | I | I | I | I |
| geometry | I | I | I | I | I | I | -- | I | I | I |
| source | I | I | I | I | I | I | I | -- | I | I |
| Hamiltonian-identification | I | I | I | I | I | I | I | I | -- | I |
| clock/Lorentz | I | I | I | I | I | I | I | I | I | -- |

The exact witnesses also separate the closest-looking pairs.  Equations
(18)–(24) analyze the action-form and coupling walls after the connection,
measure, temporal-seam, and gauge-space inputs have been supplied, without
selecting any of them.  Equations (16)–(17) settle the fixed-family geometry
response without adding a source.  Equations (28)–(29) construct a
mathematical logarithm without closing Hamiltonian identification or the
clock/Lorentz wall.  No wall follows from another, so none is collapsed.

### N3 — hidden-wall scan

`supplied action`, normalized Haar measure, temporal links, the spatial
half-action, gauge projection, fixed endpoint variables, and finite topology
are explicit hypotheses.  `Compact-group representation` and spectral
calculus are mathematical mechanisms proved or stated at their exact role,
not hidden physical bridges.  The registered kinetic-isotropy primitive is
cited only for its OS0 graining boundary and supplies no dynamics.
The three uses of `background` are also explicit mathematical hypotheses: a
flat connection at the start of the Hessian calculation, its identity
specialization for ordinary cubical curl, and the identity-background
cohomology specialization.  None is a hidden preferred physical state.

### N4 — residual matching

| Cited witness and exact source location | Residual it supplies | Residual used here | Match |
|---|---|---|---:|
| [Plaquette-holonomy connection-curvature parent](ADMISSIBILITY_DIRAC_KAHLER_PLAQUETTE_HOLONOMY_CONNECTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-08-27.md), lines 5, 16, and 280–297 | supplied orthogonal holonomy and `Q_p`; physical edge selection, action, OS test, and physical time remain open | starting carrier plus the exact action/OS blocker quoted here | yes |
| [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md), lines 114–130 and 173–187 | neighbor-conditioned distribution, but no weight values, Hamiltonian/transfer, time metric, source/action, or physical observable identification | action-form, couplings, measure, temporal-seam, source, Hamiltonian-identification, and clock/Lorentz walls are explicit imports, not axiom consequences | yes |
| [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md), lines 13–34 and 62–75 | OS0 graining form only; no coupling, dynamics, selector, or Lorentz theorem | structural graining context only, never an action or physical-time bridge | yes |

The generic Wilson positivity and transfer notes cited in N8 and in the prior-art
paragraph are exact method precedent, but their `SU(N)` Wilson residual does not
match the parent `O(3)` exterior-character residual.  They are therefore
dropped from N4 witness support and supply no novelty or closure claim here.

### N5 — rhetoric audit

The primary cached runner lands substantive `per_element`, `per_site`,
`per_mode`, `per_block`, and `lattice_wide` lines.  The negative statements are
limited respectively to individual holonomy sectors, fixed endpoint cells,
flat/topological and transfer modes, the disclosed finite action block, and
finite-cell topology.  No continuum, arbitrary-action, Lorentz, or gravity
negative is stated.

### N6 — partial-closure and primitive scan

The primitive registry was checked at the pinned `origin/main` commit.
Kinetic isotropy is approved and already available within its boundary, but it
does not supply the temporal measure or action.  No new axiom or primitive is
required by this note.  The legitimate routes are explicit import to bounded
theorem followed by retirement: derive the action/connection from the actual
Admissibility conditional law, derive metric/source coupling, and identify the
reconstructed support operator physically.  A sector convention or temporal
gauge choice is recorded as a convention, not mislabeled as an axiom.

### N7 — steelman

A hostile reviewer should reject any global claim that the framework cannot
select an action or produce metric stress: the Admissibility axiom now supplies
a neighbor-conditioned probability distribution, and its still-open
extensional law could generate a cross-object, connection, action selector,
metric-dependent measure, or source response.  Likewise global Wilson loops,
determinant characters, and matter terms can distinguish configurations that
the pure plaquette character identifies.  This steelman is convincing, so the
broad no-go is not shipped.  The surviving claims are the exact identities and
counterexamples for the disclosed family only.

### N8 — cross-cycle echo

The cross-cycle search used the pinned `origin/main` tree.  The structurally
similar landed rows are:

| Prior wall | Current status at pinned `origin/main` | Retired? / mechanism | Application here |
|---|---|---|---|
| `COLOR_COMPOSITION_RULE_MATTER_BILINEAR_POLAR_TRANSPORT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md`, lines 66–112 and 183–207 | `bounded_theorem`, `unaudited`, effective `unaudited` | conditional polar transport exists after supplying a full-rank cross-object; physical carrier, rank sector, action, and dynamics selection are not retired | identifies the exact cross-object/nondegeneracy mechanism that remains live for the connection wall |
| `AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`, lines 381–399 | `bounded_theorem`, `unaudited`, effective `unaudited` | the positivity question is closed only after importing the Wilson action, sign, normalized Haar measure, and seam; action selection is not retired | same import-to-bounded-theorem mechanism is used in (18)–(24), with every import disclosed |
| `GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`, lines 820–835 | `positive_theorem`, `unaudited`, effective `unaudited` | finite Wilson transfer is constructed for a supplied action; neither physical-action selection nor physical-Hamiltonian identification is retired | motivates the explicit separation of action/transfer inputs from Hamiltonian and clock/Lorentz identification |
| `ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`, lines 385–431 | source status `bounded-support`; no current ledger row on the pinned tree | its fixed-background ambiguity is not a universal zero-stress wall: supplying a geometry family gives inequivalent exact first derivatives | the same mechanism remains live for geometry and source, so (17) stays fixed-`R`, fixed-weight, fixed-measure, and source-free |

None of these rows supplies authority for this note.  They expose mechanisms by
which similar walls were narrowed or conditionally crossed, and every such
mechanism is kept as a live escape.  The shipped result is therefore only
the fixed-action character, topology, metric-response, and transfer boundary.

```yaml
no_go_discipline:
  status: PASS
  negative_assertion_classes:
    - derived_no_go_boundary
    - bounded_with_named_walls
  demotion: null
```

## Review record and reproduction

The statement-level prior-art sweep was performed on `origin/main` commit
`66e478505e055faf4a5b9e6f4883211e44304718`.  It found generic `SU(N)` Wilson
reflection-positive and gauge-projected transfer theorems, but no matching
parent exterior-character variational, improper-sector, topology,
metric-response, or nonlinear-family theorem.  Generic transfer positivity is
therefore rederived and credited as prior art rather than advertised as new.

The primary and independent runners use exact symbolic or rational arithmetic.
The only logarithms appear as exact symbolic values chosen to make the hostile
two-history matrices rational; no floating output is reconstructed as exact.

Run:

```bash
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mode independent
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_independent_2026_08_28.py
```

Hostile mutations:

```bash
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation drop_top_exterior_degree
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation reverse_staple_order
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation extend_so3_formula_to_improper
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation negative_temporal_sign
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation zero_coupling_injective
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation break_closed_density_cocycle
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation break_nonlinear_flat_slope
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation erase_torus_null_modes
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation break_improper_zero_force
python3 scripts/admissibility_dirac_kahler_exterior_character_action_transfer_2026_08_28.py --mutation erase_finite_curvature_nonselection
```

Every mutation must exit nonzero.  The independent checker imports no primary
implementation path.  Independent audit remains required before any effective
retained-grade status can be assigned.
