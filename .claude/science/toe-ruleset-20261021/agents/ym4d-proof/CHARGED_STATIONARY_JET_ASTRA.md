# Full-colour stationary jets and the remaining second-curvature estimate

**Author work; fresh independent review pending.** This unit concerns the
u-stripped normalized tree phase. It gives the actual cubic source and quartic
exchange, a weighted version of the existing full-colour cubic argument, and
a forced second-current recursion. The final second-curvature estimate in
CJ18 is **OPEN**. Full four-dimensional Yang–Mills existence and a positive
physical continuum Hamiltonian mass gap both remain **OPEN**.

Claim certificate: `actual_current_surface_status: bounded-support`;
`target_claim_type: bounded_theorem`; `trace_class: upstream_support`;
`reachability_to_target: partially_closes`; `bare_retained_allowed: false`;
`audit_required_before_effective_retained: true`. The supplied normalized
model and named linear mathematics are explicit conditions; CJ18 remains
an open producer. This is author support, not an audit-status assignment.

## 1. Model, inputs, and exact consumer

Take d=4, SU(N), N>=2, odd L>=3, kappa_j in a fixed compact positive interval,
depth n>=1, and periodic top side T>=3. Links are integrated Lie-algebra
variables in each level's own unit lattice, with counting inner products and
`<X,Y>=-Re tr(XY)/N`. The top field is `U_n=exp(v)`. The supplied action is

    F(U_0,...,U_n)=sum_p(1-Re tr U_p/N)
                    +sum_(j,c) kappa_j phi_(M_j,c)(U_(j+1),c),
    phi_M(V)=[max_(W in SU(N)) Re tr(W^-1 M)-Re tr(V^-1 M)]/N.       (CJ1)

`M=(24 L^4)^-1 sum_(sigma in S4,y in B(X)) T_(sigma,y)`, with the SAME
coordinate order at the two endpoints. The root is `LX+(L-1)/2`; equivalently
use centered offsets `-(L-1)/2,...,(L-1)/2` about root zero. The contour is
the root-to-y axial path, the positive length-L straight leg, then the
inverse endpoint axial path. Its length is below 5L. Independently averaging
the endpoint orders, deleting an endpoint, or changing the divisor changes
the model. No Wilson or soft dynamics is derived from framework primitives.

The corrected input [UNIFORM_SOFT_MINIMIZER_ASTRA](UNIFORM_SOFT_MINIMIZER_ASTRA.md)
has SHA256 `203d4edbf97078d88fcb488f164e525d2671fe5a2a910c5f6e49f615e8f41bfe`.
Its original review and both scope correction/confirmation records are read
together. US1–US17 concern CJ1. The finite-u logdensity has the additional
positive spread Hessian `t(1-c_N(t)) average||z||^2/2`; it is not substituted
for CJ1 here.

Consumed mathematical inputs are: US1–US16's actual linear curvature/residual
kernels and periodization; the repaired periodic version of TUNIF TU-3;
NQ_DEF §D3's `||Q^(m)||_(infinity->infinity)<=q0 L^m`,
`q0=1+d(L+1)/(2L)`; and the root interpolation construction checked in
CODEX_REVIEW_TUNIF2 and REVIEW55_TUNIF U6. Their proofs, exact ranges, bytes
and remaining scope restrictions are recorded in the read manifest. The
positive strip used below is the validated **unprimed** strip from US8–US11,
shrunk below .1 for TU-3, not an unchecked historical primed numerical rate.

The existing cubic result is reused, not claimed as new: NORMS N1-15,
CODEX_REVIEW_TUNIF2 lines204–236, and FLOW55 §3.5 give a full-colour
trivial-background cubic bound conditional on their named linear imports.
Its displayed geometric factor is `L^3/(L-1)`: 27/2 at L=3 and 125/4 at L=5.
It does not prove a nonlinear Hessian Lipschitz bound on a fixed neighborhood.

The actual finite-part consumer is UIR55 §3.4, class J(m0,CJ,cE), with
`beta[T]=1`, coercivity `D²T>=cE d*d`, and

    sup_n max_(q=2,3,4) |||D^q T_n(1)|||_m0 <= CJ,
    |||K|||_m = sup_x1 sum_(x2,...,xq) |K(x1,...,xq)|
                                      exp(m diam(x1,...,xq)).     (CJ2)

