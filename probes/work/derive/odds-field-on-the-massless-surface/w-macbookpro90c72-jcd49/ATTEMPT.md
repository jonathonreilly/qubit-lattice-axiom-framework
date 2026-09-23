# J:derive:odds-field-on-the-massless-surface:a1 — the cubic coefficient u = 90 l1²(1 − 36 l2)/(1 − 6 l2), exactly; the far field's log law; the torus control reproduced by the cubic map

**Provenance.**
- Worker `w-macbookpro90c72-jcd49`, model `claude-opus-5-5`, one session. The claim printed no prior attempts.
- Definitions are block 42's, from the note and control on PR #8548's branch (`docs/ADMISSIBILITY_RULE_INTERACTION_THROUGH_THE_ODDS_OF_UNFORMED_SITES_…_2026-09-20.md` and `specs/supervisor_control_block42_odds_field.py`), using the task's notation.
- The owner's reading (odds of unformed sites as conditions) is supplied and not adopted. Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Objects (block 42).**
- **The map.** Six contents `s = ±e₁, ±e₂, ±e₃`. The map is `π_x(s) ∝ Π_{y∼x} (Wπ_y)(s)`, where `W(s, b) = p, q, r` for `b = s`, `−s`, orthogonal.
- **The constants.** `T = p + q + 4r`, `l1 = (p − q)/T`, `l2 = (p + q − 2r)/T`.
- **The lean.** Block 42's `m_x = Σ_s π_x(s) s`. A record, a point mass, has lean 1.
- **A departure along the record's axis.** `π_y(s) = (1/6)(1 + 3v_y s₁ + D_y Q(s))` with `Q(s) = 3s₁² − 1`, so `v_y` is the lean along `e₁` and `D_y` the quadrupole along `e₁`.

**Claims.**
- **(a) Exact.**
  - **Third-order expansion.** At a site whose six neighbours carry `(v_y, D_y)`, with `v ~ t` and `D ~ t²`:
    - `v′ = l1 S₁ + 3 l1³(Σv³ − S₁Σv²) − 2 l1 l2(ΣvD − S₁ΣD) + O(t⁵)`;
    - `D′ = l2 ΣD + (3/2) l1²(S₁² − Σv²) + O(t⁴)`;
    - here `S₁ = Σ_y v_y`.
  - **The effective equation.** For slowly varying fields the quadrupole is slaved, `D = 45 l1² v²/(1 − 6 l2)`, with mass `(1 − 6 l2)/l2`. The lean then obeys

    `−Lap v + m² v + u v³ = source/l1`,  `m² = (1 − 6 l1)/l1`,  **`u = 90 l1²(1 − 36 l2)/(1 − 6 l2)`**.
  - **On the surface `5p = 7q + 4r`.** `l1 = 1/6`, `m² = 0`, and **`u = (5/2)(4r − 7q)/(r − q)`**.
    - `u > 0` iff `4r > 7q` (the quadrupole is massive iff `r > q`).
    - **At `(3,1,2)`: `l2 = 0` and `u = 5/2`.**
  - In the units `w = 3v` (the vector part of `6π − 1`) the same coefficient is `u/9 = 10 l1²(1 − 36 l2)/(1 − 6 l2)`, i.e. `5/18` at `(3,1,2)`.
- **(b) The far field.**
  - **Exact.** `v = A(r)/r` gives `Lap v = A″/r`. In `τ = log r` the radial equation `Lap v = u v³` is **`A_ττ − A_τ = u A³`**.
  - **Its decaying solutions.** They lie on the centre manifold `A_τ = −uA³ + 3u²A⁵ − 24u³A⁷ + …`. So `A⁻² = 2u log r − 3u log log r + C + o(1)`.
  - **The task's formula.** `A⁻² = A₀⁻² + 2u log(r/r₀)` is this law's leading term (the "leading log"). A weak source keeps a one-over-distance field out to `r ≈ r₀ exp(1/(2uA₀²))`.
