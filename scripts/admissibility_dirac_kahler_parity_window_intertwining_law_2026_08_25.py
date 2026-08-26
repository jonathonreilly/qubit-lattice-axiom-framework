#!/usr/bin/env python3
"""BLOCK 193 -- THE PARITY-RESOLVED WINDOW LAW OF THE INTERTWINING RESIDUAL,
AND THE BILINEAR MECHANISM THAT PRODUCES IT.

THE RESULT, AND ITS EXACT SCOPE.  On BLOCK 190's wrap-edge width family at the
SAME fixture (m, c) = (9/20, 5/13), at TWO widths T = 16 and T = 20, the
first-order intertwining residual R = dL_2 - dK_c W of Block 192's Hodge-volume
tangent is resolved into a closed-form BILINEAR FORM, and the exact set of
one-cell sources that make it nonzero is determined: a THREE-SLICE WINDOW whose
position depends on the core's PARITY.  ALL OF IT IS FINITE EXACT LINEAR
ALGEBRA ON ONE CONSTRUCTED MATRIX FAMILY.  NONE OF IT ESTABLISHES A LIGHT CONE,
A CAUSAL STRUCTURE, A PROPAGATION SPEED, A LOCALITY PRINCIPLE OR A CONTINUUM
LIMIT.  'WINDOW', 'TRANSPORT', 'HARMONIC' AND 'RESPONSE' NAME PROPERTIES OF
EXACT RATIONAL MATRICES AND OF NOTHING ELSE, AND THEY ARE FENCED BEFORE THE
FIRST NUMBER IS READ.

  0. THE EQUIVALENCE, BOTH DIRECTIONS (C).  W(delta) = W(0) matrix-exact if and
     only if R = dL_2 - dK_c W = 0.  Measured on the FULL twenty-entry
     (bump, core) table at T = 16 and at THREE exact amplitudes
     delta = 1/5, 1/3, 2/5 -- sixty finite rebuilds against twenty first-order
     residuals, and the first-order table and all three finite tables are the
     SAME TABLE ENTRY FOR ENTRY, not merely the same zero set.  The adversarial
     check's six requested cells are three zeros and three nonzeros inside it,
     and Block 192's three landed cutoff pairs are gated as INSTANCES.

  1. THE HARMONIC-RESPONSE DERIVATION, IN THREE PILLARS (D).  Let
     d_b = e_{(t_b+2, x_b)} - sum_b' W[b', b] e_{(t_b', x_b')} be the TWO-STEP
     TRANSPORT DEFECT of the b-th core column.  Then (i) K_c W = L_2 is
     EXACTLY the statement d_b^T G[:, theta_a] = 0 for the eight unperturbed
     core columns -- W is DEFINED by it, not fitted; (ii) the response field
     rho_a = G dQ G[:, theta_a] satisfies Q rho_a = dQ G[:, theta_a], so it is
     Q-harmonic on every row where the source vanishes, and its row support
     equals the FULL row support of dQ with no cancellation in all 240 tested
     columns; and (iii) R[a, b] = -d_b^T rho_a, so R = 0 is EXACTLY the
     statement that the response field obeys the same defect relation as the
     unperturbed columns.  Since R = K_c dW, R = 0 if and only if dW = 0.

  2. THE BILINEAR FORM, AND IT IS THE MECHANISM (D).  Writing u_b = G^T d_b,

         R[a, b]  =  - u_b^T dQ G[:, theta_a],

     so R is LINEAR in the Hodge tangent and the whole law is a statement about
     the SUPPORT of the eight vectors u_b.  Measured: the union of the slice
     supports of u_1 .. u_8 is EXACTLY THREE SLICES at every valid core and at
     both widths, and for a raw Hodge-tangent matrix unit E_{p,q} the residual
     is nonzero if and only if the ROW p lies on one of those three slices --
     for EVERY column q, 65280 units, ZERO mismatches.

  3. THE PARITY-RESOLVED WINDOW LAW (E).  That three-slice window is

         W(t0) = [2*floor(t0/2) + 1,  2*floor(t0/2) + 3]
               = [t0, t0+2]     for ODD  t0,
               = [t0+1, t0+3]   for EVEN t0.

     A reflected one-cell source at anchor s carries dH rows exactly on the
     slices {s, s+1}, so it breaks the identity if and only if
     {s, s+1} meets W(t0), i.e. s in [2*floor(t0/2), 2*floor(t0/2) + 3].
     Measured on 40 cells at T = 16 and 70 cells at T = 20, spatially uniform
     in all four anchors.  THE CORE'S FOOTPRINT IS FOUR SLICES {t0 .. t0+3} AND
     THE WINDOW IS ALWAYS THREE OF THEM: the LAST predicted slice t0+3 is
     exempt at odd cores, the FIRST read slice t0 is exempt at even cores.
     THE EXEMPT END SWITCHES WITH PARITY.  This REFUTES the parity-independent
     window the solve proposed and is the adversarial check's P2 discovery,
     carried here as the block's central law.

  4. THE EXEMPTION, ATTACKED EXHAUSTIVELY, AND ITS DUAL (E).  At the odd cores
     the t0+3 exemption survives every attack: the admissible one-cell tangent
     at all four spatial anchors, all SIXTEEN 4x4 cell-block directions
     including the asymmetric ones, and every raw matrix unit whose row lies on
     any positive slice from t0+3 through T/2 with an ARBITRARY column --
     1280/1280 at t0 = 1 and 768/768 at t0 = 3.  At the even cores that same
     exemption is REFUTED, measured: the t0+3 cell breaks with nnz(R) = 32, and
     256 of 1024 raw directions break at t0 = 2 and 256 of 512 at t0 = 4.  What
     the even cores have instead is the DUAL exemption at the low end, and it
     is exhaustive there: 768/768 at t0 = 2 and 1280/1280 at t0 = 4.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY.  NO
LOCALITY AND NO LIGHT CONE: the window is a statement about which exact
rational matrices are zero, and no propagation speed, causal structure or
screening length is supplied.  NO PARITY-INDEPENDENT WINDOW: the solve's
version is FALSE and is carried as a refutation.  NO PROOF FROM THE RECURRENCE:
the law is REDUCED to two measured support facts, and the closed form of the
supports is MEASURED at two widths, not derived.  NO CONTINUUM.  NO TRANSFER
OPERATOR.  NO GENERALITY: one fixture, two widths, one profile family.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 192 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: seven imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, locality/light-cone, the parity-independent
     window, the continuum limit, the transfer operator, a proof from the
     recurrence and generality ALL declared NOT CLAIMED as measured constants,
     and ten gravity structures enumerated as NOT SUPPLIED.
  C  THE EQUIVALENCE: the import's symbolic derivative and the displayed shear
     law; the covariance and inverse residuals at BOTH widths; the
     defect-functional route against the FULL dG route; the twenty-entry
     first-order table; the sixty-entry finite table at three amplitudes,
     entry for entry; the biconditional over all sixty; the check's six cells;
     and Block 192's three cutoff pairs as instances.
  D  THE DERIVATION: the transport identity as the DEFINITION of W at every
     core and both widths; the dQ row supports; the response support with no
     cancellation over 240 columns; Q-harmonicity; the response relation
     equal to -R over 30 matrix checks; the raw-unit closed form; and
     R = K_c dW with nnz(dW) = nnz(R) at all 40 cells.
  E  THE PARITY-RESOLVED WINDOW LAW: the 40-cell table at T = 16 and the
     70-cell table at T = 20 with spatial uniformity; the parity switch and
     its unified floor form; the break-density fingerprint; the odd-core
     exemption census; the even-core refutation and the dual exemption; the
     two measured support facts; the raw-unit law over 65280 units; the
     validity boundary; and the exact unexpected-break witness.
  F  the note at its final path, the N5 fence byte-identical, and the
     nsimplify count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through F PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-six declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family census is
  A 2, B 8, C 8, D 7, E 9, F 2.
  FIVE OF THE THIRTY-SIX GUARD CORRECTIONS RATHER THAN RESULTS:
  claim_parity_independent asserts the refuted parity-independent window;
  claim_law_proved asserts a proof this block does not have;
  break_even_refutation asserts that the odd-core exemption survives at even
  cores; break_break_density asserts a uniform break density; and
  break_validity_boundary asserts that the law needs no validity rule.

RUNNING
  python3 scripts/admissibility_dirac_kahler_parity_window_intertwining_law_2026_08_25.py
  python3 ... --list-mutations
  python3 ... --mutation break_even_refutation
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT, LANDED, AND IT IS EXACTLY ONE OBJECT: the Block 105
# shear_hodge() re-exported by the Block 128 module, read at a SYMBOLIC volume
# exactly as Block 192 read it, so that the tangent this block perturbs by is
# pinned to the landed law rather than transcribed.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_PARITY_WINDOW_INTERTWINING_LAW_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 192 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 191 tip.
BLOCK192_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HYBRIDIZATION_MECHANISM_SUPPORT_CUTOFF_"
    "BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
BLOCK192_RUNNER = (
    "scripts/admissibility_dirac_kahler_hybridization_mechanism_support_"
    "cutoff_2026_08_25.py"
)
PARENT_ARTIFACTS = (BLOCK192_NOTE, BLOCK192_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "872758cbd317dcbcfe3b3350d600fe148c45b0fe",   # Block 192 note
    "d9cd520980d8a6288fa448d83e3a6d9c5f905af8",   # Block 192 runner
)
# THE CONSTRUCTION AUTHORITY: Block 190's width family, whose carrier, cores and
# monodromy are carried unchanged; Block 191's volume profile; Block 105's
# primary, whose shear_hodge(c, v) is the one imported object; and Block 188's
# site route, which the width family is a disclosed variant of.
BLOCK191_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK190_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK105_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK188_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PARITY_WINDOW_INTERTWINING_LAW_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HYBRIDIZATION_MECHANISM_SUPPORT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_hybridization_mechanism_support_cutoff_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 192 RUNNER AND RE-RESOLVED AT
# DRAFT TIME; the main pin is re-verified live before the branch is cut.
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block192-"
              "hybridization-mechanism-20260825")
PARENT_COMMIT = "afb66fc43c8858cc6a1d4cf943a14085e45be3f1"
# The Block 191 tip: a real ancestor of HEAD that predates Block 192 and
# therefore carries NEITHER Block 192 artifact.
STALE_PARENT_COMMIT = "36f54ab2ad6e51cbe2bf6b8b604b63236f2c936e"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_locality_supplied",
    "claim_parity_independent",
    "claim_continuum_limit",
    "claim_transfer_operator",
    "claim_law_proved",
    "claim_generality",
    "break_import_derivative",
    "break_carrier_controls",
    "break_defect_route",
    "break_first_order_table",
    "break_finite_table",
    "break_equivalence",
    "break_six_cells",
    "break_cutoff_instances",
    "break_transport_identity",
    "break_source_rows",
    "break_response_support",
    "break_harmonic_response",
    "break_response_relation",
    "break_unit_closed_form",
    "break_dw_link",
    "break_window_sixteen",
    "break_window_twenty",
    "break_parity_switch",
    "break_break_density",
    "break_odd_exemption",
    "break_even_refutation",
    "break_support_facts",
    "break_raw_unit_law",
    "break_validity_boundary",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_locality_supplied": "B",
    "claim_parity_independent": "B",
    "claim_continuum_limit": "B",
    "claim_transfer_operator": "B",
    "claim_law_proved": "B",
    "claim_generality": "B",
    "break_import_derivative": "C",
    "break_carrier_controls": "C",
    "break_defect_route": "C",
    "break_first_order_table": "C",
    "break_finite_table": "C",
    "break_equivalence": "C",
    "break_six_cells": "C",
    "break_cutoff_instances": "C",
    "break_transport_identity": "D",
    "break_source_rows": "D",
    "break_response_support": "D",
    "break_harmonic_response": "D",
    "break_response_relation": "D",
    "break_unit_closed_form": "D",
    "break_dw_link": "D",
    "break_window_sixteen": "E",
    "break_window_twenty": "E",
    "break_parity_switch": "E",
    "break_break_density": "E",
    "break_odd_exemption": "E",
    "break_even_refutation": "E",
    "break_support_facts": "E",
    "break_raw_unit_law": "E",
    "break_validity_boundary": "E",
    "drop_n5_fence": "F",
    "break_nsimplify_absence": "F",
}
MUTATED_FAMILIES = "ABCDEF"


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict[str, bool] = {}
        for key, _, value in self.results:
            family = key.split("-", 1)[0]
            summary[family] = summary.get(family, True) and value
        return summary

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print("GATES " + " ".join(
            f"{family}={'PASS' if value else 'FAIL'}"
            for family, value in self.families().items()))

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC).strip()


def worktree_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", path), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def commit_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC).returncode == 0


def is_hash(value: str) -> bool:
    import re as _re
    return _re.fullmatch(r"[0-9a-f]{40}", value) is not None


def is_placeholder(value: str) -> bool:
    return is_hash(value) and value.startswith("0" * 30)


def audit_inputs_readable() -> tuple:
    missing = tuple(
        path for path in AUDIT_INPUT_PATHS
        if path != SELF_NOTE_INPUT and not (ROOT / path).is_file())
    return len(AUDIT_INPUT_PATHS) - 1 - len(missing), missing


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    machinery_import_landed: bool
    inputs_readable: int
    inputs_missing: tuple


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT):
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB)
    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(commit_blob(parent, p) for p in PARENT_ARTIFACTS)
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, p) for p in PARENT_ARTIFACTS)
    readable, missing = audit_inputs_readable()
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT),
        bool(is_hash(parent) and is_ancestor(parent, "HEAD")
             and (is_placeholder(PARENT_COMMIT)
                  or resolve_ref(PARENT_REF) == PARENT_COMMIT)),
        bool(len(committed_blobs) == len(PARENT_ARTIFACTS) == 2
             and all(is_hash(v) for v in committed_blobs)
             and committed_blobs == worktree_blobs
             and committed_blobs == PARENT_ARTIFACT_BLOBS),
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        MACHINERY_IMPORT_LANDED,
        readable,
        missing)


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
IMPOSED_OBJECTS = (
    "BLOCK 190's WRAP-EDGE WIDTH FAMILY, CARRIED UNCHANGED THROUGH BLOCKS 191 AND 192 AND STILL A DISCLOSED VARIANT OF BLOCK 188's SITE CONSTRUCTION, NOW AT TWO WIDTHS: the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13), read at T = 16 AND at T = 20",
    "BLOCK 191's VOLUME PROFILE AND BLOCK 192's BUMP FAMILY, BOTH CARRIED UNCHANGED: a map v from the positive anchors {0..T/2-1} to the positive rationals, placed as B(c, v(t)) for t < T/2 and as the P_4 image of the block of its thA_s(t) = -1-t partner for t >= T/2, assembled by the quarter-weighted four-corner cell average; and the one-parameter family v = 1 - delta on a chosen pair of adjacent positive anchors, evaluated at the THREE exact amplitudes delta = 1/5, 1/3 and 2/5",
    "THE REFLECTED ONE-CELL HODGE TANGENT, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT: dH(s, x) = E(s,x) dB E(s,x)^T / 4 + E(thA_s(s), x) P_4 dB P_4^T E(thA_s(s), x)^T / 4, a SINGLE cell at the positive anchor s and spatial anchor x together with its thA_s image partner -- CHOSEN BY THIS BLOCK AND DERIVED FROM NOTHING, and summing over s in a bump and over all four x reproduces Block 192's bump tangent IDENTICALLY",
    "THE PROBE DOMAIN: cell anchors s = 0 .. T/2-1 at all four spatial anchors, and cores t0 = 1 .. T/2-1 with Block 191's touch/cross validity rule t0 + 3 <= T/2 -- FORTY cells at T = 16 and SEVENTY at T = 20; TWO WIDTHS ARE NOT A SCAN AND ONE FIXTURE IS NOT A FAMILY",
    "THE PAIR CORES AND THEIR SHIFTED PAIRINGS, BLOCK 190's OBJECTS UNCHANGED: K_c[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)], L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, and the UNIT-CELL MONODROMY W = K_c^-1 L_2 -- NOT a derived transfer operator of any theory, and explicitly NOT repaired as one by this block",
    "THE TWO-STEP TRANSPORT DEFECT FUNCTIONALS d_b AND u_b = G^T d_b, BUILT HERE FROM W AND FROM NOTHING ELSE: d_b = e_{(t_b+2, x_b)} - sum_b' W[b',b] e_{(t_b', x_b')} in the T*4-dimensional carrier, so that K_c W = L_2 is EXACTLY d_b^T G[:, theta_a] = 0 -- an IDENTITY OF THE DEFINITION and not a fitted relation",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE AT A SYMBOLIC VOLUME -- THE ONLY OBJECT IMPORTED, and its delta-derivative dB is the tangent every source in this block is built from",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SEVEN ARE FALSE
# AND STAY FALSE.  THE THIRD IS THE ONE THE ADVERSARIAL CHECK REFUTED.
GRAVITY_SUPPLIED_CLAIMED = False
LOCALITY_SUPPLIED_CLAIMED = False
PARITY_INDEPENDENT_WINDOW_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
TRANSFER_OPERATOR_CLAIMED = False
LAW_PROVED_FROM_RECURRENCE_CLAIMED = False
GENERALITY_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function",
    "shift vector",
    "ADM phase space",
    "Hamiltonian constraint",
    "momentum/diffeomorphism constraint",
    "first-class constraint algebra",
    "Dirac closure",
    "Dirac observable",
    "gauge orbit and its quotient",
    "Osterwalder-Schrader reconstruction of a transfer operator",
)
CHECK_VERDICT = "CORE-CONFIRMED-PARITY-EXTENSION-REFUTED-AND-FOLDED-AS-THE-LAW"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
WIDTHS = (16, 20)
SPACE_EXTENT = 4
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)
BUMP_VOLUME = sp.Rational(4, 5)
BUMPS = ((1, 2), (2, 3), (3, 4), (4, 5))
AMPLITUDES = (sp.Rational(1, 5), sp.Rational(1, 3), sp.Rational(2, 5))

# --- C: THE EQUIVALENCE -----------------------------------------------------
# dB = d/d(delta) shear_hodge(c, 1 - delta) at delta = 0, Block 192's displayed
# tangent, re-gated here against the SYMBOLIC derivative of the import because
# every source in this block is built from it.
DISPLAYED_VOLUME_DERIVATIVE = sp.Matrix([
    [-1, 0, 0, 0],
    [0, sp.Rational(-169, 144), sp.Rational(65, 144), 0],
    [0, sp.Rational(65, 144), sp.Rational(-169, 144), 0],
    [0, 0, 0, 1]])
DISPLAYED_HODGE_UNIT = sp.Matrix([
    [1, 0, 0, 0],
    [0, sp.Rational(169, 144), sp.Rational(-65, 144), 0],
    [0, sp.Rational(-65, 144), sp.Rational(169, 144), 0],
    [0, 0, 0, 1]])
DISPLAYED_HODGE_BUMP = sp.Matrix([
    [sp.Rational(4, 5), 0, 0, 0],
    [0, sp.Rational(169, 180), sp.Rational(-13, 36), 0],
    [0, sp.Rational(-13, 36), sp.Rational(169, 180), 0],
    [0, 0, 0, sp.Rational(5, 4)]])
# THE CARRIER CONTROLS at BOTH widths: the ONE exact inverse closes, and the
# baseline is Ps-covariant.
CARRIER_CONTROLS = {16: (0, 0, 0), 20: (0, 0, 0)}
# THE DEFECT-FUNCTIONAL ROUTE against the FULL dG route, at ten gate pairs.
DEFECT_ROUTE_RESIDUAL = 0
DEFECT_ROUTE_GATE_PAIRS = 10
# nnz(R) OVER THE TWENTY VALID (bump, core) PAIRS at T = 16.  The three ZEROS at
# the odd cores are Block 192's landed cutoff table; the even cores are new, and
# ({4,5}, t0=2) breaks at HALF DENSITY.
FIRST_ORDER_TABLE = {
    ((1, 2), 1): 64, ((1, 2), 2): 64, ((1, 2), 3): 64,
    ((1, 2), 4): 0, ((1, 2), 5): 0,
    ((2, 3), 1): 64, ((2, 3), 2): 64, ((2, 3), 3): 64,
    ((2, 3), 4): 0, ((2, 3), 5): 0,
    ((3, 4), 1): 64, ((3, 4), 2): 64, ((3, 4), 3): 64,
    ((3, 4), 4): 64, ((3, 4), 5): 64,
    ((4, 5), 1): 0, ((4, 5), 2): 32, ((4, 5), 3): 64,
    ((4, 5), 4): 64, ((4, 5), 5): 64,
}
# AND THE SAME TABLE AT EVERY FINITE AMPLITUDE, ENTRY FOR ENTRY.
FINITE_TABLES_EQUAL_FIRST_ORDER = True
FINITE_CELL_COUNT = 60
EQUIVALENCE_BOTH_DIRECTIONS = True
# THE ADVERSARIAL CHECK'S SIX REQUESTED CELLS, three zeros and three nonzeros.
CHECK_SIX_ZERO_CELLS = (((1, 2), 5), ((2, 3), 5), ((4, 5), 1))
CHECK_SIX_NONZERO_CELLS = (((3, 4), 5), ((2, 3), 1), ((2, 3), 3))
# BLOCK 192's THREE LANDED CUTOFF PAIRS, gated here as INSTANCES of the law.
BLOCK192_CUTOFF_PAIRS = (((1, 2), 5), ((2, 3), 5), ((4, 5), 1))
BLOCK192_CUTOFF_TABLE = {
    ((1, 2), 1): 64, ((1, 2), 3): 64, ((1, 2), 5): 0,
    ((2, 3), 1): 64, ((2, 3), 3): 64, ((2, 3), 5): 0,
    ((3, 4), 1): 64, ((3, 4), 3): 64, ((3, 4), 5): 64,
    ((4, 5), 1): 0, ((4, 5), 3): 64, ((4, 5), 5): 64,
}

# --- D: THE HARMONIC-RESPONSE DERIVATION ------------------------------------
TRANSPORT_IDENTITY_RESIDUAL = 0
# nnz of the ROW support of dQ for the one-cell source at anchor s, x = 0.
SOURCE_ROW_SIZES = {
    16: (12, 14, 16, 16, 16, 16, 14, 12),
    20: (12, 14, 16, 16, 16, 16, 16, 16, 14, 12),
}
# and its SLICE support, positive half only: exactly the three slices
# [2*floor(s/2), 2*floor(s/2) + 2] at every anchor and both widths.
SOURCE_SLICE_RULE = True
RESPONSE_SUPPORT_COLUMNS = 240
RESPONSE_SUPPORT_MISMATCHES = 0
HARMONIC_FAILURES = 0
RESPONSE_RELATION_PAIRS = 30
RESPONSE_RELATION_RESIDUAL = 0
UNIT_CLOSED_FORM_RESIDUAL = 0
UNIT_CLOSED_FORM_GATES = 8
DW_LINK_RESIDUAL = 0
DW_LINK_CELLS = 40

# --- E: THE PARITY-RESOLVED WINDOW LAW --------------------------------------
# nnz(R) for the reflected one-cell source, anchor s against core t0, at
# T = 16.  READ THE PARITY: the break interval SHIFTS BY TWO between t0 = 1 and
# t0 = 2 and then STANDS STILL from t0 = 2 to t0 = 3.
WINDOW_TABLE_SIXTEEN = {
    (1, 0): 64, (1, 1): 64, (1, 2): 64, (1, 3): 64,
    (1, 4): 0, (1, 5): 0, (1, 6): 0, (1, 7): 0,
    (2, 0): 0, (2, 1): 0, (2, 2): 64, (2, 3): 64,
    (2, 4): 32, (2, 5): 32, (2, 6): 0, (2, 7): 0,
    (3, 0): 0, (3, 1): 0, (3, 2): 64, (3, 3): 64,
    (3, 4): 64, (3, 5): 64, (3, 6): 0, (3, 7): 0,
    (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0,
    (4, 4): 64, (4, 5): 64, (4, 6): 32, (4, 7): 32,
    (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0,
    (5, 4): 64, (5, 5): 64, (5, 6): 64, (5, 7): 64,
}
WINDOW_CELLS_SIXTEEN = 40
WINDOW_CELLS_TWENTY = 70
SPATIALLY_UNIFORM = True
# THE LAW ITSELF, as a predicate on (t0, s), and the window as an interval.
PARITY_SWITCHED = True
ODD_WINDOW_OFFSETS = (0, 2)
EVEN_WINDOW_OFFSETS = (1, 3)
WINDOW_WIDTH_IN_SLICES = 3
CORE_FOOTPRINT_IN_SLICES = 4
# THE BREAK DENSITY over the four breaking anchors [2j, 2j+3], in order.
ODD_BREAK_DENSITY = (64, 64, 64, 64)
EVEN_BREAK_DENSITY = (64, 64, 32, 32)
# THE EXEMPTION CENSUS at the HIGH end s = t0 + 3, per core.
ODD_EXEMPTION_CORES = (1, 3)
EVEN_EXEMPTION_CORES = (2, 4)
ODD_ADMISSIBLE_HIGH = 0
EVEN_ADMISSIBLE_HIGH = 32
ODD_CELL_BLOCK_DIRECTIONS = 16
ODD_CELL_BLOCK_BREAKS = 0
EVEN_CELL_BLOCK_BREAKS = 8
ODD_RAW_HIGH = {1: (1280, 0), 3: (768, 0)}
EVEN_RAW_HIGH = {2: (1024, 256), 4: (512, 256)}
# AND THE DUAL EXEMPTION at the LOW end, which is the even cores' own.
ODD_RAW_LOW = {1: (512, 256), 3: (1024, 256)}
EVEN_RAW_LOW = {2: (768, 0), 4: (1280, 0)}
# THE TWO MEASURED SUPPORT FACTS, which is the whole of the reduction.
UNION_SUPPORT_IS_THE_WINDOW = True
COLLAPSED_FUNCTIONALS_PER_EVEN_CORE = 4
COLLAPSED_FUNCTIONAL_NNZ = 4
# THE RAW-UNIT LAW: for E_{p,q} the residual is nonzero IFF the row slice lies
# in the window, for EVERY column q.
RAW_UNIT_MISMATCHES = 0
RAW_UNITS_SIXTEEN = 20480
RAW_UNITS_TWENTY = 44800
RAW_UNIT_BREAKS = {16: 768, 20: 960}
# THE VALIDITY BOUNDARY, MEASURED: the cores that violate t0 + 3 <= T/2 do NOT
# obey the law, and their union support is not a three-slice window.
INVALID_CORES = {16: (6, 7), 20: (8, 9)}
INVALID_CORES_OBEY_LAW = False
# THE EXACT UNEXPECTED-BREAK WITNESS, digit for digit as the check recorded it.
WITNESS_CELL = (2, 5)
WITNESS_ENTRY = (0, 4)
WITNESS_VALUE = sp.Rational(
    303717414128393981002946552450301011272963193469691599136505997554493148222247708710000000,
    77707725095998816829080256798567544217876202163787270905242891606801827087957579200283634261)

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO, so a residual or an incidence entry passed through it can
# silently turn a BREAK into an EXEMPTION -- and this block is a block whose
# entire content is which exact residuals are zero.  Every mass, shear, volume
# and amplitude here is ALREADY an exact sympy Rational.  Gate F counts the
# occurrences in this file's own source and requires ZERO.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def rational_matrix(matrix: sp.MatrixBase) -> DomainMatrix:
    """THE EXACT RATIONAL DOMAIN, AND IT IS NOT A NUMERICAL METHOD.  Every entry
    of every matrix in this runner is a sympy Rational, so the matrix lies in
    QQ^(n x n) exactly; DomainMatrix carries out the inverse by exact
    fraction-free arithmetic over that field.  No float is created at any point
    and no tolerance exists to be tuned.  It is used in place of the dense sympy
    fallback purely because that is slow at dimensions 64 and 80, and it changes
    NO value."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return rational_matrix(matrix).inv().to_Matrix()


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is involved."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


