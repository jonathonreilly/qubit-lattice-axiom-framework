# Runner for docs/MDTN_TRUNCATED_GAUGE_SUPPORTING_LEMMAS_LEAN_READY_NOTE_2026-11-01.md
# Requirements: Python 3, numpy, scipy. No file I/O; output to stdout.
# Run from the repo root:
#   python3 scripts/mdtn_supporting_lemmas_check_2026_11_01.py > logs/runner-cache/mdtn_supporting_lemmas_check_2026_11_01.txt
"""Finite checks of the Gauss / combinatorial supporting lemmas for truncated Kogut-Susskind / MDTN gauge models:
SU(2) with link irreps {1, 2} (j_max = 1/2, dim H_l = 5) and SU(3) with link irreps {1, 3, 3bar} (dim H_l = 19).
Conventions (identical to scripts/mdtn_ed_part3_ks_gauge_invariant_2026_10_31.py): a link l = (s -> t) carries
coefficients psi_ij of the irrep block; the generator at the START end acts on index i, at the END end on index j.
No dynamics, no perturbation theory, no spectral-gap estimate: only the unperturbed Gauss / counting statements.
Every check prints its numbers; PASS/FAIL is decided by the stated tolerance."""
import itertools, functools, math, sys, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla

TOL = 1e-9
RESULTS = []
def report(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))
    sys.stdout.flush()

# ---------------------------------------------------------------- groups / leg generators
def eps_tensor(n):
    e = np.zeros((n,)*n)
    for p in itertools.permutations(range(n)):
        e[p] = np.linalg.det(np.eye(n)[list(p)])
    return e

S = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
T2 = [x/2 for x in S]
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2])/np.sqrt(3)
T3 = [l/2 for l in lam]
GEN = {'SU2': T2, 'SU3': T3}
NFUND = {'SU2': 2, 'SU3': 3}
REPS = {'SU2': [1], 'SU3': [1, 2]}     # nontrivial link irreps: SU2: 1 = doublet; SU3: 1 = 3, 2 = 3bar

def leg_gen(g, end, rep):
    """anti-Hermitian generator matrices on one leg (end 0 = start of link, acts on index i; end 1 = end, index j)"""
    out = []
    for T in GEN[g]:
        if rep == 1: out.append((-1j*T).T if end == 0 else 1j*T)
        else:        out.append(1j*T if end == 0 else -1j*T.conj())
    return out

def kron_list(ms):
    m = ms[0]
    for o in ms[1:]: m = np.kron(m, o)
    return m

def site_generators(g, legtypes):
    d = NFUND[g]; n = len(legtypes); out = []
    for a in range(len(GEN[g])):
        M = np.zeros((d**n, d**n), complex)
        for k, (end, rep) in enumerate(legtypes):
            ops = [np.eye(d)]*n; ops[k] = leg_gen(g, end, rep)[a]; M += kron_list(ops)
        out.append(M)
    return out

@functools.lru_cache(maxsize=None)
def inv_dim_lie(g, legtypes):
    """dim of common kernel of the site Gauss generators on the tensor product of legs (definition D2)"""
    if len(legtypes) == 0: return 1
    C = sum(M.conj().T @ M for M in site_generators(g, legtypes))
    return int(np.sum(np.linalg.eigvalsh(C) < 1e-9))

# ---------------------------------------------------------------- combinatorial counts
def catalan(m): return math.comb(2*m, m)//(m+1)

@functools.lru_cache(maxsize=None)
def walks_su2(k):
    """number of Weyl-chamber walks 0 -> 0 with k steps of the doublet weights (+-1 in units of 2j)"""
    cur = {0: 1}
    for _ in range(k):
        nxt = {}
        for p, c in cur.items():
            for q in (p+1, p-1):
                if q >= 0: nxt[q] = nxt.get(q, 0) + c
        cur = nxt
    return cur.get(0, 0)

@functools.lru_cache(maxsize=None)
def walks_su3(a, b):
    """Weyl-chamber walks (Dynkin labels (p,q)) from (0,0) to (0,0): a steps by weights of 3, then b by weights of 3bar.
    Minuscule Pieri rule: V_(p,q) (x) 3 = sum over (p+1,q),(p-1,q+1),(p,q-1) that are dominant; 3bar: conjugate."""
    s3 = [(1, 0), (-1, 1), (0, -1)]; s3b = [(0, 1), (1, -1), (-1, 0)]
    cur = {(0, 0): 1}
    for st in [s3]*a + [s3b]*b:
        nxt = {}
        for (p, q), c in cur.items():
            for (dp, dq) in st:
                if p+dp >= 0 and q+dq >= 0: nxt[(p+dp, q+dq)] = nxt.get((p+dp, q+dq), 0) + c
        cur = nxt
    return cur.get((0, 0), 0)

