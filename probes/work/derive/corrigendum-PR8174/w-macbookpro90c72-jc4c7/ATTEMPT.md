# Corrigendum to block 30 (PR #8174), T1(a): `d_1 ≤ max(d_2, d_3)`

Worker `w-macbookpro90c72-jc4c7`, model `claude-opus-5`, unit
`J:derive:corrigendum-PR8174:a1`. Checks: `check.py` in this directory
(12 exact checks, C1–C10, all passing).

## 1. The exact statement attempted

Source. PR #8174, branch
`physics-loop/admissibility-induced-law-block30-six-axis-threshold-two-level-domination-amplified-nodes-20260916`,
note `docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_LIFTED_BY_A_TWO_LEVEL_DOMINATION_SEEDS_AND_AMPLIFIED_NODES_IN_THE_EXPLANATION_TREE_BOUNDED_THEOREM_NOTE_2026-09-16.md`,
runner `scripts/admissibility_rule_six_axis_formation_threshold_two_level_domination_seeds_and_amplified_nodes_2026_09_16.py`.

Definitions, from that note's line 84. Six-axis menu `φ(v, v') = p, q, r` for
equal / antipodal / orthogonal pairs, `p, q, r > 0`; sites `x ∈ Z³`, level
`τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`;
`K(v | v_1, v_2, v_3) ∝ Π_j φ(v, v_j)`; level 0 is the all-`a` plane;
`ξ_x = 1{v_x ≠ a}`;

    d_1 = 1 − K(a | a, a, a),  d_2 = 1 − K(a | a, a, −a),  d_3 = 1 − K(a | a, a, b),  b ⊥ a,
    ε₁ := d_1,   ε₂ := max(d_2, d_3),

and `η'` the two-level automaton: `η'_x = 1` if at least two predecessors are
`1`; `= 1{U_x < ε₂}` if exactly one; `= 1{U_x < ε₁}` if none, with one i.i.d.
uniform `U_x` per site.

The task states as given that T1(a)'s clause `d_1 ≤ max(d_2, d_3)` is false for
general positive `(p, q, r)`. Attempted here:

> **(a)** the largest set of `(p, q, r)` on which the clause holds, proved, with
> the minimal corrected formula for `ε₂`; **(b)** a verdict for every later
> statement in the note and in the campaign's other notes (PRs #8146–#8180)
> that uses the defective clause; **(c)** the exact lines of the note and the
> runner that must change.

Everything is homogeneous of degree 0 in `(p, q, r)`, so the answer is a region
in the projective triangle; nothing below normalises `r = 1`, but it could.

## 2. Part (a): the corrected statement

### Step 1 — the closed forms (PROVED; CHECKED, C1)

Write `w(u) = Π_j φ(u, v_j)` over the six states `±e_1, ±e_2, ±e_3`, `a = +e_1`.

* preds `(a, a, a)`: `w(a) = p³`, `w(−a) = q³`, `w(b) = r³` for each of the four
  `b ⊥ a`. So `D_1 = p³ + q³ + 4r³` and `d_1 = (q³ + 4r³)/D_1`.
* preds `(a, a, −a)`: `w(a) = p²q`, `w(−a) = pq²`, `w(b) = r·r² = r³` (four).
  So `D_2 = p²q + pq² + 4r³ = pq(p + q) + 4r³` and `d_2 = (pq² + 4r³)/D_2`.
* preds `(a, a, b)`, `b ⊥ a`: `w(a) = p²r`, `w(−a) = q²r`, `w(b) = pr²`,
  `w(−b) = qr²`, `w(±c) = r³` for the remaining axis. So
  `D_3 = r(p² + q²) + r²(p + q) + 2r³` and `d_3 = (rq² + r²(p + q) + 2r³)/D_3`.
  The four choices of `b` give the same value (C1).

These are the note's front-matter forms; they are true and are re-derived here
from the menu rather than imported.

### Step 2 — monotonicity in `p` (PROVED; CHECKED, C2b)

The other clause of T1(a) is unaffected. Differentiating the retained mass:

    ∂_p (p³/D_1)  = 3p²(q³ + 4r³)/D_1²                        > 0
    ∂_p (p²q/D_2) = (p²q³ + 8pqr³)/D_2²                        > 0
    ∂_p (p²r/D_3) = (r²p² + 2r²pq² ... ) /D_3²
                  = r(r p² + 2 r p q² /r ... )                  — expanded:
    2pr·D_3 − p²r(2rp + r²) = 2r²pq² + r³p² + 2r³pq + 4r⁴p     > 0

so all three `d_i` are strictly decreasing in `p` at fixed `q, r > 0`. (C2b
verifies, for each `d_i`, that `−∂_p d_i` is a ratio of two polynomials all of
whose coefficients are positive, which is the whole of the claim for
`p, q, r > 0`.)

### Step 3 — the two sign identities (PROVED; CHECKED, C2)

    d_2 − d_1 = p³/D_1 − p²q/D_2 = p²(p D_2 − q D_1)/(D_1 D_2),
    p D_2 − q D_1 = p³q + p²q² + 4pr³ − p³q − q⁴ − 4qr³
                  = q²(p² − q²) + 4r³(p − q) = (p − q)[q²(p + q) + 4r³],

so, the bracket being positive,

    sign(d_2 − d_1) = sign(p − q).                                      (I)

    d_3 − d_1 = p²(p D_3 − r D_1)/(D_1 D_3),
    p D_3 − r D_1 = rp³ + rpq² + r²p² + r²pq + 2r³p − rp³ − rq³ − 4r⁴ = r·g,
    g := r p² + (q² + qr + 2r²) p − (q³ + 4r³),

so

    sign(d_3 − d_1) = sign(g).                                          (II)

(`g` is also `q²(p − q) + pr(p + q) + 2r²(p − 2r)`, C2.) Combining,

    d_1 > max(d_2, d_3)   ⟺   p < q  and  g < 0.                      (III)

### Step 4 — the maximal domain (PROVED; CHECKED, C5, C6)

As a polynomial in `p`, `g` has leading coefficient `r > 0`,
`g(0) = −(q³ + 4r³) < 0` and `∂_p g = 2rp + (q² + qr + 2r²) > 0` for `p ≥ 0`.
So `g` is strictly increasing on `p ≥ 0` and has exactly one positive root

    p* = [ −(q² + qr + 2r²) + sqrt((q² + qr + 2r²)² + 4r(q³ + 4r³)) ] / (2r),
    g(p) ≥ 0  ⟺  p ≥ p*.

By (III) the clause `d_1 ≤ max(d_2, d_3)` holds exactly on

    𝒟* := {p ≥ q} ∪ {p ≥ p*} = { p ≥ min(q, p*) },

which is therefore the largest domain asked for; it is a closed half-line in `p`
at each fixed `(q, r)`, and 𝒟* is exactly the complement of the failure set in
(III). Two exact facts locate the boundary without surds:

    g(q)      = 2r(q + 2r)(q − r),        g(q − 2r) = −4r²(q + r) < 0.

Hence the dichotomy

* `q ≤ r`:  `g(q) ≤ 0`, so `p* ≥ q` and `𝒟* = {p ≥ q}` — the naive domain;
* `q > r`:  `g(q) > 0`, so `p* < q` and `𝒟*` is strictly larger than `{p ≥ q}`,
  with `q − 2r < p* < q`: the true boundary sits in a strip of width `2r` below
  `q`.

In particular the failure region always contains `{0 < p ≤ q − 2r}` (nonempty
iff `q > 2r`) and is always contained in `{p < q}`: it is an open cone of
positive measure in the parameter triangle, not an edge case. C6 confirms the
characterisation on all 729 integer triples in `1..9` and two rational lines.

### Step 5 — the failure is common (CHECKED, C3, C4)

At `(p, q, r) = (1, 2, 1)`: `D_1 = 13`, `d_1 = 12/13`; `D_2 = 10`, `d_2 = 4/5`;
`D_3 = 10`, `d_3 = 9/10`; `p < q` and `g = 4(−1) + 3 + 2(−1) = −3 < 0`, so
`d_1 = 12/13 > 9/10 = max(d_2, d_3)`. Among the 343 integer triples with
coordinates in `1..7`, exactly 127 fail, and the failing set is exactly
`{p < q} ∩ {g < 0}` (C4) — the count the task quotes, now with its description.

### Step 6 — where the note's proof breaks (PROVED)

Note line 109 argues:

> `d_1 ≤ d_3` because `K(a | a, a, a) ≥ K(a | a, a, b)` (the normalizer with
> three factors `p` is smaller relative to `p³` than that with `p, p, r`
> relative to `p²r`: both are `1 − (ratio)` with the aligned triple's dissent
> mass `q³ + 4r³` over `p³` against `(rq² + r²(p + q) + 2r³)/(p²r) ≥ 4r³/p³`)

The reduction in that parenthesis is correct. Writing `N_1 = q³ + 4r³` and
`N_3 = rq² + r²(p + q) + 2r³`, so that `D_1 = p³ + N_1`, `D_3 = p²r + N_3`,

    d_1 ≤ d_3  ⟺  N_1(p²r + N_3) ≤ N_3(p³ + N_1)  ⟺  N_1 p² r ≤ N_3 p³
               ⟺  N_1/p³ ≤ N_3/(p²r),

exactly the comparison the note sets up. What fails is the bound used to close
it: the note bounds the right side below by `4r³/p³`, whereas the target is
`N_1/p³ = (q³ + 4r³)/p³`, and `4r³ < q³ + 4r³` strictly for every `q > 0`. The
chain therefore establishes nothing for any positive `q`: the dropped term is
the `q³` in `d_1`'s own dissent mass. Clearing the correct comparison gives
`p N_3 − r N_1 = r·g`, i.e. the condition is exactly `g ≥ 0` of Step 3 — which
is false on a set of positive measure. The defect is a dropped term in a bound,
not a mis-stated definition, and it is the only step of T1(a) that fails:
Steps 1 and 2 (closed forms, monotonicity) are untouched.

### Step 7 — off `𝒟*` the domination itself fails (PROVED; CHECKED, C8)

T1(a) is used only to identify `ε₂`, so the question is whether T1(b)'s
conclusion `ξ_x ≤ η'_x` survives with the note's `ε₂ = max(d_2, d_3)`. It does
not. The note's coupling drives both chains from the same uniform `U_x`:
`ξ_x = 1{U_x < 1 − K(a | v-preds)}` and `η'_x` by its own threshold. A site
whose three `v`-predecessors are all `a` but which has exactly one `1`-predecessor
of `η'` gets threshold `ε₂` from `η'` and deviation `d_1` from the law, so the
coupling requires `d_1 ≤ ε₂` there; off `𝒟*` that window `[ε₂, d_1)` is
nonempty.

