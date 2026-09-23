# moving-jammed-clusters, attempt a2: evaporation is counted per bond, and one move is not enough

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-j7b51`, task
`J:derive:moving-jammed-clusters:a2`. The only prior attempt, a1 (`w-jonathonsmac4f50-j7b81`), was written by Claude
Opus 5 (`claude-opus-5`). That is the same model family as this worker and it is unrefereed. Block 39 itself was
supervisor-run in the same family. Nothing here is an independent confirmation of anything from that family. Section A of
this attempt checks a1 against the block-39 definition. It is a check within the family, not a referee's check.

**Plan before reading a1, and what changed it.** My plan was to extend the box to the two other convex shapes of the
cubic lattice that have only one face orientation: the octahedron ((111) faces) and the rhombic dodecahedron ((110)
faces). I would then compare the critical formation rates of the three orientations. My first draft applied the unit's
sentence "a record with k agreeing neighbours leaves with probability 1/(1 + (cp)^k)" to every surface record. Reading
the definition in block 39 (open PR "ail39: records that move", note
`ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_..._2026-09-20.md`, "Pair-weight transit" and T2) refuted
that draft. The definition says two things:

- The escape probability is for a move **"to an isolated position"**.
- A move is a **visit of a bond** with exactly one occupied end: "bonds at any symmetric rates". The unit's simulator
  visits every bond once per sweep.

Both points change the answer, and the second one changes a1's.

## 1. What is claimed

**Setting (supplied by block 39 as hypotheses; nothing is adopted here).**

- A site is empty or carries one record, and a record carries its content.
- Neighbouring records weigh `c·ω`, with `ω = p, q, r` for equal, opposite and orthogonal contents. A bond with an empty
  end weighs 1.
- **Motion.** A bond with exactly one occupied end is visited. The record at `s` moves to the empty end `t` with
  probability `w_t/(w_s + w_t)`. Here `w` is the product of the weights of the record's other bonds at that position.
- **Formation.** A record forms at an empty site at rate `z·Z_x`, where `Z_x = c^j A_j` next to `j` aligned records and
  `A_j = p^j + q^j + 4r^j` (block 39 T4).

The cluster's records all carry one content, and I write `x = cp`. Every bond is visited at rate 1. This is the
simulator's rule, and it is the only rule that depends on the bond alone and is invariant under the lattice's
translations and rotations. A common rate `λ` would rescale every departure rate, and therefore `z_c`, and nothing else.

"Evaporation" is read as in a1: the instantaneous rate of moves to an isolated position, with the departed record
treated as lost. "Growth" is `z·Z_x` summed over the empty sites touching the cluster. Section A keeps this accounting so
that it compares like with like with a1. Section C shows where the accounting stops being a growth law.

**A. The box, per bond.**
- Every move of a box record ends at an isolated position. The evaporation rate is
  `E(L) = 24/(1+x³) + 24(L−2)/(1+x⁴) + 6(L−2)²/(1+x⁵)`: a corner record departs along 3 bonds, an edge record along 2 and
  a face record along 1.
- a1 counted one attempt per record: `8/(1+x³) + 12(L−2)/(1+x⁴) + …`. That count puts a corner's departure bonds at 1/3
  of a face bond's rate. No bond-only rate law does that. The natural realization of it (each record's one attempt
  split over its empty bonds) fails detailed balance with the static law by a factor 2 at a corner.
- Write `E(L) = 6L²/(1+x⁵) + βL + γ`. Then
  - `β = 24x⁴(x−1)/((1+x⁴)(1+x⁵))`;
  - `γ = 24x³(x−1)³(x+1)(x²+1)/((1+x³)(1+x⁴)(1+x⁵))`.

  Both finite-size terms have the sign of `x − 1`. With `G = 6zcA_1L²` and `z_c = 1/(cA_1(1+x⁵))`:

| | `x = cp < 1` | `x = cp > 1` |
|---|---|---|
| `z ≥ z_c` | grows at every size | shrinks at every size if `z = z_c`; if `z > z_c`, one **repelling** critical size |
| `z < z_c` | one **attracting** critical size (a largest stable size) | shrinks at every size |

  At `x = 1` exactly, `E = 3L²` and the sign of `z − z_c` decides at every size. So the switch is at `cp = 1`, not at
  a1's `x* = 2.05597`. At the neutral scale `c₀ = 6/(p+q+4r)`, `x > 1` holds exactly when `5p > q + 4r`.
- At `(3,1,2)` the two counts give opposite verdicts:

| `z` | a1's count | the definition |
|---|---|---|
| `(9/10)z_c` | grows up to `L = 10` (a1's "largest stable size") | shrinks at every size |
| `z_c` | grows at every size | shrinks at every size |
| `(11/10)z_c` | grows at every size | repelling size between 17 and 18 |

**B. Which surface records can leave in one move.**
- Take a facet `{n·v ≤ 0}` with primitive normal `n`, and sort `|n|` as `(h, k, l)` with `h ≥ k ≥ l`.
  - The surface records are the layers `m = −n·s = 0 … h−1`.
  - A record in layer `m` has `3 + #{i: |n_i| ≤ m}` recorded neighbours.
  - It can reach an isolated position in one move **iff `m < h − k`**, and then along exactly one bond: the one in the
    direction of the largest normal component.
  - Its other moves end next to `#{i' ≠ i: |n_i'| ≥ |n_i| − m}` records.
  - The touching empty sites of layer `m'` have `j = #{i: |n_i| ≥ m'}`.
