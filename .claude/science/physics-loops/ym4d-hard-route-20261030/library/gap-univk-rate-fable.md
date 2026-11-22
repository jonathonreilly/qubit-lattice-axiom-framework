lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-23T00:40Z

# Row 1391, gap-univk-rate-fable: the ultraviolet carry (UNIV-K) in rate form, hypothesis (A1) of Theorem T

Started 2026-11-22T12:40Z (date -u), pinned at commit a1f83f4da. Worker file, not checked by another model. Research-stage working state; no status.

Moves: hypothesis (A1) of Theorem T (row 1332, `library/gap-shrink-box-fable.md` section 4.4; check 1335), which is also uniqueness of the continuum limit at a fixed physical size.

Credit: the account read here is YM4_1400.tex by Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Rows 924 and 925 (`library/gap-univk-opus.md`, `library/gap-univk-check-astra.md`) are the prior work this row builds on.

## Plan (written before any reading beyond FINISH.md and GOAL.md)

1. Repo search: rows 924, 925, 1332, 1335, 1386 and `library/open-core.md` for (UNIV-K), (A1), (MAPCONV), (VAC-ID), (DENS-K), (CLASS).
2. State (A1) in the rate form that Theorem T reads, with the dependence on ell.
3. For each of (MAPCONV), (VAC-ID), (DENS-K), (CLASS): find the account's passage, quote it, classify as proved / sketched / assumed.
4. Attack: prove (A1) in rate form as an implication from statements the account proves, or name the first input that fails with the explicit failure.
5. Equivalence test (rule "Equivalent is not progress") on any sufficient statement proposed.
6. Next two rows and their decisive outcomes.

Each step is appended below when it is done.

## Step 1. Repo search and prior work (written 12:43Z by date -u)

Search done inside this lane folder only. `origin/main` and the PR branches are not refs in this checkout, so the wider "Repo first" search was not run here; check 925 ran it on 2026-11-14 for these labels and found no hit outside this lane (`library/gap-univk-check-astra.md` L3-L46).

`library/open-core.md` has no entry for (UNIV-K), (MAPCONV), (VAC-ID), (DENS-K) or (CLASS) (grep, zero hits). FINISH rows that carry (UNIV-K): 916, 917, 924, 925, 978, 1225, 1229, 1233, 1237, 1238, 1240, 1242, 1248, 1263, 1326, 1331, 1332, 1335, 1340-1351, 1386. What they leave on file for the four inputs:

| Input | On file | Row |
|---|---|---|
| (CLASS) | Proposition 3.3 of row 1237 holds as an abstract tuning lemma; its application to the two runs FAILS (the account proves tuning for one frozen presentation) | 1237, check 1240 |
| (MAPCONV) | The account proves depth convergence only for the Taylor orders 2-4 of the classical action at the flat reference, the Gaussian polarization, and b_j, m_j. The rest is split into (M1) background map, (M2) Gaussian pointing, (M3) formation map; none is in the account | 1238 (unchecked on this point) |
| (VAC-ID) | Reduced to the account's Statement 3.4 (common companion, L84159-84204, an open input of the account) and the class bounds; Lemma VAC | 1248, check 1263 |
| (DENS-K) | B1 (extra bare level) and B2 (matched levels) open; the exponent of p_0 exceeds 8, so B1's arithmetic premise holds | 924, 1248 |
| Edge matching | The predecessor must be a first-passage datum; open | 925, 1242 |
| One-sided form | (ONE-K) needs only Phi(d) - Phi(pi d) <= (L^4+1) eps_K | 1238 Lemmas 3.1-3.2 |

Row 1238 Step 2.7 says that no text of the account states the two-cutoff comparison, and that YM4_SI makes it a hypothesis. That search was a grep of the nine submanuscripts. **It missed the account's own two-cutoff text inside YM4_1400.tex:** the subsections "Coupling coordinates and conditional comparisons" (L126164-131280) and "Weighted derivatives and matched presentations" (L131281-135994). No gap-lane file cites their matched-run statements (grep for "terminal-coupling", "partnered run", "matched limit", "geometric relabelling" in `library/gap-*.md`: the only hits are unrelated uses; row 1248 read L126169-126198 for the vacuum accounting only). These 9,800 lines are the account's treatment of exactly the object of this row. Steps 2-4 read them.

## Step 2. The account's own two-cutoff text: first reading (written 12:46Z by date -u)

Source: YM4_1400.tex (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of its text), the copy at LOCAL:ym4d-papers/sa1400, 136,637 lines. "L n" is a line of that file. READ in this step: L126164-126330, L126377-126470, L130770-131110.

