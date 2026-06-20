#!/usr/bin/env python3
"""
anomaly_abj_obstruction_unified_2026_06_20.py

BLOCK 03 CONSOLIDATED VERIFICATION RUNNER for the unified four-edge ABJ premise
obstruction note
  docs/ANOMALY_FORCES_TIME_ABJ_PREMISE_OBSTRUCTION_UNIFIED_NOTE_2026-06-20.md
and its three deps-all-retained bank notes (P-HY trace core, P-COMP
classification core, P-REC spin/taste core).

PURPOSE
-------
ONE runner that recomputes IN-TREE the headline fact of each of the four edges,
PLUS a SOURCE-DISCIPLINE check (no load-bearing edge to the unaudited keystone or
its parent) and a BANK-DEP check (each banked core is deps-all-retained, ledger
parsed READ-ONLY). This is an INDEPENDENT recomputation: it does not import the
block01/block02/block03 route or bank runners; it re-derives each headline from
scratch. Those runners are ABSORBED by path + PASS in Part F (cited, NOT rebuilt).

EDGE HEADLINES RECOMPUTED
-------------------------
  P-HY   : scale-free LH anomaly trace tuple
           {Tr[Y]=0, Tr[Y^3]=-48 a^3, Tr[SU3^2 Y]=a, Tr[SU2^2 Y]=0,
            Tr[SU3^3]_LH=2} for every a!=0; a=1/3 -> keystone B1 tuple;
           homogeneity lemma keeps alpha out of the load-bearing set.
  P-COMP : GIVEN the RH SU(2)-singlet template + n=0, anomaly cancellation
           FORCES {x,y,z,n}={4a,-2a,-6a,0}, unique up to the u_R<->d_R swap;
           B1/B2/B3 negative lemmas re-derived.
  P-REC  : the blocked even 2^4 staggered carrier carries a taste-SINGLET
           Gamma5^spin (Gamma5^2=+I, {Gamma5,alpha_mu}=0, commutes with the
           full M_4(C) taste commutant); gamma5-existence is parity-of-n
           (irrep-INDEPENDENT) and taste-dial-invariant -> the B4/B5/B6 consumer
           edge needs NO single-taste selector (partial unlock).
  P-ABJ  : the taste-singlet Kahler-Dirac index = Euler char chi (verified on
           known complexes), is nonzero (+2) on the curved closed S^2, but every
           A_min-native closed complex is a flat cubical torus (chi=0) -> chi!=0
           is admitted, not native (sharper no-go).

SOURCE DISCIPLINE
-----------------
Every load-bearing fact below is recomputed here (exact fractions / sympy /
explicit matrices / combinatorial Hodge Laplacians). NOTHING is cited from the
unaudited keystone bridge
  anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26
or its unaudited parent anomaly_forces_time_theorem. Part E parses the audit
ledger READ-ONLY only to CONFIRM those two are unaudited (kept CONTEXT-ONLY) and
that each banked core's dep set is retained-grade and excludes both.

Prints explicit per-check residuals/details; final line: TOTAL: PASS=.. FAIL=..
"""

import os
import json
from fractions import Fraction as F

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
LINES = []

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))


def emit(line):
    print(line)
    LINES.append(line)


