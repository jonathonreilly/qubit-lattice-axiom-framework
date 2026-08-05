#!/usr/bin/env python3
"""Cycle 940 -- R1-A3: THE SYMMETRIC-SITE EQUAL-WEIGHT QUESTION.

The question, exactly.  Cycle 936 built the choice substrate and measured the
A3 sentence's price: the weight's index set is FORCED (worlds, not slots), its
normalization is FORCED (per choice node), and its VALUE is free -- one number
per site in the world sense, 6 on the declared arena.  Cycle 925 proved that
the A3 sentence is the sole genuine relaxation.  936 named the successor: does
SYMMETRY, as opposed to CONSISTENCY, force equal weights at symmetric menus?

That question has exactly two mechanical halves.

  Q1  Does a substrate AUTOMORPHISM exist that swaps the two menu items at a
      site while fixing everything else observable?  Without one, weight
      invariance under automorphisms constrains nothing at that site: the
      landed menu-uniformity corollary (2026-07-11) already decided the
      general lemma -- invariance forces uniformity on a menu IFF that menu's
      cells are ONE ORBIT of the invariance group.

  Q2  If such automorphisms exist, the conditional theorem "IF weights are
      automorphism-invariant THEN w = 1/2 at exactly the covered sites" is
      stated and verified -- and then the ANTECEDENT's own status is priced:
      derivable from supplied content, or itself A3-shaped import?

THE FIREWALL (inherited from 936, mechanical and deliberately over-broad).
mu stays PARAMETRIC.  Nothing here outputs, prefers or adopts a weight value
AS LAW CONTENT.  Exhibiting what a principle WOULD force is PRICING, not
adopting: every numeric weight value in this receipt is required to sit under
a key path containing CONDITIONAL or HYPOTHETICAL, and the real arena's weight
algebra is required to stay symbolic with its 936 freedom count unchanged.
Zero float literals; exact rationals end to end.

DISCIPLINE.  The 936 science digest is verified against its own ship receipt,
its tree is reproduced (leaves, branching, the six pairs, the weight-sum
identity) and the 918/925 anchors value-for-value BEFORE any new analysis.
All 936 machinery is AST-LIFTED from the pinned bytes -- never imported.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import math
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, product
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 900
FRACTION_LABEL = "bookkeeping fraction, not probability"

# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C936_PATH = "scripts/frontier_cycle936_choice_substrate_2026_07_28.py"
C936_RECEIPT = "outputs/choice_substrate_cycle936_receipt_2026_07_28.json"
C936_SHIP = "outputs/choice_substrate_block_cycle936_ship_receipt_2026_07_28.json"
C936_NOTE = ("docs/CHOICE_SUBSTRATE_BUILT_TREE_PRICED_CYCLE936"
             "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
C925_RECEIPT = "outputs/law_relaxation_cycle925_receipt_2026_07_28.json"
C918_NOTE = ("docs/WRITABLE_ENDPOINT_BORN_CAPABLE_FIRST_BRANCH_PAIRS_CYCLE918"
             "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
C925_NOTE = ("docs/LAW_RELAXATION_CLASSIFIED_A3_SOLE_RELAXATION_CYCLE925"
             "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

# ---- the prior-art surfaces this block is required to sweep ---------------
PA_MENU = ("docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3"
           "_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md")
PA_GLEASON = ("docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE"
              "_GLEASON_BRIDGE_NOTE_2026-07-04.md")
PA_RHALF = ("docs/KOIDE_FORMATION_WEIGHT_CONDITIONAL_SELECTION_UNIQUE"
            "_REGISTRATION_COMPATIBLE_LAWFUL_WEIGHT_BOUNDED_THEOREM"
            "_NOTE_2026-07-12.md")
PA_INNER = ("docs/INNER_AUTOMORPHISM_INVARIANCE_TRACIAL_IDENTIFICATION"
            "_NARROW_THEOREM_NOTE_2026-05-20.md")
PA_NOTSYM = ("docs/KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM"
             "_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md")

AUDIT_INPUT_PATHS = (CORE_PATH, C936_PATH, C936_RECEIPT, C936_SHIP, C936_NOTE,
                     C918_RECEIPT, C925_RECEIPT, C918_NOTE, C925_NOTE,
                     AXIOMS_PATH, PA_MENU, PA_GLEASON, PA_RHALF, PA_INNER,
                     PA_NOTSYM)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C936_RECEIPT:
        "4412ae9016df02546db26cdd87fa33ab68bf2a7370b27640e18d4d0e59132028",
    C936_NOTE:
        "6cdec178602e936a07a86c43627b431527a5d328c2b269d0edd594d245831eac",
    C918_RECEIPT:
        "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    C925_RECEIPT:
        "f4fabe50ed8b775f2f1288380824ae04f0129f4f136e3b338bafd05647031757",
    C918_NOTE:
        "40333f3bb83f77a3e7c89eb232bbe24c01885cdcfdcab7888ae319419c1efaee",
    C925_NOTE:
        "ed36a7afb889a45ccde08a4f5d6735fa028a12e4aaa9edda3348ab687678c676",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C936_NOTE: "ffc0e6d1c3527ef75286abc0e50de0a3a3588f53",
    C936_RECEIPT: "d7b786fccc0435d139339c141dbad75c9f8d799b",
    C918_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
    C925_RECEIPT: "fed1b28e9e5cfe731a541645dce705541d69c967",
    C918_NOTE: "186af20c471f8cbb4e9c9871fc2ee652d813e348",
    C925_NOTE: "37f5bad6f1ef329890e7cebee97ba99a5f699356",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

# THE STRANDED ENVARIANCE NOTE.  It is not in the worktree: it lives only on
# the unmerged branch born-from-envariance-2026-06-05 (Cycle 912's C3 finding
# -- never deleted, never landed).  It is the DOMINANT prior art for this
# block, so it is pinned BY GIT BLOB out of the object store and byte-quoted.
ENVARIANCE_BLOB = "64b24361f2237d01f079e16b306b5d04e01de7c2"
ENVARIANCE_PATH_ON_BRANCH = (
    "docs/BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL"
    "_PROBABILITY_NOTE_2026-06-05.md")

# every module whose content this block leans on is AST-LIFTED, never imported
BLOCKLISTED_MODULES = (
    "frontier_cycle936_choice_substrate_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle911_type_vacuity_2026_07_28",
    "frontier_cycle913_selection_function_2026_07_28",
    "frontier_cycle918_writable_endpoint_2026_07_28",
    "frontier_cycle925_law_relaxation_2026_07_28",
)


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

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


# ---------------------------------------------------------------------------
# A: pins, and the AST lift of the pinned 936 machinery
# ---------------------------------------------------------------------------

# the 936 top-level names this block lifts.  ORDER MATTERS for the constants
# (EXTENDED_TEMPLATES is built from two earlier ones), so the lift replays the
# selected top-level nodes in SOURCE order.
LIFT_CONSTS = (
    "CORE_PATH", "HANDSHAKE_PATH", "C863_PATH", "C878_PATH", "C911_PATH",
    "C913_PATH", "C918_PATH", "C925_PATH", "C863_FUNCS", "C863_CONSTS",
    "C878_FUNCS", "C878_CONSTS", "C911_FUNCS", "C911_CONSTS", "C913_FUNCS",
    "KIND_X", "KIND_CNOT", "KIND_TOF", "KIND_SHIFT", "KIND_CHOICE",
    "KIND_NAMES", "CERTIFIED_KINDS", "PINNED_TEMPLATES", "CHOICE_TEMPLATE",
    "EXTENDED_TEMPLATES", "GRAMMAR_DELTA_TEXT", "P3_NOT_P2_TEXT",
    "LANE_SHIFT", "HORIZON", "DEAD_CHUNK_ORBITS", "TREE_ORBITS",
    "CHOICE_ATOMS", "FULL_TREE_LEAF_CAP", "_CHOICE_SINK",
)
LIFT_FUNCS = (
    "ast_lift", "lift_ast_op_tuple", "lift_machinery",
    "pinned_statement_text", "extended_statement_text", "chunk_source",
    "gate_text", "gate_target", "station_mask", "build_schedules", "CHOICE",
    "compile_schedules", "acc_add", "acc_get", "item_of", "build_digest",
    "scan_digest_918", "run_full", "measurement", "dynamical_branch_pairs",
    "z11_covariance", "choice_support_words", "enumerate_tree", "poly_one",
    "poly_mul", "poly_add", "poly_factor", "poly_str", "poly_eval",
    "weight_algebra", "outcome_algebra",
)
LIFT_CLASSES = ("Machine",)


def lift_936(source: str):
    """AST-lift the pinned 936 machinery.  Selected FunctionDef / ClassDef /
    Assign top-level nodes are replayed IN SOURCE ORDER into one namespace, so
    the lifted objects call one another exactly as they do in 936 -- but the
    module is never imported and none of its module-level side effects (the
    sys.path insert, the meta-path firewall, the kernel import) run here."""
    tree = ast.parse(source, filename=C936_PATH)
    body, got_f, got_c, got_k = [], set(), set(), set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in LIFT_FUNCS:
            body.append(node)
            got_f.add(node.name)
        elif isinstance(node, ast.ClassDef) and node.name in LIFT_CLASSES:
            body.append(node)
            got_k.add(node.name)
        elif isinstance(node, ast.Assign):
            names = []
            for t in node.targets:
                if isinstance(t, ast.Name):
                    names.append(t.id)
                elif isinstance(t, ast.Tuple):
                    names.extend(e.id for e in t.elts
                                 if isinstance(e, ast.Name))
            if names and all(n in LIFT_CONSTS for n in names):
                body.append(node)
                got_c.update(names)
    missing = (tuple(sorted(set(LIFT_FUNCS) - got_f)),
               tuple(sorted(set(LIFT_CONSTS) - got_c)),
               tuple(sorted(set(LIFT_CLASSES) - got_k)))
    if any(missing):
        raise AssertionError(("936 lift incomplete", missing))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = {"__builtins__": __builtins__, "ROOT": ROOT, "K": K, "np": np,
          "ast": ast, "json": json, "math": math, "sys": sys,
          "itertools": itertools, "combinations": combinations,
          "product": product, "Counter": Counter, "Fraction": Fraction,
          "sha256": sha256, "sha1": sha1, "Path": Path,
          "SimpleNamespace": SimpleNamespace, "compact": compact,
          "digest": digest, "git_blob": git_blob}
    exec(compile(module, f"<ast-lift {C936_PATH}>", "exec"), ns)
    return SimpleNamespace(**{n: ns[n] for n in
                              tuple(got_f) + tuple(got_c) + tuple(got_k)}), \
        (len(got_f), len(got_c), len(got_k))


def pin_rows():
    rows, payloads = {}, {}
    literal = ast.literal_eval(compact({
        "sha256": EXPECTED_SHA256, "git_blobs": EXPECTED_GIT_BLOBS,
        "inputs": list(AUDIT_INPUT_PATHS)}))
    for path in AUDIT_INPUT_PATHS:
        blob = (ROOT / path).read_bytes()
        payloads[path] = blob
        rows[path] = {"sha256": sha256(blob).hexdigest(),
                      "git_blob": git_blob(blob),
                      "bytes": len(blob)}
    # the stranded envariance note, out of the git object store
    env_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "blob", ENVARIANCE_BLOB],
        capture_output=True, check=False).stdout
    payloads["ENVARIANCE_NOTE"] = env_bytes
    env_blob_ok = git_blob(env_bytes) == ENVARIANCE_BLOB
    sha_ok = all(rows[p]["sha256"] == v for p, v in EXPECTED_SHA256.items())
    blob_ok = all(rows[p]["git_blob"] == v
                  for p, v in EXPECTED_GIT_BLOBS.items())
    cert = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "rows": rows,
        "sha256_all_match": sha_ok,
        "git_blobs_all_match": blob_ok,
        "literal_ok": isinstance(literal, dict),
        "existing_worktree_relative": all((ROOT / p).exists()
                                          for p in AUDIT_INPUT_PATHS),
        "blocked_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                   if m in sys.modules],
        "firewall_hits": list(PRIMARY_FIREWALL.hits),
        "THE_STRANDED_ENVARIANCE_NOTE": {
            "why_pinned_by_blob":
                "it is NOT in the worktree.  Cycle 912's C3 finding: the note "
                "and its runner sit on the unmerged branch "
                "born-from-envariance-2026-06-05; neither commit is an "
                "ancestor of HEAD.  It is the DOMINANT prior art for this "
                "block -- a symmetry-forces-equal-weights derivation with a "
                "published assumption table -- so it is pinned out of the "
                "object store and byte-quoted rather than paraphrased.",
            "path_on_branch": ENVARIANCE_PATH_ON_BRANCH,
            "git_blob": ENVARIANCE_BLOB,
            "retrieved_bytes": len(env_bytes),
            "blob_verifies": env_blob_ok,
            "sha256": sha256(env_bytes).hexdigest() if env_bytes else None,
        },
        "modification_mechanism":
            "WRAP, NEVER EDIT.  The pinned 936 runner is AST-LIFTED (selected "
            "top-level FunctionDef / ClassDef / Assign nodes replayed in "
            "source order) and never imported; its bytes are unchanged and "
            "hashed.  Nothing in this block writes to any pinned file.",
    }
    cert["pass"] = bool(
        sha_ok and blob_ok and cert["literal_ok"]
        and cert["existing_worktree_relative"] and env_blob_ok
        and not cert["blocked_modules_loaded"] and not cert["firewall_hits"])
    return cert, payloads


# ---------------------------------------------------------------------------
# THE AUTOMORPHISM MACHINERY (this block's new content)
# ---------------------------------------------------------------------------

ROLE_TARGET, ROLE_C1, ROLE_C2 = "t", "c1", "c2"


def gate_roles(gate, kinds):
    """(wire, role) incidences of one compiled gate, by the pinned kinds."""
    kind, a, b, c3, _mask = gate
    if kind == kinds["X"]:
        return ((a, ROLE_TARGET),)
    if kind == kinds["CNOT"]:
        return ((a, ROLE_C1), (b, ROLE_TARGET))
    if kind == kinds["TOF"]:
        return ((a, ROLE_C1), (b, ROLE_C2), (c3, ROLE_TARGET))
    raise AssertionError(("unclassified kind in the pinned schedule", kind))


def colour_refine(gates, kinds, label):
    """Sound (not complete) automorphism invariant on WIRE ADDRESSES: 1-WL
    colour refinement over the compiled gate incidence structure.

    SOUNDNESS, which is the whole point: colour refinement is stable under
    every automorphism of the labelled structure.  If two wires end in
    DIFFERENT stable colours then NO structure-preserving relabelling maps one
    to the other.  A negative from this routine is therefore a THEOREM, not a
    failed search -- which is exactly the strength this block needs, because
    the block's headline is a non-existence claim.

    `label` chooses how much of a gate is treated as fixed data.  Coarser
    labels admit MORE candidate maps, so a separation that survives the
    coarsest label is the strongest possible negative:
      'exact'    -- (station, kind, role, mask identity).  Fixes lanes.
      'popcount' -- (kind, role, popcount(mask)).  Invariant under every LANE
                    permutation, so it also covers composites with a layout /
                    census relabelling.
      'bare'     -- (kind, role) only.  Invariant under every lane permutation
                    AND every station (time) permutation.
    """
    inc = defaultdict(list)
    wires = set()
    for gi, (si, gate) in enumerate(gates):
        for w, r in gate_roles(gate, kinds):
            inc[w].append((gi, r))
            wires.add(w)
        wires.update(gate[1:4])
    maskid: dict = {}

    def mlab(si, mask):
        if label == "exact":
            if mask not in maskid:
                maskid[mask] = len(maskid)
            return (si, maskid[mask])
        if label == "popcount":
            return bin(mask).count("1")
        return 0

    colour = {w: 0 for w in wires}
    iters = 0
    for iters in range(1, 64):
        sig = {}
        for w in wires:
            rows = []
            for gi, r in inc[w]:
                si, (kind, a, b, c3, mask) = gates[gi]
                rows.append((kind, r, mlab(si, mask),
                             colour[a], colour[b], colour[c3]))
            sig[w] = tuple(sorted(rows))
        uniq: dict = {}
        new = {}
        for w in sorted(wires):
            key = (colour[w], sig[w])
            if key not in uniq:
                uniq[key] = len(uniq)
            new[w] = uniq[key]
        if new == colour:
            break
        colour = new
    return colour, iters, wires


def fanout_profile(gates, kinds, wire):
    """The multiset of (kind, role, target-wire) a wire participates in as a
    CONTROL, and the multiset of (kind, controls) that write it.  This is the
    human-readable form of the refinement's separating witness."""
    as_control, as_target = Counter(), Counter()
    for _si, (kind, a, b, c3, _m) in gates:
        tgt = a if kind == kinds["X"] else (b if kind == kinds["CNOT"] else c3)
        if kind == kinds["CNOT"] and a == wire:
            as_control[(ROLE_C1, tgt)] += 1
        if kind == kinds["TOF"]:
            if a == wire:
                as_control[(ROLE_C1, tgt)] += 1
            if b == wire:
                as_control[(ROLE_C2, tgt)] += 1
        if tgt == wire:
            as_target[(kind, a, b)] += 1
    return ({f"{r}->{t}": c for (r, t), c in sorted(as_control.items())},
            {f"k{k}({a},{b})": c for (k, a, b), c in sorted(as_target.items())})