The window must be reachable, which constrains the geometry. The three level-2
predecessors of `x = (1,1,1)` are `(0,1,1)`, `(1,0,1)`, `(1,1,0)`, and their
level-1 predecessors are

    (0,1,1): (−1,1,1), (0,0,1), (0,1,0)
    (1,0,1): (0,0,1), (1,−1,1), (1,0,0)
    (1,1,0): (0,1,0), (1,0,0), (1,1,−1)

so `(0,0,1)`, `(0,1,0)`, `(1,0,0)` are each shared by two of them, and only
`(−1,1,1)`, `(1,−1,1)`, `(1,1,−1)` are unshared. To raise exactly one of the
three level-2 sites to `η' = 1` while the other two stay `0`, the level-1
dissent must sit at an unshared site. Take `(−1,1,1)`. At `(1,2,1)`:

* level 1, `(−1,1,1)`: preds all `a`, `η'` threshold `ε₁ = d_1 = 12/13`, and
  `K(−a | a,a,a) = 8/13`; take `U ∈ [0, 8/13)`, giving `v = −a`, `ξ = η' = 1`.
* level 1, the other five sites `(0,0,1), (0,1,0), (1,0,0), (1,−1,1), (1,1,−1)`:
  take `U ∈ [12/13, 1)`, giving `v = a`, `ξ = η' = 0` (probability `1/13` each).
