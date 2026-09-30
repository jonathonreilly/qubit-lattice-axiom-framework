# T62 pre-registration (written 2026-09-29 before any T62 script was run)

Wall: the size of the cosmos (R_Lambda/a ~ 1e61, H_0) is put in by hand; S^3 versus flat.
Members: L13-W2, L13-W3.  Attacker: Claude Sonnet 5.5 (same family as supervisor).

Working hypothesis (to be attacked by the tests): T62 is not an independent wall.
  (i)   Lambda = 3/R^2 = lambda_1(S^3_R) is a slicing statement about de Sitter, true only on the
        H = 0 throat slice, so the S^3 versus flat clash is a label clash, not physics.
  (ii)  Lambda a^2 = 8 pi (G/a^2)(rho_vac a^4) = 3 (a/R_Lambda)^2, so R_Lambda/a is the same number as
        T60's rho_vac/rho_P once T70's G/a^2 is given.
  (iii) H_0 a is an epoch (age in ticks), i.e. registered data under realized_state_primitive.
The only route tested for actually producing the number is a COUNTING route:
  rho_vac a^4 = xi * N^(-p), N = number of lattice things in the causal patch, N ~ T^q, T = age/a.

## Test G (geometry, exact, sympy + arithmetic)
 G1 closed de Sitter ds^2 = -dt^2 + R^2 cosh^2(t/R) dOmega_3^2: Ricci = (3/R^2) g; slice radius
    a(t) = R cosh(t/R); lambda_1(slice) = 3/a(t)^2; H = tanh(t/R)/R.
    PASS-for-lane (S^3 identity usable today): lambda_1(slice today) = Lambda with H_0 != 0.
    FAIL-for-lane (my prediction): equality holds only at t = 0 where H = 0.
 G2 product R x S^3_rho ("stationary constant-radius S^3"): Ricci_00 = 0, so R_mu nu = Lambda g_mu nu
    (needs Ricci_00 = -Lambda) is impossible for Lambda > 0.  Prediction: not a vacuum solution.
 G3 closed FRW with dust+Lambda: lambda_1(S^3 today) = Lambda  <=>  Omega_m + Omega_r = 1.
    Prediction: contradicts Omega_m = 0.315 and the lane's own flat bridge Omega_m = 1 - Omega_Lambda.
    Also reproduce the lane's arithmetic: Omega_k = -Omega_Lambda, and R_curv >= ~22 c/H_0 for |Omega_k|<=0.002.

## Test U (unit map)
 U1 Lambda l_P^2 = 8 pi rho_Lambda/rho_P = 3 (l_P/R_Lambda)^2 to 1% (a tautology of definitions; the
    point is the accounting, not a discovery).  Report the band over H_0 in [67.4,73.0], Omega_L in [0.68,0.70].
 U2 holographic cell: a_h with (4 pi/3)(R/a_h)^3 = S_dS/ln2, S_dS = pi R^2/l_P^2.
 U3 numerology guard: how many "c * alpha_LM^n" hits fall in the observational band (calibrates the
    look-elsewhere; not evidence).

## Test C (counting exponents; the decisive arithmetic)
 Observed log10(rho_Lambda a^4 / (rho_P)) ~ -122.97 (a = l_P).  For each counting law
 (q, p) with xi = 1 compute log10 prediction.  A law PASSES if within 1.5 decades of observed
 (coefficient xi within ~30 of 1).  Candidates: creations-only Poisson (q=3,p=1/2), site-tick events
 Poisson (q=4,p=1/2), hyperuniform density fluctuation (q=3,p=2/3), area count 1/N (q=2,p=1),
 volume count 1/N (q=3,p=1), 1/sqrt(V4) with the real past-light-cone 4-volume.
 Prediction: exactly the laws with p*q = 2 pass; creations-only Poisson fails by ~31 decades,
 volume 1/N fails by ~60 decades.

## Test V (lattice number variance; decides whether local formation can supply p*q = 2)
 3D periodic lattice, L = 48 (and 32 for a check), 4 seeds.  Patterns: Bernoulli control (density 0.25);
 random-order formation with crowding rules A = {0..m}, m = 0,1,2,3 run to the frozen state;
 rule A = {0,2,3,4,5,6} (one recorded neighbour blocks); the referee's rule A = {0,3,4,5,6};
 chessboard control.  Windows: all cubic windows of side w = 1..16 (periodic, all positions).
 Measure s = d log Var(N_w) / d log w  (fit w = 4..16).  Relative fluctuation ~ w^(s/2 - 3), so
 p*q = 3 - s/2; the observed 1e-123 needs p*q = 2, i.e. s = 2 (hyperuniform).
 PASS (route survives, wounded): some non-crystal local-rule pattern has s <= 2.3 (fit error included).
 FAIL (route dead in the random-formation form): every disordered pattern has s >= 2.8.
 Prediction: FAIL.  Bernoulli s = 3.0; frozen crowding states s in 2.8-3.1 (finite Fano factor);
 chessboard s <= 2 (control passes trivially since it is a crystal).

## What each result would change
 G FAIL + U tautology  -> W3 dissolves; W2's Lambda half is T60's number; H_0 half is data  => PRICED.
 C: shows which count exponent any route must have (2 in T).
 V FAIL -> the natural "records fluctuate, vacuum energy is the fluctuation" route needs an ordered
 record pattern (a state property), so it is a relocation of the wall, not a pass.
 V PASS -> route R1 wounded only; the link "vacuum energy = count fluctuation" is still unsupplied.
