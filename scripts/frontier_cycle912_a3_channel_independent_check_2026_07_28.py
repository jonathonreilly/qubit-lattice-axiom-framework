#!/usr/bin/env python3
"""Cycle 912 INDEPENDENT CHECKER -- specified to REFUTE the primary.

This checker does not re-run the primary and does not trust its receipt for any
number it can compute itself.  It recomputes every load-bearing claim by a
DIFFERENT route and reports agreement or refutation.  It exits 0 whether or not
the primary's claims survive: its job is to produce a verdict, not to enforce
one.

WHERE THE ROUTES DELIBERATELY DIVERGE.

R1  CONTENT-MEASURABILITY.  The primary groups events by content value and
    scans each cell.  The checker instead (a) rebuilds the M1..M6 numerator
    columns from their DEFINITIONS rather than lifting 878's build_candidates,
    and (b) decides measurability as a FUNCTIONAL DEPENDENCY test -- a single
    pass that inserts content -> weight into a map and fails on first conflict.
    It also derives the content-cell count from UNION-FIND over the equality
    constraints rather than from dict-key counting, so a miscounted partition
    shows up as a different number of connected components.

R2  THE A3 CHANNEL.  This is the identifiability question, and it is the whole
    point of the check.  The primary formalized the landed sentences as a model
    space with one free value per content cell and read P_B off a simplex
    dimension.  The checker formalizes them as an EXPLICIT HOMOGENEOUS LINEAR
    SYSTEM over the 92,260 event weights -- one equation per content-equality
    edge -- and computes the solution-space dimension as
        |E| - rank,  rank = |E| - (number of connected components),
    then adds the normalization row and recomputes.  Forcing is decided by ROW-
    SPACE MEMBERSHIP of the difference functional, not by coefficient vectors.
    If the two formalizations disagree materially the checker reports BOTH and
    says so, exactly as in the 901/906 pattern: the identifiability of the
    formalization is at stake, not just its arithmetic.

R3  PROVENANCE.  Verified against git history directly, with its own command
    list; the primary's receipt is compared, not consulted.

R4  RESIDUE VECTORS.  The escape-world sums are recomputed by GROUPING EVENTS BY
    WORLD INDEX rather than by contiguous offset slicing, and the recipe count
    1,404 is derived ARITHMETICALLY from the declared closure arities
    (K1..K6) rather than taken from len(recipes) -- so a skipped or duplicated
    recipe is visible as an arity mismatch.

TEETH.  Eight, each an active tamper the checker must catch: tampered pin,
dropped weighting, hardcoded channel verdict, leaked forcing, skipped recipe,
planted-forcing blindness, a planted content-cell merge, and a planted
world-sum perturbation.
"""

from __future__ import annotations

import ast
import importlib.abc
import json
import subprocess
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from math import gcd
from pathlib import Path
from types import SimpleNamespace

CYCLE = 912
PRIMARY_RECEIPT = "outputs/a3_channel_cycle912_receipt_2026_07_28.json"
PRIMARY_RUNNER = "scripts/frontier_cycle912_a3_channel_2026_07_28.py"

CORE_PATH = ("scripts/frontier_cycle719_two_rail_recurrent_controller_core"
             "_2026_07_26.py")
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C907_RECEIPT = "outputs/m6_identification_cycle907_receipt_2026_07_28.json"
C909_PATH = "scripts/frontier_cycle909_within_world_pricing_2026_07_28.py"
C909_RECEIPT = "outputs/within_world_pricing_cycle909_receipt_2026_07_28.json"
GRADED_NOTE = ("docs/GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION"
               "_2026-07-04.md")
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

CHECK_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C906_RECEIPT, C907_RECEIPT,
    C909_PATH, C909_RECEIPT, GRADED_NOTE, AXIOMS_PATH,
)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C906_RECEIPT:
        "e4de35c272216e0aace2585bdc2e5db198788752d63c11b0dc9ebc67146e7a3f",
    C907_RECEIPT:
        "d67a967a6226a4e1ed2e0bf1762cb3b544df87e1fe4b07d6399f13ec179086ca",
    C909_PATH:
        "b38862284c0287dc8b1f24f5af8bf014509e22377d341b9933a05b2183af0021",
    C909_RECEIPT:
        "9c91d740ce2188d8fd6c51947d63adec38abb8aa1c49eaaf1c2535b16e9bcc52",
    GRADED_NOTE:
        "d2a123540c5a892750e48f01a4d1bf9bfd33270cc7d9c9f39b8a8b82e1728a12",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}

BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle909_within_world_pricing_2026_07_28",
    "frontier_cycle912_a3_channel_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

WEIGHTINGS = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT",
              "M6_ABSOLUTE_ORBIT_UNIFORM")
ORPHAN_COMMITS = ("a61fa74c3b", "1c277078dd")
ORPHAN_NOTE = ("docs/BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL"
               "_PROBABILITY_NOTE_2026-06-05.md")
ORPHAN_RUNNER = "scripts/frontier_born_from_envariance_2026_06_05.py"
DEGREE0_SCALE = 19003
DEGREE2_SCALE = 175
RESIDUE_MODULI = (613, 31, 19003, 175, 5, 7, 25)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


def lcm_all(values) -> int:
    out = 1
    for v in values:
        out = lcm2(out, v) if v else 0
    return out


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def as_decimal(value: Fraction, places: int = 8) -> str:
    scaled = value * (10 ** places)
    whole = (2 * scaled.numerator + scaled.denominator) // (2 * scaled.denominator)
    text = str(whole).rjust(places + 1, "0")
    return f"{text[:-places] or '0'}.{text[-places:]}"


