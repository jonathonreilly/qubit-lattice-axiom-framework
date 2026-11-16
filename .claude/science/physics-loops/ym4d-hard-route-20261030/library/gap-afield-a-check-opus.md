lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T15:18Z

# Check of row 1031 (`library/gap-afield-a-max.md`), work item W1

Queue row 1033, `gap-afield-a-check-opus`. Checker: Claude Opus 5.5 at max effort, Mac mini worker 3, started 2026-11-16 03:18Z (date -u). Checked file: `library/gap-afield-a-max.md` at commit ee938bdf2 (written by Claude Fable 5.2, same provider, so this is a same-provider check, not an independent one in the sense of the working rules). No new attack. Verdicts: HOLDS, HOLDS AFTER CORRECTION, FAILS with the first failing line.

## Plan (at most eight steps; each response does one step and appends its result)

1. Read W1 (L988 and following) and the definitions it relies on (`parts/gap.md` sections for (W), (S0), (BDD-Delta), (FIN), Theorem CR; `library/gap-dichotomy.md`); record the exact scope of W1 here.
2. Check Theorem CR^c and its lemmas (Lemma EQC, Lemma FLOW, Proposition OM^c, Proposition T23) line by line.
3. Check Proposition VIR (dD/d log b = 4 (D - H) on limit objects).
4. Check Corollaries KB and ENT (and Lemma Z4 if W1 names it).
5. Check Theorem CE-II and Proposition NR-II (no soft proof of (BDD-Delta) on torus data).
6. Check Lemma SURF.
7. Check the remaining items W1 names (ARGUED kills, if in scope), and the RESULT line of row 1031 against the verdicts.
8. Verdict table and RESULT line.

## Step 1 result: scope of W1 and what was read

**Scope (W1 of the checked file, L988-1006, as written).** Check line by line Sections 5.2 and 7.1-7.5 of
`library/gap-afield-a-max.md`: (P1)-(P4), Lemma EQC, Lemma ASC, Lemma FLOW with Lemma UNI, Lemma E0, Proposition
OM^c, Proposition T23, Theorem CR^c, Proposition VIR, Corollaries KB and ENT, the implication from (ENT-lat), Lemma
Z4 with Corollary Z4', Theorem CE-II, Proposition NR-II, Lemma SURF. Test first: (a) EQC (ii) with s = ceil(t/2)
and 48 C_1; (b) FLOW (c) tail bound with rounded times and Lemma UNI; (c) CR^c step "(3^c) gives (2)"; (d) VIR
(V5)-(V7); (e) KB, Fubini and invariance; (f) CE-II, record construction and converse; (g) NR-II, the lines datum,
(E2) and f = 0; (h) SURF, the mean-zero step for plaquettes that cross cells. Stop rule: stop at the first WRONG
that breaks Theorem CR^c, Corollary KB or Theorem CE-II; otherwise at most ten defects, ranked. Verdict per
statement: HOLDS, HOLDS AFTER CORRECTION, FAILS. No new attack.

**Output name.** W1 names `library/gap-afield-a-check.md`; queue row 1033 and the worker brief name
`library/gap-afield-a-check-opus.md`. This file follows the row and the brief.

**Inputs read (at ee938bdf2).** `gap-dichotomy.md` 1.1-1.4, 2.1-2.2 (datum (E1)-(E3), family with units, (S0), P,
D^+, z^-, (PHYS-SEED), (BDD-Delta), (W), admissible sequence, Omega(D_0), Theorem CE, Proposition OM, Theorem CR);
`gap-compact-rigidity-max.md` L131-243 (3.1-3.6: datum, rescaling, Lemma UF with c_S, Theorem CE with proof,
Proposition OM with proof, Theorem CR); `gap-crux-restate.md` L30-45 (Lemma A, (LB)) and 3.4 (Lemma K, Lemma X,
Lemma E, Theorem S, Lemma E', Corollary S3'). Their statements are taken as inputs, as W1 asks; they are not
re-checked here.

## Step 2a result: Section 7.1 of the checked file (L480-622)

Each line was redone from the inputs of Step 1. Verdicts first, then the details that a reader may want to
re-check.

