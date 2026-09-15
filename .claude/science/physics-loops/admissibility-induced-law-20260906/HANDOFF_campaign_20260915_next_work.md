# Handoff — the 24-hour derivation campaign of 2026-09-15 (blocks 08–11) and the next work

For whoever picks this up: a fresh session, the owner, or me after a context reset. Everything below is checkable in the pack (`.claude/science/physics-loops/admissibility-induced-law-20260906/`) and in the PRs named. Nothing is adopted; the owner runs the review-loop and integrates by his own commits (as he did for blocks 01–05 on 2026-09-07).

## 1. What this campaign did (owner directive 2026-09-15: resync, read the latest PRs, run a 24-hour campaign on unworked lanes, proofs over computation, no subagents)

Lane map read at launch: the Codex native-fermion/U1/Ward dispatch (#8036–#8092, #8094–#8104), the clock/Maxwell physics-loop dispatch (#8106–#8136), the derivation campaign #8093 (six of eleven blocks open: #8096, #8102, #8105, #8107, #8110, #8114, #8122), the landed plane-law note (#8039, on main 2026-09-15). Chosen lane: the three-dimensional formation law of the monotone class and what follows from it — nobody else on it. Four blocks, all supervisor-run, all opened as hand-off PRs against the stack `main ← #8138 ← #8139 ← #8141 ← #8142`:

| block | PR | result in one line |
|---|---|---|
| 08 | #8138 (base main) | the `Z^3` monotone formation law: one law per box with an irreducible three-body term; no translate consistency (the first plane cannot be summed out — exact `2×2` witness; the successor/predecessor-triple lemma); the plane chain with a unique stationary law per cross-section; the causal coupling theorem: `|Cov| ≤ 4‖g‖‖h‖(3c)^{⌈d/2⌉−1}`, mixing at `c/(1−2c)`, and for `c < 1/3` a unique translation-invariant law on `Z^3` with exponential decay; `c = 27/110, 10650/63407, 5782/30885` at the silent triples — inside |
| 09 | #8139 | the `Z^3` law is Gibbs for `−log K` on edges + `log K_3` on predecessor triples, Markov for the axial+face-diagonal graph and **not** for the nearest-neighbor graph; a full-support law determines its finite-range specification, so it differs from **every** static Gibbs law on `Z^3` (unique or not); eight pairwise distinct corner laws forming one rotation orbit, their mixture covariant but not ergodic; the sweep's imprint (the plane chain irreversible on the `2×2` column) |
| 10 | #8141 | the recorded-set Gibbs theorem: every formation law, for every order on every finite window, is Gibbs with `−log K` on edges and `+log K_k` on recorded sets; Markov graph = the recorded-set graph; nearest-neighbor Markov **iff** no site records two neighbors; `k`-body terms irreducible for `k = 2..6` at the declared triples; plaquette `12/13`, star `165/169` |
| 11 | #8142 | the exceptional locus of the three-body term, complete: it vanishes at exactly six points up to scale (the constant rule; `p = q = t* r`, `t³−3t²−6t−1`; `(1,ρ) r`, `(ρ,1) r`, `x³−3x²−15x−19`; a sextic mirror pair with `p = ψ(q)`); the two-body term never vanishes; the pair part survives, so blocks 09–10 hold everywhere nonconstant |

Layman's summary of the arc: forming records one site at a time with the rule produces a pattern law that is never the static law on the real lattice, because a site ends up listening to sites across the faces of the cube around it, with genuine three-way (and up to six-way) couplings the rule itself does not have; the eight ways of choosing "behind" give eight different laws whose blend, not any member, is symmetric; the finished records remember the sweep's direction; and all of this is exact, with the one exotic exception (five weight ratios where the three-way coupling disappears) found and classified.

## 2. Why the campaign stopped before 24 hours (value-gate exhaustion, per the skill's stop conditions)

After block 11 the refreshed queue held: (i) the region's boundary `3c = 1` on block 03's lines — an exact but one-step variant of block 03's threshold computation for a different coefficient (fails V5); (ii) the loci for `k ≥ 4` — block 11's mechanism on larger systems with no new premise unless a common point appears (corollary-shaped); (iii) width 6 — computation, deferred under the directive; (iv) the silent triples — heavy, unchanged; (v) strong coupling `c ≥ 1/3` — the one item with real upside, but its honest form is a Toom-type theorem (see §3), beyond a session's reach at the lane's standard of re-proving everything at scope. Filling the remaining hours with (i)–(ii) would be the corollary churn the skill forbids. Runtime used: about three and a half hours of the twenty-four (09:00Z–12:35Z).

## 3. The highest-blast-radius unattempted residual: the strong-coupling phase of the formation law

For `c ≥ 1/3` block 08's coupling says nothing. The structure there is identifiable exactly: the plane chain's kernel `r(s | a, b, c) ∝ φ(s,a) φ(s,b) φ(s,c)` is a **noisy majority rule** on three predecessors (the `x_1`-predecessor and two in-plane predecessors — the same neighborhood shape as the classical north-east-center voting automaton). Exact facts: with a unanimous triple `(a, a, a)` the site copies `a` with probability `p³/(p³ + q³ + 4r³)`; with a `2:1` triple `(a, a, b)`, `b ⊥ a`, the majority `a` wins with probability `p² r / (r(p² + q²) + r²(p + q) + 2r³)` and the majority is the most likely value iff `p > max(q, r)`. As `p → ∞` both probabilities tend to one: the sweep tends to copy the corner's value across the whole box, so the stationary plane law should have at least six extremal components (one per axis) at strong coupling — the formation law's own symmetry breaking, the counterpart of the static law's ordered phase. Proving it needs a stability theorem for noisy majority automata at low noise (the classical eroder/contour argument), re-proved at scope with explicit constants; the exact noise probabilities above are the inputs. This is the residual to attempt next, with a panel first (the owner's standing rule for direction-setting junctures). A finite-`W` exact computation of the plane chain's spectral gap as `p` grows (the `2×2` orbit quotient is 32-dimensional) is a cheap first control, not a proof.