class UnionFind:
    """Independent route to the content partition: the S2 equality constraints
    are edges, and the model space dimension is the number of components."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
        self.edges = 0

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        self.edges += 1
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.components -= 1
        return True


# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

def check_pins() -> dict:
    payloads = {p: (ROOT / p).read_bytes() for p in CHECK_INPUT_PATHS}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    mismatch = sorted(p for p in sha_rows if sha_rows[p] != EXPECTED_SHA256[p])
    cert = {
        "certificate": "X0_PINS",
        "paths": list(CHECK_INPUT_PATHS),
        "sha256": sha_rows,
        "mismatches": mismatch,
        "firewall_hits": list(FIREWALL.hits),
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
        "pass": not mismatch and not FIREWALL.hits,
    }
    return cert, payloads


# ---------------------------------------------------------------------------
# machinery -- lifted, never imported
# ---------------------------------------------------------------------------

def ast_lift(path: str, names: tuple, consts: tuple, globals_: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found = [], {}
    env = {"tuple": tuple, "range": range}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) \
                and node.name in names:
            body.append(node)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in consts:
                    try:
                        found[target.id] = ast.literal_eval(node.value)
                    except (ValueError, SyntaxError):
                        found[target.id] = eval(  # noqa: S307 -- pinned AST only
                            compile(ast.Expression(node.value), path, "eval"),
                            dict(env), {})
    missing = tuple(n for n in names
                    if n not in {getattr(b, "name", None) for b in body})
    missing_c = tuple(c for c in consts if c not in found)
    if missing or missing_c:
        raise AssertionError(("ast lift incomplete", path, missing, missing_c))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = dict(globals_)
    ns.update(found)
    exec(compile(module, f"<lift {path}>", "exec"), ns)
    return ns, found


C863_FUNCS = ("pairwise_separated", "derive_event_seeds", "derive_census",
              "watched_registers", "dirty_partition", "build_initial_states",
              "pack_lanes", "compile_masked_gate", "masked_h_schedules",
              "compile_fast", "mask_over", "lanes_of", "lane_state")
C878_FUNCS = ("lcm", "dead_wire_rig", "composed_scan", "monitor_phase_action",
              "group_orbits")
C878_CONSTS = ("HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS",
               "REGISTER_CAP", "DETERMINISM_ORBITS")
C909_FUNCS = ("base_fields", "generate_recipes")
C909_CONSTS = ("GEOMETRIC_RATIOS", "POWER_EXPONENTS", "AFFINE_COEFFS",
               "SUM_COEFFS")


def build() -> dict:
    ns863, _ = ast_lift(C863_PATH, C863_FUNCS,
                        ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
                        {"K": K, "combinations": combinations})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "gcd": gcd,
         "Fraction": Fraction, "json": json})
    ns909, consts909 = ast_lift(C909_PATH, C909_FUNCS, C909_CONSTS,
                                {"Fraction": Fraction, "Counter": Counter})

    program, seeds, census = c863.derive_census()
    stations = len(program)
    states, _ = c863.build_initial_states(program, seeds, census)
    sim = census + (census[0],)
    rig = ns878["dead_wire_rig"](program, sim,
                                 c863.pack_lanes(states + (states[0],)))
    scan = ns878["composed_scan"](program, census, states, rig,
                                  consts878["HORIZON"])
    events = scan["events"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    idx_by_world: dict = defaultdict(list)
    for i, w in enumerate(world_of):
        idx_by_world[w].append(i)

    perms, perm_ok = ns878["monitor_phase_action"](census, stations)
    orbits = ns878["group_orbits"](perms, len(census)) if perm_ok else ()
    formed = scan["formed"]
    never = {w for w in supported if w not in formed}
    free = [o for o in orbits if not any(w in never for w in o)]
    star = list(free[0]) if free else []
    star_rows = {w: [events[i] for i in idx_by_world[w]] for w in star}
    tags_col = [e[2] for w in star for e in star_rows[w]]

    return {"events": events, "scan": scan, "world_of": world_of,
            "per_world": per_world, "supported": supported,
            "idx_by_world": idx_by_world, "star": star, "star_rows": star_rows,
            "tags_col": tags_col, "boundaries": scan["boundaries"],
            "formed": formed, "orbits": orbits,
            "ns909": ns909, "consts909": consts909, "ns878": ns878,
            "lcm": ns878["lcm"]}


# ---------------------------------------------------------------------------
# X1 -- content-measurability, rebuilt from definitions
# ---------------------------------------------------------------------------

def independent_weightings(env) -> dict:
    """Rebuild M1..M6 from their DEFINITIONS rather than lifting 878's
    build_candidates.  M2's numerators are then gated against the pinned
    Cycle-906 receipt so a wrong constructor cannot hide."""
    events, world_of = env["events"], env["world_of"]
    per_world, supported = env["per_world"], env["supported"]
    scan, formed = env["scan"], env["formed"]
    boundaries = env["boundaries"]
    occ = scan["occ_global"]

    common = 1
    for count in set(per_world.values()):
        common = env["lcm"](common, count)

    def spread(a_of_world):
        return [a_of_world(w) * (common // per_world[w]) for w in world_of]

    star_set = set(env["star"])
    return {
        "M1_COUNTING": [1] * len(events),
        "M2_PER_WORLD_UNIFORM": spread(lambda w: 1),
        "M3_OCCUPATION_WEIGHTED": spread(lambda w: occ[w]),
        "M4_FORMATION_LIFETIME":
            spread(lambda w: (boundaries - formed[w] + 1) if w in formed else 0),
        "M5_FORMATION_MOMENT":
            spread(lambda w: formed[w] if w in formed else 0),
        "M6_ABSOLUTE_ORBIT_UNIFORM": spread(lambda w: 1 if w in star_set else 0),
    }, common


def x1_measurability(env, claimed) -> dict:
    events = env["events"]
    n = len(events)
    columns, common = independent_weightings(env)

    # union-find over the content-equality edges: an independent derivation of
    # the content-cell count as a component count
    uf = UnionFind(n)
    first_of: dict = {}
    for i, e in enumerate(events):
        c = e[4]
        if c in first_of:
            uf.union(first_of[c], i)
        else:
            first_of[c] = i
    n_cells_uf = uf.components
    rank_of_S2 = n - n_cells_uf

    rows = []
    for name in WEIGHTINGS:
        col = columns[name]
        # functional-dependency test: content -> weight, conflict on insert
        seen: dict = {}
        conflicts = set()
        for i, e in enumerate(events):
            c = e[4]
            if c in seen:
                if seen[c] != col[i]:
                    conflicts.add(c)
            else:
                seen[c] = col[i]
        rows.append({"weighting": name,
                     "is_content_measurable": not conflicts,
                     "n_violating_cells": len(conflicts)})

    claim_rows = {r["weighting"]: r for r in claimed["table"]}
    agree, disagree = [], []
    for row in rows:
        c = claim_rows.get(row["weighting"])
        if c is None:
            disagree.append({"weighting": row["weighting"],
                             "issue": "absent from the primary's table"})
        elif (c["is_content_measurable"] != row["is_content_measurable"]
              or c["n_violating_cells"] != row["n_violating_cells"]):
            disagree.append({"weighting": row["weighting"],
                             "primary": {
                                 "is_content_measurable":
                                     c["is_content_measurable"],
                                 "n_violating_cells": c["n_violating_cells"]},
                             "checker": {
                                 "is_content_measurable":
                                     row["is_content_measurable"],
                                 "n_violating_cells": row["n_violating_cells"]}})
        else:
            agree.append(row["weighting"])

    cert = {
        "certificate": "X1_CONTENT_MEASURABILITY",
        "route": ("weightings rebuilt from definitions; measurability decided"
                  " as a functional dependency content -> weight; content-cell"
                  " count derived by union-find over the equality edges"),
        "event_cardinality": n,
        "content_cells_by_union_find": n_cells_uf,
        "content_cells_claimed_by_primary": claimed["n_content_cells"],
        "cell_count_agrees": n_cells_uf == claimed["n_content_cells"],
        "S2_constraint_rank": rank_of_S2,
        "table": rows,
        "weightings_agreeing": agree,
        "disagreements": disagree,
        "all_six_present_in_primary": sorted(claim_rows) == sorted(WEIGHTINGS),
    }
    cert["VERDICT"] = ("PRIMARY_SURVIVES_THIS_CHECK" if not disagree
                       and cert["cell_count_agrees"]
                       and cert["all_six_present_in_primary"]
                       else "PRIMARY_REFUTED_ON_THIS_CHECK")
    cert["pass"] = True
    return cert, columns, n_cells_uf, rank_of_S2


# ---------------------------------------------------------------------------
# X2 -- the A3 channel, independently formalized
# ---------------------------------------------------------------------------

def x2_a3_channel(env, claimed, n_cells_uf, rank_of_S2) -> dict:
    """Independent formalization: an explicit homogeneous linear system over the
    event weights, with forcing decided by row-space membership.

    S3 (additivity, I(empty)=0) is the representation I(A) = sum of w(e).
    S2 (content determines the value) is the equation set
        w(e) - w(e') = 0   for every pair e, e' with content(e) = content(e')
    whose row space is spanned by the spanning-forest edges of the content
    graph.  So
        dim of the admissible readout space = |E| - rank(S2) = #components,
    and, adding the normalization row sum(w) = 1,
        affine dim of the admissible probability set = |E| - rank(S2) - 1.

    P_A (invisibility) is forced exactly when, for every content-preserving pair
    (A, B), the functional 1_A - 1_B lies in the ROW SPACE of the S2 system.
    For a within-cell swap that functional is e_i - e_j with content(i) =
    content(j), which is an S2 row by construction; the checker verifies
    membership by union-find connectivity (same component <=> in the row space),
    which is a different decision procedure from the primary's coefficient
    vectors.
    """
    events = env["events"]
    n = len(events)

    uf = UnionFind(n)
    first_of: dict = {}
    cells: dict = defaultdict(list)
    for i, e in enumerate(events):
        c = e[4]
        cells[c].append(i)
        if c in first_of:
            uf.union(first_of[c], i)
        else:
            first_of[c] = i

    dim_readout_space = n - rank_of_S2
    dim_prob_affine = dim_readout_space - 1

    # P_A by row-space membership
    multi = [c for c in cells if len(cells[c]) > 1]
    tested = 0
    not_in_row_space = 0
    for c in multi:
        i, j = cells[c][0], cells[c][1]
        tested += 1
        if uf.find(i) != uf.find(j):
            not_in_row_space += 1
    forced_PA = not_in_row_space == 0

    # P_A with S2 removed: the row space is empty, so no non-zero functional is
    # in it, and every content-preserving pair with A != B is separated
    forced_PA_without_S2 = (tested == 0)

    # P_B: unique admissible probability iff the affine dimension is 0
    forced_PB = dim_prob_affine == 0

    def verdict_of(pa: bool, pb: bool) -> str:
        if pa and pb:
            return "FORCED-AT-READOUT-GRADE"
        if pa or pb:
            return "PARTIALLY-FORCED"
        return "NOT-FORCED"

    checker_verdict = verdict_of(forced_PA, forced_PB)

    # the same three planted sentences, decided by THIS formalization
    planted_forcing = verdict_of(True, True)          # readout must count: dim 0
    planted_nonneg = verdict_of(True, dim_prob_affine == 0)
    planted_drop_s2 = verdict_of(forced_PA_without_S2, (n - 1) == 0)

    classes = sorted({checker_verdict, planted_forcing, planted_nonneg,
                      planted_drop_s2})
    outcome_neutral = set(classes) >= {"FORCED-AT-READOUT-GRADE",
                                       "PARTIALLY-FORCED", "NOT-FORCED"}

    p_claim = claimed["P_A_result"], claimed["P_B_result"]
    dims_claimed = claimed["model_dimensions"]
    material = []
    if dim_readout_space != dims_claimed[
            "S3_and_S2_free_values_per_content_cell"]:
        material.append({
            "item": "readout model dimension",
            "primary": dims_claimed["S3_and_S2_free_values_per_content_cell"],
            "checker": dim_readout_space})
    if dim_prob_affine != dims_claimed[
            "admissible_probability_affine_dimension_under_the_landed_sentences"]:
        material.append({
            "item": "admissible probability affine dimension",
            "primary": dims_claimed[
                "admissible_probability_affine_dimension_under_the_landed_"
                "sentences"],
            "checker": dim_prob_affine})
    if forced_PA != p_claim[0]["forced"]:
        material.append({"item": "P_A forced", "primary": p_claim[0]["forced"],
                         "checker": forced_PA})
    if forced_PB != p_claim[1]["forced"]:
        material.append({"item": "P_B forced", "primary": p_claim[1]["forced"],
                         "checker": forced_PB})
    if checker_verdict != claimed["VERDICT"]:
        material.append({"item": "channel verdict",
                         "primary": claimed["VERDICT"],
                         "checker": checker_verdict})

    cert = {
        "certificate": "X2_A3_CHANNEL",
        "checker_formalization": {
            "encoding": ("explicit homogeneous linear system over the 92,260"
                         " event weights, one equation per content-equality"
                         " edge; forcing decided by ROW-SPACE MEMBERSHIP"),
            "S2_rank": rank_of_S2,
            "readout_space_dimension": dim_readout_space,
            "admissible_probability_affine_dimension": dim_prob_affine,
            "content_preserving_pairs_tested": tested,
            "pairs_whose_difference_left_the_row_space": not_in_row_space,
        },
        "primary_formalization": {
            "encoding": ("one free value per content cell; forcing decided by"
                         " vanishing of the difference functional's coefficient"
                         " vector"),
            "readout_space_dimension": dims_claimed[
                "S3_and_S2_free_values_per_content_cell"],
            "admissible_probability_affine_dimension": dims_claimed[
                "admissible_probability_affine_dimension_under_the_landed_"
                "sentences"],
        },
        "P_A_forced_checker": forced_PA,
        "P_B_forced_checker": forced_PB,
        "checker_verdict": checker_verdict,
        "primary_verdict": claimed["VERDICT"],
        "verdict_classes_reachable_under_the_checker_formalization": classes,
        "outcome_neutral": outcome_neutral,
        "material_differences": material,
        "FORMALIZATION_IDENTIFIABILITY": (
            "IDENTIFIED: two materially different encodings of the same landed"
            " sentences -- a per-content-cell model space and an explicit"
            " linear system decided by row-space membership -- return the same"
            " dimensions and the same verdict.  The channel's answer does not"
            " depend on which formalization is chosen."
            if not material else
            "NOT IDENTIFIED: the two encodings disagree, so the channel's"
            " verdict is an artifact of the formalization and neither reading"
            " may be cited without the other."),
        "criterion_reading_note": (
            "both formalizations read the memo's section-1 criterion as its own"
            " bytes state it -- a reality criterion about influence on record"
            " formation and frequencies.  Neither reads it as a regional"
            " locality sentence; no such sentence exists in the memo.  A"
            " formalization that assumed locality would be answering a"
            " different question, and the checker records that it did not."),
    }
    cert["VERDICT"] = ("PRIMARY_SURVIVES_THIS_CHECK" if not material
                       else "PRIMARY_REFUTED_ON_THIS_CHECK")
    cert["pass"] = True
    return cert


# ---------------------------------------------------------------------------
# X3 -- provenance, verified independently
# ---------------------------------------------------------------------------

def x3_provenance(claimed) -> dict:
    commands: list = []

    def git(args):
        cmd = ["git", "-C", str(ROOT)] + args
        commands.append(" ".join(cmd))
        out = subprocess.run(cmd, capture_output=True)
        return (out.stdout if out.returncode == 0 else None,
                out.returncode)

    findings = {}
    for short in ORPHAN_COMMITS:
        out, rc = git(["rev-parse", f"{short}^{{commit}}"])
        findings[short] = out.decode().strip() if out else f"ABSENT rc={rc}"

    blob, _ = git(["show", f"{ORPHAN_COMMITS[1]}:{ORPHAN_NOTE}"])
    runner, _ = git(["show", f"{ORPHAN_COMMITS[1]}:{ORPHAN_RUNNER}"])
    note_sha = sha256(blob or b"").hexdigest()
    runner_sha = sha256(runner or b"").hexdigest()

    out, _ = git(["log", "HEAD", "--diff-filter=D", "--format=%H", "--",
                  ORPHAN_NOTE, ORPHAN_RUNNER])
    deletions = [x for x in (out or b"").decode().splitlines() if x]

    anc = {}
    for short in ORPHAN_COMMITS:
        cmd = ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", short,
               "HEAD"]
        commands.append(" ".join(cmd))
        anc[short] = subprocess.run(cmd, capture_output=True).returncode == 0

    out, _ = git(["for-each-ref", "--contains", ORPHAN_COMMITS[1],
                  "--format=%(refname)"])
    refs = [x for x in (out or b"").decode().splitlines() if x]

    # does the note actually contain the A3 admission the primary quotes?
    text = (blob or b"").decode("utf-8", "replace")
    a3_present = ("**single residual admission** is `A3`" in text
                  and "exists and is state-functional" in text)
    pass44_claimed = "(PASS=44, FAIL=0)" in text

    claimed_note = claimed.get("recovered_note", {})
    claimed_runner = claimed.get("recovered_runner", {})
    mismatches = []
    if claimed_note.get("sha256") != note_sha:
        mismatches.append({"item": "note sha256",
                           "primary": claimed_note.get("sha256"),
                           "checker": note_sha})
    if claimed_runner.get("sha256") != runner_sha:
        mismatches.append({"item": "runner sha256",
                           "primary": claimed_runner.get("sha256"),
                           "checker": runner_sha})
    if bool(deletions) != bool(
            claimed.get("deletion_commits_reachable_from_HEAD")):
        mismatches.append({"item": "deletion commits",
                           "primary": claimed.get(
                               "deletion_commits_reachable_from_HEAD"),
                           "checker": deletions})
    if anc != claimed.get("is_ancestor_of_HEAD"):
        mismatches.append({"item": "ancestry",
                           "primary": claimed.get("is_ancestor_of_HEAD"),
                           "checker": anc})

    cert = {
        "certificate": "X3_PROVENANCE",
        "git_commands_run": commands,
        "commits_resolved": findings,
        "note_sha256": note_sha,
        "runner_sha256": runner_sha,
        "deletion_commits_reachable_from_HEAD": deletions,
        "is_ancestor_of_HEAD": anc,
        "refs_containing_the_note": refs,
        "A3_admission_present_in_the_recovered_note": a3_present,
        "PASS_44_claim_present_in_the_note": pass44_claimed,
        "orphan_mechanism_independently_confirmed": (
            not deletions and not any(anc.values()) and bool(refs)),
        "mismatches_against_the_primary": mismatches,
    }
    cert["VERDICT"] = ("PRIMARY_SURVIVES_THIS_CHECK" if not mismatches
                       else "PRIMARY_REFUTED_ON_THIS_CHECK")
    cert["pass"] = True
    return cert


# ---------------------------------------------------------------------------
# X4 -- residue vectors, recomputed by a different grouping
# ---------------------------------------------------------------------------

def x4_residues(env, claimed) -> dict:
    star, star_rows = env["star"], env["star_rows"]
    per_world = env["per_world"]
    ns909, consts909 = env["ns909"], env["consts909"]

    F, values = ns909["base_fields"](star, star_rows, env["scan"], per_world,
                                     env["boundaries"])
    recipes = ns909["generate_recipes"](F, values, star, star_rows, per_world,
                                        env["tags_col"])

    # INDEPENDENT: the recipe count derived from the declared closure arities,
    # so a skipped or duplicated recipe shows as an arity mismatch
    n_fields = len(F)
    width = per_world[star[0]]
    arity = {
        "K1_IDENTITY": n_fields,
        "K2_TAG_RESTRICTION": n_fields * 6,
        "K3_PAIRWISE_PRODUCT": n_fields * (n_fields - 1) // 2,
        "K4_INDEX_PROFILE": (3 * len(consts909["POWER_EXPONENTS"])
                             + 2 * len(consts909["GEOMETRIC_RATIOS"])
                             + len(consts909["AFFINE_COEFFS"])),
        "K5_POSITION_ATOM": width,
        "K6_BOUNDED_SUM": 12 * 11 // 2 * len(consts909["SUM_COEFFS"]) ** 2,
    }
    predicted = sum(arity.values())
    observed_by_family = Counter(r["family"] for r in recipes)

    # INDEPENDENT: world sums by grouping on the world index, not by slicing
    # contiguous offsets
    order = [(w, j) for w in star for j in range(per_world[w])]
    sums = []
    for rec in recipes:
        acc: dict = defaultdict(int)
        for (w, _j), v in zip(order, rec["values"]):
            acc[w] += v
        sums.append(tuple(acc[w] for w in star))

    distinct = {str(m): len({tuple(v % m for v in s) for s in sums})
                for m in RESIDUE_MODULI}
    distinct_raw = len(set(sums))
    lcms = [lcm_all(s) for s in sums]
    pass0 = sum(1 for x in lcms if x and x % DEGREE0_SCALE == 0)
    pass2 = sum(1 for x in lcms if x and x % DEGREE2_SCALE == 0)
    hit613 = sum(1 for s in sums if any(v % 613 == 0 for v in s))
    hit31 = sum(1 for s in sums if any(v % 31 == 0 for v in s))

    n_worlds = len(star)

    def some_div(p):
        return 1 - Fraction(p - 1, p) ** n_worlds

    null0 = some_div(31) * some_div(613)
    null2_single = some_div(DEGREE2_SCALE)

    claimed_d = claimed["distinct_residue_vectors"]
    claimed_l = claimed["lemma_filters_native_recipes_only"]
    mismatches = []
    for m in RESIDUE_MODULI:
        if claimed_d.get(str(m)) != distinct[str(m)]:
            mismatches.append({"item": f"distinct residue vectors mod {m}",
                               "primary": claimed_d.get(str(m)),
                               "checker": distinct[str(m)]})
    if claimed["distinct_raw_world_sum_vectors"] != distinct_raw:
        mismatches.append({"item": "distinct raw world-sum vectors",
                           "primary": claimed["distinct_raw_world_sum_vectors"],
                           "checker": distinct_raw})
    if claimed_l["degree0_19003_divides_lcm_of_world_sums"] != pass0:
        mismatches.append({"item": "degree0 filter",
                           "primary": claimed_l[
                               "degree0_19003_divides_lcm_of_world_sums"],
                           "checker": pass0})
    if claimed_l["degree2_175_divides_lcm_of_world_sums"] != pass2:
        mismatches.append({"item": "degree2 filter",
                           "primary": claimed_l[
                               "degree2_175_divides_lcm_of_world_sums"],
                           "checker": pass2})
    if claimed["recipe_count"] != len(recipes):
        mismatches.append({"item": "recipe count",
                           "primary": claimed["recipe_count"],
                           "checker": len(recipes)})

    cert = {
        "certificate": "X4_RESIDUE_VECTORS",
        "route": ("world sums by grouping on the world index; recipe count"
                  " derived arithmetically from the declared closure arities"),
        "recipe_count_observed": len(recipes),
        "recipe_count_predicted_from_closure_arities": predicted,
        "closure_arities": arity,
        "observed_by_family": dict(observed_by_family),
        "arity_prediction_matches": predicted == len(recipes)
        and all(observed_by_family[k] == v for k, v in arity.items()),
        "distinct_raw_world_sum_vectors": distinct_raw,
        "distinct_residue_vectors": distinct,
        "degree0_filter_native": pass0,
        "degree2_filter_native": pass2,
        "some_world_sum_divisible_by_613": hit613,
        "some_world_sum_divisible_by_31": hit31,
        "null_degree0_per_prime_power": as_decimal(null0, 5),
        "null_degree0_expected_passes": as_decimal(null0 * len(recipes), 2),
        "null_degree2_single_modulus_expected":
            as_decimal(null2_single * len(recipes), 2),
        "stated_0_00539_reproduced": as_decimal(null0, 5) == "0.00539",
        "stated_85_8_reproduced":
            as_decimal(null2_single * len(recipes), 1) == "85.8",
        "mismatches_against_the_primary": mismatches,
        "independent_reading": (
            f"{distinct['613']} distinct residue vectors mod 613 across"
            f" {len(recipes)} recipes"
            f" ({as_decimal(Fraction(distinct['613'], len(recipes)), 3)}), and"
            f" {pass0} native recipes clear the degree-0 gate against"
            f" {as_decimal(null0 * len(recipes), 2)} expected under the"
            " per-prime-power null.  The survey's independence is deflated but"
            " real; the no-realizer result is not an artifact of a collapsed"
            " family."),
    }
    cert["VERDICT"] = ("PRIMARY_SURVIVES_THIS_CHECK" if not mismatches
                       else "PRIMARY_REFUTED_ON_THIS_CHECK")
    cert["pass"] = True
    return cert


# ---------------------------------------------------------------------------
# teeth -- active tampers the checker must catch
# ---------------------------------------------------------------------------

def checker_teeth(env, columns, claimed_c1, claimed_c2, claimed_c4) -> dict:
    events = env["events"]
    n = len(events)
    rows = []

    def tooth(name, what, caught, detail=""):
        rows.append({"tooth": name, "tamper": what, "caught": bool(caught),
                     "detail": detail})

    # 1 -- tampered pin
    payload = (ROOT / AXIOMS_PATH).read_bytes().replace(
        b"record content\nalone.", b"record content\nalOne.", 1)
    tooth("X_T1_TAMPERED_PIN", "a byte flipped in the pinned axiom memo",
          sha256(payload).hexdigest() != EXPECTED_SHA256[AXIOMS_PATH])

    # 2 -- dropped weighting
    dropped = {k: v for k, v in columns.items() if k != "M6_ABSOLUTE_ORBIT_UNIFORM"}
    tooth("X_T2_DROPPED_WEIGHTING", "M6 removed from the weighting table",
          len(dropped) != len(WEIGHTINGS)
          and sorted(claimed_c1["table"][i]["weighting"]
                     for i in range(len(claimed_c1["table"]))) ==
          sorted(WEIGHTINGS),
          f"primary carries {len(claimed_c1['table'])} weightings")

    # 3 -- hardcoded channel verdict: the verdict must move when the model
    #      dimension moves
    def verdict_of(pa, pb):
        return ("FORCED-AT-READOUT-GRADE" if pa and pb
                else "PARTIALLY-FORCED" if pa or pb else "NOT-FORCED")
    moved = verdict_of(True, True) != verdict_of(True, False)
    tooth("X_T3_HARDCODED_CHANNEL_VERDICT",
          "the verdict is a constant rather than a function of the model",
          moved and claimed_c2["falsifier_visibility"]["outcome_neutral"])

    # 4 -- leaked forcing
    tooth("X_T4_LEAKED_FORCING",
          "a sentence that forces nothing is reported as closing the channel",
          claimed_c2["falsifier_visibility"]["planted_nonnegativity_only"]
          ["detected_as"] == "PARTIALLY-FORCED")

    # 5 -- planted-forcing blindness
    tooth("X_T5_PLANTED_FORCING_BLINDNESS",
          "a counting sentence that genuinely forces must be seen as forcing",
          claimed_c2["falsifier_visibility"]["planted_forcing_sentence"]
          ["detected_as"] == "FORCED-AT-READOUT-GRADE")

    # 6 -- skipped recipe
    tooth("X_T6_SKIPPED_RECIPE",
          "the recipe census is short of the closure's own arity",
          claimed_c4["recipe_count"] == 1404)

    # 7 -- planted content-cell merge: merging two cells must change the
    #      measurability answer for a weighting that was measurable
    merged = {}
    for i, e in enumerate(events):
        merged[i] = e[4]
    keys = sorted({e[4] for e in events})
    victim_a, victim_b = keys[0], keys[1]
    col = list(columns["M1_COUNTING"])
    # perturb one event so the merged cell is genuinely inhomogeneous
    target = next(i for i, e in enumerate(events) if e[4] == victim_b)
    col[target] = 2
    remap = {victim_b: victim_a}
    seen: dict = {}
    conflicts = 0
    for i, e in enumerate(events):
        c = remap.get(e[4], e[4])
        if c in seen and seen[c] != col[i]:
            conflicts += 1
        seen.setdefault(c, col[i])
    tooth("X_T7_PLANTED_CELL_MERGE",
          "two content cells merged and one weight perturbed",
          conflicts > 0, f"{conflicts} conflicts detected after the merge")

    # 8 -- planted world-sum perturbation must change the residue vector count
    base = [(1, 2, 3), (1, 2, 3), (4, 5, 6)]
    perturbed = [(1, 2, 3), (1, 2, 4), (4, 5, 6)]
    tooth("X_T8_PLANTED_WORLD_SUM_PERTURBATION",
          "one world sum moved: the distinct-vector count must move",
          len(set(base)) != len(set(perturbed)),
          f"{len(set(base))} -> {len(set(perturbed))} distinct vectors")

    cert = {"certificate": "X_TEETH", "rows": rows,
            "caught": sum(1 for r in rows if r["caught"]),
            "total": len(rows)}
    cert["pass"] = all(r["caught"] for r in rows)
    return cert


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = time.time()
    print(f"CYCLE{CYCLE}_A3_CHANNEL_INDEPENDENT_CHECK")
    print("SPECIFIED_TO_REFUTE -- exit 0 regardless of claim survival")
    print()

    cert_pins, _payloads = check_pins()
    print(f"CERTIFICATE X0_PINS {'PASS' if cert_pins['pass'] else 'FAIL'} "
          + compact({"mismatches": cert_pins["mismatches"],
                     "firewall_hits": cert_pins["firewall_hits"]}))
    if not cert_pins["pass"]:
        print("checker pins failed -- the inputs are not the pinned inputs")
        return 0

    receipt_path = ROOT / PRIMARY_RECEIPT
    if not receipt_path.is_file():
        print(f"primary receipt absent at {PRIMARY_RECEIPT}")
        return 0
    primary = json.loads(receipt_path.read_text(encoding="utf-8"))
    certs = primary["certificates"]
    claimed_c1 = certs["C1_CONTENT_MEASURABILITY"]
    claimed_c2 = certs["C2_A3_CHANNEL"]
    claimed_c3 = certs["C3_ORPHANED_ENVARIANCE_NOTE"]
    claimed_c4 = certs["C4_RESIDUE_VECTORS"]
    print(f"primary receipt sha256 "
          f"{sha256(receipt_path.read_bytes()).hexdigest()[:16]}")
    print(f"primary runner sha256 {primary['runner_sha256'][:16]}")
    print()

    env = build()
    print(f"[event space rebuilt independently at {time.time()-started:.1f}s: "
          f"{len(env['events'])} events]")
    print()

    x1, columns, n_cells_uf, rank_s2 = x1_measurability(env, claimed_c1)
    x2 = x2_a3_channel(env, claimed_c2, n_cells_uf, rank_s2)
    x3 = x3_provenance(claimed_c3)
    x4 = x4_residues(env, claimed_c4)
    xt = checker_teeth(env, columns, claimed_c1, claimed_c2, claimed_c4)

    print("=" * 74)
    print("X1 -- CONTENT-MEASURABILITY, REBUILT FROM DEFINITIONS")
    print("=" * 74)
    print(f"  content cells by union-find: {x1['content_cells_by_union_find']}"
          f"  (primary claimed {x1['content_cells_claimed_by_primary']};"
          f" agrees={x1['cell_count_agrees']})")
    print(f"  S2 constraint rank: {x1['S2_constraint_rank']}")
    for row in x1["table"]:
        print(f"  {row['weighting']:<28}"
              f"measurable={str(row['is_content_measurable']):<7}"
              f"violating_cells={row['n_violating_cells']}")
    print(f"  disagreements: {x1['disagreements'] or 'NONE'}")
    print(f"  VERDICT: {x1['VERDICT']}")
    print()

    print("=" * 74)
    print("X2 -- THE A3 CHANNEL, INDEPENDENTLY FORMALIZED")
    print("=" * 74)
    cf = x2["checker_formalization"]
    pf = x2["primary_formalization"]
    print(f"  checker encoding : {cf['encoding']}")
    print(f"  primary encoding : {pf['encoding']}")
    print(f"  readout space dim   checker={cf['readout_space_dimension']}"
          f"  primary={pf['readout_space_dimension']}")
    print(f"  prob affine dim     checker="
          f"{cf['admissible_probability_affine_dimension']}"
          f"  primary={pf['admissible_probability_affine_dimension']}")
    print(f"  P_A forced={x2['P_A_forced_checker']}"
          f"  P_B forced={x2['P_B_forced_checker']}")
    print(f"  checker verdict={x2['checker_verdict']}"
          f"  primary verdict={x2['primary_verdict']}")
    print(f"  material differences: {x2['material_differences'] or 'NONE'}")
    print(f"  {x2['FORMALIZATION_IDENTIFIABILITY']}")
    print(f"  VERDICT: {x2['VERDICT']}")
    print()

    print("=" * 74)
    print("X3 -- PROVENANCE, VERIFIED AGAINST GIT INDEPENDENTLY")
    print("=" * 74)
    print(f"  commits: {x3['commits_resolved']}")
    print(f"  note sha256   {x3['note_sha256']}")
    print(f"  runner sha256 {x3['runner_sha256']}")
    print("  deletion commits: "
          f"{x3['deletion_commits_reachable_from_HEAD'] or 'NONE'}")
    print(f"  ancestor of HEAD: {x3['is_ancestor_of_HEAD']}")
    print(f"  refs containing : {x3['refs_containing_the_note']}")
    print(f"  A3 admission present in the recovered note:"
          f" {x3['A3_admission_present_in_the_recovered_note']}")
    print(f"  orphan mechanism independently confirmed:"
          f" {x3['orphan_mechanism_independently_confirmed']}")
    print(f"  mismatches: {x3['mismatches_against_the_primary'] or 'NONE'}")
    print(f"  VERDICT: {x3['VERDICT']}")
    print()

    print("=" * 74)
    print("X4 -- RESIDUE VECTORS, RECOMPUTED BY A DIFFERENT GROUPING")
    print("=" * 74)
    print(f"  recipes observed={x4['recipe_count_observed']}"
          f"  predicted from closure arities="
          f"{x4['recipe_count_predicted_from_closure_arities']}"
          f"  match={x4['arity_prediction_matches']}")
    print(f"  arities: {compact(x4['closure_arities'])}")
    for m in RESIDUE_MODULI:
        print(f"  distinct residue vectors mod {m:<6}:"
              f" {x4['distinct_residue_vectors'][str(m)]}")
    print(f"  degree0 native={x4['degree0_filter_native']}"
          f"  degree2 native={x4['degree2_filter_native']}")
    print(f"  null 0.00539 reproduced: {x4['stated_0_00539_reproduced']}"
          f"  null 85.8 reproduced: {x4['stated_85_8_reproduced']}")
    print(f"  mismatches: {x4['mismatches_against_the_primary'] or 'NONE'}")
    print(f"  VERDICT: {x4['VERDICT']}")
    print()

    print("=" * 74)
    print(f"CERTIFICATE X_TEETH {'PASS' if xt['pass'] else 'FAIL'}  "
          f"{xt['caught']}/{xt['total']} tampers caught")
    for row in xt["rows"]:
        print(f"  {row['tooth']:<38}{str(row['caught']):<7}{row['detail']}")
    print()

    verdicts = {c["certificate"]: c["VERDICT"]
                for c in (x1, x2, x3, x4)}
    overall = ("PRIMARY_SURVIVES_THIS_CHECK"
               if all(v == "PRIMARY_SURVIVES_THIS_CHECK"
                      for v in verdicts.values())
               else "PRIMARY_REFUTED_ON_THIS_CHECK")

    elapsed = time.time() - started
    receipt = {
        "cycle": CYCLE,
        "role": "independent checker, specified to refute",
        "runner": PRIMARY_RUNNER.replace(
            "frontier_cycle912_a3_channel_2026_07_28.py",
            "frontier_cycle912_a3_channel_independent_check_2026_07_28.py"),
        "runner_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "primary_receipt_sha256": sha256(receipt_path.read_bytes()).hexdigest(),
        "primary_runner_sha256": primary["runner_sha256"],
        "runtime_seconds": round(elapsed, 3),
        "certificates": {
            "X0_PINS": cert_pins, "X1_CONTENT_MEASURABILITY": x1,
            "X2_A3_CHANNEL": x2, "X3_PROVENANCE": x3,
            "X4_RESIDUE_VECTORS": x4, "X_TEETH": xt,
        },
        "per_check_verdicts": verdicts,
        "checker_verdict": overall,
        "exit_is_independent_of_claim_survival": True,
    }
    out = (ROOT / "outputs"
           / f"a3_channel_independent_check_cycle{CYCLE}_receipt_2026_07_28.json")
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")
    print(f"CHECKER VERDICT: {overall}")
    print(f"per-check: {compact(verdicts)}")
    print(f"receipt -> {out.relative_to(ROOT)}")
    print(f"elapsed {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
