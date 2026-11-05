---
claim_id: time_reversal_freezes_half_filled_sea_records_and_record_count_lambda_needs_poisson_input_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For a supplied half-filled Floquet sea of the supplied 1D pair walk and the supplied 3D spin-3/2 block tick, a site-diagonal antiunitary that reverses both half-ticks makes the odds equal at both half-ticks, so the record-formation rule moves nothing and vacuum records are frozen; in these models record counts are not Poisson (window-dependent Fano factor, area-law variance, past-cone variance growing as R^3). Under the supplied identification volume = record count, the unimodular estimate of Lambda depends on the Fano factor; Poisson counting at the rule density gives an estimate within a factor 10 of measured, the frozen sea does not, and a Sorkin-type Lambda is compared with measured w as an estimate. No vacuum, volume rule, causal-set structure or value of Lambda is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/time_reversal_freezes_half_filled_sea_records_and_record_count_lambda_needs_poisson_input_2026_10_21.py
---

# Time reversal freezes half-filled-sea records, and a record-count Lambda needs Poisson input

Claim type: bounded_theorem.
Primary runner: `scripts/time_reversal_freezes_half_filled_sea_records_and_record_count_lambda_needs_poisson_input_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note asks whether reading 4-volume as the number of records, as in causal-set estimates of the cosmological constant, works with the register's record-formation rule. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used, and main chooses no vacuum, so the half-filled sea is supplied.

## The unimodular estimate and the Fano factor

The vacuum energy density rho_L is conjugate to the 4-volume V, and a minimum-uncertainty packet has delta rho_L delta V = hbar/2 (runner value 0.50000000). Write V = v0 N with Var N = F <N>, where F is the Fano factor. The uncertainty reading gives rho_L ~ hbar / sqrt(F v0 V). The classical-sum reading Lambda = S/V gives rho_L ~ hbar sqrt(F) / sqrt(v0 V). The two agree only at F = 1 and move apart by the factor F otherwise. With the rules' element v0 = a^3 tau = 729.4 Planck 4-volumes per record, rho_L/rho_P = 1/sqrt(F kappa V_P) with kappa = 729.4. Counting cells instead overestimates by the factor kappa.

## Theorem: the half-filled sea is frozen

Suppose a site-diagonal antiunitary reverses both half-ticks. Then the Floquet sea has the same odds at both half-ticks, and the rule that the record set changes as little as possible moves nothing, whatever the tie-break. Every vacuum record is then frozen.

- 1D pair walk (L = 12, 924 configurations): the pair unitaries are symmetric, so U_e U_o = (U_o U_e)^T. The odds at the two half-ticks differ in total variation by 1.1e-15, the stay probability is 1, and the autocorrelation at 256 half-ticks is 1.000. Each pair's occupation is conserved, so the rule splits into independent groups, and both tie-breaks keep the odds.
- Control: a ring flux breaks the antiunitary. The odds then change (total variation 0.074, stay 0.926) and the autocorrelation at 256 half-ticks falls to 0.24.
- 3D spin-3/2 block tick with a gapped half-filled sea (mu = 0.4, b = 0.3, 4 of 8 bands filled): all hop holonomies are real with faces -1, and the antiunitary is solved to a maximum entry error of 1.9e-14 on the 8^3 torus. The |C|^2 differ by 1.1e-16 and the 4x4 minors by 8.3e-17, so the 3D vacuum records are frozen too.

## Records are not Poisson in these models

- 1D Fano factors depend on the window: 1.00 (2x2), 0.36 (6x2), 256.75 (2x512), 91.47 (6x512) for the frozen sea, and similarly for the moving control.
- 1+1D past-cone diamond: Var grows as T^1.036 while the mean grows as T^2; the Fano factor at T = 128 is 0.0179.
- 3D equal-time cube of side l: Var = 0.50 l^2, an area law (8.00 at l = 4 against 16 for independent sites, 50.32 at l = 10 against 250).
- 3D past cone: Var ~ R^3.10 with Var/R^3 = 1.063 while the mean grows as R^4, so delta N ~ V^(3/8). The Fano factor falls from 0.159 to 0.085.

## Estimates against measured Lambda

Measured rho_L = 1.133e-123 rho_P. The past light-cone 4-volume today is 0.1230 H0^-4 = 6.39e242 Planck units.

- If records were Poisson (F = 1) at the rule density, rho_L = 1.46e-123 rho_P, 1.29 times measured. The factor depends on conventions and spans roughly 0.2 to 10.
- For the frozen sea, delta N = 1.0e90 against sqrt(N) = 9.4e119. The uncertainty reading gives 1.3e-93 rho_P, about 1e31 too large, and the classical-sum reading gives 1.6e-153 rho_P, about 1e-31 too small.
- Counting matter relays per half-tick gives N = 3.6e148 in the past cone and rho_L = 3.0e-169 rho_P.
- In an empty vacuum there are no records, so the volume-count rule would give voids no volume.

A Sorkin-type Lambda (S/V random walk over nested past cones, Poisson reading) tracks the critical density, with standard deviation of Omega_L 2.54 at BBN, 1.94 at recombination and 0.88 today. At coefficient 1, histories matching today give w_eff(z = 0.5) = -0.28 [-1.22, +0.28], and the sampled fraction with w within 2 sigma of the measured -1.03 +- 0.03 is 0.000. Adding BBN and recombination, the best factorised probability over coefficients 0.1 to 3 is 2.0e-11. These are estimates against approximate bounds.

## Checks

The runner prints `TOTAL: PASS=19 FAIL=0`. Its PASS lines cover the conjugacy bound, the Fano dependence of the two readings, the element normalisation, the 1D and 3D antiunitary theorems and frozen odds, the flux control, the non-Poisson window, diamond, cube and past-cone counts, the three normalisations of the Lambda estimate, and the three measured-constraint comparisons.

## Supplied and boundary

Supplied: the 1D pair walk and its masses, mu and b, the half-filled sea, the tie-breaks (shown not to matter), the unit map a = sqrt(8 pi) l_P with tau = 2a/(sqrt(3) c), the volume-count identification, the S/V dynamics, the LCDM background and the bounds used. A Poisson sprinkling would be imported from causal-set theory, not derived from the odds, and the uncertainty reading needs V in superposition while records are definite. No vacuum, volume rule, causal-set structure or value of Lambda is established.
