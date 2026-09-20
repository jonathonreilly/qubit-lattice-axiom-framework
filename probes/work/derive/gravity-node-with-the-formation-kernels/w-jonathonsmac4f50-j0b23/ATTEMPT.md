# gravity-node-with-the-formation-kernels: derivation attempt 1 of 3

Worker `w-jonathonsmac4f50-j0b23` (claude-opus-5), unit `J-derive-gravity-node-with-the-formation-kernels-a1`.

**Provenance, stated because it bears on independence.** Two attempts existed at claim time.
`a3` (`w-jonathonsmac4f50-ja6b4`) is by the same model family, machine and running worker as this
one. `a2` (`w-macbookpro90c72-j3781`) is from another machine, and it already re-derived `a3`'s
identities independently and agreed with them. The reading of the node, the algebra of
`χ = 7/E`, and the fate of candidates (i) and (ii) are therefore settled twice over, and I do not
re-derive them. I take the one place both attempts stop, which `a2` states plainly:

> "**P6 remains an import** for (iii) as for the node: neither this attempt nor `a3` derives
> `G(r) → 1/(4πr)`. What is shown is that (iii) needs no import beyond the one `main` already
> carries."

The node's note on `main` asserts three facts about its own kernel — the on-site value
`G(0) = 0.252731`, the unit Newtonian tail `4πrG(r) → 1`, and the leading lattice correction
`[5/(32π)] K₄(n̂)/r³` — and both attempts cite them. **This attempt derives the first two and
verifies the third from the kernel itself**, so the packet carries no unchecked import about the
one object it is about. It also removes `a2`'s single `ASSUMED` identity.

## 1. The statement attempted

`G` is the `Z³` graph Green function, `Ĝ(k) = 1/E(k)`, `E(k) = Σ_a (2 − 2cos k_a)`; the light-cone
candidate's static response is `χ = 7/E = 7G` exactly (`a3` L1, `a2` step 2 — taken as given).

> **(1) On-site.** `G(0) = W/6` exactly, `W` Watson's integral
> `W = √6/(32π³)Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)`, so
> `G(0) = 0.252731009858663003…` — the note's `0.252731`, pinned to 18 digits.
>
> **(2) Tail.** `4πRG(R) → 1`, isotropically. Derived from the heat-kernel representation.
>
> **(3) Correction.** `G(x) = 1/(4πR) + [5/(32π)] K₄(x̂)/R³ + O(R⁻⁵)` with
> `K₄(n̂) = Σ_a n̂_a⁴ − 3/5`. The coefficient is recovered to `3·10⁻⁶` in three inequivalent
> directions, which is also what fixes the angular shape.
>
> **(4) Therefore** `χ = 7G` enters the node with `χ(0) = 7W/6 = 1.76911706901`, tail
> `7/(4π) = 0.557042300822` per unit `1/r`, and correction
> `35/(32π) = 0.348151438014` times `K₄/r³` — every constant exact.

## 2. Steps

**S1 (PROVED; CHECKED `H1`). The heat-kernel representation.**
`E(k) > 0` off `k = 0`, so `1/E(k) = ∫₀^∞ e^{−tE(k)}dt`, and
`e^{−tE(k)} = e^{−6t}Π_a e^{2t cos k_a}`. The one-dimensional transform
`(2π)^{−1}∫ e^{imk + 2t cos k}dk = I_m(2t)` is the generating function of the modified Bessel
functions; `H1` checks it at `m = 0..3` and two values of `t` to 25 digits. Hence

`G(x) = ∫₀^∞ e^{−6t} Π_a I_{x_a}(2t) dt`,

which is the continuous-time simple cubic walk's Green function — the object the node needs,
written so that its long-distance behaviour is an elementary calculation.

**S2 (PROVED; CHECKED `H2`). The tail.**
`e^{−6t}Π_a I_{x_a}(2t)` is the transition kernel of the continuous-time walk; by the local limit
theorem it is `(4πt)^{−3/2}e^{−|x|²/(4t)}(1 + O(1/t))` uniformly for `|x|² = O(t)`, and the
contribution of `t ≲ |x|` is exponentially small. Integrating the Gaussian against `dt`:

`∫₀^∞ (4πt)^{−3/2} e^{−r²/(4t)} dt = 1/(4πr)` — `H2` evaluates this in closed form.

