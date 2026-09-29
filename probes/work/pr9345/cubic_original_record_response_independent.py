#!/usr/bin/env python3
"""J:falsifier:PR9345 -- independent check of the original-record local-response note (cubic compensated integer-rotor law).

Own code from the definitions (the one-pair sector model of the sibling PR 9316 unit, rebuilt here): (1) closure of the 11322-word component and the H stencil; (2) the compressed full original loss
G = sum_a 2(5-o_a) F_a^* F_a - 60 per centre, from the definition of the birth maps, on that component: 118092 directed displacement entries, Hermiticity, absolute row sum 684, Gershgorin bounds [-684, 212], anchor
step, initial excess -1164/5, -1044/5, -1104/5 for the full minus, plus and coherent first vectors, the diagonal 2(5-o)(6-o)-60 in {0,-20,-36}, and the local Schur-test norms (F_a^2 <= 12, B^2 <= 9,
Gamma squared-degree bounds 60, 80, 72, 48, 20, 0); (3) the cached 4096-point sample payload decoded and the note's statistics table recomputed, the PCG64 designs checked against the cached hashes, and a spread subset of
the 4096 x 2 response values re-evaluated with the own stencils and expm_multiply, compared with the cache; (4) the exact rational parameter certificate (b, n_A, n_B, R, refined R, q, B_s(u), weak-term total, r mu, L) recomputed with Fractions.
"""
import math, sys, time, itertools
from collections import defaultdict
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from multiprocessing import Pool

PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

import itertools, sys, time
from collections import defaultdict

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
def add(s, d): return (s[0] + d[0], s[1] + d[1], s[2] + d[2])
def is_A(s): return (s[0] + s[1] + s[2]) % 2 == 0
def nbrs(s): return [add(s, d) for d in DIRS]
def vac_q(s): return 1 if is_A(s) else 0

class W:
    """word = charges deviating from the vacuum and non-zero fields; immutable tuple form for hashing."""
    __slots__ = ("Q", "E")
    def __init__(self, Q, E): self.Q, self.E = Q, E

def pack(Qd, Ed):
    return (tuple(sorted(Qd.items())), tuple(sorted((k, v) for k, v in Ed.items() if v != 0)))
def unpack(w):
    return dict(w[0]), dict(w[1])
def qget(Qd, s): return Qd.get(s, vac_q(s))
def edge(a, b): return (a, b) if is_A(a) else (b, a)

def F_move(Qd, Ed, a, b):
    """F_{a->b}: requires q_a != 0 and q_b == 0 (a in A, b in B)."""
    qa = qget(Qd, a)
    if qa == 0 or qget(Qd, b) != 0: return False
    Qd[b] = qa; Qd[a] = 0
    Ed[(a, b)] = Ed.get((a, b), 0) - qa
    return True
def F_adj(Qd, Ed, a, b):
    """adjoint: requires q_a == 0 and q_b != 0; moves the particle from b back to a."""
    qb = qget(Qd, b)
    if qget(Qd, a) != 0 or qb == 0: return False
    Qd[a] = qb; Qd[b] = 0
    Ed[(a, b)] = Ed.get((a, b), 0) + qb
    return True
def clean(Qd):
    for s in [s for s, q in Qd.items() if q == vac_q(s)]: del Qd[s]

def D_of(Qd, Ed):
    D = 0
    for (a, b), e in Ed.items():
        if e != 0 and qget(Qd, b) == 0: D += e * (e - qget(Qd, a))
    return D
def valid(Qd, Ed):
    # all A occupied, Gauss law, D = 0
    for s, q in Qd.items():
        if is_A(s) and q == 0: return False
    # Gauss: recompute divergences on the touched sites
    div = defaultdict(int)
    for (a, b), e in Ed.items():
        div[a] += e; div[b] -= e
    sites = set(div) | set(Qd)
    for s in sites:
        q = qget(Qd, s)
        if div.get(s, 0) != q - (1 if is_A(s) else 0): return False
    return D_of(Qd, Ed) == 0

