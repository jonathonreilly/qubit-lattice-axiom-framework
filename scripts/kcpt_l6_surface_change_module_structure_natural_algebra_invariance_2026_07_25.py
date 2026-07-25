"""KCPT L = 6 surface-change / natural-algebra-invariance runner (self-contained).

Ports the KCPT structure map from the landed L = 4 lane (N = 64, 4^3 torus) to
L = 6 (N = 216, 6^3 torus, staggered lattice) and verifies a surface-change /
surface-stability dichotomy:

  - the ambient H-module gains multiplicity (End_H grows to C(+)M_2(+)... , dim 19,
    non-abelian) and the ambient commutant A' = End_H cap {D2}' cap {J}' grows to
    the 13-dimensional abelian center of A = <D2, J_full, rho(H)>, with minimal
    idempotent ranks [8,8,8,12,12,12,12,24,24,24,24,24,24] (dim A = 4224);
  - the natural Dirac core A_nat = <D2, J_full, S_eps> keeps the SAME abstract type
    M_2(C)^(+)4 with center Z = C[M] = span{shell projectors}, and stays numerically
    blind (gate overlap^2 <= 1e-10; observed ~1e-30) to the now 9-dimensional
    separator space (the L = 4 separator space is 1).

Everything (L = 6 AND the L = 4 self-calibration for E4) is built from scratch; no
external data files are loaded. All isotypic decompositions use the per-shell
H-averaged-commutant method (eigenvalue-multiplicity heuristics are not used) and
are seed-stable at two independent seeds. Runs single-threaded.

Gate contract: exits 0 with a final `TOTAL: PASS=N FAIL=0` line, N >= 30.
"""

import itertools
import time
import resource
import sys
import numpy as np

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


# ----------------------------------------------------------------------------
# lattice construction (staggered D2, shell projectors, complex structure J)
# ----------------------------------------------------------------------------
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
    # distinct M eigenvalues, descending (0, -3, -6, -9 for L=6; 0,-4,-8,-12 for L=4)
    rounded = np.round(evM).astype(int)
    distinct = sorted(set(rounded.tolist()), reverse=True)
    lam = distinct
    K = len(lam)

    # integer Lagrange shell projectors
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

    # kernel sign-vector basis V8 (dim 8)
    V8 = np.zeros((N, 8), dtype=float)
    for k, S in enumerate(SUBSETS):
        for i in range(N):
            x = coords[i]
            V8[i, k] = (-1) ** sum(x[j] for j in S)

    # complex structure J = Jker + Jbulk
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


# ----------------------------------------------------------------------------
# signed-permutation group G_amb and H = <G_amb, S_eps>
# ----------------------------------------------------------------------------
def sp_from_fmap(fmap, signfn, coords, idx, N):
    """Build (perm, sign) from a coordinate map fmap: x -> x' and sign function."""
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
    """Matrix product U_a @ U_b; on column vectors b acts first, then a."""
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
    # U D2 U^{-1} == D2  <=>  s_i s_j D2[p_i,p_j] == D2[i,j]
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

    # base coordinate maps: identity, U2 = (-x1,-x0,-x2), UR = (x1,x2,x0)
    def f_stab(x):
        return (x[0], x[1], x[2])

    def f_U2(x):
        return (-x[1], -x[0], -x[2])

    def f_UR(x):
        return (x[1], x[2], x[0])

    bases = [f_stab, f_U2, f_UR]

    # translations
    trans = []
    for t in coords:
        tt = t.copy()
        trans.append(sp_from_fmap(lambda x, tt=tt: (x[0] + tt[0], x[1] + tt[1], x[2] + tt[2]),
                                  lambda x: 1, coords, idx, N))

    # 6-bit quadratic sign fields over the three coordinates
    def make_signfn(bits):
        a1, a2, a3, b12, b13, b23 = bits

        def fn(x):
            e = (a1 * x[0] + a2 * x[1] + a3 * x[2]
                 + b12 * x[0] * x[1] + b13 * x[0] * x[2] + b23 * x[1] * x[2])
            return (-1) ** e
        return fn

    allbits = list(itertools.product([0, 1], repeat=6))

    # enumerate candidate signed perms U_base @ U_sign @ U_translation,
    # keeping those that commute with D2
    commuting = {}
    for base in bases:
        base_sp = sp_from_fmap(base, lambda x: 1, coords, idx, N)
        for bits in allbits:
            sf = sp_diag(make_signfn(bits), coords, N)
            g0 = compose(base_sp, sf)  # U_base @ U_sign
            for t in trans:
                g = compose(g0, t)
                if commutes_with_D2(g, D2):
                    commuting[key(g)] = g

    gens_all = list(commuting.values())
    Gamb = closure(gens_all)
    nG = len(Gamb)

    # small generating set for G_amb: keep only candidates that grow the closure
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

    # S_eps as signed perm
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