* level 2, `(0,1,1)`: `v`-preds `(−a, a, a)`, so its deviation is `d_2 = 4/5`;
  exactly one `1`-predecessor of `η'`, so its threshold is `ε₂ = 9/10`. Take
  `U ∈ [4/5, 9/10)`: `v = a` (`ξ = 0`) while `η' = 1`. This is the slack the
  note's `ε₂` buys, and it is where it is spent.
* level 2, `(1,0,1)` and `(1,1,0)`: no `1`-predecessor, threshold
  `ε₁ = 12/13 = d_1`; take `U ∈ [12/13, 1)`, giving `v = a`, `η' = 0`.
* level 3, `x = (1,1,1)`: exactly one `1`-predecessor of `η'`, so
  `η'_x = 1{U_x < 9/10}`; all three `v`-predecessors are `a`, so
  `ξ_x = 1{U_x < 12/13}`. On `U_x ∈ [9/10, 12/13)` — width `3/130` —
  **`ξ_x = 1 > 0 = η'_x`**.

The ten constraints are on ten distinct sites, hence independent, and the event
has probability

    (8/13)·(1/13)⁵·(1/10)·(1/13)²·(3/130) = 24/(13⁸·1300) = 6/265112484325 > 0.

C8 rebuilds this configuration from the menu — it re-derives each site's
deviation, threshold and admissible `U`-interval and multiplies the lengths —
rather than asserting it. So T1(b) as stated is false off `𝒟*`; on `𝒟*` it is
true, since there `max(d_1, d_2, d_3) = max(d_2, d_3)`.

