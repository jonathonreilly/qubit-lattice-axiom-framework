# Polynomial history budgets: what sums, and the locality input it needs

Source: 8b1efefb17814662ce956f2744a66161b4125867; upper-chain Texts 14,
20.4, 21.1--21.2, 21.7; generated-observable-history.md (GH and its source
table). Continuation, 2026-11-01. **Implication** statements below are author
proofs, **unchecked** by an independent reader. **Gap** means an unproved
input, not a counterexample to Wilson Yang--Mills. No numerics ran here.
The two producer files were read for statements, not for a shared proof.

## 1. Budgets and the actual sources

Use x=x_j, x'=x_(j+1), t=x'/x, m_L=L^4. The notation beta_j below is the
extraction coefficient; call the good-set failure probability beta^GG_j.
All normalized observables are F^e_j=x_j e_j. Constants may depend on the
fixed geometry and thresholds, but not on the torus, K, or j. The reverse
kernels and the law class are exactly those in GH, including arbitrary
probability mixtures and the reference kernels at 1.

**Available source sizes [implication from the explicitly named inputs].**
Write C_A for the constant in (CF_j)(a), so that |A_j|<=C_A x_j on *all*
fields: use its K2 at regular point masses, then its prescribed regular
pullback extension. This is an input from CF, not a new deduction from
the bare recursion. Without CF the bound is only 12 x_j L^(4j).
From the regular current K1 estimate and its regular pullback extension,
section 2 of generated-observable-history.md gives

    |x' I_(j;c',c'')| <= C_I iota_j x'^(3/2) exp(-c_I d(c',c'')),
    |x' J_(j,c')| <= J_j x'^(3/2),
    J_j := C_I iota_j sum_(c'') exp(-c_I d(c',c'')) <= J_*.

Here iota_j means iota^new_j, including the logarithms of Text 18 when
that version is used. J_* is uniform provided that supplied iota_* is
finite. The torus sum is bounded by C sum_(r>=0)(r+1)^3 exp(-c_I r).
These are pointwise sizes. They are **not** a proof of current K3.

Fix f with |f|<=1 and Lip(f)<=1/l. Put alpha_j=a_j/l and
w_j(c)=exp(-c_r d_j(c,supp f)), with 0<c_r<c_*<c_I. The identically zero
test is treated as zero throughout. At a nonzero generated vertex use:

| Vertex v at level i | sigma_v | Proposed U_v(q), 1<=q<=4 |
|---|---|---|
| D, rho, h, Rem, H(a), H(rho) | 1 | A x_i^(3/2) |
| a | 1 | C_A x_i (also <= A x_i^(3/2)) |
| I_(i-1;c,c'') | iota_(i-1) exp(-c_* d(c,c'')) | C_I x_i^(3/2) sigma_v |
| r^f and its transported H(r^f) | alpha_i w_i(c) | A x_i^(3/2) sigma_v |
| d_(c,c') C_j D_(j,c), at level j+1 | abs(d_(c,c')) | A x_(j+1)^(3/2) sigma_v |
| f(c)D_(i,c)+r^f_(i,c) | abs(f(c))+alpha_i w_i(c) | A x_i^(3/2) sigma_v |

Increasing A by fixed geometric factors covers the H and individual
transport rows. Zero coefficients give identically zero vertices and do
not require division by sigma_v. These are explicit proposed budgets,
not the sharper TR_p conclusion. A is chosen below, independently of K.
All q in [1,4] use the same budget. The last row follows by addition once
the two individual rows hold. For the history estimate one may use the
weaker A x_i^(3/2) budget for the source leaves a and I as well, after
choosing A>=max(C_A,C_I). The current budget deliberately uses the slower
endpoint rate c_* that the missing locality estimate below would supply.

**Complete pointwise source bounds [implication].** Assume the lower-level
budgets have already been proved, |z_j|<=Z=2 and |beta_j|<=B_beta=1.
For a child c let U_e(c)=U_(j,c)^e(1). The reference number
v^e_(j,c)=P_j F^e_(j,c)(1) satisfies |v^e_(j,c)|<=U_e(c), because the
reference-fibre law is in LL_j. This uses *level j*, never an unproved
level-(j+1) output. The exact sources in GH therefore satisfy:

| Output at j+1 | Pointwise bound s_v for the *whole* source |
|---|---|
| A' | C_A x' |
| x'D' | t sum U_D(c) + Z J_j x'^(3/2) |
| x'rho' | t sum U_rho(c) + C_A x'[2Z m_L+Z+B_beta] + Z J_j x'^(3/2) |
| x'r'^f | t sum[U_r(c)+abs(d_(c,c'))U_D(c)] + (Z/2) x' sum abs(f(c')-f(c'')) abs(I_(j;c',c'')) |
| x'Rem | t sum U_rho(c) + B_beta C_A x' |
| x'H_j(e) | t sum U_e(c) |
| x'h | C_A x'(2m_L+1) + J_j x'^(3/2) |
| x'd C_jD_c | t abs(d) U_D(c) |

The sums in the reference columns run over the m_L children. In particular
the source of h is the *exact full-kernel difference*. Its size bound uses
|P_j A_j|, |v^a_j|<=C_A x_j, so it includes Q^s, cuts, and good-to-full-law
changes without an expansion or an assumption that they are tiny.
The beta a' and z-dependent terms in rho and Rem have not been discarded.

There are constants C_w,C_d,C_f depending only on the fixed geometry such
that w_j(c)/w_(j+1)(c')<=C_w for children,
|d_(c,c')|<=C_d alpha_(j+1)w_(j+1)(c') when d is nonzero, and

    sum_(c'') |f(c')-f(c'')| exp(-c_I d(c',c''))
      <= C_f alpha_(j+1) w_(j+1)(c').

For the second inequality, one endpoint is in supp f and the other lies
within one block, while Lipschitz continuity bounds the difference. For
the third, a nonzero difference has at least one endpoint in supp f;
w_(j+1)(c')>=exp(-c_r d(c',c'')), and the difference is at most
alpha_(j+1) d(c',c''). Sum the remaining exponential with rate c_I-c_r.
The first follows from d_j(c,supp f)>=L d_(j+1)(c',supp f)-C L.

Thus, with chi=sqrt(5/4), all these sources obey

    s_v <= S A x_(j+1)^(3/2) sigma_v,                     (S-poly)

for example with A>=max(1,C_A,C_I) and

    S = 1 + chi m_L(2+C_w/L+C_d)
          + C_A(4m_L+3) + 2J_*(1+C_f).

Extra deterministic sums use the sum of their displayed budgets.
The factor chi comes from t x_j^(3/2)/x'^(3/2)=sqrt(x_j/x')<=sqrt(5/4).
The normalization is not an implicit assertion that t=1.

**Bottom [discharged algebra; no probability premise].** The 24 Wilson
plaquettes with coefficient 1/4 give 0<=D_0=a_0<=12. Hence
|F^D_0|<=12x_0, rho_0=r_0=0. Along any length-J transport path the coupling
factors multiply to x_J/x_0. Its bottom cost before spatial coefficients is
therefore **12x_J**, not 12x_0 times an independent per-step bound.

## 2. Joint path probabilities, with the law quantifier kept

**Conditional inputs.** Use (FLOW-UL),(FLOW-END) of the companion note,
the stated lower envelope y_i=x_K/2+b'(K-i), and the *full* (RAR^ch)
for prescribed sets at several levels, both below regular tops and under
mu. For every generated vertex whose good set is used, require its K1 and
K3 with the proposed budget *at that vertex's own level*. The finite
good-set calculation then gives

    P_nu((GG_i^v)^c) <= exp(-c_G y_i^(3/2)),               (GG-prob)

uniformly for nu in LL_i. For example take
c_G=min(kappa,kappa_s) sqrt(c_lambda)/16 (omit kappa_s in the single tier),
where lambda_i>=c_lambda y_i as in section 7 of the companion note. The
finite union-bound integral has exponent at least a constant times
min(kappa,kappa_s) x_i sqrt(lambda_i); (FLOW-UL) bounds x_i by a fixed
multiple of y_i, so its polynomial prefactor is absorbed at large X. This is conditional on those K3 estimates; section 4
does not certify them. K3' uses the mixture trick and its factor two.

Write B_v=A_v union (GG_i^v)^c. Radius admissibility makes A_v a genuine
nearby nonregular-cell event. There are at most C_AA (x_i+2)^8 candidate
cells for its witness. Increase the final X, without changing alpha or
l_1, until

    log C_AA + 8 log(x_i+2) <= lambda_i                    (A-count)

at every i. Indeed x_i<=x_K+B(K-i), the derivative of the logarithmic term
is at most 8B/(x_K+2)<=l_1, and the inequality at K follows for X large
from l_0=alpha X and x_K<=2X. From
omega_i^(1/C_R)<=exp(-2lambda_i), a union over witness choices gives

    P_nu(intersection_(i in T) A_(i,c_i))
       <= exp(-sum_(i in T) lambda_i).                    (A-joint)

This holds for any prescribed cells c_i and interval T of levels below a
regular top, and under mu. It consequently holds under every GH top law:
a regular point mass at J is itself a regular top (an A mark at J is
impossible); a law below a higher regular top uses the full reverse-chain
tower; a mu marginal uses that same chain under mu; arbitrary mixtures
pass through the probability inequality by integration. No law conditioned
on a path event is placed in LL. One-level rarity alone would not prove
(A-joint). In particular the marked assertion under mu remains a producer
obligation, not a consequence of its unmarked one-level bound.

For a path with a>=1 consecutive bad vertices at levels J,...,J-a+1,
put h_a=floor(a/2), s_a=a-h_a and use its finer half, with offsets
h_a,...,a-1 from J. Either one GG fails there or all its A events hold.
The union bound and (A-joint) give

    P_nu(all a bad vertices) <= psi_J(a),
    psi_J(a) := min(1,
      s_a exp[-c_G (y_J+b'h_a)^(3/2)]
      + exp[-s_a lambda_J-l_1 sum_(r=h_a,...,a-1) r]).     (PATH)

This is a *joint-chain* estimate, not a product of bad-event marginals.
Intersecting with another event can only decrease its probability, but
does not multiply it by that event's marginal probability. Compared with
the old shorthand exp(-a lambda_J/q), (PATH) retains the precise half-path
and witness-count costs: even after dropping the extra l_1 term, its
q-norm probability factor is exp(-a lambda_J/(2q)). That loss is paid
below. It is not silently omitted.

## 3. The history sum itself closes, conditionally

**Lemma HS [implication, proof].** Suppose the source bounds of section 1,
(PATH), and the good-event bound

    |F_v| 1_(B_v^c) <= (A/8) x_i^(3/2) sigma_v            (GOOD-v)

are available for the specified finite generated graph. Then, for X large
after its fixed constants, GH proves (H20.5) with U_v(q)=A x_i^(3/2)
sigma_v for 1<=q<=4, uniformly in K and volume.

For clarity about (GOOD-v): if the output K1 coefficient obeys
eta_v<=C_eta sigma_v and its K3 has the proposed budget, the finite good-set
argument gives b_v<=C_pol C_eta x_i^(3/2)sigma_v+U_v/32.
Choose A>=max(32 C_pol C_eta,8 C_A,8 C_I,12). Then the preceding
b_v bound is <=U_v/16, hence (GOOD-v).
Neither K1 nor K3 is inferred from the conclusion of HS.

After division by sigma_v, the sum of absolute edge coefficients with
the factor t removed has a bound N depending only on L and the test
normalization. One may take

    N=max(2L^4, L^4(C_w/L+C_d), 1).

There are at most L^4 children per channel and at most two transported
channels in the r row. Other entries in the source table are source
leaves or deterministic sums, not extra edges at the same level. Induction
on path length therefore bounds the sum of normalized absolute path
weights at depth a by N^a x_J/x_(J-a). This is the precise version of the
old (2L^4)^a count; spatial weights can enlarge its fixed base to N.

The relative size of a polynomial leaf at depth a is

    (x_J/x_(J-a)) x_(J-a)^(3/2)/x_J^(3/2)
       <= (1+Ba/x_J)^(1/2).

Define the explicit scalar series

    E_J := sum_(a>=1) N^a(1+Ba/x_J)^(1/2) psi_J(a)^(1/4).

There is no unknown observable norm in this series; for a>J its displayed
psi expression is just a positive algebraic extension, not a probability
at a negative level. Take X>=2 and let Y=X/2, so x_J,y_J>=Y. Put
D=N exp(B/(2Y)), and mu_G=3 c_G b' sqrt(Y)/16. Convexity of u^(3/2) gives
(Y+b'h_a)^(3/2)>=Y^(3/2)+(3/4)b'sqrt(Y)(a-1).
Using s_a^(1/4)<=a, s_a>=a/2, and (1+t)^(1/2)<=exp(t/2), yields

    E_J <= E_*(X)
      := D exp(-c_G Y^(3/2)/4)/(1-D exp(-mu_G))^2
           + D exp(-l_0/8)/(1-D exp(-l_0/8)),             (SUM)

provided both denominator ratios are <1. This follows by summing
sum_(a>=1) a D^a exp(-mu_G(a-1)) and a geometric series, respectively.
For example differentiation of the finite geometric sum and passage to
its limit proves the first formula. Since l_0=alpha X, E_*(X) tends to
zero as X grows. This limit follows also by comparing powers with the
series for exp; no numerical fit or unrun computation is involved.

Now use GH with root event E=B_root. A good stop at depth a>=1 has a
bad vertices above it. A source at depth a>=0 has a+1 bad vertices,
including its own. A bottom leaf has J bad vertices and its actual
12x_0 bound. For q<=4, P(event)^(1/q)<=P(event)^(1/4), so

    H_q(v,nu)/U_v(q)
      <= [1/8 + S/N + 12/(A sqrt(Y))] E_*(X).            (HS-budget)

The source contribution uses the index a+1 in E_J and costs S/N.
The bottom term at a=J is bounded by 12/(A sqrt(x_J)) times that term
of E_J; the x_0 cancellation above is essential. Histories with zero
bottoms cost nothing. For J=0 use 12x_0<=A x_0^(3/2) directly.
Choose the final X so that the right side of (HS-budget) is <=1/2.
Then H_q<=U_v/2<=U_v-b_v and ||F_v||_q<=5U_v/8. This proves the
claimed conditional budget with slack; it is not u->u/4 for arbitrary
inputs. The normalization and full source costs are part of the theorem.

**Uniformity.** A,S,N and E_*(X) are independent of volume, cutoff K and
history depth J. U_v/(x_i^(3/2)sigma_v) is uniform. U_v itself grows with
x_i, and U_r also with alpha_i; it is not an absolute bound at all physical
scales. At a fixed distance K-i from the terminal physical scale,
x_i<=2X+B(K-i), so the displayed bound is cutoff independent there.
The bare 12x_0 and the elementary classical 12x_i L^(4i) grow with cutoff;
only the former is used, with its telescoping factor. HS does not yet
give the sharper mu bound ||x_i e_i||_q=O(1) required for TR_p.

**Bounded-copy attack [discharged algebra at this scope].** For the note's
F_J=b^J B, ||F_J||_q=b^J p^(1/q), so a homogeneous quarter-contraction
still fails. If its copied bad bit satisfies the present all-level rarity,
p is at most the right side of (PATH) for each full path. For pure A
paths it is in fact at most exp(-sum lambda_i). Thus its *absolute*
history cost is bounded by the corresponding term of E_J; it cannot
contradict HS while satisfying those hypotheses. A bounded bottom alone
does not imply (PATH) or (GOOD-v). The example remains an inference test,
not a Wilson countermodel.

## 4. The simultaneous locality induction: exact remainder to close

**Transport locality [implication, proof].** Fix an arbitrary nu' in
LL_(j+1) and put nu=nu'P_j. For r'<=m<=M' (primes mean j+1) with
k_m>=r_j, and G=F_(j,c), let
G_n=E_nu[G|V_j on Q_n(c)], n=k_m. From the *already proved* level-j
K2,K3, ||G_n||_2<=U and ||G-G_n||_1<=U B_j Phi_j(n).
Take conditionally independent W,W-tilde given their common restriction
to Q'_m(c'). They both have marginal nu'. The conditional-mean error of
P_j G is bounded by E|(P_jG)(W)-(P_jG)(W-tilde)|.
The two tails G-G_n cost 2U B_j Phi_j(n).

For the middle term truncate the fixed local function G_n at height T.
(SCR_j) costs tau_j(m)T. The two truncation tails cost at most
2||G_n||_2^2/T, because |z|1_(|z|>T)<=|z|^2/T. Choosing
T=U/sqrt(tau_j(m)) gives 3U sqrt(tau_j(m)); tau=0 follows by T tending
to infinity. Therefore, with

    K_j(m)=2B_j Phi_j(k_m)+3 sqrt(tau_j(m)),
    ell_(nu',m)(F)=E_nu'|F-E_nu'[F|W on Q'_m(c')]|,

    ell_(nu',m)(t sum_c P_j F_c) <= t sum_c U_c K_j(m). (K-transport)

The conditional mean is recomputed under the chosen mixture. No
linearity of K3 in nu and no membership of a conditioned law in LL was
used. Constant reference subtractions have zero locality cost. The radius
condition k_m>=r_j follows at large X from r_j<=r'+log(5/4)/(2kappa),
k_m=floor(mL/2), and L>2; it is not a use of K3 below its domain.

The source identities give the following exact sufficient bounds; define
L_a(m)=ell(A'), L_J(m)=ell(x'J), and
L_If(m)=ell(x' sum_(c'') (f(c')-f(c'')) I_(j;c',c'')):

| Output | Bound for its locality seminorm |
|---|---|
| H(e) | t sum U_e K_j(m) |
| D' | t sum U_D K_j(m) + abs(z_j) L_J(m) |
| h | t sum U_a K_j(m) + L_a(m) + L_J(m) |
| Rem | t sum U_rho K_j(m) + abs(beta_j) L_a(m) |
| rho' | t sum[U_rho+abs(z_j)U_a] K_j(m) + abs(z_j+beta_j) L_a(m) + abs(z_j) L_J(m) |
| r'^f | t sum[U_r+abs(d)U_D] K_j(m) + (abs(z_j)/2) L_If(m) |

CF supplies L_a(m)<=C_A x' B' Phi'(m). Its coefficient relative to
the proposed A x'^(3/2) budget is C_A/(A sqrt(x')), so it can be paid
without pretending the extraction source is small. For the transport
pieces the required numerical inequality is the corresponding row above
<= U_v(q) B' Phi'(m), for every m>=r'. Text 21.7 proposes profile
margins for those pieces; the extra t, weights and the constants 2,3 in
(K-transport) must be included. For m>M' one first proves the bound at
M' and uses
ell_(nu',m)(F)<=2 ell_(nu',M')(F), so this factor two must be reserved too.

**First unclosed source row [gap, I-K3].** For the actually specified
current, what remains to be derived (or supplied as an explicit additional
interface clause) is, with a fixed c_*<c_I,

    sup_(nu' in LL_(j+1)) ell_(nu',m)(x'I_(j;c',c''))
       <= C_loc iota_j x'^(3/2) exp(-c_* d(c',c''))
                         B' Phi'(m),    m>=r'.            (I-K3)

The analogous weighted sum then follows with c_r<c_* and the elementary
spatial sum above. This is a bound for the midpoint pullback extension
under arbitrary mixtures, with the actual reference law and the same
profile, including its floor. Already for two regular fields W,Wtilde
agreeing on Q_m, the admissible mixture (delta_W+delta_Wtilde)/2 requires
|F(W)-F(Wtilde)| to be at most twice the right side of (I-K3).
Thus this obligation cannot be paid just by a small probability of rough
fields. The source note supplies the pointwise current size from regular
K1; that does not establish (I-K3).

Here is a precise test of that shortcut. Take the single-tier profile at
one level, x large, lambda proportional to x, M=floor(exp(lambda/5)),
m=floor(M/2), and s=floor(sqrt(m/lambda)). On an abstract regular-shell
configuration let pullback to n erase shell bits beyond n, and put

    F=eta sum_(n=m+1,...,m+s) Phi(n) b_n,     b_n in {0,1}.

F(1)=0, each pullback increment has size at most eta Phi(n), and its
supremum is bounded by C eta, hence by C eta x^(3/2): for lambda>=1,
Phi(n)<=exp(-kappa sqrt(n)) before the cap, whose sum is finite by
grouping n between successive squares. All configurations
are regular and the regular pullback extension changes nothing. Choose
nu equally supported on the all-zero configuration and the configuration
whose displayed outer bits are all 1. They agree on Q_m, so

    ell_(nu,m)(F) = (eta/2) sum_(n=m+1,...,m+s) Phi(n)
       >= (eta s/2) exp(-kappa/2) Phi(m).

For large x, m>lambda, m+s<=M, and
sqrt((m+s)lambda)-sqrt(m lambda)<=s sqrt(lambda)/(2sqrt(m))<=1/2,
which proves the last inequality. But U B Phi(m), for
U=C eta x^(3/2), is C C_B eta x^2 Phi(m). It is smaller once
s>2 C C_B exp(kappa/2)x^2, which occurs since s has exponential rather
than polynomial growth in x. A fixed-distance antisymmetric pair can
carry this F and -F. This is a counterexample to the deduction
**regular K1 + polynomial size + regular pullback => I-K3**, not to the
specified current, (C2_j)(c), or the Wilson hierarchy. It also explains why
enlarging A by a fixed constant does not repair this shortcut.

A possible repair is to retain a stronger regular-current far-difference
estimate with an exponential rate strictly faster than kappa, and prove
that the midpoint extension preserves a sufficient version. (C2_j)(c)
and the tails of the coefficients of G^cur are the intended sources.
This still requires their quantitative use for the *actual* current:
G^cur depends on the background and the displayed recipe uses E^r with
Q^s dropped, whereas the one-step moment clause is written for the good
law. A size estimate or a K1 estimate alone cannot replace that check.
In particular, writing G_W=G^cur_(j;c',c'')(W,xi), the regular-law
attempt splits exactly as

    E_W^r G_W - E_Wtilde^r G_Wtilde
      = E_W^r(G_W-G_Wtilde) + (E_W^r-E_Wtilde^r)G_Wtilde.

To use the advertised (C2_j)(c), one must control the first term by tails
of the *background-dependent* coefficients and verify the normalized
local C^4 bounds for the second term in the law E^r. Dropping either term
would be an incorrect application of screening to a fixed observable.
The sufficient stronger target, for regular W,Wtilde agreeing on Q_n
about the midpoint, is, for fixed constants p,c_reg,c_end>0,

    t |E_W^r G_W-E_Wtilde^r G_Wtilde|
      <= C iota_j x'^(3/2) exp(-c_end d)
                          (1+n)^p exp(-c_reg (n-d)_+).   (I-REG)

Its rates must leave room relative to kappa and c_* when the midpoint
is changed to c' and when the extension is made. This is a stated missing
estimate, not a newly accepted premise. No proof of these coefficient,
law, and extension estimates is supplied here. On a producer with Q^s=0
the change-of-law issue disappears; the other checks remain. This does
not assert that the actual current fails them.

**Induction order and honest stop.** At step j+1 the permitted order is:
level-j moments/locality -> reference bounds and regular extraction ->
K1 at j+1 -> the locality rows above (including I-K3) -> K3' -> GG at
j+1 -> HS -> K2 at j+1. The estimates for z, beta and the regular
coefficients must be maintained in that same induction using the
lower-level inputs of Lemma 14.15 and the full regular estimate for h.
They are conditional inputs to HS, not consequences of its scalar sum.
For general Q^s, the first-order covariance sentence of Lemma 14.16 is
not a bound for the full change of law; Text 18 offers a producer-specific
full-law estimate on extra hypotheses. Those hypotheses must stay named.

Using a good-event bound for D', rho', h or r' before the corresponding
locality row is proved would assume the output needed to define its
small beta^GG. HS therefore does **not** complete the joint induction at
this stop. (I-K3), and the remaining explicit locality/profile and regular
coefficient budgets, are not newly certified here. No Q(n), higher-moment
claim, or cumulant level sum is inferred. The next decision is whether the
actual current's stronger regular locality and midpoint extension prove
(I-K3); if so, insert that bound in the displayed locality rows and check
their margins before invoking HS. Theorems 14.13 and 14.1c remain open.
