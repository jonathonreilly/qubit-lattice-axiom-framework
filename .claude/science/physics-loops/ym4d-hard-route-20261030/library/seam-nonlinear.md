State of attack
===============

**gap — stop at (NL-pay) below.** The first new cost in a finite
multiplicative transfer is the fourth power of the relative link logarithm.
The flat homotopy estimates its second moment, not the required fourth
moment in an admissible nonlinear alignment. The displayed estimate
(SEED) below is valid at arbitrary backgrounds and exposes the precise
missing payment. No parent-restored field X_D or admissible intermediate
chain has been constructed. Thus nonlinear (GLUE-E) and its rate condition
remain undecided. This is not a counterexample to them.

**discharged — provenance and stopping rule.** Source:
`0ce2437ea63b5e7b35fe4ef99bda3869d76fb587`, 2026-11-01. Author: OpenAI
Codex; an exact runtime model/effort receipt is not available in this
session. This is one reader's written test, not an audit, formal
verification, or a claim of independence in model from the quadratic
note's Codex author. No numerical computation was run. The criteria saved
before calculation were: check the quadratic argument first and stop on
an error; otherwise require exact parent preservation, class membership
at every intermediate level, complete replacement cost, and (RATE-exact)
at a rate fixed before L. Stop at the first missing estimate. The three
mandatory diagnostics concern statements actually used below.

| Statement | Label and result |
|---|---|
| Flat (LC), its root cancellation and depth bounds | discharged within the flat setting; no error found in the checked argument |
| Finite multiplicative seed estimate (SEED) | discharged by the matrix calculation below; no parent or class assertion |
| Nonlinear relative alignment/payment (NL-pay) | gap; the first stopping point |
| Corrected nonlinear (GLUE-E), including all intermediate classes and (RATE-exact) | unchecked beyond that stop; no constants certified |

## 1. What survives from the quadratic note

**discharged — scope of the check.** I read `seam-quadratic.md` in full,
including its transverse specialization and rate arithmetic, and the actual
trial construction in `parts/hard-core--excess.md`, Sections 2.1–2.3.
The following checks concern the flat derivative, not the asserted finite
nonlinear lift estimates or class-minimum identification in those sources.
Write B=L^n. All norms here are unweighted link/plaquette sums.

**discharged — the two gauge identities.** For the source's one-dimensional
operators, telescoping gives R_B^1 d=d'R_B^0. The bubble averages give
R_B^0 T_B^0=I; summing the four cubic-spline weights gives 1 and their
first moment gives x/B. The bubble correction has zero affine moment.
Consequently T_B^1 1=1/B and R_B^1 T_B^1=I, including the constant bond
mode. With E^p=T_B^p R_B^p and

    k h(x)=sum_z E^0(x,z) Integral_(z to x) h,

one obtains k d f=f-E^0 f directly, and d k h=h-E^1 h by taking
consecutive partial sums for h on the covering line. For h=1, k h=0 by
the affine moment, so periodization introduces no lost constant mode.
Tensoring with the signed homotopy gives dK+Kd=I-E: its four diagonal
contributions telescope as

    (I-E_1)+E_1(I-E_2)+E_1 E_2(I-E_3)
                              +E_1 E_2 E_3(I-E_4)=I-E.

The off-diagonal terms cancel because the signed k_i anticommutes with
differentials in other axes. Thus, using the true Q_n=P_B^1-d'C_n,
Q_n H=0 gives H=K dH+d psi. Put H_0=K dH and
h=H_0+dJ ev_B psi. Then h-H has a gauge parameter zero at every top
centre and Q_n h=0. For q supported at those centres, assigning chi(c)
to every bond incident to c gives chi_b dq=d(chi q), exactly. This
explains why the large centre contribution is absent from the flat curl
estimate. It does not bound its link norm.

**discharged — depth and trial check.** Direct differentiation of the
trial's crossing bond gives

    T_1 v(b)+T_0 g_y(x)-T_0 g_y'(x'),

so its discrepancy from the tensor lift is a fine gradient. The
block-constant parent gauge restoration is another gradient. The remaining
parent residual has zero first coefficient; hence the subsequent
correction has zero derivative at 1. Therefore dT_n=V_n^2 d' and
dT_n Q_n=V_n^2 P_B^2, as used in the quadratic note.

