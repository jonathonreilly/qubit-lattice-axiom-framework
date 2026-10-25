#!/usr/bin/env python3
"""Irreducible-coin freeze on the 27-point cell: exact characteristic-zero check (sympy + Fractions only).

Setting (ASSUMED, not framework content): walks U(k) = sum_{n in {-1,0,1}^3} A_n e^{i k.n}, A_n in End(C^d), unitary for all k with
respect to an invariant Hermitian form H, and covariant under the 24 proper cubic rotations R:  A_{Rn} = D(R) A_n D(R)^{-1},
with D an irreducible (projective) representation of the binary octahedral group 2O.
This script rebuilds everything from raw covariance equations, with no data from the archived campaign scripts, no Singular and no
pickles.  Output: one PASS/FAIL line per check, then TOTAL, then SUMMARY.
"""
import sys, time, itertools
from fractions import Fraction as Fr
import sympy as sp
from sympy import QQ
from sympy.polys.rings import ring
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.sdm import SDM

T0 = time.time()
NP = 0; NF = 0
def chk(name, ok, extra=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(('PASS ' if ok else 'FAIL ') + name + ((' | ' + extra) if extra else ''), flush=True)
def note(*a): print('  note:', *a, flush=True)

# ============================================================================ group, cell
RZ = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
RX = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
C3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])      # rotation by 2 pi/3 about (1,1,1)
def key(M): return tuple(int(x) for x in M)
GENS = [RZ, RX]
def build_group(gens):
    G = {key(sp.eye(3)): sp.eye(3)}
    fr = [sp.eye(3)]
    while fr:
        nx = []
        for R in fr:
            for g in gens:
                R3 = g * R
                if key(R3) not in G:
                    G[key(R3)] = R3; nx.append(R3)
        fr = nx
    return G
GROUP = build_group(GENS)
CELL = [tuple(v) for v in itertools.product((-1, 0, 1), repeat=3)]
def rot_n(g, n): return tuple(int(x) for x in g * sp.Matrix(n))
def set_group(gens):
    global GENS, GROUP
    GENS = list(gens); GROUP = build_group(GENS)

# ============================================================================ representations
sig = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(a, b): return sp.kronecker_product(a, b)
def simp(M): return M.applyfunc(lambda e: sp.expand(sp.radsimp(sp.expand(e))))

def flavour_E():
    """E: O acts on the three coordinate axes through S3; rational basis alpha1=e1-e2, alpha2=e2-e3 of the sum-zero plane, Gram form H."""
    Bm = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
    H = Bm.T * Bm
    F = {}
    for k, R in GROUP.items():
        P = R.applyfunc(abs)
        Dm = H.inv() * Bm.T * P * Bm
        assert P * Bm == Bm * Dm
        F[k] = Dm
    return H, F
def flavour_trivial():
    return sp.eye(1), {k: sp.eye(1) for k in GROUP}

def pauli_covariant_basis(HF, F, twist=None):
    """Coin = flavour (dim f, rational rep F, Gram form HF) (x) spin-1/2.  A = sum_mu a^mu (x) sigma_mu with a^mu in End(flavour).
       Ad_{S(R)} sigma_a = sum_b R[b,a] sigma_b, so covariance is a RATIONAL linear condition on the coefficient tuple (a^0,a^1,a^2,a^3):
       a^0_{Rn} = F a^0_n F^-1 ;  a^b_{Rn} = sum_a R[b,a] F a^a_n F^-1."""
    f = HF.rows
    idx = {}
    for n in CELL:
        for mu in range(4):
            for r in range(f):
                for s in range(f): idx[(n, mu, r, s)] = len(idx)
    rows = []
    for g in GENS:
        Fg = F[key(g)]; Fgi = Fg.inv(); tw = 1 if twist is None else twist(g)
        for n in CELL:
            gn = rot_n(g, n)
            for mu in range(4):
                for r in range(f):
                    for s in range(f):
                        row = {idx[(gn, mu, r, s)]: sp.Integer(1)}
                        srcs = [(0, 1)] if mu == 0 else [(a, g[mu - 1, a - 1]) for a in (1, 2, 3)]
                        for a, cf in srcs:
                            if cf == 0: continue
                            for u in range(f):
                                for v in range(f):
                                    c = tw * cf * Fg[r, u] * Fgi[v, s]
                                    if c != 0:
                                        j = idx[(n, a, u, v)]; row[j] = row.get(j, 0) - c
                        rows.append(row)
    M = sp.zeros(len(rows), len(idx))
    for i, row in enumerate(rows):
        for j, c in row.items(): M[i, j] = c
    ns = DomainMatrix.from_Matrix(M).convert_to(QQ).nullspace().to_Matrix()
    basis = []
    for v in range(ns.rows):
        Bd = {}
        for n in CELL:
            A = sp.zeros(2 * f, 2 * f)
            for mu in range(4):
                a = sp.Matrix(f, f, lambda r, s: ns[v, idx[(n, mu, r, s)]])
                A += kron(a, sig[mu])
            Bd[n] = A
        basis.append(Bd)
    return basis

def covariant_basis_conj(d, D, twist=None):
    """basis of {A_n : A_{gn} = t(g) D_g A_n D_g^{-1}} for a rational rep D (t = optional character, default 1)."""
    idx = {}
    for n in CELL:
        for r in range(d):
            for s in range(d): idx[(n, r, s)] = len(idx)
    rows = []
    for g in GENS:
        Dg = D[key(g)]; Dgi = Dg.inv(); t = 1 if twist is None else twist(g)
        for n in CELL:
            gn = rot_n(g, n)
            for r in range(d):
                for s in range(d):
                    row = {idx[(gn, r, s)]: sp.Integer(1)}
                    for a in range(d):
                        for b in range(d):
                            c = t * Dg[r, a] * Dgi[b, s]
                            if c != 0:
                                j = idx[(n, a, b)]; row[j] = row.get(j, 0) - c
                    rows.append(row)
    M = sp.zeros(len(rows), len(idx))
    for i, row in enumerate(rows):
        for j, c in row.items(): M[i, j] = c
    ns = DomainMatrix.from_Matrix(M).convert_to(QQ).nullspace().to_Matrix()
    return [{n: sp.Matrix(d, d, lambda r, s: ns[v, idx[(n, r, s)]]) for n in CELL} for v in range(ns.rows)]

