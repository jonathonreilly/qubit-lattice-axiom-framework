r"""
Audit companion - the CKM CP phase identity delta_CKM = arctan(sqrt5) = arccos(1/sqrt6) = 65.905 deg
REDUCES to a single bridge cos^2(delta) = 1/n_quark, which is an ADMISSION (an open gate; not derivable from
{Lattice, Quantum, Record} as the framework stands). Flavor-side complement to the strong-CP theta and the
charged-lepton Koide r=1/2 admissions.

This runner is an OBSTRUCTION companion, NOT a closure. Its discipline (the #3138 lesson): it must DERIVE the
FORCED skeleton from primitives, and EXHIBIT the non-forcing of each load-bearing identification (by showing the
freedom explicitly), NEVER assert the bridge cos^2(delta)=1/n as derived. The framework's own audit lane already
marks the load-bearing carrier K_R as open_gate with its physical meaning ASSERTED, and the rho_eta_to_delta
narrow theorem already DISCLAIMS deriving the 1+5 split; this runner reproves those boundaries from primitives.

COMPUTED CORE (exact sympy):
  (A) FORCED skeleton (genuinely derived):
      (A1) cos^2(delta) = rho^2/(rho^2+eta^2) = w_A1, INDEPENDENT of the CP radius r (r cancels identically).
      (A2) the totally-symmetric ("democratic") projection weight of a single basis state in an n-state module is
           exactly 1/n: w_A1 = |<dem|e_i>|^2 = 1/n. Pure projector geometry. At n=6: w_A1=1/6 -> tan delta=sqrt5.
  (B) NON-FORCING demonstrations (these EXHIBIT the admissions by showing the free choices):
      (B1) the angle depends on WHICH symmetric-block dimension is chosen: 1+5 -> 65.9, 2+4 -> 54.7, 3+3 -> 45.
           So the "1+5" split is a CHOICE, not forced (matches the rho_eta_to_delta disclaimer).
      (B2) the COUNT is load-bearing: the naive democratic angle in 3-GENERATION space is arccos(1/sqrt3)=54.74 deg,
           which does NOT match gamma; the atlas value 65.9 needs n=6 = 2(weak)x3(color) of ONE doublet. CKM mixing
           is generational, so identifying a generational CP phase with the weak-x-color count is an un-forced bridge.
      (B3) NATIVE-PHASE MISMATCH: the framework's native CP-odd circulant phase arg(b) ~ 2/9 rad ~ 12.7 deg (the Koide
           delta) and the Z3 source phase 2*pi/3 = 120 deg are BOTH != 65.9 deg. So delta_CKM is NOT the native phase.
      (B4) the "inverse-square count" reading eta^2 = 1/n_pair^2 - 1/n_color^2, rho*A^2 = 1/n_color^2 is an exact
           RE-ENCODING of (rho,eta)=(1/6,sqrt5/6), not an independent forcing of them.
  (C) EXECUTABLE cross-check (NOT hard-coded booleans): the block PARSES the actual cited files and asserts their
      exact status text - that the channel assignment (CP-even real part <-> A1/symmetric, CP-odd imag part <-> 5-dim
      complement) and the raw radius r^2=1/n_quark ride the K_R carrier, which its note declares claim_type open_gate
      with three upstream gaps and "physical meaning is asserted"; and that the rho_eta narrow theorem disclaims the
      1+5 split ("Does not derive w_axis=1/6"; the 1+5 split is "not forced by the physical Cl(3)" baseline).

Reprove-and-cite: every FORCED fact (A1,A2) and every NON-FORCING demonstration (B1-B4) is reproven from sympy
primitives (the all-ones democratic vector, the Wolfenstein-apex trig, the count arithmetic); the admission status
(C) is an executable cross-check that parses the landed notes (CKM_ATLAS_AXIOM_CLOSURE_NOTE,
CKM_CP_PHASE_RHO_ETA_TO_DELTA, S3_TIME_BILINEAR_TENSOR_PRIMITIVE), never asserting it as label-constants. The measured
gamma (direct HFLAV world avg, Summer 2025, ~66.4 +2.7/-2.8 deg; indirect CKMfitter ~65.6 +0.9/-2.7 deg, UTfit ~65.8 +/- 2.2
deg) is a COMPARATOR only - named for provenance, never a derivation input. No PDG / fit value enters any derivation;
gamma is downstream. alpha_s does NOT enter the angle (it sets magnitudes only). This is an OBSTRUCTION, not a closure.
"""
import sympy as sp

R = []
def chk(label, ok):
    R.append((label, bool(ok)))

