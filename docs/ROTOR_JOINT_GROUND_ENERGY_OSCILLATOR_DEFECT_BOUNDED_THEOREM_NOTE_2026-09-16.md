---
claim_id: rotor_joint_ground_energy_oscillator_defect_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/rotor_integer_gaussian_positive_square_check_2026_09_16.py
upstream_dependencies: ["rotor_uniform_compact_field_soft_response_bounded_theorem_note_2026-09-16"]
claim_scope: "Supplied quadratic paired Wilson/rotor model without additional onsite charge interaction: uniform ground-energy and positive-square defect densities tending to zero along every joint g to zero and L to infinity sequence."
---

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

# Uniform ground energy and oscillator-defect density

Supplied quadratic paired Wilson/rotor model without additional onsite charge interaction: uniform ground-energy and positive-square defect densities tending to zero along every joint g to zero and L to infinity sequence.

The model and state are supplied conditions. The proof uses no physical identification from another source package. Historical author checks are distinguished from current source-bound execution below.

**Matter restriction:** no additional unscaled onsite charge interaction is included. Use the normalized trace over the entire finite-volume ground space. Local probes and paths are fixed; time claims are uniform only on fixed compact intervals.

## 1. Model, restriction, and proposed result

Use the exact integer charged rotor and normalized full ground-space trace
`rho_(g,L)` of compact-field concentration theorem, on a periodic cubic lattice with V=L^3, L>=3.
All energies below are dimensionless: write `calH=aH`. Fix positive homogeneous
link and plaquette weights W_E,W_B, independent of g,L. The matter Hamiltonian
is the number-conserving conjugate pair of two-orbital Wilson matrices

    h_+(k)=sin(k_x-b) sigma1 + sin(k_y) sigma2
           +[2+zeta-cos(k_x-b)-cos(k_y)-cos(k_z)] sigma3,
    h_-(k)=h_+(-k)^*,               0<zeta<1.                 (1)

The numerical star in (1) is entrywise conjugation. The fixed matter sector
is N_+=N_-=V. **There is no additional onsite charge interaction in this
note.** compact-field concentration theorem allowed a nonnegative charge penalty; that wider hypothesis
is insufficient for convergence to free matter. An unscaled penalty would
contribute to the dressed Slater trial and remain a separate interaction.

Let D be tail-minus-head incidence, C the oriented curl, and set

    S=W_B^(1/2) C W_E^(1/2),
    Omega=(S^*S)^(1/2),       Omega_p=(SS^*)^(1/2),
    M=S^* Omega_p^+,          E_gamma,L=(1/2)tr Omega.       (2)

Here `Omega_p^+` means the inverse of Omega_p on its positive range and zero
on its kernel. Thus M is a partial isometry, S M=Omega_p, and M M^* is the
positive-range projection of Omega. All matrices are real; adjoints are
Euclidean transposes. Let E_m,L be the free paired Wilson ground energy on
the same torus and in the stated filling. Define operators

    P_l=g sqrt(e_l) E_l,
    Z_p=sqrt(b_p) sin((C theta)_p)/g,
    Q_l=P_l-i(MZ)_l,           Z_perp=(I-M^*M)Z.            (3)

There are constants C0,c0,g0>0 depending only on the fixed coefficients such
that, for 0<g<=g0 and L>=3,

    |E_ground-E_gamma,L-E_m,L|/V <= C0 (sqrt(g)+L^-1),     (4)

    rho[ sum_l Q_l^*Q_l
          +g^-2 sum_p b_p(1-cos theta_p)^2
          +||Z_perp||^2 ]/V <= C0 (sqrt(g)+L^-1).         (5)

Here and below theta_p=(C theta)_p. Each gauge and matter energy density
also differs from its respective free energy density by at most the same
order. The conclusion holds along every joint sequence g->0, L->infinity;
no relation between their rates is imposed. Estimate (5) is an averaged
ground-state bound, not an operator-norm bound or a bound on all states.

The proof uses compact-field concentration theorem only for the uniform actual-ground plaquette estimate

    rho(1-cos theta_p)<=B0 g^2,                            (6)

where B0 is independent of L. That result was derived from a different,
unoptimized integer Gaussian with a paired onsite product. No result in the
present note is used to obtain (6).

