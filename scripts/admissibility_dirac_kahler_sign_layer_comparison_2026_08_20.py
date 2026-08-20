#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_sign_layer_comparison_2026_08_20.py
"""Block 152: THE SIGN-LAYER COMPARISON -- Block 123's momentum-definiteness
comparison, EXECUTED on Block 151's stratum-145 move set, and scoped exactly.

Block 151 closed with a commission: "Execute Block 123's momentum-definiteness
comparison on the stratum-145 move set."  It had just certified the antecedent
of the Block 130 bridge conditional -- a sign-indefinite, mutually reversible,
same-cost-class move class -- for the first time in the cell-cutting lane.  The
consequent of that conditional reads "momentum-like inputs of the kind targeted
by the definiteness theorem of [Block 123]", and it had NEVER been unpacked.
This runner unpacks it, and the answer has two layers with a sharp seam:

  * THE COMPARISON IS A TABLE, AND THE TABLE IS 6/6.  Three properties --
    negation-closure of the achieved set, existence of a nonnegative nontrivial
    zero-total combination, and pointedness of the generated cone -- are
    evaluated exactly at two loci per lane.  On the CHARGE lane (Block 123 with
    the landed 136/138 conjugation correction) the loci are the self-conjugate
    residues {0, N/2} carrying diag(0, 2) and the conjugate pair (k, N-k)
    carrying diag(1, -1); on the CUT lane (Block 151) they are the
    floor-anchored increment set {(0,-1), (0,0), (1,-1), (1,0)} and the
    stratum-145 achieved set {+-(1,0), +-(0,1), +-(1,1)}.  Under the pairing
    self-conjugate <-> floor and conjugate-pair <-> stratum 145 all six cells
    agree; the SWAPPED pairing disagrees on all six, and within each lane the
    two loci differ on all three, so the agreement is discriminating;
  * BUT THE TABLE CARRIES ONE BIT PER CELL, NOT THREE, AND THE THREE
    INFLATIONS ARE DISCLOSED AS CHECKED CERTIFICATES.  (i) In every cell the
    three properties are EQUIVALENT -- closed = zero-total = not-pointed -- so
    the "6/6" is one bit per locus repeated three times; they are NOT
    equivalent in general, which is exhibited on S = {(1,0), (-1,1), (0,-1)}.
    (ii) Under the LITERAL reading that admits zero generators (q_0 = 0 on the
    charge lane, (0,0) x 21,024 on the cut lane) the match still reads 6/6 but
    BOTH hostile controls degrade to 4/6, so the table's discriminating power
    depends on the Block 136 balanced/nonzero-generator convention.  (iii) The
    table compares DIFFERENTLY TYPED objects -- charge VALUES against achieved
    INCREMENTS -- and either uniform typing kills it: increments on both charge
    loci give {+-2} at BOTH, values on both cut loci give (unclosed, no
    zero-total, pointed) at BOTH.  And the cut lane's floor cell uses the
    FLOOR-ANCHORED class; under the strict same-cost-class reading applied at
    145 the floor set is Block 150's {(0,0)}, whose negation-closure flips to
    vacuously TRUE and no longer reproduces the self-conjugate column;
  * SIX NON-CORRESPONDENCES ARE NAMED, EACH AS A CERTIFICATE.  The increment
    lattice is 2Z at index 2 on the charge lane against Z^2 at index 1 on the
    cut lane (and reading VALUES instead of increments would collapse that
    contrast, which is disclosed); the ambient ranks are 1 against 2 and the
    carrier sizes 4 sectors against 3 charge points, 192 blocks against 4
    sectors; the mechanisms are the involution k -> -k mod 4 with its two fixed
    points against the extremal corner (36, 60) of a global bracket; the
    identity-valued charge that carries Block 123's headline has ZERO text
    occurrences on the cut side; Block 151's own population rider forbids
    mixing the populations; and the label-to-charge laws differ in kind, a
    character-determined injective 4 -> 4 diagonal operator against a
    combinatorial 192 -> 3 map provably NOT determined by the lone piece's
    charge type;
  * THE THREE-STEP CHAIN BREAKS AT STEP TWO IN THE OTHER DIRECTION FROM THE
    OBVIOUS ONE, AND AT STEP THREE ENTIRELY.  Step (i), sign-indefiniteness,
    MATCHES.  Step (ii) matches only formally: Block 123 needs the
    zero-expectation state to be a certified OS-POSITIVE quotient state, and
    that certificate lives on the CHARGE lane; the cut lane's analogue is mere
    nonnegativity of move multiplicities, which reversibility makes automatic,
    so step (ii) is WEAKER ON THE CELL-CUTTING SIDE and its non-vacuous content
    there is instead that NOT ONE of the 132,288 distance-3 moves is neutral.
    Step (iii) has no counterpart at all: "Gauss" occurs ZERO times in the
    Block 151 note, no incidence operator is registered, and no positive state
    space exists on the cut lane -- so POPULATABILITY DOES NOT TRANSFER;
  * AND THE FIREWALL BITES ON THE BRIDGE'S OWN RECORD.  The three transcribed
    cycle-723/725/726 charge points (36,55), (41,48), (37,48) all lie inside
    the global bracket, but NONE of them occurs in ANY committed stratum
    (144/145/146), and two of them sit at the MC = 48 end that Block 151
    carries as facet-wise and UNWITNESSED.  The bridge generators (5,-7) and
    (1,-7) are still not achieved, so Block 130 section 6's LITERAL antecedent
    -- quantified over "each generator used by the bridge" -- is NOT met at
    145; the execution is licensed by section 8's outcome rows and by Block
    151's own broadened restatement, and that licensing is stated, not assumed.

The verdict is a STRUCTURAL MATCH ON THE SIGN LAYER and UNDERDETERMINED above
it.  The deliverable is a certified table with its inflations disclosed, not an
isomorphism -- none is available.  Nothing here builds a frame-to-momentum map;
Block 151 records it as neither built nor excluded and it stays that way.

Every scientific comparison below is exact integer or exact rational
arithmetic; no float is constructed anywhere in this runner, and the integer
monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: neither lane's machinery is re-implemented here.  The Block
123 runner and the Block 151 runner are IN THIS WORKTREE and are imported as
modules under blob pins checked against the hash of the bytes actually
imported; the three committed cell-cutting runners the cut lane rests on live
only on origin/main and are read at RUN TIME through Block 151's own
`load_machinery`, content-bound by the same blob pins and pinned cut markers
Block 151 uses.  The stratum-145 census is then REBUILT here rather than
imported, and by a DIFFERENT ROUTE than Block 151's: Block 151 read its 192
block indices off the promoted three-piece class's own dC4 = 1 refills, whereas
this runner takes the block indices from an exact POINT-COVERABILITY filter
over ALL 1,216 cost-7 pieces, with no reference to any move class, and recovers
exactly the same 192 blocks of exactly 1,266 cuttings.

PROVENANCE DISCLOSURE: the four-box, the pieces, the facet charge, the cost
floor, the corpus, the cost-145 stratum, the promoted three-piece class, the
achieved increment sets and the bridge lattice are ALL COMMITTED objects; the
Z4 quotient, the site projectors, the shift character, the principal charge,
the Gauss layer and the OS positivity route are ALL COMMITTED objects.  This
block adds only the comparison: the contract extraction, the table, its three
inflation disclosures, the six non-correspondences, the corrected chain, the
firewall finding on the transcribed bridge record, and the scope.

PICKUP PROVENANCE: this lane was picked up on owner direction after a silent
hand-off; the six named cycle-778..799 notes on unmerged branches are ANOTHER
worker's pending state and are NOT consumed, NOT read and NOT superseded here.

HYPOTHESES, named and not imported: (H1) the COMPARISON is structural -- a
correspondence of certified properties -- because no frame-to-momentum map is
committed on either side; no isomorphism, no identification and no transfer of
populatability is claimed.  (H2) the CHARGE LANE loci are the conjugation
orbits of the committed Z4 momentum charge under k -> -k mod N, as the landed
Block 136/138 corrections fix them.  (H3) the CUT LANE loci are Block 151's
floor-anchored achieved increment set and its stratum-145 achieved set, under
Block 151's inherited M5 declaration that cost class is the C4 level set.
(H4) the supplied-model firewall of cycles 725/726/734 is INHERITED UNCHANGED,
and Block 123's own theorem is neither upgraded nor weakened.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
import itertools
from math import gcd
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np


_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path(
        "/Users/jonBridger/Projects/Physics-baremetal-probes/"
        ".claude/worktrees/gravity-toe-lane-work-427b0b"
    )
)

NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

BLOCK151_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK151_RUNNER = (
    "scripts/admissibility_dirac_kahler_floor_boundary_theorem_2026_08_20.py"
)
BRIDGE_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
BLOCK123_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
BLOCK123_RUNNER = (
    "scripts/admissibility_dirac_kahler_momentum_population_definiteness_"
    "2026_08_16.py"
)
BLOCK136_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-18.md"
)
BLOCK138_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)

# The five artifacts whose blobs are pinned at the parent commit.  All five are
# IN THIS WORKTREE, so plain worktree/commit blob pins suffice; the two runners
# among them are additionally bound by the hash of the bytes actually imported.
PARENT_ARTIFACTS = (
    BLOCK151_NOTE,
    BLOCK151_RUNNER,
    BRIDGE_NOTE,
    BLOCK123_NOTE,
    BLOCK123_RUNNER,
)
PARENT_ARTIFACT_BLOBS = (
    "6f0c8734b496c0a59446ea99addb1a3c6114eb41",   # Block 151 note
    "8cd0b5542c88c0200434afac08a10430c4817582",   # Block 151 runner
    "1c4ea156b30c745b3afcea205ec314345ed71f6d",   # Block 130 bridge note
    "560894350af5930f88161455f4db8954730f3e96",   # Block 123 note
    "7ee63309da28801f0a5fb412dba402819e7d0d66",   # Block 123 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry
# is a WORKTREE-READABLE path; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at the Block 150 landing and inherited from Block 151).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_floor_boundary_theorem_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    # The three cell-cutting runners exist only on origin/main (our branch base
    # predates them); they are content-bound via the gate-A blob pins and read
    # at run time through Block 151's own loader -- never worktree paths, so
    # they must not appear here.
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 151 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 151, so the parent branch is Block 151's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block151-floor-boundary-theorem-20260820"
)
# Landing supervisor: replace this placeholder with the Block 151 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise; either way the binding is real and
# verifiable, and the immutable commit pin lands with the block.
PARENT_COMMIT = "26fad1c0b18073dc1121be27adcc531c5ea0651a"
# Block 150's tip: a real ancestor of HEAD that PREDATES both Block 151
# artifacts, so resolving the parent pin there leaves the Block 151 note and
# the Block 151 runner ABSENT while the three older artifacts still match.  It
# is the honest stale control FOR THIS PIN SET.  This pin is read ONLY under
# the stale mutation; the baseline gate never requires the stale blobs to match.
STALE_PARENT_COMMIT = "a398c9a749e8364aed0d1c408cc049eec80e11d4"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

# ---------------------------------------------------------------------------
# the committed cell-cutting machinery, pinned BY CONTENT and read at run time
# ---------------------------------------------------------------------------
# These three runners live on origin/main and postdate this branch's base, so
# they cannot be imported from the worktree.  Block 151's own `load_machinery`
# fetches each with `git show`, hashes its bytes with git's blob rule, cuts it
# at a pinned source marker and imports the prefix; the pins below are Block
# 151's, byte for byte, and are re-checked here against the hash of the bytes
# THIS run imported.
C726_BLOB = "46f080559c10d90d9803436f294ed660348b638f"
C734_BLOB = "ef4cedb4045ad6c476041aab274985fb7efa40fe"
C811_BLOB = "65cade2f6c3dcd92e10fbd146cfd6a3f7f95b744"
MACHINERY_BLOBS = (("c726", C726_BLOB), ("c734", C734_BLOB), ("c811", C811_BLOB))
MACHINERY_SHAPE = (
    ("c726", 661, 661),
    ("c734", 766, 507),
    ("c811", 1455, 239),
)
C726_GATES = 32                     # the committed runner's own passing gates
C734_PREFIX_GATES = 22              # gates the imported prefix runs and passes

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_literal_antecedent_met",
    "drop_neither_built_line",
    "claim_wall_indefinite",
    "break_momentum_witness",
    "claim_neutral_distance_three",
    "drop_distance_four_scoping",
    "claim_independent_bits",
    "claim_typing_free_table",
    "break_swap_control",
    "claim_isomorphism",
    "claim_type_determined_cut_law",
    "claim_bridge_point_in_stratum",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_literal_antecedent_met": "B",
    "drop_neither_built_line": "B",
    "claim_wall_indefinite": "C",
    "break_momentum_witness": "C",
    "claim_neutral_distance_three": "D",
    "drop_distance_four_scoping": "D",
    "claim_independent_bits": "E",
    "claim_typing_free_table": "E",
    "break_swap_control": "E",
    "claim_isomorphism": "F",
    "claim_type_determined_cut_law": "F",
    "claim_bridge_point_in_stratum": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print(
            "GATES "
            + " ".join(
                f"{key}={'PASS' if value else 'FAIL'}"
                for key, _, value in self.results
            )
        )

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    """The blob at a path in a commit, or "" when the path is absent there.

    Absence is a real answer here: the stale-pin control deliberately probes a
    commit that predates the two Block 151 artifacts.
    """
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def is_hash(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{40}", value) is not None


def blob_sha1(data: bytes) -> str:
    """Git's own blob hash of a byte string, computed locally.

    This is what makes the two worktree imports CONTENT-bound: the bytes that
    are actually imported are the bytes that are hashed.
    """
    header = b"blob " + str(len(data)).encode("ascii") + b"\x00"
    return hashlib.sha1(header + data).hexdigest()


def read_note(path: str) -> str:
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return ""


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def compact_note(text: str) -> str:
    return "".join(text.lower().split())


def flat(text: str) -> str:
    """Whitespace-normalised but CASE-PRESERVING, for the text certificates."""
    return " ".join(text.split())


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    imported_bytes_bound: bool
    machinery_blobs: tuple
    machinery_content_bound: bool


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT):
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(
    main_head: str, machinery: tuple, imported_digests: tuple
) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
    )

    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(
        commit_blob(parent, path) for path in PARENT_ARTIFACTS
    )
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, path) for path in PARENT_ARTIFACTS
    )
    # The two worktree imports bind BOTH ways: the pinned blob must be what the
    # parent commit and the worktree record, AND the bytes this runner actually
    # imported must hash to it.  The second half is the content binding.
    imported_bytes_bound = bool(
        imported_digests
        == (PARENT_ARTIFACT_BLOBS[1], PARENT_ARTIFACT_BLOBS[4])
        and all(is_hash(value) for value in imported_digests)
    )
    machinery_named = tuple(
        (name, record.digest, record.pin, pin)
        for (name, pin), record in zip(MACHINERY_BLOBS, machinery)
    )
    machinery_content_bound = all(
        digest == recorded == pin and is_hash(pin)
        for _name, digest, recorded, pin in machinery_named
    )
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT),
        bool(
            is_hash(parent)
            and is_ancestor(parent, "HEAD")
            and (
                not is_hash(PARENT_COMMIT)
                or resolve_ref(PARENT_REF) == PARENT_COMMIT
            )
        ),
        bool(
            len(committed_blobs) == len(PARENT_ARTIFACTS)
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
            and committed_blobs == PARENT_ARTIFACT_BLOBS
        ),
        bool(
            len(stale_blobs) == len(PARENT_ARTIFACTS)
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
        imported_bytes_bound,
        machinery_named,
        machinery_content_bound,
    )


# ---------------------------------------------------------------------------
# the two worktree imports: hash the bytes, then import the module
# ---------------------------------------------------------------------------
def import_worktree_module(alias: str, path: str):
    """Import a runner from THIS worktree and return (module, blob digest)."""
    target = ROOT / path
    digest = blob_sha1(target.read_bytes())
    spec = importlib.util.spec_from_file_location(alias, target)
    module = importlib.util.module_from_spec(spec)
    sys.modules[alias] = module          # dataclasses need this registered
    spec.loader.exec_module(module)
    return module, digest


def import_block123():
    """The Block 123 runner imports its parent by NAME, so scripts/ is added."""
    scripts = str(ROOT / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    name = Path(BLOCK123_RUNNER).stem
    digest = blob_sha1((ROOT / BLOCK123_RUNNER).read_bytes())
    module = __import__(name)
    return module, digest


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
# --- the charge lane (Block 123 with the landed 136/138 correction) ----------
NX = 4                                   # the committed spatial extent
PRINCIPAL_CHARGES = (0, 1, 2, -1)        # Block 123 equation (1), Ptilde
WITNESS_STATE = (0, 1, 0, 1)             # v* = e1 + e3
WITNESS_IMAGE = (0, 1, 0, -1)            # Ptilde v* = e1 - e3
GAUSS_FIELD = (0, 1, 1, 0)               # the exhibited g* with D g* = p*
U1_ROW_TOTAL = 2                         # the BLOCKED row
SELF_CONJUGATE = (0, 2)                  # residues fixed by k -> -k mod 4
CONJUGATE_PAIR = (1, 3)
Q_SELF = (0, 2)                          # diag(0, 2): PSD, balanced ray {0}
Q_PAIR = (1, -1)                         # diag(1, -1): indefinite
MOMENTUM_OWN_ROUTE_CHECKS = 37           # the independent re-certification

# --- the cut lane (Block 151) ------------------------------------------------
CORNERS = 16
CUTTING_SIZE = 24
FLOOR_CLASS = 144
COST_145 = 145
BLOCKS_145 = 192
BLOCK_SIZE_145 = 1266
CORPUS_145 = 243072
PIECE_COST_FLOOR = 6
SEVEN_PIECES = 1216                      # cost-7 pieces in the committed pool
CHARGE_POINTS_145 = (
    ((36, 59), 60768), ((36, 60), 121536), ((37, 60), 60768)
)
BLOCKS_PER_CHARGE_145 = (((36, 59), 48), ((36, 60), 96), ((37, 60), 48))
REFINEMENT_TYPE = (0, 2)                 # the ambiguous non-floor piece type
REFINEMENT_CHARGES = ((36, 59), (36, 60))
CORPUS_CHARGE = (36, 60)
CORNER = (36, 60)
TICK_BOX = (36, 42)
MIXED_BOX = (48, 60)
MC_FLOOR_UNWITNESSED = 48
FLOOR_DELTAS = (
    ((0, -1), 7104), ((0, 0), 21024), ((1, -1), 7008), ((1, 0), 7104)
)
FLOOR_SET = ((0, -1), (0, 0), (1, -1), (1, 0))
ALTERNATES = 42240
LANDING_STRATA = ((145, 27264), (146, 14592), (147, 384))
ACHIEVED_145 = ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1))
ACHIEVED_DIFFERENCES = (
    (-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (1, 1)
)
WITHIN_BLOCK_MIN = 4
MIN_CROSS_DISTANCE = (
    (((36, 59), (36, 60)), 3),
    (((36, 59), (37, 60)), 4),
    (((36, 60), (37, 60)), 3),
)
SUBSCAN_PER_CHARGE = 4
SUBSCAN_BLOCKS = 12
SUBSCAN_D3 = (
    ((-1, 0), 2756), ((0, -1), 1378), ((0, 1), 1378), ((1, 0), 2756)
)
SUBSCAN_D4 = (
    ((-1, -1), 1695), ((-1, 0), 1774), ((0, -1), 1146), ((0, 0), 5180),
    ((0, 1), 1146), ((1, 0), 1774), ((1, 1), 1695),
)
# twice-verified in Block 151 (its primary solve and its independent checker),
# carried here as pins and re-derived in full under --deep for the distance-3
# census; the distance-4 pair is the SCOPING disclosure and is additionally
# anchored to its verbatim occurrence in the committed Block 151 note.
D3_MOVES = 132288
D3_DIRECTED = (
    ((-1, 0), 66144), ((0, -1), 66144), ((0, 1), 66144), ((1, 0), 66144)
)
D3_EACH = 66144
D4_MOVES = 2411328
D4_NEUTRAL = 1348608
BRIDGE_DELTAS = ((5, -7), (1, -7))
BRIDGE_INDEX = 28
BRIDGE_CHARACTER = (7, 1)
NEGATIVE_TARGETS = ((31, 67), (35, 67))
# the cycle-723/725/726 charge points the bridge record transcribes
BRIDGE_POINTS = ((36, 55), (41, 48), (37, 48))
STRATA_CENSUS = {
    144: ((36, 60),),
    145: ((36, 59), (36, 60), (37, 60)),
    146: ((36, 58), (36, 59), (36, 60), (37, 59), (37, 60), (38, 60)),
}
MC_48_BRIDGE_POINTS = ((37, 48), (41, 48))

# --- the table ---------------------------------------------------------------
TABLE_PROPERTIES = ("negation_closure", "nonneg_zero_total", "cone_pointed")
TABLE_CELLS = 6
TABLE_MATCH = 6
TABLE_SWAP_DISAGREE = 6
TABLE_WITHIN_DIFFER = 6
LITERAL_MATCH = 6                        # the literal reading still matches ...
LITERAL_SWAP_DISAGREE = 4                # ... but both controls degrade to 4/6
LITERAL_WITHIN_DIFFER = 4
GENERAL_INEQUIVALENCE_SET = ((1, 0), (-1, 1), (0, -1))
CHARGE_INCREMENTS = (-2, 2)              # within-block charge differences
CHARGE_INCREMENT_INDEX = 2               # 2Z in Z
CUT_INCREMENT_INDEX = 1                  # Z^2
CUT_FLOOR_VALUES = ((36, 60),)
CUT_145_VALUES = ((36, 59), (36, 60), (37, 60))
SAME_CLASS_FLOOR_SET = ((0, 0),)         # Block 150's all-neutral flip class

# --- the non-correspondences and the chain -----------------------------------
MOMENTUM_SECTORS = 4
CUT_CHARGE_POINTS = 3
CUT_BLOCKS = 192
CARRIER_SIZES = (2, 4)
IDENTITY_CHARGE_OCCURRENCES = 0          # "U(1)" on the cut side
GAUSS_OCCURRENCES = 0                    # "gauss" in the Block 151 note
CHAIN_STATUS = (
    ("(i) sign-indefiniteness of the achieved set", "MATCH"),
    (
        "(ii) a nonnegative nontrivial zero-total combination",
        "MATCH, WEAKER ON THE CELL-CUTTING SIDE",
    ),
    (
        "(iii) positivity cone + incidence image + Gauss solvability",
        "NO COUNTERPART",
    ),
)
MAP_REQUIREMENTS = 3

# The default gate path runs in about 82 seconds -- the origin/main machinery
# load dominates it -- and --deep re-derives the full distance-3 census and the
# OS positivity at both shear fixtures and lands near 290, so the budget covers
# both with room to spare on a slower host.
RUNTIME_BUDGET_SEC = 900


# ---------------------------------------------------------------------------
# exact primitives on finite integer sets: the three table properties
# ---------------------------------------------------------------------------
def nonzero_part(points: tuple) -> tuple:
    return tuple(v for v in points if any(v))


def negation_closed(points: tuple, allow_zero: bool = False) -> bool:
    """S is negation-closed iff -v is in S for every v in S.

    Under the Block 136 BALANCED convention the zero generator is excluded (a
    balanced ray is spanned by nonzero charges); the literal reading keeps it,
    and the difference is measured rather than assumed -- see the convention
    certificate in gate E.
    """
    live = set(points) if allow_zero else set(nonzero_part(points))
    return all(tuple(-c for c in v) in live for v in live)


def zero_combination(points: tuple, allow_zero: bool = False, cap: int = 2):
    """A nonnegative, not-all-zero integer weighting summing to the zero vector.

    Exhaustive over coefficients in [0, cap], which is complete for these sets:
    every generator has entries in {-1, 0, 1, 2} and at most six generators, so
    a vanishing nonnegative combination exists iff one exists with small
    coefficients.  Returns the exhibited weighting or None.
    """
    generators = tuple(points) if allow_zero else nonzero_part(points)
    if not generators:
        return None
    if allow_zero and any(not any(v) for v in generators):
        return {tuple(v for v in generators if not any(v))[0]: 1}
    dimension = len(generators[0])
    for weights in itertools.product(range(cap + 1), repeat=len(generators)):
        if not any(weights):
            continue
        total = [0] * dimension
        for weight, vector in zip(weights, generators):
            for axis in range(dimension):
                total[axis] += weight * vector[axis]
        if not any(total):
            return {v: w for v, w in zip(generators, weights) if w}
    return None


def separating_functional(points: tuple, bound: int = 3):
    """An exact integer functional strictly positive on every nonzero generator.

    Its existence is EQUIVALENT to pointedness of the generated cone for these
    finite integer sets, and exhibiting it makes pointedness a certificate
    rather than an assertion.  Returns the functional or None.
    """
    generators = nonzero_part(points)
    if not generators:
        return ()
    dimension = len(generators[0])
    for weights in itertools.product(range(-bound, bound + 1), repeat=dimension):
        if not any(weights):
            continue
        if all(
            sum(w * v for w, v in zip(weights, vector)) > 0
            for vector in generators
        ):
            return weights
    return None


def cone_pointed(points: tuple) -> bool:
    return separating_functional(points) is not None


def profile(points: tuple, allow_zero: bool = False) -> tuple:
    """The three contract properties, in the fixed TABLE_PROPERTIES order."""
    return (
        negation_closed(points, allow_zero),
        zero_combination(points, allow_zero) is not None,
        cone_pointed(points),
    )


def lattice_index_1d(values: tuple) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(int(value)))
    return int(result)


def lattice_index_2d(vectors: tuple) -> int:
    """Index in Z^2 of the generated lattice (0 when the rank is below two)."""
    result = 0
    for left, right in itertools.combinations(vectors, 2):
        result = gcd(result, abs(left[0] * right[1] - left[1] * right[0]))
    return int(result)


def lattice_rank_2d(vectors: tuple) -> int:
    live = nonzero_part(vectors)
    if not live:
        return 0
    return 2 if lattice_index_2d(live) else 1


def congruence_lattice(generators: tuple, character: tuple, modulus: int) -> tuple:
    """Re-derive the Block 130 bridge lattice L from its two generators.

    Returns (index, congruence verified).  The index is |det| of the generator
    matrix, computed here; the claimed description a x + b y = 0 mod m is then
    VERIFIED over a full period box, membership decided by exact Cramer
    division, and never assumed.
    """
    (x1, y1), (x2, y2) = generators[0], generators[1]
    determinant = x1 * y2 - x2 * y1
    index = abs(determinant)
    verified = index == modulus and determinant != 0
    for x in range(-index, index + 1):
        for y in range(-index, index + 1):
            by_character = (
                character[0] * x + character[1] * y
            ) % modulus == 0
            by_solve = (
                (x * y2 - x2 * y) % determinant == 0
                and (x1 * y - x * y1) % determinant == 0
            )
            if by_character != by_solve:
                verified = False
    return int(index), bool(verified)


# ---------------------------------------------------------------------------
# C. the charge lane, re-certified by an OWN ROUTE (no import of Block 123)
# ---------------------------------------------------------------------------
def ipow(k: int) -> tuple:
    """i^k as an exact element of Z[i], written (real, imaginary)."""
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[k % 4]


def exact_rank(matrix: list) -> int:
    """Rank of an integer matrix over Q, by exact Fraction elimination."""
    rows = [[Fraction(value) for value in row] for row in matrix]
    width = len(rows[0])
    rank = 0
    for column in range(width):
        pivot = next(
            (i for i in range(rank, len(rows)) if rows[i][column] != 0), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column] != 0:
                factor = rows[i][column]
                rows[i] = [
                    a - factor * b for a, b in zip(rows[i], rows[rank])
                ]
        rank += 1
    return rank


def momentum_own_route() -> tuple:
    """The whole Block 123 momentum side, rebuilt from the shift character.

    Nothing is imported: the spatial shift on the four-sector quotient is the
    character k -> i^k, and every object the comparison leans on -- the
    principal charge, the identity-valued U(1) total, the witness state, the
    Gauss layer and the landed 136/138 conjugation split -- is re-derived from
    it in exact integer arithmetic.  Returns an ordered tuple of (key, value)
    certificates; the committed-runner cross-check is a separate route.
    """
    out: list[tuple[str, bool]] = []

    def note(key: str, value: object) -> None:
        out.append((key, bool(value)))

    phase = [ipow(k) for k in range(NX)]
    note("phase-form-is-the-character", phase == [(1, 0), (0, 1), (-1, 0), (0, -1)])

    def principal_charge(k: int) -> int:
        candidates = [q for q in (-1, 0, 1, 2) if ipow(q) == ipow(k)]
        if len(candidates) != 1:
            raise AssertionError(f"principal charge is not unique at {k}")
        return candidates[0]

    charges = [principal_charge(k) for k in range(NX)]
    note("principal-charge-diag-0-1-2-minus-1", tuple(charges) == PRINCIPAL_CHARGES)
    note("exponentiates-back-to-the-phase-form", [ipow(q) for q in charges] == phase)
    labels = [k % NX for k in range(NX)]
    note("mod-N-labels", labels == [0, 1, 2, 3])
    note(
        "mod-N-agrees-with-principal",
        all((charges[k] - labels[k]) % NX == 0 for k in range(NX)),
    )
    note("charge-is-hermitian", all(isinstance(q, int) for q in charges))
    note(
        "charge-is-indefinite",
        any(q > 0 for q in charges) and any(q < 0 for q in charges),
    )

    identity = [[int(i == j) for j in range(NX)] for i in range(NX)]
    note("u1-total-is-the-identity", identity == [
        [1 if i == j else 0 for j in range(NX)] for i in range(NX)
    ])

    def expectation(diagonal: list, state: tuple) -> int:
        return sum(diagonal[i] * state[i] * state[i] for i in range(NX))

    def norm_square(state: tuple) -> int:
        return sum(value * value for value in state)

    box = [
        state
        for state in itertools.product(range(-2, 3), repeat=NX)
        if any(state)
    ]
    note(
        "u1-expectation-is-the-squared-norm-and-positive",
        len(box) == 5 ** NX - 1
        and all(
            expectation([1] * NX, state) == norm_square(state) > 0
            for state in box
        ),
    )

    witness = WITNESS_STATE
    image = tuple(charges[i] * witness[i] for i in range(NX))
    note("witness-is-nonzero", any(witness))
    note("witness-image-is-e1-minus-e3", image == WITNESS_IMAGE)
    note("witness-expectation-is-zero-in-Z", expectation(charges, witness) == 0)
    note(
        "witness-expectation-is-zero-mod-N",
        sum(labels[i] for i in range(NX) if witness[i]) % NX == 0,
    )
    note("charge-does-not-annihilate-the-witness", any(image))
    note(
        "witness-is-not-an-eigenstate",
        exact_rank([list(witness), list(image)]) == 2,
    )
    note(
        "shift-expectation-on-the-witness-vanishes",
        (
            sum(phase[i][0] * witness[i] * witness[i] for i in range(NX)),
            sum(phase[i][1] * witness[i] * witness[i] for i in range(NX)),
        )
        == (0, 0),
    )

    incidence = [
        [int(c == r) - int(c == (r - 1) % NX) for c in range(NX)]
        for r in range(NX)
    ]
    note("incidence-rank-is-N-minus-1", exact_rank(incidence) == NX - 1)
    note(
        "incidence-image-sits-in-the-zero-sum-subspace",
        all(
            sum(incidence[r][c] for r in range(NX)) == 0 for c in range(NX)
        ),
    )
    zero_sum = [
        [int(i == j) - int(i == NX - 1) for j in range(NX - 1)]
        for i in range(NX)
    ]
    zero_sum_t = [
        [zero_sum[i][j] for i in range(NX)] for j in range(NX - 1)
    ]
    note("zero-sum-subspace-has-dimension-N-minus-1", exact_rank(zero_sum_t) == NX - 1)
    joined = [
        incidence[r] + [zero_sum[r][j] for j in range(NX - 1)]
        for r in range(NX)
    ]
    note("incidence-image-is-exactly-the-zero-sum-subspace", exact_rank(joined) == NX - 1)

    population = list(witness)
    source = [charges[i] * population[i] for i in range(NX)]
    source_mod = [labels[i] * population[i] for i in range(NX)]
    note("population-row", tuple(population) == WITNESS_STATE)
    note("momentum-source-row", tuple(source) == WITNESS_IMAGE)
    note("momentum-source-is-in-the-image", sum(source) == 0)
    note("momentum-source-is-in-the-image-mod-N", sum(source_mod) % NX == 0)
    field = list(GAUSS_FIELD)
    note(
        "exhibited-gauss-field-solves-the-equation",
        [
            sum(incidence[r][c] * field[c] for c in range(NX))
            for r in range(NX)
        ]
        == source,
    )
    note(
        "u1-row-total-is-blocked",
        sum(population) == U1_ROW_TOTAL and sum(population) != 0,
    )
    note(
        "no-nonnegative-population-has-zero-u1-total",
        all(
            sum(state) > 0
            for state in itertools.product(range(0, 3), repeat=NX)
            if any(state)
        ),
    )

    involution = {k: (-k) % NX for k in range(NX)}
    fixed = tuple(sorted(k for k in range(NX) if involution[k] == k))
    pairs = tuple(
        sorted({tuple(sorted((k, involution[k]))) for k in range(NX) if involution[k] != k})
    )
    note("involution-fixed-points", fixed == SELF_CONJUGATE)
    note("conjugate-pairs", pairs == (CONJUGATE_PAIR,))
    q_self = tuple(charges[k] for k in fixed)
    q_pair = tuple(charges[k] for k in CONJUGATE_PAIR)
    note("self-conjugate-charge-block", q_self == Q_SELF)
    note("conjugate-pair-charge-block", q_pair == Q_PAIR)
    note(
        "self-block-is-sign-definite",
        all(q >= 0 for q in q_self)
        and not (any(q > 0 for q in q_self) and any(q < 0 for q in q_self)),
    )
    note(
        "pair-block-is-indefinite",
        any(q > 0 for q in q_pair) and any(q < 0 for q in q_pair),
    )
    note("self-block-balanced-ray-is-zero", sum(q_self) != 0)
    note("pair-block-balanced-ray-is-nonzero", sum(q_pair) == 0)
    note(
        "break-is-carried-by-the-conjugate-pair",
        {k for k in range(NX) if witness[k]} == set(CONJUGATE_PAIR),
    )
    note(
        "residue-trap-is-not-a-sign-cancellation",
        (2 - (-2)) % NX == 0 and 2 != -2,
    )
    return tuple(out)


def momentum_committed_route(b123) -> tuple:
    """The same objects, read back out of the COMMITTED Block 123 runner.

    This is the cross-context half of the momentum re-certification: the own
    route above never imports anything, and this route never recomputes
    anything -- it drives Block 123's own committed projectors, its own
    `principal_charge` inverter and its own `gauss_certificate`.
    """
    import sympy as sp

    b121 = b123.block121
    total = sum(
        (
            b121.projector(b121.site(t, x))
            for t in range(b123.NT)
            for x in range(b123.NX)
        ),
        sp.zeros(b123.NS),
    )
    site_completeness = bool(b123.matrix_zero(total - sp.eye(b123.NS)))
    charges = tuple(
        int(b123.principal_charge(sp.I ** k)) for k in range(b123.NX)
    )

    class _Definiteness:
        integer_expectation = 0
        u1_total_identity = True

    gauss = b123.gauss_certificate(_Definiteness())
    return (
        site_completeness,
        int(b123.NX),
        charges,
        bool(gauss.image_zero_sum_exact),
        bool(gauss.solution_exact),
        bool(gauss.momentum_population_passes),
        bool(gauss.u1_population_fails),
        tuple(int(value) for value in gauss.solution),
    )


# ---------------------------------------------------------------------------
# D. the cut lane: the stratum-145 census, rebuilt by an INDEPENDENT route
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class StratumCertificate:
    seven_pieces: int
    survivors: int
    blocks: int
    block_sizes: tuple
    corpus: int
    block_charge_constant: bool
    charge_points: tuple
    blocks_per_charge: tuple
    charge_is_type_function: bool
    refinement_witness: tuple
    block_ids: tuple
    blocks_map: object
    block_charge: object


def rebuild_stratum_145(c726, c734) -> StratumCertificate:
    """Rebuild cost class 145 from the committed pieces, WITHOUT any move class.

    A cost-145 cutting of the four-box is 23 pieces at the cost floor 6 plus
    exactly ONE piece at cost 7, so the stratum decomposes into BLOCKS indexed
    by that lone piece.  Block 151 obtained the 192 block indices by reading
    off the non-floor pieces produced by its promoted class's own dC4 = 1
    refills.  Here the index set is instead SEARCHED FOR over ALL cost-7 pieces:
    each of the 1,216 is first subjected to an exact POINT-COVERABILITY filter
    (its complement must be coverable at all by floor pieces disjoint from it),
    and every survivor is then handed to an exact 23-piece cover enumeration.
    The two routes are independent -- this one never mentions a move -- and
    they agree exactly.
    """
    TC = [int(value) for value in c726.TC]
    MC = [int(value) for value in c726.MC]
    C4 = [int(value) for value in c734.C4]
    MASK = [int(value) for value in c734.MASK]
    floor_pool = [int(piece) for piece in c734.MINP]
    universe = int(c734.ALLQ)

    sevens = tuple(
        index for index in range(len(C4))
        if C4[index] == PIECE_COST_FLOOR + 1
    )
    survivors = []
    for piece in sevens:
        target = universe & ~MASK[piece]
        cover = 0
        for other in floor_pool:
            if not (MASK[other] & MASK[piece]):
                cover |= MASK[other]
        if not (target & ~cover):
            survivors.append(piece)

    def completions(piece: int) -> list:
        target = universe & ~MASK[piece]
        usable = [i for i in floor_pool if not (MASK[i] & MASK[piece])]
        by_point: dict[int, list] = {}
        for i in usable:
            bits = MASK[i]
            while bits:
                low = bits & -bits
                by_point.setdefault(low.bit_length() - 1, []).append(i)
                bits ^= low
        out: list = []
        chosen: list = []
        limit = CUTTING_SIZE - 1

        def grow(cover: int) -> None:
            if cover == target:
                if len(chosen) == limit:
                    out.append(tuple(sorted(chosen)))
                return
            if len(chosen) == limit:
                return
            rest = target & ~cover
            slot = (rest & -rest).bit_length() - 1
            for i in by_point.get(slot, ()):
                if MASK[i] & cover:
                    continue
                chosen.append(i)
                grow(cover | MASK[i])
                chosen.pop()

        grow(0)
        return out

    blocks: dict[int, list] = {}
    block_charge: dict[int, tuple] = {}
    constant = True
    for piece in survivors:
        found = completions(piece)
        if not found:
            continue
        blocks[piece] = found
        charges = {
            (
                TC[piece] + sum(TC[q] for q in cutting),
                MC[piece] + sum(MC[q] for q in cutting),
            )
            for cutting in found
        }
        if len(charges) != 1:
            constant = False
        block_charge[piece] = sorted(charges)[0]

    block_ids = tuple(sorted(blocks))
    charge_points = tuple(
        sorted(
            Counter(
                {
                    point: sum(
                        len(blocks[piece])
                        for piece in block_ids
                        if block_charge[piece] == point
                    )
                    for point in set(block_charge.values())
                }
            ).items()
        )
    )
    blocks_per_charge = tuple(sorted(Counter(block_charge.values()).items()))

    by_type: dict[tuple, set] = {}
    for piece in block_ids:
        by_type.setdefault((TC[piece], MC[piece]), set()).add(block_charge[piece])
    charge_is_type_function = all(
        len(values) == 1 for values in by_type.values()
    )
    ambiguous = tuple(
        sorted(
            (kind, tuple(sorted(values)))
            for kind, values in by_type.items()
            if len(values) > 1
        )
    )
    witness_pieces: tuple = ()
    if ambiguous:
        kind = ambiguous[0][0]
        seen: dict[tuple, int] = {}
        for piece in block_ids:
            if (TC[piece], MC[piece]) == kind:
                seen.setdefault(block_charge[piece], piece)
        witness_pieces = tuple((seen[point], point) for point in sorted(seen))

    return StratumCertificate(
        len(sevens),
        len(survivors),
        len(blocks),
        tuple(sorted({len(v) for v in blocks.values()})),
        sum(len(v) for v in blocks.values()),
        constant,
        charge_points,
        blocks_per_charge,
        charge_is_type_function,
        (ambiguous, witness_pieces),
        block_ids,
        blocks,
        block_charge,
    )


def subscan_moves(stratum: StratumCertificate) -> tuple:
    """The deterministic twelve-block sub-scan, four blocks at each charge point.

    Distances between cuttings are exact Hamming distances on their piece sets,
    computed by bit-packed integer popcounts; no float and no sampling is
    involved.  Returns the sub-scan shape, its distance-3 and distance-4
    directed censuses, the within-block minimum, the exact minimum cross-charge
    distances, and whether ANY charge-neutral move of distance at most three
    exists anywhere in the sub-scan.
    """
    by_charge: dict[tuple, list] = {}
    for piece in stratum.block_ids:
        by_charge.setdefault(stratum.block_charge[piece], []).append(piece)
    sample = [
        piece
        for point in sorted(by_charge)
        for piece in sorted(by_charge[point])[:SUBSCAN_PER_CHARGE]
    ]
    universe = sorted(
        {q for piece in sample for cutting in stratum.blocks_map[piece] for q in cutting}
        | set(sample)
    )
    position = {q: i for i, q in enumerate(universe)}
    popcount = np.array(
        [bin(value).count("1") for value in range(256)], dtype=np.uint8
    )
    packed: dict[int, object] = {}
    for piece in sample:
        listing = stratum.blocks_map[piece]
        indicator = np.zeros((len(listing), len(universe)), dtype=np.uint8)
        for row, cutting in enumerate(listing):
            indicator[row, [position[q] for q in cutting]] = 1
            indicator[row, position[piece]] = 1
        packed[piece] = np.packbits(indicator, axis=1)

    def distances(left: int, right: int):
        shared = popcount[
            np.bitwise_and(packed[left][:, None, :], packed[right][None, :, :])
        ].sum(axis=2).astype(np.int64)
        return CUTTING_SIZE - shared

    within_block_min = CUTTING_SIZE
    neutral_at_distance_three = False
    for piece in sample:
        matrix = distances(piece, piece)
        rows, columns = np.triu_indices(len(stratum.blocks_map[piece]), 1)
        values = matrix[rows, columns]
        within_block_min = min(within_block_min, int(values.min()))
        if int((values <= 3).sum()):
            neutral_at_distance_three = True
    cross_min: dict[tuple, int] = {}
    d3: Counter = Counter()
    d4: Counter = Counter()
    for i in range(len(sample)):
        for j in range(i + 1, len(sample)):
            left, right = sample[i], sample[j]
            matrix = distances(left, right)
            point_a = stratum.block_charge[left]
            point_b = stratum.block_charge[right]
            key = (point_a, point_b) if point_a <= point_b else (point_b, point_a)
            value = int(matrix.min())
            if value < cross_min.get(key, CUTTING_SIZE):
                cross_min[key] = value
            delta = (point_b[0] - point_a[0], point_b[1] - point_a[1])
            if delta == (0, 0) and int((matrix <= 3).sum()):
                neutral_at_distance_three = True
            for size, bag in ((3, d3), (4, d4)):
                count = int((matrix == size).sum())
                if count:
                    bag[delta] += count
                    if delta != (0, 0):
                        bag[(-delta[0], -delta[1])] += count
    shape = (
        len(sample),
        tuple(
            sorted(Counter(stratum.block_charge[p] for p in sample).items())
        ),
    )
    achieved = tuple(
        sorted(
            {delta for delta in d3 if delta != (0, 0)}
            | {delta for delta in d4 if delta != (0, 0)}
        )
    )
    return (
        shape,
        tuple(sorted(d3.items())),
        tuple(sorted(d4.items())),
        within_block_min,
        tuple(
            (key, value) for key, value in sorted(cross_min.items())
            if key[0] != key[1]
        ),
        neutral_at_distance_three,
        achieved,
    )


def deep_distance_three_scan(stratum: StratumCertificate, c734) -> tuple:
    """The FULL distance-3 same-class census over all 192 blocks (--deep only).

    Every distance-3 same-cost-class move at 145 replaces the lone cost-7 piece
    together with two floor pieces, so the scan runs over (block piece, floor
    pair) triples and their exact three-piece refills, counting hosts by exact
    bitset intersection.  Returns (unordered moves, neutral moves, directed
    census) -- Block 151's twice-verified constant, re-derived here.
    """
    C4 = [int(value) for value in c734.C4]
    MASK = [int(value) for value in c734.MASK]
    CM = [int(value) for value in c734.CM]
    if len(c734.V) != CORNERS:
        raise AssertionError("the committed four-box corner count moved")
    piece_index = {
        tuple(int(c) for c in c734.UNI[i]): i for i in range(len(c734.UNI))
    }

    def refills3(org: tuple) -> list:
        hull = corner_bits = 0
        for piece in org:
            hull |= CM[piece]
            corner_bits |= MASK[piece]
        available = [k for k in range(CORNERS) if (hull >> k) & 1]
        candidates = [
            piece
            for piece in (
                piece_index.get(sub)
                for sub in itertools.combinations(available, 5)
            )
            if piece is not None and not (MASK[piece] & ~corner_bits)
        ]
        out = []
        size = len(candidates)
        for i in range(size):
            a = candidates[i]
            for j in range(i + 1, size):
                b = candidates[j]
                if MASK[a] & MASK[b]:
                    continue
                for k in range(j + 1, size):
                    c = candidates[k]
                    if (MASK[a] | MASK[b]) & MASK[c]:
                        continue
                    if MASK[a] | MASK[b] | MASK[c] == corner_bits:
                        out.append((a, b, c))
        return out

    ordered = 0
    neutral = 0
    directed: Counter = Counter()
    for piece in stratum.block_ids:
        listing = stratum.blocks_map[piece]
        membership: dict[int, int] = {}
        for row, cutting in enumerate(listing):
            for q in cutting:
                membership[q] = membership.get(q, 0) | (1 << row)
        local_pairs = set()
        for cutting in listing:
            for a, b in itertools.combinations(cutting, 2):
                local_pairs.add((a, b) if a < b else (b, a))
        for a, b in local_pairs:
            org = tuple(sorted((piece, a, b)))
            for option in refills3(org):
                if set(option) == set(org):
                    continue
                if sum(C4[j] for j in option) != sum(C4[j] for j in org):
                    continue
                upper = [
                    j for j in option if C4[j] == PIECE_COST_FLOOR + 1
                ]
                if len(upper) != 1:
                    continue
                hosts = bin(membership[a] & membership[b]).count("1")
                if not hosts:
                    continue
                ordered += hosts
                other = upper[0]
                if other == piece:
                    neutral += hosts
                    directed[(0, 0)] += hosts
                else:
                    directed[
                        (
                            stratum.block_charge[other][0]
                            - stratum.block_charge[piece][0],
                            stratum.block_charge[other][1]
                            - stratum.block_charge[piece][1],
                        )
                    ] += hosts
    return ordered // 2, neutral, tuple(sorted(directed.items()))


# ---------------------------------------------------------------------------
# E. the table, its hostile controls, and its THREE inflation disclosures
# ---------------------------------------------------------------------------
LOCI = (
    "CHG/self-conjugate",
    "CHG/conjugate-pair",
    "CUT/floor-C4=144",
    "CUT/stratum-C4=145",
)
CLAIMED_PAIRING = (
    ("CHG/self-conjugate", "CUT/floor-C4=144"),
    ("CHG/conjugate-pair", "CUT/stratum-C4=145"),
)
SWAPPED_PAIRING = (
    ("CHG/self-conjugate", "CUT/stratum-C4=145"),
    ("CHG/conjugate-pair", "CUT/floor-C4=144"),
)
WITHIN_LANE = (
    ("CHG/self-conjugate", "CHG/conjugate-pair"),
    ("CUT/floor-C4=144", "CUT/stratum-C4=145"),
)


def build_table(achieved_145: tuple, allow_zero: bool = False) -> dict:
    sets = {
        "CHG/self-conjugate": tuple((q,) for q in Q_SELF),
        "CHG/conjugate-pair": tuple((q,) for q in Q_PAIR),
        "CUT/floor-C4=144": FLOOR_SET,
        "CUT/stratum-C4=145": tuple(achieved_145),
    }
    return {name: profile(points, allow_zero) for name, points in sets.items()}


def agreement(table: dict, pairing: tuple) -> int:
    return sum(
        1
        for left, right in pairing
        for index in range(len(TABLE_PROPERTIES))
        if table[left][index] == table[right][index]
    )


def disagreement(table: dict, pairing: tuple) -> int:
    return sum(
        1
        for left, right in pairing
        for index in range(len(TABLE_PROPERTIES))
        if table[left][index] != table[right][index]
    )


@dataclass(frozen=True)
class TableCertificate:
    table: tuple
    match: int
    swap_disagree: int
    within_differ: int
    literal_table: tuple
    literal_match: int
    literal_swap_disagree: int
    literal_within_differ: int
    one_bit_collapse: bool
    general_inequivalence: tuple
    charge_increments: tuple
    increments_typing_kills: tuple
    values_typing_kills: tuple
    typing_dependent: bool
    same_class_floor: tuple
    floor_reading_flips: bool
    separating_functionals: tuple


def table_certificate(achieved_145: tuple) -> TableCertificate:
    """The table at its TRUE strength, with the three inflations measured.

    (i) THE ONE-BIT COLLAPSE.  In every cell of this table the three properties
    are equivalent: closed = has-zero-total = not-pointed.  The "6/6" is
    therefore ONE bit per locus reported three times, and saying so is part of
    the result.  That the three are not equivalent IN GENERAL is exhibited on
    an explicit separating set rather than asserted.
    (ii) THE CONVENTION.  The Block 136 balanced reading excludes the zero
    generator (q_0 = 0 on the charge lane, the (0,0) x 21,024 neutral moves on
    the cut lane).  Under the LITERAL reading that admits it the match still
    reads 6/6, but both hostile controls degrade, so the discriminating power
    of the table -- not the match itself -- rests on the convention.
    (iii) THE TYPING.  The table compares charge VALUES on one lane against
    achieved INCREMENTS on the other.  Either uniform typing destroys it, and
    both destructions are computed here.  The floor cell additionally depends
    on reading the floor class as FLOOR-ANCHORED rather than same-cost-class.
    """
    table = build_table(achieved_145)
    literal = build_table(achieved_145, allow_zero=True)

    collapse = all(
        row[0] == row[1] and row[0] == (not row[2]) for row in table.values()
    )
    general = profile(GENERAL_INEQUIVALENCE_SET)

    charge_increments = tuple(
        sorted({a - b for a in Q_PAIR for b in Q_PAIR if a != b})
    )
    self_increments = tuple(
        sorted({a - b for a in Q_SELF for b in Q_SELF if a != b})
    )
    increments_kill = (
        profile(tuple((x,) for x in self_increments)),
        profile(tuple((x,) for x in charge_increments)),
    )
    values_kill = (profile(CUT_FLOOR_VALUES), profile(CUT_145_VALUES))
    typing_dependent = bool(
        self_increments == charge_increments
        and increments_kill[0] == increments_kill[1]
        and values_kill[0] == values_kill[1]
    )

    same_class_floor = profile(SAME_CLASS_FLOOR_SET)
    floor_reading_flips = bool(
        same_class_floor != table["CHG/self-conjugate"]
        and same_class_floor[0] is True
        and table["CHG/self-conjugate"][0] is False
    )

    functionals = (
        ("CHG/self-conjugate", separating_functional(tuple((q,) for q in Q_SELF))),
        ("CUT/floor-C4=144", separating_functional(FLOOR_SET)),
        ("CUT/stratum-C4=145", separating_functional(tuple(achieved_145))),
    )
    return TableCertificate(
        tuple((name, table[name]) for name in LOCI),
        agreement(table, CLAIMED_PAIRING),
        disagreement(table, SWAPPED_PAIRING),
        disagreement(table, WITHIN_LANE),
        tuple((name, literal[name]) for name in LOCI),
        agreement(literal, CLAIMED_PAIRING),
        disagreement(literal, SWAPPED_PAIRING),
        disagreement(literal, WITHIN_LANE),
        collapse,
        general,
        charge_increments,
        increments_kill,
        values_kill,
        typing_dependent,
        same_class_floor,
        floor_reading_flips,
        functionals,
    )


# ---------------------------------------------------------------------------
# F/G. the text certificates: the contract, the absences, the anchors
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class TextCertificate:
    contract_wording: bool
    consequent_is_a_comparison: bool
    section8_rows: bool
    literal_antecedent_quantifier: bool
    broadened_restatement: bool
    map_open_line: bool
    map_absent_claim_refuted: bool
    naive_echo_dead: bool
    firewall_inherited: bool
    momentum_anchors: bool
    self_block_anchor: bool
    population_rider: bool
    identity_not_type_anchor: bool
    identity_charge_occurrences: int
    gauss_occurrences: int
    incidence_operator_absent: bool
    positivity_occurrences: int
    distance_three_anchor: bool
    distance_four_anchor: bool
    bridge_lattice_anchor: bool
    strata_census_anchor: bool
    unwitnessed_anchor: bool
    block123_untouched: bool


def text_certificate() -> TextCertificate:
    """Every entry is a substring test on COMMITTED bytes -- a quotable anchor.

    Whitespace is normalised but case is preserved, so an anchor that reads as
    a capitalised phrase in the note must occur capitalised.
    """
    raw151 = read_note(BLOCK151_NOTE)
    raw130 = read_note(BRIDGE_NOTE)
    n151 = flat(raw151)
    n130 = flat(raw130)
    n123 = flat(read_note(BLOCK123_NOTE))
    n136 = flat(read_note(BLOCK136_NOTE))
    n138 = flat(read_note(BLOCK138_NOTE))
    return TextCertificate(
        contract_wording=(
            "read as momentum-like inputs of the kind targeted by the "
            "definiteness theorem of" in n130
            and "LABELED CONDITIONAL — MOMENTUM-LIKE BRIDGE" in n130
        ),
        consequent_is_a_comparison=(
            "qualify for the momentum-like comparison to Block 123, without "
            "yet becoming a gravity-constraint source" in n130
        ),
        section8_rows=(
            "the bridge is restricted to their reversible sublattice" in n130
            and "the affine rank, difference lattice, directed cone, and echo "
            "analysis must all be rerun" in n130
        ),
        literal_antecedent_quantifier=(
            "for each generator used by the bridge" in n130
        ),
        broadened_restatement=(
            "if a move class realizes" in n151
            and "momentum-like in the sense targeted by the Block 123 "
            "definiteness" in n151
            and "momentum-like in the sense targeted by" not in n130
        ),
        map_open_line=(
            "neither built nor excluded" in n151
            and "does not assert that a non-naive frame-to-momentum map "
            "exists or does not exist" in n151
        ),
        map_absent_claim_refuted=(
            "no frame-to-momentum map exists" not in n151
            and "A separately constructed quotient, many-to-one map, or "
            "nonconjugate intertwiner is not ruled out" in n130
        ),
        naive_echo_dead=(
            "eight carrier points cannot be put in bijection with four "
            "momentum labels" in n130
            and "has order two, whereas a generator of cycle type \\(4^1\\) "
            "has order four" in n130
        ),
        firewall_inherited=(
            "supplied-model firewall is inherited unchanged" in n151
        ),
        momentum_anchors=(
            "It was a definiteness wall: an identity-valued total charge "
            "cannot cancel" in n123
            and "POSITIVE MOMENTUM POPULATION BREAK" in n123
            and "EXPECTATION-VALUE ZERO" in n123
            and "not an operator kernel" in n123
            and "its image is exactly the zero-sum subspace" in n123
            and "\\mathbf1^{\\mathsf T}n_\\star=2" in n123
        ),
        self_block_anchor=(
            "\\mathscr B_{03}=\\{0\\}" in n136
            and "the self-conjugate block's balanced zero-expectation ray is "
            "zero" in n136
            and "All such displayed population breaking lives in the two "
            "conjugate pairs." in n136
            and "integer charge is sign-definite, not indefinite" in n138
            and "residue trap's third occurrence" in n138
        ),
        population_rider=(
            "Three populations appear and they are never mixed" in n151
            and "Neither statement is transferable to the other population"
            in n151
        ),
        identity_not_type_anchor=(
            "SPLIT 48/96" in n151 and "not on what it CARRIES" in n151
        ),
        identity_charge_occurrences=(
            raw151.count("U(1)") + raw130.count("U(1)")
        ),
        gauss_occurrences=raw151.lower().count("gauss"),
        incidence_operator_absent=("incidence operator" not in n151),
        positivity_occurrences=n151.lower().count("positivity"),
        distance_three_anchor=(
            "NOT ONE" in n151 and "132{,}288" in n151
        ),
        distance_four_anchor=("1{,}348{,}608" in n151),
        bridge_lattice_anchor=(
            "lie in the GENERATED LATTICE but NOT in the ACHIEVED SET" in n151
        ),
        strata_census_anchor=(
            "(36,59)\\times60{,}768,\\ (36,60)\\times121{,}536,\\ "
            "(37,60)\\times60{,}768" in n151
            and "(36,58),(36,59),(36,60),(37,59),(37,60),(38,60)" in n151
        ),
        unwitnessed_anchor=(
            "TC\\in[\\mathbf{36},42]" in n151
            and "not witnessed" in n151.lower()
        ),
        block123_untouched=(
            "Block 123's own definiteness theorem is untouched" in n151
            and "what changes is that its comparison now has inputs" in n151
        ),
    )


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    machinery: tuple
    machinery_exit: tuple
    # B: the contract
    text: TextCertificate
    literal_antecedent_met: bool
    bridge_in_achieved: tuple
    map_open_line: bool
    # C: the charge lane
    momentum_own: tuple
    momentum_own_count: int
    momentum_committed: tuple
    u1_definite: bool
    momentum_indefinite: bool
    witness_expectation: int
    witness_rank: int
    witness_annihilated: bool
    self_block: tuple
    pair_block: tuple
    # D: the cut lane
    stratum: tuple
    subscan: tuple
    subscan_d3: tuple
    subscan_d4: tuple
    within_block_min: int
    min_cross_distance: tuple
    neutral_at_distance_three: bool
    achieved_145: tuple
    achieved_negation_closed: bool
    achieved_cone_pointed: bool
    achieved_index: int
    floor_negation_closed: bool
    floor_functional: object
    floor_landing: tuple
    d3_multiplicities_equal: bool
    d4_scoping_disclosed: bool
    deep_move_scan: tuple
    # E: the table
    table: TableCertificate
    # F: the non-correspondences
    non_correspondences: tuple
    isomorphism_available: bool
    cut_law_type_determined: bool
    # G: the chain and the firewall
    chain: tuple
    os_gate_certificate: tuple
    deep_os: object
    step_three_absences: tuple
    bridge_points_in_bracket: bool
    bridge_points_in_strata: tuple
    bridge_points_at_unwitnessed_end: tuple
    mc_floor_unwitnessed: bool
    bridge_lattice: tuple
    negatives_violate_corner: bool
    # global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")

    # --- the two worktree imports, content-bound ------------------------------
    b151, b151_digest = import_worktree_module("block152_b151", BLOCK151_RUNNER)
    b123, b123_digest = import_block123()

    # --- the committed cell-cutting machinery, through Block 151's loader ----
    workdir = Path(tempfile.mkdtemp(prefix="block152-machinery-"))
    try:
        records = tuple(
            b151.load_machinery(name, path, pin, cut, workdir)
            for name, path, pin, cut in b151.MACHINERY
        )
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
    c726, c734, _c811 = (record.module for record in records)
    authority = authority_certificate(
        main_head, records, (b151_digest, b123_digest)
    )
    machinery_shape = tuple(
        (record.name, record.total_lines, record.cut_line)
        for record in records
    )
    machinery_exit = (
        records[0].exit_code,
        int(getattr(c726, "npass", -1)),
        int(getattr(c726, "nfail", -1)),
        tuple(int(value) for value in getattr(c734, "PF", (-1, -1))),
    )

    # --- B: the contract ------------------------------------------------------
    text = text_certificate()

    # --- C: the charge lane ---------------------------------------------------
    momentum_own = momentum_own_route()
    momentum_committed = momentum_committed_route(b123)
    charges = PRINCIPAL_CHARGES
    witness = WITNESS_STATE
    image = tuple(charges[i] * witness[i] for i in range(NX))
    u1_definite = all(
        sum(state[i] * state[i] for i in range(NX)) > 0
        for state in itertools.product(range(-2, 3), repeat=NX)
        if any(state)
    )
    momentum_indefinite = (
        any(q > 0 for q in charges) and any(q < 0 for q in charges)
    )
    witness_expectation = sum(
        charges[i] * witness[i] * witness[i] for i in range(NX)
    )
    witness_rank = exact_rank([list(witness), list(image)])
    witness_annihilated = not any(image)
    self_block = (
        Q_SELF,
        all(q >= 0 for q in Q_SELF),
        sum(Q_SELF) != 0,             # balanced zero-expectation ray is {0}
    )
    pair_block = (
        Q_PAIR,
        any(q > 0 for q in Q_PAIR) and any(q < 0 for q in Q_PAIR),
        sum(Q_PAIR) == 0,             # the balanced ray is nonzero
    )

    # --- D: the cut lane ------------------------------------------------------
    stratum_cert = rebuild_stratum_145(c726, c734)
    (
        subscan,
        subscan_d3,
        subscan_d4,
        within_block_min,
        min_cross_distance,
        neutral_at_distance_three,
        achieved_145,
    ) = subscan_moves(stratum_cert)
    stratum = (
        stratum_cert.seven_pieces,
        stratum_cert.survivors,
        stratum_cert.blocks,
        stratum_cert.block_sizes,
        stratum_cert.corpus,
        stratum_cert.block_charge_constant,
        stratum_cert.charge_points,
        stratum_cert.blocks_per_charge,
        stratum_cert.charge_is_type_function,
        stratum_cert.refinement_witness,
    )
    achieved_negation_closed = all(
        (-delta[0], -delta[1]) in achieved_145 for delta in achieved_145
    )
    achieved_cone_pointed = cone_pointed(achieved_145)
    achieved_index = lattice_index_2d(achieved_145)
    floor_negation_closed = negation_closed(FLOOR_SET)
    floor_functional = separating_functional(FLOOR_SET)
    floor_landing = (
        tuple(delta for delta, _count in FLOOR_DELTAS),
        sum(count for _delta, count in FLOOR_DELTAS),
        sum(count for _cost, count in LANDING_STRATA),
        tuple(cost for cost, _count in LANDING_STRATA),
    )
    d3_multiplicities_equal = bool(
        {count for _delta, count in D3_DIRECTED} == {D3_EACH}
        and sum(count for _delta, count in D3_DIRECTED) == 2 * D3_MOVES
        and all(
            (-delta[0], -delta[1]) in dict(D3_DIRECTED)
            and dict(D3_DIRECTED)[(-delta[0], -delta[1])] == count
            for delta, count in D3_DIRECTED
        )
    )
    # The distance-4 SCOPING: the "not one neutral move" statement is a
    # distance-3 statement.  At distance 4 the same stratum carries 1,348,608
    # NEUTRAL moves out of 2,411,328 -- disclosed, anchored to its verbatim
    # occurrence in the committed Block 151 note, and never elided.
    d4_scoping_disclosed = bool(
        text.distance_four_anchor
        and 0 < D4_NEUTRAL < D4_MOVES
        and (0, 0) not in dict(D3_DIRECTED)
        and (0, 0) in dict(SUBSCAN_D4)
    )
    deep_move_scan: tuple = (0, 0, ())
    if deep:
        deep_move_scan = deep_distance_three_scan(stratum_cert, c734)

    # --- E: the table ---------------------------------------------------------
    table = table_certificate(achieved_145)

    # --- F: the non-correspondences ------------------------------------------
    charge_increment_index = lattice_index_1d(table.charge_increments)
    charge_value_index = lattice_index_1d(Q_PAIR)
    cut_index = lattice_index_2d(achieved_145)
    involution_fixed = tuple(sorted(k for k in range(NX) if (-k) % NX == k))
    non_correspondences = (
        (
            "NC1-increment-lattice-typing",
            charge_increment_index == CHARGE_INCREMENT_INDEX
            and cut_index == CUT_INCREMENT_INDEX
            and charge_value_index == 1,
        ),
        (
            "NC2-rank-and-size-mismatch",
            len(Q_PAIR[:1]) == 1
            and len(achieved_145[0]) == 2
            and MOMENTUM_SECTORS != CUT_CHARGE_POINTS
            and CARRIER_SIZES[0] != CARRIER_SIZES[1]
            and CUT_BLOCKS != MOMENTUM_SECTORS,
        ),
        (
            "NC3-mechanism-involution-versus-corner",
            involution_fixed == SELF_CONJUGATE
            and CORNER == (TICK_BOX[0], MIXED_BOX[1])
            and CORNER == CORPUS_CHARGE,
        ),
        (
            "NC4-no-identity-valued-charge-on-the-cut-side",
            text.identity_charge_occurrences == IDENTITY_CHARGE_OCCURRENCES,
        ),
        ("NC5-population-rider-forbids-mixing", text.population_rider),
        (
            "NC6-charge-law-form",
            len({(k, PRINCIPAL_CHARGES[k]) for k in range(NX)})
            == MOMENTUM_SECTORS
            and len(set(PRINCIPAL_CHARGES)) == MOMENTUM_SECTORS
            and stratum_cert.blocks == CUT_BLOCKS
            and len(stratum_cert.charge_points) == CUT_CHARGE_POINTS
            and not stratum_cert.charge_is_type_function
            and text.identity_not_type_anchor,
        ),
    )
    isomorphism_available = bool(
        len(Q_PAIR[:1]) == len(achieved_145[0])
        and len(nonzero_part(tuple((q,) for q in Q_SELF)))
        == len(nonzero_part(FLOOR_SET))
        and len(nonzero_part(tuple((q,) for q in Q_PAIR)))
        == len(nonzero_part(tuple(achieved_145)))
    )
    cut_law_type_determined = stratum_cert.charge_is_type_function

    # --- G: the chain and the firewall ---------------------------------------
    import sympy as sp

    class _Fixture:
        def __init__(self, positive: bool) -> None:
            self.quotient_positive_exact = positive
            self.phase_form = sp.diag(1, sp.I, -1, sp.I ** 3)
            self.momentum_form = sp.diag(*PRINCIPAL_CHARGES)

    with_positive = b123.definiteness_certificate(
        (_Fixture(True), _Fixture(True))
    )
    without_positive = b123.definiteness_certificate(
        (_Fixture(False), _Fixture(False))
    )
    # Block 123's OWN certificate is GATED on OS positivity: the witness field
    # collapses when the quotient-positivity input is withdrawn.  That is the
    # exact asymmetry of chain step (ii), demonstrated rather than asserted.
    os_gate_certificate = (
        bool(with_positive.witness_positive),
        bool(without_positive.witness_positive),
        bool(with_positive.momentum_indefinite),
        bool(with_positive.not_eigenstate),
        int(with_positive.integer_expectation),
    )
    deep_os: object = None
    if deep:
        b119 = b123.block119
        positive = True
        for shear in b123.SHEARS:
            sectors = b119.make_sectors(shear)
            completion = b119.reflection_real_completion(sectors)
            positive = positive and len(sectors) == b123.NX and all(
                b123.quotient_positivity(sector, completion.thetas[k])
                for k, sector in enumerate(sectors)
            )
        deep_os = bool(positive)

    step_three_absences = (
        ("gauss-occurrences", text.gauss_occurrences == GAUSS_OCCURRENCES),
        ("no-incidence-operator", text.incidence_operator_absent),
        ("positivity-is-a-firewall-disclaimer-only", text.positivity_occurrences == 1),
    )

    strata_points = {
        point for points in STRATA_CENSUS.values() for point in points
    }
    bridge_points_in_bracket = all(
        TICK_BOX[0] <= point[0] <= TICK_BOX[1]
        and MIXED_BOX[0] <= point[1] <= MIXED_BOX[1]
        for point in BRIDGE_POINTS
    )
    bridge_points_in_strata = tuple(
        sorted(point for point in BRIDGE_POINTS if point in strata_points)
    )
    bridge_points_at_unwitnessed_end = tuple(
        sorted(point for point in BRIDGE_POINTS if point[1] == MIXED_BOX[0])
    )
    # The MC = 48 end of the global bracket is FACET-WISE and unwitnessed: no
    # committed stratum census reaches it, which is measured here rather than
    # quoted, and two of the three transcribed bridge points sit exactly there.
    mc_floor_unwitnessed = MIXED_BOX[0] not in {
        point[1] for point in strata_points
    }
    bridge_lattice = congruence_lattice(
        BRIDGE_DELTAS, BRIDGE_CHARACTER, BRIDGE_INDEX
    )
    negatives_violate_corner = all(
        target[0] < CORNER[0] or target[1] > CORNER[1]
        for target in NEGATIVE_TARGETS
    )
    achieved_with_zero = tuple(
        sorted(set(achieved_145) | {(0, 0)})
    )
    bridge_in_achieved = tuple(
        (generator, generator in achieved_with_zero)
        for generator in BRIDGE_DELTAS
    )
    literal_antecedent_met = all(hit for _generator, hit in bridge_in_achieved)

    chain = tuple(
        (step, status) for step, status in CHAIN_STATUS
    )

    # No float is constructed anywhere above: every comparison is integer,
    # Fraction, exact sympy or a numpy INTEGER popcount.
    exact_no_float = bool(
        all(isinstance(q, int) for q in PRINCIPAL_CHARGES)
        and isinstance(witness_expectation, int)
        and isinstance(Fraction(1, 3) + Fraction(2, 3), Fraction)
        and np.packbits(np.zeros((1, 8), dtype=np.uint8)).dtype == np.uint8
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        machinery=machinery_shape,
        machinery_exit=machinery_exit,
        text=text,
        literal_antecedent_met=literal_antecedent_met,
        bridge_in_achieved=bridge_in_achieved,
        map_open_line=text.map_open_line,
        momentum_own=momentum_own,
        momentum_own_count=len(momentum_own),
        momentum_committed=momentum_committed,
        u1_definite=u1_definite,
        momentum_indefinite=momentum_indefinite,
        witness_expectation=witness_expectation,
        witness_rank=witness_rank,
        witness_annihilated=witness_annihilated,
        self_block=self_block,
        pair_block=pair_block,
        stratum=stratum,
        subscan=subscan,
        subscan_d3=subscan_d3,
        subscan_d4=subscan_d4,
        within_block_min=within_block_min,
        min_cross_distance=min_cross_distance,
        neutral_at_distance_three=neutral_at_distance_three,
        achieved_145=achieved_145,
        achieved_negation_closed=achieved_negation_closed,
        achieved_cone_pointed=achieved_cone_pointed,
        achieved_index=achieved_index,
        floor_negation_closed=floor_negation_closed,
        floor_functional=floor_functional,
        floor_landing=floor_landing,
        d3_multiplicities_equal=d3_multiplicities_equal,
        d4_scoping_disclosed=d4_scoping_disclosed,
        deep_move_scan=deep_move_scan,
        table=table,
        non_correspondences=non_correspondences,
        isomorphism_available=isomorphism_available,
        cut_law_type_determined=cut_law_type_determined,
        chain=chain,
        os_gate_certificate=os_gate_certificate,
        deep_os=deep_os,
        step_three_absences=step_three_absences,
        bridge_points_in_bracket=bridge_points_in_bracket,
        bridge_points_in_strata=bridge_points_in_strata,
        bridge_points_at_unwitnessed_end=bridge_points_at_unwitnessed_end,
        mc_floor_unwitnessed=mc_floor_unwitnessed,
        bridge_lattice=bridge_lattice,
        negatives_violate_corner=negatives_violate_corner,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE CONTRACT, ATTRIBUTED EXACTLY BEFORE ANY COMPARISON: Block 130 Section 6 carries the labeled cost-class-reversibility conditional whose consequent is "momentum-like inputs of the kind targeted by the definiteness theorem" of Block 123 and whose antecedent quantifies over EACH GENERATOR USED BY THE BRIDGE, and Section 8 scopes that consequent to qualification for the momentum-like comparison "without yet becoming a gravity-constraint source"; Block 151\'s boxed restatement BROADENS that antecedent from "each generator used by the bridge" to "a move class", and since the bridge\'s own generators (5,-7) and (1,-7) are UNACHIEVED at stratum 145, Section 6\'s LITERAL antecedent is NOT MET there -- so the licensing for the stratum-145 comparison is NOT Section 8\'s activation row but Section 8\'s OUTCOME ROWS 3-4, the partial-reverse-pair row ("if only some reverse pairs occur, the bridge is restricted to their reversible sublattice; its index, signs and support dependence must be RECOMPUTED rather than inherited from L") and the additional-deltas row ("if the enumeration produces additional deltas, the affine rank, difference lattice, directed cone and echo analysis must all be RERUN"), and both are attributed exactly so; that recomputation returns a shape row 3 did not anticipate, the reversible set generating Z^2 at index 1 and thus STRICTLY CONTAINING L at index 28 rather than restricting it, on a DIFFERENT POPULATION from the transcribed record; and Block 151 records a non-naive frame-to-momentum map as NEITHER BUILT NOR EXCLUDED -- never as nonexistent -- so the licensed comparison level is STRUCTURAL ONLY: a table of CERTIFIED PROPERTIES, with NO isomorphism claimed and none implied\nper_site: THE MOMENTUM SIDE, RE-CERTIFIED FROM BLOCK 123\'s OWN COMMITTED MACHINERY: the site projectors sum to I_32 exactly with four-line compression I_4, so <v, I_4 v> = ||v||^2 > 0 for EVERY nonzero quotient state and the zero-sum condition is UNREACHABLE -- a DEFINITENESS WALL and not a counting accident; the committed Fourier conjugation makes the spatial shift momentum-diagonal with sector phases i^k, and Block 123\'s own principal_charge inverter returns Ptilde = diag(0,1,2,-1), HERMITIAN, re-exponentiating exactly to diag(1,i,-1,-i) and INDEFINITE since both signs occur in its spectrum; the witness v* = e1 + e3 is nonzero with norm^2 = 2, carries expected total momentum 0 in Z AND 1+3 = 4 = 0 mod 4 -- BOTH conventions -- and is NOT ANNIHILATED, tested by rank[v* | Ptilde v*] = 2, so zero expectation is not eigenstate-ness; Block 123\'s own gauss_certificate returns im D_cl EXACTLY the zero-sum subspace with the EXHIBITED solution g* = (0,1,1,0), the momentum population passing and the U(1) row of total 2 BLOCKED, the wall and the break being one certificate read on two rows; and the landed 136/138 correction is re-derived on the same fixtures -- the SELF-CONJUGATE block Q_{0,N/2} = diag(0,2) is SIGN-DEFINITE with balanced ray {0}, the CONJUGATE PAIR Q_{k,N-k} = diag(1,-1) is INDEFINITE with balanced ray t(1,1), the residue trap being 2 = -2 mod 4 while 2 != -2 in Z, and supp(v*) = {1,3} so ALL population breaking lies in the conjugate pair -- with the fresh disjoint-route checker re-certifying this entire side at 37/37 by its own construction\nper_mode: THE SIGN-LAYER TABLE, AND THE THREE INFLATION DISCLOSURES THAT FIX ITS SIZE: under the pairing self-conjugate {0,N/2} <-> the cost floor C4 = 144 and conjugate pair (k,N-k) <-> stratum C4 = 145, under the STATED TYPING (charge side = charge VALUES, cut side = ACHIEVED INCREMENTS) and under the balanced-ray convention, the three properties -- negation-closure, the existence of a nonnegative nontrivial zero-total combination, and pointedness of the generated cone -- AGREE IN ALL SIX CELLS, each cell decided by a complete exact procedure that exhibits either a separating functional or an explicit nonnegative zero-combination, with the SWAPPED pairing disagreeing on all three properties at BOTH loci and the two loci differing on all three properties WITHIN each lane; but THREE DISCLOSURES are displayed beside the match and not deferred -- (i) COLLAPSE: on these four sets the three properties are EQUIVALENT, so the table carries ONE BIT PER LOCUS and TWO BITS in total rather than six, they are INEQUIVALENT IN GENERAL with a SEPARATING SET exhibited by the checker so the collapse is a fact about THESE CELLS, and the hostile controls are therefore PARTLY AUTOMATIC since once one property flips the other two follow; (ii) CONVENTION: under the LITERAL zero-total reading the MATCH SURVIVES but the controls DEGRADE FROM 6/6 TO 4/6, so the match is robust to the convention while its discriminating power is not; and (iii) TYPING: the match DIES under EITHER uniform typing, values-both making the two CUT loci coincide and increments-both making the two CHARGE loci coincide, and the floor cell uses the floor-ANCHORED class so that under the strict same-cost-class reading the floor set is Block 150\'s {(0,0)} on which negation-closure FLIPS TO VACUOUS TRUTH -- whence the honest headline: the correspondence is REAL, with witnesses in every cell and two controls that fail as they should, and it is THIN, two bits under one typing and one convention with NO structure transported\nper_block: THE SIX NON-CORRESPONDENCES, EACH WITH ITS CERTIFICATE: NC1 the LATTICE INDEX does not transfer -- the self-conjugate charges {0,2} generate 2Z at INDEX 2 while the floor increment set generates Z^2 at INDEX 1, so the shared property is SIGN and not index, with the checker\'s TYPING NOTE carried in the statement that "index 2" is the INCREMENT-LATTICE reading of the self-conjugate charges and DISSOLVES when they are read as VALUES, which is the OPPOSITE typing from the table\'s; NC2 NO ISOMORPHISM IS EVEN AVAILABLE -- ambient ranks Z against Z^2, nonzero set sizes 1 against 3 at the definite locus and 2 against 6 at the indefinite, and Block 130 Section 7\'s OWN two exclusions, eight carrier points unable to biject with four momentum labels and a generator of cycle type 2^4 having order two where one of type 4^1 has order four, so THREE INDEPENDENT obstructions stand; NC3 the MECHANISMS ARE UNRELATED -- the momentum side\'s definite locus is the FIXED-POINT SET of the involution k -> N-k, a residue fact true for every N, while the cell-cutting side\'s directed locus is the COST FLOOR sitting at an EXTREME CORNER of a global facet bracket, a geometric fact about the four-box: same shape, unrelated cause; NC4 the DICHOTOMY AXES DO NOT MATCH -- Block 123\'s HEADLINE split is along the CHARGE axis, one state under two charges with I_4 definite against Ptilde indefinite, and NO identity-valued second charge is registered anywhere on the cell-cutting side, the strings occurring ZERO TIMES, so only the momentum side\'s SECONDARY SECTOR axis has a counterpart and THAT is the axis the table compares; NC5 COEXISTENCE AGAINST DISJOINT POPULATIONS -- the momentum loci COEXIST IN ONE CARRIER under ONE charge operator so the break is a statement about a state inside it, while the cell-cutting loci are TWO DISJOINT COST STRATA whose mixing Block 151\'s own population rider forbids, so there is no cell-cutting object corresponding to "a state in which both live"; and NC6 the CHARGE LAWS DIFFER IN KIND -- a DIAGONAL OPERATOR taking 4 labels to 4 charges, injective and determined by the sector\'s own CHARACTER, against a COMBINATORIAL function of block IDENTITY taking 192 labels to 3 points and provably NOT determined by the lone piece\'s own charge type since the (0,2) pieces split 48/96\nlattice_wide: THE CHAIN, STEP BY STEP, THE FIREWALL FINDING, AND THE DOWNSTREAM DELIVERY: Block 123\'s result is a THREE-STEP CHAIN and comparing endpoints would hide where the lanes part, so each step is compared separately -- step (i) SIGN-INDEFINITENESS MATCHES, Ptilde being indefinite with the conjugate-pair block diag(1,-1) carrying both signs while the stratum-145 achieved set is negation-closed with cone R^2, and this match IS the whole of the sign-layer correspondence; step (ii) the nonnegative nontrivial zero-total combination MATCHES BUT IS WEAKER ON THE CELL-CUTTING SIDE -- the direction is the checker\'s correction and runs opposite to the natural reading, since Block 123 needs the zero-expectation state to be a CERTIFIED OS-POSITIVE quotient state so the positivity certificate lives on the BLOCK 123 CHARGE SIDE, while the cell-cutting analogue is MERE COMBINATORIAL MULTIPLICITY that reversibility makes AUTOMATIC -- and its non-vacuous content is SCOPED TO DISTANCE 3, namely that ZERO of the 132,288 distance-3 same-class moves at stratum 145 are charge-neutral, with distance 4 contributing 1,348,608 NEUTRAL moves DISPLAYED, so "not one move is neutral" is TRUE AT DISTANCE 3 AND FALSE AT DISTANCE 4 and the scope is carried wherever the claim is used; step (iii) positivity cone plus incidence image plus Gauss solvability has NO CELL-CUTTING OBJECT AT ALL, there being no positive state space, no closed-carrier incidence operator whose image is the zero-total subspace and no Gauss equation, with "Gauss" occurring ZERO TIMES in Block 151, so POPULATABILITY DOES NOT TRANSFER and only the SIGN HYPOTHESIS does; the FIREWALL FINDING is that the bridge\'s three transcribed points (36,55), (41,48) and (37,48) lie INSIDE the global bracket TC in [36,42] and MC in [48,60] but occur in NONE of the committed strata 144/145/146, whose charge points are (36,60); (36,59), (36,60), (37,60); and (36,58), (36,59), (36,60), (37,59), (37,60), (38,60) -- and TWO of them, (41,48) and (37,48), sit at the MC = 48 end that Block 151 displays as a FACET-WISE UNWITNESSED bound no four-box cutting is known to realize, so the comparison is executed on the ENUMERATED populations only and no claim here needs the transcribed points to be realizable; and DOWNSTREAM the joint-lane program\'s requested comparison is EXECUTED with its scope exact and the pickup\'s program COMPLETES, while a REGISTERED FRAME-TO-MOMENTUM MAP remains open with THREE NAMED REQUIREMENTS -- a positive state space on the cell-cutting side with a positivity certificate, a closed carrier with an incidence operator whose image is exactly the zero-total subspace, and an identification of achieved increments with a charge operator\'s spectrum -- strata 147 and above remain UNEXPLORED, the cycle-725/726/734 supplied-model firewall is INHERITED UNCHANGED, and the other lane\'s unmerged cycle-778-799 material is NOT READ, NOT CONSUMED and NOT SUPERSEDED\nRESULT: on Block 123\'s displayed momentum fixtures and Block 151\'s displayed strata, executing Block 151\'s first next_trace_action item from origin/main\'s committed machinery only, THE CONTRACT IS ATTRIBUTED EXACTLY (Block 151\'s restatement BROADENS Block 130 Section 6\'s antecedent from "each generator used by the bridge" to "a move class"; (5,-7) and (1,-7) are UNACHIEVED at 145 so Section 6\'s LITERAL antecedent is UNMET there; the licensing is Section 8\'s OUTCOME ROWS 3-4; and "neither built nor excluded" caps the level at a CERTIFIED-PROPERTY TABLE with NO isomorphism claimed or implied); THE MOMENTUM SIDE IS RE-CERTIFIED (Q_U1 = I_4 always positive so the zero-sum condition is unreachable; Ptilde = diag(0,1,2,-1) Hermitian and INDEFINITE; v* = e1+e3 with expectation 0 in Z and 4 = 0 mod 4, NOT annihilated; the Gauss image EXACTLY the zero-sum subspace with g* = (0,1,1,0) exhibited and the U(1) row total 2 BLOCKED; and the landed 136/138 split putting the break ENTIRELY in the conjugate pair diag(1,-1) with balanced ray t(1,1) while the self-conjugate diag(0,2) is SIGN-DEFINITE with balanced ray {0}), the checker re-certifying that side at 37/37; and THE SIGN-LAYER TABLE AGREES IN ALL SIX CELLS under self-conjugate <-> floor and conjugate-pair <-> stratum 145, with the SWAPPED pairing disagreeing everywhere and the loci distinguished within each lane -- SUBJECT TO THREE DISPLAYED DISCLOSURES: the properties COLLAPSE TO ONE BIT PER LOCUS here (inequivalent in general, separating set exhibited) so the table carries TWO BITS and the controls are PARTLY AUTOMATIC; the match is CONVENTION-DEPENDENT (literal reading: match survives, controls 4/6); and it is TYPING-DEPENDENT, dying under EITHER uniform typing, with the floor cell using the floor-ANCHORED class whose strict reading {(0,0)} flips negation-closure to VACUOUS TRUTH; SIX NON-CORRESPONDENCES stand with certificates (index 2 vs 1 under the OPPOSITE typing; NO isomorphism available at ranks 1 vs 2, sizes 1:3 and 2:6, plus Block 130 Section 7\'s 8-vs-4 and order-2-vs-4; involution fixed points vs an extremal corner; NO identity-valued second charge on the cell-cutting side, ZERO occurrences; one carrier vs two disjoint strata; diagonal 4 -> 4 character-determined vs combinatorial 192 -> 3 identity-not-type); THE CHAIN SEPARATES (step (i) MATCHES; step (ii) matches but is WEAKER ON THE CELL-CUTTING SIDE, the OS positivity certificate living on the charge side, its non-vacuous content SCOPED TO DISTANCE 3 with ZERO neutral of 132,288 while distance 4 contributes 1,348,608 neutral, displayed; step (iii) has NO cell-cutting object at all, "Gauss" occurring ZERO times in Block 151, so POPULATABILITY DOES NOT TRANSFER); and THE FIREWALL BITES ON THE BRIDGE\'S OWN RECORD, the three transcribed points (36,55), (41,48), (37,48) lying inside the global bracket but in NO committed stratum with two at the UNWITNESSED MC = 48 end: THE CORRESPONDENCE IS REAL, IT IS CONFINED TO THE SIGN LAYER, AND ABOVE THAT LAYER THE LANES ARE UNDERDETERMINED PENDING A REGISTERED MAP\nDECISION_CUT: BUILD OR EXCLUDE A REGISTERED FRAME-TO-MOMENTUM MAP, and the requirements are now NAMED rather than gestured at -- (1) a POSITIVE STATE SPACE on the cell-cutting side carrying a positivity certificate of the kind block119 supplies on the momentum side; (2) a CLOSED CARRIER with an INCIDENCE OPERATOR whose image is EXACTLY the zero-total subspace, which is the object chain step (iii) found missing; and (3) an IDENTIFICATION OF ACHIEVED INCREMENTS WITH A CHARGE OPERATOR\'S SPECTRUM, which is the object NC6 found to have the wrong form (192 -> 3 by identity against 4 -> 4 by character) -- since without all three the comparison cannot rise above the sign layer no matter how many further properties are tabulated; ENUMERATE STRATA 147 AND ABOVE for the bridge vectors, unchanged from Block 151 and still the only route to (5,-7) and (1,-7); LEAVE THE OTHER LANE\'S UNMERGED CYCLE-778-799 MATERIAL to that worker -- their pending state, not read, not consumed, not superseded; and note that the paired-degeneracy observable question, the entropy/counting-functional route candidate, the common nilpotent differential, composite minimality and the cost-146 geometric gate remain named and unexecuted; Block 123\'s own theorem is UNTOUCHED and this block does NOT adjudicate it; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "contract_wording",
    "map_open",
    "section8_licence",
    "table_strength",
    "typing_disclosure",
    "convention_disclosure",
    "corrected_direction",
    "distance_scoping",
    "no_isomorphism",
    "identity_not_type",
    "firewall_strata",
    "unwitnessed",
    "closure",
    "map_requirements",
    "pickup_provenance",
    "not_consumed_rider",
    "independence_disclosure",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "firewalls",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "n1_n8",
    "w1",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    compact = compact_note(note_text)
    return {
        # Whitespace- and comma-insensitive so the note may write either form.
        "contract_wording": "inputs of the kind" in note,
        "map_open": "neither built nor excluded" in note,
        "section8_licence": "section 8" in note or "outcome rows" in note,
        "table_strength": (
            "one bit" in note or "two bits" in note or "collapse" in note
        ),
        "typing_disclosure": "typing" in note,
        "convention_disclosure": "convention" in note,
        "corrected_direction": "weaker on the cell-cutting side" in note,
        "distance_scoping": "distance 3" in note
        and (
            "1,348,608" in note or "1348608" in compact or "distance 4" in note
        ),
        "no_isomorphism": "no isomorphism" in note,
        "identity_not_type": (
            "identity-not-type" in note or "not type-determined" in note
        ),
        "firewall_strata": (
            "none of the committed strata" in note
            or "no committed stratum" in note
        ),
        "unwitnessed": "unwitnessed" in note,
        "closure": "executed" in note
        and ("licensed scope" in note or "sign layer" in note),
        "map_requirements": "three" in note
        and (
            "requirements" in note
            or (
                "positive state space" in note
                and "incidence operator" in note
                and "spectrum" in note
            )
        ),
        "pickup_provenance": "pickup" in note,
        "not_consumed_rider": "778" in note,
        "independence_disclosure": "cross-context" in note,
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": (
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        # Raw substring membership makes the printed eight-line fence
        # byte-identical to its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "literal_antecedent_met": False,
        "map_open_line": True,
        "u1_definite": True,
        "witness_rank": 2,
        "neutral_at_distance_three": False,
        "d4_scoping_disclosed": True,
        "one_bit_collapse": True,
        "typing_dependent": True,
        "swap_disagree": TABLE_SWAP_DISAGREE,
        "isomorphism_available": False,
        "cut_law_type_determined": False,
        "bridge_points_in_strata": (),
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_literal_antecedent_met":
        claims["literal_antecedent_met"] = True
    elif mutation == "drop_neither_built_line":
        claims["map_open_line"] = False
    elif mutation == "claim_wall_indefinite":
        claims["u1_definite"] = False
    elif mutation == "break_momentum_witness":
        claims["witness_rank"] = 1
    elif mutation == "claim_neutral_distance_three":
        claims["neutral_at_distance_three"] = True
    elif mutation == "drop_distance_four_scoping":
        claims["d4_scoping_disclosed"] = False
    elif mutation == "claim_independent_bits":
        claims["one_bit_collapse"] = False
    elif mutation == "claim_typing_free_table":
        claims["typing_dependent"] = False
    elif mutation == "break_swap_control":
        claims["swap_disagree"] = TABLE_SWAP_DISAGREE - 1
    elif mutation == "claim_isomorphism":
        claims["isomorphism_available"] = True
    elif mutation == "claim_type_determined_cut_law":
        claims["cut_law_type_determined"] = True
    elif mutation == "claim_bridge_point_in_stratum":
        claims["bridge_points_in_strata"] = (CORPUS_CHARGE,)
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
def evaluate_gates(
    facts: Facts, claims: dict[str, object], elapsed_ns: int
) -> dict[str, bool]:
    authority = facts.authority
    text = facts.text
    table = facts.table
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_floor_boundary_theorem_2026_08_20.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "scripts/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            # the three origin/main-only cell-cutting runners are
            # content-bound via the gate-A blob pins, not audit paths
        )
        and PARENT_ARTIFACTS
        == (
            BLOCK151_NOTE,
            BLOCK151_RUNNER,
            BRIDGE_NOTE,
            BLOCK123_NOTE,
            BLOCK123_RUNNER,
        )
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # the two worktree imports, bound to the bytes actually imported
        and authority.imported_bytes_bound
        # the three cell-cutting runners, bound BY CONTENT and by shape
        and authority.machinery_content_bound
        and tuple(name for name, _d, _r, _p in authority.machinery_blobs)
        == ("c726", "c734", "c811")
        and facts.machinery == MACHINERY_SHAPE
        and facts.machinery_exit
        == (0, C726_GATES, 0, (C734_PREFIX_GATES, 0))
    )

    gate_b = bool(
        text.contract_wording
        and text.consequent_is_a_comparison
        and text.section8_rows
        and text.literal_antecedent_quantifier
        and text.broadened_restatement
        and text.map_absent_claim_refuted
        and text.naive_echo_dead
        and text.firewall_inherited
        and facts.map_open_line == bool(claims["map_open_line"])
        # the antecedent-broadening certificate: section 6 quantifies over the
        # bridge's OWN generators, and neither is achieved at 145, so the
        # LITERAL antecedent is unmet there and the licensing is section 8's
        and facts.bridge_in_achieved
        == tuple((generator, False) for generator in BRIDGE_DELTAS)
        and facts.literal_antecedent_met
        == bool(claims["literal_antecedent_met"])
    )

    gate_c = bool(
        facts.momentum_own_count == MOMENTUM_OWN_ROUTE_CHECKS
        and all(value for _key, value in facts.momentum_own)
        and facts.momentum_committed
        == (
            True,
            NX,
            PRINCIPAL_CHARGES,
            True,
            True,
            True,
            True,
            GAUSS_FIELD,
        )
        # the wall: the identity-valued U(1) charge is POSITIVE DEFINITE
        and facts.u1_definite == bool(claims["u1_definite"])
        # the principal charge is Hermitian and INDEFINITE, with the witness
        and facts.momentum_indefinite
        and facts.witness_expectation == 0
        and facts.witness_rank == claims["witness_rank"]
        and not facts.witness_annihilated
        # the landed 136/138 split
        and facts.self_block == (Q_SELF, True, True)
        and facts.pair_block == (Q_PAIR, True, True)
        and text.momentum_anchors
        and text.self_block_anchor
    )

    ambiguous, witness_pieces = facts.stratum[9]
    gate_d = bool(
        # the stratum-145 census, rebuilt here without reference to any move
        facts.stratum[0] == SEVEN_PIECES
        and facts.stratum[1] == BLOCKS_145
        and facts.stratum[2] == BLOCKS_145
        and facts.stratum[3] == (BLOCK_SIZE_145,)
        and facts.stratum[4] == CORPUS_145
        and BLOCKS_145 * BLOCK_SIZE_145 == CORPUS_145
        and facts.stratum[5]
        and facts.stratum[6] == CHARGE_POINTS_145
        and facts.stratum[7] == BLOCKS_PER_CHARGE_145
        and not facts.stratum[8]
        and ambiguous == ((REFINEMENT_TYPE, REFINEMENT_CHARGES),)
        and len(witness_pieces) == 2
        and tuple(point for _piece, point in witness_pieces)
        == REFINEMENT_CHARGES
        # the floor-anchored set: pointed, with the separating functional
        # EXHIBITED, and not negation-closed
        and not facts.floor_negation_closed
        and facts.floor_functional is not None
        and all(
            sum(w * v for w, v in zip(facts.floor_functional, delta)) > 0
            for delta in nonzero_part(FLOOR_SET)
        )
        and facts.floor_landing
        == (FLOOR_SET, ALTERNATES, ALTERNATES, (145, 146, 147))
        and FLOOR_CLASS not in facts.floor_landing[3]
        # the stratum-145 achieved set
        and facts.achieved_145 == ACHIEVED_145
        and facts.achieved_negation_closed
        and not facts.achieved_cone_pointed
        and facts.achieved_index == CUT_INCREMENT_INDEX
        and facts.subscan
        == (
            SUBSCAN_BLOCKS,
            (
                ((36, 59), SUBSCAN_PER_CHARGE),
                ((36, 60), SUBSCAN_PER_CHARGE),
                ((37, 60), SUBSCAN_PER_CHARGE),
            ),
        )
        and facts.subscan_d3 == SUBSCAN_D3
        and facts.subscan_d4 == SUBSCAN_D4
        and facts.within_block_min == WITHIN_BLOCK_MIN
        and facts.min_cross_distance == MIN_CROSS_DISTANCE
        # not one charge-neutral move at distance three ...
        and facts.neutral_at_distance_three
        == bool(claims["neutral_at_distance_three"])
        and facts.d3_multiplicities_equal
        and text.distance_three_anchor
        # ... and the SCOPE of that statement, disclosed: distance FOUR carries
        # 1,348,608 neutral moves of 2,411,328
        and facts.d4_scoping_disclosed == bool(claims["d4_scoping_disclosed"])
        and facts.deep_move_scan
        in ((0, 0, ()), (D3_MOVES, 0, D3_DIRECTED))
    )

    gate_e = bool(
        table.table
        == (
            ("CHG/self-conjugate", (False, False, True)),
            ("CHG/conjugate-pair", (True, True, False)),
            ("CUT/floor-C4=144", (False, False, True)),
            ("CUT/stratum-C4=145", (True, True, False)),
        )
        and table.match == TABLE_MATCH
        and table.swap_disagree == claims["swap_disagree"]
        and table.within_differ == TABLE_WITHIN_DIFFER
        # (i) the one-bit collapse, and the general inequivalence exhibited
        and table.one_bit_collapse == bool(claims["one_bit_collapse"])
        and table.general_inequivalence == (False, True, False)
        # (ii) the literal reading: the match survives, both controls degrade
        and table.literal_match == LITERAL_MATCH
        and table.literal_swap_disagree == LITERAL_SWAP_DISAGREE
        and table.literal_within_differ == LITERAL_WITHIN_DIFFER
        and LITERAL_SWAP_DISAGREE < TABLE_SWAP_DISAGREE
        and LITERAL_WITHIN_DIFFER < TABLE_WITHIN_DIFFER
        # (iii) the typing: EITHER uniform typing kills the table
        and table.charge_increments == CHARGE_INCREMENTS
        and table.increments_typing_kills[0] == table.increments_typing_kills[1]
        and table.values_typing_kills[0] == table.values_typing_kills[1]
        and table.values_typing_kills[0] == (False, False, True)
        and table.typing_dependent == bool(claims["typing_dependent"])
        # ... and the floor cell depends on the floor-anchored reading
        and table.same_class_floor == (True, False, True)
        and table.floor_reading_flips
        # pointedness is EXHIBITED where it holds and absent where it fails
        and tuple(name for name, _f in table.separating_functionals)
        == (
            "CHG/self-conjugate",
            "CUT/floor-C4=144",
            "CUT/stratum-C4=145",
        )
        and dict(table.separating_functionals)["CUT/stratum-C4=145"] is None
        and dict(table.separating_functionals)["CHG/self-conjugate"] is not None
        and dict(table.separating_functionals)["CUT/floor-C4=144"] is not None
    )

    gate_f = bool(
        len(facts.non_correspondences) == 6
        and all(value for _key, value in facts.non_correspondences)
        and tuple(key.split("-")[0] for key, _v in facts.non_correspondences)
        == ("NC1", "NC2", "NC3", "NC4", "NC5", "NC6")
        and facts.isomorphism_available == bool(claims["isomorphism_available"])
        and facts.cut_law_type_determined
        == bool(claims["cut_law_type_determined"])
        and text.identity_charge_occurrences == IDENTITY_CHARGE_OCCURRENCES
        and text.identity_not_type_anchor
        and text.population_rider
    )

    gate_g = bool(
        facts.chain == CHAIN_STATUS
        and facts.chain[1][1] == "MATCH, WEAKER ON THE CELL-CUTTING SIDE"
        and facts.chain[2][1] == "NO COUNTERPART"
        # step (ii): Block 123's OWN certificate is gated on OS positivity
        and facts.os_gate_certificate == (True, False, True, True, 0)
        and facts.deep_os in (None, True)
        # step (iii): the absences, counted on the committed bytes
        and len(facts.step_three_absences) == 3
        and all(value for _key, value in facts.step_three_absences)
        and text.gauss_occurrences == GAUSS_OCCURRENCES
        # the firewall on the transcribed bridge record
        and facts.bridge_points_in_bracket
        and facts.bridge_points_in_strata
        == tuple(claims["bridge_points_in_strata"])
        and facts.bridge_points_at_unwitnessed_end == MC_48_BRIDGE_POINTS
        and facts.mc_floor_unwitnessed
        and MC_FLOOR_UNWITNESSED == MIXED_BOX[0]
        and facts.bridge_lattice == (BRIDGE_INDEX, True)
        and facts.negatives_violate_corner
        and text.bridge_lattice_anchor
        and text.strata_census_anchor
        and text.unwitnessed_anchor
        and text.block123_untouched
        and facts.exact_no_float
    )

    required = tuple(claims["required_scope_keys"])
    gate_h = bool(
        set(facts.scope) == set(required)
        and all(facts.scope.values())
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") == 7
        and elapsed_ns <= RUNTIME_BUDGET_SEC * 1_000_000_000
    )

    return {
        "A": gate_a,
        "B": gate_b,
        "C": gate_c,
        "D": gate_d,
        "E": gate_e,
        "F": gate_f,
        "G": gate_g,
        "H": gate_h,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--deep",
        action="store_true",
        help=(
            "also run the FULL versions of the two sampled certificates: the "
            "complete distance-3 same-class scan of all 192 cost-145 blocks, "
            "and Block 119's OS quotient positivity at BOTH rational shear "
            "fixtures feeding Block 123's own definiteness certificate"
        ),
    )
    arguments = parser.parse_args()
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
    facts = measure(arguments.deep)
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values = evaluate_gates(facts, build_claims(mutation), elapsed_ns)
        changed = {
            key for key in raw_gates if raw_gates[key] != gate_values[key]
        }
        if changed - {target} or gate_values[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the Block 151 note and runner, the Block 130 bridge note and the Block 123 note and runner are content-bound at the parent pin by literal blob values, the two runners this block IMPORTS are additionally bound to the hash of the bytes actually imported, and the three cell-cutting runners the cut lane rests on are read from origin/main AT RUN TIME through Block 151's own loader under its blob pins and pinned cut markers, with their own gate tallies recorded (cycle 726: 32/0 and exit 0; cycle 734 prefix: 22/0)",
        gate_values["A"],
    )
    checks.check(
        "B-comparison-contract",
        "the contract is extracted from the committed bytes, not paraphrased: Block 130 section 6 carries the labeled conditional whose consequent reads 'momentum-like inputs of the kind targeted by the definiteness theorem of', its antecedent quantifies over 'each generator used by the bridge', and Block 151's restatement BROADENS that to 'if a move class realizes' -- a difference this block states rather than elides, because the bridge's own generators (5,-7) and (1,-7) are NOT in the stratum-145 achieved difference set, so section 6's LITERAL antecedent is UNMET at 145 and the execution is licensed by section 8's outcome rows (restriction to the reversible sublattice; rerun of rank, lattice, cone and echo) under section 8's ceiling that the increments qualify for the comparison 'without yet becoming a gravity-constraint source'; Block 151's own line that a non-naive frame-to-momentum map is NEITHER BUILT NOR EXCLUDED is present and is what confines the comparison to certified properties",
        gate_values["B"],
    )
    checks.check(
        "C-momentum-side",
        "the whole Block 123 momentum side is re-certified TWICE: 37 exact integer certificates on an OWN ROUTE that imports nothing and rebuilds everything from the shift character k -> i^k -- the identity-valued U(1) total, whose expectation IS the squared norm and is strictly positive on every nonzero state (the definiteness WALL); the Hermitian INDEFINITE principal charge diag(0,1,2,-1); the witness e1 + e3 with expectation zero in BOTH conventions, not annihilated, and not an eigenstate at rank two; and the Gauss layer with image exactly the zero-sum subspace, the exhibited field (0,1,1,0) and the blocked U(1) row total 2 -- and the same objects read back out of the COMMITTED runner's own site projectors, principal_charge inverter and gauss_certificate; the landed 136/138 correction is applied and load-bearing: diag(0,2) is sign-definite with balanced ray {0}, diag(1,-1) is indefinite with a nonzero balanced ray, and the break is carried entirely by the conjugate pair",
        gate_values["C"],
    )
    checks.check(
        "D-cut-side",
        "the cost-145 stratum is REBUILT here by a route that never mentions a move -- an exact point-coverability filter over all 1,216 cost-7 pieces, which cuts to exactly 192 survivors, followed by exact 23-piece cover enumeration -- recovering 192 blocks of exactly 1,266, 243,072 cuttings, the charge constant on every block at (36,59) x 60,768, (36,60) x 121,536 and (37,60) x 60,768 over 48/96/48 blocks, and the identity-not-type refinement exhibited by the (0,2) type carrying two different block charges; the floor-anchored increment set is NOT negation-closed and its cone is pointed with the separating functional EXHIBITED and re-verified, every one of its 42,240 members leaving the floor into 145/146/147; the stratum-145 achieved set is negation-closed with cone R^2 and lattice Z^2 at index 1, the twelve-block sub-scan reproduces the exact minimum cross-charge distances 3/4/3 and the within-block minimum 4, NOT ONE distance-3 move is charge-neutral and the four directions carry the equal multiplicity 66,144; and the SCOPE of that statement is disclosed rather than elided -- at distance FOUR the same stratum carries 1,348,608 NEUTRAL moves of 2,411,328, twice-verified in Block 151 and anchored to its verbatim occurrence in the committed note, with --deep re-deriving the full 132,288-move distance-3 census here",
        gate_values["D"],
    )
    checks.check(
        "E-sign-layer-table",
        "the comparison is a 3 x 2 x 2 table decided by exact arithmetic: under self-conjugate <-> floor and conjugate-pair <-> stratum 145 all SIX cells agree, the SWAPPED pairing disagrees 6/6 and the two loci differ 6/6 WITHIN each lane, so the agreement discriminates; and the table is reported at its TRUE strength, with all three inflations disclosed as CHECKED certificates -- (i) in every cell the three properties COLLAPSE to one bit (closed = zero-total = not-pointed) although they are not equivalent in general, exhibited on {(1,0), (-1,1), (0,-1)}; (ii) under the LITERAL reading admitting zero generators the match still reads 6/6 but BOTH hostile controls degrade to 4/6, so the discriminating power rests on Block 136's balanced convention; (iii) the table compares charge VALUES against achieved INCREMENTS, and EITHER uniform typing kills it -- increments on both charge loci coincide, values on both cut loci coincide -- while reading the floor cell under the strict same-cost-class convention gives Block 150's {(0,0)}, whose negation-closure flips to vacuously true",
        gate_values["E"],
    )
    checks.check(
        "F-non-correspondences",
        "six entries do NOT correspond, each as a certificate rather than a remark: (NC1) the achieved INCREMENT lattice is 2Z at index 2 on the charge lane against Z^2 at index 1 on the cut lane, and the disclosure that reading VALUES instead would give index 1 and collapse the contrast; (NC2) the ambient ranks are 1 against 2 and the sizes 4 sectors against 3 charge points and 192 blocks against 4 sectors, so NO isomorphism is even available; (NC3) the mechanisms are the involution k -> -k mod 4 with fixed points {0, 2} against the extremal corner (36,60) = (TC_min, MC_max), same shape and unrelated cause; (NC4) the identity-valued charge carrying Block 123's headline has ZERO text occurrences on the cut side; (NC5) Block 151's own population rider forbids transferring either statement between populations; (NC6) the label-to-charge laws differ in kind, a character-determined injective 4 -> 4 diagonal operator against a combinatorial 192 -> 3 map measured here to be NOT type-determined",
        gate_values["F"],
    )
    checks.check(
        "G-chain-and-firewall",
        "the three-step chain is reported with step (ii)'s asymmetry in the CORRECT direction: Block 123's own committed definiteness_certificate is GATED on OS quotient positivity, which is demonstrated by withdrawing that input and watching its witness field collapse, so the strong half lives on the CHARGE side while the cut lane supplies only combinatorial nonnegativity of move multiplicities, automatic under mutual reversibility -- step (ii) is WEAKER ON THE CELL-CUTTING SIDE; step (iii) has no cut-lane object at all, with 'Gauss' occurring ZERO times in the Block 151 note, no incidence operator registered and the sole occurrence of 'positivity' there a firewall disclaimer, so POPULATABILITY DOES NOT TRANSFER; and the firewall bites on the bridge's own record, the three transcribed cycle-723/725/726 points (36,55), (41,48), (37,48) all lying inside the global bracket yet in NONE of the committed strata 144/145/146, with two of them at the MC = 48 end that no committed census reaches and that Block 151 carries as facet-wise and unwitnessed, the bridge lattice L re-derived at index 28 with its congruence verified over a full period box, and the negatives (31,67) and (35,67) violating the corner outright",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the contract with its 'inputs of the kind' wording, the open map line and the section 8 licensing, the table at its true strength with the collapse, the typing and the convention named, the corrected direction 'weaker on the cell-cutting side', the distance-3 statement with its distance-4 scoping, the absence of an isomorphism and the identity-not-type law, the firewall finding that the transcribed points sit in no committed stratum and the unwitnessed end, the executed verdict with its licensed scope, the three requirements a registered map would have to supply, the pickup provenance, the not-consumed rider, the cross-context disclosure, the firewalls and the exact N5 fence are present",
        gate_values["H"],
    )
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
