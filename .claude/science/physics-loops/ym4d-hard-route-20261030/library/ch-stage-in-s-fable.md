lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-24T09:44Z

# CH stage spaces inside the chart class S (row 1448, `ch-stage-in-s-fable`)

Provenance: Claude Fable 5.2, medium effort, Mac mini worker, pinned at b47e86bbb. Author only, one reading,
unchecked. Sources credited: T. Balaban (CMP 99b, 109, 116 via quotation, 119, 122a, 122b), the Sussman-Alpoge
complete account (with Claude and Codex), and this lane's rows 1444 (`cm-o3-fable.md`) and `ch-r2.md`.

## 0. Plan and statement (written 2026-11-23T21:44Z, before any reading of the sources)

Statement to decide (row 1448): for every admitted history and every piece of the old-terms step, the stage
spaces U~^c_k(Y_4, a~_0, a~_1) of CMP 122a (1.64)-(1.69), and the reached link backgrounds of the three links of
CMP 122b (1.61)-(1.63), lie in the chart class S of 4.5:thm-chart-existence (CA-I 12945-13017), with radii fixed
before M and the M-reading ceiling falling on alpha_0 only. Either prove it, or exhibit a stage-space clause on
Omega''_{k_0+1} minus Omega_{k_0+1} whose constant exceeds a_0^S for every admitted alpha_0.

