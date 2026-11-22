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
