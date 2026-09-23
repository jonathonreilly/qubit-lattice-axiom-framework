---
claim_id: fixed_coupling_rotor_ground_cutoff_compactness_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/ground_cutoff_check_2026_09_15.py
upstream_dependencies: ["docs/CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13.md"]
claim_scope: "Bounded conditional independent rotor ground-cutoff compactness; supplied hypotheses and limit order retained in full proofs."
---

# Independent rotor ground-cutoff compactness

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

- [CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13](CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13.md).

This ground-cutoff construction is independent of the supplied continuum quartet/action.

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK12_GROUND_STATE_CUTOFF_COMPACTNESS

Original source identity: `BLOCK12_GROUND_STATE_CUTOFF_COMPACTNESS.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Ground states, electric tightness and removal of the link cutoff

Personal derivation, 2026-09-15. PROVISIONAL; personal review and bounded checks completed.
No independent scientific audit or retained-status decision.
This is a state-construction result for a supplied Hamiltonian. It does not
establish a Coulomb phase or identify the formed physical vacuum.

#### 1. Target and precise hypotheses

Use the homogeneous charged Hamiltonian of the fully read source
`docs/CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13.md`
at immutable main083a58b4e7faca5839a7b31fab553f6fa1f2c254. Its inputs are a
cubic graph, four CAR orbitals per cell, integer electric fields E_l,
bounded link/plaquette shifts, and continuous Hamiltonian time. Work on
periodic cubes whose side tends to infinity. Parameters a,g>0, r>=0 and
positive weights w_i are fixed while volume and link cutoff vary.

Let H=H_on+H_E+V, where

 H_E=sum_(x,i) k_i E_(x,i)^2,  k_i=g^2 w_i/(2a),
 H_on=(r/a)sum_x c_x^dagger h_on c_x,
 V=sum_alpha(V_alpha+V_alpha^dagger).

The local matrix is h_on=B0 sigma3+tau_x(m1 sigma1+m3 sigma3),
B0=2+zeta, with the aligned or nearby mixed carrier parameters. Hopping
has norm at most2r/a per positive link. A plaquette normal to i has shift
coefficient w_i/(2g^2 a). There are three positive links and three
plaquettes per cell. All electric shifts are at most one per affected
link. Gauss operators are G_x=div E_x-(N_x-2).

P_S is the product of |E_l|<=S projections; H_S=P_S H P_S on its range.
Choose a density matrix supported on the lowest eigenspace of H_S in
G_x=0. Average it over translations and, if desired, the supplied ordinary
time reversal. Degeneracy is allowed. Write the resulting state omega_(L,S).
It is embedded into the full rotor Hilbert space by the natural inclusion.
Only physical, even observables are used for the ground-state assertion.

The claim is that every sequence L_j->infinity, S_j->infinity has a
subsequence converging in trace norm on each fixed finite region to a
locally normal, physical, translation-invariant rotor ground state.
The order or relative rates of these two limits need not be prescribed.
There is no assertion that different subsequences select the same state.

#### 2. A volume-independent electric moment from an actual physical trial

The eigenvalues of h_on are +/-epsilon_+ and +/-epsilon_-, where
 epsilon_eta=sqrt(m1^2+(B0+eta m3)^2).
Consequently its second quantization has minimum
 -e_on=-(epsilon_++epsilon_-), attained by filling the two negative
one-particle levels. The full Fock-space inequality is

 H_on >= -(r/a)e_on L^3.                            (1)

Take that two-particle onsite Slater state at every cell and E_l=0 on all
links. This is an exact physical state: N_x=2 and div E_x=0. It belongs
to every cutoff including S=0. Each hopping or plaquette expectation
vanishes because it shifts at least one zero-flux link. Its energy is
exactly the right side of(1). Thus, with E_(L,S) the physical ground energy,

 E_(L,S) <= -(r/a)e_on L^3,
 sum_l k_l omega_(L,S)(E_l^2) <= 2 sum_alpha ||V_alpha||.
                                                               (2)

The second line follows by subtracting(1) and using V>=-2sum||V_alpha||.
It does not replace a physical trial by a gauge-violating free Slater/link
product: the local N=2 and zero flux are the relevant exact constraints.
The onsite Slater state is only a variational comparison, not the claimed
interacting ground state.

Define the per-cell bound

 B=[12r+(w_x+w_y+w_z)/g^2]/a.

Translation averaging gives, for m_i=omega_(L,S)(E_(x,i)^2),

 sum_i k_i m_i <= B,
 m_i <= K_i=B/k_i
      =2[12r+(w_x+w_y+w_z)/g^2]/(g^2 w_i).         (3)

K=max_i K_i is finite and independent of L and S. The bare factor a cancels
in this static estimate, but this is not a continuum-limit theorem.
The weak-coupling bound is conservative: K generally grows as g^-4.
No claim of a bound uniform in g->0 is made.

For a finite region X containing m links, let P_(X,M) cut only those links.
Since the omitted integer flux has magnitude at least M+1,

 omega_(L,S)(I-P_(X,M)) <= m K/(M+1)^2.            (4)

The projectors commute with every Gauss operator. No factorization of the
physical Hilbert space across the boundary is assumed. Reduced density
matrices are taken in the ambient matter/link tensor product (or its even
CAR equivalent), then the local Gauss conditions are imposed.

#### 3. Local compactness and preservation of Gauss law

The projection P_(X,M) has finite rank on the finite region, including its
finite-dimensional matter factors. The positive reduced density matrices
rho_(L,S),X have trace one. The gentle projection estimate gives

 ||rho_X-P_(X,M) rho_X P_(X,M)||_1
       <=2 sqrt(mK)/(M+1).                        (5)

A short proof uses a purification psi: the trace distance between
|psi><psi| and |Ppsi><Ppsi| is at most2||Qpsi||, and partial trace is
contractive. The projected state is not renormalized. On each fixed
finite-rank subspace, density matrices form a compact bounded set.
First choose M for the desired error in(5), then extract a convergent
subsequence in that finite matrix space. This proves trace-norm
precompactness of the full local density matrices.

A diagonal extraction over countably many nested boxes gives consistent
trace-one local limits and hence a locally normal infinite-volume state
omega. Equation(3) passes by truncating E_l^2 first and using monotone
convergence. Translation and time-reversal invariance pass through local
expectations. On the star of x, the bounded unitary exp(itG_x) has
expectation one in every finite physical state, for all real t, and hence
in omega. Equivalently its local density matrix is supported on G_x=0.
The limit is physical without postselecting a probability that vanishes
with spatial volume.

This argument establishes subsequence compactness. It supplies no rate
at which a chosen ground state approaches a particular limiting state.

#### 4. Ground-state inequalities survive exactly on a local core

Let A be an even, gauge-invariant operator supported in a fixed finite
region X, with finite electric support on every link in X:

 A=P_(X,M0) A P_(X,M0).

For S>=M0, A and A^dagger preserve the global cutoff space. Their matter
support is finite; their flux support makes [H_E,A] bounded. Only finitely
many bounded interaction terms fail to commute with A, so A^dagger[H,A]
is a bounded operator on a fixed finite neighborhood.

For any finite ground vector psi in the support of omega_(L,S),
A psi remains physical and remains in P_S. Therefore

 <psi,A^dagger[H,A]psi>
   =<Apsi,(H_S-E_(L,S))Apsi> >=0.                 (6)

The equality also uses P_S A^dagger A=P_S A^dagger A P_S: the component
of Hpsi outside the cutoff has zero pairing with A^dagger A psi.
There is no assumption that Hpsi=E_(L,S)psi in the full rotor space.
The same identity holds for mixtures in the ground eigenspace.
Once the periodic box contains the neighborhood, the commutator is the
same local expression as in the infinite lattice. Local trace-norm
convergence now gives

 omega(A^dagger[H,A])>=0                          (7)

for every such physical finite-electric-support A. The finite cutoff is
removed on the test operator, not by applying a global cutoff to a
thermodynamic state. In particular, no many-body spectral gap is used.

#### 5. Dynamics comparison for these actual ground states

The source's bounded-shift and Lieb-Robinson proof gives constants C_X,v,nu
independent of L,S for a bounded even local observable A. Let B_R be a
neighborhood with m_R links and J_l=sum_(alpha touching l)||V_alpha||<=J.
Use a local preliminary cutoff M<S in B_R. Its probability cost follows
from(4), and its subnormalized projected state differs by at most
2 sqrt(m_R K)/(M+1) in trace norm. Comparing two norm-preserving
Heisenberg evolutions costs twice that amount times ||A||.
Combining this with the source's finite-time cutoff estimate yields

 |omega_(L,S)(alpha_t^H(A))-omega_(L,S)(alpha_t^(H_S)(A_S))|
 <=2 C_X||A|| exp(v|t|-nu R)
   +4||A|| sqrt(m_R K)/(M+1)
   +4||A|| |t| m_R J exp[-lambda(S-M)+2J|t|sinh(lambda)].    (8)

A_S means compression; its expectation at t=0 equals that of A in the
embedded state. The first term includes one spatial restriction for each
evolution. Both dynamics may first be compared in a finite larger box;
the same locality estimate defines the infinite rotor evolution on local
observables. Unbounded E^2 causes onsite phases, not an extra propagation
constant. Strong continuity in locally normal states suffices here; norm
continuity on the entire algebra of all bounded rotor operators is not
assumed.

At each fixed t and accuracy, choose R, then M, then S. All choices are
independent of the ambient torus once it contains B_R. Since the cutoff
state is stationary under H_S, the limit omega is stationary under rotor
dynamics. Choosing M=floor(S/2) also makes the two cutoff errors vanish
at fixed R,t; this does not control t->infinity at fixed S.

#### 6. Spectral ground-state condition, not only stationarity

For finite-electric-support physical A as in section4, define

 F_(L,S),A(t)=omega_(L,S)(A^dagger alpha_t^(H_S)(A)).

Finite-volume ground-state spectral decomposition gives

 F_(L,S),A(t)=int_[0,infinity) exp(itE) dmu_(L,S),A(E),
 mu_(L,S),A([0,infinity))=omega_(L,S)(A^dagger A).            (9)

Ground degeneracy is harmless; zero-energy transitions contribute at E=0.
The correlation converges at every fixed t to
F_A(t)=omega(A^dagger alpha_t^H(A)). To justify the off-diagonal passage,
use polarization into vector states obtained by C=I+zA, z in {1,-1,i,-i}.
For M>=M0 and each link in B_R, its high-flux projection Q_l obeys

 ||Q_l C psi|| <=(1+||A||)||Q_l psi||

when l is outside X, while Q_l A=0 inside X. Thus the same local tail
argument applies to these unnormalized states, with constants multiplied
by at most(1+||A||)^2. No gap, ground-state overlap or spectral-isolation
bound enters this step. Polarization recovers the mixed matrix elements;
local trace-norm convergence and locality finish the fixed-t limit.

For a smooth compactly supported test function of energy supported in
(-infinity,0), its inverse Fourier transform is integrable. Insert(9),
then pass the limit by dominated convergence using |F_(L,S),A(t)|<=||A||^2.
The limiting spectral measure therefore has no negative-energy support.
Its existence follows from positivity of the finite correlation matrices
and continuity at t=0 (local normality and strong dynamics continuity).
This is the spectral ground-state condition for all A in the displayed
local core.

For an arbitrary bounded local physical B, B_M=P_(X,M) B P_(X,M) is in
that core and converges strongly together with its adjoint to B. Local
normality gives ||(B-B_M)Omega||->0 in the GNS representation. Stationarity
bounds the difference of the two autocorrelations uniformly in t by
 [||B Omega||+||B_M Omega||]||(B-B_M)Omega||.
Thus the same nonnegative spectral support extends to every bounded local
physical B. The local vectors are dense by the GNS construction. In this
precise physical-observable sense omega is a rotor ground state.

#### 7. What the construction leaves open

These are genuine ground states of a supplied rotor Hamiltonian, obtained
as local limits of exact finite-link physical ground states. The argument
allows degeneracy and arbitrarily small many-body gaps. It improves the
previous prescribed-initial-state comparison by deriving its needed local
flux tightness and by passing the ground-state condition through the limit.
It does not prove uniqueness, purity, a photon pole, deconfinement, Weyl
quasiparticles, unbroken symmetry in pure phases, or a common metric.
A symmetry-averaged limiting state can mix symmetry-breaking pure states.

S must tend to infinity in this construction. A photon phase at a fixed
finite S still needs a long-distance estimate for that S. The local
compactness proof gives no such estimate and no uniform infrared window.
It also does not identify these supplied Hamiltonian states with a state
selected by the minimal framework's formation rules.

[Tong et al.](https://arxiv.org/pdf/2110.06942), Appendix H, Theorem12,
prove a stronger local tail for a spectrally isolated nondegenerate
finite-volume eigenstate. Their gap enters its quantitative bound.
Appendices H and I were read in full here. This argument uses an elementary
energy moment and local compactness for a different conclusion; it does
not remove the gap hypothesis from their polylogarithmic-precision theorem.
No general novelty is claimed for compactness of ground-state limits.

#### 8. Bounded verification and limits

The companion constructs the actual four-orbital onsite and CAR matrices.
A noncubic two-cell/two-link charged loop is built twice: once directly in
its Gauss basis and once by ambient tensor-product compression. Their
matrices agree. Its six cutoffs have36 through1154 physical states, and
the variational moment bound holds in each. The largest ground-eigenpair
residual is below4.8e-13. This fixture tests the charged Gauss algebra; it
is not a cubic bulk phase calculation.

A genuine four-edge pure-gauge plaquette checks the moment and exact
finite-electric-support commutator identity. An uncut shift at S=0
explicitly violates that equality, as expected: it leaves the cutoff.
The same-state finite-time comparison is challenged against a larger
finite matrix. Eight of its nine safe bounds cap at the trivial value2;
only one is nontrivial. These checks therefore provide weak numerical
coverage of the sharpness of(8). The proof of its volume independence
remains the analytic locality and tail argument, not a fit to that data.
No finite fixture establishes compactness or the infinite-volume phase.

See the personal N1-N8 review (`BLOCK12_ROUTE_AND_NO_GO_REVIEW.md`).

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK12_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK12_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Ground-state cutoff construction: personal N1-N8 review

The claim is positive and conditional on a supplied Hamiltonian. No
finite-link, gapless-ground-state or axiom no-go is claimed.

#### N1 — Actual routes

| Route family | Work done | Disposition |
|---|---|---|
| Physical variational state | Exact N=2 onsite minimum with E=0, then electric moment | ATTEMPTED; volume/cutoff-independent static moment |
| Local state compactness | Finite-rank projection, gentle bound, diagonal subsequence | ATTEMPTED; locally normal physical limits |
| Ground energy variation | Exact full/compressed commutator identity on a local core | ATTEMPTED; local stability survives the limit |
| Finite-time dynamics | Source locality bound plus derived state tail | ATTEMPTED; local stationarity passes to rotor limit |
| Excitation spectrum | Polarization and negative-energy test-function argument | ATTEMPTED; spectral ground condition, no gap assumed |
| Spectrally isolated eigenstate theorem | Tong et al. Appendix H read in full | ATTEMPTED hypothesis comparison; its stronger tail theorem has a gap hypothesis |

These are constructive steps, not a count of independent failed theories.
A fixed-S charged photon phase remains a different unresolved target.

#### N2 — Dependencies

Compactness, the core inequality and the spectral limit all use the same
electric moment. The spectral route also uses the finite-time parent.
They are two checks of ground-state status within one construction, not
independent phase evidence. The stronger fixed-S phase target cannot be
inferred from local limits with S growing.

#### N3 — Premises and hidden assumptions

CAR, graph, positive electric coefficients, bounded finite-range shifts,
Hamiltonian time, couplings and physical Gauss sector are supplied.
Translation averaging is essential to extract a local moment from an
extensive variational inequality. The state need not be pure. Time-reversal
averaging does not exclude symmetry breaking in its pure components.
Fixed a,g,r,w and both L,S tending to infinity are explicit. Global
projection probabilities are never substituted for local tightness.
The off-cutoff part of Hpsi is not set to zero.

#### N4 — Source match

The finite-link parent gives bounded-shift propagation for prescribed
low-flux states. This note derives local moment control from actual
finite-link ground states and supplies the compactness/spectral passage.
Tong's Theorem12 assumes a simple isolated eigenvalue and proves a much
stronger quantitative tail; this note neither imports nor removes that
hypothesis. No earlier fixed-S phase result is treated as available.

#### N5 — Resolution

Per site: actual onsite four-band spectrum and N=2 trial. Per link:
electric second moment, high-flux tail and compression. Per finite block:
independently built charged Gauss matrices and a real four-edge plaquette.
Per spectral test: finite-electric-support physical operators, then strong
local extension using stationarity. Lattice wide: analytic local compactness,
locality and spectral positivity, with no numerical bulk photon certificate.
The nine dynamics fixtures give only one nontrivial numerical error bound;
this limitation is recorded in the note and is not hidden by PASS counts.

#### N6 — Surviving partial paths

A fixed finite S with a directly controlled charged Coulomb phase remains
live. Uniform long-distance correlation estimates could strengthen these
state limits. Pure phases, symmetry selection, the formed vacuum and a
native kinetic identification remain open. No added axiom is requested.

#### N7 — Steelman

A critic can accept every displayed compactness step and still correctly
object that the limiting state may be confining or symmetry mixed. The
construction alone does not determine either question. Its value is to
construct actual physical ground states without requiring a gap, and to
state which extra long-distance estimate is missing. It is not evidence
that the desired phase already exists at any fixed cutoff.

#### N8 — Prior comparison

The current source distinguished low-flux dynamics from ground states.
The new delta is the explicit actual-carrier variational moment and the
joint volume/cutoff passage, including a spectral ground-state proof.
General compactness and ground-state-limit methods are established
machinery. No broad novelty or independent retained status is claimed.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: ground_cutoff_check_2026_09_15](../scripts/ground_cutoff_check_2026_09_15.py); [current cache](../logs/runner-cache/ground_cutoff_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