def conj_partition(elements, conj_gens):
    """Partition `elements` (dict key->g) into orbits under conjugation by conj_gens
    (which is closed under inverse). Elements not necessarily closed under conj is fine
    as long as conjugation stays inside the set (true for H-classes and G-orbits here)."""
    remaining = dict(elements)
    sizes = []
    while remaining:
        k0, g0 = next(iter(remaining.items()))
        orbit = {k0: g0}
        stack = [g0]
        while stack:
            g = stack.pop()
            for c in conj_gens:
                h = compose(compose(c, g), sp_inv(c))
                kh = key(h)
                if kh not in orbit:
                    orbit[kh] = h
                    stack.append(h)
        for k in orbit:
            remaining.pop(k, None)
        sizes.append(len(orbit))
    return sizes


# ----------------------------------------------------------------------------
# characters (dimension of End_H, per-shell commutant dims, cross-shell Hom)
# ----------------------------------------------------------------------------
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


# ----------------------------------------------------------------------------
# Frobenius helpers, word algebra, overlaps
# ----------------------------------------------------------------------------
def vec(A):
    return np.asarray(A, dtype=complex).reshape(-1)


def orth_add(B, A, tol=1e-9):
    v = vec(A)
    nv = np.linalg.norm(v)
    if nv < tol:
        return B, False
    v = v / nv
    for _ in range(2):
        if B.shape[0]:
            v = v - B.T @ (B.conj() @ v)
    r = np.linalg.norm(v)
    if r < tol:
        return B, False
    return np.vstack([B, v / r]), True


def word_algebra(gens, N, cap=400, tol=1e-9):
    gens = [np.asarray(g, dtype=complex) for g in gens]
    B = np.zeros((0, N * N), dtype=complex)
    B, _ = orth_add(B, np.eye(N))
    frontier = [np.eye(N, dtype=complex)]
    while frontier and B.shape[0] < cap:
        newf = []
        for w in frontier:
            for g in gens:
                p = g @ w
                B2, added = orth_add(B, p, tol)
                if added:
                    B = B2
                    newf.append(p)
        frontier = newf
    return B, len(frontier) == 0


def overlap2(B, X):
    if B.shape[0] == 0:
        return 0.0
    v = vec(X)
    v = v / np.linalg.norm(v)
    return float(np.linalg.norm(B.conj() @ v) ** 2)


def center_of(Blist, gens, tol=1e-10):
    """Center of span(Blist) as an algebra: elements commuting with generators `gens`."""
    d = len(Blist)
    Gm = np.zeros((d, d), dtype=complex)
    for gg in gens:
        gg = np.asarray(gg, dtype=complex)
        Cg = np.stack([(gg @ Xk - Xk @ gg).ravel() for Xk in Blist], axis=1)
        Gm += Cg.conj().T @ Cg
    w, V = np.linalg.eigh(Gm)
    thr = tol * max(w[-1].real, 1e-30)
    nidx = np.where(w < thr)[0]
    Z = [sum(V[k, j] * Blist[k] for k in range(d)) for j in nidx]
    return Z, len(nidx)


# ----------------------------------------------------------------------------
# rigorous per-shell isotypic decomposition (H-averaged commutant)
# ----------------------------------------------------------------------------
def shell_commutant(Pm, HP, HS, nR=14, build_seed=98765, chunk=512):
    """Return (Z, Bc): shell orthonormal basis Z (N x d) and orthonormal Frobenius
    basis Bc of End_H(shell) as d x d commutant matrices, via H-averaging."""
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
    """Rigorous isotypic decomposition of a shell from its commutant basis Bc.
    Returns (r_center, blocks) with blocks = [(irrep_dim, mult, rank, P_shell), ...]."""
    cm = len(Bc)
    d = Z.shape[1]
    # center of the commutant
    Gc = np.zeros((cm, cm), dtype=complex)
    for Xk in Bc:
        Cg = np.stack([(Xk @ Xj - Xj @ Xk).ravel() for Xj in Bc], axis=1)
        Gc += Cg.conj().T @ Cg
    wc, Vc = np.linalg.eigh(Gc)
    thr = 1e-8 * max(wc[-1].real, 1e-30)
    nidx = np.where(wc < thr)[0]
    rC = len(nidx)
    Zc = [sum(Vc[k, j] * Bc[k] for k in range(cm)) for j in nidx]
    # generic central Hermitian element
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


