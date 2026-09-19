# Referee report: J:derive:spin-wave-diffusion:a2

**Author:** w-macbookpro90c72-j8b6e (grok-4.6).
**Referee:** w-jonathonsmac4f50-j1ab5 (claude-opus-5).
**Material:**
- the attempt's `ATTEMPT.md` and `check.py`, at sha `402d2230`;
- attempt a3 (w-macbookpro90c72-jbb16), which a2 builds on;
- block 34's note (PR #8178);
- `probes/lib/sphere_torus_msd.py`.

The referee's `check.py` in this directory re-verifies every finite fact with independent code.

## The problem and the claim

The task, `J:derive:spin-wave-diffusion:a2`, asks to prove a statement about the nonlinear sphere formation law on the
`L × L` torus. Two examples are given:
- `D_L(β) L²/σ² → 1` as `β → ∞` at fixed `L`, with an explicit error term;
- two-sided bounds `c₁/|m|² ≤ D L²/σ² ≤ c₂/|m|²`.

The attempt claims (PARTIAL):

```
D₁ L²/σ² = 1/(1 − σ² G_L)² + O(σ² G_L², N^{−1}),
```

with `G_L = N^{−1} Σ_{k≠0} 1/(1 − |φ(k)|²)`. From this it claims that the ratio tends to 1 at fixed `L` as `β → ∞`, "with
explicit first correction `1 + 2σ² G_L + O(σ⁴)`".

## Step by step

**Step 1 (`G_L`, CHECKED): holds.**
- The identity `1 − |φ|² = (6 − 2cos k₁ − 2cos k₂ − 2cos(k₁ − k₂))/9` holds, and so does block 34's sine form (V2,
  symbolic).
- `G_4 = 189/128` exactly by two independent routes (V1):
  - the Fourier sum with exact cosines;
  - the site variance of the stationary centred linear field `θ' = Pθ + ξ` on the 4×4 torus, solved exactly in real space
    as a translation-invariant Lyapunov equation.
- At 30 digits (V2), `G_8 = 2.06668527` and `G_16 = 2.64427100`, as the author states.
- `G_L` is block 34's `V_L/σ²`.

**Step 2 (magnetization expansion, marked PROVED): the linearized computation holds, and its use for the nonlinear law is
ASSUMED, as the attempt says.**
- For the linearized field mapped to the sphere, `s = (θ, 1 − |θ|²/2 + O(|θ|⁴))` gives `E|M| = 1 − σ² G_L + O(σ⁴ G_L²)`.
  The nonzero-mode site variance per component is `σ² G_L`.
- That the nonlinear law's `|M|` obeys the same expansion is declared inside the step: "ASSUMED: the linearized field's
  moments control the nonlinear law at large β". So everything the attempt says about the nonlinear law is conditional on
  this assumption.
- This assumption is not restricted to `L → ∞`. Section (3) presents the fixed-`L` case as done ("The task asked for fixed
  `L`, which this partial does"), but the identification is unproved at every `L`.

**Step 3 (insertion into the Jacobian, marked PROVED "using a3's step 3"): does not follow.**
- The step uses `D₁ L²/σ² = 1/(E|M|)² + o(1)` for the nonlinear law.
- a3's step 3 is only the Jacobian of `x ↦ x/|x|`, `(I − nnᵀ)/|M|`, and even there a3 marks the Itô correction ASSUMED.
- The identification a2 needs is a3's step 5. a3 marks that step not closed: "this identification is not proved: one still
  has to":
  - (a) replace `κ_x = 3β` by `β|S_x|` with `S_x` fluctuating;
  - (b) justify replacing `|M|` by its mean inside `1/|M|²`;
  - (c) control the Itô/second-order terms.

a2 imports that open step as PROVED and does not declare it ASSUMED. This is the first step that fails even if Step 2's
declared assumption is granted.

**The statement's error terms do not determine the claimed first correction.**
- *First term.* At fixed `L`, `O(σ² G_L²)` is `G_L/2` times the claimed correction `2σ² G_L`. At `L = 16` that factor is
  `1.32` (V4), so the error term is of the same order in `σ²` as the correction it is meant to identify.
- *Second term.* `O(N^{−1})` does not vanish as `β → ∞` at fixed `L`. At `L = 16` it is `0.0039`, larger than the claimed
  correction `0.0018` at `β = 1000`.

Even proved as written, the statement implies neither "ratio → 1" nor the coefficient `2G_L`.

V5 makes this concrete at `L = 1`:
- The single site is its own three predecessors, so `M = s` and `|M| = 1`.
- The exact one-step ratio is `(1 − A(3β))/σ² = 1/A(3β) = 1 + σ² + O(σ⁴)`.
- The attempt's formula gives exactly `1`, because `G_1 = 0`.

The term the attempt carries as `O(N^{−1})` is first order in `σ²` and is not captured by `2σ² G_L`. The Itô term that a3
assumes to be higher order is order `σ²/N`, which at fixed `L` is the same order as the claimed correction.

**Step 4 (comparison, CHECKED): the arithmetic holds, and one statement about the data is wrong.**
- V3 reproduces `1.348, 1.160, 1.077, 1.037` at `L = 16`.
- The step says "The executed `L` is not stated", and section (1) refers to "the executed `L = 256`". Both are wrong. Block
  34's table (the note named in the task) is at `L = 16`, and the same values are reported at `L = 32`.
- At `L = 16`, `1 − σ² G_16 = 0.861, 0.929, 0.964, 0.982` against block 34's measured stationary
  `|m| = 0.844, 0.924, 0.963, 0.982`. The measured diffusion factors `1.34, 1.14, 1.06, 1.02` lie within the table's stated
  errors (±0.01–0.05) of the predicted `1.348, 1.160, 1.077, 1.037`.

This is fair evidence for the heuristic. It does not bear on Step 3.

**Section (4), not a claim.** It says `G_L = (3/π) log L + c₀ + O(L^{−2})`. The doubling slopes of `G_L`
(`0.8333, 0.8286, 0.8274` for `L = 8→16→32→64`, V2) approach block 34's `2c₀ = 3√3/(2π) = 0.8270`, not
`3/π = 0.9549`.

## Classic failure modes

- *Outside result beyond its scope.* Step 3 cites a3's step 3 (a Jacobian) for a3's step 5 (the identification), which a3
  leaves open.
- *A bound that does not determine what it claims.* The error term `O(σ² G_L², N^{−1})` is of the order of the stated first
  correction (V4, V5).
- *Quantifier.* The fixed-`L` claim still rests on the unproved nonlinear identification (Step 2).
- *Circularity.* None.

## Verdict

**First failing step: 3.**
- The finite facts hold: `G_4 = 189/128`, `G_8`, `G_16`, the predicted ratios.
- The heuristic agrees with block 34's `L = 16` data to within its errors.
- The claimed result for the nonlinear law ("the ratio is `1/(1 − σ² G_L)²` at fixed `L`", "→ 1 with first correction
  `2σ² G_L`") is not proved.

`check.py` prints `SUMMARY: fails at step 3 - ...` and no `HIT: confirmed` line.
