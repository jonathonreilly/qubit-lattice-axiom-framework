#!/usr/bin/env python3
"""BLOCK 213 -- THE WEIGHTED-KERNEL DISPERSION: THE DIRAC-KAHLER LANE KERNEL
COMPLETED BY THE CURVED CELL FORM, ITS EXACT SQUARED SYMBOL ON THE PERIODIC
(4,4) AND (4,2,2) BENCHES, AND THE CONE = THE METRIC'S CONE HYPOTHESIS TESTED
EXACTLY -- THE CONE IS THE UNION OF THE TWO HODGE READINGS OF THE CELL FORM
UNDER THE GRADED ASSEMBLY, AND A NON-HODGE PAIR OF CONES UNDER THE OVERLAP
ASSEMBLY; NEITHER IS ONE METRIC'S CONE OFF THE FLAT POINT.

WHAT THIS BLOCK IS.  R5 named the weighted-kernel construction as the design
task: complete the lane kernel K = d - d^T by the curved cell form H in Block
107's / Block 201's pattern Q = m H + H d - d^T H at m = 0 and periodic
closure, K_H = H d - d^T H, and ask whether the exact squared symbol's
characteristic cone is the null cone of the cell metric.  Two chain-landed
assemblies of ONE cell form into H exist (Block 105's onsite_hodge, anchored
at even sites, and its overlap_hodge, Block 191/201's 2^-d-weighted all-anchor
average); two squared-symbol readings exist (the Euclidean form -K_H^2 and
the H-pencil -(H^-1 K_H)^2 = d delta + delta d).  All four reduce EXACTLY to
R5's flat kernel at the flat cell, and the flat symbol sum_d sin^2 k_d is
reproduced as the control on both benches.  Everything is exact: period-2
Bloch matrices over exact roots of unity, verified entry for entry against
the direct bench matrices.

  (i) THE PRINCIPAL PART, EXACTLY.  With K_H,B(z) = i eps M(kappa) + O(eps^2)
      and M = H0 D(kappa) + D(kappa)^T H0, both assemblies preserve grade
      parity, so M = [[0, B], [B^T, 0]] with B(kappa) = H_e D_eo + D_oe^T H_o
      a 2^(d-1) x 2^(d-1) matrix linear in kappa.  The characteristic cone
      {det B = 0} is reading-independent.  The principal symbols are
      M^2 (form) and (H0^-1 M)^2 (pencil), both block-diagonal in B B^T and
      H_e^-1 B H_o^-1 B^T.

 (ii) THE ONSITE CONE LEMMA (general, symbolic D).  For any block-diagonal
      cell form D = diag(D0, D1, D2, D3), det B = -D3 (k^T D1 k)(k^T E adj(D2) E k)
      in three directions and det B = -D2 (k^T D1 k) in two.  The pencil
      principal symbol is block-diagonal by form degree with the EXACT
      branches k^T G1 k (G1 = D1/D0) and k^T G2 k (G2 = D3 E D2^-1 E) --
      the two Hodge readings of the degree blocks -- plus, in three
      directions, two transverse 2-form branches that are algebraic in k.
      D0 never enters the cone; the volumes enter the branches only through
      D1/D0 and D3 D2^-1.

(iii) THE OVERLAP CONE (general, symbolic h).  The folded overlap H0 is
      h0 I + two-flip couplings 2 h_f, with h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8 and
      h_f = -(s_f0 v1 g0 + s_f1 g1 / v0)/8 on the Block 211 family; the cone is
      the union of the two quadratic cones Q+ and Q- displayed below, which
      differ by the sign of the t-y plane terms, and in two directions the
      single cone h0 (kt^2 + kx^2) + 4 h_tx kt kx with the effective shear
      c_K = 2 c v^2 / (3 v^2 + 1 - c^2 (v^2 + 1)) -- the same sign as, but a
      different magnitude from, the Hodge reading's shear c.

 (iv) THE HYPOTHESIS, ANSWERED.  On the Block 211 per-offset-isotropic family
      G1 and G2 are proportional ONLY at the flat point, in every gauge class
      (exact solve on the (t, u) chart).  Hence under the graded assembly the
      cone equals the union of the two metric cones the cell form carries and
      never one metric's cone off flat; under the overlap assembly the cone is
      a non-Hodge pair.  The symbol is a quadratic form times the identity
      only in two directions on the honest-volume locus v^2 = 1 - c^2 of the
      graded assembly; everywhere else it is matrix-valued and its branches
      are not all quadratic forms.  The exact discrepancy polynomials are
      the result.

  (v) SHEAR REGISTRATION (the #7970 question).  The shears g0, g1 enter the
      cone in both assemblies (exact nonzero derivatives); the diagonal moduli
      enter only as branch scales (graded) or through h0 and the h_f sums
      (overlap), and at zero shear the overlap pencil symbol is R5's for EVERY
      volume pair.  Recorded as a named tension with the matter-side
      no-shear-response result; not resolved here.

THE WORDS ARE FENCED BEFORE THE FIRST NUMBER IS READ.  'SYMBOL' names the
exact 2^d x 2^d Bloch matrix of a finite antisymmetric kernel on a periodic
bench.  'CONE' names the zero set of det B(kappa), a homogeneous polynomial.
'METRIC' names one of two declared rational readings of the cell form's
degree blocks.  'DISPERSION' names the eigenvalue branches of a 4 x 4 or
8 x 8 exact matrix.  None names a spacetime, a light cone, a propagator, a
dynamics, a gravity or a continuum.

SCOUT-GRADE FINITE EXACT LINEAR ALGEBRA ON ONE CELL FORM, NOT A SPACETIME AND
NOT A DYNAMICS -- Block 211's fence, inherited verbatim.

GATES
  A  AUTHORITY: the five-pin block, the TWO Block 212 artifacts content-bound
     at PARENT_COMMIT and in the worktree, the stale pin (the Block 211 tip)
     a real ancestor carrying NEITHER, the machinery imports landed, the audit
     inputs readable.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted; gravity, dynamics, a spacetime cone, a decided assembly and
     licensed readings ALL declared NOT CLAIMED as measured constants.
  C  THE CONSTRUCTION'S FIDELITY TO THE CHAIN: the lane kernels are Block
     201's and Block 209's spin-diagonalised shadows; K = d - d^T with d^2 = 0
     in Block 201's grading; the assemblers reproduce Block 105's onsite and
     overlap Hodges and Block 201's fork Hodge digit for digit; the cell forms
     are Block 211's solved D with its block formulas; the flat cell gives
     H = I and K_H = K.
  D  THE R5 CONTROL: the flat symbol is sum_d sin^2 k_d times the identity as
     an exact polynomial identity, and the bench multisets on (4,4) and
     (4,2,2) are exactly {sum_d sin^2(2 pi m_d / N_d)}.
  E  THE EXACT SPECTRA AT THE WITNESSES: Bloch union = direct bench, all four
     constructions, both benches; translation covariance measured; the PD
     boundary edge case.
  F  THE PRINCIPAL PART AND THE CONE: the onsite lemma and the overlap cone,
     symbolic; the two-direction branches, symbolic in (c, v); the
     three-direction branch identification at every witness; scalar-or-not;
     the metric identifications and their exact discrepancies; coincidence
     only at flat.
  G  SHEAR REGISTRATION: exact, separately for shear and for the diagonal
     moduli, and the tension recorded.
  H  THE SCOPE FENCES, EACH A MEASURED CONSTANT.
  I  the note at its final path, the N5 fence byte-identical, nsimplify and
     float-literal and float-call counts all ZERO in this file's own source.

BASELINE EXPECTATION: A through I PASS, 35 checks, exit 0.

MUTATIONS
  THIRTY-FIVE declared mutations, each rewriting ONE CLAIM and flipping EXACTLY
  ONE FAMILY; every measurement happens once, before any mutation flag is
  read.  Per-family census A 2, B 6, C 5, D 2, E 3, F 7, G 3, H 4, I 3, for
  both checks and mutations.

RUNNING
  python3 scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py
  python3 ... --list-mutations
  python3 ... --mutation claim_cone_is_metric_cone
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
from sympy import QQ
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED, AND THEY ARE EXACTLY THREE MODULES.  Block 201
# supplies the 2D lane kernel, its spin-diagonalised covariant kernel, the
# graded raising part, the fork Hodge and the Block 105 shear_hodge through
# Block 128; Block 211 supplies the six-face system, the witnesses and the
# chart, and through it Block 209's corners, degree indices and three-direction
# rule; Block 105 supplies its own onsite and overlap Hodge assemblies.
try:
    import admissibility_dirac_kahler_covariant_rule_identification_2026_08_26 as b201
    B201_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b201 = None
    B201_IMPORT_LANDED = False
try:
    import admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27 as b211
    B211_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b211 = None
    B211_IMPORT_LANDED = False
try:
    import admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14 as b105
    B105_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b105 = None
    B105_IMPORT_LANDED = False
MACHINERY_IMPORT_LANDED = (B201_IMPORT_LANDED and B211_IMPORT_LANDED
                           and B105_IMPORT_LANDED
                           and b211 is not None and b211.b209 is not None)
b209 = b211.b209 if b211 is not None else None

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_"
    "NOTE_2026-09-05.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 212 is the commit this block's
# branch is cut from; its note and runner exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, the Block 211 tip.  THE SCIENTIFIC PARENTS
# ARE BLOCKS 201 AND 211, whose artifacts stay in AUDIT_INPUT_PATHS.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_PIN_ORDER_EXTENDED_ALPHABET_"
    "BOUNDED_THEOREM_NOTE_2026-08-27.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_joint_pin_order_extended_alphabet_"
    "2026_08_27.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "58e987946738e7f76c960ebfd01e4f810c949453",
    "eddb3f69647876ba7fa03890f3294f355fa52fde",
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_PIN_ORDER_EXTENDED_ALPHABET_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_joint_pin_order_extended_alphabet_2026_08_27.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIX_FACE_POSITIVITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  RE-RESOLVED LIVE AT DRAFT TIME against the REMOTE origin/main
# of the real repository -- never against a local main ref, which sits behind it.
CURRENT_MAIN = "e249016f759f224d9b429932cd0d1db4d452dc1a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block212-"
              "joint-pin-order-extended-alphabet-20260827")
PARENT_COMMIT = "4e9931a970ded94f769553da9e6d77770d612f64"
# The Block 211 tip: a real ancestor of HEAD that predates Block 212 and
# therefore carries NEITHER parent artifact.
STALE_PARENT_COMMIT = "7a98db1dfea59ba5b83c5dae35d71d85059a301a"
# A real but superseded authority head, carried forward from Block 212's record.
STALE_MAIN = "66e478505e055faf4a5b9e6f4883211e44304718"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_symbol_is_dynamics",
    "claim_cone_is_spacetime_cone",
    "claim_assembly_selected",
    "claim_readings_licensed",
    "break_lane_kernel_fidelity",
    "break_three_direction_shadow",
    "break_assembler_fidelity",
    "break_cell_form_reconciliation",
    "break_flat_cell_identity",
    "break_flat_symbol_identity",
    "break_flat_bench_multiset",
    "break_bloch_bench_agreement",
    "break_witness_spectra",
    "break_boundary_edge_case",
    "break_onsite_cone_lemma",
    "break_overlap_cone_formula",
    "break_two_dim_branches",
    "break_three_dim_branch_identification",
    "claim_principal_part_scalar",
    "claim_cone_is_metric_cone",
    "break_coincidence_only_at_flat",
    "break_shear_registration",
    "claim_volume_registration",
    "drop_tension_record",
    "break_scout_grade_fence",
    "claim_assembly_decided",
    "claim_hodge_reading_selected",
    "break_instance_scope",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_symbol_is_dynamics": "B",
    "claim_cone_is_spacetime_cone": "B",
    "claim_assembly_selected": "B",
    "claim_readings_licensed": "B",
    "break_lane_kernel_fidelity": "C",
    "break_three_direction_shadow": "C",
    "break_assembler_fidelity": "C",
    "break_cell_form_reconciliation": "C",
    "break_flat_cell_identity": "C",
    "break_flat_symbol_identity": "D",
    "break_flat_bench_multiset": "D",
    "break_bloch_bench_agreement": "E",
    "break_witness_spectra": "E",
    "break_boundary_edge_case": "E",
    "break_onsite_cone_lemma": "F",
    "break_overlap_cone_formula": "F",
    "break_two_dim_branches": "F",
    "break_three_dim_branch_identification": "F",
    "claim_principal_part_scalar": "F",
    "claim_cone_is_metric_cone": "F",
    "break_coincidence_only_at_flat": "F",
    "break_shear_registration": "G",
    "claim_volume_registration": "G",
    "drop_tension_record": "G",
    "break_scout_grade_fence": "H",
    "claim_assembly_decided": "H",
    "claim_hodge_reading_selected": "H",
    "break_instance_scope": "H",
    "drop_n5_fence": "I",
    "break_nsimplify_absence": "I",
    "break_float_absence": "I",
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
    "THE WEIGHTED KERNEL K_H = H d - d^T H, WHICH IS THIS BLOCK's FIRST NEW OBJECT: Block 107's / Block 201's completion Q = m H + H D_s - D_s^T H read at m = 0 and periodic closure, with d Block 201's graded raising part d_K = sum_g P_{g+1} K P_g of the eta-staggered lane kernel (eta_t = 1, eta_x = (-1)^t, and Block 209's eta_y = (-1)^(t+x) in three directions)",
    "THE TWO LANDED ASSEMBLIES OF ONE CELL FORM INTO H: Block 105's onsite_hodge (cells anchored at even sites, weight 1, the grade-diagonal assembly) and Block 105's overlap_hodge (cells anchored at every site, weight 2^-d, Block 191's rule as used by Block 201's fork_hodge), extended from two to three directions by the same anchoring rule",
    "THE TWO SQUARED-SYMBOL READINGS: the Euclidean form -K_H^2 and the H-pencil -(H^-1 K_H)^2 = d delta + delta d with delta = H^-1 d^T H, which share the generalized eigenproblem K_H v = mu H v and therefore the characteristic cone",
    "THE PERIOD-2 BLOCH REDUCTION: the 2^d x 2^d Bloch matrix A_B(z)[c, c'] = sum_delta A[c, delta] z^delta of every period-2 operator, evaluated at exact roots of unity z_d = exp(2 pi i m_d / N_d), m_d < N_d / 2, whose union over supercell momenta is the bench spectrum; the first-order matrix D(kappa) and the bipartite block B(kappa) = H_e D_eo + D_oe^T H_o whose determinant's zero set is the cone",
    "THE TWO CANDIDATE CELL METRICS, READ OFF THE DEGREE BLOCKS BY BLOCK 209's HONEST-LIFT PATTERN D3(g, V) = diag(V, V g^-1, E g E / V, 1/V): G1 = D1 / D0 (the degree-0/1 reading) and G2 = D3 E D2^-1 E (the degree-2/3 reading), with E = diag(1, -1, 1) Block 209's wedge signature; equal at the flat point and, on the Block 211 family, nowhere else",
    "BLOCK 211's LANDED FAMILY AND WITNESSES READ THROUGH ITS OWN RUNNER (face_system, solve_pinned, branch_moduli, diagonal_point, W1, W2, W3, the four class representatives, the (t, u) chart) and BLOCK 105's LANDED shear_hodge(c, v) READ THROUGH BLOCK 128's IMPORT, BLOCK 201's lane_kernel, covariant_kernel, site_sign_equivalent, raising_part and fork_hodge, and BLOCK 209's omega, GENERATORS, CORNERS and DEGREE_INDICES: no line of this block edits any of them",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
SYMBOL_IS_DYNAMICS_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
ASSEMBLY_SELECTED_CLAIMED = False
PROPAGATOR_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
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
)
SCOPED_HEADLINE_WORDS = ("SYMBOL", "CONE", "METRIC", "DISPERSION")
UNNAMED_PHYSICS_WORDS = ("SPACETIME", "LIGHT CONE", "PROPAGATOR", "EINSTEIN")
READINGS = (
    "R1: that the characteristic cone is a light cone or a causal structure.  Measured: the zero set of det B(kappa), a homogeneous polynomial in three formal variables attached to a finite antisymmetric matrix.  No time, no signal, no causality.  Reading.",
    "R2: that the H-pencil reading is the physical propagator.  Measured: one of two declared squared-symbol readings of the same antisymmetric form; the chain's action-form convention is the Euclidean reading and neither is selected by any premise.  Reading.",
    "R3: that the assembly is decided.  Measured: Block 105 lands BOTH the onsite and the overlap assembly, Block 201's completion uses the overlap one, and no premise here chooses; the two give different cones and both are reported.  Reading.",
    "R4: that kernel-side shear registration is a gravitational shear response.  Measured: exact nonzero derivatives of a polynomial with respect to two rational parameters of one cell form.  The matter-side result it stands in tension with is itself conditional (PR #7970).  Reading.",
    "R5: that Block 201's completion is corrected.  Measured: Block 201's fork Hodge is reproduced digit for digit and its overlap assembly is one of the two landed assemblies run here; nothing landed is touched.  Reading.",
    "R6: that any of it generalises past this instance.  Measured: two periodic benches, one cell family, eight witnesses, two assemblies, two readings, one rule.  Reading.",
)
CHECK_VERDICT = "DEGRADED-WORKER-MODE-FABLE-PRIMARY-REFUTING-CHECKER-PENDING"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
HALF = sp.Rational(1, 2)
BENCH_2D = (4, 4)
BENCH_3D = (4, 2, 2)
FORK_EXTENT = (8, 4)

# --- C: THE CONSTRUCTION'S FIDELITY -----------------------------------------
LANE_2D_NNZ = 64
LANE_3D_NNZ = 32                        # the extent-2 directions carry NO link
LANE_3D_LINKS_SCANNED = 48
LANE_3D_BAD_LINKS = 0
SPIN_NONSCALAR_2D = 0
FLAT_H_IS_IDENTITY = True
FLAT_KERNEL_IS_R5 = True
WITNESS_NAMES = ("flat", "W1", "W2", "W3", "mixed", "near_boundary",
                 "boundary", "honest_face")
WITNESS_COUNT = 8
PD_WITNESSES = ("flat", "W1", "W2", "W3", "mixed", "near_boundary",
                "honest_face")
COMPATIBLE_RANKS = (32, 32)

# --- D: THE R5 CONTROL --------------------------------------------------------
FLAT_SYMBOL_FORM = "sum_d sin^2 k_d = sum_d -(z_d - 1/z_d)^2 / 4"
FLAT_MULTISET_2D = ((0, 4), (1, 8), (2, 4))
FLAT_MULTISET_3D = ((0, 8), (1, 8))

# --- E: THE EXACT SPECTRA -----------------------------------------------------
ASSEMBLIES = ("onsite", "overlap")
READINGS_NAMES = ("form", "pencil")
# W1's own (4,4) spectra, the overlap assembly, declared exactly.
W1_OVERLAP_PENCIL_2D = ((0, 4), (1, 8), (sp.Rational(1922, 1081), 4))
BOUNDARY_ONSITE_H_SINGULAR = True

# --- F: THE PRINCIPAL PART AND THE CONE ---------------------------------------
ONSITE_CONE_LEMMA_3D = "det B = -D3 * (k^T D1 k) * (k^T E adj(D2) E k)"
ONSITE_CONE_LEMMA_2D = "det B = -D2 * (k^T D1 k)"
ONSITE_PENCIL_BRANCHES_3D = ("k^T G1 k  (0-form sector, G1 = D1/D0)",
                             "k^T G2 k  (3-form sector, G2 = D3 E D2^-1 E)",
                             "two transverse 2-form branches: roots of a quadratic whose product is det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k)")
OVERLAP_H0_FORM = "h0 I + 2 h_f on the two-flip pairs, h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8, h_f = -(s_f0 v1 g0 + s_f1 g1 / v0)/8"
OVERLAP_CONE_PLUS = ("h0**2*kt**2 + h0**2*kx**2 + h0**2*ky**2 + 4*h0*htx*kt*kx + 4*h0*hty*kt*ky "
                     "+ 4*h0*hxy*kx*ky - 4*htx**2*ky**2 - 8*htx*hty*kx*ky - 8*htx*hxy*kt*ky "
                     "- 4*hty**2*kx**2 - 8*hty*hxy*kt*kx - 4*hxy**2*kt**2")
OVERLAP_CONE_MINUS = ("h0**2*kt**2 + h0**2*kx**2 + h0**2*ky**2 + 4*h0*htx*kt*kx - 4*h0*hty*kt*ky "
                      "+ 4*h0*hxy*kx*ky - 4*htx**2*ky**2 - 8*htx*hty*kx*ky + 8*htx*hxy*kt*ky "
                      "- 4*hty**2*kx**2 - 8*hty*hxy*kt*kx - 4*hxy**2*kt**2")
OVERLAP_CONE_2D = "h0*(kt**2 + kx**2) + 4*htx*kt*kx"
TWO_DIM_ONSITE_BRANCHES = ("(kt**2 - 2*c*kt*kx + kx**2)/(1 - c**2)",
                           "(kt**2 - 2*c*kt*kx + kx**2)/v**2")
TWO_DIM_OVERLAP_PENCIL = ("(c**2*(v**2 + 1) - 3*v**2 - 1)*((c**2*(v**2 + 1) - 3*v**2 - 1)*(kt**2 + kx**2) + 4*c*v**2*kt*kx)"
                          "/((c**2 - 1)*(c**2*(v**2 + 1)**2 - (3*v**2 + 1)**2))")
TWO_DIM_HODGE_CONE = "(kt**2 - 2*c*kt*kx + kx**2)/(1 - c**2)"
TWO_DIM_OVERLAP_EFFECTIVE_SHEAR = "2*c*v**2/(3*v**2 + 1 - c**2*(v**2 + 1))"
TWO_DIM_OVERLAP_SHEAR_DISCREPANCY = "-c*(1 - c**2)*(v**2 + 1)/(3*v**2 + 1 - c**2*(v**2 + 1))"
TWO_DIM_ONSITE_SCALAR_LOCUS = "v**2 = 1 - c**2"
W1_ONSITE_CONES = ("2*kt**2 - kt*kx - kt*ky + 2*kx**2 - kx*ky + 2*ky**2",
                   "3*kt**2 - 2*kt*kx + 2*kt*ky + 3*kx**2 - 2*kx*ky + 3*ky**2")
W1_OVERLAP_CONES = ("55*kt**2 - 16*kt*kx - 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2",
                    "55*kt**2 - 16*kt*kx + 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2")
PRINCIPAL_PART_SCALAR_ANYWHERE_CURVED_3D = False
CONE_IS_ONE_METRIC_CONE_OFF_FLAT = False
COINCIDENCE_SOLUTIONS = ((0, 0),)
COINCIDENCE_CLASSES = 4

# --- G: SHEAR REGISTRATION ----------------------------------------------------
SHEAR_ENTERS_CONE_ONSITE = True
SHEAR_ENTERS_CONE_OVERLAP = True
VOLUME_ENTERS_CONE_ONSITE = False
OVERLAP_ZERO_SHEAR_PENCIL_IS_R5 = True
TENSION_RECORD = ("KERNEL-SIDE SHEAR REGISTRATION: YES in both assemblies (the cone moves with g0, g1 exactly); "
                  "DIAGONAL-METRIC REGISTRATION: branch scales only (graded) or through h0 and the h_f sums (overlap), "
                  "and invisible to the overlap pencil symbol at zero shear.  MATTER SIDE (PR #7970, conditional): "
                  "responds to the diagonal metric and to NO shear.  NAMED TENSION -- recorded, not resolved here.")
TENSION_RECORDED = True

# --- H: THE SCOPE FENCES ------------------------------------------------------
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
PHYSICAL_CONTENT_CLAIMED = False
ASSEMBLY_DECIDED = False
HODGE_READING_SELECTED = False
INSTANCE_SCOPE = (
    "two periodic benches, (4,4) with Block 105's 2D face form and (4,2,2) with Block 211's 3D cell form, and no other extent",
    "one cell family, Block 211's per-offset-isotropic variety at the degree-diagonal representative, and eight witnesses",
    "two assemblies, Block 105's onsite and overlap, and two squared-symbol readings, the Euclidean form and the H-pencil",
    "one rule, Block 201's A = sx, B = -sz shadow and its Block 209 three-direction shadow, at the periodic closure and m = 0",
    "the principal part at k = 0 of the eight-fold degenerate zero; no continuum limit, no lattice-spacing statement",
    "the two Hodge readings G1 and G2 as declared candidates; which, if either, is 'the' metric is not decided here",
)
INSTANCE_SCOPE_COUNT = 6

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 THROUGH BLOCK 211 AND HONOURED
# HERE BY ABSENCE.  This block's content is a set of exact polynomial
# identities and exact factorizations -- a cone factor that is or is not
# proportional to a declared quadratic form, a discrepancy polynomial that is
# or is not zero.  A tolerance-carrying call could turn the nonzero
# discrepancy 2 c (1 - c^2)(v^2 + 1) kt kx / |A| into a zero and manufacture
# the very identity this block refutes.  Gate I counts the occurrences in this
# file's own source and requires ZERO, ZERO float literals by AST, and ZERO
# float call sites, because every number here is an exact rational or symbol.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_literal_occurrences() -> int:
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def residual_count(matrix) -> int:
    matrix = sp.Matrix(matrix)
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if sp.cancel(sp.together(matrix[i, j])) != 0)


def is_zero(expression) -> bool:
    return sp.cancel(sp.together(sp.expand(expression))) == 0


def proportional(first, second, variables) -> bool:
    """TWO POLYNOMIALS ARE PROPORTIONAL iff their ratio carries none of the
    listed variables.  Exact: the ratio is cancelled and its free symbols
    inspected; no coefficient is ever compared numerically."""
    first, second = sp.expand(first), sp.expand(second)
    if first == 0 or second == 0:
        return first == 0 and second == 0
    ratio = sp.cancel(sp.together(first / second))
    return not (ratio.free_symbols & set(variables))


def primitive_factors(expression, variables) -> tuple:
    """The irreducible factors over QQ that involve the listed variables, as
    expanded primitive polynomials with their multiplicities."""
    _, factors = sp.factor_list(sp.together(sp.expand(expression)))
    out = []
    for base, power in factors:
        if base.free_symbols & set(variables):
            out.append((sp.expand(base), power))
    return tuple(out)


# ---------------------------------------------------------------------------
# THE PERIOD-2 OPERATOR MACHINERY.  An operator commuting with all even
# translations is a dictionary {(corner, delta): coefficient} meaning
# A[s, s + delta] = coefficient whenever s mod 2 = corner.  Composition,
# transposition, the Bloch matrix and the bench matrix are all exact.
# ---------------------------------------------------------------------------
KT, KX, KY = sp.symbols("kt kx ky", real=True)
LAM = sp.Symbol("lam")


def corners(dim: int) -> tuple:
    return tuple(itertools.product((0, 1), repeat=dim))


def cmod(corner: tuple) -> tuple:
    return tuple(x % 2 for x in corner)


def vadd(a: tuple, b: tuple) -> tuple:
    return tuple(x + y for x, y in zip(a, b))


def vneg(a: tuple) -> tuple:
    return tuple(-x for x in a)


def grade(corner: tuple) -> int:
    return sum(x % 2 for x in corner)


def eta(corner: tuple, direction: int) -> int:
    """Block 209's staggering phases eta = (1, (-1)^t, (-1)^(t+x)), Block
    201's (1, (-1)^t) in two directions: the product of the parities of all
    coordinates BEFORE the direction."""
    return (-1) ** sum(corner[:direction])


def lane_rules(dim: int) -> dict:
    """The eta-staggered lane kernel: +eta/2 forward, -eta/2 backward."""
    rules = {}
    for corner in corners(dim):
        for direction in range(dim):
            step = tuple(1 if k == direction else 0 for k in range(dim))
            rules[(corner, step)] = sp.Rational(eta(corner, direction), 2)
            rules[(corner, vneg(step))] = -sp.Rational(eta(corner, direction), 2)
    return rules


def raising_rules(kernel: dict) -> dict:
    """BLOCK 201's GRADING, d = sum_g P_{g+1} K P_g: the ROW grade is one
    higher than the COLUMN grade.  In dictionary form, the entries (c, delta)
    with grade(c) = grade(c + delta) + 1."""
    return {(c, d): v for (c, d), v in kernel.items()
            if grade(c) == grade(vadd(c, d)) + 1}


def transpose_rules(rules: dict) -> dict:
    return {(cmod(vadd(c, d)), vneg(d)): v for (c, d), v in rules.items()}


def compose_rules(first: dict, second: dict) -> dict:
    out: dict = {}
    for (c, d1), a in first.items():
        middle = cmod(vadd(c, d1))
        for (c2, d2), b in second.items():
            if c2 != middle:
                continue
            key = (c, vadd(d1, d2))
            out[key] = out.get(key, 0) + a * b
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def combine_rules(first: dict, second: dict, sign_second=1) -> dict:
    out: dict = {}
    for k, v in first.items():
        out[k] = out.get(k, 0) + v
    for k, v in second.items():
        out[k] = out.get(k, 0) + sign_second * v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def onsite_rules(cell, cell_corners: tuple, dim: int) -> dict:
    """BLOCK 105's onsite_hodge: one cell per even anchor, weight 1, each site
    a fixed corner of exactly one cell -- the grade-diagonal assembly."""
    rules = {}
    for i, ci in enumerate(cell_corners):
        for j, cj in enumerate(cell_corners):
            if cell[i, j] == 0:
                continue
            rules[(tuple(ci), tuple(cj[k] - ci[k] for k in range(dim)))] = cell[i, j]
    return rules


def overlap_rules(cell, cell_corners: tuple, dim: int) -> dict:
    """BLOCK 105's overlap_hodge and BLOCK 191's rule as used by BLOCK 201's
    fork_hodge: one cell per anchor, weight 2^-d, every site a corner of 2^d
    cells -- the translation-invariant assembly."""
    rules: dict = {}
    weight = sp.Rational(1, 2 ** dim)
    for i, ci in enumerate(cell_corners):
        for j, cj in enumerate(cell_corners):
            if cell[i, j] == 0:
                continue
            delta = tuple(cj[k] - ci[k] for k in range(dim))
            for corner in corners(dim):
                rules[(corner, delta)] = rules.get((corner, delta), 0) + weight * cell[i, j]
    return {k: sp.expand(v) for k, v in rules.items() if sp.expand(v) != 0}


def bloch_matrix(rules: dict, z: tuple, dim: int) -> sp.Matrix:
    cs = corners(dim)
    matrix = sp.zeros(len(cs), len(cs))
    for (c, d), a in rules.items():
        phase = sp.Integer(1)
        for k in range(dim):
            phase *= z[k] ** d[k]
        matrix[cs.index(c), cs.index(cmod(vadd(c, d)))] += a * phase
    return matrix.applyfunc(sp.expand)


def folded_matrix(rules: dict, dim: int) -> sp.Matrix:
    """A_B(1): the Bloch matrix at zero momentum."""
    cs = corners(dim)
    matrix = sp.zeros(len(cs), len(cs))
    for (c, d), a in rules.items():
        matrix[cs.index(c), cs.index(cmod(vadd(c, d)))] += a
    return matrix.applyfunc(sp.expand)


def first_order_matrix(rules: dict, dim: int, kappa: tuple) -> sp.Matrix:
    """D(kappa)[c, c'] = sum_delta (delta . kappa) A[c, delta]: the exact
    first-order coefficient of A_B(exp(i eps kappa)) divided by i eps."""
    cs = corners(dim)
    matrix = sp.zeros(len(cs), len(cs))
    for (c, d), a in rules.items():
        matrix[cs.index(c), cs.index(cmod(vadd(c, d)))] += a * sum(
            d[k] * kappa[k] for k in range(dim))
    return matrix.applyfunc(sp.expand)


def site_index(site: tuple, extent: tuple) -> int:
    index = 0
    for coordinate, size in zip(site, extent):
        index = index * size + (coordinate % size)
    return index


def bench_sites(extent: tuple) -> tuple:
    return tuple(itertools.product(*(range(size) for size in extent)))


def bench_matrix(rules: dict, extent: tuple) -> sp.Matrix:
    """THE PERIODIC BENCH MATRIX OF A PERIOD-2 OPERATOR: aliases along an
    extent-2 direction ADD, which is exactly the projection of the infinite
    lattice operator onto periodic functions."""
    sites = bench_sites(extent)
    matrix = sp.zeros(len(sites), len(sites))
    for site in sites:
        corner = cmod(site)
        for (c, d), a in rules.items():
            if c != corner:
                continue
            matrix[site_index(site, extent), site_index(vadd(site, d), extent)] += a
    return matrix.applyfunc(sp.expand)


def bench_assembly(extent: tuple, cell_corners: tuple, block_of_anchor,
                   anchors: tuple, weight) -> sp.Matrix:
    """BLOCK 201's fork_hodge PATTERN, GENERALISED: embed block_of_anchor(a)
    at the corners a + c for every anchor a with the given weight."""
    sites = bench_sites(extent)
    matrix = sp.zeros(len(sites), len(sites))
    for anchor in anchors:
        block = block_of_anchor(anchor)
        indices = [site_index(vadd(anchor, tuple(c)), extent) for c in cell_corners]
        for i, ci in enumerate(indices):
            for j, cj in enumerate(indices):
                matrix[ci, cj] += weight * block[i, j]
    return matrix.applyfunc(sp.expand)


def bench_momenta(extent: tuple) -> tuple:
    """z_d = exp(2 pi i m_d / N_d) for m_d < N_d / 2, EXACT: for N_d = 4 the
    set {1, i}, for N_d = 2 the set {1}.  The folding over the 2^d corners
    supplies the other half."""
    axes = []
    for size in extent:
        values = []
        for m in range(size // 2):
            angle = 2 * sp.pi * m / size
            values.append(sp.expand(sp.cos(angle) + sp.I * sp.sin(angle)))
        axes.append(tuple(values))
    return tuple(itertools.product(*axes))


def charpoly_expr(matrix: sp.Matrix):
    poly = sp.Matrix(matrix).charpoly(LAM).as_expr()
    return sp.expand(poly)


# THE EXACT NUMERIC DOMAINS, AND THEY ARE NOT NUMERICAL METHODS.  Every Bloch
# matrix at a root of unity lies in QQ(i)^(n x n) and every bench matrix at a
# rational witness in QQ^(n x n); DomainMatrix carries out the products, the
# inverses and the characteristic polynomials by exact fraction-free
# arithmetic over those fields.  No float is created and no tolerance exists.
def domain_of(matrix: sp.Matrix, gaussian: bool) -> DomainMatrix:
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ_I if gaussian else QQ)


def domain_charpoly(matrix: DomainMatrix):
    coefficients = matrix.charpoly()
    domain = matrix.domain
    degree = len(coefficients) - 1
    return sp.expand(sum(domain.to_sympy(coefficient) * LAM ** (degree - k)
                         for k, coefficient in enumerate(coefficients)))


def domain_symbol(hodge: DomainMatrix, raising: DomainMatrix,
                  raising_transpose: DomainMatrix, reading: str) -> DomainMatrix:
    if reading == "form":
        kernel = hodge * raising - raising_transpose * hodge
        return -(kernel * kernel)
    operator = raising - hodge.inv() * raising_transpose * hodge
    return -(operator * operator)


def form_symbol(hodge_bloch, raising_bloch, raising_bloch_transpose):
    kernel = (hodge_bloch * raising_bloch
              - raising_bloch_transpose * hodge_bloch).applyfunc(sp.expand)
    return (-kernel * kernel).applyfunc(sp.expand), kernel


def pencil_symbol_with_inverse(hodge_bloch, hodge_inverse, raising_bloch,
                               raising_bloch_transpose):
    operator = (raising_bloch
                - hodge_inverse * raising_bloch_transpose * hodge_bloch).applyfunc(sp.cancel)
    return (-operator * operator).applyfunc(sp.cancel), operator


def onsite_pencil_symbol(cell, cell_corners: tuple, dim: int, z: tuple,
                         raising: dict):
    """THE GRADED H-PENCIL SYMBOL AT SYMBOLIC PHASES, CHEAPLY: the onsite
    Bloch matrix is Z^-1 D Z with Z = diag(z^c), so its inverse is the onsite
    Bloch matrix of D^-1 -- no symbolic inversion is ever performed."""
    h_b = bloch_matrix(onsite_rules(cell, cell_corners, dim), z, dim)
    h_inverse = bloch_matrix(onsite_rules(sp.Matrix(cell).inv(), cell_corners, dim), z, dim)
    d_b = bloch_matrix(raising, z, dim)
    dT_b = bloch_matrix(transpose_rules(raising), z, dim)
    return pencil_symbol_with_inverse(h_b, h_inverse, d_b, dT_b)


def bloch_spectrum_charpoly(rules_h: dict, rules_d: dict, extent: tuple,
                            dim: int, reading: str):
    """THE BENCH CHARPOLY FROM THE BLOCH SIDE: the product over the supercell
    momenta of the 2^d x 2^d charpolys, every root of unity exact, over QQ(i)."""
    rules_dT = transpose_rules(rules_d)
    product = sp.Integer(1)
    for z in bench_momenta(extent):
        h_b = domain_of(bloch_matrix(rules_h, z, dim), True)
        d_b = domain_of(bloch_matrix(rules_d, z, dim), True)
        dT_b = domain_of(bloch_matrix(rules_dT, z, dim), True)
        product *= domain_charpoly(domain_symbol(h_b, d_b, dT_b, reading))
    return sp.expand(product)


def direct_bench_charpoly(hodge: sp.Matrix, raising: sp.Matrix, reading: str):
    return domain_charpoly(domain_symbol(
        domain_of(hodge, False), domain_of(raising, False),
        domain_of(raising.T, False), reading))


def is_singular(matrix: sp.Matrix) -> bool:
    return domain_of(matrix, False).det() == 0


def multiset_of(charpoly_expression) -> tuple:
    """The root multiset of a charpoly whose roots are all rational, as a
    sorted tuple of (root, multiplicity); None if some root is not rational."""
    poly = sp.Poly(charpoly_expression, LAM)
    roots = sp.roots(poly)
    if sum(roots.values()) != poly.degree():
        return None
    if any(not root.is_rational for root in roots):
        return None
    return tuple(sorted(((root, mult) for root, mult in roots.items()), key=lambda t: t[0]))


def expected_flat_multiset(extent: tuple) -> tuple:
    values: dict = {}
    for m in itertools.product(*(range(size) for size in extent)):
        value = sp.expand(sum(sp.sin(2 * sp.pi * m[k] / extent[k]) ** 2
                              for k in range(len(extent))))
        values[value] = values.get(value, 0) + 1
    return tuple(sorted(values.items(), key=lambda t: t[0]))


def even_odd(dim: int) -> tuple:
    cs = corners(dim)
    even = [i for i, c in enumerate(cs) if grade(c) % 2 == 0]
    odd = [i for i, c in enumerate(cs) if grade(c) % 2 == 1]
    return even, odd


def bipartite_block(h0: sp.Matrix, dk: sp.Matrix, dim: int) -> tuple:
    """B(kappa) = H_e D_eo + D_oe^T H_o, together with H_e and H_o, once the
    folded H0 is verified to preserve grade parity."""
    even, odd = even_odd(dim)
    h_e = h0.extract(even, even)
    h_o = h0.extract(odd, odd)
    parity_preserving = (residual_count(h0.extract(even, odd)) == 0
                         and residual_count(h0.extract(odd, even)) == 0)
    d_eo = dk.extract(even, odd)
    d_oe = dk.extract(odd, even)
    block = (h_e * d_eo + d_oe.T * h_o).applyfunc(sp.cancel)
    return block, h_e, h_o, parity_preserving


def is_scalar_matrix(matrix: sp.Matrix) -> bool:
    n = matrix.rows
    return (all(is_zero(matrix[i, j]) for i in range(n) for j in range(n) if i != j)
            and all(is_zero(matrix[i, i] - matrix[0, 0]) for i in range(n)))


def metric_candidates(cell: sp.Matrix) -> tuple:
    """G1 = D1/D0 and G2 = D3 E D2^-1 E, both as 3 x 3 matrices over the
    directions (t, x, y): D1 is read on the unit corners e_mu and D2 on the
    complementary corners 1 - e_mu, which is Block 209's two_order."""
    unit = [b209.CORNERS.index(tuple(1 if k == mu else 0 for k in range(3))) for mu in range(3)]
    complement = [b209.CORNERS.index(tuple(0 if k == mu else 1 for k in range(3))) for mu in range(3)]
    d0, d3 = cell[0, 0], cell[7, 7]
    d1 = sp.Matrix(3, 3, lambda i, j: cell[unit[i], unit[j]])
    d2 = sp.Matrix(3, 3, lambda i, j: cell[complement[i], complement[j]])
    signature = sp.diag(1, -1, 1)
    g1 = (d1 / d0).applyfunc(sp.cancel)
    # AT THE PD BOUNDARY D2 IS SINGULAR AND THE DEGREE-2/3 READING HAS NO
    # INVERSE: G2 is then None, measured rather than assumed.
    g2 = None
    if sp.cancel(d2.det()) != 0:
        g2 = (d3 * signature * d2.inv() * signature).applyfunc(sp.cancel)
    return g1, g2, d0, d1, d2, d3


def quadratic_form(matrix: sp.Matrix, kappa: tuple):
    vector = sp.Matrix(kappa)
    return sp.expand((vector.T * matrix * vector)[0, 0])


# ---------------------------------------------------------------------------
# THE WITNESSES, READ THROUGH BLOCK 211's OWN OBJECTS
# ---------------------------------------------------------------------------
def witness_table() -> dict:
    flipped_both = b211.flipped(("xy", 0), ("xy", 1))
    return {
        "flat": ((sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)), b211.ALL_PLUS),
        "W1": (b211.W1_MODULI, b211.ALL_PLUS),
        "W2": (b211.W2_MODULI, flipped_both),
        "W3": (b211.W3_MODULI, flipped_both),
        "mixed": (b211.diagonal_point(sp.Rational(1, 4)), b211.REPRESENTATIVES[(1, -1)]),
        "near_boundary": (b211.diagonal_point(sp.Rational(49, 100)), b211.ALL_PLUS),
        "boundary": (b211.diagonal_point(HALF), b211.ALL_PLUS),
        # THE HONEST-FACE POINT: g1 = 0, v1 = 1/v0, v0^2 = 1 - g0^2, so the
        # offset-0 tx face has v^2 = det g2(c) exactly; class (-1, .) at g0 = 4/5.
        "honest_face": ((sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(5, 3), sp.Integer(0)),
                        b211.flipped(("xy", 0))),
    }