**2.1 The account says that its matched-cutoff estimates are hypotheses (READ L126170-126177).** The subsection "Coupling coordinates and conditional comparisons" opens: "The coupling, matched-run and Ward estimates below imply their stated conclusions by elementary analytic arguments. The interacting estimates themselves remain hypotheses." and ends its first paragraph: "None computes the one-loop trace or proves a matched-cutoff or typed Ward estimate." So the status of the two-cutoff comparison in the account is: **assumed** (a stated input of a conditional proposition), with a long sketch of how the inputs would be produced (L126445-130770, L131685-135912).

**2.2 The form of the account's matched comparison (READ L126377-126419, (CP8)-(CP9)).** Fix a torus T_ell, h = g^-2 and a separated tuple of n >= 2 tests. beta_K^nat is the torus-independent tuned bare centre, Xi_K(t) = x_K^nat(beta_K^nat - t) the terminal coupling at offset t, n_K = Xi_(K+1)^-1 o Xi_K the matching map. The required inputs are
  |n_K - t| + |n_K' - 1| + |Xi_(K+1) - Xi_K| <= C eta_K,
  |F_(K,n)(t) - n_K'(t)^n F_(K+1,n)(n_K(t))| <= C_(n,ell,f) eps_K,   sum_K (eta_K + eps_K) < infinity,
with F_(K,n) the n-point function at cutoff K. "Constants and cutoff floors may depend on this fixed ell." "Often eta_K = Upsilon_K <= C K^(-3/2) (log(2+K))^(p+1); a separate remainder error Pi_K is part of eps_K". The matched scalar increments are to obey (L126432-126436) sup_t |b^B_[u](n_K(t)) - b^A_[u](t)| <= C (rho^(K-u) + Pi_K), where "Pi_K is the error from the unmatched large-field terms at the bare end".

Three facts follow for this row.
- (a) The comparison is between cutoffs K and K+1 at **matched terminal coupling**, as rows 916 and 924 proposed. It is stated for n >= 2 separated tests on one torus. The zero-source two-torus quantity Phi is not in (CP9).
- (b) The dependence on ell is left free ("may depend on this fixed ell"; the strip has height c rho e^(-C(g) ell^4), L126407-126410). (A1) asks for C_U ell^4.
- (c) **The rates are polynomial in K, not geometric.** eta_K is of order K^(-3/2) up to logarithms, and Pi_K is polynomial in the account's own example (next item).

**2.3 The account's own warning on geometric rates (READ L130953-131103, "Why a geometric relabelling needs another construction").** The account gives the three-number example F_K(t) = (1, 1 + t, 1 + Pi_K), Pi_K = K^(-q), q > 1: all summable matching inequalities hold, and no reparametrisation and common normalisation make the increments geometrically small. It then bounds the difference of the transferred coefficients of two cutoffs (L131036-131076): the remainders born at depth s from the terminal lattice compare with a geometric factor rho^(K-s), but the terms born near the bare end have only their one-run size, so "a geometric comparison at each fixed depth may still yield a polynomial error for the sum of the transferred coefficients"; the bound is O(r-hat_K) with r-hat_K "of order theta_[K]^(2 - kappa_0/2) times a power of its logarithm", "summable for kappa_0 > 6". Here theta_[K] is the bare inverse coupling, which grows linearly in K.

So in the account's coordinates the two-cutoff error that the account aims at is a negative power of K. The reason is structural: the remainders and the large-field weights at the bare level are small only by a power of the bare coupling (g_0^(kappa_0), e^(-c p_0(g_0))), the bare inverse coupling grows only linearly in K (asymptotic freedom), and the terms born within a bounded number of steps of the bare end are not matched between the two runs.

**2.4 Consequence for the rate form (A1) (ARGUED from 2.2-2.3; made exact in Step 5).** (A1) asks eps_K <= C_U ell^4 q^K with q < 1. The account does not aim at this rate. Its own target gives, at best, eps_K <= C_ell K^(-r) with r > 1. So "prove (A1) in the geometric rate form from statements the account proves" has two separate failures: the comparison is assumed, not proved (2.1); and the rate the account sketches is polynomial (2.3). Step 5 shows which rate the consumer really needs.

**2.5 The account's use of the comparison (READ L130770-130952).** Proposition "The conditional terminal-coupling limit" (L130770-130795): the inputs give convergence of F_(K,n) without a subsequence, at each terminal coupling x. The first-passage application (L130814-130853) needs "a live frozen run of length K' from the same bare value, in the admitted real tuning class" (input E4), and "The comparison between the ordinary and the frozen bookkeeping, including admission of the frozen run, is the input to this argument." The two-run coupling comparison is required in the form (L130872-130877) |x^[i+1]_[s] - x^[i]_[s]| <= C (L^(-c(i-s)) + s Pi_i), sup_(s>=1) s sum_(i>=s) Pi_i < infinity. This is the account's version of (MAPCONV) for the scalar coupling, and it is a requirement, not a theorem.
