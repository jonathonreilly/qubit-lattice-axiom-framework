# PRE47: local finite-time charge covariance in the full common process

This is a bounded independent reconstruction before author47 release. Earlier
42/43 arguments and their publication comparison are disclosed prior exposure;
the primitive calculation, physical-tree calculation and proof below were
written here without importing their scientific code. Only the three named,
exactly pinned common-model parents are scientific inputs. Their model and
limit theorems remain conditional and unaudited. No physical preparation,
particle identification, empirical fit or audit verdict is supplied here.

## Result and quantified scope

Let G be a fixed finite simple bipartite graph of maximum degree at most z,
with z>=2. Use the full physical rotor P space: A sites are occupied, B sites
may be empty or occupied, and div E=q-1_A. Let

    h = K D + delta H4,
    H4 = -2 sum_{unordered overlapping A stars a,c} S_ac* S_ac,
    S_ac = F_c F_a P,
    L_mu = sqrt(kappa) B_mu.

The B_mu are all the original resolved P j_(ab,sigma) F_a P channels, or all
the stipulated unnormalized coherent edge sums B_(ab,+)+B_(ab,-). No later
channel is removed. D is the actual empty-B-gated electric form from the
parent, not sum E_e² after a birth. Take K>=0, delta>=0, kappa>=0. The stated
strictly positive parent parameters are included.

Initially the record number is |A|. Gauss law then forces the unique matter
word q^0=1_A, with every B vacant. The field density is any normal density on
the divergence-free rotor subspace, including correlated or mixed densities
with no electric moments. Denote the complete trace-one GKLS evolution by
rho(t), and its equal-time connected charge covariance by

    C_xy(t) = Tr rho(t) q_x q_y
                  - Tr rho(t) q_x Tr rho(t) q_y.

For every pair of sites, including diagonal entries,

    C_xy(t) = kappa t M_xy + R_xy(t),                  (1)
    M = 4 sum_{a in A,b~a} (z_a-1)
                          (e_a-e_b)(e_a-e_b)^T.       (2)

Here e_x are coordinate vectors in the vertex space, not electric link
operators. A completely explicit local bound for R is given below. It is
O_z(kappa(delta+kappa)t²), uniform in the finite volume, K, the normal input
field, and the position or separation of the two sites. This is a uniform
small-time statement; it is not a claim that the first-order expression is
accurate at all positive times.

On a regular degree-z graph, M=4(z-1)(z I-Adj). On an even cubic torus of
period L>=4, z=6, so

    C_xx(t) = 120 kappa t + O(kappa(delta+kappa)t²),
    C_xy(t) = -20 kappa t + O(kappa(delta+kappa)t²), x~y,
    C_xy(t) = O(kappa(delta+kappa)t²), x!=y, x not~y.   (3)

The constants in this displayed O notation are explicit below and deliberately
loose. For kappa>0, the nearest-neighbor Pearson correlation tends to -1/6,
uniformly in that family, with an explicit error criterion. The sign-resolved
and coherent instruments have the same leading charge covariance. Their
full later densities and finite-time covariances are not asserted equal.

## Exact source boundary

The three scientific files, completely read and checked against both their
working bytes and git revision 60c5f194d940a7bbaf1cdd545296e31d74a02f1a, are:

| Parent | SHA256 | Imported content |
|---|---|---|
| LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS...2026-09-24.md | 7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a | Exact local H4 pair form, local jump form and norm bounds |
| LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT...2026-09-24.md | c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b | Actual D, common rotor Hilbert space, finite-graph mild GKLS process |
| FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES...2026-09-24.md | 2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516 | Number preservation by h and increase by two under every original channel |

The six additional source records in SOURCE_PINS.json are procedural only.
ADDITIONAL_PROCEDURAL_PIN.json identifies the installed skill distribution
copy, whose bytes equal the recorded repository skill source.
No infinite-volume theorem referenced by those notes is imported. The
finite-volume locality estimate needed here is proved directly. No parent
runner, author46/47 packet, other active checker packet, campaign checkpoint
or additional publication science was read or executed.

## 1. First-order coefficient from actual formation paths

Orient every link from A to B; this is an integer-electric convention change,
not a model change. On the minimum-number input, one term of a resolved mark
on (a,b) first moves the old + record from a to c, with c~a and c!=b, and
then forms charges sigma at a and -sigma at b. Its final charge increment is

    d_(a,b,c,sigma)
        = (sigma-1)e_a - sigma e_b + e_c,             (4)

