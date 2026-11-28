State of attack
==============

**Discharged, author proof: quadratic (LC) survives for sufficiently large
L, uniformly in depth.** Sections 1--4 give a local relative gauge, restore
the actual composite parent, cancel the centre-supported gauge from the
seam, and bound the actual iterated trial lift. Section 5 calculates a
transverse face-crossing family with `B=L^n` symbolic. Explicit sufficient
constants are in (CONSTANTS)/(AS), and their complete L-dependence and rate
substitution are in Section 6. A fixed pre-L rate `0<nu<=2^-270` works for
odd `L>=2^54+1`, subject to the consumer's other rate ceilings. These are
very conservative sufficient bounds, not sharp constants.

**Gap: an arbitrarily prescribed larger rate and nonlinear transfer.** For
any other already fixed nu, the displayed (RATE-flat) decides whether this
certificate absorbs; failure of that sufficient bound does not refute
(WAM) or (LC). No nonlinear gluing is attempted. No independent review or
formal verification is claimed. The remaining decision is a check of this
written quadratic proof, then the separate nonlinear obligation if it stands.

**Discharged: provenance and scope.** Source revision:
`45a9f59f9466396cf315529bc794b61691834863`. Author: OpenAI Codex,
2026-11-01. This is a bounded author calculation, not an independent review
or audit. No numerical calculation was run. Only this file was written.
The requested independent-side firewall was maintained.

**Discharged: criteria fixed before calculation.** A kill requires either
(i) an admissible transverse family for which the left side of (LC), divided
by the stated shell endpoint-curvature budget, is unbounded in depth at fixed
L, for every allowed representative/cutoff choice in the construction, or
(ii) an unavoidable nonzero seam for a parent-fixed zero-curvature mode.
Failure of one gauge choice or one right inverse is recorded only for that
choice. Survival requires a written general bound with its coefficient,
shell radius, and kernel moment explicit in L and uniform in depth/volume.
An incomplete proof ends at the exact unresolved inequality. No nonlinear
claim will be made before this quadratic test survives.

**Unchecked: consumer premises.** Nonlinear/class-minimum identification,
admissible intermediate classes, nonlinear trial estimates, and DS's other
hypotheses retain their source labels. Neither the source's numerical
anecdotes nor an inverse's mere finite-dimensional existence are estimates
for this task.

## 1. Linear problem and the true composite

**Discharged: conventions.** Work on a periodic four-dimensional cubic lattice
with `N_mu B` sites in direction mu, `B=L^n`, `n>=1`, and odd `L>=3`.
A fine 1-cochain is a link integral, not a potential divided by its mesh.
The differential is the oriented sum around the next-dimensional cell.
Its square is zero: forward coordinate differences commute, and the two
orders of each distinct pair have opposite orientation signs. All squared
norms are unweighted sums. Normalize su(2) by
`<X,Y>=-Tr(XY)/2`. A plaquette built from exp(tA) has first coefficient
X=dA. Write its second coefficient Y; unitarity gives
`Y+Y^*=X^2`, hence `Re Tr Y=Tr X^2/2`. Thus the quadratic coefficient
of `2-Re Tr U_p` is `-Tr X^2/2=|dA|^2`. The three orthonormal real colour
components consequently add independently at the flat background. The
arguments below apply componentwise. Distances in formulas for supports
are initially fine-coordinate infinity distances divided by B. The final
radius is enlarged by four and therefore works also for the graph distance.

**Discharged: one-dimensional restrictions and their composition.** For an
odd integer b, set m=(b-1)/2 and

    R_b^0 f(j) = b^-1 sum_(a=-m)^m f(jb+a),
    R_b^1 h(j) = b^-1 sum_(a=-m)^m sum_(s=0)^(b-1) h(jb+a+s).

Telescoping the inner sum gives `R_b^1 d=d' R_b^0`. Composing the centered
site averages at n scales gives `R_B^0`: the offsets `sum_j L^j a_j`, with
`|a_j|<=(L-1)/2`, fill the centered interval of B consecutive integers once.
This follows inductively by adjoining L consecutive disjoint intervals of
length L^(n-1). The bond restrictions also compose to `R_B^1`. To verify
this without a symbol argument, apply the differential identity to a site
function and the already proved site composition. On a periodic line every
bond field is `df+c`: subtract its mean and take consecutive partial sums.
Both composite bond maps send c to Bc, so equality on gradients proves
equality on every bond field.

