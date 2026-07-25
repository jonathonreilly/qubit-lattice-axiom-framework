"""KCPT D2 graded signed-permutation commutant characterization (self-contained).

Characterizes the FULL signed-permutation commutant

    Comm(D2) = { signed permutation U : U D2 = D2 U }

of the staggered lattice operator D2 at L in {4, 6} (N = L^3, staggered eta:
eta_0 = 1, eta_1 = (-1)^x0, eta_2 = (-1)^(x0+x1)), locates the symmetry group
H = <G_amb, S_eps> and the dressed rotation extension <H, g_r4> inside it, and
characterizes the Z_2 grading

    grade(U) : U D2 U^{-1} = grade(U) * D2 ,  grade in {+1, -1}

induced on the graded commutant GC = closure(Comm, S_eps). S_eps anticommutes
with D2, so H is NOT contained in Comm; the natural object carrying both is the
graded commutant GC, of which Comm is the (grade +1) kernel.

The commutant is enumerated EXACTLY (never by tolerance) in three exact stages:
  (1) support-graph automorphisms of the D2 adjacency graph (backtracking with
      adjacency-, distance- and common-neighbour pruning; every completion is
      verified by exact permuted-adjacency equality), assembled as Aut =
      { T_v o sigma : v a translation, sigma in Stab(0) } (orbit-stabiliser);
  (2) for each automorphism, an exact integer sign lift over a BFS spanning tree
      (s_0 = +1, unique up to a global flip), verified on every D2 support entry;
  (3) Comm = { (p, +s), (p, -s) : p a liftable automorphism }, and every element
      is re-verified by the full N x N integer identity s_i s_j D2[p_i,p_j] =
      D2[i,j].

All group arithmetic is exact (integer (perm, sign) pairs, array_equal); no
floating tolerance is ever used for a group / commutation / grade decision.
Frobenius-projection quantities (word-algebra dims, sep6 reach omega) reuse the
landed Unit 23 / Unit 24 real word-algebra machinery verbatim.

Construction (build_lattice, sp_* helpers, compose, key, commutes_with_D2,
build_group, full_character, shell_character, shell_commutant, isotypic_blocks,
dense_from_sp, word_algebra_real, g_r4 witness) is copied logic-identically from
the landed Unit 23 and Unit 24 runners: executable statements unchanged, comment
text elided, and the g_r4 witness packaged as a function. Runs single-threaded.

Gate contract: exits 0 with a final `TOTAL: PASS=N FAIL=0` line, N = 32.
"""

import itertools
import time
import gc
import resource
import sys
import numpy as np
from collections import deque

sys.setrecursionlimit(100000)

# ----------------------------------------------------------------------------
# gate harness
# ----------------------------------------------------------------------------
_P = [0]
_F = [0]


def gate(name, cond, msg=""):
    ok = bool(cond)
    tag = "PASS" if ok else "FAIL"
    line = f"[GATE {name}] {tag}"
    if msg:
        line += f" -- {msg}"
    print(line, flush=True)
    if ok:
        _P[0] += 1
    else:
        _F[0] += 1
    return ok


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes, Linux reports kB
    return r / 1e9 if r > 1e7 else r / 1e6


# ============================================================================
# COPIED CONSTRUCTION (logic-identical from the landed Unit 23 / Unit 24 runners;
# comment text elided)
# ============================================================================
SUBSETS = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]


def build_lattice(L):
    N = L ** 3
    e = np.eye(3, dtype=int)

    def idx(a, b, c):
        return ((a % L) * L + (b % L)) * L + (c % L)

    coords = np.array([[a, b, c] for a in range(L) for b in range(L) for c in range(L)],
                      dtype=int)

    def eta_mu(mu, x):
        if mu == 0:
            return 1
        if mu == 1:
            return (-1) ** x[0]
        return (-1) ** (x[0] + x[1])

    D2 = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        x = coords[i]
        for mu in range(3):
            xp = (x + e[mu]) % L
            xm = (x - e[mu]) % L
            D2[i, idx(*xp)] += eta_mu(mu, x)
            D2[i, idx(*xm)] -= eta_mu(mu, x)

    M = D2 @ D2
    evM = np.linalg.eigvalsh(M.astype(float))
    rounded = np.round(evM).astype(int)
    distinct = sorted(set(rounded.tolist()), reverse=True)
    lam = distinct
    K = len(lam)

    Mf = M.astype(float)
    Pf = []
    mults = []
    Iden = np.eye(N)
    for m in range(K):
        Q = np.eye(N)
        Nm = 1.0
        for mp in range(K):
            if mp == m:
                continue
            Q = Q @ (Mf - lam[mp] * Iden)
            Nm *= (lam[m] - lam[mp])
        P = Q / Nm
        Pf.append(P)
        mults.append(int(round(np.trace(P))))

    V8 = np.zeros((N, 8), dtype=float)
    for k, S in enumerate(SUBSETS):
        for i in range(N):
            x = coords[i]
            V8[i, k] = (-1) ** sum(x[j] for j in S)

    sidx = {frozenset(S): k for k, S in enumerate(SUBSETS)}

    def sgn_subset(S):
        s = set(S)
        a = (-1) ** len(s & {0, 2})
        b = 1 if 1 in s else -1
        return a * b

    JN = np.zeros((8, 8), dtype=float)
    for k, S in enumerate(SUBSETS):
        target = frozenset(S) ^ frozenset({1})
        JN[sidx[target], k] = N * sgn_subset(S)
    Jker_int = V8 @ JN @ V8.T
    Jkerf = Jker_int / (float(N) ** 2)

    D2f = D2.astype(float)
    Jbulk = np.zeros((N, N), dtype=float)
    for m in range(K):
        if lam[m] == 0:
            continue
        Jbulk += (D2f @ Pf[m]) / np.sqrt(abs(lam[m]))
    Jfull = Jkerf + Jbulk

    eps = np.array([(-1) ** (coords[i, 0] + coords[i, 1] + coords[i, 2]) for i in range(N)],
                   dtype=float)
    Seps = np.diag(eps)

    return {
        "L": L, "N": N, "coords": coords, "idx": idx,
        "D2": D2, "D2f": D2f, "M": M, "lam": lam, "K": K,
        "Pf": Pf, "mults": mults, "V8": V8,
        "Jfull": Jfull, "eps": eps, "Seps": Seps,
    }


