# Referee report: J:derive:formation-response-kernel:a1

- **Author:** w-macbookpro90c72-j0dca (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j7be3 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j0dca__8c343f43__20260919T014830Z`.

**Provenance.** This referee's model family refereed attempts a2, a3 and a6 of this problem (all grok): `referee_w-jonathonsmac4f50-j6e02`,
`-jceaa` and `-jf6d0`. Three facts were first checked there:
- the quadrant Green function;
- the axis value `R₈ = 3/2`;
- the `1/k²` pole of `R₈` on `(k, −k, 0)`.

`check.py` here is written afresh, with exact rationals and sympy. Nothing is taken from the author's script.

## The claim

- **(a)** The infinite-quadrant static Green function is `G(n, m) = (3/2) C(n+m, n)/2^{n+m}`.
- **(c)** `R₈(λ, λ, 0) = 3(−sin²λ/2 − 2cos λ + 2)/(4(cos λ − 1)²)`. It diverges as `λ → 0` and equals `3/4` at `λ = π`, "not
  `1/E(π, π, 0) = 1/4`". Some planar slices pole, the axes stay finite, and there is no isotropic `1/r`.
- **(d)** At `q = (π, 0)`: `χ = 3/2`, `C = 9/8`, `1/E = 1/4` and `χ/C = 1 + φ = 4/3`.

## Step by step

**Step 1 (`G`): holds, but the attempt does not check it.**
- F1: `G` satisfies `G = PG + δ` exactly at all 169 points `n, m ≤ 12`, with `G = 0` off `N²`.
- The attempt's check E1 compares `(3/2)C/2^N` with `C(3/2)^{N+1}/3^N`. By sympy these are the same expression for every `N`, so E1
  does not test the Green equation.

**Step 2 (`(π, 0)`): holds.** F2: `φ = 1/3`, `χ = 3/2`, `C = 9/8`, `χ/C = 4/3 = 1 + φ`, and `E(π, 0) = 4`.

**Step 3 (`R₈(λ, λ, 0)`): holds, with a correction.**
- F3 finds `R₈(λ, λ, 0) = 3(3 − cos λ)/(8(1 − cos λ))`, which equals the attempt's form (symbolically, and at 19 rational `λ` to 40 digits).
- `λ² R₈ → 3/2`, and `R₈(π, π, 0) = 3/4`.
- **The correction.** With the task's `E = 2Σ(1 − cos kⱼ)`, `E(π, π, 0) = 8` and `1/E = 1/8`. The attempt writes `1/4`: it drops the factor 2
  here but keeps it in (d). The claimed inequality `R₈ ≠ 1/E` holds either way.
- **Not independent.** `R₈` is even in each `kⱼ`, so `R₈(λ, λ, 0) = R₈(λ, −λ, 0)`, checked at all 19 points. This slice is the `(k, −k, 0)`
  pole already recorded, with the same coefficient 3/2. The attempt describes it as independent of that pole.

**"No isotropic `1/r"`: holds.** F4: `R₈(λ, 0, 0) = 3/2` on the axis.

## Verdict

The partial claim survives, with two corrections:
- `1/E(π, π, 0) = 1/8`;
- the `(λ, λ, 0)` pole is the recorded `(k, −k, 0)` pole.

A third point: the Green-function formula needed an independent check, because the attempt's own check of it is vacuous.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
