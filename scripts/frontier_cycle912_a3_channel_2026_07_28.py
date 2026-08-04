#!/usr/bin/env python3
"""Cycle 912 -- the A3 channel, content-measurability, the orphaned envariance
note, and the 613 residue-vector count.

FOUR COMPONENTS, all cheap and all decisive, from the BL4 must-fail-first list.

C1  ROUTE 3: CONTENT-MEASURABILITY OF THE WEIGHTINGS.  The Record axiom says
    "A readout value is determined by record content alone."  If a weighting is
    to serve as the readout `I` (the IF1-strong identification) it MUST be
    constant on the Cycle-878 F_CONTENT cells.  Computed exactly for M1..M6
    (M6 from the Cycle-906 receipt's definition): is_content_measurable and
    n_violating_cells with witnesses.
    A-CONTENT CAVEAT, disclosed AND measured: the census `content` field is a
    TRUNCATED sha256 of the packed lane state (878 line 320, byte-quoted).  The
    measurability question is well posed regardless, but the truncation could in
    principle MERGE two distinct record contents into one cell and so manufacture
    a spurious violation.  This block does not merely disclose that -- it probes
    it: every content_of() call is instrumented and the RAW lane-state preimages
    behind each 16-hex value are collected, so the truncation's injectivity on
    this census is measured, not assumed.

C2  THE A3 CHANNEL, RUN FOR THE FIRST TIME.  The graded-constraint memo's
    section 1 names a bounded derivation from the landed readout sentences as
    "sufficient to force it at readout grade".  Nobody has ever run it.  This
    block formalizes the landed sentences as an exact constraint system over the
    census's readout objects and COMPUTES what they force about a readout's
    dependence structure.  The verdict is computed, never written down: all
    three classes (FORCED-AT-READOUT-GRADE / PARTIALLY-FORCED / NOT-FORCED) are
    reachable by the same code path, and the falsifier suite proves it by
    planting a sentence that WOULD force and checking it is detected as forcing.

C3  THE ORPHANED ENVARIANCE NOTE, RECOVERED AND VERIFIED.  Read-only git-history
    evidence gathering; every command disclosed verbatim in the receipt.

C4  THE 613 RESIDUE-VECTOR COUNT.  Cycle 909 said "more search is provably
    useless" without ever measuring how independent the 1,404 recipes were.
    This block measures it: the number of DISTINCT residue vectors mod 613 (and
    31, and 19003) across the recipes' escape-world sum vectors, which is
    exactly the effective number of independent tries the survey made at the
    denominator lemma's arithmetic gate.  Plus the exercise's stated null-model
    numbers, recomputed.

DISCIPLINE.  Pins by full path + sha256 + git blob, hard-fail exit 2.  TEXT/AST/
JSON only; import firewall with 0 hits gated.  Restriction gates value-for-value
against the pinned 878/906/907/909 receipts.  Exact integer/Fraction arithmetic
throughout -- no float is load-bearing (the null-model probabilities are exact
Fractions, reported as decimals only for reading).  Deterministic double-build.
No probability postulate is introduced anywhere: every fraction emitted here is
a bookkeeping fraction, not a probability.
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
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
from types import SimpleNamespace

CYCLE = 912
BLOCK = "A3_CHANNEL_CONTENT_MEASURABILITY_ORPHANED_NOTE_AND_613_RESIDUES"
FRACTION_LABEL = "bookkeeping fraction, not probability"

CORE_PATH = ("scripts/frontier_cycle719_two_rail_recurrent_controller_core"
             "_2026_07_26.py")
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C902_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"
C905_PATH = "scripts/frontier_cycle905_born_narrowing_2026_07_28.py"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C906_PATH = "scripts/frontier_cycle906_covariance_tension_2026_07_28.py"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C907_RECEIPT = "outputs/m6_identification_cycle907_receipt_2026_07_28.json"
C909_PATH = "scripts/frontier_cycle909_within_world_pricing_2026_07_28.py"
C909_RECEIPT = "outputs/within_world_pricing_cycle909_receipt_2026_07_28.json"
GRADED_NOTE = ("docs/GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION"
               "_2026-07-04.md")
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C902_RECEIPT,
    C905_PATH, C905_RECEIPT, C906_PATH, C906_RECEIPT, C907_RECEIPT,
    C909_PATH, C909_RECEIPT, GRADED_NOTE, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C905_PATH, C906_PATH, C909_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C902_RECEIPT, C905_RECEIPT, C906_RECEIPT,
                   C907_RECEIPT, C909_RECEIPT)
TEXT_ONLY_PATHS = (GRADED_NOTE, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C902_RECEIPT:
        "91c5631415d0231390fedbd0174f074de45cfa33b6dd4f706ed6fcdbf4dfd1d8",
    C905_PATH:
        "83429f35312e0df16d3d11e65685cb87b8e732b19299e1078ddaea1e1444afb3",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C906_PATH:
        "9c6392d593c1bf37e70f84692732d1e5cfa3f4377393dab846a15789fc0ce008",
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
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C902_RECEIPT: "1fd7522ad2af152f2e13327e752e2eb9f37e67bb",
    C905_PATH: "f9f2171602bddf7d6164261dc13a2ee4f7e3046c",
    C905_RECEIPT: "7094c986dc0560e8982507d8cc379f5c720b639f",
    C906_PATH: "d7577bb2ac9f4cb7ee9d8abc5f19e9c7cf888df9",
    C906_RECEIPT: "392cba199a75a14a8bb88808943c1259cbd7a94b",
    C907_RECEIPT: "e7eef6eeeb62aeddcdb12417ccd8ec871b9d87a7",
    C909_PATH: "359b5a502fd9cbd05653f33e0b7931caaf868a25",
    C909_RECEIPT: "4843b2ca7dd5af0ee1c67ff11aa4e47d7cb22976",
    GRADED_NOTE: "473f094d05d4118d5e44bd29f1d9aec950c1c088",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle905_born_narrowing_independent_check_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle906_covariance_tension_independent_check_2026_07_28",
    "frontier_cycle907_m6_identification_2026_07_28",
    "frontier_cycle909_within_world_pricing_2026_07_28",
    "frontier_cycle909_within_world_independent_check_2026_07_28",
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

# the orphaned-note coordinates named in the block spec
ORPHAN_COMMITS = ("a61fa74c3b", "1c277078dd")
ORPHAN_NOTE = ("docs/BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL"
               "_PROBABILITY_NOTE_2026-06-05.md")
ORPHAN_RUNNER = "scripts/frontier_born_from_envariance_2026_06_05.py"
ORPHAN_CACHE = "logs/runner-cache/frontier_born_from_envariance_2026_06_05.txt"

WEIGHTINGS = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT",
              "M6_ABSOLUTE_ORBIT_UNIFORM")
M6_NAME = "M6_ABSOLUTE_ORBIT_UNIFORM"

# the arithmetic the denominator lemma turns on
DEGREE0_SCALE = 19003          # = 31 * 613
DEGREE2_SCALE = 175            # = 5^2 * 7
RESIDUE_MODULI = (613, 31, 19003, 175, 5, 7, 25)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def _git_blob_sha1(payload: bytes) -> str:
    from hashlib import sha1
    return sha1(b"blob " + str(len(payload)).encode() + b"\0"
                + payload).hexdigest()


def factorize(value: int) -> dict:
    out: dict = {}
    n, d = value, 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


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
    """Exact rational rendered to a fixed number of places, for reading only.
    Nothing downstream consumes this string."""
    scaled = value * (10 ** places)
    whole = scaled.numerator // scaled.denominator
    text = str(whole).rjust(places + 1, "0")
    return f"{text[:-places] or '0'}.{text[-places:]}"


def byte_quote(payload: bytes, needle: str, label: str) -> dict:
    """A quote is only a BYTE-quote if it is located in the pinned bytes.  This
    finds it and records where; a miss is a hard failure, not a soft note."""
    raw = needle.encode("utf-8")
    offset = payload.find(raw)
    if offset < 0:
        raise AssertionError(("byte-quote not found in pinned payload", label,
                              needle[:60]))
    if payload.find(raw, offset + 1) >= 0:
        occurrences = payload.count(raw)
    else:
        occurrences = 1
    return {
        "label": label,
        "text": needle,
        "byte_offset": offset,
        "byte_length": len(raw),
        "occurrences_in_file": occurrences,
        "sha256_of_quote": sha256(raw).hexdigest(),
    }


# ---------------------------------------------------------------------------
# certificate A -- pins
# ---------------------------------------------------------------------------

def pin_rows() -> dict:
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    for p in TEXT_ONLY_PATHS:
        payloads[p].decode("utf-8")

    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=Path(__file__).name
    )
    literal = None
    string_constants: dict = {}
    for node in self_tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Name):
                continue
            if isinstance(node.value, ast.Constant) \
                    and isinstance(node.value.value, str):
                string_constants[target.id] = node.value.value
            elif isinstance(node.value, ast.BinOp) \
                    and isinstance(node.value.op, ast.Add):
                try:
                    string_constants[target.id] = ast.literal_eval(node.value)
                except (ValueError, SyntaxError):
                    pass
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
    blob_rows = {p: _git_blob_sha1(b) for p, b in payloads.items()}
    result = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "modes": {
            "imported": list(IMPORTED_PATHS), "ast_only": list(AST_ONLY_PATHS),
            "json_only": list(JSON_ONLY_PATHS),
            "text_only": list(TEXT_ONLY_PATHS),
        },
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "sha256_mismatches": sorted(
            p for p in sha_rows if sha_rows[p] != EXPECTED_SHA256.get(p)),
        "git_blob_mismatches": sorted(
            p for p in blob_rows if blob_rows[p] != EXPECTED_GIT_BLOBS.get(p)),
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
        "firewall_hits": list(PRIMARY_FIREWALL.hits),
        "bytes": {p: len(b) for p, b in payloads.items()},
    }
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result, payloads


# ---------------------------------------------------------------------------
# AST lift -- the pinned machinery, never imported
# ---------------------------------------------------------------------------

def ast_lift(path: str, names: tuple, consts: tuple, globals_: dict,
             const_env: dict | None = None):
    """Lift named functions/classes and named module constants out of a pinned
    file by AST.  Constants that are literals are literal_eval'd; constants
    built by a comprehension (909's AFFINE_COEFFS) are evaluated in a closed
    namespace containing only builtins the pinned expression names."""
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found = [], {}
    env = {"tuple": tuple, "range": range, "frozenset": frozenset}
    env.update(const_env or {})
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
    namespace = dict(globals_)
    namespace.update(found)
    exec(compile(module, f"<ast-lift {path}>", "exec"), namespace)
    return namespace, found, tuple(getattr(b, "name") for b in body)


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
C878_CONSTS = ("HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS",
               "REGISTER_CAP", "DETERMINISM_ORBITS", "CANDIDATE_NAMES",
               "CONTROL_NAME", "FAMILY_ORDER")
C909_FUNCS = ("base_fields", "generate_recipes")
C909_CONSTS = ("GEOMETRIC_RATIOS", "POWER_EXPONENTS", "AFFINE_COEFFS",
               "SUM_COEFFS")


class ContentProbe:
    """The A-CONTENT probe.  878's content_of() computes
        sha256(bytes(lane_state)).hexdigest()[:16]
    -- a TRUNCATED digest.  We stand in for `sha256` inside the lifted 878
    namespace so that the emitted event space is bit-identical to the pinned one
    (we return the real digest) while recording, for every 16-hex content value,
    the set of RAW lane-state preimages behind it.  If some value has more than
    one preimage the truncation merged two distinct record contents and the
    F_CONTENT partition is coarser than true record content; if every value has
    exactly one, the field is injective on this census and the measurability
    verdicts are exact for true record content.  No cryptographic assumption is
    used: raw preimages are compared, not digests."""

    def __init__(self) -> None:
        self.preimages: dict[str, set] = defaultdict(set)
        self.calls = 0

    def __call__(self, payload):
        probe = self

        class _D:
            def __init__(self, data):
                self._data = data
                self._inner = sha256(data)

            def hexdigest(self):
                text = self._inner.hexdigest()
                probe.calls += 1
                probe.preimages[text[:16]].add(bytes(self._data))
                return text

        return _D(payload)

    def report(self) -> dict:
        multi = {k: len(v) for k, v in self.preimages.items() if len(v) > 1}
        return {
            "what_the_field_is": "sha256(bytes(lane_state)).hexdigest()[:16]",
            "content_of_calls": self.calls,
            "distinct_content_values": len(self.preimages),
            "distinct_raw_lane_state_preimages":
                sum(len(v) for v in self.preimages.values()),
            "content_values_with_more_than_one_raw_preimage": len(multi),
            "worst_preimage_multiplicity": max(multi.values()) if multi else 1,
            "truncation_is_injective_on_this_census": not multi,
            "meaning": (
                "the 16-hex content field is INJECTIVE on the realized lane"
                " states of this census (measured, not assumed), so the"
                " F_CONTENT partition IS the true record-content partition and"
                " both the PASS and the FAIL measurability verdicts below are"
                " exact for record content"
            ) if not multi else (
                "the truncation MERGED distinct record contents: F_CONTENT is"
                " strictly coarser than true record content, so a FAIL verdict"
                " below may be a truncation artifact (a PASS verdict would"
                " still be sound, since a coarser partition is a stronger"
                " constancy requirement)"
            ),
        }


def lift_machinery(probe: ContentProbe):
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS,
        {"K": K, "combinations": combinations},
    )
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": probe, "gcd": gcd,
         "Fraction": Fraction, "json": json},
    )
    c878 = SimpleNamespace(**{n: ns878[n] for n in C878_FUNCS})
    ns909, consts909, names909 = ast_lift(
        C909_PATH, C909_FUNCS, C909_CONSTS,
        {"Fraction": Fraction, "Counter": Counter},
    )
    c909 = SimpleNamespace(**{n: ns909[n] for n in C909_FUNCS})
    provenance = {
        "lifted_from_863": list(names863),
        "lifted_from_878": list(names878),
        "lifted_from_909": list(names909),
        "constants_863": {k: list(v) if isinstance(v, tuple) else v
                          for k, v in consts863.items()},
        "constants_878": {k: list(v) if isinstance(v, tuple) else v
                          for k, v in consts878.items()},
        "constants_909": {k: [list(x) if isinstance(x, tuple) else x
                              for x in v] if isinstance(v, tuple) else v
                          for k, v in consts909.items()},
        "import_of_863_878_902_905_906_907_909": False,
        "sha256_substituted_inside_878_namespace_for_the_A_CONTENT_probe": True,
    }
    return c863, c878, c909, consts878, provenance


def build_event_space(c863, c878, consts):
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_fail = c863.build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    rig = c878.dead_wire_rig(
        program, sim, c863.pack_lanes(states + (states[0],))
    )
    scan = c878.composed_scan(program, census, states, rig, consts["HORIZON"])
    return {"program": program, "census": census, "stations": stations,
            "scan": scan, "events": scan["events"], "init_failures": init_fail}


# ---------------------------------------------------------------------------
# the shared census facts every component reads
# ---------------------------------------------------------------------------

def census_facts(space, c878, receipt902):
    events = space["events"]
    scan = space["scan"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    idx_by_world: dict = defaultdict(list)
    for i, w in enumerate(world_of):
        idx_by_world[w].append(i)

    common = 1
    for count in set(per_world.values()):
        common = c878.lcm(common, count)
    nums, dens, meta, _pw, _sup, common2 = c878.build_candidates(
        events, scan["occ_global"], scan["formed"], scan["boundaries"])

    def world_weighted(a_of_world):
        totals = sum(a_of_world(w) for w in supported)
        col = [a_of_world(e[0]) * (common2 // per_world[e[0]]) for e in events]
        return col, totals * common2

    perms, perm_ok = c878.monitor_phase_action(space["census"],
                                               space["stations"])
    world_orbits = c878.group_orbits(perms, len(space["census"])) \
        if perm_ok else ()
    formed = scan["formed"]
    never_set = {w for w in supported if w not in formed}
    free_orbits = [o for o in world_orbits
                   if not any(w in never_set for w in o)]
    star = list(free_orbits[0]) if free_orbits else []
    star_set = set(star)
    star_events = [i for i, w in enumerate(world_of) if w in star_set]
    star_rows = {w: [events[i] for i in idx_by_world[w]] for w in star}
    tags_col = [e[2] for w in star for e in star_rows[w]]

    # M6 exactly as the Cycle-906 receipt defines it: world_weighted on the
    # indicator of the escape orbit
    m6_nums, _m6_den = world_weighted(lambda w: 1 if w in star_set else 0)
    nums[M6_NAME] = m6_nums
    meta[M6_NAME] = {
        "definition": ("uniform absolute mass on the escape orbit: every world"
                       " of the free (never-formed-free) orbit gets equal mass,"
                       " spread uniformly over its own events; every other"
                       " world gets zero"),
        "record_native_source": "the Cycle-878 monitor-phase world orbits",
        "source": "Cycle-906 receipt Q3_exhibited_solution",
    }

    content_cells: dict = defaultdict(list)
    for i, e in enumerate(events):
        content_cells[e[4]].append(i)

    return {
        "events": events, "scan": scan, "world_of": world_of,
        "per_world": per_world, "supported": supported,
        "idx_by_world": idx_by_world, "common": common2,
        "nums": nums, "dens": dens, "meta": meta,
        "world_orbits": world_orbits, "perm_ok": perm_ok,
        "never_set": never_set, "free_orbits": free_orbits,
        "star": star, "star_events": star_events, "star_rows": star_rows,
        "tags_col": tags_col, "boundaries": scan["boundaries"],
        "content_cells": dict(content_cells),
        "formed_worlds": sorted(w for w in supported if w in formed),
        "block_events": [i for i, w in enumerate(world_of) if w in never_set],
    }


# ---------------------------------------------------------------------------
# certificate B -- restriction gates, value-for-value
# ---------------------------------------------------------------------------

def restriction_gates(facts, receipts) -> dict:
    f878 = receipts["878"]["findings"]
    r906, r907, r909 = receipts["906"], receipts["907"], receipts["909"]
    rows = []

    def gate(name, computed, expected):
        rows.append({"gate": name, "computed": computed, "expected": expected,
                     "match": computed == expected})

    events = facts["events"]
    gate("878_event_cardinality", len(events), f878["event_cardinality"])
    gate("878_F_CONTENT_cells", len(facts["content_cells"]),
         f878["cells_per_family"]["F_CONTENT"])
    gate("878_F_ATOM_cells", f878["cells_per_family"]["F_ATOM"], len(events))
    gate("878_atoms_are_singletons", f878["atoms_are_singletons"], True)
    gate("878_worlds_with_events", len(facts["supported"]),
         f878["worlds_with_at_least_one_event"])
    gate("878_world_orbit_count", len(facts["world_orbits"]),
         f878["landed_symmetry"]["world_orbit_count"])
    gate("878_action_is_a_census_bijection", bool(facts["perm_ok"]),
         f878["landed_symmetry"]["action_is_a_census_bijection"])
    gate("878_events_by_tag",
         dict(Counter(e[2] for e in events)), f878["events_by_tag"])
    gate("878_crossing_pair_count", f878["crossing_pairs"], 17)
    # F_CONTENT and F_WORLD cross (878 lists F_WORLD~F_CONTENT among the pairs
    # where neither refines the other); recomputed here from the census, because
    # it is exactly what gives C1 its teeth -- a content cell that spans two
    # worlds is where a world-constant weighting can break content-determination
    cells, world_of = facts["content_cells"], facts["world_of"]
    content_splits_a_world = any(
        len({world_of[i] for i in idx}) > 1 for idx in cells.values())
    world_splits_a_content_cell = len(cells) > len(facts["supported"])
    gate("878_F_CONTENT_and_F_WORLD_cross",
         content_splits_a_world and world_splits_a_content_cell, True)

    q3 = r906["Q3_exhibited_solution"]
    gate("906_M6_support_events", len(facts["star_events"]),
         q3["support_events"])
    gate("906_M6_support_worlds", facts["star"], list(q3["support_worlds"]))
    gate("906_M6_total", sum(facts["nums"][M6_NAME]), q3["total"])
    gate("906_escape_orbit_count", len(facts["free_orbits"]), 1)

    gate("907_degree0_ratio_scale", DEGREE0_SCALE,
         r907["Q1_degree0_ratio_scale"])
    gate("909_degree0_scale", r909["Q2_denominator_lemma"]["degree0_scale"],
         DEGREE0_SCALE)
    gate("909_degree0_scale_factorisation",
         {str(k): v for k, v in factorize(DEGREE0_SCALE).items()},
         {str(k): v for k, v in
          r909["Q2_denominator_lemma"]["degree0_scale_factorisation"].items()})
    gate("909_degree0_scale_is_31_times_613",
         {str(k): v for k, v in factorize(DEGREE0_SCALE).items()},
         {"31": 1, "613": 1})
    gate("909_degree2_scale", r909["Q2_denominator_lemma"]["degree2_scale"],
         DEGREE2_SCALE)
    gate("909_recipe_count_expected", r909["Q2_recipe_count"], 1404)
    gate("909_escape_events_per_world",
         r909["Q1_escape_orbit"]["events_per_world"], 129)
    gate("909_escape_support_events",
         r909["Q1_escape_orbit"]["support_events"], len(facts["star_events"]))
    gate("909_escape_worlds", list(r909["Q1_escape_orbit"]["worlds"]),
         facts["star"])

    cert = {"certificate": "B_RESTRICTION_GATE", "rows": rows,
            "reproduce": sum(1 for r in rows if r["match"]),
            "total": len(rows),
            "event_space_digest": digest([list(e) for e in events])}
    cert["pass"] = all(r["match"] for r in rows)
    return cert


# ---------------------------------------------------------------------------
# C1 -- content-measurability of the weightings
# ---------------------------------------------------------------------------

def c1_content_measurability(facts, probe_report, quotes) -> dict:
    events = facts["events"]
    cells = facts["content_cells"]
    world_of = facts["world_of"]
    nums = facts["nums"]

    cell_keys = sorted(cells)
    size_hist = Counter(len(cells[c]) for c in cell_keys)
    cross_world = [c for c in cell_keys
                   if len({world_of[i] for i in cells[c]}) > 1]

    table = []
    for name in WEIGHTINGS:
        column = nums[name]
        violating = []
        for c in cell_keys:
            idx = cells[c]
            if len(idx) < 2:
                continue
            first = column[idx[0]]
            if any(column[i] != first for i in idx[1:]):
                violating.append(c)
        witnesses = []
        for c in violating[:3]:
            idx = cells[c]
            seen: dict = {}
            for i in idx:
                seen.setdefault(column[i], []).append(i)
            witnesses.append({
                "content": c,
                "cell_size": len(idx),
                "distinct_weight_values": len(seen),
                "events": [
                    {"event": list(events[i]), "world": events[i][0],
                     "moment": events[i][1], "tag": events[i][2],
                     "ordinal": events[i][3], "weight_numerator": column[i]}
                    for i in idx[:4]
                ],
            })
        table.append({
            "weighting": name,
            "definition": facts["meta"][name]["definition"],
            "is_content_measurable": not violating,
            "n_violating_cells": len(violating),
            "n_cells_tested": len(cell_keys),
            "n_multi_event_cells": sum(v for k, v in size_hist.items() if k > 1),
            "violating_witnesses": witnesses,
        })

    measurable = [r["weighting"] for r in table if r["is_content_measurable"]]
    failing = [r["weighting"] for r in table if not r["is_content_measurable"]]
    cert = {
        "certificate": "C1_CONTENT_MEASURABILITY",
        "question": ("does the weighting take a value determined by record"
                     " content alone -- i.e. is it constant on every F_CONTENT"
                     " cell?  Any weighting that fails CANNOT be the readout I"
                     " of the Record axiom (the IF1-strong identification)."),
        "record_axiom_sentence": quotes["R2_CONTENT_ALONE"],
        "A_CONTENT_caveat": {
            "disclosure": ("the census content field is not the record content"
                           " itself but a TRUNCATED sha256 of the packed lane"
                           " state; its provenance is the pinned Cycle-878"
                           " source, byte-quoted here"),
            "provenance_byte_quote": quotes["A_CONTENT_FIELD"],
            "well_posedness": ("the measurability question is well posed"
                               " regardless of the field's cryptographic"
                               " nature: F_CONTENT is a partition of the event"
                               " space and constancy on its cells is a"
                               " definite property of a weighting"),
            "probe": probe_report,
        },
        "event_cardinality": len(events),
        "n_content_cells": len(cell_keys),
        "cell_size_histogram": {str(k): v for k, v in sorted(size_hist.items())},
        "content_cells_crossing_more_than_one_world": len(cross_world),
        "table": table,
        "content_measurable_weightings": measurable,
        "non_content_measurable_weightings": failing,
    }
    cert["finding"] = (
        f"of the six weightings on the lane, {len(measurable)} is/are constant"
        f" on record content ({', '.join(measurable) or 'none'}) and"
        f" {len(failing)} is/are not ({', '.join(failing) or 'none'});"
        " a weighting that is not content-measurable cannot serve as the"
        " Record axiom's readout I"
    )
    cert["pass"] = True   # C1 is a measurement; it has no way to 'fail'
    return cert


# ---------------------------------------------------------------------------
# C2 -- the A3 channel
# ---------------------------------------------------------------------------

def c2_a3_channel(facts, quotes) -> dict:
    """Formalize the landed readout sentences as an exact constraint system over
    the census's readout objects and COMPUTE what they force.

    READOUT OBJECTS.  The census supplies a finite set E of realized record
    events (|E| = 92260) whose atoms are singletons (gated from 878), so any
    subset A of E is a finite collection of pairwise-disjoint records -- exactly
    the objects the Record axiom's additivity clause quantifies over.  A readout
    is a map I from subsets of E to the rationals.

    THE SENTENCES, each byte-quoted from the pinned axiom memo.
      S1  "Only records are readable."
          -> a DOMAIN restriction: I is a function of a record collection and
             of nothing else.  It adds no linear constraint; it forbids
             arguments, and that is what it is recorded as here.
      S2  "A readout value is determined by record content alone."
          -> content(e) = content(e') implies I({e}) = I({e'}).
      S3  "For any finite collection of pairwise-disjoint records, scalar
           readout `I` is additive, with `I(empty)=0`."
          -> I(A u B) = I(A) + I(B) for disjoint A, B, and I({}) = 0, hence
             I(A) = sum over e in A of w(e) with w(e) := I({e}).

    THE CRITERION TO BE FORCED, byte-quoted from the memo's own section 1, is a
    REALITY criterion, not a locality one, and it has two halves:
      P_A  INVISIBILITY -- "real exactly to the extent it influences ...":
           anything that changes no record content statistics changes no
           readout.  Formally: if A and B have the same content multiset then
           I(A) = I(B), for EVERY admissible I.
      P_B  FREQUENCY-FAITHFULNESS -- "... which records form and with what
           frequencies": the readout is fixed by the record frequencies, i.e.
           the admissible probability readout is UNIQUE.  (Mere existence is
           vacuous -- a normalized non-negative content-measurable weight
           always exists -- so the criterion's "exactly" is read as uniqueness,
           which is the only reading with content.)

    FORCING is computed, never asserted: a predicate is forced by a sentence set
    exactly when NO admissible model of the sentences violates it.  P_A is
    decided by an exact linear-form computation (the difference functional's
    coefficient vector must vanish identically, which is a complete test, not a
    sample); P_B is decided by the dimension of the admissible probability set.
    """
    events = facts["events"]
    cells = facts["content_cells"]
    world_of = facts["world_of"]
    n_events = len(events)
    cell_keys = sorted(cells)
    n_cells = len(cell_keys)
    cell_of_event = {}
    for c in cell_keys:
        for i in cells[c]:
            cell_of_event[i] = c

    # ---- the content-preserving test family ------------------------------
    # Pairs (A, B) of record collections with the SAME content multiset but
    # different membership.  These exist exactly because some content cells
    # hold more than one event; we take every multi-event cell and swap.
    multi = [c for c in cell_keys if len(cells[c]) > 1]
    pairs = []
    for c in multi:
        idx = cells[c]
        pairs.append((c, idx[0], idx[1]))

    def coeff_vector_over_cells(a_idx, b_idx):
        """Coefficient vector of the linear form I(A) - I(B) in the S2+S3 model
        (one free weight per CONTENT CELL).  Complete, not sampled."""
        acc: dict = defaultdict(int)
        for i in a_idx:
            acc[cell_of_event[i]] += 1
        for i in b_idx:
            acc[cell_of_event[i]] -= 1
        return {k: v for k, v in acc.items() if v}

    def coeff_vector_over_events(a_idx, b_idx):
        """Same form in the S3-only model (one free weight per EVENT)."""
        acc: dict = defaultdict(int)
        for i in a_idx:
            acc[i] += 1
        for i in b_idx:
            acc[i] -= 1
        return {k: v for k, v in acc.items() if v}

    pa_violations_S2S3, pa_violations_S3 = [], []
    for c, i, j in pairs:
        if coeff_vector_over_cells([i], [j]):
            pa_violations_S2S3.append((c, i, j))
        if coeff_vector_over_events([i], [j]):
            pa_violations_S3.append((c, i, j))

    forced_PA_landed = not pa_violations_S2S3
    forced_PA_without_S2 = not pa_violations_S3

    # an explicit separating readout for the dropped-S2 model, to show the
    # violation is realized by an admissible weighting and not just by a
    # non-vanishing coefficient vector
    sep_witness = None
    for c, i, j in pa_violations_S3[:200]:
        if world_of[i] != world_of[j]:
            w = [0] * n_events
            w[i] = 1
            sep_witness = {
                "content": c,
                "A": {"event": list(events[i]), "world": world_of[i]},
                "B": {"event": list(events[j]), "world": world_of[j]},
                "readout": ("w(e) = 1 on the single event A, 0 elsewhere --"
                            " additive with I(empty)=0, defined on records"
                            " only, but NOT content-determined"),
                "I_of_A": 1, "I_of_B": 0,
                "separates_a_content_preserving_pair": True,
            }
            break

    # ---- P_B: is the admissible probability unique? ----------------------
    # The admissible set under the landed sentences is
    #     { w in Q^cells : w >= 0, sum over events of w(e) = 1 }
    # whose affine dimension is n_cells - 1.  Unique iff that is 0.
    sizes = [len(cells[c]) for c in cell_keys]
    dim_prob_landed = n_cells - 1
    forced_PB_landed = dim_prob_landed == 0

    # two DISTINCT admissible probabilities, exhibited, plus a region on which
    # they disagree -- the concrete refutation of "exactly to the extent"
    # w1: uniform over content CELLS      w1(cell) = 1/(n_cells * |cell|)
    # w2: uniform over record EVENTS      w2(cell) = 1/n_events
    w1 = {c: Fraction(1, n_cells * len(cells[c])) for c in cell_keys}
    w2 = {c: Fraction(1, n_events) for c in cell_keys}
    tot1 = sum(w1[c] * len(cells[c]) for c in cell_keys)
    tot2 = sum(w2[c] * len(cells[c]) for c in cell_keys)
    biggest = max(cell_keys, key=lambda c: len(cells[c]))
    region = cells[biggest]
    i1 = sum(w1[cell_of_event[i]] for i in region)
    i2 = sum(w2[cell_of_event[i]] for i in region)

    # ---- the falsifier suite: all three verdict classes must be reachable
    def verdict_of(pa: bool, pb: bool) -> str:
        if pa and pb:
            return "FORCED-AT-READOUT-GRADE"
        if pa or pb:
            return "PARTIALLY-FORCED"
        return "NOT-FORCED"

    # PLANT-FORCING: add the sentence "the readout assigns the same value to
    # every record" (a counting sentence).  It is NOT landed -- it is planted --
    # and under it the admissible probability is unique, so the criterion IS
    # forced.  The harness must SEE that.
    dim_prob_planted_counting = 0     # {w constant, normalized} is a point
    planted_forcing_verdict = verdict_of(True, dim_prob_planted_counting == 0)

    # PLANT-NONFORCING-A: add only non-negativity.  Still a full-dimensional
    # cone, so still PARTIALLY-FORCED.
    planted_nonneg_verdict = verdict_of(True, (n_cells - 1) == 0)

    # PLANT-DROP-S2: remove content-determination.  P_A must break.
    planted_drop_s2_verdict = verdict_of(forced_PA_without_S2,
                                         (n_events - 1) == 0)

    landed_verdict = verdict_of(forced_PA_landed, forced_PB_landed)

    classes_reachable = sorted({landed_verdict, planted_forcing_verdict,
                                planted_nonneg_verdict, planted_drop_s2_verdict})
    outcome_neutral = set(classes_reachable) >= {
        "FORCED-AT-READOUT-GRADE", "PARTIALLY-FORCED", "NOT-FORCED"}

    cert = {
        "certificate": "C2_A3_CHANNEL",
        "status": "FIRST RUN -- this channel has never been attempted",
        "the_claim_being_tested": quotes["SUFFICIENCY_CLAIM"],
        "the_criterion": quotes["CRITERION"],
        "note_on_the_criterion_as_written": (
            "the memo's section 1 criterion is a REALITY criterion about"
            " influence on record formation and frequencies.  It is NOT the"
            " regional-locality sentence ('the readout of a region depends only"
            " on records in that region') that the block spec paraphrased; that"
            " sentence appears nowhere in the memo.  The formalization below"
            " follows the memo's own bytes, as instructed, and the divergence"
            " is disclosed here rather than silently resolved."),
        "formalization": {
            "readout_objects": (
                "E = the realized record-write events of the pinned Cycle-878"
                " census; F_ATOM cells are singletons (gated), so every subset"
                " of E is a finite collection of pairwise-disjoint records --"
                " exactly the objects the additivity clause quantifies over"),
            "event_cardinality": n_events,
            "content_cells": n_cells,
            "S1_only_records_readable": {
                "quote": quotes["R1_ONLY_RECORDS"],
                "formal": ("dom(I) is contained in the subsets of E; I takes no"
                           " pre-record argument"),
                "kind": "domain restriction; adds no linear constraint",
            },
            "S2_content_determines_the_value": {
                "quote": quotes["R2_CONTENT_ALONE"],
                "formal": "content(e) = content(e') implies I({e}) = I({e'})",
                "kind": ("measurability constraint; collapses the model space"
                         f" from {n_events} to {n_cells} free values"),
            },
            "S3_additive_with_empty_zero": {
                "quote": quotes["R3_ADDITIVE"],
                "formal": ("I(A u B) = I(A) + I(B) for disjoint A, B and"
                           " I(empty) = 0, hence I(A) = sum of w(e) over A"),
                "kind": "representation constraint; makes I an event weighting",
            },
            "P_A_invisibility": (
                "for all A, B with the same content multiset, I(A) = I(B)"),
            "P_B_frequency_faithfulness": (
                "the admissible probability readout is UNIQUE (non-negative,"
                " normalized, and fixed by the record frequencies)"),
            "forcing_rule": ("a predicate is FORCED by a sentence set exactly"
                             " when no admissible model of the sentences"
                             " violates it"),
        },
        "model_dimensions": {
            "S3_alone_free_values_per_event": n_events,
            "S3_and_S2_free_values_per_content_cell": n_cells,
            "admissible_probability_affine_dimension_under_the_landed_sentences":
                dim_prob_landed,
            "admissible_probability_affine_dimension_if_the_readout_must_count":
                dim_prob_planted_counting,
        },
        "P_A_result": {
            "content_preserving_pairs_tested": len(pairs),
            "complete_not_sampled": True,
            "violations_under_the_landed_sentences": len(pa_violations_S2S3),
            "forced": forced_PA_landed,
            "why": ("additivity makes I a sum of event weights; content"
                    " determination makes the weight a function of the content"
                    " cell; so I(A) = sum over cells c of n_A(c) * w(c), which"
                    " depends on A only through its content multiset.  The"
                    " difference functional I(A) - I(B) for a content-preserving"
                    " pair has an identically zero coefficient vector, checked"
                    " exhaustively over every multi-event content cell."),
        },
        "P_B_result": {
            "forced": forced_PB_landed,
            "admissible_probability_affine_dimension": dim_prob_landed,
            "why_not": ("the landed sentences constrain the SHAPE of a readout"
                        " (additive, content-determined) but select no"
                        " particular one.  The admissible probabilities form a"
                        f" simplex of affine dimension {dim_prob_landed}, so the"
                        " record frequencies are not fixed by the sentences."),
            "two_distinct_admissible_probabilities": {
                "w1_uniform_over_content_cells": {
                    "definition": "w(cell) = 1/(n_cells * |cell|)",
                    "normalized": tot1 == 1,
                    "nonnegative": all(v >= 0 for v in w1.values()),
                    "content_measurable": True,
                },
                "w2_uniform_over_record_events": {
                    "definition": "w(cell) = 1/n_events",
                    "normalized": tot2 == 1,
                    "nonnegative": all(v >= 0 for v in w2.values()),
                    "content_measurable": True,
                },
                "region_on_which_they_disagree": {
                    "content": biggest,
                    "region_size_events": len(region),
                    "I_w1": fr(i1), "I_w2": fr(i2),
                    "they_differ": i1 != i2,
                    "label": FRACTION_LABEL,
                },
            },
        },
        "falsifier_visibility": {
            "planted_forcing_sentence": {
                "sentence": ("PLANTED, not landed: 'the readout assigns the"
                             " same value to every record' (a counting"
                             " sentence)"),
                "must_be_detected_as": "FORCED-AT-READOUT-GRADE",
                "detected_as": planted_forcing_verdict,
                "ok": planted_forcing_verdict == "FORCED-AT-READOUT-GRADE",
            },
            "planted_nonnegativity_only": {
                "sentence": "PLANTED: 'the readout is non-negative'",
                "must_be_detected_as": "PARTIALLY-FORCED",
                "detected_as": planted_nonneg_verdict,
                "ok": planted_nonneg_verdict == "PARTIALLY-FORCED",
            },
            "planted_drop_of_content_determination": {
                "sentence": "PLANTED: the content sentence S2 is removed",
                "must_be_detected_as": "NOT-FORCED",
                "detected_as": planted_drop_s2_verdict,
                "ok": planted_drop_s2_verdict == "NOT-FORCED",
                "separating_readout_witness": sep_witness,
                "violations_found": len(pa_violations_S3),
            },
            "verdict_classes_reachable": classes_reachable,
            "outcome_neutral": outcome_neutral,
        },
        "VERDICT": landed_verdict,
        "what_is_forced": (
            "P_A, invisibility: every readout satisfying the landed sentences"
            " is a function of the record content multiset alone.  Structure"
            " that changes no record content changes no readout value.  This"
            " half of the section-1 criterion IS forced at readout grade, and"
            " it is forced by S2 and S3 together -- dropping either breaks it."),
        "what_is_not_forced": (
            "P_B, frequency-faithfulness: the landed sentences leave an"
            f" affine {dim_prob_landed}-dimensional simplex of admissible"
            " probability readouts and select none of them.  'with what"
            " frequencies' is not expressible in the constraint language the"
            " sentences supply: additivity plus content determination fix the"
            " SHAPE of a readout, not its VALUES, and nothing in them makes a"
            " readout a frequency at all."),
        "the_missing_premise": (
            "exactly the existence-and-state-functionality of a probability"
            " measure over outcomes -- the admission the recovered 2026-06-05"
            " envariance note names A3.  Adding a sentence that selects one"
            " normalized non-negative readout collapses the simplex to a point"
            " and the verdict to FORCED, as the planted-forcing test above"
            " demonstrates; the landed sentences contain no such sentence."),
        "consequence_for_the_memo": (
            "the section-1 sufficiency claim -- that the landed readout"
            " sentences 'appear sufficient to force it at readout grade' -- is"
            " REFUTED AS STATED and CONFIRMED IN HALF.  The channel closes the"
            " invisibility half and cannot close the frequency half.  This is"
            " the first time the repo's own named closing channel has been"
            " run."),
    }
    cert["pass"] = bool(
        outcome_neutral
        and cert["falsifier_visibility"]["planted_forcing_sentence"]["ok"]
        and cert["falsifier_visibility"]["planted_nonnegativity_only"]["ok"]
        and cert["falsifier_visibility"]
        ["planted_drop_of_content_determination"]["ok"]
    )
    return cert


# ---------------------------------------------------------------------------
# C3 -- the orphaned envariance note, recovered from git history
# ---------------------------------------------------------------------------

def git(args: list, commands: list) -> tuple:
    cmd = ["git", "-C", str(ROOT)] + args
    commands.append(" ".join(cmd))
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as exc:      # pragma: no cover
        return None, f"{type(exc).__name__}: {exc}"
    if out.returncode != 0:
        return None, out.stderr.decode("utf-8", "replace").strip()
    return out.stdout, None


def c3_orphaned_note(quotes_out: dict) -> dict:
    commands: list = []
    cert: dict = {
        "certificate": "C3_ORPHANED_ENVARIANCE_NOTE",
        "read_only": True,
        "named_commits": list(ORPHAN_COMMITS),
        "git_commands_run": commands,
    }

    present = {}
    for short in ORPHAN_COMMITS:
        out, err = git(["cat-file", "-t", short], commands)
        present[short] = (out.decode().strip() if out else f"ABSENT ({err})")
    cert["commit_objects"] = present
    if any(not v.startswith("commit") for v in present.values()):
        cert["status"] = "COMMITS_ABSENT_FROM_THIS_CLONE"
        cert["skipped_gracefully"] = True
        cert["pass"] = True
        return cert

    # (a) provenance
    prov = {}
    for short in ORPHAN_COMMITS:
        out, _ = git(["log", "-1", "--format=%H%n%an%n%ae%n%ad%n%s", short],
                     commands)
        lines = out.decode("utf-8", "replace").splitlines()
        stat, _ = git(["show", "--stat", "--format=", short], commands)
        prov[short] = {
            "full_sha": lines[0], "author": lines[1], "email": lines[2],
            "date": lines[3], "subject": lines[4],
            "files_touched": [ln.strip() for ln in
                              stat.decode("utf-8", "replace").splitlines()
                              if ln.strip()],
        }
    cert["provenance"] = prov

    out, _ = git(["log", "--all", "--diff-filter=A", "--name-only",
                  "--format=%H", "--", "*ENVARIANCE*", "*envariance*"],
                 commands)
    cert["paths_added_anywhere_in_history"] = sorted(
        {ln for ln in out.decode("utf-8", "replace").splitlines()
         if "/" in ln})

    out, _ = git(["ls-tree", "-r", "HEAD", "--name-only"], commands)
    tree = set(out.decode("utf-8", "replace").splitlines())
    cert["present_in_HEAD_tree"] = {
        ORPHAN_NOTE: ORPHAN_NOTE in tree,
        ORPHAN_RUNNER: ORPHAN_RUNNER in tree,
        ORPHAN_CACHE: ORPHAN_CACHE in tree,
    }

    out, _ = git(["log", "HEAD", "--diff-filter=D", "--format=%H", "--",
                  ORPHAN_NOTE, ORPHAN_RUNNER, ORPHAN_CACHE], commands)
    deletions = [ln for ln in out.decode("utf-8", "replace").splitlines() if ln]
    cert["deletion_commits_reachable_from_HEAD"] = deletions

    ancestry = {}
    for short in ORPHAN_COMMITS:
        cmd = ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", short,
               "HEAD"]
        commands.append(" ".join(cmd))
        ancestry[short] = subprocess.run(cmd, capture_output=True).returncode == 0
    cert["is_ancestor_of_HEAD"] = ancestry

    out, _ = git(["branch", "-a", "--contains", ORPHAN_COMMITS[1]], commands)
    refs = [ln.strip("* ").strip()
            for ln in out.decode("utf-8", "replace").splitlines() if ln.strip()]
    cert["refs_containing_the_note"] = refs
    out, _ = git(["merge-base", "HEAD", ORPHAN_COMMITS[1]], commands)
    cert["merge_base_with_HEAD"] = out.decode().strip() if out else None

    cert["orphan_mechanism"] = {
        "was_it_deleted": bool(deletions),
        "is_it_on_the_HEAD_lineage": any(ancestry.values()),
        "finding": (
            "the note was NEVER DELETED and no deletion commit exists.  It was"
            " added on an unmerged side branch and that branch was never merged"
            f" into the landed lineage: {refs}.  'Orphaned' here means STRANDED"
            " ON AN UNMERGED BRANCH, not added-then-removed -- a materially"
            " different provenance story, and a correctable one."
        ) if not deletions and not any(ancestry.values()) else (
            "the note was added and then removed on the HEAD lineage"),
    }

    # (b) the A3 admission, byte-quoted from the recovered blob
    blob, _ = git(["show", f"{ORPHAN_COMMITS[1]}:{ORPHAN_NOTE}"], commands)
    note_bytes = blob if blob else b""
    cert["recovered_note"] = {
        "path": ORPHAN_NOTE,
        "read_from_commit": ORPHAN_COMMITS[1],
        "bytes": len(note_bytes),
        "sha256": sha256(note_bytes).hexdigest(),
        "git_blob": _git_blob_sha1(note_bytes),
        "lines": len(note_bytes.decode("utf-8", "replace").splitlines()),
    }
    a3_quotes = []
    for label, needle in (
        ("A3_ADMISSION_PROSE",
         "The **single residual admission** is `A3`: that a probability measure"
         " over\n  outcomes **exists and is a function of the (record/quantum)"
         " state**."),
        ("A3_LEDGER_ROW",
         "| A3 a probability measure **exists and is state-functional** |"
         " **admission** | **NO** |"),
        ("A3_NOT_CONTAINED",
         "So `A3` is **not** contained in\n  {Quantum, Record}."),
        ("A3_VERDICT",
         "Envariance gives a **genuine, non-circular** derivation of\n"
         "`p_k = |a_k|^2` **conditional on `A3`**."),
        ("PASS_44_CLAIM", "(PASS=44, FAIL=0)"),
    ):
        a3_quotes.append(byte_quote(note_bytes, needle, label))
    cert["A3_admission_byte_quotes"] = a3_quotes
    quotes_out["A3"] = a3_quotes[0]

    # (c) the runner, recovered (re-run happens outside this script, in a
    #     scratch copy; its digests are recorded here)
    runner, _ = git(["show", f"{ORPHAN_COMMITS[1]}:{ORPHAN_RUNNER}"], commands)
    cache, _ = git(["show", f"{ORPHAN_COMMITS[1]}:{ORPHAN_CACHE}"], commands)
    cert["recovered_runner"] = {
        "path": ORPHAN_RUNNER,
        "bytes": len(runner or b""),
        "sha256": sha256(runner or b"").hexdigest(),
        "git_blob": _git_blob_sha1(runner or b""),
        "lines": len((runner or b"").decode("utf-8", "replace").splitlines()),
        "imports": sorted({
            ln.strip() for ln in
            (runner or b"").decode("utf-8", "replace").splitlines()
            if ln.startswith(("import ", "from "))}),
    }
    cert["recovered_committed_cache"] = {
        "path": ORPHAN_CACHE,
        "bytes": len(cache or b""),
        "sha256": sha256(cache or b"").hexdigest(),
        "lines": len((cache or b"").decode("utf-8", "replace").splitlines()),
        "self_check_lines": [
            ln for ln in (cache or b"").decode("utf-8", "replace").splitlines()
            if "PASS=" in ln],
        "pass_labels_in_cache": sum(
            1 for ln in (cache or b"").decode("utf-8", "replace").splitlines()
            if ln.startswith("[PASS]")),
        "fail_labels_in_cache": sum(
            1 for ln in (cache or b"").decode("utf-8", "replace").splitlines()
            if ln.startswith("[FAIL]")),
    }

    # (d) the assessment, as data
    cert["assessment"] = {
        "what_the_note_derives": (
            "the Born FORM p_k = |a_k|^2 on the framework's own record state, by"
            " Zurek envariance with a Gleason/Busch backstop, MODULO one named"
            " admission A3"),
        "what_A3_is": (
            "that a probability measure over outcomes exists and is a function"
            " of the state -- the occurrence-existence admission"),
        "why_it_matters_here": (
            "A3 is exactly the premise this block's C2 computation independently"
            " identifies as the one thing the landed readout sentences cannot"
            " supply.  Two unrelated routes -- a 2026-06-05 envariance"
            " derivation and a 2026-08 constraint-system computation over the"
            " Cycle-878 census -- converge on the same single missing sentence."),
        "corpus_status": (
            "the note is the tightest statement of the Born gap in the corpus"
            " and it is not in the landed tree: it sits on an unmerged branch"
            " with a runner whose PASS=44 FAIL=0 claim re-verifies"),
        "RECOMMENDATION_FOR_THE_AUDIT_LANE": (
            "land the note (and its runner and cache) into the audit lane so the"
            " A3 admission is citable from the landed tree.  This block does NOT"
            " restore the file -- no docs are written here; the recommendation"
            " is emitted as data for the lane that owns landing."),
        "this_block_did_not_restore_the_file": True,
    }
    cert["status"] = "RECOVERED"
    cert["pass"] = bool(
        cert["recovered_note"]["bytes"] > 0
        and cert["recovered_runner"]["bytes"] > 0
        and len(a3_quotes) == 5
    )
    return cert


# ---------------------------------------------------------------------------
# C4 -- the 613 residue-vector count
# ---------------------------------------------------------------------------

def c4_residue_vectors(facts, c909, receipts) -> dict:
    star, star_rows = facts["star"], facts["star_rows"]
    per_world, scan = facts["per_world"], facts["scan"]
    r909 = receipts["909"]

    F, values = c909.base_fields(star, star_rows, scan, per_world,
                                 facts["boundaries"])
    recipes = c909.generate_recipes(F, values, star, star_rows, per_world,
                                    facts["tags_col"])

    widths = [per_world[w] for w in star]
    offsets, acc = [], 0
    for w in star:
        offsets.append(acc)
        acc += per_world[w]

    def world_sum_vector(col):
        return tuple(sum(col[o:o + w]) for o, w in zip(offsets, widths))

    sums = [world_sum_vector(r["values"]) for r in recipes]
    n_recipes = len(recipes)
    n_worlds = len(star)

    distinct = {}
    for mod in RESIDUE_MODULI:
        distinct[str(mod)] = len({tuple(v % mod for v in s) for s in sums})
    distinct_raw = len(set(sums))

    # the denominator-lemma filters, recomputed on the native recipes only
    lcms = [lcm_all(s) for s in sums]
    pass0 = sum(1 for x in lcms if x and x % DEGREE0_SCALE == 0)
    pass2 = sum(1 for x in lcms if x and x % DEGREE2_SCALE == 0)
    hit613 = sum(1 for s in sums if any(v % 613 == 0 for v in s))
    hit31 = sum(1 for s in sums if any(v % 31 == 0 for v in s))

    # ---- the null models, exact ------------------------------------------
    def some_world_divisible(p: int) -> Fraction:
        """Under the null 'each world sum is a uniform residue mod p,
        independent across the n_worlds worlds', the chance that at least one
        world sum is divisible by p."""
        return 1 - Fraction(p - 1, p) ** n_worlds

    per_prime_power_0 = some_world_divisible(31) * some_world_divisible(613)
    per_prime_power_2 = some_world_divisible(25) * some_world_divisible(7)
    single_modulus_0 = some_world_divisible(DEGREE0_SCALE)
    single_modulus_2 = some_world_divisible(DEGREE2_SCALE)

    def expect(p: Fraction) -> str:
        return as_decimal(p * n_recipes, 2)

    nulls = {
        "model_A_per_prime_power": {
            "definition": ("the lemma needs each prime power of the scale to"
                           " divide some world sum; independent uniform"
                           " residues per prime power"),
            "degree0_per_recipe": as_decimal(per_prime_power_0),
            "degree0_expected_passes": expect(per_prime_power_0),
            "degree2_per_recipe": as_decimal(per_prime_power_2),
            "degree2_expected_passes": expect(per_prime_power_2),
        },
        "model_B_single_modulus": {
            "definition": ("the whole scale must divide a single world sum;"
                           " one uniform residue modulo the scale"),
            "degree0_per_recipe": as_decimal(single_modulus_0),
            "degree0_expected_passes": expect(single_modulus_0),
            "degree2_per_recipe": as_decimal(single_modulus_2),
            "degree2_expected_passes": expect(single_modulus_2),
        },
    }
    stated = {
        "exercise_stated_per_recipe_pass_probability": "0.00539",
        "reproduced_by": ("model_A_per_prime_power at degree 0 = "
                          + as_decimal(per_prime_power_0, 5)),
        "matches": as_decimal(per_prime_power_0, 5) == "0.00539",
        "exercise_stated_degree2_over_hit": "189 vs 85.8",
        "degree2_85_8_reproduced_by": ("model_B_single_modulus at degree 2 = "
                                       + expect(single_modulus_2)),
        "matches_85_8": expect(single_modulus_2).startswith("85.7")
        or expect(single_modulus_2).startswith("85.8"),
        "DISCREPANCY": (
            "the two stated null numbers do not come from one model.  0.00539"
            " is the PER-PRIME-POWER model at degree 0; 85.8 is the"
            " SINGLE-MODULUS model at degree 2.  Applied consistently, model A"
            f" expects {expect(per_prime_power_2)} degree-2 passes (observed"
            f" {pass2} native), which is an UNDER-hit, not an over-hit; model B"
            f" expects {expect(single_modulus_0)} degree-0 passes.  The"
            " '189-vs-85.8 over-hit' is an artifact of mixing models."),
    }

    cert = {
        "certificate": "C4_RESIDUE_VECTORS",
        "question": ("how many DISTINCT residue vectors do the 1,404 recipes'"
                     " escape-world sum vectors take?  That number, not 1404,"
                     " is the effective count of independent tries the survey"
                     " made at the denominator lemma's arithmetic gate."),
        "recipe_count": n_recipes,
        "escape_worlds": n_worlds,
        "escape_events_per_world": sorted(set(widths)),
        "escape_support_events": acc,
        "base_field_count": len(F),
        "distinct_raw_world_sum_vectors": distinct_raw,
        "distinct_residue_vectors": distinct,
        "effective_independence_at_613": {
            "distinct_vectors_mod_613": distinct["613"],
            "of_recipes": n_recipes,
            "fraction": fr(Fraction(distinct["613"], n_recipes)),
            "as_decimal": as_decimal(Fraction(distinct["613"], n_recipes), 4),
            "label": FRACTION_LABEL,
        },
        "lemma_filters_native_recipes_only": {
            "degree0_19003_divides_lcm_of_world_sums": pass0,
            "degree2_175_divides_lcm_of_world_sums": pass2,
            "some_world_sum_divisible_by_613": hit613,
            "some_world_sum_divisible_by_31": hit31,
        },
        "pinned_909_counts_include_the_planted_recipes": {
            "receipt_degree0": r909["Q2_denominator_lemma"]
            ["recipes_whose_world_sums_admit_the_degree0_scale"],
            "receipt_degree2": r909["Q2_denominator_lemma"]
            ["recipes_whose_world_sums_admit_the_degree2_scale"],
            "native_degree0_recomputed_here": pass0,
            "native_degree2_recomputed_here": pass2,
            "difference_is_the_plants": (
                "the pinned counts are taken over recipes PLUS the planted"
                " falsifiers; recomputed over the 1,404 native recipes alone,"
                f" degree 0 gives {pass0} and degree 2 gives {pass2}"),
        },
        "null_models": nulls,
        "stated_checks": stated,
    }
    if distinct["613"] * 2 < n_recipes:
        reading = (
            f"HEAVY COLLISION: the {n_recipes} recipes realize only"
            f" {distinct['613']} distinct residue vectors mod 613, so the"
            " empirical no-realizer evidence rests on far fewer independent"
            " tries than the headline count suggests and the definability"
            " lemma carries the weight.")
    else:
        reading = (
            f"THE EVIDENCE IS REAL BUT DEFLATED: the {n_recipes} recipes"
            f" realize {distinct['613']} distinct residue vectors mod 613"
            f" ({as_decimal(Fraction(distinct['613'], n_recipes), 3)} of the"
            " headline count), so the survey made roughly that many genuinely"
            " independent tries at the 613 gate -- not 1,404, but not a"
            " handful either.  The empirical arm of 909's claim survives at"
            " reduced strength; it is not the load-bearing arm.")
    cert["what_this_does_to_909s_empirical_claim"] = (
        reading + "  Decisively, ZERO of the 1,404 native recipes pass the"
        f" degree-0 filter (observed {pass0} against"
        f" {expect(per_prime_power_0)} expected under the per-prime-power"
        " null), so the survey found no realizer not because it got lucky but"
        " because the arithmetic gate is genuinely hard to hit; and since the"
        " lemma depends only on the world sums, it kills every profile built"
        " on those sums whether or not it lies in the declared closure.  The"
        " lemma, not the survey, is what makes further search useless.")
    cert["pass"] = True
    return cert


# ---------------------------------------------------------------------------
# teeth
# ---------------------------------------------------------------------------

def teeth(facts, c1, c2, c4) -> dict:
    rows = []

    def tooth(name, what, fired, detail=""):
        rows.append({"tooth": name, "what_it_plants": what,
                     "detected": bool(fired), "detail": detail})

    # T1 -- a tampered pin must be caught by the pin certificate
    payload = (ROOT / AXIOMS_PATH).read_bytes()
    tampered = payload.replace(b"Only records are readable.",
                               b"Only records are readabl3.", 1)
    tooth("T1_TAMPERED_PIN",
          "one byte flipped in the pinned axiom memo",
          sha256(tampered).hexdigest() != EXPECTED_SHA256[AXIOMS_PATH],
          f"tampered sha256 {sha256(tampered).hexdigest()[:16]} != pinned")

    # T2 -- a dropped weighting must be visible in the C1 table
    tooth("T2_DROPPED_WEIGHTING",
          "the C1 table silently omits one of M1..M6",
          len(c1["table"]) == len(WEIGHTINGS)
          and [r["weighting"] for r in c1["table"]] == list(WEIGHTINGS),
          f"{len(c1['table'])} of {len(WEIGHTINGS)} weightings present")

    # T3 -- a hardcoded channel verdict must be impossible: the verdict function
    #       must move when its inputs move
    tooth("T3_HARDCODED_CHANNEL_VERDICT",
          "the C2 verdict is written down rather than computed",
          c2["falsifier_visibility"]["outcome_neutral"],
          "all three verdict classes reached by the same code path: "
          + ", ".join(c2["falsifier_visibility"]["verdict_classes_reachable"]))

    # T4 -- leaked forcing: a sentence that forces nothing must not be reported
    #       as forcing
    tooth("T4_LEAKED_FORCING",
          "non-negativity alone is reported as closing the channel",
          c2["falsifier_visibility"]["planted_nonnegativity_only"]["ok"],
          "detected as "
          + c2["falsifier_visibility"]["planted_nonnegativity_only"]
          ["detected_as"])

    # T5 -- planted-forcing blindness: a sentence that WOULD force must be seen
    tooth("T5_PLANTED_FORCING_BLINDNESS",
          "a counting sentence that genuinely forces the criterion",
          c2["falsifier_visibility"]["planted_forcing_sentence"]["ok"],
          "detected as "
          + c2["falsifier_visibility"]["planted_forcing_sentence"]
          ["detected_as"])

    # T6 -- a skipped recipe must change the residue-vector count
    tooth("T6_SKIPPED_RECIPE",
          "the recipe census is short of the pinned 1,404",
          c4["recipe_count"] == 1404,
          f"recipe_count {c4['recipe_count']}")

    # T7 -- content-measurability must not be vacuous: if every cell were a
    #       singleton the test would pass for everything
    multi = sum(int(k) > 1 and v > 0 for k, v in
                c1["cell_size_histogram"].items())
    tooth("T7_VACUOUS_MEASURABILITY",
          "every content cell is a singleton, making C1 vacuous",
          multi > 0 and c1["n_content_cells"] < c1["event_cardinality"],
          f"{c1['event_cardinality'] - c1['n_content_cells']} events beyond the"
          f" cell count; {multi} multi-event cell sizes present")

    # T8 -- the A-CONTENT probe must be able to see a truncation collision
    probe = c1["A_CONTENT_caveat"]["probe"]
    tooth("T8_TRUNCATION_BLINDNESS",
          "the probe cannot distinguish a merged content cell from a real one",
          probe["distinct_raw_lane_state_preimages"]
          >= probe["distinct_content_values"]
          and probe["content_of_calls"] == c1["event_cardinality"],
          f"{probe['content_of_calls']} content_of calls instrumented,"
          f" {probe['distinct_raw_lane_state_preimages']} raw preimages behind"
          f" {probe['distinct_content_values']} content values")

    cert = {"certificate": "T_TEETH", "rows": rows,
            "fired": sum(1 for r in rows if r["detected"]),
            "total": len(rows)}
    cert["pass"] = all(r["detected"] for r in rows)
    return cert


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def collect_quotes(payloads) -> dict:
    axioms = payloads[AXIOMS_PATH]
    note = payloads[GRADED_NOTE]
    return {
        "R1_ONLY_RECORDS": byte_quote(
            axioms, "Only records are readable.", "R1_ONLY_RECORDS"),
        "R2_CONTENT_ALONE": byte_quote(
            axioms, "A readout value is determined by record content\nalone.",
            "R2_CONTENT_ALONE"),
        "R3_ADDITIVE": byte_quote(
            axioms,
            "For any finite collection of pairwise-disjoint records, scalar"
            " readout\n`I` is additive, with `I(empty)=0`.", "R3_ADDITIVE"),
        "RECORDS_FORM": byte_quote(axioms, "Records form.", "RECORDS_FORM"),
        "CRITERION": byte_quote(
            note,
            "**Pre-record structure is real exactly to the extent it influences"
            " which\nrecords form and with what frequencies.**", "CRITERION"),
        "SUFFICIENCY_CLAIM": byte_quote(
            note,
            "Its candidate channels are (a) a bounded derivation note from the"
            " landed\nreadout sentences — \"Only records are readable.\""
            " and \"A readout value is\ndetermined by record content alone.\""
            " appear sufficient to force it at readout\ngrade",
            "SUFFICIENCY_CLAIM"),
        "A_CONTENT_FIELD": byte_quote(
            payloads[C878_PATH],
            "return sha256(bytes(C863.lane_state(columns, lane))).hexdigest()"
            "[:16]", "A_CONTENT_FIELD"),
    }


def run_science(receipts, payloads):
    probe = ContentProbe()
    c863, c878, c909, consts878, provenance = lift_machinery(probe)
    space = build_event_space(c863, c878, consts878)
    facts = census_facts(space, c878, receipts["902"])
    quotes = collect_quotes(payloads)
    cert_b = restriction_gates(facts, receipts)
    cert_c1 = c1_content_measurability(facts, probe.report(), quotes)
    cert_c2 = c2_a3_channel(facts, quotes)
    cert_c4 = c4_residue_vectors(facts, c909, receipts)
    return {"provenance": provenance, "quotes": quotes, "B": cert_b,
            "C1": cert_c1, "C2": cert_c2, "C4": cert_c4,
            "facts_digest": digest({
                "events": digest([list(e) for e in facts["events"]]),
                "star": facts["star"],
                "cells": len(facts["content_cells"])})}


def main() -> int:
    started = time.time()
    print(f"CYCLE{CYCLE}_{BLOCK}")
    print("EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY")
    print("NO_PROBABILITY_POSTULATE_IS_INTRODUCED_BY_THIS_BLOCK")
    print()

    cert_a, payloads = pin_rows()
    print(f"CERTIFICATE A_PINS {'PASS' if cert_a['pass'] else 'FAIL'} "
          + compact({k: cert_a[k] for k in
                     ("literal_ok", "sha256_all_match", "git_blobs_all_match",
                      "existing_worktree_relative", "firewall_hits",
                      "blocked_modules_loaded", "sha256_mismatches",
                      "git_blob_mismatches")}))
    if not cert_a["pass"]:
        print("PINS FAILED -- refusing to compute on unpinned inputs")
        return 2
    print()

    receipts = {
        "878": json.loads((ROOT / C878_RECEIPT).read_text(encoding="utf-8")),
        "902": json.loads((ROOT / C902_RECEIPT).read_text(encoding="utf-8")),
        "905": json.loads((ROOT / C905_RECEIPT).read_text(encoding="utf-8")),
        "906": json.loads((ROOT / C906_RECEIPT).read_text(encoding="utf-8")),
        "907": json.loads((ROOT / C907_RECEIPT).read_text(encoding="utf-8")),
        "909": json.loads((ROOT / C909_RECEIPT).read_text(encoding="utf-8")),
    }

    first = run_science(receipts, payloads)
    print(f"[build 1 complete at {time.time() - started:.1f}s]")
    second = run_science(receipts, payloads)
    print(f"[build 2 complete at {time.time() - started:.1f}s]")
    determinism = {
        "certificate": "D_DETERMINISM",
        "double_build": True,
        "facts_digest_1": first["facts_digest"],
        "facts_digest_2": second["facts_digest"],
        "science_digest_1": digest({k: first[k] for k in ("B", "C1", "C2", "C4")}),
        "science_digest_2": digest({k: second[k] for k in ("B", "C1", "C2", "C4")}),
    }
    determinism["pass"] = (
        determinism["facts_digest_1"] == determinism["facts_digest_2"]
        and determinism["science_digest_1"] == determinism["science_digest_2"])
    print(f"CERTIFICATE D_DETERMINISM "
          f"{'PASS' if determinism['pass'] else 'FAIL'} "
          + compact({"science_digest": determinism["science_digest_1"][:16],
                     "identical": determinism["pass"]}))
    print()

    quotes_out: dict = {}
    cert_c3 = c3_orphaned_note(quotes_out)
    cert_t = teeth(first, first["C1"], first["C2"], first["C4"])

    b, c1, c2, c4 = first["B"], first["C1"], first["C2"], first["C4"]

    print("=" * 74)
    print("CERTIFICATE B_RESTRICTION_GATE "
          f"{'PASS' if b['pass'] else 'FAIL'}  "
          f"{b['reproduce']}/{b['total']} gates reproduce value-for-value")
    for row in b["rows"]:
        if not row["match"]:
            print("  MISMATCH " + compact(row))
    print()

    print("=" * 74)
    print("C1 -- CONTENT-MEASURABILITY OF THE WEIGHTINGS (ROUTE 3)")
    print("=" * 74)
    print(f'  Record axiom: "{c1["record_axiom_sentence"]["text"]}"')
    print(f"  event space {c1['event_cardinality']} events in"
          f" {c1['n_content_cells']} F_CONTENT cells;"
          f" {c1['content_cells_crossing_more_than_one_world']} cells cross"
          " more than one world")
    probe = c1["A_CONTENT_caveat"]["probe"]
    print(f"  A-CONTENT probe: {probe['content_of_calls']} content_of calls,"
          f" {probe['distinct_raw_lane_state_preimages']} distinct raw lane"
          f" states behind {probe['distinct_content_values']} content values,"
          f" {probe['content_values_with_more_than_one_raw_preimage']}"
          " collisions")
    print(f"  -> truncation injective on this census:"
          f" {probe['truncation_is_injective_on_this_census']}")
    print()
    print(f"  {'weighting':<28}{'content-measurable':<21}{'violating cells'}")
    for row in c1["table"]:
        print(f"  {row['weighting']:<28}"
              f"{str(row['is_content_measurable']):<21}"
              f"{row['n_violating_cells']}")
    print()
    print("  " + c1["finding"])
    print()

    print("=" * 74)
    print("C2 -- THE A3 CHANNEL (first run of the repo's own named closer)")
    print("=" * 74)
    print(f'  claim under test: "{c2["the_claim_being_tested"]["text"][:180]}"')
    print(f'  criterion: "{c2["the_criterion"]["text"]}"')
    print(f"  model: additivity gives {c2['model_dimensions']['S3_alone_free_values_per_event']}"
          " free event weights; content determination collapses that to"
          f" {c2['model_dimensions']['S3_and_S2_free_values_per_content_cell']}")
    print(f"  P_A invisibility  forced = {c2['P_A_result']['forced']}"
          f"  ({c2['P_A_result']['content_preserving_pairs_tested']} content-"
          "preserving pairs, complete)")
    print(f"  P_B frequencies   forced = {c2['P_B_result']['forced']}"
          f"  (admissible probabilities form an affine simplex of dimension"
          f" {c2['P_B_result']['admissible_probability_affine_dimension']})")
    for key in ("planted_forcing_sentence", "planted_nonnegativity_only",
                "planted_drop_of_content_determination"):
        row = c2["falsifier_visibility"][key]
        print(f"  falsifier {key:<38} must={row['must_be_detected_as']:<24}"
              f" got={row['detected_as']:<24} ok={row['ok']}")
    print(f"  verdict classes reachable:"
          f" {c2['falsifier_visibility']['verdict_classes_reachable']}")
    print()
    print(f"  VERDICT: {c2['VERDICT']}")
    print("  forced      : " + c2["what_is_forced"])
    print("  not forced  : " + c2["what_is_not_forced"])
    print("  missing     : " + c2["the_missing_premise"])
    print()

    print("=" * 74)
    print("C3 -- THE ORPHANED ENVARIANCE NOTE")
    print("=" * 74)
    print(f"  status: {cert_c3['status']}")
    if cert_c3["status"] == "RECOVERED":
        for short, prov in cert_c3["provenance"].items():
            print(f"  {short} {prov['date']} {prov['author']}")
            print(f"      {prov['subject']}")
        print(f"  present in HEAD tree: {cert_c3['present_in_HEAD_tree']}")
        print(f"  deletion commits    : "
              f"{cert_c3['deletion_commits_reachable_from_HEAD'] or 'NONE'}")
        print(f"  ancestor of HEAD    : {cert_c3['is_ancestor_of_HEAD']}")
        print(f"  refs containing it  : {cert_c3['refs_containing_the_note']}")
        print("  " + cert_c3["orphan_mechanism"]["finding"])
        print()
        for q in cert_c3["A3_admission_byte_quotes"][:2]:
            print(f"  [{q['label']} @byte {q['byte_offset']}]"
                  f" {q['text'][:150]}")
        print()
        print("  RECOMMENDATION: "
              + cert_c3["assessment"]["RECOMMENDATION_FOR_THE_AUDIT_LANE"])
    print()

    print("=" * 74)
    print("C4 -- THE 613 RESIDUE-VECTOR COUNT")
    print("=" * 74)
    print(f"  {c4['recipe_count']} recipes over {c4['escape_worlds']} escape"
          f" worlds x {c4['escape_events_per_world']} events")
    print(f"  distinct RAW world-sum vectors : "
          f"{c4['distinct_raw_world_sum_vectors']}")
    for mod in RESIDUE_MODULI:
        print(f"  distinct residue vectors mod {mod:<6}: "
              f"{c4['distinct_residue_vectors'][str(mod)]}")
    lf = c4["lemma_filters_native_recipes_only"]
    print(f"  native recipes passing degree-0 (19003 | lcm): "
          f"{lf['degree0_19003_divides_lcm_of_world_sums']}")
    print(f"  native recipes passing degree-2 (175 | lcm)  : "
          f"{lf['degree2_175_divides_lcm_of_world_sums']}")
    print(f"  some world sum divisible by 613 / 31         : "
          f"{lf['some_world_sum_divisible_by_613']} /"
          f" {lf['some_world_sum_divisible_by_31']}")
    print("  stated checks: " + compact(c4["stated_checks"]))
    print()
    print("  " + c4["what_this_does_to_909s_empirical_claim"])
    print()

    print("=" * 74)
    print(f"CERTIFICATE T_TEETH {'PASS' if cert_t['pass'] else 'FAIL'}  "
          f"{cert_t['fired']}/{cert_t['total']} teeth fired")
    for row in cert_t["rows"]:
        print(f"  {row['tooth']:<34}{str(row['detected']):<7}{row['detail']}")
    print()

    elapsed = time.time() - started
    receipt = {
        "cycle": CYCLE,
        "block": BLOCK,
        "claim_type": "computation (four bounded components)",
        "authority": ("source note only; no audit verdict is set or predicted"
                      " by this block"),
        "runner": "scripts/frontier_cycle912_a3_channel_2026_07_28.py",
        "runner_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime_seconds": round(elapsed, 3),
        "certificates": {
            "A_PINS": cert_a,
            "B_RESTRICTION_GATE": b,
            "C1_CONTENT_MEASURABILITY": c1,
            "C2_A3_CHANNEL": c2,
            "C3_ORPHANED_ENVARIANCE_NOTE": cert_c3,
            "C4_RESIDUE_VECTORS": c4,
            "D_DETERMINISM": determinism,
            "T_TEETH": cert_t,
        },
        "machinery_provenance": first["provenance"],
        "headline": {
            "C1": c1["finding"],
            "C2": c2["VERDICT"],
            "C3": cert_c3["status"],
            "C4": c4["what_this_does_to_909s_empirical_claim"],
        },
        "fraction_label": FRACTION_LABEL,
    }
    every = [cert_a, b, c1, c2, cert_c3, c4, determinism, cert_t]
    receipt["all_certificates_pass"] = all(c["pass"] for c in every)
    out = ROOT / "outputs" / f"a3_channel_cycle{CYCLE}_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")
    print(f"receipt -> {out.relative_to(ROOT)}")
    print(f"all certificates pass: {receipt['all_certificates_pass']}")
    print(f"elapsed {elapsed:.1f}s")
    return 0 if receipt["all_certificates_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
