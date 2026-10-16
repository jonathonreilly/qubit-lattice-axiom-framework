"""Fast exact line-branch certificate at range R (Fourier-dictionary arithmetic).

usage: python3 fastR.py R [GROUP]
"""
import itertools, sys, time, pickle
from collections import defaultdict
import sympy as sp
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_qubit_walk_cell_classification_2026_10_16 as cell

C, S = cell.C, cell.S
R = int(sys.argv[1]); GNAME = sys.argv[2] if len(sys.argv) > 2 else 'O'
H = cell.proper_cubic() if GNAME == 'O' else cell.closure(cell.GROUPS[GNAME])
t0 = time.time()
def log(*a): print(f'[{time.time()-t0:7.1f}s]', *a, flush=True)

per = [[sp.Integer(1)] + [sp.expand(sp.chebyshevt(n, C[a])) for n in range(1, R + 1)]
       + [sp.expand(S[a] * sp.chebyshevu(n - 1, C[a])) for n in range(1, R + 1)] for a in range(3)]
funcs = [sp.expand(x * y * z) for x, y, z in itertools.product(*per)]
import os
cache = f'bases_{GNAME}_{R}.pkl'
if os.path.exists(cache):
    fb, gb = pickle.load(open(cache, 'rb'))
else:
    fb = cell.scalar_basis(H, funcs); gb = cell.vector_basis(H, funcs, 'full')
    pickle.dump((fb, gb), open(cache, 'wb'))
log('scalars', len(fb), 'vectors', len(gb))

Zs = sp.symbols('z1:4')
def fourier(expr):
    sub = {}
    for a in range(3):
        sub[C[a]] = (Zs[a] + 1 / Zs[a]) / 2; sub[S[a]] = (Zs[a] - 1 / Zs[a]) / (2 * sp.I)
    e = sp.expand(sp.sympify(expr).subs(sub, simultaneous=True) * (Zs[0] * Zs[1] * Zs[2]) ** R)
    if e == 0: return {}
    P = sp.Poly(e, *Zs)
    return {tuple(m - R for m in mon): sp.nsimplify(cf) for mon, cf in P.terms()}

Fd = [fourier(x) for x in fb]
Gd = [[fourier(x) for x in v] for v in gb]
log('fourier done')
nA, nB = len(Fd), len(Gd)
X = sp.symbols(f'x0:{nA + nB}')

def conv(d1, d2):
    out = defaultdict(lambda: sp.Integer(0))
    for n1, c1 in d1.items():
        for n2, c2 in d2.items():
            out[(n1[0] + n2[0], n1[1] + n2[1], n1[2] + n2[2])] += c1 * c2
    return out

# unitarity: sum_ij x_i x_j <F_i F_j> + sum_ij y_i y_j sum_a <G_ia G_ja> = delta_0
quad = defaultdict(lambda: defaultdict(lambda: sp.Integer(0)))   # offset -> (i,j) -> coeff
for i in range(nA):
    for j in range(i, nA):
        w = 1 if i == j else 2
        for n, cf in conv(Fd[i], Fd[j]).items():
            quad[n][(i, j)] += w * cf
for i in range(nB):
    for j in range(i, nB):
        w = 1 if i == j else 2
        for a in range(3):
            for n, cf in conv(Gd[i][a], Gd[j][a]).items():
                quad[n][(nA + i, nA + j)] += w * cf
eqs = []
for n, terms in quad.items():
    e = sum(sp.expand(cf) * X[i] * X[j] for (i, j), cf in terms.items()) - (1 if n == (0, 0, 0) else 0)
    e = sp.expand(e)
    if e != 0:
        eqs.append(e)
log('unitarity equations', len(eqs))

# lines k = base + t e, base a TRIM (entries in units of pi)
def mod2(v): return tuple(int(x) % 2 for x in v)
def stab_point(b): return [M for M in H if mod2(M * sp.Matrix(b)) == tuple(b)]
def fixes_only(st, e):
    if len(st) < 2: return False
    fix = sp.Matrix.vstack(*[M - sp.eye(3) for M in st]).nullspace()
    return len(fix) == 1 and sp.Matrix.hstack(fix[0], sp.Matrix(e)).rank() == 1
def no_fix_on_line(st, e):
    # does Stab(b) fix any nonzero multiple of e?  (fix space of st intersected with span(e))
    v = sp.Matrix(e)
    return not all((M * v - v).is_zero_matrix for M in st)
seen, lines = set(), []
for b in itertools.product((0, 1), repeat=3):
    for e in itertools.product((-1, 0, 1), repeat=3):
        if not any(e): continue
        geo = frozenset([(mod2(b), e), (mod2(b), tuple(-x for x in e)), (mod2([b[k] + e[k] for k in range(3)]), e), (mod2([b[k] + e[k] for k in range(3)]), tuple(-x for x in e))])
        if any(g_ in seen for g_ in geo): continue
        # mark the whole O-orbit of this line as seen
        for M in H:
            bb = mod2(M * sp.Matrix(b)); ee = tuple(int(x) for x in M * sp.Matrix(e))
            for x in [(bb, ee), (bb, tuple(-y for y in ee)), (mod2([bb[k] + ee[k] for k in range(3)]), ee), (mod2([bb[k] + ee[k] for k in range(3)]), tuple(-y for y in ee))]:
                seen.add(x)
        st_line = [M for M in H if list(M * sp.Matrix(e)) == list(e) and mod2(M * sp.Matrix(b)) == tuple(b)]
        if not fixes_only(st_line, e): continue
        # need g = 0 at one end: try base b, else base b + e
        for base in (tuple(b), mod2([b[k] + e[k] for k in range(3)])):
            if no_fix_on_line(stab_point(base), e):
                lines.append((base, e)); break