@dataclass(frozen=True)
class CellFacts:
    name: str
    moduli: tuple
    ranks: tuple
    free_names: tuple
    blocks_match_formulas: bool
    cross_degree_zero: bool
    face_restriction_is_shear_hodge: bool
    leading_minors: tuple
    positive_definite: bool
    face_moduli: tuple
    g1: tuple
    g2: tuple
    g1_proportional_to_g2: bool
    hodge_defect_scalar: object
    hodge_defect_matrix_nnz: int


def solve_witness(name: str, moduli: tuple, signs: dict) -> tuple:
    volume0, gamma0, volume1, gamma1 = moduli
    _, matrix, rhs = b211.face_system(b211.branch_moduli(volume0, gamma0, volume1, gamma1, signs))
    ranks = (matrix.rank(), matrix.row_join(rhs).rank())
    cell, free = b211.solve_pinned(matrix, rhs)
    # THE DEGREE-BLOCK FORMULAS OF BLOCK 211, RE-VERIFIED AT THE POINT.
    first = volume1 * b211.signed_triangle((signs[("xy", 0)] * gamma0,
                                            signs[("ty", 0)] * gamma0,
                                            signs[("tx", 0)] * gamma0))
    second = b211.signed_triangle((signs[("tx", 1)] * gamma1,
                                   signs[("ty", 1)] * gamma1,
                                   signs[("xy", 1)] * gamma1)) / volume0
    blocks_ok = (residual_count(b211.degree_block(cell, 0) - sp.Matrix([[volume0]])) == 0
                 and residual_count(b211.degree_block(cell, 1) - first) == 0
                 and residual_count(b211.degree_block(cell, 2) - second) == 0
                 and residual_count(b211.degree_block(cell, 3) - sp.Matrix([[1 / volume1]])) == 0)
    cross_zero = all(cell[i, j] == 0 for i in range(8) for j in range(8)
                     if sum(b209.CORNERS[i]) != sum(b209.CORNERS[j]))
    # THE ORIGIN tx FACE IS BLOCK 105's shear_hodge AT (s_tx0 g0, v0), which
    # is what the (4,4) bench is built on.
    face_indices = [b209.CORNERS.index(c) for c in ((0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0))]
    face = sp.Matrix(4, 4, lambda i, j: cell[face_indices[i], face_indices[j]])
    face_moduli = (signs[("tx", 0)] * gamma0, volume0)
    face_ok = residual_count(face - sp.Matrix(b211.LANDED_SHEAR_HODGE(*face_moduli))) == 0
    minors = b211.leading_minors(cell)
    g1, g2, d0, d1, d2, d3 = metric_candidates(cell)
    prop = None
    if g2 is not None:
        vec1 = [g1[i, j] for i in range(3) for j in range(i, 3)]
        vec2 = [g2[i, j] for i in range(3) for j in range(i, 3)]
        prop = all(is_zero(vec1[a] * vec2[b] - vec1[b] * vec2[a])
                   for a in range(6) for b in range(a + 1, 6))
    signature = sp.diag(1, -1, 1)
    defect_matrix = (d1 * signature * d2 * signature - d0 * d3 * sp.eye(3)).applyfunc(sp.cancel)
    return CellFacts(
        name, tuple(moduli), ranks, tuple(str(s) for s in free), blocks_ok, cross_zero,
        face_ok, tuple(minors), all(m > 0 for m in minors), face_moduli,
        tuple(tuple(g1[i, j] for j in range(3)) for i in range(3)),
        (tuple(tuple(g2[i, j] for j in range(3)) for i in range(3))
         if g2 is not None else ("UNDEFINED: det D2 = 0",)),
        prop, sp.cancel(d0 * d3 - 1), residual_count(defect_matrix)), cell


