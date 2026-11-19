---
claim_id: fixed_lapse_keeps_lambda_independent_of_the_dark_constant_and_an_empty_mean_zero_start_forces_lambda_positive_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's fixed-lapse clause on isotropic edges (N = sin(eps0) l/sqrt3, so lapse a^n with n = 1) and the response law's constant per proper 4-volume Lambda: a read lapse a^n makes the tick's conserved value (the dark constant D) a fluid of w = n/3, so D is dark radiation (symbolic); Lambda enters the fixed-lapse generator as Lambda a^4 and D as a^0, so no shift of D absorbs Lambda (the unimodular degeneracy would need n = -3), and two readings of a(eta) separate them (det J = -4.124). For the homogeneous volume mode of an empty one-cube start on the finite log window l/L in [1/8, 2] (Dirichlet walls, hop kinetic matched to the classical Regge form): a mean-zero dark constant needs Lambda = <K>/<v> with K positive semidefinite, so Lambda >= 0, and Lambda > 0 strictly on the finite window (Lambda_min L^2 = 0.083 to 0.096 for 23 to 113 values per octave); with a transparent top Lambda_min falls as (top length)^-6 and as b^-6 for blocks, so the size is free; the mean form admits every Lambda >= Lambda_min. The tick has no Lambda period mod 2 pi because consecutive window ratios 2^(4/s) are irrational. Estimates and look-elsewhere statements: a least-kinetic start with a closed top gives a Planck-scale value, about 1e119 times the measured one; tick-count and split-count forms are dimensional coincidences. Supplied model, finite diagnostic: the unit map, the window, the minisuperspace mode, the hop kinetic, the least-kinetic start, the eps0 range and the measured Lambda; one radiation-like-spread statement is stated, not computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/fixed_lapse_keeps_lambda_independent_of_the_dark_constant_and_an_empty_mean_zero_start_forces_lambda_positive_2026_10_22.py
---

# Fixed lapse keeps Lambda independent of the dark constant, and an empty mean-zero start forces Lambda positive