### Step 8 — the minimal repair (PROVED; CHECKED, C9, C9b)

    ε₂ := max(d_1, d_2, d_3).

*Sufficiency.* This is the note's own bound. Line 109 argues: if exactly one
`η'`-predecessor is `1` then at most one `ξ`-predecessor is `1`, so at least two
of `v`'s predecessors equal `a` and
`P(ξ_x = 1 | past) = 1 − K(a | preds) ≤ max(d_1, d_2, d_3)`. That inequality is
correct and complete — the three states with at least two `a`-predecessors are
`(a,a,a)`, `(a,a,−a)`, `(a,a,b)` with deviations `d_1, d_2, d_3`. Only the next
move, replacing `max(d_1, d_2, d_3)` by `max(d_2, d_3)` via the false clause, is
wrong. So the repair needs no new argument.

*Minimality.* All three states occur at a site with exactly one `1`-predecessor
of `η'`, with positive probability: in the scaffold of Step 7, setting `v` at
`(0,1,1)` to `a`, `−a` or `b` (each an event of positive probability there,
since `K(−a | −a,a,a) = 2/5` and the four `b` together carry `2/5`) makes the
`v`-predecessors of `x` equal to `(a,a,a)`, `(a,a,−a)` or `(a,a,b)`, with
deviation `d_1, d_2, d_3` respectively — C9 checks all three. Any threshold pair
`(ε₁, ε₂)` dominating under this coupling must therefore satisfy
`ε₂ ≥ d_i` for each `i`. Hence `max(d_1, d_2, d_3)` is the least admissible
value, and C9b confirms it closes the window of Step 7 exactly (`[ε₂, d_1)`
becomes empty). On `𝒟*` it equals the note's value, so nothing downstream moves
there.

### Step 9 — what the corrected domain is for (PROVED; CHECKED, C10)

Off `𝒟*` the repair gives `ε₂ = max(d_1, d_2, d_3) = d_1 = ε₁` (C10), and the
two-level automaton collapses to the one-level noisy majority of block 12. So
the content of block 30 — separating a seed rate from a strictly larger
amplification rate — is non-degenerate **exactly** on `𝒟*`, and strictly so
where `d_1 < max(d_2, d_3)`. `𝒟*` is not a technical restriction; it is the
region where the note's own construction says something new.

## 3. Part (b): verdicts for everything that uses the clause

Ledger for the campaign's PRs #8146–#8180. Only #8174, #8175, #8176 and #8177
contain the identification at all; the other 31 branches (checked against
`origin/main` by three-dot diff, then by grep of the note each adds) have no
occurrence.

### Inside block 30's note (#8174)

| Statement | Verdict |
|---|---|
| front-matter closed forms for `d_1, d_2, d_3` | unaffected (Step 1) |
| T1(a), monotonicity in `p` | unaffected (Step 2) |
| T1(a), `d_1 ≤ max(d_2, d_3)` | **needs its own repair**: holds exactly on `𝒟*` |
| T1(a)'s proof parenthetical (L109) | **needs its own repair**: the dropped `q³` (Step 6) |
| T1(b), `ξ ≤ η'` with `ε₂ = max(d_2, d_3)` | **needs its own repair**: false off `𝒟*` (Step 7); holds on `𝒟*`; holds everywhere with `ε₂ = max(d_1, d_2, d_3)` |
| T2, `forks = |S| − 1`, `E ≤ 3(|S| − 1) + 2|A|` | unaffected — a statement about `η'` alone, with no reference to `d_i` |
| T3, `P(η'_x = 1) ≤ ε₁ R(t + ε₂/t², ε₁/t³)` | unaffected as stated (a function of `(ε₁, ε₂)`); its transfer to the formation law goes through T1(b), so holds on the corrected domain |
| T4, thresholds `p ≥ 4165` at `(p,1,2)`, `2085` at `(p,1,1)`, `8330` at `(p,2,4)`, `6247` at `(p,1,3)` | holds on the corrected domain, **numbers unchanged**: each line has `p ≫ q`, hence lies in `𝒟*`, where `max(d_1,d_2,d_3) = max(d_2,d_3)` (C7) |
| T5, ceiling `x < 4/27`, `ε₂ < 256/531441` | unaffected as a statement about the automaton; its instantiation holds on the corrected domain |
| refuter list (L187), "`d_1 > max(d_2, d_3)` at some tested line" | **needs its own repair**: as written the note declares itself refuted by a true fact; no tested line fires it (all have `p ≥ q`), but the refuter must be restated on `𝒟*` |
| summary (L193) | **needs its own repair** — restates the identification |

