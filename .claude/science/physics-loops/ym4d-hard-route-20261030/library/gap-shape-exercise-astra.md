# Repo search

The November 8 lead digest is a search of earlier ultraviolet work. It is
not a search of this November 12 formulation. Its relevant hits were checked:

| Source actually opened | Closeness to this task |
|---|---|
| `prior/repo-search-2026-11-08.md`, especially its source table, item 11 and screening table | Retrieval aid. No order-one twist estimate is reported. Its snapshot duplicates are not independent work. |
| PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–170`, under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` | Codex's earlier local ground-state comparison and positive plaquette witness. Equations (3), (4), (11) retain the exterior normalization. They give finite energy, not decay at order-one coupling. Reused as prior work. |
| main, `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:1–95` | A supplied abelian finite-clock Villain model. Its massless-phase statement is not a Wilson SU(2) theorem or a theorem about every finite group. |
| main, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | A determinant-weighted noncompact Maxwell measure with Dirichlet walls. Its covariance comparison does not compare the two Wilson twist sectors. |

Main was fetched at `bb4ec020d5ada57c630dd89acc98a68397ade423`.
PR 10114 was fetched at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
The task-specific `prior/gap-shape-exercise-astra.md` is absent. Searches
of `open-registry.md` for the target names, mass gap, twist deficit and
Langevin found no owner of this exercise. Row 817's flat and almost-flat
surface problem is explicitly reserved and is not attacked here.
The wider comparison, including the remaining PR heads, is deferred to
Step 5 as the caller requires. No novelty claim precedes that comparison.

# Exercise v2: changing the formulation of the gap problem

Author: Codex, configured by the caller as `gpt-6-astra`, max effort.
Base: `61af70a26b10c193cca1c7a51707545e0461c68a`, 2026-11-12.
Research text, not an audit. This file grants no scientific status.
Unqualified mathematical filenames and `prior/` paths below are in
`library/`. `GOAL.md` and `FINISH.md` are at the lane root. Explicit
repository paths and git refs retain their usual meaning.

## Step 0. Existing wall and reading boundary

**Reading.** The skill is the caller's Exercise revision
`f5af11cd0102cfd0b51aef0911f600130bf5beb1`. Its freshness procedure and
proof-search governance were read at that revision. The current main
workflow redirects to `RULES.md` and `SETTINGS.md`; both were read.
The four framework axioms and the three registered primitives
(`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive`) were read with their source notes.
None specifies the Wilson law or a confinement
estimate. The derivation-obligation registry has no matching YM gap row.
The review boundary was read, not executed. Planning-branch instructions
were read without checking its files into this tree.

The caller's source restriction narrows the skill's literature search to
the repository and the permitted primary texts. The permitted paper
directory `/Users/jonBridger/ym4d-papers` is absent on this machine.
No other home directory or shared temporary directory was searched.
The outline and CA-I were each downloaded once, into
`/tmp/sa-gap-shape-exercise-astra.kQaQHL/`. The skill was downloaded into
the separately created `/tmp/sa-gap-shape-exercise-skill.nfzW2t/`.
There is no numerical proof, numerical test, or imported computed constant.

**Reading, with credit.** Ethan Sussman and Levent Alpoge, with Claude
and Codex as authors of their text, supply the outline and complete account
at `31a47c543775`. The outline index README, relevant chunk rows and their
neighbours, and obligations were consulted first. Chunk 01:59–74 and
chunk 29:68–80 lead to SA:565–602 and 31858–31884. The latter explicitly
leaves exclusion of a spectral interval separate from scalar reconstruction.
Its example of polynomial decay without a gap is already proved there;
it is not rederived. The CA 4.12–4.19 index concerns background and
operator admission, not an order-one twist estimate. Searching that index
for the present objects gives no match. The full CA index's mass-gap hit
is CA-III `10.7:prop-clustering-mass-gap`, a different volume not downloaded
or used as a proof here. These are bounded readings, not a claim to have
checked every statement in the account.

**Reading of the supplied current record.** `gap-skeleton-final.md`
sections 0–3 and 13.15–13.20, `gap-ext-astra.md` section 1,
`gap-expose-astra.md` sections 1 and 7, `gap-tree-astra.md` sections 1 and 4,
`gap-joint-astra.md` sections 1 and 3, and `gap-gamma2-astra.md` sections
1, 2 and 5.3 were read. Their exact definitions control this exercise.
Earlier exercise packets, other gap files, literature digests and FINISH
rows 743–817 remain closed until Step 5.

What is already available is not a new target: the common-denominator
identity (J4), the sufficient bound (E17), the stronger absolute bound
(J12), and the equivalence of (G2) to a uniform auxiliary diffusion gap.
The caller reports the new checks of rows 815–816 and the range beta<2/9.
That report is the dispatch's current status, not this author's check.
The same applies to the listed transport, selector, filter and averaging
obstructions. None is rerun merely to reproduce a failure.

## Step 1. The wall twice

**Reading — plain statement.** We want to show that this particular
four-dimensional gauge theory forgets a disturbance over a fixed physical
distance. The current proof asks whether inserting a global sign change
has very little effect on its partition function. Exact identities express
that effect in several ways, but they do not bound it at the required
couplings. Bounds at much smaller coupling are available. The task is to
find and test a different mathematical mechanism, or to show precisely why
a proposed change of formulation fails. Changing the theory, the boundary,
or the observable helps only if the result can be brought back to the
original theory with its normalization and limits controlled.

**Reading — exact contract.** On the periodic lattice
`n=(a,a,c,d)`, `a>=3`, `c,d in {a,2a}`, put

\[
 Z_m(\beta)=\int\exp\{\beta\sum_p\eta_{m,p}\operatorname{tr}(U_p)/2\}\,dU,
 \qquad p_{m,i}(a,\beta)=\frac{1-Z_{m+v_{1i}}/Z_m}{2}.
\]

Haar measure has mass one. The omitted common Wilson constant cancels.
The immediate target is, uniformly on a specified compact interval
`I=[beta_-,beta_+]` in `(0,infinity)`,

\[
 \max_{m_2=0,\ i=3,4}p_{m,i}(a,\beta)
 \le C a^p\eta_*^{a/2},\qquad 0<\eta_*<1.                 \tag{T}
\]

Here eta_* is the existing witness constant; it is not adjusted to fit
an argument. (T) is the already sufficient (E17), not a necessary
characterization of every possible mass-gap proof. The exact weakest
consumer remains (FQ), involving the actual even thermal sum.

Allowed: finite-dimensional integration, representation theory, spectral
theory and fully written arguments with their hypotheses. Forbidden:
replacing the Wilson denominator, assuming a different action is equivalent,
dropping an unbounded limit cost, treating a computation as discharge, or
turning a conditional implication into a closure. Required tests retain
the U(1) Coulomb phase and the weak-coupling binary icosahedral model.
A change of ultimate target must also explain whether those remain negative
controls for that target. The continuum scalar-sector gap additionally needs
the lane's cutoff-uniform bridges; a fixed-spacing result alone is insufficient.