- **(c) Executed.**
  - The third-order lattice map at `(3,1,2)` (`u = 5/2`), with only the record and its six neighbours held at the control's `r = 1` value, reproduces block 42's full-map control at `r = 2..7` on sides 15, 21 and 27 to `4·10⁻⁴`. For example, on side 27 it gives `0.2881, 0.2809, 0.2862, …` against `0.2883, 0.2812, 0.2864, …`.
  - Scaling `u` by `0.8` or `1.2` spoils the agreement (deviations `0.028`, `0.022`), so the control pins `u`.
  - The control's "`r v(r)` flat at 0.28–0.30" is not a far field. It is the balance on a torus between the log running of the source and the uniform background that the cubic term leaves: `r v` rises again beyond `r ≈ 3` (to `0.333` at `r = 7` on side 27, and more on smaller tori).

## 2. Steps

**S1 (PROVED; CHECKED A.expansion). The expansion.**
- **The channel structure.** `(Wπ_y)(s) = (T/6)(1 + 3 l1 v_y s₁ + l2 D_y Q(s))`:
  - the vector channel has eigenvalue `p − q`: for `s = e₁` it collects `p v₁ − q v₁`, and the orthogonal terms cancel;
  - the quadrupole channel has eigenvalue `p + q − 2r`, using `D₂ + D₃ = −D₁`.
- **Taking logs.** `log π_x(s) = a s₁ + c Q(s) + const`, with
  - `a = 3 l1 S₁ − 6 l1 l2 ΣvD + 9 l1³Σv³` (using `s₁³ = s₁`, `s₁Q = 2s₁`, `s₁² = (Q + 1)/3`);
  - `c = l2 ΣD − (3/2) l1²Σv²`.
- **Reading off the new components.** Normalising over the six contents, `v′ = (π′(e₁) − π′(−e₁)) = sinh a/(cosh a + 2e^{−3c})`. That expands as `a/3 + (2/3)ac + O(t⁵)`: the `a³` terms cancel. Likewise `D′ = 1 − 6π′(e₂) = c + a²/6 + O(t⁴)`. Collecting terms gives (a).
- **CHECKED.** The exact map is a rational function of `t`. It is expanded exactly with sympy at 8 random rational neighbourhoods and 4 weight triples (`(3,1,2), (5,2,4), (7,2,3), (4,1,1)`), and both expansions agree term by term.

**S2 (PROVED; CHECKED A.coupling). The effective equation.**
- **Slowly varying fields.** Take `Σ_y f_y = 6f + Lap f + …`. For the cubic terms keep the local values: `Σv³ = 6v³`, `S₁Σv² = 36v³`, `ΣvD = 6vD`, `S₁ΣD = 36vD`.
- **The quadrupole equation** becomes `(1 − 6 l2)D − l2 Lap D = 45 l1²v²`. At leading order in gradients `D = 45 l1² v²/(1 − 6 l2)`, with mass `(1 − 6 l2)/l2 > 0` iff `0 < l2 < 1/6`. (At `l2 = 0` it is exactly local.)
- **The vector equation** becomes `0 = (6 l1 − 1)v + l1 Lap v − 90 l1³v³ + 60 l1 l2 vD`. Substituting `D` gives the stated `m²` and `u`.
- **On the surface.** With `p = (7q + 4r)/5`: `l1 = 1/6`, `l2 = (2q − r)/(2(q + 2r))`, `1 − 6 l2 = 10(r − q)/(2q + 4r)`, `1 − 36 l2 = 10(4r − 7q)/(2q + 4r)`. Hence `u = (5/2)(4r − 7q)/(r − q)`.
- **At `(3,1,2)`.** `l2 = 0` and `u = 5/2`.
- All of this is CHECKED with sympy.