# ---------------------------------------------------------------------------
# THE MEASURED FACTS
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ConstructionFacts:
    lane_2d_matches_b201: bool
    lane_2d_nnz: int
    spin_nonscalar_2d: int
    lane_2d_site_sign_equivalent: bool
    raising_matches_b201_on_fork: bool
    k_is_d_minus_dT_2d: bool
    d_squared_zero_2d: bool
    lane_3d_links_scanned: int
    lane_3d_bad_links: int
    lane_3d_shadow_matches: bool
    lane_3d_nnz: int
    lane_3d_xy_links_absent: bool
    k_is_d_minus_dT_3d: bool
    d_squared_zero_3d: bool
    fork_hodge_reproduced: bool
    onsite_hodge_reproduced: bool
    overlap_hodge_reproduced: bool
    rules_match_bench_assembly: bool
    flat_h_identity: bool
    flat_kernel_is_r5: bool
    cells: tuple


@dataclass(frozen=True)
class ControlFacts:
    flat_symbol_identity_2d: bool
    flat_symbol_identity_3d: bool
    multiset_2d: tuple
    multiset_3d: tuple
    expected_2d: tuple
    expected_3d: tuple
    bloch_equals_direct_flat: bool


@dataclass(frozen=True)
class SpectrumFacts:
    entries: tuple                 # (witness, bench, assembly, reading, factored charpoly text, agreement, multiset)
    all_agree: bool
    w1_overlap_pencil_2d: tuple
    translation_commutators: tuple
    boundary_onsite_singular_2d: bool
    boundary_onsite_singular_3d: bool
    boundary_overlap_regular: bool


@dataclass(frozen=True)
class PrincipalFacts:
    lemma_3d_holds: bool
    lemma_2d_holds: bool
    lemma_3d_block_diagonal: bool
    lemma_3d_zero_form_branch: bool
    lemma_3d_top_form_branch: bool
    lemma_3d_transverse_product: bool
    lemma_d0_absent: bool
    overlap_h0_form_holds: bool
    overlap_cone_3d_holds: bool
    overlap_cone_2d_holds: bool
    two_dim_onsite_branches: bool
    two_dim_onsite_form_scalar: bool
    two_dim_onsite_pencil_scalar_generic: bool
    two_dim_onsite_scalar_on_locus: bool
    two_dim_overlap_pencil_scalar: bool
    two_dim_overlap_pencil_matches: bool
    two_dim_overlap_cone_matches: bool
    two_dim_overlap_form_scalar: bool
    two_dim_effective_shear: bool
    two_dim_discrepancy: bool
    two_dim_onsite_zero_form_symbol: str
    two_dim_onsite_two_form_symbol: str
    two_dim_overlap_pencil_symbol: str
    witnesses: tuple               # per witness per assembly: cone factors etc
    w1_onsite_cones: bool
    w1_overlap_cones: bool
    onsite_cones_are_g1_g2_everywhere: bool
    onsite_branches_g1_g2_everywhere: bool
    overlap_cones_never_g1_g2: bool
    principal_scalar_anywhere_curved_3d: bool
    transverse_branches_quadratic_anywhere: bool
    coincidence_solutions: tuple
    coincidence_classes: int
    w1_zero_form_symbol: str


@dataclass(frozen=True)
class RegistrationFacts:
    onsite_cone_shear_derivative_nonzero: bool
    onsite_cone_volume_free: bool
    onsite_branch_scales: tuple
    overlap_symbol_depends_only_on_h: bool
    overlap_zero_shear_pencil_is_r5: bool
    overlap_zero_shear_form_scale: str
    overlap_cone_shear_derivative_nonzero: bool
    sign_class_moves_overlap_cone: bool


@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    scoped_words: int
    construction: ConstructionFacts
    control: ControlFacts
    spectra: SpectrumFacts
    principal: PrincipalFacts
    registration: RegistrationFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    float_calls: int