## 4. Other next work, ranked

1. **The Toom-type non-uniqueness at strong coupling** (§3) — derivation; hard; highest value.
2. **A structural reason for the sextic pair** `(σ_1, σ_2)` of block 11 — a hidden symmetry of the six-menu's normalizer? Small if it exists.
3. **The loci for `k = 4, 5, 6`** — exact elimination on larger systems; whether any point is exceptional for two `k` at once.
4. **The region's boundary in `(p, q, r)`** — exact bracketing of `3c = 1` on the three lines; small.
5. **Width 6 by block 06's route**; **the silent triples by a non-criterion route**; **the 3D Gaussian instance** — unchanged.
6. **The random-priority law's Markov structure** — needs the owner's unlanded note as an input.

## 5. Standing rules that bit us this campaign (each cost a fold)

- **Never quote a forbidden token inside the note, even to report its removal** — the substring scan re-trips (block 09). "certified" hides inside "certified by containment" (block 11).
- **Classical names — including method names like the elimination basis and sign-change sequences — only under Prior art and Imports**; the status block and the obligation table count as sections (blocks 08, 10, 11).
- **`git rebase --onto <new-base> <old-base>` when the base branch was rewritten**; a plain rebase replays the old base's commits and conflicts (block 09).
- **Integer-weighted enumeration** with a common denominator that is a product of lcms (not the lcm of factors) turns 6^8 passes from 50 s into 3 s (block 08).
- **A refined isolating interval is narrower than any enclosure over it** — certify a root exchange against the coarse interval (block 11).
- **Algebraic-field gcds in the symbolic engine hang** — use a resultant, a lex elimination basis and reductions modulo the minimal polynomial (block 11).
- **Re-derive every number from the control's file when writing prose** — a misread `3c = 1/3` as `3c = 1` put a triple on a boundary it is not on (block 08).
- When a parent note lands on `main` mid-campaign, rebase the stack onto that `main` so it becomes a declared input (block 09), and update the earlier blocks' citations from "open PR" to "landed".
