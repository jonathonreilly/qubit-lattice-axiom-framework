# Conditional Gaussian coordinates for the normalized soft gauge step

Author proof unit in the supplied four-dimensional SU(N) Wilson / normalized
paired S4′ model. **At the fixed coarse field V=I, a local block-tree quotient
has an explicitly positive, volume-uniform quadratic precision, including the
finite-u normalizer and Haar terms.** Its inverse and inverse square root have
uniform exponential bounds. An exact change of variables identifies the
restricted actual Haar integral, its cuts, sources, vacuum factor and Gaussian
determinant with an expectation over independent Gaussians. The expectation's
nonlinear and hard-cut factors remain present.

This is a bounded theorem awaiting independent review. The covariance below
is the **Gaussian covariance of the quadratic reference**, not the covariance
of the full interacting conditional law. Full Yang–Mills existence and the
physical continuum mass gap remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual normalized one-step identity-background quadratic precision, local quotient coordinates, Gaussian localization bounds and exact restricted-density representation."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Target, prior results and consumed contract

Fix `d=4`, `N>=2`, odd `L>=3`, `T>=2`, `u>=1`, and
`0<kappa_-<=kappa<=kappa_+<infinity`. The fine torus has side `LT`, with
centered blocks `B_X=LX+{-(L-1)/2,...,(L-1)/2}^4` and roots `LX`.
Fine and coarse links use normalized probability Haar. All scalar adjoints
below use ordinary counting norms; the Lie algebra has
`<A,B>=Re tr(A*B)`, with an orthonormal real basis of dimension `D=N^2-1`.
Only the identity coarse field is treated. No arbitrarily frozen exterior,
punctured region or general curvature-small coarse field is included.

The actual density is exactly [H1–H5](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md),
with every coarse link fixed at I:

    w_0(U;I)=exp[-u sum_p s(U_p)] product_c k_t(I;M_c(U)),
    s(U)=1-Re tr(U)/N,
    k_t(V;M)=exp[-t(1-Re tr(V^-1 M)/N)]/N_t(M),
    N_t(M)=int exp[-t(1-Re tr(W^-1 M)/N)]dW,  t=kappa u.

`M_c` is the arithmetic mean of all `24L^4` actual paired S4′ contour
transporters, using the same coordinate order at the two endpoints. Each
contour stays in the two endpoint blocks and has length at most `5L-4`.
The sources are the original Wilson coefficients
`delta S_epsilon=u sum_p epsilon_p s(U_p)`; the kernel coupling stays real
and fixed. The cut is the original product of **cube-interior** plaquette
indicators in H3. It is not the stronger all-plaquette reference `Z_delta`.
The complete new [sea construction](SOURCE_SEA_CONSTRUCTION_ASTRA.md) and
H1–H28 were read. Sea7/11/14/15 are integrated-coarse reference estimates;
none is used as a fixed-V mixing assertion here.

There is substantial prior covariance mathematics. [LINEAR_PACKAGE](LINEAR_PACKAGE.md)
§1.3, Lemma6.1 and Propositions6.2–6.4 give the classical quadratic chain, admissible linear
Faddeev–Popov fixing and a uniform one-step gap in its `h/P_res` coordinates.
`PROOF.md`'s N5 and RW results already give gauge-fixed covariance and
square-root constructions. [STEP55](STEP55.md) §§2–4 and
[its independent review](CODEX_REVIEW_STEP.md), particularly R1/R4/R6/R7/R9–R11,
separate the `1/38` lower bound on minimized **coarse curvature energy**, the
one-step precision, the exact normalizer correction and the remaining
actual-integral identification. The `1/38` result is not being reproved or
used as a conditional inverse. The preceding
[soft-minimizer note](UNIFORM_SOFT_MINIMIZER_ASTRA.md) supplies top-data maps
for its normalized classical phase; its corrected scope explicitly excludes
the exact finite-u logdensity Hessian.

The new bridge here is the explicit **local tree-coordinate** precision for
the actual normalized density, its full finite-u and Haar dictionary, and the
exact integral with its complements retained. Positivity of a soft step or
exponential decay of a gapped finite-range matrix is not claimed as a new
general theorem. The narrow current-main search used immutable coordinator
revision `ca2bc7ddf64790da96cd43d42017d000fbfe4808`; matching branch originals,
not absence of a main hit, determine this prior-art classification. Exact
read ranges and source bytes are in the input manifest. The coordinator owns
git, PR #10114, locks, shared summaries and audit authority. This author owns
only this note and `checks/soft_fluctuation_*`.