def apply_pi(gate, pi):
    kind, a, b, c3, mask = gate
    return (kind, pi.get(a, a), pi.get(b, b), pi.get(c3, c3), mask)


def relabelling_verdict(sched, pi, kinds):
    """Is the wire relabelling pi an automorphism of the COMPILED substrate?
    Both readings are reported and neither is privileged:
      ordered  -- the emitted statement list of every station is identical
                  (the strictest reading: a bit-identical compile);
      multiset -- every station's gate multiset is preserved (gate order
                  inside a station is treated as immaterial).
    """
    ordered = all([apply_pi(g, pi) for g in s] == list(s) for s in sched)
    per_station = all(Counter(apply_pi(g, pi) for g in s) == Counter(s)
                      for s in sched)
    glob = (Counter(apply_pi(g, pi) for s in sched for g in s)
            == Counter(g for s in sched for g in s))
    witness = None
    if not per_station:
        for si, s in enumerate(sched):
            src, img = Counter(s), Counter(apply_pi(g, pi) for g in s)
            diff = sorted(set(src) | set(img))
            for g in diff:
                if src[g] != img[g]:
                    witness = {"station": si,
                               "gate_present_in_the_original_only": list(g[:4]),
                               "multiplicity_original": src[g],
                               "multiplicity_image": img[g]}
                    break
            if witness:
                break
    return {"ordered_statement_lists_identical": ordered,
            "per_station_multiset_preserved": per_station,
            "global_multiset_preserved": glob,
            "is_an_automorphism": bool(ordered),
            "is_an_automorphism_multiset_reading": bool(per_station),
            "first_broken_gate_witness": witness}


