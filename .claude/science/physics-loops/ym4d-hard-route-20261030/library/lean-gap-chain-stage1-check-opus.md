lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T09:11Z

# Check of row 1459 (Lean Stage 1 of the gap chain): faithfulness and non-vacuity

Row 1503. Started 2026-11-24T21:11Z (date -u), Mac mini worker 2, at commit 7844497b7. Cross-provider check: the Lean files were written by gpt-6.2-astra (row 1459); this check is by Claude Opus 5.5 high. Release credit: the YM4 Lean library and complete account are Sussman-Alpoge (with Claude and Codex); the hand proofs are the lane's rows 668, 697-699, 1356, 1359 and the U4 row of library/gap-os-equiv.md.

## Plan

1. Read lean/gapchain/GapChain/{SequenceLemma,LemmaM1,TheoremS}.lean and RECEIPT.md in full.
2. Read the hand sources: U4 in library/gap-os-equiv.md; Lemma M1 in library/gap-mini-mneutral-fable.md (row 1356) and check 1359; Theorem S in library/gap-crux-restate.md section 3.4 with checks 698-699 and the S3' correction; Lemma A2 of row 668.
3. Faithfulness: statement by statement, and field by field for PairWeight, BoxSpectrum, TorusData.
4. Non-vacuity: build a consumer file in /tmp scratch that constructs an explicit TorusData and applies theoremS; print axioms.
5. Verdict.

## Step 1. Inventory of the Lean statements (read in full)

Files at 7844497b7: `lean/gapchain/GapChain/SequenceLemma.lean` (80 lines), `LemmaM1.lean` (110), `TheoremS.lean` (729), `RECEIPT.md` (190). Read in full.

Exported statements checked here:

- **U4** `sequenceLemma`: `q ≥ 0`, `m n ≥ 0` for all n, `m(n+1)^2 ≤ m n · m(n+2)` for all n, and `∃ᶠ j, m j ≤ C q^j` give `m(n+1) ≤ q m(n)` for all n. `sequenceLemma_of_bound`: same with the envelope at all j.
- **W1** `lemmaM1`: H a complex inner product space (completeness not assumed; a `HilbertBasis` is assumed to exist), B continuous, `B.IsPositive`, `∑ ‖B b_i‖^2` summable, `‖φ‖ = 1`, `c > 0`, and the finite-family test `HSNormLE (c⁻¹ B − |φ⟩⟨φ|) δ` (every finite orthonormal family v has `∑‖A v_i‖^2 ≤ δ^2`) give `(1 − δ^2) Σ_i Re⟨b_i, B² b_i⟩ ≤ ‖B‖^2`. `lemmaM1_hsSq` is the same without positivity, with `Σ‖B b_i‖^2`.
- **W5** structures: `PairWeight` (W : ℕ → ℕ → ℝ, all fields only at periods ≥ 3: pos, swap, submul in the first period, logConvex in the first period, lower `∃ d, d a b ≤ log W(a,b)`); `BoxSpectrum` (top > 0, ratio : ℕ → ℝ with 0 ≤ ratio ≤ 1, Σ ratio^3 summable; thermal a = Σ ratio^a; weight a = top^a (1 + thermal a); gap = inf over i with ratio_i > 0 of log(1/ratio_i) in EReal, ⊤ if none); `Box` (three spatial periods), `TorusData` (spectrum : Box → BoxSpectrum; cross: weight of box R[i:=b] at time a = weight of R[i:=a] at time b, for a, b ≥ 3 and R valid; logConvex in time for valid R; lower: for each valid R and axis i, ∃ d, ∀ a b ≥ 3, d a b ≤ log weight_{R[i:=b]}(a)). Note `T.seed n = thermal of cube(2n) at time n`; `seedRate N = log(1/(5041 s))/N` (⊤ at s = 0).
- **Theorem S** `theoremS`: N ≥ 3, seed N < 1/5041 give, for every k, `seed(2^k N) ≤ (5041 seed N)^(2^k)/5041` and `seedRate N ≤ gap(cube(2^(k+1) N))`. `corollaryS3'`: same seed hypothesis gives `seedRate N ≤ gap(cube L)` for every integer L ≥ 2N. `seed_of_phi`: Φ(n) = 16 log W_{cube n}(n) − log W_{cube 2n}(2n) ≤ 19/100000 gives seed n < 1/5041.

Axioms: per RECEIPT and row 1459 lead replay, all standard; I re-print axioms in my own consumer build (Step 5).

