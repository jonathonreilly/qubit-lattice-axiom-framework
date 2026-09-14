# Local finite-clock tensor constraints and the linear-gravity boundary

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author-proposed conditional mathematics; actual source status conditional-support.
Independent scientific review is pending. No interacting gravitational phase,
physical source identification or axiom contradiction is established.

A supplied local finite-clock Hamiltonian has exact commuting vector and scalar
constraints and an invariant sector. Its constrained quadratic symbol has two
cubic-dispersion tensor modes. A quantitative character bound shows why regular
local compact dynamics with both lifted gauge symmetries cannot supply a linear
mode. The spatially local noncompact linear-gravity comparator escapes that
hypothesis, but finite quadratic penalties leave an indefinite scalar block.
An independent source comparison distinguishes contact energy from the
attractive inverse-Laplacian kernel. These statements concern explicit models
and their declared approximation domains.

**Runner:** [self-contained primary](../scripts/local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_2026_09_14.py).
**Receipt:** [canonical cache](../logs/runner-cache/local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_2026_09_14.txt).
**Review:** [author record](../.claude/science/physics-loops/toe-charged-phase-20260914/deliveries/block5/REVIEW_HISTORY.md).

## Premises and precise scope

| Supplied data | Bounded result | Remaining obligation |
|---|---|---|
| N-level site/face slots, explicit integer stencils, positive couplings | Exact finite local Hamiltonian and invariant modular constraint sector | Native one-qubit law and selected ground-state phase |
| Canonical noncompact tensor comparator at nonzero momentum | Two TT pairs and the displayed cubic or linear dispersion | Physical quantum geometry and matter coupling |
| Lifted compact characters, fixed nonsingular canonical structure and summable spatial moments | Every small-field frequency is O(k^3) | Nonlinear, singular or nonlocal escape mechanisms remain open |
| Finite quadratic penalties on the specified linear comparator | Negative scalar kinetic determinant and a nilpotent Hamilton matrix | Full finite-clock dynamics is not decided by this Gaussian failure |
| Prescribed neutral scalar sources and isotropic quadratic energies | Exact contact or inverse-Laplacian energy difference | Actual finite-clock defect and mobile matter source map |

Take J,g,U_v,U_s>0 and integer N>=2. Continuum fields are real symmetric
three-tensors; plane-wave claims have k!=0. On periodic boxes remove zero modes
when taking inverses and require zero total scalar source. In R^3 use smooth,
neutral, rapidly decreasing sources; distributions with divergent self-energy
are not silently included. All finite-volume norm bounds retain their volume.

The current minimal axioms and three approved primitives are context. They do
not supply these tensor pairs, constraints, Hamiltonian, source or phase. No
unmerged campaign result is a scientific premise of this pair. The standard
continuum tensor comparators have prior art in Gu-Wen; the lattice formulas,
regularity bound and source calculations below are explicit and independently
challenged within the author work. No claim of literature priority is made.

## Canonical tensor comparators and physical reduction

Take symmetric real h_ij,E_ij on R^3 with canonical pairing integral E:hdot.
This is supplied phase-space data. Let
 G_j=partial_i E_ij,
 R_ij(h)=epsilon_iab epsilon_jcd partial_a partial_c h_bd,
 S=tr R=Delta tr h-partial_i partial_j h_ij,
 C_ij(E)=epsilon_iab partial_a(E_bj-delta_bj tr E/2).
The vector and scalar constraints G=0,S=0 Poisson commute. Their transformations
are h->h+sym gradient alpha (an overall factor convention is immaterial) and
E->E+(Delta I-Hessian) beta. R is vector-gauge invariant, and C is invariant
under the scalar transformation. R is symmetric and divergence free; on G=0,
C has the symmetry properties needed by the physical reduction.

For nonzero k, imposing G removes three momentum components and quotienting
its gauge transformations removes three h components. Imposing S removes the
remaining transverse scalar h component and quotienting its gauge removes the
transverse scalar E component. Exactly two canonical TT pairs remain. This is
a constrained noncompact construction, not a theorem that a finite qubit phase
realizes the constraints.

