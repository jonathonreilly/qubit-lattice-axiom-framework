"""Exact line-branch test for O-covariant cell walks with an irreducible spin-j coin (j = 1/2 or 3/2).

usage: python3 spinj_exact.py J   (J = 1/2 or 3/2)
"""
import itertools, sys, time, pickle
import sympy as sp
from sympy.physics.quantum.spin import Rotation

t0 = time.time()
def log(*a): print(f'[{time.time()-t0:7.1f}s]', *a, flush=True)
REP = sys.argv[1]
j = sp.Rational(REP) if REP != 'E' else sp.Rational(1, 2)
ms = [j - k for k in range(int(2 * j) + 1)]
d = len(ms)
Jz = sp.diag(*ms)
Jp = sp.zeros(d)
for i in range(1, d):
    Jp[i - 1, i] = sp.sqrt(j * (j + 1) - ms[i] * (ms[i] + 1))
Jx = (Jp + Jp.H) / 2; Jy = (Jp - Jp.H) / (2 * sp.I)

def wigner_D(alpha, beta, gamma):
    return sp.Matrix(d, d, lambda a, b: sp.nsimplify(sp.simplify(Rotation.D(j, ms[a], ms[b], alpha, beta, gamma).doit())))

# quarter turns: about z by pi/2 and about x by pi/2 (x-rotation = Rz(-pi/2) Ry(pi/2) Rz(pi/2))
Dz = sp.diag(*[sp.exp(-sp.I * sp.pi / 2 * m) for m in ms]).applyfunc(sp.nsimplify)
Dx = (Jx * 0 + sp.eye(d))
# exact exp(-i pi/2 Jx) via eigen-decomposition
P, Dg = Jx.diagonalize(normalize=True)
Dx = (P * sp.diag(*[sp.exp(-sp.I * sp.pi / 2 * Dg[k, k]) for k in range(d)]) * P.H).applyfunc(lambda x: sp.nsimplify(sp.simplify(x)))
assert (Dx * Dx.H - sp.eye(d)).applyfunc(sp.simplify).is_zero_matrix
RZ = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); RX = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
if REP == 'E':
    Bs = sp.Matrix([[1, 1], [-1, 1], [0, -2]]) * sp.diag(1 / sp.sqrt(2), 1 / sp.sqrt(6))   # orthonormal basis of sum-zero plane
    perm = lambda R: R.applyfunc(abs)
    Dz = (Bs.T * perm(RZ) * Bs).applyfunc(sp.nsimplify); Dx = (Bs.T * perm(RX) * Bs).applyfunc(sp.nsimplify)
    d = 2
    assert (Dz * Dz.T - sp.eye(2)).is_zero_matrix and (Dx * Dx.T - sp.eye(2)).is_zero_matrix
# covariance check of the lift: D J_a D^dag = sum_b R_ba J_b
for R, D in (((RZ, Dz), (RX, Dx)) if REP != 'E' else ()):
    for a, Ja in enumerate((Jx, Jy, Jz)):
        lhs = (D * Ja * D.H).applyfunc(sp.simplify)
        rhs = sum((R[b, a] * Jb for b, Jb in enumerate((Jx, Jy, Jz))), sp.zeros(d))
        assert (lhs - rhs).applyfunc(sp.simplify).is_zero_matrix, (R, a)
log('lift checked')
# group closure (rotation, lift); conjugation is insensitive to the lift sign
key = lambda M: tuple(int(x) for x in M)
G = {key(sp.eye(3)): (sp.eye(3), sp.eye(d))}
frontier = list(G.values())
while frontier:
    nxt = []
    for R, D in frontier:
        for R2, D2 in ((RZ, Dz), (RX, Dx)):
            R3 = R * R2; k3 = key(R3)
            if k3 not in G:
                G[k3] = (R3, (D * D2).applyfunc(sp.nsimplify)); nxt.append(G[k3])
    frontier = nxt
G = list(G.values()); assert len(G) == 24
log('group', len(G))

cell = [tuple(v) for v in itertools.product((-1, 0, 1), repeat=3)]
# orbit representatives and stabiliser-commutant parametrisation
params = []
A = {}
done = set()
for n in cell:
    if n in done: continue
    st = [D for R, D in G if key(R * sp.Matrix(n)) == n]
    # commutant: X with D X D^dag = X for all stabiliser lifts
    xs = sp.symbols(f'u{len(params)}_0:{d*d}')
    X = sp.Matrix(d, d, xs)
    eqs = []
    for D in st:
        eqs += list((D * X - X * D).applyfunc(sp.expand))
    sol = sp.solve(eqs, xs, dict=True)[0] if any(e != 0 for e in eqs) else {}
    Xs = X.subs(sol)
    fr = sorted(Xs.free_symbols, key=str)
    newp = sp.symbols(f'p{len(params)}:{len(params) + len(fr)}')
    Xs = Xs.subs(dict(zip(fr, newp)))
    params += list(newp)
    for R, D in G:
        m = key(R * sp.Matrix(n))
        if m not in A:
            A[m] = (D * Xs * D.H).applyfunc(sp.expand)
        done.add(m)
