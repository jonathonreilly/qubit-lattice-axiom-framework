# Runner (part 3) for docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md
# Requirements: Python 3, numpy, scipy (generated with numpy 2.5.4, scipy 1.18.1). No file I/O; output to stdout (~1 min).
# Run from the repo root:  python3 scripts/mdtn_ed_part3_ks_gauge_invariant_2026_10_31.py > logs/runner-cache/mdtn_ed_part3_ks_gauge_invariant_2026_10_31.txt
"""Part 3: exact diagonalisation of truncated Kogut-Susskind lattice gauge theory in the GAUGE-INVARIANT basis
(irrep label per link + intertwiner per site), for SU(2) (j_max = 1/2) and SU(3) (irreps {1, 3, 3bar}) on small
multi-plaquette lattices.  H_KS = sum_l (g^2/2) C2(l) - (1/(2 g^2)) sum_P (Tr U_P + h.c.), with the truncated
link operators U^{ab} = Pi D_ab Pi.  We report everything in units of the one-link electric energy
e1 = (g^2/2) C2(fund):  H/e1 = N - kappa * sum_P (T_P + T_P^dag)/2,  kappa = 1/(g^2 * e1) = 2/(g^4 C2)
(SU(2): kappa = 8/(3 g^4); SU(3): kappa = 3/(2 g^4)).
Matrix elements (Haar integrals, exact):
  SU(2), psi_ij = sqrt2 D_ij:  <f;ij|U^ab|0> = d_ia d_jb / sqrt2,  <0|U^ab|f;ij> = eps_ai eps_bj / sqrt2.
  SU(3), psi^f_ij = sqrt3 D_ij, psi^a_ij = sqrt3 conj(D_ij):
     <f;ij|U^ab|0> = d_ia d_jb/sqrt3,  <0|U^ab|a;ij> = d_ai d_bj/sqrt3,  <a;kl|U^ab|f;ij> = eps_aik eps_bjl / 2.
Checks: (1) single plaquette vs closed form; (2) SU(2) gauge-invariant code vs the 625-dim full-space ED of part 1;
(3) SU(3) single plaquette cross-checked by full-space ED (19^4) with explicit Gauss-law projection.
"""
import numpy as np, itertools, functools, sys, time
import scipy.sparse as sp, scipy.sparse.linalg as sla

def eps_tensor(n):
    e = np.zeros((n,)*n)
    for p in itertools.permutations(range(n)):
        e[p] = np.linalg.det(np.eye(n)[list(p)])
    return e

class Group:
    def __init__(self, name):
        self.name = name
        if name == 'SU2':
            self.N = 2; self.reps = [1]          # 1 = fundamental
            s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
            self.T = [x/2 for x in s]; self.C2 = 3/4
            e = eps_tensor(2); r = 1/np.sqrt(2)
            # trans[(from,to)][a,b] -> tensor over (in legs..., out legs...)
            self.trans = {}
            cr = np.zeros((2, 2, 2, 2)); an = np.zeros((2, 2, 2, 2))
            for a, b, i, j in itertools.product(range(2), repeat=4):
                cr[a, b, i, j] = r*(a == i)*(b == j)          # 0 -> f, out legs (i,j)
                an[a, b, i, j] = r*e[a, i]*e[b, j]           # f -> 0, in legs (i,j)
            self.trans[(0, 1)] = cr; self.trans[(1, 0)] = an
        else:
            self.N = 3; self.reps = [1, 2]       # 1 = 3, 2 = 3bar
            lam = np.zeros((8, 3, 3), complex)
            lam[0][0, 1] = lam[0][1, 0] = 1
            lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
            lam[2][0, 0] = 1; lam[2][1, 1] = -1
            lam[3][0, 2] = lam[3][2, 0] = 1
            lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
            lam[5][1, 2] = lam[5][2, 1] = 1
            lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
            lam[7] = np.diag([1, 1, -2])/np.sqrt(3)
            self.T = [l/2 for l in lam]; self.C2 = 4/3
            e = eps_tensor(3); r = 1/np.sqrt(3)
            cr = np.zeros((3, 3, 3, 3)); an = np.zeros((3, 3, 3, 3)); fa = np.zeros((3, 3, 3, 3, 3, 3))
            for a, b, i, j in itertools.product(range(3), repeat=4):
                cr[a, b, i, j] = r*(a == i)*(b == j)        # 0 -> 3
                an[a, b, i, j] = r*(a == i)*(b == j)        # 3bar -> 0
            for a, b, i, j, k, l in itertools.product(range(3), repeat=6):
                fa[a, b, i, j, k, l] = e[a, i, k]*e[b, j, l]/2   # 3 (in i,j) -> 3bar (out k,l)
            self.trans = {(0, 1): cr, (2, 0): an, (1, 2): fa}
    def leg_gen(self, end, rep):
        """generator matrices acting on the coefficient vector of one leg (end 0 = start of link, 1 = end)"""
        out = []
        for T in self.T:
            if rep == 1:
                out.append((-1j*T).T if end == 0 else 1j*T)
            else:
                out.append(1j*T if end == 0 else -1j*T.conj())
        return out

