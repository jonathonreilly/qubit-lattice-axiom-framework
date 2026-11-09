# Seven-edge marginal: regional stationary field and compact relative coercivity

Author proof, 2026-11-09; fresh mathematical checking pending. This proves a
finite-model leading-energy statement conditional on the supplied global
compact theorem, whose hypotheses are mapped below. It grants no retained
status, probability-decay estimate, or finite-u action minimizer.
Source revision: `fbdfb3c1b8852e5de302fab6f0f7cfc70ba04cac`.

## 1. Domain, exact conditional, and assertion

Fix odd L>=3, kappa>0, m>=3 and the periodic four-dimensional fine lattice
of side L²m. Use exactly the supplier's centered terminal-root fine forest,
actual 24L^4 paired-root-leg arithmetic path means at both levels, and
independent positive-edge convention. Internal trees of terminal cubes may
be any of those allowed by the global theorem. Fine forest links are fixed
I, all remaining fine links and all intermediate links are hidden variables.
Let H be this hidden link set. A link is owned by the terminal cell containing
its tail. Each cell owns n_b=3L^8+1+4L^4 hidden links. Fix J to be the seven
positive terminal edges in two distinct elementary terminal plaquettes sharing
exactly one edge; put O=E2\J. All terminal outputs in O are I; sources are zero.

For group variables a, let

    W_p=1-w(U0,p),
    gamma_0,c=|M0,c|-<U1,c,M0,c>,
    gamma_1,c=|M1,c|-<I,M1,c>,
    E_J=sum_p W_p+kappa sum_(all level-0 c) gamma_0,c
                       +kappa sum_(c in O) gamma_1,c.          (1)

Here w is the real half trace and the pairing is the quaternion scalar
product. Every centered gap is nonnegative, even at zero means. Each
surviving factor carries its complete hidden reader set: for a level-zero
kernel this includes its hidden output and every input of M0,c; for a
terminal kernel it includes every input of M1,c. In particular the reader
set includes every input of its radial normalizer, whether or not a
particular evaluation or cancellation makes it locally inactive. Fine tree
identities and fixed terminal outputs are not hidden readers. Repeated word
occurrences are retained in formulas.

Let R be any set of terminal cells and I_R the hidden links it owns. Select
all fine plaquette factors and all whole surviving kernels with a hidden
reader in I_R, counting each factor once. Let P_R,C0_R,C1_R be their labels,
with C1_R subset O. Their leading sum is E_R^J(a,z), with exterior hidden
readers fixed to z. Unselected factors are independent of a. No partial
kernel and no deleted terminal kernel is selected. The collar B_R is the
union of exterior hidden readers of selected factors. Coordinates outside
I_R union B_R are irrelevant to this conditional.

With probability Haar dQ and Z(s)=integral exp(s w(Q))dQ, the exact conditional
of the actual rho_J law at t=kappa*u, u>=1, is

    mu_R^J(da|z)=Z_R(z)^(-1) exp[-u sum_(p in P_R) W_p(a,z)]
       product_(c in C0_R) exp[t<U1,c,M0,c>]/Z(t|M0,c|)
       product_(c in C1_R) exp[t<I,M1,c>]/Z(t|M1,c|)
       product_(e in I_R) da_e,                              (2)

or equivalently

    mu_R^J(da|z)=Z_R(z)^(-1) exp[-u E_R^J(a,z)]
       product_(c in C0_R) H_u(|M0,c|)
       product_(c in C1_R) H_u(|M1,c|) product_e da_e,
    H_u(r)=exp(kappa*u*r)/Z(kappa*u*r).                       (3)

Z_R in (2) and (3) is the same integral; global normalizations and all
unselected factors cancel. Z(0)=1, so no exception is needed at zero means.
This positive continuous compact density defines the conditional at every z,
not only at almost every exterior configuration. Its derivation uses the
supplier's exact forest Haar quotient; it introduces no gauge determinant.
If expressed in injective log coordinates, the additional Haar factors are
(2pi²)^(-1)(sin|x_e|/|x_e|)² per hidden link. They are not in E_R^J.

