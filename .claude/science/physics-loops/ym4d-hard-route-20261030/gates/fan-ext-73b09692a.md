lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T15:45Z

# Gate: `library/fan-ext.md` Sections 1 to 8, pinned at 73b09692a

Provenance: claude-opus-5-5, effort high, commit 73b09692a, side mapped, Mac mini worker, fresh session. A same-model check is not independent in model and is not an audit. The author of the target is another provider (OpenAI Codex), so this is a cross-provider read. Verdicts steer research and grant no status. Finished report.

**Result.** No WRONG. Every displayed step of Sections 1 to 8 was redone by hand, and no L or fine depth enters C_0 or the rate. The flat statements stand on the brick tilings, with three local defects below. One kill run (T2) failed its written numeric rule; that is not a refutation, see Numerics.

## Verdicts

| Statement | Verdict | Note |
|---|---|---|
| Refutation of the literal condition r^(k)w = 0 on Y, L/[8(1+4 pi^2)] | ADVANCE | Numbers redone. It also holds at every depth: ||D_h r^(k)w||_N <= ||Dw|| by (7.1), so fine freedom does not rescue it |
| Correction to (1.1) | ADVANCE | Equals r_N of `fibre-propagator.md`, Setting. Checked {omega : Domega in ker bC, zero parent means} = ker r_N |
| Mean correction (2.1), (2.2), Poincare (2.3) | ADVANCE | Bump, B_0, B_1 and path count redone. Parent scale only; no L |
| Cover and pattern list, Section 3 | ADVANCE, D1, D2 | (3.1) matches Lemma BG. Residue argument redone for any pair of branches through their first split, including m_k above and below that split. Catalan counts 1, 1, 2, 5, 14 |
| Tree reflection (4.1) to (4.6) | ADVANCE | T bijective, Lip 8 and 2, R_S Lip 5, K = 80, M = 328, nu, C_R, the path lemma, and the claim that sites stay in a leaf until one crossing edge between two S leaves |
| Gluing and mean restoration (5.1) to (5.3) | ADVANCE | T_* = 328, J = 1328, support of outputs inside the chart, edges used are real Omega edges, B count, a > rho case. Correction after the partition, as required |
| Bounded fine lift (6.1) to (6.5) | ADVANCE | r^(k)Jv = v exactly; h^2 in (6.2) cancels B_1/h^2 |
| Flat torus (7.1) to (7.7) | ADVANCE | Rows agree with Lemma 1 of `block-poincare-energy-package.md`: tri times box. b(q)delta(q) = exp(iq) - 1 checked. The alias sum is avoided as claimed |
| Flat D-coer (7.8), (7.9) | ADVANCE | x^2 inequality and Young steps redone. C_0 is absolute |
| Row lift (8.1), saddle (8.2) | ADVANCE, D4 | Moments, bounds, triangular correction, Riesz recovery of lambda. ||bC|| does not enter |
| Mean bound (8.3), commutators (8.4), rate (8.5) | ADVANCE | Table constants rebuilt: rows 16 sqrt(2) delta, curl under 10 delta, P_N D* under 64(1+K_m) delta. 2^20 has ample margin |
| Decay of S_N^-1 in (8.5), class solution P_N D*H = 0 | ADVANCE | |
| Chart bound and Schur reading in (8.6) | implication | D3: rests on `fibre-propagator.md` (iv), (v), not on Section 8 |

**Where C_0 could hide L or depth.** Traced link by link: Q to D_h u uses (7.1), density norm, no L. Poincare is on unit parents with internal edges only. Extension is in parent units; the tent scale rho is absolute. The lift has absolute constants, with a single interpolation not iterated by level. The torus estimate holds at every eta. With the printed constants, log2 values are A_ext 167.5, C_T 36.2, C_0 229.9, M_0 723.9, delta_flat -764.9. These are displayable powers of two, chosen in the order K, M, rho, C_R, A_ext, a_0, a_1, C_T, C_0, K_b, M_0, C_com, delta_flat, then L. No circle: nothing before L reads L, b or eta.

## Defects

None breaks a statement of Sections 1 to 8.

