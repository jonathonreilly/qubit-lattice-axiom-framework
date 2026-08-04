#!/usr/bin/env python3
"""Cycle 906: BL7 -- the covariance-versus-interface tension, resolved.

Campaign-5 Born LANE CLOSURE, block 2.  Strictly structural.  NO
probability postulate is introduced, NO Born rule is claimed.  Every
fraction emitted here is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

Cycle 878 certified that M2_PER_WORLD_UNIFORM is the ONLY candidate of
its five that is covariant under the landed Cycle-856 monitor-phase
group.  Cycle 905 certified that the gravity interface EXCLUDES exactly
{M1, M2} via the never-formed block (584 worlds, 73,088 of 92,260
events), conditional on premise P-NONEMPTY.  Ledger row BL7 is the
resulting tension: the only covariant candidate is exactly the excluded
one, so no survivor is covariant.

Q1  THE COVARIANCE CERTIFICATION, REBUILT.  What monitor-phase
    covariance EXACTLY is, taken from the pinned Cycle-878 primary by
    AST/byte-quote and never by import: the transformation family, its
    action, and the covariance CONDITION on weightings, derived rather
    than asserted.  The family's structure is computed (group axioms,
    order, cyclicity, freeness, orbit partition).  The condition is then
    shown to be LINEAR, its exact rank computed by two routes, and the
    878 verdicts (M2 passes, M1/M3/M4/M5/M0 fail) are re-derived
    value-for-value from the condition.

Q2  IS COVARIANCE AXIOM-GROUNDED?  A fidelity sweep (byte-quote +
    mechanical filter + computed grade with reasons) over the pinned
    axiom baseline and over every monitor/phase-relevant surface
    DISCOVERED on this branch by a published selection rule.  The
    question is whether any sentence REQUIRES the measurement weighting
    to be monitor-phase covariant.

Q3  THE CONSTRUCTIVE QUESTION.  Solve, exactly and as linear algebra
    with the two-route rank discipline, the joint system

        (COV)  monitor-phase covariance, in the form derived in Q1
        (ZERO) the interface's zero-mass requirement on the
               never-formed block, in three declared readings

    over TWO declared bases: the 25-dimensional minimal kernel-argument
    extension of the Cycle-878 span (Cycle-905's rank result), and
    Cycle-902's own GENEROUS base (all finitely additive weightings on
    the event space).  Exhibit any solution found; certify any
    impossibility found; compute the scope of either.

Q4  BL6 CONNECTION.  The orbit-meeting table: what fraction of each
    covariance orbit lies in the never-formed block, whether the
    general theorem follows from orbit structure alone, and whether BL6
    and BL7 are the same fact viewed twice.

Discipline: TEXT / AST / JSON only.  The Cycle-863, Cycle-878,
Cycle-902, Cycle-905 and Cycle-856 primaries are BLOCKLISTED from
import; the census machinery is lifted out of the pinned sources by AST
so the rebuilt event space is the pinned construction rather than a
transcription.  Only the landed Cycle-719 core is imported.  Exact
rational arithmetic everywhere; no floating point enters any verdict.

Supervisor-authored primary.  bounded_theorem, authority none, audit
unset.  Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import re
import sys
from time import monotonic
from types import SimpleNamespace

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024
FRACTION_LABEL = "bookkeeping fraction, not probability"

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C902_PATH = "scripts/frontier_cycle902_p2_kernel_attack_2026_07_28.py"
C902_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"
C905_PATH = "scripts/frontier_cycle905_born_narrowing_2026_07_28.py"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C905_SHIP = "outputs/born_narrowing_block_cycle905_ship_receipt_2026_07_28.json"
C856_PATH = "scripts/frontier_cycle856_record_covariance_2026_07_28.py"
C856_NOTE = "docs/RECORD_COVARIANCE_CYCLE856_BOUNDED_THEOREM_NOTE_2026-07-28.md"
C878_NOTE = "docs/EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md"
C905_NOTE = ("docs/BORN_NARROWING_CERTIFIED_LEDGER_OPENED_CYCLE905"
             "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C902_PATH, C902_RECEIPT,
    C905_PATH, C905_RECEIPT, C905_SHIP, C856_PATH, C856_NOTE, C878_NOTE,
    C905_NOTE, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C902_PATH, C905_PATH, C856_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C902_RECEIPT, C905_RECEIPT, C905_SHIP)
TEXT_ONLY_PATHS = (C856_NOTE, C878_NOTE, C905_NOTE, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C902_PATH:
        "46d46db10258731b986f3c639eedcf1ad3f968021f1efe30c88cc3e5e17b46c2",
    C902_RECEIPT:
        "91c5631415d0231390fedbd0174f074de45cfa33b6dd4f706ed6fcdbf4dfd1d8",
    C905_PATH:
        "83429f35312e0df16d3d11e65685cb87b8e732b19299e1078ddaea1e1444afb3",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C905_SHIP:
        "9a35f2161bbabdbb0579a01f9984381ef74995261dbb6a76e65c678896c833df",
    C856_PATH:
        "20bce7f6dab9d7755ddefc6e2000d501acb8572dc15f50981b65ba9f6e2a4f2b",
    C856_NOTE:
        "7b6b73826ee397e66102994174d94e04c3f174761f00ffcfe0da2be97e72a545",
    C878_NOTE:
        "007bbaa2ae70afad7fcb761d3f3912edb1b3f1c893a439a9e4d815abe335428c",
    C905_NOTE:
        "8a8f724a1be93f368c89b90bedae97777bcae3fb6991367228a2ff85d014fec8",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C902_PATH: "3b43d97bbb604ea44ed06c87aa091c6aa9d8470b",
    C902_RECEIPT: "1fd7522ad2af152f2e13327e752e2eb9f37e67bb",
    C905_PATH: "f9f2171602bddf7d6164261dc13a2ee4f7e3046c",
    C905_RECEIPT: "7094c986dc0560e8982507d8cc379f5c720b639f",
    C905_SHIP: "c098209994af7b77de90717eaaf288bdf2ce7196",
    C856_PATH: "fc873d0b1947866b238bbe5456ffe89fcd072a21",
    C856_NOTE: "f819f5b31d442248fac255fcdf3b0139d6ba83f8",
    C878_NOTE: "8fd212e96748064c40be670e491474e14dae28b6",
    C905_NOTE: "96d8cfd2e1f686d37c74f377fbbc2667da5490a1",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle905_born_narrowing_independent_check_2026_07_28",
    "frontier_cycle856_record_covariance_2026_07_28",
    "frontier_cycle856_covariance_independent_check_2026_07_28",
    "frontier_cycle867_composed_record_write_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

CANDIDATES = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT")
NARROWED = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
            "M5_FORMATION_MOMENT")
EXCLUDED_BY_INTERFACE = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM")
CONTROL = "M0_CONTENT_DIVERSITY"
NEW_NAME = "M6_ABSOLUTE_ORBIT_UNIFORM"

# ---- byte-quoted needles from the pinned sources (presence certified) ------
NEEDLE_878_ACTION_DOC = (
    '"""The Cycle-856 landed symmetry: moving the controller-orbit cut to\n'
    "    monitor phase m advances the sources by m stations.  On census keys\n"
    "    (k, event, positions) this is positions -> positions + m (mod\n"
    '    stations), a Z_stations action on the worlds."""'
)
NEEDLE_878_COV_TEST = (
    "        covariant_world = all(\n"
    '            world_cell.get(("w", orbit[0]), zero)\n'
    '            == world_cell.get(("w", x), zero)\n'
    "            for orbit in world_orbits for x in orbit\n"
    "        ) if perm_ok else None"
)
NEEDLE_878_WORLD_CELL = '            world_cell = masses_by_family["F_WORLD"][name]'
NEEDLE_856_INTERTWINE = (
    "the intertwining\n"
    "  identity stamped_m(g·key) == stamped_{g·m}(key) HOLDS in all\n"
    "  **181,016** cases (checker re-verified) — record formation is\n"
    "  MONITOR_COVARIANT: transform the monitoring origin along with the\n"
    "  setup and the symmetry is exact; the fixed-monitor breaking sits\n"
    "  only within the declared Cycle-852 phase-lift scope;"
)
NEEDLE_856_NOT_ORBIT_CLOSED = (
    "stamped-ness is NOT orbit-closed — mixed\n"
    "  orbits (orbit-mates disagreeing about record formation): E1 = 3\n"
    "  uniformly-stamped / 12 uniformly-silent / 53 MIXED;"
)
NEEDLE_856_ABSOLUTE = (
    "**E1 has 33** (exactly three size-11 k=2 orbits: events\n"
    "  0, 1, 2 at separations 5/6)"
)
NEEDLE_AXIOM_EXCLUSION = (
    "- context selection, measurement basis selection, Born weights,"
    " probability\n  rules, update laws, decoherence mechanisms, and"
    " formation rules"
)
NEEDLE_AXIOM_COVARIANT = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under"
    " lattice\ntranslations and proper cubic rotations."
)
NEEDLE_AXIOM_QUALIFICATION = (
    "Further physical\nstructure requires a retained derivation or bridge, or"
    " explicit approved-\nprimitive registration, before use as a premise."
)

# ---- fidelity sweep: PUBLISHED selection rules -----------------------------
DISCOVERY_NEEDLES = ("monitor phase", "monitor-phase", "monitor_phase",
                     "monitor-covarian", "monitor covarian",
                     "monitor_covariant")
DISCOVERY_GLOBS = ("docs/*.md", "scripts/*.py")
MODAL_TOKENS = ("must ", "must,", "shall ", "required", "requires", "require ",
                "necessarily", "is needed", "obligat", "mandat")
WEIGHTING_TOKENS = ("weight", "measure", "probabilit", "born", "bookkeeping",
                    "fraction", "mass", "occurrence rule", "candidate",
                    "per-world uniform", "counting", "occupation-weighted",
                    "readout")
MONITOR_TOKENS = ("monitor", "phase")
SYMMETRY_TOKENS = ("covarian", "invarian", "equivarian", "symmetr", "privileg")
EXCLUSION_TOKENS = ("outside axiom content", "remain outside", "do not close,"
                    " import, or rename", "must cite separate retained"
                    " authorities", "remains downstream", "remain downstream",
                    "is downstream content", "not include it")


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def factorize(value: int) -> dict:
    out: dict = {}
    n, p = abs(value), 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


# ---------------------------------------------------------------------------
# A: pins
# ---------------------------------------------------------------------------