## 2. A local group quotient, with its measure and all root modes

Inside each block choose the complete axial tree with coordinate order
`1,2,3,4`. Equivalently the parent of a nonroot site moves its highest-index
nonzero coordinate one step toward zero. A root-to-site tree path has length
at most `2(L-1)`. Let `mathcal T` be the union of these trees and `E_*` the
remaining positive links. There are

    |mathcal T|=(L^4-1)T^4,
    |E_*|=m_0 T^4,       m_0=3L^4+1.                         (F1)

For every group configuration U there is a unique root-pinned gauge
transformation g, `g(LX)=I`, making every tree link I. Construct g successively
from the root along each tree. Write W for the transformed non-tree links.
The inverse reconstructs U from g and W. Successive leaf/tree integrations,
using left and right Haar invariance, prove the **exact measure identity**

    product_b dU_b = product_(x not a root) dg_x
                    product_(e in E_*) dW_e.               (F2)

No nonconstant Faddeev–Popov determinant occurs in these group coordinates.
The pinned gauge volume is one. Equivalently the scalar linearized tree
incidence minor with root column removed is triangular unimodular after
ordering vertices by depth. Its determinant is not a determinant of an
orthogonal horizontal projection. We do not insert the `h/P_res` slice's
Gram factors into this different change of variables.

All Wilson traces, original cuts, sources and `M_c` are invariant under this
root-pinned transformation. Thus (F2) applies directly to their global
fixed-I integral. A nongauge-invariant insertion must keep its g-average;
only gauge-invariant insertions can simply be evaluated on W. No local H4
integral with arbitrary frozen collar links is transformed by this statement.

Let `J:R^(E_*) -> R^(fine links)` insert zeros on the tree links. It is a
local isometry in **counting coordinates**. `A=Ja` parametrizes the linear
slice. Root gauge variables are not further quotiented: at fixed V their
nonzero coarse differences are charged. The global constant gauge parameter
has zero tangent at the identity; it does not supply a missing link coordinate.

There are four harmonic one-forms per colour. A constant fine form v has
`Q_root v=Lv` and the inherited horizontal quotient `kappa/L^2`. Its tree
representative is zero on internal links and `Lv_mu` on every crossing face
link. The latter has quotient `kappa/L^3` in the Euclidean tree-coordinate
norm. This difference is the metric change of the representative. For a
block-constant scalar lambda, its tree-slice gradient is supported on crossing
links and satisfies

    ||d lambda||^2=L^3||d_c lambda||^2,
    Q_root d lambda=d_c lambda.                            (F3)

Thus the long-wave root-gradient quotient is also `kappa/L^3`, independent
of wavelength when the tangent is nonzero. At `kappa=0`, the tree slice still
contains the coarse exact forms and four harmonics: on the full torus the
closed slice has dimension `T^4-1+4` per colour. They are never deleted to
make a gap. Before quotient, `d*d+kappa Q*Q` has precisely `(L^4-1)T^4`
root-pinned gauge zero directions per colour when kappa>0.

## 3. The exact finite-u quadratic law

For a linear variation A, let `theta_(c,tau)(A)` be the signed sum of A along
the actual contour and put

    q_c(A)=average_tau theta_(c,tau)(A)=Q_root A(c),
    z_(c,tau)(A)=theta_(c,tau)(A)-q_c(A),
    <A,B_sp A>=sum_c average_tau ||z_(c,tau)(A)||_HS^2.     (F4)

`B_sp` is positive semidefinite. All these maps are local, and their path
labels and averaging factors are retained.

Define the single-link tilted expectation

    E_t f = [int f(W) exp(t Re tr W/N)dW]
              /[int exp(t Re tr W/N)dW],
    E_t W=c_N(t) I.                                        (F5)

Conjugation symmetry makes the mean scalar; inversion makes it real. With
`q(W)=Re tr W/N`, `c_N(t)=E_t q`, `c_N(0)=0`, and
`c_N'(t)=Var_t(q)>0`. The compact group has full-support positive density,
so `0<c_N(t)<1` for finite t>0. Concentration at the unique maximizer I gives
`c_N(t)->1`. The already proved cap-volume argument of STEP55 §4.3 also gives
`sup_(t>0) t(1-c_N(t))<infinity`; only convergence is needed for the classical
limit below.