1. **Handoff to BG's radius, for consumers.** Section 3 supplies radius b/64, and its argument works for any cube of side < b/8, so radius strictly below t_0/16. It does not restore BG(b) at t_0/8. Readers: `energy-by-stages.md` (EXT-d) at "radius at most t_0/16", which needs strict inequality; `lift-nonlinear.md` at r_* <= t_0/16, same; `quiet-boundary-rarity.md`, Lemma J, "a ball of radius t_0/8 ... meets at most d + 1 bricks". For Lemma J, random search found 6 bricks in an open ball of radius b/8 in d = 4 (`t4.log`), so that sentence looks false; this is a run, not a hand example, and none is written. Repair, unproved in Lemma J's text: r_0 := t_0/(64(d + 1)), so the chain sits in a cube of radius b/64 and Section 3 gives at most 5 leaves. Only the bounded rank is used there. Consumers should cite Section 3, not BG(b).
2. **Unstated torus hypothesis.** "Compatible local periodic lifts" has no condition. The tiling (3.1) descends to a torus only when the side is a period. By hand from (3.1): b in coordinate 1 and 2b in coordinates 2, 3, 4 suffice; Section 1 checks only 8b. Add this to the hypotheses of (5.3), (7.9), (8.5). Not checked against the torus side of any consumer.
3. **Label of (8.6).** Section 8 marks (8.6) discharged, but two inputs come from `fibre-propagator.md` (iv), (v), through "The chart: as (iv)": that J_i annihilates D(ker r_N), which Section 8 never says, and that xi coordinatizes classes, which the Schur reading M_Y^-1(i, j) = xi_i(H_j) needs. I checked the first in the flat case: X moves by D_k(omega_k - chi_k[ev omega_k]), with parameter zero on Omega and at centres, and the tree gauge removes it. I read but did not rebuild the second. Repair: display both, or label (8.6) implication.
4. **L >= 4 K_b is more than is used (not an error).** Only L >= 32 enters, for the site count; the bound K_* already holds, since sqrt(2) K_b / L is at most order K_b at L >= 32. And the text's own count needs K_b about 2^47, not 2^120, which gives delta_flat about 2^-473. So a reader need not budget L >= 2^122. A search of the mapped file, `fd-local.md` and `lc-u.md` found no upper bound on L.

## Numerics

Criteria first in `checks/gate_fan_ext/CRITERIA.md`, with three dated amendments. Runs refute or guide. None discharges anything.

| Test | Outcome |
|---|---|
| T1 tree cover and reflection, all 1890 patterns | PASS. Sampled, so it proves nothing |
| T2 optimal corrected extension A(L), d = 3, balanced fan | **FAIL by the written rule.** Fan A = 1.925, 2.455, 2.754, 2.959 at L = 4, 8, 12, 16, so A(8)/A(4) = 1.275 > 1.25; A(16)/A(8) = 1.205. Flat control 1.458, 1.670, 1.766, 1.819, under its hand bound 2 |
| T3 flat C_0, d = 2, in L and depth | PASS. 0.1064, 0.1062, 0.1071, 0.1078 at L = 4, 8, 16, 32; 0.1054, 0.1055, 0.1056 at depth factors 2, 4, 8. No fan in d = 2 |
| T5 d = 2 re-entrant corner | Nearest clause passes: A = 1.52 to 2.79 at L = 4 to 128, increments falling from about 0.27 to 0.20. L = 256 hit the 2 GB stop, so the clause as written has no value |
| T6 edge against fan; literal control | PASS. Literal condition 1.562, 2.443, 4.309 at L = 2, 4, 8: the test does see an L loss when there is one |
| T7 energy factor of R, guide | Sampled kappa about 15.9 on the balanced fan, at most about 33 over all patterns; Euclidean Lip of R about 4 to 6 |

**Reading T2.** The fan's A rises about 0.52 per doubling, close to log L over this short range, and this is not fully explained. An edge with openings 3 pi/2 and pi/2 explains half of the slope: the edge pattern equals the d = 2 corner at L = 4, 8, and Mellin analysis of that corner gives a limit of 4 from below, slowly. Fan minus edge is 0.40, 0.63, 0.78, 0.87, still rising. The top mode at L = 16 sits near the vertex and edges across several octaves. No evidence of a break: u o R gives the continuum Dirichlet bound A <= 1 + kappa, about 17 on the sampled kappa, before mean corrections, and the hand bound (5.3) is the only actual bound. At this slope the guide value would be reached at L about 2^31, so these sizes cannot test it, and a run cannot show a limit either way. L in d = 3 stopped at 16 by memory; d = 4 was not run.

Void, kept for the record: my first T2 values, in `void/` and quoted in the first amendment, were wrong. They exceeded the hand bound 2 because rounding off ker C_O was amplified in Lanczos. Fixed, then matched to a dense solve at L = 4, 8.

## Read and not read

Read: `FINISH.md`, `GOAL.md`; `library/fan-ext.md` lines 1 to 858, without Sections 9 to 11; `library/fibre-propagator.md` lines 40 to 175; `library/block-poincare-energy-package.md` lines 1 to 60; `library/fd-local.md` lines 95 to 140; `gates/dcoer-codex-e0c0b9a6f.md`, table and items 1, 2, plus search hits. The queue rows of `FINISH.md` state fan-ext's claims, so they were seen before the hand check, as was one cut line of its Section 11 in a search hit. Its verdicts in Section 11 were not read.

Firewall: one `grep` for BG ran over `library/*.md`, which includes files forbidden on this side. No line from any of them appeared in the output and none was opened. Nothing else from the independent attempt was touched. `gates/history-budget-*`, `compute-inventory-*`, `strategy-*` and the Sussman-Alpoge repository were not read.

Not done: background statements, Sections 9 to 11, clearance between retained levels, consumers beyond the lines cited in D1, and the numerics of the rate.
