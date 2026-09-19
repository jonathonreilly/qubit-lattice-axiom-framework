# Corrigendum packet for PR #8174 (block 30): derivation attempt 2 of 2

Worker `w-jonathonsmac4f50-j8143` (claude-opus-5), unit `J-derive-corrigendum-PR8174-a2`.

**Sources.** Block 30's note and runner at the PR #8174 head `cc7662e1`, and the notes of blocks 31–33 at their heads (#8175 `798f661d`, #8176 `ee73bef6`, #8177 `9e98fd75`). Line numbers are those files' lines. The other notes of PRs #8146–#8180 were searched as fetched for the PR #8180 packet.

**Provenance.**
- The defect was found by a grok worker (`J:attack-g:PR8174`).
- It was confirmed by me as #8400 (claude-opus-5).
- My ordering-threshold-down a4 attempt proved `d_1 ≤ max(d_2, d_3)` on `(p, 1, 2)` for `p ≥ 1`.
- All three are my model family's, so this attempt is not independent of the confirmation. No attempt a1 was on `origin/ai/probes` when I wrote this.

## 1. The statement attempted

Block 30's objects: the six-axis menu, the product rule with `φ = p, q, r` (equal, antipodal, orthogonal), and the three deviations
- `d_1 = 1 − K(a | a, a, a)`;
- `d_2 = 1 − K(a | a, a, −a)`;
- `d_3 = 1 − K(a | a, a, b)`.

**(a) Corrected T1.**
- `d_2 − d_1` has the sign of `p − q`.
- `d_3 − d_1` has the sign of `g := p²r + pq² + pqr + 2pr² − q³ − 4r³`.
- Hence the original "`d_1 ≤ max(d_2, d_3)`" holds exactly on `{p ≥ q} ∪ {g ≥ 0}`, and in particular whenever `p ≥ q`.
- It fails at `(1, 2, 1)` (`12/13 > 9/10`) and on 127 integer triples in `{1..7}³` (194 in `{1..8}³`). All of these have `q > p`, and they are exactly the set `p < q`, `g < 0`.
- The proof's intermediate claim "`d_1 ≤ d_3`" holds exactly when `g ≥ 0`. It also fails at `(1, 2, 1)`, where `g = −3`.

**Corrected T1(b).** Define `ε₂ := max(d_1, d_2, d_3)`. Then the site-by-site coupling holds for every positive weight triple, and `ε₂ = max(d_2, d_3)` whenever `p ≥ q`. With block 30's `ε₂ = max(d_2, d_3)` the coupling fails at `(1, 2, 1)` at a reachable state (S3).

## 2. Steps

**S1 (PROVED; CHECKED `A1`).** The closed forms of `d_1, d_2, d_3` are `1 − K(a|·)` evaluated from the menu: symbolically, and exactly at three weight triples.

**S2 (PROVED; CHECKED `A2`).** Two exact identities, each with a positive denominator:
- `d_2 − d_1 = p²(p − q)(pq² + q³ + 4r³) / [(p³ + q³ + 4r³)(p²q + pq² + 4r³)]`;
- `d_3 − d_1 = p² g / [(p³ + q³ + 4r³)(p² + pr + q² + qr + 2r²)]`.

The equivalences follow from these.

**S3 (PROVED; CHECKED `A3`). The original fails, and so does its coupling.**
- At `(1, 2, 1)`: `(d_1, d_2, d_3) = (12/13, 4/5, 9/10)`.
- In block 30's coupling, a predecessor `z` with `ξ_z = 1` and value `−a` puts its successor `y` in the state `(a, a, −a)`. There `ξ_y = 1` with probability `4/5`, while `η'_y = 1` with probability `ε₂ = 9/10`. So with positive probability `η'_y = 1` and `ξ_y = 0`.
- Take a successor `x` of `y` whose other two predecessors are `a` in both processes. The coupling needs `P(ξ_x = 1) = d_1 = 12/13 ≤ P(η'_x = 1) = 9/10`, which is false. The census of all integer triples is checked exactly.

**S4 (PROVED; CHECKED `A4`). The repair.**
- Up to the rule's symmetry and the order of the predecessors, the predecessor triples with at least two entries `a` are `(a, a, a)`, `(a, a, −a)` and `(a, a, b)`. So their dissent probabilities are `d_1, d_2, d_3`.
- With `ε₂ := max(d_1, d_2, d_3)`, block 30's coupling goes through verbatim. Its one-dissenting-predecessor case then bounds every triple with at least two `a`'s.
- Checked on all 216 triples at the counterexamples and at the certificate points.

**S5 (PROVED; CHECKED `A5`). The executed points.** Every weight point used by blocks 30–33 has `p ≥ q`:
- the certificates 4165, 2085, 8330 and 6247;
- the ceiling 4150;
- the stakes 453 and 368;
- block 33's 2921, 1464, 5841, 4380 and 405;
- `(11, 1, 2)`.

So `ε₂ = max(d_2, d_3) = max(d_1, d_2, d_3)` at all of them. The same holds on the whole lines `(p, 1, 1)`, `(p, 1, 2)` and `(p, 1, 3)` for `p ≥ 1`, and `(p, 2, 4)` for `p ≥ 2`.

## 3. (b) Every use, with a verdict

### Block 30 note (#8174 @ `cc7662e1`)

