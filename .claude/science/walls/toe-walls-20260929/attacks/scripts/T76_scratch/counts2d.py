#!/usr/bin/env python3
"""T76-B: exact frozen counts (row DP) and reachable-frozen counts (enumeration + peeling) for count-threshold rules in 2D."""
import sys, itertools, time
import numpy as np
from math import log

def popc_table(L):
    return None

def frozen_states(L, A):
    """Enumerate ALL frozen occupation sets of the sealed LxL box for rule A (list of row-mask tuples), by row DFS.
    frozen: every empty site has k not in A (outside box unrecorded)."""
    Aset = set(A)
    full = (1 << L) - 1
    # row constraint for row r given prev, cur, nxt: for each empty j in cur: k = prev_j+nxt_j+cur_{j-1}+cur_{j+1}
    bits = [[(m >> j) & 1 for j in range(L)] for m in range(1 << L)]
    bitsa = np.array(bits, dtype=np.int8)  # (2^L, L)
    allm = np.arange(1 << L)
    # horizontal counts per cur mask
    def horiz(cur):
        b = bitsa[cur]
        h = np.zeros(L, dtype=np.int8)
        h[1:] += b[:-1]; h[:-1] += b[1:]
        return b, h
    Aarr = np.zeros(6, dtype=bool)
    for a in Aset: Aarr[a] = True
    # ok(prev, cur, nxt) vectorised over nxt
    def ok_next(prev, cur):
        b, h = horiz(cur)
        pb = bitsa[prev] if prev is not None else np.zeros(L, dtype=np.int8)
        k = (h + pb)[None, :] + bitsa  # (2^L, L) with nxt as rows
        bad = Aarr[k] & (b[None, :] == 0)
        return ~bad.any(axis=1)
    # DFS over rows
    res = []
    def rec(rows):
        r = len(rows)
        if r == L:
            # last row: nxt is zeros (outside)
            prev = rows[-2] if r >= 2 else None
            cur = rows[-1]
            b, h = horiz(cur)
            pb = bitsa[prev] if prev is not None else np.zeros(L, dtype=np.int8)
            k = h + pb
            if not (Aarr[k] & (b == 0)).any():
                res.append(tuple(rows))
            return
        prev = rows[-2] if r >= 2 else None
        cur = rows[-1] if r >= 1 else None
        if r == 0:
            for m in range(1 << L):
                rec([m])
            return
        okm = ok_next(prev, cur)
        for m in np.nonzero(okm)[0].tolist():
            rec(rows + [m])
    rec([])
    return res

def to_sitemask(rows, L):
    m = 0
    for r, rm in enumerate(rows):
        m |= rm << (r * L)
    return m

def nbmasks(L):
    nb = []
    for r in range(L):
        for c in range(L):
            m = 0
            if r > 0: m |= 1 << ((r - 1) * L + c)
            if r < L - 1: m |= 1 << ((r + 1) * L + c)
            if c > 0: m |= 1 << (r * L + c - 1)
            if c < L - 1: m |= 1 << (r * L + c + 1)
            nb.append(m)
    return nb

def reachable(mask, nbm, Aset):
    """exists order of adding sites of mask with k in A at each addition. Memoised forward DFS with greedy-first."""
    if mask == 0: return True
    seen = {0}
    stack = [0]
    while stack:
        cur = stack.pop()
        rem = mask & ~cur
        if rem == 0: return True
        r = rem
        while r:
            b = r & -r
            v = b.bit_length() - 1
            r ^= b
            k = (cur & nbm[v]).bit_count()
            if k in Aset:
                nxt = cur | b
                if nxt == mask: return True
                if nxt not in seen:
                    seen.add(nxt); stack.append(nxt)
    return False

if __name__ == "__main__":
    A = tuple(int(c) for c in sys.argv[1])
    Lmax = int(sys.argv[2])
    do_reach = len(sys.argv) < 4 or sys.argv[3] != "frozenonly"
    Aset = set(A)
    print("rule A =", A)
    prev = None
    for L in range(2, Lmax + 1):
        t0 = time.time()
        fs = frozen_states(L, A)
        nf = len(fs)
        nr = None
        if do_reach and nf <= 200000:
            nbm = nbmasks(L)
            nr = sum(1 for rows in fs if reachable(to_sitemask(rows, L), nbm, Aset))
        print(f"L={L:2d} frozen={nf:9d} reach={nr}  ln(fr)/L={log(nf)/L if nf>0 else 0:.4f} ln(fr)/L^2={log(nf)/L**2 if nf>0 else 0:.4f}  ({time.time()-t0:.1f}s)", flush=True)
