---
claim_id: finite_native_winding_curvature_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/native_twist_check_2026_09_15.py
upstream_dependencies: ["docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md", "docs/NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08.md"]
claim_scope: "Bounded conditional finite winding curvature; supplied hypotheses and limit order retained in full proofs."
---

# Finite winding curvature

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15](NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md).
- [NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08](NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK8_NATIVE_TWISTS_AND_WINDING_CONDUCTANCE

Original source identity: `BLOCK8_NATIVE_TWISTS_AND_WINDING_CONDUCTANCE.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Which boundary twist measures native pair motion?

Personal derivation, 2026-09-15. Proposed conditional finite-volume
identities for the same supplied native low-charge Hamiltonian as Block7.
The new result is an exact distinction between two flux diagnostics, not
a physical mass or an obstruction to mobile matter. Independent review
is pending. No new action, axiom or native physical identification is used.

#### 1. Electric polarization is a configuration observable

Give each cubic edge the positive-coordinate orientation v->v+e_a and put

    E_(v,a)=epsilon_v(2 n_(v,a)-1),
    div E=2Q,
    P_a(n)=-(1/2) sum_v E_(v,a).                     (1)

This P_a is an electric polarization observable on the actual finite edge
carrier, not a choice of branch for particle position around the torus.
For a hop of signed charge q=+1 or -1 by one physical step sigma e_a,
sigma=+1 or -1 (including the wraparound edge),

    Delta E_(traversed edge)=-2 q sigma,
    Delta P_a=q sigma.                             (2)

Equation (2) follows either from the permitted bit flip or directly from
the endpoint change in div E. An alternating ring flip is a closed
oriented electric circulation; its two contributions in each participating
axis cancel. It preserves P_a. The charge penalty is diagonal and also
commutes with P_a. These assertions use the alternating gate. They are
not made for arbitrary ungated face-bit flips.

#### 2. Full two-species twist identity

Fix one axis of length L. Define H(phi_+,phi_-) by multiplying a positive
charge hop of physical step sigma by exp(i phi_+ sigma/L), and a negative
charge hop by exp(i phi_- sigma/L). Keep the native matrix-element phase,
all diagonal entries, and ring terms. Opposite orientations have conjugate
amplitudes, so this is Hermitian.

Let U_delta=exp(i delta P_a/L). Equation (2) gives the exact identity

    U_delta H(phi_+,phi_-) U_delta^*
       =H(phi_++delta,phi_--delta).                 (3)

In particular H(phi_+,phi_-) is unitarily equivalent to
H(phi_++phi_-,0). Its entire spectrum depends only on the SUM of the two
species twists. The physical-sign choice (phi_+,phi_-)=(phi,-phi) has
exactly the untwisted spectrum for every real phi and every stated finite
torus. This holds at nonuniform J_p>=0 as well, and in every fixed charge
sector where the same allowed hops and gates apply.

The twist adds phases to the existing model; no independent electromagnetic
vector potential or experimental protocol has been selected. Flatness in
(3) is a unitary-equivalence identity for this supplied diagnostic.
It is compatible with Block7's strictly positive finite-time escape.
Taking this flat finite-volume energy as a proof of immobility would be an
incorrect physical inference.

#### 3. An explicit full-configuration winding cycle

The sum twist has a different behavior. Start with the polarized ice
configuration E_(v,b)=+1 on every positive-coordinate edge, all axes b.
Its divergence vanishes. Flip the edge from 0 to e_a. The charges are
m=0 and p=e_a, and that edge now has E=-1.

Repeat the following two hops L times:

1. Move the positive charge one step forward along axis a. The edge ahead
   has E=+1, so the hop is permitted and reverses it to -1.
2. Move the negative charge one step forward along the edge immediately
   behind. That edge has E=-1, so the hop against its arrow is permitted
   and restores it to +1.

Every prefix has one positive and one negative charge at distinct sites.
After each pair of hops the single reversed edge has advanced one step.
After 2L hops the complete edge configuration and both signed positions
are exactly the initial ones. Each charge has wound once around the torus.
The total signed electric displacement is zero, as required by (2).

In the ordered signed-hole frame the untwisted product of hopping signs
is (-1)^(2L)=+1. The extra phase around this actual closed configuration
cycle is

    exp[i(phi_++phi_-)].                            (4)

Thus a sum twist not in 2pi Z cannot be removed by an endpoint phase on
the configuration graph. This construction applies to every even L>=4;
it is not a path in a truncated or auxiliary particle graph.

#### 4. Strict finite-volume response to the sum twist

For this section use the conditional full D=2 connectivity theorem in
NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08.md, together
with the native signed-hole frame. The parent proves connectivity by
six-edge cuts, directed charge paths, and chord/parking cycle reversals.
That complete argument was reread for this use. This is a supplied
provisional dependency; author checking does not confer an audit verdict.

At lambda=|t|>0, the untwisted ground energy E0 is simple and its signed-frame
vector psi is strictly positive. Taking absolute values in the magnetic
Rayleigh form gives E(phi,0)>=E0. Equality requires saturation on every
nonzero off-diagonal edge. Since the untwisted minimizing vector is psi,
all its entries are nonzero, and saturation requires the hopping phases
to be an endpoint phase throughout the connected graph. Equation (4)
contradicts this unless phi belongs to 2pi Z. Hence

    E(phi,0)>E0 when phi is not in 2pi Z.            (5)

At integer 2pi twists, the usual single-valued phase exp(i phi p_a/L)
removes the positive twist, including wraparound edges. Thus equality
holds there. This identifies the exact finite-volume minima, without a
continuum dispersion claim.

#### 5. Curvature as a weighted configuration-graph problem

Orient each unordered off-diagonal configuration edge e=(x,y) arbitrarily.
Write -a_e for its untwisted matrix element, a_e>0, and define

    c_e=a_e psi_x psi_y,
    alpha_e=positive-charge displacement along a divided by L,

with alpha=0 on negative hops and ring edges. Reverse orientations negate
alpha. A ring flip and a single hop cannot connect the same configurations,
so these edge types need no phase-combination convention.

The exact ground-state transform is

    <psi u,(H(phi,0)-E0)psi u>
       =sum_e c_e |u_y-exp(i phi alpha_e)u_x|^2.     (6)

Here sum_x psi_x^2 |u_x|^2 is the norm squared. Equation (6) follows by
expanding the two endpoint squares and using H(0)psi=E0psi for the
diagonal coefficients. Orientation choices do not affect the result.

Finite-dimensional simple-eigenvalue perturbation is legitimate near
phi=0. The first-order change of the ground vector can be taken purely
imaginary: complex conjugation sends phi to -phi, and the ground vector
is real at zero. Write that change as i psi h with h real. Expanding (6)
to second order, or solving the first-order eigenvector equation, gives

    D_L := d^2/dphi^2 E(phi,0)|_(0)
      =2 min_(h real) sum_e c_e(alpha_e+h_x-h_y)^2.  (7)

Adding a constant to h is irrelevant. This is an ordinary weighted
least-squares problem on the actual configuration graph; all unknown
ground-amplitude information is explicit in c_e.

Along the cycle C of Section3, sum_C alpha_e=1 with traversal signs.
Every gradient telescopes. Cauchy-Schwarz therefore gives, for every h,

    sum_(e in C) c_e(alpha_e+h_x-h_y)^2
       >=1/[sum_(e in C) c_e^-1],

and hence

    D_L >=2/[sum_(e in C)(lambda psi_x psi_y)^-1]>0. (8)

For equal cubic tori and uniform J, the unique positive ground state has
the symmetries used in Block7. Testing h=0 in (7) then gives

    0<D_L <=lambda c_+/(3L^2)<=4lambda/(3L^2).      (9)

The lower bound (8) is finite-volume only. The probabilities of the
specific polarized configurations may become very small as L grows.
No positive lower bound on L^2 D_L has been proved. Dropping the
minimization in (7) would discard the response of the electric background.

Equation (3) implies the two-species Hessian at zero is exactly

    D_L [[1,1],[1,1]].                              (10)

The difference direction has zero curvature; the sum direction carries
the response. Treating this Hessian as two independent free-particle
masses would therefore be unjustified even though D_L>0.

#### 6. Exact interpretation through the ground-state Markov process

This section concerns an auxiliary imaginary-time process, not a new
physical stochastic dynamics. Its transition rates are

    r_(x,y)=a_(x,y) psi_y/psi_x,
    pi_x=psi_x^2,
    (G f)_x=sum_y r_(x,y)(f_y-f_x).                 (11)

The finite connected graph and psi>0 make this a conservative irreducible
continuous-time chain. Detailed balance is pi_x r_(x,y)=c_(x,y).
The diagonal identity follows from H psi=E0 psi, so G is precisely the
ground-state transform of E0-H. No unknown state was replaced by the
uniform configuration distribution.

Let A_s add alpha_(x,y) on each jump, with the orientation convention of
Section5. In stationary initial distribution pi, its mean drift is zero
by antisymmetry. Solve the finite Poisson equation

    G h=-b,  b_x=sum_y r_(x,y) alpha_(x,y).

Solvability follows from sum_x pi_x b_x=0. Then
M_s=A_s+h(X_s)-h(X_0) is a martingale. Its mean quadratic-variation rate is

    sum_(x,y) pi_x r_(x,y)
                  [alpha_(x,y)+h_y-h_x]^2
      =2 min_g sum_e c_e[alpha_e+g_x-g_y]^2=D_L.    (12)

The minimizer equation is the same Poisson equation with g=-h. Since h
is bounded on this finite state space, its endpoint difference contributes
o(s) to the variance: its own variance is bounded and its covariance with
M_s is at most a constant times sqrt(s). Therefore

    lim_(s->infinity) Var_pi(A_s)/s=D_L.            (13)

The usual finite-state additive-functional central limit theorem also
applies. One can obtain it directly from the analytic dominant eigenvalue
of the tilted generator near zero and the nonzero finite spectral gap;
its second derivative is (12). No uniform-in-L mixing rate is inferred.
For unwrapped displacement Y_+=L A_s, the variance rate is L^2 D_L,
bounded above by 4lambda/3 in the symmetric setting of (9).

For both species, the signed difference of the unwrapped displacements
is exactly P_a(X_s)-P_a(X_0), by (2), on every trajectory. Its magnitude
is at most L^3 on a cubic torus. Thus its asymptotic variance rate at
fixed L is zero; the two winding fluctuations have the rank-one covariance
matrix corresponding to (10). This bounded-polarization argument need not
remain uniform when infinite volume is taken before long time. The order
of limits is a substantive transport obligation.

#### 7. What the next proof would have to control

The sharpened transport question is whether the weighted problem (7) has
a volume-uniform lower bound after multiplying by L^2, and whether its
response identifies a particle pole in the same infinite-volume state.
A single winding cycle supplies strict finite positivity but cannot
control the thermodynamic scale of its ground-state weights. Candidate
mechanisms are a distributed flow over winding cycles, ground-amplitude
comparison, or a direct charged-observable spectral construction.

The exact flat difference twist removes one misleading mass diagnostic.
The nontrivial sum twist and Block7 motion bounds are explicit surviving
routes. No model-wide or axiom-level negative conclusion follows.
See the committed route and negative-claim review (`BLOCK8_ROUTE_AND_NO_GO_REVIEW.md`).

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK8_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK8_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Native-motion route review and negative-claim discipline

Personal review, 2026-09-15. Read with
the twist derivation (`BLOCK8_NATIVE_TWISTS_AND_WINDING_CONDUCTANCE.md`).
Broad conclusion that native charges cannot move or the axioms must change:
**FAIL**. The exact flatness of one supplied twist is a finite operator
identity with explicit positive alternatives, not a physical no-go.

#### N1 — Actual alternatives and their outcomes

| Route | Mechanism and work performed | Honest disposition |
|---|---|---|
| Real-time local dynamics | Block7 native column orthogonality and local commutator/Duhamel bound | ATTEMPTED; positive finite-time motion established conditionally |
| Momentum-resolved spectral trial | Block7 symmetry averaging and ground-state Dirichlet identity | ATTEMPTED; controlled mean and low-energy spectral weight, no particle pole |
| Physical-sign boundary flux | Block8 electric polarization gives the exact diagonal unitary | ATTEMPTED; all finite spectra flat in this difference direction |
| Configuration-cycle topology | Block8 constructs a complete native winding tape and its holonomy | ATTEMPTED; sum twist has strict finite response, so the flatness does not generalize |
| Ground-state stochastic transform | Block8 derives reversible rates, a Poisson equation and variance identity | ATTEMPTED; exact finite auxiliary variance, uniform-volume corrector remains open |
| Background state counting | Parent uniform-state36/5 bound rederived; possible Eulerian-orientation/loop methods searched | ATTEMPTED at the stated counting bound; no asymptotic defect census or mass import |

The flux/cycle and corrector descriptions are related and are not claimed
to be independent barriers. No route is declared closed by retained
authority. The five-family procedural count supplies no exhaustiveness
argument. Positive surviving routes defeat the proposed broad negative.

#### N2 — Dependence

Flat signed-current twist, bounded electric polarization, and vanishing
fixed-volume difference-winding variance are consequences of the same
coboundary identity. They count as one diagnostic fact, not three walls.
Ground weights, thermodynamic corrector control and a particle pole are
not asserted to be independent conditions; their implication relations
remain unresolved. Independent physical-wall count: zero.

#### N3 — Premises and hidden-condition scan

The low-charge gate, alternating rings, supplied couplings and full native
carrier are explicit. Finite twist flatness does not need Perron positivity.
Strict sum-twist positivity and curvature use the parent's full D2
connectivity and signed-hole basis; that provisional dependency is named
and its proof reread. Cubic isotropy of the curvature upper bound requires
equal side lengths and uniform J. The auxiliary chain uses the actual
unknown ground vector, not a uniform surrogate. Its time is not identified
with formation time or the real-time unitary motion.

#### N4 — Matching

No prior no-go is cited as a witness. The native closed tapes and the
polarization increment address exactly the phases in the displayed
two-species twist. The weighted eight-vertex graph checks the general
perturbation/least-squares identity only; it is not a native thermodynamic
counterexample. Block7's short-time theorem concerns the same supplied
Hamiltonian and explicitly survives.

#### N5 — Resolution

Per hop: the signed polarization increment is checked on108 actual native
hops. Per site/configuration: every global degree equation is checked
along the tapes;94 gated faces preserve the complete charge vector and
polarization. Per mode: one selected uniform boundary twist is exactly
removed by the displayed unitary, not every momentum excitation. Per
sector: the two-charge positive sum response is an analytic consequence
of the named connectivity input and an explicit nontrivial cycle.
Lattice-wide: the algebra is proved for every finite stated torus; finite
tapes cover L4,L6,L8. No infinite-volume stiffness is executed or inferred.
The runner records these same scope distinctions.

#### N6 — Partial closure

Sum-flux curvature, charge-position spectral measures, distributed winding
flows, and a correctly ordered infinite-volume response remain viable.
The exact difference-flux cancellation can be handled by choosing the
appropriate observable; this requires no axiom change. The approved
structural kinetic-isotropy primitive is not declared absent or refuted.

#### N7 — Strongest objection

Finite systems often have gauge-removable twists, so zero curvature need
not reveal new physics. Correct: the useful result here is identifying
that mechanism in the actual native edge carrier, preserving all phases,
and contrasting it with a nontrivial full-configuration winding cycle.
The positive curvature has no uniform lower bound yet. Neither fact is
promoted to a particle mass or a mobility obstruction.

#### N8 — Prior comparison

The September8 native notes already establish support, phase structure,
energy bounds and connectivity. Searches of those notes find no existing
twist-curvature calculation. The delta here is the two-species unitary
identity, explicit winding holonomy, weighted curvature formula and
fixed-volume auxiliary winding-variance interpretation. Standard finite
spectral perturbation and reversible-chain machinery are not claimed as
new mathematics. Literature search results not fully read are not theorem
imports, and no external independent review has occurred.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: native_twist_check_2026_09_15](../scripts/native_twist_check_2026_09_15.py); [current cache](../logs/runner-cache/native_twist_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
