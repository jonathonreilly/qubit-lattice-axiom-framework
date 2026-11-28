lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T02:14Z

# Gate: fill-cubical at a7ff7835d

Provenance: anthropic/claude-opus-5-5, effort high, commit a7ff7835d, side mapped, Mac mini worker. The proof's author is openai/gpt-6-astra, so this read is cross-provider. It is one reader's check and not an audit. Verdicts steer research and grant no status. Nothing here was committed or pushed.

## Verdicts

| Statement | Verdict | Note |
|---|---|---|
| Lemma H, (2), and the continuum forms (3), (4) | ADVANCE | Sign and order conventions for transport, gauge action and multiplication all agree. |
| Lemma E | ADVANCE | One wrong citation, D7. The bound itself holds. |
| Lemma G | ADVANCE | Strip areas (m-2)2n and 2n, the 6K/n and 4K/n bounds, and the rim matching all hold. |
| Lemma C | ADVANCE | (8) to (11) re-derived, including 8064 = 36·12·16 + 2·24². Boundary links are exact. Curl is a convex combination of plaquette curls. Traces match across sectors. |
| Theorem S | ADVANCE | Depth three, and seam plaquettes are covered. |
| Borel paragraph | ADVANCE | Each choice is a countable first-success test on open conditions. |
| F2-mult with (13) | ADVANCE | Holds on the torus and on rectangular complexes. The consumer's domain needs a one-line widening, D6. This discharges (F2) as written at `quiet-boundary-rarity.md:47`, T to C_a T, ignoring frozen bonds. |
| Frozen-brick clause | CORRECT-NO-ADVANCE | The implication is valid, but its hypothesis (FG) is false for the consumer's bricks, D1. Nothing downstream may rest on it yet. |
| Is (EXT=) what Theorem Z and Lemma OW need? | **No, not in substance** | It is the literal reading of their text, but neither proof uses it, and Text 5.9 does not ask for it, D3. |

## Defects, ranked by what each breaks

**D1. (FG) is false for the consumer's bricks.** This breaks the frozen-brick clause as applied, and `threshold-paid-reference.md` section 1, which reads it.

- L is odd and blocks are centred at sites (`hard-core--mapped.md:300`, `:902`), so brick walls lie on block faces at half-integers. (FG) asks for walls on lattice vertex hyperplanes, up to an integer translation. No integer translation does this.
- A bond is free when it has an end in a free block (`quiet-boundary-rarity.md:225`, `fibre-propagator.md:118`). So a bond between two adjacent frozen bricks is frozen, and it lies in neither closed brick. Example, L = 3, t_0 = 24: bricks on sites [2,25] and [26,49], bond (25,26). `checks/gate_fc/fill_check.py` C2 confirms this.
- This is more than a wording problem. Take any fixed integer mesh with intervals of length at least 2. The interval containing the slab [25,26] has 25 or 26 strictly inside it. Freeze the regular brick on that side, leave the other free, and let V be rough on a plaquette crossing the slab. That plaquette's bonds are free and such a V is allowed. The coarse cell is selected, and Lemma C rewrites frozen bonds inside it. So the clause's claim that the fill preserves regular bricks "independently of which are frozen" fails for the construction as written.
- *Repair, unproved.* Use the integer mesh rounded down from the walls. Where the upper side of a wall is frozen, the lower side free, and a plaquette crossing the slab is rough, select those facet cells. On their inner vertices set the crossing bonds to 1 and overwrite the free layer below with the gauge copy of the frozen layer. Keep V on facet cells that are not selected. Crossing plaquettes then have angle 0, or at most 5t at a seam, by the cube identity. Run F2-mult at 5t. Cells below a changed layer are selected if they turn rough, and they stay within a fixed multiple of n of X. The cost is that the reference then depends on V and the level's frozen mask, not on V alone. `quiet-boundary-rarity.md:205` item (7) and `threshold-paid-reference.md:78` both state independence of the mask. A mask-free version looks impossible, by the example above. Whether Lemma OW tolerates dependence on the mask is **unchecked**. At fixed (Sigma, d) in Step 4 it appears to.

**D2. Quiet does not control plaquettes between two frozen bricks.** This can break every fill, at any threshold.

- If a plaquette joins two frozen bricks, all four of its bonds are frozen. Dev_b sums "over c in b", and no file read here says such a plaquette is in b. With all bricks quiet, its angle is then unconstrained. If that angle exceeds T_2, no class field agrees with V on the frozen bonds, so (F2), (EXT=) and the 2T reference all fail for that datum.
- It cannot be fixed by reading every plaquette that touches b, since that reads free bonds and breaks the stopping property at `quiet-boundary-rarity.md:57`.
- *Repair, unproved.* A layer also tests plaquettes with all four bonds in the layer, and a failure adds a brick to E. Lemma ST, (W2) and the deterministic lemma at line 179 must then be re-read for that test.

**D3. (EXT=) comes from one line of Theorem Z, not from the proofs.** Answer to the item's last question.