# ----------------------------------------------------------------------------------------------------
# (A) FORCED skeleton - genuinely derived from primitives
# ----------------------------------------------------------------------------------------------------

# (A1) cos^2(delta) = rho^2/(rho^2+eta^2) = w_A1, with rho=r*sqrt(w_A1), eta=r*sqrt(w_perp), w_A1+w_perp=1.
#      The CP radius r cancels identically -> the ANGLE is radius-independent.
r, w = sp.symbols('r w', positive=True)          # w = w_A1 in (0,1); w_perp = 1-w
rho = r * sp.sqrt(w)
eta = r * sp.sqrt(1 - w)
cos2 = sp.simplify(rho**2 / (rho**2 + eta**2))
chk("(A1) cos^2(delta) = rho^2/(rho^2+eta^2) = w_A1, INDEPENDENT of the CP radius r (r cancels identically)",
    sp.simplify(cos2 - w) == 0)

# (A2) the totally-symmetric (democratic) projection weight of a single basis state in an n-state module is 1/n.
#      dem = (1,...,1)/sqrt(n); <dem|e_i> = 1/sqrt(n); w_A1 = |<dem|e_i>|^2 = 1/n. Symbolic n + explicit n=6.
n = sp.symbols('n', positive=True, integer=True)
overlap = sp.Rational(1, 1) / sp.sqrt(n)          # i-th component of the normalized all-ones vector
chk("(A2) symmetric-projection weight of a basis state = |<dem|e_i>|^2 = 1/n  (pure projector geometry, a theorem)",
    sp.simplify(overlap**2 - 1/n) == 0)

# explicit construction at n=6 (no shortcut): build the democratic projector and read the diagonal weight
n6 = 6
dem = sp.Matrix([1]*n6) / sp.sqrt(n6)
P_sym = dem * dem.T                               # rank-1 projector onto the democratic direction
e1 = sp.Matrix([1] + [0]*(n6-1))
w_A1_explicit = sp.simplify((e1.T * P_sym * e1)[0, 0])
chk("(A2b) explicit n=6 democratic projector: <e_1|P_sym|e_1> = 1/6 = w_A1", w_A1_explicit == sp.Rational(1, 6))

# at w_A1 = 1/6 the forced trig gives the headline identity
w16 = sp.Rational(1, 6)
tan_delta = sp.sqrt((1 - w16) / w16)
chk("(A3) at w_A1=1/6: tan(delta)=sqrt5, cos(delta)=1/sqrt6, delta=arctan(sqrt5)=arccos(1/sqrt6)",
    sp.simplify(tan_delta - sp.sqrt(5)) == 0 and sp.simplify(sp.cos(sp.atan(sp.sqrt(5))) - 1/sp.sqrt(6)) == 0)

delta_deg = sp.deg(sp.atan(sp.sqrt(5)))
chk("(A3b) delta = 65.9051574... deg (exact-form numeric)", abs(float(delta_deg) - 65.9051574478893) < 1e-9)

# ----------------------------------------------------------------------------------------------------
# (B) NON-FORCING demonstrations - EXHIBIT the admissions by deriving the freedom explicitly
# ----------------------------------------------------------------------------------------------------

# (B1) the angle depends on the chosen symmetric-block dimension k of the n=6 module: the "1+5" split is a CHOICE.
def angle_from_split(k, ntot):
    return sp.deg(sp.acos(sp.sqrt(sp.Rational(k, ntot))))
a_1_5 = angle_from_split(1, 6)   # 65.905
a_2_4 = angle_from_split(2, 6)   # 54.736
a_3_3 = angle_from_split(3, 6)   # 45.000
chk("(B1) split 1+5 -> 65.905, 2+4 -> 54.736, 3+3 -> 45.000 : the angle CHANGES with the chosen split "
    "(so the '1+5' split is a free choice, NOT forced - matches the rho_eta_to_delta disclaimer)",
    abs(float(a_1_5) - 65.9051574) < 1e-5 and abs(float(a_2_4) - 54.7356103) < 1e-5 and float(a_3_3) == 45.0)

