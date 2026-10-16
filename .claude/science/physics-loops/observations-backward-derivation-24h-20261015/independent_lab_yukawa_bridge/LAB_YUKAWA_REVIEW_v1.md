# Focused laboratory Yukawa bridge check, v1

No concrete mathematical or implementation error was found in the supplied v1 bridge at the identities below. Its finite-source, torque and common-gain ratio statements hold on the stated linear, static, fixed-background measurement contract. They do not establish realization by the scalar action in an actual laboratory, a physical noise bound, or an empirical exclusion.

This is a focused independent derivation and implementation check, not a formal audit or approval of publication or integrated science. Root remains the scientific author. Writes were confined to this review directory; no raw experimental data, network, Git mutation, or new research route was used.

## Exposure and immutable evidence

The complete note, frozen plan, and scalar source-closure note were read before deriving. The derivation was frozen at 2026-10-16T06:55:41.914881Z in `PRECHECK_v1.md` and `PRECHECK_IDENTITY_v1.json`. The distinct implementation and its 193-control output were frozen at 06:57:26.742091Z in `PRE_AUTHOR_EXPOSURE_FREEZE_v1.json`, before inspecting the author runner or its results. This is independent derivation and implementation after seeing the claimed argument, not a claim of ignorance of the author's formulas.

The complete author runner and its full saved control inventory were subsequently read and copied without alteration. At 06:59:51.429107Z the unchanged original runner was reproduced with `/usr/local/bin/python3 -B`, a 120-second cap, and captured stdout/stderr. It returned 0 in 0.7891805 seconds: 151 passed, 0 failed. Its complete stdout is byte-identical to the saved author JSON. All inspected author source hashes were unchanged before and after execution. `AUTHOR_REPRODUCTION_v1.json` records this correspondence.

| Inspected source | SHA-256 |
|---|---|
| LAB_YUKAWA_BRIDGE_v1.md | 2f211e5710f8a2ebd44eb2c6f191ccf99674690db839e3f16585a4b39b83afb6 |
| LAB_YUKAWA_PLAN_v1.json | abca49a7abd34235ed03b294997de1acb5d493b279448f021215a0505ca5efae |
| SCALAR_SOURCE_CLOSURE_v2.md | c27e409e2c953b0a115569138e0b6357f246f8c14809b3c822789bd5869569bd |
| check_lab_yukawa_bridge_v1.py | 2227793a14146ab6da7e24a2a45d996f429c3c7ff130eaad901b54321ee626e4 |
| LAB_YUKAWA_CONTROLS_v1.json | 26de055d716d6fc5d4cb0226115aed71180282a3d14213cbcaaf1af4ffd1b295 |

The source-closure note was used for its supplied action, trace and charge normalization; this check does not newly validate all of its radiation/source claims.

## Independent proof findings

For the supplied trace equation, stress enters through `sigma = rho - sum(p_i)`. At a constant weak background with `D0 = 2 omega + 3`, the static linear equation is `(Delta-m^2) deltaF = -sigma/D0`. The convention `(Delta-m^2)(exp(-mr)/r)=-4 pi delta` therefore gives the positive Green factor `1/(4 pi D0)`. In the corresponding weak unscreened, negligible-stress body sector, the equal charge product is `a=1/D0` and `GT=1/(8 pi F0)`. Replacing the trace by density, and the receiving body by a density-only test response, needs those body premises. Decay at infinity, fixed coefficients, absence of additional chamber response and nonlinear screening are supplied boundary/environment premises.

For `r>R`, angular integration yields `4 pi exp(-mr) sinh(my)/(m r y)`. Thus `Q_m=4 pi integral y^2 sigma(y) sinh(my)/(my) dy`. Positivity, support at most R, and `0<=sum(p_i)<=epsilon rho` give `(1-epsilon)M<=Q_m<=M sinh(mR)/(mR)`, with the continuous m=0 limit. The monotonicity follows from the nonnegative derivative of `z cosh(z)-sinh(z)`. Support and total mass do not bound interior compactness: a shrinking central core has Yukawa factor tending to 1 but Newtonian central potential diverging as inverse core radius. Such a pressureless profile illustrates source-distribution freedom; it is not a constructed self-supported static material equilibrium.