The diameter is the top-lattice l1 diameter; colours and oriented links are
included in absolute sums. Lemma FP then bounds the finite part. The fixed-n
volume-first residual cancellation and the all-Cartan US17 quartic have
already been reviewed; neither is repeated as the missing full-colour
producer. FLOW55 §4.3 uses the same weighted norm and separately asks for
jet convergence. This unit does not prove convergence.

For BFT34_55's Hilbert–Schmidt basis `e_a` versus FLOW's `t_a=sqrt(N)e_a`,
`T_FLOW(b)=E_BFT(sqrt(N)b)/N`, so q-jets convert by `N^(q/2-1)`.
All formulas below use the normalized CJ1 convention directly.

## 2. Actual local third and fourth polynomials

For an ordered signed path with edge matrices X_l, write

    log product_l exp(epsilon X_l)
       =epsilon A+epsilon² B+epsilon³ C+O(epsilon⁴),
    A=sum_l X_l,  B=(1/2)sum_(l<m)[X_l,X_m].                     (CJ3)

The third term is obtained by successive BCH, including both nested
commutators; it is a fixed local homogeneous cubic. For a fine plaquette use
`f=d_2 a_0`, `B_p`, `C_p`. Its coefficients are

    W2=||f||²/2,  W3=<f,B_p>,
    W4=||B_p||²/2+<f,C_p>-Re tr(f^4)/(24N).                     (CJ4)

At a soft link let `A=average A_tau=Q a`, `B=average B_tau`,
`M=I+epsilon A+epsilon² M2+epsilon³ M3+...`, with
`M2=B+(1/2)average A_tau²`,
`M3=average[C_tau+(A_tau B_tau+B_tau A_tau)/2+A_tau³/6]`.
Set `r=b-A`, `R2=M2+M2†-A²`. Directly expanding `tr sqrt(M†M)` and the
second trace in CJ1 gives

    phi2=||r||²/2,       phi3=-<r,B>,
    phi4=(1/N)Re tr[ r M3+(1/2)M2†M2-(1/2)b²M2
                            +(1/6)b³A-(1/24)b⁴-(1/8)R2² ].     (CJ5)

This is an actual S4′ polynomial, not a generic vertex placeholder. The
fourth coefficient of M cancels from this expression. `arg det M=O(epsilon³)`:
the first trace is traceless anti-Hermitian and the second trace is real.
Thus imposing determinant one on the polar maximizer changes its maximal
real trace only at degree six and does not change CJ5 for SU(N).

At `b=A`, CJ5 is exactly `||B||²/2`: substitute `M2=B+D`, D Hermitian, and
use `Re tr[D,B]=0`. In particular

    phi4=||B||²/2+R4_soft,
    R4_soft=(1/N)Re tr{r M3
      -(1/2)[(A+r)²-A²]M2+(1/6)[(A+r)³-A³]A
      -(1/24)[(A+r)^4-A^4]}.                                  (CJ6)

Every monomial of R4_soft contains a linear residual. No commuting-colour
assumption enters CJ3–CJ6.

Let `a=zetav` be one admissible linear stationary chain, `a_n=v`, and
`r_j=a_(j+1)-Q_j a_j`. Define the homogeneous polynomials Fq by
`F(epsilon a)=sum_q epsilon^q Fq(a)`. Then

    F3(a)=sum_p <d_2 a_0,B_p(a_0)>
                          -sum_(j,c) kappa_j <r_j,B_j(a_j)>.
    S_a(w)=D_hidden F3(a)[w]
      =sum_p[<d_2 w_0,B_p>+<f,DB_p[a_0]w_0>]
       -sum_(j,c) kappa_j[<w_(j+1)-Q_jw_j,B_j>
                                      +<r_j,DB_j[a_j]w_j>],
    w_n=0.                                                    (CJ7)

