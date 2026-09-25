# Two vacancies in the quadratic model — run 1

Worker `w-jonathonsmac4f50-j80ce`, model `claude-opus-5-5`. Blocks 39–41 were written by the same model family (Claude). The log is `logs/probes/C:source-two-inclusions-exact:a1/w-jonathonsmac4f50-j80ce__4e000910__20260925T033254Z.*`.

## As landed on main

Block 41 (#8547) is used only for the setting. The quadratic model and the interaction F defined below are the task's own.

## Definition and treatment of the free modes

The model lives on the torus `(Z/L)³` with the lattice Laplacian `L`. A vacancy at x removes the six bonds at x, so they have stiffness 0. The vacated site then carries an exact zero mode `e_x` of its own.

**Convention.** `det'` drops **every** zero mode: the constant on the rest of the lattice, and each vacated site's own. This is the same as deleting the vacated sites from the graph: `det' L_S` = the product of the non-zero eigenvalues of the Laplacian of `G − S`, which is connected.

  `F(x,y) = ½(log det' L_{xy} − log det' L_x − log det' L_y + log det' L)`

`F` is the interaction free energy (`Z = det'^{−1/2}`), so `F < 0` means attraction.

## Exact reduction

Let `B` be the N×k matrix of removed bond vectors `b = e_u − e_v`, where k = 6 for one vacancy, 12 for two apart and 11 for two neighbours. Let `L⁺` be the torus Green function without its zero mode, computed by FFT. Then:

  `det' L_{G−S} / det' L = det_r(I − BᵀL⁺B) · (N − |S|)/(N τ_S)`

- `det_r` is the product of the non-zero eigenvalues of the k×k matrix `A = I − BᵀL⁺B`. Its null space has dimension |S|, and on it `BᵀL⁺B = 1`.
- `τ_S` is the weighted spanning-tree sum of the quotient graph (vacated sites plus the rest of the lattice), with edge weights equal to the numbers of removed bonds. It is 6 for one vacancy, 36 for two apart, and 35 for neighbours.
- `N τ_S/(N − |S|)` is the product of the |S| small eigenvalues per unit weight as the removed bonds' weight goes to 0 (vertex masses 1, …, N − |S|).

**Check.** Dense determinants on the 4³ and 6³ tori agree to 5e−14 and 8e−14, for one vacancy, neighbours, (2,1,0) and antipodal pairs.

## Tori L = 8, 12, 16, 24 (as asked)

F(r) along an axis, on L = 24:

| r | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| F | **+1.977e−1** | −1.792e−2 | −9.443e−4 | −8.985e−5 | −1.537e−5 | −4.116e−6 | −1.491e−6 | −6.717e−7 |
| L16 ÷ L24 | 1.000 | 1.001 | 1.004 | 1.019 | 1.077 | 1.249 | 1.715 | 3.010 |

Along the body diagonal on L = 24, for r = 1 … 6: −3.778e−3, −6.041e−5, −5.592e−6, −1.001e−6, −2.521e−7, −7.804e−8. It then levels off at about −8.0e−9, a torus plateau that scales like L⁻⁶.

All tables for L = 8, 12, 16, 24, including the held-tilt column, are in the log.

**Sign.**
- Nearest neighbours **repel**: F(1) = +0.198, the same on every torus. The two vacancies share a bond, so the pair removes 11 bonds, not 12.
- Every other separation computed **attracts** (56 of 60).

**Finite size.** On these tori, images dominate beyond r ≈ L/4. The decay is therefore measured on larger tori, whose FFT Green function is cheap.

## Decay (tori 64, 96, 128)

The table gives F·d⁶ on L = 128, with d = r|v|.

| direction | r = 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 |
|---|---|---|---|---|---|---|---|---|
| axis | −1.146 | −0.366 | −0.186 | −0.150 | −0.138 | −0.133 | −0.130 | −0.128 |
| face diagonal | −0.182 | −0.130 | −0.124 | −0.123 | −0.1222 | −0.1220 | −0.1219 | −0.1217 |
| body diagonal | −0.105 | −0.115 | −0.119 | −0.120 | −0.1204 | −0.1206 | −0.1204 | −0.1200 |

- **Coefficient.** Fits of `F d⁶ = C + a/d² + b/d⁴`, over d where L = 96 and 128 agree to 0.1%, give **C = −0.1216** on the face diagonal (residuals ≤ 1e−4) and **C = −0.1216** on the body diagonal (residuals ≤ 6e−6).
- **Axis.** The axis converges slowly towards the same value: F·d⁶ is −0.128 at d = 16 and still falling. Its three-term fit is poor (−0.112, with 1e−2 residuals).
- **Local exponents on L = 128.**
  - Face diagonal: → 6.01.
  - Body diagonal: 5.85 → 6.03.
  - Axis: 7.26, 8.19, 7.95 at d = 2–5, falling to 6.10 at d = 16.
- **Free power fits** (d ≥ 6): n = 6.03 (face), 5.94 (body), 6.47 (axis, not yet asymptotic).

**Reading.** The decay is `d⁻⁶`, with a direction-independent coefficient C ≈ −0.1216. The lattice corrections are anisotropic: largest along the axes and of the opposite sign along the body diagonal.

## Comparison with two held tilts

The held-tilt interaction, `−ab G(r)/(G(0)² − G(r)²)` at a = b = 1, is −1.44, −0.58, −0.31, −0.19 at r = 1–4 on L = 24. It falls like `G(r) ~ 1/(4πr)`, and it changes sign near r ≈ L/2 because of the zero mode.

The vacancy interaction is a fluctuation-induced `r⁻⁶` force, weaker by 3 × 10⁻² at r = 2 and 5 × 10⁻⁵ at r = 6. Unlike a held value, a vacancy carries no monopole or dipole source; its leading effect is the square of the induced dipole field.

## Verdict

There is no HIT. The decay exponent is 6, as expected, with C = −0.1216.

The sign:
- nearest neighbours repel (+0.198);
- every larger separation attracts.
