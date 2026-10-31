# LIMIT — real bounds, common limits, OS axioms, and reconstruction

Author sprint, 2026-10-30. Controlling instruction: `briefs_q/LIMIT/AUTHOR.md`.
Only this file is changed. There is no new independent review, numerical
experiment, commit, audit decision, or axiom. The endpoint below is a
**conditional scalar reconstruction**, with both geometry routes worked
through. It is not an unconditional Yang–Mills existence theorem.

Each numbered step has exactly one status. A source-qualified status imports
only the quoted, previously reviewed implication, with its hypotheses. It
does not import an actual-model estimate from a conditional theorem. The
new arguments and their most likely failure points are identified separately.
The four gaps are not assumptions silently discharged later in the file.

The source snapshot has no Git metadata. Source identities and review scope
are recorded at the end; no new claim about historical Git landing is made.
In particular, `REVIEW_N5B.md` is HOLD for the stronger UV-only description:
this file uses its confirmed actual-law covariance argument, and supplies
no replacement review verdict for N5B.

Credit for the constructive RG organization belongs to Tadeusz Balaban and
Jonathan Dimock. The reconstruction problem and continuation strategy are
due to Osterwalder and Schrader; their [1975 primary paper](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf)
is attribution, not a replacement for the precise REC_LIB/REC_CONT contract.

## L01 — DRAFTED(high): freeze the observable and the assumed input

**Consumes:** the supplied real Wilson regulator and the brief's named
fixed-physical-scale real-derivative input, called `H_INDUCT^ref` here.
**Produces:** one domain and an explicit contract against which that input
can be checked. **Most likely failure point:** identifying an upstream
source derivative with the derivative of this same normalized bare law.

Fix SU(N), N>=2, odd L>=3, physical reference length ell_ref=1, and
`a=L^(-K)`. Use the clover observable of ROTDEF §2.2 and WITNESS E-ALG,

    e_a(x)=(4a^4)^(-1) sum_(mu!=nu) sum_(p in clover_mu,nu(x))
                              [1-Re tr(U_p)/N],
    X_a(x)=e_a(x)-mu_(a,R)(e_a(x)),       Z_e(a)=1.

The number of summands is a fixed finite integer; `0<=1-Re tr(U_p)/N<=2`.
Thus fix a named `C_X<infinity` satisfying `|X_a(x)|<=C_X a^(-4)` for
every regulator. No numerical value of C_X is needed. On a sphere the
observable, chart volume weights, centering and profile must be separately
matched to this prescription (L13). A different normalization requires a
new crude-power bound and a new witness comparison; it is not a free choice.

At zero source the full positive normalized soft chain has bare marginal
mu. Let V denote its reference-scale coarse field and nu its actual
marginal. For a finite list of distinct site sources define

    Psi(t,V)=log E[exp(sum_i t_i X_a(x_i)) | V],
    J_B(V)=partial_B Psi(0,V),        empty != B subset {1,...,n}.

At each finite cutoff the variables are bounded, so these real derivatives
exist and are the conditional joint cumulants. In particular
`J_{ {i} }=E[X_a(x_i)|V]` need not vanish. Keep all RG kernels and
their normalizers fixed during differentiation. If INDUCT uses the source
`sum_x a^4 eta(x)e_a(x)`, converting its coordinate derivatives to J_B
costs the corresponding `a^(-4|B|)`; one must instead use its correctly
scaled insertion directions. Removing contact terms from a logarithm is
permitted here only when their mixed derivative vanishes at these distinct
supports. No new positive probability law is inferred from that subtraction.

`H_INDUCT^ref` is assumed, as requested, rather than proved here. It names
the actual fixed-scale real derivative bounds, not a complex-source
extension, pressure comparison, sphere estimate, or lower covariance bound.
There is no `INDUCT.md` in this snapshot; `INDUCT55.md` contains targets
only. Consequently its unstated all-order constants cannot be reported as
computed outputs. L02 states the exact additional export needed by LIMIT.

Use precisely the scalar restricted domain of OSLEAF55:

    E_n = {F in Schwartz(R^(4n)): every derivative of F vanishes
                                  whenever x_i=x_j for some i!=j},
    |F|_k=max_(|alpha|<=k) sup_X (1+|X|^2)^(k/2)|partial^alpha F(X)|,
    A = direct_sum_(n>=0) E_n,                  S_0=1,
    S_n^(a,R)(F)=a^(4n) sum_(x_1,...,x_n) F(X) E product_i X_a(x_i).

Initially F is compactly supported in an embedded patch. The positive
space consists of finite sequences with F_n zero off
`0<t_1<...<t_n`. Star reverses arguments and conjugates once; theta
reflects time. Multiplication is allowed only when the resulting tensor
test is flat. In particular a general `e(f)^2` is not a test in A.
Here OS0 means restricted distribution regularity, OS1 Euclidean
invariance, OS2 the ordered-half reflection form, and OS3 permutation
symmetry, with reality stated separately. No ordinary moment measure or
contact extension is asserted.

## L02 — GAP: match fixed-scale real derivatives to the complete export

**Consumes:** H_INDUCT^ref. **Needed output:** either REALONLY R8 or R9
with all their quantifiers, or the following sufficient real-jet export.
It must hold with ONE `A>=1, p>=0, eta>=0, q>=0, c_*>0`, independent of
cutoff, volume, insertion number, placements and moment order:

    delta=min_(i<j)|x_i-x_j| >= c_* a,
    w(r)=min(r,1)^(-4) [log(2+1/min(r,1))]^q,
    ||J_B||_(L^r(nu)) <= A^b (b!)^p (1+r)^(eta b) W_B,
       b=|B|>=1,  every integer r>=1,                  (IND-J)
    W_B=product_(i in B) w(min_(j in B, j!=i)|x_i-x_j|)  if b>=2,
    W_{ {i} }=1.

All expectations are under the same actual marginal, including large-field
histories. For products of several J_B the estimates hold together under
that marginal. If a derivative producer instead gives essential suprema,
eta=0 is sufficient. A direct R9 export can replace IND-J and avoid this
particular sufficient L^r condition. For a smeared producer the alternative
is OSLEAF55 §13's corrected SP_lambda, with singleton-inclusive bounds,
scaled derivative norms and the window `c_SP a<=lambda<=1`; an unquantified
bound at each fixed positive lambda is insufficient.

The missing comparison is substantive: fixed-scale or fixed-n finiteness
does not bound its growth as n,r increase or lambda decreases with a.
Conditional higher cumulants alone also do not suffice. For a symmetric
sign V and `X_a(x)=a^(-4)V`, all conditional cumulants of order >=2
vanish given V, but the separated unconditional two-point value is
`a^(-8)`. This example tests the inference, not the Wilson model.
Likewise, the one Peierls smallness condition in SRCCD55 does not certify
every required outer moment with this n-growth. Finally the fine clover
same-test variance divergence in SRCCD55 Lemma V precludes replacing the
separated contract by a cutoff-uniform raw positive MGF on its stated
torus trajectory.

To close this step, INDUCT must export the source normalization, singleton
estimates, actual-law outer controls, separation powers and factorial
constants explicitly. The rest of this file continues conditional on
IND-J or R9; it does not upgrade H_INDUCT^ref by notation.

## L03 — DRAFTED(high): real jets give complete outer cumulants and moments

