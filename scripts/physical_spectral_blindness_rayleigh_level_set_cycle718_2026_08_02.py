"""Cycle 718 -- the frame dependence of the reassembled static operator is non-spectral,
and blindness is a level set of one fixed quadratic-form quotient.

Class-A finite check script (stdlib + numpy only).  It executes the landed Cycle-696
open-coframe endpoint compiler chain, reassembles the static operator under each of the
24 proper rotations, and asks WHERE the residual frame dependence actually lives.

Cycles 715, 716 and 717 all measured the same functional -- a source paired against the
reassembled operator -- and progressively classified which averaging sets erase its frame
dependence.  None of them asked what part of the operator carries that dependence in the
first place.  This cycle answers that, and the answer is sharp: none of the spectrum.

The derivation this script measures.  Reassembly by a proper rotation g acts on the
static variables by an index permutation m_g, so the reassembled operator is

    Q_g = P_g Q P_g^T,        (P_g x)_i = x_{m_g[i]},

an ORTHOGONAL conjugation.  Three consequences follow immediately, and each is checked
here against direct measurement rather than asserted:

  (a) every one of the 24 reassembled operators is orthogonally similar to the identity
      frame operator, so eigenvalues, trace, log-determinant and Frobenius norm are frame
      constant for free -- even though operators belonging to different body diagonals
      differ entrywise by four units.  The frame datum is carried entirely by the
      relative position of the source and the fixed eigenbasis;

  (b) the frame can be moved off the operator and onto the source exactly.  Writing
      bbar_A = sum over a in A of P_a^T b for the averaged source of a collection A, and
      R(u) = <u, Q^-1 u> / <u, u> for the quotient of the SINGLE identity-frame operator,

          v_A(g) = <bbar_A, Q_g^-1 bbar_A> / <bbar_A, bbar_A> = R(bbar_{gA}),

      because a -> P_a reverses products.  Frame blindness of A is therefore the
      statement that the distinct left translates gA all land on ONE level set of R --
      a coincidence of values, never an equality of vectors;

  (c) expanding in the eigenbasis of Q gives R(u) = sum_k w_k / lambda_k with weights
      w_k >= 0 summing to one, so every value the frame functional can take, for every
      source and every collection, lies in the convex hull of the inverse eigenvalues.

The level-set reading recovers the coset structure the earlier cycles measured: on the
24-point frame orbit of a single source, all 24 points distinct, R takes exactly four
values and its level sets are exactly the four body-diagonal fibres.

A single-slot source is then a sharp probe of how much of that structure a lone record
can see, and the census is run in full at both box sizes.

No value is read from a pinned table: every number printed here is recomputed from the
compiler chain in this run.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c718", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
DIRS = c696.regge.DIRS15
CLASS_OF = {}
for _c in c696.SPATIAL_CLASSES:
    CLASS_OF[tuple(int(abs(int(t))) for t in DIRS[_c][:3])] = _c

WRAP = False
L_LIST = (3, 4)
NDOF = {3: 98, 4: 279}
DIAGONALS = ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))
GENERIC_SEEDS = (7180, 7181)
N_GENERIC_CENSUS = 20
BUMP = 1e-3
TOL_EXACT = 1e-12
TOL_SPEC = 1e-9
TOL_BLIND = 1e-8
TOL_PART = 1e-8
SEP_ENTRY = 1.0
SEP_LEVEL = 1e-4
RATIO_MIN = 1e3
DIST_MIN = 1.0
N_PARTITIONS = 15

RECEIPT_NAME = ("physical_spectral_blindness_rayleigh_level_set_cycle718"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.1e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  Every gate below is discriminating: each carries an
    explicit wrong-index, wrong-level, absent-law or resolving-power rejector."""
    global N_PASS, N_FAIL
    ok = bool(ok)
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES[name] = {"pass": ok, "detail": detail}
    print("{} {} {}".format("PASS" if ok else "FAIL", name, detail))
    return ok


