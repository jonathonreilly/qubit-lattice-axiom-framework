# GOAL — block 17: the static six-axis law at strong coupling — long-range order and several Gibbs states by reflection positivity, a chessboard estimate and Peierls counting (2026-09-15)

**Owner directive (2026-09-15):** don't stop; assess the next lane at each conclusion; no subagents; derivations over computation.

**Why this block.** Block 03 (on `main`) proved the static law's uniqueness region on `Z³` (one Gibbs state where the one-site influence sum is below one). The strong-coupling side — "one law or several" for the static reading — is open on `main`, and blocks 13–16 make the static reading the one that carries the repository's Green functions. A rigorous route exists at scope with crude but explicit constants: reflection positivity through site planes (no condition on the weights), the chessboard estimate, a crude bound on the disseminated partition function, Peierls counting of bad-bond surfaces on the torus, and the passage from long-range order to several Gibbs states through tail triviality. The result is the two-sided picture: uniqueness below block 03's thresholds, several states above an explicit (large) ratio `p/max(q,r)`.

**Object.** The static law of the six-axis product rule: on the torus `T_L = (Z/2L Z)³`, `μ_L(v) = Π_{bonds} φ(v_x, v_y)/Z_L`, `φ = p, q, r` on same, antipodal, orthogonal pairs, positive weights; on `Z³` the Gibbs states of the specification with these weights. Executed at `(p, 1, 2)`.

**Contract.**
- T1 (spectrum and symmetry): the eigenvalues of `φ` are `Z_1`, `p − q` (three times), `p + q − 2r` (twice); the weight matrix is invariant under the full cube group including reflections, which acts transitively on the six values.
- T2 (reflection positivity): for reflections of the torus through planes containing sites, `E_L[F · θF] ≥ 0` for every function `F` of the closed half — proved for every positive weight matrix, no positivity condition on `φ` needed; executed exactly on a ring and on a `4×2` torus.
- T3 (chessboard estimate): for events attached to distinct unit cells and reflected by site reflections, `μ_L(∩ A_c) ≤ Π_c μ_L(A_c disseminated)^{1/|cells|}` — re-proved by the iterated Cauchy–Schwarz argument; executed on the ring.
- T4 (the disseminated bound): the probability that all bonds of one direction are bad satisfies `μ_L(all dir-i bonds bad)^{1/N} ≤ 6 m/p`, `m = max(q, r)`, `N = (2L)³`; executed on small tori.
- T5 (Peierls on the torus): the number of connected sets of `n` bonds containing a given bond is at most `(e·11)^{n−1}`; a set of `n` bad bonds has probability at most `(6m/p)^{n/3}`; hence `μ_L(v_0 ≠ v_x) ≤ Σ_{n ≥ 6} 3n (e·11)^{n−1}(6m/p)^{n/3} + (winding term) ≤ 1/2` for `p ≥ p_0(m)` explicit and `L` large; executed: the counts for `n ≤ 5`, the series bound, `p_0` exact.
- T6 (from long-range order to several Gibbs states): every limit point of `μ_L` is a translation-invariant Gibbs state with `μ(v_0 = v_x) ≥ 1/2` for all `x`; a unique Gibbs state would be extremal, hence tail-trivial, hence short-range correlated, contradicting long-range order; so there are at least two Gibbs states, and the symmetry orbit of any non-symmetric extremal one has at least two and at most six members. Re-proved at scope (extremal ⇔ tail-trivial; tail-trivial ⇒ short-range correlations; torus limits are Gibbs).
- N-gate: this is a positive statement (several states) resting on a negative (no unique state); walls and escapes named. The threshold is crude; no claim of sharpness.

**Lens pass (self-run panel).**
- *"Reflection positivity needs a positive-definite coupling."* For reflections through bond midplanes, yes; for reflections through site planes the shared plane makes `E[F θF]` a sum of squares for any weights. The chessboard estimate here uses site reflections only, because bond events are disseminated by site reflections.
- *"The threshold is absurdly large."* Yes (`p_0 ≈ 10^5–10^6` times `m`). The theorem is existence with explicit constants; sharpening is a separate task. Block 03's uniqueness thresholds and this one leave a wide undecided band, stated as such.
- *"Long-range order on the torus is not a Gibbs-state statement."* T6 bridges it; every step re-proved or reduced to a standard measure-theoretic limit theorem, named as such.
- *"Is this the formation law?"* No: it is the static law, the reading that the rest of the repository uses; block 12's obligation for the formation law stands. Stated in the boundaries.

**Forbidden phrases (beyond the lane's standing list):** "phase transition", "the physical phase", "converge", "emergent", "certified", "sharp threshold".

**Prior-art search at `origin/main`.** `git grep -l -iE "chessboard|reflection positiv|peierls|long-range order|symmetry break" -- 'docs/ADMISSIBILITY*.md'` → Dirac–Kähler carrier notes (reflection positivity in a different sense: OS positivity of a Gaussian carrier) and the two-site criterion note (naming an ordering argument as open); nothing on the six-axis static law's ordered side. Open PRs: none on it (#8146 is the formation law's strong-coupling side).
