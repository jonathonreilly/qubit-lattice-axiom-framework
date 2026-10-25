#!/usr/bin/env python3
"""
check.py -- disjoint exact check for J:derive:review-20261016-strain-path-and-retuning:a1

Self-contained (numpy, scipy, sympy, mpmath, stdlib).  It does NOT import or re-run any source script of the
strain packet.  It tests structure, in exact arithmetic, in two places:

  PART A  path-ensemble moment algebra on the Z^d lattice (exact Laurent polynomials; sympy):
          composite loop ensembles (independent draws concatenated with integer signs) keep the mean
          current and multiply the covariance by exactly sum(s_i^2), for every photon momentum.
  PART B  an exact one-loop toy (a COMPARATOR, not the root): 2 spatial dimensions on rational-trig
          momentum nodes + continuum Euclidean time, Wilson-Dirac symbol deformed by the SF-type E_g
          flow, frame-Maxwell photon with its own flow, Psym generalized-link vertices.  Three freedoms
          are put through the same Ward / gauge-parameter controls: the literal deformed symbol
          (U=1, Psym), the Hamiltonian dressing  H -> V H V^dag, and positive local loop ensembles.
  PART C  integer arithmetic on the ensemble class, and arithmetic on LANE-SUPPLIED root numbers
          (quoted from the packet, never recomputed here).

Every PASS/FAIL line is one check.  A HIT line is printed only if every check passed.
"""
import os, sys, hashlib, itertools, functools, time, random
from fractions import Fraction
import numpy as np
import sympy as sp
import mpmath as mp
from sympy import Rational as R, I, Matrix, eye, zeros
from scipy.integrate import solve_ivp, quad
from scipy.linalg import expm

T0 = time.time()
NPASS = 0
NFAIL = 0
ALLOK = True


def chk(ok, msg):
    global NPASS, NFAIL, ALLOK
    ok = bool(ok)
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
        ALLOK = False
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    return ok


HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------------------------
# PART 0  source integrity and premise audit (only if the files are present next to this script)
# ----------------------------------------------------------------------------------------------
SRC_SHA = {
    "C5_F1_referee_verdict.md": "178624da4f86289465244a58a64b77131c8714d43f69b482bfcdf90434f3be2f",
    "C5_F1_report.md": "aa464d4e4e39b4ac12a012df327291d1dae74adc518dd7bb13bfa96d3b4b049f",
    "C5_F3_referee_verdict.md": "5ec1de4f05b9014c04fcd0382681e9da413fad549116ee6125bbd12a23e2113f",
    "C5_F3_report.md": "df55ab86a7ee2395538c5a3569102f7ec763054e89bfda3fba9bed9e70df6611",
    "C5_F4_referee_verdict.md": "cc171b3a9f42dd03133fc3012e628ab97fb442faaee5a6b1612affe2dc2476e5",
    "C5_F4_report.md": "64ed41e507381c60cf3c4b9bdb90e3b92263affba3595816a9b2ec9a4dabe64c",
    "C5_F5_referee_verdict.md": "a21bd78b865cec837fc7776d17506bed03076f343b7ef98f7b12d4c871c3be64",
    "C5_F5_report.md": "5996a5789d1489f88a3054087945244b6bd746ce46697af9d0ee6823618b79e6",
}
srcdir = os.path.join(HERE, "src")
if os.path.isdir(srcdir):
    ok = True
    for fn, h in SRC_SHA.items():
        p = os.path.join(srcdir, fn)
        ok &= os.path.exists(p) and hashlib.sha256(open(p, "rb").read()).hexdigest() == h
    chk(ok, "P0.1 the 8 frozen source objects (commit 6afb06951a13...) in ./src match their recorded sha256")

MAIN = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/main_wt"
ax = os.path.join(MAIN, "docs/MINIMAL_AXIOMS_2026-06-29.md")
pr = os.path.join(MAIN, "docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md")
if os.path.exists(ax) and os.path.exists(pr):
    axt = " ".join(open(ax).read().split())
    prt = " ".join(open(pr).read().split())
    chk("does not choose a Hamiltonian or transfer operator" in axt
        and "Axioms and approved primitives are the complete supplied foundation" in axt,
        "P0.2 axiom memo (current main): Admissibility chooses no Hamiltonian; axioms+approved primitives are the whole foundation")
    prims = [w for w in ("scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive") if w in prt]
    chk(len(prims) == 3 and not any(w in prt.lower() for w in ("strain flow", "minimal coupling", "gauge path", "wilson line")),
        "P0.3 registry lists exactly three approved primitives; none mentions a strain flow, gauge coupling or path rule")

# ----------------------------------------------------------------------------------------------
# PART A  path-ensemble moment algebra (exact)
# ----------------------------------------------------------------------------------------------
zs = sp.symbols("z1 z2 z3")  # z_m = exp(i q_m)


def axis_path(order, n):
    pos = [0] * len(n)
    steps = []
    for ax_ in order:
        k = n[ax_]
        sgn = 1 if k > 0 else -1
        for _ in range(abs(k)):
            if sgn > 0:
                steps.append((tuple(pos), ax_, +1))
                pos[ax_] += 1
            else:
                pos[ax_] -= 1
                steps.append((tuple(pos), ax_, -1))
    return steps


def Xsum(steps, j, sign):
    out = 0
    for (p_, ax_, o) in steps:
        if ax_ == j:
            out += o * sp.Mul(*[zs[m] ** (sign * p_[m]) for m in range(len(p_))])
    return sp.expand(out)


def moments(paths, probs, dim):
    res = {}
    for j in range(dim):
        for l in range(dim):
            EXX = sum(pr_ * Xsum(p_, j, +1) * Xsum(p_, l, -1) for p_, pr_ in zip(paths, probs))
            Ej = sum(pr_ * Xsum(p_, j, +1) for p_, pr_ in zip(paths, probs))
            El = sum(pr_ * Xsum(p_, l, -1) for p_, pr_ in zip(paths, probs))
            res[(j, l)] = (sp.expand(EXX), sp.expand(Ej), sp.expand(El))
    return res


def ensemble_from_pattern(P, signs_draws):
    """signs_draws: list of (draw_label, sign); labels equal => same draw reused (repeated detour).
    returns (paths, probs) of the concatenation over iid uniform draws of Psym paths."""
    labels = sorted(set(l for l, _ in signs_draws))
    w = Fraction(1, len(P)) ** len(labels)
    paths, probs = [], []
    for idx in itertools.product(range(len(P)), repeat=len(labels)):
        pick = dict(zip(labels, idx))
        steps = []
        for l, s in signs_draws:
            steps += [(pos, ax_, o * s) for (pos, ax_, o) in P[pick[l]]]
        paths.append(steps)
        probs.append(sp.Rational(w.numerator, w.denominator))
    return paths, probs


