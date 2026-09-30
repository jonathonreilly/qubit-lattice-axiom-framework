"""T17 Test C: census of exactly conserved local parity-odd charges of a two-record sector.

Two records (distinguishable labels, exchange-symmetrised charges) on a torus Z_L^d, coin dimension c.
Ansatz for a charge (translation invariant, Hermitian, exchange-symmetric, inversion-odd):
   Q = P [ Q1 (x) 1 + 1 (x) Q1 + W ] P
   Q1 = sum_delta T(delta) (x) A_delta,  |delta|_inf <= R1, A_delta a c x c matrix
   W  = sum over (delta1, delta2, d, coin matrix unit): |s1+delta1, s2+delta2><s1, s2|, s2 = s1 + d,
        |delta_i|_1 <= 1 (own hops), |d|_inf <= RD, d != 0 (excluded) or any d (not excluded)
We count  dim{c : [H2, Q_c] = 0} - dim{c : Q_c = 0 as an operator on the pair space}.
Rank tests use two random vectors (generic).  Torus size L is chosen larger than 2*(support) so images do not alias.
"""
import itertools, sys, time, json
import numpy as np
import scipy.sparse as sp

def build(model):
    d = model['d']; L = model['L']; c = model['coin']; R1 = model['R1']; RD = model['RD']
    excl = model['excl']; soft = model.get('soft', 0.0)
    nsite = L ** d
    def s_of(p):
        idx = 0
        for a in range(d - 1, -1, -1):
            idx = idx * L + (p[a] % L)
        return idx
    pts = list(itertools.product(range(L), repeat=d))
    pts_sorted = sorted(pts, key=lambda p: s_of(p))
    site_pt = {s_of(p): p for p in pts}
    def shift(s, delta):
        p = site_pt[s]
        return s_of(tuple(p[a] + delta[a] for a in range(d)))
    def neg(s):
        p = site_pt[s]
        return s_of(tuple(-p[a] for a in range(d)))
    D1 = nsite * c
    D2 = D1 * D1
    # single-particle helpers
    def one_body(delta, A):
        rows, cols, vals = [], [], []
        for s in range(nsite):
            t = shift(s, delta)
            for a in range(c):
                for b in range(c):
                    if A[a, b] != 0:
                        rows.append(t * c + a); cols.append(s * c + b); vals.append(A[a, b])
        return sp.csr_matrix((vals, (rows, cols)), shape=(D1, D1), dtype=complex)
    # walker hopping operator h
    if model['hop'] == 'walker':
        sig = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]], dtype=complex), np.array([[1, 0], [0, -1]], dtype=complex)]
        h = sp.csr_matrix((D1, D1), dtype=complex)
        for a in range(d):
            e = tuple(1 if b == a else 0 for b in range(d)); em = tuple(-1 if b == a else 0 for b in range(d))
            h = h + one_body(e, sig[a] / (2j)) + one_body(em, -sig[a] / (2j))
        Uinv = sig[2]
    else:
        h = sp.csr_matrix((D1, D1), dtype=complex)
        for a in range(d):
            e = tuple(1 if b == a else 0 for b in range(d)); em = tuple(-1 if b == a else 0 for b in range(d))
            h = h - one_body(e, np.eye(c)) - one_body(em, np.eye(c))
        Uinv = np.eye(c)
    I1 = sp.identity(D1, dtype=complex, format='csr')
    H2full = sp.kron(h, I1, format='csr') + sp.kron(I1, h, format='csr')
    # index sets
    pair_index = np.arange(D2).reshape(D1, D1)
    s1_of = (np.arange(D2) // D1) // c
    s2_of = (np.arange(D2) % D1) // c
    exc = np.where(s1_of != s2_of)[0] if excl else np.arange(D2)
    n = len(exc)
    sel = sp.csr_matrix((np.ones(n), (np.arange(n), exc)), shape=(n, D2))
    def restrict(M):
        return (sel @ M @ sel.T).tocsr()
    H2 = restrict(H2full)
    if soft:
        # nearest-neighbour density-density interaction on the full space
        rows = []
        for s1 in range(nsite):
            for a in range(d):
                for sgn in (1, -1):
                    e = tuple(sgn if b == a else 0 for b in range(d))
                    s2 = shift(s1, e)
                    for a1 in range(c):
                        for a2 in range(c):
                            i = (s1 * c + a1) * D1 + (s2 * c + a2)
                            rows.append(i)
        Vfull = sp.csr_matrix((np.full(len(rows), soft, dtype=complex), (rows, rows)), shape=(D2, D2))
        H2 = H2 + restrict(Vfull)
    # symmetry operators on the pair space
    # exchange E: (s1,a1,s2,a2) -> (s2,a2,s1,a1)
    perm_E = np.array([ (i % D1) * D1 + (i // D1) for i in range(D2)])
    E = sp.csr_matrix((np.ones(D2), (perm_E, np.arange(D2))), shape=(D2, D2))
    # inversion I1: |s,a> -> sum_b Uinv[b,a] |-s,b>
    rows, cols, vals = [], [], []
    for s in range(nsite):
        for a in range(c):
            for b in range(c):
                if Uinv[b, a] != 0:
                    rows.append(neg(s) * c + b); cols.append(s * c + a); vals.append(Uinv[b, a])
    Iop1 = sp.csr_matrix((vals, (rows, cols)), shape=(D1, D1), dtype=complex)
    Ipair = sp.kron(Iop1, Iop1, format='csr')
    E_r = restrict(E); I_r = restrict(Ipair)
    # check symmetry of H2
    def comm_norm(A, B):
        C = A @ B - B @ A
        return abs(C).max() if C.nnz else 0.0
    sym_err = (comm_norm(H2, E_r), comm_norm(H2, I_r))
    # generators
    gens = []; labels = []
    def add_generator(M, label):
        M = restrict(M)
        for herm in (M + M.getH(), 1j * (M - M.getH())):
            herm = herm.tocsr()
            herm.eliminate_zeros()
            if herm.nnz == 0: continue
            # exchange-symmetrise, then inversion-odd part
            g = 0.5 * (herm + E_r @ herm @ E_r.T)
            g = 0.5 * (g - I_r @ g @ I_r.getH())
            g.eliminate_zeros()
            if g.nnz == 0 or abs(g).max() < 1e-12: continue
            gens.append(g); labels.append(label)
    coin_units = [np.zeros((c, c), dtype=complex) for _ in range(c * c)]
    for k in range(c * c):
        coin_units[k][k // c, k % c] = 1.0
    # one-body ansatz
    deltas = [dl for dl in itertools.product(range(-R1, R1 + 1), repeat=d)]
    for dl in deltas:
        for k in range(c * c):
            Ob = one_body(dl, coin_units[k])
            M = sp.kron(Ob, I1, format='csr') + sp.kron(I1, Ob, format='csr')
            add_generator(M, ('one', dl, k))
    n_one = len(gens)
    # two-body ansatz
    hops = [tuple(0 for _ in range(d))]
    for a in range(d):
        for m in range(1, model.get('WH', 1) + 1):
            for sgn in (1, -1):
                hops.append(tuple(sgn * m if b == a else 0 for b in range(d)))
    dvals = [dv for dv in itertools.product(range(-RD, RD + 1), repeat=d) if (not excl or any(dv))]
    c2 = c * c
    for d1 in hops:
        for d2 in hops:
            for dv in dvals:
                for k1 in range(c2):
                    for k2 in range(c2):
                        rows, cols, vals = [], [], []
                        for s1 in range(nsite):
                            s2 = shift(s1, dv)
                            t1 = shift(s1, d1); t2 = shift(s2, d2)
                            a1p, a1 = divmod(k1, c); a2p, a2 = divmod(k2, c)
                            rows.append((t1 * c + a1p) * D1 + (t2 * c + a2p))
                            cols.append((s1 * c + a1) * D1 + (s2 * c + a2))
                            vals.append(1.0)
                        M = sp.csr_matrix((vals, (rows, cols)), shape=(D2, D2), dtype=complex)
                        add_generator(M, ('two', d1, d2, dv, k1, k2))
    return dict(H2=H2, gens=gens, labels=labels, n=n, n_one=n_one, sym_err=sym_err, model=model, restrict=restrict, E=E_r, I=I_r, D2=D2)

def census(model, nvec=2, seed=1, tol=1e-9):
    t0 = time.time()
    B = build(model)
    H2, gens, n = B['H2'], B['gens'], B['n']
    rng = np.random.default_rng(seed)
    ncol = len(gens)
    print(f"[{model['name']}] pair-space dim {n}, generators {ncol} (one-body {B['n_one']}), symmetry errors {B['sym_err']}, build {time.time()-t0:.1f}s", flush=True)
    Ga = np.zeros((ncol, ncol)); Gb = np.zeros((ncol, ncol))
    for v_ in range(nvec):
        v = rng.normal(size=n) + 1j * rng.normal(size=n)
        Hv = H2 @ v
        A = np.empty((n, ncol), dtype=complex); Bm = np.empty((n, ncol), dtype=complex)
        for i, g in enumerate(gens):
            gv = g @ v
            A[:, i] = H2 @ gv - g @ Hv
            Bm[:, i] = gv
        Ga += (A.conj().T @ A).real; Gb += (Bm.conj().T @ Bm).real
        del A, Bm
    wa = np.linalg.eigvalsh(Ga); wb = np.linalg.eigvalsh(Gb)
    sa = wa.max(); sb = wb.max()
    na = int((wa < tol * sa).sum()); nb = int((wb < tol * sb).sum())
    # eigenvalue gap diagnostic
    def gap(w, k, s):
        ws = np.sort(w)
        lo = ws[k - 1] / s if k > 0 else 0.0
        hi = ws[k] / s if k < len(ws) else 1.0
        return lo, hi
    res = dict(name=model['name'], pair_dim=n, generators=ncol, null_comm=na, null_op=nb, nontrivial=na - nb,
               gap_comm=gap(wa, na, sa), gap_op=gap(wb, nb, sb), seconds=round(time.time() - t0, 1))
    print('   ', res, flush=True)
    return res

MODELS = {
    'scalar1d_excl':  dict(name='scalar1d_excl',  d=1, L=11, coin=1, hop='scalar', R1=2, RD=2, excl=True, WH=2),
    'scalar1d_free':  dict(name='scalar1d_free',  d=1, L=11, coin=1, hop='scalar', R1=2, RD=2, excl=False, WH=2),
    'scalar2d_free':  dict(name='scalar2d_free',  d=2, L=7,  coin=1, hop='scalar', R1=2, RD=2, excl=False),
    'scalar2d_excl':  dict(name='scalar2d_excl',  d=2, L=7,  coin=1, hop='scalar', R1=2, RD=2, excl=True),
    'scalar2d_soft':  dict(name='scalar2d_soft',  d=2, L=7,  coin=1, hop='scalar', R1=2, RD=2, excl=False, soft=0.7),
    'walker1d_excl':  dict(name='walker1d_excl',  d=1, L=11, coin=2, hop='walker', R1=2, RD=2, excl=True, WH=2),
    'walker1d_free':  dict(name='walker1d_free',  d=1, L=11, coin=2, hop='walker', R1=2, RD=2, excl=False, WH=2),
    'walker2d_free':  dict(name='walker2d_free',  d=2, L=7,  coin=2, hop='walker', R1=2, RD=1, excl=False),
    'walker2d_excl':  dict(name='walker2d_excl',  d=2, L=7,  coin=2, hop='walker', R1=2, RD=1, excl=True),
    'walker2d_soft':  dict(name='walker2d_soft',  d=2, L=7,  coin=2, hop='walker', R1=2, RD=1, excl=False, soft=0.7),
}

if __name__ == '__main__':
    names = sys.argv[1:] or list(MODELS)
    out = []
    for nm in names:
        out.append(census(MODELS[nm]))
        json.dump(out, open('C_results_' + '_'.join(names)[:60] + '.json', 'w'), default=str)