| What the framework supplies | What this problem supplies | What the existing arguments supply |
|---|---|---|
| Lattice, Qubit, Admissibility, Record | SU(2) link variables, four-dimensional Wilson probability, beta, periodic boxes, twist sectors and chosen observable algebra | Exact transfer and surface identities; conditional infrared consumers; strong-coupling estimates in their stated ranges |
| Units reference; kinetic-form isotropy; pointwise realized-state slot | A specific action, measure, boundary condition and limiting sequence | No dimensionless gap follows from any of those three primitives |

**Reading — blind check.** A separate-context Codex gpt-6-astra/max reader
restated the wall before opening scientific sources: exact rewritings do
not control the global-sign response in the required interval; a passing
mechanism must return to the original theory with normalization, boundaries
and limits controlled. This matches the contract. It is a comprehension
check, not an independent scientific verification.

## Step 2. Assumptions that bear the load

**Reading.** The following ledger takes its premises from the definitions
just read. A name in the last column is a proposed hand test, not a result.
Step 4 explicitly varies every row, including the definition choices.

| ID; kind | Premise and source | If changed or false; decision cost | Existing test / first test |
|---|---|---|---|
| A1; axioms | Four framework axioms; main axiom memo | They do not fix this model; changing them supplies no estimate of (T) | Not load-bearing for the model theorem |
| A2; primitives | The three registry nodes named above | Units, kinetic form and a state slot cannot supply a gap or a Gibbs law | Not load-bearing for (T); keep their scope |
| A3; supplied model | Exact Wilson plaquette weight; `gap-ext-astra.md:83–91` | Changing it loses the current transfer/character constants and identification | Compare normalized measures, not bare actions |
| A4; supplied group | SU(2); `gap-expose-astra.md:92–106` | Extension/deformation needs a return theorem | Haar tensors through degree eleven already match the finite control |
| A5; geometry | Four dimensions and the given periodic aspect ratios; `gap-ext-astra.md:80–82` | Open walls remove the twist class; other aspect ratios lose the crossing consumer | Compute the boundary observable after cutting |
| A6; observable choice | Twist deficit as immediate target; `gap-expose-astra.md:577–599` | A direct scalar-sector argument could bypass it but cannot claim (T) | Identify precisely which spectral sector is observed |
| A7; coupling choice | One beta, uniform on I; `gap-joint-astra.md:88–91` | A path in coupling or action needs a volume-uniform comparison | Test the derivative of a gap or sector ratio |
| A8; normalization | Original Z_m in numerator comparisons; `gap-joint-astra.md:130–157` | A scalar vacuum error can erase the putative gain | Preserve the denominator through every marginal |
| A9; uniformity | C,p independent of a,beta,shape,pair; same source | A fixed-volume positive gap says nothing uniform | Examine growth of every comparison constant |
| A10; sufficient rate | The fixed eta_* in (E17); `gap-expose-astra.md:585–599` | Arbitrarily slow exponential decay need not verify this sufficient test | Return to (FQ) if the witness is too costly |
| A11; representation | Signed joint activities and a fixed ordering; `gap-joint-astra.md:111–157` | Positivity of physical endpoints does not make intermediate activities positive | Keep cancellations before an absolute estimate |
| A12; method | Rooted absolute sum (J12); `gap-joint-astra.md:346–365` | It is stronger than the signed target | A signed-sum route pays a different obligation |
| A13; method | All gauge-invariant diffusion tests; `gap-gamma2-astra.md:113–161` | A smaller observed subspace may avoid irrelevant slow modes | Check invariance of the smaller subspace under the generator |
| A14; metric | Product unit S^3, Ricci=2; `gap-gamma2-astra.md:75–111` | A new generator needs its own locality and Dirichlet-form comparison | Derive the new form rather than transfer the number 2 |
| A15; Euclidean method | Reflection/transfer route; `gap-skeleton-final.md:25–36` | Hamiltonian or real-time proof needs an identification with this transfer limit | Test anisotropic discretization before continuum claims |
| A16; controls | U(1) and binary icosahedral weak coupling; caller | They constrain a confinement proof; changing the claimed observable may change the test | Name the actual failed hypothesis, not just the group name |
| A17; limiting target | Scalar tr(F^2) cyclic sector; `gap-skeleton-final.md:27–36` | Full observable gap is stronger; continuum passage is separate | Keep common physical rate and order of limits |
| A18; hidden methods | Local estimates, fixed block sizes, worst exterior, absolute norms, finite spin truncation | None is part of (T)'s definition; each can discard the joint effect | Test an exact marginal or a relative form before imposing locality |
| A19; analytic setting | Finite compact link products, smooth real tests and positive beta; `gap-gamma2-astra.md:75–161` | Noncompact or complex measures need new domains, integration by parts and positivity | Check poles, tails and boundary terms in the first lemma |
| A20; exact symmetry | Gauge invariance, central cocycles, reflection positivity and positive transfer; `gap-expose-astra.md:92–157` | Dropping any one loses its associated quotient, sector identity or spectral argument | Check symmetry of any enlarged law or altered generator |
| A21; locality | Four-link plaquettes, six occurrences per link, periods at least three; `gap-gamma2-astra.md:165–191` and task geometry | Interactions or repeated links change all degree and Hessian constants | Count incidences symbolically; do not carry constants across models |
| A22; physical state | Periodic volume-first limits and a canonical scalar component; `gap-skeleton-final.md:27–36` | A selected boundary state or another component needs a comparison; a gap above a larger kernel is a different statement | Keep vacuum uniqueness separate from positive excitation energy |
| A23; upstream inputs | The existing infrared consumer and ultraviolet/continuum construction, on their own domains | A finite-lattice proof would not close missing existence or cutoff matching inputs | State the exact consumer reached, even after a successful estimate |
| A24; evidence rule | Written Lean-formalizable arguments, no computational discharge; caller and GOAL | Relaxing this would change the task, not solve it under its contract | No relaxation is made |

## Step 3. First-principles reduction

**Reading.** The physical goal concerns the scalar cyclic sector.
The current sufficient route concerns a topological partition ratio.
The curvature route concerns every invariant function of every link.
Those are three different statements. Existing results link some of them
conditionally; a definition does not identify them.

Delete an area-law requirement from this exercise: (T) only needs its
stated linear exponent. Delete any presumption that (J12), a single-link
estimate, or a fixed spin cutoff must be used. Keep the Wilson normalization
and the ultimate physical limit unless an explicit bridge replaces them.

The smallest useful object for a deformation route is its exact marginal
law, with the auxiliary variables integrated out. For a boundary route it
is the missing seam kernel. For a diffusion route it is a test function
that distinguishes a local estimate from a volume-uniform one. These are
proof tests. No finite-volume numerical test will stand in for a uniform proof.

There are two separate costs: obtaining decay in a tractable description,
and transporting that decay to Wilson SU(2) with a uniform rate. Merely
moving the second cost into a new scalar inequality is not progress.
The route round below must attempt its first statement as an actual proof.

## Step 4. Change each assumption; attempt distinct mechanisms

**Suggested changes, with their price.** Each A-row is varied below.
These are alternatives to test, not new premises adopted for Wilson SU(2).