# ============================================================================ unitarity equations (real polynomial ring)
def build_equations(basis, H, mlist=None):
    """A_n = sum_j (x_j + i y_j) M_jn.  Equations: sum_n A_n H^-1 A_{n-m}^* H = delta_{m0} I (all 125 shifts m), split into real and imaginary parts."""
    p = len(basis); d = basis[0][CELL[0]].rows
    R, *vs = ring([f'x{j}' for j in range(p)] + [f'y{j}' for j in range(p)], QQ)
    xs = vs[:p]; ys = vs[p:]
    def q(e):
        e = sp.Rational(e); return QQ(int(e.p), int(e.q))
    XR = {}; XI = {}
    for n in CELL:
        xr = [[R.zero] * d for _ in range(d)]; xi = [[R.zero] * d for _ in range(d)]
        for j in range(p):
            for a in range(d):
                for b in range(d):
                    e = basis[j][n][a, b]
                    if e == 0: continue
                    re = q(sp.re(e)); im = q(sp.im(e))
                    xr[a][b] += xs[j] * re - ys[j] * im
                    xi[a][b] += xs[j] * im + ys[j] * re
        XR[n] = xr; XI[n] = xi
    Hi = H.inv()
    Hm = [[q(H[a, b]) for b in range(d)] for a in range(d)]
    Him = [[q(Hi[a, b]) for b in range(d)] for a in range(d)]
    def mm(A, B):
        return [[sum((A[i][l] * B[l][j] for l in range(len(B)) if A[i][l] != 0 and B[l][j] != 0), R.zero)
                 for j in range(len(B[0]))] for i in range(len(A))]
    tr = lambda A: [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    add = lambda A, B: [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    sub = lambda A, B: [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    WR = {n: mm(XR[n], Him) for n in CELL}; WI = {n: mm(XI[n], Him) for n in CELL}
    if mlist is None: mlist = list(itertools.product(range(-2, 3), repeat=3))
    eqs = {}
    for m in mlist:
        Re = [[R.zero] * d for _ in range(d)]; Im = [[R.zero] * d for _ in range(d)]
        for n in CELL:
            n2 = tuple(a - b for a, b in zip(n, m))
            if n2 not in XR: continue
            Re = add(Re, add(mm(WR[n], tr(XR[n2])), mm(WI[n], tr(XI[n2]))))
            Im = add(Im, sub(mm(WI[n], tr(XR[n2])), mm(WR[n], tr(XI[n2]))))
        Re = mm(Re, Hm); Im = mm(Im, Hm)
        if m == (0, 0, 0):
            for a in range(d): Re[a][a] -= 1
        for a in range(d):
            for b in range(d):
                for e in (Re[a][b], Im[a][b]):
                    if e != 0: eqs[e] = m
    return R, xs, ys, list(eqs.keys()), XR, XI

# ============================================================================ exact elimination tools
def span_rref(polys, R):
    mons = set()
    for f in polys: mons.update(f.keys())
    mons = sorted(mons, key=lambda m: (-sum(m), tuple(-e for e in m)))
    col = {m: i for i, m in enumerate(mons)}
    dod = {i: {col[m]: QQ.convert(c) for m, c in f.items()} for i, f in enumerate(polys)}
    dm = DomainMatrix.from_rep(SDM(dod, (len(polys), len(mons)), QQ))
    Rm, piv = dm.rref()
    out = []
    for i, row in Rm.rep.to_dod().items():
        e = R.zero
        for j, c in row.items(): e = e + R.from_dict({mons[j]: c})
        out.append(e)
    return out

def linear_cascade(eqs, R, maxit=40):
    """Repeat: Q-span of the equations (exact RREF), solve its linear members, substitute.  Every step is a consequence of the
       equations over Q, hence valid over C.  Returns (remaining equations, substitution dict var_index -> linear form);
       remaining == [1] means 1 lies in the ideal (no solution over C)."""
    eqs = [e for e in eqs if e != 0]
    subs = {}
    for it in range(maxit):
        B = span_rref(eqs, R)
        for e in B:
            if all(sum(m) == 0 for m in e.keys()): return [R.one], subs
        lin = [e for e in B if max(sum(m) for m in e.keys()) <= 1]
        if not lin: return B, subs
        s = {}
        for e in lin:
            terms = sorted(e.terms(), key=lambda t: (-sum(t[0]), tuple(-x for x in t[0])))
            lead_m, lead_c = terms[0]
            v = lead_m.index(1)
            expr = R.zero
            for m, c in terms[1:]: expr = expr + R.from_dict({m: -c / lead_c})
            s[v] = expr
        gens = R.gens
        def apply(f):
            for v, expr in s.items(): f = f.compose(gens[v], expr)
            return f
        subs = {v: apply(f) for v, f in subs.items()}
        subs.update(s)
        eqs = [apply(e) for e in B if e not in lin]
        eqs = [e for e in eqs if e != 0]
    return eqs, subs

def left_vars(eqs): return sorted({i for e in eqs for m in e.keys() for i, x in enumerate(m) if x})

def groebner_nilpotency(eqs, R, maxpow=14):
    vl = left_vars(eqs)
    gens = [R.gens[i].as_expr() for i in vl]
    G = sp.groebner([e.as_expr() for e in eqs], *gens, order='grevlex')
    if G.exprs == [1]: return True, {}, G
    res = {}
    for g in gens:
        pw = 1
        while G.reduce(g ** pw)[1] != 0 and pw < maxpow: pw += 1
        res[str(g)] = pw if G.reduce(g ** pw)[1] == 0 else None
    return False, res, G

def close_system(eqs, subs, R):
    nv = len(R.gens)
    if eqs == [R.one]: return {'status': 'infeasible'}
    appear = left_vars(eqs)
    free = [i for i in range(nv) if i not in subs and i not in appear]
    if free: return {'status': 'underdetermined', 'free': [str(R.gens[i]) for i in free]}
    nil = {}
    if appear:
        one, res, G = groebner_nilpotency(eqs, R)
        if one: return {'status': 'infeasible'}
        if any(v is None for v in res.values()): return {'status': 'not_zero_dimensional', 'res': res}
        nil = res
    pt = {}
    for i in range(nv):
        if i in subs:
            f = subs[i]; pt[i] = f.coeff(1) if f != 0 else QQ(0)
        else: pt[i] = QQ(0)
    return {'status': 'unique_point', 'nilpotency': nil, 'point': pt}

def point_to_walk(point, basis, d):
    p = len(basis); A = {}
    qq = lambda v: sp.Rational(int(v.numerator), int(v.denominator))
    for n in CELL:
        M = sp.zeros(d, d)
        for j in range(p): M += (qq(point[j]) + sp.I * qq(point[p + j])) * basis[j][n]
        A[n] = M.applyfunc(sp.expand)
    return A
def is_identity_walk(A, d): return all(A[n] == (sp.eye(d) if n == (0, 0, 0) else sp.zeros(d, d)) for n in CELL)

# ---- Macaulay-matrix certificates:  x_v^N = sum_i c_i f_i  (explicit cofactors, exact linear algebra over Q, several targets at once)
def macaulay_certs(eqs, R, targets, D, vl):
    """targets: list of (var_index, N).  Returns a list (one entry per target) of cofactor lists, or None where no certificate of degree <= D exists."""
    n = len(vl)
    def monos_upto(Dm):
        out = []
        def rec(i, left, cur):
            if i == n: out.append(tuple(cur)); return
            for e in range(left + 1):
                cur.append(e); rec(i + 1, left - e, cur); cur.pop()
        rec(0, Dm, []); return out
    red = lambda m: tuple(m[v] for v in vl)
    fd = [{red(m): c for m, c in f.items()} for f in eqs]
    degs = [max(sum(m) for m in f) for f in fd]
    cols = {m: i for i, m in enumerate(monos_upto(D))}
    rows = []; meta = []
    for i, f in enumerate(fd):
        if degs[i] > D: continue
        for sh in monos_upto(D - degs[i]):
            r = {}
            for m, c in f.items(): r[cols[tuple(a + b for a, b in zip(m, sh))]] = c
            rows.append(r); meta.append((i, sh))
    nr = len(rows); nc = len(cols)
    dod = {}
    for j, r in enumerate(rows):
        for ci, c in r.items(): dod.setdefault(ci, {})[j] = QQ.convert(c)
    ok_t = []
    for t, (v, N) in enumerate(targets):
        tm = tuple(N if u == v else 0 for u in vl)
        if sum(tm) > D: ok_t.append(False); continue
        dod.setdefault(cols[tm], {})[nr + t] = QQ(1); ok_t.append(True)
    Rm, piv = DomainMatrix.from_rep(SDM(dod, (nc, nr + len(targets)), QQ)).rref()
    pivrows = {min(row.keys()): row for ri, row in Rm.rep.to_dod().items()}
    # target t is solvable iff every row with zero left part (pivot in a right-hand-side column) has a zero entry in column nr+t
    inconsistent = set()
    for pc, row in pivrows.items():
        if pc >= nr: inconsistent.update(cidx for cidx in row.keys() if cidx >= nr)
    out = []
    for t in range(len(targets)):
        if not ok_t[t] or (nr + t) in inconsistent: out.append(None); continue
        cof = [{} for _ in eqs]
        for pc, row in pivrows.items():
            if pc < nr and (nr + t) in row:
                i, sh = meta[pc]; cof[i][sh] = cof[i].get(sh, 0) + row[nr + t]
        out.append(cof)
    return out
def verify_cert(eqs, R, var_index, N, cof, vl):
    tot = R.zero
    for f, cf in zip(eqs, cof):
        for sh, v in cf.items():
            mono = [0] * len(R.gens)
            for k, e in zip(vl, sh): mono[k] = e
            tot = tot + f * R.from_dict({tuple(mono): v})
    tgt = R.from_dict({tuple(N if i == var_index else 0 for i in range(len(R.gens))): QQ(1)})
    return tot == tgt

# ---- certificate-recording linear cascade:  1 = sum_i c_i f_i  (explicit cofactors; checked by multiplying out)
def express(polys, targets):
    """coefficients lam with sum_i lam_i polys_i = target, for each target in the Q-span (exact, sparse)"""
    mons = set()
    for f in polys: mons.update(f.keys())
    for t in targets: mons.update(t.keys())
    mons = sorted(mons, key=lambda m: (-sum(m), tuple(-e for e in m)))
    col = {m: i for i, m in enumerate(mons)}
    n = len(polys); k = len(targets)
    dod = {}
    for j, f in enumerate(polys):
        for m, c in f.items(): dod.setdefault(col[m], {})[j] = QQ.convert(c)
    for j, t in enumerate(targets):
        for m, c in t.items(): dod.setdefault(col[m], {})[n + j] = QQ.convert(c)
    Rm, piv = DomainMatrix.from_rep(SDM(dod, (len(mons), n + k), QQ)).rref()
    pivrows = {min(row.keys()): row for ri, row in Rm.rep.to_dod().items()}
    out = []
    for j in range(k):
        assert (n + j) not in pivrows
        out.append({pc: row[n + j] for pc, row in pivrows.items() if pc < n and (n + j) in row})
    return out

def cert_cascade(eqs, R, maxit=40):
    state = [(f, {i: R.one}) for i, f in enumerate(eqs) if f != 0]
    gens = R.gens
    def combine(lam, state):
        cert = {}
        for j, c in lam.items():
            for kk, cf in state[j][1].items(): cert[kk] = cert.get(kk, R.zero) + cf * c
        return cert
    for it in range(maxit):
        polys = [f for f, _ in state]
        B = span_rref(polys, R)
        lin = [e for e in B if max(sum(m) for m in e.keys()) <= 1]
        if not lin: return None
        lams = express(polys, lin)
        linc = [(e, combine(lam, state)) for e, lam in zip(lin, lams)]
        for e, cert in linc:
            if all(sum(m) == 0 for m in e.keys()):
                c0 = e.coeff(1)
                return {k_: v * (1 / c0) for k_, v in cert.items()}
        linn = []
        for e, cert in linc:
            terms = sorted(e.terms(), key=lambda t: (-sum(t[0]), tuple(-x for x in t[0])))
            lead_m, lead_c = terms[0]
            v = lead_m.index(1); inv = 1 / lead_c
            linn.append((v, e * inv, {k_: val * inv for k_, val in cert.items()}))
        rest = [e for e in B if max(sum(m) for m in e.keys()) > 1]
        lams = express(polys, rest) if rest else []
        newstate = []
        for e, lam in zip(rest, lams):
            cert = combine(lam, state); f = e
            for v, l, lc in linn:
                fc = f.compose(gens[v], gens[v] - l)
                if fc == f: continue
                g = (f - fc).exquo(l); f = fc
                for kk, val in lc.items(): cert[kk] = cert.get(kk, R.zero) - g * val
            if f != 0: newstate.append((f, cert))
        state = newstate
    return None
def verify_one(eqs, R, cert):
    tot = R.zero
    for k_, cf in cert.items(): tot = tot + cf * eqs[k_]
    return tot == R.one

# ============================================================================ field K = Q(i, sqrt3) and exact line-branch machinery
KZ = (Fr(0),) * 4
def Kadd(u, v): return tuple(a + b for a, b in zip(u, v))
def Kmul(u, v):
    a0, a1, a2, a3 = u; b0, b1, b2, b3 = v
    return (a0*b0 - a1*b1 + 3*a2*b2 - 3*a3*b3,
            a0*b1 + a1*b0 + 3*(a2*b3 + a3*b2),
            a0*b2 + a2*b0 - (a1*b3 + a3*b1),
            a0*b3 + a3*b0 + a1*b2 + a2*b1)
KB = [tuple(Fr(1) if i == j else Fr(0) for j in range(4)) for i in range(4)]
def to_K(expr):
    expr = sp.expand(sp.radsimp(sp.expand(expr)))
    s3 = sp.sqrt(3); out = [sp.Integer(0)] * 4
    for kx, v in expr.as_coefficients_dict().items():
        if kx == 1: out[0] += v
        elif kx == sp.I: out[1] += v
        elif kx == s3: out[2] += v
        elif kx == sp.I * s3: out[3] += v
        else: raise ValueError(f'outside Q(i,sqrt3): {kx}')
    r = tuple(Fr(int(o.p), int(o.q)) for o in out)
    assert sp.expand(r[0] + r[1] * sp.I + r[2] * s3 + r[3] * sp.I * s3 - expr) == 0
    return r
def Kmat(M): return [[to_K(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]

def line_forms(projs_K, basis, axis, d):
    levels = sorted({sum(a * b for a, b in zip(n, axis)) for n in CELL})
    BK = [{n: Kmat(Bj[n]) for n in CELL} for Bj in basis]
    rows = []; idx = []
    for j, P in enumerate(projs_K):
        for r in levels:
            idx.append((j, r)); row = []
            for Bk in BK:
                acc = KZ
                for n in CELL:
                    if sum(a * b for a, b in zip(n, axis)) != r: continue
                    M = Bk[n]
                    for a in range(d):
                        for b in range(d):
                            if P[a][b] != KZ and M[b][a] != KZ: acc = Kadd(acc, Kmul(P[a][b], M[b][a]))
                row.append(acc)
            rows.append(row)
    return levels, idx, rows
def weil(rows):
    out = []
    for row in rows:
        for comp in range(4): out.append([Kmul(L, KB[k])[comp] for L in row for k in range(4)])
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in r] for r in out])

def consistent_branches(projA, projB, basis, d, axisA=(1, 0, 0), axisB=(1, 1, 1)):
    """All (m,q): axis exponents m_j in {-1,0,1} (one per 1-dim eigenspace of the axis stabiliser), body exponents q_a in [-3,3], for which
       the K-linear system  tr(P_j B_r(c)) = [m_j=r], tr(P_a C_p(c)) = [q_a=p]  has a solution c in C^p.  Exact: Weil restriction over Q."""
    p = len(basis)
    lvA, idxA, rowsA = line_forms(projA, basis, axisA, d) if projA else ([], [], [])
    lvB, idxB, rowsB = line_forms(projB, basis, axisB, d) if projB else ([], [], [])
    LA = weil(rowsA) if rowsA else sp.zeros(0, 4 * p)
    LB = weil(rowsB) if rowsB else sp.zeros(0, 4 * p)
    Lm = sp.Matrix.vstack(LA, LB)
    N = DomainMatrix.from_Matrix(Lm.T).convert_to(QQ).nullspace().to_Matrix()      # left null space of Lm
    na = LA.rows
    def tv(idx, assign):
        t = []
        for (j, r) in idx: t += [sp.Rational(1 if assign[j] == r else 0), 0, 0, 0]
        return sp.Matrix(t)
    z = sp.zeros(N.rows, 1)
    vA = {m: (N[:, :na] * tv(idxA, m)) for m in itertools.product(lvA, repeat=len(projA))} if projA else {(): z}
    vB = {q: (N[:, na:] * tv(idxB, q)) for q in itertools.product(range(-3, 4), repeat=len(projB))} if projB else {(): z}
    cons = [(m, q) for m, a in vA.items() for q, b in vB.items() if (a + b).is_zero_matrix]
    return cons, len(vA), len(vB)

def eig_projectors(D0):
    d = D0.rows; ev = list(D0.eigenvals().keys()); assert len(ev) == d
    res = []
    for i, l in enumerate(ev):
        P = sp.eye(d)
        for j, m in enumerate(ev):
            if j != i: P = P * (D0 - m * sp.eye(d)) / (l - m)
        res.append(simp(P))
    return res
def matunits(d):
    out = []
    for a in range(d):
        for b in range(d):
            W = sp.zeros(d, d); W[b, a] = 1          # tr(W C) = C[a,b]
            out.append((W, 1 if a == b else 0))
    return out

def make_coin(name):
    c = {'name': name}
    if name in ('E', 'spin1'):
        if name == 'E': H, F = flavour_E(); d = 2
        else: H, F = sp.eye(3), dict(GROUP); d = 3
        c.update(d=d, H=H, D=F, basis=covariant_basis_conj(d, F))
        c['axis_projs'] = eig_projectors(F[key(RX)]); c['body_projs'] = eig_projectors(F[key(C3)])
        c['body_trivial'] = matunits(d)
    elif name == 'spin12':
        HF, F = flavour_trivial(); d = 2
        c.update(d=d, H=sp.eye(2), basis=pauli_covariant_basis(HF, F))
        c['axis_projs'] = [(sp.eye(2) + s * sig[1]) / 2 for s in (1, -1)]
        ssum = sig[1] + sig[2] + sig[3]
        c['body_projs'] = [simp((sp.eye(2) + s * ssum / sp.sqrt(3)) / 2) for s in (1, -1)]
        c['body_trivial'] = matunits(d)
    elif name == 'spin32':
        HF, F = flavour_E(); d = 4
        c.update(d=d, H=kron(HF, sp.eye(2)), D=F, basis=pauli_covariant_basis(HF, F))
        Fx = F[key(RX)]
        Pf = [(sp.eye(2) + e * Fx) / 2 for e in (1, -1)]
        Ps = [(sp.eye(2) + s * sig[1]) / 2 for s in (1, -1)]
        c['axis_projs'] = [kron(a, b) for a in Pf for b in Ps]
        F3 = F[key(C3)]; ssum = sig[1] + sig[2] + sig[3]
        om = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
        Pw = Pwb = None
        for l in F3.eigenvals():
            P = simp((F3 - sp.conjugate(l) * sp.eye(2)) / (l - sp.conjugate(l)))
            if sp.simplify(l - om) == 0: Pw = P
            else: Pwb = P
        Pn = {s: (sp.eye(2) + s * ssum / sp.sqrt(3)) / 2 for s in (1, -1)}
        c['body_projs'] = [simp(kron(Pw, Pn[1])), simp(kron(Pwb, Pn[-1]))]
        Jr = -sp.I * (2 * F3 + sp.eye(2))
        S_plus = (sp.eye(4) + kron(Jr, ssum) / 3) / 2
        S_minus = kron(Jr, sp.eye(2)) + kron(sp.eye(2), ssum)
        c['body_trivial'] = [(S_plus, 2), (S_minus, 0)]
        c['S_plus'] = S_plus; c['S_minus'] = S_minus
    return c

def branch_linear_conditions(c, R, XR, XI, m):
    """line conditions of the branch (axis exponents m, all body exponents 0) as real linear polynomials (rational coefficients)"""
    d = c['d']
    def sums(axis, r):
        lv = [n for n in CELL if sum(u * w for u, w in zip(n, axis)) == r]
        SR = [[sum((XR[n][a][b] for n in lv), R.zero) for b in range(d)] for a in range(d)]
        SI = [[sum((XI[n][a][b] for n in lv), R.zero) for b in range(d)] for a in range(d)]
        return SR, SI
    def q(e):
        e = sp.Rational(e); return QQ(int(e.p), int(e.q))
    lin = []
    for r in (-1, 0, 1):
        SR, SI = sums((1, 0, 0), r)
        T = sum((c['axis_projs'][j] for j in range(len(c['axis_projs'])) if m[j] == r), sp.zeros(d, d))
        for a in range(d):
            for b in range(d):
                e1 = SR[a][b] - q(sp.re(T[a, b])); e2 = SI[a][b] - q(sp.im(T[a, b]))
                if e1 != 0: lin.append(e1)
                if e2 != 0: lin.append(e2)
    for p in range(-3, 4):
        CR, CI = sums((1, 1, 1), p)
        for W, rhs in c['body_trivial']:
            tr = R.zero; ti = R.zero
            for a in range(d):
                for b in range(d):
                    w = W[a, b]
                    if w == 0: continue
                    wr, wi = q(sp.re(w)), q(sp.im(w))
                    tr = tr + CR[b][a] * wr - CI[b][a] * wi
                    ti = ti + CI[b][a] * wr + CR[b][a] * wi
            e1 = tr - (rhs if p == 0 else 0)
            if e1 != 0: lin.append(e1)
            if ti != 0: lin.append(ti)
    return lin

# ============================================================================ the checks
def part_group():
    print('--- Part 1: group, cell, representations', flush=True)
    chk('P1.1 proper cubic rotation group generated by two quarter turns has order 24', len(GROUP) == 24)
    orb = {}
    for n in CELL:
        orb.setdefault(frozenset(rot_n(R, n) for R in GROUP.values()), []).append(n)
    sizes = sorted(len(o) for o in orb)
    chk('P1.2 orbits of the 27 cell points have sizes 1, 6, 8, 12', sizes == [1, 6, 8, 12], str(sizes))
    stab = sorted(sum(1 for R in GROUP.values() if rot_n(R, n) == n) for n in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)])
    chk('P1.3 stabiliser orders 24, 4, 2, 3 (origin, face, edge, corner)', stab == [2, 3, 4, 24], str(stab))