Its one-axis bounds can be checked from the displayed spline and bubble:
c_B<6, absolute first/second bubble differences at most 48/B and
192/B^2, respectively, give row bounds 13, 2^8/B, 2^11/B^2 for zeta
and its differences. Taking the cumulative sums defining eta gives
2^11/B and 2^15/B^2. For S=L^2 T_L^2, subtracting the nearest coarse
value in a zero-sum difference row, whose indices are at most 32 steps
away, gives

    ||S f||_inf <= ||f||_inf+2^49 ||Delta f||_inf,
    ||Delta S f||_inf <= (2^53/L)||Delta f||_inf.

Iteration therefore sums a geometric series, rather than multiplying a
fixed bound n times. The resulting N=1+2^50/(1-2^53/L) and
R=4L/(L-1) give ||V_n^2||_2<=N(2R+3)^2 by the row/column estimate.
The homotopy has range 6B per axis and norm at most 2^62 B: each
one-axis E or k/B has norm at most 2^15 and there are four tensor terms.
Counting four sides per plaquette and six plaquettes per bond then gives
the source's localized bound for [d,chi]H_0. These checks retain both
terms of its exact remainder g-V_n^2 P_B^2(chi dH+g).

**discharged — flat constants only.** With C_V=N(2R+3)^2 and
D_0=(1+C_V)2^66+C_V, the resulting choices are

    A_s^flat=2+4D_0^2,   r^flat=64+8R,   M_*^flat=1.

For odd L>=2^54+1, N<2^52, R<=6, C_V<2^60, D_0<2^128,
A_s^flat<2^259 and r^flat<128. Hence sinh t<=2t for 0<=t<=1
gives 2A_s^flat sinh(nu r^flat)<=2^268 nu<=1/4 for
0<nu<=2^-270. None of these estimates controls a fourth power of a
finite relative connection or preserves a nonlinear intermediate class.

## 2. The first finite-displacement cost

**discharged — normalization and exact gauge factors.** Use
a(P)=1-Re Tr(P)/2. This is half the quadratic note's 2-Re Tr(P);
rescaling every energy by the same factor leaves (GLUE-E) unchanged.
For matrices use |Z|_F^2=Tr(Z*Z)/2. Then a(P)=|I-P|_F^2/2 for
P in SU(2). A site gauge acts by X_xy -> q(x)X_xy q(y)^-1;
the four factors on a plaquette telescope to conjugation by q at its
anchor, preserving a(P) exactly.

**implication — a seed, conditional on an alignment; not X_D.** Fix the
specified U,T with terminal parent V. Permit a gauge g equal to 1 at
the top centres, with T^g still in the same terminal class-chain fibre,
and a separate site gauge q supported on those centres. The restriction
on T^g is imposed here, not inferred from an unproved nonlinear chart;
g=1 always qualifies. Finding an alignment with the required estimate
is part of (NL-pay).
Write

    T^g_xy = q(x) exp(h_xy) U_xy q(y)^-1.                 (ALIGN)

No size of log q is charged. Set bar T=exp(h)U=q^-1.T^g and
bar Y_b=exp(chi_b h_b)U_b. At a centre c put
q_chi(c)=exp(chi(c) log q(c)), choosing a logarithm once, and put
q_chi=1 elsewhere. Thus it is 1 in the exterior and q in the core.
Put Y=q_chi.bar Y. This treats the root gauge as a group gauge, not as
exponentiated additive gradients.
It preserves all plaquette actions of bar Y. In the core Y=T^g and in
the exterior Y=U; both assertions are exact wherever the cutoff is
constant on the involved bonds and sites. The imposed endpoint
restriction does not make M_n(Y)=V, nor show that Y's intermediate images
are class. Those assertions are not used below.

For any fixed g,q, link logarithms in (ALIGN) exist in SU(2): unitarity
and determinant 1 give the form [[a,b],[-conj(b),conj(a)]], with
|a|^2+|b|^2=1. Expanding this matrix in I,i sigma_1,i sigma_2,i sigma_3
gives real coefficients u_0,u with u_0^2+|u|^2=1. Choose
cos t=u_0, sin t=|u|, 0<=t<=pi. When |u|>0 put J=i u.sigma/|u|;
then J^2=-I and the element is cos t I+sin t J=exp(tJ), by grouping
even and odd exponential powers. At -I choose any unit J, and at I
choose logarithm zero. No smooth choice in the endpoints is claimed.
The problem is an estimate for a suitable alignment, not pointwise
existence of these logarithms.