DELTA = sp.Symbol("delta")


# ---------------------------------------------------------------------------
# THE WIDTH FAMILY AT A VOLUME PROFILE, at an arbitrary width.  Everything
# except the shear block is rebuilt here; the shear block is the ONE import.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def site_index(width: int, time: int, space: int) -> int:
    return (time % width) * SPACE_EXTENT + space % SPACE_EXTENT


def site_theta(width: int, time: int) -> int:
    """theta_s(t) = -t, fixing the slices {0, T/2}."""
    return (-time) % width


def anchor_theta(width: int, time: int) -> int:
    """thA_s(t) = -1-t: the ANCHOR reflection that carries a NON-UNIFORM volume
    profile across the seam."""
    return (-1 - time) % width


def staggered_kernel(width: int) -> sp.Matrix:
    count = width * SPACE_EXTENT
    kernel = sp.zeros(count, count)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if time == width - 1 else 1
            here = site_index(width, time, space)
            ahead = site_index(width, time + 1, space)
            kernel[here, ahead] += sp.Rational(temporal_sign, 2)
            kernel[ahead, here] -= sp.Rational(temporal_sign, 2)
            spatial_sign = (-1) ** time
            right = site_index(width, time, space + 1)
            kernel[here, right] += sp.Rational(spatial_sign, 2)
            kernel[right, here] -= sp.Rational(spatial_sign, 2)
    return kernel


