---
claim_id: exact_gauss_reduction_and_fixed_volume_weak_coupling_spectrum_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For a supplied finite charged integer-link Hamiltonian on a fixed contractible cubical box, derive exact affine-integer Gauss coordinates and the weak-coupling fixed-index spectral limit. Primitive plaquette generation gives an oscillator plus the supplied fixed-number free CAR Hamiltonian; finite scaled flux cutoff gives a Dirichlet boundary. The theorem does not establish the thermodynamic charged photon/Weyl phase, a common interacting cone, Hamiltonian selection or an axiom update."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/exact_gauss_reduction_and_fixed_volume_weak_coupling_spectrum_2026_09_13.py
---

# Exact Gauss reduction and a fixed-volume weak-coupling spectrum

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

An exact reduction of Gauss law retains the charged, non-product flux domain.
In a fixed finite contractible box, the low spectrum of the supplied hard-link
Hamiltonian converges, as g tends to zero, to gauge oscillators plus the
supplied free matter spectrum in a fixed total-number sector. A cutoff with
finite gS retains a Dirichlet flux boundary; allowing gS to diverge removes it.
The proof below uses integer generation, quadratic forms and compactness.
Finite spectra challenge its hypotheses and coefficients but do not replace it.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Gauss isometry, positive weighted electric decomposition, fixed-graph spectral form limit and finite-boundary discriminator."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Obtain a physical low-energy spectral comparator for a charged finite-link candidate, beyond a small plaquette expectation."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Control volume dependence, harmonic holonomies, interacting charged correlations and compact defects; the thermodynamic phase remains open."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) supplies ontology
context. The [edge matter construction](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
and [current integer-link source](THE_FERMION_ON_COMPACT_U1_LINKS_THE_INTEGER_FLUX_SELECTS_THE_STAGGERED_GAUSS_LAW_AND_JOINS_THE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
identify comparison domains. The graph, CAR realization, charges, Hamiltonian
time and coefficients remain supplied. This source redeclares its complete
Hamiltonian; no unmerged campaign note is a theorem premise. No axiom, approved
primitive, state formation rule or audit verdict is changed.

Maximal-tree reduction and lattice continuum comparisons are established
mathematical methods. [Horn and Weinstein](https://www.slac.stanford.edu/pubs/slacpubs/2750/slac-pub-2864.pdf),
section 2 and sections 3.2-3.4, provide gauge-Hamiltonian and projected-flow
context. [Nakamura and Tadano](https://arxiv.org/pdf/1903.10656), section 1,
state a norm-resolvent continuum theorem for square-lattice Schrodinger
operators under specified potential and embedding hypotheses. That theorem
is not invoked for the charge-dependent domains and primitive multishifts
here. The fixed-index form argument below supplies its own hypotheses and
does not claim their norm-resolvent rate or a new general continuum principle.


Working bounded theorem. The graph, even-CAR realization, Hamiltonian time,
charges and couplings are supplied. The result is at fixed finite volume and
does not establish an interacting thermodynamic photon/Weyl phase.

## Domain and exact integer coordinates

Take a fixed connected contractible finite cubical complex with at least one
plaquette, such as an open rectangular cubic box. Let D be the oriented
vertex-by-link incidence matrix, F the oriented link-by-plaquette boundary
matrix, and c=number_of_links-number_of_vertices+1. All elementary plaquettes
are included. Contractibility implies H_1=0 over the integers, so
im_Z F=ker D intersect Z^links. This integer statement is stronger than a
real-rank condition.

Put a finite number of CAR orbitals at each vertex, integer reference charges
eta_x, and restrict matter to total number sum_x eta_x. The concrete carrier
has four orbitals, eta_x=2 and the mixed nearest-neighbor coefficients stated
below. The Gauss law is D E=rho, rho_x=N_x-eta_x. All electric components
commute with matter number operators. The hard cutoff is |E_l|<=S, with
unit-amplitude compressed shifts.

Choose a root and a spanning tree. There is an integer tree-flow matrix R,
zero on chord rows, satisfying D R=I-e_root 1^T. For each chord j let e_j be
its link unit vector and define C_j=e_j-R D e_j. Then

```text
D C=0,             C restricted to chord rows=I_c,
E=R rho+C n,       n in Z^c,
F=C Z,             Z=F restricted to chord rows.
```

The first line makes C an integer basis of the full cycle lattice: subtracting
C times a divergence-free field's chord coordinates leaves a divergence-free
field supported on a tree, which must vanish by removing tree leaves. The
same argument proves the unique affine representation of every physical E.
The columns z_p of Z generate Z^c because the plaquettes generate all integer
cycles. No extra topological sectors or finite-index sublattices are discarded.

In a matter occupation basis f, set E0(f)=R rho_f. The map
|f,n> -> |f,E0(f)+C n> is an exact isometry onto the untruncated neutral
physical Hilbert space. At finite cutoff its allowed labels satisfy

```text
|E0(f)+C n|_infinity <= S.                                   (1)
```

This domain couples matter and flux; it is not replaced by a product cutoff.
An onsite number-preserving orbital term leaves rho unchanged. A hopping
c_x^dag U_l c_y changes rho by D e_l and E by e_l, hence changes n by zero
for a tree link and by the corresponding unit vector for a chord. A plaquette
changes n by z_p. These are exact statements including occupation-basis CAR
signs. They are a maximal-tree coordinate representation, not a proposed
physical gate or autonomous preparation law.

## Exact longitudinal energy and its interpretation

Let W_E be the positive diagonal electric weight matrix and
L=D W_E^(-1) D^T. On the neutral charge sector define

```text
E_L=W_E^(-1) D^T L^+ rho,       E_T=E-E_L,
D E_T=0,                        C^T W_E E_L=0,
E^T W_E E=E_T^T W_E E_T+rho^T L^+rho.                         (2)
```

Here L^+ is the pseudoinverse with the constant mode removed. The identity
follows directly from D E=rho and the weighted orthogonal projection; all
operators in it commute. E_L generally has noninteger eigenvalues, so (2)
does not replace the affine integer flux lattice by freely adjustable real
longitudinal and transverse fields. The residual lattice and cutoff in (1)
remain exact.

For electric energy g^2 E^T W_E E/(2a), (2) isolates an exact positive
Coulomb-kernel term g^2 rho^T L^+rho/(2a). This is a contribution to the
Hamiltonian, not a theorem that the full static charged potential is
Coulombic: the transverse and magnetic sectors can still add confining
energy. No monopole or charge gap is inferred from a graph Green function.

## The finite Hamiltonian in cycle coordinates

One supplied four-orbital specialization, with sigma acting on orbital and
tau on flavor, uses 0<b<pi/2, 1/2<zeta<1, 0<mu^2<1-zeta^2 and

```text
h_on=(2+zeta)sigma3+mu tau_x(sin b sigma1+cos b sigma3),
T_i=(C_i-i S_i)/2,
C_x=-sin b sigma1-cos b sigma3, S_x=tau_z(cos b sigma1-sin b sigma3),
C_y=C_z=-sigma3,                 S_y=sigma2, S_z=0,
H_matter=(r/a)[sum_x c_x^dag h_on c_x
       +sum_(oriented links x,i)(c_x^dag T_i U_(x,i)c_(x+i)+h.c.)],
r>=0, a>0.
```

All graph directions and comparator coefficients are supplied. The theorem
below also applies to other fixed, number-preserving onsite and hopping
matrices on this finite graph. It requires their boundedness, not a presumed
Weyl or photon phase. Open boundaries do not have a Bloch-node spectrum.

Let W_B be the positive diagonal plaquette weight matrix. Use the positive
magnetic convention and fixed bounded hopping/onsite coefficients:

```text
H_g,S = (g^2/(2a)) E^T W_E E
      + (1/(g^2 a)) sum_p (W_B)_p [1-Re shift_(z_p)]
      + H_matter(tree links=I, chord j=shift_(e_j)),
```

compressed to (1). A term crossing its boundary is omitted while the magnetic
identity term is retained. This distinction will give a Dirichlet boundary,
not a reflecting discrete boundary. H_matter is bounded uniformly in g,S at
this fixed graph, by the sum of finite CAR hopping and onsite norms.

Set x=g n and identify lattice amplitudes with piecewise constant functions
on the cells g(n+[-1/2,1/2)^c), multiplying amplitudes by g^(-c/2). This is an
isometry into L^2(R^c) tensor the finite neutral matter space. Wavefunctions
are extended by zero outside their charge-dependent allowed domains.

Suppose g tends to zero and gS tends to s in (0,infinity], with all graph and
Hamiltonian coefficients fixed. Define

```text
Omega_s={x: |C x|_infinity<s} for finite s; Omega_infinity=R^c,
A=Z W_B Z^T>0,                   K=C^T W_E C>0,
H_osc,s=[-partial^T A partial+x^T K x]/(2a)
```

on H_0^1(Omega_s) for finite s and the confining full-space quadratic-form
domain for infinite s. The limiting charged Hamiltonian is

```text
H_limit,s=H_osc,s tensor I + I tensor H_free,matter,           (3)
```

where H_free,matter is the original finite CAR Hamiltonian with every link
comparator set to identity, restricted to the fixed total-number sector.
Equation (3) is a statement in the exact Gauss-reduced coordinates. It does
not assert that an undressed free Slater state is a physical product state
in the original link/matter variables.

## Fixed-index spectral convergence: form proof

The following argument establishes convergence of each fixed-index eigenvalue
and the associated isolated spectral clusters under the stated embeddings.
It also specifies where fixed volume is used.

1. **Recovery on a common core.** For a smooth compactly supported vector
function u in Omega_s, sample each matter component on gZ^c. Because the
matter space is finite, max_f |E0(f)| is finite. Its g-scaled offsets vanish,
so the sampled support is inside every relevant domain (1) for sufficiently
small g. Riemann sums give its norm limit. The electric potential converges
to x^T K x/(2a). Each plaquette difference divided by g converges to
z_p dot partial u. Each bounded matter translation by g e_j tends to identity.
Thus the sampled quadratic forms converge to that of (3). Smooth compact
functions are a form core, including for the convex bounded polytope Omega_s.

2. **Discrete derivative control.** The magnetic form of a zero-extended
amplitude is exactly

```text
(1/(2g^2 a)) sum_p (W_B)_p ||T_(g z_p)u-u||^2.               (4)
```

Integer generation is essential. Express every coordinate unit vector as an
integer sum of the z_p. Telescoping the corresponding commuting translations,
and applying the triangle inequality, bounds each nearest-coordinate
difference quotient by a fixed linear combination of those in (4). The
constants depend on this graph but not on g or S. Piecewise multilinear
interpolation therefore has a bounded H^1 norm whenever (4) and the norm are
bounded; its L^2 difference from the piecewise constant embedding tends to
zero. These statements follow cell by cell from the edge differences.

3. **Compactness and lower bound.** An upper bound on total energy gives
bounds on the positive gauge terms because H_matter has a uniform lower
bound at this fixed graph. Since C has full column rank, the electric term
also bounds the second moment in x; its gE0(f) offset changes this only by
uniformly vanishing/lower-order terms. The interpolants are therefore
precompact in L^2: apply Rellich on a fixed ball and bound the outside norm
by its second moment. A weak derivative limit of each quotient in (4) is
z_p dot partial u, which gives the lower semicontinuity bound. The limiting
function is zero outside the closure of Omega_s; for this Lipschitz polytope
its full-space H^1 zero extension is equivalent to the Dirichlet form domain.
The shifted cutoff boundaries thus produce H_0^1, not Neumann data. Truncation
of the quadratic potential on larger balls gives its lower bound. Strong L^2
convergence makes the bounded translated matter forms converge to the free
matter form.

4. **Min-max conclusion.** Sampling a finite-dimensional span of smooth
approximations to the first limit eigenfunctions gives the eigenvalue upper
bounds. Compactness of any finite collection of low discrete eigenvectors,
retention of their orthonormality and the lower-form bound give the matching
lower bounds. The limit oscillator is confining (or on a bounded domain),
so it has compact resolvent. These arguments also identify subsequential
limits of eigenvectors and the isolated finite-dimensional spectral
subspaces. Degenerate levels are handled as clusters, not by claiming a
preferred basis of individual eigenvectors. This is fixed-index convergence;
no uniform bound over all energies or growing volume is asserted.

For s=infinity the frequencies of H_osc are

```text
omega_j=sqrt(lambda_j(A^(1/2) K A^(1/2)))/a,
E_gauge,0=(1/(2a)) Tr sqrt(A^(1/2) K A^(1/2)).                (5)
```

These are the nonzero weighted curl frequencies: the nonzero eigenvalues of
W_E^(1/2) F W_B F^T W_E^(1/2) are the same as those in (5). Matter energies
add to the oscillator energies in the limiting fixed-number sector. The
result supplies a genuine finite-volume low-energy comparator, rather than
only a small classical magnetic curvature.

## Why integer generation and boundary topology matter

A real-rank test alone would be insufficient. On one flux integer, a magnetic
shift by two has positive real quadratic symbol, but the even and odd integer
sublattices never communicate. With electric term 2g^2 n^2, each sublattice
converges to -2 d^2/dx^2+2x^2, whose ground energy is 2; the full model has two
copies in the limit. Replacing primitive generation by real span would miss
that multiplicity. Ordinary plaquettes of the stated contractible complex
generate the full integer cycle lattice, so this counterexample is excluded
by a checked hypothesis rather than by an assumed continuum identification.

A periodic three-dimensional box also changes the argument: it has three
harmonic flux directions beyond the plaquette boundary span. Flat holonomies
and mobile matter require separate treatment. The positive-definite oscillator
and compactness proof above cannot simply be copied to that periodic domain.
The open contractible box is a declared domain choice; it does not erase the
periodic model's global modes.

## One-plaquette boundary and Gaussian-accuracy discriminator

For one isolated plaquette, set a=1, take C=(1,1,1,1)^T and unit weights. Then A=1,
K=4 and the limiting gauge operator is

```text
H_s=-1/2 d^2/dx^2+2x^2,     |x|<s, Dirichlet,
H_infinity ground energy=1, phi_0(x)=(2/pi)^(1/4) exp(-x^2).
```

Every finite s gives E_0(s)>1: equality in the full-line Rayleigh bound would
require the full Gaussian, which is not supported in the finite interval.
This is also a state statement independent of energy-zero conventions: the
squared overlap of any normalized interval-supported state with phi_0 is at
most 1-erfc(sqrt(2)s). A fixed finite value of gS therefore cannot recover the
full Gaussian vacuum with arbitrarily small error, even though it can give
an O(g^2) plaquette deficit.

For s>=2 the full oscillator gap and a tent cutoff of phi_0 give explicit
bounds on the box energy error:

```text
2 erfc(sqrt(2)s) <= E_0(s)-1
 <= [sqrt(2/pi)/erf(sqrt(2))] exp[-2(s-1)^2].                 (6)
```

For the lower bound, expand a normalized box state in full-line oscillator
levels. Its squared overlap with the ground state is at most the Gaussian
mass inside the interval, and the next full-line level is two higher. For
the upper bound, multiply phi_0 by a function equal to one on |x|<=s-1,
linear down to zero on the remaining unit intervals, and zero outside.
The ground-state transform gives an excess numerator (1/2) integral
|eta'|^2 |phi_0|^2. Bound that numerator by sqrt(2/pi) exp[-2(s-1)^2] and its
norm denominator below by erf(sqrt(2)). No fitted spectrum enters (6).

The even eigenfunction can also be written as exp(-x^2)u(x). Its series obeys
u''-4xu'+2(E-1)u=0, u(0)=1,u'(0)=0. The coefficient recurrence is

```text
a_(n+1)=[4n-(E-1)] a_n/[(n+1)(2n+1)],
u(x)={}_1F_1((1-E)/4;1/2;2x^2).
```

The first zero of u(s) yields E_0(s). This is used as one check of finite-
difference spectra, not as the proof of (6). The bounds imply that the scaled
cutoff needed for small box-energy error has order sqrt(log(1/epsilon)); a
Gaussian-tail integral supplies the corresponding lower order. Combining
that with S approximately s/g is an iterated weak-coupling/accuracy statement.
No uniform joint finite-g error rate or volume-uniform spectral estimate is
claimed here.

## Remaining phase task

The finite-volume spectrum separates into gauge oscillators and the free
neutral-number CAR sector only in the stated weak-coupling limit. At fixed
g>0, the charged interactions, large-volume soft modes, compact defects and
possible ordering still require control. The constants in the compactness
and integer-path arguments depend on the graph, and the smallest oscillator
frequency softens when the box grows. Neither the min-max argument nor the
exact Coulomb-kernel contribution establishes a thermodynamic charged photon,
an isolated charged-particle pole, common-cone attraction or framework
selection of the Hamiltonian. Those limits and observables remain explicit
proof obligations rather than grounds for an axiom update.


## No-Go Discipline Gate

The negative statements delimit particular regulator, topology and inference
choices. This is a constructive finite-volume theorem with an open phase task,
not a general obstruction to finite-spin photons or the framework.

**N1 — Actual distinct attack routes.**

| Route | Mechanism and disposition | Marker |
|---|---|---|
| Integer cycle and charge coordinates | Exact rooted-tree flows retain all physical states and expose the affine cutoff; a product charge/flux cutoff is generally false. | ATTEMPTED |
| Weighted electric minimization | Orthogonal projection isolates a positive Coulomb kernel, while its fractional longitudinal field leaves an affine integer residual; the full charged potential is unproved. | ATTEMPTED |
| Discrete quadratic forms and compactness | Primitive plaquette generation, confining electric energy and min-max yield fixed-index convergence on a fixed contractible graph. Growing-volume constants remain uncontrolled. | ATTEMPTED |
| Dirichlet oscillator and Gaussian tails | Finite gS retains a demonstrably different vacuum. Increasing gS is a constructive escape within the same regulator family. | ATTEMPTED |
| Integer sublattice and homology countermodels | Doubled shifts preserve two copies; periodic cubes retain three harmonic directions. These disprove extensions obtained by dropping stated hypotheses. | ATTEMPTED |
| Direct physical matrix comparison | Full link-field enumeration and separate CAR matrices challenge the reduction and its signs on a charged cycle. This is a finite check, not a phase proof. | ATTEMPTED |

These are different mathematical objects and obligations. The procedural
route count is not exhaustive proof against unexamined phase constructions.

**N2 — Implication audit.** Let R be the exact reduction, S the fixed-graph
spectral convergence, P the interacting thermodynamic phase, and C the common
interacting cone. R is used to prove S here, but R alone imposes neither a
weak-coupling limit nor primitive magnetic generation. S does not prove P,
as it supplies no uniform growing-volume control. No converse P=>this R or S
is asserted for other encodings. P and C are separate target descriptions
whose logical equivalence or independence has not been established here.
No independent-wall count is assigned to these unresolved relations.

**N3 — Hidden-premise scan.** Contractibility is over the integers; all
elementary plaquettes and positive fixed weights are specified. Total charge
is neutral and the finite matter space is nonempty. Bounded matter couplings,
fixed graph, positive a, unit-amplitude shifts, retained magnetic identity
terms, the g-scaled embedding and the limiting cutoff are explicit. The
four-orbital model is a supplied specialization. Its free Bloch behavior is
not assumed in an open box, and its interacting thermodynamic spectrum is
not inferred. Classical gauge fixing is not a physical preparation gate.

**N4 — Residual matching.** The current integer-link source is used for
conditional construction context, not as an obstruction to every regulator.
Horn/Weinstein supplies method history, not this cutoff-dependent spectral
theorem. Nakamura/Tadano section 1 concerns a different embedding and scalar
square-lattice operator: it is contextual rather than a substituted proof
of the charged moving-domain claim. No historical no-go is imported as a
witness against the full target.

**N5 — Resolution audit.** Per element, exact weighted projections and
integer link displacements are checked. Per site, direct CAR actions and
Gauss neutrality are checked. Per mode, Dirichlet oscillator coefficients,
Gaussian bounds and nonprimitive copies are checked. Per block, open-box
integer generation and the direct charged-cycle matrix are checked.
Lattice wide, the theorem quantifies over each fixed finite contractible
box; a periodic rank comparator is checked. The thermodynamic spectrum,
charged poles and common interacting cone are not tested or established.

**N6 — Partial closure and conventions.** The affine-coordinate isometry
and finite-volume spectral comparator close a supplied-model obligation.
Changing the vacuum energy zero cannot remove the missing Gaussian mass
at fixed finite gS. Allowing gS to diverge is an explicit same-family escape;
finite-spin encodings or other observables can have different requirements.
None of these choices automatically introduces a framework axiom.

**N7 — Steelman.** The strongest positive reading is that exact Gauss
dressing is compatible with a weak-coupling physical spectrum whose finite
levels approach oscillator and matter sums. It motivates, rather than proves,
a stable charged Coulomb phase. A successful uniform correlation/RG argument
or an independent finite-spin construction could settle a broader target
without contradicting the boundary or topology counterexamples.

**N8 — Cross-cycle echo.** Earlier campaign work controlled finite-time
truncation and ground-state plaquette/angle statistics. The new terminal
object is the physical finite-volume spectrum with exact charge dressing.
The remaining phase gap is not counted again as a new axiom deficit.
Periodic holonomies and growing-volume control are the next research targets.

## Author checks and verification limits

The runner independently enumerates all four-link electric fields satisfying
Gauss law and builds separate CAR matrices, then compares the complete charged
Hamiltonian with the cycle-coordinate matrix at S=1,2. This fixture has one
orbital per site, two particles and eta=(0,1,0,1); it is explicitly smaller
than the supplied four-orbital three-dimensional carrier. Open cubical boxes
check exact incidence, rooted-tree cycles and Smith invariants. Weighted
oscillator frequencies are compared against the direct curl matrix, including
the open cube frequencies (2,2,2,sqrt(6),sqrt(6))/a.

The one-plaquette hypergeometric boundary reference is compared with an
independent continuum finite-difference matrix. Finite hard-link charged
spectra approach both the finite-boundary targets and, when gS grows, the
first four full-space oscillator/matter sums. A doubled-shift model retains
two low clusters. Exact symbolic substitution checks the even ODE recurrence.
These finite checks do not certify compactness, arbitrary graph size, a
joint error rate or the thermodynamic phase; those claims stand or fall with
their actual proofs and stated limitations.

Raw exploration, source history, canonical execution and deliberate
wrong-formula checks are preserved in the branch packet. All execution and
source review in this campaign were personal author work. Independent review,
full integrated validation and formal audit remain pending; no retained
status is granted by the author checks.