This identifies every source leg: the first commutator mean, its derivative,
the actual residual, and the bottom plaquette commutator. In particular
`S_a` does not vanish for general noncommuting data. The all-Cartan
cancellation of US17 cannot remove these terms.

## 3. Hidden domain and exact stationary exchange

The quadratic form is US1:

    F2(a)=||d_2a_0||²/2+sum_j kappa_j||a_(j+1)-Q_ja_j||²/2.

At top variation zero its kernel consists of nested fine gradients with
scalar parameter zero at all top roots, modulo the irrelevant common scalar
constant. Choose a rooted block-tree slice, or the orthogonal complement of
that kernel. Both give the same stationary value. All one-form harmonic
modes are retained: a constant top v has the exact linear lift
`a_j=L^(j-n)v`. The inverse below is only the hidden slice inverse H^-1,
not a full gauge-null inverse. On every fixed finite chain H is positive.
S annihilates the kernel: differentiate exact gauge invariance at order
three, using the hidden stationarity of F2. This also justifies gauge
completion in the controls.

Writing the stationary chain as `epsilon a+epsilon² w2+...` gives

    w2=-H^-1 S,   T3(v)=F3(zetav),
    T4(v)=F4(zetav)-(1/2)<S,H^-1S>.                            (CJ8)

In derivative notation, `c(v,w)=F_xzz[zetav,zetaw]` and
`D⁴T=F⁴[zeta⁴]-sum_(three pairings)<c,H^-1c>`; for equal inputs
`c(v,v)=2S(v)`. Thus the factors 1/2 in CJ8 and 3 in the fourth-derivative
formula agree. The second-order chain is not being discarded.

The determinant factors are separate from this classical stationary value.
For root injection J, nonroot injection I, `A=I*Delta I`, the scalar
harmonic lift is `J-I A^-1 I*Delta J` and its root Schur form is S_root.
The constant scalar is excluded only when the prime/mean-zero domain says
so; `ker S_root=constants`. The induced root gauge Gram is S_root², with
`det' Delta_f=ell^4 det A det' S_root`. For harmonic one-form graphs the
two Gram factors are `(1+ell^-2)^h` and `(1+ell²)^h`, not one factor. In the
neutral comparison `h=4(N-1)`; at the trivial full-colour point the full
harmonic dimension is `4(N²-1)`. A moving charged-background kernel cannot
be replaced by this fixed kernel without a separate determinant argument.
No Gram factor is inserted into F2 or CJ8. These are the precise domains
already checked by the residual review, retained here to prevent a domain
change in later finite-part use.

## 4. A weighted admissible linear lift; reuse of the cubic theorem

Here is the additional harmonic step that avoids the global mean tail in
the repaired T-UNIF construction.

**Analytic one-form lemma.** If a holomorphic coarse one-form h(p) obeys
`nu_mu h_nu-nu_nu h_mu=0`, `nu_mu=exp(ip_mu)-1`, in a neighborhood of p=0
in dimension at least two, then `h(0)=0`. On the punctured mu-axis all
components except mu vanish. Taking its limit and using two different axes
gives the result. The same conclusion holds with extra holomorphic
parameters. This is a statement about a family, not a single closed fibre.

Apply periodic TU-3 to the actual bottom curvature kernel from US8–US11.
For ell=L^n it produces a periodic holomorphic primitive b_0 of the same
curl with entrywise kernel bounded by
`C ell^-1 exp(-eta distance_top)` after shrinking the strip. Do NOT subtract
its torus mean. In the current positive-residual convention form

    b_j=Q^(j) b_0+sum_(i<j) Q^(j-1-i) r_i,   h=v-b_n.           (CJ9)

At every real nonzero coarse momentum, the twisted fine first cohomology
vanishes. Since b_0 and the stationary lift have the same curl, their
difference is a fine gradient. Root covariance propagates this difference,
so h is a coarse gradient there. All quantities defining h are holomorphic
periodic symbols; hence `nu wedge h=0` identically and the lemma gives
`h(0)=0`. At p=0 the fine closed difference has no harmonic component:
Q^(n) maps a constant fine one-form to ell times that form, while gradients
have zero top constant component. Thus the raw b_0 already has the required
harmonic mean. This conclusion uses the actual chain residuals in CJ9; it
is not true for an arbitrary closed fibre assigned independently at p=0.