Let P_B^p be the tensor restriction with R_B^1 in the p form directions and
R_B^0 in the other directions. Its coordinate differentials commute, by
the preceding telescoping identity. In particular `d' P_B^1=P_B^2 d`.
The triangular weights of R_B^1 have row sum B and column sum 1; the latter
follows because the two neighboring triangles add to B before division by
B. R_B^0 has row sum 1 and column sum 1/B. Thus P_B^2, specifically in four
dimensions, has row sum B^2 and column sum B^-2. For any matrix A,

    |sum_y A_xy f_y|^2
       <= (sum_y |A_xy|) sum_y |A_xy| |f_y|^2.

Summing over x proves its squared operator norm is at most the product of
these two sums. Consequently

    ||P_B^2||_(2->2) <= 1.                                  (Q2)

Periodizing the positive weights preserves these bounds, even on small tori.

**Discharged: retaining the contour term.** The actual one-step map at 1 is
`Q=P^1-d' C`, where C is the average integral along the block-root contours:
the initial contour enters positively and the terminal contour negatively.
For a gradient, all three paths telescope, giving `Q d=d' ev`, where ev
samples the fine parameter at block centres. Iterating proves

    Q_n=P_B^1-d' C_n,       Q_n d=d' ev_B,
    d' Q_n=P_B^2 d.                                         (TRUE)

For example, on composing one more step the new contour functional is
`C_new=C_one P_old^1+ev_one C_old`. This proves the identity by induction;
no norm of C_n has been assumed. In particular `Q_n H=0` implies
`P_B^1 H=d' C_n H` and `P_B^2 dH=0`. Replacing the first of these by
`P_B^1 H=0` would be unjustified.

**Discharged: which part of the actual trial derivative matters.** Write
T_n for the derivative of the iterated trial lift specified in
`parts/hard-core--excess.md` Sections 2.1--2.2. Its curvature derivative is

    d T_n = V_n^2 d',                                       (TRIAL-d)

where V_n^2 is the composite of that section's tensor 2-form prolongations.
Here is the linearization argument. Products of `exp(tX)` have first
coefficient the sum of the X's, since all products of two first coefficients
have order t^2. Write g_y for the first coefficient of the coarse comb
gauge rooted at y, so g_y(y)=0, and use the convention
`v^(y)=v-d'g_y`. The local trial is `T_1 v-d T_0 g_y`. For adjacent
blocks y,y', the displayed transition has first coefficient

    T_0[g_y-g_y'-g_y(y')]+g_y(y')=T_0(g_y-g_y'),

because T_0 reproduces constants. On a crossing bond x to x' the trial
coefficient is therefore `T_1 v(b)+T_0 g_y(x)-T_0 g_y'(x')`.
Define the fine site function kappa(x)=T_0 g_y(x) in block y. Internal
and crossing bonds are both exactly `T_1 v-d kappa`. Its curl is
`T_2 d'v`, and its parent is
`v-d'[C T_1 v+ev kappa]`. The source's block-constant gauge restoration
adds the fine gradient of a function with these bracketed centre values;
Q d=d' ev makes the parent exactly v at first order. Its curl is still
`T_2 d'v`. Thus the remaining parent defect has zero first coefficient,
and the subsequent correction has zero first derivative at 1. Iterating
proves (TRIAL-d). In particular the linear map itself is a right inverse
without needing a nonlinear norm estimate. This argument uses the
displayed construction, not any numerical test. Consequently

    d T_n Q_n = V_n^2 P_B^2.                                (CQ)

The identity `Q_n T_n=I` also follows directly by differentiating the exact
parent identity, or at first order by the tensor right-inverse identity
and the displayed coarse-gauge correction.

**Discharged: seam algebra.** Put F=dH=dA_t-dA_* and
`g=[d,chi]H`. Using Q_n H=0, (CQ), and `d(chi_b H)=chi_p F+g`, the exact
(SEAM) remainder is

    R_chi = g - V_n^2 P_B^2 (chi_p F+g).                     (R)

Both terms on the right are linear in H. In particular no squared-flux
remainder can replace `Q_n chi_b H`. The rest of the proof must bound g
in a permitted representative and V_n^2 uniformly in n.

## 2. A hand bound for the actual iterated trial

**Discharged: the one-dimensional kernels, with deliberately loose bounds.**
This paragraph supplies the estimates rather than importing the source's
numerical claims. For odd b>=3 use exactly the centered cubic spline and
bubble of the trial:

    N_spl(t) = (4-6t^2+3|t|^3)/6,              |t|<=1,
           (2-|t|)^3/6,                       1<=|t|<=2,
           0,                                |t|>=2;
    xi_j(x)=N_spl(x/b-j),
    beta(x)=c_b [1-(2x/(b+1))^2]^2,            |x|<=(b-1)/2,
            0 otherwise;       R_b^0 beta(0)=1.