| Lines | Statement | Verdict |
|---|---|---|
| L4 (claim_scope, T1) | "a site with exactly one [1-predecessor] is 1 with probability epsilon_2 = max(d_2, d_3)", stated for positive `(p, q, r)` | needs its own repair: `ε₂ = max(d_1, d_2, d_3)`, which equals `max(d_2, d_3)` for `p ≥ q` |
| L32 (result up front) | "amplified with probability `ε₂ = max(d_2, d_3)`" | holds on the corrected domain (the note's lines); state `p ≥ q` or use the max of three |
| L84 (declared objects) | "`ε₂ := max(d_2, d_3)`" | needs its own repair: `max(d_1, d_2, d_3)` |
| L99 (table T1) | "`ε₁ = d_1`, `ε₂ = max(d_2, d_3)`" | as L84 |
| L107 (T1(a)) | "`d_1 ≤ max(d_2, d_3)`", stated for every positive `q, r` | needs its own repair: the `iff` of §1 |
| L109 (proof of T1(a)) | "`d_1 ≤ d_3` because `K(a \| a, a, a) ≥ K(a \| a, a, b)` … executed at the four lines" | needs its own repair: false at `(1, 2, 1)`; replace with the S2 identities |
| L109 (proof of T1(b)) | "`≤ max(d_1, d_2, d_3) = ε₂`" | holds with the corrected definition of `ε₂` |
| L134 (T4) | "With `ε₁ = d_1`, `ε₂ = max(d_2, d_3)`", on the four lines | unaffected (S5) |
| L140 (T5) | the ceiling `ε₂ < 256/531441` on `(p, 1, 2)` | unaffected |
| L187 (Falsifiers) | "`d_1 > max(d_2, d_3)` at some tested line" | holds; the falsifier cannot fire at the tested lines, where `p ≥ q` |
| L193 (Boundaries) | "amplification noise `max(d_2, d_3)`" | needs its own repair: `max(d_1, d_2, d_3)`, or scope it to `p ≥ q` |

### Block 30 runner (#8174 @ `cc7662e1`)

| Lines | Verdict |
|---|---|
| L4 (docstring) "`d_1 <= max(d_2, d_3)`" | needs its own repair |
| L452–465 (B2) | tests only the four thresholds and `(11, 1, 2)`, so it cannot see the defect. Add the S2 identities and a failing point such as `(1, 2, 1)` for the original, and test `ε₂* = max(d_1, d_2, d_3)` on all 216 triples |
| L631 `e1, e2 = d1, max(d2, d3)` | unaffected numerically on the lines; write `max(d1, d2, d3)` |
| L669 (`FENCES` sentence) | change in step with the note's L193 |

### Other notes of the campaign

| Note | Verdict |
|---|---|
| Block 31 (#8175) L92: "`ε₁ = d_1`, `ε₂ = max(d_2, d_3)` with block 30's closed forms" | holds on the corrected domain; its stakes are on `(p, 1, 2)` |
| Block 32 (#8176) L93 (same definition) | holds on the corrected domain |
| Block 33 (#8177) L95 and L135 (`ε₂` from block 30; certificates at the four lines) | holds on the corrected domain |
| Block 25 (#8168) T0 (single-level `ε = max(d_1, d_2, d_3)`) | unaffected: it includes `d_1` |
| Block 12 (#8146) S3 (`ε` = the maximum over all triples with two entries `a`) | unaffected |

No other note of #8146–#8180 defines or uses `max(d_2, d_3)`. The search covered "`max(d_2, d_3)`", "`ε₂ = max`" and "`d_1 ≤`" over the fetched notes.

## 4. (c) The exact lines to change

**Note (`cc7662e1`).**
- **L4:** "epsilon_2 = max(d_2, d_3)" → "epsilon_2 = max(d_1, d_2, d_3) (= max(d_2, d_3) when p >= q)".
- **L32:** same substitution.
- **L84:** "`ε₂ := max(d_2, d_3)`" → "`ε₂ := max(d_1, d_2, d_3)`, equal to `max(d_2, d_3)` when `p ≥ q`".
- **L99:** same substitution.
- **L107:** "`d_1 ≤ max(d_2, d_3)`" → "`d_1 ≤ d_2` iff `p ≥ q`, and `d_1 ≤ d_3` iff `p²r + pq² + pqr + 2pr² ≥ q³ + 4r³`; so `d_1 ≤ max(d_2, d_3)` exactly on the union (e.g. not at `(1, 2, 1)`)".
- **L109:**
  - replace "`d_1 ≤ d_3` because … executed at the four lines, B2)" by the two S2 identities;
  - keep "`≤ max(d_1, d_2, d_3) = ε₂`" with the new definition.
- **L134:** add "(here `p ≥ q`, so `ε₂ = max(d_2, d_3)`)".
- **L193:** "amplification noise `max(d_2, d_3)`" → "amplification noise `max(d_1, d_2, d_3)`".

**Runner (`cc7662e1`).**
- **L4:** as the note's L107.
- **L452–465:** as above.
- **L631:** `max(d1, d2, d3)`.
- **L669:** match the new L193.

**Blocks 31–33** (optional, for consistency): L92 of #8175, L93 of #8176 and L95 of #8177: write "`ε₂ = max(d_1, d_2, d_3)` (`= max(d_2, d_3)` on these lines, `p ≥ q`)".

## 5. What would finish it

Nothing in (a)–(c) is open. The edits are the note owner's; no PR is touched here.
