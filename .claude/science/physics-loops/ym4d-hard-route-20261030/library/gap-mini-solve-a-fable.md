lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:59Z

# gap-mini-solve-a-fable (queue row 1188): the mass gap of 4D SU(2) Yang-Mills, attack on the crux

Pinned at commit f7e5907e5 of `claude/ym4d-hard-route`. Worker: Claude Fable 5.2 (max), Mac mini worker 1.
Started 2026-11-19T22:59Z (`date -u`). Research-stage working state; nothing here grants status.

Labels: PROVED (every step written here, not yet checked by another model), ARGUED (argument with a named
gap), GUIDE (numeric or heuristic, never a proof step), OPEN.

## 0. Status log (one line per step, newest last)

- 22:59Z file created; reading FINISH.md rule sections, GOAL.md, `parts/gap.md` and the latest RESULT lines.
- (time typed by hand, not from `date -u`; the true time was about 23:03Z) read FINISH rule sections (L52-73, L299-350), GOAL.md, `parts/gap.md` L1-104, `library/gap-council-synthesis.md`, the RESULT lines of rows 1178-1187. Next: RESULT lines of rows 1135-1177, then the attack plan (Section 1).
- 23:28Z (`date -u`) read: RESULT lines of rows 1135-1177; `prior/gap-2don-proofs-read-opus.md` L44-170 (the two posted 2D proofs); `gap-crux-restate.md` L20-60; `gap-solve9-astra62.md` L95-150 (the neutral bound and its consumer). Section 1 written below. No attack chosen yet.
- 23:39Z (`date -u`) Section 2 written: the pinned-slice Ward route worked to its first failing step; Lemma PC proved (exact power count for every family). Anchors confirmed by grep: row 712 layer model `gap-crux-fp.md` L369-384; row 1011 Proposition W `gap-pinned-cell-gauge-max.md` L184; row 1016 `gap-global-reform-max.md` L441, L940.
- 23:42Z (`date -u`) numeric sanity run done under the numeric lock (holder solve-a-fable-1188, acquired 23:41Z, released after about 2 s; memory free 50 percent at the start). Section 3 written. One slip corrected in 2.3 (the trivial bound is (beta/4) eta^2 N for one face).

## 1. How best to attack it (analysis before any attack)

### 1.1 The target as the lane holds it (cited, not re-proved)

- The lane reduces the Jaffe-Witten gap clause to one lattice estimate plus the continuum datum. The lattice
  estimate is the one-cube physical neutral bound (N-phys): on the periodic spatial cube n_j^3 of one admissible
  physical side, the vacuum-normalized neutral excited trace s_j(floor(n_j/K); n_j) is at most 1/2, uniformly in the
  cutoff j (`gap-solve9-astra62.md`, "One finite aspect" and "consumer", L146-148; row 1161, checked in row 1162).
  The consumer is Theorem BP of row 1179 (`gap-mini-branch-fable.md`), which HOLDS AFTER CORRECTION in the
  cross-provider check 1183 (`gap-neutral-chain-check-astra.md`).
- The continuum datum ((P1)-(P4), (H2), (TOT) on the intended Hilbert space) is the T0 chain. FINISH "Where it
  stands" records: existence is not proved. I do not touch it in this row.
- The Wilson branch selection (BS) is on the path of (W) (confinement on tori), not of the gap clause (row 1179).
- (N-phys) is the glue half (GLUE-FP) of rows 895 and 920 with other constants (row 1184). In one sentence: a gap
  and a level count for centre-neutral states at one physical box, at arbitrarily weak bare coupling.
- The fixed-coupling form: the seed Phi(n) = 16 F(n^4) - F((2n)^4) <= 1.9e-4 at some n (`gap-crux-restate.md`
  L57-60, Theorems D and S). GUIDE (my arithmetic from Teper's table quoted in my memory of row 974: a m = 1.216,
  a^2 sigma = 0.136 at beta 2.3): the flux term 6 n^2 exp(-sigma n^2) passes 1e-5 at n = 12 and the glue term
  n^3 exp(-m n) at n about 18. So the seed at beta 2.3 is a statement about log Z on 18^4 and 36^4 to an absolute
  accuracy of 1e-4. No convergent expansion with absolute weights reaches beta 2.3 (method 35).

### 1.2 What a proof has to contain

ARGUED (nothing here is new; each line names its place on file).

1. The band has no small parameter. Between the last scale where the effective coupling is small and the first
   scale where the seed holds, no expansion converges, and the owner rule excludes a computed finite-box criterion.
   So the crossing must be a structural inequality that holds at every coupling. (`parts/gap.md` L41-50.)