## 2. Exact positive squares, with compact defects retained

On the smooth physical core, P and Z preserve Gauss law and

    sum_l Q_l^*Q_l
      =sum_l P_l^2 + ||MZ||^2
           -sum_p (Omega_p)_pp cos theta_p.               (7)

Indeed, the differentiated term is

    sum_(l,p) sqrt(e_l) M_lp sqrt(b_p) C_pl cos theta_p
      =sum_p (S M)_pp cos theta_p.

Using `2(1-cos t)=sin^2 t+(1-cos t)^2` gives the exact identity

    calH_gauge = (1/2)sum_l Q_l^*Q_l
       +(1/2)sum_p (Omega_p)_pp cos theta_p
       +(1/(2g^2))sum_p b_p(1-cos theta_p)^2
       +(1/2)||Z_perp||^2.                               (8)

The three displayed defect terms are nonnegative. This is a quadratic-form
identity on the electric form domain: at each finite g,L the multiplication
terms are smooth and bounded, and smooth physical functions are a form core.
The ground vectors lie in this domain. No finite Fourier cutoff is inserted.

The cubic curl satisfies ||C||<=sqrt(12), as follows from its Fourier symbol
with link differences d_i=e^(ik_i)-1 and ||C(k)||^2=sum_i|d_i|^2. Hence

    ||Omega||=||Omega_p||<=w0:=sqrt(12 e_max b_max).        (9)

By (6), the cosine trace differs from tr Omega by at most
3 w0 B0 g^2 V. In particular,

    rho(calH_gauge)>=E_gamma,L-(3/2)w0 B0 g^2 V.          (10)

## 3. The integer boundary lattice and its dual

Let S0=range(C^*) in real link space and

    Lambda0=S0 intersect Z^(3V).                         (11)

On the cubic cellulation of the three-torus,

    Lambda0=C^* Z^(3V).                                 (12)

For completeness, an integer closed link chain can be reduced by elementary
plaquette boundaries to three coordinate winding cycles: commute successive
steps by a plaquette, cancel reversed steps, and collect the three net
windings. Its integer homology class is therefore in Z^3, and vanishes
exactly for an integer plaquette boundary. Equivalently, the cubical torus
has torsion-free first integer homology Z^3. The quotient of all integer
link chains by boundaries is an extension of this free group by the free
group of integer vertex boundaries. It is torsion-free. Thus the image in
(12) is saturated, proving (11)-(12). Its rank is 2V-2: there are V-1
independent divergences and three independent winding constraints.

This argument concerns electric link boundaries, not the integer image of
curl on a dual complex. In particular, no torsion factor is omitted in the
Poisson dual below. Primitivity implies

    Lambda0^*=P_(S0) Z^(3V).                            (13)

One proof is to extend a basis of the primitive lattice to an integer basis
of all link chains. Every integer-valued linear functional on Lambda0 then
extends to the ambient integer lattice; its real representing vector is an
integer z, whose projection onto S0 gives the dual vector.

The map `eta=P_(S0)z -> q=Cz` is well defined and is a bijection from
Lambda0^* to `C Z^(3V)`. It is injective because C has no kernel on S0.
The zero-winding restriction in (11) is a choice of trial vector, not a claim
that the coupled Hamiltonian preserves that subspace.

## 4. A uniformly optimized compact Gaussian

Define the positive matrix on S0 and its inverse there by

    A=W_E^(-1/2) Omega W_E^(-1/2),     K=(A|_(S0))^-1.   (14)

A has range S0 and kernel ker C. Direct multiplication gives

    A W_E A=C^* W_B C,
    C K C^*=W_B^(-1/2) Omega_p W_B^(-1/2).               (15)

To verify the second formula without commuting noncommuting weights, put
`B=W_E^(1/2) Omega^+ W_E^(1/2)`. For d in S0, A B d=d since
W_E^(1/2)d belongs to range Omega. Thus Kd=P_(S0)Bd; applying C removes
the discarded component. The polar identity `S Omega^+ S^*=Omega_p`
then gives (15).

Use the normalized link wavefunction in electric representation

    psi(n)=Z^-1/2 exp[-g^2 n.K.n/2],    n in Lambda0.     (16)