@functools.lru_cache(maxsize=None)
def inv_basis(gname, legtypes):
    G = GROUPS[gname]; d = G.N; n = len(legtypes)
    if n == 0:
        return np.ones((1, 1), complex)
    dim = d**n
    C = np.zeros((dim, dim), complex)
    for a in range(len(G.T)):
        M = np.zeros((dim, dim), complex)
        for k, (end, rep) in enumerate(legtypes):
            g = G.leg_gen(end, rep)[a]
            ops = [np.eye(d)]*n; ops[k] = g
            m = ops[0]
            for o in ops[1:]:
                m = np.kron(m, o)
            M += m
        C += M.conj().T@M
    w, v = np.linalg.eigh(C)
    return v[:, w < 1e-9]          # columns: orthonormal invariant vectors over legs in order

GROUPS = {'SU2': Group('SU2'), 'SU3': Group('SU3')}

class Lattice:
    def __init__(self, shape, periodic=False):
        dims = len(shape)
        coords = list(itertools.product(*[range(s+ (0 if periodic else 1)) for s in shape]))
        self.V = coords; vid = {c: i for i, c in enumerate(coords)}
        size = [s + (0 if periodic else 1) for s in shape]
        self.links = []; lid = {}
        for c in coords:
            for mu in range(dims):
                t = list(c); t[mu] += 1
                if periodic: t[mu] %= size[mu]
                elif t[mu] >= size[mu]: continue
                lid[(c, mu)] = len(self.links); self.links.append((vid[c], vid[tuple(t)]))
        self.plaqs = []
        for c in coords:
            for mu, nu in itertools.combinations(range(dims), 2):
                def sh(x, m):
                    t = list(x); t[m] += 1
                    if periodic: t[m] %= size[m]
                    return tuple(t)
                c1 = sh(c, mu); c2 = sh(c, nu)
                need = [(c, mu), (c1, nu), (c2, mu), (c, nu)]
                if all(k in lid for k in need):
                    # path c -> c+mu -> c+mu+nu -> c+nu -> c : links fwd, fwd, rev, rev
                    self.plaqs.append([(lid[need[0]], True), (lid[need[1]], True), (lid[need[2]], False), (lid[need[3]], False)])
        self.star = [[] for _ in self.V]
        for l, (u, v) in enumerate(self.links):
            self.star[u].append((l, 0)); self.star[v].append((l, 1))

def link_ops(G, fwd, rin):
    """list of (rout, tensor[a,b, in legs..., out legs...]) for A^{ab} on a link with incoming irrep rin.
    reverse-traversed links use (U^dag)^{ab} = (U^{ba})^dag."""
    out = []
    for (r0, r1), t in G.trans.items():
        if fwd and r0 == rin:
            out.append((r1, t, 'fwd'))
        if (not fwd) and r1 == rin:          # adjoint of r0->r1 maps r1 -> r0
            out.append((r0, t, 'rev'))
    return out