Let H_j h be the gradient of the multilinear interpolation of a coarse
potential for h. Each fine link difference is `L^-(n-j)` times a transverse
convex combination of adjacent coarse differences. Therefore H_j is a
finite-range operator on the closed h itself, without a Coulomb inverse;
its row sum is `L^-(n-j)` and its column sum is `L^3(n-j)`. Root restriction
commutes with this interpolation. Set

    zeta_j^loc v=b_j+H_jh.                                    (CJ10)

It has exact top v, the same residuals and curvatures, and differs from any
stationary lift by a nested gradient whose scalar vanishes at every top
root. The nonlinear gauge change extending this first-order change exists
locally; alternatively use the affine local section with tangent CJ10.
Thus it is one admissible representative for all external legs.

For s=n-j, NQ-1 bounds the first term of CJ9 by `C L^-s`; a residual
transport with m=j-1-i costs `L^m L^-3(s+m)=L^-3s L^-2m`.
All composite supports stay within a fixed top distance, so weighting costs
a fixed exponential factor, not a factor per level. The local H_j correction
has the same `L^-s` bound. Consequently, for one fixed positive eta,

    |K_(zeta_j^loc)(b;x)| <= P L^-(n-j) E_eta,T(b/L^(n-j)-x),
    row_m <= P_m L^-(n-j),
    column_m <= P_m L^3(n-j),       0<m<eta.                    (CJ11)

The torus kernel is the periodization; US15–US16 justify separate absolute
row and column sums. Harmonic directions were included by the family
argument, not projected away. There is no `T^-4` constant tail to absorb
against a positive exponential weight.

Insert CJ11 and the already proved curvature/residual kernels into the
actual CJ7 cubic. Expand coefficients and take absolute sums term by term.
The anchored Wilson leg has density `L^4n`, amplitudes `L^-2n,L^-n,L^-n`,
so its exponent is zero and it occurs once. A soft vertex at s=n-j-1 has
density `L^4s`, residual amplitude `L^-3s`, and two contour-potential
amplitudes at most `C_L L^-s`, giving `C L^-s`. Fixed local path lengths,
24L^4 contour labels and Lie brackets contribute constants depending on
N,L; kappas enter their fixed compact bounds. The diameter weight is bounded
by the sum of distances to the common vertex. Hence

    |||D³T_n(1)|||_m <= C_W(m)+C_S(m) sum_(s=0)^(n-1)L^-s
                       <= C_W(m)+C_S(m)/(1-L^-1).              (CJ12)

**Author theorem conditional on the named linear inputs:** CJ11–CJ12 hold
uniformly in n,T and the permitted kappa sequence at the trivial background.
They use the same scale mechanism as NORMS N1-15, with recomputed weighted
constants. They do not claim the old displayed constants survive unchanged.
No equality between a tensor's absolute coefficient sum and its supremum
over two factorized sign vectors is used; those are different norms in
general. The termwise proof establishes the stronger absolute norm CJ2.

## 5. Full-colour second-current transport, with the funnel retained

Keep the first-order representative CJ10. For the actual stationary second
coefficient w2 define at every soft link

    r2_j=w2_(j+1)-Q_j w2_j,    q_j=kappa_j(r2_j-B_j(a_j)).       (CJ13)

q is the second-order **log-coordinate** current. The right-trivialized
current has coefficients

    J1_j=kappa_j r_j,
    J2_j=q_j-(1/2)[a_(j+1),J1_j].

At each intermediate level the lower part of the stationary chain is itself
stationary with its top fixed. Its value is gauge invariant. For the right
current this gives `D_U*J=sum_in J-sum_out Ad_U J=0`. Expanding yields

    d*J2_j=sum_out [a_(j+1),J1_j],
    d*q_j=(1/2)(sum_in+sum_out)[a_(j+1),J1_j].                 (CJ14)

Thus neither J2 nor q is generally ordinarily co-closed. This is exactly
where the order-one straight-adjoint shortcut fails.

