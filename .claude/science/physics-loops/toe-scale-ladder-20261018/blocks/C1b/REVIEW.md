# C1b review

**Reviewer:** a Claude subagent, same model as the author. This is not a different-model check.
**Date:** 2026-10-19.
**Scope:** I read all of NOTE.md (363 lines) and WORKLOG.md (173 lines), with C1/NOTE.md and C1/REVIEW.md as context.
- Code read: `ctqmc.py` (all), `sim.py`, `run_pt.py`, `exact_L2.py`, `validate_L2.py`, `validate_ti_L2.py`, `analyze.py`, `drift.py`, `energy_L8.py`, `queue.sh`, `jobs_C/D.txt`.
- Logs read: all three `validate_*`, `val*.chunk.log`, `analysis_*`, `drift`, `ti_estimates`, `posthoc`, `energy_L8`, `prod_chunks.jsonl`.
- Git history checked: `ctqmc.py` is unchanged since 03:01, so val3 (launched 03:02) and all production runs used the same kernel. The only later change to `sim.py` is the inert-by-default `noloop_sweeps` thermalisation switch.

**Writes:** only this file and `review_scripts/` (scripts, `logs/`, a numba cache). Along the way I accidentally created `scripts/__pycache__` (numba cache, gitignored) by importing the block code. I deleted it, and later scripts redirect the cache. No commits. Every job ran at nice 10 on one core, each under 6 minutes.

## Review scripts and logs