log('complex parameters', len(params))

# unitarity: sum_n A_n A_{n-m}^dag = delta I, with p = x + i y
xr = sp.symbols(f'x0:{len(params)}', real=True); yr = sp.symbols(f'y0:{len(params)}', real=True)
cs = {p: x + sp.I * y for p, x, y in zip(params, xr, yr)}
Ac = {n: M.subs(cs) for n, M in A.items()}
eqs = set()
diffs = {tuple(a - b for a, b in zip(n1, n2)) for n1 in cell for n2 in cell}
for m in diffs:
    acc = sp.zeros(d)
    for n in cell:
        n2 = tuple(a - b for a, b in zip(n, m))
        if n2 in Ac:
            acc += Ac[n] * Ac[n2].H
    if m == (0, 0, 0): acc -= sp.eye(d)
    for e in acc:
        e = sp.expand(e)
        for part in (sp.re(e), sp.im(e)):
            part = sp.expand(part)
            if part != 0: eqs.add(part)
eqs = list(eqs)
log('real unitarity equations', len(eqs), 'real unknowns', 2 * len(params))

# axis-line lemma in the J_x eigenbasis: U(t e_x) = sum_r z^r B_r, B_r = sum_{n_x = r} A_n
Px, Dgx = (Dx if REP == 'E' else Jx).diagonalize(normalize=True)
Pxs = [Px[:, k] * Px[:, k].H for k in range(d)]   # projectors, eigenvalues Dgx[k,k] distinct
assert len(set(Dgx[k, k] for k in range(d))) == d
B = {r: sum((Ac[n] for n in cell if n[0] == r), sp.zeros(d)) for r in (-1, 0, 1)}
# body diagonal: C3 about (1,1,1); 1-dim eigenspaces give monomials
C3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
D3 = [D for R, D in G if key(R) == key(C3)][0]
ev = D3.eigenvects()
ones = [(val, vecs[0]) for val, mult, vecs in ev if mult == 1]
log('C3 eigenvalue multiplicities', [mult for _, mult, _ in ev])
Pb = []
for val, v in ones:
    v = v / sp.sqrt((v.H * v)[0]); Pb.append((v * v.H).applyfunc(sp.simplify))
Bb = {r: sum((Ac[n] for n in cell if sum(n) == r), sp.zeros(d)) for r in range(-3, 4)}
lin_axis = {}
def axis_eqs_raw(mvec):
    E = []
    for r in (-1, 0, 1):
        target = sum((Pxs[k] for k in range(d) if mvec[k] == r), sp.zeros(d))
        for e in (B[r] - target):
            e = sp.expand(e)
            E += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    return E
def axis_eqs(mvec):
    E = []
    for r in (-1, 0, 1):
        target = sum((Pxs[k] for k in range(d) if mvec[k] == r), sp.zeros(d))
        for e in (B[r] - target):
            e = sp.expand(e)
            E += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    return [e for e in E if e != 0]
Tb = {(k, r): sp.expand(sp.simplify((P1 * Bb[r] * P1).trace())) for k, P1 in enumerate(Pb) for r in range(-3, 4)}
log('body traces')
def body_eqs_raw(pvec):
    E = []
    for k, p in enumerate(pvec):
        for r in range(-3, 4):
            e = sp.expand(Tb[(k, r)] - (1 if r == p else 0))
            E += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    return E
def body_eqs(pvec):
    E = []
    for k, p in enumerate(pvec):
        for r in range(-3, 4):
            e = sp.expand(Tb[(k, r)] - (1 if r == p else 0))
            E += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    return [e for e in E if e != 0]
unk = list(xr) + list(yr)