def explicit_spin_lifts():
    """SU(2) lifts S(R) for all 24 rotations (BFS products of the generators' lifts); entries in Q(i, sqrt2)."""
    Sz = ((sp.eye(2) - sp.I * sig[3]) / sp.sqrt(2)).applyfunc(sp.nsimplify)
    Sx = ((sp.eye(2) - sp.I * sig[1]) / sp.sqrt(2)).applyfunc(sp.nsimplify)
    S = {key(sp.eye(3)): sp.eye(2)}; fr = [(sp.eye(3), sp.eye(2))]
    while fr:
        nx = []
        for R, M in fr:
            for g, Sg in ((RZ, Sz), (RX, Sx)):
                R3 = g * R; k3 = key(R3)
                if k3 not in S:
                    S[k3] = simp(Sg * M); nx.append((R3, S[k3]))
        fr = nx
    return S

def part_reps():
    HE, FE = flavour_E()
    chk('P1.4 E: homomorphism O -> GL(2,Q) on the rational basis', all(FE[key(R1 * R2)] == FE[key(R1)] * FE[key(R2)] for R1 in GROUP.values() for R2 in GROUP.values()))
    chk('P1.5 E: Gram form invariant, F^T H F = H', all(F.T * HE * F == HE for F in FE.values()))
    chk('P1.6 T1 (spin 1 = vector rep): R^T R = 1 (form H=1) and homomorphism', all(R.T * R == sp.eye(3) for R in GROUP.values()))
    S = explicit_spin_lifts()
    ok = True
    for k, R in GROUP.items():
        for a in range(3):
            lhs = simp(S[k] * sig[a + 1] * S[k].H)
            rhs = sum((R[b, a] * sig[b + 1] for b in range(3)), sp.zeros(2, 2))
            ok = ok and simp(lhs - rhs).is_zero_matrix
    chk('P1.7 spin-1/2 lifts: S sigma_a S^dag = sum_b R[b,a] sigma_b for all 24 rotations (basis of the Pauli-factorised model)', ok)
    # characters on the 48 elements of 2O = {+-S(R)}
    sgn = lambda R: int(R.applyfunc(abs).det())
    elems = [(R, S[k], 1) for k, R in GROUP.items()] + [(R, -S[k], -1) for k, R in GROUP.items()]
    th = lambda M: sp.acos(sp.simplify(M.trace() / 2)) * 2           # SU(2) rotation angle in [0, 2 pi]
    chars = {name: [] for name in ('A1', 'A2', 'E', 'T1', 'T2', 'E12', 'E52', 'H', 'spin32', 'spin1')}
    for R, M, sgnlift in elems:
        k = key(R)
        trS = sp.nsimplify(sp.simplify(M.trace()))
        trF = sp.nsimplify(FE[k].trace()); trR = R.trace(); s = sgn(R)
        chars['A1'].append(1); chars['A2'].append(s); chars['E'].append(trF)
        chars['T1'].append(trR); chars['T2'].append(trR * s)
        chars['E12'].append(trS); chars['E52'].append(trS * s); chars['H'].append(sp.nsimplify(trF * trS))
        t = th(M)       # spin-3/2 and spin-1 characters of the SU(2) element M
        chars['spin32'].append(sp.simplify(2 * sp.cos(3 * t / 2) + 2 * sp.cos(t / 2)))
        chars['spin1'].append(sp.simplify(1 + 2 * sp.cos(t)))
    chk('P1.8 character of kron(E, spin-1/2) equals the spin-3/2 character on all 48 elements of 2O', all(sp.simplify(a - b) == 0 for a, b in zip(chars['H'], chars['spin32'])))
    chk('P1.9 character of the vector rep equals the spin-1 character on all 48 elements', all(sp.simplify(a - b) == 0 for a, b in zip(chars['T1'], chars['spin1'])))
    names = ['A1', 'A2', 'E', 'T1', 'T2', 'E12', 'E52', 'H']
    gram = sp.Matrix(8, 8, lambda i, j: sp.nsimplify(sp.simplify(sum(sp.conjugate(a) * b for a, b in zip(chars[names[i]], chars[names[j]])) / 48)))
    chk('P1.10 the eight characters A1,A2,E,T1,T2,E1/2,E5/2,H are orthonormal on 2O (48 elements); dims 1,1,2,3,3,2,2,4 give sum of squares 48: complete list of irreps',
        gram == sp.eye(8) and sum(x * x for x in (1, 1, 2, 3, 3, 2, 2, 4)) == 48)
    sgn_ok = all(sp.simplify(chars['A2'][i] - chars['A2'][i + 24]) == 0 for i in range(24))
    note('twisting by the sign character A2 leaves the conjugation action unchanged (T2~T1, E5/2~E1/2, A2~A1, H(x)A2~H): Ad(D(x)A2)=Ad(D)')
    chk('P1.11 sign character is even on -1 in 2O (so tensoring by it does not change Ad_D)', sgn_ok)
    mult = {nm: sp.nsimplify(sp.simplify(sum(sp.Abs(chars[nm][i]) ** 2 * chars['T1'][i] for i in range(24)) / 24)) for nm in ('E', 'T1', 'E12', 'H')}
    chk('P1.12 multiplicity of the vector rep T1 in End(D): E:0, T1:1, E1/2:1, H:2 (a covariant Clifford triple sigma_a needs T1 in End(D): impossible for E; T1 has odd dimension and Cl(3) irreps are 2-dimensional; spin 1/2 and spin 3/2 = E(x)spin 1/2 carry sigma(x)1)',
        mult == {'E': 0, 'T1': 1, 'E12': 1, 'H': 2}, str(mult))
    return S

