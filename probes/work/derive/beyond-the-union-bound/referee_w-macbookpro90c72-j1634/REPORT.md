# Referee report: J:derive:beyond-the-union-bound:a3

Author: `w-jonathonsmac4f50-jae8a` (claude-opus-5). Referee: `w-macbookpro90c72-j1634` (grok-4.6).
Problem: a count of explanation trees (or a canonical substitute) whose generating function has radius beyond the tree recursion's `x = 4/27`, with an exact rational super-solution and domination on small cones.

## Does the attempt prove that statement?

Yes, as a PARTIAL. The object counted is not the family `𝓔` of marked explanation trees (block 25/30) but the *single* refinement history that block 30's construction outputs on each configuration. That is candidate (i) in the form "minimal trees under a canonical order". The new recursion

```
Z = 1 + σ (2 + ε₂/σ)³ Z / (1 − 6 ε₁ Z / σ)³
```

has domain limited by `27 ε₂ < 1` rather than by `x = 4/27`, and the four rational certificates (`p ≥ 84, 44, 168, 125` on the four lines) sit at `ε₂ > 4/729 > 256/531441`, so they are outside both tree-route ceilings (`p > 367` at budget `c = 1` and `p > 4150` at budget `c = 2` on `(p, 1, 2)`). The located strength `p ∈ (10.5, 11)` is not claimed and is out of the route (`ε₂(11,1,2) = 43/164 > 1/27`).

H1–H3 are the statement attempted. H1 is the bound `P(η'_x = 1) ≤ ε₁ Z̄` (and `P(v_x ≠ a) ≤ ε₁ Z̄` via block 30 T1). That is the task's "provably smaller count", not a neighbouring lemma about a different automaton.

## Step-by-step

**Step 1 (domination) — holds, ASSUMED as block 30 T1 plus CHECKED A1–A2.** Independent: the three closed forms match `1 − K`; the `p`-derivatives are the stated negative numerators over squares; `d_1 ≤ max(d_2, d_3)`; every one of the 216 predecessor triples with three `a`'s (resp. exactly two) dissents with probability `≤ ε₁` (resp. `≤ ε₂`) at the four certificate points and at `(11, 1, 2)`. `(168, 2, 4)` is homogeneous to `(84, 1, 2)`.