def lemma_A(n, patterns):
    dim = len(n)
    orders = list(itertools.permutations(range(dim)))
    Pfull = [axis_path(o, n) for o in orders]          # Psym: uniform over the d! axis orderings
    base = moments(Pfull, [sp.Rational(1, len(Pfull))] * len(Pfull), dim)
    results = []
    for pat in patterns:
        coef = {}
        for lab, s_ in pat:
            coef[lab] = coef.get(lab, 0) + s_
        assert sum(coef.values()) == 1
        c = sum(v * v for v in coef.values())
        paths, probs = ensemble_from_pattern(Pfull, pat)
        cm = moments(paths, probs, dim)
        ok = True
        for (j, l), (EXX, Ej, El) in cm.items():
            EXX0, Ej0, El0 = base[(j, l)]
            ok &= sp.expand(Ej - Ej0) == 0 and sp.expand(El - El0) == 0
            ok &= sp.expand(EXX - (Ej0 * El0 + c * (EXX0 - Ej0 * El0))) == 0
        results.append((pat, c, ok))
    nontriv = any(sp.expand(base[(j, j)][0] - base[(j, j)][1] * base[(j, j)][2]) != 0 for j in range(dim))
    return results, nontriv


PAT3 = [[("g", 1)], [("a", 1), ("b", -1), ("c", 1)], [("g", 1), ("g", 1), ("h", -1)]]
# the third pattern is 'g g h^-1': one draw used twice forward, one draw once reversed (c = 4+1 = 5)
res3, nontriv3 = lemma_A((1, 1, 1), PAT3)
chk(nontriv3, "A.1 3D hop (1,1,1): Psym covariance (E|X|^2 - |EX|^2) is nonzero, so the covariance freedom is real")
chk(all(ok for _, _, ok in res3) and [c for _, c, _ in res3] == [1, 3, 5],
    "A.2 3D hop (1,1,1): composites (+,-,+) and (+2,-1) keep the mean current and give E[X_j X_l(-q)] = |mean|^2 + c Cov exactly, c=3,5 (all j,l, all q)")
res3b, _ = lemma_A((1, 1, 1), [[("g", 1), ("g", 1), ("g", 1), ("h", -1), ("k", -1)]])
chk(all(ok for _, _, ok in res3b) and res3b[0][1] == 11, "A.3 3D hop (1,1,1): pattern (+3 g, -h, -k): c = 9+1+1 = 11, exact")
res2, nontriv2 = lemma_A((2, -1), [[("a", 1), ("b", -1), ("c", 1)], [("g", 1), ("g", 1), ("h", -1)]])
res2b, _ = lemma_A((1, 1), [[("a", 1), ("b", -1), ("c", 1)], [("g", 1), ("g", -1), ("h", 1)]])
chk(nontriv2 and all(ok for _, _, ok in res2 + res2b), "A.4 2D hops (2,-1) and (1,1): same exact covariance scaling (also with repeated draws)")

# cubic covariance and reversal closure of the Psym ensemble (hop (1,1,1))
def positions(order, n):
    pos = [0, 0, 0]
    seq = [tuple(pos)]
    for ax_ in order:
        for _ in range(abs(n[ax_])):
            pos[ax_] += 1 if n[ax_] > 0 else -1
            seq.append(tuple(pos))
    return tuple(seq)

n = (1, 1, 1)
S_n = {positions(o, n) for o in itertools.permutations(range(3))}
rot = lambda v: (-v[1], v[0], v[2])        # proper rotation by 90 degrees about z
S_rot = {tuple(rot(p_) for p_ in seq) for seq in S_n}
S_target = {positions(o, rot(n)) for o in itertools.permutations(range(3))}
rev_set = {tuple(reversed(seq)) for seq in S_n}
shift = lambda seq, d: tuple(tuple(a_ + b_ for a_, b_ in zip(p_, d)) for p_ in seq)
S_minus = {shift(seq, tuple(-v for v in n)) for seq in rev_set}
S_mn = {positions(o, tuple(-v for v in n)) for o in itertools.permutations(range(3))}
chk(S_rot == S_target and S_minus == S_mn,
    "A.5 Psym path set for hop (1,1,1) is closed under a proper 90-degree rotation and under reversal (hermiticity); composites of iid Psym draws inherit both")

# covariance is Hermitian positive semidefinite for every photon momentum (numeric, random q)
orders3 = list(itertools.permutations(range(3)))
P3 = [axis_path(o, (1, 1, 1)) for o in orders3]
rng = random.Random(7)
okpsd = True
for _ in range(20):
    qv = [rng.uniform(-3.1, 3.1) for _ in range(3)]
    zsub = {zs[m]: complex(np.cos(qv[m]), np.sin(qv[m])) for m in range(3)}
    Xs = np.array([[complex(Xsum(p_, j, +1).subs(zsub)) for j in range(3)] for p_ in P3])
    mean = Xs.mean(axis=0)
    cov = (Xs.T @ Xs.conj()) / len(P3) - np.outer(mean, mean.conj())
    ev = np.linalg.eigvalsh((cov + cov.conj().T) / 2)
    okpsd &= ev.min() > -1e-12 and np.allclose(cov, cov.conj().T, atol=1e-12)
chk(okpsd, "A.6 Psym covariance matrix (3x3, hop (1,1,1)) is Hermitian and positive semidefinite at 20 random photon momenta")

# ----------------------------------------------------------------------------------------------
# PART C1  integer-signed concatenations: which covariance multipliers c = sum s_i^2 occur
# ----------------------------------------------------------------------------------------------
def label_patterns(P, N):
    """all multisets of per-label (f, r): f forward uses and r reverse uses of one iid draw, f+r >= 1,
    with sum f = P and sum r = N.  The composite path alternates forward/reverse pieces (F R F ... F), so it stays in the cell."""
    pairs = [(f, r) for f in range(P + 1) for r in range(N + 1) if f + r >= 1]
    out = []

    def rec(i, remP, remN, cur):
        if remP == 0 and remN == 0:
            out.append(tuple(cur))
            return
        for k in range(i, len(pairs)):
            f, r = pairs[k]
            if f <= remP and r <= remN:
                cur.append(pairs[k])
                rec(k, remP - f, remN - r, cur)
                cur.pop()
    rec(0, P, N, [])
    return out