def haar_dim_su2(k, M=64):
    """dim Inv(2^{(x)k}) = int_SU(2) chi^k by the Weyl integration formula on an M-point grid (exact for M > k+2)"""
    th = 2*np.pi*np.arange(M)/M; z = np.exp(1j*th)
    chi = z + 1/z; w = np.abs(z - 1/z)**2/2
    return float(np.real(np.mean(chi**k*w)))

def haar_dim_su3(a, b, M=24):
    th = 2*np.pi*np.arange(M)/M; z1, z2 = np.meshgrid(np.exp(1j*th), np.exp(1j*th)); z3 = 1/(z1*z2)
    chi = z1 + z2 + z3; vd = np.abs((z1-z2)*(z1-z3)*(z2-z3))**2/6
    return float(np.real(np.mean(chi**a*np.conj(chi)**b*vd)))

# ---------------------------------------------------------------- binary octahedral group 2O in SU(2)
def binary_octahedral():
    qs = set()
    for i in range(4):
        for s in (1, -1):
            v = [0]*4; v[i] = s; qs.add(tuple(v))
    for signs in itertools.product((1, -1), repeat=4): qs.add(tuple(x/2 for x in signs))
    r = 1/np.sqrt(2)
    for i, j in itertools.combinations(range(4), 2):
        for s1, s2 in itertools.product((1, -1), repeat=2):
            v = [0]*4; v[i] = s1*r; v[j] = s2*r; qs.add(tuple(v))
    mats = [np.array([[a+1j*b, c+1j*d], [-c+1j*d, a-1j*b]]) for (a, b, c, d) in qs]
    return mats

# ---------------------------------------------------------------- one-link operators (same tensors as part 3)
def link_data(g):
    d = NFUND[g]; r = 1/np.sqrt(d); trans = {}
    if g == 'SU2':
        e = eps_tensor(2); cr = np.zeros((2,)*4); an = np.zeros((2,)*4)
        for a, b, i, j in itertools.product(range(2), repeat=4):
            cr[a, b, i, j] = r*(a == i)*(b == j); an[a, b, i, j] = r*e[a, i]*e[b, j]
        trans = {(0, 1): cr, (1, 0): an}
    else:
        e = eps_tensor(3); cr = np.zeros((3,)*4); an = np.zeros((3,)*4); fa = np.zeros((3,)*6)
        for a, b, i, j in itertools.product(range(3), repeat=4):
            cr[a, b, i, j] = r*(a == i)*(b == j); an[a, b, i, j] = r*(a == i)*(b == j)
        for a, b, i, j, k, l in itertools.product(range(3), repeat=6):
            fa[a, b, i, j, k, l] = e[a, i, k]*e[b, j, l]/2
        trans = {(0, 1): cr, (2, 0): an, (1, 2): fa}
    nrep = len(REPS[g]); D = 1 + nrep*d*d
    def idx(rep, i, j): return 1 + d*d*(rep-1) + d*i + j
    U = {}
    for x, y in itertools.product(range(d), repeat=2):
        A = np.zeros((D, D), complex)
        for (r0, r1), t in trans.items():
            if t.ndim == 4:
                for i, j in itertools.product(range(d), repeat=2):
                    if r0 == 0: A[idx(r1, i, j), 0] += t[x, y, i, j]
                    else:       A[0, idx(r0, i, j)] += t[x, y, i, j]
            else:
                for i, j, k, l in itertools.product(range(d), repeat=4):
                    A[idx(r1, k, l), idx(r0, i, j)] += t[x, y, i, j, k, l]
        U[(x, y)] = A
    def lgen(end, a):
        M = np.zeros((D, D), complex)
        for rep in REPS[g]:
            gg = leg_gen(g, end, rep)[a]
            blk = np.kron(gg, np.eye(d)) if end == 0 else np.kron(np.eye(d), gg)
            o = idx(rep, 0, 0); M[o:o+d*d, o:o+d*d] = blk
        return M
    n1 = np.diag([0.0] + [1.0]*(D-1))
    return D, U, lgen, n1

