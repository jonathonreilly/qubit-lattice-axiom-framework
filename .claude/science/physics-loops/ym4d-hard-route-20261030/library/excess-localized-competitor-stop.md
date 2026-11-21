# Localized replacement: the seam estimate still missing

Pinned source: 25a86977f538eb6bb104f097c435b44fd42138b7, 2026-11-01.
OpenAI/gpt-6-astra/max, mac-mini-codex; mapped-side author work, not an
independent check or audit. No numerical computation. Recovery checkpoint:
../parts/hard-core--excess.md, Summary, Section 3.3, Section 6 and Obligations.
The proofs of Lemma EX and EX-loc are inputs and are unchanged.

Constants may depend on dimension four, SU(2), the fixed blocking profiles,
and the indicated radii/rate margins. A constant written C(L) may also depend
on the fixed odd L. Required consumer constants are free of x, depth, volume,
position and weight normalization, uniformly below the chosen flux threshold.
Finite-dimensional constants are explicitly distinguished below.

## 1. What a cutoff does to the parents

**Discharged algebraic lemma (linear model only).** At the trivial field,
let Q_n = D M_n(1), and let T_n be the derivative at 1 of the specified exact
trial lift. Differentiating M_n T = identity gives Q_n T_n = identity.
In the Maxwell problem let A_* minimize ||d A||^2 subject to Q_n A = v,
let A_t = T_n v, and put H = A_t - A_*. Thus Q_n H = 0. A residual gauge
may be fixed; the following identities do not depend on which minimizer
representative is used.

Choose a bond cutoff chi equal to 1 in a core and 0 beyond a shell, and
write chi_c for any corresponding scalar cutoff on coarse bonds. The seed
A_* + chi H has parent defect

    m_chi = Q_n(chi H) = (Q_n chi - chi_c Q_n)H.             (SEAM-lin)

In particular the defect is linear in H, even though the endpoints have
identical parents. The exact linear-fibre competitor is

    A_chi = A_* + D_chi,
    D_chi = chi H - T_n m_chi,       Q_n D_chi = 0.          (GLUE-lin)

This follows by applying Q_n and using Q_n T_n = identity. At flat fields
the trial derivative has finite support: its nonlinear parent correction
has zero first derivative, and its tensor/contour construction is local.
The support radii of the composite Q_n and T_n in top units are bounded
by a fixed one-step radius times sum_(j=0)^(n-1) L^-j <= L/(L-1).
Consequently m_chi is supported near the transition shell, and T_n m_chi
in a fixed enlargement of it. A_chi equals A_t sufficiently far inside
and A_* sufficiently far outside. This is a support statement, not a
depth-uniform norm estimate for the true composite contour operator.
It preserves the terminal linear parent; intermediate parents are those
of the new chain, not separately prescribed old intermediate fields.

Stationarity of A_* against D_chi gives the exact identity

    ||d A_chi||^2 - ||d A_*||^2 = ||d D_chi||^2 >= 0.        (MIN-lin)

Include every affected plaquette stencil in the shell S. On a core D where
A_chi = A_t and outside D union S where A_chi = A_*, this reads

    E_*(D) - E_t(D)
       = E_chi(S) - E_*(S) - ||d D_chi||^2
       <= E_chi(S) - E_*(S).                              (BUDGET-lin)

Thus even the exact admissible linear competitor leaves an *upper* bound
on the shell's change of energy to prove. Minimality does not pay it.
All identities hold at every fixed finite n and volume; no bound for
||T_n|| in the consumer's Eps norm is asserted.

**Discharged diagnostic for nonlinear gluing.** If an aligned relative
logarithm Z between two endpoints exists in a finite chart, a nonlinear
seed exp(eta chi Z)U has, to first order, the same defect:
Q_U(chi Z) - chi_c Q_U Z, plus the Taylor remainders. Equality of the
endpoint parents makes Q_U Z quadratic in Z; it does not make the
commutator quadratic. On a fixed finite chart the remainder is bounded
by C_fin ||Z||^2, with C_fin allowed to depend on depth and volume.
For a simple row Q(h_1,h_2)=(h_1+h_2)/2, H=(t,-t), chi=(1,0),
QH=0 but Q(chi H)=t/2. This example illustrates the commutator, not a
Yang--Mills counterexample.