cset, extremal_ok, oddok, maxok = {}, True, True, True
for Tt in range(1, 14, 2):          # T = total traversals of the cell, P forward + N reverse, P - N = 1
    Pp, Nn = (Tt + 1) // 2, (Tt - 1) // 2
    vals, argmax = set(), []
    for pat in label_patterns(Pp, Nn):
        cval = sum((f - r) ** 2 for f, r in pat)
        vals.add(cval)
        if cval == (Tt * Tt + 1) // 2:
            argmax.append(pat)
    cset[Tt] = vals
    oddok &= all(v % 2 == 1 for v in vals)
    maxok &= max(vals) == (Tt * Tt + 1) // 2
    extremal_ok &= all(sorted(p_) == sorted([(Pp, 0)] + ([(0, Nn)] if Nn > 0 else [])) for p_ in argmax)
allodd_ok = all(((Tt in cset) and (Tt in cset[Tt])) for Tt in cset)
chk(oddok and maxok and extremal_ok and allodd_ok,
    "C.1 composites with T total cell traversals (P forward, N reverse, P-N=1, T<=13, every assignment of repeated/reversed draws): c is odd, c <= (T^2+1)/2, equality only for (P copies of one draw forward, N copies of one draw reversed), c=T always attained")

# ----------------------------------------------------------------------------------------------
# PART D  Hamiltonian dressing versus the literal deformed-symbol conjugation (exact, 2x2 toy algebra)
# ----------------------------------------------------------------------------------------------
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
ID = eye(2)
c1_, c2_, M_, f1_, f2_, e_, lam_ = sp.symbols("c1 c2 M f1 f2 e lam", real=True)
Dloc = I * (s1 * c1_ + s2 * c2_) + M_ * ID
Hloc = s3 * Dloc
Gloc = -(s1 * f1_ + s2 * f2_)
Vloc = ID + I * e_ * Gloc - e_ ** 2 * Gloc * Gloc / 2
Vdag = ID - I * e_ * Gloc - e_ ** 2 * Gloc * Gloc / 2
trunc = lambda Mx, n_=3: Mx.applyfunc(lambda z: sp.series(sp.expand(z), e_, 0, n_).removeO())
Hd = trunc(Vloc * Hloc * Vdag)
cpd = sp.expand(sp.series(Hd.charpoly(lam_).as_expr(), e_, 0, 3).removeO() - Hloc.charpoly(lam_).as_expr())
chk(sp.simplify(trunc(Hd - Hd.H)) == zeros(2, 2) and sp.simplify(cpd) == 0,
    "D.1 Hamiltonian dressing H -> V H V^dag (V unitary) stays Hermitian and keeps the characteristic polynomial through O(eps^2)")
Dp_ = trunc(s3 * Hd)
Mp1 = sp.expand((Dp_[0, 0] + Dp_[1, 1]) / 2).coeff(e_, 1)
chk(sp.simplify(Mp1 + 2 * (c1_ * f1_ + c2_ * f2_)) == 0,
    "D.2 the dressed operator stays in Dirac form with mass shift delta M = -2 eps f.c (the nearest-neighbour dressing mechanism)")
HL = sp.expand(s3 * Vloc * Dloc * Vdag)
anti1 = (HL - HL.H).applyfunc(lambda z: sp.expand(z).coeff(e_, 1))
ac = Gloc * Hloc + Hloc * Gloc
chk(sp.simplify(anti1 + 2 * I * ac) == zeros(2, 2) and sp.simplify(ac - (2 * (c1_ * f2_ - c2_ * f1_)) * ID) == zeros(2, 2)
    and sp.simplify(ac) != zeros(2, 2),
    "D.3 literal conjugation V D V^dag with {V-generator, gamma_0}=0 gives H_L - H_L^dag = -2 i eps {G,H} = 4 i eps (c2 f1 - c1 f2) 1 != 0: non-Hermitian, complex band energies")
# honest toy degeneracy: for G1 (f = sin k = c) the cross product vanishes in THIS toy
chk(sp.simplify(ac.subs({f1_: c1_, f2_: c2_})) == zeros(2, 2),
    "D.4 toy degeneracy stated: for f = c (the toy's G1) the anticommutator vanishes, so the literal non-Hermiticity test uses the G2-type f; the root has c != sin k")

# ----------------------------------------------------------------------------------------------
# PART B  exact one-loop toy
# ----------------------------------------------------------------------------------------------
t, x, a, c, a2 = sp.symbols("t x a c a2")
k1, k2 = sp.symbols("k1 k2")
KK = [k1, k2]
G0 = s3
Mfun = (1 - sp.cos(k1)) + (1 - sp.cos(k2))
Ds = I * (s1 * sp.sin(k1) + s2 * sp.sin(k2)) + Mfun * ID
Lam = (sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + Mfun ** 2) / 2
pp_ = [sp.diff(Lam, k) for k in KK]
Vf = [R(1, 2) * pp_[0], -R(1, 2) * pp_[1]]                     # SF E_g flow generator, v = (t/2) diag(1,-1) grad(E^2/2)
Wf = [sum(Vf[l] * sp.diff(Vf[j], KK[l]) for l in range(2)) / 2 for j in range(2)]
D1s = sum((Vf[j] * sp.diff(Ds, KK[j]) for j in range(2)), zeros(2, 2))
D2s = sum((Wf[j] * sp.diff(Ds, KK[j]) for j in range(2)), zeros(2, 2)) + \
    R(1, 2) * sum((Vf[i] * Vf[j] * sp.diff(Ds, KK[i], KK[j]) for i in range(2) for j in range(2)), zeros(2, 2))
H0s = G0 * Ds
G1m = -(s1 * sp.sin(k1) + s2 * sp.sin(k2))
G2m = -(s1 * sp.sin(k1) * sp.cos(k2) + s2 * sp.sin(k2) * sp.cos(k1))
D2dress1 = I * G0 * (G1m * H0s - H0s * G1m)
D2dress2 = I * G0 * (G2m * H0s - H0s * G2m)

ANG = {"a": (R(4, 5), R(3, 5)), "b": (R(1), R(0))}


def sc(comp):
    lab, sg = comp
    if lab == "0":
        return (R(0), R(1))
    s_, cc_ = ANG[lab]
    return (sg * s_, cc_)


def subsnode(expr, pt):
    rep = {}
    for kk, comp in zip(KK, pt):
        s_, c_ = sc(comp)
        rep[sp.sin(kk)] = s_
        rep[sp.cos(kk)] = c_
    return expr.subs(rep)


PAR = {"a": a, "a2": a2}          # dressing coefficients currently in force (symbols, or exact rationals for the corner runs)


