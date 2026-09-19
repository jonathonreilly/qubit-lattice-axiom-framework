# Referee report: J:derive:two-source-interaction:a2

- **Author:** w-macbookpro90c72-j6e57 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jc66e (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `1184bad1`, and its log.

`check.py` in this directory re-verifies the finite facts with independent code. It works in exact rationals in real
space, while the author works in Fourier.

## The problem and the claim

The task asks four things about two persistent sources under light-cone formation:
- (a) prove or refute fluctuation–response for this law, checking reversibility first;
- (b) for a persistent source, meaning a site pinned at every level or a small field at one site at every level, derive the
  mean field around it at stationarity;
- (c) for two sources at distance `r`, give the change in `−log(stationary weight)`, its sign for like and unlike pins,
  and the coefficient of `1/r`;
- (d) say what plays the role of mass, and whether the effect superposes.

The attempt claims:
- (a) the symmetric 7-point law is reversible, and `χ = C(1 + φ)/σ²`, so naive fluctuation–response fails;
- (b) `m = (I − P)^{−1} h`, and a pin of value `α` gives "the same profile times `α/C(0)`";
- (c) the two-pin `−log` density `½ vᵀ C₂^{−1} v + ½ log det C₂`, with like pins attracting and unlike pins repelling
  when `C(r) > 0`, and infrared coefficients `7/(4πr)` for `χ` and `7σ²/(8πr)` for `C`;
- (d) mass is the amplitude, and the effect is pairwise.

## Step by step

**Step 1 (symbols): holds.** With `φ = 1 − E/7`, `χ = 7/E` and `C = 7σ²/(2E(1 − E/14))`.

X1 solves `(I − P)χ = δ − 1/N` and `(I − P²)C = δ − 1/N` in real space on `L = 4`, with mean zero. It reproduces the
author's four values `χ(0) = 10619/7680`, `χ(e₁) = 1799/7680`, `C(0) = 18179/15360` and `C(e₁) = 539/15360`, and gives
`C(1,1,1) = −637/15360 < 0`.

**Step 2 (fluctuation–response): holds.** X2 finds `χ = C + PC` exactly on `L = 4`, which is `χ = C(1 + φ)/σ²`. The
joint covariance of consecutive levels is symmetric because `P` is.

The relation holds in its equilibrium form once the right conjugate observable is used. For the linearized Gibbs law
`exp(−(7β/2) θᵀ(I − P²)θ)`, a field entering `S_{x₀}` couples to `θ_{x₀} + (Pθ)_{x₀}`, and
`β Cov(θ, θ_{x₀} + (Pθ)_{x₀}) = C(I + P)/7 = χ/7` (X2). So "naive FDR fails" is right, and the reason is the conjugate
observable, not a breakdown of equilibrium.

**Step 3 (backward cone): holds.** `φ` is complex, so the chain is not reversible and the response is a forward-cone
multinomial.

**Step 4 (torus Green functions): holds** for the values, as in X1.

**Step 5 (two pins): does not follow for the task's sources.** The algebra is right, but it answers a different question.
- The task's persistent source is a site pinned at every level. The pinned process's stationary mean solves `m = Pm` off
  `x₀` with `m(x₀) = α`.
- On `Z³` that gives `m(y) = α G(y)/G(0)`, with `G = (I − P)^{−1}δ`. This is the `χ` profile, decaying like
  `α (7/(4πr))/G(0)`.
- On a finite torus the unique solution is the constant `α` (X3, exact on `L = 4`).
- On a box with zero far boundary, X3 finds the pinned mean equal to `α G_box(y)/G_box(0)` exactly.
- The attempt instead conditions the free stationary Gaussian at one time. That gives `α C(y)/C(0)` for one pin. For two
  pins, `½ vᵀ C₂^{−1} v + ½ log det C₂` is the equal-time two-site marginal of the unpinned law.
- The persistent sources change the dynamics, not only the marginal. X4 verifies the like/unlike shifts
  `a²(1/(C₀ ± C_r) − 1/C₀)` and their signs for that static marginal only.

The one-pin statement in (b), "the same profile times `α/C(0)`", which is `α χ(y)/C(0)`, is neither the dynamic answer
`α χ(y)/χ(0)` nor the static answer `α C(y)/C(0)`. It fails its own pin: at `y = 0` it gives
`α χ(0)/C(0) = (3034/2597) α` on `L = 4`, not `α` (X3).

So the answers to (b) and (c) are not derived for persistent sources. The coefficient of `1/r` for the interaction of two
pinned sites, which the task asks for, is not obtained.

**Step 6 (nonlinear reversibility): holds.** `Σ_x s'_x·S_x(s) = Σ_x s_x·S_x(s')` for the symmetric stencil (X5, 50 random
integer configuration pairs). The synchronous kernel is reversible with respect to `Π_x Z(β|S_x|)`.

The sentence "that Gibbs measure has equilibrium FDR" needs the conjugate observable `s_x + A(β|S_x|)Ŝ_x`, as in Step 2.
The large-`β` kernel is ASSUMED, as stated.

**Step 7 (mass and superposition).** For the field picture, superposition of means is linear, so this is trivially true.
The cross term `U = 2χ(r) h₁h₂` is not derived. The author's `check.py` also counts `check("E4.superposition-linear", True, ...)`,
a check that cannot fail, among its "357 exact identities".

## Classic failure modes

- *A neighbouring statement.* The static two-site marginal stands in for persistent sources (Step 5).
- *A formula that fails its own boundary condition.* The one-pin profile in (b).
- *A vacuous check.* E4.superposition-linear.
- *Quantifier.* The infrared coefficients are ASSUMED as continuum transforms, as the attempt says.

## Verdict

**First failing step: 5.** The two-pin quantity is the equal-time marginal of the unpinned stationary law, and the pinned
process has the `χ` profile, so neither the one-pin profile in (b) nor the two-pin interaction in (c) is derived for the
task's persistent sources.

What holds, re-verified exactly:
- `χ = 7/E`, `C = 7σ²/(2E(1 − E/14))` and `χ = C(1 + φ)/σ²`;
- the `L = 4` values;
- reversibility of the linear and nonlinear kernels;
- the Gaussian two-site algebra.

`check.py` prints `SUMMARY: fails at step 5 - ...` and no `HIT: confirmed` line.
