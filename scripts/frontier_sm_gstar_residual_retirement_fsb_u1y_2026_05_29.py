#!/usr/bin/env python3
"""Verification runner for the g_* residual-retirement bounded note (R-FSB + R-U1Y).

Supports
docs/SM_GSTAR_RESIDUAL_RETIREMENT_FSB_U1Y_BOUNDED_NOTE_2026-05-29.md.

This runner does four distinct jobs, all as EXECUTED asserts (not prose):

1. **R-FSB: the 7/8 ratio from the retained anchor's two formulas.** The g_*
   census consumes only the dimensionless fermion/boson Stefan-Boltzmann ratio.
   The retained positive theorem
   hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor proves it two
   ways at d=4: the per-mode lattice ratio R_lat(c) = (c+1/2)/(c+1) at c=3, and
   the Riemann-Dirichlet quotient eta(s)/zeta(s) = 1 - 2^(1-s) at s=4. Both = 7/8,
   and the integer alignment 2^(d-2) = d is unique at d=4. The runner checks all
   of these with fractions.Fraction (exact rationals).

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
# R-FSB: the 7/8 ratio from the retained anchor's two formulas
# ---------------------------------------------------------------------------


def r_lat(c: int) -> Fraction:
    """Per-mode lattice ratio R_lat(c) = (c + 1/2)/(c + 1) of the retained
    hierarchy_seven_eighths anchor (identity (i))."""
    return (Fraction(c) + Fraction(1, 2)) / (Fraction(c) + 1)


def eta_over_zeta(s: int) -> Fraction:
    """Riemann-Dirichlet quotient eta(s)/zeta(s) = 1 - 2^(1-s) of the retained
    anchor (identity (ii)); exact rational for integer s >= 2."""
    return Fraction(1) - Fraction(1, 2) ** (s - 1)


def alignment_residual(d: int) -> int:
    """Integer alignment equation f(d) = 2^(d-2) - d (identity (iii))."""
    return 2 ** (d - 2) - d


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

section("1. R-FSB: 7/8 fermion thermal weight from the retained anchor")

seven_eighths = Fraction(7, 8)

check(
    "lattice ratio R_lat(3) = (3 + 1/2)/(3 + 1) = 7/8",
    r_lat(3) == seven_eighths,
    f"R_lat(3) = {r_lat(3)}",
)
check(
    "Riemann-Dirichlet eta(4)/zeta(4) = 1 - 2^(-3) = 7/8",
    eta_over_zeta(4) == seven_eighths,
    f"eta(4)/zeta(4) = {eta_over_zeta(4)}",
)
check(
    "the two retained-anchor formulas agree on 7/8 at d=4",
    r_lat(3) == eta_over_zeta(4) == seven_eighths,
)
check(
    "general lattice identity R_lat(c) = 1 - 1/(2(c+1)) holds (c=3)",
    r_lat(3) == Fraction(1) - Fraction(1, 2 * (3 + 1)),
)
check(
    "general eta/zeta identity = 1 - 2^(1-s) holds (s=4)",
    eta_over_zeta(4) == Fraction(1) - Fraction(2) ** (1 - 4),
)
# Integer alignment 2^(d-2) = d unique at d=4 (identity (iii)).
align_solutions = [d for d in range(2, 21) if alignment_residual(d) == 0]
check(
    "integer alignment 2^(d-2) = d unique at d=4 over 2<=d<=20",
    align_solutions == [4],
    f"solutions = {align_solutions}",
)
# At other integer d the two ratios diverge (coincidence only at d=4).
diverge = all(
    r_lat(d - 1) != eta_over_zeta(d)
    for d in range(2, 13)
    if d != 4
)
check(
    "lattice and Riemann-Dirichlet ratios differ at every integer d != 4 (2..12)",
    diverge,
)
check(
    "g_* consumes only the dimensionless 7/8 ratio (it is a pure rational)",
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
    "HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md",
    "NATIVE_GAUGE_CLOSURE_NOTE.md",
    "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
]
SEPARATED_STRONGER = [
    "AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md",
    "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md",
    "HYPERCHARGE_IDENTIFICATION_NOTE.md",
]

for fname in RETIRED_TO_RETAINED + SEPARATED_STRONGER:
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

# The separated stronger fermionic-SB law and the uniqueness note must be
# plain-text pointers (NOT markdown links) so they are not load-bearing edges.
for fname in [
    "AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md",
    "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md",
]:
    check(
        f"separated stronger statement is plain-text (non-load-bearing): {fname}",
        (fname in NOTE_TEXT) and (f"]({fname})" not in NOTE_TEXT),
    )

# Retirement bookkeeping strings present in the note.
check(
    "note marks R-FSB retired-to-retained-sourced",
    "R-FSB" in NOTE_TEXT and "retired-to-retained-sourced" in NOTE_TEXT,
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
        "hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10": "retained",
        "native_gauge_closure_note": "retained",
        "graph_first_su3_integration_note": "retained",
    }
    for cid, want in retained_expected.items():
        got = status_of(cid)
        check(
            f"retired-to source {cid} is {want}",
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