| Premise dropped or changed | What follows if we change it | Cost in the lane's proved results |
|---|---|---|
| A1–A2: framework baseline | Treat this as a theorem about a supplied probability law | No loss to the model calculation; no claim of native derivation becomes available |
| A3: Wilson action | Use heat-kernel, admissible, Higgs, or auxiliary-field weights | Transfer positivity alone survives only where separately shown; Wilson coefficients and the physical identification need replacement or comparison |
| A4: exactly SU(2) | Use a larger compact group, continuous auxiliary fields, or a deformation reducing to SU(2) | Exact marginalization is preferable to an unproved universality claim; a spectral estimate must survive projection/removal |
| A5: periodic tori | Cut to boxes or cylinders | A noncontractible twist can disappear; the missing seam is now an operator or a boundary-to-boundary correlation. Periodic gluing and the crossing theorem need that seam back |
| A5: four dimensions / these aspect ratios | Start on a plane, slab, or anisotropic lattice | An exactly solved lower-dimensional endpoint does not control the restoration of transverse couplings or the infinite-width limit |
| A6: twist deficit must be the observable | Estimate the scalar transfer spectral measure directly | Can bypass flux bookkeeping; loses the present finite-size sufficiency theorem and may require all times and all scalar polynomial vectors |
| A7: comparison at one coupling | Follow a path from a solved law | Requires a uniform stability radius or integrated comparison. Finite-volume analyticity supplies neither |
| A7: one common beta for all plaquettes | Use anisotropy or separate spatial and temporal couplings | A tractable endpoint must connect to the isotropic law without a vanishing gap; isotropic permutations used by the seed are lost along the path |
| A8: the original normalization | Integrate auxiliaries exactly or divide by a convenient vacuum | Exact marginalization retains it; division by an unrelated vacuum incurs the full relative partition-function cost |
| A9: uniformity in size | Work at one finite volume | Compactness gives a positive number but not its large-volume lower bound; no order-one closure follows |
| A10: predetermined witness rate | Use (FQ) with the actual even thermal sum | Avoids a potentially wasteful sufficient rate; requires estimating both quantities jointly |
| A11: fixed surface ordering | Sum signed classes or choose an ordering adapted to the law | May preserve (J4), but absolute activity bounds change. Positivity at the two endpoints is not positivity along this interpolation |
| A12: rooted absolute control | Estimate the signed whole sum | Removes a stronger condition; needs a quantitative cancellation mechanism. The task does not require positive individual surfaces |
| A13: all invariant diffusion observables | Use the dynamically closed subspace generated by local scalar observables | Must prove that closure and its locality bridge. A finite list of initial observables is not an invariant subspace |
| A14: the standard link diffusion | Use heat bath, blocks, lifted variables or another metric | The new Dirichlet form and finite-speed estimate must be compared. A fast sampler is not automatically a physical gap |
| A15: Euclidean proof | Use a Hamiltonian estimate, real-time propagation or a ground-state representation | Must construct the matching Hamiltonian/state and preserve the isotropic continuum limit; no such identification is supplied by a notation change |
| A16: both controls are negative controls for every conclusion | Separate confinement from a local scalar gap | U(1)'s massless scalar channel remains decisive. A gapped finite-group neutral sector can pass a scalar-gap test while failing a confinement test. This does not meet the caller's confinement contract without a further distinction |
| A17: scalar cyclic sector / chosen limits | Demand a full observable gap, or change the order of limits | The first is stronger; the second needs new existence and identification results. Neither follows from the current scalar reconstruction |
| A18: local, worst-exterior, absolute proof architecture | Retain joint gradients, integrate a whole block, or use an exact enlargement | Can escape the listed scoped obstructions. It must actually bound the resulting joint object, not introduce another name for (T) |
| A19: compactness, smoothness or positive real weights | Use a singular gauge slice, complex contour or noncompact carrier | The elliptic spectral and integration-by-parts steps require replacement. Pole and tail terms cannot be suppressed by notation |
| A20: gauge, center or reflection symmetry | Work on an unconstrained carrier or an action lacking one symmetry | The associated physical quotient, conserved-flux identity or positive transfer is lost; recover it explicitly before using the old conclusion |
| A21: local incidence structure | Change the graph, range, or number of links in a plaquette | The constants and exact local identities must be recalculated. A high-degree comparison cannot inherit the degree-eight bound below |
| A22: chosen state and unique scalar vacuum | Prove a gap above several vacua or in an open-wall state | Does not give the stated component theorem until state selection and the order of limits are controlled |
| A23: existing ultraviolet/infrared bridges | Build a separate constructive route | Potentially useful, but all missing identification and continuum obligations return; no conditional existence input is silently closed |
| A24: proof-only evidence | Permit a numerical certificate | Outside the caller's contract. This premise is fixed; only written tests count here |

**Reading — route separation.** Three fresh, restricted-context
gpt-6-astra/max agents received materially different briefs: scalar/boundary
reframing; an exact enlarged law; and a gauge-invariant differential
estimate. Their initial briefs contained none of the other routes'
conclusions. Results were shared after the distinct cores had formed;
Route C then used the primary author's Route D one-link sphere estimate.
Same model/provider and shared task provenance mean this
is search diversity, not independent verification. All readers were told
to keep the closed comparison sources closed and to leave row 817 alone.

### Route D: retain the exact one-link concentration

**Suggested mechanism.** A large external field improves relaxation on
SU(2), even though its pointwise weighted curvature becomes negative near
the opposite pole. A sharp conditional estimate could supply more reserve
for a genuinely joint argument. It does not by itself tensorize an
interacting measure.

**Pre-registration D1, before the proof attempt.** For every vector
`h in R^4`, on the unit sphere S^3 with probability proportional to
`exp(h dot q)`, attempt the Poincare bound

\[
 3\operatorname{Var}_h(f)\le\int|\nabla f|^2\,d\nu_h.       \tag{D1}
\]

Pass: a written proof uniform in h, including all angular and radial
modes, with the unit-sphere normalization. Fail: a counterexample or an
unclosed radial/angular sector. Scientific usefulness is a second test:
does it enlarge the coupling interval of the existing joint argument,
or only its prefactor? No numerical eigenvalue computation can decide D1.
The outline index has no tilted-sphere or Langevin match; its one-bond
convolution at SA:2195–2235, located through chunk 02:83–99, is a different
operator. Its Bessel coefficients are already theirs and are not rederived.

**Proved by the author, not independently checked — Lemma D1.** The
pre-registered inequality holds. Its constant 3 is sharp uniformly in h.

Rotate h to `(h,0,0,0)`, with `h>=0`. Put `x=q_0`,
`r=(1-x^2)^(1/2)`. The metric and volume in these coordinates are
`dx^2/r^2+r^2 dOmega_2^2` and a constant times `r dx dOmega_2`.
The positive weighted Laplacian is therefore

\[
 L_h=-r^2\partial_x^2+(3x-hr^2)\partial_x-r^{-2}\Delta_{S^2}.
                                                               \tag{D2}
\]

Decompose into spherical harmonics on S^2. Degree l has eigenvalue
`l(l+1)` for `-Delta_(S^2)`. For completeness, these spaces are the
restrictions of homogeneous harmonic polynomials of degree l in three
variables. The polar-coordinate Laplacian gives that eigenvalue.
Decomposition of polynomials into harmonic terms, followed by density
of restricted polynomials on the sphere, gives completeness. Thus no
angular mode is omitted.

In degree l write `f=r^l u(x)Y_l(omega)`. Its squared radial norm uses
`w_l(x)dx=exp(hx)r^(2l+1)dx`. Direct differentiation of (D2) gives