Here is a direct differentiation of the **uncentered actual** normalizer.
Write `Z_t(M)=int exp(t Re tr(W^-1 M)/N)dW`, so one kernel contributes
`-t Re tr M/N+log Z_t(M)` at V=I. At the identity,
`M'=q_c` and `Re tr M''=-average_tau||theta_(c,tau)||^2`.
The latter follows by differentiating the contour product; traces of its
second-order commutators vanish. Log-normalizer differentiation gives

    (log Z_t(M(s)))''|_0
      =(t/N)c_N(t) Re tr M''
         +(t/N)^2 Var_t(Re tr(W^-1 q_c)).                  (F6)

To evaluate the variance, use exact Haar invariance of `Z_t(exp(sq_c))`.
Its second derivative is zero, and hence the variance term in (F6) equals
`(t/N)c_N(t)||q_c||^2`. Combining terms proves

    Hess[-log k_t(I;M_c(U))]|_(U=I)[A,A]
      =(t/N)[||q_c(A)||^2
                +(1-c_N(t)) average_tau||z_(c,tau)(A)||^2]. (F7)

This is an exact finite-u identity. The contour-spread term cancels fully in
the centered classical/Laplace phase, but only partially in the actual
finite-u negative logdensity. In particular the exact kernel Hessian can be
positive on a direction with `q_c=0`. This calculation is consistent with the
coordinator's independent correction to the minimizer note; no classical
minimizer formula is changed here.

The Wilson contribution is `(u/N)d*d` at I. In exponential coordinates on
one SU(N) link write

    dHaar(exp A)=h_N j_N(A)d^D A,      j_N(0)=1,
    log j_N(A)=(1/24)Tr_ad(ad A)^2+O(||A||^4)
              =-N||A||^2/12+O(||A||^4).                   (F8)

This follows by taking the determinant of the exponential differential;
`Tr_ad(ad A)^2=2N tr(A^2)`. Thus the Hessian of `-log j_N` is `N/6 I`.
`h_N` is the fixed density at zero of probability Haar in the specified HS
Lebesgue convention. It is kept, not set equal to one.

Set `sigma=sqrt(N/u)` and write `W_e=exp(sigma z_e)` on non-tree links.
The exact Hessian at z=0 of the negative logdensity **with respect to dz**,
with its constant removed, is `K_u tensor I_D`, where

    H=J*(d*d+kappa Q_root*Q_root)J,
    B=J*B_sp J,
    K_u=H+kappa(1-c_N(kappa u))B+N^2/(6u) I.              (F9)

Here all scalar operators act on `E_*`; `*` is the counting adjoint.
The first derivative vanishes at U=V=I. There are no omitted linear terms.
For N=2 the exact mean is `c_2(t)=I_2(t)/I_1(t)`; the separate check below
uses this only against an independent Haar integral and actual noncommuting
contour products. Formula (F9) is proved for every N by (F5)–(F8).

## 4. Direct local coercivity in these coordinates

This is a local-coordinate proof of the already known soft-step mechanism,
needed to identify the particular inverse in (F9).

For an integer closed edge chain z inside a rectangular lattice box, contract
successively each coordinate to the root hyperplane. Sweeping an edge in a
transverse coordinate produces the corresponding plaquette strip. The
vertical edges cancel because `boundary z=0`. After four contractions the
chain is zero, so `z=boundary S`. The construction stays in the box and has

    ||S||_1 <= (sum of side widths) ||z||_1.               (F10)

It is a chain identity, allowing repeated edges with their signs. In one or
two endpoint blocks the width sum is <5L. A contour minus the direct
root-to-root path has chain norm <6L. A root-tree-path / single-edge / reverse
root-tree-path loop uses fewer edges. Thus the following conservative bounds
hold, with `b_L=60L^2`:

* For an internal edge e, its tree loop lies in its block; since tree links
  have A=0, `A_e=<dA,S_e>` with `||S_e||_1<=30L^2<=b_L`.
* For a crossing edge from B_X to B_(X+mu), compare its root-tree path with
  the direct root-to-root path. Compare every actual S4′ contour with that
  same direct path and average. Subtraction gives
  `A_e=Q_root A(X,mu)+<dA,R_e>`, with
  `||R_e||_1<=60L^2=b_L`. All plaquettes lie in those two blocks.

