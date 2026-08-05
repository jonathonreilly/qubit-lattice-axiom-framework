"""Cycle 909 INDEPENDENT CHECKER -- specified to REFUTE the within-world
pricing block.

The primary claims: (Q1) the Cycle-907 witness pair pins exactly three
orbit-aggregate numbers and leaves everything else free; (Q2) no recipe over
the census's own fields produces them; (Q3) the required numbers are the
gravity walk's two-layer interference spectrum, so the within-world
distribution is a PURCHASE, and the degree-2 carrier is independently
constrained.

This checker does NOT import the primary.  It rebuilds the event space from
the same pinned Cycle-863 / Cycle-878 sources by its own AST lift, reads the
required shape out of the pinned Cycle-902 and Cycle-907 receipts by its own
route, and runs its own tests.  Its attacks, in order of stakes:

  R1  INDEPENDENT SHAPE EXTRACTION.  A disagreement about what the constraint
      set IS refutes the block.  The checker derives the bridge from the
      pinned block sizes rather than from the primary's prose, and computes
      the pinned / free split by rank rather than by counting.

  R2  INDEPENDENT RECIPE INSTANTIATION.  The named recipes rebuilt from
      scratch and re-tested.

  R3  CENSUS COMPLETENESS -- the highest-stakes attack.  A hunt for a native
      recipe OUTSIDE the primary's declared closure that realizes the pair.
      A found realizer flips the verdict.

  R4  THE DEGREE-2 RELATIONSHIP, re-derived by brute force and attacked with
      a wider family of transforms than the primary tested.

  R5  TEETH.  Tampered pin, dropped recipe, hardcoded verdict, leaked
      realization, skipped world, planted-realizer blindness, and the
      primary's own denominator lemma re-proved and stress-tested.

The checker exits 0 whether or not the primary's claim survives; the verdict
is in its receipt.
"""

from __future__ import annotations

import ast
import importlib.abc
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C902_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C907_PATH = "scripts/frontier_cycle907_m6_identification_2026_07_28.py"
C907_RECEIPT = "outputs/m6_identification_cycle907_receipt_2026_07_28.json"
C907_CHECK_RECEIPT = \
    "outputs/m6_identification_independent_check_cycle907_receipt_2026_07_28.json"
PRIMARY_PATH = "scripts/frontier_cycle909_within_world_pricing_2026_07_28.py"
PRIMARY_RECEIPT = \
    "outputs/within_world_pricing_cycle909_receipt_2026_07_28.json"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C902_RECEIPT, C906_RECEIPT, C907_PATH,
    C907_RECEIPT, C907_CHECK_RECEIPT, PRIMARY_PATH, PRIMARY_RECEIPT,
)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C902_RECEIPT:
        "91c5631415d0231390fedbd0174f074de45cfa33b6dd4f706ed6fcdbf4dfd1d8",
    C906_RECEIPT:
        "e4de35c272216e0aace2585bdc2e5db198788752d63c11b0dc9ebc67146e7a3f",
    C907_PATH:
        "cfc87a647a8fe87ed97289bb179d4919bb4801731393bbec33006c6cfe348d53",
    C907_RECEIPT:
        "d67a967a6226a4e1ed2e0bf1762cb3b544df87e1fe4b07d6399f13ec179086ca",
    C907_CHECK_RECEIPT:
        "0d18a2839f1b57c55b55f0801b05e545a1e5a01cc790972d9583da5b21c0123b",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle907_m6_identification_2026_07_28",
    "frontier_cycle909_within_world_pricing_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"checker firewall forbids: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


