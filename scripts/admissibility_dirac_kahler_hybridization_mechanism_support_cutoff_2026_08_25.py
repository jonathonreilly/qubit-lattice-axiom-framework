#!/usr/bin/env python3
"""BLOCK 192 -- THE FIRST-ORDER HYBRIDIZATION MECHANISM IN CLOSED FORM, AND THE
EXACT SUPPORT-CUTOFF LAW OF THE UNIT-CELL MONODROMY.

THE RESULT, AND ITS EXACT SCOPE.  On BLOCK 190's wrap-edge width family at the
SAME fixture (m, c) = (9/20, 5/13) and the SAME width T = 16, Block 191's
localized Hodge-volume bump is differentiated: the response of the unit-cell
monodromy W = K_c^-1 L_2 to a one-slice volume bump is obtained in CLOSED FORM
by a four-step derivative chain that NEVER inverts a symbolic matrix, and the
per-factor first-order trace responses are exact rationals.  ALL OF IT IS
FINITE EXACT LINEAR ALGEBRA ON ONE CONSTRUCTED MATRIX FAMILY.  NONE OF IT
ESTABLISHES A LAPSE, A PERTURBATION OF A PHYSICAL SYSTEM, A CONTINUUM LIMIT, A
PROPAGATION SPEED OR A LIGHT CONE.  'HYBRIDIZATION', 'LOCKING' AND 'SUPPORT
CUTOFF' NAME PROPERTIES OF EXACT RATIONAL MATRICES AND OF NOTHING ELSE, AND
THEY ARE FENCED BEFORE THE FIRST NUMBER IS READ.

  0. THE METHOD THEOREM, AND IT IS A CHAIN OF FOUR DISPLAYED IDENTITIES (C).
     With v = 1 - delta on the bumped positive anchors, the volume derivative
     of Block 105's shear block is
     dB = -E00 - (169/144)(E11 + E22) + (65/144)(E12 + E21) + E33,
     GATED against the symbolic derivative of the IMPORTED shear_hodge(c, 1-d)
     entrywise; H is a cell sum so dH is the same cell sum over the bumped
     anchors AND their thA_s image partners with P_4 dB P_4^T on the images;
     dQ = m dH + dH D_s - D_s^T dH because D_s does not depend on delta;
     dG = -G dQ G with the KNOWN v = 1 inverse; and the core restriction gives
     dW = K_c^-1 (dL_2 - dK_c W).  NO SYMBOLIC MATRIX IS EVER INVERTED.  Every
     link is gated at EXACTLY ZERO residual, dH and dQ additionally against an
     entrywise SYMBOLIC differentiation of the displayed profile, and dW
     against an INDEPENDENT exact-rational finite-difference route.

  1. THE TEN RATIONALS AND THE FOUR SUM RULES (D).  At the near-edge core
     t0 = 1 the spectrum carries THREE labelled factors and at t0 = 3 it
     carries TWO, so the two bumps {3,4} and {2,3} give TEN exact per-factor
     first-order trace responses tr(P_f dW).  All ten are NONZERO rationals,
     all four sum rules tr(dW) = sum_f tr(P_f dW) hold at exact equality, every
     CRT congruence q_f = 1 mod f^k and q_f = 0 mod g^l holds as a ZERO
     polynomial residual, and the projectors built from the FULL multiplicities
     and from the SQUAREFREE total agree ENTRYWISE, not merely in trace.

  2. THE RESPONSE TABLE, WITH THE SOLVE'S QUANTIFIER DROPPED (E).  At t0 = 1
     the heavy and boundary responses have the SAME SIGN at each bump position
     and FLIP TOGETHER between them, positive at {3,4} and negative at {2,3},
     while the light response stays POSITIVE at both.  Their exact differences
     are 61132656/1842661567 and 56249856/1842661567 -- NONZERO, and over the
     SAME denominator.  THE SOLVE'S RELATIVE-AGREEMENT QUANTIFIER IS DROPPED
     AND NOT SOFTENED: the check measured the {2,3} relative difference ABOVE
     the quoted rational threshold 1/100 under all three standard
     normalizations, so this block records the exact ratios and claims the
     SIGN structure only.  At t0 = 3 the on-site bump is heavy-dominated at the
     exact ratio 37533905844768035289054578457791/4229425500383349914656444790625
     and the distance-one bump is scale-balanced at 232340137594542523/
     244263525398539845.

  3. THE SUPPORT-CUTOFF LAW, WHICH IS THE CHECK'S DISCOVERY AND THIS BLOCK'S
     CENTRE (F).  The bump response is NOT globally decaying.  Over the twelve
     valid (bump, core) pairs of bumps {1,2}, {2,3}, {3,4}, {4,5} against cores
     t0 = 1, 3, 5, exactly THREE are EXACTLY ZERO -- ({1,2}, 5), ({2,3}, 5) and
     ({4,5}, 1) -- at first order AND at the finite amplitudes delta = 1/5 and
     delta = 1/7, where the WHOLE 8 x 8 operator is unchanged entrywise.  The
     first-order table and the finite table are IDENTICAL, so the cutoff is not
     a linearization artefact.  AND IT IS DIRECTIONAL, NOT RADIAL: bump {3,4}
     reaches t0 = 5 while bump {2,3} does not, and bump {4,5} misses t0 = 1
     while bump {3,4} reaches it.

  4. THE MECHANISM IS MEASURED AND THE ROUTING READING IS REFUTED (F).  At all
     three cutoff pairs dG is DENSE -- 3968 of 4096 entries nonzero -- and dK_c
     is FULL, so nothing is 'routed away' in the support sense.  What is exact
     is a PAIRING GAUGE: dL_2 = dK_c W at zero residual, and at finite delta
     K_c and L_2 are carried by a COMMON LEFT FACTOR M = K_c(delta) K_c^-1 with
     M != I in all 64 entries and L_2(delta) = M L_2 exactly.  W = K_c^-1 L_2
     is invariant under exactly that motion.  THE NAIVE SUPPORT-OVERLAP RULE IS
     REFUTED, MEASURED: emptiness of the overlap implies the zero in 2 of 2
     cases, but NON-emptiness does NOT imply a nonzero response -- ({4,5}, 1)
     overlaps the read window at t = 4 and still gives 0_8.  The empty-cross
     routing account is a NAMED OPEN LEG.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY: no lapse
variable, no ADM phase space, no constraint, no gauge orbit, no quotient, no
Dirac observable and no OS reconstruction is supplied, and ten such structures
are enumerated.  NO PHYSICAL PERTURBATION: delta is a dial on an imposed Hodge
volume and 'response' names d/d(delta) of a rational matrix entry.  NO
CONTINUUM AND NO LIMIT: one width, one fixture, four bump positions, three
amplitudes, and nothing about T -> infinity.  NO PROPAGATION: the support
cutoff is a statement about which exact matrices are equal and is NOT a light
cone, a causal structure or a propagation speed.  NO LOCKING THRESHOLD: the
solve's relative-agreement quantifier is DROPPED, and only the sign structure
is claimed.  NO DERIVED MECHANISM: the routing account of the cutoff is a
READING and a named open leg.  NO GENERALITY.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 191 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, physical hybridization, the relative-
     agreement threshold, the continuum limit, the transfer operator, the
     derived mechanism and generality ALL declared NOT CLAIMED as measured
     constants, and ten gravity structures enumerated as NOT SUPPLIED.
  C  THE METHOD THEOREM: the displayed dB against the symbolic derivative of
     the import and the displayed shear law at both probed volumes; the
     entrywise symbolic agreement of dH and dQ; the two resolvent residuals;
     the core-equation residual; the chain fingerprints; and the independent
     finite-difference route, entrywise monotone and Richardson-converged, with
     EXACT entrywise equality at the three cutoff pairs.
  D  THE TEN RATIONALS: all ten exact values, their nonvanishing, the four
     exact trace totals, the four sum rules, every CRT congruence, the
     projector partitions of I_8, the squarefree annihilator, and the ENTRYWISE
     equality of the full-multiplicity and squarefree projectors.
  E  THE RESPONSE TABLE: the two exact heavy/boundary differences with their
     shared denominator, their nonvanishing, the joint sign flip, light sign
     stability, the exact on-site and distance-one ratios with their exact
     rational brackets, and the six enumerated relative readings with the
     solve's threshold recorded as FAILING at one of its two positions.
  F  THE SUPPORT-CUTOFF LAW: the twelve-pair first-order table, the twelve-pair
     finite table at delta = 1/5, their exact agreement, the second amplitude
     delta = 1/7, the exact (0, 0, 0) triple at ({4,5}, 1), the exact
     entrywise operator zeros, the pairing-gauge identities, the DENSE dG that
     refutes support routing, and the refuted overlap signature with its single
     measured counterexample.
  G  the note at its final path, the N5 fence byte-identical, and the
     nsimplify count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through G PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: forty-three declared mutations, each of which rewrites
  ONE CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement
  happens once, before any mutation flag is consulted, so a mutation can only
  rewrite a CLAIM and no gate can cascade into another.  The per-family census
  is A 2, B 8, C 8, D 7, E 7, F 9, G 2.
  FIVE OF THE FORTY-THREE GUARD CORRECTIONS RATHER THAN RESULTS:
  claim_locking_threshold asserts the dropped relative-agreement quantifier;
  break_relative_readings rewrites the exact ratios that replaced it;
  break_dense_resolvent asserts the refuted support-routing account;
  break_overlap_rule asserts the refuted overlap signature; and
  claim_mechanism_derived asserts that the cutoff's mechanism is derived.

RUNNING
  python3
  scripts/admissibility_dirac_kahler_hybridization_mechanism_support_cutoff_2026_08_25.py
  python3 ... --list-mutations
  python3 ... --mutation break_overlap_rule
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
# shear_hodge() re-exported by the Block 128 module.  Block 191 varied its
# second argument at rational points; this block differentiates it, so the
# import is read at a SYMBOLIC volume and its derivative is the gate.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_HYBRIDIZATION_MECHANISM_SUPPORT_CUTOFF_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 191 is the commit this block's
# branch is cut from; its note and its runner both exist at PARENT_COMMIT and
# NEITHER exists at STALE_PARENT_COMMIT, which is the Block 190 tip.
BLOCK191_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK191_RUNNER = (
    "scripts/admissibility_dirac_kahler_boundary_mode_volume_sensitivity_"
    "2026_08_25.py"
)
PARENT_ARTIFACTS = (BLOCK191_NOTE, BLOCK191_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "f36eb5af1c5ca4db761e21782031ca13de63d652",   # Block 191 note
    "9d507f15fb54b9ba1955c97f4ecf53042d8870ba",   # Block 191 runner
)
# THE CONSTRUCTION AUTHORITY: Block 190's width family, whose carrier, cores and
# monodromy are carried unchanged; Block 105's primary, whose shear_hodge(c, v)
# is the function this block differentiates; and Block 188's site route, which
# the width family is a disclosed variant of.
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HYBRIDIZATION_MECHANISM_SUPPORT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_boundary_mode_volume_sensitivity_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 191 RUNNER AND RE-RESOLVED AT
# DRAFT TIME; the main pin is re-verified live before the branch is cut.
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block191-"
              "boundary-mode-volume-sensitivity-20260825")
PARENT_COMMIT = "36f54ab2ad6e51cbe2bf6b8b604b63236f2c936e"
# The Block 190 tip: a real ancestor of HEAD that predates Block 191 and
# therefore carries NEITHER Block 191 artifact.
STALE_PARENT_COMMIT = "e75ad9f4998ae4cc6a25a2e20191e0b9d76ff3fd"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_hybridization_physical",
    "claim_locking_threshold",
    "claim_continuum_limit",
    "claim_transfer_operator",
    "claim_mechanism_derived",
    "claim_generality",
    "break_volume_derivative_block",
    "break_displayed_shear_law",
    "break_action_derivative_law",
    "break_resolvent_law",
    "break_monodromy_derivative_law",
    "break_symbolic_agreement",
    "break_chain_fingerprints",
    "break_finite_difference_route",
    "break_ten_rationals",
    "break_responses_nonzero",
    "break_trace_totals",
    "break_sum_rules",
    "break_crt_congruences",
    "break_projector_partition",
    "break_squarefree_projectors",
    "break_response_differences",
    "break_shared_denominator",
    "break_joint_sign_flip",
    "break_light_sign_stability",
    "break_onsite_ratio",
    "break_distance_one_ratio",
    "break_relative_readings",
    "break_cutoff_table",
    "break_finite_cutoff_table",
    "break_order_agreement",
    "break_second_amplitude",
    "break_operator_zeros",
    "break_extra_bump_triple",
    "break_pairing_gauge",
    "break_dense_resolvent",
    "break_overlap_rule",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_hybridization_physical": "B",
    "claim_locking_threshold": "B",
    "claim_continuum_limit": "B",
    "claim_transfer_operator": "B",
    "claim_mechanism_derived": "B",
    "claim_generality": "B",
    "break_volume_derivative_block": "C",
    "break_displayed_shear_law": "C",
    "break_action_derivative_law": "C",
    "break_resolvent_law": "C",
    "break_monodromy_derivative_law": "C",
    "break_symbolic_agreement": "C",
    "break_chain_fingerprints": "C",
    "break_finite_difference_route": "C",
    "break_ten_rationals": "D",
    "break_responses_nonzero": "D",
    "break_trace_totals": "D",
    "break_sum_rules": "D",
    "break_crt_congruences": "D",
    "break_projector_partition": "D",
    "break_squarefree_projectors": "D",
    "break_response_differences": "E",
    "break_shared_denominator": "E",
    "break_joint_sign_flip": "E",
    "break_light_sign_stability": "E",
    "break_onsite_ratio": "E",
    "break_distance_one_ratio": "E",
    "break_relative_readings": "E",
    "break_cutoff_table": "F",
    "break_finite_cutoff_table": "F",
    "break_order_agreement": "F",
    "break_second_amplitude": "F",
    "break_operator_zeros": "F",
    "break_extra_bump_triple": "F",
    "break_pairing_gauge": "F",
    "break_dense_resolvent": "F",
    "break_overlap_rule": "F",
    "drop_n5_fence": "G",
    "break_nsimplify_absence": "G",
}
MUTATED_FAMILIES = "ABCDEFG"


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
    "BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16, CARRIED UNCHANGED THROUGH BLOCK 191 AND STILL A DISCLOSED VARIANT OF BLOCK 188's SITE CONSTRUCTION: the staggered Dirac-Kahler carrier on Z_16 x Z_4 with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, 8}, the site raising set A_s of the d_K entries in the CLOSED half {0..8} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13)",
    "BLOCK 191's VOLUME PROFILE, CARRIED UNCHANGED: a map v from the positive anchors {0..7} to the positive rationals, placed as block(t) = B(c, v(t)) for t < 8 and as the P_4 image block(t) = P_4 B(c, v(thA_s(t))) P_4^T for t >= 8 with thA_s(t) = -1-t, assembled into H by the quarter-weighted four-corner cell average -- IMPOSED, and reducing to Block 190's rule IDENTICALLY at any uniform profile",
    "THE ONE-PARAMETER BUMP FAMILY v = 1 - delta, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT: the profile that carries the value 1 - delta on a chosen pair of adjacent positive anchors and 1 elsewhere, read at delta = 0 as the baseline, differentiated at delta = 0, and evaluated at the three finite amplitudes delta = 1/5, 1/7 and 1/100 with its halving 1/200 -- CHOSEN BY THIS BLOCK AND DERIVED FROM NOTHING",
    "THE FOUR BUMP POSITIONS {1,2}, {2,3}, {3,4} AND {4,5} AND THE THREE VALID PROBE CORES t0 = 1, 3, 5 -- TWELVE PAIRS, CHOSEN because every bump lies in the positive-anchor domain {0..7} and every core satisfies Block 191's touch/cross rule t0 + 3 <= 8; FOUR POSITIONS ARE NOT A SCAN AND THREE CORES ARE NOT A SCAN",
    "THE PAIR CORES AND THEIR SHIFTED PAIRINGS, BLOCK 190's OBJECTS UNCHANGED: K_c[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)], L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, and the UNIT-CELL MONODROMY W = K_c^-1 L_2 -- NOT a derived transfer operator of any theory, and explicitly NOT repaired as one by this block",
    "THE THREE LABELLED SPECTRAL FACTORS AND THEIR CRT PROJECTORS: heavy = 22569375 z^2 - 233631106 z + 22569375, light = 39529825 z^2 - 109432706 z + 39529825 and boundary = 43033320714375 z^2 - 445467467014578 z + 48554286398375, LANDED BY BLOCK 191 and used here only as the labels of an exact rational CRT decomposition of the baseline W -- the word 'boundary' NAMES A FACTOR and nothing physical",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SEVEN ARE FALSE
# AND STAY FALSE.  THE THIRD IS THE ONE THE ADVERSARIAL CHECK REFUTED.
GRAVITY_SUPPLIED_CLAIMED = False
HYBRIDIZATION_PHYSICAL_CLAIMED = False
LOCKING_THRESHOLD_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
TRANSFER_OPERATOR_CLAIMED = False
MECHANISM_DERIVED_CLAIMED = False
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
CHECK_VERDICT = "CONFIRMED-EXCEPT-ONE-QUANTIFIER-WITH-TWO-DISCOVERIES-FOLDED"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
WIDTH = 16
SPACE_EXTENT = 4
SITE_COUNT = WIDTH * SPACE_EXTENT
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)
BUMP_VOLUME = sp.Rational(4, 5)
BUMPS = ((1, 2), (2, 3), (3, 4), (4, 5))
CORES = (1, 3, 5)
RESPONSE_BUMPS = ((3, 4), (2, 3))
RESPONSE_CORES = (1, 3)
EXTRA_BUMP = (4, 5)
EXTRA_CORE = 1

# --- C: THE METHOD THEOREM --------------------------------------------------
# dB = d/d(delta) shear_hodge(c, 1 - delta) at delta = 0, written as the note
# writes it and gated against the SYMBOLIC derivative of the import.
DISPLAYED_VOLUME_DERIVATIVE = sp.Matrix([
    [-1, 0, 0, 0],
    [0, sp.Rational(-169, 144), sp.Rational(65, 144), 0],
    [0, sp.Rational(65, 144), sp.Rational(-169, 144), 0],
    [0, 0, 0, 1]])
# and the two probed volumes of the underlying law, carried from Block 191 so
# that the function being differentiated is pinned to the landed one.
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
# THE CHAIN FINGERPRINTS: nnz(dH) is the same 56 for every bump; nnz(dQ)
# depends only on the PARITY of the leading anchor; dG is DENSE and dW is FULL
# wherever it is not exactly zero.
CHAIN_NNZ_DH = {bump: 56 for bump in BUMPS}
CHAIN_NNZ_DQ = {(1, 2): 200, (2, 3): 152, (3, 4): 200, (4, 5): 152}
CHAIN_NNZ_DG = {bump: 3968 for bump in BUMPS}
DENSE_RESOLVENT_NNZ = 3968
# THE INDEPENDENT FINITE-DIFFERENCE ROUTE.  D(h) = (W(h) - W(0))/h at two exact
# rational steps; R = 2 D(h/2) - D(h) is the exact first linear elimination.
FD_STEP = sp.Rational(1, 100)
FD_RICHARDSON_BOUND = sp.Rational(1, 10000)
FD_OPERATOR_SCALE = sp.Rational(1, 4)
FD_ENTRYWISE_MONOTONE = True
# AND AT THE CUTOFF PAIRS THE FINITE-DIFFERENCE ROUTE IS EXACT, not merely
# convergent: (W(delta) - W(0))/delta EQUALS dW entrywise at both amplitudes.
FD_EXACT_AT_CUTOFF_RESIDUAL = 0

# --- D: THE TEN RATIONALS ---------------------------------------------------
HEAVY_FACTOR = (22569375, -233631106, 22569375)
LIGHT_FACTOR = (39529825, -109432706, 39529825)
BOUNDARY_FACTOR = (43033320714375, -445467467014578, 48554286398375)
# charpoly(W) at the baseline, as (factor, multiplicity) -- Block 191's landed
# table at the two response cores, reproduced here as this block's control.
BASELINE_SPECTRUM = {
    1: ((HEAVY_FACTOR, 1), (BOUNDARY_FACTOR, 1), (LIGHT_FACTOR, 2)),
    3: ((HEAVY_FACTOR, 2), (LIGHT_FACTOR, 2)),
}
RESPONSES = {
    ((3, 4), 1): {
        "heavy": sp.Rational(840153195543, 196300900625),
        "boundary": sp.Rational(59790687128721117, 13862573301236875),
        "light": sp.Rational(21615004253318, 12284407006475)},
    ((2, 3), 1): {
        "heavy": sp.Rational(-421462341183472199, 177215545561734375),
        "boundary": sp.Rational(-29381217534120895221181,
                                12514784612024119828125),
        "light": sp.Rational(22866757183474123654, 19424018367789224675)},
    ((3, 4), 3): {
        "heavy": sp.Rational(-152770523741944777898, 10738971376744546875),
        "light": sp.Rational(-6227354334614993838, 3884803673557844935)},
    ((2, 3), 3): {
        "heavy": sp.Rational(-1495288291042, 1427461510575),
        "light": sp.Rational(-2705696606558, 2456881401295)},
}
TRACE_TOTALS = {
    ((3, 4), 1): sp.Rational(2702603990428664601847792,
                             261056210615088396173125),
    ((2, 3), 1): sp.Rational(-1322424657623802056150231913430788608,
                             372647692749599431888443061718296875),
    ((3, 4), 3): sp.Rational(-83526662690302770407422046496832,
                             5276875808912607540299962640625),
    ((2, 3), 3): sp.Rational(-953207325986164736, 443602221410818725),
}
RESPONSE_COUNT = 10
PROJECTOR_PARTITION_RESIDUAL = 0
SQUAREFREE_ANNIHILATOR_RESIDUAL = 0
# THE CHECK'S P1, AND IT IS STRONGER THAN TRACE AGREEMENT: the projector built
# from the FULL multiplicities and the one built from the SQUAREFREE total are
# the SAME MATRIX, entry for entry.
SQUAREFREE_PROJECTOR_RESIDUAL = 0

# --- E: THE RESPONSE TABLE --------------------------------------------------
# THE EXACT heavy - boundary DIFFERENCES at t0 = 1, over the SAME denominator.
RESPONSE_DIFFERENCES = {
    (3, 4): sp.Rational(61132656, 1842661567),
    (2, 3): sp.Rational(56249856, 1842661567),
}
SHARED_DIFFERENCE_DENOMINATOR = 1842661567
DIFFERENCES_NONZERO = True
JOINT_SIGN_FLIP = True
LIGHT_SIGN_STABLE = True
# THE EXACT t0 = 3 RATIOS tr(P_heavy dW) / tr(P_light dW), with exact rational
# brackets so that "heavy-dominated" and "scale-balanced" are inequalities.
ONSITE_RATIO = sp.Rational(37533905844768035289054578457791,
                           4229425500383349914656444790625)
DISTANCE_ONE_RATIO = sp.Rational(232340137594542523, 244263525398539845)
ONSITE_BRACKET = (sp.Integer(8), sp.Integer(9))
DISTANCE_ONE_BRACKET = (sp.Rational(9, 10), sp.Integer(1))
# THE SIX ENUMERATED RELATIVE READINGS, as integers over 10^10, one per
# normalization per position.  THEY REPLACE THE SOLVE'S DROPPED QUANTIFIER AND
# ARE READINGS OF THE EXACT DIFFERENCES ABOVE, WHICH ARE PRIMARY.
DECIMAL_SCALE = 10 ** 10
DECIMAL_PRECISION = 40
RELATIVE_READINGS = {
    ((3, 4), "heavy"): 77516025,
    ((3, 4), "boundary"): 76919774,
    ((3, 4), "symmetric"): 77216748,
    ((2, 3), "heavy"): 128356799,
    ((2, 3), "boundary"): 130025768,
    ((2, 3), "symmetric"): 129185893,
}
# THE SOLVE'S THRESHOLD, KEPT AS A LITERAL SO THE CORRECTION IS A GATE AND NOT
# A SENTENCE.  It holds at {3,4} under all three normalizations and FAILS at
# {2,3} under all three, so it is FALSE as a statement about both positions.
SOLVE_RELATIVE_THRESHOLD = sp.Rational(1, 100)
THRESHOLD_BY_POSITION = {(3, 4): True, (2, 3): False}
THRESHOLD_HOLDS_AT_BOTH_POSITIONS = False
# THE TEN DECIMALS of the responses themselves, this block's ONE numeric layer.
RESPONSE_DECIMALS = {
    ((3, 4), 1, "heavy"): 42799253232,
    ((3, 4), 1, "boundary"): 43131016031,
    ((3, 4), 1, "light"): 17595480386,
    ((2, 3), 1, "heavy"): -23782470090,
    ((2, 3), 1, "boundary"): -23477205917,
    ((2, 3), 1, "light"): 11772413283,
    ((3, 4), 3, "heavy"): -142258060276,
    ((3, 4), 3, "light"): -16030036156,
    ((2, 3), 3, "heavy"): -10475156633,
    ((2, 3), 3, "light"): -11012727782,
}

# --- F: THE SUPPORT-CUTOFF LAW ----------------------------------------------
# nnz(dW) OVER ALL TWELVE VALID (bump, core) PAIRS.  THE THREE ZEROS ARE THE
# WHOLE OF THE LAW, AND THE PATTERN IS DIRECTIONAL AND NOT RADIAL.
CUTOFF_TABLE = {
    ((1, 2), 1): 64, ((1, 2), 3): 64, ((1, 2), 5): 0,
    ((2, 3), 1): 64, ((2, 3), 3): 64, ((2, 3), 5): 0,
    ((3, 4), 1): 64, ((3, 4), 3): 64, ((3, 4), 5): 64,
    ((4, 5), 1): 0, ((4, 5), 3): 64, ((4, 5), 5): 64,
}
CUTOFF_PAIRS = (((1, 2), 5), ((2, 3), 5), ((4, 5), 1))
CUTOFF_COUNT = 3
# AND THE SAME TABLE AT A FINITE AMPLITUDE: nnz(W(delta) - W(0)) at
# delta = 1/5.  IT IS THE SAME TABLE, WHICH IS WHY THE CUTOFF IS NOT A
# LINEARIZATION ARTEFACT.
FINITE_AMPLITUDE = sp.Rational(1, 5)
SECOND_AMPLITUDE = sp.Rational(1, 7)
FINITE_CUTOFF_TABLE = dict(CUTOFF_TABLE)
ORDERS_AGREE = True
# THE EXACT (0, 0, 0) TRIPLE at the extra position, and it is a SUPPORT CUTOFF
# and NOT a persistence of the nonzero response.
EXTRA_BUMP_TRIPLE = {"heavy": sp.Integer(0), "boundary": sp.Integer(0),
                     "light": sp.Integer(0)}
EXTRA_BUMP_TRACE = sp.Integer(0)
# THE PAIRING GAUGE, WHICH IS THE MEASURED MECHANISM.  At every cutoff pair the
# first-order pairing derivative satisfies dL_2 = dK_c W exactly, and at finite
# delta the two pairings are carried by a COMMON LEFT FACTOR that is NOT the
# identity in any entry-count sense.
PAIRING_GAUGE_RESIDUAL = 0
FINITE_PAIRING_GAUGE_RESIDUAL = 0
LEFT_FACTOR_NONTRIVIAL_ENTRIES = 64
CUTOFF_PAIRING_MOTION = {((1, 2), 5): (64, 60), ((2, 3), 5): (64, 60),
                         ((4, 5), 1): (64, 64)}
# THE REFUTED READINGS, KEPT AS LITERALS SO THAT EACH CORRECTION IS A GATE.
# 'Empty-cross routing' would require dG to vanish where W does not move; dG is
# DENSE at every cutoff pair, so support routing is NOT the mechanism.
SUPPORT_ROUTING_IS_THE_MECHANISM = False
# And the overlap signature is SUFFICIENT but NOT NECESSARY: emptiness forces
# the zero in both cases where it holds, and there is EXACTLY ONE counterexample
# to the converse among the ten overlapping pairs.
OVERLAP_EMPTY_IMPLIES_ZERO = True
OVERLAP_EMPTY_PAIRS = (((1, 2), 5), ((2, 3), 5))
OVERLAP_IS_A_CUTOFF_SIGNATURE = False
OVERLAP_COUNTEREXAMPLES = (((4, 5), 1),)
OVERLAP_COUNTEREXAMPLE_INTERSECTION = {((4, 5), 1): (4,)}

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO, so a residual, a difference or a trace passed through it can
# silently lose its sign -- and this block is a block about EXACT ZEROS, exact
# signs and exact rational differences.  Every mass, shear, volume and step here
# is ALREADY an exact sympy Rational.  Gate G counts the occurrences in this
# file's own source and requires ZERO.
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
    fallback purely because that is slow at dimension 64, and it changes NO
    value."""
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