The coefficient of the intermediate Euler equation, using CJ7, is

    q_(j-1)=Q_root,j* q_j+kappa_j DB_j[a_j]* r_j,
           =Q_str,j* q_j+E_j,
    E_j=kappa_j DB_j[a_j]*r_j-alpha_j* d*q_j,   1<=j<n,        (CJ15)

where `Q_root,j=Q_str,j-d_(j+1)alpha_j`. This is an exact source identity.
There is no kappa ratio in CJ15 because q includes kappa. Each DB_j term is
the derivative of the actual averaged ordered commutators in CJ3, not the
derivative of an independently ordered endpoint average.

Both terms in E_j are known bilinear functions of the **linear** data:
`a_j r_j` and `a_(j+1) J1_j`. For s_j=n-j-1 their own-unit amplitude is
`C L^-4s_j`, with exponential localization in both external coordinates.
The fixed L factors from alpha/path adjoints are part of C. At the top,
`q_(n-1)=gradient T3(v)`, so CJ12 supplies the required symmetric bilinear
kernel there, including an anchored-column bound. Iterating CJ15 and using
the actual straight adjoint row factor `L^-3m` gives

    q_j=(Q_str^(L^s))*q_(n-1)
        +sum_(i=j+1)^(n-1)(Q_str^(L^(i-j-1)))*E_i,
    s=n-j-1,
    L^-3(i-j-1) L^-4(n-i-1)
                       =L^3 L^-3s L^-(n-i-1).                (CJ16)

The forcing sum is geometric. After one fixed loss of exponential rate,
the bilinear kernel K_qj therefore satisfies

    |K_qj(b;x,y)| <= C L^-3s E_eta,T(b/L^s-x)E_eta,T(b/L^s-y),
    sum_(x,y)|K_qj(b;x,y)| exp(m max(dist(b,x),dist(b,y)))
                                                    <= C_m L^-3s,
    sup_x sum_(b,y)|K_qj(b;x,y)| exp(m diam(b,x,y))
                                                    <= C_m L^s. (CJ17)

The L^s in the last line is the four-dimensional output density L^4s
times amplitude L^-3s. It must not be replaced by the row amplitude.
These estimates are an author consequence of CJ11–CJ12 and the exact
current identities. They concern the second **normalized tree** residual
after subtraction of B_j. They do not assert ordinary co-closedness or
import a one-step inverse as an all-depth inverse. A depth-two actual
nonconstant chain checks the source, kappa and funnel signs below.

## 6. Completed quartic and one precise remaining producer

Put `D a=(d_2a_0,{sqrt(kappa_j)r_j})` and
`Z(a)=({B_p(a_0)},{-sqrt(kappa_j)B_j(a_j)})`. On hidden variations D_h,
`H=D_h*D_h`. Then `F3=<Da,Z(a)>` and
`F4=||Z||²/2+R4`, where R4 is CJ4's two remaining terms plus CJ6.
Let `U_a(w)=<Da,DZ[a]w>`. Thus `S=D_h*Z+U_a`, and exactly

    T4(v)=R4+min_(w_n=0 on slice)
                     {||D_hw+Z||²/2+U_a(w)}
          =R4+||Z||²/2-(1/2)<D_h*Z+U_a,H^-1(D_h*Z+U_a)>.

Equivalently, with `P=D_h H^-1 D_h*`, its last two terms are
`||(1-P)Z||²/2-<D_hH^-1U_a,Z>-<U_a,H^-1U_a>/2`.
This retains the cancellation between the bare commutator square and the
exchange. Taking absolute norms of them separately is not a valid way to
prove a uniform bound: their available estimate is merely O(n). This is
a failed estimate, not an established O(n) growth law for T4.

R4 already has a uniform polarized weighted bound: the bottom Wilson terms
occur once, and every soft term has at least one r. With the vertex density
L^4s its four amplitudes give at least L^-2s. Moreover the soft part of
`D_hw2+Z` is `q_j/sqrt(kappa_j)`, so CJ17 bounds its squared contribution
by a summable L^-2s series. What remains is the bottom second curvature and
the potential legs of w2 in U_a.

