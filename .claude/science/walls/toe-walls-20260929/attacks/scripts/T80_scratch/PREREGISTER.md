# T80 pre-registration (written BEFORE any run; Claude Sonnet 5.5, same family as supervisor)

Wall as I restate it: the record-dynamics lane adds one free dimensionless number per block.
The only number that belongs to record dynamics proper is the binding scale c (L01-W15, L16-W7 (i)).
The others in L16-W7 are gravity-member coefficients (K, alpha/K, bond-rate law) or formation-rate items
(sibling walls T64/T67/T68/T70, T01/T11). Route R1 = pin c = c0 (neutral, "crowding alone is neutral").

Question the test decides: does the pin c = c0 KILL the ordered phase at ordinary parameters
(so that a further number must be tuned, as blocks 126/153 suggest), or does the pinned gas order
in an O(1) window of (beta, z), so that the "further number" is a limit of the proof technique?

## Model (all runs)
Periodic L^3 cubic torus. Site = empty, or a record with content s. Sphere menu: s a unit 3-vector,
bond(record,record) = c exp(beta s.s'), bond with an empty end = 1, record weight z (uniform measure).
Two-valued menu: s = +-1. Neutral scale c0 = beta/sinh(beta) (sphere), 1/cosh(beta) (two-valued).
Exact site heat-bath on the 7-state (sphere) / 3-state (two-valued) variable. Order parameter
M = sum n_x s_x, U = 1 - <|M|^4>/(3 <|M|^2>^2) (limit 2/3 ordered; 4/9 sphere or 0 two-valued disordered).

## Checks and readings

### E1 (exact, Fractions): two-valued neutral gas == Ising high-temperature loop gas
Z_direct = sum_{sigma in {-1,0,1}^V} prod w(sigma_x) prod_edges (1 + t sigma sigma')  [w(0)=1, w(+-1)=z]
Z_HT     = sum_{E subset edges} t^|E| prod_v f(deg_E v),  f(0)=1+2z, f(even>=2)=2z, f(odd)=0.
PASS: exact equality on the cube graph for at least 3 (t,z) pairs. FAIL: any mismatch (then my "only loops bind at c0" reading is wrong).

### E2 (exact counting): 6N = 2 N_oo + N_oe, so c^{N_oo} = c^{3N} c^{-N_oe/2}  (chemical potential z' = z c^3, tension sigma = -ln(c)/2).
PASS: identity holds on 200 random configurations of the 4^3 torus. (Trivial; recorded so the reading "c is an interface coefficient" rests on a check.)

### E3 (numeric): massless surface of the mean-field mass channel (interaction note 2026-09-20 T5)
lambda_s = rho(1-rho)(g-1)/(1+rho(g-1)), g = c/c0. Finite-difference the 7-outcome self-consistent map.
PASS: finite difference equals closed form to 1e-6 at 5 points, and 6 lambda_s = 1 has a real density solution iff g-1 >= 24/25.
FAIL: mismatch => the note's T5 formula or my inversion is wrong; the "unpinned c still needs density tuning" claim is withdrawn.

### MC-A (main): does the pin kill order?
Runs: sphere menu, c = c0(beta), z in {1,3,10}, beta in {0.6,0.8,1.0,1.2,1.5,2.0,2.5,3.0}, L = 8 and 12 (L=16 for z=3).
Define "crossing at beta_c": U_12 - U_8 changes sign from negative (small beta) to positive (large beta) inside the grid,
with U_12 - U_8 > 3 combined standard errors on the large-beta side.
PASS (pin does not kill order; the extra-number claim is a proof-technique limit): for z = 3 and z = 10 a crossing exists with beta_c <= 3.0
AND at beta = 3.0 the order parameter per site m2 = <|M|^2>/V^2 at L=12 exceeds 0.10 with m2(L=12) >= 0.9 m2(L=8).
FAIL (pin kills order; a further number is physically needed): U_12 < U_8 for all beta <= 3.0 at z = 3 and z = 10, or m2 falling with L at beta = 3.
AMBIGUOUS: crossing only at z = 10, or a density jump (density variance kurtosis < 2.0 at any point, sign of bimodality) blocks the reading.

### MC-B (sensitivity of the ordering boundary to c)
Same grid with c = 1 (glue g = sinh(beta)/beta > 1) at z = 3, L = 8, 12.
Reading: if beta_c(c=1) differs from beta_c(c0) by > 0.25 (beta units) or rho differs by > 0.05 at fixed z, then c is load-bearing for the
phase boundary (the wall is real and the pin does work). If the shifts are below those, c is nearly irrelevant to order.

### MC-C (proof gap)
Closed form of block 126's sufficient criterion: order proven when (beta - gamma(c)) rho > 3 G(0), 3G(0) ~ 0.7586;
smallest proven c is c*(rho,beta) = g/sinh g, g = beta - 3G(0)/rho.  Compare c*/c0 with the MC (order at c0).
Reading: if MC orders at c0 where the proof needs c*/c0 > 1.5, the proof gap is at least that factor (a limit of the technique, not physics).

### Two-valued menu (block 153's case)
c0 = 1/cosh(beta); z in {1,3,10,1000}; L = 8, 12. Reading: an ordered phase (U crossing) at z <= 10 shows the unlocated window
1/320 <= z < 1e40 of PR #9285 contains ordered states at ordinary z.

## What each outcome moves
PASS => R1 survives: with c pinned the gas has parameters (beta_rule, z), z is state data, so the record-dynamics lane adds no free number;
the wall reduces to the premise c = c0 (PRICED).
FAIL => R1 dead as a route to long-range order: the pin costs the ordered phase and a second number is needed (STANDS).

---
## ADDENDUM (written after seeing the first ~55 of 112 batch-A1 rows; before any of the runs below)
What the partial batch showed (so the reader knows what was and was not blind): sphere, c = c0, z = 3 and 10 cross at beta_c ~ 0.96 and ~0.74;
z = 1 shows a density jump between beta = 1.2 (rho 0.54) and 1.5 (rho 0.90). Two follow-up tests, pre-registered now.

### MC-D (collapse): are c and z separately physical in the dense ordered phase?
Analytic prediction (suggested): for a dilute vacancy in an ordered dense phase the vacancy fugacity is 1/(z c^6 e^{beta*...}), so to leading
order in the vacancy density eps = 1 - rho, z and c enter only through z c^6; the exact identity c^{N_oo} = c^{3N} c^{-N_oe/2} (E2) shows the
residual is the interface tension, which first acts at O(eps^2).
Test: sphere, L = 12, beta = 1.2 and 1.5. Family N: neutral (g=1), z in {1,2,3,6,10,30}. Family O: c = 1, z in {0.1,0.2,0.4,0.8,1.5,3}.
Observable s = m2/rho^2 (order parameter squared per record) and U.  Log-interpolate s(rho) in each family and compare at rho = 0.90 and 0.95.
PASS (c is not an independent constant of the dense phase; only rho matters): |s_N - s_O| < 0.03 at both rho at both beta.
FAIL: |s_N - s_O| >= 0.06 at any of them (the interface tension has an independent bulk effect).  In between: report as partial.

### MC-E (order of the transition at low z, neutral scale): hysteresis
Sphere, c = c0, z = 1, L = 12, beta in {1.2, 1.3, 1.4, 1.5}, hot start and cold start (all records aligned), 6000 + 40000 sweeps.
Reading: hot and cold rho differing by > 0.10 at the same beta = first-order transition with a density jump (bistable): then rho is not a free
continuous state variable across the boundary. Agreement within 0.03 at all four = no hysteresis seen at this size.

---
## ADDENDUM 2 (written after MC-D/E order-parameter results were read; before the stiffness runs)
What MC-D/E showed (order parameter only): s = m2/rho^2 collapses onto one curve of rho for neutral and c = 1 families to <= 0.002 at rho in
[0.93, 0.998] for beta = 1.2, 1.5. Neutral family has ordered states down to rho ~ 0.82-0.90; the c = 1 family has a density gap (rho 0.29 -> 0.98 for
z 0.2 -> 0.4 at beta 1.5). No hot/cold hysteresis at beta = 1.2..1.5, z = 1, L = 12 (max |drho| = 0.0012). Not blind to these when writing the next test.

### MC-F (the quantity block 126's title says "is set by the binding scale": the infrared stiffness)
Measure the helicity modulus (stiffness) rho_s of the content field directly: twist the bond (s.s') by a spin rotation about axis a across all
bonds along direction d; Upsilon_{d,a} = (beta/V)<sum_oo (s_perp.s'_perp)> - (beta^2/V)<(sum_oo (s x s')_a)^2>; rho_s = (1/2) sum_a mean_d Upsilon_{d,a}.
Sanity: z = 1e6 (rho = 1), beta = 3 should give rho_s close to (slightly below) beta.
Test: sphere, L = 12 (L = 8 for size check), beta = 1.2 and 1.5, neutral family z in {1,2,3,6,10,30}, c = 1 family z in {0.8,1.5,3} (beta=1.2) and {0.4,0.8,1.5,3} (beta=1.5).
Compare rho_s at matched rho (log/linear interpolation in the neutral family).
PASS (stiffness is a function of (beta, rho) only, c not independent): relative difference < 5 % wherever both families are ordered and rho in [0.93, 0.998].
FAIL: relative difference > 10 % at any such matched point (then block 126's title stands for the physical stiffness, and the pin does work).
Also record rho_s at the neutral scale to compare with the proof's coefficient beta_A(c0) = 0 (the proof gives no bound there).