On a torus use these same lifted boxes. The contours have the same lifted
endpoints and winding as their reference path. For T>=2 the one/two-block
boxes are legitimate lifts, including wrapping pairs; no harmonic flux is
set to zero.

Square using Cauchy–Schwarz, or `|<F,S>|<=||S||_1 max|F|`.
There are at most `4L^4` internal edges per block and exactly `L^3` crossing
edges for each positive coarse link. A plaquette contained in an endpoint
pair is charged by at most eight such coarse links: choose one of its vertex
blocks, which has eight incident coarse-link labels. Small periodic tori
retain those labels, so the same bound applies. Consequently every tree-slice
form obeys

    ||A||^2 <= C_F ||dA||^2+C_Q||Q_root A||^2,
    C_F=4L^3(L+4)b_L^2,       C_Q=2L^3.                  (F11)

No number of blocks occurs. Hence

    H >= a I,       K_u >= a I,
    a=[max(C_F,C_Q/kappa_-)]^-1 >0.                      (F12)

The inequality for K_u uses both positive corrections in (F9). At L=3 and
kappa_-=1 this deliberately crude bound is `a=1/220449600`. It is not an
optimized spectral value or a physical mass. The proof also explains all
zero modes: `dA=0` forces internal links zero and every face constant;
`Q A=0` then forces those face constants zero. There is no hidden deletion
of root or harmonic directions.

## 5. Weighted inverse, square root and mode counting

Assign a non-tree link to its starting block. The operators in (F9) have
range at most two in block `l1` distance. A plaquette reads at most four
links and each link six plaquettes, giving row sum at most24 for `d*d`.
Put `P=5L`. Each contour row has absolute sum <=P; a fine link is in the
support of at most eight coarse means, so the corresponding averaged column
sum is <=8P. Thus `Q*Q` has row sum <=8P^2. The path Gram minus `Q*Q` in B
has row sum <=16P^2. These bounds survive J compression. Uniformly in u>=1,

    max_e sum_f |K_u(e,f)| <= b,
    b=24+24 kappa_+ P^2+N^2/6.                            (F13)

For a 1-Lipschitz block function f and weight `W_m=exp(m f)`, the Schur test
gives

    ||W_m K_u W_m^-1-K_u|| <= b(exp(2m)-1).

This is the existing `PROOF.md` Lemma CT mechanism, applied to the explicit
new K_u and block density; the proof is included to fix that dictionary.
Choose

    m=(1/2)log[1+a/(2b)]>0.                               (F14)

For every t>=0 the perturbation is at most a/2, so

    ||W_m(K_u+t)^-1 W_m^-1|| <=2/(a+t).

Use `f(X)=distance(X,Y)` (or bounded truncations on the infinite lattice),
then the exact positive-operator formula

    K_u^-1/2=(1/pi) int_0^infinity t^-1/2(K_u+t)^-1 dt.    (F15)

It follows that for either the infinite periodic-block lattice or its torus,
`C_u=K_u^-1` and `S_u=K_u^-1/2` have entrywise exponential bounds with
prefactors `2/a` and `2/sqrt(a)`, respectively. In infinite volume (F11)
holds first on compactly supported forms and extends by density; (F13)
defines a bounded operator. This justifies the same resolvent argument.

Finite-torus kernels are exactly periodizations of the infinite-lattice
kernels, by their block Fourier symbols and the absolutely convergent
kernels, including the functional calculus in (F15). Thus one usable form is

    |C_u,T(e,f)| <=(2/a) E_m,T(X_e,X_f),
    |S_u,T(e,f)| <=(2/sqrt(a)) E_m,T(X_e,X_f),
    E_m,T(X,Y)=sum_(v in Z^4) exp[-m|X-Y+Tv|_1].           (F16)

For `0<mu<m`, unfold the images and use the exact counting sum
`sum_(x in Z^4)exp[-(m-mu)|x|_1]=coth((m-mu)/2)^4`.
Both weighted rows and columns of S_u are at most

    R_S=(2m_0/sqrt(a)) coth((m-mu)/2)^4,                  (F17)

