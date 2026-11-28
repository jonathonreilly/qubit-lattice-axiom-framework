# New attack paths from the checked reduction chain (FINISH row 1158)

Worker: Claude Fable 5.2 high, laptop subagent. Started 2026-11-19 06:18Z.
Status marks: PROVED, ARGUED, GUIDE, OPEN.

## Plan (six steps)

1. State the Jaffe-Witten target for 4D SU(2) and the wall (W) in my own words.
2. Read the council brief, the council synthesis, and rows 1143-1157 with the files they name.
3. Choose one path among (A), (B), (C) or another. Say why it can be selective.
4. State its first lemma with quantifiers. Name the failing line for U(1), a massless factor, Q_8 and 2T.
5. Attempt the first lemma: proof, counterexample, or named failing line.
6. Compare with `parts/gap.md` (methods 1-36). Mark the path new or tried. End with RESULT.

## Step 1. The target and the wall, in my own words

**Target (Jaffe and Witten).** Build a quantum Yang-Mills theory with gauge group SU(2) on R^4. It must satisfy
the Osterwalder-Schrader axioms. Its Hamiltonian must have spectrum {0} plus a set inside [Delta, infinity) with
Delta > 0. So two things are asked: existence of the continuum theory, and a gap that survives the continuum
limit in physical units.

**Lattice form.** Wilson SU(2) on periodic tori, weight exp(-beta sum_p (1 - (1/2) tr U_p)), couplings beta_j
on an asymptotically free trajectory, spacings a_j to 0. Ultraviolet control is Balaban's renormalization group,
written up by Sussman and Alpoge (with Claude and Codex as authors of their text). It stops where the effective
coupling is of order one.

**The wall (W) (row 720, Theorem ZD-c).** Let D^+(L) be the excess free energy of the symmetric torus of
physical side L. Let z^-(L) = L m(L) be the lowest gap of the periodic cube of side L in units of 1/L, all eight
flux sectors included. (W) asks for L_0, D_0 with D^+(L) <= D_0 for every dyadic L >= L_0, and for one L >= 4 L_0
with z^-(L) > 256 D_0 + 30. Everything after (W) is proved in the lane.

**What (W) says physically (ARGUED).** z^-(L) is a running coupling. In a scale-invariant theory it is constant
in L. In a massive theory it grows like L. (W) asks that this coupling leave every bounded set, with the Casimir
energy staying bounded. So (W) is the statement that the theory generates a scale and has no massless state. A
proof must use a step that is false when z is constant in L (compact U(1), a massless spectator factor) and
false when the flux sectors stay degenerate (frozen Q_8, the binary tetrahedral group 2T).

## Step 2. What was read

Read in full: `library/gap-council-brief.md`, `library/gap-council-synthesis.md`, the RESULT lines of rows
1143-1155 (rows 1156 and 1157 have no RESULT line yet), and these sections:
`gap-solve2-astra62.md` Sections 7, 10, 11; `gap-solve4-astra62.md` "The signed quantity", Sections 1, 5, 6, 7, 8;
`gap-solve5-astra62.md` Sections 1, 2; `gap-solve6-astra62.md` from "The endpoint" to (8), and (24) to the end;
`gap-solve7-astra62.md` (1)-(2), (20)-(24) and (27)-(35).

The chain, in one notation (all on a fixed physical side L, n = L/a_j, N = n^3, T = n/2, beta = beta_j):

- F is the Wilson transfer operator on the gauge-invariant functions of one periodic spatial slice.
  J_T = 2 log Tr F^T - log Tr F^(2T). The strict test is limsup_j J_T < log(1651/1650) at one L. It is
  equivalent to (W) (rows 1145 Section 10 and 720). e^(-J_T) is the purity Tr rho_T^2 of rho_T = F^T / Tr F^T.
- (24), (30), (15), (28), (22) are the same number written as an integrated plaquette response along a
  coupling path that starts where the thermal defect is proved to vanish.
- Row 1153 (5): at periods m with m^4 beta^(-1/4) log beta to 0, the trace is a free gas of 3 colours times 2
  polarizations. Row 1153 (24): only levels with T E_i <= T E_o matter; a count bound
  D_j(x) <= K e^(eta (x - X)), eta < 1, would bound the total.
- Row 1155 (1)-(2): the gas states have vanishing weight at time T. Row 1155 (34):
  e^(-J_T) = A(B_T) u_2T / (8 u_T^2) + O(n^(-k)), where A(B_T) is the purity of the sector that is neutral under
  the three flat centre flips, and u_p is the probability of the trivial temporal twist class in the adjoint
  measure (35).