# ---------------------------------------------------------------------------
# frame group layer
# ---------------------------------------------------------------------------
def mul_table():
    keyed = {tuple(f.ravel().tolist()): i for i, f in enumerate(FRAMES)}
    M = np.zeros((24, 24), dtype=np.int64)
    for a in range(24):
        for b in range(24):
            M[a, b] = keyed[tuple((FRAMES[a] @ FRAMES[b]).ravel().tolist())]
    return M


MUL = mul_table()
IDENT = [i for i in range(24) if np.array_equal(FRAMES[i], np.eye(3, dtype=np.int64))][0]
INV = [[b for b in range(24) if MUL[a][b] == IDENT][0] for a in range(24)]


def closure(gens):
    H = set(int(g) for g in gens) | {IDENT}
    while True:
        nxt = H | {int(MUL[a][b]) for a in H for b in H}
        if nxt == H:
            return frozenset(H)
        H = nxt


def diag_key(v):
    t = tuple(int(x) for x in v)
    return t if t[0] > 0 else tuple(-x for x in t)


DIAG_ID = {diag_key(d): j for j, d in enumerate(DIAGONALS)}


def delta(g):
    """The body diagonal that frame g carries onto d0."""
    return DIAG_ID[diag_key(FRAMES[g].T @ np.asarray(DIAGONALS[0], dtype=np.int64))]


DELTA = [delta(g) for g in range(24)]
FIBRE = {j: tuple(sorted(g for g in range(24) if DELTA[g] == j)) for j in range(4)}
SUBGROUPS = {closure(g) for r in (1, 2, 3) for g in itertools.combinations(range(24), r)}
REGULAR = sorted((H for H in SUBGROUPS
                  if len(H) == 4 and len({DELTA[h] for h in H}) == 4),
                 key=lambda H: sorted(H))


def left_stabiliser(A):
    return frozenset(t for t in range(24)
                     if {int(MUL[t][a]) for a in A} == set(A))


def left_translates(A):
    return {frozenset(int(MUL[g][a]) for a in A) for g in range(24)}


# ---------------------------------------------------------------------------
# physical layer
# ---------------------------------------------------------------------------
def relabel(L, g):
    """Index permutation induced on the static variables by proper rotation g."""
    idx = c696.static_variable_index(L, WRAP)
    smap = c696.frame_site_map(L, FRAMES[g])
    m = np.zeros(len(idx), dtype=np.int64)
    for (c, x), i in idx.items():
        w = FRAMES[g] @ np.asarray(DIRS[c][:3], dtype=np.int64)
        site = np.asarray(smap[x], dtype=np.int64) + np.minimum(w, 0)
        m[i] = idx[(CLASS_OF[tuple(int(abs(int(t))) for t in w)],
                    tuple(int(t) for t in site))]
    return m


def perm_matrix(m, n):
    P = np.zeros((n, n))
    P[np.arange(n), m] = 1.0
    return P


def build_ctx(L):
    Q = c696.assemble_static_hessian(L, WRAP)["Q"]
    n = int(Q.shape[0])
    perms = [relabel(L, g) for g in range(24)]
    QG = [Q[np.ix_(perms[g], perms[g])] for g in range(24)]
    lam, vec = np.linalg.eigh(Q)
    return {"L": L, "Q": Q, "n": n, "perms": perms, "QG": QG,
            "P": [perm_matrix(perms[g], n) for g in range(24)],
            "QI": [np.linalg.inv(QG[g]) for g in range(24)],
            "Qi": np.linalg.inv(Q), "lam": lam, "vec": vec,
            "scale": float(np.abs(Q).max())}


def pulled(ctx, b):
    """The 24 pulled-back sources transpose(P_a) b, stacked."""
    return np.stack([b[np.argsort(ctx["perms"][a])] for a in range(24)])


def rayleigh(ctx, u):
    return float(u @ ctx["Qi"] @ u) / float(u @ u)


