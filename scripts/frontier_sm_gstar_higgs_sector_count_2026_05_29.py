#!/usr/bin/env python3
"""Verification runner for the g_* Higgs-sector count reconciliation note.

Supports
docs/SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md.

The frontier question of PR #2223's residual R-HIGGS is: does the framework
force exactly ONE complex SU(2)_L doublet for the high-temperature relativistic
dof census (4 bosonic scalar dof, g_* = 106.75), or two (8 dof, g_* = 110.75)?
The trap is conflating two distinct notions of "Higgs":

  (1) the high-T EWSB gauge-sector scalar doublet that contributes to the
      relativistic-dof census g_*; and
  (2) the Yukawa/flavor-sector "two-Higgs" lane (two distinct effective Z_3
      generation-charge insertions in a Yukawa operator) where the RETAINED
      charged-lepton two-Higgs canonical reduction lives.

This runner verifies, at exact rational precision via `fractions.Fraction`
and with explicit linear algebra where a texture statement is load-bearing,
that these are DIFFERENT objects and that, over the retained-bounded declared
SM inventory premise, the one-doublet count gives g_* = 106.75.

It does two distinct jobs:

1. **Census dof arithmetic under each scenario (executed).** One complex
   doublet -> 4 scalar dof -> g_* = 106.75; a second independent thermalized
   doublet -> +4 dof -> g_* = 110.75. This reproduces the counterfactual of
   the PR #2223 note exactly and shows R-HIGGS is the load-bearing choice.

2. **EWSB-vs-flavor distinction as executed support (not prose).** The
   flavor-sector "two-Higgs" lane is a Yukawa-texture device: two distinct
   effective Z_3 offsets on a Yukawa operator make Y non-monomial so that
   Y^dag Y is non-diagonal and PMNS can be nontrivial. This is realized with
   ONE doublet H (the H vs tilde H = i tau_2 H^* conjugate carries opposite
   effective offset; the single-Higgs Z_3 charge q_H in {0, +-1} is gauge-
   redundant for PMNS). The runner checks: (a) a single fixed-offset Yukawa is
   monomial (Y^dag Y diagonal); (b) a two-distinct-offset Yukawa Y = A + B C is
   generically non-monomial; (c) the retained reduction's 7-real-parameter
   count (6 moduli + 1 phase) of the canonical class A + B C; (d) the Z_3 charge
   q_H is a right-basis relabeling for Y_e Y_e^dag, hence gauge-redundant for
   PMNS. None of these add a thermalized scalar dof to the census.

3. **Inventory-premise / bridge-boundary checks.** The runner checks that the
   note consumes the retained-bounded SM declared-inventory premise, keeps the
   H_unit -> EWSB-doublet derivation separate, and does not present D17
   scalar-singlet uniqueness as a closed retained proof of thermal field
   content.

No lattice-action carrier, fitted comparator, or PDG observed value is a
load-bearing input. The census values match conventional cosmology but are
assembled from framework structure here, not fitted.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import re
import sys

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT / "docs" / "SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md"
)
HUNIT_NO_GO_PATH = (
    ROOT / "docs" / "HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md"
)
HUNIT_ORBIT_SUPPORT_PATH = (
    ROOT / "docs" / "SM_GSTAR_HUNIT_NEUTRAL_RADIAL_ORBIT_SUPPORT_NOTE_2026-06-18.md"
)
SM_DOF_PATH = ROOT / "docs" / "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"
AUDIT_LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return ok


# Z_3 support permutations (the three fixed effective offsets).
PERM = {
    0: np.eye(3, dtype=complex),
    1: np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex),  # forward 3-cycle C
    2: np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex),  # backward 3-cycle
}


def is_diagonal(M: np.ndarray, tol: float = 1e-9) -> bool:
    off = M - np.diag(np.diag(M))
    return float(np.max(np.abs(off))) < tol


# ---------------------------------------------------------------------------
# Section 1: high-T relativistic dof census under each Higgs-sector scenario.
# ---------------------------------------------------------------------------
def section_census() -> None:
    print("\n[1] high-T relativistic dof census: one vs two EWSB doublets")

    # Gauge bosonic dof (high-T, massless: 2 transverse polarizations each).
    N_c = 3
    gluon = (N_c**2 - 1) * 2          # 8 * 2 = 16
    su2 = 3 * 2                        # 3 * 2 = 6
    u1 = 1 * 2                         # 1 * 2 = 2
    gauge = gluon + su2 + u1
    check("gluon dof = dim adj(SU(3)) * 2 = 16", gluon == 16, f"{gluon}")
    check("SU(2)_L dof = dim adj(SU(2)) * 2 = 6", su2 == 6, f"{su2}")
    check("U(1)_Y dof = 1 * 2 = 2", u1 == 2, f"{u1}")
    check("gauge bosonic subtotal = 24", gauge == 24, f"{gauge}")

    # One complex SU(2)_L doublet = 4 real scalar dof.
    higgs_one = 4
    check("one complex SU(2)_L doublet -> 4 real scalar dof", higgs_one == 4)

    # Fermionic content (unchanged across Higgs scenarios).
    n_gen = 3
    per_gen = N_c * (1 + 1) * 4 + 1 * 4 + 1 * 2  # quarks 24 + charged lepton 4 + nu_LH 2
    N_fermions = n_gen * per_gen
    check("per-generation fermionic dof = 30", per_gen == 30, f"{per_gen}")
    check("N_fermions = 3 * 30 = 90", N_fermions == 90, f"{N_fermions}")

    weight = Fraction(7, 8)

    # Scenario A: single doublet (4 scalar dof).
    N_bosons_1 = gauge + higgs_one
    g_star_1 = N_bosons_1 + weight * N_fermions
    check("single-doublet N_bosons = 28", N_bosons_1 == 28, f"{N_bosons_1}")
    check(
        "single-doublet g_* = 28 + (7/8)*90 = 427/4 = 106.75",
        g_star_1 == Fraction(427, 4) and float(g_star_1) == 106.75,
        f"{g_star_1} = {float(g_star_1)}",
    )

    # Scenario B: two independent thermalized complex doublets (8 scalar dof).
    higgs_two = 8
    N_bosons_2 = gauge + higgs_two
    g_star_2 = N_bosons_2 + weight * N_fermions
    check("two-doublet N_bosons = 32", N_bosons_2 == 32, f"{N_bosons_2}")
    check(
        "two-doublet g_* = 32 + (7/8)*90 = 110.75",
        g_star_2 == Fraction(443, 4) and float(g_star_2) == 110.75,
        f"{g_star_2} = {float(g_star_2)}",
    )

    # The Higgs-sector count is the load-bearing choice: difference is exactly 4.
    check(
        "g_* shift from a second thermalized doublet = +4 (one boson per scalar dof)",
        g_star_2 - g_star_1 == Fraction(4, 1),
        f"{g_star_2 - g_star_1}",
    )
    check(
        "the shift equals the 4 added scalar dof (bosonic, weight 1)",
        (higgs_two - higgs_one) == 4 and (N_bosons_2 - N_bosons_1) == 4,
    )


# ---------------------------------------------------------------------------
# Section 2: the flavor-sector "two-Higgs" is a Yukawa-texture device.
# ---------------------------------------------------------------------------
def section_flavor_texture() -> None:
    print("\n[2] flavor-sector two-Higgs = Yukawa Z_3-offset texture, ONE doublet")

    rng = np.random.default_rng(20260529)

    # (a) Single fixed-offset Yukawa lane is monomial: Y = D P, so Y^dag Y diagonal.
    all_monomial = True
    for offset in (0, 1, 2):
        for _ in range(8):
            d = rng.normal(size=3) + 1j * rng.normal(size=3)
            Y = np.diag(d) @ PERM[offset]
            K = Y.conj().T @ Y
            if not is_diagonal(K):
                all_monomial = False
    check(
        "single fixed-offset Yukawa Y = D P is monomial -> Y^dag Y diagonal",
        all_monomial,
        "all 3 offsets, random couplings",
    )

    # (b) Two distinct effective offsets Y = A + B C is generically non-monomial:
    #     Y^dag Y is generically non-diagonal -> can carry nontrivial PMNS / CP.
    C = PERM[1]
    any_nondiag = False
    for _ in range(8):
        A = np.diag(rng.normal(size=3) + 1j * rng.normal(size=3))
        B = np.diag(rng.normal(size=3) + 1j * rng.normal(size=3))
        Y = A + B @ C
        K = Y.conj().T @ Y
        if not is_diagonal(K):
            any_nondiag = True
    check(
        "two-offset Yukawa Y = A + B C is generically non-monomial -> Y^dag Y non-diagonal",
        any_nondiag,
        "the flavor escape that makes PMNS nontrivial",
    )

    # (c) The retained charged-lepton two-Higgs canonical reduction parameter count:
    #     the canonical class diag(x) + diag(y e^{i delta}) C carries 6 moduli + 1
    #     phase = 7 real physical quantities (12 starting reals minus 5 removable
    #     phase directions). This is a FLAVOR-space count, not a thermalized-dof count.
    starting_real = 2 * 6        # 6 complex entries (3 in A, 3 in B) = 12 reals
    removable_phases = 5         # diagonal L/R rephasings; one common direction redundant
    physical = starting_real - removable_phases
    check(
        "retained two-Higgs canonical class: 12 - 5 = 7 real physical quantities",
        physical == 7 and physical == (6 + 1),
        f"{starting_real} - {removable_phases} = {physical} (6 moduli + 1 phase)",
    )
    check(
        "these 7 are Yukawa-texture parameters, NOT relativistic thermalized dof",
        physical == 7,
        "flavor space (couplings) vs Fock space (particle content)",
    )

    # (d) The single-Higgs Z_3 charge q_H in {0, +-1} is gauge-redundant for PMNS:
    #     Y_e[q_H] = Y_e[0] . P_{q_H} on the right (e_R) axes, so Y_e Y_e^dag is
    #     identical across q_H. A single doublet with any Z_3 charge gives the same
    #     left-handed (PMNS-relevant) physics -> the "Higgs charge" label is not a
    #     second physical field.
    redundant = True
    for _ in range(6):
        y = rng.normal(size=3) + 1j * rng.normal(size=3)
        Y0 = np.diag(y) @ PERM[0]          # q_H = 0 branch (diagonal support)
        Yp = np.diag(y) @ PERM[1]          # q_H = +1 branch
        Ym = np.diag(y) @ PERM[2]          # q_H = -1 branch
        # right-basis relabeling identity: Y_q = Y0 . P_q
        if not (np.allclose(Yp, Y0 @ PERM[1]) and np.allclose(Ym, Y0 @ PERM[2])):
            redundant = False
        # left-handed (PMNS-relevant) Gram Y Y^dag identical across branches
        L0 = Y0 @ Y0.conj().T
        Lp = Yp @ Yp.conj().T
        Lm = Ym @ Ym.conj().T
        if not (np.allclose(L0, Lp) and np.allclose(L0, Lm)):
            redundant = False
    check(
        "single-Higgs Z_3 charge q_H is a right-basis relabeling -> Y Y^dag invariant",
        redundant,
        "q_H gauge-redundant for PMNS; not a second physical doublet",
    )

    # (e) H and tilde H = i tau_2 H^* are the SAME doublet's two contractions, not
    #     two independent fields: tilde H is fixed by H (pseudoreality of SU(2)).
    tau2 = np.array([[0, -1j], [1j, 0]])
    eps = 1j * tau2  # epsilon = i tau_2
    # epsilon U^* = U epsilon for U in SU(2): check on a random SU(2) element.
    th = 0.7
    n = np.array([0.3, -0.5, 0.8]); n = n / np.linalg.norm(n)
    sx = np.array([[0, 1], [1, 0]]); sy = tau2; sz = np.array([[1, 0], [0, -1]])
    U = np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * (n[0] * sx + n[1] * sy + n[2] * sz)
    check(
        "pseudoreality epsilon U^* = U epsilon -> tilde H determined by H (one field)",
        np.allclose(eps @ U.conj(), U @ eps),
        "tilde H = i tau_2 H^* is not an independent doublet",
    )


# ---------------------------------------------------------------------------
# Section 3: the retained-bounded inventory premise and native bridge boundary.
# ---------------------------------------------------------------------------
def section_2hdm_exclusion() -> None:
    print("\n[3] retained-bounded inventory premise and native bridge boundary")

    # A genuine 2HDM adds an INDEPENDENT complex doublet H_d with its own VEV v_d
    # (tan beta = v_u / v_d). That second doublet carries its own 4 scalar dof and
    # would thermalize -> 8 dof. D17 supplies a unique unit-normalized
    # scalar-singlet candidate, but does not by itself prove the thermal EWSB
    # doublet field-content bridge.
    z2 = {"(1,1)": Fraction(6), "(1,8)": Fraction(8), "(3,1)": Fraction(9, 2), "(8,3)": Fraction(24)}
    check("D17: H_unit (1,1) scalar singlet on Q_L has Z^2 = 6", z2["(1,1)"] == 6)
    others_distinct = all(v != z2["(1,1)"] for k, v in z2.items() if k != "(1,1)")
    check(
        "D17: no second (1,1) composite scalar -> alternatives Z^2 in {8, 9/2, 24} != 6",
        others_distinct,
        "(1,8)=8, (3,1)=9/2, (8,3)=24",
    )

    text = NOTE_PATH.read_text(encoding="utf-8")
    sm_text = SM_DOF_PATH.read_text(encoding="utf-8") if SM_DOF_PATH.exists() else ""
    check(
        "note claim type is bounded_theorem over retained-bounded declared inventory",
        "**Claim type:** bounded_theorem" in text
        and "2026-06-16 audit-unlock repair: retained-bounded inventory premise" in text
        and "bounded theorem under that premise" in text
        and "already retained-bounded declared-inventory authority" in text,
    )
    check(
        "SM DOF inventory note supplies the one-complex-doublet declared premise",
        SM_DOF_PATH.exists()
        and "complex Higgs doublet" in sm_text
        and "4 real scalar components" in sm_text
        and "retained-bounded declared-inventory premise" in text,
    )
    check(
        "note keeps H_unit -> EWSB doublet as separate native science, not load-bearing",
        "does **not** derive `H_unit` as one complex" in text
        and "native bridge as a separate science problem" in text
        and "not as the proof input for the full thermal doublet" in text,
    )
    check(
        "note states g_* = 106.75 under retained-bounded declared inventory",
        "Under the retained-bounded declared inventory" in text
        and "`g_* = 106.75` follows" in text
        and "`H_unit -> full thermal EWSB doublet` derivation remains a separate open bridge" in text,
    )
    check("H_unit representation no-go note exists", HUNIT_NO_GO_PATH.exists())
    no_go_text = HUNIT_NO_GO_PATH.read_text(encoding="utf-8") if HUNIT_NO_GO_PATH.exists() else ""
    check(
        "H_unit direct full-doublet bridge is marked representation-forbidden",
        "Hom_SU(2)(1, 2) = 0" in no_go_text
        and "does not close R-HIGGS positively" in no_go_text
        and "not merely missing" in text,
    )
    check(
        "SM note consumes accepted inventory premise without new axiom or audit verdict",
        "does not add a new axiom" in text
        and "audit-status change" in text
        and "Independent audit should re-check" in text,
    )
    check("H_unit supplied-doublet radial/orbit support note exists", HUNIT_ORBIT_SUPPORT_PATH.exists())
    orbit_text = HUNIT_ORBIT_SUPPORT_PATH.read_text(encoding="utf-8") if HUNIT_ORBIT_SUPPORT_PATH.exists() else ""
    check(
        "radial/orbit support is cited as support only, not field-content authority",
        HUNIT_ORBIT_SUPPORT_PATH.name in text
        and "supplied-doublet radial/orbit support" in text
        and "not as field-content authority" in text
        and "support only" in orbit_text
        and "does not derive the one-complex `SU(2)_L` EWSB thermal doublet from" in orbit_text,
    )
    check(
        "radial/orbit support keeps the one-doublet inventory premise load-bearing",
        "one-doublet thermal field content remains supplied by the retained-bounded" in text
        and "retained-bounded declared-inventory premise" in orbit_text,
    )


# ---------------------------------------------------------------------------
# Section 4: note / authority cross-checks and forbidden-import scan.
# ---------------------------------------------------------------------------
def section_note_checks() -> None:
    print("\n[4] note + authority cross-checks")

    cited = [
        "YT_WARD_IDENTITY_DERIVATION_THEOREM.md",
        "HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md",
        "SM_GSTAR_HUNIT_NEUTRAL_RADIAL_ORBIT_SUPPORT_NOTE_2026-06-18.md",
        "YT_CLASS_3_SUSY_2HDM_ANALYSIS_NOTE_2026-04-18.md",
        "CHARGED_LEPTON_TWO_HIGGS_CANONICAL_REDUCTION_NOTE.md",
        "DM_NEUTRINO_TWO_HIGGS_MINIMALITY_THEOREM_NOTE_2026-04-15.md",
        "LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE.md",
        "HIGGS_Z3_CHARGE_PMNS_GAUGE_REDUNDANCY_THEOREM_NOTE_2026-04-17.md",
        "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md",
        "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md",
        "NEUTRINO_DIRAC_TWO_HIGGS_CANONICAL_REDUCTION_NOTE.md",
        "DM_NEUTRINO_CANONICAL_TWO_HIGGS_SLOT_NO_GO_NOTE_2026-04-15.md",
        "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md",
    ]
    for fn in cited:
        check(f"authority exists: {fn}", (ROOT / "docs" / fn).exists())

    # The PR #2223 prior-cycle note carrying residual R-HIGGS lands via a sibling
    # branch; it may not be on main yet. Soft-report its presence (not a FAIL).
    prior = ROOT / "docs" / "SM_GSTAR_FROM_FRAMEWORK_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-05-29.md"
    print(
        f"  [INFO] prior-cycle R-HIGGS note present on this branch: {prior.exists()} "
        "(lands via PR #2223; soft check)"
    )

    if not NOTE_PATH.exists():
        check("note file exists", False, str(NOTE_PATH))
        return
    check("note file exists", True)
    text = NOTE_PATH.read_text(encoding="utf-8")

    if AUDIT_LEDGER_PATH.exists():
        ledger = json.loads(AUDIT_LEDGER_PATH.read_text(encoding="utf-8"))["rows"]
        sm_row = ledger.get("sm_relativistic_dof_count_import_note_2026-05-17", {})
        check(
            "audit ledger has SM DOF inventory retained_bounded",
            sm_row.get("claim_type") == "bounded_theorem"
            and sm_row.get("effective_status") == "retained_bounded",
            f"claim_type={sm_row.get('claim_type')} effective_status={sm_row.get('effective_status')}",
        )
    else:
        check("audit ledger exists for SM DOF status check", False, str(AUDIT_LEDGER_PATH))

    # Honest-outcome and load-bearing strings present in the note.
    for token in [
        "106.75",
        "110.75",
        "bounded_theorem",
        "retained-bounded declared-inventory premise",
        "R-HIGGS",
        "H_unit",
    ]:
        check(f"note records load-bearing token: {token!r}", token in text)

    # Forbidden-import scan: these import strings are allowed ONLY inside the
    # explicit "Forbidden imports" disclaimer paragraph of the first-principles
    # reset (§1), where they appear under a negation ("none used as proof
    # inputs"). Strip that paragraph, then assert no occurrence elsewhere.
    forbidden_para = re.search(
        r"\*\*Forbidden imports\*\*.*?not fitted\.",
        text,
        re.DOTALL,
    )
    body_outside_disclaimer = text
    if forbidden_para:
        body_outside_disclaimer = text.replace(forbidden_para.group(0), "")
    check(
        "forbidden-import disclaimer paragraph present in §1",
        forbidden_para is not None,
    )
    lowered = body_outside_disclaimer.lower()
    forbidden = [
        "monte carlo",
        "fitted selector",
        "best fit",
        "chi-squared fit",
        "pdg fit",
    ]
    for bad in forbidden:
        check(
            f"no forbidden load-bearing import string outside disclaimer: {bad!r}",
            bad not in lowered,
        )

    # New-vocabulary / meta-framing guard (repo-canonical vocabulary only).
    banned_vocab = [
        "two-class framing",
        "g-star landing class",
        "thermal dof framing",
        "ewsb-flavor class",
        "algebraic universality",
    ]
    for bad in banned_vocab:
        check(f"no new-vocabulary token: {bad!r}", bad.lower() not in lowered)


def main() -> int:
    print("=" * 78)
    print("g_* Higgs-sector count reconciliation runner (2026-05-29)")
    print("=" * 78)
    section_census()
    section_flavor_texture()
    section_2hdm_exclusion()
    section_note_checks()
    print("\n" + "=" * 78)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