- `Text 5.9` (`hard-core--mapped.md:1027`) sets the margin T_2 = C_p C_a T for a fill whose input is T: "The fill and the path read only T at their inputs, so nothing feeds back", and "a hole's threshold is T at every level". `quiet-boundary-rarity.md:69` then sets X at T_2. With that X the fill gives C_a T_2 = C_p C_a² T, above T_2. So the two texts disagree, and (EXT=) is what the disagreement leaves. As written, Theorem Z (line 81), Step 4 (line 139) and Lemma OW (line 189) do read exactly (EXT=), for every W_B and every V_i.
- What their proofs actually read about the reference:
  1. X is inside R_k, which needs an input threshold of at least 2T (line 201).
  2. At a class top the reference is V, with no tube loss (line 201).
  3. Off the tube V is class, so far components are class (line 133). Any threshold up to T_2 gives this.
  4. The reference has flux at most T_2, so (I_l^𝔡) applies (line 107).
- None of these needs the output threshold to equal the input threshold. Threshold T alone is not enough: label-0 cells in (T, 2T) are not in R_k (line 205 item (5)), and a class top would have X non-empty. Threshold 2T with the class branch V^# = V meets all four. F2-mult at t = 2T gives 2 C_a T <= T_2 once C_p >= 2. C_p is free for this use, since the class path lemma was withdrawn (line 143).
- That is the shape of `threshold-paid-reference.md`. I read that note before reaching this list, so the list is not independent of it, and I did not gate its budget argument (N_pay, (CI-paid), (P5) to (P11)). The new price is its jump at the class boundary, not (EXT=).
- (EXT=) itself stays open: neither proved nor refuted here.

**D4. t_0 as defined does not meet t_0 >= 8n.** `quiet-boundary-rarity.md:37` has t_0 := max(8L, 4 r_S, 3 R_loc, C L log(1/T)), while the clause needs t_0 >= 8n, with n about 5 L a_*^(-1/2) at t = 2T. For small a_* the listed terms are too small, because a_*^(-1/2) outgrows log(1/T). Line 203 notes t_0 >= C R_1 only in a route remark. *Repair:* add the term to line 37. I found no upper bound on t_0 that this violates, since x_* comes after it.

**D5. Periodicity is unchecked.** (FG) also asks for a torus compatible with the tiling. t_0 is a multiple of 8L, so the side must be even in level-l cells. With L odd, a side that is a power of L admits no periodic tiling. The files I read do not state the side.

**D6. F2-mult is stated too narrowly for its use.** Step 4 reads W_B on a union of bricks inside Sigma, which is neither a torus nor a full rectangle. Theorem S covers this at once, as the mesh cells in the domain form a subcomplex. The statement should say so.

**D7. Wrong citation in Lemma E, harmless.** `fill-cubical-extension.md:139-140` says |S_p(q)| <= 2/delta follows from 1 - cos(delta) >= 2 delta²/pi². That gives only pi/delta. The bound is still true: |S_p(q)| = cot(d/2) <= 2/delta, with d the distance from p.

## What a reader should know about C_a

log2 C_a is about 41374 (C1). It is absolute, and the order of constants allows it. T_2/T then carries that size, K >= 4 C_f C_J C_s (T_2/T)² is near 2^82748, and L_0 >= (4 C_s C_p C_a)^(1/kappa). I found no place that needs C_a small.

## Numerics

`checks/gate_fc/fill_check.py`, criteria written in its header before the run, one run, log in `run1.log`, under the numeric lock at 65 percent memory free. Max RSS 0.07 GB.

| Check | Result | Reach |
|---|---|---|
| C1, displayed constants | PASS | Sample values, not a re-proof. |
| C2, half-integer walls and the unassigned bond | PASS | One-dimensional slice, supports D1. |
| C3, Lemmas G, E, C on one SU(2) 3-cell, charged boundary, n = 8, 12, 16, 24 | PASS | See below. |
| C4, Lemma H on 40 random rectangles | PASS | |

- In C3 the transport of A_ext reproduced the boundary links to 4e-16 before they were overwritten. That is the real test of exactness.
- Criterion (b) of C3 was empty, since G is measured from the same links.
- Max theta n² was 27.7, 33.5, 39.2, 46.4, with K near 2 and measured G from 5.3 to 7.1. It tracks G². The bound (c) holds by a factor above 10^4.
- A run cannot reach the proved branch, which needs n >= 32 G(K) with G about 2^176. So C3 exercises the mechanism only. Dimension 4 was not run. Lemma E at d = 3 and the 4-cell case rest on the hand read. C3 says nothing about the best possible fill.

## Read and not read

Read: `FINISH.md`, `GOAL.md`, all of `library/fill-cubical-extension.md` and `parts/hard-core--fill.md`, `library/threshold-paid-reference.md`, `quiet-boundary-rarity.md` lines 1 to 222, Text 5.9, Lemma BG in `fibre-propagator.md`, and targeted lines of the mapped file. Of `library/threshold-saturation.md`, sections 2 and 4 only.

Not read: the proofs of Lemma RF, (CI-N), Lemma ST beyond its statement, and `parts/hard-core--dm.md`. I saw the head of `parts/hard-core--threshold.md` only. The firewall held: no independent-side part or gate was opened. A listing showed the name of `checks/hard-core--independent_fill_trap.py`, and I did not open it.
