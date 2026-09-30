"""Assemble and solve the degree-2 linear system of test A1-planar (S1 sector)."""
import sys, time, itertools
import numpy as np
from fractions import Fraction as F
from model import *

PRIMES = (2147483629, 2147483587)


def build(R, mode='full', use=('V2', 'T3', 'G2', 'xi1', 'chi'), k=K, alpha=ALPHA, extra_rows=None):
    cols = []   # list of (label, dict)
    if 'V2' in use:
        for m in enum_V2(R):
            cols.append((('V2', m), col_V2(m, alpha)))
    if 'T3' in use:
        for m in enum_T3(R):
            cols.append((('T3', m), col_T3(m, k)))
    if 'G2' in use:
        for u in enum_G2(R):
            cols.append((('G2', u), fscale(col_G2(u, k, alpha), F(-1))))
    if 'xi1' in use:
        for u in enum_xi1(R):
            cols.append((('xi1', u), fscale(col_xi1(u), F(-1))))
    if 'chi' in use:
        for u in enum_chi(R):
            cols.append((('chi', u), fscale(col_chi(u, k), F(-1))))
    if mode == 'uniformM':
        cols = [(lab, restrict_uniform_M(d)) for lab, d in cols]
    # normalisation rows: V2 with N -> 1 equals k*R2
    norm_cols = {}
    if 'V2' in use:
        for j, (lab, d) in enumerate(cols):
            if lab[0] == 'V2':
                u = substitute_uniform(V2_of(lab[1], 'N'), 'N')
                norm_cols[j] = u
    rows = {}
    def rid(key):
        if key not in rows:
            rows[key] = len(rows)
        return rows[key]
    entries = []
    for j, (lab, d) in enumerate(cols):
        for mono, c in d.items():
            entries.append((rid(('I', mono)), j, c))
    b = {}
    if 'V2' in use:
        for j, u in norm_cols.items():
            for mono, c in u.items():
                entries.append((rid(('R', mono)), j, c))
        for mono, c in R2_S1().items():
            b[rid(('R', mono))] = k * c
    return cols, rows, entries, b


def to_dense_float(cols, rows, entries, b):
    A = np.zeros((len(rows), len(cols)))
    for i, j, c in entries:
        A[i, j] += float(c)
    bb = np.zeros(len(rows))
    for i, c in b.items():
        bb[i] = float(c)
    return A, bb


def to_mod(entries, b, nrows, ncols, p):
    A = np.zeros((nrows, ncols + 1), dtype=np.int64)
    for i, j, c in entries:
        A[i, j] = (A[i, j] + (c.numerator % p) * pow(c.denominator % p, -1, p)) % p
    for i, c in b.items():
        A[i, ncols] = (c.numerator % p) * pow(c.denominator % p, -1, p) % p
    return A


def rref_mod(A, p, ncols):
    """Row-reduce augmented A (last col = rhs) mod p. Returns (rank_coeff, consistent, pivots)."""
    A = A.copy()
    nr = A.shape[0]
    r = 0
    piv = []
    for c in range(ncols):
        if r >= nr:
            break
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), -1, p)
        A[r] = (A[r] * inv) % p
        fac = A[:, c].copy()
        fac[r] = 0
        idx = np.nonzero(fac)[0]
        if len(idx):
            A[idx] = (A[idx] - (fac[idx, None] * A[r][None, :]) % p) % p
        piv.append(c)
        r += 1
    # inconsistent iff some zero row has nonzero rhs
    bad = np.nonzero((A[:, :ncols] == 0).all(axis=1) & (A[:, ncols] != 0))[0]
    return r, len(bad) == 0, piv, A


def analyse(R, mode='full', use=('V2', 'T3', 'G2', 'xi1', 'chi'), exact=True, verbose=True):
    t0 = time.time()
    cols, rows, entries, b = build(R, mode, use)
    nr, nc = len(rows), len(cols)
    res = {'R': R, 'mode': mode, 'use': use, 'rows': nr, 'cols': nc}
    A, bb = to_dense_float(cols, rows, entries, b)
    sol, resid, rank, sv = np.linalg.lstsq(A, bb, rcond=None)
    res['float_rank'] = int(rank)
    res['float_resid'] = float(np.linalg.norm(A @ sol - bb))
    res['float_bnorm'] = float(np.linalg.norm(bb))
    if exact:
        ok = []
        for p in PRIMES[:1]:
            M = to_mod(entries, b, nr, nc, p)
            rk, cons, piv, Mred = rref_mod(M, p, nc)
            ok.append((p, rk, cons))
        res['mod'] = ok
    res['secs'] = round(time.time() - t0, 1)
    if verbose:
        print(res)
    return res, (cols, rows, entries, b, A, bb)


if __name__ == '__main__':
    R = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'full'
    analyse(R, mode)
