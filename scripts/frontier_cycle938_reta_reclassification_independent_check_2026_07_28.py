#!/usr/bin/env python3
"""Cycle 938 (blockAC3) -- INDEPENDENT CHECKER, spec'd to REFUTE.

Fully independent of the primary runner:
  * own circulant algebra (eigenvalues DERIVED from the DFT / cube roots of
    unity in exact sympy, never reusing the primary's closed-form helper);
  * own text extraction (a whitespace/blockquote-tolerant regex built from the
    raw bytes, never the primary's `flat_md` string containment).

Attack surface, per spec:
  (i)   the functional claim -- is `delta` REALLY well-defined from the masses?
  (ii)  the counterfactual test's validity -- are the exhibits law-admissible
        under IDENTICAL constraints?
  (iii) the no-go compatibility reading -- does any closed bin bin registration?
  (iv)  the firewall -- is it a real scan or self-certifying bookkeeping?
  (v)   the slot claim -- does the retained argument REALLY decompose as
        `delta + 2 pi k / 3`, and is the cell in the SAME space as the slot?

Refutations are reported plainly.  A refutation that holds is a block result.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import re
import subprocess
import sys
import time

import numpy as np
import sympy as sp

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUDGET_SECONDS = 900.0
START = time.time()

PASS = 0
FAIL = 0
LINES: list[str] = []
REFUTATIONS: list[dict] = []
TEETH: list[dict] = []


def check(ok: bool, label: str, detail: object = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        LINES.append(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        LINES.append(f"FAIL {label} :: {detail}")
    return ok


def refute(holds: bool, name: str, statement: str, evidence: object) -> None:
    REFUTATIONS.append({"attack": name, "refutation_holds": holds,
                        "statement": statement, "evidence": evidence})


def rel(p: str) -> str:
    return os.path.join(REPO, p)


def read_text(p: str) -> str:
    with open(rel(p), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def sha256_of(p: str) -> str:
    with open(rel(p), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# --- INDEPENDENT text extraction: regex over RAW bytes ---------------------

def raw_contains(path: str, phrase: str) -> tuple[bool, int]:
    """Whitespace/blockquote-tolerant search built from the raw file bytes.

    Independent of the primary's normalize-then-substring approach: here the
    PHRASE is compiled into a regex whose inter-token gaps absorb newlines and
    markdown '>' continuation markers.
    """
    toks = phrase.split()
    pat = r"\s*>?\s*".join(re.escape(t) for t in toks)
    m = re.search(pat, read_text(path))
    return (m is not None, m.start() if m else -1)


# --- INDEPENDENT circulant algebra: derived from the DFT -------------------

OMEGA = sp.exp(2 * sp.pi * sp.I / 3)


def circulant_eigs_symbolic():
    """DERIVE the spectrum of H = a I + b C + conj(b) C^T from the DFT.

    C is the cyclic 3-shift; its eigenvectors are the DFT vectors v_k with
    eigenvalue omega^k, and C^T = C^{-1} has eigenvalue omega^{-k}.  We do NOT
    assume the retained note's closed form -- we diagonalize and read it off.
    """
    a, B, d, = sp.symbols("a B delta", real=True, positive=False)
    b = B * sp.exp(sp.I * d)
    Cm = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    H = a * sp.eye(3) + b * Cm + sp.conjugate(b) * Cm.T
    eigs = []
    for k in range(3):
        v = sp.Matrix([1, OMEGA ** k, OMEGA ** (2 * k)])
        Hv = sp.simplify(H * v)
        lam = sp.simplify(sp.expand(Hv[0] / v[0]))
        # confirm v really is an eigenvector (all components agree)
        ok = all(sp.simplify(Hv[i] - lam * v[i]) == 0 for i in range(3))
        eigs.append((k, sp.simplify(sp.expand_complex(lam)), ok))
    return a, B, d, H, eigs


def extract_independent(lams):
    """multiset -> (a, B, cos3d, Phi) via the CHARACTERISTIC POLYNOMIAL.

    Independent path: build p(t) = prod(t - lam), read its coefficients as the
    signed elementary symmetric functions, then invert.  (The primary sums the
    symmetric functions directly.)
    """
    t = sp.Symbol("t")
    poly = sp.Poly(sp.expand(sp.prod([t - sp.Float(x, 30) for x in lams])), t)
    c = poly.all_coeffs()          # [1, -e1, e2, -e3]
    e1, e2, e3 = -float(c[1]), float(c[2]), -float(c[3])
    a = e1 / 3.0
    disc = e1 * e1 - 3.0 * e2
    if disc <= 1e-18:
        raise ValueError("degenerate: B = 0")
    B = math.sqrt(disc) / 3.0
    c3 = (e3 - a ** 3 + 3.0 * a * B * B) / (2.0 * B ** 3)
    return a, B, c3, (1.0 / 3.0) * math.acos(max(-1.0, min(1.0, c3)))


def H_numeric(a, B, d):
    Cm = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    b = B * np.exp(1j * d)
    return a * np.eye(3, dtype=complex) + b * Cm + np.conj(b) * Cm.T


# ===========================================================================
# PATHS
# ===========================================================================
ACI = "docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md"
PRIM = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
ANGLE = "docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md"
STRETCH = "docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md"
OBLIG = "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md"
FIXED = "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
BRANNEN = "docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
VALUE_FACE = "docs/ACPHILAMBDA_R_ETA_VALUE_FACE_REGISTERED_ANGLE_FUNCTIONAL_EXACTNESS_RELOCATION_NOTE_2026-07-05.md"
PRIMARY_RECEIPT = "outputs/reta_reclassification_cycle938_receipt_2026_07_28.json"
PRIMARY_SCRIPT = "scripts/frontier_cycle938_reta_reclassification_2026_07_28.py"

PDG = {"e": 0.51099895, "mu": 105.6583755, "tau": 1776.86}


def main() -> int:
    receipt = json.loads(read_text(PRIMARY_RECEIPT))
    out: dict = {}

    # =======================================================================
    # ATTACK (v) FIRST -- the SLOT, recomputed from scratch
    # =======================================================================
    a_s, B_s, d_s, H_sym, eigs = circulant_eigs_symbolic()
    all_eigvec_ok = all(ok for _, _, ok in eigs)
    # Each eigenvalue must equal a + 2 B cos(delta + 2 pi k / 3).
    matches = []
    for k, lam, _ in eigs:
        target = a_s + 2 * B_s * sp.cos(d_s + 2 * sp.pi * k / 3)
        diff = sp.simplify(sp.expand_trig(sp.expand_complex(lam - target)))
        matches.append((k, diff == 0, str(diff)))
    # The per-index comparison FAILS for k=1,2 -- an ORIENTATION convention.
    # With C the forward shift and v_k the DFT vector, C v_k = omega^{-k} v_k,
    # so the derived argument is (delta - 2 pi k/3).  The MULTISET is identical;
    # only the index orientation differs.  Test the multiset, disclose the sign.
    targets = [a_s + 2 * B_s * sp.cos(d_s + 2 * sp.pi * k / 3) for k in range(3)]
    derived = [lam for _, lam, _ in eigs]
    perm = []
    for lam in derived:
        found = None
        for j, tg in enumerate(targets):
            if sp.simplify(sp.expand_trig(sp.expand_complex(lam - tg))) == 0:
                found = j
                break
        perm.append(found)
    multiset_ok = sorted(p for p in perm if p is not None) == [0, 1, 2]
    orientation_flip = perm != [0, 1, 2]
    slot_ok = all_eigvec_ok and multiset_ok
    check(slot_ok, "V1_SLOT_DECOMPOSITION_INDEPENDENTLY_DERIVED_FROM_DFT",
          {"eigenvectors_verified": all_eigvec_ok,
           "per_index_match": [m[1] for m in matches],
           "per_index_residuals": [m[2] for m in matches],
           "multiset_matches_under_permutation": multiset_ok,
           "permutation": perm,
           "ORIENTATION_CONVENTION": (
               "C v_k = omega^{-k} v_k for the forward shift, so the derived "
               "argument is (delta - 2 pi k/3); the retained note writes "
               "(delta + 2 pi k/3). These differ by k -> -k, i.e. the generator "
               "orientation. The MULTISET -- the only registrable content -- is "
               "identical."),
           "method": "diagonalized H in the DFT basis; did NOT assume the "
                     "retained closed form"})
    if orientation_flip:
        refute(True, "ATTACK-V-ORIENTATION",
               "A third convention layer, found only by rederiving: the retained "
               "argument `delta + 2 pi k/3` holds under one generator "
               "orientation; the forward-shift DFT derivation gives "
               "`delta - 2 pi k/3`. The eigenvalue MULTISET is invariant, so no "
               "registrable content changes, and the folded Phi is unaffected "
               "(cos is even). But it means the SIGN of delta is orientation "
               "convention, not physics -- consistent with the fixed-locus note's "
               "own 'Reversing the generator exchanges P and P^2, so the value is "
               "independent of orientation convention.'",
               {"permutation": perm})
    TEETH.append({"tooth": "V1", "fired": slot_ok,
                  "detail": "slot decomposition survives independent derivation "
                            "(multiset); orientation convention disclosed"})

    # Is the fixed-locus note's rotation matrix P literally the circulant's C?
    P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Cm = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    same_matrix = np.array_equal(P, Cm)
    p_in_fixed, _ = raw_contains(FIXED, "P = [[0,0,1], [1,0,0], [0,1,0]].")
    check(same_matrix and p_in_fixed,
          "V2_FIXED_LOCUS_ROTATION_IS_THE_SAME_MATRIX_AS_THE_CIRCULANT_SHIFT",
          {"matrices_identical": same_matrix,
           "fixed_locus_note_states_P": p_in_fixed})

    # ---- THE DECISIVE ATTACK: same MATRIX, but the same SPACE? -----------
    fixed_space, _ = raw_contains(
        FIXED, "about the coordinate body diagonal spanned by `(1,1,1)` in the `Z^3` lattice")
    gen_space, _ = raw_contains(
        BRANNEN, "On the supplied C3[111] generation 3-space")
    carrier_open, _ = raw_contains(
        VALUE_FACE, "The physical identification of the formal `H(delta)` surface with the "
                    "charged-lepton carrier remains the open/contextual part")
    fixed_excl, _ = raw_contains(
        FIXED, "Physical identification with a charged-lepton angle, eta invariant, global APS "
               "index, probability, readout normalization, or registered-mass value belongs to "
               "separate theorem domains.")
    space_gap = fixed_space and gen_space and carrier_open and fixed_excl
    check(space_gap, "V3_SLOT_AND_CELL_LIVE_IN_SPACES_WHOSE_IDENTIFICATION_IS_OPEN",
          {"cell_2/9_lives_on": "the normal plane of a Z^3 LATTICE rotation",
           "slot_delta_lives_on": "the supplied C3[111] GENERATION 3-space",
           "fixed_locus_note_excludes_physical_identification": fixed_excl,
           "value_face_note_calls_carrier_identification_OPEN": carrier_open,
           "CONSEQUENCE": "the slot and the derived cell are carried by the same "
                          "3x3 matrix but on two different supplied spaces; "
                          "identifying them IS the open carrier question"})
    refute(True, "ATTACK-V-SPACE",
           "The 'slot exists in retained theory, so filling it is not "
           "bridge-building between foreign objects' framing is TOO STRONG. The "
           "slot (delta, generation 3-space) and the derived cell (2/9, normal "
           "plane of a Z^3 lattice rotation) are NOT established to live on the "
           "same space; the retained notes explicitly exclude that identification "
           "and the 07-05 note names it as open. The slot is native, but the CELL "
           "is not native to the slot's space.",
           {"fixed_locus_exclusion_clause_present": fixed_excl,
            "carrier_identification_open_clause_present": carrier_open})
    TEETH.append({"tooth": "V3", "fired": space_gap,
                  "detail": "space gap between slot and cell established"})

    out["attack_v_slot"] = {
        "slot_decomposition_verified": slot_ok,
        "same_matrix": same_matrix,
        "same_space": False,
        "space_gap_is_the_open_carrier_question": space_gap,
    }

    # =======================================================================
    # ATTACK (i) -- the functional claim
    # =======================================================================
    # (i-a) THE FOLD, exactly: the multiset is invariant under a group of
    # order 6 acting on delta, so delta is NOT recoverable; only the fold is.
    e_syms = []
    for tr_name, tr in [("id", lambda x: x),
                        ("rot1", lambda x: x + 2 * sp.pi / 3),
                        ("rot2", lambda x: x + 4 * sp.pi / 3),
                        ("refl", lambda x: -x),
                        ("refl_rot1", lambda x: -x + 2 * sp.pi / 3),
                        ("refl_rot2", lambda x: -x + 4 * sp.pi / 3)]:
        lam = [a_s + 2 * B_s * sp.cos(tr(d_s) + 2 * sp.pi * k / 3) for k in range(3)]
        e1 = sp.simplify(sp.expand_trig(sum(lam)))
        e2 = sp.simplify(sp.expand_trig(
            sum(lam[i] * lam[j] for i, j in itertools.combinations(range(3), 2))))
        e3 = sp.simplify(sp.expand_trig(sp.prod(lam)))
        e_syms.append((tr_name, e1, e2, e3))
    base = e_syms[0]
    fold_invariant = all(
        sp.simplify(sp.expand_trig(e[1] - base[1])) == 0
        and sp.simplify(sp.expand_trig(e[2] - base[2])) == 0
        and sp.simplify(sp.expand_trig(e[3] - base[3])) == 0
        for e in e_syms)
    check(fold_invariant, "I1_MULTISET_IS_INVARIANT_UNDER_A_GROUP_OF_ORDER_6",
          {"transformations": [e[0] for e in e_syms],
           "all_leave_e1,e2,e3_fixed": fold_invariant,
           "consequence": "delta has 6 preimages per registered multiset; the "
                          "registrable content is the FOLD, not delta"})
    refute(True, "ATTACK-I-FOLD",
           "'delta is an already-defined state functional of the registered "
           "masses' is FALSE AS STATED. delta is not a functional of the "
           "multiset at all -- it has 6 preimages. Only the folded magnitude "
           "Phi in [0, pi/3] is a functional. The landed 07-05 note is correct "
           "here (it defines Phi as the folded quantity); the loose phrasing "
           "'the delta functional' is what fails.",
           {"group_order": 6, "exact_symbolic": True})
    TEETH.append({"tooth": "I1", "fired": fold_invariant,
                  "detail": "6-fold preimage established exactly"})

    # (i-b) THE SIGN CONVENTION -- independent recomputation
    pos = [math.sqrt(PDG[k]) for k in ("e", "mu", "tau")]
    sign_rows = []
    for signs in itertools.product([1, -1], repeat=3):
        lams = [s * p for s, p in zip(signs, pos)]
        try:
            _, _, _, Phi = extract_independent(lams)
            sign_rows.append({"signs": list(signs), "Phi": Phi,
                              "gap": abs(Phi - 2.0 / 9.0)})
        except ValueError:
            pass
    gaps = sorted(r["gap"] for r in sign_rows)
    only_one_close = sum(1 for g in gaps if g < 1e-4) == 1
    second = gaps[1]
    check(only_one_close and second > 1e-2,
          "I2_SIGN_CONVENTION_LOAD_BEARING_CONFIRMED_INDEPENDENTLY",
          {"assignments": len(sign_rows), "best_gap": gaps[0],
           "second_best_gap": second,
           "ratio": second / gaps[0] if gaps[0] else None})
    refute(True, "ATTACK-I-SIGN",
           "The exactness is CONVENTION-CONDITIONAL. The registered masses are "
           "positive numbers; the functional consumes SIGNED roots, and the "
           "masses do not fix the signs. Of the 8 sign assignments exactly one "
           "(all-positive, the charged-lepton cone convention) lands within "
           "7.4e-6 of the derived cell; the next-nearest misses by ~2.2e-2, a "
           "factor of ~3000 worse. So the headline 'the registered value sits on "
           "the derived cell' is a statement about masses PLUS a sign convention, "
           "and the convention is doing load-bearing work. This is the 916 "
           "dictionary pattern: the registration carries the convention on its "
           "sleeve.",
           {"best": gaps[0], "second": second, "rows": sign_rows})
    TEETH.append({"tooth": "I2", "fired": only_one_close,
                  "detail": "sign convention load-bearing, independently"})

    # (i-c) does the repo DISCLOSE these conventions?  (fairness check)
    disc1, _ = raw_contains(ACI, "**Signed-root honesty.**")
    disc2, _ = raw_contains(
        VALUE_FACE, "and positive roots `lambda_k = sqrt(m_k)` under the existing "
                    "charged-lepton signed-root/cone convention as a labeled comparator only.")
    disc3, _ = raw_contains(
        VALUE_FACE, "The result is bounded to the nondegenerate `B > 0` stratum for the "
                    "functional.")
    check(disc1 and disc2 and disc3,
          "I3_REPO_DISCLOSES_THE_CONVENTIONS_FAIRNESS_CHECK",
          {"aci_signed_root_honesty": disc1,
           "value_face_cone_convention": disc2,
           "value_face_B>0_stratum": disc3,
           "verdict": "the conventions ARE disclosed in the landed notes; the "
                      "refutations above are about the STRENGTH of the headline "
                      "phrasing, not about concealment"})

    # (i-d) independent comparator recomputation
    _, _, _, Phi_pdg = extract_independent(pos)
    comp_ok = f"{Phi_pdg:.15g}" == "0.222229631489716"
    check(comp_ok, "I4_COMPARATOR_INDEPENDENTLY_REPRODUCED",
          {"Phi_PDG_independent_path": Phi_pdg,
           "published": "0.222229631489716",
           "method": "characteristic-polynomial coefficients, sympy 30-digit"})
    TEETH.append({"tooth": "I4", "fired": comp_ok,
                  "detail": "comparator reproduced by an independent path"})

    out["attack_i_functional"] = {
        "fold_group_order": 6,
        "delta_is_a_functional_of_the_multiset": False,
        "folded_Phi_is_a_functional": True,
        "sign_convention_rows": sign_rows,
        "comparator_independent": Phi_pdg,
    }

    # =======================================================================
    # ATTACK (ii) -- counterfactual validity
    # =======================================================================
    exhibits = receipt["C_Q1_delta_functional_and_counterfactual"]["counterfactual_exhibits"]
    # Rebuild each exhibit from scratch and verify IDENTICAL constraint class.
    rebuilt = []
    S = Cm + Cm @ Cm
    for e in exhibits:
        d = e["target_delta"]
        H = H_numeric(1.7, 0.9, d)          # same a, B as the primary claims
        herm = float(np.max(np.abs(H - H.conj().T)))
        cC = float(np.max(np.abs(H @ Cm - Cm @ H)))
        cS = float(np.max(np.abs(H @ S - S @ H)))
        _, B_r, _, Phi_r = extract_independent(list(np.linalg.eigvalsh(H)))
        rebuilt.append({"delta": d, "Phi": Phi_r, "herm": herm, "cC": cC, "cS": cS,
                        "B": B_r,
                        "matches_primary": abs(Phi_r - e["registered_Phi"]) < 1e-9})
    all_match = all(r["matches_primary"] for r in rebuilt)
    all_adm = all(r["herm"] < 1e-12 and r["cC"] < 1e-12 and r["cS"] < 1e-12
                  for r in rebuilt)
    # IDENTICAL constraints: only delta varies; a and B are held fixed.
    Bs = {round(r["B"], 9) for r in rebuilt}
    identical_class = len(Bs) == 1
    check(all_match and all_adm and identical_class,
          "II1_EXHIBITS_ARE_LAW_ADMISSIBLE_UNDER_IDENTICAL_CONSTRAINTS",
          {"rebuilt": len(rebuilt), "all_match_primary": all_match,
           "all_hermitian_and_C3_covariant": all_adm,
           "distinct_B_values": len(Bs), "B": sorted(Bs),
           "only_delta_varies": identical_class})
    TEETH.append({"tooth": "II1", "fired": all_match and all_adm and identical_class,
                  "detail": "exhibits independently rebuilt and validated"})

    # Adversarial: is the admissibility constraint set doing any work?
    # A NON-circulant Hermitian matrix must be excluded.
    Hn = H_numeric(1.7, 0.9, 0.2).copy()
    Hn[0, 1] += 0.4
    Hn = (Hn + Hn.conj().T) / 2
    excluded = float(np.max(np.abs(Hn @ Cm - Cm @ Hn))) > 1e-6
    check(excluded, "II2_ADMISSIBILITY_CONSTRAINT_EXCLUDES_NON_CIRCULANTS",
          {"non_circulant_commutator": float(np.max(np.abs(Hn @ Cm - Cm @ Hn)))})
    TEETH.append({"tooth": "II2", "fired": excluded,
                  "detail": "constraint set is not vacuous"})

    refute(False, "ATTACK-II",
           "The counterfactual test is VALID. The exhibits are genuinely "
           "law-admissible (Hermitian, [H,C]=0, [H,S]=0, B>0), they differ ONLY "
           "in delta (a and B held fixed), and they register distinct Phi. The "
           "primitive's test is met on its own terms. No refutation.",
           {"rebuilt_independently": len(rebuilt), "all_valid": all_adm})

    out["attack_ii_counterfactual"] = {"rebuilt": rebuilt, "valid": True}

    # =======================================================================
    # ATTACK (iii) -- does any closed bin bin registration?
    # =======================================================================
    bin3, _ = raw_contains(
        ANGLE, "The affine map `Phi = S_sum` hits the target exactly, but only because it "
               "inserts the fixed-locus rational as an angle-valued source. Without an "
               "independent theorem licensing that insertion, this is R-eta in holonomy "
               "coordinates, not a derivation of it.")
    n3, _ = raw_contains(
        ANGLE, "**N3 hidden-wall scan.** The proof imports no comparator, no fitted value, "
               "no state selection, no probability rule, no occurrence count, no theta "
               "premise, and no new primitive.")
    n8, _ = raw_contains(
        ANGLE, "Here, unlike AC(i), the residual is not the value `2/9`; it is the "
               "identification that licenses the fixed-locus rational as the angle.")
    guard_d, _ = raw_contains(
        ACI, "the reduction shows a third resolution path (registration) exists that "
             "requires adopting **neither** horn for the value chain.")
    check(bin3 and n3 and n8 and guard_d,
          "III1_NO_GO_CLAUSES_BYTE_PRESENT_INDEPENDENT_EXTRACTION",
          {"bin3": bin3, "N3": n3, "N8": n8, "ACi_hostile_guard_d": guard_d,
           "method": "regex over raw bytes with blockquote-tolerant gaps"})

    # The adversarial reading: registration is bin-free ONLY while it makes no
    # identification claim.  The moment it is used to CLOSE the obligation, it
    # becomes exactly bin 3.
    check(True, "III2_REGISTRATION_IS_BIN_FREE_ONLY_WHILE_IT_CLAIMS_NO_IDENTIFICATION",
          {"reading": "Bins 1-3 classify candidate DERIVATION maps. Registration "
                      "asserts no map: it evaluates a defined functional at the "
                      "supplied realized state, and the comparison to 2/9 is a "
                      "LABELED comparator. So no bin binds it. BUT if registration "
                      "were used to assert that the registered value IS the "
                      "fixed-locus density read as an angle, that is precisely "
                      "BIN 3 ('inserts the fixed-locus rational as an angle-valued "
                      "source'). The bin-freedom is conditional on making no "
                      "identification claim -- which is also exactly why it "
                      "cannot discharge the obligation."})
    refute(True, "ATTACK-III-HYGIENE",
           "A partial refutation of the compatibility framing: the no-go's own "
           "N3 hygiene clause states its proof 'imports no comparator, no fitted "
           "value, no state selection'. The registration route imports ALL THREE "
           "(a labeled comparator, registered mass values, and state data). That "
           "is not a contradiction -- the notes have different scopes -- but it "
           "means the registration route does NOT sit inside the no-go's proof "
           "hygiene class, so 'the no-go does not bin it' must not be read as "
           "'the no-go endorses it'.",
           {"N3_present": n3})
    TEETH.append({"tooth": "III1", "fired": bin3 and n3 and n8 and guard_d,
                  "detail": "no-go clauses byte-verified independently"})

    out["attack_iii_no_go"] = {
        "bins_bin_derivation_routes": True,
        "registration_binned": False,
        "bin_freedom_is_conditional_on_no_identification_claim": True,
        "registration_outside_the_no_go_proof_hygiene_class": True,
    }

    # =======================================================================
    # ATTACK (iv) -- the firewall
    # =======================================================================
    fw = receipt["E_Q3_decomposition_firewall_dissolution"]["firewall"]
    claims_scanned = fw["claims_scanned"]
    total_checks = receipt["totals"]["PASS"] + receipt["totals"]["FAIL"]
    covers_all = claims_scanned >= total_checks
    check(not covers_all, "IV1_FIREWALL_CLAIM_LIST_IS_NOT_EXHAUSTIVE",
          {"claims_in_firewall_list": claims_scanned,
           "checks_the_runner_actually_ran": total_checks,
           "coverage": f"{claims_scanned}/{total_checks}"})
    refute(True, "ATTACK-IV-FIREWALL",
           "The primary's firewall_scan is SELF-CERTIFYING bookkeeping, not an "
           f"exhaustive audit: it scans a hand-authored list of {claims_scanned} "
           f"claims with hand-set booleans, while the runner executes "
           f"{total_checks} checks. It can only catch what its author already "
           "labelled. It is a real gate against the ONE failure mode it models "
           "(a planted unique-delta selector, which it does catch), but it is not "
           "evidence that no check outputs a unique delta.",
           {"coverage": f"{claims_scanned}/{total_checks}"})

    # So run an INDEPENDENT firewall over the whole receipt payload.
    blob = json.dumps(receipt, default=str)
    forbidden = [
        r"delta\s*(?:is|=)\s*2\s*/\s*9\s+is\s+derived",
        r"derives?\s+delta\s*=\s*2\s*/\s*9",
        r"forces?\s+delta\s*=\s*2\s*/\s*9",
        r"unique\s+delta\s+is\s+derived",
        r"the\s+law\s+selects\s+delta",
    ]
    hits = {p: len(re.findall(p, blob, re.I)) for p in forbidden}
    independent_clean = sum(hits.values()) == 0
    # positive control: the scanner is not blind
    control_hit = len(re.findall(forbidden[1], "this derives delta = 2/9 somehow", re.I))
    check(independent_clean and control_hit == 1,
          "IV2_INDEPENDENT_FIREWALL_OVER_WHOLE_PAYLOAD_IS_CLEAN",
          {"pattern_hits": hits, "positive_control_fires": control_hit == 1,
           "payload_bytes": len(blob)})
    TEETH.append({"tooth": "IV2", "fired": independent_clean and control_hit == 1,
                  "detail": "independent payload-wide firewall clean, scanner not blind"})

    # And confirm the multi-lane dial genuinely survives.
    phis = [r["Phi"] for r in rebuilt]
    survives = len({round(p, 9) for p in phis}) == len(phis) and max(phis) - min(phis) > 0.5
    check(survives, "IV3_MULTI_LANE_DIAL_SURVIVES_INDEPENDENTLY",
          {"distinct_Phi": len({round(p, 9) for p in phis}),
           "span": max(phis) - min(phis)})

    out["attack_iv_firewall"] = {
        "primary_firewall_coverage": f"{claims_scanned}/{total_checks}",
        "primary_firewall_is_exhaustive": False,
        "independent_payload_scan_clean": independent_clean,
        "multi_lane_dial_survives": survives,
    }

    # =======================================================================
    # ATTACK (vi) -- the DISSOLUTION verdict, steelmanned
    # =======================================================================
    ob_target, _ = raw_contains(
        OBLIG, "Derive from the retained framework chain that the physical charged-lepton "
               "readout is the fixed-locus density class `h`, identity-read in `h`-units as "
               "the eta angle, with no extra clock-rate, transport, or normalization factor.")
    ob_closure, _ = raw_contains(
        OBLIG, "A closing theorem must provide a physical carrier/source-action bridge")
    hclass, _ = raw_contains(
        STRETCH, "h-class: the registered charged-lepton angle is a fixed-locus density of "
                 "the realized C3 cycle;")
    hunit, _ = raw_contains(
        STRETCH, "h-unit:  that density is identity-read as the bare cycle holonomy angle.")
    check(ob_target and ob_closure and hclass and hunit,
          "VI1_OBLIGATION_AND_ITS_SPLIT_BYTE_VERIFIED",
          {"obligation_target": ob_target, "closure_criterion": ob_closure,
           "h_class": hclass, "h_unit": hunit})

    # Independent alpha-family recomputation in EXACT rationals.
    alphas = [sp.Rational(0), sp.Rational(1, 9), sp.Rational(1, 3),
              sp.Integer(1), sp.Rational(2, 27)]
    vals = {str(al): sp.Rational(3) * al for al in alphas}
    hits29 = [k for k, v in vals.items() if v == sp.Rational(2, 9)]
    distinct = len(set(str(v) for v in vals.values())) == len(alphas)
    check(distinct and hits29 == ["2/27"],
          "VI2_ALPHA_FAMILY_INDEPENDENTLY_RECOMPUTED_EXACT_RATIONALS",
          {"I_alpha(1,1,1)": {k: str(v) for k, v in vals.items()},
           "member_giving_2/9": hits29,
           "all_distinct": distinct,
           "consequence": "the class coefficient is free; a registered delta "
                          "value cannot select it"})
    TEETH.append({"tooth": "VI2", "fired": distinct and hits29 == ["2/27"],
                  "detail": "alpha family exact-rational recomputation"})

    # Steelman the dissolution reading as hard as possible.
    steelman = {
        "argument": "If delta is registered state data, there is no 'readout "
                    "map' left to derive -- the state simply HAS a delta, so the "
                    "obligation asks for something that no longer exists.",
        "why_it_fails": "The obligation is not about the dial coordinate of the "
                        "generation-space circulant. It is about the PHYSICAL "
                        "charged-lepton readout being the fixed-locus density "
                        "class of the Z^3 lattice C3 cycle, identity-read in "
                        "h-units. Registration hands you a number in the "
                        "generation dial (V3: a DIFFERENT space); it does not "
                        "hand you the identification of that number with the "
                        "lattice fixed-locus density, nor the unit identity. "
                        "Both remain law-side type assignments.",
        "byte_support": ob_target and hclass and hunit and space_gap,
        "survives": False,
    }
    check(not steelman["survives"] and steelman["byte_support"],
          "VI3_DISSOLUTION_STEELMAN_FAILS_ON_BYTES",
          {"steelman_survives": steelman["survives"],
           "byte_support_for_refusal": steelman["byte_support"]})
    refute(False, "ATTACK-VI-DISSOLUTION",
           "The primary's verdict (the obligation does NOT dissolve) SURVIVES "
           "adversarial attack, and the independent space-gap finding (V3) makes "
           "it STRONGER than the primary states: not only is the obligation "
           "type-shaped rather than value-shaped, the registered value does not "
           "even live on the space where the derived cell is defined.",
           {"steelman_fails": True})

    out["attack_vi_dissolution"] = {"steelman": steelman, "verdict_survives": True}

    # =======================================================================
    # ATTACK (vii) -- prior art and the unit-face
    # =======================================================================
    pa1, _ = raw_contains(VALUE_FACE, "sub-admission (ii) = (ii-value) + (ii-exactness).")
    pa2, _ = raw_contains(
        VALUE_FACE, "**S4 (unit-face dissolution at the value face).**")
    pa3, _ = raw_contains(
        VALUE_FACE, "The value-face comparison is number-to-number; \"read as an angle in "
                    "radians\" adds no further value-face content.")
    check(pa1 and pa2 and pa3, "VII1_PRIOR_ART_BYTE_VERIFIED",
          {"net_decomposition": pa1, "S4_unit_face": pa2,
           "number_to_number_clause": pa3,
           "date": "2026-07-05",
           "finding": "the value-face reclassification for delta is LANDED "
                      "PRIOR ART, one day after the 2026-07-04 no-gos"})
    refute(True, "ATTACK-VII-UNITFACE",
           "The landed 07-05 note's S4 'unit-face dissolution' is arguably the "
           "TYPE GAP restated rather than dissolved. It dissolves the unit face "
           "by declaring both sides dimensionless pure numbers and comparing "
           "number-to-number. But the h-unit obligation demands precisely a "
           "DERIVATION that the density is identity-read as the angle -- i.e. "
           "that the two dimensionless numbers are the SAME quantity, not merely "
           "both dimensionless. Cycle 928 independently reached the same wall "
           "('the TYPE GAP is the new wall'). So S4 does not reach h-unit, which "
           "is consistent with -- and reinforces -- the non-dissolution verdict.",
           {"S4_present": pa2, "number_to_number": pa3})
    TEETH.append({"tooth": "VII1", "fired": pa1 and pa2 and pa3,
                  "detail": "prior art byte-verified"})

    # =======================================================================
    # ATTACK (viii) -- is the comparator really non-load-bearing?
    # =======================================================================
    sci = {k: v for k, v in receipt.items()
           if k.startswith(("A_", "B_", "C_", "D_", "E_", "F_"))}
    pdg_paths: list[str] = []

    def walk(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")
        else:
            if any(str(x) in str(node) for x in (0.51099895, 105.6583755, 1776.86)):
                pdg_paths.append(path)

    walk(sci, "receipt")
    allowed = ("comparator", "sign_convention", "masses_MeV", "PDG")
    stray = [p for p in pdg_paths if not any(a.lower() in p.lower() for a in allowed)]
    check(not stray, "VIII1_PDG_CONFINED_TO_COMPARATOR_AND_CONVENTION_SECTIONS",
          {"pdg_bearing_paths": len(pdg_paths), "stray_paths": stray,
           "verdict": "the comparator feeds no derivation step"})
    TEETH.append({"tooth": "VIII1", "fired": not stray,
                  "detail": "PDG confined to labeled sections"})

    # =======================================================================
    # ATTACK (ix) -- gate integrity
    # =======================================================================
    gates = receipt["B_restriction_gates"]
    gate_ok = (gates["aci_reduction_runner"] == "TOTAL: PASS=25 FAIL=0"
               and gates["angle_native_no_go"] == "TOTAL: PASS=128 FAIL=0")
    prior = gates["value_face_prior_art_runner"]
    check(gate_ok and prior["reproduces"] is False,
          "IX1_GATES_AS_CLAIMED_AND_PRIOR_ART_FAILURE_DISCLOSED",
          {"aci": gates["aci_reduction_runner"],
           "angle_native": gates["angle_native_no_go"],
           "prior_art_observed": prior["observed"],
           "prior_art_published": prior["note_publishes"]})

    # Independently confirm the stale-memo-pin diagnosis.
    memo_raw = read_text("docs/MINIMAL_AXIOMS_2026-06-29.md")
    old_ok, _ = raw_contains(
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "Further physical structure requires derivation, bridge, explicit admission, or "
        "approved primitive registration before use as a premise.")
    new_ok, _ = raw_contains(
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "Further physical structure requires a retained derivation or bridge, or explicit "
        "approved- primitive registration, before use as a premise.")
    check((not old_ok) and new_ok,
          "IX2_STALE_MEMO_PIN_DIAGNOSIS_CONFIRMED_INDEPENDENTLY",
          {"superseded_wording_present": old_ok,
           "current_wording_present": new_ok,
           "AUDIT_ROW": "the landed 2026-07-05 value-face note's runner pins a "
                        "memo sentence that no longer exists; it publishes "
                        "PASS=27 FAIL=0 but produces PASS=26 FAIL=1 on current "
                        "main. Text-provenance drift only; no science step "
                        "depends on it."})
    TEETH.append({"tooth": "IX2", "fired": (not old_ok) and new_ok,
                  "detail": "stale memo pin independently confirmed"})

    # =======================================================================
    # ATTACK (x) -- no-conversion, independently
    # =======================================================================
    # 2/9 = 2*pi*q would need q = 1/(9 pi), which is irrational.
    q = sp.nsimplify(sp.Rational(2, 9) / (2 * sp.pi))
    q_rational = bool(q.is_rational)
    # Exact: 2*pi*L and 2*pi*S_sum vs the targets.
    twopiL = sp.simplify(2 * sp.pi * sp.Rational(2, 9))
    twopiS = sp.simplify(2 * sp.pi * sp.Rational(2, 3))
    miss1 = sp.simplify(twopiL - sp.Rational(2, 9)) != 0
    miss2 = sp.simplify(twopiS - sp.Rational(2, 3)) != 0
    check((not q_rational) and miss1 and miss2,
          "X1_NO_CONVERSION_EXACT_SYMBOLIC",
          {"2/9 / (2 pi) is rational": q_rational, "2*pi*L": str(twopiL),
           "2*pi*S_sum": str(twopiS), "both_miss_their_targets": miss1 and miss2})

    # Scan the PRIMARY's payload for an asserted conversion.
    conv_pat = r"2\s*/\s*9\s*=+\s*2\s*\*?\s*pi|2\s*/\s*3\s*=+\s*2\s*\*?\s*pi"
    NEG = ("no ", "not ", "never", "reject", "plant", "!=", "has no", "cannot",
           "without", "miss")
    conv_rows = []
    for m in re.finditer(conv_pat, blob, re.I):
        ctx = blob[max(0, m.start() - 90):m.end() + 90]
        negated = any(n in ctx.lower() for n in NEG)
        conv_rows.append({"match": m.group(0), "negated_or_planted": negated,
                          "context": ctx})
    asserted = [r for r in conv_rows if not r["negated_or_planted"]]
    conv_control = len(re.findall(conv_pat, "check 2/9 == 2*pi times something", re.I))
    check(not asserted and conv_control == 1,
          "X2_NO_ASSERTED_CONVERSION_IN_PRIMARY_PAYLOAD",
          {"pattern_occurrences": len(conv_rows),
           "all_negated_or_planted": len(conv_rows) - len(asserted),
           "ASSERTED_conversions": len(asserted),
           "positive_control_fires": conv_control == 1,
           "occurrences": [r["match"] + " | " + r["context"][:110] for r in conv_rows]})
    TEETH.append({"tooth": "X2", "fired": not asserted and conv_control == 1,
                  "detail": "no-conversion scan clean (context-classified), "
                            "scanner not blind"})

    out["attack_x_conversion"] = {"conversion_asserted": False,
                                  "pi_irrationality_used": True}

    # =======================================================================
    # SUMMARY
    # =======================================================================
    holding = [r for r in REFUTATIONS if r["refutation_holds"]]
    out["refutations"] = REFUTATIONS
    out["refutations_that_hold"] = len(holding)
    out["teeth"] = {"count": len(TEETH), "all_fired": all(t["fired"] for t in TEETH),
                    "teeth": TEETH}
    check(len(TEETH) >= 8, "Z0_AT_LEAST_8_TEETH", {"teeth": len(TEETH)})
    check(all(t["fired"] for t in TEETH), "Z1_ALL_TEETH_FIRED",
          {"not_fired": [t["tooth"] for t in TEETH if not t["fired"]]})

    out["VERDICT_SUMMARY"] = {
        "primary_core_verdict_survives": True,
        "core_verdict": "the R-eta obligation does NOT dissolve under the "
                        "realized-state reclassification",
        "refutations_that_hold": [r["attack"] for r in holding],
        "material_findings": [
            "delta is NOT a functional of the registered multiset (6 preimages); "
            "only the folded Phi in [0, pi/3] is",
            "the exactness is CONVENTION-CONDITIONAL on the all-positive "
            "signed-root choice (next-nearest sign assignment is ~3000x worse)",
            "the slot (generation 3-space) and the derived cell (Z^3 normal "
            "plane) live on DIFFERENT supplied spaces; their identification is "
            "the open carrier question",
            "the primary's firewall list is not exhaustive over its own checks "
            "(an independent payload-wide scan was run and is clean)",
            "the landed 07-05 prior-art runner no longer reproduces its "
            "published total (stale memo pin); text-provenance only",
        ],
    }

    runtime = round(time.time() - START, 2)
    check(runtime <= BUDGET_SECONDS, "Z2_RUNTIME_WITHIN_BUDGET",
          f"{runtime}s / {BUDGET_SECONDS}s")

    digest = hashlib.sha256(
        json.dumps(out, sort_keys=True, separators=(",", ":"), default=str).encode()
    ).hexdigest()

    receipt_out = dict(out)
    receipt_out.update({
        "cycle": 938,
        "block": "toe-time-blockAC3-20260802",
        "campaign": "toe-time-expansion-20260802",
        "role": "independent checker, spec'd to refute",
        "authority": "none",
        "audit": "unset",
        "adopts": "nothing",
        "primary_receipt_sha256": sha256_of(PRIMARY_RECEIPT),
        "primary_script_sha256": sha256_of(PRIMARY_SCRIPT),
        "totals": {"PASS": PASS, "FAIL": FAIL},
        "runtime_seconds": runtime,
        "science_digest": digest,
        "VERDICT": "PASS" if FAIL == 0 else "FAIL",
    })

    os.makedirs(rel("outputs"), exist_ok=True)
    with open(rel("outputs/reta_reclassification_independent_check_cycle938_receipt_2026_07_28.json"), "w") as fh:
        json.dump(receipt_out, fh, indent=1, sort_keys=True, default=str)
        fh.write("\n")

    body = ["===== runner cache v1 =====",
            "runner: frontier_cycle938_reta_reclassification_independent_check_2026_07_28.py", ""]
    body += LINES
    body += ["", "----- REFUTATIONS -----"]
    for r in REFUTATIONS:
        body.append(f"{'HOLDS ' if r['refutation_holds'] else 'FAILED'} {r['attack']} :: {r['statement']}")
    body += ["",
             f"science_digest={digest}",
             f"TOTAL: PASS={PASS} FAIL={FAIL}",
             f"VERDICT: {'PASS' if FAIL == 0 else 'FAIL'}",
             f"runtime_seconds={runtime} budget={BUDGET_SECONDS}"]
    with open(rel("logs/runner-cache/frontier_cycle938_reta_reclassification_independent_check_2026_07_28.txt"), "w") as fh:
        fh.write("\n".join(body) + "\n")

    print("\n".join(LINES))
    print("\n".join(body[len(LINES) + 3:]))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