def part_covariant(coins):
    print('--- Part 2: covariant parameter counts, Schur, unitarity forms', flush=True)
    exp = {'E': 7, 'spin1': 12, 'spin12': 7, 'spin32': 19}
    for name, c in coins.items():
        p = len(c['basis'])
        d = c['d']
        chk(f'P2.{name}.a covariant parameter count = 1 (origin) + dim(commutant of C4) + dim(commutant of C2) + dim(commutant of C3) = {exp[name]}', p == exp[name], f'p={p}')
        origin = [Bj[(0, 0, 0)] for Bj in c['basis']]
        sc = all(M == M[0, 0] * sp.eye(d) for M in origin) and sum(1 for M in origin if M != sp.zeros(d, d)) == 1
        chk(f'P2.{name}.b origin coefficient A_0 is forced to be a scalar by covariance (Schur: coin irreducible)', sc)
        U0 = [sum((Bj[n] for n in CELL), sp.zeros(d, d)) for Bj in c['basis']]
        chk(f'P2.{name}.c U(0) = sum_n A_n is a scalar matrix for every covariant walk', all(M == M[0, 0] * sp.eye(d) for M in U0))
    # unitarity form invariance for the explicit D (spin-3/2: kron(F, S) with the SU(2) lifts of the generators)
    HE, FE = flavour_E()
    Sz = ((sp.eye(2) - sp.I * sig[3]) / sp.sqrt(2)); Sx = ((sp.eye(2) - sp.I * sig[1]) / sp.sqrt(2))
    H4 = kron(HE, sp.eye(2)); ok = True
    for g, Sg in ((RZ, Sz), (RX, Sx)):
        D4 = kron(FE[key(g)], Sg)
        ok = ok and simp(D4.H * H4 * D4 - H4).is_zero_matrix
    chk('P2.spin32.d explicit D(g)=F(g)(x)S(g) preserves the Hermitian form H(x)1 on the generators (unitarity is meaningful)', ok)
    # covariance of the Pauli-factorised basis verified against the explicit spinor-lift D
    ok = True
    for g, Sg in ((RZ, Sz), (RX, Sx)):
        D4 = kron(FE[key(g)], Sg); D4i = D4.inv()
        for Bj in coins['spin32']['basis']:
            for n in CELL:
                diff = simp(Bj[rot_n(g, n)] - D4 * Bj[n] * D4i)
                if not diff.is_zero_matrix: ok = False
    chk('P2.spin32.e Pauli-factorised covariant basis satisfies A_{gn} = D(g) A_n D(g)^-1 with the explicit 4x4 D(g)=F(g)(x)S(g) (generators; group generated)', ok)
    ok = True
    for g, Sg in ((RZ, Sz), (RX, Sx)):
        for Bj in coins['spin12']['basis']:
            for n in CELL:
                if not simp(Bj[rot_n(g, n)] - Sg * Bj[n] * Sg.inv()).is_zero_matrix: ok = False
    chk('P2.spin12.e Pauli-factorised covariant basis satisfies A_{gn} = S(g) A_n S(g)^-1 with explicit SU(2) lifts', ok)