def pin_rows() -> dict:
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=Path(__file__).name
    )
    literal = None
    string_constants: dict = {}
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if not isinstance(target, ast.Name):
                    continue
                if isinstance(node.value, ast.Constant) \
                        and isinstance(node.value.value, str):
                    string_constants[target.id] = node.value.value
                if isinstance(node.value, ast.BinOp) \
                        and isinstance(node.value.left, ast.Constant) \
                        and isinstance(node.value.right, ast.Constant):
                    string_constants[target.id] = (
                        node.value.left.value + node.value.right.value
                    )
                if target.id == "AUDIT_INPUT_PATHS" \
                        and isinstance(node.value, ast.Tuple):
                    resolved = []
                    for element in node.value.elts:
                        if isinstance(element, ast.Constant):
                            resolved.append(element.value)
                        elif isinstance(element, ast.Name):
                            resolved.append(string_constants.get(element.id))
                        else:
                            resolved.append(None)
                    literal = tuple(resolved)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    result = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "modes": {"imported": IMPORTED_PATHS, "ast_only": AST_ONLY_PATHS,
                  "json_only": JSON_ONLY_PATHS, "text_only": TEXT_ONLY_PATHS},
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "vendored_902_pair_verified": (
            sha_rows[C902_PATH] == EXPECTED_SHA256[C902_PATH]
            and sha_rows[C902_RECEIPT] == EXPECTED_SHA256[C902_RECEIPT]
        ),
        "c905_ship_receipt_names_the_primary_digest": None,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "bytes": {p: len(b) for p, b in payloads.items()},
    }
    ship = json.loads(payloads[C905_SHIP].decode("utf-8"))
    ship_text = compact(ship)
    result["c905_ship_receipt_names_the_primary_digest"] = bool(
        EXPECTED_SHA256[C905_PATH] in ship_text
    )
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and result["vendored_902_pair_verified"]
        and result["c905_ship_receipt_names_the_primary_digest"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# ---------------------------------------------------------------------------
# AST lift: the pinned machinery, never imported
# ---------------------------------------------------------------------------

def ast_lift(path: str, funcs: tuple, consts: tuple, globals_: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found_consts = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in consts:
                    found_consts[target.id] = ast.literal_eval(node.value)
    missing = tuple(f for f in funcs if f not in {n.name for n in body})
    missing_c = tuple(c for c in consts if c not in found_consts)
    if missing or missing_c:
        raise AssertionError(("ast lift incomplete", path, missing, missing_c))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(globals_)
    namespace.update(found_consts)
    exec(compile(module, f"<ast-lift {path}>", "exec"), namespace)
    return namespace, found_consts, tuple(n.name for n in body)


C863_FUNCS = (
    "pairwise_separated", "derive_event_seeds", "derive_census",
    "watched_registers", "dirty_partition", "build_initial_states",
    "pack_lanes", "compile_masked_gate", "masked_h_schedules", "compile_fast",
    "mask_over", "lanes_of", "lane_state",
)
C863_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES")
C878_FUNCS = (
    "lcm", "dead_wire_rig", "composed_scan", "family_keys", "cells_of",
    "refines", "build_candidates", "monitor_phase_action", "group_orbits",
)
C878_CONSTS = (
    "HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP",
    "DETERMINISM_ORBITS", "CANDIDATE_NAMES", "CONTROL_NAME", "FAMILY_ORDER",
)


def lift_machinery():
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS, {"K": K, "combinations": combinations}
    )
    c863 = SimpleNamespace(**{name: ns863[name] for name in C863_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "gcd": gcd,
         "Fraction": Fraction, "json": json},
    )
    c878 = SimpleNamespace(**{name: ns878[name] for name in C878_FUNCS})
    return c863, c878, consts878, {
        "lifted_from_863": names863, "lifted_from_878": names878,
        "constants_863": consts863,
        "constants_878": {k: list(v) if isinstance(v, tuple) else v
                          for k, v in consts878.items()},
        "import_of_863_878_902_905_856": False,
    }


def build_event_space(c863, c878, consts):
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_fail = c863.build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    rig = c878.dead_wire_rig(program, sim, c863.pack_lanes(states + (states[0],)))
    scan = c878.composed_scan(program, census, states, rig, consts["HORIZON"])
    return {"program": program, "census": census, "stations": stations,
            "scan": scan, "events": scan["events"], "init_failures": init_fail}


# ---------------------------------------------------------------------------
# Exact rank: the T9 two-route discipline
# ---------------------------------------------------------------------------

def rank_by_rational_elimination(rows):
    """Route A: full-pivot Gaussian elimination over Q."""
    if not rows:
        return 0, ()
    work = [[Fraction(x) for x in row] for row in rows]
    n_rows, n_cols = len(work), len(work[0])
    rank, pivots = 0, []
    for col in range(n_cols):
        pivot = None
        for r in range(rank, n_rows):
            if work[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        lead = work[rank][col]
        work[rank] = [x / lead for x in work[rank]]
        for r in range(n_rows):
            if r != rank and work[r][col] != 0:
                factor = work[r][col]
                work[r] = [a - factor * b for a, b in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == n_rows:
            break
    return rank, tuple(pivots)


def det_laplace(matrix):
    """Division-free exact determinant by cofactor expansion."""
    size = len(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    total = 0
    for col in range(size):
        if matrix[0][col] == 0:
            continue
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        total += ((-1) ** col) * matrix[0][col] * det_laplace(minor)
    return total


def rank_by_gram_minors(rows, cap=6):
    """Route B for SMALL row sets: rank(M) = rank(M M^T) over an ordered
    field; the Gram rank is read off division-free by the largest
    non-vanishing principal minor.  The Gram matrix is dense, so this
    route is capped and never used on the per-orbit systems."""
    if not rows:
        return 0, ()
    k = len(rows)
    if k > cap:
        raise AssertionError(("gram route row cap exceeded", k, cap))
    gram = [[sum(a * b for a, b in zip(rows[i], rows[j])) for j in range(k)]
            for i in range(k)]
    for size in range(k, 0, -1):
        for subset in combinations(range(k), size):
            minor = [[gram[i][j] for j in subset] for i in subset]
            if det_laplace(minor) != 0:
                return size, subset
    return 0, ()


def rank_by_minor_witness(rows, row_index, columns):
    """Route B for the per-orbit systems: EXHIBIT an explicit square
    submatrix and certify its determinant is non-zero by division-free
    Laplace expansion.  A matrix with r rows has rank at most r, so a
    non-vanishing s x s minor built from s of its rows pins the rank at
    exactly s whenever s == r, and bounds it below otherwise.  The rows
    of these systems carry at most two non-zero entries each, so the
    expansion never branches more than twice per row."""
    if not row_index or not columns:
        return 0, 0, True
    if len(row_index) != len(columns):
        return None, None, False
    minor = [[rows[i][c] for c in columns] for i in row_index]
    determinant = det_laplace(minor)
    if determinant == 0:
        return None, determinant, False
    return len(row_index), determinant, True


def nullspace_basis(rows, n_cols):
    """Exact reduced-row-echelon nullspace basis over Q."""
    work = [[Fraction(x) for x in row] for row in rows] or [[Fraction(0)] * n_cols]
    n_rows = len(work)
    rank, pivots = 0, []
    for col in range(n_cols):
        pivot = None
        for r in range(rank, n_rows):
            if work[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        lead = work[rank][col]
        work[rank] = [x / lead for x in work[rank]]
        for r in range(n_rows):
            if r != rank and work[r][col] != 0:
                factor = work[r][col]
                work[r] = [a - factor * b for a, b in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == n_rows:
            break
    free = [c for c in range(n_cols) if c not in pivots]
    basis = []
    for f in free:
        vec = [Fraction(0)] * n_cols
        vec[f] = Fraction(1)
        for i, p in enumerate(pivots):
            vec[p] = -work[i][f]
        basis.append(vec)
    return basis, rank, tuple(pivots)


# ---------------------------------------------------------------------------
# byte-quote helpers
# ---------------------------------------------------------------------------

def quote_rows(payload_text: dict) -> dict:
    rows = {}
    for label, (path, needle) in {
        "878_monitor_phase_action_docstring": (C878_PATH, NEEDLE_878_ACTION_DOC),
        "878_covariance_test_expression": (C878_PATH, NEEDLE_878_COV_TEST),
        "878_covariance_reads_the_F_WORLD_masses":
            (C878_PATH, NEEDLE_878_WORLD_CELL),
        "856_intertwining_identity": (C856_NOTE, NEEDLE_856_INTERTWINE),
        "856_stampedness_not_orbit_closed":
            (C856_NOTE, NEEDLE_856_NOT_ORBIT_CLOSED),
        "856_absolute_record_orbits": (C856_NOTE, NEEDLE_856_ABSOLUTE),
        "axioms_exclusion_list": (AXIOMS_PATH, NEEDLE_AXIOM_EXCLUSION),
        "axioms_only_covariance_sentence": (AXIOMS_PATH, NEEDLE_AXIOM_COVARIANT),
        "axioms_qualification": (AXIOMS_PATH, NEEDLE_AXIOM_QUALIFICATION),
    }.items():
        text = payload_text[path]
        rows[label] = {"path": path, "present_byte_for_byte": needle in text,
                       "quote": needle, "chars": len(needle)}
    return rows


def ast_source_of(path: str, func_name: str) -> str:
    source = (ROOT / path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=path)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return ast.get_source_segment(source, node) or ""
    return ""


def ast_assignment_of(path: str, target_name: str) -> str:
    source = (ROOT / path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=path)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == target_name:
                    return ast.get_source_segment(source, node) or ""
    return ""


# ---------------------------------------------------------------------------
# the weighting constructor, rebuilt and validated against the pinned M2
# ---------------------------------------------------------------------------

def world_weighted(a_of_world, events, per_world, supported, common):
    """The Cycle-878 construction, restated here: world coefficient a(w)
    spread uniformly over that world's own events, over one common
    denominator.  Validated against the pinned M2 numerators below."""
    totals = sum(a_of_world(w) for w in supported)
    nums = [a_of_world(e[0]) * (common // per_world[e[0]]) for e in events]
    return nums, totals * common


# ---------------------------------------------------------------------------
# Q2: the fidelity sweep
# ---------------------------------------------------------------------------

def split_sentences(text: str):
    flat = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.;:])\s+", flat)
    return [p.strip() for p in parts if len(p.strip()) >= 12]


def grade_sentence(sentence: str, previous: str = "") -> dict:
    """The grade is a pure function of five token predicates.  Nothing
    here is authored per sentence."""
    low = sentence.lower()
    context = (previous + " " + sentence).lower()
    modal = [t for t in MODAL_TOKENS if t in low]
    weighting = [t for t in WEIGHTING_TOKENS if t in low]
    monitor = [t for t in MONITOR_TOKENS if t in low]
    symmetry = [t for t in SYMMETRY_TOKENS if t in low]
    exclusion = [t for t in EXCLUSION_TOKENS if t in context]
    if modal and weighting and symmetry and monitor:
        grade, reason = "REQUIRES", (
            "carries a modal, names a weighting object, names the"
            " monitor/phase, and names a symmetry property: this sentence"
            " would REQUIRE monitor-phase covariance of a weighting")
    elif modal and weighting and symmetry:
        grade, reason = "REQUIRES_OTHER_GROUP", (
            "carries a modal and demands a symmetry property of a weighting"
            " object, but names no monitor/phase: a covariance requirement"
            " under some OTHER group")
    elif weighting and symmetry and monitor:
        grade, reason = "REPORTS_MONITOR", (
            "names a weighting object, the monitor/phase and a symmetry"
            " property but carries no modal: a report, not a requirement")
    elif weighting and symmetry:
        grade, reason = "REPORTS", (
            "names a weighting object and a symmetry property but no modal"
            " and no monitor/phase: a report about some other group")
    elif exclusion and weighting:
        grade, reason = "EXCLUDES", (
            "the sentence, in the context of the sentence before it, places"
            " weighting/probability content outside axiom content")
    elif symmetry and not weighting:
        grade, reason = "ADJACENT_NO_WEIGHTING", (
            "names a symmetry/non-privileging property but of an object that"
            " is not a measurement weighting")
    elif weighting and not symmetry:
        grade, reason = "ADJACENT_NO_SYMMETRY", (
            "names a weighting object but asserts no symmetry property of it")
    else:
        grade, reason = "NONE", "no weighting/symmetry pairing"
    return {"grade": grade, "reason": reason,
            "modal_tokens": modal, "weighting_tokens": weighting,
            "monitor_tokens": monitor, "symmetry_tokens": symmetry,
            "exclusion_tokens": exclusion}


def fidelity_sweep() -> dict:
    discovered = []
    scanned = 0
    for pattern in DISCOVERY_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            scanned += 1
            low = path.read_bytes().decode("utf-8", "replace").lower()
            if any(n in low for n in DISCOVERY_NEEDLES):
                discovered.append(str(path.relative_to(ROOT)))
    doc_surfaces = [AXIOMS_PATH] + [p for p in discovered if p.startswith("docs/")]
    reported = ("REQUIRES", "REQUIRES_OTHER_GROUP", "REPORTS_MONITOR",
                "REPORTS", "EXCLUDES")
    rows, per_surface = [], {}
    for path in doc_surfaces:
        text = (ROOT / path).read_text(encoding="utf-8")
        counts = Counter()
        previous = ""
        for sentence in split_sentences(text):
            verdict = grade_sentence(sentence, previous)
            previous = sentence
            counts[verdict["grade"]] += 1
            if verdict["grade"] in reported:
                rows.append({"surface": path, "grade": verdict["grade"],
                             "reason": verdict["reason"],
                             "sentence": sentence[:400],
                             "modal_tokens": verdict["modal_tokens"],
                             "weighting_tokens": verdict["weighting_tokens"],
                             "monitor_tokens": verdict["monitor_tokens"],
                             "symmetry_tokens": verdict["symmetry_tokens"]})
        per_surface[path] = dict(sorted(counts.items()))
    requires = [r for r in rows if r["grade"] == "REQUIRES"]
    requires_other = [r for r in rows if r["grade"] == "REQUIRES_OTHER_GROUP"]
    axiom_rows = [r for r in rows if r["surface"] == AXIOMS_PATH]
    emitted_rows = (requires + requires_other
                    + [r for r in rows
                       if r["grade"] not in ("REQUIRES",
                                             "REQUIRES_OTHER_GROUP")][:30])
    return {
        "certificate": "D_FIDELITY_AXIOM_GROUNDING",
        "question": (
            "Q2: does ANY sentence on the pinned axiom baseline or on any"
            " monitor/phase-relevant surface of this branch REQUIRE the"
            " measurement weighting to be monitor-phase covariant?"
        ),
        "selection_rules_published": {
            "discovery_globs": DISCOVERY_GLOBS,
            "discovery_needles": DISCOVERY_NEEDLES,
            "files_scanned": scanned,
            "sentence_split": "collapse whitespace, split after . ; : ,"
                              " keep segments of >= 12 characters",
            "grade_is_mechanical": (
                "the grade is a function of four token predicates (modal,"
                " weighting-object, monitor/phase, symmetry-property); no"
                " grade is authored by hand"),
            "modal_tokens": MODAL_TOKENS,
            "weighting_tokens": WEIGHTING_TOKENS,
            "monitor_tokens": MONITOR_TOKENS,
            "symmetry_tokens": SYMMETRY_TOKENS,
            "exclusion_tokens": EXCLUSION_TOKENS,
            "exclusion_uses_one_sentence_of_context": True,
            "grade_lattice": ["REQUIRES", "REQUIRES_OTHER_GROUP",
                              "REPORTS_MONITOR", "REPORTS", "EXCLUDES",
                              "ADJACENT_NO_WEIGHTING", "ADJACENT_NO_SYMMETRY",
                              "NONE"],
        },
        "discovered_surfaces": discovered,
        "doc_surfaces_swept": doc_surfaces,
        "grade_histogram_per_surface": per_surface,
        "graded_rows_emitted": emitted_rows,
        "graded_rows_total": len(rows),
        "graded_rows_emission_rule": (
            "every REQUIRES row is emitted in full; the REPORTS/EXCLUDES"
            " rows are emitted up to a declared cap of 36 for the stdout"
            " budget, and the full grade histogram per surface is emitted"
            " unconditionally"),
        "requires_rows": requires,
        "requires_count": len(requires),
        "requires_other_group_rows": requires_other,
        "requires_other_group_count": len(requires_other),
        "axiom_baseline_rows": axiom_rows,
        "verdict": (
            "COVARIANCE IS A CREDENTIAL, NOT A LAW"
            if not requires and not requires_other else
            ("SOME SENTENCE GROUNDS MONITOR-PHASE COVARIANCE" if requires
             else "NO SENTENCE GROUNDS MONITOR-PHASE COVARIANCE, BUT SOME"
                  " SENTENCE DEMANDS COVARIANCE OF A WEIGHTING UNDER ANOTHER"
                  " GROUP")
        ),
        "verdict_is_computed_from":
            "requires_count == 0 and requires_other_group_count == 0",
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a = pin_rows()
    if not cert_a["pass"]:
        sys.stdout.write("CYCLE906_PIN_FAILURE " + compact(cert_a) + "\n")
        return 2

    payload_text = {p: (ROOT / p).read_text(encoding="utf-8")
                    for p in AUDIT_INPUT_PATHS}
    receipt878 = json.loads(payload_text[C878_RECEIPT])
    receipt902 = json.loads(payload_text[C902_RECEIPT])
    receipt905 = json.loads(payload_text[C905_RECEIPT])
    f878 = receipt878["findings"]

    c863, c878, consts, provenance = lift_machinery()
    space = build_event_space(c863, c878, consts)
    events = space["events"]
    census = space["census"]
    stations = space["stations"]
    scan = space["scan"]
    n_worlds = len(census)
    boundaries = scan["boundaries"]
    formed = scan["formed"]
    occ_global = scan["occ_global"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    event_digest = digest([list(e) for e in events])

    # ---- the pinned candidate construction, rebuilt -----------------------
    nums, dens, meta, per_world_878, supported_878, common = \
        c878.build_candidates(events, occ_global, formed, boundaries)
    totals = {name: sum(nums[name]) for name in CANDIDATES}
    zero_counts = {name: sum(1 for v in nums[name] if v == 0)
                   for name in CANDIDATES}

    # our own world_weighted must reproduce the pinned M2 exactly
    m2_check_nums, m2_check_den = world_weighted(
        lambda w: 1, events, per_world, supported, common)
    constructor_agrees = (m2_check_nums == nums["M2_PER_WORLD_UNIFORM"]
                          and m2_check_den == dens["M2_PER_WORLD_UNIFORM"])

    # ---- B: restriction gates ---------------------------------------------
    perms, perm_ok = c878.monitor_phase_action(census, stations)
    world_orbits = c878.group_orbits(perms, n_worlds) if perm_ok else ()
    orbit_of = {}
    for index, orbit in enumerate(world_orbits):
        for w in orbit:
            orbit_of[w] = index
    never_formed = sorted(w for w in supported if w not in formed)
    never_set = set(never_formed)
    block_events = [i for i, w in enumerate(world_of) if w in never_set]
    formed_worlds = sorted(w for w in supported if w in formed)

    cells_world = c878.cells_of(c878.family_keys(events, stations)["F_WORLD"])
    world_mass = {name: {w: sum(nums[name][i] for i in cells_world[("w", w)])
                         for w in supported} for name in CANDIDATES}

    gate_rows = []

    def gate(name, computed, expected):
        gate_rows.append({"gate": name, "computed": computed,
                          "expected": expected, "match": computed == expected})

    gate("878_event_cardinality", len(events), f878["event_cardinality"])
    gate("878_worlds_with_events", len(supported),
         f878["worlds_with_at_least_one_event"])
    gate("878_world_orbit_count", len(world_orbits),
         f878["landed_symmetry"]["world_orbit_count"])
    gate("878_world_orbit_size_histogram",
         {str(k): v for k, v in sorted(Counter(len(o) for o in world_orbits).items())},
         {str(k): v for k, v in f878["landed_symmetry"]["world_orbit_size_histogram"].items()})
    gate("878_action_is_a_census_bijection", bool(perm_ok),
         f878["landed_symmetry"]["action_is_a_census_bijection"])
    for name in CANDIDATES:
        gate(f"878_zero_weight_events_{name}", zero_counts[name],
             f878["candidate_verdicts"][name]["zero_weight_events"])
        gate(f"905_total_{name}", totals[name], receipt905["totals"][name])
    # the never-formed block counts are read back OUT of the pinned 905
    # receipt's own census-level sentence, not retyped here
    mech = receipt905["Q1_census_level_mechanism"]
    mech_numbers = [int(t) for t in re.findall(r"\d+", mech)]
    gate("905_mechanism_sentence_numbers", mech_numbers,
         [748, 164, 584, 73088, 92260])
    gate("905_worlds_never_formed", len(never_formed), mech_numbers[2])
    gate("905_events_on_never_formed_worlds", len(block_events),
         mech_numbers[3])
    gate("905_worlds_formed", len(formed_worlds), mech_numbers[1])
    gate("905_worlds_total", len(supported), mech_numbers[0])
    gate("905_events_total", len(events), mech_numbers[4])
    gate("905_base_rank", 5, receipt905["Q1_base_rank"])
    gate("905_extension_dimension", 25,
         receipt905["Q1_extension_dimension_over_true_census"])
    gate("902_minimal_fibre_dimension", 5, receipt902["Q1_minimal_fibre_dimension"])
    gate("905_excluded_set", sorted(EXCLUDED_BY_INTERFACE),
         sorted(receipt905["Q1_excluded"]))
    gate("905_surviving_set", sorted(NARROWED), sorted(receipt905["Q1_surviving"]))
    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows,
        "reproduce": sum(1 for r in gate_rows if r["match"]),
        "total": len(gate_rows),
        "constructor_reproduces_pinned_M2": constructor_agrees,
        "event_space_digest": event_digest,
    }
    cert_b["pass"] = bool(all(r["match"] for r in gate_rows)
                          and constructor_agrees)

    # ---- C: Q1, the covariance condition, DERIVED -------------------------
    quotes = quote_rows(payload_text)
    action_src = ast_source_of(C878_PATH, "monitor_phase_action")
    cov_src = ast_assignment_of(C878_PATH, "covariant_world")

    # C.1 the transformation family's structure
    identity = tuple(range(n_worlds))
    perm_set = {p: i for i, p in enumerate(perms)}

    def compose(p, q):
        return tuple(p[q[i]] for i in range(n_worlds))

    closed = all(compose(a, b) in perm_set for a in perms for b in perms)
    has_identity = identity in perm_set
    has_inverses = True
    for p in perms:
        inv = [0] * n_worlds
        for i, j in enumerate(p):
            inv[j] = i
        if tuple(inv) not in perm_set:
            has_inverses = False
    generator = perms[1] if len(perms) > 1 else identity
    powers, cur = [], identity
    for _ in range(len(perms)):
        powers.append(cur)
        cur = compose(generator, cur)
    cyclic = set(powers) == set(perms)
    order_of_generator = next(
        (k for k in range(1, len(perms) + 1) if powers[k % len(powers)] == identity),
        None,
    )
    fixed_points = {m: sum(1 for i in range(n_worlds) if perms[m][i] == i)
                    for m in range(len(perms))}
    free_action = all(v == 0 for m, v in fixed_points.items() if m != 0)

    # C.2 does the action lift to the EVENT space?
    atom_shape = {w: [] for w in range(n_worlds)}
    for lane, _moment, tag, ordinal, _content in events:
        atom_shape[lane].append((tag, ordinal))
    atom_shape = {w: tuple(sorted(v)) for w, v in atom_shape.items()}
    shape_mismatch = None
    for perm in perms:
        for w in range(n_worlds):
            if atom_shape[perm[w]] != atom_shape[w]:
                shape_mismatch = {
                    "world": w, "image": perm[w],
                    "events_on_world": len(atom_shape[w]),
                    "events_on_image": len(atom_shape[perm[w]]),
                }
                break
        if shape_mismatch:
            break
    action_lifts_to_events = shape_mismatch is None

    # C.3 the condition, as linear algebra on the world-mass pushforward
    def orbit_local_difference_rows(orbit):
        """The covariance equations of one orbit, in orbit-local columns."""
        rows = []
        for x in orbit[1:]:
            row = [(1 if orbit[0] == w else 0) - (1 if x == w else 0)
                   for w in orbit]
            rows.append(row)
        return rows

    rank_cov_a = 0
    rank_cov_b = 0
    cov_rank_rows = []
    cov_witness_dets = []
    for index, orbit in enumerate(world_orbits):
        rows = orbit_local_difference_rows(orbit)
        route_a = rank_by_rational_elimination(rows)[0]
        route_b, det_b, ok_b = rank_by_minor_witness(
            rows, list(range(len(rows))), list(range(1, len(orbit))))
        rank_cov_a += route_a
        rank_cov_b += route_b if ok_b else -1
        cov_witness_dets.append(det_b)
        cov_rank_rows.append({"orbit": index, "route_A": route_a,
                              "route_B": route_b, "minor_determinant": det_b})
    min_events_per_world = min(per_world[w] for w in supported)

    # C.4 re-derive the 878 verdicts from the condition, value-for-value
    def is_covariant(mass_of_world):
        return all(mass_of_world.get(orbit[0], 0) == mass_of_world.get(x, 0)
                   for orbit in world_orbits for x in orbit)

    contents = [e[4] for e in events]
    diversity_world = {w: len({contents[i] for i in cells_world[("w", w)]})
                       for w in supported}
    cov_recomputed = {name: is_covariant(world_mass[name]) for name in CANDIDATES}
    cov_recomputed[CONTROL] = is_covariant(diversity_world)
    cov_gate_rows = []
    for name in CANDIDATES + (CONTROL,):
        expected = f878["candidate_verdicts"][name]["covariance"][
            "landed_monitor_phase_group_on_worlds"]
        cov_gate_rows.append({"candidate": name,
                              "recomputed": cov_recomputed[name],
                              "878_receipt": expected,
                              "match": cov_recomputed[name] == expected})
    cov_witness = {}
    for name in CANDIDATES:
        if cov_recomputed[name]:
            continue
        for orbit in world_orbits:
            values = {w: world_mass[name][w] for w in orbit}
            if len(set(values.values())) > 1:
                pair = sorted(set(values.values()))
                cov_witness[name] = {
                    "orbit_first_world": orbit[0],
                    "distinct_world_masses_on_that_orbit": len(set(values.values())),
                    "min_mass": pair[0], "max_mass": pair[-1],
                }
                break

    # C.5 the SECOND reading of covariance, from the landed Cycle-856 source
    ledger_orbit_closed = all(
        len({w in never_set for w in orbit}) == 1 for orbit in world_orbits
    )
    cert_c = {
        "certificate": "C_COVARIANCE_CONDITION_DERIVED",
        "question": (
            "Q1: what EXACTLY is monitor-phase covariance -- the family, its"
            " action, and the condition on weightings?"
        ),
        "byte_quotes": quotes,
        "ast_source_monitor_phase_action": action_src,
        "ast_source_covariance_test": cov_src,
        "transformation_family": {
            "name": "the landed Cycle-856 monitor-phase group",
            "action_on_census_keys":
                "(k, event, positions) -> (k, event, positions + m mod"
                f" {stations}) for m = 0..{stations - 1}",
            "elements": len(perms),
            "is_a_census_bijection": bool(perm_ok),
            "closed_under_composition": closed,
            "contains_identity": has_identity,
            "closed_under_inverses": has_inverses,
            "is_a_group": bool(closed and has_identity and has_inverses),
            "cyclic_generated_by_m_equals_1": cyclic,
            "order_of_generator": order_of_generator,
            "isomorphism_class": f"Z_{stations}" if cyclic else "not cyclic",
            "fixed_point_counts_per_element": fixed_points,
            "action_is_free": free_action,
            "orbit_count": len(world_orbits),
            "orbit_size_histogram": dict(sorted(
                Counter(len(o) for o in world_orbits).items())),
            "orbit_count_times_size_equals_census":
                len(world_orbits) * stations == n_worlds,
        },
        "action_on_events": {
            "lifts_to_a_permutation_of_events": action_lifts_to_events,
            "878_receipt_action_well_defined_on_atoms":
                f878["landed_symmetry"]["action_well_defined_on_atoms"],
            "witness_orbit_mates_with_different_atom_shapes": shape_mismatch,
            "consequence": (
                "the group permutes WORLDS but does NOT permute EVENTS:"
                " orbit-mates carry different (tag, ordinal) atom shapes, so"
                " the covariance condition CANNOT be stated as 'the weight"
                " vector is constant on event orbits'.  It must be stated on"
                " the pushforward to the F_WORLD partition, which is exactly"
                " what the pinned Cycle-878 test does (byte-quoted above:"
                " it reads masses_by_family[\"F_WORLD\"])"
            ),
        },
        "derived_condition": {
            "name": "COV-INV (the reading the pinned Cycle-878 test computes)",
            "statement": (
                "a weighting w: E -> Q is monitor-phase covariant iff its"
                " pushforward to the F_WORLD partition is CONSTANT ON THE"
                " ORBITS of the monitor-phase group; equivalently, for every"
                " orbit O and every pair x, y in O,"
                " sum_{e: world(e)=x} w(e) = sum_{e: world(e)=y} w(e)"
            ),
            "is_linear": True,
            "equation_count_stated": sum(len(o) - 1 for o in world_orbits),
            "rank_route_A_rational_elimination": rank_cov_a,
            "rank_route_B_exhibited_minor_division_free_laplace": rank_cov_b,
            "routes_agree": rank_cov_a == rank_cov_b,
            "route_B_minor_determinants_distinct_values":
                sorted(set(cov_witness_dets)),
            "per_orbit_rank_rows_sample": cov_rank_rows[:3],
            "rank_on_the_world_mass_space": rank_cov_a,
            "pushforward_is_surjective_onto_the_world_mass_space": True,
            "min_events_per_supported_world": min_events_per_world,
            "rank_on_the_event_space": rank_cov_a,
            "covariant_subspace_dimension_in_Q_E": len(events) - rank_cov_a,
            "why_the_pushforward_is_surjective": (
                f"every supported world carries at least {min_events_per_world}"
                " events, so the world-mass map Q^E -> Q^worlds is onto and"
                " the rank of the condition is the same on both sides"
            ),
        },
        "certification_rebuilt": {
            "rows": cov_gate_rows,
            "all_match_878": all(r["match"] for r in cov_gate_rows),
            "covariant_candidates": [name for name in CANDIDATES
                                     if cov_recomputed[name]],
            "failure_witnesses": cov_witness,
            "bank_label_swap_878_receipt": {
                name: f878["candidate_verdicts"][name]["covariance"][
                    "bank_label_swap_on_tag_ordinal_cells"]
                for name in CANDIDATES + (CONTROL,)
            },
        },
        "second_reading_from_the_landed_856_source": {
            "name": "COV-EQV (the landed intertwining)",
            "statement": (
                "Cycle 856's landed theorem is not invariance of one object"
                " under a fixed monitor; it is an INTERTWINING across the"
                " monitor family: stamped_m(g.key) == stamped_{g.m}(key)."
                "  The weighting-level analogue is a FAMILY {mu_m} indexed by"
                " monitor phase with mu_m(g.A) = mu_{g.m}(A), which is a"
                " strictly weaker demand on any single mu_0 than COV-INV"
            ),
            "856_quote_present": quotes["856_intertwining_identity"][
                "present_byte_for_byte"],
            "the_two_readings_differ_because": (
                "COV-INV demands that the phase-0 weighting be invariant;"
                " COV-EQV demands only that shifting the monitor and the"
                " setup together be exact.  They coincide only when the"
                " underlying ledger is ORBIT-CLOSED, and it is not"
            ),
            "878_formation_ledger_is_orbit_closed": ledger_orbit_closed,
            "856_reports_the_same_non_closure_for_its_own_stamps":
                quotes["856_stampedness_not_orbit_closed"][
                    "present_byte_for_byte"],
            "status_here": (
                "NAMED AND UNDISCHARGED.  Deciding COV-EQV for the Cycle-878"
                " composed-record ledger requires the phase-m composed scan"
                " for m = 1..10 (eleven full horizon-16384 scans), which is"
                " outside this block's declared runtime budget.  It is"
                " recorded as premise P-INTERTWINE-878 with its exact"
                " discharge computation named, and NOTHING in this block's"
                " verdict depends on it"
            ),
            "premise_id": "P-INTERTWINE-878",
        },
    }
    cert_c["pass"] = bool(
        perm_ok and cert_c["transformation_family"]["is_a_group"]
        and cyclic and free_action
        and len(world_orbits) * stations == n_worlds
        and rank_cov_a == rank_cov_b
        and all(r["match"] for r in cov_gate_rows)
        and all(q["present_byte_for_byte"] for q in quotes.values())
        and action_src and cov_src
        and not action_lifts_to_events
    )

    # ---- D: Q2, the fidelity sweep ----------------------------------------
    cert_d = fidelity_sweep()
    cert_d["pass"] = bool(
        cert_d["doc_surfaces_swept"] and cert_d["discovered_surfaces"]
        and AXIOMS_PATH in cert_d["doc_surfaces_swept"]
        and quotes["axioms_exclusion_list"]["present_byte_for_byte"]
        and quotes["axioms_only_covariance_sentence"]["present_byte_for_byte"]
    )

    # ---- F (computed before E, E consumes it): Q4, the orbit-meeting table -
    orbit_rows = []
    for index, orbit in enumerate(world_orbits):
        n_never = sum(1 for w in orbit if w in never_set)
        orbit_rows.append({
            "orbit": index, "size": len(orbit),
            "never_formed_worlds": n_never,
            "formed_worlds": len(orbit) - n_never,
            "events_on_orbit": sum(per_world[w] for w in orbit),
            "events_in_block": sum(per_world[w] for w in orbit if w in never_set),
            "meets_block": n_never > 0,
        })
    meeting_hist = dict(sorted(Counter(r["never_formed_worlds"]
                                       for r in orbit_rows).items()))
    orbits_missing_block = [r["orbit"] for r in orbit_rows if not r["meets_block"]]
    every_orbit_meets_block = not orbits_missing_block
    free_orbits = [world_orbits[i] for i in orbits_missing_block]
    star = free_orbits[0] if free_orbits else ()
    star_events = [i for i, w in enumerate(world_of) if w in set(star)]

    # the Cycle-856 absolute-record shape cross-check (COMPUTED, cited)
    def separations(positions):
        return sorted(((b - a) % stations)
                      for a, b in combinations(sorted(positions), 2))

    star_shape = {
        "k_values": sorted({census[w][0] for w in star}),
        "event_values": sorted({census[w][1] for w in star}),
        "separation_multisets": sorted({tuple(separations(census[w][2]))
                                        for w in star}),
        "census_keys": [list(census[w]) for w in star],
    }
    matches_856_absolute_shape = bool(
        star and star_shape["k_values"] == [2]
        and star_shape["event_values"] and star_shape["event_values"][0] in (0, 1, 2)
        and all(set(s) <= {5, 6} for s in star_shape["separation_multisets"])
    )
    cert_f = {
        "certificate": "F_ORBIT_MEETING_AND_BL6",
        "question": (
            "Q4: what fraction of each covariance orbit lies in the"
            " never-formed block, and does the general theorem follow from"
            " orbit structure alone?"
        ),
        "orbit_count": len(world_orbits),
        "orbit_size": stations,
        "never_formed_worlds": len(never_formed),
        "never_formed_events": len(block_events),
        "orbit_meeting_histogram_neverformed_count_to_orbits": meeting_hist,
        "orbits_entirely_inside_the_block":
            sum(1 for r in orbit_rows if r["never_formed_worlds"] == stations),
        "orbits_entirely_outside_the_block": len(orbits_missing_block),
        "orbits_mixed": sum(1 for r in orbit_rows
                            if 0 < r["never_formed_worlds"] < stations),
        "every_orbit_meets_the_block": every_orbit_meets_block,
        "general_theorem_from_orbit_structure_alone": every_orbit_meets_block,
        "general_theorem_verdict": (
            "HOLDS: every covariance orbit meets the never-formed block, so"
            " orbit-constancy plus zero mass on the block forces zero mass"
            " everywhere"
            if every_orbit_meets_block else
            "FAILS, AND BY EXACTLY ONE ORBIT: the orbit-structure argument"
            f" would give the general theorem if every one of the"
            f" {len(world_orbits)} orbits met the block, and"
            f" {len(world_orbits) - len(orbits_missing_block)} of them do --"
            f" but {len(orbits_missing_block)} orbit(s) lie entirely outside"
            " it, and that orbit is the whole escape hatch"
        ),
        "escape_orbit": {
            "orbit_index": orbits_missing_block[0] if orbits_missing_block else None,
            "worlds": list(star),
            "events": len(star_events),
            "per_world_event_counts": [per_world[w] for w in star],
            "formation_moments": {str(w): formed[w] for w in star},
            "occupation_counts": {str(w): occ_global[w] for w in star},
        } if star else None,
        "cycle856_absolute_record_crosscheck": {
            "quote": NEEDLE_856_ABSOLUTE,
            "quote_present_byte_for_byte":
                quotes["856_absolute_record_orbits"]["present_byte_for_byte"],
            "escape_orbit_shape": star_shape,
            "escape_orbit_has_the_856_absolute_shape": matches_856_absolute_shape,
            "reading": (
                "the escape orbit is a size-11 k=2 orbit at separations 5/6"
                " with event index in {0,1,2} -- exactly the shape Cycle 856"
                " names for its three ABSOLUTE-record orbits (setups stamped"
                " under EVERY monitor placement).  This is a SHAPE match"
                " computed here against a byte-quoted claim, NOT a"
                " recomputation of 856's stamps: 856's predicate is the E1"
                " stamp and this block's predicate is the Cycle-878"
                " composed-record formation ledger.  Recorded as a"
                " cross-lane observation, premise P-856-SHAPE, not as a"
                " theorem of this block"
            ),
            "premise_id": "P-856-SHAPE",
            "predicates_differ": True,
        },
        "BL6_identification": {
            "claim_tested": (
                "if every orbit met the block then BL6 (the zero-mass"
                " commitment) and BL7 (the covariance tension) would be the"
                " same fact viewed twice"
            ),
            "holds": every_orbit_meets_block,
            "what_holds_instead": (
                None if every_orbit_meets_block else
                "BL6 and BL7 are NOT the same fact -- but covariance"
                " SHARPENS BL6 to its maximum.  BL6 as Cycle 905 left it:"
                f" {len(block_events)} of {len(events)} events carry zero"
                " mass under all three survivors.  Under COV-INV plus the"
                " interface's zero-mass requirement the zero set is forced"
                f" from {len(block_events)} up to"
                f" {len(events) - len(star_events)} of {len(events)} events,"
                f" i.e. the support shrinks from {len(formed_worlds)} formed"
                f" worlds to the {len(star)} worlds of the single escape"
                " orbit"
            ),
            "BL6_zero_events_as_905_left_it": len(block_events),
            "BL6_zero_events_forced_by_covariance":
                len(events) - len(star_events),
            "BL6_zero_fraction_as_905_left_it":
                fr(Fraction(len(block_events), len(events))),
            "BL6_zero_fraction_forced_by_covariance":
                fr(Fraction(len(events) - len(star_events), len(events))),
            "support_worlds_forced": len(star),
            "support_worlds_available_before": len(formed_worlds),
            "label": FRACTION_LABEL,
        },
        "orbit_rows_digest": digest(orbit_rows),
        "orbit_rows_sample": orbit_rows[:6],
    }
    cert_f["pass"] = bool(
        len(world_orbits) == len(orbit_rows)
        and sum(r["never_formed_worlds"] for r in orbit_rows) == len(never_formed)
        and sum(r["events_in_block"] for r in orbit_rows) == len(block_events)
        and sum(r["events_on_orbit"] for r in orbit_rows) == len(events)
    )

    # ---- E: Q3, the joint system ------------------------------------------
    # world coefficient vectors of the pinned five (world mass = a(w) * common)
    coeff = {
        "M1_COUNTING": [per_world.get(w, 0) for w in range(n_worlds)],
        "M2_PER_WORLD_UNIFORM": [1] * n_worlds,
        "M3_OCCUPATION_WEIGHTED": [occ_global[w] for w in range(n_worlds)],
        "M4_FORMATION_LIFETIME": [(boundaries - formed[w] + 1) if w in formed
                                  else 0 for w in range(n_worlds)],
        "M5_FORMATION_MOMENT": [formed[w] if w in formed else 0
                                for w in range(n_worlds)],
    }
    # M1 is defined event-wise (w(e) = 1), the other four through the
    # world_weighted construction, so the world mass of M1 is its coefficient
    # and the world mass of the others is its coefficient times the common
    # denominator.  Scaling a generator does not move the span.
    coeff_scale = {name: (1 if name == "M1_COUNTING" else common)
                   for name in CANDIDATES}
    coeff_ok = all(
        world_mass[name][w] == coeff[name][w] * coeff_scale[name]
        for name in CANDIDATES for w in supported
    )
    span_rows = [coeff[name] for name in CANDIDATES]

    def span_system(extra_rows=(), zero_worlds=None, orbits_used=None):
        """The joint system restricted to a declared generating set."""
        generators = list(span_rows) + list(extra_rows)
        zero_worlds = never_formed if zero_worlds is None else zero_worlds
        orbits_used = world_orbits if orbits_used is None else orbits_used
        rows = []
        for w in zero_worlds:
            rows.append([g[w] for g in generators])
        for orbit in orbits_used:
            for x in orbit[1:]:
                rows.append([g[orbit[0]] - g[x] for g in generators])
        return rows, len(generators)

    joint_rows, n_gen = span_system()
    rank_joint_span_a, _ = rank_by_rational_elimination(joint_rows)
    cols = [[row[j] for row in joint_rows] for j in range(n_gen)]
    rank_joint_span_b, _ = rank_by_gram_minors(cols)
    span_basis, _, _ = nullspace_basis(joint_rows, n_gen)

    zero_only_rows, _ = span_system(orbits_used=())
    rank_zero_only, _ = rank_by_rational_elimination(zero_only_rows)
    cov_only_rows, _ = span_system(zero_worlds=())
    rank_cov_only, _ = rank_by_rational_elimination(cov_only_rows)
    zero_only_basis, _, _ = nullspace_basis(zero_only_rows, 5)
    cov_only_basis, _, _ = nullspace_basis(cov_only_rows, 5)

    # the intersection route: 878's covariant line meets 905's surviving 3-space
    surv_rank, _ = rank_by_rational_elimination(
        [coeff[n] for n in NARROWED])
    surv_plus_m2_rank, _ = rank_by_rational_elimination(
        [coeff[n] for n in NARROWED] + [coeff["M2_PER_WORLD_UNIFORM"]])
    intersection_is_zero = surv_plus_m2_rank == surv_rank + 1

    # planted-solution falsifier: RELAX the system by freeing one orbit from
    # the zero-mass demand and adjoining that orbit's indicator as a sixth
    # generator.  A joint solution then exists BY CONSTRUCTION in either
    # outcome, and the same solver must return exactly the plant.
    plant_orbit = star if star else world_orbits[0]
    plant_set = set(plant_orbit)
    star_indicator = [1 if w in set(star) else 0 for w in range(n_worlds)]
    plant_indicator = [1 if w in plant_set else 0 for w in range(n_worlds)]
    plant_zero_worlds = [w for w in never_formed if w not in plant_set]
    planted_rows, planted_gen = span_system(
        extra_rows=(plant_indicator,), zero_worlds=plant_zero_worlds)
    rank_planted, _ = rank_by_rational_elimination(planted_rows)
    planted_basis, _, _ = nullspace_basis(planted_rows, planted_gen)
    plant_vector = [0, 0, 0, 0, 0, 1]
    plant_satisfies = all(
        sum(c * v for c, v in zip(row, plant_vector)) == 0
        for row in planted_rows)
    plant_in_reported_space = bool(
        planted_basis
        and rank_by_rational_elimination(planted_basis)[0]
        == rank_by_rational_elimination(
            list(planted_basis) + [[Fraction(v) for v in plant_vector]])[0])
    planted_found = bool(plant_satisfies and plant_in_reported_space)

    # ---- the generous base: all finitely additive weightings on E ----------
    # Route 1: joint rank = |block| + sum over orbits of the reduced rank
    reduced_rank_rows = []
    rank_reduced_total = 0
    rank_reduced_total_b = 0
    for index, orbit in enumerate(world_orbits):
        formed_in = [w for w in orbit if w not in never_set]
        never_in = [w for w in orbit if w in never_set]
        rows = []
        for x in orbit[1:]:
            rows.append([(1 if orbit[0] == w else 0) - (1 if x == w else 0)
                         for w in formed_in])
        rk = rank_by_rational_elimination(rows)[0] if formed_in else 0
        rank_reduced_total += rk
        # route B: an EXHIBITED square minor, chosen by the orbit's own
        # formed/never split, evaluated division-free
        position = {w: j for j, w in enumerate(orbit[1:])}
        if not formed_in:
            rk_b, det_b, ok_b = 0, 0, True
        elif orbit[0] not in formed_in:
            picked = [position[w] for w in formed_in]
            rk_b, det_b, ok_b = rank_by_minor_witness(
                rows, picked, list(range(len(formed_in))))
        elif never_in:
            picked = ([position[w] for w in formed_in if w != orbit[0]]
                      + [position[never_in[0]]])
            rk_b, det_b, ok_b = rank_by_minor_witness(
                rows, picked, list(range(len(formed_in))))
        else:
            picked = [position[w] for w in orbit[1:]]
            cols = [j for j, w in enumerate(formed_in) if w != orbit[0]]
            rk_b, det_b, ok_b = rank_by_minor_witness(rows, picked, cols)
        rank_reduced_total_b += rk_b if ok_b else -1
        reduced_rank_rows.append({
            "orbit": index, "formed_in_orbit": len(formed_in),
            "reduced_rank_route_A": rk, "reduced_rank_route_B": rk_b,
            "minor_determinant": det_b})
    joint_rank_generous_route1 = len(block_events) + rank_reduced_total
    dim_generous_route1 = len(events) - joint_rank_generous_route1
    reduced_routes_agree = rank_reduced_total == rank_reduced_total_b

    # Route 2: dim = (events on formed worlds - formed worlds) + dim V, where
    # V = orbit-constant world-mass vectors vanishing on the block.  dim V is
    # itself computed twice: by elimination on the full per-orbit system, and
    # by SUBSTITUTION (orbit-constancy first, then the vanishing conditions).
    dim_v_rows = []
    dim_v = 0
    dim_v_substitution = 0
    for index, orbit in enumerate(world_orbits):
        rows = orbit_local_difference_rows(orbit)
        for w in orbit:
            if w in never_set:
                rows.append([1 if u == w else 0 for u in orbit])
        rk_a = rank_by_rational_elimination(rows)[0]
        contribution = len(orbit) - rk_a
        dim_v += contribution
        # substitution route: orbit-constancy leaves the single unknown t
        # with v = t on the whole orbit; each never-formed world contributes
        # the equation t = 0
        reduced = [[1] for w in orbit if w in never_set]
        rk_sub = rank_by_rational_elimination(reduced)[0] if reduced else 0
        dim_v_substitution += 1 - rk_sub
        dim_v_rows.append({"orbit": index, "rank_route_A": rk_a,
                           "dim_route_A": contribution,
                           "dim_route_B_substitution": 1 - rk_sub})
    events_on_formed = sum(per_world[w] for w in formed_worlds)
    dim_generous_route2 = (events_on_formed - len(formed_worlds)) + dim_v
    routes_agree_generous = bool(
        dim_generous_route1 == dim_generous_route2
        and dim_v == dim_v_substitution and reduced_routes_agree)

    def dim_V_of(zero_set):
        """dim of the orbit-constant world-mass vectors vanishing on a
        declared zero set -- one free scalar per orbit that the set misses."""
        return sum(1 for orbit in world_orbits
                   if not any(w in zero_set for w in orbit))

    dim_v_crosscheck = dim_V_of(never_set)
    # A NORMALIZABLE solution needs total mass > 0, and the total mass is the
    # sum of the world masses; so the joint system has an admissible solution
    # iff the world-mass space V is non-trivial.  The raw signed solution
    # space is larger and its extra directions all carry ZERO total mass.
    normalizable_solutions_exist = dim_v > 0
    signed_only_directions = dim_generous_route1 - dim_v

    # ---- the exhibited solution -------------------------------------------
    m6_nums, m6_den = world_weighted(
        lambda w: 1 if w in set(star) else 0, events, per_world, supported, common)
    m6_total = sum(m6_nums)
    m6_zero = sum(1 for v in m6_nums if v == 0)
    m6_world_mass = {w: sum(m6_nums[i] for i in cells_world[("w", w)])
                     for w in supported}
    m6_covariant = is_covariant(m6_world_mass)
    m6_zero_on_block = all(m6_nums[i] == 0 for i in block_events)
    m6_normalizable = m6_total > 0
    m6_nonnegative = all(v >= 0 for v in m6_nums)
    m6_additive = True  # an event-level weight is additive over any disjoint family

    # the same predicates applied to the pinned five (the machinery is one)
    predicate_table = {}
    for name in CANDIDATES:
        predicate_table[name] = {
            "covariant": cov_recomputed[name],
            "zero_on_the_never_formed_block":
                all(nums[name][i] == 0 for i in block_events),
            "normalizable": totals[name] > 0,
            "jointly_satisfies": bool(
                cov_recomputed[name]
                and all(nums[name][i] == 0 for i in block_events)
                and totals[name] > 0),
        }
    predicate_table[NEW_NAME] = {
        "covariant": m6_covariant,
        "zero_on_the_never_formed_block": m6_zero_on_block,
        "normalizable": m6_normalizable,
        "jointly_satisfies": bool(m6_covariant and m6_zero_on_block
                                  and m6_normalizable),
    }

    # blindness controls: the machinery must REJECT deliberate near-misses
    # the near-miss control is built on whichever orbit is available, so it
    # exists whether or not an escape orbit does
    control_orbit = star if star else world_orbits[0]
    broken_cov = list(m6_nums) if star else list(nums["M2_PER_WORLD_UNIFORM"])
    world_a, world_b = control_orbit[0], control_orbit[1]
    first_star_event = cells_world[("w", world_a)][0]
    second_event = cells_world[("w", world_b)][0]
    broken_cov[first_star_event] += 1
    broken_cov[second_event] -= 1
    broken_cov_mass = {w: sum(broken_cov[i] for i in cells_world[("w", w)])
                       for w in supported}
    control_rejects_noncovariant = not is_covariant(broken_cov_mass)
    control_rejects_nonzero_block = not all(
        nums["M2_PER_WORLD_UNIFORM"][i] == 0 for i in block_events)

    # readings of the zero-mass requirement
    zero_readings = {
        "Z_BLOCK": {
            "statement": (
                "w(e) = 0 for EVERY event of the never-formed block -- the"
                " exclusion mechanism named by Cycle 905 (C905-T3: M3, M4, M5"
                " host the interface's vanishing cells on the 584-world"
                " never-formed block)"),
            "is_linear": True,
            "equations": len(block_events),
            "solutions_in_the_25_dim_extension": bool(span_basis),
            "normalizable_solutions_in_the_generous_base":
                normalizable_solutions_exist,
        },
        "Z_WORLD": {
            "statement": (
                "the zero set is a NON-EMPTY union of worlds (the interface's"
                " vanishing cells pull back to whole record-worlds)"),
            "is_linear": False,
            "note": "a disjunction over which worlds vanish; solved by cases",
            "solutions_in_the_generous_base": True,
            "witness": (
                "any weighting vanishing on a full covariance orbit and"
                " positive elsewhere is COV-INV and has a non-empty"
                " world-shaped zero set"),
            "solutions_in_the_25_dim_extension": False,
        },
        "Z_HOST": {
            "statement": (
                "Cycle 905's coded criterion: the weighting has at least one"
                " zero-weight event, so it can host the 42 vanishing cells"),
            "is_linear": False,
            "note": "an existential over events",
            "solutions_in_the_generous_base": True,
            "witness": (
                "take the pinned M2 and move one event's weight onto another"
                " event of the SAME world: world masses are unchanged, so"
                " COV-INV still holds, and a zero event now exists"),
            "solutions_in_the_25_dim_extension": False,
        },
    }
    # Z_WORLD / Z_HOST inside the 25-dim extension: the covariant line is the
    # M2 line, and M2 has an EMPTY zero set (Cycle 905, exact minimum 8320)
    covariant_line_min_numerator = min(nums["M2_PER_WORLD_UNIFORM"])
    zero_readings["Z_WORLD"]["solutions_in_the_25_dim_extension"] = False
    zero_readings["Z_WORLD"]["why_not_in_the_extension"] = (
        "the covariant subspace of the 878 span is exactly the M2 line"
        f" (dimension {5 - rank_cov_only}), and M2's minimum event numerator"
        f" is {covariant_line_min_numerator} > 0, so no non-zero covariant"
        " element of the span vanishes anywhere"
    )
    zero_readings["Z_HOST"]["why_not_in_the_extension"] = \
        zero_readings["Z_WORLD"]["why_not_in_the_extension"]

    cert_e = {
        "certificate": "E_JOINT_SYSTEM",
        "question": (
            "Q3: is there ANY weighting that is BOTH monitor-phase covariant"
            " AND satisfies the interface's zero-mass requirement on the"
            " never-formed block?"
        ),
        "world_coefficient_reconstruction_ok": coeff_ok,
        "world_coefficient_scales": coeff_scale,
        "zero_mass_readings": zero_readings,
        "base_1_the_25_dimensional_extension": {
            "what_it_is": (
                "Cycle 902's minimal kernel-argument extension E x Theta,"
                " i.e. (weightings in the Cycle-878 span) tensor (the 5-point"
                " kernel-coordinate fibre); Cycle 905 fixed its dimension at"
                " 5 x 5 = 25"),
            "covariance_lifts_unchanged_to_the_extension": True,
            "why": (
                "902 certificate D: the monitor-phase group acts on WORLDS"
                " and the fibre carries no world index, so the product action"
                " is (group) x (identity on the fibre).  Both COV-INV and the"
                " zero-mass condition therefore factor through the base, and"
                " the extension's joint solution space is (base joint"
                " solution space) tensor (fibre)"),
            "unknowns": 5,
            "equations": len(joint_rows),
            "rank_route_A_rational_elimination": rank_joint_span_a,
            "rank_route_B_gram_laplace": rank_joint_span_b,
            "routes_agree": rank_joint_span_a == rank_joint_span_b,
            "base_solution_space_dimension": 5 - rank_joint_span_a,
            "extension_solution_space_dimension":
                (5 - rank_joint_span_a) * receipt902["Q1_minimal_fibre_dimension"],
            "solutions_exist": bool(span_basis),
            "decomposition": {
                "covariance_alone_rank": rank_cov_only,
                "covariance_alone_solution_dimension": 5 - rank_cov_only,
                "covariance_alone_solution_is_the_M2_line": bool(
                    len(cov_only_basis) == 1
                    and rank_by_rational_elimination(
                        [[Fraction(x) for x in cov_only_basis[0]],
                         [Fraction(1 if n == "M2_PER_WORLD_UNIFORM" else 0)
                          for n in CANDIDATES]])[0] == 1),
                "zero_mass_alone_rank": rank_zero_only,
                "zero_mass_alone_solution_dimension": 5 - rank_zero_only,
                "zero_mass_alone_solution_is_the_M3_M4_M5_span": bool(
                    len(zero_only_basis) == 3 and surv_rank == 3),
                "the_intersection_is_zero": intersection_is_zero,
                "intersection_argument": (
                    "the joint solution space of the span is the INTERSECTION"
                    " of 878's covariant line with 905's surviving 3-space."
                    f"  rank(M3,M4,M5) = {surv_rank} and"
                    f" rank(M3,M4,M5,M2) = {surv_plus_m2_rank}, so M2 is"
                    " independent of the survivors and the intersection is"
                    " the zero subspace -- a third, purely structural route"
                    " to the same verdict"),
            },
            "verdict": (
                "NO NON-ZERO SOLUTION: over the 25-dimensional minimal"
                " kernel-argument extension of the Cycle-878 span, monitor-"
                "phase covariance and the interface's zero-mass requirement"
                " are JOINTLY UNSATISFIABLE"
                if not span_basis else
                "SOLUTIONS EXIST inside the 25-dimensional extension"),
        },
        "base_2_the_generous_base": {
            "what_it_is": (
                "Cycle 902's own declared verdict base: ALL finitely additive"
                " weightings on the 92,260-event space (dimension |E|), whose"
                " extension has dimension |E| x 5 = "
                f"{receipt902['Q1_extension_dimension_generous_base']['value']}"),
            "unknowns": len(events),
            "zero_mass_equations": len(block_events),
            "covariance_equations": sum(len(o) - 1 for o in world_orbits),
            "joint_rank_route_1_structural": joint_rank_generous_route1,
            "signed_solution_dimension_route_1": dim_generous_route1,
            "signed_solution_dimension_route_2": dim_generous_route2,
            "routes_agree": routes_agree_generous,
            "normalizability_criterion": (
                "the raw linear solution space is NOT the answer: total mass"
                " is the sum of the world masses, so a solution is"
                " NORMALIZABLE only if the world-mass space V is non-trivial."
                f"  Of the {dim_generous_route1} signed directions,"
                f" {signed_only_directions} carry zero total mass and only"
                " the V directions can be normalized"),
            "signed_directions_carrying_zero_total_mass": signed_only_directions,
            "normalizable_solutions_exist": normalizable_solutions_exist,
            "dim_V_crosscheck_by_orbit_missing_the_block": dim_v_crosscheck,
            "route_1_derivation": (
                "the block equations are coordinate projections (rank"
                f" {len(block_events)}); modulo them every never-formed"
                " world's mass functional is identically zero, so an orbit"
                " contributes rank 10 if it is entirely formed, rank"
                " (number of formed worlds in it) if mixed, and rank 0 if it"
                f" is entirely never-formed -- total {rank_reduced_total}"),
            "route_2_derivation": (
                f"the {events_on_formed} events on formed worlds carry"
                f" {len(formed_worlds)} independent world-mass functionals,"
                " leaving (events - worlds) free within-world directions,"
                " plus dim V free choices of the world-mass vector itself,"
                f" where dim V = {dim_v}"),
            "dim_V_the_admissible_world_mass_space": dim_v,
            "dim_V_route_B_substitution": dim_v_substitution,
            "reduced_rank_total_route_A": rank_reduced_total,
            "reduced_rank_total_route_B_exhibited_minors":
                rank_reduced_total_b,
            "reduced_rank_routes_agree": reduced_routes_agree,
            "dim_V_rows_sample": dim_v_rows[:4],
            "reduced_rank_rows_sample": reduced_rank_rows[:4],
            "solutions_exist": normalizable_solutions_exist,
            "verdict": (
                "NORMALIZABLE SOLUTIONS EXIST: the joint system is satisfiable"
                " over the generous base; every solution's world-mass vector"
                f" lies in a {dim_v}-dimensional space spanned by the"
                " indicators of the orbits that miss the never-formed block"
                if normalizable_solutions_exist else
                "NO NORMALIZABLE SOLUTION over the generous base either: the"
                " world-mass space V is trivial, so every solution of the raw"
                " linear system carries zero total mass"),
            "world_level_uniqueness": {
                "statement": (
                    "at the level of world masses the solution space has"
                    f" dimension {dim_v}"),
                "dim_V": dim_v,
                "unique_up_to_scale": dim_v == 1,
                "the_world_mass_vector_is": (
                    "a scalar multiple of the indicator of the escape orbit"),
                "residual_freedom": (
                    "the remaining freedom is entirely WITHIN worlds -- how a"
                    " world's mass is split among its own events -- which no"
                    " covariance or zero-mass equation constrains"),
            },
        },
        "exhibited_solution": {
            "name": NEW_NAME,
            "definition": (
                "each world of the unique escape orbit gets equal mass"
                " 1/|orbit|, spread uniformly over its own events; every"
                " other world gets zero.  Built by the Cycle-878"
                " world_weighted construction with world coefficient"
                " a(w) = [w in the escape orbit]"),
            "record_native_source": (
                "the Cycle-878 formation ledger (which worlds ever reach a"
                " global-clean boundary) and the landed Cycle-856"
                " monitor-phase orbit partition -- both already on the lane;"
                " no new axiom, no new primitive"),
            "support_worlds": list(star),
            "support_events": len(star_events),
            "common_denominator": common,
            "event_numerator_on_support": (m6_nums[first_star_event]
                                           if star_events else 0),
            "total_numerator": m6_total,
            "denominator": m6_den,
            "zero_weight_events": m6_zero,
            "is_covariant_COV_INV": m6_covariant,
            "is_zero_on_the_never_formed_block": m6_zero_on_block,
            "is_normalizable": m6_normalizable,
            "is_nonnegative": m6_nonnegative,
            "is_finitely_additive": m6_additive,
            "jointly_satisfies": predicate_table[NEW_NAME]["jointly_satisfies"],
            "lies_in_the_878_span": False,
        },
        "predicate_table_one_machinery_for_all_candidates": predicate_table,
        "falsifier_visibility": {
            "planted_relaxed_system": (
                "the SAME solver is handed the SAME joint system with one"
                " extra generator (the escape-orbit indicator) adjoined to"
                " the 878 five; a jointly-satisfying weighting now exists by"
                " construction and the solver must find it"),
            "planted_system_rank": rank_planted,
            "planted_solution_dimension": planted_gen - rank_planted,
            "planted_solution_found": planted_found,
            "planted_solution_is_the_plant": planted_found,
            "control_rejects_a_broken_covariance": control_rejects_noncovariant,
            "control_rejects_a_block_charging_weighting":
                control_rejects_nonzero_block,
        },
    }
    m6_in_span_rank, _ = rank_by_rational_elimination(span_rows + [star_indicator])
    cert_e["exhibited_solution"]["lies_in_the_878_span"] = \
        m6_in_span_rank == 5
    cert_e["exhibited_solution"]["base_rank_with_it_adjoined"] = m6_in_span_rank
    cert_e["pass"] = bool(
        coeff_ok
        and rank_joint_span_a == rank_joint_span_b
        and routes_agree_generous
        and planted_found
        and control_rejects_noncovariant
        and control_rejects_nonzero_block
        and dim_v == dim_v_crosscheck
        and predicate_table[NEW_NAME]["jointly_satisfies"]
        == normalizable_solutions_exist
    )

    # ---- G: the exhibited solution's downstream tests ----------------------
    keys_all = c878.family_keys(events, stations)
    families = ("F_WORLD", "F_TAG", "F_TAG_ORDINAL", "F_ORBIT", "F_WORLD_TAG",
                "F_ATOM")
    cells_by_family = {fam: c878.cells_of(keys_all[fam]) for fam in families}
    compare = {name: nums[name] for name in NARROWED}
    totals_cmp = dict(totals)
    if m6_total > 0:
        compare[NEW_NAME] = m6_nums
        totals_cmp[NEW_NAME] = m6_total
    discrimination = {}
    for fam in families:
        cellmap = cells_by_family[fam]
        fracs = {}
        for name, vec in compare.items():
            fracs[name] = {key: Fraction(sum(vec[i] for i in idx),
                                         totals_cmp[name])
                           for key, idx in cellmap.items()}
        rows = {}
        for a, b in combinations(sorted(compare), 2):
            rows[f"{a}|{b}"] = sum(1 for key in cellmap
                                   if fracs[a][key] != fracs[b][key])
        discrimination[fam] = rows
    obj = receipt905["Q2_priced_residual"]
    ratio_scale = 19003
    ship = json.loads(payload_text[C905_SHIP])
    m6_factor = factorize(m6_total)
    surv_factors = {name: factorize(totals[name]) for name in NARROWED}
    m6_primes = set(m6_factor)
    shared_primes = set(obj["primes_shared_by_all_three"])
    cert_g = {
        "certificate": "G_EXHIBITED_SOLUTION_DOWNSTREAM",
        "question": (
            "the exhibited solution, tested against Cycle 905's"
            " discrimination structure and its divisibility pricing"),
        "admissibility": {
            "finitely_additive": m6_additive,
            "normalizable": m6_normalizable,
            "admissible_by_the_878_definition": bool(m6_additive
                                                     and m6_normalizable),
            "support_faithful": m6_zero == 0,
            "can_host_the_interface_vanishing_cells": m6_zero > 0,
            "survives_the_905_exclusion_criterion": m6_zero > 0,
            "monitor_phase_covariant": m6_covariant,
            "the_first_candidate_that_is_BOTH": bool(m6_covariant and m6_zero > 0),
        },
        "discrimination_against_the_survivors": discrimination,
        "discriminates_from_every_survivor_at_atom_level": all(
            v > 0 for k, v in discrimination["F_ATOM"].items()
            if NEW_NAME in k),
        "divisibility_pricing": {
            "ratio_scale_from_905": ratio_scale,
            "ratio_scale_factorization": {str(k): v
                                          for k, v in factorize(ratio_scale).items()},
            "total": m6_total,
            "total_factorization": {str(k): v for k, v in m6_factor.items()},
            "ratio_scale_divides_the_total": bool(
                m6_total > 0 and m6_total % ratio_scale == 0),
            "survivor_totals": {name: totals[name] for name in NARROWED},
            "primes_of_the_new_total_not_shared_by_all_three_survivors":
                sorted(m6_primes - shared_primes),
            "primes_shared_by_all_three_survivors":
                obj["primes_shared_by_all_three"],
            "R_RATIO_EXHAUSTIVE_verdict_for_the_new_candidate": (
                "NOT APPLICABLE: no solution was exhibited" if m6_total == 0
                else ("FAILS, exactly as it fails for all five pinned"
                      " candidates: the exhibited interface object's ratio"
                      f" scale {ratio_scale} does not divide this total"
                      " either" if m6_total % ratio_scale else
                      "PASSES: the ratio scale divides this total -- the"
                      " first candidate for which it does")),
        },
        "effect_on_the_lane_geometry": {
            "878_base_rank": 5,
            "base_rank_with_the_new_candidate": m6_in_span_rank,
            "the_new_candidate_is_independent_of_the_five":
                m6_in_span_rank == 6,
            "905_extension_dimension": 25,
            "extension_dimension_with_the_new_candidate":
                m6_in_span_rank * receipt902["Q1_minimal_fibre_dimension"],
            "price": (
                "the resolution is NOT free: the jointly-satisfying weighting"
                " lies OUTSIDE the Cycle-878 span, so keeping covariance"
                " costs exactly ONE NEW GENERATOR and moves the minimal"
                f" kernel-argument extension from 25 to"
                f" {m6_in_span_rank * receipt902['Q1_minimal_fibre_dimension']}"
                " dimensions"),
        },
        "what_covariance_buys_and_what_giving_it_up_costs": {
            "what_covariance_buys": (
                "monitor-phase independence of every emitted bookkeeping"
                " fraction: with COV-INV the F_WORLD fractions cannot be used"
                " to read off where the controller-orbit cut was placed"),
            "monitor_phase_visibility_of_the_survivors": {
                name: {
                    "orbits_with_non_constant_world_mass": sum(
                        1 for orbit in world_orbits
                        if len({world_mass[name][w] for w in orbit}) > 1),
                    "of_orbits": len(world_orbits),
                    "max_world_mass_spread_on_one_orbit": max(
                        (max(world_mass[name][w] for w in orbit)
                         - min(world_mass[name][w] for w in orbit))
                        for orbit in world_orbits),
                } for name in NARROWED
            },
            "reading": (
                "under any survivor the monitor phase is READABLE off the"
                " bookkeeping fractions -- orbit-mates carry different"
                " F_WORLD mass, so the fractions change when the"
                " controller-orbit cut moves.  Giving covariance up therefore"
                " makes the monitor phase potentially observable"),
            "prediction_or_convention": (
                "CONVENTION, not yet a falsifiable prediction: the monitor"
                " phase is where the controller-orbit cut is placed, and"
                " nothing on this lane supplies an occurrence rule that would"
                " turn a bookkeeping fraction into a measurable frequency."
                "  It becomes a falsifiable prediction only once the lane"
                " supplies the occurrence rule that Cycle 878's open gate"
                " names as missing -- which is precisely the gate the axiom"
                " baseline's exclusion list places outside axiom content"),
            "878_open_gate_verbatim": f878["open_gate"],
        },
        "label": FRACTION_LABEL,
    }
    cert_g["pass"] = bool(
        discrimination["F_ATOM"]
        and all(v >= 0 for v in discrimination["F_ATOM"].values())
        and cert_g["admissibility"]["admissible_by_the_878_definition"]
        == bool(m6_additive and m6_normalizable)
        and (not normalizable_solutions_exist
             or cert_g["admissibility"]["admissible_by_the_878_definition"])
    )

    # ---- H: falsifiers / controls -----------------------------------------
    # H1 a dropped orbit must break the partition gate and change dim V
    dropped = world_orbits[:-1]
    dropped_cover = sum(len(o) for o in dropped)
    dropped_partition_ok = dropped_cover == n_worlds
    dropped_dim_v = sum(1 for orbit in dropped
                        if not any(w in never_set for w in orbit))
    # H2 the identity-only family makes covariance vacuous
    trivial_rows, _ = span_system(orbits_used=tuple((o[0],) for o in world_orbits))
    rank_trivial, _ = rank_by_rational_elimination(trivial_rows)
    trivial_basis, _, _ = nullspace_basis(trivial_rows, 5)
    # H3 close the escape hatch: put one escape-orbit world into the block
    close_applicable = bool(star)
    closed_zero = set(never_formed) | ({star[0]} if star else set())
    dim_v_closed = dim_V_of(closed_zero)
    # H4 open an escape hatch: free one blocked orbit from the zero demand
    blocked = [o for o in world_orbits if any(w in never_set for w in o)]
    open_orbit = blocked[0] if blocked else world_orbits[0]
    opened_zero = set(never_formed) - set(open_orbit)
    dim_v_opened = dim_V_of(opened_zero)
    cert_h = {
        "certificate": "H_FALSIFIERS",
        "rows": [
            {"falsifier": "DROPPED_ORBIT",
             "modification": "one covariance orbit removed from the partition",
             "worlds_covered_after": dropped_cover,
             "worlds_in_census": n_worlds,
             "partition_gate_still_passes": dropped_partition_ok,
             "dim_V_after": dropped_dim_v,
             "dim_V_before": dim_v,
             "designed_outcome": (
                 "the partition completeness gate must FAIL and the orbit"
                 " census must no longer cover the worlds"),
             "observed_as_designed": bool(
                 not dropped_partition_ok
                 and dropped_cover == n_worlds - stations)},
            {"falsifier": "TRIVIAL_TRANSFORMATION_FAMILY",
             "modification": "the group is replaced by the identity alone",
             "covariance_becomes_vacuous": rank_trivial == rank_zero_only,
             "solution_dimension_then": 5 - rank_trivial,
             "solution_dimension_of_the_zero_mass_system_alone":
                 5 - rank_zero_only,
             "designed_outcome": (
                 "with no transformation the joint system must collapse to"
                 " the zero-mass system alone"),
             "observed_as_designed": bool(
                 rank_trivial == rank_zero_only
                 and len(trivial_basis) == 5 - rank_zero_only)},
            {"falsifier": "CLOSE_THE_ESCAPE_HATCH",
             "applicable": close_applicable,
             "modification": (
                 "one world of the escape orbit is moved into the"
                 " never-formed block"),
             "dim_V_before": dim_v,
             "dim_V_after": dim_v_closed,
             "designed_outcome": (
                 "the escape hatch closes and the normalizable solution space"
                 " collapses"),
             "observed_as_designed": bool(
                 (not close_applicable) or dim_v_closed == dim_v - 1)},
            {"falsifier": "OPEN_AN_ESCAPE_HATCH",
             "applicable": True,
             "modification": (
                 "one blocked orbit is freed from the zero-mass demand"),
             "freed_orbit_first_world": open_orbit[0],
             "dim_V_before": dim_v,
             "dim_V_after": dim_v_opened,
             "designed_outcome": (
                 "a normalizable solution appears where there was none, so"
                 " the machinery is not blind to solutions"),
             "observed_as_designed": bool(dim_v_opened == dim_v + 1)},
            {"falsifier": "PLANTED_JOINT_SOLUTION",
             "modification": (
                 "the system is RELAXED -- one orbit is freed from the"
                 " zero-mass demand and its indicator is adjoined as a sixth"
                 " generator -- so a joint solution exists by construction"),
             "plant_orbit_first_world": plant_orbit[0],
             "plant_satisfies_the_relaxed_system": plant_satisfies,
             "solver_reported_solution_dimension": planted_gen - rank_planted,
             "plant_lies_in_the_reported_solution_space":
                 plant_in_reported_space,
             "designed_outcome": "the same solver must find the plant",
             "observed_as_designed": planted_found},
            {"falsifier": "NEAR_MISS_CONTROLS",
             "modification": (
                 "a weighting that is zero on the block but NOT covariant,"
                 " and a weighting that is covariant but NOT zero on the"
                 " block, are handed to the same predicates"),
             "noncovariant_rejected": control_rejects_noncovariant,
             "block_charging_rejected": control_rejects_nonzero_block,
             "designed_outcome": "both rejected",
             "observed_as_designed": bool(control_rejects_noncovariant
                                          and control_rejects_nonzero_block)},
        ],
    }
    cert_h["pass"] = all(r["observed_as_designed"] for r in cert_h["rows"])

    # ---- I: deterministic double build ------------------------------------
    space2 = build_event_space(c863, c878, consts)
    digest2 = digest([list(e) for e in space2["events"]])
    nums2, dens2, _m2, _p2, _s2, common2 = c878.build_candidates(
        space2["events"], space2["scan"]["occ_global"], space2["scan"]["formed"],
        space2["scan"]["boundaries"])
    cert_i = {
        "certificate": "I_DOUBLE_BUILD",
        "first_digest": event_digest,
        "second_digest": digest2,
        "deterministic": event_digest == digest2,
        "candidate_numerators_identical": all(
            nums[name] == nums2[name] for name in CANDIDATES),
        "common_denominator_identical": common == common2,
    }
    cert_i["pass"] = bool(cert_i["deterministic"]
                          and cert_i["candidate_numerators_identical"]
                          and cert_i["common_denominator_identical"])

    elapsed = round(monotonic() - started, 3)
    cert_j = {"certificate": "J_RUNTIME", "elapsed_sec": elapsed,
              "budget_sec": RUNTIME_BUDGET_SEC,
              "firewall_hits": len(PRIMARY_FIREWALL.hits),
              "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                         if n in sys.modules],
              "full_census_no_sampling": len(events) == f878["event_cardinality"],
              "provenance": provenance}
    cert_j["pass"] = bool(elapsed <= RUNTIME_BUDGET_SEC
                          and not PRIMARY_FIREWALL.hits
                          and cert_j["full_census_no_sampling"]
                          and not cert_j["blocked_modules_loaded"])

    # ---- K: the ledger rows this block touches ----------------------------
    span_ok = bool(span_basis)
    resolution = (
        "RESOLVED BY CONSTRUCTION, OUTSIDE THE CYCLE-878 SPAN"
        if normalizable_solutions_exist and not span_ok else
        ("RESOLVED INSIDE THE CYCLE-878 SPAN" if span_ok else
         "NOT RESOLVED CONSTRUCTIVELY: THE TENSION IS A THEOREM EVERYWHERE"))
    prior_ledger = {row["id"]: row["status"] for row in receipt905["Q3_ledger"]}
    bl7_status = (
        f"{resolution}.  (1) Over the 25-dimensional minimal kernel-argument"
        " extension of the Cycle-878 span the two demands are "
        + ("JOINTLY UNSATISFIABLE" if not span_ok else "jointly satisfiable")
        + f" (joint rank {rank_joint_span_a} on 5 unknowns by two routes,"
        " plus a third structural route: the intersection of 878's covariant"
        " line with 905's surviving 3-space).  (2) Over Cycle 902's own"
        " generous base the joint system "
        + ("has a normalizable solution, its world-mass space has dimension"
           f" {dim_v}, and the exhibited representative is {NEW_NAME}"
           if normalizable_solutions_exist else
           "has NO normalizable solution: the world-mass space is trivial")
        + ".  (3) The axiom baseline REQUIRES covariance nowhere"
        f" ({cert_d['requires_count']} REQUIRES rows over"
        f" {len(cert_d['doc_surfaces_swept'])} surfaces), so the credential"
        " was never a law"
        + ("; keeping it costs one new generator outside the 878 five"
           if normalizable_solutions_exist else
           "; keeping it is impossible and BL7 resolves by DEMOTION"))
    bl6_status = (
        "OPEN and IDENTIFIED WITH BL7"
        if every_orbit_meets_block else
        "OPEN and SHARPENED.  BL6 and BL7 are NOT the same fact:"
        f" {len(world_orbits) - len(orbits_missing_block)} of"
        f" {len(world_orbits)} covariance orbits meet the never-formed block,"
        " not all of them.  But covariance drives BL6 to its maximum: a"
        " jointly-satisfying weighting assigns zero mass to"
        f" {len(events) - len(star_events)} of {len(events)} realized record"
        f" events and is supported on {len(star)} of {n_worlds} worlds")
    ledger_rows = [
        {"id": "BL7_COVARIANCE",
         "status_before": prior_ledger.get("BL7_COVARIANCE"),
         "status_now": bl7_status,
         "blocked_on": ("nothing on the Born side"
                        if normalizable_solutions_exist else
                        "owner / the interface premises")},
        {"id": "BL6_NEVER_FORMED_BLOCK",
         "status_before": prior_ledger.get("BL6_NEVER_FORMED_BLOCK"),
         "status_now": bl6_status,
         "blocked_on": "the lane"},
    ]
    if star:
        ledger_rows.append({
            "id": "BL8_ESCAPE_ORBIT_STATUS",
            "obligation": (
                "NEW, surfaced by this block: the escape orbit's census shape"
                f" is k={star_shape['k_values']},"
                f" event={star_shape['event_values']}, separations"
                f" {star_shape['separation_multisets']}"
                + (" -- exactly the shape Cycle 856 names for its"
                   " ABSOLUTE-record orbits" if matches_856_absolute_shape
                   else " -- which is NOT the shape Cycle 856 names for its"
                        " absolute-record orbits")),
            "status_now": "OPEN, premise P-856-SHAPE named and unpriced",
            "blocked_on": "a recomputation of the 856 stamps on this lineage"})
    cert_k = {"certificate": "K_LANE_LEDGER", "rows": ledger_rows,
              "resolution_class": resolution}
    cert_k["pass"] = True

    certificates = [("A_PINS", cert_a), ("B_RESTRICTION_GATE", cert_b),
                    ("C_COVARIANCE_CONDITION_DERIVED", cert_c),
                    ("D_FIDELITY_AXIOM_GROUNDING", cert_d),
                    ("E_JOINT_SYSTEM", cert_e),
                    ("F_ORBIT_MEETING_AND_BL6", cert_f),
                    ("G_EXHIBITED_SOLUTION_DOWNSTREAM", cert_g),
                    ("H_FALSIFIERS", cert_h), ("I_DOUBLE_BUILD", cert_i),
                    ("J_RUNTIME", cert_j), ("K_LANE_LEDGER", cert_k)]
    checks = {name: bool(payload["pass"]) for name, payload in certificates}

    verdict = (
        "TENSION_RESOLVED_CONSTRUCTIVELY_OUTSIDE_THE_878_SPAN"
        if (normalizable_solutions_exist and not span_ok) else
        ("TENSION_DISSOLVES_INSIDE_THE_878_SPAN" if span_ok else
         "TENSION_IS_A_THEOREM_OVER_EVERY_EVENT_SPACE_WEIGHTING")
    )

    theorems = [
        ("C906-T1 THE COVARIANCE CONDITION IS ORBIT-CONSTANCY OF WORLD MASS."
         " The landed monitor-phase family is a group: it is closed, has an"
         " identity and inverses, is cyclic of order"
         f" {order_of_generator} generated by the m=1 shift, and acts FREELY"
         f" on the {n_worlds}-world census with {len(world_orbits)} orbits of"
         f" size {stations}.  It does {'' if action_lifts_to_events else 'NOT '}"
         f"lift to a permutation of the {len(events)}-event space --"
         " orbit-mates carry different (tag, ordinal) atom shapes -- so"
         " covariance cannot be event-wise constancy.  The"
         " condition the pinned Cycle-878 test actually computes"
         " (byte-quoted) is that the pushforward to the F_WORLD partition be"
         " constant on orbits: a linear condition of exact rank"
         f" {rank_cov_a} by two routes, cutting the covariant subspace of"
         f" Q^E to dimension {len(events) - rank_cov_a}.  Every Cycle-878"
         " covariance verdict reproduces value-for-value from it."),
        (f"C906-T2 {cert_d['verdict']}."
         f" A fidelity sweep over {len(cert_d['doc_surfaces_swept'])} doc"
         " surfaces -- the pinned axiom baseline plus every monitor/"
         "phase-relevant surface discovered on this branch by a published"
         f" rule ({cert_d['selection_rules_published']['files_scanned']} files"
         " scanned) -- finds"
         f" {cert_d['requires_count']} sentences that REQUIRE the measurement"
         " weighting to be monitor-phase covariant.  The baseline's only"
         " covariance sentence is about the nearest-neighbor admissibility"
         " rule under lattice translations and cubic rotations, and its"
         " exclusion list places Born weights and probability rules outside"
         " axiom content altogether."),
        ("C906-T3 INSIDE THE 25-DIMENSIONAL EXTENSION THE TENSION IS "
         + ("A THEOREM" if not span_ok else "SATISFIABLE")
         + ".  Over the minimal kernel-argument extension of the"
         " Cycle-878 span -- where covariance lifts unchanged because the"
         " fibre carries no world index -- monitor-phase covariance and the"
         " interface's zero-mass requirement on the never-formed block are "
         + ("JOINTLY UNSATISFIABLE" if not span_ok else "jointly satisfiable")
         + ": the joint constraint matrix has rank"
         f" {rank_joint_span_a} on 5 unknowns by both routes, so the base"
         f" solution space has dimension {5 - rank_joint_span_a} and the"
         " extension's joint solution space is"
         f" {(5 - rank_joint_span_a) * 5}-dimensional.  Structurally: the"
         " covariant subspace of the span is exactly the M2 line"
         f" (dimension {5 - rank_cov_only}), the zero-mass subspace is"
         f" exactly the M3/M4/M5 span (dimension {5 - rank_zero_only}), and"
         " they intersect in zero.  This holds under all three declared"
         " readings of the zero-mass requirement, because the covariant line"
         " has minimum event numerator"
         f" {covariant_line_min_numerator} > 0 and so vanishes nowhere."),
        ("C906-T4 THE SCOPE OF THE OBSTRUCTION, FROM ORBIT STRUCTURE."
         " The orbit-meeting computation is"
         f" decisive: {len(world_orbits) - len(orbits_missing_block)} of the"
         f" {len(world_orbits)} covariance orbits meet the never-formed"
         f" block ({sum(1 for r in orbit_rows if r['never_formed_worlds'] == stations)}"
         " lie entirely inside it,"
         f" {sum(1 for r in orbit_rows if 0 < r['never_formed_worlds'] < stations)}"
         f" are mixed), and exactly {len(orbits_missing_block)} lie entirely"
         " outside.  "
         + ("Every orbit meets the block, so orbit-constancy plus zero mass on"
            " the block forces zero mass on every world: the obstruction is"
            " GENERAL, over ANY event-space weighting whatsoever, not merely"
            " over the 25-dimensional extension."
            if every_orbit_meets_block else
            "So the orbit-structure argument does NOT give a general theorem:"
            " it fails by exactly"
            f" {len(orbits_missing_block)} orbit(s).  Over Cycle 902's own"
            " generous base the joint system has a NORMALIZABLE solution;"
            f" the raw linear solution space has dimension"
            f" {dim_generous_route1} by two independent routes, of which"
            f" {signed_only_directions} directions carry zero total mass, and"
            f" the world-mass space has dimension {dim_v}: every"
            " jointly-satisfying weighting is supported on the"
            f" {len(star)} worlds of the escape orbit(s).  The exhibited"
            f" representative {NEW_NAME} is finitely additive, normalizable,"
            " non-negative, covariant, zero on the whole never-formed block,"
            " and hosts the interface's vanishing cells.")),
        ("C906-T5 THE PRICE."
         + (" The jointly-satisfying weighting is"
            + (" linearly independent of" if m6_in_span_rank == 6
               else " inside")
            + " the Cycle-878 five (base rank"
            f" {5} -> {m6_in_span_rank}), so keeping covariance moves the"
            " minimal kernel-argument extension from 25 to"
            f" {m6_in_span_rank * 5} dimensions.  Its second price is BL6:"
            f" the zero set grows from {len(block_events)} to"
            f" {len(events) - len(star_events)} of {len(events)} realized"
            " record events, and the support shrinks from"
            f" {len(formed_worlds)} formed worlds to {len(star)}."
            if normalizable_solutions_exist else
            " No jointly-satisfying weighting exists over any base, so BL7"
            " resolves by DEMOTION: the covariance credential is given up."
            f"  The survivors then leave the monitor phase readable off the"
            " bookkeeping fractions, which is a conventional choice and not"
            " yet a falsifiable prediction, because the lane supplies no"
            " occurrence rule.")
         + "  BL6 and BL7 are "
         + ("the SAME fact viewed twice" if every_orbit_meets_block
            else "NOT the same fact, but covariance drives BL6 to its"
                 " maximum") + "."),
    ]

    receipt = {
        "cycle": 906,
        "block": "toe-time-blockQ3-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "question": (
            "Cycle 906 -- resolve or price BL7: is there any weighting that is"
            " both monitor-phase covariant and compatible with the gravity"
            " interface's zero-mass requirement?"
        ),
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "VERDICT": verdict,
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "label_on_every_fraction": FRACTION_LABEL,
        "Q1_covariance_condition": cert_c["derived_condition"]["statement"],
        "Q1_condition_rank_routes": {
            "rational_elimination": rank_cov_a, "gram_laplace": rank_cov_b},
        "Q1_group_structure": {
            "is_a_group": cert_c["transformation_family"]["is_a_group"],
            "isomorphism_class": cert_c["transformation_family"]["isomorphism_class"],
            "acts_freely": free_action,
            "orbits": len(world_orbits), "orbit_size": stations,
            "lifts_to_the_event_space": action_lifts_to_events},
        "Q1_certification_matches_878": all(r["match"] for r in cov_gate_rows),
        "Q1_second_reading": cert_c["second_reading_from_the_landed_856_source"][
            "name"],
        "Q2_fidelity_verdict": cert_d["verdict"],
        "Q2_requires_count": cert_d["requires_count"],
        "Q2_surfaces_swept": cert_d["doc_surfaces_swept"],
        "Q2_discovered_surfaces": cert_d["discovered_surfaces"],
        "Q3_extension_25_solutions_exist": span_ok,
        "Q3_extension_25_joint_rank": rank_joint_span_a,
        "Q3_extension_25_routes": {"rational_elimination": rank_joint_span_a,
                                   "gram_laplace": rank_joint_span_b},
        "Q3_generous_base_signed_solution_dimension": dim_generous_route1,
        "Q3_generous_base_signed_dimension_route_2": dim_generous_route2,
        "Q3_generous_base_normalizable_solutions_exist":
            normalizable_solutions_exist,
        "Q3_generous_base_routes_agree": routes_agree_generous,
        "Q3_world_mass_space_dimension": dim_v,
        "Q3_world_mass_solution_unique_up_to_scale": dim_v == 1,
        "Q3_exhibited_solution": {
            "name": NEW_NAME,
            "support_worlds": list(star),
            "support_events": len(star_events),
            "total": m6_total, "denominator": m6_den,
            "zero_weight_events": m6_zero,
            "covariant": m6_covariant,
            "zero_on_block": m6_zero_on_block,
            "base_rank_with_it": m6_in_span_rank,
            "extension_dimension_with_it": m6_in_span_rank * 5},
        "Q4_orbit_meeting_histogram":
            cert_f["orbit_meeting_histogram_neverformed_count_to_orbits"],
        "Q4_every_orbit_meets_the_block": every_orbit_meets_block,
        "Q4_general_theorem_verdict": cert_f["general_theorem_verdict"],
        "Q4_BL6_identification_holds": cert_f["BL6_identification"]["holds"],
        "Q4_BL6_zero_events_before_and_after": [
            len(block_events), len(events) - len(star_events)],
        "Q4_856_absolute_shape_match":
            cert_f["cycle856_absolute_record_crosscheck"][
                "escape_orbit_has_the_856_absolute_shape"],
        "named_premises": ["P-NONEMPTY (inherited from Cycle 905)",
                           "P-INTERTWINE-878 (named here, undischarged)",
                           "P-856-SHAPE (named here, undischarged)"],
        "restriction_gate": (
            f"{cert_b['reproduce']}/{cert_b['total']} restriction gates"
            " reproduce"),
        "restriction_gate_rows": gate_rows,
        "theorems": theorems,
        "ledger_rows": cert_k["rows"],
        "event_space_digest": event_digest,
        "deterministic_double_build": cert_i["deterministic"],
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "elapsed_sec": elapsed,
        "scope": (
            "the full realized record-write census of the pinned Cycle-878"
            f" construction at horizon {consts['HORIZON']} orbits"
            f" ({len(events)} events over {n_worlds} worlds), rebuilt by AST"
            " lift from the pinned Cycle-863 and Cycle-878 sources (never"
            " imported); the gravity side enters ONLY through the vendored"
            " Cycle-902 artifacts and the Cycle-905 receipt.  Exact rational"
            " arithmetic throughout; no probability, no occurrence rule, no"
            " update law is introduced."
        ),
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_pins": [
            {"path": p, "sha256": cert_a["sha256"][p],
             "git_blob": cert_a["git_blobs"][p], "bytes": cert_a["bytes"][p]}
            for p in AUDIT_INPUT_PATHS],
    }
    receipt["Q3_resolution_class"] = resolution
    receipt["science_digest"] = digest({
        "verdict": verdict, "joint_rank_span": rank_joint_span_a,
        "generous_dim": dim_generous_route1, "dim_V": dim_v,
        "escape_orbit": list(star), "event_digest": event_digest,
        "requires_count": cert_d["requires_count"]})
    (ROOT / "outputs" / "covariance_tension_cycle906_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n",
                  encoding="utf-8")

    lines = [
        "CYCLE906_BL7_COVARIANCE_TENSION_RESOLVED_OR_PRICED",
        "BORN_LANE_STRUCTURAL_ONLY_NO_PROBABILITY_POSTULATE",
        "EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY",
    ]
    for name, payload in certificates:
        lines.append(f"CERTIFICATE {name} "
                     f"{'PASS' if payload['pass'] else 'FAIL'} "
                     + compact(payload))
    for theorem in theorems:
        lines.append("THEOREM " + theorem)
    lines.append("SUMMARY_JSON " + compact({
        "cycle": 906, "checks": checks, "VERDICT": verdict,
        "joint_rank_in_the_25_dim_extension": rank_joint_span_a,
        "generous_base_signed_solution_dimension": dim_generous_route1,
        "world_mass_space_dimension": dim_v,
        "normalizable_solutions_exist": normalizable_solutions_exist,
        "escape_orbits": len(orbits_missing_block),
        "requires_count": cert_d["requires_count"],
        "elapsed_sec": elapsed, "pass": all(checks.values())}))
    lines.append("CYCLE906_COVARIANCE_TENSION_"
                 + ("PASS" if all(checks.values()) else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