### Other notes of the campaign

| PR | Verdict |
|---|---|
| #8146 (block 12) | unaffected — one-level automaton, no `d_i` |
| #8168 (block 25) | unaffected — supplies T0(a)–(b), i.e. the closed forms and the monotonicity, both true (Steps 1–2); it does not assert the ordering |
| #8175 (block 31), note L92 | **needs its own repair** — restates `ε₁ = d_1`, `ε₂ = max(d_2, d_3)`. Its four lines `(453,1,2), (232,1,1), (905,2,4), (677,1,3)` all have `p ≫ q`: every number holds on the corrected domain |
| #8176 (block 32), note L93 | **needs its own repair** — same restatement. L134's floor, `d_3 = (2p + 11)/(p² + 2p + 11)` on `(p,1,2)` crossing `4/729` between `p = 367` and `368`, uses `d_3` where `p ≫ q`, so `max(d_1,d_2,d_3) = d_3`: holds on the corrected domain, unchanged by this corrigendum |
| #8177 (block 33), note | unaffected — uses `x_A = ε₂/t^c`, `y = ε₁/t³` symbolically and never restates the identification |
| #8178 (block 34), #8179 (decision record), #8180 (block 35) | unaffected — no occurrence |

### Runners

`e1, e2 = d1, max(d2, d3)` is copied verbatim into all four runners; each needs
the same one-line change, and each runs only lines with `p ≥ q`, so no executed
number moves. C7 checks all 19 distinct parameter lines of PRs #8174–#8177
(`(4165,1,2), (2085,1,1), (8330,2,4), (6247,1,3), (11,1,2), (453,1,2),
(232,1,1), (905,2,4), (677,1,3), (367,1,2), (368,1,2), (2921,1,2), (1464,1,1),
(5841,2,4), (4380,1,3), (405,1,2), (208,1,1), (810,2,4), (605,1,3)`) lie in
`𝒟*` with `max(d_1,d_2,d_3) = max(d_2,d_3)`.

Separately, and not from this corrigendum: block 32's `(p,1,2)` floor is moved
`367 → 488` by the failure of block 33's tight-sibling lemma reported under
`J:derive:tight-sibling-vacuity`. The two corrections are independent and do not
interact — that one changes `c*`, this one changes only the domain of `ε₂`.

## 4. Part (c): the exact lines that must change