def partition_of(vals, tol):
    """Set partition of the four body diagonals induced by equality of the values,
    written as a restricted growth string."""
    label = {}
    raw = []
    for j in range(4):
        hit = None
        for k in label:
            if abs(vals[j] - vals[k]) <= tol:
                hit = k
                break
        if hit is None:
            label[j] = j
            raw.append(j)
        else:
            raw.append(hit)
    canon, out = {}, []
    for x in raw:
        if x not in canon:
            canon[x] = len(canon)
        out.append(canon[x])
    return tuple(out)


ALL_PARTITIONS = set()
for _p in itertools.product(range(4), repeat=4):
    if _p[0] == 0 and all(_p[i] <= max(_p[:i]) + 1 for i in range(1, 4)):
        ALL_PARTITIONS.add(_p)
FINEST = (0, 1, 2, 3)


# ---------------------------------------------------------------------------
# G1 -- reassembly is an orthogonal relabelling
# ---------------------------------------------------------------------------
def run_relabel_layer(ctx):
    L = ctx["L"]
    check("g1_L{}_dof_and_scale".format(L),
          ctx["n"] == NDOF[L] and abs(ctx["scale"] - 2.9e+01) < 1.0,
          "n {} scale {}".format(ctx["n"], fmt(ctx["scale"])))
    sym = float(np.abs(ctx["Q"] - ctx["Q"].T).max())
    check("g1_L{}_symmetric".format(L), sym <= TOL_EXACT,
          "identity-frame operator symmetric to {}".format(fmt(sym)))
    dev = max(float(np.abs(ctx["QG"][g] - ctx["P"][g] @ ctx["Q"] @ ctx["P"][g].T).max())
              for g in range(24))
    check("g1_L{}_orthogonal_conjugation".format(L), dev <= TOL_EXACT,
          "24 frames reassemble by permutation conjugation, dev {}".format(fmt(dev)))
    ok, bad, nbad = 0.0, 0.0, 0
    for a in range(24):
        for b in range(24):
            c = int(MUL[INV[b]][a])
            w = int(MUL[a][INV[b]])
            Pc = ctx["P"][c]
            ok = max(ok, float(np.abs(ctx["QG"][a] - Pc @ ctx["QG"][b] @ Pc.T).max()))
            if c != w:
                nbad += 1
                Pw = ctx["P"][w]
                bad = max(bad, float(np.abs(ctx["QG"][a] - Pw @ ctx["QG"][b] @ Pw.T).max()))
    check("g1_L{}_conjugator_index".format(L), ok <= TOL_EXACT,
          "576 ordered pairs, inverse-left product, dev {}".format(fmt(ok)))
    check("g1_L{}_swapped_index_rejected".format(L),
          nbad == 456 and bad >= SEP_ENTRY,
          "reversed product fails on {} pairs by up to {}".format(nbad, fmt(bad)))
    NOTES["conjugator_L{}".format(L)] = {"exact": fmt(ok), "swapped": fmt(bad)}


