#!/usr/bin/env python3
"""BLOCK 215 -- THE COVARIANCE LOCUS OF THE FOUR DUALITY PARAMETERS.

Block 214 exhibited the plane D16 = D34 = -D25 (onsite) and the sum s = 0
(overlap) as the loci where the cone is the union of the two Hodge cones, and
recorded that no premise prefers them.  The Admissibility axiom names one
symmetry: "covariant under lattice translations and proper cubic rotations".
This runner computes EXACTLY what that symmetry does to the four parameters
of Block 211's six-face-compatible cell form, at symbolic moduli, in every
corner-sign gauge class, for EVERY conjugacy class of subgroups of the proper
cubic group O (the classes are computed from the group, not recalled):

  the corner action of O on the eight-corner cell, BUILT HERE from the 3 x 3
  signed permutations (Block 201) as the multiplicative extension through the
  lane's own wedge (the raising part D(kappa) of Block 213/214), verified as a
  representation and as an intertwiner L D(kappa) L^-1 = D(R kappa);
  the star lemma (the Hodge star derived from the lane's wedge; the plane IS
  the star line); the twisted-covariance census (E_R R) H (E_R R)^T = H over
  Block 211's 64 sign vectors, strict and twisted, with the fate of the shears
  reported first; the overlap sum; the controls (positivity, onsite parity,
  the flat cell).  The block's theorem is a CONDITIONAL: IF the cell form is
  twisted-covariant under G THEN the parameters lie on L(G).  Whether the cell
  form inherits the axiom's covariance is a reading, enumerated and not
  licensed.  Nothing is registered and nothing is adopted; no subgroup, no
  assembly, no reading and no parameter value is selected.

Gate families: A authority, B banner and fences, C construction fidelity,
D the star lemma, E the census, F the overlap sum, G the controls, H scope
fences, I note and hygiene.  Every measurement is taken once before any
mutation flag is read; exact arithmetic only -- no float, no nsimplify.
Scout-grade finite exact linear algebra on one cell form, not a spacetime and
not a dynamics.
"""
from __future__ import annotations

import argparse
import ast
import itertools
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY.
try:
    import admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05 as b214
    B214_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b214 = None
    B214_IMPORT_LANDED = False
try:
    import admissibility_dirac_kahler_covariant_rule_identification_2026_08_26 as b201
    B201_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b201 = None
    B201_IMPORT_LANDED = False
b213 = b214.b213 if b214 is not None else None
b211 = b214.b211 if b214 is not None else None
b209 = b214.b209 if b214 is not None else None
MACHINERY_IMPORT_LANDED = bool(B214_IMPORT_LANDED and B201_IMPORT_LANDED and b214 is not None
                               and b214.MACHINERY_IMPORT_LANDED and b213 is not None
                               and b211 is not None and b209 is not None)

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_"
    "NOTE_2026-09-05.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 214 is the commit this block is cut
# from AND its scientific parent; its note and runner exist at PARENT_COMMIT
# and NEITHER exists at STALE_PARENT_COMMIT, the Block 213 tip.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_"
    "THEOREM_NOTE_2026-09-05.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_"
    "2026_09_05.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "467b2c2eea9bdaca3fb8baa6855a33b8386211a3",
    "7cbd27e40d101a383cfb651fc8144bd94762023b",
)

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS (the cache parser AST-reads it).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27.py",
    "scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, re-resolved live against the REMOTE origin/main.
CURRENT_MAIN = "4407b6a0e0a38074d9b38710da6ed3a83c9e5e56"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block214-"
              "duality-parameters-principal-part-20260905")
PARENT_COMMIT = "1dc2ae2557a22ef188f344665bc00edc2593d113"
# The Block 213 tip: a real ancestor of HEAD carrying NEITHER Block 214 artifact.
STALE_PARENT_COMMIT = "851aff9b3f950e5f08b0bd0878df2e1992bbe15b"
# A real but superseded authority head, carried forward from Block 214's record.
STALE_MAIN = "e249016f759f224d9b429932cd0d1db4d452dc1a"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_covariance_inherited",
    "claim_subgroup_selected",
    "claim_assembly_decided",
    "break_representation_orders",
    "break_intertwining",
    "break_subgroup_class_count",
    "break_gauge_congruence",
    "break_star_signs",
    "break_star_line",
    "break_twisted_census",
    "break_strict_census",
    "claim_shears_killed_by_twisted_covariance",
    "break_p111_commutation",
    "break_overlap_locus",
    "claim_positivity_selects_plane",
    "claim_parity_selects_plane",
    "break_flat_cell_loci",
    "break_scout_grade_fence",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_covariance_inherited": "B", "claim_subgroup_selected": "B",
    "claim_assembly_decided": "B",
    "break_representation_orders": "C", "break_intertwining": "C",
    "break_subgroup_class_count": "C", "break_gauge_congruence": "C",
    "break_star_signs": "D", "break_star_line": "D",
    "break_twisted_census": "E", "break_strict_census": "E",
    "claim_shears_killed_by_twisted_covariance": "E",
    "break_p111_commutation": "F", "break_overlap_locus": "F",
    "claim_positivity_selects_plane": "G", "claim_parity_selects_plane": "G",
    "break_flat_cell_loci": "G",
    "break_scout_grade_fence": "H", "break_instance_scope": "H",
    "drop_n5_fence": "I", "break_float_absence": "I",
}
MUTATED_FAMILIES = "ABCDEFGHI"


class Checks:
    def __init__(self) -> None:
        self.results: list = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict = {}
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
def git_maybe(*args: str) -> str:
    result = subprocess.run(
        ("git",) + args, cwd=ROOT, text=True, capture_output=True,
        check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC).returncode == 0


def is_hash(value: str) -> bool:
    return len(value) == 40 and all(ch in "0123456789abcdef" for ch in value)


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_is_ancestor: bool
    parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    machinery_import_landed: bool
    inputs_readable: int


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and git_maybe("rev-parse", f"origin/main:{AXIOM_PATH}") == CURRENT_AXIOM_BLOB
        and git_maybe("rev-parse", f"origin/main:{REGISTRY_PATH}") == CURRENT_REGISTRY_BLOB
        and git_maybe("hash-object", AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and git_maybe("hash-object", REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB)
    worktree_blobs = tuple(git_maybe("hash-object", p) for p in PARENT_ARTIFACTS)
    committed_blobs = tuple(git_maybe("rev-parse", f"{PARENT_COMMIT}:{p}") for p in PARENT_ARTIFACTS)
    stale_blobs = tuple(git_maybe("rev-parse", f"{STALE_PARENT_COMMIT}:{p}") for p in PARENT_ARTIFACTS)
    readable = sum(1 for p in AUDIT_INPUT_PATHS if p != SELF_NOTE_INPUT and (ROOT / p).is_file())
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT),
        is_ancestor(PARENT_COMMIT, "HEAD"),
        bool(all(is_hash(v) for v in committed_blobs)
             and committed_blobs == worktree_blobs == PARENT_ARTIFACT_BLOBS),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        MACHINERY_IMPORT_LANDED,
        readable)