and those of C_u have `sqrt(a)` replaced by a. The `m_0=3L^4+1`
coordinates per block are counted. Each colour is a separate diagonal copy,
so a fixed scalar row has no extra D sum; a full trace/determinant has all D
copies. Images are summed, not dropped in favor of a lone geodesic term.
The explicit rate can be extremely small; at N=2,L=3,kappa=1, (F14) is about
`2.09e-13`. No useful numerical continuum scale is inferred from it.

For the scaled field z, the localized potential map is `G_u=J S_u`.
The curvature map is `d J S_u`; it is not the same kernel. The latter has
`6L^4` output coordinates per block. Each plaquette row reads at most four
links and a link contributes to six plaquettes. Moving between the starting
blocks costs at most one block step. Hence its weighted row bound is
`4 exp(mu) R_S` and its weighted column bound is `6 exp(mu) R_S`.
The scaled potential covariance is `J C_u J*`; its curvature covariance is
`d J C_u J* d*`, whose weighted rows/columns are bounded by
`24 exp(2mu)` times the C_u row bound. This distinguishes gauge-coordinate
potentials from the gauge-invariant linear curvature projection. The actual Lie-algebra field A has an additional factor sigma,
so both Gaussian covariances acquire the factor `N/u`. The tree map itself
has no long tail.

All Gaussian normalization costs stay extensive. For example, if a real
self-adjoint perturbation E is supported on the coordinates of a set S of blocks and
`||K_u^-1/2 E K_u^-1/2||<=eta<1`, then

    |log det(K_u+E)-log det K_u|
                    <=m_0|S|[-log(1-eta)]                (F18)

for one colour, and D times this for independent colours. This is the rank
bound from the nonzero eigenvalues, not a dimension-free operator estimate.
Without support restriction use `m_0 T^4`. Local trace/HS budgets remain
necessary in any subsequent forest expansion.

## 6. Exact normalized change of variables, with remainder and complement

Choose a fixed radius `0<r<min{injectivity radius, pi/sqrt(N)}` in the HS
norm. Let `Omega_r` be the event that every non-tree link of the unique
pinned tree representative belongs to `exp{A in su(N): ||A||_HS<r}`.
Equivalently, its matrix principal logarithm is traceless and has HS norm
less than r. The radius keeps every logarithm eigenvalue inside the principal
branch; also `|tr Log W|<=sqrt(N)||Log W||_HS<pi`, so `det W=1` forces
`tr Log W=0`. Thus this event is exactly the image of the specified
traceless coordinate ball. It is invariant under root-pinned gauges and
under global conjugation. This is a **global small-link chart**. In particular
it is not defined by small curvature alone and does not cover all flat
holonomies.

In this chart define the scalar function

    S_eff(A;I)=u sum_p s(U_p(A))
                   +sum_c[-log k_t(I;M_c(U(A)))],
    F_u(z)=S_eff(sigma Jz;I)-S_eff(0;I)
                           -sum_(e in E_*) log j_N(sigma z_e),
    R_u(z)=F_u(z)-(1/2)<z,(K_u tensor I_D)z>.              (F19)

The function R_u includes every cubic and higher action, kernel-normalizer
and Haar term. Its zero, first and second derivatives vanish at zero by
(F7)–(F9). Let `chi_cut` be the original interior-only cut, and define
`U(z)` with tree links I and non-tree links `exp(sigma z_e)`.
The exact restricted integral with any bounded gauge-invariant insertion Xi
is

    Theta_r(z)=1{max_e ||sigma z_e||_HS<r},

    Z_cut,r^epsilon[Xi](I)
      = A_u E_(xi iid N(0,1))[
          Theta_r(S_u xi) chi_cut(U(S_u xi))
          Xi(U(S_u xi),I)
          exp{-R_u(S_u xi)-delta S_epsilon(U(S_u xi))}],

    A_u=N_t(I)^(-4T^4) h_N^(m_0 T^4)
          (2pi N/u)^(D m_0 T^4/2) det(K_u)^(-D/2).        (F20)

`S_u` acts on each colour. The entire bracket is defined to be zero outside
Theta_r before evaluating the chart-only R_u. The coordinate cutoff is
essential: using only the event that exp(sigma z) lies in Omega_r would
include repeated exponential preimages. The factor `N_t(I)^(-4T^4)` is the
actual vacuum weight `w_0(I;I)`. The power of `h_N`, the scaling Jacobian, every Gaussian
mode and the determinant are explicit. Formula (F20) follows from (F2), (F8),
`z=S_u xi` and the normalized standard Gaussian density. No integration over
V has occurred and no identity `int k_t(V;M)dV=1` is used at fixed V.

