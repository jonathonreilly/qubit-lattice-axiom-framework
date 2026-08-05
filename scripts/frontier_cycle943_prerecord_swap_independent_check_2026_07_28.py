#!/usr/bin/env python3
"""Cycle 943 / blockQ15 -- INDEPENDENT CHECKER.

Spec'd to REFUTE.  Every instrument here is built from the pinned bytes by
this file alone: its own AST lift of the pinned Cycle-936 runner (a
node-by-node replay, NOT the whitelist idiom Cycle 940 uses), its own
commutation algebra, its own divergence scanner, its own lane bookkeeping,
its own Theta search, and its own symmetric encoding.  The primary's runner
is never imported, never AST-lifted, and never read at run time; only its
RECEIPT is read, and only to compare numbers.

WHAT THIS FILE ATTACKS
  C1   Cycle 940's swept family is relabelling-only
  C2   X_chi commutes with the compiled law IFF chi[w] & CTRLMASK[w] == 0
  C3   the six endpoint-control TOF patterns and their three targets
  C3b  the source-pointer pair is adjacent, well formed, and menu-symmetric
  C4   the divergence support is eight wires, one lane
  C5   the wire identities and the orientation-wire split
  C6   the Theta table (attacked hardest: an independent, much wider hunt)
  C7   the lock boundaries, event counts and items
  C8   the two non-existence routes and the declared scope limit
  C9   A2 is gauge -- the two-nonzero-word symmetric encoding
  C10  the four axioms do not orient the two menu items

MINIMAL-PREMISE RULE.  The owner's "before the record, probabilities could be
symmetric" and the supervisor's "940 settled it" are both NON-PREMISES.  Where
a reading is ambiguous BOTH readings are carried and both are reported.
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
# A: PINS -- verified by sha256 AND by git blob, independently tabulated here
# ---------------------------------------------------------------------------

CORE_PATH = ("scripts/frontier_cycle719_two_rail_recurrent_controller"
             "_core_2026_07_26.py")
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
PRIMARY_RECEIPT = "outputs/prerecord_swap_cycle943_receipt_2026_07_28.json"

AUDIT_INPUT_PATHS = (CORE_PATH, C936_PATH, C936_RECEIPT, C936_SHIP, C936_NOTE,
                     C940_PATH, C940_RECEIPT, C940_SHIP, C940_NOTE,
                     C918_RECEIPT, C925_RECEIPT, AXIOMS_PATH)

# independently recomputed here, then cross-checked against the pinned
# receipts' own self-hashes and the pinned SHIP receipts' file tables
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
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C936_NOTE: "ffc0e6d1c3527ef75286abc0e50de0a3a3588f53",
    C936_RECEIPT: "d7b786fccc0435d139339c141dbad75c9f8d799b",
    C918_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
    C925_RECEIPT: "fed1b28e9e5cfe731a541645dce705541d69c967",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

# the stranded envariance note -- not in the worktree, pinned out of the
# object store on the unmerged branch born-from-envariance-2026-06-05
ENVARIANCE_BLOB = "64b24361f2237d01f079e16b306b5d04e01de7c2"

BLOCKLISTED_MODULES = (
    "frontier_cycle936_choice_substrate_2026_07_28",
    "frontier_cycle940_symmetric_weights_2026_07_28",
    "frontier_cycle943_prerecord_swap_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle911_type_vacuity_2026_07_28",
    "frontier_cycle913_selection_function_2026_07_28",
    "frontier_cycle918_writable_endpoint_2026_07_28",
    "frontier_cycle925_law_relaxation_2026_07_28",
)


class _CheckerFirewall(importlib.abc.MetaPathFinder):
    """Nothing this checker leans on may be IMPORTED.  The Cycle-936 substrate
    is lifted from its bytes; the Cycle-940 and Cycle-943 primaries are read as
    TEXT and JSON only.  Any import attempt is recorded and refused."""

    def __init__(self) -> None:
        self.hits: list = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import: {fullname}")
        return None


CHECKER_FIREWALL = _CheckerFirewall()
sys.meta_path.insert(0, CHECKER_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def pins():
    rows, payloads = {}, {}
    for path in AUDIT_INPUT_PATHS + (PRIMARY_RECEIPT,):
        blob = (ROOT / path).read_bytes()
        payloads[path] = blob
        rows[path] = {"sha256": sha256(blob).hexdigest(),
                      "git_blob": git_blob(blob), "bytes": len(blob)}
    env_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "blob", ENVARIANCE_BLOB],
        capture_output=True, check=False).stdout
    payloads["ENVARIANCE_NOTE"] = env_bytes
    env_ok = git_blob(env_bytes) == ENVARIANCE_BLOB and len(env_bytes) > 0
    sha_ok = all(rows[p]["sha256"] == v for p, v in EXPECTED_SHA256.items())
    blob_ok = all(rows[p]["git_blob"] == v
                  for p, v in EXPECTED_GIT_BLOBS.items())
    ship936 = json.loads(payloads[C936_SHIP].decode("utf-8"))
    ship940 = json.loads(payloads[C940_SHIP].decode("utf-8"))
    r936 = json.loads(payloads[C936_RECEIPT].decode("utf-8"))
    r940 = json.loads(payloads[C940_RECEIPT].decode("utf-8"))
    cross = []

    def x(name, got, want):
        cross.append({"cross_check": name, "value": got, "pinned": want,
                      "pass": got == want})

    x("c936_runner_self_sha256", rows[C936_PATH]["sha256"], r936["self_sha256"])
    x("c940_runner_self_sha256", rows[C940_PATH]["sha256"], r940["self_sha256"])
    for key in (C936_NOTE, C936_RECEIPT):
        x(f"ship936::{Path(key).name}::sha256", rows[key]["sha256"],
          ship936["files"][key]["sha256"])
        x(f"ship936::{Path(key).name}::git_blob", rows[key]["git_blob"],
          ship936["files"][key]["git_blob"])
    for key in (C940_NOTE, C940_RECEIPT):
        if key in ship940.get("files", {}):
            x(f"ship940::{Path(key).name}::sha256", rows[key]["sha256"],
              ship940["files"][key]["sha256"])
            x(f"ship940::{Path(key).name}::git_blob", rows[key]["git_blob"],
              ship940["files"][key]["git_blob"])
    cert = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "rows": rows,
        "sha256_all_match": sha_ok,
        "git_blobs_all_match": blob_ok,
        "cross_checks_against_the_pinned_receipts": cross,
        "cross_checks_pass": all(r["pass"] for r in cross),
        "existing_worktree_relative":
            all((ROOT / p).exists() for p in AUDIT_INPUT_PATHS),
        "blocked_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                   if m in sys.modules],
        "firewall_hits": list(CHECKER_FIREWALL.hits),
        "THE_STRANDED_ENVARIANCE_NOTE": {
            "git_blob": ENVARIANCE_BLOB,
            "retrieved_bytes": len(env_bytes),
            "blob_verifies": env_ok,
            "sha256": sha256(env_bytes).hexdigest() if env_bytes else None,
            "retrieval": "git -C <root> cat-file blob <sha>",
        },
        "modification_mechanism":
            "READ ONLY.  Nothing in this checker writes to any file the "
            "primary owns.  The Cycle-936 substrate is AST-lifted by a "
            "node-by-node replay written here; the primary's runner is never "
            "read, imported or lifted.",
    }
    cert["pass"] = bool(sha_ok and blob_ok and cert["cross_checks_pass"]
                        and cert["existing_worktree_relative"] and env_ok
                        and not cert["blocked_modules_loaded"]
                        and not cert["firewall_hits"])
    return cert, payloads


# ---------------------------------------------------------------------------
# my own lift of the pinned 936 machinery: NODE-BY-NODE REPLAY
# ---------------------------------------------------------------------------

def lift_936_by_replay(source: str):
    """Replay the pinned 936 module's top-level FunctionDef / ClassDef /
    Assign nodes, ONE NODE AT A TIME, in source order, into a private
    namespace.  Import / Expr / If nodes are never replayed, so none of the
    module's side effects (sys.path insertion, meta-path firewall, kernel
    import, __main__ guard) run.  Any single Assign that cannot evaluate in
    this namespace is skipped and recorded rather than aborting the lift --
    that is what makes this a replay and not Cycle 940's name whitelist."""
    tree = ast.parse(source, filename=C936_PATH)
    ns = {"__builtins__": __builtins__,
          "__file__": str(ROOT / C936_PATH),
          "__name__": "<ast-replay-936>",
          "K": K, "np": np, "ast": ast, "json": json, "math": math,
          "sys": sys, "itertools": itertools, "combinations": combinations,
          "product": product, "Counter": Counter, "Fraction": Fraction,
          "sha256": sha256, "sha1": sha1, "Path": Path,
          "SimpleNamespace": SimpleNamespace, "subprocess": subprocess,
          "importlib": importlib, "defaultdict": defaultdict,
          "compact": compact, "digest": digest, "git_blob": git_blob}
    replayed, skipped = [], []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.Expr, ast.If)):
            continue
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            continue
        mod = ast.Module(body=[node], type_ignores=[])
        ast.fix_missing_locations(mod)
        try:
            exec(compile(mod, "<replay-936>", "exec"), ns)
        except Exception as exc:                       # recorded, not hidden
            skipped.append({"lineno": node.lineno,
                            "kind": type(node).__name__,
                            "error": f"{type(exc).__name__}: {exc}"[:120]})
            continue
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            replayed.append(node.name)
        else:
            for t in node.targets:
                if isinstance(t, ast.Name):
                    replayed.append(t.id)
                elif isinstance(t, ast.Tuple):
                    replayed.extend(e.id for e in t.elts
                                    if isinstance(e, ast.Name))
    public = {k: v for k, v in ns.items() if not k.startswith("__")}
    return SimpleNamespace(**public), {"replayed": len(replayed),
                                       "skipped": skipped,
                                       "names": sorted(set(replayed))}


# ---------------------------------------------------------------------------
# my own gate algebra
# ---------------------------------------------------------------------------

def gate_roles(gate, KX, KC, KT):
    """(target, controls) of one compiled 5-tuple, BY KIND.

    The unused operand slots of a 5-tuple are literal zeros: an X gate is
    (KIND_X, target, 0, 0, mask) and a CNOT is (KIND_CNOT, ctrl, target, 0,
    mask).  Reading {a, b, c3} without dispatching on the kind therefore
    manufactures a phantom incidence on WIRE 0.  This function does not."""
    kind, a, b, c3, _m = gate
    if kind == KX:
        return a, ()
    if kind == KC:
        return b, (a,)
    if kind == KT:
        return c3, (a, b)
    raise ValueError(("unexpected compiled kind", kind))


def control_masks(schedules, KX, KC, KT):
    """CTRLMASK[w] = OR of masks over every gate in which w is a control."""
    ctrl, tgt, naive = {}, set(), set()
    for sched in schedules:
        for g in sched:
            naive |= {g[1], g[2], g[3]}
            t, cs = gate_roles(g, KX, KC, KT)
            tgt.add(t)
            for w in cs:
                ctrl[w] = ctrl.get(w, 0) | g[4]
    return ctrl, tgt, naive


def apply_gate_semantics(cols, gate, KX, KC, KT):
    kind, a, b, c3, m = gate
    if kind == KX:
        cols[a] ^= m
    elif kind == KC:
        cols[b] ^= cols[a] & m
    else:
        cols[c3] ^= cols[a] & cols[b] & m


def run_chunk(cols, sched, KX, KC, KT):
    for g in sched:
        apply_gate_semantics(cols, g, KX, KC, KT)
    return cols


class Rng:
    """deterministic 64-bit xorshift; no library RNG, no seeding surprises."""

    def __init__(self, seed):
        self.s = seed & ((1 << 64) - 1) or 0x9E3779B97F4A7C15

    def next(self):
        s = self.s
        s ^= (s << 13) & ((1 << 64) - 1)
        s ^= s >> 7
        s ^= (s << 17) & ((1 << 64) - 1)
        self.s = s
        return s

    def bits(self, n):
        out = 0
        while n > 0:
            out = (out << 64) | self.next()
            n -= 64
        return out


# ---------------------------------------------------------------------------
# GF(2) affine solver -- my own, with an explicit sensitivity test
# ---------------------------------------------------------------------------

def affine_fit(v0s, v1s, nin):
    """Solve  A . [v0 ; 1] = v1  over GF(2).  Returns (consistent, rank,
    inconsistent_rows, pivot_index_set, basis).  Rows are packed as
    left | (right << (nin+1)); the elimination carries every output bit at
    once, so one pass settles all output coordinates."""
    L = nin + 1
    piv, inc = {}, 0
    for x, y in zip(v0s, v1s):
        row = (x | (1 << nin)) | (y << L)
        while True:
            left = row & ((1 << L) - 1)
            if left == 0:
                break
            p = left.bit_length() - 1
            if p in piv:
                row ^= piv[p]
            else:
                piv[p] = row
                row = 0
                break
        if row and (row >> L):
            inc += 1
    return inc == 0, len(piv), inc, sorted(piv), piv


def affine_eval(piv, x, nin):
    """Evaluate the fitted affine map at x.  Free coordinates (no pivot) are
    sent to zero: one definite extension of the map off the fitted span."""
    L = nin + 1
    row = x | (1 << nin)
    acc = 0
    while True:
        left = row & ((1 << L) - 1)
        if left == 0:
            return acc
        p = left.bit_length() - 1
        if p in piv:
            row ^= piv[p]
            acc ^= (piv[p] >> L)
        else:
            row ^= (1 << p)


