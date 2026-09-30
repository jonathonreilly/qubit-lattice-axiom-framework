# GRW/CSL exit for T03: detail behind the kill report (Claude Sonnet 5.5, same family; not a referee)

Scripts and outputs in this folder: `PREREGISTRATION_kill.md` (written first), `kill_lattice_csl_heating.py` / `out_kill_lattice.txt`
(11/0; first run `out_kill_lattice_first_run.txt` had 3 failures that were bugs in my own test: wrong analytic vacuum energy -1/pi
instead of -2/pi for two modes per site, a spurious factor N in the one-particle prediction, and an ill-posed 1e3 criterion),
`kill_grw_csl_arithmetic.py` / `out_kill_arith.txt` (8/0), `kill_3d_constants.py` / `out_kill_3d_constants.txt`,
`rerun_fast.txt`, `rerun_test3.txt` (reruns of the attack's scripts).

## 1. The physics in one paragraph
White-noise collapse with Hermitian one-body operators L_x = sum_z g_x(z) n_z has mean dynamics d rho/dt = gamma sum_x (L rho L - {L^2,rho}/2).
Every operator O_M = c^dag M c obeys [L,[L,O_M]] = O_{[A,[A,M]]}, so the one-body matrix closes and the mean energy input is exact:
dE/dt = -(gamma/2) sum_x Tr([A_x,[A_x,h]] Gamma).  (Checked against the full many-body Lindblad on 4 sites, 8 modes: 0.21433525 both ways.)
For nearest-neighbour hopping and a site-diagonal A this is (gamma/2) sum_bonds |<h_b>| sum_x (dg)^2, the f-sum rule, and it is
nonzero in ANY vacuum with bond energy (checked in 1D: rate*rho^3 constant to 0.6 % for rho >= 4; formula matches the exact rate to 6 digits).
For a band-diagonal A (excitation-number density) the vacuum term is a sum of second differences over the full Brillouin zone and vanishes
(1e-15 to 1e-16), while one particle heats at (1/2) eps''(k0) integral g'^2 (ratio 0.97-1.00 for rho=10).
3D constants (`kill_3d_constants.py`): <|s|> = 1.1938 (repo: 1.19); (1/2) gamma int|grad g|^2 with gamma = lambda (4 pi r_C^2)^{3/2} is (3/4) lambda / r_C^2 (grid 0.746).

## 2. SI numbers (reference inputs as in the repo runner `scripts/record_birth_rate_bound_from_heat_budgets_2026_09_28.py`)
- NR mass-proportional GRW: 4.99e-44 W per nucleon, 2.99e-17 W/kg, 4.3e-6 of Earth's 7e-12 W/kg; 5.0e-28 J per hit.
- Sharp births at GRW's rate (map check C): 3e15 and 2e31 times Earth's, reproduced. A soft NR hit is 7.5e20 (a=1e-19 m) to 4.7e36 (l_P) times cheaper per hit.
- Site-occupation coupling of the walker sea, vacuum: P/V = (3/4) lambda (a/r_C)^2 <|s|> (hbar c/a)/a^3.
  a = l_P: 7.9e68 x cosmic budget; 1e-19 m: 2.1e37; 1e-15 m: 2.1e29; 1e-9 m: 2.1e17 (budget 6e-10 J/m^3 over 4.4e17 s = 1.4e-27 W/m^3).
  lambda allowed by the budget alone at 1e-19 m: 4.8e-54 s^-1. Ordinary-matter NR heating for comparison: 3e-14 W/m^3.
- Reading of the 1D scan: the vacuum bill per site is set by t and barely falls with mass, the particle bill goes as 1/m.

## 3. Experimental window (what I rely on)
Read from the PDF text of arXiv:2202.01343 (Majorana Demonstrator, PRL 129, 080401 (2022)), saved by the fetch tool:
- theory values quoted there at r_C = 1e-7 m: GRW 1e-16 s^-1; Bassi et al. 1e-10 (+-2 orders); Adler 1e-8 (+-2), and 1e-6 (+-2) at r_C = 1e-6 m;
- non-mass-proportional CSL: lambda/r_C^2 = (5.15 +- 0.16)e-6 s^-1 m^-2 (limit; "factor of 39 improvement");
- mass-proportional, 30 quasi-free electrons: (17.4 +- 0.5); mass-proportional with coherent nuclear emission: (4.94 +- 0.15)e-1 ("factor of 105"),
  "most stringent limits in the region r_C < 1e-6 m". They say the electron-only limit "first fully excludes" Bassi et al.'s values.
- At r_C = 1e-7 m these are lambda < 5e-20, < 1.7e-13, < 4.9e-15 s^-1. A review summary (arXiv:2508.18822, via a fetch summariser, not verified
  against primary papers) quotes the same 4.9e-15 and adds CUORE 3.3e-11, Neptune heating 6.6e-11, optomechanics 2.0e-10 at r_C = 1e-7 m.
- Not relied on / from memory: Donadi et al., Nature Phys. 17, 74 (2021) (excluded the parameter-free Diosi-Penrose model; abstract seen);
  Carlesso et al., Nature Phys. 18, 243 (2022) (review; abstract only); Bassi et al., Rev. Mod. Phys. 85, 471 (2013); Adler, J. Phys. A 40, 2935 (2007);
  the coherent-nuclear-emission enhancement is model-dependent (an electron-only reading is ~35 x weaker); dissipative or coloured variants have different bounds.
- Window for mass-proportional CSL at r_C = 1e-7 m: 1e-16 <~ lambda <~ 5e-15 s^-1 (49 x margin under the strongest, model-dependent limit; 1700 x under the electron-only one).
  An unweighted coupling is out at GRW's lambda, r_C = 1e-7 m; at lambda = 1e-16 it needs r_C >~ 4.4e-6 m (from this one bound; whether such a point still collapses macroscopic pointers is NOT checked).

## 4. Prior art in the repo (paths)
- `docs/TOE_VIABILITY_MAP_WHERE_THE_AXIOMS_ARE_EXPOSED_AND_THE_FASTEST_DECISIVE_TESTS_2026-09-27.md` (PR #9363): Option B `:489-498`; "Drop primitive collapse" `:635`; check D `:844-857`.
- `docs/RECORD_FORMATION_A_SHARP_ONE_SITE_LOCK_COSTS_THE_ENERGY_OF_ITS_BONDS_…_2026-09-27.md` (#9363): T6(b) soft record; escape 1 `:358-365` "has the shape of the spontaneous-collapse models ... relativistic versions are known to excite the vacuum for the reason T6 shows".
- `docs/UNDER_A_UNITARY_WAVE_WITH_BORN_COUNT_STATISTICS_…_2026-09-28.md` (#9363): escape 4 (flashes) `:165-172`, N1 route 4 `:215`; it says the flash route "pays the record cost that option C avoids"; that is true of a site projection and not of a band-diagonal soft hit.
- `scripts/record_birth_rate_bound_from_heat_budgets_2026_09_28.py` (#9363): checks C and D. C is correct and is about SHARP births at GRW's rate.
- `archive/notes/docs/work_history/repo/review_feedback/BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md:142-190,489-490,660-675`: GRW, CSL, Dowker-Henson (qubits on a 1+1 null lattice with a collapse parameter), rGRWf: ATTEMPTED; residuals: weights and readiness are law inputs, covariance, wavefunction sufficiency.
- `archive/notes/…/RECORD_FORMATION_THREE_ROUTE_ASSUMPTIONS_EXERCISE_AND_AXIOM_TARGET_NOTE_2026-07-13.md:215,290`: row EN (collapse heating or loss); GRW/rGRWf "route-one reference architecture: modified dynamics, basis/rate/constants, energy/noise signatures".
- On main: `docs/ADMISSIBILITY_RULE_WHAT_A_FORMATION_EVENT_DOES_TO_THE_LEDGER_AND_TO_THE_FAR_FIELD_…_2026-09-21.md:37,134` (a sudden localisation does not keep energy and the centre of energy; the dipole moves unless hit odds are ledger-matched); `docs/RECORD_FORMATION_CLOCK_IN_THE_CLAUSE_…_2026-09-24.md:156` (GRW and Diosi as prior art for state-dependent rates).
- `docs/FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md:332-334`: the repo's own non-unitary (GKLS) formation law; its energy per event diverges (Delta = delta/eps^2) and it "does not supply autonomous fuel". The attack's Test 2 (2 Delta per birth, 0 in H') restates this.
- Open PRs: only #9363 bears on this (gh search "collapse OR GRW OR CSL OR localisation OR flash").

## 5. What the exit still does not give (labels)
- Permanence: by ontology in the flash reading (a flash is an event in the history), not by dynamics. In the wave-level reading a localised single particle re-spreads on m r_C^2/hbar ~ 1.6e-7 s (arithmetic, nucleon) against a hit every 1e16 s, so only macroscopic pointers are effectively permanent. [suggested]
- Content: GRW hits are position events. "Locks exactly one admissible possibility of a qubit" needs a hit variable built from the qubit's possibility; for Heisenberg qubits a smeared sigma^z density also has a f-sum vacuum bill (the same double commutator, (2/3) of the bond energy), so the same band-diagonal requirement appears (a smeared magnon number). [suggested, not run]
- Born: hit density is the norm-square of the global wave by construction, so T05 is assumed, not solved, and Admissibility's nearest-neighbour clause covers only which possibility is locked, not where or when (axioms memo, Admissibility reading note 2). Formation site and rate are exactly what the memo leaves downstream, so GRW is a candidate supplier for T01, consistent with the axioms.
- Relativistic: the nonrelativistic model is what the bounds test. White-noise relativistic extensions excite the vacuum (literature, and the repo's own note); Tumulka's rGRWf is covariant for non-interacting distinguishable particles only (archive audit `:176-185`). [reading]