For rotating coordinates x, `dr/dtheta=(x-y).Jx/r`; differentiating `U=-GT a exp(-mr)/r` gives the stated negative torque kernel `K_m=-(x-y).Jx (1+mr)exp(-mr)/r^3`. With Fourier coefficients defined using `exp(-in theta)`, the independent check gives `tau_n=-i n U_n`; the real cosine/sine coefficients are `2 Re(tau_n)` and `-2 Im(tau_n)`. A periodic conservative interaction has zero mean torque. Positive masses alone do not imply a nonzero selected harmonic.

On fixed geometry with separation at least d and lever arm at most L, `|K_m|<=L(1+md)exp(-md)/d^2`. Expanding the two perturbed density measures gives the stated bound proportional to `M_A deltaM_B + M_B deltaM_A + deltaM_A deltaM_B`. For signed density contrasts, M and deltaM must mean total-variation masses, not signed total masses. The bound is not a geometry-displacement error bound.

The common complex gain cancels only with the same gain in every modeled channel and a nonzero calibration record. For `r=(N_i+aY_i)/(N_c+aY_c)`, define `b=rN_c-N_i` and `A=Y_i-rY_c`; then `b=aA`. Nonzero-A channels must recover the same real, nonnegative a, while the original calibration denominator remains nonzero. `A=0,b!=0` is inconsistent, including when pairwise determinant tests alone vanish. `A=b=0` gives no value of a. At m=0, Y=N and all ratios become Newtonian geometry ratios independent of a. There is no first-order small-m correction to the torque factor, so long-range sensitivity can be poor even away from exact degeneracy.

For the complex fractional-linear inverse, the exact numerator of the difference is `(rhat-r)(N_c Y_i-N_i Y_c)`. The denominator lower bound is `|Ahat|-|Y_c|e`, which must be strictly positive. This proves the stated error bound without assuming real channel phases. An independently chosen complex error direction attains the bound in exact arithmetic. It is an externally supplied ratio-error bound, not a derived detector/calibration noise certificate, and it does not turn interval widths for geometry or density into such a certificate automatically.

The scale transformation `GT -> t GT, gain -> gain/t` is exact in the supplied record equations. It is not a proof that every transformed value is realized by a global scalar/matter/environment solution. Calling the calibration Newtonian does not remove its scalar leakage; in the massless equal-charge sector a measured Newtonian force scale would contain `GT(1+a)`. For `V=F W(log(F/C))`, direct differentiation gives `V_F=W+W_x`, `F V_FF=W_x+W_xx`; at a constant vacuum `W_x=W`, so `m^2=2(W_xx-W)/(2omega+3)`. C cancels from that conditional mass formula, not from the unresolved question of which physical background is selected.

## Distinct controls and source correspondence

The independently authored `independent_controls_v1.py` ran once in 0.9968409 seconds with 193 passed and 0 failed, empty stderr, and a 120-second cap. Its source SHA-256 is `9f735a7b684825a0c782eab5dfb6a98365e69fc144fbd7d6051b06a22ccfbd54`; result SHA-256 is `59b0a67d9b2a09048bdf3fcf3531d0050fd3f6eb6c6ecf4fb5cf564e04521f1a`.

Distinct controls include a nonpolynomial radial density with variable trace fraction, direct nested angular/radial integration against the reduced exterior formula (maximum discrepancy 1.39e-16), a different asymmetric 3-by-2 point configuration, independently differentiated energy and n=1,2,4 Fourier relations, positive-mass symmetry cancellation, a signed-zero-total-mass witness requiring total variation, genuinely complex geometry/gain channels, all zero-signal branches, and explicit saturation of the complex error bound. Source, pre-exposure freeze, complete output and receipts are retained.

The author runner's radial quadrature, torque derivative, harmonic cancellation, density perturbation and leaking-calibration checks implement the displayed formulas. Its geometry and profiles differ from the independent controls. Exact reproduction is separately recorded and is not counted as an independent derivation. Floating quadrature, finite differences and sampled angle grids remain numerical checks, not interval-certified integrations. A few floating ratio-error values can exceed the floating evaluation of the bound by roundoff well below the declared numerical allowance; the enclosure is the algebraic statement, not outward-rounded output. No tolerance was changed and no failed attempt was discarded in this review.

Remaining premises are the supplied action/background and static linearization, stable nonnegative mass and positive scalar kinetic coefficient, body trace/weak-charge assumptions, actual density and geometry, separation and boundary conditions, shared gain, sufficiently informative nonzero channels, and supplied measurement-error bounds. None is retired by this focused synthetic check. No PR, empirical fit, independent experimental test, or absolute physical calibration is claimed.
