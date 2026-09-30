"""T03 kill check: SI arithmetic for the GRW/CSL exit.  Pre-registered as K3, K4 in PREREGISTRATION_kill.md.

Inputs marked (ref) are reference inputs from the literature or the repository's own runner
(scripts/record_birth_rate_bound_from_heat_budgets_2026_09_28.py on PR #9363), not framework content.
The lattice-side formulas are the ones verified numerically in kill_lattice_csl_heating.py.
"""
import math

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    PASS += bool(cond); FAIL += (not cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}")


HBAR = 1.054571817e-34        # J s
C = 2.99792458e8
HBARC_EVM = 1.973269804e-7    # eV m
EV = 1.602176634e-19
M_N = 1.67262192e-27          # kg (ref)
LAMBDA_GRW, RC = 1e-16, 1e-7  # s^-1, m  (GRW 1986, ref)
NUC_PER_KG = 6e26             # (ref, as in the repo runner)
EARTH = 7e-12                 # W/kg (ref, as in the repo runner)
RHO_COSMIC, T_H = 6e-10, 4.4e17   # J/m^3, s (ref, as in the repo runner)
LP = 1.616255e-35
COST_PARTICLE_HOPS, COST_LOCK_HOPS = 1.19, 2.39   # probe 1 T4 (repo)
SEA_BOND_ENERGY_PER_SITE_HOPS = 1.19              # = <|s|>, all vacuum energy is hopping (probe 1 T4)

print("== 1. Standard nonrelativistic, mass-proportional GRW/CSL heating (ref formula: Bassi et al. RMP 85, 471 (2013))")
per_nuc = 0.75 * HBAR ** 2 * LAMBDA_GRW / (M_N * RC ** 2)
per_kg = per_nuc * NUC_PER_KG
print(f"   per nucleon {per_nuc:.2e} W; per kg {per_kg:.2e} W/kg; Earth internal heat {EARTH:.1e} W/kg; ratio {per_kg / EARTH:.1e}")
per_hit = 0.75 * HBAR ** 2 / (M_N * RC ** 2)
print(f"   energy per hit (NR nucleon) {per_hit:.2e} J")
check("1a K3: NR GRW heating is below Earth's internal heat by more than 1e4", per_kg < EARTH / 1e4, f"(ratio {per_kg / EARTH:.1e})")

print("== 2. The repository's check C (sharp births at GRW rate) reproduced, and what it compares")
for label, a in (("a = 1e-19 m", 1e-19), ("a = l_P", LP)):
    hop = HBARC_EVM / a * EV
    birth = COST_PARTICLE_HOPS * hop
    heat = LAMBDA_GRW * NUC_PER_KG * birth
    print(f"   {label}: sharp birth {birth:.2e} J; GRW-rate sharp births heat {heat:.2e} W/kg = {heat / EARTH:.0e} x Earth;"
          f" NR soft hit is {birth / per_hit:.1e} x cheaper per hit")
    check(f"2 {label}: map check C reproduced (> 1e10 x Earth)", heat / EARTH > 1e10)

print("== 3. Vacuum heating if the collapse operator is the smeared SITE OCCUPATION of the walker sea (unweighted coupling)")
print("   P/V = (3/4) lambda (a/r_C)^2 * <|s|> (hbar c / a) / a^3    [3D, from the double commutator; 1D verified in kill_lattice_csl_heating.py]")
budget = RHO_COSMIC / T_H
print(f"   cosmic energy budget: {RHO_COSMIC:.1e} J/m^3 over {T_H:.1e} s = {budget:.2e} W/m^3;"
      f"  ordinary-matter NR heating at 1e3 kg/m^3: {per_kg * 1e3:.1e} W/m^3")
worst = 1e99
for label, a in (("a = l_P", LP), ("a = 1e-19 m", 1e-19), ("a = 1e-15 m", 1e-15), ("a = 1e-9 m", 1e-9)):
    t_J = HBARC_EVM / a * EV
    PV = 0.75 * LAMBDA_GRW * (a / RC) ** 2 * SEA_BOND_ENERGY_PER_SITE_HOPS * t_J / a ** 3
    lam_max = LAMBDA_GRW * budget / PV
    worst = min(worst, PV / budget)
    print(f"   {label}: P/V = {PV:.2e} W/m^3 = {PV / budget:.1e} x cosmic budget; lambda allowed by the budget alone: {lam_max:.1e} s^-1")
check("3 K3: the site-occupation vacuum bill exceeds the cosmic budget by > 1e30 at a = 1e-19 m",
      (0.75 * LAMBDA_GRW * (1e-19 / RC) ** 2 * SEA_BOND_ENERGY_PER_SITE_HOPS * (HBARC_EVM / 1e-19 * EV) / 1e-19 ** 3) / budget > 1e30)
check("3b it exceeds the budget at every spacing from l_P to 1e-9 m", worst > 1)

print("== 4. Experimental window (ref: Majorana Demonstrator, PRL 129, 080401 (2022), arXiv:2202.01343; text read from the PDF)")
lims = {"mass-proportional, coherent nuclear emission (lambda/r_C^2 < 0.494 s^-1 m^-2)": 0.494,
        "mass-proportional, quasi-free electrons only (lambda/r_C^2 < 17.4)": 17.4,
        "non-mass-proportional (lambda/r_C^2 < 5.15e-6)": 5.15e-6}
for k, v in lims.items():
    print(f"   {k}: lambda < {v * RC ** 2:.2e} s^-1 at r_C = 1e-7 m;  GRW's 1e-16 is {'inside' if LAMBDA_GRW < v * RC ** 2 else 'EXCLUDED'}"
          f" ({(v * RC ** 2) / LAMBDA_GRW:.2g} x margin)")
print(f"   theory values quoted in that paper at r_C = 1e-7 m: GRW 1e-16; Bassi et al. 1e-10+-2; Adler 1e-8+-2")
check("4a mass-proportional CSL: GRW's 1e-16 allowed, Adler's 1e-8 excluded (coherent-emission limit)",
      LAMBDA_GRW < 0.494 * RC ** 2 and 1e-8 * 1e-2 > 0.494 * RC ** 2)
check("4b non-mass-proportional CSL: lambda=1e-16 at r_C=1e-7 m is excluded", LAMBDA_GRW > 5.15e-6 * RC ** 2)
rc_min = math.sqrt(LAMBDA_GRW / 5.15e-6)
print(f"   unweighted coupling at lambda = 1e-16 needs r_C >= {rc_min:.1e} m (from the X-ray bound alone; other constraints not checked)")

print("== 5. Sparsity of flashes (GRWf reading): can 'one record per site' hold without coarse-graining?")
sites_universe_1e19 = (4.3e26 ** 3 * 4 * math.pi / 3) / (1e-19) ** 3
flashes = 1e80 * LAMBDA_GRW * 4.4e17
print(f"   flashes in the universe over 4.4e17 s (1e80 nucleons, lambda = 1e-16): {flashes:.1e}; sites at a = 1e-19 m: {sites_universe_1e19:.1e};"
      f" ratio {flashes / sites_universe_1e19:.1e}")
print(f"   sites per hit-width volume (r_C/a)^3 at a = 1e-19 m: {(RC / 1e-19) ** 3:.1e}")
check("5 flashes are sparser than sites by > 1e40 (one per site holds trivially)", flashes / sites_universe_1e19 < 1e-40)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
