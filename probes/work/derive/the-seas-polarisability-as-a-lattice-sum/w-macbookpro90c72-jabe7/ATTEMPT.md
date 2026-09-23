# J:derive:the-seas-polarisability-as-a-lattice-sum:a1: kappa = I/12 = 0.0994834268 exactly and positive; no q² log q in the rates' response or in any reach-three strain mode

**Provenance.**
- Worker `w-macbookpro90c72-jabe7`, model `claude-opus-5-5`, one session. Unit a1 (attempt 1 of 2); no prior attempts on the branch.
- **Overlap, disclosed.** Earlier in this same session the same model did `J:derive:the-held-sea-against-the-free-sea:a1` (#8716). That unit found:
  - the interband kernel `ΔΠ(q) = −(1/8)∫(a−b)²/(a+b)(1 − n·n')/2`, with two-sided bounds of order `q⁴ log(1/q)`;
  - `κ_free = κ_held = I/12 ≈ 0.0995`;
  - that block 76's `0.095` is a torus value carried by the zero modes.

  Parts (a)–(c) below are therefore **not** independent of #8716. They are re-derived by the task's own route (second-order perturbation theory of the two-band spectrum) and add three things:
  - `I` as a one-dimensional Bessel integral, giving `κ` to 20 digits;
  - an exact sympy check of the held part;
  - dense-diagonalisation validation on an antiperiodic torus.

  Part (d), the reach-three strain modes, is new.
- **Setting.** Block 76 (PR #8611), read on its branch together with its control script, defines the objects exactly: `E_sea`, `Π(q) = c₀/4 + (κ/4)|q|²_lat + …`, and the reach-three strain coupling (bond value = mean of the ends, `P_j = (T_j² − T_j⁻²)/4i`). Blocks 54 and 55 supply the walk and the clocked walk.
- Nothing is adopted, the parked decisions are untouched, and no gravitational claim is made.

## 1. The statement attempted

**Notation.** `s(k) = (sin k₁, sin k₂, sin k₃)`, `b = |s(k)|`, `a = |s(k + q)|`, `n = ŝ(k)`, `n' = ŝ(k + q)`. The eight zeros of `s` are `{0, π}³`. The sea's energy is `E_sea = Σ_{E<0} E(φHφ)` with `φ = e^{u/2}`, and the mode is `u = ε cos(q·x)`.

**(a) (PROVED; CHECKED A1, B1).** Per site and per `ε²`,

`Π(q) = −I/4 + (I/48)|q|²_lat + ΔΠ(q)`,

where:
- `I = ∫ |s(k)| d³k/(2π)³`, the magnitude of the sea's energy per site;
- the first two terms are the **held** part, the second order of `φ_xφ_y` evaluated in the unperturbed sea;
- `ΔΠ(q) = −(1/8) ∫ (a − b)²/(a + b) · (1 − n·n')/2 d³k/(2π)³` is the **interband** part: occupied states at `k` go to empty states at `k ± q`, with matrix element `(ε/4)(a − b)⟨+(k+q)|−(k)⟩` and denominator `−(a + b)`.

Checked against dense diagonalisation on the antiperiodic `6³` torus (no zero modes): `−0.274729178` both ways.

**(b) (PROVED; CHECKED C1, D2).** The `q²` coefficient is the held part's alone:

`κ = I/12`, with `I = (1/(2√π)) ∫₀^∞ t^{−3/2}[1 − (e^{−t/2}I₀(t/2))³] dt = 1.19380112142979520212`.

So `κ = 0.0994834268 > 0`. The sign holds because `I > 0`, and `c₀ = −I = −1.1938011`. Block 76's `κ = 0.0952 ± 0.0016` and `c₀ = −1.193` are torus values (tori `L ≤ 12`, with zero modes; see E1 and #8716).

**(c) (PROVED; CHECKED D1, D2).**
- **Finite.** Every integrand is bounded, since `(a − b)²/(a + b) ≤ |a − b| ≤ |q|`, so `Π` is continuous and `Π(q) → −I/4`.
- **Non-analytic part.** It comes only from the eight zeros. There the interband integrand is homogeneous of degree `d = 1` in `(p, q)`, so `Π ∈ C³` at `q = 0` and the first non-analytic term is `q⁴ log q`. There is **no `q² log q`** in the rates' response.
- **Numbers.** The interband part's `q²` coefficient on the zone grid is `~10⁻⁸` at `L = 16…128` (`q = 0.002`).
- **Control.** The same diagnostic detects `q² log q` where it is present: a plain density coupling (`d = −1`) gives a coefficient that falls by `0.0119` per doubling of `L`, against `ln 2/(6π²) = 0.0117`.

**(d) (PROVED; CHECKED A2, B1, D3, E1).**
- **The vertex.** Under block 76's reach-three coupling, the strain mode `B_aj = e_aj ε cos(q·x)` has vertex

  `(ε/2) Σ_{a,j} e_aj σ_a cos(q_a/2) cos(k_a + q_a/2) · [p_j(k) + p_j(k+q)]/2`,  with `p_j = sin(2k_j)/2`.

  It is checked against dense diagonalisation to 10 digits on the antiperiodic `6³` torus for all three modes.
- **It vanishes at all eight zeros**, because `sin 2K_j = 0` there. Near a zero it is `Σ e_aj σ_a cos K_a (p_j + q_j/2)`, of degree 1. So the integrand `|⟨+|W|−⟩|²/(a + b)` has `d = 1`, and **no reach-three strain mode has a `q² log q` piece**, for any polarization or direction.
- **Zone-limit `q²` coefficients** (per `q²` along `x`, per site per `ε²`; floating point, extrapolated from `L = 64` and `128`; steps shrink about fourfold per doubling):

  | mode | `q²` coefficient | local part |
  |---|---|---|
  | TT cross (`yz`) | `0.00502` | `−0.01866` |
  | TT plus (`yy − zz`) | `0.00529` | `−0.02540` |
  | isotropic stretch | `0.00488` | `−0.01160` |

- **Block 76's W2 values are finite-torus values.** Dense diagonalisation on the periodic `8³` torus at `q = 2π/8` reproduces them exactly: `0.0035, 0.0021, 0.0004`, local `−0.0200, −0.0202, −0.0088`. The same torus with antiperiodic walls gives `0.0035, 0.0054, 0.0052`. The periodic torus's zero modes carry the difference, as #8716 found for the rates, whose W1 value `0.0221` is also reproduced here.

**The task's HIT condition is not met.** `κ` is positive in the exact limit, and there is no `q² log q` term in the rates' response.

## 2. Steps

**S1: the expansion (PROVED; CHECKED A1).**
- `(H_w)_{xy} = φ_xφ_y H_xy` and `φ_xφ_y = e^{(u_x + u_y)/2}`. So `V₁ = ((u_x + u_y)/2)H` and `V₂ = ((u_x + u_y)²/8)H` bond by bond.
- **The held part.** `Tr V₂P₋ = Σ_bonds ((u_x + u_y)²/8) t_a`, where `t_a` is the sea's energy on a bond along `a`: `e_s/3` by cubic symmetry, with `e_s = −I` per site.
- **The mode average.** For the mode, `⟨(u_x + u_{x+e_a})²⟩ = ε²(1 + cos q_a)`.
- **Result.** Per site, `(e_s/24)Σ_a(1 + cos q_a) = e_s/4 − (e_s/48)|q|²_lat`.

**S2: the interband part (PROVED at the scope of standard second-order perturbation theory for a filled band; CHECKED B1).**
- Intraband terms cancel in a filled band.
- The interband term is `−Σ|⟨+,k±q|V₁|−,k⟩|²/(a_± + b)`.
- The matrix element is `(ε/4)(E₊ + E₋)⟨+|−⟩ = (ε/4)(a − b)⟨+|−⟩`, with `|⟨+(k+q)|−(k)⟩|² = (1 − n·n')/2`.

**S3: `ΔΠ = O(q⁴ log(1/q))` (PROVED).**
1. **Two bounds.** Each component satisfies `|sin x − sin y| ≤ |x − y|`, so `|a − b| ≤ |s(k+q) − s(k)| ≤ |q|`. For unit vectors, `|n − n'| ≤ 2|s − s'|/max(a, b)`, so `(1 − n·n')/2 = |n − n'|²/4 ≤ |q|²/max(a, b)²`.
2. **The integrand** is therefore at most `|q|² min(1/(a + b), |q|²/(a + b)³)`.
3. **Near each zero** `|s| ≥ (2/π)|p|`. Integrating over `|p| < |q|` and `|q| < |p| < 1` gives `O(q⁴) + O(q⁴ log(1/q))`. Away from the zeros `|s|` is bounded below, which gives `O(q⁴)`.
4. So `ΔΠ/q² → 0` and `κ = I/12`. #8716 gives the matching lower bound, so `q⁴ log q` is actually present.

**S4: `I` as a one-dimensional integral (PROVED; CHECKED C1).**
- `√A = (1/(2√π)) ∫₀^∞ (1 − e^{−tA}) t^{−3/2} dt` for `A ≥ 0`.
- The zone average of `e^{−t Σ sin²k_a}` is `m(t)³`, with `m(t) = (1/2π)∫e^{−t sin²k}dk = e^{−t/2}I₀(t/2)`.
- Evaluated with mpmath at 30 digits. Grid sums converge to it: `1.1938011222` at `L = 256`.

**S5: degree counting (PROVED as the standard homogeneity argument; CHECKED D1–D3).**
- Near a zero, the integrand is homogeneous of degree `d` in `(p, q)` up to higher-degree corrections.
- The `n`-th `q`-derivative has degree `d − n` and is integrable in three dimensions iff `d − n > −3`. The singularities at `p = 0` and `p = −q` are both integrable, uniformly in small `q`.
- So `Π ∈ C^{d+2}` at `q = 0`, and the first non-analytic term is `q^{d+3} log q`.
- The degrees are: rates' interband part `d = 1`; reach-three strains `d = 1` (A2); density coupling `d = −1`.

**S6: the strain vertex (PROVED; CHECKED B1, A2).**
- `C_a[v]` hops along `a` with bond values `v_x = (B_x + B_{x+e_a})/2`. For `B = εe^{iq·x}/2` it maps `k → k + q` with amplitude `(ε/2)cos(q_a/2)cos(k_a + q_a/2)`.
- `P_j` is diagonal with symbol `p_j(k)`, so `½{C_a, P_j}` carries `[p_j(k) + p_j(k+q)]/2`.
- **Matrix elements.** For `A = w·σ`, `|⟨+(n')|A|−(n)⟩|² = ½|w|²(1 + n·n') − (w·n)(w·n')`.

**S7: the tori (CHECKED E1).** Dense diagonalisation at `L = 8`, with both periodic and antiperiodic walls, using block 76's own definitions.

## 3. The first failing step

- **The task's HIT route fails.** `κ` is positive, `I/12`. No `q² log q` appears in the rates' response or in any reach-three strain mode.
- **The first place a `q² log q` could enter is excluded.** It would need a vertex that does not vanish at the eight zeros. `φHφ` and the reach-three coupling both vanish there, to first order in `(p, q)`.
- **What is not proved.** The strain coefficients are floating-point zone sums: their absence of a log is proved, their values are not. Standard perturbation theory is used at its textbook scope (S2).

## 4. What would finish it

1. The strain modes' `q²` coefficients as closed zone integrals, analogous to `I/12`, if one exists. The local parts would follow from the same vertex at `q = 0`.
2. A coupling with a non-vanishing vertex at the zeros, such as a scalar density term or a reach-two coupling with a different completion. That is where a `q² log q` would appear, with the density's coefficient `1/(6π²)` as the benchmark.
3. A referee from another model family; #8716 is the same model.

## 5. Running it

```
python3 probes/work/derive/the-seas-polarisability-as-a-lattice-sum/w-macbookpro90c72-jabe7/check.py
```

The run takes about 16 s and peaks near 230 MB. It prints:
- exact sympy checks A1–A2 and the degree statement A3;
- floating-point checks B1, D1–D3 and E1, labelled;
- the 30-digit value of `I` in C1;
- then the SUMMARY and HIT lines.

Standard mathematics used, none as authority:
- Rayleigh–Schrödinger second-order perturbation theory for a filled band;
- the integral representation of `√A`;
- the modified Bessel function `I₀`;
- dense Hermitian diagonalisation.