def grade_projector(width: int, grade: int) -> sp.Matrix:
    return sp.diag(*[1 if (time % 2 + space % 2) == grade else 0
                     for time in range(width) for space in range(SPACE_EXTENT)])


def raising_part(width: int, kernel: sp.Matrix) -> sp.Matrix:
    p0, p1, p2 = (grade_projector(width, g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation(width: int) -> sp.Matrix:
    count = width * SPACE_EXTENT
    matrix = sp.zeros(count, count)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            matrix[site_index(width, site_theta(width, time), space),
                   site_index(width, time, space)] = 1
    return matrix


def site_restricted_raising(width: int, raising: sp.Matrix) -> sp.Matrix:
    count = width * SPACE_EXTENT
    half = width // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(count, count)
    for row in range(count):
        for column in range(count):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            if row_time not in closed or column_time not in closed:
                continue
            if row_time == column_time and row_time in fixed:
                continue
            matrix[row, column] = raising[row, column]
    return matrix


def cell_embedding(width: int, time: int, space: int) -> sp.Matrix:
    matrix = sp.zeros(width * SPACE_EXTENT, 4)
    for column, (delta_t, delta_x) in enumerate(
            ((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[site_index(width, time + delta_t, space + delta_x), column] = 1
    return matrix


def imported_shear_block(volume: object) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT, read AT A SYMBOLIC VOLUME: the LANDED Block 105
    shear Hodge diag(v, v g(c)^-1, 1/v).  NO nsimplify: the shear is already a
    sympy Rational and the volume is a Rational or a Symbol."""
    return sp.Matrix(b128.block105.shear_hodge(FIXTURE_SHEAR, volume))


def cell_sum(width: int, blocks: dict) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule.
    Only the times present in `blocks` contribute, which is exactly why the
    tangent of H is the same cell sum over the perturbed times alone."""
    result = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for time, block in blocks.items():
        for space in range(SPACE_EXTENT):
            embedding = cell_embedding(width, time, space)
            result += embedding * block * embedding.T / 4
    return sp.expand(result)


def site_hodge_profile(width: int, profile: dict) -> sp.Matrix:
    half = width // 2
    blocks = {}
    for time in range(width):
        if time < half:
            blocks[time] = imported_shear_block(profile[time])
        else:
            block = imported_shear_block(profile[anchor_theta(width, time)])
            blocks[time] = sp.expand(
                OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    return cell_sum(width, blocks)


def bump_profile(width: int, anchors: tuple, delta: object) -> dict:
    return {time: (UNIT_VOLUME - delta if time in anchors else UNIT_VOLUME)
            for time in range(width // 2)}


def completion(hodge: sp.Matrix, glue: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    return sp.expand(FIXTURE_MASS * hodge + hodge * glue - glue.T * hodge)


def action_tangent(tangent: sp.Matrix, glue: sp.Matrix) -> sp.Matrix:
    """dQ = m dH + dH D_s - D_s^T dH, exact because D_s does not depend on the
    volume profile at all."""
    return sp.expand(FIXTURE_MASS * tangent + tangent * glue - glue.T * tangent)


def core_cells(core: int) -> tuple:
    return tuple((time, space) for time in (core, core + 1)
                 for space in range(SPACE_EXTENT))


def shifted_pairing(width: int, inverse: sp.Matrix, core: int,
                    step: int) -> sp.Matrix:
    """L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]; k = 0 is K_c."""
    cells = core_cells(core)
    matrix = sp.zeros(len(cells), len(cells))
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(width, site_theta(width, row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(width, column_time + step, column_space), partner]
    return matrix


def one_cell_tangent(width: int, anchor: int, space: int,
                     block: sp.Matrix = None) -> sp.Matrix:
    """THE REFLECTED ONE-CELL HODGE TANGENT: the single cell at (anchor, space)
    carrying dB, plus its thA_s image cell carrying P_4 dB P_4^T."""
    if block is None:
        block = DISPLAYED_VOLUME_DERIVATIVE
    positive = cell_embedding(width, anchor, space)
    image = cell_embedding(width, anchor_theta(width, anchor), space)
    mirrored = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    return sp.expand(positive * block * positive.T / 4
                     + image * mirrored * image.T / 4)


def bump_tangent(width: int, anchors: tuple) -> sp.Matrix:
    """Block 192's bump tangent, rebuilt as the SUM of this block's one-cell
    tangents over the anchors and all four spatial positions."""
    total = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for anchor in anchors:
        for space in range(SPACE_EXTENT):
            total += one_cell_tangent(width, anchor, space)
    return sp.expand(total)


def slice_support(width: int, vector: sp.Matrix) -> tuple:
    return tuple(sorted({index // SPACE_EXTENT
                         for index in range(width * SPACE_EXTENT)
                         if vector[index] != 0}))


def row_support(width: int, matrix: sp.Matrix) -> tuple:
    count = width * SPACE_EXTENT
    return tuple(row for row in range(count)
                 if any(matrix[row, column] != 0 for column in range(count)))


def window_of(core: int) -> tuple:
    """THE MEASURED CLOSED FORM, declared as a predicate and then checked
    against the measured union support: the window depends on t0 ONLY through
    floor(t0 / 2)."""
    base = 2 * (core // 2)
    return tuple(range(base + 1, base + 4))


def breaks_predicted(core: int, anchor: int) -> bool:
    base = 2 * (core // 2)
    return base <= anchor <= base + 3


# ---------------------------------------------------------------------------
# THE CORE FRAME AND ITS TRANSPORT-DEFECT FUNCTIONALS
# ---------------------------------------------------------------------------
class CoreFrame:
    """The pair core at t0, with W, its defect functionals d_b and u_b = G^T d_b,
    and the two contracted factors that make the residual a BILINEAR FORM."""

    def __init__(self, width: int, inverse: sp.Matrix, glue: sp.Matrix,
                 core: int) -> None:
        count = width * SPACE_EXTENT
        cells = core_cells(core)
        self.width, self.core = width, core
        self.gram = shifted_pairing(width, inverse, core, 0)
        self.second = shifted_pairing(width, inverse, core, 2)
        self.gram_inverse = exact_inverse(self.gram)
        self.monodromy = sp.expand(self.gram_inverse * self.second)
        self.transport_residual = residual_count(
            self.gram * self.monodromy - self.second)
        defects = sp.zeros(8, count)
        for b, (time_b, space_b) in enumerate(cells):
            defects[b, site_index(width, time_b + 2, space_b)] += 1
            for other, (time_o, space_o) in enumerate(cells):
                defects[b, site_index(width, time_o, space_o)] -= (
                    self.monodromy[other, b])
        self.defects = defects
        self.dual = sp.expand(defects * inverse)                    # u_b^T
        self.dual_glued = sp.expand(self.dual * glue.T)             # (D u_b)^T
        self.columns = sp.Matrix.hstack(*[
            inverse[:, site_index(width, site_theta(width, time_a), space_a)]
            for (time_a, space_a) in cells])
        self.columns_glued = sp.expand(FIXTURE_MASS * self.columns
                                       + glue * self.columns)
        self.union_support = tuple(sorted({
            index // SPACE_EXTENT for b in range(8)
            for index in range(count) if self.dual[b, index] != 0}))
        self.per_functional = tuple(
            tuple(sorted({index // SPACE_EXTENT for index in range(count)
                          if self.dual[b, index] != 0})) for b in range(8))
        self.functional_nnz = tuple(
            sum(1 for index in range(count) if self.dual[b, index] != 0)
            for b in range(8))

    def residual(self, tangent: sp.Matrix) -> sp.Matrix:
        """R[a,b] = -u_b^T dQ G[:, theta_a], expanded through dQ's definition so
        that only the eight-row and eight-column contractions are ever formed."""
        left = sp.expand(self.dual * tangent)
        right = sp.expand(self.dual_glued * tangent)
        return sp.expand(-(left * self.columns_glued
                           - right * self.columns).T)

    def unit_residual(self, row: int, column: int) -> sp.Matrix:
        """The SAME residual for the raw tangent E_{row, column}, in closed form:
        no matrix product is formed at all."""
        matrix = sp.zeros(8, 8)
        for a in range(8):
            for b in range(8):
                matrix[a, b] = -(self.dual[b, row]
                                 * self.columns_glued[column, a]
                                 - self.dual_glued[b, row]
                                 * self.columns[column, a])
        return matrix

    def full_route_residual(self, inverse: sp.Matrix, glue: sp.Matrix,
                            tangent: sp.Matrix) -> sp.Matrix:
        """THE DEFINITIONAL ROUTE, kept for the gate: form the WHOLE dG and
        restrict it, exactly as Block 192 did."""
        daction = action_tangent(tangent, glue)
        dresolvent = sp.expand(-inverse * daction * inverse)
        dgram = shifted_pairing(self.width, dresolvent, self.core, 0)
        dsecond = shifted_pairing(self.width, dresolvent, self.core, 2)
        return sp.expand(dsecond - dgram * self.monodromy)


def build_carrier(width: int, profile: dict) -> dict:
    reflection = reflection_permutation(width)
    restricted = site_restricted_raising(
        width, raising_part(width, staggered_kernel(width)))
    glue = sp.expand(restricted - reflection * restricted * reflection)
    hodge = site_hodge_profile(width, profile)
    action = completion(hodge, glue)
    return {"reflection": reflection, "glue": glue, "hodge": hodge,
            "action": action, "inverse": exact_inverse(action)}


# ---------------------------------------------------------------------------
# THE MEASUREMENT.  Everything below happens ONCE, before any mutation flag is
# read, and every heavy inverse is built once and shared.
# ---------------------------------------------------------------------------
@dataclass
class Facts:
    main_head: str
    authority: AuthorityCertificate
    scope: dict
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    volume_derivative: sp.Matrix
    volume_derivative_residual: int
    displayed_law_residual: int
    carrier_controls: dict
    bump_tangent_residual: dict
    defect_route: dict
    first_order_table: dict
    finite_tables: dict
    finite_equal_first_order: bool
    equivalence: bool
    equivalence_cells: int
    transport_residual: dict
    source_rows: dict
    source_slices: dict
    source_slice_rule: bool
    response_columns: int
    response_mismatches: int
    harmonic_failures: int
    response_relation: dict
    unit_closed_form: tuple
    dw_link: dict
    window_tables: dict
    window_law: dict
    spatial_uniform: dict
    break_density: dict
    exemption: dict
    union_supports: dict
    union_matches_window: dict
    collapsed: dict
    raw_units: dict
    invalid_obey: dict
    witness: object
    nsimplify_calls: int


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    authority = authority_certificate(main_head)
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""

    # ---- C: the displayed tangent, against the IMPORT ----------------------
    symbolic_block = imported_shear_block(UNIT_VOLUME - DELTA)
    imported_derivative = symbolic_block.applyfunc(
        lambda value: sp.diff(value, DELTA).subs(DELTA, 0))
    volume_derivative_residual = residual_count(
        imported_derivative - DISPLAYED_VOLUME_DERIVATIVE)
    displayed_law_residual = (
        residual_count(imported_shear_block(UNIT_VOLUME) - DISPLAYED_HODGE_UNIT)
        + residual_count(imported_shear_block(BUMP_VOLUME)
                         - DISPLAYED_HODGE_BUMP))

    # ---- the TWO baseline carriers, ONE exact inverse each -----------------
    carriers, frames, controls = {}, {}, {}
    for width in WIDTHS:
        half = width // 2
        carrier = build_carrier(width, bump_profile(width, (), sp.Integer(0)))
        carriers[width] = carrier
        inverse, glue = carrier["inverse"], carrier["glue"]
        controls[width] = (
            residual_count(carrier["action"] * inverse
                           - sp.eye(width * SPACE_EXTENT)),
            residual_count(carrier["reflection"] * carrier["hodge"]
                           * carrier["reflection"] - carrier["hodge"]),
            residual_count(carrier["reflection"] * carrier["action"]
                           * carrier["reflection"] - carrier["action"].T))
        frames[width] = {core: CoreFrame(width, inverse, glue, core)
                         for core in range(1, half)}
    transport_residual = {(width, core): frame.transport_residual
                          for width, table in frames.items()
                          for core, frame in table.items()}

    # ---- C: the one-cell tangents SUM to Block 192's bump tangent ----------
    bump_tangent_residual = {}
    for bump in BUMPS:
        blocks = {time: DISPLAYED_VOLUME_DERIVATIVE for time in bump}
        blocks.update({
            time: sp.expand(OFFSET_PERMUTATION * DISPLAYED_VOLUME_DERIVATIVE
                            * OFFSET_PERMUTATION.T)
            for time in range(8, 16) if anchor_theta(16, time) in bump})
        bump_tangent_residual[bump] = residual_count(
            cell_sum(16, blocks) - bump_tangent(16, bump))

    # ---- C: the defect-functional route against the FULL dG route ----------
    defect_route = {}
    for core in range(1, 6):
        for anchor in (core - 1, core + 2):
            tangent = one_cell_tangent(16, anchor, 0)
            defect_route[(core, anchor)] = residual_count(
                frames[16][core].full_route_residual(
                    carriers[16]["inverse"], carriers[16]["glue"], tangent)
                - frames[16][core].residual(tangent))

    # ---- E: the one-cell incidence tables at both widths -------------------
    window_tables, spatial_uniform, window_law = {}, {}, {}
    for width in WIDTHS:
        half = width // 2
        valid = tuple(core for core in range(1, half) if core + 3 <= half)
        table, uniform, law = {}, True, True
        for core in range(1, half):
            for anchor in range(half):
                counts = tuple(
                    nonzero_entries(frames[width][core].residual(
                        one_cell_tangent(width, anchor, space)))
                    for space in range(SPACE_EXTENT))
                table[(core, anchor)] = counts[0]
                if len(set(counts)) != 1:
                    uniform = False
                if core in valid and ((counts[0] > 0)
                                      != breaks_predicted(core, anchor)):
                    law = False
        window_tables[width] = table
        spatial_uniform[width] = uniform
        window_law[width] = (law, len(valid) * half)

    # ---- E: the break-density fingerprint ----------------------------------
    break_density = {}
    for width in WIDTHS:
        half = width // 2
        for core in range(1, half):
            if core + 3 > half:
                continue
            base = 2 * (core // 2)
            break_density[(width, core)] = tuple(
                window_tables[width][(core, base + offset)]
                for offset in range(4))

    # ---- E: the exemption census, high end and low end ---------------------
    exemption = {}
    for core in (1, 2, 3, 4):
        frame = frames[16][core]
        high, low = core + 3, core - 1
        cell_blocks = tuple(
            nonzero_entries(frame.residual(one_cell_tangent(
                16, high, 0, _unit_block(row, column))))
            for row in range(4) for column in range(4))
        record = {
            "admissible_high": tuple(
                nonzero_entries(frame.residual(one_cell_tangent(16, high, x)))
                for x in range(SPACE_EXTENT)),
            "admissible_low": tuple(
                nonzero_entries(frame.residual(one_cell_tangent(16, low, x)))
                for x in range(SPACE_EXTENT)),
            "cell_block_directions": len(cell_blocks),
            "cell_block_breaks": sum(1 for value in cell_blocks if value),
            "raw_high": _raw_census(frame, range(high, 9)),
            "raw_low": _raw_census(frame, range(0, low + 2)),
        }
        exemption[core] = record

    # ---- E: the two support facts and the raw-unit law ---------------------
    union_supports, union_matches, collapsed, raw_units = {}, {}, {}, {}
    invalid_obey = {}
    source_rows, source_slices = {}, {}
    source_slice_rule = True
    for width in WIDTHS:
        half = width // 2
        for core in range(1, half):
            frame = frames[width][core]
            union_supports[(width, core)] = frame.union_support
            union_matches[(width, core)] = (
                frame.union_support == window_of(core))
            collapsed[(width, core)] = tuple(
                index for index in range(8)
                if len(frame.per_functional[index]) == 1)
        for anchor in range(half):
            daction = action_tangent(one_cell_tangent(width, anchor, 0),
                                     carriers[width]["glue"])
            rows = row_support(width, daction)
            source_rows[(width, anchor)] = len(rows)
            positive = tuple(sorted({row // SPACE_EXTENT for row in rows
                                     if row // SPACE_EXTENT <= half}))
            source_slices[(width, anchor)] = positive
            if positive != tuple(range(2 * (anchor // 2), 2 * (anchor // 2) + 3)):
                source_slice_rule = False
        count = width * SPACE_EXTENT
        for core in range(1, half):
            frame = frames[width][core]
            if core + 3 > half:
                # THE DOMAIN BOUNDARY, MEASURED RATHER THAN ASSUMED: outside
                # Block 191's touch/cross rule neither the window nor the law
                # survives, and both failures are recorded as facts.
                invalid_obey[(width, core)] = (
                    frame.union_support == window_of(core),
                    all((window_tables[width][(core, anchor)] > 0)
                        == breaks_predicted(core, anchor)
                        for anchor in range(half)))
                continue
            total = breaks = mismatches = 0
            inside = set(frame.union_support)
            for row in range(count):
                predicted = (row // SPACE_EXTENT) in inside
                for column in range(count):
                    total += 1
                    nonzero = nonzero_entries(
                        frame.unit_residual(row, column)) > 0
                    breaks += nonzero
                    mismatches += (nonzero != predicted)
            raw_units[(width, core)] = (total, breaks, mismatches)

    # ---- D: the response support, harmonicity and the response relation ----
    inverse16 = carriers[16]["inverse"]
    action16 = carriers[16]["action"]
    glue16 = carriers[16]["glue"]
    response_columns = response_mismatches = harmonic_failures = 0
    response_relation, tangents16 = {}, {}
    for anchor in range(8):
        tangents16[anchor] = action_tangent(one_cell_tangent(16, anchor, 0),
                                            glue16)
    for anchor in range(1, 7):
        daction = tangents16[anchor]
        target = row_support(16, daction)
        for core in range(1, 6):
            cells = core_cells(core)
            responses = {}
            for a, (time_a, space_a) in enumerate(cells):
                response_columns += 1
                partner = site_index(16, site_theta(16, time_a), space_a)
                source = sp.expand(daction * inverse16[:, partner])
                if tuple(i for i in range(64) if source[i] != 0) != target:
                    response_mismatches += 1
                field = sp.expand(inverse16 * source)
                if residual_count(action16 * field - source):
                    harmonic_failures += 1
                responses[a] = field
            relation = sp.zeros(8, 8)
            for a in range(8):
                for b, (time_b, space_b) in enumerate(cells):
                    relation[a, b] = (
                        responses[a][site_index(16, time_b + 2, space_b)]
                        - sum(responses[a][site_index(16, time_o, space_o)]
                              * frames[16][core].monodromy[other, b]
                              for other, (time_o, space_o) in enumerate(cells)))
            response_relation[(anchor, core)] = residual_count(
                relation + frames[16][core].residual(
                    one_cell_tangent(16, anchor, 0)))

    # ---- D: the raw-unit closed form, and the dW link ----------------------
    unit_gates = []
    for core in (1, 2):
        for (row, column) in ((site_index(16, 4, 0), site_index(16, 9, 2)),
                              (site_index(16, 7, 3), 17),
                              (site_index(16, 2, 1), 41),
                              (site_index(16, 13, 2), 5)):
            unit = sp.zeros(64, 64)
            unit[row, column] = 1
            unit_gates.append(residual_count(
                frames[16][core].residual(unit)
                - frames[16][core].unit_residual(row, column)))
    dw_link = {}
    for core in range(1, 6):
        frame = frames[16][core]
        for anchor in range(8):
            residual = frame.residual(one_cell_tangent(16, anchor, 0))
            monodromy_tangent = sp.expand(frame.gram_inverse * residual)
            dw_link[(core, anchor)] = (
                nonzero_entries(residual),
                nonzero_entries(monodromy_tangent),
                residual_count(frame.gram * monodromy_tangent - residual))

    # ---- C: the twenty-entry first-order table and the finite tables -------
    first_order_table = {}
    for bump in BUMPS:
        tangent = bump_tangent(16, bump)
        for core in range(1, 6):
            first_order_table[(bump, core)] = nonzero_entries(
                frames[16][core].residual(tangent))
    finite_tables = {}
    for bump in BUMPS:
        for amplitude in AMPLITUDES:
            moved = exact_inverse(completion(
                site_hodge_profile(16, bump_profile(16, bump, amplitude)),
                glue16))
            for core in range(1, 6):
                moved_monodromy = sp.expand(
                    exact_inverse(shifted_pairing(16, moved, core, 0))
                    * shifted_pairing(16, moved, core, 2))
                finite_tables[(bump, amplitude, core)] = nonzero_entries(
                    sp.expand(moved_monodromy - frames[16][core].monodromy))
    finite_equal = all(
        finite_tables[(bump, amplitude, core)] == first_order_table[(bump, core)]
        for bump in BUMPS for amplitude in AMPLITUDES for core in range(1, 6))
    equivalence = all(
        (finite_tables[(bump, amplitude, core)] == 0)
        == (first_order_table[(bump, core)] == 0)
        for bump in BUMPS for amplitude in AMPLITUDES for core in range(1, 6))

    witness = frames[16][WITNESS_CELL[0]].residual(
        one_cell_tangent(16, WITNESS_CELL[1], 0))[WITNESS_ENTRY]

    return Facts(
        main_head=main_head,
        authority=authority,
        scope=scope_certificate(note_text),
        imposed=len(IMPOSED_OBJECTS),
        registered=len(REGISTERED_OBJECTS),
        adopted=len(ADOPTED_OBJECTS),
        unsupplied=len(UNSUPPLIED_GRAVITY_STRUCTURES),
        volume_derivative=imported_derivative,
        volume_derivative_residual=volume_derivative_residual,
        displayed_law_residual=displayed_law_residual,
        carrier_controls=controls,
        bump_tangent_residual=bump_tangent_residual,
        defect_route=defect_route,
        first_order_table=first_order_table,
        finite_tables=finite_tables,
        finite_equal_first_order=finite_equal,
        equivalence=equivalence,
        equivalence_cells=len(finite_tables),
        transport_residual=transport_residual,
        source_rows=source_rows,
        source_slices=source_slices,
        source_slice_rule=source_slice_rule,
        response_columns=response_columns,
        response_mismatches=response_mismatches,
        harmonic_failures=harmonic_failures,
        response_relation=response_relation,
        unit_closed_form=tuple(unit_gates),
        dw_link=dw_link,
        window_tables=window_tables,
        window_law=window_law,
        spatial_uniform=spatial_uniform,
        break_density=break_density,
        exemption=exemption,
        union_supports=union_supports,
        union_matches_window=union_matches,
        collapsed=collapsed,
        raw_units=raw_units,
        invalid_obey=invalid_obey,
        witness=witness,
        nsimplify_calls=nsimplify_occurrences())


def _unit_block(row: int, column: int) -> sp.Matrix:
    block = sp.zeros(4, 4)
    block[row, column] = 1
    return block


def _raw_census(frame: CoreFrame, slices) -> tuple:
    count = frame.width * SPACE_EXTENT
    total = breaks = 0
    for time in slices:
        for space in range(SPACE_EXTENT):
            row = site_index(frame.width, time, space)
            for column in range(count):
                total += 1
                if nonzero_entries(frame.unit_residual(row, column)):
                    breaks += 1
    return (total, breaks)


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE LOCALITY LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13)), BLOCK 191's VOLUME PROFILE AND BLOCK 192's BUMP FAMILY v = 1 - delta AT THE THREE AMPLITUDES 1/5, 1/3 AND 2/5, THE REFLECTED ONE-CELL HODGE TANGENT dH(s,x) -- THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT -- THE PROBE DOMAIN of anchors s = 0..T/2-1 at all four spatial anchors against cores t0 = 1..T/2-1 under BLOCK 191's touch/cross rule t0+3 <= T/2, THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE TWO-STEP TRANSPORT DEFECT FUNCTIONALS d_b AND u_b = G^T d_b, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module AT A SYMBOLIC VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED AND NO LOCALITY PRINCIPLE IS ESTABLISHED: delta is a dial on an IMPOSED Hodge-volume parameter, 'response' names d/d(delta) of a rational matrix entry at delta = 0, and this block supplies NO lapse variable in an ADM phase space, NO Hamiltonian constraint, NO gauge orbit, NO quotient, NO Dirac observable and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, THE EXACT SET OF ONE-CELL HODGE TANGENTS THAT MAKE THE FIRST-ORDER INTERTWINING RESIDUAL NONZERO IS A THREE-SLICE INTERVAL WHOSE POSITION DEPENDS ON THE PARITY OF THE CORE. 'WINDOW', 'TRANSPORT', 'HARMONIC' AND 'RESPONSE' NAME PROPERTIES OF EXACT RATIONAL MATRICES: 'window' NAMES the set of slices carrying the nonzero rows of the transport-defect functionals, 'two-step transport' NAMES the linear relation L_2 = K_c W, 'Q-harmonic' NAMES membership in the kernel of Q on the rows where a source vanishes, and 'response' NAMES a derivative of a rational matrix entry. THE WINDOW IS NOT A LIGHT CONE AND NOT A LOCALITY PRINCIPLE: it is a statement about which exact matrices are zero, and NO propagation speed, NO causal structure, NO screening length and NO continuum limit is supplied or implied. THE PARITY-INDEPENDENT WINDOW IS REFUTED, NOT SOFTENED: the adversarial check measured the even cores carrying the SHIFTED window [t0+1, t0+3], so at t0 = 2 the anchors s = 1 and s = 5 carry the OPPOSITE statuses from the solve's rule and the admissible t0+3 cell BREAKS with nnz(R) = 32 where the odd cores exempt it, and PARITY_INDEPENDENT_WINDOW_CLAIMED = False is a declared constant with a gate and a mutation. THE LAW IS NOT PROVED FROM THE STAGGERED RECURRENCE: it is REDUCED to the bilinear identity R[a,b] = -u_b^T dQ G[:, theta_a] together with TWO MEASURED SUPPORT FACTS -- that the union slice support of the eight functionals u_b is EXACTLY the three slices [2 floor(t0/2)+1, 2 floor(t0/2)+3] and that a one-cell tangent at anchor s carries dH rows exactly on the slices {s, s+1} -- and both support facts are MEASURED at two widths and DERIVED FROM NOTHING. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NO GENERALITY IS CLAIMED: ONE fixture, TWO widths, ONE profile family, THREE amplitudes, and NOTHING about the infinite-width or continuum limit. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE EQUIVALENCE IS MEASURED IN BOTH DIRECTIONS AND THE FINITE TABLE IS THE FIRST-ORDER TABLE ENTRY FOR ENTRY. W(delta) = W(0) matrix-exact IF AND ONLY IF R = dL_2 - dK_c W = 0: over the TWENTY valid (bump, core) pairs at T = 16 -- bumps {1,2}, {2,3}, {3,4}, {4,5} against cores t0 = 1, 2, 3, 4, 5 -- nnz(R) is 64 at FOURTEEN pairs, 32 at ONE pair, and EXACTLY ZERO at FIVE; and nnz(W(delta) - W(0)) at delta = 1/5, 1/3 AND 2/5 reproduces that table ENTRY FOR ENTRY in all SIXTY finite rebuilds, so the biconditional holds sixty times over and the zero set is not a linearization artefact. THE ADVERSARIAL CHECK'S SIX REQUESTED CELLS SIT INSIDE IT: ({1,2}, 5), ({2,3}, 5) and ({4,5}, 1) are the exact zero matrix and ({3,4}, 5), ({2,3}, 1) and ({2,3}, 3) are fully dense. BLOCK 192's THREE LANDED CUTOFF PAIRS ARE GATED AS INSTANCES and its twelve-entry odd-core table is reproduced entry for entry as this block's control. THE ONE-CELL TANGENT IS GATED AGAINST BLOCK 192's BUMP TANGENT: summing this block's dH(s,x) over the two anchors of a bump and over all four spatial anchors reproduces Block 192's cell-sum tangent at ZERO residual at all four bumps. THE CARRIER CONTROLS CLOSE AT BOTH WIDTHS: nnz(Q G - I) = nnz(Ps H Ps - H) = nnz(Ps Q Ps - Q^T) = 0 at T = 16 and at T = 20, and the displayed dB is gated entrywise at ZERO against the SYMBOLIC derivative of the IMPORTED shear_hodge with the underlying law gated at BOTH probed volumes, thirty-two numbers. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's exemptions could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate F.\\nper_mode: THE DERIVATION IS THREE PILLARS AND A BILINEAR FORM, AND EVERY PILLAR IS GATED AT EXACTLY ZERO. With d_b = e_{(t_b+2, x_b)} - sum_b' W[b',b] e_{(t_b', x_b')} and u_b = G^T d_b: (i) K_c W = L_2 is EXACTLY d_b^T G[:, theta_a] = 0 for the eight unperturbed core columns, so W is DEFINED by the two-step transport relation and not fitted -- nnz(K_c W - L_2) = 0 at EVERY core at BOTH widths, sixteen frames; (ii) the response field rho_a = G dQ G[:, theta_a] satisfies Q rho_a = dQ G[:, theta_a] and is therefore Q-HARMONIC on every row where the source vanishes, and its row support equals the FULL row support of dQ with NO cancellation in all 240 tested columns and ZERO harmonic failures; and (iii) R[a,b] = -d_b^T rho_a, so R = 0 is EXACTLY the statement that the response field obeys the same defect relation as the unperturbed columns -- nnz(response relation + R) = 0 at all THIRTY (anchor, core) pairs. THE BILINEAR FORM FOLLOWS: R[a,b] = -u_b^T dQ G[:, theta_a], so R is LINEAR in the Hodge tangent and the whole law is a statement about the SUPPORT of the eight vectors u_b. THE dW LINK IS EXACT: R = K_c dW at zero residual, so R = 0 if and only if dW = 0, and nnz(dW) = nnz(R) at all FORTY cells. THE MEASURED SOURCE ROWS: the dQ row-support sizes for anchors s = 0..7 at T = 16 are (12, 14, 16, 16, 16, 16, 14, 12) and their positive slice supports are EXACTLY [2 floor(s/2), 2 floor(s/2)+2] at every anchor and at BOTH widths.\\nper_block: THE PARITY-RESOLVED WINDOW LAW, AND IT IS THE CHECK'S DISCOVERY CARRIED AS THIS BLOCK'S CENTRE. A reflected one-cell tangent at anchor s BREAKS the intertwining identity at core t0 IF AND ONLY IF s lies in [2 floor(t0/2), 2 floor(t0/2) + 3], equivalently if and only if its support {s, s+1} meets the THREE-SLICE WINDOW [t0, t0+2] for ODD t0 and [t0+1, t0+3] for EVEN t0. THE CORE'S FOOTPRINT IS FOUR SLICES {t0, t0+1, t0+2, t0+3} AND THE WINDOW IS ALWAYS THREE OF THEM, WITH ONE EXEMPT END THAT SWITCHES WITH PARITY: the LAST predicted slice t0+3 is exempt at odd cores and the FIRST read slice t0 is exempt at even cores. MEASURED ON FORTY CELLS AT T = 16 (anchors 0..7 against cores 1..5) AND SEVENTY AT T = 20 (anchors 0..9 against cores 1..7), spatially uniform in all four spatial anchors, with ZERO exceptions. THE BREAK DENSITY IS A FINGERPRINT AND NOT A BINARY: over the four breaking anchors in order the densities are (64, 64, 64, 64) at every odd core and (64, 64, 32, 32) at every even core, at BOTH widths. THE VALIDITY BOUNDARY IS MEASURED AND IS EXACTLY BLOCK 191's TOUCH/CROSS RULE: the cores t0 = 6, 7 at T = 16 and t0 = 8, 9 at T = 20 violate t0+3 <= T/2 and do NOT obey the law, and their functional supports are not three-slice windows. AN EXACT UNEXPECTED-BREAK WITNESS IS RECORDED digit for digit at (t0, s) = (2, 5), entry R[0,4].\\nlattice_wide: THE EXEMPTION IS ATTACKED EXHAUSTIVELY AT THE ODD CORES AND REFUTED AT THE EVEN ONES. At the odd cores t0 = 1 and t0 = 3 the t0+3 exemption survives every attack: the admissible reflected one-cell tangent gives nnz(R) = 0 at ALL FOUR spatial anchors; ALL SIXTEEN 4x4 cell-block matrix-unit directions, INCLUDING the eight asymmetric ones, give the exact zero matrix; and every raw matrix unit whose ROW lies on any positive slice from t0+3 through T/2 with an ARBITRARY column anywhere in the 64-dimensional carrier gives the exact zero matrix -- 1280 of 1280 at t0 = 1 and 768 of 768 at t0 = 3. AT THE EVEN CORES THAT SAME EXEMPTION IS FALSE, MEASURED: the admissible t0+3 cell BREAKS with nnz(R) = 32 at t0 = 2 and t0 = 4, eight of the sixteen cell-block directions break, and 256 of 1024 raw directions break at t0 = 2 and 256 of 512 at t0 = 4. WHAT THE EVEN CORES CARRY INSTEAD IS THE DUAL EXEMPTION AT THE LOW END, AND IT IS EXHAUSTIVE THERE: 768 of 768 raw directions give zero at t0 = 2 and 1280 of 1280 at t0 = 4, while the same low-end census BREAKS at the odd cores, 256 of 512 at t0 = 1 and 256 of 1024 at t0 = 3. THE EXEMPT END IS THEREFORE NOT A COINCIDENCE OF THE CELL SOURCE: it is a property of the whole tangent space, and it switches with parity.\\nper_scope: THE MECHANISM IS REDUCED TO TWO MEASURED SUPPORT FACTS, AND BLOCK 192's REFUTED OVERLAP SIGNATURE IS REPAIRED. FACT ONE: the union of the slice supports of the eight transport-defect functionals u_b is EXACTLY the three-slice window [2 floor(t0/2)+1, 2 floor(t0/2)+3] at EVERY valid core at BOTH widths, with NO negative-half support at all; and at every even core exactly FOUR of the eight functionals COLLAPSE to a single slice with four nonzero entries, which is the structural origin of the shifted window. FACT TWO: a one-cell tangent at anchor s carries dH rows exactly on the slices {s, s+1}. TOGETHER WITH THE BILINEAR IDENTITY THEY GIVE THE LAW, AND THE RAW-UNIT FORM IS SHARPER STILL: for a raw Hodge tangent E_{p,q} the residual is nonzero IF AND ONLY IF the ROW p lies on one of the three window slices, for EVERY column q -- 20480 units at T = 16 and 44800 at T = 20, 65280 in all, with ZERO mismatches, and exactly 768 breaking units per core at T = 16 and 960 at T = 20. BLOCK 192 LEFT A NAMED OPEN LEG AND ONE MEASURED COUNTEREXAMPLE, AND BOTH ARE SETTLED HERE: its overlap signature compared the dH support against the naive FOUR-slice read window {t0, t0+1, t0+2, t0+3}, which is ONE SLICE TOO WIDE at odd cores; replacing dH by dQ and the naive window by the measured supp(u_b) makes the pair ({4,5}, t0 = 1) an ordinary instance -- the bump's dQ slices are {4, 5, 6} and the window is {1, 2, 3}, disjoint -- and there is NO counterexample left among the twenty pairs. WHAT REMAINS OPEN IS NAMED: the closed forms of the two supports are MEASURED at two widths and are NOT derived from the staggered recurrence.\\nRESULT: THE EXACT SET OF ONE-CELL HODGE TANGENTS THAT BREAK THE INTERTWINING IDENTITY IS DETERMINED AT TWO WIDTHS AND IS A THREE-SLICE WINDOW WHOSE EXEMPT END SWITCHES WITH THE PARITY OF THE CORE, THE EQUIVALENCE W(delta) = W(0) IF AND ONLY IF R = 0 IS MEASURED IN BOTH DIRECTIONS OVER SIXTY FINITE REBUILDS, THE HARMONIC-RESPONSE DERIVATION IS GATED IN ALL THREE PILLARS, AND THE MECHANISM IS REDUCED TO A BILINEAR FORM AND TWO MEASURED SUPPORT FACTS -- AND NOT ONE LINE OF IT IS A LIGHT CONE, A LOCALITY PRINCIPLE, A PROPAGATION SPEED, A CONSTRAINT OR A CONTINUUM LIMIT. The parity-independent window the solve proposed is REFUTED and carried as the block's central correction; the odd-core exemption is confirmed against an exhaustive raw-unit attack and its even-core dual is exhibited; Block 192's twelve-entry cutoff table is reproduced as a control and extended to twenty entries; and Block 192's refuted overlap signature is REPAIRED with its single counterexample explained away. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-192 STAND EXACTLY AS LANDED. BLOCK 192 IS NOT CORRECTED: its twelve-entry cutoff table is reproduced here entry for entry as this block's control, its three cutoff pairs are gated as instances of the window law, and its NAMED OPEN LEG is closed by reduction rather than by revision. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE fixture, TWO widths, ONE profile family and THREE amplitudes -- two widths are not a scan; the closed forms of the two supports are MEASURED and not derived from the recurrence; and the law's domain is bounded by a validity rule that is itself measured rather than proved. SEVEN ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the P2 REFUTATION, that the window is NOT parity-independent and the even cores carry [t0+1, t0+3]; the C2 CONFIRMATION of the odd-core incidence, extended here from eighteen cells to forty; the C3 SURVIVAL of the t0+3 exemption against an exhaustive raw-unit attack, extended here to all sixteen cell-block directions and to the even-core dual; the C1 EQUIVALENCE on the six requested cells, extended here to twenty pairs and sixty finite rebuilds; the C4 DERIVATION pillars, all three reproduced independently; the P1 WIDTH check at T = 20, extended here from nine cells to seventy; and the P3 ALL-AMPLITUDE check at three exact rationals, extended here to every bump and every core. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE CUTOFF MECHANISM DERIVATION (block 193 candidate), CUT PHASE A MEASURED, CUT PHASE B MEASURED, CUT PHASE B3 MEASURED, CUT PHASE C MEASURED and B193 CHECK VERDICT anchors.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


def build_claims(mutation: str) -> dict:
    claims = {
        # A -- authority.
        "main_head": CURRENT_MAIN,
        "parent_commit": PARENT_COMMIT,
        "stale_parent": STALE_PARENT_COMMIT,
        # B -- the banner.
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "locality_supplied": LOCALITY_SUPPLIED_CLAIMED,
        "parity_independent": PARITY_INDEPENDENT_WINDOW_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "transfer_operator": TRANSFER_OPERATOR_CLAIMED,
        "law_proved": LAW_PROVED_FROM_RECURRENCE_CLAIMED,
        "generality": GENERALITY_CLAIMED,
        # C -- the equivalence.
        "volume_derivative": DISPLAYED_VOLUME_DERIVATIVE,
        "volume_derivative_residual": ZERO_RESIDUAL,
        "displayed_law_residual": ZERO_RESIDUAL,
        "carrier_controls": dict(CARRIER_CONTROLS),
        "bump_tangent_residual": ZERO_RESIDUAL,
        "defect_route_residual": DEFECT_ROUTE_RESIDUAL,
        "defect_route_pairs": DEFECT_ROUTE_GATE_PAIRS,
        "first_order_table": dict(FIRST_ORDER_TABLE),
        "finite_equal": FINITE_TABLES_EQUAL_FIRST_ORDER,
        "finite_cells": FINITE_CELL_COUNT,
        "equivalence": EQUIVALENCE_BOTH_DIRECTIONS,
        "six_zero_cells": CHECK_SIX_ZERO_CELLS,
        "six_nonzero_cells": CHECK_SIX_NONZERO_CELLS,
        "block192_cutoff_pairs": BLOCK192_CUTOFF_PAIRS,
        "block192_cutoff_table": dict(BLOCK192_CUTOFF_TABLE),
        # D -- the derivation.
        "transport_residual": TRANSPORT_IDENTITY_RESIDUAL,
        "source_rows": {width: tuple(sizes)
                        for width, sizes in SOURCE_ROW_SIZES.items()},
        "source_slice_rule": SOURCE_SLICE_RULE,
        "response_columns": RESPONSE_SUPPORT_COLUMNS,
        "response_mismatches": RESPONSE_SUPPORT_MISMATCHES,
        "harmonic_failures": HARMONIC_FAILURES,
        "response_relation_pairs": RESPONSE_RELATION_PAIRS,
        "response_relation_residual": RESPONSE_RELATION_RESIDUAL,
        "unit_closed_form_residual": UNIT_CLOSED_FORM_RESIDUAL,
        "unit_closed_form_gates": UNIT_CLOSED_FORM_GATES,
        "dw_link_residual": DW_LINK_RESIDUAL,
        "dw_link_cells": DW_LINK_CELLS,
        # E -- the parity-resolved window law.
        "window_table_sixteen": dict(WINDOW_TABLE_SIXTEEN),
        "window_cells_sixteen": WINDOW_CELLS_SIXTEEN,
        "window_cells_twenty": WINDOW_CELLS_TWENTY,
        "window_law": True,
        "spatially_uniform": SPATIALLY_UNIFORM,
        "parity_switched": PARITY_SWITCHED,
        "odd_offsets": ODD_WINDOW_OFFSETS,
        "even_offsets": EVEN_WINDOW_OFFSETS,
        "window_width": WINDOW_WIDTH_IN_SLICES,
        "core_footprint": CORE_FOOTPRINT_IN_SLICES,
        "odd_density": ODD_BREAK_DENSITY,
        "even_density": EVEN_BREAK_DENSITY,
        "odd_admissible_high": ODD_ADMISSIBLE_HIGH,
        "even_admissible_high": EVEN_ADMISSIBLE_HIGH,
        "cell_block_directions": ODD_CELL_BLOCK_DIRECTIONS,
        "odd_cell_block_breaks": ODD_CELL_BLOCK_BREAKS,
        "even_cell_block_breaks": EVEN_CELL_BLOCK_BREAKS,
        "odd_raw_high": dict(ODD_RAW_HIGH),
        "even_raw_high": dict(EVEN_RAW_HIGH),
        "odd_raw_low": dict(ODD_RAW_LOW),
        "even_raw_low": dict(EVEN_RAW_LOW),
        "union_is_window": UNION_SUPPORT_IS_THE_WINDOW,
        "collapsed_per_even_core": COLLAPSED_FUNCTIONALS_PER_EVEN_CORE,
        "raw_unit_mismatches": RAW_UNIT_MISMATCHES,
        "raw_units_sixteen": RAW_UNITS_SIXTEEN,
        "raw_units_twenty": RAW_UNITS_TWENTY,
        "raw_unit_breaks": dict(RAW_UNIT_BREAKS),
        "invalid_cores": dict(INVALID_CORES),
        "invalid_obey": INVALID_CORES_OBEY_LAW,
        "witness": WITNESS_VALUE,
        # F -- the note, the fence and the nsimplify absence.
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
    }

    # --- A ----------------------------------------------------------------
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_commit"] = STALE_PARENT_COMMIT
    # --- B ----------------------------------------------------------------
    elif mutation == "claim_objects_registered":
        claims["registered"] = 1
        claims["adopted"] = 1
    elif mutation == "claim_gravity_supplied":
        claims["gravity_supplied"] = True
        claims["unsupplied"] = 0
    elif mutation == "claim_locality_supplied":
        claims["locality_supplied"] = True
    elif mutation == "claim_parity_independent":
        # THE REFUTED WINDOW REASSERTED, AND THIS IS THE MUTATION THAT GUARDS
        # THE CHECK'S P2 DISCOVERY: the solve's parity-independent window
        # [t0, t0+2] is asserted to hold at every core.  It does not.
        claims["parity_independent"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
    elif mutation == "claim_transfer_operator":
        claims["transfer_operator"] = True
    elif mutation == "claim_law_proved":
        # THE OPEN LEG DENIED: the window law is asserted to be proved from the
        # staggered recurrence rather than reduced to measured supports.
        claims["law_proved"] = True
    elif mutation == "claim_generality":
        claims["generality"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_import_derivative":
        broken = sp.Matrix(DISPLAYED_VOLUME_DERIVATIVE)
        broken[1, 2] = sp.Rational(-65, 144)
        claims["volume_derivative"] = broken
    elif mutation == "break_carrier_controls":
        claims["carrier_controls"] = {16: (0, 0, 0), 20: (1, 0, 0)}
    elif mutation == "break_defect_route":
        claims["defect_route_residual"] = 1
    elif mutation == "break_first_order_table":
        broken = dict(FIRST_ORDER_TABLE)
        broken[((4, 5), 2)] = 64
        claims["first_order_table"] = broken
    elif mutation == "break_finite_table":
        claims["finite_equal"] = False
    elif mutation == "break_equivalence":
        claims["equivalence"] = False
    elif mutation == "break_six_cells":
        claims["six_zero_cells"] = (((1, 2), 5), ((2, 3), 5), ((3, 4), 5))
    elif mutation == "break_cutoff_instances":
        broken = dict(BLOCK192_CUTOFF_TABLE)
        broken[((4, 5), 1)] = 64
        claims["block192_cutoff_table"] = broken
    # --- D ----------------------------------------------------------------
    elif mutation == "break_transport_identity":
        claims["transport_residual"] = 1
    elif mutation == "break_source_rows":
        claims["source_rows"] = {16: (14, 14, 16, 16, 16, 16, 14, 12),
                                 20: (12, 14, 16, 16, 16, 16, 16, 16, 14, 12)}
    elif mutation == "break_response_support":
        claims["response_mismatches"] = 1
    elif mutation == "break_harmonic_response":
        claims["harmonic_failures"] = 1
    elif mutation == "break_response_relation":
        claims["response_relation_residual"] = 1
    elif mutation == "break_unit_closed_form":
        claims["unit_closed_form_residual"] = 1
    elif mutation == "break_dw_link":
        claims["dw_link_residual"] = 1
    # --- E ----------------------------------------------------------------
    elif mutation == "break_window_sixteen":
        broken = dict(WINDOW_TABLE_SIXTEEN)
        broken[(2, 1)] = 64
        broken[(2, 5)] = 0
        claims["window_table_sixteen"] = broken
    elif mutation == "break_window_twenty":
        claims["window_cells_twenty"] = 63
    elif mutation == "break_parity_switch":
        # THE PARITY SWITCH DENIED AT THE LEVEL OF THE INTERVAL: the even cores
        # are asserted to carry the odd cores' offsets.
        claims["even_offsets"] = ODD_WINDOW_OFFSETS
    elif mutation == "break_break_density":
        # THE FINGERPRINT FLATTENED: the even cores are asserted to break at
        # full density like the odd ones.
        claims["even_density"] = ODD_BREAK_DENSITY
    elif mutation == "break_odd_exemption":
        claims["odd_raw_high"] = {1: (1280, 1), 3: (768, 0)}
    elif mutation == "break_even_refutation":
        # THE CHECK'S P2 DENIED AT THE CENSUS: the odd-core exemption is
        # asserted to survive at the even cores too.
        claims["even_admissible_high"] = 0
        claims["even_raw_high"] = {2: (1024, 0), 4: (512, 0)}
    elif mutation == "break_support_facts":
        claims["union_is_window"] = False
    elif mutation == "break_raw_unit_law":
        claims["raw_unit_mismatches"] = 1
    elif mutation == "break_validity_boundary":
        # THE DOMAIN DENIED: the cores that violate the touch/cross rule are
        # asserted to obey the law anyway.
        claims["invalid_obey"] = True
    # --- F ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 192 artifacts are "
        f"content-identical at it and in the worktree, the stale pin "
        f"{STALE_PARENT_COMMIT[:12]} is a real ancestor carrying NEITHER, the "
        f"machinery import is landed, and {authority.inputs_readable} of "
        f"{len(AUDIT_INPUT_PATHS) - 1} audit inputs are readable",
        authority.parent_pin_is_commit
        and claims["parent_commit"] == PARENT_COMMIT
        and claims["stale_parent"] == STALE_PARENT_COMMIT
        and authority.parent_ref_and_ancestry
        and authority.parent_artifact_blobs
        and not authority.stale_parent_artifact_blobs
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact
        and authority.machinery_import_landed
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
        and not authority.inputs_missing)

    # --- B: THE BANNER AND THE FENCE ---------------------------------------
    checks.check(
        "B-1", f"{facts.imposed} imposed objects, {claims['registered']} "
        f"registered, {claims['adopted']} adopted",
        facts.imposed == claims["imposed"]
        and facts.registered == claims["registered"]
        and facts.adopted == claims["adopted"])
    checks.check(
        "B-2", f"NO GRAVITY IS SUPPLIED: gravity_supplied = "
        f"{claims['gravity_supplied']} and {claims['unsupplied']} gravity "
        f"structures are enumerated as NOT SUPPLIED",
        claims["gravity_supplied"] is False
        and facts.unsupplied == claims["unsupplied"])
    checks.check(
        "B-3", "NO LOCALITY AND NO LIGHT CONE: 'window' names the slices "
        "carrying the nonzero rows of the transport-defect functionals, and "
        "no propagation speed, causal structure or screening length is "
        "supplied",
        claims["locality_supplied"] is False)
    checks.check(
        "B-4", "THE PARITY-INDEPENDENT WINDOW IS NOT CLAIMED: the solve's "
        "window [t0, t0+2] is FALSE at the even cores, which carry "
        "[t0+1, t0+3], and the refutation is this block's central content",
        claims["parity_independent"] is False)
    checks.check(
        "B-5", "NO CONTINUUM AND NO LIMIT: one fixture, two widths, one "
        "profile family, three amplitudes",
        claims["continuum_limit"] is False)
    checks.check(
        "B-6", "W IS NOT A TRANSFER OPERATOR: Block 190 refuted the naive OS "
        "transfer pairing on this class and nothing here repairs it",
        claims["transfer_operator"] is False)
    checks.check(
        "B-7", "THE LAW IS NOT PROVED FROM THE STAGGERED RECURRENCE: it is "
        "REDUCED to the bilinear identity plus TWO MEASURED support facts, "
        "and the closed forms of those supports are measured at two widths",
        claims["law_proved"] is False)
    checks.check(
        "B-8", "NO GENERALITY IS CLAIMED: no second fixture, no third width, "
        "no other profile family and nothing about the infinite-width limit",
        claims["generality"] is False)

    # --- C: THE EQUIVALENCE -------------------------------------------------
    checks.check(
        "C-1", f"dB = d/d(delta) shear_hodge(c, 1-delta) at delta = 0 equals "
        f"-E00 - (169/144)(E11+E22) + (65/144)(E12+E21) + E33 entrywise "
        f"against the SYMBOLIC derivative of the import, residual "
        f"{facts.volume_derivative_residual}, with the displayed law gated at "
        f"BOTH probed volumes at residual {facts.displayed_law_residual}",
        facts.volume_derivative == claims["volume_derivative"]
        and facts.volume_derivative_residual
        == claims["volume_derivative_residual"]
        and facts.displayed_law_residual == claims["displayed_law_residual"])
    checks.check(
        "C-2", f"the carrier controls close at BOTH widths: "
        f"(nnz(Q G - I), nnz(Ps H Ps - H), nnz(Ps Q Ps - Q^T)) = "
        f"{facts.carrier_controls}, and this block's one-cell tangents SUM to "
        f"Block 192's bump tangent at residual "
        f"{set(facts.bump_tangent_residual.values())} at all four bumps",
        facts.carrier_controls == claims["carrier_controls"]
        and all(value == claims["bump_tangent_residual"]
                for value in facts.bump_tangent_residual.values()))
    checks.check(
        "C-3", f"the defect-functional route R = -u_b^T dQ G[:, theta_a] "
        f"agrees with the FULL dG route entrywise at "
        f"{len(facts.defect_route)} gate pairs, residual "
        f"{set(facts.defect_route.values())}",
        len(facts.defect_route) == claims["defect_route_pairs"]
        and all(value == claims["defect_route_residual"]
                for value in facts.defect_route.values()))
    checks.check(
        "C-4", f"nnz(R) over the twenty valid (bump, core) pairs at T = 16 is "
        f"the declared table, with FIVE exact zeros, FOURTEEN full entries "
        f"and ONE at HALF density",
        facts.first_order_table == claims["first_order_table"])
    checks.check(
        "C-5", f"nnz(W(delta) - W(0)) at delta = 1/5, 1/3 and 2/5 reproduces "
        f"that table ENTRY FOR ENTRY in all {facts.equivalence_cells} finite "
        f"rebuilds",
        facts.finite_equal_first_order == claims["finite_equal"]
        and facts.equivalence_cells == claims["finite_cells"])
    checks.check(
        "C-6", f"the biconditional holds in both directions over all "
        f"{claims['finite_cells']} (bump, amplitude, core) cells: "
        f"W(delta) = W(0) matrix-exact if and only if R = 0",
        facts.equivalence == claims["equivalence"])
    checks.check(
        "C-7", f"the adversarial check's six requested cells are exactly "
        f"{claims['six_zero_cells']} zero and {claims['six_nonzero_cells']} "
        f"fully dense, at first order and at both of its amplitudes",
        all(facts.first_order_table[cell] == 0
            for cell in claims["six_zero_cells"])
        and all(facts.first_order_table[cell] == 64
                for cell in claims["six_nonzero_cells"])
        and all(facts.finite_tables[(cell[0], amplitude, cell[1])] == 0
                for cell in claims["six_zero_cells"]
                for amplitude in AMPLITUDES)
        and all(facts.finite_tables[(cell[0], amplitude, cell[1])] == 64
                for cell in claims["six_nonzero_cells"]
                for amplitude in AMPLITUDES))
    checks.check(
        "C-8", f"Block 192's twelve-entry odd-core cutoff table is reproduced "
        f"entry for entry and its three cutoff pairs "
        f"{claims['block192_cutoff_pairs']} are INSTANCES of this block's law",
        all(facts.first_order_table[key] == value
            for key, value in claims["block192_cutoff_table"].items())
        and all(facts.first_order_table[pair] == 0
                for pair in claims["block192_cutoff_pairs"])
        and all(breaks_predicted(pair[1], pair[0][0]) is False
                and breaks_predicted(pair[1], pair[0][1]) is False
                for pair in claims["block192_cutoff_pairs"]))

    # --- D: THE HARMONIC-RESPONSE DERIVATION -------------------------------
    checks.check(
        "D-1", f"K_c W = L_2 is the DEFINITION of W and closes at every one of "
        f"the {len(facts.transport_residual)} core frames at both widths: "
        f"nnz(K_c W - L_2) = 0",
        all(value == claims["transport_residual"]
            for value in facts.transport_residual.values()))
    checks.check(
        "D-2", f"the dQ row-support sizes are {claims['source_rows'][16]} at "
        f"T = 16 and {claims['source_rows'][20]} at T = 20, and every positive "
        f"slice support is exactly [2*floor(s/2), 2*floor(s/2)+2]",
        all(tuple(facts.source_rows[(width, anchor)]
                  for anchor in range(width // 2))
            == claims["source_rows"][width] for width in WIDTHS)
        and facts.source_slice_rule == claims["source_slice_rule"])
    checks.check(
        "D-3", f"the response field's row support equals the FULL row support "
        f"of dQ with NO cancellation in all {facts.response_columns} tested "
        f"columns, {facts.response_mismatches} mismatches",
        facts.response_columns == claims["response_columns"]
        and facts.response_mismatches == claims["response_mismatches"])
    checks.check(
        "D-4", f"the response field is Q-harmonic off the source rows: "
        f"Q rho_a = dQ G[:, theta_a] at {facts.harmonic_failures} failures "
        f"over the same {claims['response_columns']} columns",
        facts.harmonic_failures == claims["harmonic_failures"])
    checks.check(
        "D-5", f"R = 0 is EXACTLY the statement that the response field obeys "
        f"the same two-step defect relation: nnz(relation + R) = 0 at all "
        f"{len(facts.response_relation)} (anchor, core) pairs",
        len(facts.response_relation) == claims["response_relation_pairs"]
        and all(value == claims["response_relation_residual"]
                for value in facts.response_relation.values()))
    checks.check(
        "D-6", f"the raw-unit closed form R[a,b] = -(u_b[p] Cm[q,a] - "
        f"(D u_b)[p] C[q,a]) agrees with the matrix route at "
        f"{len(facts.unit_closed_form)} gates, residual "
        f"{set(facts.unit_closed_form)}",
        len(facts.unit_closed_form) == claims["unit_closed_form_gates"]
        and all(value == claims["unit_closed_form_residual"]
                for value in facts.unit_closed_form))
    checks.check(
        "D-7", f"R = K_c dW at zero residual so R = 0 if and only if dW = 0, "
        f"and nnz(dW) = nnz(R) at all {len(facts.dw_link)} cells",
        len(facts.dw_link) == claims["dw_link_cells"]
        and all(value[0] == value[1] and value[2] == claims["dw_link_residual"]
                for value in facts.dw_link.values()))

    # --- E: THE PARITY-RESOLVED WINDOW LAW ---------------------------------
    checks.check(
        "E-1", f"the {claims['window_cells_sixteen']}-cell incidence table at "
        f"T = 16 is the declared table and obeys the law, spatially uniform in "
        f"all four spatial anchors",
        {key: value for key, value in facts.window_tables[16].items()
         if key[0] + 3 <= 8} == claims["window_table_sixteen"]
        and facts.window_law[16][0] == claims["window_law"]
        and facts.window_law[16][1] == claims["window_cells_sixteen"]
        and facts.spatial_uniform[16] == claims["spatially_uniform"])
    checks.check(
        "E-2", f"the law holds again at a SECOND width over "
        f"{claims['window_cells_twenty']} cells at T = 20, spatially uniform, "
        f"with zero exceptions",
        facts.window_law[20][0] == claims["window_law"]
        and facts.window_law[20][1] == claims["window_cells_twenty"]
        and facts.spatial_uniform[20] == claims["spatially_uniform"])
    checks.check(
        "E-3", f"the window is {claims['window_width']} slices of the core's "
        f"{claims['core_footprint']}-slice footprint, at offsets "
        f"{claims['odd_offsets']} for ODD cores and {claims['even_offsets']} "
        f"for EVEN cores -- one exempt end, SWITCHED BY PARITY, and unified as "
        f"[2*floor(t0/2)+1, 2*floor(t0/2)+3]",
        claims["parity_switched"] is True
        and claims["window_width"] == 3
        and claims["core_footprint"] == 4
        and all(facts.union_supports[(width, core)]
                == tuple(core + offset
                         for offset in range(claims["odd_offsets"][0],
                                             claims["odd_offsets"][1] + 1))
                for width in WIDTHS
                for core in range(1, width // 2)
                if core % 2 == 1 and core + 3 <= width // 2)
        and all(facts.union_supports[(width, core)]
                == tuple(core + offset
                         for offset in range(claims["even_offsets"][0],
                                             claims["even_offsets"][1] + 1))
                for width in WIDTHS
                for core in range(1, width // 2)
                if core % 2 == 0 and core + 3 <= width // 2))
    checks.check(
        "E-4", f"the break density over the four breaking anchors in order is "
        f"{claims['odd_density']} at every ODD core and "
        f"{claims['even_density']} at every EVEN core, at both widths",
        all(value == (claims["odd_density"] if core % 2 else
                      claims["even_density"])
            for (_width, core), value in facts.break_density.items()))
    checks.check(
        "E-5", f"the t0+3 exemption survives EVERY attack at the odd cores "
        f"{ODD_EXEMPTION_CORES}: the admissible cell at all four spatial "
        f"anchors, all {claims['cell_block_directions']} cell-block "
        f"directions including the asymmetric ones, and the raw census "
        f"{claims['odd_raw_high']} with an ARBITRARY column",
        all(facts.exemption[core]["admissible_high"]
            == (claims["odd_admissible_high"],) * SPACE_EXTENT
            and facts.exemption[core]["cell_block_directions"]
            == claims["cell_block_directions"]
            and facts.exemption[core]["cell_block_breaks"]
            == claims["odd_cell_block_breaks"]
            and facts.exemption[core]["raw_high"] == claims["odd_raw_high"][core]
            for core in ODD_EXEMPTION_CORES))
    checks.check(
        "E-6", f"that same exemption is REFUTED at the even cores "
        f"{EVEN_EXEMPTION_CORES} -- the admissible t0+3 cell breaks at "
        f"nnz(R) = {claims['even_admissible_high']} and the raw census is "
        f"{claims['even_raw_high']} -- while the DUAL low-end exemption is "
        f"exhaustive there, {claims['even_raw_low']}, and fails at the odd "
        f"cores, {claims['odd_raw_low']}",
        all(facts.exemption[core]["admissible_high"]
            == (claims["even_admissible_high"],) * SPACE_EXTENT
            and facts.exemption[core]["cell_block_breaks"]
            == claims["even_cell_block_breaks"]
            and facts.exemption[core]["raw_high"] == claims["even_raw_high"][core]
            and facts.exemption[core]["raw_low"] == claims["even_raw_low"][core]
            for core in EVEN_EXEMPTION_CORES)
        and all(facts.exemption[core]["raw_low"] == claims["odd_raw_low"][core]
                for core in ODD_EXEMPTION_CORES))
    checks.check(
        "E-7", f"SUPPORT FACT ONE: the union slice support of the eight "
        f"functionals u_b is EXACTLY the window at every valid core at both "
        f"widths, with no negative-half support; and exactly "
        f"{claims['collapsed_per_even_core']} of the eight COLLAPSE to a "
        f"single slice at every even core",
        all(value for key, value in facts.union_matches_window.items()
            if key[1] + 3 <= key[0] // 2) == claims["union_is_window"]
        and all(len(facts.collapsed[(width, core)])
                == (claims["collapsed_per_even_core"] if core % 2 == 0 else 0)
                for width in WIDTHS for core in range(1, width // 2)
                if core + 3 <= width // 2))
    checks.check(
        "E-8", f"THE RAW-UNIT LAW: for E_{{p,q}} the residual is nonzero if and "
        f"only if the ROW p lies on a window slice, for EVERY column q -- "
        f"{claims['raw_units_sixteen']} units at T = 16 and "
        f"{claims['raw_units_twenty']} at T = 20, "
        f"{claims['raw_unit_mismatches']} mismatches, with "
        f"{claims['raw_unit_breaks']} breaking units per core",
        sum(value[0] for key, value in facts.raw_units.items() if key[0] == 16)
        == claims["raw_units_sixteen"]
        and sum(value[0] for key, value in facts.raw_units.items()
                if key[0] == 20) == claims["raw_units_twenty"]
        and all(value[2] == claims["raw_unit_mismatches"]
                for value in facts.raw_units.values())
        and all(value[1] == claims["raw_unit_breaks"][key[0]]
                for key, value in facts.raw_units.items()))
    checks.check(
        "E-9", f"the law's DOMAIN is exactly Block 191's touch/cross rule: the "
        f"cores {claims['invalid_cores']} violate t0+3 <= T/2 and do NOT obey "
        f"the law nor carry a three-slice window; and the exact unexpected-"
        f"break witness at (t0, s) = {WITNESS_CELL}, entry R{WITNESS_ENTRY}, "
        f"is the declared rational",
        tuple(sorted(key[1] for key in facts.invalid_obey if key[0] == 16))
        == tuple(sorted(claims["invalid_cores"][16]))
        and tuple(sorted(key[1] for key in facts.invalid_obey if key[0] == 20))
        == tuple(sorted(claims["invalid_cores"][20]))
        and all(value[0] == claims["invalid_obey"]
                and value[1] == claims["invalid_obey"]
                for value in facts.invalid_obey.values())
        and facts.witness == claims["witness"])

    # --- F: THE NOTE, THE FENCE AND THE nsimplify ABSENCE -------------------
    checks.check(
        "F-1", f"the note is landed at docs/{FINAL_NOTE_NAME}",
        NOTE_PATH.is_file() == claims["note_present"])
    checks.check(
        "F-2", "the N5 fence appears in the note byte-identically to this "
        "runner's single-line constant",
        facts.scope == claims["scope"])
    checks.check(
        "F-3", f"sp.nsimplify occurs {facts.nsimplify_calls} times in this "
        f"runner's own source",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED")
    print(f"  elapsed: {elapsed_ns / 1e9:.1f}s")
    print(f"  origin/main {facts.main_head}")
    print(f"  authority {facts.authority}")
    print(f"  imposed {facts.imposed}, registered {facts.registered}, "
          f"adopted {facts.adopted}, gravity structures NOT SUPPLIED "
          f"{facts.unsupplied}")
    print(f"  check verdict carried: {CHECK_VERDICT}")
    print(f"  THE IMPORT: dB = {facts.volume_derivative.tolist()}")
    print(f"    dB vs the IMPORT's symbolic derivative: residual "
          f"{facts.volume_derivative_residual}; displayed law residual "
          f"{facts.displayed_law_residual}")
    print(f"    carrier controls (QG-I, PsHPs-H, PsQPs-Q^T) "
          f"{facts.carrier_controls}")
    print(f"    one-cell tangents SUM to Block 192's bump tangent: "
          f"{facts.bump_tangent_residual}")
    print(f"    defect route vs FULL dG route {facts.defect_route}")
    print(f"  THE EQUIVALENCE: first order {facts.first_order_table}")
    print(f"    finite tables equal the first-order table entry for entry: "
          f"{facts.finite_equal_first_order} over {facts.equivalence_cells} "
          f"rebuilds; biconditional {facts.equivalence}")
    for key in sorted(facts.finite_tables, key=str):
        if facts.finite_tables[key] != facts.first_order_table[
                (key[0], key[2])]:
            print(f"      DISAGREEMENT at {key}")
    print(f"  THE DERIVATION: transport residuals "
          f"{set(facts.transport_residual.values())} over "
          f"{len(facts.transport_residual)} frames")
    print(f"    dQ row sizes {facts.source_rows}")
    print(f"    dQ positive slice supports {facts.source_slices}")
    print(f"    response columns {facts.response_columns}, support mismatches "
          f"{facts.response_mismatches}, harmonic failures "
          f"{facts.harmonic_failures}")
    print(f"    response relation + R over {len(facts.response_relation)} "
          f"pairs: {set(facts.response_relation.values())}")
    print(f"    raw-unit closed form gates {facts.unit_closed_form}")
    print(f"    (nnz(R), nnz(dW), nnz(K_c dW - R)) "
          f"{set(facts.dw_link.values())}")
    print("  THE PARITY-RESOLVED WINDOW LAW")
    for width in WIDTHS:
        half = width // 2
        print(f"    T = {width}: law {facts.window_law[width]} spatially "
              f"uniform {facts.spatial_uniform[width]}")
        for core in range(1, half):
            row = " ".join(f"s{anchor}:{facts.window_tables[width][(core, anchor)]}"
                           for anchor in range(half))
            print(f"      t0={core} window {facts.union_supports[(width, core)]}"
                  f" | {row}")
    print(f"    break densities {facts.break_density}")
    print(f"    collapsed functionals per core {facts.collapsed}")
    print(f"    raw-unit census (total, breaking, mismatches) "
          f"{facts.raw_units}")
    print(f"    invalid cores (union is a window?, law holds?) "
          f"{facts.invalid_obey}")
    for core, record in sorted(facts.exemption.items()):
        print(f"    exemption t0={core}: {record}")
    print(f"    witness R{WITNESS_ENTRY} at {WITNESS_CELL} = {facts.witness}")
    print(f"  nsimplify occurrences: {facts.nsimplify_calls}")
    print("  SCOPE: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. NO GRAVITY "
          "IS SUPPLIED AND NO LOCALITY PRINCIPLE IS ESTABLISHED: delta is a "
          "dial on an IMPOSED Hodge-volume parameter and 'response' names "
          "d/d(delta) of a rational matrix entry. 'WINDOW', 'TRANSPORT', "
          "'HARMONIC' AND 'RESPONSE' NAME PROPERTIES OF EXACT RATIONAL "
          "MATRICES. THE WINDOW IS NOT A LIGHT CONE. THE PARITY-INDEPENDENT "
          "WINDOW IS REFUTED. THE LAW IS REDUCED TO TWO MEASURED SUPPORT "
          "FACTS AND IS NOT PROVED FROM THE RECURRENCE. ONE FIXTURE, TWO "
          "WIDTHS, ONE PROFILE FAMILY AND THREE AMPLITUDES IS NOT A SCAN.")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No family can cascade into another
    # because no gate feeds a measurement.
    facts = measure()
    elapsed_ns = time.monotonic_ns() - started_ns

    checks = build_checks(facts, build_claims(""))
    if mutation:
        raw = checks.families()
        checks = build_checks(facts, build_claims(mutation))
        mutated = checks.families()
        target = MUTATION_GATE[mutation]
        changed = {family for family in raw if raw[family] != mutated[family]}
        if changed - {target} or mutated[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    report_measured(facts, elapsed_ns)
    checks.report()
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