**Assertion.** There are epsilon_*,alpha,C,c,C_Q,rho_Q>0 depending only on
L,kappa, uniform in m,R,pair position/orientation and the permitted trees,
with the following property. If d(z_e,I)<=epsilon<=epsilon_* for every
exterior reader e in B_R, where d is quaternion chord distance, there is
a continuous (hence measurable) stationary field a*_R(z) such that

    |log a*_e|<=C epsilon exp[-alpha dist(owner(e),R^c)].      (4)

Distances use the ambient periodic terminal-cell graph. For full R use
infinite distance and a*=I; empty R is the empty field. For every compact
q in SU(2)^(I_R), with (a*q)_e=a*_e q_e,

    E_R^J(a*q,z)-E_R^J(a*,z)>=c sum_(e in I_R)[1-w(q_e)].     (5)

Consequently a* is the unique global minimum of the leading energy. If all
d(q_e,I)<=rho_Q there is also the volume-uniform cap bound

    0<=E_R^J(a*q,z)-E_R^J(a*,z)
                       <=C_Q sum_(e in I_R) d(q_e,I)².       (6)

Stationarity here is only that of E_R^J; neither radial normalizers nor Haar
chart terms are silently differentiated away in the full finite-u action.

## 2. Global baseline, local templates, and the principal Hessian

The seven-edge compact theorem supplies C_g(L,kappa)<infinity with

    E_J(v)>=c_g sum_(e in H)[1-w(v_e)], c_g=1/C_g>0.          (7)

Its quantified geometry is exactly that in section 1. In particular, the
unused-direction three-edge detours exist globally even for m=3 and seam
pairs. We need no assumption that such a detour lies inside R. Extend q by
I on H\I_R. Every unselected factor now has all readers I and equals zero;
selected factors evaluate exactly to their regional values. Thus

    E_R^J(q,I)=E_J(q extended by I)
                     >=c_g sum_(e in I_R)[1-w(q_e)].         (8)

This is the required global-to-regional step. A proof that instead discarded
parts of crossing factors or demanded witnesses internal to R would not
justify (8). Global recovery witnesses may leave R: their entire inequality
is applied before the equality (8), and unselected energy terms are zero.

For fixed L, all factors have uniformly bounded arity, word lengths,
coefficients, and incidence per hidden link. Their reduced reader supports
are contained in the original endpoint-block supports after setting tree
links to I. Cell-reader diameter has a finite uniform bound r0; one may use
the supplier's r0=2, but only finiteness is used below. Permitted internal
trees form a finite family within each fixed-size block. Taking maxima over
that family preserves all constants. Periodic coincidences add occurrence
multiplicities rather than creating new unbounded templates. Consequently
m=3, wrapped R and arbitrary tree choices have the same bounds.

Every factor is globally Lipschitz in compact reader variables: word products
telescope, averages are linear, norm is 1-Lipschitz, and pairing is smooth.
On a sufficiently small all-reader identity chart, all actual path words
are close to I, hence every |M|>=1/2. On that chart factor derivatives through
order three have uniform bounds. Coefficients 1,kappa are included throughout.

Put U_e=exp(i x_e dot sigma). The actual means' signed linear path averages
are Q0,Q1. The supplied direct centered-gap expansion gives

    <x,H_E,J x>=||d0 x0||²+kappa||x1-Q0 x0||²
                                      +kappa||P_O Q1 x1||². (9)

There is no terminal-J term and no intermediate Wilson action. From (7),
using 1-w(exp(i s x dot sigma))=s²|x|²/2+O(s^4), follows H_E,J>=c_g I.
Uniform template Hessian row bounds give H_E,J<=M I for a finite M, enlarged
if necessary so M>c_g. Its cell-block range is at most r0. These statements
also follow for the upper bound from the explicit identity Hessian supplier;
we do not infer absolute row bounds from an operator bound alone.