\[
 A_lu=-r^2u''+((2l+3)x-hr^2)u'
                   +\{l(l+2)+lhx\}u.                         \tag{D3}
\]

For any positive smooth phi on the closed interval `[-1,1]`,
integration by parts gives the exact identity

\[
 \langle u,A_lu\rangle_{w_l}
 =\int r^2\phi^2|(u/\phi)'|^2w_l\,dx
       +\int (A_l\phi/\phi)|u|^2w_l\,dx.                    \tag{D4}
\]

The boundary term vanishes: `r^2 w_l=exp(hx)r^(2l+3)` tends to zero
at both ends. Smooth spherical eigenfunctions have regular u there.
This regularity can also be read from their Taylor expansion in the
transverse coordinates at either pole: the degree-l harmonic factor is
`r^l Y_l`, and the remaining invariant coefficients are smooth in r^2.
One may first apply (D4) to such eigenfunctions and then use the spectral
expansion; no singular trial function at a pole is admitted.

For `l>=1`, take `phi=exp(-alpha hx)`, `alpha=l/(2l+3)`.
Substitution into (D3) gives

\[
 A_l\phi/\phi=l(l+2)+\alpha(1-\alpha)h^2r^2\ge l(l+2)\ge3.
                                                               \tag{D5}
\]

The linear term cancels because `l-alpha(2l+3)=0`. Equation (D4)
therefore bounds every eigenvalue in an angular sector by 3 from below.

It remains to handle the nonconstant radial sector `l=0`. Let
`A_0u=lambda u`, `lambda>0`, and put `v=u'`, which is nonzero.
Differentiating this equation yields

\[
 -r^2v''+(5x-hr^2)v'+(3+2hx)v=\lambda v.              \tag{D6}
\]

This operator is symmetric with weight `exp(hx)r^3 dx`. Apply the
same identity (D4) to it with `phi=exp(-2hx/5)`. Its value on phi,
divided by phi, is `3+(6/25)h^2r^2`. Thus `lambda>=3`.
The finite sphere has a smooth positive density and compact elliptic
resolvent. Constants form its kernel, by integration of `|grad f|^2`.
The complete eigenfunction expansion now proves (D1) for smooth f,
and closure gives the form-domain version. At h=0 a coordinate function
has eigenvalue 3, proving sharpness. This is a written argument, not a
computed spectrum.

**Proved implication, with its limitation.** On a Wilson lattice with
no repeated link in a plaquette, the conditional law of one quaternion
q_e is exactly `exp(H_e dot q_e)` times Haar. All other variables are
fixed in H_e. Center signs change H_e but not the argument. Consequently

\[
 \sum_e\mu[\operatorname{Var}_e f]
                 \le\tfrac13\mu\sum_e|\nabla_e f|^2.          \tag{D7}
\]

If the full heat-bath generator has invariant gap g, its variational
inequality and (D7) give Langevin gap at least `3g`. No heat-bath gap
has been established by (D7). All one-coordinate conditional laws can
be well behaved while the joint law has a slow mode. D1 is a useful
local reserve only if a joint mechanism uses it. Whether it improves
the already known beta interval must await Step 5's exact comparison.

### Route A: a scalar spectral certificate in place of twists

**Suggested route; first cheap certificate fails.** The separate reader
proposed the normalized physical transfer restricted to the scalar cyclic
sector. A finite matrix of scalar time moments would be cheaper than a
twist estimate. The following exact construction tests that proposal.

**Proved by the route author, self-checked here — finite-moment lemma.**
Fix K, distinct `0<x_i<q_0<1`, `0<=i<=K`, and positive weights w_i
summing to one. Let `nu_0=sum w_i delta_(x_i)`. Take an increasing
sequence `q_0<y_j<1` tending to one and `rho=sum_(j>=1)2^(-j)delta_(y_j)`.
Let l_i be the degree-K Lagrange polynomial with `l_i(x_j)=delta_ij`,
and put `alpha_i=int l_i d rho`. Choose epsilon>0 so small that
`epsilon max(alpha_i,0)<w_i` for every i. Then

\[
 \nu_1=\sum_i(w_i-\epsilon\alpha_i)\delta_{x_i}+\epsilon\rho
                                                               \tag{A1}
\]

is positive. Polynomial interpolation gives
`x^k=sum_i x_i^k l_i(x)` for `0<=k<=K`, so nu_0 and nu_1 have the
same first K moments, including total mass. But nu_1 has support
accumulating at one and no atom there.

Realize the positive transfer as `1` on `C Omega` and multiplication
by x on `L^2(nu_1)`. Let f=1 in the second summand and
`A=|f><Omega|+|Omega><f|`. The only eigenvector at transfer value one
is Omega, while `H=-log T` has spectrum approaching zero in the scalar
cyclic sector. Polynomials in x are dense there: continuous functions
are dense for a finite Borel measure on [0,1], and polynomials uniformly
approximate those functions. The missing tail is therefore observable.
The nu_0 realization has a gap at least `-log q_0` and the same first K
correlations. Truncating and renormalizing rho before this construction
gives finite-dimensional transfers with gaps tending to zero and the same
prescribed moments. Thus finite-volume trace class does not repair it.

In particular K at least `2N+1` fixes both matrices
`G_ij=c(i+j)` and `M_ij=c(i+j+1)`, `0<=i,j<=N`.
A compression inequality `M<=qG` valid in the gapped example is valid
in the tail examples too. The counterexample is about positive transfers
and finite scalar moments. It is not a Wilson measure, a local gauge
model, or a counterexample to a proposed Wilson-specific tail theorem.
The missing theorem must control all degrees or exclude these tails by
additional local dynamics. Full contraction on a dense cyclic core is
equivalent to the scalar gap, and remains unproved. Its relation to (T)
is not established. The finite-group control cannot be discarded while
still claiming the original confinement target.

### Route B: an exact Gaussian enlargement

**Proved by the route author, self-checked here — exact marginal.** For
`p=(x,mu,nu)`, `mu<nu`, set
`A_p=U_(x,mu)U_(x+mu,nu)` and
`B_p=U_(x,nu)U_(x+nu,mu)`. These are unit quaternions and
`q_p=<A_p,B_p>`. Let independent Q_p have standard Gaussian law in R^4,
and set `T_p(U)=sqrt(beta)(A_p+eta_(m,p)B_p)`. Since
`|T_p|^2/2=beta(1+eta_(m,p)q_p)`, the Gaussian integral gives exactly

\[
 e^{-\beta|P|}\int\exp\{\sum_p Q_p\cdot T_p(U)\}\,d\gamma(Q)
             =\exp\{\beta\sum_p\eta_{m,p}q_p(U)\}.            \tag{B1}
\]

Normalize this joint density by the original Z_m. No replacement
partition function has entered. The conditional law is
`Q|U=N(T(U),I)`; equivalently `R=Q-T(U)` is an independent Gaussian.
The gauge action on Q_p is left multiplication at x and right inverse
multiplication at `x+mu+nu`. It preserves its Euclidean metric and
makes T equivariant.

**Proved implication — the enlargement does not remove the spectral
obligation.** Product unit-sphere/Euclidean metrics give
`||DT||^2<=24 beta`: each plaquette derivative is bounded by
`sqrt(beta)sum_(e in p)|v_e|`, then square and count six faces per link.
For an invariant smooth F set `g(U)=E_R F(U,R+T(U))`.
Gaussian conditional variance, followed by a Wilson invariant Poincare
inequality of constant lambda_W, gives