**Consumes:** IND-J and the finite normalized law of L01.
**Produces:** the following generalized R9 and then R8, with all-n
constants. **Most likely failure point:** using an L^r bound from a
different coarse marginal or only on a selected small-field event.

For a partition pi of n labels into r blocks, the cumulant formula and
Holder give

    |kappa_nu(J_B:B in pi)|
       <= [sum_(rho partition of r) (|rho|-1)!] product_(B in pi)||J_B||_r.

An ordered partition into k nonempty blocks is counted by compositions
of r and has at most r! choices per composition. Therefore
`sum_rho |rho|! <= 2^(r-1) r!`, which also bounds the bracket above.
Subset nearest-neighbor distances are no smaller than those of the full
configuration, and w is nonincreasing and at least one. Put

    A_* = 2 A (2 exp(1))^eta.

Using `r<=n`, `(1+r)^(eta n)<= (2exp(1))^(eta n)(n!)^eta`
(from `n^n<=exp(n)n!`) proves

    |kappa_nu(J_B:B in pi)|
      <= A_*^n r! (n!)^eta product_(B in pi)(|B|!)^p
                                        product_i w(delta_i).       (L-R9)

The extra `(n!)^eta` is displayed; this is literal R9 only when eta=0.
Total cumulance follows by taking the finite coefficient of
`t_1...t_n` in `log E_V exp(Psi(t,V))`, working in the nilpotent
ring `t_i^2=0`. No complex log estimate is used. Since
`product_B |B|!<=n!` and `sum_pi |pi|!<=2^(n-1)n!`, it gives

    |kappa_mu(X_1,...,X_n)|
       <= (2A_*)^n (n!)^(p+eta+1) product_i w(delta_i).

Expand each moment into products of unconditional cumulants. Singleton
unconditional cumulants are zero by centering (a bounded singleton
would also fit). For every partition the factorial products are bounded
by n! to the same power, the subset weights by the full weights, and
there are at most n! partitions. Consequently R8 holds with

    A_0=2A_*,       b_0=p+eta+2,                       (MOM)
    |E product_i X_a(x_i)|<=A_0^n(n!)^b_0 product_i w(delta_i).

This deliberately generous bound retains exactly the factorial form
needed downstream. It controls separated signed moments, not absolute
moments of coincident smears or extensive tilted products.

## L04 — PROVEN(REALONLY.md): the direct R9 interface

**Consumes:** REALONLY §4 R9, with its own constants A,p,q,c_*:

    |kappa_outer(kappa_cond(B):B in pi)|
      <=A^n r! product_(B in pi)(|B|!)^p product_i w(delta_i).

**Exact statement used:**

> This includes singleton conditional means and all required outer/LF
> products. Total cumulance, product_B |B|!<=n!, and
> sum_pi |pi|!<=2^(n-1)n! give unconditional cumulant exponent p+1.

And:

> Moment expansion has at most n! partitions, giving R8 with b_0=p+2.

**Produces:** R8 with `A_0=2A` and `b_0=p+2` as a sufficient choice
from the displayed combinatorics. Its reviewed scope is the implication
in REVIEW_REALONLY §4, not verification of R9 for Yang–Mills. This is
an alternative to L03, not a further loss of factorial power. Set
`p_eff=p` on this branch and `p_eff=p+eta` on L03's branch, so both
give `b_0=p_eff+2`.

## L05 — PROVEN(REC_LIB.md): separated moments imply E0-prime

**Consumes:** R8/MOM, the centered crude envelope of L01, and the stated
embedded lattice sum. **Exact statement used (REC_LIB §16):**

> Then on every compact admissible flat test
>
>     |S_n^a(F)|≤C^n(n!)^b_0 |F|_(10n+1),                (16.2)
>
> with a single C. Any common infinite-volume/cutoff limit continuous on
> flat tests satisfies E0′ with s=11, β=b_0+1 and α=e^C (enlarged for
> n=0,1 if needed). In particular b_0=p+2 gives β=p+3.