**discharged — matrix remainder, with its proof.** Orient a plaquette's
four sides cyclically. Move the unperturbed link matrices to the right;
the relative increments become alpha_1,...,alpha_4 transported by
unitary conjugation, including the inverse-link convention. Thus

    P_barT = (prod_(j=1)^4 exp(alpha_j)) P_U,
    P_barY = (prod_(j=1)^4 exp(chi_j alpha_j)) P_U,
    s_p = sum_j |alpha_j| = sum_(b in boundary p) |h_b|.

For G(t)=prod_j exp(t beta_j), differentiate twice. Terms with both
derivatives on one factor have norm at most |beta_j|^2; the ordered
cross terms have norm at most |beta_i||beta_j|. Here an su(2) matrix
i v.sigma has operator norm |v| because its square is -|v|^2 I;
unitary multiplication preserves |.|_F. It follows that
|G''(t)|_F<=(sum_j |beta_j|)^2. Twice integrating gives

    |G(1)-I-sum_j beta_j|_F <= (sum_j |beta_j|)^2/2.

Apply this once with beta_j=chi_j alpha_j and once with beta_j=alpha_j.
For tau=chi_p in [0,1], with |chi_j-tau|<=2/B as in the quadratic
cutoff, the difference from the chord satisfies

    P_barY = (1-tau)P_U+tau P_barT+E_p,
    |E_p|_F <= (2/B)s_p+s_p^2.

The chord need not be a group element; this is a matrix identity. Convexity
of the squared norm follows by subtracting
tau(1-tau)|Z_1-Z_0|_F^2. Apply it to I-P_U and I-P_barT, then use
|v+e|^2<=2|v|^2+2|e|^2. The exact conclusion is

    a_Y(p) <= 2[(1-tau)a_U(p)+tau a_T(p)]
                         +8 B^-2 s_p^2+2 s_p^4.          (SEED)

This estimate uses actual Wilson curvatures at both endpoints, not dh.
It holds at finite background without a Taylor or BCH hypothesis. Off
the transition shell the seed is an exact endpoint up to gauge, so its
replacement cost there is zero; (SEED) is used only on that shell.
Writing R_D(Y) by the same formula as R_D in (GLUE-E), but without
asserting admissibility of Y, nonnegativity of the subtracted endpoint
actions consequently gives the complete seed bound

    R_D(Y) <= 2 sum_(S_0) [a_U+a_T]
                    +sum_(S_0) [8 B^-2 s_p^2+2 s_p^4].

**gap — the exact first missing inequality.** Let S_0 contain every
plaquette touched by the transition cutoff, enlarged to include its bond
stencils. The direct transfer now needs a choice of (ALIGN) for which

    sum_(p in S_0) [8 B^-2 s_p(h)^2+2 s_p(h)^4]
       <= C_rel(L) sum_p (K*1_(S_r(D)))(p)
                                    [a_U(p)+a_T(p)].     (NL-pay)

Quantifiers: every n>=1, volume, allowed V, its specified class minimizer U
and iterated trial T, and required D. Here g fixes the top centres, q is
factored exactly as above, r is in top units, and K is a symmetric
nonnegative probability kernel with depth/volume-uniform exponential
moment at the pre-L rate. C_rel is depth/volume independent, with its
L dependence to be retained in any later absorption. I have not derived
(NL-pay), even before the nonlinear parent correction. This is one
missing estimate for this construction, not a claim that every possible
proof of (GLUE-E) must establish it.

**discharged — why the flat estimate does not pay that term.** Its
energy-carrying representative satisfies only
||H_0||_(2,X)^2<=2^124 B^2 ||dH||_(2,X+6B)^2. Even granting the
corresponding second-moment estimate for a nonlinear h would not finish
(NL-pay). Indeed, if |h_b|<=rho, then

    sum_(S_0) s_p^2 <=24 sum_X |h_b|^2,
    sum_(S_0) s_p^4 <=16 rho^2 sum_(S_0) s_p^2.