| script | what it does | log(s) end |
|---|---|---|
| `rs1_cube_move_db.py` | My own lattice, circulation test and enumeration of the **exact one-call kernel** of the cube move as NOTE §2.4 describes it. It checks that the kernel is symmetric, i.e. detailed balance w.r.t. uniform (all equal-n_F configurations have equal weight at V=0). It then runs the block's `cube_moves` (ntry=1) 4×10⁵ times and χ²-compares its empirical transition frequencies with my kernel row by row. A control repeats the kernel with acceptance 1 in place of min(1,N′/N). | L=2: `seed1_nF10`, `seed2_nF10`, `seed3_nF12` PASS=7 FAIL=0 each. L=4 (where N≠N′ occurs): `L4_seed11_nF12`, `L4_seed13_nF12` PASS=8 FAIL=0 each. |
| `rs2_nF_histogram_L2.py` | **Combined update set** (markers + super-clusters + loops + cube + PT, the block's `sim.PT`, run in memory) against an exact distribution finer than ⟨E⟩: P(n_F=n) and P(n_F=n, W=0) = βⁿTr_W(Aⁿ)/n!/Z. I computed these myself: own enumeration of 2²⁴ states, own adjacency and eigenvalues, giving 9600 states, 937 components and E0 = −9.0267209135. 11-β ladder, 10 min, about 4.6×10⁵ sweeps per run. | cube on, seeds 11, 12: **PASS=3 FAIL=0** each (max\|z\| ≤ 2.73). **Control, cube off:** **PASS=0 FAIL=3**, z up to 22, ⟨n_F⟩ z = −7.8, −21, −5.0. |
| `rs3_cluster_holonomy.py` | Claim 0.2(a) at L=2, mod 2, exhaustively. A cluster's time-slice set S obeys S → S⊕∂p, only if ∂p∩S=∅ or ∂p⊆S. A union of clusters obeys the same rule, because the 4 legs on one side of a vertex share a cluster. I compute the holonomy group of this graph over **all** 2²⁴ S(0). | `rs3_cluster_holonomy_v2.log` PASS=6 FAIL=0. v1 log kept (PASS=3 FAIL=1): its one FAIL was my own wrong conjecture (span(H) ⊆ span(planes)), not a C1b claim, and it was turned into INFO in v2. |
| `rs4_reproduce_validation_logs.py` | Recomputes `validate_L2_val2.log` and `validate_L2_val3.log` row by row from the raw validation files that the author moved to the session scratchpad. Provenance check only. | PASS=2 FAIL=0 |
| `rs5_cluster_conditional_db.py` | Re-run of the author's unkept §3.3 test: vertices frozen, cluster phase only, occupancy vs e^{−βĪ} with Ī from my own code, 20 batch means. | 4 of 5 logs PASS=1 FAIL=0; `seed1_b1.0_n400000` **PASS=0 FAIL=1** (χ² 63.2/31, p=0.001). See R10. |
| `rs6_cluster_kernel_balance.py` | The same frozen-vertex setting without autocorrelation. The kernel K(i→j) is estimated from M independent single sweeps per configuration, then global balance πK=π and pairwise detailed balance are tested. | `seed1_b1.0_M200000` (6.4M sweeps, the configuration where rs5 failed), `seed1_b1.0_M20000`, `seed3_b1.5_M20000`: PASS=2 FAIL=0 each. TV(stationary(K̂), π) = 0.0009. |

Exploratory runs that were not logged: rs1 at L=4 with only 2000 calls gave χ² FAILs, because many expected counts were below 5. The test is underpowered at that size, and the same configurations pass at 4×10⁵ calls. rs5 with 2×10⁴ sweeps passed at β=0.7 and 1.0.

## My own derivation of the stationary-measure conditions

- **Weight.** On the circulating subspace, −gσˣ = −g(1+σˣ) + g·1, so e^{−βH} expands into F (flip) and P (identity) vertices of weight g, plus e^{−gβĪ}. With P markers drawn as a Poisson process of rate gβ on circulating time, Σ_{n_P}(gβĪ)^{n_P}/n_P! · e^{−gβĪ} = 1, which returns the marginal (gβ)^{n_F}. This is correct.
- **Marker resampling.** This is an exact Gibbs step. Discarding the markers at the end of the sweep marginalises them. Correct.
- **Super-cluster flips.** A flip of cluster c negates c's contribution to Q_v, so |Q_v(c)| is invariant; free links always carry |Q|=1. The partition (including the giant-cluster skip, which depends only on segment counts) is therefore the same in the forward and reverse configurations. n_F+n_P is fixed, so the target ratio is e^{−gβΔĪ}. A heat-bath step at fixed partition is detailed-balanced, and a Gauss-illegal target has weight 0 and is rejected symmetrically. Correct. rs6 confirms it numerically.
- **Static ice loops.** The walk starts at a random v0 with a tail, and the tail is discarded. The loop links touch only vertex-free plaquettes, so no marker or event is affected. The reverse loop is generated with the same probability from the same (v0, tail):
  - tail vertices are off the loop, so their out-degree among free links is unchanged;
  - at loop vertices, one free in-link and one free out-link swap roles, so kc is unchanged;
  - the reverse walk closes at the same junction, because the forward loop avoided the tail.
  So the proposal is symmetric, and heat-bath in e^{−gβΔĪ} is correct.
- **Cube move.** The configuration is selected as (e1 uniform among n_F events, c uniform among the 2 cubes of fp[e1]). T is the next two events that touch c's 12 links. Nothing else in the window touches those links, so relabelling T→T′ (T∪T′ = ∂c) leaves every other event valid and leaves the state after the window unchanged, because ∂c flips each link twice. The reverse move from Y uses the same (e1, c) and the same window. c is unique, since no other cube has face set T∪T′, and the state before e1 is unchanged.
  - **N and N′.** These are the numbers of orderings of T and of T′ that are valid sequentially from the cube-link state just before e1.
  - **The proposal is not symmetric.** q(X→Y) = 1/(2n_F N′) and q(Y→X) = 1/(2n_F N). The Metropolis–Hastings acceptance is therefore min(1, N′/N), which is what `cube_moves` implements: `random()*Nv < Np_`, then a uniform pick among the valid T′ orders.
  - **Weights.** At V=0 the weights are equal (n_F is unchanged), and the move is correctly restricted to V=0. N≠N′ does occur. Enumerating all 2¹² cube-link states and all 20 triples T gives 1152 cases with N≥1. Of these, 96 have (N,N′) = (1,2), 96 have (2,1), and 192 have N′ = 0 (no move). This was an unlogged inline check. The rs1 control shows the factor is needed (kernel asymmetry 2.1×10⁻²), and the block's code matches the exact kernel that includes it.
- **PT.** The configurations are in u units, so w ∝ β^{n_F}. The swap ratio is (β_j/β_i)^{n_a−n_b}, and the V≠0 branch −V(β_j−β_i)(Ī_i−Ī_j) is also correct. The energy estimator is E = −⟨n_F⟩/β.
- **TI identity.** H conserves W, so d ln Z_S/dβ = −⟨H⟩_S is exact.
- **Round trips.** The code counts lowest→highest passages that follow a visit to the lowest β. This is the standard round-trip count, to within ±1 per walker.

## Per-claim verdicts

| # | claim (NOTE §) | verdict | severity | evidence / fix |
|---|---|---|---|---|
| R1 | The weight representation, markers, super-clusters, loops, cube move and PT satisfy detailed balance (§2, §0.1) | **correct** | — | Own derivation (above). Numerically: rs1 (cube move alone, L=2 and L=4), rs6 (cluster phase alone), rs2 (everything combined, P(n_F, W=0) at β = 1, 2, 4). |
| R2 | Cube move: acceptance min(1,N′/N), window rules (§2.4, §9.1) | **correct** | — | rs1: block transition frequencies vs my exact kernel give χ² 1037.5/1056 and 24.5/32 at L=4, and 637.1/624, 719.1/624 (p=0.005) and 1058.4/1088 at L=2. The kernel is exactly symmetric and the class is irreducible. At L=2 none of my configurations had N≠N′; L=4 was needed to exercise the factor. **Suggestion:** state in §2.4 that N′/N is the Hastings correction for the 1/N′ uniform choice. |
| R3 | V1 validation: val3 PASS=25 FAIL=0, TI PASS=10 FAIL=0 (§0.1, §3.1) | **correct with fix** | minor | rs4 reproduces val2 and val3 row by row from the raw files, and rs2 adds an independent, finer check. **Fixes:** (a) the raw validation files (125 MB) are only in the session scratchpad, which is not durable, so state that only `val_bins_L2.npz` summaries remain in the repo; (b) the spline quadrature was chosen after the trapezoid failed on the same val3 data, so the TI 10/10 is a consistency check, not an independent validation of that choice. The NOTE discloses the choice but should say this. |
| R4 | val2 log preserved; "8–27σ bias" (§0.2a, §3.1) | **correct with fix** | nit | The log is preserved (PASS=16 FAIL=9) and rs4 reproduces it. The failing z values span 3.4–26.6, and E specifically spans 5.4–26.6, not "8–27σ". At β=2, W², P0, N_c and S also fail. |
| R5 | Clusters alone cannot generate the elementary-cube class (§0.2a, §3.2, labelled [THM + NUM]) | **correct with fix** | minor | rs3, at L=2 mod 2 and exhaustive over all S(0): the cluster holonomy span has dimension 9 out of dim Z = 10, contains **no single cube**, but contains **every sum of two cubes** and all 6 planes. So the obstruction is a **Z₂ invariant (parity of the cube number)**, not a locality limit. The NOTE's justification ("sweeping a cube needs XOR updates…") is heuristic, not a proof. The super-cluster remark is right, because a union of clusters obeys the same add-disjoint/remove-contained rule. rs2's cube-off control shows the resulting bias. **Fix:** relabel as [NUM; exhaustive at L=2 (review rs3)], state it as an odd-cube-number obstruction, and keep general L as a conjecture. |
| R6 | Loop-proposal symmetry, ΔĪ bookkeeping, marker intensities (§3.3) | **correct** (derivation) / scratch tests **unverified** | nit | The symmetry argument checks out (above). The scratch tests t8, t18 and t24 were not kept. |
| R7 | Conditional DB at fixed vertices "χ² = 19.5/19, and 66.6/31 after 4× longer" (§3.3) | **cited evidence incorrect; underlying claim correct** | minor | 66.6/31 has p = 2×10⁻⁴; it is a failure, not support. A χ² that grows with run length is the signature of bias. My rs5 reproduces the same pattern on a 32-state configuration (39.8/25 → 63.2/31). The autocorrelation-free rs6 test on that same configuration, at 16× higher statistics, passes (global balance χ² 24.9/31; detailed balance 508.6/496), so the chained batch-mean statistic is unreliable and there is no bias. **Fix:** drop the 66.6/31 citation or call it a failed test, and cite rs6 instead. |
| R8 | Event-free-start trapping; compromised runs excluded (§0.2b, §5.1, §6) | **correct with fix** | minor | The mechanism is consistent with DB: at n_F=0 all base states have weight 1. The fix changes thermalisation only. The verdicts do not use L4_s1/s2 or L6_s1/s2. **But** the exclusion is post hoc: under the declared EQ rule, L4_s1/s2 at β=4 **pass** (W² z = −0.38, 27/24 trips). **Fix:** label the exclusion [POST HOC deviation from EQ]. It does not change the verdict (see R10). §7 still uses compromised runs (dF2/dF1) under a "No evidence of confinement [NUM, weak]" heading. Relabel that heading [POST HOC]. |
| R9 | Drift table; EQ fails at β=L for L=4 and 6 (§5.2–5.4, §6) | **correct** | — | `drift.log` matches §5.2 entry by entry, and `analysis_L4_clean.log` gives W² z = −3.00 and S1 z = −2.24. L=6 clean has one start and 0 trips; L=6 compromised has W² z = −3.42. |
| R10 | C-W / X-W **INCONCLUSIVE**; S_T exponent not evaluable; overall INCONCLUSIVE (§0.4, §6) | **correct** | — | No two L have EQ-passing β=L points. The verdict is robust to R8: applying EQ mechanically to the compromised runs passes L=4, but L=6 still fails, and the compromised fit s = −0.52(10) matches neither C-W nor X-W. "NOT EVALUABLE" equals the declared "otherwise inconclusive"; nit: use the declared word. |
| R11 | Post hoc S_T exponent p = 0.93(5) labelled invalid (§5.4, §6) | **correct** | nit | It is clearly labelled [POST HOC] and "not a valid evaluation". Arithmetic: p = 0.925, with error 0.058, so 0.93(6). The clean vs compromised S1 shift is reproduced at 5.0σ. |
| R12 | "Equilibrated-looking" L=4, β=L/2: P1 stationary, dF1 = 0.505(25) (§0.5, §5.3) | **correct with fix** | **moderate** | The per-run values are reproduced: 0.510(34)/0.500(28), weighted 0.504(22). Not stated in the NOTE: (a) the compromised runs give dF1(2.05) = 0.394(24), which is 3.4σ lower at the same β, so β=L/2 is also start-protocol-sensitive; (b) the s4 chunk-0 P1 is 0.477 (§5.2), but the §5.3 table says "0.39–0.43". By the NOTE's own logic (start agreement is not proof), this point is "consistent between two clean starts", not "equilibrated". **Fix:** add (a) and (b), and soften "stationary in every chunk". |
| R13 | L=4, β=4 last-chunk dF1 ≈ 0.88 [POST HOC] (§0.5) | **correct** | — | Arithmetic: P1 = 0.0565 gives dF1 = 0.877. It is labelled post hoc. |
| R14 | L=4 E(β=8) = −56.20(6), consistent with C1's −56.253(45) (§0.5, §8) | **correct** | — | `analysis_L4_clean.log` gives −56.197(55). |
| R15 | L=8: E(β=16) = −443.4 ± ≳0.5, which does not discriminate C1's −443.83(14) from the repo's −443.364(31) (§0.5, §5.5) | **correct** | — | `energy_L8.log`: binned error 0.31→0.43 and fifths −444.8…−442.3, whose standard error is 0.42, so "≳0.5" is fair. The difference between the references is 0.47, about 1σ, so the run cannot discriminate. The one-sided logic (⟨H⟩ ≥ E0 for any stationary sector-restricted ensemble) is sound. One start, W stayed 0, compromised attempts L8E_s1/s2 discarded. |
| R16 | Production code = validated code (§3.1, WORKLOG 03:35) | **correct** | — | `ctqmc.py` mtime is 03:01, before the val3 launch, and is unchanged in git after 04:10. The `sim.py` diff after validation adds only `noloop_sweeps` (default 0). |
| R17 | TI vs direct "not established at β ≥ L" (§6) | **correct** (wording) | nit | Within each run TI and direct agree, e.g. s3 0.805/0.824 and s4 0.620/0.648. What disagrees is the start. "Shows the W=1-sector energies of s4 are not equilibrated" (§5.3) should read "of at least one run". |

## Summary of required fixes

1. **Moderate (R12):** β=L/2 dF1 also differs by 3.4σ from the compromised runs, and P1(s4, chunk 0) = 0.477. Downgrade "equilibrated-looking" to "agrees between two clean starts".
2. **Minor (R5):** give the cube obstruction its exact form, Z₂ parity (an odd number of cubes), shown exhaustively at L=2 (rs3). It is not a proven [THM] for general L.
3. **Minor (R7):** the χ² = 66.6/31 citation is a failed test. Replace it with an autocorrelation-free check (rs6 passes).
4. **Minor (R8):** label the exclusion of the compromised runs a post hoc deviation from EQ (verdict unaffected), and label §7 [POST HOC].
5. **Minor (R3):** the raw validation files are not durable, and the TI spline was tuned on the validation data.
6. **Nits:** R4 (z range), R10 (use "inconclusive"), R11 (0.93(6)), R17 (wording).

**No claim on which a verdict rests is incorrect.** Detailed balance of every move holds by derivation, and three independent numerical tests confirm it, including the N′/N factor of the cube move at L=4. The INCONCLUSIVE verdict is correct and robust. Not done by this review: a check at L ≥ 4 against an independent method (NOTE §9.1), and any test of winding-sector ergodicity beyond L=2.

## Correction confirmation (2026-10-19)

**Who and what.** The same reviewer (a Claude subagent, same model as the author) read the complete corrected NOTE.md (391 lines), including its "Review dispositions" section.

**Per finding:**

| finding | resolved? | where |
|---|---|---|
| R12 (moderate) | yes | §0.5 (3.4σ against the compromised runs, P1 = 0.477, "not shown to be equilibrated") and the dispositions |
| R5 | yes | §0.2(a) label, §3.2 "Exact form" paragraph |
| R7 | yes | §3.3 |
| R8 | yes | §0.2(b), dispositions, §7 heading [POST HOC] |
| R3 | yes | §11, dispositions |
| R10 | yes | §6 |
| R4, R11 | in dispositions only | see below |

**The three items left as they are:**
1. **"8–27σ" in §0.2(a).** Acceptable. The dispositions give the correct range (3.4–26.6, and 5.4–26.6 for E), and the val2 log is cited. It is a nit, and an inline edit would be cleaner.
2. **"0.39–0.43" in §5.3.** Acceptable. The dispositions say the range applies only to later chunks, and §0.5 and §5.2 both show 0.477.
3. **"stationary in every chunk" (§0.5; also "At β = L/2 the populations are stationary", §5.2).** Acceptable but loose. The same §0.5 bullet now says the value "is not shown to be equilibrated" and quotes the 0.477 chunk, so a reader is not misled. **Suggestion:** "approximately stationary (0.39–0.48)".

**New defects.** None that affect any verdict. Remaining nits:
1. The post hoc p is still 0.93(5) in §5.4 and §6, while the dispositions say 0.93(6).
2. The §3.2 heading still reads [THM + NUM].
3. The R17 wording ("in s4") is unchanged in §5.3.
4. The dispositions say the review confirmed "detailed balance of all moves with independent exact kernels". In fact the loops were checked by derivation and by the combined test rs2, the clusters by an estimated-kernel balance test (rs6), and only the cube move against an exact kernel (rs1).

**Final verdict: READY.** The overall INCONCLUSIVE verdict and every claim a verdict rests on are unchanged and consistent with this review.