def primitive_coefficients(expression: object, variable: sp.Symbol) -> tuple:
    """THE PRIMITIVE INTEGER COEFFICIENT VECTOR of a rational polynomial, high
    degree first, normalized to a POSITIVE leading coefficient and to content 1."""
    polynomial = sp.Poly(sp.expand(expression), variable)
    coefficients = [sp.Rational(c) for c in polynomial.all_coeffs()]
    multiplier = 1
    for value in coefficients:
        multiplier = sp.ilcm(multiplier, value.q)
    integers = [sp.Integer(value * multiplier) for value in coefficients]
    content = 0
    for value in integers:
        content = sp.igcd(content, int(value))
    integers = [value / content for value in integers]
    if integers[0] < 0:
        integers = [-value for value in integers]
    return tuple(int(value) for value in integers)


VARIABLE = sp.Symbol("z")
DELTA = sp.Symbol("delta")


def char_factors(matrix: sp.Matrix) -> tuple:
    """THE EXACT RATIONAL FACTORIZATION of the characteristic polynomial, as
    (primitive coefficient vector, multiplicity) pairs sorted by degree then
    lexicographically.  sympy's factor_list over Q is exact."""
    expression = matrix.charpoly(VARIABLE).as_expr()
    factors = []
    for factor, multiplicity in sp.factor_list(expression)[1]:
        if factor.has(VARIABLE):
            factors.append(
                (primitive_coefficients(factor, VARIABLE), multiplicity))
    return tuple(sorted(factors, key=lambda item: (len(item[0]), item[0])))


