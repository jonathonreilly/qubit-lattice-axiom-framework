---
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: In the chosen free-chain full-spin GNS, the actual scaled boost acts on even coefficient words by the proved lattice generator and converges in norm on each fixed even polynomial, uniformly on compact boost intervals, to the specified local Lorentz action.
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_id: microscopic_local_boost_limit_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: In the chosen free-chain full-spin GNS, the actual scaled boost acts on even coefficient words by the proved lattice generator and converges in norm on each fixed even polynomial, uniformly on compact boost intervals, to the specified local Lorentz action.
upstream_dependencies:
- concrete_gapped_chain_bounded_theorem_note_2026-10-12
- continuum_local_boost_bounded_theorem_note_2026-10-12
runner: scripts/microscopic_local_boost_limit_2026_10_12.py
artifact_role: theorem
claim_type_reason: Conditional supplied-model theorem with complete analytic argument and finite controls; source review does not confer retained status.
target_claim_id: null
target_blocker_text: compares that action to the actual scaled spin boost
source_of_blocker_text: handoff
next_trace_action: Compose the actual boost and cell estimate with time and rounded translations only for fixed finite words and their stated compact parameter sets.
---

**Type:** bounded_theorem


**Publication status:** The five exact source notes have completed separate-context source review and root integration for conditional composition. Original pending-review statements below describe the historical freeze and are superseded by this record. Mathematical arguments, failures and their original source identities are preserved. This is not an audit verdict or retained status.


# Actual microscopic even-spin boosts and their local continuum limit

**Author derivation, 2026-10-12.** This conditional theorem identifies the
literal scaled spin-GNS boost on the even algebra, bounds its discrepancy
from a continuum generator through physical cell averages, and proves an
O(a) norm limit for every specified finite even polynomial on compact boost
parameter intervals. The limiting region is a Lorentz-transformed double
cone of the specified continuum net. The source of that geometric
interpretation is an explicitly provisional continuum theorem below.

This is a supplied 1+1 dimensional free model. No physical parameter,
framework selection, odd-spin scaling field, full spin scaling net,
uniform operator-unit-ball limit, uniform microscopic spin locality bound,
interaction or higher-dimensional extension is asserted. Exact Lorentz
closure still fails at each nonzero lattice spacing.

## 1. Sources, open dependencies, and precise target

Write S for this directory and E for `microscopic_local_boost_limit/`.
The source copies and hashes in E are authoritative for this derivation.

| Source | SHA-256 | Exact role |
|---|---|---|
| `CONCRETE_GAPPED_CHAIN_PROBE.md` | `0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd` | Supplied actual spin model, state, even-CAR identification and canonical full-GNS boost, especially C13–C28 |
| `CONCRETE_GAPPED_CHAIN_REVIEW.md` | `7c554adcf96ce281128c560af453234b346147f725879c25df17bbd9bcdb7d94` | Root-accepted independent source review at that supplied-model scope |
| `LOCAL_EVEN_CONTINUUM_PROBE.md` | `7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b` | Sealed prior author construction; review pending at this freeze. Its elementary even-CAR embeddings are rederived here |
| `continuum_local_boost/frozen/CONTINUUM_LOCAL_BOOST_PROBE.md` | `9fc9cf7f203855faef12e63a9de355cdea525ad007c8ae27ada8c06509d62055` | **Open reviewed-status dependency:** L7, L14–L15, L22–L35 for the continuum Cauchy group, compact smooth orbits, and specified spacetime net |
| `ROOT_MICROSCOPIC_LOCAL_COVARIANCE_DIRECT_ROUTE.md` | `b7cb8ac2358dbb571711074c77b8dbc073fe70a6748fa4b0aa4de32ef804670e` | Proposed route and constants, critically reconstructed here; not proof evidence |
| `ROOT_MICROSCOPIC_LOCAL_COVARIANCE_LEAD.md` | `862fed4f20bcf35f24ee8bbcf8a577d803965b9e2828bb71a43548bfe512644e` | Alternative route and actual first-moment guidance; not proof evidence |

The already reviewed scalar group theorem
`GAPPED_CONTINUUM_LIMIT_PROBE.md`, hash
`617b9a1cbb541d6f207de89c10f1fbb2005fbb27f68e818f0c14a3fe67bf802d`,
is context, not a premise for the direct comparison below. In particular,
no Shannon/cell embedding comparison is needed. No general assertion about
boosted microscopic localization is imported from that scalar theorem.

The root and this author know the proposed formulas. Author calculations
are neither blind nor a separate-context independent review. The initial
complete argument and control protocol are frozen before any scientific
execution. Subsequent changes and failed controls must remain recorded.
The selected model/effort is unchanged, and no work is delegated.