and its electric change is +sigma on (a,b), -1 on (a,c), zero elsewhere.
The first hop and formation separately satisfy Gauss law. Each amplitude is
one. All other A records are unchanged.

For a fixed resolved channel the distinct c have distinct final matter
words. For a coherent edge channel the two signs have distinct final charge
at a, so they are also orthogonal for every charge-diagonal observable.
Within each branch the electric action is a unitary translation between
the relevant Gauss fibers. Hence, for every bounded diagonal matter function
f and every arbitrary normal incoming field, the channel effect compressed
to the minimum-number block is exactly

    P0 B_mu* f(q) B_mu P0
       = [sum_{branches of mu} f(q^0+d_branch)] P0.   (5)

In particular the output norm squared on a normalized minimum-number input
is z_a-1 per resolved sign, or 2(z_a-1) for the coherent edge. This is not a
global operator-norm formula. No sqrt(2) is divided out. The coherent signs are
not treated as extra observed submarks.

The loss term subtracts f(q^0) times these same rates. For
Delta q_x=q_x-q_x^0 and Delta q_x Delta q_y that loss contribution vanishes
on the initial block, because the initial values are zero. The Hamiltonian
also contributes zero: it preserves the minimum-number block and each such
observable is zero on it.

Consequently the initial mean and second centered raw slopes are

    d/dt <Delta q_x>|_0 = kappa mu_x,
    d/dt <Delta q_x Delta q_y>|_0 = kappa M_xy,
    mu = -2 sum_{a,b~a} (z_a-1)(e_a-e_b).             (6)

To check the covariance matrix, sum d d^T over all ordered choices of b,c
and both signs. Its A diagonal is 4 z_a(z_a-1), its B diagonal at b is
4 sum_{a~b}(z_a-1), its A-B entry on edge (a,b) is -4(z_a-1), and every
off-diagonal A-A or B-B entry is zero. The B-B cancellation uses BOTH signs:
the plus branch contributes -1 and the minus branch +1 to the product of
its two B charges. This proves (2), including all multiplicities.

The two mean increments start at zero, so their product has zero derivative
at time zero. Equations (1)-(2) thus concern the connected covariance of the
full ensemble, not the charge variance conditioned on one normalized mark.
M is positive semidefinite and annihilates the constant vector, consistent
with exact conservation of total charge.

## 2. Electric domains and local dynamics

D is the nonnegative diagonal multiplication operator

    D(q,E) = sum_{a in A,b~a,q_b=0} E_ab(E_ab-q_a)     (7)

in this orientation. Its local summands D_e commute strongly. Each depends
only on the two endpoint matter factors and that link's electric variable.
Every charge polynomial commutes strongly with D. H4 is bounded on a fixed
graph, and the finite jump family is bounded. Thus the parent finite-graph
trace-class semigroup exists for every normal input; no D-domain or moment
condition is imposed on the density in this report.

Write alpha_s(O)=exp(iKDs) O exp(-iKDs). For a bounded operator O supported
on a finite collection X of site/link atoms, only D_e whose support
intersects X enter alpha_s(O). All other D_e commute with O and with the
remaining D terms and cancel exactly. Therefore

    supp alpha_s(O) subset N_D(X),
    ||alpha_s(O)||=||O||.                            (8)

The enlargement is applied once to the ORIGINAL support. It is not an
iterated spread through all overlapping electric terms. This distinction
uses their mutual commutation.

These conjugated operators are strongly star-continuous, although they need
not be norm continuous. On trace class, left/right multiplication by a
uniformly bounded strongly star-continuous family is strongly continuous:
first prove it on finite-rank matrices, then approximate in trace norm.
The interaction-picture Hamiltonian commutator and jump/loss maps therefore
admit the usual trace-class Dyson integrals on a fixed graph. Equivalently
their adjoint integrals may be interpreted ultraweakly; no Bochner integral
in the norm topology of all bounded rotor operators is assumed.

A concrete reason not to use norm continuity is a plaquette shift W on an
initial divergence-free circulation E=M around that plaquette. The electric
energy difference for W is K(8M+4). At t_M=pi/[K(8M+4)], K>0,

    ||(alpha_(t_M)(W)-W)|E=M>||=2,