The normalized source response of this **restricted** integral is therefore
exactly the ratio of the expectation in (F20) at epsilon and at zero. Its
real zero-source denominator is positive. A nonzero, volume-uniform complex
neighborhood for this interacting ratio is not proved here. The exact
original reference still obeys

    Z_cut^epsilon(I)=Z_cut,r^epsilon(I)
                        +Z_cut,Omega_r^c^epsilon(I).      (F21)

The complement includes large tree coordinates and holonomy sectors. It is
not suppressed, omitted or equated with a collection of original bad cubes.
Likewise, the stronger Sea3 all-fine-good cut is not substituted in (F20).

There is genuine local remainder control before whitening. Each term in
(F19) depends only on one plaquette, one coarse endpoint pair or one link.
For the single-normalizer part, use the **proved single-kernel** polar
recentering and fixed complex field width in STEP55 §4.1–§4.3, including
its §10 errata S5–S7 and CODEX_REVIEW_STEP R6. Its centered logarithm, after subtracting its value
at I, has all fixed-order local derivatives bounded uniformly for real t>0.
The centered classical phase is analytic near I by its local nondegenerate
polar maximizer. Cauchy estimates on a smaller fixed link chart, and the
analytic Haar Jacobian, give constants r_0,C depending only on N,L,kappa_±:
for `max_e||z_e||<=p`, `sigma p<=r_0`, each local third-order remainder
satisfies

    |R_(u,X)(z)| <= C u^-1/2 p^3,                         (F22)

with bounded multiplicity of X at each block. More explicitly the classical
terms cost `C u sigma^3 p^3`, while the centered normalizer and Haar terms
cost `C sigma^3 p^3`; N is fixed. Quadratic pieces are subtracted from each
same local term, so their sum is exactly the K_u of (F9). This is a local
analytic remainder bound, not a small bound on the total volume sum.
For the sources, `|epsilon_p|<=rho` gives per plaquette
`|u epsilon_p s(U_p)|<=C rho p^2` on the same scaled chart. Original source
labels remain on their actual plaquettes.

After whitening, (F22) becomes a function of `S_u xi`. Exponential decay of
S_u supplies a candidate localization mechanism, but hard indicators and
these nonlinear functions are not ultralocal functions of xi. No hard
indicator is Taylor-expanded or replaced by an independent white-noise cut.
No background-dependent prefactor, determinant or vacuum term is dropped
from a logarithm. The first missing source-return producer is a convergent
local expansion of this exact weighted expectation, with its pulled-back
cuts and original sources, followed by control of (F21) and the actual
history insertions on the required coarse-field domain. This is a more
specific remaining obligation than the quadratic reference constructed here.
It is still substantially short of higher-level induction, continuum OS
existence and a physical Hamiltonian gap.

## 7. Primary-source dictionary and scope of reuse

The original papers were freshly located by their versioned primary pages
on 2026-10-29 and their matching cached PDFs/text were read. Full external
PDFs and text remain under `/tmp`; exact file hashes and page coverage are
in `checks/soft_fluctuation_primary_sources.json`.