def sp_from_fmap(fmap, signfn, coords, idx, N):
    p = np.zeros(N, dtype=np.int64)
    s = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x = coords[i]
        xn = fmap(x)
        j = idx(*[int(v) for v in xn])
        p[i] = j
        s[i] = signfn(x)
    return p, s


def sp_diag(signfn, coords, N):
    p = np.arange(N, dtype=np.int64)
    s = np.array([signfn(coords[i]) for i in range(N)], dtype=np.int64)
    return p, s


def compose(a, b):
    pa, sa = a
    pb, sb = b
    return (pb[pa], sa * sb[pa])


def sp_inv(a):
    p, s = a
    pinv = np.empty_like(p)
    pinv[p] = np.arange(len(p))
    return (pinv, s[pinv])


def key(g):
    return g[0].tobytes() + (g[1].astype(np.int8)).tobytes()


def commutes_with_D2(g, D2):
    p, s = g
    A = (s[:, None] * s[None, :]) * D2[np.ix_(p, p)]
    return np.array_equal(A, D2)


def closure(gens):
    seen = {}
    idg = (np.arange(len(gens[0][0]), dtype=np.int64),
           np.ones(len(gens[0][0]), dtype=np.int64))
    stack = [idg]
    seen[key(idg)] = idg
    while stack:
        g = stack.pop()
        for gg in gens:
            h = compose(g, gg)
            k = key(h)
            if k not in seen:
                seen[k] = h
                stack.append(h)
    return seen


def build_group(lat):
    L, N = lat["L"], lat["N"]
    coords, idx, D2 = lat["coords"], lat["idx"], lat["D2"]

    def f_stab(x):
        return (x[0], x[1], x[2])

    def f_U2(x):
        return (-x[1], -x[0], -x[2])

    def f_UR(x):
        return (x[1], x[2], x[0])

    bases = [f_stab, f_U2, f_UR]

    trans = []
    for t in coords:
        tt = t.copy()
        trans.append(sp_from_fmap(lambda x, tt=tt: (x[0] + tt[0], x[1] + tt[1], x[2] + tt[2]),
                                  lambda x: 1, coords, idx, N))

    def make_signfn(bits):
        a1, a2, a3, b12, b13, b23 = bits

        def fn(x):
            e = (a1 * x[0] + a2 * x[1] + a3 * x[2]
                 + b12 * x[0] * x[1] + b13 * x[0] * x[2] + b23 * x[1] * x[2])
            return (-1) ** e
        return fn

    allbits = list(itertools.product([0, 1], repeat=6))

    commuting = {}
    for base in bases:
        base_sp = sp_from_fmap(base, lambda x: 1, coords, idx, N)
        for bits in allbits:
            sf = sp_diag(make_signfn(bits), coords, N)
            g0 = compose(base_sp, sf)
            for t in trans:
                g = compose(g0, t)
                if commutes_with_D2(g, D2):
                    commuting[key(g)] = g

    gens_all = list(commuting.values())
    Gamb = closure(gens_all)
    nG = len(Gamb)

    ident0 = np.arange(N)
    gens_G = []
    cur_size = 1
    for g in gens_all:
        if np.array_equal(g[0], ident0) and np.all(g[1] == 1):
            continue
        trial = closure(gens_G + [g])
        if len(trial) > cur_size:
            gens_G.append(g)
            cur_size = len(trial)
            if cur_size == nG:
                break

    Seps_sp = sp_diag(lambda x: (-1) ** (x[0] + x[1] + x[2]), coords, N)
    gens_H = gens_G + [Seps_sp]
    Hclos = closure(gens_H)
    nH = len(Hclos)

    HP = np.array([g[0] for g in Hclos.values()], dtype=np.int64)
    HS = np.array([g[1] for g in Hclos.values()], dtype=np.int8)
    Gkeys = set(Gamb.keys())

    return {
        "Gamb": Gamb, "H": Hclos, "nG": nG, "nH": nH,
        "HP": HP, "HS": HS, "Gkeys": Gkeys,
        "gens_G": gens_G, "gens_H": gens_H, "Seps_sp": Seps_sp,
    }


def full_character(HP, HS):
    nH, N = HP.shape
    ar = np.arange(N)
    chi = np.empty(nH)
    for h in range(nH):
        p, s = HP[h], HS[h]
        fixed = (p == ar)
        chi[h] = float(np.sum(s[fixed]))
    return chi


def shell_character(Pm, HP, HS):
    nH, N = HP.shape
    ar = np.arange(N)
    chi = np.empty(nH)
    for h in range(nH):
        p, s = HP[h], HS[h]
        chi[h] = float(np.sum(Pm[ar, p] * s))
    return chi


def vec(A):
    return np.asarray(A, dtype=complex).reshape(-1)


def word_algebra_real(gens, N, cap, tol=1e-9):
    gens = [np.asarray(g, dtype=np.float64) for g in gens]
    NN = N * N
    B = np.empty((cap, NN), dtype=np.float64)
    v = np.eye(N).reshape(-1).astype(np.float64)
    v /= np.linalg.norm(v)
    B[0] = v
    cnt = 1
    frontier = [np.eye(N, dtype=np.float64)]
    while frontier and cnt < cap:
        newf = []
        for w in frontier:
            for g in gens:
                p = g @ w
                v = p.reshape(-1).copy()
                nv = np.linalg.norm(v)
                if nv < tol:
                    continue
                v /= nv
                for _ in range(2):
                    if cnt:
                        v = v - B[:cnt].T @ (B[:cnt] @ v)
                r = np.linalg.norm(v)
                if r < tol:
                    continue
                B[cnt] = v / r
                cnt += 1
                newf.append(p)
                if cnt >= cap:
                    break
            if cnt >= cap:
                break
        frontier = newf
    closed = (len(frontier) == 0)
    return B[:cnt], cnt, closed


def overlap2(B, X):
    if B.shape[0] == 0:
        return 0.0
    v = vec(X)
    v = v / np.linalg.norm(v)
    return float(np.linalg.norm(B.conj() @ v) ** 2)


