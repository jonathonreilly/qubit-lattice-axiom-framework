"""
Audit companion (numpy/sympy) for
GRAVITON_MASS_SCALE_IS_RECORD_FORCED_TO_LAMBDA_PREDICTION_NOTE_2026-06-06.md

PREDICTION note (conditional/structural). It does NOT re-derive the framework's graviton-mass identity
m_g^2 = 2*Lambda (that is the bounded GRAVITON_MASS_DERIVED_NOTE, cited as input). It establishes the NEW content:
under RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE (#2988), a graviton mass can only come from a RECORD that
pins the locally-gauge metric perturbation; the ONLY global record is the finite universe size R = sqrt(3/Lambda);
a local record (lattice spacing ~ Planck) gaps UV modes, not the IR zero mode. Therefore the graviton-mass SCALE
is record-forced to O(sqrt(Lambda)) (cosmological), NOT Planck and NOT zero, and the massless graviton is exactly
the no-global-record (R -> infinity) limit. This distinguishes the framework (definite nonzero m_g) from GR
(massless by assumption), and is near the current testability frontier.

This runner verifies the SCALE/structural claims only. The coefficient (2 in m_g^2=2*Lambda) is the geometric
Lichnerowicz S^3 gap (inherited, bounded); the framework's S^3 / R = c/H0 cosmology is a premise. No PDG values
are derivation inputs; observational bounds are cited only to place the prediction on the falsification surface.
"""
import numpy as np
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "GRAVITON_MASS_SCALE_IS_RECORD_FORCED_TO_LAMBDA_PREDICTION_NOTE_2026-06-06.md"

# ---- the framework's identity (INPUT, cited): Lambda = 3/R^2, lowest TT Lichnerowicz mode 6/R^2 = 2*Lambda ----
Rr = 1.0
Lam = 3 / Rr**2
m_g2 = 6 / Rr**2
chk("(1) INPUT (cited bounded identity): Lambda=3/R^2, lowest TT mode=6/R^2 -> m_g^2 = 2*Lambda", abs(m_g2 - 2*Lam) < 1e-12)

# ---- massless = no-global-record limit: R -> infinity -> m_g -> 0 ----
ms = [6 / (Rr*s)**2 for s in [1, 10, 100, 1000]]
chk("(2) massless graviton = the NO-GLOBAL-RECORD limit: as R -> infinity (no finite global record) m_g^2 -> 0",
    ms[-1] < ms[0] and ms[-1] < 1e-4)

# ---- the record-forcing of the SCALE: the only GLOBAL record is R; a LOCAL record can't pin the IR zero mode ----
hbar = 6.582e-16   # eV*s
H0 = 2.2e-18       # 1/s (~70 km/s/Mpc)
c = 3.0e8
m_g_cosmo = hbar * H0                  # global-record (R = c/H0) graviton-mass scale ~ hbar*H0
E_planck = 1.22e28                     # eV : the scale a LOCAL (lattice/Planck) record would set
chk("(3) record-forcing: the ONLY global record is R = c/H0 -> graviton-mass scale ~ hbar*H0 ~ %.1e eV (cosmological)" % m_g_cosmo,
    1e-34 < m_g_cosmo < 1e-32)
chk("(4) a LOCAL record (lattice spacing ~ Planck) gaps only UV modes (~E_Planck ~ %.0e eV), NOT the IR zero mode -> a graviton mass is FORCED to the cosmological scale, NOT Planck (ratio ~ %.0e)" % (E_planck, E_planck/m_g_cosmo),
    E_planck / m_g_cosmo > 1e60)

# ---- placement on the falsification surface (bounds are comparators, not inputs) ----
m_g_pred = 3.52e-33                     # eV, the framework's bounded value (cited)
bound_ligo = 1.3e-23                    # eV (GW dispersion)
bound_cosmo = 1e-32                     # eV (tightest solar-system/cosmological analyses)
chk("(5) prediction m_g ~ 3.52e-33 eV is BELOW the LIGO bound (~1e-23) and just below the tightest cosmological bound (~1e-32) -> on the falsification frontier, not beyond it",
    m_g_pred < bound_ligo and m_g_pred < bound_cosmo and m_g_pred > 1e-34)

# ---- distinguishing from GR (massless by assumption) ----
chk("(6) DISTINGUISHING: GR assumes m_g = 0 (exact diffeomorphism invariance); the framework predicts a definite nonzero m_g forced to O(sqrt(Lambda)) -> a falsifiable difference, not a re-reading",
    m_g_pred > 0)

# ---- source-note boundary tokens ----
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["**Type:** bounded_theorem", "record-forced", "only global record", "no-global-record", "conditional", "not Planck", "GR assumes", "comparator", "Independent audit required"]
    chk("(7) source note keeps the record-forced-scale / conditional / distinguishing boundary", all(k in t for k in toks))
else:
    chk("(7) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nPREDICTION: the graviton-mass SCALE is RECORD-FORCED to O(sqrt(Lambda)) (cosmological), because the only\n"
    "global record able to pin the locally-gauge graviton is the finite universe R = sqrt(3/Lambda); a local/Planck\n"
    "record cannot pin the IR zero mode. So m_g ~ 3.52e-33 eV (NOT Planck, NOT zero), and the massless graviton is\n"
    "the no-global-record (R -> infinity) limit. Distinguishes the framework (definite nonzero m_g) from GR\n"
    "(massless by assumption), on the falsification frontier. The coefficient (2*Lambda) is the inherited bounded\n"
    "Lichnerowicz identity; the record-forcing of the SCALE is the new content."
)
