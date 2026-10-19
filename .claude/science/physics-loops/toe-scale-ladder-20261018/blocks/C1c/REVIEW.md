# C1c REVIEW

**Reviewer:** a Claude subagent, the same model as the author. This is not an independent-model review.
**Date:** 2026-10-19, 16:48–17:05 UTC. The review had a 45-minute budget and used light CPU only.
**Inputs read:**
- `NOTE.md` and `WORKLOG.md`;
- the C1b criteria: C1b WORKLOG 01:32/03:40 and C1b NOTE §4;
- `logs/analysis_L4_L6_final.log`, `energy_L8_final.log`, `drift_L6.log`, `drift_L4.log` (head), `posthoc_chunk_errors.log`;
- `scripts/energy_L8.py`, `jobs_C1c.txt`, `launch.sh`;
- the repo source note of −443.364;
- C1 NOTE and REVIEW lines on the 8³ energy.

**Reviewer scripts** (in `review_scripts/`, read-only on the data):
- `rev_criteria.py` recomputes every criterion number from the tabulated per-run values;
- `rev_L8_binning.py` does a full binning and Sokal τ_int analysis of the L=8 raw series;
- `rev_window.py` is a [REVIEWER POST HOC] half-series sensitivity check of P1(β=L), using the per-chunk drift logs.

**Provenance check:**
- The sha256 values of all C1b scripts in `scripts/` match `blocks/C1b/scripts/` and `data/source_hashes_C1b.sha256`.
- `worker.sh` is present and new, as the NOTE states.
- All numbers in NOTE §2 and §3 agree with the logs.

## Per-claim verdicts

### (1) EQ rule applied as declared: **CORRECT as applied, but passing it here is weak evidence (see the major point)**

The declared rule is: at least 2 starts; E, ⟨W²⟩ and S_T(q1) agree within 2.5σ; at least 10 PT round trips per run. I recomputed the z values from the per-run values in the log.

| point | E z | ⟨W²⟩ z | S_T z | trips | declared outcome |
|---|---|---|---|---|---|
| L=4, β=4 | +0.25 | +0.42 | +0.04 | 71 / 78 | PASS. The NOTE is correct. |
| L=6, β=6 | −2.30 | +0.81 | +0.10 | 29 / 32 | PASS. The NOTE is correct. The combined E error 0.15 is the seed scatter (0.145), which is larger than the binned error (0.063). That is the declared max rule. |
| L=6, β=3 | +0.14 | **−3.66** | −0.40 | 29 / 32 | FAIL. The NOTE is correct, and it does not use this point. |

**Major point.** C1b already showed that this EQ test can pass while the populations are still drifting (C1b NOTE §5, the L4_s1/s2 case). C1c's own L=6 drift log repeats that pattern:
- In L6_s3 (the W=0 start), P1(β=6) is ≤ 0.02 in 13 of its first 14 chunks, up to about 47k sweeps. Then it sits at 0.06–0.14 for most of chunks 14–23.
- After the 20% discard, the first half of L6_s3's retained series has a mean P1 of about 0.014. The second half has about 0.081, a factor of about 6.
- In L6_s4, P1 is 0.000–0.003 in 4 of its last 5 chunks.

In that light, the NOTE has two problems:
- The headline wording "What equilibrated" (§0.1) should read "what passed the declared EQ test".
- The sentence "neither run shows a monotone trend after the first few chunks" (§2.1) is not accurate for L6_s3. Its P1(β=6) has a step change after about 14 of its 24 chunks.

The NOTE does flag the L=6 equilibration as marginal (§4), so this is a wording and emphasis problem, not a hidden one.

### (2) Recomputed criterion numbers: **ARITHMETIC CORRECT; reading "contradict → no phase verdict" CORRECT; post hoc material CLEARLY LABELLED**

