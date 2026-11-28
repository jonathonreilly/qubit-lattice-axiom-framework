lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-29T01:33Z

# Check of the (PUR-io) consumer of the Lean gap chain (FINISH row 1681)

Claude Opus 5.5, high, Mac mini worker 1. Branch claude/ym4d-hard-route at 44550e2f4. Started 2026-11-28T13:33:13Z, finished 13:47:17Z (date -u). Method of row 1671 (`lean-gap-chain-final-check-opus.md`). Not an audit.

## Repo search

FINISH.md names Purity.lean, PurIo.lean and Offset.lean only in rows 1676-1685. No earlier check of these modules is on file. `library/open-core.md` has no match for `passingCutoffs`, `PurityAlong` or `su2_fixed_observable_gap_of_infinite_passing`. I did not repeat the authors' searches of main and the PRs.

## Part A. Reproduction: NOT REPRODUCED (the 6 GB cap blocks it)

Setup. I made a new scratch root, `/tmp/opus-purio-check.Qk6YOv`. It holds copies of the committed `GapChain/*.lean` and `lean-toolchain`, checked against `logs/committed-sha256.txt` (0 mismatches). It uses my own lakefile and manifest from row 1671, and the package folders are symlinks to the read-only fixture. No olean was reused. The sandbox profile applies to every lake and lean run. It denies writes to the fixture and `~/.elan`, and it denies reads of `/tmp/sa-lean-gap-chain-*` and of my row 1671 build folder. Both guards were tested and gave `Operation not permitted`. The release preflight `--no-build` gave `All targets up-to-date (21134 jobs).` The watchdog `tools/watch.sh` ran with nohup from 13:35:39Z to 13:42:19Z, with a heartbeat each minute. Every second it reads the `ps` RSS of each `lean` process and kills any process above 6 GiB. Every 5 s it also logs the physical footprint.

Probe. `check/Probe.lean` holds only the two release imports of Stage 0 and `#eval 1`. It ran with `lake env lean`, nice 10, `LEAN_NUM_THREADS=2`, in the sandbox, with 71 percent free memory.

| Run | Page eviction (my own `tools/evict.py`: lsof lists the 3,497 mapped oleans, mmap read-only, msync) | Killed at RSS | `ru_maxrss` | Wall |
|---|---|---|---|---|
| 1 | none | 6,298,624 KB | 6,455,656,448 B | 158.4 s |
| 2 | `MS_INVALIDATE` every 10 s, 0 errors | 6,334,352 KB | 6,487,801,856 B | 48.5 s |
| 3 | `MS_KILLPAGES`, `MS_DEACTIVATE`, both, one pass each | 6,314,896 KB | 6,469,632,000 B | 30.7 s |

The physical footprint at the kill was 949-982 MB. So the resident set is almost all clean pages of the memory-mapped Mathlib and release oleans. No msync flag lowered the RSS (run 3: 4,055,440 KB before the passes and 4,245,184 KB after). `/usr/sbin/purge` gave `Operation not permitted`. I did not create memory pressure on purpose, because other workers share the machine. Free memory was 62 percent at the end.

**Verdict A.** The import alone reaches 6.3-6.5 GB resident before any local code runs. Every module from Stage 0 to Offset, and any Check.lean, imports this closure. The brief says to stop at 6 GB, so I stopped. No local module was compiled and no `#print axioms` was run. So the kernel claim of rows 1676, 1678 and 1679 has no independent reproduction. The authors report 4.86 GB with their pager. I did not read that pager, so I cannot say how it works.

What I checked without a build:
- The SHA-256 values agree with the receipts: Purity `07895d22b4d9703f04e90f5bb6157a5b7e98cd4b5391f50e185fe1d5a93ed6b2`, PurIo `956de7cf4da125b22485c69e31323a3c9e9c7424840eb00510286d1c1076e14b`, Offset `e119ac9879dd73a387db9818fc9442d4fe62b869dc2f02f7b0f7ba929f7df6a0`. The other 14 modules are byte-identical to the ones row 1671 built and kernel-checked.
- A grep of the three modules finds no `sorry`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, axiom declaration, `debug.`/`skipKernelTC` option, `ofReduceBool`, or `elab`/`macro`/`syntax` command. The only options are `autoImplicit false` and `Elab.async false`. This scan is not a kernel check.

**Proposal for the lead (not done).** Cap the physical footprint at 6 GB, or cap RSS at 8 GB together with the 50 percent free rule. Row 1671 ran at 7.2-7.6 GB RSS and never had less than 56 percent free. Either ruling lets a fresh build run here. Expected time: about 40 min.