2. Symmetry does not force disorder in four dimensions. A continuous one-form symmetry can break in d = 4 (the
   Coulomb phase of compact U(1)), and SU(2) has only the Z_2 centre as a one-form symmetry. So there is no
   Mermin-Wagner argument; the gap is dynamical. The comparison cases of lead rule W2 say the same.
3. The only band-crossing mechanism on record is the pair of posted 2D O(N) proofs (rows 1006-1011). My reading of
   the OpenAI skeleton (from `prior/gap-2don-proofs-read-opus.md` B(2), not from the paper): the twist between two
   pinned layers is produced by commutators of single-axis spin waves at each of log N scales. The amplitudes add,
   lambda about log N. The costs add as squares of Dirichlet energies, also about log N, by orthogonality. So the
   stiffness is at most K/log N. Two facts make it work: (a) a response functional W with exact invariance under a
   non-abelian group of changes of variables; (b) Ward bounds for that group whose cost form is scale invariant.
4. In 4D gauge theory (a) exists and (b) fails. The exact analogue of W is the Schrodinger functional as a function
   of a pinned boundary field C. It is invariant under the gauge group of the boundary slice, by Haar invariance of
   the time-like links that leave the slice. Its Ward bound is the exact contact identity for smeared Gauss-law
   generators, <X(df a)^2> = <Y> <= beta |df|_2^2. But the gauge functions live on a 3D slice and their Dirichlet
   energy is not scale invariant. Count for a holonomy twist h of size 1/N per link: with plane waves of weight c_p,
   lambda/N = sum c_p^2 k_p and cost = sum c_p^4 k_p^4 N^6, so by Cauchy-Schwarz lambda^2/cost <= N^(-4) sum_k
   k^(-2), which is about 1/N. The fourth-order inequality then gives a bound of order K N, the order of the bound
   with no commutator. This is the lane's slot (ii) and R6 of row 1013 (`gap-invent-selective-max.md` L83, L91) and
   row 1016 (`gap-global-reform-max.md` L359, L429, L545): "scale invariant in two dimensions and not in four".
   My count is a second derivation by the same model family, not a check.
5. The scale-invariant cost form in 4D is the covariant curl form of a one-form. For a move in a fixed colour
   direction it turns into a mass form, because every adjoint direction is rough at the lattice scale (row 1141 (2);
   row 1181 Lemma 5.1a; Proposition J). The exact stiffness is R = <Hess S(a,a)> - Var X(a) for any extension a of
   the boundary twist. Both terms are of order N^2 in lattice units and their difference is of order beta_eff. A
   Jensen bound drops the variance, so it can never see the cancellation (rows 1011, 1016).
6. The other continuous twists in reach are spacetime twists (shifted or rotated identifications). Their Ward
   bounds are stress-tensor contact terms with power divergences. Discrete twists (shifts, the cubic group, the
   centre) isolate every sector except the vacuum sector, and (N-phys) is the statement about the vacuum sector.