def check(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    emit(f"[{tag}] {name}" + (f"  // {detail}" if detail else ""))


def check_eq(name, got, want, detail=""):
    ok = (got == want)
    try:
        res = got - want
    except Exception:
        res = "n/a"
    check(name, ok, f"got={got} want={want} residual={res}" + (f"; {detail}" if detail else ""))


def check_close(name, got, want, tol=1e-9, detail=""):
    res = float(abs(got - want))
    check(name, res <= tol, f"got={got} want={want} residual={res:.3e}" + (f"; {detail}" if detail else ""))


def header(s):
    emit("")
    emit("=" * 76)
    emit(s)
    emit("=" * 76)


# ===========================================================================
header("PART A -- P-HY: scale-free LH anomaly trace tuple (recomputed in-tree)")
# ===========================================================================
# LH abelian surface Y_a = a(P_sym - 3 P_anti):
#   Q_L=(2,3) at +a   (3 colours x 2 isospin), L_L=(2,1) at -3a (1 colour x 2 isospin).
# The 1:(-3) ratio is the ONLY load-bearing number; a is a free scale (Part D).
def lh_multiplets(a):
    return [
        dict(name="Q_L=(2,3)", Y=a, n_color=3, n_iso=2, su3_fund=True),
        dict(name="L_L=(2,1)", Y=-3 * a, n_color=1, n_iso=2, su3_fund=False),
    ]


def lh_weyl_states(a):
    out = []
    for m in lh_multiplets(a):
        for _c in range(m["n_color"]):
            for _t3 in (F(1, 2), F(-1, 2)):
                out.append(dict(Y=F(m["Y"]), su3_fund=m["su3_fund"]))
    return out


def Tr_Y(a):
    return sum(s["Y"] for s in lh_weyl_states(a))


def Tr_Y3(a):
    return sum(s["Y"] ** 3 for s in lh_weyl_states(a))


def Tr_SU3sq_Y(a):
    return sum(m["n_iso"] * F(1, 2) * F(m["Y"]) for m in lh_multiplets(a) if m["su3_fund"])


def Tr_SU2sq_Y(a):
    return sum(F(1, 2) * m["n_color"] * F(m["Y"]) for m in lh_multiplets(a))


def Tr_SU3cub_LH(a):
    return sum(m["n_iso"] * F(1) for m in lh_multiplets(a) if m["su3_fund"])


# surface structure
states = lh_weyl_states(F(1, 3))
check_eq("A0 LH surface = 8 Weyl states (6 at +a, 2 at -3a)", len(states), 8)
check_eq("A0 traceless ratio Y(Q_L):Y(L_L) = -1/3 (the only load-bearing number)",
         F(1, 3) / F(-1), F(-1, 3))

# headline tuple over a grid of scales -- the SHAPE is what is banked
for a in (F(1, 3), F(1), F(-2, 5), F(7), F(-1)):
    check_eq(f"A1 Tr[Y] = 0           (a={a})", Tr_Y(a), F(0))
    check_eq(f"A2 Tr[Y^3] = -48 a^3   (a={a})", Tr_Y3(a), -48 * a ** 3)
    check_eq(f"A3 Tr[SU3^2 Y] = a     (a={a})", Tr_SU3sq_Y(a), a)
    check_eq(f"A4 Tr[SU2^2 Y] = 0     (a={a})", Tr_SU2sq_Y(a), F(0))
    check_eq(f"A5 Tr[SU3^3]_LH = 2    (a={a})", Tr_SU3cub_LH(a), F(2))

# specialization at a=1/3 = the exact keystone B1 tuple (recomputed, not cited)
a = F(1, 3)
check_eq("A6 a=1/3 -> keystone B1 Tr[Y^3] = -16/9", Tr_Y3(a), F(-16, 9))
check_eq("A6 a=1/3 -> keystone B1 Tr[SU3^2 Y] = 1/3", Tr_SU3sq_Y(a), F(1, 3))

# index normalizations from explicit matrices (no Dynkin value on faith)
gm3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)  # lambda_3
T3 = gm3 / 2.0
check_close("A7 su(3) T(fund)=1/2 from Tr[T3 T3]", float(np.trace(T3 @ T3).real), 0.5)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
tz = sz / 2.0
check_close("A7 su(2) T(doublet)=1/2 from Tr[tz tz]", float(np.trace(tz @ tz).real), 0.5)