For 0<=t<=1 the four nonzero spline weights at centres -1,0,1,2 are
`(1-t)^3/6`, `(4-6t^2+3t^3)/6`,
`(1+3t+3t^2-3t^3)/6`, and `t^3/6`. Adding their numerators gives 6;
multiplying by -1,0,1,2 before adding gives 6t. Translation proves that
Xi reproduces constants and affine functions. Differentiating the displayed
pieces proves `0<=N_spl<=1`, `|N_spl'|<=1`, and `|N_spl''|<=2`.
Here N_spl is the function called N in the source; N(L) below is a
separately defined norm bound.

At least b/3 of the integer sites obey |x|<=b/4: for b=4q+1 or 4q+3 their
number is 2q+1, which has this bound. At these sites the unnormalized
bubble is >=9/16. Thus `1<=c_b<=16/3<6`. Extend that polynomial by zero
at the continuous endpoints |x|=(b+1)/2. Its first derivative is continuous
there; direct differentiation bounds the first and piecewise second
absolute derivatives by `48/b` and `192/b^2`. Integrating over intervals
of length one gives the same bounds for its first and second differences.

Put `a_cj=R_b^0 xi_j(c)` and

    zeta_j(x)=xi_j(x)+sum_c beta(x-cb) [1_(j=c)-a_cj],
    T_b^0 f(x)=sum_j zeta_j(x) f(j),
    eta_j(x)=sum_(k>=j+1) [zeta_k(x+1)-zeta_k(x)],
    T_b^1 h(x)=sum_j eta_j(x) h(j).

The a_cj are nonnegative and sum to one. At an integer x only one bubble
is nonzero; taking one or two differences involves at most two or three
bubbles. The spline part involves at most six translates. Hence the
triangle inequality gives, explicitly,

    sum_j |zeta_j(x)| <= 1+2*6=13,
    sum_j |Delta zeta_j(x)| <= (12+2*48*2)/b <= 2^8/b,
    sum_j |Delta^2 zeta_j(x)| <= (12+3*192*2)/b^2 <= 2^11/b^2.

The zeta support has |x-jb|<=3b. Its difference has at most eight relevant
coarse cuts in the cumulative sum defining eta; its next difference has
at most ten. The total difference of the row sum is zero, so those
cumulative sums vanish beyond the extreme nonzero indices. Therefore

    sum_j |eta_j(x)| <= 2^11/b,
    sum_j |Delta eta_j(x)| <= 2^15/b^2,                     (KER)

and eta has |x-jb|<=4b. These counts bound an interval of length at most
6b+2 by ten coarse cut positions; there is no enumeration by computer.

The disjoint bubble averages give `R_b^0 T_b^0=I` exactly. Summation by
parts in j gives `T_b^1 d'=d T_b^0`. The affine-reproduction identity
then gives `T_b^1 1=1/b`. Thus `R_b^1 T_b^1=I`: it holds on coarse
gradients by commutation, and on the remaining constant bond field by
this last formula. This also proves the tensor chain identities used
in (TRIAL-d), including the constant 2-form normalization b^-2.

**Discharged: no factor C^n is needed.** Let S=L^2 T_L^2, acting on one
component of a coarse 2-form; each of its four tensor factors is either
T_L^0 or L T_L^1. By (KER) its row absolute sum is <=2^44 and the row
absolute sum of a fine-coordinate first difference is <=2^48/L.
Its row sum is exactly one. Relative to a nearest coarse centre, every
coarse index in a row or its first difference is reachable in at most
32 coarse nearest-neighbor steps: each coordinate differs by at most
six, and 4*6<=32. Subtracting the value at that centre before using the
zero row sum of the difference gives

    ||S f||_infinity <= ||f||_infinity+2^49 ||Delta f||_infinity,
    ||Delta S f||_infinity <= (2^53/L) ||Delta f||_infinity.  (REF)

Here the gradient norm is the maximum over the four forward differences,
not their sum. The same estimate holds for each form component. Define

    lambda(L)=2^53/L,
    N_n(L)=1+2^50 (1-lambda(L)^n)/(1-lambda(L)),
    R_n(L)=4 (1-L^-n)/(1-L^-1),
    N(L)=1+2^50/(1-2^53/L),
    R(L)=4L/(L-1).                                         (NR)

