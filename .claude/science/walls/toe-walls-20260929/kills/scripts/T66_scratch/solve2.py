"""Degree-2 identity + continuum-limit (ADM frame) matching rows. Solve and report."""
import sys, time
import numpy as np
from fractions import Fraction as F
from collections import defaultdict
from solve import *
from match import *
from refs import REF

LEVELS = {'V2': (0, 1, 2), 'T3': (0,), 'G2': (0, 1), 'xi1': (0, 1, 2), 'chi': (0, 1, 2, 3)}
NPTS = {3: 10, 4: 16}


def lattice_fun(lab):
    fam, u = lab
    if fam == 'V2':
        return V2_of(u, 'N'), {}
    if fam == 'T3':
        return T3_of(u, 'N'), {}
    if fam == 'G2':
        c, d, i, j = u
        # density xi(bond 0 @ 0.5) P_c(i) h_d(j): return raw monomial, positions include X at half
        return {(('X', 0, F(1, 2)), ('P', c, F(i)), ('h', d, F(j))): F(1)}, {'raw': True}
    if fam == 'xi1':
        return col_xi1(u), {}
    if fam == 'chi':
        return col_chi(u), {}


def slots_of(mono):
    # returns list of ((kind,comp) label, pos) ordered by label
    sl = [((v[0], v[1]), F(v[2])) for v in mono]
    sl.sort(key=lambda t: t[0])
    return sl


def match_rows(cols, fams=('V2', 'T3', 'G2', 'xi1', 'chi'), levels=LEVELS, seed=7):
    """Return list of (dict{col_index: coef}, rhs)."""
    rows = []
    # gather lattice functionals per column
    bytype = defaultdict(lambda: defaultdict(list))   # (fam,type) -> col -> list of (coef, slots)
    for j, (lab, _) in enumerate(cols):
        fam = lab[0]
        if fam not in fams:
            continue
        fun, info = lattice_fun(lab)
        for mono, c in fun.items():
            sl = slots_of(mono)
            typ = tuple(t[0] for t in sl)
            bytype[(fam, typ)][j].append((c, sl))
    # continuum targets per (fam,type)
    tgt = defaultdict(list)
    for fam in fams:
        for coef, slots in REF.get(fam, []):
            sl = sorted(slots, key=lambda t: t[0])
            typ = tuple(t[0] for t in sl)
            tgt[(fam, typ)].append((coef, sl))
    keys = set(bytype.keys()) | set(tgt.keys())
    for (fam, typ) in sorted(keys, key=str):
        m = len(typ)
        pts = hyperplane_points(m, NPTS.get(m, 16), seed=seed)
        for D in levels[fam]:
            for ks in pts:
                row = {}
                for j, lst in bytype.get((fam, typ), {}).items():
                    v = sum(c * sym_lattice(sl, ks, D) for c, sl in lst)
                    if v != 0:
                        row[j] = v
                rhs = F(0)
                for coef, sl in tgt.get((fam, typ), []):
                    if sum(n for _, n in sl) == D:
                        rhs += sym_cont(coef, sl, ks)
                if row or rhs != 0:
                    rows.append((row, rhs))
    return rows


def run(R, fams=('V2', 'T3', 'G2', 'xi1', 'chi'), use=('V2', 'T3', 'G2', 'xi1', 'chi'), verbose=True):
    t0 = time.time()
    cols, rows_d, entries, b = build(R, 'full', use)
    mrows = match_rows(cols, fams)
    nr0 = len(rows_d)
    entries = list(entries)
    b = dict(b)
    for r, (row, rhs) in enumerate(mrows):
        ri = nr0 + r
        for j, v in row.items():
            entries.append((ri, j, v))
        if rhs != 0:
            b[ri] = rhs
    nr = nr0 + len(mrows)
    nc = len(cols)
    A = np.zeros((nr, nc)); bb = np.zeros(nr)
    for i, j, c in entries:
        A[i, j] += float(c)
    for i, c in b.items():
        bb[i] = float(c)
    sol, resid, rank, sv = np.linalg.lstsq(A, bb, rcond=None)
    r_float = float(np.linalg.norm(A @ sol - bb))
    out = {'R': R, 'rows_identity': nr0, 'rows_match': len(mrows), 'cols': nc, 'float_rank': int(rank), 'float_resid': r_float, 'bnorm': float(np.linalg.norm(bb))}
    # exact mod p
    for p in PRIMES[:1]:
        M = np.zeros((nr, nc + 1), dtype=np.int64)
        for i, j, c in entries:
            M[i, j] = (M[i, j] + (c.numerator % p) * pow(c.denominator % p, -1, p)) % p
        for i, c in b.items():
            M[i, nc] = (c.numerator % p) * pow(c.denominator % p, -1, p) % p
        rk, cons, piv, Mred = rref_mod(M, p, nc)
        out['mod'] = (p, rk, cons)
    out['secs'] = round(time.time() - t0, 1)
    if verbose:
        print(out)
    return out, (cols, entries, b, A, bb, sol)


if __name__ == '__main__':
    R = int(sys.argv[1])
    fams = tuple(sys.argv[2].split(',')) if len(sys.argv) > 2 else ('V2', 'T3', 'G2', 'xi1', 'chi')
    print("matching families:", fams)
    run(R, fams)
