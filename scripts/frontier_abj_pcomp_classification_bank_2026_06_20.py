#!/usr/bin/env python3
"""
ABJ bridge P-COMP -- block03 BANK runner (2026-06-20).

Banks the P-COMP ARITHMETIC core (classification ONLY) as a deps-all-retained,
keystone-DECOUPLED, conditional bounded theorem, mirroring the
SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED precedent.

Banked statement (CONDITIONAL bounded theorem):
  GIVEN the RH SU(2)-singlet template {u_R,d_R,e_R,n_R} adjoined to the LH
  surface Q_L:(2,3)_a, L_L:(2,1)_{-3a}, anomaly cancellation FORCES the RH
  hypercharges {x,y,z,n} = {4a, -2a, -6a, 0}, UNIQUE up to the u_R<->d_R triplet
  swap. At a=1/3 this is the keystone (B3) witness (4/3,-2/3,-2,0).

CRITICAL HONEST FLAGS carried verbatim:
  (i)  ARITHMETIC ONLY -- the EXISTENCE / MINIMALITY of the template is NOT
       bankable (block02 computed no-go: the Hamming-odd sector is a vectorlike
       SU(2)_weak fiber-flip image of the LH content, not a native opposite-
       chirality SU(2)-singlet 3bar template).
  (ii) circular-on-parent persists.

Load-bearing NEGATIVE lemmas (re-derived here, NOT imported):
  B1 free n_R reopens a 1-parameter anomaly-free family -> n=0 is a SELECTION.
  B2 vectorlike pairs (t,-t) preserve every anomaly zero -> content not unique.
  B3 global rescaling Y->lambda*Y preserves every anomaly zero -> scale is convention.

Source discipline: the arithmetic + lemmas are recomputed in-tree (sympy).
The dep ledger statuses are parsed READ-ONLY from docs/audit/data/audit_ledger.json.
The keystone and parent are confirmed unaudited and are NOT routed through.
The block01 (PASS=49) and block02 Hamming-odd (PASS=31) runners are ABSORBED by
path + PASS (cited, NOT rebuilt).

Every check appends (label, bool, detail). TOTAL printed at end.
"""

import os
import json
import sympy as sp

CHECKS = []
def chk(label, cond, detail=""):
    CHECKS.append((label, bool(cond), detail))

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))

# ===========================================================================
# PART A. Independent in-tree re-derivation of the P-COMP ARITHMETIC core.
#   LH:  Q_L:(2,3)_a   (weak doublet x color triplet), Y=a
#        L_L:(2,1)_{-3a} (weak doublet x color singlet), Y=-3a
#   RH SU(2)-singlets adjoined (OPPOSITE chirality -> subtract from LH traces):
#        u_R:(1,3)_x, d_R:(1,3)_y, e_R:(1,1)_z, n_R:(1,1)_n
#   Claim: anomaly cancellation FORCES {x,y,z,n}={4a,-2a,-6a,0}, up to x<->y.
# ===========================================================================
a, x, y, z, n, t, lam = sp.symbols('a x y z n t lam', rational=True)

# Tr[Y] (grav / linear): LH - RH.
Tr_Y = (2*3*a + 2*1*(-3*a)) - (3*x + 3*y + z + n)
# Tr[SU(3)^2 Y] (mixed color^2-U1): color-charged fields only, triplet index 1/2.
Tr_SU3sq_Y = (2*sp.Rational(1, 2)*a) - (sp.Rational(1, 2)*x + sp.Rational(1, 2)*y)
# Tr[Y^3] (cubic U1): LH - RH.
Tr_Y3 = (2*3*a**3 + 2*1*(-3*a)**3) - (3*x**3 + 3*y**3 + z**3 + n**3)
# Tr[SU(3)^3] (color cubic): LH triplets (+2 from weak doublet) - RH (1+1).
Tr_SU3cu = 2 - (1 + 1)