Plan, one step per response, each appended here before the next:
1. Read the inputs named by the row (cm-o3-fable, ch-r2 with (P4'), prior/ch, CH rows of open-registry and
   open-core). Record what is already on file.
2. Print the chart class S (CA-I 12945-13017) and its order of choice (a_0^S, alpha_0, M).
3. Print the stage spaces, CMP 122a (1.64)-(1.69), and the account's version; list every clause with its constant.
4. Print the three links, CMP 122b (1.61)-(1.63), and the reached backgrounds.
5. Clause-by-clause comparison: stage clause constant against the class constant, in the account's order of choice.
6. Verdict, labels (proved / sketched / guessed), next two rows.

Status log (times from date -u):
- 2026-11-23T21:44Z file created.

## 1. What is on file (step 1, written 2026-11-23T21:46Z)

Read: FINISH rows 1444, 1447, 1448 and the rule sections; `cm-o3-fable.md` (whole); `ch-r2.md` (whole);
`prior/ch.md` (stage-entry table L68-87 and hits for "stage"); registry rows CH (L17), CH4-AUX (L23);
`open-core.md` L551. Account: CA-I 12936-13085 (class S and its inclusion proof), 49497-49700
(`4.14:rem-supply-scope` with proof). CA-I and CA-II are the copies fetched for row 1444 at the pinned upstream
commit, in my scratch folder /tmp/cm-o3-fable-sa.

1.1 **The class S (CA-I 12936-12971).** Radii a_0, a_1, a_gamma "depending on d and L only". (S1) U = e^{i eta a} U_r,
U_r G-valued, and for every level j and every cube of side 12 M-frak in level-j units a G-valued gauge u with
U_r^u = e^{i eta A}, l_j |A| < a_0, l_j^2 |grad A| < a_0. (S2) N_{U_r}(a) < a_1. (S3) |J|_{(-3)} < a_gamma. No
relation between J and U, no condition (iv), no auxiliary configuration U_{p,X}, J_{p,X}.
So of the seven stage entries (CA-I 49597-49600) the class reads at most: the gauge clause of the real factor
(S1), the twist entries 6-7 (S2), the current entry 3 (S3). Entries 1, 2, 4, 5 are not read by S. This is
`ch-r2.md` Proposition F (L109-122) applied to the class.

1.2 **The account's own inclusion (CA-I 13000-13085) is for CMP 109 (i)-(iii) on X, one scale.** Ceilings
c_12 L M B^109 alpha_0 <= a_0, alpha_1 <= a_1, gamma_0 <= a_gamma; floors 17 M_1 <= L M, 17 M_1 <= c_12 L M,
c_12 L >= 2. Its proof puts every cube of side <= 17 M_1 l_j in one cube of side c_12 L M of CMP 109 (1.12) and uses
l_j <= 1. It does not treat the layered conditions of CMP 119 (2.34)-(2.39) or the stage spaces of CMP 122a.

1.3 **The tool already in the account: the powers of L_0 are paid by R_n (CA-I 49543-49700,
`4.14:rem-supply-scope` (v), written for the operator theorem 4.14, not for S).** The stage bound is
(coefficient <= 1) x L_0^{2e} x (bracket of seven entries with alpha_{0,n} or alpha_{1,n}), with e = max(0, m - k_0),
n = m in (1.64); e = j - m, n = j in (1.66); e = 0 in (1.68). Always 0 <= e <= n - k_0 <= N_0 (4.14:eq-supply-scope-1)
and L_0^{2e} <= c_1 R_n, c_1 = 1 + c(beta_0) L (L+1) (4.14:eq-supply-scope-2, from lem-integer-power-bound /
lem-top-power-bound). The account concludes: the gauge constant supplied on a cube in layer n is at most
c_1 R_n alpha_{0,n}, the radii are read at c_1 R_n alpha_{.,n}, and these are "one-sided conditions ... on each
layer's own coupling", imposed after L and M. So the candidate obstruction of the row (a constant on
Omega''_{k_0+1} minus Omega_{k_0+1} above a_0^S for every admitted alpha_0) has to beat this: the power is at most
polylogarithmic in g_n and alpha_{0,n} is g_n times a polylogarithm, so the product tends to 0 with the coupling.
What rem-supply-scope does NOT do: (a) the class S of 4.5 (it serves 4.14:eq-real-backgrounds); (b) the match of
levels between the stage layers and the tower of the chart at each link (`ch-r2.md` (P4')); (c) the reached
link backgrounds.

1.4 **Rule 0a matches for the row's statement.** `ch-r2.md` (P4), (P4') L148, L188-198 (level match, open);
`cm-o3-fable.md` 2.4 last paragraph and Section 4 item 2 (this row); `prior/ch.md` L79-87 (stage weight on
every entry); CA-I `4.14:rem-supply-scope` (v). No file found proving stage space inside S.

## 2. The printed clauses (step 2, written 2026-11-23T21:50Z)

Read from page images (PyMuPDF renders of the owner's PDFs): CMP 122a pp. 190-191 (the stage spaces), CMP 119
p. 261 (the layered spaces (2.34)-(2.39)). Read from OCR: CMP 99b p. 396 ((3.35)-(3.38), the cube class), CMP 122a
pp. 178-182, CMP 122b pp. 361-362, 365, 373-375. Account: CA-I 12640-12790 (conventions), 14497-14530 (chart theorem).

2.1 **The stage space (CMP 122a p. 190-191), for a stage with j = h + n > k_0.** Pairs (U-bold, J-bold) defined on X,
U-bold = U'U, U G-valued, U' = exp(i eta A'). Write l_m = L^m eta and
kappa = 1 - beta sum_{i=h+1..j} 2^{-|m-i|} - beta sum_{q=m+1..k} 2^{-(q-m)} <= 1.
- (i), on (Omega''_m minus Omega''_{m+1}) cap X for m = 1..j-1, and on (Omega''_j minus Omega_{k_0+1}) cap X for m = j:
  the seven entries are below kappa L_0^{2 max(0, m-k_0)} times
  [a_{0,m} eta^2 l_m^{-2}, (aux.), a_{0,m} l_m^{-3}, (aux.), a_{0,m} eta^2 l_m^{-2}, a_{1,m} l_m^{-1}, a_{1,m} l_m^{-2}].
  Gauge clause (1.65): l_m |A|, l_m^2 |grad A| < L_0^{2 max(0, m-k_0)} B C M a_{0,m} on cubes of size C M l_m with
  cube inside Omega''_m and meeting the complement of Omega''_{m+1} (m < j), or inside Omega''_j and meeting the
  complement of Omega_{k_0+1} (m = j).
- (ii), on (Omega_m minus Omega_{m+1}) cap X for m = k_0+1..j: the same seven entries below
  kappa' L_0^{2(j-m)} times the bracket at level j (a_{0,j}, a_{1,j}, l_j). Gauge clause (1.67):
  l_j |A|, l_j^2 |grad A| < L_0^{2(j-m)} B C M a_{0,j} on cubes of size C M l_j inside Omega_m meeting the complement
  of Omega_{m+1}.
- (iii), on (Omega_m minus Omega_{m+1}) cap X for m = j+1..k-1 and on Omega_k cap X for m = k: the entries below
  kappa c times the bracket at level m, with c = 1 for m < k and c = 3 for m = k, no power of L_0. Gauge clause
  (1.69): l_m |A|, l_m^2 |grad A| < B C M a_{0,m}, cubes of size C M l_m inside Omega_m meeting the complement of
  Omega_{m+1} (inside Omega_k if m = k).
"The constant C above is a positive integer ... we can assume that C <= 2. The constant B is a fixed absolute
constant, for example ... B = B_3 from Theorem 1 [16]." For j <= k_0 there are no powers of L_0 in (i) and (ii) is
empty. "For n = j - h = 0 the above space coincides with the space U~^c_k(X, a~_0, a~_1)."

2.2 **The layered space of CMP 119 p. 261.** On X cap (Omega_n minus Omega_{n+1}), n = 1..j-1, and X cap Omega_j:
entries below (1 - beta(1 - 2^{-(j-n)})) times [a_{0,n} xi^2 l_n^{-2}, ..., a_{0,n} l_n^{-3}, ...], twist
l_n |A'|, l_n^2 |grad A'| < (...) a_{1,n}; gauge clause (2.38): l_n |A|, l_n^2 |grad A| < B C M a_{0,n} on cubes of
size C M l_n inside Omega_n minus Omega_{n+2} that meet the complement of Omega_{n+1}. This is the case "no power
of L_0" of 2.1, with the same seven entries.

2.3 **The cube class of the chart (CMP 99b p. 396; CA-I 12945-12956).** Each cube has one index j: it lies in
B^j(Lambda_j) cup B^{j+1}(Lambda_{j+1}) with Lambda_j = Omega_j minus Omega_{j+1}, it meets B^j(Lambda_j), and it is
a union of big blocks of the level-j lattice, of side O(1) M-frak l_j; the account takes O(1) = 12. So a cube of
index j of the tower T lies in Omega^T_j and meets the complement of Omega^T_{j+1}. This is the same shape as the
gauge clauses (1.65), (1.67), (1.69), (2.38).

2.4 **Common form.** Every space of 2.1-2.2 is given by a decreasing chain of domains
D_1, D_2, ..., D_r in X (for 2.1: Omega''_1..Omega''_j, Omega_{k_0+1}..Omega_j, Omega_{j+1}..Omega_k), and for each
link mu of the chain a scale index s_mu (nondecreasing in mu: 1..j-1, then j for the pairs
(Omega''_j, Omega_{k_0+1}), (Omega_{k_0+1}, Omega_{k_0+2}), ..., (Omega_j, Omega_{j+1}), then j+1..k), a radius index
n_mu = s_mu, an exponent e_mu with 0 <= e_mu <= n_mu - k_0 when n_mu > k_0 and e_mu = 0 otherwise, and:
- (E) on (D_mu minus D_{mu+1}) cap X: l |A'| , l^2 |grad_U A'| < 3 L_0^{2e} a_{1,n}; l^3 |J-bold| < 3 L_0^{2e} a_{0,n},
  with l = l_{s_mu};
- (G) for every cube Q of side C M l inside D_mu that meets the complement of D_{mu+1}: a G-valued u on Q cap X with
  U^u = exp(i eta A), l |A|, l^2 |grad A| < L_0^{2e} B C M a_{0,n}.
The level function of the space is lambda(x) := s_mu for x in D_mu minus D_{mu+1}.
Two things are read from the printed clause and not re-derived from the geometry of CMP 122a (1.12)-(1.13):
(G1) the chain is decreasing (in particular Omega_{k_0+1} inside Omega''_j for j > k_0), and (G2) the regions of
(i)-(iii) cover X. Both are what the wording "on (Omega''_j minus Omega_{k_0+1}) cap X for m = j" presupposes.

## 3. Theorem A: a layered space lies in the chart class of every tower that is nowhere coarser (step 3, written 2026-11-23T21:52Z)

**Setting.** X a domain. A *layered supplier* on X is a set of pairs in the common form 2.4: chain D_1 > ... > D_r
with X inside D_1, scales s_mu, level function lambda, clauses (E) and (G) with constants
K^G_mu = L_0^{2 e_mu} B C M a_{0,n_mu}, K^1_mu = 3 L_0^{2 e_mu} a_{1,n_mu}, K^J_mu = 3 L_0^{2 e_mu} a_{0,n_mu}.
T = {Omega^T_j} is an admissible tower in the sense of CA-I 12712-12722, with level function
lambda^T(x) = j on Omega^T_j minus Omega^T_{j+1}. S(T; X) is the class (S1)-(S3) of CA-I 12945-12971 read on X:
(S1) for the cubes of the class of T (2.3) that lie in X, (S2) and (S3) at the bonds of X with the weights
l_{lambda^T}. (The class is cube-local and pointwise, so this restriction is meaningful; whether the switched chart
needs only S(T; X) when the cubes outside X are switched off is the link reading, `ch-r2.md` (P1)/(I2), not
this row.)

**Premises (each named; none is a sought membership).**
- (RC) *Sub-cube reading of the gauge clause.* Clause (G) is read on every lattice cube of side at most
  C M l_{s_mu} that lies in D_mu and meets the complement of D_{mu+1} (no second condition for mu = r). This is the
  analogue of the account's reading (rho 1) for CMP 109 (1.12) (CA-I 13096-13100: "read as imposed on every cube
  ... of size at most c_12 L M") and of `4.14:rem-supply-scope` (i)-(ii). It follows by restriction of u if the
  printed family consists of all lattice translates of cubes of side C M l and each D_mu is a union of cubes of
  the M l-grid: a cube Q' of side at most M l inside D_mu meets at most two grid cubes in each direction, all of
  them inside D_mu; in each direction choose an interval of length M l inside their union containing the interval
  of Q'; the product is a translate Q of side M l with Q' inside Q inside D_mu, and Q meets the complement of
  D_{mu+1} because Q' does. [proved under the two stated "if"s; whether Balaban's cubes are all translates or grid
  cubes is not printed, so (RC) stays a reading convention]
- (G1), (G2) of 2.4.
- (REG) *Balaban's small-coupling regime* as in `4.14:lem-integer-power-bound` (CA-I 48867-48880): block counts
  R_i powers of L, CMP 119 (2.9), N_0 exists, 1 <= L_0 and L_0^2 <= L/3. Then L_0^{2e} <= c_1 R_n whenever
  0 <= e <= n - k_0 and n <= k, and for e = 0 (`4.14:eq-supply-scope-2`, CA-I 49650-49662; R_n >= 1, c_1 >= 1).
- (FL) 17 M-frak <= M. It holds in the account: M > M_2 = L^2 M_1 >= 25 M-frak (CA-I 49725-49726, 12689-12693).
- (LM) *Level inequality.* lambda^T(x) <= lambda(x) for every x in X.

**Ceilings (after d, L, M-frak, M_1, M; on the layer couplings).** For every level n <= k:
(C1) c_1 B C M R_n a_{0,n} <= a_0;  (C2) 3 c_1 R_n a_{1,n} < a_1;  (C3) 3 c_1 R_n a_{0,n} < a_gamma.

**Theorem A.** Under (RC), (G1), (G2), (REG), (FL), (LM) and (C1)-(C3), every pair of the layered supplier lies in
S(T; X), with a := A', U_r := U, J := J-bold. **Proved** (from the printed clauses and the premises; one reading).

*Proof.* (S1). Let Q' be a cube of the class of T with index p, inside X; its side is at most 17 M-frak l_p (12 for
the class cubes; the argument also covers the enlarged cubes of sides 11 and 17, as at CA-I 13056-13062). By 2.3,
Q' lies in Omega^T_p, so lambda^T >= p on Q'. Let mu be the largest index with Q' inside D_mu (it exists since
Q' is inside X inside D_1). If mu < r pick x in Q' outside D_{mu+1}; then lambda(x) = s_mu, and by (LM)
p <= lambda^T(x) <= lambda(x) = s_mu. If mu = r then lambda = s_r on Q' and again p <= s_r. So
side(Q') <= 17 M-frak l_p <= M l_{s_mu} by (FL), and (RC) gives a G-valued u on Q' with U^u = exp(i eta A) and
l_{s_mu} |A|, l_{s_mu}^2 |grad A| < K^G_mu. Since l_p <= l_{s_mu},
l_p |A| <= l_{s_mu} |A| < K^G_mu = L_0^{2e} B C M a_{0,n} <= c_1 B C M R_n a_{0,n} <= a_0,
and the same for l_p^2 |grad A|, by (REG) and (C1). This is (S1) at index p.
(S2). At a bond at x in D_mu minus D_{mu+1}, with q = lambda^T(x) <= s_mu by (LM): l_q |A'| <= l_{s_mu} |A'| < K^1_mu
and l_q^2 |grad_U A'| <= l_{s_mu}^2 |grad_U A'| < K^1_mu, by (E). There are finitely many levels, so
N_U(A') <= max_n 3 c_1 R_n a_{1,n} < a_1 by (REG) and (C2).
(S3). Likewise l_q^3 |J-bold| <= l_{s_mu}^3 |J-bold| < K^J_mu <= 3 c_1 R_n a_{0,n} < a_gamma, by (C3). QED

**Remarks.**
1. *What the proof uses of the seven entries.* Only the gauge clause, the two twist entries and the current
   entry. Entries 1, 2, 4, 5 (plaquettes of U-bold and U, auxiliary minimisers and their currents) are not read:
   S has no such clause (CA-I 12969-12970, 13016-13017). The coefficient kappa <= 1 and Balaban's c = 3 are
   absorbed in the factor 3.
2. *The cube-fitting clause of `ch-r2.md` (P4') is automatic.* (P4') asked for the level inequality AND that each
   class cube of the finer tower fit inside a cube of the coarser class. For a supplier in the common form the
   second clause follows from the first, (FL) and (RC): that is the step "mu := largest index with Q' inside D_mu".
3. *Order of choice.* a_0, a_1, a_gamma depend on (d, L) only (CA-I 12942-12943, 14504-14510). (C1) is the only
   ceiling that contains M explicitly; it bounds M R_n a_{0,n}, the quantity of the account's own layerwise ceiling
   `4.14:eq-block-size-conditions-c` (CA-I 45789-45792: L^2 c_1 B M R_n a_{0,n} <= a^sharp_ceil, "read after d, L,
   M_1, M_1^sharp, M"); since C <= 2 <= L^2, (C1) is implied by that ceiling whenever a^sharp_ceil <= a_0, and is
   otherwise one more ceiling of the same kind at the same position. With a_{i,n} = g_n C_i (log g_n^{-2})^q
   (CMP 119 (2.28); CA-I 1606-1608) and R_n a power of log g_n^{-2}, each of (C1)-(C3) is g_n <= g^flat(d, L, M, C_0,
   C_1), a condition on the layer's own coupling, uniform in k, K, the history, X and the piece. So: radii before
   M; the explicit M-reading ceiling falls on a_{0,n} only. One qualification, so that nothing is hidden: (C2)
   reads M implicitly, because the Stage-7 floor C_1 > 2 B_3^2 O(1) M C_0 (CA-I 1601-1611) makes a_{1,n} at least
   2 B_3^2 O(1) M a_{0,n}; so (C2) implies 6 c_1 B_3^2 O(1) M R_n a_{0,n} < a_1, again a ceiling on M R_n a_{0,n}.
   Both fall on the coupling, which is chosen last. No floor on a coupling and no cap arises.
4. *The row's obstruction does not exist for the stage spaces.* **Corollary A1 (proved, same premises).** On the
   crucial domain Omega''_{k_0+1} minus Omega_{k_0+1}, and on every other region, each stage-space constant read by
   S is at most c_1 B C M R_n a_{0,n} (gauge), 3 c_1 R_n a_{1,n} (twist), 3 c_1 R_n a_{0,n} (current) at its own
   radius index n. None of them exceeds the class radius for every admitted coupling: the largest power is
   L_0^{2 N_0} <= c_1 R_n (`4.14:lem-top-power-bound`), polylogarithmic in g_n, against a_{0,n} = g_n times a
   polylogarithm. The second alternative of the row (a legal stage datum outside S for every admitted a_0) is
   excluded for every tower satisfying (LM).
5. *Scope.* Theorem A covers: the CMP 119 space (e = 0), every stage space of CMP 122a (any n, in particular
   n = N, Balaban's value space of (1.65)), and any other supplier in the common form. Its one geometric
   hypothesis is (LM). Section 4 examines (LM) at the three links.

## 4. The three links: which backgrounds Theorem A reaches (step 4, written 2026-11-23T21:53Z)

The composed read is R = E_2(sigma^(2); E_3(sigma^(3); E_4(sigma^(4); d))) (`cm-o3-fable.md` 2.1). Each link has a
chart tower (the determining system of its response function) and a background (the configuration at which the
response is taken). From CMP 122b pp. 373-374 and `ch-r2.md` (2a), Proposition F:

| link | response | chart tower | background |
|---|---|---|---|
| 4 | H_k of (1.58), (1.64) | B_k (new set, (1.33)) | the source pair (U-bold, J-bold) on Y_4 |
| 3 | H_{B_1} of (1.57) | B_1(Y_2) = B(Y_2) cup B_1, B_1 = B''_k cup B_h(Omega''~_{h+1}) by (1.52) | w_3 = output (1.63), a minimiser for B_k(Y_3) with switched data on the layer of Y_3 |
| 2 | H''_k of (1.61) | B''_k(Y_1) = B(Y_1) cup B''_k | w_2 = output (1.62), a minimiser for B_1(Y_2) |

4.1 **Link 4: the source space. Proved, given one identification.** (D1) *Identification:* the argument space
U~^c_k(Y_4, a~_0, a~_1) of CMP 122b (1.65) is the layered space of CMP 119 (2.34)-(2.39) (Section 2.2) for the
domain sequence of the new determining set B_k, read on Y_4. Grounds: CMP 122b does not reprint the space; its
(1.68) states the new terms on "the space U~^c_k(Y, a~_0, a~_1)" for the new set, which is the inductive format of
CMP 119 (2.41)-(2.42); CMP 122a p. 191 says the stage space at n = 0 "coincides with the space
U~^c_k(X, a~_0, a~_1)" and at n = 0, j = h <= k_0 there is no power of L_0. The account cites the space without
restating it (CA-II 48352-48354). [reading, not printed in one place]
Under (D1) the supplier's level function is lambda^{B_k}, and the chart tower is B_k itself, so (LM) is an
equality. **Corollary A2 (proved under (D1), (RC), (FL), (G1)-(G2)).** Every source pair lies in S(B_k; Y_4), with
e = 0: the ceilings are B C M a_{0,n} <= a_0, 3 a_{1,n} < a_1, 3 a_{0,n} < a_gamma, and (REG) is not needed. The same
holds for every tower T on Y_4 with lambda^T <= lambda^{B_k}. If instead the argument space is read with the
stage powers (any of the forms of 2.1), Theorem A gives the same conclusion with the ceilings (C1)-(C3). Either
way the first half of the row's statement holds: the stage / source spaces on Y_4 lie in the chart class, radii
before M, explicit M-ceiling on a_{0,n} only.

4.2 **Level relations between the three towers, from the printed definitions.**
- (L-a) lambda^{B''_k} <= lambda^{B_k} everywhere, with equality off Z. **Proved** from (1.33): "Gamma_j =
  Gamma''_j cap Z^c for j < k, Gamma_k = Gamma''_k cup Z^(k)" (CMP 122b p. 365, OCR L529-533; `ch-r2.md` L194).
- (L-b) lambda^{B_1} <= lambda^{B''_k} on the support of B_1, with strict inequality on the layer of the seam
  d Omega''~_{h+1}. **Sketched.** (1.52) joins B''_k with the boundary tower B_h(Omega''~_{h+1}), levels 0..h, by the
  rule (2.14) of CMP 119, which keeps B''_k away from the seam and uses the boundary tower on the layer at the
  seam (`ch-r2.md` L195-196, read there from the page image). Inside Omega''_{h+1} the levels of B''_k are at
  least h + 1, and the boundary tower's are at most h and go down to 0 at the seam. Not checked: the support
  conventions of (2.14) and on which side of the seam each layer lies.
- (L-c) lambda^{B(Y) cup B} <= lambda^B on Y (the localised system is nowhere coarser than the system it localises).
  **Sketched.** CMP 122b p. 373: Y minus Y^0 is "a boundary layer ... of the width 2 M_1 at most, for the
  corresponding scale"; a boundary tower reaches level n + 1 only at distance at least M_1 l_{n+1} = L M_1 l_n
  from the boundary, more than 2 M_1 l_n. Not checked at edges of level regions.

4.3 **Link 3: right direction.** The chart tower is B_1(Y_2); the background w_3 is a minimiser for B_k(Y_3). By
(L-a), (L-b), (L-c), lambda^{B_1(Y_2)} <= lambda^{B_k(Y_3)} on Y_2 off the two boundary layers; on them the comparison is
between boundary towers of Y_2 inside Y_3 (`ch-r2.md` L195: "a point is no farther from Y_2^c than from Y_3^c").
**Sketched.** If w_3 = e^{i eta a} W with W regular in the common form (E), (G) at the levels of B_k(Y_3) and a small
at those levels, then the proof of Theorem A gives (w_3, J_3) in S(B_1(Y_2); Y_2) with the factor of the supplier's
constants only; this is the implication (P4') => (P4) of `ch-r2.md`, now with its cube-fitting clause removed
(Remark 2 of Section 3), provided the gauge family of W obeys a sub-cube reading (RC'): CMP 99b (3.35) for the
tower of W read on every sub-cube of side at most 12 M-frak l inside a class cube. **Not proved here:** that W and
a have that regularity. It is `ch-r2.md` (P1)-(P3), (P5) (CMP 102b Theorem 1 at the localised system, the switched
response bound, the reference datum). Balaban prints only "almost the same" (CMP 122b p. 375; `ch-r2.md` (2b)).

4.4 **Link 2: wrong direction on the seam layer. Finding, sketched.** The chart tower is B''_k(Y_1); the background
w_2 is a minimiser for B_1(Y_2). By (L-b) the chart tower is COARSER than the background's own tower on the layer
of the seam d Omega''~_{h+1}, by up to h + 1 levels (boundary-tower level 0 at the seam against level h + 1 of
B''_k). So (LM) fails there for the pair (chart = B''_k(Y_1), supplier = regularity of w_2 at its own tower), and
the monotone argument of Theorem A cannot give (w_2, J_2) in S(B''_k(Y_1); Y_1) on that layer. What the own-tower
regularity gives at a point of level q' < q = lambda^{B''_k}: l_q |a| <= L^{q-q'} l_{q'} |a|, a loss of L^{q-q'}, up to
L^{h+1}; this is not polylogarithmic in the coupling (h = k - N), so no coupling ceiling pays it; and the class
cubes of index q are L^{q-q'} times larger than the cubes on which the own-tower gauge clause is given.
*What this is and is not.* It is not a counterexample: a minimiser for a finer system whose data are the
averages of a configuration regular at the coarser levels has that coarser regularity (the nesting identity:
`ch-r2.md` Lemma R, `mu.md` Sections 5-6, CA-I `4.5:lem-window-minimiser` 19267-19374), and Balaban's claim (1.65)
for the composite presupposes exactly this ("regularity properties ... almost the same as of the configuration
U(B_1(Y_2), M(U-bold))", p. 375). But the data of (1.62) are not all averages of one regular configuration: on
the seam they contain the entries M(U_0^{(A,L)}) on Lambda cap Omega''_k and 1 on Z''_k cap Omega''~_{h+1}
(`ch-r2.md` L118), put there "to break the configuration U_k into two independent parts by the boundary
conditions at the boundary d Omega''_{h+1}" (CMP 122b p. 362). So the membership of w_2 in the chart class of link 2
needs a statement that is neither in Theorem A nor in (P4'): *coarse regularity of the glued configuration
U_1 of (1.53) across the seam, at the levels of B''_k*. I did not find it printed (Balaban: "the same remarks
apply"), nor in the account's link definitions (CA-II 47976-48145 give the formulas; the reading
`5.6:def-link-readings` takes the bound "uniformly in the background" as a hypothesis), nor in `ch-r2.md` (its
CH3-REG item says "should apply ... not written"; link 2 is not treated). [the level picture of the seam rests
on (L-b), which is sketched; the conclusion "a seam statement is needed" is therefore sketched, not proved]

4.5 **Summary of Section 4.**
| object | in the chart class? | status |
|---|---|---|
| source / stage spaces on Y_4 at link 4 (tower B_k or finer) | yes | proved under (D1) or directly by Theorem A; reading premises (RC), (G1), (G2) |
| Balaban's value space on Y_1 (n = N) at tower B''_k(Y_1) or finer | yes (Theorem A, (LM) by (L-c)) | proved given (L-c), which is sketched |
| background w_3 of link 3 | reduces to own-tower regularity of the link-4 output | implication proved (Theorem A's argument); premises = `ch-r2.md` (P1)-(P3), (P5); level inequality sketched |
| background w_2 of link 2 | not reached: level inequality fails on the seam layer | open; needs the seam statement of 4.4 |