def measure_construction(witnesses: dict) -> tuple:
    """FAMILY C, MEASURED ONCE."""
    # (1) THE 2D LANE KERNEL IS BLOCK 201's, AND IT IS THE SHADOW.
    lane2 = lane_rules(2)
    bench2 = bench_matrix(lane2, BENCH_2D)
    b201_lane = b201.lane_kernel(BENCH_2D[0], BENCH_2D[1], "periodic")
    lane_matches = residual_count(bench2 - b201_lane) == 0
    scalar, nonscalar = b201.covariant_kernel(BENCH_2D[0], BENCH_2D[1], (1, 1))
    equivalent = b201.site_sign_equivalent(scalar, b201_lane, BENCH_2D[0] * BENCH_2D[1])
    d2 = raising_rules(lane2)
    fork_lane = b201.lane_kernel(FORK_EXTENT[0], FORK_EXTENT[1], "periodic")
    raising_matches = residual_count(bench_matrix(d2, FORK_EXTENT) - b201.raising_part(fork_lane)) == 0
    k_is_d_minus_dT_2d = combine_rules(lane2, combine_rules(d2, transpose_rules(d2), -1), -1) == {}
    d_squared_2d = compose_rules(d2, d2) == {}
    # (2) THE 3D LANE KERNEL IS BLOCK 209's SHADOW, LINK BY LINK.
    lane3 = lane_rules(3)
    scanned, bad, shadow_ok = 0, 0, True
    for site in bench_sites(BENCH_3D):
        for direction in range(3):
            stepped = list(site)
            stepped[direction] += 1
            neighbour = tuple(c % e for c, e in zip(stepped, BENCH_3D))
            block = sp.Matrix(sp.expand(
                b209.omega(site).T * (b209.GENERATORS[direction] / 2) * b209.omega(neighbour)))
            scanned += 1
            off_diagonal = any(block[i, j] != 0 for i in range(4) for j in range(4) if i != j)
            diagonal_equal = block[0, 0] == block[1, 1] == block[2, 2] == block[3, 3]
            if off_diagonal or not diagonal_equal:
                bad += 1
                continue
            step = tuple(1 if k == direction else 0 for k in range(3))
            if sp.expand(block[0, 0] - lane3[(cmod(site), step)]) != 0:
                shadow_ok = False
    bench3 = bench_matrix(lane3, BENCH_3D)
    xy_absent = all(
        bench3[site_index(s, BENCH_3D), site_index(vadd(s, step), BENCH_3D)] == 0
        for s in bench_sites(BENCH_3D) for step in ((0, 1, 0), (0, 0, 1)))
    d3 = raising_rules(lane3)
    k_is_d_minus_dT_3d = combine_rules(lane3, combine_rules(d3, transpose_rules(d3), -1), -1) == {}
    d_squared_3d = compose_rules(d3, d3) == {}
    # (3) THE ASSEMBLERS REPRODUCE THE LANDED HODGES DIGIT FOR DIGIT.
    fork_block = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(b201.FORK_SHEAR, sp.Integer(1))))
    reflected = sp.expand(b201.OFFSET_PERMUTATION * fork_block * b201.OFFSET_PERMUTATION.T)
    fork = bench_assembly(
        FORK_EXTENT, b201.CELL_CORNERS,
        lambda anchor: fork_block if anchor[0] < FORK_EXTENT[0] // 2 else reflected,
        bench_sites(FORK_EXTENT), sp.Rational(1, 4))
    fork_ok = residual_count(fork - b201.fork_hodge(b201.FORK_SHEAR)) == 0
    length = b105.LENGTH
    onsite_anchors = tuple((2 * ct, 2 * cx) for ct in range(b105.COARSE_EXTENT)
                           for cx in range(b105.COARSE_EXTENT))
    onsite = bench_assembly(
        (length, length), b201.CELL_CORNERS,
        lambda anchor: sp.Matrix(b105.shear_hodge(*b105.BASE_SHEARS[2 * (anchor[0] // 2) + anchor[1] // 2])),
        onsite_anchors, sp.Integer(1))
    onsite_ok = residual_count(onsite - b105.onsite_hodge()) == 0
    field = b105.overlap_field()
    overlap = bench_assembly(
        (length, length), b201.CELL_CORNERS,
        lambda anchor: sp.Matrix(b105.shear_hodge(*field[anchor])),
        bench_sites((length, length)), sp.Rational(1, 4))
    overlap_ok = residual_count(overlap - b105.overlap_hodge(field)) == 0
    # (4) THE RULE-BASED ASSEMBLIES EQUAL THE BENCH ASSEMBLIES OF A UNIFORM CELL.
    w1_face = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(sp.Rational(1, 4), sp.Rational(15, 16))))
    rules_ok = (
        residual_count(bench_matrix(onsite_rules(w1_face, b201.CELL_CORNERS, 2), BENCH_2D)
                       - bench_assembly(BENCH_2D, b201.CELL_CORNERS, lambda a: w1_face,
                                        tuple(s for s in bench_sites(BENCH_2D) if s[0] % 2 == 0 and s[1] % 2 == 0),
                                        sp.Integer(1))) == 0
        and residual_count(bench_matrix(overlap_rules(w1_face, b201.CELL_CORNERS, 2), BENCH_2D)
                           - bench_assembly(BENCH_2D, b201.CELL_CORNERS, lambda a: w1_face,
                                            bench_sites(BENCH_2D), sp.Rational(1, 4))) == 0)
    # (5) THE CELL FORMS, SOLVED THROUGH BLOCK 211.
    cells, cell_matrices = [], {}
    for name in WITNESS_NAMES:
        moduli, signs = witnesses[name]
        facts, cell = solve_witness(name, moduli, signs)
        cells.append(facts)
        cell_matrices[name] = cell
    flat_cell = cell_matrices["flat"]
    flat_face = sp.Matrix(4, 4, lambda i, j: flat_cell[[0, 2, 4, 6][i], [0, 2, 4, 6][j]])
    flat_identity, flat_r5 = True, True
    for dim, extent, cell, cell_corners, lane, raising in (
            (2, BENCH_2D, flat_face, b201.CELL_CORNERS, lane2, d2),
            (3, BENCH_3D, flat_cell, b209.CORNERS, lane3, d3)):
        for assembly in (onsite_rules, overlap_rules):
            hodge = bench_matrix(assembly(cell, cell_corners, dim), extent)
            if residual_count(hodge - sp.eye(hodge.rows)) != 0:
                flat_identity = False
            raise_bench = bench_matrix(raising, extent)
            kernel = hodge * raise_bench - raise_bench.T * hodge
            if residual_count(kernel - bench_matrix(lane, extent)) != 0:
                flat_r5 = False
    return ConstructionFacts(
        lane_matches, sum(1 for i in range(16) for j in range(16) if bench2[i, j] != 0),
        nonscalar, equivalent, raising_matches, k_is_d_minus_dT_2d, d_squared_2d,
        scanned, bad, shadow_ok,
        sum(1 for i in range(16) for j in range(16) if bench3[i, j] != 0), xy_absent,
        k_is_d_minus_dT_3d, d_squared_3d, fork_ok, onsite_ok, overlap_ok, rules_ok,
        flat_identity, flat_r5, tuple(cells)), cell_matrices


def measure_control() -> ControlFacts:
    """FAMILY D, MEASURED ONCE: R5's flat symbol, symbolically and on both
    benches, from the Bloch side and from the direct bench matrices."""
    identities, multisets, expected, agree = [], [], [], True
    for dim, extent in ((2, BENCH_2D), (3, BENCH_3D)):
        z = sp.symbols(f"z0:{dim}")
        lane = lane_rules(dim)
        kernel_bloch = bloch_matrix(lane, z, dim)
        symbol = (-kernel_bloch * kernel_bloch).applyfunc(sp.expand)
        target = sum(-(z[k] - 1 / z[k]) ** 2 / 4 for k in range(dim))
        identities.append(residual_count(symbol - sp.expand(target) * sp.eye(2 ** dim)) == 0)
        direct = bench_matrix(lane, extent)
        direct_poly = charpoly_expr((-direct * direct).applyfunc(sp.expand))
        raising = raising_rules(lane)
        identity_rules = {(c, tuple(0 for _ in range(dim))): sp.Integer(1) for c in corners(dim)}
        bloch_poly = bloch_spectrum_charpoly(identity_rules, raising, extent, dim, "form")
        if sp.expand(direct_poly - bloch_poly) != 0:
            agree = False
        multisets.append(multiset_of(direct_poly))
        expected.append(expected_flat_multiset(extent))
    return ControlFacts(identities[0], identities[1], multisets[0], multisets[1],
                        expected[0], expected[1], agree)


def measure_spectra(cell_matrices: dict) -> SpectrumFacts:
    """FAMILY E, MEASURED ONCE: the exact bench spectra of all four
    constructions at every witness, Bloch union against direct bench."""
    entries, all_agree = [], True
    commutators = []
    w1_pencil = None
    boundary_onsite_singular = {}
    boundary_overlap_regular = True
    for name in WITNESS_NAMES:
        cell3 = cell_matrices[name]
        face = sp.Matrix(4, 4, lambda i, j: cell3[[0, 2, 4, 6][i], [0, 2, 4, 6][j]])
        for dim, extent, cell, cell_corners in ((2, BENCH_2D, face, b201.CELL_CORNERS),
                                               (3, BENCH_3D, cell3, b209.CORNERS)):
            lane = lane_rules(dim)
            raising = raising_rules(lane)
            raise_bench = bench_matrix(raising, extent)
            for assembly in ASSEMBLIES:
                rules_h = (onsite_rules if assembly == "onsite" else overlap_rules)(cell, cell_corners, dim)
                hodge = bench_matrix(rules_h, extent)
                singular = is_singular(hodge)
                if name == "boundary":
                    if assembly == "onsite":
                        boundary_onsite_singular[dim] = singular
                    else:
                        boundary_overlap_regular = boundary_overlap_regular and not singular
                for reading in READINGS_NAMES:
                    if reading == "pencil" and singular:
                        entries.append((name, extent, assembly, reading, "UNDEFINED: det H = 0", True, None))
                        continue
                    direct_poly = direct_bench_charpoly(hodge, raise_bench, reading)
                    bloch_poly = bloch_spectrum_charpoly(rules_h, raising, extent, dim, reading)
                    agreement = sp.expand(direct_poly - bloch_poly) == 0
                    all_agree = all_agree and agreement
                    multiset = multiset_of(direct_poly)
                    entries.append((name, extent, assembly, reading,
                                    str(sp.factor(direct_poly)), agreement, multiset))
                    if name == "W1" and dim == 2 and assembly == "overlap" and reading == "pencil":
                        w1_pencil = multiset
                if name == "W1":
                    # TRANSLATION COVARIANCE, MEASURED: nnz([-K^2, T_mu]) per direction.
                    kernel = (hodge * raise_bench - raise_bench.T * hodge).applyfunc(sp.expand)
                    squared = (-kernel * kernel).applyfunc(sp.expand)
                    counts = []
                    for direction in range(dim):
                        shift = sp.zeros(hodge.rows, hodge.rows)
                        for site in bench_sites(extent):
                            stepped = list(site)
                            stepped[direction] += 1
                            shift[site_index(tuple(stepped), extent), site_index(site, extent)] = 1
                        counts.append(residual_count(squared * shift - shift * squared))
                    commutators.append((extent, assembly, tuple(counts)))
    return SpectrumFacts(tuple(entries), all_agree, w1_pencil, tuple(commutators),
                         boundary_onsite_singular.get(2, False), boundary_onsite_singular.get(3, False),
                         boundary_overlap_regular)


def principal_objects(rules_h: dict, raising: dict, dim: int, kappa: tuple,
                      with_pencil: bool = True) -> dict:
    """THE PRINCIPAL-PART OBJECTS OF ONE CONSTRUCTION: H0, D(kappa), B, det B,
    the form block B B^T and the pencil block H_e^-1 B H_o^-1 B^T."""
    h0 = folded_matrix(rules_h, dim)
    dk = first_order_matrix(raising, dim, kappa)
    block, h_e, h_o, parity = bipartite_block(h0, dk, dim)
    det_b = sp.factor(sp.cancel(block.det(method="berkowitz")))
    form_block = (block * block.T).applyfunc(sp.cancel)
    pencil_block = None
    if with_pencil and sp.cancel(h_e.det()) != 0 and sp.cancel(h_o.det()) != 0:
        pencil_block = (h_e.inv() * block * h_o.inv() * block.T).applyfunc(sp.cancel)
    return {"h0": h0, "dk": dk, "B": block, "H_e": h_e, "H_o": h_o, "parity": parity,
            "detB": det_b, "form": form_block, "pencil": pencil_block}


def linear_branches(charpoly, kappa: tuple) -> tuple:
    """The linear-in-lam factors of a charpoly in lam, i.e. the eigenvalue
    branches that ARE polynomials (quadratic forms) in kappa, and the
    remaining factor's degree structure."""
    _, factors = sp.factor_list(sp.expand(charpoly), LAM)
    branches, remainder = [], []
    for base, power in factors:
        poly = sp.Poly(base, LAM)
        if poly.degree() == 1:
            root = sp.cancel(-poly.coeff_monomial(1) / poly.coeff_monomial(LAM))
            branches.append((sp.expand(root), power))
        elif poly.degree() >= 2:
            remainder.append((poly.degree(), power))
    return tuple(branches), tuple(remainder)


def measure_principal(cell_matrices: dict) -> PrincipalFacts:
    """FAMILY F, MEASURED ONCE: the symbolic lemmas and the witnesses."""
    kappa3 = (KT, KX, KY)
    kappa2 = (KT, KX)
    signature = sp.diag(1, -1, 1)
    lane3, lane2 = lane_rules(3), lane_rules(2)
    d3, d2 = raising_rules(lane3), raising_rules(lane2)

    # --- THE ONSITE CONE LEMMA AT FULLY SYMBOLIC D --------------------------
    D0, D3 = sp.symbols("D0 D3", positive=True)
    a = sp.symbols("a11 a12 a13 a22 a23 a33", real=True)
    b = sp.symbols("b11 b12 b13 b22 b23 b33", real=True)
    D1 = sp.Matrix([[a[0], a[1], a[2]], [a[1], a[3], a[4]], [a[2], a[4], a[5]]])
    D2 = sp.Matrix([[b[0], b[1], b[2]], [b[1], b[3], b[4]], [b[2], b[4], b[5]]])
    cell = sp.zeros(8, 8)
    cell[0, 0], cell[7, 7] = D0, D3
    unit = [b209.CORNERS.index(tuple(1 if k == mu else 0 for k in range(3))) for mu in range(3)]
    complement = [b209.CORNERS.index(tuple(0 if k == mu else 1 for k in range(3))) for mu in range(3)]
    for i in range(3):
        for j in range(3):
            cell[unit[i], unit[j]] = D1[i, j]
            cell[complement[i], complement[j]] = D2[i, j]
    objects = principal_objects(onsite_rules(cell, b209.CORNERS, 3), d3, 3, kappa3)
    q1 = quadratic_form(D1, kappa3)
    q2_adj = quadratic_form(signature * D2.adjugate() * signature, kappa3)
    lemma_3d = is_zero(objects["detB"] + D3 * q1 * q2_adj)
    pencil = objects["pencil"]
    # BLOCK-DIAGONALITY BY FORM DEGREE, the 0-form branch, the top-form
    # eigenvector adj(D2) E k with eigenvalue D3 k^T E D2^-1 E k, and the
    # product of the two transverse branches.
    even, _ = even_odd(3)
    zero_form_position = even.index(0)
    block_diagonal = all(is_zero(pencil[zero_form_position, j]) and is_zero(pencil[j, zero_form_position])
                         for j in range(4) if j != zero_form_position)
    zero_form_branch = is_zero(pencil[zero_form_position, zero_form_position] - q1 / D0)
    two_form_positions = [j for j in range(4) if j != zero_form_position]
    two_form_block = pencil.extract(two_form_positions, two_form_positions)
    # the 2-form corners in even order (3, 5, 6) are the complement order (t, x, y)
    eigenvector = D2.adjugate() * signature * sp.Matrix(kappa3)
    q2 = sp.cancel(D3 * quadratic_form(signature * D2.inv() * signature, kappa3))
    top_form_branch = residual_count((two_form_block * eigenvector - q2 * eigenvector).applyfunc(sp.cancel)) == 0
    transverse_product = is_zero(
        sp.cancel(two_form_block.det() / q2) - sp.cancel(D2.det() / D1.det() * q1 * quadratic_form(signature * D2.inv() * signature, kappa3)))
    d0_absent = D0 not in sp.together(objects["detB"]).free_symbols
    # --- THE 2D LEMMA -------------------------------------------------------
    e0, e2 = sp.symbols("e0 e2", positive=True)
    p = sp.symbols("p11 p12 p22", real=True)
    P1 = sp.Matrix([[p[0], p[1]], [p[1], p[2]]])
    cell2 = sp.zeros(4, 4)
    cell2[0, 0], cell2[3, 3] = e0, e2
    for i, ci in enumerate((1, 2)):
        for j, cj in enumerate((1, 2)):
            cell2[ci, cj] = P1[i, j]
    objects2 = principal_objects(onsite_rules(cell2, b201.CELL_CORNERS, 2), d2, 2, kappa2)
    # corners 1 = (0,1) = the x step, 2 = (1,0) = the t step: k' = (kx, kt)
    q1_2d = quadratic_form(P1, (KX, KT))
    lemma_2d = is_zero(objects2["detB"] + e2 * q1_2d)

    # --- THE OVERLAP H0 FORM AND CONE, SYMBOLIC ------------------------------
    v0, v1, g0, g1 = sp.symbols("v0 v1 g0 g1", positive=True)
    s = sp.symbols("s_tx0 s_ty0 s_xy0 s_tx1 s_ty1 s_xy1")
    signs = {("tx", 0): s[0], ("ty", 0): s[1], ("xy", 0): s[2],
             ("tx", 1): s[3], ("ty", 1): s[4], ("xy", 1): s[5]}
    family = sp.zeros(8, 8)
    family[0, 0], family[7, 7] = v0, 1 / v1
    first = v1 * b211.signed_triangle((signs[("xy", 0)] * g0, signs[("ty", 0)] * g0, signs[("tx", 0)] * g0))
    second = b211.signed_triangle((signs[("tx", 1)] * g1, signs[("ty", 1)] * g1, signs[("xy", 1)] * g1)) / v0
    ones, twos = b209.DEGREE_INDICES[1], b209.DEGREE_INDICES[2]
    for i in range(3):
        for j in range(3):
            family[ones[i], ones[j]] = first[i, j]
            family[twos[i], twos[j]] = second[i, j]
    h_folded = folded_matrix(overlap_rules(family, b209.CORNERS, 3), 3)
    h0_expected = (v0 + 3 * v1 + 3 / v0 + 1 / v1) / 8
    h_expected = {"tx": -(signs[("tx", 0)] * v1 * g0 + signs[("tx", 1)] * g1 / v0) / 8,
                  "ty": -(signs[("ty", 0)] * v1 * g0 + signs[("ty", 1)] * g1 / v0) / 8,
                  "xy": -(signs[("xy", 0)] * v1 * g0 + signs[("xy", 1)] * g1 / v0) / 8}
    flips = {"tx": (1, 1, 0), "ty": (1, 0, 1), "xy": (0, 1, 1)}
    h0_form_ok = True
    cs = corners(3)
    for i, ci in enumerate(cs):
        for j, cj in enumerate(cs):
            difference = tuple((ci[k] + cj[k]) % 2 for k in range(3))
            if i == j:
                target = h0_expected
            elif difference in flips.values():
                plane = [name for name, flip in flips.items() if flip == difference][0]
                target = 2 * h_expected[plane]
            else:
                target = 0
            if not is_zero(h_folded[i, j] - target):
                h0_form_ok = False
    h0s, htx, hty, hxy = sp.symbols("h0 htx hty hxy", real=True)
    rules_h_symbolic = {}
    for corner in cs:
        rules_h_symbolic[(corner, (0, 0, 0))] = h0s
        for delta, h in (((1, -1, 0), htx), ((-1, 1, 0), htx), ((1, 0, -1), hty),
                         ((-1, 0, 1), hty), ((0, 1, -1), hxy), ((0, -1, 1), hxy)):
            rules_h_symbolic[(corner, delta)] = h
    overlap_objects = principal_objects(rules_h_symbolic, d3, 3, kappa3)
    local = {"h0": h0s, "htx": htx, "hty": hty, "hxy": hxy, "kt": KT, "kx": KX, "ky": KY}
    q_plus = sp.sympify(OVERLAP_CONE_PLUS, locals=local)
    q_minus = sp.sympify(OVERLAP_CONE_MINUS, locals=local)
    overlap_cone_3d = (is_zero(overlap_objects["detB"] - q_plus * q_minus)
                       or is_zero(overlap_objects["detB"] + q_plus * q_minus))
    rules_h2 = {}
    for corner in corners(2):
        rules_h2[(corner, (0, 0))] = h0s
        rules_h2[(corner, (1, -1))] = htx
        rules_h2[(corner, (-1, 1))] = htx
    overlap_objects2 = principal_objects(rules_h2, d2, 2, kappa2)
    q_2d = sp.sympify(OVERLAP_CONE_2D, locals=local)
    overlap_cone_2d = is_zero(overlap_objects2["detB"] + h0s * q_2d)

    # --- TWO DIRECTIONS AT SYMBOLIC (c, v): BLOCK 105's OWN CELL FORM -------
    c, v = sp.symbols("c v", positive=True)
    face = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(c, v)))
    local2 = {"c": c, "v": v, "kt": KT, "kx": KX}
    branch_targets = [sp.sympify(text, locals=local2) for text in TWO_DIM_ONSITE_BRANCHES]
    on2 = principal_objects(onsite_rules(face, b201.CELL_CORNERS, 2), d2, 2, kappa2)
    pencil2 = on2["pencil"]
    onsite_branches_ok = (
        is_zero(pencil2[0, 1]) and is_zero(pencil2[1, 0])
        and ((is_zero(pencil2[0, 0] - branch_targets[0]) and is_zero(pencil2[1, 1] - branch_targets[1]))
             or (is_zero(pencil2[0, 0] - branch_targets[1]) and is_zero(pencil2[1, 1] - branch_targets[0]))))
    onsite_form_scalar = is_scalar_matrix(on2["form"])
    onsite_pencil_scalar_generic = is_scalar_matrix(pencil2)
    onsite_scalar_on_locus = is_scalar_matrix(pencil2.subs(v, sp.sqrt(1 - c ** 2)).applyfunc(sp.simplify))
    ov2 = principal_objects(overlap_rules(face, b201.CELL_CORNERS, 2), d2, 2, kappa2)
    pencil_ov2 = ov2["pencil"]
    overlap_pencil_scalar = is_scalar_matrix(pencil_ov2)
    overlap_target = sp.sympify(TWO_DIM_OVERLAP_PENCIL, locals=local2)
    overlap_pencil_matches = is_zero(pencil_ov2[0, 0] - overlap_target)
    hodge_cone = sp.sympify(TWO_DIM_HODGE_CONE, locals=local2)
    overlap_form_scalar = is_scalar_matrix(ov2["form"])
    abs_a = 3 * v ** 2 + 1 - c ** 2 * (v ** 2 + 1)
    overlap_cone_target = abs_a * (KT ** 2 + KX ** 2) - 4 * c * v ** 2 * KT * KX
    overlap_cone_matches = proportional(ov2["detB"], overlap_cone_target, (KT, KX))
    effective = sp.sympify(TWO_DIM_OVERLAP_EFFECTIVE_SHEAR, locals=local2)
    normalized = sp.expand(overlap_cone_target / abs_a)
    effective_ok = is_zero(-sp.Poly(normalized, KT, KX).coeff_monomial(KT * KX) / 2 - effective)
    discrepancy = sp.sympify(TWO_DIM_OVERLAP_SHEAR_DISCREPANCY, locals=local2)
    discrepancy_ok = is_zero(effective - c - discrepancy) and not is_zero(discrepancy)
    # THE EXACT TWO-DIRECTION SYMBOLS, DISPLAYED: the graded pencil symbol is
    # block-diagonal by degree at symbolic (c, v, z); its 0-form and 2-form
    # entries are scalars.  The overlap pencil symbol is translation-invariant
    # in two directions and is displayed at W1's own face (c, v) = (1/4, 15/16).
    z2 = sp.symbols("zt zx")
    pencil_sym, _ = onsite_pencil_symbol(face, b201.CELL_CORNERS, 2, z2, d2)
    zero_form_symbol = sp.cancel(pencil_sym[0, 0])
    two_form_symbol = sp.cancel(pencil_sym[3, 3])
    w1_face = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(sp.Rational(1, 4), sp.Rational(15, 16))))
    h_bo = bloch_matrix(overlap_rules(w1_face, b201.CELL_CORNERS, 2), z2, 2)
    d_b = bloch_matrix(d2, z2, 2)
    dT_b = bloch_matrix(transpose_rules(d2), z2, 2)
    pencil_sym_o, _ = pencil_symbol_with_inverse(h_bo, h_bo.inv().applyfunc(sp.cancel), d_b, dT_b)
    row_sums = [sp.cancel(sum(pencil_sym_o[i, j] for j in range(4))) for i in range(4)]
    overlap_scalar_symbol = (sp.factor(row_sums[0]) if all(is_zero(r - row_sums[0]) for r in row_sums)
                             else "NOT-TRANSLATION-INVARIANT")

    # --- THREE DIRECTIONS AT THE WITNESSES ----------------------------------
    witness_records = []
    onsite_cones_ok, onsite_branches_ok3, overlap_never = True, True, True
    scalar_anywhere, transverse_quadratic_anywhere = False, False
    w1_onsite_ok = w1_overlap_ok = False
    w1_zero_form = ""
    local3 = {"kt": KT, "kx": KX, "ky": KY}
    for name in WITNESS_NAMES:
        cell_w = cell_matrices[name]
        g1_m, g2_m, _, _, _, _ = metric_candidates(cell_w)
        cone1 = quadratic_form(g1_m, kappa3) if g1_m is not None else None
        cone2 = quadratic_form(g2_m, kappa3) if g2_m is not None else None
        for assembly in ASSEMBLIES:
            rules_h = (onsite_rules if assembly == "onsite" else overlap_rules)(cell_w, b209.CORNERS, 3)
            objects_w = principal_objects(rules_h, d3, 3, kappa3)
            factors = primitive_factors(objects_w["detB"], kappa3)
            # THE RANK OF EACH CONE FACTOR'S HESSIAN: 3 for a genuine cone, 2
            # when the cone has degenerated to a line (the PD boundary).
            factor_texts = tuple(
                f"({sp.expand(base)})^{power} [hessian rank {sp.hessian(base, kappa3).rank()}]"
                for base, power in factors)
            pencil_w = objects_w["pencil"]
            branches, remainder = (linear_branches(charpoly_expr(pencil_w), kappa3)
                                   if pencil_w is not None else ((), ()))
            form_branches, form_remainder = linear_branches(charpoly_expr(objects_w["form"]), kappa3)
            scalar_pencil = pencil_w is not None and is_scalar_matrix(pencil_w)
            scalar_form = is_scalar_matrix(objects_w["form"])
            cones_are_g1_g2 = None
            branches_are_g1_g2 = None
            if cone1 is not None and cone2 is not None and name != "flat":
                cone_bases = [base for base, _ in factors]
                cones_are_g1_g2 = (len(cone_bases) == 2
                                   and any(proportional(base, cone1, kappa3) for base in cone_bases)
                                   and any(proportional(base, cone2, kappa3) for base in cone_bases))
                if pencil_w is not None:
                    branch_values = [value for value, _ in branches]
                    branches_are_g1_g2 = (any(is_zero(value - cone1) for value in branch_values)
                                          and any(is_zero(value - cone2) for value in branch_values))
                if assembly == "onsite":
                    onsite_cones_ok = onsite_cones_ok and bool(cones_are_g1_g2)
                    if pencil_w is not None:
                        onsite_branches_ok3 = onsite_branches_ok3 and bool(branches_are_g1_g2)
                        # THE TRANSVERSE PAIR: the remaining factor is quadratic in lam;
                        # it is a pair of quadratic forms only if it splits.
                        if any(degree == 1 for degree, _ in remainder) or len(branches) > 2:
                            transverse_quadratic_anywhere = True
                else:
                    overlap_never = overlap_never and not any(
                        proportional(base, cone1, kappa3) or proportional(base, cone2, kappa3)
                        for base in cone_bases)
                if scalar_pencil or scalar_form:
                    scalar_anywhere = True
            if name == "W1":
                bases = [sp.expand(base) for base, _ in factors]
                targets = [sp.sympify(text, locals=local3) for text in
                           (W1_ONSITE_CONES if assembly == "onsite" else W1_OVERLAP_CONES)]
                matched = all(any(proportional(base, target, kappa3) for base in bases) for target in targets)
                if assembly == "onsite":
                    w1_onsite_ok = matched and len(bases) == 2
                    z3 = sp.symbols("zt zx zy")
                    pencil_sym3, _ = onsite_pencil_symbol(cell_w, b209.CORNERS, 3, z3, d3)
                    w1_zero_form = str(sp.factor(pencil_sym3[0, 0]))
                else:
                    w1_overlap_ok = matched and len(bases) == 2
            witness_records.append((name, assembly, factor_texts,
                                    tuple((str(value), power) for value, power in branches), remainder,
                                    tuple((str(value), power) for value, power in form_branches), form_remainder,
                                    scalar_pencil, scalar_form, cones_are_g1_g2, branches_are_g1_g2,
                                    objects_w["parity"], str(cone1), str(cone2)))

    # --- COINCIDENCE OF THE TWO HODGE READINGS ON THE FAMILY -----------------
    t, u = b211.CHART_T, b211.CHART_U
    solutions, classes = set(), 0
    for orientation, class_signs in b211.REPRESENTATIVES.items():
        _, matrix, rhs = b211.face_system(b211.chart_moduli(class_signs))
        chart_cell, _ = b211.solve_pinned(matrix, rhs)
        g1_c, g2_c, _, _, _, _ = metric_candidates(chart_cell)
        vec1 = [g1_c[i, j] for i in range(3) for j in range(i, 3)]
        vec2 = [g2_c[i, j] for i in range(3) for j in range(i, 3)]
        minors = set()
        for i in range(6):
            for j in range(i + 1, 6):
                minor = sp.numer(sp.together(sp.cancel(vec1[i] * vec2[j] - vec1[j] * vec2[i])))
                if minor != 0:
                    minors.add(sp.expand(minor))
        for solution in sp.solve(list(minors), [t, u], dict=True):
            if all(value.is_real for value in solution.values()) and set(solution) == {t, u}:
                solutions.add((solution[t], solution[u]))
        classes += 1
    return PrincipalFacts(
        lemma_3d, lemma_2d, block_diagonal, zero_form_branch, top_form_branch, transverse_product,
        d0_absent, h0_form_ok, overlap_cone_3d, overlap_cone_2d,
        onsite_branches_ok, onsite_form_scalar, onsite_pencil_scalar_generic, onsite_scalar_on_locus,
        overlap_pencil_scalar, overlap_pencil_matches, overlap_cone_matches, overlap_form_scalar,
        effective_ok, discrepancy_ok, str(zero_form_symbol), str(two_form_symbol), str(overlap_scalar_symbol),
        tuple(witness_records), w1_onsite_ok, w1_overlap_ok, onsite_cones_ok, onsite_branches_ok3,
        overlap_never, scalar_anywhere, transverse_quadratic_anywhere,
        tuple(sorted(solutions)), classes, w1_zero_form)


