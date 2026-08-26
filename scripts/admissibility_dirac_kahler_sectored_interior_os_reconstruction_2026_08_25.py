#!/usr/bin/env python3
"""BLOCK 195 -- THE SECTORED INTERIOR OS RECONSTRUCTION: ON AN INTERIOR WINDOW
THE TWO-SLICE SHIFT DESCENDS TO THE EIGHT-DIMENSIONAL OS QUOTIENT, AND ON ONE OF
ITS TWO MOMENTUM SECTORS IT IS A POSITIVE SELF-ADJOINT OPERATOR.

THE RESULT, AND ITS EXACT SCOPE.  Block 190's wrap-edge width family is carried
at T = 16 AND T = 20, at the fixture (m, c) = (9/20, 5/13) and at the second
rational point (1/2, 1/3).  The question this block answers is the one Blocks
190 to 194 left open: does the two-slice evolution DESCEND to the OS quotient
H = X_A / rad(K_AA) as a well-defined, OS-self-adjoint, positive operator?  The
answer is SECTORED, and both halves are the result:

  (i) IT DESCENDS -- BUT NOT FROM EVERY PRESENTATION.  On the SEAM-ANCHORED
      PREFIX domains D = {1..dmax} the invariant obstruction rank is 2, 1, 1 at
      both widths, so no representative-independent operator exists from those
      presentations.  On the INTERIOR windows D = {2, 3, 4} at T = 16 and
      D = {2..6} at T = 20 the obstruction rank is EXACTLY ZERO on kernels of
      dimension 4 and 12, and rank(K_AD) = 8, so the window surjects onto all
      of H and T_2 = q_A tau^2 q_D^-1 is a genuine operator on the quotient.

 (ii) AND IT SPLITS.  The momentum involution U is an exact isometry of the
      quotient Gram, commutes with T_2, and splits H orthogonally into a LIGHT
      sector U = +1 and a HEAVY sector U = -1.  On the LIGHT sector the shifted
      form is EXACTLY SYMMETRIC and both forms are positive-definite, so T_+ is
      a POSITIVE SELF-ADJOINT OPERATOR with spectrum the doubly degenerate pair
      e^{+/- theta_light}.  On the HEAVY sector the antisymmetric defect has
      EXACT RANK 2 and T_- is NOT self-adjoint in the OS form.  The complete
      defect is rank 2 with spectral-projector ranks (0, 2, 0, 0): entirely
      heavy, zero on the light sector and zero on both cross blocks.

THAT SPLIT IS THE THEOREM.  ALL OF IT IS FINITE EXACT LINEAR ALGEBRA OVER QQ ON
ONE CONSTRUCTED MATRIX FAMILY.  NONE OF IT SUPPLIES GRAVITY, A SEMIGROUP, A
GENERATOR, A HAMILTONIAN, A CONTINUUM TIME OR A CONTINUUM LIMIT.  'HILBERT
SPACE', 'EVOLUTION', 'SELF-ADJOINT', 'POSITIVE' AND 'MASS' NAME PROPERTIES OF
EXACT RATIONAL MATRICES AND OF NOTHING ELSE, AND THEY ARE FENCED BEFORE THE
FIRST NUMBER IS READ.

  0. H EXISTS (C).  The reflected Gram of the full positive span is exactly
     symmetric of exact rank 8 at both widths and both points, and it is
     POSITIVE SEMIDEFINITE of rank 8 rather than merely symmetric of rank 8 --
     certified with NO floating inertia call by an eight-column frame with
     eight positive leading minors plus an exact zero Schur residual and the
     four exact projector identities.

  1. THE PREFIX OBSTRUCTION AND THE INTERIOR LOOPHOLE (D).  The invariant
     obstruction ranks on the prefix presentations are 2, 1, 1 at both widths
     and the residual support meets every positive slice; the solve's counts of
     violating kernel vectors are PRESENTATION-DEPENDENT and are corrected here
     by an explicit THREE-PRESENTATION construction on the same kernel --
     default 8, 6, 2 and 14, 12, 8; adapted exactly rank many, 2, 1, 1;
     all-violating exactly nullity many, 12, 8, 4 and 20, 16, 12.  The interior
     windows carry obstruction rank 0.

  2. THE DESCENT (E).  The quotient is eight-dimensional, K_c is symmetric with
     eight positive leading minors, the symmetric part of the shifted form is
     positive-definite, charpoly(T_2) is the LANDED Block 194 pair of primitive
     palindromic quadratics squared -- carried with Block 194's own MONIC
     NORMALIZATION formula s = (a_light a_heavy)^2 -- and in the deep pair-core
     section the descended operator IS Block 190's W.

  3. THE SECTOR THEOREM (F).  The light sector: defect 0, both forms PD, T_+
     self-adjoint and positive.  The heavy sector: defect rank 2, symmetric part
     PD, T_- not self-adjoint.  Basis independence is gated as congruence and
     similarity on two declared alternative sections.  The round-2 fence is
     gated too: the defect is U-equivariant but does NOT purely pair the two
     momentum-degenerate copies.

  4. GENERALITY (G).  Every structural statement above persists at (1/2, 1/3)
     at both widths while the polynomials change -- structure of the class,
     coefficients of the point.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY.  NO FULL
RECONSTRUCTION: the heavy sector's defect is rank two and is not removed, and
this block says so first.  NO SEMIGROUP AND NO GENERATOR: one fixed 8 x 8
matrix is not a dynamics.  NO PHYSICAL MASS.  NO DEGENERATE-COPY PAIRING: the
stronger reading of the defect is REFUTED and the refutation is gated.  NO
CONTINUUM: two widths are not a limit.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 194 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: seven imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, a COMPLETE reconstruction, a licensed heavy
     reading, the degenerate-copy pairing, a semigroup, a physical mass and the
     continuum limit ALL declared NOT CLAIMED as measured constants, and nine
     gravity structures enumerated as NOT SUPPLIED.
  C  H EXISTS: symmetry, rank 8, the frame/Schur positive-semidefiniteness
     certificate and the four projector identities, at both widths and both
     points.
  D  THE PREFIX OBSTRUCTION AND THE INTERIOR LOOPHOLE: the invariant ranks; the
     three-presentation basis-dependence construction; the invariant all-slice
     residual support; and the interior windows at obstruction rank 0 with
     nontrivial kernels.
  E  THE DESCENT: the quotient dimension and K_c's positive-definiteness; the
     positive symmetric part; the landed bulk monodromy with the monic
     normalization identity; and the deep pair-core section identity.
  F  THE SECTOR THEOREM: the isometry, the commutation and the orthogonal
     split; the light sector's symmetry, positivity and self-adjointness; the
     light spectrum; the heavy sector's rank-two defect with positive symmetric
     part; the exact (0, 2, 0, 0) localization with U-equivariance; the two
     alternative sections; and the round-2 pairing fence.
  G  GENERALITY at (1/2, 1/3): the whole structure at both widths, the changed
     polynomials, and the prefix ranks.
  H  the note at its final path, the N5 fence byte-identical, and the
     nsimplify count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through H PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-five declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family census is
  A 2, B 8, C 3, D 4, E 5, F 8, G 3, H 2.
  FIVE OF THE THIRTY-FIVE GUARD CORRECTIONS RATHER THAN RESULTS:
  claim_full_reconstruction asserts the whole descended operator is
  OS-self-adjoint; claim_defect_pairs_copies asserts the REFUTED
  degenerate-copy pairing; break_basis_dependence asserts the violation counts
  are invariants; break_interior_loophole asserts the obstruction survives on
  the interior windows; and break_monic_normalization asserts the unnormalized
  integer product IS the characteristic polynomial.

RUNNING
  python3 scripts/admissibility_dirac_kahler_sectored_interior_os_reconstruction_2026_08_25.py
  python3 ... --list-mutations
  python3 ... --mutation claim_full_reconstruction
"""

from __future__ import annotations

import argparse
import math
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
# shear_hodge() re-exported by the Block 128 module, read here at UNIT VOLUME
# and at the two rational shears this block probes.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_SECTORED_INTERIOR_OS_RECONSTRUCTION_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 194 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 193 tip.
BLOCK194_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK194_RUNNER = (
    "scripts/admissibility_dirac_kahler_transfer_package_mc_generality_"
    "2026_08_25.py"
)
PARENT_ARTIFACTS = (BLOCK194_NOTE, BLOCK194_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "6c304e5c2f945e241e052fa5536b17aa2e1deda2",   # Block 194 note
    "0d0f0ab3833816b5c8b1740aa0b2a650611605f5",   # Block 194 runner
)
# THE CONSTRUCTION AUTHORITY: Block 190's width family, whose carrier, reflected
# pairings and monodromy are carried unchanged; Block 191's cell-average Hodge
# assembly, read here at UNIT volume; Block 105's primary, whose shear_hodge is
# the one imported object; and Block 188's site route, of which the width family
# is a disclosed variant.
BLOCK190_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK191_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SECTORED_INTERIOR_OS_RECONSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_transfer_package_mc_generality_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  RE-RESOLVED LIVE AT DRAFT TIME against the REMOTE origin/main
# of the real repository -- never against a local main ref, which sits behind it.
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block194-"
              "transfer-package-mc-generality-20260825")
PARENT_COMMIT = "4cbd56203b020475bc9b24cf04a2d24bfe6da43f"
# The Block 193 tip: a real ancestor of HEAD that predates Block 194 and
# therefore carries NEITHER Block 194 artifact.
STALE_PARENT_COMMIT = "37a5f926c9e15745faaffda66b308f0d04e76e47"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_full_reconstruction",
    "claim_heavy_reading_licensed",
    "claim_defect_pairs_copies",
    "claim_semigroup",
    "claim_physical_mass",
    "claim_continuum_limit",
    "break_hilbert_rank",
    "break_gram_symmetry",
    "break_psd_certificate",
    "break_prefix_ranks",
    "break_basis_dependence",
    "break_row_slices",
    "break_interior_loophole",
    "break_quotient_dimension",
    "break_monic_normalization",
    "break_bulk_monodromy",
    "break_core_section",
    "break_form_positivity",
    "break_sector_orthogonality",
    "break_light_symmetry",
    "break_light_positivity",
    "break_light_spectrum",
    "break_defect_rank",
    "break_defect_localization",
    "break_section_independence",
    "break_pairing_fence",
    "break_second_point_structure",
    "break_second_point_polynomials",
    "break_second_point_prefix",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_full_reconstruction": "B",
    "claim_heavy_reading_licensed": "B",
    "claim_defect_pairs_copies": "B",
    "claim_semigroup": "B",
    "claim_physical_mass": "B",
    "claim_continuum_limit": "B",
    "break_hilbert_rank": "C",
    "break_gram_symmetry": "C",
    "break_psd_certificate": "C",
    "break_prefix_ranks": "D",
    "break_basis_dependence": "D",
    "break_row_slices": "D",
    "break_interior_loophole": "D",
    "break_quotient_dimension": "E",
    "break_monic_normalization": "E",
    "break_bulk_monodromy": "E",
    "break_core_section": "E",
    "break_form_positivity": "E",
    "break_sector_orthogonality": "F",
    "break_light_symmetry": "F",
    "break_light_positivity": "F",
    "break_light_spectrum": "F",
    "break_defect_rank": "F",
    "break_defect_localization": "F",
    "break_section_independence": "F",
    "break_pairing_fence": "F",
    "break_second_point_structure": "G",
    "break_second_point_polynomials": "G",
    "break_second_point_prefix": "G",
    "drop_n5_fence": "H",
    "break_nsimplify_absence": "H",
}
MUTATED_FAMILIES = "ABCDEFGH"


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
    "BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20, CARRIED UNCHANGED AND STILL A DISCLOSED VARIANT OF BLOCK 188's SITE CONSTRUCTION: the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H",
    "THE FULL POSITIVE SPAN AND ITS TWO REFLECTED PAIRINGS, BLOCK 190's OBJECTS READ ON THE WHOLE SPAN RATHER THAN ON A PAIR CORE: X_A spanned by the cells of the slices {1..T/2-1}, the reflected Gram K_AA[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)] and the two-slice shifted pairing M_2[a,b] = G[idx(t_b+2, x_b), idx(theta_s t_a, x_a)] on G = Q^-1",
    "THE SEAM-ANCHORED PREFIX DOMAINS D = {1..dmax}, THE SOLVE'S OWN PRESENTATIONS, IMPOSED HERE ONLY TO BE SCOPED: dmax in {5, 4, 3} at T = 16 and dmax in {7, 6, 5} at T = 20, each the largest tau^2-safe depths and their two predecessors -- THREE DEPTHS PER WIDTH ARE NOT A DOMAIN SCAN",
    "THE INTERIOR WINDOWS D = {2, 3, 4} AT T = 16 AND D = {2..6} AT T = 20, FOUND BY THE ADVERSARIAL CHECK's CONTIGUOUS-WINDOW SCAN AND IMPOSED HERE RATHER THAN DERIVED: they are the widest windows satisfying start >= 2 and end + 2 <= T/2 - 2, and NO width-independent proof of that boundary-layer rule is supplied by this block",
    "THE PIVOT SECTION AND ITS TWO DECLARED ALTERNATIVES: the eight representative cells returned by the exact rref pivots of K_AD -- the pair core at slices {2, 3} -- together with the deep pair core at slices {3, 4} and a SCATTERED eight-cell section deliberately NOT closed under the displayed momentum involution",
    "THE MOMENTUM INVOLUTION U AS THE TWO-SITE SPATIAL SHIFT ON THE EIGHT REPRESENTATIVES, AND THE ONE-SITE SPATIAL SHIFT S PROJECTED ONTO THE HEAVY SECTOR -- both are Block 190's grading objects carried unchanged, and NEITHER is a derived symmetry of any theory",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE AT UNIT VOLUME AND AT THE TWO RATIONAL SHEARS 5/13 AND 1/3 -- THE ONLY OBJECT IMPORTED -- assembled into H by Block 191's quarter-weighted four-corner cell average at Block 190's seam convention",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SEVEN ARE FALSE