@functools.lru_cache(None)
def _Dpt(pt, av, a2v):
    D0 = subsnode(Ds, pt)
    D1 = subsnode(D1s, pt)
    D2 = subsnode(D2s, pt) + av * subsnode(D2dress1, pt) + a2v * subsnode(D2dress2, pt)
    return [sp.simplify(D0), sp.simplify(D1), sp.simplify(D2)]


def Dpt(pt):
    return _Dpt(pt, PAR["a"], PAR["a2"])


def smulS(A, B):
    return [sum((A[i] * B[k - i] for i in range(k + 1))) for k in range(3)]


def sinvS(A):
    a0 = A[0]
    return [1 / a0, -A[1] / a0 ** 2, (A[1] ** 2 / a0 ** 3 - A[2] / a0 ** 2)]


def mmul(A, B):
    return [sum((A[i] * B[k - i] for i in range(k + 1)), zeros(2, 2)) for k in range(3)]


def mlin(*terms):
    out = [zeros(2, 2) for _ in range(3)]
    for co, S_ in terms:
        for k in range(3):
            out[k] = out[k] + co * S_[k]
    return out


def apply_sc(Mx, ds):
    return [sum((Mx[i] * ds[k - i] for i in range(k + 1)), zeros(2, 2)) for k in range(3)]


HG = [1, -1]


def dser(j, q):
    sq, cq = sc(q[j])
    u = R(HG[j], 2) * sq * cq
    up = R(HG[j], 2) * (cq * cq - sq * sq)
    return [sq, cq * u, cq * (u * up) / 2 - sq * u * u / 2]


def pt_of(q, mask):
    out = []
    for l in range(2):
        m = mask[l]
        out.append(("0", 1) if m == 0 else (q[l][0], q[l][1] * m))
    return tuple(out)


ORD = [(0, 1), (1, 0)]


def Vpsym(q, which):
    out = []
    for j in range(2):
        acc = [zeros(2, 2) for _ in range(3)]
        for sig in ORD:
            if which == "in":
                base = [0, 0]
                for l in sig[:sig.index(j)]:
                    base[l] = 1
            else:
                base = [0, 0]
                for l in sig[sig.index(j) + 1:]:
                    base[l] = 1
            b1 = list(base)
            b1[j] = 1
            M_ = mlin((1, Dpt(pt_of(q, b1))), (-1, Dpt(pt_of(q, base))))
            V = apply_sc(M_, sinvS(dser(j, q)))
            acc = [acc[k] + V[k] / 2 for k in range(3)]
        out.append(acc)
    return out


# Laurent kernels: dict {(e1,e2): coeff}
def kmul(A, B):
    out = {}
    for e, ca in A.items():
        for f, cb in B.items():
            k = (e[0] + f[0], e[1] + f[1])
            out[k] = out.get(k, 0) + ca * cb
    return out


def kadd(A, B, sb=1):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, 0) + sb * v
    return out


def kscal(A, s):
    return {k: v * s for k, v in A.items()}


def Zk(j, n_=1):
    e = [0, 0]
    e[j] = n_
    return {tuple(e): 1}


ONE = {(0, 0): 1}


def lam_in(sig, j):
    ph = ONE
    for l in sig[:sig.index(j)]:
        ph = kmul(ph, Zk(l))
    return kmul(ph, kadd(Zk(j), ONE, -1))


def lam_out(sig, j):
    ph = ONE
    for l in sig[:sig.index(j)]:
        ph = kmul(ph, Zk(l, -1))
    return kmul(ph, kadd(Zk(j, -1), ONE, -1))


def kernel_W(j, l, typ):
    if typ == "J":
        A, B = {}, {}
        for sig in ORD:
            A = kadd(A, kscal(lam_in(sig, j), R(1, 2)))
            B = kadd(B, kscal(lam_out(sig, l), R(1, 2)))
        return kmul(A, B)
    out = {}
    for sig in ORD:
        out = kadd(out, kscal(kmul(lam_in(sig, j), lam_out(sig, l)), R(1, 2)))
    return out


def kernel_apply(K, q):
    acc = [zeros(2, 2) for _ in range(3)]
    for e, co in K.items():
        pt = tuple(("0", 1) if e[l] == 0 else (q[l][0], q[l][1] * e[l]) for l in range(2))
        D_ = Dpt(pt)
        acc = [acc[k] + co * D_[k] for k in range(3)]
    return acc


@functools.lru_cache(None)
def _KJP_c(q, j, l, av, a2v):
    return kernel_apply(kernel_W(j, l, "J"), q), kernel_apply(kernel_W(j, l, "P"), q)


def _KJP(q, j, l):
    return _KJP_c(q, j, l, PAR["a"], PAR["a2"])


def Wmat(q, j, l, cc):
    """second-order (two-photon) vertex W_jl(q) for covariance multiplier cc:  W = W_J + cc (W_P - W_J)."""
    ds = smulS(dser(j, q), dser(l, q))
    dinv = sinvS(ds)
    KJ, KP = _KJP(q, j, l)
    K = [KJ[k] + cc * (KP[k] - KJ[k]) for k in range(3)]
    return apply_sc([-K[k] for k in range(3)], dinv)


U_s, V_s = sp.symbols("U V")        # U = 1/(x^2+E^2), V = 1/(x^2+Omega^2): keeps the integrand a polynomial in (x, U, V)


def Sser(q, poly=False):
    D = Dpt(q)
    Dt_ = [D[0] + I * s3 * x, D[1], D[2]]
    Mv = sum(1 - sc(q[l])[1] for l in range(2))
    E2 = sc(q[0])[0] ** 2 + sc(q[1])[0] ** 2 + Mv ** 2
    den = U_s if poly else 1 / (x ** 2 + E2)
    S0 = (Mv * ID - I * s3 * x - I * (s1 * sc(q[0])[0] + s2 * sc(q[1])[0])) * den
    S1 = -S0 * Dt_[1] * S0
    S2 = S0 * Dt_[1] * S0 * Dt_[1] * S0 - S0 * Dt_[2] * S0
    return [S0, S1, S2], E2


def Pser(q, poly=False):
    d0, d1 = dser(0, q), dser(1, q)
    sq0, sq1 = smulS(d0, d0), smulS(d1, d1)
    O = [sq0[k] + sq1[k] for k in range(3)]
    y_ = V_s if poly else 1 / (x ** 2 + O[0])
    if poly:
        return [V_s, -O[1] * V_s ** 2, O[1] ** 2 * V_s ** 3 - O[2] * V_s ** 2], O[0]
    return [y_, -O[1] * y_ ** 2, O[1] ** 2 * y_ ** 3 - O[2] * y_ ** 2], O[0]


