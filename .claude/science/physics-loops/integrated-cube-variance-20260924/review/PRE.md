# Independent PRE: time-integrated ordinary cube birth variance

2026-09-24. This is a selective independent mathematical reconstruction in
the supplied lambda=0 compensated cube, using the inherited model and reasoning
effort. It is not a formal audit, a physical law or a bath construction. No
root file under `fixed-time-variance-personal` or `averaged-variance-personal`
was read. No subagent was used. The new candidate remains undisclosed until
this PRE is sealed.

## Supported conclusion and remaining term

Use the original normalized actual first birth, original subsequent resolved
or coherent instrument, and complete ensemble rho_epsilon(t). Keep fixed
delta,K,kappa>0, integer S->infinity and epsilon^2 S(S+1)=delta/K. Fix
0<a<b<infinity. Let

    I_epsilon(a,b)=integral_a^b Var_{rho_epsilon(t)}(H_epsilon) dt.

The following lower bound is supported by the argument below:

    liminf_joint epsilon^2 I_epsilon(a,b)
        >= (kappa/2)[s_i(a)-s_i(b)] > 0,                         (1)

where s_i(t)=||psi_i(t)||^2 is the no-second-birth survival probability of
the supplied common rotor target started from beta_i. The microscopic
second-birth probabilities converge to 1-s_i(t), so the coefficient also
equals kappa/2 times the limiting probability of a second birth in (a,b].

An independently reconstructed, conservative rotor loss bound is

    2 I <= Gamma_B,infinity <= 16 I.                            (2)

It yields the explicit strictly positive estimate

    (kappa/2)[s_i(a)-s_i(b)]
      >= (kappa/2) exp(-16 kappa a)
                     [1-exp(-2 kappa(b-a))].                   (3)

Thus the ordinary variance integral diverges at least as a positive multiple
of epsilon^(-2). The supplied ordinary-energy parent's norm bounds also give
the coarse upper bound I_epsilon(a,b)=O(epsilon^(-7/2)). No sharp order or
pointwise full-ensemble variance limit is established.

The precise unresolved contribution can be retained. Let E_1,epsilon be the
exact grade-one Riesz projector of the no-event Hamiltonian, v_epsilon the
unnormalized full no-event vector and z_1=E_1,epsilon v_epsilon. Then

    epsilon^2 I_epsilon(a,b)
       -epsilon^2 integral_a^b ||H_epsilon z_1(t)||^2 dt
       -> (kappa/2)[s_i(a)-s_i(b)].                              (4)

The subtracted term is nonnegative and is not proved to vanish or remain
bounded. Formula (4), rather than a claimed full asymptotic equality to (1)'s
coefficient, records the remaining scientific question.

## Definitions and imported estimates

The graph, charge/field words, Gauss law, normalized spin shifts, actual marks
and canonical preparation are exactly those in the assigned parents. On the
N=6 sector after the actual first birth,

    H=delta epsilon^(-4)h,
    h=W+epsilon T+epsilon^2 C_S,
    T=-(F+F*),  C_S=P F*F P+P(D/C)P,
    C=S(S+1),  epsilon^2 C=delta/K,
    Gamma_S=sum_j j_S*j_S,
    h_eff=h-i kappa epsilon^2 Gamma_S/(2 delta),
    v(t)=exp[-i delta epsilon^(-4)t h_eff] phi_i.

Here P=1_(W=0), W=0,1,2 in N=6, and phi_i is the actual normalized
j_i U_epsilon Omega for the zero-field all-A-plus initial preparation. The
three first marks on edge 01 have leading normalized P vectors beta_i, with
b_i=2,2,4. The subsequent original instruments have the same loss Gamma_S;
their recycling outputs need not coincide. The second birth reaches N=8,
where H=0, so exactly

    Tr(H rho(t))=<v,Hv>,    Tr(H^2 rho(t))=||Hv||^2,
    s_epsilon(t)=||v(t)||^2=1-p_{2,epsilon}(t).                  (5)

No survival normalization is inserted into (5).

