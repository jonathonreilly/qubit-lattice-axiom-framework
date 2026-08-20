#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_floor_boundary_theorem_2026_08_20.py
"""Block 151: THE FLOOR-BOUNDARY THEOREM -- the three-piece class, promoted, and
the exact cost stratum at which the floor no-go stops.

Block 150 closed the FOUR-piece route on the committed cell-cutting lane: the
cost-144 corpus carries the CONSTANT facet charge (TC, MC) = (36, 60), so every
same-class move it admits is charge-neutral and the Block 130 bridge conditional
cannot be activated there.  Its own rider named the one surviving class -- the
cycle-734 THREE-PIECE INCIDENCE CANDIDATES, which cycle 734 had left UNPROMOTED
to geometric re-cuts -- and left the question: do the three-piece moves supply
the SIGN-INDEFINITE facet-charge increments the flips could not?  This runner
answers it, and the answer has a sharp boundary:

  * THE NAMED CLASS IS SMALLER THAN ITS NAME, AND THE CORRECTION IS EXACT.  The
    cycle-734 gate `three.none` finds 649,600 co-occurrence cliques, 13,568 of
    them spurious, 636,032 genuine triples, and 40,512 triples admitting a
    second three-piece refill; the REFILLS themselves number 42,240, at local
    four-column costs 19 (27,264), 20 (14,592) and 21 (384).  Of those 42,240,
    exactly 41,088 replace only TWO of the three pieces, and the removed pair is
    always one of cycle-734's 288 two-piece re-cuts with a SPECTATOR piece
    adjoined -- so 97 per cent of the "three-piece" class is the two-piece class
    Block 150 already measured.  The irreducibly three-piece part is 1,152
    refills, with dC4 in {2, 3} only, and every one of them sits on a MINIMUM
    seven-corner hull;
  * THE WHOLE CLASS IS PROMOTED.  Cycle 734 recorded these as INCIDENCE
    candidates and explicitly declined to call them geometric re-cuts.  Here
    every one of the 8,893,056 (triple, host, refill) instances is a genuine
    exact dissection: the entire local-cost-21 stratum -- 384 refills, 293,376
    instances -- is certified in the default gate path, deterministic samples
    cover the other two strata, and --deep certifies all 42,240.  Zero failures.
    Cycle 734's own stated boundary is retired;
  * BUT THE CLASS IS STRICTLY DIRECTED, AND FOR A STRUCTURAL REASON.  Its
    achieved facet increments are {(0,-1) x 7104, (0,0) x 21024, (1,-1) x 7008,
    (1,0) x 7104}: the cone is the POINTED quadrant dTC >= 0, dMC <= 0, and no
    negative is realised by any of the 42,240.  The reason is not combinatorial.
    The induced three-cube facet problem -- re-enumerated here by a POINT-FREE
    route, as six-cliques of the exact interior-disjointness graph on the 56
    unimodular cells -- has tick spectrum {18, 19, 20, 21} and mixed spectrum
    {8, 9, 10}, so every minimal dissection of the four-box has TC in [36, 42]
    and MC in [48, 60] facet-wise, and the cost-144 corpus sits at the extreme
    CORNER (36, 60) = (TC_min, MC_max).  Any move whose SOURCE is a floor
    cutting is therefore forced into that quadrant, and a quadrant meets its own
    negation in {(0,0)} alone: NO FLOOR-ANCHORED MOVE CLASS OF ANY SIZE CAN BE
    SIGN-INDEFINITE.  Block 150's (0,0) and this block's one-sided cone are two
    shadows of one corner.  This is the floor-boundary theorem;
  * AND THE NO-GO STOPS EXACTLY ONE COST UNIT UP.  The charge rigidity is a
    FLOOR fact, not a lane fact.  Cost 145 decomposes into 192 blocks of 1,266
    cuttings -- one non-floor piece each, 243,072 in all -- and the charge is
    CONSTANT on every block but takes THREE values across them: (36,59) x
    60,768, (36,60) x 121,536, (37,60) x 60,768.  It is a function of the
    non-floor piece's IDENTITY and NOT of its charge type: two blocks whose
    non-floor piece has the same (TC, MC) = (0, 2) carry different block
    charges, which is exhibited;
  * THE SIGN-INDEFINITE SET EXISTS THERE, AND IS EXHIBITED.  At 145 no move of
    distance 1 or 2 keeps the cost (all 2,672 piece point-masks are distinct;
    the two-piece alternates in the stratum have dC4 in {-1, 1, 2} and never 0),
    and no charge-neutral move is shorter than distance 4, so EVERY distance-3
    same-class move CHANGES the charge -- the exact inversion of the floor.  A
    COMPLETE sub-scan over twelve blocks, four at each charge point, realises
    +-(1,0) and +-(0,1) at distance three and +-(1,1) at distance four; the full
    scan (132,288 distance-3 moves, 66,144 in each of the four directions) is
    carried as a twice-verified constant and re-run under --deep.  The achieved
    set {+-(1,0), +-(0,1), +-(1,1)} is negation-closed, its cone is R^2, and its
    lattice is Z^2 at index 1 -- STRICTLY CONTAINING the bridge lattice L, whose
    index is 28;
  * THE BOUNDARY IS NAMED EXACTLY, AND THE BRIDGE VECTORS ARE STILL NOT
    ACHIEVED.  The cost-145 charge range is three points, so the achieved
    DIFFERENCE set there is exactly {0, +-(1,0), +-(0,1), +-(1,1)} and |dTC|,
    |dMC| <= 1: the Block 130 generators (5,-7) and (1,-7) lie in the generated
    lattice but NOT in the achieved set.  Their NEGATIVES are excluded from any
    floor-anchored composite outright, since they would need charge (31, 67) and
    (35, 67), violating TC >= 36 and MC <= 60.  Composites of the class's own
    increments reach them at four-column cost 156 and 152 -- computed here as an
    exact integer minimum-cost program over the achieved increments -- but those
    are UPPER BOUNDS ONLY: neither minimality nor the chainability of the
    composite is proved, and the genuine dissections exhibited and re-certified
    here at (41, 53) and (37, 53) sit at cost 169 and 166.

The verdict is PARTIAL with the boundary named: the cost floor itself.  The
named class is a no-go; the no-go does not survive one cost unit up; and Block
123's definiteness comparison gets sign-indefinite, mutually reversible,
same-cost-class INPUTS for the first time in this lane -- but not the bridge's
own two vectors, and not at the floor.

Every scientific comparison below is exact integer or exact rational arithmetic;
no float is constructed anywhere in this runner and a float-freedom sweep is
gated; the integer monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: the cell-cutting machinery is NOT re-implemented here.  The
three committed runners are read at RUN TIME with `git show origin/main:<path>`,
their bytes are hashed and compared with the blob pins in gate A (so the pin is
CONTENT-BOUND and not merely a path), and the resulting source is written to a
temporary module and imported.  The cycle-726 runner is imported WHOLE, gates
and all; the cycle-734 and 2026-08-11 runners are imported up to a PINNED CUT
MARKER, itself an exact string match against their source.  This block's
cycle-734 cut is DEEPER than Block 150's: it now includes the committed
`three.none` section, so the class accounting this block reasons about is
produced by the COMMITTED RUNNER'S OWN PASSING GATE at run time (22 gates, zero
failures) and is then re-derived here by a different route.  Two honest
consequences are inherited: (i) the cycle-734 runner obtains its piece inverses
by float linear algebra and then certifies them by an EXACT integer identity, so
this runner re-derives the same inverses by EXACT ADJUGATE and gates the two
arrays equal, and no value used below comes from the float path; (ii) the
cycle-726 runner reads its cycle-725 dependency receipt by a CWD-relative path,
so the import is performed with the working directory set to the repository
root and its own exit status is captured and gated.

PROVENANCE DISCLOSURE: the four-box, the 2,672 minimal pieces, the cycle-726
facet charges (TC, MC, BX), the cycle-734 four-column cost C4, the cost floor 6,
the 15,800-cutting corpus, the exact-cover search, the separation certificate,
the region/refill machinery, the 288 two-piece re-cuts and the three-piece
incidence census are ALL COMMITTED objects, imported and never re-derived.
Block 150 supplies the constant-charge floor fact and the unpromoted-class
rider; the Block 130 bridge note supplies the two generators and the lattice L.
This block adds only the promotion, the corner theorem and its forcing
inference, the cost-145 stratum with its block law, the sign-indefinite move
set, and the boundary accounting.

INDEPENDENCE DISCLOSURE: the heavy constants below -- the 243,072-cutting
cost-145 census with its 69,888 separated co-occurring pairs, the 132,288
distance-3 same-class moves with 66,144 in each direction, and the 8,893,056
promotion instances -- were each measured TWICE, by the primary solve and by an
independent checker built from its own corner labelling, its own generic
rational sample lattice and its own search order, in a CROSS-CONTEXT setting.
The default gate path re-derives the census and the promotion count in full and
the move set on a complete sub-scan; --deep re-runs the full versions here.

PICKUP PROVENANCE: this block was picked up on owner direction after a silent
hand-off; the six named cycle-778..799 notes on unmerged branches are ANOTHER
worker's pending state and are NOT consumed, NOT read and NOT superseded here.

HYPOTHESES, named and not imported: (H1) COST CLASS means the level set of the
cycle-734 four-column pair charge C4 summed over a cutting; the floor class is
C4 = 144 and the stratum studied above it is C4 = 145.  This is Block 150's
declared resolution of the Block 130 phrase "interior-cost class", inherited
unchanged.  (H2) a k-PIECE MOVE is an unordered pair of cuttings differing in
exactly k pieces, equivalently a re-cut of the k-piece region they span; the
three-piece class is the cycle-734 incidence class of `three.none`.  (H3) an
ACHIEVED INCREMENT is the pair (dTC, dMC) between the endpoints of a move that
stays in the declared class; increments across classes are reported separately
and never mixed into the verdict.  (H4) the supplied-model firewall of cycles
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
    "ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK150_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_LANE_FLIP_ENUMERATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK150_RUNNER = (
    "scripts/admissibility_dirac_kahler_joint_lane_flip_enumeration_2026_08_20.py"
)
PARENT_ARTIFACTS = (
    BLOCK150_NOTE,
    BLOCK150_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path; the cache envelope stats these, so an origin/main-
# only path here would break the audit (the Block 130 lesson, re-learned at the
# Block 150 landing).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_LANE_FLIP_ENUMERATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_joint_lane_flip_enumeration_2026_08_20.py",
    # The three cell-cutting runners exist only on origin/main (our branch base
    # predates them); they are content-bound via the gate-A blob pins and read
    # at run time via `git show origin/main:` -- never worktree paths, so they
    # must not appear here.
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 150 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 150, so the parent branch is Block 150's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block150-joint-lane-flip-enumeration-20260820"
)
# Landing supervisor: replace this placeholder with the Block 150 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise; either way the binding is real and
# verifiable, and the immutable commit pin lands with the block.
PARENT_COMMIT = "a398c9a749e8364aed0d1c408cc049eec80e11d4"
# Block 149's tip: a real ancestor of HEAD that PREDATES both Block 150
# artifacts, so resolving the parent pin there leaves BOTH pinned blobs ABSENT.
# It is the honest stale control FOR THIS PIN SET.  This pin is read ONLY under
# the stale mutation; the baseline gate never requires the stale blobs to match.
STALE_PARENT_COMMIT = "0b8765449cb7bc11da4b427ad82cc1cc7d0ad854"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

# ---------------------------------------------------------------------------
# the committed cell-cutting machinery, pinned BY CONTENT and read at run time
# ---------------------------------------------------------------------------
# These runners live on origin/main and postdate this branch's base, so they
# cannot be imported from the worktree.  Each is fetched with `git show`, its
# bytes are hashed with git's own blob rule and compared against the pin, and
# the (optionally truncated) source is imported from a temporary module.  The
# CUT MARKER is an exact source line: everything before it is DEFINITION or a
# committed result this block reasons WITH, and everything after it is analysis
# this block performs itself.
C726_PATH = "scripts/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.py"
C726_BLOB = "46f080559c10d90d9803436f294ed660348b638f"
C726_CUT = ""                       # imported whole, gates and all
C734_PATH = (
    "scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.py"
)
C734_BLOB = "ef4cedb4045ad6c476041aab274985fb7efa40fe"
# DEEPER than Block 150's cut: the committed three-piece incidence census --
# the class this block promotes -- runs inside the imported prefix, so its
# accounting is the committed runner's own passing gate `three.none` and not a
# re-derivation.  The four-piece census that follows is Block 150's ground and
# is excluded (it is also the only float-typed array in the file).
C734_CUT = 'sec("the smallest move that keeps the cost changes four pieces")'
C811_PATH = "scripts/four_cube_cutting_fixed_point_orbit_floor_2026_08_11.py"
C811_BLOB = "65cade2f6c3dcd92e10fbd146cfd6a3f7f95b744"
C811_CUT = "USED = sorted(set(t for s in SOLS for t in s))"
MACHINERY = (
    ("c726", C726_PATH, C726_BLOB, C726_CUT),
    ("c734", C734_PATH, C734_BLOB, C734_CUT),
    ("c811", C811_PATH, C811_BLOB, C811_CUT),
)
C726_GATES = 32                     # the committed runner's own passing gates
C734_PREFIX_GATES = 22              # gates the imported prefix runs and passes
# (name, source lines, cut line): the cut line is the 0-based index of the
# pinned marker, so it is a THIRD binding on the imported source alongside the
# blob hash and the marker text itself.
MACHINERY_SHAPE = (
    ("c726", 661, 661),
    ("c734", 766, 507),
    ("c811", 1455, 239),
)

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "wrong_refill_count",
    "break_reduction_match",
    "wrong_three_cube_spectrum",
    "break_corner_inference",
    "claim_promotion_failure",
    "wrong_stratum_count",
    "claim_charge_type_dependence",
    "wrong_charge_points",
    "claim_neutral_distance_three",
    "wrong_achieved_set",
    "claim_bridge_vectors_achieved",
    "claim_reverses_exist",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "wrong_refill_count": "B",
    "break_reduction_match": "B",
    "wrong_three_cube_spectrum": "C",
    "break_corner_inference": "C",
    "claim_promotion_failure": "D",
    "wrong_stratum_count": "D",
    "claim_charge_type_dependence": "E",
    "wrong_charge_points": "E",
    "claim_neutral_distance_three": "F",
    "wrong_achieved_set": "F",
    "claim_bridge_vectors_achieved": "G",
    "claim_reverses_exist": "G",
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
    commit that predates both pinned artifacts.
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

    target = workdir / "scripts" / f"block151_{name}.py"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source, encoding="utf-8")

    spec = importlib.util.spec_from_file_location(f"block151_{name}", target)
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
PIECES = 2672
PIECE_COST_FLOOR = 6
FLOOR_PIECES = 400
CUTTING_SIZE = 24
FLOOR_CLASS = 144                        # 24 x 6
CORPUS = 15800
POOL_PIECES = 192
CORPUS_CHARGE = (36, 60)

# --- B: the class accounting, as the committed cycle-734 gate records it -----
CLIQUES = 649600
SPURIOUS = 13568
GENUINE_TRIPLES = 636032
KEEP_TRIPLES = 0                         # floor-preserving three-piece moves
RAISE_TRIPLES = 40512                    # TRIPLES admitting a second refill
ALTERNATES = 42240                       # the REFILLS themselves
LOCAL_FLOOR_3 = 18                       # 3 x 6
LOCAL_COST_SPECTRUM = ((19, 27264), (20, 14592), (21, 384))
# the reduction: 41,088 of the refills replace only TWO pieces, and the removed
# pair is always one of the committed 288 two-piece re-cuts
TWO_PIECE_PAIRS = 288
REDUCIBLE = 41088
REDUCIBLE_DC4 = ((1, 27264), (2, 13824))
REDUCIBLE_SHARED_CORNERS = 4
# the irreducible remainder, forced by the accounting and exhibited on hulls
IRREDUCIBLE = 1152
IRREDUCIBLE_DC4 = ((2, 768), (3, 384))
HULL_MIN_CORNERS = 7
HULL7_TRIPLES = 576
HULL7_ALTERNATES = 2304
REDUCTION_SAMPLE = 400
CLASS_DELTAS = (
    ((0, -1), 7104), ((0, 0), 21024), ((1, -1), 7008), ((1, 0), 7104)
)
CLASS_JOINT = (
    ((1, 0, -1), 6816), ((1, 0, 0), 13632), ((1, 1, 0), 6816),
    ((2, 0, -1), 192), ((2, 0, 0), 7296), ((2, 1, -1), 6912), ((2, 1, 0), 192),
    ((3, 0, -1), 96), ((3, 0, 0), 96), ((3, 1, -1), 96), ((3, 1, 0), 96),
)
LANDING_STRATA = ((145, 27264), (146, 14592), (147, 384))

# --- C: the induced three-cube facet problem and the corner ------------------
CUBE_CELLS = 56                          # unimodular cells of the unit 3-cube
CUBE_VOLUME_SPECTRUM = ((0, 12), (1, 56), (2, 2))
FACET_DISSECTIONS = 180
FACET_TETS = 6
TICK_FACETS = 2
MIXED_FACETS = 6
TICK_SPECTRUM = ((18, 16), (19, 72), (20, 84), (21, 8))
MIXED_SPECTRUM = ((8, 12), (9, 64), (10, 104))
TICK_BOX = (36, 42)                      # 2 x [18, 21]
MIXED_BOX = (48, 60)                     # 6 x [8, 10]
CORNER = (36, 60)                        # (TC_min, MC_max)
# the facet-wise caveat, carried as data: the TC ceiling is WITNESSED by a
# genuine dissection, the MC floor is NOT -- 48 would need all six mixed facets
# at 8 simultaneously and no dissection is exhibited that does it.
TC_CEILING_WITNESS_CHARGE = (42, 60)
TC_CEILING_WITNESS_COST = 165
TC_CEILING_WITNESS = (
    26, 103, 123, 186, 192, 330, 578, 709, 745, 748, 768, 826,
    828, 829, 861, 1096, 1142, 1235, 1245, 1327, 1385, 1390, 1419, 1422,
)
MC_FLOOR_UNWITNESSED = 48
QUADRANT_INTERSECTION = ((0, 0),)

# --- D: the promotion --------------------------------------------------------
PROMOTION_INSTANCES = 8893056
C21_INSTANCES = 293376
PROMOTION_FAILURES = 0
PROMOTION_SAMPLE = 200

# --- E: the cost-145 stratum -------------------------------------------------
COST_145 = 145
BLOCKS_145 = 192
BLOCK_SIZE_145 = 1266
CORPUS_145 = 243072
CHARGE_POINTS_145 = (
    ((36, 59), 60768), ((36, 60), 121536), ((37, 60), 60768)
)
BLOCKS_PER_CHARGE_145 = (((36, 59), 48), ((36, 60), 96), ((37, 60), 48))
COOCCURRING_145 = 69888
REFINEMENT_TYPE = (0, 2)                 # the ambiguous non-floor piece type
REFINEMENT_CHARGES = ((36, 59), (36, 60))

# --- F: the sign-indefinite move set at 145 ----------------------------------
DISTANCE2_SPECTRUM = ((-1, 192), (1, 576), (2, 96))
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
D3_MOVES = 132288                        # twice-verified: solve and checker
D3_DIRECTED = (
    ((-1, 0), 66144), ((0, -1), 66144), ((0, 1), 66144), ((1, 0), 66144)
)
D4_MOVES = 2411328
ACHIEVED_145 = ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1))
ACHIEVED_LATTICE_INDEX = 1

# --- G: the bridge-vector boundary -------------------------------------------
ACHIEVED_DIFFERENCES = (
    (-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (1, 1)
)
BRIDGE_DELTAS = ((5, -7), (1, -7))
BRIDGE_MODULUS = 28                      # L = {7x + y = 0 mod 28}
BRIDGE_CHARACTER = (7, 1)
BRIDGE_INDEX = 28
BRIDGE_TARGETS = ((41, 53), (37, 53))    # (36,60) + the two generators
NEGATIVE_TARGETS = ((31, 67), (35, 67))  # (36,60) - the two generators
COMPOSITE_BOUNDS = (((5, -7), 12, 156), ((1, -7), 8, 152))
BRIDGE_WITNESS_41_53_COST = 169
BRIDGE_WITNESS_41_53 = (
    57, 234, 335, 345, 441, 444, 530, 637, 647, 650, 670, 679,
    699, 796, 829, 1489, 1711, 1822, 1874, 2029, 2149, 2435, 2477, 2497,
)
BRIDGE_WITNESS_37_53_COST = 166
BRIDGE_WITNESS_37_53 = (
    56, 250, 310, 361, 438, 447, 448, 499, 531, 568, 693, 797,
    1051, 1128, 1393, 1401, 1421, 1683, 2023, 2046, 2055, 2187, 2280, 2584,
)

# The default gate path runs in about 90 seconds; --deep re-runs the three
# sampled certificates in full and lands near 450, so the budget covers both.
RUNTIME_BUDGET_SEC = 900


# ---------------------------------------------------------------------------
# exact helpers: integer determinants, adjugates, the point-free 3-cube route
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


def adjugate(matrix) -> list:
    """Exact integer adjugate of a square integer matrix."""
    size = len(matrix)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            minor = [
                [matrix[r][c] for c in range(size) if c != i]
                for r in range(size)
                if r != j
            ]
            result[i][j] = ((-1) ** (i + j)) * idet(minor)
    return result


def adjugate_inverse(matrix) -> list:
    """Exact integer inverse of a unimodular integer matrix, by adjugate."""
    determinant = idet(matrix)
    if determinant not in (1, -1):
        raise AssertionError(f"not unimodular: {determinant}")
    return [
        [value // determinant for value in row] for row in adjugate(matrix)
    ]


def three_cube_certificate() -> tuple:
    """The induced facet problem, re-derived here WITHOUT any sample points.

    Block 150 enumerated the 180 minimal dissections of the unit three-cube by
    an exact interior-sample exact cover.  This block takes the POINT-FREE
    route instead: it builds the exact interior-disjointness graph on the
    unimodular cells -- each edge an EXHIBITED integer separating plane drawn
    from the two cells' facet normals and the cross products of their edge
    vectors, a complete candidate family for two tetrahedra -- and enumerates
    its six-cliques.  Six unimodular cells that are pairwise interior-disjoint
    have total normalised volume six, which is the whole cube, so a six-clique
    IS a dissection and conversely; no sampling and no cover search is involved,
    which makes this an independent route to the same spectra rather than a
    re-run of the same one.

    Returns (volume spectrum, cells, dissections, sizes, tick, mixed, alt-axis
    mixed spectra).
    """
    cube = [tuple((k >> (2 - j)) & 1 for j in range(3)) for k in range(8)]
    volumes: Counter = Counter()
    cells = []
    for choice in itertools.combinations(range(8), 4):
        edges = [
            [cube[choice[r + 1]][c] - cube[choice[0]][c] for c in range(3)]
            for r in range(3)
        ]
        value = abs(idet(edges))
        volumes[value] += 1
        if value == 1:
            cells.append(choice)

    edge_pairs = list(itertools.combinations(range(4), 2))

    def facet_normals(cell) -> list:
        matrix = [
            [cube[cell[j + 1]][r] - cube[cell[0]][r] for j in range(3)]
            for r in range(3)
        ]
        rows = adjugate(matrix)
        if idet(matrix) < 0:
            rows = [[-value for value in row] for row in rows]
        out = [tuple(rows[k]) for k in range(3)]
        out.append(
            tuple(-sum(rows[k][r] for k in range(3)) for r in range(3))
        )
        return out

    def cross(u, v) -> tuple:
        return (
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0],
        )

    def separated(left, right) -> bool:
        pa = [cube[c] for c in left]
        pb = [cube[c] for c in right]
        ea = [
            tuple(pa[y][r] - pa[x][r] for r in range(3)) for x, y in edge_pairs
        ]
        eb = [
            tuple(pb[y][r] - pb[x][r] for r in range(3)) for x, y in edge_pairs
        ]
        candidates = facet_normals(left) + facet_normals(right)
        for u in ea:
            for v in eb:
                normal = cross(u, v)
                if any(normal):
                    candidates.append(normal)
        for normal in candidates:
            va = [sum(n * x for n, x in zip(normal, p)) for p in pa]
            vb = [sum(n * x for n, x in zip(normal, p)) for p in pb]
            if max(va) <= min(vb) or max(vb) <= min(va):
                return True
        return False

    count = len(cells)
    disjoint = [[False] * count for _ in range(count)]
    for i in range(count):
        for j in range(i + 1, count):
            value = separated(cells[i], cells[j])
            disjoint[i][j] = disjoint[j][i] = value

    cliques: list[tuple] = []

    def grow(start: int, chosen: list) -> None:
        if len(chosen) == FACET_TETS:
            cliques.append(tuple(chosen))
            return
        for i in range(start, count):
            if all(disjoint[i][j] for j in chosen):
                chosen.append(i)
                grow(i + 1, chosen)
                chosen.pop()

    grow(0, [])

    def cost(cell, axes) -> int:
        return sum(
            1
            for a, b in itertools.combinations(cell, 2)
            if sum(abs(cube[a][c] - cube[b][c]) for c in axes) > 1
        )

    tick_cost = [cost(cell, (0, 1, 2)) for cell in cells]
    mixed_cost = [cost(cell, (0, 1)) for cell in cells]
    tick = Counter(sum(tick_cost[i] for i in clique) for clique in cliques)
    mixed = Counter(sum(mixed_cost[i] for i in clique) for clique in cliques)
    alternates = []
    for axes in ((0, 2), (1, 2)):
        other = [cost(cell, axes) for cell in cells]
        alternates.append(
            tuple(
                sorted(
                    Counter(
                        sum(other[i] for i in clique) for clique in cliques
                    ).items()
                )
            )
        )
    return (
        tuple(sorted(volumes.items())),
        count,
        len(cliques),
        tuple(sorted({len(clique) for clique in cliques})),
        tuple(sorted(tick.items())),
        tuple(sorted(mixed.items())),
        tuple(alternates),
    )


def quadrant_self_negation(vectors: tuple, bound: int) -> tuple:
    """{v in cone(vectors) : -v in cone(vectors)} over an integer box.

    The achieved increments of a floor-anchored class all satisfy dTC >= 0 and
    dMC <= 0.  A set whose nonnegative cone meets its own negation only at the
    origin is SIGN-DEFINITE, and that is what this returns: the intersection is
    computed, not asserted, over every integer combination of the generators
    inside a box, so a nonzero answer would be exhibited rather than inferred.
    """
    reachable = {(0, 0)}
    frontier = {(0, 0)}
    for _step in range(bound):
        grown = set()
        for point in frontier:
            for vector in vectors:
                candidate = (point[0] + vector[0], point[1] + vector[1])
                if abs(candidate[0]) <= bound and abs(candidate[1]) <= bound:
                    if candidate not in reachable:
                        grown.add(candidate)
        if not grown:
            break
        reachable |= grown
        frontier = grown
    return tuple(
        sorted(
            point
            for point in reachable
            if (-point[0], -point[1]) in reachable
        )
    )


def min_composite_cost(target: tuple, increments: tuple, cap: int) -> int:
    """Least total dC4 of a nonnegative composite of `increments` = target.

    `increments` is a tuple of ((dTC, dMC), dC4) pairs measured on the class.
    The answer is an UPPER BOUND on the four-column cost of reaching the target
    charge from the floor: it is an exact integer minimum over multiplicities,
    but it does not certify that the composite can actually be CHAINED as a
    sequence of applicable moves, and it proves nothing about minimality of the
    cost over all routes.  Returns -1 when the target is unreachable in the box.
    """
    best: dict[tuple, int] = {(0, 0): 0}
    frontier = {(0, 0)}
    for _step in range(cap):
        grown = set()
        for point in frontier:
            base = best[point]
            for vector, price in increments:
                if vector == (0, 0):
                    continue
                candidate = (point[0] + vector[0], point[1] + vector[1])
                if abs(candidate[0]) > cap or abs(candidate[1]) > cap:
                    continue
                value = base + price
                if value < best.get(candidate, 1 << 30):
                    best[candidate] = value
                    grown.add(candidate)
        if not grown:
            break
        frontier = grown
    return best.get(target, -1)


def lattice_index(vectors: tuple) -> int:
    """Index in Z^2 of the lattice generated by integer vectors (0 = rank < 2)."""
    value = 0
    for left, right in itertools.combinations(vectors, 2):
        value = gcd(value, abs(left[0] * right[1] - left[1] * right[0]))
    return int(value)


def cone_is_pointed(vectors: tuple) -> bool:
    """True iff the nonnegative cone on `vectors` contains no line."""
    nonzero = [v for v in vectors if v != (0, 0)]
    for left in nonzero:
        for right in nonzero:
            if (
                left[0] * right[1] - left[1] * right[0] == 0
                and left[0] * right[0] + left[1] * right[1] < 0
            ):
                return False
    return True


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    machinery: tuple
    machinery_exit: tuple
    # the shared fixture
    corner_orders_agree: bool
    piece_lists_agree: bool
    volume_spectrum: tuple
    cost_spectrum: tuple
    exact_inverses_agree: bool
    separation_agrees: tuple
    corpus: tuple
    pool_pieces: int
    floor_forcing: bool
    corpus_charge_points: tuple
    independent_corpus: tuple
    # B: the class accounting
    committed_class: tuple
    own_clique_census: tuple
    committed_two_piece: tuple
    reducible: tuple
    reducible_dc4: tuple
    reduction_sample: tuple
    deep_reduction: tuple
    hull_census: tuple
    irreducible: tuple
    irreducible_dc4: tuple
    alternates_total: int
    local_cost_spectrum: tuple
    class_deltas: tuple
    class_joint: tuple
    landing_strata: tuple
    class_cone_pointed: bool
    # C: the corner theorem
    own_three_cube: tuple
    tick_box: tuple
    mixed_box: tuple
    corner: tuple
    tc_ceiling_witness: tuple
    mc_floor_witnessed: bool
    quadrant_intersection: tuple
    corner_forces_class: bool
    # D: the promotion
    promotion_instances: int
    promotion_c21: tuple
    promotion_samples: tuple
    promotion_failures: int
    deep_promotion: tuple
    # E: the cost-145 stratum
    blocks_145: tuple
    block_charge_constant: bool
    charge_points_145: tuple
    blocks_per_charge_145: tuple
    corpus_145: int
    cooccurring_145: tuple
    charge_is_type_function: bool
    refinement_witness: tuple
    # F: the move set at 145
    masks_distinct: bool
    distance2_spectrum: tuple
    within_block_min: int
    min_cross_distance: tuple
    subscan: tuple
    subscan_d3: tuple
    subscan_d4: tuple
    neutral_at_distance_three: bool
    achieved_145: tuple
    achieved_negation_closed: bool
    achieved_cone_pointed: bool
    achieved_index: int
    deep_move_scan: tuple
    # G: the bridge-vector boundary
    achieved_differences: tuple
    bridge_in_lattice: tuple
    bridge_in_achieved: tuple
    negatives_admissible: tuple
    composite_bounds: tuple
    bridge_witnesses: tuple
    bridge_lattice: tuple
    # global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")

    # --- the committed machinery, content-bound and imported at run time -----
    workdir = Path(tempfile.mkdtemp(prefix="block151-machinery-"))
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

    TC = [int(value) for value in c726.TC]
    MC = [int(value) for value in c726.MC]
    C4 = [int(value) for value in c734.C4]
    MASK = list(c734.MASK)
    CM = [int(value) for value in c734.CM]
    SOL = c734.SOL
    USED = c734.USED
    P2I = dict(c734.P2I)
    SSET = [set(cutting) for cutting in SOL]
    piece_index = {
        tuple(int(c) for c in c734.UNI[i]): i for i in range(len(c734.UNI))
    }

    # An exact integer separating-plane predicate of our own, in pure Python
    # integers so that the 69,888 cost-145 incidences are affordable; it is
    # GATED against the committed cycle-734 `separated` routine below, and the
    # candidate normal family is the committed one, vector for vector.
    normals = [t for t in itertools.product((-1, 0, 1), repeat=4) if any(t)]
    corner_points = [
        [int(value) for value in c734.V[k]] for k in range(CORNERS)
    ]
    piece_points = [
        [corner_points[int(c)] for c in c734.UNI[i]] for i in range(len(c734.UNI))
    ]
    piece_facets = []
    for i in range(len(c734.UNI)):
        rows = [
            [int(c734.IV[i][k][c]) for c in range(4)] for k in range(4)
        ]
        rows.append(
            [-sum(int(c734.IV[i][k][c]) for k in range(4)) for c in range(4)]
        )
        piece_facets.append(rows)
    separation_cache: dict[tuple, bool] = {}

    def apart(left: int, right: int) -> bool:
        key = (left, right) if left < right else (right, left)
        value = separation_cache.get(key)
        if value is None:
            pa, pb = piece_points[key[0]], piece_points[key[1]]
            value = False
            for normal in (
                normals + piece_facets[key[0]] + piece_facets[key[1]]
            ):
                sa = [
                    p[0] * normal[0] + p[1] * normal[1]
                    + p[2] * normal[2] + p[3] * normal[3]
                    for p in pa
                ]
                sb = [
                    p[0] * normal[0] + p[1] * normal[1]
                    + p[2] * normal[2] + p[3] * normal[3]
                    for p in pb
                ]
                if max(sa) <= min(sb) or max(sb) <= min(sa):
                    value = True
                    break
            separation_cache[key] = value
        return value

    sample_pairs = [
        (USED[a], USED[b]) for a, b in c734.CP[::7]
    ] + [
        (int(a), int(b))
        for a, b in itertools.combinations(range(0, len(c734.UNI), 331), 2)
    ]
    separation_agrees = (
        len(sample_pairs),
        sum(
            1
            for a, b in sample_pairs
            if apart(a, b) == (c734.separated([a, b])[0] == 1)
        ),
    )

    cost_sums = [sum(C4[p] for p in cutting) for cutting in SOL]
    floor_forcing = bool(
        min(C4) == PIECE_COST_FLOOR
        and CUTTING_SIZE * PIECE_COST_FLOOR == FLOOR_CLASS
        and all(len(cutting) == CUTTING_SIZE for cutting in SOL)
        and set(cost_sums) == {FLOOR_CLASS}
        and all(C4[piece] == PIECE_COST_FLOOR for piece in USED)
    )
    corpus_charge_counter = Counter(
        (sum(TC[p] for p in cutting), sum(MC[p] for p in cutting))
        for cutting in SOL
    )
    corpus_charge_points = tuple(sorted(corpus_charge_counter.items()))
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

    # --- B: the class accounting ---------------------------------------------
    # The committed cycle-734 gate `three.none` ran inside the imported prefix;
    # these are ITS numbers, read off the module, not re-derived.
    committed_class = (
        int(c734.CLIQUE),
        int(c734.SPURIOUS),
        int(c734.TRI),
        int(c734.KEEP),
        int(c734.RAISE),
        tuple(sorted((int(k), int(v)) for k, v in c734.TSP.items())),
    )
    committed_two_piece = (
        len(c734.FLIP), tuple(sorted(c734.DL)), int(c734.GEO2)
    )
    MEM = list(c734.MEM)
    pool = len(USED)
    adjacency = [0] * pool
    for a in range(pool):
        for b in range(pool):
            if a != b and c734.CO[a, b]:
                adjacency[a] |= 1 << b

    own_cliques = own_spurious = 0
    triples: list[tuple] = []
    for a in range(pool):
        neighbours = [b for b in range(a + 1, pool) if (adjacency[a] >> b) & 1]
        for x in range(len(neighbours)):
            b = neighbours[x]
            for y in range(x + 1, len(neighbours)):
                c = neighbours[y]
                if not (adjacency[b] >> c) & 1:
                    continue
                own_cliques += 1
                if not (MEM[a] & MEM[b] & MEM[c]):
                    own_spurious += 1
                    continue
                triples.append((a, b, c))
    own_clique_census = (own_cliques, own_spurious, len(triples))

    def region_of(org: tuple) -> tuple:
        hull = corners = 0
        for piece in org:
            hull |= CM[piece]
            corners |= MASK[piece]
        return hull, corners

    def refills3(org: tuple) -> list:
        """Every three-piece exact refill of the region a triple spans.

        The candidate pool is enumerated from the region's CORNER HULL, which
        is what makes the search affordable; it is gated against the committed
        cycle-734 `refills` on a sample below, set for set.
        """
        hull, region = region_of(org)
        available = [k for k in range(CORNERS) if (hull >> k) & 1]
        candidates = [
            piece
            for piece in (
                piece_index.get(sub)
                for sub in itertools.combinations(available, 5)
            )
            if piece is not None and not (MASK[piece] & ~region)
        ]
        out = []
        size = len(candidates)
        for i in range(size):
            mask_i = MASK[candidates[i]]
            for j in range(i + 1, size):
                mask_j = MASK[candidates[j]]
                if mask_i & mask_j:
                    continue
                pair_mask = mask_i | mask_j
                for k in range(j + 1, size):
                    mask_k = MASK[candidates[k]]
                    if pair_mask & mask_k or (pair_mask | mask_k) != region:
                        continue
                    out.append(
                        (candidates[i], candidates[j], candidates[k])
                    )
        return out

    # the reducible part, CONSTRUCTED from the committed 288 two-piece re-cuts:
    # a triple containing a flippable pair inherits that pair's alternate with
    # the third piece as a SPECTATOR, and the result is automatically an exact
    # refill of the same region.
    flip_alternate = {
        pr: tuple(sorted(next(t for t in c734.SEC2[pr] if set(t) != set(pr))))
        for pr in c734.FLIP
    }
    reducible_rows: list[tuple] = []
    reducible_counter: Counter = Counter()
    removed_pairs: set = set()
    for pr in c734.FLIP:
        a, b = P2I[pr[0]], P2I[pr[1]]
        alternate = flip_alternate[pr]
        delta = sum(C4[j] for j in alternate) - (C4[pr[0]] + C4[pr[1]])
        both = MEM[a] & MEM[b]
        for c in range(pool):
            if c in (a, b) or not (both & MEM[c]):
                continue
            key = tuple(sorted((a, b, c)))
            org = tuple(sorted((pr[0], pr[1], USED[c])))
            new = tuple(sorted(alternate + (USED[c],)))
            reducible_rows.append((org, new, LOCAL_FLOOR_3 + delta, key))
            reducible_counter[delta] += 1
            removed_pairs.add(tuple(sorted(pr)))
    reducible = (
        len(reducible_rows),
        len(removed_pairs),
        len({tuple(sorted(set(row[0]) - set(row[1]))) for row in reducible_rows}),
        all(
            bin(CM[pair[0]] & CM[pair[1]]).count("1") == REDUCIBLE_SHARED_CORNERS
            for pair in removed_pairs
        ),
    )
    reducible_dc4 = tuple(sorted(reducible_counter.items()))

    # the irreducible part, SEARCHED on the minimum seven-corner hulls: every
    # refill that shares no piece with its triple turns out to live there, and
    # the count closes against the committed 42,240 exactly, which is what
    # makes the restricted search COMPLETE rather than merely suggestive.
    hull_counter: Counter = Counter()
    hull_seven: list[tuple] = []
    for key in triples:
        org = tuple(sorted(USED[i] for i in key))
        size = bin(region_of(org)[0]).count("1")
        hull_counter[size] += 1
        if size == HULL_MIN_CORNERS:
            hull_seven.append((org, key))
    irreducible_rows: list[tuple] = []
    hull_seven_alternates = 0
    for org, key in hull_seven:
        original = set(org)
        for option in refills3(org):
            if set(option) == original:
                continue
            hull_seven_alternates += 1
            if not (set(option) & original):
                irreducible_rows.append(
                    (org, tuple(sorted(option)), sum(C4[j] for j in option), key)
                )
    hull_census = (
        tuple(sorted(hull_counter.items())),
        len(hull_seven),
        hull_seven_alternates,
    )
    irreducible = len(irreducible_rows)
    irreducible_dc4 = tuple(
        sorted(
            Counter(
                row[2] - LOCAL_FLOOR_3 for row in irreducible_rows
            ).items()
        )
    )

    alternates = reducible_rows + irreducible_rows
    alternates_total = len(alternates)
    local_cost_spectrum = tuple(
        sorted(Counter(row[2] for row in alternates).items())
    )
    class_delta_counter = Counter(
        (
            sum(TC[j] for j in row[1]) - sum(TC[j] for j in row[0]),
            sum(MC[j] for j in row[1]) - sum(MC[j] for j in row[0]),
        )
        for row in alternates
    )
    class_deltas = tuple(sorted(class_delta_counter.items()))
    class_joint = tuple(
        sorted(
            Counter(
                (
                    row[2] - LOCAL_FLOOR_3,
                    sum(TC[j] for j in row[1]) - sum(TC[j] for j in row[0]),
                    sum(MC[j] for j in row[1]) - sum(MC[j] for j in row[0]),
                )
                for row in alternates
            ).items()
        )
    )
    landing_strata = tuple(
        sorted(
            Counter(
                FLOOR_CLASS + row[2] - LOCAL_FLOOR_3 for row in alternates
            ).items()
        )
    )
    class_cone_pointed = cone_is_pointed(
        tuple(delta for delta, _count in class_deltas)
    )

    # the completeness spot-check: on a deterministic sample of triples the
    # exhaustive refill search is run BOTH by our corner-hull enumerator and by
    # the committed cycle-734 `refills`, the two are required to agree set for
    # set, and the resulting alternate set is required to be exactly what the
    # construction above predicts for that triple.
    predicted: dict[tuple, set] = {}
    for row in alternates:
        predicted.setdefault(row[3], set()).add(row[1])
    stride = max(1, len(triples) // REDUCTION_SAMPLE)

    def check_triples(selection) -> tuple:
        checked = matched = committed_agree = 0
        for key in selection:
            org = tuple(sorted(USED[i] for i in key))
            hull, region = region_of(org)
            ours = {
                tuple(sorted(option))
                for option in refills3(org)
                if set(option) != set(org)
            }
            theirs = {
                tuple(sorted(option))
                for option in c734.refills(hull, region, 3, c734.ALLI, c734.CM)[1]
                if set(option) != set(org)
            }
            checked += 1
            committed_agree += int(ours == theirs)
            matched += int(ours == predicted.get(key, set()))
        return checked, matched, committed_agree

    reduction_sample = check_triples(triples[::stride][:REDUCTION_SAMPLE])
    deep_reduction = (0, 0, 0)
    if deep:
        deep_reduction = check_triples(triples)

    # --- C: the corner theorem ------------------------------------------------
    def verify_dissection(pieces: tuple) -> tuple:
        ordered = tuple(sorted(pieces))
        cover = 0
        overlap = False
        for piece in ordered:
            if cover & MASK[piece]:
                overlap = True
            cover |= MASK[piece]
        pairs = list(itertools.combinations(ordered, 2))
        return (
            len(ordered),
            bool(
                len(set(ordered)) == len(ordered)
                and not overlap
                and cover == c734.ALLQ
            ),
            sum(1 for a, b in pairs if apart(a, b)),
            len(pairs),
            sum(TC[piece] for piece in ordered),
            sum(MC[piece] for piece in ordered),
            sum(C4[piece] for piece in ordered),
        )

    own_three_cube = three_cube_certificate()
    tick_values = [value for value, _count in own_three_cube[4]]
    mixed_values = [value for value, _count in own_three_cube[5]]
    tick_box = (TICK_FACETS * min(tick_values), TICK_FACETS * max(tick_values))
    mixed_box = (
        MIXED_FACETS * min(mixed_values), MIXED_FACETS * max(mixed_values)
    )
    corner = (tick_box[0], mixed_box[1])
    tc_ceiling_witness = verify_dissection(TC_CEILING_WITNESS)
    # every (TC, MC) value this runner has an EXHIBITED dissection for; the MC
    # floor of the facet-wise box is checked against it rather than assumed
    # unattainable, and the honest answer is that it is NOT witnessed.
    observed_mc = {point[1] for point, _count in corpus_charge_points}
    observed_mc.add(tc_ceiling_witness[5])
    quadrant_intersection = quadrant_self_negation(
        tuple(delta for delta, _count in class_deltas), 8
    )
    corner_forces_class = all(
        corner[0] + delta[0] >= tick_box[0]
        and corner[1] + delta[1] <= mixed_box[1]
        for delta, _count in class_deltas
    )

    # --- D: the promotion -----------------------------------------------------
    host_bits: dict[tuple, int] = {}

    def hosts_of(key: tuple) -> int:
        bits = host_bits.get(key)
        if bits is None:
            bits = MEM[key[0]] & MEM[key[1]] & MEM[key[2]]
            host_bits[key] = bits
        return bits

    def bit_positions(bits: int) -> list:
        out = []
        while bits:
            low = bits & -bits
            out.append(low.bit_length() - 1)
            bits ^= low
        return out

    promotion_instances = sum(
        bin(hosts_of(row[3])).count("1") for row in alternates
    )

    def certify(selection) -> tuple:
        """Promote (triple, host, refill) instances to genuine re-cuts.

        For one (triple, refill) the check is done ONCE against the union of
        every host's complement: the refill pieces must tile the triple's own
        region exactly, be pairwise interior-disjoint, and be interior-disjoint
        from every piece that can appear in a host complement.  That certifies
        the swap for EVERY host at once, which is why the instance count can be
        8,893,056 while the geometric work stays finite.
        """
        good = total = 0
        for org, alternate, _cost, key in selection:
            original, replacement = set(org), set(alternate)
            hosts = bit_positions(hosts_of(key))
            total += len(hosts)
            complement: set = set()
            for host in hosts:
                complement |= SSET[host] - original
            region = region_of(org)[1]
            cover = 0
            clash = False
            for piece in replacement:
                if cover & MASK[piece]:
                    clash = True
                cover |= MASK[piece]
            if (
                not clash
                and len(replacement) == 3
                and cover == region
                and all(
                    apart(x, y)
                    for x, y in itertools.combinations(sorted(replacement), 2)
                )
                and all(
                    apart(fresh, old)
                    for fresh in (replacement - original)
                    for old in complement
                )
            ):
                good += len(hosts)
        return good, total

    stratum_21 = [row for row in alternates if row[2] == 21]
    promotion_c21 = certify(stratum_21)
    promotion_samples = []
    for cost in (19, 20):
        bucket = [row for row in alternates if row[2] == cost]
        step = max(1, len(bucket) // PROMOTION_SAMPLE)
        promotion_samples.append(
            (cost,) + certify(bucket[::step][:PROMOTION_SAMPLE])
        )
    promotion_samples = tuple(promotion_samples)
    promotion_failures = (
        promotion_c21[1] - promotion_c21[0]
        + sum(row[2] - row[1] for row in promotion_samples)
    )
    deep_promotion = (0, 0)
    if deep:
        deep_promotion = certify(alternates)

    # --- E: the cost-145 stratum ---------------------------------------------
    # A cost-145 cutting is 23 floor pieces plus exactly ONE piece of cost 7, so
    # the stratum decomposes into BLOCKS indexed by that piece.  The block
    # indices are not guessed: they are read off the class itself, as the
    # non-floor pieces that its own dC4 = 1 refills produce.
    block_ids = sorted(
        {
            piece
            for row in alternates
            if row[2] == LOCAL_FLOOR_3 + 1
            for piece in row[1]
            if C4[piece] == PIECE_COST_FLOOR + 1
        }
    )
    floor_pool = [int(piece) for piece in c734.MINP]

    def completions(piece: int) -> list:
        target = c734.ALLQ & ~MASK[piece]
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
    block_constant = True
    for piece in block_ids:
        found = completions(piece)
        blocks[piece] = found
        charges = {
            (
                TC[piece] + sum(TC[q] for q in cutting),
                MC[piece] + sum(MC[q] for q in cutting),
            )
            for cutting in found
        }
        if len(charges) != 1:
            block_constant = False
        block_charge[piece] = sorted(charges)[0]
    blocks_145 = (
        len(blocks), tuple(sorted({len(v) for v in blocks.values()}))
    )
    corpus_145 = sum(len(v) for v in blocks.values())
    charge_points_145 = tuple(
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
    blocks_per_charge_145 = tuple(
        sorted(Counter(block_charge.values()).items())
    )
    observed_mc |= {point[1] for point, _count in charge_points_145}
    pairs_145: set = set()
    for piece in block_ids:
        for cutting in blocks[piece]:
            whole = (piece,) + cutting
            for a, b in itertools.combinations(sorted(whole), 2):
                pairs_145.add((a, b))
    cooccurring_145 = (
        len(pairs_145), sum(1 for a, b in pairs_145 if apart(a, b))
    )
    # the refinement: the block charge is a function of the non-floor piece's
    # IDENTITY, and NOT of its own (TC, MC) type -- exhibited, not asserted.
    by_type: dict[tuple, set] = {}
    for piece in block_ids:
        by_type.setdefault((TC[piece], MC[piece]), set()).add(
            block_charge[piece]
        )
    charge_is_type_function = all(
        len(values) == 1 for values in by_type.values()
    )
    ambiguous = sorted(
        (kind, tuple(sorted(values)))
        for kind, values in by_type.items()
        if len(values) > 1
    )
    witness_pieces = ()
    if ambiguous:
        kind = ambiguous[0][0]
        seen: dict[tuple, int] = {}
        for piece in block_ids:
            if (TC[piece], MC[piece]) == kind:
                seen.setdefault(block_charge[piece], piece)
        witness_pieces = tuple(
            (seen[point], point) for point in sorted(seen)
        )
    refinement_witness = (
        tuple(ambiguous), witness_pieces
    )
    mc_floor_witnessed = mixed_box[0] in observed_mc

    # --- F: the sign-indefinite move set at 145 -------------------------------
    masks_distinct = len(set(MASK)) == len(c734.UNI)
    distance2_counter: Counter = Counter()
    for a, b in sorted(pairs_145):
        hull, region = region_of((a, b))
        for option in c734.refills(hull, region, 2, c734.ALLI, c734.CM)[1]:
            if set(option) == {a, b}:
                continue
            distance2_counter[
                sum(C4[j] for j in option) - (C4[a] + C4[b])
            ] += 1
    distance2_spectrum = tuple(sorted(distance2_counter.items()))

    by_charge: dict[tuple, list] = {}
    for piece in block_ids:
        by_charge.setdefault(block_charge[piece], []).append(piece)
    sample_blocks = [
        piece
        for point in sorted(by_charge)
        for piece in sorted(by_charge[point])[:SUBSCAN_PER_CHARGE]
    ]
    universe = sorted(
        {q for piece in sample_blocks for cutting in blocks[piece] for q in cutting}
        | set(sample_blocks)
    )
    position = {q: i for i, q in enumerate(universe)}
    popcount = np.array(
        [bin(value).count("1") for value in range(256)], dtype=np.uint8
    )
    packed: dict[int, object] = {}
    for piece in sample_blocks:
        indicator = np.zeros(
            (len(blocks[piece]), len(universe)), dtype=np.uint8
        )
        for row, cutting in enumerate(blocks[piece]):
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
    for piece in sample_blocks:
        matrix = distances(piece, piece)
        rows, columns = np.triu_indices(len(blocks[piece]), 1)
        values = matrix[rows, columns]
        within_block_min = min(within_block_min, int(values.min()))
        if int((values <= 3).sum()):
            neutral_at_distance_three = True
    cross_min: dict[tuple, int] = {}
    subscan_d3: Counter = Counter()
    subscan_d4: Counter = Counter()
    for i in range(len(sample_blocks)):
        for j in range(i + 1, len(sample_blocks)):
            left, right = sample_blocks[i], sample_blocks[j]
            matrix = distances(left, right)
            point_a, point_b = block_charge[left], block_charge[right]
            key = (point_a, point_b) if point_a <= point_b else (point_b, point_a)
            value = int(matrix.min())
            if value < cross_min.get(key, CUTTING_SIZE):
                cross_min[key] = value
            delta = (point_b[0] - point_a[0], point_b[1] - point_a[1])
            if delta == (0, 0) and int((matrix <= 3).sum()):
                neutral_at_distance_three = True
            for size, bag in ((3, subscan_d3), (4, subscan_d4)):
                count = int((matrix == size).sum())
                if count:
                    bag[delta] += count
                    if delta != (0, 0):
                        bag[(-delta[0], -delta[1])] += count
    subscan = (
        len(sample_blocks),
        tuple(sorted(Counter(block_charge[p] for p in sample_blocks).items())),
    )
    min_cross_distance = tuple(
        (key, value) for key, value in sorted(cross_min.items())
        if key[0] != key[1]
    )
    subscan_d3_out = tuple(sorted(subscan_d3.items()))
    subscan_d4_out = tuple(sorted(subscan_d4.items()))
    achieved_145 = tuple(
        sorted(
            {delta for delta in subscan_d3 if delta != (0, 0)}
            | {delta for delta in subscan_d4 if delta != (0, 0)}
        )
    )
    achieved_negation_closed = all(
        (-delta[0], -delta[1]) in achieved_145 for delta in achieved_145
    )
    achieved_cone_pointed = cone_is_pointed(achieved_145)
    achieved_index = lattice_index(achieved_145)

    deep_move_scan = (0, 0, ())
    if deep:
        ordered = 0
        neutral = 0
        directed: Counter = Counter()
        for piece in block_ids:
            listing = blocks[piece]
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
                    # same cost class: the re-cut must preserve the local cost
                    if sum(C4[j] for j in option) != sum(C4[j] for j in org):
                        continue
                    upper = [j for j in option if C4[j] == PIECE_COST_FLOOR + 1]
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
                                block_charge[other][0] - block_charge[piece][0],
                                block_charge[other][1] - block_charge[piece][1],
                            )
                        ] += hosts
        deep_move_scan = (
            ordered // 2, neutral, tuple(sorted(directed.items()))
        )

    # --- G: the bridge-vector boundary ---------------------------------------
    points_145 = tuple(point for point, _count in charge_points_145)
    achieved_differences = tuple(
        sorted(
            {
                (right[0] - left[0], right[1] - left[1])
                for left in points_145
                for right in points_145
            }
        )
    )
    bridge_in_lattice = tuple(
        (
            generator,
            bool(
                achieved_index == 1
                and (1, 0) in achieved_145
                and (0, 1) in achieved_145
            ),
        )
        for generator in BRIDGE_DELTAS
    )
    bridge_in_achieved = tuple(
        (generator, generator in achieved_differences)
        for generator in BRIDGE_DELTAS
    )
    # a floor-anchored composite reaching the NEGATIVE of a bridge generator
    # would have to land outside the facet-wise box; that is checked here on the
    # box this runner derived, not on an imported bound.
    negatives_admissible = tuple(
        (
            point,
            bool(point[0] >= tick_box[0] and point[1] <= mixed_box[1]),
        )
        for point in NEGATIVE_TARGETS
    )
    increments = tuple(
        ((tick, mixed), cost) for cost, tick, mixed in
        (row[0] for row in class_joint)
    )
    composite_bounds = tuple(
        (
            generator,
            min_composite_cost(generator, increments, 16),
            FLOOR_CLASS + min_composite_cost(generator, increments, 16),
        )
        for generator in BRIDGE_DELTAS
    )
    bridge_witnesses = (
        (BRIDGE_TARGETS[0],) + verify_dissection(BRIDGE_WITNESS_41_53),
        (BRIDGE_TARGETS[1],) + verify_dissection(BRIDGE_WITNESS_37_53),
    )
    bridge_lattice = lattice_from_generators(
        BRIDGE_DELTAS, BRIDGE_CHARACTER, BRIDGE_MODULUS
    )

    integer_arrays = (
        c734.C4, c726.TC, c726.MC, c726.BX, c734.IV, c734.MM, c726.SCOST,
        popcount,
    )
    exact_no_float = bool(
        all(np.issubdtype(array.dtype, np.integer) for array in integer_arrays)
        and Fraction(FLOOR_CLASS, CUTTING_SIZE) == Fraction(PIECE_COST_FLOOR, 1)
        and Fraction(COST_145, 1) == Fraction(FLOOR_CLASS + 1, 1)
        and all(
            isinstance(value, int)
            for value in (
                promotion_instances, alternates_total, corpus_145,
                own_cliques, achieved_index, within_block_min,
            )
        )
        and not any(
            isinstance(value, float)
            for delta, _count in class_deltas
            for value in delta
        )
        and not any(
            isinstance(value, float)
            for delta in achieved_145
            for value in delta
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        machinery=machinery_shape,
        machinery_exit=machinery_exit,
        corner_orders_agree=corner_orders_agree,
        piece_lists_agree=piece_lists_agree,
        volume_spectrum=volume_spectrum,
        cost_spectrum=cost_spectrum,
        exact_inverses_agree=exact_inverses_agree,
        separation_agrees=separation_agrees,
        corpus=(len(SOL), CORPUS),
        pool_pieces=len(USED),
        floor_forcing=floor_forcing,
        corpus_charge_points=corpus_charge_points,
        independent_corpus=independent_corpus,
        committed_class=committed_class,
        own_clique_census=own_clique_census,
        committed_two_piece=committed_two_piece,
        reducible=reducible,
        reducible_dc4=reducible_dc4,
        reduction_sample=reduction_sample,
        deep_reduction=deep_reduction,
        hull_census=hull_census,
        irreducible=irreducible,
        irreducible_dc4=irreducible_dc4,
        alternates_total=alternates_total,
        local_cost_spectrum=local_cost_spectrum,
        class_deltas=class_deltas,
        class_joint=class_joint,
        landing_strata=landing_strata,
        class_cone_pointed=class_cone_pointed,
        own_three_cube=own_three_cube,
        tick_box=tick_box,
        mixed_box=mixed_box,
        corner=corner,
        tc_ceiling_witness=tc_ceiling_witness,
        mc_floor_witnessed=mc_floor_witnessed,
        quadrant_intersection=quadrant_intersection,
        corner_forces_class=corner_forces_class,
        promotion_instances=promotion_instances,
        promotion_c21=promotion_c21,
        promotion_samples=promotion_samples,
        promotion_failures=promotion_failures,
        deep_promotion=deep_promotion,
        blocks_145=blocks_145,
        block_charge_constant=block_constant,
        charge_points_145=charge_points_145,
        blocks_per_charge_145=blocks_per_charge_145,
        corpus_145=corpus_145,
        cooccurring_145=cooccurring_145,
        charge_is_type_function=charge_is_type_function,
        refinement_witness=refinement_witness,
        masks_distinct=masks_distinct,
        distance2_spectrum=distance2_spectrum,
        within_block_min=within_block_min,
        min_cross_distance=min_cross_distance,
        subscan=subscan,
        subscan_d3=subscan_d3_out,
        subscan_d4=subscan_d4_out,
        neutral_at_distance_three=neutral_at_distance_three,
        achieved_145=achieved_145,
        achieved_negation_closed=achieved_negation_closed,
        achieved_cone_pointed=achieved_cone_pointed,
        achieved_index=achieved_index,
        deep_move_scan=deep_move_scan,
        achieved_differences=achieved_differences,
        bridge_in_lattice=bridge_in_lattice,
        bridge_in_achieved=bridge_in_achieved,
        negatives_admissible=negatives_admissible,
        composite_bounds=composite_bounds,
        bridge_witnesses=bridge_witnesses,
        bridge_lattice=bridge_lattice,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


def lattice_from_generators(
    generators: tuple, character: tuple, modulus: int
) -> tuple:
    """Re-derive the Block 130 bridge lattice L from the WITNESS DIFFERENCES.

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
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE CLASS ACCOUNTING, CORRECTED, AND THE CLASS REDUCED: the cycle-734 gate is rebuilt from the corpus rather than quoted -- 649,600 co-occurrence cliques, 13,568 SPURIOUS (three pairwise co-occurring pieces sharing NO common cutting), 636,032 GENUINE triples, KEEP = 0 and RAISE = 40,512 reproduced EXACTLY -- and the number the parent handed forward counts a DIFFERENT OBJECT than its label says: RAISE = 40,512 counts TRIPLES admitting a second three-piece refill, while the REFILLS themselves number 42,240, at local C4 costs 19 (27,264), 20 (14,592) and 21 (384) summing to 42,240 and NOT to 40,512, so "40,512 at local costs 19/20/21" CONFLATES the triple count with the refill count and every statement here is made on the 42,240 refills because a refill is the object that can be a MOVE; every source triple is three co-occurring pieces of C4 = 6 at local cost 3 x 6 = 18 with 21 pieces untouched, and dC4 in {1,2,3} on every alternate, so NO three-piece move holds the floor; and the class is SMALLER THAN ITS NAME -- 41,088 of the 42,240 alternates replace only TWO of the three pieces, the removed pair ALWAYS sharing EXACTLY FOUR corners, over EXACTLY 288 distinct removed pairs, which is cycle-734\'s COMPLETE two-piece move set with a SPECTATOR piece adjoined and therefore a class Block 150 had ALREADY measured, so 97% of the "three-piece incidence candidates" was already decided; the IRREDUCIBLY three-piece remainder is 1,152 alternates, all on 7-CORNER regions, with dC4 in {2,3} ONLY (768 at +2 and 384 at +3, NEVER +1, so it never even reaches stratum 145), and its own deltas {(0,-1):288, (0,0):480, (1,-1):96, (1,0):288} occupy the SAME pointed quadrant -- the reduction is NOT an escape route\nper_site: THE PROMOTION, AND WHOSE RESULT IT IS: cycle 734 stopped at INCIDENCE, declaring the alternates CANDIDATES and not re-cuts, and Block 150 inherited that boundary verbatim in its move rider; this block RETIRES it, by testing two things exactly on every instance -- COVERING, the union of the alternate\'s piece masks EQUAL to the region span as an exact MASK EQUALITY and never a sampled volume, and DISJOINTNESS, every pair inside the alternate and every NEW piece against every piece of the HOST\'S COMPLEMENT separated by an EXHIBITED INTEGER PLANE -- over the FULL HOST CROSS PRODUCT, because a (triple, alternate) pair is a move only relative to a host cutting containing the triple and the complement differs from host to host; the result is 8,893,056 (triple, host, alternate) instances tested, 8,893,056 PASS, ZERO FAILURES, covering equality on all 42,240, so ALL 42,240 alternates are GENUINE GEOMETRIC RE-CUTS FOR EVERY HOST and cycle-734\'s "incidence candidates only, NOT promoted" caveat is RETIRED; the checker fully RE-VERIFIED the complete local-cost-21 stratum -- the smallest and structurally most delicate, at 384 alternates -- and sampled the local-cost-19 and local-cost-20 strata on its OWN independently constructed sample lattice, distinct from all three committed point families; and the retirement is stated as a CONTRIBUTION TO THE OTHER LANE\'S OWN PROGRAM, a result about THEIR object produced from THEIR committed machinery on origin/main, superseding NO unmerged work\nper_mode: THE FLOOR-CORNER THEOREM, THE STRUCTURAL HEADLINE: the 180 minimal 3-cube facet dissections, each of six unit-determinant tetrahedra, are rebuilt from scratch on THREE INDEPENDENT ROUTES -- the solve\'s N = 11 rational sample grid (the committed cycle-726 runner used 58 points), the checker\'s INDEPENDENT INTEGER-LATTICE EXACT COVER, and the checker\'s POINT-FREE CLIQUE ENUMERATION which uses NO SAMPLE LATTICE AT ALL and therefore removes the last shared assumption, since routes 1 and 2 both decide interior membership by barycentric signs at sample points and a shared blind spot in that method would be invisible to their agreement -- and all three give tick facet spectrum {18:16, 19:72, 20:84, 21:8} and mixed facet spectrum {8:12, 9:64, 10:104}; the four-box has TWO tick facets and SIX mixed facets, so EVERY minimal dissection of the four-box has TC in [36, 42] and MC in [48, 60], with the MC = 48 end a FACET-WISE bound (six mixed facets each at their own minimum 8) that is NOT WITNESSED by any four-box cutting enumerated here and is displayed as a valid lower bound rather than an attained value; the cost-144 corpus sits at (36, 60) = (TC_min, MC_max), the EXTREME CORNER of that box, and both of those extremes ARE attained by all 15,800 floor cuttings, so the unwitnessed end weakens nothing; whence THE THEOREM: for ANY minimal dissection X reachable from a floor cutting by ANY move, TC(X) >= 36 = TC(floor) and MC(X) <= 60 = MC(floor), so dTC >= 0 and dMC <= 0 ALWAYS, and NO FLOOR-ANCHORED MOVE CLASS OF ANY SIZE CAN BE SIGN-INDEFINITE -- a statement quantifying over move classes NEVER BUILT, four-piece, three-piece, k-piece for any k, single or composite, promoted or not, since a set inside a pointed quadrant cannot be negation-closed unless it is {(0,0)}; and TWO SHADOWS OF ONE CORNER: Block 150\'s flip class STAYS INSIDE the floor so its delta is (0,0), the only quadrant point that is also a return, while this block\'s three-piece class LEAVES the floor so its delta is one-sided in the quadrant -- the parent\'s neutrality was a fact about WHERE ITS POPULATION SITS IN THE GLOBAL BRACKET\nper_block: THE STRATA LANDSCAPE, AND THE PROMOTED CLASS\'S OWN CENSUS: the promoted class is STRICTLY DIRECTED -- achieved increments {(0,-1) x7104, (0,0) x21024, (1,-1) x7008, (1,0) x7104}, landing strata {145: 27,264, 146: 14,592, 147: 384} with 144 NEVER, a POINTED cone in the quadrant dTC >= 0 and dMC <= 0, (0,1) and (-1,0) realized by ZERO of the 42,240, and a lattice Z^2 at INDEX 1 that STRICTLY CONTAINS the bridge\'s L = {7x + y = 0 mod 28} at index 28, which is the EXACT INVERSION of Block 150\'s kill: there the achieved lattice had RANK 0 and the conditional died on RANK, here it has RANK 2 and index 1 and the conditional still fails because the achieved set is NOT NEGATION-CLOSED, so the obstruction is SIGN and NOT RANK; and CHARGE RIGIDITY IS A FLOOR FACT, NOT A LANE FACT -- budgeted exact covers enumerate 258,872 cuttings with C4 <= 145 over 9,522,735 nodes of which 243,072 sit at EXACTLY 145, and 2,618,552 with C4 <= 146 of which 2,359,680 sit at EXACTLY 146, with budget 0 degenerating to Block 150\'s 15,800 as a PASSED hostile control; stratum 145 is GEOMETRICALLY GATED, all 69,888 co-occurring pairs split by an EXHIBITED INTEGER PLANE at 69,888/69,888, and the checker REBUILT it by a DIFFERENT DECOMPOSITION at 730,566,987 nodes, while stratum 146 is measured at INCIDENCE LEVEL ONLY with NO separating-plane certificate -- a DISPLAYED BOUNDARY on which no conclusion rests; the charge points run 1 -> 3 -> 6 across strata 144/145/146, at 145 exactly (36,59) x60,768, (36,60) x121,536 and (37,60) x60,768 and at 146 the six points (36,58), (36,59), (36,60), (37,59), (37,60), (38,60), ALL still inside the corner cone TC >= 36, MC <= 60 as the global bracket requires; and at 145 every cutting has EXACTLY ONE piece of C4 = 7, giving 192 BLOCKS of EXACTLY 1,266 indexed by that lone piece with the charge CONSTANT on every block, refined by the checker to the statement that the charge is a function of the IDENTITY of that piece and NOT of its own CHARGE TYPE, since the (0,2) pieces SPLIT 48/96 across TWO DIFFERENT charge points -- the block\'s charge depends on how the piece SITS, not on what it CARRIES -- with the downstream consequence that every charge-changing move at 145 must SWAP the lone non-floor piece\nlattice_wide: THE SIGN-INDEFINITE MOVE SET, THE BRIDGE-VECTOR BOUNDARY, AND THE DOWNSTREAM DELIVERY: cycle 734\'s KEEP = 0 says there is NO same-class three-piece move at the floor, and ONE COST UNIT UP THAT REVERSES -- a COMPLETE scan of ALL 243,072 cost-145 cuttings gives exact minimum cross-charge distances 3 between (36,59) and (36,60), 4 between (36,59) and (37,60), and 3 between (36,60) and (37,60), so the THREE-PIECE same-class class is POPULATED; distance 1 and distance 2 are EXCLUDED STRUCTURALLY rather than merely unobserved, and the WITHIN-BLOCK minimum distance is 4, so every distance-3 move ALWAYS crosses blocks, hence always swaps the lone C4 = 7 piece, hence always CHANGES the charge -- which is exactly why NOT ONE of the 132,288 unordered distance-3 same-class moves is charge-neutral, the EXACT INVERSION of the floor where EVERY move of EVERY size is; those moves achieve EXACTLY +-(1,0) and +-(0,1) at 66,144 EACH, and the 2,411,328 distance-4 moves add +-(1,1) alongside 1,348,608 neutral ones, so the achieved set {+-(1,0), +-(0,1), +-(1,1)} is NEGATION-CLOSED with cone R^2 -- NOT POINTED -- and lattice Z^2 at index 1 STRICTLY CONTAINING L, every move being MUTUALLY REVERSIBLE as an unordered pair of C4 = 145 cuttings read both ways so that forward and reverse are the SAME move with field 7 TRUE under the inherited M5 declaration that cost class = the C4 level set: SIGN-INDEFINITE, MUTUALLY REVERSIBLE, SAME COST CLASS, the FIRST move class in the cell-cutting lane to meet EVERY clause of the Block 130 antecedent, so THE MOMENTUM-COMPARISON INPUTS BLOCK 123 TARGETS EXIST FOR THE FIRST TIME; but the delivery is INPUTS and NOT the bridge\'s own generators -- the cost-145 charge range is THREE POINTS, so |dTC| <= 1 and |dMC| <= 1 there and the achieved difference set at EVERY distance is {0, +-(1,0), +-(0,1), +-(1,1)}, placing (5,-7) and (1,-7) in the GENERATED LATTICE but NOT in the ACHIEVED SET by any single move or composite at that stratum, while FROM THE FLOOR both ARE achieved by SEPARATOR-CERTIFIED COMPOSITE WITNESSES landing at C4 = 156 and 152, which are UPPER BOUNDS OBTAINED BY DESCENT and are NOT PROVEN MINIMAL, and their NEGATIVES would require (31,67) and (35,67) VIOLATING TC >= 36 and MC <= 60, hence lying OUTSIDE the floor-anchored cone at ANY composite length; whence DOWNSTREAM Block 123\'s momentum-definiteness comparison becomes EXECUTABLE on the stratum-145 move set while BLOCK 123\'s OWN THEOREM IS UNTOUCHED, strata 147 and above are NOT ENUMERATED so the bridge vectors\' fate there is OPEN, no non-naive frame-to-momentum map is built or excluded, the entropy/counting-functional route candidate is NOT BUILT, the cycle-725/726/734 supplied-model firewall is INHERITED UNCHANGED, and the other lane\'s unmerged cycle-778-799 material is NOT READ, NOT CONSUMED and NOT SUPERSEDED\nRESULT: on the committed cost-144 four-cube corpus, the cycle-734 three-piece incidence class on it, the completely enumerated cost-145 and cost-146 strata, and the cycle-726 facet charge at the displayed fixtures, executing Block 150\'s three-piece item from origin/main\'s committed machinery only, THE ACCOUNTING IS CORRECTED (RAISE = 40,512 counts TRIPLES; the REFILLS number 42,240 at local C4 19/20/21 = 27,264/14,592/384) and THE CLASS REDUCED (41,088 of the 42,240 replace only TWO pieces over exactly cycle-734\'s 288 two-piece re-cuts; the irreducible remainder is 1,152 with dC4 in {2,3}, all on 7-corner regions); THE PROMOTION retires cycle 734\'s own caveat -- ALL 42,240 are GENUINE GEOMETRIC RE-CUTS FOR EVERY HOST across 8,893,056 separator-certified instances with ZERO FAILURES, the checker fully re-verifying the local-cost-21 stratum; the class is STRICTLY DIRECTED, every one LEAVING the floor into 145/146/147 at 27,264/14,592/384 with increments {(0,-1) x7104, (0,0) x21024, (1,-1) x7008, (1,0) x7104} in a POINTED quadrant generating Z^2 at index 1, so the obstruction is SIGN and NOT RANK; and that is CORNER-FORCED by THE FLOOR-CORNER THEOREM -- the 180 minimal 3-cube facet dissections on THREE INDEPENDENT ROUTES give tick {18:16, 19:72, 20:84, 21:8} and mixed {8:12, 9:64, 10:104}, so EVERY minimal four-box dissection has TC in [36,42] and MC in [48,60] (the MC = 48 end facet-wise and UNWITNESSED, displayed), and the cost-144 corpus sits at the EXTREME CORNER (36,60) = (TC_min, MC_max), whence NO FLOOR-ANCHORED MOVE CLASS OF ANY SIZE CAN BE SIGN-INDEFINITE and Block 150\'s all-neutral flips and this block\'s one-sided cone are TWO SHADOWS OF ONE CORNER; but CHARGE RIGIDITY IS A FLOOR FACT -- cost 145 is COMPLETE at 243,072, gated 69,888/69,888 by exhibited integer planes and rebuilt by the checker at 730,566,987 nodes, with THREE charge points in 192 blocks of 1,266 whose charge depends on the IDENTITY and not the CHARGE TYPE of the lone C4 = 7 piece, and cost 146 is complete at 2,359,680 with SIX points at INCIDENCE LEVEL ONLY -- and at 145 the three-piece same-class class that cycle 734 proved EMPTY at the floor is POPULATED: 132,288 distance-3 moves, NOT ONE charge-neutral, achieving +-(1,0) and +-(0,1) at 66,144 each with distance 4 adding +-(1,1), a NEGATION-CLOSED set with cone R^2 and lattice Z^2 -- SIGN-INDEFINITE, MUTUALLY REVERSIBLE, SAME COST CLASS -- so BLOCK 123\'s MOMENTUM-COMPARISON INPUTS EXIST FOR THE FIRST TIME, while (5,-7) and (1,-7) remain IN THE LATTICE and NOT IN THE ACHIEVED SET, one-way from the floor at C4 = 156 and 152 (NOT PROVEN MINIMAL) with negatives (31,67)/(35,67) violating the corner: THE COST FLOOR IS THE BOUNDARY BETWEEN CHARGE RIGIDITY AND SIGN-INDEFINITE REVERSIBILITY, and the no-go does NOT survive one cost unit up\nDECISION_CUT: EXECUTE BLOCK 123\'s MOMENTUM-DEFINITENESS COMPARISON ON THE STRATUM-145 MOVE SET -- the first move class in the lane that is sign-indefinite, mutually reversible and same-cost-class, so the comparison the bridge conditional points at is now EXECUTABLE with real inputs, and this block does NOT predict its outcome; ENUMERATE STRATA 147 AND ABOVE for the bridge vectors, since the cost-145 charge range is only three points and caps |dTC| and |dMC| at 1 while the global bracket leaves room for |dTC| up to 6 and |dMC| up to 12, and PROVE OR REFUTE THE MINIMALITY of the separator-certified composite witnesses landing at C4 = 156 and 152, which are upper bounds from descent only; BUILD OR EXCLUDE A NON-NAIVE FRAME-TO-MOMENTUM MAP, still open exactly as Block 130 and Block 150 left it; and LEAVE THE OTHER LANE\'S UNMERGED CYCLE-778-799 MATERIAL to that worker -- their pending state, not read, not consumed, not superseded -- while the entropy/counting-functional route candidate, the paired-degeneracy observable question and the common nilpotent differential remain named and unexecuted; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "class_accounting",
    "promotion",
    "corner_point",
    "corner_forcing",
    "facet_caveat",
    "strata",
    "refinement",
    "move_set",
    "reversible",
    "boundary",
    "upper_bounds",
    "verdict",
    "downstream",
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
        "class_accounting": (
            "42,240" in note or "42240" in compact
            or ("triples" in note and "refills" in note)
        ),
        "promotion": (
            ("promoted" in note or "retiring" in note or "retired" in note)
            and (
                "8,893,056" in note or "8893056" in compact
                or "zero failures" in note
            )
        ),
        "corner_point": "corner" in note
        and ("(36, 60)" in note or ("36" in note and "60" in note)),
        "corner_forcing": "no floor-anchored" in note
        or "sign-indefinite" in note,
        "facet_caveat": "facet-wise" in note or "not witnessed" in note,
        "strata": "floor fact" in note or "three charge points" in note,
        "refinement": ("identity" in note and "not" in note)
        or "not of its charge type" in note
        or "not a function of the charge type" in note,
        "move_set": "132,288" in note or "132288" in compact
        or "negation-closed" in note,
        "reversible": "mutually reversible" in note or "same cost class" in note,
        "boundary": "achieved set" in note or "not achieved" in note,
        "upper_bounds": "upper bounds" in note or "not proven minimal" in note,
        "verdict": "the cost floor" in note and "boundary" in note,
        "downstream": "executable" in note
        and ("block 123" in note or "momentum" in note),
        "pickup_provenance": "pickup" in note,
        "not_consumed_rider": "778" in note or "not consumed" in note,
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
        "alternates_total": ALTERNATES,
        "reduction_pairs": TWO_PIECE_PAIRS,
        "tick_spectrum": TICK_SPECTRUM,
        "quadrant_intersection": QUADRANT_INTERSECTION,
        "promotion_failures": PROMOTION_FAILURES,
        "c21_instances": C21_INSTANCES,
        "charge_is_type_function": False,
        "charge_points_145": CHARGE_POINTS_145,
        "neutral_at_distance_three": False,
        "achieved_145": ACHIEVED_145,
        "bridge_in_achieved": tuple(
            (generator, False) for generator in BRIDGE_DELTAS
        ),
        "negatives_admissible": tuple(
            (point, False) for point in NEGATIVE_TARGETS
        ),
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "wrong_refill_count":
        claims["alternates_total"] = ALTERNATES - 1
    elif mutation == "break_reduction_match":
        claims["reduction_pairs"] = TWO_PIECE_PAIRS - 1
    elif mutation == "wrong_three_cube_spectrum":
        claims["tick_spectrum"] = ((17, 16), (19, 72), (20, 84), (21, 8))
    elif mutation == "break_corner_inference":
        claims["quadrant_intersection"] = ((0, 0), (1, 0))
    elif mutation == "claim_promotion_failure":
        claims["promotion_failures"] = 1
    elif mutation == "wrong_stratum_count":
        claims["c21_instances"] = C21_INSTANCES - 1
    elif mutation == "claim_charge_type_dependence":
        claims["charge_is_type_function"] = True
    elif mutation == "wrong_charge_points":
        claims["charge_points_145"] = (
            ((36, 59), 60768), ((36, 60), 121536), ((37, 59), 60768)
        )
    elif mutation == "claim_neutral_distance_three":
        claims["neutral_at_distance_three"] = True
    elif mutation == "wrong_achieved_set":
        claims["achieved_145"] = ((-1, 0), (0, -1), (0, 1), (1, 0))
    elif mutation == "claim_bridge_vectors_achieved":
        claims["bridge_in_achieved"] = tuple(
            (generator, True) for generator in BRIDGE_DELTAS
        )
    elif mutation == "claim_reverses_exist":
        claims["negatives_admissible"] = tuple(
            (point, True) for point in NEGATIVE_TARGETS
        )
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_LANE_FLIP_ENUMERATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_joint_lane_flip_enumeration_2026_08_20.py",
            # the three origin/main-only cell-cutting runners are
            # content-bound via the gate-A blob pins, not audit paths
        )
        and PARENT_ARTIFACTS == (BLOCK150_NOTE, BLOCK150_RUNNER)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # the three cell-cutting runners, bound BY CONTENT and by shape
        and authority.machinery_content_bound
        and tuple(
            name for name, _recorded, _digest, _pin in authority.machinery_blobs
        )
        == ("c726", "c734", "c811")
        and facts.machinery == MACHINERY_SHAPE
        and facts.machinery_exit
        == (0, C726_GATES, 0, (C734_PREFIX_GATES, 0))
    )

    gate_b = bool(
        facts.corner_orders_agree
        and facts.piece_lists_agree
        and facts.volume_spectrum == ((0, 1360), (1, 2672), (2, 320), (3, 16))
        and facts.cost_spectrum
        == ((6, 400), (7, 1216), (8, 864), (9, 192))
        and sum(count for _cost, count in facts.cost_spectrum) == PIECES
        and facts.exact_inverses_agree
        and facts.separation_agrees[0] == facts.separation_agrees[1]
        and facts.separation_agrees[0] > 2000
        and facts.corpus == (CORPUS, CORPUS)
        and facts.pool_pieces == POOL_PIECES
        and facts.floor_forcing
        and facts.corpus_charge_points == ((CORPUS_CHARGE, CORPUS),)
        and facts.independent_corpus
        == (CORPUS, PIECE_COST_FLOOR, FLOOR_PIECES, True, True)
        # the committed cycle-734 gate `three.none`, run inside the prefix
        and facts.committed_class
        == (
            CLIQUES, SPURIOUS, GENUINE_TRIPLES, KEEP_TRIPLES, RAISE_TRIPLES,
            LOCAL_COST_SPECTRUM,
        )
        and facts.own_clique_census == (CLIQUES, SPURIOUS, GENUINE_TRIPLES)
        and facts.committed_two_piece
        == (TWO_PIECE_PAIRS, ((1, 192), (2, 96)), TWO_PIECE_PAIRS)
        # the reduction: 41,088 refills replace a committed two-piece re-cut
        and facts.reducible
        == (
            REDUCIBLE,
            claims["reduction_pairs"],
            claims["reduction_pairs"],
            True,
        )
        and facts.reducible_dc4 == REDUCIBLE_DC4
        and facts.reduction_sample
        == (REDUCTION_SAMPLE, REDUCTION_SAMPLE, REDUCTION_SAMPLE)
        and facts.deep_reduction
        in ((0, 0, 0), (GENUINE_TRIPLES,) * 3)
        # the irreducible remainder, found on the minimum hulls and CLOSED
        # against the committed total
        and facts.hull_census[0][0][0] == HULL_MIN_CORNERS
        and facts.hull_census[1] == HULL7_TRIPLES
        and facts.hull_census[2] == HULL7_ALTERNATES
        and sum(count for _size, count in facts.hull_census[0])
        == GENUINE_TRIPLES
        and facts.irreducible == IRREDUCIBLE
        and facts.irreducible_dc4 == IRREDUCIBLE_DC4
        and REDUCIBLE + IRREDUCIBLE == ALTERNATES
        and facts.alternates_total == claims["alternates_total"]
        and facts.alternates_total
        == sum(count for _cost, count in facts.committed_class[5])
        and facts.local_cost_spectrum == LOCAL_COST_SPECTRUM
        and facts.class_deltas == CLASS_DELTAS
        and facts.class_joint == CLASS_JOINT
        and facts.landing_strata == LANDING_STRATA
        and FLOOR_CLASS not in tuple(
            cost for cost, _count in facts.landing_strata
        )
        and facts.class_cone_pointed
    )

    gate_c = bool(
        facts.own_three_cube
        == (
            CUBE_VOLUME_SPECTRUM,
            CUBE_CELLS,
            FACET_DISSECTIONS,
            (FACET_TETS,),
            claims["tick_spectrum"],
            MIXED_SPECTRUM,
            (MIXED_SPECTRUM, MIXED_SPECTRUM),
        )
        and facts.tick_box == TICK_BOX
        and facts.mixed_box == MIXED_BOX
        and facts.corner == CORNER
        # the corner IS the constant charge Block 150 measured, re-measured
        # here on the same committed corpus rather than imported as a number
        and facts.corner == CORPUS_CHARGE
        and facts.corpus_charge_points == ((CORNER, CORPUS),)
        # the TC ceiling IS witnessed by a genuine dissection ...
        and facts.tc_ceiling_witness
        == (
            CUTTING_SIZE,
            True,
            276,
            276,
            TC_CEILING_WITNESS_CHARGE[0],
            TC_CEILING_WITNESS_CHARGE[1],
            TC_CEILING_WITNESS_COST,
        )
        # ... and the MC floor is NOT: 48 is a facet-wise bound only
        and not facts.mc_floor_witnessed
        and MC_FLOOR_UNWITNESSED == MIXED_BOX[0]
        # the forcing inference, computed rather than argued
        and facts.corner_forces_class
        and facts.quadrant_intersection == claims["quadrant_intersection"]
    )

    gate_d = bool(
        facts.promotion_instances == PROMOTION_INSTANCES
        and facts.promotion_c21 == (claims["c21_instances"], C21_INSTANCES)
        and len(facts.promotion_samples) == 2
        and tuple(row[0] for row in facts.promotion_samples) == (19, 20)
        and all(row[1] == row[2] and row[2] > 0 for row in facts.promotion_samples)
        and facts.promotion_failures == claims["promotion_failures"]
        and facts.deep_promotion
        in ((0, 0), (PROMOTION_INSTANCES, PROMOTION_INSTANCES))
    )

    gate_e = bool(
        facts.blocks_145 == (BLOCKS_145, (BLOCK_SIZE_145,))
        and facts.block_charge_constant
        and facts.corpus_145 == CORPUS_145
        and BLOCKS_145 * BLOCK_SIZE_145 == CORPUS_145
        and facts.charge_points_145 == tuple(claims["charge_points_145"])
        and facts.blocks_per_charge_145 == BLOCKS_PER_CHARGE_145
        and facts.cooccurring_145 == (COOCCURRING_145, COOCCURRING_145)
        and facts.charge_is_type_function == bool(claims["charge_is_type_function"])
        and facts.refinement_witness[0]
        == ((REFINEMENT_TYPE, REFINEMENT_CHARGES),)
        and len(facts.refinement_witness[1]) == 2
        and tuple(point for _piece, point in facts.refinement_witness[1])
        == REFINEMENT_CHARGES
    )

    gate_f = bool(
        facts.masks_distinct
        and facts.distance2_spectrum == DISTANCE2_SPECTRUM
        and 0 not in tuple(delta for delta, _count in facts.distance2_spectrum)
        and facts.within_block_min == WITHIN_BLOCK_MIN
        and facts.min_cross_distance == MIN_CROSS_DISTANCE
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
        and facts.neutral_at_distance_three
        == bool(claims["neutral_at_distance_three"])
        and facts.achieved_145 == tuple(claims["achieved_145"])
        and facts.achieved_negation_closed
        and not facts.achieved_cone_pointed
        and facts.achieved_index == ACHIEVED_LATTICE_INDEX
        and facts.deep_move_scan
        in ((0, 0, ()), (D3_MOVES, 0, D3_DIRECTED))
    )

    gate_g = bool(
        facts.achieved_differences == ACHIEVED_DIFFERENCES
        and facts.bridge_in_lattice
        == tuple((generator, True) for generator in BRIDGE_DELTAS)
        and facts.bridge_in_achieved == tuple(claims["bridge_in_achieved"])
        and facts.negatives_admissible == tuple(claims["negatives_admissible"])
        and facts.composite_bounds == COMPOSITE_BOUNDS
        and facts.bridge_witnesses
        == (
            (
                BRIDGE_TARGETS[0], CUTTING_SIZE, True, 276, 276,
                BRIDGE_TARGETS[0][0], BRIDGE_TARGETS[0][1],
                BRIDGE_WITNESS_41_53_COST,
            ),
            (
                BRIDGE_TARGETS[1], CUTTING_SIZE, True, 276, 276,
                BRIDGE_TARGETS[1][0], BRIDGE_TARGETS[1][1],
                BRIDGE_WITNESS_37_53_COST,
            ),
        )
        # the witnesses are EXISTENCE certificates at cost 169 and 166; the
        # composite bounds 156 and 152 are upper bounds only, and neither is
        # claimed minimal
        and all(
            cost > bound
            for (_generator, _steps, bound), (_point, _n, _ok, _s, _t, _tc, _mc, cost)
            in zip(facts.composite_bounds, facts.bridge_witnesses)
        )
        and facts.bridge_lattice == (BRIDGE_INDEX, 1, True)
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
            "also run the FULL versions of the three sampled certificates: the "
            "exhaustive three-piece refill census over all 636,032 triples, the "
            "geometric promotion of all 42,240 refills over every host, and the "
            "complete region-first distance-3 scan of the cost-145 stratum"
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
        "main plus the committed Block 150 note and runner are content-bound at the parent pin, and the three cell-cutting runners this block reasons with are read from origin/main AT RUN TIME under blob pins checked against the hash of the bytes actually imported, with their pinned cut markers and their own gate tallies recorded (cycle 726: 32/0 and exit 0; cycle 734 prefix, cut DEEPER than Block 150's so that the three-piece incidence gate runs inside it: 22/0)",
        gate_values["A"],
    )
    checks.check(
        "B-class-accounting",
        "the committed cycle-734 gate `three.none` runs inside the imported prefix and reports 649,600 cliques, 13,568 spurious, 636,032 genuine triples, KEEP = 0 and RAISE = 40,512 triples whose 42,240 refills cost 19/20/21 at 27,264/14,592/384; the clique census is reproduced here independently, and the class is then SPLIT exactly: 41,088 refills replace a committed two-piece re-cut with a spectator, over exactly 288 distinct removed pairs each sharing four corners, at dC4 1 x 27,264 and 2 x 13,824, while the remaining 1,152 are irreducible with dC4 2 x 768 and 3 x 384, found by exhaustive search on the 576 minimum seven-corner hulls and CLOSED against the committed total, 41,088 + 1,152 = 42,240; the achieved increments are {(0,-1) x 7104, (0,0) x 21024, (1,-1) x 7008, (1,0) x 7104}, the cone is pointed, every refill LEAVES the floor into strata 145/146/147, and a 400-triple sample re-runs the exhaustive refill search under BOTH this runner's corner-hull enumerator and the committed cycle-734 `refills`, agreeing set for set and matching the split exactly (--deep does all 636,032)",
        gate_values["B"],
    )
    checks.check(
        "C-floor-corner-theorem",
        "the induced three-cube facet problem is re-enumerated here by a POINT-FREE route -- six-cliques of the exact interior-disjointness graph on the 56 unimodular cells, each edge an exhibited integer separating plane, no sample lattice anywhere -- giving 180 dissections of six cells with tick spectrum {18,19,20,21} and mixed spectrum {8,9,10} on all three two-axis choices, hence the facet-wise box TC in [36,42] and MC in [48,60]; the cost-144 corpus sits at the CORNER (36,60) = (TC_min, MC_max), the TC ceiling 42 is WITNESSED by a re-certified genuine dissection at cost 165 while the MC floor 48 is NOT witnessed by any dissection this runner holds and is carried as a facet-wise bound only; and the forcing is computed, not argued: every class increment keeps TC >= 36 and MC <= 60, and the nonnegative cone on those increments meets its own negation in {(0,0)} alone, so NO floor-anchored move class of any size can be sign-indefinite",
        gate_values["C"],
    )
    checks.check(
        "D-promotion",
        "cycle 734 left the three-piece class as INCIDENCE candidates; here all 8,893,056 (triple, host, refill) instances are counted and the promotion to genuine geometric re-cuts is certified with ZERO failures -- the entire local-cost-21 stratum in full, 293,376 instances, plus deterministic 200-refill samples of the 19 and 20 strata, each certified once against the union of every host's complement so that one check covers every host -- and --deep certifies all 42,240 refills over all 8,893,056 instances",
        gate_values["D"],
    )
    checks.check(
        "E-cost-145-landscape",
        "the cost-145 stratum is rebuilt COMPLETELY by its own block decomposition -- one cost-7 piece plus 23 floor pieces, the 192 block indices read off the class's own dC4 = 1 refills -- giving 192 blocks of exactly 1,266 and 243,072 cuttings, all 69,888 co-occurring pairs separated by exhibited integer planes; the facet charge is CONSTANT on every block and takes exactly three values across them, (36,59) x 60,768, (36,60) x 121,536 and (37,60) x 60,768 over 48/96/48 blocks, so the Block 150 rigidity is a FLOOR fact and not a lane fact; and the charge is a function of the non-floor piece's IDENTITY and NOT of its charge type, which is exhibited rather than asserted: two blocks whose non-floor piece has the same (TC, MC) = (0, 2) carry the different charges (36,59) and (36,60)",
        gate_values["E"],
    )
    checks.check(
        "F-sign-indefinite-moves",
        "at cost 145 the short moves are excluded structurally -- all 2,672 piece point-masks are distinct so no distance-1 move exists at all, and the two-piece alternates over all 69,888 co-occurring pairs of the stratum have dC4 in {-1, 1, 2} and NEVER 0 -- while no charge-neutral move is shorter than distance 4, within a block or across blocks of equal charge; a COMPLETE sub-scan over twelve blocks, four at each charge point, gives minimum cross-charge distances 3, 4, 3 and realises +-(1,0) and +-(0,1) at distance three and +-(1,1) at distance four, so EVERY distance-3 same-class move changes the charge, the exact inversion of the floor; the achieved set is negation-closed, its cone is R^2 rather than pointed, and it generates Z^2 at index 1; the full scan, 132,288 distance-3 moves with 66,144 in each direction and not one charge-neutral, is carried as a twice-verified constant and re-run under --deep",
        gate_values["F"],
    )
    checks.check(
        "G-bridge-boundary",
        "the cost-145 charge range is three points, so the achieved DIFFERENCE set there is exactly {0, +-(1,0), +-(0,1), +-(1,1)} and the Block 130 generators (5,-7) and (1,-7) lie in the generated lattice Z^2 -- whose bridge counterpart L = {7x + y = 0 mod 28} is re-derived here from the witness differences as the gcd 28 of the 2x2 minors, with the congruence verified over a full period box -- but NOT in the achieved set; their negatives are excluded from every floor-anchored composite outright, since they would need charge (31,67) and (35,67) against TC >= 36 and MC <= 60; composites of the class's own increments reach the two targets at four-column cost 156 and 152 by an exact integer minimum-cost program, carried as UPPER BOUNDS ONLY with neither minimality nor chainability proved; and the two target charges are shown NON-EMPTY by re-certified genuine dissections at (41,53) and (37,53), which sit at cost 169 and 166, strictly above both bounds",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the class accounting with its refill count and its reduction, the promotion with its zero failures, the floor-corner theorem with its (36,60) corner, its no-floor-anchored-sign-indefinite forcing and its facet-wise caveat, the three-charge-point strata fact with the identity-not-type refinement, the negation-closed move set with its mutual reversibility inside one cost class, the boundary with its unachieved bridge vectors and its upper-bound-only composites, the cost-floor verdict, the executable downstream for Block 123, the pickup provenance, the not-consumed rider, the cross-context disclosure, the firewalls and the exact N5 fence are present",
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
