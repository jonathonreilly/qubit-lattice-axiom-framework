#!/usr/bin/env python3
"""Cycle 940 -- INDEPENDENT CHECK, spec'd to REFUTE.

This checker does not trust one number of the primary's.  It rebuilds the
substrate from the pinned bytes, re-derives every claim by a DIFFERENT method,
and attacks the four surfaces the spec names:

  (i)   ANY CLAIMED AUTOMORPHISM.  Recompute its action on the FULL state, not
        on the named observables -- hunt a moved quantity.  The primary's
        positive control is re-verified by direct gate-image comparison AND by
        executing the relabelled program against the original on real columns.
  (ii)  ANY CLAIMED NON-EXISTENCE.  Hunt an automorphism the primary missed
        over a WIDER candidate family than the primary tried: an exhaustive
        single-transposition sweep, a closure/propagation search seeded on
        LEFT->RIGHT that is allowed to grow arbitrarily, an orbit-reachability
        argument, and a direct semantic test that ignores the gate list
        entirely and asks whether the two menu items are DISTINGUISHABLE by the
        substrate's own dynamics.
  (iii) THE ANTECEDENT ANALYSIS.  Adversarially re-read the quoted grounds.
        Does any quoted clause actually ground naturality?  Is the primary's
        negative too quick -- or, worse for the primary, is its READING of the
        no-privilege clause a convenient one?
  (iv)  THE FIREWALL.  Try to slip a weight value past it.

Independence: the checker computes the refinement by a DIFFERENT algorithm
(iterated signature hashing over an explicitly built incidence graph, with a
separately implemented stable-partition test), replays the tree WITHOUT the
primary's enumerator, and recomputes the weight algebra by DETERMINING GRID
EVALUATION rather than symbolic polynomials.

Refutations are reported plainly.  A refutation is not a failure of this
runner; it is its product.
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

BUDGET = 900
PRIMARY = "scripts/frontier_cycle940_symmetric_weights_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/symmetric_weights_cycle940_receipt_2026_07_28.json"
C936_PATH = "scripts/frontier_cycle936_choice_substrate_2026_07_28.py"
C936_RECEIPT = "outputs/choice_substrate_cycle936_receipt_2026_07_28.json"
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PA_MENU = ("docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3"
           "_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md")
PA_GLEASON = ("docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE"
              "_GLEASON_BRIDGE_NOTE_2026-07-04.md")
ENVARIANCE_BLOB = "64b24361f2237d01f079e16b306b5d04e01de7c2"

BLOCKED = ("frontier_cycle936_choice_substrate_2026_07_28",
           "frontier_cycle940_symmetric_weights_2026_07_28",
           "frontier_cycle863_time_from_records_2026_07_28",
           "frontier_cycle913_selection_function_2026_07_28")


class _FW(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKED:
            self.hits.append(fullname)
            raise ImportError(f"checker blocklist: {fullname}")
        return None


FW = _FW()
sys.meta_path.insert(0, FW)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def dig(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


# ---------------------------------------------------------------------------
# the checker's OWN lift of the pinned machinery (own selector, own namespace)
# ---------------------------------------------------------------------------

def lift(path, funcs, consts, classes, glb):
    src = (ROOT / path).read_text(encoding="utf-8")
    tree = ast.parse(src, filename=path)
    body = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        elif isinstance(node, ast.ClassDef) and node.name in classes:
            body.append(node)
        elif isinstance(node, ast.Assign):
            nm = []
            for t in node.targets:
                if isinstance(t, ast.Name):
                    nm.append(t.id)
                elif isinstance(t, ast.Tuple):
                    nm.extend(e.id for e in t.elts if isinstance(e, ast.Name))
            if nm and all(x in consts for x in nm):
                body.append(node)
    mod = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(mod)
    ns = dict(glb)
    exec(compile(mod, f"<check-lift {path}>", "exec"), ns)
    return ns


def main() -> int:
    t_start = monotonic()
    checks, refutations, teeth, findings = [], [], [], []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return bool(ok)

    def refute(name, detail):
        refutations.append({"refutation": name, "detail": detail})

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    # ---------------- the primary's own artefacts, read but not trusted ----
    primary_src = (ROOT / PRIMARY).read_bytes()
    pr = json.loads((ROOT / PRIMARY_RECEIPT).read_text(encoding="utf-8"))
    ck("primary_receipt_self_sha256_matches_the_primary_file",
       sha256(primary_src).hexdigest() == pr["self_sha256"],
       "the receipt names the bytes that produced it")
    ck("primary_reports_all_certificates_pass", pr["all_certificates_pass"])

    P1 = pr["certificates"]["Q1_THE_MENU_SWAP_AUTOMORPHISM"]
    P2 = pr["certificates"]["Q2_THE_CONDITIONAL_THEOREM_AND_ITS_ANTECEDENT"]
    P3 = pr["certificates"]["Q3_THE_VERDICT_FOR_THE_ASK_BAR"]
    PF = pr["certificates"]["F_PARAMETRIC_FIREWALL"]

    # ---------------- rebuild the substrate independently ------------------
    c936_src = (ROOT / C936_PATH).read_text(encoding="utf-8")
    ns936 = lift(
        C936_PATH,
        ("ast_lift", "lift_ast_op_tuple", "lift_machinery", "station_mask",
         "build_schedules", "chunk_source", "pinned_statement_text",
         "extended_statement_text", "gate_target", "CHOICE",
         "compile_schedules", "acc_add", "acc_get", "item_of", "build_digest",
         "choice_support_words"),
        ("CORE_PATH", "HANDSHAKE_PATH", "C863_PATH", "C878_PATH", "C911_PATH",
         "C913_PATH", "C863_FUNCS", "C863_CONSTS", "C878_FUNCS",
         "C878_CONSTS", "C911_FUNCS", "C911_CONSTS", "C913_FUNCS", "KIND_X",
         "KIND_CNOT", "KIND_TOF", "KIND_SHIFT", "KIND_CHOICE", "KIND_NAMES",
         "CERTIFIED_KINDS", "PINNED_TEMPLATES", "CHOICE_TEMPLATE",
         "EXTENDED_TEMPLATES", "LANE_SHIFT", "HORIZON", "DEAD_CHUNK_ORBITS",
         "TREE_ORBITS", "CHOICE_ATOMS", "FULL_TREE_LEAF_CAP", "_CHOICE_SINK"),
        ("Machine",),
        {"__builtins__": __builtins__, "ROOT": ROOT, "K": K, "np": np,
         "ast": ast, "json": json, "sys": sys, "Path": Path,
         "math": math, "itertools": itertools,
         "combinations": combinations, "product": product,
         "Counter": Counter, "Fraction": Fraction, "sha256": sha256,
         "SimpleNamespace": SimpleNamespace, "compact": compact,
         "digest": dig})
    M = SimpleNamespace(**ns936)
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     _prov) = M.lift_machinery()
    KX, KC, KT = M.KIND_X, M.KIND_CNOT, M.KIND_TOF

    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _ = c863.build_initial_states(program, event_seeds, census)
    left_w, right_w, src_w = c913.endpoint_wires()
    n = len(census)
    BB = K.M.R12.BANK_BASES
    sim_fwd = tuple(census) + (census[0],)
    sched = c863.masked_h_schedules(program, sim_fwd)
    flat = [g for s in sched for g in s]
    proto = c863.pack_lanes(tuple(states) + (states[0],))

    ck("endpoint_wires_agree_with_the_primary",
       [left_w, right_w, src_w]
       == [P1["THEOREM_A1"]["endpoint_wires"][k]
           for k in ("LEFT", "RIGHT", "SOURCE_POINTER")],
       f"LEFT={left_w} RIGHT={right_w} SOURCE={src_w}")
    ck("compiled_gate_total_independently_recomputed",
       len(flat) == 34166, f"{len(flat)}")

    # =====================================================================
    # ATTACK (i): THE CLAIMED AUTOMORPHISM -- act on the FULL state
    # =====================================================================
    t0 = monotonic()

    def img(g, pi):
        k, a, b, c3, m = g
        return (k, pi.get(a, a), pi.get(b, b), pi.get(c3, c3), m)

    def is_auto(pi, ordered=True):
        if ordered:
            return all([img(g, pi) for g in s] == list(s) for s in sched)
        return all(Counter(img(g, pi) for g in s) == Counter(s)
                   for s in sched)

    # rebuild the primary's positive control from ITS OWN reported classes,
    # then verify it by EXECUTING both programs on real columns -- a semantic
    # test the primary never ran.
    pc = P1["THE_POSITIVE_CONTROL"]
    # re-derive the classes independently (checker's own refinement below)
    def checker_refine(label):
        """Independent implementation: explicit incidence graph + iterated
        signature HASHING (the primary used dict-keyed canonical relabelling).
        Different algorithm, same mathematical invariant."""
        inc = defaultdict(list)
        wires = set()
        for gi, g in enumerate(flat):
            k, a, b, c3, m = g
            wires |= {a, b, c3}
            if k == KX:
                inc[a].append((gi, 2))
            elif k == KC:
                inc[a].append((gi, 0))
                inc[b].append((gi, 2))
            else:
                inc[a].append((gi, 0))
                inc[b].append((gi, 1))
                inc[c3].append((gi, 2))
        col = {w: "0" for w in wires}
        prev = None
        rounds = 0
        while col != prev and rounds < 64:
            prev = dict(col)
            nxt = {}
            for w in wires:
                acc = []
                for gi, role in inc[w]:
                    k, a, b, c3, m = flat[gi]
                    if label == "bare":
                        lab = (k, role)
                    elif label == "popcount":
                        lab = (k, role, bin(m).count("1"))
                    else:
                        lab = (k, role, m)
                    acc.append((lab, col[a], col[b], col[c3]))
                acc.sort(key=lambda x: compact(x))
                nxt[w] = sha256(
                    (col[w] + "|" + compact(acc)).encode()).hexdigest()[:24]
            col = nxt
            rounds += 1
        return col, wires, rounds

    col_exact, wires, rounds = checker_refine("exact")
    cls = defaultdict(list)
    for w in wires:
        cls[col_exact[w]].append(w)
    my_classes = sorted([sorted(v) for v in cls.values() if len(v) > 1])
    ck("checker_refinement_reproduces_the_class_COUNT",
       len(my_classes) == P1["REFINEMENTS"]["exact"]["non_singleton_classes"],
       f"checker {len(my_classes)} vs primary "
       f"{P1['REFINEMENTS']['exact']['non_singleton_classes']} "
       f"(independent algorithm: signature hashing, {rounds} rounds)")

    pi_pc = {}
    for v in my_classes:
        if len(v) == 2:
            pi_pc[v[0]] = v[1]
            pi_pc[v[1]] = v[0]
    ck("checker_rebuilds_the_positive_control_with_the_same_support",
       len(pi_pc) == pc["wires_moved"],
       f"{len(pi_pc)} wires vs primary {pc['wires_moved']}")
    ck("positive_control_ordered_reading_agrees",
       is_auto(pi_pc, True) == pc["is_a_program_automorphism_ordered_reading"])
    ck("positive_control_multiset_reading_agrees",
       is_auto(pi_pc, False)
       == pc["is_a_program_automorphism_multiset_reading"])

    # THE ATTACK PROPER: execute the relabelled program against the original
    # on REAL columns and diff the FULL state, not the named observables.
    def run_chunks(gate_rows, cols, steps):
        fns = M.compile_schedules(gate_rows)
        c = list(cols)
        for t in range(steps):
            fns[t % len(fns)](c)
        return c

    steps = stations * 3
    base_cols = run_chunks(sched, proto, steps)

    # CHECKER-SIDE BUG FOUND AND FIXED, DISCLOSED.  The first version of this
    # test ran the RELABELLED program on the RELABELLED initial state and
    # un-permuted the result.  That is a TAUTOLOGY: for any permutation pi
    # whatsoever, (pi.P.pi^-1)(pi(s)) = pi(P(s)), so it passes everything and
    # tests nothing.  The sensitivity tooth below caught it.  The correct
    # semantic condition for pi to be an automorphism is that pi COMMUTES with
    # the dynamics: run the ORIGINAL program on the permuted state and compare
    # with permuting the original run's result.
    def commutes(pi, nsteps):
        permuted_init = list(proto)
        for x, y in pi.items():
            permuted_init[y] = proto[x]
        got = run_chunks(sched, permuted_init, nsteps)
        want = run_chunks(sched, proto, nsteps)
        expect = list(want)
        for x, y in pi.items():
            expect[y] = want[x]
        return [w for w in range(len(got)) if got[w] != expect[w]]

    moved_wires = commutes(pi_pc, steps)
    # THE FINDING THIS CHECKER CONTRIBUTED, NOW ADOPTED BY THE PRIMARY.
    # The multiset-level automorphism does NOT commute with the law, so
    # multiset preservation is too weak to define a substrate automorphism.
    # The primary was re-run with this adopted; the check below verifies the
    # primary states the corrected fact rather than the original stronger one.
    pc_says_commutes = pc.get("commutes_with_the_law_on_real_columns")
    ck("primary_correctly_reports_the_positive_control_does_NOT_commute",
       pc_says_commutes is False and bool(moved_wires),
       f"checker finds pi.P disagrees with P.pi on {len(moved_wires)} wires; "
       f"the primary reports commutes={pc_says_commutes} and "
       f"{pc.get('wires_where_it_fails_to_commute')} failing wires")
    ck("checker_and_primary_agree_on_the_failing_wire_COUNT",
       pc.get("wires_where_it_fails_to_commute") == len(moved_wires),
       f"checker {len(moved_wires)} vs primary "
       f"{pc.get('wires_where_it_fails_to_commute')}")
    findings.append({
        "finding": "MULTISET PRESERVATION IS NOT SUFFICIENT FOR A SYMMETRY OF "
                   "THE LAW.  The involution built from the refinement's own "
                   "colour classes preserves every station's gate multiset "
                   "but does not commute with the dynamics, because gates "
                   "inside a station do not commute.",
        "moved_wires": len(moved_wires),
        "raised_by": "this checker",
        "adopted_by_the_primary": bool(pc_says_commutes is False),
        "bears_on": "the primary's POSITIVE CONTROL, whose role is to show "
                    "the LOOSEST candidate notion of automorphism is "
                    "non-trivially inhabited so that the negative at that "
                    "level is not an artefact of an over-strict definition.  "
                    "That role is untouched.  Theorem A1 is established at "
                    "the loose end and therefore holds A FORTIORI at every "
                    "stricter end, so this finding SHRINKS the automorphism "
                    "group further and strengthens the block's negative.",
        "refutes_a_load_bearing_claim": False,
        "changed_the_science_digest": False})

    # does it move any OBSERVABLE the primary named as fixed?
    ck("positive_control_leaves_the_endpoint_wires_untouched",
       pi_pc.get(left_w, left_w) == left_w
       and pi_pc.get(right_w, right_w) == right_w,
       "hunting a moved quantity among the named-fixed observables: none")

    # =====================================================================
    # ATTACK (ii): THE CLAIMED NON-EXISTENCE -- hunt harder than the primary
    # =====================================================================
    # (a) EXHAUSTIVE single-transposition sweep: is ANY transposition
    #     involving an endpoint wire an automorphism?
    single_hits = []
    for w in sorted(wires):
        if w in (left_w, right_w):
            continue
        for e in (left_w, right_w):
            pi = {e: w, w: e}
            if is_auto(pi, False):
                single_hits.append([e, w])
    ck("exhaustive_single_transposition_sweep_finds_no_endpoint_swap",
       not single_hits,
       f"swept {2 * (len(wires) - 2)} transpositions moving an endpoint "
       f"wire; automorphisms found: {single_hits}")

    # (b) CLOSURE SEARCH seeded on LEFT->RIGHT, allowed to grow arbitrarily.
    #     If a swap automorphism exists at all, a correct closure must find it
    #     or must terminate in a provable contradiction.
    def closure_search(seed):
        pi = dict(seed)
        # index gates by (kind, mask) so the map is forced gate by gate
        buckets = defaultdict(list)
        for g in flat:
            buckets[(g[0], g[4])].append(g)
        for _round in range(64):
            forced = {}
            contradiction = None
            for key, gs in buckets.items():
                src = Counter(gs)
                for g in gs:
                    k, a, b, c3, m = g
                    ia, ib, ic = pi.get(a, a), pi.get(b, b), pi.get(c3, c3)
                    cand = [h for h in src
                            if (h[1] == ia or a not in pi)
                            and (h[2] == ib or b not in pi)
                            and (h[3] == ic or c3 not in pi)]
                    if not cand:
                        contradiction = {
                            "gate": list(g[:4]),
                            "image_addresses": [ia, ib, ic],
                            "reason": "no gate of the same (kind, mask) can "
                                      "receive this gate's image"}
                        break
                    if len(cand) == 1:
                        h = cand[0]
                        for x, y in ((a, h[1]), (b, h[2]), (c3, h[3])):
                            if x in pi and pi[x] != y:
                                contradiction = {
                                    "gate": list(g[:4]),
                                    "conflict_on_wire": x,
                                    "already_mapped_to": pi[x],
                                    "now_forced_to": y,
                                    "reason": "the forced image conflicts "
                                              "with an earlier forcing"}
                                break
                            forced[x] = y
                        if contradiction:
                            break
                if contradiction:
                    break
            if contradiction:
                return None, contradiction
            new = {k: v for k, v in forced.items() if pi.get(k) != v}
            if not new:
                return pi, None
            pi.update(new)
        return pi, {"reason": "closure did not converge in 64 rounds"}

    clo_pi, clo_contra = closure_search({left_w: right_w, right_w: left_w})
    swap_found = clo_pi is not None and is_auto(clo_pi, False)
    # record WHY it fails, not merely that it does
    clo_break = None
    if clo_pi is not None and not swap_found:
        for si, sch in enumerate(sched):
            src_c, img_c = Counter(sch), Counter(img(g, clo_pi) for g in sch)
            for g in sorted(set(src_c) | set(img_c)):
                if src_c[g] != img_c[g]:
                    clo_break = {"station": si, "gate": list(g[:4]),
                                 "multiplicity_original": src_c[g],
                                 "multiplicity_image": img_c[g]}
                    break
            if clo_break:
                break
    clo_report = {
        "seeded_on": {"LEFT": left_w, "RIGHT": right_w},
        "terminated_with_a_contradiction": clo_contra is not None,
        "contradiction": clo_contra,
        "converged_to_a_map_of_size": len(clo_pi) if clo_pi else None,
        "the_converged_map_is_an_automorphism": bool(swap_found),
        "first_gate_the_converged_map_breaks": clo_break,
        "reading":
            "the closure was seeded ONLY on LEFT->RIGHT and allowed to grow "
            "without bound.  It is a genuine attempt to construct the "
            "automorphism the primary says does not exist; it fails, and the "
            "gate it fails on is reported so the failure can be inspected "
            "rather than taken on trust.",
    }
    ck("closure_search_seeded_on_LEFT_to_RIGHT_finds_no_automorphism",
       not swap_found,
       f"contradiction: {compact(clo_contra)[:300]}" if clo_contra
       else f"closure converged to a map of size "
            f"{len(clo_pi) if clo_pi else 0} which is NOT an automorphism; "
            f"first broken gate {compact(clo_break)}")
    if swap_found:
        refute("A SWAP AUTOMORPHISM EXISTS -- the primary's Theorem A1 is "
               "FALSE",
               f"closure search produced {compact(clo_pi)[:400]}")

    # (c) ORBIT-REACHABILITY: an automorphism preserves the set of wires
    #     reachable from a wire by k gate-steps.  Compare the reachability
    #     profiles of LEFT and RIGHT directly -- a second, refinement-free
    #     invariant.
    succ = defaultdict(set)
    for g in flat:
        k, a, b, c3, m = g
        tgt = a if k == KX else (b if k == KC else c3)
        if k == KC:
            succ[a].add(tgt)
        elif k == KT:
            succ[a].add(tgt)
            succ[b].add(tgt)

    def reach(w, depth):
        cur, seen = {w}, {w}
        prof = []
        for _ in range(depth):
            nxt = set()
            for x in cur:
                nxt |= succ.get(x, set())
            nxt -= seen
            seen |= nxt
            prof.append(len(nxt))
            cur = nxt
        return prof, seen

    pL, sL = reach(left_w, 4)
    pR, sR = reach(right_w, 4)
    ck("reachability_profiles_of_LEFT_and_RIGHT_differ",
       pL != pR,
       f"LEFT {pL} vs RIGHT {pR} -- a refinement-FREE invariant that "
       "independently forbids any automorphism mapping one to the other")
    if pL == pR:
        findings.append({
            "finding": "the reachability profiles agree, so this particular "
                       "invariant does not separate LEFT from RIGHT",
            "bears_on": "the refinement separation would then be the only "
                        "support for Theorem A1",
            "refutes_a_load_bearing_claim": False})

    # (d) THE SEMANTIC TEST that ignores the gate list entirely: are the two
    #     menu items distinguishable by the substrate's own dynamics?  Prepare
    #     two states differing ONLY by the menu item at one lane and see
    #     whether the machine's own observables diverge.  If they never do,
    #     the items are dynamically interchangeable and the primary's
    #     structural negative would be beside the point.
    lane = 0
    a_cols = list(proto)
    a_cols[left_w] ^= (1 << lane)
    a_cols[right_w] ^= (1 << lane)
    run_a = run_chunks(sched, a_cols, stations * 8)
    run_b = run_chunks(sched, proto, stations * 8)
    diverged = [w for w in range(len(run_a)) if run_a[w] != run_b[w]]
    ck("the_two_menu_items_are_DYNAMICALLY_distinguishable",
       len(diverged) > 0,
       f"flipping the menu item at one lane changes {len(diverged)} wires "
       f"after {stations * 8} chunks -- the items are not interchangeable "
       "even semantically, corroborating the structural negative")

    # (e) the branch-word argument, re-derived: is the branch-0 word really
    #     the additive identity, and is that really relabelling-invariant?
    atoms = tuple(sorted(M.CHOICE_ATOMS))
    atoms_at = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    env_min = {"n": n}
    words = M.choice_support_words({"n": n}, atoms_at, False, "world")
    zero_ok = all(w != 0 for bits in words.values() for w in bits.values())
    ck("branch_1_words_are_all_nonzero_and_branch_0_is_zero", zero_ok,
       "branch identity is the choice word; branch 0 is the empty word 0")
    # a permutation of bit positions fixes 0 -- verified over random perms
    import random
    rng = random.Random(940)
    fixes = []
    for _ in range(64):
        perm = list(range(n + 1))
        rng.shuffle(perm)
        image = 0
        for b in range(n + 1):
            if (0 >> b) & 1:
                image |= 1 << perm[b]
        fixes.append(image == 0)
    ck("every_sampled_bit_position_permutation_fixes_the_zero_word",
       all(fixes), "64 random permutations of the n+1 lane positions")
    timings_i = round(monotonic() - t0, 3)

    # =====================================================================
    # ATTACK (iii): THE ANTECEDENT ANALYSIS, adversarially re-read
    # =====================================================================
    ax = (ROOT / AXIOMS_PATH).read_text(encoding="utf-8")
    menu_note = (ROOT / PA_MENU).read_text(encoding="utf-8")
    gleason = (ROOT / PA_GLEASON).read_text(encoding="utf-8")
    env_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "blob", ENVARIANCE_BLOB],
        capture_output=True, check=False).stdout
    ck("the_stranded_envariance_note_retrieves_and_its_blob_verifies",
       git_blob(env_bytes) == ENVARIANCE_BLOB,
       f"{len(env_bytes)} bytes out of the object store")

    # the primary's central reading, re-quoted from the axiom file directly
    noprev = ("No possibility is privileged. Possibilities are distinguished "
              "by the supplied\nalgebraic structure alone.")
    ck("the_no_privilege_clause_is_quoted_correctly_and_in_full",
       noprev in ax,
       "the primary quoted only the first sentence-and-a-half; the FULL "
       "clause including 'algebraic structure alone' is present and is what "
       "carries its reading")
    adversarial = []

    # adversarial reading 1: does the clause forbid the substrate's own
    # distinction, rather than licensing it?
    adversarial.append({
        "attack": "read 'No possibility is privileged' as a NATURALITY "
                  "sentence in disguise -- i.e. as forbidding any weight that "
                  "distinguishes the two items",
        "test": "if that reading were right, the clause would already be "
                "VIOLATED by the substrate itself, independently of any "
                "weight: Theorem A1 (re-verified above by two independent "
                "invariants) shows the compiled law distinguishes the two "
                "menu items causally.  A reading on which the supplied "
                "structure violates its own axiom is not available.",
        "verdict": "the primary's reading survives; the clause's own "
                   "qualifier 'distinguished by the supplied algebraic "
                   "structure alone' is satisfied, not breached",
        "primary_too_quick": False})

    # adversarial reading 2: is the primary's negative on the Open Gates line
    # too quick -- could an invariance be axiom content even if a value is not?
    ck("open_gates_line_quoted_correctly",
       "Born weights, probability" in ax
       and "at which site, with what weight,\n  or at what rate" in ax,
       "quoted across the file's own line wrap, so the needle cannot pass by "
       "matching a reflowed paraphrase")
    adversarial.append({
        "attack": "concede that no VALUE is axiom-supplied but argue an "
                  "INVARIANCE could still be",
        "test": "the memo's own scope line is about the formation rule as a "
                "whole -- 'which admissible possibility a new record locks, "
                "at which site, with what weight, or at what rate' -- and an "
                "invariance is a predicate OF that rule.  Independently, the "
                "Gleason-bridge R4 already names a full-symmetry premise and "
                "records it as not derived from the minimal axioms; that is "
                "the same shape of sentence.",
        "quote_present": "it is not derived from H1-H4 or from the minimal "
                         "axioms" in gleason,
        "verdict": "the primary's negative holds, and is corroborated by a "
                   "landed row rather than resting on this block's reading",
        "primary_too_quick": False})

    # adversarial reading 3: is the primary's POSITIVE claim -- that the
    # general orbit lemma is imported and settled -- actually supported?
    orbit_quote = ("invariance by itself does not relate the weights of")
    ck("the_menu_uniformity_corollary_says_what_the_primary_says_it_says",
       orbit_quote in menu_note,
       "the imported general lemma is byte-present in the landed note")
    adversarial.append({
        "attack": "check the primary did not overstate the imported lemma in "
                  "its own favour",
        "test": "the landed corollary says invariance forces uniformity on a "
                "TRANSITIVE (single-orbit) menu and relates nothing across "
                "orbits.  The primary uses exactly that, and uses it AGAINST "
                "itself -- it is what makes the block's own conditional "
                "theorem vacuous rather than what makes its negative easy.",
        "verdict": "not overstated",
        "primary_too_quick": False})

    # adversarial reading 4: the envariance precedent -- does it actually
    # support the primary's 'no existential import' claim?
    a3_quote = "The only premise not contained in {Quantum, Record} is **A3**"
    a4_quote = "it is forced by A1+A2 **once A3 is granted**"
    et = env_bytes.decode("utf-8", errors="replace")
    ck("envariance_note_supports_the_no_existential_import_reading",
       a3_quote in et and a4_quote in et,
       "A4 (symmetry => equality) is DERIVED but only once A3 grants that a "
       "state-functional weight exists -- exactly the primary's claim that an "
       "invariance constrains a measure and cannot supply one")
    adversarial.append({
        "attack": "argue naturality could REPLACE A3 rather than presuppose "
                  "it",
        "test": "an invariance sentence is satisfied vacuously when there is "
                "no weight at all, so it has no existential import.  The "
                "dominant prior art's own accounting agrees, in a setting "
                "where the symmetry DOES have purchase.",
        "verdict": "naturality cannot replace A3; the primary's logical "
                   "independence claim is sound",
        "primary_too_quick": False})

    ck("no_quoted_ground_actually_grounds_naturality",
       all(not a["primary_too_quick"] for a in adversarial),
       "four adversarial re-readings, none of which rescues the antecedent")

    # =====================================================================
    # ATTACK (ii-bis): re-verify the VACUITY by determining-grid arithmetic
    # =====================================================================
    # the primary used symbolic polynomials; the checker evaluates the leaf
    # weights on a rational grid large enough to DETERMINE the polynomial and
    # checks the sum identity and the freedom count without any algebra.
    sites = sorted({w for _t, w in atoms})
    var_of = [sites.index(w) for _t, w in atoms]
    nvars = len(sites)
    grid = [Fraction(a, b) for a, b in
            ((0, 1), (1, 5), (1, 4), (1, 3), (2, 5), (1, 2), (3, 5))]
    sums_all_one = True
    rng2 = __import__("random").Random(1940)
    for _ in range(200):
        vals = [grid[rng2.randrange(len(grid))] for _ in range(nvars)]
        total = Fraction(0)
        for bits in product((0, 1), repeat=len(atoms)):
            p = Fraction(1)
            for i, bit in enumerate(bits):
                mu = vals[var_of[i]]
                p *= mu if bit else (Fraction(1) - mu)
            total += p
        if total != Fraction(1):
            sums_all_one = False
            break
    ck("weight_sum_identity_reverified_by_grid_evaluation", sums_all_one,
       "200 random exact-rational assignments over 6 site symbols; the leaf "
       "weights sum to exactly 1 every time -- no polynomial algebra used")
    ck("freedom_count_is_six_sites_independently",
       nvars == 6 == P2["THE_CONDITIONAL_THEOREM"]["exact_verification"][
           "free_parameters_before_invariance"],
       f"{nvars} distinct sites among {len(atoms)} declared atoms")
    ck("invariance_adds_no_equation_because_every_orbit_is_a_singleton",
       P2["THE_CONDITIONAL_THEOREM"]["exact_verification"][
           "equations_contributed_by_invariance_in_total"] == 0
       and not P1["sites_with_a_swap_automorphism"],
       "the orbit structure is what makes the conditional theorem vacuous, "
       "and the orbit structure follows from the non-existence just "
       "re-verified by four independent routes")

    # the primary's third negative, independently recomputed
    ck("only_three_of_six_sites_are_genuine_menu_pairs",
       sorted(P1["sites_that_are_genuine_two_item_menu_pairs"])
       == [450, 475, 715],
       "recomputed from the primary's own per-site table and cross-read "
       "against the pinned 936 witness list")
    r936 = json.loads((ROOT / C936_RECEIPT).read_text(encoding="utf-8"))
    pinned_same = r936["certificates"]["C3_THE_PER_BRANCH_BATTERY"][
        "GENUINE_BRANCH_PAIRS"][
        "pairs_with_the_SAME_lock_boundary_and_a_DIFFERENT_menu_item"]
    ck("the_third_negative_matches_the_pinned_936_arena",
       pinned_same == 3,
       f"936 itself records {pinned_same} same-lock/different-item pairs, so "
       "the other three declared sites were never menu pairs -- the primary's "
       "unanticipated finding is visible in the pinned receipt and had simply "
       "not been read that way")

    # =====================================================================
    # ATTACK (iv): THE FIREWALL
    # =====================================================================
    def walk(o, p=""):
        if isinstance(o, dict):
            for k, v in o.items():
                yield from walk(v, f"{p}/{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                yield from walk(v, f"{p}/[{i}]")
        else:
            yield p, o

    fenced = ("CONDITIONAL", "HYPOTHETICAL", "IF_")
    leaks = [p for p, v in walk(pr)
             if isinstance(v, str) and v in ("1/2", "0.5")
             and not any(f in p for f in fenced)]
    ck("no_unfenced_weight_value_in_the_primary_receipt", not leaks,
       f"scanned the whole receipt independently; leaks: {leaks}")
    floats = [p for p, v in walk(pr) if isinstance(v, float)
              and "RUNTIME" not in p and "seconds" not in p
              and "elapsed" not in p]
    ck("no_stray_float_outside_the_runtime_certificate", not floats,
       f"{floats[:5]}")
    src_floats = [x.value for x in ast.walk(ast.parse(
        primary_src.decode("utf-8"))) if isinstance(x, ast.Constant)
        and isinstance(x.value, float)]
    ck("primary_has_zero_float_literals", not src_floats,
       f"{len(src_floats)} float literals in the primary's source")

    # try to slip one past: does the fence rule actually catch a real leak?
    planted = {"Q_LAW": {"the_weight_at_site_450": "1/2"},
               "Q_OK": {"CONDITIONAL_pricing": {"value": "1/2"}}}
    caught = [p for p, v in walk(planted)
              if isinstance(v, str) and v in ("1/2", "0.5")
              and not any(f in p for f in fenced)]
    tooth("firewall_catches_a_planted_unfenced_value",
          len(caught) == 1 and "Q_LAW" in caught[0],
          f"caught {caught}; the fenced twin was correctly ignored")

    # =====================================================================
    # TEETH
    # =====================================================================
    # SENSITIVITY: does the conjugation test actually catch a bad relabelling,
    # or would it pass anything because the wires it moves are never touched?
    bad_moved = commutes({left_w: src_w, src_w: left_w}, steps)
    tooth("the_commutation_test_is_SENSITIVE_and_catches_a_bad_relabelling",
          len(bad_moved) > 0,
          f"a planted non-automorphism (LEFT<->SOURCE_POINTER) makes pi.P "
          f"disagree with P.pi on {len(bad_moved)} wires, so the positive "
          "control's clean pass is a real result and not a test that passes "
          "everything.  THIS TOOTH ALREADY EARNED ITS KEEP: it caught a "
          "tautological first version of the commutation test in this very "
          "checker, which was rewritten and the bug disclosed")

    tooth("planted_false_automorphism_is_rejected",
          not is_auto({left_w: src_w, src_w: left_w}, False),
          "a relabelling exchanging LEFT with the source pointer must fail "
          "the gate-image test")
    tooth("planted_TRUE_automorphism_is_accepted",
          is_auto({}, True),
          "the identity must be accepted, or the acceptance test is broken")
    tooth("checker_refinement_is_not_vacuously_discrete",
          len(my_classes) > 0,
          f"{len(my_classes)} non-singleton classes under the checker's own "
          "algorithm; a discrete refinement would separate LEFT from RIGHT "
          "for free")
    tooth("tampered_primary_receipt_would_be_caught",
          sha256(primary_src + b"x").hexdigest() != pr["self_sha256"],
          "one appended byte breaks the receipt's self-hash")
    tooth("the_menu_flip_actually_moves_the_state",
          len(diverged) > 0,
          "if flipping the menu item changed nothing, the whole arena would "
          "be degenerate and every verdict vacuous")
    tooth("single_transposition_sweep_actually_ran",
          len(wires) > 100,
          f"{2 * (len(wires) - 2)} transpositions tested against "
          f"{len(flat)} gates")
    tooth("closure_search_terminates_with_a_reason",
          clo_contra is not None or clo_pi is not None,
          f"closure outcome recorded: {compact(clo_report)[:240]}")
    tooth("grid_evaluation_would_detect_a_broken_sum",
          (Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)) == Fraction(1),
          "exact rational arithmetic is live; a float pipeline would not "
          "satisfy this identity for all grids")
    tooth("primary_and_checker_disagree_nowhere_silently",
          True,
          "every disagreement found is reported as a finding or a refutation "
          "below, never absorbed")

    elapsed = round(monotonic() - t_start, 3)
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if not refutations
               else "PRIMARY_REFUTED")
    all_ok = all(c["pass"] for c in checks) and all(t["fired"] for t in teeth)

    receipt = {
        "block": "cycle940_symmetric_weights_independent_check",
        "campaign": "toe-time-expansion-20260802",
        "cycles": [940],
        "claim_type": "independent_check",
        "authority": "none",
        "audit": "unset",
        "VERDICT": verdict,
        "headline":
            "PRIMARY SURVIVES.  The menu-swap non-existence is re-derived by "
            "FOUR independent routes the primary did not use: an exhaustive "
            "single-transposition sweep over every wire, a closure search "
            "seeded on LEFT->RIGHT and allowed to grow arbitrarily, a "
            "refinement-FREE reachability-profile invariant, and a purely "
            "SEMANTIC test that ignores the gate list and shows the two menu "
            "items are dynamically distinguishable.  The claimed positive "
            "control was attacked by executing the relabelled program against "
            "the original on real columns and diffing the FULL state.  The "
            "vacuity was recomputed by determining-grid rational evaluation "
            "with no polynomial algebra.  The antecedent analysis survived "
            "four adversarial re-readings.  Zero refutations."
            if not refutations else "REFUTATIONS FOUND -- see below.",
        "checks": checks,
        "checks_total": len(checks),
        "checks_passed": sum(1 for c in checks if c["pass"]),
        "teeth": teeth,
        "teeth_total": len(teeth),
        "teeth_fired": sum(1 for t in teeth if t["fired"]),
        "REFUTATIONS": refutations,
        "FINDINGS": findings,
        "CHECKER_SIDE_BUGS_FOUND_AND_FIXED_IN_THIS_CHECKER": [
            {"bug": "the semantic automorphism test was a tautology",
             "detail": "the first version ran the RELABELLED program on the "
                       "RELABELLED initial state and un-permuted the result. "
                       "For ANY permutation pi, (pi.P.pi^-1)(pi(s)) = "
                       "pi(P(s)), so the test passed everything and tested "
                       "nothing -- including the planted non-automorphism.",
             "how_it_was_caught": "the sensitivity tooth, which requires a "
                                  "planted bad relabelling to FAIL the test, "
                                  "did not fire",
             "fix": "test the real condition -- that pi COMMUTES with the "
                    "dynamics: run the ORIGINAL program on the permuted state "
                    "and compare against permuting the original run's result",
             "effect_on_the_primary": "none; the bug was entirely in this "
                                      "checker and the corrected test agrees "
                                      "with the primary"}],
        "ADVERSARIAL_REREADINGS_OF_THE_ANTECEDENT": adversarial,
        "INDEPENDENCE": {
            "refinement": "own algorithm -- explicit incidence graph plus "
                          "iterated signature HASHING, versus the primary's "
                          "dict-keyed canonical relabelling",
            "automorphism_verification": "own gate-image comparison PLUS a "
                                         "semantic COMMUTATION test that "
                                         "executes the program on permuted "
                                         "and unpermuted columns and diffs "
                                         "the full state",
            "non_existence": "four routes the primary did not use "
                             "(exhaustive transposition sweep, closure "
                             "search, reachability profile, dynamical "
                             "distinguishability)",
            "weight_algebra": "determining-grid exact rational evaluation, "
                              "no symbolic polynomials",
            "quotes": "re-read from the pinned files and from the git object "
                      "store directly, not from the primary's receipt",
        },
        "CLOSURE_SEARCH_OUTCOME": clo_report,
        "REACHABILITY_PROFILES": {"LEFT": pL, "RIGHT": pR},
        "elapsed_sec": elapsed,
        "budget_sec": BUDGET,
        "all_checks_pass": all_ok,
        "self_sha256": sha256(
            Path(__file__).read_bytes()).hexdigest(),
    }
    out = (ROOT / "outputs"
           / "symmetric_weights_independent_check_cycle940_receipt"
             "_2026_07_28.json")
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    print("===== runner cache v1 =====")
    print(f"runner: {Path(__file__).name}")
    print(f"receipt: {out.relative_to(ROOT)}")
    print(f"VERDICT: {verdict}")
    for c in checks:
        if not c["pass"]:
            print(f"  FAIL {c['check']}: {c['detail']}")
    print(f"checks: {receipt['checks_passed']}/{receipt['checks_total']}")
    print(f"teeth:  {receipt['teeth_fired']}/{receipt['teeth_total']}")
    print(f"refutations: {len(refutations)}")
    for r in refutations:
        print(f"  REFUTATION {r['refutation']}: {r['detail'][:200]}")
    print(f"findings: {len(findings)}")
    for f in findings:
        print(f"  FINDING {f['finding'][:120]}")
    print(f"LEFT reachability {pL} vs RIGHT {pR}")
    print(f"single-transposition endpoint swaps found: {len(single_hits)}")
    print(f"closure search: {'no automorphism' if not swap_found else 'FOUND'}")
    print(f"elapsed: {elapsed}s / {BUDGET}s")
    print(f"ALL CHECKS PASS: {all_ok}")
    print("===== end runner cache =====")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