7. Thin twisted compactification (Route T, row 842, (AC')), ground-state curvature (rows 957, 968), abelian
   conditional structures (below) and the dichotomy with an emergent massless vector (row 1017, Theorem CR) are on
   file with their first failing steps.

One small item I did not find on file (grep "Hopf", "Ginibre", "abelian projection" in `library/`; hits are about
frames, U(1) and the O(N) proofs). PROVED by direct expansion, unchecked, and negative:

**Lemma HF (the maximal-torus amplitude decomposition is frustrated).** Write a link as U = [[a, b], [-b*, a*]]
with a = cos(phi) e^(i alpha), b = sin(phi) e^(i gamma), phi in [0, pi/2]. For a plaquette U_1 U_2 U_3^* U_4^*,

(1/2) tr = c1 c2 c3 c4 cos(m_0) - s1 s2 c3 c4 cos(m_12) + s1 c2 s3 c4 cos(m_13) + s1 c2 c3 s4 cos(m_14)
 + c1 s2 s3 c4 cos(m_23) + c1 s2 c3 s4 cos(m_24) - c1 c2 s3 s4 cos(m_34) + s1 s2 s3 s4 cos(m_1234),

with c_i = cos(phi_i), s_i = sin(phi_i) and the angle forms m_0 = alpha_1 + alpha_2 - alpha_3 - alpha_4,
m_12 = gamma_1 - gamma_2 - alpha_3 - alpha_4, m_13 = gamma_1 - alpha_2 - gamma_3 - alpha_4,
m_14 = gamma_1 - alpha_2 + alpha_3 - gamma_4, m_23 = alpha_1 + gamma_2 - gamma_3 - alpha_4,
m_24 = alpha_1 + gamma_2 + alpha_3 - gamma_4, m_34 = alpha_1 + alpha_2 + gamma_3 - gamma_4,
m_1234 = gamma_1 - gamma_2 + gamma_3 - gamma_4. Since m_12 = m_0 + m_13 - m_23 as linear forms, and the
coefficients of cos(m_0), cos(m_13), cos(m_23) are non-negative while that of cos(m_12) is non-positive, no shift
of the angles (alpha_l -> alpha_l + eta_l, gamma_l -> gamma_l + delta_l) makes all eight coefficients non-negative
on one plaquette. So, given the amplitudes phi, the abelian model in the angles is not of Ginibre type in any
shifted angle variables, already on a single plaquette.

Proof. The eight terms are the eight even flip patterns of the index path 1 -> . -> . -> . -> 1 through the four
matrices, with entries (U)_11 = a, (U)_12 = b, (U)_21 = -b*, (U)_22 = a* and (U^*)_11 = a*, (U^*)_12 = -b,
(U^*)_21 = b*, (U^*)_22 = a; the path that starts at index 2 gives the complex conjugate. The two minus signs come
from b_1 (-b_2^*) and (-b_3) b_4^*. A shift changes the argument of each cosine by a constant; all coefficients
become non-negative only if the shift is 0 mod 2 pi on m_0, m_13, m_23 and pi on m_12, which contradicts
m_12 = m_0 + m_13 - m_23. QED.

Use: it closes the "amplitude decomposition with abelian conditional systems and association" cell of the reading
table (`prior/gap-2don-proofs-read-opus.md` B(5), marked NONE there) for the Hopf coordinates. It does not exclude
other coordinates. It is consistent with method 35 (the signs are in the model, not in the expansion).

### 1.3 Decision

Every structural route I can name is on the lane's map with a first failing step. I therefore do not open a new
framing. The next sections take one open point and work it to a proof or to a first failing step. The choice and
its reason are in Section 2.

## 2. Attack 1: the pinned-slice Ward route (the gauge form of the 2D commutator mechanism)

Reason for the choice. Of the routes in 1.2 this is the only one with a mechanism that is selective by
construction (the gain is a Lie bracket) and that has crossed a band in some model. The lane holds its failure in
four dimensions as an ARGUED dimension count (row 1013 R6; row 1016, `gap-global-reform-max.md` L441, L940). I work
it once in full, to turn the count into a statement that holds for every family of moves, and to see whether the
transfer kernel (two independent faces of a slice) changes the count. It does not. Result: Lemma PC below, PROVED,
and the obstruction 2.4, ARGUED.

### 2.1 Setting (standard; credit Luscher, Osterwalder and Seiler through row 667)

Lattice Z_N^(d-1) x Z_T with T >= 2, Wilson SU(2), coupling beta. The slice is t = 0, of dimension d_s = d - 1. Its
links l = (x -> y) are pinned to a field C. V^+_x is the time-like link from (x, 0) to (x, 1), V^-_x the one from
(x, -1) to (x, 0); U^(1)_l and U^(-1)_l are the links above and below l. The two time-like plaquettes through l are

(1/2) tr(C_l M^+_l), M^+_l = V^+_y U^(1)*_l V^+*_x, and (1/2) tr(C_l M^-_l), M^-_l = V^-*_y U^(-1)*_l V^-_x.

(The second uses tr g = tr g^(-1) in SU(2).) Let the upper face read a field C^+ and the lower face a field C^-:

Z_2[C^+, C^-] = integral over all unpinned links of exp( beta sum_l (1/2) tr(C^+_l M^+_l)
 + beta sum_l (1/2) tr(C^-_l M^-_l) + beta (all other plaquettes) ).

Then Z[slice = C] = exp(beta sum of slice plaquettes of C) Z_2[C, C], and Z_2 is the T-step transfer kernel between
two slice fields without their magnetic weights. Its one-step case is the layer model of row 712
(`gap-crux-fp.md` L371).

**P1 (PROVED; standard).** For all site functions g, g' on the slice, Z_2[g.C^+, g'.C^-] = Z_2[C^+, C^-], where
(g.C)_l = g_x C_l g_y^(-1). Proof: V^+_x -> g_x^(-1) V^+_x is Haar preserving, touches only the upper plaquettes of
the slice, and maps M^+_l to g_y^(-1) M^+_l g_x; then tr(C^+_l g_y^(-1) M^+_l g_x) = tr((g.C^+)_l M^+_l). The lower
face is the same with V^-_x -> V^-_x g'_x. T >= 2 makes V^+ and V^- distinct variables. QED.

So the temporal twist through a slice direction is one argument moved: for a flat field C_eta with holonomy
exp(eta c) around the 1-cycle, C_eta times the seam flip is C_(eta + pi), and Z_tw[slice = C_eta]/Z[slice = C_eta]
= Z_2[C_(eta + pi), C_eta] / Z_2[C_eta, C_eta]. A response bound in the upper argument alone would bound it.

**P2 (PROVED; the Gauss contact identity; relative on file: Proposition W of row 1011).** Fix C^- and put C^+ = 1.
Let <.> be the normalized measure of Z_2[1, C^-]. For a real site function f and a unit a in su(2) (a = i a.sigma/2
in angle units), X(df a) := beta sum_l (df_l / 2) (1/2) tr(i a.sigma M^+_l). Then <X(df a)> = 0 and

<X(df a)^2> = (beta/4) sum_l (df_l)^2 <(1/2) tr M^+_l> <= (beta/4) |df|_2^2.

Proof: by P1 with g_x = exp(t f_x a), Z_2[exp(-t df a), C^-] = Z_2[1, C^-] for all t, because one generator
commutes with itself. The second derivative at t = 0 is <X^2> - <Y> with Y = beta sum_l (df_l/2)^2 (1/2) tr M^+_l.
QED. It is an identity, with a local right side: the Gauss-law generators of a slice have contact correlations.

### 2.2 The mechanism, and what it would give (ARGUED: the port of the fourth-order inequality is not written)

With F = sum_i (Re f_i a + Im f_i b), P1 gives Z_2[exp(-dF), .] = Z_2[exp(B(F)), .] with
B_l = (1/2)[F_x, F_y] + O(F^3), a field along c with profile S(f, g)_l = (f_x g_y - g_x f_y)/2. The OpenAI inequality
(their Proposition 2.2, as restated in `prior/gap-2don-proofs-read-opus.md` B(2) item 4; I have not read the paper)
bounds the stiffness on Q = sum_i S(f_i, f_i-bar) by K(beta) ||T||_HS^2 plus a second term, where
T = sum_i df_i (x) df_i-bar. Its proof uses only: P1, the bounds of P2, and the algebra of the bracket. All three
hold here, with the pair (s_x, s_y) replaced by the staple M^+_l. So I expect the inequality to hold for
R(Q, Q-bar) := -D^2 Z_2[exp(. c), C^-]/Z_2 at a flat upper field, for every lower field and every T >= 2. I did
not write that port. Nothing below depends on it being true: Lemma PC bounds what it could give.

### 2.3 Lemma PC (PROVED): the exact power count, for every family

Let the slice be the torus Z_N^(d_s), h the constant one-form eta/N on the links of direction 1, and (f_i) any
finite family of complex site functions with

sum_i Im( f_i(x) f_i-bar(y) ) = -lambda h_l + (d phi)_l for all links l = (x -> y), (PC1)

for some real lambda and real phi (this is sum_i S(f_i, f_i-bar) = -i lambda h up to a gradient, the hypothesis of
the mechanism). Let cost := ||T||_HS^2 = sum_(i,j) |<df_i, df_j>|^2. Then

lambda^2 eta^2 N^(2 d_s - 2) <= cost x G(N), G(N) := sum over k != 0 of sin^2(k_1) / D(k)^2, (PC2)

where k runs over the dual torus and D(k) = sum_mu 4 sin^2(k_mu / 2). Moreover G(N) <= sum_(k != 0) 1/D(k), which
is at most N^3 for d_s = 3 and N >= 4. Hence for d_s = 3:

cost >= lambda^2 eta^2 N. (PC3)

Proof. Pair (PC1) with h. The gradient drops out, because sum_l h_l (d phi)_l = (eta/N) sum_x (phi(x + e_1) -
phi(x)) = 0. So | sum_i sum_x Im(f_i(x) f_i-bar(x + e_1)) | = lambda eta N^(d_s - 1). In Fourier variables,
sum_x f(x) f-bar(x + e_1) = sum_k |f^(k)|^2 exp(-i k_1), so the left side is |tr(rho s)| with rho = sum_i
|f_i><f_i| >= 0 and s the multiplier sin(k_1). The cost is sum_(i,j) |<f_i, Delta f_j>|^2 = tr(rho Delta rho Delta)
= || Delta^(1/2) rho Delta^(1/2) ||_HS^2 with Delta = d*d, the multiplier D(k). s vanishes at k = 0 and commutes
with Delta, so tr(rho s) = tr( Delta^(1/2) rho Delta^(1/2) . Delta^(-1/2) s Delta^(-1/2) ) on the complement of the
constants. Cauchy-Schwarz for the Hilbert-Schmidt pairing gives (PC2). For the bound on G: sin^2 k_1 = 4
sin^2(k_1/2) cos^2(k_1/2) <= D(k). For d_s = 3: 4 sin^2(k/2) >= (4/pi^2) k^2 on [-pi, pi], so with k = 2 pi n/N,
1/D(k) <= N^2/(16 |n|^2); the shell |n|_inf = m has 24 m^2 + 2 points with |n|^2 >= m^2, so the sum over
1 <= m <= N/2 is at most (N^2/16)(12 N + 4) <= N^3 for N >= 4. QED.

Reading. Any inequality of the form R(Q, Q-bar) <= K x cost, used with Q = lambda h, gives R(h, h) <= K cost /
lambda^2, and by (PC3) this is at least K eta^2 N on a three-dimensional slice, whatever the family. The bound with
no commutator is R(h, h) <= <Y> <= (beta/4) |h|_2^2 = (beta/4) eta^2 N (one face). So on the slice of a four-dimensional lattice
the mechanism returns the order of the trivial bound and no logarithm. For d_s = 2 the same (PC2) allows cost of
order lambda^2 eta^2 / log N, which is what the 2D proof attains. This makes the lane's count a statement about
all families, not about plane waves with one weight. It also covers the two-face kernel, since P1 and P2 are
statements about one face.

### 2.4 Why the count is the truth for this route (ARGUED)

The route reads only P1 and P2, so any bound it proves holds for every T >= 2 and every lower field, in particular
for the kernel between two flat slices one step apart. By row 712 that kernel is the three-dimensional principal
chiral (O(4)) model at coupling beta, with the holonomy as a twisted boundary condition. That model has long-range
order at large beta (Frohlich, Simon and Spencer, RECALLED), and the response of an ordered model to a twist is of
order beta N (the helicity modulus; RECALLED, not proved here). So for one member of the class the order N is
attained, and no argument that reads one slice can do better. In three dimensions the slice is two-dimensional and
its one-step kernel is the 2D chiral model, which never orders: there the route would give Z_2[C_(eta + pi), C^-]
/ Z_2[C_eta, C^-] >= 1 - C_beta/log N at a flat upper field for every lower field (ARGUED, given the port in 2.2).
Row 1139 shows that with both faces rough the 2D statement fails at large b; one flat face is the case left.

**What four dimensions needs, in this language.** Disorder of the holonomy appears only across about N time steps
(springs in series: the stiffness beta N of one step becomes beta N / T). So the gain must come from composing
kernels, and the middle slices of a composition are rough, not flat. Around a rough slice C the gauge directions are the covariant gradients d_C F (F_x - Ad(C_l) F_y on the link l),
so a bound of the kind of P2 can only have |d_C F|_2^2 on its right side, and row 1141 (2) shows that d_C of every adjoint section has
energy of order one per site. This is the same wall as rows 1011, 1013, 1016 and 1141, reached from the transfer
kernel. First failing step of Attack 1: there is no family of slice gauge functions with scale-invariant cost in
d_s = 3 (Lemma PC), and no flat middle slice.

## 3. Sanity run (GUIDE; not a proof step)

Script and log are in a scratch folder under /tmp (`solve-a-fable-1188/check_hf_pc.py`, `check_hf_pc.log`), plain
numpy, 34 MB, about 2 s. A run can only refute a formula; it proves nothing.

| Check | Outcome |
|---|---|
| Lemma HF: the eight-term formula against the direct matrix product, 2000 random plaquettes | largest difference 1.4e-15 |
| Lemma PC: G(N)/N^3 on the 3D torus, N = 4, 8, 16, 32 | 0.023, 0.034, 0.038, 0.041 (the proof needs at most 1) |
| sum over k != 0 of 1/D(k), divided by N^3, same N | 0.198, 0.225, 0.239, 0.246 (the proof needs at most 1) |
| G(N)/(N^2 log N) on the 2D torus, same N | 0.036, 0.051, 0.058, 0.062 (it grows like log N, as the 2D mechanism needs) |
| (PC3) on three plane-wave families at N = 16: cost/(lambda^2 eta^2 N) | 52.2 (weights sin k_1 / D^2 on sin k_1 > 0), 62.2 (weights D^(-2)), 227.9 (flat); Lemma PC needs at least 1 |

The first family is the extremal one for families of plane waves with positive weights. Its value 52.2 equals
2 N^3/G(N). So the true constant in (PC3) is near 50, not 1: positivity of rho costs the factor 2 that
Cauchy-Schwarz does not see, and G/N^3 is about 0.04.