Logs: `/tmp/opus-purio-check.Qk6YOv/logs/` (`watch.log`, `watch-rss.log`, `watch-fp.log`, `evict.log`, `time-probe*.txt`).

## Part B. Faithfulness (reading; no kernel confirmation from this row)

### Item 1. `purity` and `passingCutoffs` against the lane's P_K. HOLDS.

```lean
def purity (Γ : CubicPeriodSublattice) (β : ℝ) (u : ℕ) : ℝ :=
  let T := Γ.transfer μt β
  let P₀ := neutralProj Γ μt
  (tracePW (P₀ * T ^ (2 * u)) / tracePW (P₀ * T ^ u) ^ 2).re
def passingCutoffs (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) : Set ℕ :=
  {k | ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ k →
    457 / 625 ≤ purity Γ (betaAt L M k g₀) (Γ.side / 512)}
```

The lane's definition (row 1468 §3.1; `gap-agy-seed-approaches-neon.md` L12): n = ℓb^K, u = n/512, Z_+(v) = Tr(P_0 T^v), P_K = Z_+(2u)/Z_+(u)^2.
- T is the release transfer along `TimeAxis.timeIdx`, and β is `betaAt = (renormalizedBareCoupling)⁻²`, the calibrated least root.
- P_0 is `neutralProj`, (1/8) Σ over the subsets of the 3 spatial axes of `centreTranslation`. It acts on all of L^2, but the release T carries P_G on both sides, so P_0 T^v = P_0 P_G T^v (design row 1457 §2.1; Stage 0 check §1.1).
- The release uses K^(1/2) e^(−V) K^(1/2) and the lane uses e^(−V/2) K e^(−V/2). P_0 commutes with both factors (−1 is central, and a spatial plaquette has 0 or 2 flipped links). By cyclicity, Tr(P_0(AB)^v) = Tr(P_0(BA)^v). P_K is also unchanged under T → cT. This agrees with row 1680: the two transfers have the same spectra but not the same kernels, and P_K reads only traces.
- `purity_eq_traceRatio` proves that the complex ratio is real, so `.re` loses nothing. `purity_eq_sectorMoments` proves that purity is (1 + Σ r_i^(2u))/(1 + Σ r_i^u)^2 in the zero-flux sector.
- u = `Γ.side/512` is exact when 1024 ∣ ℓ, and every consumer theorem requires 1024 ∣ ℓ.
- "Every cube": the data of `CubicPeriodSublattice` are `side` and `lattice`, and `periods_eq` fixes `lattice.periods`. So there is one Γ for each side, the lane's (Z/n)^3.

Not vacuous. (a) The condition is not trivially true. The release builds a cubic `PeriodSublattice` for each side ≥ 3 (`PeriodicGibbsStatesAtASpacingProof.lean` L29). I read this but did not check in Lean that its periods are literally `cubicSublattice 1 n`. (b) The condition can hold: 0 < purity ≤ 1/D ≤ 1, and purity tends to 1 when the excited neutral ratios to the power u go to 0. Whether it holds at β_K is (PUR-io), which is open.

Remark. Lean uses only 2/3 ≤ purity, which gives D − 1 ≤ 1/2, the bound of `NeutralPhysicalSeed`. This is not new: FINISH row 1675 says "purity P >= 2/3 (457/625 is above it) gives the neutral tail D - 1 <= 1/2 directly". No row restates (PUR-io) with the threshold 2/3.

### Item 2. The top theorem. HOLDS.

```lean
theorem su2_fixed_observable_gap_of_infinite_passing :
    FixedObservableLimit (fun L M g₀ =>
      ∀ (ℓ : ℕ) (A : Set ℕ), 0 < ℓ → 1024 ∣ ℓ → A.Infinite → A ⊆ PurIo.passingCutoffs L M g₀ ℓ →
        ∃ K v ν S X₂ X₄, (∀ j, (K j : ℕ) ∈ A) ∧
          FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧
          HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S))
```

- Order: `FixedObservableLimit` binds M and δ before g₀, and ℓ and A are bound inside P. The witnesses come after ℓ and A, so they may depend on g₀, ℓ and A, as RECEIPT-offset says. In Final and Purity, the witnesses come before ℓ.
- Every K j is in A, as stated. The proof uses K ∘ t with `hmem (t i)`.
- `FixedObservableWitnesses` is the release's body by `fixedObservableContinuum_iff := Iff.rfl`. The kernel accepted this in row 1671, on a Stage0.lean that is byte-identical to this one.
- The rate is `gapRate ℓ = (2/ℓ) log(2^18/5041)`, at the original cutoffs and side ℓ.
- Note for the producer of (PUR-io). M and δ are those of `bare_root_with_window_data` at H = Bs + γ⁻² + 1 (PurIo.lean L416-L417), not those of the release export. `passingCutoffs` depends on M. So (PUR-io) must be proved at this M and δ, or for every M with g₀ small. RECEIPT-offset says "at the same calibrated L, M, g₀", which is correct.

