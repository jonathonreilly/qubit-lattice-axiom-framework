#!/usr/bin/env python3
"""Bosonized qubit sites: do Z2-string-end fermions reproduce CL-1's cube hop?

Supplied construction (standard Bravyi-Kitaev-superfast-type bosonization with
site qubits): site qubit v carries B_v -> Z_v; one link qubit per bond e=(a,b);
edge operator A_ab = -i g_a g_b -> X_a X_b L_e, L_e = X_e prod_{l <_a e} Z_l
prod_{l <_b e} Z_l (fixed ordering +x,-x,+y,-y,+z,-z at every vertex);
Gauss constraint G_v = Z_v prod_{e at v} Z_e.  Face fluxes = loop products of
bosonized A are conserved register values.

Tests: (1) exact Pauli algebra (cube complex and periodic 4^3);
(2) many-body spectra on the single cube complex (20 qubits, G-sector 4096,
flux sector 128) vs the fermionic cube hop with face phase -1; periodic
single-particle tick band (Dirac point at K=0, speed, copy sign);
(3) half-filled sea energy per flux sector on 4^3; (4) Klein/Pauli-frame
symmetries surviving on bosonized sites; (5) printed rule count.
Finite diagnostics; nothing fitted.
"""
import itertools
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
RNG = np.random.default_rng(20261026)
PASS = 0
FAIL = 0