# AND STAY FALSE.  THE SECOND IS THE HALF THIS BLOCK REFUSES TO OVERSTATE AND
# THE THIRD IS THE READING ROUND TWO REFUTED.
GRAVITY_SUPPLIED_CLAIMED = False
FULL_RECONSTRUCTION_CLAIMED = False
HEAVY_READING_LICENSED_CLAIMED = False
DEFECT_PAIRS_COPIES_CLAIMED = False
SEMIGROUP_CLAIMED = False
PHYSICAL_MASS_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
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
CHECK_VERDICT = "SECTORED-INTERIOR-RECONSTRUCTION-CONFIRMED-TWICE-PAIRING-READING-REFUTED"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
WIDTHS = (16, 20)
SPACE_EXTENT = 4
QUOTIENT_DIM = 8
DEEP_ODD_CORE = 3
UNIT_VOLUME = sp.Integer(1)

FIXTURE = ("9/20", "5/13")
SECOND_POINT = ("1/2", "1/3")
POINTS = (FIXTURE, SECOND_POINT)


def rat(text: str) -> sp.Rational:
    """A rational from a plain string literal.  NOT nsimplify: sp.Rational on a
    decimal-free ratio of integers is exact by construction."""
    return sp.Rational(text)


# --- C: THE OS HILBERT SPACE -------------------------------------------------
# The full positive span has T/2 - 1 slices of four cells each.
SPAN_SIZES = {16: 28, 20: 36}
CARRIER_RANKS = {16: 64, 20: 80}
HILBERT_RANK = 8
GRAM_SYMMETRY_RESIDUAL = 0
# THE POSITIVE-SEMIDEFINITENESS CERTIFICATE, AND IT USES NO FLOATING INERTIA
# CALL: eight positive leading minors of the framed Gram, an exact ZERO Schur
# residual through that frame, and the four projector identities.
FRAME_MINOR_SIGNS = (1,) * 8
SCHUR_RESIDUAL = 0
PROJECTOR_RESIDUALS = (0, 0, 0, 0)      # V#E - I, P^2 - P, P^T K - K P, K(I-P)

# --- D: THE PREFIX OBSTRUCTION AND THE INTERIOR LOOPHOLE ---------------------
PREFIX_DEPTHS = {16: (5, 4, 3), 20: (7, 6, 5)}
# rank(K_AD) is 8 at every prefix depth: the prefix already spans the quotient,
# which is exactly why its failure to descend is a PRESENTATION failure.
PREFIX_DOMAIN_RANK = 8
PREFIX_NULLITIES = {16: (12, 8, 4), 20: (20, 16, 12)}
# THE INVARIANT OBSTRUCTION, AND IT IS A RANK AND NOT A COUNT.
PREFIX_OBSTRUCTION_RANKS = {16: (2, 1, 1), 20: (2, 1, 1)}
# THE THREE PRESENTATIONS OF THE SAME KERNEL.  The default presentation is
# SymPy's nullspace; the adapted one takes the pivot columns of M_2 N followed
# by ker(M_2 N) pulled back through N; the all-violating one adds one violating
# vector to every joint-null vector.  All three are exact bases -- their spans
# have the full kernel rank -- and their violating-vector COUNTS differ.
PREFIX_DEFAULT_COUNTS = {16: (8, 6, 2), 20: (14, 12, 8)}
PREFIX_ADAPTED_COUNTS = {16: (2, 1, 1), 20: (2, 1, 1)}
PREFIX_ALL_COUNTS = {16: (12, 8, 4), 20: (20, 16, 12)}
VIOLATION_COUNT_IS_INVARIANT = False
# The residual column support meets EVERY positive slice, and THAT is invariant
# under kernel-basis change.
PREFIX_ROW_SLICES = {16: (1, 2, 3, 4, 5, 6, 7), 20: (1, 2, 3, 4, 5, 6, 7, 8, 9)}
# THE LOOPHOLE.  The interior windows are the widest contiguous domains obeying
# start >= 2 and end + 2 <= T/2 - 2.
INTERIOR_WINDOWS = {16: (2, 3, 4), 20: (2, 3, 4, 5, 6)}
INTERIOR_NULLITIES = {16: 4, 20: 12}
INTERIOR_OBSTRUCTION_RANK = 0
INTERIOR_DOMAIN_RANK = 8

# --- E: THE DESCENT ----------------------------------------------------------
QUOTIENT_GRAM_SYMMETRY_RESIDUAL = 0
QUOTIENT_MINOR_SIGNS = (1,) * 8
# The shifted form's SYMMETRIC PART is positive-definite: shifted reflection
# positivity holds as a FORM on all of H, and what fails is symmetry.
SHIFTED_SYMMETRIC_MINOR_SIGNS = (1,) * 8
OPERATOR_DEFINITION_RESIDUAL = 0        # nnz(K_c T_2 - M_2c)
# THE LANDED BLOCK 194 PRIMITIVE PALINDROMIC QUADRATICS, per point, as
# (a, b, a) coefficient triples.  They are LANDED VALUES, reproduced here as the
# spectrum of the DESCENDED operator rather than of a pair-core frame.
LIGHT_FACTORS = {
    FIXTURE: (39529825, -109432706, 39529825),
    SECOND_POINT: (233, -690, 233),
}
HEAVY_FACTORS = {
    FIXTURE: (22569375, -233631106, 22569375),
    SECOND_POINT: (739, -7258, 739),
}
FACTOR_MULTIPLICITY = 2
# BLOCK 194's MONIC-NORMALIZATION CORRECTION, CARRIED FORWARD AS THE SAME
# FORMULA: the displayed integer product equals s times the MONIC characteristic
# polynomial, and s = (a_light a_heavy)^2 exactly.
MONIC_SCALARS = {
    FIXTURE: 795955611005101889386962890625,
    SECOND_POINT: 29648362969,
}
MONIC_SCALAR_IS_LEADING_SQUARED = True
MONIC_RESIDUAL = 0
# THE DEEP PAIR-CORE SECTION IS BLOCK 190's OWN FRAME: taking t0 = 3 as the
# section reproduces K_c and L_2 entrywise, so the descended operator IS W there.
CORE_SECTION_TIMES = (3, 4)
CORE_SECTION_IS_LANDED_W = True
LANDED_W_RESIDUALS = (0, 0)             # nnz(K_sec - K_c(t0=3)), nnz(M_sec - L_2)

# --- F: THE SECTOR THEOREM ---------------------------------------------------
SECTOR_DIM = 4
ISOMETRY_RESIDUAL = 0                   # nnz(U^T K_c U - K_c)
COMMUTATION_RESIDUAL = 0                # nnz(T_2 U - U T_2)
CROSS_BLOCK_RESIDUALS = (0, 0)          # nnz(b+^T K_c b-), nnz(b+^T M_2c b-)
# THE LIGHT SECTOR: the reconstruction, and it is the block's centre.
LIGHT_DEFECT_RANK = 0
LIGHT_DEFECT_RESIDUAL = 0               # nnz(M_+ - M_+^T)
LIGHT_SELF_ADJOINT_RESIDUAL = 0         # nnz(K_+ T_+ - T_+^T K_+)
LIGHT_GRAM_MINOR_SIGNS = (1, 1, 1, 1)
LIGHT_FORM_MINOR_SIGNS = (1, 1, 1, 1)
# THE LIGHT SPECTRUM, READ WITH NO RADICAL EVER EVALUATED: the trace T = -b/a of
# the palindromic quadratic exceeds 2 and the discriminant is positive, so the
# roots are a POSITIVE reciprocal pair e^{+/- theta}, each of multiplicity two.
LIGHT_DISCRIMINANTS = {FIXTURE: 5725088884359936, SECOND_POINT: 258944}
HEAVY_DISCRIMINANTS = {FIXTURE: 52545986939220736, SECOND_POINT: 50494080}
LIGHT_TRACE_EXCEEDS_TWO = True
LIGHT_ROOT_PRODUCT = 1
# THE HEAVY SECTOR: positive-definite symmetric part, and an exact rank-two
# self-adjointness defect that is NOT removed by anything in this block.
HEAVY_DEFECT_RANK = 2
HEAVY_DEFECT_RESIDUAL = 8               # nnz(M_- - M_-^T) = nnz(K_- T_- - T_-^T K_-)
HEAVY_GRAM_MINOR_SIGNS = (1, 1, 1, 1)
HEAVY_SYMMETRIC_MINOR_SIGNS = (1, 1, 1, 1)
# THE COMPLETE DEFECT AND ITS EXACT LOCALIZATION.  The projector ranks are in
# the order (+,+), (-,-), (+,-), (-,+).
DEFECT_RANK = 2
DEFECT_NONZERO_ENTRIES = 32
DEFECT_PROJECTOR_RANKS = (0, 2, 0, 0)
DEFECT_EQUIVARIANCE_RESIDUALS = (0, 0)  # nnz(U^T D U - D), nnz(U D - D U)
# THE TWO DECLARED ALTERNATIVE SECTIONS, given as explicit cell tuples so the
# basis-independence statement is a CONGRUENCE statement and not a re-run.
ALTERNATIVE_SECTIONS = {
    16: {
        "deep_core": ((3, 0), (3, 1), (3, 2), (3, 3),
                      (4, 0), (4, 1), (4, 2), (4, 3)),
        "scattered": ((2, 0), (2, 2), (2, 3), (3, 2),
                      (3, 3), (4, 0), (4, 1), (4, 3)),
    },
    20: {
        "deep_core": ((3, 0), (3, 1), (3, 2), (3, 3),
                      (4, 0), (4, 1), (4, 2), (4, 3)),
        "scattered": ((2, 1), (3, 2), (4, 2), (5, 0),
                      (5, 3), (6, 0), (6, 1), (6, 3)),
    },
}
SECTION_RESIDUALS = (0, 0, 0, 0)   # K congruence, M congruence, T similarity, U^2-I
SCATTERED_SECTION_U_IS_PERMUTATION = False
# THE ROUND-2 FENCE, GATED.  In the DECLARED heavy basis at T = 16 and the
# fixture, the defect is the exact rational multiple s J of an integer skew
# matrix and factors as a two-direction wedge; the heavy discriminant is NOT a
# rational square, so the heavy module is two copies of one irreducible
# quadratic module; the one-site shift restricted to the heavy sector is an
# exact commuting complex structure; and yet the defect does NOT satisfy
# S^T D S = D.  Both S-parity components have rank FOUR.
DEFECT_SCALE = sp.Rational(
    15412245266178664398193359375000000,
    12468368115055868578374473995988256597352642542544230293)
DEFECT_INTEGER_MATRIX = (
    (0, 0, -499791697674660, 1588013041094501),
    (0, 0, 12377859914160, -39328790486076),
    (499791697674660, -12377859914160, 0, 0),
    (-1588013041094501, 39328790486076, 0, 0),
)
WEDGE_U = (0, 0, 2034493740, -6464298239)
WEDGE_V = (-245659, 6084, 0, 0)
WEDGE_U_NORM = 45926316500837688721
WEDGE_V_NORM = 60385359337
WEDGE_INNER = 0
WEDGE_RESIDUAL = 0
HEAVY_DISCRIMINANT_IS_SQUARE = False
COMPLEX_STRUCTURE_RESIDUALS = (0, 0)    # nnz(S^2 + I), nnz(S T_- - T_- S)
PAIRING_RESIDUALS = (8, 8)              # nnz(S^T D S - D), nnz(S^T D S + D)
PARITY_COMPONENT_RANKS = (4, 4)
DEFECT_PURELY_PAIRS_COPIES = False

# --- G: THE SECOND POINT -----------------------------------------------------
# Every structural invariant persists; only the coefficients move.
SECOND_POINT_STRUCTURE = (
    INTERIOR_OBSTRUCTION_RANK, QUOTIENT_GRAM_SYMMETRY_RESIDUAL,
    DEFECT_RANK, DEFECT_PROJECTOR_RANKS, LIGHT_DEFECT_RANK, HEAVY_DEFECT_RANK)
SECOND_POINT_POLYNOMIALS_DIFFER = True
SECOND_POINT_PREFIX_RANKS = {16: (2, 1, 1), 20: (2, 1, 1)}

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO, so a residual, a minor or a defect entry passed through it can
# silently turn a RANK-TWO OBSTRUCTION into a clean self-adjoint operator -- and
# this block's entire content is the difference between an exactly zero
# antisymmetric part on one sector and an exactly rank-two one on the other.
# The defect's own scale here is s = 1.2e-19 in magnitude, far below any default
# tolerance, so a single such call would ERASE the block's negative half.
# Every mass, shear and volume here is ALREADY an exact sympy Rational.  Gate H
# counts the occurrences in this file's own source and requires ZERO.
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
    QQ^(n x n) exactly; DomainMatrix carries out the inverse, the rank, the rref
    and the determinant by exact fraction-free arithmetic over that field.  No
    float is created at any point and no tolerance exists to be tuned.  It is
    used in place of the dense sympy fallback purely because that is slow at
    dimension 80, and it changes NO value."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return rational_matrix(matrix).inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    return rational_matrix(matrix).rank()


def exact_det(matrix: sp.MatrixBase) -> sp.Expr:
    return QQ.to_sympy(rational_matrix(matrix).det())


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is
    involved."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


def leading_minor_signs(matrix: sp.MatrixBase) -> tuple:
    """THE POSITIVITY CERTIFICATE, AND IT IS A SIGN OF AN EXACT RATIONAL
    DETERMINANT.  Sylvester's criterion certifies definiteness for a SYMMETRIC
    matrix and for nothing else, so every gate that reads these signs measures
    the symmetry residual of the same matrix in the same gate."""
    return tuple(int(sp.sign(exact_det(matrix[:k, :k])))
                 for k in range(1, matrix.rows + 1))