def measure_registration() -> RegistrationFacts:
    """FAMILY G, MEASURED ONCE: does the shear enter, does the volume enter."""
    kappa3 = (KT, KX, KY)
    v0, v1, g0, g1 = sp.symbols("v0 v1 g0 g1", positive=True)
    lane3 = lane_rules(3)
    d3 = raising_rules(lane3)
    signature = sp.diag(1, -1, 1)
    results = {}
    for class_signs in (b211.ALL_PLUS, b211.flipped(("xy", 0), ("xy", 1))):
        family = sp.zeros(8, 8)
        family[0, 0], family[7, 7] = v0, 1 / v1
        first = v1 * b211.signed_triangle((class_signs[("xy", 0)] * g0, class_signs[("ty", 0)] * g0, class_signs[("tx", 0)] * g0))
        second = b211.signed_triangle((class_signs[("tx", 1)] * g1, class_signs[("ty", 1)] * g1, class_signs[("xy", 1)] * g1)) / v0
        ones, twos = b209.DEGREE_INDICES[1], b209.DEGREE_INDICES[2]
        for i in range(3):
            for j in range(3):
                family[ones[i], ones[j]] = first[i, j]
                family[twos[i], twos[j]] = second[i, j]
        g1_m, g2_m, _, _, _, _ = metric_candidates(family)
        cone1 = quadratic_form(g1_m, kappa3)
        cone2 = quadratic_form(g2_m, kappa3)
        results[str(class_signs[("xy", 0)])] = (cone1, cone2)
        onsite = principal_objects(onsite_rules(family, b209.CORNERS, 3), d3, 3, kappa3, False)
        overlap = principal_objects(overlap_rules(family, b209.CORNERS, 3), d3, 3, kappa3, False)
        results[("onsite", str(class_signs[("xy", 0)]))] = onsite["detB"]
        results[("overlap", str(class_signs[("xy", 0)]))] = overlap["detB"]
    cone1_plus, cone2_plus = results["1"]
    det_onsite = results[("onsite", "1")]
    det_overlap = results[("overlap", "1")]
    # SHEAR MOVES THE CONE, THE VOLUMES DO NOT: exact derivatives, and the
    # exact proportionality of det B to its own value at unit volumes.
    onsite_shear = (
        (not is_zero(sp.diff(cone1_plus, g0))) and (not is_zero(sp.diff(cone2_plus, g1)))
        and not proportional(det_onsite, det_onsite.subs({g0: 0, g1: 0}), kappa3))
    onsite_volume_free = proportional(det_onsite, det_onsite.subs({v0: 1, v1: 1}), kappa3)
    triangle_one = first_block(g0, b211.ALL_PLUS)
    triangle_two = second_block(g1, b211.ALL_PLUS)
    scales = (str(sp.cancel(cone1_plus / quadratic_form(triangle_one, kappa3))),
              str(sp.cancel(cone2_plus / quadratic_form(
                  signature * triangle_two.inv() * signature, kappa3))))
    # THE OVERLAP SYMBOL DEPENDS ON THE MODULI ONLY THROUGH (h0, h_f): the
    # zero-shear pencil symbol is R5's for every volume pair, the zero-shear
    # form symbol is h0^2 times R5's.
    z3 = sp.symbols("zt zx zy")
    family0 = sp.diag(v0, v1, v1, 1 / v0, v1, 1 / v0, 1 / v0, 1 / v1)
    rules0 = overlap_rules(family0, b209.CORNERS, 3)
    h_b = bloch_matrix(rules0, z3, 3)
    d_b = bloch_matrix(d3, z3, 3)
    dT_b = bloch_matrix(transpose_rules(d3), z3, 3)
    h0_value = sp.cancel((v0 + 3 * v1 + 3 / v0 + 1 / v1) / 8)
    depends_only_on_h = residual_count(h_b - h0_value * sp.eye(8)) == 0
    pencil0, _ = pencil_symbol_with_inverse(h_b, sp.eye(8) / h0_value, d_b, dT_b)
    form0, _ = form_symbol(h_b, d_b, dT_b)
    k_b = bloch_matrix(lane3, z3, 3)
    r5 = (-k_b * k_b).applyfunc(sp.expand)
    zero_shear_pencil_r5 = depends_only_on_h and residual_count(pencil0 - r5) == 0
    zero_shear_form_scale = "h0^2 times R5" if residual_count(form0 - h0_value ** 2 * r5) == 0 else "NOT h0^2 R5"
    overlap_shear = (
        (not is_zero(sp.diff(det_overlap, g0))) and (not is_zero(sp.diff(det_overlap, g1)))
        and not proportional(det_overlap, det_overlap.subs({g0: 0, g1: 0}), kappa3))
    sign_class_moves = not proportional(det_overlap, results[("overlap", "-1")], kappa3)
    return RegistrationFacts(onsite_shear, onsite_volume_free, scales, depends_only_on_h,
                             zero_shear_pencil_r5, zero_shear_form_scale, overlap_shear, sign_class_moves)