class Model:
    def __init__(self, gname, lat):
        self.G = GROUPS[gname]; self.g = gname; self.lat = lat
    def vertex_legs(self, conf, v):
        return tuple((l, end) for (l, end) in sorted(self.lat.star[v]) if conf[l] != 0)
    def legtypes(self, conf, v):
        return tuple((end, conf[l]) for (l, end) in self.vertex_legs(conf, v))
    def plaq_action(self, conf, P):
        """returns (newconf, amplitude matrix [alpha'_corners, alpha_corners]) for T_P = Tr prod A, or None"""
        G = self.G; d = G.N; lat = self.lat
        corners = sorted(set(v for (l, _) in P for v in lat.links[l]))
        # unique outgoing config (each link has at most one transition per direction for these truncations)
        new = list(conf)
        for (l, fwd) in P:
            ops = link_ops(G, fwd, conf[l])
            if not ops: return None
            new[l] = ops[0][0]
        new = tuple(new)
        key = (tuple(conf[l] for v in corners for (l, _) in lat.star[v]), tuple(P), tuple(corners))
        if key in self.cache: return new, self.cache[key]
        # ket legs ordering: corner by corner
        in_legs = [lg for v in corners for lg in self.vertex_legs(conf, v)]
        out_legs = [lg for v in corners for lg in self.vertex_legs(new, v)]
        bases_in = [inv_basis(self.g, self.legtypes(conf, v)) for v in corners]
        bases_out = [inv_basis(self.g, self.legtypes(new, v)) for v in corners]
        nin = [b.shape[1] for b in bases_in]; nout = [b.shape[1] for b in bases_out]
        amp = np.zeros((int(np.prod(nout)), int(np.prod(nin))), complex)
        for ai, alpha in enumerate(itertools.product(*[range(n) for n in nin])):
            psi = np.ones(())
            labels = []
            for v, b, a in zip(corners, bases_in, alpha):
                legs = self.vertex_legs(conf, v)
                t = b[:, a].reshape((d,)*len(legs)) if legs else np.array(b[0, a])
                psi = np.multiply.outer(psi, t); labels += list(legs)
            total = None
            for idx in itertools.product(range(d), repeat=4):    # a,b,c,e indices around the loop
                pairs = [(idx[0], idx[1]), (idx[1], idx[2]), (idx[2], idx[3]), (idx[3], idx[0])]
                cur = psi; lab = list(labels)
                for (l, fwd), (x, y) in zip(P, pairs):
                    rout, t, kind = link_ops(G, fwd, conf[l])[0]
                    if kind == 'fwd':
                        tt = t[x, y]
                    else:   # adjoint of t^{yx}: swap in/out legs, conjugate
                        tt = t[y, x]
                        nin_ = (tt.ndim)//2 if conf[l] != 0 and rout != 0 else (tt.ndim if conf[l] == 0 else 0)
                        # tensors: cr/an have 2 legs (either in or out); fa has 4 (2 in, 2 out)
                        if tt.ndim == 4: tt = tt.transpose(2, 3, 0, 1)
                        tt = tt.conj()
                    nin_legs = 2 if conf[l] != 0 else 0
                    nout_legs = 2 if rout != 0 else 0
                    # contract in legs
                    if nin_legs:
                        ax = [lab.index((l, 0)), lab.index((l, 1))]
                        cur = np.tensordot(cur, tt, axes=(ax, [0, 1]))
                        lab = [x_ for k, x_ in enumerate(lab) if k not in ax] + ([(l, 0), (l, 1)] if nout_legs else [])
                    else:
                        cur = np.multiply.outer(cur, tt); lab = lab + [(l, 0), (l, 1)]
                total = cur if total is None else total + cur
            # reorder to out_legs and project onto out invariants
            perm = [lab.index(x) for x in out_legs]
            total = np.transpose(total, perm) if perm else total
            vec = total.reshape(-1)
            # project
            B = bases_out[0]
            for b in bases_out[1:]:
                B = np.kron(B, b)
            amp[:, ai] = B.conj().T@vec
        self.cache[key] = amp
        return new, amp
    def build(self, kappa_list, verbose=True):
        self.cache = {}
        lat = self.lat; t0 = time.time()
        conf0 = tuple([0]*len(lat.links))
        confs = {conf0: 0}; order = [conf0]; k = 0
        trans = []
        while k < len(order):
            c = order[k]; k += 1
            for P in lat.plaqs:
                r = self.plaq_action(c, P)
                if r is None: continue
                new, amp = r
                if new not in confs:
                    confs[new] = len(order); order.append(new)
                trans.append((c, new, P, amp))
        # basis offsets
        mult = {}
        off = {}; tot = 0
        for c in order:
            ms = [inv_basis(self.g, self.legtypes(c, v)).shape[1] for v in range(len(lat.V))]
            mult[c] = ms; off[c] = tot; tot += int(np.prod(ms))
        rows, cols, vals = [], [], []
        for (c, new, P, amp) in trans:
            corners = sorted(set(v for (l, _) in P for v in lat.links[l]))
            others = [v for v in range(len(lat.V)) if v not in corners]
            mi, mo = mult[c], mult[new]
            for full in itertools.product(*[range(m) for m in mi]):
                # index of ket
                ki = off[c] + int(np.ravel_multi_index(full, mi)) if mi else off[c]
                ci = int(np.ravel_multi_index(tuple(full[v] for v in corners), [mi[v] for v in corners]))
                col = amp[:, ci]
                for co, a in enumerate(col):
                    if abs(a) < 1e-13: continue
                    cout = np.unravel_index(co, [mo[v] for v in corners])
                    fo = list(full)
                    for v, x in zip(corners, cout): fo[v] = x
                    ko = off[new] + int(np.ravel_multi_index(tuple(fo), mo))
                    rows.append(ko); cols.append(ki); vals.append(a)
        T = sp.csr_matrix((vals, (rows, cols)), shape=(tot, tot))
        diag = np.zeros(tot)
        for c in order:
            nexc = sum(1 for x in c if x != 0)
            diag[off[c]:off[c]+int(np.prod(mult[c]))] = nexc
        self.T = T; self.N = sp.diags(diag); self.dim = tot; self.nconf = len(order)
        if verbose:
            print(f"   {self.g} lattice: links={len(lat.links)} plaquettes={len(lat.plaqs)} flux configs={len(order)} "
                  f"dim H_phys={tot}  (build {time.time()-t0:.1f}s)")
        return self
    def gap(self, kappa):
        H = self.N - kappa*(self.T + self.T.getH())/2
        if self.dim <= 3000:
            e = np.linalg.eigvalsh(H.toarray())
        else:
            e = np.sort(sla.eigsh(H.tocsc(), k=3, which='SA', tol=1e-11)[0])
        return e[0], e[1]-e[0]

