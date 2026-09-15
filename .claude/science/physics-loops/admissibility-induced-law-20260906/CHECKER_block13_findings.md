# Refuting pass — block 13 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block13_causal_gaussian.py`, refuting pass `specs/supervisor_control_block13_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the kernel and covariance (T1) | the level recursion `C_t = A C_{t−1} Aᵀ + σ² I` against the path-count kernel on a `5×5` torus | explicit forward-substitution inverse of `I − A` on the full six-level system (150 sites), `Cov = G Gᵀ` | equal at every pair of sites |
| `P_n` (T2) | walk counts of the projected lazy walk | the multinomial-square formula `Σ_α (n!/α!)²/9^n` | equal for `n ≤ 60` |
| the walk identity (T3) | the multiset count of returning walks | brute-force enumeration of all `6^m` step sequences, `m ≤ 8` | equal; odd lengths never return |
| the harmonic bounds (T2b) | the walk-count route | the multinomial route | equal for `t ≤ 60` |
| the Born expansion (T5b) | exponential coordinates | the stereographic chart | `κ = 1/4` in both |

Findings (all fixed before the census):
- **F1 (structural).** Block 12's note (the level-time identification) is not on `main`, so a stacked block would have carried five open PRs as its base; the seam belongs to the derivation campaign, not to the strong-coupling stack, and block 07 — the only load-bearing parent — is on `main`. The block was re-cut as an independent PR against `main`; level time is restated in two lines; blocks 09 and 12 are referenced for context only.
- **F2 (fixed).** The yaml's quotation of the campaign's phrase carried a token the note itself forbids; reworded.
- **F3 (fixed).** A decimal string in a detail message tripped the runner's own floating-point scan; replaced by a fraction. The runner checks the rational relaxation `2/n` of the note's `9π/(16n)`.

Attempts to refute (nothing refuted): T2(a)'s uniqueness was re-read for the case of a stationary law that is not Gaussian — the argument uses only uniformly bounded variance and the independence of the fresh noise, so it covers every such law; T2(b)'s lower bound was re-derived with the square of half-side `(8n/9)^{1/2}` (`(2R + 1)² ≤ 9n` holds for `n ≥ 1` since `4(8n/9)^{1/2} + 1 ≤ 49n/9`); T3(iii)'s bound on the static series uses T4's `3/(4(2n+1))` and T2(b)'s `9π/(16n)`, whose product is summable; T5(c)'s reading of block 07's formula `mean = −(1/P_xx) Σ P_xy z_y` with `P_xy = −1/2` gives `+1/6` per recorded neighbour, so the gain is `1/2`, not `−1/2`. Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