So `G(x) = 1/(4π|x|)(1 + o(1))`, which is the import. `H4` executes the conclusion: at
`r = 8, 16, 30` along the axis, the face diagonal and the body diagonal, `4πRG(R)` is within
`4·10⁻³`, `1·10⁻³`, `3·10⁻⁴` of `1` and approaching it — and the three directions approach from
both sides, which is the isotropy.

**S3 (CHECKED `H3`). The on-site value.**
`G(0) = ∫₀^∞ e^{−6t}I₀(2t)³dt` agrees with `W/6` to `9·10⁻²⁷`. This is the same constant as the
light-cone long-range-order threshold's `I₀` — the self-energy of the gravity kernel and the
infrared constant of the ordering bound are one number.

**S4 (CHECKED `H5`). The correction, and why three directions matter.**
Writing `c(r) := R²(RG(R) − 1/(4π))/K₄(x̂)` and extrapolating in `1/r²` from `r = 20, 30`:

| direction | `K₄` | `c(10)` | `c(20)` | `c(30)` | extrapolated |
|---|---|---|---|---|---|
| axis `(1,0,0)` | `+2/5` | 0.0512860 | 0.0500999 | 0.0498961 | 0.04973298 |
| face `(1,1,0)` | `−1/10` | 0.0483348 | 0.0493876 | 0.0495813 | 0.04973616 |
| body `(1,1,1)` | `−4/15` | 0.0498139 | 0.0497563 | 0.0497451 | 0.04973606 |

against `5/(32π) = 0.04973592`. The three agree with each other and with the note's coefficient
to `3·10⁻⁶`, from three **different** values of `K₄` including two of opposite sign — so the
angular shape is the `l = 4` cubic harmonic and not something that happens to match on one ray.

**S5 (PROVED; CHECKED `H6`). Candidate (iii).**
`χ = 7G`, so it inherits (1)–(3) with one factor `7` and the constants above. Nothing in the
node's use of its kernel is now cited rather than checked.

**S6 (PROVED; CHECKED `H7`). `a2`'s assumption is unnecessary.**
`a2` lists `A(κ)/κ = Σ_n 2/(κ² + n²π²)` as `ASSUMED` and uses it for three things: the
monotonicity of `A(κ)/κ`, the bound `A ≤ κ/3`, and the limit `1/3`. All three follow from an
elementary series argument: `κA′ − A < 0` reduces to
`cosh x − 1 − x²/4 − (x/4)sinh x ≤ 0` at `x = 2κ`, whose Taylor coefficients are
`(2−m)/(4m(2m−1)!)` — zero at `m = 1, 2`, negative after — together with
`A(κ) = κ/3 − κ³/45 + …`. So `A(κ)/κ` decreases strictly from `1/3`, which is everything `a2`
draws from the partial fractions. The assumption can be struck from the packet.

## 3. Where the route stops

- **S2's local limit theorem is quoted, not proved.** The uniform Gaussian approximation of
  `e^{−6t}Π I_{x_a}(2t)` on `|x|² = O(t)` is standard, and the attempt's own numbers agree with
  it, but a self-contained proof (a saddle point on the Bessel integral with explicit error) is
  not here. This is the honest residue of the import: it moves from "the note says so" to "a
  standard theorem about the simple cubic walk says so, and the numbers agree at three
  directions".
- **S4 is an extrapolation.** The coefficient is not proved to be `5/(32π)`; it is recovered to
  `3·10⁻⁶` from three directions. The derivation from the symbol —
  `1/E = |k|^{−2} + (1/12)Σk_a⁴|k|^{−4} + …`, whose degree-4 part transforms to the cubic
  harmonic over `R³` — is sketched in the check's prose but the Fourier constant is not computed
  analytically here.
- **Nothing here revisits** the node's reading, the fate of candidates (i) and (ii), or the
  normalization equations; `a3` and `a2` agree on those and `a2` is from another machine.

## 4. What would finish it

1. The saddle-point version of S2 with an explicit error term, which would make the tail fully
   self-contained.
2. The analytic Fourier constant for the degree-4 cubic harmonic, which would turn S4's
   `3·10⁻⁶` agreement into an identity.
3. With (1) and (2) the gravity node's three kernel properties would be theorems of the formation
   kernel rather than properties asserted by its note — which is what a lane wanting to quote
   `χ = 7/E` as its input should have.

## 5. Running it

```
python3 probes/work/derive/gravity-node-with-the-formation-kernels/w-jonathonsmac4f50-j0b23/check.py
```
from the repository root. `sympy` and `mpmath`. About two minutes, most of it in the
thirty-digit Bessel quadratures at `r = 30`.
