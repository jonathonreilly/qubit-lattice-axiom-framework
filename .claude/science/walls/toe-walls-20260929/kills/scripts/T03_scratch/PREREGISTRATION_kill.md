# T03 kill check: pre-registration for the GRW/CSL exit (written before running kill_*.py)
Checker: Claude Sonnet 5.5 (same family as attacker and supervisor; same-family check, not a referee).

Question: does the attack's route R2 (GRW/CSL soft locks, "survives, priced, not new") deserve to be the T03 exit,
and what does it cost in a lattice whose only stated energy scale is the hop hbar*c/a?

Hypotheses (predictions, before running):
K1 (lattice, exact Lindblad, free fermions): mean energy input of a white-noise collapse whose operator is the SMEARED
   SITE OCCUPATION, on a half-filled Dirac walker sea, is  dE/dt = (gamma/2) sum_bonds |<h_b>| sum_x (Delta g)^2 > 0,
   scaling as rho^-3 (1D, normalised kernel width rho), and does NOT vanish as the sea is a vacuum.
   FAIL of prediction: rate ~ 0 or not ~ rho^-3.
K2 (same lattice): if the collapse operator is the smeared BAND-PROJECTED excitation number, the filled-band vacuum
   heating is exactly 0 (sum of second differences over the full Brillouin zone), and a single upper-band particle
   heats at (gamma/2) eps''(k0) * integral g'^2  (the nonrelativistic GRW/CSL value with 1/m = eps'').
   FAIL: vacuum rate > 1e-10 of the site-coupled rate, or particle rate off by > 5 %.
K3 (arithmetic, SI): standard NR mass-proportional GRW heating (3/4) hbar^2 lambda/(m r_C^2) per nucleon at
   lambda=1e-16 s^-1, r_C=1e-7 m is below Earth's internal heat 7e-12 W/kg by > 1e4; the repo's "3e15 times Earth's"
   (map check C) belongs to SHARP births; the vacuum heating of an unweighted site-occupation coupling of the walker
   sea, P/V = (3/4) lambda (a/r_C)^2 * 1.19 hbar c/a / a^3, exceeds the cosmic energy budget (6e-10 J/m^3 over 4.4e17 s)
   by > 1e30 at a = 1e-19 m.
   FAIL: NR heating within 1e4 of Earth's, or vacuum heating below the cosmic budget.
K4 (experiment): the mass-proportional CSL window at r_C = 1e-7 m keeps lambda ~ 1e-16 (allowed) but excludes Adler's
   1e-8; the NON-mass-proportional (unweighted) bound lambda/r_C^2 < 5.15e-6 s^-1 m^-2 excludes lambda=1e-16 at r_C=1e-7 m.
   Source: Majorana Demonstrator, PRL 129, 080401 (2022), arXiv:2202.01343 (text read from the PDF).
Decision: R2 "survives" as a route only if K2 and K3 hold (the collapse variable must be the band-projected excitation
density); if K1 holds, the site-occupation reading of "records at sites" is dead by heat at every spacing.
