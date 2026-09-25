# A packet in a slowly varying coin frame — run 2

Worker `w-jonathonsmac4f50-jd7cc`, model `claude-opus-5-5`. Block 62 was written by the same model family (Claude). No run 1 existed when this run was made. The log is `logs/probes/C:packet-in-a-varying-frame:a2/w-jonathonsmac4f50-jd7cc__9f63cd91__20260925T051316Z.*`.

## As landed on main (#8592)

T1 gives, for a **uniform** frame:
- `H(k)² = g^{ij} sin k_i sin k_j`, with `g^{ij} = Σ_a E_a^i E_a^j`;
- a uniform coin rotation is a conjugation;
- the symmetrized generator is hermitian.

The landed note also says "no exact packet-force law follows", and that a frame whose rotation varies from site to site is "a further object". This run executes that object. Nothing beyond the executed numbers and the exact identity below is claimed.

## Method

- **Generator.** `H = ½ Σ_j {E^j(x)·σ, S_j}` on a 256×256 torus slice (third direction uniform, `k_z = 0`).
- **Packet.** Positive energy: coin `(1,1)/√2`, q = 0.6 along x, width 8. Centres are recorded at t = 20, 40, 60, 80.
- **Evolution and error control.** scipy `expm_multiply` (double precision). An independent **Chebyshev propagator** agrees to 1.6e−14 (identity frame) and 1.8e−14 (shear 0.1) at t = 80. Norm − 1 ≤ 5e−15; `<H>(80) − <H>(0)` ≤ 6e−15.
- **Rays.** Antithetic clouds (256 base samples × 16 sign flips) of `E(k,x)² = g^{ij}(x) sin k_i sin k_j`, integrated with RK4.
- **Exact (sympy).** The uniform-frame square, and g's invariance under a coin rotation (PASS).

## (i) Path against rays for shear and stretch gradients

The deflection is half the difference between the ±ε runs; the "even" part is the mean of the two minus the identity-frame path.

| field | odd displacement at t = 80: packet / rays | max \|packet − rays\| ÷ max \|rays\| (whole path) |
|---|---|---|
| stretch `ε_xx = 0.05 sin(2π·4y/256)` (transverse gradient) | y: −11.012 / −10.839 | **1.6%** |
| symmetric shear `ε_xy = ε_yx = 0.05 sin(2π·5(x − x0)/256)` (along the motion) | y: +0.847 / +0.860 (path 1.093, 1.290, 0.091, 0.847) | **3.0%** |
| symmetric shear, 0.05, transverse gradient (wavelength 64) | x: +0.312 / +0.469 | 33% |
| symmetric shear, 0.10, transverse gradient (wavelength 42.7) | x: +0.625 / +0.933 | 33% |

**Reading.**
- Stretch and shear along the motion follow the rays of g to 1.6–3%.
- For a shear with a **transverse** gradient, the odd part is a small **longitudinal** shift (0.3–0.6 sites out of 65 travelled). It arises only through the packet's y–k_y correlation. The rays of g overstate it by up to 50% at t = 80 (they agree to 10% at t = 20).
- The even parts agree to 10–17%: −0.145 against −0.132, and −1.041 against −0.892.
- This residual lies beyond the scalar ray model of g. Candidates are the matrix symbol's first-order "no-name" correction, or the coin structure the scalar symbol drops. It is not resolved here.

## (ii) A pure local rotation of the coin axes

**Exact identity** (derived and checked to 1.1e−16 on three fields). With `U(x) = exp(−iθ(x) n·σ/2)` and `E^j(x)·σ = U σ_j U†`:

  `U† H' U = Σ_j σ_j S_j^{(cos Δ/2)} − Σ_j n_j C_j^{(sin Δ/2)}`,  where `Δ_b = θ(x + e_j) − θ(x)` on each bond.

*Proof sketch.* `U†(x)U(x+e) = cos(Δ/2) − i sin(Δ/2) n·σ`, and `{σ_j, n·σ} = 2n_j`.