def part_channels(coins):
    print('--- Part 2b: Clifford-spinor x flavour content of the spin-3/2 covariant parameters', flush=True)
    HE, FE = flavour_E()
    sgn = lambda g: int(g.applyfunc(abs).det())
    x = sp.symbols('j0:4'); J = sp.Matrix(2, 2, x); eqs = []
    for g in GENS: eqs += list(FE[key(g)] * J * FE[key(g)].inv() - sgn(g) * J)
    sol = sp.solve(eqs, x, dict=True)[0]; Jm = J.subs(sol); fr = sorted(Jm.free_symbols, key=str); Jm = Jm.subs({fr[0]: 1})
    chk('P2b.1 End(E) = A1 (identity) + A2 (one element J with F J F^-1 = sign J, J^2 = -3) + E (two elements); J exists and J^2 is a nonzero scalar',
        (Jm * Jm)[0, 1] == 0 and (Jm * Jm)[0, 0] == (Jm * Jm)[1, 1] != 0, str(Jm.tolist()))
    def chan(a, c):
        if c == '1': return a.trace() / 2 * sp.eye(2)
        if c == 'J': return (a * Jm).trace() / (Jm * Jm).trace() * Jm
        return a - chan(a, '1') - chan(a, 'J')
    basis = coins['spin32']['basis']
    def comps(A4):
        return {mu: sp.Matrix(2, 2, lambda r, s_: sum((A4[2 * r + u, 2 * s_ + v] * sig[mu][v, u] for u in range(2) for v in range(2)), 0) / 2) for mu in range(4)}
    CM = [{n: comps(Bj[n]) for n in CELL} for Bj in basis]
    parts = {}
    for typ, mus in (('spin-scalar', [0]), ('spin-vector', [1, 2, 3])):
        for ch in ('1', 'J', 'E'):
            vecs = []
            for cm in CM:
                v = []
                for n in CELL:
                    for mu in mus: v += list(chan(cm[n][mu], ch))
                vecs.append(v)
            parts[(typ, ch)] = sp.Matrix(vecs).rank()
    chk('P2b.2 the 19 covariant parameters split as spin-scalar (x) {identity, J, E-doublet} = 4+1+2 and spin-vector (x) {identity, J, E-doublet} = 3+3+6; the identity-flavour channel (4+3=7) is the one-qubit sector u(k)(x)1',
        parts == {('spin-scalar', '1'): 4, ('spin-scalar', 'J'): 1, ('spin-scalar', 'E'): 2, ('spin-vector', '1'): 3, ('spin-vector', 'J'): 3, ('spin-vector', 'E'): 6}, str(parts))

