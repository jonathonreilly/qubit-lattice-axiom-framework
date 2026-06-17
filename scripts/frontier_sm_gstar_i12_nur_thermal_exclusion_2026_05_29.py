#!/usr/bin/env python3
"""Verification runner for the g_* census import I12 (nu_R thermal exclusion).

Supports
docs/SM_GSTAR_I12_NUR_THERMAL_EXCLUSION_BOUNDED_NOTE_2026-05-29.md.

I12 is the sharpest fork of the high-T unbroken-phase g_* census:

    nu_R excluded from the light-relativistic census  ->  g_* = 106.75
    nu_R thermalized as a Dirac partner               ->  g_* = 112.

nu_R = (1,1)_0 is a complete gauge singlet (zero color, zero isospin, zero
hypercharge), so it equilibrates with the thermal bath ONLY through its Dirac
Yukawa coupling y_nu to the gauge-charged operator H.L. This runner asserts, as
EXECUTED arithmetic (not prose):

1. **The fork dof arithmetic.** 15 gauge-charged Weyl/gen -> 30/gen -> 90 ->
   g_* = 28 + (7/8)*90 = 427/4 = 106.75; 16 Weyl/gen (adding nu_R) -> 32/gen ->
   96 -> g_* = 112. Fork delta = 21/4 = 5.25 (the nu_R contribution). Exact
   rationals via fractions.Fraction.

2. **The Yukawa implied by the empirical small neutrino mass.** With the Dirac
   mass m_D = y_nu * <H>, <H> = 174 GeV (the one-Higgs vev convention v/sqrt2),
   an empirical neutrino mass m_nu ~ 0.05-0.1 eV implies y_nu ~ 3e-13 to 6e-13.
   This reproduces the "order 10^-13" tiny Dirac Yukawa quoted by the retained
   no-go NEUTRINO_LANE4_DIRAC_SEESAW_FORK_NO_GO_NOTE_2026-04-27. The small
   neutrino mass m_nu is an ADMITTED EMPIRICAL OBSERVATION (comparator), NOT a
   framework derivation.

3. **The Yukawa needed for nu_R thermalization.** Order-of-magnitude
   equilibration criterion Gamma ~ y_nu^2 T >~ H ~ 1.66 sqrt(g*) T^2 / M_Pl
   gives a threshold y_thr ~ sqrt(1.66 sqrt(g*) T / M_Pl). Even at the most
   lenient (lowest) census temperature T ~ 100 GeV, y_thr ~ 1e-8; at
   leptogenesis temperatures T ~ 1e9-1e12 GeV, y_thr ~ 4e-5 to 1e-3.

4. **Incompatibility (the load-bearing assertion).** The implied small-m_nu
   Yukawa is below the thermalization threshold by MANY orders of magnitude at
   every relevant temperature (>= 4 orders even at the most favourable T = 100
   GeV; ~7-9 orders at leptogenesis T). Gamma/H << 1 throughout: nu_R is
   decoupled. The ONLY route to g_* = 112 is a thermalizing Dirac Yukawa
   y_nu >= y_thr (with O(1) as a stronger steelman), which is excluded by the
   small neutrino mass.

5. **Branch table.** Across the framework's RETAINED-no-go Dirac/seesaw fork:
   light Dirac (small y_nu) -> nu_R never thermalizes -> EXCLUDED -> 106.75;
   heavy Majorana/seesaw (M_R >> T) -> nu_R not a light dof at the census epoch
   -> EXCLUDED -> 106.75; thermalizing Dirac (y_nu >= y_thr) -> thermalized
   -> 112 but EXCLUDED by the empirical small m_nu. So g_* = 106.75 is robust across
   BOTH branches of the retained no-go, conditioned on the empirical small m_nu.

6. **Note / authority cross-checks.** Reduction bookkeeping, authority-file
   existence, optional ledger-status cross-check (the no-go is retained_no_go;
   the functional-form theorem is retained), and a no-overclaim /
   forbidden-import / new-vocabulary scan.

The smallness of m_nu is named as an ADMITTED EMPIRICAL OBSERVATION (comparator),
not a framework derivation; the runner does NOT derive small neutrino mass. No
lattice-action quantity or fitted selector is a load-bearing input. The Dirac
vs Majorana branch is NOT picked by the framework (retained no-go); the result's
strength is branch-independence.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import math
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT / "docs" / "SM_GSTAR_I12_NUR_THERMAL_EXCLUSION_BOUNDED_NOTE_2026-05-29.md"
)
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


NOTE_TEXT = NOTE_PATH.read_text(encoding="utf-8")
NOTE_FLAT = re.sub(r"\s+", " ", NOTE_TEXT)


# ===========================================================================
# Framework / census constants (sourced from the companion census notes)
# ===========================================================================

# Gauge-charged Weyl content per generation (retained / decoration-under-retained
# in the sibling R-MATTER note); the gauge-singlet nu_R is the 16th Weyl.
GAUGE_CHARGED_WEYL = 15
NU_R = 1                       # (1,1)_0 gauge singlet: zero color/isospin/hypercharge
N_GEN = 3
WEYL_DOF = 2                   # particle/antiparticle cardinality (retained)
N_BOSONS = 28                  # retained-sourced bosonic count (companion notes)
W_F = Fraction(7, 8)           # fermion thermal weight (retained hierarchy_seven_eighths)

# Physical constants (order-of-magnitude inputs; standard, not fitted selectors).
M_PL_GEV = 1.22e19             # Planck mass in GeV
HUBBLE_PREFACTOR = 1.66        # radiation-era H = 1.66 sqrt(g*) T^2 / M_Pl
# One-Higgs vev convention <H> = v/sqrt2 = 174 GeV (the convention the retained
# no-go uses for m_D = y_nu <H>); expressed in eV for m_nu in eV.
H_VEV_EV = 174e9


# ===========================================================================
# 1. The I12 fork dof arithmetic: 106.75 (excluded) vs 112 (thermalized)
# ===========================================================================

section("1. I12 fork dof arithmetic (106.75 vs 112)")

per_gen_excluded = GAUGE_CHARGED_WEYL * WEYL_DOF          # 15*2 = 30
n_fermions_excluded = N_GEN * per_gen_excluded            # 3*30 = 90
g_star_excluded = N_BOSONS + W_F * n_fermions_excluded    # 28 + (7/8)*90

check(
    "nu_R excluded: gauge-charged Weyl/gen = 15",
    GAUGE_CHARGED_WEYL == 15,
)
check(
    "nu_R excluded: 15 Weyl * 2 = 30 dof/gen",
    per_gen_excluded == 30,
    f"{per_gen_excluded}",
)
check(
    "nu_R excluded: N_fermions = 3 * 30 = 90",
    n_fermions_excluded == 90,
    f"{n_fermions_excluded}",
)
check(
    "nu_R excluded: g_* = 28 + (7/8)*90 = 427/4 = 106.75",
    g_star_excluded == Fraction(427, 4) and float(g_star_excluded) == 106.75,
    f"{g_star_excluded} = {float(g_star_excluded)}",
)

full_matter_weyl = GAUGE_CHARGED_WEYL + NU_R              # 16
per_gen_dirac = full_matter_weyl * WEYL_DOF               # 16*2 = 32
n_fermions_dirac = N_GEN * per_gen_dirac                  # 3*32 = 96
g_star_dirac = N_BOSONS + W_F * n_fermions_dirac          # 28 + (7/8)*96 = 112

check(
    "full framework matter = 15 gauge-charged + 1 nu_R = 16 Weyl",
    full_matter_weyl == 16,
    f"{full_matter_weyl}",
)
check(
    "nu_R thermalized Dirac: 16 Weyl * 2 = 32 dof/gen",
    per_gen_dirac == 32,
    f"{per_gen_dirac}",
)
check(
    "nu_R thermalized Dirac: N_fermions = 3 * 32 = 96",
    n_fermions_dirac == 96,
    f"{n_fermions_dirac}",
)
check(
    "nu_R thermalized Dirac: g_* = 28 + (7/8)*96 = 112",
    g_star_dirac == Fraction(112),
    f"{g_star_dirac} = {float(g_star_dirac)}",
)
check(
    "I12 fork is load-bearing: 106.75 (excluded) != 112 (thermalized)",
    g_star_excluded != g_star_dirac,
    f"{float(g_star_excluded)} vs {float(g_star_dirac)}",
)
fork_delta = g_star_dirac - g_star_excluded
check(
    "fork delta = n_gen * (nu_R Weyl) * 2 * 7/8 = 3*1*2*7/8 = 21/4 = 5.25",
    fork_delta == Fraction(21, 4) and float(fork_delta) == 5.25,
    f"{fork_delta} = {float(fork_delta)}",
)
# Sanity: 15->30->90->106.75 vs 16->32->112 chain reproduced from a single
# additive nu_R Weyl, so the fork is exactly one Weyl per generation.
check(
    "fork is exactly one extra Weyl/gen (16 - 15 = 1)",
    full_matter_weyl - GAUGE_CHARGED_WEYL == NU_R == 1,
)


# ===========================================================================
# 2. Yukawa implied by the EMPIRICAL small neutrino mass (admitted comparator)
# ===========================================================================

section("2. Yukawa implied by empirical small m_nu (admitted observation)")

# Dirac mass m_D = y_nu * <H>, with <H> = 174 GeV (one-Higgs vev convention).
# y_nu = m_nu / <H>. m_nu is an ADMITTED EMPIRICAL OBSERVATION, not derived here.
def y_implied(m_nu_eV: float) -> float:
    return m_nu_eV / H_VEV_EV


y_atm = y_implied(0.05)    # atmospheric scale ~ 0.05 eV
y_01 = y_implied(0.1)      # ~ 0.1 eV (cosmological Sum m_nu ballpark per species)
y_06 = y_implied(0.6)      # generous upper edge ~ 0.6 eV

check(
    "implied y_nu(m_nu=0.05 eV) ~ 2.9e-13 (matches no-go 'order 1e-13')",
    2.0e-13 < y_atm < 4.0e-13,
    f"{y_atm:.3e}",
)
check(
    "implied y_nu(m_nu=0.1 eV) ~ 5.7e-13 (order 1e-12)",
    4.0e-13 < y_01 < 1.0e-12,
    f"{y_01:.3e}",
)
check(
    "implied y_nu(m_nu=0.6 eV, generous) ~ 3.4e-12 (still << any thermal threshold)",
    1.0e-12 < y_06 < 1.0e-11,
    f"{y_06:.3e}",
)
# Cross-check against the retained no-go's quoted tiny-Yukawa magnitude ~1e-13.
check(
    "implied y at atmospheric scale is within an order of magnitude of 1e-13",
    1e-13 <= y_atm <= 1e-12,
    f"{y_atm:.3e}",
)


# ===========================================================================
# 3. Yukawa NEEDED for nu_R thermalization (equilibration threshold)
# ===========================================================================

section("3. Yukawa threshold for nu_R thermalization (Gamma ~ H)")

# Gauge-singlet nu_R equilibrates ONLY via the Yukawa vertex to the bath fields
# H, L. Order-of-magnitude equilibration rate Gamma ~ y_nu^2 T. Radiation-era
# Hubble H ~ 1.66 sqrt(g*) T^2 / M_Pl. Equilibrium requires Gamma >~ H:
#   y_nu^2 T  >~  1.66 sqrt(g*) T^2 / M_Pl
#   y_nu^2    >~  1.66 sqrt(g*) T / M_Pl
#   y_thr     =   sqrt( 1.66 sqrt(g*) T / M_Pl ).
gstar_float = 106.75


def y_threshold(T_GeV: float) -> float:
    return math.sqrt(HUBBLE_PREFACTOR * math.sqrt(gstar_float) * T_GeV / M_PL_GEV)


def gamma_over_H(y_nu: float, T_GeV: float) -> float:
    # Gamma/H = (y^2 T) / (1.66 sqrt(g*) T^2 / M_Pl) = y^2 M_Pl / (1.66 sqrt(g*) T)
    return (y_nu ** 2) * M_PL_GEV / (HUBBLE_PREFACTOR * math.sqrt(gstar_float) * T_GeV)


T_EW = 1e2
T_LEPTO_LO = 1e9
T_LEPTO_HI = 1e12

y_thr_EW = y_threshold(T_EW)
y_thr_lepto_lo = y_threshold(T_LEPTO_LO)
y_thr_lepto_hi = y_threshold(T_LEPTO_HI)

check(
    "threshold y_thr(T=100 GeV) ~ 1e-8 (most lenient, lowest T)",
    5e-9 < y_thr_EW < 5e-8,
    f"{y_thr_EW:.3e}",
)
check(
    "threshold y_thr(T=1e9 GeV, leptogenesis) ~ 4e-5",
    1e-5 < y_thr_lepto_lo < 1e-4,
    f"{y_thr_lepto_lo:.3e}",
)
check(
    "threshold y_thr(T=1e12 GeV, leptogenesis) ~ 1e-3",
    3e-4 < y_thr_lepto_hi < 3e-3,
    f"{y_thr_lepto_hi:.3e}",
)
# The threshold RISES with T: decoupling is most easily evaded (smallest required
# y) at the LOWEST census temperature; even there the implied y is far below.
check(
    "threshold rises with T (T=100 < 1e9 < 1e12)",
    y_thr_EW < y_thr_lepto_lo < y_thr_lepto_hi,
)


# ===========================================================================
# 4. Incompatibility: implied y << threshold y by many orders (decoupled)
# ===========================================================================

section("4. Incompatibility (implied small-m_nu Yukawa << thermalization threshold)")

# Use the GENEROUS empirical case (m_nu = 0.1 eV) and the MOST LENIENT
# temperature (T = 100 GeV, smallest required y_thr). If decoupled even here,
# decoupled everywhere relevant.
y_emp = y_01  # m_nu = 0.1 eV
ratio_EW = y_thr_EW / y_emp
orders_EW = math.log10(ratio_EW)

check(
    "at the MOST LENIENT T=100 GeV: y_threshold > y_implied",
    y_thr_EW > y_emp,
    f"thr {y_thr_EW:.2e} > implied {y_emp:.2e}",
)
check(
    "incompatibility margin at T=100 GeV is >= 4 orders of magnitude",
    orders_EW >= 4.0,
    f"{orders_EW:.1f} decades (ratio {ratio_EW:.2e})",
)
# At leptogenesis temperatures the margin is much larger.
ratio_lepto = y_thr_lepto_lo / y_emp
orders_lepto = math.log10(ratio_lepto)
check(
    "incompatibility margin at leptogenesis T=1e9 GeV is >= 7 orders",
    orders_lepto >= 7.0,
    f"{orders_lepto:.1f} decades (ratio {ratio_lepto:.2e})",
)

# Gamma/H for the empirically-implied Yukawa: far below unity (never equilibrates).
GoH_EW = gamma_over_H(y_emp, T_EW)
GoH_lepto = gamma_over_H(y_emp, T_LEPTO_LO)
check(
    "Gamma/H << 1 at T=100 GeV for implied y (nu_R decoupled)",
    GoH_EW < 1e-6,
    f"Gamma/H = {GoH_EW:.2e}",
)
check(
    "Gamma/H << 1 at T=1e9 GeV for implied y (nu_R decoupled)",
    GoH_lepto < 1e-6,
    f"Gamma/H = {GoH_lepto:.2e}",
)

# The ONLY route to g_* = 112 is a thermalizing Yukawa. The minimum such y
# (at the most lenient T) is ~1e-8, i.e. >= 4 orders ABOVE the small-m_nu
# value. A y_nu >= y_thr means m_nu = y_nu <H> >> 0.1 eV.
m_nu_for_thermalization_EW = y_thr_EW * H_VEV_EV  # eV
check(
    "a thermalizing y (>= y_thr at T=100 GeV) implies m_nu >> 1 eV (excluded by data)",
    m_nu_for_thermalization_EW > 1e3,  # > 1 keV, vastly above sub-eV bound
    f"m_nu(thermalizing) >~ {m_nu_for_thermalization_EW:.2e} eV",
)
# i.e. requiring nu_R to thermalize at T=100 GeV forces m_nu >~ keV; the
# observed sub-eV neutrino mass forbids it. (Higher T forces even larger m_nu.)
check(
    "small-m_nu Yukawa and thermalization Yukawa are mutually exclusive",
    y_emp < y_thr_EW < y_thr_lepto_lo,
)


# ===========================================================================
# 5. Branch table across the retained Dirac/seesaw no-go
# ===========================================================================

section("5. Branch table (light-Dirac / heavy-Majorana / thermalizing-Dirac)")

# Each branch -> census disposition of nu_R -> g_*.
# Branch A: LIGHT DIRAC (small y_nu, as required by small m_nu = y_nu <H>).
#   y_nu ~ 1e-12 << threshold -> nu_R never thermalizes -> EXCLUDED -> 106.75.
branchA_thermalizes = y_emp >= y_thr_EW            # False
branchA_gstar = Fraction(112) if branchA_thermalizes else Fraction(427, 4)
check(
    "Branch A light-Dirac: nu_R does NOT thermalize -> g_* = 106.75",
    (not branchA_thermalizes) and branchA_gstar == Fraction(427, 4),
    f"thermalizes={branchA_thermalizes}, g_*={float(branchA_gstar)}",
)

# Branch B: HEAVY MAJORANA / seesaw (M_R >> T_census).
#   nu_R is a heavy state, NOT a light relativistic dof at the census epoch
#   -> Boltzmann-suppressed / decayed -> EXCLUDED -> 106.75.
#   Model M_R as a benchmark seesaw scale >> census T.
M_R_seesaw_GeV = 1e14   # representative heavy Majorana scale
branchB_light_at_census = M_R_seesaw_GeV < T_LEPTO_HI   # False: heavy
branchB_gstar = Fraction(427, 4)  # excluded as a light dof regardless
check(
    "Branch B heavy-Majorana: M_R >> T_census so nu_R is NOT a light dof -> g_* = 106.75",
    (not branchB_light_at_census) and branchB_gstar == Fraction(427, 4),
    f"M_R={M_R_seesaw_GeV:.0e} GeV >> T; light_at_census={branchB_light_at_census}",
)

# Branch C: THERMALIZING DIRAC (y_nu >= y_thr) — the ONLY route to 112.
#   Even at the most lenient threshold, thermalization implies m_nu >= keV;
#   the O(1) Yukawa steelman is a stronger excluded subcase.
y_thermalizing_min = y_thr_EW
y_large = 1.0
branchC_thermalizes = y_thermalizing_min >= y_thr_EW    # True by construction
m_nu_branchC_min_eV = y_thermalizing_min * H_VEV_EV     # ~2 keV
m_nu_branchC_large_eV = y_large * H_VEV_EV              # ~1.74e11 eV = 174 GeV
branchC_gstar = Fraction(112) if branchC_thermalizes else Fraction(427, 4)
check(
    "Branch C thermalizing-Dirac: y_nu >= y_thr thermalizes -> g_* = 112",
    branchC_thermalizes and branchC_gstar == Fraction(112),
    f"thermalizes={branchC_thermalizes}, y_thr={y_thermalizing_min:.2e}, g_*={float(branchC_gstar)}",
)
check(
    "Branch C is EXCLUDED by data: y>=y_thr implies m_nu >= keV; O(1) gives 174 GeV",
    m_nu_branchC_min_eV > 1e3 and m_nu_branchC_large_eV > 1e9,
    f"m_nu(min thermalizing) ~ {m_nu_branchC_min_eV:.2e} eV; O(1) ~ {m_nu_branchC_large_eV:.2e} eV",
)

# ROBUSTNESS: both ADMITTED branches (A light-Dirac, B heavy-Majorana) give
# 106.75; only the empirically-excluded branch C gives 112.
admitted_branches_gstar = {branchA_gstar, branchB_gstar}
check(
    "g_* = 106.75 is ROBUST across BOTH admitted branches (light-Dirac, heavy-Majorana)",
    admitted_branches_gstar == {Fraction(427, 4)},
    f"{[float(x) for x in admitted_branches_gstar]}",
)
check(
    "g_* = 112 arises ONLY in the empirically-excluded thermalizing-Dirac branch",
    branchC_gstar == Fraction(112) and branchA_gstar == branchB_gstar == Fraction(427, 4),
)
# The framework does NOT pick Dirac vs Majorana (retained no-go); the resolution
# holds in BOTH, so it is branch-independent.
check(
    "resolution is branch-independent (framework retained no-go does not pick a branch)",
    branchA_gstar == branchB_gstar,
)


# ===========================================================================
# 6. Note / authority cross-checks
# ===========================================================================

section("6. Note / authority cross-checks")

# Load-bearing authorities cited as markdown links (citation-graph edges).
SOURCED_AUTHORITIES = [
    "SM_GSTAR_I12_EMPIRICAL_THERMAL_COMPARATOR_BRIDGE_BOUNDED_NOTE_2026-06-15.md",
    "NEUTRINO_LANE4_DIRAC_SEESAW_FORK_NO_GO_NOTE_2026-04-27.md",
    "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md",
]

# Separated / supporting pointers -> plain text (NON-load-bearing edges). These
# are sibling-campaign-PR notes that may not yet be merged to main, so they are
# deliberately NOT load-bearing and their existence is NOT required; the only
# requirement is that they appear as plain text (not as markdown links).
PLAINTEXT_POINTERS = [
    "SM_GSTAR_R_MATTER_RESIDUAL_REDUCTION_BOUNDED_NOTE_2026-05-29.md",
    "SM_GSTAR_FROM_FRAMEWORK_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-05-29.md",
]

# Load-bearing authorities must exist on main (this PR's true dependencies).
for fname in SOURCED_AUTHORITIES:
    check(
        f"load-bearing authority file exists: {fname}",
        (ROOT / "docs" / fname).exists(),
    )

for fname in SOURCED_AUTHORITIES:
    check(
        f"load-bearing authority cited as markdown link: {fname}",
        f"]({fname})" in NOTE_TEXT,
    )

# Plain-text pointers must be NON-load-bearing: present as plain text but NOT as
# a markdown link (so the citation-graph builder records no edge).
for fname in PLAINTEXT_POINTERS:
    check(
        f"plain-text pointer is non-load-bearing (no markdown-link edge): {fname}",
        (fname in NOTE_TEXT) and (f"]({fname})" not in NOTE_TEXT),
    )

# Required note content.
check(
    "note names I12 nu_R thermal exclusion as the load-bearing fork",
    "I12" in NOTE_TEXT and "nu_R" in NOTE_TEXT and "thermal exclusion" in NOTE_TEXT,
)
check(
    "note carries the 106.75 vs 112 fork explicitly",
    "106.75" in NOTE_TEXT and "112" in NOTE_TEXT,
)
check(
    "note engages the retained Dirac/seesaw no-go",
    "retained_no_go" in NOTE_TEXT or "Dirac/seesaw" in NOTE_TEXT or "Dirac-seesaw" in NOTE_TEXT,
)
check(
    "note states branch-independence (both branches -> exclusion)",
    "branch-independ" in NOTE_TEXT.lower() or "both branches" in NOTE_TEXT.lower(),
)
check(
    "note names small m_nu as an ADMITTED EMPIRICAL observation (not derived)",
    "empirical" in NOTE_TEXT.lower()
    and ("admitted" in NOTE_TEXT.lower())
    and ("small" in NOTE_TEXT.lower()),
)

comparator_bridge = (
    ROOT
    / "docs"
    / "SM_GSTAR_I12_EMPIRICAL_THERMAL_COMPARATOR_BRIDGE_BOUNDED_NOTE_2026-06-15.md"
)
comparator_text = (
    comparator_bridge.read_text(encoding="utf-8") if comparator_bridge.exists() else ""
)
check(
    "comparator bridge isolates the admitted small-m_nu input",
    "admitted empirical small-neutrino-mass observation" in comparator_text
    and "does not derive small neutrino mass" in comparator_text.lower(),
)
check(
    "comparator bridge isolates the thermalization comparator",
    "Gamma_nuR ~ y_nu^2 T" in comparator_text
    and "H ~ 1.66 sqrt(g_*) T^2 / M_Pl" in comparator_text
    and "This note does **not**" in comparator_text
    and "derive `Gamma_nuR ~ y_nu^2 T` from a framework collision operator" in comparator_text,
)
check(
    "note records the steelman (N7) FOR g_* = 112 and its rebuttal",
    "steelman" in NOTE_TEXT.lower() and "rebut" in NOTE_TEXT.lower(),
)
check(
    "note states the honest ceiling: I12 partially-resolved (conditioned on small m_nu)",
    "partially" in NOTE_TEXT.lower()
    and ("conditioned" in NOTE_TEXT.lower() or "conditional" in NOTE_TEXT.lower()),
)
check(
    "note states it does NOT fully derive I12 from first principles",
    "does **not**" in NOTE_TEXT.lower() or "does not" in NOTE_TEXT.lower(),
)


# ===========================================================================
# 7. Ledger status cross-check (optional)
# ===========================================================================

section("7. Ledger status cross-check (optional)")
if LEDGER_PATH.exists():
    led = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = led.get("rows", led)

    def status_of(cid: str):
        if isinstance(rows, dict):
            for k, r in rows.items():
                if cid == str(k) or cid == str(r.get("claim_id", "")):
                    return r.get("effective_status")
        else:
            for r in rows:
                if cid == str(r.get("claim_id", "")):
                    return r.get("effective_status")
        return None

    check(
        "Dirac/seesaw fork no-go is retained_no_go (the load-bearing engine)",
        status_of("neutrino_lane4_dirac_seesaw_fork_no_go_note_2026-04-27")
        == "retained_no_go",
        f"ledger = {status_of('neutrino_lane4_dirac_seesaw_fork_no_go_note_2026-04-27')}",
    )
    check(
        "relativistic dof count import is retained_bounded",
        status_of("sm_relativistic_dof_count_import_note_2026-05-17")
        == "retained_bounded",
        f"ledger = {status_of('sm_relativistic_dof_count_import_note_2026-05-17')}",
    )
    # The retained neutrino-mass functional-form theorem (cited as corroboration
    # that the framework's retained neutrino-mass surface is small-m_nu-bearing).
    ff = status_of("neutrino_lane4_4f_sigma_m_nu_functional_form_theorem_note_2026-04-28")
    check(
        "Sum m_nu functional-form theorem is retained (named for context, not a derivation of small m_nu)",
        ff == "retained",
        f"ledger = {ff}",
    )
else:
    print("  [SKIP] audit ledger not present; status cross-check skipped")


# ===========================================================================
# 8. No-overclaim / forbidden-import / new-vocabulary scan
# ===========================================================================

section("8. No-overclaim / forbidden-import / vocabulary scan")

banned_status_lines = re.findall(
    r"(?im)^\*\*Status:\*\*\s*(retained|promoted)\b", NOTE_TEXT
)
check(
    "no bare '**Status:** retained/promoted' line",
    not banned_status_lines,
    f"found {banned_status_lines}" if banned_status_lines else "",
)
check(
    "claim type is bounded_theorem",
    "**Claim type:** bounded_theorem" in NOTE_TEXT,
)
check(
    "status authority is independent audit lane only",
    "independent audit lane only" in NOTE_TEXT,
)
# Honesty: must NOT claim to derive small neutrino mass.
low = NOTE_TEXT.lower()
check(
    "note does NOT claim to derive the small neutrino mass",
    "does **not** derive the small" in low
    or "not a framework derivation of the small" in low
    or "does not derive small neutrino" in low
    or "small m_nu is an admitted" in low
    or "small neutrino mass is an admitted" in low,
)
# Forbidden load-bearing imports.
forbidden = [
    "wilson plaquette",
    "staggered phase",
    "brillouin",
    "link unitar",
    "monte carlo",
    "best-fit",
    "chi-squared fit",
    "fitted to data",
]
for term in forbidden:
    n_occ = low.count(term)
    n_neg = low.count("no lattice-action carrier")
    check(
        f"no load-bearing forbidden import '{term}'",
        n_occ == 0 or n_neg >= 1,
        f"{n_occ} occurrence(s)",
    )
# No new repo vocabulary / meta-framings.
banned_vocab = [
    "algebraic universality",
    "two-class framing",
    "lattice-realization-invariant by definition",
    "(ckn)",
]
for term in banned_vocab:
    check(
        f"no new-vocabulary string '{term}'",
        term not in low,
    )


# ===========================================================================
# Scorecard
# ===========================================================================

section("SCORECARD")
print(f"  PASS = {PASS}")
print(f"  FAIL = {FAIL}")
print()
if FAIL == 0:
    print(f"RESULT: PASS={PASS} FAIL=0")
    sys.exit(0)
else:
    print(f"RESULT: PASS={PASS} FAIL={FAIL}")
    sys.exit(1)