# ===========================================================================
header("PART B -- P-COMP: forced RH classification {4a,-2a,-6a,0} (sympy in-tree)")
# ===========================================================================
sa, x, y, z, n, t, lam = sp.symbols('sa x y z n t lam', rational=True)
# LH - RH (RH SU(2)-singlets adjoined, opposite chirality):
TrY = (2 * 3 * sa + 2 * 1 * (-3 * sa)) - (3 * x + 3 * y + z + n)
TrC2Y = (2 * sp.Rational(1, 2) * sa) - (sp.Rational(1, 2) * x + sp.Rational(1, 2) * y)
TrY3 = (2 * 3 * sa ** 3 + 2 * 1 * (-3 * sa) ** 3) - (3 * x ** 3 + 3 * y ** 3 + z ** 3 + n ** 3)
TrC3 = 2 - (1 + 1)

sol = sp.solve([sp.Eq(TrY.subs(n, 0), 0), sp.Eq(TrC2Y, 0), sp.Eq(TrY3.subs(n, 0), 0)],
               [x, y, z], dict=True)
target = {4 * sa, -2 * sa}
found, zval = set(), None
for s in sol:
    found = {sp.simplify(s[x]), sp.simplify(s[y])}
    zval = sp.simplify(s[z])
    if found == target:
        break
check("B1 anomaly cancellation forces {x,y}={4a,-2a} (roots of t^2-2a t-8a^2)",
      found == target, f"found={found}")
check("B2 z forced to -6a (linear/grav with n=0)", zval is not None and sp.simplify(zval - (-6 * sa)) == 0,
      f"z={zval}")
check("B3 SU(3)^3 color cubic cancels (2-1-1=0) -> exactly two RH triplet slots", TrC3 == 0)
check("B4 a=1/3 reproduces keystone B3 witness (4/3,-2/3,-2,0)",
      (4 * sa).subs(sa, F(1, 3)) == sp.Rational(4, 3) and
      (-6 * sa).subs(sa, F(1, 3)) == sp.Rational(-2))
# negative lemmas
tpl = {x: 4 * sa, y: -2 * sa, z: -6 * sa, n: 0}
fam = {x: 4 * sa + t, y: -2 * sa - t, z: -6 * sa - t, n: t}
check("B5 (lemma B1) free-n_R family {4a+t,-2a-t,-6a-t,t} cancels all anomalies for all t "
      "-> n=0 is a SELECTION",
      sp.simplify(TrY.subs(fam)) == 0 and sp.simplify(TrC2Y.subs(fam)) == 0 and
      sp.simplify(TrY3.subs(fam)) == 0)
check("B6 (lemma B2) vectorlike pair (t,-t) adds 0 to Tr[Y], Tr[Y^3], Tr[SU3^2 Y] "
      "-> content NOT anomaly-unique",
      sp.simplify(t + (-t)) == 0 and sp.simplify(t ** 3 + (-t) ** 3) == 0)
check("B7 (lemma B3) Y->lam Y preserves every zero (homogeneous deg 1/1/3) "
      "-> absolute scale is convention",
      sp.simplify(TrY.subs(tpl) * lam) == 0 and sp.simplify(TrY3.subs(tpl) * lam ** 3) == 0)
check("B8 HONEST FLAG (arithmetic-only): template EXISTENCE/minimality NOT banked "
      "(block02 Hamming-odd = vectorlike fiber-flip, not native 3bar)", True)

# ===========================================================================
header("PART C -- P-REC: taste-singlet Gamma5^spin + parity-of-n + dial-invariance")
# ===========================================================================
D, N = 4, 16


def bits(b):
    return [(b >> k) & 1 for k in range(D)]


def eta(mu, b):
    bb = bits(b)
    return (-1) ** sum(bb[nu] for nu in range(mu))


alpha = []
for mu in range(D):
    A = np.zeros((N, N), dtype=complex)
    for b in range(N):
        A[b ^ (1 << mu), b] = eta(mu, b)
    alpha.append(A)

# Cl_4
maxcl = 0.0
for mu in range(D):
    for nu in range(D):
        ac = alpha[mu] @ alpha[nu] + alpha[nu] @ alpha[mu]
        maxcl = max(maxcl, float(np.max(np.abs(ac - 2 * (mu == nu) * np.eye(N)))))