# ----------------------------------------------------------------------------
# ambient commutant A' = End_H cap {D2}' cap {J}'  (from embedded shell commutants)
# ----------------------------------------------------------------------------
def build_aprime(shell_ZB, D2f, Jfull, N):
    XH = []
    for Z, Bc in shell_ZB:
        for B in Bc:
            XH.append(Z @ B @ Z.conj().T)
    dH = len(XH)
    Gm = np.zeros((dH, dH), dtype=complex)
    for gg in (D2f.astype(complex), np.asarray(Jfull, dtype=complex)):
        Cg = np.stack([(gg @ Xk - Xk @ gg).ravel() for Xk in XH], axis=1)
        Gm += Cg.conj().T @ Cg
    w, V = np.linalg.eigh(Gm)
    thr = 1e-10 * max(w[-1].real, 1e-30)
    nidx = np.where(w < thr)[0]
    q = len(nidx)
    Aprime = [sum(V[k, j] * XH[k] for k in range(dH)) for j in nidx]
    return XH, Aprime, q, w


def idempotent_ranks(Aprime, seed, q):
    rng = np.random.default_rng(seed)
    C = sum(rng.standard_normal() * A for A in Aprime)
    Hc = C + C.conj().T
    ev, U = np.linalg.eigh(Hc)
    if q > 1:
        gaps = np.diff(ev)
        cut = np.sort(np.argsort(gaps)[-(q - 1):])
    else:
        cut = []
    groups = []
    start = 0
    for c in cut:
        groups.append(np.arange(start, c + 1))
        start = c + 1
    groups.append(np.arange(start, len(ev)))
    return sorted(len(g) for g in groups)


def dense_from_sp(p, s, N):
    U = np.zeros((N, N), dtype=float)
    U[np.arange(N), p] = s
    return U