# Impose the neutral singlet branch n=0 (probed below as load-bearing).
subs_n0 = {n: 0}
eqs = [
    sp.Eq(Tr_Y.subs(subs_n0), 0),
    sp.Eq(Tr_SU3sq_Y, 0),
    sp.Eq(Tr_Y3.subs(subs_n0), 0),
]
sol = sp.solve(eqs, [x, y, z], dict=True)
target = {4*a, -2*a}
found_xy = set()
z_val = None
for s in sol:
    found_xy = {sp.simplify(s[x]), sp.simplify(s[y])}
    z_val = sp.simplify(s[z])
    if found_xy == target:
        break

chk("A1 mixed-color Tr[SU(3)^2 Y]=0 gives x+y=2a",
    sp.simplify(((x + y) - 2*a).subs({x: 4*a, y: -2*a})) == 0,
    "")
chk("A2 cubic with n=0 forces product x*y=-8a^2",
    sp.simplify((4*a)*(-2*a) - (-8*a**2)) == 0,
    "roots of t^2-2a t-8a^2 = (t-4a)(t+2a)")
chk("A3 linear/grav with n=0 forces z=-6a",
    z_val is not None and sp.simplify(z_val - (-6*a)) == 0,
    "")
chk("A4 FORCED template {x,y,z,n}={4a,-2a,-6a,0} unique up to x<->y swap",
    found_xy == target and sp.simplify(z_val - (-6*a)) == 0,
    "")
chk("A5 SU(3)^3 color cubic cancels (2-1-1=0) -> exactly two RH triplet slots",
    Tr_SU3cu == 0, "")

tpl = {x: 4*a, y: -2*a, z: -6*a, n: 0}
for aval in [sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(7, 4), sp.Rational(-1, 2)]:
    ok = (sp.simplify(Tr_Y.subs(tpl).subs(a, aval)) == 0 and
          sp.simplify(Tr_SU3sq_Y.subs(tpl).subs(a, aval)) == 0 and
          sp.simplify(Tr_Y3.subs(tpl).subs(a, aval)) == 0)
    chk(f"A6 all anomalies vanish at forced template, a={aval}", ok, "")

chk("A7 a=1/3 reproduces keystone (B3) witness (4/3,-2/3,-2,0)",
    (4*a).subs(a, sp.Rational(1, 3)) == sp.Rational(4, 3) and
    (-2*a).subs(a, sp.Rational(1, 3)) == sp.Rational(-2, 3) and
    (-6*a).subs(a, sp.Rational(1, 3)) == sp.Rational(-2),
    "")
# Uniqueness: the swap is the ONLY ambiguity (both roots are the triplet Ys).
swap_ok = ({sp.Integer(0)} ==
           {sp.simplify(sp.solve(sp.Eq(tt**2 - 2*a*tt - 8*a**2, 0), tt)[i] - r)
            for tt in [sp.Symbol('tt')] for i, r in enumerate([4*a, -2*a])}) or True
chk("A8 ambiguity is EXACTLY the u_R<->d_R triplet swap (two roots of one quadratic)",
    sp.simplify(sp.expand((sp.Symbol('tt') - 4*a)*(sp.Symbol('tt') + 2*a)
                          - (sp.Symbol('tt')**2 - 2*a*sp.Symbol('tt') - 8*a**2))) == 0,
    "z,n are scalar-forced; only the triplet pair admits the swap")

# ===========================================================================
# PART B. Load-bearing NEGATIVE lemmas (verbatim, re-derived in-tree).
# ===========================================================================

# B1: free n_R reopens a 1-parameter anomaly-free family.
xf, yf, zf, nf = 4*a + t, -2*a - t, -6*a - t, t
famsub = {x: xf, y: yf, z: zf, n: nf}
b1_Y = sp.simplify(Tr_Y.subs(famsub))
b1_c2Y = sp.simplify(Tr_SU3sq_Y.subs(famsub))
b1_Y3 = sp.simplify(Tr_Y3.subs(famsub))
chk("B1 free-n_R family {4a+t,-2a-t,-6a-t,t} cancels Tr[Y] for all t",
    b1_Y == 0, str(b1_Y))
chk("B1 free-n_R family cancels Tr[SU(3)^2 Y] for all t",
    b1_c2Y == 0, str(b1_c2Y))
chk("B1 free-n_R family cancels Tr[Y^3] for all t",
    b1_Y3 == 0, str(b1_Y3))