if len(sys.argv) > 2 and sys.argv[2] == 'exact':
    # exact recheck: L x = t(branch); branch consistent iff N t = 0 for the left null space N of L
    allE = []
    keys = []
    for mvec in itertools.product((-1, 0, 1), repeat=d):
        pass
    def lin_parts(E):
        rows, rhs = [], []
        for e in E:
            P = sp.Poly(e, *unk); row = [0] * len(unk); c0 = 0
            for mon, c in P.terms():
                if sum(mon) == 0: c0 = c
                else: row[mon.index(1)] = c
            rows.append(row); rhs.append(-c0)
        return rows, rhs
    # the coefficient rows do not depend on the branch; only the right-hand side does
    zero_axis = axis_eqs_raw((0,) * d)
    zero_body = body_eqs_raw((0,) * len(Pb))
    rows_a, _ = lin_parts([sp.expand(e) for e in zero_axis]); rows_b, _ = lin_parts([sp.expand(e) for e in zero_body])
    Lm = sp.Matrix(rows_a + rows_b)
    Nl = Lm.T.nullspace(); N = sp.Matrix.hstack(*Nl).T
    log('exact left null space', N.shape)
    canon = lambda x: sp.nsimplify(sp.radsimp(sp.expand(x)))
    na = len(zero_axis)
    va = {}
    for mvec in itertools.product((-1, 0, 1), repeat=d):
        _, ra = lin_parts([sp.expand(e) for e in axis_eqs_raw(mvec)])
        va[mvec] = (N[:, :na] * sp.Matrix(ra)).applyfunc(canon)
    log('axis vectors', len(va))
    vb = {}
    for pvec in itertools.product(range(-3, 4), repeat=len(Pb)):
        _, rb = lin_parts([sp.expand(e) for e in body_eqs_raw(pvec)])
        vb[pvec] = (N[:, na:] * sp.Matrix(rb)).applyfunc(canon)
    log('body vectors', len(vb))
    ok = []
    for mvec, a_ in va.items():
        for pvec, b_ in vb.items():
            if (a_ + b_).applyfunc(canon).is_zero_matrix:
                ok.append((mvec, pvec))
    log('exactly consistent branches', ok)
    sys.exit(0)
import numpy as np
def to_num(E):
    A = np.zeros((len(E), len(unk))); b = np.zeros(len(E))
    for r, e in enumerate(E):
        P = sp.Poly(e, *unk)
        for mon, c in P.terms():
            if sum(mon) == 0: b[r] = -float(sp.N(c, 30))
            else: A[r, mon.index(1)] = float(sp.N(c, 30))
    return A, b
def consistent(E):
    if not E: return True
    A, b = to_num(E)
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    return np.abs(A @ x - b).max() < 1e-9
axis_cache = {m: axis_eqs(m) for m in itertools.product((-1, 0, 1), repeat=d)}
log('axis cache')
body_cache = {p: body_eqs(p) for p in itertools.product(range(-3, 4), repeat=len(Pb))}
log('body cache')
num_axis = {k: to_num(v) if v else (np.zeros((0, len(unk))), np.zeros(0)) for k, v in axis_cache.items()}
num_body = {k: to_num(v) if v else (np.zeros((0, len(unk))), np.zeros(0)) for k, v in body_cache.items()}
log('numeric caches')
def ncons(A, b):
    if len(b) == 0: return True
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    return np.abs(A @ x - b).max() < 1e-9
feas = []
for mvec, Ea in axis_cache.items():
    if not ncons(*num_axis[mvec]): continue
    for pvec, Eb in body_cache.items():
        E = Ea + Eb
        if ncons(np.vstack([num_axis[mvec][0], num_body[pvec][0]]), np.concatenate([num_axis[mvec][1], num_body[pvec][1]])):
            log('numerically feasible', mvec, pvec); sol = sp.solve(E, unk, dict=True)
            if sol:
                s0 = sol[0]
                feas.append((mvec, pvec, [s0.get(u, u) for u in unk]))
            else:
                log('numerically consistent but exact solve failed', mvec, pvec)
log('feasible branches', len(feas), [(f[0], f[1]) for f in feas])
pickle.dump({'eqs': eqs, 'unk': unk, 'feas': feas}, open(f'spinj_{REP.replace("/", "_")}.pkl', 'wb'))
for mvec, pvec, sol in feas:
    sub = dict(zip(unk, sol))
    free = sorted(set().union(*[sp.sympify(v).free_symbols for v in sol]), key=str)
    red = [e for e in (sp.expand(e.subs(sub)) for e in eqs) if e != 0]
    moving = any(sp.expand(sp.sympify(sub[u])) != 0 for u in unk) or True
    log(f'branch {mvec} {pvec}: {len(free)} free, {len(red)} eqs')
    if len(free) <= 10 and red:
        Gb = sp.groebner(red, *free, order='grevlex')
        log(f'   groebner {Gb.exprs == [1] and "INFEASIBLE" or "size %d" % len(Gb.exprs)}')