**Step 2 (construction) — holds, ASSUMED as block 30 T2 (which imports block 25 T3) plus CHECKED.** The notes state T2.1–T2.4 as used: terminals are excuses, which are axis-moves; `d_k = k` exactly on bad pairs; the Steiner subtree of the cluster–fork graph has fork-vertices of degree two; `Φ` rises by at least `1 − b`; a cluster and a bad pair appear at most once; termination at seeds. Independent explainer written from those paragraphs (not the author's copied runner) succeeds on every configuration of the depth-2 cone (`308`, of which `234` have `η'_x = 1`) and the depth-3 cone (`47952` / `38752`): moves, bad-pair rule, degree-2 forks, spanning identity `Σ_X Span = Σ M_k(u_k)`, excuse identity `Σ M_k(u_k) = Span(K) + 1 − b`.

**Step 3 (two counts) — holds.** `|S| = F + 1` is the tree accounting: start with one cluster, each refinement replaces a cluster by a tree of `n` clusters and `n − 1` forks. `R ≤ F + B` is `Σ (1 − b) ≤ ΔΦ = F` from T2.4. Independent: both identities on every depth-2/3 configuration above.

**Step 4 (encoding determines seeds and bads) — holds.** The two-pass placement is the pole rule of block 25 T3 (ASSUMED) plus the moves of step 2a. Independent: the abstract encoding rebuilt from the explainer's Steiner data, with no positions stored, reproduces the realized seed set and bad set on every depth-2/3 configuration; those sites are respectively 0-predecessor and 1-predecessor 1-sites of that configuration, pairwise distinct, and disjoint from each other.

**Step 5 (union bound over histories) — holds.** The construction is deterministic, so `{η'_x = 1}` is covered by the disjoint events `{h(ω) = h}`. For a *fixed* history, `S(h)` and `B(h)` are fixed sites (step 4), and `{h(ω) = h}` sits inside `{U_z < ε₁ on S} ∩ {U_z < ε₂ on B}`. The inequality `ε₁^{F+1} ε₂^B ≤ ε₁ σ^R (ε₁/σ)^F (ε₂/σ)^B` uses `R ≤ F + B` and `σ ≤ 1`. Independent: on both complete cones, the sum of configuration weights mapped to each encoding is `≤ ε₁^{|S|} ε₂^B`; the total equals an independent level-by-level DP for `P(η'_x = 1)` and is `≤` the history union, which at the certificate points is `≤ ε₁ Z̄`.

**Step 6 (grammar generating function) — holds.** The four Steiner shapes with three labelled terminals (one cluster; two clusters in 3 ways; a path of three in 3 ways; a Y with non-terminal centre), with an arm `a = Σ_{j≥1} (6φ)^j W^{j−1} = 6φ/(1 − 6φ W)`, sum to `W(1 + W a)^3 = W / (1 − 6φ W)^3`. Moves contribute `(2 + r)^3`. Independent: that algebraic identity; a shape-based coefficient enumerator (not the author's hang/grouping recursion) agrees with iteration of `Z = 1 + σ(2+r)^3 Z/(1−6φ Z)^3` up to `σ^2 φ^2` and `σ^3 φ`; realized `(R, B, F)` counts on the two cones never exceed the coefficients. Extra grammar objects (non-embeddable trees, coincident-pole overcount) only enlarge the upper bound.

**Step 7 (super-solution) — holds.** The map `Z ↦ 1 + μ Z (1 − c Z)^{−3}` is increasing on `[0, 1/c)`. Height truncation still sums unbounded arms, which is an upper bound on finite histories whenever `c W_h < 1`. Induction from `Z̄ ≥ 1` and `Z̄ ≥ f(Z̄)` gives `W_h ≤ Z̄`. Finite termination is T2.4.

**Step 8 (certificates) — holds.** Independent exact arithmetic: each listed `(σ, Z̄)` satisfies `0 < σ ≤ 1`, `c Z̄ < 1` and `Z̄ ≥ 1 + μ Z̄ / (1 − c Z̄)^3` at the integer threshold, with `ε₁ Z̄ < 3·10^{-4}`. Monotonicity in `p` (A1) reuses the same `Z̄` for every larger `p` on the line. At every certificate point `ε₂ > 4/729 > 256/531441`, and `d_3(4150) > 256/531441`, `d_3(367) > 4/729` on `(p, 1, 2)`.

**Step 9 (this route's ceiling) — holds.** Independent: `σ(2 + ε/σ)^3 − 27 ε = (σ − ε)^2 (8σ + ε)/σ^2 ≥ 0`, so `μ ≥ 27 ε₂` with equality at `σ = ε₂`. Any super-solution needs `μ < 1`, hence `ε₂ < 1/27`. On `(p, 1, 2)`, `ε₂ = d_3` and `d_3(57) = 125/3374 > 1/27 ≥ d_3(58) = 127/3491`. At `(11, 1, 2)`, `max(d_2, d_3) = 43/164 > 1/27`.

## Classic failure modes

- Quantifier: none swapped. The bound is for every site `x`, via a translation-invariant generating function; near the initial plane it is even cheaper (`Z̄ ≥ 1` covers a lone seed).
- Induction at the wrong level: the height induction is on the grammar, not on the lattice; T1–T2 are not being proved here.
- Bound only at checked sizes: the cone checks are domination evidence, not the proof. The proof is the grammar union bound, which does not depend on a cutoff depth.
- Outside theorems: block 30 T1–T2 and block 25 T3 are ASSUMED as stated in those notes (PR #8174, #8168). They are used at the stated scope (two-level `η'`, extended construction, spanning lemma with three poles). No other import.
- Circular: none. The located threshold `p ∈ (10.5, 11)` is not an input. The tree-route ceilings are compared, not assumed as bounds on `η'`.

## Verdict

The PARTIAL survives. First failing proof step: none. First failing independent check: none.

`HIT: confirmed` — see `check.py`.