def pt2_lambda(lat):
    P = [set(l for (l, _) in p) for p in lat.plaqs]; n = len(P)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            if len(P[i] & P[j]) == 1: A[i, j] = A[j, i] = 1
    return np.linalg.eigvalsh(np.diag(A.sum(1)) + A)[-1] if n else 0

if __name__ == '__main__':
    np.set_printoptions(precision=6, suppress=True)
    print("=== Check 1: single plaquette (gauge-invariant code)")
    for gname in ['SU2', 'SU3']:
        m = Model(gname, Lattice((1, 1))).build([])
        Hs = (m.T + m.T.getH())/2
        print(f"   {gname}: N-spectrum {sorted(set(m.N.diagonal()))}, max|T - T^dag| = {abs(m.T - m.T.getH()).max():.2e}")
        for kappa in [0.1, 0.5]:
            e = np.linalg.eigvalsh((m.N - kappa*Hs).toarray())
            print(f"     kappa={kappa}: spectrum {np.round(e, 6)}")
    print("   SU2 closed form (2-level, unit amplitude): gap = sqrt(16 + 4 kappa^2): kappa=0.1 ->",
          round(np.sqrt(16+4*0.01), 6), " kappa=0.5 ->", round(np.sqrt(16+4*0.25), 6))
    print("   (part-1 full-space ED, KS units g^2=2: gap 3.16228)")
    m = Model('SU2', Lattice((1, 1))).build([], verbose=False)
    g2 = 2.0; kappa = 2/(g2**2*0.75); e0, gp = m.gap(kappa)
    print(f"   SU2 gauge-invariant code at g^2=2: gap*(3g^2/8) = {gp*3*g2/8:.5f}")
    sys.stdout.flush()

    # ---- Check 3: SU(3) single plaquette in the FULL 19^4 link space, Gauss law by penalty ----
    print("=== Check 3: SU(3) single plaquette, full 19^4 = 130321-dim space vs gauge-invariant code")
    G = GROUPS['SU3']; lat = Lattice((1, 1))
    def link_matrix(x, y):
        A = np.zeros((19, 19), complex)
        def idx(rep, i, j): return 1 + 9*(rep-1) + 3*i + j
        for (r0, r1), t in G.trans.items():
            if t.ndim == 4:
                for i, j in itertools.product(range(3), repeat=2):
                    if r0 == 0: A[idx(r1, i, j), 0] += t[x, y, i, j]
                    else:       A[0, idx(r0, i, j)] += t[x, y, i, j]
            else:
                for i, j, k, l in itertools.product(range(3), repeat=4):
                    A[idx(r1, k, l), idx(r0, i, j)] += t[x, y, i, j, k, l]
        return A
    U = {(x, y): link_matrix(x, y) for x in range(3) for y in range(3)}
    def lgen(end, a):
        M = np.zeros((19, 19), complex)
        for rep in (1, 2):
            g = G.leg_gen(end, rep)[a]
            blk = np.kron(g, np.eye(3)) if end == 0 else np.kron(np.eye(3), g)
            o = 1 + 9*(rep-1); M[o:o+9, o:o+9] = blk
        return sp.csr_matrix(M)
    I19 = sp.identity(19, format='csr')
    def emb(op, l):
        m = None
        for k in range(4):
            o = op if k == l else I19
            m = o if m is None else sp.kron(m, o, format='csr')
        return m
    P = lat.plaqs[0]
    T = None
    for idx4 in itertools.product(range(3), repeat=4):
        pairs = [(idx4[0], idx4[1]), (idx4[1], idx4[2]), (idx4[2], idx4[3]), (idx4[3], idx4[0])]
        term = None
        for (l, fwd), (x, y) in zip(P, pairs):
            A = U[(x, y)] if fwd else U[(y, x)].conj().T
            e = emb(sp.csr_matrix(A), l)
            term = e if term is None else term @ e
        T = term if T is None else T + term
    Cas = None
    for v in range(len(lat.V)):
        for a in range(8):
            Gv = None
            for (l, end) in lat.star[v]:
                e = emb(lgen(end, a), l)
                Gv = e if Gv is None else Gv + e
            c = Gv.getH() @ Gv
            Cas = c if Cas is None else Cas + c
    print("   max |[Gauss Casimir, T]| =", abs(Cas @ T - T @ Cas).max())
    n1 = sp.diags([0.0] + [1.0]*18)
    Nf = sum(emb(n1, l) for l in range(4))
    for kappa in [0.1, 0.5]:
        H = Nf - kappa*(T + T.getH())/2 + 50.0*Cas
        e = np.sort(sla.eigsh(H.tocsc(), k=4, which='SA', tol=1e-12)[0])
        print(f"   kappa={kappa}: lowest 3 levels with Gauss penalty 50*Cas: {np.round(e[:3], 6)}")
    sys.stdout.flush()

    # ---- Check 4: SU(2) 1x2 open strip (7 links, shared link) in FULL 5^7 space vs gauge-invariant code ----
    print("=== Check 4: SU(2) 1x2 strip (shared link): full 5^7 = 78125-dim space vs gauge-invariant code")
    G2 = GROUPS['SU2']; lat = Lattice((2, 1)); nl = len(lat.links)
    def lm2(x, y):
        A = np.zeros((5, 5))
        for i, j in itertools.product(range(2), repeat=2):
            A[1+2*i+j, 0] = G2.trans[(0, 1)][x, y, i, j]; A[0, 1+2*i+j] = G2.trans[(1, 0)][x, y, i, j]
        return A
    U2 = {(x, y): lm2(x, y) for x in range(2) for y in range(2)}
    I5 = sp.identity(5, format='csr')
    def emb2(op, l):
        m = None
        for k in range(nl):
            o = op if k == l else I5
            m = o if m is None else sp.kron(m, o, format='csr')
        return m
    Ttot = None
    for P in lat.plaqs:
        for idx4 in itertools.product(range(2), repeat=4):
            pairs = [(idx4[0], idx4[1]), (idx4[1], idx4[2]), (idx4[2], idx4[3]), (idx4[3], idx4[0])]
            term = None
            for (l, fwd), (x, y) in zip(P, pairs):
                A = U2[(x, y)] if fwd else U2[(y, x)].T
                e = emb2(sp.csr_matrix(A), l); term = e if term is None else term @ e
            Ttot = term if Ttot is None else Ttot + term
    Cas = None
    for v in range(len(lat.V)):
        for a in range(3):
            Gv = None
            for (l, end) in lat.star[v]:
                g = G2.leg_gen(end, 1)[a]; M = np.zeros((5, 5), complex)
                M[1:, 1:] = np.kron(g, np.eye(2)) if end == 0 else np.kron(np.eye(2), g)
                e = emb2(sp.csr_matrix(M), l); Gv = e if Gv is None else Gv + e
            c = Gv.getH() @ Gv; Cas = c if Cas is None else Cas + c
    Nf = sum(emb2(sp.diags([0.0, 1, 1, 1, 1]), l) for l in range(nl))
    mgi = Model('SU2', lat).build([], verbose=False)
    for kappa in [0.3, 1.0]:
        e = np.sort(sla.eigsh((Nf - kappa*Ttot + 50*Cas).tocsc(), k=3, which='SA', tol=1e-12)[0])
        eg = np.linalg.eigvalsh((mgi.N - kappa*(mgi.T + mgi.T.getH())/2).toarray())
        print(f"   kappa={kappa}: full-space+penalty lowest {np.round(e[:2], 6)} | gauge-invariant code {np.round(eg[:2], 6)}")

    # ---- Production runs ----
    def pt2(m):
        """numerical 2nd-order (degenerate, first order included) strong-coupling estimate of the gap, from the
        built matrices: H = N + kappa V, V = -(T+T^dag)/2.  E_vac = -kappa^2 sum |V_m0|^2/N_m;
        one-plaquette block: H_eff = 4 + kappa P V P - kappa^2 P V Q (N-4)^{-1} Q V P (Q = complement of N=4).
        returns (a1, M2) so that gap_PT(kappa) = lowest eig of (4 + kappa*a1 + kappa^2*M2) - E_vac(kappa)."""
        V = (-(m.T + m.T.getH())/2).tocsr(); d = m.N.diagonal()
        i0 = np.where(d == 0)[0]; i4 = np.where(d == 4)[0]; q = np.where(d != 4)[0]
        v0 = V[:, i0].toarray().ravel(); nz = d > 0
        evac2 = -np.sum(np.abs(v0[nz])**2/d[nz])
        V44 = V[i4][:, i4].toarray(); Vq4 = V[q][:, i4].toarray()
        M2 = -(Vq4.conj().T*(1/(d[q]-4))) @ Vq4
        return V44, M2, evac2
    print("\n=== Production: physical-sector gap Delta(kappa) in units of e1 = (g^2/2)C2, H/e1 = N - kappa*sum_P Re-part")
    print("    (Z2-MDTN PT2 formula with unit amplitudes: 4 + kappa^2/2 - (kappa^2/4)*lambda_max(D+A))")
    systems = [('SU2', (1, 1)), ('SU2', (2, 1)), ('SU2', (2, 2)), ('SU2', (3, 2)),
               ('SU2', (1, 1, 1)),
               ('SU3', (1, 1)), ('SU3', (2, 1))]
    kappas = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6]
    for gname, shape in systems:
        t0 = time.time()
        try:
            m = Model(gname, Lattice(shape)).build([])
        except MemoryError:
            print("   memory error", gname, shape); continue
        V44, M2, ev2 = pt2(m); lam = pt2_lambda(m.lat)
        print(f"   {gname} open {'x'.join(map(str, shape))}: lambda_max(D+A)={lam:.4f}")
        print("     kappa |  Delta_ED   |  Delta_PT(num, 2nd order) | Z2 formula | (4-Delta_ED)/kappa^2")
        for k in kappas:
            e0, gp = m.gap(k)
            hb = 4*np.eye(len(V44)) + k*V44 + k*k*M2
            gpt = np.linalg.eigvalsh((hb + hb.conj().T)/2)[0] - k*k*ev2
            z2 = 4 + k*k/2 - k*k*lam/4
            print(f"     {k:5.2f} | {gp:11.6f} | {gpt:11.6f}              | {z2:10.6f} | {(4-gp)/k**2:9.5f}")
        print(f"     ({time.time()-t0:.1f}s)"); sys.stdout.flush()