It is smooth in angle space at finite g,L and invariant under all link-angle
directions in ker C. In particular, it carries no unaccounted electric
harmonic flux. Poisson summation, or the theta-function maximality at an
integer center, gives the moment-generating bound

    E exp(t.n)<=exp[t.A.t/(4g^2)],
    E(n n^*)<=A/(2g^2).                                (17)

For the first inequality complete the square; the shifted theta sum is no
larger than the centered sum because its dual terms have phases of modulus
one and the centered terms are all positive. Differentiate at t=0 for the
covariance bound. Therefore the trial electric energy is <=tr Omega/4.

Let beta=pi^2/g^2. Under (13), the dual weights are exp[-beta F(q)] with

    F(q)=eta.A.eta
        =q.W_B^(1/2) Omega_p^+ W_B^(1/2).q
        >=c ||q||^2,          c=b_min/w0>0.             (18)

The inequality follows from Omega^2<=w0 Omega, conjugated by W_E^-1/2;
it holds for every dual vector, uniformly in volume.

For d_p=C^*1_p, completing the square in the overlap and applying Poisson
summation gives exactly

    I_p=<psi,U^(d_p)psi>
       =exp[-g^2 d_p.K.d_p/4] E_beta (-1)^(q_p).         (19)

The expectation uses the normalized dual measure on C Z^(3V). Although the
last expression contains signs, I_p is real and positive by its original
overlap sum. Since 1-(-1)^n<=2n^2, (15) implies

    g^-2 sum_p b_p(1-I_p)
       <=tr Omega/4 +(2 b_max/g^2) E_beta ||q||^2.       (20)

The dual partition function need not be close to one in a large volume.
Only its pressure is used. Set theta1(t)=sum_(n in Z) exp(-t n^2). Then

    Z_dual(beta/2)<=theta1(beta c/2)^(3V),
    E_beta F <=(2/beta)log Z_dual(beta/2).               (21)

For the second line integrate the nonincreasing expectation E_s F from
beta/2 to beta and use Z_dual(beta)>=1. All finite-volume sums converge
absolutely. Combining (18)-(21) bounds the gauge trial excess per volume by

    r(g):=(12 b_max/(pi^2 c)) log theta1(pi^2 c/(2g^2))
          =O(exp[-c1/g^2]).                             (22)

For example log theta1(t)<=2 exp(-t)/(1-exp(-3t)). This follows from
n^2>=1+3(n-1) for integers n>=1 and log(1+x)<=x. We have proved

    <psi,calH_gauge psi><=E_gamma,L+V r(g).              (23)

A second, less sharp estimate will control dressed hopping individually.
The direct overlap form and Jensen give

    1-I_p<=g^2 d_p.K.d_p/2<=g^2 w0/(2b_min).            (24)

This trial plaquette estimate is distinct from the actual-ground estimate
(6), and neither one assumes the desired Gaussian ground state.

## 5. Blocks, half filling, and exact charge dressing

Choose an integer 2<=R<=L. Let q=floor(L/R). Divide each periodic coordinate
into q intervals whose lengths differ by at most one. Every side length is
between R and 2R, and cutting the interval boundaries removes at most

    3 q L^2 <= 3V/R                                    (25)

links, including the three periodic seams when q=1. The blocks themselves
have open boundaries. Each contains n_B sites and 2n_B orbitals per species.

At b=0 the antiunitary sigma1 K_complex anticommutes with each open-block
Wilson matrix: this follows separately for the onsite sigma3 term and the
three hopping matrices `(-sigma3-i sigma1)/2`,
`(-sigma3-i sigma2)/2`, and `-sigma3/2`. For nonzero b use the open-block
site unitary u_x=exp(ib x_1); the antiunitary becomes u^2 sigma1 K_complex.
The spectrum is symmetric about zero. Its zero eigenspace has even
dimension because the entire dimension is even and nonzero eigenvalues
occur in pairs. Occupying the negative subspace and half of any zero
subspace gives an unrestricted Fock ground state with precisely n_B
particles. Let phi_B be this Slater vector for the plus species and its
complex conjugate for the minus species. Their product has zero total
charge in the block and equal local expected densities. The product over
blocks is a free cut-system ground state with N_+=N_-=V.