Let F_R(x;y)=E_R^J(exp(ix),exp(iy)), where y are principal logs of collar
coordinates. Its interior Hessian H_R=D_x² F_R(0;0) is precisely the
principal restriction of H_E,J to I_R. Indeed unselected factors have no
interior reader and thus no interior derivatives; selected factors are
unchanged. Hence

    g I<=H_R<=M I, g=c_g,                                  (10)

uniformly for every R. An arbitrary exterior value does not define H_R:
(10) is explicitly at the all-identity baseline.

For comparison only, the exact normalized full-law chart Hessian is

    u^(-1)D² S_J(0)=H_E,J+kappa[1-B(kappa*u)]diag(V0,V1,O)
                                    +(2/(3u))I,
    B(t)=Z'(t)/Z(t), 0<=B(t)<=1.                            (11)

V0,V1,O are the actual path-variance forms. Formula (11) confirms why the
principal leading Hessian used here is not the entire finite-u precision.

## 3. Uniform weighted inverse and stationary construction

Assume first R is nonempty and proper. Write matrices in cell blocks of
3n_b real coordinates. Choose M'>M, set rho=1-g/M' in (0,1), and use

    H_R^(-1)=(1/M') sum_(k>=0)(I-H_R/M')^k.                 (12)

The kth summand has cell-block range at most k r0 and operator norm at most
rho^k. Thus for X,Y in R,

    ||(H_R^(-1))_(XY)||<=g^(-1) rho^ceil(dist(X,Y)/r0).     (13)

This bound uses ambient distance: any chain of nonzero blocks has total
ambient displacement at most k r0, whether or not R is connected. For r0
replace it by max(1,r0) if necessary. Choose 0<alpha<-log(rho)/r0 and put

    A=g^(-1)[1+sum_(r>=1)(2r+1)^4 exp(alpha r)rho^(r/r0)]<infinity.

A periodic four-dimensional graph has at most (2r+1)^4 vertices in a shell
of radius r: representatives with coordinate distances at most r give this
volume-uniform overcount. With s_X=dist(X,R^c), w_X=exp(alpha s_X), define
||x||_w=max_(X in R) w_X |x_X|, where |x_X| is cell Euclidean norm.
The function s is 1-Lipschitz, so w_X/w_Y<=exp(alpha dist(X,Y)). Summing
(13) by shells proves ||H_R^(-1)||_(w->w)<=A. Disconnectedness, holes and
periodic wrapping require no modification.

For epsilon<=1, the collar logs satisfy |y_e|<=2epsilon. Define

    f(y)=grad_x F_R(0;y),
    grad_x F_R(x;y)=f(y)+H_R x+N(x;y), N(0;y)=0.             (14)

Every factor has zero gradient at all-reader identity. Therefore f is
supported only at interior reader cells within distance r0 of R^c, since
only a selected factor with an exterior reader can contribute. Smoothness,
finite incidence and finite block dimension imply

    ||f(y)||_w<=B epsilon                                 (15)