Here is a sufficient, source-specific obligation, not a demand for an
unrestricted inverse. Let `g0(v,w)=d_2 w2_0(v,w)`, with the first-order
representative fixed as CJ10. Prove for some C,eta>0, independent of n,T,

    |K_g0(p;x,y)| <= C L^-2n
           E_eta,T(p/L^n-x) E_eta,T(p/L^n-y).                  (CJ18 OPEN)

It suffices to prove the corresponding weighted row and anchored-column
estimates with their proper density factors. The exact source is CJ7 and
the hidden-domain inverse in CJ8. Equivalently its second total plaquette
curvature `F2curv=g0+B_p(a_0)` obeys

    d_2*F2curv=Q_root,0* q_0-DB_p[a_0]* f
                                       +kappa_0 DB_0[a_0]*r_0,
    d_3F2curv=d_3 B_p(a_0),
    harmonic(F2curv)=harmonic(B_p(a_0)).                       (CJ19)

All right sides are now specified by the actual linear data and CJ15's
current, including its top cubic boundary value. Harmonic two-forms in
CJ19 are retained. A massless Hodge inverse cannot be assigned exponential
locality without proving the source cancellations and root constraints.
The existing one-step conditional covariance does not prove CJ18.

**Why CJ18 suffices for the remaining quartic.** Apply periodic TU-3 to
the closed bilinear g0, treating total external momentum as the twisted
momentum and the other external momentum as a parameter. Shrink both
strips a fixed amount and symmetrize. This yields a bottom potential
primitive of amplitude L^-n. Propagate with
`r2_j=B_j+q_j/kappa_j`, whose known bilinear kernels have at most
`C L^-2(n-j)` amplitude (fixed L factors absorbed). NQ-1 makes the forward
sum geometric. The top defect is closed; the analytic one-form lemma with
the extra momentum parameter gives zero at total momentum zero, so the
same local interpolation as CJ10 restores top w2_n=0 without a mean tail.
Consequently an admissible second coefficient has potential amplitude
`L^-(n-j)` and both weighted absolute kernel sums.

Then the bottom part `g0+B_p` has amplitude L^-2n and its square has one
O(1) contribution. The soft squares are already summable by CJ17. In U_a,
the bottom `f a_0 w2_0` term has amplitudes `L^-2n,L^-n,L^-n` against
L^4n output density, and each soft `r_j a_j w2_j` term has a summable
L^-s factor. Polarize before taking the absolute anchored sums. Together
with R4 this proves CJ2's q=4 bound, conditional on CJ18. This is an exact
remaining interface for the finite-part consumer; it is stronger than a
statement restricted to four Cartan legs and includes two neutral external
legs with charged internal exchange.

## 7. Controls, literature and boundary

The [criteria](checks/charged_stationary_jet_criteria.md) predate code.
[Program01](checks/charged_stationary_jet_01.py) builds all 124,416 actual
paired paths on fine6^4/top2^4, with 5,184 hidden links and 7,776 plaquettes.
For its deterministic noncommuting datum the bare quartic is
`-1.0748764611826833`, exchange is `0.8954898046602893`, and CJ8 predicts
`-1.9703662658429726`. Direct quaternion group-action evaluation at three
epsilon values and Richardson extrapolation gives `-1.9703662085730969`.
The discrepancy is `5.73e-8`, below the predeclared tolerance. The second
right-current divergence is `1.2692090879126354`, and its endpoint funnel
is `0.15669247998921373`; the covariant identity agrees to solver accuracy.

The original run had 36/37 predicates: a proposed constant-field
endpoint-deletion detector failed because that particular averaged BCH2
still cancels. Its complete source/output/stderr are preserved with
`_initial` names. It was not evidence of a stationary-jet failure. The
constant noncommuting control has individual BCH2 up to .2 but mean zero,
cubic source norm `1.56e-16`, and zero soft quartic to roundoff. Centering
therefore defeats the proposed constant-field marginal witness. A
post-exposure prospectively declared supplement checks exact group gauge
invariance and the endpoint mutation on a nonconstant field. The final
Program01 output records 40/40 predicates; it also rejects omission, sign
and factor changes in exchange, deleted colour commutators, wrong contour
normalization, wrong counting adjoint, and a gauge-null inverse shortcut.
Counts are predicates, not independent theorems.