Z = sp.Symbol("z")


# ---------------------------------------------------------------------------
# THE WIDTH FAMILY AT AN ARBITRARY WIDTH AND (m, c).  Everything except the
# shear block is rebuilt here; the shear block is the ONE import.
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


def staggered_kernel(width: int) -> sp.Matrix:
    kernel = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
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
    matrix = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            matrix[site_index(width, site_theta(width, time), space),
                   site_index(width, time, space)] = 1
    return matrix


def site_restricted_raising(width: int, raising: sp.Matrix) -> sp.Matrix:
    half = width // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for row in range(width * SPACE_EXTENT):
        for column in range(width * SPACE_EXTENT):
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


_GEOMETRY_CACHE: dict = {}


def geometry(width: int) -> dict:
    """The (m, c)-independent half of the carrier, built once per width."""
    if width in _GEOMETRY_CACHE:
        return _GEOMETRY_CACHE[width]
    kernel = staggered_kernel(width)
    reflection = reflection_permutation(width)
    raising = site_restricted_raising(width, raising_part(width, kernel))
    glue = sp.expand(raising - reflection * raising * reflection)
    embeddings = {(time, space): cell_embedding(width, time, space)
                  for time in range(width) for space in range(SPACE_EXTENT)}
    record = {"reflection": reflection, "glue": glue, "embeddings": embeddings}
    _GEOMETRY_CACHE[width] = record
    return record


def imported_shear_block(shear: sp.Rational) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT: the LANDED Block 105 shear Hodge
    diag(v, v g(c)^-1, 1/v) with g(c) = [[1, c], [c, 1]], read at UNIT volume.
    NO nsimplify: both arguments are already exact sympy Rationals."""
    return sp.Matrix(b128.block105.shear_hodge(shear, UNIT_VOLUME))


def site_hodge(width: int, shear: sp.Rational) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule
    at Block 190's seam convention and at unit volume."""
    half = width // 2
    block = imported_shear_block(shear)
    reflected = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    embeddings = geometry(width)["embeddings"]
    result = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for time in range(width):
        chosen = block if time < half else reflected
        for space in range(SPACE_EXTENT):
            embedding = embeddings[time, space]
            result += embedding * chosen * embedding.T / 4
    return sp.expand(result)


