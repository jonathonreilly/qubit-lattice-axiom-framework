# The crowd's alternation coefficient in three dimensions — run 1

Worker `w-jonathonsmac4f50-ja6f8`, model `claude-opus-5-5`. Blocks 80, 85 and 89 were written by the same model family (Claude). The log is `logs/probes/C:the-crowds-alternation-coefficient-in-3d:a1/`.

## As landed on main

- **Block 80 (#8615):** the compressed generator (one record per site, any coins) is a supplied choice.
- **Block 85 (#8657):** only non-increase of the crowd's ground energy is proved; a cusp is allowed. The fitted 2D coefficients are **not** bounds.
- **Block 89 (#8678):**
  - `h² = sin²k + sinh²δ`;
  - `h = cosh δ · h_lin(tanh δ)`;
  - finite grids with zero modes have a cusp.

Nothing below builds on withdrawn wording.

## Model

**One body.** `H = Σ_j σ_j D_j`, with bond amplitude t on the bond (x, x+e_j).
- log alternation: `t = e^{δ(−1)^{x_j}}`
- linear alternation: `t = 1 + δ(−1)^{x_j}`

**Many body.** N records, one per site, coins free, in two compositions:
- antisymmetric: sign `(−1)^{records strictly between}`;
- symmetric.

**Response.** Ground energies come from exact diagonalization or Lanczos (floating point). The fit is `E_N(δ) − E_N(0) = a|δ| + bδ² + cδ³`, at δ = 0.01, 0.02, 0.04.

**Free sea (comparator).** No exclusion, every negative one-body level filled, on the same torus, in closed form:
- log: `E = −Σ_k √(Σ_j sin²k_j + Σ_alt sinh²δ)`;
- linear: `E = −Σ_k √(Σ_j sin²k_j + δ² Σ_alt cos²k_j)`.

**Checks.**
- The one-particle spectrum matches the closed form.
- Block 85's four-ring values reproduce exactly: `E_2(0) = −√2` and `E_2(0.3) = −√218/10`.

## Exact statements

1. **A side of length 2 has no hop.** On a two-site ring `T = T†`, so `D = (i/2)(T − T†) = 0`. That axis is not alternated, as the task asks.
   - So the 2×2×L torus is **four independent L-rings**, and the 2×4×4 torus is **two independent 4×4 tori**.
   - Exclusion is per site, and with sites ordered ring by ring, a hop's exchange sign counts only records of its own ring. So `E_N = min over (N_1 + … = N) of Σ_r E_{N_r}(piece)`.
   - The task's tori are therefore one- and two-dimensional problems. The genuinely three-dimensional crowd is computed on **4×4×4**.
2. **The unit of rate.** When every hopping axis alternates, the compressed generator is linear in the bond amplitudes. Since `e^{±δ} = cosh δ (1 ± tanh δ)`, this gives `E_log(δ) = cosh δ · E_lin(tanh δ)`.
   - Checked on 4×4×4 at N = 2: −3.465660577782 on both sides.
   - Hence `b_log = b_lin + E_N(0)/2`. The fitted rows agree to 3e−4 (fit truncation).

## 4×4×4 (three-dimensional), low filling

| N (filling) | composition | E_N(0) | b_lin per site | b_log per site | b_log per record |
|---|---|---|---|---|---|
| 1 (1/64) | either | −√3 | 0.000000 | −0.013530 | −0.8659 |
| 2 (1/32) | either | −2√3 | 0.000000 | −0.027060 | −0.8659 |
| 3 (3/64) | antisymmetric | −3√3 | 0.000000 | −0.040590 | −0.8659 |
| 3 (3/64) | symmetric | −5.18109 | −0.000112 | −0.040584 | −0.8658 |

**Free sea on 4×4×4.**
- log: b = −1.0688 per site, i.e. per record with 64 records.
- linear: b = −0.5079.
- Both have a zero-mode **cusp** a = −0.2165 per site (8 of 64 momenta have sin k = 0).
- The sum over the other momenta of `1/|s|` per site is 0.71233.

**Reading.**
- At low filling the records sit at the band edge (`|sin k_j| = 1`, `cos k_j = 0`). There the linear alternation has **no** second-order effect, and the log alternation acts only through the overall rate factor cosh δ: `b_log = E_N(0)/2`, which is `−√3/2` per record.
- The crowd has **no** cusp (a = 0).

## The task's tori, every filling (per site; log | linear; both compositions give the same numbers)

**2×2×4 (four 4-rings), N = 1 … 16:**
- log: b = −0.0312·N for N ≤ 4; −0.1821, −0.2393, −0.2965, **−0.3536** at N = 5–8 (half filling); symmetric about half filling.
- linear: 0 for N ≤ 4; −0.0442·(N − 4) up to **−0.1768** at N = 8.
- Free sea: a = −0.5000 (cusp); b = −0.2500 (log) and 0.0000 (linear).

**2×2×6 (four 6-rings), N = 1 … 24:**
- log: −0.0241·N up to N = 8; −0.2590, −0.3255, −0.3920, **−0.4586** at N = 9–12; then falling to 0 at N = 24 (−0.1653 at N = 17 … −0.0209 at N = 23).
- linear: −0.0060·N up to N = 8; −0.1097, −0.1712, −0.2328, **−0.2944** at N = 9–12.
- Free sea: a = −0.3333; b = −0.3849 (log) and −0.0962 (linear).

**2×4×4 (two 4×4 tori), N = 1 … 4:**
- log: b = −0.0221·N.
- linear: b = 0.
- Free sea: a = −0.3536; b = −0.6769 (log) and −0.2501 (linear).

The crowd's `a` is zero at every filling of every piece. The free sea's cusp comes from its zero modes; the crowd, with its exclusion, never shows it.

## Verdict

There is no HIT.
- The side-2 tori are not three-dimensional (exact factorisation).
- On 4×4×4 at low filling, the crowd's alternation coefficient is **zero** in linear rates and **exactly the rate unit** in log rates (`b_log = E_N(0)/2`, −0.866 per record), against the free sea's −1.069 per record with a cusp.
- On rings at half filling, the crowd's quadratic coefficient exceeds the free sea's quadratic one (4-ring log −0.354 vs −0.250, 6-ring −0.459 vs −0.385). The crowd lacks the sea's |δ| term.

**Open.** Higher fillings on 4×4×4 (N ≥ 4, about 10⁷ states) were not run.