Status of sources: rows 1143-1153 are checked line by line by Claude Opus 5.5 (rows 1144-1154), no failed
statement. Row 1155 is unchecked today (its check, row 1156, is running). I use row 1155 only through (29),
(30) and (34), and I say so where I do.

## Step 3. The three paths against one test, and the choice

The test for a path: name the line of the path that reads the group and the whole state space. A line that
holds for compact U(1) at weak coupling, for SU(2) times a massless spectator, and for a frozen finite subgroup
cannot carry the wall.

### 3.1 Common notation: sectors and the vacuum chain

G = (Z_2)^3 is the group of flat centre flips R_b of the spatial slice. It commutes with F. For a character chi
of G, H_chi is the sector. H_1 is the neutral sector. Levels: E_i = -log(lambda_i / lambda_0) >= 0 per lattice
step. m_+ is the lowest level of H_1 above the vacuum. eps_chi is the lowest level of H_chi, chi != 1.
z_+ = n m_+, z_chi = n eps_chi, and z^- = min(z_+, min_chi z_chi).

**PROVED (vacuum chain).** F = M C M with M = exp(-beta A_sp / 2) > 0 and C the gauge-averaged product of
normalized one-link Wilson convolutions (row 1149 Section 1). The kernel of F on the gauge quotient is continuous
and strictly positive. So lambda_0 is simple and psi_0 > 0 (Jentzsch). Put mu = psi_0^2 dHaar and
Q f = (lambda_0 psi_0)^(-1) F (psi_0 f). Then Q is self-adjoint on L^2(mu), Q 1 = 1, Q has a positive kernel
q(x, dy), Q >= 0 as an operator, Q commutes with G, and spec Q = {e^(-E_i)}. With phi = M psi_0,

    Q f = C(phi f) / C(phi).                                                        (M)

Proof of (M): F psi_0 = lambda_0 psi_0 gives C(phi) = lambda_0 psi_0 / M. So
(lambda_0 psi_0)^(-1) M C(M psi_0 f) = C(phi f) / C(phi). In words: the vacuum chain is the electric random walk
C, tilted by the positive function phi. Since phi(R y) = phi(y), the one-step likelihood ratio of a flat flip is
purely electric: q(x, R dy) / q(x, dy) = C(x, R y) / C(x, y).

### 3.2 Path (B): the energy-weighted count

**ARGUED.** The criterion of row 1153 (24), D_j(x) <= K e^(eta (x - X)), has two parts. With X = 0 it is a
bounded total. That part holds for the free photon gas: the number of multi-photon states with T E <= x on a
cube with T = n/2 does not depend on the cutoff and grows like exp(c x^(3/4)). So the X = 0 part is not
selective. It is a statement about ultraviolet normalization (row 1153 (1), the pressure route). With X large
the criterion is the gap itself.

**ARGUED.** A Weyl or Cwikel-Lieb-Rozenblum bound counts phase-space volume. Near the vacuum the magnetic energy
of SU(2) has the same quadratic form as three copies of U(1) (row 1153 (5) is this statement at short periods).
Away from the vacuum the classical SU(2) potential has flat valleys (the commuting constant fields), where the
classical count is larger, not smaller. A phase-space count therefore returns at least the free-gas count. For
a cube with T = n/2 the free-gas thermal sum is about 18 (GUIDE, a direct mode sum in pure Python:
6 polarization-colour species times sum over k != 0 of -log(1 - e^(-pi |k|)) = 6 x 0.4924 = 2.95, and
e^2.95 - 1 = 18.2; torons not counted). The wall needs 1/1650. The gain for SU(2) is a quantum effect in the valleys (Simon's mechanism for x^2 y^2, Luscher's toron
Hamiltonian), not a volume count. I found no line of (B) that reads it at order-one coupling.

**ARGUED.** There is a second problem. Levels are counted from lambda_0, which is known only to extensive
precision. Any operator inequality for F that is not in the vacuum representation (M) loses an extensive
constant. Row 1153 states the same fact for separate stability bounds.

Verdict on (B): its non-selective half is an ultraviolet problem; its selective half is the target. Not chosen.

### 3.3 Path (C): the one-step seam

**ARGUED.** Take row 1151 (1) in its range v <= c_0 / sqrt(n (1 + beta)):
log K_v(x, y) = c_j(v) + (v^2 / 4) sum_R a^(2 q(R)) w_R(x) w_R(y) + error. K_0 is the constant kernel. Expand
J(v) = 2 log Tr(B K_v) - log Tr(B K_v B K_v) to first order in the rectangle term. With b = <1, B 1>:

    J(v) = (v^2 / 2) sum_R a^(2 q(R)) [ <w_R, B w_R> / b - <1, B w_R>^2 / b^2 ] + higher order.