def shared(a, c):
    return len(set(nbrs(a)) & set(nbrs(c)))

def H4_row(word, want_D=False):
    """Returns dict target-word -> coefficient of (H4 - vacuum scalar over interacting pairs) applied to `word`, before the -2, restricted to D=0 targets (P0)."""
    Q0, E0 = unpack(word)
    occB = [s for s, q in Q0.items() if (not is_A(s)) and q != 0]
    neg = [s for s, q in Q0.items() if q == -1]
    Aint = set()
    for s in neg:
        if is_A(s): Aint.add(s)
    for (a, b), e in E0.items(): Aint.add(a)
    for o in occB:
        for n in nbrs(o): Aint.add(n)
    pairs = set()
    for a in Aint:
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                for dz in range(-2, 3):
                    c = (a[0] + dx, a[1] + dy, a[2] + dz)
                    if c != a and is_A(c) and shared(a, c) > 0:
                        pairs.add((a, c) if a < c else (c, a))
    out = defaultdict(int); vac_total = 0
    for (a, c) in pairs:
        vac_total += 36 - shared(a, c)
        Na, Nc = nbrs(a), nbrs(c)
        for b in Na:
            Q1 = dict(Q0); E1 = dict(E0)
            if not F_move(Q1, E1, a, b): continue
            for b2 in Nc:
                Q2 = dict(Q1); E2 = dict(E1)
                if not F_move(Q2, E2, c, b2): continue
                for d2 in Nc:
                    Q3 = dict(Q2); E3 = dict(E2)
                    if not F_adj(Q3, E3, c, d2): continue
                    for d in Na:
                        if d == d2: continue
                        Q4 = dict(Q3); E4 = dict(E3)
                        if not F_adj(Q4, E4, a, d): continue
                        clean(Q4)
                        if valid(Q4, E4): out[pack(Q4, E4)] += 1
    return out, vac_total

E1 = (1, 0, 0)
def translate(w, t):
    Qd, Ed = unpack(w)
    Q2 = {(s[0] - t[0], s[1] - t[1], s[2] - t[2]): q for s, q in Qd.items()}
    E2 = {((a[0] - t[0], a[1] - t[1], a[2] - t[2]), (b[0] - t[0], b[1] - t[1], b[2] - t[2])): e for (a, b), e in Ed.items()}
    return pack(Q2, E2)
def neg_site(w):
    for s, q in w[0]:
        if q == -1: return s
    raise ValueError("no negative particle")
def anchor_of(n):
    return (0, 0, 0) if is_A(n) else E1
def canon(w):
    n = neg_site(w); anc = anchor_of(n)
    t = (n[0] - anc[0], n[1] - anc[1], n[2] - anc[2])
    return translate(w, t), t                     # raw = T_t(canonical)

def row_of(w):
    """canonical word -> {(canonical target, t): stencil coefficient H_rel = -2 (count - vac delta)}"""
    row, vac = H4_row(w)
    out = {}
    for tgt, cnt in row.items():
        cw, t = canon(tgt)
        key = (cw, t)
        if cw == w and t == (0, 0, 0): out[key] = out.get(key, 0) - 2 * (cnt - vac)
        else: out[key] = out.get(key, 0) - 2 * cnt
    if (w, (0, 0, 0)) not in out: out[(w, (0, 0, 0))] = -2 * (0 - vac)
    return out



def g_row(w):
    """rows of the excess loss operator for one word: {(canonical target, displacement): coefficient} for D = 0 targets, the per-centre diagonal excesses and the weighted count of dropped D > 0 incidences"""
    Qd, Ed = unpack(w)
    occB = {s for s, q in Qd.items() if (not is_A(s)) and q != 0}
    centers = set()
    for o in occB:
        for a in nbrs(o): centers.add(a)
    acc = defaultdict(int); centre_diags = []; dpos = 0
    for a in centers:
        Na = nbrs(a); occ = [x for x in Na if x in occB]; o = len(occ); coef = 2 * (5 - o)
        acc[(w, (0, 0, 0))] += -60; centre_diags.append(coef * (6 - o) - 60)
        for d in Na:
            if d in occB: continue
            Q1, E1 = dict(Qd), dict(Ed); F_move(Q1, E1, a, d)
            for d2 in [d] + occ:
                Q2, E2 = dict(Q1), dict(E1)
                if not F_adj(Q2, E2, a, d2): continue
                clean(Q2)
                if D_of(Q2, E2) > 0: dpos += coef; continue
                cw, t = canon(pack(Q2, E2)); acc[(cw, t)] += coef
    return dict(acc), centre_diags, dpos

