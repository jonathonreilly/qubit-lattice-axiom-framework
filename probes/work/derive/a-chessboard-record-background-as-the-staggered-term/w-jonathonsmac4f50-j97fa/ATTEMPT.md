# a-chessboard-record-background-as-the-staggered-term, attempt a2: block 17 has no chessboard phase

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-j97fa`, task
`J:derive:a-chessboard-record-background-as-the-staggered-term:a2`. There were no prior attempts at claim time. Blocks 17, 53,
54 and 77 were supervisor-run in the same model family, so this is not independent of them.

**What I read.** I read block 17's note (PR #8151) and block 77's note (PR #8612) on their branches. I did not read the fork
probe or the notes of blocks 76 and 78 in full; their content enters only through the unit's summary. Block 76's "a chessboard
of clocks is invisible" is re-derived here (step 5). The parked decisions are not touched.

## 1. What is claimed

**The premise fails.** The unit states that "Block 17 (#8151) found chessboard-ordered Gibbs states of the six-axis static law
of records". Block 17's note says otherwise:
- **"Chessboard" names its method.** In block 17 the word refers to the reflection-positivity chessboard estimate, T3
  ("Theorem T3 — the chessboard estimate", line 165).
- **The ordered states are uniform.** Its Gibbs states are translation-invariant, with `μ(v₀ = v_x) ≥ 1/2` for every `x`
  (T5, T6; the note at lines 264–265). That order is **agreement** of contents, the same at every site.
- **No pattern appears.** The note never mentions a sublattice, a staggered pattern or an antiferromagnetic pattern.

In that static law every site carries a record. So the supplied clause ("a record's presence at a site adds a coin-scalar
on-site energy `c`") adds the same `c` everywhere. That is an offset and **no staggered term**: at the eight zeros the coin
vector still vanishes (block 77 T1), and no rest energy arises. The route "block 17's chessboard states supply block 77's
staggered term" fails at its first step.

**Conditional results.** Suppose a record background on one sublattice were supplied by some other means (it is not in any
block read here). Then the clause gives `a₀(x) = c/2 + (c/2)ε(x)`, and:

- **(a) The masses.** The energies are exactly `c/2 ± √(c²/4 + (2a(3 − 2|n|))²)` at the eight zeros.
  - With `a = 0` every species has the same rest energy `|c|/2`. There is **no species dependence**, so the unit's HIT
    condition is not met (block 77 T3).
  - With `a ≠ 0` the pairs `(n, n + (111))` have `√(c²/4 + 36a²)` and `√(c²/4 + 4a²)`. That is block 77 T4's split with
    `m = c/2`: the dependence is the `a`-term's, not the background's.
  - **The offset does not move the sea's filling.** The two branches multiply to `E₊E₋ = −λ² ≤ 0`, so one branch is never
    above zero and the other never below.
- **(b) The rates.** The same background sources a chessboard of clocks, `u = U + δε`.
  - Every nearest-neighbour hop is rescaled by the same `e^U`, since `ε_x + ε_y = 0` for neighbours. The on-site term is
    rescaled by `e^{u_x}`.
  - So exactly `φ(H_hop + a₀)φ = e^U[H_hop + (c/2)e^δ(1 + ε)]`: the background is felt **only** through the on-site term,
    and the clock chessboard multiplies its amplitude by `e^δ`.
  - Block 53's rule, with the zero-sum part of the source `log κ·(1 + ε)/2`, gives `δ = (log κ)/4`. Hence
    **`m = (c/2)κ^{1/4}`** in units of the hop.
- **(c) Covariance.**
  - `ε` is invariant under all 48 cube symmetries about a site, so under the 24 proper rotations. It changes sign under
    every odd translation.
  - A chessboard background therefore keeps rotation covariance, breaks the odd translations, and comes in two copies (which
    sublattice holds the records).
  - A coin scalar singles out no content direction, so "no possibility is privileged" is not violated by the term. The
    sublattice choice is a broken symmetry of the background, not a privilege in the rule.
- **(d) The bare energy.**
  - The walker's rest energy would need `c = 2mκ^{−1/4}` per recorded site.
  - Block 40's binding scale `c₀ = 6/(p + q + 4r)` is a dimensionless pair weight between records, not an energy. Relating
    the two needs a clause that converts record weights into walker energies. None is supplied, so (d) is not determined
    here.

## 2. Steps

1. **CHECKED (P1) — reading block 17.** check.py fetches block 17's branch and locates the four quoted phrases by line: the
   T3 heading, the translation-invariant Gibbs state, `μ(v₀ = v_x) ≥ 1/2`, and the claim scope's "v_0 = v_x with probability
   above 1/2". It also confirms that "sublattice", "staggered" and "antiferro" do not occur in the note.

2. **PROVED / CHECKED (P2) — what the clause does with block 17's states.** Every site is recorded, so `a₀(x) = c` for
   every `x`. At the zeros, `sin(πn_j) = 0` and the level is `a₀ + c + 2a(3 − 2|n|)` (block 77 T1): an offset, with no gap.

3. **PROVED / CHECKED (C1) — the masses.**
   - Under `k → k + (π,π,π)`, `cos k_j` and `sin k_j` change sign, so the hops' symbol `h(k)` goes to `−h(k)`.
   - The staggered term couples `k` with `k + (π,π,π)`, giving the `4 × 4` block `[[h + c/2, c/2], [c/2, −h + c/2]]`.
   - Its eigenvalues are `c/2 ± √(c²/4 + λ²)`, where `λ` runs over the eigenvalues `2aΣcos k ± |s|` of `h`.
   - At the zeros `λ = 2a(3 − 2|n|)`. sympy computes the eigenvalues at all eight zeros exactly.

4. **CHECKED (C2) — the torus, and the filling.**
   - The real-space generator on the `4³` torus (`a = 0.13`, `c = 0.6`) has exactly the formula's spectrum, to
     `4.7·10⁻¹⁵` (floating point).
   - `(c/2 + √(c²/4 + λ²))(c/2 − √(c²/4 + λ²)) = −λ²` (sympy).

5. **PROVED / CHECKED (C3) — the rates.**
   - `φ_xφ_y = e^{(u_x + u_y)/2} = e^U` for neighbours, and `φ_x² = e^U e^{δε(x)}`.
   - `(1 + ε)e^{δε} = (1 + ε)e^δ`, because `1 + ε` vanishes where `ε = −1`.
   - The identity is checked on the torus to `10⁻¹²`.
   - For block 53, the chessboard ansatz `u = U + δε` gives `u − (mean of the six neighbours) = 2δε`. Setting this equal to
     the zero-sum part `(log κ/2)ε` of the source gives `δ = (log κ)/4` (sympy). The uniform part of the source is a global
     rescaling of rates, invisible because only ratios mean anything (block 53).

6. **CHECKED (C4) — covariance.** Exact on all points with `|coordinates| ≤ 3`, for all 48 cube symmetries and three odd
   translations.

## 3. Where the route stops

- **At step 1.** No block read here supplies a sublattice record background.
  - A chessboard of occupancy needs neighbouring records to repel: every pair weight `cω` below the empty-bond weight 1.
  - That is below block 39's neutral scale, where block 39 T5 says reflection positivity fails. So the reflection-positivity
    chessboard machinery that block 17 uses would not be available to prove such an order.
  - At or above the neutral scale, aligned records attract (`c₀p > 1` when `5p > q + 4r`) and the law clumps.

  This remark is not proved here.
- **What is not read or computed.**
  - The fork probe and blocks 76 and 78 were not read in full.
  - The exchange sign and hard-core interaction of block 78 are not used.
  - The sea's energy as a function of the background, block 76's machinery, is not computed.

## 4. What would finish it

1. **A mechanism for a sublattice background.** One candidate is a repulsive regime of the record gas, or a clause giving
   the two sublattices different roles. Whether any of them respects the axioms' covariance would then be the question.
2. **A clause relating record weight to walker energy.** Without it, (d) cannot be answered.
3. **A reread of the unit's premise** by the supervisor. The fork probe or its summary appears to have taken the name of
   block 17's method for the pattern of its phase.

## 5. Running it

```
python3 probes/work/derive/a-chessboard-record-background-as-the-staggered-term/w-jonathonsmac4f50-j97fa/check.py
```

It needs `numpy`, `sympy` and `git`: P1 fetches block 17's branch from `origin`. It runs 6 checks (P1, P2, C1–C4) in a few
seconds.