The constant cancellation also has an exact proof. For constant a,
`T_(sigma,y)=P_(sigma,y) exp(L a_mu) P_(sigma,y)^-1`, hence its BCH2 is
`L[sum_nu(y_nu-root_nu)a_nu,a_mu]`. Centered averaging kills every offset,
so B_j=0. The linear residual and plaquette curl vanish, while the
plaquette BCH2 is constant; its counting divergence is zero. CJ7 then
gives S=0. The constant-field quartic is the single bottom Wilson
commutator-square term; the `L^4n` count cancels its `L^-4n` amplitude.
This supplies no conclusion for the tested nonconstant source.

[Program02](checks/charged_stationary_jet_02.py) uses the actual depth-two
four-dimensional rectangular periodic chain with top side (2,1,1,1),
intermediate side (6,3,3,3), bottom side (18,9,9,9), and kappas (.7,1.4).
It has 53,136 hidden links and 1,275,264 paired contours. Its 19/19
predicates include intermediate recursion error `3.79e-14`, covariant
current error `7.03e-14`, omitted-DB-source discrepancy `.144986225282`,
and omitted-funnel discrepancy `.140556076342`. Its exchange is
`1.830988205484`. No unexpected predicate failed in this run. The complete
outputs and the preserved initial diagnostic failure are bound by the
[freeze receipt](checks/charged_stationary_jet_receipt.json). These small top
quotients are algebra controls only; the analytic theorem has T>=3.
Neither implementation imports a predecessor helper. Neither finite
control proves depth-uniformity or a continuum theorem.

The primary literature comparison is [Dimock, Covariant Axial Gauge,
arXiv1410.2798v3](https://arxiv.org/html/1410.2798v3), §§3.6,3.8,
Propositions6–7: hard block constraints and axial/Feynman gauge identities
give a constrained covariance with explicit projections. It is an abelian
construction specialized there to d=3, not the nonlinear soft chain here.
[Dimock, Multiscale block averaging for QED in d=3,
arXiv1712.10029v3](https://arxiv.org/html/1712.10029v3), (272)–(303) and
Theorem1/(327), treats nested multiscale regions, hard averages, appropriate
Landau/axial constraints, sufficiently large M, and weights satisfying
`p_j'/p_j<=L^|j-j'|`. Its regularity mechanism is relevant to CJ18; its
dimension, field normalization, constraints and source class do not match
without a new bridge. Its proof explicitly notes that naive smooth
interpolation identities need correction in the multiscale setting. No
unread or unmatched theorem is adopted.

[Balaban CMP102 (1985),277–309](https://doi.org/10.1007/BF01229381) and
[CMP109 (1987),249–301](https://doi.org/10.1007/BF01215223) were screened
at the primary publisher pages. The former abstract concerns regular
configurations with fixed averages; the latter explicitly concerns the
four-dimensional small-field approximation. Only metadata/abstract scope
is used here, not an unread theorem. The existing LITERATURE_BRIDGES,
ASSUMPTIONS_AND_IMPORTS and BALABAN_EXTRACT are retrieval/context sources,
not substitutes for matching hypotheses. This pass obtains no external
all-depth normalized-soft source estimate.

The physics-loop and review-loop methodology is bound to fetched revision
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`. The initial local-main lookup
`9ce38a06...` was stale; its failed methodology reads are superseded.
The read manifest distinguishes full reads, selected proof ranges,
truncated exploratory outputs and bibliographic screening. The current
primitive registry and its declarations supply no Wilson action, soft
normalization or spectral conclusion. No new physical primitive, empirical
fit, audit status or negative-route verdict is proposed. The coordinator
owns integration, publication and fresh independent review.

The exact next mathematical task is CJ18 for the CJ19 source on the stated
root/harmonic domains, potentially via source-specific regularity and
curvature-controlled transport. Uniform finite-u corrections, the complete
finite-part increment, nonlinear complex neighborhoods, interacting
small/large-field control, continuum OS construction and a physical
positive Hamiltonian gap remain separate obligations.
