---
claim_id: nuclear_vacuum_breakup_under_rule_fixed_dimension_six_liv_is_a_hard_wall_below_fifty_eev_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "With the rule-fixed dimension-six dispersion (c_q = -S/6 + 1/24, E* = 1.217e18 GeV) and nucleons taken UNIVERSAL (c_N = c_q at all momenta; bracket c_N = 0.214 c_q): (i) [T] at matched velocities the free-nucleon and additive-bound LIV are identical (c P^3/A^2) and stationary; the breakup driver is second order, the negative curvature 6c/A of sum x^3 (convexity of x^3 with c < 0), not a first-order 'sum x^3 < 1' term; (ii) [F] exact light-front two-body diagonalisation at fixed P (rank-one separable kernel, x and k_perp, deuteron binding reproduced): the bound deuteron does not follow the flow (|c_eff|/|c| 0.253 -> 0.308, universal = 1) and dissolves at 2.5/3.0/4.3 EeV (axis/sky/body); (iii) [F] nucleon + core cluster model: breakup opens at t 3.3-5.7, 4He 4.1-7.0, 14N 8.6-15, 56Fe 18-31 EeV (x 1.47 at the weak-driver end), insensitive to the form-factor range (beta 0.2-0.4 GeV changes lam_open by < 3 %); (iv) [F] above opening the frozen nucleus is a resonance (N, Fe) or no pole at all (d, He) with decay lengths 1e-8 to 5e-3 m at 1.1-2 x P_open: a hard wall, 22 orders below kpc; (v) [E] above <= 46 EeV on every ray/beta/c_N corner the rules' UHECR flux is nucleons only, contradicting Auger's heavier-and-purer composition at 50-100 EeV. Verdict: EXCLUDED unless the rules also alter air-shower development (uncomputed)."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/nuclear_vacuum_breakup_under_rule_fixed_dimension_six_liv_is_a_hard_wall_below_fifty_eev_2026_10_26.py
---

# Nuclear vacuum breakup under the rule-fixed dimension-six LIV is a hard wall below 50 EeV

Runner: runner.py. TOTAL: PASS=11 FAIL=0, 2.3 s, seeded, AUDIT_TIMEOUT_SEC = 120, 3.6 k characters, 120 MB.
Criteria fixed before the run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic in a supplied exact model, [E] estimate vs measurement, [S] reading.
Pre-run deviation, stated: F1c's pre-written tolerance (within 10 % of additive) was too tight; the computed
slope reaches 1.23 x additive before the pole dissolves. The check was rewritten to "< 1/2 of universal" and
the number is reported. F1d was rewritten to accept the two degenerate (x*, 1-x*) minima of the symmetric case.

## Builds on / narrows
- agents/liv-surviving-observables (A3c): its claim "nuclei cannot follow the flow" is CONFIRMED by an exact
  model, and its walls are SHARPENED DOWNWARD. Its kinematic openings (d 3.5-6, Fe 19-32 EeV) are reproduced
  (d slightly lower, 2.5-4.3). Its "Fermi core" walls (Fe 100-160 EeV) are WITHDRAWN: the exact width is not
  suppressed, so the wall is the kinematic opening.
- agents/composite-dispersion: its line "nuclei inherit the same flow [S]" stays contradicted.
- No prior main-branch work on vacuum dissociation (git grep origin/main, docs+scripts).

## Results
- [T] T1 (sympy). A universal nucleons at P/A carry A c (P/A)^3 = c P^3/A^2, the same as the additive bound
  nucleus, and sum x^3 is stationary at x_i = 1/A. So the naive driver "sum x_i^3 < 1, nucleus less
  subluminal" is zero at matched velocities. The real driver is the Hessian 6c/A < 0: the LIV rewards
  unequal sharing. Unbound matched nucleons go locally unstable at lam|c| = M^2 A^4/3,
  P_inst = A (M^2 E*^2/6|c|)^(1/4) (A = 2: 2.3/2.8/4.0 EeV).
- [F] F1, deuteron. Exact at fixed P: separable kernel f = 1/(M0^2 - 4M^2 + 4 beta^2), beta = 0.286 GeV
  (Yamaguchi), strength fixed by B = 2.2246 MeV; the k_perp integral is closed form (matches 2D quadrature to
  2e-16), so the eigenvalue condition g I(z) = 1 is a 1D integral in x.
  - Bound-state slope dM_B^2/d(lam|c|) = -0.253, -0.260, -0.308 at 0, 0.5, 0.95 lam_open (additive -0.25,
    universal -1). The bound state barely follows.
  - The continuum minimum leaves x = 1/2 continuously (pitchfork at 16M^2/3 = 4.70 GeV^2). The pole meets it
    and dissolves at lam|c| = 6.60 GeV^2, i.e. P = 2.50e18 (axis), 3.03e18 (sky), 4.33e18 (body) eV.