\[
 \operatorname{Var}_\nu F
 \le E_\nu|\partial_Q F|^2+
 \lambda_W^{-1}E_\nu|\partial_UF+DT^*\partial_QF|^2
 \le\left(1+\frac{1+24\beta}{\lambda_W}\right)E_\nu|\nabla F|^2.
                                                               \tag{B2}
\]

Taking F=f(U) for the reverse direction proves

\[
 \frac{\lambda_W}{\lambda_W+1+24\beta}
           \le\lambda_{\rm ext}\le\lambda_W.                 \tag{B3}
\]

Hence a uniform invariant gap for this enlargement is equivalent to the
Wilson gap on a compact beta interval. The independent Gaussian remainder
does not make the joint U-law independent. This equivalence is not a gap
estimate and does not provide the order-one supplier.

**Proved scoped failure — full-space pointwise curvature.** In the
untwisted law take all U=I and `Q_p=-t I` on the six faces of one link.
Vary just that link along `U_e(s)=cos s+n sin s`, with |n|=1.
Each affected T_p has second derivative `-sqrt(beta) I`.
The joint potential relative to Euclidean volume in Q is
`V=|Q|^2/2-sum Q_p dot T_p`. Thus in this unit direction

\[
 (\operatorname{Ric}+\operatorname{Hess}V)(v,v)
                       =2-6t\sqrt\beta\longrightarrow-\infty. \tag{B4}
\]

This defeats the attempted positive-curvature proof on the full enlarged
manifold at every beta>0. It does not defeat curvature restricted to
invariant gradients, nor an integrated estimate; the displayed tangent
was not asserted to be such a gradient. Replacing the failed pointwise
criterion by the existence of lambda_ext merely returns to (B3).

### Route C: propagate the gauge constraint through neighbouring vertices

**Proved by the route author, pending the separate check — reserve lemma.**
Use a simple D-regular graph and unit S^3 link metrics. For an invariant
smooth f put `g_e=grad_e f`, and let H_ej be its Hessian block from the
j-link tangent space to the e-link tangent space. Define pointwise

\[
 e_f=\sum_e|g_e|^2,\quad
 A_f=\sum_{e\ne j:\ e\sim j}\|H_{ej}\|_{\rm HS}^2,\quad
 N_f=\sum_{e\ne j:\ e\not\sim j}\|H_{ej}\|_{\rm HS}^2.       \tag{C1}
\]

Here `e~j` means they share a vertex. Sums are ordered, and the diagonal
is excluded from both. For each incident pair (v,e), the infinitesimal
gauge action is the isometry `J_ve a=aU_e` at a source and `-U_e a` at
a target. Set `g_ve=J_ve^*g_e`. Gauge invariance gives
`sum_(e incident v)g_ve=0`.

Identify imaginary quaternions with R^3, so `[a,b]=2a cross b`.
The unit-round connection obeys
`nabla_(J_ve b)(J_ve a)=J_ve(a cross b)` at either endpoint.
At the source these are right-invariant fields; at the target both
minus signs accompany the left-invariant connection. Differentiating
`df(K_v^a)=0` in direction `J_ve b` therefore gives, with
`B_ej=J_ve^*H_ej J_vj`,

\[
 \sum_{j\ni v}B_{ej}=-[g_{ve}]_\times.
\]

The diagonal B_ee is symmetric. The skew parts K_ej of the off-diagonal
blocks satisfy `K_je=-K_ej`, row sums `C_e=-[g_ve]_times`, and
`sum_e C_e=0`. The complete graph on the D incident links has the exact
Hilbert-space identity

\[
 \sum_{e\ne j}\|K_{ej}\|^2
 =\frac2D\sum_e\|C_e\|^2+
   \sum_{e\ne j}\|K_{ej}-(C_e-C_j)/D\|^2.                  \tag{C2}
\]

To verify it, the residual has zero row sums and hence is orthogonal
to `(C_e-C_j)/D`; the squared norm of that array is
`(2/D)sum ||C_e||^2`. Since `||[g]_times||HS^2=2|g|^2`, summing over
vertices counts each adjacent ordered pair once and each link twice.
Thus `A_f >= (8/D)e_f`. In four dimensions D=8 and `A_f>=e_f`.

Now require every torus period to be at least four. Fix the link
`e=(x,y)`, take `x=0,y=e_1`, and let W be the neighbours of x or y
other than x,y. They are the fourteen vertices
`-e_1,2e_1,+/-e_nu,e_1+/-e_nu`, `nu=2,3,4`.
Each z in W has exactly one link j(z) to {x,y}. The induced graph on
W is a matching: it pairs `+/-e_nu` with `e_1+/-e_nu`, with the
additional axial pair `-e_1,2e_1` precisely when the first period is
four. Coordinate differences show there are no other edges; a
transverse period four gives a difference of two, not one, between
its opposite neighbours.

At z, differentiate the gauge identity in an e-link direction.
The gauge vector at z has no e-coordinate, so its derivative is zero:

\[
 H_{e,j(z)}J_{z,j(z)}
       =-\sum_{k\ni z,\ k\ne j(z)}H_{ek}J_{zk}.             \tag{C3}
\]

Every k on the right is nonadjacent to e. Regard that right side as
an incidence operator B acting on the array `(H_ek)`. Its product
`BB^*` has diagonal `7I`. An off-diagonal block exists only for a
matching edge inside W, and is an isometry. A two-vertex block of
this form has norm at most 8: its cross term is bounded by the sum
of the two squared norms. Isolated blocks have norm 7. Thus

\[
 \sum_{j\sim e}\|H_{ej}\|^2
       \le8\sum_{k\not\sim e,\ k\ne e}\|H_{ek}\|^2,
 \qquad A_f\le8N_f,
 \qquad h_m(f)=A_f+N_f\ge\tfrac98 e_f.                     \tag{C4}
\]

No averaging, gauge slice, field smallness or orbit regularity is used.
These are smooth identities on the full product manifold. Triangles
at period three are why (C3)'s counting is not asserted there.

**Proved by the combined written argument, pending check and comparison —
candidate diffusion estimate.** Let L_e be the conditional one-link
Langevin operator. D1 and its conditional spectral expansion give
`sum_e mu[(L_e f)^2]>=3 E(f)`. Subtracting the diagonal Bochner identities
from the full identity in `gap-gamma2-astra.md:103–111` gives exactly

\[
 Q(f)=\sum_e\mu[(L_e f)^2]+H_m(f)+C_m(f).                  \tag{C5}
\]

A mixed derivative of one Wilson plaquette has operator norm at most
beta. Its twelve ordered mixed terms are bounded below by
`-beta sum_(e!=j in p)|g_e||g_j| >= -3 beta sum_(e in p)|g_e|^2`.
Six plaquettes per link give `C_m>=-18 beta E`. Combining with (C4),

\[
 Q(f)\ge(33/8-18\beta)E(f),\qquad
 \gamma_{\rm inv}(\beta,\Lambda)\ge33/8-18\beta
                 \quad(0\le\beta<11/48).                    \tag{C6}
\]

