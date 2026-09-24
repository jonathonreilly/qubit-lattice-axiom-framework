# Referee: only the turn is massless, a2

Author `w-macbookpro9927a-j6622` (claude-opus-5-5). Referee `w-macbookpro90c72-j51e0` (grok-4.6).

## Steps

1. **Sectors.** The angular average of `e^{x cos ψ} cos(mψ)` matches `I_m(x)` through `x^12` for `m = 0..4`. Each azimuthal order has the positive kernel `e^{β t t'} I_m(β r r')`.

2. **Order one.** If the turn is the eigenvalue `1/6` with profile `√(1−t²)(log F)' > 0`, Jentzsch makes it the simple Perron root. A negative eigenvalue `−1/6` would force that profile to change sign. Every other order-one eigenvalue then has modulus below `1/6`. Jentzsch and the turn eigenvalue stay assumed.

3. **Higher orders.** `I_m < I_1` for `m ≥ 2` is Soni's inequality, assumed. The kernel comparison is strict on the open square, so an order-`|m| ≥ 2` eigenvalue has modulus below `1/6`.

4. **Monotonicity.** At polar angle `θ`, reflection through the plane normal to the meridian tangent fixes `s·b` and raises `b·n` by `2(e_θ·b) sin θ` on the half `e_θ·b > 0`. A non-decreasing non-constant sea is sent to a strictly increasing one.

5. **Large β.** A Gaussian sea of curvature `a` is sent to curvature `a β/(2a+β)`. The sixth power fixes `a = 5β/2`. The chain is `N(x/6, 1/(6β))`, with Mehler eigenvalues `6^{-n}`. The lean-size mode and `m = ±2` have `μ = 1/36` and `m² = 30`. The next `m = ±1` and `m = ±3` have `μ = 1/216` and `m² = 210`. This is the tangent approximation; the rate of convergence is not bounded. The 320-node table was not re-run.

6. **Order zero.** `I_0 > I_1`, so the same comparison does not push the size mode below `1/6`. That part stays executed only.

## Verdict

The exact `|m| ≥ 1` statement survives, with the three named inputs. The lean-size mass of the limiting chain is 30.

`HIT: confirmed`.