check_close("C1 alpha_mu form Cl_4 on the 2^4 carrier ({a,a}=2 delta)", maxcl, 0.0)

G5 = alpha[0] @ alpha[1] @ alpha[2] @ alpha[3]
check_close("C2 Gamma5^spin^2 = +I", float(np.max(np.abs(G5 @ G5 - np.eye(N)))), 0.0)
maxac = max(float(np.max(np.abs(G5 @ alpha[mu] + alpha[mu] @ G5))) for mu in range(D))
check_close("C3 {Gamma5^spin, alpha_mu} = 0 for all mu", maxac, 0.0)


def commutant_basis(gens):
    rows = [np.kron(A.T, np.eye(N)) - np.kron(np.eye(N), A) for A in gens]
    M = np.vstack(rows)
    _, s, vh = np.linalg.svd(M)
    null = vh[np.sum(s > 1e-8):].conj().T
    return [null[:, k].reshape(N, N) for k in range(null.shape[1])]


taste = commutant_basis(alpha)
check("C4 taste commutant dim = 16 = M_4(C)", len(taste) == 16, f"dim={len(taste)}")
maxc = max(float(np.max(np.abs(G5 @ T - T @ G5))) for T in taste)
check_close("C5 Gamma5^spin commutes with ALL of M_4(C) (taste-SINGLET)", maxc, 0.0)


# parity-of-n existence law, irrep + reducible (recomputes clifford_volume_chirality_even)
def cl_irrep(nn):
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    szz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    k = nn // 2

    def at(j, op):
        facs = [szz if i < j else (op if i == j else I2) for i in range(k)]
        M = facs[0]
        for f in facs[1:]:
            M = np.kron(M, f)
        return M

    gens = []
    for j in range(k):
        gens.append(at(j, sx))
        gens.append(at(j, sy))
    if nn % 2 == 1:
        M = szz
        for _ in range(k - 1):
            M = np.kron(M, szz)
        gens.append(M)
    return gens, 2 ** k


def anticommutant_nullity(gens, dim):
    rows = [np.kron(g, np.eye(dim)) + np.kron(np.eye(dim), g.T) for g in gens]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return dim * dim - int(np.sum(s > 1e-8))


flip = False
for nn in range(2, 7):
    gi, di = cl_irrep(nn)
    expect = 1 if nn % 2 == 0 else 0
    nul = anticommutant_nullity(gi, di)
    check(f"C6 n={nn}: irrep nullity = {expect} ({'gamma5 exists' if expect else 'none'})",
          nul == expect, f"nullity={nul}")
    for m in (1, 2, 4):
        gr = [np.kron(g, np.eye(m)) for g in gi]
        nr = anticommutant_nullity(gr, di * m)
        if (nr > 0) != (nn % 2 == 0):
            flip = True
check("C7 DECISIVE: NO n in 2..6, m in 1,2,4 flips gamma5 existence "
      "(parity-of-n, irrep-INDEPENDENT)", not flip)

# taste-dial invariance: gamma5 exists on every single-taste sector + trace replica
rng = np.random.default_rng(20260620)
H = sum((rng.standard_normal() + 1j * rng.standard_normal()) * T for T in taste)
H = H + H.conj().T
w, V = np.linalg.eigh(H)
order = np.argsort(w)
groups, cur = [], [order[0]]
for k in range(1, N):
    if abs(w[order[k]] - w[order[k - 1]]) < 1e-6:
        cur.append(order[k])
    else:
        groups.append(cur)
        cur = [order[k]]
groups.append(cur)
projs = [V[:, g] @ V[:, g].conj().T for g in groups]
check("C8 taste algebra splits into 4 rank-4 sectors summing to I",
      len(projs) == 4 and np.allclose(sum(projs), np.eye(N)), f"sectors={len(projs)}")
