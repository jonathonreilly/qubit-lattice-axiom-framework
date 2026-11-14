# Uniform volume-first Gaussian one-loop coupling

Author argument, awaiting fresh independent review. This unit proves the
uniform one-loop bound and the bracket for **every** scale increment in the
supplied normalized Wilson/S4′ model, using the precise internal linear,
stationary-jet and full-colour residual lemmas listed below. It rebuilds the
finite-part argument with the corrected bubble coefficient. It does not
prove a finite-u remainder estimate, nonlinear RG, continuum existence or a
positive physical continuum Hamiltonian mass gap. Both physical targets
remain open.

The constructive strategy and block-field mathematics build on Balaban and
Dimock. The perturbative comparison literature is credited in Section 9;
its theorems are not substituted for the model-specific estimates here.
The coordinator owns publication and audit operations. This is an author
unit under PROCESS_LIGHT, not an audit disposition.

## 1. Model, exact inputs and statement

Fix d=4, SU(N), N>=2, an odd L>=3, and **one fixed kappa>0 at every level**.
Use integrated link variables in each level's own unit lattice and counting
inner products, with `<X,Y>=-Re tr(XY)/N`. The normalized tree phase is

    F_n(U_0,...,U_n)=sum_p (1-Re tr U_p/N)
                        +kappa sum_(j<n,c) phi_(M_j,c)(U_(j+1),c),
    phi_M(V)=[max_(W in SU(N)) Re tr(W^-1 M)-Re tr(V^-1 M)]/N,
    T_n(V)=stationary value of F_n with U_n=V; T_0=S_W.       (UL1)

The stationary branch is the branch through the identity, on the rooted
hidden gauge complement. Its gauge-invariant value is independent of that
choice of representative. The S4′ mean is exactly `(24 L^4)^-1` times the
sum over block offsets and all 24 coordinate orders, with the **same** order
at the two endpoints. Blocks are centered at `LX+(L-1)/2`; centered offsets
about zero are equivalent. Neither an independent endpoint average nor an
uncentered root is used.

These are internal mathematical inputs, with their supplied-model scope:

| Input consumed | Exact content used |
|---|---|
| LINEAR_PACKAGE and its repaired snapshot derivations; UNIFORM_SOFT_MINIMIZER US1–US16 | The actual quadratic chain, root identity, uniform unprimed complex strip, curvature/residual kernels, own-unit row/column counts and exact periodization. |
| CHARGED_STATIONARY_JET CJ11–CJ17 and its review | One common localized linear representative; full-colour cubic bound; actual second-current recursion, including root funnels. These use the repaired periodic TU-3 primitive, NQ-1 and local root interpolation at their stated scopes. |
| BOTTOM_SECOND_CURVATURE BC3, BC23–BC26 and its fresh review | Source-specific second-curvature estimate, both density bounds and the full-colour fourth-jet bound, including cubic exchange. |
| RESIDUAL_FULL_COLOUR FC3–FC17 and its review | Fixed-domain Gram/ghost identities and `Rho_n^full=0` for each fixed n, in the original volume-first a.e. Bloch convention. |

The fresh bottom-curvature review has SHA256
`d4597d612af42aa994475767fe4f33828b8eb2fa4e2762d696fb529e6c5c134b`;
its scoped confirmation is of BC3/CJ18 and BC26 under the named
normalized-tree/linear/current contracts. It is not a review of this unit.
The source/read manifest binds the exact upstream bytes and read coverage.
In particular no generic all-depth hidden inverse, uniform nonlinear
analytic neighborhood, finite-u Hessian estimate, or unproved historical
primed strip is included as an input.

For a unit regular Cartan H use the plane wave
`v_(x,1)=epsilon cos(P x_2+vartheta) H`, other components zero, and average
over vartheta. Its Wilson epsilon-squared density is

    w(P)=lambda(P)/4,       lambda(P)=4 sin²(P/2).             (UL2)

For the volume-first one-loop functional define

    V_perp[T](V)= (1/2) log det(Hess_X T(V exp X)|_0+D_V D_V*)
                                      -(1/2) log det' Delta_V,
    a(T)=lim_(P->0) { beta_(V_perp[T])(P)-sigma_perp log(1/P) },
    sigma_perp=-7N²/(8pi²)=-(21/22) beta0,
    beta0=11N²/(12pi²),       u=1/g²=2N/g_std².               (UL3)

Here beta at nonzero P is the epsilon-squared density divided by w(P).
Determinants mean their full-colour Gaussian Taylor coefficients on the
prescribed free complements, followed by the thermodynamic/Bloch integral;
they do not mean a nonlinear pseudodeterminant through a changing rank.
Let `a_n=a(T_n)` and let `B_n=sum_(k<n)b_k=-beta[Gamma_(0->n)]` be FLOW's
original one-loop cumulative change in u, with `B_0=0`.