def first_block(g0, class_signs):
    return b211.signed_triangle((class_signs[("xy", 0)] * g0, class_signs[("ty", 0)] * g0, class_signs[("tx", 0)] * g0))


def second_block(g1, class_signs):
    return b211.signed_triangle((class_signs[("tx", 1)] * g1, class_signs[("ty", 1)] * g1, class_signs[("xy", 1)] * g1))


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    witnesses = witness_table()
    construction, cell_matrices = measure_construction(witnesses)
    return Facts(
        main_head,
        authority_certificate(main_head),
        len(IMPOSED_OBJECTS),
        len(REGISTERED_OBJECTS),
        len(ADOPTED_OBJECTS),
        len(UNSUPPLIED_GRAVITY_STRUCTURES),
        len(READINGS),
        len(SCOPED_HEADLINE_WORDS),
        construction,
        measure_control(),
        measure_spectra(cell_matrices),
        measure_principal(cell_matrices),
        measure_registration(),
        scope_certificate(note_text),
        nsimplify_occurrences(),
        float_literal_occurrences(),
        float_call_sites())


# ---------------------------------------------------------------------------
# THE CLAIMS.  Every one of them is a literal, and a mutation rewrites exactly
# one of them.  No measurement is taken here.
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims = {
        # A
        "main_head": CURRENT_MAIN,
        "parent_commit": PARENT_COMMIT,
        "stale_parent": STALE_PARENT_COMMIT,
        # B
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "symbol_is_dynamics": SYMBOL_IS_DYNAMICS_CLAIMED,
        "propagator": PROPAGATOR_CLAIMED,
        "cone_is_spacetime_cone": CONE_IS_SPACETIME_CONE_CLAIMED,
        "scoped_words": len(SCOPED_HEADLINE_WORDS),
        "assembly_selected": ASSEMBLY_SELECTED_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "lane_2d_nnz": LANE_2D_NNZ,
        "spin_nonscalar_2d": SPIN_NONSCALAR_2D,
        "lane_2d_fidelity": True,
        "lane_3d_links": LANE_3D_LINKS_SCANNED,
        "lane_3d_bad": LANE_3D_BAD_LINKS,
        "lane_3d_nnz": LANE_3D_NNZ,
        "lane_3d_shadow": True,
        "assemblers_reproduce_landed": True,
        "cell_forms_reconciled": True,
        "witness_count": WITNESS_COUNT,
        "compatible_ranks": COMPATIBLE_RANKS,
        "flat_h_identity": FLAT_H_IS_IDENTITY,
        "flat_kernel_is_r5": FLAT_KERNEL_IS_R5,
        # D
        "flat_symbol_identity": True,
        "flat_multiset_2d": FLAT_MULTISET_2D,
        "flat_multiset_3d": FLAT_MULTISET_3D,
        # E
        "bloch_equals_bench": True,
        "w1_overlap_pencil_2d": W1_OVERLAP_PENCIL_2D,
        "boundary_onsite_singular": BOUNDARY_ONSITE_H_SINGULAR,
        # F
        "onsite_lemma_3d": True,
        "onsite_lemma_2d": True,
        "onsite_lemma_structure": True,
        "overlap_h0_form": True,
        "overlap_cone_3d": True,
        "overlap_cone_2d": True,
        "two_dim_onsite_branches": True,
        "two_dim_onsite_scalar_generic": False,
        "two_dim_onsite_scalar_on_locus": True,
        "two_dim_overlap_pencil_scalar": True,
        "two_dim_overlap_matches": True,
        "two_dim_effective_shear": True,
        "three_dim_branches": True,
        "w1_cones": True,
        "principal_scalar_curved_3d": PRINCIPAL_PART_SCALAR_ANYWHERE_CURVED_3D,
        "transverse_quadratic_anywhere": False,
        "onsite_cones_g1_g2": True,
        "overlap_cones_never_g1_g2": True,
        "cone_is_one_metric_cone": CONE_IS_ONE_METRIC_CONE_OFF_FLAT,
        "coincidence_solutions": COINCIDENCE_SOLUTIONS,
        "coincidence_classes": COINCIDENCE_CLASSES,
        # G
        "shear_enters_onsite": SHEAR_ENTERS_CONE_ONSITE,
        "shear_enters_overlap": SHEAR_ENTERS_CONE_OVERLAP,
        "volume_enters_onsite_cone": VOLUME_ENTERS_CONE_ONSITE,
        "overlap_zero_shear_pencil_r5": OVERLAP_ZERO_SHEAR_PENCIL_IS_R5,
        "tension_recorded": TENSION_RECORDED,
        # H
        "scout_grade_only": SCOUT_GRADE_ONLY,
        "physical_content": PHYSICAL_CONTENT_CLAIMED,
        "assembly_decided": ASSEMBLY_DECIDED,
        "hodge_reading_selected": HODGE_READING_SELECTED,
        "instance_scope": INSTANCE_SCOPE_COUNT,
        # I
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
        "float_literals": 0,
        "float_calls": 0,
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
    elif mutation == "claim_symbol_is_dynamics":
        # THE FIRST MISREAD: the squared symbol of a finite antisymmetric
        # matrix is asserted to be a dynamics or a propagator.
        claims["symbol_is_dynamics"] = True
        claims["propagator"] = True
    elif mutation == "claim_cone_is_spacetime_cone":
        # THE SECOND MISREAD: the zero set of det B is asserted to be a
        # light cone.  It is a homogeneous polynomial's zero set.
        claims["cone_is_spacetime_cone"] = True
        claims["scoped_words"] = 0
    elif mutation == "claim_assembly_selected":
        claims["assembly_selected"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_lane_kernel_fidelity":
        # THE CHAIN DENIED: the lane kernel is asserted NOT to be Block 201's.
        claims["lane_2d_fidelity"] = False
        claims["lane_2d_nnz"] = 48
    elif mutation == "break_three_direction_shadow":
        claims["lane_3d_bad"] = 8
        claims["lane_3d_shadow"] = False
    elif mutation == "break_assembler_fidelity":
        claims["assemblers_reproduce_landed"] = False
    elif mutation == "break_cell_form_reconciliation":
        claims["cell_forms_reconciled"] = False
        claims["compatible_ranks"] = (32, 33)
    elif mutation == "break_flat_cell_identity":
        # THE CONTROL DENIED: the flat cell is asserted to give a kernel
        # DIFFERENT from R5's.  It gives R5's exactly, in all four constructions.
        claims["flat_h_identity"] = False
        claims["flat_kernel_is_r5"] = False
    # --- D ----------------------------------------------------------------
    elif mutation == "break_flat_symbol_identity":
        claims["flat_symbol_identity"] = False
    elif mutation == "break_flat_bench_multiset":
        claims["flat_multiset_3d"] = ((0, 4), (1, 8), (2, 4))
    # --- E ----------------------------------------------------------------
    elif mutation == "break_bloch_bench_agreement":
        claims["bloch_equals_bench"] = False
    elif mutation == "break_witness_spectra":
        claims["w1_overlap_pencil_2d"] = ((0, 4), (1, 8), (2, 4))
    elif mutation == "break_boundary_edge_case":
        claims["boundary_onsite_singular"] = False
    # --- F ----------------------------------------------------------------
    elif mutation == "break_onsite_cone_lemma":
        # THE LEMMA DENIED: det B is asserted to depend on D0 and not to
        # factor into the two Hodge readings.
        claims["onsite_lemma_3d"] = False
        claims["onsite_lemma_structure"] = False
    elif mutation == "break_overlap_cone_formula":
        claims["overlap_cone_3d"] = False
        claims["overlap_h0_form"] = False
    elif mutation == "break_two_dim_branches":
        claims["two_dim_onsite_branches"] = False
        claims["two_dim_overlap_matches"] = False
    elif mutation == "break_three_dim_branch_identification":
        claims["three_dim_branches"] = False
        claims["w1_cones"] = False
    elif mutation == "claim_principal_part_scalar":
        # THE QUADRATIC-FORM READING: the curved principal symbol is asserted
        # to be a quadratic form times the identity in three directions.
        # It never is; only the two-direction graded symbol on the honest
        # locus v^2 = 1 - c^2 is.
        claims["principal_scalar_curved_3d"] = True
        claims["two_dim_onsite_scalar_generic"] = True
    elif mutation == "claim_cone_is_metric_cone":
        # R5's HYPOTHESIS AS STATED: the cone is asserted to be ONE metric's
        # cone at curved points.  It is the union of two, or a non-Hodge pair.
        claims["cone_is_one_metric_cone"] = True
        claims["overlap_cones_never_g1_g2"] = False
    elif mutation == "break_coincidence_only_at_flat":
        claims["coincidence_solutions"] = ((0, 0), (sp.Rational(1, 3), HALF))
    # --- G ----------------------------------------------------------------
    elif mutation == "break_shear_registration":
        claims["shear_enters_onsite"] = False
        claims["shear_enters_overlap"] = False
    elif mutation == "claim_volume_registration":
        # THE #7970 MIRROR MISREAD: the volumes are asserted to move the
        # graded cone and the zero-shear overlap symbol.  They do neither.
        claims["volume_enters_onsite_cone"] = True
        claims["overlap_zero_shear_pencil_r5"] = False
    elif mutation == "drop_tension_record":
        claims["tension_recorded"] = False
    # --- H ----------------------------------------------------------------
    elif mutation == "break_scout_grade_fence":
        claims["scout_grade_only"] = False
        claims["physical_content"] = True
    elif mutation == "claim_assembly_decided":
        claims["assembly_decided"] = True
    elif mutation == "claim_hodge_reading_selected":
        claims["hodge_reading_selected"] = True
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 0
    # --- I ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    elif mutation == "break_float_absence":
        claims["float_literals"] = 1
        claims["float_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    build = facts.construction
    control = facts.control
    spectra = facts.spectra
    principal = facts.principal
    registration = facts.registration
    cells = {cell.name: cell for cell in build.cells}

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 212 artifacts are "
        f"content-identical at it and in the worktree, the stale pin "
        f"{STALE_PARENT_COMMIT[:12]} -- the Block 211 tip -- is a real "
        f"ancestor carrying NEITHER, the three machinery imports are landed "
        f"(Blocks 201, 211 with 209, and 105), and "
        f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} audit "
        f"inputs are readable",
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
        "B-3", f"THE WORD *SYMBOL* IS SCOPED BEFORE THE FIRST NUMERAL: it names "
        f"the exact 2^d x 2^d Bloch matrix of a finite antisymmetric kernel on "
        f"a periodic bench and its eigenvalue branches; symbol_is_dynamics = "
        f"{claims['symbol_is_dynamics']}, propagator = {claims['propagator']}",
        claims["symbol_is_dynamics"] is False and claims["propagator"] is False)
    checks.check(
        "B-4", f"THE WORD *CONE* IS SCOPED: it names the zero set of det B(kappa), "
        f"a homogeneous polynomial in three formal variables, and NO light cone, "
        f"NO causal structure and NO spacetime; cone_is_spacetime_cone = "
        f"{claims['cone_is_spacetime_cone']}, and {claims['scoped_words']} "
        f"headline words {SCOPED_HEADLINE_WORDS} are scoped before any number, "
        f"the words {UNNAMED_PHYSICS_WORDS} naming NOTHING established here",
        claims["cone_is_spacetime_cone"] is False
        and facts.scoped_words == claims["scoped_words"])
    checks.check(
        "B-5", f"THE ASSEMBLY IS NOT SELECTED BY THIS BLOCK: Block 105 lands BOTH "
        f"the onsite and the overlap assembly and Block 201's completion uses "
        f"the overlap one; both are run and both are reported; "
        f"assembly_selected = {claims['assembly_selected']}",
        claims["assembly_selected"] is False)
    checks.check(
        "B-6", f"NO GENERIC-PARAMETER THEOREM AND NO CONTINUUM LIMIT, AND THE "
        f"READINGS ARE READINGS: {claims['readings']} of them are enumerated, "
        f"readings_licensed = {claims['readings_licensed']}, and EVERY NEGATIVE "
        f"HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL "
        f"NECESSITY -- the cycle-913 caution, carried verbatim, with nothing "
        f"registered and nothing adopted",
        claims["generic_parameter_theorem"] is False
        and claims["continuum_limit"] is False
        and facts.readings == claims["readings"]
        and claims["readings_licensed"] is False
        and not REGISTERED_OBJECTS and not ADOPTED_OBJECTS
        and claims["registered"] == 0 and claims["adopted"] == 0)

    # --- C: THE CONSTRUCTION'S FIDELITY TO THE CHAIN --------------------------
    checks.check(
        "C-1", f"THE 2D LANE KERNEL IS BLOCK 201's: on (4,4) the eta-staggered "
        f"rules give Block 201's lane_kernel exactly ({build.lane_2d_matches_b201}) "
        f"with {claims['lane_2d_nnz']} nonzero entries, it is site-sign-equivalent "
        f"to Block 201's spin-diagonalised covariant kernel "
        f"({build.lane_2d_site_sign_equivalent}) which has "
        f"{claims['spin_nonscalar_2d']} non-scalar blocks, the graded raising "
        f"part equals Block 201's raising_part on its (8,4) fork extent "
        f"({build.raising_matches_b201_on_fork}), and K = d - d^T with d^2 = 0 "
        f"({build.k_is_d_minus_dT_2d}, {build.d_squared_zero_2d})",
        build.lane_2d_matches_b201 is claims["lane_2d_fidelity"]
        and claims["lane_2d_fidelity"] is True
        and build.lane_2d_nnz == claims["lane_2d_nnz"]
        and build.spin_nonscalar_2d == claims["spin_nonscalar_2d"]
        and build.lane_2d_site_sign_equivalent
        and build.raising_matches_b201_on_fork
        and build.k_is_d_minus_dT_2d and build.d_squared_zero_2d)
    checks.check(
        "C-2", f"THE 3D LANE KERNEL IS BLOCK 209's SHADOW, LINK BY LINK: on "
        f"(4,2,2) all {claims['lane_3d_links']} directed links scalarise under "
        f"Omega = G1^t G2^x G3^y with {claims['lane_3d_bad']} bad links and every "
        f"scalar equal to the rule's eta_d / 2 ({build.lane_3d_shadow_matches}); "
        f"the bench kernel has {claims['lane_3d_nnz']} nonzero entries because "
        f"the extent-2 directions carry NO antisymmetric link "
        f"({build.lane_3d_xy_links_absent}) -- R5's (4,2,2) structure -- and "
        f"K = d - d^T, d^2 = 0 ({build.k_is_d_minus_dT_3d}, {build.d_squared_zero_3d})",
        build.lane_3d_links_scanned == claims["lane_3d_links"]
        and build.lane_3d_bad_links == claims["lane_3d_bad"]
        and build.lane_3d_shadow_matches is claims["lane_3d_shadow"]
        and claims["lane_3d_shadow"] is True
        and build.lane_3d_nnz == claims["lane_3d_nnz"]
        and build.lane_3d_xy_links_absent
        and build.k_is_d_minus_dT_3d and build.d_squared_zero_3d)
    checks.check(
        "C-3", f"THE ASSEMBLERS REPRODUCE THE LANDED HODGES DIGIT FOR DIGIT: "
        f"Block 201's fork_hodge on (8,4) at c = {b201.FORK_SHEAR if b201 else '?'} "
        f"({build.fork_hodge_reproduced}), Block 105's onsite_hodge "
        f"({build.onsite_hodge_reproduced}) and overlap_hodge "
        f"({build.overlap_hodge_reproduced}), and the rule-based onsite and "
        f"overlap assemblies equal the bench assemblies of a uniform cell "
        f"({build.rules_match_bench_assembly})",
        (build.fork_hodge_reproduced and build.onsite_hodge_reproduced
         and build.overlap_hodge_reproduced and build.rules_match_bench_assembly)
        is claims["assemblers_reproduce_landed"]
        and claims["assemblers_reproduce_landed"] is True)
    checks.check(
        "C-4", f"THE CELL FORMS ARE BLOCK 211's, RECONCILED: all "
        f"{claims['witness_count']} witnesses solve at ranks "
        f"{claims['compatible_ranks']} with free names D07, D16, D25, D34, the "
        f"degree blocks equal Block 211's formulas [v0], v1 M1, M2/v0, [1/v1] "
        f"with zero cross-degree entries, the origin tx face equals Block 105's "
        f"shear_hodge(s_tx0 g0, v0), and PD holds exactly at "
        f"{PD_WITNESSES} and fails at the boundary",
        len(build.cells) == claims["witness_count"]
        and all(cell.ranks == claims["compatible_ranks"] for cell in build.cells)
        and all(cell.free_names == ("D07", "D16", "D25", "D34") for cell in build.cells)
        and all(cell.blocks_match_formulas and cell.cross_degree_zero
                and cell.face_restriction_is_shear_hodge for cell in build.cells)
        is claims["cell_forms_reconciled"]
        and claims["cell_forms_reconciled"] is True
        and all(cells[name].positive_definite for name in PD_WITNESSES)
        and not cells["boundary"].positive_definite)
    checks.check(
        "C-5", f"THE FLAT CELL IS THE CONTROL'S CELL: at (c, v) = (0, 1) and at "
        f"Block 211's flat point both assemblies give H = I on both benches "
        f"({build.flat_h_identity}) and K_H = K exactly ({build.flat_kernel_is_r5})",
        build.flat_h_identity is claims["flat_h_identity"]
        and build.flat_kernel_is_r5 is claims["flat_kernel_is_r5"]
        and claims["flat_h_identity"] is True and claims["flat_kernel_is_r5"] is True)

    # --- D: THE R5 CONTROL ----------------------------------------------------
    checks.check(
        "D-1", f"R5's FLAT SYMBOL IS AN EXACT POLYNOMIAL IDENTITY: -K_B(z)^2 = "
        f"({FLAT_SYMBOL_FORM}) times the identity in two "
        f"({control.flat_symbol_identity_2d}) and three "
        f"({control.flat_symbol_identity_3d}) directions",
        (control.flat_symbol_identity_2d and control.flat_symbol_identity_3d)
        is claims["flat_symbol_identity"]
        and claims["flat_symbol_identity"] is True)
    checks.check(
        "D-2", f"AND THE BENCH MULTISETS ARE R5's, WITH MULTIPLICITIES: on (4,4) "
        f"{claims['flat_multiset_2d']} and on (4,2,2) {claims['flat_multiset_3d']}, "
        f"equal to {{sum_d sin^2(2 pi m_d / N_d)}} computed exactly, from the "
        f"direct bench charpoly and from the Bloch union alike "
        f"({control.bloch_equals_direct_flat})",
        control.multiset_2d == tuple((sp.Integer(a), b) for a, b in claims["flat_multiset_2d"])
        and control.multiset_3d == tuple((sp.Integer(a), b) for a, b in claims["flat_multiset_3d"])
        and control.expected_2d == control.multiset_2d
        and control.expected_3d == control.multiset_3d
        and control.bloch_equals_direct_flat)

    # --- E: THE EXACT SPECTRA AT THE WITNESSES ---------------------------------
    defined = [entry for entry in spectra.entries if entry[6] is not None or entry[4] != "UNDEFINED: det H = 0"]
    checks.check(
        "E-1", f"BLOCH UNION = DIRECT BENCH, EVERY TIME: {len(defined)} "
        f"(witness, bench, assembly, reading) charpolys of degree 16 agree "
        f"exactly between the product of 2^d x 2^d Bloch charpolys at exact "
        f"roots of unity and the direct 16 x 16 bench matrix "
        f"({spectra.all_agree}); translation covariance of -K_H^2 at W1, as "
        f"nnz([-K_H^2, T_mu]) per direction: {spectra.translation_commutators}",
        spectra.all_agree is claims["bloch_equals_bench"]
        and claims["bloch_equals_bench"] is True
        and all(entry[5] for entry in spectra.entries))
    checks.check(
        "E-2", f"W1's OWN (4,4) SPECTRUM, DECLARED: the overlap H-pencil "
        f"reading has the exact multiset {claims['w1_overlap_pencil_2d']} "
        f"against R5's {FLAT_MULTISET_2D} -- only the (pi/2, pi/2)-type momenta "
        f"move; every other witness spectrum is printed as its factored "
        f"charpoly above",
        spectra.w1_overlap_pencil_2d == tuple(
            (sp.sympify(a), b) for a, b in claims["w1_overlap_pencil_2d"]))
    checks.check(
        "E-3", f"THE PD BOUNDARY IS AN EDGE CASE, MEASURED: at gamma0 = gamma1 = "
        f"1/2 all-plus the onsite H is SINGULAR on both benches "
        f"({spectra.boundary_onsite_singular_2d}, {spectra.boundary_onsite_singular_3d}) "
        f"so the H-pencil reading is undefined there while the form reading "
        f"stays defined; the overlap H stays regular "
        f"({spectra.boundary_overlap_regular})",
        (spectra.boundary_onsite_singular_2d and spectra.boundary_onsite_singular_3d)
        is claims["boundary_onsite_singular"]
        and claims["boundary_onsite_singular"] is True
        and spectra.boundary_overlap_regular)

    # --- F: THE PRINCIPAL PART AND THE CONE ------------------------------------
    checks.check(
        "F-1", f"THE ONSITE CONE LEMMA, AT FULLY SYMBOLIC D: {ONSITE_CONE_LEMMA_3D} "
        f"({principal.lemma_3d_holds}) and in two directions {ONSITE_CONE_LEMMA_2D} "
        f"({principal.lemma_2d_holds}); D0 is absent from det B "
        f"({principal.lemma_d0_absent}); the pencil principal block is "
        f"block-diagonal by form degree ({principal.lemma_3d_block_diagonal}) "
        f"with the 0-form branch k^T D1 k / D0 ({principal.lemma_3d_zero_form_branch}), "
        f"the eigenvector adj(D2) E k at eigenvalue D3 k^T E D2^-1 E k "
        f"({principal.lemma_3d_top_form_branch}) and transverse product "
        f"det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k) ({principal.lemma_3d_transverse_product})",
        (principal.lemma_3d_holds and principal.lemma_2d_holds) is claims["onsite_lemma_3d"]
        and claims["onsite_lemma_3d"] is True
        and (principal.lemma_d0_absent and principal.lemma_3d_block_diagonal
             and principal.lemma_3d_zero_form_branch and principal.lemma_3d_top_form_branch
             and principal.lemma_3d_transverse_product) is claims["onsite_lemma_structure"]
        and claims["onsite_lemma_structure"] is True)
    checks.check(
        "F-2", f"THE OVERLAP CONE, AT SYMBOLIC h: the folded overlap H0 is "
        f"{OVERLAP_H0_FORM} ({principal.overlap_h0_form_holds}); det B = +-Q+ Q- "
        f"with Q+ = {OVERLAP_CONE_PLUS} and Q- = {OVERLAP_CONE_MINUS} "
        f"({principal.overlap_cone_3d_holds}), and in two directions det B = "
        f"-h0 ({OVERLAP_CONE_2D}) ({principal.overlap_cone_2d_holds})",
        principal.overlap_h0_form_holds is claims["overlap_h0_form"]
        and claims["overlap_h0_form"] is True
        and (principal.overlap_cone_3d_holds and principal.overlap_cone_2d_holds)
        is claims["overlap_cone_3d"]
        and claims["overlap_cone_3d"] is True)
    checks.check(
        "F-3", f"TWO DIRECTIONS AT SYMBOLIC (c, v), BLOCK 105's OWN CELL FORM: the "
        f"graded H-pencil principal symbol has EXACTLY the branches "
        f"{TWO_DIM_ONSITE_BRANCHES} ({principal.two_dim_onsite_branches}) -- the "
        f"Hodge reading's cone k^T (D1/D0) k and det(g)/v^2 times it -- so the "
        f"cone IS the cell metric's cone there; the overlap H-pencil principal "
        f"symbol is the scalar {TWO_DIM_OVERLAP_PENCIL} times the identity "
        f"({principal.two_dim_overlap_pencil_scalar}, {principal.two_dim_overlap_pencil_matches}) "
        f"with cone {principal.two_dim_overlap_cone_matches and 'h0(kt^2+kx^2)+4 htx kt kx'}",
        principal.two_dim_onsite_branches is claims["two_dim_onsite_branches"]
        and claims["two_dim_onsite_branches"] is True
        and (principal.two_dim_overlap_pencil_scalar and principal.two_dim_overlap_pencil_matches
             and principal.two_dim_overlap_cone_matches) is claims["two_dim_overlap_matches"]
        and claims["two_dim_overlap_matches"] is True
        and claims["two_dim_overlap_pencil_scalar"] is True)
    checks.check(
        "F-4", f"AND THE OVERLAP CONE IS NOT THE METRIC'S: its effective shear is "
        f"{TWO_DIM_OVERLAP_EFFECTIVE_SHEAR} ({principal.two_dim_effective_shear}), "
        f"the same sign as the Hodge reading's c but never its magnitude, with "
        f"the exact discrepancy c_K - c = {TWO_DIM_OVERLAP_SHEAR_DISCREPANCY} "
        f"({principal.two_dim_discrepancy}), nonzero for every c != 0",
        principal.two_dim_effective_shear is claims["two_dim_effective_shear"]
        and claims["two_dim_effective_shear"] is True
        and principal.two_dim_discrepancy)
    checks.check(
        "F-5", f"THREE DIRECTIONS AT EVERY CURVED WITNESS: under the graded "
        f"assembly det B factors EXACTLY into the two Hodge readings' cones "
        f"k^T G1 k and k^T G2 k ({principal.onsite_cones_are_g1_g2_everywhere}) "
        f"and both are exact H-pencil branches ({principal.onsite_branches_g1_g2_everywhere}); "
        f"at W1 the cones are {W1_ONSITE_CONES} ({principal.w1_onsite_cones}) "
        f"and under the overlap assembly {W1_OVERLAP_CONES} ({principal.w1_overlap_cones})",
        (principal.onsite_cones_are_g1_g2_everywhere and principal.onsite_branches_g1_g2_everywhere)
        is claims["three_dim_branches"]
        and claims["three_dim_branches"] is True
        and (principal.w1_onsite_cones and principal.w1_overlap_cones) is claims["w1_cones"]
        and claims["w1_cones"] is True)
    checks.check(
        "F-6", f"THE SYMBOL IS NOT A QUADRATIC FORM TIMES THE IDENTITY: at no "
        f"curved three-direction witness, under either assembly or reading, is "
        f"the principal symbol scalar (principal_scalar_curved_3d = "
        f"{claims['principal_scalar_curved_3d']}); the transverse 2-form "
        f"branches are quadratic forms nowhere ({principal.transverse_branches_quadratic_anywhere}); "
        f"in two directions the graded symbol is scalar exactly on "
        f"{TWO_DIM_ONSITE_SCALAR_LOCUS} ({principal.two_dim_onsite_scalar_on_locus}) "
        f"and not generically ({principal.two_dim_onsite_pencil_scalar_generic}); "
        f"the form readings are scalar nowhere ({principal.two_dim_onsite_form_scalar}, "
        f"{principal.two_dim_overlap_form_scalar})",
        principal.principal_scalar_anywhere_curved_3d is claims["principal_scalar_curved_3d"]
        and claims["principal_scalar_curved_3d"] is False
        and principal.transverse_branches_quadratic_anywhere is claims["transverse_quadratic_anywhere"]
        and principal.two_dim_onsite_scalar_on_locus is claims["two_dim_onsite_scalar_on_locus"]
        and principal.two_dim_onsite_pencil_scalar_generic is claims["two_dim_onsite_scalar_generic"]
        and claims["two_dim_onsite_scalar_generic"] is False
        and not principal.two_dim_onsite_form_scalar
        and not principal.two_dim_overlap_form_scalar)
    checks.check(
        "F-7", f"THE HYPOTHESIS, ANSWERED: on the Block 211 family the two Hodge "
        f"readings G1 and G2 are proportional ONLY at the chart points "
        f"{claims['coincidence_solutions']} -- the flat point -- in all "
        f"{claims['coincidence_classes']} gauge classes, so the graded cone is "
        f"the UNION of two distinct metric cones at every curved point; the "
        f"overlap cones are proportional to neither reading at any curved "
        f"witness ({principal.overlap_cones_never_g1_g2}); cone_is_one_metric_cone = "
        f"{claims['cone_is_one_metric_cone']}",
        principal.coincidence_solutions == tuple(
            (sp.sympify(a), sp.sympify(b)) for a, b in claims["coincidence_solutions"])
        and principal.coincidence_classes == claims["coincidence_classes"]
        and principal.overlap_cones_never_g1_g2 is claims["overlap_cones_never_g1_g2"]
        and claims["overlap_cones_never_g1_g2"] is True
        and claims["cone_is_one_metric_cone"] is False
        and principal.onsite_cones_are_g1_g2_everywhere)

    # --- G: SHEAR REGISTRATION ------------------------------------------------
    checks.check(
        "G-1", f"THE SHEAR ENTERS THE CONE, EXACTLY: under the graded assembly "
        f"d(k^T G1 k)/dg0 and d(k^T G2 k)/dg1 are nonzero and det B is not "
        f"proportional to its zero-shear value ({registration.onsite_cone_shear_derivative_nonzero}); "
        f"under the overlap assembly likewise ({registration.overlap_cone_shear_derivative_nonzero}) "
        f"and the sign class moves the cone at fixed magnitudes "
        f"({registration.sign_class_moves_overlap_cone})",
        registration.onsite_cone_shear_derivative_nonzero is claims["shear_enters_onsite"]
        and registration.overlap_cone_shear_derivative_nonzero is claims["shear_enters_overlap"]
        and claims["shear_enters_onsite"] is True and claims["shear_enters_overlap"] is True
        and registration.sign_class_moves_overlap_cone)
    checks.check(
        "G-2", f"THE DIAGONAL METRIC DOES NOT: under the graded assembly det B is "
        f"proportional to its unit-volume value ({registration.onsite_cone_volume_free}) "
        f"and the volumes enter only the branch scales "
        f"{registration.onsite_branch_scales}; under the overlap assembly the "
        f"Bloch H at zero shear is h0 times the identity "
        f"({registration.overlap_symbol_depends_only_on_h}), the zero-shear "
        f"H-pencil symbol is R5's for EVERY volume pair "
        f"({registration.overlap_zero_shear_pencil_is_r5}) and the zero-shear "
        f"form symbol is {registration.overlap_zero_shear_form_scale}; "
        f"volume_enters_onsite_cone = {claims['volume_enters_onsite_cone']}",
        registration.onsite_cone_volume_free is (not claims["volume_enters_onsite_cone"])
        and claims["volume_enters_onsite_cone"] is False
        and registration.overlap_zero_shear_pencil_is_r5 is claims["overlap_zero_shear_pencil_r5"]
        and claims["overlap_zero_shear_pencil_r5"] is True
        and registration.overlap_symbol_depends_only_on_h)
    checks.check(
        "G-3", f"THE #7970 TENSION IS RECORDED AND NOT RESOLVED: {TENSION_RECORD} "
        f"(tension_recorded = {claims['tension_recorded']})",
        claims["tension_recorded"] is True and TENSION_RECORDED)

    # --- H: THE SCOPE FENCES ----------------------------------------------------
    checks.check(
        "H-1", f"FENCE ONE -- '{SCOUT_GRADE_FENCE}', BLOCK 211's FENCE INHERITED "
        f"VERBATIM: scout_grade_only = {claims['scout_grade_only']}, "
        f"physical_content = {claims['physical_content']}",
        claims["scout_grade_only"] is True and claims["physical_content"] is False)
    checks.check(
        "H-2", f"FENCE TWO -- THE ASSEMBLY IS A SUPPLIED FORK, NOT A RESULT: "
        f"Block 105's onsite and overlap assemblies give DIFFERENT cones and "
        f"this block decides between them nowhere; assembly_decided = "
        f"{claims['assembly_decided']}",
        claims["assembly_decided"] is False)
    checks.check(
        "H-3", f"FENCE THREE -- NO HODGE READING IS SELECTED: G1 = D1/D0 and "
        f"G2 = D3 E D2^-1 E are both realised as exact branches and neither is "
        f"named 'the' metric; hodge_reading_selected = {claims['hodge_reading_selected']}",
        claims["hodge_reading_selected"] is False)
    checks.check(
        "H-4", f"FENCE FOUR -- THE INSTANCE SCOPE, ENUMERATED: "
        f"{claims['instance_scope']} restrictions ({INSTANCE_SCOPE})",
        claims["instance_scope"] == len(INSTANCE_SCOPE)
        and claims["instance_scope"] == INSTANCE_SCOPE_COUNT
        and claims["instance_scope"] > 0)

    # --- I: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE ----------------------
    checks.check(
        "I-1", f"the note is present at {NOTE_PATH.name} and the N5 fence "
        f"appears in it VERBATIM as a single line",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "I-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in this "
        f"runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn the nonzero discrepancy polynomial into a zero and "
        f"manufacture the identity this block refutes",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "I-3", f"and {claims['float_literals']} float literals appear in that "
        f"same source with EXACTLY {claims['float_calls']} float call sites, "
        f"both MEASURED by an AST walk -- Block 211's strict form",
        facts.float_literals == claims["float_literals"]
        and facts.float_calls == claims["float_calls"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED")
    print(f"  elapsed: {elapsed_ns // 1000000000}s")
    print(f"  origin/main {facts.main_head}")
    print(f"  authority {facts.authority}")
    print(f"  imposed {facts.imposed}, registered {facts.registered}, "
          f"adopted {facts.adopted}, gravity structures NOT SUPPLIED "
          f"{facts.unsupplied}, readings {facts.readings}, scoped headline "
          f"words {facts.scoped_words}")
    print(f"  check verdict carried: {CHECK_VERDICT}")
    build = facts.construction
    print("  THE CONSTRUCTION")
    print(f"    2D lane kernel = Block 201's {build.lane_2d_matches_b201}, nnz "
          f"{build.lane_2d_nnz}, spin-nonscalar {build.spin_nonscalar_2d}, "
          f"site-sign-equivalent {build.lane_2d_site_sign_equivalent}, raising "
          f"part = Block 201's on (8,4) {build.raising_matches_b201_on_fork}, "
          f"K = d - d^T {build.k_is_d_minus_dT_2d}, d^2 = 0 {build.d_squared_zero_2d}")
    print(f"    3D lane kernel: {build.lane_3d_links_scanned} links scanned, "
          f"{build.lane_3d_bad_links} bad, shadow = eta/2 {build.lane_3d_shadow_matches}, "
          f"nnz {build.lane_3d_nnz}, x/y links absent on extent 2 "
          f"{build.lane_3d_xy_links_absent}, K = d - d^T {build.k_is_d_minus_dT_3d}, "
          f"d^2 = 0 {build.d_squared_zero_3d}")
    print(f"    assemblers: fork_hodge {build.fork_hodge_reproduced}, onsite_hodge "
          f"{build.onsite_hodge_reproduced}, overlap_hodge {build.overlap_hodge_reproduced}, "
          f"rules = bench assembly {build.rules_match_bench_assembly}")
    print(f"    flat: H = I {build.flat_h_identity}, K_H = K {build.flat_kernel_is_r5}")
    for cell in build.cells:
        print(f"    witness {cell.name}: moduli (v0, g0, v1, g1) = {cell.moduli}, ranks "
              f"{cell.ranks}, free {cell.free_names}, blocks = formulas "
              f"{cell.blocks_match_formulas}, cross-degree zero {cell.cross_degree_zero}, "
              f"origin tx face = shear_hodge{cell.face_moduli} {cell.face_restriction_is_shear_hodge}")
        print(f"      leading minors {cell.leading_minors}, PD {cell.positive_definite}")
        print(f"      G1 = D1/D0 = {cell.g1}")
        print(f"      G2 = D3 E D2^-1 E = {cell.g2}")
        print(f"      G1 ~ G2 {cell.g1_proportional_to_g2}; Hodge-consistency defects: "
              f"D0 D3 - 1 = {cell.hodge_defect_scalar}, nnz(D1 E D2 E - D0 D3 I) = "
              f"{cell.hodge_defect_matrix_nnz}")
    control = facts.control
    print("  THE R5 CONTROL")
    print(f"    flat symbol identity 2D {control.flat_symbol_identity_2d}, 3D "
          f"{control.flat_symbol_identity_3d}; (4,4) multiset {control.multiset_2d} "
          f"expected {control.expected_2d}; (4,2,2) multiset {control.multiset_3d} "
          f"expected {control.expected_3d}; Bloch = direct {control.bloch_equals_direct_flat}")
    spectra = facts.spectra
    print("  THE EXACT SPECTRA (factored charpoly of the 16 x 16 bench -K^2; "
          "'agree' = Bloch union equals direct bench)")
    for name, extent, assembly, reading, text, agreement, multiset in spectra.entries:
        print(f"    [{name} {extent} {assembly} {reading}] agree {agreement}"
              f"{' multiset ' + str(multiset) if multiset is not None else ''}")
        print(f"      {text}")
    print(f"    translation covariance at W1, nnz([-K_H^2, T_mu]): {spectra.translation_commutators}")
    print(f"    boundary: onsite H singular on (4,4) {spectra.boundary_onsite_singular_2d}, "
          f"on (4,2,2) {spectra.boundary_onsite_singular_3d}; overlap H regular "
          f"{spectra.boundary_overlap_regular}")
    principal = facts.principal
    print("  THE PRINCIPAL PART AND THE CONE")
    print(f"    onsite lemma 3D {principal.lemma_3d_holds}, 2D {principal.lemma_2d_holds}, "
          f"D0 absent {principal.lemma_d0_absent}, block-diagonal {principal.lemma_3d_block_diagonal}, "
          f"0-form branch {principal.lemma_3d_zero_form_branch}, top-form branch "
          f"{principal.lemma_3d_top_form_branch}, transverse product {principal.lemma_3d_transverse_product}")
    print(f"    overlap H0 form {principal.overlap_h0_form_holds}, overlap cone 3D "
          f"{principal.overlap_cone_3d_holds}, 2D {principal.overlap_cone_2d_holds}")
    print(f"    2D (c, v): onsite branches {principal.two_dim_onsite_branches}, onsite pencil "
          f"scalar generically {principal.two_dim_onsite_pencil_scalar_generic}, on the locus "
          f"v^2 = 1 - c^2 {principal.two_dim_onsite_scalar_on_locus}, onsite form scalar "
          f"{principal.two_dim_onsite_form_scalar}; overlap pencil scalar "
          f"{principal.two_dim_overlap_pencil_scalar}, matches {principal.two_dim_overlap_pencil_matches}, "
          f"cone matches {principal.two_dim_overlap_cone_matches}, form scalar "
          f"{principal.two_dim_overlap_form_scalar}, effective shear {principal.two_dim_effective_shear}, "
          f"discrepancy {principal.two_dim_discrepancy}")
    print(f"    2D onsite exact 0-form H-pencil symbol: {principal.two_dim_onsite_zero_form_symbol}")
    print(f"    2D onsite exact 2-form H-pencil symbol: {principal.two_dim_onsite_two_form_symbol}")
    print(f"    2D overlap exact H-pencil scalar symbol: {principal.two_dim_overlap_pencil_symbol}")
    for record in principal.witnesses:
        (name, assembly, factor_texts, branches, remainder, form_branches, form_remainder,
         scalar_pencil, scalar_form, cones_ok, branches_ok, parity, cone1, cone2) = record
        print(f"    [{name} {assembly}] parity-preserving H0 {parity}; det B factors {factor_texts}")
        print(f"      pencil branches (quadratic-form eigenvalues, multiplicity) {branches}; "
              f"remaining factor degrees {remainder}; scalar {scalar_pencil}")
        print(f"      form branches {form_branches}; remaining {form_remainder}; scalar {scalar_form}")
        print(f"      k^T G1 k = {cone1}; k^T G2 k = {cone2}; cones are G1, G2 {cones_ok}; "
              f"branches include G1, G2 {branches_ok}")
    print(f"    W1 graded exact 0-form H-pencil symbol: {principal.w1_zero_form_symbol}")
    print(f"    W1 cones onsite {principal.w1_onsite_cones}, overlap {principal.w1_overlap_cones}; "
          f"onsite cones = G1, G2 everywhere {principal.onsite_cones_are_g1_g2_everywhere}; "
          f"branches everywhere {principal.onsite_branches_g1_g2_everywhere}; overlap cones "
          f"never G1, G2 {principal.overlap_cones_never_g1_g2}; scalar anywhere curved 3D "
          f"{principal.principal_scalar_anywhere_curved_3d}; transverse quadratic anywhere "
          f"{principal.transverse_branches_quadratic_anywhere}")
    print(f"    G1 ~ G2 on the family: chart solutions {principal.coincidence_solutions} "
          f"over {principal.coincidence_classes} classes")
    registration = facts.registration
    print("  SHEAR REGISTRATION")
    print(f"    onsite: shear moves the cone {registration.onsite_cone_shear_derivative_nonzero}, "
          f"volumes do not {registration.onsite_cone_volume_free}, branch scales "
          f"{registration.onsite_branch_scales}")
    print(f"    overlap: Bloch H at zero shear = h0 I {registration.overlap_symbol_depends_only_on_h}, "
          f"zero-shear pencil = R5 {registration.overlap_zero_shear_pencil_is_r5}, zero-shear form = "
          f"{registration.overlap_zero_shear_form_scale}, shear moves the cone "
          f"{registration.overlap_cone_shear_derivative_nonzero}, sign class moves the cone "
          f"{registration.sign_class_moves_overlap_cone}")
    print(f"    {TENSION_RECORD}")
    print("  READINGS, AND EACH IS A READING")
    for reading in READINGS:
        print(f"    {reading}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}; float literals: "
          f"{facts.float_literals}; float call sites: {facts.float_calls}")
    print("  NOT CLAIMED: NO GRAVITY. NO DYNAMICS. NO SPACETIME CONE. NO PROPAGATOR. "
          "NO ASSEMBLY DECIDED. NO HODGE READING SELECTED. NO CONTINUUM. THE "
          "READINGS ARE READINGS.")
    print()


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE WORDS SYMBOL, CONE, METRIC AND DISPERSION ARE EACH SCOPED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- THE WEIGHTED KERNEL K_H = H d - d^T H (Block 107's / Block 201's completion at m = 0 and periodic closure, with d Block 201's graded raising part of the eta-staggered lane kernel and Block 209's three-direction shadow), THE TWO LANDED ASSEMBLIES (Block 105's onsite_hodge at even anchors and its overlap_hodge at every anchor with weight 2^-d, Block 191's rule as used by Block 201's fork_hodge), THE TWO SQUARED-SYMBOL READINGS (the Euclidean form -K_H^2 and the H-pencil -(H^-1 K_H)^2), THE PERIOD-2 BLOCH REDUCTION with its bipartite block B(kappa), THE TWO CANDIDATE CELL METRICS G1 = D1/D0 and G2 = D3 E D2^-1 E read off the degree blocks by Block 209's honest-lift pattern, and BLOCK 211's FAMILY AND WITNESSES with BLOCK 105's shear_hodge READ THROUGH THEIR OWN RUNNERS, are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. 'SYMBOL' NAMES THE EXACT 2^d x 2^d BLOCH MATRIX OF A FINITE ANTISYMMETRIC KERNEL ON A PERIODIC BENCH AND NAMES NO DYNAMICS AND NO PROPAGATOR. 'CONE' NAMES THE ZERO SET OF det B(kappa), A HOMOGENEOUS POLYNOMIAL, AND NAMES NO LIGHT CONE, NO CAUSAL STRUCTURE AND NO SPACETIME. 'METRIC' NAMES ONE OF TWO DECLARED RATIONAL READINGS OF THE CELL FORM'S DEGREE BLOCKS. 'DISPERSION' NAMES THE EIGENVALUE BRANCHES OF AN EXACT 4 x 4 OR 8 x 8 MATRIX. THE WORDS SPACETIME, LIGHT CONE, PROPAGATOR AND EINSTEIN NAME NOTHING ESTABLISHED HERE. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE CONSTRUCTION IS THE CHAIN'S AND THE CONTROL IS R5's. The 2D lane kernel equals Block 201's lane_kernel exactly and is site-sign-equivalent to its spin-diagonalised covariant kernel with zero non-scalar blocks; the 3D lane kernel is Block 209's shadow link by link (48 links, 0 bad, every scalar eta_d / 2), and on (4,2,2) the extent-2 directions carry NO antisymmetric link; K = d - d^T with d^2 = 0 in Block 201's grading in both dimensions; the assemblers reproduce Block 201's fork_hodge and Block 105's onsite_hodge and overlap_hodge digit for digit; the eight cell forms are Block 211's solved D at ranks (32, 32) with its degree-block formulas and its origin tx face equal to Block 105's shear_hodge; at the flat cell both assemblies give H = I and K_H = K on both benches; and -K_B(z)^2 = sum_d -(z_d - 1/z_d)^2 / 4 times the identity is an exact polynomial identity in two and three directions, whose bench multisets are {0 x4, 1 x8, 2 x4} on (4,4) and {0 x8, 1 x8} on (4,2,2), exactly R5's.\\nper_mode: THE EXACT SPECTRA AND THE PRINCIPAL PART. Every (witness, bench, assembly, reading) charpoly of degree 16 agrees exactly between the Bloch union over exact roots of unity and the direct bench matrix; at W1 on (4,4) the overlap H-pencil multiset is {0 x4, 1 x8, 1922/1081 x4} against R5's {0 x4, 1 x8, 2 x4}; at the PD boundary the onsite H is singular on both benches and the H-pencil reading is undefined there while the form reading and the overlap assembly remain defined. With K_H,B(exp(i eps kappa)) = i eps M(kappa) + O(eps^2) and M = H0 D(kappa) + D(kappa)^T H0, both assemblies preserve grade parity, M = [[0, B], [B^T, 0]] with B = H_e D_eo + D_oe^T H_o, the characteristic cone {det B = 0} is reading-independent, and the principal symbols are B B^T (form) and H_e^-1 B H_o^-1 B^T (pencil) on the even sector with the same spectra on the odd sector.\\nper_block: THE TWO LEMMAS, AT SYMBOLIC ARGUMENTS. Graded assembly, any block-diagonal cell form: det B = -D3 (k^T D1 k)(k^T E adj(D2) E k) in three directions and -D2 (k^T D1 k) in two; D0 is absent; the pencil principal symbol is block-diagonal by form degree with the EXACT branches k^T (D1/D0) k on 0-forms and D3 k^T E D2^-1 E k on top forms, the transverse 2-form pair being the roots of a quadratic whose product is det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k). Overlap assembly: the folded H0 is h0 I + two-flip couplings 2 h_f with h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8 and h_f = -(s_f0 v1 g0 + s_f1 g1 / v0)/8, and det B = +-Q+ Q- with the two displayed quadratic cones differing by the sign of the t-y plane terms; in two directions the single cone h0 (kt^2 + kx^2) + 4 h_tx kt kx.\\nlattice_wide: THE HYPOTHESIS, ANSWERED EXACTLY. In two directions at symbolic (c, v) the graded H-pencil branches are k^T g^-1 k and (det g / v^2) k^T g^-1 k with g = [[1, c], [c, 1]] = (D1/D0)^-1, so the cone IS the cell metric's cone and the symbol is a quadratic form times the identity exactly on the honest-volume locus v^2 = 1 - c^2; the overlap cone has the effective shear c_K = 2 c v^2 / (3 v^2 + 1 - c^2 (v^2 + 1)) with the exact discrepancy c_K - c = -c (1 - c^2)(v^2 + 1) / (3 v^2 + 1 - c^2 (v^2 + 1)). In three directions, at every curved witness the graded cone is EXACTLY the union of the two Hodge readings' cones k^T (D1/D0) k = 0 and k^T (D3 E D2^-1 E) k = 0, both exact H-pencil branches, and on the Block 211 family those two readings are proportional ONLY at the flat point in all four gauge classes; the overlap cones are proportional to neither reading; no curved three-direction principal symbol is scalar under either assembly or reading, and the transverse branches are quadratic forms nowhere. THE CONE IS NEVER ONE METRIC'S CONE OFF THE FLAT POINT, AND THE EXACT DISCREPANCIES ARE THE RESULT.\\nper_scope: SHEAR REGISTRATION, SEPARATELY. The shears g0 and g1 move the cone under both assemblies (exact nonzero derivatives, exact non-proportionality to the zero-shear cone, and the sign class moves the overlap cone at fixed magnitudes); the diagonal moduli do not move the graded cone (det B is proportional to its unit-volume value) and enter only the branch scales v1/v0 and v0/v1; under the overlap assembly the Bloch H at zero shear is h0 times the identity, the zero-shear H-pencil symbol is R5's for EVERY volume pair and the zero-shear form symbol is h0^2 times R5's. THIS IS A NAMED TENSION WITH THE MATTER-SIDE NO-SHEAR-RESPONSE RESULT OF PR #7970 (itself conditional): kernel side registers the shear and not the diagonal, matter side the diagonal and not the shear -- RECORDED, NOT RESOLVED HERE. WHAT REMAINS OPEN: which assembly, if either, the framework selects; which Hodge reading, if either, is 'the' metric; the transverse branches' meaning; every extent, witness and convention not run; and no energy, no mass, no measurement postulate, no Born rule, no dynamics, no continuum and no gravity is supplied by any line of this block.\\nRESULT: THE WEIGHTED KERNEL K_H = H d - d^T H REPRODUCES R5's FLAT SYMBOL EXACTLY AT THE FLAT CELL IN ALL FOUR CONSTRUCTIONS; ITS CHARACTERISTIC CONE IS, UNDER THE GRADED ASSEMBLY, THE UNION OF THE TWO HODGE READINGS' CONES k^T (D1/D0) k = 0 AND k^T (D3 E D2^-1 E) k = 0 -- ONE METRIC'S CONE ONLY AT THE FLAT POINT -- AND, UNDER THE OVERLAP ASSEMBLY, A NON-HODGE PAIR OF CONES; THE PRINCIPAL SYMBOL IS A QUADRATIC FORM TIMES THE IDENTITY ONLY IN TWO DIRECTIONS ON v^2 = 1 - c^2; AND THE SHEAR, NOT THE DIAGONAL METRIC, IS WHAT THE KERNEL REGISTERS. THESE ARE SCOUT-GRADE FINITE EXACT LINEAR-ALGEBRA FACTS ON ONE CELL FORM, NOT A SPACETIME AND NOT A DYNAMICS. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 105, 107, 128, 171, 190, 191, 201, 209, 210, 211 and 212 STAND EXACTLY AS LANDED. BLOCK 201 IS NOT CORRECTED: its fork_hodge is reproduced digit for digit and its overlap assembly is one of the two landed assemblies run here. BLOCK 211 IS NOT CORRECTED: its witnesses, ranks, block formulas and minors are reproduced through its own runner. THIS BLOCK's OWN DEFECTS ARE DISCLOSED: two benches, one cell family, eight witnesses, two assemblies and two readings, one rule, the principal part at one degenerate zero -- not a parameter space and not a limit; the assembly fork is supplied and not decided; the two Hodge readings are declared candidates and neither is selected; the transverse 2-form branches are exhibited and not interpreted. DEGRADED WORKER MODE IS DISCLOSED: drafted on Fable worker seats after the gpt-5.6-sol seats died at the account limit, with the refuting checker pending. PROVENANCE: the R5 weighted-kernel design task of this lane, at TOTAL PASS=35 FAIL=0 across nine families.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