for a uniform B, including exp(alpha r0). On ||x||_w,||x'||_w<=s, uniform
third derivatives give an unweighted block Hessian perturbation row bound
K(s+epsilon). All entries still have range r0; multiplying by weights costs
at most exp(alpha r0). Integrating this Hessian difference along the segment
from x' to x yields

    ||N(x;y)-N(x';y)||_w
                         <=K_alpha(s+epsilon)||x-x'||_w.  (16)

These estimates use only small all-reader logs; choose their common domain
radius r_s>0 so every relevant |M|>=1/2 throughout all these segments.

Set s=2AB epsilon. Reduce epsilon_* so s+2epsilon<r_s (with the fixed chart
norm conversion absorbed in r_s) and A K_alpha(s+epsilon)<=1/2, strictly
if desired. The map

    T_y(x)=-H_R^(-1)[f(y)+N(x;y)]                           (17)

then preserves the closed weighted ball of radius s and is a contraction
there. Its unique fixed point x* obeys grad_x F_R(x*;y)=0 and
|x*_e|<=2AB epsilon exp(-alpha s_owner(e)), proving (4). The log chart is a
local diffeomorphism, so this is stationarity in every group tangent direction.
Iterates from zero are continuous functions of the exterior logs and converge
uniformly on the prescribed collar domain (the contraction constant and
initial bound are uniform). Thus a*(z)=exp(ix*(z)) is continuous there.

For full R there is no collar, f=0 and x*=0. Equation (8) already gives its
unique global minimum. For empty R all products, sums and coordinates are
empty, and (2)-(6) have their natural trivial meanings. All later arguments
also cover these cases. In particular epsilon=0 gives a*=I for every R.

## 4. Factorwise compact perturbation, including zero means

Let h_f be one selected energy factor, including coefficient 1 or kappa,
and S_f its distinct interior hidden readers. S_f is nonempty by selection.
Its exterior reader values are z and its fixed readers remain I. Define

    D_f(q)=h_f((a*_e q_e)_(e in S_f),z)
                      -h_f((a*_e)_(e in S_f),z)-h_f(q,I),
    b(q)=Im quaternion(q) in R³,
    l_(f,e)=derivative_(x_e at 0) D_f((exp(ix_e))_e).        (18)

One has D_f(I)=0, as h_f(I,I)=0. We prove the uniform bound

    |D_f(q)-sum_(e in S_f) l_(f,e) dot b(q_e)|
                 <=K0 epsilon sum_(e in S_f) d(q_e,I)²    (19)

for every compact reader assignment q. Constants include the fixed upper
bound on |log a*|/epsilon supplied by section 3, and are independent of R.

First, all background parameters a*_e,z_e lie O(epsilon) from I. Global
Lipschitz continuity of h_f implies |D_f(q)|<=K epsilon for every q,
including at means equal to zero. The comparison includes the subtraction
h_f(a*,z), whose absolute value is O(epsilon), and uses h_f(I,I)=0.

Next restrict every q_e to a sufficiently small, fixed chord cap delta.
The parameterized functions h_f(a*exp(ix),z) and h_f(exp(ix),I), including
interpolations of the small background logs, then stay in the common smooth
all-reader chart. Differentiation twice in x and once in a background log
is controlled by the third derivative bounds and smooth group multiplication.
The Hessian in x of D_f is therefore O(epsilon), and |l_(f,e)|<=K epsilon.
Taylor's formula at zero gives

    |D_f(exp(ix))-sum_e l_(f,e) dot x_e|
                                      <=K epsilon sum_e |x_e|².

Since b(exp(ix))=(sin|x|/|x|)x, one has |x-b(exp(ix))|<=K|x|³; in this
fixed chart log and chord lengths are comparable. This proves (19) on the
small cap. If q is outside that product cap, some reader has d(q_e,I)>=delta.
The global bound on D_f, the derivative bound on l, |b(q)|<=1 and bounded
arity give a left side at most K'epsilon, while the right sum is at least
delta². Increasing K0 proves (19) on the complement as well. No derivative
of the Euclidean norm at zero mean was taken. Antipodal group values and
all zero-mean loci belong to the valid compact complement argument.

## 5. Exact tangent-proxy cancellation and global absorption

Summing l_(f,e) over the selected factors reading an interior coordinate e
is the derivative at q=I of

    E_R^J(a*q,z)-E_R^J(a*,z)-E_R^J(q,I).

The first term has zero derivative by group stationarity at a*; the last
has zero derivative because each identity-baseline factor does. The path
q_e=exp(itv) differentiates a*_e exp(itv), so the same right-tangent frame
is used in every factor contributing to this coordinate. Consequently

    sum_(f reading e) l_(f,e)=0                            (20)

exactly, and multiplying by the common proxy b(q_e) cancels the linear terms
for every compact q, without requiring a global log for q. Summing (19) and
using the uniform maximum incidence D gives

    |E_R^J(a*q,z)-E_R^J(a*,z)-E_R^J(q,I)|
                     <=D K0 epsilon sum_e d(q_e,I)².      (21)

As d(q,I)²=2[1-w(q)], (8) and (21) imply (5) with c=c_g/2 after reducing
epsilon_* so 2D K0 epsilon_*<=c_g/2. If any q_e differs from I the sum is
strictly positive, proving the asserted unique global leading minimum.
The relative estimate is genuinely all-compact: no smallness of q, mean
nonvanishing, or region-constrained detour enters this final step.

For the upper bound, reduce epsilon_* so all background readers stay inside
a smaller smooth identity chart. Choose rho_Q>0 such that each q_e with
d(q_e,I)<=rho_Q has principal log v_e and every interpolated variable
 a*_e exp(i t v_e dot sigma), 0<=t<=1, remains in the smooth chart. Uniform
factor Hessian bounds and incidence give an operator bound C_H on the
Hessian of v -> E_R^J(a*exp(iv),z) throughout this product cap, independent
of its dimension. Its differential at v=0 is zero by stationarity. The
integral Taylor remainder and |v_e|<=C_log d(q_e,I) yield

    |E_R^J(a*q,z)-E_R^J(a*,z)|
                            <=(C_H C_log²/2) sum_e d(q_e,I)².

Together with (5) this is (6). A large total Euclidean norm of v is harmless:
the entire segment remains in the product chart and the Hessian operator
bound is uniform there.

## 6. Source provenance, scope, and recovery

All three mathematical sources below were read in full at the assigned
revision. Paths are relative to this pack's `parts/` directory:

| Source | SHA-256 | Exact use |
|---|---|---|
| two-plaquette-compact-coercivity.md | b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e | Actual seven-edge compact inequality; uniform geometry, tree and periodic multiplicities; bounded reader locality |
| partial-terminal-normalizer-hessian.md | a17f372f928930bd9be6e81d68349a62232a027f17a13a7cd47e813f43584139 | Exact rho_J, forest Haar measure, centered-gap Hessian (9), and finite-u distinction (11) |
| local-relative-coercivity.md | 6b7c3a0eba818566fad0cb34f13998a3cf98de632761d7942ca527c51c80cb37 | General regional method, reinstantiated in sections 2-5 with the actual deleted law and principal H_E,J |

Instructions read in full from this worktree: `AGENTS.md` SHA-256
`7def904fdd52d811e7aba87a0d3d859bfb017cccd59703125f4a53f2805aaab2`;
`docs/ai_methodology/SCIENCE_WORKFLOW.md`
`1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`;
`docs/ai_methodology/skills/workhorse/SKILL.md`
`e3e3cea67ad1877e4e73e38c7d62f1561142a0dffc66abe991f2ad0250133ad8`;
and that skill's freshness procedure. This is the assigned coherent snapshot;
no network refresh or installed skill execution was performed. Parent supplied
preflight and science lease (memory cap unavailable), authorized bounded medium
worker effort, and reported the completed initial repo/literature pass: these
were the closest supplied statements; no direct sparse-deleted regional theorem
was found. The mathematical proof here uses no external literature theorem or
unproved Dobrushin contraction. The weighted contraction is proved in (12)-(17).

Recovery checkpoint: (7) is the explicit inherited mathematical premise;
(8)-(21) give its full regional transfer for the actual seven-edge law, including
all surviving normalizer readers. The old all-terminal relative result is a
method source, not a claim that deletion preserves its constants automatically.
Its finite template bounds and the new global c_g instead produce the constants
above. No regional-detour route was used. No counterexample was found or claimed.
Fresh independent checking of this complete argument is pending; the author
read the supplied global proof but did not re-read its ancestral source chain.
No full finite-u minimizer, conditional probability bound, rough-sector
summability, connected response decay, or physical continuum conclusion follows
here. Only this deliverable was edited; no prompt edits, numeric jobs, Git
mutations, commits, pushes, or network actions were performed.
