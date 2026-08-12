"""Cycle 719 -- finite single-slot level sets and center-reflection orbits.

Class-A finite check script (stdlib + numpy only).  It runs on the landed Cycle-696
open-coframe endpoint compiler, taking the identity-frame static assembly Q and its
inverse, and measures, from that assembly alone:

Gate groups cover the faithful 24-frame action and its right-coset fibres; the
numerical near-stabilizer and uniform within-fibre Rayleigh bound; finite seeded
probes and a broken-operator control; the center reflection and 12-element numerical
near-symmetry census; the complete single-slot orbit/level-set census at L={3,4};
transitivity agreement; and a disjoint proper-sextet versus reflection-required
merged-pair census.  Exact every-source implications are conditional on exact
operator invariance; the compiled matrices carry numerical residuals.

No value is read from a pinned table: every number printed here is recomputed from the
compiler chain in this run.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 300

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c719", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
DIRS = c696.regge.DIRS15
CLASS_OF = {tuple(int(abs(int(t))) for t in DIRS[c][:3]): c for c in c696.SPATIAL_CLASSES}
WRAP = False
L_LIST = (3, 4)
DIAGONALS = ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))
TOL_LEVEL = 1e-8
TOL_STABILIZER = 1e-9
SEP_OPERATOR = 1.0
RECEIPT_NAME = ("physical_level_set_orbit_law_improper_center_identity_cycle719"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: list[dict] = []
NOTES: list[str] = []


def fmt(x) -> str:
    return "{:.6e}".format(float(x))


def check(gate: str, ok: bool, detail: str) -> None:
    global N_PASS, N_FAIL
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES.append({"detail": detail, "gate": gate, "ok": bool(ok)})
    print("  [{}] {} {}".format("PASS" if ok else "FAIL", gate, detail))


def dkey(v) -> tuple:
    t = tuple(int(x) for x in v)
    return t if t[0] > 0 else tuple(-x for x in t)


DID = {dkey(d): j for j, d in enumerate(DIAGONALS)}
KEYED = {tuple(f.ravel().tolist()): i for i, f in enumerate(FRAMES)}
MUL = np.array([[KEYED[tuple((FRAMES[a] @ FRAMES[b]).ravel().tolist())]
                 for b in range(24)] for a in range(24)], dtype=np.int64)
SEXTET = tuple(sorted(g for g in range(24)
                      if dkey(FRAMES[g] @ np.asarray(DIAGONALS[0], dtype=np.int64))
                      == DIAGONALS[0]))
DELTA = [DID[dkey(FRAMES[g].T @ np.asarray(DIAGONALS[0], dtype=np.int64))] for g in range(24)]
FIB = {j: tuple(sorted(g for g in range(24) if DELTA[g] == j)) for j in range(4)}
# action of a frame on the four body diagonals
ACT = [[DID[dkey(FRAMES[h] @ np.asarray(DIAGONALS[j], dtype=np.int64))] for j in range(4)]
       for h in range(24)]


def relabel(L: int, g: int) -> np.ndarray:
    idx = c696.static_variable_index(L, WRAP)
    smap = c696.frame_site_map(L, FRAMES[g])
    m = np.zeros(len(idx), dtype=np.int64)
    for (c, x), i in idx.items():
        w = FRAMES[g] @ np.asarray(DIRS[c][:3], dtype=np.int64)
        site = np.asarray(smap[x], dtype=np.int64) + np.minimum(w, 0)
        m[i] = idx[(CLASS_OF[tuple(int(abs(int(t))) for t in w)], tuple(int(t) for t in site))]
    return m


def center_reflection(L: int) -> np.ndarray:
    """Point reflection of the open box through its center, as a slot relabelling."""
    idx = c696.static_variable_index(L, WRAP)
    m = np.zeros(len(idx), dtype=np.int64)
    for (c, x), i in idx.items():
        w = [abs(int(t)) for t in DIRS[c][:3]]
        m[i] = idx[(c, tuple((L - 1) - int(x[a]) - w[a] for a in range(3)))]
    return m


def axis_face_swaps(L: int) -> list:
    """The eight independent per-axis face swaps -- used as a rejector, not a symmetry."""
    idx = c696.static_variable_index(L, WRAP)
    out = []
    for bits in range(8):
        m = np.zeros(len(idx), dtype=np.int64)
        good = True
        for (c, x), i in idx.items():
            w = [abs(int(t)) for t in DIRS[c][:3]]
            y = tuple(((L - 1) - int(x[a]) - w[a]) if (bits >> a) & 1 else int(x[a])
                      for a in range(3))
            if (c, y) not in idx:
                good = False
                break
            m[i] = idx[(c, y)]
        if good:
            out.append(m)
    return out


def orbit_partition(n: int, gens) -> dict:
    par = list(range(n))

    def find(a: int) -> int:
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for m in gens:
        for i in range(n):
            a, b = find(i), find(int(m[i]))
            if a != b:
                par[a] = b
    orb = defaultdict(list)
    for i in range(n):
        orb[find(i)].append(i)
    return orb


def diag_transitive(H) -> bool:
    seen = {0}
    for _ in range(4):
        seen |= {ACT[h][j] for h in H for j in seen}
    return len(seen) == 4


def run_L(L: int) -> dict:
    Q = c696.assemble_static_hessian(L, WRAP)["Q"]
    n = Q.shape[0]
    d = np.diag(np.linalg.inv(Q)).copy()
    perms = [relabel(L, g) for g in range(24)]
    sig = center_reflection(L)
    rec = {"n": n}
    print("-- L={} n={} --".format(L, n))

    # The relabelling index map is a faithful homomorphism.
    hom = max(int(np.abs(perms[MUL[a][b]] - perms[a][perms[b]]).max())
              for a in range(24) for b in range(24))
    anti = max(int(np.abs(perms[MUL[a][b]] - perms[b][perms[a]]).max())
               for a in range(24) for b in range(24))
    rec["hom_mismatch"], rec["antihom_mismatch"] = hom, anti
    faithful = len({tuple(int(x) for x in p) for p in perms}) == 24
    check("frame_action_L{}".format(L), hom == 0 and anti > 0 and faithful,
          "index map homomorphism mismatch {} anti-homomorphism mismatch {}".format(hom, anti))

    # The body-diagonal fibres are exactly the four right cosets of the sextet.
    sizes = sorted(len(FIB[j]) for j in range(4))
    sset = frozenset(SEXTET)
    closed = frozenset(int(MUL[a][b]) for a in sset for b in sset) == sset
    right_cosets = {frozenset(int(MUL[h][a]) for h in sset) for a in range(24)}
    fibres = set(frozenset(FIB[j]) for j in range(4))
    check("body_diagonal_right_cosets_L{}".format(L),
          len(SEXTET) == 6 and sizes == [6, 6, 6, 6] and closed
          and fibres == right_cosets,
          "sextet {} closed {}, four fibre sizes {}, fibres equal right cosets {}"
          .format(list(SEXTET), closed, sizes, fibres == right_cosets))

    # Numerical near-stabilizer of the compiled assembly among the 24 frames.
    devs = [float(np.abs(Q[np.ix_(perms[g], perms[g])] - Q).max()) for g in range(24)]
    din = max(devs[g] for g in SEXTET)
    dout = min(devs[g] for g in range(24) if g not in SEXTET)
    stab = tuple(sorted(g for g in range(24) if devs[g] <= TOL_STABILIZER))
    rec["stab_in_dev"], rec["stab_out_dev"] = fmt(din), fmt(dout)
    check("numerical_near_stabilizer_L{}".format(L),
          stab == SEXTET and din <= TOL_STABILIZER and dout >= SEP_OPERATOR,
          "near-stabilizer {} sextet dev {} outside dev {}".format(
              "matches the sextet" if stab == SEXTET else list(stab), fmt(din), fmt(dout)))

    # Uniform numerical within-fibre Rayleigh bound, plus slot and seeded probes.
    meas = 0
    for i in range(n):
        vals = np.array([d[perms[g][i]] for g in range(24)])
        if all(float(np.abs(vals[list(FIB[j])] - vals[FIB[j][0]]).max()) <= TOL_LEVEL
               for j in range(4)):
            meas += 1
    rng = np.random.default_rng(7190 + L)
    spread, gap = 0.0, float("inf")
    Qi = np.linalg.inv(Q)
    rayleigh_operators = [Qi[np.ix_(perms[g], perms[g])] for g in range(24)]
    uniform = max(float(np.linalg.norm(
        rayleigh_operators[g] - rayleigh_operators[FIB[j][0]], ord=2))
        for j in range(4) for g in FIB[j])
    for _ in range(8):
        u = rng.standard_normal(n)
        v = []
        for g in range(24):
            t = np.empty(n)
            t[perms[g]] = u
            v.append(float(t @ Qi @ t) / float(u @ u))
        v = np.array(v)
        for j in range(4):
            spread = max(spread, float(np.abs(v[list(FIB[j])] - v[FIB[j][0]]).max()))
        gap = min(gap, min(abs(v[FIB[a][0]] - v[FIB[b][0]])
                           for a in range(4) for b in range(a + 1, 4)))
    rec["slots_measurable"], rec["uniform_rayleigh_bound"] = meas, fmt(uniform)
    rec["dense_spread"], rec["dense_gap"] = fmt(spread), fmt(gap)
    check("finite_body_diagonal_measurability_L{}".format(L),
          meas == n and uniform <= TOL_LEVEL and spread <= TOL_LEVEL and gap >= 1e-4,
          "slots {} of {}, uniform normalized-source bound {}, seeded spread {}, "
          "seeded label gap {}".format(meas, n, fmt(uniform), fmt(spread), fmt(gap)))

    # G5 -- sextet-breaking control: the same measurement must fail on a broken assembly
    R = Q.copy()
    R[0, 0] += 1.0
    Ri = np.linalg.inv(R)
    bad = 0.0
    for _ in range(4):
        u = rng.standard_normal(n)
        v = []
        for g in range(24):
            t = np.empty(n)
            t[perms[g]] = u
            v.append(float(t @ Ri @ t) / float(u @ u))
        v = np.array(v)
        for j in range(4):
            bad = max(bad, float(np.abs(v[list(FIB[j])] - v[FIB[j][0]]).max()))
    rec["control_spread"] = fmt(bad)
    check("broken_operator_control_L{}".format(L), bad >= 1e-4,
          "sextet-breaking control destroys delta-measurability, spread {}".format(fmt(bad)))

    # Center reflection as a finite numerical computational identity.
    is_perm = sorted(sig.tolist()) == list(range(n))
    invol = int(np.abs(sig[sig] - np.arange(n)).max()) == 0
    devs_sig = float(np.abs(Q[np.ix_(sig, sig)] - Q).max())
    dev_diag = float(np.abs(d[sig] - d).max())
    isframe = any(int(np.abs(sig - perms[g]).max()) == 0 for g in range(24))
    comm = max(int(np.abs(sig[perms[g]] - perms[g][sig]).max()) for g in range(24))
    rec["reflection_dev"], rec["reflection_diag_dev"] = fmt(devs_sig), fmt(dev_diag)
    check("center_reflection_L{}".format(L),
          is_perm and invol and devs_sig <= TOL_STABILIZER and dev_diag <= TOL_LEVEL
          and not isframe and comm == 0,
          "center reflection involution {} assembly dev {} diag dev {} a frame {} central {}"
          .format(invol, fmt(devs_sig), fmt(dev_diag), isframe, comm == 0))

    # Numerical near-symmetry census among 48 distinct relabellings.
    proper = sum(1 for g in range(24) if devs[g] <= TOL_STABILIZER)
    improper = 0
    candidates = [tuple(int(x) for x in perms[g]) for g in range(24)]
    candidates += [tuple(int(x) for x in sig[perms[g]]) for g in range(24)]
    for g in range(24):
        m2 = sig[perms[g]]
        if float(np.abs(Q[np.ix_(m2, m2)] - Q).max()) <= TOL_STABILIZER:
            improper += 1
    rec["sym_proper"], rec["sym_improper"] = proper, improper
    check("numerical_near_symmetry_census_L{}".format(L),
          len(set(candidates)) == 48 and proper == 6 and improper == 6,
          "48 distinct candidates, near-symmetry count {} = {} proper + {} improper"
          .format(
              proper + improper, proper, improper))

    # Complete finite single-slot level-set/orbit census.
    orb = orbit_partition(n, [perms[s] for s in SEXTET] + [sig])
    const = max(float(np.abs(d[v] - d[v[0]]).max()) for v in orb.values())
    reps = [float(d[v[0]]) for v in orb.values()]
    sep = min(abs(reps[a] - reps[b]) for a in range(len(reps))
              for b in range(a + 1, len(reps)))
    hist = dict(sorted(Counter(len(v) for v in orb.values()).items()))
    rec["orbits"], rec["orbit_const"], rec["orbit_sep"] = len(orb), fmt(const), fmt(sep)
    rec["orbit_sizes"] = {str(k): v for k, v in hist.items()}
    check("slot_level_set_orbit_census_L{}".format(L),
          const <= TOL_LEVEL and sep > TOL_LEVEL,
          "orbits {} constant to {} separated by {} sizes {}".format(
              len(orb), fmt(const), fmt(sep), hist))

    # Rejector: independent per-axis face-flip combinations over-merge.
    swaps = axis_face_swaps(L)
    orb8 = orbit_partition(n, swaps + [perms[s] for s in SEXTET])
    dev8 = max(float(np.abs(d[v] - d[v[0]]).max()) for v in orb8.values())
    rec["swap_maps"], rec["swap_orbits"], rec["swap_dev"] = len(swaps), len(orb8), fmt(dev8)
    check("axis_face_flip_rejector_L{}".format(L),
          len(swaps) == 8 and len(orb8) < len(orb) and dev8 >= 1e-3,
          "{} per-axis face swaps over-merge to {} orbits, value dev {}".format(
              len(swaps), len(orb8), fmt(dev8)))

    # Finite slot-by-slot blindness/transitivity agreement.
    blind = trans = both = 0
    for i in range(n):
        vd = [float(d[perms[FIB[j][0]][i]]) for j in range(4)]
        b = max(abs(vd[j] - vd[0]) for j in range(4)) <= TOL_LEVEL
        H = [h for h in range(24) if perms[h][i] == i]
        t = diag_transitive(H)
        blind += int(b)
        trans += int(t)
        both += int(b and t)
    rec["blind"], rec["transitive"] = blind, trans
    check("slot_blindness_transitivity_census_L{}".format(L),
          blind == trans == both,
          "blind slots {} stabilizer-transitive {} agreeing {}".format(blind, trans, both))

    # Complete disjoint group census of every merged single-slot label pair.
    tally = Counter()
    source_stabilizer_links = 0
    for i in range(n):
        rp = [perms[FIB[j][0]][i] for j in range(4)]
        H = [h for h in range(24) if perms[h][i] == i]
        for a in range(4):
            for b in range(a + 1, 4):
                if abs(d[rp[a]] - d[rp[b]]) > TOL_LEVEL:
                    continue
                source_stabilizer_links += int(
                    any(perms[h][rp[a]] == rp[b] for h in H)
                )
                if any(perms[g][rp[a]] == rp[b] for g in SEXTET):
                    tally["proper_sextet"] += 1
                elif any(sig[perms[g][rp[a]]] == rp[b] for g in SEXTET):
                    tally["reflection_required"] += 1
                else:
                    tally["residue"] += 1
    tot = sum(tally.values())
    rec["merged_total"] = tot
    rec["merged"] = {k: tally[k] for k in (
        "proper_sextet", "reflection_required", "residue"
    )}
    rec["source_stabilizer_links"] = source_stabilizer_links
    check("merged_pair_group_census_L{}".format(L),
          tally["residue"] == 0 and tot > 0
          and tally["reflection_required"] > tally["proper_sextet"],
          "merged pairs {} = {} proper-sextet + {} reflection-required, "
          "residue {}; overlapping source-stabilizer links {}".format(
              tot, tally["proper_sextet"], tally["reflection_required"],
              tally["residue"], source_stabilizer_links))
    return rec


def main() -> int:
    print("Cycle 719 finite single-slot Rayleigh level-set and reflection-orbit census")
    print("24 proper rotations, body-diagonal sextet {}, four cosets".format(list(SEXTET)))
    per_L = {}
    for L in L_LIST:
        per_L[str(L)] = run_L(L)
    NOTES.append("center reflection fixes each body diagonal as an unsigned line")
    receipt = {"box_sizes": list(L_LIST),
               "fail": N_FAIL,
               "gates": GATES,
               "notes": NOTES,
               "pass": N_PASS,
               "per_box": per_L,
               "runner": Path(__file__).name,
               "sextet": list(SEXTET),
               "tolerances": {"level": fmt(TOL_LEVEL),
                              "stabilizer": fmt(TOL_STABILIZER)}}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
