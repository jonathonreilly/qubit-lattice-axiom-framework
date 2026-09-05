#!/usr/bin/env python3
"""BLOCK 219 -- THE CONE'S SHAPE IN THREE DIRECTIONS ON THE (4,4,4) BENCH AT THE COVARIANT WITNESS.

Block 218 ran Block 213's (4,4,2) bench at L+-'s covariant cell: the raising
Bloch block is i D(kappa_z) with the fine momenta entering additively, the
onsite pencil block charpoly is the charpoly of (H0^-1 M(kappa_z))^2 at every
point including the mixed point, and every nonzero eigenvalue at the three
nonzero points is a Block 216 branch constant times k^T G1 k -- the cone's
shape on the (t, x) plane, the y direction unsampled (Block 218's N6, REOPEN
item 1).  This runner computes EXACTLY, on the three-direction bench of the
same chain -- Block 213's bench_matrix at extent (4,4,4): 64 sites, Bloch
momenta (z_t, z_x, z_y) in {1, i}^3, so the zero point, three pure points,
three doubly-mixed points and the triply-mixed point (i,i,i) -- at L+-'s cell
(mask 2, the curve moduli) with the parameters at the star-line point
(0, 1/4, -1/4, 1/4), at a second line multiple (0, 1/2, -1/2, 1/2), at
D07 = 1/4 with lambda = 1/4, and at the all-plus W1 control:

  (a) the Bloch-point lemma in three directions: d_B(z) = sum_mu
      (z_mu - 1/z_mu)/2 D(e_mu) at symbolic z with z_y live, the onsite
      similarity H_B = Z^-1 H0 Z at all eight points, and the identity of the
      onsite pencil block charpoly with the charpoly of (H0^-1 M(kappa_z))^2 at
      all eight points, kappa_z in {0, e_t, e_x, e_y, e_t + e_x, e_t + e_y,
      e_x + e_y, e_t + e_x + e_y};
  (b) the shape in three directions: at each of the seven nonzero points
      every nonzero eigenvalue is a Block 216 branch constant {1, 128/99,
      16/11, 16/11} times Q(kappa_z) = kappa_z^T G1 kappa_z, the seven Q values
      computed from G1 = D1/D0 (9/8 at the pure points, 3/2 at the
      doubly-mixed points, 9/8 at the triply-mixed point);
  (c) G1 read off the bench: the six entries from the three pure and three
      doubly-mixed points, the triply-mixed point as the over-determined
      consistency check (predicted 9/8 against measured 9/8);
  (d) Block 216's two rescalings seen on the bench: at the second line
      multiple lambda = 1/2 (positivity by leading minors first) and at
      D07 = 1/4, the pure-t block multisets against the rescaled constants
      times Q;
  (e) Bloch union = direct for the 64 x 64 direct charpolys over QQ(sqrt 6)
      where they fit (the onsite pencil under one second; the onsite form and
      the overlap constructions timed and declared);
  (f) the all-plus W1 control at the triply-mixed point (the rational branch
      reads W1's quadric, the rest an irreducible cubic) and the overlap
      fold's parameter dependence at the new points (i,1,i), (1,i,i), (i,i,i)
      at symbolic face signs, moduli and parameters.

  Nothing registered or adopted; no assembly, cell, subgroup, reading or
  parameter value selected; the covariance antecedent stays a reading; 'one
  metric's cone' names Block 213's exact statement and nothing physical; no
  dispersion-law, Lorentzian, light-cone or continuum reading of the bench.

Gate families: A authority, B banner/fences, C construction fidelity, D the
bench charpolys, E the Bloch-point identities, F the shape in three
directions and G1 read off the bench, G the rescalings, the control and the
overlap fold, H scope, I note and hygiene.  Every measurement is taken once
before any mutation flag is read; exact arithmetic only -- no float, no
nsimplify.  Scout-grade finite exact linear algebra on one cell form, not a
spacetime and not a dynamics.
"""
from __future__ import annotations

