lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T14:08Z

# Row 1428: build step 1 of the computer-assisted tool in Lean

Started 2026-11-23T02:08Z (date -u), pinned at commit ac38ef61e. Research-stage working state; no status granted.

## Plan (save protocol)

1. Read row 1418 ('What to implement', 'First buildable component'), check 1420, row 1427 and `lean/glue/RECEIPT.md`.
2. (a) Lean: N = 1 four-dimensional link inventory (counts 1, 15, 30, 5; D_1 = 51) and the 12,910,079 slot count.
3. (b) Lean: one signed closed fundamental cube, b = 1/16, contribution 2^(-28).
4. (c) Lean: four failing acceptance fixtures, each corruption named exactly.
5. Report axioms, wall time, peak memory; state what stays outside Lean; next two rows.

Each step is appended below as it is done.

## Repo search and credit

- Row 1418 (`library/gap-rg-step-sizing-astra62.md`, gpt-6.2-astra): the inventory formula, the counts 1, 15, 30, 5, D_1 = 51, the 12,910,079 slots, the histogram, the cube value b^6/16 and the fixture list. All statements checked here are theirs; nothing below is a new mathematical statement.
- Check 1420 (`library/gap-rg-step-sizing-check-opus.md`, Claude Opus 5.5): independent C brute force over 2^24 corner subsets; defect 3 (fixture corruptions must be named exactly) and defect 4 (no kernel receipt) are what this row answers.
- Row 1427 (`lean/glue/GlueNamed.lean`, `RECEIPT.md`): the 2D gluing fixture, already kernel-checked; reused unchanged for fixture (c).
- Published sources behind the model: Oeckl and Pfeiffer hep-lat/0110034 (spin-foam form of lattice gauge theory); Sussman-Alpoge complete account GL3-GL4 (SA 2195-2243) for the character coefficients; Yosprakob arXiv 2311.02541 (site tensor without magnetic indices).
- `grep` of `library/open-core.md` for the cube, b^6/16 and the unbranched surface formula: no hit; the value is used as row 1418 states it (unbranched closed surface, b^F d^(V-E)).

## Design (written before any Lean run)

Lean 4.36.0, `import Init` only, no mathlib, no `native_decide`. Closing tactic: `decide` or `decide +kernel` (kernel definitional evaluation; proof term `of_decide_eq_true (Eq.refl true)`, no axiom expected; to be confirmed by `#print axioms`).

(a) Link inventory. Two independent definitions and one formula, all evaluated in the kernel:
  1. weight count: singlet multiplicity of k fundamentals = [z^0] - [z^2] of (z + 1/z)^k, by explicit polynomial product;
  2. C(6,k) Cat(k/2);
  3. D_1 = [z^6] of the row 1418 generating function at N = 1, by truncated integer power-series arithmetic.
  Slots: vertex figure K_{2,2,2,2}, nodes 0..7 with antipode i xor 1, 24 edges. Degree vector stored as one natural in base 8 (degree <= 6). (i) Definition: sum over ALL 2^24 edge subsets of prod_v w(deg v), w = 1, 0, 1, 0, 2, 0, 5 (so odd degree gives 0). (ii) Pruned: the same recursion, abandoning a branch when a node whose edges are all decided has odd degree. Attempt (i) in the kernel; if too slow, report it and keep (ii). Also the histogram by the pattern at node 0 and its two moments.

(b) Cube. Geometry given as data: 8 vertices, 6 faces as oriented 4-cycles. Trace indices: one two-valued index per (face, corner), 24 in all. Haar second moments in integer form (2 x integral): same direction 2 int U_ab U_cd = eps_ac eps_bd; opposite direction 2 int U_ab (U^-1)_cd = delta_ad delta_bc. Lean finds, for every link, its two faces and their relative direction, builds the 24 link-end factors, sums the product over all 2^24 index assignments (depth-first, a zero partial product is abandoned), and checks numerator / denominator = b^6 2^8 / 2^12 = 2^(-28) at b = 1/16. Checked for the outward orientation and for all 64 choices of face orientation (the sign must not depend on them because chi_(1/2) is real).

(c) Failing fixtures, each naming the exact corruption: C1 missing 1/d on exactly one link; C2 spin-one channel dropped; C3 zero denominator; C4 twist sign (centre source on one face not applied / applied on a closed pair).

## Step 1 log: what the kernel can and cannot do in one evaluation (measured)

- First attempt: `pruned (wt 8) steps 0 = 12910079` as ONE `decide +kernel`, with the step list left as an unevaluated expression. Stopped after 10 minutes without an answer.
- With the step list as a literal: 65,536 leaves take 14 s and 3.27 GB peak; the full 131,072 leaves did not finish in 240 s. The time grows faster than the work, and memory is the cause (the kernel caches every intermediate term and the accumulated degree vector stays an unevaluated sum).
- With the accumulator forced to a literal at each step (a `match` on `d + c`): the same 65,536 leaves take 2.8 s and 1.1 GB.
- Consequence for the design: one kernel evaluation of the whole count is the wrong shape. The count is split by the six-bit pattern at node 0 into 64 separate theorems (each its own kernel run with fresh caches), joined by a lemma proved in Lean by induction. The all-subsets sum over 2^24 corner sets (the bare definition) is NOT attempted in the kernel: at the measured rate it would need about 128 times the work and a split into about a thousand theorems. It is instead tied to the pruned sum by a kernel check on the smaller figure K_{2,2,2} (4,096 subsets) and by check 1420's independent C brute force (outside Lean).
- The numeric lock is held (holder `gap-rg-build-step1-fable`) for the Lean runs; memory free was 68 percent at the first run.