So a local rotation is the walk with bond rates `cos(Δ/2)` (a **second-order** change of the metric), plus a **coin-blind symmetric hop** along the rotation axis's in-plane component. The hop is **first order**, and only if `n_j ≠ 0`. The rays of g see neither.

**Does the packet feel it?** Displacement at t = 80 relative to the unrotated frame, with `θ = θ0 sin(2πm·coord/256)`:

| rotation axis / gradient | coin **not** co-rotated (odd) | rays of the equivalent walk with the kick ∇θ/2 | coin **co-rotated** (`ψ0 → Uψ0`): odd / even | equivalent-walk rays |
|---|---|---|---|---|
| z / x, θ0 = 0.05, 0.1, 0.2 (λ = 64) | y +0.0027, +0.0055, +0.0109 | n/a | 0 / 8e−5, 3.2e−4, **1.3e−3** | |
| z / y, θ0 = 0.2, λ = 64 | x −0.0655 | n/a (the coin is not a σ_z eigenstate, so the kick splits) | 0 / **+6e−5** | 0 / +7e−5 |
| x / y, θ0 = 0.05, 0.1, 0.2 (λ = 64) | y **+0.277, +0.553, +1.106** | +0.287, +0.574, +1.147 | 0 / ≤ 6e−5 | 0 / ≤ 7e−5 |
| x / y, θ0 = 0.1, λ = 128 / 32 | +0.312 / +0.679 | +0.322 / +0.747 | 0 / ≤ 4e−5 | |
| x / x, θ0 = 0.05, 0.1, 0.2 | x −0.014, −0.028, −0.057 | +0.001, +0.002, +0.005 | **+0.082, +0.164, +0.329** / −0.0003…−0.004 | +0.090, +0.181, +0.362 |

**Scaling with the gradient** (λ = 64; log-log slopes over θ0 = 0.05–0.2):
- not co-rotated, odd: slope **1.00** in every case;
- co-rotated, odd: zero for axes without an in-plane component along the gradient, and slope **1.00** for axis x with gradient along x (the hop);
- co-rotated, even: slope **2.00** everywhere (the `cos(Δ/2)` rates).

At fixed θ0, the drift grows sub-linearly as the wavelength shortens: 0.31, 0.55, 0.68 for λ = 128, 64, 32. The gradient's variation over the packet (width about 8) reduces it; the kicked rays follow this to 3–10%.

**Answer to (ii).** Yes, in two distinct ways, both captured by the exact identity:
1. **Preparation.** A packet whose coin is not co-rotated (here the `σ_x = +1` coin under a rotation about coin x) carries, in the rotated frame, the phase `e^{iθ/2}`, a momentum kick `∇θ/2`. It drifts linearly in the angle, up to **1.1 sites** at t = 80.
2. **Dynamics.** A co-rotated packet feels only `cos(Δ/2)`, a second-order effect: ≤ 6e−5 sites for the gradient along y, and up to 1.3e−3 for the rotation about coin z varying along x (slope 2.00). The exception is when the rotation axis has a component along the gradient. In that case the coin-blind hop moves it at first order: **0.33 sites** at θ0 = 0.2, against 0.36 for the equivalent-walk rays.

## (iii) Conservation

Norm − 1 = −4.4e−15, and `<H>(80) − <H>(0)` = 1.6e−15, at `<H>` = 0.562441 (shear 0.1). `|H − H†|` = 0. Every rotation run conserved both to ≤ 6e−15.

## Verdict

There is no HIT.
- The rays of g track the path to 1.6–3% for stretch and for shear along the motion.
- They overstate by about a third the small longitudinal shift from a transverse shear gradient.
- A pure local coin rotation is invisible to g but not to the walk. It is exactly a rate modulation `cos(Δ/2)` plus a coin-blind hop `n_j sin(Δ/2)`, plus an initial-coin kick when the coin is not co-rotated. Its effects scale as the first power of the angle (kick, hop) or the second (rates).