**Theorem.** In this supplied model, using the internal lemmas above, there
is a finite constant C_FP depending on N,L,kappa and the stated uniform
linear/jet constants, but not on n,j or an auxiliary torus, such that

    |a_n-a_0| <= C_FP                       for every n>=0,
    B_n-B_j=beta0 (n-j) log L+a_n-a_j       for every 0<=j<=n,
    |B_n-B_j-beta0 (n-j) log L| <= 2 C_FP.                    (UL4)

The coefficient is defined volume first at each fixed depth. The uniform
bound is subsequently over those coefficients. No simultaneous n,P,T
limit or finite-T coupling bound is asserted.

## 2. The actual tree actions occupy one common J class

Write `|||K|||_m=sup_x1 sum_(x2,...,xq) |K(x1,...,xq)|
exp(m diam(x1,...,xq))`, with top-lattice l1 diameter; colour and link
indices are included in the absolute sums. The class needed below is

    beta[T]=1,    max_(q=2,3,4) |||D^q T(1)|||_m <= C_J,
    H_T=D²T(1) >= c_E d* d.                                 (UL5)

It also includes reality, gauge invariance, translations, signed coordinate
permutations B4 and charge conjugation, and analytic Taylor germs.

All these symmetries follow from UL1. Gauge transformations act at the
retained roots; the paired path family is permuted by the spatial
symmetries, and complex conjugation preserves each real trace and the
SU(N) maximum. Changing a gauge slice only changes the hidden
representative. Uniqueness of the local stationary orbit therefore passes
these symmetries to its value. Its fixed-depth analytic germ follows from
positivity of the hidden Hessian on that complement. Constant hidden
fields are fixed by the zero top boundary through the soft chain; gradients
vanishing at the roots are removed, not inverted. No depth-independent
radius of this nonlinear germ is needed.

**Quadratic bound.** With `r_(n-1)=v-Q a_(n-1)`, the envelope identity is
`H_n v=kappa r_(n-1)`. US11 bounds the top-residual kernel by
`C exp(-eta|X-y|)` uniformly in n. Thus its absolute exponentially weighted
row sum is uniform. At n=0 the finite-range Wilson kernel supplies the
same conclusion. **Cubic and quartic bounds.** CJ12 supplies the complete
full-colour cubic coefficient. BC26 supplies the complete fourth
coefficient; its proof uses

    T4=R4+(1/2)||D_h w2+Z||²+<Da,DZ[a]w2>,                  (UL6)

with the actual stationary w2. The ell^4 bottom count cancels ell^-4;
the soft square sums L^-2s and the soft mixed term sums L^-s. This is why
the cubic exchange cannot be dropped or estimated separately by a
marginal level count. Polarization and anchored-column bounds in BC23
give the coefficientwise diameter norm in UL5, not just bounds on
factorized test fields. Choose one m below all three available rates,
with a fixed further loss if required when comparing diameter weights.
Enlarge C_J to include Wilson.

Exact periodization also matters. At each fixed depth the rooted hidden
Hessian is a finite Laurent matrix in top Bloch variables. On real fibres
it is positive on its fixed gauge complement, including the retained
harmonic sector. Compactness gives a fixed-depth positive minimum and a
fixed-depth complex inverse. Fourier inversion and periodization identify
its finite-torus inverse. Differentiating stationary equations produces
finite **tree** contractions at any fixed Taylor order. Periodizing each
external leg of such a contraction gives the finite-torus coefficient:
internal image labels are eliminated uniquely along a rooted tree. The
US/CJ/BC estimates supply the uniform bounds for orders two through four.
Consequently the same infinite-lattice kernels underlie all T>=3 tori;
no independently chosen volume-dependent jets enter UL5.

**Ellipticity.** LINEAR_PACKAGE Lemma 2.7 bounds the minimum quadratic
ENERGY, not its Hessian:

    E_n(v) >= c_LP ||dv||²,
    c_LP=2kappa/[pi²(kappa+4pi² Rbar)],
    Rbar=1+1/(L²-1)+kappa/9.                                (UL7)

Its dual formula has `Pdual_mu^-1=phi/beta_mu`,
`beta_mu<=kappa+4pi²Rbar`; minimizing over the longitudinal multiplier
gives `|nu wedge v|²/|nu|²`, and `phi/|nu|²>=4/pi²`.
Multiplication by kappa/2 gives UL7. Since `E_n=(1/2)<v,H_n v>`,
`H_n>=2 c_LP d*d`. Hence `c_E=min(1,c_LP)>0` is a common safe choice.

**Tree normalization.** This can be checked directly, without a claim
about a nonlinear background. Let G_k be the transverse inverse of H_k.
The actual one-step Gaussian Schur formula at coarse momentum p is

    G_(k+1)(p)=kappa^-1 P_perp(p)
      +L^-4 P_perp(p) sum_K Qtilde_K P_T(q_K) G_k(q_K)
                            P_T(q_K) Qtilde_K* P_perp(p),
    q_K=(p+2pi K)/L.                                       (UL8)

