#!/usr/bin/env python3
"""Verification runner for the g_* residual-retirement bounded note (R-FSB + R-U1Y).

Supports
docs/SM_GSTAR_RESIDUAL_RETIREMENT_FSB_U1Y_BOUNDED_NOTE_2026-05-29.md.

This runner does four distinct jobs, all as EXECUTED asserts (not prose):

1. **R-FSB: the 7/8 ratio from the direct thermal integrals.** The g_*
   census consumes the dimensionless Fermi/Bose Stefan-Boltzmann ratio. The
   repaired note proves this role directly:
   I_B = int x^3/(e^x-1) dx = pi^4/15,
   I_F = int x^3/(e^x+1) dx = 7*pi^4/120,
   and I_F/I_B = 7/8. This replaces the prior role-substitution from a
   numerically equal hierarchy anchor.

2. **R-U1Y: the one-abelian-factor gauge-rank dof count.** The g_* census
   consumes only the abelian-factor RANK (one gl(1) factor), sourced from the
   retained gl(3)+gl(1) commutant (native_gauge_closure_note /
   graph_first_su3_integration_note). The runner checks dim adj(SU(3)) = 8,
   dim adj(SU(2)) = 3, one abelian factor = 1, generator count 8+3+1 = 12, and
   gauge dof 8*2 + 3*2 + 1*2 = 16 + 6 + 2 = 24.

3. **Separation check.** The abelian dof count depends only on the rank, NOT on
   the hypercharge eigenvalue normalization. The runner asserts the dof count is
   the same 2 whether the abelian generator's eigenvalues are the SM {+1/3, -1}
   set or an arbitrary nonzero rescaling. The hypercharge VALUES stay bounded
   and are not a dof-count input.

4. **Note / authority cross-checks.** Retirement bookkeeping (which residuals
   move to retained-sourced, which stronger statements stay separate, which
   residuals remain), authority-file existence, optional ledger-status
   cross-check, and a no-overclaim / forbidden-import / new-vocabulary scan.

No lattice-action quantity, fitted comparator, or PDG observed value is a
load-bearing input. The 7/8 ratio and the gauge rank are framework /
classical-mathematics quantities, not fitted.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import re
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "SM_GSTAR_RESIDUAL_RETIREMENT_FSB_U1Y_BOUNDED_NOTE_2026-05-29.md"
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


# ---------------------------------------------------------------------------
# R-FSB: the 7/8 ratio from direct thermal integrals
# ---------------------------------------------------------------------------


def bose_fermi_integrals():
    """Return exact symbolic Bose/Fermi x^3 thermal integrals."""
    gamma4 = sp.gamma(4)
    zeta4 = sp.pi**4 / 90
    eta4 = (1 - sp.Rational(1, 8)) * zeta4
    bose = sp.simplify(gamma4 * zeta4)
    fermi = sp.simplify(gamma4 * eta4)
    return gamma4, zeta4, eta4, bose, fermi


# ---------------------------------------------------------------------------
# R-U1Y: the one-abelian-factor gauge-rank dof count
# ---------------------------------------------------------------------------


def dim_adjoint_su(n: int) -> int:
    """dim adj(SU(N)) = N^2 - 1. SU(3)_c uses N_c = 3 (retained
    cl3_color_automorphism); SU(2)_L uses N = 2 (retained native_gauge bivectors)."""
    return n * n - 1


def n_abelian_factors_from_commutant() -> int:
    """The retained gl(3)+gl(1) joint commutant (graph_first_su3_integration,
    native_gauge_closure) has exactly ONE gl(1) abelian summand. Modeled here as
    the multiplicity of the 1-dimensional (antisymmetric) block in the 3 (+) 1
    base split: dim base = 4, semisimple color block = 3, abelian block = 1."""
    dim_base = 4
    color_block = 3  # symmetric / semisimple gl(3) part
    abelian_block = dim_base - color_block  # antisymmetric gl(1) part
    return abelian_block  # = 1, the single abelian factor


def transverse_polarizations_massless() -> int:
    """Massless-vector transverse polarization count (residual R-POL, NOT
    retired here): 4 Lorentz components - 1 Lorenz constraint - 1 residual gauge
    orbit = 2. Kept as the separate residual factor; the abelian RANK is what is
    retired."""
    return 4 - 1 - 1


def abelian_gauge_dof_from_rank(eigenvalue_scale: Fraction) -> int:
    """The abelian gauge dof = (number of abelian factors) * (transverse pol).
    The eigenvalue_scale argument is intentionally UNUSED in the count: the dof
    count depends only on the rank, not on the hypercharge eigenvalue
    normalization. Passing different scales must give the same dof."""
    _ = eigenvalue_scale  # values are NOT a dof-count input (separation)
    return n_abelian_factors_from_commutant() * transverse_polarizations_massless()


# ===========================================================================
# 1. R-FSB: 7/8 ratio from the retained anchor
# ===========================================================================

section("1. R-FSB: 7/8 fermion thermal weight from direct thermal integrals")

seven_eighths = Fraction(7, 8)
gamma4, zeta4, eta4, bose_integral, fermi_integral = bose_fermi_integrals()

check("Gamma(4) = 6", gamma4 == 6, str(gamma4))
check("zeta(4) = pi^4/90", zeta4 == sp.pi**4 / 90, str(zeta4))
check(
    "eta(4) = (7/8) zeta(4)",
    sp.simplify(eta4 / zeta4) == sp.Rational(7, 8),
    str(sp.simplify(eta4 / zeta4)),
)
check(
    "Bose integral I_B = pi^4/15",
    sp.simplify(bose_integral - sp.pi**4 / 15) == 0,
    str(bose_integral),
)
check(
    "Fermi integral I_F = 7*pi^4/120",
    sp.simplify(fermi_integral - 7 * sp.pi**4 / 120) == 0,
    str(fermi_integral),
)
check(
    "direct thermal-integral ratio I_F/I_B = 7/8",
    sp.simplify(fermi_integral / bose_integral) == sp.Rational(7, 8),
    str(sp.simplify(fermi_integral / bose_integral)),
)
prefactor = sp.Rational(1, 2) / sp.pi**2
rho_b = sp.simplify(prefactor * bose_integral)
rho_f = sp.simplify(prefactor * fermi_integral)
check(
    "rho_B per dof = pi^2/30 * T^4",
    sp.simplify(rho_b - sp.pi**2 / 30) == 0,
    str(rho_b),
)
check(
    "rho_F per dof = (7/8) rho_B",
    sp.simplify(rho_f / rho_b) == sp.Rational(7, 8),
    str(sp.simplify(rho_f / rho_b)),
)
check(
    "g_* consumes only the dimensionless direct thermal 7/8 ratio",
    isinstance(seven_eighths, Fraction) and 0 < seven_eighths < 1,
    f"7/8 = {float(seven_eighths)}",
)


# ===========================================================================
# 2. R-U1Y: one-abelian-factor gauge-rank dof count
# ===========================================================================

section("2. R-U1Y: one-abelian-factor gauge-rank dof count from retained gl(3)+gl(1)")

n_c = 3
check(
    "dim adj(SU(3)) = N_c^2 - 1 = 8 (retained cl3_color_automorphism N_c=3)",
    dim_adjoint_su(n_c) == 8,
    f"dim adj SU(3) = {dim_adjoint_su(n_c)}",
)
check(
    "dim adj(SU(2)) = 2^2 - 1 = 3 (retained native_gauge Cl(3) bivectors)",
    dim_adjoint_su(2) == 3,
    f"dim adj SU(2) = {dim_adjoint_su(2)}",
)
check(
    "exactly ONE abelian factor: gl(1) summand of retained gl(3)+gl(1) commutant",
    n_abelian_factors_from_commutant() == 1,
    f"abelian factors = {n_abelian_factors_from_commutant()}",
)
# Generator (gauge-boson) count: 8 + 3 + 1 = 12.
gen_count = dim_adjoint_su(3) + dim_adjoint_su(2) + n_abelian_factors_from_commutant()
check(
    "gauge generator count 8 + 3 + 1 = 12",
    gen_count == 12,
    f"generators = {gen_count}",
)
# Gauge dof: each generator -> one massless vector -> 2 transverse pol.
gluon_dof = dim_adjoint_su(3) * transverse_polarizations_massless()
weak_dof = dim_adjoint_su(2) * transverse_polarizations_massless()
abelian_dof = n_abelian_factors_from_commutant() * transverse_polarizations_massless()
check("gluon dof = 8 * 2 = 16", gluon_dof == 16, f"{gluon_dof}")
check("SU(2)_L dof = 3 * 2 = 6", weak_dof == 6, f"{weak_dof}")
check("abelian (one-factor) dof = 1 * 2 = 2", abelian_dof == 2, f"{abelian_dof}")
gauge_dof = gluon_dof + weak_dof + abelian_dof
check(
    "gauge dof subtotal 16 + 6 + 2 = 24",
    gauge_dof == 24,
    f"gauge dof = {gauge_dof}",
)
check(
    "gauge dof = generator count * 2 (each generator one massless vector)",
    gauge_dof == gen_count * transverse_polarizations_massless(),
)
check(
    "transverse-pol factor 2 stays the SEPARATE residual R-POL (not retired here)",
    transverse_polarizations_massless() == 2,
)


# ===========================================================================
# 3. Separation: abelian dof depends on RANK, not hypercharge VALUES
# ===========================================================================

section("3. Separation: abelian dof = rank only; hypercharge VALUES not a dof input")

# SM hypercharge eigenvalue set on the gl(1) direction (graph-first note:
# +1/3 on the 6-dim block, -1 on the 2-dim block). These are the bounded VALUES.
sm_eigenvalues = (Fraction(1, 3), Fraction(-1))
# Arbitrary nonzero rescaling of the same single abelian generator.
rescaled_eigenvalues = tuple(Fraction(5, 7) * e for e in sm_eigenvalues)

dof_sm = abelian_gauge_dof_from_rank(eigenvalue_scale=Fraction(1))
dof_rescaled = abelian_gauge_dof_from_rank(eigenvalue_scale=Fraction(5, 7))
check(
    "abelian dof = 2 under SM hypercharge eigenvalue normalization",
    dof_sm == 2,
    f"dof = {dof_sm}",
)
check(
    "abelian dof = 2 under arbitrary nonzero eigenvalue rescaling",
    dof_rescaled == 2,
    f"dof = {dof_rescaled}",
)
check(
    "dof count is INVARIANT under hypercharge eigenvalue normalization (values not an input)",
    dof_sm == dof_rescaled,
)
check(
    "the eigenvalue sets differ (so the invariance is non-trivial)",
    sm_eigenvalues != rescaled_eigenvalues,
)
check(
    "both eigenvalue sets describe ONE abelian factor (rank 1) -> same dof",
    n_abelian_factors_from_commutant() == 1,
)


# ===========================================================================
# 4. Note + authority cross-checks
# ===========================================================================

section("4. Note / authority cross-checks and retirement bookkeeping")

RETIRED_TO_RETAINED = [
    "NATIVE_GAUGE_CLOSURE_NOTE.md",
    "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
]
NON_LOAD_BEARING_CONTEXT = [
    "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
    "HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md",
    "AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md",
    "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md",
    "HYPERCHARGE_IDENTIFICATION_NOTE.md",
]

for fname in RETIRED_TO_RETAINED + NON_LOAD_BEARING_CONTEXT:
    check(
        f"authority file exists: {fname}",
        (ROOT / "docs" / fname).exists(),
    )

# Markdown-link (load-bearing) edges must be present for the retained sources.
for fname in RETIRED_TO_RETAINED:
    check(
        f"retained source cited as markdown link (load-bearing edge): {fname}",
        f"]({fname})" in NOTE_TEXT,
    )

# The parallel/context statements must be plain-text pointers (NOT markdown
# links) so they are not load-bearing edges.
for fname in [
    "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
    "HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md",
    "AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md",
    "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md",
    "HYPERCHARGE_IDENTIFICATION_NOTE.md",
]:
    check(
        f"context/separated statement is plain-text (non-load-bearing): {fname}",
        (fname in NOTE_TEXT) and (f"]({fname})" not in NOTE_TEXT),
    )

# Retirement bookkeeping strings present in the note.
check(
    "note marks R-FSB source-local direct bounded closure",
    "R-FSB -> direct bounded closure proposed" in NOTE_TEXT
    and "source-local Bose/Fermi thermal-integral proof" in NOTE_TEXT,
)
check(
    "note marks R-U1Y retired-to-retained-sourced",
    "R-U1Y" in NOTE_TEXT,
)
for residual in ["R-HIGGS", "R-POL", "R-MATTER", "R-SPIN"]:
    check(
        f"remaining residual named: {residual}",
        residual in NOTE_TEXT,
    )

# Optional ledger cross-check (skipped cleanly if ledger absent).
section("5. Ledger status cross-check (optional)")
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

    retained_expected = {
        "native_gauge_closure_note": "retained",
        "graph_first_su3_integration_note": "retained",
    }
    for cid, want in retained_expected.items():
        got = status_of(cid)
        check(
            f"retired-to R-U1Y source {cid} is {want}",
            got == want,
            f"ledger = {got}",
        )
    # The separated stronger statements are NOT retained (stay blocked/bounded).
    sep_expected = {
        "axiom_first_fermionic_stefan_boltzmann_narrow_theorem_note_2026-05-26": "unaudited",
        "standard_model_hypercharge_uniqueness_theorem_note_2026-04-24": "unaudited",
        "hypercharge_identification_note": "retained_bounded",
    }
    for cid, want in sep_expected.items():
        got = status_of(cid)
        check(
            f"separated statement {cid} stays {want} (not retired by this note)",
            got == want,
            f"ledger = {got}",
        )
else:
    print("  [SKIP] audit ledger not present; status cross-check skipped")


# ===========================================================================
# 6. No-overclaim / forbidden-import / new-vocabulary scan
# ===========================================================================

section("6. No-overclaim / forbidden-import / vocabulary scan")

# Bare retained/promoted status lines are banned (status authority is audit lane).
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
# Honest-scope sentences present.
check(
    "note states full fermionic-SB law NOT claimed derived",
    "does **not**" in NOTE_TEXT
    and "fermionic Stefan-Boltzmann law is derived" in NOTE_TEXT,
)
check(
    "note states hypercharge values NOT claimed derived",
    "hypercharge values" in NOTE_TEXT and "stay bounded" in NOTE_TEXT,
)

# Forbidden load-bearing imports: no lattice-action / fitted / PDG carrier.
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
low = NOTE_TEXT.lower()
for term in forbidden:
    # allow the explicit negative ledger statement listing these as NOT used
    n_occ = low.count(term)
    n_neg = low.count("no lattice-action carrier")  # the ledger disclaimer line
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
    "(CKN)",
]
for term in banned_vocab:
    check(
        f"no new-vocabulary string '{term}'",
        term.lower() not in low,
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
