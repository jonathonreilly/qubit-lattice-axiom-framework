"""Reviewer's independent classification of translation-invariant O-covariant one-qubit
Clifford QCAs with single-site images in the Chebyshev ball of radius rad.

Pipeline: (1) F2 covariant space (rv_linear, own elimination), (2) exhaustive enumeration of the
space with all symplectic conditions as F2 quadratic forms, split hi/lo meet-in-the-middle,
(3) every survivor re-verified by explicit Pauli-string commutation with all overlapping
translates, (4) signs fixed by explicit phased Pauli multiplication against the signed
covariance relation for all 24 R on X_0 and Z_0.
"""
import sys, itertools, time
import numpy as np
from scipy.signal import correlate
from rv_common import O, ACTIONS, beta, mul, canon, translate, anticomm
from rv_linear import covariant_space, decode, BITS

def grid_arrays(vec, sites, rad, img):
    L = 2 * rad + 1
    xa = np.zeros((L, L, L), dtype=np.int64); za = np.zeros_like(xa)
    for i, r in enumerate(sites):
        u = (vec >> (4 * i + 2 * img)) & 1
        w = (vec >> (4 * i + 2 * img + 1)) & 1
        p = tuple(c + rad for c in r)
        xa[p] = u; za[p] = w
    return xa, za

def form(A, B):
    """array over shifts of <A, T_t B> mod 2 (full correlation)."""
    (ax, az), (bx, bz) = A, B
    return (correlate(ax, bz, mode='full', method='direct') + correlate(az, bx, mode='full', method='direct')) % 2

def classify(rad, action):
    sites, basis = covariant_space(rad, action)
    d = len(basis)
    arr = [[grid_arrays(b, sites, rad, img) for img in (0, 1)] for b in basis]
    S = 4 * rad + 1  # shifts per axis
    # g[pair][i][j] : array over shifts
    g = {}
    for (A, B) in ((0, 0), (1, 1), (0, 1)):
        G = np.zeros((d, d, S, S, S), dtype=np.int64)
        for i in range(d):
            for j in range(d):
                G[i, j] = form(arr[i][A], arr[j][B])
        g[(A, B)] = G
    centre = (2 * rad, 2 * rad, 2 * rad)
    conds = []  # (diag vec, upper-sym matrix, target)
    for (A, B), G in g.items():
        for t in itertools.product(range(S), repeat=3):
            M = G[:, :, t[0], t[1], t[2]]
            target = 1 if ((A, B) == (0, 1) and t == centre) else 0
            if not M.any() and target == 0:
                continue
            diag = np.diag(M).copy() % 2
            sym = (M + M.T) % 2
            np.fill_diagonal(sym, 0)
            conds.append((diag, sym, target))
    m = min(d, 13)
    lo_all = np.arange(1 << m, dtype=np.int64)
    lo_bits = ((lo_all[:, None] >> np.arange(m)) & 1)
    par = np.array([bin(x).count('1') & 1 for x in range(1 << m)], dtype=np.int64)
    # precompute per condition q_lo over all lo
    pre = []
    for diag, sym, target in conds:
        dl = diag[:m]; sl = np.triu(sym[:m, :m])
        qlo = (lo_bits @ dl + np.einsum('ki,ij,kj->k', lo_bits, sl, lo_bits)) % 2
        pre.append(qlo)
    sols = []
    nh = d - m
    for hi in range(1 << nh):
        hb = np.array([(hi >> k) & 1 for k in range(nh)], dtype=np.int64)
        alive = lo_all
        for (diag, sym, target), qlo in zip(conds, pre):
            dh = diag[m:]; sh = np.triu(sym[m:, m:])
            qhi = (hb @ dh + hb @ sh @ hb) % 2
            cross = (sym[:m, m:] @ hb) % 2
            mask = int(sum(int(cross[i]) << i for i in range(m)))
            val = (qhi + qlo[alive] + par[alive & mask]) % 2
            alive = alive[val == target]
            if alive.size == 0:
                break
        for lo in alive.tolist():
            c = lo | (hi << m)
            vec = 0
            for k in range(d):
                if (c >> k) & 1:
                    vec ^= basis[k]
            sols.append(vec)
    return sites, sols, d

def explicit_symplectic(PX, PZ, rad):
    """independent check by explicit commutation with all overlapping translates."""
    P = {'X': (0, PX), 'Z': (0, PZ)}
    for t in itertools.product(range(-2 * rad, 2 * rad + 1), repeat=3):
        for a, b in (('X', 'X'), ('Z', 'Z'), ('X', 'Z')):
            ac = anticomm(P[a], translate(P[b], t))
            want = 1 if (a, b) == ('X', 'Z') and t == (0, 0, 0) else 0
            if ac != want:
                return False
    return True

def signed_ok(PX, PZ, sx, sz, action):
    aX = (0 if sx > 0 else 2, PX)
    aZ = (0 if sz > 0 else 2, PZ)
    aY = mul(mul((1, {}), aX), aZ)  # Y = i X Z
    assert aY[0] in (0, 2)
    img = {'X': aX, 'Y': aY, 'Z': aZ}
    for R in O:
        for a in ('X', 'Z'):
            lhs_in = beta(R, action, (0, {(0, 0, 0): a}))
            ph, d = lhs_in
            (lab,) = d.values()
            lhs = (ph, img[lab][1]); lhs = ((ph + img[lab][0]) % 4, img[lab][1])
            rhs = beta(R, action, img[a])
            if canon(lhs) != canon(rhs):
                return False
    return True

if __name__ == '__main__':
    rad = int(sys.argv[1])
    acts = sys.argv[2:] or ACTIONS
    PASS = FAIL = 0
    for a in acts:
        t0 = time.time()
        sites, sols, d = classify(rad, a)
        nexp = 0; nsigned = 0; details = []
        for vec in sols:
            PX, PZ = decode(vec, sites)
            ok = explicit_symplectic(PX, PZ, rad)
            nexp += ok
            ns = [(sx, sz) for sx in (1, -1) for sz in (1, -1) if signed_ok(PX, PZ, sx, sz, a)]
            nsigned += len(ns)
            details.append((PX, PZ, ns))
        print(f'[{time.strftime("%H:%M:%S")}] radius {rad} action {a}: dim W={d} unsigned={len(sols)} '
              f'explicit-symplectic-ok={nexp} signed={nsigned} ({time.time()-t0:.1f}s)', flush=True)
        if nexp == len(sols): PASS += 1
        else: FAIL += 1
        if len(sols) <= 8:
            for PX, PZ, ns in details:
                print('   X ->', sorted(PX.items()), '\n   Z ->', sorted(PZ.items()), '\n   signs', ns)
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