### Item 3. The clause table of RECEIPT-offset.md. HOLDS.

| Witness clause | Lean (L748-L771) | Verdict |
|---|---|---|
| Least root, both coupling limits | `hroot`, `hgs`, `hbs` from row 1678, at the original K | HOLDS |
| Infinite-volume states | `match_volume_state`: a real cubic weak limit at K', with cumulants (n ≥ 2) equal to the pushed-forward passage state's | HOLDS |
| Growing tori, test family | `shift_volumes` (v = m − r → ∞); IsR4TestFamily on the unscaled X, monotone in the side | HOLDS |
| Volume and torus cumulant limits | `hi`, `hf`, `torus_cumulant_at_offset` (same sites, same β) | HOLDS |
| Centred moments | `volume_moments_tendsto`, release `su2_moments_tendsto` | HOLDS |
| Positive smooth X₂, X₄ | pulled back by a⁻¹; `scaleTuple_inverse` | HOLDS |
| Growth | base B·(max(1,a⁻¹)max(1,a))^order; the other constants are kept | HOLDS |
| Euclid, permutation, RP, reality | `scale_motion` (same orthogonal part, translation a⁻¹v) and its companions | HOLDS |
| Canonical decomposition, component OS, clustering, non-Gaussian | `canonical_scale`, `scale_OS`/`scale_cluster` (spatial ray a⁻¹v ≠ 0), `nonGaussian_scale` | HOLDS |
| Gap, unique vacuum | `massGap_of_purity` at K' ⊆ A, side ℓ | HOLDS |

Direction. Take a = L^(−r). An original-unit point is y = a·x, so S'(X) = S(X(a·)). The kernel would reject the opposite direction, because `hi` and `hf` must match `stateAtOffset_cumulant` and `torus_cumulant_at_offset`.

Physical scale. Only the calibration `referenceResponse L M (K j) … = fixedPhysicalLevel g₀` fixes a scale. It is a lattice statement at the original cutoff, and the proof keeps it there. S' is the limit at mesh L^(−K'), so it is in calibrated units. No continuum clause reads S at a fixed test or at a fixed rate. The gap rate uses the original mesh, where the cube of ℓL^(K') sites has side ℓ. So no clause is broken by the rescaling.

### Item 4. Receipt wording. HOLDS (no overstatement found).

No receipt says that the continuum limit is unique; "unique" appears only in `HasUniqueVacuum`. No receipt says that (PUR-io) is proved. They say "No Wilson purity lower bound is proved" and "remains a hypothesis", and they make it the next row. "(PUR-io) means that `passingCutoffs L M g₀ ℓ` is infinite" is correct, subject to the M and δ note in item 2. "Identifies ν with the dilated μ on every cumulant used by the witness" is correct for n ≥ 2, and the moments follow from these. I did not check the receipts' sentences on the Sussman-Alpoge outline and complete account (RF53, CA-I 2692-2713), their searches, or their olean hashes.

## Credit

The YM4 Lean release, outline and complete account are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. gpt-6.2-astra max wrote Purity, PurIo, Offset and the three receipts (rows 1676, 1678, 1679). Fact PUR comes from rows 1373, 1461, 1465 and 1468. The 2/3 remark comes from row 1675.

RESULT: Part A NOT REPRODUCED. The brief's live 6 GB RSS watchdog killed even an import-only probe of the release, at 6.30-6.33 GB RSS with about 0.95 GB physical footprint. Clean mapped olean pages could not be evicted (msync had no effect, purge was refused). So there is no independent kernel run of rows 1676/1678/1679. The source hashes match the receipts, and a grep of the three modules is clean. Part B: items 1-4 HOLD (purity = lane P_K, not vacuous; top theorem has M, δ before g₀, ℓ, A, every K_j ∈ A, the full release witness body, rate gapRate ℓ; every transported clause is right and none fixes a scale that S' breaks; no receipt overstatement). Note: (PUR-io) must be proved at the Offset theorem's own M and δ. Open: (PUR-io) itself, and a kernel reproduction under a footprint-based cap or an 8 GB cap if the lead rules for one.