# (B2) the COUNT is load-bearing: 3-generation democratic angle != the n=6 atlas value.
gen3_angle = sp.deg(sp.acos(1 / sp.sqrt(3)))      # 54.7356 : naive democratic angle in 3-GENERATION space
quark6_angle = sp.deg(sp.acos(1 / sp.sqrt(6)))    # 65.9052 : atlas value, n=6 = 2(weak)x3(color)
chk("(B2) democratic angle in 3-GENERATION space = arccos(1/sqrt3) = 54.736 deg, which does NOT equal the atlas "
    "65.905 deg : the construction REQUIRES n=6 = weak x color (one doublet), NOT the 3-generation count "
    "(generational CP phase identified with the weak-x-color count = an un-forced bridge)",
    abs(float(gen3_angle) - 54.7356103) < 1e-6 and abs(float(quark6_angle) - 65.9051574) < 1e-6
    and sp.simplify(gen3_angle - quark6_angle) != 0)

# (B3) NATIVE-PHASE MISMATCH: the framework's native CP-odd phases are NOT 65.9 deg.
#      arg(b) ~ 2/9 rad (the Koide delta) and the Z3 source phase 2*pi/3 are both != arctan(sqrt5).
koide_delta_deg = sp.deg(sp.Rational(2, 9))       # ~12.73 deg  (native circulant phase arg(b))
z3_source_deg = sp.deg(sp.Rational(2, 1) * sp.pi / 3)  # 120 deg  (Z3 source phase)
chk("(B3) native CP-odd phases differ from delta_CKM: Koide arg(b)~2/9 rad ~ 12.73 deg != 65.905, and Z3 source "
    "2*pi/3 = 120 deg != 65.905 : delta_CKM is NOT the native circulant phase nor the Z3 source phase",
    abs(float(koide_delta_deg) - 12.7324) < 1e-3 and float(z3_source_deg) == 120.0
    and sp.simplify(koide_delta_deg - delta_deg) != 0 and sp.simplify(z3_source_deg - delta_deg) != 0)

# (B4) the "inverse-square count" reading is an exact RE-ENCODING of (rho,eta), not an independent forcing.
n_pair, n_color = 2, 3
A2 = sp.Rational(n_pair, n_color)                  # A^2 = 2/3
rho_v, eta_v = sp.Rational(1, 6), sp.sqrt(5) / 6
chk("(B4a) eta^2 = 1/n_pair^2 - 1/n_color^2 = 1/4 - 1/9 = 5/36  (exact restatement of eta=sqrt5/6)",
    sp.simplify(eta_v**2 - (sp.Rational(1, n_pair**2) - sp.Rational(1, n_color**2))) == 0)
chk("(B4b) rho*A^2 = 1/n_color^2 = 1/9, and eta^2 + rho*A^2 = 1/n_pair^2 = 1/4  (exact restatements, NOT forcings)",
    sp.simplify(rho_v * A2 - sp.Rational(1, n_color**2)) == 0
    and sp.simplify(eta_v**2 + rho_v * A2 - sp.Rational(1, n_pair**2)) == 0)

# ----------------------------------------------------------------------------------------------------
# (C) EXECUTABLE cross-check of the cited landed-note status (NOT hard-coded booleans).
#     The bridge's load-bearing identifications - the CP-even<->A1 / CP-odd<->complement channel assignment and the
#     raw radius r^2=1/n_quark - ride the K_R carrier; the 1+5 split is disclaimed by the rho_eta narrow theorem.
#     This block PARSES the actual cited files and asserts their exact status text (the #3138-safe posture: cross-check
#     the bridge's admission status against the landed notes, do not assert it as label-constants).
# ----------------------------------------------------------------------------------------------------
import os
import re

_HERE = os.path.dirname(os.path.abspath(__file__))
_DOCS = os.path.join(_HERE, os.pardir, "docs")


def _norm(filename):
    """Read a cited doc; strip markdown bold/backticks and collapse whitespace for robust substring matching."""
    with open(os.path.join(_DOCS, filename), encoding="utf-8") as fh:
        txt = fh.read()
    txt = txt.replace("`", "").replace("**", "")
    return re.sub(r"\s+", " ", txt)