For the remainder of the survival bound assume odd `L>=2^54+1`; this
is a sufficient large-block threshold, not a claim of necessity. Applying
(REF) at the successive scales and using
`||Delta f||_infinity<=2||f||_infinity` proves that the normalized composite
`B^2 V_n^2` has infinity norm <=N_n(L)<=N(L). Indeed the gradient at step
j is at most lambda^j times its initial value, so the changes in the
supremum norm add as a geometric series. At n=2 and n=3 the factors are
explicitly `1+2^50(1+lambda)` and `1+2^50(1+lambda+lambda^2)`;
no depth has been replaced by a fixed small number.

Its support radius is <=R_n in top infinity units: one-step radii add as
`4(1+L^-1+...+L^-(n-1))`. The infinity bound, applied to the signs of a
single matrix row, bounds that row's absolute sum. Each entry of V_n^2
is consequently <=N_n/B^2 in absolute value. For a fixed coarse input,
there are at most `(2R_n+3)^4 B^4` possible fine output anchors. The column
absolute sum is therefore <=N_n B^2(2R_n+3)^4. The row/column inequality
proved above now yields

    ||V_n^2||_(2->2) <= N_n(L)(2R_n(L)+3)^2
                      <= C_V(L):=N(L)(2R(L)+3)^2.           (V)

This is where four-dimensional energy scaling is used a second time.
On a small torus use the periodized infinite-lattice kernels; summing
absolute values before periodization gives the same bounds. No volume
factor or estimate on a point-evaluation contour enters (V).

## 3. A local relative gauge, with the true parent restored

**Discharged: an elementary cochain homotopy.** This is an auxiliary gauge
construction, not a replacement of the actual T_n in (R). Use the same
one-step kernels just proved, now at side b=B, and define on a line
`E^0=T_B^0 R_B^0` and `E^1=T_B^1 R_B^1`. Both have range <=6B, row
absolute sum <=2^11, and entries <=2^11/B. There are at most 12B+1
entries in a column, so its absolute sum is <2^15. Their 2-norms are
therefore <=2^15. Define a local map from bonds to sites by

    (k h)(x)=sum_z E^0(x,z) Integral_(z to x) h,

where the integral is the oriented consecutive sum on the line. The
integral for h=df is f(x)-f(z), so `k d=I-E^0`. Every bond sequence on
the covering line has a potential obtained by consecutive partial sums;
using `d E^0=E^1 d` proves `d k=I-E^1` on every sequence. Locality then
periodizes these identities. The affine identity also gives k(1)=0,
so no constant-period ambiguity has been introduced.

Each row of k has absolute sum <=6B*2^11. Each entry is <=2^11 and
can be nonzero only at distance <=6B, so its column absolute sum is
<2^15 B. The row/column inequality proves `||k||_2<=2^15 B`.

In four dimensions let E be the tensor cochain map, using E^0 or E^1
according to degree in an axis. In the tensor complex define

    K = k_1 + E_1 k_2 + E_1 E_2 k_3 + E_1 E_2 E_3 k_4,

with the sign on k_i equal to (-1) to the sum of the preceding coordinate
degrees. A differential in another coordinate anticommutes with this
signed k_i, whereas E_j commutes with differentials. Thus the terms from
different coordinates cancel in dK+Kd; the remaining terms are
`(I-E_1)+E_1(I-E_2)+E_1E_2(I-E_3)+E_1E_2E_3(I-E_4)=I-E`.
This explicitly proves

    dK+Kd=I-E,       ||K||_(2->2)<=4(2^15)^4 B=2^62 B.    (HOM)

The range is <=6B in each coordinate, since every product has at most
one factor acting in any one coordinate. The norm includes all form
components: each signed tensor term has the displayed product norm,
and there are four terms.

**Discharged: the permitted representative.** For H in ker Q_n let
F=dH and `H_0=K F`. Since `P_B^1 H=d' C_n H`, (HOM) on 1-forms gives

    H=H_0+d psi,      psi=K H+T_B^0,4 C_n H,              (GAUGE)

where T_B^0,4 is the tensor site prolongation. In particular dH_0=F.
Let J put a coarse site value on its fine block centre and zero on all
other fine sites. Set

    h=H_0+d J ev_B psi.

Then `h-H=d(J ev_B psi-psi)`, whose gauge parameter is zero at every
top centre. By (TRUE), Q_n h=0 exactly. This is a parent-fixed change
of endpoint representatives; e.g. keep A_t and replace A_* by A_t-h.
Its curvature and its Maxwell minimality are unchanged. Intermediate
images are the images of this representative, not separately frozen
intermediate link values. This is the terminal-parent setting of (LC).

For every set X of fine bond anchors, locality and (HOM) give

    ||1_X H_0||_2 <= 2^62 B ||1_(X expanded by 6B) F||_2.  (LOCAL)