def shell_commutant(Pm, HP, HS, nR=14, build_seed=98765, chunk=512):
    N = Pm.shape[0]
    w, V = np.linalg.eigh(Pm)
    d = int(round(np.trace(Pm).real))
    Z = V[:, N - d:].astype(complex)
    nH = HP.shape[0]
    HSf = HS.astype(float)
    rng = np.random.default_rng(build_seed)
    Rs = []
    for _ in range(nR):
        A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
        Rs.append(A + A.conj().T)
    acc = [np.zeros((d, d), dtype=complex) for _ in range(nR)]
    for c0 in range(0, nH, chunk):
        c1 = min(c0 + chunk, nH)
        W = np.stack([Z.conj().T @ (HSf[h][:, None] * Z[HP[h], :]) for h in range(c0, c1)])
        for j, R in enumerate(Rs):
            T = W @ R
            acc[j] += np.einsum('hij,hkj->ik', T, W.conj())
        del W
    B = []
    for a in acc:
        M0 = a / nH
        for Q in B:
            M0 = M0 - np.vdot(Q, M0) * Q
        nrm = np.sqrt(abs(np.vdot(M0, M0)))
        if nrm > 1e-8:
            B.append(M0 / nrm)
    return Z, B


def isotypic_blocks(Z, Bc, cluster_seed):
    cm = len(Bc)
    d = Z.shape[1]
    Gc = np.zeros((cm, cm), dtype=complex)
    for Xk in Bc:
        Cg = np.stack([(Xk @ Xj - Xj @ Xk).ravel() for Xj in Bc], axis=1)
        Gc += Cg.conj().T @ Cg
    wc, Vc = np.linalg.eigh(Gc)
    thr = 1e-8 * max(wc[-1].real, 1e-30)
    nidx = np.where(wc < thr)[0]
    rC = len(nidx)
    Zc = [sum(Vc[k, j] * Bc[k] for k in range(cm)) for j in nidx]
    rng = np.random.default_rng(cluster_seed)
    C = sum(rng.standard_normal() * Zb for Zb in Zc)
    Hc = (C + C.conj().T) / 2
    ev, U = np.linalg.eigh(Hc)
    if rC <= 1:
        groups = [np.arange(len(ev))]
    else:
        gaps = np.diff(ev)
        cut = np.sort(np.argsort(gaps)[-(rC - 1):])
        groups = []
        start = 0
        for c in cut:
            groups.append(np.arange(start, c + 1))
            start = c + 1
        groups.append(np.arange(start, len(ev)))
    blocks = []
    for gr in groups:
        cols = U[:, gr]
        Pdd = cols @ cols.conj().T
        rank = int(round(np.trace(Pdd).real))
        pm = []
        for Xk in Bc:
            Y = Pdd @ Xk @ Pdd
            for Q in pm:
                Y = Y - np.vdot(Q, Y) * Q
            nrm = np.sqrt(abs(np.vdot(Y, Y)))
            if nrm > 1e-6:
                pm.append(Y / nrm)
        mult = int(round(np.sqrt(len(pm))))
        dim = rank // mult if mult else 0
        Pshell = Z @ Pdd @ Z.conj().T
        blocks.append((dim, mult, rank, Pshell))
    return rC, blocks


def dense_from_sp(p, s, N):
    U = np.zeros((N, N), dtype=float)
    U[np.arange(N), p] = s
    return U


def make_g_r4(lat):
    """Dressed four-fold rotation witness (Unit 23 B8 inline construction, packaged):
    g_r4 = diag((-1)^(x0*x1 + x0)) @ R4, R4 : x -> (x1, -x0, x2)."""
    coords, idx, N = lat["coords"], lat["idx"], lat["N"]
    r4_perm = sp_from_fmap(lambda x: (x[1], -x[0], x[2]), lambda x: 1,
                           coords, idx, N)
    r4_sign = sp_diag(lambda x: (-1) ** (int(x[0]) * int(x[1]) + int(x[0])),
                      coords, N)
    return compose(r4_sign, r4_perm)


# ============================================================================
# NEW MACHINERY (exact commutant enumeration + Z_2 grading)
# ============================================================================
def support_structures(D2):
    """Support graph adjacency (sets), BFS order/parent from site 0, distance,
    boolean adjacency, and D2's nonzero (rows, cols, values) support arrays."""
    N = D2.shape[0]
    Abool = (D2 != 0)
    adj = [set(np.nonzero(D2[i])[0].tolist()) for i in range(N)]
    # BFS order/parent/distance from 0
    order = [0]
    parent = -np.ones(N, dtype=np.int64)
    dist0 = -np.ones(N, dtype=np.int64)
    dist0[0] = 0
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for w in sorted(adj[u]):
            if w not in seen:
                seen.add(w)
                parent[w] = u
                dist0[w] = dist0[u] + 1
                order.append(w)
                q.append(w)
    connected = (len(order) == N)
    rows, cols = np.nonzero(D2)
    rows = rows.astype(np.int64)
    cols = cols.astype(np.int64)
    dvals = D2[rows, cols].astype(np.int64)
    return {
        "N": N, "adj": adj, "Abool": Abool, "order": order,
        "parent": parent, "dist0": dist0, "connected": connected,
        "rows": rows, "cols": cols, "dvals": dvals,
    }


def enumerate_stab0(sup):
    """All support-graph automorphisms fixing site 0, by backtracking with
    adjacency-intersection, distance and common-neighbour pruning. Every
    completion is verified by exact permuted-adjacency equality."""
    N = sup["N"]
    adj = sup["adj"]
    dist0 = sup["dist0"]
    Abool = sup["Abool"]
    # deterministic BFS order for the search (fixing 0 first)
    order = [0]
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for w in sorted(adj[u]):
            if w not in seen:
                seen.add(w)
                order.append(w)
                q.append(w)
    pos = {v: i for i, v in enumerate(order)}
    assigned_nbrs = [[u for u in sorted(adj[v]) if pos[u] < pos[v]] for v in order]
    # precompute common-neighbour targets against assigned neighbours
    common_target = []
    for v in order:
        d = {}
        for u in assigned_nbrs[pos[v]]:
            d[u] = len(adj[v] & adj[u])
        common_target.append(d)

    sols = []
    sigma = [-1] * N
    used = [False] * N
    sigma[0] = 0
    used[0] = True

    def rec(k):
        if k == len(order):
            sols.append(list(sigma))
            return
        v = order[k]
        anb = assigned_nbrs[k]
        cand = None
        for u in anb:
            simg = adj[sigma[u]]
            cand = set(simg) if cand is None else (cand & simg)
        dv = dist0[v]
        ct = common_target[k]
        for img in sorted(cand):
            if used[img]:
                continue
            if dist0[img] != dv:
                continue
            ok = True
            for u in anb:
                if len(adj[img] & adj[sigma[u]]) != ct[u]:
                    ok = False
                    break
            if not ok:
                continue
            sigma[v] = img
            used[img] = True
            rec(k + 1)
            used[img] = False
            sigma[v] = -1

    rec(1)
    # exact verification of every completion
    verified = []
    for sol in sols:
        sarr = np.array(sol, dtype=np.int64)
        if np.array_equal(Abool[np.ix_(sarr, sarr)], Abool):
            verified.append(sarr)
    return verified


