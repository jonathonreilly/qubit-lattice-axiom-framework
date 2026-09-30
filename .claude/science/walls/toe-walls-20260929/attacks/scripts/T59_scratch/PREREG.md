# T59 pre-registration (written before T59_test.py was run)

Question the test decides: how much of "cosmic history" do the abundances and the
expansion law actually read, and is the fixed-lattice reading of expansion viable?
All parts use SUPPLIED models (label: checked, supplied model, same-family). None is a
derivation from the four axioms.

## A. Initial-state independence of the freeze-out yield (radiation era, s-wave)
Model: dY/dx = -lam x^(q-4) (Y^2 - Yeq^2), x = m/T, Yeq = (45/4pi^4)(g/g*s) x^2 K2(x),
q = 2 (H ~ T^2). lam set so Omega h^2 ~ 0.12 for m = 3.94 TeV, g*s = 427/4.
Grid: x_i in {0.3,0.5,1,2,4,8}, Y_i/Yeq(x_i) in {1e-12,1e-6,1,1e3}. Integrate to x=400.
- PASS (thermal start is not a premise beyond an inequality): max relative spread of Y_inf
  over the whole grid <= 1 %.
- FAIL: spread > 5 %. (1-5 % = partial; report.)
- Control (must show the inequality is real): starts at x_i >= 30 with Y_i = 1e-12 Yeq or 1e3 Yeq must
  give spreads > 50 %; if not, the "attractor" test is vacuous.

## B. What the yield reads of the expansion history
B1 kernel: K(ln x) = d ln Y_inf / d ln H(x), by Gaussian bumps (sigma_u = 0.2 in ln x) on
48 log-spaced centres x in [0.2, 500].
- PASS: 5-95 % window of |K| spans <= 1.5 decades in x (<= 3 decades in radiation-era time),
  and integral of K equals the global response d ln Y/d ln H within 5 %.
- FAIL: > 10 % of |K| outside x in [1, 300] (the yield reads the very early or very late history).
B2 exponent scan: H = H_m x^-q, q in {0,1,1.5,2,3(<3 excluded from analytic)}, same lam.
- PASS ("the expansion LAW is load-bearing, the wall does not vanish"): Y_inf(q=1)/Y_inf(q=2) >= 10.
- FAIL: < 3.
- Also record analytic Y_inf ~ (3-q) xF^(3-q)/lam agreement (informative only).

## C. Symbolic: does block 146 discharge the H_rad (rho+3p) gate inside its own model?
(sympy) Claims: (i) acceleration eq + continuity => d/dt[ldot^2 - (8piG/3) rho l^2] = 0
(Friedmann with integration constant k); (ii) block 146's massless branch l=(1+t/t1)^(1/2),
t1^2 = 6 alpha/eps, satisfies constraint, length eq, and H^2 = (8piG/3) rho at alpha = K/4,
G = 1/(16 pi K); matter branch l=(1+t/t0)^(2/3) likewise; (iii) with kinetic prefactor exponent s
instead of 3: radiation exponent = 2/(1+s), matter = 2/s, so both 1/2 and 2/3 need s = 3 = d.
- PASS: all residuals simplify to 0 (checked exactly).
- FAIL: any residual nonzero, or (iii) exponents not as stated.

## D. Counting numerology (reading only)
Lambda l_P^2 * sqrt(V4/l_P^4) for V4 = past-light-cone 4-volume and V4 = (4pi/3)(c/H0)^3 t0.
- "Coincidence of order" if |log10(product)| <= 1.5 for both conventions. Anything else: fail.
- This is NOT evidence; it is the input count for the causal-set / everpresent-Lambda route.

## E. Fixed-lattice causal-fill bound
Ratio R = particle horizon (proper, today) / (c t0) in flat LCDM with radiation, over
H0 in [60,75], Om in [0.25,0.40].
- PASS (kills "expansion = growth of the recorded region on a fixed lattice at <= 1 site/tick"):
  R >= 2 everywhere on the grid. (Then the site count exceeds the light-speed fill by R^3.)
- FAIL: R < 1.5 anywhere.

## F. Does one history datum (age) replace (H0, L)?
Fix t0 = 13.8 Gyr, Omega_r = 9.2e-5, flat. For L in {0.5,0.6,0.685,0.75,0.85} solve H0.
- PASS ("age is a third observable of the same 2-parameter family; it replaces neither"):
  H0 varies by > 10 % over the range.
- FAIL: <= 10 %.


Deviation logged at run time: starts with x_i < 1 and Y_i/Yeq = 1e3 are skipped (equilibration
is faster than the double-precision spacing in x, so the solver cannot resolve it; the states are
equilibrated instantly in any case).  Y_i/Yeq grid uses 1e-12 not 1e-20 for the same reason.