Let E_r be the exact no-event Riesz projectors for r=0,1,2. Define

    u=E_0 v,   z_1=E_1 v,   z_2=E_2 v,   v=u+z_1+z_2.

These are oblique, not mutually orthogonal, components. In particular u is
not a vector in the Hermitian low-energy band. Let J_epsilon map W grades
to these exact clusters as in the parents and let

    a_0=Pi_0 J_epsilon^(-1)v,
    u=J_epsilon a_0.

The ordinary-energy parent, read in full at its supplied hash, supplies the
following specific estimates; no fixed-laboratory-time rotor-tail substitution
is used here:

    sup_[0,b] ||w a_0(t)|| <= C_b,      w=1+sum_e E_e^2,
    a_0(t) -> psi_i(t) uniformly in norm on [0,b],
    a_0'=(-i KD+B_epsilon)a_0,         sup||B_epsilon||<infinity,
    J_epsilon P=P+epsilon F_S P+O(epsilon^2),
    sup_(t>=epsilon) ||z_1(t)||=O(epsilon^(9/4)),
    sup_(t>=0) ||z_2(t)||=O(epsilon^4).                         (6)

The last two bounds concern exact Riesz components and are propagated to all
later times by exact contraction. They do not require a relative approximation
to the rotor tail at t/epsilon^2. The low limit is

    psi_i(t)=exp[t(-i H_rot-kappa Gamma_B,infinity/2)] beta_i,
    H_rot=KD-delta Z_infinity*Z_infinity/2,
    Gamma_B,infinity=P F_infinity* Gamma_infinity F_infinity P,
    Z=Pi_2 T Pi_1 T P.

The parent also supplies uniform ordinary mean convergence, hence

    sup_[a,b] |<v,Hv>| <= C_(a,b).                              (7)

All constants may depend on the fixed interval and supplied positive
parameters, but not on the joint spin/epsilon sequence. Operators acting on
spin boxes are compared by the common physical-word zero extension. The
previously checked contour expansions and parity additionally give

    ||H||=O(epsilon^-4),
    ||(h_eff-r)z_r|| <= C epsilon^2 ||z_r||, r=1,2.             (8)

For (8), conjugate to the exact separated cluster coordinates. Their r-th
dimensionless blocks are r I+O(epsilon^2), and J and its inverse have common
norm bounds. This is an exact restricted-operator estimate.

## 1. The low no-event component has a large Hermitian energy norm

The exact physical no-event equation is

    v'=-i H v-alpha Gamma_S v,       alpha=kappa/(2 epsilon^2).