Claim type: bounded_theorem.
Primary runner: `scripts/fixed_lapse_keeps_lambda_independent_of_the_dark_constant_and_an_empty_mean_zero_start_forces_lambda_positive_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3 in the three-law numbering) carries a supplied constant Lambda per proper 4-volume; its update law (CL-1) fixes the lapse per tick; the tick's conserved value, the dark constant D, has zero mean in every cube. This note asks whether the quantum edge rules (fixed lapse, mean-zero dark constant, the finite log window of edge values, the glued split) fix Lambda's sign or size, or make it periodic. Units: rung units, L the flat cell rung, 8 pi G hbar = L^2, c = 1; per cell and tick the proper time is sig l with sig = sin(eps0)/sqrt3. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Lambda and the dark constant under fixed lapse.

1. With lapse N = a^n the tick's conserved value enters the minisuperspace generator as a perfect fluid of w = n/3.
2. The fixed-lapse clause, sqrt3 N rms sqrt(gamma^ii) = sin eps0 on isotropic edges, gives N = sig l, so n = 1 and D is dark radiation (w = 1/3).
3. Lambda enters the fixed-lapse generator as Lambda a^4 and D as a^0. They are linearly independent, so no shift of D absorbs Lambda; the unimodular degeneracy would need n = -3. In conformal time, a'^2 = C(D + rho_m a + Lambda a^4/3), the coefficients are separately readable.

B. A mean-zero dark constant on the empty one-cube start (quantum volume mode, D = -K + Lambda v with zero matter departure).

4. <D> = 0 needs Lambda = <K>/<v>. K is positive semidefinite and v > 0, so Lambda >= 0. On the finite window K > 0 strictly, so Lambda > 0: the sign is forced.
5. Lambda_min is set by the window's lengths, mostly its top, not by the number s of window values per octave.
6. If the top is transparent (the glued split continuing the start's homogeneous mode), Lambda_min falls as (top length)^-6 towards 0: Lambda > 0 strictly, but its size is free.
7. In the mean form every Lambda >= Lambda_min has mean-zero states: no quantisation. The sharp form (a D = 0 eigenstate, which the response law rejects because it freezes the odds) would quantise Lambda at the generalised eigenvalues, Planck-spaced.
8. A block of b^3 cells moving together gives Lambda_min ~ b^-6.

C. Quasi-energy mod 2 pi.

9. Lambda -> Lambda + dL is a symmetry of the tick iff dL sig (l_n/L)^4 lies in 2 pi Z for every window value. Consecutive ratios 2^(4/s) are irrational for s not dividing 4 (and s > 23 is required), so no period exists.
10. Even an exact period (s dividing 4) would be at least 2 pi/v_min = 2 pi 8^4/sig in units 1/L^2: the circle acts only at the Planck scale.

D. Window, splits and tick-count forms.

11. One cell's Lambda phase over a split cycle (L -> 2L in de Sitter) is (7/sqrt3) sqrt(Lambda L^2). The window bounds it per cycle but no rule fixes it; demanding 2 pi gives a Planck-scale Lambda.
12. The runner states, without computing, that the dark constant's spread is radiation-like (w = 1/3) in every branch, so its zero-mean distribution cannot supply w = -1, and that the actuality law (CL-2) never changes a conserved value. A Sorkin-type 1/sqrt(V4) value would need Lambda conjugate to a 4-volume count; here D is conjugate to the tick count.

## Derivation

Items 1-3 are sympy algebra on the minisuperspace generator N sqrt(gamma)(rho - 3 H^2/(8 pi G)). The numeric separation integrates a'^2 = D + 1 + 0.3 a + Lambda a^4/3 by RK4 to two conformal times and takes the Jacobian in (Lambda, D). Items 4-8 build, on window values l_n/L = 2^(n/s - 3), n = 0 .. (4 + Delta) s, a hop kinetic operator K with bond weights 1/m, m = 6 b^3 x^2 (ln2/s)^2/sig, Dirichlet walls, and v = b^3 x^4; Lambda_min is the lowest generalised eigenvalue of (K, v). Item 7 builds mean-zero states from two generalised eigenvectors. Item 9 tests irrationality with sympy; a grid scan of 200000 values of dL up to 2 pi x 1e3 checks for near-periods. Item 11 integrates Lambda e^{3Ht} over one doubling.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- w = n/3; N = sqrt(3) l sin(eps0)/3 (symbolic).
- Lambda a^4 and D a^0 are separate monomials; det J = -4.124e+00 (asserted nonzero).
- Lambda_min L^2 = 8.346e-02 (s = 23), 9.142e-02 (s = 50), 9.562e-02 (s = 113), all positive.
- 2^(4/23), 2^(4/50), 2^(4/113) irrational; 2 pi 8^4 = 25736.
- Split-cycle coefficient 7/sqrt3 to 1e-9.

Finite diagnostics (supplied model, finite diagnostic):
- Spread of Lambda_min over s = 23 to 113: max/min 1.146; top 4L (Delta = 1, s = 50): 1.424e-03.
- Transparent top: top 2L, 8L, 32L give 8.3e-02, 2.0e-05, 5.0e-09; slope -6.00.
- Mean form: 7 targets in [1.01, 37.5] x Lambda_min each have a mean-zero state.
- Sharp form: Lambda_j/Lambda_1 = 1.00, 4.29, 9.79, 17.33.
- Blocks b = 1, 2, 4: slope -6.000.
- No near-period up to dL L^2 = 6e3/sig: best maximum distance from 2 pi Z is 0.470 turn (asserted above 0.05).

## Estimates against measurement

Estimates with supplied inputs (the Planck 2018 value Lambda L^2 = 7.151e-121 for L = sqrt(8 pi) l_P, t0 = 13.8 Gyr, eps0 = 0.0075 to 0.0375 from the register):
- A least-kinetic start with the top treated as a wall (a supplied clause) forces Lambda L^2 = 8.35e-02, about 1e+119 times the measured value; at b_e = 10 and 76 it is 8.3e-08 and 4.3e-13.
- Today's Lambda phase per cell-tick is 1.68e-122 rad (eps0 = 0.0075) and 8.37e-122 rad (eps0 = 0.0375); per split cycle 3.4e-60 rad; a 2 pi phase per cycle would need Lambda L^2 = 2.42.

Look-elsewhere statements (each a coincidence, not a derivation):
- The block that would give the measured value, b* = 6.99e+19, has b* L = 5.66e-15 m, close to the dimensional combination (L^2 R_Lambda)^(1/3) = 1.03e-14 m; it is not a rule scale (a one-cube start has b = 1; the rules use b_e of 10 to 76).
- (2 pi/N_ticks)^2 lands within about 1e2 of Lambda L^2 (ratio 8.3e-04 to 2.1e-02 over the eps0 range) because Lambda L^2 = 3 Omega_L (H0 L)^2 and N_ticks ~ 1/(H0 sig L); it tracks H^2, so w is not -1.
- 4^-k with k the split count to the Lambda radius equals (L/R)^2 by definition (k = 200.4 octaves); a growing count tracks a size-set term, which an earlier campaign computation found to dilute as w = -1/3, 23 sigma from the measured w.
- A family of 45 tick-count forms with eps0 free contains 1 hit within a factor 2 (the H^2 coincidence form); it would carry no weight.

## Boundary

Not claimed: a value of Lambda from the rules (only the sign under an empty mean-zero start, and a Planck-scale value under a supplied least-kinetic closed-top start); inhomogeneous edge modes beyond the minisuperspace volume mode; the matter departure's contribution; the radiation-like-spread statement of item 12 (stated, not computed); any period of Lambda for s dividing 4 below the stated bound.

## Supplied vs forced

Supplied: the unit map 8 pi G hbar = L^2; the Dirichlet window [L/8, 2L] (Delta = 0, also 1); the minisuperspace homogeneous mode; the hop kinetic matched to the classical Regge form; the least-kinetic start (estimate only); the eps0 range; the measured Lambda; t0. Forced, given those: w = n/3 and n = 1; the independence of Lambda and D; Lambda >= 0, and > 0 on a finite window, under an empty mean-zero start; the (top length)^-6 and b^-6 scalings; no quantisation in the mean form; no mod-2 pi period.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's fixed-lapse clause and finite log window, the glued split, the actuality law's conservation of conserved values, the response law's constant per proper 4-volume and zero-mean dark constant. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/fixed_lapse_keeps_lambda_independent_of_the_dark_constant_and_an_empty_mean_zero_start_forces_lambda_positive_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 110 MB resident, prints about 5.2 kB and ends with `TOTAL: PASS=20 FAIL=0`. It uses no random draws; two repeated runs gave identical output.