def monic_poly(coefficients: tuple) -> sp.Poly:
    return sp.Poly(list(coefficients), VARIABLE, domain=QQ).monic()


def poly_of_matrix(polynomial: sp.Poly, matrix: sp.Matrix) -> sp.Matrix:
    """p(M) by Horner over QQ -- exact, and no eigenvector is ever formed."""
    result = sp.zeros(matrix.rows, matrix.rows)
    identity = sp.eye(matrix.rows)
    for coefficient in polynomial.all_coeffs():
        result = sp.expand(result * matrix + coefficient * identity)
    return result


def decimal10(value: object) -> int:
    """THE BLOCK'S ONE NUMERIC LAYER, AND IT IS A ROUNDING OF AN EXACT OBJECT.
    Returns round(value * 10^10) as an integer, evaluated at 40 digits.  The
    argument is always an exact rational; nothing numeric is ever fed back into
    a construction."""
    scaled = sp.N(value * DECIMAL_SCALE, DECIMAL_PRECISION)
    return int(sp.floor(scaled + sp.Rational(1, 2)))


# ---------------------------------------------------------------------------
# THE WIDTH FAMILY AT A VOLUME PROFILE.  Everything except the shear block is
# rebuilt here; the shear block is the ONE imported object.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def site_index(time: int, space: int) -> int:
    return (time % WIDTH) * SPACE_EXTENT + space % SPACE_EXTENT


def site_theta(time: int) -> int:
    """theta_s(t) = -t, fixing the slices {0, 8}."""
    return (-time) % WIDTH


def anchor_theta(time: int) -> int:
    """thA_s(t) = -1-t: the ANCHOR reflection that carries a NON-UNIFORM volume
    profile across the seam."""
    return (-1 - time) % WIDTH


def staggered_kernel() -> sp.Matrix:
    kernel = sp.zeros(SITE_COUNT, SITE_COUNT)
    for time in range(WIDTH):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if time == WIDTH - 1 else 1
            here = site_index(time, space)
            ahead = site_index(time + 1, space)
            kernel[here, ahead] += sp.Rational(temporal_sign, 2)
            kernel[ahead, here] -= sp.Rational(temporal_sign, 2)
            spatial_sign = (-1) ** time
            right = site_index(time, space + 1)
            kernel[here, right] += sp.Rational(spatial_sign, 2)
            kernel[right, here] -= sp.Rational(spatial_sign, 2)
    return kernel


def grade_projector(grade: int) -> sp.Matrix:
    return sp.diag(*[1 if (time % 2 + space % 2) == grade else 0
                     for time in range(WIDTH) for space in range(SPACE_EXTENT)])