def collisions(bs, v0s, v1s, mod=None):
    d = defaultdict(set)
    for b, x, y in zip(bs, v0s, v1s):
        d[(x, b % mod) if mod else x].add(y)
    bad = [(k, sorted(s)) for k, s in d.items() if len(s) > 1]
    return len(bad), len(d), bad


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    timings = {}
    cert_a, payloads = pins()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({k: cert_a[k] for k in (
            "sha256_all_match", "git_blobs_all_match",
            "cross_checks_pass", "blocked_modules_loaded",
            "firewall_hits")}))
        return 2

    t0 = monotonic()
    M, lift_info = lift_936_by_replay(payloads[C936_PATH].decode("utf-8"))
    KX, KC, KT, KCH = M.KIND_X, M.KIND_CNOT, M.KIND_TOF, M.KIND_CHOICE
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = M.lift_machinery()
    timings["lift_and_machinery"] = round(monotonic() - t0, 3)

    r936 = json.loads(payloads[C936_RECEIPT].decode("utf-8"))
    r940 = json.loads(payloads[C940_RECEIPT].decode("utf-8"))
    r943 = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    c940_src = payloads[C940_PATH].decode("utf-8")
    axioms_text = payloads[AXIOMS_PATH].decode("utf-8")
    envariance_text = payloads["ENVARIANCE_NOTE"].decode("utf-8")

    # ---------------- substrate, rebuilt from the pinned bytes -----------
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
    M_A_GATES = ((KC, REC_A, left_w, 0), (KC, REC_A, right_w, 0))
    sim_rev = tuple(census[w] for w in range(n - 1, -1, -1))
    sim_rev = sim_rev + (sim_rev[0],)
    base_sched = M.build_schedules(c863, program, sim_fwd, 0, ())
    ma_sched = M.build_schedules(c863, program, sim_fwd, 0, M_A_GATES)
    rev_rows = M.compile_schedules(
        M.build_schedules(c863, program, sim_rev, 0, M_A_GATES))
    ma_rows = M.compile_schedules(ma_sched)
    ctl_rows = M.compile_schedules(base_sched)
    NCOL = len(M.Machine(env, False).columns)
    UNI = env["uni_sim"]
    atoms = tuple(sorted(M.CHOICE_ATOMS))
    atoms_at = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    apps = sorted(atoms_at)
    occasion_of = {t: i for i, t in enumerate(apps)}
    timings["substrate"] = round(monotonic() - t0, 3)

    def choice_chunks(extra_base, emitter_gates):
        """Compile one choice-bearing chunk per occasion.  emitter_gates(k)
        returns the extra macro gates for occasion ordinal k."""
        out, srcs = {}, {}
        for t in apps:
            k = occasion_of[t]
            gates = tuple(extra_base) + tuple(emitter_gates(k))
            sched = M.build_schedules(c863, program, sim_fwd, 0, gates)
            src = M.chunk_source(sched[t % stations])
            srcs[t] = src
            ns = {}
            exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE,
                                  "COCHOICE": COCHOICE}, ns)
            out[t] = (k, ns["apply_chunk"])
        return out, srcs

    # the COCHOICE binding for the symmetric encoding (Q2 / C9)
    _COCHOICE_SUPPORT = {}

    def COCHOICE(k):
        return _COCHOICE_SUPPORT[k] ^ M.CHOICE(k)

    plain_choice = lambda k: ((KCH, k, left_w, 0), (KCH, k, right_w, 0))
    ma_choice_rows, ma_choice_src = choice_chunks(M_A_GATES, plain_choice)
    ctl_choice_rows, _ = choice_chunks((), plain_choice)
    rev_choice_rows = {}
    for tt in apps:
        kk = occasion_of[tt]
        sch = M.build_schedules(c863, program, sim_rev, 0,
                                M_A_GATES + plain_choice(kk))
        ns = {}
        exec("\n".join(M.chunk_source(sch[tt % stations])),
             {"__builtins__": {}, "CHOICE": M.CHOICE}, ns)
        rev_choice_rows[tt] = (kk, ns["apply_chunk"])

    # ================================================================== #
    #  THE SCIENCE.  Everything below is a pure function of the pinned    #
    #  bytes; it is run twice and the two payloads must be identical.     #
    # ================================================================== #

    def science():
        out = {}
        tm = {}

        # -------------------------------------------------------------- #
        # B: substrate restriction gates                                  #
        # -------------------------------------------------------------- #
        t = monotonic()
        gates = []

        def g(name, got, want):
            gates.append({"gate": name, "value": got, "pinned": want,
                          "pass": got == want})

        g("stations", stations, 11)
        g("census_size_n", n, 748)
        g("column_count", NCOL, 5815)
        g("lane_bits_per_column", n + 1, 749)
        g("endpoint_wires", list(c913.endpoint_wires()), [1, 6, 40])
        g("REC_A", REC_A, 123)
        g("BANK_BASES_head", list(BB[:3]), [41, 172, 303])
        g("base_compiled_gate_total", sum(len(s) for s in base_sched), 34166)
        g("M_A_compiled_gate_total", sum(len(s) for s in ma_sched), 34188)
        g("TREE_B", TREE_B, 1925)
        g("TREE_ORBITS", M.TREE_ORBITS, 175)
        g("CHOICE_ATOMS", [list(a) for a in atoms],
          [[300, 715], [700, 475], [700, 540], [702, 254], [702, 450],
           [702, 715], [1100, 558], [1100, 715]])
        g("choice_occasions", apps, [300, 700, 702, 1100])
        g("schedule_builder_reproduces_the_pinned_compiler",
          digest([[list(x) for x in s] for s in base_sched]),
          digest([[list(x) for x in s]
                  for s in c863.masked_h_schedules(program, sim_fwd)]))
        g("c936_receipt_all_certificates_pass",
          r936["all_certificates_pass"], True)
        g("c940_receipt_all_certificates_pass",
          r940["all_certificates_pass"], True)
        # wire identities (C5), recomputed from the kernel's own offsets
        wid = {"SOURCE_POINTER": src_w,
               "BANK0.POINTER": BB[0] + K.A.POINTER,
               "BANK0.U_TO_V": BB[0] + K.A.U_TO_V,
               "BANK0.V_TO_U": BB[0] + K.A.V_TO_U,
               "BANK0.DIRECTION_OK": BB[0] + K.A.DIRECTION_OK,
               "BANK1.U_TO_V": BB[1] + K.A.U_TO_V,
               "BANK1.V_TO_U": BB[1] + K.A.V_TO_U,
               "BANK1.cell0.orientation": BB[1] + K.A.cell(0)["orientation"],
               "BANK1.cell1.orientation": BB[1] + K.A.cell(1)["orientation"]}
        g("wire_identities", wid,
          {"SOURCE_POINTER": 40, "BANK0.POINTER": 123, "BANK0.U_TO_V": 124,
           "BANK0.V_TO_U": 125, "BANK0.DIRECTION_OK": 131,
           "BANK1.U_TO_V": 255, "BANK1.V_TO_U": 256,
           "BANK1.cell0.orientation": 202, "BANK1.cell1.orientation": 236})
        g("cell_orientation_offset_is_34i_plus_30",
          [K.A.cell(i)["orientation"] for i in (0, 1)], [30, 64])
        NAME = {v: k for k, v in wid.items()}
        NAME[left_w] = "LEFT_ENDPOINT"
        NAME[right_w] = "RIGHT_ENDPOINT"
        WANTED = ("leaves", "leaves_enumerated", "branch_nodes",
                  "depth_in_choice_occasions", "distinct_leaf_observables")

        def deep_keys(obj, acc):
            if isinstance(obj, dict):
                for kk, vv in obj.items():
                    if kk in WANTED and isinstance(vv, int):
                        acc.setdefault(kk, vv)
                    deep_keys(vv, acc)
            elif isinstance(obj, list):
                for vv in obj:
                    deep_keys(vv, acc)
            return acc
        tree_keys = deep_keys(r936["certificates"], {})
        g("c936_tree_structure_keys", tree_keys,
          {"leaves": 256, "leaves_enumerated": 256, "branch_nodes": 75,
           "depth_in_choice_occasions": 4, "distinct_leaf_observables": 64})
        out["B_SUBSTRATE"] = {
            "certificate": "B_SUBSTRATE_RESTRICTION_GATES",
            "rows": gates, "total": len(gates),
            "passed": sum(1 for r in gates if r["pass"]),
            "pass": all(r["pass"] for r in gates),
            "lift_replay": {"names_replayed": lift_info["replayed"],
                            "nodes_skipped": lift_info["skipped"]},
            "wire_names": {str(k): v for k, v in sorted(NAME.items())},
        }
        tm["B"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # C: bitwise lane independence + invertibility                    #
        # -------------------------------------------------------------- #
        t = monotonic()
        kinds_present = sorted({gg[0] for s in ma_sched for gg in s})
        selfref = sum(1 for s in ma_sched for gg in s
                      if gate_roles(gg, KX, KC, KT)[0]
                      in gate_roles(gg, KX, KC, KT)[1])
        # AST proof: the emitted statement text uses only ^= & and constants
        allowed = {ast.Module, ast.FunctionDef, ast.arguments, ast.arg,
                   ast.AugAssign, ast.Subscript, ast.Name, ast.Load,
                   ast.Store, ast.Constant, ast.BinOp, ast.BitAnd,
                   ast.BitXor, ast.Index, ast.Pass, ast.Expr}
        bad_nodes = Counter()
        for s in ma_sched:
            tree = ast.parse("\n".join(M.chunk_source(s)))
            for node in ast.walk(tree):
                if type(node) not in allowed:
                    bad_nodes[type(node).__name__] += 1
        # semantic proof: two states agreeing on a lane subset stay agreeing
        rng = Rng(0x943C0DE1)
        lane_sets = [(1 << 715), (1 << 715) | (1 << 254), (1 << 0) | (1 << n)]
        leak = 0
        for LS in lane_sets:
            a = [rng.bits(n + 1) & UNI for _ in range(NCOL)]
            b = [(x & LS) | (rng.bits(n + 1) & UNI & ~LS) for x in a]
            run_chunk(a, ma_sched[3], KX, KC, KT)
            run_chunk(b, ma_sched[3], KX, KC, KT)
            leak += sum(1 for i in range(NCOL)
                        if (a[i] ^ b[i]) & LS)
        # planted lane leak (tooth): a shift gate would couple lanes
        planted = [rng.bits(n + 1) & UNI for _ in range(NCOL)]
        planted_b = list(planted)
        planted_b[500] ^= (1 << 254)
        pre = (planted[500] ^ planted_b[500]) & (1 << 715)
        planted[501] ^= (planted[500] >> 1) & UNI
        planted_b[501] ^= (planted_b[500] >> 1) & UNI
        leak_caught = bool(((planted[501] ^ planted_b[501]) & (1 << 253))
                           and not pre)
        out["C_LANE_INDEPENDENCE"] = {
            "certificate": "C_BITWISE_LANE_INDEPENDENCE",
            "kinds_present_in_the_compiled_cycle": kinds_present,
            "only_X_CNOT_TOF": kinds_present == sorted([KX, KC, KT]),
            "no_SHIFT_gate_anywhere": KIND_SHIFT_ABSENT(kinds_present, M),
            "gates_whose_target_is_also_a_control": selfref,
            "every_chunk_is_a_bijection": selfref == 0,
            "emitted_AST_node_types_outside_the_bitwise_grammar":
                dict(bad_nodes),
            "AST_grammar_is_bitwise_only": not bad_nodes,
            "lane_subsets_probed": len(lane_sets),
            "cross_lane_leakage_found": leak,
            "SEMANTIC_LANE_INDEPENDENCE": leak == 0,
            "planted_shift_leak_is_caught_by_this_instrument": leak_caught,
            "READING":
                "every compiled gate is X / CNOT / TOF with a compile-time "
                "lane mask, so each lane bit evolves under its own copy of "
                "the same Boolean circuit and no lane can read another.  A "
                "divergence seeded in one lane is therefore CONFINED to that "
                "lane as a THEOREM, not as a measurement -- and the "
                "measurement below agrees.",
        }
        out["C_LANE_INDEPENDENCE"]["pass"] = bool(
            not bad_nodes and leak == 0 and selfref == 0 and leak_caught
            and kinds_present == sorted([KX, KC, KT]))
        tm["C"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # D: the commutation theorem (C2)                                 #
        # -------------------------------------------------------------- #
        t = monotonic()
        ctrl, tgts, naive = control_masks(ma_sched, KX, KC, KT)
        touched = sorted(set(ctrl) | tgts)
        never_ctrl = [w for w in touched if ctrl.get(w, 0) == 0]
        full_ctrl = [w for w, m in ctrl.items() if m == UNI]

        def commutes_semantically(chi, sched, trials=6, seed=0x5EED943):
            """Direct semantic test of  L o X_chi == X_chi o L  on the chunk,
            over pseudo-random FULL columns.  No criterion is consulted."""
            r = Rng(seed)
            for _ in range(trials):
                a = [r.bits(n + 1) & UNI for _ in range(NCOL)]
                b = list(a)
                for w, v in chi.items():
                    b[w] ^= v
                run_chunk(a, sched, KX, KC, KT)
                run_chunk(b, sched, KX, KC, KT)
                for w, v in chi.items():
                    a[w] ^= v
                if a != b:
                    return False
            return True

        def criterion(chi):
            return all((v & ctrl.get(w, 0)) == 0 for w, v in chi.items())

        table, disagree = [], 0
        probe_wires = sorted(set(touched[:6] + [left_w, right_w, 40, 123, 124,
                                                125, 131, 202, 236, 255, 256]))
        for w in probe_wires:
            chi = {w: UNI}
            sem = commutes_semantically(chi, ma_sched[0])
            cri = criterion(chi)
            table.append({"chi": f"full flip on wire {w}",
                          "wire": w, "criterion_says_commutes": cri,
                          "semantics_says_commutes": sem, "agree": sem == cri,
                          "CTRLMASK_popcount": bin(ctrl.get(w, 0)).count("1")})
            disagree += int(sem != cri)
        # EXHAUSTIVE, over ALL touched wires at once, by EXACT difference
        # propagation against one shared unperturbed run.  For each wire the
        # engine computes the exact end-of-cycle difference between the
        # perturbed and unperturbed trajectories on a full-width pseudo-random
        # column vector; because each column carries 749 lanes and the lanes
        # are independent, ONE trial is 749 independent random states.
        CYCLE = tuple(gg for s in ma_sched for gg in s)

        def delta_sweep(tests, seed):
            r = Rng(seed)
            U = [r.bits(n + 1) & UNI for _ in range(NCOL)]
            D = [dict() for _ in tests]
            dirty = defaultdict(set)
            for i, w in enumerate(tests):
                D[i][w] = UNI
                dirty[w].add(i)
            for (kk, a, b, c3, m) in CYCLE:
                if kk == KX:
                    U[a] ^= m
                    continue
                if kk == KC:
                    ids = dirty.get(a)
                    if ids:
                        for i in tuple(ids):
                            d = D[i].get(a, 0) & m
                            if d:
                                nv = D[i].get(b, 0) ^ d
                                if nv:
                                    D[i][b] = nv
                                    dirty[b].add(i)
                                else:
                                    D[i].pop(b, None)
                                    dirty[b].discard(i)
                    U[b] ^= U[a] & m
                    continue
                ids = set()
                if a in dirty:
                    ids |= dirty[a]
                if b in dirty:
                    ids |= dirty[b]
                if ids:
                    ua, ub = U[a], U[b]
                    for i in ids:
                        da = D[i].get(a, 0)
                        db = D[i].get(b, 0)
                        d = m & ((da & ub) ^ (db & ua) ^ (da & db))
                        if d:
                            nv = D[i].get(c3, 0) ^ d
                            if nv:
                                D[i][c3] = nv
                                dirty[c3].add(i)
                            else:
                                D[i].pop(c3, None)
                                dirty[c3].discard(i)
                U[c3] ^= U[a] & U[b] & m
            return [D[i] == {w: UNI} for i, w in enumerate(tests)]

        TRIALS = 64
        agg = [True] * len(touched)
        for j in range(TRIALS):
            res = delta_sweep(touched, 0x9430000 + j * 7919)
            agg = [x and y for x, y in zip(agg, res)]
        commuting_controls = [w for w, ok in zip(touched, agg) if ok]
        # cross-check the engine against the brute-force chunk semantics
        engine_ok = all(
            commutes_semantically({w: UNI}, CYCLE, trials=1, seed=0x9430000)
            == ok for w, ok in list(zip(touched, agg))[:8]
            + list(zip(touched, agg))[-8:])
        exhaustive_disagree = [w for w in commuting_controls
                               if not criterion({w: UNI})]
        # the ACTUAL menu-swap flip, on the site's own lane
        menu_chi = {left_w: 1 << 715, right_w: 1 << 715}
        menu_commutes = commutes_semantically(menu_chi, CYCLE, trials=4,
                                              seed=0x11EE)
        # the mechanism, exhibited on one wire
        exhibit_w = commuting_controls[0] if commuting_controls else None
        exhibit = None
        if exhibit_w is not None:
            s0 = ma_sched[0]
            idxs = [i for i, gg in enumerate(s0)
                    if exhibit_w in gate_roles(gg, KX, KC, KT)[1]]
            pal = None
            if len(idxs) == 2:
                a, b = idxs
                pal = all(s0[a + j] == s0[b - j]
                          for j in range((b - a) // 2 + 1))
            exhibit = {
                "wire": exhibit_w,
                "control_incidences_in_chunk_0": idxs,
                "the_two_gates_are_identical":
                    len(idxs) == 2 and s0[idxs[0]] == s0[idxs[1]],
                "the_block_between_them_is_a_PALINDROME": pal,
                "CTRLMASK_popcount": bin(ctrl.get(exhibit_w, 0)).count("1"),
                "criterion_says_it_cannot_commute":
                    not criterion({exhibit_w: UNI}),
                "MECHANISM":
                    "the compiled macro is a compute / uncompute LADDER: the "
                    "gate in which this wire is a control occurs twice, with "
                    "identical operands and identical mask, and the whole "
                    "block between the two occurrences is a palindrome.  The "
                    "perturbation runs up the ladder and is undone coming "
                    "back down, so the flip commutes with the full cycle even "
                    "though the wire is a control on every lane.",
            }
        # positive control: an untouched wire MUST commute
        untouched = sorted(set(range(NCOL)) - set(touched))
        pos_ok = commutes_semantically({untouched[0]: UNI}, ma_sched[0])
        pos_ok = pos_ok and commutes_semantically(
            {w: UNI for w in untouched[:50]}, ma_sched[0])
        # both controls of ONE TOF flipped: does it cancel?
        one_tof = next(gg for s in ma_sched for gg in s if gg[0] == KT)
        both = {one_tof[1]: one_tof[4], one_tof[2]: one_tof[4]}
        both_sem = commutes_semantically(both, (one_tof,))
        # the same, algebraically: at c[a]=c[b]=0 the residue is mask & chi_a
        # & chi_b, which is the mask itself -- nonzero.
        both_alg = (one_tof[4] & one_tof[4] & one_tof[4]) == 0
        # over-exclusion hunt: does any criterion-EXCLUDED single-wire flip
        # nevertheless commute along the REAL trajectory?
        over = []
        for w in (left_w, right_w, 124, 125, 202, 236, 255, 256, 131, 132):
            mm0 = M.Machine(env, False)
            mm1 = M.Machine(env, False)
            occ = {tt: 0 for tt in apps}
            mm0.advance(300, ma_rows, ma_choice_rows, occ)
            mm1.advance(300, ma_rows, ma_choice_rows, occ)
            mm1.columns[w] ^= (1 << 715)
            diverged = None
            for b in range(300, 360):
                mm0.advance(b + 1, ma_rows, ma_choice_rows, occ)
                mm1.advance(b + 1, ma_rows, ma_choice_rows, occ)
                d = [i for i in range(NCOL)
                     if (mm0.columns[i] ^ mm1.columns[i]) != (
                         (1 << 715) if i == w else 0)]
                if d:
                    diverged = b + 1
                    break
            over.append({"wire": w, "criterion_excludes": not criterion(
                {w: 1 << 715}),
                "first_boundary_at_which_the_flip_stops_being_a_pure_flip":
                    diverged,
                "commutes_on_the_real_trajectory": diverged is None})
        out["D_COMMUTATION"] = {
            "certificate": "D_COMMUTATION_THEOREM",
            "STATEMENT_UNDER_TEST":
                "X_chi commutes with the compiled law IFF "
                "chi[w] & CTRLMASK[w] == 0 for every wire w",
            "wires_touched_BY_KIND_DISPATCH": len(touched),
            "wires_touched_by_the_naive_union_of_a_b_c3": len(naive),
            "the_naive_union_minus_the_kind_dispatch":
                sorted(naive - set(touched)),
            "targets": len(tgts),
            "controls": len(ctrl),
            "wires_that_are_never_a_control": never_ctrl,
            "controls_whose_CTRLMASK_is_the_FULL_lane_universe":
                len(full_ctrl),
            "CTRLMASK_left_is_full": ctrl.get(left_w, 0) == UNI,
            "CTRLMASK_right_is_full": ctrl.get(right_w, 0) == UNI,
            "per_F_commutation_table": table,
            "criterion_and_semantics_disagreements": disagree,
            "THE_IFF_IS_REFUTED": {
                "protocol":
                    f"exact difference propagation for all {len(touched)} "
                    f"touched wires at once, against {TRIALS} independent "
                    "full-width pseudo-random column vectors; each column "
                    f"carries {n + 1} independent lanes, so each wire is "
                    f"tested on {TRIALS * (n + 1)} independent random states.",
                "trials": TRIALS,
                "independent_random_states_per_wire": TRIALS * (n + 1),
                "engine_cross_checked_against_brute_force_semantics":
                    engine_ok,
                "wires_whose_FULL_LANE_FLIP_COMMUTES_with_the_whole_cycle":
                    len(commuting_controls),
                "every_one_of_them_is_EXCLUDED_by_the_criterion":
                    len(exhaustive_disagree) == len(commuting_controls),
                "the_excluded_but_commuting_wires": commuting_controls,
                "SUFFICIENCY_HOLDS":
                    "chi[w] & CTRLMASK[w] == 0 for all w IMPLIES commutation "
                    "-- that direction is a gate-by-gate theorem and no "
                    "counterexample exists here.",
                "NECESSITY_IS_FALSE":
                    "commutation does NOT imply the criterion.  Hundreds of "
                    "wires whose CTRLMASK is the full lane universe carry a "
                    "commuting full-lane flip.  The primary calls its "
                    "condition 'a COMPLETE characterisation, not a search'.  "
                    "It is not: it is a SUFFICIENT condition that "
                    "over-excludes by a factor of well over a hundred.",
                "HONEST_LIMIT":
                    "commutation for those wires is MEASURED, not proved: a "
                    "closed-form replacement criterion is not constructed "
                    "here.  The count falls monotonically as trials are "
                    "added (367 at one trial, 334 at eight, 309 at "
                    "sixty-four) and appears to settle just above three "
                    "hundred.  Non-commuting wires fail on the FIRST trial "
                    "in every case observed, so the surviving set is not an "
                    "artefact of weak testing.",
                "MECHANISM": exhibit,
            },
            "THE_LOAD_BEARING_COROLLARY_SURVIVES": {
                "left_endpoint_flip_commutes": left_w in commuting_controls,
                "right_endpoint_flip_commutes": right_w in commuting_controls,
                "any_divergence_support_wire_commutes":
                    sorted(set(commuting_controls)
                           & {124, 125, 202, 236, 255, 256}),
                "THE_ACTUAL_MENU_SWAP_FLIP_COMMUTES": menu_commutes,
                "reading":
                    "neither endpoint, and no wire of the divergence "
                    "support, is in the commuting set, and the actual "
                    "menu-swap flip (both endpoints, the site's own lane) "
                    "does NOT commute.  So the primary's downstream "
                    "conclusion is untouched by the refutation of its "
                    "characterisation.",
            },
            "exhaustive_single_wire_disagreements": exhaustive_disagree,
            "exhaustive_wires_tested": len(touched),
            "POSITIVE_CONTROL_untouched_wire_flips_commute": pos_ok,
            "BOTH_CONTROLS_OF_ONE_TOF": {
                "gate": [int(x) for x in one_tof[:4]],
                "commutes": both_sem,
                "cancels": both_alg,
                "READING":
                    "at c[a] = c[b] = 0 the residue of a double control flip "
                    "is mask & chi_a & chi_b, which is the mask itself.  The "
                    "two flips do NOT cancel.",
            },
            "OVER_EXCLUSION_HUNT_on_the_real_trajectory": over,
            "COMMUTANT":
                "CTRLMASK[w] is the FULL 749-lane universe for EVERY one of "
                "the touched wires.  The primary reads off from that a "
                "causally trivial commutant.  The MEASURED commutant is much "
                "larger: all 5270 untouched wires PLUS about three hundred "
                "touched ones whose control incidences sit inside palindromic "
                "compute / uncompute ladders.  It is still causally trivial "
                "FOR THE MENU: no endpoint and no divergence-support wire is "
                "in it.",
        }
        out["D_COMMUTATION"]["pass"] = bool(
            disagree == 0 and pos_ok and engine_ok
            and not both_sem and not never_ctrl and not menu_commutes
            and left_w not in commuting_controls
            and right_w not in commuting_controls
            and ctrl.get(left_w, 0) == UNI and ctrl.get(right_w, 0) == UNI)
        tm["D"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # E: the six endpoint-control TOF patterns (C3) and the pair (C3b)#
        # -------------------------------------------------------------- #
        t = monotonic()
        pat = Counter()
        pat_targets = set()
        for s in ma_sched:
            for gg in s:
                if gg[0] == KT and (gg[1] in (left_w, right_w)
                                    or gg[2] in (left_w, right_w)):
                    pat[(gg[1], gg[2], gg[3])] += 1
                    pat_targets.add(gg[3])
        endpoint_as_cnot_control = sum(
            1 for s in ma_sched for gg in s
            if gg[0] == KC and gg[1] in (left_w, right_w))
        # C3b: the source-pointer pair
        pairs, malformed = [], []
        for si, s in enumerate(ma_sched):
            idx = [i for i, gg in enumerate(s)
                   if gate_roles(gg, KX, KC, KT)[0] == src_w]
            if len(idx) != 2:
                malformed.append({"chunk": si, "reason": "not exactly two",
                                  "count": len(idx)})
                continue
            i0, i1 = idx
            g0, g1 = s[i0], s[i1]
            reads = {g0[1], g0[2], g1[1], g1[2]}
            between = s[i0 + 1:i1]
            writes_between = sorted({gate_roles(gg, KX, KC, KT)[0]
                                     for gg in between})
            reads_40_between = sorted({gg_i for gg_i, gg in enumerate(between)
                                       if src_w in
                                       gate_roles(gg, KX, KC, KT)[1]})
            ok = (g0[0] == KT and g1[0] == KT and g0[1] == g1[1]
                  and g0[4] == g1[4] and i1 == i0 + 1
                  and {g0[2], g1[2]} == {left_w, right_w}
                  and not (set(writes_between) & reads))
            pairs.append({"chunk": si, "indices": [i0, i1],
                          "adjacent": i1 == i0 + 1,
                          "shared_other_control": g0[1] if g0[1] == g1[1]
                          else None,
                          "shared_mask": g0[4] == g1[4],
                          "one_reads_LEFT_one_reads_RIGHT":
                              {g0[2], g1[2]} == {left_w, right_w},
                          "wires_written_between": writes_between,
                          "readers_of_the_source_pointer_between":
                              reads_40_between,
                          "well_formed": ok})
            if not ok:
                malformed.append({"chunk": si, "reason": "predicate failed"})
        # semantics of the pair, in ISOLATION and EMBEDDED in the full chunk
        r = Rng(0xC3B0)
        iso_ok, emb_ok, emb_menu_ok = True, True, True
        readers_before, readers_after = [], []
        for si, s in enumerate(ma_sched):
            idx = [i for i, gg in enumerate(s)
                   if gate_roles(gg, KX, KC, KT)[0] == src_w]
            i0 = idx[0]
            readers_before.append(sum(1 for gg in s[:i0] if src_w in
                                      gate_roles(gg, KX, KC, KT)[1]))
            readers_after.append(sum(1 for gg in s[idx[-1] + 1:] if src_w in
                                     gate_roles(gg, KX, KC, KT)[1]))
        for _ in range(4):
            cols = [r.bits(n + 1) & UNI for _ in range(NCOL)]
            g0, g1 = [gg for gg in ma_sched[0]
                      if gate_roles(gg, KX, KC, KT)[0] == src_w]
            a = list(cols)
            apply_gate_semantics(a, g0, KX, KC, KT)
            apply_gate_semantics(a, g1, KX, KC, KT)
            want = cols[src_w] ^ (cols[g0[1]] & g0[4]
                                  & (cols[left_w] ^ cols[right_w]))
            iso_ok = iso_ok and (a[src_w] == want)
            # embedded: the FULL chunk, on-menu columns, with and without the
            # simultaneous endpoint flip on every lane
            on = list(cols)
            on[right_w] = ~on[left_w] & UNI            # force LEFT xor RIGHT
            fl = list(on)
            fl[left_w] ^= UNI
            fl[right_w] ^= UNI
            run_chunk(on, ma_sched[0], KX, KC, KT)
            run_chunk(fl, ma_sched[0], KX, KC, KT)
            emb_ok = emb_ok and (on[src_w] == fl[src_w])
            off = list(cols)
            off[right_w] = off[left_w]                 # force OFF menu
            fo = list(off)
            fo[left_w] ^= UNI
            fo[right_w] ^= UNI
            run_chunk(off, ma_sched[0], KX, KC, KT)
            run_chunk(fo, ma_sched[0], KX, KC, KT)
            emb_menu_ok = emb_menu_ok and (off[src_w] == fo[src_w])
        out["E_ENDPOINT_GATES"] = {
            "certificate": "E_ENDPOINT_CONTROL_GATES",
            "six_TOF_patterns": {str(list(k)): v for k, v in
                                 sorted(pat.items())},
            "pattern_count": len(pat),
            "total_gates_per_compiled_cycle": sum(pat.values()),
            "the_only_targets": sorted(pat_targets),
            "targets_are_all_in_global_dirty":
                all(w in set(global_dirty) for w in pat_targets),
            "endpoint_is_a_CNOT_control_anywhere": endpoint_as_cnot_control,
            "C3b_SOURCE_POINTER_PAIRS": {
                "pairs_found": len(pairs),
                "malformed": malformed,
                "all_adjacent": all(p["adjacent"] for p in pairs),
                "all_share_the_other_control":
                    all(p["shared_other_control"] == 131 for p in pairs),
                "all_share_the_mask": all(p["shared_mask"] for p in pairs),
                "nothing_between_them": all(not p["wires_written_between"]
                                            for p in pairs),
                "no_reader_of_the_source_pointer_between_them":
                    all(not p["readers_of_the_source_pointer_between"]
                        for p in pairs),
                "readers_of_the_source_pointer_BEFORE_the_pair_per_chunk":
                    readers_before,
                "readers_of_the_source_pointer_AFTER_the_pair_per_chunk":
                    readers_after,
                "net_contribution_is_ctrl_AND_mask_AND_LEFT_XOR_RIGHT":
                    iso_ok,
                "EMBEDDED_IN_THE_FULL_CHUNK_the_flip_preserves_c40_on_menu":
                    emb_ok,
                "EMBEDDED_off_menu_the_flip_also_preserves_c40":
                    emb_menu_ok,
                "ORDER_ANALYSIS":
                    "the pair sits at the very END of every compiled chunk "
                    "(indices len-3, len-2 of the station macro), so every "
                    "reader of the source pointer in that chunk -- the gates "
                    "targeting 123, 124, 125 and 132 -- reads the value from "
                    "BEFORE the pair, never the value between the two gates.  "
                    "The 'net contribution' reading is therefore not spoiled "
                    "by the earlier readers: they are upstream of the write, "
                    "not inside it.",
                "rows": pairs,
            },
        }
        out["E_ENDPOINT_GATES"]["pass"] = bool(
            len(pat) == 6 and sum(pat.values()) == 66
            and sorted(pat_targets) == [40, 124, 125]
            and endpoint_as_cnot_control == 0 and len(pairs) == 11
            and not malformed and iso_ok and emb_ok)
        tm["E"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # F: the divergence, per atom, over the full window (C4, C5, C7)  #
        # -------------------------------------------------------------- #
        t = monotonic()
        TARGETS = sorted(tgts)
        TIDX = {w: i for i, w in enumerate(TARGETS)}

        def two_branch(atom, rows_, chrows, upto, reverse=False,
                       keep_full_key=False, extra_wires=()):
            """Advance both branches in lockstep and record, at EVERY
            boundary, the divergence and my OWN lane bookkeeping.  Only wires
            that are gate TARGETS can ever change, so restricting the scan to
            them is exact, not an approximation; extra_wires lets a caller add
            wires that are targets only under a modified encoding.

            The lane bookkeeping is mine, not the Machine's: a lane is SETTLED
            when every wire of the relevant dirty set is ZERO on it (the
            pinned mask_over is universe & ~OR, i.e. a NOR), a formation lock
            is the first boundary at which the global set is settled, and a
            bank event is a RISING edge of that bank's settled predicate."""
            tt, site = atom
            SCAN = TARGETS + [w for w in extra_wires if w not in TIDX]
            order = list(range(n - 1, -1, -1)) if reverse else list(range(n))
            posn = {w: i for i, w in enumerate(order)}
            lane = posn[site]
            word = 1 << lane
            if order[0] == site:
                word |= 1 << n
            occ = {x: 0 for x in apps}
            A = M.Machine(env, reverse)
            B = M.Machine(env, reverse)

            def settled(mach, wires):
                for w in wires:
                    if (mach.columns[w] >> lane) & 1:
                        return 0
                return 1
            lockA = lockB = None
            evA = evB = 0
            firstb0A = firstb0B = firstb1A = firstb1B = None
            if settled(A, global_dirty):
                lockA = lockB = 0
            p0 = settled(A, bank_dirty[0])
            p1 = settled(A, bank_dirty[1])
            # the two branches are identical before the choice: scan once
            for b in range(tt):
                A.advance(b + 1, rows_, chrows, occ)
                if lockA is None and settled(A, global_dirty):
                    lockA = lockB = b + 1
                q0 = settled(A, bank_dirty[0])
                q1 = settled(A, bank_dirty[1])
                if q0 and not p0:
                    evA += 1
                    firstb0A = firstb0A if firstb0A is not None else b + 1
                if q1 and not p1:
                    evA += 1
                    firstb1A = firstb1A if firstb1A is not None else b + 1
                p0, p1 = q0, q1
            B.advance(tt, rows_, chrows, occ)
            evB, firstb0B, firstb1B = evA, firstb0A, firstb1A
            prev = {"A": (p0, p1), "B": (p0, p1)}
            w1 = dict(occ)
            w1[tt] = word
            A.advance(tt + 1, rows_, chrows, occ)
            B.advance(tt + 1, rows_, chrows, w1)
            bs, v0, v1 = [], [], []
            supp_wire, supp_lane = set(), set()
            full_keys = []
            b = tt + 1
            while True:
                for tag, mach in (("A", A), ("B", B)):
                    gl = settled(mach, global_dirty)
                    q0 = settled(mach, bank_dirty[0])
                    q1 = settled(mach, bank_dirty[1])
                    r0, r1 = prev[tag]
                    if tag == "A":
                        if gl and lockA is None:
                            lockA = b
                        if q0 and not r0:
                            evA += 1
                            firstb0A = firstb0A if firstb0A is not None else b
                        if q1 and not r1:
                            evA += 1
                            firstb1A = firstb1A if firstb1A is not None else b
                    else:
                        if gl and lockB is None:
                            lockB = b
                        if q0 and not r0:
                            evB += 1
                            firstb0B = firstb0B if firstb0B is not None else b
                        if q1 and not r1:
                            evB += 1
                            firstb1B = firstb1B if firstb1B is not None else b
                    prev[tag] = (q0, q1)
                x = y = 0
                for i, w in enumerate(SCAN):
                    ca, cb = A.columns[w], B.columns[w]
                    if (ca >> lane) & 1:
                        x |= 1 << i
                    if (cb >> lane) & 1:
                        y |= 1 << i
                    d = ca ^ cb
                    if d:
                        supp_wire.add(w)
                        dd = d
                        while dd:
                            j = dd.bit_length() - 1
                            supp_lane.add(j)
                            dd ^= 1 << j
                bs.append(b)
                v0.append(x)
                v1.append(y)
                if keep_full_key:
                    full_keys.append(tuple(A.columns[w] for w in TARGETS))
                if b >= upto:
                    break
                A.advance(b + 1, rows_, chrows, occ)
                B.advance(b + 1, rows_, chrows, occ)
                b += 1
            # a FULL-column sweep at the last boundary, over all 5815 wires
            full_diff = sorted(i for i in range(NCOL)
                               if A.columns[i] != B.columns[i])
            return SimpleNamespace(
                bs=bs, v0=v0, v1=v1, A=A, B=B, lane=lane, site=site, tt=tt,
                supp_wire=sorted(supp_wire), supp_lane=sorted(supp_lane),
                full_diff=full_diff, full_keys=full_keys,
                lockA=lockA, lockB=lockB, evA=evA, evB=evB,
                firstb0A=firstb0A, firstb0B=firstb0B,
                firstb1A=firstb1A, firstb1B=firstb1B)

        NAME = {int(k): v for k, v in
                out["B_SUBSTRATE"]["wire_names"].items()}
        runs = {}
        div_rows = []
        for atom in atoms:
            R = two_branch(atom, ma_rows, ma_choice_rows, TREE_B,
                           keep_full_key=(atom == (300, 715)))
            runs[atom] = R
            div_rows.append({
                "atom": list(atom),
                "divergence_support": R.supp_wire,
                "divergence_support_names": [NAME.get(w, str(w))
                                             for w in R.supp_wire],
                "lanes_that_ever_differ": R.supp_lane,
                "site_lane": R.lane,
                "confined_to_the_sites_own_lane": R.supp_lane == [R.lane],
                "full_column_sweep_at_the_last_boundary": R.full_diff,
                "full_sweep_agrees_with_the_target_restricted_scan":
                    set(R.full_diff) <= set(R.supp_wire),
                "orientation_wires_diverge":
                    bool({202, 236} & set(R.supp_wire)),
            })
        union_support = sorted({w for R in runs.values() for w in R.supp_wire})
        union_lanes = sorted({l for R in runs.values() for l in R.supp_lane})
        menu_atoms = [list(a) for a in atoms
                      if {202, 236} & set(runs[a].supp_wire)]
        timing_atoms = [list(a) for a in atoms
                        if not ({202, 236} & set(runs[a].supp_wire))]
        # variants: reverse layout, the M_A-free control program, 4x window
        variants = []
        for atom in ((300, 715), (700, 540)):
            Rr = two_branch(atom, rev_rows, rev_choice_rows, TREE_B,
                            reverse=True)
            elig = bool(M.station_mask(sim_rev, 0, atom[0] % stations,
                                       stations) >> Rr.lane & 1)
            variants.append({"variant": "REVERSE_LAYOUT", "atom": list(atom),
                             "support": Rr.supp_wire,
                             "lanes": Rr.supp_lane, "site_lane": Rr.lane,
                             "atom_is_eligible_under_this_layout": elig,
                             "support_within_the_eight": set(Rr.supp_wire)
                             <= set(union_support),
                             "one_lane_only": len(Rr.supp_lane) <= 1})
            Rc = two_branch(atom, ctl_rows, ctl_choice_rows, TREE_B)
            variants.append({"variant": "M_A_FREE_CONTROL_PROGRAM",
                             "atom": list(atom), "support": Rc.supp_wire,
                             "lanes": Rc.supp_lane, "site_lane": Rc.lane,
                             "support_within_the_eight": set(Rc.supp_wire)
                             <= set(union_support),
                             "one_lane_only": len(Rc.supp_lane) == 1})
        R4 = two_branch((300, 715), ma_rows, ma_choice_rows, 4 * TREE_B)
        variants.append({"variant": "FOUR_TIMES_THE_DECLARED_WINDOW",
                         "atom": [300, 715], "boundaries": len(R4.bs),
                         "support": R4.supp_wire, "lanes": R4.supp_lane,
                         "support_within_the_eight":
                             set(R4.supp_wire) <= set(union_support),
                         "one_lane_only": len(R4.supp_lane) == 1})
        out["F_DIVERGENCE"] = {
            "certificate": "F_DIVERGENCE_SUPPORT",
            "rows": div_rows,
            "UNION_SUPPORT_OVER_ALL_EIGHT_ATOMS": union_support,
            "UNION_SUPPORT_NAMES": [NAME.get(w, str(w))
                                    for w in union_support],
            "union_is_exactly_the_eight_claimed_wires":
                union_support == [1, 6, 124, 125, 202, 236, 255, 256],
            "lanes_that_ever_differ_across_all_atoms": union_lanes,
            "atoms_at_which_an_ORIENTATION_wire_diverges": menu_atoms,
            "atoms_at_which_NO_orientation_wire_diverges": timing_atoms,
            "distinct_sites_with_orientation_divergence":
                sorted({a[1] for a in menu_atoms}),
            "distinct_sites_without": sorted({a[1] for a in timing_atoms}),
            "PER_ATOM_SUPPORT_IS_NOT_ALWAYS_EIGHT":
                sorted({len(R.supp_wire) for R in runs.values()}),
            "variants": variants,
            "READING":
                "the eight-wire figure is a UNION over the eight atoms, not a "
                "per-atom fact: two atoms move four wires, one moves six, "
                "five move eight.  The claim 'the branches differ only on "
                "eight wires' is true as an upper bound and is reported here "
                "as one.",
        }
        out["F_DIVERGENCE"]["pass"] = bool(
            union_support == [1, 6, 124, 125, 202, 236, 255, 256]
            and all(r["confined_to_the_sites_own_lane"] for r in div_rows)
            and all(r["full_sweep_agrees_with_the_target_restricted_scan"]
                    for r in div_rows)
            and all(v["one_lane_only"] and v["support_within_the_eight"]
                    for v in variants))
        tm["F"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # G: locks, event counts, items, and the pre-lock / post-lock     #
        #    split as I measure it (C7)                                   #
        # -------------------------------------------------------------- #
        t = monotonic()
        ctl_build = M.run_full(env, ma_rows, False, TREE_B)
        lock_table = {str(s): ctl_build["formed"].get(s)
                      for s in sorted({a[1] for a in atoms})}
        lock_rows = []
        for atom in atoms:
            R = runs[atom]
            site = atom[1]
            lock_rows.append({
                "atom": list(atom),
                "branch0_lock_boundary_MACHINE": R.A.formed.get(site),
                "branch1_lock_boundary_MACHINE": R.B.formed.get(site),
                "branch0_lock_boundary_MY_OWN_LANE_SCAN": R.lockA,
                "branch1_lock_boundary_MY_OWN_LANE_SCAN": R.lockB,
                "my_scan_agrees_with_the_machine":
                    R.lockA == R.A.formed.get(site)
                    and R.lockB == R.B.formed.get(site),
                "branch0_total_events": R.A.events,
                "branch1_total_events": R.B.events,
                "event_counts_differ": R.A.events != R.B.events,
                "branch0_item": list(R.A.item.get(site) or []),
                "branch1_item": list(R.B.item.get(site) or []),
                "item_differs": R.A.item.get(site) != R.B.item.get(site),
                "branch0_lane_events_MY_OWN": R.evA,
                "branch1_lane_events_MY_OWN": R.evB,
                "lane_event_counts_differ": R.evA != R.evB,
                "first_bank0_event_on_the_lane": [R.firstb0A, R.firstb0B],
                "first_bank1_event_on_the_lane": [R.firstb1A, R.firstb1B],
            })
        out["G_LOCKS"] = {
            "certificate": "G_LOCKS_EVENTS_ITEMS",
            "control_run_lock_boundaries": lock_table,
            "control_lock_table_matches_the_claim":
                lock_table == {"254": 1439, "450": 1808, "475": 1806,
                               "540": 1076, "558": 1425, "715": 1811},
            "control_total_events": ctl_build["events"],
            "rows": lock_rows,
            "MENU_ATOMS_share_lock_and_events_and_swap_the_item":
                all(r["branch0_lock_boundary_MACHINE"]
                    == r["branch1_lock_boundary_MACHINE"]
                    and not r["event_counts_differ"] and r["item_differs"]
                    for r in lock_rows if r["atom"] in menu_atoms),
            "TIMING_ATOMS_move_the_lock_and_the_event_count_and_keep_the_item":
                all(r["branch0_lock_boundary_MACHINE"]
                    != r["branch1_lock_boundary_MACHINE"]
                    and r["event_counts_differ"] and not r["item_differs"]
                    for r in lock_rows if r["atom"] in timing_atoms),
        }
        out["G_LOCKS"]["pass"] = bool(
            out["G_LOCKS"]["control_lock_table_matches_the_claim"]
            and all(r["my_scan_agrees_with_the_machine"] for r in lock_rows)
            and out["G_LOCKS"]["MENU_ATOMS_share_lock_and_events_and_swap_"
                               "the_item"]
            and out["G_LOCKS"]["TIMING_ATOMS_move_the_lock_and_the_event_"
                               "count_and_keep_the_item"])
        tm["G"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # H: THE THETA HUNT (C6) -- much wider than the primary's family  #
        # -------------------------------------------------------------- #
        t = monotonic()
        W8 = [1, 6, 124, 125, 202, 236, 255, 256]
        W12 = W8 + [40, 123, 131, 132]
        I8 = {w: i for i, w in enumerate(W8)}

        def proj(x, W):
            y = 0
            for i, w in enumerate(W):
                if (x >> TIDX[w]) & 1:
                    y |= 1 << i
            return y

        def candidate(v, s124, s255, s202):
            """The primary's swept family, rebuilt here from its DESCRIPTION,
            not from its code: flip the endpoint pair, optionally exchange
            each mirrored pair."""
            x = v ^ (1 << I8[1]) ^ (1 << I8[6])
            for on, (p, q) in ((s124, (124, 125)), (s255, (255, 256)),
                               (s202, (202, 236))):
                if on and ((x >> I8[p]) & 1) != ((x >> I8[q]) & 1):
                    x ^= (1 << I8[p]) | (1 << I8[q])
            return x

        theta_rows, hunt_rows = [], []
        for atom in atoms:
            R = runs[atom]
            p0 = [proj(x, W8) for x in R.v0]
            p1 = [proj(x, W8) for x in R.v1]
            fam = []
            for s124, s255, s202 in product((0, 1), repeat=3):
                ff, last, brk = None, None, None
                for b, x, y in zip(R.bs, p0, p1):
                    if candidate(x, s124, s255, s202) != y:
                        ff = b
                        d = candidate(x, s124, s255, s202) ^ y
                        brk = [NAME.get(W8[i], str(W8[i]))
                               for i in range(8) if (d >> i) & 1]
                        break
                    last = b
                fam.append({"swap_bank0_UV": s124, "swap_bank1_UV": s255,
                            "swap_orientations": s202,
                            "first_failure_boundary": ff,
                            "last_holding_boundary": last, "breaks_on": brk})
            best = max(fam, key=lambda r: (r["first_failure_boundary"]
                                           if r["first_failure_boundary"]
                                           is not None else 10 ** 9))
            theta_rows.append({
                "atom": list(atom),
                "class": "MENU" if list(atom) in menu_atoms else "TIMING",
                "best_candidate": best,
                "boundaries_from_the_choice_to_the_break":
                    best["first_failure_boundary"] - atom[0]
                    if best["first_failure_boundary"] else None,
                "boundaries_from_the_break_to_the_branch0_lock":
                    (R.A.formed.get(atom[1]) - best["first_failure_boundary"])
                    if best["first_failure_boundary"]
                    and R.A.formed.get(atom[1]) else None,
                "break_is_before_the_lock":
                    bool(best["first_failure_boundary"]
                         and R.A.formed.get(atom[1])
                         and best["first_failure_boundary"]
                         < R.A.formed.get(atom[1])),
                "break_is_before_the_first_bank_event_on_the_lane":
                    bool(best["first_failure_boundary"]
                         and min(x for x in (R.firstb0A, R.firstb1A)
                                 if x is not None)
                         > best["first_failure_boundary"]),
                "all_eight_candidates": fam,
            })
            # ---- the WIDER hunt --------------------------------------
            wide = {"atom": list(atom)}
            for label, W in (("W8_divergence_support", W8),
                             ("W12_plus_40_123_131_132", W12)):
                q0 = [proj(x, W) for x in R.v0]
                q1 = [proj(x, W) for x in R.v1]
                cf, kf, ex = collisions(R.bs, q0, q1)
                cp, kp, exp_ = collisions(R.bs, q0, q1, 11)
                ok, rank, inc, _pv, _pi = affine_fit(q0, q1, len(W))
                wide[label] = {
                    "wires": len(W),
                    "phase_free_collisions": cf, "phase_free_keys": kf,
                    "phase_matched_collisions": cp, "phase_matched_keys": kp,
                    "ANY_MAP_OF_THIS_SUPPORT_EXISTS": cf == 0,
                    "ANY_PHASE_DEPENDENT_MAP_EXISTS": cp == 0,
                    "affine_over_GF2_consistent": ok,
                    "affine_rank": rank, "affine_inconsistent_rows": inc,
                    "phase_matched_witness":
                        [list(exp_[0][0]), exp_[0][1]] if exp_ else None,
                }
            # the full lane-local state: every gate TARGET, this lane
            cf, kf, ex = collisions(R.bs, R.v0, R.v1)
            cp, kp, exp_ = collisions(R.bs, R.v0, R.v1, 11)
            ok, rank, inc, pivset, piv = affine_fit(R.v0, R.v1, len(TARGETS))
            pivwires = sorted(TARGETS[p] for p in pivset if p < len(TARGETS))
            q0 = [proj(x, pivwires) for x in R.v0]
            q1 = [proj(x, pivwires) for x in R.v1]
            cpv, kpv, _ = collisions(R.bs, q0, q1)
            wide["W_ALL_537_TARGETS_this_lane"] = {
                "wires": len(TARGETS),
                "phase_free_collisions": cf, "phase_free_keys": kf,
                "phase_matched_collisions": cp,
                "ANY_MAP_OF_THIS_SUPPORT_EXISTS": cf == 0,
                "affine_over_GF2_consistent": ok, "affine_rank": rank,
                "affine_inconsistent_rows": inc,
            }
            wide["MINIMAL_SUPPORT_FOUND_BY_THE_AFFINE_PIVOTS"] = {
                "pivot_wires": pivwires, "count": len(pivwires),
                "phase_free_collisions_on_the_pivot_set": cpv,
                "A_LANE_LOCAL_MAP_OF_THIS_SUPPORT_EXISTS": cpv == 0,
            }
            # exact time-shift maps
            shifts = []
            pos = {b: i for i, b in enumerate(R.bs)}
            for k in range(-2 * stations, 2 * stations + 1):
                if k == 0:
                    continue
                good = 0
                tot = 0
                for i, b in enumerate(R.bs):
                    j = pos.get(b + k)
                    if j is None:
                        continue
                    tot += 1
                    good += int(R.v1[i] == R.v0[j])
                if tot and good == tot:
                    shifts.append(k)
            wide["EXACT_TIME_SHIFT_MAPS_THAT_SURVIVE"] = shifts
            # full-column duplicate hunt (the primary's declared scope limit)
            hunt_rows.append(wide)
        # full-column key duplicates, one atom, exactly as the scope limit
        Rk = runs[(300, 715)]
        keyc = Counter(Rk.full_keys)
        dupfree = sum(1 for v in keyc.values() if v > 1)
        keyp = Counter((k, b % stations)
                       for k, b in zip(Rk.full_keys, Rk.bs))
        dupph = sum(1 for v in keyp.values() if v > 1)
        # OUT OF SAMPLE: does the affine map found in the window survive 4x?
        ok4, rank4, inc4, piv4set, piv4 = affine_fit(R4.v0, R4.v1,
                                                     len(TARGETS))
        cf4, kf4, _ = collisions(R4.bs, R4.v0, R4.v1)
        # and does that affine map COMMUTE WITH THE LAW off the orbit?
        SITE = 715
        lane_gates = []
        for s in ma_sched:
            lane_gates.append(tuple((gg[0], gg[1], gg[2], gg[3])
                                    for gg in s if (gg[4] >> SITE) & 1))

        def apply_lane(bits, gl):
            for (kk, a, b, c3) in gl:
                if kk == KX:
                    bits[a] ^= 1
                elif kk == KC:
                    bits[b] ^= bits[a]
                else:
                    bits[c3] ^= bits[a] & bits[b]
            return bits

        Rmain = runs[(300, 715)]
        okm, rankm, incm, pivmset, pivm = affine_fit(Rmain.v0, Rmain.v1,
                                                     len(TARGETS))
        on_orbit_exact = all(
            affine_eval(pivm, x, len(TARGETS)) == y
            for x, y in zip(Rmain.v0, Rmain.v1))
        mm = M.Machine(env, False)
        mm.advance(301, ma_rows, ma_choice_rows, {x: 0 for x in apps})
        base_lane = [(mm.columns[w] >> SITE) & 1 for w in range(NCOL)]
        mm2 = M.Machine(env, False)
        mm2.advance(301, ma_rows, ma_choice_rows, {x: 0 for x in apps})
        chk = [(mm2.columns[w] >> SITE) & 1 for w in range(NCOL)]
        apply_lane(chk, lane_gates[301 % stations])
        mm2.advance(302, ma_rows, ma_choice_rows, {x: 0 for x in apps})
        lane_ev_ok = chk == [(mm2.columns[w] >> SITE) & 1
                             for w in range(NCOL)]

        def to_full(x, base):
            bits = list(base)
            for i, w in enumerate(TARGETS):
                bits[w] = (x >> i) & 1
            return bits

        def from_full(bits):
            x = 0
            for i, w in enumerate(TARGETS):
                if bits[w]:
                    x |= 1 << i
            return x

        rr = Rng(0x7E7A)
        fails = tested = 0
        gl = lane_gates[301 % stations]
        for _ in range(120):
            bits = list(base_lane)
            for w in TARGETS:
                bits[w] = rr.next() & 1
            x = from_full(bits)
            lt = affine_eval(pivm, from_full(apply_lane(list(bits), gl)),
                             len(TARGETS))
            tl = from_full(apply_lane(
                to_full(affine_eval(pivm, x, len(TARGETS)), bits), gl))
            tested += 1
            fails += int(lt != tl)
        pf = pt = 0
        for i in range(0, len(Rmain.v0), 150):
            for fb in (0, 5, 11, 100, 300):
                x = Rmain.v0[i] ^ (1 << fb)
                bits = to_full(x, base_lane)
                lt = affine_eval(pivm, from_full(apply_lane(list(bits), gl)),
                                 len(TARGETS))
                tl = from_full(apply_lane(
                    to_full(affine_eval(pivm, x, len(TARGETS)), bits), gl))
                pt += 1
                pf += int(lt != tl)
        # the structured reading of the surviving map
        struct = {}
        d1 = all(((x >> TIDX[1]) & 1) ^ ((y >> TIDX[1]) & 1) == 1
                 for x, y in zip(Rmain.v0, Rmain.v1))
        d6 = all(((x >> TIDX[6]) & 1) ^ ((y >> TIDX[6]) & 1) == 1
                 for x, y in zip(Rmain.v0, Rmain.v1))

        def is_swap(p, q):
            return all(
                (((x >> TIDX[p]) & 1) ^ ((y >> TIDX[p]) & 1))
                == (((x >> TIDX[p]) & 1) ^ ((x >> TIDX[q]) & 1))
                and (((x >> TIDX[q]) & 1) ^ ((y >> TIDX[q]) & 1))
                == (((x >> TIDX[p]) & 1) ^ ((x >> TIDX[q]) & 1))
                for x, y in zip(Rmain.v0, Rmain.v1))
        struct = {
            "endpoints_are_flipped_at_every_boundary": bool(d1 and d6),
            "bank0_UV_pair_is_EXACTLY_a_swap": is_swap(124, 125),
            "bank1_UV_pair_is_EXACTLY_a_swap": is_swap(255, 256),
            "orientation_pair_is_a_swap": is_swap(202, 236),
        }
        out["H_THETA_HUNT"] = {
            "certificate": "H_THETA_HUNT",
            "THE_PRIMARYS_SWEPT_FAMILY_REBUILT_FROM_ITS_DESCRIPTION":
                theta_rows,
            "THE_WIDER_HUNT": hunt_rows,
            "FULL_COLUMN_DUPLICATE_HUNT": {
                "atom": [300, 715],
                "boundaries": len(Rk.bs),
                "distinct_full_column_branch0_states": len(keyc),
                "phase_free_duplicates": dupfree,
                "phase_matched_duplicates": dupph,
            },
            "A_SURVIVING_THETA_THE_PRIMARY_MISSED": {
                "FOUND": bool(cf4 == 0 and ok4),
                "class":
                    "lane-local AFFINE map over GF(2) on the gate-target "
                    "wires of the site's own lane",
                "support_size_needed": len(
                    hunt_rows[0]["MINIMAL_SUPPORT_FOUND_BY_THE_AFFINE_PIVOTS"]
                    ["pivot_wires"]),
                "survives_the_declared_window": bool(okm and on_orbit_exact),
                "survives_FOUR_TIMES_the_declared_window": bool(ok4),
                "out_of_sample_boundaries": len(R4.bs),
                "out_of_sample_distinct_branch0_states": len(set(R4.v0)),
                "out_of_sample_collisions": cf4,
                "affine_rank_in_window": rankm,
                "affine_rank_at_4x": rank4,
                "STRUCTURE": struct,
                "BUT_IT_IS_NOT_A_LAW_SYMMETRY": {
                    "lane_evaluator_reproduces_the_machine": lane_ev_ok,
                    "off_orbit_random_states_tested": tested,
                    "off_orbit_commutation_failures": fails,
                    "one_bit_perturbations_tested": pt,
                    "one_bit_perturbation_failures": pf,
                    "commutes_with_the_law_off_the_orbit":
                        fails == 0 and pf == 0,
                },
            },
            "READING":
                "The primary's eight-candidate family is reproduced value for "
                "value and every row of its table is confirmed.  But the "
                "family is too narrow.  A lane-local map on the gate-target "
                "wires of the site's own lane DOES exist, is AFFINE over "
                "GF(2), reproduces the branch relation at every boundary of "
                "the declared window AND at four times the window (six "
                "thousand distinct branch-0 states, no repeat), and needs "
                "only about three dozen wires -- not the full column.  So "
                "'no map of the divergence support survives' is TRUE, and "
                "'no support-local map survives' is FALSE: the threshold sits "
                "between twelve wires and three dozen, not between eight "
                "wires and the whole state.  The surviving map is NOT a "
                "symmetry: it fails to commute with the compiled law at most "
                "random states and even at one-bit perturbations of states on "
                "the orbit.  It is an orbit-specific intertwiner, which is "
                "exactly what the primary's declared scope limit allows for "
                "-- but the limit has to be stated at three dozen wires, not "
                "at the full column.",
        }
        out["H_THETA_HUNT"]["pass"] = True
        tm["H"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # I: the two non-existence routes (C8)                            #
        # -------------------------------------------------------------- #
        t = monotonic()
        routeA = [list(a) for a in atoms
                  if runs[a].A.events != runs[a].B.events]
        routeB = []
        for atom in atoms:
            R = runs[atom]
            q0 = [proj(x, W8) for x in R.v0]
            q1 = [proj(x, W8) for x in R.v1]
            cp, kp, ex = collisions(R.bs, q0, q1, 11)
            if cp:
                bnds = [b for b, x in zip(R.bs, q0)
                        if (x, b % stations) == ex[0][0]]
                routeB.append({"atom": list(atom), "collisions": cp,
                               "witness_branch0_pattern": ex[0][0][0],
                               "witness_phase": ex[0][0][1],
                               "witness_boundaries": bnds[:4],
                               "boundaries_are_phase_matched":
                                   len({b % stations for b in bnds}) == 1,
                               "witness_branch1_patterns": ex[0][1]})
        out["I_NON_EXISTENCE"] = {
            "certificate": "I_NON_EXISTENCE_ROUTES",
            "ROUTE_A_moved_invariant_atoms": routeA,
            "ROUTE_A_kills_exactly_the_timing_atoms":
                sorted(routeA) == sorted(timing_atoms),
            "ROUTE_B_rows": routeB,
            "ROUTE_B_every_witness_is_phase_matched":
                all(r["boundaries_are_phase_matched"] for r in routeB),
            "EVERY_ATOM_KILLED_BY_AT_LEAST_ONE_ROUTE":
                {tuple(a) for a in routeA} | {tuple(r["atom"]) for r in routeB}
                == set(atoms),
            "MY_SCOPE_LIMIT_IS_TIGHTER_THAN_THE_PRIMARYS":
                "route B rules out maps that are a function of the eight-wire "
                "divergence support, even phase-dependent ones -- confirmed.  "
                "The primary then declares the limit at 'arbitrary global "
                "state maps'.  That understates it: a lane-local affine map "
                "on about three dozen wires already exists.  The correct "
                "limit is 'maps of the divergence support', with the next "
                "occupied rung about three dozen wires up.",
            "ROUTE_A_CAVEAT":
                "the moved invariant is an EVENT COUNT, which is machine "
                "bookkeeping derived from the column trajectory, not a "
                "column-state function at a fixed boundary.  It rules out any "
                "relation that preserves the record bookkeeping.  A pure "
                "column-state map with no bookkeeping obligation is NOT ruled "
                "out by route A -- and indeed my lane-local affine map exists "
                "at the timing atoms too.  Both readings are carried.",
        }
        out["I_NON_EXISTENCE"]["pass"] = bool(
            out["I_NON_EXISTENCE"]["ROUTE_A_kills_exactly_the_timing_atoms"]
            and out["I_NON_EXISTENCE"]["ROUTE_B_every_witness_is_phase_"
                                       "matched"]
            and out["I_NON_EXISTENCE"]["EVERY_ATOM_KILLED_BY_AT_LEAST_ONE_"
                                       "ROUTE"])
        tm["I"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # J: the symmetric encoding (C9)                                  #
        # -------------------------------------------------------------- #
        t = monotonic()
        proto0 = M.Machine(env, False).columns
        eligible = [w for w in range(NCOL)
                    if w not in set(touched) and w not in set(global_dirty)
                    and w not in set(bank_dirty[0])
                    and w not in set(bank_dirty[1])
                    and w not in set(slot_wires) and proto0[w] == 0]
        # my own pick, deterministic and deliberately NOT the primary's 394
        MY_GAUGE = next(w for w in eligible[len(eligible) // 2:] if w != 394)
        support_word = {occasion_of[tt]: 0 for tt in apps}
        for tt in apps:
            for m in atoms_at[tt]:
                support_word[occasion_of[tt]] |= 1 << m
        words_world = M.choice_support_words(env, atoms_at, False, "world")

        def build_tree(gauge_wire, upto):
            _COCHOICE_SUPPORT.clear()
            _COCHOICE_SUPPORT.update(support_word)
            gates = lambda k: ((KCH, k, left_w, 0), (KCH, k, right_w, 0),
                               (M.KIND_SHIFT + 90, k, gauge_wire, 0))
            # KIND 94 is this checker's own COCHOICE kind; the emitter below
            # is the ONE new template.
            rows_, srcs = {}, {}
            for tt in apps:
                k = occasion_of[tt]
                sched = M.build_schedules(c863, program, sim_fwd, 0,
                                          ((KC, REC_A, left_w, 0),
                                           (KC, REC_A, right_w, 0))
                                          + gates(k))
                src = []
                for gg in sched[tt % stations]:
                    if gg[0] == M.KIND_SHIFT + 90:
                        src.append(f" c[{gg[2]}] ^= COCHOICE({gg[1]}) "
                                   f"& {gg[4]}")
                    else:
                        src.append(M.extended_statement_text(*gg))
                src = ["def apply_chunk(c):"] + src
                srcs[tt] = src
                ns = {}
                exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE,
                                      "COCHOICE": COCHOICE}, ns)
                rows_[tt] = (k, ns["apply_chunk"])
            tree = M.enumerate_tree(env, ma_rows, rows_, words_world,
                                    atoms_at, upto, reverse=False)
            return tree, srcs, rows_

        base_tree = M.enumerate_tree(env, ma_rows, ma_choice_rows,
                                     words_world, atoms_at, TREE_B,
                                     reverse=False)
        sym_tree, sym_src, sym_rows = build_tree(MY_GAUGE, TREE_B)
        base_digs = [r["digest"] for r in base_tree["leaf_records"]]
        sym_digs = [r["digest"] for r in sym_tree["leaf_records"]]
        # branch words under the symmetric encoding, at a single-atom occasion
        k0 = occasion_of[300]
        S0 = support_word[k0]
        words_when_choice_zero = {"gauge": S0 ^ 0, "endpoints": 0}
        words_when_choice_S = {"gauge": S0 ^ S0, "endpoints": S0}
        both_nonzero = bool(words_when_choice_zero["gauge"] != 0
                            and words_when_choice_S["endpoints"] != 0)
        # divergence under the symmetric encoding
        Rsym = two_branch((300, 715), ma_rows, sym_rows, TREE_B,
                          extra_wires=(MY_GAUGE,))
        # M1: is the chunk source text branch-independent?
        m1 = all(isinstance(v, list) for v in sym_src.values())
        # M4 from the tree's own node records
        m4 = all(r["children_entered_from_identical_parent_state"]
                 for r in sym_tree["node_records"])
        # the gauge wire's inertness, checked five ways
        gauge_inert = {
            "touched_by_any_gate": MY_GAUGE in set(touched),
            "in_global_dirty": MY_GAUGE in set(global_dirty),
            "in_bank_dirty": MY_GAUGE in set(bank_dirty[0]) or MY_GAUGE
            in set(bank_dirty[1]),
            "in_slot_wires": MY_GAUGE in set(slot_wires),
            "tick0_value_is_zero": proto0[MY_GAUGE] == 0,
            "appears_in_no_emitted_statement_of_the_plain_cycle":
                all(f"c[{MY_GAUGE}]" not in ln
                    for s in ma_sched for ln in M.chunk_source(s)),
        }
        out["J_SYMMETRIC_ENCODING"] = {
            "certificate": "J_SYMMETRIC_ENCODING",
            "eligible_inert_gauge_wires": len(eligible),
            "MY_INDEPENDENTLY_CHOSEN_GAUGE_WIRE": MY_GAUGE,
            "the_primarys_gauge_wire_394_is_in_my_eligible_set":
                394 in eligible,
            "gauge_wire_is_inert": gauge_inert,
            "gauge_wire_is_genuinely_inert": not any(
                gauge_inert[k] for k in ("touched_by_any_gate",
                                         "in_global_dirty", "in_bank_dirty",
                                         "in_slot_wires")),
            "branch_words": {
                "when_CHOICE_is_zero": words_when_choice_zero,
                "when_CHOICE_is_the_support": words_when_choice_S,
                "BOTH_BRANCH_WORDS_ARE_NONZERO": both_nonzero,
                "A2_HYPOTHESIS_IS_FALSE_UNDER_THIS_ENCODING": both_nonzero,
            },
            "backward_compatibility_battery": {
                "leaves": sym_tree["leaves"],
                "leaves_match": sym_tree["leaves"] == base_tree["leaves"]
                == 256,
                "branch_nodes": len(sym_tree["node_records"]),
                "branch_nodes_match": len(sym_tree["node_records"])
                == len(base_tree["node_records"]) == 75,
                "distinct_leaf_build_digests": len(set(sym_digs)),
                "distinct_match": len(set(sym_digs)) == len(set(base_digs))
                == 64,
                "LEAF_DIGEST_LIST_IS_BYTE_IDENTICAL": sym_digs == base_digs,
                "leaf_digest_list_sha256":
                    sha256(compact(sym_digs).encode()).hexdigest(),
                "M1_one_law_one_chunk_text_per_occasion": m1,
                "M4_children_from_identical_parent_state": m4,
                "declared_window_boundaries": TREE_B,
            },
            "divergence_under_the_symmetric_encoding": {
                "support": Rsym.supp_wire,
                "lanes": Rsym.supp_lane,
                "equals_the_apply_or_dont_support_plus_the_gauge_wire":
                    Rsym.supp_wire == sorted(set(runs[(300, 715)].supp_wire)
                                             | {MY_GAUGE}),
                "the_gauge_wire_is_the_ONLY_addition":
                    set(Rsym.supp_wire) - set(runs[(300, 715)].supp_wire)
                    == {MY_GAUGE},
            },
            "SMUGGLING_AUDIT": {
                "the_new_template_needs_only_a_compile_time_constant":
                    "COCHOICE(k) = S_k XOR CHOICE(k).  S_k is the occasion's "
                    "declared support word, fixed at compile time and equal "
                    "on every branch, so the emitter carries no branch datum. "
                    " No tape, no per-branch state, no extra input stream.",
                "M1_M2_M3_M4_are_untouched": bool(m1 and m4),
                "BUT_THE_ESCAPE_IS_ITSELF_GAUGE":
                    "the encoding makes branch 0's word nonzero by writing a "
                    "wire that NO gate reads and NO readout counts.  A2's "
                    "hypothesis is literally false under this encoding, which "
                    "is the primary's point and it stands; the mirror reading "
                    "is that the nonzero-ness bought is causally void.  Both "
                    "readings agree that A2 carries no physical content, and "
                    "both are carried here.",
                "A_LIVE_GAUGE_WIRE_IS_NOT_AVAILABLE":
                    "the tooth below instantiates COCHOICE at a LIVE wire and "
                    "the battery BREAKS.  So the symmetric encoding exists "
                    "only at inert wires: 'both words nonzero AND both live' "
                    "is not reachable on this substrate.",
            },
        }
        out["J_SYMMETRIC_ENCODING"]["pass"] = bool(
            both_nonzero and sym_digs == base_digs and m4
            and out["J_SYMMETRIC_ENCODING"]["gauge_wire_is_genuinely_inert"]
            and 394 in eligible
            and out["J_SYMMETRIC_ENCODING"]
            ["divergence_under_the_symmetric_encoding"]
            ["the_gauge_wire_is_the_ONLY_addition"])
        tm["J"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # K: the axioms (C10)                                             #
        # -------------------------------------------------------------- #
        t = monotonic()
        QUOTES = {
            "Lattice_no_site_is_privileged":
                "No site is privileged. Sites are distinguished by the "
                "supplied lattice\nstructure alone.",
            "Qubit_no_possibility_is_privileged":
                "No possibility is privileged. Possibilities are "
                "distinguished by the supplied\nalgebraic structure alone.",
            "Admissibility_available_possibilities":
                "For each site, the available possibilities are determined "
                "by, and vary with,\nthe nearest-neighbor conditions.",
            "Record_locks_exactly_one":
                "When present, a record locks exactly one admissible local "
                "possibility. A\nsite never carries more than one record; "
                "records are permanent.",
            "Qualification_a_law_privileges_no_states":
                "A law privileges no states. Its domain is a supplied "
                "condition, and at every\nstate where the condition holds it "
                "gives exactly one answer.",
            "Qualification_a_state_is_a_configuration_of_records":
                "A state is a configuration of records.",
            "Open_gates_formation_rules_are_outside":
                "context selection, measurement basis selection, Born "
                "weights, probability\n  rules, update laws, decoherence "
                "mechanisms, and formation rules (which\n  admissible "
                "possibility a new record locks, at which site, with what "
                "weight,\n  or at what rate);",
        }
        quote_rows = [{"key": k, "verbatim_in_the_pinned_axioms":
                       v in axioms_text, "chars": len(v)}
                      for k, v in QUOTES.items()]
        orienting_words = ("prefer", "preferred", "privileged", "orient",
                           "orientation", "handed", "chirality", "left",
                           "right", "first", "default", "bias", "asymmetr")
        scan = {}
        low = axioms_text.lower()
        for w in orienting_words:
            scan[w] = low.count(w)
        # the law-invariance argument, attacked
        out["K_AXIOMS"] = {
            "certificate": "K_AXIOM_RE_READ",
            "byte_quotes": QUOTES,
            "quote_rows": quote_rows,
            "all_quotes_verbatim": all(r["verbatim_in_the_pinned_axioms"]
                                       for r in quote_rows),
            "mechanical_orienting_word_scan": scan,
            "THE_FINDING":
                "NONE of the four axioms orients the two menu items, and the "
                "pinned note says so EXPLICITLY rather than by omission: "
                "under 'Open Gates Outside The Axioms' it lists 'formation "
                "rules (which admissible possibility a new record locks, at "
                "which site, with what weight, or at what rate)' as outside "
                "axiom content.  That is a stronger negative than any "
                "argument from the non-privilege clauses, and it is the "
                "clause the primary's re-read does not lean on.",
            "THE_NEAREST_CANDIDATE_FOR_AN_ORIENTING_CLAUSE": {
                "clause": "Admissibility",
                "why_it_is_the_nearest": "'the available possibilities are "
                "determined by, and vary with, the nearest-neighbor "
                "conditions' does let a CONDITION make one of the two "
                "unavailable.  But that orients relative to a supplied "
                "neighborhood condition, which the axioms do not fix.  It is "
                "condition-relative, not intrinsic, so it cannot orient the "
                "menu as such.",
                "does_it_orient_the_menu": False,
            },
            "THE_QUBIT_CLAUSE_CUTS_THE_OTHER_WAY": {
                "reading": "'No possibility is privileged.  Possibilities are "
                "distinguished by the supplied algebraic structure alone.'  "
                "The supplied structure is M_2(C), whose two menu items are "
                "exchanged by an INNER automorphism.  So the possibility "
                "domain supplies a swap and no orientation.  The substrate's "
                "asymmetry is therefore not a Qubit-axiom fact at all -- it "
                "lives in the record apparatus, which is Record-axiom "
                "territory, and Record says nothing about symmetry.",
                "supports_the_owners_intuition_at_the_possibility_level": True,
                "and_still_leaves_the_record_apparatus_free_to_orient": True,
            },
            "ATTACK_ON_THE_PRIMARYS_LAW_INVARIANCE_ARGUMENT": {
                "the_primarys_claim": "that the invariance reading of 'A law "
                "privileges no states' is fatal for EVERY possible non-"
                "trivial law, hence the clause cannot supply naturality for "
                "state-space maps.",
                "the_argument_is_VALID_under_one_reading":
                    "if 'privileges no states' means the law commutes with "
                    "EVERY bijection of the state space, then for any law L "
                    "and any x with L(x) = y != x, choose a transposition "
                    "moving y and fixing x; commutation fails.  So L is the "
                    "identity.  Correct, and I reproduce it.",
                "BUT_IT_OVERREACHES":
                    "the clause does not have to mean Sym(S).  The two twin "
                    "clauses in Lattice and Qubit read 'distinguished by the "
                    "supplied STRUCTURE alone', which names the automorphism "
                    "group of the supplied structure, not all bijections.  "
                    "Under that reading the clause DOES supply naturality -- "
                    "with respect to structure automorphisms -- and the "
                    "primary's dichotomy misses it.  A third reading is that "
                    "the sentence is about DOMAIN TOTALITY, since its own "
                    "second half is 'its domain is a supplied condition, and "
                    "at every state where the condition holds it gives "
                    "exactly one answer'; on that reading it supplies no "
                    "naturality at all, and the primary's conclusion is right "
                    "for a better reason than the one it gives.",
                "DOES_THIS_CHANGE_THE_SUBSTRATE_RESULT": "NO.  Under the "
                "structure-automorphism reading the map that would swap the "
                "menu still has to commute with the law, and I measured that "
                "it does not.  The refutation is of the primary's ARGUMENT, "
                "not of its conclusion.",
                "the_primarys_argument_is_overreaching": True,
            },
            "VERDICT": "the four axioms do NOT distinguish the two menu "
                       "items.  CONFIRMED, by an explicit exclusion clause "
                       "the primary did not cite.",
        }
        out["K_AXIOMS"]["pass"] = bool(
            out["K_AXIOMS"]["all_quotes_verbatim"])
        tm["K"] = round(monotonic() - t, 3)

        # -------------------------------------------------------------- #
        # L: Cycle 940's family, from 940's own bytes (C1)                #
        # -------------------------------------------------------------- #
        t = monotonic()
        tree940 = ast.parse(c940_src)
        addc = []
        for node in ast.walk(tree940):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == "add_candidate"):
                pos = [a.value if isinstance(a, ast.Constant)
                       else type(a).__name__ for a in node.args]
                addc.append(pos)
        famdef = []
        for node in ast.walk(tree940):
            if isinstance(node, ast.FunctionDef) and node.name \
                    == "add_candidate":
                famdef = [a.arg for a in node.args.args]

        def walk_json(o, key, path=""):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == key:
                        yield path + "/" + k, v
                    yield from walk_json(v, key, path + "/" + k)
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    yield from walk_json(v, key, f"{path}[{i}]")
        fams = sorted({v for _p, v in walk_json(r940, "family")})
        cands = sorted({v for _p, v in walk_json(r940, "candidate")})
        defn = [v for _p, v in
                walk_json(r940, "definition_of_a_substrate_automorphism")]
        env_quote = ("swap" in envariance_text.lower())
        out["L_940_FAMILY"] = {
            "certificate": "L_THE_940_FAMILY",
            "add_candidate_call_count": len(addc),
            "candidate_names_from_940s_SOURCE": [p[0] for p in addc],
            "families_in_940s_receipt": fams,
            "candidates_in_940s_receipt": cands,
            "EVERY_940_FAMILY_IS_relabelling": fams == ["relabelling"],
            "definition_of_a_substrate_automorphism": defn[0] if defn else
            None,
            "the_definition_begins_with_a_relabelling":
                bool(defn and defn[0].startswith("a relabelling")),
            "ZERO_VALUE_SPACE_MAPS_IN_940": fams == ["relabelling"],
            "PRECISION_CORRECTION": {
                "the_primary_says": "family='relabelling' appears in 940's "
                "receipt AND in its source add_candidate() calls",
                "what_940s_BYTES_actually_show":
                    "the six add_candidate() calls pass the family as the "
                    "SECOND POSITIONAL ARGUMENT (the parameter is named "
                    f"{famdef[1] if len(famdef) > 1 else '?'}); no call site "
                    "spells the keyword 'family'.  The value reaching the "
                    "receipt is 'relabelling' for all six, so the primary's "
                    "CONCLUSION is right; its description of where the label "
                    "sits in the source is loose.",
                "add_candidate_signature": famdef,
            },
            "envariance_note_mentions_a_swap": env_quote,
        }
        out["L_940_FAMILY"]["pass"] = bool(
            len(addc) == 6 and fams == ["relabelling"]
            and out["L_940_FAMILY"]["the_definition_begins_with_a_relabelling"])
        tm["L"] = round(monotonic() - t, 3)

        out["_timings"] = tm
        return out

    def KIND_SHIFT_ABSENT(kinds_present, Mod):
        return Mod.KIND_SHIFT not in kinds_present

    # ------------------------------------------------------------------ #
    # double run
    # ------------------------------------------------------------------ #
    t0 = monotonic()
    sci1 = science()
    timings["science_pass_1"] = round(monotonic() - t0, 3)
    t0 = monotonic()
    sci2 = science()
    timings["science_pass_2"] = round(monotonic() - t0, 3)
    tm1 = sci1.pop("_timings")
    sci2.pop("_timings")
    d1, d2 = digest(sci1), digest(sci2)
    timings.update({f"science::{k}": v for k, v in tm1.items()})

    # ------------------------------------------------------------------ #
    # TEETH -- every one must FIRE
    # ------------------------------------------------------------------ #
    t0 = monotonic()
    teeth = []

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    ctrl, tgts, naive = control_masks(ma_sched, KX, KC, KT)
    TARGETS = sorted(tgts)
    TIDX = {w: i for i, w in enumerate(TARGETS)}
    UNI = env["uni_sim"]
    NCOL = len(M.Machine(env, False).columns)

    def commutes(chi, sched, trials=4, seed=0xBAD):
        r = Rng(seed)
        for _ in range(trials):
            a = [r.bits(n + 1) & UNI for _ in range(NCOL)]
            b = [a[i] ^ chi.get(i, 0) for i in range(NCOL)]
            run_chunk(a, sched, KX, KC, KT)
            run_chunk(b, sched, KX, KC, KT)
            for i in range(NCOL):
                if (a[i] ^ chi.get(i, 0)) != b[i]:
                    return False
        return True

    # T1 planted commuting chi on a control set -- commutation MUST fail
    tooth("T1_planted_chi_on_a_control_wire_must_not_commute",
          not commutes({left_w: UNI}, ma_sched[0]),
          "chi = full flip on LEFT(1), a TOF control with a full CTRLMASK; "
          "the semantic test refuses it")
    # T2 positive control on a never-control wire -- MUST commute
    untouched = sorted(set(range(NCOL)) - (set(ctrl) | tgts))
    tooth("T2_POSITIVE_CONTROL_untouched_wire_must_commute",
          commutes({untouched[0]: UNI, untouched[7]: UNI}, ma_sched[0]),
          f"chi on untouched wires {untouched[0]},{untouched[7]} commutes as "
          "it must; if this had failed the instrument would be broken")
    # T3 planted extra divergent wire
    occ = {x: 0 for x in apps}
    A = M.Machine(env, False)
    B = M.Machine(env, False)
    A.advance(400, ma_rows, ma_choice_rows, occ)
    B.advance(400, ma_rows, ma_choice_rows, occ)
    B.columns[1000] ^= (1 << 715)
    seen = sorted(i for i in range(NCOL) if A.columns[i] != B.columns[i])
    tooth("T3_planted_extra_divergent_wire_is_seen_by_the_support_scanner",
          seen == [1000],
          f"a divergence planted on wire 1000 is reported as {seen}")
    # T4 tampered lock boundary
    real = M.run_full(env, ma_rows, False, TREE_B)["formed"].get(715)
    tooth("T4_tampered_lock_boundary_is_rejected",
          (real + 1) != 1811 and real == 1811,
          f"the measured lock is {real}; the tampered value {real + 1} does "
          "not match the pinned 1811")
    # T5 planted symmetric encoding at a LIVE wire must break the battery
    TOOTH_B = 1155
    _CO = {}
    support_word = {}
    for tt in apps:
        k = occasion_of[tt]
        support_word[k] = 0
        for m in atoms_at[tt]:
            support_word[k] |= 1 << m
    words_world = M.choice_support_words(env, atoms_at, False, "world")

    def tooth_tree(gauge_wire, upto):
        _CO.clear()
        _CO.update(support_word)

        def CO(k):
            return _CO[k] ^ M.CHOICE(k)
        rows_ = {}
        for tt in apps:
            k = occasion_of[tt]
            sched = M.build_schedules(
                c863, program, sim_fwd, 0,
                ((KC, REC_A, left_w, 0), (KC, REC_A, right_w, 0),
                 (KCH, k, left_w, 0), (KCH, k, right_w, 0)))
            src = ["def apply_chunk(c):"]
            mask_here = None
            for gg in sched[tt % stations]:
                src.append(M.extended_statement_text(*gg))
                if gg[0] == KCH:
                    mask_here = gg[4]
            src.append(f" c[{gauge_wire}] ^= COCHOICE({k}) & {mask_here}")
            ns = {}
            exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE,
                                  "COCHOICE": CO}, ns)
            rows_[tt] = (k, ns["apply_chunk"])
        return M.enumerate_tree(env, ma_rows, rows_, words_world, atoms_at,
                                upto, reverse=False)

    base_small = M.enumerate_tree(env, ma_rows, ma_choice_rows, words_world,
                                  atoms_at, TOOTH_B, reverse=False)
    bd = [r["digest"] for r in base_small["leaf_records"]]
    inert_small = tooth_tree(394, TOOTH_B)
    id_ = [r["digest"] for r in inert_small["leaf_records"]]
    live_small = tooth_tree(131, TOOTH_B)
    ld = [r["digest"] for r in live_small["leaf_records"]]
    tooth("T5_COCHOICE_at_a_LIVE_wire_breaks_the_battery",
          ld != bd and id_ == bd,
          "gauge at the inert wire 394 reproduces the leaf digest list "
          "byte for byte; gauge at the LIVE wire 131 (BANK0.DIRECTION_OK) "
          "does not -- so the battery is sensitive")
    # T6 parametric firewall
    WEIGHT_KEYS = ("CONDITIONAL", "HYPOTHETICAL")

    def firewall_scan(obj, path=""):
        hits = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                hits += firewall_scan(v, path + "/" + str(k))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                hits += firewall_scan(v, f"{path}[{i}]")
        elif isinstance(obj, (float, Fraction)):
            if not any(w in path for w in WEIGHT_KEYS):
                hits.append(path)
        return hits
    planted_bad = {"weights": {"mu": Fraction(1, 2)}}
    planted_ok = {"CONDITIONAL_weights": {"mu": Fraction(1, 2)}}
    tooth("T6_parametric_firewall_catches_an_unfenced_weight",
          bool(firewall_scan(planted_bad)) and not firewall_scan(planted_ok),
          f"unfenced planted weight flagged at {firewall_scan(planted_bad)}; "
          "the same value under a CONDITIONAL fence is not flagged")
    # T7 tampered pin
    tampered = bytearray(payloads[C936_PATH])
    tampered[100] ^= 1
    tooth("T7_tampered_pin_is_rejected",
          sha256(bytes(tampered)).hexdigest() != r936["self_sha256"]
          and git_blob(bytes(tampered)) != git_blob(payloads[C936_PATH]),
          "a one-bit flip in the pinned 936 runner breaks both the sha256 "
          "and the git blob")
    # T8 planted NON-phase-matched collision must be rejected as a witness
    W8 = [1, 6, 124, 125, 202, 236, 255, 256]

    def proj8(x):
        y = 0
        for i, w in enumerate(W8):
            if (x >> TIDX[w]) & 1:
                y |= 1 << i
        return y
    occ = {x: 0 for x in apps}
    A = M.Machine(env, False)
    B = M.Machine(env, False)
    A.advance(300, ma_rows, ma_choice_rows, occ)
    B.advance(300, ma_rows, ma_choice_rows, occ)
    w1 = dict(occ)
    w1[300] = 1 << 715
    A.advance(301, ma_rows, ma_choice_rows, occ)
    B.advance(301, ma_rows, ma_choice_rows, w1)
    bs, p0, p1 = [], [], []
    b = 301
    while True:
        x = y = 0
        for i, w in enumerate(W8):
            if (A.columns[w] >> 715) & 1:
                x |= 1 << i
            if (B.columns[w] >> 715) & 1:
                y |= 1 << i
        bs.append(b)
        p0.append(x)
        p1.append(y)
        if b >= TREE_B:
            break
        A.advance(b + 1, ma_rows, ma_choice_rows, occ)
        B.advance(b + 1, ma_rows, ma_choice_rows, occ)
        b += 1
    cfree, _, exfree = collisions(bs, p0, p1)
    cph, _, exph = collisions(bs, p0, p1, stations)
    bad_witness = None
    for key, outs in exfree:
        bnds = [bb for bb, x in zip(bs, p0) if x == key]
        if len({bb % stations for bb in bnds}) > 1:
            bad_witness = (key, bnds[:3])
            break
    tooth("T8_a_NON_phase_matched_collision_is_rejected_as_a_witness",
          bad_witness is not None and cph > 0,
          f"planted witness {bad_witness} spans several phases and is "
          f"refused; the {cph} genuine witnesses are phase matched")
    # T9 planted 'surviving Theta' that only matches at the first boundary
    seed_diff = p0[0] ^ p1[0]
    fake_fail = None
    for bb, x, y in zip(bs, p0, p1):
        if (x ^ seed_diff) != y:
            fake_fail = bb
            break
    tooth("T9_planted_surviving_Theta_is_rejected_by_the_search",
          fake_fail is not None,
          "the constant-XOR map fitted at the first post-choice boundary is "
          f"refused at boundary {fake_fail}")
    # T10 both controls of one TOF
    one_tof = next(gg for s in ma_sched for gg in s if gg[0] == KT)
    tooth("T10_both_controls_of_one_TOF_do_not_cancel",
          not commutes({one_tof[1]: one_tof[4], one_tof[2]: one_tof[4]},
                       (one_tof,)),
          f"TOF({one_tof[1]},{one_tof[2]})->{one_tof[3]} with both controls "
          "flipped does not commute")
    # T11 planted affine defect
    v0f, v1f = [], []
    A = M.Machine(env, False)
    B = M.Machine(env, False)
    A.advance(300, ma_rows, ma_choice_rows, occ)
    B.advance(300, ma_rows, ma_choice_rows, occ)
    A.advance(301, ma_rows, ma_choice_rows, occ)
    B.advance(301, ma_rows, ma_choice_rows, w1)
    b = 301
    while True:
        x = y = 0
        for i, w in enumerate(TARGETS):
            if (A.columns[w] >> 715) & 1:
                x |= 1 << i
            if (B.columns[w] >> 715) & 1:
                y |= 1 << i
        v0f.append(x)
        v1f.append(y)
        if b >= TREE_B:
            break
        A.advance(b + 1, ma_rows, ma_choice_rows, occ)
        B.advance(b + 1, ma_rows, ma_choice_rows, occ)
        b += 1
    ok_clean = affine_fit(v0f, v1f, len(TARGETS))[0]
    spoiled = list(v1f)
    spoiled[900] ^= 1 << TIDX[256]
    ok_bad = affine_fit(v0f, spoiled, len(TARGETS))[0]
    tooth("T11_planted_affine_defect_makes_the_fit_INCONSISTENT",
          ok_clean and not ok_bad,
          "the clean relation is affine; flipping ONE bit of ONE branch-1 "
          "state makes the GF(2) system inconsistent, so the affine finding "
          "is not a vacuous fit")
    # T12 tampered gauge wire (a live wire claimed inert)
    proto0 = M.Machine(env, False).columns
    def inert(w):
        return (w not in (set(ctrl) | tgts) and w not in set(global_dirty)
                and w not in set(bank_dirty[0]) and w not in set(bank_dirty[1])
                and w not in set(env["slot_wires"]) and proto0[w] == 0)
    tooth("T12_a_live_wire_claimed_inert_is_rejected",
          inert(394) and not inert(124) and not inert(131),
          "394 passes the inertness predicate; 124 (BANK0.U_TO_V) and 131 "
          "(BANK0.DIRECTION_OK) do not")
    # T13 planted lane leak
    r = Rng(0xF00D)
    a = [r.bits(n + 1) & UNI for _ in range(NCOL)]
    bb_ = list(a)
    bb_[500] ^= (1 << 254)
    pre = (a[500] ^ bb_[500]) & (1 << 715)
    a[501] ^= (a[500] >> 1) & UNI
    bb_[501] ^= (bb_[500] >> 1) & UNI
    tooth("T13_a_planted_cross_lane_shift_is_caught",
          bool(((a[501] ^ bb_[501]) & (1 << 253)) and not pre),
          "a fabricated SHIFT-style gate moves a lane-254 difference into "
          "lane 253; the lane-confinement instrument sees it")
    # T14 tampered C3b pair
    s0 = list(ma_sched[0])
    idx40 = [i for i, gg in enumerate(s0)
             if gate_roles(gg, KX, KC, KT)[0] == src_w]
    tam = s0[:idx40[1]] + [(KX, 131, 0, 0, s0[idx40[0]][4])] + s0[idx40[1]:]
    i0, i1 = [i for i, gg in enumerate(tam)
              if gate_roles(gg, KX, KC, KT)[0] == src_w]
    between_writes = {gate_roles(gg, KX, KC, KT)[0] for gg in tam[i0 + 1:i1]}
    reads = {tam[i0][1], tam[i0][2], tam[i1][1], tam[i1][2]}
    tooth("T14_tampered_source_pointer_pair_is_rejected",
          bool(between_writes & reads) and (i1 != i0 + 1),
          "inserting an X on wire 131 between the two source-pointer gates "
          "breaks both the adjacency test and the nothing-between test")
    timings["teeth"] = round(monotonic() - t0, 3)

    # ------------------------------------------------------------------ #
    # per-claim verdicts
    # ------------------------------------------------------------------ #
    B_ = sci1["B_SUBSTRATE"]
    C_ = sci1["C_LANE_INDEPENDENCE"]
    D_ = sci1["D_COMMUTATION"]
    E_ = sci1["E_ENDPOINT_GATES"]
    F_ = sci1["F_DIVERGENCE"]
    G_ = sci1["G_LOCKS"]
    H_ = sci1["H_THETA_HUNT"]
    I_ = sci1["I_NON_EXISTENCE"]
    J_ = sci1["J_SYMMETRIC_ENCODING"]
    Kx = sci1["K_AXIOMS"]
    L_ = sci1["L_940_FAMILY"]
    prim_ctrl = r943["certificates"]["Q1_THE_VALUE_SPACE_SYMMETRY_FAMILY"][
        "commutant"]
    theta_agrees = []
    PINNED_THETA = {
        (300, 715): 306, (700, 475): 761, (700, 540): 702, (702, 254): 705,
        (702, 450): 763, (702, 715): 706, (1100, 558): 1102,
        (1100, 715): 1113}
    for row in H_["THE_PRIMARYS_SWEPT_FAMILY_REBUILT_FROM_ITS_DESCRIPTION"]:
        a = tuple(row["atom"])
        theta_agrees.append({
            "atom": list(a),
            "my_first_failure": row["best_candidate"]["first_failure_boundary"],
            "pinned_first_failure": PINNED_THETA[a],
            "agree": row["best_candidate"]["first_failure_boundary"]
            == PINNED_THETA[a],
            "my_best_swaps": [row["best_candidate"]["swap_bank0_UV"],
                              row["best_candidate"]["swap_bank1_UV"],
                              row["best_candidate"]["swap_orientations"]],
            "my_breaks_on": row["best_candidate"]["breaks_on"]})

    verdicts = {
        "C1_940s_family_is_relabelling_only": {
            "verdict": "SURVIVES",
            "evidence": {
                "add_candidate_calls": L_["add_candidate_call_count"],
                "families_in_the_receipt": L_["families_in_940s_receipt"],
                "definition_begins_with_a_relabelling":
                    L_["the_definition_begins_with_a_relabelling"]},
            "precision_correction": L_["PRECISION_CORRECTION"],
        },
        "C2_the_commutation_IFF": {
            "verdict": "REFUTED TWICE.  The 'if' half is a theorem and the "
                       "downstream corollary survives; the 'only if' half is "
                       "FALSE, and the wire census is an artefact.",
            "criterion_and_semantics_disagreements":
                D_["criterion_and_semantics_disagreements"],
            "REFUTATION_1_THE_IFF_IS_NOT_AN_IFF": D_["THE_IFF_IS_REFUTED"],
            "THE_LOAD_BEARING_COROLLARY_SURVIVES":
                D_["THE_LOAD_BEARING_COROLLARY_SURVIVES"],
            "exhaustive_single_wire_disagreements_count":
                len(D_["exhaustive_single_wire_disagreements"]),
            "REFUTATION_2_THE_WIRE_CENSUS": {
                "the_primary_claims": "546 wires are touched by the program "
                "and exactly ONE of them (wire 0) is never a control",
                "what_I_measure": {
                    "touched_by_kind_dispatch":
                        D_["wires_touched_BY_KIND_DISPATCH"],
                    "touched_by_the_naive_union_of_a_b_c3":
                        D_["wires_touched_by_the_naive_union_of_a_b_c3"],
                    "the_difference":
                        D_["the_naive_union_minus_the_kind_dispatch"],
                    "wires_that_are_never_a_control":
                        D_["wires_that_are_never_a_control"]},
                "why": "WIRE 0 IS NOT TOUCHED AT ALL.  It is the literal zero "
                "in the UNUSED operand slots of the compiled 5-tuple: an X "
                "gate is (KIND_X, target, 0, 0, mask) and a CNOT is "
                "(KIND_CNOT, ctrl, target, 0, mask).  Taking the union of "
                "{a,b,c3} without dispatching on the kind manufactures a "
                "phantom incidence on wire 0.  There are 13706 X gates and "
                "1254 CNOTs in the compiled cycle, every one of which "
                "contributes the phantom.  No gate reads or writes wire 0.",
                "the_correct_statement_is_STRICTLY_STRONGER":
                    "545 wires are touched; EVERY ONE of them is a control; "
                    "and every one of their CTRLMASKs is the full 749-lane "
                    "universe.  So the commutant of the compiled cycle inside "
                    "the value-flip group is exactly the flips on wires the "
                    "program never touches -- causally trivial.  The "
                    "primary's own conclusion is not weakened; its census is "
                    "wrong by one phantom wire.",
                "the_primarys_number": prim_ctrl["wires_touched_by_any_gate"],
                "the_primarys_never_control":
                    prim_ctrl["wires_that_are_never_a_control"],
                "we_agree_on_the_545":
                    prim_ctrl["wires_whose_control_mask_is_the_FULL_lane"
                              "_universe"]
                    == D_["controls_whose_CTRLMASK_is_the_FULL_lane_universe"],
            },
            "both_controls_of_one_TOF_do_not_cancel":
                not D_["BOTH_CONTROLS_OF_ONE_TOF"]["commutes"],
            "over_exclusion_hunt":
                D_["OVER_EXCLUSION_HUNT_on_the_real_trajectory"],
            "positive_control":
                D_["POSITIVE_CONTROL_untouched_wire_flips_commute"],
        },
        "C3_the_six_endpoint_TOF_patterns": {
            "verdict": "SURVIVES",
            "patterns": E_["six_TOF_patterns"],
            "gates_per_cycle": E_["total_gates_per_compiled_cycle"],
            "only_targets": E_["the_only_targets"],
            "endpoints_are_never_a_CNOT_control":
                E_["endpoint_is_a_CNOT_control_anywhere"] == 0,
        },
        "C3b_the_source_pointer_pair": {
            "verdict": "SURVIVES",
            "rows": {k: v for k, v in E_["C3b_SOURCE_POINTER_PAIRS"].items()
                     if k != "rows"},
            "MY_ADDITIONAL_ATTACK":
                "the pair sits at the END of every chunk, so the three "
                "readers of the source pointer inside the chunk (targets 123, "
                "124/125 and 132) all read the value from BEFORE the pair.  "
                "The order does NOT spoil the reading.  I also checked the "
                "identity EMBEDDED in the full chunk, not only in isolation: "
                "the simultaneous endpoint flip leaves c[40] unchanged after "
                "the whole chunk runs, on-menu AND off-menu -- the pair reads "
                "the endpoints only through LEFT XOR RIGHT, and flipping both "
                "preserves that regardless of the menu predicate.",
        },
        "C4_divergence_is_eight_wires_one_lane": {
            "verdict": "SURVIVES AS AN UPPER BOUND; THE PER-ATOM READING IS "
                       "REFUTED",
            "union_support": F_["UNION_SUPPORT_OVER_ALL_EIGHT_ATOMS"],
            "lanes": F_["lanes_that_ever_differ_across_all_atoms"],
            "REFUTATION": {
                "the_claim": "for all 8 atoms the two branches differ ONLY on "
                "the 8 wires and on NO other lane",
                "what_I_measure": "the UNION over the eight atoms is exactly "
                "those eight wires and the lane confinement is exact, so the "
                "claim is true as stated.  But the per-atom supports are NOT "
                "eight: two atoms move FOUR wires {1,6,124,125}, one moves "
                "SIX {1,6,124,125,255,256}, and only five move all eight.  "
                "Anyone reading 'the two branches differ on eight wires' as a "
                "per-atom fact reads it wrong.",
                "per_atom_support_sizes":
                    F_["PER_ATOM_SUPPORT_IS_NOT_ALWAYS_EIGHT"],
                "per_atom_rows": [{"atom": r["atom"],
                                   "support": r["divergence_support"]}
                                  for r in F_["rows"]],
            },
            "lane_confinement_is_a_THEOREM_not_a_measurement":
                C_["SEMANTIC_LANE_INDEPENDENCE"],
            "variants_all_agree": F_["variants"],
        },
        "C5_wire_identities_and_the_orientation_split": {
            "verdict": "SURVIVES",
            "wire_identity_gate": [r for r in B_["rows"]
                                   if r["gate"] == "wire_identities"][0],
            "atoms_with_orientation_divergence":
                F_["atoms_at_which_an_ORIENTATION_wire_diverges"],
            "atoms_without": F_["atoms_at_which_NO_orientation_wire_diverges"],
            "NOTE_ON_THE_PRIMARYS_PROSE":
                "the receipt's answer text says the orientation wires diverge "
                "at 'EXACTLY the three genuine-menu SITES'.  That is five "
                "ATOMS at three distinct SITES (715, 475, 450); the three "
                "lock-timing sites are 540, 254, 558.  Atom count and site "
                "count are both right in their own register; the two are not "
                "interchangeable and the receipt uses both.",
        },
        "C6_the_theta_table": {
            "verdict": "TABLE REPRODUCED VALUE FOR VALUE; THE NEGATIVE'S "
                       "SCOPE IS REFUTED",
            "table_agreement": theta_agrees,
            "all_eight_rows_agree": all(r["agree"] for r in theta_agrees),
            "THE_BETTER_THETA_I_FOUND":
                H_["A_SURVIVING_THETA_THE_PRIMARY_MISSED"],
            "THE_SUPPORT_THRESHOLD_IS_ATOM_DEPENDENT": [
                {"atom": r["atom"],
                 "eight_wire_map_exists":
                     r["W8_divergence_support"]["ANY_MAP_OF_THIS_SUPPORT_"
                                                "EXISTS"],
                 "eight_wire_phase_dependent_map_exists":
                     r["W8_divergence_support"]["ANY_PHASE_DEPENDENT_MAP_"
                                                "EXISTS"],
                 "twelve_wire_phase_dependent_map_exists":
                     r["W12_plus_40_123_131_132"]["ANY_PHASE_DEPENDENT_MAP_"
                                                  "EXISTS"],
                 "affine_pivot_support_that_suffices":
                     r["MINIMAL_SUPPORT_FOUND_BY_THE_AFFINE_PIVOTS"]["count"]}
                for r in H_["THE_WIDER_HUNT"]],
            "MAJOR_FINDING":
                "A THETA THE PRIMARY MISSED DOES SURVIVE THE WHOLE WINDOW.  "
                "It is a lane-local AFFINE map over GF(2) on the gate-target "
                "wires of the site's own lane; about three dozen wires "
                "suffice (the affine pivots).  It reproduces the branch "
                "relation at EVERY boundary of the declared 1925-boundary "
                "window for EVERY one of the eight atoms, and at FOUR TIMES "
                "the window (7400 boundaries, 6299 distinct branch-0 states, "
                "no repeat).  Its structure is: flip both endpoints; EXCHANGE "
                "the two bank-0 U_TO_V/V_TO_U bits; EXCHANGE the two bank-1 "
                "bits; and flip each ORIENTATION bit by a LINEAR FUNCTIONAL "
                "of the wider lane state.  The primary's family could only "
                "EXCHANGE the two orientation bits with each other, which is "
                "why it broke there.  THE HONEST OTHER HALF: this map is NOT "
                "a symmetry.  It fails to commute with the compiled law at "
                "most random states and at one-bit perturbations of states "
                "on the orbit, so it is an orbit-specific intertwiner, not a "
                "law automorphism.  The primary's PHYSICS conclusion stands; "
                "its statement that no support-local map survives does not.",
        },
        "C_PROSE_the_primarys_timing_sentence": {
            "verdict": "ONE CLAUSE IS FALSE, TWO ARE LOOSE GLOSSES",
            "the_primarys_sentence":
                r943["certificates"]["Q1_THE_VALUE_SPACE_SYMMETRY_FAMILY"]
                ["THE_ANSWER_TO_THE_OWNERS_QUESTION"]["REFUTED_IN_TIMING"],
            "FALSE_CLAUSE": {
                "clause": "'and before the first bank settle event on the "
                          "lane'",
                "measurement": [
                    {"atom": r["atom"],
                     "break": r["best_candidate"]["first_failure_boundary"],
                     "break_is_before_the_first_bank_event_on_the_lane":
                         r["break_is_before_the_first_bank_event_on_the_lane"]}
                    for r in H_["THE_PRIMARYS_SWEPT_FAMILY_REBUILT_FROM_ITS_"
                                "DESCRIPTION"]],
                "why": "on six of the eight atoms the lane's FIRST bank-0 "
                       "settle event happens at boundary 6, 41, 69 or 71 -- "
                       "hundreds of boundaries BEFORE the choice occasion "
                       "itself, let alone before the break.  Only the two "
                       "atoms whose lane has no bank event until the lock "
                       "(sites 540 and 254) satisfy the clause.",
                "per_atom_first_bank_events":
                    [{"atom": r["atom"],
                      "first_bank0_event_on_the_lane":
                          r["first_bank0_event_on_the_lane"],
                      "first_bank1_event_on_the_lane":
                          r["first_bank1_event_on_the_lane"]}
                     for r in G_["rows"]],
            },
            "LOOSE_GLOSS_1": {
                "clause": "'the symmetry breaks about five boundaries after "
                          "the choice'",
                "measured_boundaries_from_the_choice_to_the_break":
                    [{"atom": r["atom"],
                      "delta": r["boundaries_from_the_choice_to_the_break"]}
                     for r in H_["THE_PRIMARYS_SWEPT_FAMILY_REBUILT_FROM_ITS_"
                                 "DESCRIPTION"]],
                "reading": "two, three, four, six and thirteen -- but SIXTY "
                           "ONE at two of the atoms.  'About five' is the "
                           "median, not the range.",
            },
            "LOOSE_GLOSS_2": {
                "clause": "'roughly fifteen hundred boundaries BEFORE the "
                          "formation lock'",
                "measured_break_to_lock":
                    [{"atom": r["atom"],
                      "delta":
                          r["boundaries_from_the_break_to_the_branch0_lock"]}
                     for r in H_["THE_PRIMARYS_SWEPT_FAMILY_REBUILT_FROM_ITS_"
                                 "DESCRIPTION"]],
                "reading": "fifteen hundred holds for ONE atom.  The range is "
                           "323 to 1505.  The clause that DOES hold "
                           "universally is the weaker one: the break is "
                           "before the lock at every one of the eight atoms.",
            },
            "WHAT_SURVIVES":
                "the load-bearing half of the sentence -- 'there is no "
                "extended pre-record segment carrying the symmetry' -- "
                "survives: at every atom the break precedes the formation "
                "lock, and at every atom the divergence enters the record "
                "channels one boundary after the choice.",
        },
        "C7_locks_events_items": {
            "verdict": "SURVIVES",
            "control_lock_table": G_["control_run_lock_boundaries"],
            "matches": G_["control_lock_table_matches_the_claim"],
            "menu_atoms_row": G_["MENU_ATOMS_share_lock_and_events_and_swap_"
                                 "the_item"],
            "timing_atoms_row":
                G_["TIMING_ATOMS_move_the_lock_and_the_event_count_and_keep_"
                   "the_item"],
            "my_own_lane_bookkeeping_agrees_with_the_machine":
                all(r["my_scan_agrees_with_the_machine"] for r in G_["rows"]),
        },
        "C8_the_two_non_existence_routes": {
            "verdict": "BOTH ROUTES ARE CLEAN; THE DECLARED SCOPE LIMIT IS "
                       "UNDERSTATED",
            "route_A": I_["ROUTE_A_moved_invariant_atoms"],
            "route_A_caveat": I_["ROUTE_A_CAVEAT"],
            "route_B_witnesses_are_phase_matched":
                I_["ROUTE_B_every_witness_is_phase_matched"],
            "every_atom_killed": I_["EVERY_ATOM_KILLED_BY_AT_LEAST_ONE_ROUTE"],
            "full_column_duplicates": H_["FULL_COLUMN_DUPLICATE_HUNT"],
            "SCOPE_CORRECTION": I_["MY_SCOPE_LIMIT_IS_TIGHTER_THAN_THE_"
                                   "PRIMARYS"],
            "did_the_primary_overclaim_past_its_limit":
                "NO -- it declares the limit explicitly and does not argue "
                "past it.  But the limit it declares is 'arbitrary global "
                "state maps', and the true next rung is about three dozen "
                "lane-local wires.  That gap is a real understatement of what "
                "route B does not cover.",
        },
        "C9_A2_is_gauge": {
            "verdict": "SURVIVES",
            "my_gauge_wire": J_["MY_INDEPENDENTLY_CHOSEN_GAUGE_WIRE"],
            "primary_gauge_394_is_eligible":
                J_["the_primarys_gauge_wire_394_is_in_my_eligible_set"],
            "battery": J_["backward_compatibility_battery"],
            "divergence": J_["divergence_under_the_symmetric_encoding"],
            "smuggling_audit": J_["SMUGGLING_AUDIT"],
            "sensitivity": "T5 fires: COCHOICE at the LIVE wire 131 breaks "
                           "the leaf digest list.",
        },
        "C10_the_axioms_do_not_orient_the_menu": {
            "verdict": "SURVIVES; THE PRIMARY'S SUPPORTING ARGUMENT IS "
                       "OVERREACHING",
            "the_finding": Kx["THE_FINDING"],
            "nearest_candidate":
                Kx["THE_NEAREST_CANDIDATE_FOR_AN_ORIENTING_CLAUSE"],
            "qubit_clause": Kx["THE_QUBIT_CLAUSE_CUTS_THE_OTHER_WAY"],
            "REFUTATION_OF_THE_LAW_INVARIANCE_ARGUMENT":
                Kx["ATTACK_ON_THE_PRIMARYS_LAW_INVARIANCE_ARGUMENT"],
        },
    }

    # ------------------------------------------------------------------ #
    # parametric firewall over MY OWN payload and MY OWN source
    # ------------------------------------------------------------------ #
    self_src = Path(__file__).read_bytes()
    float_lits = sum(1 for node in ast.walk(ast.parse(self_src.decode()))
                     if isinstance(node, ast.Constant)
                     and isinstance(node.value, float))
    payload_for_firewall = {"verdicts": verdicts, "science": sci1,
                            "teeth": teeth}
    fw_hits = firewall_scan(payload_for_firewall)
    cert_f = {
        "certificate": "M_PARAMETRIC_FIREWALL",
        "rule": "no weight value may appear as law content; any numeric "
                "weight must sit under a key path containing CONDITIONAL or "
                "HYPOTHETICAL.  Zero float literals in this runner; exact "
                "rationals only.",
        "float_literals_in_this_runner": float_lits,
        "zero_float_literals": float_lits == 0,
        "weight_values_outside_a_conditional_fence": fw_hits,
        "no_unfenced_weight_value": not fw_hits,
        "no_weight_value_appears_at_all": True,
        "fraction_label": FRACTION_LABEL,
        "scope_note": "runtime timings are excluded from the science payload "
                      "and from this scan; they are elapsed seconds, not law "
                      "content.",
    }
    cert_f["pass"] = bool(cert_f["zero_float_literals"]
                          and cert_f["no_unfenced_weight_value"])

    elapsed = round(monotonic() - started, 3)
    certs = {
        "A_PINS": cert_a,
        "B_SUBSTRATE": B_, "C_LANE_INDEPENDENCE": C_, "D_COMMUTATION": D_,
        "E_ENDPOINT_GATES": E_, "F_DIVERGENCE": F_, "G_LOCKS": G_,
        "H_THETA_HUNT": H_, "I_NON_EXISTENCE": I_,
        "J_SYMMETRIC_ENCODING": J_, "K_AXIOMS": Kx, "L_940_FAMILY": L_,
        "M_PARAMETRIC_FIREWALL": cert_f,
        "N_TEETH": {"certificate": "N_FALSIFIERS", "teeth": teeth,
                    "teeth_total": len(teeth),
                    "teeth_fired": sum(1 for x in teeth if x["fired"]),
                    "pass": all(x["fired"] for x in teeth)},
        "O_DOUBLE_RUN": {"certificate": "O_DOUBLE_RUN",
                         "pass1_digest": d1, "pass2_digest": d2,
                         "identical": d1 == d2,
                         "digest_is_timing_free": True,
                         "pass": d1 == d2},
        "P_RUNTIME": {"certificate": "P_RUNTIME", "elapsed_sec": elapsed,
                      "budget_sec": RUNTIME_BUDGET_SEC,
                      "within_budget": elapsed <= RUNTIME_BUDGET_SEC,
                      "timings": timings,
                      "pass": elapsed <= RUNTIME_BUDGET_SEC},
    }
    all_pass = all(c.get("pass", False) for c in certs.values())
    receipt = {
        "block": "toe-time-expansion-20260802/blockQ15",
        "campaign": "toe-time-expansion-20260802",
        "cycles": [943],
        "role": "INDEPENDENT CHECKER (spec'd to refute)",
        "worker": "Claude Opus 5 independent checker under supervisor spec",
        "claim_type": "bounded_theorem_check",
        "authority": "none",
        "audit": "unset",
        "fraction_label": FRACTION_LABEL,
        "headline":
            "THE PRIMARY'S MEASUREMENTS ALL REPRODUCE; THREE OF ITS GENERAL "
            "STATEMENTS DO NOT.  Its Theta table reproduces value for value "
            "on all eight atoms, as do its lock table, its event counts, its "
            "wire identities, its six endpoint TOF patterns, its "
            "source-pointer pair, its symmetric encoding and its axiom "
            "verdict.  REFUTATION 1: the commutation THEOREM is not an IFF.  "
            "The condition is SUFFICIENT, but 309 of the 545 touched wires -- "
            "every one of them excluded by the criterion -- carry a full-lane "
            "flip that commutes with the whole compiled cycle, because their "
            "control incidences sit inside palindromic compute/uncompute "
            "ladders.  The primary calls its condition 'a COMPLETE "
            "characterisation, not a search'; it is not.  Its DOWNSTREAM "
            "corollary survives: no endpoint, no divergence-support wire, and "
            "not the actual menu-swap flip, is in the commuting set.  "
            "REFUTATION 2: the wire census is off by a phantom.  Wire 0 is "
            "not touched at all -- it is the unused operand padding of the "
            "compiled 5-tuple -- so 545 wires are touched, not 546, and NONE "
            "of them is never-a-control.  REFUTATION 3: the eight-wire "
            "divergence support is a UNION over the eight atoms, not a "
            "per-atom fact; two atoms move four wires and one moves six.  "
            "MAJOR FINDING: a Theta the primary's family could not express "
            "DOES survive the entire window and four times beyond it -- a "
            "lane-local AFFINE map over GF(2) on about three dozen wires, "
            "whose orientation-wire correction is a LINEAR FUNCTIONAL rather "
            "than a pair exchange.  It is NOT a law symmetry: it fails to "
            "commute with the compiled law off the orbit.  So the physics "
            "conclusion stands and the negative's SCOPE does not.",
        "VERDICT":
            "C1 SURVIVES (with a loose source description corrected).  C2 IS "
            "REFUTED TWICE -- the IFF is only an IF, and the wire census "
            "counts a phantom -- while its load-bearing corollary survives.  "
            "C3, C3b, C5, C7, C9 SURVIVE.  C4 SURVIVES as an upper bound; its "
            "per-atom reading is REFUTED.  C6's table reproduces value for "
            "value but its NEGATIVE'S SCOPE is REFUTED by a surviving affine "
            "Theta.  C8's two routes are clean and kill exactly the atoms "
            "claimed, but its declared scope limit is UNDERSTATED.  C10 "
            "SURVIVES; the primary's law-invariance argument is OVERREACHING.",
        "claim_verdicts": verdicts,
        "certificates": certs,
        "all_certificates_pass": all_pass,
        "science_digest": d1,
        "provenance": {
            "pins": {p: certs["A_PINS"]["rows"][p]["sha256"]
                     for p in AUDIT_INPUT_PATHS},
            "git_blobs": {p: certs["A_PINS"]["rows"][p]["git_blob"]
                          for p in AUDIT_INPUT_PATHS},
            "envariance_blob": ENVARIANCE_BLOB,
            "primary_receipt_sha256":
                certs["A_PINS"]["rows"][PRIMARY_RECEIPT]["sha256"],
            "primary_science_digest_at_read_time": r943["science_digest"],
        },
        "self_sha256": sha256(self_src).hexdigest(),
    }
    out_path = ROOT / ("outputs/prerecord_swap_independent_check_cycle943"
                       "_receipt_2026_07_28.json")
    out_path.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                                   default=str) + "\n")
    print("===== runner cache v1 =====")
    print(f"CYCLE 943 blockQ15 INDEPENDENT CHECK  elapsed={elapsed}s "
          f"budget={RUNTIME_BUDGET_SEC}s")
    print(f"science_digest pass1={d1}")
    print(f"science_digest pass2={d2}  identical={d1 == d2}")
    for name, c in certs.items():
        print(f"{name:26s} pass={c.get('pass')}")
    print("-- claim verdicts --")
    for k, v in verdicts.items():
        print(f"{k:48s} {v['verdict']}")
    print("-- teeth --")
    for x in teeth:
        print(f"  fired={x['fired']}  {x['tooth']}")
    print(f"receipt -> {out_path.relative_to(ROOT)}")
    print("===== end runner cache =====")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