import argparse
import ast
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY: Block 218 (the
# two-direction bench over the algebraic fields, its helpers) and through it
# Blocks 217, 216, 215, 214, 213, 211, 209.
try:
    import admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05 as b218
    B218_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b218 = None
    B218_IMPORT_LANDED = False
b217 = b218.b217 if b218 is not None else None
b216 = b218.b216 if b218 is not None else None
b214 = b218.b214 if b218 is not None else None
b213 = b218.b213 if b218 is not None else None
b211 = b218.b211 if b218 is not None else None
b209 = b218.b209 if b218 is not None else None
MACHINERY_IMPORT_LANDED = bool(B218_IMPORT_LANDED and b218 is not None and b218.MACHINERY_IMPORT_LANDED
                               and b217 is not None and b216 is not None and b214 is not None
                               and b213 is not None and b211 is not None and b209 is not None)
# THE STACK PARENT'S TWO ARTIFACTS.  Block 218 is the commit this block is cut
# from AND its scientific parent; its note and runner exist at PARENT_COMMIT
# and NEITHER exists at STALE_PARENT_COMMIT, the Block 217 tip.
PARENT_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
PARENT_RUNNER = "scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py"
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "75b23ae3658091f488ddb771a0111b329b92c987",
    "0216289cf16cbd2102ebb7b6d66d91781ed0f0ef",
)
FINAL_NOTE_NAME = "ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS (the cache parser AST-reads it).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27.py",
    "scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE SIX-PIN AUTHORITY BLOCK, re-resolved live against the REMOTE origin/main.
CURRENT_MAIN = "4407b6a0e0a38074d9b38710da6ed3a83c9e5e56"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = "origin/physics-loop/toe-axiom-closure-block218-two-direction-bench-covariant-witness-20260905"
PARENT_COMMIT = "39b3fd0acb53b8c3279234b04ac6a68b7a83d811"
# The Block 217 tip: a real ancestor of HEAD carrying NEITHER Block 218 artifact.
STALE_PARENT_COMMIT = "163b48814f67f22baca4fca3eabec3b458c9dd41"
# A real but superseded authority head, carried forward from Block 214's record.
STALE_MAIN = "e249016f759f224d9b429932cd0d1db4d452dc1a"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_covariance_inherited",
    "claim_assembly_decided",
    "claim_cell_selected",
    "claim_reading_selected",
    "claim_continuum_read",
    "break_bench_momenta",
    "break_witness_reproduction",
    "break_flat_control",
    "break_second_multiple_positivity",
    "break_bloch_equals_direct",
    "break_witness_multisets",
    "break_control_multisets",
    "break_raising_block_additivity",
    "break_onsite_similarity",
    "break_triply_mixed_identity",
    "break_cone_shape_visible",
    "break_g1_readoff",
    "break_triply_mixed_consistency",
    "break_line_rescaling",
    "break_d07_rescaling",
    "break_control_failure",
    "break_overlap_fold_dependence",
    "break_scout_grade_fence",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_covariance_inherited": "B", "claim_assembly_decided": "B",
    "claim_cell_selected": "B", "claim_reading_selected": "B", "claim_continuum_read": "B",
    "break_bench_momenta": "C", "break_witness_reproduction": "C", "break_flat_control": "C",
    "break_second_multiple_positivity": "C",
    "break_bloch_equals_direct": "D", "break_witness_multisets": "D", "break_control_multisets": "D",
    "break_raising_block_additivity": "E", "break_onsite_similarity": "E", "break_triply_mixed_identity": "E",
    "break_cone_shape_visible": "F", "break_g1_readoff": "F", "break_triply_mixed_consistency": "F",
    "break_line_rescaling": "G", "break_d07_rescaling": "G", "break_control_failure": "G",
    "break_overlap_fold_dependence": "G",
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