# ---------------------------------------------------------------- graphs
class Graph:
    def __init__(self, shape, periodic=False):
        size = [s + (0 if periodic else 1) for s in shape]
        self.V = list(itertools.product(*[range(s) for s in size])); vid = {c: i for i, c in enumerate(self.V)}
        self.links = []; lid = {}
        for c in self.V:
            for mu in range(len(shape)):
                t = list(c); t[mu] += 1
                if periodic: t[mu] %= size[mu]
                elif t[mu] >= size[mu]: continue
                lid[(c, mu)] = len(self.links); self.links.append((vid[c], vid[tuple(t)]))
        self.plaqs = []
        for c in self.V:
            for mu, nu in itertools.combinations(range(len(shape)), 2):
                def sh(x, m):
                    t = list(x); t[m] += 1
                    if periodic: t[m] %= size[m]
                    return tuple(t)
                need = [(c, mu), (sh(c, mu), nu), (sh(c, nu), mu), (c, nu)]
                if all(k in lid for k in need):
                    self.plaqs.append([(lid[need[0]], True), (lid[need[1]], True), (lid[need[2]], False), (lid[need[3]], False)])
        self.star = [[] for _ in self.V]
        for l, (u, v) in enumerate(self.links):
            self.star[u].append((l, 0)); self.star[v].append((l, 1))
        self.adj = [set() for _ in self.V]
        for (u, v) in self.links: self.adj[u].add(v); self.adj[v].add(u)

    def simple(self):
        es = [frozenset(e) for e in self.links]
        return all(len(e) == 2 for e in es) and len(set(es)) == len(es)

    def girth(self):
        best = math.inf
        for s in range(len(self.V)):
            dist = {s: 0}; par = {s: -1}; q = [s]
            for u in q:
                for v in self.adj[u]:
                    if v not in dist: dist[v] = dist[u]+1; par[v] = u; q.append(v)
                    elif par[u] != v: best = min(best, dist[u]+dist[v]+1)
        return best

    def count_4cycles(self):
        cnt = 0
        for a in range(len(self.V)):
            for b in self.adj[a]:
                for c in self.adj[b]:
                    if c == a: continue
                    for dd in self.adj[c]:
                        if dd in (a, b): continue
                        if a in self.adj[dd]: cnt += 1
        return cnt // 8

def cycle_basis_mod_p(G, p):
    """basis of {c in Z_p^E : boundary c = 0}, boundary(l) = [t] - [s]"""
    E = len(G.links); nV = len(G.V)
    B = np.zeros((nV, E), dtype=np.int64)
    for l, (u, v) in enumerate(G.links): B[u, l] -= 1; B[v, l] += 1
    B %= p; A = B.copy(); piv = []; r = 0
    for col in range(E):
        pr = next((i for i in range(r, nV) if A[i, col] % p), None)
        if pr is None: continue
        A[[r, pr]] = A[[pr, r]]; inv = pow(int(A[r, col]), -1, p); A[r] = (A[r]*inv) % p
        for i in range(nV):
            if i != r and A[i, col]: A[i] = (A[i] - A[i, col]*A[r]) % p
        piv.append(col); r += 1
    free = [c for c in range(E) if c not in piv]; basis = []
    for f in free:
        v = np.zeros(E, dtype=np.int64); v[f] = 1
        for i, pc in enumerate(piv): v[pc] = (-A[i, f]) % p
        basis.append(v)
    return basis, r

def legtypes_of(G, conf, s):
    return tuple((end, conf[l]) for (l, end) in sorted(G.star[s]) if conf[l] != 0)