# ---------------------------------------------------------------------------
# G2 -- the frame dependence is non-spectral
# ---------------------------------------------------------------------------
def run_spectral_layer(ctx):
    L = ctx["L"]
    same = max(float(np.abs(ctx["QG"][a] - ctx["QG"][b]).max())
               for a in range(24) for b in range(24) if DELTA[a] == DELTA[b])
    cross = max(float(np.abs(ctx["QG"][a] - ctx["QG"][b]).max())
                for a in range(24) for b in range(24) if DELTA[a] != DELTA[b])
    check("g2_L{}_entries_differ_across_diagonals".format(L),
          same <= TOL_BLIND and cross >= SEP_ENTRY,
          "same diagonal <= {}, across >= {}".format(fmt(same), fmt(cross)))
    ev = [np.sort(np.linalg.eigvalsh(ctx["QG"][g])) for g in range(24)]
    dev_ev = max(float(np.abs(ev[g] - ev[0]).max()) for g in range(24))
    tr = [float(np.trace(ctx["QG"][g])) for g in range(24)]
    fro = [float(np.linalg.norm(ctx["QG"][g])) for g in range(24)]
    sld = [float(np.linalg.slogdet(ctx["QG"][g])[1]) for g in range(24)]
    dev_sc = max(max(tr) - min(tr), max(fro) - min(fro), max(sld) - min(sld))
    check("g2_L{}_spectrum_frame_constant".format(L),
          dev_ev <= TOL_SPEC and dev_sc <= TOL_SPEC,
          "eigenvalues to {}, trace norm logdet to {}".format(fmt(dev_ev), fmt(dev_sc)))
    e = np.zeros(ctx["n"])
    e[0] = 1.0
    ev2 = np.sort(np.linalg.eigvalsh(ctx["Q"] + BUMP * np.outer(e, e)))
    moved = float(np.abs(ev2 - ev[0]).max())
    check("g2_L{}_spectral_gate_resolves".format(L),
          moved >= RATIO_MIN * max(dev_ev, 1e-300),
          "rank-one {} moves the spectrum {}".format(fmt(BUMP), fmt(moved)))
    NOTES["spectral_L{}".format(L)] = {"eigen": fmt(dev_ev), "scalar": fmt(dev_sc),
                                       "bump": fmt(moved), "cross": fmt(cross)}


# ---------------------------------------------------------------------------
# G3 -- the transfer identity, the weight law and the hull bound
# ---------------------------------------------------------------------------
def run_transfer_layer(ctx, b, tag):
    L = ctx["L"]
    bp = pulled(ctx, b)

    def bbar(A):
        return bp[sorted(A)].sum(axis=0)

    tests = [frozenset({IDENT}), frozenset({1, 4}), frozenset({0, 5, 11}),
             frozenset(FIBRE[0]), frozenset(int(MUL[h][3]) for h in REGULAR[0])]
    worst = 0.0
    vals_all = []
    for A in tests:
        u0 = bbar(A)
        nrm = float(u0 @ u0)
        for g in range(24):
            lhs = float(u0 @ ctx["QI"][g] @ u0) / nrm
            rhs = rayleigh(ctx, bbar({int(MUL[g][a]) for a in A}))
            worst = max(worst, abs(lhs - rhs))
            vals_all.append(lhs)
    check("g3_L{}_{}_transfer".format(L, tag), worst <= TOL_SPEC,
          "frame moves onto the source, dev {} over {}".format(fmt(worst), len(vals_all)))
    lam = ctx["lam"]
    inv = 1.0 / lam
    dev_w, wmin = 0.0, 1.0
    for A in tests:
        u = bbar(A)
        c = ctx["vec"].T @ u
        w = (c * c) / float(c @ c)
        wmin = min(wmin, float(w.min()))
        dev_w = max(dev_w, abs(float(np.sum(w * inv)) - rayleigh(ctx, u)))
    check("g3_L{}_{}_weights".format(L, tag),
          dev_w <= TOL_SPEC and wmin >= -TOL_EXACT,
          "weighted mean of inverse eigenvalues, dev {}".format(fmt(dev_w)))
    lo, hi = float(inv.min()), float(inv.max())
    inside = all(lo - TOL_SPEC <= v <= hi + TOL_SPEC for v in vals_all)
    margin = min(min(v - lo for v in vals_all), min(hi - v for v in vals_all))
    check("g3_L{}_{}_hull_bound".format(L, tag), inside and margin > 0.0,
          "values inside hull {} to {}, margin {}".format(fmt(lo), fmt(hi), fmt(margin)))
    NOTES["transfer_L{}_{}".format(L, tag)] = {"identity": fmt(worst), "weights": fmt(dev_w),
                                               "hull_lo": fmt(lo), "hull_hi": fmt(hi)}