while t_M tends to zero. This is a genuine physical Gauss-fiber example,
not a field violating the constraint.

The Gauss subspace does not factor into local tensor products. Locality
counts below are made in the ambient effective tensor product with A local
dimension two, B dimension three and rotor links, then restricted to the
invariant Gauss subspace. Disjoint supports commute there as well.

For any normal initial state, not only the minimum-number preparation,
the weak integral equation for a bounded local charge polynomial O is

    <O>_t - <O>_s
       = integral_s^t < i delta[H4,O]
                         + kappa sum_mu D[B_mu]^*(O) >_r dr.  (9)

The integrand is bounded and continuous for a finite graph. Thus these
expectations are scalar C^1 without electric moments. In particular the
local covariance is Lipschitz for all finite times, with a volume-independent
constant given below. This is not a claim about an unbounded energy
expectation or about trace-norm differentiability of the whole density.

## 3. Explicit local constants

Use site and link variables as distinct atoms. An electric summand has
support {a,b,e}. Let

    b_z = 1+2z,      s_z = 2 b_z²,      R = s_z-1,
    h_0 = 4 delta z^6(z-1),
    j_0 = 8 kappa z²(z-1)²,
    u = b_z h_0,    v = b_z j_0,       Omega = u+v.   (10)

These are upper bounds, not fitted or optimal constants.

An outward star has at most 1+2z atoms. A magnetic pair has at most
2+4z=2 b_z atoms. Each atom belongs to at most z outward stars, and an A
anchor has at most z(z-1) other overlapping A stars. Therefore each atom
belongs to at most z²(z-1) magnetic pair supports. Since

    ||-2 delta S_ac* S_ac|| <= 2 delta z^4,

the sum of commutator-map norm bounds touching one atom is at most h_0.
There are at most 2z² resolved channels touching an atom, with
||B_res||<=z-1. For a coherent channel the safe triangle bound is
||B_coh||<=2(z-1), and at most z² such channels touch an atom. The
dissipator-map bound 2 kappa ||B||² makes j_0 valid for either choice.

The relation of sharing an electric support is symmetric; each atom has
at most b_z neighbors in this relation, including itself. Electric dressing
therefore multiplies the maximal pointwise sum of local map norms by at
most b_z and the support cardinality by at most b_z. All dressed magnetic
or jump maps have support size at most s_z, with Hamiltonian point-density
at most u and dissipative point-density at most v. None of these constants
depends on K, electric amplitudes or the number of vertices.

Before dressing, (9) gives |d<O>/dt|<=m(h_0+j_0)||O|| for a charge
polynomial with m site atoms. In particular, because ||q_x||<=1,

    |C_xy(t)-C_xy(s)| <= 4(h_0+j_0)|t-s|             (11)

for x!=y; the same bound also safely covers the diagonal. This all-time
Lipschitz estimate is weaker than the preparation-specific bound below.

## 4. A colored local Dyson bound retaining every birth

Let O be a bounded local charge-diagonal observable of support cardinality
m, scalar o_0 on P0. In a nonzero product of adjoint local maps, each new
support must intersect the union already reached from O. A disjoint
Hamiltonian commutator vanishes; a disjoint dissipator vanishes because
its jump and loss terms cancel exactly. After k maps the union has at most
m+kR atoms. Hence for a specified sequence of n Hamiltonian/dissipative
types, the sum of norms of all possible local terms is bounded by

    ||O|| product_{k=0}^{n-1}(m+kR) u^(n_H) v^(n_J). (12)

Time ordering supplies t^n/n!. The constants control the actual supports of
the time-dependent dressed terms, so they do not require their norm
continuity.

Every dressed magnetic term preserves P0. Any word containing only
Hamiltonian commutators has zero expectation in rho0, because O is scalar
on that block. Removing these zero contributions is legitimate before
bounding the remaining terms. For n>=1 the sum over type sequences with
at least one dissipator is bounded by

    ||O|| product_{k=0}^{n-1}(m+kR)
              [(u+v)^n-u^n] t^n/n!.                 (13)

This subtraction does not subtract one upper bound from another. It is
the direct sum of the nonnegative bounds for all colored words except the
all-Hamiltonian word.

