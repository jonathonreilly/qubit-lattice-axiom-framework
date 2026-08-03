"""Cycle 719 -- level sets of the k-endpoint value functional are orbits of an
order-12 assembly symmetry whose improper half carries no frame label.

Class-A finite check script (stdlib + numpy only).  It runs on the landed Cycle-696
open-coframe endpoint compiler, taking the identity-frame static assembly Q and its
inverse, and measures, from that assembly alone:

  G1  the relabelling index map is a homomorphism of the 24 proper rotations, and is
      NOT the anti-homomorphism the matrix convention would suggest;
  G2  the body-diagonal stabilizer sextet and the four right cosets it cuts;
  G3  the exact stabilizer of the assembly among the 24 frames IS that sextet, with a
      wide separation from every frame outside it;
  G4  delta-measurability of the value functional for EVERY slot source and for drawn
      dense sources, with a resolved gap between distinct body-diagonal labels;
  G5  a sextet-breaking control on the assembly, which destroys G4;
  G6  the box-center point reflection as an improper computational identity: an
      involution, an exact symmetry of the assembly, central in the relabelling group,
      and not equal to any of the 24 frames;
  G7  the resulting symmetry order 12 = 6 proper + 6 improper;
  G8  the orbits of that order-12 group carry the diagonal value function exactly:
      constant on orbits AND separating distinct orbits;
  G9  a rejector showing the improper half is the single center reflection and not the
      larger group of independent per-axis face swaps;
  G10 full frame-blindness of a slot source is equivalent to its frame stabilizer being
      transitive on the four body diagonals;
  G11 a complete classification of every merged value pair as stabilizer-linked,
      sextet-linked, or center-reflection-linked, with no residue.

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
TOL = 1e-8
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

    # G1 -- the relabelling index map is a homomorphism, not an anti-homomorphism
    hom = max(int(np.abs(perms[MUL[a][b]] - perms[a][perms[b]]).max())
              for a in range(24) for b in range(24))
    anti = max(int(np.abs(perms[MUL[a][b]] - perms[b][perms[a]]).max())
               for a in range(24) for b in range(24))
    rec["hom_mismatch"], rec["antihom_mismatch"] = hom, anti
    check("G1", hom == 0 and anti > 0,
          "index map homomorphism mismatch {} anti-homomorphism mismatch {}".format(hom, anti))

    # G2 -- the body-diagonal stabilizer sextet and its four right cosets
    sizes = sorted(len(FIB[j]) for j in range(4))
    check("G2", len(SEXTET) == 6 and sizes == [6, 6, 6, 6],
          "sextet {} cuts four cosets of sizes {}".format(list(SEXTET), sizes))

    # G3 -- the exact stabilizer of the assembly among the 24 frames
    devs = [float(np.abs(Q[np.ix_(perms[g], perms[g])] - Q).max()) for g in range(24)]
    din = max(devs[g] for g in SEXTET)
    dout = min(devs[g] for g in range(24) if g not in SEXTET)
    stab = tuple(sorted(g for g in range(24) if devs[g] <= 1e-9))
    rec["stab_in_dev"], rec["stab_out_dev"] = fmt(din), fmt(dout)
    check("G3", stab == SEXTET and din <= 1e-9 and dout >= 1.0,
          "assembly stabilizer {} sextet dev {} outside dev {}".format(
              "IS the sextet" if stab == SEXTET else list(stab), fmt(din), fmt(dout)))

    # G4 -- delta-measurability of the value functional, slot sources and dense sources
    meas = 0
    for i in range(n):
        vals = np.array([d[perms[g][i]] for g in range(24)])
        if all(float(np.abs(vals[list(FIB[j])] - vals[FIB[j][0]]).max()) <= TOL
               for j in range(4)):
            meas += 1
    rng = np.random.default_rng(7190 + L)
    spread, gap = 0.0, float("inf")
    Qi = np.linalg.inv(Q)
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
    rec["slots_measurable"] = meas
    rec["dense_spread"], rec["dense_gap"] = fmt(spread), fmt(gap)
    check("G4", meas == n and spread <= TOL and gap >= 1e-4,
          "delta-measurable slots {} of {} dense spread {} label gap {}".format(
              meas, n, fmt(spread), fmt(gap)))

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
    check("G5", bad >= 1e-4,
          "sextet-breaking control destroys delta-measurability, spread {}".format(fmt(bad)))

    # G6 -- the center reflection as an improper computational identity
    is_perm = sorted(sig.tolist()) == list(range(n))
    invol = int(np.abs(sig[sig] - np.arange(n)).max()) == 0
    devs_sig = float(np.abs(Q[np.ix_(sig, sig)] - Q).max())
    dev_diag = float(np.abs(d[sig] - d).max())
    isframe = any(int(np.abs(sig - perms[g]).max()) == 0 for g in range(24))
    comm = max(int(np.abs(sig[perms[g]] - perms[g][sig]).max()) for g in range(24))
    rec["reflection_dev"], rec["reflection_diag_dev"] = fmt(devs_sig), fmt(dev_diag)
    check("G6", is_perm and invol and devs_sig <= 1e-9 and dev_diag <= 1e-8
          and not isframe and comm == 0,
          "center reflection involution {} assembly dev {} diag dev {} a frame {} central {}"
          .format(invol, fmt(devs_sig), fmt(dev_diag), isframe, comm == 0))

    # G7 -- the symmetry order among the 24 frames and their center-reflected partners
    proper = sum(1 for g in range(24) if devs[g] <= 1e-9)
    improper = 0
    for g in range(24):
        m2 = sig[perms[g]]
        if float(np.abs(Q[np.ix_(m2, m2)] - Q).max()) <= 1e-9:
            improper += 1
    rec["sym_proper"], rec["sym_improper"] = proper, improper
    check("G7", proper == 6 and improper == 6 and proper + improper == 12,
          "assembly symmetry order {} = {} proper + {} improper".format(
              proper + improper, proper, improper))

    # G8 -- the order-12 orbits carry the diagonal value function exactly
    orb = orbit_partition(n, [perms[s] for s in SEXTET] + [sig])
    const = max(float(np.abs(d[v] - d[v[0]]).max()) for v in orb.values())
    reps = [float(d[v[0]]) for v in orb.values()]
    sep = min(abs(reps[a] - reps[b]) for a in range(len(reps))
              for b in range(a + 1, len(reps)))
    hist = dict(sorted(Counter(len(v) for v in orb.values()).items()))
    rec["orbits"], rec["orbit_const"], rec["orbit_sep"] = len(orb), fmt(const), fmt(sep)
    rec["orbit_sizes"] = {str(k): v for k, v in hist.items()}
    check("G8", const <= TOL and sep > TOL,
          "orbits {} constant to {} separated by {} sizes {}".format(
              len(orb), fmt(const), fmt(sep), hist))

    # G9 -- rejector: independent per-axis face swaps over-merge
    swaps = axis_face_swaps(L)
    orb8 = orbit_partition(n, swaps + [perms[s] for s in SEXTET])
    dev8 = max(float(np.abs(d[v] - d[v[0]]).max()) for v in orb8.values())
    rec["swap_maps"], rec["swap_orbits"], rec["swap_dev"] = len(swaps), len(orb8), fmt(dev8)
    check("G9", len(swaps) == 8 and len(orb8) < len(orb) and dev8 >= 1e-3,
          "{} per-axis face swaps over-merge to {} orbits, value dev {}".format(
              len(swaps), len(orb8), fmt(dev8)))

    # G10 -- full frame-blindness is transitivity of the frame stabilizer
    blind = trans = both = 0
    for i in range(n):
        vd = [float(d[perms[FIB[j][0]][i]]) for j in range(4)]
        b = max(abs(vd[j] - vd[0]) for j in range(4)) <= TOL
        H = [h for h in range(24) if perms[h][i] == i]
        t = diag_transitive(H)
        blind += int(b)
        trans += int(t)
        both += int(b and t)
    rec["blind"], rec["transitive"] = blind, trans
    check("G10", blind == trans == both,
          "blind slots {} stabilizer-transitive {} agreeing {}".format(blind, trans, both))

    # G11 -- complete classification of every merged value pair
    tally = Counter()
    for i in range(n):
        rp = [perms[FIB[j][0]][i] for j in range(4)]
        H = [h for h in range(24) if perms[h][i] == i]
        for a in range(4):
            for b in range(a + 1, 4):
                if abs(d[rp[a]] - d[rp[b]]) > TOL:
                    continue
                if any(perms[h][rp[a]] == rp[b] for h in H):
                    tally["stabilizer"] += 1
                elif any(perms[g][rp[a]] == rp[b] for g in SEXTET):
                    tally["sextet"] += 1
                elif any(sig[perms[g][rp[a]]] == rp[b] for g in range(24)):
                    tally["reflection"] += 1
                else:
                    tally["residue"] += 1
    tot = sum(tally.values())
    rec["merged_total"] = tot
    rec["merged"] = {k: tally[k] for k in ("stabilizer", "sextet", "reflection", "residue")}
    check("G11", tally["residue"] == 0 and tot > 0,
          "merged pairs {} = {} stabilizer + {} sextet + {} reflection, residue {}".format(
              tot, tally["stabilizer"], tally["sextet"], tally["reflection"],
              tally["residue"]))
    return rec


def main() -> int:
    print("c719 level sets of the k-endpoint value functional as symmetry orbits")
    print("24 proper rotations, body-diagonal sextet {}, four cosets".format(list(SEXTET)))
    per_L = {}
    for L in L_LIST:
        per_L[str(L)] = run_L(L)
    NOTES.append("the improper half of the assembly symmetry carries no body-diagonal label")
    receipt = {"box_sizes": list(L_LIST),
               "fail": N_FAIL,
               "gates": GATES,
               "notes": NOTES,
               "pass": N_PASS,
               "per_box": per_L,
               "runner": Path(__file__).name,
               "sextet": list(SEXTET)}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