The centre-supported gradient in h need not have this bound. It is
retained explicitly, not charged to (LOCAL).

**Discharged: zero-curvature test.** If F=0 then (GAUGE) says H=d psi.
Since Q_n H=0, ev_B psi is constant on the connected coarse torus.
Subtract that constant from psi and gauge H to zero with a parameter
vanishing at the top centres. Thus there is no parent-fixed
zero-curvature mode left over in this flat periodic problem. This proof
also excludes a hidden harmonic-period exception; it does not rely on a
Poincare lemma recalled without its hypotheses.

## 4. The quadratic shell estimate

**Discharged: a cutoff that does not turn the root gauge into curvature.**
Let D be any set of fine anchors. For D empty or the whole torus take the
constant cutoff; the conclusion follows immediately from P_B^2 F=0.
Otherwise let t(x) be the fine infinity distance to D's complement divided
by B and put

    chi(x)=theta(t(x)),     theta(t)=t^2/4 for 0<=t<=2,
                                      1 for t>=2.

Distance to a set changes by at most the distance between its arguments,
by the triangle inequality. Since 0<=theta'<=1, neighboring site values
of chi differ by <=1/B. Put chi_p=chi at the plaquette anchor. On a bond
use chi at its initial site, except that every bond incident to a top
centre receives chi at that centre. No bond has two such centres because
B>=3. For every plaquette and every boundary bond,
`|chi_b-chi_p|<=2/B`; the anchor and the relevant centre are at most two
fine steps apart. The core and exterior agree with D beyond a fixed shell.

If q is supported on the top centres, then

    chi_b d q = d q_chi,       q_chi(c)=chi(c)q(c).         (ROOT)

Indeed each nonzero bond of dq has just one centre as an endpoint, and
its multiplier is exactly chi at that endpoint. Applying d proves that
the root-supported part of h in Section 3 contributes zero to g.
It also contributes zero to the correction curvature: Q_n of the
right side of (ROOT) is a coarse gradient, and (TRIAL-d) kills its curl.
Thus the large, unestimated norm of J ev_B psi never enters the energy.
This is what the relative gauge on the shell can do. Merely saying
`Q_n H=0` does not itself bound H or its commutator.

**Discharged: bounding the two first-order terms.** Use the representative
h of Section 3 and let g=[d,chi]h=[d,chi]H_0. A plaquette has four sides;
a bond belongs to six unoriented plaquettes in dimension four. Consequently

    ||g||_2^2 <= (96/B^2) ||1_X H_0||_2^2,
    ||g||_2 <= 2^66 ||1_(S_10(D)) F||_2,                 (G)

where X consists of bonds in the affected stencils. For the second line,
g lies within infinity distance 3 of the transition boundary, its bonds
within distance 4, and (LOCAL) enlarges this by 6; also sqrt(96)<16.
All shell radii in this paragraph are in top infinity units.

A row of P_B^2 reads anchors within distance 2 of its coarse anchor. If
all of them have chi=0 or all have chi=1, that row of P_B^2(chi F) is
zero, the latter case because P_B^2 F=0. Every remaining row lies within
distance 4 of the boundary and reads only S_6(D). Restrict to those output
rows before restricting the input; this avoids creating artificial terms
at the edge of the input restriction. The norm (Q2) therefore proves

    ||P_B^2(chi F)||_2 <= ||1_(S_6(D)) F||_2.              (CF)

Using (R), (Q2), (V), (G) and (CF), define

    D(L)=(1+C_V(L))*2^66+C_V(L),
    C_seam(L)=2 D(L)^2,
    r(L)=4[16+2R(L)]=64+32L/(L-1),
    K(z)=1_(z=0),             M_*(L)=1.                   (CONSTANTS)

The curvature of V_n^2 P_B^2 g is supported within infinity distance
5+R_n of the boundary; that of V_n^2 P_B^2(chi F) within distance 4+R_n.
The radius 16+2R dominates these radii and the input radius 10. Multiplying
by four covers graph distance as well, so the final displayed r works for
either of the usual lattice distance conventions. Since
`|F|^2=|dA_t-dA_*|^2<=2(|dA_t|^2+|dA_*|^2)`, the complete bound is

    sum_p |R_chi(p)|^2
       <= C_seam(L) sum_(p in S_r(L)(D))
                              [|dA_*(p)|^2+|dA_t(p)|^2]. (LC-flat)