The bracket is the covariance of the rectangle loop w_R between the two ends of the open cylinder of T - 1
steps. It is non-negative because B >= 0. So the integrand of (22) starts as a sum of two-point functions of
neutral loops across the whole period. The group enters only through the decay of that two-point function. For
compact U(1) the same formula holds, with a photon in the correlator. (The higher orders are not controlled
here; rows 1149 (20)-(21) show that bounds uniform in the rest B stop at N beta v^2 = o(1).)

**ARGUED.** The seam kernel is a three-dimensional S^3-valued spin model on the vertices, in the external SO(4)
gauge field (x, y) (the Durhuus-Frohlich form). For typical pairs it is massive at the scale beta^(1/4) lattice
units, because the curvature of (x, y) is of order beta^(-1/2). This is the box scale of row 1153 (3). It is an
ultraviolet scale. A pinned-cell step would need a gain that survives to the physical scale. I see no such line.

Verdict on (C): the seam form does not separate the two failure modes; its first-order term is the neutral
correlator. Not chosen.

### 3.4 Path (A): the adjoint form splits exactly

Let a_p = Tr(P_+ F^p) / lambda_0^p = 1 + S_+(p) and c_p = Tr((1 - P_+) F^p) / lambda_0^p, p = T or 2T.
J_T^+ = 2 log a_T - log a_2T >= 0 is the neutral defect.

**Lemma S (split). PROVED.**

    J_T = J_T^+ + 2 log(1 + c_T / a_T) - log(1 + c_2T / a_2T),
    J_T^+ + 2 log(1 + c_T / a_T) - log(1 + c_T^2) <= J_T <= J_T^+ + 2 log(1 + c_T).

Proof. The identity is algebra. For the bounds use 0 <= c_2T <= c_T^2 (a sum of squares is at most the square
of the sum), a_2T >= 1 and a_T >= 1. In the notation of row 1155 (34): A(B_T) = e^(-J_T^+) up to O(n^(-k)), and
u_2T / (8 u_T^2) = (1 + c_2T / a_2T) / (1 + c_T / a_T)^2, since the neutral weight is
p_1(p) = a_p / (a_p + c_p) = 1 / (8 theta_0(p)). So the strict test is: the neutral purity is close to 1, and
the charged thermal sum c_T is small. This answers the first question of the row: yes, the test splits, exactly.

**Lemma Z (the Z_2 part is frozen). PROVED given row 1155 (29), which is unchecked today.** In the ensemble that
mixes the eight temporal twists, let pi_v(b) be the conditional law of the twist class b given the adjoint path
v. It is proportional to the Z_2 partition function with plaquette couplings beta w_p(v) and twist b. Then
E[1 - pi_v(bhat(v))] = P_mix(bhat != b) <= e_n := C n^4 e^(-c beta n^2). By Markov's inequality,
P(1 - max_b pi_v(b) > sqrt(e_n)) <= sqrt(e_n).
So, given the adjoint path, the twist class is known up to sqrt(e_n). The Z_2 gauge theory in the random
couplings set by the adjoint field is deep in its ordered phase for almost every environment. There is no
quenched vortex statement to prove. The factor u_p is the frequency of one value of a function of the adjoint
path. Both factors of (34) are statements about the one adjoint law (35). This answers the second question:
the "Z_2 vortex in a random environment" is not a separate dynamical problem.

**Which models must fail which factor. ARGUED (standard facts about the comparison models, not re-proved).**

| Model | Neutral factor (z_+ unbounded) | Charged factor (c_T small) |
|---|---|---|
| compact U(1), weak coupling | fails: z_+ stays bounded; the neutral sector holds the photon (z = 2 pi) and the level with two units of flux (z = 2 g^2) | fails: one unit of electric flux costs about g^2 / (2 n), so z_chi = g^2 / 2 |
| SU(2) times a massless spectator | fails: the spectator is neutral | holds if it holds for SU(2): the flips do not act on the spectator |
| frozen Z_2 above the Peierls coupling | holds | fails: the eight flux sectors are degenerate |
| frozen Q_8, binary tetrahedral 2T | fails: the neutral ground space is degenerate (flat holonomies that are not central) | fails |