kr_doc = _norm("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
chk("(C1) [executable cross-check of the landed file] S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE declares 'Claim type: "
    "open_gate', names 'three upstream gaps', and states its 'physical meaning is asserted' -> the carrier on which "
    "the channel assignment AND the raw radius r^2=1/n_quark ride is open_gate, not a derived primitive",
    ("Claim type: open_gate" in kr_doc) and ("three upstream gaps" in kr_doc)
    and ("physical meaning is asserted" in kr_doc))

rho_eta_doc = _norm("CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md")
chk("(C2) [executable cross-check of the landed file] the rho_eta narrow theorem (the only retained row in the chain) "
    "states 'Does not derive w_axis = 1/6 or w_perp = 5/6' and that the '1 + 5 decomposition is forced by the physical "
    "Cl(3)' baseline is explicitly NOT claimed -> the 1+5 split is a posited partition, not a theorem",
    ("Does not derive w_axis = 1/6 or w_perp = 5/6" in rho_eta_doc)
    and ("1 + 5 decomposition is forced by the physical Cl(3)" in rho_eta_doc))

atlas_doc = _norm("CKM_ATLAS_AXIOM_CLOSURE_NOTE.md")
chk("(C3) [executable cross-check of the landed file] CKM_ATLAS_AXIOM_CLOSURE_NOTE builds the angle from "
    "'n_quark = 2 x 3 = 6' (weak x color of one doublet) and a Z3 source phase 'delta_source = 2*pi/3' -> the count "
    "and the CP source are posited construction inputs (not the 3-generation count, cf. (B2))",
    ("n_quark = 2 x 3 = 6" in atlas_doc) and ("delta_source = 2*pi/3" in atlas_doc))

# ----------------------------------------------------------------------------------------------------
# (D) COMPARATOR (downstream, NOT an input): measured gamma. Each determination is a comparator only, with its source.
#     Direct world average (HFLAV Summer 2025, Unitarity Triangle angles page): gamma ~ 66.4 +2.7/-2.8 deg.
#     Indirect global CKM fit: CKMfitter gamma ~ 65.6 +0.9/-2.7 deg; UTfit (Bayesian) gamma ~ 65.8 +/- 2.2 deg.
#     No PDG / fit value enters any derivation above; gamma is purely downstream.
# ----------------------------------------------------------------------------------------------------
delta_num = float(delta_deg)
gamma_comparators = {
    "direct world avg (HFLAV Summer 2025)": (66.4, 2.75),  # +2.7/-2.8 -> use 2.75 as the 1-sigma scale
    "CKMfitter global fit":                 (65.6, 0.9),   # +0.9/-2.7 -> use the TIGHTER +0.9 side (conservative pull)
    "UTfit Bayesian global fit":            (65.8, 2.2),
}
gamma_pulls = {k: abs(delta_num - c) / e for k, (c, e) in gamma_comparators.items()}
chk("(D) [comparators only, not derivation inputs] delta_CKM = 65.905 deg agrees with the measured unitarity-triangle "
    "angle gamma within 1 sigma for the direct (HFLAV Summer 2025, 66.4 +2.7/-2.8) and indirect (CKMfitter 65.6 +0.9/-2.7; "
    "UTfit 65.8 +/-2.2) "
    "determinations [tightest pull ~0.34 sigma vs CKMfitter]; import-clean (no quark masses, no fitted CKM); "
    "alpha_s does NOT enter the angle",
    all(p < 1.0 for p in gamma_pulls.values()) and abs(gamma_pulls["CKMfitter global fit"] - 0.339) < 0.02)

# ----------------------------------------------------------------------------------------------------
P = sum(1 for _, o in R if o)
Fa = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, Fa))
if Fa:
    raise SystemExit(1)
print("""
OBSTRUCTION RESULT (CKM CP phase delta_CKM = arctan(sqrt5)):
 - The entire predictive content reduces to the single bridge cos^2(delta) = 1/n_quark. The FORCED skeleton is only
   (A1) the radius-independent trig cos^2(delta)=w_A1 and (A2) the symmetric-projection weight w_A1=1/n.
 - Every LOAD-BEARING physical identification is the framework's OWN documented admission: the CP-even<->A1 /
   CP-odd<->complement channel assignment and the raw radius r^2=1/n_quark ride the K_R carrier (open_gate, 3 unclosed
   gaps, physical meaning asserted); the 1+5 split is NOT forced by Cl(3)/Z^3; the count n=6=weak x color (NOT the
   3 generations) is un-forced and load-bearing (3-generation democratic angle = 54.7 deg, not 65.9); and the
   framework's native CP-odd phases (arg b ~ 12.7 deg, Z3 source 120 deg) are NOT 65.9 deg.
 - Therefore the bridge cos^2(delta)=1/n_quark is NOT derivable from {Lattice, Quantum, Record} as the framework
   stands: delta_CKM = arctan(sqrt5) is an ADMISSION (an open gate), structurally parallel to the strong-CP theta
   and the Koide r=1/2 admissions. The cleanest closure target is a retained-grade bridge identifying K_R with a
   physical readout primitive AND fixing the CP-even<->A1 / CP-odd<->complement channel assignment (K_R gaps #2,#3).
   This is an obstruction, not a closure; the sub-sigma agreement with the measured gamma is a downstream comparator,
   not a derivation.
""")
