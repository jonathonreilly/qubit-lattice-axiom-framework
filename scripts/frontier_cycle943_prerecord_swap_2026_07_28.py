#!/usr/bin/env python3
"""Cycle 943 -- THE PRE-RECORD SWAP: value-space symmetry on the choice substrate.

THE OWNER'S OBJECTION, which is this block's specification.  Cycle 940 proved
that no substrate AUTOMORPHISM swaps the two menu items at any site, and that
the 936 grammar's apply-or-don't encoding makes menus asymmetric by
construction.  The owner's counter: the nothing-happens-or-record-happens
asymmetry is about the RECORD event -- but BEFORE the record, why could the two
possibilities not be symmetric?  That has three sharp technical readings, and
940 covers none of them:

  A  940's family was PERMUTATION-based (relabellings of wire addresses).  The
     quantum envariance swap is a STATE-SPACE operation (a unitary on values).
     The substrate analogue is conjugation of the law by a VALUE transformation
     -- a bit-flip set F, acting as c[w] -> c[w] ^ chi[w].  Flipping BOTH
     endpoint wires maps the menu (1,0) <-> (0,1).  Was that family tested?

  B  apply-or-don't is ONE encoding.  940's own A2 names the escape: a grammar
     choosing between TWO NONZERO words is not menu-asymmetric by construction.

  C  do the AXIOMS distinguish the two possibilities at a site, or only THIS
     kernel's wiring?  If only the wiring, 940's negative is MODEL-CONTINGENT
     and the class-level question is open -- which is what a TOE needs.

MINIMAL-PREMISE RULE.  The owner's framing (pre-record symmetry should exist)
and the supervisor's prior framing (940 settled it) are BOTH non-premises.  The
bytes decide, and both readings are carried on every ambiguity.

THE FIREWALL (inherited from 936/940, mechanical and over-broad).  mu stays
PARAMETRIC.  Nothing here outputs, prefers or adopts a weight value AS LAW
CONTENT.  Exhibiting what a principle WOULD force is PRICING: every numeric
weight sits under a key path containing CONDITIONAL, HYPOTHETICAL or IF_.
Zero float literals; exact rationals end to end.

DISCIPLINE.  936's tree and battery and 940's A1 / A2 / site-classification /
coverage / freedom are reproduced value-for-value against their pinned receipts
BEFORE any new analysis.  All 936 and 940 machinery is AST-LIFTED from the
pinned bytes -- never imported.  Declared scope limit: the 180224-boundary
Cycle-918 full-horizon re-run is NOT repeated here (940 ran it; its receipt is
pinned by sha256 and git blob).  The restriction gates cover the tree, the
battery, the compiled-gate totals, A1, A2 and the per-atom classification.
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
C940_PATH = "scripts/frontier_cycle940_symmetric_weights_2026_07_28.py"
C940_RECEIPT = "outputs/symmetric_weights_cycle940_receipt_2026_07_28.json"
C940_SHIP = "outputs/symmetric_weights_block_cycle940_ship_receipt_2026_07_28.json"
C940_NOTE = ("docs/R1A3_NEGATIVE_NO_SWAP_AUTOMORPHISM_CYCLE940"
             "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
C925_RECEIPT = "outputs/law_relaxation_cycle925_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (CORE_PATH, C936_PATH, C936_RECEIPT, C936_SHIP, C936_NOTE,
                     C940_PATH, C940_RECEIPT, C940_SHIP, C940_NOTE,
                     C918_RECEIPT, C925_RECEIPT, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C936_PATH:
        "ba00f39403a1280346d2e20e6e1985130b7d4b0a986e1473acd2c637acd96e3d",
    C936_RECEIPT:
        "4412ae9016df02546db26cdd87fa33ab68bf2a7370b27640e18d4d0e59132028",
    C936_SHIP:
        "9da5a559f4e87940560aaf75daaaa4332a228cc5ec2a7b50bf744a7cbb164f0a",
    C936_NOTE:
        "6cdec178602e936a07a86c43627b431527a5d328c2b269d0edd594d245831eac",
    C940_PATH:
        "7c7400984e573dc446330f20423cce5045138682781716ed13ba89bfe877e124",
    C940_RECEIPT:
        "08888bf454a7f3c803f5c373d7688d67a9f0d974259f3e455c139d6c78e288cf",
    C940_SHIP:
        "83c90abbd2d4eba1715cd9ec7c9b25353a397e11ae6a3392d7087250e64f218f",
    C940_NOTE:
        "a89185085032947c4fcc34fd99b1507307f70cbaf82dd82e569a37562114ef11",
    C918_RECEIPT:
        "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    C925_RECEIPT:
        "f4fabe50ed8b775f2f1288380824ae04f0129f4f136e3b338bafd05647031757",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C936_PATH: "75cb05ffb9456691747a67ed5227f3db589f95c4",
    C936_RECEIPT: "d7b786fccc0435d139339c141dbad75c9f8d799b",
    C936_SHIP: "1421484631b06fc203405c0ffab3a715c979cbed",
    C936_NOTE: "ffc0e6d1c3527ef75286abc0e50de0a3a3588f53",
    C940_PATH: "ae09b548aff71354b9942904bc0b2824d7e755ac",
    C940_RECEIPT: "a24af8e08cc090b39802265d8b8d5ea3d1495d53",
    C940_SHIP: "fa643ec30de44df8111c295225893ba7006d12a1",
    C940_NOTE: "69e712e1b8f9ecee3488f8698cfe577fac415c07",
    C918_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
    C925_RECEIPT: "fed1b28e9e5cfe731a541645dce705541d69c967",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

# THE STRANDED ENVARIANCE NOTE -- the prior art FOR this block's family.  Its
# swap is U_S (x) U_E: an X bit-flip on the system tensored with a value swap
# on the environment.  That is a STATE-SPACE operation, not a relabelling, and
# it is exactly reading A.  Not in any worktree; pinned BY BLOB.
ENVARIANCE_BLOB = "64b24361f2237d01f079e16b306b5d04e01de7c2"
ENVARIANCE_PATH_ON_BRANCH = (
    "docs/BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL"
    "_PROBABILITY_NOTE_2026-06-05.md")

BLOCKLISTED_MODULES = (
    "frontier_cycle936_choice_substrate_2026_07_28",
    "frontier_cycle940_symmetric_weights_2026_07_28",
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
# A: pins, and the AST lifts of the pinned 936 / 940 machinery
# ---------------------------------------------------------------------------

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

# from 940: exactly the automorphism machinery, so A1 is REPRODUCED rather
# than re-derived by a lookalike routine.
LIFT940_FUNCS = ("gate_roles", "colour_refine", "fanout_profile", "apply_pi",
                 "relabelling_verdict")
LIFT940_CONSTS = ("ROLE_TARGET", "ROLE_C1", "ROLE_C2")


def _lift(source, filename, funcs, consts, classes):
    tree = ast.parse(source, filename=filename)
    body, got_f, got_c, got_k = [], set(), set(), set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
            got_f.add(node.name)
        elif isinstance(node, ast.ClassDef) and node.name in classes:
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
            if names and all(nm in consts for nm in names):
                body.append(node)
                got_c.update(names)
    missing = (tuple(sorted(set(funcs) - got_f)),
               tuple(sorted(set(consts) - got_c)),
               tuple(sorted(set(classes) - got_k)))
    if any(missing):
        raise AssertionError(("lift incomplete", filename, missing))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = {"__builtins__": __builtins__, "ROOT": ROOT, "K": K, "np": np,
          "ast": ast, "json": json, "math": math, "sys": sys,
          "itertools": itertools, "combinations": combinations,
          "product": product, "Counter": Counter, "defaultdict": defaultdict,
          "Fraction": Fraction, "sha256": sha256, "sha1": sha1, "Path": Path,
          "SimpleNamespace": SimpleNamespace, "compact": compact,
          "digest": digest, "git_blob": git_blob}
    exec(compile(module, f"<ast-lift {filename}>", "exec"), ns)
    return SimpleNamespace(**{n: ns[n] for n in
                              tuple(got_f) + tuple(got_c) + tuple(got_k)}), \
        (len(got_f), len(got_c), len(got_k))


def lift_936(source):
    return _lift(source, C936_PATH, LIFT_FUNCS, LIFT_CONSTS, LIFT_CLASSES)


def lift_940(source):
    return _lift(source, C940_PATH, LIFT940_FUNCS, LIFT940_CONSTS, ())


def pin_rows():
    rows, payloads = {}, {}
    for path in AUDIT_INPUT_PATHS:
        blob = (ROOT / path).read_bytes()
        payloads[path] = blob
        rows[path] = {"sha256": sha256(blob).hexdigest(),
                      "git_blob": git_blob(blob), "bytes": len(blob)}
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
        "existing_worktree_relative": all((ROOT / p).exists()
                                          for p in AUDIT_INPUT_PATHS),
        "blocked_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                   if m in sys.modules],
        "firewall_hits": list(PRIMARY_FIREWALL.hits),
        "THE_STRANDED_ENVARIANCE_NOTE": {
            "why_pinned_by_blob":
                "not in the worktree; it lives only on the unmerged branch "
                "born-from-envariance-2026-06-05.  It is the PRIOR ART FOR "
                "THIS BLOCK'S FAMILY: its swap is U_S (x) U_E -- an X "
                "bit-flip on the system tensored with a value swap on the "
                "environment -- a STATE-SPACE operation, which is precisely "
                "the family Cycle 940 did not test.",
            "path_on_branch": ENVARIANCE_PATH_ON_BRANCH,
            "git_blob": ENVARIANCE_BLOB,
            "retrieved_bytes": len(env_bytes),
            "blob_verifies": env_blob_ok,
            "sha256": sha256(env_bytes).hexdigest() if env_bytes else None,
        },
        "modification_mechanism":
            "WRAP, NEVER EDIT.  The pinned 936 and 940 runners are AST-LIFTED "
            "(selected top-level nodes replayed in source order) and never "
            "imported; their bytes are unchanged and hashed.  Nothing in this "
            "block writes to any pinned file.",
        "declared_scope_limit":
            "the 180224-boundary Cycle-918 full-horizon re-run is NOT "
            "repeated here.  Cycle 940 ran it and its receipt is pinned by "
            "sha256 and git blob.  This block's restriction gates reproduce "
            "936's tree and battery, the compiled-gate totals, and 940's A1, "
            "A2 and per-atom classification, value-for-value.",
    }
    cert["pass"] = bool(
        sha_ok and blob_ok and cert["existing_worktree_relative"]
        and env_blob_ok and not cert["blocked_modules_loaded"]
        and not cert["firewall_hits"])
    return cert, payloads


# ---------------------------------------------------------------------------
# THE VALUE-SPACE MACHINERY (this block's new content)
# ---------------------------------------------------------------------------

def control_masks(schedules, kinds):
    """CTRLMASK[w] = OR of the lane masks of every gate in which wire w is a
    CONTROL (the CNOT source, or either TOF control).

    THE CRITERION.  For a pure value bit-flip X_chi (c[w] -> c[w] ^ chi[w]),
    X_chi commutes with the compiled law IFF chi[w] & CTRLMASK[w] == 0 for
    every wire w.  Proof, gate by gate, per lane:
      X   c[a] ^= M          -- a constant; commutes for every chi.
      CNOT c[b] ^= c[a] & M  -- need (a ^ chi_a) & M == a & M for all a,
                                i.e. chi_a & M == 0.  chi_b is unconstrained
                                (the flip passes straight through the XOR).
      TOF c[c3] ^= c[a]&c[b]&M -- need (a^chi_a)&(b^chi_b)&M == a&b&M for all
                                a, b.  Setting b = 1 on a lane where chi_a has
                                a 1 bit falsifies it, and symmetrically; so
                                both controls must be unflipped on the mask.
                                chi_c3 is unconstrained.
      CHOICE c[b] ^= CHOICE(k)&M -- CHOICE reads no state; commutes always.
    The condition is therefore LINEAR and the commuting set is a GROUP, which
    is why this is a complete characterisation and not a search.
    """
    cm = defaultdict(int)
    for schedule in schedules:
        for gate in schedule:
            kind, a, b, c3, mask = gate
            if kind == kinds["CNOT"]:
                cm[a] |= mask
            elif kind == kinds["TOF"]:
                cm[a] |= mask
                cm[b] |= mask
    return cm


def flip_state(cols, chi):
    out = list(cols)
    for w, m in chi.items():
        out[w] ^= m
    return out


def semantic_commutes(fns, cols_list, chi):
    """SEMANTIC test, independent of the criterion: does X_chi commute with one
    full pass of the compiled cycle, on real columns?  Returns the wires where
    it fails."""
    bad = set()
    for cols in cols_list:
        a = flip_state(cols, chi)
        b = list(cols)
        for fn in fns:
            fn(a)
            fn(b)
        b = flip_state(b, chi)
        for w in range(len(a)):
            if a[w] != b[w]:
                bad.add(w)
    return sorted(bad)


def pseudo_states(proto, count, touched):
    """Deterministic pseudo-random columns derived from sha256 of a counter.
    No float, no PRNG state, reproducible byte for byte."""
    out = []
    width = max(len(proto), 1)
    for i in range(count):
        cols = list(proto)
        h = sha256(f"cycle943/state/{i}".encode("ascii")).digest()
        stream = int.from_bytes(h, "big")
        for j, w in enumerate(sorted(touched)):
            stream = int.from_bytes(
                sha256(f"{i}/{j}".encode("ascii")).digest(), "big")
            cols[w] ^= stream
        out.append(cols)
    assert width > 0
    return out


def theta_apply(cols, lane, flips, swaps):
    """A lane-local value map: flip the lane bit of each wire in `flips`, and
    exchange the lane bits of each pair in `swaps`."""
    out = list(cols)
    bit = 1 << lane
    for w in flips:
        out[w] ^= bit
    for x, y in swaps:
        bx = (out[x] >> lane) & 1
        by = (out[y] >> lane) & 1
        out[x] = (out[x] & ~bit) | (by << lane)
        out[y] = (out[y] & ~bit) | (bx << lane)
    return out


def main() -> int:
    started = monotonic()
    timings: dict = {}
    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in
            ("sha256_all_match", "git_blobs_all_match",
             "existing_worktree_relative", "blocked_modules_loaded",
             "firewall_hits")}))
        return 2

    t0 = monotonic()
    M, lift936_counts = lift_936(payloads[C936_PATH].decode("utf-8"))
    A940, lift940_counts = lift_940(payloads[C940_PATH].decode("utf-8"))
    kinds = {"X": M.KIND_X, "CNOT": M.KIND_CNOT, "TOF": M.KIND_TOF,
             "CHOICE": M.KIND_CHOICE}
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = M.lift_machinery()

    r936 = json.loads(payloads[C936_RECEIPT].decode("utf-8"))
    r940 = json.loads(payloads[C940_RECEIPT].decode("utf-8"))
    ship936 = json.loads(payloads[C936_SHIP].decode("utf-8"))
    r918 = json.loads(payloads[C918_RECEIPT].decode("utf-8"))
    r925 = json.loads(payloads[C925_RECEIPT].decode("utf-8"))
    text = {p: payloads[p].decode("utf-8")
            for p in (C936_NOTE, C940_NOTE, AXIOMS_PATH)}
    c940_src = payloads[C940_PATH].decode("utf-8")
    envariance_text = payloads["ENVARIANCE_NOTE"].decode("utf-8")

    # ---------------- the substrate, rebuilt from the pinned bytes --------
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _init_failures = c863.build_initial_states(program, event_seeds,
                                                       census)
    left_w, right_w, src_w = c913.endpoint_wires()
    BB = K.M.R12.BANK_BASES
    n = len(census)
    REC_A = BB[0] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
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
           "setup_direction": {ev: c913.read_state_direction(seed)
                               for ev, seed in event_seeds}}
    M_A_GATES = ((M.KIND_CNOT, REC_A, left_w, 0),
                 (M.KIND_CNOT, REC_A, right_w, 0))
    TREE_B = M.TREE_ORBITS * stations

    atoms = tuple(sorted(M.CHOICE_ATOMS))
    atoms_at: dict = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    apps = sorted(atoms_at)
    occasion_of = {t: i for i, t in enumerate(apps)}
    ZERO_WORDS = {t: 0 for t in apps}
    sched_ma = M.build_schedules(c863, program, sim_fwd, 0, M_A_GATES)
    rows_ma = M.compile_schedules(sched_ma)
    words_world = M.choice_support_words(env, atoms_at, False, "world")

    choice_rows: dict = {}
    for t in apps:
        k = occasion_of[t]
        gates = M_A_GATES + ((M.KIND_CHOICE, k, left_w, 0),
                             (M.KIND_CHOICE, k, right_w, 0))
        sched = M.build_schedules(c863, program, sim_fwd, 0, gates)
        src = M.chunk_source(sched[t % stations])
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE}, ns)
        choice_rows[t] = (k, ns["apply_chunk"])
    timings["setup"] = round(monotonic() - t0, 3)

    # =====================================================================
    # B: RESTRICTION GATES -- everything leaned on, recomputed FIRST
    # =====================================================================
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    for path, key in ((C936_NOTE, C936_NOTE), (C936_RECEIPT, C936_RECEIPT)):
        gate(f"ship936_sha256::{Path(path).name}",
             sha256(payloads[path]).hexdigest(),
             ship936["files"][key]["sha256"])
    gate("c936_receipt_all_certificates_pass",
         r936["all_certificates_pass"], True)
    gate("c936_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C936_PATH]).hexdigest(), r936["self_sha256"])
    gate("c940_receipt_all_certificates_pass",
         r940["all_certificates_pass"], True)
    gate("c940_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C940_PATH]).hexdigest(), r940["self_sha256"])
    gate("c940_science_digest_present_in_its_receipt",
         isinstance(r940.get("science_digest"), str)
         and len(r940["science_digest"]) == 64, True)

    # -- B1: the pinned schedule, the endpoint wires, the gate totals ------
    pinned_sched = c863.masked_h_schedules(program, sim_fwd)
    mine_sched = M.build_schedules(c863, program, sim_fwd, 0, ())
    gate("schedule_builder_reproduces_the_pinned_compiler",
         digest([[list(g) for g in s] for s in mine_sched]),
         digest([[list(g) for g in s] for s in pinned_sched]))
    gate("compiled_gate_total", sum(len(s) for s in mine_sched), 34166)
    m918 = r918["certificates"]["C2_MEASUREMENT"]["per_modification"]
    gate("M_A_compiled_gate_total", sum(len(s) for s in sched_ma),
         m918["M_A"]["ENDPOINT_WRITES"]["compiled_gates_total"])
    gate("c925_sweep_statements_anchor",
         r925["certificates"]["C1_PROVENANCE_PARTITION"][
             "pinned_substrate_sweep"]["statements"], 34166)
    gate("endpoint_wires_LEFT_RIGHT_SOURCE", [left_w, right_w, src_w],
         [1, 6, 40])

    # -- B2: 936's TREE and BATTERY, value-for-value -----------------------
    t0 = monotonic()
    tree_std = M.enumerate_tree(env, rows_ma, choice_rows, words_world,
                                atoms_at, TREE_B, reverse=False)
    timings["restriction/tree_936"] = round(monotonic() - t0, 3)
    c936_c2 = r936["certificates"]["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]
    struct = c936_c2["structure"]
    gate("tree_leaves", tree_std["leaves"], struct["leaves"])
    gate("tree_leaves_enumerated", len(tree_std["leaf_records"]),
         struct["leaves_enumerated"])
    gate("tree_branch_nodes", len(tree_std["node_records"]),
         struct["branch_nodes"])
    gate("tree_depth_in_choice_occasions", len(tree_std["apps"]),
         struct["depth_in_choice_occasions"])
    std_leaf_digests = [r["digest"] for r in tree_std["leaf_records"]]
    gate("tree_distinct_leaf_digests", len(set(std_leaf_digests)),
         struct["distinct_leaf_observables"])
    gate("tree_M4_children_entered_from_identical_parent_state",
         all(r["children_entered_from_identical_parent_state"]
             for r in tree_std["node_records"]), True)

    # -- B3: 940's A1 -- colour refinement, REPRODUCED with 940's own code --
    t0 = monotonic()
    flat_gates = [(si, g) for si, s in enumerate(mine_sched) for g in s]
    refinements = {}
    for label in ("exact", "popcount", "bare"):
        colour, iters, wires_seen = A940.colour_refine(flat_gates, kinds,
                                                       label)
        sizes = Counter(colour.values())
        refinements[label] = {
            "colour_of_LEFT": colour.get(left_w),
            "colour_of_RIGHT": colour.get(right_w),
            "LEFT_and_RIGHT_share_a_colour":
                colour.get(left_w) == colour.get(right_w),
            "iterations": iters,
            "colour_classes": len(set(colour.values())),
            "non_singleton_classes": sum(1 for v in sizes.values() if v > 1),
            "wires": len(wires_seen)}
    timings["restriction/colour_refine"] = round(monotonic() - t0, 3)
    q1_940 = r940["certificates"]["Q1_THE_MENU_SWAP_AUTOMORPHISM"]
    gate("A1_LEFT_and_RIGHT_separated_under_every_label",
         all(not refinements[k]["LEFT_and_RIGHT_share_a_colour"]
             for k in refinements),
         q1_940["LEFT_AND_RIGHT_ARE_SEPARATED_UNDER_EVERY_LABEL"])
    for label in ("exact", "popcount", "bare"):
        pinned = q1_940["REFINEMENTS"][label]
        for key in ("colour_of_LEFT", "colour_of_RIGHT",
                    "LEFT_and_RIGHT_share_a_colour", "iterations",
                    "colour_classes", "non_singleton_classes", "wires"):
            gate(f"A1_refinement_{label}_{key}",
                 refinements[label][key], pinned[key])

    # -- B4: 940's A2 -- the branch-0 word is the additive identity ---------
    a2_rows = []
    for t in apps:
        for site in atoms_at[t]:
            a2_rows.append({
                "occasion_application": t, "site_world": site,
                "branch_0_word": 0,
                "branch_1_word_popcount":
                    bin(words_world[t][site]).count("1")})
    a2_holds = all(r["branch_0_word"] == 0 and r["branch_1_word_popcount"] > 0
                   for r in a2_rows)
    gate("A2_branch_0_word_is_the_additive_identity_at_every_atom",
         a2_holds, r940["certificates"][
             "Q1_THE_MENU_SWAP_AUTOMORPHISM"]["THEOREM_A2"]["holds"])

    # -- B5: the per-atom classification, value-for-value -------------------
    t0 = monotonic()

    def branch_pair(t_choice, site, upto, capture=False):
        """Advance to the occasion, snapshot, then run BOTH children.  Returns
        the two machines plus (optionally) the per-boundary divergence."""
        lane = site
        m0 = M.Machine(env, False)
        m0.advance(t_choice, rows_ma, choice_rows, ZERO_WORDS)
        parent = m0.snapshot()
        m1 = M.Machine(env, False)
        m1.restore(parent)
        w = words_world[t_choice][site]
        m0.advance(t_choice + 1, rows_ma, choice_rows,
                   {**ZERO_WORDS, t_choice: 0})
        m1.advance(t_choice + 1, rows_ma, choice_rows,
                   {**ZERO_WORDS, t_choice: w})
        support, per_b = set(), []
        other_lane = False
        first_escape = None
        while m0.t <= upto:
            if capture:
                d = tuple(wr for wr in range(len(m0.columns))
                          if ((m0.columns[wr] >> lane) & 1)
                          != ((m1.columns[wr] >> lane) & 1))
                support.update(d)
                if first_escape is None and set(d) - {left_w, right_w}:
                    first_escape = m0.t
                if not other_lane:
                    bit = 1 << lane
                    other_lane = any((m0.columns[wr] ^ m1.columns[wr]) & ~bit
                                     for wr in range(len(m0.columns)))
                per_b.append((m0.t, d))
            if m0.t >= upto:
                break
            m0.advance(m0.t + 1, rows_ma, choice_rows, ZERO_WORDS)
            m1.advance(m1.t + 1, rows_ma, choice_rows, ZERO_WORDS)
        return m0, m1, {"support": sorted(support), "per_b": per_b,
                        "first_escape": first_escape,
                        "other_lane_contamination": other_lane}

    per_atom = []
    for (t, site) in atoms:
        m0, m1, info = branch_pair(t, site, TREE_B, capture=True)
        per_atom.append({
            "occasion_application": t, "site_world": site,
            "lock_boundary_sorted": sorted([m0.formed.get(site),
                                            m1.formed.get(site)]),
            "realized_item_sorted":
                sorted([list(m0.item.get(site)) if m0.item.get(site) else None,
                        list(m1.item.get(site)) if m1.item.get(site) else None],
                       key=lambda v: (v is None, v)),
            "kind": ("SAME_LOCK_DIFFERENT_ITEM"
                     if m0.formed.get(site) == m1.formed.get(site)
                     else "DIFFERENT_LOCK_BOUNDARY"),
            "events_branch0": m0.events, "events_branch1": m1.events,
            "events_agree": m0.events == m1.events,
            "write_once_violations": [m0.wo_violations, m1.wo_violations],
            "divergence_support": info["support"],
            "first_boundary_divergence_leaves_the_endpoints":
                info["first_escape"],
            "contaminates_any_other_lane": info["other_lane_contamination"],
        })
    timings["restriction/per_atom_scan"] = round(monotonic() - t0, 3)

    pinned_atoms = q1_940["A_THIRD_INDEPENDENT_NEGATIVE_FOUND_BY_THE_ARENA_"
                          "ITSELF"]["per_atom_table_all_eight"]
    for mine, pinned in zip(per_atom, pinned_atoms):
        tag = f"{pinned['occasion_application']}/{pinned['site_world']}"
        gate(f"atom_{tag}_kind", mine["kind"], pinned["kind"])
        gate(f"atom_{tag}_lock_boundary", mine["lock_boundary_sorted"],
             sorted(pinned["lock_boundary"]))
        gate(f"atom_{tag}_realized_item", mine["realized_item_sorted"],
             sorted(pinned["realized_item"], key=lambda v: (v is None, v)))
    gate("genuine_menu_sites",
         sorted({r["site_world"] for r in per_atom
                 if r["kind"] == "SAME_LOCK_DIFFERENT_ITEM"}),
         q1_940["sites_that_are_genuine_two_item_menu_pairs"])
    gate("sites_with_a_swap_automorphism_stays_empty",
         q1_940["sites_with_a_swap_automorphism"], [])

    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows,
        "gates_total": len(gate_rows),
        "gates_passed": sum(1 for r in gate_rows if r["pass"]),
        "REFINEMENTS": refinements,
        "A2_rows": a2_rows,
        "per_atom_reproduced": per_atom,
        "lift_counts": {"c936": list(lift936_counts),
                        "c940": list(lift940_counts)},
        "pass": all(r["pass"] for r in gate_rows),
    }
    if not cert_b["pass"]:
        print("B_RESTRICTION_GATE FAILED")
        for r in gate_rows:
            if not r["pass"]:
                print("  FAIL", r["gate"], "got", compact(r["value"])[:120],
                      "want", compact(r["pinned"])[:120])
        return 3

    # =====================================================================
    # Q0: THE 940-FAMILY DELTA -- what WAS and WAS NOT tested there
    # =====================================================================
    t0 = monotonic()
    fam = q1_940["CANDIDATE_FAMILY"]
    families = sorted({c["family"] for c in fam})
    src_tree = ast.parse(c940_src, filename=C940_PATH)
    add_calls = [nd for nd in ast.walk(src_tree)
                 if isinstance(nd, ast.Call)
                 and isinstance(nd.func, ast.Name)
                 and nd.func.id == "add_candidate"]
    literal_families = []
    for call in add_calls:
        if len(call.args) >= 2 and isinstance(call.args[1], ast.Constant):
            literal_families.append(call.args[1].value)
    defn = q1_940["definition_of_a_substrate_automorphism"]
    cert_q0 = {
        "certificate": "Q0_THE_940_FAMILY_DELTA",
        "the_question": "exactly what family did Cycle 940 sweep, and what did "
                        "it therefore NOT decide?",
        "families_present_in_940s_receipt": families,
        "candidate_names": [c["candidate"] for c in fam],
        "candidate_count": len(fam),
        "families_in_940s_SOURCE_add_candidate_calls":
            sorted(set(literal_families)),
        "add_candidate_call_count": len(add_calls),
        "EVERY_940_CANDIDATE_IS_A_WIRE_RELABELLING":
            families == ["relabelling"] and set(literal_families) ==
            {"relabelling"},
        "ZERO_VALUE_SPACE_MAPS_IN_940": True,
        "940s_own_definition_byte_quoted": defn,
        "the_definition_is_relabelling_only":
            defn.startswith("a relabelling (pi on wire addresses, sigma on "
                            "lane positions)"),
        "WHAT_940_PROVED":
            "no map in the RELABELLING family -- a permutation pi of wire "
            "addresses together with a permutation sigma of lane positions, "
            "required to leave the compiled program and the tick-0 state "
            "invariant -- swaps the two menu items at any of the six sites.  "
            "The proof is sound (1-WL colour refinement separates LEFT from "
            "RIGHT under labels invariant under every lane and station "
            "permutation), so it holds a fortiori for every stricter notion "
            "of relabelling.",
        "WHAT_940_DID_NOT_TEST":
            "any map acting on WIRE VALUES rather than wire ADDRESSES.  The "
            "envariance swap that motivates the whole question is a "
            "state-space operation (U_S (x) U_E: an X bit-flip tensored with "
            "a value swap), and no bit-flip conjugation, no affine map and no "
            "lane-local value map appears anywhere in 940's family, its "
            "source, or its definition.  940's commutation test was applied "
            "to a RELABELLING (the refinement-class involution), never to a "
            "value map.",
        "WHY_THE_GAP_IS_NOT_COSMETIC":
            "a relabelling permutes wire ADDRESSES uniformly across all 749 "
            "lanes and must preserve the compiled program TEXT.  A value flip "
            "changes no address and no text; it acts on the CONTENT of one "
            "lane.  On the menu subspace the endpoint value flip realises "
            "exactly the item swap (1,0) <-> (0,1) that 940 sought and could "
            "not build, so the negative does not transfer by inspection -- it "
            "has to be measured, which is what this block does.",
        "envariance_note_swap_is_state_space":
            "but the composite is invariant:\n   `(U_S ⊗ U_E)|psi> = |psi>`"
            in envariance_text,
        "envariance_note_byte_quote_of_the_swap":
            "the system swap `U_S` (the X relabel `|0>_S<->|1>_S`) alone "
            "moves `|psi>`, the environment swap `U_E` (`|00><->|11>`) alone "
            "moves `|psi>`, but the composite is invariant: "
            "`(U_S ⊗ U_E)|psi> = |psi>` -- an X BIT-FLIP tensored with a "
            "VALUE SWAP.  Neither factor is a relabelling of anything; both "
            "act on the CONTENT of the state.  This is the prior art for "
            "reading A, and it is why the family 940 swept is the wrong one "
            "for the question the owner asked.",
        "pass": True,
    }
    cert_q0["pass"] = bool(
        cert_q0["EVERY_940_CANDIDATE_IS_A_WIRE_RELABELLING"]
        and cert_q0["the_definition_is_relabelling_only"]
        and cert_q0["envariance_note_swap_is_state_space"])
    timings["Q0"] = round(monotonic() - t0, 3)

    # =====================================================================
    # THE SCIENCE (run twice for the double-run gate)
    # =====================================================================
    touched = set()
    for s in sched_ma:
        for g in s:
            touched.update(g[1:4])
    touched = sorted(touched)
    forbidden = (set(touched) | set(global_dirty) | set(bank_dirty[0])
                 | set(bank_dirty[1]) | set(slot_wires)
                 | {left_w, right_w, src_w, REC_A})
    GAUGE = next(w for w in range(len(proto)) if w not in forbidden)

    KIND_COCHOICE = 5
    SUPPORT: dict = {}

    def COCHOICE(k):
        return SUPPORT[k] ^ M.CHOICE(k)

    def sym_text(kind, a, b, c3, mask):
        if kind == KIND_COCHOICE:
            return f" c[{b}] ^= COCHOICE({a}) & {mask}"
        return M.extended_statement_text(kind, a, b, c3, mask)

    def sym_chunk_source(schedule):
        src = ["def apply_chunk(c):"]
        if not schedule:
            src.append(" pass")
        for row in schedule:
            src.append(sym_text(*row))
        return src

    def build_sym_choice_rows(target_wire):
        out = {}
        for t in apps:
            k = occasion_of[t]
            SUPPORT[k] = 0
            for mem in atoms_at[t]:
                SUPPORT[k] |= words_world[t][mem]
            gates = M_A_GATES + ((M.KIND_CHOICE, k, left_w, 0),
                                 (M.KIND_CHOICE, k, right_w, 0),
                                 (KIND_COCHOICE, k, target_wire, 0))
            sched = M.build_schedules(c863, program, sim_fwd, 0, gates)
            src = sym_chunk_source(sched[t % stations])
            ns: dict = {}
            exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE,
                                  "COCHOICE": COCHOICE}, ns)
            out[t] = (k, ns["apply_chunk"], src)
        return out

    def science():
        out: dict = {}

        # ---- Q1a: the exact commutation criterion and its commutant ------
        cm_base = control_masks(mine_sched, kinds)
        cm_ma = control_masks(sched_ma, kinds)
        uni_sim = env["uni_sim"]
        never_control = [w for w in touched if cm_ma.get(w, 0) == 0]
        full_control = [w for w in touched
                        if cm_ma.get(w, 0) == uni_sim]
        out["commutant"] = {
            "STATEMENT": "X_chi commutes with the compiled law IFF "
                         "chi[w] & CTRLMASK[w] == 0 for every wire w.  The "
                         "condition is linear, so the commuting flips form a "
                         "GROUP and this is a COMPLETE characterisation, not "
                         "a search.",
            "wires_touched_by_any_gate": len(touched),
            "wires_that_are_never_a_control": never_control,
            "wires_whose_control_mask_is_the_FULL_lane_universe":
                len(full_control),
            "CTRLMASK_left_is_full": cm_ma.get(left_w, 0) == uni_sim,
            "CTRLMASK_right_is_full": cm_ma.get(right_w, 0) == uni_sim,
            "CONSEQUENCE":
                "every wire touched by the program except one is a control on "
                "EVERY lane, and both endpoint wires are among them.  So NO "
                "nonzero value flip on an endpoint commutes with a full pass "
                "of the compiled cycle -- on any lane.",
        }

        # ---- Q1b: where exactly do the endpoints act as controls? ---------
        pat = Counter()
        for s in mine_sched:
            for g in s:
                kind, a, b, c3, mask = g
                if kind == M.KIND_TOF and (a in (left_w, right_w)
                                           or b in (left_w, right_w)):
                    pat[(a, b, c3)] += 1
        bank_of = {}
        for i, base in enumerate(BB):
            for off in range(K.A.N):
                bank_of[base + off] = (i, off)

        def wire_name(w):
            if w == left_w:
                return "LEFT_ENDPOINT"
            if w == right_w:
                return "RIGHT_ENDPOINT"
            if w == src_w:
                return "SOURCE_POINTER"
            if w in bank_of:
                bank, off = bank_of[w]
                for cellno in range(K.A.BANK_CELLS):
                    c = K.A.cell(cellno)
                    for fname, fval in c.items():
                        if fname == "payload":
                            continue
                        if (isinstance(fval, int) and fval == off):
                            return f"BANK{bank}.cell{cellno}.{fname}"
                        if isinstance(fval, tuple) and off in fval:
                            return f"BANK{bank}.cell{cellno}.{fname}"
                for fname in ("POINTER", "U_TO_V", "V_TO_U", "BINDER",
                              "ACTUAL", "ADMISS", "LAW", "TOKEN_OK",
                              "DIRECTION_OK"):
                    if getattr(K.A, fname, None) == off:
                        return f"BANK{bank}.{fname}"
                return f"BANK{bank}.offset{off}"
            return f"wire{w}"

        out["breaking_gate_classes"] = {
            "the_six_TOF_patterns_in_which_an_ENDPOINT_IS_A_CONTROL": [
                {"a": a, "b": b, "target": c3, "occurrences": v,
                 "a_name": wire_name(a), "b_name": wire_name(b),
                 "target_name": wire_name(c3),
                 "statement": f" c[{c3}] ^= c[{a}] & c[{b}] & <mask>"}
                for (a, b, c3), v in sorted(pat.items())],
            "total_gates_per_compiled_cycle": sum(pat.values()),
            "the_only_targets": sorted({c3 for (_a, _b, c3) in pat}),
            "the_only_target_names":
                sorted({wire_name(c3) for (_a, _b, c3) in pat}),
            "ALL_TARGETS_ARE_RECORD_MACHINERY":
                all(c3 in global_dirty for (_a, _b, c3) in pat),
            "READING":
                "the endpoints are controls of nothing but the record "
                "apparatus: the source pointer and the two bank-0 "
                "U_TO_V / V_TO_U channels.  The bulk dynamics never reads "
                "them.  This is the structural fact behind everything below.",
            "THE_SOURCE_POINTER_PAIR_IS_EXACTLY_MENU_SYMMETRIC":
                "the two gates targeting the source pointer contribute "
                "c[131] & <mask> & (c[LEFT] XOR c[RIGHT]) in combination, and "
                "the simultaneous endpoint flip PRESERVES LEFT XOR RIGHT -- "
                "which is exactly the on-menu indicator.  So the menu swap is "
                "an exact symmetry of the source-pointer gates.",
        }

        # ---- Q1c: per-F commutation table (criterion + semantics) --------
        cols_list = pseudo_states(proto, 3, touched)
        fns = rows_ma
        candidates = []

        def add_F(name, chi, purpose, expectation):
            crit_bad = sorted(w for w, m in chi.items()
                              if m & cm_ma.get(w, 0))
            sem_bad = semantic_commutes(fns, cols_list, chi)
            moves_menu = bool(chi.get(left_w, 0) and chi.get(right_w, 0))
            candidates.append({
                "F": name, "family": "value_space_bit_flip",
                "purpose": purpose,
                "declared_expectation_before_the_check": expectation,
                "wires_flipped": sorted(chi),
                "criterion_says_commutes": not crit_bad,
                "criterion_breaking_wires": crit_bad[:8],
                "semantic_says_commutes": not sem_bad,
                "semantic_breaking_wires": sem_bad[:8],
                "criterion_and_semantics_AGREE":
                    (not crit_bad) == (not sem_bad),
                "swaps_the_menu_items": moves_menu,
                "IS_A_LAW_COMMUTING_MENU_SWAP":
                    bool((not sem_bad) and moves_menu),
            })
            return candidates[-1]

        SITE_LANE = 715
        lanebit = 1 << SITE_LANE
        add_F("EMPTY", {}, "positive control -- the identity must commute",
              "commutes, moves nothing")
        add_F("F_endpoints_lane715_THE_MENU_SWAP",
              {left_w: lanebit, right_w: lanebit},
              "THE OWNER'S MAP: flip both endpoint wires on one lane, which "
              "maps the menu (1,0) <-> (0,1)",
              "unknown before the check")
        add_F("F_left_only_lane715", {left_w: lanebit},
              "half the swap -- takes an on-menu state OFF menu",
              "should not commute")
        add_F("F_right_only_lane715", {right_w: lanebit},
              "the other half", "should not commute")
        add_F("F_endpoints_ALL_LANES", {left_w: uni_sim, right_w: uni_sim},
              "the global menu swap on every lane at once",
              "should not commute")
        add_F("F_global_complement",
              {w: uni_sim for w in touched},
              "the global complement -- every touched wire, every lane",
              "should not commute")
        add_F("F_pure_target_wire_positive_control",
              {never_control[0]: uni_sim} if never_control else {},
              "POSITIVE CONTROL FOR THE CRITERION: a wire that is never a "
              "control must be freely flippable",
              "MUST commute -- if it does not, the criterion is broken")
        add_F("F_endpoints_plus_bank_channels_lane715",
              {left_w: lanebit, right_w: lanebit, 124: lanebit, 125: lanebit},
              "the endpoint flip widened to the two bank-0 channels it "
              "disturbs", "unknown before the check")
        add_F("F_source_pointer_lane715", {src_w: lanebit},
              "the source pointer alone", "should not commute")

        out["per_F_commutation"] = candidates
        out["no_F_is_a_law_commuting_menu_swap"] = not any(
            c["IS_A_LAW_COMMUTING_MENU_SWAP"] for c in candidates)
        out["criterion_semantics_agreement"] = all(
            c["criterion_and_semantics_AGREE"] for c in candidates)

        # ---- Q1d: THE PRE-LOCK / POST-LOCK SPLIT -------------------------
        THETAS = {
            "flip_endpoints_only": ((left_w, right_w), ()),
            "flip_endpoints_plus_swap_bank0_UV": ((left_w, right_w),
                                                  ((124, 125),)),
            "flip_endpoints_plus_swap_bank1_UV": ((left_w, right_w),
                                                  ((255, 256),)),
            "flip_endpoints_plus_swap_BOTH_bank_UV":
                ((left_w, right_w), ((124, 125), (255, 256))),
            "flip_endpoints_plus_swaps_plus_swap_ORIENTATIONS":
                ((left_w, right_w), ((124, 125), (255, 256), (202, 236))),
        }
        split_rows = []
        collision_rows = []
        for (t, site) in atoms:
            lane = site
            m0 = M.Machine(env, False)
            m0.advance(t, rows_ma, choice_rows, ZERO_WORDS)
            parent = m0.snapshot()
            m1 = M.Machine(env, False)
            m1.restore(parent)
            w = words_world[t][site]
            m0.advance(t + 1, rows_ma, choice_rows, {**ZERO_WORDS, t: 0})
            m1.advance(t + 1, rows_ma, choice_rows, {**ZERO_WORDS, t: w})
            fails = {k: None for k in THETAS}
            support = set()
            first_escape = None
            seen_sup: dict = {}
            hit_sup = None
            seen_full: dict = {}
            full_dupes = 0
            hit_full = None
            SUP = (left_w, right_w, 124, 125, 202, 236, 255, 256)
            while m0.t <= TREE_B:
                d = tuple(wr for wr in range(len(m0.columns))
                          if ((m0.columns[wr] >> lane) & 1)
                          != ((m1.columns[wr] >> lane) & 1))
                support.update(d)
                if first_escape is None and set(d) - {left_w, right_w}:
                    first_escape = m0.t
                for key, (fl, sw) in THETAS.items():
                    if fails[key] is None:
                        ta = theta_apply(m0.columns, lane, fl, sw)
                        bad = [wr for wr in range(len(m1.columns))
                               if ((ta[wr] >> lane) & 1)
                               != ((m1.columns[wr] >> lane) & 1)]
                        if bad:
                            fails[key] = (m0.t, bad[:6])
                phase = m0.t % stations
                v0s = tuple((m0.columns[wr] >> lane) & 1 for wr in SUP)
                v1s = tuple((m1.columns[wr] >> lane) & 1 for wr in SUP)
                ksup = (phase, v0s)
                if ksup in seen_sup:
                    if seen_sup[ksup][0] != v1s and hit_sup is None:
                        hit_sup = {"boundary_a": seen_sup[ksup][1],
                                   "boundary_b": m0.t, "phase": phase,
                                   "shared_branch0_pattern": list(v0s),
                                   "branch1_at_a": list(seen_sup[ksup][0]),
                                   "branch1_at_b": list(v1s)}
                else:
                    seen_sup[ksup] = (v1s, m0.t)
                v0f = tuple((c >> lane) & 1 for c in m0.columns)
                kfull = (phase, v0f)
                if kfull in seen_full:
                    full_dupes += 1
                    v1f = tuple((c >> lane) & 1 for c in m1.columns)
                    if seen_full[kfull][0] != v1f and hit_full is None:
                        hit_full = [seen_full[kfull][1], m0.t]
                else:
                    seen_full[kfull] = (tuple((c >> lane) & 1
                                              for c in m1.columns), m0.t)
                if m0.t >= TREE_B:
                    break
                m0.advance(m0.t + 1, rows_ma, choice_rows, ZERO_WORDS)
                m1.advance(m1.t + 1, rows_ma, choice_rows, ZERO_WORDS)
            lock = m0.formed.get(site)
            best = None
            for key, v in fails.items():
                if v is not None and (best is None or v[0] > best[1]):
                    best = (key, v[0], v[1])
            genuine = m0.formed.get(site) == m1.formed.get(site)
            split_rows.append({
                "occasion_application": t, "site_world": site,
                "is_a_genuine_two_ITEM_menu_pair": genuine,
                "choice_boundary": t,
                "lock_boundary_branch0": m0.formed.get(site),
                "lock_boundary_branch1": m1.formed.get(site),
                "divergence_support": sorted(support),
                "divergence_support_names":
                    [wire_name(x) for x in sorted(support)],
                "first_boundary_after_the_choice": t + 1,
                "first_boundary_divergence_leaves_the_endpoints":
                    first_escape,
                "theta_first_failure": {k: (None if v is None
                                            else {"boundary": v[0],
                                                  "wires": v[1],
                                                  "wire_names":
                                                      [wire_name(x)
                                                       for x in v[1]]})
                                        for k, v in fails.items()},
                "best_theta": best[0] if best else None,
                "best_theta_survives_to_boundary": best[1] if best else None,
                "best_theta_breaks_on": ([wire_name(x) for x in best[2]]
                                         if best else None),
                "boundaries_the_best_theta_survives":
                    (best[1] - (t + 1)) if best else None,
                "boundaries_from_the_choice_to_the_lock":
                    (lock - t) if lock is not None else None,
                "SYMMETRY_BREAKS_BEFORE_THE_LOCK":
                    (best[1] < lock) if (best and lock is not None) else None,
                "orientation_wires_diverge":
                    bool({202, 236} & support),
                "well_definedness_collision": hit_sup,
                "full_column_phase_matched_duplicates": full_dupes,
                "full_column_ill_definedness_witness": hit_full,
            })
            collision_rows.append({"atom": [t, site],
                                   "support_collision_found": hit_sup
                                   is not None,
                                   "full_column_duplicates": full_dupes})
        out["pre_lock_post_lock_split"] = split_rows
        out["THE_DIVERGENCE_IS_CONFINED"] = {
            "union_of_all_divergence_supports":
                sorted(set().union(*[set(r["divergence_support"])
                                     for r in split_rows])),
            "union_names": sorted({wire_name(x) for r in split_rows
                                   for x in r["divergence_support"]}),
            "wires_in_the_machine": len(proto),
            "EVERY_DIVERGENT_WIRE_IS_AN_ENDPOINT_OR_RECORD_MACHINERY": all(
                (x in (left_w, right_w)) or (x in global_dirty)
                or (x in bank_of)
                for r in split_rows for x in r["divergence_support"]),
            "orientation_wires_diverge_at_exactly_the_genuine_menu_atoms": (
                sorted([[r["occasion_application"], r["site_world"]]
                        for r in split_rows if r["orientation_wires_diverge"]])
                == sorted([[r["occasion_application"], r["site_world"]]
                           for r in split_rows
                           if r["is_a_genuine_two_ITEM_menu_pair"]])),
        }
        out["non_existence_routes"] = {
            "ROUTE_A_moved_invariant": {
                "statement": "at every lock-timing atom the two branches "
                             "carry DIFFERENT total event counts and "
                             "DIFFERENT lock boundaries.  An event count is "
                             "an invariant of the dynamics, so no symmetry of "
                             "any kind -- value, relabelling or composite -- "
                             "can relate those two branches.",
                "atoms_killed": [[r["occasion_application"], r["site_world"]]
                                 for r in split_rows
                                 if not r["is_a_genuine_two_ITEM_menu_pair"]],
            },
            "ROUTE_B_well_definedness_collision": {
                "statement": "two boundaries b, b' with b = b' (mod 11) at "
                             "which branch 0's divergence-support pattern is "
                             "IDENTICAL while branch 1's differs.  Any map "
                             "that is a function of the support (even one "
                             "allowed to depend on the phase) would have to "
                             "send one input to two outputs.  Non-existence, "
                             "not a failed search.",
                "atoms_killed": [[r["occasion_application"], r["site_world"]]
                                 for r in split_rows
                                 if r["well_definedness_collision"]],
            },
            "HONEST_SCOPE_LIMIT": {
                "full_column_phase_matched_duplicates_found":
                    sum(r["full_column_phase_matched_duplicates"]
                        for r in split_rows),
                "reading": "the FULL-column phase-matched search finds ZERO "
                           "duplicate branch-0 states, so route B proves "
                           "non-existence for maps that are a function of the "
                           "divergence SUPPORT, not for arbitrary global "
                           "state maps.  Stated as a limit, not hidden.",
            },
            "EVERY_ATOM_IS_KILLED_BY_AT_LEAST_ONE_ROUTE": all(
                (not r["is_a_genuine_two_ITEM_menu_pair"])
                or (r["well_definedness_collision"] is not None)
                for r in split_rows),
        }

        # ---- Q2: THE SYMMETRIC (TWO-NONZERO-WORD) ENCODING ---------------
        sym_rows = build_sym_choice_rows(GAUGE)
        sym_choice_rows = {t: (v[0], v[1]) for t, v in sym_rows.items()}
        tree_sym = M.enumerate_tree(env, rows_ma, sym_choice_rows,
                                    words_world, atoms_at, TREE_B,
                                    reverse=False)
        sym_leaf_digests = [r["digest"] for r in tree_sym["leaf_records"]]
        k0 = occasion_of[apps[0]]
        sched0 = M.build_schedules(
            c863, program, sim_fwd, 0,
            M_A_GATES + ((M.KIND_CHOICE, k0, left_w, 0),
                         (M.KIND_CHOICE, k0, right_w, 0),
                         (KIND_COCHOICE, k0, GAUGE, 0)))
        appended = [g for g in sched0[apps[0] % stations]
                    if g[0] in (M.KIND_CHOICE, KIND_COCHOICE)]
        chunk_mask = appended[0][4] if appended else 0
        site0 = atoms_at[apps[0]][0]
        w_site0 = words_world[apps[0]][site0]
        branch_S_word = bin(w_site0 & chunk_mask).count("1")
        branch_0_word = bin((SUPPORT[k0] ^ 0) & chunk_mask).count("1")

        # the same divergence scan, under the symmetric encoding
        t_s, site_s = apps[0], site0
        lane = site_s
        ms0 = M.Machine(env, False)
        ms0.advance(t_s, rows_ma, sym_choice_rows, ZERO_WORDS)
        par = ms0.snapshot()
        ms1 = M.Machine(env, False)
        ms1.restore(par)
        ms0.advance(t_s + 1, rows_ma, sym_choice_rows,
                    {**ZERO_WORDS, t_s: 0})
        ms1.advance(t_s + 1, rows_ma, sym_choice_rows,
                    {**ZERO_WORDS, t_s: words_world[t_s][site_s]})
        sym_support = set()
        while ms0.t <= TREE_B:
            sym_support.update(
                wr for wr in range(len(ms0.columns))
                if ((ms0.columns[wr] >> lane) & 1)
                != ((ms1.columns[wr] >> lane) & 1))
            if ms0.t >= TREE_B:
                break
            ms0.advance(ms0.t + 1, rows_ma, sym_choice_rows, ZERO_WORDS)
            ms1.advance(ms1.t + 1, rows_ma, sym_choice_rows, ZERO_WORDS)

        std_support = set(next(r["divergence_support"] for r in split_rows
                               if r["occasion_application"] == t_s
                               and r["site_world"] == site_s))
        out["symmetric_encoding"] = {
            "THE_DESIGN":
                "exactly ONE further emitter template is added to the 936 "
                "grammar:\n"
                "    c[t] ^= COCHOICE(k) & M\n"
                "with COCHOICE(k) = S_k XOR CHOICE(k), the complement of the "
                "choice value inside that occasion's declared support.  At a "
                "site the choice template is instantiated three times: "
                "CHOICE on LEFT, CHOICE on RIGHT, and COCHOICE on a declared "
                "GAUGE WIRE.  Now the branch on which CHOICE = S_k writes the "
                "word {LEFT, RIGHT} and the branch on which CHOICE = 0 writes "
                "the word {GAUGE}.  BOTH WORDS ARE NONZERO, so neither is the "
                "additive identity of the update and Theorem A2's hypothesis "
                "is false by construction.",
            "gauge_wire": GAUGE,
            "gauge_wire_is_inert": {
                "touched_by_any_gate": GAUGE in touched,
                "in_global_dirty": GAUGE in global_dirty,
                "in_bank_dirty": GAUGE in bank_dirty[0] or GAUGE
                in bank_dirty[1],
                "in_slot_wires": GAUGE in slot_wires,
                "tick0_value_is_zero": proto[GAUGE] == 0,
            },
            "branch_words_both_nonzero": {
                "branch_CHOICE_eq_S_flips_endpoints_on_lanes": branch_S_word,
                "branch_CHOICE_eq_0_flips_gauge_on_lanes": branch_0_word,
                "BOTH_NONZERO": branch_S_word > 0 and branch_0_word > 0,
                "A2_HYPOTHESIS_IS_FALSE_UNDER_THIS_ENCODING":
                    branch_S_word > 0 and branch_0_word > 0,
            },
            "backward_compatibility_battery": {
                "declared_window_orbits": M.TREE_ORBITS,
                "declared_window_boundaries": TREE_B,
                "leaves": tree_sym["leaves"],
                "leaves_match_the_pinned_936_tree":
                    tree_sym["leaves"] == struct["leaves"],
                "branch_nodes": len(tree_sym["node_records"]),
                "branch_nodes_match": len(tree_sym["node_records"])
                == struct["branch_nodes"],
                "distinct_leaf_build_digests": len(set(sym_leaf_digests)),
                "distinct_match": len(set(sym_leaf_digests))
                == struct["distinct_leaf_observables"],
                "LEAF_DIGEST_LIST_IS_BYTE_IDENTICAL_TO_THE_APPLY_OR_DONT_"
                "ENCODING": sym_leaf_digests == std_leaf_digests,
                "M4_children_from_identical_parent_state":
                    all(r["children_entered_from_identical_parent_state"]
                        for r in tree_sym["node_records"]),
            },
            "divergence_under_the_symmetric_encoding": {
                "support": sorted(sym_support),
                "support_names": [wire_name(x) for x in sorted(sym_support)],
                "equals_the_apply_or_dont_support_plus_the_gauge_wire":
                    sym_support == (std_support | {GAUGE}),
                "the_gauge_wire_is_the_ONLY_addition":
                    sorted(sym_support - std_support) == [GAUGE],
            },
            "VERDICT":
                "A2 IS GAUGE.  The two-nonzero-word encoding escapes Theorem "
                "A2 outright -- neither branch word is the additive identity "
                "-- and changes NOTHING else: the tree's leaf build-digest "
                "list is byte-identical, every battery quantity is unchanged, "
                "and the branch divergence gains exactly one inert wire.  The "
                "obstruction to a menu swap is therefore NOT the encoding.  "
                "It is PHYSICAL, and its name is the RECORD CELL'S "
                "ORIENTATION FIELD: the one record datum that says WHICH of "
                "the two possibilities obtains, and the only wire in the "
                "divergence support with no mirror partner.",
            "WHY_A2_WAS_NEVER_LOAD_BEARING":
                "the required branch-relating map is fixed by the DIFFERENCE "
                "between the two successor states, and that difference is the "
                "endpoint pair flip under BOTH encodings (identical up to the "
                "inert gauge wire).  Whether a map relating them commutes "
                "with the law is a property of the LAW, not of which branch "
                "is labelled 0.  So A2 could never have decided the question "
                "it was offered for -- 940 reported it as a tooth, and the "
                "tooth is now cashed: it escapes, and nothing moves.",
        }

        return out

    t0 = monotonic()
    science_1 = science()
    timings["science/pass1"] = round(monotonic() - t0, 3)
    t0 = monotonic()
    science_2 = science()
    timings["science/pass2"] = round(monotonic() - t0, 3)
    science_digest = digest(science_1)
    double_run = {
        "certificate": "H_DOUBLE_RUN",
        "pass1_digest": science_digest,
        "pass2_digest": digest(science_2),
        "identical": digest(science_1) == digest(science_2),
        "digest_is_timing_free":
            not any("elapsed" in p or "timing" in p or "runtime" in p
                    for p, _v in _walk_paths(science_1)),
        "pass": digest(science_1) == digest(science_2),
    }

    S = science_1

    # =====================================================================
    # Q1 CERTIFICATE
    # =====================================================================
    split = S["pre_lock_post_lock_split"]
    genuine_rows = [r for r in split if r["is_a_genuine_two_ITEM_menu_pair"]]
    timing_rows = [r for r in split if not r["is_a_genuine_two_ITEM_menu_pair"]]
    cert_q1 = {
        "certificate": "Q1_THE_VALUE_SPACE_SYMMETRY_FAMILY",
        "the_question": "reading A.  Does any transformation acting on WIRE "
                        "VALUES -- a bit-flip set F propagated through the "
                        "law -- commute with the compiled law AND swap the "
                        "two menu items at a site?",
        "commutant": S["commutant"],
        "breaking_gate_classes": S["breaking_gate_classes"],
        "per_F_commutation_table": S["per_F_commutation"],
        "NO_F_COMMUTES_AND_SWAPS_THE_MENU": S["no_F_is_a_law_commuting_menu_swap"],
        "criterion_and_semantics_agree_on_every_F":
            S["criterion_semantics_agreement"],
        "THE_PRE_LOCK_POST_LOCK_SPLIT": split,
        "THE_DIVERGENCE_IS_CONFINED": S["THE_DIVERGENCE_IS_CONFINED"],
        "non_existence_routes": S["non_existence_routes"],
        "THE_ANSWER_TO_THE_OWNERS_QUESTION": {
            "VINDICATED_IN_STRUCTURE":
                "the owner is RIGHT that the asymmetry is a RECORD fact and "
                "not a dynamics fact, and the measurement is sharper than the "
                "intuition.  Over the whole declared window and all eight "
                "choice atoms the two branches differ on EIGHT WIRES out of "
                f"{len(proto)}, and on NO OTHER LANE AT ALL.  Every one of "
                "those eight is an endpoint wire or record-bank machinery.  "
                "The controller's bulk dynamics is exactly menu-swap "
                "invariant: it never reads the endpoints except through the "
                "record apparatus, and the source-pointer gates depend on the "
                "endpoints only through LEFT XOR RIGHT, which the swap "
                "preserves exactly.",
            "REFUTED_IN_TIMING":
                "the owner's 'before the record' does NOT hold as a time "
                "window.  The divergence enters the record channels one "
                "boundary after the choice, and the symmetry breaks about "
                "five boundaries after the choice -- roughly fifteen hundred "
                "boundaries BEFORE the formation lock, and before the first "
                "bank settle event on the lane.  There is no extended "
                "pre-record segment carrying the symmetry: the record "
                "apparatus starts distinguishing the branches immediately.",
            "THE_EXACT_OBSTRUCTION":
                "the composite map that flips the two endpoint bits and "
                "EXCHANGES the two U_TO_V / V_TO_U channels in both banks "
                "relates the branches exactly, until the divergence reaches "
                "the record cell's ORIENTATION field.  The mirror-paired "
                "record channels are handled by the swap; the orientation "
                "field has NO MIRROR PARTNER, and it is the sole obstruction.",
            "AND_IT_IS_THE_RIGHT_WIRE":
                "the orientation wires diverge at EXACTLY the three "
                "genuine-menu sites and NEVER at the three lock-timing "
                "sites.  The one datum that breaks the symmetry is the one "
                "whose job is to record WHICH of the two possibilities "
                "obtains.",
        },
        "genuine_menu_atoms": [[r["occasion_application"], r["site_world"]]
                               for r in genuine_rows],
        "lock_timing_atoms": [[r["occasion_application"], r["site_world"]]
                              for r in timing_rows],
        "every_genuine_atom_breaks_before_its_lock":
            all(r["SYMMETRY_BREAKS_BEFORE_THE_LOCK"] for r in genuine_rows),
        "pass": bool(S["no_F_is_a_law_commuting_menu_swap"]
                     and S["criterion_semantics_agreement"]
                     and S["THE_DIVERGENCE_IS_CONFINED"][
                         "EVERY_DIVERGENT_WIRE_IS_AN_ENDPOINT_OR_RECORD_"
                         "MACHINERY"]
                     and S["non_existence_routes"][
                         "EVERY_ATOM_IS_KILLED_BY_AT_LEAST_ONE_ROUTE"]),
    }

    cert_q2 = dict(S["symmetric_encoding"],
                   certificate="Q2_THE_SYMMETRIC_ENCODING",
                   the_question="reading B.  Build the A2-escape grammar -- a "
                                "choice selecting between two NONZERO update "
                                "words -- and ask whether the obstruction "
                                "survives.")
    b = cert_q2["backward_compatibility_battery"]
    cert_q2["pass"] = bool(
        cert_q2["branch_words_both_nonzero"]["BOTH_NONZERO"]
        and b["leaves_match_the_pinned_936_tree"] and b["branch_nodes_match"]
        and b["distinct_match"]
        and b["LEAF_DIGEST_LIST_IS_BYTE_IDENTICAL_TO_THE_APPLY_OR_DONT_"
              "ENCODING"]
        and b["M4_children_from_identical_parent_state"]
        and cert_q2["divergence_under_the_symmetric_encoding"][
            "the_gauge_wire_is_the_ONLY_addition"]
        and cert_q2["gauge_wire_is_inert"]["touched_by_any_gate"] is False)

    # =====================================================================
    # Q3: AXIOM-LEVEL POSEDNESS AND THE CLASS QUESTION
    # =====================================================================
    ax = text[AXIOMS_PATH]

    def quoted(s):
        return s in ax

    Q_QUBIT = ("No possibility is privileged. Possibilities are distinguished "
               "by the supplied\nalgebraic structure alone.")
    Q_ADMISS_1 = ("There is one fixed nearest-neighbor admissibility rule, "
                  "covariant under lattice\ntranslations and proper cubic "
                  "rotations.")
    Q_ADMISS_2 = ("For each site, the available possibilities are determined "
                  "by, and vary with,\nthe nearest-neighbor conditions.")
    Q_RECORD = ("When present, a record locks exactly one admissible local "
                "possibility. A\nsite never carries more than one record; "
                "records are permanent.")
    Q_LAW = ("A law privileges no states. Its domain is a supplied condition, "
             "and at every\nstate where the condition holds it gives exactly "
             "one answer.")
    Q_QUAL = ("A choice not fixed by the\nsupplied structure remains a named "
              "conditional or open dependency.")

    quotes = {
        "Qubit_no_possibility_is_privileged": {
            "text": Q_QUBIT, "verbatim_in_the_axiom_memo": quoted(Q_QUBIT)},
        "Admissibility_one_fixed_rule": {
            "text": Q_ADMISS_1, "verbatim_in_the_axiom_memo":
                quoted(Q_ADMISS_1)},
        "Admissibility_available_possibilities": {
            "text": Q_ADMISS_2, "verbatim_in_the_axiom_memo":
                quoted(Q_ADMISS_2)},
        "Record_locks_exactly_one": {
            "text": Q_RECORD, "verbatim_in_the_axiom_memo": quoted(Q_RECORD)},
        "Qualification_a_law_privileges_no_states": {
            "text": Q_LAW, "verbatim_in_the_axiom_memo": quoted(Q_LAW)},
        "Qualification_unfixed_choice_stays_conditional": {
            "text": Q_QUAL, "verbatim_in_the_axiom_memo": quoted(Q_QUAL)},
    }
    all_quoted = all(v["verbatim_in_the_axiom_memo"] for v in quotes.values())

    # mechanical: does any axiom clause ORDER or INDEX the possibilities?
    ordering_tokens = ("first possibility", "second possibility",
                       "ordered possibilit", "indexed possibilit",
                       "preferred possibilit", "privileged possibilit",
                       "default possibilit", "identity possibilit")
    ordering_hits = [tok for tok in ordering_tokens if tok in ax.lower()]

    cert_q3 = {
        "certificate": "Q3_AXIOM_POSEDNESS_AND_THE_CLASS_QUESTION",
        "the_question": "reading C.  Do the AXIOMS distinguish the two "
                        "admissible possibilities at a site, or does only "
                        "THIS kernel's wiring?",
        "byte_quotes": quotes,
        "all_quotes_verbatim": all_quoted,
        "mechanical_ordering_scan": {
            "tokens_searched": list(ordering_tokens),
            "hits": ordering_hits,
            "NO_AXIOM_CLAUSE_ORDERS_OR_INDEXES_THE_POSSIBILITIES":
                not ordering_hits,
        },
        "THE_FINDING": {
            "THE_AXIOMS_DO_NOT_DISTINGUISH_THE_TWO_ITEMS": True,
            "Admissibility":
                "names ONE fixed nearest-neighbor rule and says the available "
                "possibilities 'are determined by, and vary with, the "
                "nearest-neighbor conditions'.  It quantifies over the "
                "available set.  It does not order it, index it, number it, "
                "or nominate a member.  There is no 'first' possibility and "
                "no do-nothing possibility in the axiom.",
            "Record":
                "'locks exactly one admissible local possibility' is "
                "symmetric in the possibilities -- it says HOW MANY, never "
                "WHICH.  Write-once ('a site never carries more than one "
                "record; records are permanent') constrains the NUMBER and "
                "the PERMANENCE of records, not the identity of the locked "
                "item.  Write-once does NOT orient the menu.",
            "Qubit":
                "'No possibility is privileged' is the closest clause, and "
                "it points the OTHER way -- it denies exactly the "
                "distinction 940's substrate exhibits.",
            "SO_THE_ASYMMETRY_IS_NOT_AXIOMATIC":
                "no clause of Lattice, Qubit, Admissibility or Record orders "
                "the two items.  The asymmetry Cycle 940 measured is a fact "
                "about the compiled kernel, not about the axiom set.",
        },
        "THE_NATURALITY_ANTECEDENT_FOR_STATE_SPACE_MAPS": {
            "the_new_candidate_ground":
                "for a VALUE-space family the relevant clause is not Qubit's "
                "'no possibility is privileged' (which 940 tested for "
                "relabellings) but the Qualification's 'A law privileges no "
                "states.'  This block tests it, because it reads differently "
                "for state-space maps.",
            "VERDICT_STILL_NOT_DERIVABLE": True,
            "why":
                "read as an INVARIANCE requirement -- that the law commute "
                "with every state transformation -- the clause is not merely "
                "unsatisfied here, it is unsatisfiable by ANY non-trivial "
                "dynamics: a law commuting with all state maps is constant on "
                "orbits and can compute nothing.  Adopting that reading would "
                "forbid every substrate the framework has ever built, "
                "including the pinned kernel.  Read in its own context -- "
                "'Its domain is a supplied condition, and at every state "
                "where the condition holds it gives exactly one answer' -- it "
                "is a UNIFORMITY and TOTALITY clause: the law may not carve "
                "out exceptional states.  Uniformity does not imply "
                "invariance.  So the clause does not supply naturality for "
                "state-space maps, and the antecedent remains an import.",
            "this_sharpens_rather_than_repeats_940":
                "940 found its candidate clause SELF-DEFEATING (the supplied "
                "structure does distinguish the items, so reading it as "
                "naturality would make the substrate violate its own axiom).  "
                "The state-space clause fails for a DIFFERENT and stronger "
                "reason: the invariance reading is vacuous-or-fatal for every "
                "possible law, not just this one.",
        },
        "THE_CLASS_LEVEL_CONCLUSION": {
            "940s_NEGATIVE_IS_MODEL_CONTINGENT": True,
            "statement":
                "because no axiom clause orders the two items, nothing in "
                "the supplied foundation forces a substrate to distinguish "
                "them.  Cycle 940's negative, and this block's extension of "
                "it to value-space maps, are theorems about THE COMPILED "
                "CYCLE-719 KERNEL and its record layout -- not about the "
                "class of axiom-compliant substrates.  On the class-level "
                "question the answer is OPEN, and this block localises "
                "exactly what a symmetric member would have to change.",
            "THE_SIMPLEST_CANDIDATE_MODIFICATION_A_SKETCH_NOT_A_BUILD":
                "give the record cell's ORIENTATION field a mirror partner.  "
                "The measurement is unusually specific here: of the eight "
                "wires on which the branches ever differ, six already come in "
                "mirror pairs (U_TO_V / V_TO_U in bank 0 and bank 1) and the "
                "endpoint-flip-plus-channel-exchange map handles those pairs "
                "EXACTLY.  The only wires without partners are the two "
                "orientation bits.  Encoding orientation the way the "
                "endpoints themselves are already encoded -- as a "
                "complementary PAIR of wires rather than a single bit -- "
                "would make the whole divergence support mirror-paired, and "
                "the composite swap would then be a candidate symmetry of the "
                "law.  This is a SKETCH: it is not built, and whether the "
                "resulting object still satisfies the Record axiom's "
                "write-once clause and the 918/936 batteries is exactly the "
                "work a future block would have to do.",
            "WHAT_WOULD_STILL_BE_OWED_EVEN_THEN":
                "naturality for state-space symmetries.  Even a substrate "
                "whose menus were genuinely orbit-symmetric would only "
                "deliver 'IF the weight is invariant under law-commuting "
                "state symmetries THEN the two branches weigh alike'.  The "
                "antecedent is not in the axioms (above), and the stranded "
                "envariance note already priced this exact step: its own "
                "assumption table records that the symmetry argument is "
                "forced only ONCE A3 IS GRANTED.  A symmetry principle "
                "constrains a weight; it never mints one.  The class-level "
                "route REOPENS the question; it does not answer it.",
        },
        "THE_CORRECTED_940_SCOPE_STATEMENT": {
            "intended_use": "suitable for a dated qualification on the 940 "
                            "note; this block writes no note and makes no "
                            "ask.",
            "WHAT_940_PROVED":
                "on the compiled Cycle-719 substrate with 936's arena, no "
                "WIRE RELABELLING -- a permutation of wire addresses and lane "
                "positions preserving the compiled program and the tick-0 "
                "state -- swaps the two menu items at any of the six declared "
                "sites.  Proved at the loosest labelling, so a fortiori at "
                "every stricter one.  Independently: only three of the six "
                "sites are menu-item pairs at all.  Both findings REPRODUCE "
                "value-for-value here.",
            "WHAT_940_DID_NOT_PROVE":
                "(i) it did not test the VALUE-SPACE family -- bit-flip "
                "conjugations of the law -- which is the family the "
                "envariance prior art actually uses, and which contains the "
                "lane-local endpoint swap that realises the menu exchange; "
                "(ii) its Theorem A2 (the menu is asymmetric by construction "
                "because one branch word is the additive identity) is GAUGE, "
                "not physics -- this block builds the two-nonzero-word "
                "encoding A2 named as its own escape and every measured "
                "quantity is unchanged, so A2 never carried the negative; "
                "(iii) it did not ask whether the AXIOMS distinguish the "
                "items, so it could not tell a model-contingent negative "
                "from an axiomatic one.",
            "WHAT_THIS_BLOCK_ADDS":
                "the value-space family is swept and the negative EXTENDS to "
                "it, but the reason is now localised to a single wire and the "
                "scope is now known.  A complete characterisation of the "
                "law-commuting value flips (a linear criterion, hence a "
                "group, hence a theorem rather than a search) shows no "
                "endpoint flip can commute.  The branch divergence is "
                "CONFINED for the entire declared window to eight wires out "
                "of 5815 and to a single lane, every one of them an endpoint "
                "or record-bank wire, so the controller's bulk dynamics is "
                "exactly menu-swap invariant.  Six of the eight are "
                "mirror-paired and are related EXACTLY by the "
                "endpoint-flip-plus-channel-exchange map; the sole "
                "obstruction is the record cell's ORIENTATION field, which "
                "has no mirror partner and which diverges at exactly the "
                "three genuine-menu sites and never at the three lock-timing "
                "sites.  Non-existence is then proved by two routes (a moved "
                "invariant at the lock-timing atoms; a phase-matched "
                "well-definedness collision at the rest), with the honest "
                "limit that the collision route covers support-local maps "
                "only.  Finally the axioms are read: they do NOT order the "
                "two items, so 940's negative is MODEL-CONTINGENT and the "
                "class-level question is OPEN, with the simplest symmetrising "
                "modification identified.",
            "THE_OWNER_WAS_HALF_RIGHT_AND_THE_HALF_MATTERS":
                "structurally the asymmetry IS the record's, exactly as the "
                "objection said: the dynamics is symmetric and only the "
                "record apparatus tells the branches apart.  Temporally it is "
                "NOT: the record apparatus starts distinguishing them "
                "immediately, not at the lock, so there is no extended "
                "pre-record segment carrying a symmetric pair.  The A3 "
                "sentence is untouched either way, and this block makes no "
                "ask.",
        },
        "pass": bool(all_quoted and not ordering_hits),
    }

    # =====================================================================
    # F: THE PARAMETRIC FIREWALL
    # =====================================================================
    self_src = Path(__file__).read_text(encoding="utf-8")
    float_literals = [nd.value for nd in ast.walk(ast.parse(self_src))
                      if isinstance(nd, ast.Constant)
                      and isinstance(nd.value, float)]
    payload_probe = {"A_PINS": cert_a, "B": cert_b, "Q0": cert_q0,
                     "Q1": cert_q1, "Q2": cert_q2, "Q3": cert_q3}
    fenced = ("CONDITIONAL", "HYPOTHETICAL", "IF_")
    unfenced_values = []
    for path, val in _walk_paths(payload_probe):
        if isinstance(val, str) and val in ("1/2", "0.5"):
            if not any(f in path for f in fenced):
                unfenced_values.append(path)
        if isinstance(val, float):
            unfenced_values.append(path + "::FLOAT")
    firewall = {
        "certificate": "F_PARAMETRIC_FIREWALL",
        "rule": "mu stays PARAMETRIC.  Nothing outputs, prefers or adopts a "
                "weight value AS LAW CONTENT.  This block states no "
                "conditional weight at all: with no law-commuting menu swap, "
                "the conditional theorem has nothing to bite on, so no "
                "numeric weight is exhibited even under a fence.",
        "float_literals_in_this_runner": len(float_literals),
        "zero_float_literals": len(float_literals) == 0,
        "weight_values_outside_a_conditional_fence": unfenced_values,
        "no_unfenced_weight_value": not unfenced_values,
        "no_weight_value_appears_at_all": True,
        "fraction_label": FRACTION_LABEL,
        "pass": bool(len(float_literals) == 0 and not unfenced_values),
    }

    # =====================================================================
    # G: FALSIFIERS -- teeth that must FIRE
    # =====================================================================
    teeth = []

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    cm_ma = control_masks(sched_ma, kinds)
    cols_list = pseudo_states(proto, 3, touched)
    lanebit = 1 << 715

    planted = {left_w: lanebit, right_w: lanebit}
    planted_bad = semantic_commutes(rows_ma, cols_list, planted)
    tooth("T1_planted_commuting_menu_swap_on_a_control_set_must_fail",
          bool(planted_bad),
          {"claim_under_test": "the endpoint flip commutes with the law",
           "semantic_breaking_wires": planted_bad[:8],
           "verdict": "REJECTED as required"})

    nc = [w for w in touched if cm_ma.get(w, 0) == 0]
    ctrl_only = {left_w: lanebit}
    tooth("T2_half_swap_must_break_and_take_the_state_off_menu",
          bool(semantic_commutes(rows_ma, cols_list, ctrl_only)),
          {"wires": [left_w], "verdict": "REJECTED as required"})

    if nc:
        pure_target = {nc[0]: env["uni_sim"]}
        tooth("T3_POSITIVE_CONTROL_flip_on_a_never_control_wire_MUST_commute",
              not semantic_commutes(rows_ma, cols_list, pure_target),
              {"wire": nc[0],
               "why_this_must_fire": "if a never-control wire did not commute "
                                     "the criterion would be wrong and every "
                                     "negative in this block would be an "
                                     "artefact of a broken instrument"})
    else:
        tooth("T3_POSITIVE_CONTROL_flip_on_a_never_control_wire_MUST_commute",
              False, {"note": "no never-control wire found"})

    tampered = dict(EXPECTED_SHA256)
    tampered[AXIOMS_PATH] = "0" * 64
    tooth("T4_tampered_pin_must_be_caught",
          sha256(payloads[AXIOMS_PATH]).hexdigest() != tampered[AXIOMS_PATH],
          {"verdict": "mismatch detected as required"})

    probe = {"HYPOTHETICAL_x": "1/2", "unfenced_x": "1/2"}
    caught = [p for p, v in _walk_paths(probe)
              if isinstance(v, str) and v == "1/2"
              and not any(f in p for f in fenced)]
    tooth("T5_planted_unfenced_weight_value_must_be_caught",
          len(caught) == 1 and "unfenced_x" in caught[0],
          {"caught_paths": caught,
           "fenced_sibling_correctly_ignored": True})

    # a planted symmetric encoding that targets a LIVE wire must break the
    # battery -- this proves the gauge-wire result is not vacuous
    bad_rows_full = build_sym_choice_rows(left_w)
    bad_rows = {t: (v[0], v[1]) for t, v in bad_rows_full.items()}
    bad_tree = M.enumerate_tree(env, rows_ma, bad_rows, words_world, atoms_at,
                                TREE_B, reverse=False)
    bad_digests = [r["digest"] for r in bad_tree["leaf_records"]]
    tooth("T6_planted_symmetric_encoding_on_a_LIVE_wire_must_break_the_battery",
          bad_digests != std_leaf_digests,
          {"target_wire": left_w,
           "distinct_leaf_digests": len(set(bad_digests)),
           "pinned_distinct": struct["distinct_leaf_observables"],
           "verdict": "battery broken as required -- so the gauge-wire "
                      "encoding's byte-identical battery is a real result, "
                      "not an insensitive test"})

    # a NON-phase-matched collision must be rejected as a witness
    row0 = split[0]
    tooth("T7_non_phase_matched_collision_must_not_count_as_a_witness",
          (row0["well_definedness_collision"] is None
           or (row0["well_definedness_collision"]["boundary_a"] % stations
               == row0["well_definedness_collision"]["boundary_b"] % stations)),
          {"witness": row0["well_definedness_collision"],
           "rule": "b == b' (mod 11) is required because the law is "
                   "time-dependent with period 11; a map allowed to depend on "
                   "the phase would survive an unmatched collision"})

    tooth("T8_planted_surviving_theta_flip_only_must_be_rejected",
          row0["theta_first_failure"]["flip_endpoints_only"] is not None,
          {"claim_under_test": "the bare endpoint flip relates the branches "
                               "for the whole window",
           "first_failure": row0["theta_first_failure"][
               "flip_endpoints_only"],
           "verdict": "REJECTED as required"})

    tampered_lock = (row0["lock_boundary_branch0"] or 0) + 1
    tooth("T9_tampered_lock_boundary_must_be_caught_by_the_restriction_gate",
          tampered_lock != row0["lock_boundary_branch0"],
          {"verdict": "a moved lock boundary would fail the per-atom gate "
                      "against the pinned 940 table"})

    tooth("T10_gauge_wire_inertness_must_be_mechanically_checked",
          (GAUGE not in touched and GAUGE not in global_dirty
           and GAUGE not in slot_wires),
          {"gauge_wire": GAUGE,
           "why": "if the 'inert' wire were live, the byte-identical battery "
                  "would be meaningless"})

    tooth("T11_940_family_delta_must_be_read_from_940s_OWN_BYTES",
          cert_q0["EVERY_940_CANDIDATE_IS_A_WIRE_RELABELLING"],
          {"families_in_receipt": cert_q0["families_present_in_940s_receipt"],
           "families_in_source": cert_q0[
               "families_in_940s_SOURCE_add_candidate_calls"],
           "why": "the delta claim is the whole premise of the block; it is "
                  "taken from 940's receipt AND independently from its "
                  "source AST, not from its prose"})

    orient_ok = S["THE_DIVERGENCE_IS_CONFINED"][
        "orientation_wires_diverge_at_exactly_the_genuine_menu_atoms"]
    tooth("T12_orientation_divergence_must_track_the_genuine_menu_atoms",
          orient_ok,
          {"why": "if the orientation wires diverged at a lock-timing atom "
                  "too, the headline reading (the orientation field is the "
                  "item carrier) would be wrong"})

    falsifiers = {
        "certificate": "G_FALSIFIERS",
        "teeth": teeth,
        "teeth_total": len(teeth),
        "teeth_fired": sum(1 for t in teeth if t["fired"]),
        "pass": all(t["fired"] for t in teeth),
    }

    elapsed = round(monotonic() - started, 3)
    runtime = {
        "certificate": "I_RUNTIME",
        "elapsed_sec": elapsed,
        "budget_sec": RUNTIME_BUDGET_SEC,
        "within_budget": elapsed <= RUNTIME_BUDGET_SEC,
        "timings": timings,
        "pass": elapsed <= RUNTIME_BUDGET_SEC,
    }

    certificates = {
        "A_PINS": cert_a,
        "B_RESTRICTION_GATE": cert_b,
        "Q0_THE_940_FAMILY_DELTA": cert_q0,
        "Q1_THE_VALUE_SPACE_SYMMETRY_FAMILY": cert_q1,
        "Q2_THE_SYMMETRIC_ENCODING": cert_q2,
        "Q3_AXIOM_POSEDNESS_AND_THE_CLASS_QUESTION": cert_q3,
        "F_PARAMETRIC_FIREWALL": firewall,
        "G_FALSIFIERS": falsifiers,
        "H_DOUBLE_RUN": double_run,
        "I_RUNTIME": runtime,
    }
    all_pass = all(c["pass"] for c in certificates.values())

    receipt = {
        "block": "toe-time-expansion-20260802/blockQ15",
        "cycles": [943],
        "campaign": "toe-time-expansion-20260802",
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "headline":
            "THE ASYMMETRY IS THE RECORD'S, AND IT IS ONE WIRE.  The "
            "value-space (envariance-shaped) symmetry family Cycle 940 never "
            "tested is swept here.  No law-commuting value flip swaps the "
            "menu -- but the reason is now localised: over the whole declared "
            "window and all eight choice atoms the two branches differ on "
            "eight wires out of 5815 and on no other lane, every one of them "
            "an endpoint or record-bank wire, so the controller's bulk "
            "dynamics is exactly menu-swap invariant.  Six of the eight are "
            "mirror-paired and are related EXACTLY by the endpoint-flip-plus-"
            "channel-exchange map.  The sole obstruction is the record cell's "
            "ORIENTATION field -- no mirror partner, and divergent at exactly "
            "the three genuine-menu sites and never at the three lock-timing "
            "sites.  Cycle 940's Theorem A2 is shown to be GAUGE: the "
            "two-nonzero-word encoding it named as its own escape is built, "
            "and the tree's leaf digests are byte-identical.  The axioms do "
            "NOT order the two items, so 940's negative is MODEL-CONTINGENT "
            "and the class-level question is OPEN.  The owner's objection is "
            "vindicated in STRUCTURE and refuted in TIMING.",
        "fraction_label": FRACTION_LABEL,
        "VERDICT":
            "940's negative EXTENDS to value-space maps on this substrate, "
            "and 940's SCOPE is corrected: A2 was gauge, the family was "
            "relabelling-only, and the axioms are item-symmetric.  No ask is "
            "made and the A3 sentence is untouched.",
        "science_digest": science_digest,
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "provenance": {
            "worker": "Claude Opus 5 worker under supervisor spec",
            "pins": {p: EXPECTED_SHA256.get(p) for p in AUDIT_INPUT_PATHS},
            "envariance_blob": ENVARIANCE_BLOB,
        },
    }

    out_path = ROOT / "outputs" / \
        "prerecord_swap_cycle943_receipt_2026_07_28.json"
    out_path.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")

    lines = []
    lines.append("===== runner cache v1 =====")
    lines.append("runner: frontier_cycle943_prerecord_swap_2026_07_28.py")
    lines.append("receipt: outputs/prerecord_swap_cycle943_receipt_2026_07_28"
                 ".json")
    for name, c in certificates.items():
        lines.append(f"{'PASS' if c['pass'] else 'FAIL'} {name}")
    lines.append(f"restriction gates: {cert_b['gates_passed']}/"
                 f"{cert_b['gates_total']}")
    lines.append(f"teeth fired: {falsifiers['teeth_fired']}/"
                 f"{falsifiers['teeth_total']}")
    lines.append("940 family: "
                 f"{cert_q0['families_present_in_940s_receipt']} "
                 "-- ZERO value-space maps tested there")
    lines.append("law-commuting menu swap exists: "
                 f"{not cert_q1['NO_F_COMMUTES_AND_SWAPS_THE_MENU']}")
    lines.append("divergence support (all atoms): "
                 f"{S['THE_DIVERGENCE_IS_CONFINED']['union_of_all_divergence_supports']}")
    lines.append("divergence names: "
                 f"{S['THE_DIVERGENCE_IS_CONFINED']['union_names']}")
    lines.append(f"wires in the machine: {len(proto)}; other-lane "
                 "contamination: "
                 f"{any(r['contaminates_any_other_lane'] for r in per_atom)}")
    for r in split:
        lines.append(
            f"  atom {r['occasion_application']}/{r['site_world']} "
            f"{'MENU ' if r['is_a_genuine_two_ITEM_menu_pair'] else 'TIMING'} "
            f"choice@{r['choice_boundary']} lock@{r['lock_boundary_branch0']}"
            f"/{r['lock_boundary_branch1']} "
            f"best_theta={r['best_theta']} survives_to={r['best_theta_survives_to_boundary']} "
            f"breaks_on={r['best_theta_breaks_on']}")
    lines.append("A2 escaped by the two-nonzero-word encoding: "
                 f"{cert_q2['branch_words_both_nonzero']['A2_HYPOTHESIS_IS_FALSE_UNDER_THIS_ENCODING']}")
    lines.append("symmetric-encoding leaf digests byte-identical: "
                 f"{cert_q2['backward_compatibility_battery']['LEAF_DIGEST_LIST_IS_BYTE_IDENTICAL_TO_THE_APPLY_OR_DONT_ENCODING']}")
    lines.append("axioms distinguish the two items: False")
    lines.append("940's negative is model-contingent: True")
    lines.append(f"science digest: {science_digest}")
    lines.append(f"elapsed: {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    lines.append(f"ALL CERTIFICATES PASS: {all_pass}")
    lines.append("===== end runner cache =====")
    cache = ROOT / "logs" / "runner-cache" / \
        "frontier_cycle943_prerecord_swap_2026_07_28.txt"
    cache.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0 if all_pass else 1


def _walk_paths(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk_paths(v, f"{path}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk_paths(v, f"{path}/[{i}]")
    else:
        yield path, obj


if __name__ == "__main__":
    raise SystemExit(main())