A centre-twist tool can never see a spectator; that is the content of the council's point 2c. After Lemma F
(Step 4) the charged factor only has to exclude the ordered phase of the centre; the neutral factor has to
exclude everything else. (The table is compared with the lane's test table in Step 6.)

### 3.5 The choice

I choose (A). Reasons:

1. It is the only one of the three in which the two failure modes sit in two different factors (Lemma S and the
   table). In (B) and (C) one number carries both.
2. For the charged factor the vacuum chain (M) gives a new proved step, Lemma F below. It replaces "c_T small"
   by a statement with no small number in it: the flux gap is not parametrically below the neutral gap. The
   sufficient condition is an overlap bounded below, (TUN).
3. After Lemma F every remaining obligation of (A) is one statement about the neutral sector of the adjoint law
   (35), plus the soft condition (TUN). That is the smallest selective target I can state from the chain.

What (A) does not give: a mechanism for the neutral factor. I found none. This is said again in Step 5.4.

Note added after Step 6: the registry was closed when Steps 3 to 5 were written. Step 6 finds most of path (A) on
file (rows 876, 886, 892, 894; methods 13, 14, 17). Read the marks there before using any statement below as
new.

## Step 4. The first lemma of path (A), with quantifiers

**Definitions.** Fix a cutoff j, a spatial side n, and a generator R of G (a flat flip across one plane).
q_t(x, dy) is the kernel of Q^t. Put

    tau_t(x) = 1 - TV( q_t(x, .), q_t(x, R .) ),          taubar_t = integral of tau_t dmu.

Here TV is the total variation distance (between 0 and 1). tau_t(x) is the best achievable overlap between the
law of the slice at time t started from x and the same law after the flat flip. Equivalently,
taubar_t = 1 - TV(P_t, (1 x R)_* P_t), where P_t is the vacuum law of the pair (slice at time 0, slice at time
t). It is twice the Bayes error for deciding, from the two slices alone, whether a flat flip was inserted
between them.

**Lemma F (flux gap from neutral gap and tunnelling overlap).** For every beta > 0, every even n >= 4, every
character chi of G with chi(R) = -1, and every integer t >= 1,

    1 - e^(-2 t eps_chi)  >=  (1/2) taubar_t^2 (1 - e^(-t m_+)).                     (F)

**Corollary F1.** If m_+ <= 1 and t_* = ceil(1 / m_+), then eps_chi >= taubar_{t_*}^2 m_+ / 13. Hence, with
tau_* the smallest of the three numbers taubar_{t_*} (one for each generator),

    z^-(n)  >=  (tau_*^2 / 13) z_+(n).

So (W) holds if D^+ <= D_0 on the dyadic sizes above L_0 and, at one L >= 4 L_0,
z_+(L) > 13 (256 D_0 + 30) / tau_*(L)^2 along the trajectory.

**Remark F2.** (F) holds at every t. Since -log(1 - x) >= x, it gives
eps_chi >= taubar_t^2 (1 - e^(-t m_+)) / (4 t) for every t >= 1. The choice t = t_* is the one that returns a
fixed fraction of m_+.

**The selective statement the path then needs, beside the neutral gap:**

(TUN): there is tau_0 > 0 with liminf_j tau_*(j, L) >= tau_0 at the size L used in (W).

**Where each comparison model must fail.**

- Compact U(1) at weak coupling. Lemma F holds (it is true for every reversible positive Markov chain with a
  Z_2 symmetry). (TUN) holds too: the flux levels are (g^2 / (2 n)) k^2, so m_+ <= 2 g^2 / n (two units of
  flux), t_* is about n / (2 g^2), and by then the toron angle has spread by an angle of order one; my estimate
  is taubar about 0.05, independent of g (GUIDE, a wrapped Gaussian of variance 1/2 against its shift by pi).
  The ratio eps_chi / m_+ is 1/4. The failing line is the input "z_+ unbounded": z_+ <= min(2 pi, 2 g^2).
  ARGUED.
- SU(2) times a massless spectator. The chain is a product chain and R acts on the SU(2) factor only, so tau_t
  is the same function as for SU(2) alone (PROVED: total variation of product laws that differ in one factor).
  The failing line is again the input z_+ unbounded. Lemma F cannot fail here, and must not: the flux gap of the
  product is the flux gap of SU(2).
- Frozen Z_2, Q_8 and 2T at large beta. The failing line is (TUN). The flat holonomy class is conserved up to
  events of probability e^(-c beta n^2) per step (Peierls). Then (T1) below, applied to the set A of slices with
  one decoded sign, gives taubar_t <= 4 P(X_0 in A, X_2t in R A) <= 8 t e^(-c beta n^2). ARGUED (the Peierls
  estimate is standard and is not re-proved here). For Q_8 and 2T the neutral input fails as well (Step 3.4).

So Lemma F moves the whole exclusion of U(1) and of spectators to the neutral gap, and the exclusion of the
ordered centre to (TUN). (TUN) asks for a positive constant, not for a number close to 1.

## Step 5. The attempt

### 5.1 Three inequalities for the vacuum chain

Let f be a real eigenfunction of Q in H_chi with Q f = e^(-eps) f, eps = eps_chi, normalized by
integral f^2 dmu = 1. Put kappa = integral f^4 dmu. kappa is finite (f is continuous on a compact space) and
kappa >= 1. Since chi^2 = 1, f^2 is in H_1.

**Lemma J (pair bound). PROVED.** For every integer t >= 1,

    kappa e^(-2 t eps) - 1 <= (kappa - 1) e^(-t m_+),   that is   1 - e^(-2 t eps) >= (1 - 1/kappa)(1 - e^(-t m_+)).   (J)

Proof. Q^t is a Markov operator, so (Q^t f)^2 <= Q^t(f^2) pointwise (Jensen). Put g = f^2 - 1. Then g is in H_1,
g is orthogonal to constants, and |g|^2 = kappa - 1. Since f^2 >= 0,
<g, Q^t g> = <f^2, Q^t f^2> - 1 >= <f^2, (Q^t f)^2> - 1 = kappa e^(-2 t eps) - 1.
Since Q >= 0 and g is neutral and orthogonal to constants, <g, Q^t g> <= e^(-t m_+) (kappa - 1). QED.

In words: the square of a flux state is a neutral state (the "flux pair"). So the neutral gap is at most about
twice the flux gap, unless f^2 is almost constant. f^2 almost constant means f is close to +1 or -1: two wells
exchanged by R. That is the ordered phase of the centre.

**Lemma T (odd functions and tunnelling). PROVED.** For every h in L^2(mu) with h(R x) = -h(x) and every t >= 1,

    (Q^t h)(x)^2 <= (1 - tau_t(x)) Q^t(h^2)(x)   for mu-almost every x.              (T0)

Hence |Q^t h|^2 <= |h|^2 - <tau_t, Q^t(h^2)>, and for the eigenfunction f,

    1 - e^(-2 t eps) >= taubar_t - (1/2) e^(-t m_+) sqrt(kappa - 1).                  (T)

Proof. Let nu_x = q_t(x, .) - q_t(x, R .). Since h is odd, integral h(y) q_t(x, R dy) = -(Q^t h)(x), so
(Q^t h)(x) = (1/2) integral h dnu_x. The total mass of |nu_x| is 2 (1 - tau_t(x)), and
|nu_x| <= q_t(x, .) + q_t(x, R .). By Cauchy-Schwarz,
(Q^t h)(x)^2 <= (1/4) |nu_x|(all) integral h^2 d|nu_x| <= (1/2)(1 - tau_t(x)) * 2 Q^t(h^2)(x),
because h^2 is R-invariant. This is (T0). Integrate against mu and use the symmetry of Q^t for the second
claim. For (T): tau_t is invariant under all of G (total variation does not change when both laws are pushed
forward by the same bijection, and q_t(R' x, R' .) = q_t(x, .)). So tau_t - taubar_t is neutral and orthogonal to
constants, and its norm is at most 1/2 (a variable with values in [0, 1]). Then
<tau_t, Q^t f^2> = taubar_t + <Q^t(tau_t - taubar_t), f^2 - 1> >= taubar_t - (1/2) e^(-t m_+) sqrt(kappa - 1). QED.

**Proof of Lemma F. PROVED.** Write tau = taubar_t and a = 1 - e^(-t m_+), both in [0, 1].
If kappa - 1 >= tau^2, (J) gives 1 - e^(-2 t eps) >= a tau^2 / (1 + tau^2) >= a tau^2 / 2.
If kappa - 1 < tau^2, (T) gives 1 - e^(-2 t eps) >= tau - (1/2)(1 - a) tau >= tau / 2 >= a tau^2 / 2. QED.

**Proof of Corollary F1. PROVED.** At t_* = ceil(1/m_+), a >= 1 - 1/e, so
2 t_* eps >= -log(1 - 0.316 tau^2) >= 0.316 tau^2. If m_+ <= 1 then t_* <= 2 / m_+, so eps >= 0.079 tau^2 m_+
>= tau^2 m_+ / 13. Every chi != 1 has a generator R with chi(R) = -1. QED.

**Lemma T1 (three more facts). PROVED.**

(a) tau_t(x) is non-decreasing in t. Proof: q_{t+1}(x, .) and q_{t+1}(x, R .) are the images of q_t(x, .) and
q_t(x, R .) under the same kernel q (use q(R z, R A) = q(z, A)). Total variation does not increase under a
common kernel.

(b) taubar_t >= 1 - sqrt(S_R(2t)), where S_R(s) is the sum of e^(-s E_i) over the levels that are odd under R.
Proof: with respect to mu x mu the density of q_t(x, dy) is sum_i e^(-t E_i) f_i(x) f_i(y). The difference of
the two densities is 2 sum over odd i. Its L^1 norm is at most its L^2 norm, 2 sqrt(S_R(2t)). So
TV(P_t, (1 x R)_* P_t) <= sqrt(S_R(2t)).

(c) For every measurable A with R A equal to the complement of A,
P_mu(X_0 in A, X_2t in R A) >= taubar_t / 4. Proof: h = 1_A - 1_{R A} is odd and h^2 = 1. By Lemma T,
<h, Q^2t h> = |Q^t h|^2 <= 1 - taubar_t. Also <h, Q^2t h> = 1 - 4 P_mu(X_0 in A, X_2t in R A).

Reading of (b) with (F): (TUN) at time t_* holds when the odd thermal sum at time 2 t_* is below 1, and (TUN)
gives back eps_chi >= tau_0^2 m_+ / 13. So (TUN) is, up to the count of levels, the statement
"eps_chi >= c m_+ for some c > 0". It is a ratio of two gaps. It contains no large number.

**GUIDE (numeric, not a proof).** A pure-Python run on 160 random reversible positive semidefinite Markov chains
with a Z_2 symmetry (10 states, four strengths of the coupling between the two sheets, t = 1, 2, 5, 20; a few
megabytes) found no violation of (J), (T), (T0), (F) or T1(b) in 640 cases. In the weak-tunnelling samples
kappa is 1.0000 to four places. In one such sample at t = 20 the two sides of (F) are 0.176 and 0.0042.

### 5.2 What (TUN) is in the adjoint form

**PROVED.** By (M), one step of the chain has q(x, R dy) / q(x, dy) = C(x, R y) / C(x, y). For t steps the
ratio q_t(x, R dy) / q_t(x, dy) is F^t(x, R y) / F^t(x, y): the slab of t steps with boundary slices x and y,
with one temporal twist seam inserted, divided by the same slab without the seam.

**ARGUED.** By the slab form of Lemma Z, the seam is (up to tiny probability) a function of the adjoint path
inside the slab. (TUN) says: this function is not determined by the two boundary slices. In the words of path
(A): given two fundamental slices a time t_* apart, the relative flat class of the lift across the slab keeps
conditional entropy bounded below on average. This is the precise "Z_2 vortex statement" that the charged
factor needs. It is weaker than u_T close to 1/8.

### 5.3 The attempt to prove (TUN), and the line where it fails

**PROVED (a first-moment bound).** Let Phi be a bijection of slab configurations that fixes the bottom slice,
sends the top slice y to R y, and preserves Haar measure on the interior links for each fixed pair (x, y). Let Delta = S o Phi - S be the change of the Wilson action.
Then q_t(x, R y) / q_t(x, y) = E[e^(-Delta) | x, y] and, by Jensen twice,
taubar_t = E min(1, q_t(x, R y) / q_t(x, y)) >= exp(-E[Delta^+]).

**ARGUED (this bound cannot give (TUN)).** The simplest Phi flips the n^2 temporal plaquettes of one seam:
E[Delta] = 2 beta n^2 E[w_p], the thin vortex. A seam that turns from 1 to -1 through a fixed colour axis over
several time steps is not central in between. On the spatial plaquettes through the seam plane it conjugates one
link by a rotation that is not small. The links of a two-dimensional slice are not close to any fixed axis
beyond areas of order beta. So the cost stays of order beta n^2 per unit of time spent off the centre. Every
first-moment bound of this kind is of the size e^(-c beta n^2). That is the frozen-group size. For SU(2) the
true overlap is of order one because of fluctuations (the twisted free energy at fixed lattice is
(3/2) log beta + log log beta, rows 1143-1144, not of order beta). A first-moment bound cannot see this.

**The failing line.** The step "Jensen on an insertion map" fails. What is needed is the second-moment
(entropy) form: a lower bound on E[e^(-Delta) | x, y] itself at the physical scale. That is a bound on a
renormalized twist free energy, in other words an upper bound on the stiffness at scale L. It is the kind of
statement that the first-passage data of the account are about (K-flow). I did not read the account for a
twisted or two-slice statement, so this stays OPEN. I do not claim that the account contains it.

### 5.4 Where the path stands

- PROVED: Lemma S, Lemma J, Lemma T, Lemma F, Corollary F1, Lemma T1, the identity (M). They are class-wide:
  they hold for every reversible positive Markov chain with a Z_2 symmetry. They are not selective. They move
  the selective content.
- PROVED given the unchecked row 1155 (29): Lemma Z.
- OPEN: (TUN). It fails for frozen groups, as it must. The first attempt (a first-moment insertion bound) fails
  at the Jensen step.
- OPEN: the neutral gap z_+ unbounded with D^+ bounded. This is the target on the neutral sector of the adjoint
  law (35). Lemma J shows why no sector argument can reach it: Jensen bounds the gap of a "square" sector from
  above, and the neutral sector is the square of every sector. I found no selective inequality for it.

One sentence for the lead: under (TUN), the council's GUIDE statement "the zero-flux half is the binding one"
(row 1130, 2c of the synthesis) becomes the proved inequality z^- >= (tau_*^2 / 13) z_+.

## Step 6. Comparison with the registry (opened only now)

Read for this step: `parts/gap.md` in full where it lists routes (State of attack, methods 19-36, lead rules,
the route registry, the test table, the exact price); `library/gap-crux-exercise2-max.md` 6a (methods 1-18);
the RESULT lines of rows 731, 783, 876, 886, 889, 892, 894, 930, 931 and 1025; `library/gap-wall-max.md`
(statement list and Step 6a, Attack B). Grep over `library/`, `parts/` and FINISH.md for: kurtosis, torelon,
Doob, ground-state transform, tunnel, flux pair, pair bound, total variation with flip or flux, Bayes, Simon,
Durhuus, Luscher, toron, Cwikel, Weyl.

### 6.1 Path (A): already tried, part by part

| Piece of Steps 3-5 | On file as | Mark |
|---|---|---|
| Lemma S (split of the strict test) | Lemma SPLIT and Corollary O1, row 892 (S_ev and Q_0 on one box) | found again |
| Lemma Z (the Z_2 part is frozen) | method 14, "thin Z_2 lift with Griffiths inequalities: frozen at order one" | found again; Lemma Z is its proved form from row 1155 (29) |
| The table of 3.4 | the test table of `parts/gap.md` (row 998 6c, corrected in 8.5 after check 884): frozen Z_2 fails T_per only; frozen Q_8 and 2T fail T_ev too | found again; it agrees |
| Lemma J (pair bound) | Lemma SQ and Theorem SQ, row 876; Theorem 4.1 of row 886 (HOLDS in check 889) | found again, same inequality |
| "f^2 almost constant means a sign bit" | the hidden-bit reading, row 886 Theorem 4.5; (HB); (WALL)_40, rows 892 and 894 | found again |
| Lemma T, Lemma F, Corollary F1, Lemma T1 | no statement with a total-variation overlap of the two-slice law was found by the grep above | VARIANT of the (KURT)/(HB)/(WALL) line; new as a statement |
| Step 5.3 (first-moment insertion bound fails) | method 17, "thick vortex by field-independent spreading"; row 894 Attack B, items B1-B2 and its stop | found again, same stop |
| (TUN) needs a renormalized vortex weight | (S1)/(VF) of row 892; "a lower bound on a non-perturbative vortex weight", row 894 | found again |
| The neutral factor | route RE, (EV-STEP), row 731; "the glue half is supplied by no flux node", row 892 | unchanged |

What the variant adds to the file (ARGUED, from the RESULT lines of rows 876-894, whose files I read only in
part):

- Rows 876-894 remove the flux half given a regularity statement on the flux ground function: (KURT)
  (kappa >= 1 + c_0, later kappa >= 2 or 1.66) or (WALL)_40. Lemma F needs no fourth moment. Its hypothesis is
  an overlap of the vacuum two-slice law with its flipped copy, bounded below by any positive constant.
- Relation to row 892's (CORE), as its RESULT line states it (Z^v / Z^0 >= 9/10 at time a). Write E_R(a) for
  the sum of e^(-a E_i) over the R-even levels, vacuum included. (CORE) gives S_R(a) <= E_R(a) / 19, and T1(b)
  gives taubar_{a/2} >= 1 - sqrt(E_R(a) / 19). Lemma F at t = a/2 then gives a flux gap of order 1/a only.
  (TUN) asks for the overlap at the shorter time t_*, the even relaxation time. In exchange any positive
  constant is enough, and the flux gap comes out as a fixed fraction of the neutral gap. Neither input implies
  the other in general.
- Lemma T covers the near-bit case that rows 886-894 leave: if kappa - 1 < taubar_t^2, then
  1 - e^(-2 t eps) >= taubar_t (2 - e^(-t m_+)) / 2. At t = t_* this is at least 0.81 taubar, so
  a eps >= 0.2 taubar a m_+ for a time extent a (with m_+ <= 1). So the
  near-bit of row 894 (flux weight at least 1/20 at time a, that is a eps <= 3.0) needs
  taubar_{t_*} < 15 / (a m_+). This does not prove that the overlap is positive.
- Method 13 set aside "flux half from glue half by clustering". Lemma F does not revive it: it has the extra
  hypothesis (TUN), and (TUN) is where the conserved-charge obstruction sits.

So path (A) is the lane's route RE together with the flux line of rows 876-894. It stops where they stop.

### 6.2 Path (B)

The words Cwikel, Lieb-Rozenblum and Weyl bound occur in no row before 1158. A state-count bound was named
once: (M5-H) of row 738, read in row 747. So a counting bound is new as a named tool. By Step 3.2 its X = 0 form
is not selective and its X > 0 form is the target. Not attempted. Mark: new as a tool, ARGUED not selective.

### 6.3 Path (C)

Method 36 (rows 1139, 1140) is the same object one dimension lower: the frameless layer, a 2D O(4) model in a
two-sided SO(4) background, the layer of a 3D gauge field. Background-uniform mixing fails at large b, and a
proof must average over the actual Wilson backgrounds. Durhuus and Frohlich are cited in 38 lane files; route
BR-2 and (T-pin) (row 1018) are the layer and pinned lines. The 3D seam of rows 1149 (22) and 1151 (1) in the
actual backgrounds has no proof row. Not attempted here. Mark: variant of method 36 and BR-2.

### 6.4 One remark that the grep did not find

**PROVED (entropy form of the strict test).** Let U = F / |F|, g(s) = log Tr U^s, rho_s = U^s / Tr U^s and
S(s) = g(s) - s g'(s), the von Neumann entropy of rho_s. Then (g(s)/s)' = -S(s)/s^2, so

    J_T = 2 g(T) - g(2T) = 2T * integral from T to 2T of S(s) ds / s^2,    and    S(2T) <= J_T <= S(T),

because S is non-increasing (S' = -s g'' <= 0). So the strict test is squeezed between the thermal entropies of
the box at periods T and 2T. This is a restatement, not a route. (Grep: "von Neumann entropy" and "thermal
entropy" have no hit in the solve files, `gap-crux-restate.md`, `gap-phys-seed.md` or `parts/gap.md`.)

### 6.5 Verdict

- None of (A), (B), (C) is a new mechanism. (A) is on file almost line by line. I did not find a path better
  than the three.
- New statements of this row: Lemma T, Lemma F, Corollary F1, Lemma T1 (class-wide, PROVED here, checked by no
  one), the identity (M) in this form, and the entropy sandwich of 6.4.
- No selective inequality was obtained. The reopen conditions of RA, RE, RF, RC and RG are not met by anything
  here.
- If a later row works on the flux half again, (TUN) is the form to use: it is a coupling statement about two
  slices, it needs no eigenfunction, and any positive constant is enough (ARGUED).

Not done: the files of rows 876, 886 and 892 were read only through their RESULT lines and the quotations in
`gap-wall-max.md`; the account was not read for a twisted or two-slice statement; rows 1156 and 1157 had no
RESULT line when this file was written; Lemma Z rests on the unchecked row 1155 (29).

RESULT: Row 1158 (Claude Fable 5.2 high, laptop subagent; checked by no one; one pure-Python guide run of a few megabytes, no numeric step in a proof). Path chosen: (A), the adjoint two-factor form, because it alone puts the massless failure and the ordered-centre failure in different factors; (B) is argued non-selective (its bounded-total half holds for the photon gas, its other half is the gap) and (C) starts as a neutral two-point function across the period. First lemma, PROVED by hand: Lemma F, for every beta, n, t and every flux sector, 1 - e^(-2 t eps_chi) >= (1/2) taubar_t^2 (1 - e^(-t m_+)), where taubar_t is the overlap of the vacuum two-slice law with its flat-flipped copy; hence z^- >= (tau_*^2 / 13) z_+, so (W) follows from (BDD-Delta), a neutral gap z_+ > 13 (256 D_0 + 30) / tau_0^2 and the overlap bound (TUN). Also PROVED: the split Lemma S, the pair bound Lemma J, the pointwise bound (T0), Lemma T1 (monotonicity in t; (TUN) follows from an odd thermal sum below 1; every antisymmetric set is crossed with probability at least taubar/4), the vacuum-chain identity Q f = C(phi f)/C(phi), and the entropy sandwich S(2T) <= J_T <= S(T). Comparison: the path is ALREADY TRIED: Lemma S is Lemma SPLIT of row 892, Lemma J is Lemma SQ of row 876, the frozen Z_2 part is method 14, the insertion attempt is method 17 and Attack B of row 894, and the neutral factor is route RE at (EV-STEP); Lemma F with (TUN) is a new variant of the (KURT)/(WALL) line with no fourth moment and no number. Where it stands: (TUN) is OPEN and fails at the Jensen step of any first-moment vortex insertion (it needs a renormalized vortex weight, the stop (S1)/(VF) of rows 892 and 894); the neutral gap is OPEN and untouched; no selective inequality was obtained and (W) is unchanged.
