# C1c — Long production with C1b's validated finite-T PT QMC: the declared EQ test passes at β = L for L = 4 and L = 6; the declared winding criteria then read X-W while the S_T exponent reads Coulomb (conflict, so no clean phase verdict); L=8 W=0 energy E(β=16) = −443.85(15)

**Block:** `toe-scale-ladder-20261018 / C1c`. This is a production follow-up to C1b (`blocks/C1b/NOTE.md`, `REVIEW.md`).
**Claim types:** [NUM] numerical evidence from this block's runs; [VERDICT] a pre-declared criterion applied as declared;
[POST HOC] a diagnostic chosen after the data were seen; [EXT] a value from elsewhere, not re-verified here.
**Status:** this note has not been reviewed. Author: a Claude subagent (Opus 5.5). No independent check was made:
the code is C1b's, re-run.
**Criteria:** C1b's pre-declared criteria (C1b WORKLOG 01:32/03:35/03:40; C1b NOTE §4), used **unchanged**. The C1c
plan, its fixed schedule and the L=8 criterion (error ≤ 0.15, from C1's review) were declared in `WORKLOG.md` at 08:57 UTC,
before any C1c data existed.

## 0. Bottom line

1. **What equilibrated, by the declared EQ rule.** The rule asks two starts to agree on E, ⟨W²⟩ and S_T(q1) within 2.5σ,
   with at least 10 round trips per run. [NUM]
   - **L=4, β=4: PASS.** It took 173k sweeps per start, with 71 and 78 trips. The start-difference z values are
     E +0.26, ⟨W²⟩ +0.43, S_T +0.03.
   - **L=6, β=6: PASS, but only marginally.** It took 82k and 89k sweeps, with 29 and 32 trips. The z values are
     E −2.32, ⟨W²⟩ +0.82, S_T +0.10.
   - **L=6, β=L/2=3: fails.** The ⟨W²⟩ z is −3.63. This β is not a verdict input.
   - **L=8 PT: not run.** It was in the lowest priority tier and was not feasible in the budget.
2. **Winding criteria [VERDICT]**, from the fit a(L) = L·dF1 at β = L over L = 4 and 6.
   - **C-W (Coulomb) fails.** The slope is s = 0.50(9), which is not consistent with 0.
   - **The X-W (confined) conditions are met as declared:**
     - s > 0 at 5.5σ (direct estimator) and at 4.9σ (TI estimator). The two estimators agree.
     - K(6)/K(4) = 0.39(7), which is below 1/2.
3. **S_T exponent [VERDICT]:** p = 1.131(24). That is **inside the Coulomb window [0.6, 1.4]**.
4. **The two declared criteria contradict each other.** C1b declared no rule for combining them. I therefore report
   **no phase verdict for OBL-R2.1**. My reading [POST HOC] is that the X-W reading is unreliable (§4). Taken as a
   function of L, dF1 *decreases* (0.692(21) → 0.626(26)). That is the opposite of the dF1 ∝ σL scaling which X-W is
   meant to detect. The fit passes only because a = L·dF1 grows when dF1 is roughly constant.
5. **L=8 W=0 thermal energy [NUM]:** E(β=16) = **−443.85 ± 0.15**, from 2 starts, 20 bins, max(binned, scatter).
   - It meets the declared precision requirement of ≤ 0.15, barely.
   - It agrees with C1's −443.83(14): z = −0.1.
   - It lies **3.3σ below** the repo's −443.364(31).
   - In the W=0 sector, ⟨H⟩_β ≥ E0(W=0). So, if the repo value is meant as the W=0 ground energy, it lies above the
     true ground energy, and C1's value is supported. This conclusion holds only if the errors are not
     underestimated (§3.3).

## 1. What was run

All runs used C1b's scripts, copied unchanged (sha256 in `data/source_hashes_C1b.sha256`). The settings were also
C1b's: the declared ladders `data/ladders/L{4,6}.txt` with β_max = 8 and 6, a measurement every 2 sweeps, and loops
off at β > 1 for the first 2000 sweeps (C1b's thermalisation fix).

- **Seeded continuations of C1b's clean runs.** C1b's checkpoints and its raw chunks were copied, so each tag's full
  series is a single run:
  - L4_s3 (canonical, W=0);
  - L4_s4 (mixW_rot: half the replicas start at W=(1,0,0));
  - L6_s4 (mixW_rot);
  - L8E_s3 (canonical, single β=16).
- **New runs:**
  - L6_s3: canonical, seed 203;
  - L8E_s5: rotated canonical with W=0, seed 305.
- **Scheduling.** A thin dynamic 3-worker queue (`scripts/worker.sh`, with flock per tag) ran 15-minute chunks in
  priority tiers L4 > L6 > L8E from 08:56 to 16:42 UTC, at nice 10.
- **Integrity.** All 93 chunks returned `check=0`, so every configuration was valid.

| tag | L | start | chunks (15 min) | sweeps | PT round trips |
|---|---|---|---|---|---|
| L4_s3 | 4 | W=0 | 17 (3 from C1b) | 172.6k | 71 |
| L4_s4 | 4 | half W=1 | 17 (3 from C1b) | 173.4k | 78 |
| L6_s3 | 6 | W=0 | 24 | 81.8k | 29 |
| L6_s4 | 6 | half W=1 | 26 (2 from C1b) | 88.7k | 32 |
| L8E_s3 | 8 | W=0, β=16 only | 11 (2 from C1b) | 36.3k | – |
| L8E_s5 | 8 | W=0 (rotated), β=16 only | 8 | 26.6k | – |

## 2. Results [NUM]

The analysis used the declared scripts unchanged: `analyze_prod.py 4 6` with SEEDS=3,4, plus `ti.py`, `drift.py` and
`energy_L8.py`. The first 20% of each series was discarded, and errors use 20 bins, combined as max(binned, seed
scatter). Logs: `logs/analysis_L4_L6_final.log`, `analysis_L4_final.log`, `ti_L4.log`, `ti_L6.log`, `drift_L4.log`,
`drift_L6.log`, `energy_L8_final.log`. Summary: `data/summary_prod.json`.

### 2.1 Observables at β = L

| L | E | K = ⟨W_a²⟩ | P1 | dF1 direct | dF1 TI | a = L·dF1 (direct / TI) | S_T(2π/L) |
|---|---|---|---|---|---|---|---|
| 4 | −54.655(49) | 0.1142(83) | 0.1115(83) | 0.692(21) | 0.670(20) | 2.768(85) / 2.68(8) | 0.3289(16) |
| 6 | −186.49(15) | 0.0449(67) | 0.0449(67) | 0.626(26) | 0.647(39) | 3.76(16) / 3.88(23) | 0.2079(18) |

- **Other β values:**
  - At L=4, β=8: E = −56.115(19) and ⟨W²⟩ = 0.0019(11). The ⟨W²⟩ start z is −2.07.
  - At L=6, β=3: ⟨W²⟩ is 0.452(22) from one start and 0.588(30) from the other, so **EQ fails** there.
- **Per-chunk drift.** P1(β=L) fluctuates strongly from chunk to chunk:
  - L=4: 0.035 to 0.20;
  - L=6: 0 to 0.14, with stretches of several chunks near 0.
  - Neither run shows a monotone trend after the first few chunks, and the two starts overlap (`logs/drift_*.log`).
- **Chunk-mean errors [POST HOC].** `scripts/posthoc_chunk_errors.py` and `logs/posthoc_chunk_errors.log` treat each
  chunk as one sample. This gives ⟨W²⟩ errors 1.2–1.4× larger than the binned ones at L=4, and about 1.0–1.3× larger
  at L=6. The start-difference z becomes +0.15 (L=4) and +0.75 (L=6). None of the conclusions below changes if the
  errors are inflated by 1.4×; for example, s would be 0.50(13).

### 2.2 Criteria evaluated as declared [VERDICT]

- **EQ at β=L:**
  - L=4 PASS.
  - L=6 PASS. The E z of −2.32 is near the 2.5 limit.
  - The user's tighter target of z < 2 on ⟨W²⟩ is met at both L: z = 0.43 and 0.82.
- **TI vs direct agreement:** agree at both L, at 0.8σ and 0.4σ.
- **Fit a(L) = a0 + sL** over L = 4 and 6, with 0 degrees of freedom:
  - direct: s = 0.495(90), a0 = 0.79(41);
  - TI: s = 0.60(12).
- **C-W:** needs |s| ≤ 2σ **and** K(L_max) ≥ 0.02. The K condition holds (K(6) = 0.045), but |s| is 5.5σ, so C-W
  **fails**.
- **X-W:** needs s > 0 at more than 3σ **and** K to fall by more than a factor of 2 per ΔL = 2.
  - The slope condition holds: 5.5σ direct and 4.9σ TI.
  - K(6)/K(4) = 0.394. With chunk errors it is 0.39(7), which is 1.6σ below 0.5. The criterion as declared
    states no significance for this ratio, so the point estimate is applied.
  - So the **X-W conditions are met**.
- **S_T exponent** p = ln(S_T(4)/S_T(6))/ln(6/4) = **1.131(24)**. This is in the **Coulomb window** [0.6, 1.4].
  The gapped window starts at p ≥ 1.6, which this value is 20σ away from.
- **Overall: the two declared probes contradict each other** (X-W from the winding fit, Coulomb from S_T). The
  declared criteria have no rule for combining them, so **OBL-R2.1 remains unresolved**. I do not substitute a new
  rule after seeing the data.

### 2.3 dF1 versus L [NUM]

The question was asked directly, so the values are collected here. At β = L, dF1 falls from 0.692(21) at L=4 to
0.626(26) at L=6 (direct), a 2.0σ decrease, and from 0.670(20) to 0.647(39) by TI.

At β = L/2, the L=4 value is not evaluated by `analyze_prod.py`, because L/2 = 2 is not on the L=4 ladder (2.053 is).
`ti_L4.log` gives dF1(2.053) = 0.430(17) direct and 0.415(13) TI. At L=6, β=3 fails EQ.

## 3. L = 8 energy at β = 16 (W = 0) [NUM]

- **Per run** (`logs/energy_L8_final.log`, 20% discard). W stayed (0,0,0) throughout in both runs.
  - L8E_s3: E = −443.788. The error is 0.164, 0.192 and 0.202 with 10, 20 and 40 bins.
  - L8E_s5: E = −443.914. The error is 0.231, 0.218 and 0.208 with 10, 20 and 40 bins.
- **Combined** with 20 bins and max(binned, scatter): **E = −443.85 ± 0.145**. The seed scatter alone is 0.06.
- **Comparison with the two reference values:**
  - against C1 [EXT] −443.83(14): z = −0.10;
  - against the repo [EXT] −443.364(31): z = −3.29.
- **Interpretation.** The sampler is exact for the W=0 sector at fixed β, so ⟨H⟩_{β, W=0} ≥ E0(W=0) holds up to
  statistics. A value 3.3σ below −443.364 therefore indicates that the repo figure lies above the W=0 ground energy, by
  roughly 0.5 ± 0.15. This is a one-sided statement.
- **Caveats.**
  - The autocorrelation is long. Fifths of the s5 run range from −444.4 to −443.1, and a fifths-based error, which
    is post hoc, would be about 0.14 combined.
  - The errors only just meet the 0.15 requirement.
  - I did not check whether the repo's −443.364 refers to exactly this sector and Hamiltonian convention. That
    premise is taken from the task and from C1's review.

## 4. Caveats and post hoc reading [POST HOC]

- **Only two L values, both small**, with 0 degrees of freedom in the fit.
- **β = L ties temperature to size.** dF1 is a free energy at T = 1/L, so it contains entropy terms of order
  ln(g1/g0)/β (C1b §8).
- **The X-W rule may be operationally weak.** In a Coulomb phase, dF1 ∝ 1/L asymptotically, so a is constant. Under
  a string tension, dF1 ∝ L, so a ∝ L². The observed dF1 is roughly constant and slightly decreasing, which is
  neither. A linear-in-L slope test is passed by a constant dF1. So the declared X-W test does not separate
  "confined" from "not yet asymptotic", and the decrease of dF1 with L points away from a string tension.
- **The K-ratio condition is met only at 1.6σ significance.**
- **L=6 equilibration is marginal:**
  - E z = −2.32;
  - P1(β=6) stays near 0 for several consecutive chunks of L6_s4 at the end;
  - β = 3 fails EQ.
  The β = L populations at L=6 therefore rest on about 30 round trips with large chunk-to-chunk fluctuations.
- **The S_T exponent is the more robust probe here.** Its start differences are tiny (z = 0.03 and 0.10), and p =
  1.13 sits mid-window. That observation is post hoc, not a verdict rule.
- **What is needed to settle the conflict:**
  - L = 8 at β = 8 with PT, with about 10× the throughput per sweep;
  - or a fixed-β (not β = L) dF1(L) series, which would need a new declaration before any data.

## 5. Files

- **Durable, in this directory:**
  - `scripts/`: C1b scripts copied unchanged, plus `worker.sh`, `launch.sh`, `jobs_C1c.txt` and the post hoc
    `posthoc_chunk_errors.py`;
  - `logs/`: the analysis logs listed in §2, `prod_chunks.jsonl` and `queue_w{1,2,3}.log`;
  - `data/`: `summary_prod.json`, `ladders/` and `source_hashes_C1b.sha256`.
- **Not durable:** the raw chunks and checkpoints (about 96 MB) are in `/tmp/claude-0/c1c_raw/{raw,ckpt}`, and
  `data/raw` and `data/ckpt` are symlinks to them. The numba cache was moved there as well. If those files are lost,
  the logs above are the record. The C1b originals of the continued tags remain in `blocks/C1b/data/`.
- **Resume or extend:** `scripts/launch.sh HHMM` (see `WORKLOG.md`).