- A **tied** facet is one whose two largest `|n_i|` are equal: (110), (111), (221), (331), …. No record of a tied
  facet can leave in one move.
- **Octahedron `|x|+|y|+|z| ≤ R`.** Its one-move evaporation is `6/(1+x)` at every size: only the 6 tips can leave.
- **Rhombic dodecahedron.** Its one-move evaporation is `6/(1+x) + 12R/(1+x³)` (R even) or `6/(1+x) + 12(R−1)/(1+x³)`
  (R odd).
- Both shapes' formation grows as `R²`. So the one-move accounting gives them no critical rate: for every `z > 0` they
  grow above a finite size.

**C. The no-go.**
- The zero in B is not a zero of evaporation. On every facet, a top-layer record reaches an isolated position in two
  moves along the largest normal component. The first move is a hop with probability `1/(1+x)` on (111) and `1/(1+x³)`
  on (110).
- By block 39 T1, the static-law weight of the displaced record relative to the ideal facet is `x^{−k_s}` for any
  path: `x^{−3}` on (111), `x^{−4}` on (110) and `x^{−5}` on (100).
- A per-orientation growth law therefore has to follow at least two moves. The route "one-move balance per face
  orientation" (a1 §4 item 1, and my own first plan) fails at its first step.

**D. (a) and (c).**
- **(a)** Take any cluster whose axis-parallel lines meet it in intervals; every convex lattice cluster qualifies. One
  move reaches exactly `2(|π_x C| + |π_y C| + |π_z C|)` arrangements, twice the sum of its projection areas. That is
  `6L²` for the box (a1's count) and `12R² + 12R + 6` for both the octahedron and the dodecahedron.
- **(c)** Interior records never move until erosion reaches them, and their contents never change. The **law** of the
  surface's moves depends on the contents one layer below the surface and on nothing deeper. The reachable **set** is
  blind to the interior (a1). The law is not.

## 2. Steps

1. **ASSUMED — the setting and the rate convention.** Block 39's motion clause and formation rate are used as supplied
   hypotheses. "Bonds at any symmetric rates" is read as one rate for every bond, which is the unit's simulator
   (`probes/lib/moving_gas.py`: "one sweep visits every bond once"). The accounting of `G` and `E` is a1's: the
   instantaneous rates of the ideal shape, a departed record is lost, and a formation at a touching site is growth. It
   is kept on purpose, and step 12 says what it cannot do.

2. **PROVED / CHECKED (A1) — the box's departures.**
   - Let `s` be a box record and `t = s + e` an empty neighbour. Then `e` points out of the box through a face containing
     `s`.
   - Every other neighbour of `t` is `t + e'` with `e' ≠ −e`. Its coordinate along `e` is one beyond the box, so it is
     empty. So `t` is isolated once the record has moved.
   - The departure probability along that bond is therefore `1/(1 + x^{k_s})`, and `E(L)` sums it over the
     occupied–empty bonds. A corner has 3 such bonds with `k = 3`, an edge record 2 with `k = 4`, and a face record 1
     with `k = 5`.
   - check.py enumerates every occupied–empty bond for `L = 2..7`. All destinations are isolated, the symbolic sum
     equals `E(L)`, and the bond count is `6L²`.

3. **PROVED / CHECKED (A2) — a1's count is not a bond-rate law.**
   - a1's count gives a corner record a total departure rate `1/(1+x³)` over three isolated destinations. That is an
     average rate of 1/3 per departure bond, against 1 for a face record's single departure bond.
   - A rate that depends only on the bond, and is invariant under translations and rotations, is one number for all
     bonds, so it cannot do this.
   - Block 39's T1 proof needs "the same bond is visited at the same rate" before and after the move.
   - Realize a1's count as one attempt per record split over its empty bonds. Then the corner of the 2-box (3 empty
     neighbours) moving to an isolated site (6 empty neighbours) has forward/backward flux ratio
     `(1/3)P_f / (μ'/μ · (1/6) P_b) = 2`. With every bond at rate 1 the ratio is 1. Both are computed exactly.