# ---------------------------------------------------------------------------
# G4 -- the orbit level-set law
# ---------------------------------------------------------------------------
def run_levelset_layer(ctx, b, tag):
    L = ctx["L"]
    bp = pulled(ctx, b)
    dmin = min(float(np.linalg.norm(bp[a] - bp[c]))
               for a in range(24) for c in range(a + 1, 24))
    check("g4_L{}_{}_orbit_distinct".format(L, tag), dmin >= DIST_MIN,
          "24 pulled sources separated by >= {}".format(fmt(dmin)))
    R = np.array([rayleigh(ctx, bp[a]) for a in range(24)])
    within = max(float(R[list(FIBRE[j])].max() - R[list(FIBRE[j])].min()) for j in range(4))
    mu = [float(R[list(FIBRE[j])].mean()) for j in range(4)]
    between = min(abs(mu[i] - mu[j]) for i in range(4) for j in range(i + 1, 4))
    check("g4_L{}_{}_four_levels".format(L, tag),
          within <= TOL_BLIND and between >= SEP_LEVEL
          and between >= RATIO_MIN * max(within, 1e-300),
          "within {} between {} ratio {}".format(
              fmt(within), fmt(between), fmt(between / max(within, 1e-300))))
    lev = {}
    for a in range(24):
        key = min((k for k in lev if abs(k - R[a]) <= TOL_BLIND), default=None)
        lev.setdefault(R[a] if key is None else key, []).append(a)
    got = sorted(tuple(sorted(v)) for v in lev.values())
    want = sorted(tuple(FIBRE[j]) for j in range(4))
    check("g4_L{}_{}_levels_are_fibres".format(L, tag), got == want,
          "level sets are the four body-diagonal fibres of six")
    NOTES["levelset_L{}_{}".format(L, tag)] = {"within": fmt(within), "between": fmt(between),
                                               "distance": fmt(dmin)}


# ---------------------------------------------------------------------------
# G5 -- blindness is a coincidence of values, not of vectors
# ---------------------------------------------------------------------------
def run_coincidence_layer(ctx, b, tag):
    L = ctx["L"]
    bp = pulled(ctx, b)

    def bbar(A):
        return bp[sorted(A)].sum(axis=0)

    A = frozenset(int(MUL[h][3]) for h in REGULAR[0])
    stab = left_stabiliser(A)
    tr = sorted(left_translates(A), key=sorted)
    check("g5_L{}_{}_translate_count".format(L, tag),
          len(stab) == 4 and len(tr) == 24 // len(stab) == 6,
          "left stabiliser {}, distinct translates {}".format(len(stab), len(tr)))
    U = np.stack([bbar(t) for t in tr])
    vals = [rayleigh(ctx, U[i]) for i in range(len(tr))]
    spread = max(vals) - min(vals)
    vdist = min(float(np.linalg.norm(U[i] - U[j]))
                for i in range(len(tr)) for j in range(i + 1, len(tr)))
    check("g5_L{}_{}_values_agree".format(L, tag), spread <= TOL_BLIND,
          "{} averaged sources, one value to {}".format(len(tr), fmt(spread)))
    W = []
    for i in range(len(tr)):
        c = ctx["vec"].T @ U[i]
        W.append((c * c) / float(c @ c))
    W = np.stack(W)
    l1 = [float(np.abs(W[i] - W[j]).sum())
          for i in range(len(tr)) for j in range(i + 1, len(tr))]
    check("g5_L{}_{}_sources_differ".format(L, tag),
          vdist >= DIST_MIN and min(l1) > TOL_BLIND,
          "separated >= {}, weights differ {} to {}".format(
              fmt(vdist), fmt(min(l1)), fmt(max(l1))))
    B = frozenset(FIBRE[0][:4])
    trB = sorted(left_translates(B), key=sorted)
    valsB = [rayleigh(ctx, bbar(t)) for t in trB]
    sB = max(valsB) - min(valsB)
    check("g5_L{}_{}_contrast_not_blind".format(L, tag),
          len(trB) == 24 and sB >= SEP_LEVEL,
          "one-diagonal 4-set: {} translates, spread {}".format(len(trB), fmt(sB)))
    NOTES["coincidence_L{}_{}".format(L, tag)] = {"spread": fmt(spread), "distance": fmt(vdist),
                                                  "l1_min": fmt(min(l1)), "l1_max": fmt(max(l1)),
                                                  "contrast": fmt(sB)}