The first bound uses four sides and six incidences; the second uses
s_p<=4rho. Paying the quartic term by these bounds would introduce a
coefficient proportional to rho^2 B^2=rho^2 L^(2n). Shrinking a positive
rho after L, independently of n, cannot make that coefficient uniform
in n. This diagnoses the loss of this particular estimate, not a lower
bound on the best possible seam cost. Moreover the nonlinear analogue
of the second-moment estimate itself has not been proved here: dH is
not the difference of nonlinear curvatures. The exact unpaid quantity
is the left side of (NL-pay), with actual endpoint actions on its right.

## 3. Mandatory diagnostics of that payment

**discharged — exact-gradient test.** Put X=i sigma_1=[[0,i],[i,0]],
Y=i sigma_2=[[0,1],[-1,0]], Z=i sigma_3=diag(i,-i). Multiplying these
matrices gives XY=-Z, YZ=-X, ZX=-Y, with reversed
products of opposite sign, and X^2=Y^2=Z^2=-I. On a square give the
site potential the values 0,tX,t(X+Y),tY in cyclic order. Its oriented
increments are tX,tY,-tX,-tY, so dh=0. Writing c=cos t, s=sin t,
multiply (c+sX)(c+sY)(c-sX)(c-sY) to get

    C(t)=(1-2s^4)I+2cs^3 X-2cs^3 Y-2c^2s^2 Z.

For example conjugating Y by c+sX first gives
(c^2-s^2)Y-2csZ, which yields all four displayed coefficients after
the last multiplication. Hence

    a(C(t))=2 sin^4(t)>0        for 0<|t|<pi.             (GRAD)

An estimate of the nonlinear action by |dh|^2 alone is false even on
this square. In (SEED)/(NL-pay), this action belongs to a_T when that
field is an endpoint, and the relative fourth-power term is explicitly
retained. An exact site gauge is different: its plaquette is conjugated
and has unchanged action, as proved above. No commutator action is
assigned to the exact root gauge q_chi. This local diagnostic is not
claimed to be a counterexample using the specified minimizing chain.

**discharged — nonzero background and its flux power.** Put
P_U=exp(fZ), 0<f<=T_class<pi/2, with T_class the small class flux threshold
(not the trial field T). The same transported increments give
P(t)=C(t)exp(fZ). Taking the scalar part of the preceding product yields

    a(P(t))=1-cos f+2 sin^4(t) cos f
                         -2 cos^2(t) sin^2(t) sin f.     (BG)

Changing f to -f changes the last sign, so this interaction has no
uniform favorable sign. More directly, at a constant seam value 1/2
its deviation from the endpoint chord is

    J_f(t)=a(P(t/2))-[a(P(0))+a(P(t))]/2,
    lim_(t->0) J_f(t)/t^2 = (sin f)/2 >0.

To check the limit without a recalled expansion, integrate
|cos u|<=1 to get |sin u|<=|u|, use
1-cos u=2 sin^2(u/2)<=u^2/2, and integrate again to get
|sin u-u|<=|u|^3/6. Substitution in (BG) gives the limit.
The same inequalities give sin f/f ->1. Thus the background adds a
term of order f|h|^2, linear in flux, even with zero sum of transported
increments; it is not an f^2|h|^2 error. This calculation includes
f=T_class. On this plaquette the endpoint at small t still has flux
at most f: its scalar part increases when tan^2 t<=tan f. This local
check does not assert admissibility of a whole class chain constructed
by prescribing just these four links.

**discharged — where that term is charged, conditional application.**
For the possibly positive background term, the elementary inequality
2ab<=a^2+b^2 gives

    2 |sin f| cos^2(t) sin^2(t)
       <= sin^2 f+cos^4(t) sin^4(t)
       <= 2 a(P_U)+sin^4(t).

Thus full background action and the same fourth-power budget pay it;
no extra small factor of f is assumed. Estimate (SEED) implements this
principle for arbitrary plaquettes without expanding in f. At threshold
the background energy is retained on its right. The remaining payment
is still (NL-pay), not an assertion that small background flux alone
absorbs an unestimated relative connection.

**discharged — where frozen data sit, and where they do not.** The
terminal-parent class problem used in `parts/hard-core--excess.md`,
Section 3, and `relative-density-bound.md`, item (o), fixes V and takes
the infimum over class chains. It does not separately prescribe fine
links: intermediate images are the images of the candidate. It is not
the data-dependent problem a_d(V) in `paid-inputs-frozen-energy.md`.
No bound in this note replaces a_U+a_T by coarse curvature.