There are no omitted correction tails in this linear construction.
K is a symmetric probability kernel on the fine torus and its exponential
moment is exactly one at every rate, volume, depth and L. Every occurrence
of n before the supremum is displayed in N_n and R_n; no n remains in
(CONSTANTS). The proof covers any pair in the same terminal linear fibre,
so in particular the specified trial and Maxwell minimizer. It does not
assert this estimate with frozen fine boundary data or at a nonflat
background.

**Discharged: coefficient for the quadratic E-SHELL.** The competitor is
`A_chi=A_*+chi_b h-T_n Q_n chi_b h`, with the changed minimizer
representative understood. Applying Q_n shows it is admissible. Write
`v_p=(1-chi_p)dA_*+chi_p dA_t`. For 0<=chi_p<=1,

    |v_p|^2 <= (1-chi_p)|dA_*|^2+chi_p|dA_t|^2,
    |v_p+R_chi|^2 <= 2|v_p|^2+2|R_chi|^2.

The first inequality follows by subtracting
`chi_p(1-chi_p)|dA_t-dA_*|^2`; the second follows from
`2|v_p||R_chi|<=|v_p|^2+|R_chi|^2`. Away from S_r the curvature is the
chosen endpoint curvature. Dropping the negative reference energy inside
the shell therefore bounds the complete quadratic replacement cost by

    A_s(L) sum_(S_r(D)) (|dA_*|^2+|dA_t|^2),
    A_s(L)=2+2 C_seam(L)=2+4 D(L)^2.                      (AS)

The difference between competitor energy and minimum energy is nonnegative.
Rearranging it, with the reference A_t inside D and A_* outside, gives
quadratic (E-SHELL) with exactly (AS), r and M_* above. This is an energy
comparison; root gauges have not been asserted to give nonlinear field
matching or a nonlinear admissible chain.

## 5. A transverse mode crossing a face, with the composite constraint

**Discharged: an actual endpoint family, not arbitrary fibre data.** Choose
M>=4 top cells in direction 1 and any positive transverse periods. Take
one colour, `v_2(j)=a exp(i p j_1)`, other components zero, where
`p=2 pi k/M`, `k!=0 mod M`. Real and imaginary parts give real fields;
complex notation only combines the two independent calculations. Fine
potentials of the form `A_2(x)=f(x_1)` have sole curvature
`F_12(x)=f(x_1+1)-f(x_1)`. In every axis-ordered rooted contour the integral
of this field is the centred displacement in direction 2 times a function
independent of that displacement. Its block average is zero. This remains
true after each step and after averaging contour orders. Thus for this
family the *true* Q_n is, exactly,

    (q_B f)(j)=sum_(u=-(B-1)/2)^((B-1)/2) f(jB+u),
    B=L^n,

on component 2, and zero on the others. This is not an assumption that
the contour term vanishes for arbitrary H.

Let W_n^0 be the composition of the actual T_L^0 kernels of Section 2.
A representative of the actual trial is
`f_t=B^-1 W_n^0 v_2`; its curvature is fixed by (TRIAL-d), and its parent
is q_B f_t=v_2 by the successive right-inverse identities. To compute the
minimum put

    t_j(x)=#{(u,s): |u|<=(B-1)/2, 0<=s<B, x=jB+u+s},
    C_B F(j)=sum_x t_j(x)F(x),
    b_j=v_2(j+1)-v_2(j).

Telescoping gives `C_B d=d' q_B`. The rows t_j have values
`1,2,...,B,...,2,1`. Their squared norm and adjacent overlap are

    a_B=(2B^3+B)/3,       b_B=(B^3-B)/6,
    C_B C_B^*=a_B I+b_B(S+S^-1).

For example these are `B^2+2 sum_(h=1)^(B-1) h^2` and
`sum_(h=1)^(B-1) h(B-h)`. The formulas for the sums follow by induction
from the differences h and h^2, respectively. For this Fourier mode set

    gamma_B(p)=a_B+2b_B cos p >= a_B-2b_B=(B^3+2B)/3>0,
    F_*(x)=gamma_B(p)^-1 sum_j t_j(x)b_j,
    F_t(x)=B^-1 d W_n^0 v_2(x).                            (MODE)

C_B F_*=b and F_* is orthogonal to ker C_B, so it is the minimum in
this scalar curvature problem by expansion of the square. Its fine sum
is zero since `sum b=0` and each triangle has mass B^2. Integrate it
periodically to f_*. Then d'(q_B f_*-v_2)=0; adding a fine constant fixes
that remaining parent constant, since q_B sends it to B times itself.

