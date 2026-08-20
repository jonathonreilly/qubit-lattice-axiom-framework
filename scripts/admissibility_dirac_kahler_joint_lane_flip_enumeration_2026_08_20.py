#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_joint_lane_flip_enumeration_2026_08_20.py
"""Block 150: THE JOINT-LANE FLIP ENUMERATION -- the Block 130 bridge, executed.

The Block 130 facet-charge bridge closed with a CONDITIONAL: if the cell-cutting
lane's cost-preserving moves realise the facet-charge increments (5, -7) and
(1, -7) -- the differences of the three extremal witnesses it recorded -- then
the lane supplies the sign-indefinite, two-positive-direction increments that
Block 123's definiteness theorem wants for its inputs.  Its Section 8 left a
work order: ENUMERATE THE MOVES AND MEASURE THE ACHIEVED INCREMENTS.  This
runner executes that order against the actual committed cell-cutting machinery,
read at RUN TIME from origin/main, and the answer is a CLOSURE, not a bridge:

  * THE POPULATION INTERSECTION IS EMPTY, AND FOR A STRUCTURAL REASON.  The
    corpus the work order lives on is the 15,800 cost-144 cuttings of the unit
    four-box.  The three bridge witnesses are NOT in it: W1, W5 and W6 have
    four-column cost 165, 159 and 169, each using pieces above the cost floor.
    Stronger, and this is the structural fact: the facet charge is the CONSTANT
    (TC, MC) = (36, 60) on ALL 15,800 cuttings, so not one of the three bridge
    POINTS (36, 55), (41, 48), (37, 48) is attained by any cutting either;
  * THE CONSTANCY IS A FLOOR-MEETS-CEILING LOCK, NOT A COINCIDENCE.  Cost 144 is
    24 x 6, and 6 is the piece floor, so a cost-144 cutting is forced to use 24
    FLOOR pieces and nothing else.  On the induced three-cube facet problem the
    tick facet charge runs over [18, 21] and the mixed facet charge over [8, 10]
    across all 180 facet dissections; a floor cutting puts BOTH tick facets at
    their FLOOR 18 and ALL SIX mixed facets at their CEILING 10.  36 = 2 x 18
    and 60 = 6 x 10: the charge is pinned between a floor and a ceiling with no
    room left, and TC and MC are each separately constant;
  * AND THE PIECE ALGEBRA IS FORCED TOO, WITH AN EXCLUSION CERTIFICATE.  The 400
    floor pieces carry four (TC, MC) types -- (0, 3) x 144, (3, 2) x 96,
    (3, 3) x 112, (3, 4) x 48 -- but only TWO of them ever appear in a cutting.
    The two totals alone force it: n1 + n2 + n3 + n4 = 24 with 3(n2+n3+n4) = 36
    and 3n1 + 2n2 + 3n3 + 4n4 = 60 has the UNIQUE nonnegative solution
    (12, 12, 0, 0).  The (3, 3) and (3, 4) types are EXCLUDED by arithmetic, and
    every cutting is 12 pieces of type (0, 3) and 12 of type (3, 2);
  * THE MOVE SET IS ENUMERATED IN FULL AND ITS ACHIEVED INCREMENT SET IS {(0,0)}.
    The complete pair census over all 124,812,100 pairs of cuttings shows the
    minimal same-class move changes FOUR pieces (46,128 pairs; distances 1, 2, 3
    and 5 do not occur), those pairs re-cut one of exactly 120 eight-corner
    regions in five support families, each region has exactly TWO local-floor
    refills, and the resulting 92,256 DIRECTED flips are INVOLUTIVE, stay inside
    the cost class, land in the corpus, and achieve the increment (0, 0) EVERY
    TIME.  The bridge generators (5, -7) and (1, -7) are realised by zero flips
    in either direction;
  * THE VERDICT IS BRANCH 2 IN ITS STRONGEST FORM, AND THE KILL IS RANK.  The
    achieved lattice L_flip = {(0, 0)} is a PROPER RANK-0 SUBLATTICE of the
    bridge lattice L = {7x + y = 0 mod 28}, whose modulus is re-derived here
    from the witness differences (the 2x2 minor gcd is 28) rather than imported.
    The move ladder [349, 349, 157, 61, 61, 13, 1] is charge-neutral at EVERY
    rung, so the closure is not confined to four-piece moves.  The sharpening
    the note must carry: the bridge does NOT die on irreversibility -- every
    flip is an involution, so the reversibility premise is MET -- it dies on
    RANK, because no nonzero increment is achievable at all;
  * THE BOUNDARY OF THE CLASS IS MEASURED, NOT ASSUMED.  The 288 two-piece
    re-cuts are genuine geometric re-cuts, but every one RAISES the cost (+1 on
    192, +2 on 96), so they are strictly one-way and cannot witness the bridge's
    antecedent.  Their facet deltas -- (0, 0) x 144, (1, 0) x 48, (0, -1) x 48,
    (1, -1) x 48 -- span Z^2 at INDEX 1, so it is the cost class, not the facet
    charge, that confines the walk;
  * AND THE BRIDGE'S SECTION 5 INVERTS.  On this population a nontrivial
    conserved affine facet total DOES exist -- TC and MC each separately -- the
    opposite of the Section 5 finding, which was narrow to three extremal
    witnesses lying outside the population.

Every scientific comparison below is exact integer or exact rational arithmetic;
no float is constructed anywhere in this runner and a float-freedom sweep is
gated; the integer monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: the cell-cutting machinery is NOT re-implemented here.  The
three committed runners are read at RUN TIME with `git show origin/main:<path>`,
their bytes are hashed and compared with the blob pins in gate A (so the pin is
CONTENT-BOUND and not merely a path), and the resulting source is written to a
temporary module and imported.  The cycle-726 runner is imported WHOLE, gates
and all; the cycle-734 and 2026-08-11 runners are imported up to a PINNED CUT
MARKER, which is itself an exact string match against their source, so that the
default gate path stays inside its runtime budget -- everything after the marker
is analysis this block redoes itself, never a definition it needs.  Two honest
consequences are carried: (i) the cycle-734 runner obtains its piece inverses by
float linear algebra and then certifies them by an EXACT integer identity, so
this runner re-derives the same inverses by EXACT ADJUGATE and gates the two
arrays equal, and no value used below comes from the float path; (ii) the
cycle-726 runner reads its cycle-725 dependency receipt by a CWD-relative path,
so the import is performed with the working directory set to the repository
root and its own exit status is captured and gated.

PROVENANCE DISCLOSURE: the four-box, the 2,672 minimal pieces, the cycle-726
facet charges (TC, MC, BX), the cycle-734 four-column cost C4, the cost floor 6,
the 15,800-cutting corpus, the exact-cover search, the separation certificate,
the region/refill machinery, the two-piece tier and the six W1..W6 witnesses are
ALL COMMITTED objects, imported and never re-derived.  The Block 130 bridge note
supplies the three witness points, the two generators, the lattice L and the
Section 8 work order.  This block adds only the enumeration of the achieved
increments, the floor/ceiling and exclusion certificates, the ladder neutrality,
the lattice verdict and the accounting that closes the route.

PICKUP PROVENANCE: this block was picked up on owner direction after a silent
hand-off; the six named cycle-778..799 notes on unmerged branches are ANOTHER
worker's pending state and are NOT consumed, NOT read and NOT superseded here.

HYPOTHESES, named and not imported: (H1) COST CLASS means the level set of the
cycle-734 four-column pair charge C4 summed over a cutting; the corpus is the
class C4 = 144.  The Block 130 work order's phrase "interior-cost class" has no
committed definition and this is the declared resolution.  (H2) FLIP means the
cycle-734 four-piece region swap between a region's two local-floor refills; it
is explicitly NOT the cycle-745/747 binary target vectors named "four" and
"four-flip", and NOT cycle-769's coordinate sign flips.  (H3) an ACHIEVED
INCREMENT is the pair (dTC, dMC) between the endpoints of a move that stays in
the declared class; increments across classes are reported separately, in gate
G, and never mixed into the verdict.  (H4) the supplied-model firewall of cycles
725/726/734 is INHERITED UNCHANGED: one equal-grained tick-box, corner-simplex
pieces, declared spatial-L1 pair charge; nothing here is a statement about
physical ticks, multiple boxes, or the continuum.
"""

from __future__ import annotations

import argparse
from collections import Counter
import contextlib
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
import io
import itertools
from math import gcd
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

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
    "ADMISSIBILITY_DIRAC_KAHLER_JOINT_LANE_FLIP_ENUMERATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK149_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK149_RUNNER = (
    "scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py"
)
BRIDGE_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_ARTIFACTS = (
    BLOCK149_NOTE,
    BLOCK149_RUNNER,
    BRIDGE_NOTE,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_LANE_FLIP_ENUMERATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    # The three cell-cutting runners exist only on origin/main (our branch
    # base predates them); they are content-bound via the gate-A blob pins
    # and read at run time via `git show origin/main:` — never worktree
    # paths, so they must not appear in AUDIT_INPUT_PATHS (the cache
    # envelope stats these paths in the worktree; the Block 130 lesson).
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 149 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 149, so the parent branch is Block 149's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block149-shear-gauge-classification-20260820"
)
# Landing supervisor: replace this placeholder with the Block 149 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise (the parent branch may not be published
# yet); either way the binding is real and verifiable, and the immutable commit
# pin lands with the block.
PARENT_COMMIT = "0b8765449cb7bc11da4b427ad82cc1cc7d0ad854"
# Block 148's tip: a real ancestor that PREDATES the Block 149 note and runner,
# so resolving the parent pin there leaves two of the three artifacts ABSENT.
# It is the honest stale control FOR THIS PIN SET -- an older Block 149-era
# commit would not be, since the bridge note already carries its worktree blob
# far down the branch and a pin resolved there would still certify on it.  This
# pin is read ONLY under the stale mutation; the baseline gate never requires
# the stale blobs to match.
STALE_PARENT_COMMIT = "71ee2f8a9faaf0ff2182b0ad3338869dcecf2890"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