For 0<=t<1/(R Omega), with the zero-coupling endpoint interpreted directly,
define

    F_m(w,t) = (1-R w t)^(-m/R),
    Psi_m(t) = F_m(Omega,t)-F_m(u,t),
    Phi_m(t) = Psi_m(t)-m v t.                       (14)

The binomial series sums (13), since the coefficient of (w t)^n is exactly
product_{k=0}^{n-1}(m+kR)/n!. Its positive series converges in this window,
uniformly over all finite graphs in the degree class and all fields.

The first dissipative term has exactly constant expectation in its time
variable. Equation (5) makes P0 J^*(O)P0 a scalar multiple of P0, and P0
commutes with D, so electric dressing leaves this compression unchanged.
The first Hamiltonian expectation vanishes. If a_O is the initial slope
computed from the undressed instrument, then

    |<O>_t-o_0-t a_O| <= ||O|| Phi_m(t).             (15)

This is a finite-time estimate of the complete process. It neither keeps
only one birth nor conditions on no earlier global event. In particular
the observation time need not satisfy t times the TOTAL graph event rate
much smaller than one; only the local bound in (14) is imposed.

One can see the coupling dependence without an asymptotic convention:

    Psi_1(t) <= v t/(1-R Omega t)^(1+1/R),
    Phi_m(t) <= m(m+R) v Omega t²
                        /(1-R Omega t)^(2+m/R).     (16)

These follow by integrating the derivative of F_m in w over [u,u+v] and
then bounding the remaining difference from its value at w=0.

## 5. Connected covariance and an explicit remainder

Apply (15) to Delta q_x Delta q_y, whose norm is at most four and whose
support has at most two sites. Apply (13)-(14) to each Delta q, of norm at
most two and initial expectation zero. All series coefficients are
nonnegative, so using m=2 also bounds the diagonal case. This proves

    |R_xy(t)| <= E(t) := 4 Phi_2(t)+4 Psi_1(t)²
              <= [8(R+2)v Omega+4v²] t²
                            /(1-R Omega t)^(2+2/R). (17)

The second term includes the product of the evolving mean increments;
it is not silently omitted in passing from a raw moment to a covariance.
Since u is proportional to delta and v to kappa, (17) proves the uniform
O_z(kappa(delta+kappa)t²) claim. For kappa=0 all these covariances are
exactly zero for all times, because the matter stays in P0. The Pearson
normalization is then undefined, not a nonzero limiting prediction.

For the cubic degree-six case, one possible explicit choice is

    R=337, u=12,130,560 delta, v=93,600 kappa,
    0<=t<1/[337(12,130,560 delta+93,600 kappa)].       (18)

These constants are intentionally very conservative. Their small numerical
window is a sufficient analytic window, not an estimate of the actual
breakdown time. No optimized constant or experimental accessibility follows.
If couplings grow in a further limit, the window must shrink accordingly;
fixed positive time cannot simply be substituted into a small-time estimate.

The proof applies to arbitrary normal fields, even a field family varying
with t or volume, with no moment bound. It establishes a uniform first-order
remainder; no uniform third-order expansion, energy-power statement or
norm-continuous field dynamics is inferred.

## 6. Dimensionless comparison before fitting

On a regular graph with z>1 and kappa>0 put

    V(t)=4 z(z-1) kappa t,     eta(t)=E(t)/V(t).

Whenever (14) holds and eta(t)<1, the site variances are positive and lie
between V(t)(1-eta) and V(t)(1+eta). For a nearest-neighbor pair,

    | C_xy(t)/sqrt(C_xx(t)C_yy(t)) + 1/z |
                 <= (1+1/z) eta/(1-eta).             (19)

For distinct non-neighbors the absolute normalized correlation is at most
eta/(1-eta). This follows just by bounding the normalized denominator
between 1-eta and 1+eta. As t decreases, eta=O_z((delta+kappa)t), so the
nearest-neighbor limit is -1/z, and specifically -1/6 on cubic tori.
No field translation invariance is needed: the leading coefficient is
geometric and field independent even if higher-order correlations are not.

This is a conditional dimensionless pattern for joint measurements of the
supplied commuting q observables in the specified preparation. It requires
no amplitude fit to kappa or an electric-charge unit to state it. It does
not identify q with measured electromagnetic charge, select the preparation
or lattice geometry in nature, select a physical time window, derive an
absorption detector, or compare with any actual dataset. Those remain
separate physical/calibration obligations.