4. **PROVED / CHECKED (A3) — the finite-size terms and the table.**
   - Expanding `E(L)` in `L` gives `6L²/(1+x⁵) + βL + γ`.
   - `β = 24/(1+x⁴) − 24/(1+x⁵) = 24x⁴(x−1)/((1+x⁴)(1+x⁵))`.
   - The numerator of `γ = 24/(1+x³) − 48/(1+x⁴) + 24/(1+x⁵)` is `24x³(x−1)²(x⁴−1)`, which gives the stated factored
     form. sympy `factor` confirms both.
   - `G − E = εL² − βL − γ` with `ε = 6(zcA_1 − 1/(1+x⁵))`. So `ε` has the sign of `z − z_c`, and `β`, `γ` have the
     sign of `x − 1`.
   - **x > 1.** If `z ≤ z_c`, every term is `≤ 0` and `−γ < 0`, so `G − E < 0` at every size. If `z > z_c`, the
     quadratic is negative at `L = 0` and its roots have product `−γ/ε < 0`. So exactly one positive root exists, with
     shrinkage below it and growth above it: a repelling size.
   - **x < 1.** The signs flip, which gives growth everywhere for `z ≥ z_c` and one attracting root for `z < z_c`.
   - **x = 1.** `β = γ = 0` and `E = 3L²` (every bond's move has probability 1/2).
   - a1's count gives `β_a1 = 12(x⁵ − 2x⁴ − 1)/((1+x⁴)(1+x⁵))`, which is a1's `x*`.

5. **CHECKED (A4) — the numbers.** `G − E` is computed as an exact rational at `L = 2..200`. Beyond 200, step 4's signs
   decide.
   - At the neutral scale, `c₀p − 1 = (5p − q − 4r)/(p+q+4r)`.
   - `(3,1,2)`: `c₀ = 1/2`, `x = 3/2`, `z_c = 16/825`. The verdicts are as in the table in §1A.
   - `(20,1,1)` at `(3/2)z_c`: both counts are repelling. The size is 13 to 14 for a1's count and 33 to 34 for the
     definition.
   - `(1,1,2)` at `(99/100)z_c`: `x = 3/5 < 1`, so the definition gives an attracting size between 18 and 19.

6. **PROVED / CHECKED (B1) — the facet classification.**
   - **Reduction.** Coordinate permutations and sign changes are symmetries of the lattice and its neighbour graph. So
     take `n = (h, k, l)` with `h ≥ k ≥ l ≥ 0` and `gcd = 1`, and `H = {v: n·v ≤ 0}`.
   - **Layers.** For `s ∈ H` put `m = −n·s ≥ 0`. The neighbour `s + σe_i` is in `H` iff `σn_i ≤ m`. That holds always
     for `σ = −1`, and holds for `σ = +1` iff `n_i ≤ m`. Hence `k_s = 3 + #{i: n_i ≤ m}`, and `s` has an empty neighbour
     iff `h > m`.
   - **Destinations.** Let `t = s + e_i` be an empty neighbour, so `n_i > m`. A neighbour `t + σ'e_{i'}` of `t` other than
     `s` lies in `H` iff `σ'n_{i'} ≤ m − n_i < 0`. That forces `σ' = −1`, `i' ≠ i` and `n_{i'} ≥ n_i − m`. So
     `k_t = #{i' ≠ i: n_{i'} ≥ n_i − m}`.
     - For `i = 1`, `t` is isolated iff `k < h − m`, that is `m < h − k`.
     - For `i ≠ 1`, `n_1 = h ≥ n_i > n_i − m`, so `t` is never isolated.
   - **Growth sites.** An empty `t` with `n·t = m' ≥ 1` has recorded neighbours `t − e_i` with `n_i ≥ m'`.
   - **Layer density.** All points of one layer are related by translations `v` with `n·v = 0`, which preserve `H`. So
     every property above depends on `m` alone. Different layers are translates of each other: Bezout gives a `u` with
     `n·u = 1`. So every layer has the same density per unit area.
   - **Per-facet one-move accounting (consequence).** Per layer area:
     - departures `Σ_{m=0}^{h−k−1} 1/(1 + x^{3+#{i: n_i ≤ m}})`;
     - formation `z Σ_{m'=1}^{h} c^{j(m')} A_{j(m')}`, with `j(m') = #{i: n_i ≥ m'}`.

     A tied facet has no departures.
   - check.py confirms every layer statement at every lattice point with `|coordinates| ≤ 4` for 19 normals, including
     permuted and signed ones.

7. **PROVED (octahedron) / CHECKED (dodecahedron) (B2) — the polytopes.**
   - **Octahedron.** Let a record `s = (a,b,c)` with `|a|+|b|+|c| = R` move to `t = s + e_1` (outside iff `a ≥ 0`).
     `t − sign(b)e_2` stays inside unless `b = 0`, and the same holds for `c`. So `t` is isolated only if `b = c = 0`,
     that is at a tip, and then only along its axis. That gives 6 departures at every size.
   - **Both shapes' full move and growth censuses** are CHECKED at `R = 2..12`: the octahedron's, and the dodecahedron's
     for each parity of `R`. The formulas are in check.py B2 and §1. For the dodecahedron beyond `R = 12`, the
     quasi-polynomial form of the census is ASSUMED, not proved.

8. **PROVED (B3) — one-move accounting for the tied shapes.**
   - From step 7: `D_oct = 6/(1+x)`, and `D_dod = 6/(1+x) + 12R/(1+x³)` (even) or `6/(1+x) + 12(R−1)/(1+x³)` (odd).
   - Formation is `Θ(R²)`, so `G/D → ∞` (sympy `limit`).

9. **PROVED / CHECKED (C1) — two moves suffice everywhere, and the static weights.**
   - Let `s` be in the top layer (`m = 0`) of any facet. The first move is `s → t = s + e_1`, with `n·t = h > 0`.
   - After it, the recorded neighbours of `t` are the `t − e_i` (`i ≠ 1`) with `n_i = h`. So
     `k_t = #{i ≠ 1: n_i = h}`: 2 on (111), 1 on (110), 0 on (100).
   - The second move is `t → u = s + 2e_1`. Every neighbour of `u` other than `t` has `n·(·) ≥ 2h − h > 0`, so `u` is
     isolated.
   - The two probabilities are `x^{k_t}/(x^{k_s}+x^{k_t})` and `1/(1+x^{k_t})`.
   - By T1 each move multiplies the static weight by `w_new/w_old`. Along the path the product is
     `x^{k_t−k_s}·x^{−k_t} = x^{−k_s}`, and so is any other path's product, since only the endpoints enter.
   - check.py confirms a two-move path on (111), (110), (221) and (331). On (111) and (110) it has the probabilities
     stated in §1C.

10. **PROVED / CHECKED (D1) — one move.**
    - Every axis-parallel line that meets the cluster in an interval contributes exactly its two end bonds.
    - Distinct occupied–empty bonds give distinct arrangements. If `C − s + t = C − s' + t'` with `s ≠ s'`, then
      `s' ∈ C − s + t` forces `s' = t ∉ C`, which is impossible. So `s = s'` and then `t = t'`.
    - The count is therefore `2Σ_i |π_i C|`. It is enumerated for the box, octahedron and dodecahedron at sizes 2..5.

11. **PROVED / CHECKED (D2) — what the surface reads.**
    - A move `s → t` has probability `w_t/(w_s + w_t)`.
    - `w_s` involves the contents of `s`'s recorded neighbours. `s` has an empty neighbour, so they lie at depth ≤ 1.
    - `w_t` involves records next to the empty site `t`, which lie at depth 0.
    - So a move's law involves depth ≤ 1 only. A record at depth `d ≥ 2` enters only after erosion has brought the
      surface to depth `d − 1` next to it.
    - Depth 1 does enter. At `(3,1,2)`, `c = 1/2`, changing one interior record between aligned, opposite and orthogonal
      gives three distinct exact first-move laws for:
      - the 3-box centre;
      - a site of the 4-box core;
      - the 5-box site `(1,2,2)`.

      For the 5-box centre (depth 2) it gives identical laws.
    - Interior records have no occupied–empty bond, so they never move. Contents are carried and never changed (T1). No
      formation happens inside.

12. **Where the accounting stops (the no-go, stated).** The balance `G − E` of steps 2–8 uses the instantaneous rates of
    the ideal shape.
    - On tied facets the first move is a hop, and its rate is far above the box's departure rate: `1/(1+x)` against
      `1/(1+x⁵)`. So the ideal octahedron and dodecahedron are not the configurations the dynamics spends its time in.
    - Step 9 shows that evaporation from them is two moves away, with a larger static weight than from (100).
    - Any per-orientation growth law has to use the surface's own statistics.

## 3. Where the route stops

- **Instantaneous rates only.** The whole of A and B is the instantaneous, one-move accounting, kept to compare with a1.
  Even for the box, a departed record sits next to the face, above its own vacancy, and can return. "Departed = lost"
  is a1's assumption and is kept here, not proved.
- **The no-go.** Step 12 / C1 shows that the one-move accounting cannot be the growth law for tied facets.
- **What is missing.** I have not computed the stationary evaporation flux: the static-law surface statistics times the
  escape of departed records.
- **The dodecahedron census.** It is proved here only for `R ≤ 12`.
- **(a) beyond one move.** The number of arrangements reachable in `T > 1` moves is still only a1's bound.

## 4. What would finish it

1. **The stationary flux.** Block 39's remark says that at rare formation the occupied set relaxes to the static law
   between formations. Then:
   - evaporation is the static-law density of records at isolated positions next to the surface, times the rate at
     which such a record escapes instead of re-attaching;
   - growth is `z·Z_x` averaged in the same law.

   The escape of a free record from a cluster of linear size `R` in three dimensions is a capacity problem. My
   expectation is that it scales like `R`, against formation `∝ R²`. That would mean a critical size exists for every
   `z > 0`. This is a prediction and it is not claimed here. It would replace both a1's table and the per-bond table
   in §1A.
2. **The dodecahedron census for every R.** An Ehrhart-type argument for the lattice points of each face, edge and vertex
   class would do it.
3. **The simulator has no formation step.** Adding one at rate `z·Z_x` would test the §1A table directly. The table
   predicts nucleation at `(3,1,2)`, which is `x = 3/2 > 1`.

## 5. Running it

```
python3 probes/work/derive/moving-jammed-clusters/w-jonathonsmac4f50-j7b51/check.py
```

Standard library plus `sympy`. It runs 10 checks (A1–A4, B1–B3, C1, D1, D2), all with integer, rational or
rational-function arithmetic. It takes about 20 seconds and prints `PASS`/`FAIL` per check, then `SUMMARY:` and `HIT:`.