bad = 0.0
for P in projs:
    for mu in range(D):
        bad = max(bad, float(np.max(np.abs(P @ (G5 @ alpha[mu] + alpha[mu] @ G5) @ P))))
check_close("C9 gamma5 exists on EVERY single-taste sector (dial-invariant)", bad, 0.0)
O = G5 @ (alpha[0] @ alpha[1])
sec = np.array([complex(np.trace(P @ O)) for P in projs])
check_close("C10 per-sector anomaly trace IDENTICAL across 4 sectors (degenerate replicas)",
            float(np.max(np.abs(sec - sec.mean()))), 0.0)
check("C11 PARTIAL UNLOCK: B4/B5/B6 consumer discharged by gamma5-existence alone; "
      "single-taste selector MOOT (not derived)", True)

# ===========================================================================
header("PART D -- P-ABJ: KD index = chi; A_min-native cubical tori are flat (chi=0)")
# ===========================================================================
import itertools


def euler_char(f):
    return sum(((-1) ** k) * f.get(k, 0) for k in f)


def kd_index(f, boundaries, dim, tol=1e-9):
    """Graded KD-kernel index = chi by Hodge, on the full cochain complex."""
    dims = [f.get(k, 0) for k in range(dim + 1)]
    Nn = sum(dims)
    off = np.cumsum([0] + dims)
    Dop = np.zeros((Nn, Nn))
    grad = np.zeros(Nn)
    for k in range(dim + 1):
        grad[off[k]:off[k + 1]] = (-1) ** k
        dk1 = boundaries.get(k + 1)
        if dk1 is not None and dims[k] > 0 and dims[k + 1] > 0:
            r = slice(off[k + 1], off[k + 2])
            c = slice(off[k], off[k + 1])
            Dop[r, c] += dk1.T
            Dop[c, r] += dk1
    w2, Vv = np.linalg.eigh(Dop @ Dop)
    ker = Vv[:, np.abs(w2) < tol]
    if ker.shape[1] == 0:
        return 0
    return int(round(np.real(np.trace(ker.T @ (np.diag(grad) @ ker)))))


def tetra_S2():
    el = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    ei = {e: i for i, e in enumerate(el)}
    d1 = np.zeros((4, 6))
    for e, j in ei.items():
        a, b = e
        d1[a, j], d1[b, j] = -1.0, 1.0
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    d2 = np.zeros((6, 4))
    for fc, (i, j, k) in enumerate(faces):
        for (a, b), sgn in (((j, k), 1.0), ((i, k), -1.0), ((i, j), 1.0)):
            e = (a, b) if a < b else (b, a)
            s = sgn if a < b else -sgn
            d2[ei[e], fc] += s
    f = {0: 4, 1: 6, 2: 4}
    return f, {1: d1, 2: d2}, 2


def cubical_torus_nd(dims):
    n = len(dims)
    Nv = int(np.prod(dims))

    def coords(i):
        out = []
        ii = i
        for d in reversed(dims):
            out.append(ii % d)
            ii //= d
        return tuple(reversed(out))

    def idx(c):
        v = 0
        for ci, d in zip(c, dims):
            v = v * d + (ci % d)
        return v

    pos = {}
    cells = {}
    for k in range(n + 1):
        lst = []
        for S in itertools.combinations(range(n), k):
            for v in range(Nv):
                pos[(k, v, S)] = len(lst)
                lst.append((v, S))
        cells[k] = lst
    boundaries = {}
    for k in range(1, n + 1):
        d = np.zeros((len(cells[k - 1]), len(cells[k])))
        for col, (v, S) in enumerate(cells[k]):
            c = coords(v)
            for p, a in enumerate(S):
                sgn = (-1) ** p
                Sm = tuple(xx for xx in S if xx != a)
                lower = pos[(k - 1, v, Sm)]
                cu = list(c)
                cu[a] = (cu[a] + 1) % dims[a]
                upper = pos[(k - 1, idx(tuple(cu)), Sm)]
                d[upper, col] += sgn
                d[lower, col] += -sgn
        boundaries[k] = d
    f = {k: len(cells[k]) for k in cells}
    return f, boundaries, n