Every exact Riesz component satisfies the same equation. Consequently

    H u=i[u'+alpha Gamma_S u].                                 (9)

The second term in (9) must be retained. Replacing H by the no-event
generator would remove it and compute a different observable.

The weighted bound in (6), |D|<=Cw and the bounded low generator part give
||a_0'||<=C_b. Since J is time independent and uniformly bounded,

    sup_[0,b] ||u'|| <= C_b.                                   (10)

Also Gamma_S P=0 and the low-column expansion in (6) imply

    Gamma_S u/epsilon = Gamma_S F_S a_0+O(epsilon).

The operators Gamma_S F_S converge strongly with a common bound. Combining
this fact with the compact continuous limiting orbit of psi_i gives, uniformly
on [0,b],

    Gamma_S u/epsilon -> Gamma_infinity F_infinity psi_i(t),
    epsilon H u -> (i kappa/2) Gamma_infinity F_infinity psi_i(t).
                                                                    (11)

Thus the slow exact no-event component has a physical energy-vector norm of
order 1/epsilon whenever the displayed limiting vector is nonzero. This
does not contradict the parent's bounded Hermitian low-band second moment:
the oblique Riesz low component contains small Hermitian high-band admixtures.

There is also an exact integrated identity. For any differentiable solution
x of the original no-event equation, self-adjointness of Gamma_S gives

    ||H x||^2 = ||x'||^2 + alpha^2 ||Gamma_S x||^2
                    +alpha d/dt <x,Gamma_S x>.                 (12)

In particular,

    epsilon^2 integral_a^b ||H u||^2 dt
      = epsilon^2 integral_a^b ||u'||^2 dt
        +kappa^2/(4 epsilon^2) integral_a^b ||Gamma_S u||^2 dt
        +(kappa/2)[<u,Gamma_S u>]_a^b.                          (13)

Because the Gamma-supported part of u is O(epsilon), the endpoint
expectations in (13) are O(epsilon^2). Formula (10) controls the first
term. This is an alternative exact check of the limit from (11).

On the full rotor N=6 sector, Gamma_infinity is twice the projector onto
one-A/one-B adjacent-vacancy words. It is zero on the other words. Therefore

    Gamma_infinity^2=2 Gamma_infinity,
    ||Gamma_infinity F_infinity psi||^2
                  =2 <psi,Gamma_B,infinity psi>.

It follows that

    epsilon^2 integral_a^b ||H u||^2 dt
       -> (kappa^2/2) integral_a^b <psi_i,Gamma_B,infinity psi_i> dt
        = (kappa/2)[s_i(a)-s_i(b)].                             (14)

The last equality is the exact target survival law
s_i'=-kappa <psi_i,Gamma_B,infinity psi_i>. Its differentiability here
follows from the supplied finite-support initial state and the weighted
low-domain control. The coefficient has no missing delta: delta cancels
from the exact loss term in the physical equation (9).

## 2. Oscillatory low/high interference is negligible after integration

The components u,z_1,z_2 are not orthogonal for the Hermitian energy quadratic
form. Their energy cross terms cannot be dropped pointwise. Here is an
independent estimate of the relevant oscillatory integral.

For r=1,2 put

    omega_r=delta r/epsilon^4,
    q_r(t)=exp(i omega_r t) z_r(t),
    M_r=sup_[a,b] ||z_r(t)||.

Equation (8) implies ||q_r'||<=C epsilon^-2 M_r. From (9)-(10),
||Hu||<=C epsilon^-1. The deliberately loose bound
||(Hu)'||=||H u'||<=C epsilon^-4 suffices; no new weighted derivative
assumption is needed. Write

    integral_a^b <Hu,Hz_r> dt
        = integral_a^b exp(-i omega_r t) g_r(t) dt,
    g_r(t)=<Hu,Hq_r>.

Integration by parts once gives the explicit bound

    |integral_a^b <Hu,Hz_r> dt|
      <= C M_r [epsilon^-1+(b-a)(epsilon^-4+epsilon^-3)].        (15)

Indeed |g_r|<=C epsilon^-5 M_r and
|g_r'|<=C(epsilon^-8+epsilon^-7)M_r, while 1/omega_r=O(epsilon^4).
All quantities are differentiable at each finite spin. Using (6) on the
fixed interval, which lies after t=epsilon eventually, yields

    epsilon^2 integral_a^b <Hu,Hz_1> dt=O(epsilon^(1/4)),
    epsilon^2 integral_a^b <Hu,Hz_2> dt=O(epsilon^2).             (16)

These estimates are for integrated cross terms. They do not make a pointwise
claim about their sign or relative size.

Moreover ||Hz_2||=O(1) by (6) and (8), while
||Hz_1||=O(epsilon^-7/4). Hence its scaled squared norm and its scaled cross
term with Hz_1 vanish:

    epsilon^2 integral_a^b ||Hz_2||^2 dt=O(epsilon^2),
    epsilon^2 integral_a^b <Hz_1,Hz_2> dt=O(epsilon^(1/4)).       (17)

Expanding ||Hv||^2 in the three exact Riesz components, using (14), (16)-(17),
and subtracting the bounded mean square from (7), proves (4). The retained
high term is nonnegative, which proves (1)'s non-strict inequality.

The norm bounds also give ||Hv||^2<=C epsilon^-7/2 on [a,b], and thus the
stated coarse upper bound on the variance integral. This estimate is not a
sharp variance exponent.

## 3. A second exact route exposes the survival coefficient directly

Apply (12) to the full no-event vector v. By (6), z_1+z_2=o(epsilon)
uniformly on [a,b]. Thus Gamma_S v/epsilon has the same limit as in (11),
and <v,Gamma_S v>=O(epsilon^2). The mean is bounded by (7). Consequently,

    epsilon^2 I_epsilon(a,b)
       -epsilon^2 integral_a^b ||v'(t)||^2 dt
       -> (kappa/2)[s_i(a)-s_i(b)].                             (18)

The remainder in (18) is nonnegative. This proves the same lower bound
without having to identify every energy cross term. It independently checks
the sign and coefficient in (14)-(16).

The actual survival satisfies s_epsilon(t)=||v(t)||^2 -> s_i(t) uniformly
on [a,b], from (6), the low-column expansion and a_0->psi_i. Therefore one
may equivalently write

    epsilon^2 I_epsilon(a,b)
      = epsilon^2 integral_a^b ||v'(t)||^2 dt
        +(kappa/2)[p_{2,epsilon}(b)-p_{2,epsilon}(a)]+o(1).      (19)

Equation (19) is an asymptotic identity for the original full ensemble's
variance and second-event probabilities, with an explicit nonnegative
remainder. It does not assert that the remainder vanishes. The original
physical energy is still H, not h_eff.

## 4. A uniform rotor second-birth loss bound

This part was reconstructed directly from the original local charge hops.
In N=6,P there are two vacant B sites, all four A sites occupied, five
positive charges and one negative charge. Every B-vacancy pair has exactly
two common A neighbors. Call them active centers for that word.

Let P_a project onto P words whose two vacant B sites both neighbor a. Only
these inputs can contribute to P_bright F_a P. Different a have different
vacant A sites after F_a, so the loss separates exactly:

    Gamma_B,infinity=2 sum_a F_a* P_bright F_a,
    sum_a P_a=2 I.                                            (20)

For a local block, freeze all electric links outside the three-edge star
at a, and all matter charges outside that star. Gauss at each B leaf then
determines its incident star field uniquely from the leaf charge and the
frozen external fields. Gauss at a is preserved by the fixed local total
charge. Thus the following finite local matrices describe direct summands
of the complete physical rotor operator. No single Fourier phase or field
truncation is substituted for a physical state.

If the negative charge is outside the star, its two occupied local sites
both have positive charge. Label an input by the one occupied B leaf and
an output by the one vacant B leaf. The unsigned local hop matrix is

    A_plus = [[0,1,1],[1,0,1],[1,1,0]],
    A_plus* A_plus=I+J_3,

with eigenvalues 1,1,4. If the negative charge lies inside the star, the
local occupied charges are opposite. There are six inputs (occupied leaf,
sign at a) and six outputs (positive leaf, negative leaf). Each output has
two positive unit-amplitude preimages. The squared singular values are
0,1,1,3,3,4. Thus, denoting by P_a,out the active inputs with the negative
charge outside that star,

    P_a,out <= F_a* P_bright F_a <= 4 P_a.                      (21)

For any B-vacancy pair the two active centers have disjoint pairs of
occupied local sites: each pair consists of its A center and its third,
occupied B neighbor. The single negative charge belongs to at most one
of those pairs. Hence it is outside at least one active star, and

    sum_a P_a,out >= I.

Combining this fact with (20)-(21) proves (2) on the entire physical rotor
N=6,P Hilbert space. The possible kernel in an individual opposite-charge
local block therefore causes no global zero mode for Gamma_B. No analogous
uniform finite-spin lower bound is assumed at the spin boundary.

The survival equation now gives

    -16 kappa s_i <= s_i' <= -2 kappa s_i,
    exp(-16 kappa t) <= s_i(t) <= exp(-2 kappa t).

Applying the upper loss inequality forward from a and the lower survival
bound at a proves (3). Thus the lower variance-integral coefficient is
strictly positive on every nonempty fixed interval after birth, for each
of the three supplied actual marks.

## Finite checks and their limits

`independent_variance_checks.py` imports no campaign builder. Its exact
finite calculations check the two local Gram spectra, the complete 36-word
N=6,P combinatorial cover, and a separately constructed 36 by 36 flat-phase
Gamma_B=F_10* Gamma_1 F_10. The cover counts are 24 words with one guaranteed
same-sign active center and 12 words with two. A spurious oriented-incidence
replacement makes the same-sign local matrix singular, so the local lower-
bound check discriminates against that consequential incorrect sign model.

An exact two-dimensional algebra calculation checks (12)'s endpoint
coefficient. Its correct residual is zero; doubling that coefficient gives
the nonzero residual 156/49. A separate two-level dissipative diagnostic
numerically illustrates that a slowly evolving exact no-event low eigenvector
has a Hermitian energy norm of order 1/epsilon. On [0.2,0.4] at kappa=0.7,
the scaled integrated low energy-square approaches the predicted coefficient
0.0646011371624187; errors at epsilon=0.2,0.1,0.05,0.025 are about
0.00394,0.00101,0.000256,0.0000640. This toy is explicitly not the cube and
does not prove its limiting theorem.

Command executed:

    PYTHONDONTWRITEBYTECODE=1 python3 independent_variance_checks.py > FINITE_CHECKS.log 2>&1

It exited zero. The entire log was inspected. `FINITE_CHECKS.json` also
contains all 36 cover rows and the exact flat-phase characteristic roots.
The proof of the rotor operator bound is the physical-star direct-sum
argument above, not extrapolation from a flat fiber. No large-spin finite-
time numerical variance sequence was run, and no numerical test is being
used to replace the oscillatory estimate.

## Scope, failed shortcut and recovery obligations

- The result concerns a time integral on fixed 0<a<b. A divergent integral
  does not establish a pointwise lower bound or divergence at every fixed
  time. Oscillatory cancellations remain a pointwise issue.
- Ordinary mean convergence does not bound ordinary second moments. Nor
  does decay of the initial exact high Riesz component make the exact low
  Riesz component an energy-bounded vector: (9)-(11) exhibit its energy cost.
- A relative rotor-tail formula at t/epsilon^2 was not used. The full
  high Riesz remainder in (4) or the derivative remainder in (18) is open;
  setting either to zero would overstate this PRE.
- The strict positivity uses the rotor loss bound (2), fixed positive
  kappa, and the supplied cube/charge sector. It is not a lower bound for
  every graph or spin-boundary state. The lambda=0 zero terminal Hamiltonian
  is essential to the full-ensemble identity (5).
- Canonical zero-field preparation, the compensation, GKLS law, joint
  resource scaling and positivity of fixed parameters remain model premises.
  No heat, work, reservoir, empirical selection or new axiom is supplied.
- The precise next unresolved quantity is
  epsilon^2 integral_a^b ||H E_1 v||^2 dt. Its vanishing would sharpen (1)
  to a full scaled integral limit; the present bounds do not prove it.

## Source identities and exposure boundary

The assigned base science revision is
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The ordinary-energy publication
checkout was read at HEAD `c234d47c9d99b7fd5590957ec08d9083877d25e6`:

    /Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/ordinary-energy-publication

The new parent was read in full:

    docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md
      4a484ec7403e3f2306454fe01cfb91cdf2a7f601d2e896aaef6307134deec28f

The following previously read sources were hash-verified unchanged and
reused for model definitions, the exact no-event cluster expansions and
the compensated low coefficient:

    docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md
      af0b8e6494ea54cdb450e430a45e9d89d9e1e931e21b9a74ab2b4ea260a3a718
    docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md
      f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9
    docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md
      c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b

The workflow and reviewer skill were verified unchanged at
`d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4` and
`9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455`.
Their already read instructions were reused. This selective calculation
does not independently re-certify every transitive sharp-tail or weighted
estimate in the ordinary-energy parent; the exact reused bounds are listed
in (6)-(8), and the new conclusion is conditional on them.

All new files are in the assigned `averaged-variance-independent` directory.
No private next-variance author source, candidate or checkpoint was read,
and no science checkout, audit state, existing PRE/POST or publication was
modified. The immutable PRE hash and evidence hashes are recorded in
PRE_SEAL.json before any candidate release.
