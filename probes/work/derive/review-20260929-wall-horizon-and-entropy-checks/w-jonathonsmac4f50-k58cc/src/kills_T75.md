# Kill check on T75

Checker: Claude Sonnet 5.5 (same family as the attacker and supervisor; not an independent referee). Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md`, `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (registry text as generated there), lane entries L15-W6/W7, the attack report, PREREG, RESULTS, all scripts, and blocks 53, 55, 56 on main. All attack scripts re-run (each under 11 s); every output file is identical to the attacker's. My own scripts: `kills/T75_scratch/K1..K6`.

## Outcome verdict
WEAKENED. PRICED stands as an outcome, but two claims are overstated and the price omits a premise.

## Route verdicts
| Route | Verdict | Reason, with evidence |
|---|---|---|
| R1 lattice Unruh | wounded | The post-hoc "0.3%" is a through-origin fit (`A4_planck_plot.py`) dominated by high-energy levels. Level by level (`K1_lowlevels.py`, checked) the low levels, the ones that set a temperature, sit 7-11% high: eps/(pi E) for the lowest level is 1.106, 1.096, 1.088, 1.081, 1.076, 1.070 for N = 100..3200, converging slowly and not shown to reach 1. The attacker's own matrix fit (`out_A3.txt`) gives 1.09-1.07. The test also uses the uniform-chain vacuum, so it shows Unruh/Bisognano-Wichmann kinematics for a supplied profile, not Hawking emission. Registered A missed (0.775); geometry was changed after the miss (disclosed). R^2 is not discriminating: the double-zero control also has R^2 = 0.994-0.997, and only the drift in beta separates it. |
| R2 stopped clock from the ledger | wounded | B2 reproduces (m = 17.925 at w0 = 1e-3). "One bond energy only" is overclaimed: three energies were tried, and any bond energy with finite dF/dw at w = 0 stops at finite mass. Block 56 T5 (`:96`) selects F1 (quadratic in phi) among nearest-neighbour covariant bilinear energies, and F2/F3 violate that principle. The report never says so. |
| R3 misframed | survives as a reading | Shapiro-Teukolsky cite is from memory, flagged as such. |

## Errors found
1. "Every smooth weight-one energy gives a double zero" is a formal-asymptotic lemma (suggested), and it is not universal. (a) It needs a source-free exterior or nonnegative rest energies. With F1 and a negative amplitude energy density phi'' = -phi/(4x^2), w has a LINEAR zero (`K6_negsource.py`, checked; positive c gives p = 2.7, 4). Block 56 T1 Remark (`:64`) says energy density can have both signs, and Hawking's near-horizon energy density is negative. The price should say "source-free or nonnegative-energy exterior". (b) The exponent is the order of vanishing of f: plugging u = p ln n into the exact stationarity gives p = q for f = |d|^q (`K5_asymptotic_root.py`, checked as a formal root only). Quartic f gives p = 4, still no linear zero. Non-smooth q = 1 (total variation) is degenerate and admits any monotone profile, linear included. (c) f = d^2 (smooth, f_2 > 0, weight one) gives p(20) = 0.18 at N = 400, w0 = 1e-9 (`K2_general_f.py`); that energy cannot reach w = 0 at finite cost, so no stopped region exists there, but the pre-registered B3 band (p(20) >= 1.7) would fail on it.
2. B3's F1 result is tautological (phi linear); F2 and F3 are the only non-trivial checks. B1 (3D) missed its band; the double zero in 3D rests on the Hopf lemma for F1 only. F2/F3 balls were not tested.
3. "The framework clock dresses hopping only" (block 55 `:26`) is wrong as stated: phi H phi with a mass term gives an on-site potential proportional to w. Massive walkers were not tested.
4. No prior art found in `docs/` or archive for the lattice Bisognano-Wichmann or double-zero result (grep; `gh` search returned nothing). Not proof of absence.
5. Line cites to blocks 53, 55, 56 check out.

## Corrected plain-language verdict
The lattice clocked walker's vacuum looks thermal at pi/kappa to about 1% overall and 7-11% for the lowest levels, but that is Unruh kinematics with a supplied profile. For the framework's own supplied energy (F1), a stopped region in a source-free exterior has a double zero, so kappa = 0. The zero exponent equals the order of vanishing of the stiffness, and a negative-energy near-horizon source could make it linear, so "kappa = 0" needs that premise named. Priced, not passed.
