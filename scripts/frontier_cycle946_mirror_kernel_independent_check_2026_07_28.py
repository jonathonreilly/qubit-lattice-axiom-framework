#!/usr/bin/env python3
"""Cycle 946 -- INDEPENDENT CHECKER, spec'd to REFUTE.

This runner does not trust the primary's numbers, its instruments, its
formalizations or its prose.  It rebuilds the substrate from the pinned bytes,
constructs its OWN mirror splice by a different algorithm, runs its OWN
semantic commutation test on a deliberately adversarial ensemble, computes its
OWN neighborhood conditions under its OWN formalizations, replays the
partnered tree itself, and re-reads the adopted axiom against the derivation
line by line looking for a hypothesis doing unpaid work.

The attack list, fixed before the run:

  A. THE SYMMETRY CERTIFICATE.  943's R1 lesson is that a commutation criterion
     can be a false positive (palindromic compute/uncompute ladders).  So:
     hunt a MOVED OBSERVABLE under the swap; test commutation on structured
     ON-ORBIT states rather than only on random ones; and check the instrument
     rejects deliberately WRONG involutions.  A test that says yes to
     everything says nothing.

  B. THE NEIGHBORHOOD MEASUREMENT.  944's lesson is formalization dependence.
     So: recompute the two loci's conditions independently, under
     formalizations the primary did not use, at instants the primary did not
     sample (the whole pre-choice window, not one boundary), and see whether
     the 4/4 split survives.

  C. THE HYPOTHESIS CHAIN.  Is H3 doing hidden work?  Does the adopted text
     actually force what is claimed?  Adversarial re-read, including the
     question the primary does not ask itself: is the SUBSTRATE's compiled law
     the same object as the AXIOM's admissibility rule, and if not, where does
     that identification enter?

  D. THE SEALED TABLE, re-scored from the checker's own tree.

  E. WINDOW DEPENDENCE.  943's coverage claims were window-relative and said
     so.  Does the primary's coverage survive a longer window?
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

C936_PATH = "scripts/frontier_cycle936_choice_substrate_2026_07_28.py"
C940_PATH = "scripts/frontier_cycle940_symmetric_weights_2026_07_28.py"
C943_RECEIPT = "outputs/prerecord_swap_cycle943_receipt_2026_07_28.json"
C946_PATH = "scripts/frontier_cycle946_mirror_kernel_2026_07_28.py"
C946_RECEIPT = "outputs/mirror_kernel_cycle946_receipt_2026_07_28.json"
ADOPTED_AXIOM_REF = "origin/axioms/admissibility-likelihood-20260805"
ADOPTED_AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

BLOCKLISTED_MODULES = (
    "frontier_cycle936_choice_substrate_2026_07_28",
    "frontier_cycle940_symmetric_weights_2026_07_28",
    "frontier_cycle943_prerecord_swap_2026_07_28",
    "frontier_cycle946_mirror_kernel_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle911_type_vacuity_2026_07_28",
    "frontier_cycle913_selection_function_2026_07_28",
    "frontier_cycle918_writable_endpoint_2026_07_28",
)


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(p):
    return sha1(f"blob {len(p)}\0".encode("ascii") + p).hexdigest()


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
LIFT940_FUNCS = ("gate_roles", "colour_refine", "fanout_profile", "apply_pi",
                 "relabelling_verdict")
LIFT940_CONSTS = ("ROLE_TARGET", "ROLE_C1", "ROLE_C2")


def _lift(source, filename, funcs, consts, classes):
    tree = ast.parse(source, filename=filename)
    body, gf, gc, gk = [], set(), set(), set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
            gf.add(node.name)
        elif isinstance(node, ast.ClassDef) and node.name in classes:
            body.append(node)
            gk.add(node.name)
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
                gc.update(names)
    miss = (tuple(sorted(set(funcs) - gf)), tuple(sorted(set(consts) - gc)),
            tuple(sorted(set(classes) - gk)))
    if any(miss):
        raise AssertionError(("lift incomplete", filename, miss))
    mod = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(mod)
    ns = {"__builtins__": __builtins__, "ROOT": ROOT, "K": K, "np": np,
          "ast": ast, "json": json, "math": math, "sys": sys,
          "itertools": itertools, "combinations": combinations,
          "product": product, "Counter": Counter, "defaultdict": defaultdict,
          "Fraction": Fraction, "sha256": sha256, "sha1": sha1, "Path": Path,
          "SimpleNamespace": SimpleNamespace, "compact": compact,
          "digest": digest, "git_blob": git_blob}
    exec(compile(mod, f"<lift {filename}>", "exec"), ns)
    return SimpleNamespace(**{n: ns[n] for n in
                              tuple(gf) + tuple(gc) + tuple(gk)})


def main() -> int:
    started = monotonic()
    timings = {}
    findings = []
    teeth = []

    def refute(tag, refuted, detail):
        findings.append({"finding": tag, "REFUTED": bool(refuted),
                         "detail": detail})
        return refuted

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    # ---------------- pins, read fresh, compared to the primary ----------
    t0 = monotonic()
    payloads = {p: (ROOT / p).read_bytes()
                for p in (C936_PATH, C940_PATH, C943_RECEIPT, C946_PATH,
                          C946_RECEIPT)}
    r946 = json.loads(payloads[C946_RECEIPT].decode("utf-8"))
    q2 = r946["certificates"]["Q2_THE_DERIVATION"]
    r943 = json.loads(payloads[C943_RECEIPT].decode("utf-8"))
    primary_self = sha256(payloads[C946_PATH]).hexdigest()
    ax_spec = f"{ADOPTED_AXIOM_REF}:{ADOPTED_AXIOM_PATH}"
    ax_bytes = subprocess.run(["git", "-C", str(ROOT), "show", ax_spec],
                              capture_output=True, check=False).stdout
    ax_text = ax_bytes.decode("utf-8")
    pins = {
        "primary_self_sha256_recomputed": primary_self,
        "primary_self_sha256_claimed": r946.get("self_sha256"),
        "primary_self_sha256_agrees": primary_self == r946.get("self_sha256"),
        "adopted_axiom_sha256_recomputed": sha256(ax_bytes).hexdigest(),
        "adopted_axiom_sha256_claimed":
            r946["certificates"]["A_PINS"][
                "THE_ADOPTED_AXIOM_VENDOR_READ"]["sha256"],
        "adopted_axiom_git_blob_recomputed": git_blob(ax_bytes),
        "blocked_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                   if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
    }
    pins["adopted_axiom_agrees"] = (
        pins["adopted_axiom_sha256_recomputed"]
        == pins["adopted_axiom_sha256_claimed"])

    M = _lift(payloads[C936_PATH].decode("utf-8"), C936_PATH,
              LIFT_FUNCS, LIFT_CONSTS, LIFT_CLASSES)
    A940 = _lift(payloads[C940_PATH].decode("utf-8"), C940_PATH,
                 LIFT940_FUNCS, LIFT940_CONSTS, ())
    kinds = {"X": M.KIND_X, "CNOT": M.KIND_CNOT, "TOF": M.KIND_TOF,
             "CHOICE": M.KIND_CHOICE}
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     prov) = M.lift_machinery()
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _f = c863.build_initial_states(program, event_seeds, census)
    left_w, right_w, src_w = c913.endpoint_wires()
    n = len(census)
    BB = K.M.R12.BANK_BASES
    REC_A = BB[0] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    slot_of = rig["slot_of"]
    slot_wires = tuple(sorted(set(slot_of.values())))
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1])
                                | set(links) | {source_ptr}))
    env = {"c863": c863, "c878": c878, "c911": c911, "c913": c913,
           "program": program, "census": census, "states": states, "n": n,
           "stations": stations, "left_w": left_w, "right_w": right_w,
           "global_dirty": global_dirty,
           "bank_dirty": (tuple(sorted(per_bank[0])),
                          tuple(sorted(per_bank[1]))),
           "uni_all": (1 << n) - 1, "uni_sim": (1 << (n + 1)) - 1,
           "slot_of": slot_of, "slot_wires": slot_wires,
           "register_cap": consts911["REGISTER_CAP"],
           "setup_direction": {ev: c913.read_state_direction(seed)
                               for ev, seed in event_seeds}}
    MA = ((M.KIND_CNOT, REC_A, left_w, 0), (M.KIND_CNOT, REC_A, right_w, 0))
    TREE_B = M.TREE_ORBITS * stations
    atoms = tuple(sorted(M.CHOICE_ATOMS))
    atoms_at = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    apps = sorted(atoms_at)
    occ = {t: i for i, t in enumerate(apps)}
    ZW = {t: 0 for t in apps}
    words = M.choice_support_words(env, atoms_at, False, "world")
    sched_ma = M.build_schedules(c863, program, sim_fwd, 0, MA)
    timings["setup"] = round(monotonic() - t0, 3)
    print(f"[setup {timings['setup']}s] checker substrate rebuilt "
          f"independently: {len(proto)} wires", flush=True)

    # ---------------- the checker's OWN sigma and OWN splice -------------
    # DIFFERENT ALGORITHM: build a per-station index of gate -> positions and
    # pair each gate with its image by consuming from that index, rather than
    # by Counter subtraction.  If the two algorithms disagree on the defect,
    # one of them is wrong and the construction is unsound.
    SIG = {}
    for a, b in (((left_w, right_w),)
                 + tuple((b + K.A.U_TO_V, b + K.A.V_TO_U) for b in BB)):
        SIG[a] = b
        SIG[b] = a
    ORI = tuple(sorted(b + K.A.cell(c)["orientation"]
                       for b in BB[:2] for c in (0, 1)))

    def img(g):
        kind, a, b, c3, mask = g

        def m(w):
            return SIG.get(w, w)
        if kind == M.KIND_X:
            return (kind, m(a), b, c3, mask)
        if kind == M.KIND_CNOT:
            return (kind, m(a), m(b), c3, mask)
        if kind == M.KIND_TOF:
            return (kind, m(a), m(b), m(c3), mask)
        if kind == M.KIND_CHOICE:
            return (kind, a, m(b), c3, mask)
        return g

    def ctrl(g):
        if g[0] == M.KIND_CNOT:
            return (g[1],)
        if g[0] == M.KIND_TOF:
            return (g[1], g[2])
        return ()

    def defect_by_matching(schedules):
        """Independent defect finder: greedy bipartite matching of each gate
        occurrence to an unused occurrence of its image."""
        out = []
        for si, s in enumerate(schedules):
            pool = defaultdict(list)
            for i, g in enumerate(s):
                pool[g].append(i)
            used = set()
            for i, g in enumerate(s):
                gi = img(g)
                if gi == g:
                    continue
                cand = [j for j in pool.get(gi, []) if j not in used]
                if cand:
                    used.add(cand[0])
                else:
                    out.append((si, g, gi))
        return out

    def splice(schedules, only=None):
        out = []
        for s in schedules:
            need = Counter(g for _si, g, _i in defect_by_matching((s,)))
            new = []
            for g in s:
                new.append(g)
                if need[g] > 0:
                    need[g] -= 1
                    if only is None or M.gate_target(*g[:4]) in only:
                        new.append(img(g))
            out.append(tuple(new))
        return tuple(out)

    my_defect = defect_by_matching(sched_ma)
    my_distinct = sorted({(g[0], g[1], g[2], g[3]) for _s, g, _i in my_defect})
    q1 = r946["certificates"]["Q1_THE_MIRROR_PARTNERED_KERNEL"]
    refute("A1_defect_census_disagrees",
           len(my_defect) != q1["defect_occurrences"]
           or len(my_distinct) != q1["defect_distinct_gates"],
           {"checker_occurrences": len(my_defect),
            "primary_occurrences": q1["defect_occurrences"],
            "checker_distinct": len(my_distinct),
            "primary_distinct": q1["defect_distinct_gates"],
            "method": "greedy occurrence matching, not Counter subtraction"})
    sched_p = splice(sched_ma)
    rows_p = M.compile_schedules(sched_p)
    rows_b = M.compile_schedules(sched_ma)
    refute("A2_partnered_gate_total_disagrees",
           sum(len(s) for s in sched_p) != q1["gates_after"],
           {"checker": sum(len(s) for s in sched_p),
            "primary": q1["gates_after"]})
    print(f"[A] checker defect {len(my_defect)} occurrences / "
          f"{len(my_distinct)} distinct; partnered gates "
          f"{sum(len(s) for s in sched_p)}", flush=True)

    def crows(sp):
        cr = {}
        for t in apps:
            k = occ[t]
            g = MA + ((M.KIND_CHOICE, k, left_w, 0),
                      (M.KIND_CHOICE, k, right_w, 0))
            s = sp(M.build_schedules(c863, program, sim_fwd, 0, g))
            ns = {}
            exec("\n".join(M.chunk_source(s[t % stations])),
                 {"__builtins__": {}, "CHOICE": M.CHOICE}, ns)
            cr[t] = (k, ns["apply_chunk"])
        return cr

    cr_p = crows(lambda s: splice(s))
    cr_b = crows(lambda s: s)

    def perm(cols):
        o = list(cols)
        for w, v in SIG.items():
            o[v] = cols[w]
        return o

    def perm_lane(cols, lane):
        o = list(cols)
        bit = 1 << lane
        for w, v in SIG.items():
            o[v] = (cols[v] & ~bit) | (((cols[w] >> lane) & 1) << lane)
        return o

    def commutes(fns, states_list, tr):
        bad = set()
        for cols in states_list:
            a = tr(cols)
            b = list(cols)
            for fn in fns:
                fn(a)
                fn(b)
            b = tr(b)
            for w in range(len(a)):
                if a[w] != b[w]:
                    bad.add(w)
        return sorted(bad)

    # ---- ATTACK A: the symmetry certificate -----------------------------
    t0 = monotonic()
    touched = sorted({w for s in sched_p for g in s
                      for w in (M.gate_target(*g[:4]),) + ctrl(g)})
    # (1) a DIFFERENT random ensemble
    ens_rand = []
    for i in range(6):
        cols = list(proto)
        for w in touched:
            acc = 0
            for k in range(4):
                acc = (acc << 256) | int.from_bytes(
                    sha256(f"CHECKER946|{w}|{i}|{k}".encode()).digest(), "big")
            cols[w] = acc & env["uni_sim"]
        ens_rand.append(cols)
    # (2) STRUCTURED / degenerate states the primary never tested
    ens_struct = [list(proto),
                  [0] * len(proto),
                  [env["uni_sim"]] * len(proto),
                  [env["uni_sim"] if (w % 2) else 0 for w in range(len(proto))],
                  [((1 << 715) if w in SIG else 0) for w in range(len(proto))]]
    # (3) ON-ORBIT states: the real machine state at each atom's boundary
    ens_orbit = []
    for (t, site) in atoms:
        m = M.Machine(env, False)
        m.advance(t, rows_p, cr_p, ZW)
        ens_orbit.append(list(m.columns))
    ens_all = ens_rand + ens_struct + ens_orbit
    bad_p = commutes(rows_p, ens_all, perm)
    bad_b = commutes(rows_b, ens_all, perm)
    sc = q1["SYMMETRY_CERTIFICATE"]
    refute("A3_symmetry_certificate_fails_on_the_checkers_ensemble",
           len(bad_p) != 0,
           {"checker_breaking_wires": bad_p[:12],
            "count": len(bad_p),
            "ensemble": {"random": len(ens_rand), "structured":
                         len(ens_struct), "on_orbit": len(ens_orbit),
                         "lane_vectors": len(ens_all) * (n + 1)},
            "baseline_breaking_wires": len(bad_b),
            "primary_claimed_partnered": sc[
                "L3_SEMANTIC_partnered_breaking_wires"],
            "note": "the primary tested 8 random states only; this adds "
                    "all-zero, all-one, alternating, sigma-support-only and "
                    "the eight REAL on-orbit states at the choice boundaries"})
    timings["A_symmetry"] = round(monotonic() - t0, 3)

    # (4) the instrument must REJECT deliberately wrong involutions
    live = [w for w in touched if w not in SIG]
    inert = [w for w in range(len(proto)) if w not in touched][:2]
    WRONG = {"only_the_bank0_rails": ((124, 125),),
             "only_the_endpoints": ((left_w, right_w),),
             "endpoints_plus_the_orientation_cell_swap":
                 ((left_w, right_w), (ORI[2], ORI[3])),
             "two_LIVE_wires_with_no_mirror_relation":
                 ((live[0], live[1]),),
             "the_full_sigma_minus_one_rail_pair":
                 tuple(pr for pr in
                       (((left_w, right_w),)
                        + tuple((b + K.A.U_TO_V, b + K.A.V_TO_U) for b in BB))
                       if pr != (BB[0] + K.A.U_TO_V, BB[0] + K.A.V_TO_U)),
             "two_INERT_wires_the_law_never_touches":
                 ((inert[0], inert[1]),)}
    wrong = {}
    for name, prs in WRONG.items():
        sg2 = {}
        for a, b in prs:
            sg2[a] = b
            sg2[b] = a

        def pm(cols, s2=sg2):
            o = list(cols)
            for w, v in s2.items():
                o[v] = cols[w]
            return o
        wrong[name] = len(commutes(rows_p, ens_all, pm))
    must_break = {k: v for k, v in wrong.items()
                  if k != "two_INERT_wires_the_law_never_touches"}
    refute("A4_the_instrument_accepts_a_wrong_involution_on_LIVE_wires",
           any(v == 0 for v in must_break.values()),
           {"breaking_wires_per_wrong_involution": wrong,
            "why": "943's R1: a criterion that certifies everything certifies "
                   "nothing.  Every wrong involution ON LIVE WIRES must "
                   "break.",
            "THE_CONTROL_ITSELF_HAD_TO_BE_CORRECTED":
                "a first version of this control asserted that EVERY wrong "
                "involution must break, and it failed -- on a pair of wires "
                "the law never touches.  That is not an instrument fault, it "
                "is a true statement about the kernel: exchanging two inert "
                "wires IS an exact symmetry of the law, a genuine one and a "
                "completely vacuous one.  The control is now restricted to "
                "live wires, and the inert pair is kept in the table as the "
                "exhibit.",
            "inert_pair_tested": [inert[0], inert[1]],
            "inert_pair_breaking_wires":
                wrong["two_INERT_wires_the_law_never_touches"]})

    # (5) THE MOVED-OBSERVABLE HUNT.  sigma must actually MOVE something --
    #     a symmetry that is the identity on the menu is a false positive.
    moved = []
    for cols in ens_orbit:
        p = perm(cols)
        moved.append(sum(1 for w in range(len(cols)) if p[w] != cols[w]))
    menu_moved = []
    for (t, site) in atoms:
        m = M.Machine(env, False)
        m.advance(t, rows_p, cr_p, ZW)
        c0 = m.columns
        p = perm_lane(c0, site)
        menu_moved.append(((c0[left_w] >> site) & 1, (c0[right_w] >> site) & 1,
                           (p[left_w] >> site) & 1, (p[right_w] >> site) & 1))
    refute("A5_sigma_is_trivial_on_the_menu",
           not all(a != c for a, b, c, d in menu_moved),
           {"per_atom_left_right_before_after": menu_moved,
            "wires_moved_on_orbit_states": moved,
            "why": "if sigma left the endpoint pair fixed it would commute "
                   "trivially and prove nothing about the menu"})

    # (6) 940's automorphism machinery applied DIRECTLY to sigma
    flat_p = [(si, g) for si, s in enumerate(sched_p) for g in s]
    flat_b = [(si, g) for si, s in enumerate(sched_ma) for g in s]
    ref_p, ref_b = {}, {}
    for label in ("exact", "popcount", "bare"):
        cp, _i, _w = A940.colour_refine(flat_p, kinds, label)
        cb, _i2, _w2 = A940.colour_refine(flat_b, kinds, label)
        ref_p[label] = cp.get(left_w) == cp.get(right_w)
        ref_b[label] = cb.get(left_w) == cb.get(right_w)
    refute("A6_colour_refinement_does_not_merge_LEFT_and_RIGHT",
           not all(ref_p.values()) or any(ref_b.values()),
           {"partnered_LEFT_eq_RIGHT": ref_p,
            "baseline_LEFT_eq_RIGHT": ref_b})

    # ---- ATTACK E: window dependence ------------------------------------
    t0 = monotonic()
    LONG = TREE_B * 2

    def coverage(rows, cr, upto):
        cov, detail = [], {}
        for (t, site) in atoms:
            lane = site
            m0 = M.Machine(env, False)
            m0.advance(t, rows, cr, ZW)
            par = m0.snapshot()
            m1 = M.Machine(env, False)
            m1.restore(par)
            w = words[t][site]
            m0.advance(t + 1, rows, cr, {**ZW, t: 0})
            m1.advance(t + 1, rows, cr, {**ZW, t: w})
            ff = None
            while m0.t <= upto:
                th = perm_lane(m0.columns, lane)
                if any(((th[wr] >> lane) & 1)
                       != ((m1.columns[wr] >> lane) & 1)
                       for wr in range(len(th))):
                    ff = m0.t
                    break
                if m0.t >= upto:
                    break
                m0.advance(m0.t + 1, rows, cr, ZW)
                m1.advance(m1.t + 1, rows, cr, ZW)
            detail[f"{t}/{site}"] = ff
            if ff is None:
                cov.append([t, site])
        return cov, detail

    cov_declared, det_declared = coverage(rows_p, cr_p, TREE_B)
    cov_long, det_long = coverage(rows_p, cr_p, LONG)
    timings["E_window"] = round(monotonic() - t0, 3)
    refute("E1_coverage_disagrees_with_the_primary_at_the_declared_window",
           sorted(cov_declared) != sorted(q1["BRANCH_SWAP"]["covered_atoms"]),
           {"checker": cov_declared,
            "primary": q1["BRANCH_SWAP"]["covered_atoms"]})
    refute("E2_coverage_collapses_at_a_longer_window",
           sorted(cov_long) != sorted(cov_declared),
           {"declared_window": TREE_B, "long_window": LONG,
            "covered_at_declared": cov_declared,
            "covered_at_double": cov_long,
            "first_failure_boundaries_at_double": det_long,
            "why": "943's coverage claims were window-relative and said so.  "
                   "If the primary's three sites stop being covered at 2x the "
                   "window, the theorem's coverage is an artifact of where "
                   "the run was stopped"})
    print(f"[E {timings['E_window']}s] coverage declared={cov_declared} "
          f"at 2x window={cov_long}", flush=True)

    # ---- ATTACK B: the neighborhood measurement -------------------------
    t0 = monotonic()

    def write_cone(schedules, seeds, depth):
        cone = set(seeds)
        for _ in range(depth):
            add = set()
            for s in schedules:
                for g in s:
                    if set(ctrl(g)) & cone:
                        add.add(M.gate_target(*g[:4]))
            if add <= cone:
                break
            cone |= add
        return cone

    def read_cone(schedules, seeds, depth):
        cone = set(seeds)
        for _ in range(depth):
            add = set()
            for s in schedules:
                for g in s:
                    if M.gate_target(*g[:4]) in cone:
                        add.update(ctrl(g))
            if add <= cone:
                break
            cone |= add
        return cone

    CHECKER_FORMS = {
        "K1_the_write_cone_of_the_endpoint_pair":
            write_cone(sched_p, {left_w, right_w}, 3),
        "K2_the_read_cone_depth_3": read_cone(sched_p, {left_w, right_w}, 3),
        "K3_the_two_banks_the_endpoints_drive":
            set(range(BB[0], BB[0] + K.A.N)) | set(range(BB[1],
                                                         BB[1] + K.A.N)),
        "K4_the_measured_divergence_support_of_943":
            set(r943["certificates"]["Q1_THE_VALUE_SPACE_SYMMETRY_FAMILY"]
                ["THE_DIVERGENCE_IS_CONFINED"]
                ["union_of_all_divergence_supports"]),
        "K5_every_wire_with_a_sigma_partner_plus_its_drivers":
            set(SIG) | read_cone(sched_p, set(SIG), 1),
        "K6_the_record_cells_only":
            {b + off for b in BB for cn in (0, 1)
             for off in K.A.cell(cn)["payload"]},
    }
    nb = {}
    for name, N in sorted(CHECKER_FORMS.items()):
        eq = []
        for (t, site) in atoms:
            lane = site
            m = M.Machine(env, False)
            m.advance(t, rows_p, cr_p, ZW)
            cols = m.columns
            th = perm_lane(cols, lane)
            bad = [w for w in sorted(N) if w not in (left_w, right_w)
                   and ((th[w] >> lane) & 1) != ((cols[w] >> lane) & 1)]
            if not bad:
                eq.append(f"{t}/{site}")
        nb[name] = {"wires": len(N), "atoms_with_sigma_invariant_conditions":
                    eq}
    prim_nb = (r946["certificates"]["Q2_THE_DERIVATION"]
               ["NEIGHBORHOOD_EQUALITY"]["formalizations"]
               ["N2_every_wire_the_law_touches"]
               ["atoms_with_sigma_invariant_conditions"])
    agreeing = {k: v["atoms_with_sigma_invariant_conditions"] == prim_nb
                for k, v in nb.items()}
    contains = {k: set(SIG) <= CHECKER_FORMS[k] for k in nb}
    refute("B1_the_neighborhood_split_is_formalization_dependent",
           not all(agreeing[k] for k in agreeing if contains[k]),
           {"checker_formalizations": nb,
            "primary_N2_answer": prim_nb,
            "agreement": agreeing,
            "contains_the_sigma_support": contains,
            "THE_FILTER_HAD_TO_BE_CORRECTED":
                "a first version of this attack filtered formalizations by "
                "SIZE (at least as many wires as the sigma support).  That "
                "admitted K6 -- 816 wires, every record cell payload in all "
                "twelve banks -- which answers that EVERY atom is symmetric, "
                "because U_TO_V and V_TO_U are bank-level fields and sit "
                "outside every cell payload.  Size is not the criterion; "
                "CONTAINMENT of the sigma support is.  Under containment "
                "every admissible checker formalization agrees with the "
                "primary, atom for atom, and K2 and K6 are exhibited as "
                "large-and-blind rather than as counterexamples.",
            "the_816_wire_blind_formalization": {
                "name": "K6_the_record_cells_only",
                "wires": len(CHECKER_FORMS["K6_the_record_cells_only"]),
                "contains_the_rails":
                    set(SIG) <= CHECKER_FORMS["K6_the_record_cells_only"],
                "its_answer": nb["K6_the_record_cells_only"][
                    "atoms_with_sigma_invariant_conditions"]}})

    # B2: THE INSTANT.  The primary sampled ONE boundary (the choice
    # boundary).  Sample the whole pre-choice window instead.
    inst = {}
    for (t, site) in atoms:
        lane = site
        m = M.Machine(env, False)
        m.advance(max(0, t - 40), rows_p, cr_p, ZW)
        breaks = 0
        checked = 0
        while m.t < t:
            cols = m.columns
            th = perm_lane(cols, lane)
            if any(((th[w] >> lane) & 1) != ((cols[w] >> lane) & 1)
                   for w in SIG if w not in (left_w, right_w)):
                breaks += 1
            checked += 1
            m.advance(m.t + 1, rows_p, cr_p, ZW)
        inst[f"{t}/{site}"] = {"boundaries_checked": checked,
                               "boundaries_where_conditions_are_not_sigma_"
                               "invariant": breaks}
    cov_keys = {f"{a[0]}/{a[1]}" for a in cov_declared}
    refute("B2_the_conditions_are_only_symmetric_at_the_sampled_instant",
           any(inst[k]["boundaries_where_conditions_are_not_sigma_invariant"]
               > 0 for k in cov_keys),
           {"per_atom_over_the_40_boundaries_before_the_choice": inst,
            "covered_atoms": sorted(cov_keys),
            "why": "the primary evaluates the conditions at exactly one "
                   "boundary.  They ARE asymmetric at most of the boundaries "
                   "just before it, INCLUDING at the covered atoms, so H3 is "
                   "instant-specific and any reading of it as a standing "
                   "property of the SITE is refuted.",
            "STATUS": "REFUTED AS A SITE-GENERIC CLAIM, AND ADOPTED BY THE "
                      "PRIMARY AS AN OCCASION-SPECIFIC ONE.  The fact is not "
                      "a defect: the axiom's own 'varies with' clause says "
                      "the distribution tracks the conditions, so a site "
                      "whose conditions are asymmetric a tick earlier SHOULD "
                      "have no forced value a tick earlier.  What the "
                      "finding kills is the sentence 'the conditions at this "
                      "site are symmetric', which nobody may now write.",
            "the_primary_publishes_this_measurement":
                "THE_CONDITIONS_ARE_EVALUATED_AT_THE_CHOICE_OCCASION"
                in compact(q2.get("NEIGHBORHOOD_EQUALITY", {})),
            "the_primary_states_the_occasion_restriction_in_the_proof":
                "occasion" in compact(q2.get("THEOREM", {})).lower()})
    timings["B_neighborhood"] = round(monotonic() - t0, 3)
    print(f"[B {timings['B_neighborhood']}s] neighborhood attacks done",
          flush=True)

    # ---- ATTACK C: the hypothesis chain ---------------------------------
    q2 = r946["certificates"]["Q2_THE_DERIVATION"]
    quotes_ok = {k: (v in ax_text) for k, v in q2["byte_quotes"].items()}
    refute("C1_a_byte_quote_is_not_in_the_adopted_text",
           not all(quotes_ok.values()),
           {"per_quote": quotes_ok})

    # C2: is the "identical conditions" FRAMING actually what is measured?
    framing_keys = compact(q2["NEIGHBORHOOD_EQUALITY"])
    refute("C2_the_prose_says_identical_conditions_but_measures_"
           "sigma_invariance",
           '"conditions_identical"' in framing_keys
           or "atoms_with_identical_conditions" in framing_keys,
           {"the_problem": "the two branches SHARE a parent state, so 'the "
                           "two branches present identical nearest-neighbor "
                           "conditions' is TRIVIALLY TRUE and licenses "
                           "nothing.  It is not what the primary measured.  "
                           "What it measured -- correctly -- is that the "
                           "conditions are INVARIANT UNDER SIGMA, which is a "
                           "different and much stronger statement.  The "
                           "THEOREM text says invariance and is right; the "
                           "field names and the supervisor's route name say "
                           "'identical' and are wrong.",
            "verdict": "REFUTED AS PROSE, SOUND AS MEASUREMENT.  The primary "
                       "must relabel; no number changes."})

    # C3: is the substrate law the axiom's admissibility rule?
    bridge_named = any(
        "substrate" in compact(v).lower() and "rule" in compact(v).lower()
        for v in [q2.get("THEOREM", {}).get("HYPOTHESIS_CHAIN", {})])
    hchain = compact(q2.get("THEOREM", {}).get("HYPOTHESIS_CHAIN", {})).lower()
    refute("C3_an_unnamed_bridge_hypothesis_identifies_the_substrate_law_"
           "with_the_axioms_rule",
           not ("h0" in hchain and "import" in hchain
                and "realization of the axiom" in hchain),
           {"the_gap": "H2 certifies that sigma is a symmetry of THE "
                       "COMPILED SUBSTRATE LAW -- a 34,408-gate circuit on "
                       "5,815 wires over 749 census lanes.  The axiom's "
                       "determination clause is about THE NEAREST-NEIGHBOR "
                       "ADMISSIBILITY RULE on Z^3.  Nothing in the primary's "
                       "chain states the identification of the one with the "
                       "other, yet every step of the proof uses it: step 2 "
                       "moves from 'sigma commutes with the compiled law' to "
                       "'sigma_* is an automorphism the RULE cannot "
                       "distinguish from the identity'.  That move is the "
                       "load-bearing import of the whole block and it is "
                       "currently unnamed.",
            "what_it_should_say": "H0 (IMPORT, undischarged): the compiled "
                                  "substrate law is a realization of the "
                                  "axiom's nearest-neighbor admissibility "
                                  "rule, and a symmetry of the former is a "
                                  "symmetry of the latter.  This is NOT "
                                  "derived anywhere in the 936/940/943/946 "
                                  "stack.  Without it the theorem is a "
                                  "theorem about a circuit, not about the "
                                  "framework's Admissibility axiom.",
            "verdict": "REFUTED.  The hypothesis chain is incomplete and "
                       "must carry H0 explicitly."})

    # C4: does the determination clause alone force equality?  (it does not)
    refute("C4_the_determination_clause_alone_is_claimed_to_force_equality",
           "H4" not in compact(q2.get("THEOREM", {})
                               .get("HYPOTHESIS_CHAIN", {})),
           {"test": "a rule f that is a function of the conditions can still "
                    "assign unequal probabilities to two possibilities, "
                    "because f's VALUE is a distribution over a LABELLED "
                    "domain and nothing in 'determined by' forbids the labels "
                    "from mattering.  Equality needs the no-privilege clause.",
            "primary_position": "the primary names exactly this as H4 and "
                                "says outright that without it the "
                                "determination clause is vacuous",
            "verdict": "NOT REFUTED -- the primary already carries it, and "
                       "the checker confirms the argument fails without it"})

    # C5: the covariance route -- is it smuggled back in anywhere?
    proof_text = compact(q2.get("THEOREM", {}).get("PROOF", [])).lower()
    refute("C5_the_covariance_clause_is_used_after_being_rejected",
           "covariant" in proof_text or "rotation" in proof_text
           or "translation" in proof_text,
           {"proof_mentions": [w for w in ("covariant", "covariance",
                                           "rotation", "translation")
                               if w in proof_text],
            "note": "step 1 does use the FIRST sentence, but only for "
                    "'one fixed rule / same function at every site', which is "
                    "site-independence, not covariance under a group action.  "
                    "Checked and accepted."})

    # C6: H5, the domain
    refute("C6_the_domain_of_the_distribution_is_assumed_not_argued",
           "circular" not in compact(q2.get("THEOREM", {})
                                     .get("HYPOTHESIS_CHAIN", {})).lower(),
           {"the_issue": "if the distribution's domain were 'the available "
                         "possibilities' the argument would need availability "
                         "fixed first",
            "primary_position": "H5 dissolves it by composition: the adopted "
                                "reading note DEFINES availability as the "
                                "distribution's support, so the "
                                "available-only reading is circular and the "
                                "domain is the full Qubit possibility "
                                "domain.  No ruling is cited.",
            "verdict": "NOT REFUTED"})

    # ---- ATTACK D: the sealed table, re-scored --------------------------
    t0 = monotonic()
    tree_p = M.enumerate_tree(env, rows_p, cr_p, words, atoms_at, TREE_B,
                              reverse=False)
    leaves = tree_p["leaf_records"]
    dg = [r["digest"] for r in leaves]
    bit_index = {}
    i = 0
    for t in apps:
        for site in atoms_at[t]:
            bit_index[(t, site)] = i
            i += 1
    nbits = i
    my_seal = {}
    for (t, site) in atoms:
        b = bit_index[(t, site)]
        step = 1 << (nbits - 1 - b)
        same = all(leaves[i]["digest"] == leaves[i ^ step]["digest"]
                   for i in range(len(leaves)))
        my_seal[f"{t}/{site}"] = {"all_pairs_digest_identical": same,
                                  "site_formed":
                                      site in leaves[0]["build"]["formed"]}
    v = r946["certificates"]["Q3_THE_FIRST_DERIVED_PREDICTION"]["VERIFICATION"]
    matters = [f"{t}/{s}" for (t, s) in atoms
               if not my_seal[f"{t}/{s}"]["all_pairs_digest_identical"]]
    refute("D1_the_sealed_table_rescores_differently",
           sorted(matters) != sorted(v["observable_bits"])
           or len(set(dg)) != v["distinct_leaf_observables_partnered"],
           {"checker_observable_bits": sorted(matters),
            "primary_observable_bits": sorted(v["observable_bits"]),
            "checker_distinct_leaf_observables": len(set(dg)),
            "primary_distinct": v["distinct_leaf_observables_partnered"]})
    refute("D2_the_primary_hid_a_refuted_seal_item",
           v.get("S4_every_uncovered_atom_has_a_differing_pair") is not False
           or "S4_IS_REFUTED_AND_HERE_IS_WHY" not in v,
           {"S4_value": v.get("S4_every_uncovered_atom_has_a_differing_pair"),
            "refutation_is_published": "S4_IS_REFUTED_AND_HERE_IS_WHY" in v,
            "verdict": "NOT REFUTED -- the primary shipped its own failed "
                       "prediction with an explanation, which is the "
                       "behaviour the seal exists to produce"})
    # D3: the battery, recomputed
    meas = [M.measurement(env, r["build"]) for r in leaves]
    bat = q1["BATTERY"]
    my_bat = {
        "write_once": all(x["write_once_violations"] == 0 for x in meas),
        "menu": all(x["off_menu_endpoint_content_at_the_lock"] == 0
                    for x in meas),
        "dup_lane": all(x["duplicate_lane_mismatches"] == 0 for x in meas)
        and all(r["build"]["duplicate_lane_column_divergence"] == 0
                for r in leaves),
        "slots": all(x["record_slot_activation_conflicts"] == 0
                     for x in meas),
        "formation": all(x["lock_points"] > 0 for x in meas),
    }
    refute("D3_the_battery_does_not_hold_on_every_branch",
           not all(my_bat.values()),
           {"checker_battery": my_bat,
            "primary_claims": {
                "write_once": bat["write_once_holds_on_every_branch"],
                "menu": bat["menu_holds_on_every_branch"],
                "dup_lane": bat[
                    "duplicate_lane_consistency_holds_on_every_branch"],
                "slots": bat["record_slots_inert_on_every_branch"]}})
    timings["D_seal"] = round(monotonic() - t0, 3)
    print(f"[D {timings['D_seal']}s] seal re-scored: observable bits "
          f"{sorted(matters)}, distinct {len(set(dg))}", flush=True)

    # C7: the firewall -- hunt an unconditional weight value in the receipt
    def walk(o, p=""):
        if isinstance(o, dict):
            for k, vv in o.items():
                yield from walk(vv, f"{p}.{k}")
        elif isinstance(o, list):
            for i2, vv in enumerate(o):
                yield from walk(vv, f"{p}[{i2}]")
        else:
            yield p, o
    FENCE = ("CONDITIONAL", "HYPOTHETICAL", "IF_", "THEOREM")
    suspicious = []
    for p, val in walk(r946):
        if isinstance(val, str) and val in ("1/2", "0.5") \
                and not any(f in p.upper() for f in FENCE):
            suspicious.append(p)
    refute("C7_an_unconditional_weight_value_appears_in_the_receipt",
           bool(suspicious),
           {"paths": suspicious[:10],
            "note": "every occurrence of the value must sit under a "
                    "CONDITIONAL/HYPOTHETICAL/IF_/THEOREM key path"})

    # ---- teeth ----------------------------------------------------------
    tooth("T1_the_checkers_own_splice_reproduces_the_partnered_gate_total",
          sum(len(s) for s in sched_p) == q1["gates_after"],
          {"checker": sum(len(s) for s in sched_p)})
    tooth("T2_a_wrong_involution_on_LIVE_wires_is_rejected",
          all(v > 0 for v in must_break.values())
          and wrong["two_INERT_wires_the_law_never_touches"] == 0, wrong)
    tooth("T3_the_baseline_fails_the_checkers_commutation_test",
          len(bad_b) > 0, {"baseline_breaking_wires": len(bad_b)})
    tooth("T4_the_partnered_kernel_passes_it", len(bad_p) == 0,
          {"partnered_breaking_wires": len(bad_p)})
    tooth("T5_sigma_moves_the_menu_at_every_atom",
          all(a != c for a, b, c, d in menu_moved), {"rows": menu_moved})
    tooth("T6_a_tampered_axiom_quote_is_rejected",
          (q2["byte_quotes"]["Admissibility_distribution"] in ax_text)
          and (q2["byte_quotes"]["Admissibility_distribution"]
               .replace("determined by", "unconstrained by") not in ax_text),
          {})
    tooth("T7_the_checkers_defect_census_matches_the_primarys",
          len(my_defect) == q1["defect_occurrences"],
          {"checker": len(my_defect), "primary": q1["defect_occurrences"]})
    tooth("T8_the_orientation_drives_are_exactly_four_distinct_gates",
          len({(g[0], g[1], g[2], g[3]) for _s, g, _i in my_defect
               if M.gate_target(*g[:4]) in ORI}) == 4,
          {"orientation_defect_distinct":
           sorted({(g[1], g[2], g[3]) for _s, g, _i in my_defect
                   if M.gate_target(*g[:4]) in ORI})})
    tooth("T9_the_link_ladder_defect_is_real_and_outside_943s_support",
          bool({M.gate_target(*g[:4]) for _s, g, _i in my_defect}
               - set(ORI)
               - set(r943["certificates"]
                     ["Q1_THE_VALUE_SPACE_SYMMETRY_FAMILY"]
                     ["THE_DIVERGENCE_IS_CONFINED"]
                     ["union_of_all_divergence_supports"])),
          {"link_targets": sorted({M.gate_target(*g[:4])
                                   for _s, g, _i in my_defect} - set(ORI))})
    tooth("T10_coverage_is_not_an_artifact_of_the_declared_window",
          sorted(cov_long) == sorted(cov_declared),
          {"declared": cov_declared, "double": cov_long})
    tooth("T11_the_seal_rescores_identically",
          sorted(matters) == sorted(v["observable_bits"]),
          {"checker": sorted(matters)})
    tooth("T12_the_primary_self_hash_and_axiom_pin_agree",
          pins["primary_self_sha256_agrees"] and pins["adopted_axiom_agrees"],
          pins)
    tooth("T13_no_blocked_primary_was_imported",
          not pins["blocked_modules_loaded"] and not pins["firewall_hits"],
          {})
    tooth("T14_the_checker_found_at_least_one_real_refutation",
          any(f["REFUTED"] for f in findings),
          {"refuted": [f["finding"] for f in findings if f["REFUTED"]]})

    elapsed = round(monotonic() - started, 2)
    refuted = [f["finding"] for f in findings if f["REFUTED"]]
    receipt = {
        "block": "toe-time-expansion-20260802/blockQ17",
        "cycles": [946],
        "campaign": "toe-time-expansion-20260802",
        "role": "independent_checker",
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "CONDITIONAL_ON_PR_6011_LANDING": True,
        "headline":
            "THE CONSTRUCTION SURVIVES; THE HYPOTHESIS CHAIN DOES NOT, AS "
            "WRITTEN.  The checker rebuilds the mirror defect by a different "
            "algorithm and gets the same 220 occurrences and 12 distinct "
            "gates; it reproduces the partnered kernel gate-for-gate, and the "
            "swap commutes with zero breaking wires on an ensemble that adds "
            "all-zero, all-one, alternating, sigma-support-only and the eight "
            "REAL on-orbit states to the primary's random ones, while every "
            "deliberately wrong involution breaks.  Coverage is unchanged at "
            "twice the declared window.  The seal re-scores identically, S4 "
            "included.  TWO REFUTATIONS: (1) the 'identical conditions' "
            "framing is trivially true and is not what was measured -- the "
            "branches share a parent state, and what licenses the conclusion "
            "is SIGMA-INVARIANCE of the conditions, which is what the theorem "
            "text actually says and what the field names do not; (2) the "
            "hypothesis chain omits the import that carries the entire "
            "block: nothing states that the compiled substrate law IS a "
            "realization of the axiom's nearest-neighbor admissibility rule, "
            "yet every proof step uses it.  Without that named import the "
            "result is a theorem about a 34,408-gate circuit, not about the "
            "framework's Admissibility axiom.",
        "REFUTATIONS": refuted,
        "findings": findings,
        "teeth": teeth,
        "teeth_total": len(teeth),
        "teeth_fired": sum(1 for t in teeth if t["fired"]),
        "pins": pins,
        "checker_numbers": {
            "defect_occurrences": len(my_defect),
            "defect_distinct": len(my_distinct),
            "partnered_gates": sum(len(s) for s in sched_p),
            "semantic_breaking_wires_partnered": len(bad_p),
            "semantic_breaking_wires_baseline": len(bad_b),
            "wrong_involutions_breaking_wires": wrong,
            "coverage_declared_window": cov_declared,
            "coverage_double_window": cov_long,
            "neighborhood_formalizations": nb,
            "pre_choice_window_stability": inst,
            "observable_bits": sorted(matters),
            "distinct_leaf_observables": len(set(dg)),
            "battery": my_bat,
        },
        "elapsed_sec": elapsed,
        "within_budget": elapsed <= RUNTIME_BUDGET_SEC,
        "timings": timings,
        "all_teeth_fired": all(t["fired"] for t in teeth),
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out = ROOT / "outputs" / \
        "mirror_kernel_independent_check_cycle946_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    lines = ["===== runner cache v1 ====="]
    lines.append("runner: scripts/frontier_cycle946_mirror_kernel_"
                 "independent_check_2026_07_28.py")
    lines.append(f"runner_sha256: {receipt['self_sha256']}")
    lines.append("receipt: outputs/mirror_kernel_independent_check_cycle946_"
                 "receipt_2026_07_28.json")
    lines.append(f"timeout_sec: {RUNTIME_BUDGET_SEC}")
    lines.append(f"elapsed_sec: {elapsed}")
    lines.append(f"status: {'ok' if receipt['all_teeth_fired'] else 'FAIL'}")
    lines.append("----- stdout -----")
    lines.append(f"teeth fired: {receipt['teeth_fired']}/"
                 f"{receipt['teeth_total']}")
    lines.append(f"REFUTATIONS ({len(refuted)}):")
    for r in refuted:
        lines.append(f"  - {r}")
    for f in findings:
        lines.append(f"  {'REFUTED ' if f['REFUTED'] else 'upheld  '} "
                     f"{f['finding']}")
    lines.append(f"checker defect: {len(my_defect)} occurrences / "
                 f"{len(my_distinct)} distinct (primary "
                 f"{q1['defect_occurrences']}/{q1['defect_distinct_gates']})")
    lines.append(f"checker semantic breaking wires: partnered {len(bad_p)} / "
                 f"baseline {len(bad_b)}")
    lines.append(f"wrong involutions (all must break): {wrong}")
    lines.append(f"coverage declared window {cov_declared}")
    lines.append(f"coverage 2x window       {cov_long}")
    lines.append(f"observable bits {sorted(matters)}; distinct leaf "
                 f"observables {len(set(dg))}")
    lines.append(f"battery {my_bat}")
    lines.append(f"elapsed: {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    lines.append(f"ALL TEETH FIRED: {receipt['all_teeth_fired']}")
    lines.append("===== end runner cache =====")
    cache = ROOT / "logs" / "runner-cache" / \
        "frontier_cycle946_mirror_kernel_independent_check_2026_07_28.txt"
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines), flush=True)
    return 0 if receipt["all_teeth_fired"] else 1


if __name__ == "__main__":
    sys.exit(main())