Fix m,v>0, a>0, and define

    sigma_a=sqrt(m²/4+v²/a²),
    g_a=sigma_a/2+m/4,  J_a=sigma_a/2-m/4,
    c_a=2aJ_a=sqrt(v²+m²a²/4)-ma/2.

Then g_a>J_a>0, 2(g_a-J_a)=m, 4g_aJ_a=v²/a², and

    0<c_a≤v,  0≤v-c_a≤ma/2.                         (M1)

For the actual symmetric spin density
`h_n=-J_a X_nX_(n+1)-(g_a/2)(Z_n+Z_(n+1))`, use the parent's
state `omega_a=omega_0 o beta_a` and full-spin representation `pi_a`.
Let B_spin,a be its canonical vacuum-normalized self-adjoint first-moment
GNS generator. In the parent's sign convention

    pi_a(lambda_t^b(A))=exp(+it B_spin,a) pi_a(A) exp(-it B_spin,a).

The action studied here is specifically

    W_a(s)=exp(-is a B_spin,a),
    Xi_a(s)=lambda^b_(-as).                           (M2)

We will construct isometric maps Phi_a from the even spin C*-algebra into
one common continuum even-CAR algebra and, for each finite even polynomial
A_a built from cell averages of real compact smooth test vectors, show
`Phi_a(Xi_a(s)A_a)` converges in C*-norm uniformly for |s|≤S to its
continuum boost. The maps, polynomial, and parameter interval are specified
before a→0; this is not an intrinsic identification of all spin algebras.

## 2. Literal weighted spin matrix, domains, and band frame

Let K_a=ell²(Z;C²), with real subspace K_a,R, and use inner products
conjugate-linear in the first entry. The lattice Fourier map is

    (F_a psi)(q)=sqrt(a/(2pi)) sum_n exp(-ianq) psi_n,
    I_a=[-pi/a,pi/a], with periodic endpoints and Lebesgue measure dq.

X_a psi_n=an psi_n. The actual Hermitian coefficient matrix is

    (D_a psi)_(1,n)=2i(g_a psi_(2,n)-J_a psi_(2,n-1)),
    (D_a psi)_(2,n)=-2i(g_a psi_(1,n)-J_a psi_(1,n+1)),
    D_a(q)=-2J_a sin(aq) sigma_x
            -2(g_a-J_a cos(aq)) sigma_y.              (M3)

It satisfies D_a²=E_a²1, where
`E_a(q)²=m²+4v² sin²(aq/2)/a²`. With auxiliary Majoranas gamma=(a_n,b_n),
the finite identities `Z_n=-ia_nb_n` and `X_nX_(n+1)=-ib_na_(n+1)`
give

    h_n=iJ_a b_n a_(n+1)+(ig_a/2)(a_nb_n+a_(n+1)b_(n+1)).

In `a sum_n n h_n`, the onsite coefficient is
`iag_a(n-1/2)a_nb_n`, and the bond coefficient is `iaJ_a n b_na_(n+1)`.
For Q=(i/4)gamma^T A gamma, i[Q,gamma]=A gamma and the Hermitian
coefficient generator is iA. Thus on finitely supported coefficient data
the literal scaled first moment is

    B_a={X_a,D_a}/2-aD_a/2.                           (M4)

In particular its two components are exactly

    (B_a psi)_(1,n)=i[m(x_n-a/2)psi_(2,n)
                  +c_a(x_n-a)nabla_-psi_(2,n)+(c_a/2)psi_(2,n)],
    (B_a psi)_(2,n)=i[-m(x_n-a/2)psi_(1,n)
                  +c_a x_n nabla_+psi_(1,n)+(c_a/2)psi_(1,n)],
    x_n=an, nabla_-psi_n=(psi_n-psi_(n-1))/a,
    nabla_+psi_n=(psi_(n+1)-psi_n)/a.                  (M5)

Boundary warning with an exact formula: for a finite open chain [L,R]
and the literal sum `a sum_(n=L)^(R-1) n h_n`, its Majorana matrix equals
the principal [L,R] block of M4, plus onsite 12-entry corrections
`iag_a(1-L)` at L and `-iag_a R` at R, with conjugate 21 entries.
This follows because the endpoint onsite coefficients are `iag_a L/2`
and `iag_a(R-1)/2`, rather than the interior formula. The controls retain
these corrections; only padded interior action directly tests M4 without
them. The infinite first-moment sum is not a norm-convergent observable.

For completeness, fix the actual parent phase rather than an arbitrary
eigenvector. Let C_0=-sigma_y, e_+=(1,-i)^T/sqrt(2), e_-=conj(e_+), and

    theta_a(q)=arg(g_a-J_a exp(-iaq)),
    R_a(q)=exp(i theta_a(q) sigma_z/2),
    u_(a,±)=R_a e_±,
    (J_a psi)_±=u_(a,±)^* F_a psi.                    (M6)

