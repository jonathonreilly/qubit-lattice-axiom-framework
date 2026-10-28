# f16 (FLOW lane C, session 13): Cartan tower, exact Cartan linearisation, covariant decomposition at U, T-split decay.
# Criteria: checks/f16_criteria.md (written before this script). Conventions: FLOW.md section 103.
import os, sys, time, itertools, resource
import numpy as np
import scipy.sparse as sp

T0 = time.time()
SMOKE = os.environ.get('F16_SMOKE', '0') == '1'
L, R = 3, 1
ORD = list(itertools.permutations(range(4)))
OFF = list(itertools.product([-1, 0, 1], repeat=4))
NCON = len(ORD) * len(OFF)
verdicts = []

def verdict(name, ok, msg):
    verdicts.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")

def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20  # macOS: bytes

# ---------------------------------------------------------------- geometry
def path_steps(base, sigma, y):
    """axial path from base to base+y moving coordinates in the order sigma; steps (site, dir, sign)."""
    cur = list(base); st = []
    for a in sigma:
        if y[a] == 1:
            st.append((tuple(cur), a, +1)); cur[a] += 1
        elif y[a] == -1:
            cur[a] -= 1; st.append((tuple(cur), a, -1))
    return st

def contour_steps(mu, sigma, y):
    st = path_steps((0, 0, 0, 0), sigma, y)
    cur = list(y)
    for j in range(L):
        st.append((tuple(cur), mu, +1)); cur[mu] += 1
    cY = [0, 0, 0, 0]; cY[mu] = L
    back = path_steps(tuple(cY), sigma, y)
    for (z, a, s) in reversed(back):
        st.append((z, a, -s))
    return st

class Geom:
    """fine torus fs -> coarse torus cs = fs/L; per mu a local box of base-site offsets (mu: -1..4, others -1..1)."""
    def __init__(self, fs):
        self.fs = tuple(fs); self.cs = tuple(f // L for f in fs)
        self.Nf = int(np.prod(self.fs)); self.Nc = int(np.prod(self.cs))
        Xc = np.array(list(np.ndindex(*self.cs)))           # (Nc,4) in C order
        self.root = L * Xc + R
        self.boxes = []; self.site_of = []                     # per mu: list of offsets, (nbox, Nc) site indices
        for mu in range(4):
            rng = [range(-1, 5) if a == mu else range(-1, 2) for a in range(4)]
            offs = list(itertools.product(*rng))
            self.boxes.append({o: k for k, o in enumerate(offs)})
            arr = np.empty((len(offs), self.Nc), dtype=np.int64)
            for k, o in enumerate(offs):
                arr[k] = np.ravel_multi_index(tuple(((self.root[:, a] + o[a]) % self.fs[a]) for a in range(4)), self.fs)
            self.site_of.append(arr)
        self.cont = []                                          # per mu: list of (offidx, dirs, signs)
        for mu in range(4):
            lst = []
            for s in ORD:
                for y in OFF:
                    st = contour_steps(mu, s, y)
                    lst.append((np.array([self.boxes[mu][z] for (z, a, sg) in st]), np.array([a for (z, a, sg) in st]),
                                np.array([sg for (z, a, sg) in st])))
            self.cont.append(lst)
        # slice paths c_X -> c_X + y (box -1..1, use mu=0 box which contains it)
        self.paths = []
        for s in ORD:
            for y in OFF:
                st = path_steps((0, 0, 0, 0), s, y)
                self.paths.append((np.array([self.boxes[0][z] for (z, a, sg) in st], dtype=np.int64),
                                   np.array([a for (z, a, sg) in st], dtype=np.int64), np.array([sg for (z, a, sg) in st], dtype=np.int64)))
        self.cmu = []
        for mu in range(4):
            Y = (np.array(list(np.ndindex(*self.cs))) + np.eye(4, dtype=int)[mu]) % np.array(self.cs)
            self.cmu.append(np.ravel_multi_index(tuple(Y[:, a] for a in range(4)), self.cs))
        self.croot_site = np.ravel_multi_index(tuple(self.root[:, a] for a in range(4)), self.fs)

    def link(self, d, site):
        return d * self.Nf + site

# ---------------------------------------------------------------- fine-level operators
def D_op(fs, a, q):
    """root-sector covariant gradient (D w)_{x,mu} = e^{-iq a_{x,mu}} w(x) - w(x+e_mu); a shape (4,)+fs."""
    N = int(np.prod(fs)); X = np.array(list(np.ndindex(*fs)))
    rows, cols, vals = [], [], []
    for mu in range(4):
        Y = (X + np.eye(4, dtype=int)[mu]) % np.array(fs)
        y = np.ravel_multi_index(tuple(Y[:, b] for b in range(4)), fs)
        x = np.arange(N)
        rows += [mu * N + x, mu * N + x]; cols += [x, y]
        vals += [np.exp(-1j * q * a[mu].ravel()), -np.ones(N, complex)]
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(4 * N, N))