Root covariance `Q_root d=d ev` makes this a formula on the gradient
quotient. The factor L^-4 is the counting Fourier normalization.
For K!=0, q_K stays off zero as p tends to zero. For K=0,
`Qtilde_0(0)=L I`, since every actual contour integrates a constant link
field to L times that field. Starting with `G_0=P_T/lambda`, induction
in UL8 gives

    lambda(p) G_(k+1)(p) -> L^-4 L² L² P_perp =P_perp.

The nonzero aliases and kappa^-1 term vanish after multiplication by
lambda(p). Analyticity and B4 invariance then give `beta[T_k]=1` for
every k. This proves the missing J1 match. UL7 excludes extra zeros
(doublers), so the inverses used in the induction are valid off p=0.
The straight-map symbol used in all alias estimates is
`ell D_ell(q_mu) product_alpha D_ell(q_alpha)`, up to its centering phase:
the **extra leg-direction Dirichlet factor** is retained.

Thus UL5 is satisfied with one `(m,C_J,c_E)`. This discharges common-J
membership using the exact normalized-tree/linear contracts, without
assuming jet convergence or a uniform nonlinear analyticity radius.

## 3. Normalization and the Gaussian determinant dictionary

For an HS-orthonormal basis e_a and FLOW basis `t_a=sqrt(N)e_a`,
`F_FLOW=F_HS/N` and

    T_FLOW(b)=T_HS(sqrt(N)b)/N,
    D^q T_FLOW=N^(q/2-1) D^q T_HS,   q=2,3,4.                (UL9)

The factors are 1, sqrt(N), N respectively. UL1–UL8 already use FLOW
coordinates, so no further colour normalization is applied to them.
The original stiffness ratio is kappa at every step; the present theorem
does not replace it by a depth-dependent bare ratio kappa u_j/u_0.

For N>=3 the polar U(N) maximizer may not lie in SU(N). The exact
normalized phase is phi in UL1. At the identity its difference from the
old polar `ktilde` bookkeeping is the scalar `d(M)=O(A^6)`:
`arg det M=O(A^3)` and the maximizing trace defect is quadratic in that
phase. This is an analytic statement in the local branch. Therefore
their jets through order five, their stationary values through order four,
and the background two-jet of their Gaussian Hessians agree. The
maximizer displacement starts at degree three and cannot alter the
second background derivative of the normalizing prefactor. This is the
local dictionary used here, not equality at general backgrounds.

The field-dependent leading normalizer is retained. In the one-loop
Laplace dictionary of the normalized composite kernel, its covariance
factor combines with coarse gauge integration to give

    G_perp,n=(1/2) log det_(ker D_0*) H^natural
                       +(1/2) log det_(ker D*) (P_perp C P_perp),
    G_gh,n=(1/2) log det' Delta_V-(1/2) log det' Delta_(W*).
                                                                    (UL10)

Here W* is the actual rooted stationary background, and H^natural is the
Hessian after minimizing the relative coarse gauge coordinate. It
annihilates fine gauge directions because that partially minimized
function is gauge invariant and W* is its critical point. The scalar
identity behind UL10 is

    det C=det_perp(P_perp C P_perp)
                    det'(D*D)/det'(D*C^-1D),                (UL11)

on the specified complements, with null-space Grams treated separately.
Joint Laplace integration supplies `+(1/2)log det Hess_h Psi` and the
normalizer supplies `+(1/2)log det C`; UL11 cancels the coarse gauge
covariance block. The fine gauge quotient contributes
`-(1/2)log det' Delta_(W*)`. These signs give UL10 and, after the
reviewed zero-marginal drift/relative-gauge terms are included in the
complete residual, the original B_n identity used in Section 8.

The two harmonic Grams are not interchangeable. In the neutral sector
let `h=4(N-1)` and ell=L^n. The fine-to-joint and coarse-to-joint harmonic
graphs have Grams `(1+ell^-2) I_h` and `(1+ell²) I_h`. The scalar root
Schur factor is `det' Delta_f=ell^4 det A det' S`, and the completed
ghost is `det'(Fbar_1 d)=ell^4 det A det' Delta_c det R_c^(1/2)`.
The root projection is `P_int+J P_c0 J*`, not just P_int. These are
FC3–FC7's counting-norm formulas. They leave the background-independent
constant `-h log ell` in the complete neutral residual on rho=0.
It has zero background coefficient; it was not discarded before taking
the determinant identities. FC10's residual determinant weights are

    L_per: +1/2,    Delta_c: -1,    G_c: +1/2,    H_h: -1/2. (UL12)

In particular V_perp in UL3 has a **half** ghost, and UL10 supplies the
additional half-ghost scale difference. Neither may be counted twice.
Right-translated Haar measure has a background-independent density at
zero quantum field; its quantum-quadratic correction enters higher order
in 1/u. The normalized soft prefactor already in UL10 does have a
background quadratic term. The exact finite-u spread Hessian is a
different object: its leading one-loop normalizer contribution is kept
here, while no estimate on its finite-u remainder is inferred.

## 4. Ward identities give the required improved vertices