The strongly gauge-invariant positive Hamiltonian
 H_L=J/2 integral |C(E)|^2+g/2 integral |R(h)|^2
restricts to J k^2 |E_TT|^2/2+g k^4 |h_TT|^2/2. Hence omega^2=Jg k^6.
The weakly gauge-invariant linearized gravity comparator
 H_N=J/2 integral [E:E-(tr E)^2/2]+g/2 integral h:R(h)
restricts to J |E_TT|^2/2+g k^2 |h_TT|^2/2, giving omega^2=Jg k^2.
Its momentum term is scalar-gauge invariant only on G=0; its spatial density
is vector-gauge invariant after integration by parts. These distinctions matter
when exponentiating finite local clock operators and replacing constraints by
finite energy penalties. The boundary variation of a density does not make
the Hamiltonian spatially nonlocal; H_N has local support. Its polynomial
energy is not a periodic function of each local compact coordinate: shifting
one h component by its compact period changes its cross terms with neighboring
curvature. Its existence therefore does not contradict the compact-character
bound below. A periodic replacement must be checked as its own Hamiltonian.

## Integer clock constraint complex

Put three diagonal canonical pairs on each site and one off-diagonal pair on
each ij face. Use q=(h_xx,h_yy,h_zz,2h_xy,2h_yz,2h_xz) and
p=(E_xx,E_yy,E_zz,E_xy,E_yz,E_xz), so sum p dq is the tensor pairing.
In the basis |n>, n=0,...,N-1, define X|n>=omega^n|n> and
Z|n>=|n+1 mod N>, omega=e^(2 pi i/N). Thus XZ=omega ZX.
The notation Z=e^(i q), X=e^(2 pi i p/N) refers to these unitary generators;
an exact bounded canonical commutator is not asserted for finite N.

For the j edge based at x, define the integer incidence
 (G p)_j(x)=p_jj(x+e_j)-p_jj(x)
            +sum_(i!=j)[p_ij(x)-p_ij(x-e_i)].
At site x define
 (S q)(x)=sum_j sum_(i!=j)[q_jj(x+e_i)+q_jj(x-e_i)-2q_jj(x)]
 -sum_(i<j)[q_ij(x)-q_ij(x-e_i)-q_ij(x-e_j)+q_ij(x-e_i-e_j)].
Here an off-diagonal q_ij is the canonical doubled component. Then G S^T=0
as an integer local-stencil identity. The commuting stabilizers X^(G_row)
and Z^(S_row) admit the joint +1 sector. Their product projector is nonzero:
start in the p=0 vector-constraint state and average the scalar stabilizers;
the zero identity term has positive overlap, so the averaged vector is nonzero.
This gives a finite Hilbert space with exact modular constraints, not a
proof of a gapless phase.

The rows have absolute coefficient sums at most 6 for G and 36 for S.
A Weyl character with each integer exponent at most M in magnitude and
zero modular syndrome therefore has exact zero integer syndrome if N>36M.
At finite perturbative order n built from exponent-bound M bare characters,
the unreduced word exponents are at most nM. N>36nM suffices for each returning
word to lift. This is an algebraic statement about words; it does not assume
a uniform-in-volume convergence theorem for a perturbative effective Hamiltonian.

For the commuting positive penalty H0=sum_a u_a(1-Re W_a), a word acting on
the zero-syndrome sector has energy determined by its syndrome alone. Thus
finite-volume resolvent expansion matrix elements between two zero-syndrome
states are sums of returning Weyl words with scalar energy denominators.
Every surviving word commutes with the constraints. Where the effective terms
also have a controlled local/moment expansion, the derivative-order result
applies. Global convergence and uniform locality need their own proof; neither
follows merely from a finite stabilizer gap or a finite-order return-word list.

A literature check of Bravyi-DiVincenzo-Loss 1105.0675 finds that its displayed
many-body linked-cluster theorem assumes a product low-energy subspace. The
present stabilizer code does not have that hypothesis. Do not import that
specific theorem unmodified to declare uniform perturbative control here.

## A bounded local finite-clock Hamiltonian