def build_aut(lat, sup, stab_perms):
    """Aut = { T_v o sigma } via orbit-stabiliser: translations composed with
    Stab(0). Returns list of permutation arrays (int64)."""
    coords, idx, N = lat["coords"], lat["idx"], lat["N"]
    # translation permutations: shift by coords[v]
    trans_perm = np.empty((N, N), dtype=np.int64)
    for v in range(N):
        sh = coords[v]
        for i in range(N):
            x = coords[i]
            trans_perm[v, i] = idx(int(x[0] + sh[0]), int(x[1] + sh[1]), int(x[2] + sh[2]))
    aut = []
    for v in range(N):
        Tv = trans_perm[v]
        for sigma in stab_perms:
            aut.append(Tv[sigma])
    return aut


def grade_support(p, s, sup, D2):
    """Exact grade of signed permutation (p, s): +1 if U D2 U^{-1} = D2,
    -1 if = -D2, 0 otherwise. For automorphism perms this support-restricted
    integer test is exactly equivalent to the full N x N identity (both sides
    have identical nonzero counts)."""
    rows, cols, dvals = sup["rows"], sup["cols"], sup["dvals"]
    val = s[rows] * s[cols] * D2[p[rows], p[cols]]
    if np.array_equal(val, dvals):
        return 1
    if np.array_equal(val, -dvals):
        return -1
    return 0


def sign_lift(phi, sup, D2):
    """Exact integer sign lift of automorphism phi over the BFS spanning tree
    (s_0 = +1). Returns s if (phi, s) commutes with D2 (grade +1), else None."""
    N = sup["N"]
    order, parent = sup["order"], sup["parent"]
    s = np.ones(N, dtype=np.int64)
    for j in order[1:]:
        i = parent[j]
        s[j] = s[i] * D2[i, j] * D2[phi[i], phi[j]]
    if grade_support(phi, s, sup, D2) == 1:
        return s
    return None


def enumerate_commutant(lat, sup):
    """Exact Comm(D2): enumerate Stab(0), build Aut, sign-lift each automorphism,
    assemble Comm = {(p,+s),(p,-s)}. Returns dict of measurements + the group."""
    D2 = lat["D2"]
    N = lat["N"]
    stab = enumerate_stab0(sup)
    nStab = len(stab)
    aut = build_aut(lat, sup, stab)
    nAut = len(aut)
    # keys distinct (perm bytes)
    aut_keys = set(a.tobytes() for a in aut)
    keys_distinct = (len(aut_keys) == nAut)
    # spot-verify a deterministic spread of >= 200 full-Aut elements
    Abool = sup["Abool"]
    if nAut <= 256:
        spot_idx = range(nAut)
    else:
        spot_idx = np.unique(np.linspace(0, nAut - 1, 256).astype(int)).tolist()
    spot_ok = 0
    spot_tot = 0
    for i in spot_idx:
        a = aut[i]
        spot_tot += 1
        if np.array_equal(Abool[np.ix_(a, a)], Abool):
            spot_ok += 1
    # sign lift
    nLift = 0
    Comm = {}
    for phi in aut:
        s = sign_lift(phi, sup, D2)
        if s is None:
            continue
        nLift += 1
        g1 = (phi, s)
        g2 = (phi, -s)
        Comm[key(g1)] = g1
        Comm[key(g2)] = g2
    nComm = len(Comm)
    return {
        "nStab": nStab, "nAut": nAut, "keys_distinct": keys_distinct,
        "spot_ok": spot_ok, "spot_tot": spot_tot,
        "nLift": nLift, "nComm": nComm, "Comm": Comm,
    }


def find_generators(gdict, target_size, N):
    """Verified small generating set of a group given as key->(p,s): a set whose
    closure has exactly target_size elements. Deterministic (sorted by key)."""
    idg = (np.arange(N, dtype=np.int64), np.ones(N, dtype=np.int64))
    idk = key(idg)
    gens = []
    cur = {idk}
    for k in sorted(gdict.keys()):
        if k in cur:
            continue
        gens.append(gdict[k])
        cur = set(closure(gens).keys())
        if len(cur) == target_size:
            break
    return gens


def group_arrays(gdict):
    P = np.array([g[0] for g in gdict.values()], dtype=np.int64)
    S = np.array([g[1] for g in gdict.values()], dtype=np.int8)
    return P, S


def char_dim(gdict):
    P, S = group_arrays(gdict)
    chi = full_character(P, S)
    raw = float(np.mean(chi ** 2))
    return raw, int(round(raw))


def grade_partition(gdict, sup, D2):
    plus = minus = neither = 0
    for g in gdict.values():
        gr = grade_support(g[0], g[1], sup, D2)
        if gr == 1:
            plus += 1
        elif gr == -1:
            minus += 1
        else:
            neither += 1
    return plus, minus, neither


