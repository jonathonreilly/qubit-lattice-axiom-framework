---
claim_id: positive_auxiliary_current_law_and_regulator_witness_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/positive_auxiliary_check_2026_09_15.py
upstream_dependencies: ["docs/FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15.md"]
claim_scope: "Positive auxiliary identity and regulator estimates; exclusion certification deferred; supplied hypotheses and full mathematical arguments retained."
---

# Positive auxiliary identity and regulator estimates; exclusion certification deferred

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

## Partial salvage disposition

Current bounded mathematics consists of the positive auxiliary identity, explicit planar-loop sequence and lower bounds, and the translation-escape calculation, with all original hypotheses. The class-wide statement that no fixed integrable unshifted quadratic regulator uniformly bounds the declared planar-loop family has DEFERRED N1 NEGATIVE CERTIFICATION. Its reviewed mathematical derivation is preserved below, but this landing does not accept or certify that negative claim. No five distinct in-domain attack routes have been established; finite controls and the positive identity do not certify exhaustion.

The complete original text below is retained for mathematical context and recovery. Its class-wide exclusion and foundation-selection interpretations remain subject to the explicit dispositions here; historical headings or review language do not override them.

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15](FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK6_PLANAR_LOOP_AND_QUADRATIC_REGULATOR_TEST

Original source identity: `BLOCK6_PLANAR_LOOP_AND_QUADRATIC_REGULATOR_TEST.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Planar loops test a fixed Gaussian regulator

Personal conditional mathematical derivation, 2026-09-15. This rejects
one proposed uniform auxiliary-activity bound. It does not prove failure
of a field limit, of renormalization methods, or of the framework axioms.

#### 1. Area and energy can have different orders

In Z^4 let S_L be the unit integer sheet of L^2 faces in a coordinate
two-plane, with square side L. Its boundary current j_L=D*S_L has
mass4L, squared l2 norm4L, and

    ||S_L||^2=L^2, E_L=||P S_L||^2=<j_L,G_1 j_L>.

The cubic Hodge Green operator is the scalar lattice Green kernel on
each orientation. Its entries are nonnegative: use the nonnegative
continuous-time random-walk heat kernel and integrate over time.
Each of the two current orientations consists of two parallel, opposite
segments of length L. The negative cross interaction between those
opposite segments can be dropped for an upper bound. A segment's
self-energy is at most

    L sum_(n in Z) G_4(n e_1)=L G_3(0).

The equality follows by summing the heat kernel over that coordinate
(Tonelli applies to its nonnegative entries), leaving the three-dimensional
walk. Hence

    E_L <=4 L G_3(0)<=C L, C=sqrt(3) pi/2.          (1)

For the explicit constant, lambda_3(p)>=4|p|^2/pi^2 on [-pi,pi]^3,
and this cube is contained in the ball of radius sqrt(3)pi. Therefore

    G_3(0)<= (pi^2/4) integral_(|p|<=sqrt(3)pi)
                       |p|^-2 dp/(2pi)^3
           =sqrt(3)pi/8.

No numerical Green value or continuum replacement is used. In particular
the coexact part obeys ||Q S_L||^2>=L^2-C L. This is an explicit family
with filling area growing quadratically and boundary energy at most
linearly. It is stronger for this family than the general l1-l2 energy
bound from Block4.

#### 2. Match the free finite boxes, instead of importing an infinite bound

For a fixed finite sheet S, exhaust Z^4 by free contractible cubes
containing its support. Let P_R be their exact face projections, and
extend P_R S by zero outside each cube. Their l2 norms are bounded by
||S||, and ||P_R S||^2=<S,P_R S>.

Every weak limit u is closed: on each fixed interior three-cell,
B P_R S=0 once the cube is large enough. In l2 on Z^4 the Fourier
exterior-algebra identity gives ker B=closure(im D). For any compactly
supported edge field a, Da lies inside a sufficiently large cube and

    <P_R S,Da>=<S,Da>.

Thus the weak limit is exactly P S. The displayed norm identity then
gives convergence of the squared norms to ||P S||^2 and hence strong
convergence. All subsequences have that same limit. Consequently, for
each L one can choose a finite free cube with

    E_(L,R)=||P_R S_L||^2<=2 C L.                   (2)

No bound on the required cube size is claimed. This existence statement
is enough to challenge a constant asserted uniform in all free volumes.
No torus harmonic mode has been dropped in this argument.

#### 3. The tested activity and the precise regulator contract

Use A0,T,R from the positive auxiliary note in such a finite cube. For
the pair of orientations of one electric current define

    F_S(eta)=exp[-g^2 S.RS/2] cosh(g eta.TB S).

Consider the fixed quadratic regulator

    G_kappa(eta)=exp[kappa eta.A0^-1 eta/2],
    0<kappa<1,
    ||F_S||_kappa=sup_eta F_S(eta)/G_kappa(eta).      (3)

The upper restriction is exactly Gaussian integrability:
E_gamma(A0) G_kappa=(1-kappa)^(-dim(V)/2)<infinity in
each finite volume. This particular expectation is not asserted to be
uniform in volume. The test concerns a uniform small activity norm.

Put a=TB S and Q_R=I-P_R. From the exact matrix identities,

    a.A0 a=S.(R-P_R)S=:U_S,
    S.RS=E_S+U_S,
    U_S>=||Q_R S||^2.

Evaluate the supremum at eta=(g/kappa)A0 a and use cosh(t)>=exp(t)/2:

    log ||F_S||_kappa
      >=-log2+(g^2/2)[(kappa^-1-1)U_S-E_S].         (4)

For S=S_L and the sufficiently large free cube in (2), this is at least

    -log2+(g^2/(2kappa))[(1-kappa)L^2-2 C L],       (5)

which tends to positive infinity for every fixed g>0 and kappa<1.
For example the lower bound turns positive in its quadratic bracket
once L>2C/(1-kappa). Increasing the fixed electric coupling g does not
repair it. The lower bound is on the actual single positive activity,
not on a loose upper majorant. These S_L are ordinary planar fillings,
not large artificial additions of a closed sheet to one fixed current.

A regulator formed from only part of this positive quadratic energy
cannot improve this supremum bound. The conclusion does not cover a
different nonquadratic regulator, a current-dependent center, an
operator-valued norm, or a cancellation between a differently grouped
set of terms. Nor does it say that all polymer norms used in the
literature have exactly the form (3).

#### 4. Constructive escape retained

The exact translation eta -> xi=eta+gGBS in the companion note replaces
F_S by exp[-g^2 E_S/2] times a shifted bounded positive theta function.
It removes the offending filling-area term from the activity exactly.
What remains is a nonlocal dependence of that theta function on the
current through GBS, with integer periodicity. Therefore (5) is a reason
to use that translated representation or a different organization; it
is not a wall on the physical model. The full coupled source estimate
remains to be supplied.

#### 5. A separate duality-to-Gaussianity control

Even a self-dual scalar source relation need not force Gaussianity.
Let sigma^2=1/2, He4(z)=z^4-6z^2+3, and epsilon=1/16. The density

    p(x)=Gaussian_(sigma^2)(x)[1+epsilon He4(x/sigma)]

is positive and normalized: min He4=-6 and its Gaussian integral is0.
It has mean0 and variance1/2. Direct Gaussian differentiation gives

    M(t)=exp(t^2/4)(1+epsilon t^4/4),
    chi(t)=exp(-t^2/4)(1+epsilon t^4/4),
    chi(t)=exp(-t^2/2) M(t).                        (6)

The characteristic function is positive for every real t. Also
M(t)<=exp(t^2/2): with u=t^2/4, use
1+4epsilon u^2<=1+u+u^2/2<=exp(u). Nevertheless
its fourth cumulant is6epsilon=3/8, not zero. This is an explicit
probability counterexample to that logical shortcut, not a lattice
gauge state or an axiom-compatible alternative TOE.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK6_POSITIVE_AUXILIARY_CURRENT_REPRESENTATION

Original source identity: `BLOCK6_POSITIVE_AUXILIARY_CURRENT_REPRESENTATION.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### A positive auxiliary field with both clock defect sectors

Personal derivation, 2026-09-15. Conditional on the supplied finite-clock
Villain law, this is an exact finite-volume representation. It does not
establish its infinite-volume state, a Gaussian scaling limit, or a native
selection of the law. General lattice Poisson duality is already used on
main; the delta here is its resolved Gaussian/current representation,
including the full physical source and an explicit filling-change check.

#### 1. Finite free complex and normalization

Use the contractible free cubic complex with D=d1, B=d2, and C=d3.
Counting inner products and positive cell orientations are understood.
Let P project onto im D and Q=I-P=B*G B, where G=(BB*)^-1 on
V=ran B=ker C. Only this subspace is integrated below. Set

    b=2pi sqrt(beta), g=N/sqrt(beta), bg=2pi N,
    0<c<1/16, A0=G-cI on V, T=(I-c BB*)^-1 on V,
    R=I+c B*T B=(I-c B*B)^-1 on face fields.

The free cubic incidence has squared norm at most16, so A0 is positive.
The choices c=1/32 and fixed finite N,beta will be used in the checks.
The identities used repeatedly are

    A0 T=G,
    B*T A0 T B=R-P,
    RP=P, RQ=QR, R>=I.                               (1)

Magnetic charges range over the lattice L_m=B Z^faces in V. This avoids
silently replacing an integer image lattice by a real kernel or introducing
torus harmonic sectors. Define

    Theta_c(eta)=sum_(q in L_m)
          exp[-b^2 c ||q||^2/2] exp[i b q.eta].

Finite-dimensional Poisson summation on the full-rank lattice L_m in V
proves Theta_c(eta)>0 for real eta. All its derivatives are legitimate
finite-dimensional Gaussian theta series. Put

    mu(deta)=Z_m^-1 Theta_c(eta) gamma_A0(deta),
    Z_m=sum_q exp[-b^2 q.Gq/2].                       (2)

This is a positive probability, since Gaussian integration of Theta_c
gives Z_m. No assertion that its potential is uniformly convex is needed
for the representation.

#### 2. Haar source identity, derived on the same finite complex

The continuous Haar link/image flux decomposes as

    X_H=P W-b B*G q,

where W is a standard face Gaussian, q has weight proportional to
exp[-b^2 q.Gq/2], and the two are independent. Free contractibility and
constant fiber multiplicity justify the image quotient. Consequently

    chi_H(v)=exp[-v.Pv/2]
       Z_m^-1 sum_q exp[-b^2 q.Gq/2-i b q.GBv].       (3)

For real face v, Gaussian integration and (1) give the alternative identity

    chi_H(v)=exp[-v.Rv/2]
                E_mu exp[-eta.TBv].                 (4)

Indeed the integrand's q term has Gaussian expectation

    exp[ (TBv).A0(TBv)/2
          -i b q.A0 TBv-b^2 q.A0q/2].

The cross term is -i b q.GBv; cI+A0=G; and
R-B*T A0 T B=P. This proves (4), rather than presuming a random
Gaussian decomposition of X_H. Its right side uses a real moment
generating function. It is not a convolution of two real independent
random fields with covariances of opposite sign.

#### 3. Impose the actual clock through conserved currents

Let J={j in Z^edges:d0*j=0}. For each j choose any integer face filling
S_j with D*S_j=j. Fourier expansion of the link clock comb, followed by
gauge integration, gives for the original lifted clock flux X

    chi_clock(h)=sum_(j in J) chi_H(h+g S_j)
                    /sum_(j in J) chi_H(g S_j).      (5)

The same identity follows by Poisson summation on the clock flux lattice
(b/N)(D Z^edges+N Z^faces). Gauge multiplicities are constant and cancel.
For each fixed finite complex these sums converge absolutely: the real
Haar representation (3) bounds the q sum by Z_m, while the electric
Gaussian factor is coercive in j, including the fixed linear source.
The expression is independent of S_j: an integer difference U with
D*U=0 has U.X_H in b Z, so exp[i g U.X_H]=1.

Substitute (4) in (5). Each term is positive for real h. Tonelli now
produces a positive joint probability on (eta,j):

    nu(deta,j) proportional gamma_A0(deta) Theta_c(eta)
       exp[-g^2 S_j.R S_j/2-g eta.TB S_j].           (6)

Set Y=-B*T eta-g R S_j. The full source identity is

    chi_clock(h)=exp[-h.Rh/2] E_nu exp[h.Y].         (7)

There are no discarded defect species and no interpretation of a complex
pair weight as a probability. Finiteness of (6) follows from (5), or from
the change of variables in the next section. The same calculations with
real linear sources give all required exponential moments. Reflection
of both eta and j centers Y. In particular,

    Cov(X)=R-Cov(Y),
    cumulant_(2k)(X)=(-1)^k cumulant_(2k)(Y), k>=2,   (8)

with the tensor identity interpreted by polarization. Odd cumulants
vanish. These are relations, not bounds that make the higher cumulants
small. They are consistent with the general positive dual-lattice formula
already present in the repository.

#### 4. Translate the Gaussian instead of paying a filling-area factor

In (6) set xi=eta+g G B S_j. Completing the square, using (1), gives

    nu'(dxi,j) proportional gamma_A0(dxi)
        exp[-g^2 ||P S_j||^2/2]
        Theta_c(xi-g G B S_j),                      (9)

and the source variable simplifies to

    Y=-B*T xi-g P S_j.                              (10)

The quadratic filling norm in (6) has disappeared from the activity in
(9); the remaining electric energy depends only on the current. Equation
(9) is positive and exact, not a most-probable-point replacement.

It is also pointwise independent of the integer filling. If U is an
integer face field with D*U=0 and q=B n is an allowed magnetic charge,

    q.GB U=n.Q U=n.U in Z.

Thus Theta_c(xi-gGB(S_j+U))=Theta_c(xi-gGB S_j), because bg=2pi N.
Also P(S_j+U)=P S_j. Consequently the right sides of both (9) and
(10) need no preferred integer filling, although a filling can be used
to calculate them. This exact periodicity is lost if N is treated as a
generic real parameter or if the current lattice is replaced by its span.

One can describe the carrier geometrically. Put

    U=B*xi+g P S_j.

Then Y=-R U. Its carrier is im B*+g P Z^faces, equivalently
im B*+g Z^faces, with Lebesgue measure on each coexact fiber and
counting measure on the discrete exact quotient. This is the exchanged
electric/magnetic support; no claim of matched free/relative boundary
self-duality is made merely from that description.

In a local magnetic filling representation, the phase in Theta_c is

    exp[i b n.B*xi-i bg n.Q S_j]
      =exp[i b n.(B*xi+g P S_j)].                   (11)

The integer phase bg n.S_j is the reason for the equality. Thus the
usual real magnetic extension can be evaluated at U, subject to its own
proved extension and locality bounds. Its argument contains P S_j;
the current/field coupling has not become a local independent product.

#### 5. Identify the resulting field: a smoothed dual clock lattice

The positive representation should not be mistaken for an easier theory
merely because its variables look different. It can be identified exactly.
The original X is the centered unit-precision Gaussian on the full-rank
lattice Lambda=(b/N)(D Z^edges+N Z^faces). Let Z_d be the centered
unit-precision Gaussian on Lambda_d=2pi Lambda*. Ordinary Poisson
summation, with every finite normalization canceled, gives

    chi_X(h)=exp[-||h||^2/2] E exp[-h.Z_d].          (12)

Compare (12) with (7). Uniqueness of finite-dimensional moment generating
functions gives

    Y has law -Z_d+W, W independent Gaussian(R-I).  (13)

Here R-I is positive semidefinite, and degenerate Gaussian directions
are permitted. This is an actual real independent-noise identity for Y;
it does not turn (7) into a real independent decomposition of X.

For clarity, integer character annihilation gives

    Lambda_d=(1/sqrt(beta)) L_N,
    L_N={n in Z^faces:D*n in N Z^edges}
       =N Z^faces+B* Z^three-cells.                 (14)

For the last equality, write D*n=N j. Conservation makes j an integer
cycle; free integral homology supplies S with D*S=j. Then n-N S is
an integer two-cycle and hence B* of an integer three-chain. The reverse
inclusion is immediate. The factor is 1/sqrt(beta), not g. Under Hodge
duality this is the exchanged clock coupling with the matched relative
boundary structure, not an automatic equality to the original free-box
ensemble. No boundary-state independence is assumed.

Put K=R^-1=I-cB*B. Equations (10) and (13) identify U in law as

    U=K(Z_d+W), W independent Gaussian(R-I),        (15)

changing the harmless sign of W if needed. Centered lattice Gaussian
domination gives Cov(Z_d)<=I, so this coupling obeys

    Cov(U)<=K,
    E |h.(U-Z_d)|^2<=h.(I-K)h=c||Bh||^2.           (16)

Indeed the two independent errors contribute at most
(I-K)^2+K(R-I)K=I-K. For smooth four-dimensional tests
h_a(p)=a^2 f_p(a x), ||B h_a||^2=O(a^2), away from the free boundary.
Thus U and this specific dual flux have the same possible limiting
finite source laws. Fixed c,N,beta suffice. The representation closes
back onto the dual clock problem; it has not removed the need for its
infrared analysis. This is a useful exact route comparison rather than
a new proof of Gaussianity.

#### 6. What the representation changes and what it leaves

The real-tilt form (6) is a candidate entry to an auxiliary Gaussian
expansion. The translated form (9) avoids its explicit large real tilt,
and retains positivity and exact filling independence. The companion
note tests the simplest fixed quadratic regulator for (6) and shows why
large planar loops defeat that particular estimate. That failure does
not defeat (9), adaptive shifts, an expansion in blocks, or a direct
response argument on the positive support.

To use (9) for the full field one still needs a uniform estimate on the
coupled current/field measure and its diffuse-source higher cumulants,
then the same physical state and quadratic limit. Conditional Gaussian
integration or a small magnetic extension alone does not supply those
steps. No new axiom, phase assertion, or independent retained grade is
introduced here.

#### Finite author checks

The checker constructs a free three-cube, with its five independent
integer current coordinates, as a finite cochain normalization challenge.
It compares the original 32,243,1024 gauge-fixed clock configurations and
positive image sums with independent Gaussian quadrature of (9), at
(beta,N)=(.25,2),(.5,3),(.8,4). It checks complete six-face source and
covariance identities and projected/mixed fourth cumulants. These
three-cubes are not thermodynamic four-dimensional evidence. Integer
cutoffs3/4, image cutoffs8/10 and quadrature orders120/160 are compared,
without an interval certificate. Exact rational cochains check (1),
the square completion and the allowed filling change. A noninteger-N
control loses that periodicity. The written proof carries the general
finite-dimensional statement.

<a id="owned-argument-3"></a>
## Owned argument 3: BLOCK6_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK6_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Block6 route comparison and scoped negative review

Personal review only, 2026-09-15. The two mathematical notes and their
runner were read in full. No independent audit or effective retained
grade is represented. The broad claim that the model or axioms cannot
work is **FAIL**. The narrow fixed-regulator counterexample remains.

#### N1 — Materially different mechanisms considered

| Mechanism | Work actually done | Disposition |
|---|---|---|
| Hybrid reversible generator and pointwise curvature | Block1 exact positive dynamics and actual negative curvature fixtures | That curvature criterion fails; integrated response remains open |
| Bounded rates and integrated jump identities | Block1 exact rate changes and moment identities | Positive alternative, no uniform mixing theorem |
| Signed loop plus contact/Gaussian registers | Blocks2/4 derive prescribed source bounds and exact graph counts | Restricted family controlled; full graph organization open |
| One Gaussian auxiliary with real electric tilts | Block6 derives the full positive source identity and tests its fixed quadratic regulator | Exact representation; proposed uniform activity bound fails on planar loops |
| Current-dependent Gaussian translation | Block6 completes the square and checks integer filling independence | Constructive escape from the particular regulator failure; nonlocal current coupling remains |
| Positive dual lattice with independent Gaussian smoothing | Block6 resolves the translated field through Poisson duality | Exact return to the dual clock problem, not a new proof of its limit |
| Scale-by-scale local Gaussian perturbation | Primary Brydges-Keller proof read; Brydges-Dimock-Hurd opening/norms inspected | Literature route remains open; initial local norm and full coupled model not matched |

These are mechanisms, not a quota of alleged independent obstructions.
The literature route is not described as an executed finite-clock proof.
No route has been marked ruled out by prior retained authority.

#### N2 — Dependence and wall count

The real-tilt regulator failure and the successful current-dependent
translation concern the same representation. The latter removes the
large-area cost from the activity and hence defeats an all-representation
negative claim. The dual identification is an exact algebraic consequence,
not a second obstruction. Asserted independent physical-wall count: zero.

#### N3 — Hidden premises

Finite free contractible complex, counting metric, specified Villain law,
integer N, full image lattice, matched inverse on ran B, c<1/16 and the
regulator's fixed kappa<1 are explicit. Integer homology is used only on
the free cube. No periodic harmonic sector is discarded. Local relative
boundary data on the dual are retained. The auxiliary Gaussian is not an
assumed physical carrier or physical clock. No axiom is amended.

#### N4 — Residual matching

The source check compares actual finite clock/image sums with a positive
Gaussian/current integral and with an independently enumerated dual lattice.
It tests full six-face sources, covariance and fourth cumulants. Exact
cochains check square completion and filling changes. The large-loop
statement uses a nonnegative lattice Green kernel and an explicit free-box
projection exhaustion proof. Fourier grids merely challenge the infinite
normalization; they do not compute that exhaustion or certify its limit.

The rejected bound is specifically sup F_S/G_kappa, with F_S and G_kappa
displayed in the note. It is an actual lower bound on that activity norm,
not divergence of an upper estimate and not a lower bound on physical
non-Gaussianity. The scalar self-duality example refutes only a proposed
logical implication, not a gauge theory.

#### N5 — Resolution and rhetoric

The runner prints per_element, per_site, per_mode, per_block and lattice_wide
scope lines. Initial finite cube calculations passed before a structural
expanded-versus-factored polynomial assertion failed. Its exact-zero
diagnosis, source and stdout are frozen under review/block6_initial_symbolic_failure.
The comparison now expands the difference; no science formula or tolerance
was changed. Finite quadratures and cutoffs are not interval certified.

The final extended check also compares the positive representation with
the dual lattice and its independent-noise law. Its source, covariance and
fourth-cumulant identities pass. No result is labeled an infinite simulation.

#### N6 — Partial closure and positive escapes

The translated positive representation is explicit and survives. A
current-dependent regulator, blocked renormalization, a suitable operator
norm, or a direct response estimate could still control the full field.
The existing real-C3 extensions do not require a uniform complex strip.
Thus failure to enter one analytic norm is not failure of every RG route.
Further work should resolve one of these remaining mechanisms or turn to
another physical bottleneck, rather than recount Poisson duality as progress.

#### N7 — Strongest objection

A reviewer could correctly object that Gaussian smoothing and duality were
already known, and that a poor fixed regulator says nothing decisive about
the model. The notes explicitly make both points. Their limited delta is
the resolved positive joint source representation, its filling-independent
translation, the identification with dual smoothing, and a genuine planar
counterexample to the tested norm. No axiom-level wall is inferred.

#### N8 — Prior comparison

Main's clock smoothing and exact dual covariance sources were re-read at
the current source checkout; remote main remains2ed54cb83a4cb6b336e7053e19c8010d5d2930d8.
The general lattice Poisson formula is credited as existing machinery.
Earlier imaginary-field/area cautions were bounds on a proposed series;
the present fixed-quadratic-regulator test has its own displayed lower
bound and explicit finite-volume matching. Its successful translation is
preserved in the same packet. This supports a narrower method decision,
not a repeated or stronger framework no-go.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: positive_auxiliary_check_2026_09_15](../scripts/positive_auxiliary_check_2026_09_15.py); [current cache](../logs/runner-cache/positive_auxiliary_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).

## Certification and recovery conclusion

Current bounded mathematics consists of the positive auxiliary identity, explicit planar-loop sequence and lower bounds, and the translation-escape calculation, with all original hypotheses. The class-wide statement that no fixed integrable unshifted quadratic regulator uniformly bounds the declared planar-loop family has DEFERRED N1 NEGATIVE CERTIFICATION. Its reviewed mathematical derivation is preserved below, but this landing does not accept or certify that negative claim. No five distinct in-domain attack routes have been established; finite controls and the positive identity do not certify exhaustion.

N1 certification is not granted by a changed label, numerical agreement, or this preservation of the original proof. The original route records remain available below and in the exact archive. The original branch must remain as the recovery handle when this PR is closed after partial salvage.