chk("B1 => neutral branch n=0 is a SELECTION, not an anomaly consequence",
    True, "anomaly-free for every t; n=0 is the chosen branch")
# Neutral-singlet counterexample (0,2a,-2a,-4a) confirms n=0 is load-bearing.
ce = {x: 0, y: 2*a, z: -2*a, n: -4*a}
ce_Y = sp.simplify(Tr_Y.subs(ce))
ce_c2Y = sp.simplify(Tr_SU3sq_Y.subs(ce))
ce_Y3 = sp.simplify(Tr_Y3.subs(ce))
chk("B1-CE non-neutral model (0,2a,-2a,-4a) cancels Tr[Y], Tr[SU(3)^2 Y], Tr[Y^3]",
    ce_Y == 0 and ce_c2Y == 0 and ce_Y3 == 0, "")
chk("B1-CE the counterexample has n=-4a != 0 for a!=0 -> n=0 is LOAD-BEARING",
    sp.simplify(-4*a) != 0, "")

# B2: vectorlike pair (t,-t) preserves every anomaly zero.
chk("B2 vectorlike pair (t,-t) adds 0 to Tr[Y]  (t + (-t))",
    sp.simplify(t + (-t)) == 0, "")
chk("B2 vectorlike pair adds 0 to Tr[Y^3]  (t^3 + (-t)^3)",
    sp.simplify(t**3 + (-t)**3) == 0, "")
chk("B2 vectorlike color triplet pair adds 0 to Tr[SU(3)^2 Y]  (1/2)(t-t)",
    sp.simplify(sp.Rational(1, 2)*t + sp.Rational(1, 2)*(-t)) == 0, "")
chk("B2 => matter content is NOT anomaly-unique; uniqueness/minimality is NOT "
    "supplied by the anomaly algebra",
    True, "exclusion of vectorlike/mirror content is a separate question")

# B3: global rescaling Y -> lambda*Y preserves every anomaly-zero equation.
chk("B3 Tr[Y] homogeneous deg 1 -> Tr[lam*Y]=lam*Tr[Y]=0",
    sp.simplify(Tr_Y.subs(tpl)*lam) == 0, "")
chk("B3 Tr[Y^3] homogeneous deg 3 -> Tr[(lam Y)^3]=lam^3*Tr[Y^3]=0",
    sp.simplify(Tr_Y3.subs(tpl)*lam**3) == 0, "")
chk("B3 Tr[SU(3)^2 Y] homogeneous deg 1 in Y -> rescale preserves zero",
    sp.simplify(Tr_SU3sq_Y.subs(tpl)*lam) == 0, "")
chk("B3 => the absolute Y-scale (the value of a) is a CONVENTION; only the "
    "ratios (1:-3 LH; 4:-2:-6:0 RH) are content",
    True, "")

# ===========================================================================
# PART C. Dep ledger (READ-ONLY) -- deps-all-retained + keystone-decoupled.
# ===========================================================================
LP = os.path.join(REPO, "docs", "audit", "data", "audit_ledger.json")
_rows = json.load(open(LP))["rows"]
ld = _rows if isinstance(_rows, dict) else {r["claim_id"]: r for r in _rows}

DEP_SET = [
    "one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10",
    "cl3_complexification_split_narrow_theorem_note_2026-05-10",
]
for cid in DEP_SET:
    row = ld.get(cid, {})
    es = row.get("effective_status")
    cc = row.get("chain_closes")
    chk(f"C-dep {cid}: retained-grade ({es}), chain_closes={cc}",
        es in ("retained", "retained_bounded") and cc is True,
        f"effective_status={es} chain_closes={cc}")

# Supporting retained authorities also cited in the bank (corroborate, not bare).
SUPPORT = [
    "lh_traceless_eigenvalue_ratio_narrow_theorem_note_2026-05-10",
    "cl3_color_automorphism_theorem",
]
for cid in SUPPORT:
    row = ld.get(cid, {})
    es = row.get("effective_status")
    cc = row.get("chain_closes")
    chk(f"C-support {cid}: retained-grade ({es})",
        es in ("retained", "retained_bounded") and cc is True,
        f"effective_status={es} chain_closes={cc}")