The integer constraint complex admits actual local dynamics. Define R2 to map
the canonical q slots to 2R(h), and C2 to map p=E to 2C(E). A fully explicit
stencil rule uses doubled lattice positions. Diagonal components have offset
0, off-diagonal ij components have offset e_i+e_j. A derivative D_i evaluates
f(position+e_i)-f(position-e_i); two derivatives use the four signed shifts.
For R2 use 2 epsilon_iab epsilon_jcd D_a D_c h_bd with
h_bd=q_bd/2 off diagonal and h_bb=q_bb. For C2 use
2 epsilon_iab D_a(E_bj-delta_bj tr E/2). All coefficients are integers.
R2 outputs diagonal values on sites and off-diagonal values on faces. C2_ii
lies at a body center; C2_ij for i!=j lies on the edge in the remaining axis.
These rules specify every term without importing a figure or numerical fit.

Commutativity of the differences and antisymmetry of epsilon prove
 R2 G^T=0, C2 S^T=0, G R2=0, R2^T=R2, tr R2=2S.
The checker also constructs the entire integer matrices on 3^3 and 5^3 tori.
The largest coefficients are 4 for R2 and 2 for C2; their row l1 bounds are
24 and 10. The proof is the stencil identity, not the two torus examples.

Let w_a=1 on diagonal slots and 2 on off-diagonal slots. The bounded local
clock Hamiltonian is
 H=H0 + (g/4) sum_(x,a) w_a [1-Re Z^(R2_row(x,a))]
       + [J N^2/(16 pi^2)] sum_(x,i,j)
                                  [1-Re X^(C2_row(x,i,j))],
 H0=U_v sum_edges [1-Re X^(G_row)]
                  +U_s sum_sites [1-Re Z^(S_row)].
Every coefficient is positive. The two dynamic sums commute with every
constraint stabilizer, by the displayed integer identities, for every N>=2.
They need not commute with each other. This is an exact finite-dimensional
local candidate Hamiltonian and an exactly invariant zero-syndrome sector.

Its formal small-field symbol is H_L plus higher powers of R and C, with
q's off-diagonal doubling and X=exp(2 pi i E/N) included. This is a statement
about that symbol and its constrained linearization. No bounded canonical
commutator, gapless finite-N ground-state phase or thermodynamic approximation
is inferred. N small enough to alias local characters illustrates why an
off-grid Taylor expansion alone cannot prove such a phase.

For a finite V-site periodic box, the dynamic Hamiltonian has norm at most
 B_V=9g V/2+9J N^2 V/(8 pi^2).
The penalty gap above its zero-syndrome sector is at least
 delta=min(U_v,U_s)[1-cos(2 pi/N)].
Because the dynamic part is positive and preserves the sectors, delta>B_V
is a sufficient finite-box condition for a full ground state to lie in the
zero-syndrome sector. This sufficient condition scales with volume; it is
explicitly not a uniform phase bound. Alternatively one can study the supplied
zero-syndrome sector directly without claiming it is the selected ground sector.

Each N-level slot can be embedded in finitely many qubits with an additional
local penalty for unused states. Mapping this model to the framework's precise
one-qubit nearest-neighbor law and its native formation is a separate compiler
and identification obligation. Finite-dimensional encoding alone does not
select this Hamiltonian, clock, geometry or state from the axioms.

## Regular compact characters and derivative order

Consider an exact compact realization of both linear gauge actions, with a
translation-invariant Hamiltonian expressible as a finite sum of local Weyl
characters exp i[<m,h>+<r,E>] and their adjoints. More generally allow an
absolutely summable character expansion with enough support/moment weights
to differentiate its symbol twice in k and twice in fields. Assume its Fourier
characters lift to the exact integer constraints, not merely modulo N aliases.
Here m and r denote the physical symmetric-tensor coefficients obtained from
the six canonical slots, including the constant 2 pi/N in an X character.
Integer lifting is tested before this fixed change of normalization.
In a smooth canonical small-field expansion, gauge invariance implies
 k_i m_ij(k)=0,
 (k^2 delta_ij-k_i k_j) r_ij(k)=0,
with m and r symmetric analytic symbols near k=0. Lattice midpoint differences
have the same leading forms, with qhat_i=2 sin(k_i/2).

