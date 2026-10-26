# Attempt a1: reachable and frozen counts, and the opposite-neighbour ("Fibonacci") rule

Task `J:derive:review-20260929-formation-frozen-boundary-counts:a1`.
Written by Claude Sonnet 5.5 (`claude-sonnet-5-5`), one worker, no subagents. Same model family as the sources and
unrefereed. Nothing here is an independent confirmation of anything.

## Plain-language summary

The earlier note counts the ways a sealed box can end up "frozen" under simple formation rules. A later wall campaign
says one rule is different: a site may form a record unless exactly two opposite neighbours are recorded. On an
`a x b` box with an empty outside, it said the count is a Fibonacci sum, `F_a + F_b - 1`.

This attempt proves that count for every box size (the campaign only checked it and sketched an argument). It then
shows the count is not a boundary law. It depends on box shape, not area or perimeter. It collapses to a single state
if the outside is recorded. The actual randomness of the formation process is almost zero for a large box. All of
this is for that one supplied 2D rule. Nothing here selects a rule or an entropy, and nothing is said about black
holes or 3D.

## What I read (stated as required)

- `docs/MINIMAL_AXIOMS_2026-06-29.md`, the whole file (233 lines), on current main. Used:
  - Lattice is `Z^3` (lines 35-41).
  - Admissibility concerns which possibility a forming record locks, not the formation site, probability or rate
    (63-73).
  - Record: records form, at most one per site, permanent, a site with no record cannot be read (75-83).
  - Admissibility supplies no record-production process (119-123).
  - Formation rules and rate are open gates outside the axioms (181-185).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, whole file. The three approved primitives are the scale
  reference, kinetic isotropy and the realized state. The realized-state primitive supplies "no special boundary
  condition" (lines 124-127). None supplies a formation rule, a box edge convention, a weighting or an entropy.
- Frozen-box note `docs/THE_OWNERS_FROZEN_BOX_READING_WITH_COUNT_THRESHOLD_...2026-09-29.md` at commit `fd51a1f4`, in
  full, with its runner and cache. It is not on current main (`3e1a2dd253`; checked by tree listing and grep).
- The wall campaign's kill note `.claude/science/walls/toe-walls-20260929/kills/T76.md` at `4bd42747` (PR 9395
  branch), error 1, which holds the stripe-rule claim, with its `rect_stripe.py` and `covariant2d.py`. Its hash
  matches SOURCE_MAP.json.
- Hashes: all 97 objects of the 9363 source map (28 named in the task) verified. The six PR 9395 files used also
  verified. See `RECOVERY_STATUS.json`.
- Prior-art search: no note on main or in `probes/work` contains the stripe-rule proof. The `moving-jammed-clusters`
  attempts concern a different object. The open-PR title search found nothing relevant. I did not read open PR
  bodies.

## Setting and premises (all supplied, none from the axioms)