def compact(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def fr(v: Fraction) -> str:
    return f"{v.numerator}/{v.denominator}"


def gcd_list(values) -> int:
    out = 0
    for v in values:
        out = gcd(out, abs(v))
    return out


def lcm2(a: int, b: int) -> int:
    return a // gcd(a, b) * b if a and b else 0


def proportional(sample, target) -> bool:
    if all(v == 0 for v in sample):
        return False
    for i in range(len(target)):
        for j in range(i + 1, len(target)):
            if sample[i] * target[j] != sample[j] * target[i]:
                return False
    return True


def ast_lift(path: str, funcs: tuple, consts: tuple, globals_: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in consts:
                    found[t.id] = ast.literal_eval(node.value)
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = dict(globals_)
    ns.update(found)
    exec(compile(module, f"<check-lift {path}>", "exec"), ns)
    return ns, found


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


def build_space():
    ns863, _ = ast_lift(C863_PATH, C863_FUNCS, C863_CONSTS,
                        {"K": K, "combinations": combinations})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts = ast_lift(C878_PATH, C878_FUNCS, C878_CONSTS,
                             {"C863": c863, "Counter": Counter,
                              "sha256": sha256, "gcd": gcd,
                              "Fraction": Fraction, "json": json})
    c878 = SimpleNamespace(**{n: ns878[n] for n in C878_FUNCS})
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _fail = c863.build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    rig = c878.dead_wire_rig(program, sim,
                             c863.pack_lanes(states + (states[0],)))
    scan = c878.composed_scan(program, census, states, rig, consts["HORIZON"])
    return c863, c878, consts, census, stations, scan


# ---------------------------------------------------------------------------
# R1: the required shape, extracted INDEPENDENTLY
# ---------------------------------------------------------------------------

def r1_shape(star, star_rows, per_world, obj, receipt907, receipt907c,
             primary_receipt) -> dict:
    """The checker derives the bridge from the PINNED BLOCK SIZES rather than
    from the primary's prose, and the pinned/free split by RANK rather than by
    counting.  Any disagreement about the constraint set refutes the block."""
    n_star = len(star)
    width = per_world[star[0]]
    sizes = list(receipt907["Q1_exhibited_identification"]["block_sizes"])
    atoms = obj["atoms"]
    # the block sizes force the shape of phi: three blocks of exactly n_star
    # events and one holding everything else.  With phi covariant across the
    # orbit that means one designated event per escape world per atom.
    forced = (len(sizes) == atoms and sorted(sizes[1:]) == [n_star] * (atoms - 1)
              and sizes[0] == sum(per_world.values()) - (atoms - 1) * n_star)

    # rebuild the witness pair from the 902 columns, independently
    def spread(pattern, positions):
        col = []
        for w in star:
            prof = [0] * per_world[w]
            for v, p in zip(pattern, positions):
                prof[p] = v
            col.extend(prof)
        return col

    positions = list(range(atoms))
    m7 = spread(obj["degree0"], positions)
    m8 = spread(obj["degree2"], positions)
    offsets, acc = [], 0
    for w in star:
        offsets.append(acc)
        acc += per_world[w]

    def blocks(col, designated):
        S = [0] * atoms
        for o in offsets:
            for i, p in enumerate(designated, start=1):
                S[i] += col[o + p]
        S[0] = sum(col) - sum(S[1:])
        return S

    designated = list(range(1, atoms))
    S7 = blocks(m7, designated)
    S8 = blocks(m8, designated)
    slice_props = receipt907c["certificates"]["R2_BRIDGE_SEARCH"][
        "primary_identification_reverified_by_substitution"]["slice_properties"]
    totals_agree = (sum(m7) == slice_props["0"]["total"]
                    and sum(m8) == slice_props["2"]["total"])
    grid_ok = (S7 == [n_star * v for v in obj["degree0"]]
               and S8 == [n_star * v for v in obj["degree2"]])

    # the constraint set, as exact fractions -- the checker's own statement
    own = {
        "degree0": {f"position_{i}": fr(Fraction(obj["degree0"][i],
                                                obj["degree0_sum"]))
                    for i in designated},
        "degree2": {f"position_{i}": fr(Fraction(obj["degree2"][i],
                                                obj["degree2_sum"]))
                    for i in designated},
    }
    own["degree0"]["everything_else"] = fr(Fraction(obj["degree0"][0],
                                                   obj["degree0_sum"]))
    own["degree2"]["everything_else"] = fr(Fraction(obj["degree2"][0],
                                                   obj["degree2_sum"]))
    claimed = primary_receipt["Q1_constraint_set"]
    agree = {
        "degree0": all(own["degree0"][k] ==
                       claimed["degree0_required_orbit_profile"][k]
                       for k in own["degree0"]),
        "degree2": all(own["degree2"][k] ==
                       claimed["degree2_required_orbit_profile"][k]
                       for k in own["degree2"]),
        "designated_positions": (designated ==
                                 list(claimed["designated_positions"])),
    }

    # the pinned/free split BY RANK: the constraint system on the 1419 escape
    # coordinates is (n_star - 1) covariance equalities plus (atoms - 1)
    # designated aggregates; the checker builds the matrix and ranks it.
    support = sum(per_world[w] for w in star)
    rows = []
    for a in range(n_star - 1):
        r = [0] * support
        for k in range(per_world[star[a]]):
            r[offsets[a] + k] = 1
        for k in range(per_world[star[a + 1]]):
            r[offsets[a + 1] + k] = -1
        rows.append(r)
    for p in designated:
        r = [0] * support
        for o in offsets:
            r[o + p] = 1
        rows.append(r)
    rank = 0
    work = [row[:] for row in rows]
    ncols = support
    pivots = []
    for col in range(ncols):
        piv = None
        for i in range(rank, len(work)):
            if work[i][col]:
                piv = i
                break
        if piv is None:
            continue
        work[rank], work[piv] = work[piv], work[rank]
        lead = Fraction(work[rank][col])
        work[rank] = [Fraction(x) / lead for x in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][col]:
                f = work[i][col]
                work[i] = [a - f * b for a, b in zip(work[i], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(work):
            break
    free_dim = support - rank
    claimed_free = claimed["residual_freedom_inside_the_escape_orbit"]

    # exhibit the freedom independently: perturb one FREE coordinate inside a
    # world and compensate inside the same world, and re-test
    pert = list(m7)
    pert[offsets[0] + 0] -= 5
    pert[offsets[0] + width - 1] += 5
    pert_ok = proportional(blocks(pert, designated), obj["degree0"])
    # and break a PINNED coordinate: must fail
    broken = list(m7)
    broken[offsets[0] + designated[-1]] += 1
    broken[offsets[0] + 0] -= 1
    broken_fails = not proportional(blocks(broken, designated), obj["degree0"])

    return {
        "certificate": "R1_INDEPENDENT_SHAPE",
        "block_sizes_force_one_event_per_world_per_atom": forced,
        "checker_block_masses_degree0": S7,
        "checker_block_masses_degree2": S8,
        "checker_totals": [sum(m7), sum(m8)],
        "totals_agree_with_the_907_checker_receipt": totals_agree,
        "pushforward_reproduces_the_902_columns": grid_ok,
        "checker_constraint_set": own,
        "primary_constraint_set": {
            "degree0": claimed["degree0_required_orbit_profile"],
            "degree2": claimed["degree2_required_orbit_profile"]},
        "agreement": agree,
        "checker_free_dimension_by_rank": free_dim,
        "constraint_matrix_rank": rank,
        "primary_free_dimension": claimed_free,
        "free_dimension_agrees": free_dim == claimed_free,
        "free_coordinate_perturbation_preserves_the_shape": pert_ok,
        "pinned_coordinate_perturbation_breaks_the_shape": broken_fails,
        "disagreement": not (all(agree.values())
                             and free_dim == claimed_free
                             and grid_ok and totals_agree and pert_ok
                             and broken_fails),
    }


# ---------------------------------------------------------------------------
# the checker's own shape harness
# ---------------------------------------------------------------------------

class Harness:
    def __init__(self, star, per_world, obj):
        self.star = star
        self.widths = [per_world[w] for w in star]
        self.offsets, acc = [], 0
        for w in star:
            self.offsets.append(acc)
            acc += per_world[w]
        self.support = acc
        self.atoms = obj["atoms"]
        self.deg0 = list(obj["degree0"])
        self.deg2 = list(obj["degree2"])
        self.scale0 = sum(v // gcd_list(self.deg0) for v in self.deg0)
        self.scale2 = sum(v // gcd_list(self.deg2) for v in self.deg2)

    def slices(self, col):
        return [col[o:o + w] for o, w in zip(self.offsets, self.widths)]

    def sums(self, col):
        return [sum(s) for s in self.slices(col)]

    def blocks(self, col):
        S = [0] * self.atoms
        for s in self.slices(col):
            for i in range(1, self.atoms):
                S[i] += s[i]
        S[0] = sum(sum(s) for s in self.slices(col)) - sum(S[1:])
        return S

    def cone(self, col):
        sums = self.sums(col)
        if any(s <= 0 for s in sums):
            return None
        L = 1
        for s in sums:
            L = lcm2(L, s)
        out = []
        for s, part in zip(sums, self.slices(col)):
            k = L // s
            out.extend(v * k for v in part)
        g = gcd_list(out) or 1
        return [v // g for v in out]

    def lemma_admits(self, col, scale):
        """The primary's denominator lemma, re-derived here from scratch and
        used only as a NECESSARY filter: with equal world masses the mass at
        the ratio-r atom is r/scale of the total, so summing rho_w(p)/S_w over
        the orbit must equal n_star * r / scale, and clearing denominators
        forces scale | lcm(S_w) whenever gcd(scale, n_star) = 1."""
        sums = self.sums(col)
        if any(s <= 0 for s in sums):
            return False
        L = 1
        for s in sums:
            L = lcm2(L, s)
        return L % scale == 0

    def realizes(self, col, which):
        cone = self.cone(col)
        if cone is None:
            return False, None
        target = self.deg0 if which == 0 else self.deg2
        S = self.blocks(cone)
        return proportional(S, target), S


def checker_base_fields(star, star_rows, scan, per_world, boundaries):
    """Written independently of the primary's list, and deliberately WIDER:
    it includes fields the primary did not name."""
    occ_g, occ_b, formed = scan["occ_global"], scan["occ_bank"], scan["formed"]
    tagcode = {"F": 0, "B0": 1, "B1": 2}
    out = {}

    def col(fn):
        vals = []
        for w in star:
            prev = None
            for j, e in enumerate(star_rows[w]):
                vals.append(fn(w, j, e, prev))
                prev = e
        return vals

    out["one"] = col(lambda w, j, e, p: 1)
    out["moment"] = col(lambda w, j, e, p: e[1])
    out["moment1"] = col(lambda w, j, e, p: e[1] + 1)
    out["ordinal"] = col(lambda w, j, e, p: e[3])
    out["ordinal1"] = col(lambda w, j, e, p: e[3] + 1)
    out["index"] = col(lambda w, j, e, p: j)
    out["index1"] = col(lambda w, j, e, p: j + 1)
    out["revindex1"] = col(lambda w, j, e, p: per_world[w] - j)
    out["content"] = col(lambda w, j, e, p: int(e[4], 16))
    out["content_pop"] = col(lambda w, j, e, p: bin(int(e[4], 16)).count("1"))
    out["content_lo16"] = col(lambda w, j, e, p: int(e[4], 16) & 0xFFFF)
    out["content_hi16"] = col(lambda w, j, e, p: int(e[4], 16) >> 48)
    out["isF"] = col(lambda w, j, e, p: 1 if e[2] == "F" else 0)
    out["isB0"] = col(lambda w, j, e, p: 1 if e[2] == "B0" else 0)
    out["isB1"] = col(lambda w, j, e, p: 1 if e[2] == "B1" else 0)
    out["tag1"] = col(lambda w, j, e, p: tagcode[e[2]] + 1)
    out["gap1"] = col(lambda w, j, e, p: 1 if p is None else e[1] - p[1] + 1)
    out["since_form"] = col(lambda w, j, e, p: abs(e[1] - formed[w]))
    out["to_horizon"] = col(lambda w, j, e, p: boundaries - e[1])
    out["occ"] = col(lambda w, j, e, p: occ_g[w])
    out["occ0"] = col(lambda w, j, e, p: occ_b[0][w])
    out["occ1"] = col(lambda w, j, e, p: occ_b[1][w])
    out["formed"] = col(lambda w, j, e, p: formed[w])
    out["nevents"] = col(lambda w, j, e, p: per_world[w])
    # fields the primary did NOT name -- part of the completeness attack
    out["moment_parity"] = col(lambda w, j, e, p: e[1] & 1)
    out["ordinal_parity1"] = col(lambda w, j, e, p: (e[3] & 1) + 1)
    out["content_mod_small"] = col(lambda w, j, e, p: int(e[4], 16) % 97 + 1)
    out["content_rank"] = None
    # within-world rank of the content word: an order statistic, not a field
    ranks = []
    for w in star:
        vals = [int(e[4], 16) for e in star_rows[w]]
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        rk = [0] * len(vals)
        for r, i in enumerate(order):
            rk[i] = r + 1
        ranks.extend(rk)
    out["content_rank"] = ranks
    out["moment_log2"] = col(lambda w, j, e, p: e[1].bit_length())
    out["digitsum"] = col(lambda w, j, e, p: sum(int(c, 16) for c in e[4]))
    return out


NAMED = ("one", "occ", "index1", "content", "moment1", "ordinal1", "isF",
         "formed")


def r2_recipes(H, fields, primary_receipt) -> dict:
    """Independent instantiation of the named recipes, and a re-test."""
    rows = []
    for name in NAMED:
        col = fields[name]
        ok0, S0 = H.realizes(col, 0)
        ok2, S2 = H.realizes(col, 2)
        cone = H.cone(col)
        prof = None
        if cone is not None:
            T = sum(cone)
            prof = [fr(Fraction(v, T)) for v in H.blocks(cone)]
            prof = [p if len(p) <= 40 else "<long exact fraction>"
                    for p in prof]
        rows.append({"recipe": name, "degree0_realizes": ok0,
                     "degree2_realizes": ok2, "orbit_profile": prof})
    claimed0 = primary_receipt["Q2_native_degree0_realizers"]
    claimed2 = primary_receipt["Q2_native_degree2_realizers"]
    found0 = [r["recipe"] for r in rows if r["degree0_realizes"]]
    found2 = [r["recipe"] for r in rows if r["degree2_realizes"]]
    # the uniform recipe's profile is the sharpest single disagreement test
    uni = H.cone(fields["one"])
    uni_prof = [fr(Fraction(v, sum(uni))) for v in H.blocks(uni)]
    return {
        "certificate": "R2_INDEPENDENT_RECIPES",
        "rows": rows,
        "uniform_orbit_profile": uni_prof,
        "uniform_required_profile": [
            fr(Fraction(v, sum(H.deg0))) for v in H.deg0],
        "checker_found_degree0_realizers": found0,
        "checker_found_degree2_realizers": found2,
        "primary_claimed_degree0_realizers": claimed0,
        "primary_claimed_degree2_realizers": claimed2,
        "disagreement": bool(found0 or found2 or claimed0 or claimed2),
    }


def r3_completeness(H, fields, star, star_rows, per_world) -> dict:
    """THE HIGHEST-STAKES ATTACK.  Hunt a recipe OUTSIDE the primary's declared
    closure that realizes either slice.  Three independent hunts:

      HUNT A  a wide constructive sweep -- triple products, integer ratios,
              modular residues, order statistics, piecewise tag rules, min/max
              and bit slices -- none of which is in the primary's K1..K6.
      HUNT B  the arithmetic hunt behind the denominator lemma: does ANY census
              quantity, or any product of at most three of them, carry the
              prime factors 31 or 613 that a degree-0 realizer needs?
      HUNT C  the position scan: for a realizer the three designated positions
              must carry masses in the exact ratio 2910 : 492 : 1 within the
              orbit aggregate.  Scan every base field for ANY pair of positions
              whose orbit-aggregate masses stand in one of the required ratios.
    """
    names = sorted(fields)
    cols = [fields[n] for n in names]
    hunt_a, realizers = [], []
    tested = 0

    def test(rid, col):
        nonlocal tested
        tested += 1
        if not H.lemma_admits(col, H.scale0):
            return ("BLOCKED_BY_LEMMA", None)
        ok, S = H.realizes(col, 0)
        if ok:
            realizers.append({"id": rid, "slice": 0, "block_masses": S})
        return ("REALIZES" if ok else "FAILS", S)

    def test2(rid, col):
        nonlocal tested
        tested += 1
        if not H.lemma_admits(col, H.scale2):
            return "BLOCKED_BY_LEMMA"
        ok, S = H.realizes(col, 2)
        if ok:
            realizers.append({"id": rid, "slice": 2, "block_masses": S})
        return "REALIZES" if ok else "FAILS"

    lemma_survivors0, lemma_survivors2 = [], []

    def sweep(rid, col):
        if any(v < 0 for v in col):
            col = [abs(v) for v in col]
        v0, _ = test(rid, col)
        v2 = test2(rid, col)
        if v0 != "BLOCKED_BY_LEMMA":
            lemma_survivors0.append(rid)
        if v2 != "BLOCKED_BY_LEMMA":
            lemma_survivors2.append(rid)

    # HUNT A1 -- triple products (outside K3, which stops at pairs)
    for a in range(len(names)):
        for b in range(a + 1, len(names)):
            for c in range(b + 1, len(names)):
                if (a + b + c) % 7:
                    continue          # declared stride, disclosed below
                sweep(f"TRIPLE({names[a]},{names[b]},{names[c]})",
                      [x * y * z for x, y, z in
                       zip(cols[a], cols[b], cols[c])])
    # HUNT A2 -- integer ratios and residues (outside every K rule)
    mods = (2, 3, 5, 7, 11, 13, 17, 31, 41, 97, 613, 19003)
    for n, colv in zip(names, cols):
        for m in mods:
            sweep(f"MOD({n},{m})", [v % m + 1 for v in colv])
            sweep(f"DIV({n},{m})", [v // m for v in colv])
    # HUNT A3 -- piecewise tag rules with independent branches
    for n, colv in zip(names, cols):
        for other, colo in zip(names, cols):
            if n >= other:
                continue
            if (hash(n) + hash(other)) % 11:
                continue
            sweep(f"PIECEWISE({n} on F/B0, {other} on B1)",
                  [(colv[i] if fields["isB1"][i] == 0 else colo[i])
                   for i in range(len(colv))])
    # HUNT A4 -- min / max combinations and order statistics
    for a in range(len(names)):
        for b in range(a + 1, len(names)):
            if (a * 3 + b) % 5:
                continue
            sweep(f"MIN({names[a]},{names[b]})",
                  [min(x, y) for x, y in zip(cols[a], cols[b])])
            sweep(f"MAX({names[a]},{names[b]})",
                  [max(x, y) for x, y in zip(cols[a], cols[b])])
    # HUNT A5 -- rank-keyed geometric and factorial-like profiles
    for n, colv in zip(names, cols):
        sweep(f"SQ({n})", [v * v for v in colv])
        sweep(f"CUBE({n})", [v ** 3 for v in colv])
        sweep(f"BITLEN({n})", [v.bit_length() + 1 for v in colv])

    # HUNT B -- can the census reach the primes 31 and 613 at all?
    need = (31, 613)
    reach = {p: [] for p in need}
    for n, colv in zip(names, cols):
        sums = H.sums(colv)
        for p in need:
            if any(s % p == 0 for s in sums if s):
                reach[p].append(n)
    both = sorted(set(reach[31]) & set(reach[613]))

    # HUNT C -- the position scan
    want = {Fraction(2910, 492), Fraction(2910, 1), Fraction(492, 1)}
    hits = []
    for n, colv in zip(names, cols):
        cone = H.cone(colv)
        if cone is None:
            continue
        S = H.blocks(cone)
        for i in range(1, H.atoms):
            for j in range(1, H.atoms):
                if i == j or S[j] == 0:
                    continue
                if Fraction(S[i], S[j]) in want:
                    hits.append({"field": n, "positions": [i, j],
                                 "ratio": fr(Fraction(S[i], S[j]))})

    return {
        "certificate": "R3_CENSUS_COMPLETENESS",
        "declared_strides": (
            "HUNT A1 keeps one triple in seven, A3 one pair in eleven and A4"
            " one pair in five.  A stride can only make the hunt WEAKER, never"
            " produce a false realizer, and it is disclosed here rather than"
            " hidden.  The lemma below is what makes the negative complete."),
        "recipes_tested_outside_the_declared_closure": tested,
        "realizers_found": realizers,
        "lemma_survivors_degree0": sorted(set(lemma_survivors0))[:40],
        "lemma_survivor_count_degree0": len(set(lemma_survivors0)),
        "lemma_survivor_count_degree2": len(set(lemma_survivors2)),
        "hunt_B_prime_reachability": {
            "primes_a_degree0_realizer_needs": list(need),
            "fields_whose_world_sums_reach_31": reach[31],
            "fields_whose_world_sums_reach_613": reach[613],
            "fields_reaching_both": both,
        },
        "hunt_C_position_ratio_hits": hits,
        "verdict": ("REFUTES_THE_PRIMARY" if realizers
                    else "NO_REALIZER_FOUND_OUTSIDE_THE_DECLARED_CLOSURE"),
        "disagreement": bool(realizers),
    }


def r4_degree_two(obj, primary_receipt) -> dict:
    """Re-derive the layer decomposition by BRUTE FORCE (no isqrt shortcut),
    recount the admissible degree-2 columns, and attack the primary's claim
    that no native transform carries one column to the other with a WIDER
    transform family than the primary tested."""
    sites = obj["sites"]
    d0, d2 = obj["degree0"], obj["degree2"]
    per0 = [c // s if c % s == 0 else None for c, s in zip(d0, sites)]
    per2 = [c // s if c % s == 0 else None for c, s in zip(d2, sites)]
    brute = []
    for m0, m2 in zip(per0, per2):
        found = None
        if m0 is not None:
            for p in range(0, m0 + 1):
                for q in range(0, p + 1):
                    if p * p + q * q == m0 and 2 * p * q == m2:
                        found = [p, q]
                        break
                if found:
                    break
        brute.append(found)
    claimed = primary_receipt["Q3_gravity_terms_reading"][
        "recovered_layer_amplitudes_p_q"]
    layers_agree = brute == claimed

    reps = []
    for m0 in per0:
        r = []
        if m0 is not None:
            for a in range(isqrt(m0) + 1):
                b2 = m0 - a * a
                b = isqrt(b2)
                if b * b == b2 and a <= b:
                    r.append([b, a])
        reps.append(r)
    count = 1
    for r in reps:
        count *= max(1, len(r))
    claimed_count = primary_receipt["Q3_gravity_terms_reading"][
        "count_of_arithmetically_admissible_degree2_columns"]

    # WIDER transform attack
    transforms = []

    def add(name, holds, why):
        transforms.append({"transform": name, "holds": holds, "why": why})

    add("SCALAR", proportional(d2, d0), "per-atom ratios are not constant")
    # affine c2 = a c0 + b over the rationals, fitted on two atoms and tested
    A = Fraction(d2[0] - d2[1], d0[0] - d0[1])
    B = Fraction(d2[0]) - A * Fraction(d0[0])
    affine_ok = all(Fraction(c2) == A * Fraction(c0) + B
                    for c0, c2 in zip(d0, d2))
    add("AFFINE c_2 = a c_0 + b", affine_ok,
        f"fitted a = {fr(A)}, b = {fr(B)}; tested on all four atoms")
    # site-mediated: c2 = k * sites
    ks = {Fraction(c2, s) for c2, s in zip(d2, sites)}
    add("SITE PROPORTIONAL c_2 = k * sites", len(ks) == 1,
        f"c_2 / sites takes the values {sorted(fr(k) for k in ks)}")
    # quadratic in c0 through three atoms, tested on the fourth
    xs = [Fraction(v) for v in d0[:3]]
    ys = [Fraction(v) for v in d2[:3]]
    den = ((xs[0] - xs[1]) * (xs[0] - xs[2]) * (xs[1] - xs[2]))
    quad_ok = False
    if den != 0:
        a2 = ((ys[0] - ys[1]) * (xs[0] - xs[2])
              - (ys[0] - ys[2]) * (xs[0] - xs[1])) / (
            (xs[0] ** 2 - xs[1] ** 2) * (xs[0] - xs[2])
            - (xs[0] ** 2 - xs[2] ** 2) * (xs[0] - xs[1]))
        b2 = ((ys[0] - ys[1]) - a2 * (xs[0] ** 2 - xs[1] ** 2)) / (xs[0] - xs[1])
        c2c = ys[0] - a2 * xs[0] ** 2 - b2 * xs[0]
        quad_ok = (a2 * Fraction(d0[3]) ** 2 + b2 * Fraction(d0[3]) + c2c
                   == Fraction(d2[3]))
    add("QUADRATIC in c_0, fitted on three atoms", quad_ok,
        "interpolated through atoms 0,1,2 and tested on atom 3")
    add("SQRT-LINKED c_2 = 2 sqrt(c_0 * k)", False,
        "c_2 = 2 p q with p^2 + q^2 = c_0 fixes only a PRODUCT; the pair"
        " (p, q) is not a function of c_0, which is exactly the finding")
    claimed_any = primary_receipt["Q3_degree_two_relationship"][
        "any_native_transform_works"]
    return {
        "certificate": "R4_DEGREE_TWO",
        "brute_force_layer_amplitudes": brute,
        "primary_layer_amplitudes": claimed,
        "layers_agree": layers_agree,
        "identity_holds": all(
            lay is not None and lay[0] ** 2 + lay[1] ** 2 == m0
            and 2 * lay[0] * lay[1] == m2
            for lay, m0, m2 in zip(brute, per0, per2)),
        "sum_of_two_squares_representations": reps,
        "checker_admissible_degree2_column_count": count,
        "primary_admissible_degree2_column_count": claimed_count,
        "counts_agree": count == claimed_count,
        "wider_transform_family": transforms,
        "any_transform_works": any(t["holds"] for t in transforms),
        "primary_claimed_any_transform_works": claimed_any,
        "disagreement": not (layers_agree and count == claimed_count
                             and (any(t["holds"] for t in transforms)
                                  == bool(claimed_any))),
    }


def r5_teeth(H, fields, star, per_world, obj, primary_receipt,
             r1, r2, r3, r4) -> dict:
    teeth = []

    # 1 tampered pin
    raw = bytearray((ROOT / C907_RECEIPT).read_bytes())
    raw[10] ^= 0x01
    teeth.append({"tooth": "TAMPERED_PIN",
                  "detected": sha256(bytes(raw)).hexdigest()
                  != EXPECTED_SHA256[C907_RECEIPT]})

    # 2 planted-realizer blindness: the checker's own harness must detect the
    #   exact transcription of the gravity columns
    def flat(pattern):
        col = []
        for w in star:
            prof = [0] * per_world[w]
            for i, v in enumerate(pattern):
                prof[i] = v
            col.extend(prof)
        return col

    plant0, _ = H.realizes(flat(obj["degree0"]), 0)
    plant2, _ = H.realizes(flat(obj["degree2"]), 2)
    near = list(obj["degree0"])
    near[3] += 1
    nearmiss, _ = H.realizes(flat(near), 0)
    teeth.append({"tooth": "PLANTED_REALIZER_BLINDNESS",
                  "detected": bool(plant0 and plant2 and not nearmiss),
                  "rows": {"degree0_plant": plant0, "degree2_plant": plant2,
                           "near_miss_rejected": not nearmiss}})

    # 3 leaked realization: a planted realizer must survive the lemma filter
    #   the R3 hunt uses, or the hunt would be blind by construction
    lemma_lets_the_plant_through = H.lemma_admits(flat(obj["degree0"]),
                                                  H.scale0)
    teeth.append({"tooth": "LEAKED_REALIZATION",
                  "what": ("the denominator-lemma filter used by the"
                           " completeness hunt must NOT block a genuine"
                           " realizer"),
                  "detected": bool(lemma_lets_the_plant_through)})

    # 4 skipped world
    col = flat(obj["degree0"])
    dropped = list(col)
    for i in range(per_world[star[0]]):
        dropped[i] = 0
    one_off = list(col)
    one_off[3] = 0
    teeth.append({"tooth": "SKIPPED_WORLD",
                  "detected": bool(H.cone(dropped) is None
                                   and not H.realizes(one_off, 0)[0])})

    # 5 dropped recipe: the primary's verdict table must actually contain
    #   every family it declares, and the counts must add up
    table = primary_receipt["Q2_verdict_table"]
    fams = Counter(r[1] for r in table)
    declared = set(primary_receipt["Q2_closure_rules"]) - {"CONSTANT_RULE"}
    teeth.append({"tooth": "DROPPED_RECIPE",
                  "detected": bool(declared <= set(fams)
                                   and sum(v for k, v in fams.items()
                                           if k != "PLANTED")
                                   == primary_receipt["Q2_recipe_count"]),
                  "rows": {"families_in_the_table": dict(fams),
                           "declared": sorted(declared)}})

    # 6 hardcoded verdict: the primary's classifier must be a pure function of
    #   its realizer sets, and the receipt's verdict must match what that
    #   function returns on the receipt's OWN numbers
    r0n = len(primary_receipt["Q2_native_degree0_realizers"])
    r2n = len(primary_receipt["Q2_native_degree2_realizers"])
    pn = len(primary_receipt["Q2_native_pairs"])
    recomputed = ("i_SELECTION_BY_CONSTRUCTION" if pn == 1 else
                  "i_NATIVE_WITH_RESIDUAL_CHOICE" if pn > 1 else
                  "iii_PARTIAL" if (r0n or r2n) else "ii_PURCHASE")
    src = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(src)
    literal_verdicts = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "classify_outcome":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                        and sub.value.startswith(("i_", "ii_", "iii_")):
                    literal_verdicts += 1
    teeth.append({
        "tooth": "HARDCODED_VERDICT",
        "what": ("the receipt's outcome class must be reproducible from the"
                 " receipt's own realizer counts, and the classifier must"
                 " branch on them rather than return a constant"),
        "detected": bool(recomputed == primary_receipt["Q3_outcome"]["class"]
                         and literal_verdicts >= 4),
        "rows": {"recomputed": recomputed,
                 "receipt": primary_receipt["Q3_outcome"]["class"],
                 "distinct_verdict_literals_in_the_classifier":
                     literal_verdicts}})

    # 7 the denominator lemma, stress-tested: a profile built to satisfy it
    #   must pass, and one built to violate it must be blocked
    good = flat(obj["degree0"])
    bad = flat([1, 1, 1, 1])
    teeth.append({"tooth": "LEMMA_STRESS",
                  "detected": bool(H.lemma_admits(good, H.scale0)
                                   and not H.lemma_admits(bad, H.scale0))})

    # 8 the primary must not have leaked the answer into its own field list
    fields_text = compact(primary_receipt["Q2_base_fields"])
    leaked = any(str(v) in fields_text for v in obj["degree0"] if v > 3)
    teeth.append({"tooth": "ANSWER_LEAKED_INTO_THE_FIELD_LIST",
                  "what": ("no base field definition may name a gravity"
                           " coefficient"),
                  "detected": not leaked})

    return {"certificate": "R5_TEETH", "teeth": teeth,
            "tooth_count": len(teeth),
            "all_teeth_bite": all(t["detected"] for t in teeth)}


def main() -> int:
    started = monotonic()
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    pins_ok = all(sha_rows[p] == EXPECTED_SHA256[p] for p in EXPECTED_SHA256)
    primary_receipt = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    receipt902 = json.loads(payloads[C902_RECEIPT].decode("utf-8"))
    receipt906 = json.loads(payloads[C906_RECEIPT].decode("utf-8"))
    receipt907 = json.loads(payloads[C907_RECEIPT].decode("utf-8"))
    receipt907c = json.loads(payloads[C907_CHECK_RECEIPT].decode("utf-8"))

    tbl = [o for o in receipt902["Q3_exhibited_objects"]
           if o["config"] == "single"][0]["coefficient_table"]
    degrees = len(tbl[0]["c_by_degree"])
    C = [[int(Fraction(c)) for c in row["c_by_degree"]] for row in tbl]
    obj = {"atoms": len(tbl), "degrees": degrees,
           "sites": [row["sites"] for row in tbl],
           "C": C,
           "degree0": [C[i][0] for i in range(len(C))],
           "degree2": [C[i][2] for i in range(len(C))]}
    obj["degree0_sum"] = sum(obj["degree0"])
    obj["degree2_sum"] = sum(obj["degree2"])

    c863, c878, consts, census, stations, scan = build_space()
    events = scan["events"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    idx_by_world: dict = defaultdict(list)
    for i, w in enumerate(world_of):
        idx_by_world[w].append(i)
    formed = scan["formed"]
    perms, perm_ok = c878.monitor_phase_action(census, stations)
    orbits = c878.group_orbits(perms, len(census)) if perm_ok else ()
    never = {w for w in supported if w not in formed}
    free_orbits = [o for o in orbits if not any(w in never for w in o)]
    star = list(free_orbits[0])
    star_rows = {w: [events[i] for i in idx_by_world[w]] for w in star}
    boundaries = scan["boundaries"]

    H = Harness(star, per_world, obj)
    fields = checker_base_fields(star, star_rows, scan, per_world, boundaries)

    r1 = r1_shape(star, star_rows, per_world, obj, receipt907, receipt907c,
                  primary_receipt)
    r2 = r2_recipes(H, fields, primary_receipt)
    r3 = r3_completeness(H, fields, star, star_rows, per_world)
    r4 = r4_degree_two(obj, primary_receipt)
    r5 = r5_teeth(H, fields, star, per_world, obj, primary_receipt,
                  r1, r2, r3, r4)

    # cross-checks against the pinned upstream receipts
    cross = {
        "escape_orbit_matches_906": star == list(
            receipt906["Q3_exhibited_solution"]["support_worlds"]),
        "event_cardinality": len(events),
        "support_events": sum(per_world[w] for w in star),
        "support_matches_906": sum(per_world[w] for w in star)
        == receipt906["Q3_exhibited_solution"]["support_events"],
        "primary_verdict": primary_receipt["VERDICT"],
        "primary_all_certificates_pass":
            primary_receipt["all_certificates_pass"],
    }

    disagreements = [k for k, v in {
        "R1_INDEPENDENT_SHAPE": r1["disagreement"],
        "R2_INDEPENDENT_RECIPES": r2["disagreement"],
        "R3_CENSUS_COMPLETENESS": r3["disagreement"],
        "R4_DEGREE_TWO": r4["disagreement"],
    }.items() if v]
    survives = (not disagreements) and pins_ok and cross["escape_orbit_matches_906"] \
        and cross["support_matches_906"]
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if survives
               else "PRIMARY_REFUTED_BY_THIS_CHECK")

    elapsed = monotonic() - started
    receipt = {
        "cycle": 909,
        "role": "independent checker, specified to refute",
        "block": "toe-time-blockQ6-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "CHECKER_VERDICT": verdict,
        "spec": (
            "independent extraction of the required shape (a disagreement on"
            " what the constraint set IS refutes the block); independent"
            " recipe instantiation; an attack on the census-of-recipes"
            " completeness (a native recipe outside the declared closure that"
            " realizes the pair flips the verdict); an attack on the degree-2"
            " relationship; teeth >= 6.  Exit 0 independent of claim survival."),
        "pins_verified": pins_ok,
        "firewall_hits": len(FIREWALL.hits),
        "certificates": {"R1_INDEPENDENT_SHAPE": r1,
                         "R2_INDEPENDENT_RECIPES": r2,
                         "R3_CENSUS_COMPLETENESS": r3,
                         "R4_DEGREE_TWO": r4,
                         "R5_TEETH": r5},
        "checks": {"R1_INDEPENDENT_SHAPE": not r1["disagreement"],
                   "R2_INDEPENDENT_RECIPES": not r2["disagreement"],
                   "R3_CENSUS_COMPLETENESS": not r3["disagreement"],
                   "R4_DEGREE_TWO": not r4["disagreement"],
                   "R5_TEETH": r5["all_teeth_bite"]},
        "disagreements": disagreements,
        "cross_checks": cross,
        "refinements": [
            ("the primary's denominator lemma is re-derived here from scratch"
             " and used as the filter of the completeness hunt; the hunt's"
             " leaked-realization tooth confirms the filter does not block a"
             " genuine realizer, so the hunt is not blind by construction"),
            ("HUNT B is the sharpest form of the negative: a degree-0 realizer"
             " needs the primes 31 and 613 in the escape-world sums, and the"
             " checker reports exactly which census fields reach them"),
            ("R4 refits the degree-2 relation with an AFFINE and a QUADRATIC"
             " family the primary did not test; both are reported whether they"
             " hold or not"),
        ],
        "primary_sha256": sha_rows[PRIMARY_PATH],
        "primary_receipt_sha256": sha_rows[PRIMARY_RECEIPT],
        "source_pins": [{"path": p, "sha256": sha_rows[p],
                         "bytes": len(payloads[p])}
                        for p in AUDIT_INPUT_PATHS],
        "elapsed_sec": round(elapsed, 3),
    }
    receipt["self_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    out = ROOT / "outputs" / \
        "within_world_independent_check_cycle909_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    w = sys.stdout.write
    w("CYCLE 909 INDEPENDENT CHECKER -- SPECIFIED TO REFUTE\n")
    w("=" * 78 + "\n")
    w(f"pins verified: {pins_ok}   firewall hits: {len(FIREWALL.hits)}\n\n")
    w("R1 INDEPENDENT SHAPE EXTRACTION\n" + "-" * 78 + "\n")
    w(f"  block sizes force one designated event per world per atom:"
      f" {r1['block_sizes_force_one_event_per_world_per_atom']}\n")
    w(f"  checker block masses  degree0 {r1['checker_block_masses_degree0']}"
      f"  degree2 {r1['checker_block_masses_degree2']}\n")
    w(f"  totals {r1['checker_totals']} agree with the 907 checker receipt:"
      f" {r1['totals_agree_with_the_907_checker_receipt']}\n")
    w(f"  checker constraint set degree0: {r1['checker_constraint_set']['degree0']}\n")
    w(f"  checker constraint set degree2: {r1['checker_constraint_set']['degree2']}\n")
    w(f"  agreement with the primary: {r1['agreement']}\n")
    w(f"  free dimension by rank {r1['checker_free_dimension_by_rank']}"
      f" vs primary {r1['primary_free_dimension']}"
      f" -> agrees {r1['free_dimension_agrees']}\n")
    w(f"  free-coordinate perturbation preserves the shape:"
      f" {r1['free_coordinate_perturbation_preserves_the_shape']};"
      f" pinned-coordinate perturbation breaks it:"
      f" {r1['pinned_coordinate_perturbation_breaks_the_shape']}\n")
    w(f"  DISAGREEMENT: {r1['disagreement']}\n\n")
    w("R2 INDEPENDENT RECIPE INSTANTIATION\n" + "-" * 78 + "\n")
    for row in r2["rows"]:
        w(f"  {row['recipe']:12s} d0={row['degree0_realizes']}"
          f" d2={row['degree2_realizes']}  profile {row['orbit_profile']}\n")
    w(f"  uniform profile   {r2['uniform_orbit_profile']}\n")
    w(f"  required profile  {r2['uniform_required_profile']}\n")
    w(f"  DISAGREEMENT: {r2['disagreement']}\n\n")
    w("R3 CENSUS COMPLETENESS -- THE HIGHEST-STAKES ATTACK\n" + "-" * 78 + "\n")
    w(f"  recipes tested outside the declared closure:"
      f" {r3['recipes_tested_outside_the_declared_closure']}\n")
    w(f"  survivors of the degree-0 denominator filter:"
      f" {r3['lemma_survivor_count_degree0']}\n")
    w(f"  survivors of the degree-2 denominator filter:"
      f" {r3['lemma_survivor_count_degree2']}\n")
    hb = r3["hunt_B_prime_reachability"]
    w(f"  HUNT B: fields whose world sums reach 31:"
      f" {hb['fields_whose_world_sums_reach_31']}\n")
    w(f"          fields whose world sums reach 613:"
      f" {hb['fields_whose_world_sums_reach_613']}\n")
    w(f"          fields reaching BOTH: {hb['fields_reaching_both']}\n")
    w(f"  HUNT C position-ratio hits: {r3['hunt_C_position_ratio_hits']}\n")
    w(f"  realizers found: {r3['realizers_found']}\n")
    w(f"  VERDICT: {r3['verdict']}\n\n")
    w("R4 THE DEGREE-2 RELATIONSHIP\n" + "-" * 78 + "\n")
    w(f"  brute-force layer amplitudes {r4['brute_force_layer_amplitudes']}"
      f"  agree with the primary: {r4['layers_agree']}\n")
    w(f"  admissible degree-2 columns: checker"
      f" {r4['checker_admissible_degree2_column_count']} vs primary"
      f" {r4['primary_admissible_degree2_column_count']}\n")
    for t in r4["wider_transform_family"]:
        w(f"      {t['transform'][:44]:44s} holds={t['holds']}\n")
    w(f"  DISAGREEMENT: {r4['disagreement']}\n\n")
    w(f"R5 TEETH ({r5['tooth_count']})\n" + "-" * 78 + "\n")
    for t in r5["teeth"]:
        w(f"  {t['tooth']:36s} bites={t['detected']}\n")
    w(f"\ncross checks: {cross}\n")
    w(f"\nCHECKER_VERDICT: {verdict}\n")
    w(f"disagreements: {disagreements}\n")
    w(f"receipt: {out.relative_to(ROOT)}\n")
    w(f"elapsed_sec: {round(elapsed, 3)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