def ev_op(fs):
    cs = tuple(f // L for f in fs); Nc = int(np.prod(cs)); Xc = np.array(list(np.ndindex(*cs)))
    rt = np.ravel_multi_index(tuple(L * Xc[:, a] + R for a in range(4)), fs)
    return sp.csr_matrix((np.ones(Nc), (np.arange(Nc), rt)), shape=(Nc, int(np.prod(fs))))

def step_angles(G, mu, con, aflat):
    offidx, dirs, signs = con
    sites = G.site_of[mu][offidx]                     # (ns, Nc)
    return signs[:, None] * aflat[dirs[:, None] * G.Nf + sites], sites, dirs, signs

def xi_coefs(ang, signs, q):
    """coefficient of phi_b for each step: fwd e^{-iq th_>s}, bwd -e^{-iq th_>=s}."""
    suf = np.cumsum(ang[::-1], axis=0)[::-1]          # suf[s] = sum_{t>=s}
    gt = suf - ang                                    # sum_{t>s}
    return np.where(signs[:, None] > 0, np.exp(-1j * q * gt), -np.exp(-1j * q * suf))

def build_chain_su2(G, a, q, want_h=True):
    """exact chain-map linearisation T(U) (SU(2), h = +-q/2) at the Cartan background a; coarse angles; transported slice h_U."""
    aflat = a.reshape(-1)
    acoarse = np.zeros((4,) + G.cs)
    nslot = [len(G.boxes[mu]) * 4 for mu in range(4)]
    rows_all, cols_all, vals_all = [], [], []
    for mu in range(4):
        th = np.empty((NCON, G.Nc))
        for k, con in enumerate(G.cont[mu]):
            ang, _, _, _ = step_angles(G, mu, con, aflat); th[k] = ang.sum(0)
        m1 = np.exp(0.5j * q * th).mean(0)
        acoarse[mu] = (2.0 * np.angle(m1) / q).reshape(G.cs)
        W = np.zeros((G.Nc, nslot[mu]), complex)
        for k, con in enumerate(G.cont[mu]):
            ang, sites, dirs, signs = step_angles(G, mu, con, aflat)
            c = xi_coefs(ang, signs, q) * (np.exp(0.5j * q * th[k]) / m1 / NCON)[None, :]
            slot = con[0] * 4 + dirs
            for s in range(len(dirs)):
                W[:, slot[s]] += c[s]
        # columns
        cols = np.empty((G.Nc, nslot[mu]), dtype=np.int64)
        for o, kk in G.boxes[mu].items():
            for d in range(4):
                cols[:, kk * 4 + d] = d * G.Nf + G.site_of[mu][kk]
        rows_all.append(np.repeat(mu * G.Nc + np.arange(G.Nc), nslot[mu])); cols_all.append(cols.ravel()); vals_all.append(W.ravel())
        del W, th
    T = sp.csr_matrix((np.concatenate(vals_all), (np.concatenate(rows_all), np.concatenate(cols_all))), shape=(4 * G.Nc, 4 * G.Nf))
    T.sort_indices()
    if not want_h:
        return T, acoarse, None
    nsl = len(G.boxes[0]) * 4
    Wh = np.zeros((G.Nc, nsl), complex)
    for (offidx, dirs, signs) in G.paths:
        if len(dirs) == 0:
            continue
        sites = G.site_of[0][offidx]
        ang = signs[:, None] * aflat[dirs[:, None] * G.Nf + sites]
        c = xi_coefs(ang, signs, q) * np.exp(1j * q * ang.sum(0))[None, :] * (-1.0 / NCON)
        slot = offidx * 4 + dirs
        for s in range(len(dirs)):
            Wh[:, slot[s]] += c[s]
    cols = np.empty((G.Nc, nsl), dtype=np.int64)
    for o, kk in G.boxes[0].items():
        for d in range(4):
            cols[:, kk * 4 + d] = d * G.Nf + G.site_of[0][kk]
    h = sp.csr_matrix((Wh.ravel(), (np.repeat(np.arange(G.Nc), nsl), cols.ravel())), shape=(G.Nc, 4 * G.Nf))
    h.sort_indices()
    return T, acoarse, h

# ---------------------------------------------------------------- Part A (nonlinear maps, SU(N))
def unit_rot(phi, t, i, j, N):
    """expm(t(phi e_ij - conj(phi) e_ji)) batched."""
    n = len(phi); E = np.tile(np.eye(N, dtype=complex), (n, 1, 1))
    r = np.abs(phi); ph = np.where(r > 0, phi / np.where(r > 0, r, 1), 1)
    c, s = np.cos(t * r), np.sin(t * r)
    E[:, i, i] = c; E[:, j, j] = c; E[:, i, j] = ph * s; E[:, j, i] = -np.conj(ph) * s
    return E

def ulog(V):
    w, P = np.linalg.eig(V)
    return P @ (np.log(w)[..., None] * np.linalg.inv(P))

def uexp_ah(B):
    w, P = np.linalg.eigh(1j * B)                     # 1j*B hermitian
    return (P * np.exp(-1j * w)[..., None, :]) @ np.conj(np.swapaxes(P, -1, -2))

def w_nat(M, N):
    if N == 2:
        u, s, vh = np.linalg.svd(M); return u @ vh
    u, s, vh = np.linalg.svd(M); V = u @ vh
    V = V / np.linalg.det(V)[:, None, None] ** (1.0 / N)
    for it in range(200):
        A = np.linalg.solve(V, M)
        B = 0.5 * (A - np.conj(np.swapaxes(A, -1, -2)))
        B = B - (np.trace(B, axis1=1, axis2=2) / N)[:, None, None] * np.eye(N)
        res = np.abs(B).max()
        V = V @ uexp_ah(B)
        if res < 1e-15:
            break
    return V

def nonlinear_maps(G, Ulinks, N):
    """returns chain W_nat(Mbar) and S4' map, per coarse link: arrays (4, Nc, N, N); also max eigen-angle of S_c^-1 T."""
    Uh = np.conj(np.swapaxes(Ulinks, -1, -2))
    chain = np.empty((4, G.Nc, N, N), complex); s4 = np.empty_like(chain); amax = 0.0
    for mu in range(4):
        prods = []
        for (offidx, dirs, signs) in G.cont[mu]:
            P = np.tile(np.eye(N, dtype=complex), (G.Nc, 1, 1))
            for s in range(len(dirs)):
                site = G.site_of[mu][offidx[s]]
                P = P @ (Ulinks[dirs[s], site] if signs[s] > 0 else Uh[dirs[s], site])
            prods.append(P)
        prods = np.array(prods)                        # (NCON, Nc, N, N)
        chain[mu] = w_nat(prods.mean(0), N)
        k0 = ORD.index(tuple(range(4))) * len(OFF) + OFF.index((0, 0, 0, 0))
        Sc = prods[k0]; Sci = np.linalg.inv(Sc)
        Z = Sci[None] @ prods
        w = np.linalg.eigvals(Z); amax = max(amax, np.abs(np.angle(w)).max())
        lg = ulog(Z.reshape(-1, N, N)).reshape(Z.shape).mean(0)
        lg = 0.5 * (lg - np.conj(np.swapaxes(lg, -1, -2)))
        s4[mu] = Sc @ uexp_ah(lg)
    return chain, s4, amax

def cartan_links(G, a, h):
    U = np.zeros((4, G.Nf, len(h), len(h)), complex)
    for k, hk in enumerate(h):
        U[:, :, k, k] = np.exp(1j * hk * a.reshape(4, G.Nf))
    return U

def closed_forms(G, a, h, i, j, phi, phiW):
    """(X3) closed forms applied to phi (shape (4*Nf,)): chain (with W_nat phases phiW (4,Nc,N)), S4', naive avg xi."""
    q = h[i] - h[j]; aflat = a.reshape(-1)
    out = {k: np.zeros((4, G.Nc), complex) for k in ('chain', 's4', 'naive')}
    k0 = ORD.index(tuple(range(4))) * len(OFF) + OFF.index((0, 0, 0, 0))
    for mu in range(4):
        th = np.empty((NCON, G.Nc)); xi = np.empty((NCON, G.Nc), complex)
        for k, con in enumerate(G.cont[mu]):
            ang, sites, dirs, signs = step_angles(G, mu, con, aflat)
            th[k] = ang.sum(0)
            xi[k] = (xi_coefs(ang, signs, q) * phi[dirs[:, None] * G.Nf + sites]).sum(0)
        psi_i = h[i] * th - phiW[mu][None, :, i]; psi_j = h[j] * th - phiW[mu][None, :, j]
        Nn = np.exp(1j * psi_i) + np.exp(-1j * psi_j); Nb = np.exp(-1j * psi_i) + np.exp(1j * psi_j)
        out['chain'][mu] = (Nn * xi).mean(0) / Nb.mean(0)
        out['naive'][mu] = xi.mean(0)
        dl = th - th[k0]; db = dl.mean(0); xc = xi[k0]
        def g(z):
            return np.where(np.abs(z) > 1e-14, z / np.where(np.abs(z) > 1e-14, 1 - np.exp(-z), 1), 1.0 + 0j)
        zb = 1j * q * db
        out['s4'][mu] = np.exp(-zb) * xc + (1.0 / g(zb)) * (g(1j * q * dl) * (xi - np.exp(-1j * q * dl) * xc[None])).mean(0)
        out.setdefault('rootphase_s4', np.zeros((4, G.Nc)))[mu] = q * (th[k0] + db)
        out.setdefault('Qroot', np.zeros((4, G.Nc)))[mu] = th.mean(0)
    return out

def partA():
    print("=== Part A: Cartan tower and exact Cartan linearisation (fine 9^4, coarse 3^4) ===")
    G = Geom((9, 9, 9, 9)); p, vt, eps = 2 * np.pi / 9, 0.4, 0.25
    x2 = np.array(list(np.ndindex(*G.fs)))[:, 1].reshape(G.fs)
    def bg(e):
        a = np.zeros((4,) + G.fs); a[0] = e * np.cos(p * x2 + vt); return a
    cfgs = [('SU(2)', np.array([0.5, -0.5]), [(0, 1)])]
    if not SMOKE:
        cfgs.append(('SU(3)', np.array([0.7, -0.2, -0.5]), [(0, 1), (0, 2)]))
    Xc2 = np.array(list(np.ndindex(*G.cs)))[:, 1].reshape(G.cs)
    rng = np.random.default_rng(16)
    for name, h, roots in cfgs:
        N = len(h)
        res = {}
        for e in (eps, -eps, eps / 2):
            a = bg(e); U = cartan_links(G, a, h)
            res[e] = nonlinear_maps(G, U, N) + (a,)
        chain, s4, amax, a = res[eps]
        print(f"{name}: max |eigen-angle of S_c^-1 T| = {amax:.4f} (< pi/3 = 1.0472: {amax < np.pi/3})")
        # A1a
        cf = closed_forms(G, a, h, roots[0][0], roots[0][1], np.zeros(4 * G.Nf, complex), np.zeros((4, G.Nc, N)))
        Qr = cf['Qroot']
        lin = np.zeros((4, G.Nc, N, N), complex)
        for k in range(N):
            lin[:, :, k, k] = np.exp(1j * h[k] * Qr)
        e1A = np.abs(s4 - lin).max()
        e1 = eps * np.sin(3 * p / 2) / np.sin(p / 2); th1 = vt + p
        pred = np.zeros((4,) + G.cs); pred[0] = e1 * np.cos(3 * p * Xc2 + th1)
        e1B = np.abs(Qr - pred.reshape(4, -1)).max()
        verdict(f"A1a {name}", e1A <= 1e-12 and e1B <= 1e-12, f"S4' = exp(Q_root a H_1): {e1A:.2e}; tower formula: {e1B:.2e}")
        # A1b
        offd = max(np.abs(chain[..., k, l]).max() for k in range(N) for l in range(N) if k != l)
        phis = {e: np.angle(np.diagonal(res[e][0], axis1=-2, axis2=-1)) for e in res}
        odd = np.abs(phis[eps] + phis[-eps]).max() / np.abs(phis[eps]).max()
        def dev(e):
            Qe = closed_forms(G, res[e][3], h, roots[0][0], roots[0][1], np.zeros(4 * G.Nf, complex), np.zeros((4, G.Nc, N)))['Qroot']
            return np.abs(phis[e] - h[None, None, :] * Qe[..., None]).max()
        d1, d2 = dev(eps), dev(eps / 2); rat = d1 / d2
        verdict(f"A1b {name}", offd <= 1e-13 and odd <= 1e-12 and 7 <= rat <= 9,
                f"off-diag {offd:.1e}; oddness {odd:.1e}; dev(e)={d1:.3e}, dev(e/2)={d2:.3e}, ratio {rat:.3f}")
        phiW = phis[eps]
        for (i, j) in roots:
            q = h[i] - h[j]
            phi = (rng.standard_normal(4 * G.Nf) + 1j * rng.standard_normal(4 * G.Nf))
            cf = closed_forms(G, a, h, i, j, phi, phiW)
            tt = 1e-5; Ul = cartan_links(G, a, h)
            Z = {}
            for sg in (+1, -1):
                Up = Ul @ unit_rot(phi, sg * tt, i, j, N).reshape(4, G.Nf, N, N)
                cp, sp4, _ = nonlinear_maps(G, Up, N)
                Z[sg] = (ulog(np.linalg.solve(chain, cp).reshape(-1, N, N))[:, i, j].reshape(4, G.Nc),
                         ulog(np.linalg.solve(s4, sp4).reshape(-1, N, N))[:, i, j].reshape(4, G.Nc))
            fd_c = (Z[1][0] - Z[-1][0]) / (2 * tt); fd_s = (Z[1][1] - Z[-1][1]) / (2 * tt)
            ec = np.linalg.norm(cf['chain'] - fd_c) / np.linalg.norm(fd_c)
            es = np.linalg.norm(cf['s4'] - fd_s) / np.linalg.norm(fd_s)
            en = np.linalg.norm(cf['naive'] - fd_c) / np.linalg.norm(fd_c)
            verdict(f"A2 {name} root ({i+1},{j+1}) q={q:.2f}", ec <= 1e-7 and es <= 1e-7, f"chain {ec:.2e}; S4' {es:.2e}")
            verdict(f"A2c {name} root ({i+1},{j+1}) control", en >= 1e-3, f"naive avg xi against the chain FD: {en:.2e}")
            # A3a covariance
            om = rng.standard_normal(G.Nf) + 1j * rng.standard_normal(G.Nf)
            Dphi = D_op(G.fs, a, q) @ om
            cfD = closed_forms(G, a, h, i, j, Dphi, phiW)
            omc = om[G.croot_site]
            rp_c = phiW[..., i] - phiW[..., j]; rp_s = cfD['rootphase_s4']
            pc = np.array([np.exp(-1j * rp_c[mu]) * omc - omc[G.cmu[mu]] for mu in range(4)])
            ps = np.array([np.exp(-1j * rp_s[mu]) * omc - omc[G.cmu[mu]] for mu in range(4)])
            e3c = np.linalg.norm(cfD['chain'] - pc) / np.linalg.norm(pc); e3s = np.linalg.norm(cfD['s4'] - ps) / np.linalg.norm(ps)
            verdict(f"A3a {name} root ({i+1},{j+1})", e3c <= 1e-12 and e3s <= 1e-12, f"chain {e3c:.2e}; S4' {e3s:.2e}")
            # A3b
            r = []
            for e in (eps, eps / 2):
                cfe = closed_forms(G, res[e][3], h, i, j, phi, phis[e])
                r.append(np.linalg.norm(cfe['chain'] - cfe['s4']) / np.linalg.norm(cfe['chain']))
            verdict(f"A3b {name} root ({i+1},{j+1})", 3 <= r[0] / r[1] <= 5, f"r(e)={r[0]:.3e}, r(e/2)={r[1]:.3e}, ratio {r[0]/r[1]:.3f}")
    print(f"Part A time {time.time()-T0:.1f} s, peak RSS {rss_mb():.0f} MB")

# ---------------------------------------------------------------- Part B
def pfrob(P, X, blk=40000):
    X = X.tocsc(); tot = 0.0
    for c0 in range(0, X.shape[1], blk):
        Y = P @ X[:, c0:c0 + blk].toarray(); tot += np.sum(np.abs(Y) ** 2)
    return np.sqrt(tot)

def partB(dl=0.02, tag=''):
    top = tuple(int(v) for v in os.environ.get('F16_TOP', '3,3,1,1' if SMOKE else '3,3,2,2').split(','))
    print(f"=== Part B{tag and ' ('+tag+')'}: SU(2) chain map, levels b -> n-1 -> n, level-n torus {top}, delta = {dl} ===")
    q = 1.0; Pb = 2 * np.pi / (top[1] * 9); vt = 0.3
    fs_b = tuple(9 * t for t in top); fs_m = tuple(3 * t for t in top)
    Gb, Gm = Geom(fs_b), Geom(fs_m)
    Nn = int(np.prod(top)); nl = 4 * Nn
    x2 = np.array(list(np.ndindex(*fs_b)))[:, 1].reshape(fs_b)
    evm = ev_op(fs_m)
    # sector projector on level-n links: zero sector = average over X1, X3, X4 at fixed X2
    Xn = np.array(list(np.ndindex(*top)))
    Pi0 = np.zeros((nl, nl))
    for mu in range(4):
        for x in range(Nn):
            for yv in range(Nn):
                if Xn[x, 1] == Xn[yv, 1]:
                    Pi0[mu * Nn + x, mu * Nn + yv] = 1.0 / (Nn // top[1])
    Pinz = np.eye(nl) - Pi0
    w, V = np.linalg.eigh(Pinz); Bnz = V[:, w > 0.5]               # orthonormal basis of the nonzero sectors
    def snorm(M):
        return np.linalg.norm(Bnz.conj().T @ M @ Bnz, 2)
    eps_list = [0.0, dl, -dl, 2 * dl, -2 * dl]
    # Richardson weights: first derivative and half second derivative
    c1 = {dl: 8 / (12 * dl), -dl: -8 / (12 * dl), 2 * dl: -1 / (12 * dl), -2 * dl: 1 / (12 * dl), 0.0: 0.0}
    c2 = {dl: 16 / (24 * dl**2), -dl: 16 / (24 * dl**2), 2 * dl: -1 / (24 * dl**2), -2 * dl: -1 / (24 * dl**2), 0.0: -30 / (24 * dl**2)}
    store = {}
    accQ = {1: {}, 2: {}}; accA = {}
    ref_struct = {}
    rng = np.random.default_rng(1613)
    for e in eps_list:
        tb = time.time()
        a_b = np.zeros((4,) + fs_b); a_b[0] = e * np.cos(Pb * x2 + vt)
        Tb, a_m, hb = build_chain_su2(Gb, a_b, q)
        Tm, a_n, hm = build_chain_su2(Gm, a_m, q)
        Dm = D_op(fs_m, a_m, q); Dn = D_op(top, a_n, q).toarray()
        Qb = (Tb + Dm @ hb).tocsr(); Qb.sort_indices()
        Qm = Tm + sp.csr_matrix(Dn) @ hm; Qm = sp.csr_matrix(Qm); Qm.sort_indices()
        A2 = (Tm @ Tb).tocsr(); A2.sort_indices()
        Q2 = (Qm @ Qb).tocsr(); Q2.sort_indices()
        s1 = (Tm @ Tm.conj().T).toarray(); s2 = (A2 @ A2.conj().T).toarray()
        Delta = Dn.conj().T @ Dn
        P = np.eye(nl) - Dn @ np.linalg.pinv(Delta, rcond=1e-10, hermitian=True) @ Dn.conj().T
        store[e] = dict(P=P, s1=s1, s2=s2, Dn=Dn, Qm=Qm.toarray(), Tm=Tm.toarray(), a_n=a_n.copy(), a_m=a_m.copy())
        for r, cw in ((1, c1), (2, c2)):
            if cw[e] != 0.0:
                accQ[r]['Q2'] = (cw[e] * Q2) if 'Q2' not in accQ[r] else (accQ[r]['Q2'] + cw[e] * Q2).tocsr()
        if c1[e] != 0.0:
            accA['A2'] = (c1[e] * A2) if 'A2' not in accA else (accA['A2'] + c1[e] * A2).tocsr()
        if abs(e - 2 * dl) < 1e-15:
            # B1 identities
            h2 = (evm @ hb + hm @ Qb).tocsr()
            X = (A2 - (Q2 - sp.csr_matrix(Dn) @ h2)).tocsr()
            e_dec = np.sqrt(abs(X.multiply(X.conj()).sum())) / np.sqrt(abs(A2.multiply(A2.conj()).sum()))
            e_p1 = pfrob(P, (Tm - Qm)) / np.sqrt(np.trace(s1).real)
            e_p2 = pfrob(P, (A2 - Q2)) / np.sqrt(np.trace(s2).real)
            om_b = rng.standard_normal(Gb.Nf) + 1j * rng.standard_normal(Gb.Nf)
            om_m = rng.standard_normal(Gm.Nf) + 1j * rng.standard_normal(Gm.Nf)
            l1 = Tb @ (D_op(fs_b, a_b, q) @ om_b); r1 = Dm @ (ev_op(fs_b) @ om_b)
            l2 = Tm @ (Dm @ om_m); r2 = Dn @ (evm @ om_m)
            e_cov = max(np.linalg.norm(l1 - r1) / np.linalg.norm(l1), np.linalg.norm(l2 - r2) / np.linalg.norm(l2))
            verdict(tag + "B1 decomposition algebra", e_dec <= 1e-11 and e_p1 <= 1e-11 and e_p2 <= 1e-11 and e_cov <= 1e-12,
                    f"A2 = Q2 - D h2: {e_dec:.1e}; P(A1-Q1): {e_p1:.1e}; P(A2-Q2): {e_p2:.1e}; covariance: {e_cov:.1e}")
            # (X2)(c) at levels n-1, n (diagnostic)
            Am = np.sin(3 * Pb / 2) / np.sin(Pb / 2); An = np.sin(9 * Pb / 2) / np.sin(Pb / 2)
            xm2 = np.array(list(np.ndindex(*fs_m)))[:, 1].reshape(fs_m); xn2 = Xn[:, 1].reshape(top)
            pm = e * Am * np.cos(3 * Pb * xm2 + vt + Pb); pn = e * An * np.cos(9 * Pb * xn2 + vt + 4 * Pb)
            print(f"  (X2)(c) diagnostic at e={e}: level n-1 |a - linear| = {np.abs(a_m[0]-pm).max():.2e} (other dirs {np.abs(a_m[1:]).max():.1e}); "
                  f"level n {np.abs(a_n[0]-pn).max():.2e} (e^3 = {e**3:.1e})")
        del Tb, hb, Qb, A2, Q2, Dm
        print(f"  built e={e:+.3f} in {time.time()-tb:.1f} s, RSS {rss_mb():.0f} MB")
    def coef(key, r):
        cw = c1 if r == 1 else c2
        return sum(cw[e] * store[e][key] for e in eps_list)
    PsP = {i: {e: store[e]['P'] @ store[e][f's{i}'] @ store[e]['P'] for e in eps_list} for i in (1, 2)}
    c = {}
    for i in (1, 2):
        for r in (0, 1, 2):
            if r == 0:
                c[(r, i)] = snorm(PsP[i][0.0])
            else:
                cw = c1 if r == 1 else c2
                c[(r, i)] = snorm(sum(cw[e] * PsP[i][e] for e in eps_list))
    qn = {}
    for r in (1, 2):
        qn[(r, 1)] = np.linalg.norm(coef('Qm', r), 2)
        Cm = accQ[r]['Q2']
        qn[(r, 2)] = np.sqrt(np.linalg.norm((Cm @ Cm.conj().T).toarray(), 2))
    print(f"  c_0(i): {c[(0,1)]:.4e}, {c[(0,2)]:.4e} (diagnostic)")
    for r in (1, 2):
        rc = c[(r, 2)] / c[(r, 1)]; rq = qn[(r, 2)] / qn[(r, 1)]
        verdict(tag + f"B2 r={r}", rc <= 0.25 and rq <= 0.6,
                f"c_r(1)={c[(r,1)]:.4e}, c_r(2)={c[(r,2)]:.4e}, ratio {rc:.4f} (<=0.25); ||[e^r]Q^(i)||: {qn[(r,1)]:.4e}, {qn[(r,2)]:.4e}, ratio {rq:.4f} (<=0.6)")
    # B3
    P0 = store[0.0]['P']; P1 = coef('P', 1); D1 = coef('Dn', 1)
    base = P0 @ D1 @ D1.conj().T @ P0 / 8.0
    Lc = {}; lmin = {}
    for i in (1, 2):
        s0 = store[0.0][f's{i}']
        Lc[i] = P1 @ (np.eye(nl) - P0) @ s0 @ (np.eye(nl) - P0) @ P1
        M = Bnz.conj().T @ (Lc[i] - base) @ Bnz; M = 0.5 * (M + M.conj().T)
        lmin[i] = np.linalg.eigvalsh(M).min()
    rl = snorm(Lc[2]) / snorm(Lc[1])
    verdict(tag + "B3 control (U = 1 bookkeeping leak)", min(lmin.values()) >= -1e-10 and rl >= 0.5,
            f"lambda_min(L^(i) - P0 D1 D1* P0/8) = {lmin[1]:.2e}, {lmin[2]:.2e}; ||L^(1)||={snorm(Lc[1]):.4e}, ||L^(2)||={snorm(Lc[2]):.4e}, ratio {rl:.4f}")
    for i in (1, 2):
        s0 = store[0.0][f's{i}']
        print(f"  diagnostic: termwise first-order piece ||[e]P (1-P0) s_{i}^0 P0|| = {snorm(P1 @ (np.eye(nl)-P0) @ s0 @ P0):.4e}")
    CA = accA['A2']
    print(f"  diagnostic (U = 1 pairing, [e]Q'^(i) = [e]A^(i)): ||[e]A^(1)|| = {np.linalg.norm(coef('Tm', 1), 2):.4e}, "
          f"||[e]A^(2)|| = {np.sqrt(np.linalg.norm((CA @ CA.conj().T).toarray(), 2)):.4e}")
    # B4
    An = np.sin(9 * Pb / 2) / np.sin(Pb / 2); thn = vt + 4 * Pb; P = 2 * np.pi / top[1]
    beta = -1j * q * An * np.exp(1j * thn) / 2
    def fvec(K):
        return np.exp(1j * (Xn @ K)) / np.sqrt(Nn)
    emax = 0.0; ncount = 0
    for kv in itertools.product(*[range(t) for t in top]):
        K = 2 * np.pi * np.array(kv) / np.array(top)
        if np.allclose(np.mod(K[[0, 2, 3]], 2 * np.pi), 0):
            continue
        KP = K + np.array([0, P, 0, 0])
        fK, fKP = fvec(K), fvec(KP)
        blk = np.array([[fKP.conj() @ P1[mu * Nn:(mu + 1) * Nn, nu * Nn:(nu + 1) * Nn] @ fK for nu in range(4)] for mu in range(4)])
        dK = 1 - np.exp(1j * K); dKP = 1 - np.exp(1j * KP)
        lK, lKP = np.sum(np.abs(dK) ** 2), np.sum(np.abs(dKP) ** 2)
        e1 = np.eye(4)[0]
        D1t = -beta * dK[0] + np.conj(dKP[0]) * beta
        form = -(beta * lKP * np.outer(e1, dK.conj()) - beta * lK * np.outer(dKP, e1) - D1t * np.outer(dKP, dK.conj()))
        emax = max(emax, np.abs(lK * lKP * blk - form).max()); ncount += 1
    verdict(tag + "B4 Lemma P-poles (first order)", emax <= 1e-7, f"max |normalised FD - closed form| over {ncount} K: {emax:.2e}")
    print(f"Part B time {time.time()-T0:.1f} s (cumulative), peak RSS {rss_mb():.0f} MB")

if __name__ == '__main__':
    print(f"f16 start; SMOKE={SMOKE}; numpy {np.__version__}")
    partA()
    partB(0.02, '')
    for k, d in enumerate((0.002, 0.0005)):
        print(f'=== Part B addendum {k+1} (NOT pre-stated; added after the smoke runs): the same verdicts with delta = {d}, {2*d} ===')
        partB(d, f'add{k+1}-')
    npass = sum(ok for _, ok in verdicts)
    pre = [v for v in verdicts if not v[0].startswith("add")]
    print(f"PRE-STATED verdicts: {sum(ok for _, ok in pre)}/{len(pre)} PASS; addendum: {npass - sum(ok for _, ok in pre)}/{len(verdicts) - len(pre)} PASS")
    print(f"SUMMARY: {npass}/{len(verdicts)} verdict lines PASS; total time {time.time()-T0:.1f} s; peak RSS {rss_mb():.0f} MB")