def completion(mass: sp.Rational, hodge: sp.Matrix, glue: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    return sp.expand(mass * hodge + hodge * glue - glue.T * hodge)


# ---------------------------------------------------------------------------
# THE HEAVY WORK, DONE ONCE PER (width, m, c) AND SHARED.  The exact 64 x 64 and
# 80 x 80 inverses are the only expensive steps in this runner and nothing
# recomputes one: four inverses serve every gate below.
# ---------------------------------------------------------------------------
_CARRIER_CACHE: dict = {}


def carrier(width: int, point: tuple) -> dict:
    key = (width, point)
    if key in _CARRIER_CACHE:
        return _CARRIER_CACHE[key]
    mass, shear = rat(point[0]), rat(point[1])
    parts = geometry(width)
    action = completion(mass, site_hodge(width, shear), parts["glue"])
    domain = rational_matrix(action)
    rank = domain.rank()
    record = {"width": width, "action": action, "rank": rank,
              "reflection": parts["reflection"], "inverse": None}
    if rank == width * SPACE_EXTENT:
        record["inverse"] = domain.inv().to_Matrix()
    _CARRIER_CACHE[key] = record
    return record


def cells(times: tuple) -> tuple:
    return tuple((time, space) for time in times for space in range(SPACE_EXTENT))


def reflected_pairing(width: int, inverse: sp.Matrix, rows: tuple,
                      columns: tuple, shift: int) -> sp.Matrix:
    """K_AA at shift 0 and M_2 at shift 2, in Block 190's convention:
    G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]."""
    matrix = sp.zeros(len(rows), len(columns))
    for a, (row_time, row_space) in enumerate(rows):
        image = site_index(width, site_theta(width, row_time), row_space)
        for b, (column_time, column_space) in enumerate(columns):
            matrix[a, b] = inverse[
                site_index(width, column_time + shift, column_space), image]
    return matrix


def positive_slices(width: int) -> tuple:
    return tuple(range(1, width // 2))


def momentum_involution(reps: tuple, amount: int) -> sp.Matrix:
    """U at amount 2 is the two-site spatial shift and is an involution; S at
    amount 1 is the one-site shift."""
    position = {cell: index for index, cell in enumerate(reps)}
    matrix = sp.zeros(len(reps), len(reps))
    for index, (time, space) in enumerate(reps):
        matrix[position[time, (space + amount) % SPACE_EXTENT], index] = 1
    return matrix


def eigen_basis(involution: sp.Matrix, sign: int) -> sp.Matrix:
    vectors = (involution - sign * sp.eye(involution.rows)).nullspace()
    return sp.Matrix.hstack(*vectors)


# ---------------------------------------------------------------------------
# THE EXACT SPECTRAL READ.  Everything below is polynomial arithmetic over QQ:
# no root is ever evaluated, no radical is taken and no float exists.
# ---------------------------------------------------------------------------
def primitive_coefficients(expression: sp.Expr) -> tuple:
    """The integer PRIMITIVE form of a rational polynomial: clear denominators
    by their lcm, divide by the integer content, and fix a positive leader."""
    coefficients = [sp.Rational(value)
                    for value in sp.Poly(sp.expand(expression), Z).all_coeffs()]
    multiplier = 1
    for value in coefficients:
        multiplier = sp.ilcm(multiplier, value.q)
    integers = [sp.Integer(value * multiplier) for value in coefficients]
    content = 0
    for value in integers:
        content = sp.igcd(content, int(value))
    integers = [value // content for value in integers]
    if integers[0] < 0:
        integers = [-value for value in integers]
    return tuple(int(value) for value in integers)


def primitive_factors(matrix: sp.Matrix) -> tuple:
    """The primitive irreducible QQ factors of charpoly with multiplicity."""
    factors = []
    for factor, multiplicity in sp.factor_list(
            matrix.charpoly(Z).as_expr())[1]:
        if factor.has(Z):
            factors.append((primitive_coefficients(factor), int(multiplicity)))
    return tuple(sorted(factors, key=lambda item: (len(item[0]), item[0])))


def factor_expression(coefficients: tuple) -> sp.Expr:
    degree = len(coefficients) - 1
    return sum(sp.Integer(coefficients[i]) * Z ** (degree - i)
               for i in range(len(coefficients)))


def monic_scalar(matrix: sp.Matrix, factors: tuple) -> tuple:
    """BLOCK 194's C1 CORRECTION, CARRIED FORWARD AS AN EXACT MEASUREMENT.
    Returns the scalar s and the polynomial residual of

        prod_i (primitive factor_i)^(multiplicity_i)  =  s * charpoly_monic.

    A zero residual with an integer s is the whole content of the correction:
    the displayed integer product is the characteristic polynomial only after
    division by s."""
    product = sp.Integer(1)
    for coefficients, multiplicity in factors:
        product *= factor_expression(coefficients) ** multiplicity
    monic = sp.Poly(matrix.charpoly(Z).as_expr(), Z).monic().as_expr()
    quotient, remainder = sp.div(sp.expand(product), sp.expand(monic), Z)
    return sp.Rational(quotient), sp.expand(remainder)


def quadratic_trace(coefficients: tuple) -> sp.Rational:
    """T = 2 cosh(theta) = -b/a for a primitive palindromic factor a z^2+b z+a."""
    return sp.Rational(-coefficients[1], coefficients[0])


def quadratic_discriminant(coefficients: tuple) -> int:
    a, b, c = coefficients
    return b * b - 4 * a * c


def is_perfect_square(value: int) -> bool:
    """EXACT, AND NO RADICAL IS EVALUATED: an integer square root by integer
    arithmetic, squared back and compared."""
    if value < 0:
        return False
    root = math.isqrt(int(value))
    return root * root == int(value)


def quadratic_annihilates(matrix: sp.Matrix, coefficients: tuple) -> int:
    a, b, c = coefficients
    return residual_count(
        a * matrix * matrix + b * matrix + c * sp.eye(matrix.rows))


# ---------------------------------------------------------------------------
# THE MEASUREMENT PASS.  Every number this runner reports is produced here, once
# and before any mutation flag is read, and every heavy inverse is shared.
# ---------------------------------------------------------------------------
@dataclass
class SectorFacts:
    defect_rank: int
    defect_residual: int
    self_adjoint_residual: int
    gram_signs: tuple
    form_signs: tuple
    symmetric_signs: tuple
    factors: tuple
    annihilated: int


@dataclass
class PackageFacts:
    carrier_rank: int
    span_size: int
    gram_rank: int
    gram_symmetry: int
    frame_signs: tuple
    schur_residual: int
    projector_residuals: tuple
    domain_rank: int
    nullity: int
    obstruction: int
    reps: tuple
    quotient_symmetry: int
    quotient_signs: tuple
    shifted_symmetric_signs: tuple
    operator_residual: int
    factors: tuple
    monic_scalar: object
    monic_residual: object
    monic_is_leading_squared: bool
    isometry_residual: int
    commutation_residual: int
    cross_residuals: tuple
    defect_rank: int
    defect_entries: int
    defect_projectors: tuple
    defect_equivariance: tuple
    sectors: dict
    sections: dict
    heavy_extra: dict


def sector_facts(gram: sp.Matrix, form: sp.Matrix,
                 basis: sp.Matrix) -> tuple:
    restricted_gram = sp.expand(basis.T * gram * basis)
    restricted_form = sp.expand(basis.T * form * basis)
    defect = sp.expand(restricted_form - restricted_form.T)
    operator = sp.expand(exact_inverse(restricted_gram) * restricted_form)
    factors = primitive_factors(operator)
    facts = SectorFacts(
        defect_rank=exact_rank(defect) if residual_count(defect) else 0,
        defect_residual=residual_count(defect),
        self_adjoint_residual=residual_count(
            restricted_gram * operator - operator.T * restricted_gram),
        gram_signs=leading_minor_signs(restricted_gram),
        form_signs=leading_minor_signs(restricted_form),
        symmetric_signs=leading_minor_signs(
            sp.expand((restricted_form + restricted_form.T) / 2)),
        factors=factors,
        annihilated=quadratic_annihilates(operator, factors[0][0])
        if len(factors) == 1 and len(factors[0][0]) == 3 else -1)
    return facts, restricted_gram, restricted_form, defect, operator


def measure_package(width: int, point: tuple) -> PackageFacts:
    record = carrier(width, point)
    inverse = record["inverse"]
    full = cells(positive_slices(width))
    domain = cells(INTERIOR_WINDOWS[width])
    gram = reflected_pairing(width, inverse, full, full, 0)
    domain_gram = reflected_pairing(width, inverse, full, domain, 0)
    shifted = reflected_pairing(width, inverse, full, domain, 2)

    domain_rank = exact_rank(domain_gram)
    stacked = exact_rank(domain_gram.col_join(shifted))

    _, pivots = rational_matrix(domain_gram).rref()
    pivots = tuple(pivots)
    reps = tuple(domain[column] for column in pivots)
    position = {cell: index for index, cell in enumerate(full)}
    rows = tuple(position[cell] for cell in reps)
    quotient_gram = gram.extract(rows, rows)
    quotient_form = shifted.extract(rows, pivots)
    operator = sp.expand(exact_inverse(quotient_gram) * quotient_form)

    # the frame / Schur positive-semidefiniteness certificate
    frame = sp.zeros(len(full), QUOTIENT_DIM)
    for column, row in enumerate(rows):
        frame[row, column] = 1
    sharp = sp.expand(exact_inverse(quotient_gram) * frame.T * gram)
    projector = sp.expand(frame * sharp)
    schur = residual_count(gram - gram * frame
                           * exact_inverse(quotient_gram) * frame.T * gram)
    projector_residuals = (
        residual_count(sharp * frame - sp.eye(QUOTIENT_DIM)),
        residual_count(projector * projector - projector),
        residual_count(projector.T * gram - gram * projector),
        residual_count(gram * (sp.eye(len(full)) - projector)))

    involution = momentum_involution(reps, 2)
    defect = sp.expand(quotient_form - quotient_form.T)
    plus = (sp.eye(QUOTIENT_DIM) + involution) / 2
    minus = (sp.eye(QUOTIENT_DIM) - involution) / 2
    light_basis = eigen_basis(involution, 1)
    heavy_basis = eigen_basis(involution, -1)

    sectors = {}
    heavy_extra = {}
    for name, basis in (("light", light_basis), ("heavy", heavy_basis)):
        facts, _, restricted_form, restricted_defect, sector_operator = \
            sector_facts(quotient_gram, quotient_form, basis)
        sectors[name] = facts
        if name == "heavy":
            heavy_extra = {"defect": restricted_defect,
                           "operator": sector_operator, "basis": basis,
                           "form": restricted_form}

    # the two declared alternative sections, as congruence statements
    sections = {}
    domain_position = {cell: index for index, cell in enumerate(domain)}
    for label, chosen_cells in ALTERNATIVE_SECTIONS[width].items():
        columns = tuple(domain_position[cell] for cell in chosen_cells)
        section_rows = tuple(position[cell] for cell in chosen_cells)
        section_gram = gram.extract(section_rows, section_rows)
        section_form = shifted.extract(section_rows, columns)
        cross = gram.extract(rows, section_rows)
        change = sp.expand(exact_inverse(quotient_gram) * cross)
        section_operator = sp.expand(
            exact_inverse(section_gram) * section_form)
        induced = sp.expand(exact_inverse(change) * involution * change)
        section_light, section_heavy = (
            sector_facts(section_gram, section_form,
                         eigen_basis(induced, sign))[0]
            for sign in (1, -1))
        landed = (0, 0)
        if label == "deep_core":
            core = cells(CORE_SECTION_TIMES)
            landed = (
                residual_count(section_gram - reflected_pairing(
                    width, inverse, core, core, 0)),
                residual_count(section_form - reflected_pairing(
                    width, inverse, core, core, 2)))
        sections[label] = {
            "determinant_nonzero": exact_det(change) != 0,
            "residuals": (
                residual_count(section_gram - change.T * quotient_gram * change),
                residual_count(section_form - change.T * quotient_form * change),
                residual_count(section_operator
                               - exact_inverse(change) * operator * change),
                residual_count(induced * induced - sp.eye(QUOTIENT_DIM))),
            "u_is_permutation": all(
                induced[i, j] in (0, 1)
                for i in range(QUOTIENT_DIM) for j in range(QUOTIENT_DIM)),
            "light": section_light,
            "heavy": section_heavy,
            "landed_w": landed,
        }

    factors = primitive_factors(operator)
    scalar, remainder = monic_scalar(operator, factors)
    leading = sp.Integer(1)
    for coefficients, multiplicity in factors:
        leading *= sp.Integer(coefficients[0]) ** multiplicity

    facts = PackageFacts(
        carrier_rank=record["rank"],
        span_size=len(full),
        gram_rank=exact_rank(gram),
        gram_symmetry=residual_count(gram - gram.T),
        frame_signs=leading_minor_signs(quotient_gram),
        schur_residual=schur,
        projector_residuals=projector_residuals,
        domain_rank=domain_rank,
        nullity=len(domain) - domain_rank,
        obstruction=stacked - domain_rank,
        reps=reps,
        quotient_symmetry=residual_count(quotient_gram - quotient_gram.T),
        quotient_signs=leading_minor_signs(quotient_gram),
        shifted_symmetric_signs=leading_minor_signs(
            sp.expand((quotient_form + quotient_form.T) / 2)),
        operator_residual=residual_count(quotient_gram * operator
                                         - quotient_form),
        factors=factors,
        monic_scalar=scalar,
        monic_residual=remainder,
        monic_is_leading_squared=(scalar == leading),
        isometry_residual=residual_count(
            involution.T * quotient_gram * involution - quotient_gram),
        commutation_residual=residual_count(
            operator * involution - involution * operator),
        cross_residuals=(
            residual_count(light_basis.T * quotient_gram * heavy_basis),
            residual_count(light_basis.T * quotient_form * heavy_basis)),
        defect_rank=exact_rank(defect),
        defect_entries=residual_count(defect),
        defect_projectors=(
            exact_rank(sp.expand(plus.T * defect * plus)),
            exact_rank(sp.expand(minus.T * defect * minus)),
            exact_rank(sp.expand(plus.T * defect * minus)),
            exact_rank(sp.expand(minus.T * defect * plus))),
        defect_equivariance=(
            residual_count(involution.T * defect * involution - defect),
            residual_count(involution * defect - defect * involution)),
        sectors=sectors,
        sections=sections,
        heavy_extra=heavy_extra)
    return facts


@dataclass
class PrefixFacts:
    domain_rank: int
    nullity: int
    obstruction: int
    default_count: int
    adapted_count: int
    all_count: int
    adapted_is_basis: bool
    all_is_basis: bool
    row_slices: tuple


def measure_prefix(width: int, point: tuple, depth: int) -> PrefixFacts:
    """THE SEAM-ANCHORED PREFIX DOMAIN D = {1..depth}, MEASURED IN THREE
    PRESENTATIONS OF THE SAME KERNEL.  The invariant is the RANK of M_2
    restricted to ker(K_AD); the COUNT of violating basis vectors is not an
    invariant, and the two constructed presentations prove it."""
    inverse = carrier(width, point)["inverse"]
    full = cells(positive_slices(width))
    domain = cells(tuple(range(1, depth + 1)))
    domain_gram = reflected_pairing(width, inverse, full, domain, 0)
    shifted = reflected_pairing(width, inverse, full, domain, 2)
    basis = domain_gram.nullspace()
    nullity = len(basis)
    default_count = sum(1 for vector in basis
                        if residual_count(shifted * vector))
    kernel = sp.Matrix.hstack(*basis)
    residual = sp.expand(shifted * kernel)
    obstruction = exact_rank(residual)
    _, residual_pivots = rational_matrix(residual).rref()
    residual_pivots = tuple(residual_pivots)
    joint_null = [sp.expand(kernel * vector) for vector in residual.nullspace()]
    adapted = [kernel[:, column] for column in residual_pivots] + joint_null
    witness = kernel[:, residual_pivots[0]] if residual_pivots else None
    violating = ([kernel[:, column] for column in residual_pivots]
                 + [sp.expand(vector + witness) for vector in joint_null]
                 if witness is not None else list(adapted))
    slices = set()
    for row in range(residual.rows):
        if any(residual[row, column] != 0 for column in range(residual.cols)):
            slices.add(full[row][0])
    return PrefixFacts(
        domain_rank=exact_rank(domain_gram),
        nullity=nullity,
        obstruction=obstruction,
        default_count=default_count,
        adapted_count=sum(1 for vector in adapted
                          if residual_count(shifted * vector)),
        all_count=sum(1 for vector in violating
                      if residual_count(shifted * vector)),
        adapted_is_basis=exact_rank(sp.Matrix.hstack(*adapted)) == nullity,
        all_is_basis=exact_rank(sp.Matrix.hstack(*violating)) == nullity,
        row_slices=tuple(sorted(slices)))


@dataclass
class WedgeFacts:
    scale: object
    integer_matrix: tuple
    gamma: object
    left: tuple
    right: tuple
    left_norm: object
    right_norm: object
    inner: object
    residual: int
    complex_structure: tuple
    pairing_residuals: tuple
    parity_ranks: tuple
    discriminant: int
    discriminant_is_square: bool


def measure_wedge(facts: PackageFacts, reps: tuple) -> WedgeFacts:
    """THE ROUND-2 FENCE, MEASURED.  The heavy defect is factored exactly as a
    two-direction wedge over QQ -- no normalisation, so no square root ever
    appears -- and the one-site shift restricted to the heavy sector is tested
    as a pairing of the two momentum-degenerate copies.  It is not one."""
    extra = facts.heavy_extra
    defect, operator, basis = extra["defect"], extra["operator"], extra["basis"]
    denominator = 1
    for entry in defect:
        denominator = sp.ilcm(denominator, sp.Rational(entry).q)
    integers = defect * denominator
    content = 0
    for entry in integers:
        content = sp.igcd(content, abs(int(entry)))
    integers = integers / content
    scale = sp.Rational(content, denominator)
    pivot = next((row, column)
                 for row in range(integers.rows)
                 for column in range(row + 1, integers.cols)
                 if integers[row, column] != 0)
    row, column = pivot
    left_column, right_column = integers[:, row], integers[:, column]
    left_content = right_content = 0
    for entry in left_column:
        left_content = sp.igcd(left_content, abs(int(entry)))
    for entry in right_column:
        right_content = sp.igcd(right_content, abs(int(entry)))
    left = left_column / left_content
    right = right_column / right_content
    gamma = sp.Rational(scale * left_content * right_content,
                        integers[row, column])
    shift = momentum_involution(reps, 1)
    heavy_shift = sp.expand(
        exact_inverse(basis.T * basis) * basis.T * shift * basis)
    transformed = sp.expand(heavy_shift.T * defect * heavy_shift)
    heavy_factor = facts.sectors["heavy"].factors[0][0]
    return WedgeFacts(
        scale=scale,
        integer_matrix=tuple(tuple(int(integers[i, j]) for j in range(4))
                             for i in range(4)),
        gamma=gamma,
        left=tuple(int(value) for value in left),
        right=tuple(int(value) for value in right),
        left_norm=(left.T * left)[0, 0],
        right_norm=(right.T * right)[0, 0],
        inner=(left.T * right)[0, 0],
        residual=residual_count(defect - gamma * (left * right.T
                                                  - right * left.T)),
        complex_structure=(
            residual_count(heavy_shift * heavy_shift + sp.eye(4)),
            residual_count(heavy_shift * operator - operator * heavy_shift)),
        pairing_residuals=(residual_count(transformed - defect),
                           residual_count(transformed + defect)),
        parity_ranks=(exact_rank(sp.expand((defect + transformed) / 2)),
                      exact_rank(sp.expand((defect - transformed) / 2))),
        discriminant=quadratic_discriminant(heavy_factor),
        discriminant_is_square=is_perfect_square(
            quadratic_discriminant(heavy_factor)))


@dataclass
class Facts:
    main_head: str
    authority: AuthorityCertificate
    scope: dict
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    packages: dict
    prefixes: dict
    wedge: WedgeFacts
    inverse_count: int
    nsimplify_calls: int


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    authority = authority_certificate(main_head)
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""

    packages = {(width, point): measure_package(width, point)
                for point in POINTS for width in WIDTHS}
    prefixes = {(width, point, depth): measure_prefix(width, point, depth)
                for point in POINTS for width in WIDTHS
                for depth in PREFIX_DEPTHS[width]}
    wedge = measure_wedge(packages[(16, FIXTURE)],
                          packages[(16, FIXTURE)].reps)

    return Facts(
        main_head=main_head,
        authority=authority,
        scope=scope_certificate(note_text),
        imposed=len(IMPOSED_OBJECTS),
        registered=len(REGISTERED_OBJECTS),
        adopted=len(ADOPTED_OBJECTS),
        unsupplied=len(UNSUPPLIED_GRAVITY_STRUCTURES),
        packages=packages,
        prefixes=prefixes,
        wedge=wedge,
        inverse_count=len(_CARRIER_CACHE),
        nsimplify_calls=nsimplify_occurrences())


# ---------------------------------------------------------------------------
# THE CLAIMS, and the thirty-five mutations that each rewrite exactly one
# ---------------------------------------------------------------------------
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
        "full_reconstruction": FULL_RECONSTRUCTION_CLAIMED,
        "heavy_reading_licensed": HEAVY_READING_LICENSED_CLAIMED,
        "defect_pairs_copies": DEFECT_PAIRS_COPIES_CLAIMED,
        "semigroup": SEMIGROUP_CLAIMED,
        "physical_mass": PHYSICAL_MASS_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        # C -- the OS Hilbert space.
        "hilbert_rank": HILBERT_RANK,
        "gram_symmetry": GRAM_SYMMETRY_RESIDUAL,
        "span_sizes": dict(SPAN_SIZES),
        "carrier_ranks": dict(CARRIER_RANKS),
        "frame_signs": FRAME_MINOR_SIGNS,
        "schur_residual": SCHUR_RESIDUAL,
        "projector_residuals": PROJECTOR_RESIDUALS,
        # D -- the prefix obstruction and the interior loophole.
        "prefix_ranks": {width: PREFIX_OBSTRUCTION_RANKS[width]
                         for width in WIDTHS},
        "prefix_nullities": dict(PREFIX_NULLITIES),
        "prefix_domain_rank": PREFIX_DOMAIN_RANK,
        "prefix_default": dict(PREFIX_DEFAULT_COUNTS),
        "prefix_adapted": dict(PREFIX_ADAPTED_COUNTS),
        "prefix_all": dict(PREFIX_ALL_COUNTS),
        "count_is_invariant": VIOLATION_COUNT_IS_INVARIANT,
        "row_slices": dict(PREFIX_ROW_SLICES),
        "interior_obstruction": INTERIOR_OBSTRUCTION_RANK,
        "interior_nullities": dict(INTERIOR_NULLITIES),
        "interior_domain_rank": INTERIOR_DOMAIN_RANK,
        # E -- the descent.
        "quotient_dim": QUOTIENT_DIM,
        "quotient_symmetry": QUOTIENT_GRAM_SYMMETRY_RESIDUAL,
        "quotient_signs": QUOTIENT_MINOR_SIGNS,
        "shifted_symmetric_signs": SHIFTED_SYMMETRIC_MINOR_SIGNS,
        "operator_residual": OPERATOR_DEFINITION_RESIDUAL,
        "light_factors": dict(LIGHT_FACTORS),
        "heavy_factors": dict(HEAVY_FACTORS),
        "factor_multiplicity": FACTOR_MULTIPLICITY,
        "monic_scalars": dict(MONIC_SCALARS),
        "monic_is_leading_squared": MONIC_SCALAR_IS_LEADING_SQUARED,
        "monic_residual": MONIC_RESIDUAL,
        "landed_w_residuals": LANDED_W_RESIDUALS,
        "core_section_is_landed_w": CORE_SECTION_IS_LANDED_W,
        # F -- the sector theorem.
        "isometry_residual": ISOMETRY_RESIDUAL,
        "commutation_residual": COMMUTATION_RESIDUAL,
        "cross_residuals": CROSS_BLOCK_RESIDUALS,
        "light_defect_rank": LIGHT_DEFECT_RANK,
        "light_defect_residual": LIGHT_DEFECT_RESIDUAL,
        "light_self_adjoint": LIGHT_SELF_ADJOINT_RESIDUAL,
        "light_gram_signs": LIGHT_GRAM_MINOR_SIGNS,
        "light_form_signs": LIGHT_FORM_MINOR_SIGNS,
        "light_discriminants": dict(LIGHT_DISCRIMINANTS),
        "light_trace_exceeds_two": LIGHT_TRACE_EXCEEDS_TWO,
        "light_root_product": LIGHT_ROOT_PRODUCT,
        "heavy_defect_rank": HEAVY_DEFECT_RANK,
        "heavy_defect_residual": HEAVY_DEFECT_RESIDUAL,
        "heavy_gram_signs": HEAVY_GRAM_MINOR_SIGNS,
        "heavy_symmetric_signs": HEAVY_SYMMETRIC_MINOR_SIGNS,
        "defect_rank": DEFECT_RANK,
        "defect_entries": DEFECT_NONZERO_ENTRIES,
        "defect_projectors": DEFECT_PROJECTOR_RANKS,
        "defect_equivariance": DEFECT_EQUIVARIANCE_RESIDUALS,
        "section_residuals": SECTION_RESIDUALS,
        "scattered_is_permutation": SCATTERED_SECTION_U_IS_PERMUTATION,
        "wedge_residual": WEDGE_RESIDUAL,
        "wedge_scale": DEFECT_SCALE,
        "wedge_integer_matrix": DEFECT_INTEGER_MATRIX,
        "wedge_left": WEDGE_U,
        "wedge_right": WEDGE_V,
        "wedge_norms": (WEDGE_U_NORM, WEDGE_V_NORM, WEDGE_INNER),
        "complex_structure": COMPLEX_STRUCTURE_RESIDUALS,
        "pairing_residuals": PAIRING_RESIDUALS,
        "parity_ranks": PARITY_COMPONENT_RANKS,
        "heavy_discriminant_is_square": HEAVY_DISCRIMINANT_IS_SQUARE,
        "purely_pairs_copies": DEFECT_PURELY_PAIRS_COPIES,
        # G -- the second point.
        "second_structure": SECOND_POINT_STRUCTURE,
        "second_polynomials_differ": SECOND_POINT_POLYNOMIALS_DIFFER,
        "second_prefix_ranks": dict(SECOND_POINT_PREFIX_RANKS),
        # H -- the note, the fence and the nsimplify absence.
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
    elif mutation == "claim_full_reconstruction":
        # THE NEGATIVE HALF DENIED: the descended operator is asserted to be
        # OS-self-adjoint on ALL of H.  It is not -- the heavy sector carries an
        # exact rank-two defect, and half the block is that failure.
        claims["full_reconstruction"] = True
    elif mutation == "claim_heavy_reading_licensed":
        # THE HEAVY theta ASSERTED TO BE OPERATOR CONTENT LIKE THE LIGHT ONE.
        claims["heavy_reading_licensed"] = True
    elif mutation == "claim_defect_pairs_copies":
        # THE READING ROUND TWO REFUTED, REASSERTED.
        claims["defect_pairs_copies"] = True
    elif mutation == "claim_semigroup":
        claims["semigroup"] = True
    elif mutation == "claim_physical_mass":
        claims["physical_mass"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_hilbert_rank":
        claims["hilbert_rank"] = 9
    elif mutation == "break_gram_symmetry":
        claims["gram_symmetry"] = 1
    elif mutation == "break_psd_certificate":
        claims["schur_residual"] = 1
    # --- D ----------------------------------------------------------------
    elif mutation == "break_prefix_ranks":
        claims["prefix_ranks"] = {16: (1, 1, 1), 20: (2, 1, 1)}
    elif mutation == "break_basis_dependence":
        # THE CORRECTION DENIED: the violating-vector count is asserted to be an
        # invariant of the kernel, i.e. all three presentations agree.
        claims["count_is_invariant"] = True
        claims["prefix_adapted"] = dict(PREFIX_DEFAULT_COUNTS)
        claims["prefix_all"] = dict(PREFIX_DEFAULT_COUNTS)
    elif mutation == "break_row_slices":
        claims["row_slices"] = {16: (1, 2, 3, 4, 5, 6), 20: PREFIX_ROW_SLICES[20]}
    elif mutation == "break_interior_loophole":
        # THE LOOPHOLE DENIED: the obstruction is asserted to survive on the
        # interior windows, which is the solve's original no-go.
        claims["interior_obstruction"] = 1
    # --- E ----------------------------------------------------------------
    elif mutation == "break_quotient_dimension":
        claims["quotient_dim"] = 7
    elif mutation == "break_monic_normalization":
        claims["monic_scalars"] = {point: 1 for point in POINTS}
        claims["monic_is_leading_squared"] = False
    elif mutation == "break_bulk_monodromy":
        broken = dict(LIGHT_FACTORS)
        broken[SECOND_POINT] = (233, -691, 233)
        claims["light_factors"] = broken
    elif mutation == "break_core_section":
        claims["landed_w_residuals"] = (1, 0)
    elif mutation == "break_form_positivity":
        claims["shifted_symmetric_signs"] = (1, 1, 1, 1, 1, 1, 1, -1)
    # --- F ----------------------------------------------------------------
    elif mutation == "break_sector_orthogonality":
        claims["cross_residuals"] = (0, 1)
    elif mutation == "break_light_symmetry":
        claims["light_defect_residual"] = 1
        claims["light_self_adjoint"] = 1
    elif mutation == "break_light_positivity":
        claims["light_form_signs"] = (1, 1, 1, -1)
    elif mutation == "break_light_spectrum":
        broken = dict(LIGHT_DISCRIMINANTS)
        broken[FIXTURE] = LIGHT_DISCRIMINANTS[FIXTURE] + 1
        claims["light_discriminants"] = broken
    elif mutation == "break_defect_rank":
        claims["heavy_defect_rank"] = 4
        claims["defect_rank"] = 4
    elif mutation == "break_defect_localization":
        claims["defect_projectors"] = (0, 1, 1, 0)
    elif mutation == "break_section_independence":
        claims["section_residuals"] = (0, 1, 0, 0)
    elif mutation == "break_pairing_fence":
        # THE FENCE DROPPED: the defect is asserted to pair the two canonical
        # momentum-degenerate copies, i.e. S^T D S = D.
        claims["pairing_residuals"] = (0, 8)
        claims["parity_ranks"] = (2, 0)
        claims["purely_pairs_copies"] = True
    # --- G ----------------------------------------------------------------
    elif mutation == "break_second_point_structure":
        claims["second_structure"] = (
            1, 0, 2, (0, 2, 0, 0), 0, 2)
    elif mutation == "break_second_point_polynomials":
        claims["second_polynomials_differ"] = False
    elif mutation == "break_second_point_prefix":
        claims["second_prefix_ranks"] = {16: (2, 2, 1), 20: (2, 1, 1)}
    # --- H ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    packages = facts.packages
    prefixes = facts.prefixes
    wedge = facts.wedge
    primary = tuple((width, FIXTURE) for width in WIDTHS)
    every = tuple((width, point) for point in POINTS for width in WIDTHS)

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 194 artifacts are "
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
        "B-3", "THE RECONSTRUCTION IS PARTIAL AND THIS BLOCK SAYS SO FIRST: "
        "the descended operator is self-adjoint on the LIGHT sector only, the "
        "HEAVY sector carries an exact rank-two defect that nothing here "
        "removes, and a complete OS reconstruction of the two-slice evolution "
        "on all of H is NOT claimed",
        claims["full_reconstruction"] is False)
    checks.check(
        "B-4", "THE HEAVY READING STAYS A READING: only the light sector's "
        "theta is licensed as the spectrum of an OS-self-adjoint positive "
        "operator; the heavy theta remains a property of a non-self-adjoint "
        "matrix and is NOT licensed as operator content",
        claims["heavy_reading_licensed"] is False)
    checks.check(
        "B-5", "THE DEGENERATE-COPY PAIRING IS REFUTED, NOT ASSUMED: the "
        "rank-two defect is heavy and U-equivariant, but it does NOT satisfy "
        "S^T D S = D and both S-parity components have rank four, so the "
        "stronger spectral reading is declared FALSE",
        claims["defect_pairs_copies"] is False)
    checks.check(
        "B-6", "NO SEMIGROUP AND NO GENERATOR: one fixed 8 x 8 rational matrix "
        "is measured, no family {T^n} is constructed, no logarithm is taken and "
        "no Hamiltonian is extracted",
        claims["semigroup"] is False)
    checks.check(
        "B-7", "NO PHYSICAL MASS: theta is a logarithm of an algebraic number "
        "attached to an exact rational matrix, 'heavy' and 'light' order two "
        "such numbers, and no particle, dispersion relation or energy is "
        "supplied",
        claims["physical_mass"] is False)
    checks.check(
        "B-8", "NO CONTINUUM AND NO LIMIT: two widths, two rational points, "
        "one profile at unit volume and one two-slice shift",
        claims["continuum_limit"] is False)

    # --- C: THE OS HILBERT SPACE -------------------------------------------
    checks.check(
        "C-1", f"the carrier closes and the full-span reflected Gram is "
        f"EXACTLY SYMMETRIC of EXACT RANK {claims['hilbert_rank']} at both "
        f"widths and both points: spans {claims['span_sizes']}, carrier ranks "
        f"{claims['carrier_ranks']}, nnz(K_AA - K_AA^T) = "
        f"{claims['gram_symmetry']}",
        all(packages[key].carrier_rank == claims["carrier_ranks"][key[0]]
            for key in every)
        and all(packages[key].span_size == claims["span_sizes"][key[0]]
                for key in every)
        and all(packages[key].gram_rank == claims["hilbert_rank"]
                for key in every)
        and all(packages[key].gram_symmetry == claims["gram_symmetry"]
                for key in every))
    checks.check(
        "C-2", f"and it is POSITIVE SEMIDEFINITE of that rank rather than "
        f"merely symmetric of it, certified with NO floating inertia call: the "
        f"eight-column frame has leading-minor signs {claims['frame_signs']} "
        f"and the exact Schur residual nnz(K_AA - K_AA E K_c^-1 E^T K_AA) is "
        f"{claims['schur_residual']} at both widths and both points",
        all(packages[key].frame_signs == claims["frame_signs"]
            for key in every)
        and all(packages[key].schur_residual == claims["schur_residual"]
                for key in every))
    checks.check(
        "C-3", f"the frame is an exact isometric section of the quotient: "
        f"nnz(V# E - I), nnz(P^2 - P), nnz(P^T K_AA - K_AA P) and "
        f"nnz(K_AA (I - P)) are {claims['projector_residuals']} for "
        f"V# = K_c^-1 E^T K_AA and P = E V#, at both widths and both points",
        all(packages[key].projector_residuals == claims["projector_residuals"]
            for key in every))

    # --- D: THE PREFIX OBSTRUCTION AND THE INTERIOR LOOPHOLE ---------------
    def prefix_tuple(width, point, field):
        return tuple(getattr(prefixes[(width, point, depth)], field)
                     for depth in PREFIX_DEPTHS[width])

    checks.check(
        "D-1", f"ON THE SEAM-ANCHORED PREFIX DOMAINS D = {{1..dmax}} THE SHIFT "
        f"DOES NOT DESCEND: at dmax = {PREFIX_DEPTHS[16]} and "
        f"{PREFIX_DEPTHS[20]} the INVARIANT obstruction rank(M_2 | ker K_AD) "
        f"is {claims['prefix_ranks'][16]} and {claims['prefix_ranks'][20]}, on "
        f"kernels of dimension {claims['prefix_nullities'][16]} and "
        f"{claims['prefix_nullities'][20]}, with rank(K_AD) = "
        f"{claims['prefix_domain_rank']} throughout -- the prefix already "
        f"spans the quotient, so this is a PRESENTATION failure",
        all(prefix_tuple(width, FIXTURE, "obstruction")
            == claims["prefix_ranks"][width] for width in WIDTHS)
        and all(prefix_tuple(width, FIXTURE, "nullity")
                == claims["prefix_nullities"][width] for width in WIDTHS)
        and all(prefixes[(width, FIXTURE, depth)].domain_rank
                == claims["prefix_domain_rank"]
                for width in WIDTHS for depth in PREFIX_DEPTHS[width]))
    checks.check(
        "D-2", f"THE SOLVE'S VIOLATION COUNTS WERE PRESENTATION-DEPENDENT, AND "
        f"THE CORRECTION IS A CONSTRUCTION: on the SAME kernel the default "
        f"presentation gives {claims['prefix_default'][16]} and "
        f"{claims['prefix_default'][20]} violating vectors, the ADAPTED "
        f"presentation gives {claims['prefix_adapted'][16]} and "
        f"{claims['prefix_adapted'][20]} -- exactly the invariant rank -- and "
        f"the ALL-VIOLATING presentation gives "
        f"{claims['prefix_all'][16]} and {claims['prefix_all'][20]} -- exactly "
        f"the nullity; all three are exact bases, so 'the count is an "
        f"invariant' is {claims['count_is_invariant']}",
        all(prefix_tuple(width, FIXTURE, "default_count")
            == claims["prefix_default"][width] for width in WIDTHS)
        and all(prefix_tuple(width, FIXTURE, "adapted_count")
                == claims["prefix_adapted"][width] for width in WIDTHS)
        and all(prefix_tuple(width, FIXTURE, "all_count")
                == claims["prefix_all"][width] for width in WIDTHS)
        and all(prefixes[(width, FIXTURE, depth)].adapted_is_basis
                and prefixes[(width, FIXTURE, depth)].all_is_basis
                for width in WIDTHS for depth in PREFIX_DEPTHS[width])
        and (claims["prefix_adapted"] == claims["prefix_all"]
             == claims["prefix_default"]) == claims["count_is_invariant"])
    checks.check(
        "D-3", f"and what IS invariant under kernel-basis change is the "
        f"residual support, which meets EVERY positive slice at every depth: "
        f"{claims['row_slices'][16]} at T = 16 and {claims['row_slices'][20]} "
        f"at T = 20",
        all(prefixes[(width, FIXTURE, depth)].row_slices
            == claims["row_slices"][width]
            for width in WIDTHS for depth in PREFIX_DEPTHS[width]))
    checks.check(
        "D-4", f"THE INTERIOR LOOPHOLE, AND IT IS WHY THIS BLOCK EXISTS: on "
        f"D = {INTERIOR_WINDOWS[16]} at T = 16 and D = {INTERIOR_WINDOWS[20]} "
        f"at T = 20 the obstruction rank is EXACTLY "
        f"{claims['interior_obstruction']} on NONTRIVIAL kernels of dimension "
        f"{claims['interior_nullities'][16]} and "
        f"{claims['interior_nullities'][20]}, with rank(K_AD) = "
        f"{claims['interior_domain_rank']} so the window surjects onto all of "
        f"H -- at both widths and both points",
        all(packages[key].obstruction == claims["interior_obstruction"]
            for key in every)
        and all(packages[key].nullity == claims["interior_nullities"][key[0]]
                for key in every)
        and all(packages[key].domain_rank == claims["interior_domain_rank"]
                for key in every))

    # --- E: THE DESCENT ----------------------------------------------------
    checks.check(
        "E-1", f"THE DESCENT EXISTS AND ITS GRAM IS A GENUINE INNER PRODUCT: "
        f"the quotient is {claims['quotient_dim']}-dimensional, "
        f"nnz(K_c - K_c^T) = {claims['quotient_symmetry']} and the eight "
        f"leading minors are {claims['quotient_signs']}, and the operator is "
        f"defined by nnz(K_c T_2 - M_2c) = {claims['operator_residual']}, at "
        f"both widths and both points",
        all(len(packages[key].reps) == claims["quotient_dim"] for key in every)
        and all(packages[key].quotient_symmetry == claims["quotient_symmetry"]
                for key in every)
        and all(packages[key].quotient_signs == claims["quotient_signs"]
                for key in every)
        and all(packages[key].operator_residual == claims["operator_residual"]
                for key in every))
    checks.check(
        "E-2", f"SHIFTED REFLECTION POSITIVITY HOLDS AS A FORM ON ALL OF H: "
        f"the symmetric part (M_2c + M_2c^T)/2 has leading-minor signs "
        f"{claims['shifted_symmetric_signs']} at both widths and both points, "
        f"so what fails on the heavy sector is SYMMETRY and not positivity",
        all(packages[key].shifted_symmetric_signs
            == claims["shifted_symmetric_signs"] for key in every))
    checks.check(
        "E-3", f"THE SPECTRUM OF THE DESCENDED OPERATOR IS THE LANDED BULK "
        f"MONODROMY: charpoly(T_2) factors over QQ into exactly the two Block "
        f"194 primitive palindromic quadratics, each of multiplicity "
        f"{claims['factor_multiplicity']}, at BOTH widths -- "
        f"{claims['light_factors'][FIXTURE]} and "
        f"{claims['heavy_factors'][FIXTURE]} at {FIXTURE}",
        all(packages[key].factors
            == tuple(sorted(((claims["light_factors"][key[1]],
                              claims["factor_multiplicity"]),
                             (claims["heavy_factors"][key[1]],
                              claims["factor_multiplicity"])),
                            key=lambda item: (len(item[0]), item[0])))
            for key in every))
    checks.check(
        "E-4", f"BLOCK 194's MONIC-NORMALIZATION CORRECTION IS CARRIED FORWARD "
        f"AS THE SAME FORMULA: the displayed integer product equals s times the "
        f"MONIC characteristic polynomial with s = (a_light a_heavy)^2 exactly "
        f"-- {claims['monic_scalars'][FIXTURE]} and "
        f"{claims['monic_scalars'][SECOND_POINT]} -- at polynomial residual "
        f"{claims['monic_residual']}",
        all(packages[key].monic_scalar == claims["monic_scalars"][key[1]]
            for key in every)
        and all(packages[key].monic_residual == claims["monic_residual"]
                for key in every)
        and all(packages[key].monic_is_leading_squared
                == claims["monic_is_leading_squared"] for key in every))
    checks.check(
        "E-5", f"AND THE DESCENDED OPERATOR IS THE LANDED ONE: taking the DEEP "
        f"PAIR CORE t0 = {DEEP_ODD_CORE} as the section reproduces Block 190's "
        f"K_c and L_2 entrywise at residuals "
        f"{claims['landed_w_residuals']}, so T_2 IS W = K_c^-1 L_2 in that "
        f"section -- the monodromy spectrum is OPERATOR content on the "
        f"interior window and not merely FRAME content",
        all(packages[key].sections["deep_core"]["landed_w"]
            == claims["landed_w_residuals"] for key in every)
        and claims["core_section_is_landed_w"] is True)

    # --- F: THE SECTOR THEOREM ---------------------------------------------
    checks.check(
        "F-1", f"THE MOMENTUM INVOLUTION SPLITS H ORTHOGONALLY: "
        f"nnz(U^T K_c U - K_c) = {claims['isometry_residual']}, "
        f"nnz(T_2 U - U T_2) = {claims['commutation_residual']}, and the two "
        f"{SECTOR_DIM}-dimensional eigenspaces are orthogonal for BOTH forms "
        f"at {claims['cross_residuals']}, at both widths and both points",
        all(packages[key].isometry_residual == claims["isometry_residual"]
            for key in every)
        and all(packages[key].commutation_residual
                == claims["commutation_residual"] for key in every)
        and all(packages[key].cross_residuals == claims["cross_residuals"]
                for key in every))
    checks.check(
        "F-2", f"THE LIGHT SECTOR IS A COMPLETE RECONSTRUCTION: the restricted "
        f"shifted form is EXACTLY SYMMETRIC at nnz(M_+ - M_+^T) = "
        f"{claims['light_defect_residual']} with defect rank "
        f"{claims['light_defect_rank']}, both K_+ and M_+ are POSITIVE-DEFINITE "
        f"with leading-minor signs {claims['light_gram_signs']} and "
        f"{claims['light_form_signs']}, and therefore T_+ = K_+^-1 M_+ obeys "
        f"nnz(K_+ T_+ - T_+^T K_+) = {claims['light_self_adjoint']} and is a "
        f"POSITIVE SELF-ADJOINT OPERATOR -- at both widths and both points",
        all(packages[key].sectors["light"].defect_rank
            == claims["light_defect_rank"] for key in every)
        and all(packages[key].sectors["light"].defect_residual
                == claims["light_defect_residual"] for key in every)
        and all(packages[key].sectors["light"].self_adjoint_residual
                == claims["light_self_adjoint"] for key in every)
        and all(packages[key].sectors["light"].gram_signs
                == claims["light_gram_signs"] for key in every)
        and all(packages[key].sectors["light"].form_signs
                == claims["light_form_signs"] for key in every))
    checks.check(
        "F-3", f"AND ITS SPECTRUM IS A POSITIVE RECIPROCAL PAIR, READ WITH NO "
        f"RADICAL EVER EVALUATED: charpoly(T_+) is the LIGHT quadratic squared, "
        f"the quadratic annihilates T_+ exactly, its discriminants are "
        f"{claims['light_discriminants'][FIXTURE]} and "
        f"{claims['light_discriminants'][SECOND_POINT]} -- both positive and "
        f"neither a perfect square -- its root product is "
        f"{claims['light_root_product']} and its trace exceeds 2, so the "
        f"eigenvalues are e^{{+/- theta_light}}, each of multiplicity two",
        all(packages[key].sectors["light"].factors
            == ((LIGHT_FACTORS[key[1]], FACTOR_MULTIPLICITY),) for key in every)
        and all(packages[key].sectors["light"].annihilated == 0
                for key in every)
        and all(quadratic_discriminant(LIGHT_FACTORS[point])
                == claims["light_discriminants"][point] for point in POINTS)
        and all(claims["light_discriminants"][point] > 0 for point in POINTS)
        and all(not is_perfect_square(claims["light_discriminants"][point])
                for point in POINTS)
        and all(LIGHT_FACTORS[point][2]
                == LIGHT_FACTORS[point][0] * claims["light_root_product"]
                for point in POINTS)
        and all((quadratic_trace(LIGHT_FACTORS[point]) > 2)
                == claims["light_trace_exceeds_two"] for point in POINTS))
    checks.check(
        "F-4", f"THE HEAVY SECTOR IS NOT: K_- and the symmetric part "
        f"(M_- + M_-^T)/2 are POSITIVE-DEFINITE at {claims['heavy_gram_signs']} "
        f"and {claims['heavy_symmetric_signs']} and charpoly(T_-) is the HEAVY "
        f"quadratic squared, but the antisymmetric defect has EXACT RANK "
        f"{claims['heavy_defect_rank']} at "
        f"{claims['heavy_defect_residual']} nonzero entries, so "
        f"nnz(K_- T_- - T_-^T K_-) = {claims['heavy_defect_residual']} and T_- "
        f"is NOT self-adjoint in the OS form",
        all(packages[key].sectors["heavy"].defect_rank
            == claims["heavy_defect_rank"] for key in every)
        and all(packages[key].sectors["heavy"].defect_residual
                == claims["heavy_defect_residual"] for key in every)
        and all(packages[key].sectors["heavy"].self_adjoint_residual
                == claims["heavy_defect_residual"] for key in every)
        and all(packages[key].sectors["heavy"].gram_signs
                == claims["heavy_gram_signs"] for key in every)
        and all(packages[key].sectors["heavy"].symmetric_signs
                == claims["heavy_symmetric_signs"] for key in every)
        and all(packages[key].sectors["heavy"].factors
                == ((HEAVY_FACTORS[key[1]], FACTOR_MULTIPLICITY),)
                for key in every))
    checks.check(
        "F-5", f"THE DEFECT IS EXACTLY LOCALIZED AND EXACTLY EQUIVARIANT: on "
        f"the whole quotient M_2c - M_2c^T has rank {claims['defect_rank']} "
        f"with {claims['defect_entries']} nonzero entries, its "
        f"spectral-projector ranks in the order (+,+), (-,-), (+,-), (-,+) are "
        f"{claims['defect_projectors']} -- ZERO on the light sector, TWO on the "
        f"heavy one and ZERO on both cross blocks -- and "
        f"nnz(U^T D U - D), nnz(U D - D U) are "
        f"{claims['defect_equivariance']}, at both widths and both points",
        all(packages[key].defect_rank == claims["defect_rank"] for key in every)
        and all(packages[key].defect_entries == claims["defect_entries"]
                for key in every)
        and all(packages[key].defect_projectors == claims["defect_projectors"]
                for key in every)
        and all(packages[key].defect_equivariance
                == claims["defect_equivariance"] for key in every))
    checks.check(
        "F-6", f"AND NONE OF IT IS A PIVOT ARTIFACT: two DECLARED alternative "
        f"sections -- the deep pair core at slices {CORE_SECTION_TIMES} and a "
        f"SCATTERED eight-cell section whose induced involution is a coordinate "
        f"permutation: {claims['scattered_is_permutation']} -- give nonzero "
        f"change-of-section determinant and residuals "
        f"{claims['section_residuals']} for the K congruence, the M congruence, "
        f"the T_2 similarity and U_alt^2 - I, with light defect rank "
        f"{claims['light_defect_rank']}, heavy defect rank "
        f"{claims['heavy_defect_rank']} and both positivity certificates "
        f"UNCHANGED",
        all(packages[key].sections[label]["determinant_nonzero"]
            and packages[key].sections[label]["residuals"]
            == claims["section_residuals"]
            and packages[key].sections[label]["light"].defect_rank
            == claims["light_defect_rank"]
            and packages[key].sections[label]["heavy"].defect_rank
            == claims["heavy_defect_rank"]
            and packages[key].sections[label]["light"].form_signs
            == claims["light_form_signs"]
            and packages[key].sections[label]["heavy"].symmetric_signs
            == claims["heavy_symmetric_signs"]
            for key in every for label in ALTERNATIVE_SECTIONS[key[0]])
        and all(packages[key].sections["scattered"]["u_is_permutation"]
                == claims["scattered_is_permutation"] for key in every))
    checks.check(
        "F-7", f"THE DEFECT'S EXACT SHAPE, OVER QQ AND WITH NO NORMALISATION: "
        f"in the declared heavy basis at T = 16 and {FIXTURE} it is the "
        f"rational multiple s J of the declared integer skew matrix, and it "
        f"factors as the wedge gamma (u v^T - v u^T) with gamma = -s, "
        f"u = {claims['wedge_left']}, v = {claims['wedge_right']}, "
        f"(u.u, v.v, u.v) = {claims['wedge_norms']} and reconstruction residual "
        f"{claims['wedge_residual']}",
        wedge.scale == claims["wedge_scale"]
        and wedge.integer_matrix == claims["wedge_integer_matrix"]
        and wedge.gamma == -claims["wedge_scale"]
        and wedge.left == claims["wedge_left"]
        and wedge.right == claims["wedge_right"]
        and (wedge.left_norm, wedge.right_norm, wedge.inner)
        == claims["wedge_norms"]
        and wedge.residual == claims["wedge_residual"])
    checks.check(
        "F-8", f"AND THE STRONGER READING IS REFUTED, WHICH IS THE ROUND-2 "
        f"FENCE: the heavy discriminant "
        f"{HEAVY_DISCRIMINANTS[FIXTURE]} is a perfect square: "
        f"{claims['heavy_discriminant_is_square']}, so the heavy module is two "
        f"copies of ONE irreducible quadratic module; the one-site shift "
        f"restricted to the heavy sector is an exact commuting complex "
        f"structure at {claims['complex_structure']}; and yet "
        f"nnz(S^T D S - D), nnz(S^T D S + D) are {claims['pairing_residuals']} "
        f"and the S-even and S-odd components have ranks "
        f"{claims['parity_ranks']}, so 'the defect purely pairs the two "
        f"degenerate copies' is {claims['purely_pairs_copies']}",
        wedge.discriminant == HEAVY_DISCRIMINANTS[FIXTURE]
        and wedge.discriminant_is_square
        == claims["heavy_discriminant_is_square"]
        and wedge.complex_structure == claims["complex_structure"]
        and wedge.pairing_residuals == claims["pairing_residuals"]
        and wedge.parity_ranks == claims["parity_ranks"]
        and (claims["pairing_residuals"][0] == 0)
        == claims["purely_pairs_copies"])

    # --- G: THE SECOND POINT -----------------------------------------------
    second = tuple((width, SECOND_POINT) for width in WIDTHS)
    checks.check(
        "G-1", f"THE SECTORED STRUCTURE PERSISTS AT {SECOND_POINT} AT BOTH "
        f"WIDTHS: (obstruction, nnz(K_c - K_c^T), defect rank, projector "
        f"ranks, light defect rank, heavy defect rank) = "
        f"{claims['second_structure']}, with K_c and both sector certificates "
        f"positive-definite exactly as at the fixture",
        all((packages[key].obstruction, packages[key].quotient_symmetry,
             packages[key].defect_rank, packages[key].defect_projectors,
             packages[key].sectors["light"].defect_rank,
             packages[key].sectors["heavy"].defect_rank)
            == claims["second_structure"] for key in second)
        and all(packages[key].quotient_signs == QUOTIENT_MINOR_SIGNS
                for key in second)
        and all(packages[key].sectors["light"].form_signs
                == LIGHT_FORM_MINOR_SIGNS for key in second)
        and all(packages[key].sectors["heavy"].symmetric_signs
                == HEAVY_SYMMETRIC_MINOR_SIGNS for key in second))
    checks.check(
        "G-2", f"WHILE THE POLYNOMIALS MOVE, WHICH IS THE OTHER HALF OF THE "
        f"STATEMENT: the light and heavy quadratics are "
        f"{LIGHT_FACTORS[SECOND_POINT]} and {HEAVY_FACTORS[SECOND_POINT]} at "
        f"{SECOND_POINT} against {LIGHT_FACTORS[FIXTURE]} and "
        f"{HEAVY_FACTORS[FIXTURE]} at {FIXTURE}, with monic scalar "
        f"{MONIC_SCALARS[SECOND_POINT]} -- the structure is of the CLASS and "
        f"the coefficients are of the POINT: "
        f"{claims['second_polynomials_differ']}",
        all(packages[key].sectors["light"].factors
            == ((LIGHT_FACTORS[SECOND_POINT], FACTOR_MULTIPLICITY),)
            and packages[key].sectors["heavy"].factors
            == ((HEAVY_FACTORS[SECOND_POINT], FACTOR_MULTIPLICITY),)
            and packages[key].monic_scalar == MONIC_SCALARS[SECOND_POINT]
            for key in second)
        and ((LIGHT_FACTORS[SECOND_POINT] != LIGHT_FACTORS[FIXTURE]
              and HEAVY_FACTORS[SECOND_POINT] != HEAVY_FACTORS[FIXTURE])
             == claims["second_polynomials_differ"]))
    checks.check(
        "G-3", f"AND SO DOES THE PREFIX OBSTRUCTION: the invariant ranks at "
        f"{SECOND_POINT} are {claims['second_prefix_ranks'][16]} and "
        f"{claims['second_prefix_ranks'][20]}, identical to the fixture's, on "
        f"the same kernel dimensions and with the same all-slice residual "
        f"support -- the near-seam obstruction is a property of the "
        f"PRESENTATION and not of the point",
        all(prefix_tuple(width, SECOND_POINT, "obstruction")
            == claims["second_prefix_ranks"][width] for width in WIDTHS)
        and all(prefix_tuple(width, SECOND_POINT, "nullity")
                == PREFIX_NULLITIES[width] for width in WIDTHS)
        and all(prefixes[(width, SECOND_POINT, depth)].row_slices
                == PREFIX_ROW_SLICES[width]
                for width in WIDTHS for depth in PREFIX_DEPTHS[width]))

    # --- H: THE NOTE, THE FENCE AND THE NSIMPLIFY ABSENCE ------------------
    checks.check(
        "H-1", f"the note is present at {NOTE_PATH.name} and the N5 fence is "
        f"byte-identical there and in this runner",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "H-2", f"sp.nsimplify appears {facts.nsimplify_calls} times in this "
        f"runner's own source, MEASURED and not promised -- the hazard is a "
        f"rational TOLERANCE that maps a small nonzero rational to exactly "
        f"zero, and this block's entire negative half is an antisymmetric part "
        f"whose own scale is about 1.2e-19, so a single such call would ERASE "
        f"the rank-two defect and manufacture a complete reconstruction",
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
    print(f"  exact carrier inverses built and shared: {facts.inverse_count}")
    for point in POINTS:
        for width in WIDTHS:
            item = facts.packages[(width, point)]
            print(f"  (m, c) = ({point[0]}, {point[1]}), T = {width}")
            print(f"    rank(Q) {item.carrier_rank}, span {item.span_size}, "
                  f"rank(K_AA) {item.gram_rank}, nnz(K_AA - K_AA^T) "
                  f"{item.gram_symmetry}")
            print(f"    frame minors {item.frame_signs}, Schur residual "
                  f"{item.schur_residual}, projector residuals "
                  f"{item.projector_residuals}")
            print(f"    interior window {INTERIOR_WINDOWS[width]}: rank(K_AD) "
                  f"{item.domain_rank}, nullity {item.nullity}, obstruction "
                  f"{item.obstruction}")
            print(f"    representatives {item.reps}")
            print(f"    nnz(K_c - K_c^T) {item.quotient_symmetry}, K_c minors "
                  f"{item.quotient_signs}, Sym(M_2c) minors "
                  f"{item.shifted_symmetric_signs}, nnz(K_c T_2 - M_2c) "
                  f"{item.operator_residual}")
            print(f"    charpoly(T_2) factors {item.factors}")
            print(f"    monic scalar {item.monic_scalar} (= (a_l a_h)^2: "
                  f"{item.monic_is_leading_squared}), residual "
                  f"{item.monic_residual}")
            print(f"    nnz(U^T K_c U - K_c) {item.isometry_residual}, "
                  f"nnz(T_2 U - U T_2) {item.commutation_residual}, cross "
                  f"blocks {item.cross_residuals}")
            print(f"    defect rank {item.defect_rank}, entries "
                  f"{item.defect_entries}, projectors "
                  f"{item.defect_projectors}, equivariance "
                  f"{item.defect_equivariance}")
            for name in ("light", "heavy"):
                sector = item.sectors[name]
                print(f"    {name}: defect rank {sector.defect_rank}, defect "
                      f"nnz {sector.defect_residual}, self-adjointness "
                      f"residual {sector.self_adjoint_residual}, K minors "
                      f"{sector.gram_signs}, M minors {sector.form_signs}, "
                      f"Sym(M) minors {sector.symmetric_signs}")
                print(f"        charpoly {sector.factors}, quadratic "
                      f"annihilates: {sector.annihilated == 0}")
            for label, section in item.sections.items():
                print(f"    section {label}: det != 0 "
                      f"{section['determinant_nonzero']}, residuals "
                      f"{section['residuals']}, U is a permutation "
                      f"{section['u_is_permutation']}, landed-W residuals "
                      f"{section['landed_w']}")
    print("  THE PREFIX PRESENTATIONS")
    for point in POINTS:
        for width in WIDTHS:
            for depth in PREFIX_DEPTHS[width]:
                item = facts.prefixes[(width, point, depth)]
                print(f"    ({point[0]}, {point[1]}) T = {width}, "
                      f"D = {{1..{depth}}}: rank(K_AD) {item.domain_rank}, "
                      f"nullity {item.nullity}, INVARIANT obstruction rank "
                      f"{item.obstruction}; violating vectors -- default "
                      f"{item.default_count}, adapted {item.adapted_count}, "
                      f"all-violating {item.all_count} (both constructed "
                      f"presentations are bases: {item.adapted_is_basis} "
                      f"{item.all_is_basis}); residual slices "
                      f"{item.row_slices}")
    print("  THE HEAVY DEFECT, EXACTLY")
    print(f"    scale s = {facts.wedge.scale}")
    print(f"    integer skew matrix {facts.wedge.integer_matrix}")
    print(f"    gamma {facts.wedge.gamma}, u {facts.wedge.left}, v "
          f"{facts.wedge.right}, norms ({facts.wedge.left_norm}, "
          f"{facts.wedge.right_norm}), inner {facts.wedge.inner}, residual "
          f"{facts.wedge.residual}")
    print(f"    heavy discriminant {facts.wedge.discriminant}, perfect square "
          f"{facts.wedge.discriminant_is_square}")
    print(f"    complex structure (S^2 + I, [S, T_-]) "
          f"{facts.wedge.complex_structure}")
    print(f"    pairing residuals (S^T D S -/+ D) "
          f"{facts.wedge.pairing_residuals}, S-parity component ranks "
          f"{facts.wedge.parity_ranks}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}")
    print("  NOT CLAIMED: NO GRAVITY. NO COMPLETE RECONSTRUCTION -- THE HEAVY "
          "SECTOR'S RANK-TWO DEFECT IS NOT REMOVED. THE HEAVY READING IS NOT "
          "LICENSED. THE DEFECT DOES NOT PAIR THE DEGENERATE COPIES. NO "
          "SEMIGROUP AND NO GENERATOR. NO PHYSICAL MASS. NO CONTINUUM. TWO "
          "WIDTHS AND TWO RATIONAL POINTS ARE NOT A LIMIT.")
    print()


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE RECONSTRUCTION LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), THE FULL POSITIVE SPAN X_A over the slices {1..T/2-1} with its REFLECTED GRAM K_AA[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)] and its TWO-SLICE SHIFTED PAIRING M_2[a,b] = G[idx(t_b+2, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE SEAM-ANCHORED PREFIX DOMAINS D = {1..dmax} for dmax in {5, 4, 3} at T = 16 and {7, 6, 5} at T = 20, THE INTERIOR WINDOWS D = {2, 3, 4} at T = 16 and D = {2..6} at T = 20 CHOSEN BY THE ADVERSARIAL CHECK's OWN SCAN AND DERIVED FROM NOTHING, THE PIVOT SECTION of eight representative cells with its two DECLARED ALTERNATIVE SECTIONS, THE MOMENTUM INVOLUTION U as the two-site spatial shift and the ONE-SITE SHIFT S, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORDS OS RECONSTRUCTION AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, ON AN INTERIOR WINDOW AND ON ONE OF ITS TWO MOMENTUM SECTORS, THE TWO-SLICE SHIFT DESCENDS TO THE EIGHT-DIMENSIONAL QUOTIENT AS A POSITIVE SELF-ADJOINT OPERATOR -- AND ON THE OTHER SECTOR IT DOES NOT. THE RECONSTRUCTION IS PARTIAL AND THIS BLOCK SAYS SO FIRST. 'HILBERT SPACE' NAMES A RANK-EIGHT QUOTIENT OF A FINITE RATIONAL VECTOR SPACE BY THE RADICAL OF AN EXACT RATIONAL FORM, 'EVOLUTION' NAMES ONE FIXED 8 x 8 RATIONAL MATRIX AND NEVER A SEMIGROUP, 'SELF-ADJOINT' NAMES nnz(K T - T^T K) = 0 IN THAT FINITE FORM, 'POSITIVE' NAMES EXACT LEADING-MINOR SIGNS OF A SYMMETRIC RATIONAL MATRIX, and 'MASS' NAMES acosh(T/2) FOR A RATIONAL TRACE T > 2 AND THEREFORE A LOGARITHM OF AN ALGEBRAIC NUMBER. NO SEMIGROUP IS SUPPLIED, NO GENERATOR IS SUPPLIED, NO CONTINUUM TIME IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: TWO WIDTHS AND TWO RATIONAL POINTS ARE NOT A LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE OS HILBERT SPACE EXISTS AND IT IS EIGHT-DIMENSIONAL, AND THE PREFIX NO-GO OF THE SOLVE IS NARROWED BY THE ADVERSARIAL CHECK's OWN LOOPHOLE. The reflected Gram of the FULL positive span is EXACTLY SYMMETRIC at nnz(K_AA - K_AA^T) = 0 and has EXACT RANK 8 at T = 16 (28 x 28) and T = 20 (36 x 36) and at both (m, c) = (9/20, 5/13) and (1/2, 1/3), so H = X_A / rad(K_AA) is EIGHT-DIMENSIONAL; and it is POSITIVE SEMIDEFINITE OF RANK EIGHT rather than merely symmetric of rank eight, certified WITHOUT A FLOATING INERTIA CALL by an eight-column frame E whose compressed Gram K_c = E^T K_AA E has all EIGHT leading minors POSITIVE together with the EXACT SCHUR IDENTITY nnz(K_AA - K_AA E K_c^-1 E^T K_AA) = 0 and the projector identities nnz(V# E - I) = nnz(P^2 - P) = nnz(P^T K_AA - K_AA P) = nnz(K_AA (I - P)) = 0 for V# = K_c^-1 E^T K_AA and P = E V#. ON THE SEAM-ANCHORED PREFIX DOMAINS D = {1..dmax} THE TWO-SLICE SHIFT DOES NOT DESCEND: the invariant obstruction rank(M_2 | ker K_AD) is 2, 1, 1 at dmax = 5, 4, 3 and again 2, 1, 1 at dmax = 7, 6, 5, at BOTH widths and BOTH points, and the residual column support meets EVERY positive slice. THE SOLVE'S COUNTS OF VIOLATING KERNEL VECTORS WERE PRESENTATION-DEPENDENT AND THE CORRECTION IS CARRIED AS A CONSTRUCTION: in SymPy's default nullspace presentation the counts are 8, 6, 2 and 14, 12, 8, in an ADAPTED presentation of the SAME kernel -- pivot columns of M_2 N followed by ker(M_2 N) pulled back through N -- exactly rank many vectors violate, namely 2, 1, 1, and in an ALL-VIOLATING presentation obtained by adding one violating vector to every joint-null one, ALL of them violate, namely 12, 8, 4 and 20, 16, 12; all three presentations are exact bases of the same kernel, so THE COUNT IS NOT AN INVARIANT AND THE RANK IS. AND THE PREFIX PRESENTATION IS NOT THE QUOTIENT: on the INTERIOR windows D = {2, 3, 4} at T = 16 and D = {2..6} at T = 20 the obstruction rank is EXACTLY ZERO with kernels of dimension 4 and 12 -- nontrivial, not vacuous -- and rank(K_AD) = 8, so the window surjects onto all of H.\\nper_mode: THE DESCENT EXISTS ON THE INTERIOR WINDOW AND ITS SPECTRUM IS THE LANDED BULK MONODROMY. Because ker(K_AD) is contained in ker(M_2) on the interior window, the assignment [g] |-> [tau^2 g] is representative-independent and T_2 = q_A tau^2 q_D^-1 is a genuine operator on the whole eight-dimensional quotient; in the pivot section it is T_2 = K_c^-1 M_2c with nnz(K_c T_2 - M_2c) = 0. THE COMPRESSED GRAM IS A GENUINE INNER PRODUCT: nnz(K_c - K_c^T) = 0 with all eight leading minors POSITIVE. THE SHIFTED FORM IS POSITIVE AS A FORM: the symmetric part (M_2c + M_2c^T)/2 has all eight leading minors POSITIVE at both widths and both points, so shifted reflection positivity holds on H and what fails is SYMMETRY and not positivity. THE SPECTRUM IS NOT NEW CONTENT AND THAT IS THE POINT: charpoly(T_2) factors over QQ into exactly the two LANDED Block 194 primitive palindromic quadratics, each of multiplicity two, at BOTH widths -- (22569375 z^2 - 233631106 z + 22569375) and (39529825 z^2 - 109432706 z + 39529825) at (9/20, 5/13), and (233 z^2 - 690 z + 233) and (739 z^2 - 7258 z + 739) at (1/2, 1/3) -- and BLOCK 194's MONIC-NORMALIZATION CORRECTION IS CARRIED FORWARD AS THE SAME FORMULA rather than re-committed: the product of those factors equals s times the MONIC characteristic polynomial with s = (a_light a_heavy)^2 exactly, s = 795955611005101889386962890625 and s = 29648362969, each at ZERO polynomial residual. AND THE OPERATOR IS THE LANDED ONE: taking the DEEP PAIR CORE t0 = 3 as the section reproduces Block 190's K_c and L_2 entrywise, so the descended operator IS W = K_c^-1 L_2 in that section, with change-of-section congruence residuals nnz(K_alt - P^T K P) = nnz(M_alt - P^T M P) = 0 and similarity residual nnz(T_alt - P^-1 T_2 P) = 0. THE MONODROMY SPECTRUM IS THEREFORE OPERATOR CONTENT ON THE INTERIOR WINDOW AND NOT MERELY FRAME CONTENT, WHICH IS THE SOLVE'S OWN READING CORRECTED.\\nper_block: THE SECTOR THEOREM, AND IT IS THE BLOCK. The momentum involution U -- the two-site spatial shift -- is an EXACT ISOMETRY of the quotient Gram at nnz(U^T K_c U - K_c) = 0 and commutes with the descended operator at nnz(T_2 U - U T_2) = 0, and its two eigenspaces are ORTHOGONAL for both forms at nnz(b_+^T K_c b_-) = nnz(b_+^T M_2c b_-) = 0, so H splits as an ORTHOGONAL DIRECT SUM of a four-dimensional LIGHT sector U = +1 and a four-dimensional HEAVY sector U = -1 and the descended operator preserves each. ON THE LIGHT SECTOR THE RECONSTRUCTION IS COMPLETE: in the rational basis e_(t,0) + e_(t,2) and e_(t,1) + e_(t,3) the restricted shifted form is ENTRYWISE SYMMETRIC at nnz(M_+ - M_+^T) = 0, both K_+ and M_+ have all four leading minors POSITIVE, and therefore T_+ = K_+^-1 M_+ satisfies nnz(K_+ T_+ - T_+^T K_+) = 0 and is a POSITIVE SELF-ADJOINT OPERATOR for the inner product K_+; its characteristic polynomial is the LIGHT quadratic squared, its trace exceeds 2 with positive discriminant and unit root product, so its spectrum is the doubly degenerate positive reciprocal pair e^{+/- theta_light} -- 5725088884359936 and 258944 are the two discriminants and neither is a perfect square. ON THE HEAVY SECTOR IT IS NOT: K_- and the symmetric part (M_- + M_-^T)/2 both have all four leading minors POSITIVE and the characteristic polynomial is the HEAVY quadratic squared, but the antisymmetric defect D_- = M_- - M_-^T is NONZERO of EXACT RANK 2, so nnz(K_- T_- - T_-^T K_-) = 8 and T_- is NOT self-adjoint in the OS form. THE DEFECT IS ENTIRELY HEAVY AND EXACTLY LOCALIZED: on the whole quotient the defect M_2c - M_2c^T has rank 2 with 32 nonzero entries, and its spectral-projector ranks in the order (+,+), (-,-), (+,-), (-,+) are (0, 2, 0, 0) -- ZERO on the light sector, TWO on the heavy sector and ZERO on both cross blocks -- at both widths and both points. THAT SPLIT IS THE THEOREM: THE LIGHT MODE OF THE GRAVITATIONAL SECTOR HAS A RECONSTRUCTED POSITIVE SELF-ADJOINT TWO-SLICE EVOLUTION ON ITS SECTOR OF H, AND THE HEAVY MODE HAS AN EXACT RANK-TWO OBSTRUCTION TO ONE.\\nlattice_wide: THE DEFECT IS RANK TWO, HEAVY AND U-EQUIVARIANT -- AND IT IS NOT A PAIRING OF THE TWO DEGENERATE COPIES, WHICH IS THE ROUND-TWO FENCE. On the whole quotient the defect is EXACTLY U-EQUIVARIANT at nnz(U^T D U - D) = 0 and nnz(U D - D U) = 0. In the DECLARED heavy basis -e_(2,0) + e_(2,2), -e_(2,1) + e_(2,3), -e_(3,0) + e_(3,2), -e_(3,1) + e_(3,3) at T = 16 and (m, c) = (9/20, 5/13) it is the exact rational multiple s J of the integer skew matrix J with rows (0, 0, -499791697674660, 1588013041094501), (0, 0, 12377859914160, -39328790486076), (499791697674660, -12377859914160, 0, 0) and (-1588013041094501, 39328790486076, 0, 0), where s = 15412245266178664398193359375000000/12468368115055868578374473995988256597352642542544230293, and it admits the EXACT two-direction wedge factorization D_- = gamma (u v^T - v u^T) with gamma = -s, u = (0, 0, 2034493740, -6464298239), v = (-245659, 6084, 0, 0), u^T u = 45926316500837688721, v^T v = 60385359337, u^T v = 0 and ZERO reconstruction residual. THE STRONGER READING IS REFUTED AND THE REFUTATION IS GATED. The heavy rational module is two isomorphic copies of one irreducible quadratic module -- the heavy discriminant 52545986939220736 = 2^8 x 13 x 31 x 37 x 71 x 313^2 x 1979 is NOT a rational square -- and the ONE-SITE spatial shift restricted to the heavy sector is an EXACT commuting complex structure with nnz(S_-^2 + I) = 0 and nnz(S_- T_- - T_- S_-) = 0, which canonically distinguishes the two momentum copies after scalar extension. A defect that PURELY PAIRED those copies would satisfy S_-^T D_- S_- = D_-. IT DOES NOT: nnz(S_-^T D_- S_- - D_-) = 8 and nnz(S_-^T D_- S_- + D_-) = 8, and the S-even and S-odd components (D_- +/- S_-^T D_- S_-)/2 EACH have exact rank 4, so the rank-two cancellation mixes cross-copy and within-copy parts. THE ONLY BASIS-FREE STATEMENTS ARE THAT THE DEFECT IS RANK TWO, ENTIRELY HEAVY AND U-EQUIVARIANT; ITS BLOCK-OFF-DIAGONAL APPEARANCE IN THE DISPLAYED COORDINATES IS A COORDINATE FACT AND NOT A SPECTRAL THEOREM.\\nper_scope: THE SECTORED STRUCTURE IS NOT A PROPERTY OF THE PIVOT SECTION AND NOT A PROPERTY OF THE FIXTURE, AND WHAT REMAINS OPEN IS NAMED. TWO DECLARED ALTERNATIVE SECTIONS -- the deep pair core at slices {3, 4}, and a SCATTERED eight-cell section deliberately NOT closed under the displayed U -- reproduce every sector statement exactly: the change of section P has nonzero determinant, the congruence residuals for K and M and the similarity residual for T_2 are ZERO, the induced involution satisfies U_alt^2 = I exactly and for the scattered section is NOT a coordinate permutation, and the light defect rank 0, the heavy defect rank 2, both sector polynomials and all four positivity certificates are UNCHANGED. THE STRUCTURE PERSISTS AT THE SECOND POINT (m, c) = (1/2, 1/3) AT BOTH WIDTHS -- obstruction rank 0, K_c symmetric with eight positive minors, defect rank 2, projector ranks (0, 2, 0, 0), light form symmetric and positive-definite, heavy symmetric part positive-definite -- WHILE THE POLYNOMIALS CHANGE, from (39529825, -109432706) and (22569375, -233631106) to (233, -690) and (739, -7258): THE STRUCTURE IS OF THE CLASS AND THE COEFFICIENTS ARE OF THE POINT. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: no semigroup is constructed and no generator is extracted, so nothing here is a Hamiltonian; the heavy sector's rank-two defect is CHARACTERIZED and NOT REMOVED, and no mechanism explaining WHY it is rank two rather than four is offered; the interior windows are the adversarial check's own scan at two widths and no width-independent proof of the near-seam and far-seam boundary layers is supplied; the descent is measured on TWO widths and TWO rational points and a finite pair of widths is not a continuum; and whether any OTHER admissible domain presentation of the same quotient carries a self-adjoint heavy sector is NOT decided either way.\\nRESULT: ON THE SITE-GLUED WIDTH FAMILY AT T = 16 AND T = 20, THE EIGHT-DIMENSIONAL OS QUOTIENT H EXISTS AND IS POSITIVE SEMIDEFINITE OF RANK EIGHT, THE TWO-SLICE SHIFT FAILS TO DESCEND FROM THE SEAM-ANCHORED PREFIX PRESENTATIONS AT INVARIANT OBSTRUCTION RANKS 2, 1, 1 BUT DESCENDS EXACTLY FROM THE INTERIOR WINDOWS AT OBSTRUCTION RANK 0, AND THE DESCENDED OPERATOR -- WHOSE SPECTRUM IS THE LANDED BULK MONODROMY AND WHICH IS THE LANDED W IN THE DEEP PAIR-CORE SECTION -- SPLITS ALONG THE MOMENTUM INVOLUTION INTO A LIGHT SECTOR ON WHICH IT IS A POSITIVE SELF-ADJOINT OPERATOR AND A HEAVY SECTOR ON WHICH ITS SELF-ADJOINTNESS DEFECT IS EXACTLY RANK TWO. The prefix violation counts of the solve are corrected to invariant ranks by an explicit three-presentation construction; the solve's bulk-distributed and width-persistent reading is corrected to a NEAR-SEAM artifact of the prefix presentation; the solve's conclusion that NO descended two-step evolution exists on H is REFUTED and replaced by the sectored statement; the solve's reading that the monodromy spectrum is FRAME content and not OPERATOR content is corrected on the interior window; and the reading that the rank-two defect pairs the two momentum-degenerate copies is REFUTED and fenced. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-194 STAND EXACTLY AS LANDED. BLOCK 190 IS NOT CORRECTED: its refutation of the naive OS transfer pairing was a statement about PAIR CORES, which are positive-definite frames carrying no quotient, and this block's sectored result on the QUOTIENT neither contradicts it nor repairs it. BLOCK 194 IS NOT CORRECTED: its monic-normalization identity is carried forward here as the same formula. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: TWO widths, TWO rational points, ONE profile at unit volume, ONE interior window per width and ONE two-slice shift -- not a scan, not a limit and not a semigroup; the interior windows were found by the adversarial check's scan and are IMPOSED here rather than derived; the boundary-layer mechanism that makes near-seam and far-seam windows fail is NOT proved; the heavy defect's rank two is MEASURED and its mechanism is NOT explained; and the positivity certificates are leading-minor sign tests applied ONLY to matrices whose symmetry residual is measured ZERO in the same gate, because leading minors certify definiteness for a symmetric matrix and for nothing else. SIX ITEMS ARE FOLDED FROM THE TWO ADVERSARIAL CHECK ROUNDS AS CONTENT AND NOT AS ERRATA: round one's C2 PRESENTATION-DEPENDENCE correction, carried as a three-presentation construction; round one's INTERIOR-WINDOW LOOPHOLE, which is the reason this block exists; round one's N2 finding that the image-metric wall is DOWNSTREAM of the null-transport wall and must be collapsed; round one's N-DISCIPLINE PARTIAL-NARROWING to the seam-anchored prefix presentations; round two's P1 BASIS-INDEPENDENCE, gated here as congruence and similarity on two declared alternative sections; and round two's P2 REFUTATION of the degenerate-copy pairing reading, gated here as the S-invariance residuals and the rank-four S-parity components. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE OS RECONSTRUCTION SOLVE (block 195 candidate), OSR PHASE 1 MEASURED, OSR PHASE 2 MEASURED, B195 CHECK VERDICT, OSR PHASE 3+4 MEASURED and B195 ROUND-2 VERDICT anchors.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