**S3 (PROVED; CHECKED A.farfield). The far field of the effective equation.**
- **The radial reduction.** For radial `v = A(r)/r` in three dimensions, `Lap v = v″ + (2/r)v′ = A″/r` (CHECKED). So away from the source `A″ = uA³/r²`. With `τ = log r` this is `A_ττ − A_τ = uA³` (CHECKED).
- **The decaying solutions.** Write the system as `A′ = B`, `B′ = B + uA³`. Its linearisation at the origin has eigenvalues 0 and 1. The solutions with `A → 0` as `τ → ∞` lie on the centre manifold `B = h(A)`. From `h′h = h + uA³`: `h = −uA³ + 3u²A⁵ − 24u³A⁷ + …` (CHECKED).
- **The log law.** Then `(A⁻²)_τ = −2A⁻³h = 2u − 6u²A² + …`, so `A⁻² = 2uτ − 3u log τ + C + o(1)`.
- **The task's formula.** It keeps `2uτ`. It follows from neglecting `A_ττ`, whose relative size is `3uA²`: the leading-log approximation.

**S4 (executed; notes). The control, predicted from the cubic map.**
- **The comparison.** Iterate the third-order lattice map at `(3,1,2)`, `v′ = S₁/6 + (Σv³ − S₁Σv²)/72` (with `l2 = 0` the quadrupole does not feed back), on tori of sides 15, 21 and 27, holding the record (`v = 1`) and its six neighbours at the control's `r = 1` value (`0.3064, 0.3016, 0.2992`).
  - Result: `r v(r)` at `r = 2..7` matches block 42's full-map control to `4·10⁻⁴` on every side.
  - Scaling `u` by `0.8` or `1.2` gives deviations `0.028` or `0.022` at side 21.
- **What the torus does.** On a torus the source has no sink. The cubic term alone fixes a uniform background lean, and `r v_bg` grows linearly in `r`. With the zero-mode-free Green function (whose `r G(r)` falls by a term `∝ r/L`) and the log running of the core, this gives the dip-then-rise that the control shows.
- **The infinite-volume law.** The shooting solution of S3 with `A(1) = 0.3` gives `A = 0.2249, 0.1856, 0.1668` at `r = 10, 100, 1000`. The leading log gives `0.2102, 0.1712, 0.1480`. It falls short by 7–11%, because at `A₀ = 0.3` `uA₀² = 0.225` is not small; the `−3u log log r` term accounts for most of the difference.

**ASSUMED.**
- The gradient expansion of S2, the local slaving of the quadrupole and the neglect of higher-order terms, as the description of the lattice far field. S4 supports this (`4·10⁻⁴` on the tori) but does not prove it.
- The centre-manifold theorem, used in S3 for the existence and smoothness of the decaying branch. The expansion coefficients themselves are checked exactly.

## 3. The first failing step

None for (a), which is the task's HIT condition: the expansion, and `u` as a function of `(p, q, r)` on the surface, are exact.

For (b), the task's formula is the leading term of an exact asymptotic law. Its neglected next term, `−3u log log r`, is quantified. What is not proved is that the lattice far field follows the continuum equation (assumed; supported by S4).

## 4. What would finish it

1. **A lattice far-field theorem.** Show that the fixed point of the full map on `Z³` with one record has `v(r) = A(r)/r` with `A⁻² = 2u log r + O(log log r)`. This could be done by a comparison principle for the cubic map (it is monotone in `v` for small `v`) with sub- and supersolutions built from S3's centre-manifold expansion.
2. **The core value.** `A(1)`, or the effective `A₀`, is set by the strongly nonlinear core (`v = 1` at the record). An exact or rigorous computation of the full map's fixed point on the first shells would turn S4's "held core" into a prediction from first principles.
3. **Off the surface.** Near the surface `m²` is small, and there is a crossover between the screened field (range `m⁻¹`) and the cubic log law, at `m ≈ (u/…) A²`-type scales. The same expansion gives it.

## 5. Running it

```
python3 probes/work/derive/odds-field-on-the-massless-surface/w-macbookpro90c72-jcd49/check.py
```

The run takes about 16 s. It makes three exact checks: sympy series of the exact rational map at rational points, the continuum reduction, and the radial and centre-manifold algebra. The `note` lines are floating point: the torus iterations, the sensitivity to `u`, and the shooting solution.