For a version with prescribed fine bonds F, an admissible seed would
have to keep those actual bonds: U_b=T_b=Y_b=d_b on F. Endpoint gauges
and q_chi must preserve these equalities, not just plaquette actions.
A plaquette all of whose links are fixed then has
a_Y=a_U=a_T, so its summand in R_D is exactly zero whether inside or
outside D. Mixed plaquettes remain in the cost and may not be dropped.
This is cancellation of identical data, not a coarse-energy estimate.
The frozen-energy note's field with parent 1 and positive locked action
therefore cannot be charged to curvature of parent 1. Its unconstrained
trial lift of 1 would not be an admissible trial for that frozen-data
problem. Neither (ALIGN) with these additional fixed-link restrictions
nor (NL-pay) for that problem is claimed here. The unrestricted flat
centre gauge cannot supply it.

## 4. Stop and verification boundary

**gap — no nonlinear constants or admissibility claim.** A proof of
(NL-pay) would bound this seed's shell action. It would not yet prove
(GLUE-E): Y need not have parent V, and its intermediate images have
not been shown to remain class. I stop before attempting that correction,
as requested. In particular K=delta_0 and M_*=1 from the flat correction
have not been assigned to a nonlinear correction with possible tails.
No numerical or finite-dimensional existence argument supplies the
missing uniform estimate.

**implication — the unchanged final rate obligation.** If a completed
construction eventually has A_s(L), r(L), M_*(L), it must still satisfy

    2 A_s(L) M_*(L) sinh(nu r(L)) < 1                    (RATE-exact)

with nu fixed before L. The flat certificate in Section 1 does not
certify this inequality for the missing nonlinear construction. A
coefficient depending on L^(2n) is inadmissible even if nu is very small.
No rate has been silently reduced and no conclusion is drawn from
failure of a sufficient upper-bound calculation.

**discharged — read/write boundary.** Read GOAL in full; FINISH,
including the independence and rules sections; all of `seam-quadratic.md`,
`excess-shell-end.md`, and `paid-inputs-frozen-energy.md`. Relevant
additional reads were `excess-seam.md` Sections 1–2 (and the beginning
of its diagnostic), `excess-localized-competitor-stop.md` Sections 1–2,
the excess part's trial/class statements, the mapped Text 3.1 and
5.1–5.2, item (o) of `relative-density-bound.md`, and the setting and
tangent statements at the beginning of `fibre-propagator.md`. The
regularity passages (R1)–(R3), the opening portions of `analytic-lift.md`
and `block-poincare-energy-package.md`, and map locators were also
inspected; their nonlinear estimates are not premises of (SEED).
The superseded convention note was inspected only to identify its obsolete
thresholds; they were not used. Locator output, source claims of
numerical tests, and source proofs outside the reconstructed flat and
matrix arguments above do not discharge premises. No forbidden-side
file, gate, external proof account, or historical numerical log was
opened. The workflow, absent from the sparse working tree, was read
with `git show HEAD:docs/ai_methodology/SCIENCE_WORKFLOW.md`. The
physics-claim-reviewer skill was used only for this bounded proof check.
Only this file was written; no scripts, numeric job, subagent, audit,
commit, push, or post were used.

**discharged — source identities.** The three principal input blob IDs
at inspection were, respectively,
`ad23a6108554209cd6def7e5eb6902541bfb2f2e` (quadratic),
`8eaa8cfde57623ba73cdca44d3c0f632b37d8f7d` (shell end), and
`a1ff3b8fe1199ef333ae4154ffae855cdb9b4ff3` (frozen energy).
File/status checks are bookkeeping, not mathematical validation.
At the final scope check HEAD and these three input hashes were unchanged,
the tracked diff was empty, and status listed only this new file. The
no-index whitespace check emitted no diagnostics (its exit status 1
reports the new file's difference from `/dev/null`).

**gap — verdict: undecided at (NL-pay), the depth-uniform nonlinear
relative-gauge budget containing the fourth-power term in (SEED).**
Neither its nonlinear second-moment part nor its fourth-moment part has
been derived for the specified endpoints. The flat proof was not refuted.
Its nonlinear transfer, admissible corrected class
chain, and (RATE-exact) constants have not been derived. No claim of
failure of Yang–Mills or of impossibility of another construction follows.