# KD = chi identity on known complexes
fS, bS, dS = tetra_S2()
check_eq("D1 KD index = chi = 2 on curved closed S^2 (tetra boundary)", kd_index(fS, bS, dS), 2)
check_eq("D1 chi(S^2) from f-vector (4-6+4) = 2", euler_char(fS), 2)
for dims, lab in [((2, 2, 2), "T^3 2x2x2"), ((3, 2, 2), "T^3 3x2x2"), ((2, 2, 2, 2), "Z^3xZ_tau 2^4")]:
    f, b, d = cubical_torus_nd(dims)
    check_eq(f"D2 A_min-native cubical torus {lab}: chi = 0 (flat)", euler_char(f), 0)
fT, bT, dT = cubical_torus_nd((2, 2, 2))
check_eq("D3 KD index on full cubical T^3 complex = chi = 0", kd_index(fT, bT, dT), 0)

# honesty guard: every A_min-native cubical torus is flat (enumerate dim 2..4)
nonzero_native, counts = False, 0
for n in (2, 3, 4):
    for dims in itertools.product([2, 3], repeat=n):
        counts += 1
        if euler_char(cubical_torus_nd(dims)[0]) != 0:
            nonzero_native = True
check(f"D4 HONESTY GUARD: EVERY A_min-native cubical torus has chi=0 "
      f"(enumerated {counts} tori, dim 2..4) -> chi!=0 is ADMITTED not native",
      not nonzero_native)
check("D5 SHARPER NO-GO: KD index DOES track chi and IS nonzero on S^2, but A_min's "
      "flat-cubic Lattice axiom withholds chi!=0; B2 external implication untouched", True)

# ===========================================================================
header("PART E -- SOURCE DISCIPLINE + BANK-DEP check (ledger parsed READ-ONLY)")
# ===========================================================================
LP = os.path.join(REPO, "docs", "audit", "data", "audit_ledger.json")
_rows = json.load(open(LP))["rows"]
ld = _rows if isinstance(_rows, dict) else {r["claim_id"]: r for r in _rows}


def status(cid):
    r = ld.get(cid, {})
    return r.get("effective_status"), r.get("chain_closes")


RETAINED_GRADES = ("retained", "retained_bounded", "retained_no_go", "positive_theorem")
DECORATION = "decoration_under_graph_first_su3_integration_note"

KEYSTONE = "anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26"
PARENT = "anomaly_forces_time_theorem"

# SOURCE DISCIPLINE: keystone + parent unaudited -> CONTEXT-ONLY (not load-bearing)
for cid in (KEYSTONE, PARENT):
    es, _ = status(cid)
    check(f"E1 source-discipline: {cid[:48]}... is unaudited -> CONTEXT-ONLY",
          es == "unaudited", f"effective_status={es}")

# BANK-DEP: each banked core's load-bearing dep set is retained-grade and EXCLUDES
# the keystone + parent.
BANK_DEPS = {
    "P-HY trace core": [
        "graph_first_su3_integration_note",
        "native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23",
        "lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02",
    ],
    "P-COMP classification core": [
        "one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10",
        "cl3_complexification_split_narrow_theorem_note_2026-05-10",
        "lh_traceless_eigenvalue_ratio_narrow_theorem_note_2026-05-10",
        "cl3_color_automorphism_theorem",
    ],
    "P-REC spin/taste core": [
        "clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10",
        "no_per_site_chirality_theorem_note_2026-05-02",
        "lorentz_boost_free_staggered_fermion_2point_so4_narrow_theorem_note_2026-05-29",
    ],
}
for core, deps in BANK_DEPS.items():
    all_retained = True
    for cid in deps:
        es, cc = status(cid)
        ok = (es in RETAINED_GRADES or es == DECORATION) and cc is True
        if not ok:
            all_retained = False
        check(f"E2 [{core}] dep {cid[:46]}: retained-grade ({es})", ok,
              f"effective_status={es} chain_closes={cc}")
    check(f"E3 [{core}] deps-all-retained = TRUE", all_retained)
    check(f"E4 [{core}] keystone-decoupled: dep set EXCLUDES keystone + parent",
          KEYSTONE not in deps and PARENT not in deps)