- ASSUMED P1. Sealed `a x b` box (or `L^d`) of the square (cubic) lattice, one permanent record per site.
- ASSUMED P2. A formation rule: an empty site may form iff its pattern of recorded neighbours is allowed.
- ASSUMED P3. Edge convention: outside sites count as unrecorded ("empty boundary"), or as recorded ("recorded
  wall"). The realized-state primitive says no boundary condition is supplied.
- ASSUMED P4. Start from the empty box.
- ASSUMED P5. A process, only where entropy of the process is asked: unit-rate Poisson clocks, a ring forms the
  site if eligible. Its embedded jump chain picks uniformly among eligible sites. The axioms supply no such
  process (lines 119-123).
- ASSUMED P6. The axiom lattice is `Z^3`. The stripe rule below is a 2D rule. A 2D box is not axiom content, and no
  3D version is treated here.
- Definitions. `N` = number of frozen occupation sets reachable from the empty box. Frozen = no empty site eligible.
  I count frozen and reachable separately.
- Rule S ("stripe"): an empty site may form unless its recorded neighbours are exactly `{N,S}` or exactly `{E,W}`.
  It is one of the 64 rotation-covariant neighbour-pattern rules on `Z^2` (kill note, error 1).

## Steps

1. RETRIEVAL (checked by hash, not new). Branch heads, 97/97 and 6/6 hashes verified. The stripe-rule claim lives
   only on the PR 9395 snapshot and is an unlanded hypothesis.

2. PROVED (standard). For a crowding rule `A = {0..m}` a set is reachable iff it is `m`-degenerate. Forward order:
   at the time a site is added, its recorded neighbours are exactly its earlier neighbours. Reverse that order for
   peeling. Greedy peeling is confluent, because removing sites only lowers other counts. For `m = 0` this means
   independent, for `m = 1` a forest. Frozen is a radius-one local condition (every empty site has more than `m`
   recorded neighbours), so frozen sets satisfy an exact layer-transfer recursion. Reachability does not, for
   `m < d`, because degeneracy is global.

3. CHECKED. Frozen and reachable-frozen counted separately for `A = {0..m}` (`check.py` Part A, Part A2). Layer
   transfer for frozen counts, pruned backtracking and peeling for reachable, cross-checked by a forward DP over all
   `2^n` subsets for `n <= 16`. 2D, `L = 2..5`:

   | m | reachable-frozen (matches source table) | all frozen |
   |---|---|---|
   | 0 | 2, 10, 42, 358 | 11, 291, 28661, 10982565 |
   | 1 | 6, 57, 1699, 144205 | 7, 89, 4781, 858605 |
   | 2 | 1, 17, 305, 22398 | same |
   | 3 | 1, 2, 7, 63 | same |

   3D, `L = 2, 3`:

   | m | reachable-frozen | all frozen |
   |---|---|---|
   | 0 | 6, 496 | 183, 64289327 |
   | 1 | 40, not enumerated | 77, 8500681 |
   | 2 | 34, 413615 | 35, 482063 |
   | 3 | 1, 12274 | same |
   | 4 | 1, 65 | same |
   | 5 | 1, 2 | same |

   The 28 source counts are reproduced where enumerated. The new content is the all-frozen column. For `m < d` the
   frozen count and the reachable-frozen count differ by orders of magnitude (3D `m = 0`, `L = 3`: 64,289,327
   against 496). Any entropy extrapolation must say which one it extrapolates. The source's "m >= d implies all
   frozen sets reachable" is rechecked on tiny boxes and matches the table.
   Not new: the reachable column.

4. ASSUMED (taken from the source, not re-proved). The source volume law (lemma C) for crowding rules. The note
   reports its referees closed it. Nothing in this attempt depends on it.

5. Rule S, empty outer boundary: structure lemma. PROVED.
   Let `R` be frozen on `[1..a] x [1..b]` and `v` empty. Then `v` has recorded neighbours exactly `{N,S}`
   ("vertical") or exactly `{E,W}` ("horizontal"). Suppose `v` is vertical. Its `E` and `W` neighbours are
   unrecorded, so each is empty or outside. If the east neighbour `u` is inside, `u` is empty, and its west
   neighbour `v` is empty, so `u`'s recorded pair cannot be `{E,W}`. Hence `u` is vertical. Repeating east and west:
   the entire row of `v` is empty with every site vertical. So for each column the sites above and below that row
   exist and are recorded. Therefore the row index lies in `2..a-1` and the rows `r-1, r+1` are fully recorded. In
   particular two empty rows are never adjacent. Horizontal is symmetric (full empty column, index in `2..b-1`,
   neighbouring columns recorded). A full empty row and a full empty column cannot coexist: the recorded row above
   the empty row would meet the empty column. Conversely any such set is frozen: a site in an empty interior row has
   `N,S` recorded and `E,W` empty or outside.
   So frozen sets = (non-adjacent subsets of the interior rows) union (non-adjacent subsets of the interior columns).
   The first family has `F_a` members (independent sets of a path on `a-2` vertices, with `F_1 = F_2 = 1`). The
   second has `F_b`. They share only the full box.
   Count: `F_a + F_b - 1`.

6. Rule S, empty outer boundary: every set is reachable. PROVED. Add the sites of any target `R` in row-major order.
   When `(r,c)` is added, its recorded neighbours are among the earlier ones, so a subset of `{N, W}`. That is never
   `{N,S}` or `{E,W}`, so the addition is allowed.
   Therefore **frozen = reachable-frozen, and `N(a,b) = F_a + F_b - 1` for all `a, b >= 1`.**
   CHECKED (Part B1): all boxes with `ab <= 20` (2x2 to 2x10, 3x3 to 3x6, 4x4, 4x5, and 1xb) by a full DP over all
   `2^n` subsets. Frozen count, reachable-frozen count, "every subset reachable" and the structure lemma all
   agree. Constructed sets on 5x6, 6x7, 8x8, 9x11 and 12x12 are frozen and number `F_a + F_b - 1`.
   NEW relative to the sources: the proof. The campaign's note says "suggested" and checks `a, b <= 9`.

7. Rule S, recorded wall. PROVED: `N = 1` for every `a, b >= 1`.
   Frozen: an empty vertical site needs its `E`, `W` neighbours unrecorded. The outside is recorded, so they are
   inside and empty. Step 5's propagation then runs to the box edge, where the next east neighbour is outside and
   recorded. That is a contradiction in a finite box. So no empty site exists: the only frozen set is the full box.
   Reachable: in row-major order each added site has `W` recorded (earlier, or outside) and `N` recorded, so its
   recorded set contains both `N` and `W`. That is never `{N,S}` or `{E,W}`, so it is allowed.
   CHECKED (B2): all boxes with `ab <= 20`, frozen = reachable-frozen = 1.
   First size where the convention matters: 2x3 (empty boundary N = 2, wall N = 1).

8. CHECKED (not proved). The 16 side conventions (each of N, E, S, W outside either empty or recorded), seven box
   shapes each (Part B3). The frozen count equals `R + C - 1`, where `R` (`C`) counts non-adjacent row (column)
   subsets allowed by the conventions, and in every case frozen = reachable-frozen. This follows the step 5 argument
   but I did not write the proof for mixed conventions, and the reachability claim is checked only on the seven
   shapes.

9. PROVED from step 6. `N` is not a function of area or perimeter: 5x5 (area 25, perimeter 20) gives 9. 2x8 (area
   16, perimeter 20) gives 21. 4x4 (area 16) gives 5. Square boxes: `ln N = L ln(phi) + ln(2/sqrt5) + O(phi^-L)`,
   so `ln N / perimeter -> ln(phi)/4`. Strip `2 x b`: `ln N / perimeter -> ln(phi)/2`. There is no common
   coefficient. Also N depends on the edge convention (step 7). So the rule S flat count is not a boundary-law
   candidate with a coefficient in this model. CHECKED (B4) for the numeric examples.

10. Process entropy of rule S (P5). PROVED, with the exact small values CHECKED.
    Claim: for an `a x b` box with empty outer boundary, the probability that the final state is not the full box
    is at most `eps_bar = (a-2) 3^-b + (b-2) 3^-a`.
    Proof: if the final state is not the full box, some interior row `r` ends empty (or an interior column does).
    Look at row `r`. For each column `c`, the site `v_c = (r,c)` never forms. At its first ring `tau(v_c)` it must
    be blocked, so `N_c` and `S_c` are already recorded. A site records only at a ring, so their first rings come
    earlier: `tau(v_c) > max(tau(N_c), tau(S_c))`. First-ring times are independent Exp(1) variables, and the
    triples `{N_c, v_c, S_c}` are disjoint for different `c`. Each triple has `v_c` last with probability 1/3.
    So the row ends empty with probability at most `3^-b`. Union bound over interior rows and columns.
    Fano: `H(final) <= h2(eps) + eps ln(N-1)`, increasing in `eps` on `[0, 1/2]`. If `eps_bar <= 1/2`, then
    `H <= h2(eps_bar) + eps_bar ln(N-1)` with `N = F_a + F_b - 1`.
    All sizes: for the `L x L` box this bound is 0.265 nats at `L = 4`, `3.8e-5` at `L = 15`, `1.0e-20` at `L = 50`
    and below `1e-150` at `L = 400`, while `ln N` grows like `0.48 L`.
    CHECKED (exact, Part C): the full outcome law was computed for 2x2 to 2x9, 3x3 to 3x6, 4x4 and 4x5 (floats),
    and in `Fraction`s for 2x2, 2x3, 3x3, 3x4. In every case `P(not full) <= eps_bar`. For example `14/405 <= 2/27`
    for 3x3. The single-row probability is below `3^-b`, and `H <= ln N` and `H <=` the Fano bound hold. With a
    recorded wall the process ends in the full box with probability 1 (C.wall).
    So the flat count `N` is not the entropy of this process. Its process entropy vanishes faster than any
    exponential while `ln N` grows linearly with `max(a,b)`.

11. CHECKED (exact small boxes, not extrapolated). Process entropy of the threshold crowding rules, same process
    (Part C2). `m = 0`: H = 1.936 (3x3), 2.586 (3x4), 3.430 (4x4), 4.287 (4x5) nats against `ln N` = 2.303, 2.890,
    3.738, 4.682. `H / (number of sites)` is 0.2151, 0.2155, 0.2144, 0.2144. The ratio `H / ln N` is 0.72-0.93
    across `m = 0..3`. So for these rules at these sizes process entropy is close to the flat count, unlike rule S.
    Nothing is claimed about large sizes.

12. CHECKED then PROVED for `m = 0` (part W). With a recorded wall, a boundary site always has a recorded outside
    neighbour, so for `m = 0` it can never form. The reachable frozen sets are therefore exactly the
    empty-boundary reachable frozen sets of the `(L-2)^d` interior. Checked at `L = 3, 4` in 2D. Other `m`
    change differently. Data for `m = 1,2,3` with a recorded wall: 2D, `L = 3`: 6, 65, 62. `L = 4`: 82, 3609, 1233.
    Reported only (the counts depend on the edge convention). Threshold counts are therefore convention-dependent
    too (the source lists recorded boundaries as an escape).

13. READING. Rule S shows that, among rotation-covariant neighbour rules, a flat frozen count can grow only
    linearly in the side length (no volume law), but only because the frozen configurations are rigid stripes whose
    existence needs the empty outer boundary. The three properties the frozen-box reading would need are not met by
    S: boundary-proportional coefficient (step 9), edge-convention independence (step 7), nonzero entropy of the
    process (step 10). I make no claim about other covariant rules.

## NEW relative to the sources

- Proof of `N = F_a + F_b - 1` (steps 5-6) for all box sizes, for both frozen and reachable-frozen.
- Proof that a recorded wall gives `N = 1` for all sizes (step 7).
- Exact shape dependence consequences (step 9).
- A proved all-size Shannon-entropy bound for the process on rule S, and exact small-box process entropies (step 10).
  The kill note's Monte Carlo ("process entropy 0") is replaced by this bound.
- Frozen (not just reachable-frozen) counts for the threshold models (step 3), and the process entropies in
  steps 11-12.
- NOT new: the reachable counts for threshold rules, the degeneracy criterion, the Fibonacci counts as numbers, and
  the volume law.

## First unresolved step, and what remains

- First unresolved: **step 8 and the 3D rule.** The mixed-convention formula and reachability are only checked, and
  no 3D analogue of rule S is defined or treated (the source reports counts 1, 20, 139 for L = 2-4, not re-run).
- The 64 rotation-covariant 2D neighbour rules were not classified. Only rule S and the count-threshold family were
  treated. So this says nothing about whether another covariant rule has a boundary-proportional count together with
  positive process entropy.
- The 3D threshold rule `m = 1`, `L = 3` reachable count is not re-enumerated here.
- No negative claim is promoted. A failed search is not a no-go, and the N1-N8 gate is not run. The statements in
  steps 9-10 are scoped to rule S with P1-P5 and are exact for it.
- No entropy identification is supplied by the axioms. This attempt chooses none.

## Files

- `check.py`: 292 checks, runtime 30-65 s, under 0.3 GB.
- `check_output.txt`: its output. `check_stderr.txt`: timing.
- `RECOVERY_STATUS.json`.
