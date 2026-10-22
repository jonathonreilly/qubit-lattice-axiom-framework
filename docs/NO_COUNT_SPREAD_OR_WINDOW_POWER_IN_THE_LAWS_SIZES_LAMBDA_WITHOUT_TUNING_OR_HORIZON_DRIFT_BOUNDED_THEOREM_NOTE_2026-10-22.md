---
claim_id: no_count_spread_or_window_power_in_the_laws_sizes_lambda_without_tuning_or_horizon_drift_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Three size rules for the response law's constant Lambda per proper 4-volume, built from structures of the candidate laws, tested against Lambda L^2 = 7.15e-121 (L = sqrt(8 pi) l_P) and w = -1. (a) Inverse counts: under the actuality law cell, split and record counts are fixed by the geometry (Fano 0); the split trigger never stops while H > 0, so no count freezes; the de Sitter past-cone 4-volume grows as (4 pi/3) H^-3 (t - 11/(6H)) (exact); a rule Lambda L^2 = C N^-p with N = k (HL)^-d has the de Sitter fixed point (Lambda L^2)^(1-pd/2) = C k^-p 3^(pd/2), rung-sized for order-one C and scale-free at pd = 2. (b) The dark constant's zero-mean spread: with lapse a^n its density goes as a^-(n+3), w = n/3, so under the fixed lapse every spread is dark radiation of either sign (exact enumeration of skewed zero-mean cells: mean 0, variance N sigma^2, P(negative) -> 1/2); w = -1 needs n = -3. A Sorkin-type variant (Lambda conjugate to 4-volume, not in the current laws) with exact counts and a least-kinetic edge vacuum gives 6 to 13 times the measured size but tracks H^2. (c) The window ratio 2^(4+Delta) per rung to the horizon gives about 1e-241 and tracks H^(4+Delta); a frozen variant 2^-(4+Delta)s hits at s = 99.8 only as a fit of s (chance 2/(4+Delta)). Every horizon-tied form has w0 > -0.7 and wa > 0, opposite in sign to DESI's wa. Supplied model, finite diagnostic: LambdaCDM (Planck 2018), the eps0 range, the edge vacua, the unimodular coupling of the Sorkin variant, and DESI DR2 (w0, wa) for a sign comparison."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/no_count_spread_or_window_power_in_the_laws_sizes_lambda_without_tuning_or_horizon_drift_2026_10_22.py
---

# No count, spread or window power in the laws sizes Lambda without tuning or horizon drift