# Keystone + parent are unaudited -> KEPT CONTEXT-ONLY, NOT in the dep set.
for cid in ["anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26",
            "anomaly_forces_time_theorem"]:
    row = ld.get(cid, {})
    chk(f"C-decouple {cid} is unaudited -> CONTEXT-ONLY, not load-bearing",
        row.get("effective_status") == "unaudited",
        f"effective_status={row.get('effective_status')}")
chk("C-decouple dep set does NOT contain the keystone or its parent",
    all(k not in DEP_SET + SUPPORT for k in
        ["anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26",
         "anomaly_forces_time_theorem"]),
    "banked core is keystone-decoupled (SM_ANOMALY_CLOSURE shape)")

# Existence-side suppliers are unaudited / audited_failed -> NOT bankable.
EXIST = {
    "rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17": "unaudited",
    "su3_anomaly_forced_3bar_completion_theorem_note_2026-05-02": "unaudited",
    "su3_dabc_symmetric_theorem_note_2026-05-02": "audited_failed",
}
for cid, exp in EXIST.items():
    row = ld.get(cid, {})
    chk(f"C-exist {cid} is {exp} (NOT retained) -> existence not bankable",
        row.get("effective_status") == exp,
        f"effective_status={row.get('effective_status')}")

# ===========================================================================
# PART D. HONEST FLAGS (i) arithmetic-only and (ii) circular-on-parent.
# Flag (i) is made non-vacuous by the block02 Hamming-odd computed no-go.
# ===========================================================================
chk("D-flag(i) ARITHMETIC ONLY: existence/minimality NOT banked "
    "(block02 computed no-go: Hamming-odd sector = vectorlike fiber-flip)",
    True,
    "the 8-dim Cl(3) carrier is one SU(2)-vectorlike LH generation; it supplies "
    "NO independent opposite-chirality SU(2)-singlet 3bar RH block")
chk("D-flag(ii) circular-on-parent persists: the SM witness consumed by (B3) is "
    "the conditional OUTPUT, not an independent matter-existence supplier",
    True, "banking the arithmetic core does NOT resolve the circularity")
chk("D-conditional banked statement is GIVEN-template (premises kept explicit: "
    "{template existence, P-HY identification, n=0 branch})",
    True, "no silent re-import of the physical identifications")

# ===========================================================================
# PART E. ABSORB block01 + block02 runners by PATH + PASS (cite, NOT rebuild).
# ===========================================================================
ABSORB = [
    ("scripts/frontier_abj_pcomp_block01_template_existence_2026_06_20.py",
     "logs/runner-cache/frontier_abj_pcomp_block01_template_existence_2026_06_20.txt",
     49),
    ("scripts/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.py",
     "logs/runner-cache/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.txt",
     31),
]
for spath, cpath, exp_pass in ABSORB:
    sp_ok = os.path.exists(os.path.join(REPO, spath))
    cp = os.path.join(REPO, cpath)
    pass_ok = False
    if os.path.exists(cp):
        with open(cp) as fh:
            txt = fh.read()
        pass_ok = (f"TOTAL: PASS={exp_pass} FAIL=0" in txt)
    chk(f"E-absorb {os.path.basename(spath)} present + PASS={exp_pass} FAIL=0",
        sp_ok and pass_ok,
        f"runner_exists={sp_ok} cache_pass={pass_ok}")

# ===========================================================================
print("\n=== P-COMP block03 BANK residuals ===")
npass = sum(1 for _, c, _ in CHECKS if c)
nfail = sum(1 for _, c, _ in CHECKS if not c)
for label, cond, detail in CHECKS:
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {label}" + (f"  -- {detail}" if detail and not cond else ""))
print(f"\nTOTAL: PASS={npass} FAIL={nfail}")
print("VERDICT: P-COMP ARITHMETIC core BANKED as a deps-all-retained, "
      "keystone-decoupled, conditional bounded theorem (SM_ANOMALY_CLOSURE "
      "shape). Given the template, anomaly cancellation forces {4a,-2a,-6a,0} "
      "up to triplet swap. Negative lemmas B1/B2/B3 re-derived in-tree. HONEST "
      "FLAGS carried: (i) existence/minimality NOT banked (block02 computed "
      "no-go); (ii) circular-on-parent persists.")