# ---------------------------------------------------------------------------
# the committed cell-cutting machinery, pinned BY CONTENT and read at run time
# ---------------------------------------------------------------------------
# These runners live on origin/main and postdate this branch's base, so they
# cannot be imported from the worktree.  Each is fetched with `git show`, its
# bytes are hashed with git's own blob rule and compared against the pin, and
# the (optionally truncated) source is imported from a temporary module.  The
# CUT MARKER is an exact source line: everything before it is DEFINITION, and
# everything after it is analysis this block performs itself.
C726_PATH = "scripts/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.py"
C726_BLOB = "46f080559c10d90d9803436f294ed660348b638f"
C726_CUT = ""                       # imported whole, gates and all
C734_PATH = (
    "scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.py"
)
C734_BLOB = "ef4cedb4045ad6c476041aab274985fb7efa40fe"
C734_CUT = 'sec("no move on three pieces keeps the cost")'
C811_PATH = "scripts/four_cube_cutting_fixed_point_orbit_floor_2026_08_11.py"
C811_BLOB = "65cade2f6c3dcd92e10fbd146cfd6a3f7f95b744"
C811_CUT = "USED = sorted(set(t for s in SOLS for t in s))"
MACHINERY = (
    ("c726", C726_PATH, C726_BLOB, C726_CUT),
    ("c734", C734_PATH, C734_BLOB, C734_CUT),
    ("c811", C811_PATH, C811_BLOB, C811_CUT),
)
C726_GATES = 32                     # the committed runner's own passing gates
C734_PREFIX_GATES = 21              # gates the imported prefix runs and passes
# (name, source lines, cut line): the cut line is the 0-based index of the
# pinned marker, so it is a THIRD binding on the imported source alongside the
# blob hash and the marker text itself.
MACHINERY_SHAPE = (
    ("c726", 661, 661),
    ("c734", 766, 456),
    ("c811", 1455, 239),
)

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "wrong_corpus_count",
    "break_two_type_law",
    "claim_charge_not_constant",
    "wrong_tick_floor",
    "claim_witness_inside_corpus",
    "wrong_witness_cost_total",
    "wrong_flip_count",
    "claim_nonzero_flip_delta",
    "claim_flip_lattice_is_L",
    "claim_kill_is_irreversibility",
    "claim_two_piece_reversible",
    "claim_charge_not_conserved",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "wrong_corpus_count": "B",
    "break_two_type_law": "B",
    "claim_charge_not_constant": "C",
    "wrong_tick_floor": "C",
    "claim_witness_inside_corpus": "D",
    "wrong_witness_cost_total": "D",
    "wrong_flip_count": "E",
    "claim_nonzero_flip_delta": "E",
    "claim_flip_lattice_is_L": "F",
    "claim_kill_is_irreversibility": "F",
    "claim_two_piece_reversible": "G",
    "claim_charge_not_conserved": "G",
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


def git_bytes(*args: str) -> bytes:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        timeout=AUDIT_TIMEOUT_SEC,
    )


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    """The blob at a path in a commit, or "" when the path is absent there.

    Absence is a real answer here: the stale-pin control deliberately probes a
    commit that predates two of the pinned artifacts.
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

    This is what makes the machinery pins CONTENT-bound: the bytes that are
    actually imported are the bytes that are hashed.
    """
    header = b"blob " + str(len(data)).encode("ascii") + b"\x00"
    return hashlib.sha1(header + data).hexdigest()


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def compact_note(text: str) -> str:
    return "".join(text.lower().split())


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
    machinery_blobs: tuple
    machinery_content_bound: bool


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT):
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(
    main_head: str, machinery: tuple
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
    # The machinery pins bind BOTH ways: origin/main must record the pinned
    # blob at the pinned path, AND the bytes this runner actually imported must
    # hash to it.  The second half is the content binding.
    machinery_named = tuple(
        (name, commit_blob("origin/main", path), record.digest, record.pin)
        for (name, path, _pin, _cut), record in zip(MACHINERY, machinery)
    )
    machinery_content_bound = all(
        recorded == digest == pin and is_hash(pin)
        for _name, recorded, digest, pin in machinery_named
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
        ),
        bool(
            len(stale_blobs) == len(PARENT_ARTIFACTS)
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
        machinery_named,
        machinery_content_bound,
    )


# ---------------------------------------------------------------------------
# the machinery loader: git show -> hash -> cut at a pinned marker -> import
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class MachineryRecord:
    name: str
    path: str
    pin: str
    digest: str
    total_lines: int
    cut_line: int
    exit_code: object
    module: object


def load_machinery(name: str, path: str, pin: str, marker: str, workdir: Path):
    """Read a committed runner from origin/main and import it, exactly.

    The bytes are hashed before anything else happens; the marker, when given,
    must occur EXACTLY ONCE as a full source line, so the cut is as pinned as
    the blob.  The module is written under `<workdir>/scripts/` so that any
    `parents[1]`-relative artifact a runner writes lands in the temporary tree
    and never in the repository.
    """
    data = git_bytes("show", f"origin/main:{path}")
    digest = blob_sha1(data)
    text = data.decode("utf-8")
    lines = text.split("\n")
    if marker:
        hits = [i for i, line in enumerate(lines) if line == marker]
        if len(hits) != 1:
            raise AssertionError(f"{name}: cut marker is not unique: {hits}")
        cut_line = hits[0]
        source = "\n".join(lines[:cut_line])
    else:
        cut_line = len(lines)
        source = text

    target = workdir / "scripts" / f"block150_{name}.py"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source, encoding="utf-8")

    spec = importlib.util.spec_from_file_location(f"block150_{name}", target)
    module = importlib.util.module_from_spec(spec)
    buffer = io.StringIO()
    exit_code: object = None
    previous = Path.cwd()
    try:
        # The cycle-726 runner reads its cycle-725 dependency receipt by a
        # CWD-relative path, so every import is performed from the repo root.
        os.chdir(ROOT)
        with contextlib.redirect_stdout(buffer):
            try:
                spec.loader.exec_module(module)
            except SystemExit as stop:      # the committed runners exit at end
                exit_code = stop.code
    finally:
        os.chdir(previous)
    return MachineryRecord(
        name, path, pin, digest, len(lines), cut_line, exit_code, module
    )


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
CORNERS = 16
PIECE_CANDIDATES = 4368                  # C(16, 5)
PIECES = 2672                            # normalized volume one
VOLUME_SPECTRUM = ((0, 1360), (1, 2672), (2, 320), (3, 16))
COST_SPECTRUM = ((6, 400), (7, 1216), (8, 864), (9, 192))
PIECE_COST_FLOOR = 6
FLOOR_PIECES = 400
CUTTING_SIZE = 24
COST_CLASS = 144                         # 24 x 6
CORPUS = 15800
SEARCH_NODES = 502838
POOL_PIECES = 192
POOL_ORBITS = 4
COOCCURRING_PAIRS = 15168

FACETS = 8
TICK_FACETS = 2
MIXED_FACETS = 6
TICK_FLOOR = 18
TICK_CEILING = 21
MIXED_FLOOR = 8
MIXED_CEILING = 10
FACET_DISSECTIONS = 180                  # of the induced three-cube
FACET_TETS = 6
TICK_SPECTRUM = ((18, 16), (19, 72), (20, 84), (21, 8))
MIXED_SPECTRUM = ((8, 12), (9, 64), (10, 104))
CORPUS_CHARGE = (36, 60)                 # (TC, MC) = (2 x 18, 6 x 10)
CORPUS_FACET_TOTAL = 96
CORPUS_BOX_CHARGE = 108
FLOOR_PIECE_TYPES = (((0, 3), 144), ((3, 2), 96), ((3, 3), 112), ((3, 4), 48))
POOL_PIECE_TYPES = (((0, 3), 96), ((3, 2), 96))
EXCLUDED_TYPES = ((3, 3), (3, 4))
TYPE_SOLUTION = (12, 12, 0, 0)
BALANCE_LAW = (12, 12, 12)
PER_CUTTING_TYPES = ((((0, 3), 12), ((3, 2), 12)),)

WITNESS_NAMES = ("W1", "W2", "W3", "W4", "W5", "W6")
WITNESS_ROWS = {                         # (TC, MC, FC, BX) from cycle 726
    "W1": (37, 48, 85, 108),
    "W2": (36, 60, 96, 108),
    "W3": (39, 49, 88, 110),
    "W4": (42, 60, 102, 128),
    "W5": (36, 55, 91, 110),
    "W6": (41, 48, 89, 110),
}
WITNESS_COST = (                         # the four-column cost C4 of each
    ("W1", 165), ("W2", 144), ("W3", 168), ("W4", 168),
    ("W5", 159), ("W6", 169),
)
WITNESSES_IN_CORPUS = ("W2",)
BRIDGE_POINTS = (("P0", (36, 55)), ("P1", (41, 48)), ("P2", (37, 48)))
BRIDGE_DELTAS = ((5, -7), (1, -7))
BRIDGE_MODULUS = 28                      # L = {7x + y = 0 mod 28}
BRIDGE_CHARACTER = (7, 1)
BRIDGE_INDEX = 28

TOTAL_PAIRS = 124812100                  # C(15800, 2)
DISJOINT_PAIRS = 29069284
D4_PAIRS = 46128
ABSENT_DISTANCES = (1, 2, 3, 5)
DISTANCE_SUPPORT = (4,) + tuple(range(6, 25))
COMPONENTS_K4 = 349
LADDER = (349, 349, 157, 61, 61, 13, 1)  # k = 4 .. 10, cumulative
REGIONS = 120
REGION_CORNERS = 8
SUPPORT_FAMILIES = 5
FAMILY_SIZES = (12, 12, 24, 24, 48)
REGION_CANDIDATES = (8, 32)
REGION_REFILLS = (2, 24)
REGION_LOCAL_FLOOR = 24                  # 4 x 6
FLOOR_REFILLS_PER_REGION = 2
REFILL_TOTAL = 2352                      # incidence refills over the 120 regions
DIRECTED_FLIPS = 92256                   # 2 x 46128
ACHIEVED_DELTAS = ((0, 0),)
FLIP_LATTICE_RANK = 0
KILL_REASON = "rank"

TWO_PIECE_PAIRS = 288
TWO_PIECE_COST_DELTAS = ((1, 192), (2, 96))
TWO_PIECE_FACET_DELTAS = (
    ((0, -1), 48), ((0, 0), 144), ((1, -1), 48), ((1, 0), 48)
)
TWO_PIECE_SPAN_INDEX = 1
CONSERVED_FUNCTIONALS = ((1, 0), (0, 1))
CORRECTIONS = 9
RUNTIME_BUDGET_SEC = 600