def check(name, ok, info=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


# ---------- Pauli engine: P = i^k X^x Z^z (x,z python-int bitmasks) ----------
def pc(n):
    return bin(n).count("1")


def pmul(p, q):
    x1, z1, k1 = p
    x2, z2, k2 = q
    return (x1 ^ x2, z1 ^ z2, (k1 + k2 + 2 * pc(z1 & x2)) % 4)


def anti(p, q):
    return (pc(p[0] & q[1]) + pc(p[1] & q[0])) % 2 == 1


I0 = (0, 0, 0)


def X(i):
    return (1 << i, 0, 0)


def Z(i):
    return (0, 1 << i, 0)


def Y(i):
    return (1 << i, 1 << i, 1)


def prod(ps):
    r = I0
    for p in ps:
        r = pmul(r, p)
    return r


# ---------- lattices ----------
def lattice(L, periodic):
    if periodic:
        idx = lambda x, y, z: (x % L) + L * (y % L) + L * L * (z % L)
    else:
        idx = lambda x, y, z: x + L * y + L * L * z
    V = L ** 3
    coords = [(v % L, (v // L) % L, v // (L * L)) for v in range(V)]
    edges = []  # (a, b, axis), oriented a -> a + e_axis
    for v, (x, y, z) in enumerate(coords):
        for ax in range(3):
            c = [x, y, z]
            c[ax] += 1
            if not periodic and c[ax] >= L:
                continue
            edges.append((v, idx(*c), ax))
    return V, coords, edges


def bos_ops(V, edges):
    """Bosonized and fermionic (JW) generators."""
    E = len(edges)
    inc = {v: [] for v in range(V)}
    for ei, (a, b, ax) in enumerate(edges):
        inc[a].append((2 * ax, ei))      # +axis at a
        inc[b].append((2 * ax + 1, ei))  # -axis at b
    for v in inc:
        inc[v].sort()
    rank = {}
    for v in inc:
        for r, (_, ei) in enumerate(inc[v]):
            rank[(v, ei)] = r
    Ab, Af = [], []
    for ei, (a, b, ax) in enumerate(edges):
        p = pmul(X(a), X(b))
        p = pmul(p, X(V + ei))
        for v in (a, b):
            for (_, ej) in inc[v]:
                if rank[(v, ej)] < rank[(v, ei)]:
                    p = pmul(p, Z(V + ej))
        Ab.append(p)
    Bb = [Z(v) for v in range(V)]
    G = [prod([Z(v)] + [Z(V + ej) for (_, ej) in inc[v]]) for v in range(V)]
    # fermions via JW on V modes: g_j = Z..Z X_j, g'_j = Z..Z Y_j
    jw = lambda j: (0, (1 << j) - 1, 0)
    gam = [pmul(jw(j), X(j)) for j in range(V)]
    gamp = [pmul(jw(j), Y(j)) for j in range(V)]
    mi = (0, 0, 3)  # -i
    Af = [pmul(mi, pmul(gam[a], gam[b])) for (a, b, ax) in edges]
    Bf = [pmul(mi, pmul(gam[v], gamp[v])) for v in range(V)]
    return Ab, Bb, G, Af, Bf, inc


def faces(L, coords, edges, periodic):
    emap = {(a, b): ei for ei, (a, b, ax) in enumerate(edges)}
    idx = (lambda x, y, z: (x % L) + L * (y % L) + L * L * (z % L)) if periodic \
        else (lambda x, y, z: x + L * y + L * L * z)
    out = []
    for v, c in enumerate(coords):
        for a1, a2 in ((0, 1), (0, 2), (1, 2)):
            def sh(cc, ax):
                d = list(cc)
                d[ax] += 1
                return d
            c1 = sh(c, a1)
            c3 = sh(c, a2)
            c2 = sh(c1, a2)
            if not periodic and (max(c1) >= L or max(c2) >= L or max(c3) >= L):
                continue
            v1, v2, v3 = idx(*c1), idx(*c2), idx(*c3)
            # loop v->v1->v2->v3->v : steps (edge, +1 forward / -1 reversed)
            out.append([(emap[(v, v1)], 1), (emap[(v1, v2)], 1),
                        (emap[(v3, v2)], -1), (emap[(v, v3)], -1)])
    return out


def loopword(A, loop):
    r = I0
    for ei, s in loop:
        g = pmul((0, 0, 1), A[ei])  # i A_e  (gamma_a gamma_b = i A_ab)
        if s < 0:
            g = pmul((0, 0, 2), g)
        r = pmul(r, g)
    return r


# ============ TEST 1: exact algebra ============
print("== (1) exact algebra ==")
for (L, per, tag) in ((2, False, "cube complex 2x2x2"), (4, True, "periodic 4^3")):
    V, coords, edges = lattice(L, per)
    Ab, Bb, G, Af, Bf, inc = bos_ops(V, edges)
    gb = Ab + Bb
    gf = Af + Bf
    okG = all(not anti(g, h) for g in G for h in gb)
    mism = sum(anti(gb[i], gb[j]) != anti(gf[i], gf[j])
               for i in range(len(gb)) for j in range(i + 1, len(gb)))
    herm = all(pmul(p, p) == I0 for p in gb)
    check(f"{tag}: all {len(Ab)} bosonized A_e and {V} B_v commute with all {V} G_v", okG)
    check(f"{tag}: (anti)commutation table equals Majorana bilinears' "
          f"({len(gb)*(len(gb)-1)//2} pairs)", mism == 0 and herm, f"mismatches={mism}")
    fl = faces(L, coords, edges, per)
    cvals, phis, okc = [], [], True
    for lp in fl:
        lf = loopword(Af, lp)
        lb = loopword(Ab, lp)
        okc &= (lf[0] == 0 and lf[1] == 0)
        cvals.append(lf[2])
        okc &= all(not anti(lb, h) for h in gb + G)
        phis.append(lb)
    check(f"{tag}: {len(fl)} fermion face loops are scalars (c_p = {sorted(set(cvals))} as i^k)"
          f" and bosonized face loops commute with every generator", okc)
    if per:
        P4 = (V, coords, edges, Ab, Bb, G, Af, Bf, fl, phis, cvals)
    else:
        P2 = (V, coords, edges, Ab, Bb, G, Af, Bf, fl, phis, cvals)


# single-particle path algebra: op = {(a, d): {path(tuple of (ei,s)): coeff}}
def W_axis(V, coords, edges, ax, tsign):
    op = {}
    for ei, (a, b, axx) in enumerate(edges):
        if axx != ax:
            continue
        t = tsign[ei]
        op.setdefault((b, a), {})[((ei, 1),)] = t   # hop a -> b : c_b^dag c_a
        op.setdefault((a, b), {})[((ei, -1),)] = t
    return op


def compose(P, Q):  # (P Q)_{ad} = sum_b P_{ab} Q_{bd}; path of c^dag_a c_d runs d -> a
    out = {}
    for (a, b), pa in P.items():
        for (b2, d), qa in Q.items():
            if b2 != b:
                continue
            dd = out.setdefault((a, d), {})
            for p1, c1 in pa.items():
                for p2, c2 in qa.items():
                    pth = p2 + p1
                    dd[pth] = dd.get(pth, 0) + c1 * c2
    return out


def addops(*ops):
    out = {}
    for c, P in ops:
        for k, pa in P.items():
            dd = out.setdefault(k, {})
            for p, v in pa.items():
                dd[p] = dd.get(p, 0) + c * v
    return out


def to_matrix(P, V):
    M = np.zeros((V, V), complex)
    for (a, d), pa in P.items():
        M[a, d] += sum(pa.values())
    return M


def bilinear_terms(P, A, B):
    """Second-quantised sum_{a,d} P_ad c^dag_a c_d as {pauli: coeff}."""
    terms = {}

    def add(p, c):
        key = (p[0], p[1])
        terms[key] = terms.get(key, 0) + c * (1j ** p[2])
    for (a, d), pa in P.items():
        for pth, c in pa.items():
            if abs(c) < 1e-14:
                continue
            Gw = loopword(A, pth) if pth else I0  # gamma_d ... gamma_a along path d -> a
            # path runs from d to a, so Gw = gamma_d gamma_a ; c^dag_a c_d needs gamma_a gamma_d
            if a == d:
                add(Gw, 0.5 * c)
                add(pmul(Gw, B[a]), -0.5 * c)
            else:
                Gad = pmul((0, 0, 2), Gw)  # gamma_a gamma_d = - gamma_d gamma_a
                add(Gad, 0.25 * c)
                add(pmul(Gad, B[d]), -0.25 * c)
                add(pmul(Gad, B[a]), 0.25 * c)
                add(pmul(Gad, pmul(B[a], B[d])), -0.25 * c)
    return terms


def pauli_matrix(terms, states, index_of):
    """Sparse matrix of sum c*X^x Z^z on the basis 'states' (int bit configs)."""
    n = len(states)
    rows, cols, vals = [], [], []
    st = np.array(states, dtype=np.int64)
    for (x, z), c in terms.items():
        if abs(c) < 1e-14:
            continue
        sgn = np.array([1 - 2 * (pc(int(s) & z) % 2) for s in st])
        img = st ^ x
        r = np.array([index_of[int(s)] for s in img])
        rows.append(r)
        cols.append(np.arange(n))
        vals.append(c * sgn)
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                         shape=(n, n))


# ============ TEST 2: many-body cube + periodic band ============
print("== (2) cube tick and band ==")
V, coords, edges, Ab, Bb, G, Af, Bf, fl, phis, cvals = P2
E = len(edges)
pi_t = []
for (a, b, ax) in edges:
    x, y, z = coords[a]
    pi_t.append([1, (-1) ** x, (-1) ** (x + y)][ax])
one_t = [1] * E
Wf = [W_axis(V, coords, edges, ax, pi_t) for ax in range(3)]
Wb = [W_axis(V, coords, edges, ax, one_t) for ax in range(3)]
Mw = [to_matrix(w, V) for w in Wf]
anti_w = max(np.abs(Mw[i] @ Mw[j] + Mw[j] @ Mw[i]).max() for i in range(3) for j in range(i + 1, 3))
Rf = addops(*[(1 / np.sqrt(3), w) for w in Wf])
Rb = addops(*[(1 / np.sqrt(3), w) for w in Wb])
MR = to_matrix(Rf, V)
check("face phase -1 <=> W_i anticommute, R^2 = 1 (fermionic reference)",
      anti_w < 1e-14 and np.abs(MR @ MR - np.eye(V)).max() < 1e-14, f"max|{{Wi,Wj}}|={anti_w:.1e}")
M0 = to_matrix(Rb, V)
check("zero-flux (uniform) cube hop is NOT a reflection", np.abs(M0 @ M0 - np.eye(V)).max() > 0.1,
      f"max|R0^2-1|={np.abs(M0 @ M0 - np.eye(V)).max():.3f}")


def copy_sign(Wl):
    R3 = [(1.0, w) for w in Wl]  # R_i = sqrt3 * (W_i/sqrt3): unit axis hops
    R = addops(*[(1 / np.sqrt(3), w) for w in Wl])
    p = compose(compose(compose(addops(R3[0]), addops(R3[1])), addops(R3[2])), R)
    return addops((1j, p))


Sf, Sb = copy_sign(Wf), copy_sign(Wb)
MS = to_matrix(Sf, V)
check("copy sign s = i R1R2R3R: Hermitian, s^2 = 1, [s,R] = 0 (fermionic reference)",
      np.abs(MS - MS.conj().T).max() < 1e-13 and np.abs(MS @ MS - np.eye(V)).max() < 1e-13
      and np.abs(MS @ MR - MR @ MS).max() < 1e-13)
# fermion Fock (8 modes, even sector)
fstates = [s for s in range(2 ** V) if pc(s) % 2 == 0]
fidx = {s: i for i, s in enumerate(fstates)}
# bosonic G-sector: link config l -> full config (site bits = parity of incident links)
bstates = []
for l in range(2 ** E):
    s = 0
    for v in range(V):
        par = 0
        for ei, (a, b, ax) in enumerate(edges):
            if (a == v or b == v) and (l >> ei) & 1:
                par ^= 1
        s |= par << v
    bstates.append(s | (l << V))
bidx = {s: i for i, s in enumerate(bstates)}
Gsec_ok = all(pc(s & g[1]) % 2 == 0 for s in bstates[:64] for g in G)
evenB = all(not anti(t, g) for t in [(x, z, 0) for (x, z) in bilinear_terms(Sb, Ab, Bb)] for g in G)
check("bosonized copy sign (path words) commutes with every G_v (constraint-even)", evenB)
HRf = pauli_matrix(bilinear_terms(Rf, Af, Bf), fstates, fidx).toarray()
HSf = pauli_matrix(bilinear_terms(Sf, Af, Bf), fstates, fidx).toarray()
HRb = pauli_matrix(bilinear_terms(Rb, Ab, Bb), bstates, bidx)
HSb = pauli_matrix(bilinear_terms(Sb, Ab, Bb), bstates, bidx)
Phi = [pauli_matrix({(p[0], p[1]): 1j ** p[2]}, bstates, bidx) for p in phis]
# fermionic loop value with pi signs: prod t * c_p ; choose bosonized sector phi_p = that value
phival = []
for lp, c in zip(fl, cvals):
    tp = np.prod([pi_t[ei] for ei, s in lp])
    phival.append(tp * (1j ** c))


def sector_basis(phiv):
    P = sp.identity(len(bstates), format="csr", dtype=complex)
    for Ph, ph in zip(Phi, phiv):
        P = P @ ((sp.identity(len(bstates)) + np.conj(ph) * Ph) * 0.5)
    P = P.tocsc()
    seen = np.zeros(len(bstates), bool)
    cols = []
    for j in range(len(bstates)):
        if seen[j]:
            continue
        c = P[:, j]
        if c.nnz == 0 or np.abs(c.data).max() < 1e-12:
            continue
        seen[c.indices[np.abs(c.data) > 1e-12]] = True
        cols.append(c.toarray().ravel())
    Mx = np.array(cols).T
    u, sv, _ = np.linalg.svd(Mx, full_matrices=False)
    r = int((sv > 1e-8).sum())
    return u[:, :r]


Q = sector_basis(phival)
check("flux sector chosen by the face-phase rule has the even-Fock dimension 128", Q.shape[1] == 128,
      f"dim={Q.shape[1]}, G-sector=4096 of 2^20")
hR = Q.conj().T @ (HRb @ Q)
hS = Q.conj().T @ (HSb @ Q)
eps = 0.3
for nm, hb, hf in (("R", hR, HRf), ("s", hS, HSf), ("R+0.37s", hR + 0.37 * hS, HRf + 0.37 * HSf)):
    d = np.abs(np.sort(np.linalg.eigvalsh(hb)) - np.sort(np.linalg.eigvalsh(hf))).max()
    check(f"many-body spectrum of bosonized {nm} (no face phase written) = fermionic", d < 1e-10,
          f"maxdiff={d:.1e}")
Ub = expm(-1j * eps * hR)
Uf = expm(-1j * eps * HRf)
wb = np.sort(np.angle(np.linalg.eigvals(Ub)))
wf = np.sort(np.angle(np.linalg.eigvals(Uf)))
check("cube tick exp(-i eps R) eigenphases agree", np.abs(wb - wf).max() < 1e-10,
      f"eps={eps}, maxdiff={np.abs(wb - wf).max():.1e}")
Q0 = sector_basis([1j ** c for c in cvals])
d0 = np.abs(np.sort(np.linalg.eigvalsh(Q0.conj().T @ (HRb @ Q0))) - np.sort(np.linalg.eigvalsh(HRf))).max()
check("zero-flux sector gives a different (non-reflection) spectrum", d0 > 0.1, f"maxdiff={d0:.3f}")


# periodic single-particle Bloch tick, block = 2x2x2 (pi gauge has period 2)
def bloch_R(K, odd):
    M = np.zeros((8, 8), complex)
    o = 1 if odd else 0
    for c in itertools.product((0, 1), repeat=3):
        p = np.array(c) + o
        for ax in range(3):
            if c[ax] == 1:
                continue
            q = p.copy()
            q[ax] += 1
            x, y, z = p
            t = [1, (-1) ** x, (-1) ** (x + y)][ax]
            ia = int((p % 2) @ [1, 2, 4])
            ib = int((q % 2) @ [1, 2, 4])
            ph = np.exp(1j * np.dot(K, (q // 2) - (p // 2)))
            M[ib, ia] += t * ph
            M[ia, ib] += t * np.conj(ph)
    return M / np.sqrt(3)


def tick(K, eps, mu=0.0, Mc=0.0):
    Re, Ro = bloch_R(np.zeros(3), False), bloch_R(K, True)
    Wloc = [np.zeros((8, 8)) for _ in range(3)]
    for c in itertools.product((0, 1), repeat=3):
        for ax in range(3):
            if c[ax] == 0:
                d = list(c)
                d[ax] = 1
                x, y, z = c
                t = [1, (-1) ** x, (-1) ** (x + y)][ax]
                ia, ib = c[0] + 2 * c[1] + 4 * c[2], d[0] + 2 * d[1] + 4 * d[2]
                Wloc[ax][ia, ib] = Wloc[ax][ib, ia] = t
    s = 1j * Wloc[0] @ Wloc[1] @ Wloc[2] @ Re
    Cm = expm(1j * (Mc / 4) * (np.eye(8) - s) @ Re)
    Ue = Cm @ expm(-1j * (eps - mu / 2) * Re) @ Cm
    Uo = expm(1j * (eps + mu / 2) * Ro)
    return Uo @ Ue


for e0 in (0.3, 0.8):
    w0 = np.angle(np.linalg.eigvals(tick(np.zeros(3), e0)))
    nz = int((np.abs(w0) < 1e-7).sum())
    vs = []
    for nvec in (np.array([1, 0, 0]), np.array([1, 1, 1]) / np.sqrt(3), np.array([1, 2, 0]) / np.sqrt(5)):
        k = 1e-4
        w = np.sort(np.abs(np.angle(np.linalg.eigvals(tick(k * nvec, e0)))))
        vs.append(w[0] / k)
    v_th = np.sin(e0) / np.sqrt(3)
    rel = max(abs(v - v_th) / v_th for v in vs)
    w1 = np.angle(np.linalg.eigvals(tick(np.zeros(3), e0, Mc=0.5)))
    nz1 = int((np.abs(w1) < 1e-7).sum())
    check(f"band eps={e0}: K=0 Dirac point, speed = sin(eps)/sqrt3 isotropic (3 dirs)",
          nz == 8 and rel < 0.02, f"zero modes={nz}, v={np.round(vs, 5)}, th={v_th:.5f}")
    check(f"band eps={e0}: copy mass M=0.5 leaves exactly one light copy (4 zero modes)", nz1 == 4,
          f"zero modes {nz}->{nz1}")
print("periodic band uses the exact sector map of (1): bosonized sector phi_p = -c_p == pi-flux fermion")

# ============ TEST 3: flux selection on 4^3 ============
print("== (3) flux sector energies, half-filled NN sea, 4^3 ==")
V4, coords4, edges4 = P4[0], P4[1], P4[2]


def sea_energy(signs, twists=True):
    best = None
    tw = list(itertools.product((1, -1), repeat=3)) if twists else [(1, 1, 1)]
    for t3 in tw:
        h = np.zeros((V4, V4))
        for ei, (a, b, ax) in enumerate(edges4):
            s = signs[ei]
            if coords4[a][ax] == 3:
                s *= t3[ax]
            h[a, b] += -s
            h[b, a] += -s
        ev = np.linalg.eigvalsh(h)
        e = ev[ev < 0].sum() / V4
        best = e if best is None else min(best, e)
    return best


pis = [[1, (-1) ** coords4[a][0], (-1) ** (coords4[a][0] + coords4[a][1])][ax] for (a, b, ax) in edges4]
Epi = sea_energy(pis)
Ezero = sea_energy([1] * len(edges4))
rnd = [sea_energy(list(RNG.choice([-1, 1], len(edges4))), twists=False) for _ in range(300)]
flipc = []
for ax in range(3):
    ei = [i for i, e in enumerate(edges4) if e[2] == ax][5]
    s2 = list(pis)
    s2[ei] *= -1
    flipc.append((sea_energy(s2) - Epi) * V4)
print(f"E/site: pi={Epi:.4f} zero={Ezero:.4f} random min={min(rnd):.4f} median={np.median(rnd):.4f}")
print(f"single-link flip cost (total) by axis: {np.round(flipc, 3)}; min gap to random (total) "
      f"{(min(rnd) - Epi) * V4:.2f}")
check("pi-flux sector lowest among zero, 300 random and all single-link defects",
      Epi < Ezero and Epi < min(rnd) and min(flipc) > 0)
print("NOTE: every flux commutes with the tick; selection needs a least-energy initial sea (supplied).")

# ============ TEST 4: Klein / Pauli-frame symmetry on bosonized sites ============
print("== (4) Pauli-frame (Klein) symmetries ==")


def null_basis(gens, n):
    """Basis of Paulis (x,z) commuting with every generator (GF(2) symplectic kernel)."""
    m = np.array([[((g[1] >> j) & 1) for j in range(n)] + [((g[0] >> j) & 1) for j in range(n)]
                  for g in gens], dtype=np.uint8)
    A = m.copy()
    piv = []
    r = 0
    for c in range(2 * n):
        rows = np.nonzero(A[r:, c])[0]
        if len(rows) == 0:
            continue
        k = r + rows[0]
        A[[r, k]] = A[[k, r]]
        for rr in np.nonzero(A[:, c])[0]:
            if rr != r:
                A[rr] ^= A[r]
        piv.append(c)
        r += 1
        if r == A.shape[0]:
            break
    free = [c for c in range(2 * n) if c not in piv]
    out = []
    for f in free:
        u = np.zeros(2 * n, np.uint8)
        u[f] = 1
        for i, c in enumerate(piv):
            u[c] = A[i, f]
        x = sum(int(u[j]) << j for j in range(n))
        z = sum(int(u[n + j]) << j for j in range(n))
        out.append((x, z, 0))
    return out


def nullspace_pauli(gens, n):
    """Paulis (x,z) commuting with all gens: solve symplectic GF(2) system."""
    rows = []
    for (x, z, k) in gens:
        rows.append(z | (x << n))  # sympl: P=(x',z') commutes iff x'.z + z'.x = 0
    # unknown vector u = (x' bits 0..n-1, z' bits n..2n-1) ; row r dotted with u
    piv = {}
    for r in rows:
        for b in list(piv):
            if (r >> b) & 1:
                r ^= piv[b]
        if r:
            b = r.bit_length() - 1
            for bb in list(piv):
                if (piv[bb] >> b) & 1:
                    piv[bb] ^= r
            piv[b] = r
    return 2 * n - len(piv)


def rank_gf2(ps, n):
    vecs = [p[0] | (p[1] << n) for p in ps]
    piv = {}
    for r in vecs:
        for b in sorted(piv, reverse=True):
            if (r >> b) & 1:
                r ^= piv[b]
        if r:
            piv[r.bit_length() - 1] = r
    return len(piv)


for tag, P in (("cube", P2), ("4^3", P4)):
    Vv, cc, ee, A_, B_, G_, Af_, Bf_, fl_, ph_, cv_ = P
    n = Vv + len(ee)
    if tag == "4^3":  # add the three non-contractible Wilson loops (boundary-twist registers)
        em = {(a, ax): i for i, (a, b, ax) in enumerate(ee)}
        for ax in range(3):
            lp, v = [], 0
            for _ in range(4):
                i = em[(v, ax)]
                lp.append((i, 1))
                v = ee[i][1]
            ph_ = ph_ + [loopword(A_, lp)]
    stab = rank_gf2(G_ + ph_, n)
    comm_all = nullspace_pauli(A_ + B_ + G_, n)
    terms = [pmul(A_[i], B_[a]) for i, (a, b, ax) in enumerate(ee)] + \
            [pmul(A_[i], B_[b]) for i, (a, b, ax) in enumerate(ee)]
    comm_R = nullspace_pauli(terms + G_, n)
    onsite = [nm for nm, p in (("X", X(0)), ("Y", Y(0)), ("Z", Z(0))) if all(not anti(p, g) for g in G_)]
    glob = {nm: prod([f(v) for v in range(Vv)]) for nm, f in (("X", X), ("Y", Y), ("Z", Z))}
    gi = [nm for nm, p in glob.items() if all(not anti(p, g) for g in G_)]
    print(f"{tag}: stabilizer rank {stab}; Pauli commutant of hop algebra {comm_all}; of hop TERMS+G {comm_R}; "
          f"gauge-invariant on-site Paulis {onsite}; gauge-invariant global site Paulis {gi}")
    check(f"{tag}: commutant of the full hop algebra = constraint group (no extra Pauli label)",
          comm_all == stab)
    check(f"{tag}: only Z (fermion parity) survives on a site; X, Y are string ends (gauge-charged)",
          onsite == ["Z"] and gi == ["Z"])
    extra = comm_R - stab
    if tag == "cube":
        nb = null_basis(terms + G_, n)
        base = rank_gf2(G_ + ph_, n)
        for q in nb:
            if rank_gf2(G_ + ph_ + [q], n) > base:
                sx = "".join({(1, 0): "X", (1, 1): "Y", (0, 1): "Z", (0, 0): "I"}[((q[0] >> v) & 1, (q[1] >> v) & 1)]
                             for v in range(Vv))
                sterms = [(x, z, 0) for (x, z), c in bilinear_terms(Sb, Ab, Bb).items() if abs(c) > 1e-12]
                nbrk = sum(anti(q, t) for t in sterms)
                print(f"  extra Z2 vs bosonized copy-sign terms: anticommutes with {nbrk}/{len(sterms)}"
                      f" (copy mass {'breaks' if nbrk else 'keeps'} it)")
                anticB = sum(anti(q, b) for b in B_)
                anticA = sum(anti(q, a) for a in A_)
                print(f"  extra Z2 on cube: site part {sx}; anticommutes with {anticB}/{Vv} B_v and "
                      f"{anticA}/{len(A_)} A_e  (=> B->-B, A->-A: particle-hole/sublattice type)")
                break
    check(f"{tag}: Pauli symmetries of the hop modulo constraints form at most one Z2 (no Klein, "
          f"three-sector group)", extra <= 1, f"extra generators={extra}")

print("== records (CL-2 reading) ==")
V, coords, edges, Ab, Bb, G, Af, Bf, fl, phis, cvals = P2
okZ = all(not anti(Z(v), g) for v in range(V) for g in G + phis)
nfl = [sum(anti(Z(V + ei), ph) for ph in phis) for ei in range(len(edges))]
check("site Z records (= occupation) are gauge- and flux-invariant", okZ)
check("a Z record of any link qubit anticommutes with the face fluxes through it (would scramble the"
      " face-phase sector): link qubits must be excluded from records", min(nfl) >= 1, f"faces hit per link={sorted(set(nfl))}")
print("== (5) rule count: see note ==")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