- [F] F2, cluster N + (A-1), lowest single-nucleon separation energy (AME values, supplied), core at c/(A-1)^2.

  | Nucleus | lam_open|c| (GeV^2) | P_open axis / sky / body (EeV) | per nucleon, axis |
  |---|---|---|---|
  | t | 19.9 | 3.3 / 4.0 / 5.7 | 1.1 EeV |
  | 4He | 45.5 | 4.1 / 4.9 / 7.0 | 1.0 EeV |
  | 14N | 929 | 8.6 / 10.4 / 14.9 | 0.62 EeV |
  | 56Fe | 1.74e4 | 17.9 / 21.7 / 31.0 | 0.32 EeV |

  - beta = 0.2 / 0.4 GeV moves lam_open by < 3 %: the opening is kinematic (frozen pole vs the far minimum).
  - At the weak-driver end c_N = 0.214 c_q everywhere, all P x 1.47 (exact scaling): Fe <= 45.6 EeV.
  - The real nucleon has c_N(P/A) < c_q in the bound state, while the emitted fast nucleon is near c_q.
    That mixed case drives harder than either bracket, so the bracket's top is an upper bound.
- [F] R, rate. Complex pole of the exact amplitude, Gamma_M2 = 2 Im I/Re I', Gamma_lab = Gamma_M2/2P:

  | Nucleus | x1.1 P_open | x1.5 P_open | x2 P_open |
  |---|---|---|---|
  | 14N | L = 1.2 mm | 67 um | 9 um |
  | 56Fe | L = 5.1 mm | 1.3 mm | 0.27 mm |
  | 4He | no pole, L_form 2e-7 m | 2e-8 m | 7e-9 m |

  - Fe Gamma_M2 = 1.5e-3 GeV^2 at 1.1 P_open, narrow against the 1.07 GeV^2 gap.
  - The form-factor tail is power law, not exponential, so there is no Fermi-core suppression. It is a HARD
    WALL, about 22 orders below the kpc scale.
  - Products: one nucleon with most of P plus a cold core, which cascades on.
- [E] Confrontation (sources below).
  - Every nucleus t..56Fe is gone above <= 46 EeV on every ray/beta/c_N corner. Nuclei heavier than Fe extrapolate
    as P_open ~ A^0.53 (N -> Fe) and would need A ~ 250 for 100 EeV, so there are none in practice. The
    predicted flux above 50 EeV is protons and neutrons.
  - Auger SD + deep learning (arXiv:2406.06315, PRL 2025; PRD 111 companion arXiv:2406.06319): composition
    "increasingly heavier and purer", incompatible with a large light fraction between 50 and 100 EeV.
    Pure protons there would sit about 100 g/cm^2 deeper in <Xmax>, with sigma(Xmax) about 2x larger,
    several times the hadronic-model spread. EXCLUDED.
  - Amaterasu, 2.44e20 eV (TA, Science 382, 903 (2023), doi:10.1126/science.abo5095), and Fly's Eye,
    3.2 +- 0.9e20 eV (Bird et al., ApJ 441, 144 (1995); Xmax 815 g/cm^2 does not identify the primary):
    both must be protons under the rules. That is CONSISTENT on its own, since there is no GZK horizon
    upstream, but it is not a rescue.
  - TA hybrid composition is light below 10^19.1 and statistics-limited above (arXiv:1810.00431,
    arXiv:2209.03591). It is NOT in conflict, and it does not offset Auger.

## Verdict (pre-registered): BREAKUP REAL; HARD WALL; EXCLUDED by Auger 50-100 EeV composition
- Caveat that could reopen it: the flowed proton (one quark at x ~ 1) might develop air showers differently,
  biasing the Xmax-based lnA. That is uncomputed and should be the next probe.
- Minimal rescue in rule terms (UNTESTED, gate below). The driver is the dimension-six term itself (the
  negative curvature of c x^3). The minimal rule-level cure is to make the update's leading lattice correction
  vanish at order p^4 for every species, e.g. a symmetric two-rung composition of the tick (zoom first). The
  first surviving term is then dimension eight. The same analysis gives
  P_inst = A (M^2 E*^4/20|c8|)^(1/6) ~ 1e21 A eV, so Fe ~ 1e22 eV, safely above every event, and time of
  flight becomes unmeasurable.
  - Gate: no number chosen, no observed structure named, bends no axiom (CL-1 condition). Its untested
    prediction is that the c pattern, the 1e17 eV gamma -> e+e- cutoff and the body cones of the parent note
    all disappear.
  - Alternatives not preferred: flipping the sign of c (superluminal; concave x^3 stabilises nuclei, but it
    reopens vacuum Cherenkov for e at ~5e16 eV) or raising E* by ~30x (a fitted number, gate FAIL).

## Smuggling review
- Forced or exact: c_q pattern and E* (upstream); the light-front placement lam sum c x^3; T1 algebra; the
  closed-form k_perp integral; the pole and width formulas.
- Supplied:
  - the universal-nucleon hypothesis, bracketed by 0.214 c_q;
  - the rank-one separable kernel and its invariant-mass form factor (beta);
  - measured separation energies;
  - the core at its additive c/(A-1)^2, a two-body cluster model for A >= 3, and no LIV in the kernel;
  - the Auger/TA/Fly's Eye values.
- Nothing is fitted. No rule is adopted.

## Open
- Air-shower Xmax of a flowed proton, and of nucleons from breakup.
- A three-body light-front nucleus with transverse dynamics, as a check on the cluster model.
- The LIV in the NN kernel.
- Building and testing the dimension-eight (p^4-cancelling) tick.