# ============================================================================
# per-L analysis
# ============================================================================
def analyze(L, want_extras):
    R = {"L": L}
    lat = build_lattice(L)
    N = lat["N"]
    D2 = lat["D2"]
    D2f = lat["D2f"]
    Jfull = lat["Jfull"]
    Seps = lat["Seps"]
    Pf = lat["Pf"]
    R["N"] = N
    R["lam"] = lat["lam"]
    R["mults"] = lat["mults"]

    # D2 integer + antisymmetric
    R["D2_integer"] = bool(np.array_equal(D2, np.round(D2)))
    R["D2_antisym"] = bool(np.array_equal(D2, -D2.T))

    grp = build_group(lat)
    R["nG"] = grp["nG"]
    R["nH"] = grp["nH"]
    Hdict = grp["H"]
    Hkeys = set(Hdict.keys())
    HP, HS = grp["HP"], grp["HS"]
    Seps_sp = grp["Seps_sp"]
    gens_H = grp["gens_H"]

    g_r4 = make_g_r4(lat)
    R["g_r4_comm"] = bool(commutes_with_D2(g_r4, D2))
    R["g_r4_in_H"] = key(g_r4) in Hdict

    sup = support_structures(D2)
    R["connected"] = sup["connected"]

    # dim A_nat = <D2, Jfull, Seps>
    _, dim_anat, closed_anat = word_algebra_real([D2f, Jfull, Seps], N, cap=400)
    R["dim_anat"] = dim_anat
    R["closed_anat"] = closed_anat

    # ---------------- exact commutant enumeration ----------------
    ce = enumerate_commutant(lat, sup)
    R.update({k: ce[k] for k in
              ("nStab", "nAut", "keys_distinct", "spot_ok", "spot_tot", "nLift", "nComm")})
    Comm = ce["Comm"]
    Commkeys = set(Comm.keys())

    # exhaustive exact commutation verification of ALL of Comm (full N x N)
    fails = 0
    for g in Comm.values():
        if not commutes_with_D2(g, D2):
            fails += 1
    R["comm_verify_fails"] = fails

    # closure spot-check: >= 400 deterministic pairwise products land in Comm
    comm_list = [Comm[k] for k in sorted(Commkeys)]
    nprod = min(400, len(comm_list))
    closed_prod_ok = 0
    for i in range(nprod):
        a = comm_list[i]
        b = comm_list[(i * 7 + 3) % len(comm_list)]
        if key(compose(a, b)) in Commkeys:
            closed_prod_ok += 1
    R["closed_prod_ok"] = closed_prod_ok
    R["closed_prod_tot"] = nprod

    # g_r4 in Comm \ H
    R["g_r4_in_Comm"] = key(g_r4) in Commkeys

    # ---------------- grading ----------------
    R["seps_grade"] = grade_support(Seps_sp[0], Seps_sp[1], sup, D2)
    R["seps_in_Comm"] = key(Seps_sp) in Commkeys

    # H grade partition
    R["H_part"] = grade_partition(Hdict, sup, D2)
    # H^+ subset Comm
    Hplus_in_comm = all(key(g) in Commkeys for g in Hdict.values()
                        if grade_support(g[0], g[1], sup, D2) == 1)
    R["Hplus_in_Comm"] = Hplus_in_comm

    # <H, g_r4>
    HG = closure(gens_H + [g_r4])
    HGkeys = set(HG.keys())
    R["nHG"] = len(HG)
    R["HG_part"] = grade_partition(HG, sup, D2)
    HGplus_in_comm = all(key(g) in Commkeys for g in HG.values()
                         if grade_support(g[0], g[1], sup, D2) == 1)
    R["HGplus_in_Comm"] = HGplus_in_comm
    R["HG_cap_Comm"] = len(HGkeys & Commkeys)
    R["HG_eq_Comm"] = (HGkeys == Commkeys)

    # explicit witnesses of difference
    commOnly = [k for k in sorted(Commkeys) if k not in HGkeys]
    hgOnly = [k for k in sorted(HGkeys) if k not in Commkeys]
    R["n_comm_not_hg"] = len(commOnly)
    R["n_hg_not_comm"] = len(hgOnly)
    if commOnly:
        g = Comm[commOnly[0]]
        R["comm_not_hg_witness"] = (grade_support(g[0], g[1], sup, D2),
                                    int(np.sum(g[1][g[0] == np.arange(N)])))
    if hgOnly:
        g = HG[hgOnly[0]]
        R["hg_not_comm_witness"] = (grade_support(g[0], g[1], sup, D2),
                                    int(np.sum(g[1][g[0] == np.arange(N)])))

    # verified generating set of Comm + graded commutant GC = closure(Comm, S_eps)
    comm_gens = find_generators(Comm, R["nComm"], N)
    R["n_comm_gens"] = len(comm_gens)
    R["comm_gens_close"] = (len(closure(comm_gens)) == R["nComm"])
    GC = closure(comm_gens + [Seps_sp])
    GCkeys = set(GC.keys())
    R["nGC"] = len(GC)
    R["GC_part"] = grade_partition(GC, sup, D2)
    R["Comm_subset_GC"] = Commkeys.issubset(GCkeys)
    R["H_subset_GC"] = Hkeys.issubset(GCkeys)
    R["HG_subset_GC"] = HGkeys.issubset(GCkeys)

    # grade multiplicativity over >= 400 deterministic GC products
    gc_list = [GC[k] for k in sorted(GCkeys)]
    ngc = min(400, len(gc_list))
    grade_mult_ok = 0
    for i in range(ngc):
        a = gc_list[i]
        b = gc_list[(i * 11 + 5) % len(gc_list)]
        ga = grade_support(a[0], a[1], sup, D2)
        gb = grade_support(b[0], b[1], sup, D2)
        ab = compose(a, b)
        gab = grade_support(ab[0], ab[1], sup, D2)
        if gab == ga * gb and ga in (1, -1) and gb in (1, -1):
            grade_mult_ok += 1
    R["grade_mult_ok"] = grade_mult_ok
    R["grade_mult_tot"] = ngc

    # ---------------- character (End) dims ----------------
    R["c_Comm_raw"], R["c_Comm"] = char_dim(Comm)
    R["c_HG_raw"], R["c_HG"] = char_dim(HG)
    R["c_H_raw"], R["c_H"] = char_dim(Hdict)

    # dim <A_nat, g_r4>
    U_gr4 = dense_from_sp(g_r4[0], g_r4[1].astype(float), N)
    _, dim_ag, closed_ag = word_algebra_real([D2f, Jfull, Seps, U_gr4], N, cap=600)
    R["dim_anat_gr4"] = dim_ag
    R["closed_anat_gr4"] = closed_ag

    # per-shell End_<H,g_r4> via copied shell machinery + shell-character cross-check
    HGP, HGS = group_arrays(HG)
    per_shell_sc = []
    per_shell_chi = []
    for m in range(len(Pf)):
        _, Bc = shell_commutant(Pf[m], HGP, HGS)
        per_shell_sc.append(len(Bc))
        chim = shell_character(Pf[m], HGP, HGS)
        per_shell_chi.append(int(round(float(np.mean(chim ** 2)))))
    R["per_shell_sc"] = per_shell_sc
    R["per_shell_chi"] = per_shell_chi

    # ---------------- L = 6 extras: sep6, generating-set displacement, omega ----------------
    if want_extras:
        shell3_Z, shell3_B = shell_commutant(Pf[3], HP, HS)
        _, blocks_m3 = isotypic_blocks(shell3_Z, shell3_B, 7)
        rank8 = [P for (d, mu, r, P) in blocks_m3 if mu == 1 and d == 8]
        P8a, P8b = rank8[0], rank8[1]
        sep6 = P8a - P8b
        R["sep6_rank_sum"] = int(round((np.trace(P8a) + np.trace(P8b)).real))
        R["sep6_norm"] = float(np.linalg.norm(sep6))
        sep_re = np.real(sep6).reshape(-1)
        sep_im = np.imag(sep6).reshape(-1)
        sep_norm2 = float(R["sep6_norm"] ** 2)

        # H-invariance of sep6 over gens_H + inverses
        l1_max = 0.0
        for g in gens_H:
            for gg in (g, sp_inv(g)):
                Uh = dense_from_sp(gg[0], gg[1].astype(float), N)
                l1_max = max(l1_max, float(np.linalg.norm(Uh @ sep6 @ Uh.T - sep6)))
        R["sep6_H_inv_max"] = l1_max

        # displacement of sep6 under the Comm generating set (moves it: not Comm-invariant)
        disp_max = 0.0
        disp_modsign_max = 0.0
        for g in comm_gens:
            Ug = dense_from_sp(g[0], g[1].astype(float), N)
            X = Ug @ sep6 @ Ug.T
            d_plain = float(np.linalg.norm(X - sep6))
            d_mod = min(d_plain, float(np.linalg.norm(X + sep6)))
            disp_max = max(disp_max, d_plain)
            disp_modsign_max = max(disp_modsign_max, d_mod)
        R["comm_disp_max"] = disp_max
        R["comm_disp_modsign_max"] = disp_modsign_max

        # omega for the first 5 deterministic Comm \ H elements
        commNotH = [k for k in sorted(Commkeys) if k not in Hkeys]
        omega_rows = []
        for k in commNotH[:5]:
            g = Comm[k]
            Ug = dense_from_sp(g[0], g[1].astype(float), N)
            B, dim, closed = word_algebra_real([D2f, Jfull, Seps, Ug], N, cap=600)
            if not closed:
                del B
                gc.collect()
                B, dim, closed = word_algebra_real([D2f, Jfull, Seps, Ug], N, cap=4300)
            w = (np.linalg.norm(B @ sep_re) ** 2 + np.linalg.norm(B @ sep_im) ** 2) / sep_norm2
            omega_rows.append((dim, closed, float(w)))
            del B
            gc.collect()
        R["omega_rows"] = omega_rows

        # PERT1: diag((-1)^x0) must classify as "neither"
        coords = lat["coords"]
        pert1 = sp_diag(lambda x: (-1) ** int(x[0]), coords, N)
        R["pert1_grade"] = grade_support(pert1[0], pert1[1], sup, D2)

        # PERT2: a valid Comm generator composed with an adjacent transposition must
        # FAIL exact commutation (full N x N check)
        nb0 = sorted(sup["adj"][0])[0]
        tp = np.arange(N, dtype=np.int64)
        tp[0], tp[nb0] = nb0, 0
        tau = (tp, np.ones(N, dtype=np.int64))
        corrupt = compose(comm_gens[0], tau)
        R["pert2_commutes"] = bool(commutes_with_D2(corrupt, D2))

    del Comm, HG, GC, Hdict
    gc.collect()
    return R