If a realized input differs from the specified one by trace norm epsilon,
contractivity and ||q_x||,||q_x q_y||<=1 bound the covariance change at any
time by 3 epsilon. Thus epsilon=o(kappa t) is a sufficient additional
condition to retain the normalized small-time limit in such a family.
Fixed-time common-density convergence from a microscopic approximation
does transfer these bounded covariances. It does not, without an error
small relative to kappa t, justify a joint derivative/short-time limit.
The theorem here is for the common process; no microscopic-volume theorem
or physical selection is added.

## 7. Independent controls and what they actually test

`primitive_covariance_control.py` builds the cubic graphs afresh and executes
the legal old-record hop and formation separately, checking intermediate and
final Gauss law. The full result stores 1,920 L4 branches and 6,480 L6 branches,
both full covariance matrices for the two original instruments, a deliberately
wrong plus-only matrix, and 126 complete selected effect-Gram matrices on
two physical incoming fields. It also counts actual site/link supports after
the one electric enlargement. The complete exact covariance matrices give
diagonal 120, nearest entry -20, and all other distinct entries zero.

The separate `verify_read_only.py` reconstructs these slopes from the explicit
charge increment and from the weighted edge Laplacian, checks every stored
primitive and Gram entry and all support-incidence arrays, and rejects the
plus-only mutation. The 4,096 and 46,656 entries of each covariance matrix
are compared exactly. This is distinct checking machinery written here,
not another independent agent or an author runner.

`tree_full_generator_control.py` uses the connected tree

    A={0,1}, B={2,3,4,5},
    edges={(0,2),(0,3),(0,4),(1,4),(1,5)}.

On a tree each allowed charge word has a unique integer Gauss flow. The
entire total-charge-two physical space has 90 basis words, and the effective
P space has 40. This is an exact finite physical model, not a rotor cutoff.
The script constructs the primitive full-space F and j matrices, the exact
magnetic S* S term, all original effective jumps and the gated D. Its output
retains every integer matrix entry and physical field word.

The full GKLS matrix is evolved for both instruments, K=0,2,200,
delta=0.3, kappa=0.4 and t=0.0001,0.0002,0.0004,0.01: 24 finite-time rows.
All number sectors N=2,4,6 are kept. The smallest observed N6 probability is
2.5592833328030667e-8, so the control actually includes a second formation.
The exact initial kernel is the weighted irregular-graph Laplacian, not
the cubic kernel. The nearest pair (0,2) has normalized limit -1/sqrt(3).
Its smallest-time value is approximately -0.5773079380. Doubling the two
smallest times multiplies the absolute covariance remainder by about
3.9984901. These are floating diagnostics, not interval enclosures.

The read-only verifier independently rebuilds every saved integer primitive,
H4 and jump matrix, checks all gated electric entries, initial derivatives,
all 24 saved covariance arrays and all 1,628 finite floating leaves. It
checks exact charge-conservation identities, the initial-sector survival
exp(-16 kappa t), normalization, Hermiticity diagnostics and subsequent
birth probabilities. The largest stored trace error is 1.1102230246251565e-16.
The deliberate gate, loss and recycling mutations are documented separately.

The tree does not numerically sample arbitrary normal harmonic-field states,
and the finite torus controls do not replace the all-volume proof. Conversely
the rigorous cluster constants are not fitted to these diagnostics; most
diagnostic times exceed the deliberately loose sufficient window.

## 8. Evidence and remaining boundaries

SOURCE_PINS.json binds all allowed sources and procedural references.
Every run has an exact source hash, command, actual elapsed time, exit code,
and complete stdout/stderr under its own execution receipt. The four recorded
runs succeeded; failed proof routes and deliberate wrong-model discriminators
are retained in FAILED_ROUTES_AND_SCOPE.md. The verifier is genuinely read
only; the separate record_run.py is the explicitly named log writer.

The formal result is the finite-graph full-process covariance bound with
uniform local constants and its conditional normalized small-time limit.
No assertion is made about an infinite-volume process, a volume-uniform
Fourier remainder, long-time relaxation, a finite-spin energy law, physical
charge identification, or empirical agreement. All prior packets and
publication files remain unchanged. Stop after the PRE seal, before any
author47 release.