Here is a direct replacement for the rank computation used in the older
JET-MARG discussion. Let T,T' belong to UL5 and set delta equal to the
maximum of their three weighted jet differences. Weighted summability
bounds all momentum derivatives of these symbols on a fixed smaller
complex tube: for any fixed multi-index a the bound is
`C_a(m) delta`, by `r^s exp(-mr/2)<=C_s(m)`.

In the exponential chart the infinitesimal gauge variation is

    Theta_b=-d lambda_b-(1/2)[X_b,lambda_x+lambda_y]
                       -(1/12)[X_b,[X_b,d lambda_b]]+O(X^3).

Differentiating invariance gives

    T2[X,d lambda]=0,
    T3[X,X,d lambda]=-T2[X,[X,lambda_x+lambda_y]],
    T4[X,X,X,d lambda]=-(3/2)T3[X,X,[X,lambda_x+lambda_y]]
                         -(1/2)T2[X,[X,[X,d lambda]]].       (UL13)

The one-jet is zero by global colour invariance. Link-centered Fourier
coordinates remove orientation shifts under point inversion. Quadratic
and quartic tensors are then even, and cubic tensors odd, in all momenta.
For the quadratic degree-two tensor B4 covariance permits only
`a|k|² delta_mu,nu+b k_mu k_nu+c delta_mu,nu k_mu²`.
Transversality forces `b=-a,c=0`; beta=1 fixes a. Thus
`delta H=O(delta |k|^4)`.

For the cubic difference the degree-one tensor, with arbitrary fixed
colour indices, is `A_(mu,nu,rho,alpha) p_alpha+
B_(mu,nu,rho,beta) q_beta`. UL13 makes it transverse in both independent
legs p and q: its lower-jet right side has degree at least four.
Contracting p first makes B=0 (the p_mu q_beta monomials are independent).
Contracting q then makes A=0. Odd parity therefore gives
`delta T3=O(delta r^3)`, where r is the norm of the independent momenta.
The constant quartic difference is annihilated by contraction with an
arbitrary momentum, since UL13's right side starts at degree three.
It is zero; even parity gives `delta T4=O(delta r^2)`.
This argument applies to all colours, including two neutral external
legs and charged internal legs; it uses no Cartan-only quartic shortcut.

For the determinant it is convenient to use the symmetric background
split `U=e^(B/2) e^X e^(B/2)`. It differs from `U=e^B e^Y` by the exact
linear quantum transformation `Y=Ad_(e^-B/2) X`, of determinant one.
Writing this orthogonal matrix as M gives `H_s=M*H_r M`, `D_s=M*D_r`,
and hence `O_s=M*O_r M` and `Delta_s=Delta_r`, including off shell.
The vector determinant is exactly unchanged when its complement and
induced measure are transported with M. This is not an exact invariance
of the prescribed FIXED free-complement determinant. The Hessian in each
split still includes the force times the second quantum derivative of
the nonlinear map to action-log coordinates; off-shell stationarity is
not assumed.

Here is the correction on that fixed regulator. Let P0 project onto the
free vector harmonics, Q=1-P0, `O0=0 direct-sum D` with D positive on Q,
`O=O0+e O1+e^2 O2+...`, and `M=exp(e A)`, A*=-A. Put
`U=P0 A Q`, `F=P0 O1 Q`. Expanding `M*O M` and the compressed logarithm
gives

    [e^2]{log det_Q(M*O M)-log det_Q O}
          =2 Re tr(D^-1 F*U)-tr(U*U).                     (UL13a)

Indeed the off-diagonal part of `Q[O1,A]Q` is `F*U+U*F`, and that of
`(1/2)Q[[O0,A],A]Q` is `-(D U*U+U*U D)/2`. Within-Q commutator terms
cancel against the corresponding bubble terms, since conjugation entirely
within Q preserves its determinant. These signs correspond to `Y=M X`
and `O_s=M*O_r M`; UL13a is an e^2 coefficient, not the second derivative.
It generally is nonzero. The vector determinant's outside factor 1/2
is applied to this correction as to every other vector term.

For the actual single external plane wave, U and F connect a free
constant mode only to the shifted momenta +/-P e2. Their ranks and
matrix entries are bounded independently of volume; UL14 bounds D^-1
there at each fixed P!=0. The correction after division by T^4 is
therefore at most `T^-4 C_J(P)`, with finite C_J(P), and vanishes in
the prescribed volume-first limit. This does not give a uniform finite-T
statement as P tends to zero. The scalar Delta is unchanged already
before this limit.

Thus the symmetric split may be used for the same volume-first Bloch
coefficient. Together with link centering it gives ordinary inversion
parity to the vertices. The local analytic change of coordinates and its
retained off-shell force term cannot lower the jet-difference orders just
found. This also supplies the two-power improvement in the Wilson versus
continuum comparison in Section 6, in that same volume-first convention.