For the spectral implication apply (C6) to invariant eigenfunctions:
`Q=lambda E`. Ellipticity on the connected compact manifold, commuting
gauge projection, and integration by parts give the discrete invariant
spectrum with constants as its kernel. Expansion then gives the
Poincare inequality for every invariant test. Fixed center signs do not
affect any estimate.

The task also has a=3, with four possibilities for c,d. These have at
most 1944 plaquettes. Their log-density oscillation is at most
`3888 beta`. Product Haar has gap 3, by tensorizing the h=0 case of D1.
If a probability density relative to Haar lies between m and M,
`Var_mu f <= M Var_Haar f <= (M/3)E_Haar(f) <= (M/(3m))E_mu(f)`.
This proves a gap at least `3 exp(-3888 beta)` for these finite exceptions.
On every compact `I subset (0,11/48)` the entire task family therefore has

\[
 \gamma_{\rm inv}\ge
 \min\{33/8-18\beta_+,\ 3e^{-3888\beta_+}\}>0.              \tag{C7}
\]

The endpoint increases by `11/48-2/9=1/144`. For example, on
`I=[2/9,9/40]` the first number is `3/40`. These are rational hand
calculations, not numerical certificates. Arbitrary tori with a thin
period two or three and unbounded remaining periods are not covered by
the finite-exception argument. No statement about those families is made.

**Reading — controls and remaining price.** The nonabelian bracket
supplies the nonzero row sums in (C2). For U(1) that source is zero;
(C2) gives no positive gradient reserve. The Haar unit-circle gap is
also 1, not 3. On the binary icosahedral group there is no link tangent
space or infinitesimal gauge action of this kind. The proposed extension
therefore stops at named steps in both controls. It does not infer anything
about their weak-coupling phases from a small-beta bound.

At beta=1/2 the right side of (C6) is negative. The remaining order-one
problem is a quantitative joint control of C_m or a different mechanism.
(C7) is an auxiliary diffusion result. It does not itself prove (T), its
fixed eta_* rate, or a cutoff-uniform physical mass gap.

## Step 5. Compare with the opened record

**Reading — search receipt.** The comparison opened 128 `gap-*.md` and
`prior/gap-lit-*.md` files for search, including both earlier crux exercises,
and searched FINISH rows 743–817. It then searched tracked Markdown and
TeX on HEAD, main and all five PR refs below. Searches used the objects
and mechanisms, not just our labels: tilted sphere/von Mises, Langevin,
mixed Hessian, differentiated gauge invariance, adjacent/nonadjacent Hessian
blocks, skew reserve, Gaussian auxiliary/enlargement, Hubbard–Stratonovich,
Krylov, finite/truncated moments, moment matching, Lagrange interpolation,
and the exact proposed constants. Bounded relevant source ranges were
opened; false-positive arithmetic and unrelated model hits were not
treated as proof suppliers. This is a search record, not an absence theorem.

| Ref | Commit at comparison |
|---|---|
| main | `bb4ec020d5ada57c630dd89acc98a68397ade423` |
| PR 10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| PR 10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| PR 10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| PR 10141 | `fb99b4dddc7254e6124ac124887d58eeb3a77802` |
| PR 10144 | `1f20846b8057f6346ebab6c0dbebdabbd9e472a4` |

Full retrieval logs are in `/tmp/sa-gap-shape-exercise-astra.kQaQHL/`:
`step5-lane-matches.txt`, `*-step5.txt`, and `*-mechanisms.txt`.
The first six-ref pass found 307, 329, 329, 307, 310 and 307 matching
lines respectively. The broader mechanism pass found 309 on HEAD and
253, 347, 347, 256, 256 and 253 on those refs. These are retrieval counts,
not mathematical evidence. Searches of the downloaded SA and CA-I for
the precise diffusion/augmentation objects gave no match. No extra copy
of either primary text was fetched. No primary literature beyond the
permitted local corpus was obtained.

**Reading — what this exercise repeats and must credit.**

The PR "soft-route" directory is
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

| Earlier statement, source and lines | Relation to this file |
|---|---|
| `gap-ext-astra.md:78–128`; `gap-expose-astra.md:573–599` | The Wilson conventions, (FQ), and (E17) are exactly the consumer in Step 1. No new reduction is claimed. |
| `gap-joint-astra.md:70–178,327–365` | Original-normalization joint representation and the distinction between signed and absolute sums are prior results. We do not work on row 817's shape classes. |
| `gap-gamma2-astra.md:73–226` | Bochner identity, Wilson Hessian bound, and equivalence of (G2) to a uniform invariant gap. C5 is the diagonal/mixed subtraction of that identity, not a new Bochner formula. |
| `gap-gamma2-astra.md:229–279,281–347,505–531,557–600` | Conditional sphere gap 2, mixed bound `-18 beta E`, diffusion bound `2-9 beta`, sharp worst-exterior influence threshold 2/9, and the retained-square identity are already present. Only the new reserves change the estimate. |
| `gap-vmf-lip.md:58–78`, with its prior-work record at 14–53 | The sharp chord influence 1/4 and exact one-link exponential family are prior work by Codex, checked by Claude Opus 5.5. D1 is a different Dirichlet-form inequality. It cannot improve that already sharp influence coefficient. |
| `gap-gamma2-astra.md:348–466` | The covariance/locality and conditional physical-transfer bridges are prior work, credited there to `gap-tu-retry.md`. They may consume C7 on its stated volume family, but compare no twisted normalizers. |
| `gap-crux-exercise-astra.md:830–858,920–972,985–1055` | Auxiliary mixing versus physical time, failed full-law convexity imports, density-oscillation comparison, and the price of changing the action were already explicit. B1–B4 test one concrete enlargement; they do not newly discover those general cautions. C7's finite-volume density comparison is the same elementary method. |
| `gap-crux-exercise-max.md:21–59` | The earlier max exercise stopped at Step 1. It already treats a route outside the seed formulation with a proved first statement as progress; it supplies no competing gauge-Hessian proof. |
| SA:588–599,31871–31882 | Scalar correlation decay need not exclude low spectral support. A1 is a finite-moment realization of this familiar danger, not a new claim that clustering is insufficient. Credit Sussman and Alpoge, with Claude and Codex as authors of their text. |
| PR 10133, soft-route `MASS_GAP_CW_CROSSOVER_ATTACK.md:115–174` | The six-staple sphere law and incidence counts already appear in Grok's crossover work. Its parallel-variance input is explicitly open there. It is not D1 or C4. No computer certificate is imported. |
| PR 10114, soft-route `CODEX_REVIEW_OFFGLOB.md:98–112` | Differentiated gauge invariance is already used for a critical background Hessian kernel. That is a Ward-identity precedent, not an arbitrary-test-function mixed-Hessian reserve on full link space. |
| main, `docs/POSITIVE_WILSON_VILLAIN_MIXTURE_AND_WEAK_REGION_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md:218–235` | A circle convolution/Gaussian limit. It is not a uniform tilted-S^3 diffusion estimate. |