# ============================================================================
# MAIN
# ============================================================================
def main():
    t_start = time.time()
    np.set_printoptions(suppress=True)

    # -------------------- build L = 6 --------------------
    lat = build_lattice(6)
    N = lat["N"]
    D2 = lat["D2"]
    D2f = lat["D2f"]
    Jfull = lat["Jfull"]
    Pf = lat["Pf"]
    Seps = lat["Seps"]
    lam = lat["lam"]
    mults = lat["mults"]
    V8 = lat["V8"]
    print(f"[info] L=6 built: N={N}, M spectrum {lam}, shell mults {mults} "
          f"({time.time()-t_start:.0f}s)", flush=True)

    # ================= SECTION A: staggered D2, spectrum, kernel, J =================
    gate("A1", D2.dtype.kind in "iu" and np.array_equal(D2, -D2.T),
         "D2 integer and D2^T = -D2")

    exp_spec = [0, -3, -6, -9]
    exp_mults = [8, 48, 96, 64]
    evM = np.linalg.eigvalsh(lat["M"].astype(float))
    # clusters separated by >= 1
    rr = np.sort(np.round(evM))
    gap_ok = True
    for a, b in zip(rr[:-1], rr[1:]):
        if b - a > 1e-6 and b - a < 1.0:
            gap_ok = False
    max_round_err = float(np.max(np.abs(evM - np.round(evM))))
    gate("A2", lam == exp_spec and mults == exp_mults and gap_ok and max_round_err < 1e-6,
         f"M spectrum {lam} mults {mults}, cluster gap>=1 ({gap_ok}), "
         f"max|ev-round|={max_round_err:.1e}")

    from math import comb
    formula = [comb(3, m) * 2 ** (3 - m) * 4 ** m for m in range(4)]
    gate("A3", formula == exp_mults and sum(formula) == 216,
         f"mult formula C(3,m)*2^(3-m)*4^m = {formula}, sum {sum(formula)}")

    ker_resid = float(np.max(np.abs(D2f @ V8)))
    rank_ker = np.linalg.matrix_rank(V8, tol=1e-9)
    entries_pm1 = np.all(np.abs(np.abs(V8) - 1.0) < 1e-12)
    gate("A4", ker_resid < 1e-10 and rank_ker == 8 and entries_pm1,
         f"ker dim 8, D2@V8 resid {ker_resid:.1e}, entries +/-1 {entries_pm1}")

    J_real = float(np.max(np.abs(Jfull.imag))) if np.iscomplexobj(Jfull) else 0.0
    antisym = float(np.max(np.abs(Jfull + Jfull.T)))
    J2 = Jfull @ Jfull
    j2_resid = float(np.max(np.abs(J2 + np.eye(N))))
    gate("A5", J_real < 1e-10 and antisym < 1e-10 and j2_resid < 1e-10,
         f"J real (im {J_real:.1e}), antisym {antisym:.1e}, ||J^2+I|| {j2_resid:.1e}")

    # ================= SECTION B: symmetry group, chi_sgn census =================
    t0 = time.time()
    grp = build_group(lat)
    nG, nH = grp["nG"], grp["nH"]
    HP, HS = grp["HP"], grp["HS"]
    Gkeys = grp["Gkeys"]
    print(f"[info] groups built: |G_amb|={nG}, |H|={nH} ({time.time()-t0:.0f}s)", flush=True)

    seps_in_G = key(grp["Seps_sp"]) in Gkeys
    gate("B1", nG == 2592 and nH == 5184 and (nH // nG) == 2 and not seps_in_G,
         f"|G_amb|={nG}=6^3*12, |H|={nH}, [H:G]={nH//nG}, S_eps in G_amb: {seps_in_G}")

    # H conjugacy classes
    conj_gens = grp["gens_H"] + [sp_inv(g) for g in grp["gens_H"]]
    from collections import Counter
    hclass_sizes = conj_partition(grp["H"], conj_gens)
    hc = dict(Counter(hclass_sizes))
    exp_hc = {1: 2, 2: 5, 3: 4, 4: 3, 6: 24, 12: 57, 54: 6, 72: 6, 108: 21, 144: 9}
    gate("B2", len(hclass_sizes) == 137 and hc == exp_hc,
         f"{len(hclass_sizes)} H-classes, size multiset {dict(sorted(hc.items()))}")

    # G_amb orbits under H-conjugation
    gorbit_sizes = conj_partition(grp["Gamb"], conj_gens)
    go = dict(Counter(gorbit_sizes))
    exp_go = {1: 2, 2: 3, 3: 4, 4: 1, 6: 14, 12: 27, 54: 6, 72: 6, 108: 9, 144: 3}
    gate("B3", len(gorbit_sizes) == 75 and go == exp_go,
         f"{len(gorbit_sizes)} G-orbits under H-conj, size multiset {dict(sorted(go.items()))}")

    # chi_sgn census: h D2 h^T = +/- D2 for every h
    ar = np.arange(N)
    cnt_p = 0
    cnt_m = 0
    cnt_bad = 0
    chisgn = {}
    for h in range(nH):
        p = HP[h]
        s = HS[h].astype(np.int64)
        A = (s[:, None] * s[None, :]) * D2[np.ix_(p, p)]
        if np.array_equal(A, D2):
            cnt_p += 1
            chisgn[HP[h].tobytes() + HS[h].astype(np.int8).tobytes()] = 1
        elif np.array_equal(A, -D2):
            cnt_m += 1
            chisgn[HP[h].tobytes() + HS[h].astype(np.int8).tobytes()] = -1
        else:
            cnt_bad += 1
    gate("B4", cnt_p == 2592 and cnt_m == 2592 and cnt_bad == 0,
         f"chi_sgn=+1 on {cnt_p}, =-1 on {cnt_m}, neither on {cnt_bad}")

    # ker chi_sgn = G_amb (set equality)
    plus_keys = set(k for k, v in chisgn.items() if v == 1)
    # note: chisgn keys use int8 sign bytes, matching key() convention
    gate("B5", plus_keys == Gkeys,
         f"ker chi_sgn set == G_amb ({len(plus_keys)} vs {len(Gkeys)})")

    # multiplicativity on 400 seeded pairs
    Hlist = [(HP[h], HS[h].astype(np.int64)) for h in range(nH)]

    def chi_of(p, s):
        A = (s[:, None] * s[None, :]) * D2[np.ix_(p, p)]
        if np.array_equal(A, D2):
            return 1
        if np.array_equal(A, -D2):
            return -1
        return 0
    rng = np.random.default_rng(20260725)
    mult_ok = True
    for _ in range(400):
        i, j = int(rng.integers(nH)), int(rng.integers(nH))
        gh = compose(Hlist[i], Hlist[j])
        if chi_of(*gh) != chi_of(*Hlist[i]) * chi_of(*Hlist[j]):
            mult_ok = False
            break
    gate("B6", mult_ok, "chi_sgn multiplicative on 400 seeded pairs")

    seps_p, seps_s = grp["Seps_sp"]
    A_seps = (seps_s[:, None] * seps_s[None, :]) * D2[np.ix_(seps_p, seps_p)]
    gate("B7", np.array_equal(A_seps, -D2) and chi_of(seps_p, seps_s.astype(np.int64)) == -1,
         "S_eps D2 S_eps = -D2, chi_sgn(S_eps) = -1")

    # B8: H is NOT the maximal signed-permutation symmetry group of D2 — explicit
    # witness g_r4 = diag((-1)^(x0*x1 + x0)) @ R4, where R4 implements
    # r4: x -> (x1, -x0, x2). Thus R4 acts first and the sign field second on
    # column vectors. This commutes with D2 exactly (chi_sgn = +1) yet lies outside H.
    r4_perm = sp_from_fmap(lambda x: (x[1], -x[0], x[2]), lambda x: 1,
                           lat["coords"], lat["idx"], N)
    r4_sign = sp_diag(lambda x: (-1) ** (int(x[0]) * int(x[1]) + int(x[0])),
                      lat["coords"], N)
    g_r4 = compose(r4_sign, r4_perm)
    r4_comm = commutes_with_D2(g_r4, D2)
    r4_in_H = key(g_r4) in grp["H"]
    gate("B8", r4_comm and not r4_in_H,
         f"dressed-r4 witness: commutes with D2 {r4_comm}, in H {r4_in_H} (H not maximal)")

    # ================= SECTION C: End_H structure (character + rigorous isotypic) ===
    t0 = time.time()
    chi = full_character(HP, HS)
    cH_char = int(round(np.mean(chi ** 2)))
    chi_m = [shell_character(Pf[m], HP, HS) for m in range(4)]
    cm_char = [int(round(np.mean(chi_m[m] ** 2))) for m in range(4)]
    cross_max = max(abs(np.mean(chi_m[a] * chi_m[b])) for a in range(4) for b in range(4) if a != b)
    exp_cm = [1, 4, 8, 6]

    # embedded shell commutant bases (rigorous H-averaged commutant), reused for C/E
    shell_ZB = []
    for m in range(4):
        Z, Bc = shell_commutant(Pf[m], HP, HS)
        shell_ZB.append((Z, Bc))
    cm_dim = [len(Bc) for _, Bc in shell_ZB]
    cH_dim = sum(cm_dim)
    print(f"[info] End_H: char c_H={cH_char}, dim c_H={cH_dim}, c_m(char)={cm_char}, "
          f"c_m(dim)={cm_dim} ({time.time()-t0:.0f}s)", flush=True)
    gate("C1", cH_char == 19 and cH_dim == 19 and cm_char == exp_cm and cm_dim == exp_cm
         and cross_max < 1e-8 and (1 + 4 + 8 + 6) == 19,
         f"c_H=19 (char & dim), c_m={cm_char}, cross-shell Hom max {cross_max:.1e}, 19=1+4+8+6")

    exp_tables = {
        0: sorted([(8, 1)]),
        1: sorted([(24, 2)]),
        2: sorted([(12, 1), (12, 1), (12, 1), (12, 1), (24, 2)]),
        3: sorted([(8, 1), (8, 1), (24, 2)]),
    }
    tables_by_seed = {}
    blocks_by_seed = {}
    for seed in (7, 1234):
        tabs = {}
        blks = {}
        ok = True
        for m in range(4):
            Z, Bc = shell_ZB[m]
            rC, blocks = isotypic_blocks(Z, Bc, seed)
            tab = sorted((d, mu) for (d, mu, r, P) in blocks)
            tabs[m] = tab
            blks[m] = blocks
            if tab != exp_tables[m]:
                ok = False
        tables_by_seed[seed] = tabs
        blocks_by_seed[seed] = blks
        gate(f"C2s{seed}",
             ok,
             f"isotypic tables seed {seed}: "
             + "; ".join(f"m{m}:{tabs[m]}" for m in range(4)))

    agree = tables_by_seed[7] == tables_by_seed[1234]
    # consistency: sum mult^2 = c_m and sum mult*dim = shell dim
    c3_ok = agree
    for m in range(4):
        blocks = blocks_by_seed[7][m]
        s_mult2 = sum(mu * mu for (d, mu, r, P) in blocks)
        s_multdim = sum(mu * d for (d, mu, r, P) in blocks)
        if s_mult2 != exp_cm[m] or s_multdim != mults[m]:
            c3_ok = False
    gate("C3", c3_ok,
         "two-seed agreement + sum(mult^2)=c_m + sum(mult*dim)=shell dim per shell")

    # non-abelian End_H: exhibit two commutant elements with ||[X,Y]||_F > 0.1
    XH_full = []
    for Z, Bc in shell_ZB:
        for B in Bc:
            XH_full.append(Z @ B @ Z.conj().T)
    max_comm = 0.0
    for i in range(len(XH_full)):
        for j in range(i + 1, len(XH_full)):
            c = np.linalg.norm(XH_full[i] @ XH_full[j] - XH_full[j] @ XH_full[i])
            if c > max_comm:
                max_comm = c
    gate("C4", max_comm > 0.1,
         f"End_H non-abelian: max pairwise ||[X,Y]||_F = {max_comm:.3f} "
         f"(L=4 landed comparison: abelian C^6)")

    # ================= SECTION D: natural algebra A_nat = <D2,J,S_eps> =============
    t0 = time.time()
    Bnat, closed = word_algebra([D2f, Jfull, Seps], N, cap=400, tol=1e-9)
    gate("D1", Bnat.shape[0] == 16 and closed,
         f"dim A_nat = {Bnat.shape[0]}, closed below cap = {closed}")

    Xnat = [Bnat[k].reshape(N, N) for k in range(Bnat.shape[0])]
    Znat, zdim = center_of(Xnat, [D2f, Jfull, Seps], tol=1e-10)
    # build orthonormal center basis then check each P_m lies in it
    BZc = np.zeros((0, N * N), dtype=complex)
    for z in Znat:
        BZc, _ = orth_add(BZc, z)
    ov_center = [overlap2(BZc, Pf[m]) for m in range(4)]
    gate("D2", zdim == 4 and all(o >= 1 - 1e-10 for o in ov_center),
         f"dim Z(A_nat)={zdim}, overlap^2(Z, P_m) min {min(ov_center):.12f}")

    # Wedderburn at two seeds
    def wedderburn(seed):
        rngw = np.random.default_rng(seed)
        C = sum(rngw.standard_normal() * z for z in Znat)
        Hc = (C + C.conj().T) / 2
        ev, U = np.linalg.eigh(Hc)
        if zdim > 1:
            gaps = np.diff(ev)
            cut = np.sort(np.argsort(gaps)[-(zdim - 1):])
        else:
            cut = []
        groups = []
        start = 0
        for c in cut:
            groups.append(np.arange(start, c + 1))
            start = c + 1
        groups.append(np.arange(start, len(ev)))
        res = []
        for gr in groups:
            cols = U[:, gr]
            P = cols @ cols.conj().T
            rank = int(round(np.trace(P).real))
            # block algebra: A_nat elements compressed to this block
            bb = []
            for Xk in Xnat:
                Y = P @ Xk @ P
                for Q in bb:
                    Y = Y - np.vdot(Q, Y) * Q
                nrm = np.sqrt(abs(np.vdot(Y, Y)))
                if nrm > 1e-8:
                    bb.append(Y / nrm)
            block_alg_dim = len(bb)
            # center of the block algebra M_2(C): elements of span(bb) commuting with bb
            if bb:
                _, bcent = center_of(bb, bb, tol=1e-9)
            else:
                bcent = 0
            # shell match
            match = min(float(np.linalg.norm(P - Pf[m])) for m in range(4))
            res.append((rank, block_alg_dim, bcent, match))
        return sorted(res)

    for seed in (7, 1234):
        res = wedderburn(seed)
        ranks = sorted(r[0] for r in res)
        alg_dims = [r[1] for r in res]
        cents = [r[2] for r in res]
        matches = [r[3] for r in res]
        ok = (ranks == [8, 48, 64, 96]
              and all(a == 4 for a in alg_dims)
              and all(c == 1 for c in cents)
              and max(matches) <= 1e-10)
        gate(f"D3s{seed}", ok,
             f"4 blocks, ranks {ranks}, block-alg dim {alg_dims} (=>M_2), "
             f"block-center {cents}, max||P_block-P_shell|| {max(matches):.1e}")

    ov_pos = [overlap2(Bnat, Pf[m]) for m in range(4)]
    gate("D4", all(o >= 1 - 1e-10 for o in ov_pos),
         f"positive control overlap^2(A_nat, P_m) min {min(ov_pos):.12f}")

    print(f"[info] section D done ({time.time()-t0:.0f}s)", flush=True)

    # ================= SECTION E: ambient A', separators, blindness ================
    t0 = time.time()
    XH, Aprime, q, wgram = build_aprime(shell_ZB, D2f, Jfull, N)
    ws = np.sort(wgram.real)
    null_max = ws[q - 1] if q >= 1 else 0.0
    first_nonnull = ws[q] if q < len(ws) else np.inf
    scale = ws[-1]
    gate("E1", q == 13 and null_max <= 1e-10 * scale and first_nonnull >= 1e-2 * scale,
         f"dim A' = {q}; Gram null_max {null_max:.2e}, first non-null {first_nonnull:.2e}, "
         f"scale {scale:.2e}")

    comm_max = 0.0
    for i in range(len(Aprime)):
        for j in range(i + 1, len(Aprime)):
            c = np.linalg.norm(Aprime[i] @ Aprime[j] - Aprime[j] @ Aprime[i])
            if c > comm_max:
                comm_max = c
    gate("E2", comm_max <= 1e-10, f"A' abelian: max pairwise ||[A,B]||_F = {comm_max:.2e}")

    exp_ranks6 = [8, 8, 8, 12, 12, 12, 12, 24, 24, 24, 24, 24, 24]
    for seed in (11, 2024):
        ranks = idempotent_ranks(Aprime, seed, q)
        dimA = sum(r * r for r in ranks)
        gate(f"E3s{seed}", ranks == exp_ranks6 and sum(ranks) == 216 and dimA == 4224,
             f"ranks {ranks}, sum {sum(ranks)}, dim A = sum r_i^2 = {dimA}")

    # E4: L = 4 self-calibration through the identical A' machinery
    lat4 = build_lattice(4)
    grp4 = build_group(lat4)
    HP4, HS4 = grp4["HP"], grp4["HS"]
    shell_ZB4 = []
    for m in range(lat4["K"]):
        Z4, Bc4 = shell_commutant(lat4["Pf"][m], HP4, HS4)
        shell_ZB4.append((Z4, Bc4))
    _, Aprime4, q4, _ = build_aprime(shell_ZB4, lat4["D2f"], lat4["Jfull"], lat4["N"])
    ranks4a = idempotent_ranks(Aprime4, 11, q4)
    ranks4b = idempotent_ranks(Aprime4, 2024, q4)
    dimA4 = sum(r * r for r in ranks4a)
    gate("E4", q4 == 5 and ranks4a == [8, 8, 12, 12, 24] and ranks4a == ranks4b
         and dimA4 == 992 and grp4["nH"] == 1536,
         f"L=4: |H|={grp4['nH']}, dim A'={q4}, ranks {ranks4a}, dim A = {dimA4}")

    # E4b: the landed L = 4 comparison facts asserted in the note, gated from
    # scratch: End_H(C^64) = C^6 and abelian (character count == per-shell
    # commutant dim sum == 6, so cross-shell Homs vanish; all per-shell commutant
    # generators commute), and the dressed-r4 witness of B8 lies outside H at
    # L = 4 as well
    chi4 = full_character(HP4, HS4)
    cH4_char = int(round(np.mean(chi4 ** 2)))
    cm4_dim = sum(len(Bc) for _, Bc in shell_ZB4)
    comm4_max = 0.0
    for _, Bc in shell_ZB4:
        for i in range(len(Bc)):
            for j in range(i + 1, len(Bc)):
                c = np.linalg.norm(Bc[i] @ Bc[j] - Bc[j] @ Bc[i])
                comm4_max = max(comm4_max, c)
    r4_perm4 = sp_from_fmap(lambda x: (x[1], -x[0], x[2]), lambda x: 1,
                            lat4["coords"], lat4["idx"], lat4["N"])
    r4_sign4 = sp_diag(lambda x: (-1) ** (int(x[0]) * int(x[1]) + int(x[0])),
                       lat4["coords"], lat4["N"])
    g_r44 = compose(r4_sign4, r4_perm4)
    r44_comm = commutes_with_D2(g_r44, lat4["D2"])
    r44_in_H = key(g_r44) in grp4["H"]
    gate("E4b", cH4_char == 6 and cm4_dim == 6 and comm4_max <= 1e-10
         and r44_comm and not r44_in_H,
         f"L=4: End_H = C^6 abelian (char {cH4_char}, dim {cm4_dim}, "
         f"max ||[X,Y]||_F {comm4_max:.1e}); dressed-r4 commutes {r44_comm}, in H {r44_in_H}")

    # E5: separator complement of C[M] inside A'
    BZ = np.zeros((0, N * N), dtype=complex)
    for m in range(4):
        BZ, added = orth_add(BZ, Pf[m])
    n_cm = BZ.shape[0]
    extras = []
    for A in Aprime:
        BZ2, added = orth_add(BZ, A)
        if added:
            extras.append(BZ2[-1].reshape(N, N))
            BZ = BZ2
    # L=4 comparison
    BZ4 = np.zeros((0, lat4["N"] * lat4["N"]), dtype=complex)
    for m in range(lat4["K"]):
        BZ4, _ = orth_add(BZ4, lat4["Pf"][m])
    n_cm4 = BZ4.shape[0]
    extras4 = 0
    for A in Aprime4:
        BZ4b, added = orth_add(BZ4, A)
        if added:
            extras4 += 1
            BZ4 = BZ4b
    gate("E5", n_cm == 4 and len(extras) == 9 and n_cm4 == 4 and extras4 == 1,
         f"L=6 separator complement dim {len(extras)} (C[M] dim {n_cm}); "
         f"L=4 comparison dim {extras4}")

    # sep6 from m=3 rank-8 mult-1 isotypic pair (seed 7 blocks)
    blocks_m3 = blocks_by_seed[7][3]
    rank8 = [P for (d, mu, r, P) in blocks_m3 if mu == 1 and d == 8]
    P8a, P8b = rank8[0], rank8[1]
    sep6 = P8a - P8b
    rank_sum = int(round((np.trace(P8a) + np.trace(P8b)).real))
    sep6_norm = float(np.linalg.norm(sep6))
    # commutes with D2, J, 400 seeded rho(h)
    cD = float(np.linalg.norm(sep6 @ D2f - D2f @ sep6))
    cJ = float(np.linalg.norm(sep6 @ Jfull - Jfull @ sep6))
    rng2 = np.random.default_rng(424242)
    cH_max = 0.0
    for _ in range(400):
        h = int(rng2.integers(nH))
        U = dense_from_sp(HP[h], HS[h].astype(float), N)
        c = float(np.linalg.norm(sep6 @ U - U @ sep6))
        if c > cH_max:
            cH_max = c
    gate("E6", rank_sum == 16 and abs(sep6_norm - 4.0) <= 1e-10
         and cD <= 1e-10 and cJ <= 1e-10 and cH_max <= 1e-10,
         f"sep6 rank sum {rank_sum}, ||sep6||_F {sep6_norm:.12f}, "
         f"[sep6,D2] {cD:.1e}, [sep6,J] {cJ:.1e}, max[sep6,rho(h)] {cH_max:.1e}")

    # E7a: 9 complement directions blind to A_nat
    ov_extras = [overlap2(Bnat, E) for E in extras]
    gate("E7a", len(ov_extras) == 9 and max(ov_extras) <= 1e-10,
         f"overlap^2(A_nat, 9 complement dirs) max {max(ov_extras):.2e}")

    # E7b: named separators (sep6 + six m=2 quartet pairwise differences) blind
    blocks_m2 = blocks_by_seed[7][2]
    rank12 = [P for (d, mu, r, P) in blocks_m2 if mu == 1 and d == 12]
    quartet_diffs = []
    for i in range(len(rank12)):
        for j in range(i + 1, len(rank12)):
            quartet_diffs.append(rank12[i] - rank12[j])
    named = [sep6] + quartet_diffs
    ov_named = [overlap2(Bnat, X) for X in named]
    gate("E7b", len(rank12) == 4 and len(quartet_diffs) == 6 and max(ov_named) <= 1e-10,
         f"sep6 + {len(quartet_diffs)} quartet diffs blind: overlap^2 max {max(ov_named):.2e}")

    # E8: wrong-value rejector -- augment A_nat with sep6/||sep6|| flips overlap^2 to 1
    Bnat_aug, added = orth_add(Bnat.copy(), sep6 / sep6_norm)
    ov_aug = overlap2(Bnat_aug, sep6)
    gate("E8", added and ov_aug >= 1 - 1e-10,
         f"augmented A_nat basis: overlap^2(aug, sep6) = {ov_aug:.12f}")

    print(f"[info] section E done ({time.time()-t0:.0f}s)", flush=True)

    # -------------------- summary --------------------
    dt = time.time() - t_start
    print(f"[info] wall-clock {dt:.1f}s, peak RSS {rss_gb():.2f} GB", flush=True)
    print(f"TOTAL: PASS={_P[0]} FAIL={_F[0]}", flush=True)
    sys.exit(0 if _F[0] == 0 else 1)


if __name__ == "__main__":
    main()
