"""Cycle 720: on the Cycle-696 open-box static assembly, the frame label of a
sub-domain response is fixed by the AMBIENT assembly's stabilizer, while the level
sets of that response are fixed by the SUB-DOMAIN's own symmetry.

The two are independent. Restricting the response to a sub-domain that is not
centre-symmetric halves the sub-domain symmetry group and does restore the finer
level sets, but it never removes that group's improper half and never refines the
frame label past four classes.

Class-A finite-dimensional check. Every printed float is produced here. No coupling
value, sign, or scale is selected or derived. The signed permutations that are not
proper rotations enter as computational identities on the assembly, never as
framework symmetries.
"""

from __future__ import annotations

import importlib.util
import json
from collections import defaultdict
from itertools import permutations
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
_MODULE = (ROOT / "scripts"
           / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py")
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c720", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
DIRS = c696.regge.DIRS15
CLASS_OF = {tuple(int(abs(int(t))) for t in DIRS[c][:3]): c for c in c696.SPATIAL_CLASSES}
WRAP = False
ONE3 = np.array([1, 1, 1], dtype=np.int64)
NEG_EYE = -np.eye(3, dtype=np.int64)

SEXTET = (1, 4, 9, 15, 18, 23)
L_LIST = (3, 4, 5)
CORNER_K = (2, 3, 4)
SLAB_CUT = 1

BOUND_AMBIENT = 1e-9
BOUND_CROSS = 1.0
BOUND_RATIO = 1e8
BOUND_SEP = 1e3
TOL_LEVEL = 1e-7
TOL_SYM = 1e-9
N_CLASSES = 4

WORST = {"const": 0.0, "gap": float("inf"), "sep": float("inf")}

RECEIPT_NAME = ("physical_ambient_domain_symmetry_split_cycle720"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.6e}".format(float(x))


def gate(name: str, ok: bool, detail: str) -> None:
    global N_PASS, N_FAIL
    GATES[name] = {"detail": detail, "ok": bool(ok)}
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
        print("FAIL {} :: {}".format(name, detail))


# ---------------------------------------------------------------- group set-up
KEYED = {tuple(FRAMES[g].ravel().tolist()): g for g in range(24)}
MUL = np.array([[KEYED[tuple((FRAMES[a] @ FRAMES[b]).ravel().tolist())] for b in range(24)]
                for a in range(24)], dtype=np.int64)
IDENT = [g for g in range(24)
         if int(np.abs(FRAMES[g] - np.eye(3, dtype=np.int64)).max()) == 0][0]

PERMS = []
for _p in permutations(range(3)):
    _A = np.zeros((3, 3), dtype=np.int64)
    for _a in range(3):
        _A[_a, _p[_a]] = 1
    PERMS.append(_A)
PERM_DET = [int(round(float(np.linalg.det(A)))) for A in PERMS]
G12 = PERMS + [-A for A in PERMS]
G12_DET = [int(round(float(np.linalg.det(A)))) for A in G12]


def relabel_mat(L: int, R, idx: dict) -> np.ndarray:
    """Slot relabelling induced by a signed permutation R of the axes.

    Sites go by x -> R x + t with t the unique box-preserving shift; the stored slot
    key is an edge's low corner, so the image key picks up min(R w, 0).
    """
    R = np.asarray(R, dtype=np.int64)
    t = np.array([(L - 1) if R[a].min() < 0 else 0 for a in range(3)], dtype=np.int64)
    m = np.zeros(len(idx), dtype=np.int64)
    for (c, x), i in idx.items():
        w = R @ np.asarray(DIRS[c][:3], dtype=np.int64)
        y = R @ np.asarray(x, dtype=np.int64) + t + np.minimum(w, 0)
        m[i] = idx[(CLASS_OF[tuple(int(abs(int(v))) for v in w)], tuple(int(v) for v in y))]
    return m


def site_shift(L: int, R) -> np.ndarray:
    R = np.asarray(R, dtype=np.int64)
    return np.array([(L - 1) if R[a].min() < 0 else 0 for a in range(3)], dtype=np.int64)


def orbits_under(maps, D: np.ndarray) -> dict:
    """Union-find orbits of the slot set D under the given slot relabellings."""
    nd = len(D)
    pos = {int(v): k for k, v in enumerate(D)}
    par = list(range(nd))

    def find(a: int) -> int:
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for m in maps:
        for k, v in enumerate(D):
            a, b = find(k), find(pos[int(m[int(v)])])
            if a != b:
                par[a] = b
    out = defaultdict(list)
    for k in range(nd):
        out[find(k)].append(k)
    return out


def levels_of(vals, tol: float) -> list:
    out = []
    for x in sorted(float(v) for v in vals):
        if not any(abs(x - y) <= tol for y in out):
            out.append(x)
    return out


def domain_list(L: int, inv: dict, n: int) -> list:
    tot = np.array([sum(int(t) for t in inv[i][1]) + sum(int(t) for t in DIRS[inv[i][0]][:3])
                    for i in range(n)])
    first = np.array([int(inv[i][1][0]) + int(DIRS[inv[i][0]][0]) for i in range(n)])
    out = [("full box", np.arange(n))]
    for K in CORNER_K:
        d = np.flatnonzero(tot <= K)
        if 6 <= len(d) < n:
            out.append(("corner K={}".format(K), d))
    d = np.flatnonzero(first <= SLAB_CUT)
    if 6 <= len(d) < n:
        out.append(("slab x<={}".format(SLAB_CUT), d))
    return out


# ------------------------------------------------------ A: the order-12 identity set
def section_a() -> None:
    keys = {A.tobytes() for A in G12}
    npr = sum(1 for d in G12_DET if d == 1)
    nim = sum(1 for d in G12_DET if d == -1)
    gate("A1.distinct", len(keys) == 12 and npr == 6 and nim == 6,
         "distinct {} proper {} improper {}".format(len(keys), npr, nim))

    proper = {G12[k].tobytes() for k in range(12) if G12_DET[k] == 1}
    sextet = {FRAMES[g].tobytes() for g in SEXTET}
    gate("A2.proper_half_is_sextet", proper == sextet,
         "proper half of the order-12 set equals the cycle-719 sextet")

    ok = True
    for k, A in enumerate(PERMS):
        pair = [A, -A]
        det = [PERM_DET[k], -PERM_DET[k]]
        chosen = [pair[j].tobytes() in proper for j in range(2)]
        ok = ok and chosen == [det[0] == 1, det[1] == 1] and sum(chosen) == 1
    gate("A3.sign_character_graph", ok,
         "for each axis permutation exactly one of P, -P is proper, selected by det(P)")

    closed = all((G12[a] @ G12[b]).tobytes() in keys for a in range(12) for b in range(12))
    comm = max(int(np.abs(NEG_EYE @ A - A @ NEG_EYE).max()) for A in G12)
    gate("A4.closed_and_central", closed and comm == 0,
         "closed under composition {} centre-reflection commutator {}".format(closed, comm))

    print("A order-12 set: distinct {} proper {} improper {} | proper half is the "
          "cycle-719 sextet {}".format(len(keys), npr, nim, proper == sextet))
    print("A the proper half is the graph of the sign character {} | composition-closed "
          "{} | centre reflection central {}".format(ok, closed, comm == 0))
    NOTES["order12"] = {"distinct": len(keys), "improper": nim, "proper": npr}


# -------------------------------------------------------------------- per box size
def run_L(L: int) -> None:
    idx = c696.static_variable_index(L, WRAP)
    n = len(idx)
    inv = {i: k for k, i in idx.items()}
    Q = c696.assemble_static_hessian(L, WRAP)["Q"]
    perms = [relabel_mat(L, FRAMES[g], idx) for g in range(24)]
    sigma = relabel_mat(L, NEG_EYE, idx)
    print("-- L={} n={} --".format(L, n))

    # R1a: the site part is the compiler's own frame site map, exactly.
    bad = 0
    for g in range(24):
        smap = c696.frame_site_map(L, FRAMES[g].astype(float))
        t = site_shift(L, FRAMES[g])
        for s, img in smap.items():
            y = FRAMES[g] @ np.asarray(s, dtype=np.int64) + t
            bad += int(tuple(int(v) for v in y) != tuple(int(v) for v in img))
    gate("R1a.site_map.L{}".format(L), bad == 0,
         "site images vs compiler frame_site_map mismatches {}".format(bad))

    # R1b: every relabelling is a slot bijection; R1c: index maps compose covariantly.
    bij = sum(1 for g in range(24) if len(set(perms[g].tolist())) == n)
    bij += int(len(set(sigma.tolist())) == n)
    hom = max(int(np.abs(perms[int(MUL[a, b])] - perms[a][perms[b]]).max())
              for a in range(24) for b in range(24))
    gate("R1b.bijective.L{}".format(L), bij == 25, "slot bijections {} of 25".format(bij))
    gate("R1c.homomorphism.L{}".format(L), hom == 0,
         "composition mismatch over all 576 frame pairs {}".format(hom))
    print("R1 site map vs compiler {} | slot bijections {}/25 | composition mismatch {}"
          .format(bad, bij, hom))

    # B: the ambient assembly's own symmetry tolerance, and its rejector.
    amb = max(float(np.abs(Q[np.ix_(perms[s], perms[s])] - Q).max()) for s in SEXTET)
    ref = float(np.abs(Q[np.ix_(sigma, sigma)] - Q).max())
    non = min(float(np.abs(Q[np.ix_(perms[g], perms[g])] - Q).max())
              for g in range(24) if g not in SEXTET)
    qmax = float(np.abs(Q).max())
    gate("B1.ambient.L{}".format(L), amb <= BOUND_AMBIENT and ref <= BOUND_AMBIENT,
         "sextet {} centre reflection {}".format(fmt(amb), fmt(ref)))
    gate("B2.ambient_rejector.L{}".format(L), non >= BOUND_CROSS,
         "smallest non-sextet frame deviation {}".format(fmt(non)))
    print("B ambient sextet dev {} centre-reflection dev {} | entry max {} | "
          "non-sextet floor {}".format(fmt(amb), fmt(ref), fmt(qmax), fmt(non)))
    NOTES["ambient_L{}".format(L)] = {"centre_reflection": fmt(ref), "entry_max": fmt(qmax),
                                      "non_sextet": fmt(non), "sextet": fmt(amb)}

    dfull = np.diag(np.linalg.inv(Q)).copy()
    cosets = defaultdict(list)
    for g in range(24):
        cosets[min(int(MUL[s, g]) for s in SEXTET)].append(g)
    classes = sorted(cosets.values(), key=lambda v: v[0])

    for name, D in domain_list(L, inv, n):
        run_domain(L, n, idx, Q, perms, sigma, dfull, classes, name, D)


def run_domain(L, n, idx, Q, perms, sigma, dfull, classes, name, D) -> None:
    nd = len(D)
    tag = "L{}.{}".format(L, name.replace(" ", "_").replace("<", "le").replace("=", ""))
    pos = {int(v): k for k, v in enumerate(D)}
    dset = set(D.tolist())
    QD = Q[np.ix_(D, D)]

    # C: the symmetry of the restricted assembly inside the order-12 set.
    sym_det, sym_maps, sigma_in = [], [], False
    for A, det in zip(G12, G12_DET):
        m = relabel_mat(L, A, idx)
        if set(m[D].tolist()) != dset:
            continue
        r = np.array([pos[int(m[int(v)])] for v in D])
        if float(np.abs(QD[np.ix_(r, r)] - QD).max()) <= TOL_SYM:
            sym_det.append(det)
            sym_maps.append(m)
            sigma_in = sigma_in or int(np.abs(A - NEG_EYE).max()) == 0
    npr = sum(1 for d in sym_det if d == 1)
    nim = sum(1 for d in sym_det if d == -1)
    gate("C.half_improper.{}".format(tag), npr == nim and npr > 0,
         "domain symmetry {} proper {} improper {}".format(len(sym_det), npr, nim))

    # D: level sets of the restricted response are the domain symmetry orbits.
    d0 = np.diag(np.linalg.inv(QD)).copy()
    orb = orbits_under(sym_maps, D)
    const = max(float(np.abs(d0[v] - d0[v[0]]).max()) for v in orb.values())
    lv = levels_of([d0[v[0]] for v in orb.values()], TOL_LEVEL)
    gap = min((lv[i + 1] - lv[i] for i in range(len(lv) - 1)), default=0.0)
    sep = gap / const if const > 0.0 else float("inf")
    WORST["const"] = max(WORST["const"], const)
    WORST["gap"] = min(WORST["gap"], gap)
    WORST["sep"] = min(WORST["sep"], sep)
    gate("D.levels_are_orbits.{}".format(tag),
         len(lv) == len(orb) and const < TOL_LEVEL < gap and sep >= BOUND_SEP,
         "levels {} orbits {} within-orbit {} smallest gap {}".format(
             len(lv), len(orb), fmt(const), fmt(gap)))

    # E: the frame label follows the AMBIENT stabilizer, on every domain.
    A_g = [Q[np.ix_(perms[g][D], perms[g][D])] for g in range(24)]
    within = max(float(np.abs(A_g[g] - A_g[v[0]]).max()) for v in classes for g in v)
    cross = min(float(np.abs(A_g[classes[a][0]] - A_g[classes[b][0]]).max())
                for a in range(len(classes)) for b in range(a + 1, len(classes)))
    ratio = cross / within if within > 0.0 else float("inf")
    gate("E.ambient_label.{}".format(tag),
         len(classes) == N_CLASSES and within <= BOUND_AMBIENT
         and cross >= BOUND_CROSS and ratio >= BOUND_RATIO,
         "classes {} within {} cross {}".format(len(classes), fmt(within), fmt(cross)))

    # F: the centre reflection is in the domain symmetry exactly when levels merge.
    perm_only = []
    for A in PERMS:
        m = relabel_mat(L, A, idx)
        if set(m[D].tolist()) == dset:
            perm_only.append(m)
    orb_p = orbits_under(perm_only, D)
    deficit = len(orb_p) - len(orb)
    gate("F.merge_iff_central.{}".format(tag), (deficit > 0) == sigma_in,
         "axis-permutation orbits {} domain orbits {} deficit {} centre reflection in "
         "domain symmetry {}".format(len(orb_p), len(orb), deficit, sigma_in))

    # G: on the same slot set, restriction blinds no additional slots.
    reps = [v[0] for v in classes]
    dcls = [np.diag(np.linalg.inv(A_g[g])).copy() for g in reps]
    W = np.array([[float(dcls[j][k]) for j in range(len(reps))] for k in range(nd)])
    blind_r = sum(1 for k in range(nd)
                  if max(abs(W[k, j] - W[k, 0]) for j in range(len(reps))) <= TOL_LEVEL)
    blind_a = 0
    for k in range(nd):
        i = int(D[k])
        vals = [dfull[perms[g][i]] for g in reps]
        blind_a += int(max(abs(v - vals[0]) for v in vals) <= TOL_LEVEL)
    gate("G.blindness.{}".format(tag), blind_r <= blind_a,
         "blind slots ambient {} restricted {}".format(blind_a, blind_r))

    print("  {:11s} |D|={:4d} sym {}={}+{} levels {} = orbits {} within {} gap {} | cls {} "
          "coset {} cross {} | perm orbits {} deficit {} | blind {} -> {}"
          .format(name, nd, len(sym_det), npr, nim, len(lv), len(orb), fmt(const), fmt(gap),
                  len(classes), fmt(within), fmt(cross), len(orb_p), deficit,
                  blind_a, blind_r))
    NOTES[tag] = {"blind_ambient": blind_a, "blind_restricted": blind_r,
                  "classes": len(classes), "cross": fmt(cross), "deficit": deficit,
                  "gap": fmt(gap), "improper": nim, "levels": len(lv), "orbits": len(orb),
                  "proper": npr, "size": nd, "within": fmt(within)}


# ------------------------------------------------------------------- rejectors
def rejectors() -> None:
    L = 4
    idx = c696.static_variable_index(L, WRAP)
    n = len(idx)
    inv = {i: k for k, i in idx.items()}
    Q = c696.assemble_static_hessian(L, WRAP)["Q"]
    perms = [relabel_mat(L, FRAMES[g], idx) for g in range(24)]
    tot = np.array([sum(int(t) for t in inv[i][1]) + sum(int(t) for t in DIRS[inv[i][0]][:3])
                    for i in range(n)])
    D = np.flatnonzero(tot <= 3)
    pos = {int(v): k for k, v in enumerate(D)}
    dset = set(D.tolist())

    # R3: the reversed composition convention is genuinely different.
    anti = sum(1 for a in range(24) for b in range(24)
               if int(np.abs(perms[int(MUL[a, b])] - perms[b][perms[a]]).max()) > 0)
    gate("R3.anti_composition_rejected", anti > 0,
         "frame pairs on which the reversed composition differs {} of 576".format(anti))

    # R4: a single perturbed diagonal entry destroys the domain symmetry.
    Qb = Q.copy()
    Qb[int(D[0]), int(D[0])] += 1.0
    QDb = Qb[np.ix_(D, D)]
    devs = []
    for A in G12:
        m = relabel_mat(L, A, idx)
        if set(m[D].tolist()) != dset:
            continue
        r = np.array([pos[int(m[int(v)])] for v in D])
        devs.append(float(np.abs(QDb[np.ix_(r, r)] - QDb).max()))
    surv = sum(1 for d in devs if d <= TOL_SYM)
    gate("R4.bumped_diagonal_rejected", surv < len(devs) and max(devs) >= BOUND_CROSS,
         "symmetry survivors {} of {} largest deviation {}".format(
             surv, len(devs), fmt(max(devs))))

    # R5: grouping by the other coset side does not carry the frame label.
    A_g = [Q[np.ix_(perms[g][D], perms[g][D])] for g in range(24)]
    left = defaultdict(list)
    for g in range(24):
        left[min(int(MUL[g, s]) for s in SEXTET)].append(g)
    dev_left = max(float(np.abs(A_g[g] - A_g[v[0]]).max()) for v in left.values() for g in v)
    gate("R5.left_grouping_rejected", dev_left >= 1e-3,
         "other-side grouping deviation {}".format(fmt(dev_left)))
    print("R3 reversed composition differs on {}/576 frame pairs | R4 bumped-diagonal "
          "survivors {}/{} at {} | R5 other-side grouping {}".format(
              anti, surv, len(devs), fmt(max(devs)), fmt(dev_left)))
    NOTES["rejectors"] = {"bumped_survivors": surv, "left_grouping": fmt(dev_left),
                          "reversed_composition": anti}


def main() -> int:
    print("c720 ambient stabilizer versus domain symmetry on the cycle-696 open-box "
          "static assembly")
    print("box sizes {} | domains: full box, corner simplices, one slab".format(
        " ".join(str(v) for v in L_LIST)))
    section_a()
    for L in L_LIST:
        run_L(L)
    rejectors()

    gate("D0.separation_margin",
         WORST["const"] < TOL_LEVEL < WORST["gap"] and WORST["sep"] >= BOUND_SEP,
         "largest within-orbit spread {} smallest level gap {} smallest ratio {}".format(
             fmt(WORST["const"]), fmt(WORST["gap"]), fmt(WORST["sep"])))
    print("D0 over all rows: largest within-orbit spread {} smallest level gap {} "
          "smallest ratio {}".format(fmt(WORST["const"]), fmt(WORST["gap"]),
                                     fmt(WORST["sep"])))
    NOTES["separation"] = {"largest_within_orbit": fmt(WORST["const"]),
                           "smallest_gap": fmt(WORST["gap"]),
                           "smallest_ratio": fmt(WORST["sep"])}

    receipt = {"box_sizes": list(L_LIST),
               "classes_expected": N_CLASSES,
               "corner_cuts": list(CORNER_K),
               "fail": N_FAIL,
               "gates": GATES,
               "identity_frame": IDENT,
               "notes": NOTES,
               "pass": N_PASS,
               "runner": Path(__file__).name,
               "sextet": list(SEXTET),
               "slab_cut": SLAB_CUT}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")

    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