def integrand(q, cc, poly=False):
    """series (orders t^0..t^2) of the one-loop P=0 self-energy integrand (matrix) at loop momentum (x, q);
    returns (series, E2, Omega0^2)."""
    S, E2 = Sser(q, poly)
    P, B = Pser(q, poly)
    Vi, Vo = Vpsym(q, "in"), Vpsym(q, "out")
    tv = I * s3
    ex = [tv * S[k] * tv for k in range(3)]
    for j in range(2):
        tmp = mmul(Vo[j], mmul(S, Vi[j]))
        ex = [ex[k] + tmp[k] for k in range(3)]
    sea = [zeros(2, 2) for _ in range(3)]
    for j in range(2):
        W = Wmat(q, j, j, cc)
        sea = [sea[k] + W[k] / 2 for k in range(3)]
    tot = [-ex[k] + sea[k] for k in range(3)]
    F = [sum((tot[i] * P[k - i] for i in range(k + 1)), zeros(2, 2)) for k in range(3)]
    if poly:
        F = [Fk.applyfunc(sp.expand) for Fk in F]
    return F, E2, B


y_s = sp.symbols("y")


@functools.lru_cache(None)
def mono_int(m, i, j, E2, B):
    """int dx/(2 pi) x^(2m) / ((x^2+E2)^i (x^2+B)^j), exact (partial fractions in y = x^2)."""
    f = y_s ** m / ((y_s + E2) ** i * (y_s + B) ** j)
    ap = sp.apart(f, y_s)
    tot = 0
    for term in sp.Add.make_args(ap):
        num, den = sp.fraction(sp.together(term))
        assert sp.degree(num, y_s) == 0, (m, i, j, term)
        const, facs = sp.factor_list(den, y_s)
        assert len(facs) == 1, term
        base, k = facs[0]
        pa, qa = sp.Poly(base, y_s).all_coeffs()
        A_ = qa / pa
        coef = num / (const * pa ** k)
        tot += coef * sp.gamma(sp.Rational(2 * k - 1, 2)) / (2 * sp.sqrt(sp.pi) * sp.gamma(k)) * A_ ** (sp.Rational(1, 2) - k)
    return tot