# ---------------------------------------------------------------------------
# exact helpers: integer determinants, adjugate inverses, union-find
# ---------------------------------------------------------------------------
def idet(matrix) -> int:
    """Exact integer determinant by cofactor expansion (list of lists)."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    total = 0
    for column in range(size):
        if matrix[0][column] == 0:
            continue
        minor = [
            [row[c] for c in range(size) if c != column]
            for row in matrix[1:]
        ]
        total += ((-1) ** column) * matrix[0][column] * idet(minor)
    return total


def adjugate_inverse(matrix) -> list:
    """Exact integer inverse of a unimodular integer matrix, by adjugate."""
    determinant = idet(matrix)
    if determinant not in (1, -1):
        raise AssertionError(f"not unimodular: {determinant}")
    size = len(matrix)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            minor = [
                [matrix[r][c] for c in range(size) if c != i]
                for r in range(size)
                if r != j
            ]
            result[i][j] = ((-1) ** (i + j)) * idet(minor) // determinant
    return result


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        parent = self.parent
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        a, b = self.find(left), self.find(right)
        if a != b:
            self.parent[a] = b

    def components(self) -> int:
        return len({self.find(i) for i in range(len(self.parent))})


def three_cube_certificate() -> tuple:
    """The induced facet problem, re-derived here and NOT imported.

    Enumerates every unimodular tetrahedron of the unit three-cube, every exact
    dissection of the cube by them (via an exact integer interior-sample cover),
    and the two charge spectra: the TICK facet charge (all three axes) and the
    MIXED facet charge (two axes).  Returns (dissections, sizes, tick, mixed).
    All arithmetic is exact integer; the sample weights are superincreasing so
    that no sample point can land on a facet plane, which is asserted.
    """
    cube = [[(k >> (2 - j)) & 1 for j in range(3)] for k in range(8)]
    tets = []
    for choice in itertools.combinations(range(8), 4):
        edges = [
            [cube[choice[r + 1]][c] - cube[choice[0]][c] for c in range(3)]
            for r in range(3)
        ]
        if abs(idet(edges)) == 1:
            tets.append(list(choice))

    weights = (1, 7, 49, 343)
    scale = sum(weights)
    inverses = [
        adjugate_inverse(
            [
                [cube[t[r + 1]][c] - cube[t[0]][c] for c in range(3)]
                for r in range(3)
            ]
        )
        for t in tets
    ]
    # One weighted interior point per unimodular tetrahedron; the weights are
    # superincreasing, so no such point can land on any facet plane, which is
    # not assumed but COUNTED (the returned boundary-incidence count is zero).
    points = sorted(
        {
            tuple(
                sum(weights[r] * cube[tet[r]][c] for r in range(4))
                for c in range(3)
            )
            for tet in tets
        }
    )
    masks, boundary_hits = [], 0
    for index, tet in enumerate(tets):
        bits = 0
        for slot, point in enumerate(points):
            shifted = [
                point[c] - scale * cube[tet[0]][c] for c in range(3)
            ]
            mu = [
                sum(shifted[r] * inverses[index][r][k] for r in range(3))
                for k in range(3)
            ]
            if any(value == 0 for value in mu) or sum(mu) == scale:
                boundary_hits += 1
            if all(value > 0 for value in mu) and sum(mu) < scale:
                bits |= 1 << slot
        masks.append(bits)

    universe = (1 << len(points)) - 1
    solutions: list[tuple] = []

    def search(covered: int, chosen: list) -> None:
        if covered == universe:
            solutions.append(tuple(chosen))
            return
        free = universe & ~covered
        slot = (free & -free).bit_length() - 1
        for index in range(len(tets)):
            if masks[index] >> slot & 1 and not masks[index] & covered:
                chosen.append(index)
                search(covered | masks[index], chosen)
                chosen.pop()

    search(0, [])

    def cost(index: int, axes: tuple) -> int:
        vertices = [cube[k] for k in tets[index]]
        return sum(
            1
            for a, b in itertools.combinations(range(4), 2)
            if sum(abs(vertices[a][c] - vertices[b][c]) for c in axes) > 1
        )

    tick = Counter(
        sum(cost(t, (0, 1, 2)) for t in solution) for solution in solutions
    )
    mixed = Counter(
        sum(cost(t, (0, 1)) for t in solution) for solution in solutions
    )
    return (
        len(solutions),
        tuple(sorted({len(s) for s in solutions})),
        tuple(sorted(tick.items())),
        tuple(sorted(mixed.items())),
        boundary_hits,
    )


def type_exclusion_certificate(types: tuple, tick: int, mixed: int) -> tuple:
    """Every nonnegative piece-type census obeying the two facet totals.

    `types` is the (TC, MC) type list of the floor pieces.  A cost-class cutting
    uses CUTTING_SIZE pieces with tick total `tick` and mixed total `mixed`;
    this enumerates EVERY nonnegative integer solution of those three linear
    equations, so a unique answer is an EXCLUSION PROOF and not a census.
    """
    solutions = []
    ranges = [range(CUTTING_SIZE + 1)] * (len(types) - 1)
    for head in itertools.product(*ranges):
        last = CUTTING_SIZE - sum(head)
        if last < 0:
            continue
        counts = head + (last,)
        if sum(c * t[0] for c, t in zip(counts, types)) != tick:
            continue
        if sum(c * t[1] for c, t in zip(counts, types)) != mixed:
            continue
        solutions.append(counts)
    return tuple(solutions)


def lattice_from_generators(
    generators: tuple, character: tuple, modulus: int
) -> tuple:
    """Re-derive the bridge lattice L from the WITNESS DIFFERENCES.

    Returns (index, entry gcd, congruence verified).  The index is the gcd of
    the 2x2 minors of the generator matrix -- for two generators in Z^2 that is
    |det| -- and it is computed here, not imported.  The claimed congruence
    description a x + b y = 0 mod m is then VERIFIED, not assumed: over a full
    period box every lattice point is checked to satisfy it and every point
    satisfying it is checked to be an exact integer combination of the
    generators, membership being decided by exact Cramer division.
    """
    (x1, y1), (x2, y2) = generators[0], generators[1]
    determinant = x1 * y2 - x2 * y1
    index = abs(determinant)
    entry_gcd = 0
    for value in (x1, y1, x2, y2):
        entry_gcd = gcd(entry_gcd, abs(value))
    verified = index == modulus and determinant != 0
    for x in range(-index, index + 1):
        for y in range(-index, index + 1):
            by_character = (
                character[0] * x + character[1] * y
            ) % modulus == 0
            a_numerator = x * y2 - x2 * y
            b_numerator = x1 * y - x * y1
            by_solve = (
                a_numerator % determinant == 0
                and b_numerator % determinant == 0
            )
            if by_character != by_solve:
                verified = False
    return int(index), int(entry_gcd), bool(verified)


# ---------------------------------------------------------------------------
# THE NINE CARRIED CORRECTIONS to the Block 130 bridge note
# ---------------------------------------------------------------------------
# Recorded here so the count is a checked object and not a prose claim; M1, M4
# and M7 are MEASURED below (gates D, D and A respectively), the rest are
# resolutions or scope statements the note carries.
CORRECTION_IDS = ("M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9")
CORRECTION_TITLES = (
    "the three literals are all cycle-726 witnesses, not 723/725/726",
    "the ((1,192),(2,96)) histogram is the two-piece COST-INCREASE spectrum",
    "the two generators are witness differences, not realised moves",
    "the population intersection is empty",
    "'interior-cost class' is undefined and is resolved by declaration (H1)",
    "the 'frame covering' is unsourced and internally impossible",
    "the cycle-767 pin is valid REACHABLE history, merely not a main-tip path",
    "'flip' is overloaded in the lane and is resolved by declaration (H2)",
    "two recon-scope names have no lane referent: carried, NOT consumed",
)
# M7's own pin, checked in gate A: the bridge note cites this commit/blob pair
# for a path that origin/main's TIP no longer carries (it was renamed on merge).
C767_COMMIT = "64ed8d38b68c53e0e1df55a81ed2bf3dd685d0b3"
C767_BLOB = "82dcb69e9e47ce0211552d4f5e9ac595246e6c25"
C767_PATH = "docs/PHYSICAL_CELL_CUTTING_ORBIT_STRATA_CYCLE767_NOTE_2026-08-09.md"


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    machinery: tuple
    machinery_exit: tuple
    c767_pin: tuple
    # B: the corpus
    corner_orders_agree: bool
    piece_lists_agree: bool
    volume_spectrum: tuple
    cost_spectrum: tuple
    exact_inverses_agree: bool
    corpus: tuple
    search_nodes: int
    cutting_sizes: tuple
    pool_pieces: int
    pool_orbits: int
    cost_sums: tuple
    floor_forcing: bool
    floor_types: tuple
    pool_types: tuple
    type_solutions: tuple
    balance_law: tuple
    per_cutting_types: tuple
    cooccurring_pairs: tuple
    independent_corpus: tuple
    # C: the constant charge
    charge_points: tuple
    charge_multiplicity: int
    facet_split_reconstructs: bool
    tick_facet_totals: tuple
    mixed_facet_totals: tuple
    box_charge: tuple
    committed_tick_spectrum: tuple
    committed_mixed_spectrum: tuple
    own_three_cube: tuple
    facet_bracket: tuple
    charge_is_floor_times_ceiling: bool
    # D: gate 0
    witness_rows: tuple
    witness_costs: tuple
    witnesses_in_corpus: tuple
    bridge_point_hits: tuple
    bridge_points_are_cycle726: bool
    # E: the walk
    distance_support: tuple
    distance_total: int
    d4_pairs: tuple
    disjoint_pairs: int
    regions: tuple
    region_families: tuple
    region_refills: tuple
    refill_geometry: tuple
    deep_separation: tuple
    flip_attempts: tuple
    directed_flips: tuple
    involution: tuple
    same_cost_class: bool
    images_in_corpus: bool
    achieved_deltas: tuple
    deltas_by_family: tuple
    # F: the verdict structure
    flip_lattice_rank: int
    flip_lattice: tuple
    bridge_lattice: tuple
    generators_from_witnesses: tuple
    generators_unrealised: tuple
    proper_sublattice: bool
    ladder: tuple
    ladder_charge_neutral: bool
    components_k4: int
    reversibility_premise: bool
    kill_reason: str
    # G: the boundary classes
    two_piece_pairs: int
    two_piece_cost_deltas: tuple
    two_piece_cost_raising: bool
    two_piece_geometric: int
    two_piece_facet_deltas: tuple
    two_piece_span: tuple
    conserved_functionals: tuple
    corrections: tuple
    # global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")

    # --- the committed machinery, content-bound and imported at run time -----
    workdir = Path(tempfile.mkdtemp(prefix="block150-machinery-"))
    try:
        records = tuple(
            load_machinery(name, path, pin, cut, workdir)
            for name, path, pin, cut in MACHINERY
        )
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
    c726, c734, c811 = (record.module for record in records)
    authority = authority_certificate(main_head, records)
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
    # M7: the bridge note's cycle-767 pin is reachable history even though the
    # path it names is absent from origin/main's tip.
    c767_pin = (
        resolve_ref(C767_COMMIT + "^{commit}") == C767_COMMIT,
        is_ancestor(C767_COMMIT, "origin/main"),
        commit_blob(C767_COMMIT, C767_PATH) == C767_BLOB,
        commit_blob("origin/main", C767_PATH) == "",
    )

    # --- the shared fixture ---------------------------------------------------
    corner_orders_agree = [
        tuple(int(value) for value in c726.COR[k]) for k in range(CORNERS)
    ] == [tuple(corner) for corner in c734.CORN]
    piece_lists_agree = [tuple(cell) for cell in c726.CELL] == [
        tuple(int(value) for value in row) for row in c734.UNI
    ]
    volume_spectrum = tuple(sorted(c726.SPEC.items()))
    cost_values, cost_counts = np.unique(c734.C4, return_counts=True)
    cost_spectrum = tuple(
        (int(value), int(count)) for value, count in zip(cost_values, cost_counts)
    )
    # The committed cycle-734 runner inverts its piece matrices in FLOATING
    # POINT and then certifies the result by an exact integer identity.  Here
    # the same inverses are re-derived by EXACT ADJUGATE and the two integer
    # arrays are required equal, so nothing below depends on the float path.
    exact_inverses_agree = True
    for index in range(len(c734.UNI)):
        edges = [
            [
                int(c734.V[c734.UNI[index][r + 1]][c] - c734.V[c734.UNI[index][0]][c])
                for r in range(4)
            ]
            for c in range(4)
        ]
        if [list(map(int, row)) for row in adjugate_inverse(edges)] != [
            [int(value) for value in row] for row in c734.IV[index]
        ]:
            exact_inverses_agree = False
            break

    TC, MC, BX = c726.TC, c726.MC, c726.BX
    C4 = c734.C4
    SOL = c734.SOL
    USED = c734.USED
    MASK = c734.MASK
    SSET = [set(cutting) for cutting in SOL]
    SFRZ = {frozenset(cutting) for cutting in SOL}
    INDEX_OF = {cutting: position for position, cutting in enumerate(SOL)}

    # --- B: the corpus --------------------------------------------------------
    cost_sums = np.array(
        [int(C4[list(cutting)].sum()) for cutting in SOL], dtype=np.int64
    )
    floor_forcing = bool(
        int(C4.min()) == PIECE_COST_FLOOR
        and CUTTING_SIZE * PIECE_COST_FLOOR == COST_CLASS
        and all(len(cutting) == CUTTING_SIZE for cutting in SOL)
        and bool((cost_sums == COST_CLASS).all())
        # equality in "24 pieces, each at least the floor" forces every piece
        # to sit exactly at the floor; verified rather than argued
        and all(int(C4[piece]) == PIECE_COST_FLOOR for piece in USED)
    )
    floor_types = tuple(
        sorted(
            Counter(
                (int(TC[piece]), int(MC[piece])) for piece in c734.MINP
            ).items()
        )
    )
    pool_types = tuple(
        sorted(
            Counter((int(TC[piece]), int(MC[piece])) for piece in USED).items()
        )
    )
    type_solutions = type_exclusion_certificate(
        tuple(pair for pair, _count in floor_types),
        CORPUS_CHARGE[0],
        CORPUS_CHARGE[1],
    )
    balance = {
        (
            sum(1 for piece in cutting if int(TC[piece]) == 3),
            sum(1 for piece in cutting if int(MC[piece]) == 3),
            sum(1 for piece in cutting if int(BX[piece]) == 5),
        )
        for cutting in SOL
    }
    per_cutting_types = tuple(
        sorted(
            {
                tuple(
                    sorted(
                        Counter(
                            (int(TC[piece]), int(MC[piece])) for piece in cutting
                        ).items()
                    )
                )
                for cutting in SOL
            }
        )
    )
    cooccurring_pairs = (len(c734.CP), int(c734.SEP))
    independent_corpus = (
        len(c811.SOLS),
        int(c811.FLOOR),
        int(c811.NKEPT),
        bool(c811.GENERIC),
        {
            frozenset(
                frozenset(
                    tuple(int(value) for value in c734.V[corner])
                    for corner in c734.UNI[piece]
                )
                for piece in cutting
            )
            for cutting in SOL
        }
        == {
            frozenset(
                frozenset(c811.CORN[corner] for corner in c811.KEPT[piece])
                for piece in cutting
            )
            for cutting in c811.SOLS
        },
    )

    # --- C: the constant charge ----------------------------------------------
    tick_sums = np.array(
        [int(TC[list(cutting)].sum()) for cutting in SOL], dtype=np.int64
    )
    mixed_sums = np.array(
        [int(MC[list(cutting)].sum()) for cutting in SOL], dtype=np.int64
    )
    box_sums = np.array(
        [int(BX[list(cutting)].sum()) for cutting in SOL], dtype=np.int64
    )
    charge_counter = Counter(zip(tick_sums.tolist(), mixed_sums.tolist()))
    charge_points = tuple(sorted(charge_counter.items()))

    # the per-facet split of the committed charge, re-derived and then GATED
    # against the committed per-piece totals
    facet_cost = np.zeros((len(c734.UNI), FACETS), dtype=np.int64)
    for piece in range(len(c734.UNI)):
        vertices = c726.V4[piece]
        for slot, (axis, side) in enumerate(c726.FAC):
            face = [a for a in range(5) if int(vertices[a][axis]) == side]
            if len(face) != 4:
                continue
            others = [j for j in range(3) if j != axis]
            facet_cost[piece, slot] = sum(
                1
                for a, b in itertools.combinations(face, 2)
                if sum(
                    abs(int(vertices[a][j]) - int(vertices[b][j]))
                    for j in others
                )
                > 1
            )
    tick_slots = [s for s, (axis, _side) in enumerate(c726.FAC) if axis == 3]
    mixed_slots = [s for s, (axis, _side) in enumerate(c726.FAC) if axis < 3]
    facet_split_reconstructs = bool(
        (facet_cost[:, tick_slots].sum(axis=1) == TC).all()
        and (facet_cost[:, mixed_slots].sum(axis=1) == MC).all()
    )
    per_facet = np.array(
        [facet_cost[list(cutting)].sum(axis=0) for cutting in SOL],
        dtype=np.int64,
    )
    tick_facet_totals = tuple(
        sorted({int(value) for value in per_facet[:, tick_slots].ravel()})
    )
    mixed_facet_totals = tuple(
        sorted({int(value) for value in per_facet[:, mixed_slots].ravel()})
    )
    committed_tick_spectrum = tuple(
        tuple(sorted(Counter(c726.SCOST[slot].tolist()).items()))
        for slot in tick_slots
    )
    committed_mixed_spectrum = tuple(
        tuple(sorted(Counter(c726.SCOST[slot].tolist()).items()))
        for slot in mixed_slots
    )
    own_three_cube = three_cube_certificate()
    facet_bracket = (
        TICK_FACETS * TICK_FLOOR + MIXED_FACETS * MIXED_FLOOR,
        TICK_FACETS * TICK_CEILING + MIXED_FACETS * MIXED_CEILING,
    )
    charge_is_floor_times_ceiling = bool(
        TICK_FACETS * TICK_FLOOR == CORPUS_CHARGE[0]
        and MIXED_FACETS * MIXED_CEILING == CORPUS_CHARGE[1]
        and own_three_cube[2][0][0] == TICK_FLOOR
        and own_three_cube[3][-1][0] == MIXED_CEILING
    )

    # --- D: gate 0 ------------------------------------------------------------
    selections = {name: list(c726.SEL[name]) for name in WITNESS_NAMES}
    witness_rows = tuple(
        (name, tuple(int(value) for value in c726.ROW[name][:4]))
        for name in WITNESS_NAMES
    )
    witness_costs = tuple(
        (name, int(C4[selections[name]].sum())) for name in WITNESS_NAMES
    )
    witnesses_in_corpus = tuple(
        name
        for name in WITNESS_NAMES
        if frozenset(selections[name]) in SFRZ
    )
    bridge_point_hits = tuple(
        (label, int(charge_counter.get(point, 0)))
        for label, point in BRIDGE_POINTS
    )
    bridge_points_are_cycle726 = bool(
        tuple(int(v) for v in c726.ROW["W5"][:2]) == BRIDGE_POINTS[0][1]
        and tuple(int(v) for v in c726.ROW["W6"][:2]) == BRIDGE_POINTS[1][1]
        and tuple(int(v) for v in c726.ROW["W1"][:2]) == BRIDGE_POINTS[2][1]
    )

    # --- E: the walk ----------------------------------------------------------
    # The complete pair census, by exact bit arithmetic: the packed 192-bit
    # membership word of each cutting, popcount by table lookup, distance
    # 24 - |intersection|.  Nothing here is a float and nothing is sampled.
    pool_position = c734.P2I
    indicator = np.zeros((len(SOL), len(USED)), dtype=np.uint8)
    for row, cutting in enumerate(SOL):
        indicator[row, [pool_position[piece] for piece in cutting]] = 1
    packed = np.packbits(indicator, axis=1)
    popcount = np.array(
        [bin(value).count("1") for value in range(256)], dtype=np.uint8
    )
    histogram = np.zeros(CUTTING_SIZE + 1, dtype=np.int64)
    ladder_edges: dict[int, list] = {k: [] for k in range(4, 11)}
    stride = 200
    for low in range(0, len(SOL), stride):
        chunk = packed[low:low + stride]
        shared = popcount[
            np.bitwise_and(chunk[:, None, :], packed[None, :, :])
        ].sum(axis=2).astype(np.int64)
        distance = CUTTING_SIZE - shared
        for rung in ladder_edges:
            rows, columns = np.nonzero(distance == rung)
            keep = (rows + low) < columns
            if keep.any():
                ladder_edges[rung].append(
                    np.stack([rows[keep] + low, columns[keep]]).astype(np.int32)
                )
        for offset in range(chunk.shape[0]):
            histogram += np.bincount(
                distance[offset, low + offset + 1:], minlength=CUTTING_SIZE + 1
            )
    edges4 = np.concatenate(ladder_edges[4], axis=1)
    distance_support = tuple(
        k for k in range(CUTTING_SIZE + 1) if int(histogram[k])
    )
    distance_total = int(histogram.sum())
    d4_pairs = (int(histogram[4]), int(edges4.shape[1]))
    disjoint_pairs = int(histogram[CUTTING_SIZE])

    # the regions: the eight corners a minimal move re-cuts
    region_count: dict[tuple, int] = {}
    region_edge: dict[tuple, tuple] = {}
    region_symmetric = True
    for column in range(edges4.shape[1]):
        left, right = int(edges4[0, column]), int(edges4[1, column])
        key = c734.span(sorted(SSET[left] - SSET[right]))
        if c734.span(sorted(SSET[right] - SSET[left])) != key:
            region_symmetric = False
        region_count[key] = region_count.get(key, 0) + 1
        region_edge.setdefault(key, (left, right))
    ordered_regions = sorted(region_count)
    regions = (
        len(region_count),
        len({key[0] for key in region_count}),
        sum(region_count.values()),
        region_symmetric,
        tuple(sorted({bin(key[0]).count("1") for key in region_count})),
    )

    canonical: dict[int, list] = {}
    for key in ordered_regions:
        images = []
        for (_rotation, _time_flip, corner_map) in c734.G:
            word = 0
            for corner in range(CORNERS):
                if key[0] >> corner & 1:
                    word |= 1 << int(corner_map[corner])
            images.append(word)
        canonical.setdefault(min(images), []).append(key)
    family_of: dict[tuple, int] = {}
    family_size: dict[int, int] = {}
    for family, (_representative, keys) in enumerate(sorted(canonical.items())):
        family_size[family] = len(keys)
        for key in keys:
            family_of[key] = family
    region_families = (
        len(canonical),
        tuple(sorted(len(keys) for keys in canonical.values())),
    )

    refill_data: dict[tuple, tuple] = {}
    for key in ordered_regions:
        candidates, filled = c734.refills(key[0], key[1], 4, c734.ALLI, c734.CM)
        local_costs = [sum(int(C4[piece]) for piece in option) for option in filled]
        floor_options = [
            option
            for option, cost in zip(filled, local_costs)
            if cost == REGION_LOCAL_FLOOR
        ]
        refill_data[key] = (
            candidates, len(filled), min(local_costs), floor_options, filled
        )
    region_refills = (
        tuple(sorted({value[0] for value in refill_data.values()})),
        tuple(sorted({value[1] for value in refill_data.values()})),
        tuple(sorted({value[2] for value in refill_data.values()})),
        tuple(sorted({len(value[3]) for value in refill_data.values()})),
    )

    # every incidence-compatible refill is a GENUINE geometric re-cut: the
    # separation certificate is the committed cycle-734 routine, memoised, and
    # seeded with the 15,168 co-occurring pairs it already certified.
    separation_cache: dict[tuple, bool] = {}
    for left, right in c734.CP:
        pair = (USED[left], USED[right])
        separation_cache[(min(pair), max(pair))] = True

    def apart(left: int, right: int) -> bool:
        pair = (left, right) if left < right else (right, left)
        value = separation_cache.get(pair)
        if value is None:
            value = c734.separated([pair[0], pair[1]])[0] == 1
            separation_cache[pair] = value
        return value

    def genuine(key: tuple, refill: tuple) -> bool:
        left, right = region_edge[key]
        candidate = sorted(SSET[left] & SSET[right]) + list(refill)
        if len(set(candidate)) != CUTTING_SIZE:
            return False
        covered = 0
        for piece in candidate:
            covered |= MASK[piece]
        return bool(
            covered == c734.ALLQ
            and all(
                apart(x, y) for x, y in itertools.combinations(candidate, 2)
            )
        )

    refill_geometry = (
        len(ordered_regions),
        sum(len(refill_data[key][4]) for key in ordered_regions),
        sum(
            1
            for key in ordered_regions
            for option in refill_data[key][4]
            if genuine(key, option)
        ),
    )
    # --deep lifts the one convenience above: the memo was SEEDED with the
    # 15,168 co-occurring pairs the committed prefix had already certified, so
    # the deep pass re-derives every one of them from scratch, cache-free, in
    # this process.
    deep_separation = (0, 0)
    if deep:
        deep_separation = (
            len(c734.CP),
            sum(
                c734.separated([USED[left], USED[right]])[0]
                for left, right in c734.CP
            ),
        )

    # the flips themselves
    hosts_by_piece: dict[int, set] = {}
    for position, cutting in enumerate(SOL):
        for piece in cutting:
            hosts_by_piece.setdefault(piece, set()).add(position)
    attempts = 0
    flip_rows: list[tuple] = []
    forward = back = 0
    for identifier, key in enumerate(ordered_regions):
        first, second = refill_data[key][3][0], refill_data[key][3][1]
        pairs = ((set(first), set(second)), (set(second), set(first)))
        for direction, (leaving, arriving) in enumerate(pairs):
            hosts = set.intersection(
                *[hosts_by_piece[piece] for piece in leaving]
            )
            for host in sorted(hosts):
                attempts += 1
                image = (SSET[host] - leaving) | arriving
                if frozenset(image) not in SFRZ:
                    continue
                target = INDEX_OF[tuple(sorted(image))]
                flip_rows.append((identifier, direction, host, target, key))
                if direction == 0:
                    forward += 1
                    if ((image - arriving) | leaving) == SSET[host]:
                        back += 1
    flip_attempts = (attempts, len(flip_rows))
    directed_flips = (len(flip_rows), DIRECTED_FLIPS)
    involution = (forward, back, d4_pairs[0])
    identifiers = {
        (identifier, direction, host)
        for identifier, direction, host, _target, _key in flip_rows
    }
    reverse_closure = all(
        (identifier, 1 - direction, target) in identifiers
        for identifier, direction, _host, target, _key in flip_rows
    )
    same_cost_class = all(
        int(cost_sums[host]) == COST_CLASS and int(cost_sums[target]) == COST_CLASS
        for _identifier, _direction, host, target, _key in flip_rows
    )
    delta_counter = Counter(
        (
            int(tick_sums[target]) - int(tick_sums[host]),
            int(mixed_sums[target]) - int(mixed_sums[host]),
        )
        for _identifier, _direction, host, target, _key in flip_rows
    )
    achieved_deltas = tuple(sorted(delta_counter.items()))
    family_deltas: dict[int, Counter] = {
        family: Counter() for family in sorted(family_size)
    }
    for _identifier, _direction, host, target, key in flip_rows:
        family_deltas[family_of[key]][
            (
                int(tick_sums[target]) - int(tick_sums[host]),
                int(mixed_sums[target]) - int(mixed_sums[host]),
            )
        ] += 1
    deltas_by_family = tuple(
        (family, tuple(sorted(counter.items())))
        for family, counter in sorted(family_deltas.items())
    )

    # --- F: the verdict structure --------------------------------------------
    achieved_set = tuple(delta for delta, _count in achieved_deltas)
    nonzero = [delta for delta in achieved_set if delta != (0, 0)]
    if not nonzero:
        flip_lattice_rank = 0
    elif all(
        nonzero[0][0] * other[1] - nonzero[0][1] * other[0] == 0
        for other in nonzero
    ):
        flip_lattice_rank = 1
    else:
        flip_lattice_rank = 2
    witness_point = {name: tuple(int(v) for v in c726.ROW[name][:2])
                     for name in WITNESS_NAMES}
    generators_from_witnesses = (
        (
            witness_point["W6"][0] - witness_point["W5"][0],
            witness_point["W6"][1] - witness_point["W5"][1],
        ),
        (
            witness_point["W1"][0] - witness_point["W5"][0],
            witness_point["W1"][1] - witness_point["W5"][1],
        ),
    )
    bridge_lattice = lattice_from_generators(
        generators_from_witnesses, BRIDGE_CHARACTER, BRIDGE_MODULUS
    )
    generators_unrealised = tuple(
        (
            generator,
            int(delta_counter.get(generator, 0))
            + int(delta_counter.get((-generator[0], -generator[1]), 0)),
        )
        for generator in generators_from_witnesses
    )

    def in_bridge_lattice(delta: tuple) -> bool:
        return (
            BRIDGE_CHARACTER[0] * delta[0] + BRIDGE_CHARACTER[1] * delta[1]
        ) % BRIDGE_MODULUS == 0

    proper_sublattice = bool(
        all(in_bridge_lattice(delta) for delta in achieved_set)
        and any(
            in_bridge_lattice(generator) and generator not in achieved_set
            for generator in generators_from_witnesses
        )
        and flip_lattice_rank < 2
    )

    ladder_state = DisjointSet(len(SOL))
    ladder: list[int] = []
    ladder_charge_neutral = True
    for rung in range(4, 11):
        for piece_of_edges in ladder_edges[rung]:
            for column in range(piece_of_edges.shape[1]):
                ladder_state.union(
                    int(piece_of_edges[0, column]), int(piece_of_edges[1, column])
                )
        ladder.append(ladder_state.components())
        charges: dict[int, set] = {}
        for position in range(len(SOL)):
            charges.setdefault(ladder_state.find(position), set()).add(
                (int(tick_sums[position]), int(mixed_sums[position]))
            )
        if any(len(value) != 1 for value in charges.values()):
            ladder_charge_neutral = False
    reversibility_premise = bool(
        forward == d4_pairs[0] and back == forward and reverse_closure
        and same_cost_class
    )
    kill_reason = (
        "rank"
        if reversibility_premise and flip_lattice_rank < 2
        else "irreversibility"
    )

    # --- G: the boundary classes ---------------------------------------------
    two_piece_facet: Counter = Counter()
    for pair in c734.FLIP:
        base_tick = int(TC[pair[0]]) + int(TC[pair[1]])
        base_mixed = int(MC[pair[0]]) + int(MC[pair[1]])
        for option in c734.SEC2[pair]:
            if set(option) == set(pair):
                continue
            two_piece_facet[
                (
                    int(TC[list(option)].sum()) - base_tick,
                    int(MC[list(option)].sum()) - base_mixed,
                )
            ] += 1
    two_piece_facet_deltas = tuple(sorted(two_piece_facet.items()))
    two_piece_cost_deltas = tuple(sorted(c734.DL))
    two_piece_cost_raising = bool(
        two_piece_cost_deltas and min(k for k, _v in two_piece_cost_deltas) > 0
    )
    boundary_vectors = [
        delta for delta, _count in two_piece_facet_deltas if delta != (0, 0)
    ]
    span_index = 0
    unimodular_pair = ()
    for left, right in itertools.combinations(boundary_vectors, 2):
        minor = left[0] * right[1] - left[1] * right[0]
        span_index = gcd(span_index, abs(minor))
        if abs(minor) == 1 and not unimodular_pair:
            unimodular_pair = (left, right)
    two_piece_span = (span_index, unimodular_pair, len(boundary_vectors))
    conserved_functionals = tuple(
        functional
        for functional, values in (
            ((1, 0), tick_sums), ((0, 1), mixed_sums)
        )
        if len({int(value) for value in values}) == 1
    )

    integer_arrays = (
        cost_sums, tick_sums, mixed_sums, box_sums, per_facet, histogram,
        indicator, packed, facet_cost, C4, TC, MC, BX, c734.IV, c734.MM,
        c726.SCOST, edges4,
    )
    exact_no_float = bool(
        all(np.issubdtype(array.dtype, np.integer) for array in integer_arrays)
        and Fraction(COST_CLASS, CUTTING_SIZE) == Fraction(PIECE_COST_FLOOR, 1)
        and all(
            isinstance(value, int)
            for value in (distance_total, attempts, forward, back, span_index)
        )
        and not any(
            isinstance(value, float)
            for value, _count in achieved_deltas + two_piece_facet_deltas
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        machinery=machinery_shape,
        machinery_exit=machinery_exit,
        c767_pin=c767_pin,
        corner_orders_agree=corner_orders_agree,
        piece_lists_agree=piece_lists_agree,
        volume_spectrum=volume_spectrum,
        cost_spectrum=cost_spectrum,
        exact_inverses_agree=exact_inverses_agree,
        corpus=(len(SOL), CORPUS),
        search_nodes=int(c734.NODE[0]),
        cutting_sizes=tuple(sorted({len(cutting) for cutting in SOL})),
        pool_pieces=len(USED),
        pool_orbits=len({int(c734.LAB[piece]) for piece in USED}),
        cost_sums=tuple(sorted({int(value) for value in cost_sums})),
        floor_forcing=floor_forcing,
        floor_types=floor_types,
        pool_types=pool_types,
        type_solutions=type_solutions,
        balance_law=tuple(sorted(balance)),
        per_cutting_types=per_cutting_types,
        cooccurring_pairs=cooccurring_pairs,
        independent_corpus=independent_corpus,
        charge_points=charge_points,
        charge_multiplicity=int(charge_counter.get(CORPUS_CHARGE, 0)),
        facet_split_reconstructs=facet_split_reconstructs,
        tick_facet_totals=tick_facet_totals,
        mixed_facet_totals=mixed_facet_totals,
        box_charge=tuple(sorted({int(value) for value in box_sums})),
        committed_tick_spectrum=committed_tick_spectrum,
        committed_mixed_spectrum=committed_mixed_spectrum,
        own_three_cube=own_three_cube,
        facet_bracket=facet_bracket,
        charge_is_floor_times_ceiling=charge_is_floor_times_ceiling,
        witness_rows=witness_rows,
        witness_costs=witness_costs,
        witnesses_in_corpus=witnesses_in_corpus,
        bridge_point_hits=bridge_point_hits,
        bridge_points_are_cycle726=bridge_points_are_cycle726,
        distance_support=distance_support,
        distance_total=distance_total,
        d4_pairs=d4_pairs,
        disjoint_pairs=disjoint_pairs,
        regions=regions,
        region_families=region_families,
        region_refills=region_refills,
        refill_geometry=refill_geometry,
        deep_separation=deep_separation,
        flip_attempts=flip_attempts,
        directed_flips=directed_flips,
        involution=involution,
        same_cost_class=same_cost_class,
        images_in_corpus=attempts == len(flip_rows),
        achieved_deltas=achieved_deltas,
        deltas_by_family=deltas_by_family,
        flip_lattice_rank=flip_lattice_rank,
        flip_lattice=achieved_set,
        bridge_lattice=bridge_lattice,
        generators_from_witnesses=generators_from_witnesses,
        generators_unrealised=generators_unrealised,
        proper_sublattice=proper_sublattice,
        ladder=tuple(ladder),
        ladder_charge_neutral=ladder_charge_neutral,
        components_k4=ladder[0],
        reversibility_premise=reversibility_premise,
        kill_reason=kill_reason,
        two_piece_pairs=len(c734.FLIP),
        two_piece_cost_deltas=two_piece_cost_deltas,
        two_piece_cost_raising=two_piece_cost_raising,
        two_piece_geometric=int(c734.GEO2),
        two_piece_facet_deltas=two_piece_facet_deltas,
        two_piece_span=two_piece_span,
        conserved_functionals=conserved_functionals,
        corrections=CORRECTION_IDS,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: GATE 0, THE POPULATION QUESTION, DECIDED, and its MECHANISM: the cost-144 four-cube cutting corpus carries the CONSTANT facet charge (TC, MC) = (36, 60) on ALL 15,800 members (hence FC = 96 and BX = 108 on every one), so the bridge\'s three points (36,55), (41,48), (37,48) are attained by ZERO cuttings and their cycle-726 witnesses W5, W6, W1 -- at C4 = 159, 169, 165, ALL ABOVE THE FLOOR 144 -- lie OUTSIDE THE CORPUS ENTIRELY, while W2, the one cycle-726 witness INSIDE, sits at EXACTLY (36,60) and is the one the bridge did not use; the constancy is FORCED, not incidental, by a chain each step of which is certified: cost 144 = 24 x 6 forces an ALL-COST-6 cutting with no slack anywhere; the 192 USED pieces carry ONLY TWO charge types, (0,3) x96 and (3,2) x96, although types (3,3) and (3,4) EXIST among the 400 cost-6 pieces, so the exclusion is NON-TRIVIAL and not definitional; every cutting takes exactly 12 pieces with TC = 3, 12 with MC = 3 and 12 with BX = 5; each of the EIGHT facets takes EXACTLY SIX pieces, every TICK facet sitting at 18 and every MIXED facet at 10, giving 2 x 18 = 36 and 6 x 10 = 60 by a SECOND, independent route; and the INDEPENDENT 3-CUBE ENUMERATION of the 180 minimal facet dissections, whose tick spectrum has MINIMUM 18 and whose mixed spectrum has MAXIMUM 10, proves 18 the EXACT TICK FLOOR and 10 the EXACT MIXED CEILING, so the C4 floor class is EXACTLY the class that minimizes every tick facet and maximizes every mixed facet SIMULTANEOUSLY -- which is why nothing inside the class can move the charge\nper_site: THE DEFINITIONS AND THE ROW FORMAT, stated exactly because the bridge left two terms undefined: COST CLASS := the level set of the cycle-734 four-column charge C4 summed over the 24 pieces, under which the 46,128 four-piece flips are ONE class and the 288 two-piece re-cuts are OUTSIDE it (this resolves the bridge\'s undefined "interior-cost class" by DECLARATION, making field 7 of the work order total rather than vacuous); FLIP := the cycle-734 four-piece region swap between a region\'s two local-cost-24 refills, explicitly NOT the cycle-745/747 binary target vectors named "four"/"four-flip" and NOT cycle-769\'s coordinate sign flips in the order-384 group; and the SEVEN FIELDS the work order specified are populated per row -- flip identifier (region key, direction, host), support type (the region\'s carried family among the five sizes 12, 12, 24, 24, 48 with its eight-corner support), pre-flip (TC, MC) RECOMPUTED on the endpoint cutting, post-flip (TC, MC) recomputed likewise, achieved delta, reverse identifier as the NAMED INVOLUTION PARTNER, and the same-cost-class flag TESTED rather than assumed -- with both aggregation requirements met, deltas grouped by support type and multiplicity and reversibility tested AT THE FLIP LEVEL, so that a -v arising from an unrelated support or a different class does not count\nper_mode: THE COMPLETE ENUMERATION, on two routes: the corpus of 15,800 cuttings on 192 pieces, each piece in 1,975 cuttings and the 192 forming four complete orbits of the carried order-48 action, is produced by a COMPLETE exact-cover search with all 15,168 co-occurring pairs separated by EXHIBITED INTEGER PLANES rather than sample-grid coincidence, and is REBUILT BY A DIFFERENT SEARCH STRATEGY with the cycle-734 node count 502,838 REPLICATED EXACTLY under its own point construction -- agreement on the interior node count, not merely on the leaf count; the pair-distance census runs over ALL 124,812,100 pairs and finds NO pair at distance 1, 2, 3 or 5 and EXACTLY 46,128 at distance 4, so the four-piece move is MINIMAL in the class and the edge set is COMPLETE rather than a chosen subfamily; the 120 eight-corner regions fall into FIVE carried families of sizes 12, 12, 24, 24, 48, each exposing 8 or 32 candidate pieces with 2 or 24 refills, local cost floor 24 and EXACTLY TWO floor refills, and EVERY incidence-compatible refill is certified a GENUINE EXACT RE-CUT by full tiling verification before it is promoted to a move; the walk then enumerates 92,256 DIRECTED FLIPS with every image IN-CORPUS, every flip an INVOLUTION whose swap-back restores the original, and every flip SAME-COST-CLASS at C4 = 144 on both endpoints, the 46,128 unordered edges matching the d = 4 census exactly; the checker RE-WALKED THE COMPLETE 48-REGION FAMILY from scratch -- 45,888 directed flips -- with FULL TILING RE-VERIFICATION; and the k = 4 flip graph has 349 components, the head of the cumulative ladder [349, 349, 157, 61, 61, 13, 1] for k = 4..10, EVERY component carrying the single charge orbit {(36,60)}\nper_block: THE VERDICT AGAINST THE BRIDGE CONDITIONAL: the achieved delta set is {(0,0)} with multiplicity 92,256 -- EVERY FLIP IS CHARGE-NEUTRAL -- identical across all five support families and all 349 components, and the bridge\'s generators (5,-7) and (1,-7) are realized by ZERO flips in EITHER direction; hence L_flip = Z-span(D) = {(0,0)} has RANK 0, the achieved cone is {0} and pointed only vacuously with no positive direction at all, and the rational nullspace {(a,b) : a dTC + b dMC = 0 for all achieved deltas} is Q^2 of DIMENSION 2; against the bridge\'s L = {7x + y = 0 mod 28} of index 28 -- RE-DERIVED INDEPENDENTLY by the checker as the GCD 28 OF THE 2x2 MINORS -- L_flip is a PROPER RANK-0 SUBLATTICE, the comparison named exactly as containment proper BY RANK rather than equality, disjointness or incomparability; the constancy closes the k = 6..10 LADDER ESCAPE, since every rung is charge-neutral on a population whose charge is constant; and THE KILL IS SHARPENED: the flips ARE same-cost-class and ARE reversible, so the conditional\'s REVERSIBILITY PREMISE IS MET, and the momentum-like reading dies on RANK -- a rank-0 increment set is not sign-indefinite, it has no signs at all -- rather than on irreversibility, which is a CLEANER KILL THAN THE BRIDGE ANTICIPATED, since a kill by irreversibility would leave the increments intact for a later reversible route while a kill by rank removes the increments themselves; SECTION 8 BRANCH 2 therefore obtains IN ITS STRONGEST FORM, branch 3 collapsing onto it because the reversible sublattice is {0} and branch 4 firing only past the declared class, so THE CONDITIONAL BRIDGE IS NOT ACTIVATED ON ANY READING while THE BLOCK 130 ARITHMETIC SURVIVES UNTOUCHED AS ARITHMETIC\nlattice_wide: THE INVERSION, THE BOUNDARY, THE CORRECTIONS, AND THE DOWNSTREAM CLOSURE: TC = 36 and MC = 60 are SEPARATELY CONSERVED on the corpus -- a GENUINE CONSERVATION LAW, exactly OPPOSITE to the bridge\'s Section 5 non-conservation reading, which the enumeration shows was NARROW TO THREE EXTREMAL WITNESSES OUTSIDE THIS POPULATION at C4 = 159, 169, 165, so the failure was one of SAMPLING and not of arithmetic, the parent\'s determinant -28 remaining exactly true of its three points; the 288 TWO-PIECE re-cuts, all genuine, are STRICTLY COST-RAISING with C4 deltas +1 x192 and +2 x96 -- a DIRECTED, NON-REVERSIBLE class that never returns to the floor -- with facet deltas {(0,-1), (0,0), (1,-1), (1,0)} at multiplicities 48/144/48/48 generating Z^2 at INDEX 1 rather than L\'s 28, and the branch-4 rerun on that expanded record giving four points of AFFINE RANK 2 with a pointed cone in the quadrant x >= 0, y <= 0, STILL cost-raising and STILL non-reversible; the NINE BRIDGE CORRECTIONS are carried as NAMED FINDINGS and not silent edits -- the three points are cycle-726 witnesses W5, W6, W1 with values right and attribution wrong; the ((1,192),(2,96)) histogram is the C4 COST-INCREASE SPECTRUM of the directed two-piece class, not an "interior-cost move histogram" and not a facet-charge quantity; Delta1 and Delta2 are WITNESS-TO-WITNESS DIFFERENCES, NEVER FLIPS, realized by zero of the 92,256 rows; the witness/corpus population gap is DECIDED by Gate 0; "interior-cost class" and "flip" are RESOLVED BY DECLARATION; the "frame covering" has NO COMMITTED SOURCE and its order-four reading is ARITHMETICALLY IMPOSSIBLE, a (2,2,2,2) cycle type having order 2, as checked on the eight facets where the six elements of that type all have order two; and the pinned cycle-767 authority is a VALID REACHABLE CONTENT-BOUND PIN, its commit an ancestor of origin/main with both objects resolving, the path rename on main being exactly why BLOB PINS ARE THE CORRECT CITATION FORM; whence DOWNSTREAM THE FLIP ROUTE IS CLOSED -- the cell-cutting flip move set supplies NO sign-indefinite facet-charge increments and cannot furnish the momentum-like inputs the Block 123 definiteness comparison targets -- while BLOCK 123\'s OWN THEOREM IS UNTOUCHED, the 40,512 three-piece incidence candidates at local costs 19/20/21 are NOT PROMOTED and NOT DECIDED, no non-naive frame-to-momentum map is excluded, the paired-degeneracy question is not tested, the cycle-725/726/734 supplied-model firewall is INHERITED UNCHANGED, and the other lane\'s unmerged cycle-778-799 material -- six notes, last touched 2026-08-15 -- is NOT READ, NOT CONSUMED and NOT SUPERSEDED\nRESULT: on the committed cost-144 four-cube cutting corpus, the cycle-734 four-piece flip class on it, and the cycle-726 facet charge at the displayed fixtures, executing the Block 130 bridge\'s Section 8 flip-enumeration work order OURSELVES from origin/main\'s committed machinery only, GATE 0 gives the CONSTANT facet charge (TC, MC) = (36, 60) on ALL 15,800 members -- forced by 144 = 24 x 6 through an all-cost-6 cutting, the two used piece types (0,3) x96 and (3,2) x96 against the EXISTING but EXCLUDED types (3,3) and (3,4), the 12/12/12 balance, six pieces per facet, and the INDEPENDENTLY PROVED tick floor 18 and mixed ceiling 10 from the 180 minimal 3-cube facet dissections -- so the bridge points (36,55), (41,48), (37,48) are attained by ZERO cuttings and W5, W6, W1 at C4 = 159, 169, 165 lie OUTSIDE, W2 being the unique cycle-726 witness inside at exactly (36,60); the ENUMERATION is COMPLETE on both routes, 15,800 cuttings rebuilt by two different search strategies with the node count 502,838 REPLICATED EXACTLY, 15,168 co-occurring pairs separated by exhibited integer planes, a pair-distance census over ALL 124,812,100 pairs with d = 4 EXACTLY 46,128 and NO d in {1, 2, 3, 5}, and 92,256 DIRECTED FLIPS over 120 regions in five support families, all images in-corpus, involutive and same-cost-class, the checker re-walking the COMPLETE 48-REGION FAMILY (45,888 directed flips) with FULL TILING RE-VERIFICATION; the VERDICT is that the achieved delta set is {(0,0)} at multiplicity 92,256, EVERY FLIP CHARGE-NEUTRAL, so L_flip = {(0,0)} is a PROPER RANK-0 SUBLATTICE of L = {7x + y = 0 mod 28} (re-derived independently as the gcd 28 of the 2x2 minors), with cone {0} and nullspace Q^2, the constancy closing the k = 6..10 ladder escape on [349, 349, 157, 61, 61, 13, 1]; THE KILL IS SHARPENED -- the reversibility premise is MET and the momentum-like reading dies on RANK, a CLEANER KILL than the bridge anticipated -- so SECTION 8 BRANCH 2 obtains IN ITS STRONGEST FORM, branch 3 collapsing onto it and branch 4 firing only past the class, THE CONDITIONAL BRIDGE IS NOT ACTIVATED ON ANY READING and the Block 130 arithmetic survives as arithmetic; TC and MC are SEPARATELY CONSERVED on the corpus, inverting the bridge\'s Section 5 reading, which was narrow to three extremal witnesses outside this population; the 288 two-piece re-cuts are STRICTLY COST-RAISING (+1 x192, +2 x96) with facet deltas {(0,-1), (0,0), (1,-1), (1,0)} at 48/144/48/48 generating Z^2 at INDEX 1; all NINE bridge corrections are carried as named findings, the cycle-767 pin being VALID; and DOWNSTREAM THE FLIP ROUTE IS CLOSED, Block 123\'s own theorem untouched\nDECISION_CUT: PROMOTE OR REFUTE THE THREE-PIECE INCIDENCE CANDIDATES -- 40,512 at local costs 19/20/21, never promoted to geometric re-cuts here and the only remaining declared class that could supply same-class increments; BUILD OR EXCLUDE A NON-NAIVE FRAME-TO-MOMENTUM MAP, since the echo exclusion is strengthened at the naive level only and a separately constructed quotient, many-to-one map or nonconjugate intertwiner is still open; BUILD THE ENTROPY/COUNTING-FUNCTIONAL ROUTE CANDIDATE, named here precisely because the flip route is now closed and a constant-charge population with a complete move class is the natural place for a counting rather than a charge functional -- this block does NOT predict whether it works; TEST THE PAIRED-DEGENERACY OBSERVABLE QUESTION in the Block 129 live transfer sector and DERIVE THE COMMON NILPOTENT DIFFERENTIAL or its exact connection residual, the bridge\'s two remaining items; and LEAVE THE OTHER LANE\'S UNMERGED CYCLE-778-799 MATERIAL to that worker -- their pending state, not read, not consumed, not superseded; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "gate0_constant",
    "gate0_outside",
    "mechanism_floor_ceiling",
    "mechanism_two_types",
    "enumeration_count",
    "enumeration_involution",
    "verdict_neutral",
    "verdict_branch",
    "verdict_kill",
    "inversion",
    "two_piece_boundary",
    "corrections",
    "downstream_closure",
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
        "gate0_constant": "constant" in note
        and ("(36, 60)" in note or ("36" in note and "60" in note)),
        "gate0_outside": "outside the corpus" in note
        or "none is a cost-144" in note,
        "mechanism_floor_ceiling": "floor" in note and "ceiling" in note,
        "mechanism_two_types": "two charge types" in note
        or "two piece types" in note
        or ("(3, 3)" in note and "exclu" in note),
        # Whitespace- and comma-insensitive so the note may write either form.
        "enumeration_count": "92,256" in note
        or "46,128" in note
        or "92256" in compact
        or "46128" in compact,
        "enumeration_involution": "involut" in note,
        "verdict_neutral": "charge-neutral" in note or "{(0,0)}" in compact,
        "verdict_branch": "branch 2" in note,
        "verdict_kill": "dies on rank" in note or "sharpened" in note,
        "inversion": "separately conserved" in note
        or "conservation law" in note,
        "two_piece_boundary": "cost-raising" in note or "index 1" in note,
        "corrections": ("nine" in note or "corrections" in note)
        and ("content-bound pin" in note or "reachable" in note),
        "downstream_closure": "closed" in note
        and ("block 123" in note or "momentum" in note),
        "pickup_provenance": "pickup" in note
        or "owner directed" in note
        or "silent" in note,
        "not_consumed_rider": "778" in note
        or "not consumed" in note
        or "pending state" in note,
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
        "corpus_count": CORPUS,
        "pool_types": POOL_PIECE_TYPES,
        "charge_point_count": 1,
        "tick_floor": TICK_FLOOR,
        "witnesses_in_corpus": WITNESSES_IN_CORPUS,
        "witness_costs": WITNESS_COST,
        "directed_flips": DIRECTED_FLIPS,
        "achieved_deltas": ACHIEVED_DELTAS,
        "flip_lattice_rank": FLIP_LATTICE_RANK,
        "kill_reason": KILL_REASON,
        "two_piece_cost_raising": True,
        "conserved_functionals": CONSERVED_FUNCTIONALS,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "wrong_corpus_count":
        claims["corpus_count"] = CORPUS - 1
    elif mutation == "break_two_type_law":
        claims["pool_types"] = (((0, 3), 96), ((3, 3), 96))
    elif mutation == "claim_charge_not_constant":
        claims["charge_point_count"] = 2
    elif mutation == "wrong_tick_floor":
        claims["tick_floor"] = TICK_FLOOR - 1
    elif mutation == "claim_witness_inside_corpus":
        claims["witnesses_in_corpus"] = ("W2", "W5")
    elif mutation == "wrong_witness_cost_total":
        claims["witness_costs"] = tuple(
            (name, COST_CLASS if name == "W5" else cost)
            for name, cost in WITNESS_COST
        )
    elif mutation == "wrong_flip_count":
        claims["directed_flips"] = DIRECTED_FLIPS - 2
    elif mutation == "claim_nonzero_flip_delta":
        claims["achieved_deltas"] = ((0, 0), (1, -1))
    elif mutation == "claim_flip_lattice_is_L":
        claims["flip_lattice_rank"] = 2
    elif mutation == "claim_kill_is_irreversibility":
        claims["kill_reason"] = "irreversibility"
    elif mutation == "claim_two_piece_reversible":
        claims["two_piece_cost_raising"] = False
    elif mutation == "claim_charge_not_conserved":
        claims["conserved_functionals"] = ()
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
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_LANE_FLIP_ENUMERATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            # the three origin/main-only cell-cutting runners are
            # content-bound via the gate-A blob pins, not audit paths
        )
        and PARENT_ARTIFACTS == (BLOCK149_NOTE, BLOCK149_RUNNER, BRIDGE_NOTE)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # the three cell-cutting runners, bound BY CONTENT and by shape
        and authority.machinery_content_bound
        and tuple(name for name, _recorded, _digest, _pin in authority.machinery_blobs)
        == ("c726", "c734", "c811")
        and facts.machinery == MACHINERY_SHAPE
        and facts.machinery_exit
        == (0, C726_GATES, 0, (C734_PREFIX_GATES, 0))
        # M7: the bridge note's cycle-767 pin is reachable history
        and facts.c767_pin == (True, True, True, True)
    )

    gate_b = bool(
        facts.corner_orders_agree
        and facts.piece_lists_agree
        and facts.volume_spectrum == VOLUME_SPECTRUM
        and sum(count for _volume, count in facts.volume_spectrum)
        == PIECE_CANDIDATES
        and facts.cost_spectrum == COST_SPECTRUM
        and sum(count for _cost, count in facts.cost_spectrum) == PIECES
        and facts.exact_inverses_agree
        and facts.corpus == (claims["corpus_count"], CORPUS)
        and facts.search_nodes == SEARCH_NODES
        and facts.cutting_sizes == (CUTTING_SIZE,)
        and facts.pool_pieces == POOL_PIECES
        and facts.pool_orbits == POOL_ORBITS
        and facts.cost_sums == (COST_CLASS,)
        and facts.floor_forcing
        and facts.floor_types == FLOOR_PIECE_TYPES
        and facts.pool_types == tuple(claims["pool_types"])
        and facts.type_solutions == (TYPE_SOLUTION,)
        # the exclusion, stated as such: neither excluded type survives
        and all(
            excluded not in tuple(pair for pair, _count in facts.pool_types)
            for excluded in EXCLUDED_TYPES
        )
        and all(
            excluded in tuple(pair for pair, _count in facts.floor_types)
            for excluded in EXCLUDED_TYPES
        )
        and facts.balance_law == (BALANCE_LAW,)
        and facts.per_cutting_types == PER_CUTTING_TYPES
        and facts.cooccurring_pairs == (COOCCURRING_PAIRS, COOCCURRING_PAIRS)
        and facts.independent_corpus
        == (CORPUS, PIECE_COST_FLOOR, FLOOR_PIECES, True, True)
    )

    gate_c = bool(
        facts.charge_points == ((CORPUS_CHARGE, CORPUS),)
        and len(facts.charge_points) == claims["charge_point_count"]
        and facts.charge_multiplicity == CORPUS
        and facts.facet_split_reconstructs
        and facts.tick_facet_totals == (claims["tick_floor"],)
        and facts.mixed_facet_totals == (MIXED_CEILING,)
        and facts.box_charge == (CORPUS_BOX_CHARGE,)
        and facts.committed_tick_spectrum == (TICK_SPECTRUM,) * TICK_FACETS
        and facts.committed_mixed_spectrum == (MIXED_SPECTRUM,) * MIXED_FACETS
        and facts.own_three_cube
        == (
            FACET_DISSECTIONS,
            (FACET_TETS,),
            TICK_SPECTRUM,
            MIXED_SPECTRUM,
            0,
        )
        and facts.facet_bracket
        == (
            TICK_FACETS * TICK_FLOOR + MIXED_FACETS * MIXED_FLOOR,
            TICK_FACETS * TICK_CEILING + MIXED_FACETS * MIXED_CEILING,
        )
        and facts.charge_is_floor_times_ceiling
        and CORPUS_CHARGE[0] + CORPUS_CHARGE[1] == CORPUS_FACET_TOTAL
    )

    gate_d = bool(
        facts.witness_rows
        == tuple((name, WITNESS_ROWS[name]) for name in WITNESS_NAMES)
        and facts.witness_costs == tuple(claims["witness_costs"])
        and facts.witnesses_in_corpus == tuple(claims["witnesses_in_corpus"])
        and facts.bridge_point_hits
        == tuple((label, 0) for label, _point in BRIDGE_POINTS)
        and facts.bridge_points_are_cycle726
        # the three bridge witnesses are outside the class, by cost
        and all(
            cost != COST_CLASS
            for name, cost in WITNESS_COST
            if name in ("W1", "W5", "W6")
        )
    )

    gate_e = bool(
        facts.distance_support == DISTANCE_SUPPORT
        and all(
            value not in facts.distance_support for value in ABSENT_DISTANCES
        )
        and facts.distance_total == TOTAL_PAIRS
        and facts.d4_pairs == (D4_PAIRS, D4_PAIRS)
        and facts.disjoint_pairs == DISJOINT_PAIRS
        and facts.regions
        == (REGIONS, REGIONS, D4_PAIRS, True, (REGION_CORNERS,))
        and facts.region_families == (SUPPORT_FAMILIES, FAMILY_SIZES)
        and facts.region_refills
        == (
            REGION_CANDIDATES,
            REGION_REFILLS,
            (REGION_LOCAL_FLOOR,),
            (FLOOR_REFILLS_PER_REGION,),
        )
        and facts.refill_geometry == (REGIONS, REFILL_TOTAL, REFILL_TOTAL)
        and facts.deep_separation
        in ((0, 0), (COOCCURRING_PAIRS, COOCCURRING_PAIRS))
        and facts.flip_attempts == (DIRECTED_FLIPS, DIRECTED_FLIPS)
        and facts.directed_flips == (claims["directed_flips"], DIRECTED_FLIPS)
        and facts.involution == (D4_PAIRS, D4_PAIRS, D4_PAIRS)
        and facts.same_cost_class
        and facts.images_in_corpus
        and tuple(delta for delta, _count in facts.achieved_deltas)
        == tuple(claims["achieved_deltas"])
        and facts.achieved_deltas == (((0, 0), DIRECTED_FLIPS),)
        and len(facts.deltas_by_family) == SUPPORT_FAMILIES
        and all(
            tuple(delta for delta, _count in counter) == ACHIEVED_DELTAS
            for _family, counter in facts.deltas_by_family
        )
    )

    gate_f = bool(
        facts.flip_lattice == ACHIEVED_DELTAS
        and facts.flip_lattice_rank == claims["flip_lattice_rank"]
        and facts.generators_from_witnesses == BRIDGE_DELTAS
        and facts.bridge_lattice == (BRIDGE_INDEX, 1, True)
        and facts.generators_unrealised
        == tuple((generator, 0) for generator in BRIDGE_DELTAS)
        and facts.proper_sublattice
        and facts.ladder == LADDER
        and facts.ladder_charge_neutral
        and facts.components_k4 == COMPONENTS_K4
        and facts.reversibility_premise
        and facts.kill_reason == claims["kill_reason"]
    )

    span_index, unimodular_pair, boundary_count = facts.two_piece_span
    gate_g = bool(
        facts.two_piece_pairs == TWO_PIECE_PAIRS
        and facts.two_piece_cost_deltas == TWO_PIECE_COST_DELTAS
        and sum(count for _delta, count in facts.two_piece_cost_deltas)
        == TWO_PIECE_PAIRS
        and facts.two_piece_cost_raising == bool(claims["two_piece_cost_raising"])
        and facts.two_piece_geometric == TWO_PIECE_PAIRS
        and facts.two_piece_facet_deltas == TWO_PIECE_FACET_DELTAS
        and span_index == TWO_PIECE_SPAN_INDEX
        and len(unimodular_pair) == 2
        and abs(
            unimodular_pair[0][0] * unimodular_pair[1][1]
            - unimodular_pair[0][1] * unimodular_pair[1][0]
        )
        == 1
        and boundary_count == 3
        and facts.conserved_functionals == tuple(claims["conserved_functionals"])
        and facts.corrections == CORRECTION_IDS
        and len(CORRECTION_IDS) == CORRECTIONS
        and len(CORRECTION_TITLES) == CORRECTIONS
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
            "also re-derive, cache-free and from scratch, the separating "
            "integer plane of every one of the 15,168 co-occurring piece pairs"
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
        "main plus the committed Block 149 note/runner and the Block 130 bridge note are content-bound, and the three cell-cutting runners this block reasons with are read from origin/main AT RUN TIME under blob pins that are checked against the hash of the bytes actually imported, with their pinned cut markers and their own gate tallies (cycle 726: 32/0 and exit 0; cycle 734 prefix: 21/0) recorded, and the bridge note's cycle-767 pin re-checked as reachable history whose path is merely absent from the main tip",
        gate_values["A"],
    )
    checks.check(
        "B-corpus",
        "the corpus is the complete 15,800 cost-144 cuttings found by the committed cycle-734 exact-cover search in 502,838 nodes over 400 floor pieces, using 192 of them in four whole orbits, INDEPENDENTLY reproduced cutting-for-cutting by the committed 2026-08-11 orbit-floor runner on a different sample lattice; cost 144 = 24 x 6 FORCES every piece to the floor; the 192 pool pieces carry exactly two (TC,MC) types, (0,3) x 96 and (3,2) x 96, with the (3,3) and (3,4) floor types EXCLUDED by an exhaustive nonnegative-solution certificate rather than by census, and every cutting takes 12 of each type; all 15,168 co-occurring pairs are separated by exhibited integer planes and the committed float piece-inverse is re-derived by exact adjugate and gated equal",
        gate_values["B"],
    )
    checks.check(
        "C-constant-charge",
        "on all 15,800 cuttings the cycle-726 facet charge is the single point (TC, MC) = (36, 60), with box charge 108; the per-facet split re-derived here reconstructs the committed per-piece charges and puts BOTH tick facets at 18 and ALL SIX mixed facets at 10; the induced three-cube facet problem is re-enumerated in this runner (180 dissections, six tetrahedra each, zero boundary incidences) and gives tick spectrum {18,19,20,21} and mixed spectrum {8,9,10}, so 36 = 2 x 18 is the tick FLOOR and 60 = 6 x 10 the mixed CEILING within the facet-wise bracket [84, 102] -- the charge is locked between a floor and a ceiling, not merely observed constant",
        gate_values["C"],
    )
    checks.check(
        "D-gate-zero",
        "the six committed cycle-726 witness rows are reproduced exactly and the three Block 130 bridge points are identified as W5, W6 and W1; W1, W5 and W6 have four-column cost 165, 159 and 169, so NONE is a cost-144 cutting, and the only witness inside the corpus is W2 at the corpus charge (36,60), which the bridge did not use; each of the three bridge points is attained by 0 of the 15,800 cuttings, so the population intersection is EMPTY twice over -- by class membership and by charge value",
        gate_values["D"],
    )
    checks.check(
        "E-flip-enumeration",
        "the complete census of all 124,812,100 pairs gives distances 4 and 6..24 and never 1, 2, 3 or 5, with 46,128 pairs at distance four and 29,069,284 disjoint; those pairs re-cut exactly 120 eight-corner regions in five support families (12, 12, 24, 24, 48) with 8 or 32 candidates, 2 or 24 incidence refills, local floor 24 and exactly two floor refills each, all 2,352 incidence refills over all 120 regions checked genuine geometric re-cuts; the resulting 92,256 directed flips are involutive with every reverse partner enumerated, stay inside the cost class, land in the corpus (92,256 attempts, 92,256 landings) and achieve the increment (0,0) every time, in every support family",
        gate_values["E"],
    )
    checks.check(
        "F-verdict-structure",
        "the achieved lattice L_flip = {(0,0)} has rank 0 and is a PROPER sublattice of the bridge lattice L = {7x + y = 0 mod 28}, whose modulus is re-derived here from the witness differences (5,-7) and (1,-7) as the gcd of the 2x2 minors, 28, with the congruence description verified over a full period box; both bridge generators are realised by ZERO flips in either direction; the ladder [349, 349, 157, 61, 61, 13, 1] over k = 4..10 is charge-neutral at every rung; and the kill is SHARPENED: the reversibility premise is MET (every flip an involution, every reverse enumerated, every image same-class), so the conditional dies on RANK and not on irreversibility",
        gate_values["F"],
    )
    checks.check(
        "G-boundary-and-inversion",
        "the 288 two-piece re-cuts are genuine geometric re-cuts, 288 of 288, and every one RAISES the cost (+1 on 192, +2 on 96), so the tier is strictly one-way and cannot witness the antecedent; its facet delta multiset (0,0) x 144, (1,0) x 48, (0,-1) x 48, (1,-1) x 48 spans Z^2 at index 1 with an exhibited unimodular pair, so the confinement is by COST CLASS and not by charge; on this population TC and MC are each separately conserved, inverting the bridge Section 5 finding; the nine carried corrections are recorded and the whole computation is float-free",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the constant-charge Gate 0 with its outside-the-corpus witnesses, the floor-meets-ceiling mechanism with its two-type exclusion, the complete involutive enumeration, the branch-2 verdict with its charge-neutral ladder and its sharpened rank kill, the Section 5 inversion, the cost-raising two-piece boundary, the nine corrections with the reachable cycle-767 pin, the downstream closure of the Block 123 route, the pickup provenance, the not-consumed rider, the cross-context disclosure, the firewalls and the exact N5 fence are present",
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