| quantity | from the logs | reviewer recomputation |
|---|---|---|
| a(4), a(6) | 2.768(85), 3.76(16) | 2.768(84), 3.759(156) |
| s (direct) | 0.495(90) | 0.495(89): 5.6σ |
| s (TI) | 0.60(12) | 0.60(12): 4.9σ |
| K(6)/K(4) | 0.394 | 0.394(65): 1.6σ below 0.5. With chunk errors it is 0.40(7). |
| p | 1.131(24) | 1.131(24). That is 11σ below 1.4 and 19σ below 1.6. The NOTE's "20σ" is loose but harmless. |
| dF1 decrease 4 → 6 | 2.0σ | 1.96σ |

**How each declared criterion reads:**
- **C-W fails.** |s| is not within 2σ of 0.
- **X-W is met as declared:**
  - s > 0 at more than 3σ for both estimators, so the 03:40 addendum is satisfied;
  - K(6)/K(4) < 1/2. The declared rule gives no significance threshold for this ratio, so applying the point estimate is a fair reading. The NOTE also discloses the 1.6σ.
- **S_T: p is in the Coulomb window.**

The declared criteria contain no rule for combining these probes. Reporting both and giving **no phase verdict** is therefore the correct, conservative reading. Picking either probe would be a post hoc choice.

**Labelling of post hoc material.** The material in §0.4, §2.1 (chunk errors) and §4 is labelled [POST HOC] in every place. That includes the argument that "a linear-in-L slope test is passed by a constant dF1", which is physically correct (Coulomb: a is constant; string tension: a ∝ L²; constant dF1: a ∝ L). It also includes "S_T is more robust".

**[REVIEWER POST HOC, not a criterion evaluation] Window sensitivity.** This is computed from unweighted chunk means of P1(β=L), with the same 20% discard, in `rev_window.py`. It reproduces the full-series dF1(6) = 0.626.
- **Second half of the retained series:**
  - K(6)/K(4) ≈ 0.064/0.113 ≈ 0.57, which is above 1/2;
  - dF1(6) ≈ 0.56, a(6) ≈ 3.38, s ≈ 0.31.
  - So the X-W K-condition would fail, and the winding test would read "inconclusive" rather than "X-W met".
- **First half:** s ≈ 0.78 and K-ratio ≈ 0.23.
- **L=4** is stable between halves: a = 2.87 vs 2.76.

So the "X-W met" outcome depends on the analysis window through L=6 alone. This supports the NOTE's decision to give no verdict. It also means the statement that "none of the conclusions below changes if the errors are inflated by 1.4×" (§2.1) is narrower than it sounds. The dominant uncertainty is the L=6 population's non-stationarity, not the size of the error bar.

**S_T caveat.** C1b (§5.4) found that S_T can be shifted by a winding artifact. The small start differences in S_T therefore do not on their own make the S_T probe robust. The NOTE's "more robust" remark is post hoc and labelled, but it should carry this caveat.

### (3) L=8 W=0 β=16 energy −443.85 ± 0.15: **ERROR CREDIBLE; COMPARISON LIKE-FOR-LIKE in Hamiltonian and sector; DIRECTION OF THE BOUND CORRECT; one wording fix**

**Error estimate (`rev_L8_binning.py`, full raw series, 20% discard):**
- **Binned errors reach a plateau:**
  - s3: about 0.18–0.20 for bins of 350–1800 measurements;
  - s5: about 0.20–0.23 for bins of 255–1700 measurements.
- **Sokal τ_int ≈ 5 measurements** (about 10 sweeps) in both runs. That gives about 1000–1300 independent samples per run and errors of 0.144 and 0.159, both at or below the binned values. The 20-bin bins (500–700 measurements) are therefore ≫ τ_int.
- **The spread of the fifths is consistent with statistics.** The std of the s5 fifths, divided by √5, is about 0.25, which matches the binned error.
- **The combined error reproduces:** max(0.145 binned, 0.063 scatter) = 0.145. The z values reproduce as well: −3.28 against the repo and −0.10 against C1.

The NOTE's caveat "the autocorrelation is long" is not supported, because τ_int is short. If anything that caveat is over-cautious. What cannot be excluded are slow modes longer than about 28k sweeps.