_ARR = None
def _init_arr(arr):
    global _ARR
    _ARR = arr
def sample_eval(args):
    """one response sample: Bloch fibres of H and G at the momentum, propagation of the full first-minus vector at t = .02 and at the sampled time"""
    i, k, times_i = args
    import scipy.sparse as sp_
    from scipy.sparse.linalg import expm_multiply
    (Hs, Hd, Ht, Hc), (Gs, Gd, Gt, Gc), phi, shift, n = _ARR
    kk = np.array(k)
    fib = lambda s_, d_, tau_, c_: sp_.coo_matrix((c_ * np.exp(-1j * (tau_ @ kk)), (d_, s_)), shape=(n, n)).tocsr()
    H = fib(Hs, Hd, Ht, Hc); G = fib(Gs, Gd, Gt, Gc); ident = sp_.eye(n, format="csr"); out = []
    for t in (.02, float(times_i)):
        y = expm_multiply((-1j * t) * (H - shift * ident), phi, traceA=0.)
        out.append(float(np.vdot(y, G @ y).real))
    return i, out

def main():
    import base64, hashlib, json, subprocess, os
    from fractions import Fraction as Fr
    from pathlib import Path
    T0 = time.time()
    ROOT = Path(__file__).resolve().parents[3]
    BR = "codex/original-record-local-response-20260926"
    subprocess.run(["git", "fetch", "origin", BR, "--quiet"], cwd=ROOT)
    def gshow(p): return subprocess.run(["git", "show", f"origin/{BR}:{p}"], cwd=ROOT, capture_output=True, text=True).stdout
    e1, e2 = (1, 0, 0), (0, 1, 0); O = (0, 0, 0)
    s0 = pack({(0, 0, 0): -1, e1: 1, e2: 1}, {((0, 0, 0), e1): -1, ((0, 0, 0), e2): -1})
    words = {s0: 0}; order = [s0]; rows = {}; frontier = [s0]
    nproc = min(9, max(2, (os.cpu_count() or 4) - 1))
    with Pool(nproc) as pool:
        while frontier:
            res = pool.map(row_of, frontier, chunksize=4); nxt = []
            for w, r in zip(frontier, res):
                rows[w] = r
                for (cw, t) in r:
                    if cw not in words: words[cw] = len(order); order.append(cw); nxt.append(cw)
            frontier = nxt
    idx = {w: i for i, w in enumerate(order)}; n = len(order)
    check("the closed component has 11322 words (the parent's quotient, rebuilt from the definitions)", n == 11322, f"{n}, {time.time()-T0:.0f}s")
    Gent = {}; missing_D0 = 0; dropped = 0; centre_diag_vals = set()
    for w in order:
        r, cd, dpos = g_row(w); dropped += dpos; centre_diag_vals.update(cd)
        i = idx[w]
        for (cw, t), v in r.items():
            if v == 0: continue
            if cw not in idx: missing_D0 += 1; continue
            Gent[(i, idx[cw], t)] = v
    offd = sum(1 for (i, j, t) in Gent if not (i == j and t == (0, 0, 0)))
    check("the excess loss G has 118092 directed displacement entries on the component and zero missing D = 0 targets (targets with D > 0 are dropped by the compression)", offd == 118092 and missing_D0 == 0, f"{offd} entries, {missing_D0} missing D=0 targets, {dropped} weighted D>0 incidences dropped")
    check("G is exactly reverse-displacement Hermitian", all(Gent.get((j, i, (-t[0], -t[1], -t[2]))) == v for (i, j, t), v in Gent.items()))
    absrow = np.zeros(n); offrow = np.zeros(n); dg = np.zeros(n); tmax = 0
    for (i, j, t), v in Gent.items():
        absrow[i] += abs(v)
        if i == j and t == (0, 0, 0): dg[i] = v
        else: offrow[i] += abs(v)
        tmax = max(tmax, abs(t[0]) + abs(t[1]) + abs(t[2]))
    check("full absolute row sum of G at most 684, and uniform Gershgorin bounds [-684, 212]", absrow.max() == 684 and (dg - offrow).min() == -684 and (dg + offrow).max() == 212, f"{absrow.max():.0f}, [{(dg-offrow).min():.0f}, {(dg+offrow).max():.0f}]")
    check("anchor step (largest l1 displacement between anchored words) at most 2", tmax <= 2, f"{tmax}")
    check("per-centre diagonal excess 2(5-o)(6-o)-60 takes the values -20 and -36 for o = 1, 2 occupied neighbours (0 for o = 0, which contributes no excess)", centre_diag_vals == {-20, -36} and [2 * (5 - o) * (6 - o) - 60 for o in range(3)] == [0, -20, -36], f"{sorted(centre_diag_vals)}")
    def first_branches(sigma):
        out = []
        for bd in nbrs(O):
            if bd == e1: continue
            Qd, Ed = {}, {}; F_move(Qd, Ed, O, bd); Qd[O] = sigma; Qd[e1] = -sigma; Ed[(O, e1)] = Ed.get((O, e1), 0) + sigma
            clean(Qd); out.append(canon(pack(Qd, Ed))[0])
        return out
    vm = np.zeros(n); vp = np.zeros(n)
    for w in first_branches(-1): vm[idx[w]] = 1 / math.sqrt(5)
    for w in first_branches(1): vp[idx[w]] = 1 / math.sqrt(5)
    G0 = sp.csr_matrix(([v for (i, j, t), v in Gent.items() if t == (0, 0, 0)], ([i for (i, j, t) in Gent if t == (0, 0, 0)], [j for (i, j, t) in Gent if t == (0, 0, 0)])), shape=(n, n), dtype=float)
    vc = (vm + vp) / math.sqrt(2)
    ex = [vm @ (G0 @ vm), vp @ (G0 @ vp), vc @ (G0 @ vc)]
    check("exact initial excess -1164/5 (first-minus), -1044/5 (plus), -1104/5 (coherent)", all(abs(a - b) < 1e-9 for a, b in zip(ex, (-1164 / 5, -1044 / 5, -1104 / 5))), f"{ex}")
    sv = []
    for o in range(6):
        subsets = [frozenset(c) for c in itertools.combinations(range(6), o)]; targets = [frozenset(c) for c in itertools.combinations(range(6), o + 1)]
        M = np.array([[1.0 if s <= t_ else 0.0 for s in subsets] for t_ in targets]); sv.append(np.linalg.svd(M, compute_uv=False)[0] ** 2)
    check("||F_a||^2 on the block with o occupied neighbours equals (6-o)(o+1) exactly (biregular incidence), at most 12; the ||B||^2 bound max (5-o)(o+1) = 9; Gamma squared-degree bounds 60, 80, 72, 48, 20, 0",
          all(abs(sv[o] - (6 - o) * (o + 1)) < 1e-9 for o in range(6)) and max(sv) < 12 + 1e-9 and max((5 - o) * (o + 1) for o in range(6)) == 9 and [2 * (5 - o) * (6 - o) * (o + 1) for o in range(6)] == [60, 80, 72, 48, 20, 0], f"{[round(x) for x in sv]}")
    cache = gshow("logs/runner-cache/cubic_original_record_local_response_2026_09_26.txt").split("----- stdout -----\n", 1)[1]
    i0 = cache.index('"sample_payload_schema"'); st = cache.rfind("{", 0, i0); depth = 0
    for jx in range(st, len(cache)):
        if cache[jx] == "{": depth += 1
        elif cache[jx] == "}":
            depth -= 1
            if depth == 0: en = jx + 1; break
    payload = json.loads(cache[st:en])
    vals = np.frombuffer(base64.b64decode(payload["values"]), dtype="<f8").reshape(4096, 2)
    raw = lambda x: np.ascontiguousarray(x, dtype='<f8').tobytes()
    ks = np.random.Generator(np.random.PCG64(261926322)).uniform(-np.pi, np.pi, (4096, 3)); times = np.random.Generator(np.random.PCG64(261926323)).uniform(0., .02, 4096)
    check("cached payload hash, PCG64 momentum design (seed 261926322) and time design (seed 261926323) reproduce the recorded sha256 values", hashlib.sha256(vals.tobytes()).hexdigest() == payload["values_sha256"] and hashlib.sha256(raw(ks)).hexdigest() == payload["design"]["momenta_sha256"] and hashlib.sha256(raw(times)).hexdigest() == payload["design"]["times_sha256"])
    ch = vals + 1164 / 5; fac = math.log(160); lo, hi = -684, 212; tab = []
    for j in range(2):
        x = ch[:, j]; var = float(np.var(x, ddof=1)); mean = float(np.mean(x)); rad = math.sqrt(2 * var * fac / 4096) + 7 * (hi - lo) * fac / (3 * 4095); tab.append((mean, var, mean - rad, mean + rad))
    cov = float(np.cov(ch.T, ddof=1)[0, 1])
    check("the note's table from the cached samples: endpoint -4.22773599689, [-6.83883359965, -1.61663839413]; time average -3.74314936801, [-6.39235515321, -1.09394358280]; variances .161602291839, 1.363102969974; covariance -.000927014493",
          abs(tab[0][0] + 4.22773599689) < 5e-12 and abs(tab[0][2] + 6.83883359965) < 5e-11 and abs(tab[0][3] + 1.61663839413) < 5e-11 and abs(tab[1][0] + 3.74314936801) < 5e-12 and abs(tab[1][2] + 6.39235515321) < 5e-11 and abs(tab[1][3] + 1.09394358280) < 5e-11
          and abs(tab[0][1] - .161602291839) < 5e-13 and abs(tab[1][1] - 1.363102969974) < 5e-13 and abs(cov + .000927014493) < 5e-13, f"{[tuple(round(v, 11) for v in t_) for t_ in tab]}, cov {cov:.12f}")
    check("adding the analytic transfer error .014 to the time-average interval gives the note's [-6.40636, -1.07994]", abs((tab[1][2] - .014) + 6.40636) < 2e-5 and abs((tab[1][3] + .014) + 1.07994) < 2e-5, f"[{tab[1][2]-.014:.5f}, {tab[1][3]+.014:.5f}]")
    Hs = []
    for w, r in rows.items():
        i = idx[w]
        for (cw, t), v in r.items():
            if v != 0: Hs.append((i, idx[cw], t, v))
    def arrays(ent): return (np.array([e[0] for e in ent]), np.array([e[1] for e in ent]), np.array([e[2] for e in ent], dtype=float), np.array([e[3] for e in ent], dtype=float))
    Ha = arrays(Hs); Ga = arrays([(i, j, t, v) for (i, j, t), v in Gent.items()])
    phi = vm.astype(complex); m0 = (Ha[0] == Ha[1]) & (np.abs(Ha[2]).sum(1) == 0); diagH = np.zeros(n); diagH[Ha[0][m0]] = Ha[3][m0]; shift = float(np.mean(diagH))
    NS = int(os.environ.get("PROBE_SAMPLES", 72))
    pick = sorted(set(list(range(NS // 2)) + [int(x) for x in np.linspace(NS // 2, 4095, NS - NS // 2)]))
    with Pool(nproc, initializer=_init_arr, initargs=((Ha, Ga, phi, shift, n),)) as pool2:
        res = pool2.map(sample_eval, [(i, ks[i], times[i]) for i in pick], chunksize=1)
    mine = np.array([r[1] for r in sorted(res)]); dev = np.abs(mine - vals[pick])
    check(f"{len(pick)} of the 4096 momenta (the first {NS//2} and an even spread) re-evaluated with the own H and G stencils and expm_multiply agree with the cached values, endpoint and time average, to 1e-9", dev.max() < 1e-9, f"max deviation {dev.max():.2e} (endpoint {dev[:,0].max():.1e}, time average {dev[:,1].max():.1e}); {time.time()-T0:.0f}s")
    l = 2048; s = l + 2; u = Fr(1, 50); r = Fr(1, 10 ** 33); Tt = 256
    J = 1195776 + 27200 * r; b = l + 7 + math.ceil(18 * J * u) + 6 * Tt
    odd = (-1) ** b; nA = ((2 * b + 1) ** 3 + odd) // 2; nB = ((2 * b + 1) ** 3 - odd) // 2
    eps = r * u / 400; lb = nA * (5184 + 160 * r)
    R1 = math.ceil(24 * nB / eps ** 2); R2 = math.ceil(Fr(22, 7) * lb * (1 + 2 * lb * u) / (2 * eps)); Rold = max(R1, R2)
    W = ((2 * l + 1) ** 3 + 1) // 2; m = 80 * W; lH = 5184 * nA
    R3 = math.ceil(24 * nB * (1000 * m) ** 2); R4 = math.ceil(Fr(22, 7) * lH * (1 + 2 * lH * u) * 1000 * m / 2); Rref = max(R3, R4)
    z = Fr(6, 7); q = math.ceil(s + 2 + 6 * 3 * J * u)
    Bs = (2 * q + 1) ** 3 + 24 * (q ** 2 * z / (1 - z) + 2 * q * z / (1 - z) ** 2 + z * (1 + z) / (1 - z) ** 3) + 2 * z / (1 - z)
    weak = 160 * r * m * u * Bs + r * m * m * u
    check("exact certificate arithmetic: b = 434071, R = 31406174599109769984 x 10^74 (24 n_B / epsilon^2 dominates), refined R = 497313353615986515185363764932926666957967531268139212800 (the averaging term dominates), q = 432532, B_s(u) = 647387480797214709",
          b == 434071 and Rold == 31406174599109769984 * 10 ** 74 and R1 > R2 and Rref == 497313353615986515185363764932926666957967531268139212800 and R4 > R3 and q == 432532 and math.floor(Bs) == 647387480797214709 == math.ceil(Bs), f"b {b}, q {q}, |W| {W}, m {m}")
    check("weak terms 160 r m u B_s(u) + r m^2 u = .005698652434347410 (to 2e-18), r m u = 5.50158565392e-23, even L >= 4(b+4)+2 = 1736302, exp(-19183/75) <= 2^-255",
          abs(float(weak) - .005698652434347410) < 2e-18 and abs(float(r * m * u) - 5.50158565392e-23) < 1e-33 and 4 * (b + 4) + 2 == 1736302 and math.exp(-19183 / 75) <= 2.0 ** -255, f"weak {float(weak):.18f}")
    print(f"   total {time.time()-T0:.0f}s")
    if not HITS:
        print(f"SUMMARY: no falsifier fires: from the definitions the closed 11322-word component, the loss operator G (118092 entries, row sum 684, Gershgorin [-684,212], initial excess -1164/5, -1044/5, -1104/5), the local Schur-test norms, the note's statistics table (recomputed from the cached 4096 x 2 samples), {len(pick)} independently re-evaluated response samples (max deviation {dev.max():.1e}) and the exact rational parameter certificate (b, R, refined R, q, B_s, weak terms, L) all reproduce; {PASS} checks pass")
    else:
        print("SUMMARY: failed: " + "; ".join(HITS)); print("HIT: independent reconstruction differs from the note on: " + "; ".join(HITS))
    sys.exit(0)

if __name__ == "__main__":
    main()