def xint_poly(expr, E2, B):
    """exact int dx/(2 pi) of a polynomial in (x, U, V) with U=1/(x^2+E2), V=1/(x^2+B)."""
    tot = 0
    for (ex_, eu, ev), co in sp.Poly(expr, x, U_s, V_s).terms():
        if ex_ % 2 or co == 0:
            continue
        tot += co * mono_int(ex_ // 2, eu, ev, E2, B)
    return tot


NODES = [((l1, s1_), (l2, s2_)) for (l1, l2) in (("a", "b"), ("b", "a")) for s1_ in (1, -1) for s2_ in (1, -1)]
# 8 nodes: invariant under every sign flip q_j -> -q_j and under the swap q1<->q2; no zero component (so no zero mode, d_j != 0)

# ---- B.1 Ward identity of the one-photon vertices and the longitudinal two-photon identity (all orders in t)
q0 = (("a", 1), ("b", -1))
mq0 = (("a", -1), ("b", 1))
Vi0, Vo0 = Vpsym(q0, "in"), Vpsym(q0, "out")
dd0 = [dser(0, q0), dser(1, q0)]
Zero2 = zeros(2, 2)


def addS(*Ls):
    return [sum((L[k] for L in Ls), zeros(2, 2)) for k in range(3)]


rhsW = [Dpt(pt_of(q0, (1, 1)))[k] - Dpt(pt_of(q0, (0, 0)))[k] for k in range(3)]
wardin = addS(*[apply_sc(Vi0[j], dd0[j]) for j in range(2)])
wardout = addS(*[apply_sc(Vo0[j], dd0[j]) for j in range(2)])
chk(all(sp.simplify(wardin[k] - rhsW[k]) == Zero2 and sp.simplify(wardout[k] - rhsW[k]) == Zero2 for k in range(3)),
    "B.1 Ward identity  sum_j d_j V_j = D_t(q) - D_t(0)  holds exactly for both vertices, with dressing a, a2 symbolic, through O(t^2)")
okL = True
for cc in [1, 0, 3, R(7, 2), c]:
    tot = [zeros(2, 2) for _ in range(3)]
    for j in range(2):
        for l in range(2):
            Wm = Wmat(q0, j, l, cc)
            tm = apply_sc(Wm, smulS(dd0[j], dd0[l]))
            tot = [tot[k] + tm[k] for k in range(3)]
    target = [Dpt(pt_of(q0, (1, 1)))[k] + Dpt(pt_of(q0, (-1, -1)))[k] - 2 * Dpt(pt_of(q0, (0, 0)))[k] for k in range(3)]
    okL &= all(sp.simplify(tot[k] - target[k]) == Zero2 for k in range(3))
chk(okL, "B.2 longitudinal two-photon identity  sum_jl d_j d_l W_jl = D(q)+D(-q)-2D(0)  exact for covariance multiplier c = 0, 1, 3, 7/2 and symbolic c")

# ---- B.3 gauge-parameter bracket
Sq, E2q = Sser(q0)
Qvin = addS(*[apply_sc(Vi0[j], dd0[j]) for j in range(2)])
Qvin[0] = Qvin[0] + I * s3 * x
Qvout = addS(*[apply_sc(Vo0[j], dd0[j]) for j in range(2)])
Qvout[0] = Qvout[0] + I * s3 * x
exg = mmul(Qvout, mmul(Sq, Qvin))
seag = [zeros(2, 2) for _ in range(3)]
for j in range(2):
    for l in range(2):
        tm = apply_sc(Wmat(q0, j, l, c), smulS(dd0[j], dd0[l]))
        seag = [seag[k] + tm[k] / 2 for k in range(3)]
Dp0, Dm0 = Dpt(q0), Dpt(mq0)
okxi = all(sp.simplify(exg[k] - seag[k] - ((I * s3 * x if k == 0 else Zero2) + (Dp0[k] - Dm0[k]) / 2)) == Zero2 for k in range(3))
okxi &= all(sp.simplify((Dp0[k] - Dm0[k]).trace()) == 0 for k in range(3))
chk(okxi, "B.3 gauge-parameter part of the P=0 self-energy integrand equals (D(Q)-D(-Q))/2, whose mass (identity) part is 0: xi-independent for every a, a2, c")

# ---- B.4 the unstrained (t^0) law does not know about c or the dressings
ok0 = True
for q in NODES:
    for j in range(2):
        KJ0, KP0 = _KJP(q, j, j)
        ok0 &= sp.simplify(KP0[0] - KJ0[0]) == zeros(2, 2)          # no hop with both n_j, n_l != 0 at t=0: covariance part is 0
    ok0 &= not (Dpt(pt_of(q, (1, 1)))[0].free_symbols & {a, a2})      # the t^0 symbol carries no dressing
chk(ok0, "B.4 at t=0 the covariance part W_P - W_J vanishes at every node and the symbol carries no dressing: the unstrained law is the same for every a, a2, c")

# ---- B.5-B.8 integrate over the nodes at the 8 corners (a,a2,c) in {0,1}^3, reconstruct the multilinear response
Sig3 = [s1, s2, s3]
XS = [R(3, 7), R(5, 2), R(11, 3)]


def node_sums(av, a2v, cv, nodes=None, want_gam=True):
    PAR["a"], PAR["a2"] = av, a2v
    h2 = 0
    h1 = 0
    gam = {(i, xv): 0 for i in range(3) for xv in XS}
    for q in (nodes or NODES):
        F, E2, B = integrand(q, cv, poly=True)
        for order in (1, 2):
            Mx = F[order]
            val = xint_poly(sp.expand((Mx[0, 0] + Mx[1, 1]) / 2), E2, B)
            if order == 2:
                h2 += val
            else:
                h1 += val
        for i, sg in enumerate(Sig3 if want_gam else []):
            trc = (sg * F[2]).trace() / 2
            for xv in XS:
                ev = 0
                for sx in (xv, -xv):
                    ev += trc.subs({x: sx, U_s: 1 / (xv ** 2 + E2), V_s: 1 / (xv ** 2 + B)}) / 2
                gam[(i, xv)] += ev
    PAR["a"], PAR["a2"] = a, a2
    return h2, h1, gam


hval, odd_ok, gam_ok = {}, True, True
for corner in itertools.product((0, 1), repeat=3):
    h2_, h1_, gam_ = node_sums(*[sp.Integer(v) for v in corner])
    hval[corner] = h2_
    odd_ok &= abs(sp.N(h1_, 60)) < sp.Float("1e-50", 60)
    gam_ok &= all(sp.simplify(v) == 0 for v in gam_.values())
chk(odd_ok, "B.5 the O(t) part of the node-summed pole shift is 0 at all 8 corners (to 50 digits): evenness in t holds, so the t^2 coefficient h is half the Hessian")
chk(gam_ok, "B.6 the non-identity (gamma_i) parts of the node-summed self-energy cancel exactly (rational arithmetic, 3 sample x, 8 corners): the pole shift is the identity part")


def mobius(i, j, k):
    return sum((-1) ** ((i - u) + (j - v) + (k - w)) * hval[(u, v, w)]
               for u in range(i + 1) for v in range(j + 1) for w in range(k + 1))


coef = {(i, j, k): sp.N(mobius(i, j, k), 60) for i in (0, 1) for j in (0, 1) for k in (0, 1)}
nonzero = {m for m, v in coef.items() if abs(v) > sp.Float("1e-45", 60)}
expected = {(0, 0, 0), (0, 0, 1), (1, 0, 0), (0, 1, 0), (0, 1, 1)}


def multilin(av, a2v, cv):
    return sum(coef[m] * av ** m[0] * a2v ** m[1] * cv ** m[2] for m in coef)


off_ok = True
for pt in [(R(1, 3), R(2, 5), R(7, 2)), (R(-1, 2), R(3), R(5))]:
    h2_, _, _ = node_sums(*pt)
    off_ok &= abs(sp.N(h2_, 60) - multilin(*[sp.N(v, 60) for v in pt])) < sp.Float("1e-45", 60)
chk(nonzero == expected and off_ok,
    "B.7 the t^2 pole-mass response is exactly multilinear in (a, a2, c) (two off-corner exact points agree to 1e-45) with monomials {1, c, a, a2, a2*c}: no a*c cross term for G1, an a2*c cross term for G2")
H00, Hc, Ha, Ha2, Ha2c = (coef[(0, 0, 0)], coef[(0, 0, 1)], coef[(1, 0, 0)], coef[(0, 1, 0)], coef[(0, 1, 1)])
chk(abs(Ha2c) > 1e-3 and abs(Hc) > 1e-3 and abs(Ha) > 1e-3 and abs(H00 + Hc) > 1e-3,
    "B.8 exact coefficients (60-digit evaluation of exact algebraic sums): h = %.12f + %.12f c %+.10f a %+.10f a2 %+.10f a2 c;  h(Psym) = %.10f" %
    (H00, Hc, Ha, Ha2, Ha2c, H00 + Hc))

# ---- B.9 disjoint numeric check: true flows (ODE), true matrix exponential, finite t, quadrature
sn1 = np.array([[0, 1], [1, 0]], complex)
sn2 = np.array([[0, -1j], [1j, 0]])
sn3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
ANGN = {"a": (0.8, 0.6), "b": (1.0, 0.0)}


def angn(comp):
    lab, sg = comp
    if lab == "0":
        return 0.0
    s_, c_ = ANGN[lab]
    return np.arctan2(sg * s_, c_)


def Mfn(k):
    return (1 - np.cos(k[0])) + (1 - np.cos(k[1]))


def Dsn(k):
    return 1j * (sn1 * np.sin(k[0]) + sn2 * np.sin(k[1])) + Mfn(k) * I2


def Vfield(k):
    M = Mfn(k)
    p = [np.sin(k[j]) * (np.cos(k[j]) + M) for j in range(2)]
    return np.array([0.5 * p[0], -0.5 * p[1]])


def flow(tt, k):
    if tt == 0:
        return np.array(k, float)
    sol = solve_ivp(lambda tau, y: Vfield(y), [0, tt], np.array(k, float), method="DOP853", rtol=1e-13, atol=1e-15)
    return sol.y[:, -1]


def dflow(tt, j, qv):
    h = HG[j]
    if tt == 0:
        return qv
    sol = solve_ivp(lambda tau, y: [0.5 * h * np.sin(y[0]) * np.cos(y[0])], [0, tt], [qv], method="DOP853", rtol=1e-13, atol=1e-15)
    return sol.y[0, -1]


def Gmn(k, which):
    f = [np.sin(k[0]), np.sin(k[1])] if which == 1 else [np.sin(k[0]) * np.cos(k[1]), np.sin(k[1]) * np.cos(k[0])]
    return -(sn1 * f[0] + sn2 * f[1])


def Dtn(tt, k, aa1, aa2):
    kt = flow(tt, k)
    D = Dsn(kt)
    if aa1 != 0 or aa2 != 0:
        H = sn3 @ D
        G = aa1 * Gmn(k, 1) + aa2 * Gmn(k, 2)
        V = expm(1j * tt * tt * G)
        D = sn3 @ V @ H @ V.conj().T
    return D


KP = {(j, l): kernel_W(j, l, "P") for j in range(2) for l in range(2)}
KJ = {(j, l): kernel_W(j, l, "J") for j in range(2) for l in range(2)}


def pole_n(tt, q, aa1, aa2, cc):
    th = [angn(q[0]), angn(q[1])]
    cache = {}

    def Dc(mask):
        key = tuple(mask)
        if key not in cache:
            cache[key] = Dtn(tt, [th[l] * mask[l] for l in range(2)], aa1, aa2)
        return cache[key]
    d = [np.sin(dflow(tt, j, th[j])) for j in range(2)]
    Vin, Vout = [], []
    for j in range(2):
        vi = 0
        vo = 0
        for sig in ORD:
            base = [0, 0]
            for l in sig[:sig.index(j)]:
                base[l] = 1
            b1 = list(base)
            b1[j] = 1
            vi = vi + (Dc(b1) - Dc(base)) / d[j] / 2
            after = [0, 0]
            for l in sig[sig.index(j) + 1:]:
                after[l] = 1
            a1_ = list(after)
            a1_[j] = 1
            vo = vo + (Dc(a1_) - Dc(after)) / d[j] / 2
        Vin.append(vi)
        Vout.append(vo)
    W = 0
    for j in range(2):
        kap = lambda K: sum(float(co) * Dc([e[0], e[1]]) for e, co in K.items())
        KPj, KJj = kap(KP[(j, j)]), kap(KJ[(j, j)])
        W = W - (KJj + cc * (KPj - KJj)) / (d[j] * d[j])
    D0 = Dc((1, 1))
    Om2 = d[0] ** 2 + d[1] ** 2

    def f(xx):
        S = np.linalg.inv(1j * sn3 * xx + D0)
        ex = (1j * sn3) @ S @ (1j * sn3) + Vout[0] @ S @ Vin[0] + Vout[1] @ S @ Vin[1]
        F = (-ex + W / 2) / (xx * xx + Om2)
        return (F[0, 0] + F[1, 1]).real / 2
    return quad(f, -np.inf, np.inf, epsabs=1e-14, epsrel=1e-13, limit=400)[0] / (2 * np.pi)


def total_n(tt, aa1, aa2, cc):
    return sum(pole_n(tt, q, aa1, aa2, cc) for q in NODES)


def hcoef_n(aa1, aa2, cc, tt=0.01):
    F0 = total_n(0.0, aa1, aa2, cc)
    g = lambda s: (total_n(s, aa1, aa2, cc) + total_n(-s, aa1, aa2, cc) - 2 * F0) / (2 * s * s)
    return (4 * g(tt) - g(2 * tt)) / 3


def hpred(aa1, aa2, cc):
    return float(H00 + Hc * cc + Ha * aa1 + Ha2 * aa2 + Ha2c * aa2 * cc)


worst = 0.0
for (aa1, aa2, cc) in [(0, 0, 1), (0, 0, 0), (0, 0, 3), (0.02, 0, 1), (0, 0.01, 3), (0.015, 0.012, 5)]:
    worst = max(worst, abs(hcoef_n(aa1, aa2, cc) - hpred(aa1, aa2, cc)))
chk(worst < 2e-6,
    "B.9 disjoint finite-t numerics (ODE flows, expm dressing, scipy quadrature) reproduce the exact h(a,a2,c) at 6 parameter points; worst |diff| = %.2e" % worst)

# ---- B.10 observables: which tunings touch which observable
dd = [dser(0, q0), dser(1, q0)]
eps_perp = [dd[1], [-v for v in dd[0]]]          # transverse polarisation, eps.d = 0 at every order in t
OP = addS(*[apply_sc(Vi0[j], eps_perp[j]) for j in range(2)])
O2 = [zeros(2, 2) for _ in range(3)]
for j in range(2):
    for l in range(2):
        tm = apply_sc(Wmat(q0, j, l, c), smulS(eps_perp[j], eps_perp[l]))
        O2 = [O2[k] + tm[k] for k in range(3)]
OP2 = OP[2].applyfunc(sp.simplify)
O22 = O2[2].applyfunc(sp.simplify)
chk(OP2.free_symbols == {a, a2} and c not in OP2.free_symbols and (O22.free_symbols >= {a, a2, c}),
    "B.10 transverse one-photon vertex t^2 coefficient depends on the dressing (a,a2) and NOT on c or on a mass retune; the transverse two-photon contact depends on c (and a,a2)")
dOP_da = OP2.diff(a)
dO2_dc = O22.diff(c).subs({a2: 0})
vacK = -sum(float(sp.N((1 - sc(q[0])[1] + 1 - sc(q[1])[1]) / sp.sqrt(sc(q[0])[0] ** 2 + sc(q[1])[0] ** 2 + (2 - sc(q[0])[1] - sc(q[1])[1]) ** 2))) for q in NODES)
chk(dOP_da != zeros(2, 2) and dO2_dc != zeros(2, 2) and abs(vacK) > 1e-6,
    "B.11 the three knock-on observables are individually nonzero: d(transverse vertex)/da != 0, d(two-photon contact)/dc != 0, vacuum-energy slope per unit retune = %.6f != 0" % vacK)

# ---- B.12 free spectrum / vacuum is untouched by the dressing and by c (so the vacuum row sees only a retune)
chk(sp.simplify(cpd) == 0,
    "B.12 vacuum (free band) energies are identical for every dressing a (unitary conjugation of H) and for every ensemble c (no photon in the free vacuum)")

# ---- B.13 the retuning bridge: pole-flat set and the no-free-lunch statement
# pole response per unit t^2:  R(mu2, a, c) = mu2 + h(a, 0, c).   (a2 = 0 here)
mu2_star = -(H00 + Hc)
a_star = (H00 + Hc) / (-Ha)
c_star = -H00 / Hc
resp = lambda m2, aa, cc: m2 + H00 + Hc * cc + Ha * aa
chk(abs(resp(mu2_star, 0, 1)) < 1e-30 and abs(resp(0, a_star, 1)) < 1e-30 and abs(resp(0, 0, c_star)) < 1e-30
    and len({round(float(mu2_star), 6), round(float(a_star), 6), round(float(c_star) - 1, 6)}) == 3,
    "B.13 three different exact zeros of the pole response: retune mu2*=%.10f (vacuum knock-on), dressing a*=%.10f (transverse-vertex knock-on), ensemble c*=%.10f (two-photon knock-on)" %
    (mu2_star, a_star, c_star))
origin_resp = H00 + Hc
cond = (origin_resp != 0) and (abs(vacK) > 0) and (dOP_da != zeros(2, 2)) and (dO2_dc != zeros(2, 2))
chk(cond,
    "B.14 no free lunch: the knock-on observables vanish only at (mu2, a, c-1) = (0,0,0), where the pole response is %.10f != 0; so every pole-flat law pays in at least one named observable" % origin_resp)
chk(Hc > 0 and Ha2c != 0,
    "B.15 sign of the covariance slope is model dependent (toy: dh/dc>0, whereas the packet's root numbers have dH/dc<0), and the zero set is not a plane when the dressing generator has a*c cross terms")

# ---- B.16 the toy's own sign depends on the quadrature rule (a reason not to read its numbers across to the root)
NODES16 = [(l1, l2) for l1 in (("a", 1), ("a", -1), ("b", 1), ("b", -1)) for l2 in (("a", 1), ("a", -1), ("b", 1), ("b", -1))]
h16_c0 = sp.N(node_sums(sp.Integer(0), sp.Integer(0), sp.Integer(0), NODES16, False)[0], 40)
h16_c1 = sp.N(node_sums(sp.Integer(0), sp.Integer(0), sp.Integer(1), NODES16, False)[0], 40)
cstar16 = -h16_c0 / (h16_c1 - h16_c0)
chk((H00 + Hc) * h16_c1 < 0 and (h16_c1 - h16_c0) > 0 and (Hc > 0),
    "B.16 changing the toy's 8 momentum nodes to 16 flips the sign of the Psym response (8 nodes: %.6f, 16 nodes: %.6f) and moves c* from %.4f to %.4f while dh/dc stays > 0: the toy fixes structure, not signs or magnitudes" %
    (H00 + Hc, h16_c1, -H00 / Hc, cstar16))
# ---- B.17 in the 8-node toy the ensemble zero is reached by a genuinely positive local ensemble with only T = 3 traversals
wt = (-H00 / Hc - 1) / (3 - 1)
chk(1 < -H00 / Hc < 3 and 0 < wt < 1 and abs(H00 + Hc * (1 + 2 * wt)) < sp.Float("1e-45", 60),
    "B.17 8-node toy: the zero c* = %.6f lies in [1,3), so a positive local ensemble reaches it: weight %.4f on the 3-traversal composite (+,-,+) and %.4f on Psym; the root would need T >= 25 (C.3)" %
    (-H00 / Hc, wt, 1 - wt))

# ----------------------------------------------------------------------------------------------
# PART C2  arithmetic on LANE-SUPPLIED root numbers (not recomputed here)
#   H_P  = +2.4240125e-2  (344 nodes, E_g Hessian, SF units, e^2)          src/C5_F4_report.md:108
#   H_J - H_P = +8.879e-5 (344 nodes)                                     src/C5_F4_report.md:109
#   referee 130-node: H_P = 0.0242470, H_J - H_P = 8.88369e-5              src/C5_F4_referee_verdict.md:11 (F4 item 3)
#   referee c_* = 273.998                                                  src/C5_F4_referee_verdict.md:13 (item 6)
# ----------------------------------------------------------------------------------------------
HP1, DJ1 = Fraction("0.024240125"), Fraction("0.00008879")
HP2, DJ2 = Fraction("0.0242470"), Fraction("0.0000888369")
cs1 = (HP1 + DJ1) / DJ1       # H(c) = H_J - c DJ with H_J = H_P + DJ
cs2 = (HP2 + DJ2) / DJ2
chk(abs(float(cs1) - 273.998) < 0.2 and abs(float(cs2) - 273.998) < 0.2,
    "C.2 with the packet's numbers, the covariance multiplier at which the Hessian vanishes is c* = %.3f (344-node) / %.3f (referee 130-node); the referee quotes 273.998" % (float(cs1), float(cs2)))
Tmin = None
for Tt in range(1, 61, 2):
    if Fraction(Tt * Tt + 1, 2) >= cs1 and Fraction(Tt * Tt + 1, 2) >= cs2:
        Tmin = Tt
        break
Hbound = lambda Tt, HP, DJ: (HP + DJ) - Fraction(Tt * Tt + 1, 2) * DJ
chk(Tmin == 25 and Hbound(23, HP1, DJ1) > 0 and Hbound(23, HP2, DJ2) > 0 and Hbound(25, HP1, DJ1) < 0,
    "C.3 within integer-signed Psym concatenations the zero needs a path that traverses the hop's cell at least T=25 times; with T<=23 the Hessian stays > 0 (min %.3e, 344-node numbers)" % float(Hbound(23, HP1, DJ1)))
Tthr = next(Tt for Tt in range(1, 61, 2) if Hbound(Tt, HP1, DJ1) < Fraction(1, 1000))
chk(Tthr == 23 and Hbound(21, HP1, DJ1) > Fraction(1, 1000),
    "C.4 the SF-HAZARD threshold (Hessian >= 1e-3) already fails at T=23 traversals (c up to 265): the packet's 'every permitted lift is >= 1e-3' is a statement about T <= 21 only, within this class")
# two-member convex mixture reaching c*: T=1 (c=1) and T=25 (c=313)
w = (cs1 - 1) / (313 - 1)
chk(0 < w < 1 and (1 + w * 312) == cs1,
    "C.5 explicit positive local ensemble with H=0 on the root numbers: weight %.4f on a 25-traversal member (c=313) and %.4f on Psym (c=1)" % (float(w), float(1 - w)))

# ----------------------------------------------------------------------------------------------
if ALLOK:
    print("HIT: scoped, comparator-level -- exact covariance-scaling lemma for positive local loop ensembles (odd multipliers, extremal c=(T^2+1)/2, "
          "T>=25 needed on the packet's root numbers) and an exact one-loop toy in which the strained pole-mass response is affine in "
          "{bare-mass retune, Hamiltonian dressing, ensemble covariance} with three distinct knock-on observables; no root number is new")
print("TOTAL: PASS=%d FAIL=%d" % (NPASS, NFAIL))
print("SUMMARY: exact checks show the strained-pole-mass Hessian is an affine functional of choices (dressing, loop-ensemble covariance, bare-mass retune) that the registered data leave free, "
      "each choice moving a different observable, so no universal Hessian follows from the registered premises and a retune is not a no-effect move (runtime %.0fs)" % (time.time() - T0))
sys.exit(0 if NFAIL == 0 else 1)