def comb_weight(g, G, conf, s):
    lt = legtypes_of(G, conf, s)
    if g == 'SU2':
        k = len(lt); return catalan(k//2) if k % 2 == 0 else 0
    a = sum(1 for (end, rep) in lt if (end == 0) == (rep == 1)); b = len(lt) - a
    return walks_su3(a, b)

def is_cycle(g, G, conf):
    p = 2 if g == 'SU2' else 3
    for s in range(len(G.V)):
        tot = 0
        for (l, end) in G.star[s]:
            c = conf[l] if g == 'SU3' else conf[l]  # SU3: rep 1 -> 1, rep 2 -> 2 = -1 mod 3
            tot += (c if end == 1 else -c)
        if tot % p: return False
    return True

def sector_dims(g, G, brute):
    """returns dict N -> dim(H_phys cap E_N), computed (a) by summing per-site Lie-kernel dims over configurations
    (brute force over all configurations if brute, otherwise over Z_p cycles only) and (b) combinatorially."""
    nl = len(G.links); reps = [0] + REPS[g]; p = 2 if g == 'SU2' else 3
    num = {}; comb = {}; support_ok = True; weight_ok = True
    if brute:
        it = itertools.product(reps, repeat=nl)
    else:
        basis, _ = cycle_basis_mod_p(G, p)
        def gen():
            for coef in itertools.product(range(p), repeat=len(basis)):
                c = np.zeros(nl, dtype=np.int64)
                for k, b in zip(coef, basis): c = (c + k*b) % p
                yield tuple(int(x) for x in c)
        it = gen()
    for conf in it:
        dn = 1
        for s in range(len(G.V)):
            dn *= inv_dim_lie(g, legtypes_of(G, conf, s))
            if dn == 0: break
        cyc = is_cycle(g, G, conf)
        if (dn > 0) != cyc: support_ok = False
        dc = 1
        if cyc:
            for s in range(len(G.V)): dc *= comb_weight(g, G, conf, s)
        else: dc = 0
        if dc != dn: weight_ok = False
        N = sum(1 for x in conf if x)
        if dn: num[N] = num.get(N, 0) + dn
        if dc: comb[N] = comb.get(N, 0) + dc
    return dict(sorted(num.items())), dict(sorted(comb.items())), support_ok, weight_ok

# =========================================================================================== main
if __name__ == '__main__':
    t0 = time.time()
    print("=== A. Site invariant spaces (Lemma S1-S3: parity/triality, Catalan, Weyl-chamber walks)")
    print("   SU(2): k | Lie-kernel dim (all-out legs, alternating legs) | Haar (Weyl integration) | Catalan / walks")
    okA = True
    for k in range(0, 9):
        d1 = inv_dim_lie('SU2', tuple((0, 1) for _ in range(k)))
        d2 = inv_dim_lie('SU2', tuple((i % 2, 1) for i in range(k)))
        h = haar_dim_su2(k); c = catalan(k//2) if k % 2 == 0 else 0; w = walks_su2(k)
        okA &= (d1 == d2 == round(h) == c == w) and abs(h - round(h)) < 1e-9
        print(f"     k={k}: {d1:3d} {d2:3d} | {h:8.4f} | {c:3d} / {w:3d}")
    report("SU(2) dim Inv(2^k) = Catalan(k/2) (k even), 0 (k odd), k = 0..8; Lie kernel = Haar = walks", okA)
    print("   SU(3): (a,b) | Lie-kernel dim (a out-3 legs, b out-3bar legs) | Lie-kernel, mixed ends | Haar | walks | a=b mod 3")
    okB = True; okTri = True
    for n in range(0, 7):
        for a in range(n+1):
            b = n - a
            lt1 = tuple([(0, 1)]*a + [(0, 2)]*b)
            lt2 = tuple([(1, 2)]*a + [(0, 2)]*b)       # an incoming 3bar link presents the same leg irrep as an outgoing 3
            d1 = inv_dim_lie('SU3', lt1); d2 = inv_dim_lie('SU3', lt2)
            h = haar_dim_su3(a, b); w = walks_su3(a, b); tri = (a - b) % 3 == 0
            okB &= (d1 == d2 == round(h) == w) and abs(h - round(h)) < 1e-9
            okTri &= ((d1 > 0) == tri)
            print(f"     ({a},{b}): {d1:3d} | {d2:3d} | {h:8.4f} | {w:3d} | {tri}")
    report("SU(3) dim Inv(3^a (x) 3bar^b), a+b <= 6: Lie kernel = Haar = Weyl-chamber walk count", okB)
    report("SU(3) Inv(3^a (x) 3bar^b) != 0  <=>  a = b mod 3  (a+b <= 6)", okTri)
    # Cartan-eigenvalue obstruction (the elementary proof of S1)
    H3 = np.diag(T2[2]).real
    ok = all(np.min(np.abs(sum(np.kron(np.kron(np.eye(2**i), np.diag(H3)), np.eye(2**(k-1-i))) for i in range(k)).diagonal())) >= 0.5 - 1e-12
             for k in (1, 3, 5, 7))
    report("SU(2) odd k: the Cartan generator sum_i T^3_i has no zero eigenvalue (all |eig| >= 1/2)", ok)
    Y = np.diag([1/3, 1/3, -2/3])
    def ydiag(a, b):
        ds = [np.diag(Y)]*a + [-np.diag(Y)]*b; tot = np.zeros(1)
        for dvec in ds: tot = np.add.outer(tot, dvec).ravel()
        return tot
    ok = all((np.min(np.abs(ydiag(a, b))) >= 1/3 - 1e-12) == ((a - b) % 3 != 0) for n in range(1, 7) for a in range(n+1) for b in [n-a])
    report("SU(3): hypercharge Y = diag(1/3,1/3,-2/3) summed over legs has a zero eigenvalue iff a = b mod 3 (a+b <= 6), else |eig| >= 1/3", ok)

    print("=== B. Finite-group average (definition D3, SU(2) only; Lemma G7): binary octahedral group 2O, |2O| = 48")
    G48 = binary_octahedral()
    closed = all(any(np.allclose(x@y, z) for z in G48) for x in G48 for y in G48)
    report("2O: 48 distinct SU(2) matrices, closed under multiplication", len(G48) == 48 and closed and
           all(np.allclose(m.conj().T@m, np.eye(2)) and abs(np.linalg.det(m)-1) < 1e-12 for m in G48))
    for k in range(0, 9):
        lt = tuple((i % 2, 1) for i in range(k))
        if k == 0: continue
        mats = []
        Pf = np.zeros((2**k, 2**k), complex)
        for m in G48:
            Pf += kron_list([m.conj() if e == 0 else m for (e, _) in lt])
        Pf /= 48
        if k <= 7:
            C = sum(M.conj().T@M for M in site_generators('SU2', lt)); w, v = np.linalg.eigh(C); K = v[:, w < 1e-9]
            Pl = K@K.conj().T
            report(f"k={k}: 2O average = orthogonal projector onto Lie kernel", np.abs(Pf - Pl).max() < 1e-9,
                   f"max|P_2O - P_Lie| = {np.abs(Pf-Pl).max():.1e}, rank {int(round(np.trace(Pf).real))}")
        else:
            rk = int(round(np.trace(Pf).real))
            report(f"k={k}: 2O average has rank {rk} > Catalan(4) = 14 (D3 fails beyond 7 legs, as predicted)", rk > 14)

    print("=== C. One-link covariance of the truncated link operators (Lemma G6 hypothesis (Cov))")
    for g in ['SU2', 'SU3']:
        D, U, lgen, n1 = link_data(g); d = NFUND[g]; r1 = r2 = r3 = 0.0
        for a in range(len(GEN[g])):
            As, Ae = lgen(0, a), lgen(1, a); X = -1j*GEN[g][a]
            r3 = max(r3, np.abs(As@n1 - n1@As).max(), np.abs(Ae@n1 - n1@Ae).max(), np.abs(As@Ae - Ae@As).max())
            for x, y in itertools.product(range(d), repeat=2):
                lhs = As@U[(x, y)] - U[(x, y)]@As; rhs = sum(X[x, z]*U[(z, y)] for z in range(d))
                r1 = max(r1, np.abs(lhs - rhs).max())
                lhs = Ae@U[(x, y)] - U[(x, y)]@Ae; rhs = -sum(U[(x, z)]*X[z, y] for z in range(d))
                r2 = max(r2, np.abs(lhs - rhs).max())
        report(f"{g}: [A^a_start, U^xy] = sum_z X^a_xz U^zy  (X^a = -i T^a)", r1 < TOL, f"residual {r1:.1e}")
        report(f"{g}: [A^a_end,   U^xy] = -sum_z U^xz X^a_zy", r2 < TOL, f"residual {r2:.1e}")
        report(f"{g}: [A^a_end-e, n_l] = 0 and [A^a_start, A^b_end] = 0 on one link", r3 < TOL, f"residual {r3:.1e}")

    print("=== D. Lemmas G2-G6 on a single plaquette (definition D2: P_s = projector onto ker of site Gauss Casimir)")
    for g in ['SU2', 'SU3']:
        D, U, lgen, n1 = link_data(g); d = NFUND[g]; Gp = Graph((1, 1)); nl = 4; dimH = D**nl
        I = sp.identity(D, format='csr')
        def emb(op, l):
            return kron_sp([sp.csr_matrix(op) if k == l else I for k in range(nl)])
        def kron_sp(ms):
            m = ms[0]
            for o in ms[1:]: m = sp.kron(m, o, format='csr')
            return m
        Gs = [[sum(emb(lgen(end, a), l) for (l, end) in Gp.star[s]) for a in range(len(GEN[g]))] for s in range(4)]
        N = sum(emb(n1, l) for l in range(nl))
        P = Gp.plaqs[0]; TrU = None
        for idx4 in itertools.product(range(d), repeat=4):
            pairs = [(idx4[0], idx4[1]), (idx4[1], idx4[2]), (idx4[2], idx4[3]), (idx4[3], idx4[0])]
            term = None
            for (l, fwd), (x, y) in zip(P, pairs):
                A = U[(x, y)] if fwd else U[(y, x)].conj().T
                e = emb(A, l); term = e if term is None else term @ e
            TrU = term if TrU is None else TrU + term
        def nrm(M): return abs(M).max() if M.nnz else 0.0
        rc = max(nrm(Gs[s][a]@Gs[t][b] - Gs[t][b]@Gs[s][a]) for s in range(4) for t in range(4) if s != t
                 for a in range(len(GEN[g])) for b in range(len(GEN[g])))
        rn = max(nrm(Gs[s][a]@N - N@Gs[s][a]) for s in range(4) for a in range(len(GEN[g])))
        ru = max(nrm(Gs[s][a]@TrU - TrU@Gs[s][a]) for s in range(4) for a in range(len(GEN[g])))
        report(f"{g} plaquette (dim {dimH}): [G_s^a, G_t^b] = 0 for s != t", rc < TOL, f"{rc:.1e}")
        report(f"{g} plaquette: [G_s^a, N] = 0", rn < TOL, f"{rn:.1e}")
        report(f"{g} plaquette: [G_s^a, Tr U_P] = 0 (and hence for Tr U_P^dag)", ru < TOL, f"{ru:.1e}")
        Cs = [sum(M.getH()@M for M in Gs[s]) for s in range(4)]
        if g == 'SU2':
            Ps = []
            for s in range(4):
                w, v = np.linalg.eigh(Cs[s].toarray()); K = v[:, w < 1e-9]; Ps.append(K@K.conj().T)
            Nd = N.toarray(); Td = TrU.toarray()
            e1 = max(np.abs(Pm@Pm - Pm).max() for Pm in Ps); e2 = max(np.abs(Pm - Pm.conj().T).max() for Pm in Ps)
            e3 = max(np.abs(Ps[s]@Ps[t] - Ps[t]@Ps[s]).max() for s in range(4) for t in range(4))
            e4 = max(np.abs(Pm@Nd - Nd@Pm).max() for Pm in Ps); e5 = max(np.abs(Pm@Td - Td@Pm).max() for Pm in Ps)
            Pphys = Ps[0]@Ps[1]@Ps[2]@Ps[3]
            Ctot = sum(Cs).toarray(); w, v = np.linalg.eigh(Ctot); K = v[:, w < 1e-9]
            e6 = np.abs(Pphys - K@K.conj().T).max()
            report("SU2 plaquette: P_s^2 = P_s, P_s^dag = P_s", max(e1, e2) < TOL, f"{e1:.1e}, {e2:.1e}")
            report("SU2 plaquette: [P_s, P_t] = 0, [P_s, N] = 0, [P_s, Tr U_P] = 0", max(e3, e4, e5) < TOL, f"{e3:.1e}, {e4:.1e}, {e5:.1e}")
            report("SU2 plaquette: prod_s P_s = projector onto common kernel of all Gauss generators", e6 < TOL,
                   f"{e6:.1e}; rank {int(round(np.trace(Pphys).real))}")
            # locality: P_s = (local projector on star(s)) (x) identity on the other links
            s = 0; legs = sorted(l for (l, _) in Gp.star[s]); Pt = Ps[s].reshape([D]*8)
            other = [l for l in range(4) if l not in legs]
            # check P acts as identity on 'other' factors: contract with traceless test ops
            Ploc_ok = True
            for l in other:
                X = np.zeros((D, D)); X[0, 1] = 1
                Xe = emb(X, l).toarray(); Ploc_ok &= np.abs(Ps[s]@Xe - Xe@Ps[s]).max() < TOL
            report("SU2 plaquette: P_s commutes with every operator on links outside star(s) (locality)", Ploc_ok)
            # 2O average of the full-space gauge transformation at s equals P_s
            G48 = binary_octahedral(); Pf = np.zeros((dimH, dimH), complex)
            for m in G48:
                ops = []
                for l in range(nl):
                    Wl = np.eye(D, dtype=complex)
                    for (ll, end) in Gp.star[s]:
                        if ll == l:
                            Wl[1:, 1:] = np.kron(m.conj(), np.eye(2)) if end == 0 else np.kron(np.eye(2), m)
                    ops.append(Wl)
                Pf += kron_list(ops)
            Pf /= 48
            report("SU2 plaquette: (1/48) sum_{g in 2O} W_s(g) = P_s (D3 = D2 on the full 625-dim space)",
                   np.abs(Pf - Ps[s]).max() < TOL, f"{np.abs(Pf - Ps[s]).max():.1e}")
            ev = np.linalg.eigvalsh(K.conj().T@Nd@K)
            report("SU2 plaquette: spec(N | H_phys) = {0, 4}", np.allclose(np.sort(ev), [0, 4]), f"{np.round(ev, 9)}")
        else:
            Ctot = sum(Cs).tocsc()
            w, v = sla.eigsh(Ctot, k=8, sigma=-0.1, which='LM', tol=1e-12)
            o = np.argsort(w); w = w[o]; v = v[:, o]; kz = int(np.sum(w < 1e-8))
            # shift-invert Lanczos does not guarantee orthonormal vectors inside a degenerate eigenspace:
            # re-orthonormalise (QR) and verify they lie in the kernel before restricting N.
            K, _ = np.linalg.qr(v[:, :kz]); kres = np.abs(Ctot@K).max()
            report("SU3 plaquette: orthonormalised kernel vectors satisfy |C_tot K| < 1e-8", kres < 1e-8, f"{kres:.1e}")
            ev = np.linalg.eigvalsh(K.conj().T@(N@K))
            report(f"SU3 plaquette: dim ker(total Gauss Casimir) = 3 (8 lowest eigenvalues {np.round(w, 6)})", kz == 3)
            report("SU3 plaquette: spec(N | H_phys) = {0, 4, 4}", np.allclose(np.sort(ev), [0, 4, 4]), f"{np.round(ev, 9)}")
            # local projector checks on the star of corner 0 (2 links, dim 361) and adjacent corners (3 links, dim 6859)
            def local_P(s, links):
                Il = sp.identity(D, format='csr'); nl_ = len(links)
                def eml(op, l): 
                    return kron_sp([sp.csr_matrix(op) if k == links.index(l) else Il for k in range(nl_)]) if nl_ > 1 else sp.csr_matrix(op)
                Cl = None
                for a in range(8):
                    Gl = sum(eml(lgen(end, a), l) for (l, end) in Gp.star[s])
                    Cl = Gl.getH()@Gl if Cl is None else Cl + Gl.getH()@Gl
                return Cl
            s, t = 0, 1
            common = sorted(set(l for (l, _) in Gp.star[s]) | set(l for (l, _) in Gp.star[t]))
            Cl_s = local_P(s, common).toarray(); Cl_t = local_P(t, common).toarray()
            def proj(C):
                w, v = np.linalg.eigh(C); K = v[:, w < 1e-9]; return K@K.conj().T, K.shape[1]
            Ps_, rs = proj(Cl_s); Pt_, rt = proj(Cl_t)
            e1 = max(np.abs(Ps_@Ps_ - Ps_).max(), np.abs(Ps_ - Ps_.conj().T).max())
            e3 = np.abs(Ps_@Pt_ - Pt_@Ps_).max()
            report(f"SU3 on star(s) u star(t), s~t ({len(common)} links, dim {D**len(common)}): P_s idempotent, self-adjoint; [P_s,P_t]=0",
                   max(e1, e3) < 1e-8, f"{e1:.1e}, {e3:.1e}; ranks {rs}, {rt}")

    print("=== E. Lemmas C1, C2, C4, C5: configuration-block decomposition, support (cycle) lemma, exact counts, N-spectrum on H_phys")
    print("   numeric = sum over configurations of prod_s (Lie-kernel dim at s);  comb = Z_p-cycle enumeration with")
    print("   Catalan (SU2) / Weyl-chamber-walk (SU3) site weights.  'support' = nonzero blocks are exactly the Z_p cycles.")
    part3 = {('SU2', (1, 1)): 2, ('SU2', (2, 1)): 4, ('SU2', (2, 2)): 18, ('SU2', (3, 2)): 82, ('SU2', (1, 1, 1)): 32,
             ('SU3', (1, 1)): 3, ('SU3', (2, 1)): 9}
    cases = [('SU2', (1, 1), False, True), ('SU2', (2, 1), False, True), ('SU2', (2, 2), False, True),
             ('SU2', (3, 2), False, True), ('SU2', (1, 1, 1), False, True), ('SU2', (2, 1, 1), False, True),
             ('SU2', (3, 3), True, True),
             ('SU3', (1, 1), False, True), ('SU3', (2, 1), False, True), ('SU3', (2, 2), False, True),
             ('SU3', (1, 1, 1), False, True), ('SU3', (2, 1, 1), False, False), ('SU3', (3, 3), True, False)]
    for g, shape, per, brute in cases:
        G = Graph(shape, periodic=per); t1 = time.time()
        num, comb, sup, wt = sector_dims(g, G, brute)
        gir = G.girth(); c4 = G.count_4cycles(); mult4 = 1 if g == 'SU2' else 2
        tag = f"{g} {'periodic' if per else 'open'} {'x'.join(map(str, shape))} (|V|={len(G.V)}, |E|={len(G.links)}, plaquettes={len(G.plaqs)}, girth={gir}, 4-cycles={c4})"
        print(f"   {tag}  [{'brute force over all ' + str((len(REPS[g])+1)**len(G.links)) + ' configs' if brute else 'Z_p cycles only'}, {time.time()-t1:.1f}s]")
        print(f"     dim(H_phys cap E_N), numeric: {num}")
        print(f"     dim(H_phys cap E_N), comb.  : {comb}   total {sum(comb.values())}")
        report("numeric = combinatorial (every block)", wt and num == comb)
        if brute: report("nonzero configuration blocks are exactly the Z_p 1-cycles", sup)
        pos = [k for k in num if k > 0]
        report("H_phys cap E_0 = C|0>  and  min{N > 0 on H_phys} = girth", num.get(0) == 1 and (not pos or min(pos) == gir),
               f"min N>0 = {min(pos) if pos else None}")
        if gir == 4: report(f"dim(H_phys cap E_4) = {mult4} x #4-cycles", num.get(4, 0) == mult4*c4, f"{num.get(4,0)} vs {mult4}x{c4}")
        if (g, shape) in part3 and not per:
            report(f"total dim H_phys = part-3 runner's gauge-invariant basis size {part3[(g, shape)]}", sum(num.values()) == part3[(g, shape)])
        if g == 'SU2' and not per:
            report("SU2 on a bipartite graph: H_phys lives only in even N", all(k % 2 == 0 for k in num))

    print("=== F. Girth / simplicity of the Z^3 graphs (Lemma C3)")
    for shape, per in [((3, 3, 3), True), ((4, 4, 4), True), ((5, 5, 5), True), ((6, 6, 6), True), ((2, 3, 4), False), ((3, 3, 3), False)]:
        G = Graph(shape, periodic=per); gir = G.girth(); c4 = G.count_4cycles(); L = shape[0]
        exp4 = len(G.plaqs) + (3*L*L if per and L == 4 else 0)
        print(f"   {'periodic' if per else 'open'} {'x'.join(map(str, shape))}: |V|={len(G.V)} |E|={len(G.links)} simple={G.simple()} "
              f"girth={gir} plaquettes={len(G.plaqs)} 4-cycles={c4}")
        if per and L == 3: report("periodic L=3: girth 3 (so L >= 4 is needed)", gir == 3)
        else:
            report("simple, girth 4", G.simple() and gir == 4)
            report("4-cycles = plaquettes" + (" + 3L^2 straight winding loops (L = 4)" if per and L == 4 else ""), c4 == exp4, f"{c4} vs {exp4}")
    print(f"=== Summary: {sum(ok for _, ok in RESULTS)}/{len(RESULTS)} checks PASS  (total {time.time()-t0:.0f}s)")