Note `docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_LIFTED_BY_A_TWO_LEVEL_DOMINATION_SEEDS_AND_AMPLIFIED_NODES_IN_THE_EXPLANATION_TREE_BOUNDED_THEOREM_NOTE_2026-09-16.md` (#8174):

| line | what is there | what it must become |
|---|---|---|
| 4 | `claim_scope`: "… a site with exactly one is 1 with probability `epsilon_2 = max(d_2, d_3)` …" | `epsilon_2 = max(d_1, d_2, d_3)`, or the same scope restricted to `p ≥ min(q, p*)` |
| 32 | abstract: "`ε₂ = max(d_2, d_3)`" | as line 4 |
| 84 | definitions: "`ε₁ := d_1`, `ε₂ := max(d_2, d_3)`" | `ε₂ := max(d_1, d_2, d_3)` |
| 99 | T1 table row: "`ε₂ = max(d_2, d_3)`, decreasing in `p`" | as line 84 |
| 107 | T1(a) statement: "`d_1 ≤ max(d_2, d_3)`" | `d_1 ≤ max(d_2, d_3)` **iff** `p ≥ q` or `g ≥ 0`, `g := r p² + (q² + qr + 2r²)p − (q³ + 4r³)`; equivalently `p ≥ min(q, p*)` |
| 109 | T1(a) proof: the parenthetical bounding `(rq² + r²(p + q) + 2r³)/(p²r) ≥ 4r³/p³` | the bound is too weak (Step 6); replace by `p D_3 − r D_1 = r·g`, and keep the T1(b) line's `≤ max(d_1, d_2, d_3)` as the definition of `ε₂` |
| 134 | T4/T5 preamble: "With `ε₁ = d_1`, `ε₂ = max(d_2, d_3)`" | as line 84 |
| 175 | witness table: "executed … `d_1 ≤ max(d_2, d_3)`" | the corrected clause, with the line's own `(p, q, r)` shown to lie in `𝒟*` |
| 187 | refuter: "`d_1 > max(d_2, d_3)` at some tested line" | "`d_1 > max(d_1, d_2, d_3)`", or "`d_1 > max(d_2, d_3)` at a tested line with `p ≥ min(q, p*)`" |
| 193 | summary: "amplification noise `max(d_2, d_3)`" | as line 84 |

Runner `scripts/admissibility_rule_six_axis_formation_threshold_two_level_domination_seeds_and_amplified_nodes_2026_09_16.py` (#8174):

| line | what is there | what it must become |
|---|---|---|
| 4 | docstring Scope: "`d_1 <= max(d_2, d_3)`" | the corrected clause |
| 452 | B2 comment: "`d_1 <= max(d_2, d_3)` and the two-level coupling inequality …" | as line 4 |
| 455 | `e1, e2 = deviations(pv, qv, rv)[0], max(deviations(pv, qv, rv)[1:])` | `max(deviations(pv, qv, rv))` |
| 465 | `checks.check("B2", ok2, …)` — `ok2` includes `e1 <= e2` | keep, and add the domain test `pv >= qv or g(pv, qv, rv) >= 0` so the check is of the corrected statement, not of a fact that is true only on the lines chosen |
| 631 | `e1, e2 = d1, max(d2, d3)` in the certificate block | `e2 = max(d1, d2, d3)` |
| 669 | the printed summary string, "amplification noise `max(d_2, d_3)`" | as note line 193 |

Downstream (same one-line change, same reason):

* #8175 note L92; runner `…sharper_bad_pair_budget_false_explicit_witnesses_and_the_two_level_period_2026_09_16.py` L551.
* #8176 note L93; runner `…minimal_marked_tree_family_constant_at_least_one_exact_certificates_and_the_tree_route_floor_2026_09_17.py` L443.
* #8177 runner `…rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17.py` L553 and L564 (note text unaffected).

Per the probe rules nothing was edited; this is the list, not a patch.

## 5. What would finish it

Part (a) is complete: `𝒟* = {p ≥ min(q, p*)}` is exactly the set where the
clause holds (Steps 3–4, C6), the repair `ε₂ = max(d_1, d_2, d_3)` is sufficient
by the note's own argument and minimal for its coupling (Step 8, C9/C9b), and
off `𝒟*` the domination genuinely fails, not merely its proof (Step 7, C8).

Three things remain open, none of them needed for the corrigendum:

1. Whether a *different* coupling — not the shared-uniform one of L109 — can
   keep `ε₂ = max(d_2, d_3)` off `𝒟*`. Step 8's minimality is for the note's
   coupling; a monotone-rearrangement coupling would face the same conditional
   deviation `d_1` at a one-predecessor site, but that is an argument not made
   here. Listed as open, not as ASSUMED: nothing above uses it.
2. Whether `𝒟*` is worth widening by strengthening the automaton: off `𝒟*` the
   repaired automaton degenerates (Step 9), so a genuinely two-level statement
   for `p < min(q, p*)` needs a different amplification rule, e.g. one keyed to
   *which* predecessor dissents.
3. The `p*` half-line has irrational endpoints, so any executed witness table on
   a `(p, q, r)` with `q > r` and `p` near `p*` must test `g ≥ 0` in exact
   integer arithmetic rather than comparing to a decimal `p*`. `g` is a cubic-free
   integer polynomial, so this is free; C6 does it that way.

Nothing above imports a theorem from outside the notes; the only external tool
is exact polynomial algebra, re-checked in `check.py`.
