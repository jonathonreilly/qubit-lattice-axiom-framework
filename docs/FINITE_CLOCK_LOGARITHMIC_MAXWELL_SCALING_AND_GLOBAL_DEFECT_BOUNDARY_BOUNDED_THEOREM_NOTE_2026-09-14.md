---
claim_id: finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For the supplied finite-clock Villain law on equal even four-tori, the explicit logarithmic family beta=ceil(4log(2L^4)), N=8beta has the score-field Gaussian Maxwell limit with all smeared moments, principal-flux distribution limit, and relative separated rectilinear Wilson-loop Coulomb limit, conditional on the direct source's integer geometry and continuum/OS lemmas. Local defect tails and injected integer-current theta sums replace volume-dimensional packing; a bounded line-current potential controls thin Wilson sources. At fixed beta the positive lift's globally exact sector instead has exponentially small probability, and uniform dual theta smallness requires growing sigma. Those are boundaries of global defect/theta removal, not obstructions to a fixed-law infrared phase or to the axioms."
upstream_dependencies:
  - finite_clock_direct_maxwell_scaling_and_coulomb_wilson_interactions_bounded_theorem_note_2026-09-14
runner: scripts/finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_2026_09_14.py
---

# Logarithmic finite-clock Maxwell scaling and global defect removal

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

A supplied finite-clock Villain family with coupling and alphabet of order
logarithmic in the volume already has the Maxwell and external Coulomb
limits specified below. The proof uses local defect quantization and
integer-current theta estimates. It also identifies the limitation of this
method: at fixed coupling, a completely defect-free lift has probability
tending to zero. Positive defect density does not rule out a massless phase.

This is a proposed theorem pending independent review and formal audit.
The direct source linked below is also provisional; its appearance in a
PR does not establish its proof. No axioms or primitive registries change.