def part_equations(coins):
    print('--- Part 3: Laurent unitarity equations (all 125 shifts m) and the identity walk', flush=True)
    data = {}
    for name, c in coins.items():
        t = time.time()
        R, xs, ys, eqs, XR, XI = build_equations(c['basis'], c['H'])
        data[name] = (R, xs, ys, eqs, XR, XI)
        d = c['d']
        # identity walk: x_0 = 1 at the origin-coefficient parameter
        p = len(c['basis'])
        j0 = [j for j in range(p) if c['basis'][j][(0, 0, 0)] != sp.zeros(d, d)][0]
        pt = {}
        for g in R.gens: pt[g] = 0
        sc = c['basis'][j0][(0, 0, 0)][0, 0]
        pt[xs[j0]] = 1 / sc
        ok = all(e.evaluate(list(pt.items())) == 0 for e in eqs)
        chk(f'P3.{name} {len(eqs)} distinct real equations in {2*p} real unknowns; the identity walk (A_0 = 1, others 0) satisfies all of them', ok, f'{time.time()-t:.1f}s')
    return data

def part_controls():
    print('--- Part 4: positive controls (the machinery must not hide genuine moving covariant walks)', flush=True)
    global GENS, GROUP
    saveG, saveGr = GENS, GROUP
    try:
        # D4 (fourfold axis z + half turn about x): axial shifts exp(+-i k_z sigma_z) of the companion classification
        set_group([RZ, sp.diag(1, -1, -1)])
        HF, F = flavour_trivial(); basis = pauli_covariant_basis(HF, F)
        R, xs, ys, eqs, XR, XI = build_equations(basis, sp.eye(2))
        res = []
        for s in (1, -1):
            A = {(0, 0, 1): (sp.eye(2) + s * sig[3]) / 2, (0, 0, -1): (sp.eye(2) - s * sig[3]) / 2}
            p = len(basis); cs = sp.symbols(f'c0:{p}')
            lin = []
            for n in CELL: lin += list(sum((cs[j] * basis[j][n] for j in range(p)), sp.zeros(2, 2)) - A.get(n, sp.zeros(2, 2)))
            sol = sp.solve(lin, cs, dict=True)
            inside = bool(sol) and all(c in sol[0] for c in cs)
            if inside:
                vals = [sp.re(sol[0][c]) for c in cs] + [sp.im(sol[0][c]) for c in cs]
                bad = sum(1 for e in eqs if sp.expand(e.as_expr().subs(dict(zip([g.as_expr() for g in R.gens], vals)))) != 0)
            else: bad = -1
            res.append((inside, bad))
        chk('P4.1 D4 control: both axial shifts exp(+-i k_z sigma_z) lie in the D4-covariant space and satisfy all unitarity equations exactly',
            all(i and b == 0 for i, b in res), str(res))
        projA = [Kmat((sp.eye(2) + s * sig[3]) / 2) for s in (1, -1)]
        cons, na, nb = consistent_branches(projA, [], basis, 2, axisA=(0, 0, 1))
        chk('P4.2 D4 control: the exact line-branch test keeps the shift branches (+1,-1), (-1,+1) and the trivial branch', {(c[0]) for c in cons} == {(1, -1), (-1, 1), (0, 0)}, str(cons))
        # D3 (body diagonal): shifts exp(+-i (k1+k2+k3) sigma.n)
        set_group([C3, sp.Matrix([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])])
        HF, F = flavour_trivial(); basis = pauli_covariant_basis(HF, F)
        R, xs, ys, eqs, XR, XI = build_equations(basis, sp.eye(2))
        ssum = sig[1] + sig[2] + sig[3]; res = []
        for s in (1, -1):
            Pp = simp((sp.eye(2) + s * ssum / sp.sqrt(3)) / 2); Pm = simp((sp.eye(2) - s * ssum / sp.sqrt(3)) / 2)
            A = {(1, 1, 1): Pp, (-1, -1, -1): Pm}
            p = len(basis); cs = sp.symbols(f'c0:{p}')
            lin = []
            for n in CELL: lin += list(sum((cs[j] * basis[j][n] for j in range(p)), sp.zeros(2, 2)) - A.get(n, sp.zeros(2, 2)))
            sol = sp.solve(lin, cs, dict=True)
            inside = bool(sol) and all(c in sol[0] for c in cs)
            if inside:
                vals = [sp.re(sol[0][c]) for c in cs] + [sp.im(sol[0][c]) for c in cs]
                bad = sum(1 for e in eqs if sp.simplify(e.as_expr().subs(dict(zip([g.as_expr() for g in R.gens], vals)))) != 0)
            else: bad = -1
            res.append((inside, bad))
        chk('P4.3 D3 control: both body-diagonal shifts exp(+-i (k1+k2+k3) sigma.n) lie in the D3-covariant space and satisfy all unitarity equations exactly',
            all(i and b == 0 for i, b in res), str(res))
        projB = [Kmat(simp((sp.eye(2) + s * ssum / sp.sqrt(3)) / 2)) for s in (1, -1)]
        cons, na, nb = consistent_branches([], projB, basis, 2)
        chk('P4.4 D3 control: the exact line-branch test keeps the shift branches (+1,-1), (-1,+1) and the trivial branch', {c[1] for c in cons} >= {(1, -1), (-1, 1), (0, 0)}, f'{len(cons)} consistent body-line branches')
        # E-flavour control on D4: the shift exp(+-i k_z sigma_z) (x) 1_E is covariant and unitary for the form H_E (x) 1
        set_group([RZ, sp.diag(1, -1, -1)])
        HEc, FEc = flavour_E(); basis = pauli_covariant_basis(HEc, FEc); H4 = kron(HEc, sp.eye(2))
        res = []
        for s_ in (1, -1):
            A = {(0, 0, 1): kron(sp.eye(2), (sp.eye(2) + s_ * sig[3]) / 2), (0, 0, -1): kron(sp.eye(2), (sp.eye(2) - s_ * sig[3]) / 2)}
            p = len(basis); cs = sp.symbols(f'c0:{p}'); lin = []
            for n in CELL: lin += list(sum((cs[j] * basis[j][n] for j in range(p)), sp.zeros(4, 4)) - A.get(n, sp.zeros(4, 4)))
            sol = sp.solve(lin, cs, dict=True)
            inside = bool(sol) and all(c_ in sol[0] for c_ in cs)
            Hi4 = H4.inv(); bad = 0
            for m in itertools.product(range(-2, 3), repeat=3):
                acc = sp.zeros(4, 4)
                for n in CELL:
                    n2 = tuple(a - b for a, b in zip(n, m))
                    if n in A and n2 in A: acc += A[n] * Hi4 * A[n2].H * H4
                if m == (0, 0, 0): acc -= sp.eye(4)
                if not simp(acc).is_zero_matrix: bad += 1
            res.append((inside, bad))
        chk('P4.5 flavour-E control on D4: the shifts exp(+-i k_z sigma_z)(x)1_E lie in the D4-covariant space of the spin-1/2(x)E coin and satisfy the Laurent unitarity identities for H_E(x)1 (all 125 shifts m)',
            all(i and b == 0 for i, b in res), f'{len(basis)} D4-covariant parameters; {res}')
    finally:
        GENS, GROUP = saveG, saveGr