The error-of-error with 20 bins is about 16%. With errors 1.2–1.4× larger, the z against the repo would be −2.8 to −2.4, which is still above the declared 2σ threshold.

**Like-for-like comparison:**
- **Source.** `git grep "443.36" docs` points to `docs/RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25.md`, Diagnostic 2: 8³, eight seeds, E(0) = −443.3635 ± 0.0311.
- **Sector.** The repo value is for the W=(0,0,0) sector of the link-qubit ring Hamiltonian, in units of g. C1c's runs stayed at W=(0,0,0) throughout. The sector matches.
- **Hamiltonian convention.** The convention matches. C1b's exact 2³ E0 = −9.0267209 equals the repo note's exact 2³ value −9.026721.
- **Status of the repo value.** It is a projector estimate. That note itself says it is an estimate "for the reached support, not certified unrestricted sector minima", with population, projection and component bias uncontrolled, and its status is unaudited.
- **What a lower thermal value refutes.** It refutes −443.364 as E0 of the full W=0 sector. The repo's loop moves are meant to sample the whole sector (C1 REVIEW C15(d)), so the component-versus-sector difference cannot rescue a value that is too high. A residual bias in the projector is the more likely explanation, but this block does not show that.
- **NOTE §3 wording.** The NOTE says it "did not check" the sector and convention. This review has now checked them, and §3 can be updated to say so.

**Variational argument.** For a correct sampler, ⟨H⟩_{β,W=0} ≥ E0(W=0) holds exactly at any β. CTQMC has no Trotter error, and the bound holds even if only part of the sector is sampled, as long as each component is sampled at equilibrium. So a thermal value significantly *below* a claimed E0 refutes that E0. The NOTE states the direction correctly.

**Wording fix.** "Lies above the W=0 ground energy, by roughly 0.5 ± 0.15" should read "**by at least** about 0.49 ± 0.15". The thermal excess makes the true E0(W=0) lower still. The bound is also statistical (about 3.3σ), not rigorous.

**Agreement with C1.** The agreement with C1's −443.83(14) carries some weight, because C1 used a different method (a Rayleigh-quotient projector) and different code. The lineage is shared, however.

### (4) Overstatements and other points

- **Title and §0.1.** "EQ test passes … L=6" is accurate as declared. "What equilibrated" overstates it, given the L6_s3 step change. Change it to "passed the declared EQ test".
- **§2.1.** "No monotone trend after the first few chunks" is inaccurate for L6_s3. Use "a step increase in L6_s3 after about 47k sweeps".
- **§2.2, "X-W conditions met".** This is correct as declared. Add a one-line note that it is window-dependent through L=6 (see the reviewer post hoc check above).
- **§0.5 and §3.** Change "roughly 0.5" to "at least about 0.5". Delete or soften "the autocorrelation is long" (τ_int ≈ 10 sweeps). Record that the sector and convention match the repo note, and that the repo note disclaims certification.
- **§4.** Add the C1b §5.4 caveat that S_T can be biased by winding artifacts.
- **Minor.** C1b NOTE §4 says β = L/2 is on every ladder, but the L4 ladder has 2.053, not 2. C1c handles this correctly (§2.3).
- **Not overstated.** The NOTE gives no phase verdict and no claim on OBL-R2.1, and it states L=8 PT as "not run". The β=3 failure is reported. The precision criterion is met "barely" (0.145 ≤ 0.15), which the NOTE says.

## Overall verdict: **READY after the minor wording fixes listed in (4)**

No numerical or criterion-application errors were found. The central reading is the correct one: the declared winding test (X-W) and the S_T test (Coulomb) disagree, there is no combination rule, and so there is no phase verdict. The reviewer's window check strengthens that reading, because the X-W outcome is itself not stable at L=6.

The L=8 result has a credible error, a like-for-like sector and Hamiltonian, and a correct one-sided logic. It is about a 3.3σ statistical refutation of −443.364 as E0(W=0). It is not proof.

The fixes are wording only and do not change any number or verdict.