| Source read | Exact use and mismatch |
|---|---|
| Dimock, [Covariant Axial Gauge, arXiv:1410.2798v3](https://arxiv.org/abs/1410.2798v3), §§3.7–3.10, PDF pp.16–21, (100)–(152), including Propositions7–8 | His local C parametrizes `QZ=tau Z=0`, removes central linking bonds by the **hard** constraint, and uses `(C^T Delta_k C)^-1`. The Gaussian normalization is retained through the normalized integrals, the resolvent square root (141), and independent Gaussians (152). Here J only removes the root-pinned tree gauge; all coarse-visible crossing variables remain, finite kappa is part of H, and (F7)–(F9) add the exact SU(N) finite-u/Haar terms. We prove our d=4 local gap/counting bounds directly. His hard-constraint representation is a construction guide, not the supplier of this model's precision. |
| Dimock, [Balaban II, arXiv:1212.5562v2](https://arxiv.org/abs/1212.5562v2), Appendix F, PDF pp.91–92, (633)–(646) | F.1 starts with an ultralocal probability law, locality in **all** displayed fields, and a small interaction bound on its support. Its integration step uses independence on disjoint supports. Formula (F20) gives independent Gaussian reference variables but leaves nonlocal pullbacks of interactions/cuts. F.1 is not yet applicable to that full expectation. No d=3 scalar theorem is imported as a completed d=4 gauge estimate. |
| Abdesselam–Rivasseau, [Trees, forests and jungles, hep-th/9409094v1](https://arxiv.org/abs/hep-th/9409094v1), §V.E, PDF pp.31–33 | The two-level forest keeps fixed cells as vertices and retains normalized positive interpolated Gaussian measures. Its application assumes summable covariance connections and a small large-field probability per cell. Equations (F16)–(F18) provide a quadratic connection/mode inventory; neither those probabilities nor the complete source/cut forest bounds are supplied here. |

These are non-derivation comparisons; the resolvent integral and finite
Gaussian identities are independently proved/used with their hypotheses
above. The prior `CROSSOVER_LITERATURE_BRIDGE_ASTRA.md` warning about mode
counts is respected in (F18),(F20). The dimensional/length conventions of
Dimock's `1712.10029v3` are not imported; all present coordinates use d=4
counting density directly. The current axiom memo, primitive procedure and
registry were checked at the immutable methodology revision. The Wilson
law is explicit model input; no framework dynamics, axiom or primitive is
created or inferred from those authority documents.

## 8. Evidence, failures and handoff

The predeclared criteria are `checks/soft_fluctuation_criteria.md`.
`checks/soft_fluctuation_check.py` imports no predecessor code. It generates
all 7,776 paired contours directly, while an independent coordinate-chain
homotopy checks their exact integer filling boundaries. Bloch matrices are
compared to a separately assembled periodic sparse matrix; noncommuting
SU(2) path products and a Haar/Bessel normalizer independently test (F7)–(F9).
A separate matrix-group implementation in
`checks/soft_fluctuation_tree_group.py` constructs and reverses the full
pinned-root tree transformation, checking all Wilson plaquettes and selected
actual means, including periodic wrapping.

The final combined scalar/path/SU(2)/periodic run reports 90/90 predicates;
the separate group-coordinate run reports 9/9. Earlier mode runs overlap
with the combined run and are not counted again. The finite tests and their
limits are recorded in the receipt and final raw diagnostic outputs. The
volume-uniform claim rests on the analytic proof (F10)–(F17). The SU(2) numerical derivatives and integrals are
floating-point diagnostics, not interval certificates. Exact integer
boundaries and path counts have a different, exhaustive status.

A first spectral diagnostic reported 38/39: at momentum `1e-7`, a fixed
`1e-9` eigenvalue threshold counted four small bare eigenvalues, while the
proposed assertion called them exactly one zero mode. Three curl eigenvalues
are of order momentum squared. The threshold did not resolve their rank.
The original code and output are preserved as attempt01; the repaired check
reports the four near-zero eigenvalues without claiming exact nullity there.
The root-gradient construction and positive soft matrix remain tested at
that momentum. No positivity threshold was weakened. The initial external
text parsing assumed form-feed pages and failed; the matching cache used
explicit PDF PAGE markers and was subsequently read successfully.

Obligation graph: (F2) is the elementary group/Haar quotient proof;
(F7) is the exact normalization derivative; (F8) is the Lie-algebra Jacobian;
(F11) is the actual local path/counting estimate; together they prove (F9),
(F12). Finite-range counting and the resolvent integral prove (F16)–(F17).
The ordinary Gaussian change proves (F20) with every prefactor. Only the
optional local analytic remainder estimate (F22) consumes the prior
single-kernel nonvanishing theorem, with its fixed real coupling and local
complex-field domain explicitly preserved. No prior sea clustering or
continuum theorem is a premise.

The next proposed background route is the blockwise lift whose internal
links are I and whose crossing-face links equal V_c. Every actual S4′
contour then equals V_c; fine curvature appears at double-face intersections.
A transported path estimate, its curvature-error count and a local critical
shift for the nonzero Wilson gradient would be new work. Arbitrary small
coarse curvature and allowed holonomies are not part of this frozen unit.

Independent review must confirm the final source, tree-measure dictionary,
finite-u variance cancellation, Haar coefficient, local filling multiplicity,
periodic density and full normalization. Root owns that review and all
integration. Author computations and this receipt confer no audit status.