# ============================================================================
# MAIN
# ============================================================================
def main():
    t_start = time.time()
    np.set_printoptions(suppress=True)

    # expected values pinned by the gates below; every quantity is recomputed above
    XREF = {
        4: dict(nG=768, nH=1536, nStab=720, nAut=46080, nLift=3072, nComm=6144,
                c_Comm=7, c_HG=4, c_H=6, per_shell_chi=[1, 1, 1, 1],
                dim_anat_gr4=52, HG_part=(3072, 3072, 0), H_part=(768, 768, 0),
                nGC=12288, lam=[0, -4, -8, -12], mults=[8, 24, 24, 8]),
        6: dict(nG=2592, nH=5184, nStab=48, nAut=10368, nLift=10368, nComm=20736,
                c_Comm=7, c_HG=7, c_H=19, per_shell_chi=[1, 2, 2, 2],
                dim_anat_gr4=60, HG_part=(10368, 10368, 0), H_part=(2592, 2592, 0),
                nGC=41472, lam=[0, -3, -6, -9], mults=[8, 48, 96, 64]),
    }

    R4 = analyze(4, want_extras=False)
    print(f"[info] L=4 analysis done ({time.time()-t_start:.0f}s), peak RSS {rss_gb():.2f} GB",
          flush=True)
    R6 = analyze(6, want_extras=True)
    print(f"[info] L=6 analysis done ({time.time()-t_start:.0f}s), peak RSS {rss_gb():.2f} GB",
          flush=True)

    # ---------------- PHASE A probe (raw measured numbers) ----------------
    print("\n==================== PHASE A PROBE (raw measurements) ====================",
          flush=True)
    for R in (R4, R6):
        L = R["L"]
        print(f"\n---- L = {L} (N = {R['N']}) ----", flush=True)
        print(f"  M spectrum lam={R['lam']} mults={R['mults']}", flush=True)
        print(f"  D2 integer={R['D2_integer']} antisym={R['D2_antisym']} "
              f"support_connected={R['connected']}", flush=True)
        print(f"  |G_amb|={R['nG']} |H|={R['nH']} [H:G]={R['nH']//R['nG']} "
              f"dim A_nat={R['dim_anat']} (closed {R['closed_anat']})", flush=True)
        print(f"  |Stab_Aut(0)|={R['nStab']} |Aut|={R['nAut']} (=N*Stab {R['N']*R['nStab']}) "
              f"keys_distinct={R['keys_distinct']} spot_verify={R['spot_ok']}/{R['spot_tot']}",
              flush=True)
        print(f"  liftable={R['nLift']} (=48*N {48*R['N']}) |Comm|=2*liftable={R['nComm']} "
              f"commute_verify_fails={R['comm_verify_fails']} "
              f"closure_spotcheck={R['closed_prod_ok']}/{R['closed_prod_tot']}", flush=True)
        print(f"  grade(S_eps)={R['seps_grade']} S_eps_in_Comm={R['seps_in_Comm']} "
              f"g_r4: comm={R['g_r4_comm']} in_H={R['g_r4_in_H']} in_Comm={R['g_r4_in_Comm']}",
              flush=True)
        print(f"  H grade partition (+/-/neither)={R['H_part']} H+_subset_Comm={R['Hplus_in_Comm']}",
              flush=True)
        print(f"  |<H,g_r4>|={R['nHG']} grade partition={R['HG_part']} "
              f"HG+_subset_Comm={R['HGplus_in_Comm']} |HG cap Comm|={R['HG_cap_Comm']} "
              f"HG==Comm={R['HG_eq_Comm']}", flush=True)
        print(f"  |Comm\\HG|={R['n_comm_not_hg']} witness(grade,chi)={R.get('comm_not_hg_witness')} "
              f"|HG\\Comm|={R['n_hg_not_comm']} witness={R.get('hg_not_comm_witness')}", flush=True)
        print(f"  #Comm gens={R['n_comm_gens']} gens_close={R['comm_gens_close']} "
              f"|GC|=closure(Comm,S_eps)={R['nGC']} (2*|Comm|={2*R['nComm']}) "
              f"GC grade partition={R['GC_part']}", flush=True)
        print(f"  Comm_subset_GC={R['Comm_subset_GC']} H_subset_GC={R['H_subset_GC']} "
              f"HG_subset_GC={R['HG_subset_GC']} [GC:H]={R['nGC']//R['nH']}", flush=True)
        print(f"  grade_mult={R['grade_mult_ok']}/{R['grade_mult_tot']}", flush=True)
        print(f"  dim End_Comm={R['c_Comm']} (raw {R['c_Comm_raw']:.9f}) "
              f"dim End_<H,g_r4>={R['c_HG']} (raw {R['c_HG_raw']:.9f}) "
              f"dim End_H={R['c_H']} (raw {R['c_H_raw']:.9f})", flush=True)
        print(f"  per-shell End_<H,g_r4>: shell_commutant={R['per_shell_sc']} "
              f"shell_char={R['per_shell_chi']} (sum {sum(R['per_shell_chi'])})", flush=True)
        print(f"  dim <A_nat, g_r4>={R['dim_anat_gr4']} (closed {R['closed_anat_gr4']})",
              flush=True)
        if R["L"] == 6:
            print(f"  sep6 rank_sum={R['sep6_rank_sum']} ||sep6||={R['sep6_norm']:.10f} "
                  f"H_inv_max={R['sep6_H_inv_max']:.2e}", flush=True)
            print(f"  Comm-gen displacement max={R['comm_disp_max']:.6f} "
                  f"mod-sign max={R['comm_disp_modsign_max']:.6f} (4*sqrt2={4*2**0.5:.6f})",
                  flush=True)
            print(f"  PERT1 grade(diag(-1)^x0)={R['pert1_grade']} (expect 0/neither) "
                  f"PERT2 corrupted_commutes={R['pert2_commutes']} (expect False)", flush=True)
            print("  omega sample (Comm\\H, first 5): dim closed omega", flush=True)
            for i, (dim, closed, w) in enumerate(R["omega_rows"]):
                known = {0.0, 1/4, 4/15, 1/3, 1/2, 1.0}
                tag = "known" if any(abs(w - kv) < 1e-9 for kv in known) else "DISCOVERY"
                print(f"    om{i}: dim {dim:4d} closed {int(closed)} omega {w:.15f} [{tag}]",
                      flush=True)

    # ---------------- PHASE B gates ----------------
    print("\n==================== PHASE B GATES ====================", flush=True)
    for R in (R4, R6):
        L = R["L"]
        X = XREF[L]
        sfx = f"L{L}"

        gate(f"STRUCT_{sfx}",
             R["D2_integer"] and R["D2_antisym"] and R["connected"]
             and list(R["lam"]) == X["lam"] and list(R["mults"]) == X["mults"]
             and R["nG"] == X["nG"] and R["nH"] == X["nH"]
             and R["nH"] // R["nG"] == 2 and R["dim_anat"] == 16 and R["closed_anat"]
             and R["seps_in_Comm"] is False,
             f"D2 int/antisym, support connected, M spectrum {R['lam']} mults {R['mults']}, "
             f"|G|={R['nG']} |H|={R['nH']} [H:G]=2, "
             f"dim A_nat={R['dim_anat']}, S_eps not in Comm")

        gate(f"AUT_ENUM_{sfx}",
             R["nStab"] == X["nStab"] and R["nAut"] == X["nAut"]
             and R["nAut"] == R["N"] * R["nStab"] and R["keys_distinct"]
             and R["spot_ok"] == R["spot_tot"] and R["spot_tot"] >= 200,
             f"|Stab(0)|={R['nStab']} |Aut|={R['nAut']}=N*Stab, distinct keys, "
             f"spot-verified {R['spot_ok']}/{R['spot_tot']} automorphisms")

        gate(f"LIFT_{sfx}",
             R["nLift"] == X["nLift"] and R["nLift"] == 48 * R["N"]
             and R["nComm"] == X["nComm"] and R["nComm"] == 2 * R["nLift"],
             f"liftable={R['nLift']}=48*N, |Comm|={R['nComm']}=2*liftable")

        gate(f"COMM_VERIFY_{sfx}",
             R["comm_verify_fails"] == 0 and R["closed_prod_ok"] == R["closed_prod_tot"],
             f"all {R['nComm']} Comm elements commute exactly (fails {R['comm_verify_fails']}); "
             f"closure spot-check {R['closed_prod_ok']}/{R['closed_prod_tot']}")

        gate(f"GRADE_SEPS_{sfx}",
             R["seps_grade"] == -1 and R["seps_in_Comm"] is False,
             f"grade(S_eps)={R['seps_grade']} (anticommutes) => S_eps not in Comm; "
             f"H not contained in Comm")

        gate(f"GRADE_MULT_{sfx}",
             R["grade_mult_ok"] == R["grade_mult_tot"] and R["grade_mult_tot"] >= 400,
             f"grade multiplicative on {R['grade_mult_ok']}/{R['grade_mult_tot']} GC products")

        gate(f"GRADE_PART_{sfx}",
             tuple(R["H_part"]) == X["H_part"] and tuple(R["HG_part"]) == X["HG_part"]
             and R["H_part"][2] == 0 and R["HG_part"][2] == 0
             and R["Hplus_in_Comm"] and R["HGplus_in_Comm"],
             f"H partition {R['H_part']}, <H,g_r4> partition {R['HG_part']}, "
             f"0 neither, H+/HG+ subset Comm")

        gate(f"GC_{sfx}",
             R["nGC"] == X["nGC"] and R["nGC"] == 2 * R["nComm"]
             and R["GC_part"] == (R["nComm"], R["nComm"], 0)
             and R["Comm_subset_GC"] and R["H_subset_GC"] and R["HG_subset_GC"],
             f"|GC|={R['nGC']}={X['nGC']} (pinned) =2*|Comm|, partition {R['GC_part']} "
             f"(kernel=Comm), H and <H,g_r4> subset GC")

        gate(f"ORDER_COINCIDENCE_{sfx}",
             R["nHG"] == R["nComm"] and (not R["HG_eq_Comm"])
             and R["n_comm_not_hg"] > 0 and R["n_hg_not_comm"] > 0
             and R["HG_cap_Comm"] == R["nComm"] // 2,
             f"|<H,g_r4>|={R['nHG']}=|Comm| but distinct groups "
             f"(|Comm\\HG|={R['n_comm_not_hg']}, |HG\\Comm|={R['n_hg_not_comm']}), "
             f"|HG cap Comm|={R['HG_cap_Comm']}=|Comm|/2")

        gate(f"END_COMM_{sfx}",
             R["c_Comm"] == X["c_Comm"] and abs(R["c_Comm_raw"] - R["c_Comm"]) < 1e-6,
             f"dim End_Comm(C^N)={R['c_Comm']} (raw {R['c_Comm_raw']:.9f})")

        gate(f"END_HG_{sfx}",
             R["c_HG"] == X["c_HG"] and R["per_shell_sc"] == X["per_shell_chi"]
             and R["per_shell_chi"] == X["per_shell_chi"]
             and sum(R["per_shell_chi"]) == R["c_HG"],
             f"dim End_<H,g_r4>={R['c_HG']} = per-shell {R['per_shell_chi']} "
             f"(shell_commutant {R['per_shell_sc']} agrees)")

        gate(f"END_H_{sfx}",
             R["c_H"] == X["c_H"] and abs(R["c_H_raw"] - R["c_H"]) < 1e-6,
             f"dim End_H={R['c_H']} (landed anchor {X['c_H']}), End_Comm={R['c_Comm']} "
             f"({'L-stable' if R['c_Comm']==7 else 'CHANGED'}) vs End_H growing")

        rej = 20 if L == 6 else -1
        rej_note = ", explicit !=20 exclusion (redundant given the =60 pin)" if L == 6 else ""
        gate(f"WORD_R4_{sfx}",
             R["dim_anat_gr4"] == X["dim_anat_gr4"] and R["closed_anat_gr4"]
             and R["g_r4_comm"] and (not R["g_r4_in_H"]) and R["g_r4_in_Comm"]
             and R["dim_anat_gr4"] != rej,
             f"dim <A_nat,g_r4>={R['dim_anat_gr4']}={X['dim_anat_gr4']} pinned (closed), "
             f"g_r4 in Comm\\H{rej_note}")

    # L = 4 wrong-value rejector against the naive L = 6 guess
    gate("COMM_REJECT_L4", R4["nComm"] != 20736 and R4["nComm"] == 6144,
         f"|Comm|_L4={R4['nComm']} != 20736 (L=6 value); the two lattices differ")

    # L = 6 only structural / grading extras
    R = R6
    gate("SEP6_ANCHOR",
         R["sep6_rank_sum"] == 16 and abs(R["sep6_norm"] - 4.0) <= 1e-10
         and R["sep6_H_inv_max"] <= 1e-10,
         f"sep6 rank_sum={R['sep6_rank_sum']}, ||sep6||={R['sep6_norm']:.10f}, "
         f"H-invariance {R['sep6_H_inv_max']:.1e}")

    gate("SEP6_GENSET_MOVE",
         R["comm_gens_close"] and abs(R["comm_disp_max"] - 8.0) <= 1e-9
         and abs(R["comm_disp_modsign_max"] - 4 * 2 ** 0.5) <= 1e-9,
         f"Comm generating set closes to |Comm|; sep6 moved by Comm gens: "
         f"max disp {R['comm_disp_max']:.4f} (pinned 8), "
         f"mod-sign {R['comm_disp_modsign_max']:.4f} (pinned 4*sqrt2) "
         f"(H-specific: not Comm-invariant even up to sign)")

    om = R["omega_rows"]
    gate("OMEGA_SAMPLE",
         len(om) == 5 and all(c and d == 32 and abs(w) < 1e-9 for (d, c, w) in om),
         f"omega for 5 Comm\\H elements (sample, not census): "
         f"{[round(w,6) for (_,_,w) in om]} all closed, dim 32, omega 0 each")

    gate("PERT1_NEITHER", R["pert1_grade"] == 0,
         f"diag((-1)^x0) grade={R['pert1_grade']} (neither: classifier is not a "
         f"commute/anticommute proxy)")

    gate("PERT2_FAIL", R["pert2_commutes"] is False,
         f"Comm generator o adjacent transposition commutes={R['pert2_commutes']} "
         f"(exact verification rejects a corrupted element)")

    dt = time.time() - t_start
    print(f"\n[info] total wall-clock {dt:.0f}s, peak RSS {rss_gb():.2f} GB", flush=True)
    print(f"\nTOTAL: PASS={_P[0]} FAIL={_F[0]}", flush=True)
    sys.exit(0 if _F[0] == 0 else 1)


if __name__ == "__main__":
    main()