This is also a minimum among general four-dimensional fields with the
true parent constraint. To check this rather than assume a symmetry
reduction, put `u=(C_B C_B^*)^-1 b`. Taking adjoints of C_B d=d' q_B gives
`d^*F_*=q_B^* d'^*u` on the line. A coarse multiplier with component 2
`B^3 d'^*u`, constant in the other coordinates, has zero coarse divergence.
The contour term in Q_n^* therefore vanishes on it. The adjoint path
restriction on this multiplier is exactly the displayed line expression:
its three transverse factors are 1, B^-1, B^-1 and its direction-1
factor is B^-1 q_B^*, giving B^-3 before the chosen factor B^3.
Consequently `<dA_*,dZ>=0` for every Q_n Z=0. Expanding
`||d(A_*+Z)||^2` proves full constrained minimality.

**Discharged: the face seam and its ratio.** Now h=f_t-f_* has zero sum
on every centered B-block. For a face-normal cutoff chi(x_1) as in
Section 4, set chi_b on the nonzero direction-2 bonds equal to chi(x_1).
It is already constant on those bonds incident to a top centre. A parent
cutoff may be the same scalar sampled at its bond anchor; Q_n h=0 makes
its value drop out of the following commutator. Then

    g_12(x)=Delta chi(x_1) h(x_1+1),
    [Q_n,chi]h(j)=sum_(u=-(B-1)/2)^((B-1)/2)
                                chi(jB+u)h(jB+u),
    R_12 = g_12 - B^-1 W_n^1 C_B(chi F+g_12),             (FACE)

where W_n^1 is the corresponding composite one-dimensional bond lift.
Thus the correction uses the first-order commutator, with its actual
block face and all n scales. No O(a^2) term has been substituted for it.
Both terms of R scale as a, and all compared energies scale as |a|^2.

For a site x in a B-block I,
`h(x)=B^-1 sum_(z in I)(h(x)-h(z))`. Cauchy--Schwarz in this average and
then along each path of at most B bonds gives

    sum_(x in I)|h(x)|^2 <= B^2 sum_(edges inside I)|d h|^2.

Since |Delta chi|<=1/B, summing over the blocks meeting the seam gives
`||g||_2<=||1_(an enlarged shell) F||_2`. Applying (Q2), (V) and (CF)
to (FACE) therefore gives the sharper family bound

    ||R||_2^2 / sum_(S_r(D)) (|F_*|^2+|F_t|^2)
       <= 2[1+2 C_V(L)]^2.                                (FACE-ratio)

When the denominator is zero the numerator is zero by the same inequality;
no division is then taken. The number of transverse fine sites multiplies
both sides and cancels. Formula (MODE) keeps B=L^n, and (NR) keeps the
separate geometric depth factors of the actual trial. This family has no
depth-growing seam ratio for the large L covered by Section 2. It is not
an independent numerical check of (LC-flat): it is a written transverse
specialization with a second, blockwise proof of the potential bound.

## 6. Rate substitution (one page)

**Discharged: the effective quadratic constants and exact L-dependence.**
For odd L>=2^54+1, with no dependence on depth or volume, this construction
has

    R=4L/(L-1),                  N=1+2^50/(1-2^53/L),
    C_V=N(2R+3)^2,               D=(1+C_V)2^66+C_V,
    A_s(L)=2+4D^2,               r(L)=64+8R,
    K=delta_0,                   M_*(L)=1,
    beta_*(L,nu)=2(2+4D^2) sinh[nu(64+8R)].               (RATE-flat)

These are proved upper-bound choices, not optimal constants. Substitution
into (RATE-exact) is precisely `beta_*(L,nu)<1`. When it holds, layer
integration of quadratic E-SHELL gives

    E_*(w) <= [1+D_A(L,nu)s] E_t(w),       0<=s<=nu,
    D_A=4 A_s r cosh(nu r)/(1-beta_*).                    (WAM-flat)

Indeed the shell integral is at most `2 sinh(sr)w`; hence
`(1-beta(s))E_*(w)<=(1+beta(s))E_t(w)`, and
`sinh(sr)<=sr cosh(nu r)` supplies the displayed coefficient. This also
covers s=0 and zero trial energy without dividing by that energy.

**Discharged: a fixed pre-L rate really is available.** On the stated
L range, `N<2^52`, `R<=6`, `C_V<2^60`, `D<2^128`, `A_s<2^259`,
and `r<=112<128`. For 0<=t<=1, `sinh t<=2t`: integrate cosh t<=cosh 1<2,
where `e<3` follows from its series and `k!>=2^(k-1)` for k>=2.
Consequently any fixed `0<nu<=2^-270`, chosen before L, gives
`beta_*<=2^268 nu<=1/4`. No post-L rate choice is needed for this certificate.
The same bound controls `2 A_s r cosh(nu r)nu`, so the stronger convenient
(RATE) also holds. Take L odd above both this threshold and the consumer's
other lower thresholds.