def part_routeA(data, coins):
    print('--- Part 5: Route A (no line lemma): normalisation + exact linear cascade + Groebner basis over Q', flush=True)
    for name in ('E', 'spin12'):
        c = coins[name]; R, xs, ys, eqs, XR, XI = data[name]; d = c['d']
        norm = []
        for a in range(d):
            for b in range(d):
                re = sum((XR[n][a][b] for n in CELL), R.zero) - (1 if a == b else 0); im = sum((XI[n][a][b] for n in CELL), R.zero)
                if re != 0: norm.append(re)
                if im != 0: norm.append(im)
        t = time.time()
        B, subs = linear_cascade(eqs + norm, R)
        out = close_system(B, subs, R)
        ok = out['status'] == 'unique_point' and is_identity_walk(point_to_walk(out['point'], c['basis'], d), d)
        chk(f'P5.{name} Route A: with U(0)=1 (Schur gauge) the unitarity ideal over Q has the single solution U = 1 (all remaining unknowns nilpotent; checked in char 0, solutions counted over C)',
            ok, f"remaining {len(B)} eqs in {len(left_vars(B))} unknowns, nilpotency {out.get('nilpotency')}, {time.time()-t:.1f}s")

def part_routeB(data, coins):
    print('--- Part 6: Route B (line lemma): exact branch exhaustion + exact closure of every consistent branch', flush=True)
    results = {}
    for name in ('E', 'spin12', 'spin1', 'spin32'):
        c = coins[name]; d = c['d']; basis = c['basis']
        R, xs, ys, eqs, XR, XI = data[name]
        # (i) the rational line conditions used below equal the projector conditions: B_r, C_p commute with the stabiliser rep and projectors resolve identity
        t = time.time()
        projA = [Kmat(P) for P in c['axis_projs']]; projB = [Kmat(P) for P in c['body_projs']]
        # structural facts behind the line conditions: orthogonal rank-one idempotents, resolution of the identity (axis: all of it;
        # diagonal: with the leftover block for spin 3/2), level sums commute with every projector (hence P B_r P = tr(P B_r) P)
        okS = True
        for axis, projs in (((1, 0, 0), c['axis_projs']), ((1, 1, 1), c['body_projs'])):
            allp = list(projs)
            rest = sp.eye(d) - sum(projs, sp.zeros(d, d))
            if axis == (1, 1, 1) and name == 'spin32': allp.append(rest)
            else: okS = okS and simp(rest).is_zero_matrix
            for i, P in enumerate(allp):
                for j, Q in enumerate(allp):
                    okS = okS and simp(P * Q - (P if i == j else sp.zeros(d, d))).is_zero_matrix
            for P in projs: okS = okS and P.rank() == 1
            lv = sorted({sum(a * b for a, b in zip(n, axis)) for n in CELL})
            for Bj in basis:
                for r in lv:
                    Mr = sum((Bj[n] for n in CELL if sum(a * b for a, b in zip(n, axis)) == r), sp.zeros(d, d))
                    for P in allp: okS = okS and simp(P * Mr - Mr * P).is_zero_matrix
        if name == 'spin32':
            P1, P2 = c['body_projs']
            okS = okS and simp(P1 + P2 - c['S_plus']).is_zero_matrix and simp(2 * sp.sqrt(3) * (P1 - P2) - c['S_minus']).is_zero_matrix
        chk(f'P6.{name}.0 line-condition structure: projectors orthogonal rank-one idempotents resolving the identity, every level sum B_r, C_p commutes with them' + ('; P1+P2 = S_plus and 2 sqrt3 (P1-P2) = S_minus (rational forms used for the trivial diagonal branch)' if name == 'spin32' else ''), okS)
        cons, na, nb = consistent_branches(projA, projB, basis, d)
        results[name] = {'cons': cons}
        expected_n = {'E': 1, 'spin12': 1, 'spin1': 1, 'spin32': 3}[name]
        chk(f'P6.{name}.a exact exhaustion of {na} axis-exponent patterns x {nb} body-exponent patterns: {len(cons)} line-consistent branch(es)',
            len(cons) == expected_n and all(all(x == 0 for x in q) for (m, q) in cons), f'{cons} {time.time()-t:.1f}s')
        outs = []
        for (m, q) in cons:
            lin = branch_linear_conditions(c, R, XR, XI, m)
            B, subs = linear_cascade(eqs + lin, R)
            out = close_system(B, subs, R)
            outs.append((m, out, B, subs))
        results[name]['outs'] = outs
        triv = [o for o in outs if all(x == 0 for x in o[0])]
        mov = [o for o in outs if any(x != 0 for x in o[0])]
        ok_triv = len(triv) == 1 and triv[0][1]['status'] == 'unique_point' and is_identity_walk(point_to_walk(triv[0][1]['point'], basis, d), d)
        chk(f'P6.{name}.b trivial branch: unique solution U = 1 (remaining unknowns nilpotent {triv[0][1].get("nilpotency")})', ok_triv)
        if name == 'spin32':
            Bt = triv[0][2]; vl = left_vars(Bt); gens = [R.gens[i].as_expr() for i in vl]; ok2 = True; info2 = []
            for order in ('grlex', 'lex'):
                G2 = sp.groebner([e.as_expr() for e in Bt], *gens, order=order)
                nil2 = {str(g): next((p for p in range(1, 15) if G2.reduce(g ** p)[1] == 0), None) for g in gens}
                ok2 = ok2 and all(v is not None for v in nil2.values()) and nil2 == triv[0][1]['nilpotency']
                info2.append((order, len(G2.exprs)))
            chk('P6.spin32.d trivial-branch residual re-closed with two further monomial orders (grlex, lex): same nilpotency indices for all 10 unknowns', ok2, str(info2))
            chk('P6.spin32.c both axis-moving branches (-1,+1,+1,-1) and (+1,-1,-1,+1) are infeasible over C: 1 lies in the ideal (linear cascade, pure linear algebra over Q)',
                len(mov) == 2 and all(o[1]['status'] == 'infeasible' for o in mov))
        else:
            chk(f'P6.{name}.c no moving branch survives the exact line test', len(mov) == 0)
    return results