| Statement | Verdict | Note |
|---|---|---|
| (P1), (P2), (P3) | HOLDS | (P3)'s "in particular" uses (P1) from (a, a, a, a), not (P3) itself; the proof covers it. |
| (P4) | HOLDS AFTER CORRECTION (typographic) | Source line L493 starts with "  - ((t' - t)/(t - s)) ...". In Markdown that minus is a list bullet, so the rendered text says ((t' - t)/(t - s)) Delta(s, B) <= Delta(t', B) - Delta(t, B), which is false. Write it as Delta(t', B) - Delta(t, B) >= - ((t' - t)/(t - s)) Delta(s, B). The proof and every use (EQC) have the minus. |
| Lemma EQC (i), (ii) and the "more exactly" form | HOLDS | test (a) below |
| Lemma ASC | HOLDS | |
| Lemma FLOW (a), (b) | HOLDS | |
| Lemma FLOW (c) with Lemma UNI | HOLDS | test (b) below; UNI tacitly needs e_0 finite (true in every use: e_0 >= - C(1)) |
| Lemma FLOW (d), (e) | HOLDS | |
| Lemma E0, both uses | HOLDS | lattice use: see below |
| Proposition OM^c (a), (b), (c) | HOLDS | |

**Test (a), Lemma EQC (ii).** All entries lie in [N m_1, N m_2 + 1], so t >= N m_1 >= 12. Then s = ceil(t/2) >= 6,
s < t, and t - s = floor(t/2) >= (t - 1)/2 >= t/3 (true for t >= 3). The quadruple (s, B) has all entries integers
in [N m_1/2, N m_2 + 1], so (P3) at its least entry mu' reads M, and |(s, B)|/mu'^4 <= (2 (N m_2 + 1)/(N m_1))^4
<= (4 m_2/m_1)^4 = 16 C_1, because N m_2 + 1 <= 2 N m_2. Left side of (P4): Delta(t', B) - Delta(t, B) >=
- (t' - t) Delta(s, B)/(t - s) >= - 3 (t' - t) 16 C_1 M/t >= - 48 C_1 M (t' - t)/(N m_1). Right side of (P4) gives
the smaller bound C_1 M (t' - t)/(N m_1). Every intermediate quadruple of the one-entry-at-a-time path keeps its
entries in the interval. |ceil(a) - ceil(b)| < |a - b| + 1. The constant 48 C_1 M/m_1 and the term 4/N follow.

**Test (b), Lemma FLOW (c).** With T'_i = ceil(N_i T')/N_i and (T'/2)_i = ceil(N_i T'/2)/N_i: the count at the
time (T'/2)_i gives at most exp((T'/2)_i Lam + C(T'/2)) <= exp((T'/2 + 1) Lam + C(T'/2)) < R levels with
eps_r <= Lam, so eps_r > Lam > 0 for r >= R (levels are ordered). For those r, exp(- T'_i eps_r) <=
exp(- (T'_i - (T'/2)_i) Lam) exp(- (T'/2)_i eps_r), with T'_i - (T'/2)_i >= T'/2 - 1/N_i (also when this is
negative). Summing gives the stated tail bound. The limit tail obeys the same bound as a limit of partial sums.
Lemma UNI: dominated convergence on [1, infinity) against exp(T e_0) G(1) gives m_0; induction removes one level
value at a time, and only finitely many levels lie below any bound. The sub-subsequence argument then gives
convergence of every level along the whole subsequence of (a); the extraction is per box B, which is allowed
because the limit levels do not depend on the extraction.

**Lemma E0, lattice use.** g_i(T) = Delta_(j_i)(ceil(N_i T), B_i) = - T_i c_i + log(1 + S(ceil(N_i T); B_i)), with
T_i = ceil(N_i T)/N_i. The two inequalities of the proof hold with T_i in place of T, and T_i/T -> 1. Pointwise
convergence g_i(T) -> E(T, B) for integer boxes with B_i/N_i -> B follows from (a) and the "more exactly" form of
EQC, since |B_i - ceil(N_i B)| = o(N_i).

**Proposition OM^c (a).** For E in EE with D_E <= D_0 on (0, infinity), the real form of EQC is direct: on
[m_1, m_2]^4, E <= (m_2/m_1)^4 D_0, the increment to the right is at most (t' - t)(m_2/m_1)^4 D_0/m_1 (E/T
non-increasing), and convexity with s = t/2 bounds it below by - (t' - t) 32 (m_2/m_1)^4 D_0/m_1. So the set is
equicontinuous on compacts; closedness as written (FLOW (e); the proof of FLOW (c) with continuous times; (c)).

## Step 2b result: Proposition T23 (7.2) and Theorem CR^c (7.3)

| Statement | Verdict | Note |
|---|---|---|
| Proposition T23 (a)-(d) | HOLDS | |
| Proposition T23 (e) | HOLDS as an implication on Omega^c(16 D_0); the identification with a limit set "built with sizes 2^i 3^j" stays ARGUED, as the file says | the heading of 7.2 and the RESULT line say "PROVED" for T23 as a whole; it is PROVED except that identification |
| Proposition T23 (f) | HOLDS | the product family may need to be indexed by i (pairs (j_i, j'_i)); harmless |
| Theorem CR^c, all five equivalences and the last sentence | HOLDS | test (c) below |
| By-products (1), (2) of 7.2 | HOLD as stated (upper bounds on D only) | see the note below |

**T23 (e).** Read on Omega^c(16 D_0), (RIG-23) says that no non-empty closed set is invariant under sigma_2 and
sigma_3 and minimal. By (b) these sets are the closed flow-invariant sets, so (RIG-23) on Omega^c(16 D_0) is
(4^c) of Theorem CR^c, which is (W). This part is PROVED. The row's own wording of (RIG-23) speaks of a limit set
built from sizes 2^i 3^j, which the file never defines; identifying it with the restriction of Omega^c is the
ARGUED step, and no other statement reads it. Repair (unproved, not needed by any consumer): define the grid set
by (H1), (H2) at the sizes N_i 2^i 3^j; the seed argument of CR^c ("(3^c) gives (2)") shows that (H2) at every
grid size holds for large i along any dyadic admissible sequence, which gives non-emptiness when (PHYS-SEED)
fails; the converse direction is that of OM (b).

**T23 (f).** A_(m, eps) is a datum: Z(k, B) = 1^k + (m - 1) exp(- eps |B|)^k, f = 0 (values positive, tending to
0), Delta = log(1 + (m - 1) exp(- eps |n|)). With eps_i N_i^4 -> 0 the rescaled functions tend to log m and the
rescaled levels to 0 (m - 1 of them) uniformly on compacts; D <= log m gives local boundedness. Product: f of the
product is f + f' because F/|n| does not increase in each side (P1), so f is the limit along the diagonal and the
two Delta add; the top product eigenvalue is strictly largest. Then
S_(E + E') = (1 + S_E)(1 + S_(E')) - 1 >= S_E.

**Test (c), Theorem CR^c.**
- "(2) gives (3^c)". q = 5041 S_j(N; (2N)^3) <= q' and N = l u_j/2 >= 6 is an integer by (S0); Corollary S3' gives
  S_j(2^k N; L^3) <= q'^(2^k)/71 <= s_0 for L in [2^(k+1) N, 2^(k+2) N), k >= k_0; s_0 < 1/71^2 = 1/5041. Thermal
  sums do not increase in time because lambda_0 > lambda_1 (E2). 2 ceil(y/2) >= ceil(y), so t_i >= L_i/2. The
  identification of the lattice thermal sum with exp(Delta_i(b/2, b, b, b) + (t_i/N_i) eps_0^(i)(b^3)) - 1 is exact,
  since ceil(N_i b/2) = t_i and ceil(N_i b) = L_i; the limit is s_E(b) by FLOW (a), (c).
- "(3^c) gives (2)". (P3)'s second form gives D(a) <= 16 D(2^m N_i) on [2^m N_i, 2^(m+1) N_i], so (j_i, N_i) is a
  blow-down sequence and D_E <= 16 D_0 at every real b. L_i = 2 ceil(N_i b/2) differs from ceil(N_i b) by 0 or 1,
  and n_i = L_i/2 = ceil(N_i b/2) is exactly the rounded time of Delta_i(b/2, ...). So the Delta part converges by
  the "more exactly" form of EQC, and N_i E_0(L_i^3) -> e_0^E(b^3) by Lemma E0 in its lattice form (B_i = L_i^3,
  B_i/N_i -> (b, b, b)). Theorem S is monotone in s: S(2 n_i; (4 n_i)^3) <= c_S = ((1 + 1/5041)^64 - 1)^2; by hand,
  64/5041 = 0.012696, e^0.012696 - 1 < 0.012778, square < 1.633 x 10^(-4) < 1.64 x 10^(-4). q_1 < 5041 x 1.64 x 10^(-4)
  = 0.8267 < 0.83; ln 0.83 < -0.186; q_1^32 < e^(-5.95) < 2.7 x 10^(-3); /71 < 3.9 x 10^(-5) < 1/5041. Corollary S3'
  with N' = 2 n_i = L_i covers every L >= 2^6 N' = 64 L_i (k >= 5), and the time L/2 >= D/2 for even L. With
  2^m >= 64 (b + 1) and N_i >= 2: 2^m N_i >= 64 N_i b + 128 >= 64 L_i, and 2^m N_i = 2^(k_i + m) u_(j_i) is even. So
  s^(j_i,k_i)(2^m) < 1/5041 for all large i, against (H2). The step is right.
- Last sentence: for x dyadic and i large, ceil(N_i x) = 2^(k_i) u_(j_i) x, so the real limit restricts to the
  pointwise dyadic limit.
- (4^c), (5^c): Zorn with the finite intersection property; Krylov-Bogolyubov for a continuous flow on a compact
  metric space (OM^c (a), (b) supply compactness, metrisability and continuity). Named input, standard.

**By-products of 7.2.** (1) holds: Theorem CR^c is the proof. (2) is (P3) and holds for upper bounds on D. It does
not remove (S0) from Theorem CR^c: "(2) gives (3^c)" uses that l u_j/2 is an integer, and Theorem CE (i)(b) is
stated under (S0). The file's wording ("as far as upper bounds on D are concerned") already limits it so.

## Step 3 result: Proposition VIR, Corollaries KB and ENT, the implication from (ENT-lat) (7.3, L716-784)

| Statement | Verdict | Note |
|---|---|---|
| Proposition VIR (V1)-(V4) | HOLDS | |
| Proposition VIR (V5)-(V7) | HOLDS | test (d) below |
| Proposition VIR (V8) | HOLDS | |
| Corollary KB | HOLDS | test (e) below; Krylov-Bogolyubov is used only for the existence of nu in ENT and CR^c, not in KB |
| Corollary ENT, both parts | HOLDS | |
| (ENT-lat) gives (W) | HOLDS | |

**(V1)-(V4).** x e^(-T x) <= x e^(-T_0 x) <= (2/(T_0 e)) e^(-T_0 x/2) for x >= 0, T >= T_0; x^2 e^(-T_0 x/2) is
bounded; the levels <= 0 are at most G(T) in number. So G = sum e^(-T e_r) is C^2 on (0, infinity) term by term,
E' = - <e>, E'' = <e^2> - <e>^2. Gibbs: H = sum p_r (T e_r + E). (V3): (T E' - E)/T^2 = - H/T^2 <= 0 since H >= 0.
(V4): with g = E(., b^3) convex and b g'(b) = - tau_E(b): g(2b) >= D - tau and g(2b) <= 2 D give tau >= - D;
g(b/2) >= D + tau/2 and g(b/2) = E(b/2, b, b, b) <= 8 D_E(b/2) (E/x_i non-increasing, three sides) give
tau <= 16 D_E(b/2) - 2 D. With D <= D_0 this gives |tau| <= 16 D_0, as KB uses.

**Test (d), (V5)-(V7).** (V5): g_n(t) = E_n(t, B_n) -> E(t, B) uniformly for t in compacts, because E_n -> E
uniformly on compacts and E is jointly continuous (the hypothesis "E continuous" is what this step reads; elements
of BB are locally Lipschitz). Lemma CVX then needs only the two difference quotients of a convex differentiable
function; its recalled fact (pointwise convergence of convex functions is locally uniform) is not even needed
here, since convergence is uniform by hypothesis. So <e> is jointly continuous in (E, T, B). (V6): the four
telescoping terms move side 1, 2, 3, 4 in turn; after the symmetry the fixed sides are exactly B_1, ..., B_4, and
each term is the integral of E' = - <e> (E(., B) is C^1). (V7): B_i(lambda) -> b^3 as lambda -> 1, and the integrand
is within o(1) of <e>(b; b^3) on the whole interval by joint continuity, from either side of lambda = 1. So
D_E'(b) = - 4 <e>(b; b^3), continuous, and d/ds D_E(e^s) = - 4 tau_E(e^s). (V8): the weights of phi_lambda E at
(b; b^3) are those of E at (lambda b; (lambda b)^3).

**Test (e), Corollary KB.** E -> tau_E(1) = <e>_E(1; 1^3) is continuous by (V5) and bounded by 16 D_0. The map
(u, E) -> tau_(phi_(e^u) E)(1) is continuous on [0, s] x Omega^c(D_0) (OM^c (b)) and bounded, so Fubini applies.
Invariance is used twice, each time on a bounded continuous function: E -> D_E(1) (bounded by D_0) and
E -> tau_E(1). The identity D_(phi_(e^s) E)(1) - D_E(1) = - 4 integral_0^s tau_(phi_(e^u) E)(1) du is (V7) with (V8).

**Corollary ENT.** The support of an invariant measure is closed, non-empty and invariant (the phi_t are
homeomorphisms), so it is M. A continuous function >= 0 with nu-integral 0 vanishes on supp nu. The dichotomy is
exhaustive: if tau_E(1) does not take both strict signs, it is >= 0 or <= 0 on M. D_E(1) is constant on orbits
(tau = 0, (V7)) and orbits are dense in M. (ENT+) as defined at A2 (tau_E(b) > 0 for all b) equals tau_E(1) > 0
on the invariant set. Then (ENT+) on Omega^c(16 D_0) iff Omega^c(16 D_0) is empty iff (W), by CR^c.

**(ENT-lat) gives (W).** (P2) at (t - 1, t, t + 1) needs t >= 4. N a_(j_i) >= N_i b l_1/u_(j_i) -> infinity, and
D_(j_i)(N) -> D_E(b) >= d_min > d_min/2. The increments Delta(t - 1) - Delta(t) do not increase in t, so
Delta(N - k) - Delta(N) >= k (Delta(N) - Delta(N + 1)) >= k c/N; (ENT-lat) is read only at N. N - k = ceil((1 - h) N)
is within 2 of ceil(N_i (1 - h) b), so the "more exactly" form of EQC passes to the limit: E((1 - h) b, b^3) - D_E(b)
>= h c. Letting h -> 0 gives - b g'(b) = tau_E(b) >= c. Then D_E(e^s) <= D_E(1) - 4 c s < 0 for large s, against
E >= 0. Not checked (record, not mathematics): the sentence that (ENT-lat) is (MONO-Delta) with a rate and is "on
file as blocked".

## Step 4b result: Lemma Z4 and Corollary Z4' (7.4, L785-821)

| Statement | Verdict | Note |
|---|---|---|
| Lemma Z4 (a), (b) | HOLDS | (a) needs no topology: sigma_c y = y for y = tau^a E gives Lambda(sigma_c y) = Lambda(y) directly |
| Corollary Z4' | HOLDS | e_0(B) > 0 is excluded too (the right side would tend to 0 while exp E >= 1); the text folds this into "it is at least 1 because E >= 0" |
| "Reading (ARGUED)" | not checked line by line (labelled ARGUED); its one formal use, that a scale-invariant element makes every jointly monotone Lambda constant on its tau-orbit, is Lemma Z4 (a) | |

Details. The tau_i are bijections of functions on DD^4 or (0, infinity)^4 and map X onto X, so tau^a is defined for
a in Z^4. In (b): sigma_c^(t_n) y -> y for y = tau^a E (tau^a continuous, maps commute); Lambda(sigma_c^t y) does not
increase in t >= 0, so Lambda(y) = lim Lambda(sigma_c^(t_n) y) <= Lambda(sigma_c y) <= Lambda(y); the chain through
tau_1 tau_2 tau_3 tau_4 forces Lambda(tau_4 y) = Lambda(y), and commutation gives each i; applying it at tau_i^(-1) y
gives the inverse steps. In Z4': strictness gives tau_i E = E; then E(2^k T, B) = E(T, B); e_0(B) < 0 makes the right
side unbounded and e_0(B) > 0 makes it tend to 0 < 1 <= exp E; so e_0(B) = 0 and, by dominated convergence from
time T, exp E(T, B) = m_0(B), an integer >= 1. The argument in each direction (spectral form in each direction)
makes E constant; a critical element has s = m - 1 >= 1/5041, so m >= 2.

## Step 5 result: Theorem CE-II and Proposition NR-II (7.5, L822-901)

| Statement | Verdict | Note |
|---|---|---|
| Theorem CE-II (i) | HOLDS AFTER CORRECTION (cosmetic) | eta_i = (2/i)/(d(k_i) - 1/i) needs d(k_i) > 1/i; true for large i since d(k_i) -> infinity; drop the finitely many first records |
| Theorem CE-II (ii) (a)-(c) | HOLDS | (ii) reads only the properties listed in (i), so it applies to every sequence with (i), as the equivalence needs |
| Theorem CE-II, converse and the equivalence with (LIOU-II) given (FIN) | HOLDS | |
| Proposition NR-II (1) | HOLDS | |
| Proposition NR-II (2), many vacua and lines | HOLDS | test (g) below; both families have D^+ = +infinity, as the file says |
| Proposition NR-II (3) | RECALLED, not checked | labelled so in the file |
| RESULT line: "so no soft proof of (BDD-Delta) exists on torus data" | OVERSTATED: ARGUED, not PROVED | see below |

**Test (f), the record construction.** Given (FIN), failure of (BDD-Delta) is the same as d unbounded (finitely
many finite values cannot bound it), so R(k) -> infinity and R changes only at records, which are therefore
infinite. (beta) is finitely many limsup conditions, so it holds for all large j; (alpha) holds for infinitely many
j because d(k_i) is a finite upper limit. For - k_i <= m <= 0 the size 2^m N_i is 2^(m + k_i) u_(j_i) with
0 <= m + k_i <= k_i, so (beta) and the record property give D <= d(k_i) + 1/i, and
(d(k_i) - 1/i)(1 + eta_i) = d(k_i) + 1/i. (ii): for a in [m_1 N_i, m_2 N_i] take m with a/2 < 2^m N_i <= a; if
2^(-k_i) < m_1/4 then m > - k_i, so (P3) gives D(a) <= 16 D(2^m N_i) <= 16 max(1 + eta_i, 16^m) M_i. EQC and ASC are
linear in M. Dt(1) = 1 since ceil(N_i) = N_i; for m <= 0 and k_i >= - m, ceil(2^m N_i) = 2^m N_i. The "hence" bounds
follow from (b) in four sides. Converse: k_i -> infinity puts 2^(k_i) l_1 above L_0, so M_i <= D_0 + 1/i.

**Test (g), NR-II (2).** Lines: with |n|/n_1 = |B| and |n|/n_i = k |B|/n_i for i >= 2,
Z_q(k, B) = (1 + q^k)^(|B|) c_B^k = sum_(l = 0..|B|) binom(|B|, l) (c_B q^l)^k, with |B|/n_i an integer. So (E2) holds
for every k, the top eigenvalue c_B is simple and c_B q < c_B. (E3): log Z_q(n)/|n| = sum_i log(1 + q^(n_i))/n_i > 0
tends to 0, so f = 0 and Delta = log Z_q. With q = e^(-1/N), D(N) = 4 N^3 log(1 + 1/e), and the rescaled function
is N^3 [sum_i (prod_(j != i) x_j) log(1 + e^(- x_i)) + o(1)] on compacts. log(1 + e^(-x)) has second derivative
e^x/(1 + e^x)^2 > 0 and is decreasing, which gives (b). (c): the bracket 3 log(1 + e^(-b)) - b/(1 + e^b) is at least
3 x 0.31326 - 1/2 = 0.4398 > 0.43 on (0, 1]. Many vacua: eps_i prod_k (N_i x_k + 1) -> 0 uniformly on compacts, so
numerator and D(N_i) are both log m_i - o(1) = log m_i (1 + o(1)).

**On "no soft proof of (BDD-Delta) on torus data".** NR-II (1) shows that the properties (a)-(c) kept by a
normalised limit admit the constant and every profile b^alpha, alpha in [0, 3]. NR-II (2) realises two of these
shapes as normalised limits of data, but of families that violate (FIN) and at the unit scale, not at record
scales. A family of data with (FIN) in branch (II) is only RECALLED (NR-II (3)). So the claim that the datum axioms
with (FIN) cannot give (BDD-Delta) rests on (3), and "soft proof" is not defined. What is PROVED: a proof of
(BDD-Delta) that reads only (a)-(c) of a normalised limit cannot exist. The RESULT line of row 1031 lists the wider
sentence under "PROVED by hand"; it should be marked ARGUED (or narrowed to the sentence above). The section title
"the kept properties exclude no growth rate" is also wider than (1): (c) excludes growth above b^4, and
alpha in (3, 4) is not covered (alpha = 4 is, by x_1 x_2 x_3 x_4). No consumer reads either sentence.

## Step 6 result: Lemma SURF (5.2, L424-454)

| Statement | Verdict | Note |
|---|---|---|
| Lemma SURF, D(N) <= 6 beta (2N - 1) N^2 xbar_N <= 12 beta N^3 | HOLDS AFTER CORRECTION (scope of an intermediate line) | the energy formula for E_nu[A_M] needs every k_i >= 2; the proof uses k_i = n_i >= 3, so the lemma stands |
| The defect identity D(N) = 6 beta (2N - 1) N^2 xbar_N - N^4 h | ARGUED, as labelled; consistent | given the variational principle for N-periodic states, the algebra checks (below) |
| The "dynamic form" Phi(N) <= 16 x 6 beta (2N - 1) N^2 xbar_N | HOLDS (stronger than its ARGUED label) | it is the proof of SURF with M = (2N)^4, K = 16, k_i = 2; no Boue-Dupuis form is needed |

**Test (h), the mean-zero step.** Take a plaquette (x; mu, nu) of M with x in the cell C, cell coordinates
x_mu, x_nu in {0, ..., N - 1}. Its link tails are x, x + mu, x + nu, x. If x_mu, x_nu <= N - 2 all four tails lie in
C and the plaquette maps, with no wrap, to the plaquette (x mod N; mu, nu) of the torus of side N: mean xbar_N;
6 N^2 (N - 1)^2 per cell. If x_mu = N - 1, the link U = (x + mu, nu) has its tail in C' = C + e_mu; the links (x, mu),
(x, nu) lie in C, and (x + nu, mu) lies in C or in C + e_nu. C' differs from C and from C + e_nu when k_mu >= 2
(and k_nu >= 2 for the second). If x_nu = N - 1 and x_mu <= N - 2, U = (x + nu, mu) has its tail in C + e_nu and the
other three tails x, x + mu, x lie in C. So U is the only link of the plaquette in its cell. The copies are
independent, so the mean of (1/2) tr U_p is (1/2) tr of a product in which U enters through its matrix mean
E_(mu_N)[U]. The gauge transformation h at the tail y of U preserves mu_N and maps U to h U (the head y + nu or
y + mu differs from y, so no right factor h^(-1) falls on U); so E[U] = h E[U] for all h, and averaging over Haar
measure gives E[U] = 0. The other links of the cell C' that the transformation moves are not in the plaquette.
**Correction of scope.** If some k_mu = 1, the cell wraps in direction mu, the plaquettes with x_mu = N - 1 are
internal, and the displayed E_nu[A_M] is wrong. The lemma's proof only uses M = (N n_1, ..., N n_4) with n_i >= 3,
so state "k_i >= 2" in the setup.

**Rest of the proof.** Gibbs: log int e^(-beta A) >= int rho (- beta A) - int rho log rho (Jensen). Each cell holds
4 N^4 links (tails in the cell), in bijection with the links of the torus of side N; -Ent(mu_N | Haar) =
beta E[A_N] + F(N^4), E[A_N] = 6 N^4 (1 - xbar_N) (all plaquettes of the symmetric torus have the same mean). Then
F(M) >= K F(N^4) - 6 beta K xbar_N N^2 (N^2 - (N - 1)^2), |M| = K N^4, and Lemma A gives F(N n)/|N n| <= F(n)/|n|.
Taking the infimum over n and multiplying by N^4 gives the lemma; xbar_N <= 1 gives 12 beta N^3.

**Defect identity (ARGUED in the file).** For the N-periodic tiling state: entropy per site
(beta E[A_N] + F(N^4))/N^4, energy per site 6 - 6 (N - 1)^2 xbar_N/N^2. If h = f - (s - beta e) (the variational
principle for periodic states, recalled from Georgii Chapter 15 and not rebuilt), then
N^4 h = - D(N) + 6 beta (2N - 1) N^2 xbar_N. The algebra is right; the identification of h is the recalled part.

## State

Step 6 done. Next: step 7, the RESULT line of row 1031 against the verdicts; step 8, verdict table and RESULT.