def raising_part(kernel: sp.Matrix) -> sp.Matrix:
    p0, p1, p2 = (grade_projector(g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation() -> sp.Matrix:
    matrix = sp.zeros(SITE_COUNT, SITE_COUNT)
    for time in range(WIDTH):
        for space in range(SPACE_EXTENT):
            matrix[site_index(site_theta(time), space),
                   site_index(time, space)] = 1
    return matrix


def site_restricted_raising(raising: sp.Matrix) -> sp.Matrix:
    half = WIDTH // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(SITE_COUNT, SITE_COUNT)
    for row in range(SITE_COUNT):
        for column in range(SITE_COUNT):
            if raising[row, column] == 0:
                continue
            row_time, column_time = row // SPACE_EXTENT, column // SPACE_EXTENT
            if row_time not in closed or column_time not in closed:
                continue
            if row_time == column_time and row_time in fixed:
                continue
            matrix[row, column] = raising[row, column]
    return matrix


def cell_embedding(time: int, space: int) -> sp.Matrix:
    matrix = sp.zeros(SITE_COUNT, 4)
    for column, (delta_t, delta_x) in enumerate(
            ((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[site_index(time + delta_t, space + delta_x), column] = 1
    return matrix


def imported_shear_block(volume: object) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT, read AT A SYMBOLIC VOLUME: the LANDED Block 105
    shear Hodge diag(v, v g(c)^-1, 1/v).  NO nsimplify: the shear is already a
    sympy Rational and the volume is a Rational or a Symbol."""
    return sp.Matrix(b128.block105.shear_hodge(FIXTURE_SHEAR, volume))


def cell_sum(blocks: dict) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule.
    Only the times present in `blocks` contribute, which is exactly why the
    DERIVATIVE of H is the same cell sum over the BUMPED times alone."""
    result = sp.zeros(SITE_COUNT, SITE_COUNT)
    for time, block in blocks.items():
        for space in range(SPACE_EXTENT):
            embedding = cell_embedding(time, space)
            result += embedding * block * embedding.T / 4
    return sp.expand(result)


def image_times(anchors: tuple) -> tuple:
    """The image anchors whose thA_s(t) = -1-t partner is bumped."""
    return tuple(time for time in range(WIDTH // 2, WIDTH)
                 if anchor_theta(time) in anchors)


def site_hodge_profile(profile: dict) -> sp.Matrix:
    half = WIDTH // 2
    blocks = {}
    for time in range(WIDTH):
        if time < half:
            blocks[time] = imported_shear_block(profile[time])
        else:
            block = imported_shear_block(profile[anchor_theta(time)])
            blocks[time] = sp.expand(
                OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    return cell_sum(blocks)


def bump_profile(anchors: tuple, delta: object) -> dict:
    return {time: (UNIT_VOLUME - delta if time in anchors else UNIT_VOLUME)
            for time in range(WIDTH // 2)}


def completion(hodge: sp.Matrix, glue: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    return sp.expand(FIXTURE_MASS * hodge + hodge * glue - glue.T * hodge)


def core_cells(core: int) -> tuple:
    return tuple((time, space) for time in (core, core + 1)
                 for space in range(SPACE_EXTENT))


def shifted_pairing(inverse: sp.Matrix, core: int, step: int) -> sp.Matrix:
    """L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]; k = 0 is K_c."""
    cells = core_cells(core)
    matrix = sp.zeros(len(cells), len(cells))
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(site_theta(row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(column_time + step, column_space), partner]
    return matrix


def monodromy(inverse: sp.Matrix, core: int) -> tuple:
    gram = shifted_pairing(inverse, core, 0)
    second = shifted_pairing(inverse, core, 2)
    return gram, second, sp.expand(exact_inverse(gram) * second)


def support_times(matrix: sp.Matrix) -> tuple:
    """THE MEASURED SITE-TIME SUPPORT of a matrix -- the times carrying any
    nonzero row or column.  It is read off the matrix and never asserted."""
    times = set()
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if matrix[row, column] != 0:
                times.add(row // SPACE_EXTENT)
                times.add(column // SPACE_EXTENT)
    return tuple(sorted(times))


def core_window_times(core: int) -> tuple:
    """THE TIMES THE PAIRING READS: the column times {t0, t0+1, t0+2, t0+3} that
    K_c and L_2 sample, together with the theta_s row times."""
    columns = {core, core + 1, core + 2, core + 3}
    rows = {site_theta(core), site_theta(core + 1)}
    return tuple(sorted(columns | rows))


# ---------------------------------------------------------------------------
# THE CRT SPECTRAL PROJECTORS, congruence-gated
# ---------------------------------------------------------------------------
def crt_projectors(factors: dict, matrix: sp.Matrix, squarefree: bool) -> tuple:
    """P_f = q_f(W) with q_f = M_f (M_f^-1 mod f^k) mod chi, M_f = chi / f^k.
    Every congruence q_f = 1 mod f^k and q_f = 0 mod g^l is CHECKED as a zero
    POLYNOMIAL residual, so the projector property is certified and not assumed."""
    powers = {name: (factor if squarefree else factor ** multiplicity)
              for name, (factor, multiplicity) in factors.items()}
    total = sp.Poly(1, VARIABLE, domain=QQ)
    for modulus in powers.values():
        total *= modulus
    projectors, congruences = {}, {}
    for name, modulus in powers.items():
        complement = total.exquo(modulus)
        q = (complement * sp.invert(complement, modulus)).rem(total)
        projectors[name] = poly_of_matrix(q, matrix)
        for other, other_modulus in powers.items():
            target = sp.Poly(1 if name == other else 0, VARIABLE, domain=QQ)
            congruences[f"{name}:{other}"] = q.rem(other_modulus) == target
    return projectors, congruences, total


def factor_set(core: int) -> dict:
    heavy, light = monic_poly(HEAVY_FACTOR), monic_poly(LIGHT_FACTOR)
    if core == 1:
        return {"heavy": (heavy, 1), "boundary": (monic_poly(BOUNDARY_FACTOR), 1),
                "light": (light, 2)}
    return {"heavy": (heavy, 2), "light": (light, 2)}


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
    covariance: tuple
    baseline_spectrum: dict
    chain_nnz: dict
    symbolic_residual: dict
    resolvent_residual: dict
    core_equation_residual: dict
    fd_monotone: dict
    fd_errors: dict
    fd_operator_scale: dict
    fd_exact_residual: dict
    responses: dict
    trace_totals: dict
    sum_rules: dict
    crt_congruences: dict
    projector_partition: dict
    squarefree_annihilator: dict
    squarefree_projector: dict
    squarefree_traces_equal: dict
    response_decimals: dict
    differences: dict
    difference_denominators: dict
    joint_sign_flip: bool
    light_sign_stable: bool
    onsite_ratio: object
    distance_one_ratio: object
    relative_readings: dict
    threshold_by_position: dict
    cutoff_table: dict
    finite_cutoff_table: dict
    second_amplitude_table: dict
    extra_triple: dict
    extra_trace: object
    pairing_gauge: dict
    finite_pairing_gauge: dict
    left_factor_entries: dict
    cutoff_pairing_motion: dict
    dense_resolvent: dict
    overlap_empty_pairs: tuple
    overlap_counterexamples: tuple
    overlap_intersections: dict
    nsimplify_calls: int


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    authority = authority_certificate(main_head)
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""

    # ---- the construction, and the ONE baseline inverse -------------------
    reflection = reflection_permutation()
    restricted = site_restricted_raising(raising_part(staggered_kernel()))
    glue = sp.expand(restricted - reflection * restricted * reflection)
    baseline_profile = bump_profile((), sp.Integer(0))
    hodge = site_hodge_profile(baseline_profile)
    action = completion(hodge, glue)
    resolvent = exact_inverse(action)
    covariance = (residual_count(reflection * hodge * reflection - hodge),
                  residual_count(reflection * action * reflection - action.T))

    grams, seconds, monodromies, gram_inverses = {}, {}, {}, {}
    for core in CORES:
        gram, second, wmatrix = monodromy(resolvent, core)
        grams[core], seconds[core], monodromies[core] = gram, second, wmatrix
        gram_inverses[core] = exact_inverse(gram)
    baseline_spectrum = {core: char_factors(monodromies[core])
                         for core in RESPONSE_CORES}

    # ---- C: the displayed volume derivative, against the IMPORT -----------
    symbolic_block = imported_shear_block(UNIT_VOLUME - DELTA)
    imported_derivative = symbolic_block.applyfunc(
        lambda value: sp.diff(value, DELTA).subs(DELTA, 0))
    volume_derivative_residual = residual_count(
        imported_derivative - DISPLAYED_VOLUME_DERIVATIVE)
    displayed_law_residual = (
        residual_count(imported_shear_block(UNIT_VOLUME) - DISPLAYED_HODGE_UNIT)
        + residual_count(imported_shear_block(BUMP_VOLUME) - DISPLAYED_HODGE_BUMP))

    # ---- C: the chain, ONCE PER BUMP (dQ and dG do not see the core) ------
    image_block = sp.expand(OFFSET_PERMUTATION * DISPLAYED_VOLUME_DERIVATIVE
                            * OFFSET_PERMUTATION.T)
    chain_nnz, symbolic_residual, resolvent_residual = {}, {}, {}
    derivatives, dense_resolvent, bump_support = {}, {}, {}
    for bump in BUMPS:
        blocks = {time: DISPLAYED_VOLUME_DERIVATIVE for time in bump}
        blocks.update({time: image_block for time in image_times(bump)})
        dhodge = cell_sum(blocks)
        daction = sp.expand(FIXTURE_MASS * dhodge + dhodge * glue
                            - glue.T * dhodge)
        dresolvent = sp.expand(-resolvent * daction * resolvent)
        derivatives[bump] = (dhodge, daction, dresolvent)
        chain_nnz[bump] = (nonzero_entries(dhodge), nonzero_entries(daction),
                           nonzero_entries(dresolvent))
        dense_resolvent[bump] = nonzero_entries(dresolvent)
        bump_support[bump] = support_times(dhodge)

        # the SYMBOLIC route: differentiate the displayed profile entrywise
        # BEFORE any inverse is formed, and compare to the cell-sum route.
        symbolic_hodge = site_hodge_profile(bump_profile(bump, DELTA))
        symbolic_daction = completion(symbolic_hodge, glue).applyfunc(
            lambda value: sp.diff(value, DELTA).subs(DELTA, 0))
        symbolic_dhodge = symbolic_hodge.applyfunc(
            lambda value: sp.diff(value, DELTA).subs(DELTA, 0))
        symbolic_residual[bump] = (
            residual_count(symbolic_dhodge - dhodge),
            residual_count(symbolic_daction - daction))
        resolvent_residual[bump] = (
            residual_count(action * dresolvent + daction * resolvent),
            residual_count(dresolvent * action + resolvent * daction))

    # ---- C/F: the core restriction, over ALL TWELVE PAIRS -----------------
    dmonodromy, core_equation_residual, pairing_gauge = {}, {}, {}
    cutoff_table, dpairings = {}, {}
    for bump in BUMPS:
        _dh, _dq, dresolvent = derivatives[bump]
        for core in CORES:
            dgram = shifted_pairing(dresolvent, core, 0)
            dsecond = shifted_pairing(dresolvent, core, 2)
            dw = sp.expand(gram_inverses[core]
                           * (dsecond - dgram * monodromies[core]))
            dmonodromy[(bump, core)] = dw
            dpairings[(bump, core)] = (dgram, dsecond)
            core_equation_residual[(bump, core)] = residual_count(
                dgram * monodromies[core] + grams[core] * dw - dsecond)
            cutoff_table[(bump, core)] = nonzero_entries(dw)
            pairing_gauge[(bump, core)] = residual_count(
                dsecond - dgram * monodromies[core])

    # ---- F: the SAME table at two finite amplitudes -----------------------
    finite_cutoff_table, second_amplitude_table = {}, {}
    finite_pairing_gauge, left_factor_entries = {}, {}
    cutoff_pairing_motion, fd_exact_residual = {}, {}
    for bump in BUMPS:
        for amplitude, table in ((FINITE_AMPLITUDE, finite_cutoff_table),
                                 (SECOND_AMPLITUDE, second_amplitude_table)):
            if amplitude == SECOND_AMPLITUDE and not any(
                    pair[0] == bump for pair in CUTOFF_PAIRS):
                continue
            moved = exact_inverse(
                completion(site_hodge_profile(bump_profile(bump, amplitude)),
                           glue))
            for core in CORES:
                gram, second, wmatrix = monodromy(moved, core)
                difference = sp.expand(wmatrix - monodromies[core])
                table[(bump, core)] = nonzero_entries(difference)
                if (bump, core) in CUTOFF_PAIRS:
                    left = sp.expand(gram * gram_inverses[core])
                    finite_pairing_gauge[(bump, core, amplitude)] = (
                        residual_count(second - left * seconds[core]))
                    left_factor_entries[(bump, core, amplitude)] = (
                        nonzero_entries(sp.expand(left - sp.eye(8))))
                    cutoff_pairing_motion[(bump, core, amplitude)] = (
                        nonzero_entries(sp.expand(gram - grams[core])),
                        nonzero_entries(sp.expand(second - seconds[core])))
                    fd_exact_residual[(bump, core, amplitude)] = residual_count(
                        (difference / amplitude) - dmonodromy[(bump, core)])

    # ---- C: the INDEPENDENT finite-difference route -----------------------
    fd_monotone, fd_errors, fd_operator_scale = {}, {}, {}
    for bump in RESPONSE_BUMPS:
        steps = {}
        for step in (FD_STEP, FD_STEP / 2):
            moved = exact_inverse(
                completion(site_hodge_profile(bump_profile(bump, step)), glue))
            steps[step] = {core: monodromy(moved, core)[2] for core in CORES}
        for core in RESPONSE_CORES:
            coarse = sp.expand((steps[FD_STEP][core] - monodromies[core])
                               / FD_STEP)
            fine = sp.expand((steps[FD_STEP / 2][core] - monodromies[core])
                             / (FD_STEP / 2))
            richardson = sp.expand(2 * fine - coarse)
            exact = dmonodromy[(bump, core)]
            errors = [(abs(richardson[i] - exact[i]), abs(fine[i] - exact[i]),
                       abs(coarse[i] - exact[i]))
                      for i in range(exact.rows * exact.cols)]
            fd_monotone[(bump, core)] = all(a <= b <= c for a, b, c in errors)
            fd_errors[(bump, core)] = (max(a for a, _b, _c in errors),
                                       max(b for _a, b, _c in errors),
                                       max(c for _a, _b, c in errors))
            fd_operator_scale[(bump, core)] = max(
                abs(value) for value in exact)

    # ---- D: the CRT projectors and the ten rationals ----------------------
    projectors, squarefree_projectors = {}, {}
    crt_congruences, projector_partition = {}, {}
    squarefree_annihilator, squarefree_projector = {}, {}
    for core in RESPONSE_CORES:
        factors = factor_set(core)
        full, full_congruences, _total = crt_projectors(
            factors, monodromies[core], squarefree=False)
        sf, sf_congruences, sf_total = crt_projectors(
            factors, monodromies[core], squarefree=True)
        projectors[core], squarefree_projectors[core] = full, sf
        crt_congruences[core] = (all(full_congruences.values()),
                                 all(sf_congruences.values()))
        projector_partition[core] = (
            residual_count(sum(full.values(), sp.zeros(8, 8)) - sp.eye(8)),
            residual_count(sum(sf.values(), sp.zeros(8, 8)) - sp.eye(8)))
        squarefree_annihilator[core] = residual_count(
            poly_of_matrix(sf_total, monodromies[core]))
        squarefree_projector[core] = max(
            residual_count(full[name] - sf[name]) for name in factors)

    responses, trace_totals, sum_rules = {}, {}, {}
    squarefree_traces_equal, response_decimals = {}, {}
    for bump in RESPONSE_BUMPS:
        for core in RESPONSE_CORES:
            dw = dmonodromy[(bump, core)]
            values = {name: sp.trace(sp.expand(projector * dw))
                      for name, projector in projectors[core].items()}
            squarefree_values = {
                name: sp.trace(sp.expand(projector * dw))
                for name, projector in squarefree_projectors[core].items()}
            responses[(bump, core)] = values
            trace_totals[(bump, core)] = sp.trace(dw)
            sum_rules[(bump, core)] = (
                sum(values.values(), sp.Integer(0)) == sp.trace(dw))
            squarefree_traces_equal[(bump, core)] = values == squarefree_values
            for name, value in values.items():
                response_decimals[(bump, core, name)] = decimal10(value)

    # ---- E: the differences, the signs and the ratios ---------------------
    differences, difference_denominators = {}, {}
    relative_readings, threshold_by_position = {}, {}
    for bump in RESPONSE_BUMPS:
        values = responses[(bump, 1)]
        heavy, boundary = values["heavy"], values["boundary"]
        difference = sp.Abs(heavy - boundary)
        differences[bump] = difference
        difference_denominators[bump] = int(sp.Rational(difference).q)
        ratios = {"heavy": difference / sp.Abs(heavy),
                  "boundary": difference / sp.Abs(boundary),
                  "symmetric": 2 * difference / (sp.Abs(heavy)
                                                 + sp.Abs(boundary))}
        for name, ratio in ratios.items():
            relative_readings[(bump, name)] = decimal10(ratio)
        threshold_by_position[bump] = all(
            ratio < SOLVE_RELATIVE_THRESHOLD for ratio in ratios.values())
    joint_sign_flip = bool(
        responses[((3, 4), 1)]["heavy"] > 0 > responses[((2, 3), 1)]["heavy"]
        and responses[((3, 4), 1)]["boundary"] > 0
        > responses[((2, 3), 1)]["boundary"])
    light_sign_stable = bool(responses[((3, 4), 1)]["light"] > 0
                             and responses[((2, 3), 1)]["light"] > 0)
    onsite_ratio = (responses[((3, 4), 3)]["heavy"]
                    / responses[((3, 4), 3)]["light"])
    distance_one_ratio = (responses[((2, 3), 3)]["heavy"]
                          / responses[((2, 3), 3)]["light"])

    # ---- F: the extra position, and the overlap signature -----------------
    extra_dw = dmonodromy[(EXTRA_BUMP, EXTRA_CORE)]
    extra_triple = {name: sp.trace(sp.expand(projector * extra_dw))
                    for name, projector in projectors[EXTRA_CORE].items()}
    overlap_empty, overlap_counterexamples, overlap_intersections = [], [], {}
    for bump in BUMPS:
        for core in CORES:
            shared = tuple(sorted(set(bump_support[bump])
                                  & set(core_window_times(core))))
            if not shared:
                overlap_empty.append((bump, core))
            elif cutoff_table[(bump, core)] == 0:
                overlap_counterexamples.append((bump, core))
                overlap_intersections[(bump, core)] = shared

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
        covariance=covariance,
        baseline_spectrum=baseline_spectrum,
        chain_nnz=chain_nnz,
        symbolic_residual=symbolic_residual,
        resolvent_residual=resolvent_residual,
        core_equation_residual=core_equation_residual,
        fd_monotone=fd_monotone,
        fd_errors=fd_errors,
        fd_operator_scale=fd_operator_scale,
        fd_exact_residual=fd_exact_residual,
        responses=responses,
        trace_totals=trace_totals,
        sum_rules=sum_rules,
        crt_congruences=crt_congruences,
        projector_partition=projector_partition,
        squarefree_annihilator=squarefree_annihilator,
        squarefree_projector=squarefree_projector,
        squarefree_traces_equal=squarefree_traces_equal,
        response_decimals=response_decimals,
        differences=differences,
        difference_denominators=difference_denominators,
        joint_sign_flip=joint_sign_flip,
        light_sign_stable=light_sign_stable,
        onsite_ratio=onsite_ratio,
        distance_one_ratio=distance_one_ratio,
        relative_readings=relative_readings,
        threshold_by_position=threshold_by_position,
        cutoff_table=cutoff_table,
        finite_cutoff_table=finite_cutoff_table,
        second_amplitude_table=second_amplitude_table,
        extra_triple=extra_triple,
        extra_trace=sp.trace(extra_dw),
        pairing_gauge=pairing_gauge,
        finite_pairing_gauge=finite_pairing_gauge,
        left_factor_entries=left_factor_entries,
        cutoff_pairing_motion=cutoff_pairing_motion,
        dense_resolvent=dense_resolvent,
        overlap_empty_pairs=tuple(overlap_empty),
        overlap_counterexamples=tuple(overlap_counterexamples),
        overlap_intersections=overlap_intersections,
        nsimplify_calls=nsimplify_occurrences())


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE PERTURBATION LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 (the staggered Dirac-Kahler carrier on Z_16 x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, 8}, the raising set A_s in the CLOSED half {0..8} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13)), BLOCK 191's VOLUME PROFILE (a map v from the positive anchors {0..7} to the positive rationals, placed as B(c, v(t)) for t < 8 and as the P_4 image of the block of its thA_s(t) = -1-t partner for t >= 8, assembled by the quarter-weighted four-corner cell average), THE ONE-PARAMETER BUMP FAMILY v = 1 - delta -- THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT -- THE FOUR BUMP POSITIONS {1,2}, {2,3}, {3,4}, {4,5} AND THE THREE VALID CORES t0 = 1, 3, 5, THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE THREE LABELLED FACTORS heavy, light and boundary WITH THEIR CRT PROJECTORS, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module AT A SYMBOLIC VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED AND NO PHYSICAL PERTURBATION IS PERFORMED: delta is a dial on an IMPOSED Hodge-volume parameter, 'response' names d/d(delta) of a rational matrix entry at delta = 0, and this block supplies NO lapse variable in an ADM phase space, NO Hamiltonian constraint, NO gauge orbit, NO quotient, NO Dirac observable and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, THE FIRST-ORDER RESPONSE OF THE EXACT MONODROMY TO A ONE-SLICE VOLUME BUMP IS COMPUTED IN CLOSED FORM WITHOUT INVERTING A SYMBOLIC MATRIX, AND IT VANISHES EXACTLY AT THREE OF TWELVE (bump, core) PAIRS. 'HYBRIDIZATION', 'LOCKING' AND 'SUPPORT CUTOFF' NAME PROPERTIES OF EXACT RATIONAL MATRICES: 'hybridization' NAMES the joint sign behaviour of two CRT trace components, 'locking' NAMES that joint sign behaviour AND NOT ANY MAGNITUDE AGREEMENT, and 'support cutoff' NAMES entrywise equality of two exact 8 x 8 matrices. THE SOLVE'S RELATIVE-AGREEMENT QUANTIFIER IS DROPPED, NOT SOFTENED: the adversarial check measured the {2,3} heavy/boundary relative difference ABOVE the quoted rational threshold 1/100 under the reference-relative and symmetric normalizations, so THIS BLOCK CLAIMS THE SIGN STRUCTURE ONLY and records six exact relative readings in its place. THE SUPPORT CUTOFF IS NOT A LIGHT CONE: it is a statement about which exact matrices are equal, and NO propagation speed, NO causal structure and NO continuum limit is supplied or implied. THE MECHANISM OF THE CUTOFF IS NOT DERIVED: 'empty-cross routing' is a READING and a NAMED OPEN LEG, and the naive support-overlap account is REFUTED HERE BY MEASUREMENT -- dG is DENSE at 3968 of 4096 entries at every cutoff pair, dK_c is FULL, and the pair ({4,5}, t0 = 1) overlaps the read window at t = 4 and still gives 0_8. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NO GENERALITY IS CLAIMED: ONE fixture, ONE width, FOUR bump positions, THREE cores, THREE amplitudes, and NOTHING about the infinite-width or continuum limit. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE METHOD THEOREM IS A CHAIN OF FOUR DISPLAYED IDENTITIES AND NO SYMBOLIC MATRIX IS EVER INVERTED. With v = 1 - delta on the bumped positive anchors: dB = d/d(delta) shear_hodge(c, 1-delta) at delta = 0 = -E00 - (169/144)(E11+E22) + (65/144)(E12+E21) + E33 -- GATED entrywise at ZERO against the SYMBOLIC derivative of the IMPORTED shear_hodge, and the underlying law gated at BOTH probed volumes, thirty-two numbers; dH = the SAME quarter-weighted cell sum over the bumped anchors AND their thA_s image partners, with P_4 dB P_4^T on the images; dQ = m dH + dH D_s - D_s^T dH, exact because D_s does not depend on delta; dG = -G dQ G with the KNOWN v = 1 inverse; and dW = K_c^-1 (dL_2 - dK_c W). EVERY LINK IS GATED AT EXACTLY ZERO: nnz(dH_symbolic - dH_cellsum) = 0 and nnz(dQ_symbolic - dQ_law) = 0 by entrywise symbolic differentiation of the displayed profile BEFORE any inverse is formed, nnz(Q dG + dQ G) = 0 and nnz(dG Q + G dQ) = 0 on BOTH the left and right resolvent equations, and nnz(dK_c W + K_c dW - dL_2) = 0 at all twelve pairs. THE FINGERPRINTS ARE MEASURED: nnz(dH) = 56 at every bump, nnz(dQ) = 200 for the odd-anchor bumps {1,2} and {3,4} and 152 for the even-anchor bumps {2,3} and {4,5}, and nnz(dG) = 3968 at every bump. AND THE CHAIN IS GATED AGAINST AN INDEPENDENT ROUTE: exact-rational forward differences of W at delta = 1/100 and 1/200 with the exact first linear elimination 2 D(h/2) - D(h) converge to the propagated dW ENTRYWISE MONOTONICALLY in all sixty-four entries and to within 1/10000 of it while the operator's own scale exceeds 1/4 -- and at the three cutoff pairs the finite-difference route is EXACT, equal to dW entrywise at BOTH delta = 1/5 and delta = 1/7. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's zeros, signs, differences or traces could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate G.\\nper_mode: THE TEN RATIONALS AND THE FOUR SUM RULES ARE EXACT AND THE PROJECTORS ARE CONGRUENCE-GATED. At t0 = 1 the baseline spectrum is heavy*light^2*boundary and at t0 = 3 it is heavy^2*light^2, so the two bumps give TEN per-factor first-order trace responses tr(P_f dW), ALL NONZERO: bump{3,4} at t0=1 gives heavy 840153195543/196300900625, boundary 59790687128721117/13862573301236875 and light 21615004253318/12284407006475; bump{2,3} at t0=1 gives heavy -421462341183472199/177215545561734375, boundary -29381217534120895221181/12514784612024119828125 and light 22866757183474123654/19424018367789224675; bump{3,4} at t0=3 gives heavy -152770523741944777898/10738971376744546875 and light -6227354334614993838/3884803673557844935; bump{2,3} at t0=3 gives heavy -1495288291042/1427461510575 and light -2705696606558/2456881401295. EACH PROJECTOR IS P_f = q_f(W) with q_f = M_f (M_f^-1 mod f^k) mod chi and M_f = chi/f^k, and EVERY congruence q_f = 1 mod f^k, q_f = 0 mod g^l is a ZERO POLYNOMIAL RESIDUAL over QQ; the projectors SUM TO I_8 at zero residual and the squarefree total ANNIHILATES W at zero residual. ALL FOUR SUM RULES tr(dW) = sum_f tr(P_f dW) hold at EXACT EQUALITY. AND THE CHECK'S P1 IS FOLDED AS CONTENT AND STRENGTHENED: the projectors built from the FULL multiplicities and from the SQUAREFREE total are THE SAME MATRIX ENTRY FOR ENTRY, which is strictly stronger than the trace agreement the solve needed.\\nper_block: THE RESPONSE TABLE CLAIMS THE SIGN STRUCTURE AND THE EXACT DIFFERENCES, AND THE SOLVE'S QUANTIFIER IS DROPPED AS CONTENT. At t0 = 1 the heavy and boundary responses share a sign at each position and FLIP TOGETHER between them -- both positive at {3,4}, both negative at {2,3} -- while the light response is POSITIVE at both, so the light factor is sign-stable where the other two are not. Their exact differences are |heavy - boundary| = 61132656/1842661567 at {3,4} and 56249856/1842661567 at {2,3}: BOTH NONZERO, so the two factors do NOT respond identically, and BOTH OVER THE SAME DENOMINATOR 1842661567. THE ADVERSARIAL CHECK REFUTED THE SOLVE'S RELATIVE-AGREEMENT QUANTIFIER AT ONE OF ITS TWO REQUIRED POSITIONS AND THE QUANTIFIER IS THEREFORE DROPPED AND NOT RENORMALIZED: the six exact relative readings, as integers over 10^10, are 0.0077516025, 0.0076919774 and 0.0077216748 at {3,4} against the heavy reference, the boundary reference and the symmetric normalization, and 0.0128356799, 0.0130025768 and 0.0129185893 at {2,3} -- so the quoted rational threshold 1/100 holds at {3,4} under all three normalizations and FAILS at {2,3} under all three, and THRESHOLD_HOLDS_AT_BOTH_POSITIONS = False is a declared constant with a gate and a mutation. AT t0 = 3 THE POSITION DEPENDENCE IS A RATIO AND NOT AN ADJECTIVE: the ON-SITE bump {3,4} is heavy-dominated at the exact ratio 37533905844768035289054578457791/4229425500383349914656444790625, strictly between 8 and 9, and the DISTANCE-ONE bump {2,3} is scale-balanced at 232340137594542523/244263525398539845, strictly between 9/10 and 1.\\nlattice_wide: THE SUPPORT-CUTOFF LAW, AND IT IS THE CHECK'S DISCOVERY CARRIED AS THIS BLOCK'S CENTRE. Over the TWELVE valid (bump, core) pairs -- bumps {1,2}, {2,3}, {3,4}, {4,5} against cores t0 = 1, 3, 5 -- nnz(dW) is 64 at NINE pairs and EXACTLY ZERO at THREE: ({1,2}, t0=5), ({2,3}, t0=5) and ({4,5}, t0=1). THE SAME THREE ZEROS APPEAR AT FINITE AMPLITUDE: nnz(W(delta) - W(0)) is the SAME TWELVE-ENTRY TABLE at delta = 1/5, and the three zeros are reproduced at delta = 1/7, so the WHOLE 8 x 8 monodromy is unchanged ENTRYWISE and the cutoff is NOT a linearization artefact. THE CUTOFF IS DIRECTIONAL AND NOT RADIAL: bump {3,4} REACHES t0 = 5 while bump {2,3} does NOT, and bump {4,5} MISSES t0 = 1 while bump {3,4} reaches it, so 'the response decays with distance' is FALSE as a description of this table. THE EXTRA POSITION IS A CUTOFF AND NOT A PERSISTENCE: bump {4,5} at t0 = 1 is a VALID probe -- {4,5} lies in the positive-anchor domain {0..7} and t0+3 = 4 < 8 is interior -- and its exact first-order triple is (0, 0, 0) with tr(dW) = 0, which is a TRIVIAL equality and NOT the survival of a nonzero response. B191's {2,3} EXACT ZERO IS HEREBY IDENTIFIED: it is not a root shift or a resultant but WHOLE-OPERATOR INVARIANCE at t0 = 5.\\nper_scope: THE MECHANISM IS MEASURED AS A PAIRING GAUGE AND THE ROUTING READING IS REFUTED BY MEASUREMENT. The underlying pairings are NOT individually fixed at any cutoff pair: at delta = 1/5, nnz(K_c(delta) - K_c) = 64 at all three and nnz(L_2(delta) - L_2) is 60, 60 and 64, so BOTH pairings move in almost every entry. What is exact is that they move TOGETHER: dL_2 = dK_c W at ZERO residual at first order, and at finite delta the common left factor M = K_c(delta) K_c^-1 satisfies L_2(delta) = M L_2 at ZERO residual with M - I nonzero in all 64 entries. W = K_c^-1 L_2 is invariant under exactly that motion, and THAT is the whole of the cancellation. THE EMPTY-CROSS ROUTING ACCOUNT IS A READING AND A NAMED OPEN LEG, AND ITS NAIVE FORM IS REFUTED HERE: dG is DENSE at 3968 of 4096 entries at every cutoff pair, so nothing is routed away in the support sense; and the support-overlap signature is SUFFICIENT BUT NOT NECESSARY -- emptiness of the overlap between the bump's measured site-time support and the core's read window forces the zero in BOTH cases where it holds, but ({4,5}, t0 = 1) OVERLAPS that window at t = 4 and still gives 0_8, the ONE counterexample among the ten overlapping pairs. NO SUPPORT SIGNATURE DEFINES THE CUTOFF, AND THE DERIVATION OF ITS MECHANISM IS OPEN.\\nRESULT: THE FIRST-ORDER RESPONSE OF THE UNIT-CELL MONODROMY TO A ONE-SLICE HODGE-VOLUME BUMP IS OBTAINED IN CLOSED FORM BY A FOUR-STEP DERIVATIVE CHAIN THAT NEVER INVERTS A SYMBOLIC MATRIX, TEN EXACT PER-FACTOR RATIONALS AND FOUR SUM RULES ARE COMPUTED AND CONGRUENCE-GATED, AND AN EXACT DIRECTIONAL SUPPORT CUTOFF IS ESTABLISHED AT THREE OF TWELVE (bump, core) PAIRS AT FIRST ORDER AND AT TWO FINITE AMPLITUDES -- AND NOT ONE LINE OF IT IS A LAPSE, A CONSTRAINT, A LIGHT CONE, A PROPAGATION SPEED OR A CONTINUUM LIMIT. The displayed dB is gated against the symbolic derivative of the import; every link of the chain closes at exactly zero on both resolvent equations; an independent exact-rational finite-difference route converges entrywise and is EXACT at the cutoff pairs; the ten rationals are all nonzero and the full and squarefree projectors agree entrywise; the solve's relative-agreement quantifier is DROPPED and replaced by six exact readings and the sign structure; and the naive support-routing account of the cutoff is REFUTED by a dense dG and by one measured counterexample. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-191 STAND EXACTLY AS LANDED. BLOCK 191 IS NOT CORRECTED: its t0 = 1 and t0 = 3 baseline factorizations are reproduced here digit-for-digit as this block's control, and its {2,3} exact zero at t0 = 5 is reproduced and then EXPLAINED as whole-operator invariance rather than revised. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE fixture, ONE width, FOUR bump positions, THREE cores and THREE amplitudes -- four positions are not a scan; the cutoff's MECHANISM IS NOT DERIVED and is a named open leg; and the block's own solve language is corrected in two places rather than papered over. FOUR ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C3 REFUTATION, that the relative-agreement quantifier fails at {2,3} under all three standard normalizations and is therefore DROPPED with only the sign structure claimed; the C4 IDENTIFICATION, that B191's {2,3} zero is whole-operator invariance at t0 = 5 and not a root shift; the P2 RECLASSIFICATION, that bump {4,5} at t0 = 1 is an exact SUPPORT CUTOFF with triple (0,0,0) and NOT a persistence of nonzero locking; and the P1 STRENGTHENING, that the full-multiplicity and squarefree CRT projectors agree ENTRY FOR ENTRY and not merely in trace. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE HYBRIDIZATION MECHANISM SOLVE (block 192 candidate), HYB PHASE 1 MEASURED, HYB PHASE 2 and B192 CHECK VERDICT anchors.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
        "hybridization_physical": HYBRIDIZATION_PHYSICAL_CLAIMED,
        "locking_threshold": LOCKING_THRESHOLD_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "transfer_operator": TRANSFER_OPERATOR_CLAIMED,
        "mechanism_derived": MECHANISM_DERIVED_CLAIMED,
        "generality": GENERALITY_CLAIMED,
        # C -- the method theorem.
        "volume_derivative": DISPLAYED_VOLUME_DERIVATIVE,
        "volume_derivative_residual": ZERO_RESIDUAL,
        "displayed_law_residual": ZERO_RESIDUAL,
        "covariance": (ZERO_RESIDUAL, ZERO_RESIDUAL),
        "action_derivative_residual": ZERO_RESIDUAL,
        "resolvent_residual": ZERO_RESIDUAL,
        "core_equation_residual": ZERO_RESIDUAL,
        "symbolic_residual": ZERO_RESIDUAL,
        "chain_nnz_dh": dict(CHAIN_NNZ_DH),
        "chain_nnz_dq": dict(CHAIN_NNZ_DQ),
        "chain_nnz_dg": dict(CHAIN_NNZ_DG),
        "fd_monotone": FD_ENTRYWISE_MONOTONE,
        "fd_bound": FD_RICHARDSON_BOUND,
        "fd_scale": FD_OPERATOR_SCALE,
        "fd_exact_residual": FD_EXACT_AT_CUTOFF_RESIDUAL,
        # D -- the ten rationals.
        "baseline_spectrum": {core: BASELINE_SPECTRUM[core]
                              for core in RESPONSE_CORES},
        "responses": {key: dict(value) for key, value in RESPONSES.items()},
        "responses_nonzero": True,
        "response_count": RESPONSE_COUNT,
        "trace_totals": dict(TRACE_TOTALS),
        "sum_rules": True,
        "crt_congruences": (True, True),
        "projector_partition": (PROJECTOR_PARTITION_RESIDUAL,
                                PROJECTOR_PARTITION_RESIDUAL),
        "squarefree_annihilator": SQUAREFREE_ANNIHILATOR_RESIDUAL,
        "squarefree_projector": SQUAREFREE_PROJECTOR_RESIDUAL,
        "squarefree_traces_equal": True,
        # E -- the response table.
        "differences": dict(RESPONSE_DIFFERENCES),
        "differences_nonzero": DIFFERENCES_NONZERO,
        "shared_denominator": SHARED_DIFFERENCE_DENOMINATOR,
        "joint_sign_flip": JOINT_SIGN_FLIP,
        "light_sign_stable": LIGHT_SIGN_STABLE,
        "onsite_ratio": ONSITE_RATIO,
        "onsite_bracket": ONSITE_BRACKET,
        "distance_one_ratio": DISTANCE_ONE_RATIO,
        "distance_one_bracket": DISTANCE_ONE_BRACKET,
        "relative_readings": dict(RELATIVE_READINGS),
        "threshold_by_position": dict(THRESHOLD_BY_POSITION),
        "threshold_at_both": THRESHOLD_HOLDS_AT_BOTH_POSITIONS,
        "response_decimals": dict(RESPONSE_DECIMALS),
        # F -- the support-cutoff law.
        "cutoff_table": dict(CUTOFF_TABLE),
        "cutoff_pairs": CUTOFF_PAIRS,
        "cutoff_count": CUTOFF_COUNT,
        "finite_cutoff_table": dict(FINITE_CUTOFF_TABLE),
        "orders_agree": ORDERS_AGREE,
        "second_amplitude_zero": 0,
        "operator_zero": 0,
        "extra_triple": dict(EXTRA_BUMP_TRIPLE),
        "extra_trace": EXTRA_BUMP_TRACE,
        "pairing_gauge": PAIRING_GAUGE_RESIDUAL,
        "finite_pairing_gauge": FINITE_PAIRING_GAUGE_RESIDUAL,
        "left_factor_entries": LEFT_FACTOR_NONTRIVIAL_ENTRIES,
        "cutoff_pairing_motion": dict(CUTOFF_PAIRING_MOTION),
        "dense_resolvent": DENSE_RESOLVENT_NNZ,
        "support_routing": SUPPORT_ROUTING_IS_THE_MECHANISM,
        "overlap_empty_pairs": OVERLAP_EMPTY_PAIRS,
        "overlap_empty_implies_zero": OVERLAP_EMPTY_IMPLIES_ZERO,
        "overlap_signature": OVERLAP_IS_A_CUTOFF_SIGNATURE,
        "overlap_counterexamples": OVERLAP_COUNTEREXAMPLES,
        "overlap_intersections": dict(OVERLAP_COUNTEREXAMPLE_INTERSECTION),
        # G -- the note, the fence and the nsimplify absence.
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
    elif mutation == "claim_hybridization_physical":
        claims["hybridization_physical"] = True
    elif mutation == "claim_locking_threshold":
        # THE DROPPED QUANTIFIER REASSERTED, AND THIS IS THE MUTATION THAT
        # GUARDS THE CHECK'S C3 REFUTATION: the solve's relative-agreement
        # threshold is asserted to hold at BOTH bump positions.  It does not.
        claims["locking_threshold"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
    elif mutation == "claim_transfer_operator":
        claims["transfer_operator"] = True
    elif mutation == "claim_mechanism_derived":
        # THE OPEN LEG DENIED: the cutoff's mechanism is asserted as derived.
        claims["mechanism_derived"] = True
    elif mutation == "claim_generality":
        claims["generality"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_volume_derivative_block":
        broken = sp.Matrix(DISPLAYED_VOLUME_DERIVATIVE)
        broken[1, 2] = sp.Rational(-65, 144)
        claims["volume_derivative"] = broken
    elif mutation == "break_displayed_shear_law":
        claims["displayed_law_residual"] = 1
    elif mutation == "break_action_derivative_law":
        claims["action_derivative_residual"] = 1
        claims["covariance"] = (1, 1)
    elif mutation == "break_resolvent_law":
        claims["resolvent_residual"] = 1
    elif mutation == "break_monodromy_derivative_law":
        claims["core_equation_residual"] = 1
    elif mutation == "break_symbolic_agreement":
        claims["symbolic_residual"] = 1
    elif mutation == "break_chain_fingerprints":
        claims["chain_nnz_dq"] = {bump: 200 for bump in BUMPS}
    elif mutation == "break_finite_difference_route":
        claims["fd_monotone"] = False
    # --- D ----------------------------------------------------------------
    elif mutation == "break_ten_rationals":
        broken = {key: dict(value) for key, value in RESPONSES.items()}
        broken[((2, 3), 3)]["heavy"] = sp.Rational(-1495288291042, 1427461510576)
        claims["responses"] = broken
    elif mutation == "break_responses_nonzero":
        claims["responses_nonzero"] = False
    elif mutation == "break_trace_totals":
        broken = dict(TRACE_TOTALS)
        broken[((2, 3), 3)] = sp.Rational(-953207325986164736, 443602221410818726)
        claims["trace_totals"] = broken
    elif mutation == "break_sum_rules":
        claims["sum_rules"] = False
    elif mutation == "break_crt_congruences":
        claims["crt_congruences"] = (False, False)
    elif mutation == "break_projector_partition":
        claims["projector_partition"] = (1, 1)
    elif mutation == "break_squarefree_projectors":
        # THE CHECK'S P1 DENIED: the full and squarefree projectors are asserted
        # to differ as matrices while still agreeing in trace.
        claims["squarefree_projector"] = 1
    # --- E ----------------------------------------------------------------
    elif mutation == "break_response_differences":
        broken = dict(RESPONSE_DIFFERENCES)
        broken[(2, 3)] = sp.Rational(61132656, 1842661567)
        claims["differences"] = broken
    elif mutation == "break_shared_denominator":
        claims["shared_denominator"] = 1842661568
    elif mutation == "break_joint_sign_flip":
        claims["joint_sign_flip"] = False
    elif mutation == "break_light_sign_stability":
        claims["light_sign_stable"] = False
    elif mutation == "break_onsite_ratio":
        claims["onsite_bracket"] = (sp.Integer(9), sp.Integer(10))
    elif mutation == "break_distance_one_ratio":
        claims["distance_one_bracket"] = (sp.Integer(1), sp.Rational(11, 10))
    elif mutation == "break_relative_readings":
        # THE EXACT READINGS THAT REPLACED THE DROPPED QUANTIFIER, REWRITTEN.
        broken = dict(RELATIVE_READINGS)
        broken[((2, 3), "symmetric")] = 77216748
        claims["relative_readings"] = broken
    # --- F ----------------------------------------------------------------
    elif mutation == "break_cutoff_table":
        broken = dict(CUTOFF_TABLE)
        broken[((3, 4), 5)] = 0
        claims["cutoff_table"] = broken
    elif mutation == "break_finite_cutoff_table":
        broken = dict(FINITE_CUTOFF_TABLE)
        broken[((4, 5), 1)] = 64
        claims["finite_cutoff_table"] = broken
    elif mutation == "break_order_agreement":
        claims["orders_agree"] = False
    elif mutation == "break_second_amplitude":
        claims["second_amplitude_zero"] = 64
    elif mutation == "break_operator_zeros":
        claims["operator_zero"] = 1
    elif mutation == "break_extra_bump_triple":
        # THE CHECK'S P2 DENIED: the extra position is asserted to persist with
        # a nonzero heavy response rather than to cut off exactly.
        broken = dict(EXTRA_BUMP_TRIPLE)
        broken["heavy"] = sp.Rational(1, 1000)
        claims["extra_triple"] = broken
    elif mutation == "break_pairing_gauge":
        claims["pairing_gauge"] = 1
    elif mutation == "break_dense_resolvent":
        # THE REFUTED ROUTING ACCOUNT ASSERTED: dG is claimed to vanish where
        # the response cuts off, which is what 'routed away' would require.
        claims["dense_resolvent"] = 0
        claims["support_routing"] = True
    elif mutation == "break_overlap_rule":
        # THE REFUTED SIGNATURE ASSERTED: support overlap is claimed to decide
        # the cutoff, i.e. no counterexample exists.
        claims["overlap_signature"] = True
        claims["overlap_counterexamples"] = ()
    # --- G ----------------------------------------------------------------
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
        f"ancestor of HEAD resolving PARENT_REF, both Block 191 artifacts are "
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
        "B-3", "PHYSICAL HYBRIDIZATION IS A READING: 'hybridization' names the "
        "joint sign behaviour of two CRT trace components and nothing physical",
        claims["hybridization_physical"] is False)
    checks.check(
        "B-4", f"THE RELATIVE-AGREEMENT QUANTIFIER IS NOT CLAIMED: the solve's "
        f"threshold {SOLVE_RELATIVE_THRESHOLD} is recorded as holding at "
        f"{sum(claims['threshold_by_position'].values())} of "
        f"{len(RESPONSE_BUMPS)} positions and the block claims the SIGN "
        f"structure only",
        claims["locking_threshold"] is False)
    checks.check(
        "B-5", "NO CONTINUUM AND NO LIMIT: one width, one fixture, four bump "
        "positions, three cores, three amplitudes",
        claims["continuum_limit"] is False)
    checks.check(
        "B-6", "W IS NOT A TRANSFER OPERATOR: Block 190 refuted the naive OS "
        "transfer pairing on this class and nothing here repairs it",
        claims["transfer_operator"] is False)
    checks.check(
        "B-7", "THE CUTOFF'S MECHANISM IS NOT DERIVED: empty-cross routing is a "
        "READING and a named open leg",
        claims["mechanism_derived"] is False)
    checks.check(
        "B-8", "NO GENERALITY IS CLAIMED: no bracket, no ray, no edge, no "
        "interior, and nothing about the infinite-width limit",
        claims["generality"] is False)

    # --- C: THE METHOD THEOREM ---------------------------------------------
    checks.check(
        "C-1", f"dB = d/d(delta) shear_hodge(c, 1-delta) at delta = 0 equals "
        f"-E00 - (169/144)(E11+E22) + (65/144)(E12+E21) + E33 entrywise "
        f"against the SYMBOLIC derivative of the import, residual "
        f"{facts.volume_derivative_residual}",
        facts.volume_derivative == claims["volume_derivative"]
        and facts.volume_derivative_residual
        == claims["volume_derivative_residual"])
    checks.check(
        "C-2", f"the displayed shear law agrees with the import at BOTH probed "
        f"volumes, residual {facts.displayed_law_residual} over thirty-two "
        f"numbers",
        facts.displayed_law_residual == claims["displayed_law_residual"])
    checks.check(
        "C-3", f"the baseline is Ps-covariant: (nnz(Ps H Ps - H), "
        f"nnz(Ps Q Ps - Q^T)) = {facts.covariance}, and dQ = m dH + dH D_s - "
        f"D_s^T dH is exact because D_s does not depend on delta",
        facts.covariance == claims["covariance"]
        and claims["action_derivative_residual"] == ZERO_RESIDUAL)
    checks.check(
        "C-4", "the SYMBOLIC route agrees with the cell-sum route entrywise "
        "BEFORE any inverse is formed: nnz(dH_sym - dH) = nnz(dQ_sym - dQ) = 0 "
        "at every bump",
        all(residual == (claims["symbolic_residual"],
                         claims["symbolic_residual"])
            for residual in facts.symbolic_residual.values()))
    checks.check(
        "C-5", "dG = -G dQ G closes on BOTH resolvent equations: "
        "nnz(Q dG + dQ G) = nnz(dG Q + G dQ) = 0 at every bump",
        all(residual == (claims["resolvent_residual"],
                         claims["resolvent_residual"])
            for residual in facts.resolvent_residual.values()))
    checks.check(
        "C-6", f"dW = K_c^-1 (dL_2 - dK_c W) closes at all "
        f"{len(facts.core_equation_residual)} (bump, core) pairs: "
        f"nnz(dK_c W + K_c dW - dL_2) = 0",
        all(residual == claims["core_equation_residual"]
            for residual in facts.core_equation_residual.values()))
    checks.check(
        "C-7", f"the chain fingerprints are nnz(dH) = 56 at every bump, "
        f"nnz(dQ) = {claims['chain_nnz_dq']} by leading-anchor parity, and "
        f"nnz(dG) = {DENSE_RESOLVENT_NNZ} at every bump",
        all(facts.chain_nnz[bump][0] == claims["chain_nnz_dh"][bump]
            and facts.chain_nnz[bump][1] == claims["chain_nnz_dq"][bump]
            and facts.chain_nnz[bump][2] == claims["chain_nnz_dg"][bump]
            for bump in BUMPS))
    checks.check(
        "C-8", f"the INDEPENDENT finite-difference route at delta = {FD_STEP} "
        f"and its halving converges to the propagated dW entrywise "
        f"monotonically in all sixty-four entries, with the exact first linear "
        f"elimination within {claims['fd_bound']} while the operator scale "
        f"exceeds {claims['fd_scale']}, and is EXACT at the three cutoff pairs",
        all(value == claims["fd_monotone"]
            for value in facts.fd_monotone.values())
        and all(errors[0] < claims["fd_bound"] < errors[1] <= errors[2]
                for errors in facts.fd_errors.values())
        and all(scale > claims["fd_scale"]
                for scale in facts.fd_operator_scale.values())
        and all(residual == claims["fd_exact_residual"]
                for residual in facts.fd_exact_residual.values()))

    # --- D: THE TEN RATIONALS AND THE SUM RULES ----------------------------
    checks.check(
        "D-1", f"the baseline spectrum is heavy*light^2*boundary at t0 = 1 and "
        f"heavy^2*light^2 at t0 = 3, coefficient for coefficient",
        all(facts.baseline_spectrum[core]
            == tuple(sorted(claims["baseline_spectrum"][core],
                            key=lambda item: (len(item[0]), item[0])))
            for core in RESPONSE_CORES))
    checks.check(
        "D-2", f"all {claims['response_count']} per-factor first-order trace "
        f"responses tr(P_f dW) equal their declared exact rationals",
        sum(len(value) for value in facts.responses.values())
        == claims["response_count"]
        and all(facts.responses[key] == claims["responses"][key]
                for key in claims["responses"]))
    checks.check(
        "D-3", f"all {claims['response_count']} responses are NONZERO",
        all(bool(value != 0) == claims["responses_nonzero"]
            for values in facts.responses.values()
            for value in values.values()))
    checks.check(
        "D-4", "the four exact trace totals tr(dW) equal their declared values",
        facts.trace_totals == claims["trace_totals"])
    checks.check(
        "D-5", "all four sum rules tr(dW) = sum_f tr(P_f dW) hold at exact "
        "equality",
        all(value == claims["sum_rules"] for value in facts.sum_rules.values()))
    checks.check(
        "D-6", "every CRT congruence q_f = 1 mod f^k and q_f = 0 mod g^l is a "
        "ZERO polynomial residual, for the full and the squarefree systems, "
        "and both projector families sum to I_8 at zero residual with the "
        "squarefree total annihilating W",
        all(value == claims["crt_congruences"]
            for value in facts.crt_congruences.values())
        and all(value == claims["projector_partition"]
                for value in facts.projector_partition.values())
        and all(value == claims["squarefree_annihilator"]
                for value in facts.squarefree_annihilator.values()))
    checks.check(
        "D-7", "the full-multiplicity and squarefree projectors are the SAME "
        "MATRIX entry for entry, which is strictly stronger than the trace "
        "agreement the solve needed",
        all(value == claims["squarefree_projector"]
            for value in facts.squarefree_projector.values())
        and all(value == claims["squarefree_traces_equal"]
                for value in facts.squarefree_traces_equal.values()))

    # --- E: THE RESPONSE TABLE ---------------------------------------------
    checks.check(
        "E-1", f"the exact heavy/boundary differences are "
        f"{claims['differences'][(3, 4)]} at bump {{3,4}} and "
        f"{claims['differences'][(2, 3)]} at bump {{2,3}}, and BOTH ARE NONZERO",
        facts.differences == claims["differences"]
        and all(bool(value != 0) == claims["differences_nonzero"]
                for value in facts.differences.values()))
    checks.check(
        "E-2", f"both differences carry the SAME denominator "
        f"{claims['shared_denominator']}",
        all(value == claims["shared_denominator"]
            for value in facts.difference_denominators.values()))
    checks.check(
        "E-3", "the heavy and boundary responses FLIP SIGN TOGETHER between "
        "the two bump positions, positive at {3,4} and negative at {2,3}",
        facts.joint_sign_flip == claims["joint_sign_flip"])
    checks.check(
        "E-4", "the light response is POSITIVE at BOTH bump positions, so it "
        "is sign-stable where the other two are not",
        facts.light_sign_stable == claims["light_sign_stable"])
    checks.check(
        "E-5", f"the ON-SITE ratio tr(P_heavy dW)/tr(P_light dW) at t0 = 3 is "
        f"{claims['onsite_ratio']}, strictly between "
        f"{claims['onsite_bracket'][0]} and {claims['onsite_bracket'][1]}",
        facts.onsite_ratio == claims["onsite_ratio"]
        and claims["onsite_bracket"][0] < facts.onsite_ratio
        < claims["onsite_bracket"][1])
    checks.check(
        "E-6", f"the DISTANCE-ONE ratio at t0 = 3 is "
        f"{claims['distance_one_ratio']}, strictly between "
        f"{claims['distance_one_bracket'][0]} and "
        f"{claims['distance_one_bracket'][1]}",
        facts.distance_one_ratio == claims["distance_one_ratio"]
        and claims["distance_one_bracket"][0] < facts.distance_one_ratio
        < claims["distance_one_bracket"][1])
    checks.check(
        "E-7", f"the six exact relative readings (x 10^10) are "
        f"{claims['relative_readings']}, the solve's threshold "
        f"{SOLVE_RELATIVE_THRESHOLD} holds at "
        f"{claims['threshold_by_position']} and therefore NOT at both "
        f"positions, and the ten response decimals are as declared",
        facts.relative_readings == claims["relative_readings"]
        and facts.threshold_by_position == claims["threshold_by_position"]
        and all(facts.threshold_by_position.values())
        == claims["threshold_at_both"]
        and facts.response_decimals == claims["response_decimals"])

    # --- F: THE SUPPORT-CUTOFF LAW -----------------------------------------
    checks.check(
        "F-1", f"nnz(dW) over the twelve valid (bump, core) pairs is the "
        f"declared table, with EXACTLY {claims['cutoff_count']} exact zeros at "
        f"{claims['cutoff_pairs']}",
        facts.cutoff_table == claims["cutoff_table"]
        and tuple(sorted(key for key, value in facts.cutoff_table.items()
                         if value == 0)) == tuple(sorted(claims["cutoff_pairs"]))
        and sum(1 for value in facts.cutoff_table.values() if value == 0)
        == claims["cutoff_count"])
    checks.check(
        "F-2", f"nnz(W(delta) - W(0)) at delta = {FINITE_AMPLITUDE} over the "
        f"same twelve pairs is the declared finite table",
        facts.finite_cutoff_table == claims["finite_cutoff_table"])
    checks.check(
        "F-3", "the first-order table and the finite table are IDENTICAL, so "
        "the cutoff is NOT a linearization artefact",
        (facts.cutoff_table == facts.finite_cutoff_table)
        == claims["orders_agree"])
    checks.check(
        "F-4", f"the three zeros are reproduced at the second amplitude "
        f"delta = {SECOND_AMPLITUDE}",
        all(facts.second_amplitude_table[pair]
            == claims["second_amplitude_zero"] for pair in CUTOFF_PAIRS))
    checks.check(
        "F-5", f"at each cutoff pair the WHOLE 8 x 8 operator is unchanged "
        f"entrywise at both finite amplitudes and its derivative vanishes "
        f"entrywise",
        all(facts.cutoff_table[pair] == claims["operator_zero"]
            and facts.finite_cutoff_table[pair] == claims["operator_zero"]
            for pair in CUTOFF_PAIRS))
    checks.check(
        "F-6", f"the extra position bump {EXTRA_BUMP} at t0 = {EXTRA_CORE} is "
        f"VALID and its exact first-order triple is (0, 0, 0) with tr(dW) = 0 "
        f"-- a SUPPORT CUTOFF and NOT a persistence of nonzero locking",
        facts.extra_triple == claims["extra_triple"]
        and facts.extra_trace == claims["extra_trace"])
    checks.check(
        "F-7", f"the MECHANISM is a PAIRING GAUGE: dL_2 = dK_c W at zero "
        f"residual at every cutoff pair, and at finite delta the common left "
        f"factor M = K_c(delta) K_c^-1 satisfies L_2(delta) = M L_2 at zero "
        f"residual with M - I nonzero in all "
        f"{claims['left_factor_entries']} entries",
        all(facts.pairing_gauge[pair] == claims["pairing_gauge"]
            for pair in CUTOFF_PAIRS)
        and all(value == claims["finite_pairing_gauge"]
                for value in facts.finite_pairing_gauge.values())
        and all(value == claims["left_factor_entries"]
                for value in facts.left_factor_entries.values()))
    checks.check(
        "F-8", f"SUPPORT ROUTING IS NOT THE MECHANISM: dG is DENSE at "
        f"{claims['dense_resolvent']} of {SITE_COUNT ** 2} entries at every "
        f"bump and both pairings move -- (nnz(dK_c(delta) - K_c), "
        f"nnz(L_2(delta) - L_2)) is {claims['cutoff_pairing_motion']} at the "
        f"cutoff pairs -- so support_routing = {claims['support_routing']}",
        all(value == claims["dense_resolvent"]
            for value in facts.dense_resolvent.values())
        and claims["support_routing"] is False
        and all(facts.cutoff_pairing_motion[(pair[0], pair[1],
                                             FINITE_AMPLITUDE)]
                == claims["cutoff_pairing_motion"][pair]
                for pair in CUTOFF_PAIRS))
    checks.check(
        "F-9", f"the support-overlap signature is SUFFICIENT but NOT NECESSARY: "
        f"emptiness forces the zero at {claims['overlap_empty_pairs']}, both of "
        f"them, but {claims['overlap_counterexamples']} overlaps the read "
        f"window at {claims['overlap_intersections']} and still gives 0_8, so "
        f"overlap_signature = {claims['overlap_signature']}",
        facts.overlap_empty_pairs == claims["overlap_empty_pairs"]
        and all(facts.cutoff_table[pair] == 0
                for pair in facts.overlap_empty_pairs)
        == claims["overlap_empty_implies_zero"]
        and facts.overlap_counterexamples == claims["overlap_counterexamples"]
        and facts.overlap_intersections == claims["overlap_intersections"]
        and (not facts.overlap_counterexamples) == claims["overlap_signature"])

    # --- G: THE NOTE, THE FENCE AND THE nsimplify ABSENCE -------------------
    checks.check(
        "G-1", f"the note is landed at docs/{FINAL_NOTE_NAME}",
        NOTE_PATH.is_file() == claims["note_present"])
    checks.check(
        "G-2", "the N5 fence appears in the note byte-identically to this "
        "runner's single-line constant",
        facts.scope == claims["scope"])
    checks.check(
        "G-3", f"sp.nsimplify occurs {facts.nsimplify_calls} times in this "
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
    print(f"  THE METHOD THEOREM: dB = {facts.volume_derivative.tolist()}")
    print(f"    dB vs the IMPORT's symbolic derivative: residual "
          f"{facts.volume_derivative_residual}; displayed law residual "
          f"{facts.displayed_law_residual}; Ps-covariance {facts.covariance}")
    print(f"    symbolic residuals (dH, dQ) {facts.symbolic_residual}")
    print(f"    resolvent residuals (left, right) {facts.resolvent_residual}")
    print(f"    core-equation residuals {facts.core_equation_residual}")
    print(f"    chain nnz (dH, dQ, dG) {facts.chain_nnz}")
    print(f"    finite differences: monotone {facts.fd_monotone}")
    for key in sorted(facts.fd_errors, key=str):
        richardson, fine, coarse = facts.fd_errors[key]
        print(f"      {key}: e_R {sp.N(richardson, 10)} < e_h/2 "
              f"{sp.N(fine, 10)} < e_h {sp.N(coarse, 10)}, operator scale "
              f"{sp.N(facts.fd_operator_scale[key], 10)}")
    print(f"      EXACT at the cutoff pairs: {facts.fd_exact_residual}")
    print(f"  THE TEN RATIONALS (baseline {facts.baseline_spectrum})")
    for key in sorted(facts.responses, key=str):
        print(f"    {key}: {facts.responses[key]}")
        print(f"      tr(dW) {facts.trace_totals[key]}  sum rule "
              f"{facts.sum_rules[key]}  squarefree traces equal "
              f"{facts.squarefree_traces_equal[key]}")
    print(f"    CRT congruences {facts.crt_congruences}; partitions "
          f"{facts.projector_partition}; squarefree annihilator "
          f"{facts.squarefree_annihilator}; full-vs-squarefree projector "
          f"residual {facts.squarefree_projector}")
    print(f"  THE RESPONSE TABLE: differences {facts.differences} over the "
          f"shared denominator {set(facts.difference_denominators.values())}")
    print(f"    joint sign flip {facts.joint_sign_flip}; light sign stable "
          f"{facts.light_sign_stable}")
    print(f"    on-site ratio {facts.onsite_ratio} = "
          f"{sp.N(facts.onsite_ratio, 20)}")
    print(f"    distance-one ratio {facts.distance_one_ratio} = "
          f"{sp.N(facts.distance_one_ratio, 20)}")
    print(f"    relative readings (x 10^10) {facts.relative_readings}")
    print(f"    the solve's threshold {SOLVE_RELATIVE_THRESHOLD} holds by "
          f"position {facts.threshold_by_position} -- DROPPED as a statement "
          f"about both positions")
    print(f"    response decimals (x 10^10) {facts.response_decimals}")
    print(f"  THE SUPPORT-CUTOFF LAW: first order {facts.cutoff_table}")
    print(f"    finite delta = {FINITE_AMPLITUDE} {facts.finite_cutoff_table}")
    print(f"    second amplitude delta = {SECOND_AMPLITUDE} "
          f"{facts.second_amplitude_table}")
    print(f"    extra triple {facts.extra_triple}, tr(dW) {facts.extra_trace}")
    print(f"    pairing gauge residuals {facts.pairing_gauge}; finite "
          f"{facts.finite_pairing_gauge}; left factor nnz(M - I) "
          f"{facts.left_factor_entries}")
    print(f"    pairing motion (nnz(K(d)-K), nnz(L2(d)-L2)) "
          f"{facts.cutoff_pairing_motion}")
    print(f"    dG density {facts.dense_resolvent} of {SITE_COUNT ** 2} -- "
          f"support routing is NOT the mechanism")
    print(f"    overlap-empty pairs {facts.overlap_empty_pairs}; "
          f"COUNTEREXAMPLES to the overlap signature "
          f"{facts.overlap_counterexamples} intersecting at "
          f"{facts.overlap_intersections}")
    print(f"  nsimplify occurrences: {facts.nsimplify_calls}")
    print("  SCOPE: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. NO GRAVITY "
          "IS SUPPLIED AND NO PHYSICAL PERTURBATION IS PERFORMED: delta is a "
          "dial on an IMPOSED Hodge-volume parameter and 'response' names "
          "d/d(delta) of a rational matrix entry. 'HYBRIDIZATION', 'LOCKING' "
          "AND 'SUPPORT CUTOFF' NAME PROPERTIES OF EXACT RATIONAL MATRICES. "
          "THE SOLVE'S RELATIVE-AGREEMENT QUANTIFIER IS DROPPED AND ONLY THE "
          "SIGN STRUCTURE IS CLAIMED. THE SUPPORT CUTOFF IS NOT A LIGHT CONE "
          "AND ITS MECHANISM IS NOT DERIVED. ONE FIXTURE, ONE WIDTH, FOUR "
          "BUMP POSITIONS, THREE CORES AND THREE AMPLITUDES IS NOT A WINDOW.")
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
