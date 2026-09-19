# Referee report: J:derive:re-recording:a4

**Author:** w-macbookpro90c72-j0cfe (grok-4.6).
**Referee:** w-jonathonsmac4f50-jf4b6 (claude-opus-5).
**Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `82832540`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (exact integers and rationals, sympy).

## The problem and the claim

The task asks, without assuming that re-recording is admissible, for three things:
- (a) Asynchronous re-recording has the static law as its stationary law, proved by exact detailed balance.
- (b) Synchronous re-recording is reversible with respect to `π ∝ Π_x Z(S_x)`. Compare its small-window marginals with the
  static law, decide whether it orders, and give its transverse kernel at large `β` for the sphere.
- (c) Which results transfer to each case.

The attempt claims all of this, including, in (b), that the synchronous law has the same `1/E` kernel with "IR stiffness
`2β` against the static law's `β/2`", and that the synchronous law orders at large `β` in the same sense as the static law.

## Step by step

**Step 1 (pairing identity): holds.**
- It is a reindexing over an undirected (multi)graph.
- Q1 checks it on 241056 configuration pairs on C4 (six-axis vectors).

**Step 2 (asynchronous detailed balance): holds.**
- The static weight's one-site conditional is the rule, so each update is a Gibbs kernel for `μ`, whatever the clock
  rates.
- Q2 checks `μ(s) K(a | S_x) = μ(s_{x←a}) K(s_x | S_x)` at every configuration, site and value: 124416 cases on C4 and on
  the 2×2 torus with multiplicity 2, for both Boltzmann `e^β = 3` and product `(3, 1, 2)`.
- Uniqueness on a finite window with `φ > 0` follows from irreducibility (finite menu). For the sphere menu on a finite
  window it is the standard positive-density argument, which the attempt uses without restating.

**Step 3 (synchronous reversibility): holds.**
- `π(s) P(s → s') = Π_x Π_{y∼x} φ(s'_x, s_y)` is symmetric under `s ↔ s'`, by Step 1 and the symmetry of `φ`.
- Q3 checks 112320 configuration pairs on C4.
- One point of notation: for the six-axis menu, `Z` depends on `S_x` itself (`Σ_i 2 cosh(βS_{x,i})`), not only on
  `|S_x|`. The attempt's own check uses `Z(S_x)`.

**Step 4 (the two laws differ): holds.**
- Q4 recomputes `TV(π, μ) = 39161524/79474827` on C4 and `122900831405716/159789899835723` on the 2×2 torus, with 14
  distinct values of `π/μ` on each. These are exactly the author's numbers.

**Step 5 (sphere kernel at large `β`): the expansion holds; the stated stiffness comparison does not follow.**
- *The expansion.* Expanding for small transverse spins, `Σ_x(|S_x| − 6) = Σ_k (−E + E²/12)|θ_k|²` and
  `Σ_bonds(s·s' − 1) = −½ Σ_k E|θ_k|²`. Q5 checks both with exact series for single cosine modes at four wavevectors on
  `(Z/4)³`.
- *What it implies.* `−log π = β Σ_k E|θ_k|² + …` and `−log μ = (β/2) Σ_k E|θ_k|² + …`. The synchronous quadratic form is
  twice the static one, so its transverse variance is `1/(2βE)` against block 19's `1/(βE)`.
- *The flaw.* The attempt concludes "IR stiffness `2β` against the static law's `β/2`". That is a factor 4, and it does not
  match the step's own displayed exponents, `β` against `β/2`. The same factor-4 wording appears in the statement, the
  HIT line and the SUMMARY line. The attempt's `check.py` line "stiffness-ratio-2" prints the correct ratio 2.
- The `O(1)·E` correction from `−log(β|S|)` is relative `O(1/β)`, as section (4) says. Its θ-dependence is not
  `O(log β)`, as a remark in step 5 suggests; only the constant is.

**Step 6 (ordering): not proved.**
- Q6 reproduces the C4 ratios of the all-`+z` weight to a one-site opposite flip: static `p⁴`, and synchronous `121/64`,
  `3481/729`, `14641/625`, `187489/2401` at `p = 2, 3, 5, 7`.
- A four-site ratio is not an ordering statement on `Z³`, and the step marks the Peierls argument ASSUMED. So the sentence
  in (b), "The chain orders in the same sense as the static law at large `β`", is not established.

**Step 7 (transfer): holds for (a), qualitative for (b).** The table's entries for (a) follow, because the measure is the
static law. The entries for (b) are consistent with Steps 4 and 5 once the stiffness ratio reads 2.

## Classic failure modes

- *A conclusion that contradicts the step's own formula.* The stiffness ratio in Step 5.
- *Bound only at checked sizes.* The ordering sentence rests on C4.
- *Quantifier and circularity.* None.

## Verdict

**First failing step: 5**, for its stated stiffness comparison (a factor 4 where the exponents give 2).

The ordering sentence of (b) is not proved.

Everything else survives and was re-verified independently:
- the pairing identity;
- asynchronous detailed balance for both rules;
- synchronous reversibility with respect to `Π_x Z_x`;
- the exact TV values;
- the spin-wave expansion `−E + E²/12`, whose correct reading is the transverse kernel `1/(2βE)`, half the static
  `1/(βE)`;
- the C4 ratios.

`check.py` prints `SUMMARY: fails at step 5 - ...` and no `HIT: confirmed` line.
