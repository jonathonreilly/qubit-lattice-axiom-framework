# Closed lattice: uniform motion of the lengths; the simplest member's pair — run 2

Worker `w-jonathonsmac4f50-j44ae`, model `claude-opus-5-5`. Blocks 60, 62 and 75 were written by the same model family (Claude). The log is `logs/probes/C:closed-lattice-uniform-motion-of-the-lengths:a2/w-jonathonsmac4f50-j44ae__601ad55d__20260925T052316Z.*`.

## As landed on main

- **Block 60 T5(b) (#8590):** a uniform solution exists iff `c_k < 0`. In the label w = 1 it is `ℓ = (1 + t/t0)^{2/s}`, and the constraint is kept.
- **Block 75 T3(c) (#8608):** the tuned pair condition `1/|m_B| − 1/m_A = γ(G_0 − G_d)`. The landed note says: "Whether such a configuration is stable is not examined."

## Model

**Curvature member.**
- Field: `G_x = 8K χ_x (Δχ)_x`, with `χ = ℓ^{1/2}`.
- Kinetic term: `Σ_x c_k ℓ_x^s λ̇_x²/w_x`. Block 62's rotation-invariant family, evaluated on `h = 2λδ`, gives `c_k = 12α + 36β`. With β = −α and α = K/4 this is `c_k = −6K`, block 60's comparator (sympy). s = 3.
- Content: bodies at rest at every site, m = 1 (K = 1). The uniform massive-sea variant was not run.

**Hamiltonian form.** `H = Σ_x w_x C_x`, with `C_x = m + G_x + p_x²/(4c_k ℓ_x^s)`. The rates are multipliers, and `C_x = 0` are the constraints.

## (1) Uniform motion on the 6³ torus

**Exact (sympy).** In w = 1, `ℓ = (1 + (s/2)√(m/|c_k|) t)^{2/s}` solves the lengths' equation and the constraint with residual 0.

**Numerical (RK4, dt = t0/500).** Starting from uniform λ = 0 with p fixed by the constraint:

| t/t0 | 1 | 3 | 10 | 30 | 100 |
|---|---|---|---|---|---|
| ℓ(t) / exact | 1.00000000 | 1.00000000 | 1.00000000 | 1.00000000 | 1.00000000 |
| max \|C\| | 4.0e−13 | 5.1e−13 | 5.6e−13 | 4.1e−13 | 7.4e−13 |

- **Fitted exponent:** 0.66667, against `2/s` = 0.66667.
- **Clocks follow:** w = 1 keeps every constraint to 7e−13.

## (2) First failing step: non-uniform data

`{C_x, C_y} = 4K χ_x χ_y (v_y − v_x)` on bonds, with `v = p/(2c_k ℓ^s)`. It vanishes identically on uniform data (checked: 0).

A clock field w keeps every constraint iff `Σ_y {C_x, C_y} w_y = 0`. With site-random perturbations of λ, and p fixed by the constraints at t = 0:

| perturbation | norm of {C_x, C_y} | smallest singular value (relative) | max \|C\| in w = 1 at t/t0 = 1, 3, 10 | spread of λ (from) | mean ℓ ÷ uniform law at t/t0 = 1, 3, 10 |
|---|---|---|---|---|---|
| 1e−2 | 3.23 | 9.0e−3 (2.8e−3) | 3.6, 3.9, 3.1 | 2.3e−2, 1.3e−2, 6.0e−3 (9.8e−3) | 0.99649, 0.99647, 0.99741 |
| 1e−3 | 0.271 | 4.6e−4 (1.7e−3) | 0.26, 0.23, 0.22 | 2.0e−3, 1.0e−3, 4.8e−4 (9.1e−4) | 0.999975, 0.999975, 0.999982 |
| 1e−4 | 0.0265 | 2.6e−5 (1.0e−3) | 0.025, 0.026, 0.030 | 2.2e−4, 1.1e−4, 5.3e−5 (1.0e−4) | 1.000000 |

**Reading.**
- The bracket matrix is antisymmetric of even size (216), and it is non-singular. So **no clock field other than w = 0 keeps all the constraints** once the data are non-uniform.
- In the label w = 1, the constraints drift at first order in the perturbation, with a large coefficient: about 250× the amplitude.
- The perturbation of λ itself decays, and the mean length follows the uniform law.
- So the uniform motion is the only solution of the closed constrained system that these runs found. Non-uniform data break the constraint algebra on the lattice.

## (3) The simplest member on the 4³ torus (exact rationals), γ = 1

**Tuned pairs** (T3(c) reproduced exactly; the static-law residual is exactly zero):

| B (A at origin) | h = G0 − Gd | m_B (m_A = 1) | φ_A | φ_B |
|---|---|---|---|---|
| (1,0,0) | 21/128 | −128/149 | 256/277 | 298/277 |
| (2,1,0) | 131/640 | −640/771 | 1280/1411 | 1542/1411 |
| (2,2,2) | 13/60 | −60/73 | 120/133 | 146/133 |

**Perturbations of the pair A = (0,0,0), B = (1,0,0).** Each row gives the least eigenvalue of `(2/γ)(−Δ) + diag(m)`, which is zero iff a positive static φ exists (Perron–Frobenius):

| perturbation | least eigenvalue | rest |
|---|---|---|
| none | −1.8e−14 | yes |
| translate the pair by (1,2,3) | +1.1e−14 | persists |
| separation rotated to (0,1,0) (same h) | −2.7e−14 | persists |
| re-tuned pair, m_A = 2 | −1.1e−14 | persists |
| B one more step, to (2,0,0) | −3.96e−4 | lost |
| m_A × 1.01 | +1.33e−4 | lost |
| m_A × 0.99 | −1.34e−4 | lost |
| third body m = +0.01 at (2,2,2) | +1.56e−4 | lost |

**As a landscape for test bodies** (both signs fall towards slow clocks: block 71's twins):
- At A (the positive body), `Δφ = +0.4621`: the minimum of the clocks, so A is held.
- At B (the negative body), `Δφ = −0.4621`: the maximum, so B is pushed off by every displacement.
- `φ_A = 0.9242 < φ_B = 1.0758`.

## Verdict

There is no HIT.
- The lengths' exponent equals 2/s to five digits.
- The tuned pair keeps rest under 3 of the 7 perturbations tried: those along its tuning surface (translation, an equivalent separation, re-tuning).

**First failing step:** on the closed lattice the curvature member's constraints close only on uniform data. For any tested non-uniform perturbation, no clock field keeps them.

**Stability, first look.** Off the tuning surface the pair loses its static clock field at first order. As test bodies, the negative body sits on the clocks' maximum.