Put `O_T=H_T(B)+D_B D_B*`, `G_T=O_T(0)^-1`. For real k!=0, UL5 and the
exact longitudinal eigenvalue lambda(k) give

    O_T(k)>=min(c_E,1) lambda(k) I,
    |partial_k^j G_T(k)|<=C |k|^(-2-j),
    |partial_k^j (G_T-G_T')(k)|<=C delta |k|^-j,  j<=2.       (UL14)

The last estimate follows by differentiating
`G_T-G_T'=-G_T(H_T-H_T')G_T'`; the fourth-order numerator is essential.
The same constants apply away from zero by compactness and UL5.
For the external wave, let V_+,V_- be the two O1 transfer vertices and
S the phase-averaged O2 vertex, with no factorial hidden in O2. Jointly
near k,P=0, with `r=(|k|²+P²)^(1/2)`,

    V=O(r),   delta V=O(delta r³),
    S=O(1),   delta S=O(delta r²),                            (UL15)

and up to two momentum derivatives reduce these powers by their order.
For Wilson versus its leading continuum operator the same estimates hold
with delta replaced by a fixed constant. They follow by the local
plaquette expansion, UL13 and the symmetric split just specified, not by
assuming pointwise cancellation between singular diagrams.

## 5. Corrected finite-part difference theorem

For `O=O0+epsilon O1+epsilon² O2+...`, ordinary matrix differentiation gives

    [epsilon²] Tr log O=Tr(G O2)-(1/2)Tr(G O1 G O1).           (UL16)

After phase averaging, **both** ordered transfers (+,-) and (-,+) remain.
The factor inside this formula is 1/2; the separate outside weight for
the vector determinant in V_perp is another 1/2. The printed 1/4 bubble
in the old UIR55 FP display is incorrect. Using the same gauge fixing
for T,T', the half-ghost cancels in their difference, but is retained in
each individual finite part.

Let f_T(k,P) be the complete phase-averaged vector integrand, including
that outside weight, and set D=f_T-f_T'. Expanding a difference of a
bubble one factor at a time, using UL14–UL15, gives

    |D(k,P)| <= C delta [1+r²(|k|^-2+|k+P e2|^-2+|k-P e2|^-2)
                  +r^4 |k|^-2(|k+P e2|^-2+|k-P e2|^-2)].    (UL17)

For example, replacing one propagator makes it bounded, giving
`r²/|k+P e2|²`; replacing one cubic vertex gives
`r^4/(|k|² |k+P e2|²)`. Tadpoles give `1+r²/|k|²`.
This checks each pole separately. At fixed P!=0 each possible center
has exponent at most two, strictly less than d=4. A total homogeneity
count alone would not justify the integral.

On `|k|<=2|P|`, set k=|P|z. UL17 is bounded by delta times integrable
functions with distinct centers 0,+e2,-e2 on a fixed ball. Hence

    integral_(|k|<=2|P|) |D(k,P)| dk <= C delta P^4.          (UL18)

On `2|P|<=|k|<=r0`, all `|k+tP e2|` are comparable to |k| for |t|<=1.
Differentiating the actual products gives

    |partial_P^j D(k,tP)|<=C delta |k|^-j, j=0,1,2.          (UL19)

The remaining compact region has the same bound with |k| replaced by
one. This controls all two-center poles; neither an omitted center nor
a fictitious uniform mass was used.

We next remove the order-zero and order-one integrals. At P=0 the
constant Cartan field is pure gauge on the infinite lattice. In a root
sector of charge q the flat-background symbol is, up to a determinant-one
conjugation, the zero-background symbol with `k_1 -> k_1+q epsilon cos
vartheta`. Thus its trace-log epsilon-squared integrand is
`(q²/4) partial_(k1)^2 log det O_T(k)`, with the relevant determinant
weight. The affine gauge parameter can be implemented by compact cutoffs
in these jet identities: all moments of the exponentially summable
kernels exist, so boundary terms tend to zero. This is an infinite-lattice
statement, not the assertion that a finite torus toron is pure gauge.
It integrates to zero on the Brillouin torus. The small sphere
removed about zero has boundary flux `O(r³ r^-1)=O(r²)`; the periodic
outer faces cancel. Neutral q=0 contributes zero to this particular flat
field statement. Hence `integral D(k,0)=0`. Reflection and phase averaging
make the integrated coefficient even in P. Its first derivative is
integrable, so `integral partial_P D(k,0)=0` as well.

Subtract these two Taylor terms before dividing by P². On the outer
region the Taylor remainder is dominated by `C delta |k|^-2`, integrable
in four dimensions, and converges pointwise to `(1/2)partial_P²D(k,0)`.
On the inner ball UL18 contributes O(delta P²) after division; the
subtracted zero and first Taylor terms have integrals O(delta P^4) by
UL19 at P=0. Consequently

    lim_(P->0) [integral D(k,P) dk/(2pi)^4]/P²
        =(1/2) integral partial_P²D(k,0) dk/(2pi)^4,
    |limit|<=C delta.                                      (UL20)

Since w(P)/P² tends to 1/4, the finite-part difference exists and obeys

    |a(T)-a(T')| <= C_* delta.                              (UL21)

The assertion so far means that existence of either reference finite part
implies existence of the other. All constants in UL14–UL21 depend only
on `(N,m,C_J,c_E)`. The reference existence and its absolute logarithmic
coefficient are established next.

The same bounds hold with vector external momentum and polarized external
link directions. The finite difference has a second-order Taylor tensor
at zero; background gauge invariance makes it transverse, and B4 and
colour invariance identify its marginal coefficient with the plane-wave
coefficient above. Thus this is the beta functional of the original
action convention, not an independently projected charged observable.

## 6. Wilson reference: finite part, logarithm and neutral contribution

This is a local proof of the needed lattice-to-continuum step. In the
symmetric split the leading Wilson operator in a root sector is
`O_c=(-i partial-q A)^2 I+2 i q F`, while the scalar ghost is
`(-i partial-q A)^2`. For `A_1=epsilon cos(Px_2+vartheta)`, write
`J=E12-E21`. The Fourier transfer and seagull vertices are

    V_+=-q k_1 I+qP J,    V_-=-q k_1 I-qP J,
    S=(q²/2) I.                                           (UL22)

The scalar has J=0. These follow by expanding the covariant derivative
and the curvature term; the Wilson plaquette expansion supplies exactly
this leading curvature Hessian. Higher terms satisfy UL15, with two
extra powers, as explained using the symmetric split.

Let f_c be the weighted sum of these continuum vector and half-ghost
integrands using UL16, summed over colours. It is homogeneous of degree
-2 in (k,P). Choose a radial smooth cutoff chi supported in a small
ball of the Brillouin cube and equal to one on a smaller ball. Put
`R=f_W-chi f_c`. Near the three small centers, the two-power improvement
gives exactly the bounds UL17–UL19 with a fixed constant. Away from them
R is smooth. Thus the Taylor-subtracted integral of R, divided by P²,
has a finite limit, by the proof of UL20.

The full Wilson integral has zero constant and linear Taylor terms by
the flat-background Ward calculation. Its continuum comparison can
therefore also be Taylor-subtracted. For P>0, change variables k=Pz:

    P^-2 integral chi(k)[f_c(k,P)-f_c(k,0)-P partial_P f_c(k,0)] dk
      = integral chi(Pz) J_c(z) dz,
    J_c(z)=f_c(z,1)-f_c(z,0)-partial_P f_c(z,0).              (UL23)

Factors `(2pi)^-4` are understood on both integrals. Near 0,+e2,-e2
the separate pole exponents are two, with the subtracted derivative
at zero of degree -3; all are locally integrable in d=4. At infinity,

    J_c(z)=|z|^-4 h(z/|z|)+O(|z|^-5).

Subtract `1_(|z|>=1)|z|^-4 h` to obtain an absolutely integrable function.
Dominated convergence applies to that difference. The subtracted part
is a radial integral `A integral_1^infinity chi(Pr) dr/r`, equal to
`A log(1/P)` plus a finite cutoff constant. This proves an actual finite
limit after subtracting the logarithm. It does not use real smoothness
as a replacement for a pole estimate, or set external momentum to zero
inside a logarithmically divergent integral.

For completeness the coefficient is computed directly. Expanding UL16
at large |k| gives, per unit q²,

    h_S(n)=n_1²-4n_1² n_2²,
    h_V(n)=4 h_S(n)-2.

On S3, rotational symmetry gives `<n_1²>=1/4`. Rotating
`n_1 -> (n_1+n_2)/sqrt(2)` gives `<n_1^4>=3<n_1²n_2²>`; squaring
`sum n_i²=1` then gives `<n_1²n_2²>=1/24`. Hence the scalar mean is
1/12. The vector spin term follows from `tr J=0,tr J²=-2`; its mean
is -5/3, twenty times the scalar with opposite sign. The radial measure
is `|S3|/(2pi)^4=1/(8pi²)`. Thus

    C_S=q² c_g,  C_V=-20 q² c_g,  c_g=1/(96pi²).             (UL24)

There are **two real quantum components per positive root pair**. With
the outside weights +1/2 and -1/2 in UL3 this gives, per positive root,
`C_V-C_S=-21q²c_g`. Write `H=i diag(h_1,...,h_N)` with
`sum h_i=0,sum h_i²=N`. Then
`sum_(i<j)(h_i-h_j)²=N sum h_i²-(sum h_i)²=N²`.
Finally division by UL2 multiplies a raw P² coefficient by four:

    sigma_perp=4(-21)N²c_g=-7N²/(8pi²),
    sigma_extra_ghost=-4N²c_g=-N²/(24pi²),
    sigma_full=-88N²c_g=-11N²/(12pi²).                     (UL25)

These computations establish UL3 in the original u convention. The
conversion is `beta0=2N (2 b0)` with `b0=11N/(48pi²)`; using b0 itself
as the u slope would be a normalization error.

The neutral colour sector is included in the finite part of R above.
It has no root-charge logarithm, but its lattice finite part is nonzero.
Here is an explicit check independent of the continuum comparison.
For commuting neutral fields the Wilson Hessian contains its full
plaquette cosine. If `{T_a}` is the normalized Cartan basis, then
`sum_a tr(H² T_a²)/N=N-1`. On a periodic fine lattice of volume V_f,
the diagonal of the exact-two-form projector
`d (d*d+dd*)^+ d*` is `(1/2)(1-1/V_f)` for each plaquette orientation:
its rank is `3(V_f-1)` and there are `6 V_f` plaquettes. Expanding the
cosine, including the outside half determinant, and dividing by the
Wilson quadratic energy gives

    a_W,neutral=-(N-1)/4,
    a_W,neutral^(finite V_f)=-(N-1)(1-1/V_f)/4.              (UL26)

The neutral ghost has no background vertex. UL26 is FC1's coefficient;
it survives in a_0 and is not assigned to the logarithmic continuum
piece. Similarly every neutral quartic tadpole of T_n stays in a_n.
The full-colour difference estimate UL21 bounds those finite terms
along with the charged terms.

Wilson therefore has a finite a_0. Applying UL21 to the common class
gives all a_n and

    |a_n-a_0|<=C_*(C_J+C_W)=:C_FP<infinity.                  (UL27)

No numerical value of a_0 or C_FP is fitted or used as an input.

## 7. Full-colour residual and the order of limits

Set `W_perp=V_perp[S_W]` and
`Delta_n=G_perp,n-W_perp composed with W*+V_perp[T_n]`.
The consumed FC16 theorem is

    Rho_n^full=lim_(P->0) beta_(Delta_n)(P)=0
                                                   for each fixed n. (UL28)

Its content is stronger than cancellation of a charged continuum
symbol. The actual determinant combination uses UL12 and both Grams
in Section 3. Neutral tadpoles, the root-mean term and the harmonic
constant are kept. The neutral mixed vertex has a Ward zero O_n(P);
the actual linear residual is O_n(P²), so after Wilson normalization
the remainder is O_n(P+P²). Charged mixed loops have separate pole
powers (1,2),(2,1),(2,0); the repeated-residual worst case is (2,2),
which is multiplied by P^4 and gives `P² log(1/P)` after normalization.

For clarity, the regulator identification is part of UL28. On periodic
free complements, `G O=1-P_0`. Every exceptional word from completing
the determinant cancellation contains a Fourier kernel projector, which
anchors loop momentum to 0 or +/-P. After the true acoustic zero is
removed, the other factors are bounded high blocks or fixed-n multiples
of `1+P^-2`. Their normalized trace is bounded by
`C_n T^-4 (1+P^-2)^(m_n)` and vanishes at fixed n and fixed P!=0.
Dyadic mesh counting for each remaining pole of exponent s<4 is bounded
by `C r^(4-s)`. The periodic Taylor regulator and the common root-pair
antiperiodic regulator therefore yield the same a.e. Bloch integral.
Only after that identification is P sent to zero. The antiperiodic
root-pair calculation is not asserted to define a new full SU(N) bundle.

These are the actual source and review arguments behind UL28; no
uniform bound on C_n, no finite-T coefficient limit at P=0, and no
exchange of n with the infrared limit is extracted from them.

## 8. Scale transfer and every-increment bracket

The original sequential and composite definitions of B_n agree at this
Gaussian order. In a local rooted gauge the joint hidden Hessian has
successive Schur complements equal to the Hessians of the partially
minimized phases. Thus its determinant factors into the one-step
determinants; the normalized soft prefactors and gauge factors are
additive after taking logarithms. This is FLOW's F-tel identity
`Gamma_(0->n)=sum_(k<n) Gamma_k composed with Phi_(k+1<-n)`.
At each fixed k the rooted one-step free Hessian has no zero mode:
zero curvature and zero soft residual would be a removed root-zero
gradient, while its constant field is fixed by the zero top boundary.
Compact real Bloch fibres and analytic coefficients give a fixed-k
exponentially local inverse. The now-available second through fourth
tree jets therefore supply the fixed-k local Hessian of Gamma_k. Its
beta coefficient is unchanged by the stationary transport, by the
scale calculation below. Consequently `-beta[Gamma_(0->n)]=sum b_k`.
No finite-u flow estimate is used in this Gaussian Schur argument.

The fixed-n linear stationary map has low-alias amplitude
`ell^-1 v (1+O_n(P))` at fine momentum P/ell. Its nonzero transverse
aliases are O_n(P³). To see the latter directly in UL8, the stationary
fine component is
`L^-4 G_k(q_K) Qtilde_K* H_(k+1)(p) v`. For K!=0 the transverse
straight-map factor vanishes to first order in p, its fine inverse is
bounded, and `H_(k+1)(p)=O(p²)`. Root funnels are coarse gradients and
drop out of that transverse factor. Composing finitely many steps
proves the same assertions at depth n. The extra Dirichlet factor
specified after UL8 is present throughout.

Only the linear map enters the background two-point function of
W_perp composed with W*: its first variation at the identity is zero
by colour invariance. Fine momentum conservation pairs each alias with
its opposite. At any fixed n, nonzero aliases contribute O_n(P^6) to
the density and hence o(P²). For the smooth component the three scale
factors are

    ell^4 (fine sites per top site),
    ell^-2 (squared field amplitude),
    ell^-2 (quadratic momentum).                            (UL29)

They cancel in d=4. More exactly
`ell² lambda(P/ell)/lambda(P)=1+O_n(P²)`, and an O_n(P) amplitude
error times `log(ell/P)` tends to zero for fixed n. Thus

    beta_(W_perp composed with W*)(P)
             =sigma_perp log(ell/P)+a_0+o_n(1),
    beta_(V_perp[T_n])(P)=sigma_perp log(1/P)+a_n+o_n(1).

Combining with UL28 gives the exact fixed-depth identity

    beta[G_perp,n]=sigma_perp n log L+a_0-a_n.               (UL30)

The additional ghost in UL10 compares the **same** nearest-neighbor
covariant Laplacian in fine and coarse own units. Its reference finite
part cancels by UL29 and its scalar logarithm from UL24 gives
`beta[G_gh,n]=-(beta0/22)n log L`. Keeping the zero-marginal normalizer
drift and relative-gauge terms in the complete residual, the original
Gaussian coupling is consequently

    B_n=-beta[G_perp,n]+(beta0/22)n log L
       =beta0 n log L+a_n-a_0.                              (UL31)

Subtract UL31 at two arbitrary fixed integers j<=n. This gives the
middle equation of UL4 without any limiting exchange. Apply UL27 twice
to obtain its last inequality. At j=0 the sharper error bound is C_FP;
n=j and n=0 obey the formula exactly.

For HINT2_55 R2.3 L4, take
`beta'=beta''=beta0>0` and `R'=2 C_FP`. This is the full B-BR quantifier,
not merely a bound on B_n starting from zero left unstated at other
starting scales. No convergence of a_n or b_n was used or proved. As
a matter of logic a bounded oscillating sequence a_n would still obey
this bracket and could give nonconvergent successive differences.

This closes the Gaussian one-loop ingredient within the supplied model
and the named internal linear contracts. The finite-u estimates SF-g,
RLF-delta, SF-cont and SF-infinity, connected source return and large
fields, continuum/nonfree hierarchy and physical Hamiltonian gap remain
separate obligations. Neither the bounded one-loop remainder nor fresh
review alone establishes any of them.

## 9. Literature, controls and provenance

The existing LITERATURE_BRIDGES B10/B11 and ASSUMPTIONS_AND_IMPORTS are
respected as context, not additional theorem premises. In particular:

- Kim–Adams–Lee, [arXiv:0710.1930](https://arxiv.org/abs/0710.1930),
  Sections 2–5, gives a comparison framework for logarithmic one-loop
  lattice integrals. Its hypotheses include infrared finiteness and
  absence of doublers; its rate proof invokes a lattice power-counting
  theorem. UL14, UL17–UL23 establish the needed estimates directly for
  this class, including the separate moving poles. No such rate theorem
  is imported here.
- Lüscher–Weisz, [hep-lat/9504006](https://arxiv.org/abs/hep-lat/9504006),
  Section 5 and the inspected Section 6 identities, explains the lattice
  background gauge framework. Its left quantum split is related to ours
  by adjoint coordinates; its all-order perturbative conclusion is not
  used. UL13 and the flat-background shift argument supply the Ward
  steps required here.
- Balaban's and Dimock's block-field and localization methods remain
  the constructive background for the internal linear and stationary
  sources. No d=3 hard-constraint covariance theorem is relabeled as
  the present d=4 soft stationary chain.

The source/read manifest records bounded external coverage rather than
claiming a full read of unconsumed all-order arguments. Numerical criteria
precede any new program. The evidence below is to falsify action, bubble,
colour and density normalization errors; the proof above, not finite
sampling, establishes uniformity.

The [prospective criteria](checks/uniform_one_loop_criteria.md) preceded
[the program](checks/uniform_one_loop_01.py). Its first and only run has
24 passing predicates: 16 ordinary checks and eight intentional mutations
detected. [The full output](checks/uniform_one_loop_01_output.txt) and
[structured results](checks/uniform_one_loop_01_results.json) are retained.
The actual SU(2) charged flat-block coefficient is -3/16 for Wilson and
-387/1568 for the normalized rectangle family member. Direct determinant
polynomials and full tadpole/bubble traces agree exactly. The incorrect
quarter-bubble gives -3/32 in the Wilson case and is rejected; direct
finite-epsilon determinant averages agree within 2.21e-7 over the four
prespecified comparisons. The independent 3^4 neutral Wilson calculation
gives -20/81 after division by the actual wave density 3/4, with error
below 3e-17. Removing that neutral term or its finite harmonic correction
is detected. These are finite Gaussian blocks, not numerical assertions
of the all-depth theorem.

The [input/read manifest](checks/uniform_one_loop_read_manifest.json)
records exact consumed bytes and the [freeze receipt](checks/uniform_one_loop_receipt.json)
binds all owned evidence. Prior frozen author and reviewer units were not
edited. Fresh review of this new argument is the next obligation.
