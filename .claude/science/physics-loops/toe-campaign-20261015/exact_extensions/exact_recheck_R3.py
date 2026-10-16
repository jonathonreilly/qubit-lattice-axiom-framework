import pickle, itertools, sympy as sp, time
t0=time.time()
d = pickle.load(open('fastR3_O_3.pkl', 'rb'))
L, keys, lines = d['L'], d['keys'], d['lines']
print('lines', lines, flush=True)
Nl = L.T.nullspace(); Nm = sp.Matrix.hstack(*Nl).T
print('left null', Nm.shape, time.time()-t0, flush=True)
def cls(b): return sum(b)
deg = {be: max(abs(m) for (b2, k, m) in keys if b2 == be) for be in lines}
gam = [be for be in lines if be[0] == (0, 0, 0)]
rest = [be for be in lines if be[0] != (0, 0, 0)]
def target(ns, eps):
    t = []
    for (be, kind, m) in keys:
        n = ns[be]; ep = eps[cls(be[0])]
        t.append(ep * (sp.Rational(1, 2) * ((m == n) + (m == -n)) if kind == 'f' else (sp.Integer(1) / (2 * sp.I)) * ((m == n) - (m == -n))))
    return sp.Matrix(t)
feas = []; cnt = 0
classes = sorted({cls(be[0]) for be in rest})
for sg in itertools.product((1, -1), repeat=len(classes)):
    eps = {0: 1, **dict(zip(classes, sg))}
    for nr in itertools.product(*[range(-deg[be], deg[be] + 1) for be in rest]):
        ns = {**{be: 0 for be in gam}, **dict(zip(rest, nr))}
        v = (Nm * target(ns, eps)).applyfunc(lambda x: sp.nsimplify(sp.expand(x)))
        cnt += 1
        if v.is_zero_matrix: feas.append((nr, sg))
print('checked', cnt, 'exact feasible', feas, time.time()-t0, flush=True)