In each rectangular block root the axial tree at its lower corner: use all
z-links, the y-links at z=0, and the x-links at y=z=0. Let p_x be its root-to-x
integer path, so Dp_x=delta_root-delta_x. For a block-neutral matter charge
configuration Q define

    E_T(Q)=-sum_x Q_x p_x,             D E_T(Q)=Q.       (26)

On the support of the block Slater vector define the unitary dressing

    Phi(theta)=exp[i theta.E_T(Q)] phi_blocks,
    Psi(theta)=psi(theta) Phi(theta).                   (27)

The link Fourier modes of psi are divergence free. Acting with -i partial
on the exponential in (27) adds the integer flow E_T(Q), so Psi obeys exact
integer Gauss law. Its norm is one. No charge sector is projected away.

For a tree edge l, E_T,l is a signed total charge of its descendant subtree
A_l. With C_B the occupied one-particle projector, the ordinary Slater
variance identity gives

    <E_T,l>=0,
    <E_T,l^2>=2 tr[C_(A_l)(1-C_(A_l))]<=2m |A_l|,
    m=2.                                                (28)

Independence of the species and equality of their local means are used
here. The electric cross term between E psi and E_T phi vanishes exactly.
Counting each vertex once for each ancestor edge yields

    sum_l |A_l|=sum_x dist_tree(root,x)<=6R n_B.          (29)

Thus the entire dressing adds at most 6m e_max g^2 R V to the electric
energy. Estimating the norm of the worst charge configuration instead would
give an unnecessarily large and unusable cost.

## 6. Hopping after dressing and the trial upper bound

For a link l from x to y, the dressed phase in the plus hopping matrix is
the fundamental loop

    exp[i theta.(e_l+p_x-p_y)].                          (30)

The minus phase is its conjugate. A literal filling of the loop uses at
most 4R elementary plaquettes. For an x-link at (x,y,z), it is the negative
xy strip from 0 to y at z=0 followed by the negative xz strip from 0 to z
at that y; for a y-link it is the negative yz strip from 0 to z; z-links
belong to the tree. This construction works on every rectangular block.

For any such product of plaquette unitaries, pointwise telescoping gives

    |U_loop-1|<=sum_(p in filling)|U_p-1|.               (31)

With (24) and Cauchy--Schwarz, its trial expectation is <=C gR. The operator
norm of the paired Hermitian link hopping difference is bounded by
`2||T_l||_* |U_loop-1|`; the nuclear norm is required. Summing links costs
at most C gR V. Cross-block hopping has zero expectation in (27), because
each block has a fixed particle number for each species and the dressing
is diagonal in occupations.

Removing a boundary link changes the free many-body Hamiltonian in operator
norm by at most 2||T_l||_*. The free cut ground energy E_m,cut consequently
satisfies |E_m,cut-E_m,L|<=C V/R. Both minima are attained at the stipulated
half filling, so this comparison is valid in the fixed global sector as
well as in unrestricted Fock space. Equations (23)-(31) prove

    E_ground<=E_gamma,L+E_m,L
                  +C V(R^-1+gR+g^2R+r(g)).             (32)

## 7. A lower bound on the actual matter energy

At each fixed theta, remove cross-block links and apply the same site
phase transformation defined by the tree. This is a finite-dimensional
matter unitary, and turns every internal hopping phase into (30). The
zero-field open-block Fock Hamiltonian is bounded below by E_m,cut on all
occupations, by the half-filling argument above. Hence, as a pointwise
matrix inequality in angle space,

    calH_m(theta)>=E_m,L-C V/R
                  -sum_(internal l)2||T_l||_*|U_loop,l-1|.  (33)

This lower bound does not assert that the actual state has neutral charge
in every block. No such assertion is needed: the pointwise matrix
inequality holds on the full matter Fock space before imposing Gauss law.
Taking the actual ground trace and using (6), (31), and translation
invariance gives

    rho(calH_m)>=E_m,L-C V(R^-1+gR).                    (34)

Together with (10), this proves the energy lower bound complementary to
(32). Subtract (34) and the cosine-trace term of (8) from (32) to obtain

    rho[sum Q^*Q+g^-2 sum b(1-cos theta)^2+||Z_perp||^2]/V
        <=C[R^-1+gR+g^2R+g^2+r(g)].                    (35)