**Reading — literature reused, with its limits.** The local digest
`prior/gap-lit-vmf-tor.md:17–46,58–83` records Föllmer, Dobrushin–Shlosman,
Wu, Ollivier, and Aizenman–Simon. The first group supplies conditional
mixing tools; the ferromagnet result has hypotheses unavailable for an
arbitrary Wilson background. The same digest distinguishes the
Tomboulis–Yaffe implication from a twist estimate, and finite-group local
clustering from periodic flux suppression. None is imported as a proof here.
The Gaussian identity B1 is the usual completion-of-the-square method;
no invention of that method is claimed. The scalar-moment construction
uses elementary finite interpolation, not a newly discovered moment theory.

The normalization question for Shen–Zhu–Zhu was already addressed in
PR 10114's `LITERATURE_BRIDGES.md:24` and
`checks/review_massgap_block_literature.md:26–41`. That earlier reader
records density `exp(N beta_S sum Re Tr U_p)` and
`|beta_S|<1/[16(d-1)]`. Comparing this recorded formula with ours gives
`beta_W=N^2 beta_S`, hence `beta_W<1/12` for SU(2), d=4. This is an
arithmetic comparison of the already recorded normalization, not a fresh
check of the primary paper. No claim about its optimal constant is made.

**Reading — novelty disposition after comparison.** No matching proof
of D1, C4 or C6–C7 was located in the searched record. The modest new
result claimed here is their explicit combination, improving the stated
thick-torus invariant-diffusion endpoint from 2/9 to 11/48. This is
new relative to the sources searched, not a global priority claim.
Neither the original order-one target nor the reserved flat-surface work
was found closed by a source read here. The exercise therefore continues
with its own bounded result rather than reopening an owned surface lane.

**Reading — mathematical lenses and reframes.** Spectral moment theory
gave A1; probabilistic enlargement gave B1–B4; Riemannian analysis gave
D1; graph incidence and the nonabelian gauge identity gave C4. Their
minimal tests are written above. The topology of a periodic twist and
representation-theoretic degree-twelve distinction were considered but
supplied no additional artifact outside existing work and row 817.
Category-theoretic, number-theoretic and logical reformulations supplied
no concrete changed object or test in this round and are not routes.
The useful change is from estimating each link response separately to
using constraints between derivatives on different links. The action,
group, original measure and physical target remain supplied model choices.

## Step 6. Try to break the routes

**Reading — diagnostic boundary.** The primary author checked A1 by
interpolation and by its operator realization, and B1–B4 by marginalization,
variance decomposition and the explicit link geodesic. These are author
checks. A separate route reader checked D1 by a different quadratic-form
calculation. Another checked the graph incidence count and C6–C7.
All are Codex gpt-6-astra/max. They are same-family diagnostics with
restricted inputs, not an independent audit or an independent-provider check.

| Route | Verdict and precise failed or surviving statement | Strength and reopening condition |
|---|---|---|
| A: finite scalar moments | Dead as a universal finite-moment certificate: A1 preserves every matrix entry while allowing arbitrarily small gaps. Wounded as a Wilson-specific route: that model imposes more than positivity. | Full contraction on the complete cyclic core is equivalent to the scalar gap, not a cheaper closing input. Relation to (T) remains unknown. Reopen with a Wilson-specific tail or exact closure theorem. |
| B: positive Gaussian enlargement | Exact marginal survives. Full-manifold positive curvature is dead for this lift, by B4. | Existence of a uniform invariant lifted gap is equivalent to the original diffusion-gap branch, by B3. Mark that fallback blocked-equivalent. Reopen with an actual integrated bound that uses the lift. |
| C: propagated gauge derivatives | Survives for all periods >=4, plus the four explicitly compared a=3 task shapes. The separately counted nonadjacent blocks make a strict improvement over the local reserve. | C4 is a proved geometric supplier, weaker than the needed order-one analytic estimate. C7 proves only its displayed interval. Reopen the order-one extension with a new bound on the mixed action term, not with the assertion of a gap. |
| D: sharp one-link sphere bound | Survives all h, including h=0 and both poles. Used with C it improves the range. Used only with old heat-bath contraction it improves a prefactor, not the endpoint. | No joint gap follows from D1 alone. Reopen further gains only if a joint estimate consumes the exact square remainders. |

**Proved scope checks.** No unbounded inverse, gauge-orbit division or
finite-spin cutoff enters C. The sign at the two endpoints of an oriented
link was checked explicitly. Both mixed Hessian sums are ordered; the
factor 18 is not divided by two. At transverse period four, opposite
neighbours are two steps apart; at axial period four one additional
matching edge is retained. Period three is treated only by the finite
comparison on the task's four shapes. Arbitrary thin-volume G2 is not
claimed. The logarithm in A's operator realization never meets zero,
and the added spectral tail has no second vacuum. B's curvature witness
does not assert a gauge-invariant gradient at its singular configuration.

**Reading — controls.** C's bracket source vanishes for U(1), and its
smooth differential objects do not exist on the finite group's support.
These are actual non-transfer steps, not a claim that all functional
inequalities fail in those models. A neutral scalar-gap route would have
to revise the finite-group control explicitly; it cannot silently certify
the original twist target. None of the tested routes proves confinement
in either negative control's weak-coupling regime.

## Step 7. Rank and keep an approach registry

**Suggested priority.** Rank by evidence gained per next proof obligation,
not by a claimed probability of solving the mass gap.

| Rank / family | Changed premise and mechanism | Terminal obligation; relation to target | Evidence, cost and stop/reopen condition |
|---|---|---|---|
| 1; joint differential estimate C+D | Drops separate-link response as the proof architecture. Noncommuting vertex gauge flows force mixed derivatives, including nonadjacent links. | At order one, a positive uniform lower bound on Q/E is still needed. This is equivalent to the diffusion-gap branch; its relation to the specified twist rate is not proved. | First concrete artifacts D1 and C4 are proved here. Small-range branch is complete as an author argument. Order-one branch is blocked-local: use the exact remainders with C_m or stop; more small constant refinements alone do not reach the requested interval. |
| 2; scalar spectral route A | Drops the twist observable and works on the actual scalar transfer sector. | Uniform spectral exclusion on the entire scalar cyclic core is target-equivalent to the ultimate scalar gap. It is not shown equivalent to (T). | Finite-moment shortcut is refuted; a new tail theorem is expensive and absent. Reopen only with dynamical information not captured by A1. |
| 3; enlarged-law route B | Changes carrier while retaining the exact Wilson marginal. | A uniform invariant lifted gap is equivalent to G2 on the same interval. | Exact normalization is cheap and settled; pointwise curvature fails. Integrated lifting is blocked-equivalent without a new estimate. Reopen only on a concrete inequality beyond B3. |

The registry's completed item is the small-interval estimate, not the
mass-gap target. The primitive and action choices remain named supplied
inputs. No branch is described as the unique route or a final route.

## Step 8. Written decisive tests and their recorded outcomes

**Proved / diagnostic-checked, with provenance.** The tests below are
hand arguments. Their original success conditions are retained. Validation
of an already seen candidate is labelled validation, not a new blind
prediction. No program evaluated an eigenvalue, enumerated configurations,
or discharged an inequality. Source searches and file bookkeeping are the
only computations in this exercise.

