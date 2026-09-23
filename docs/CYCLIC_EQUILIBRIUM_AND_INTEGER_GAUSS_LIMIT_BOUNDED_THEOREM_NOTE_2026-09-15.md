---
claim_id: cyclic_equilibrium_and_integer_gauss_limit_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/cyclic_equilibrium_check_2026_09_15.py
upstream_dependencies: ["docs/POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md"]
claim_scope: "Bounded conditional cyclic equilibrium and integer Gauss limit; supplied hypotheses and limit order retained in full proofs."
---

# Cyclic equilibrium and integer Gauss limit

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

- [POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14](POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md).

Evidence correction: the separate three-level search mentioned in the original narrative has no recovered separate source/output. That ancillary narrative is unverified and supplies no numerical evidence here; the analytical proof and identifiable final program remain separately scoped.

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK16_CYCLIC_EQUILIBRIUM_AND_INTEGER_GAUSS_LIMIT

Original source identity: `BLOCK16_CYCLIC_EQUILIBRIUM_AND_INTEGER_GAUSS_LIMIT.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Cyclic equilibrium states, disappearing Gauss aliases and rotor limits

Personal derivation, 2026-09-15. PROVISIONAL. Personal checks and review complete.
No independent audit. This is a regulator/state theorem for a supplied model,
not a photon, Weyl, Coulomb or symmetry-breaking phase theorem.

#### 1. Fixed model and the missing state bridge

Use the full model in main revision e0ef7cf4633034a8c1e6d57f5812cc4275bf1349,
POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION,
dated2026-09-14. That source has been read in full. It proves positive projected
finite-slice histories and local finite-time rotor approximation for states
with an initial electric cap. It does not prove that its equilibrium states
converge. Block12 treats a different, hard integer-link regulator and does
not discharge the cyclic aliases considered here.

Fix a nondegenerate periodic cubic L^3 graph, N=2S+1>=3 odd cyclic states per link, m CAR
orbitals of each charge per cell, and fixed translation-invariant couplings.
All limits here keep the lattice spacing, gauge coupling and Hamiltonian
coefficients fixed. In particular all three electric coefficients k_i>0.
Zero electric stiffness and a simultaneous weak-coupling limit are excluded.

In centered electric representatives n=-S,...,S, the link energy is

 lambda_(N,i)(n)=k_i n^2 sinc^2(pi n/N),
 k_i=g^2 w_i/(2a)>0.                                    (1)

The magnetic terms are K_p(1-Re U_p), K_p>=0. Matter has the conjugate
number-preserving blocks c_+^dag h(U)c_+ and c_-^dag h(U)^*c_-, with
Q_x=N_(+,x)-N_(-,x), and optionally(u/2)sum_x Q_x^2, u>=0. All non-electric
interactions have fixed bounded finite-range norms. The physical projection
imposes G_x=div E_x-Q_x=0 modulo N, not as an integer.

Let e_on be the exact minimum of the paired onsite matter term in one cell.
If the plus onsite matrix is v, then e_on=2 sum_(nu<0)nu, counting its
eigenvalues. Fill the corresponding negative onsite orbitals in both
conjugate species. This onsite ground state has Q_x=0, including a balanced
choice in any zero eigenspace. Its product over cells and all E_l=0 is an
exact modular and integer Gauss state. Its hopping expectation vanishes,
and its magnetic energy is sum_p K_p.

Write each hopping term as V_l+V_l^dag, including both charges in V_l, and put

 B=[sum_p K_p+2 sum_l ||V_l||]/L^3.                     (2)

This is independent of L,N for the stated homogeneous model. The bound
||V_l||<=2||T_l||_* follows from CAR and the two conjugate species; an upper
bound may be used in(2). Finite cell periodicity can be treated with finitely
many types; no arbitrary inhomogeneous pointwise moment bound is asserted.

#### 2. Uniform electric moments for exact cyclic ground and Gibbs states

Concavity of sine on[0,pi/2] gives, for all centered representatives,

 c_E k_i n^2 <=lambda_(N,i)(n)<=k_i n^2,
 c_E=4/pi^2.                                            (3)

Unlike a bare bound on the dimension, this is uniform as N increases.
The onsite lower bound, positive magnetic and charge-square terms, hopping
norm bound and the physical trial state above give for a translation-averaged
ground-state density matrix

 sum_i k_i <E_(0,i)^2> <= B/c_E.                        (4)

The averaging permits degeneracy and does not select a pure phase.

Now take the EXACT physical finite-volume Gibbs density

 rho_(L,N,beta)=P_N exp(-beta H_N)/Tr[P_N exp(-beta H_N)],
 beta>0.                                               (5)

It is translation invariant. Its entropy is the ordinary density-matrix
entropy, including its zero eigenvalues outside the physical subspace.
Compare it, by nonnegative quantum relative entropy, with the full-space
product reference proportional to

 exp[-(beta c_E/2) sum_l k_l E_l^2] tensor I_matter.

No projection of that reference is required. If
theta(q)=sum_(n in Z) exp(-q n^2), define

 s(beta)=2m log2+sum_(i=1)^3 log theta(beta c_E k_i/2).

Then the entropy bound is

 S(rho)<= (beta c_E/2) sum_l k_l <E_l^2>+L^3 s(beta).     (6)

The finite cyclic Gaussian sum is at most theta. For an elementary finite
upper bound, theta(q)<=1+sqrt(pi/q), from the decreasing Gaussian integral.
The Gibbs variational principle with the physical pure trial gives
F<=L^3 e_on+sum_p K_p. Conversely(3),(6) and the hopping lower bound give

 sum_i k_i <E_(0,i)^2>
       <=(2/c_E)[B+s(beta)/beta].                       (7)

For every fixed beta0>0, the right side is uniformly bounded for
beta>=beta0, L and odd N. Indeed s is decreasing and positive. This proves
thermal tightness without a log N entropy loss. It does not assume that the
cyclic state is flux diagonal or that Gauss and hopping can be classicalized.

Let K_i denote the resulting uniform bound on each <E_(0,i)^2>, using(4)
for ground states or(7) with beta0 for the Gibbs family. Constants depend
on the fixed couplings and beta0; they need not remain bounded as g->0.

#### 3. Modular aliases disappear locally

Embed every cyclic link into the rotor basis using its centered representative.
On a modular physical basis vector, the integer operator G_x has eigenvalues
in N Z. Since |Q_x|<=m and each cubic vertex has six incident links,

 Prob(G_x!=0) <=<G_x^2>/N^2
   <=7[2 sum_i K_i+m^2]/N^2.                           (8)

The first inequality uses the actual modular support, not just gauge
invariance of a density matrix. The second is scalar Cauchy-Schwarz for
the seven commuting integer quantities. The bound remains valid for
coherent density matrices because all projectors and squared quantities
in this inequality are diagonal and it is an operator inequality on the
modular physical subspace.

For any fixed finite vertex set X, the union bound multiplies(8) by |X|.
There is no claim that the probability of ANY alias in the whole growing
torus tends to zero. That global conclusion would require a relation between
L and N. The local conclusion does not. In particular finite total-charge
aliases need not be deleted by hand from the projected trace.

#### 4. Local normal compactness in simultaneous limits

For a finite carrier region R with n_R links, let P_(R,M) project every
such electric number to |E_l|<=M and retain all its finite matter space.
The moment bounds give

 Tr[rho_R(1-P_(R,M))] <=n_R K_max/(M+1)^2,
 ||rho_R-P_(R,M)rho_R P_(R,M)||_1
       <=2 sqrt(n_R K_max)/(M+1).                      (9)

The second is the gentle projection bound for the SUBNORMALIZED projected
state. Its finite rank depends only on R,M, not on ambient L,N. Finite-rank
compactness followed by(9) therefore gives trace-norm precompactness of
every local marginal. A diagonal subsequence through an exhaustion of
regions yields consistent trace-one normal marginals and a locally normal
state on the infinite rotor/CAR algebra.

This works for arbitrary joint L,N->infinity sequences, for ground states
or for Gibbs states with beta>=beta0. No growth-rate relation is required.
By(8) and local trace convergence, every limit obeys

 omega(1_(G_x=0))=1 for every x.                        (10)

It is thus supported on exact INTEGER Gauss law. Translation symmetry of
the averaged finite states passes to the limit; a pure-phase selection does
not follow. No global postselection onto a growing flux cap is used.

Local trace compactness of unbounded quantum rotators is established
mathematical practice; see [Kelbert and Suhov](https://arxiv.org/pdf/1206.1229),
section1.4, for a different two-dimensional rotator Gibbs construction.
Their symmetry theorem and model hypotheses are not imported here. The
coercive cyclic energy, entropy bound and modular-to-integer estimate above
are the regulator-specific inputs to this direct proof.

#### 5. Finite-time convergence now applies to these equilibrium states

The current cyclic parent provides an ambient-volume-independent locality
bound and an explicit finite-region comparison epsilon_(N,R)(t,M) for
initial support |E_l|<=M. At fixed R,M,t it tends to zero as N->infinity:
its terms are O(N^-2) plus a wrap/truncation exponential. All interaction
norms and the locality velocity are independent of N; the large diagonal
electric energy is placed in the onsite interaction picture.

For a bounded even observable A supported in X, choose a larger R. Replacing
the local initial marginal by P_(R,M)rho_R P_(R,M) costs, in expectations,
at most a constant times ||A|| sqrt(n_R K_max)/(M+1). The subnormalized
version of the parent's bound follows by linearity; no conditioning
probability is divided out. After restriction to R, compare the two
dynamics with its finite-cap estimate. Thus an error majorant has the form

 2 B_R(t)+4||A|| sqrt(n_R K_max)/(M+1)
               +2||A|| epsilon_(N,R)(t,M),             (11)

where B_R(t)->0 as R grows at fixed t. Constants can be enlarged harmlessly
if both regulator initial states are separately projected. The order is:
fix t and accuracy, choose R, then M, then N. Ambient volume is absent.
The initial local states themselves converge in trace norm by section4.

This proves convergence of local real-time expectations to the rotor
dynamics. It also proves stationarity of a limiting equilibrium state,
because each exact finite state is stationary. This reasoning needs only
strong continuity in locally normal states. Operator-norm continuity of
unbounded-onsite rotor dynamics on all local bounded operators is not
assumed.

For correlation functions start with a physical finite-electric-core
operator A=P_(X,M0) A P_(X,M0). Its cyclic compression preserves modular
Gauss law, and A or A^* acting on a moment-controlled state has the same
local tail control away from X and finite support on X. Polarizing the
states obtained from I+zA, z=1,-1,i,-i, or applying the finite-region
propagator comparison to these vectors, proves convergence of

 F_A(t)=omega(A^* alpha_t(A)).                          (12)

No bound on a normalized postselected vector is used. General bounded
physical local operators follow by finite-core compression: local normality
makes A_M Omega->A Omega and A_M^* Omega->A^* Omega. Stationarity bounds
the resulting correlation error uniformly in real t.

#### 6. Cooling the cyclic Gibbs states yields actual rotor ground states

Suppose also beta->infinity, with arbitrary joint rates relative to L,N.
For finite physical Gibbs matrices and a physical observable A, write

 F_A(t)=int exp(it nu) dmu_A(nu).

The spectral measure has weights p_n |A_mn|^2 at nu=E_m-E_n. Swapping m,n
gives the exact detailed-balance identity, for nu>0,

 dmu_A(-nu)=exp(-beta nu) dmu_(A^*)(nu).                 (13)

Consequently for every epsilon>0,

 mu_A((-infinity,-epsilon])
        <=exp(-beta epsilon)||A||^2.                   (14)

The limiting real-time correlations in(12) are positive definite and
continuous at zero. Their finite positive measures converge weakly; testing
with compactly supported functions in negative energies and using(14)
shows that the limit has no negative spectral support. In the stationary
GNS representation the implementing unitaries act by
U_t A Omega=alpha_t(A)Omega. The dense set of physical local vectors has
nonnegative generator spectral measure, hence the generator is positive.
The limit is a ground state of the interacting rotor Hamiltonian on its
physical observable algebra.

The same conclusion holds starting directly from exact cyclic ground-state
mixtures: their measures already have no negative support and(4) supplies
the tighter moments. This argument does not assume a finite-volume gap,
a unique vacuum, exponential clustering or an isolated charged pole.

At a fixed finite beta limit, the same measure argument retains(13) rather
than replacing it by(14). To pass detailed balance to the limit, first
test the full signed-frequency identity on compact frequency intervals;
the exponential factor is uniformly bounded there. Exhaustion then gives
the measure identity, including the zero atom. It supplies the two-point beta-KMS boundary
condition on physical local observables in the locally normal stationary
representation: F_A(t+is)=int exp(it nu-s nu)dmu_A(nu) is bounded and
analytic for0<s<beta, and detailed balance identifies its other boundary.
Polarization gives cross observables. This is a statement in that weakly
continuous representation, not a claim of norm-continuous rotor dynamics
on every bounded local operator.

#### 7. Fixed-volume spectral comparison and positive-history provenance

At a FIXED finite graph, the same coercive bound gives global trace
compactness of cyclic ground states. Any finite-energy physical rotor
trial vector can be approximated in its form norm by a finite electric
core. Such a vector is also modular physical after embedding for large N.
On that core, lambda_N(E)->k E^2 and all bounded hopping/plaquette terms
converge to their rotor counterparts. Variational upper bounds follow.

For the lower bound, use(3) for tightness, local finite-core pointwise
convergence for the positive electric form, and bounded strong convergence
for the remaining finite-graph interactions. Fatou's inequality and trace
compactness give the rotor ground-energy lower bound. Thus the finite-graph
cyclic ground energies converge to the physical rotor ground energy, and
ground-state limit points lie in its ground subspace. No rate or preferred
basis in a degenerate ground subspace is claimed.

The exact finite-volume Gibbs traces in this construction already have the
parent's nonnegative Gauss-projected finite-slice representation, followed
by its Trotter limit. If desired, for each finite L,N,beta one may choose
enough symmetric slices to approximate its density matrix before taking
the diagonal state limit. Finite-dimensional convergence supplies this
existence choice. No volume-uniform slice count, efficient sampling method,
positive estimator for every observable or converged continuum history
measure is asserted.

The result closes a STATE/REGULATOR bridge: local normal equilibrium limits,
integer Gauss support and zero-temperature spectral positivity. It does not
identify which phase those states realize. A Coulomb photon, protected Weyl
matter, absence of spontaneous pairing, a common interacting light cone,
or a physical selection of this supplied law remain separate questions.
In particular this N->infinity theorem proves no phase for a fixed finite
link payload and makes no simultaneous g->0 claim. No axiom update is forced.

#### 8. Personal verification and its limits

The accompanying checker constructs a four-edge charged cycle with two
opposite-charge CAR modes per vertex. It is a noncubic fixture. For N=3,
direct enumeration of all electric fields followed by exact modular Gauss
projection agrees entrywise with the reduced flux-coordinate construction;
the independently assembled 256-dimensional matter matrices satisfy CAR.
The physical dimensions for N=3,5,7 are258,350,490, including106,58,58
basis vectors with at least one integer Gauss alias. No alias sector was
silently removed.

All twelve exact finite Gibbs fixtures, beta=.5,1.5,5,15 at each N, obey
the entropy, electric-moment, alias and detailed-balance bounds. The bounds
are deliberately conservative: at beta=.5 the electric-square bound is
about254 while measured totals are between2 and4. The probability of any
alias on this FIXED cycle at beta=.5 is approximately.302,.0296,.00177
for N=3,5,7. This finite observation is not the proof of(8). Detailed
balance discrepancies are below7e-19.

Hard integer cutoffs through12 and cyclic N through33 give converging
finite-graph ground energies. The hard-cutoff12 comparator is approximately
.0964258280 and cyclic N=33 gives.0959982737. The hard comparator is still
finite, not an exact infinite-rotor value or a certified convergence rate.
Sparse searches use a deterministic generic complex initial vector to
avoid excluding a symmetry sector. A separate three-level search confirmed
the N=9,N=17 and hard-cutoff4 minima against the initial constant-vector
search. Residuals are reported in the evidence, not interpreted as proofs
of a phase or of the infinite theorem. No scientific check failed.

This is author verification. The compactness, dynamics and spectral-limit
arguments still require independent mathematical review before retention.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK16_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK16_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Block16 route and no-go review

PROVISIONAL personal review. No independent audit and no axiom update.

N1 — Alternatives. Hard integer truncation already has Block12's state
bridge. The cyclic regulator has positive projected histories and distinct
modular aliases, so that result does not replace this proof. Direct
finite-temperature compactness, ground-state compactness, cooling Gibbs
states and fixed-volume min-max are all retained routes.

N2 — Wall independence. No claimed obstruction is proved. The constants
diverging at g->0 do not establish a physical weak-coupling failure; they
only delimit this fixed-coupling estimate.

N3 — Hidden assumptions. Positive electric coefficients, fixed finite
orbital number, bounded finite-range interactions, paired onsite trial,
nonnegative magnetic/charge-square terms, translation averaging and exact
physical projection are explicit. A phase, vacuum gap, unique state,
exponential clustering or norm continuity on all local bounded operators
is not inserted.

N4 — Residual matching. The parent gives finite-time comparison only from
an electric cap. The new entropy/moment argument supplies local caps for
equilibrium states. Modular support, rather than mere gauge invariance,
is used to suppress aliases. The limiting integer Gauss state and its
positive spectral generator are matched to the full supplied rotor law.

N5 — Rhetoric. This is state/regulator existence and spectral positivity.
It does not prove a Coulomb, Weyl or unpaired phase, nor a physical
selection of this Hamiltonian from the axioms. The ground limit is not
identified with a particular vacuum.

N6 — Partial closure. Arbitrary joint volume/regulator/cooling sequences
have subsequential local limits. Fixed beta gives a two-point KMS limit;
fixed finite graph gives ground-energy convergence. Rates, uniqueness,
global alias probability and fixed finite-payload phase remain open.

N7 — Steelman. Even though finite aliases exist and finite-slice positivity
alone proves no state limit, coercive energy and relative entropy give the
missing tightness without a log N penalty. No global charge postselection
or normalized rare-event division is needed. This is the strongest
positive route established in this block.

N8 — Cross-cycle echo. Block12's hard-cutoff proof is credited, and the
new main positive cyclic source is credited for dynamics/history positivity.
The new pieces are uniform cyclic equilibrium tightness, local removal
of modular aliases and the Gibbs-cooling spectral argument. The source's
earlier finite N=3/N=5 alias census was diagnostic, not this state theorem.

Disposition: provisional positive theorem. Broad no-go: FAIL / not claimed.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: cyclic_equilibrium_check_2026_09_15](../scripts/cyclic_equilibrium_check_2026_09_15.py); [current cache](../logs/runner-cache/cyclic_equilibrium_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