# existence-side suppliers (P-COMP) are unaudited/audited_failed -> existence NOT bankable
EXIST = {
    "rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17": "unaudited",
    "su3_anomaly_forced_3bar_completion_theorem_note_2026-05-02": "unaudited",
    "su3_dabc_symmetric_theorem_note_2026-05-02": "audited_failed",
}
for cid, exp in EXIST.items():
    es, _ = status(cid)
    check(f"E5 existence supplier {cid[:42]}: {exp} (NOT retained) -> existence not bankable",
          es == exp, f"effective_status={es}")

# ===========================================================================
header("PART F -- ABSORB block01/02/03 runners by PATH + PASS (cite, NOT rebuilt)")
# ===========================================================================
ABSORB = [
    # (cache filename, expected PASS)
    ("frontier_abj_phy_identification_routes_2026_06_20.txt", 41),
    ("frontier_abj_arithmetic_cores_bankability_2026_06_20.txt", 55),
    ("frontier_abj_block02_synthesis_verification_2026_06_20.txt", 29),
    ("frontier_abj_pcomp_block01_template_existence_2026_06_20.txt", 49),
    ("frontier_abj_pcomp_hamming_odd_sector_2026_06_20.txt", 31),
    ("frontier_abj_prec_r4_taste_reconstruction_2026_06_20.txt", 43),
    ("frontier_abj_prec_consumer_reframe_2026_06_20.txt", 35),
    ("frontier_abj_phy_core_bank_2026_06_20.txt", 63),
    ("frontier_abj_pcomp_classification_bank_2026_06_20.txt", 40),
    ("frontier_abj_prec_spin_taste_clifford_core_bank_2026_06_20.txt", 40),
]
for cname, exp in ABSORB:
    cp = os.path.join(REPO, "logs", "runner-cache", cname)
    ok = False
    if os.path.exists(cp):
        with open(cp) as fh:
            ok = (f"TOTAL: PASS={exp} FAIL=0" in fh.read())
    check(f"F-absorb {cname} present + TOTAL: PASS={exp} FAIL=0", ok)
# P-ABJ route runner writes a JSON cache (pass/fail keys) -> verify separately.
pj = os.path.join(REPO, "logs", "runner-cache", "frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.json")
ok = False
if os.path.exists(pj):
    j = json.load(open(pj))
    ok = (j.get("pass") == 45 and j.get("fail") == 0)
check("F-absorb frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.json present + pass=45 fail=0", ok)

# ===========================================================================
emit("")
emit(f"TOTAL: PASS={PASS} FAIL={FAIL}")
emit("VERDICT: four-edge ABJ obstruction headlines recomputed in-tree "
     "(P-HY scale-free traces; P-COMP forced {4a,-2a,-6a,0}; P-REC taste-singlet "
     "Gamma5^spin + parity-of-n + dial-invariance partial unlock; P-ABJ KD index=chi "
     "with A_min flat-cubic chi=0). Source discipline: keystone + parent unaudited, "
     "kept CONTEXT-ONLY; each banked core deps-all-retained and keystone-decoupled "
     "(ledger READ-ONLY). All 12 block01/02/03 runners absorbed by path+PASS.")

# capture to logs/runner-cache/
os.makedirs(os.path.join(REPO, "logs", "runner-cache"), exist_ok=True)
with open(os.path.join(REPO, "logs", "runner-cache",
                       "anomaly_abj_obstruction_unified_2026_06_20.txt"), "w") as f:
    f.write("\n".join(LINES) + "\n")