| Test and prior reading | Actual result | What it decides |
|---|---|---|
| D1, registered in Step 4: all fields and every radial/angular mode, unit-sphere gap at least 3 | Pass by D2–D6. Separate quadratic-form check below finds no failing step. | A sharp local supplier is available; tensorization is not inferred. |
| C's route brief: derive a gauge-specific joint estimate that goes beyond beta<2/9 | Pass for the narrower thick-torus diffusion question: C4 and C6–C7. At `beta_+=9/40`, `33/8-18 beta_+=3/40`; endpoint gain is `1/144`. | The small coupling range is strictly enlarged. This was not substituted for the caller's order-one completion criterion. |
| Same C mechanism at beta=1/2 | Its displayed certificate is negative: `33/8-9=-39/8`. | This bound fails to certify that coupling. It is not a negative Rayleigh quotient and does not refute the true gap. |
| A's finite-moment certificate | Fail: A1 and its finite-dimensional approximants retain all the required entries with gaps tending to zero. | Positivity and a finite scalar matrix alone do not suffice. Wilson-specific structure remains outside the counterexample. |
| B's positive full-manifold curvature mechanism | Fail: B4 tends to minus infinity at every positive beta. | That proof mechanism fails for this enlargement; invariant integrated estimates are not refuted. |

The separate reader checked D1 by completing forms. For its radial
operator let `a=1-x^2`, `w_0=e^(hx)a^(1/2)`, `w_1=a w_0`, and v=u'.
Direct expansion and integration by parts yield

\[
 \|A_0u\|_{w_0}^2-3\int a|u'|^2w_0
 =\int a|v'+(2h/5)v|^2w_1
       +\frac{6h^2}{25}\int a|v|^2w_1\ge0.                 \tag{D8}
\]

For the angular sector, the corresponding form identity is
`<u,A_lu>-l(l+2)||u||^2 = int a|u'+alpha h u|^2 w_l
+alpha(1-alpha)h^2 int a|u|^2 w_l`. This checks the signs and both
pole limits through a quadratic-form path. Smoothness excludes the
singular radial branch, even when that branch would be square integrable.

The graph reader separately recounted the fourteen vertices and seven
coefficients per row, including the period-four wrap, and recomputed
the complete-graph square identity and ordered plaquette count. No
failing step was found in C1–C7. The exact checked source was
`/tmp/sa-gap-shape-diffusion.dve0rs2c/proof-20261112.txt`, SHA-256
`c8ce1947cdcba348f0d79c8c24f4bf5da41c9bd79aaa9f06e7b56a0a3c7d8e98`.
The primary author then checked the transcription into this output.
The sphere reader's distinct calculation is preserved in
`/tmp/ym4d-scalar-reframe.YjkBEy/TILTED_SPHERE_CHECK.md`.
Both readers were configured gpt-6-astra/max. These checks used different
calculations where specified but remain within this author-led, same-family
exercise; they grant no independent scientific status.

The proof dependencies are acyclic: one-link sphere geometry gives D1;
gauge invariance and graph geometry give C4; the already proved Bochner
identity and plaquette Hessian bound then give C6. Density comparison
covers exactly the finite exceptions. There is no imported gap, twist
bound or target-equivalent hypothesis in this small-range proof.

No Lean formalization was run or requested. The proof uses finite sums,
smooth compact-manifold integration, elementary graph linear algebra and
the compact elliptic spectral theorem; no computational certificate is
hidden in a leaf. Independent-provider checking is still absent.

## Step 9. Report and handoff

**Reading — the wall.** We still lack the required estimate showing that
the global sign change has little effect in the original theory at the
requested couplings. Changing its description does not remove that cost.
The small-coupling result below does not settle the continuum mass gap.

**Proved here, with same-family diagnostic checks — what changed.**
Gauge symmetry forces derivatives on different links to constrain each
other. Keeping that relation gives a bound which a separate-link estimate
misses. Combined with a sharp one-link bound, it extends a proved interval
for the auxiliary diffusion from beta<2/9 to beta<11/48 on the stated
volume family. This is a small improvement, not passage through the main
wall. A finite set of scalar measurements and the tested Gaussian
curvature shortcut each fail by the written examples above.

**Suggested — work worth doing.** The joint derivative route has one
concrete next question: can its exact positive remainders pay for the
mixed derivatives of the action without replacing all of them by their
absolute bound? A useful follow-up must prove such an estimate at a
named larger coupling. It must keep the original probability law and
the comparison groups. Further small improvements in the graph constant
alone should not be presented as an order-one mechanism. The scalar
route needs a new theorem controlling the unmeasured spectral tail;
the Gaussian route needs a new integrated estimate. Neither is currently
a cheaper closing problem.

**Reading — what not to do next.** Do not rerun the sharp chord influence
calculation, claim a gap from finitely many scalar moments, insert a
different vacuum normalizer, or assume the Gaussian lift is convex.
Do not duplicate row 817. Do not identify auxiliary stochastic time with
physical Euclidean time or omit the cutoff-uniform physical-unit bridge.

**Reading — exact price and scope.** No new premise decision equivalent
to the main wall was established. B3 gives an exact equivalence to the
already existing diffusion-gap branch; A's complete-core contraction is
the scalar gap itself. Neither is a cheaper physical assumption. The
strongest constructive result of this exercise is (C7), with (C4) its
new geometric ingredient in the searched record. Applying the existing
equivalence in `gap-gamma2-astra.md:192–209` supplies G2 on this same
family and interval. Applying its locality theorem supplies its stated
same-measure covariance bound there. Neither application compares the
two twist normalizers at the fixed eta_* rate.

**Reading — appendix and recovery.** Steps 1–8 contain the contract,
assumption and variation ledgers, family registry, proofs and tests.
The assumptions most liable to waste work are that the twist criterion
is logically mandatory for every scalar proof, that absolute activity
bounds are necessary, and that single-link sharpness limits all joint
estimates. The costly assumptions to change are the Wilson action,
the state/limit sequence, and normalization; each carries an identification
or uniformity debt. D1 and C4–C7 are candidates for a later checked
research note, not an automatically authorized PR or status change.
The useful tools are spherical form completion, vertex Ward identities
and graph incidence estimates. The existing stochastic locality bridge
should be reused rather than translated again from literature.

## Final checkpoint

Source base and six comparison refs are recorded above. All Steps 0–9
are complete. Open obligations: the order-one joint estimate, (T)/(FQ),
and the physical continuum bridges. Failed routes retained: finite scalar
moment certification and full positive curvature of the explicit Gaussian
lift. Next decision: review the small-range proof, then pursue a concrete
mixed-action estimate only if it can go materially beyond (C6).
No audit, ledger, registry, FINISH row, source proof or remote branch was
changed. This is the only changed checkout file, on
`research/gap-shape-exercise-astra-61af70a26`; it is uncommitted and unpushed.

## Measure of the skill

The first success measure is met: a distinct route has its first written
test completed, with a positive small-range result and scoped failures
recorded. No new exact premise price or checked global misframing was
established. This exercise produced more than a map, but it did not get
past the main order-one wall. Its gain is the explicit endpoint extension
by 1/144 for the auxiliary invariant diffusion on the stated boxes.

RESULT: SMALL-RANGE ADVANCE, MAIN CRUX OPEN — hand proofs of the tilted-S^3 gap 3 and the gauge-invariant reserve H_m>=9E/8 give the uniform twisted Wilson diffusion bound (C7) for beta<11/48; same-family diagnostic checks found no failing step, no independent-provider status is granted, and the order-one twist deficit, fixed-rate (E17), and continuum mass gap remain unproved.
