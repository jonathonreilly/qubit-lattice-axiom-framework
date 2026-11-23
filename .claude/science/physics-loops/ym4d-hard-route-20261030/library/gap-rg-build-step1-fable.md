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

## Step 2 result: (a) the N = 1 inventory is kernel-checked

Run finished 2026-11-23T03:00Z (date -u). File `lean/step1/Inventory.lean` (760 lines; sha256 06969f99ebd5d8d008748e8562c62e12c068eb9f008da98e76eb47a788c182e8), command `lean Inventory.lean`, Lean 4.36.0, `import Init` only, no `native_decide`. Exit 0, **60.9 s wall, peak resident 1,169,571,840 bytes (1.17 GB)**; memory free before the run 76 percent.

What is proved (theorem names in namespace `Step1`):

| Statement of row 1418 | Lean theorem | How |
|---|---|---|
| singlet multiplicities 1, 0, 1, 0, 2, 0, 5 for 0..6 fundamentals | `singlet_table`, `w_is_singlet` | weight count [z^0] - [z^2] of (z + 1/z)^k |
| link counts 1, 15, 30, 5 | `link_counts` | C(6,k) times the multiplicity |
| D_1 = 51 | `link_total_by_occupancy`, `link_total_by_patterns`, `D_one` | three routes: by occupancy, by the 64 patterns, and the generating function of row 1418 by truncated integer series |
| D_2 = 977 | `D_two` | same generating function |
| 24 corners, every node of degree 6 | `corners_card`, `corners_degree_six` | K_{2,2,2,2} built from the rule j != i xor 1 |
| 131,072 even subgraphs | `even_subgraphs` | pruned sum, 64 pieces |
| **12,910,079 slots** | `slots` | pruned sum of prod_v Cat(deg v / 2), 64 pieces |
| 413,122,528 bytes | `slot_bytes` | arithmetic |
| histogram 50,920 / 114,551 / 115,144 / 262,978 / 265,805 / 635,318 | `histogram` | for each of the 64 patterns at node 0 |
| label counts 1, 3, 12, 6, 24, 5 | `histogram_labels` | |
| first moment 12,910,079, second moment 4,329,800,859,159 | `first_moment`, `second_moment` | |

Structure of the slot proof. `pruned leaf steps d` is the sum over corner subsets in lexicographic order that returns 0 as soon as a node whose corners are all decided has odd degree. `prunedS` is the same function with the accumulator forced to a numeral; `prunedS_eq` proves them equal by induction. `split` (induction, no evaluation) rewrites the sum as a sum over the 64 start vectors of the six corners at node 0. Each start vector is one theorem `slot_k`, `even_k`, `hist_k` closed by `decide +kernel` (192 small kernel evaluations, about 0.6 s each for the 96 even ones). `total_of_pieces` joins them.

What is NOT proved in Lean here:

1. The sum over all 2^24 corner subsets (the bare definition `brute`) is not evaluated for K_{2,2,2,2}, and no Lean theorem states `brute = pruned` in general. The pruning only drops branches where a completed node has odd degree, where the leaf weight is 0; this is checked in the kernel on the octahedron K_{2,2,2} (`octahedron_slots_agree`: all 4,096 subsets against the pruned sum; `octahedron_even` = 128 = 2^(12-6+1)), and check 1420's C brute force gives 12,910,079 outside Lean. A general Lean lemma `brute = pruned` is a short induction on the step list (gap, not done).
2. That Cat(deg/2) is the number of structurally admissible entries (noncrossing pairings as a basis of invariants) is the representation-theory input of row 1418, not a Lean statement; Lean checks the weight count 1, 1, 2, 5 only.

The generator `gen_inventory.py` (with `inventory_head.lean.txt` and `values.txt`) writes the 192 piece theorems; the values come from Lean's `#eval` and are only right-hand sides that the kernel then checks.

`#print axioms`, verbatim:

```text
'Step1.singlet_table' depends on axioms: [propext]
'Step1.w_is_singlet' depends on axioms: [propext]
'Step1.link_counts' depends on axioms: [propext]
'Step1.link_total_by_occupancy' depends on axioms: [propext]
'Step1.link_total_by_patterns' depends on axioms: [propext]
'Step1.div_mul_sanity' does not depend on any axioms
'Step1.D_one' depends on axioms: [propext]
'Step1.D_two' depends on axioms: [propext]
'Step1.corners_card' depends on axioms: [propext]
'Step1.corners_degree_six' depends on axioms: [propext]
'Step1.prunedS_eq' does not depend on any axioms
'Step1.octahedron_even' depends on axioms: [propext]
'Step1.octahedron_even_pruned' depends on axioms: [propext]
'Step1.octahedron_slots_agree' depends on axioms: [propext]
'Step1.split' depends on axioms: [propext, Quot.sound]
'Step1.steps_eq' depends on axioms: [propext]
'Step1.stepsLit_split' does not depend on any axioms
'Step1.starts_eq' does not depend on any axioms
'Step1.starts_eq_masks' does not depend on any axioms
'Step1.slot_pieces' does not depend on any axioms
'Step1.even_pieces' does not depend on any axioms
'Step1.hist_pieces' does not depend on any axioms
'Step1.split0' depends on axioms: [propext, Quot.sound]
'Step1.total_of_pieces' depends on axioms: [propext, Quot.sound]
'Step1.even_subgraphs' depends on axioms: [propext, Quot.sound]
'Step1.slots' depends on axioms: [propext, Quot.sound]
'Step1.slot_bytes' does not depend on any axioms
'Step1.histogram' does not depend on any axioms
'Step1.histogram_labels' does not depend on any axioms
'Step1.first_moment' does not depend on any axioms
'Step1.second_moment' does not depend on any axioms
```

So nothing beyond `propext` and `Quot.sound`. They enter through `omega` (in `split`, `sum_map_add`) and through core library instances used by `decide`; no `Classical.choice`, no `Lean.ofReduceBool`, no `sorryAx`.
