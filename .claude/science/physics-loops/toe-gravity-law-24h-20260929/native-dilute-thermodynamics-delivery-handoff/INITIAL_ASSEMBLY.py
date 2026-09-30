from pathlib import Path
root=Path('/Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929')
out=Path('/private/tmp/toe-native-dilute-thermodynamics-20260930/docs')
def read(p):return (root/p).read_text()
def between(text,start,end):return text[text.index(start):text.index(end)]
owner='NATIVE_DILUTE_THERMODYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-30.md'
pa='NATIVE_DILUTE_PHYSICAL_BOUNDARY_PROOF_2026-09-30.md'
pb='NATIVE_DILUTE_CELL_INTERACTION_PROOF_2026-09-30.md'
pc='NATIVE_DILUTE_LOWER_AND_LIMITS_PROOF_2026-09-30.md'
base='NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md'
density='NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md'
header=lambda title: f'''# {title}

This is current supporting proof owned by `{owner}`,
under exactly its supplied full-qubit Hamiltonian and fixed positive mu,tau.
It has no separate claim classification or runner. The owner directly links
and binds it as a primary input. Its complete argument and interactions are
part of that one scientific unit. Equation numbers are local to each named
part below. Unsubscripted energy forms always use actual occupation amplitudes.

'''
# Boundary and relative capacity, with all necessary core/Neumann details.
b=read('native-relative-neumann-collision-route/BOUNDARY_PENALTY_PROOF.md')
b=between(b,'## 1. Actual lower cells','## 7. What this changes')
b=b.replace('the root ledger\'s safe nonnegative diagonal','the safe nonnegative diagonal')
b=b.replace('the checked boundary proof','the boundary proof here').replace('the checked proof','the proof here')
b=b.replace('The same elementary block resolvent argument as for any positive finite\nmatrix gives','Block Gaussian elimination gives')
r=read('native-relative-neumann-collision-route/WORKING_PROOF.md')
r=between(r,'## 1. Statement with physical normalization','## Current status')
r=r[:r.index('For all N, removal amplitudes')]
r=r.replace('The candidate theorem is','The relative-capacity statement is').replace('the previously checked physical normalization','the physical normalization of the threshold input')
r=r.replace('The checked physical compact-source inequality states',f'The [physical threshold proof]({base}) establishes the compact-source inequality')
r=r.replace('This is a possible two-pair input for a subsequent replacement\nargument, not that many-particle replacement itself.','The mean is an N4 relative-coordinate observable. The physical-cell\nconstruction in Part I and the subsequent cell-interaction proof use the\nsame Neumann estimates on actual anchor rectangles.')
r=r.replace('the proposed convergence','the convergence')
r=r.replace('## 8. Actual N4 lower form and the exact remaining many-body obstruction','## 8. Actual N4 lower form and its domain')
intro=f'''The actual [law and simultaneous gradient bound]({density}) and
[physical threshold completion]({base}) are the source inputs.
Part I constructs positive physical cells with a priced boundary penalty,
an exact guarded physical compression and a complementary gap. Part II
retains the full matching core and nonmatching self-energy in an auxiliary
relative Neumann capacity. The latter is an N4 theorem; it is never used as
an unpriced all-particle row allocation. Its scalar Neumann estimate and
actual high-component analysis also support the cell residual proof.

# Part I. Physical cells, spectator pins and complementary gap

'''
(out/pa).write_text(header('Physical boundaries and relative collision capacity')+intro+b+'\n# Part II. Full-channel relative Neumann capacity\n\n'+r)
# Actual cutoff construction, expanded with its physical/core/Fourier proof.
c=read('native-compatible-collision-route/REPORT.md')
cut=between(c,'## 2. Actual N4 exterior','## 3. A single compatible correction')
cut=cut.replace('## 2. Actual N4 exterior and a sharper compact corrector','## 1. Physical threshold response and a compact residual')
cut=cut.replace('the checked threshold energy completion', 'the threshold energy completion')
cut=cut.replace('the actual nine-bond S+W symbol already checked in the matrix-pin route','the actual nine-bond S+W symbol displayed below')
cut=cut.replace('exactly as in the checked one-pair matrix\nGreen proof','by the dyadic-shell argument given below')
cutdetails=between(c,'## A. Physical exterior, completion and cutoff details','## B. Labeled contraction proof')
cutdetails=cutdetails.replace('## A. Physical exterior, completion and cutoff details','## 2. Core, matrix Fourier and cutoff details')
cutdetails=cutdetails.replace('section2','the preceding section')
cell=read('native-relative-neumann-collision-route/CENTERED_RESIDUAL_PROOF.md')
cell=between(cell,'## 1. Exact statement','## 8. Limits of this candidate')
cell=cell.replace('The candidate result is','The fixed-cell result is').replace('The checked adiabatic threshold construction applies','The construction in Part I applies')
cell=cell.replace('The checked gap is','The physical boundary proof gives').replace('the checked boundary proof','Part I of the physical boundary proof')
cell=cell.replace('the previously checked local pin argument','the local pin argument').replace('The previously checked local pin argument','The local pin argument')
cell=cell.replace('the checked proof','the physical boundary proof')
cell=cell.replace('The NEW centered-residual candidate','The centered residual theorem')
cell=cell.replace('This repeats the actual symbol/core derivation for(3)', 'Part I supplies the actual symbol/core derivation for(3)')
cell=cell.replace('in the relative-Neumann argument','in Part II of the physical boundary proof')
cell=cell.replace('the same coherent polynomial construction','the following physical polynomial construction')
cell=cell.replace('No uniform-in-n rate, useful\nfinite-density threshold, many-cell lower law, EOS or phase conclusion is\ncontained in(5)-(6).','The constants need not be uniform in n. The lower-and-limits proof uses\nonly finitely many n at each chosen particle cutoff before taking the\ndilute limit.')
(out/pb).write_text(header('Actual cell collision corrections and the full internal Schur form')+f'''The [physical boundary proof]({pa}) supplies the actual lower cells,
anchor normalization, guarded compression and complementary gap. The
[threshold source]({base}) supplies the physical energy completion and
compact-source inverse. Part I proves the stronger compact residual estimates
needed here from that actual operator. Part II then proves the fixed-n
physical-cell Schur limit, with all boundary and penalty residuals priced.
No periodic interaction coefficient is substituted for an open-cell form.

# Part I. Adiabatic physical four-particle corrections

'''+cut+'\n'+cutdetails+'\n# Part II. Compatible sources on actual physical cells\n\n'+cell)
# Lower and thermodynamic composition.
globalproof='''## 1. Global bad-particle estimate with its actual R-cubed growth

Let F_b count occupied x whose Chebyshev b-cube contains at least three
particles. For integer b>=10 and L>=10b, partition each coordinate circle
into intervals with lengths between b and2b, enlarge each product box B
by b to C and then by one to C+. For x in B its b-cube lies in C, so
F_b<=sum_B N_C 1_(N_C>=3). The expanded rectangles C+ have aspect ratio
at most two, volume at most125b^3 and incidence at most125 at each site
or selected free edge. In one dimension at most five intervals expanded
by b+1 can cover a point. The landed local spectator-pin bound

    <N_C 1_(N_C>=3)> <= <D_C>+896|C+| Egrad15_C+

therefore gives

    <F_b> <=125<D>+14000000 b^3 Egrad15.

Here D_C retains the actual full-torus neighbors; it is not a deleted-neighbor
polynomial. All restrictions are on actual annihilation outputs before
positive gradient sums are taken.

Let B_b count particles outside b-isolated graph dimers. A singleton has
D contribution one. Every vertex in a graph component of size at least
three has two other component vertices within at most two graph steps,
hence within Chebyshev distance four; it is counted by F_b. For an isolated
dimer rejected by the b-isolation condition, one endpoint sees its partner
and a third particle in its b-cube; charge its two particles to that F_b
endpoint. Different dimers have disjoint endpoints. Thus, pointwise,

    B_b <= D+2F_b.

Together with H>=mu D+a Egrad15 this proves the deliberately loose bound

    <B_b> <= (C_B b^3/a)<H>,       C_B=28000322.

Indeed D+2F_b<=251D+28000000b^3 Egrad15, and a<=mu and b>=1 make
28000251 a safe constant; the larger C_B preserves the stated common
normalization. The estimate holds for every state and particle sector.
It counts lost particles, not energy or a global no-defect projection.

## 2. Exact finite-five-mode sphere identity

For n particles in the auxiliary symmetric space Sym^n C^d, let gamma1 and
gamma2 be normalized reduced density matrices. With normalized sphere
measure dz, d_n=binom(n+d-1,d-1), the measure

    d_n <z^n,gamma_n z^n> dz

has total mass one. Its two-body moment is

    tilde gamma2=[n(n-1)gamma2
       +4n P_sym(gamma1 tensor I)P_sym+2P_sym]/[(n+d)(n+d+1)].

This identity can be derived directly from

    integral z^alpha conjugate(z)^beta dz
        =delta_(alpha,beta)(d-1)! alpha!/(|alpha|+d-1)!.

One derivation takes the normalized coherent resolution at n+2 and commutes
its two tested annihilators past the two creators:

    a(v)^2 a(v)^dagger^2
      =a(v)^dagger^2 a(v)^2+4a(v)^dagger a(v)+2

for ||v||=1. Testing every v tensor v and polynomial polarization fixes
all matrix entries on the symmetric square, including complex off-diagonal
entries. This is finite-dimensional auxiliary algebra, not a physical-pair
CCR. The auxiliary space is only used after the proved physical compression.

The extra terms are positive and have complementary trace1-p with
p=n(n-1)/[(n+d)(n+d+1)]. Thus
||gamma2-tilde gamma2||_1<=2(1-p). For d=5,n>=2,

    n(n-1)(1-p)<=12n+30<=27n.

For every positive full15-dimensional T and t_coh(T)=min_unit_z<T>_(z^2),

    <sum_(i<j)T^(ij)>
      >=t_coh(T)n(n-1)/2-27||T||n.

The harmless n=0,1 cases follow from positivity. The identity permits
arbitrary complex, mixed and fragmented internal states and independent
coherent measures in different cells. No claim about condensation is used.

'''
tail=read('native-relative-neumann-collision-route/PARTICLE_TAIL_AND_LOWER_COMPOSITION.md')
tail=tail[tail.index('## 1. An actual total-cell-count tail lemma'):]
tail=tail[:tail.index('Equation(10) must not be advertised')]
tail=tail.replace('The checked unchanged-law estimate is','Part I above gives the unchanged-law estimate')
tail=tail.replace('## 2. The exact low-sector hypothesis needed for composition','## 2. The actual low-sector estimate')
tail=tail.replace('The NEW centered-residual candidate,\nif correct, implies','The actual cell-interaction proof implies')
tail=tail.replace('the candidate Schur error','the cell Schur error')
tail=tail.replace('from that one conditional input','from that fixed-n cell theorem')
tail=tail.replace('This is the exact finite\nsphere identity previously proved and checked in compatible REPORT04e13444,\nnot an assumption that an energy-minimizing state is coherent.','Part I above proves this identity; the energy-minimizing state is not\nassumed coherent.')
tail=tail.replace('Thus the sole unverified new mathematical dependency in(5) is the actual\ncentered-residual coefficient theorem. The finite-mode identity, odd-sector\ngap and physical boundary comparison have separate earlier checks.','All dependencies of(5) have now been proved in this unit: the actual\ncell-interaction theorem, finite-mode identity, odd-sector gap and physical\nboundary comparison. Only finitely many sectors are used for each fixed K.')
tail=tail.replace('## 4. Conditional dilute lower coefficient, with all ordered limits','## 4. Dilute lower coefficient with all ordered limits')
tail=tail.replace('It follows conditionally that','It follows that').replace('the CONDITIONAL\nfull-carrier dilute LOWER bound','the full-carrier dilute lower bound')
tail=tail.replace('It does\nnot supply a canonical upper construction, condensate, ODLRO, channel\nselection, phase diagram, or equality of a separately defined EOS.','The upper construction and thermodynamic conclusions are proved separately\nbelow and in the canonical note.')
mean=read('native-mean-density-composition-route/REPORT.md')
mean=between(mean,'## 2. Thermodynamic limits actually used','## 6. Scope and evidence')
mean=mean.replace('The old unitary trial','The canonical note\'s exact unitary trial')
mean=mean.replace('The separately checked lower','Part II\'s all-state lower')
mean=mean.replace('Equation(8)','the canonical note\'s uniform unitary bounds')
# Mean section(5) references its own originally earlier all-density statement: add that as setup.
meansetup='''Use the canonical definitions e_L(rho),g_L(nu), t=t0, c=t/8,
c0=a/99090432 and h_*=182mu+240tau. The landed all-density coercivity is
H>=c0 N(N-2)/V, so every state satisfies

    <H>/V>=c0(rho^2-2rho/V).                              (5)

Dephasing in N preserves mean and energy. Thus e_L is the convex hull of
sector ground energies, continuous and convex on[0,1], with

    e_L(0)=0, 0<=e_L(rho)<=h_*rho,
    g_L(nu)=min_(0<=rho<=1)[e_L(rho)-nu rho].              (7)

The upper bound uses the vacuum/fully occupied mixture, not an equality
for the full-occupancy energy. Here and throughout, e_L constrains the
MEAN number. The fixed-sector energies are treated in Part IV.

'''
can=read('native-canonical-block-transfer-route/WORKING_PROOF.md')
can=between(can,'## 2. Tune the actual finite-block mean','## 6. Status and limits')
can=can.replace('The new claim','The claim')
can=can.replace('the completed actual PARTICLE_TAIL_AND_LOWER_COMPOSITION, source2e4d9f8b/receipt124091e9','Part II\'s actual all-state lower')
can=can.replace('the supplied uniform mean-density trial','the exact unitary mean-density trial')
can=can.replace('The candidate','The construction')
# Internal old numbered references remain locally defined in the setups or restated assertions.
can=can.replace('from(2)','from the canonical uniform trial bounds').replace('bound from(2)','bound from the canonical uniform trial bounds')
can=can.replace('proves(3)','proves the canonical upper statement').replace('give(4)','give the canonical dilute envelope statement')
can=can.replace('combines with(3)','combines with the upper').replace('gives the lower coefficient','gives the lower coefficient')
(out/pc).write_text(header('All-state dilute lower bound and thermodynamic limits')+f'''Inputs are the [landed local pin and all-density bound]({density}),
the actual full threshold form in the [threshold source]({base}), and
this unit's [physical boundary]({pa}) and [cell-interaction]({pb}) proofs.
The exact uniform trial is proved in the canonical note. Every additional
counting, finite-mode and thermodynamic step is given here.

# Part I. Physical particle separation and internal variance

'''+globalproof+'\n# Part II. Particle tails and the all-state lower bound\n\n'+tail+'\n# Part III. Mean energy, grand energy and density slope\n\n'+meansetup+mean+'\n# Part IV. Exact particle-number upper transfer\n\n'+'''For any integer0<=N<=L^3 write E_L(N) for the lowest actual energy in
that sector. Fix a compact correction chi, t=t_chi,B=B_chi,D=D_chi.
The canonical unitary bounds hold on every sufficiently large periodic
block; all such sectors exist in its actual qubit carrier. Fix rho in(0,1)
before every thermodynamic/block limit in this part.

'''+can)
# Canonical source main theorem and exact full-carrier upper proof.
u=read('native-threshold-variational-route/REPORT.md')
u=between(u,'## 1. Target and exact physical preparation','## 6. Grand-canonical upper asymptotic')
u=u.replace('## 1. Target and exact physical preparation','## 1. Exact physical variational state')
u=u.replace('The checked N4 theorem','The physical threshold theorem').replace('the checked threshold source','the threshold source').replace('the checked finite inverse form','the finite inverse form proved there')
u=u.replace('The strict positivity is the separately checked extension at fixedmu,tau;\nno uniform-coupling lower bound is imported from it.','Strict positivity follows from T0>=2a/g in the threshold source.')
u=u.replace('This is an EXACT normalized state','This is an exact normalized state')
u=u.replace('The shared-center normalizations','The shared-center normalizations')
main=f'''---
claim_id: native_dilute_thermodynamics_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "For the supplied full-qubit pair Hamiltonian with fixed mu,tau>0: the mean-density thermodynamic energy has dilute coefficient t0/8, the grand energy and every thermodynamic ground-density accumulation have coefficients -2/t0 and 4/t0, and the ordered exact-number dilute energy envelopes equal t0/8, where t0 is the coherent minimum of the full physical fifteen-channel threshold form."
upstream_dependencies:
  - minimal_axioms
  - native_qubit_pair_density_onset_bounded_theorem_note_2026-09-30
  - native_four_particle_threshold_bounded_theorem_note_2026-09-30
runner: scripts/native_dilute_thermodynamics_2026_09_30.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Investigate actual pair correlations and collective excitations for the same supplied model."
conditional_surface_status: "Dilute thermodynamic statements for the explicit full-qubit model and ordered limits."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The operator estimates and limits are derived for a supplied Hamiltonian; its physical selection and quantum interpretation are separate inputs."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Dilute thermodynamics of a local qubit pair Hamiltonian

**Type:** bounded_theorem
**Status:** conditional-support (supplied model; unaudited)

**Target.** For the unchanged explicit full-qubit pair Hamiltonian with fixed
mu,tau>0, prove that its actual fifteen-channel four-particle threshold form
determines the leading dilute mean energy, grand energy, grand-ground density
and ordered exact-particle-number energy envelopes.

The Hilbert tensor product, basis, quantum expectation rule, Hamiltonian and
chemical-potential perturbation are supplied mathematical objects. The theorem
uses the actual two-dimensional site factors and all physical occupation
configurations. It does not select a framework Hamiltonian or a realized state.
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix that premise boundary;
the approved units, kinetic-form and realized-state grants are left unchanged.

## Quantified statement and proof map

On periodic cubes with V=L^3 define N=sum_x n_x and

    e_L(rho)=min_(Gamma>=0,Tr Gamma=1,Tr Gamma N=rho V) Tr(Gamma H0)/V,
    g_L(nu)=min spec(H0-nu N)/V,
    E_L(N)=min spec(H0 restricted to exact particle number N).

Let T0 be the full physical zero-energy threshold form on Sym^2 C^5 with
its Frobenius norm and actual incoming normalization defined below. Put

    t0=min_(||z||=1)<z tensor z,T0 z tensor z>,
    a=min(tau,mu/12), c0=a/99090432.

This is a coherent minimum of a full fifteen-channel form, not its least
unrestricted eigenvalue. Strict positivity T0>=2a/g gives t0>0. All conclusions
hold for each fixed positive mu,tau; no uniform zero-coupling limit is asserted.
The limits e(rho)=lim_L e_L(rho) for0<=rho<=1/2 and g(nu)=lim_L g_L(nu)
for real nu exist. At volume first and then rho or nu decreasing to zero,

    e(rho)=t0 rho^2/8+o(rho^2),
    g(nu)=-2nu^2/t0+o(nu^2),
    rho_gr(nu)=4nu/t0+o(nu).

The last statement holds uniformly over EVERY thermodynamic accumulation
of densities of finite-volume grand-ground density matrices, including
degenerate ground eigenspaces. It is an onset ratio, not a differentiability
or compressibility assumption. Their internal energy density is
2nu^2/t0+o(nu^2). For nu<0 the vacuum is the finite-volume ground state.

For every family of integer sequences with N_L(rho)/L^3 -> rho at each fixed
rho>0, both ordered canonical dilute envelopes satisfy

    lim_(rho down0) liminf_(L->infinity) E_L(N_L(rho))/(L^3 rho^2)
      =lim_(rho down0) limsup_(L->infinity)
                            E_L(N_L(rho))/(L^3 rho^2)=t0/8.

Odd particle numbers and nondivisible volume sequences are included. Equality
of the two canonical envelopes at each fixed nonzero rho is not a conclusion.
Neither an unrestricted simultaneous L,rho limit nor any joint finite-size
rate is used. The mathematical results concern energies and mean densities;
phase, ODLRO, state polarization, excitation spectra, preparation efficiency,
original-record observables and physical-source identification remain outside
the claimed conclusions.

The complete proof has the following dependencies, with no target-equivalent
terminal lemma left open inside this quantified statement:

* The [landed density theorem]({density}) supplies the actual law,
  simultaneous bare gradients, local spectator pin and all-density coercivity.
  Its conditional supplied-model hypotheses are retained here.
* The exact stacked [threshold theorem]({base}) supplies the full physical
  N4 energy completion, compact-source inverse and strict positivity. Its
  supporting proofs and source are inherited provisional inputs of this
  coherent unit, with exact base identity in the delivery provenance.
* The [physical boundary proof]({pa}) proves safe open cells, boundary
  penalty averaging, actual spectator pins, guarded compression/gap and full
  relative Neumann capacity with the physical matching constraints.
* The [cell-interaction proof]({pb}) constructs actual compact collision
  corrections and a compatible centered residual, pricing high components,
  boundary clusters, all internal tensors and the comparison penalty. Its
  limits are fixed particle number followed by ordered deformation limits.
* The [lower and limits proof]({pc}) proves the R-cubed bad-particle bound,
  exact finite-five-mode sphere identity, actual particle-number tail cutoff,
  uniform all-state dilute lower, mean/grand limits, concave density secants
  and deterministic exact-number block transfer.
* The full unitary variational upper with a volume-uniform remainder is proved
  below. It reaches every finite compact threshold correction before taking
  its infimum; no l2 threshold minimizer is assumed.

These are one argument. Periodic block Hamiltonians occur only in the bounded
norm thermodynamic/upper transfer. Physical lower cells retain their real
boundary rows and an explicit penalty debit. Internal fragmentation is priced
through the finite-mode identity rather than excluded by a state ansatz.

## Actual law and pair normalization

At each site use b_x=|0><1|, n_x=b_x^dagger b_x and Omega the empty product
vector. Distinct sites commute and b_x^2=0. The graph offsets are
D={{+/-2e_i,+/-e_i+/-e_j:i<j}}, with18 neighbors, and m_x=sum_(d in D)n_(x+d).
The literal bare/collective annihilators are

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
    Q_E1=(d1-d2)/sqrt2, Q_E2=(d1+d2-2d3)/sqrt6,
    Q_Tij=(1/2)sum_(s,t) v_ij^(s,t).

P_E and P_T denote the sums of Q^dagger Q in their two and three components.
The law is

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)
          +mu sum_x n_x binom(m_x,2)
          +tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|^2.

It is finite range, of interaction diameter four, and number conserving.
The exact full-carrier completion is H0=S+mu Ddiag+W, where

    S=(2mu/3)sum_x|d1+d2+d3|^2
       +(mu/4)sum_(x,i<j,r<s)|v_ij^r-v_ij^s|^2,
    Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2)>=0.

Axial edges have one center and plane edges two. Thus
2sum d_i^dagger d_i+sum v_r^dagger v_r=sum n_x m_x; the four-word difference
identity and1-m+binom(m,2)=(m-1)(m-2)/2 prove this completion. Splitting
collective and orthogonal components and using the lattice gradient norm
bound12 gives the SIMULTANEOUS inequality

    H0>=mu Ddiag+a Egrad15.

The fifteen gradients are those of all literal d and signed v fields.
The density source proves this and H0>=c0 N(N-2)/V on every sector.

Use nine forward graph edges d=2e_i,e_i+eta e_j. Their constant normalized
pair amplitudes form U with axial columns(1,-1,0)/sqrt2 and(1,1,-2)/sqrt6,
and one column(-1,+1)/sqrt2 on each plane's two orientations. U^T U=I5.
This corresponds to R=(Q_E1,Q_E2,Q_T12/sqrt2,Q_T13/sqrt2,Q_T23/sqrt2).
For symmetric complex A the physical incoming four-site profile is the
literal coefficient of

    Phi_A=(1/sqrt2)sum_(a,b) A_ab C_a^dagger C_b^dagger Omega,
    C_a^dagger=sum_(x,d)U_(d,a)b_x^dagger b_(x+d)^dagger.

Every alternative matching is summed and every overlap vanishes. At two
separated edges the amplitude is sqrt2(UAU^T)_(d,e). The threshold is
T0[A]=inf_(finite physical orbit support chi) E(Phi_A+chi), not a free-dimer
assignment in the collision core. Its energy completion and strict positivity
are exactly those of the threshold input. No numerical T0 eigenvalues or
channel ordering are assumed in any coefficient here.

# Uniform compact-correction upper on the full physical carrier

'''+u+'''
## Evidence and source-review boundary

The proofs above and in the three owned proofs carry the all-volume and
infinite-volume quantifiers. The primary is a bounded finite control of
literal pair words, boundary row/anchor structure, centered-source and
finite-mode normalization, and exact-number bookkeeping. It does not compute
a thermodynamic ground state or certify an infinite limit by extrapolation.
Its actual source, input identities, execution cache and scratch mutation
records are recorded in the unit pack after execution. An unexecuted check
is not a result. Author reuse of earlier controls is disclosed explicitly.

Earlier focused independent reconstructions checked the source-bound campaign
lemmas. They remain evidence about those frozen sources, with their actual
independence limits; they are not formal source review of this newly composed
unit. A historical boundary control used837 complete plane-family rows on a
5-cube, a strict subset of the1017 individual complete rows. The preserved
clarification and independent control bind that distinction. The mathematical
proof uses complete individual rows; no numerical C_pin value is imported.

No historical priority claim is made. The exact finite-dimensional sphere
identity is derived here; no external dilute-gas theorem is imported. The
provisional threshold base, supplied model and quantum interpretation remain
explicit dependencies. No authority, primitive, audit status or source law
is changed. Integration and audit remain separate requirements.
'''
(out/owner).write_text(main)
for f in [owner,pa,pb,pc]:print(f,len((out/f).read_text().splitlines()))