Write m=A+B_l k_l+O(k^2). The first identity forces A=0. Symmetry in i,j and
antisymmetry in i,l of B_ij,l imply B=0 by cycling the three indices. Thus
every such local h-character is O(k^2). For r=R+O(k), the second identity says
tr R k^2-k^T R k=0 for every k. Hence R=(tr R)I, and taking the trace in three
dimensions forces R=0. Every local E-character is O(k).

Therefore the Hessian of any such character Hamiltonian has blocks
 H_hh=O(k^4), H_EE=O(k^2), H_hE=O(k^3).
For its canonical linearization F, the similarity transformation with
T=diag(I,|k|I) gives T^-1 F T=O(|k|^3). All eigenfrequencies are consequently
O(|k|^3). In a stable nonsingular TT basin the L-type construction saturates
the cubic order. A nonzero linear graviton speed is excluded in this precisely
specified regular compact-character class. This is not a no-go for qubits,
emergent nonlinear gauge symmetry or strongly interacting constraint phases.

A finite-N clock character only commutes with constraints modulo N. If the
integer divergence or scalar-contraction coefficients are bounded in magnitude
strictly below N, modular vanishing lifts to integer vanishing and the above
argument applies. High harmonics, winding/support scaling with N, a singular
semiclassical limit, nonanalytic infinite-order resummation or an additional
field can evade that hypothesis. None is silently discarded.

## Quantitative spatial-moment proof

The derivative statement can be proved directly in real space. Any constant
or linear symmetric strain is a symmetric gradient of a polynomial vector
field of degree at most two. Such a polynomial can be cut off outside the
finite support of a character and its stencil neighborhood. Therefore a
compactly supported divergence-free symmetric character annihilates every
constant and linear strain. In components, its zeroth and first spatial
moments vanish, including the declared midpoint offsets. Midpoint differences
reproduce these polynomial derivatives exactly. Likewise the scalar-gauge
map applied to quadratic beta produces every constant symmetric E shift,
since H->(tr H)I-H is invertible in three dimensions. Every invariant local
E-character has zero zeroth moment.

For a character centered at x, let mu_2(m) be the sum of absolute coefficient
norms times squared distance from x, and mu_1(r) the analogous first moment.
Taylor's integral remainder gives
 |m(k)|<=|k|^2 mu_2(m)/2, |r(k)|<=|k| mu_1(r).
Fixed changes between the six canonical slots and orthonormal tensor slots
only change a finite dimension-dependent constant. For H=sum_(x,a) c_a
cos(<m_a,h>+<r_a,E>+phi_a), the sufficient summability condition is
 sum_a |c_a| [mu_2(m_a)^2+mu_1(r_a)^2]<infinity.
It bounds the three Hessian blocks at orders 4,2,3 respectively. The cross
bound follows by Cauchy-Schwarz. This makes the locality/regularity premise
quantitative and prevents hiding a singular infinite-range sum behind a
finite-order Taylor argument. Canonical symplectic normalization is fixed
and nonsingular; an independently derived singular Berry structure is outside
this class and requires a separate mode calculation.

A translation-invariant compact effective energy that retains these exact
symmetries and this summability after eliminating auxiliary variables retains
the bound. Merely saying that auxiliary matter is massive does not prove all
these hypotheses. A gapless boundary, nonlocal topological functional, new
gauge action or uncontrolled infinite-order sum is not excluded by this result.

## Finite penalties and the scalar Jordan chain

Use k=(0,0,k), normalized scalar coordinates h_t=(h_xx+h_yy)/sqrt(2),h_z=h_zz,
and the same E_t,E_z. Add U/2 |G|^2+V/2 S^2 to H_N. The scalar blocks in
H=(p^T K p+q^T B q)/2 are
 K=[[0,-J/sqrt(2)],[-J/sqrt(2),J/2+U k^2]],
 B=diag(-g k^2+2 V k^4,0).
For every finite U and J>0, det K=-J^2/2<0. A large derivative penalty cannot
make this unconstrained real canonical quadratic Hamiltonian bounded below.
Even taking U arbitrarily large at fixed nonzero k leaves a negative eigenvalue.
It vanishes only in the singular projection onto G=0, not at finite U.