def part_certificates(results, data, coins):
    print('--- Part 7: explicit Nullstellensatz cofactors (engine-independent re-verification of the nilpotent residues)', flush=True)
    for name in ('E', 'spin1', 'spin32'):
        R, xs, ys, eqs, XR, XI = data[name]
        o = [q for q in results[name]['outs'] if all(x == 0 for x in q[0])][0]
        B = o[2]; vl = left_vars(B); nil = o[1]['nilpotency']
        t = time.time(); allok = True; info = []
        todo = [(v, nil[str(R.gens[v])]) for v in vl]
        gens_now = list(B)
        for D in (2, 3):                       # degree <= 3 cofactors; higher degrees exceed the time budget for spin 3/2 (see ATTEMPT.md)
            while todo:
                res = macaulay_certs(gens_now, R, todo, D, vl)
                found = [(tg, cof) for tg, cof in zip(todo, res) if cof is not None]
                if not found: break
                for (v, N), cof in found:
                    allok = allok and verify_cert(gens_now, R, v, N, cof, vl); info.append((str(R.gens[v]), N, D))
                for (v, N), cof in found: gens_now.append(R.gens[v] ** N)      # certified powers become extra generators (each is itself certified above)
                todo = [tg for tg, cof in zip(todo, res) if cof is None]
        uncert = [str(R.gens[v]) for v, N in todo]
        if name != 'spin32': allok = allok and not todo
        chk(f'P7.{name} explicit certificates x^N = sum_i c_i f_i (cofactors by exact linear algebra over Q, verified by polynomial multiplication) for {len(vl)-len(uncert)} of the {len(vl)} remaining unknowns' + (f'; not certified at cofactor degree <= 1 (these rest on the Groebner runs only): {uncert}' if uncert else ''), allok and len(info) > 0, f'{info} {time.time()-t:.1f}s')
        if name == 'spin32':
            c = coins['spin32']
            for m in [q[0] for q in results['spin32']['outs'] if any(x != 0 for x in q[0])]:
                t = time.time()
                allp = eqs + branch_linear_conditions(c, R, XR, XI, m)
                cert = cert_cascade(allp, R)
                okc = cert is not None and verify_one(allp, R, cert)
                info = (len(cert), sum(len(v) for v in cert.values()), max(max(sum(mm) for mm in v.keys()) for v in cert.values() if v)) if cert else None
                chk(f'P7.spin32.moving{m} explicit identity 1 = sum_i c_i f_i for the moving axis branch {m} (cofactors recorded through the cascade, verified by multiplying out): no solution over C', okc, f'(nonzero cofactors, terms, max cofactor degree) = {info}; {time.time()-t:.0f}s')

def part_twist(coins):
    print('--- Part 8: sign-twisted covariance, one-dimensional coins', flush=True)
    HE, FE = flavour_E()
    sgn = lambda g: int(g.applyfunc(abs).det())
    # T1 (spin 1): twisted-covariant walks have U(0) = 0
    tb = covariant_basis_conj(3, dict(GROUP), twist=sgn)
    chk('P8.1 sign-twisted covariance A_{Rn} = sign(R) R A_n R^T on spin 1: every twisted-covariant U has U(0)=0 (T1 x sign = T2 is not T1), hence none is unitary',
        all(sum((Bj[n] for n in CELL), sp.zeros(3, 3)) == sp.zeros(3, 3) for Bj in tb), f'{len(tb)} twisted parameters')
    HF1, F1 = flavour_trivial()
    tb = pauli_covariant_basis(HF1, F1, twist=sgn)
    chk('P8.2 sign-twisted covariance on spin 1/2: every twisted-covariant U has U(0)=0, hence none is unitary',
        all(sum((Bj[n] for n in CELL), sp.zeros(2, 2)) == sp.zeros(2, 2) for Bj in tb), f'{len(tb)} twisted parameters')
    # E: intertwiner T (T F = sign F T); W = U T plainly covariant
    x = sp.symbols('t0:4'); T = sp.Matrix(2, 2, x)
    eq = []
    for g in GENS: eq += list(T * FE[key(g)] - sgn(g) * FE[key(g)] * T)
    sol = sp.solve(eq, x, dict=True)[0]
    T0m = T.subs(sol); fr = sorted(T0m.free_symbols, key=str)
    Tm = T0m.subs({fr[0]: 1}) if len(fr) == 1 else None
    okT = Tm is not None and Tm.det() != 0
    if okT:
        G2 = Tm.T * HE * Tm
        okT = (G2 - (G2[0, 0] / HE[0, 0]) * HE).is_zero_matrix and G2[0, 0] != 0
    chk('P8.3 E x sign = E: the intertwiner T (T F(g) = sign(g) F(g) T) is unique up to scale, invertible and H-conformal (T^T H T = c H), so W = U T^-1 turns a twisted covariant unitary walk into a plainly covariant one', okT, str(Tm.tolist() if Tm is not None else None))
    if okT:
        tbE = covariant_basis_conj(2, FE, twist=sgn)
        ok = all(all(simp(Bj[rot_n(g, n)] * Tm - FE[key(g)] * Bj[n] * Tm * FE[key(g)].inv()).is_zero_matrix for n in CELL for g in GENS) for Bj in tbE)
        chk('P8.4 for E, every twisted-covariant family B_n times T is plainly covariant (A_{gn} = F A_n F^-1), so twisted E reduces to the plain E case', ok, f'{len(tbE)} twisted parameters')
        # spin 3/2: T (x) 1 on the flavour factor works the same way; check on the Pauli model
        tb32 = pauli_covariant_basis(HE, FE, twist=sgn)
        Sz = ((sp.eye(2) - sp.I * sig[3]) / sp.sqrt(2)); Sx = ((sp.eye(2) - sp.I * sig[1]) / sp.sqrt(2))
        T4 = kron(Tm, sp.eye(2)); ok = True
        for g, Sg in ((RZ, Sz), (RX, Sx)):
            D4 = kron(FE[key(g)], Sg); D4i = D4.inv()
            for Bj in tb32:
                for n in CELL:
                    if not simp(Bj[rot_n(g, n)] * T4 - D4 * Bj[n] * T4 * D4i).is_zero_matrix: ok = False
        chk('P8.5 for spin 3/2, every twisted-covariant family B_n times T(x)1 is plainly covariant under the explicit D=F(x)S, so twisted spin 3/2 reduces to the plain case', ok, f'{len(tb32)} twisted parameters')

def main():
    part_group()
    part_reps()
    coins = {nm: make_coin(nm) for nm in ('E', 'spin1', 'spin12', 'spin32')}
    part_covariant(coins)
    part_channels(coins)
    data = part_equations(coins)
    part_controls()
    part_routeA(data, coins)
    results = part_routeB(data, coins)
    part_certificates(results, data, coins)
    part_twist(coins)
    print(f'--- elapsed {time.time()-T0:.0f}s', flush=True)
    if NF == 0:
        print('HIT: characteristic-zero closure, by an independently rebuilt exact pipeline (sympy/Fractions only, raw covariance equations, no Singular), of the cubic-covariant 27-point-cell freeze for the irreducible coins E, spin 1 and spin 3/2 (and spin 1/2): every unitary walk is a constant phase; no exact dispersive counterexample exists in this class')
    print(f'TOTAL: PASS={NP} FAIL={NF}')
    print('SUMMARY: rebuilding the cubic-covariant cell-walk equations from raw covariance for the irreducible 2O coins E, spin 1, spin 1/2 and spin 3/2 and eliminating exactly over Q shows that the unitarity ideal has only the constant-phase solution (positive D4/D3 controls retain genuine moving walks), so no irreducible coin admits a moving walk on the 27-point cell.')
    return 0 if NF == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