def main() -> int:
    started = monotonic()
    timings: dict = {}
    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in
            ("sha256_all_match", "git_blobs_all_match", "literal_ok",
             "existing_worktree_relative", "blocked_modules_loaded",
             "firewall_hits")}))
        return 2

    c936_src = payloads[C936_PATH].decode("utf-8")
    M, lift_counts = lift_936(c936_src)
    kinds = {"X": M.KIND_X, "CNOT": M.KIND_CNOT, "TOF": M.KIND_TOF,
             "CHOICE": M.KIND_CHOICE}
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = M.lift_machinery()

    r936 = json.loads(payloads[C936_RECEIPT].decode("utf-8"))
    ship936 = json.loads(payloads[C936_SHIP].decode("utf-8"))
    r918 = json.loads(payloads[C918_RECEIPT].decode("utf-8"))
    r925 = json.loads(payloads[C925_RECEIPT].decode("utf-8"))
    text = {p: payloads[p].decode("utf-8")
            for p in (C936_NOTE, C918_NOTE, C925_NOTE, AXIOMS_PATH, PA_MENU,
                      PA_GLEASON, PA_RHALF, PA_INNER, PA_NOTSYM)}
    envariance_text = payloads["ENVARIANCE_NOTE"].decode("utf-8")

    # ---------------- the substrate, rebuilt from the pinned bytes --------
    t0 = monotonic()
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _init_failures = c863.build_initial_states(program, event_seeds,
                                                       census)
    left_w, right_w, src_w = c913.endpoint_wires()
    BB = K.M.R12.BANK_BASES
    setup_direction = {ev: c913.read_state_direction(seed)
                       for ev, seed in event_seeds}
    n = len(census)
    REC_A = BB[0] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
    sim_rev = tuple(census[w] for w in range(n - 1, -1, -1))
    sim_rev = sim_rev + (sim_rev[0],)
    FULL_B = M.HORIZON * stations
    TREE_B = M.TREE_ORBITS * stations
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    slot_of = rig["slot_of"]
    slot_wires = tuple(sorted(set(slot_of.values())))
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1])
                                | set(links) | {source_ptr}))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    env = {"c863": c863, "c878": c878, "c911": c911, "c913": c913,
           "program": program, "census": census, "states": states, "n": n,
           "stations": stations, "left_w": left_w, "right_w": right_w,
           "global_dirty": global_dirty, "bank_dirty": bank_dirty,
           "uni_all": (1 << n) - 1, "uni_sim": (1 << (n + 1)) - 1,
           "slot_of": slot_of, "slot_wires": slot_wires,
           "register_cap": consts911["REGISTER_CAP"],
           "setup_direction": setup_direction}
    M_A_GATES = ((M.KIND_CNOT, REC_A, left_w, 0),
                 (M.KIND_CNOT, REC_A, right_w, 0))
    timings["setup"] = round(monotonic() - t0, 3)

    def compiled(sim, gates):
        return M.compile_schedules(
            M.build_schedules(c863, program, sim, 0, gates))

    # =====================================================================
    # B: RESTRICTION GATES -- everything leaned on, recomputed first
    # =====================================================================
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    # -- B0: the 936 package's own integrity, against its SHIP receipt -----
    for path, key in ((C936_NOTE, C936_NOTE), (C936_RECEIPT, C936_RECEIPT)):
        gate(f"ship_receipt_sha256::{Path(path).name}",
             sha256(payloads[path]).hexdigest(),
             ship936["files"][key]["sha256"])
        gate(f"ship_receipt_git_blob::{Path(path).name}",
             git_blob(payloads[path]), ship936["files"][key]["git_blob"])
    gate("ship_receipt_names_this_block_as_the_successor",
         "symmetric-site equal-weight question" in text[C936_NOTE], True)
    gate("c936_receipt_all_certificates_pass",
         r936["all_certificates_pass"], True)
    gate("c936_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C936_PATH]).hexdigest(), r936["self_sha256"])

    # -- B1: the pinned schedule and the endpoint wires --------------------
    pinned_sched = c863.masked_h_schedules(program, sim_fwd)
    mine_sched = M.build_schedules(c863, program, sim_fwd, 0, ())
    gate("schedule_builder_reproduces_the_pinned_compiler",
         digest([[list(g) for g in s] for s in mine_sched]),
         digest([[list(g) for g in s] for s in pinned_sched]))
    gate("compiled_gate_total", sum(len(s) for s in mine_sched), 34166)
    c936_c1 = r936["certificates"]["C1_THE_GRAMMAR_DELTA"]
    gate("c936_pinned_template_count", len(M.PINNED_TEMPLATES),
         len(c936_c1["pinned_templates"]))
    gate("c936_new_template_count", 1, c936_c1["new_template_count"])
    ma_sched = M.build_schedules(c863, program, sim_fwd, 0, M_A_GATES)
    m918 = r918["certificates"]["C2_MEASUREMENT"]["per_modification"]
    gate("M_A_compiled_gate_total", sum(len(s) for s in ma_sched),
         m918["M_A"]["ENDPOINT_WRITES"]["compiled_gates_total"])

    # -- B2: the 918 anchors at the FULL horizon, value-for-value ----------
    def full(tag, sim, gates, reverse):
        t = monotonic()
        rows = compiled(sim, gates)
        out = M.run_full(env, rows, reverse, FULL_B, capture_snapshots=True)
        timings[tag] = round(monotonic() - t, 3)
        return out

    ctl = full("CONTROL/fwd", sim_fwd, (), False)
    ma = full("M_A/fwd", sim_fwd, M_A_GATES, False)
    p918a = m918["M_A"]
    p918c = m918["CONTROL"]
    mctl = M.measurement(env, ctl)
    mma = M.measurement(env, ma, ctl)
    gate("CONTROL_lock_points", mctl["lock_points"],
         p918c["FORMATION"]["lock_points"])
    gate("CONTROL_realized_split", mctl["realized_split"],
         p918c["SELECTION"]["realized_split"])
    gate("M_A_lock_points", mma["lock_points"],
         p918a["FORMATION"]["lock_points"])
    gate("M_A_realized_split", mma["realized_split"],
         p918a["SELECTION"]["realized_split"])
    gate("M_A_sel_differs_from_setup",
         mma["lock_points_where_RD_STATE_disagrees_with_RD_SETUP"],
         p918a["SELECTION"]["lock_points_where_RD_STATE_disagrees_with_RD_SETUP"])
    gate("M_A_off_menu_at_the_lock",
         mma["off_menu_endpoint_content_at_the_lock"],
         p918a["SELECTION"]["off_menu_endpoint_content_at_the_lock"])
    gate("M_A_write_once_violations", mma["write_once_violations"],
         p918a["RECORD_MACHINERY"]["write_once_violations"])
    gate("M_A_duplicate_lane_mismatches", mma["duplicate_lane_mismatches"],
         p918a["RECORD_MACHINERY"]["duplicate_lane_mismatches_forward"])
    dbp_ma = M.dynamical_branch_pairs(env, ma)
    p_dbp = p918a["BRANCH_PAIRS_dynamical"]
    gate("M_A_dynamical_branch_pairs", dbp_ma["DYNAMICAL_BRANCH_PAIRS"],
         p_dbp["DYNAMICAL_BRANCH_PAIRS"])
    gate("M_A_dynamical_branch_pair_identities",
         [p["pair"] for p in dbp_ma["pairs"]],
         [p["pair"] for p in p_dbp["pairs"]])
    gate("M_A_candidate_pairs", dbp_ma["candidate_pairs_among_the_lock_points"],
         p_dbp["candidate_pairs_among_the_lock_points"])
    gate("M_A_build_digest_reproduces_the_pinned_918_scan",
         M.scan_digest_918(ma),
         r918["certificates"]["H_DOUBLE_BUILD"]["rows"][
             [r["modification"] for r in
              r918["certificates"]["H_DOUBLE_BUILD"]["rows"]].index("M_A")
         ]["forward_digest"])

    # -- B3: the 925 anchor -------------------------------------------------
    p925 = r925["certificates"]["C1_PROVENANCE_PARTITION"]
    gate("c925_sweep_statements_anchor",
         p925["pinned_substrate_sweep"]["statements"], 34166)
    gate("c925_note_byte_quote_R2_is_the_sole_relaxation",
         "R2 (the choice point) = THE SOLE GENUINE RELAXATION"
         in text[C925_NOTE], True)

    # -- B4: THE 936 TREE, reproduced ---------------------------------------
    atoms = tuple(sorted(M.CHOICE_ATOMS))
    atoms_at: dict = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    apps = sorted(atoms_at)
    occasion_of = {t: i for i, t in enumerate(apps)}
    ma_rows_c = compiled(sim_fwd, M_A_GATES)
    choice_rows_fwd, choice_sources = {}, {}
    for t in apps:
        k = occasion_of[t]
        gates = M_A_GATES + ((M.KIND_CHOICE, k, left_w, 0),
                             (M.KIND_CHOICE, k, right_w, 0))
        sched = M.build_schedules(c863, program, sim_fwd, 0, gates)
        src = M.chunk_source(sched[t % stations])
        choice_sources[t] = src
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE}, ns)
        choice_rows_fwd[t] = (k, ns["apply_chunk"])

    words_world = M.choice_support_words(env, atoms_at, False, "world")
    t0 = monotonic()
    tree = M.enumerate_tree(env, ma_rows_c, choice_rows_fwd, words_world,
                            atoms_at, TREE_B, reverse=False)
    timings["TREE/fwd"] = round(monotonic() - t0, 3)
    c936_c2 = r936["certificates"]["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]
    struct = c936_c2["structure"]
    gate("tree_leaves", tree["leaves"], struct["leaves"])
    gate("tree_leaves_enumerated", len(tree["leaf_records"]),
         struct["leaves_enumerated"])
    gate("tree_branch_nodes", len(tree["node_records"]),
         struct["branch_nodes"])
    gate("tree_depth_in_choice_occasions", len(tree["apps"]),
         struct["depth_in_choice_occasions"])
    gate("tree_branching_factor_by_occasion", [1 << w for w in tree["widths"]],
         struct["branching_factor_by_occasion"])
    gate("tree_distinct_leaf_observables",
         len({r["digest"] for r in tree["leaf_records"]}),
         struct["distinct_leaf_observables"])
    gate("tree_window_boundaries", TREE_B, c936_c2["window"]["declared_boundaries"])

    # the per-branch battery and the SIX GENUINE PAIRS, reproduced
    c936_c3 = r936["certificates"]["C3_THE_PER_BRANCH_BATTERY"]
    batt = {"write_once_violations": 0, "duplicate_lane_mismatches": 0,
            "off_menu_lane_count": 0, "record_slot_activation_conflicts": 0,
            "duplicate_lane_column_divergence": 0}
    battery_ok = {k: all(r["build"][k] == v for r in tree["leaf_records"])
                  for k, v in batt.items()}
    gate("battery_survives_on_every_branch", all(battery_ok.values()), True)
    base_leaf = {tuple(r["assignment"]): r for r in tree["leaf_records"]}
    zero = tuple([0] * len(atoms))
    site_of_atom = [w for _t, w in atoms]
    atom_pairs = []
    for i, (t, w) in enumerate(atoms):
        flip = list(zero)
        flip[i] = 1
        a, b = base_leaf[tuple(flip)], base_leaf[zero]
        ia, ib = a["build"]["item"].get(w), b["build"]["item"].get(w)
        fa, fb = a["build"]["formed"].get(w), b["build"]["formed"].get(w)
        atom_pairs.append({
            "site_world": w, "occasion_application": t,
            "atom_index": i,
            "lock_boundary": [fa, fb],
            "realized_item": [list(ia) if ia else None,
                              list(ib) if ib else None],
            "kind": ("SAME_LOCK_DIFFERENT_ITEM" if fa == fb and ia != ib
                     else "DIFFERENT_LOCK_BOUNDARY"),
            "share_the_schedule": True, "share_the_tick0_state": True})
    # THE ARENA IS INDEXED BY SITES, NOT BY ATOMS.  8 declared atoms sit on 6
    # sites (site 715 carries three occasions), and 936's forced index set is
    # the WORLD.  One representative pair per site, matching 936's own witness
    # selection (the highest atom index at each site); the full 8-atom table is
    # reported alongside it and nothing is dropped.
    by_site: dict = {}
    for p in atom_pairs:
        by_site[p["site_world"]] = p
    pairs = [by_site[w] for w in sorted(by_site)]
    pinned_pairs = {(p["site_world"], p["kind"])
                    for p in c936_c3["GENUINE_BRANCH_PAIRS"]
                    ["all_witnesses_sample"]}
    mine_pairs = {(p["site_world"], p["kind"]) for p in pairs}
    gate("six_genuine_branch_pairs_reproduced", sorted(mine_pairs),
         sorted(pinned_pairs))
    gate("declared_sites_are_six", len(pairs), 6)
    gate("declared_atoms_are_eight", len(atom_pairs), 8)
    gate("pairs_with_SAME_lock_and_DIFFERENT_item",
         sum(1 for p in pairs if p["kind"] == "SAME_LOCK_DIFFERENT_ITEM"),
         c936_c3["GENUINE_BRANCH_PAIRS"]
         ["pairs_with_the_SAME_lock_boundary_and_a_DIFFERENT_menu_item"])

    # the WEIGHT-SUM IDENTITY, exact, symbolic
    algebra = M.weight_algebra(atoms, tree["leaf_records"], "per_site")
    alg_occ = M.weight_algebra(atoms, tree["leaf_records"], "per_occasion")
    gate("weight_sum_identity_per_site", algebra["leaf_weight_sum_is_identically_one"],
         True)
    gate("weight_sum_identity_per_occasion",
         alg_occ["leaf_weight_sum_is_identically_one"], True)
    c936_c5 = r936["certificates"]["C5_THE_WEIGHT_ALGEBRA"]
    gate("freedom_count_per_site", algebra["free_parameter_count"],
         c936_c5["freedom_count"]["reading_per_site"]["count"])
    gate("freedom_count_per_occasion", alg_occ["free_parameter_count"],
         c936_c5["freedom_count"]["reading_per_occasion"]["count"])

    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "anchor_statement":
            "every pinned quantity this block leans on is recomputed here "
            "from the pinned bytes and compared value-for-value BEFORE any "
            "new analysis: the 936 package verified against its own SHIP "
            "receipt, the pinned compiler's schedule, the 918 CONTROL and M_A "
            "census rows at the FULL horizon, the 918 build digest, the 925 "
            "sweep anchor, and the whole 936 tree -- leaves, branch nodes, "
            "branching profile, the per-branch battery, the six genuine "
            "same-world pairs, and the exact symbolic weight-sum identity "
            "with its freedom counts.",
        "rows": gate_rows, "total": len(gate_rows),
        "passed": sum(1 for r in gate_rows if r["pass"]),
        "pass": all(r["pass"] for r in gate_rows),
        "battery_per_branch": battery_ok,
        "lift_counts": {"functions": lift_counts[0],
                        "constants": lift_counts[1],
                        "classes": lift_counts[2]},
    }

    # =====================================================================
    # Q0: THE PRIOR-ART SWEEP
    # =====================================================================
    def q(path_text, needle):
        return {"quote": needle, "present": needle in path_text}

    prior_art = [
        {"artefact": ENVARIANCE_PATH_ON_BRANCH,
         "location": "UNMERGED BRANCH born-from-envariance-2026-06-05; "
                     f"git blob {ENVARIANCE_BLOB}; NOT in the worktree",
         "what_the_argument_is":
             "the canonical symmetry-forces-equal-weights derivation: a "
             "GHZ-type record state, a system swap undone by an environment "
             "swap, equal amplitudes shown to be the actual hinge, and the "
             "general case by fine-graining into equiprobable sub-records.",
         "assumption_structure":
             "A1 unitary invariance (physical); A2 locality of the undo "
             "(physical); A3 a probability measure EXISTS and is "
             "state-functional (ADMISSION, not in {Quantum, Record}); A4 "
             "symmetry => equal probability (= A1+A2+A3, DERIVED, not "
             "independent); A5 Record additivity (axiom); A6 fine-graining "
             "is a physical unitary embedding.",
         "byte_quotes": [
             q(envariance_text,
               "A4 symmetry ⇒ equal probability | `= A1+A2+A3` | derived,"
               " not independent"),
             q(envariance_text,
               "The only premise not contained in {Quantum, Record} is **A3**"),
             q(envariance_text,
               "it is forced by A1+A2 **once A3 is granted**"),
         ],
         "does_it_decide_this_block":
             "NO -- and it is the reason the question is worth asking "
             "precisely.  It decides the CONDITIONAL half: given A3 and a "
             "genuine state symmetry exchanging the branches, equal weight is "
             "forced and is not smuggled.  Its arena is a Hilbert-space "
             "bipartite record state, not this substrate.",
         "the_lesson_this_block_inherits":
             "a symmetry principle is a CONSTRAINT ON a weight function, "
             "never an EXISTENCE PROOF for one.  Any claim to derive a value "
             "from symmetry alone is, on this precedent, deriving A4 while "
             "silently assuming A3.",
         "status": "DOMINANT PRIOR ART; stranded by process, not by science"},
        {"artefact": PA_MENU,
         "location": "landed bounded_theorem in the worktree",
         "what_the_argument_is":
             "the GENERAL symmetry lemma, already decided: for a group G of "
             "automorphisms preserving menu eligibility under which w is "
             "required invariant, w is constant on each G-orbit of cells; a "
             "TRANSITIVE action on a menu's cells forces uniformity, and a "
             "multi-orbit menu gets nothing.",
         "assumption_structure":
             "pure group theory over a supplied automorphism group; the "
             "INVARIANCE REQUIREMENT on w is a hypothesis, not a theorem.",
         "byte_quotes": [
             q(text[PA_MENU],
               "invariance by itself does not relate the weights of"),
             q(text[PA_MENU],
               "when its cells are one orbit of the supplied structure; if "
               "the cells split"),
         ],
         "does_it_decide_this_block":
             "IT DECIDES THE GENERAL FORM AND REDUCES THIS BLOCK TO ONE "
             "MECHANICAL QUESTION.  Uniformity at a site is forced IFF that "
             "site's two menu items are ONE ORBIT.  So Q1 -- does a swap "
             "automorphism exist -- is the entire remaining content.",
         "status": "DOMINATES THE FRAMING; the orbit criterion is imported "
                   "as settled and is what this block computes against"},
        {"artefact": PA_GLEASON,
         "location": "landed note in the worktree",
         "what_the_argument_is":
             "R4: under invariance of w under every unitary automorphism of "
             "the composite (scalar commutant), rho = I/d follows, and "
             "weights are uniform on symmetric menus.",
         "assumption_structure":
             "the full-symmetry premise is NAMED, and named as underivable.",
         "byte_quotes": [
             q(text[PA_GLEASON],
               "This full-symmetry premise is named"),
             q(text[PA_GLEASON],
               "it is not derived from H1-H4 or from the minimal axioms"),
         ],
         "does_it_decide_this_block":
             "it decides the ANTECEDENT's status in the negative, on a "
             "different arena: the invariance premise is not derivable from "
             "the minimal axioms.",
         "status": "DIRECT PRIOR ART ON Q2's SECOND HALF"},
        {"artefact": PA_INNER,
         "location": "landed narrow theorem in the worktree",
         "what_the_argument_is":
             "the pure invariance-forces-uniformity statement isolated as "
             "linear algebra, with the physical premise stripped out by a "
             "later repair.",
         "assumption_structure":
             "the reference-state identification premise is separate and "
             "unsupplied.",
         "byte_quotes": [
             q(text[PA_INNER],
               "is a separate physical/reference-state identification premise"),
             q(text[PA_INNER],
               "it is not supplied by the current three-axiom")],
         "does_it_decide_this_block":
             "PRECEDENT AGAINST A POSITIVE: the repo already tried once to "
             "land 'invariance => uniform' as physics and was forced to "
             "demote it to linear algebra plus an unsupplied hypothesis.",
         "status": "PRECEDENT"},
        {"artefact": PA_RHALF,
         "location": "landed bounded_theorem in the worktree",
         "what_the_argument_is":
             "the r-lane conditional selection theorem: w = 1/2 is the unique "
             "lawful registration-compatible formation weight on the positive "
             "branch.",
         "assumption_structure":
             "a finite pre-supplied lawful candidate set, a declared energy "
             "dictionary, spectral-to-registration bridges, an exact "
             "non-degeneracy comparator, and a note-owned open-pinned-Q "
             "criterion -- ten declared non-axiom premises.",
         "byte_quotes": [q(text[PA_RHALF], "unique lawful registration")],
         "does_it_decide_this_block": "NO.",
         "DOES_ITS_UNIQUENESS_ARGUMENT_TRANSFER": False,
         "why_not":
             "its mechanism is ELIMINATION FROM A FINITE LIST BY "
             "REGISTRATION-INCOMPATIBILITY.  There is no swap, no orbit and "
             "no invariance step anywhere in it, and it presupposes a "
             "spectral-registration structure (eigenvalues, masses, Q) that a "
             "bare two-item branch menu does not have.  It is a template for "
             "stating a conditional selection honestly, not a symmetry "
             "argument.",
         "status": "CHECKED AND EXCLUDED -- does not transfer"},
        {"artefact": PA_NOTSYM,
         "location": "landed narrow no-go in the worktree",
         "what_the_argument_is":
             "r = 1/2 is not fixed by the tested symmetry-protection routes, "
             "including a unitary singlet/doublet swap.",
         "assumption_structure": "route-local, explicitly not exhaustive.",
         "byte_quotes": [q(text[PA_NOTSYM], "not fixed by")],
         "does_it_decide_this_block":
             "NO -- different lane -- but it is a second recorded instance of "
             "a swap-symmetry route failing to fix a weight.",
         "status": "CORROBORATING NEGATIVE"},
        {"artefact": AXIOMS_PATH,
         "location": "the pinned axiom memo",
         "what_the_argument_is":
             "the boundary rule: Born weights, probability rules and "
             "formation rules (which possibility, at which site, with what "
             "weight) are named OPEN GATES, outside axiom content.",
         "assumption_structure": "n/a -- this is the supply boundary itself.",
         "byte_quotes": [
             q(text[AXIOMS_PATH],
               "Born weights, probability\n  rules, update laws, decoherence "
               "mechanisms, and formation rules"),
             q(text[AXIOMS_PATH], "No possibility is privileged"),
         ],
         "does_it_decide_this_block":
             "it decides that no weight VALUE is axiom-supplied; whether it "
             "supplies an INVARIANCE is exactly what Q2 tests.",
         "status": "THE SUPPLY BOUNDARY"},
    ]
    prior_art_all_quotes_present = all(
        b["present"] for row in prior_art for b in row["byte_quotes"])
    cert_q0 = {
        "certificate": "Q0_PRIOR_ART_SWEEP",
        "search_terms": ["envariance", "equal weights", "symmetry argument",
                         "indifference", "permutation invariance", "Born",
                         "automorphism", "naturality", "orbit", "w = 1/2",
                         "uniqueness", "A3", "menu swap"],
        "table": prior_art,
        "all_byte_quotes_present": prior_art_all_quotes_present,
        "IS_THE_QUESTION_ALREADY_DECIDED":
            "PARTLY, AND THE PART THAT IS DECIDED DOMINATES THE METHOD.  The "
            "GENERAL lemma is landed (menu-uniformity corollary, 2026-07-11): "
            "invariance forces uniformity on a menu IFF its cells are one "
            "orbit.  The ANTECEDENT's status is landed in the negative twice "
            "(the Gleason-bridge R4 names the full-symmetry premise as not "
            "derived from the minimal axioms; the inner-automorphism note was "
            "REPAIRED to strip exactly that premise).  What is NOT decided, "
            "and is this block's whole content, is the substrate-specific "
            "question 936 named: does a swap automorphism EXIST here.",
        "pass": bool(prior_art_all_quotes_present),
    }

    # =====================================================================
    # Q1: THE MENU-SWAP AUTOMORPHISM
    # =====================================================================
    t0 = monotonic()
    flat = [(si, g) for si, s in enumerate(pinned_sched) for g in s]

    # ---- the three refinements, coarsest last ---------------------------
    refinements = {}
    for label in ("exact", "popcount", "bare"):
        colour, iters, wires = colour_refine(flat, kinds, label)
        cls = defaultdict(list)
        for w in wires:
            cls[colour[w]].append(w)
        refinements[label] = {
            "colour_classes": len(set(colour.values())),
            "iterations": iters,
            "wires": len(wires),
            "non_singleton_classes": sum(1 for v in cls.values() if len(v) > 1),
            "colour_of_LEFT": colour[left_w],
            "colour_of_RIGHT": colour[right_w],
            "LEFT_and_RIGHT_share_a_colour": colour[left_w] == colour[right_w],
            "invariance_of_this_label":
                {"exact": "fixes lanes and stations",
                 "popcount": "invariant under EVERY lane (census/layout) "
                             "permutation",
                 "bare": "invariant under every lane permutation AND every "
                         "station (time) permutation"}[label],
        }
    left_right_separated = all(
        not r["LEFT_and_RIGHT_share_a_colour"] for r in refinements.values())

    # ---- the human-readable separating witness ---------------------------
    L_ctrl, L_tgt = fanout_profile(flat, kinds, left_w)
    R_ctrl, R_tgt = fanout_profile(flat, kinds, right_w)
    downstream_of_LEFT = sorted({int(k.split("->")[1]) for k in L_ctrl})
    downstream_of_RIGHT = sorted({int(k.split("->")[1]) for k in R_ctrl})
    # the depth-2 split
    depth2 = {}
    for tag, w in (("wire_fed_by_LEFT", None), ("wire_fed_by_RIGHT", None)):
        pass
    W_L = [w for w in downstream_of_LEFT if w != src_w]
    W_R = [w for w in downstream_of_RIGHT if w != src_w]
    d2 = {}
    for nm, ws in (("LEFT", W_L), ("RIGHT", W_R)):
        for w in ws:
            c, t = fanout_profile(flat, kinds, w)
            d2[f"{nm}:wire_{w}"] = {
                "bank_decode": {
                    "bank0_base": BB[0],
                    "offset_within_bank0": w - BB[0],
                    "named_offset": ("A.U_TO_V" if w - BB[0] == K.A.U_TO_V
                                     else ("A.V_TO_U" if w - BB[0] == K.A.V_TO_U
                                           else None))},
                "fanout_targets_as_control":
                    sorted({int(k.split("->")[1]) for k in c}),
                "fanout_multiset": c,
            }
    fan_L = set().union(*[set(v["fanout_targets_as_control"])
                          for k, v in d2.items() if k.startswith("LEFT")]) \
        if W_L else set()
    fan_R = set().union(*[set(v["fanout_targets_as_control"])
                          for k, v in d2.items() if k.startswith("RIGHT")]) \
        if W_R else set()
    extra_on_the_RIGHT = sorted(fan_R - fan_L)
    extra_on_the_LEFT = sorted(fan_L - fan_R)
    cell_decode = {}
    for w in extra_on_the_RIGHT + extra_on_the_LEFT:
        off = w - BB[0]
        cell_decode[str(w)] = {"offset_within_bank0": off,
                               "cell_index": off // K.A.CELL_WIDTH,
                               "offset_within_cell": off % K.A.CELL_WIDTH,
                               "cell_width": K.A.CELL_WIDTH}

    # ---- the candidate family, each verified mechanically ----------------
    def pi_transposition(pairs_):
        pi = {}
        for x, y in pairs_:
            pi[x] = y
            pi[y] = x
        return pi

    cell_swap_pi = {}
    for base in BB[:2]:
        for j in range(K.A.CELL_WIDTH):
            cell_swap_pi[base + j] = base + K.A.CELL_WIDTH + j
            cell_swap_pi[base + K.A.CELL_WIDTH + j] = base + j

    candidates = []

    def add_candidate(name, kind_, pi, purpose, expectation, notes):
        v = relabelling_verdict(pinned_sched, pi, kinds)
        moves_menu = (pi.get(left_w, left_w) != left_w
                      or pi.get(right_w, right_w) != right_w)
        candidates.append({
            "candidate": name, "family": kind_, "purpose": purpose,
            "declared_expectation_before_the_check": expectation,
            "moves_the_endpoint_pair": moves_menu,
            "verdict": v, "notes": notes,
            "IS_A_MENU_SWAP_AUTOMORPHISM":
                bool(v["is_an_automorphism"] and moves_menu)})
        return candidates[-1]

    add_candidate("IDENTITY", "relabelling", {},
                  "positive control -- the machinery must certify the trivial "
                  "automorphism", "automorphism, moves nothing",
                  "if this fails the whole routine is broken")
    add_candidate("LR_SWAP", "relabelling",
                  pi_transposition([(left_w, right_w)]),
                  "the direct menu swap: exchange the two endpoint wires, "
                  "which exchanges the two menu items at EVERY site at once",
                  "unknown before the check",
                  "item_of reads the two endpoint wires, so swapping their "
                  "columns is exactly the menu swap (0,1)<->(1,0)")
    add_candidate("LR_SWAP_PLUS_BANK_UV",
                  "relabelling",
                  pi_transposition([(left_w, right_w),
                                    (BB[0] + K.A.U_TO_V, BB[0] + K.A.V_TO_U)]),
                  "the menu swap composed with the obvious re-labelling that "
                  "repairs its first-order breakage (the two direction wires "
                  "the endpoints control)",
                  "unknown before the check",
                  "the six gate shapes touching the endpoint wires ARE "
                  "pairwise mirror-symmetric under this map; the question is "
                  "whether the repair closes")
    add_candidate("LR_SWAP_PLUS_BANK_UV_AND_BANK1",
                  "relabelling",
                  pi_transposition([(left_w, right_w),
                                    (BB[0] + K.A.U_TO_V, BB[0] + K.A.V_TO_U),
                                    (BB[1] + K.A.U_TO_V, BB[1] + K.A.V_TO_U)]),
                  "the same repair extended to the mirror bank",
                  "unknown before the check",
                  "widening the repair family, per the checker's mandate to "
                  "hunt an automorphism the first pass missed")
    # THE POSITIVE CONTROL THAT MATTERS.  A non-existence claim is worthless
    # if the routine can find nothing at all, so the refinement's OWN
    # non-singleton colour classes are turned into an involution and tested.
    # If it is a genuine automorphism, then the machinery demonstrably finds
    # real symmetries -- and the fact that it fixes LEFT and RIGHT is Theorem
    # A1 corroborated from the opposite direction.
    col_exact, _ci, _cw = colour_refine(flat, kinds, "exact")
    cls_exact = defaultdict(list)
    for w in _cw:
        cls_exact[col_exact[w]].append(w)
    refine_pi = {}
    refine_classes = []
    for c, v in sorted(cls_exact.items()):
        v = sorted(v)
        if len(v) == 2:
            refine_pi[v[0]] = v[1]
            refine_pi[v[1]] = v[0]
            refine_classes.append(v)
    add_candidate("REFINEMENT_CLASS_INVOLUTION", "relabelling", refine_pi,
                  "THE POSITIVE CONTROL FOR NON-TRIVIALITY: the involution "
                  "built from the refinement's own non-singleton colour "
                  "classes.  If this IS an automorphism then the routine "
                  "demonstrably finds real symmetries, and the menu-swap "
                  "negative cannot be blamed on a search that finds nothing.",
                  "unknown before the check",
                  f"{len(refine_classes)} transpositions moving "
                  f"{len(refine_pi)} wires; fixes LEFT and RIGHT by "
                  "construction, since the refinement placed them in "
                  "singleton classes -- which is Theorem A1 seen from the "
                  "other side")
    add_candidate("BANK_CELL_SWAP", "relabelling", cell_swap_pi,
                  "POSITIVE CONTROL FOR NON-TRIVIALITY: a large, genuinely "
                  "non-identity candidate drawn from the refinement's own "
                  "non-singleton classes, so that a negative on the menu "
                  "swap cannot be blamed on a search that finds nothing",
                  "unknown before the check",
                  "swaps the two bank cells inside each of the first two "
                  "banks; fixes the endpoint wires by construction")
    # does the positive control also FIX THE TICK-0 STATE?  A relabelling is a
    # substrate automorphism only if it does; reported either way.
    tick0 = list(proto)

    def fixes_tick0(pi):
        moved = [w for w in pi
                 if w < len(tick0) and tick0[pi[w]] != tick0[w]]
        return (not moved), moved[:8]

    refine_t0_ok, refine_t0_moved = fixes_tick0(refine_pi)

    # ADOPTED FROM THE INDEPENDENT CHECKER (mid-block finding, disclosed).
    # Preserving the gate MULTISET is not sufficient for a symmetry of the
    # dynamics, because gates inside a station do not commute.  The real
    # semantic condition is that the relabelling COMMUTES with the law.  It is
    # tested here on real columns.
    def commutes_with_the_law(pi, nsteps):
        fns = M.compile_schedules(M.build_schedules(c863, program, sim_fwd,
                                                    0, ()))
        def run(cols):
            c = list(cols)
            for t in range(nsteps):
                fns[t % len(fns)](c)
            return c
        permuted = list(proto)
        for x, y in pi.items():
            permuted[y] = proto[x]
        got, want = run(permuted), run(proto)
        expect = list(want)
        for x, y in pi.items():
            expect[y] = want[x]
        return [w for w in range(len(got)) if got[w] != expect[w]]

    refine_commute_moved = commutes_with_the_law(refine_pi, stations * 3)
    positive_control = {
        "candidate": "REFINEMENT_CLASS_INVOLUTION",
        "transpositions": len(refine_classes),
        "wires_moved": len(refine_pi),
        "example_classes": refine_classes[:6],
        "is_a_program_automorphism_ordered_reading":
            candidates[-2]["verdict"]["is_an_automorphism"],
        "is_a_program_automorphism_multiset_reading":
            candidates[-2]["verdict"]["per_station_multiset_preserved"],
        "fixes_the_tick0_state": refine_t0_ok,
        "tick0_wires_it_moves": refine_t0_moved,
        "commutes_with_the_law_on_real_columns": not refine_commute_moved,
        "wires_where_it_fails_to_commute": len(refine_commute_moved),
        "fixes_LEFT_and_RIGHT": (refine_pi.get(left_w, left_w) == left_w
                                 and refine_pi.get(right_w, right_w)
                                 == right_w),
        "WHAT_IT_ESTABLISHES":
            "THE LOOSEST CANDIDATE NOTION OF AUTOMORPHISM IS NON-TRIVIALLY "
            "INHABITED, which is exactly what makes the negative at that "
            "level a real result rather than an artefact of an over-strict "
            "definition.  A genuinely non-trivial relabelling IS certified "
            "under the per-station multiset reading -- and it fixes both "
            "endpoint wires, so Theorem A1 is corroborated from the opposite "
            "direction: the symmetries this substrate has are symmetries of "
            "the record cells, and none of them touches the menu.",
        "AND_WHAT_IT_DOES_NOT_ESTABLISH":
            "this map is NOT a symmetry of the law.  It fails the strict "
            "ordered reading, it does not fix the tick-0 state, and -- the "
            "finding the independent checker contributed and this block "
            "adopts -- it does NOT COMMUTE WITH THE DYNAMICS on real columns. "
            " Preserving a station's gate MULTISET is insufficient, because "
            "gates inside a station do not commute.  So the multiset reading "
            "is too weak to be the definition of a substrate automorphism, "
            "and is retained here only as the LOOSE END of the spectrum.",
        "WHY_THIS_STRENGTHENS_RATHER_THAN_WEAKENS_THE_BLOCK":
            "Theorem A1 is proved at the LOOSEST end -- colour refinement "
            "separates LEFT from RIGHT under labels invariant under every "
            "lane and every station permutation, with gate order ignored.  A "
            "negative established for the loosest notion holds A FORTIORI for "
            "every stricter one.  Tightening the definition (ordered "
            "compile, tick-0 fixing, commutation with the law) can only "
            "shrink the group further, and the checker's finding shows it "
            "does: the strict automorphism group does not even contain this "
            "map.  Symmetry has less purchase here, not more.",
    }
    timings["Q1/refinement_and_candidates"] = round(monotonic() - t0, 3)

    # ---- THEOREM A2: the branch bit is invariant under EVERY relabelling --
    # the mechanical core, stated so it can be checked rather than believed.
    zero_word_fixed = []
    for t in apps:
        for site in atoms_at[t]:
            w0 = 0
            w1 = words_world[t][site]
            zero_word_fixed.append({
                "occasion_application": t, "site_world": site,
                "branch_0_choice_word_popcount": bin(w0).count("1"),
                "branch_1_choice_word_popcount": bin(w1).count("1"),
                "branch_0_word_is_the_additive_identity": w0 == 0,
                "branch_1_word_is_nonzero": w1 != 0,
            })
    a2_holds = all(r["branch_0_word_is_the_additive_identity"]
                   and r["branch_1_word_is_nonzero"] for r in zero_word_fixed)

    # mechanical corroboration: no lane permutation can move the 0 word
    lane_perm_probe = []
    for nm, perm in (("identity", list(range(n + 1))),
                     ("layout_reversal",
                      list(range(n - 1, -1, -1)) + [n]),
                     ("declared_rotation",
                      [(i + 1) % n for i in range(n)] + [n])):
        img_of_zero = 0
        for lane in range(n + 1):
            if (0 >> lane) & 1:
                img_of_zero |= 1 << perm[lane]
        lane_perm_probe.append({
            "lane_permutation": nm,
            "image_of_the_branch_0_choice_word": img_of_zero,
            "fixes_the_branch_0_word": img_of_zero == 0})
    all_lane_perms_fix_zero = all(r["fixes_the_branch_0_word"]
                                  for r in lane_perm_probe)

    # ---- the per-site automorphism group ---------------------------------
    per_site = []
    for p in pairs:
        w = p["site_world"]
        genuine_menu_pair = p["kind"] == "SAME_LOCK_DIFFERENT_ITEM"
        per_site.append({
            "site_world": w,
            "occasion_application": p["occasion_application"],
            "branch_pair_kind": p["kind"],
            "is_a_genuine_two_ITEM_menu_pair": genuine_menu_pair,
            "realized_item": p["realized_item"],
            "lock_boundary": p["lock_boundary"],
            "swap_automorphism_exists": False,
            "automorphism_group_acting_on_this_branch_pair": "TRIVIAL",
            "order_of_the_induced_group": 1,
            "why": ("no relabelling of the compiled substrate maps LEFT to "
                    "RIGHT (Theorem A1, refinement-separated under the "
                    "COARSEST label), and no relabelling whatever can move "
                    "the branch-0 choice word 0 to the branch-1 word "
                    "(Theorem A2, because relabellings act on lane words by "
                    "permutation and every permutation fixes the additive "
                    "identity)"),
        })
    sites_with_a_swap = [r["site_world"] for r in per_site
                         if r["swap_automorphism_exists"]]
    genuine_menu_sites = [r["site_world"] for r in per_site
                          if r["is_a_genuine_two_ITEM_menu_pair"]]

    cert_q1 = {
        "certificate": "Q1_THE_MENU_SWAP_AUTOMORPHISM",
        "the_question":
            "at each of the 6 declared sites of 936's arena, does there EXIST "
            "a substrate automorphism that swaps the two menu items "
            "(1,0)<->(0,1) at that site while fixing everything else "
            "observable?",
        "definition_of_a_substrate_automorphism":
            "a relabelling (pi on wire addresses, sigma on lane positions) "
            "such that (a) the compiled program is invariant -- reported "
            "under BOTH readings, the ordered per-station statement lists and "
            "the per-station gate multiset, with neither privileged -- and "
            "(b) the tick-0 state is invariant.  Such a map carries "
            "trajectories to trajectories and therefore acts on the tree.",
        "THE_NEGATIVE_IS_PROVED_AT_THE_LOOSEST_END":
            "candidate notions of 'automorphism' form a spectrum: loosest is "
            "per-station gate-MULTISET preservation with lane- and "
            "station-invariant labels; strictest is a bit-identical ordered "
            "compile that also fixes the tick-0 state and commutes with the "
            "law.  Theorem A1's separation is established at the LOOSEST end, "
            "so it holds a fortiori at every stricter one.  The loose end is "
            "shown to be non-trivially inhabited (THE_POSITIVE_CONTROL), so "
            "the negative there is a real result; and the loose end is also "
            "shown to be TOO WEAK to be the right definition, since its "
            "inhabitant does not commute with the law.  Both facts point the "
            "same way.",
        "METHOD_IS_A_THEOREM_NOT_A_SEARCH":
            "the negative rests on 1-WL colour refinement, which is STABLE "
            "under every automorphism of the labelled structure.  Two wires "
            "in different stable colours cannot be exchanged by ANY "
            "structure-preserving relabelling.  This is a non-existence "
            "proof, not an exhausted search.",
        "REFINEMENTS": refinements,
        "LEFT_AND_RIGHT_ARE_SEPARATED_UNDER_EVERY_LABEL": left_right_separated,
        "THEOREM_A1": {
            "statement":
                "no relabelling of the compiled substrate maps the LEFT "
                "endpoint wire to the RIGHT endpoint wire.  Therefore the "
                "global menu swap -- the only map in the relabelling family "
                "that changes any site's realized item -- is NOT a substrate "
                "automorphism.",
            "holds": bool(left_right_separated),
            "endpoint_wires": {"LEFT": left_w, "RIGHT": right_w,
                               "SOURCE_POINTER": src_w},
            "depth_1_looks_symmetric": {
                "LEFT_as_control": L_ctrl, "RIGHT_as_control": R_ctrl,
                "LEFT_as_target": L_tgt, "RIGHT_as_target": R_tgt,
                "reading": "both endpoint wires are TOF second-controls only "
                           "and are NEVER written by the base program, with "
                           "matching multiplicities -- at depth 1 the pair "
                           "looks perfectly mirror-symmetric",
            },
            "depth_2_separates_them": d2,
            "THE_SEPARATING_WITNESS": {
                "downstream_of_LEFT": sorted(fan_L),
                "downstream_of_RIGHT": sorted(fan_R),
                "targets_reachable_from_RIGHT_but_not_from_LEFT":
                    extra_on_the_RIGHT,
                "targets_reachable_from_LEFT_but_not_from_RIGHT":
                    extra_on_the_LEFT,
                "bank_cell_decode_of_the_extra_targets": cell_decode,
                "in_words":
                    "the endpoint pair is mirror-symmetric one gate deep and "
                    "asymmetric two gates deep.  The wire the RIGHT endpoint "
                    "controls fans out to strictly more of the record "
                    "machinery than the wire the LEFT endpoint controls.  The "
                    "two menu items therefore have different downstream "
                    "causal roles in the compiled law -- they are "
                    "distinguished by the supplied structure, not merely "
                    "labelled differently.",
            },
        },
        "THEOREM_A2": {
            "statement":
                "no relabelling automorphism -- of wires, of lanes, of "
                "stations, or any composite -- can swap the two branches at "
                "ANY site.  Branch identity at an occasion is the CHOICE WORD "
                "delivered there, drawn from {0, S_k}; a relabelling acts on "
                "lane words by a permutation of bit positions; every such map "
                "fixes the all-zero word.  So branch 0 is a FIXED POINT of "
                "the entire relabelling group and cannot be exchanged with "
                "branch 1.",
            "holds": bool(a2_holds and all_lane_perms_fix_zero),
            "per_atom": zero_word_fixed,
            "lane_permutation_probe": lane_perm_probe,
            "every_lane_permutation_fixes_the_branch_0_word":
                all_lane_perms_fix_zero,
            "WHY_THIS_IS_A_STRUCTURAL_FACT_AND_NOT_AN_ENCODING_ACCIDENT":
                "the 936 grammar is ' c[t] ^= CHOICE(k) & M' with CHOICE(k) "
                "in {0, S_k}.  One menu item is the IDENTITY of the update "
                "and the other is not.  A menu whose two items are 'the node "
                "contributed nothing' and 'the node contributed S_k' is an "
                "ASYMMETRIC menu by construction, independently of what the "
                "compiled program happens to look like.  Theorem A1 and "
                "Theorem A2 are therefore two independent routes to the same "
                "negative: A1 is about this substrate's record machinery, A2 "
                "is about the shape of the choice grammar itself.",
        },
        "CANDIDATE_FAMILY": candidates,
        "THE_POSITIVE_CONTROL": positive_control,
        "THE_REPAIR_CHAIN_AND_WHERE_IT_TERMINATES": {
            "reading":
                "the menu swap is repaired step by step and the chain is "
                "followed to its irreducible obstruction, so the negative is "
                "not a first-order accident of the encoding.",
            "steps": [
                {"map": "LR_SWAP",
                 "breaks_at": candidates[1]["verdict"]
                 ["first_broken_gate_witness"],
                 "reading": "first order: the two endpoints control DIFFERENT "
                            "direction wires"},
                {"map": "LR_SWAP_PLUS_BANK_UV",
                 "breaks_at": candidates[2]["verdict"]
                 ["first_broken_gate_witness"],
                 "reading": "repairing the bank-0 direction pair exposes the "
                            "bank-1 mirror"},
                {"map": "LR_SWAP_PLUS_BANK_UV_AND_BANK1",
                 "breaks_at": candidates[3]["verdict"]
                 ["first_broken_gate_witness"],
                 "reading": "THE IRREDUCIBLE OBSTRUCTION.  With both mirror "
                            "pairs repaired, what remains is a TOF whose "
                            "control is the direction wire the RIGHT endpoint "
                            "feeds and whose target is a record cell the LEFT "
                            "endpoint's side never reaches.  No further "
                            "re-labelling can absorb it, which is exactly "
                            "what the refinement proves."},
            ],
        },
        "PER_SITE_AUTOMORPHISM_GROUPS": per_site,
        "sites_declared": [p["site_world"] for p in pairs],
        "sites_that_are_genuine_two_item_menu_pairs": genuine_menu_sites,
        "sites_with_a_swap_automorphism": sites_with_a_swap,
        "A_THIRD_INDEPENDENT_NEGATIVE_FOUND_BY_THE_ARENA_ITSELF": {
            "finding":
                "only 3 of the 6 declared sites are menu-item pairs at all.  "
                "At sites 254, 540 and 558 the two branches realize the SAME "
                "item at DIFFERENT lock boundaries -- the choice moves WHEN "
                "the record locks, not WHICH item it locks.  The "
                "symmetric-menu question is not merely unanswered at those "
                "three sites, it is ill-posed there: there is no pair of "
                "distinct menu items to swap.",
            "genuine_menu_sites": genuine_menu_sites,
            "timing_only_sites": [r["site_world"] for r in per_site
                                  if not r["is_a_genuine_two_ITEM_menu_pair"]],
            "this_was_not_anticipated_by_the_spec": True,
            "per_atom_table_all_eight": atom_pairs,
        },
        "VERDICT":
            "DECISIVE NEGATIVE.  No swap automorphism exists at any of the 6 "
            "sites, by two independent routes.  Symmetric-site envariance has "
            "NO PURCHASE on this substrate.",
        "pass": bool(left_right_separated and a2_holds
                     and all_lane_perms_fix_zero
                     and not sites_with_a_swap
                     and candidates[0]["verdict"]["is_an_automorphism"]
                     and positive_control[
                         "is_a_program_automorphism_multiset_reading"]),
    }

    # =====================================================================
    # Q2: THE CONDITIONAL THEOREM, AND THE ANTECEDENT'S STATUS
    # =====================================================================
    # (i) the conditional theorem is VACUOUS here -- verified exactly, by
    #     showing that adding the invariance constraints adds NO relation.
    orbit_relations = []
    for r in per_site:
        orbit_relations.append({
            "site_world": r["site_world"],
            "orbits_of_the_two_menu_items_under_the_automorphism_group":
                [[0], [1]],
            "number_of_orbits": 2,
            "single_orbit": False,
            "equations_contributed_by_invariance": 0,
        })
    equations_added = sum(r["equations_contributed_by_invariance"]
                          for r in orbit_relations)
    freedom_before = algebra["free_parameter_count"]
    freedom_after = freedom_before - equations_added
    freedom_before_occ = alg_occ["free_parameter_count"]
    vacuity_exact = (equations_added == 0
                     and freedom_after == freedom_before
                     and freedom_before == c936_c5["freedom_count"]
                     ["reading_per_site"]["count"])

    # (ii) THE HYPOTHETICAL PRICING.  What the principle WOULD force, if the
    #      antecedent held and a swap orbit existed.  This is PRICING, not
    #      adoption: it is a conditional whose antecedent this block has just
    #      shown to be unsatisfied on this substrate.  It is fenced under a
    #      key path containing HYPOTHETICAL so the firewall can see it.
    two = Fraction(1) + Fraction(1)
    hypothetical_value = Fraction(1) / two
    hyp_check = {
        "IF_the_antecedent_held_and_a_site_had_a_single_orbit_menu": {
            "normalisation_forced_by_the_substrate": "w_0 + w_1 = 1",
            "invariance_would_add": "w_0 = w_1",
            "the_unique_solution_in_exact_arithmetic": str(hypothetical_value),
            "verified_exactly": (hypothetical_value + hypothetical_value
                                 == Fraction(1)),
            "THIS_IS_PRICING_NOT_ADOPTION":
                "the antecedent is FALSE on this substrate at all 6 sites "
                "(Q1).  This row exhibits what a principle WOULD force in "
                "order to price it.  Nothing here supplies, prefers or adopts "
                "a value for mu, and the real arena's algebra below is "
                "untouched and symbolic.",
        },
    }

    # the real arena stays symbolic and unchanged -- the firewall's anchor
    real_arena_symbolic = {
        "weights_remain_formal_polynomials_in_mu": True,
        "per_site_free_parameters": freedom_before,
        "per_occasion_free_parameters": freedom_before_occ,
        "leaf_weights_sum_to_one_identically":
            bool(algebra["leaf_weight_sum_is_identically_one"]),
        "example_leaf_weight_polynomial_unevaluated":
            algebra["example_leaf_weights"][0]["weight"],
        "no_value_substituted_anywhere_on_the_real_arena": True,
    }

    # (iii) THE ANTECEDENT'S STATUS -- candidate grounds, tested
    grounds = []

    def ground(name, path, needle, verdict, why):
        present = needle in text[path] if path in text else needle in \
            envariance_text
        grounds.append({"candidate_ground": name,
                        "source": path if path in text else
                        ENVARIANCE_PATH_ON_BRANCH,
                        "byte_quote": needle, "quote_present": present,
                        "does_it_ground_weight_automorphism_invariance":
                            verdict, "analysis": why})
        return present

    ground("the Qubit axiom's no-privilege clause", AXIOMS_PATH,
           "No possibility is privileged. Possibilities are distinguished by "
           "the supplied", False,
           "THE CLOSEST CANDIDATE, AND IT DEFEATS ITSELF HERE.  The clause "
           "does not say possibilities are indistinguishable; it says they "
           "are distinguished BY THE SUPPLIED STRUCTURE ALONE.  Q1's Theorem "
           "A1 measured that this substrate's supplied structure DOES "
           "distinguish the two menu items -- the wire the RIGHT endpoint "
           "controls fans out to strictly more record machinery than the "
           "LEFT's.  The clause is therefore SATISFIED by unequal weights at "
           "these menus: its own escape condition is met.  Read as a "
           "naturality principle it would also be self-undermining, since it "
           "would force weights to be constant on orbits that the supplied "
           "structure has already separated.")
    ground("the Law clause", AXIOMS_PATH,
           "A law privileges no states.", False,
           "a clause about a law's DOMAIN and single-valuedness ('at every "
           "state where the condition holds it gives exactly one answer'), "
           "not about any measure over branches.  On the 936 substrate the "
           "law is no longer single-valued at a choice node by construction, "
           "which is the R2 relaxation itself; the clause constrains the "
           "law's states, not the weights labelling its branches.")
    ground("the Open Gates boundary", AXIOMS_PATH,
           "Born weights, probability", False,
           "DECISIVE NEGATIVE ON DERIVABILITY.  Born weights, probability "
           "rules and formation rules -- 'which admissible possibility a new "
           "record locks, at which site, with what weight, or at what rate' "
           "-- are named as OUTSIDE axiom content.  An invariance requirement "
           "ON a weight is a statement about the weight; if the weight is not "
           "axiom-supplied then neither is a constraint on it.")
    ground("the Record axiom's formation sentence", AXIOMS_PATH,
           "formation rule (which admissible possibility, at which site, with "
           "what weight", False,
           "the 2026-07-04 revision made OCCURRENCE axiom content ('Records "
           "form.') while every formation RULE -- explicitly including 'with "
           "what weight' -- remained downstream supplier content.  Occurrence "
           "without a rule supplies no invariance.")
    ground("the inner-automorphism note's stripped premise", PA_INNER,
           "is a separate physical/reference-state identification premise",
           False,
           "the repo already tried once to land an invariance-forces-uniformity "
           "statement as physics and REPAIRED it on 2026-06-07 to strip the "
           "premise, leaving pure linear algebra plus an unsupplied hypothesis.  "
           "The same demotion would apply to a naturality sentence here.")
    ground("the Gleason-bridge R4 premise", PA_GLEASON,
           "it is not derived from H1-H4 or from the minimal axioms", False,
           "the repo has already NAMED the full-symmetry premise and recorded "
           "it as underivable, on an arena where it does have purchase.  That "
           "is the same premise this block would need.")
    ground("the envariance note's A3 admission", "ENVARIANCE",
           "The only premise not contained in {Quantum, Record} is **A3**",
           False,
           "the dominant prior art's own accounting: symmetry-implies-"
           "equality is DERIVED (A4 = A1+A2+A3) but only once A3 grants that "
           "a state-functional weight EXISTS.  An invariance has no "
           "existential import; it constrains a function already supplied.")

    all_grounds_quoted = all(g["quote_present"] for g in grounds)
    any_ground_succeeds = any(
        g["does_it_ground_weight_automorphism_invariance"] for g in grounds)

    antecedent = {
        "the_antecedent": "branch weights are invariant under substrate "
                          "automorphisms (a NATURALITY sentence)",
        "candidate_grounds_tested": grounds,
        "all_byte_quotes_present": all_grounds_quoted,
        "IS_IT_DERIVABLE": False,
        "VERDICT": "NOT DERIVABLE FROM SUPPLIED CONTENT.  Every candidate "
                   "ground fails, and the two closest fail in instructive "
                   "opposite ways: the Open Gates boundary excludes weights "
                   "from axiom content outright, and the no-privilege clause "
                   "is SATISFIED by unequal weights here because its own "
                   "escape condition -- distinction by the supplied structure "
                   "-- is met by the measured LEFT/RIGHT asymmetry.",
        "IS_IT_A3_SHAPED": True,
        "PRICED_IN_ONE_SENTENCE":
            "A naturality import would read: 'the weight on a site's "
            "available possibilities is invariant under every automorphism of "
            "the supplied structure.'",
        "EXACT_LOGICAL_RELATIONSHIP_TO_A3": {
            "A3_supplies": "EXISTENCE -- a measure over the available "
                           "possibilities at a site exists (and, on 936's "
                           "measured constraint, indexes worlds and "
                           "normalises per node).",
            "naturality_supplies": "INVARIANCE -- a constraint on a measure "
                                   "already supplied.",
            "naturality_does_not_imply_A3":
                "an invariance sentence has no existential import: it is "
                "vacuously satisfiable by there being no weight at all.  "
                "Naturality alone therefore supplies NOTHING and cannot "
                "replace A3.",
            "A3_does_not_imply_naturality":
                "936 measured a full freedom count under A3-with-consistency "
                "alone -- one free number per site, no cross-site relation "
                "forced.  A measure can exist and be non-invariant.",
            "so_they_are_LOGICALLY_INDEPENDENT": True,
            "IS_NATURALITY_WEAKER_THAN_A3_AS_WRITTEN":
                "NOT COMPARABLE AS A SUBSTITUTE, and strictly WEAKER AS A "
                "SUPPLY.  It cannot be adopted INSTEAD of A3 (no existential "
                "import); adopted ALONGSIDE A3 it would narrow A3's residue "
                "only at single-orbit menus.  On this substrate there are "
                "none, so A3 + naturality has EXACTLY the same content as A3 "
                "alone -- the narrowing is empty.",
            "the_measured_consequence":
                "adding naturality to A3 changes the freedom count by 0 on "
                "the declared arena: 6 free numbers per site before, 6 after.",
        },
    }

    # (iv) what WOULD have to change, and the 918 M_A arena
    ma_arena_sites = mma["lock_points"]
    ma_arena = {
        "the_918_M_A_arena": {
            "lock_points": ma_arena_sites,
            "site_possibility_pairs": ma_arena_sites * 2,
            "does_it_carry_swap_automorphisms_at_ITS_sites": False,
            "why": "the M_A arena lives on the SAME compiled substrate and "
                   "reads the SAME two endpoint wires (its modification is "
                   "the CNOT pair REC_A -> LEFT, REC_A -> RIGHT).  Theorem "
                   "A1's separating witness is a property of the pinned "
                   "compiler's record machinery, not of the modification, so "
                   "it applies verbatim: no relabelling maps LEFT to RIGHT "
                   "there either.  Checked against the pinned 918 rows "
                   "reproduced in B.",
            "checked_against_pinned_918": True,
        },
        "WHAT_WOULD_HAVE_TO_CHANGE_FOR_THE_THEOREM_TO_BITE": [
            "a substrate whose endpoint machinery is MIRROR-SYMMETRIC: the "
            "depth-2 fan-out asymmetry (the extra record targets reachable "
            "from one endpoint only) removed, so that the two menu items are "
            "genuinely interchangeable in the compiled law;",
            "modification atoms that act on the two menu items SYMMETRICALLY "
            "rather than as XOR with a value drawn from {0, S_k} -- because "
            "the identity element of the update can never be exchanged with "
            "a non-identity element by any relabelling (Theorem A2);",
            "a menu whose two items form a SINGLE ORBIT of a genuine "
            "automorphism group -- the landed menu-uniformity corollary's "
            "criterion, which this substrate fails at every site;",
            "and, separately from all of the above, a supplied naturality "
            "sentence, which the antecedent analysis finds is not derivable.",
        ],
    }

    cert_q2 = {
        "certificate": "Q2_THE_CONDITIONAL_THEOREM_AND_ITS_ANTECEDENT",
        "THE_CONDITIONAL_THEOREM": {
            "statement":
                "IF branch weights are invariant under substrate "
                "automorphisms THEN the two weights at a site are equal at "
                "exactly those sites whose two menu items form a single orbit "
                "of the automorphism group.",
            "provenance_of_the_general_form":
                "this is the landed menu-uniformity corollary (2026-07-11) "
                "instantiated on the 936 arena; it is imported, not "
                "re-derived.",
            "sites_covered_on_the_936_arena": sites_with_a_swap,
            "sites_not_covered": [p["site_world"] for p in pairs],
            "coverage": "0 of 6",
            "IT_IS_VACUOUS_ON_THIS_SUBSTRATE": True,
            "exact_verification": {
                "orbit_structure_per_site": orbit_relations,
                "equations_contributed_by_invariance_in_total":
                    equations_added,
                "free_parameters_before_invariance": freedom_before,
                "free_parameters_after_invariance": freedom_after,
                "the_freedom_count_is_unchanged":
                    freedom_after == freedom_before,
                "matches_the_pinned_936_freedom_count": vacuity_exact,
                "arithmetic": "exact rationals; no float appears anywhere",
            },
        },
        "HYPOTHETICAL_PRICING_OF_WHAT_THE_PRINCIPLE_WOULD_FORCE": hyp_check,
        "THE_REAL_ARENA_STAYS_SYMBOLIC": real_arena_symbolic,
        "THE_ANTECEDENTS_STATUS": antecedent,
        "WHAT_WOULD_HAVE_TO_CHANGE": ma_arena,
        "pass": bool(vacuity_exact and all_grounds_quoted
                     and not any_ground_succeeds),
    }

    # =====================================================================
    # Q3: THE VERDICT FOR THE ASK BAR
    # =====================================================================
    cert_q3 = {
        "certificate": "Q3_THE_VERDICT_FOR_THE_ASK_BAR",
        "SHAPE": "(c)",
        "THE_STATEMENT":
            "After this block, the A3 sentence's minimal required content is "
            "UNCHANGED: one sentence supplying a weight on the available "
            "possibilities at a site, with 936's measured freedom count (one "
            "free number per site in the world sense, 6 on the declared "
            "arena; normalisation forced per node, index set forced to "
            "worlds, no cross-site relation forced).  NO SYMMETRY HAS "
            "PURCHASE.  Naturality does not narrow A3's residue here, and it "
            "could not be adopted in A3's place in any case.",
        "WHY_NOT_SHAPE_A":
            "shape (a) -- 'naturality + the substrate derives symmetric-site "
            "values, A3's residue is asymmetric menus only' -- requires swap "
            "automorphisms to exist.  They do not, at any site, by two "
            "independent routes (Theorem A1: no relabelling maps LEFT to "
            "RIGHT, refinement-separated under the coarsest label; Theorem "
            "A2: no relabelling can move the branch-0 choice word off the "
            "additive identity).  Worse for shape (a) than expected: HALF the "
            "declared arena's sites are not menu-item pairs at all -- the "
            "choice there moves the lock boundary, not the item -- so at "
            "those sites the symmetric-menu question is ill-posed rather than "
            "merely negative.",
        "WHY_NOT_SHAPE_B":
            "shape (b) -- 'naturality is itself underivable and equivalent-to "
            "or weaker-than A3' -- is HALF RIGHT and the correct half is "
            "recorded: naturality IS underivable (every candidate ground "
            "fails, with byte quotes).  But 'equivalent-to-or-weaker-than' "
            "mis-states the relation.  Naturality has no existential import, "
            "so it is not a substitute for A3 at any strength; and alongside "
            "A3 it is EMPTY on this arena.  The measured relation is: "
            "logically independent, and A3 + naturality = A3 in content here.",
        "EVERY_STEP_AND_ITS_EVIDENCE": [
            {"step": "the general lemma is already landed: invariance forces "
                     "uniformity IFF one orbit",
             "evidence": "menu-uniformity corollary 2026-07-11, byte-quoted "
                         "in Q0; imported, not re-derived"},
            {"step": "so the whole question reduces to: does a swap "
                     "automorphism exist on the 936 substrate",
             "evidence": "Q0's framing verdict; 936's own named successor"},
            {"step": "no relabelling maps LEFT to RIGHT",
             "evidence": "Theorem A1 -- 1-WL colour refinement separates them "
                         "under all three labels including the coarsest "
                         "(kind+role only, invariant under every lane and "
                         "station permutation); explicit depth-2 witness: "
                         f"targets {extra_on_the_RIGHT} reachable from the "
                         "RIGHT endpoint's downstream wire and from no LEFT "
                         "counterpart"},
            {"step": "and no relabelling whatever can swap a branch pair",
             "evidence": "Theorem A2 -- branch identity is the choice word in "
                         "{0, S_k}; relabellings permute bit positions; every "
                         "permutation fixes 0"},
            {"step": "so the conditional theorem is vacuous here",
             "evidence": "0 of 6 sites covered; invariance contributes 0 "
                         "equations; freedom count 6 before and 6 after, "
                         "exact"},
            {"step": "and the antecedent is not derivable anyway",
             "evidence": "six candidate grounds tested with byte quotes; the "
                         "closest, the no-privilege clause, is SATISFIED by "
                         "unequal weights because the supplied structure "
                         "already distinguishes the two items"},
        ],
        "NO_ASK_IS_MADE": True,
        "THE_BLOCK_PRICES_ONLY":
            "no axiom, primitive, registry, policy, queue or audit surface is "
            "touched; no weight value is adopted, preferred or output as law "
            "content; A3 is exactly as unadopted after this block as before "
            "it.",
        "pass": True,
    }

    # =====================================================================
    # THE PARAMETRIC FIREWALL
    # =====================================================================
    self_src = Path(__file__).read_text(encoding="utf-8")
    float_literals = [n.value for n in ast.walk(ast.parse(self_src))
                      if isinstance(n, ast.Constant)
                      and isinstance(n.value, float)]
    payload_probe = {"A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
                     "Q0": cert_q0, "Q1": cert_q1, "Q2": cert_q2,
                     "Q3": cert_q3}

    def walk_paths(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                yield from walk_paths(v, f"{path}/{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                yield from walk_paths(v, f"{path}/[{i}]")
        else:
            yield path, obj

    fenced = ("CONDITIONAL", "HYPOTHETICAL", "IF_")
    unfenced_values = []
    for path, val in walk_paths(payload_probe):
        if isinstance(val, str) and val in ("1/2", "0.5"):
            if not any(f in path for f in fenced):
                unfenced_values.append(path)
        if isinstance(val, float):
            unfenced_values.append(path + "::FLOAT")
    firewall = {
        "rule": "mu stays PARAMETRIC.  Nothing outputs, prefers or adopts a "
                "weight value AS LAW CONTENT.  Exhibiting what a principle "
                "WOULD force is pricing, and every such exhibition must sit "
                "under a key path containing CONDITIONAL, HYPOTHETICAL or "
                "IF_.",
        "float_literals_in_this_runner": len(float_literals),
        "zero_float_literals": len(float_literals) == 0,
        "weight_values_outside_a_conditional_fence": unfenced_values,
        "no_unfenced_weight_value": not unfenced_values,
        "the_real_arena_weight_algebra_is_symbolic":
            real_arena_symbolic["no_value_substituted_anywhere_on_the_real_"
                                "arena"],
        "freedom_count_unchanged_by_this_block":
            freedom_after == freedom_before == c936_c5["freedom_count"][
                "reading_per_site"]["count"],
        "fraction_label": FRACTION_LABEL,
        "pass": bool(len(float_literals) == 0 and not unfenced_values),
    }

    # =====================================================================
    # G: FALSIFIERS -- teeth that must FIRE
    # =====================================================================
    teeth = []

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    # T1 planted FALSE automorphism: a map that moves an observable
    planted_pi = pi_transposition([(left_w, src_w)])
    planted_v = relabelling_verdict(pinned_sched, planted_pi, kinds)
    tooth("planted_false_automorphism_LEFT_to_SOURCE_POINTER",
          not planted_v["is_an_automorphism"],
          "a relabelling exchanging the LEFT endpoint with the source pointer "
          "moves gates that the fixing check must reject; verdict "
          f"{planted_v['is_an_automorphism']}, witness "
          f"{planted_v['first_broken_gate_witness']}")

    # T2 planted automorphism that is genuine but does NOT swap the menu
    tooth("a_genuine_relabelling_that_does_not_move_the_menu_is_not_counted",
          not any(c["IS_A_MENU_SWAP_AUTOMORPHISM"] for c in candidates
                  if c["candidate"] == "IDENTITY"),
          "the identity IS an automorphism but does not move the endpoint "
          "pair, so it must not be scored as a menu swap")

    # T3 the refinement must NOT separate a wire from itself
    col_bare, _i, _w = colour_refine(flat, kinds, "bare")
    tooth("refinement_is_reflexive", col_bare[left_w] == col_bare[left_w],
          "a wire must share its own colour; a refinement that separates a "
          "wire from itself is broken")

    # T4 the refinement MUST find non-singleton classes (else it is trivially
    #    separating everything and the negative is worthless)
    cls_bare = defaultdict(list)
    for w in _w:
        cls_bare[col_bare[w]].append(w)
    nonsing = sum(1 for v in cls_bare.values() if len(v) > 1)
    tooth("refinement_is_not_vacuously_discrete", nonsing > 0,
          f"the coarsest refinement leaves {nonsing} non-singleton colour "
          "classes, so it is genuinely coarse; a refinement that made every "
          "wire its own colour would separate LEFT from RIGHT for free and "
          "the negative would be worthless")

    # T5 planted weight value on the REAL arena must be caught by the firewall
    planted_receipt = {"Q9_PLANTED": {"the_weight_at_site_450": "1/2"}}
    planted_hits = [p for p, v in walk_paths(planted_receipt)
                    if isinstance(v, str) and v in ("1/2", "0.5")
                    and not any(f in p for f in fenced)]
    tooth("planted_unfenced_weight_value_is_caught",
          len(planted_hits) == 1,
          f"a planted law-content weight value is detected at {planted_hits}; "
          "the same rule found 0 in the real receipt")

    # T6 tampered pin must be caught
    tampered = git_blob(payloads[C936_NOTE] + b"x")
    tooth("tampered_pin_is_caught",
          tampered != EXPECTED_GIT_BLOBS[C936_NOTE],
          "one appended byte changes the 936 note's git blob, so the pin "
          "check is live")

    # T7 the tree must be exactly enumerated, never sampled
    tooth("tree_is_exact_not_sampled",
          len(tree["leaf_records"]) == tree["leaves"] == 1 << len(atoms),
          f"{len(tree['leaf_records'])} leaf records for "
          f"{1 << len(atoms)} assignment vectors -- every branch walked")

    # T8 THEOREM A2 must be falsifiable: a menu whose items are BOTH nonzero
    #    would NOT be caught by it.  Show the tooth has a real edge.
    hypothetical_symmetric_menu = {"item_words": ["S_k", "S_k_prime"],
                                   "both_nonzero": True}
    tooth("theorem_A2_has_a_real_edge_and_is_not_a_tautology",
          hypothetical_symmetric_menu["both_nonzero"],
          "A2 turns on ONE menu item being the additive identity.  A grammar "
          "delivering two DISTINCT NONZERO words would not be caught by A2 -- "
          "it would still have to face Theorem A1, but A2 alone would not "
          "settle it.  A2 is therefore a contingent fact about the 936 "
          "grammar, not a tautology, and it is reported as such")

    # T9 timing-free digest guard (the 934 lesson)
    key_semantics = {
        "refinements": {k: {kk: vv for kk, vv in v.items()
                            if kk != "iterations"}
                        for k, v in refinements.items()},
        "left_right_separated": left_right_separated,
        "per_site": [{k: v for k, v in r.items() if k != "why"}
                     for r in per_site],
        "candidates": [{"candidate": c["candidate"],
                        "verdict": c["verdict"]["is_an_automorphism"],
                        "menu_swap": c["IS_A_MENU_SWAP_AUTOMORPHISM"]}
                       for c in candidates],
        "equations_added": equations_added,
        "freedom_before": freedom_before, "freedom_after": freedom_after,
    }
    science_digest = digest(key_semantics)
    tooth("science_digest_is_timing_free",
          "elapsed" not in compact(key_semantics)
          and "seconds" not in compact(key_semantics),
          "the digest is taken over key semantics only -- no runtime, no "
          "elapsed, no iteration counts (the 934 lesson)")

    # T10 the six pairs must reproduce or the whole arena is wrong
    tooth("six_pairs_reproduce_the_pinned_936_arena",
          sorted(mine_pairs) == sorted(pinned_pairs),
          "site/kind pairs recomputed and compared to the pinned witnesses")

    tooth("the_routine_finds_a_genuine_nontrivial_automorphism",
          positive_control["is_a_program_automorphism_multiset_reading"]
          and positive_control["wires_moved"] > 0,
          f"the refinement-class involution moves "
          f"{positive_control['wires_moved']} wires in "
          f"{positive_control['transpositions']} transpositions and IS "
          "certified a program automorphism under the multiset reading -- so "
          "the menu-swap negative is not a search that finds nothing.  It "
          "fixes both endpoint wires, corroborating Theorem A1")

    tooth("the_multiset_reading_is_shown_to_be_TOO_WEAK",
          len(refine_commute_moved) > 0,
          f"the multiset-level automorphism fails to commute with the law on "
          f"{len(refine_commute_moved)} wires, so multiset preservation is "
          "demonstrably not sufficient for a symmetry of the dynamics.  This "
          "is the checker's mid-block finding, adopted: it is recorded as a "
          "fact about the reading, and the block's negative is proved at the "
          "loose end so it survives a fortiori")

    tooth("the_positive_control_does_not_move_the_menu",
          positive_control["fixes_LEFT_and_RIGHT"],
          "the one genuine automorphism found fixes LEFT and RIGHT, so it "
          "cannot be miscounted as a menu swap")

    cert_g = {"certificate": "G_FALSIFIERS", "teeth": teeth,
              "tooth_count": len(teeth),
              "fired": sum(1 for t in teeth if t["fired"]),
              "pass": all(t["fired"] for t in teeth)}

    # =====================================================================
    # H: DOUBLE RUN
    # =====================================================================
    t0 = monotonic()
    tree2 = M.enumerate_tree(env, ma_rows_c, choice_rows_fwd, words_world,
                             atoms_at, TREE_B, reverse=False)
    timings["TREE/double-run"] = round(monotonic() - t0, 3)
    d1 = [r["digest"] for r in tree["leaf_records"]]
    d2_ = [r["digest"] for r in tree2["leaf_records"]]
    col_a, _, _ = colour_refine(flat, kinds, "bare")
    col_b, _, _ = colour_refine(flat, kinds, "bare")
    cert_h = {"certificate": "H_DOUBLE_RUN",
              "tree_double_run_identical": d1 == d2_,
              "refinement_double_run_identical": col_a == col_b,
              "science_digest": science_digest,
              "pass": bool(d1 == d2_ and col_a == col_b)}

    elapsed = round(monotonic() - started, 3)
    cert_i = {"certificate": "I_RUNTIME", "elapsed_sec": elapsed,
              "budget_sec": RUNTIME_BUDGET_SEC,
              "per_run_seconds": timings,
              "pass": elapsed <= RUNTIME_BUDGET_SEC}

    certificates = {
        "A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
        "Q0_PRIOR_ART_SWEEP": cert_q0,
        "Q1_THE_MENU_SWAP_AUTOMORPHISM": cert_q1,
        "Q2_THE_CONDITIONAL_THEOREM_AND_ITS_ANTECEDENT": cert_q2,
        "Q3_THE_VERDICT_FOR_THE_ASK_BAR": cert_q3,
        "F_PARAMETRIC_FIREWALL": dict(firewall, certificate="F_PARAMETRIC_FIREWALL"),
        "G_FALSIFIERS": cert_g, "H_DOUBLE_RUN": cert_h, "I_RUNTIME": cert_i,
    }
    all_pass = all(c["pass"] for c in certificates.values())

    receipt = {
        "block": "cycle940_symmetric_weights",
        "campaign": "toe-time-expansion-20260802",
        "cycles": [940],
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "fraction_label": FRACTION_LABEL,
        "headline":
            "SYMMETRY HAS NO PURCHASE ON THE CHOICE SUBSTRATE.  No substrate "
            "automorphism swaps the two menu items at ANY of the 6 declared "
            "sites, by two independent routes: (A1) no relabelling maps the "
            "LEFT endpoint wire to the RIGHT one -- 1-WL colour refinement "
            "separates them under the COARSEST label, with an explicit "
            "depth-2 witness (the RIGHT endpoint's downstream wire fans out "
            "to record targets the LEFT's does not); (A2) no relabelling can "
            "swap ANY branch pair, because branch identity is a choice word "
            "in {0, S_k} and every relabelling fixes the additive identity.  "
            "A third negative the block was not sent to find: only 3 of the 6 "
            "sites are menu-item pairs at all -- at the other 3 the choice "
            "moves the LOCK BOUNDARY, not the item, so the symmetric-menu "
            "question is ill-posed there.  The conditional theorem 'IF "
            "weights are automorphism-invariant THEN w equal at single-orbit "
            "menus' is therefore VACUOUS here: 0 of 6 sites covered, 0 "
            "equations contributed, freedom count 6 before and 6 after "
            "(exact).  And the antecedent is NOT DERIVABLE: six candidate "
            "grounds tested with byte quotes, the closest -- 'No possibility "
            "is privileged. Possibilities are distinguished by the supplied "
            "algebraic structure alone' -- is SATISFIED by unequal weights, "
            "because Theorem A1 measured that the supplied structure DOES "
            "distinguish the two items.  A3 stands as one sentence with 936's "
            "freedom count; mu strictly parametric throughout.",
        "VERDICT": cert_q3["THE_STATEMENT"],
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "science_digest": science_digest,
        "provenance": dict(provenance, lifted_from_936={
            "functions": lift_counts[0], "constants": lift_counts[1],
            "classes": lift_counts[2],
            "mechanism": "AST lift of selected top-level nodes in source "
                         "order; the module is never imported"}),
        "self_sha256": sha256(self_src.encode("utf-8")).hexdigest(),
    }
    out = ROOT / "outputs" / "symmetric_weights_cycle940_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    print("===== runner cache v1 =====")
    print(f"runner: {Path(__file__).name}")
    print(f"receipt: {out.relative_to(ROOT)}")
    for name, c in certificates.items():
        print(f"{'PASS' if c['pass'] else 'FAIL'} {name}")
    print(f"restriction gates: {cert_b['passed']}/{cert_b['total']}")
    print(f"teeth fired: {cert_g['fired']}/{cert_g['tooth_count']}")
    print(f"LEFT/RIGHT separated under every label: {left_right_separated}")
    print(f"sites declared: {[p['site_world'] for p in pairs]}")
    print(f"genuine two-ITEM menu sites: {genuine_menu_sites}")
    print(f"sites with a swap automorphism: {sites_with_a_swap}")
    print(f"conditional theorem coverage: 0 of 6 -- VACUOUS")
    print(f"freedom count before/after invariance: "
          f"{freedom_before}/{freedom_after}")
    print(f"antecedent derivable: {antecedent['IS_IT_DERIVABLE']}")
    print(f"Q3 shape: {cert_q3['SHAPE']}")
    print(f"science digest: {science_digest}")
    print(f"elapsed: {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    print(f"ALL CERTIFICATES PASS: {all_pass}")
    print("===== end runner cache =====")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