The scalar Hamilton matrix F=[[0,K],[-B,0]] obeys F^4=0. If B_tt is nonzero,
F^3 is nonzero: all scalar frequencies are zero but the flow has a nontrivial
Jordan chain and can grow cubically in time. Treating these zero eigenvalues
as stable harmonic modes would be wrong. On the exact constrained quotient
they are removed and the two TT modes are positive. The bounded finite-clock
Hamiltonian is not unbounded; this calculation challenges its unconstrained
small-field Gaussian approximation, not its full nonlinear quantum phase.

## Static scalar-source comparison

For nonzero k define P=I-kk^T/k^2. R is symmetric transverse, and a supplied
scalar source imposes tr R=rho. Minimize g|R|^2/2 over this affine space:
R_min=rho P/2, since P:P=2. The minimum is g|rho|^2/4, with no k-dependent
Coulomb kernel. On a periodic box use neutral sources and omit k=0. The
resulting cross-energy for disjoint neutral scalar-source profiles is zero
in the isotropic quadratic H_L comparator. Directional field tails alone do
not establish an interaction tail after the full tensor contraction.

For H_N, the physical TT part remains positive while the supplied scalar
constraint fixes h_scalar=-rho P/(2k^2). Its static energy contribution is
-g|rho|^2/(4k^2), giving the attractive inverse-Laplacian kernel. This does not
prove matter energy positivity, nonlinear gravity or a finite-clock phase.
The scalar source itself is supplied; deriving a mobile conserved matter
stress source and reciprocal backreaction is a separate obligation.

The minimization is over the actual curvature image, not an enlarged set
of arbitrary transverse tensors. For each nonzero momentum,
R(R(h))=k^4 h on the transverse symmetric subspace. Thus every transverse R
has a preimage; the minimizing one has h=-rho P/(2k^2). On the staggered
lattice replace k by qhat=2 sin(k/2), including the actual midpoint phases.
There are no extra zeros of qhat^2 in the Brillouin zone. The runner constructs
this metric field and verifies S q=rho against the real-space integer stencil,
then compares the entire R field with a separate constrained least-squares
minimization.

More explicitly, R=R_TT+rho P/2 is an orthogonal decomposition, so
H_L has minimum g integral |rho(k)|^2/4. The H_N spatial quadratic form is
k^2 |h_TT|^2-k^2 |tr h_transverse|^2/2, giving its stated minimum. The same
source shift leaves the reduced TT oscillator frequencies unchanged, so these
are also the source-dependent energy differences of the specified reduced
quadratic quantum comparators after the common zero-point term is subtracted.
This does not calculate a nonlinear finite-clock defect potential. A source
text with a different scalar-defect force statement is not used as a premise;
the reading ledger records that scope distinction.

## Checks and falsifiers

The exact polynomial system gives no constant or linear divergence-free
symmetric h-character, a six-dimensional quadratic space, no constant
scalar-invariant E-character and an eight-dimensional linear space. Direct
canonical tensor operators reduced to TT agree with the two mode
powers at axial and non-axial k. The scalar Hamilton matrix has exact
characteristic polynomial lambda^4, fourth power zero and generic third power
nonzero. A separate real-space constrained minimization on 3^3 and 5^3 periodic
staggered lattices gives g/4 sum rho^2 and zero cross-energy between disjoint
neutral scalar profiles, with residuals below 4e-15. The integer incidences
commute exactly. These checks support the displayed comparator; the full
nonlinear finite-clock phase remains open.

The primary embeds all scientific code, uses no input files or helper
runners, and reports four substantial families. Mutation receipts bind exact
changed source and execution evidence. Passing examples challenge the proofs;
they do not confer independent review, a phase theorem or formal retention.
The mixed-character check retains the factor i from one spatial derivative,
so its Hessian is Hermitian and respects the reality relation at opposite k.

## Negative-claim discipline

### N1