log('lines (base in units of pi, direction)', lines)
def cls(b): return sum(b)   # 0 Gamma, 1 X, 2 M, 3 R

def line_rows(be):
    base, e = be
    norm = sp.sqrt(sum(x * x for x in e))
    fr, gr = defaultdict(lambda: [0] * (nA + nB)), defaultdict(lambda: [0] * (nA + nB))
    for i, d in enumerate(Fd):
        for n, cf in d.items():
            ph = (-1) ** (sum(a * b for a, b in zip(n, base)) % 2)
            m = sum(a * b for a, b in zip(n, e)); fr[m][i] += ph * cf
    for i, v in enumerate(Gd):
        for a in range(3):
            if e[a] == 0: continue
            for n, cf in v[a].items():
                ph = (-1) ** (sum(x * y for x, y in zip(n, base)) % 2)
                m = sum(x * y for x, y in zip(n, e)); gr[m][nA + i] += ph * cf * e[a] / norm
    return fr, gr

rows, keys = [], []
deg = {}
for be in lines:
    fr, gr = line_rows(be)
    ms = sorted(set(fr) | set(gr)); deg[be] = max(abs(m) for m in ms)
    for m in ms:
        rows.append(fr.get(m, [0] * (nA + nB))); keys.append((be, 'f', m))
        rows.append(gr.get(m, [0] * (nA + nB))); keys.append((be, 'g', m))
L = sp.Matrix(rows).applyfunc(sp.nsimplify)
log('line system', L.shape, 'rank', L.rank(), 'degrees', deg)
Nl = L.T.nullspace()
log('left null space dim', len(Nl))
Nm = sp.Matrix.hstack(*Nl).T if Nl else sp.zeros(0, L.rows)

def target(br):
    ns, eps = br   # eps: dict class -> sign
    t = []
    for (be, kind, m) in keys:
        n = ns[lines.index(be)]
        ep = eps[cls(be[0])]
        if kind == 'f': t.append(ep * sp.Rational(1, 2) * ((m == n) + (m == -n)))
        else: t.append(ep * (sp.Integer(1) / (2 * sp.I)) * ((m == n) - (m == -n)))
    return sp.Matrix(t)

import numpy as np
Nn = np.array(Nm.evalf(30).tolist(), dtype=complex) if Nm.rows else np.zeros((0, L.rows))
def line_target(li, n, eps):
    t = np.zeros(L.rows, dtype=complex)
    for r, (be, kind, m) in enumerate(keys):
        if be != lines[li]: continue
        if kind == 'f': t[r] = eps * 0.5 * ((m == n) + (m == -n))
        else: t[r] = eps * (1 / 2j) * ((m == n) - (m == -n))
    return t
classes = sorted({cls(be[0]) for be in lines} - {0})
rowsof = {be: [r for r, k in enumerate(keys) if k[0] == be] for be in lines}
Ln = np.array(L.evalf(30).tolist(), dtype=complex)
def tvec(be, n, ep):
    t = np.zeros(len(keys), dtype=complex)
    for r in rowsof[be]:
        _, kind, m = keys[r]
        t[r] = ep * (0.5 * ((m == n) + (m == -n)) if kind == 'f' else (1 / 2j) * ((m == n) - (m == -n)))
    return t
def consistent(rows, t):
    A = Ln[rows]; bvec = t[rows]
    x, *_ = np.linalg.lstsq(A, bvec, rcond=None)
    return np.abs(A @ x - bvec).max() < 1e-9
feas = []
for sg in itertools.product((1, -1), repeat=len(classes)):
    eps = {0: 1, **dict(zip(classes, sg))}
    partial = [((), np.zeros(len(keys), dtype=complex), [])]
    for be in lines:
        new_p = []
        for ns, t, rows in partial:
            for n in range(-deg[be], deg[be] + 1):
                t2 = t + tvec(be, n, eps[cls(be[0])]); r2 = rows + rowsof[be]
                if consistent(r2, t2): new_p.append((ns + (n,), t2, r2))
        partial = new_p
    for ns, t, rows in partial:
        if (Nm * target((ns, eps))).applyfunc(sp.simplify).is_zero_matrix:
            feas.append((ns, tuple(sorted(eps.items()))))
log('feasible branches', len(feas), 'of', sp.prod([2 * deg[e] + 1 for e in lines]) * 2 ** len(classes), feas)
pickle.dump({'eqs': eqs, 'L': L, 'keys': keys, 'lines': lines, 'feas': feas, 'nA': nA, 'nB': nB}, open(f'fastR3_{GNAME}_{R}.pkl', 'wb'))
for ns in feas:
    sol = sp.linsolve((L, target((ns[0], dict(ns[1])))), list(X))
    sub = dict(zip(X, next(iter(sol))))
    ns = ns
    free = sorted(set().union(*[sp.sympify(v).free_symbols for v in sub.values()]), key=str)
    red = [e for e in (sp.expand(e.subs(sub)) for e in eqs) if e != 0]
    log(f'branch {ns}: {len(free)} free, {len(red)} equations; writing Singular input')
    pickle.dump({'sub': sub, 'free': free, 'red': red}, open(f'fastR3_{GNAME}_{R}_branch_{abs(hash(ns))}.pkl', 'wb'))
    if len(free) <= 12:
        G = sp.groebner(red, *free, order='grevlex')
        nil = [v for v in free if any(G.contains(v ** p) for p in range(1, 7))]
        log(f'branch {ns}: groebner size {len(G.exprs)}; nilpotent {len(nil)}/{len(free)}; is [1]: {G.exprs == [1]}')
