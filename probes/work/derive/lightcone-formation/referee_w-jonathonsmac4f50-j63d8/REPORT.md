# Referee report: J:derive:lightcone-formation:a5

**Author:** w-macbookpro90c72-j795a (grok-4.6).
**Referee:** w-jonathonsmac4f50-j63d8 (claude-opus-5).
**Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `65e04d16`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (sympy, mpmath at 30 digits). A linear
program gives a numerical picture, which is information only and not a claim.

## The problem and the claim

The task asks for five things about the symmetric 7-stencil sphere formation law:
- (a) reversibility and the Gibbs identification;
- (b) long-range order at large `β`;
- (c) two-sided bounds on the kernel;
- (d) the uniqueness region at small `β`;
- (e) the comparison with the static comparator.

The attempt claims (d), Dobrushin uniqueness for every `β < 3/7`, and the two-sided envelope of the *linear* kernel for
(c). It does not claim long-range order or a nonlinear kernel bound.

## Step by step

**Steps 1–4 (the vMF covariance): hold.**
- The inequalities `e^t > 1 + t` and `e^u (1 − u) ≤ 1` are correct.
- The Euler-product bound `sinh κ < κ e^{κ²/6}` holds, giving `A'(κ) < 1/3`.
- `q' = κ r` and `r' = κ sinh κ` hold, giving `A(κ)/κ ≤ 1/3`.
- L1 re-verifies the symbolic derivatives, both limits `1/3` at `κ → 0`, and both inequalities at 400 points of `(0, 40]`.
- So `‖Cov_vMF(κ)‖ ≤ 1/3`.

**Step 5 (the Dobrushin coefficient): does not follow.**
- The first half is right. The Jacobian of the mean map `m(S) = A(β|S|) S/|S|` is `β[A' P + (A/κ)(I − P)]`, with `P` the
  projector on `S` (L2). Its norm is therefore at most `β/3`, and the mean map is `(β/3)`-Lipschitz.
- The step then treats this as the Wasserstein-1 influence of a predecessor on the new record. It is not.
- W1 between two laws is at least the distance between their means, not at most.
- The W1 rate of the kernel `S ↦ vMF(βS)` in a direction `u` is `β` times the supremum, over chord-1-Lipschitz `f`, of
  `Cov_κ(f, u·s)`. Taking `f = u·s` recovers only the covariance eigenvalue, which is a lower bound.

L3 gives a witness at `κ = 3`. The function `f(s) = −|s − n|` is 1-Lipschitz, and
`d/dt E_{vMF((3+t) n)} f = Cov(f, s·n) = 0.113646 > A'(3) = 0.101147`. So the longitudinal W1 rate exceeds the
covariance eigenvalue, and `‖Cov‖ ≤ 1/3` does not control the Dobrushin coefficient.

The conclusion `β < 3/7` is not refuted. A numerical linear program (L4, 300 points on the sphere) finds the W1 rates in
the longitudinal and transverse directions at or below `1/3` for `κ ∈ [0, 3]`, with the maximum at `κ = 0`. At `κ = 0` the
value is exactly `1/3`: the reflection coupling and the test function `f = s₁` both give it.

What is missing is the lemma `sup_{u, f 1-Lip} Cov_κ(f, u·s) ≤ 1/3` for every `κ`, over all directions `u`, including
mixed ones. With it, the Wasserstein contraction `7β/3 < 1` would follow.

The Dobrushin–Vasershtein uniqueness theorem for the synchronous automaton is itself an outside theorem, used without
being listed as ASSUMED.

**Step 6 (linear envelope): holds.**
- `1/(1 − φ²) = 49/(E(14 − E))`, with `φ = 1 − E/7`.
- `E ≤ 12` on `Z³`, attained at `(π, π, π)`.
- So `(7/2)/E ≤ S/σ² ≤ (49/2)/E` (L5).
- This bounds the linear model only, as the attempt says.

## Classic failure modes

- *An outside principle beyond its hypotheses.* A Lipschitz mean map is used as a Wasserstein contraction (Step 5).
- *Bound only at checked sizes.* Not an issue. Steps 1–4 are proved for every `κ`.
- *Quantifier and circularity.* None.

## Verdict

**First failing step: 5.** The uniqueness threshold `β < 3/7` does not follow from `‖Cov_vMF‖ ≤ 1/3`. The numerical
Wasserstein rates are consistent with it, so the gap is a missing lemma, not a counterexample.

Steps 1–4, which bound the vMF covariance, and Step 6, the linear envelope, hold and were re-verified independently.

`check.py` prints `SUMMARY: fails at step 5 - ...` and no `HIT: confirmed` line.
