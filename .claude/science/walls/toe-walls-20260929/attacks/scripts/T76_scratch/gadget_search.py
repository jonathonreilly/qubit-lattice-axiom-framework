#!/usr/bin/env python3
"""T76-A: sealed-gadget classification of count-threshold rules A subset {0..2d}.
A gadget: window W, >=2 patterns P (subsets of W) that are (i) peelable inside W with outside empty,
(ii) sealed: every empty v in W has kin(v)+j not in A for all j in 0..o(v).
"""
import itertools, sys, time
import numpy as np

def window(shape):
    d = len(shape)
    sites = list(itertools.product(*[range(s) for s in shape]))
    idx = {s: i for i, s in enumerate(sites)}
    nb = []
    o = []
    for s in sites:
        lst = []
        for k in range(d):
            for dv in (-1, 1):
                t = list(s); t[k] += dv; t = tuple(t)
                if t in idx: lst.append(idx[t])
        nb.append(lst); o.append(2 * d - len(lst))
    return sites, nb, o

def patterns_sealed(shape, A):
    """return array of pattern masks that are sealed (ignoring peelability)."""
    sites, nb, o = window(shape)
    n = len(sites)
    d = len(shape)
    Aset = set(A)
    # for each site and each kin, bad if kin+j in A for some j in 0..o
    P = np.arange(1 << n, dtype=np.uint64 if n > 31 else np.uint32)
    ok = np.ones(1 << n, dtype=bool)
    for v in range(n):
        nbmask = 0
        for u in nb[v]: nbmask |= (1 << u)
        # kin = popcount(P & nbmask)
        x = P & np.array(nbmask, dtype=P.dtype)
        kin = np.zeros(1 << n, dtype=np.int8)
        for u in nb[v]:
            kin += ((x >> np.array(u, dtype=P.dtype)) & 1).astype(np.int8)
        empty = ((P >> np.array(v, dtype=P.dtype)) & 1) == 0
        badk = np.zeros(2 * d + 2, dtype=bool)  # kin values for which sealed fails
        for kk in range(2 * d + 1):
            for j in range(0, o[v] + 1):
                if (kk + j) in Aset: badk[kk] = True
        bad = badk[kin] & empty
        ok &= ~bad
    return P[ok], sites, nb

def peelable(mask, nb, Aset, cache):
    # exists order adding sites of mask, each with kin(prefix) in A. Reverse peel with memo.
    # forward search: from empty set add site v if kin in A.
    n = len(nb)
    nbm = [sum(1 << u for u in nb[v]) for v in range(n)]
    seen = set()
    stack = [0]
    seen.add(0)
    while stack:
        cur = stack.pop()
        if cur == mask: return True
        rem = mask & ~cur
        while rem:
            b = rem & -rem
            v = b.bit_length() - 1
            rem ^= b
            k = bin(cur & nbm[v]).count("1")
            if k in Aset:
                nxt = cur | b
                if nxt not in seen:
                    seen.add(nxt); stack.append(nxt)
    return False

def gadget_count(shape, A):
    """number of sealed & peelable patterns in window 'shape' (includes empty pattern when it is sealed)."""
    Aset = set(A)
    pats, sites, nb = patterns_sealed(shape, A)
    cnt = 0
    good = []
    for m in pats.tolist():
        if m == 0:
            # empty pattern: sealed iff no empty site can ever form; peelable trivially
            good.append(m); continue
        if 0 not in Aset: continue
        if peelable(m, nb, Aset, None): good.append(m)
    return good, sites

def shapes(d, maxvol, maxside):
    out = []
    if d == 2:
        for a in range(1, maxside + 1):
            for b in range(a, maxside + 1):
                if a * b <= maxvol: out.append((a, b))
    else:
        for a in range(1, maxside + 1):
            for b in range(a, maxside + 1):
                for c in range(b, maxside + 1):
                    if a * b * c <= maxvol: out.append((a, b, c))
    return out

def classify(d, A, maxvol, maxside):
    Aset = set(A)
    if 0 not in Aset:
        return "TRIV0", None
    if Aset == set(range(min(Aset), 2 * d + 1)) and False:
        pass
    best = None
    for sh in sorted(shapes(d, maxvol, maxside), key=lambda s: np.prod(s)):
        good, _ = gadget_count(sh, A)
        if len(good) >= 2:
            g = len(good)
            b = max(sh)  # spacing: windows at gap 1 -> period (side+1) along each axis; use per-axis
            per = int(np.prod([s + 1 for s in sh]))
            rate = np.log(g) / per
            if best is None or rate > best[2]:
                best = (sh, g, rate)
            # keep going a little for a better rate but stop at first to save time when small
            if np.prod(sh) >= 12: break
    if best: return "GADGET", best
    return "NOGADGET", None

if __name__ == "__main__":
    d = int(sys.argv[1]); maxvol = int(sys.argv[2]); maxside = int(sys.argv[3])
    t0 = time.time()
    rules = []
    for r in range(0, 2 * d + 2):
        for A in itertools.combinations(range(2 * d + 1), r):
            if len(A) == 0: continue
            rules.append(A)
    for A in rules:
        cls, info = classify(d, A, maxvol, maxside)
        print(d, "A=", "".join(map(str, A)), cls, info, flush=True)
    print("time", time.time() - t0)