**Produces:** uniform continuity on compact flat tests and, after L06–L07,

    |S_n(F)| <= alpha (n!)^beta |F|_(s n),
    s=11,     beta=p_eff+3,     alpha=exp(C),       S_1=0.       (E0')

C>=1 is a named constant, independent of n,a,R, satisfying the displayed
(16.2), not a guessed numerical value. The proof supplies finite
majorants from

    Z_* >= sup_(0<a<=1) a^4 sum_x (1+|x|^2)^(-5/2),
    Z_* = 3^(5/2) integral_(R^4)(1+|y|^2)^(-5/2)dy  is sufficient,
    C_q = sup_(0<r<=1) r [log(2+1/r)]^q < infinity.

For clarity, the mechanism and the order count are retained. At a closest
coincidence plane, flat Taylor expansion with M derivatives yields

    |F(X)| <= (2delta)^M/M! * 2^(5n/2) |F|_(M+5n)
                                 product_i(1+|x_i|^2)^(-5/2).

For `c_*a<=delta<1`, choose M=5n and use `product_i w(delta_i)
<=C_q^n delta^(-5n)`. For `0<delta<c_*a<=1`, choose M=4n+1;
`a^(-4n)delta^(4n+1)<=c_*^(4n+1)a`. Exact coincidences contribute
zero. For delta>=1 use the integrable weight; when c_*a>1 the spacing
is bounded below and the crude envelope suffices. Every remaining
constant is exponential in n and can be absorbed in the same C.
Finally `10n+1<=11n` and `C^n<=exp(C)n!` give E0'.

This is the corrected reviewed REC_LIB/REC_CONT consumer scope, also
checked in REVIEW_REC_CONSUMER_ALIGNMENT_ASTRA, rather than SRCCD55
Proposition E's unqualified inference about outer cumulants. For a different
crude power `|X_a|<=C_X a^(-q_X)`, its permitted order is
`s=max(11,ceil(q_X)+6)`; s=11 is not exported to arbitrary fields.

## L06 — DRAFTED(high): one determining family and continuous extension

**Consumes:** the uniform bound of L05 on admissible compact tests.
**Produces:** a common convergence topology covering all moments, motion
tests, RP forms and witness tests. **Most likely failure point:** forgetting
an observable/motion Cartesian pair when specifying the countable family.

For each n choose a countable dense subset of
`D_n=C_c^infinity(R^(4n)\Delta_n)` in E_n. Such a set exists: cut a
flat Schwartz function off at infinity, then cut it off within epsilon
of each coincidence plane. Each derivative of the latter cutoff costs
a fixed inverse power of epsilon; flatness supplies an arbitrarily high
positive power. The resulting sequence converges in every Schwartz
seminorm. These separable test spaces therefore have countable dense sets.

Take their rational-complex linear span, and close it countably under
permutations, conjugation, reflection, the group generated by the rotation
Q of L08, hypercubic symmetries and rational translations. Add dense
compact ordered-positive test sets in every degree and every admissible
`theta(F_n^*) tensor G_m` from them, all required motion-derivative tests,
and the countable witness family of L20. Enumerate the CARTESIAN product
of observable, group, derivative, degree, and geometry indices. Call
the resulting countable collection D. This does not require one finite
cutoff to satisfy infinitely many tolerances.

For each fixed degree the L05 bound makes values on each D test bounded.
Successive subsequences and the Cantor diagonal yield convergence on all
of D. If `F_l->F` in `|.|_(11n)`, then for two regulators j,k

    |S_n^j(F)-S_n^k(F)|
       <=2 C^n(n!)^b_0 |F-F_l|_(11n)
                                  +|S_n^j(F_l)-S_n^k(F_l)|.

For noncompact F this is the definition of the extension; first take
j,k large for compact F_l, then l large. It defines a unique continuous
S_n on E_n, with the same bound. No wrapping of a noncompact test onto
a finite torus is being assumed. The same estimate with a finite net
proves uniform convergence on compact subsets of E_n, including each
fixed compact motion orbit and its derivative tests. The motion action
is continuous in Schwartz seminorms and preserves flatness; for a common
translation by u its bound retains the insertion count,

    |T_u F_n|_k <= 2^(k/2)(1+n|u|^2)^(k/2)|F_n|_k.

There is no claim of a rate uniform over all n or all tests.

## L07 — DRAFTED(high): thermodynamic and continuum limits, on one selection

**Consumes:** L05–L06, one tuned trajectory, and compatible finite tori.
**Produces:** the flat common hierarchy and a finite-regulator diagonal
which also satisfies any applicable pressure constraints of L09.
**Most likely failure point:** interlacing two estimates whose allowable
cutoff/volume windows do not overlap.

For each fixed a in the countable L-adic sequence first let R tend to
infinity through compatible tori. Every compact lattice observable is a
finite sum and is bounded at that a. In particular the centering constants
are bounded at fixed a. A countable diagonal gives a thermodynamic
subsequence for every D test and every needed centering constant. Thus
define `S_n^a(F)=lim_(k->infinity) S_n^(a,R_(a,k))(F)` on compact tests.
It is not claimed to be independent of the chosen thermodynamic phase.
L05's estimates pass to it. Now choose a subsequence a_j tending to zero
on which every S_n^a value in D converges; extend by L06.

Choose R_j from the thermodynamic sequence at a_j sufficiently far out
that it exceeds j, embeds the first j supports and RP stencils, and
approximates the first j thermodynamic moment values within 1/j. Include
the first j exact witness tests. Then

    S_n^(a_j,R_j)(F) -> S_n(F)             for all n and F in E_n,
    S_n = lim_(j->infinity) [lim_(k->infinity) S_n^(a_j,R_(a_j,k))].

This is existence of iterated subsequential limits and their realizing
diagonal, not convergence of the entire array or interchange of limits.
For Q with denominators 5 choose `R_j in 10 N`; then every level has
even integral periods, including the commensurate rotated period lattices.

If L09 is used, at each fixed a the pressure limit is independent of
the thermodynamic subsequence. Add its finitely many constraints at
`0,+t,-t` and the required frames/periods before choosing R_j. For a
moving radius t=t_(j,F), demand pressure errors at most t_(j,F)/j;
for fixed source values, errors at most 1/j suffice. Both demands can
be met far enough out along the selected fixed-a volume subsequence.
For centered pressure approximants the state-independent centering
compatibility specified in L10 is an additional premise.

A cutoff-first fixed-R comparison cannot be added this way without a
compatibility estimate: `E_UV=aR` and `E_vol=1/(aR)` each have one of
the separate limits but cannot both tend to zero. This is why the
volume-uniform pressure comparison in L09 is an explicit input.

## L08 — PROVEN(TQ.md): the flat Ward route leaves an all-product charge

**Consumes:** TQ §5 U-all on the same D, maps, trajectory and sequence:

    d/ds S_j^F(s)+tau_j^F(s,r_F)=e_j^F(s,r_F),
    sup_s |e_j^F(s,r_F)| -> 0,
    tau_j^F=Cov(P_j(F_s), matched fine shell torque).

**Exact statement used:**

> TQ-min is equivalent to S(F_Q)=S(F), Q=exp(theta J), for every F∈D.

Here `cos(theta)=3/5, sin(theta)=4/5`, and TQ-min is
`integral_0^theta tau_j^F(s,r_F) ds ->0` for every F on that same
sequence. **Produces:** OS1 if U-all and TQ-min hold, with L06 continuity.
The integral identity proves the assertion without convergence of derivatives.
Since `exp(i theta)+exp(-i theta)=6/5` is not an integer, theta/pi is
irrational: a root of unity would have rational algebraic-integer sum.
Powers of Q are dense in one plane's circle. Hypercubic conjugation
gives all plane circles and hence SO(4); exact coordinate reflections
give O(4). Lattice translations approaching each fixed real translation,
and L06 equicontinuity, give translation invariance.

The pair-only ROTDEF §7 does not supply U-all. Its corrected decomposition
retains the actual coarse covariance

    q_j(s,r)=Cov_nu(E[F_j(s)|V], E[torque_(j,r)|V])/Z_e^2,

beside the conditional part. With the corrected SRCCD55 inputs the
pair error has the shape

    C_F [g_bare^2 + a^2 mathcalL(a)(1+r^5)
                         +r^4 exp(-mu(r-rho_F-1))],     mu>0.

Take a->0 at each fixed r, then r->infinity; the q term still needs
control. Replacing the refuted fine SRC-E variance bound by the name
SRC-E-prime does not prove it. At order n>2 derivatives of the
state-dependent centering also contribute
`-sum_i c_i'(s) E product_(k!=i)(O_k-c_k)`, which U-all must include.
A sampled all-product stress covariance `C_F(1+|x|)^(-4-epsilon)`
would make an absolute shell bound `O(r^(-epsilon))`; neither this
sufficient decay estimate nor the signed charge condition is inferred
from local moment bounds. None is a physical spectral-gap theorem.

## L09 — PROVEN(TQ2.md): the alternative flat pressure route

**Consumes:** LOC/COMMON and the following NC/PC estimates for every real
and imaginary part of every whole-product test F, including transported
tests. **Exact statement used (TQ2 §4.2):**

> Under COMMON and NC there is a common volume-first diagonal satisfying
> VQ-all. If PC also holds, that same diagonal satisfies
> \(\omega_j(F_Q)-\omega_j(F)\to0\) for every \(F\in\mathcal D\).
> With the common continuity/extension hypotheses it gives H_Euc.

**Produces:** OS1 on the L07 selection. For a bounded finite-range
fixed-cutoff approximant Y_a^G(F), independent of the volume/periods
once embedded, define

    A_(a,R,F)^G=a^4 sum_x tau_x Y_a^G(F),
    p_(a,R,F)^(G,P)(t)=R^(-4) log E exp(t A_(a,R,F)^G).

Translate the entire product, not its factors separately. At real t,
`p(0)=0`, `p'(0)=E Y_a^G(F)` and
`p''(t)=R^(-4) Var_t(A)>=0`. The fixed-cutoff finite-range cutting
argument in TQ2 §3 gives `p_(a,F)^G=lim_(R->infinity)p_(a,R,F)^(G,P)`,
independent of the commensurate period frame P. Its boundary constants
can depend on a and F. For a fixed countable t_l decreasing to zero,

    lim_(l->infinity) limsup_(j->infinity)
       [p_(a_j,F)^I(t_l)+p_(a_j,F)^I(-t_l)]/t_l = 0,        (NC)
    |p_(a_j,F)^I(t)-p_(a_j,F)^Q(t)| <= epsilon_(j,F)(t)->0. (PC)

Convex secants bound a derivative between `-p(-t)/t` and `p(t)/t`.
Exact transport gives `p_(a,F_Q)^Q=p_(a,F)^I`. On the common diagonal,
the tested rotation defect is therefore at most

    [p_(a_j,F)^I(t_l)+p_(a_j,F)^I(-t_l)]/t_l
       +[max_+/- epsilon_(j,F_Q)(+/-t_l)+2/j]/t_l.

First take j->infinity, then l->infinity. This proves the all-order
endpoint equalities, and the dense-group argument of L08 proves OS1.
If instead moving t_(j,F)>0 are used, both the pressure width/t and
the comparison error/t must tend to zero, with finite-volume errors
`<=t_(j,F)/j`. No interchange of a derivative and a thermodynamic limit
has occurred.

A sufficient producer of PC on a common coarse space at length ell_0 is

    sup_V |log Z_t^I(V)-log Z_t^Q(V)-c_(a,R,F)(t)|
                     <= (R^4/ell_0^4) eta_(a,F)(t),
    |c_(a,R,F)(t)-c_(a,R,F)(0)|/R^4 <= v_(a,F)(t).

Integrating the exponential inequalities, dividing by R^4, and subtracting
the t=0 identity gives

    |p^I(t)-p^Q(t)|
       <= v_(a,F)(t)+ell_0^(-4)[eta_(a,F)(t)+eta_(a,F)(0)].

These are extensive-source, all-data, volume-uniform inequalities. The
source-dependent scalar c cannot be dropped as vacuum normalization.
This route can prove symmetry without U-all; identifying its answer with
a vanishing matched Ward torque would additionally consume U-all.

## L10 — GAP: the actual flat symmetry estimates and centering match

**Consumes:** the flat R8/E0' hierarchy. **Needed output:** NC+PC+LOC on
its actual source prescription, or U-all+TQ-min on that same hierarchy.
Neither is supplied by H_INDUCT^ref or by the all-order upper bounds alone.

Pressure boundary independence does not imply independence of its derivative.
For instance, for V=R^4 and H_R=R^3 the two finite pressures

    p_+/-(t)=V^(-1)[log cosh(tV+/-H_R)-log cosh(H_R)]

have difference <=2/R and common limit |t|, whereas their derivatives
at zero tend to opposite signs. This is TQ2's diagnostic, not a Wilson
phase claim. Uniform susceptibility would suffice for NC, but involves
covariances of translated whole products, including overlapping supports;
R8 does not supply those correlations. A fixed-cutoff compact field also
does not give a fixed continuum real source radius for every polynomial.

There is a further explicit map requirement. L01 centers with actual
means, potentially dependent on R and orientation. LOC requires a
volume-independent approximant with fixed coefficients. One may choose
reference thermodynamic centering constants at each a, prove their
compatibility across the compared grids, and prove convergence of the
finite polynomial recentering corrections. At fixed a all factors are
bounded and the correction can be made arbitrarily small by enlarging R;
its small-cutoff comparison across orientations still needs the same
one-point and product estimates. Alternatively prove PC directly for
the prescribed maps. The exact same normalization and subtractions must
appear in the extracted hierarchy and the witness. Simply declaring
state-dependent means fixed during a rotation or pressure tilt is not a
proof of this match.

## L11 — DRAFTED(high): check the pressure source window quantitatively

**Consumes:** a PC bound epsilon_j for the relevant transported product
valid at every `|t|<=r_j`, and the optional response bound
`p_j(t)+p_j(-t)<=K_j t^2` on that interval, with K_j>=0.
**Produces:** a sufficient nonempty moving-radius choice.
**Most likely failure point:** having the bounds only at a different
source radius or with unrecorded source-dependent scalar errors.

Assume `epsilon_j->0`, `epsilon_j/r_j->0`, and
`epsilon_j(K_j+1)->0`. For epsilon_j>0 set

    t_j=min(r_j/2, sqrt(epsilon_j/(K_j+1))).

Then t_j>0, t_j->0, and

    epsilon_j/t_j
       =max(2epsilon_j/r_j, sqrt(epsilon_j(K_j+1))) ->0,
    [p_j(t_j)+p_j(-t_j)]/t_j
       <=K_j t_j <=sqrt(epsilon_j(K_j+1)) ->0.

If epsilon_j=0, use `t_j=min(r_j/2,1/[j(K_j+1)])` instead.
For finitely many tests at stage j choose R_j large enough to make
all their pressure errors <=t_j/j as in L07. This proves mutual
compatibility under the displayed hypotheses, not their actual-model
availability. Without such a condition, shrinking the source radius can
make PC/t worse. A zero-source derivative bound is not the response
bound throughout this extensive tilt interval.

## L12 — DRAFTED(high): sphere seam cancellation under the actual law

**Consumes:** the positive normalized chain on the actual prism regulator
K_a of N5B, its net seam insertion mathfrakS, and the following E,D,T
inputs for every fixed radius R, cap product/path, and fixed J.
**Produces:** N5 for that product/path. **Most likely failure point:**
silently replacing an actual-law average by a supremum over coarse data.

Write h_i=aL^i, h_n=1, k=n-J,
`F_i=E[F|U_i]`, `S_i=E[mathfrakS|U_i]`. Past/future conditional
independence in the Markov chain, rather than nesting of single-level
sigma-fields, gives the exact telescoping identity

    Cov(F,mathfrakS)=sum_(i<k) E Cov(F_i,S_i|U_(i+1))
                                      +Cov(F_k,S_k).

For a degree-q product retain its normalization Z_a^q (Z_a=1 on the
present scalar branch). Assume, uniformly on each compact motion path,

    Z_a^(-q)||F_k-EF||_2 <= C_(R,F,v)(J)<infinity,             (E)
    inf_(scalar c) sup_(U_k)|S_k-c|=tau_R(a,J)->0 as a->0,    (T)
    Z_a^(-q) sum_(i<k) E|Cov(F_i,S_i|U_(i+1))|
                    <=delta_(R,F,v)(J)->0 as J->infinity.   (D)

They hold for `a<=a_0(R,F,v,J)` and n>J. Center the first factor
in the terminal covariance and subtract a SINGLE scalar c from the
second. Cauchy–Schwarz and (T) yield exactly

    sup_path Z_a^(-q)|Cov(F,mathfrakS)|
               <=delta_(R,F,v)(J)+C_(R,F,v)(J)tau_R(a,J).    (SEAM)

Given epsilon, fix J with delta(J)<epsilon/2, then take a sufficiently
small that C(J)tau_R(a,J)<epsilon/2. No bound uniform in J and no
optimized J(a) are required. A sufficient fine-covariance envelope is

    Gamma L^(p_s(n-i)) exp[-m d_0/(2h_(i+1))],   m,d_0>0,

whose tail is `Gamma sum_(j>=J) L^(p_s(j+1))
exp[-m d_0 L^j/2]`; its successive-term ratio tends to zero. This
is conditional fluctuation decay, not a physical mass gap.

This reproduces the implication confirmed by REVIEW_N5B items 3–5
while respecting its item 1. E and D remain actual-law estimates.
No coarse-law decorrelation is used in the deduction, but it has not
thereby become an all-data UV theorem. That stronger description would
also need, for example,

    inf_b sup_(U_k)|F_k-b| <= C(J)Z_a^q,
    sup_V E[sum_(i<k)|Cov(F_i,S_i|U_(i+1))| | V]
                                                  <=Z_a^q delta(J),

and analogous conditional bulk and moment producers. They are not
consequences of E/D. No such strengthened premise is smuggled into L12.

## L13 — GAP: sphere producers, profile and radius-uniform moment control

**Consumes:** the torus fixed-scale estimates and the finite prism
definitions. **Needed output:** E/D/T of L12 on the actual sphere law;
all-product bulk/observable Ward errors; and sphere analogues of L02–L05
with constants sufficient for the eventual flat E0' estimate.

The regulator is
`K_a=D_a union (boundary D_a times [0,1]) union theta D_a`, with
`beta_hat_p=(1/4)sum_(Q incident to p) beta_Q` and the stated normalized
shortest-path seam kernels. Its profile and kernel parameters stay fixed
during each source comparison. N5B F13 does not transfer the torus
Hessian, source, large-field, contour and backward-normalization estimates
to this regulator. A local equality of action formulas does not identify
the law obtained after integrating the exterior.

In particular `1<=Omega<=2` bounds local chart spacing, not every prism
edge or RG neighborhood. Require a finite C_geom controlling the latter,
`C_geom ell_ref<=ell_UV`, and a common nonempty kernel/Hessian interval.
The prism need not have a physical edge lower bound comparable to a.
The allowed dimension-three two-sided seam operator
`sum_i tr((A_i^+-A_i^-)(F_ni^++F_ni^-))` cannot be discarded by a
single-connection symmetry argument. Normalized positive kernels do
not impose exact equality of the two coarse connections.

The L-adic flat tuning does not prescribe `G(a Omega)` at every
non-L-adic spacing. Supply one reflection-paired radial profile and its
local coupling/observable matching (W0/W1/W3, including contacts and
coefficient-weighted insertions). On each cap path require

    sup_path Z_a^(-q)(|C_a|+|Cov(F,B_a)|) ->0
                                  at fixed R, for EVERY product order.

For the large-radius step require one C,A_0,b_0,q,c_* and crude envelope
after pole-chart pullback, independent of R on each admissible compact
test, with the same C working for every compact test; the required
minimum radius may depend on its support. Include uniform chart volume
and distance comparisons. At each R the cutoff range for the uniform
estimate must cover the whole allowed cap test class, for example
`0<a<=a_mom(R)` with `a_mom(R)>0`; select the realizing diagonal below
this threshold. Bounds only along a different cutoff sequence for each
test would not justify the L06 density extension of that diagonal.
Constants merely allowed to grow arbitrarily
with support diameter do not give the global weighted E0' seminorm.
Fixed-R Ward rates may depend on R; moment/extension constants used in
the second limit may not. Torus chessboard estimates, coordinate RP,
or the distance to the equator supply none of these missing inequalities.

## L14 — DRAFTED(high): sphere OS1 and its common iterated limit

**Consumes:** L12, the all-product Ward and uniform moment/geometry inputs
of L13, and the common scalar domain. **Produces:** a sphere-derived
flat hierarchy with OS1 on a common realizing lattice sequence.
**Most likely failure point:** using only pair Ward identities or only
radius-dependent continuity constants in the radius limit.

At fixed R the exact Ward split is

    d/dt mu(F_t)=-C_a(t)+Cov(F_t,B_a)+Cov(F_t,mathfrakS_a).

L12 and L13 make its normalized right side vanish uniformly along each
permitted compact cap path. Integrate before taking the fixed-R continuum
subsequence. Include all product, derivative and group-pair tests in D_R.
Moment compactness gives one continuum functional S_R with those path
identities. Extend from separated product tests to compact flat tests:
cover any compact off-diagonal support by finitely many product boxes
whose coordinate supports are mutually disjoint, take a smooth partition,
and approximate each smooth compact piece by finite tensor-test sums.
Continuity supplies the extension. No values on the coincidence set
are introduced by this argument.

In the pole chart z=2x, N5B §3.4 gives

    g_R=(1+|z|^2/(4R^2))^(-2) delta,
    v_(R,e)(z)=e+[(e dot z)z-|z|^2 e/2]/(2R^2).

The vector fields and all derivatives tend uniformly on compact sets
to the translation field e. Their fixed finite-time flows therefore
tend smoothly to translations on the slightly larger compact sets
containing the paths (integrate the vector-field error and the local
Lipschitz bound). Pole rotations and coordinate reflections are exactly
linear. By the uniform seminorm bound, replacing the contracting test
flow by its flat limit changes S_R(F) by a quantity tending to zero.
Hence any common R_j->infinity subsequential limit has translations,
SO(4), and the inherited reflections: OS1.

For each R_j first select its fixed-R continuum hierarchy. Extract a
subsequence of the S_Rj values on the full countable family using the
radius-uniform bound. Then choose a_j from THAT radius's continuum
subsequence so that a_j<1/j, the first j moment and RP pairings and
witness coordinates are approximated within 1/j, and the finitely many
Ward errors are small. In L12 choose each required J first and then a_j;
take the minimum of the finitely many positive cutoff thresholds.
This realizes the iterated limit on one diagonal without an R-uniform
Ward rate. Extend by L06. This is a separate selection from L07's flat
route. Neither route proves equality of their states or identifies
the sphere regulator with a flat periodic Wilson selection.

## L15 — PROVEN(HRP.md): finite reflection positivity for the actual law

**Consumes:** HRP's geometric half-edge algebra, reflection-paired Wilson
coefficients, and the zero-source normalized chain. **Exact statements
used (HRP §§3.1, 4.1):**

>     μ((Θ_l F)F)≥0 for every bounded measurable F in the closed-half algebra.

>     Z_ch=Z_Wilson,       E_ch[A(U_0)]=μ_Wilson(A).

The first is for even periodic tori, paired finite real coefficients and
nonnegative crossing coefficients. For the site-plane choice used here,
HRP §3.2 proves positivity for all paired finite real coefficients by
conditioning on the spatial links W in BOTH fixed planes:

>     Z Q_μ(F,F)=∫ e^{-S_0(W)}
>        |∫ F(X_+,W)e^{-S_+(X_+,W)}dX_+|² dW ≥0.

For the actual sphere profile HRP §5.3 states:

>     μ_{K_a}((Θ_μF)F)≥0.

**Produces:** finite-cutoff RP for bare clover observables in either
route, subject to the stated profile and geometric support conditions.
Temporal extent-two parallel edges are distinguished by their geometric
arcs, not their endpoint names. This is the correction confirmed in
REVIEW_HRP_HALF_ARC_ASTRA; both periodic fixed planes are retained.
Successively integrating the normalized kernels proves the marginal
identity. No RP of a conditional/coarse/tilted law is inferred. The
sphere result is for the four coordinate great-sphere reflections;
additional planes use the eventual state invariance, not averaging.

## L16 — DRAFTED(high): pass OS2 on the full ordered-half domain

**Consumes:** L15 and the L06–L07 or L14 common hierarchy.
**Produces:** the full restricted OS2 quadratic form for S.
**Most likely failure point:** admitting a same-half collision test or
an observable whose bare-link stencil crosses the reflection plane.

Let F be a finite sequence of compact tests in `0<t_1<...<t_n`.
For small enough a every clover stencil is inside the closed positive
geometric half, and the remote periodic plane lies beyond its support.
On the sphere use the pole cap and its exact coordinate reflection.
The observable reflection is antilinear; test reflection is linear and
star supplies the single conjugation. Consequently

    Q_j(F)=sum_(n,m) S_(n+m)^j(theta(F_n^*) tensor F_m)
          =mu_j(overline(A_F(rho U)) A_F(U)) >=0.

Every test in that finite sum is compact and flat: the negative and
positive tuples are separated and each tuple is strictly time ordered.
Their common-sequence limits therefore give Q(F)>=0. For a general
Schwartz ordered-half F, approximate by compact tests cut off away
from t_1=0 and every adjacent time coincidence. Boundary flatness
absorbs all cutoff derivatives, as in L06. The inequality

    |theta(F_n^*) tensor G_m|_k <= |F_n|_k |G_m|_k

follows from `1+|X|^2+|Y|^2 <=(1+|X|^2)(1+|Y|^2)` and the derivative
product rule. Continuity of each S_(n+m) passes Q>=0 to all finite
sequences in the ordered-half domain. OS1, when supplied by the chosen
route, transports this to every affine hyperplane. This argument never
uses or claims finite ordinary moments of e(f)^2 on colliding tests.

## L17 — DRAFTED(high): OS3, reality and normalization survive

**Consumes:** the same real bare scalar maps and common moment limits.
**Produces:** `S_n(F^pi)=S_n(F)`, `S_n(conjugate F)=conjugate S_n(F)`,
`S_0=1`, and `S_1=0`. **Most likely failure point:** changing the
centering or label prescription between the different consumers.

At every cutoff the scalar factors commute, so relabeling the finite
lattice summation proves the permutation identity exactly. Real fields,
real centering and real volume weights give the reality identity.
Probability normalization gives S_0=1, and centering gives S_1=0.
The limits preserve all four identities on compact tests; density and
continuity preserve them on E_n. No rotation argument, clustering or
ordinary same-half positivity is needed for OS3.

## L18 — PROVEN(REC_CONT.md): E0-prime through OS3 give full continuation

**Consumes:** ONE hierarchy from the preceding steps, with E0', full
E(4) invariance, ordered-half RP, permutations, reality, and S_0=1.
**Exact statement used (REC_CONT §1, quoting REC_LIB §6):**

> For each n and
> ordered label word a, there are holomorphic functions 𝒲_n^a on
>
>     𝒯_n={z∈C^(4n): Im(z_(j+1)−z_j)∈V_+, 1≤j<n},

The same statement specifies

>     |𝒲_n^a(x+iy)| ≤ C_n(1+|x|+|y|)^B_n (1+d_n(y)^−1)^A_n,
>     d_n(y)=min_(j<n){(y_(j+1)−y_j)^0−|(y_(j+1)−y_j)⃗|}.   (6.1)

**Produces:** these matching holomorphic functions, their tempered
boundaries in all real spacetime variables, common complex-translation
invariance, and equality with the original S_n on compact strictly
ordered Wick-slice tests. Scalars are the rank-zero case of the reviewed
finite Cartesian tensor theorem. No new tensor-family estimates are
inferred from e-only bounds. The constants A_n,B_n,C_n may depend on n;
the INPUT E0' triple may not.

The exact all-n interface match is quantitative. From L05,
`(s,alpha,beta)=(11,exp(C),p_eff+3)`. REC_CONT (3.2) uses

    D_0=max(1,alpha),  gamma_0=beta+24s+100=beta+364,
    t_0=12s+36=168,
    |S_n(X)|<=D_0 K_0^n(n!)^gamma_0
       [1+sum g_i+(min g_i)^(-1)+sum |xi_i|]^(t_0 n),

on ordered real configurations, g_i>0. K_0 is precisely the finite
constant of REC_CONT (3.3):

    b_s=2s+10, c_s=4s+15,
    K_1=2^(r_max+beta+7s+4)10^s c_s^(2s)5^(s+3)exp(4s+3),
    K_0=K_1 2^(8s+39)(8c_s)^c_s(48b_s)^b_s
                                 128^(2s+c_s)exp(9s+40),   r_max=0.

Its SEED constants in (6.9) are
`D=D_0, gamma=gamma_0, t=t_0, K_seed=K_0 2^gamma_0 4^t_0`.
These are derived constants, not independent windows to be tuned.
REC_CONT §§3–11 then remove smearing, construct compatible axial cuts,
convexify and exhaust the time domains quantitatively, and extend the
spatial variables by the proved spectral/Fourier–Laplace construction.
E0' is used before the final boundary step. Single-cut semigroup
analyticity alone would not replace it. REVIEW_REC_CONT_R2 and
REVIEW2_REC confirm this precise implication; no actual YM seed is an
output of the abstract theorem.

## L19 — PROVEN(REC_LIB.md): reconstruct the same scalar sector

**Consumes:** L18's exact L-CONT output and the SAME S satisfying the
other displayed axioms. **Exact statement used (REC_LIB §18):**

> then L-BV, L-BOOST, L-LOCAL, L-POS, L-GNS and L-ID/SPEC construct a local
> tempered Wightman theory on the Hilbert space of L-HILB. Its vacuum is
> cyclic and invariant, its joint spectrum is in the closed future cone,
> and its self-adjoint time generator is precisely the OS H. Its Wightman
> functions continue the restricted S_n.

**Produces:** a scalar Hermitian local tempered field on a dense invariant
polynomial domain, the OS Hilbert space, cyclic invariant unit vacuum,
and proper-orthochronous Poincare covariance with forward-cone spectrum.
The construction is unique up to field/vacuum-preserving unitary
equivalence; this is not uniqueness of the vacuum vector.

Specifically the Hilbert space is the completion of the ordered-half
space modulo its RP null vectors, with
`<F,G>=sum S_(n+m)(theta(F_n^*) tensor G_m)`. Positive time
translations yield the strongly continuous contraction semigroup
`P_t=exp(-tH)`, H>=0. The relevant growth is polynomial for each
finite vector, with `(1+n t^2)^(k/2)` retained. The identity
`||T_t F||^2=<F,T_(2t)F>` and iterated Cauchy–Schwarz remove that
polynomial growth and prove contractivity, including preservation of
null vectors. REC_LIB's insertion, boundary, positivity and GNS steps
identify this H with the Wightman time generator; a bare separated
Euclidean insertion is not already a general Minkowski field operator.

This output identifies the e-generated sector only. The scalar estimates
do not identify the full gauge-invariant Yang–Mills field algebra. No
E4, unique vacuum, positive physical mass threshold, or non-freeness
claim follows solely from the reconstruction implication.

## L20 — DRAFTED(high): the precise possible collapse and its witness

**Consumes:** common-limit convergence for a reflected separated test
pair, centering, and a positive lower bound on that same pair.
**Produces:** a nonzero OS vector orthogonal to the vacuum and hence a
nontrivial reconstructed e sector. **Most likely failure point:** using
a moving test, a changed normalization, or a witness on another algebra.

The point at which a trivial scalar limit can enter is the compactness
extraction in L07 or L14: every positive-degree S_n can tend to zero
despite all the upper estimates. The hierarchy S_0=1, S_n=0 (n>=1)
satisfies E0', OS1–OS3 and reality. L19 then quotients out every
positive-degree vector and returns a one-dimensional Hilbert space and
the zero centered field. Contact-only prelimit correlations are also
invisible on the chosen flat domain. The subsequent axioms and analytic
continuation cannot create a missing separated correlation. A
normalization tending to infinity can cause exactly this collapse;
Z_e=1 and a same-map lower bound prevent that escape.

Use WITNESS §1's fixed real nonnegative nonzero f supported in t>1,
`g=f composed theta`, `lambda_m=L^(-m)`, and
`f_lambda(x)=lambda^(-4)f(x/lambda)` (likewise g). Include every one
of these tests in D. For each FIXED m,

    V_m^j=lambda_m^8 S_2^j(g_lambda_m tensor f_lambda_m),
    V_m^j -> V_m=lambda_m^8 ||[e(f_lambda_m)]||_OS^2.

For centered fields the vector is orthogonal to Omega. Therefore
`liminf_j V_(m_*)^j >= v_*>0` for one fixed m_* gives
`||[e(f_lambda_m_*)]||^2 >=lambda_m_*^(-8)v_*>0`.
The same inner products are preserved by L19, so reconstruction cannot
kill this vector. This proves dimension greater than one, not a
strictly positive energy for that vector or a unique vacuum.

The fuller WITNESS E-TS contract is

    c_- u_(K-m)^(-kappa') <= V_m^(K,R)
                          <=C_+ u_(K-m)^(-kappa),
    0<kappa<=kappa', c_->0, K>=m+d_0, R>=R_0, m>=m_0,
    U_-(m)<=u_(K-m)<=U_+(m),
    U_+/-(m)=g_ref^(-2)+beta_+/- m log L +/- R_F, beta_->0.

It implies the uniform fixed-m lower bound
`V_m^j>=c_- U_+(m)^(-kappa')>0`. Pass the cutoff/volume limit
FIRST for each m. Only then may m->infinity: the upper bound gives
V_m->0 while `lambda_m^(-epsilon)V_m->infinity` for every epsilon>0.
This is the stated short-distance discriminator against WITNESS's
specified canonical finite free-field class. It is not a separator
against all generalized-free/Wick-composite realizations; WITNESS §§3,6
give counterexamples to those broader identifications. For an elementary
Gaussian e hierarchy a distinct finite-coordinate separator is a nonzero
separated connected fourth moment, which needs its own estimate. No such
non-freeness conclusion is added to the lower-norm argument above.

## L21 — GAP: supply the actual witness lower bound on the selected route

**Consumes:** real-derivative upper bounds and the chosen hierarchy.
**Needed output:** the positive fixed-test lower bound in L20, or the
stronger E-TS/C4-sep contract for its explicitly named comparator class,
on the SAME normalization and sequence. Upper bounds cannot provide it.

The named PL-1L route is a quantitative signed matching estimate, not
the assertion that each scale contribution is positive. Write

    D_i=lambda^8 E Cov(G_i,H_i|U_(i+1))   (i<K),
    D_K=lambda^8 Cov(G_K,H_K),
    |sum_(i=0)^K (D_i-Lambda_i)| <=C_err u_k^(-2-theta),
                      k=K-m, theta>0.

Retain the terminal term D_K, the running couplings and every matched
normalization. WITNESS E11/E12 and the accompanying free bubble estimate
are actual remaining input obligations. If the leading bubble has lower
constant c_B>0 and its running-kernel correction is at most
`C_AF u_k^(-3)`, a sufficient lower-bound margin is

    C_err u_k^(-theta)+C_AF/u_k <= c_B/2.               (W-MARGIN)

For fixed constants it is sufficient that
`u_k>=max((4C_err/c_B)^(1/theta),4C_AF/c_B)`; if a numerator
vanishes its constraint is vacuous. This is a named inequality to check
with the actual output constants, not a computed YM margin. Constants
depending on g_ref cannot be frozen and then reused after changing
g_ref without proving their new bounds. A sphere application needs a
radius-uniform witness and the sphere map/profile match; the flat
WITNESS theorem explicitly does not supply that transfer.

## L22 — DRAFTED(high): endpoint theorem and end-to-end interface check

**Consumes:** the contracts explicitly listed below. **Produces:** the
conditional endpoint, its exact limitations and an interface check.
**Most likely failure point:** claiming the same hierarchy while changing
the regulator selection, centering, field family or witness normalization.

**Conditional endpoint.** Assume the tuned real trajectory and actual-law
source identification of L01, and close L02 by IND-J or literal R9.
For the flat route additionally supply L10's pressure package (with
compatible radii) or its all-product Ward alternative. For the sphere
route instead supply L13, including radius-uniform flat-test constants.
Then the corresponding common diagonal has the scalar restricted
Schwinger hierarchy satisfying E0', OS1, OS2, OS3, reality and S_0=1.
L18–L19 give its local tempered Wightman reconstruction on the same OS
Hilbert space. If L21's same-test positive witness is supplied on that
selection, the centered e field and the vacuum-orthogonal sector are
nonzero. Both routes remain live; neither is chosen in advance or
identified with the other. A full physical field-family identification,
vacuum uniqueness, and physical mass gap are outside this conclusion.

The composition can be checked by these exact interface identifiers:

| Consumer | Consumed output | Producer | Check |
|---|---|---|---|
| All-n moments | IND-J or literal R9, singletons and actual nu included | L02 -> L03 or L04 | Conditional; no mere fixed-order substitute |
| E0' | R8 with common A_0,b_0,q,c_*, crude power 4 and Z_e=1 | L03/L04 -> L05 | s=11, beta=p_eff+3, alpha=exp(C) |
| Compactness/extension | One seminorm bound for each n, same constants for every compact test | L05 -> L06/L07 or L14 | One D includes all degrees, pairings and witnesses |
| Flat OS1 | COMMON+NC+PC, or U-all+TQ-min | L08–L11 | L10 remains open; source pressures couple whole products |
| Sphere OS1 | E/D/T plus all-product Ward and radius-uniform bounds | L12–L14 | L13 remains open; no UV-only relabeling |
| OS2 | Exact zero-source bare RP and common flat-test convergence | L15 -> L16 | Geometric half-arcs, both cuts, one conjugation |
| OS3/(Re)/S_0 | Real commuting maps, common hierarchy | L17 | Preserved exactly |
| L-CONT | E0', E1, E2, E3, (Re), S_0=1, scalar rank zero | L05–L18 | One all-n triple; full spatial tube and boundary |
| Wightman theory | Exact L-CONT on that same S | L18 -> L19 | Same OS Hilbert space and H; no E4 imported |
| Nontrivial sector | Fixed reflected pair with liminf V_m>0 | L20–L21 | L21 remains open; quotient preserves its positive norm |

**Constant and limit windows.** All upstream constants below are named
symbols with the inequalities that must hold; none is assigned a
fabricated number.

| Window | Required inequalities and compatibility check |
|---|---|
| Common flat trajectory | L odd >=3, a=L^(-K), R in 10 N is compatible with even blocks and Q. Use one fixed nonzero g_ref, not one choice per cutoff. |
| Coupling bracket | `0<beta_-<=beta_+`, `R_F>=0`, `u_ref=g_ref^(-2)`, `u_ref-R_F>=gamma^(-2)>0`, and `g_ref<=g_sink`. Thus `U_-(m)>0` and `g_bare->0`. If gamma,g_sink are positive certified inputs, the scalar window `0<g_ref<=min(g_sink,(gamma^(-2)+R_F)^(-1/2))` is nonempty. Their upstream certification is assumed, not computed here. |
| Real kernels | One `0<kappa_-<=kappa_ker<=kappa_+<infinity` at every level; do not confuse kappa_ker with the witness exponents kappa,kappa'. Any additional sphere lower/upper restrictions require `max(lower bounds)<=min(upper bounds)` on the SAME constants. L13 supplies no proof of that intersection. |
| Separation/contacts | R8 applies for `delta>=c_*a`; crude flat Taylor bounds cover `delta<c_*a`. Contact-subtracted jets need `c_*` at least their interaction-range factor. Each fixed witness scale eventually satisfies `K>=m+d_0` and `lambda_m d>=c_*a`. |
| Large-field path conversion, if used | SRCCD55 E3/E14 require `80(exp(2C_LF)epsilon_LF+exp(-m_c M))<1`, not its superseded one-exponent version. Equivalently `m_c M>log 80` and `0<=epsilon_LF<exp(-2C_LF)(1/80-exp(-m_c M))`; this is a nonempty formal interval with the former inequality, but all-order outer moments still require L02. |
| Ward bulk window | Fixed r larger than the full support orbit, `r<=R/4-a`, `a^2 mathcalL(a)->0`, `g_bare->0`; then take r->infinity when needed. A moving-r rate is not substituted for those iterated quantifiers. |
| Pressure source window | Fixed t_l in the actual comparison domain, or `0<t_(j,F)<=r_(j,F)` with width/t and epsilon/t tending to zero and finite-volume error/t tending to zero. L11 gives an explicit sufficient compatibility test, not an unconditional choice. |
| Sphere physical-scale window | `C_geom ell_ref<=ell_UV`, matching positive weak-coupling/profile and kernel intervals. For each finite list first choose R and J, then a below every `a_0(R,F,v,J)`; this is compatible without an R-uniform Ward rate. Radius-uniform E0' constants remain essential. |
| Reconstruction | C finite and uniform; s=11, beta=p_eff+3>=0, alpha=exp(C)>=1. REC_CONT's t_0=168 and gamma_0=beta+364, K_0, K_seed are outputs. There is no smallness condition on these reconstruction constants. |
| Witness margin | c_->0 or c_B>0 and W-MARGIN, with the same g_ref and map. Fixed-m lower bound passes before m->infinity. A lower bound only for m=m(j)->infinity does not establish a nonzero fixed OS vector. |

The end-to-end check therefore reaches reconstruction conditional on
four exposed gaps. The three weakest links are: (1) the singleton,
outer-law and shrinking-separation export from INDUCT; (2) all-product
OS1, with the separate NC/PC and sphere seam/profile transfer burdens;
(3) a quantitative lower witness on the very same hierarchy. Exact
finite RP and the reviewed abstract continuation do not repair them.

The status count over the 22 numbered steps is **7 PROVEN, 11 DRAFTED,
4 GAP**. This counts implications separately from their open premises.
The sprint's new arguments have only author checking, as required by
the instruction to reach the endpoint and then check the whole chain.

## Source identities and verification record

The required files were inspected by their argument, consumer and erratum
sections; large historical summaries were not treated as authority over
later corrections. In particular the controlling reconstruction statements
are REC_LIB §§6,15,16,18 and REC_CONT §§1,3.1,6.1,7,10,11; OSLEAF55's
current definitions/REC/GROW/SP_lambda and ASSEMBLY55 N9 supply the
consumer match. The route checks use TQ §§1–5, TQ2 §§1–7, N5B's E/D/T,
ST and F13, REVIEW_N5B's binding item 1, ROTDEF §7 with its errata,
SRCCD55's corrected source/CD and outer-moment qualifications, and
HRP's geometric half-algebra, marginal and restricted limit passage.

| Source | SHA256 of the supplied snapshot |
|---|---|
| REALONLY.md | `3856594faffe9b1c6beab42f38385c820f06ab7476c4cbdd6934b5bf30bac019` |
| OSLEAF55.md | `c261a0c5eb300052445a05b3041b5ddf6e518445d3eacac36fc4421e60f66b78` |
| HRP.md | `d3a53ef3b29d09c774b1a836603ca731eeadb580127d3928dbbcd5dbe343699e` |
| REC_LIB.md | `47dd75c7ca3c4f9f1af43139292d1fcfa6774b10f8e6ea2babc05ad67a48e29a` |
| REC_CONT.md | `ac7ac0854fb320f183779f67be136063dfb750ee3f13b869acad10a7ac12a278` |
| TQ.md | `c184ec1ad4dfae8626676e99e4bc6ec2ec513c6230a6dc38b21ec00ba6d640aa` |
| TQ2.md | `3d9342a392f01d3e705e5fe381ca88aed20e4dd06c8138751be23e768e96e38a` |
| N5B.md | `317a1ba0a08ccd188e4c9c15bb7eeb8894e646a6521b3b4e8de6961e8d9693da` |
| REVIEW_N5B.md | `ae7eb7264f61d316d0dab20d1b01819b77e2502984901d3f563ce9711c6eb407` |
| ROTDEF.md | `413261674aaafa7c68793e9f10ebc1421fdf92871bd583f7c654981511104bf2` |
| SRCCD55.md | `80a347f5d2bc801fc0395b6d61aa5c0661dd098ae4430bcf760b874729761d03` |
| ASSEMBLY55.md | `c15524d7a1c3c04ce9c32567f6f61ec5113ebe24be9eba8de87f97e3109d326d` |
| INDUCT55.md | `2fbb4575b95d5c8f2d4ba25f93f1665274ba36b0e266c4ecb2bab9ad3f515000` |
| WITNESS.md | `f545b2b544234e9e2a133fb0957bee18cf2c290912897d5a5028ccadc484ecb8` |

Reviewed imports are limited by REVIEW_REALONLY, REVIEW_TQ,
REVIEW_TQ2, REVIEW_HRP_R2, REVIEW_HRP_HALF_ARC_ASTRA,
REVIEW_REC_CONT_R2, REVIEW2_REC and
REVIEW_REC_CONSUMER_ALIGNMENT_ASTRA. The latter's terminal OSLEAF55
and ASSEMBLY55 hashes match the snapshot above; stale source prose
calling that consumer correction pending does not erase its reviewed
scope. N5B's HOLD remains explicitly in force. None of these records
is a new audit certification.

Author verification checked all 12 quoted source blocks against their
named files (whitespace-normalized exact matches), all 22 unique step
identifiers, the 7/11/4 status count, and a consumes/produces contract and
single failure point for each drafted step. Mathematical readback checked
the factorial and seminorm interfaces, the two different orders of
limits, the single conjugation and half-support in RP, the pressure
window algebra, and fixed-test witness survival. It also made the sphere
cutoff threshold uniform over its cap test class explicit above.
Filesystem comparison against 4,049 pre-existing files found only the
addition of LIMIT.md, no removed or modified pre-existing files, and
unchanged hashes for all 14 source files listed above. These are author
and static checks, not independent review or numerical science evidence.