Actual examined alternatives are (i) exact compact vector and scalar
constraints, with a constructed cubic-symbol Hamiltonian; (ii) noncompact
weakly invariant linearized gravity, with positive TT quotient; (iii) finite
quadratic penalties, with an indefinite scalar form and nilpotent dynamics;
(iv) finite-N modular characters, with explicit non-lifting aliases;
(v) a trace-free E constraint, whose quadratic divergence-free traceless
h-character space vanishes and whose first possible invariant is cubic;
(vi) massive auxiliary matter with an explicitly conditional regular local
effective energy; and (vii) strongly interacting/nonlinear or boundary routes,
which remain open. The list is not an exhaustive classification of qubit models.

### N2

The regular compact-character hypothesis, a controlled ground-state phase,
and a native physical-source map are related obligations, not independent
no-go walls. Finite penalty failure concerns a Gaussian comparator and is not
a second proof against the full compact model. Source contact behavior concerns
one specified isotropic quadratic energy; generic anisotropy or additional
couplings are outside that exact formula.

### N3

Canonical tensor pairs, Gauss/scalar constraints, couplings, zero-syndrome
sector, small-field expansion and scalar source are supplied. The local
integer construction makes them concrete but does not derive them from the
minimal axioms or the kinetic-isotropy primitive. A spin-two cubic-group
representation is not a graviton spectrum or a physical metric.

### N4

The current-main Regge action-selection note grants metric/edge-length
variables and embedding-inertness. Its linearized action class does not provide
this finite-clock phase. Gu-Wen's N-type strong-coupling gap is explicitly
uncontrolled in its own section VII.E. The scalar-defect force sentence is not
used; the complete isotropic quadratic source problem is rederived and checked
both in real space and by its actual metric field in Fourier space.

### N5

Exact coefficient algebra, arbitrary-momentum analytic mode reduction and
integer stencil identities carry the bounded general statements. Finite torus
ranks are examples, not prime-N code dimensions or a thermodynamic limit.
Nonzero-momentum mode count excludes the six uniform canonical pairs.

### N6

The finite-clock Hamiltonian and its invariant sector are constructive
partial results. The live routes include an independently controlled nonlinear
constraint mechanism, an additional physical field or boundary structure, and
a regularity assumption that actually fails in a demonstrated phase. None is
added as an axiom or declared impossible.

### N7

The strongest objection to an all-qubit negative claim is correct: finite-N
aliases and the strongly interacting N-type route lie outside the regular
character bound. Also, H_N is spatially local despite its density having a
boundary variation, and its exact constrained quotient is positive. These
facts are retained explicitly. They do not establish its finite-clock phase.

### N8

Earlier charged-gauge milestones concern spin-one histories/covariances
and matter metric flow. This block supplies an actual tensor constraint complex,
its local clock dynamics and a spectrum/source comparison. The standard
continuum tensor models have prior art. No new axiom contradiction or claim
of literature priority follows from the present derivations.

## Sources and review boundary

- [Gu and Wen, helicity-two modes from qubit models](https://arxiv.org/abs/0907.1203v3): continuum comparators and explicit warning about the N-type approximation.
- [Xu and Horava, lattice Lifshitz gravity](https://arxiv.org/abs/1003.0009v1): tensor-phase and boundary-term comparator.
- [Pretko, higher-rank U(1) spin liquids](https://arxiv.org/abs/1604.05329v3): charge-mobility context.
- [Bravyi, DiVincenzo and Loss, Schrieffer-Wolff theory](https://arxiv.org/abs/1105.0675): its product-space hypothesis is checked and not imported into this stabilizer code.

No editable prompt, workflow, axiom or primitive file changes. No author audit
verdict, effective retained status or main merge is part of this proposal.

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "Construct native dynamical geometry with controlled helicity-two propagation, constraints and reciprocal physical sources."
source_of_blocker_text: "frontier_question"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Independently review the finite-clock constraint complex and regularity bound; pursue a controlled nonlinear or otherwise explicitly escaping linear-mode mechanism."
conditional_surface_status: "Supplied finite local tensor model and exact comparator mathematics; finite-payload gravitational phase and native source/law identification remain open."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit integer construction, regular-character frequency bound and exact quadratic penalty/source comparisons; no all-qubit or axiom-forcing conclusion."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
