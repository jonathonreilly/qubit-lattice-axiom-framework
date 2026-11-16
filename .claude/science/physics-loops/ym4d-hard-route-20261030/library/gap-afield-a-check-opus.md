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

## State

Step 2a done (7.1). Next: step 2b, Proposition T23 (7.2) and Theorem CR^c (7.3), test (c).