## 2. What the finite-range inverse actually supplies at a seam

**Implication, proved (conditional correction lemma).** Suppose a specified
response map Psi_chi(y), continuously differentiable on a neighborhood of
the closed sup-norm ball of radius b in parent corrections, has
Psi_chi(0)=m_chi and, throughout that ball,

    D Psi_chi(y) = I + E_y,
    sup_c sum_c' ||(E_y)_(c,c')|| <= q < 1,
    (E_y)_(c,c') = 0 for d(c,c') > R,
    ||m_chi||_infinity <= (1-q)b.                           (GLUE-domain)

The map y -> y - Psi_chi(y) preserves the ball and contracts with constant
q, so it has a unique fixed point there. The mean-value formula gives
y = -(I+E_bar)^-1 m_chi, with the same range and row bound. In its Neumann
series the term of order j cannot travel farther than jR and has row sum
at most q^j. Therefore, for any fixed initial support enlargement a,

    |y(c)| <= (1-q)^-1 sum_c' k_q(c-c') |m_chi(c')|,
    k_q(z) = q^floor((d(z,0)-a)_+/R).                       (GLUE-INV)

The kernel includes the finite bond-type multiplicity. Let M_q=sum k_q,
K_q=k_q/M_q. Jensen and transposition of this symmetric kernel give

    sum_c W(c)|y(c)|^2
       <= M_q^2/(1-q)^2 sum_c (K_q*W)(c)|m_chi(c)|^2.       (GLUE-W)

For q<=q_*<1 and q_* exp(nu R)<1, the polynomial shell count in four
dimensions bounds M_q and the moment M_nu(K_q)=sum K_q exp(nu d)
uniformly in volume. For scalar log-Lipschitz W of rate nu,
K_q*W<=M_nu(K_q)W. Periodizing the cover kernel preserves these bounds.
Here constants depend on a,R,q_* and the positive rate margin, not on
x,L,n or volume if those parameters are fixed independently of them.
They are not a bound for constructing Psi_chi. At q=0 use 0^0=1.

This is the q^floor inverse used correctly on a seam source. Its source
is |m_chi|^2 in GLUE-W, not the squared parent flux from the trial's
special quadratic residual. For m_chi=O(t), the leading cost is O(t^2).
It need not have an additional flux factor. For q>0 the correction has
tails; exact agreement with the two endpoints off a finite shell is
not promised. Their energy cost must be included in a gluing estimate.

**Gap in its application.** The proved (FR) in
excess-finite-range-repair.md is for Psi_V(y)=log(M B(exp(y)V)V^-1).
It does not assert GLUE-domain for a mixture of the true lift and B, or
for the true composite M_n on such a mixture. Replacing the seed by
B(exp(y)V) everywhere would discard the proposed localization. No
parent-fixed nonlinear mixture, with admissible descendants and the
required uniform response bounds, has been established here. Even if
GLUE-domain were supplied, GLUE-W controls the correction by the seam
defect; the missing shell estimate below must still control that defect
and the change of action. A tail estimate alone is not that estimate.

## 3. The exact shell inequality sufficient for LOC-MIN

**Implication (scalar localization lemma).** This paragraph states explicit
sufficient premises; it does not assert them for the chain. Let y=v-b
be a signed top-cell excess density, v>=0 its variance density, v_t>=0
the trial density, and c>=0 an error density. Suppose |b|<=C_b c.
For sets D write D^(+r) for the r-neighborhood, D^(-r) for the points
whose entire r-ball lies in D, and S_r(D)=D^(+r) minus D^(-r).
Let K be a symmetric nonnegative probability kernel, such as the repaired
K_q with all fixed enlargements included. The precise sufficient shell
budget is, for every relevant superlevel set D,

    y(1_D) <= C_0 v_t(1_(D^(+r)))
             + alpha v(K*1_(S_r(D)))
             + C_1 c(K*1_(D^(+r))).                        (SHELL)

This inequality must include the energy of the corrected competitor's
tails and the conversion from Wilson action to squared flux, since
global minimality is for the action. Global class-minimality itself
retains item (o) if that identification is used. In the application,
identifying v with Yhat and bounding b by the cubic density retain
CJ/CR; they are not checked by this localization lemma.

Here is the exact conversion of SHELL to a slow-weight budget. For a
positive scalar w of log-Lipschitz rate nu set D_t={B:w(B)>t}. On a
finite torus, integrating their indicators over t gives w, while

    integral 1_(D_t^(+r)) dt = w_r^+ := max_(d<=r) w,
    integral 1_(D_t^(-r)) dt = w_r^- := min_(d<=r) w,
    0 <= w_r^+-w_r^- <= 2 sinh(nu r) w.

Finite sums, integration and convolution commute. Thus SHELL implies

    Y(w) <= C_0 exp(nu r) v_t(w) + epsilon v(w)
                     + C_1 M_nu(K) exp(nu r)c(w),
    epsilon = 2 alpha M_nu(K) sinh(nu r).                  (LOC-rate)

This is LOC-MIN with a displayed absorption test. If epsilon<1, use
v(w)<=Y(w)+C_b c(w) to obtain

    Y(w) <= [C_0 exp(nu r)/(1-epsilon)] v_t(w)
           + [C_1 M_nu(K) exp(nu r)+epsilon C_b]
                          /(1-epsilon) c(w).              (LOC-upper)

All constants inherit precisely those of SHELL and its error bound.
In particular, a large C(L) in alpha cannot silently be absorbed at
the consumer's fixed spatial rate: LOC-rate has to be checked.
At nu=0 the shell contribution integrates to zero, as it should.

**Discharged weight bookkeeping; implication for its use.** D2 of
repair-gate-105283f2c.md forbids assigning a shrinking fine-edge rate
to the down-averaged orientation weights. Apply the preceding argument
to a scalar interpolated profile only. If W^q and w obey
c_w^-1 w<=W^q<=c_w w, transfer *positive* v and c estimates once;
for example v(W)<=c_w v(w)<=c_w^2 C v_t(W)+c_w^2 C' c(W).
Recover signed Y from its separately controlled b, rather than
comparing two signed excesses by positivity. This retains persistent
jumps without a factor at every depth. With sampled energies use the
explicit O(nu_l) E_l conversion in the earlier continuation. Nothing
in this argument removes that energy error.

**Gap, LOC-MIN stop.** No SHELL estimate with the indicated uniform
constants and epsilon<1, or another admissible comparison implying
LOC-MIN, has been proved for the nonlinear class chain. EX-loc states
e(W)>=c_1 I^grad(W^-)-C(L)cub(W^+): it bounds a coarse gradient from
above by excess plus errors. It does not bound from above the cost
of the seam correction, its relative link field, or the corrected
competitor's excess. In particular it cannot be applied as an upper
bound for E_chi(S)-E_*(S) in BUDGET-lin. A relative-field/shell estimate
is the extra assertion needed, even after admissibility is established.

## 4. The two requested attacks

**Discharged two-site check.** In the earlier note's fibre
Q(u_A,u_B)=u_A-u_B=a, take T a=(a,0),
u_*=(a/2,-a/2), H=(a/2,a/2), and chi=(0,1).
GLUE-lin gives Q(chi H)=-a/2 and
(I-TQ)chi H=(a/2,a/2)=H. Replacing B also changes A.
The correction reaches the other site, a distance D away; its support
radius is not uniform in D. The energy ratio for the slow weight is
(5+exp(nu D))/4, as in the earlier note. Thus this model defeats
minimality alone, but not a *uniformly local* SHELL premise. It shows
exactly which locality hypothesis a shell proof must supply.

**Discharged Maxwell far-tail check, using the earlier algebraic field.**
In excess-weighted-fibre-stop.md the minimizing curvature is
F_*=C^*(CC^*)^-1 b with a nonzero value in every distant slab,
whereas the commuting trial has compactly supported curvature.
Choose a distant core with trial curvature zero and F_* nonzero.
GLUE-lin is an admissible linear replacement. BUDGET-lin now gives

    E_chi(S)-E_*(S) = E_*(D)+||d D_chi||^2 >= E_*(D)>0.

Scaling the data by t scales this entire quadratic identity by t^2.
Thus a proposed shell cost made only of cubic errors, or claiming
the minimizer's far response has the trial's flux-vanishing tail,
fails already in this linear problem. On a fixed lattice, any
differentiable admissible nonlinear gluing with this linearization
would retain the quadratic shell cost. That statement is conditional
on the gluing; its existence is not supplied by the earlier analytic
minimizer branch. The test does not rule out SHELL with its quadratic
variance term.

The slow weights do not reproduce the arbitrary-weight falsifier:
its linear inverse has tail rho_L^d, with rho_L<2-sqrt(3);
conjugation by sqrt(w) costs exp(nu d/2), leaving a summable kernel
when nu< -2 log(rho_L). This is the earlier slab calculation, not a
uniform nonlinear theorem. Even with the fast q=O(t) *constraint*
correction, the seam source already contains the minimizer's linear
tail. It is therefore incorrect to remove that tail from the source
or to infer an unrestricted TOP bound from GLUE-INV.

**Step 1 result: gap.** A localized admissible competitor is constructed
here in the Maxwell problem only. The nonlinear route stops at
GLUE-domain/admissibility and SHELL with LOC-rate<1. These are named
missing estimates, not a counterexample to LOC-MIN or TOP-slow.
The requested fallback to END is considered next; no later dependent
transport or remainder estimate has been promoted.

## 5. END fallback: the finite gauge argument is not uniform

**Discharged anchored-gauge diagnostic.** The finite TRUE-CH construction
in excess-consumer-weight-continuation.md fixes fine gauge parameters
to zero at every top centre and inverts their Dirichlet gauge matrix.
At U=1 take top spacing 1, fine spacing eta=L^-n, L odd >=3, n>=1,
and a periodic lattice with N top sites. Use density-normalized norms,
||omega||_2^2=eta^4 sum_x |omega(x)|^2, and
d_eta omega(b)=(omega(b_+)-omega(b_-))/eta.
Let P_0 project onto parameters zero at top centres and set

    L_eta = P_0 d_eta^* d_eta P_0, restricted to im P_0.

For a fixed nonzero X in su(2), take omega=0 at all top centres and
omega=X at every other site. This is an allowed test vector. Each
centre has eight incident unoriented bonds, with no shared such bond
between centres, since L^n>=3. All other bond differences vanish.
There are N eta^-4 fine sites. Direct counting therefore gives

    ||d_eta omega||_2^2 = 8 N eta^2 |X|^2,
    ||omega||_2^2 = N(1-eta^4)|X|^2,
    lambda_min(L_eta) <= 8 eta^2/(1-eta^4),
    ||L_eta^-1||_(2->2) >= (1-eta^4)/(8 eta^2).             (ANCHOR)

The Rayleigh inequality follows by diagonalizing this finite positive
matrix, or by expressing the quotient as a convex combination of its
eigenvalues. Positivity follows because a zero-gradient parameter is
constant on the connected lattice and zero at a centre. This proves
ANCHOR without a computation run. The number 8 is the dimension-four
bond count, independent of x,L,n and N; eta displays the unavoidable
depth dependence of this particular inverse norm. The conclusion
already holds at zero flux and in any fixed physical volume.

This does **not** disprove END. A gauge parameter norm is not the
norm of the gauge action on links; a projected derivative of an
ill-conditioned inverse can be bounded. Another slice can also have
better estimates. Theorem F uses block averages and a class quotient,
not this point-anchored Dirichlet norm. ANCHOR rules out silently
making the finite TRUE-CH gauge inverse uniformly bounded in L^2,
or treating its finite norm equivalences as uniform estimates.
It does not prove that every true-fibre chart radius shrinks.

**Gap after examining the alternatives.** The bounded portions of
fibre-propagator.md used here are its setting, Theorem F and hostile
point (6'); analytic-lift.md supplies the statements and construction
of AN1--AN3; mapped (R1)--(R3) distinguish the one-shot reference from
the specified exact tensor trial. These retain their own premises.
F is a tangent/class inverse. AN3 varies the parent of a minimizing
branch; setting its parent increment to zero returns that branch and
does not reach the nonstationary trial. R2's comparison is with its
one-shot reference, not a proved alignment with the specified trial.
Replacing point anchors by F's block-mean slice would still need a
controlled finite conversion back to the true parent-fixed fibre and
endpoint coverage. F's warning that an arbitrary Eps ball does not
supply R3's summable contour control prevents assuming its hypotheses
along an unconstructed interpolation.

The exact first missing endpoint assertion remains: for every allowed
parent V, true lift U, specified trial T(V), depth n and finite volume,
there are a gauge g and a genuine parent-fixed slice chart Z(h) with

    g|_top centres=1,    eta=L^-n,
    Z_tr=eta^-1 log((g . T(V)) U^-1),
    sup_B ||Z_tr||_Eps(B) <= r_ch(L),
    Z_tr=Z(h),    {t h: 0<=t<=1} in the chart domain,
    ||Z(h)||_(Eps,W) <= C_ch(L)||h||_(Eps,W).                (END)

Here r_ch(L)>0 and C_ch(L)<infinity must be uniform in x,n,volume,
position, sector and the allowed flux class, for the consumer weights.
The radius must be within the domain needed for the subsequent uniform
secant contraction. The earlier finite construction supplies none of
these uniformities; ANCHOR identifies a concrete loss in one proposed
way of obtaining them. No counterexample to END for these particular
endpoints is claimed.

**Gap, dependent inequalities not attempted past END.** With
S=A composed with the chart, A_U=D^2 S(0), J_h=D S(h), the next
requirements are still

    ||A_U^-1 integral_0^1 (D^2 S(t h)-D^2 S(0))h dt||_(Eps,W)
                      <= epsilon ||h||_(Eps,W), epsilon<=1/2,  (SEC-unif)
    ||A_U^-1 J_h||_(Eps,W)^2
       <= C_J(L) Yhat_tr(W^dagger)
                     + C_4(L) sum_B W^dagger(B) f_B^4.      (TRIAL-J)

J_h(v)=D a_U(Z(h))[D Z(h)v] includes the derivative of the fibre
correction. These constants need the same uniformities as END and a
controlled identification with F's class representatives. If all three
hold, the already proved algebra gives
C_H <= C_ch(L)^2 max(C_J(L),C_4(L))/(1-epsilon)^2.
That remains an implication, not an estimate established in this session.
HC-W and the level-free CJ/CR checks are not pursued across this stop.

## 6. Result and next precise test

| Statement | Label | Constant scope / limit |
|---|---|---|
| SEAM-lin, GLUE-lin, MIN-lin | discharged, author proof | Exact Maxwell identities; support radius uniform in depth, no Eps norm estimate |
| GLUE-INV/W | implication, proved | Given GLUE-domain; kernel constants depend on a,R,q_* and the rate margin; construction/domain still gap |
| SHELL implies LOC-MIN and LOC-upper | implication, proved | Given SHELL, cubic remainder bound and 2 alpha M_nu(K) sinh(nu r)<1; no application to the chain yet |
| Nonlinear LOC-MIN | gap | Admissibility, uniform gluing response and upper shell cost, including tails and action conversion |
| ANCHOR | discharged, author proof | Exact at U=1; inverse grows at least as eta^-2; independent of x and volume |
| END on the consumer class | gap, final stop | Uniform true-fibre endpoint alignment/chart not obtained |
| SEC-unif, TRIAL-J, HC-W | gap | Dependent work stopped |
| All-depth CJ/CR | unchecked | Carried statements, not rechecked or promoted |

Reopen LOC-MIN with an explicit nonlinear replacement and a proof of
SHELL (or an equally precise upper budget) meeting LOC-rate. Reopen the
fallback with END, in a gauge/norm whose bounds survive depth and whose
chart contains the specified trial. A tangent inverse, finite-dimensional
existence or a numerical finite-size test alone does not meet either
criterion. TOP-W is still open; COMP-ii-g and FALL retain their existing
TOP/cubic/energy hypotheses. No Yang--Mills counterexample, existence
theorem, new axiom or audit status follows from this note.