**Implication: a prescribed rate is not silently changed.** For a rate
already fixed at some other value, use (RATE-flat), not the small-rate
example. The displayed coefficient decreases with L to

    C_infinity=121(1+2^50),
    A_infinity=2+4[(1+C_infinity)2^66+C_infinity]^2,
    beta_infinity(nu)=2 A_infinity sinh(96nu).

If beta_infinity(nu)<1, some sufficiently large odd L satisfies
(RATE-flat); this follows directly from the displayed rational limits
and continuity of sinh. If beta_infinity(nu)>=1, these conservative
bounds cannot absorb at that rate for any finite L. That is a limitation
of this certificate, not a lower bound on the best shell constant and
not a counterexample to (LC) or (WAM). The input specifies a symbolic nu,
not a numerical one; the parameter conditions above are the rate verdict.

**Implication: substitution into DS.** Its first two orders deliver
`alpha=min(delta_#/2,nu)/2`. Thus the unchanged consumer requires
`mu<=alpha`, equivalently `2mu<=nu` and `4mu<=delta_#`.
A compatible pre-L choice is nu below all its inherited ceilings and
2^-270, then mu<=alpha, then L. This preserves the mapped order.
If an already fixed nu fails this certificate, direct (WAM-req) at that
nu remains the option preserving the promised DS rate. A post-L rate
nu(L) can instead be tested in (RATE-flat), but it changes alpha to
alpha(L), and requires changing mu and downstream profiles whenever
nu(L)<2mu. It does not preserve the existing interface merely by increasing
a prefactor. No need for that reordering has been proved here. All these
DS statements are interface implications: nonlinear WAM and DS's other
premises have not been supplied by a flat calculation.

## 7. Limits and verification record

**Gap: scopes not established.** The norm estimate (V) here is proved for
odd L>=2^54+1. Its huge sufficient threshold does not determine what
happens at smaller L. The constants are intentionally inefficient; a
failed (RATE-flat) at a larger prescribed nu is not evidence that sharper
constants fail. No nonlinear seam, frozen-fine-data extension, finite-flux
parent correction, or admissible nonlinear intermediate chain has been
constructed. None is inferred from the fact that a flat gradient has
zero curl. In particular this note supplies no nonlinear (GLUE-E), no
full nonlinear (WAM-req), and no existence proof for Yang--Mills.

**Unchecked: independent validation.** The displayed arguments have been
author-checked only; they have no independent reader or formalization in
this session. A meaningful further check would rederive (HOM), (ROOT),
and the stability of the actual spline composite, since these are the
load-bearing steps. Repeating scalar Gram arithmetic alone would not
check the four-dimensional seam.

**Discharged: source and work boundary.** The source is the pinned HEAD
stated at the top, not the older internal provenance of the two input
notes. Read GOAL and FINISH, both requested excess notes, the mapped map
and constants order, the trial construction in the excess part Sections
2.1--2.2, the composite-adjoint definition, the relevant fibre-propagator
setting and flat estimates, the localized-competitor definition of T_n,
and the CRUDE/DS consumer. Only the definitions and the explicitly rebuilt
linear identities were used as premises for (LC-flat); the source's
reported computations were not evidence. Initial truncated locator outputs
were not proof coverage; the consequential map, trial and consumer ranges
were read separately. The workflow was read with `git show HEAD:...`
because this is a sparse checkout. The physics-claim-reviewer skill was
used only for the scoped mathematical check; no landing process was run.
The final mechanical check found HEAD unchanged, no source modifications,
only this untracked output in worktree status, and no whitespace diagnostics
from `git diff --no-index --check /dev/null` on this file. These are file
checks, not mathematical validation.
No forbidden-side source, gate, external proof account or historical
numeric log was opened. No numerical computation, script, lock, subagent,
audit, commit, push or post was run. Only this output file was written.

**Discharged: verdict.** Quadratic (LC) **survives**, for odd L>=2^54+1,
with C_seam=2[(1+C_V)2^66+C_V]^2, A_s, r and M_* exactly as displayed.
There is no depth-growing loss in this estimate and no surviving
parent-fixed zero-curvature obstruction. Its shell absorption survives
at every fixed pre-L rate 0<nu<=2^-270 (with the other source ceilings),
and more generally exactly when the displayed sufficient (RATE-flat)
condition is met. At a larger prescribed rate where that certificate
fails, absorption remains undecided; (WAM) has not been refuted.
Nonlinear gluing remains outside this test.