The argument has positive real part for all q, so theta_a is a smooth
odd periodic real function. Direct multiplication gives
`D_a=E_a R_a C_0 R_a*`, `u_±*u_±'=0`, and
`u_(a,-)(q)=conj(u_(a,+)(-q))`. J_a is unitary to two scalar bands.
In Fourier space M4 is `iD_a partial_q+iD_a'/2-aD_a/2`. Its connection
term after conjugation by R_a is
`(iE_a/2){C_0,R_a*R_a'}`; it vanishes since `R_a*R_a'=i theta_a' sigma_z/2`
anticommutes with C_0. Consequently on smooth periodic functions

    J_a B_a J_a*=b_a^0 oplus (-b_a^0),
    b_a^0=i(E_a partial_q+E_a'/2)-aE_a/2.             (M7)

This also proves positive-band preservation; it was not inferred from a
formal commutator alone. Write `r(q)=int_0^q du/E_a(u)` on the circle.
The unitary coordinate change `psi(q) -> sqrt(E_a(q(r))) psi(q(r))`
sends b_a^0 to `i partial_r-aE_a(q(r))/2` on a circle of finite length
`int_Ia dq/E_a(q)`. The bounded real potential preserves the self-adjoint
periodic H¹ derivative domain. Smooth coordinate changes and multiplication
by sqrt(E_a) preserve H¹ with equivalent norms at fixed a. Therefore

    Dom b_a^0=H¹_per(I_a),
    Dom B_a=F_a^* H¹_per(I_a;C²)
           ={psi: sum_n (1+n²)|psi_n|²<infinity}.     (M8)

Both smooth periodic functions and trigonometric polynomials are cores;
the graph norm is equivalent to H¹ at fixed a by the displayed coordinate
change and frame. Thus finite-position data are a core for B_a and M4–M5
identify its unique closure. No uniform-in-a graph norm equivalence is
asserted, and no product-domain intersection defines the final domain.
Position conjugation C_a^real anticommutes with B_a, so
`Z_a(s)=exp(-isB_a)` preserves real coefficient data.

## 3. Identification with the actual full-spin GNS boost

The parent proves a full-spin statement, not just a two-band calculation:
in its product-Fock coordinates, `pi_a=pi_0 o beta_a`, and
`B_spin,a=dGamma(b_parent,a)`, with
`b_parent,a=i(E partial_k+E'/2)-E/2` and its periodic domain.
Its proof uses the actual spin weighted-flow cutoff, the even-algebra lift,
vacuum invariance, and finite-particle cores. Those established hypotheses
are the imported supplied-model premise here; M4 alone would not replace it.

Under the scalar unitary `psi(k) -> sqrt(a/(2pi)) psi(aq)`, the operator
`a b_parent,a` becomes exactly b_a^0 in M7. Thus in the same actual GNS
representation, after this unitary one-particle reparametrization,

    W_a(s)=Gamma(exp(-is b_a^0)).                     (M9)

No scalar vacuum phase is left: the parent generator and the displayed
second quantization both annihilate the vacuum. Its full domain is the
Hilbert direct sum of the maximal closed sector sums, not an intersection
of individual particle domains. Restriction to even particle number takes
the corresponding sectors of the same self-adjoint operator.

Here is the coefficient/creation check that fixes the group sign. In the
reference product vacuum `c_n=(a_n+ib_n)/2` annihilates, and
`c_n*=(a_n-ib_n)/2` creates. Therefore for real coefficients f,

    sum_n(f_(1,n)a_n+f_(2,n)b_n)
       =c*(f_1+i f_2)+c(f_1+i f_2).

The scalar amplitude is `sqrt(2)e_+* f=f_1+i f_2`. The parent's beta_a
acts on the field column by R_a, so on coefficients it acts by R_a*.
For real f define the auxiliary bounded GNS field

    c_a^GNS(f)=a*(sqrt(2)(J_a f)_+)+a(sqrt(2)(J_a f)_+).  (M10)

This has covariance `2<f,P_(a,+)g>`, where P_(a,+)=(1+D_a/E_a)/2.
Its even finite products are exactly pi_a of their even Jordan–Wigner
spin polynomials, by the finite identities and continuity of beta_a.
Odd M10 fields are representation tools, not claimed bilateral quasilocal
spin elements. Second quantization sends M10 to
`c_a^GNS(Z_a(s)f)` because M7 gives its positive amplitude
`exp(-is b_a^0)(J_a f)_+`. The negative band is forced by reality: its
generator is -b_a^0, and conjugation together with q reflection exchanges
the two bands. Hence for every even product, and then by norm closure,

    W_a(s) pi_a(jw_a(product_j c_a(f_j))) W_a(s)*
       =pi_a(jw_a(product_j c_a(Z_a(s)f_j))).          (M11)

For initially finite f_j this equality concerns actual spin observables.
For general ell² data the even products are norm limits of finite ones.
The parent GNS representation is faithful: the full spin UHF algebra is
simple and its unital representation is nonzero. Alternatively its even
restriction has the same norms by the CAR isomorphism below and simplicity
of the infinite even CAR algebra. We use the first argument. Combining M2,
M9 and M11 identifies the actual Xi_a(s) on the even spin algebra, rather
than replacing it by a separately postulated quadratic evolution.

The onsite test J=0 is a useful sign check (outside the strict J>0 family,
but a finite algebra identity): for Q=-ag(n-1/2)Z, conjugation by exp(-isQ)
sends X to `cos(2ag(n-1/2)s)X-sin(2ag(n-1/2)s)Y`. This agrees with
the coefficient group exp(-isB_a). It is the opposite parameter to the
parent Heisenberg boost automorphism lambda^b_(as).

## 4. Physical cells and the weighted consistency estimate

Put K=L²(R;C²), with real part K_R, and define

    (C_a f)_n=a^(-1/2) int_[an,a(n+1)] f(x) dx,
    (j_a psi)(x)=a^(-1/2)psi_n on [an,a(n+1)).         (M12)

Cauchy–Schwarz gives ||C_a||≤1; direct integration gives C_a j_a=1,
so j_a=C_a* is isometric and Q_a=j_a C_a is the cell projection.
The one-cell Poincare estimate, or the integral fundamental theorem and
Cauchy–Schwarz, gives

    ||(Q_a-1)f||≤a||f'||,  f in H¹(R;C²).            (M13)

In particular Q_a→1 strongly by density. Real functions remain real.
If f has compact support in I, C_a f has finite support and its physical
cell union lies inside the enlargement of I by a in each direction.

The continuum generator is

    D=i v sigma_x partial_x-m sigma_y,
    B={X,D}/2=i v sigma_x(x partial_x+1/2)-mx sigma_y. (M14)

Initially this is a differential expression on compact smooth data.
Its self-adjoint closure and real unitary group
`Z(s)=exp(-isB)=V_(vs)` are the frozen continuum result L14–L15.
That result gives the full domain through the parallel bands
`b=i(E partial_q+E'/2)`, using
`r=v^(-1)arsinh(vq/m)` and the full H¹(R,dr) derivative domain. It also
proves compact smooth Cauchy data are a core, by a Schwartz band core
followed by spatial cutoffs. No finite endpoint extension is imported.

For the estimate, use the explicit domain class

    W={f in H²(R;C²): xf,xf',xf'' in L²(R;C²)}.

Then Bf exists in L² by M14, and C_a f lies in Dom B_a by M8: cellwise
`|an|≤|x|+a` and Jensen give `||X_a C_a f||≤||xf||+a||f||`.
The condition xf is needed for these domains even though it does not occur
in the final error bound. All compact smooth data belong to W.

Whole-cell translations commute with C_a. Hence
`nabla_± C_a f=C_a Delta_± f`, where Delta_± are the continuum forward
and backward differences of step a. Integral Taylor remainders give

    ||Delta_± f||≤||f'||,
    ||x(Delta_± f-f')||
        ≤(a/2)||xf''||+(a²/6)||f''||.                (M15)

For example `Delta_-f-f'=-(1/a)int_0^a int_0^s f''(x-u)du ds`.
The triangle inequality and
`||x f''(x-u)||≤||xf''||+u||f''||` give respectively the integrals
a/2 and a²/6. The forward sign has x+u and the same estimates. If opposite
translations are chosen in the two components, diagonal translation remains
a vector isometry and the identical Minkowski argument applies. There is
no extra sqrt(2) and no sum of separate component norms.

Compare M5 cell by cell with M14. For the first derivative coefficient
`an-a`, its distance from x in its cell is at most 2a; for `an` it is
at most a. Separate the derivative error into the three contributions

    c_a(coefficient-x)Delta_±f,
    c_a x(Delta_±f-f'),
    (c_a-v)xf'.

Their norms are bounded, respectively, by
`2va||f'||`, `va||xf''||/2+va²||f''||/6`, and `ma||xf'||/2`.
The mass location `an-a/2` differs from x by at most 3a/2; its error is
at most `3ma||f||/2`. Finally the half-density coefficient difference
`(c_a-v)/2` contributes at most `ma||f||/4`. Component exchange and the
mass sign matrix are isometries; C_a is a contraction on each vector
error. Summing proves, for every f in W,

    ||B_a C_a f-C_a Bf||≤a R_a(f),
    R_a(f)=(m/2)||xf'||+(v/2)||xf''||+2v||f'||
             +(7m/4)||f||+(va/6)||f''||.             (D1)

This is a safe bound, not an asserted optimal constant. In particular an
O(a) origin change can still satisfy a bound of this size. Literal origin
identification therefore requires M4 and the actual-spin control, not a
convergence plot or D1 alone.

## 5. Quantitative compact-orbit group comparison

Let f be real C_c^infinity and fix S<infinity. The continuum theorem gives
`Z(s)=V_(vs)=U_(-vs)` with

    (U_eta f)(x)=exp(-eta sigma_x/2)
       (exp(itD)f)(y),
    t=(x/v)sinh eta,  y=x cosh eta.                 (M16)

It proves this is a real unitary group and that if supp f⊂[-R,R], all
Z(t)f for |t|≤S have support in `[-R exp(vS),R exp(vS)]`.
The solution formula is smooth jointly in the parameter and position;
therefore all derivatives required in W and all their weighted L² norms
are bounded on that common compact set, uniformly for |t|≤S. This is the
specific regularity input needed here, not a general assertion that arbitrary
unbounded generators preserve every core.

For each fixed a, the vectors C_a Z(t)f have common finite lattice support,
are continuously differentiable in t, and vary continuously in the B_a
graph norm. Their derivative is `-i C_a B Z(t)f`. Differentiate
`exp(-i(s-t)B_a) C_a Z(t)f` in the Hilbert space and integrate, first for
s≥0 and then with reversed orientation for s<0. Using M8 and D1 gives

    ||Z_a(s)C_a f-C_a Z(s)f||
       ≤a int_0^|s| R_a(Z(sign(s)t)f) dt.            (M17)

At s=0 the integral is zero. After the isometric cell embedding and M13,

    ||j_a Z_a(s)C_a f-Z(s)f||
       ≤a ||(Z(s)f)'||
          +a int_0^|s| R_a(Z(sign(s)t)f) dt.         (D2)

For 0<a≤a_0, define the finite constant

    K_(f,S,a0)=sup_(|s|≤S)||(Z(s)f)'||
                   +S sup_(|t|≤S)R_(a0)(Z(t)f).

Then D2 is at most a K_(f,S,a0), uniformly on the stated interval.
There is no uniform bound over all unit vectors. Because j_a,C_a are
contractions and both groups are unitary, approximation of an arbitrary
real L² vector by compact smooth data gives

    sup_(|s|≤S)||j_a Z_a(s) C_a f-Z(s)f|| -> 0
    for every f in K_R.                             (M18)

Indeed the two errors on the approximating difference sum to at most
2||f-f_epsilon||, independently of a and s. No rate on general L² is
claimed. This direct argument does not require a Brillouin boundary
condition for zero extensions or an alias estimate.

## 6. Even spin locality and isometric common embeddings

For a finite interval [L,R], set
`gamma_(1,n)=(prod_(j=L)^(n-1)Z_j)X_n` and the analogous expression with
Y_n for gamma_(2,n). These Majoranas generate the finite spin matrix
algebra and satisfy the real CAR. Their even products are exactly the
spin polynomials even under simultaneous X,Y sign change. Enlarging the
left endpoint multiplies every old gamma by the same exterior parity
string, which commutes with the old interval. In an even product it
cancels; in an odd product it does not. Enlarging the right endpoint is
immediate. Thus the finite even identifications are compatible and
isometric, and their completions give

    jw_a: CAR(K_a,R)^even -> spin^even.              (M19)

An even word of finite coefficient support is a genuine spin observable
in the interval hull of that support. Arbitrary even CAR elements are
norm limits of such local even polynomials. This establishes exactly the
bilateral even correspondence; it does not assert an odd spin embedding.

Use the continuum CAR with real self-adjoint c(f) satisfying
`{c(f),c(g)}=2(f,g)_R`, `||c(f)||=||f||`. It may be represented by
the positive-band vacuum fields L22 of the continuum parent. For finite
dimensional real coefficient subspaces of even dimension, the Clifford
algebra is a full matrix algebra. Every real isometry induces a unital
CAR homomorphism, and on such a full matrix algebra it is injective and
isometric. Enlarging to even-dimensional subspaces and taking the norm
completion proves the isometric embedding induced by j_a:

    iota_a(c_a(f))=c(j_a f),
    Phi_a=iota_a o jw_a^(-1): spin^even -> CAR(K_R)^even. (M20)

This proof uses the full CAR embedding before restricting to its even
part; it does not incorrectly infer simplicity for a finite even Clifford
algebra. The continuum positive Fock representation is faithful for this
CAR: its restriction to each even-dimensional full finite Clifford
subalgebra is a nonzero unital representation, hence isometric, and the
union is norm dense. Thus M20 computes the same norms in that representation.

For real compact smooth f_1,...,f_(2r) supported in a bounded open I, set

    A_a=jw_a(product_(j=1)^(2r)c_a(C_a f_j)),
    A=product_(j=1)^(2r)c(f_j),
    M_A=product_j||f_j||.                            (M21)

A_a is an actual finite even spin polynomial supported in the cell
enlargement of I and ||A_a||≤M_A. It need not be self-adjoint; real and
imaginary parts have the corresponding observable statement. Equations
M11 and M20 give the exact identity

    Phi_a(Xi_a(s)A_a)
      =product_j c(j_a Z_a(s) C_a f_j).               (M22)

The elementary product telescoping inequality and the field norm identity
yield

    ||Phi_a(Xi_a(s)A_a)-product_j c(Z(s)f_j)||
      ≤sum_j epsilon_a(f_j,s) product_(k!=j)||f_k||,
    epsilon_a(f,s)=a||(Z(s)f)'||
       +a int_0^|s| R_a(Z(sign(s)t)f) dt.             (M23)

This is O(a) uniformly for |s|≤S, with explicit finite constants above.
Finite linear combinations obey the sum of these bounds weighted by the
absolute polynomial coefficients. Constants map to constants. Completion
also gives pointwise convergence for any separately controlled polynomial
approximation, but no uniform statement on a local operator unit ball or
an intrinsic identification of entire spin local algebras follows.

## 7. Exact limiting region, conventions, and preserved limits

The continuum parent defines the net, rather than inferring it from a
one-particle dispersion: for real compact smooth spacetime H put
`kH=int exp(-itD)H(t,.)dt`, `Phi(H)=c(kH)`, and let A(O) be the norm
closed even polynomial algebra generated by sources supported in O.
For `I=(l,r)` put `D(I)={(tau,x):l+v|tau|<x<r-v|tau|}`.
Its time-slice identity is

    A(D(I))=CAR(L²(I;R²))^even.                      (M24)

It follows using finite propagation: kH for sources inside D(I) is
supported in I; conversely a compact smooth f in I is kH for
`H(t,x)=chi(t)(exp(itD)f)(x)` with integral chi=1 and sufficiently
small time support. The exact norm identity extends to L²(I).

With `Lambda_eta(tau,x)=(tau cosh eta+(x/v)sinh eta,
x cosh eta+v tau sinh eta)`, the parent's source transformation is
`H_eta(z)=exp(-eta sigma_x/2)H(Lambda_-eta z)`.
Its duality/flux proof gives `kH_eta=V_eta kH`. Because this is an
invertible test-source transformation, both inclusions hold in

    Vcal_eta A(O) Vcal_eta*=A(Lambda_eta O),
    Vcal_(vs)=Gamma(exp(-is b)).                    (M25)

M16 and the positive-band generator identify our Z(s) with V_(vs), so
the limit in M23 is the continuum boost of A and belongs to

    A(Lambda_(vs) D(I)).                             (M26)

M24–M26 use precisely the frozen continuum-local-boost theorem whose
independent review was still pending at this freeze. A later review must
bind to its exact hash and check the domain, real structure, and source
duality; a successful numerical bound here does not certify that net.

The coordinate-time convention is explicit. The actual chain Heisenberg
time has positive-band implementer `Gamma(exp(+itE))`. The source-net
translation by tau has `Gamma(exp(-i tau E))`. Therefore tau=-t.
The boost in M2 and M26 has eta=vs. Neither sign is interchangeable with
the raw solution pullback U_(vs) or the spin automorphism lambda^b_(as).

The continuum fields satisfy spacelike graded locality from finite speed v;
the even net commutes at spacelike separation. M23 can therefore be used
for finitely many constructed boosted polynomials whose limiting double
cones are strictly spacelike separated: their actual spin commutator norms
tend to zero by the same finite-product estimate and the isometric Phi_a.
No exact finite-a vanishing or uniform microscopic support bound is claimed.

Parity remains substantive. The full supplied spin-GNS space is full Fock,
whereas the cyclic space of the global even vacuum algebra is F_even.
All M21–M26 actions preserve the latter; an even polynomial cannot create
a one-particle state from the vacuum. The underlying gap is m, and the
nonvacuum even-sector threshold is 2m. No odd local spin-field limit has
been constructed by writing auxiliary Majoranas.

Finally the supplied finite-spacing current/stress bracket retains its
cos(aq) factor; the nonzero spacing model has not acquired exact Lorentz
Lie closure. The theorem concerns a chosen continuum family and specified
observable sequences. It does not exclude other choices or select this
family from the framework. Mixed finite compositions of time, translations
and boosts, general vacuum correlation limits, and exhaustion of a full
spin scaling net are not part of the claim of this note.

## 8. Frozen controls and review handoff

The complete analytic argument above is to be frozen together with
`microscopic_local_boost_limit/CONTROL_PROTOCOL.md` before scientific runs.
The principal controls reconstruct literal finite spin matrices and compare
weighted cell integrals by a different arithmetic route. A whole-flow
comparison uses finite sparse matrix exponentiation and a variable-time
continuum solution integral, not just D1 evaluated twice. Floating results
are diagnostics; M8–M11 and D1–D2 are proved analytically above.

All helpers, source variants, numerical refinements, complete output and
error streams, interpreter/library versions, actual subprocess timeouts,
and failures or surviving mutations belong in E. Author checks do not
replace the requested fresh independent review. Root retains all Git,
publication and audit decisions. No prompt, axiom or prior sealed packet
is modified by this task.

## 9. Post-freeze clarification, actual controls, and final handoff

The original complete §§1–8 are unchanged byte for byte from the initial
freeze, SHA `7e7c127faf6ceb0fc799252c6aedfcc0a233f2117307c07f8ff03e25212e2240`.
The initial protocol SHA is
`b8d21e2555c95af29548c8c1e87e5d95e3b038c04b5b14c5ae18a0b0aa42d431`.
This appended section records subsequent clarification and actual evidence.
It does not replace the frozen pre-execution argument or its historical
review-pending statements.

**Closed-domain clarification.** Root's full proof read requested an
explicit justification at the definition of W in §4. For f∈W the
displayed differential expression B_form f lies in L². Integration by
parts against every h∈C_c^infinity gives
`<B_initial h,f>=<h,B_form f>`, so f∈Dom(B_initial*) and
`B_initial* f=B_form f`. The frozen continuum theorem proves B_initial
essentially self-adjoint on that test domain. Hence B_initial*=B and
f∈Dom B with the stated expression. This clarification was separately
frozen in [DOMAIN_ADDENDUM.md](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/a8ab3f49038327e3080d2f93afb7e34601459928/.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json)
before any scientific run; its SHA is
`b85803ad92cb1c461def6ddf9352511785a2ab1ca172f08a63bb5e5b7fae1207`.
No formula, bound, premise or tolerance was changed.

There were five baseline calculations, thirteen targeted mutant runs and
two complete-vector refinement comparisons, each under an actual 60-second
subprocess limit. The baseline row counts are 16 literal-spin, 120 weighted
cell, and 47 in each of three whole-flow resolutions. These baseline
predicates all passed. Numerical agreement remains author evidence, not
an infinite-dimensional proof or an independent review.

* Literal finite Pauli first moments, commutator-extracted coefficient
  matrices, and full even-spin conjugations agree with M4/M11 to at most
  `2.45e-15` in the reported matrix residuals. The finite-open endpoint
  corrections and both boost signs were exercised. The tested odd endpoint
  changes have operator norm 2; the even changes are zero.
* For m=.8,v=1.3 and a=.4,.2,.1,.05,.025, the four compact polynomial
  fixtures include centers 8 and 200 to stress the weighted terms. The
  largest D1 residual/bound ratio is .903368. The two cell integration
  routes differ by at most `4.53e-13`. The integral Taylor remainders are
  also tested separately. These polynomial fixtures are C5 and in W;
  they are not mislabeled C_c^infinity.
* Whole-flow data compare literal finite-open sparse exponentiation with
  the variable-time continuum Fourier solution. At s=-.27 the high-resolution
  embedded error decreases from .339169 at a=.4 to .0295542 at a=.025;
  at s=+.27 it decreases from .277905 to .0218405. Each lies below D2's
  independently integrated bound. The highest reference uses Q=96,
  2816 Fourier nodes, 640 physical quadrature nodes and spatial box 10.
  Its tested outside-support residual is below `1.78e-10`. Floating
  quadrature, spectral tails and finite boxes are not rigorous total-error
  certificates, and a fitted convergence rate is not used as the proof.

The initial Q=40/box6 to Q=64/box10 comparison **failed three of twenty
rows** at the frozen `3e-7` full-vector threshold; its largest continuum-cell
difference was `3.570496035751336e-7`. All lattice-flow differences were
at most `1.015e-15`. One further resolution was registered before execution
in [REFINEMENT_ADDENDUM.md](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/a8ab3f49038327e3080d2f93afb7e34601459928/.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json).
It changes only the fine settings tuple in a separately preserved copy,
keeps box10, and uses the same threshold. Fine-to-high continuum-cell
differences are at most `1.5670314140905884e-8`, and all twenty rows pass.
Both the failed and successful comparisons and every full vector remain
in the packet. The comparison helper's generic limitation text says the
box and quadrature change together; that applies to the first comparison.
The actual recorded settings show the second comparison holds the box fixed.

All nine source variants are detected somewhere in their preregistered
targeted suite. The following counts describe evidence coverage, not a
proof by counting successful controls:

| Source variant | Failing predicates / tested predicates | Surviving limitation |
|---|---|---|
| Half-site origin reversed | spin9/16; weighted0/120 | **Entire weighted suite survives.** The literal spin matrix fixes this O(a) origin |
| Group parameter reversed | spin5/16; flow5/47 | Several coarse-spacing D2 bounds remain too loose to discriminate |
| Cell power -1 instead of -1/2 | weighted75/120 | Some coarse D1 rows survive; physical normalization and right inverse do not |
| Mass sign reversed | spin9/16; weighted7/120 | Many loose weighted rows survive; broad displaced packets discriminate |
| Space sign reversed | spin8/16; weighted15/120 | Coarse rows may survive |
| Half-density term omitted | spin10/16 | Unrelated family/parity rows survive; self-adjointness fails |
| Weighted second derivative omitted from R_a | weighted9/120 | Off-grid and broad fixtures survive; narrow displaced data discriminate |
| Weighted first derivative omitted from R_a | weighted5/120 | Only the broad displaced fixture discriminates at all five spacings |
| Finite-open endpoint corrections erased | spin6/16 | Interior rows survive exactly; full literal finite matrices and flows fail |

The complete result rows, unchanged and passing mutant-row indices, source
diffs and numerical values are retained in `all_result_rows.json`,
`result_disposition.json`, `inspection_rows.jsonl` and the individual raw
run files. There were no timeouts or baseline repairs. The higher-resolution
copy changes one settings tuple only. All scientific source hashes matched
before and after their runs. Three isolated corruption controls—source,
helper, and helper plus self-rebound manifest—were rejected before
mathematical dispatch against the external execution-manifest digest.
These identity checks are separate from scientific checks.

The recorded runtime is Python3.13.5, NumPy2.4.4, SciPy1.17.1 on
macOS26.6.2 arm64, with the actual interpreter and complete streams in
each receipt. Scientific subprocess durations range below five seconds
on this host; every recorder enforces timeout=60. Initial source-reading
tool calls predate the recorder and have no fabricated process metadata.
The first combined continuum-source display was truncated, followed by
complete separate reads of its lines1–616. Root proposal text is preserved
as exposure/context, not treated as evidence of its own correctness.

Root subsequently reported that the unchanged local-even theorem passed
its fresh review: `LOCAL_EVEN_CONTINUUM_REVIEW.md` SHA
`52367af926771b082f898782ebb22ffcfc332d9ac4aad35812c0cf8e5c0d26e8`;
review receipt `36607e5a9a60518fb98e2ae8072e107193dc63ba62cd5273baf49a259d5eb1cc`;
root coverage `57563c2b2a88fb5bcdb9ee7e9c0b015d04657c92cbc64bddda9fa5da335f1e78`.
That does not retrospectively alter the initial freeze or establish this
new theorem's review status. At this handoff the continuum local-boost
source's fresh review remains an explicitly open dependency, and the new
microscopic bridge requires its own independent review. No retained or
Lean-verified status, physical identification, or full scaling-net result
is asserted. Root owns integration and any publication or audit action.


## Publication evidence, imports and review record

**Author/checker pairing:** Same selected model family and reasoning effort; separate reviewer contexts with formula exposure, not blinded or diverse-family. Root supplied routes and is a coauthor; the section note is root-authored. Mechanical preparation and reproduction add no independent scientific review.

The original three failed refinement predicates remain at the unchanged 3e-7 gate, followed by the declared higher resolution. The wrong-origin weighted-consistency and reverse-origin spectrum survivors remain. The local-even elementary embedding is rederived here; the scalar continuum group note is explicitly context. No operator-unit-ball or uniform microscopic-locality claim follows.

The exact original note, source review, root coverage, all author/reviewer helper sources, complete results, rejected controls, survivors, timeouts and recording repairs are preserved through the [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/a8ab3f49038327e3080d2f93afb7e34601459928/.claude/science/physics-loops/toe-local-continuum-20261012/EVIDENCE_MAP.json). Original source paths and SHA values identify frozen probes. The [literal publication map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/a8ab3f49038327e3080d2f93afb7e34601459928/.claude/science/physics-loops/toe-local-continuum-20261012/PUBLICATION_EDITS.json) reconstructs the entire canonical note and runner without mathematical edits. Historical evidence is not relabeled as a new independent check.

Direct mathematical imports, each at the supplied scope stated in the original argument:

- [concrete gapped chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md).
- [continuum local boost](CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md).

The chosen free one-dimensional dynamics, positive m and v, scaling, quasifree state, CAR machinery and cell comparison are stated hypotheses or constructions; the framework does not select these data. There is no empirical prediction, interacting or three-dimensional result. Broader spin-scaling classification remains a separate question.

All mathematical helper sources and imported finite refinement specimens are explicit primary inputs. No helper registry or dependency-policy edit is proposed. Canonical execution, vocabulary, graph comparison and focused compatibility are pending root execution; global combined pipeline and strict audit lint are independent landing gates.

The historical continuum premise is the frozen original boost argument. The canonical dependency is its accepted revised source: the only mathematical narrowing is the separately reviewed smooth-gauge condition in L19, and no L19 rough-gauge differential identity is used here. Elementary local-even embeddings are rederived; the scalar group note is context, so neither creates an additional direct edge.