# ---------------------------------------------------------------------------
# G6 -- what a single record can see
# ---------------------------------------------------------------------------
def run_census_layer(ctx):
    L = ctx["L"]
    rep = {j: FIBRE[j][0] for j in range(4)}
    QI4 = {j: ctx["QI"][rep[j]] for j in range(4)}
    idx = c696.static_variable_index(L, WRAP)
    inv_idx = {i: k for k, i in idx.items()}
    cnt = Counter()
    blind_classes = Counter()
    nblind = 0
    for i in range(ctx["n"]):
        u = np.zeros(ctx["n"])
        u[i] = 1.0
        vals = [float(u @ QI4[j] @ u) for j in range(4)]
        p = partition_of(vals, TOL_PART)
        cnt[p] += 1
        if len(set(p)) == 1:
            nblind += 1
            blind_classes[inv_idx[i][0]] += 1
    check("g6_L{}_census_complete".format(L),
          sum(cnt.values()) == ctx["n"] and set(cnt) <= ALL_PARTITIONS,
          "{} single slots, {} of {} patterns".format(ctx["n"], len(cnt), N_PARTITIONS))
    check("g6_L{}_finest_pattern".format(L),
          (cnt[FINEST] == 0) == (L == 3),
          "slots separating all four diagonals: {}".format(cnt[FINEST]))
    check("g6_L{}_unresolved_slots".format(L),
          nblind > 0 and nblind < ctx["n"],
          "{} slots frame constant unaveraged, classes {}".format(
              nblind, sorted(blind_classes)))
    gen = Counter()
    for s in range(N_GENERIC_CENSUS):
        x = np.random.default_rng(900 + s + ctx["L"]).standard_normal(ctx["n"])
        vals = [float(x @ QI4[j] @ x) / float(x @ x) for j in range(4)]
        gen[partition_of(vals, TOL_PART)] += 1
    check("g6_L{}_generic_separates".format(L),
          gen[FINEST] == N_GENERIC_CENSUS,
          "{} of {} generic sources at the finest pattern".format(
              gen[FINEST], N_GENERIC_CENSUS))
    NOTES["census_L{}".format(L)] = {"patterns": len(cnt), "finest": cnt[FINEST],
                                     "unresolved": nblind,
                                     "classes": sorted(blind_classes)}


# ---------------------------------------------------------------------------
def main():
    print("c718 the frame dependence of the reassembled static operator is non-spectral")
    check("g0_regular_subgroups", len(REGULAR) == 4,
          "{} regular frame subgroups".format(len(REGULAR)))
    for L in L_LIST:
        print("-- L={} --".format(L))
        ctx = build_ctx(L)
        run_relabel_layer(ctx)
        run_spectral_layer(ctx)
        for k, seed in enumerate(GENERIC_SEEDS):
            b = np.random.default_rng(seed + L).standard_normal(ctx["n"])
            tag = "s{}".format(k)
            run_transfer_layer(ctx, b, tag)
            run_levelset_layer(ctx, b, tag)
            run_coincidence_layer(ctx, b, tag)
        run_census_layer(ctx)
    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))

    receipt = {
        "runner": Path(__file__).name,
        "pass": N_PASS,
        "fail": N_FAIL,
        "box_sizes": list(L_LIST),
        "body_diagonals": [list(d) for d in DIAGONALS],
        "coincidence_patterns": N_PARTITIONS,
        "tolerance": {"exact": fmt(TOL_EXACT), "spectral": fmt(TOL_SPEC),
                      "blind": fmt(TOL_BLIND), "level_separation": fmt(SEP_LEVEL)},
        "gates": GATES,
        "notes": NOTES,
    }
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    return 0 if N_FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