The bounds on each separate energy follow in the same way by subtracting
the lower bound on the other contribution from the total upper bound.

Finally choose `R=floor(min(g^-1/2,L))` and take g0<=1/4. Then R>=2,
R^-1<=2(sqrt(g)+L^-1), gR<=sqrt(g), and g^2R<=g^(3/2).
The remaining g^2 and exponential terms are also bounded by a constant
times sqrt(g). This proves (4)-(5) without an order-of-limits assumption.

## 8. Finite evidence and scope

The paired integer-Gaussian/positive-square runner checks the lattice rank
and Smith invariants on the literal 3^3 torus, the weighted metric identities,
the Poisson parity formula, and the operator identity on a padded Fourier
core. Its hard-cutoff discrepancy is retained and identified explicitly:
a truncated shift is not unitary at its artificial boundary. The analytic
proof uses the untruncated rotor throughout.

The tree/Slater runner constructs literal paths and plaquette fillings,
checks exact charged Gauss law and the dressed hopping energy in a 64-state
two-species sector, and compares Slater charge variances with determinant
fidelity curvature on open Wilson blocks. A reversed-dressing control has
an order-one energy error. These are selective author checks of load-bearing
identities; they do not prove a thermodynamic phase or confer independent
review status.

The next separate obligation is to turn (5), using translation invariance,
into a local characteristic-function bound uniform in L. An energy-density
estimate alone is not yet a statement about those correlations. Fixed-g
masslessness, real-time limits, finite-cyclic realization, law selection, and
axiomatic TOE closure remain unproved here.

## No-Go Discipline Gate

N1: this is a positive supplied-model theorem. Fixed-positive-coupling infrared behavior, nonlinear gauge dynamics, growing-support limits, finite-clock realization and native law selection are open directions, not five completed exclusion attempts. No broad negative certificate is claimed.

N2: the model assumptions are stated hypotheses, not independent physical walls. The finite counterexamples refute only the particular inference specified beside them.

N3: the proof retains the normalized full ground trace, possible ground degeneracy, exact Gauss constraint, fixed coefficients, observable domain and order-of-limits quantifiers. Notes requiring free matter exclude an extra unscaled onsite charge interaction.

N4: the supplied continuous rotor/CAR carrier, Hamiltonian, homogeneous weights, Wilson parameters, time and ground ensemble are conditional inputs. Linked proofs below are the actual mathematical dependencies; historical campaign pins confer no authority or additional premise.

N5: the paired programs report finite element/site/mode/block coverage and unchanged tolerances. Uniform-volume estimates, arbitrary joint-sequence convergence and bounded-time analytical arguments are written proofs, not executed infinite-lattice simulations.

N6: conditional mathematical progress does not select the supplied model from the framework axioms or require a new axiom.

N7: alternative interacting fixed-coupling constructions and different physical carriers remain open. Neither finite check success nor the explicit toy counterexamples excludes them.

N8: original personal reviews, failed runs and 28 mutation failures are historical evidence, preserved with their original source hashes. They are not fresh independent review or an audit verdict.


## Mathematical dependencies and current evidence

Actual load-bearing proofs: [compact-field concentration theorem](ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-16.md).

Reproduction programs: [rotor_integer_gaussian_positive_square_check_2026_09_16.py](../scripts/rotor_integer_gaussian_positive_square_check_2026_09_16.py), [rotor_tree_slater_dressing_check_2026_09_16.py](../scripts/rotor_tree_slater_dressing_check_2026_09_16.py). Each declares 120 seconds; all calculations and tolerances retain the original finite scope.

Current canonical caches: [rotor_integer_gaussian_positive_square_check_2026_09_16](../logs/runner-cache/rotor_integer_gaussian_positive_square_check_2026_09_16.txt), [rotor_tree_slater_dressing_check_2026_09_16](../logs/runner-cache/rotor_tree_slater_dressing_check_2026_09_16.txt). These links describe the required current evidence; historical outputs do not certify the new source bytes.

[Original recovery](work_history/review_loop/pr8160/README.md) and [exact manifest](work_history/review_loop/pr8160/original-manifest.json) preserve all 86 original files, including full proof development, original outputs, failed propagation runs and mutations.