Claim type: bounded_theorem.
Primary runner: `scripts/no_count_spread_or_window_power_in_the_laws_sizes_lambda_without_tuning_or_horizon_drift_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3) carries Lambda as a supplied constant per proper 4-volume, so w = -1 exactly and the size is free. Earlier notes show that record-count, growth, whole-history, relaxation and mod-2-pi rules fail (fixed 4-volume per record, PR #9900; Poisson record counts, PR #9876; fixed lapse and the one-cube sign, PR #9947). This note tests three further rules built from the laws' own structures: an inverse count at the end of the split cascade, the zero-mean spread of the dark constant, and the edge window's ratio raised to a rung count. None gives about 1e-120 without tuning and without drift. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

Units: rung units, L the flat cell rung, 8 pi G hbar = L^2, c = 1. Per cell and tick the proper time is sig l, sig = sin(eps0)/sqrt3. Measured: Lambda L^2 = 3 Omega_L (H0 L)^2 = 7.151e-121 (Planck 2018; the register's 7.3e-121 uses a slightly different H0), ln(1/Lambda L^2) = 276.65, H0 L = 5.90e-61.

## Statement

A. Inverse counts (idea a).

1. Under the actuality law every matter site records once per half-tick, and each split turns one block into eight. Cell, split and record counts in any region are fixed by the geometry, with Fano factor 0. Discreteness gives no Poisson fluctuation.
2. The split trigger fires whenever a block's log-mean edge reaches twice the flat length. With H > 0 this happens every ln2/H, so the cascade never ends and no count freezes. A comoving region's cell count grows as a^3.
3. In de Sitter the past-cone 4-volume is V4 = (4 pi/3) H^-3 (t - 11/(6H)) + O(e^-Ht). It grows linearly, at the rate of one horizon volume.
4. Fixed points. Take a rule Lambda L^2 = C N^-p, with N a horizon-tied count equal to k (HL)^-d in de Sitter (d = 3 for cells, 4 for cell-ticks). With H^2 = Lambda/3 the rule gives (Lambda L^2)^(1 - pd/2) = C k^-p 3^(pd/2). For pd != 2 and order-one C the value is rung-sized (0.65 for horizon cells at p = 1; 107 for horizon cell-ticks at p = 1; 0.19 at p = 2, d = 3). For pd = 2 the rule is scale-free: any size, or none, depending on C k^-p alone. A small Lambda needs C of order 1e122.
5. Today's past cone holds N = V4/(sig L^4) = 4.7e241 to 2.3e242 cell-ticks (V4 = 0.1229 H0^-4). 1/N is 2e-242, off by 1e-121. 1/sqrt(N) is 0.09 to 0.20 times the measured value, which is the known Sorkin coincidence.
6. Drift. A density proportional to V4^-q has w = -1 + (q/3) dlnV4/dlna, and dlnV4/dlna = 3.96 today in LambdaCDM. That gives w0 = 0.32 at q = 1 and w0 = -0.34 at q = 1/2, with wa = +1.01 and +0.51.

B. The dark constant's zero-mean spread (idea b).

7. The tick's conserved value is N sqrt(gamma) rho_D. With lapse a^n, rho_D goes as a^-(n+3), so w = n/3. The fixed lapse has n = 1, so every dark-constant spread is dark radiation, w = 1/3 exactly. Only a unimodular lapse (n = -3) would make it a w = -1 term. This rederives item A of PR #9947.
8. Exact enumeration of N zero-mean cells with a skewed three-valued spread gives a sum of mean 0 and variance N sigma^2 exactly. Its sign is either: P(negative) is 0.400, 0.486, 0.514 and 0.497 at N = 1, 4, 16 and 48. A Hubble-volume average is a random-sign term of size sigma/sqrt(N_H), so the zero-mean clause makes it a fluctuating dark-radiation term, not a fluctuating Lambda. Its size is the free sigma.
9. Sorkin-type variant (not the current law). If Lambda were conjugate to 4-volume, through the dropped fixed-4-volume clause or a unimodular lapse, then Delta Lambda Delta V4 / L^2 ~ 1. By item 1 counts do not fluctuate, so Delta V4 comes only from the edges' length spread: Delta V4 = sig L^4 sqrt(N) std(x^4), x = l/L. That gives Delta Lambda L^2 = 1/(r sqrt(sig <x^4>) sqrt(V4/L^4)) with r = std(x^4)/<x^4>. For the least-kinetic edge vacuum of PR #9947 (s = 23, Lambda_min L^2 = 0.083, r = 0.74) this is 6.0 to 13.4 times the measured value over the eps0 range, and 8.0 for a uniform window. Sharper edges (r -> 0) raise it.
10. The variant tracks. |rho_L|/rho_c goes as 1/(sqrt(V4) H^2). Normalised to today's 0.685 it is 1.96 at BBN and 1.50 at recombination, against bounds of about 0.05 and 0.02. The ratio is fixed by the background, so no prefactor fits both.

C. The window ratio per rung (idea c).

11. From the cell to the Hubble radius there are k = 200.1 rungs (200.4 to the Lambda radius sqrt(3/Lambda)). 2^-(4+Delta)k is 1.2e-241 at Delta = 0 and 7e-302 at Delta = 1, about (Lambda L^2)^2. A hit needs 4 + Delta = 1.992, which is the horizon tautology Lambda = 3/R^2.
12. Any horizon-counted rung number tracks. rho proportional to H^p gives w = -1 + p eps/3, with eps = -dlnH/dlna = 0.47 today: (w0, wa) = (-0.68, +0.65) at p = 2, (-0.37, +1.30) at p = 4 and (-0.21, +1.62) at p = 5. Its self-consistent de Sitter fixed point is Lambda L^2 = 3^((4+Delta)/(2+Delta)), which is 9.0 at Delta = 0.
13. Frozen variant. 2^-(4+Delta)s, one over the number of states of one edge-register end, is a fixed integer power, so it would not drift and would keep w = -1. It matches at s = 99.8 (Delta = 0; s = 100 gives 0.54 times the measured value), 79.8 (Delta = 1), 66.5 (Delta = 2) and 57.0 (Delta = 3), all inside the allowed s range of 23 to 113. With s free the chance of a factor-2 hit is 2/(4+Delta), 0.50 to 0.29, so the match is a fit of s. No law ties Lambda to that dimension.

D. Against DESI. Every horizon-tied form above has w0 > -0.7 and wa > 0, because eps falls towards today. DESI DR2 (with CMB and DESY5) prefers w0 of about -0.75 and wa of about -0.86. So the tracking forms miss the measured w = -1 and point the opposite way from the DESI hint. The constant forms (CL-3 as written, and the frozen variant) give w = -1 exactly and share K3's DESI tension.

## Candidate law tested (not adopted)

> "Edge-register dimension. Lambda per proper 4-volume is 2^-(4+Delta)s in rung units, one over the number of occupation states of one end of an edge register."

Smuggling check. The text uses no measured number, but its content is the choice s(4 + Delta) = 399, which the update law leaves free (it gives only s >= 0.85/sin eps0). It trades one supplied number, Lambda, for another, s, at a factor-2 chance of 50%. There is no derivation: Lambda is a phase per proper 4-volume, and nothing in CL-1 to CL-3 links it to a register's Hilbert-space dimension. The register should not adopt it unless s is fixed independently, for example by the coupling or edge-stiffness fits. A fixed s would make it a prediction of Lambda.

## Derivation

Item 3 is sympy on int_0^T (1 - e^-x)^3 dx, with the past-cone slice volume (4 pi/3) H^-3 (1 - e^-H tau)^3 in de Sitter. Item 4 solves Lambda = C (k (Lambda/3)^(-d/2))^-p. Items 5, 6, 10 and 12 integrate LambdaCDM (Omega_m 0.3153, Omega_r 9.1e-5, Omega_L 0.6847) on 240001 log-a points from a = 1e-12. V4 at an observer is the trapezoid integral of a^3 (4 pi/3) chi^3 dt, with chi the comoving distance to the observer. The CPL tangent is wa = -dw/da at a = 1. Item 7 is sympy on rho_D ~ a^-(n+3). Item 8 enumerates multinomial sums exactly. Item 9 rebuilds PR #9947's hop kinetic K on the window (bond weight 1/m, m = 6 x^2 (ln2/s)^2/sig, Dirichlet walls) and takes the |psi|^2 spread of x^4 in its lowest generalised mode with v = x^4.

## Finite checks

The runner gives 14 PASS and 0 FAIL. Several PASS lines record a failure against measurement.
- Exact: counts with variance 0 (one-cube start, 3 splits, 5 ticks: 512 cells, 46800 records), Poisson control Fano 0.999 (seeded); de Sitter constant -11/6; w(n) = n/3; enumeration mean 0 and variance N sigma^2 to 1e-9.
- Diagnostics: V4 H0^4 = 0.0044, 0.1229, 1.021 and 3.464 at a = 0.5, 1, 2 and 4; dlnV4/dlna = 3.962 today and 5.482 at a = 0.5. Lambda_min L^2 = 0.083 reproduces PR #9947.

## Boundary

Not claimed: that no size rule exists. Only these three families are excluded, together with their horizon-tied and frozen variants. Not computed: inhomogeneous edge modes, correlated edge spreads across cells (the coherent many-cell limit, which raises item 9's value), and a self-consistent everpresent-Lambda history. The DESI comparison is a sign test against supplied central values, not a fit. Open: a rule-fixed integer near 399 bits (item 13), or a conserved charge set by the first slab (register; it joins the initial-odds gap).

## Supplied vs forced

Supplied: LambdaCDM and the measured values, the eps0 range, the edge vacua (least-kinetic, uniform), the unimodular coupling in items 9 and 10, the rule families' forms and prefactors C and q, and DESI DR2 central values. Forced, given the laws: exact counts (Fano 0), no freezing of the cascade, linear growth of the de Sitter past cone, the fixed-point relation, w = n/3 with n = 1, and the random-sign dark-radiation character of the zero-mean spread.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs.
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1's fixed lapse, finite log window and split trigger; CL-2's record per site per half-tick and its conservation of conserved values; CL-3's constant per proper 4-volume and zero-mean dark constant. Zero premise weight; results that use it are conditional on it.
- Builds on the open notes of PR #9947 (fixed lapse, one-cube sign), PR #9900 (fixed 4-volume per record) and PR #9876 (record-count Lambda needs Poisson input).

## How to run

```
python3 scripts/no_count_spread_or_window_power_in_the_laws_sizes_lambda_without_tuning_or_horizon_drift_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 118 MB resident, prints about 4.7 kB and ends with `TOTAL: PASS=14 FAIL=0`. It is seeded (one Poisson control), and two runs gave identical output apart from the runtime line.