## Status and dependency map

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Reduce the supplied Maxwell family's growing microscopic resources and distinguish a fixed-law phase from global defect exclusion."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the local-tail and theta derivation, then obtain fixed-law connected-correlation estimates rather than require zero defects everywhere."
conditional_surface_status: "Uses the explicitly provisional direct source's integer geometry, physical field discretization, Green limit and Gaussian OS construction."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "New analytic finite-volume estimates imply an explicit logarithmic family, with finite checks and narrow method-boundary countercontrols; neither dependency nor conclusion has formal retained status."
```

The sole scientific repository premise is
[the direct finite-clock source](FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md),
originally committed at44faa4d4ce09b8634726cef62a84146f940eb233.
Its precise uses are:

| Imported lemma | Use here | Status |
|---|---|---|
| Positive lifted clock law, constant fibers and saturated integer curl lattice | Defines M and identifies the exact sector | Provisional proof, independent review pending |
| Four-torus Hodge norm, integer periods and minimum dual-vector length | Local defect quantization and source condition(A) | Provisional proof, independent review pending |
| Midpoint cell averages and continuum Hodge limit | Converts source covariance to the Maxwell field | Provisional proof, independent review pending |
| Score conditioning and principal-flux coupling | Transfers to actual bounded clock observables | Provisional proof, independent review pending |
| Heat-kernel estimates and off-diagonal periodic Green limit | Bounds line potentials and separated Wilson pairings | Provisional proof, independent review pending |
| Relative Wilson ratio algebra, subsequent time/return-charge limits and explicit Gaussian OS quotient | External Coulomb interaction and two transverse linear modes | Provisional proof, independent review pending |

This source derives the improved probability bounds, integer-current theta
majorant, potential-source estimate, logarithmic parameter sequence and
global-method lower bounds. It imports no all-affine covariance theorem.
The physical model, varying alphabet, coupling, spacing and probe strengths
are supplied. A fixed-N=3 Hamiltonian phase, native law selection and
dynamical charged matter remain open.

## 1. Target and leverage

Replace the sufficient beta=64L^4,N=8beta family by beta of order log V and
N=8beta, where V=L^4 on equal even four-tori. Preserve Gaussian scaling of
actual bounded score fields and relative Wilson loops. Diagnose why this
GLOBAL defect-removal method cannot prove a fixed-coupling phase.

Definitions: K=d_1 Z^E is saturated in S=im d_1; M=K+NZ^P;
sigma=N^2/(4pi^2 beta); X=z/sqrt(sigma) for z in M with centered Gaussian
weight exp(-|z|^2/(2sigma)). The exact positive lift has z=da-Nk and
X=sqrt(beta)(dtheta-2pi k). Conditional on the clock angles, all integer
image labels k_p are independent discrete Gaussians.

Write P_e for projection on S, and P_h for the six harmonic plaquette
modes. There are 4V edges,6V faces,4V elementary three-cubes.

## 2. Centered Gaussian domination and local defect tails

Completing the square for the full-rank lattice M gives

 E exp(<h,X>) = exp(|h|^2/2) Z_M(-sqrt(sigma)h)/Z_M(0)
              <= exp(|h|^2/2).

The last inequality is the centered theta maximum: Poisson summation has
positive Gaussian Fourier coefficients, so the real shifted theta is at
most its value at zero. This is valid for every real h, with no covariance
or phase premise. Hence for any real vector v and u>=0,

 Pr(|<v,X>|>=u) <= 2 exp(-u^2/(2|v|^2)).

For one oriented three-cube c, dX_c=-2pi sqrt(beta) (dk)_c. The incidence
vector d_2^*1_c has exactly six coefficients +/-1 and squared norm6.
Thus

 Pr((dk)_c !=0) <= 2 exp(-pi^2 beta/3),
 Pr(dk !=0) <= 8V exp(-pi^2 beta/3).                     (2.1)

If dk=0, integer periods of k are six integers kappa_{mu nu}. On equal
four-tori the unit harmonic form h_{mu nu} has value L^-2 on every face
of its orientation, so <k,h_{mu nu}>=kappa_{mu nu}. The exact part dtheta
has zero harmonic projection. Therefore

 Pr(dk=0 and P_h X !=0) <= 12 exp(-2pi^2 beta).          (2.2)

If both dk and the harmonic periods vanish, X is real exact and the
saturation of K makes z an element of K. Conversely z in K implies these
conditions. Consequently

 p_bad := Pr(z not in K)
 <= min(1,8V exp(-pi^2 beta/3)+12 exp(-2pi^2 beta)).      (2.3)

This uses local integer defect quantization instead of packing the entire
perpendicular lattice in dimension3V+3. It retains harmonic sectors.

## 3. Integer-current theta bound

For w in K^* subset S, a=d_1^*w is in Z^E: <a,e>=<w,d_1 e> is an integer
for every unit edge. The map is injective, because a=0 with w in im d_1
forces w=0. In Fourier coordinates ||d_1||<=4, hence |a|<=4|w|.
Thus for t>0,

 sum_{w in K^*,w!=0} exp(-t|w|^2)
 <= theta_1(t/16)^(4V)-1,
 theta_1(u)=sum_{n in Z} exp(-u n^2).                  (3.1)

The right side overcounts many currents, but is explicit. For u>=1,

 theta_1(u)-1 <= 2 exp(-u)/(1-exp(-3u)) <= 3exp(-u).

The first inequality uses n^2>=1+3(n-1) for n>=1; the second is strict
already at u=1. Therefore define

 eta_sigma := theta_1(pi^2 sigma/16)^(4V)-1
 <= exp(12V exp(-pi^2 sigma/16))-1                      (3.2)

when pi^2 sigma/16>=1. The exponential in the written finite sum is
controlled analytically; numerical truncation is not a tail proof.

## 4. Uniform shifted relative characteristic estimates

For b in S the affine discrete Gaussian on b+K, normalized with variance
sigma, has characteristic C_b(h), for h_e=P_e h. Poisson summation gives

 C_b(h)/G(h)
 = [1+sum_{w!=0} exp(-2pi^2 sigma|w|^2
                +2pi sqrt(sigma)<w,h_e>) exp(2pi i<w,b>)]
   /[1+sum_{w!=0} exp(-2pi^2 sigma|w|^2) exp(2pi i<w,b>)],
 G(h)=exp(-|h_e|^2/2).                                 (4.1)

Changing w to -w reverses the source and phase signs together. Reversing
only one generally changes the answer; the source term is REAL.
Two alternative sufficient source conditions control the numerator tail:

(A) |h_e|<=pi sqrt(sigma)/8. Since each nonzero w has length>=1/4,
    2pi sqrt(sigma)|<w,h_e>|<=pi^2 sigma|w|^2.

(B) Put psi=(d_1^*d_1)^+ d_1^*h. Then <w,h_e>=<a,psi>. If
    ||psi||_infinity<=pi sqrt(sigma)/32, integrality gives
    |a|_1<=|a|^2, and

 -2pi^2 sigma|w|^2+2pi sqrt(sigma)<a,psi>
 <= -pi^2 sigma|a|^2/8+pi^2 sigma|a|_1/16
 <= -pi^2 sigma|a|^2/16.

In either case the numerator tail is at most eta_sigma; so is the
denominator tail. If eta_sigma<1 then, uniformly in every b,

 |C_b(h)/G(h)-1| <= 2eta_sigma/(1-eta_sigma).            (4.2)

The full M law is a positive mixture of these affine K laws with fixed
perpendicular representatives. Its exact coset has no perpendicular
source phase, and the other phases have unit modulus. Hence

 |E exp(i<h,X>)/G(h)-1|
 <= 2p_bad+2eta_sigma/(1-eta_sigma).                    (4.3)

This bound controls a relative error even if G(h) tends to zero. The
perpendicular-source contribution is bounded by2p_bad rather than by an
absolute error subsequently divided by a small Gaussian expectation.

## 5. Logarithmic sequence and actual local fields

For V=L^4 and even L>=4 take

 beta=ceil(4 log(2V)), N=8beta, sigma=16beta/pi^2.       (5.1)

These are finite clock alphabets, varying only logarithmically with V.
Here pi^2 sigma/16=beta and

 eta_sigma <= exp(3/(4V^3))-1,
 p_bad <= 8V(2V)^(-4pi^2/3)+12(2V)^(-8pi^2).

Both vanish. Any bounded-L2 source family satisfies(A) eventually. With
spacing a->0 and physical side aL->infinity, cell-average sources
(J_a f)_p=a^-2 integral_{cell(p)}f satisfy ||J_a f||<=||f||. The precise
midpoint Hodge/Riemann-sum argument in PR8130 yields

 <J_a f,P_e J_a g> -> <f,P_Maxwell g>.

The bounded physical score Y=-phi_beta'(dtheta)/(sqrt(beta)phi_beta(dtheta))
is E[X|theta]. The conditional independent Gaussian images give

 E|<h,X-Y>|^2 <= (8pi^2 beta+16)exp(-pi^2 beta/2)||h||^2.

Thus the characteristic limit in(4.3) transfers to Y. Conditional Jensen
also gives E exp(<h,Y>)<=exp(||h||^2/2), uniformly in V. These real MGF
bounds give uniform integrability of every fixed smeared moment. The score
field converges with all joint moments to the same Gaussian Maxwell field.
Uniform test variance and the local Sobolev trace/compact embedding argument
in PR8130 give convergence as local H^-s random distributions for s>2.

For the principal-flux field R=sqrt(beta)principal(dtheta), R=X whenever
all |X_p|<pi sqrt(beta). The exceptional probability is

 p_wrap <= 12V exp(-pi^2 beta/2).                       (5.2)

Hence the finite-dimensional limit also transfers to R. For its local
Sobolev tightness, use |R_p|<=|X_p| and Gaussian moment bounds to obtain

 E|<h,X-R>|^k <= C_k (6V)^(k/2)||h||^k sqrt(p_wrap).     (5.3)

At k=2 the right side tends to zero along(5.1), giving uniform test
variance and the same local H^-s tightness. This deliberately does NOT
claim all principal-flux moments from(5.3): at coefficient4 that bound
only proves convergence of total-degree k moments when k+1<2pi^2, in
particular integers k<=18. All score moments do converge. For a prescribed
finite K, replacing4 by any C>max(1,2(K+1)/pi^2) proves principal moments
through degree K by the same argument. A single beta growing faster than
log V, such as ceil(log(2V)^2), makes(5.3) vanish for every fixed k, but
is a different specified family.

The explicit positive-time Gaussian Gram/Wick construction of PR8130
therefore applies to the limiting field, with two transverse linear modes
and energy |p|. No statement about fixed-parameter photon dispersion follows.

## 6. Thin Wilson loops: bounded current potential

Condition(A) alone does not cover every allowed continuum sequence. For a
nondegenerate fixed rectangle, nonzero g and polynomially growing boxes,
for example L of order a^-2, the source h=qS/sqrt(beta) satisfies

 |P_e h|^2=(q^2/beta)<j,G_L*j> >= (q^2/(16beta))|j|^2,

because the nonzero lattice Laplacian eigenvalues are at most16. The loop
has |j|^2 of order a^-1, while sigma is only of order log(1/a), so(A)
eventually fails. On much faster-growing boxes(A) might hold; no universal
failure is claimed. Condition(B) covers the required loops for every
allowed a->0,aL->infinity sequence.

Let G_L be the zero-mode-subtracted scalar inverse Laplacian. The heat
kernel bounds derived in PR8130 extend uniformly to the torus as

 |G_L(n)| <= C/(1+dist_L(n,0)^2)+C/L^2.                 (6.1)

For dist<=L/4, use the infinite-kernel bound plus O(L^-2) comparison already
derived there. For dist>L/4, split the heat integral at L^2: the small-time
image sum has off-diagonal distance of order L and integrates to O(L^-2),
the subtracted zero mode on that interval is L^-2, and the large-time
nonzero Fourier modes integrate to O(L^-2). Thus no divergent sum of Green
images is taken.

For any straight axis segment with at most L distinct edges, summing the
first term in(6.1) along that segment is at most the convergent circle-line
sum sum_{r in Z} C/(1+r^2), with at most a fixed multiplicity. The second
term contributes at most C/L. Therefore

 sup_x sum_{y in segment}|G_L(x-y)| <= C_line,          (6.2)

with C_line independent of L and segment length. This controls the near
self singularity; it does not require two loops to be separated.

For a contractible rectilinear loop j=d_1^*S with at most J straight
segments and integer charge q, h=qS/sqrt(beta) has

 psi=(d_1^*d_1)^+ d_1^*h=(q/sqrt(beta))G_L*j,
 ||psi||_infinity <= C_line J |q|/sqrt(beta).           (6.3)

The scalar Green identity uses divergence-free and harmonic-free j; it is
not valid for arbitrary edge currents. Rounding q to g sqrt(beta) keeps the
right side bounded for each supplied finite g. A fixed finite collection
of such loops also has bounded total source potential. Since sigma->infinity,
condition(B) eventually holds for all individual and joint sources.

The exact integer character W_q(C)=exp(iq<j,theta>)=exp(i<h,X>) and the
surface-independent pairing <P_e S_i,P_e S_j>=<j_i,G_L*j_j> are unchanged.
Using(4.3) before dividing expectations controls their ratios even as the
self expectations vanish. For separated loops with positive physical gap,
the off-diagonal Green limit of PR8130 and ordinary edge Riemann sums give

 E(W_1 W_2)/(E W_1 E W_2)
 -> exp[-g_1 g_2 integral_{C_1}dx_mu integral_{C_2}dy_mu
                     /(4pi^2 |x-y|^2)].               (6.4)

The same subsequent long-time rectangular and return-charge limits give
Coulomb interaction g_1 g_2/(4pi R) for the external charges. Limit order,
integer charge condition and positive separation remain essential. This
constructs neither dynamical charged states nor a native matter law.

## 7. A lower bound on defects and the limit of this method

For a single image label conditioned on theta, write t=dtheta_p/(2pi).
Its mass at k is proportional to exp[-2pi^2 beta(k-t)^2]. A nearest integer
k_0 is a mode. One of its adjacent integers has relative weight at least
q_beta=exp(-2pi^2 beta): choose the neighbor towards t, including either
when t=k_0. Thus every atom has mass at most

 m_beta = 1/(1+q_beta), eta_beta=1-m_beta>0.            (7.1)

Take the V/16 three-cubes of orientation(0,1,2) whose four base coordinates
are all even. Their face supports are disjoint. Choose one special face
in each. Conditional on theta and all other k labels, the special labels
remain independent. Vanishing dk at a selected cube fixes its special
integer to at most one value. Hence

 Pr(dk=0) <= m_beta^(V/16),
 Pr(z in K) <= m_beta^(V/16).                          (7.2)

Moreover the count D of defective selected cubes stochastically dominates
Binomial(V/16,eta_beta), by conditioning the independent Bernoulli indicators
and using their uniformly lower-bounded success probabilities. In particular

 E D >= eta_beta V/16,
 Pr(D<=eta_beta V/32) <= exp(-eta_beta V/128).          (7.3)

The latter is the elementary multiplicative Chernoff estimate with deficit
one half. No unconditional independence of defects is asserted.

For every FIXED beta>0,N>=2 the global exact-sector probability therefore
tends to zero exponentially in V. More generally it tends to zero whenever
V exp(-2pi^2 beta(V))->infinity. If that global probability is bounded
away from zero, (7.2) forces beta(V)>=log V/(2pi^2)-O(1).
This is a necessary scale for GLOBAL defect exclusion, not a necessary
scale for a massless phase or Maxwell infrared limit.

There is a parallel bound for the chosen uniform theta-smallness strategy.
Choose V/16 plaquettes of one orientation with all base coordinates even.
Their edge boundaries are disjoint. For any integer coefficients n_j,
w=P_e sum_j n_j 1_{p_j} is in K^*, and the map from coefficients is
injective because d_1^*w=d_1^*sum_j n_j1_{p_j} has disjoint nonzero
boundaries. Orthogonal projection gives |w|^2<=sum_j n_j^2. Therefore

 sum_{w in K^*} exp(-2pi^2 sigma|w|^2)
 >= theta_1(2pi^2 sigma)^(V/16).                       (7.4)

At fixed sigma this theta sum grows exponentially. Making its nonzero tail
tend to zero requires V exp(-2pi^2 sigma)->0. Thus sigma must also grow
at least logarithmically for this particular uniform small-tail method.
With sigma=N^2/(4pi^2 beta), simultaneous global requirements imply
N at least of logarithmic order. Equation(5.1) supplies a sufficient
logarithmic-order family with deliberately loose constants.

These lower bounds do not refute fixed-law Gaussianity. An infrared
limit can average a positive dilute defect density and acquire a
renormalized stiffness. A local connected-correlation, Ward-identity,
homogenization or multiscale argument would have to replace global defect
exclusion. Which of these applies to the selected finite-clock model
remains open; no exhaustion or independent-wall claim is made.

## 8. Primary-source comparison

Driver's [author-hosted1987 paper](https://mathweb.ucsd.edu/~bdriver/DRIVER/Papers/Drivers_Papers/A1-U%281%29_4-Lattice.pdf),
Commun.Math.Phys.110,479–501, was read in full extracted text (23pages);
page484 was also visually checked because its formula extraction was poor.
Theorems4.2–4.5 concern closed test two-forms, equivalently the current
d*F. Their hypotheses include a continuous U(1) a priori measure and
specified unique or invariant/extreme Gibbs states, or Wilson-like actions
with the further qualifications stated there. They do not supply a
finite-clock full-field theorem. This is a comparison to an established
method, not a claim of novelty for continuum electromagnetism or a theorem
premise here. The present source obtains a different, explicitly varying
finite-clock family using the direct elementary bounds above.


## 9. Finite challenge record and scope

The self-contained executable is
`scripts/finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_2026_09_14.py`.
It reads no repository scientific inputs or helper runner. Numerical theta
and image sums are finite challenges, not certifications of infinite tails.
The analytic tail bounds and continuum implications are in the proof.

| Family | Executed domain and distinct check |
|---|---|
| Cochain quantization | Side-four and side-six tori; cube incidence norms, even-sublattice disjoint supports, angle/integer lift, closed flux and nonclosed harmonic control |
| Image atoms and single-cube law | Four beta values and61 shifts each; four gauge-fixed cube laws compared by integer convolution, root-of-unity filtering and direct clock-angle sums |
| Integer-current theta and source bound | Three independently projected plaquettes, all27 small coefficient combinations, five random source pairings, scalar Poisson duality, and a highest-mode equality witness for the source constant |
| Affine characteristic | Three-face shifted integer lattice at four variances; complex direct sums versus dual Poisson sums, with the relative bound invoked only when its hypotheses hold |
| Thin loop potential | Square loops at inverse meshes2,4,6,8 in finite physical boxes; four-torus FFT current energies and scalar Green envelopes, plus a charge-alias countercontrol |
| Logarithmic sequence | Six values of L from4 through1024; explicit theta/defect/wrap rates and the principal-moment exponent boundary |
| Conditional defect count | Two conditional Bernoulli families and their mixture, with a separate control against inferring unconditional independence |

The finite cube probabilities of no defect are approximately0.28944,
0.45765,0.64649 and0.78213 at the disclosed(N,beta) values. The loop
surface norms increase from2 to8 while their potential supremum norms
range from0.17089 to0.23655; these finite boxes do not execute the
infinite-volume continuum limit. The actual proof of the uniform potential
bound is(6.1)–(6.3). A highest-frequency transverse integer edge current
saturates both the operator norm and the source-exponent inequality, so
its numerical equality checks the otherwise easy-to-miss factor32.

## 10. No-Go Discipline Gate

The negative result is restricted to global lift-defect exclusion and
uniform dual-theta smallness. It is not a fixed-law phase no-go, does not
exhaust microscopic routes, and forces no change to the axioms.

### N1 — Materially distinct attempts

| Honesty | Attempt and mathematical mechanism | Disposition |
|---|---|---|
| ATTEMPTED | Keep beta fixed while suppressing every integer image defect | Conditional atom bounds and disjoint cube faces yield(7.2); finite image and mixture checks challenge the mechanism. |
| ATTEMPTED | Remove only magnetic cubes and silently discard global topology | A closed nonzero integer period survives dk=0. Section2 retains six harmonic tests; the cochain family executes that countercontrol. |
| ATTEMPTED | Use the original dimension-packing estimate to demand volume-order couplings | The injective integer-current map replaces it by a scalar theta product and yields the explicit logarithmic family. |
| ATTEMPTED | Control thin-loop relative errors by a bounded surface norm | The surface norm diverges; section6 instead proves a bounded Green-current potential. The Fourier energy also gives a lower bound on the projected norm. |
| ATTEMPTED | Extend that potential bound to arbitrary clock charges | Charge q=N is identically aliased and violates the source-radius hypothesis in the declared plaquette control. |
| ATTEMPTED | Transfer every principal-flux moment through the rare-wrap event at coefficient4 | The Holder bound has positive volume exponent at degree19. The proof retains all score moments, limits the principal claim, and states how to strengthen the chosen family. |
| ATTEMPTED | Treat conditionally independent image labels as unconditionally independent defects | Section7 integrates uniform conditional domination; the finite mixture has strictly positive unconditional covariance. |

These are different mechanisms, not repetitions counted as independent
science. No row is marked ruled out by prior retained authority.

### N2 — Relations and open dependencies

The global defect and dual theta bounds are both obstacles to this
particular proof strategy; neither is shown equivalent to a physical phase
criterion. Their model parameters satisfy sigma=N^2/(4pi^2 beta), so they
are explicitly coupled rather than counted as independent walls. Native
law selection, the fixed-N=3 Hamiltonian phase and dynamical matter remain
open. No implication between those three physical obligations is established
here, and their independence is unknown. The direct source is a provisional
mathematical dependency, not an independently checked authority.

### N3 — Hidden-condition scan

The model is the supplied isotropic Villain law on equal even four-tori,
L>=4, with all integer image labels retained and ordinary cochain norms.
Source conditions(A) or(B), eta_sigma<1 and the displayed logarithmic
sequence are explicit. The physical limit has a->0 and aL->infinity.
Wilson loops have a fixed finite number of straight segments, contractible
integer currents, fixed finite real strengths rounded to integer charges,
and positive physical separation for their cross pairing. Large-time and
return-charge limits follow the continuum limit. A probability about the
auxiliary positive lift is not identified with a physical phase criterion.
The principal-flux all-moment limitation is explicit. No rate of native
record formation, fixed alphabet, continuum covariance or Wick closure is
quietly added to the axioms.

### N4 — Residual matching

| Source or witness | Exact residual | Matching use |
|---|---|---|
| Direct finite-clock source, sections1–3 | Integer lift, saturation and Hodge geometry | Same torus, clock law and source normalization |
| Direct source, physical-field and Green/OS sections | Limit of the Gaussian comparison and relative loop algebra | Same observables and limit order; its proof remains provisional |
| This source, local cube and scalar theta derivation | Replace volume-dimensional packing | Explicit finite-volume analytic inequalities |
| Closed harmonic flux, aliased plaquette and conditional-mixture controls | Specific missing-hypothesis inferences | Narrow countercontrols, never physical-phase counterexamples |
| Driver1987, closed-test current-sector theorem | Comparison with a fixed-coupling literature route | Context only; no full-field or finite-clock theorem is imported |

### N5 — Resolution and rhetoric

The primary runner reports five substantive resolution lines. Scalar
probabilities and phases are per-element checks; cube geometry is per-site;
Fourier current potentials are per-mode; declared finite tori and mixtures
are per-block. The arbitrary-volume and continuum statements are checked
and not executed: the written estimates bear them, subject to review.
Finite agreement and deliberate-fault detection do not constitute an audit
or prove an infinite-volume claim. The global boundary is never described
as excluding a Coulomb phase or forcing an axiom update.

### N6 — Partial paths

The logarithmic family is a constructive partial path using the same
supplied finite-clock law. A local treatment of positive defect density,
renormalized connected correlations, a continuum current identity with a
verified observable scope, or a multiscale argument could support a
fixed-law phase without globally removing defects. These are open routes,
not discharged lemmas. This note makes no claim that approved primitives
cannot help, introduces no primitive and changes no axiom or registry.

### N7 — Steelman

A hostile reviewer should insist that an exponentially unlikely globally
clean configuration says little about long-distance physics: ordinary
phases contain a positive density of local excitations. That criticism is
correct and defeats any broader negative reading. The construction also
still chooses N and beta as functions of volume and supplies the probability
law and external probe strengths; reducing their growth does not select
those quantities natively. Finally, the source depends on unreviewed
integer/continuum lemmas. The stated result keeps every limitation.

### N8 — Cross-cycle comparison

The direct source's beta proportional to volume was a sufficient choice,
not a lower bound; this note replaces it constructively. The earlier
fixed-parameter covariance route does not require zero defects everywhere
and is not contradicted. Bare finite-penalty defects in the earlier quantum
Hamiltonian are a different model and observable; its density result is
not imported as the witness here. No old wall is recounted as a new
independent obstruction.

## 11. Author review and non-claims

All work in this campaign was performed personally, without subagents.
The author rederived the source-potential bound with a saturating
highest-frequency current, compared the three single-cube representations,
and retained the harmonic and conditional-independence countercontrols.
A first draft's potential implication of all principal-flux moments was
restricted after checking the volume exponent. The shifted complex phase,
integer charge alias and actual source conditions remain explicit.
Independent proof review and the formal audit path are pending.

There is no selected native probability law, fixed-N=3 phase, dynamical
charged matter, non-Abelian sector, empirical coupling prediction, gravity,
Born-rule derivation, completed TOE or forced axiom update in this result.
