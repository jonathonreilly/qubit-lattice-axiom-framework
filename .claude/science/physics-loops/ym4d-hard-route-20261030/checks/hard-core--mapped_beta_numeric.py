#!/usr/bin/env python3
"""Direct numerics of the Gaussian coupling coefficient B_k of the hard-constraint RG (Text 3 of hard-core--mapped.md).

Uses Prop 3.6 in complex normalisation at constant flux, charged sector of SU(2), Balaban's average [109 (0.4)]:
    Gamma_c(f) = - log|det K_f| - log|det G_f| - log|det (D_k^* G_f^-1 D_k)| + 2 log det(D_f^* D_f),   G_f = Q_f K_f^-1 Q_f^*,
per level-k cell, with flux phi = 2 pi m/N^2 per fine plaquette in the 12-plane, f = ell^2 phi, N = ell n_c, ell = L^k.
Then Gamma(f) = Gamma_0 + (B_k/2) f^2 + e f^4 + ..., where Gamma = Gamma_c + neutral part, the neutral part being f^2/8 (1 + O(eta^4)) per level-k cell
(Text 3.8 item on the neutral sector; computed explicitly below to first order in cos(phi) - 1).

PRE-REGISTERED, written before any d = 4 run.
 N0 (self test, d=3): Gamma_c from this script equals the dense formula of hard-core--mapped_onshell_flux.py at N=9, L=3, m=1 up to a flux-independent
    constant: the difference between m=1 and m=2 values agrees within 1e-8.
 N1 (self test): c_mu(z,nu) from the kernel builder agrees with a finite difference of the true M at y=0 in the symmetric gauge, rel 1e-5.
 N2 (prediction, d=4, L=3): with c_0 = (11/(3 pi^2)) log 3 = 0.4081, B_2 - B_1 lies within 25 percent of c_0. Failure would not by itself refute Theorem P1, since L=3 is
    small and n_c is small, but it would have to be explained before the theorem is relied on.
 N3 (report): B_1, B_2, and the fit residual. Finite-size control: B_1 at n_c = 5, 7.
Run one job at a time under the numeric lock. BLAS threads 1. RSS guard 2 GB.
Usage: beta_numeric.py selftest | beta_numeric.py run L k n_c [m_list]
"""
import itertools, math, resource, sys, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

def rss_guard():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == 'darwin':
        r /= 1024
    if r > 2_000_000:
        raise SystemExit("RSS above 2 GB")

def wedge(x, y):
    return x[0]*y[1]-x[1]*y[0]

def block_points(d, L, s):
    R = (L-1)//2
    return [tuple(s*v for v in p) for p in itertools.product(range(-R, R+1), repeat=d)]

def contours(y, x, s):
    """shortest axial contours from y to y+x with lattice step s, as lists of sites"""
    d = len(y)
    nz = [i for i in range(d) if x[i] != 0]
    res = []
    for p in (itertools.permutations(nz) if nz else [()]):
        cur = list(y); pts = [tuple(cur)]
        for i in p:
            target = y[i]+x[i]
            step = s if target > cur[i] else -s
            while cur[i] != target:
                cur[i] += step
                pts.append(tuple(cur))
        res.append(pts)
    return res

def path_angle_and_add(pts, s, phi, base, weight, out):
    """adds weight * sum_b s_b exp(2i angle) to out[(bond base, dir)]; angle is the transport angle from the loop base, in the symmetric gauge"""
    ang = base
    for a, b in zip(pts[:-1], pts[1:]):
        nu = [i for i in range(len(a)) if a[i] != b[i]][0]
        if b[nu] > a[nu]:
            key = (a, nu)
            out[key] = out.get(key, 0)+weight*np.exp(2j*ang)
            ang += (phi/2)*wedge(a, b)
        else:
            key = (b, nu)
            ang -= (phi/2)*wedge(b, a)
            out[key] = out.get(key, 0)-weight*np.exp(2j*ang)
    return ang

def loop_area_angle(pts, phi):
    ang = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        ang += (phi/2)*wedge(a, b)
    return ang

def one_step_kernel(d, L, s, phi):
    """c[mu] = dict {(z,nu): coefficient} of the charged linearisation of one step of M at the bond (0, mu), lattice step s (fine units).
    z is the base point of the fine bond, phi the flux per FINE plaquette in the 12-plane, symmetric gauge A_nu(a) = (phi/2) a ^ (a + nu)."""
    pts = block_points(d, L, s)
    y = (0,)*d
    c = []
    for mu in range(d):
        yp = tuple((L*s if i == mu else 0) for i in range(d))
        cpts = [tuple((t*s if i == mu else 0) for i in range(d)) for t in range(L+1)]
        items = []
        phisum = 0.0
        for x in pts:
            G = contours(y, x, s)
            Gp = contours(yp, x, s)
            xs = tuple(y[i]+x[i] for i in range(d))
            straight = [tuple(xs[i]+(t*s if i == mu else 0) for i in range(d)) for t in range(L+1)]
            wt = 1.0/(len(pts)*len(G)*len(Gp))
            for g in G:
                for gp in Gp:
                    loop = list(g)+straight[1:]+list(reversed(gp))[1:]+list(reversed(cpts))[1:]
                    phi_l = loop_area_angle(loop, phi)
                    items.append((loop, wt, phi_l))
                    phisum += wt*phi_l
        xib = 2j*phisum
        Lp = (np.exp(xib)-1)/xib if abs(xib) > 1e-14 else 1.0
        out = {}
        for loop, wt, phi_l in items:
            xi = 2j*phi_l
            Lx = xi/(np.exp(xi)-1) if abs(xi) > 1e-14 else 1.0
            path_angle_and_add(loop, s, phi, 0.0, Lp*wt*Lx, out)
        path_angle_and_add(cpts, s, phi, phisum, 1.0, out)
        c.append({k: v for k, v in out.items() if abs(v) > 1e-14})
    return c

class Fold:
    """Magnetic periodicity in the 12-plane: w(x + a) = exp(-i (theta/2) a ^ x) w(x), a in N Z^2, theta = 2 phi, coordinates in fine units; period N (fine units) in all directions.
    The sites of a lattice of step s are indexed by (x1/s, x2/s) mod N/s."""
    def __init__(self, N, s, theta):
        self.N = N; self.s = s; self.theta = theta; self.n = N//s
    def fold(self, x1, x2):
        N = self.N
        f1 = x1 % N; f2 = x2 % N
        a = (x1-f1, x2-f2)
        ph = -(self.theta/2)*wedge(a, (f1, f2))
        return f1, f2, ph
    def index(self, x1, x2):
        return (x1//self.s)*self.n+(x2//self.s)

def K_blocks(d, N, phi):
    """Returns a function q -> sparse K(q) for the charged Feynman operator K = H + D D^* on bonds (x1,x2,nu), Fourier in x3.. xd.
    Built from local terms in the symmetric gauge with the exact plaquette form; flux only in the 12-plane."""
    theta = 2*phi
    F = Fold(N, 1, theta)
    nb = d*N*N
    # terms: list of (row, col, value, shift vector for the Fourier phase in the transverse directions)
    terms = {}
    def add(i, j, v, tvec):
        key = (i, j, tvec)
        terms[key] = terms.get(key, 0)+v
    A = lambda a, b: (phi/2)*wedge(a, b)
    def e(mu):
        return tuple(1 if i == mu else 0 for i in range(d))
    def plus(x, v):
        return tuple(x[i]+v[i] for i in range(d))
    for x1 in range(N):
        for x2 in range(N):
            x = (x1, x2)+(0,)*(d-2)
            def bond_index(z, nu):
                """index and folding phase of the charged bond variable at base z"""
                f1, f2, ph = F.fold(z[0], z[1])
                return (f1*N+f2)*d+nu, ph, tuple(z[2:])
            for mu, nu in itertools.combinations(range(d), 2):
                xm = plus(x, e(mu)); xn = plus(x, e(nu)); xmn = plus(xm, e(nu))
                a1 = A(x, xm); a2 = A(xm, xmn); a3 = A(xmn, xn); a4 = A(xn, x)
                phip = a1+a2+a3+a4
                # w_1 = w_mu(x); w_2 = e^{2i a1} w_nu(xm); w_3 = -e^{2i(a1+a2+ a3)} w_mu(xn); w_4 = -e^{2i phip} w_nu(x)   (a3 = -A_mu(xn), a4 = -A_nu(x))
                co = [1.0, np.exp(2j*a1), -np.exp(2j*(a1+a2+a3)), -np.exp(2j*phip)]
                sites = [(x, mu), (xm, nu), (xn, mu), (x, nu)]
                data = []
                for (z, n_), c_ in zip(sites, co):
                    idx, ph, tv = bond_index(z, n_)
                    data.append((idx, c_*np.exp(1j*ph), tv))
                for a in range(4):
                    ia, ca, ta = data[a]
                    tvec = tuple(p-q for p, q in zip(ta, ta))
                    add(ia, ia, abs(ca)**2*math.cos(phip), tvec)
                    for b in range(a+1, 4):
                        ib, cb, tb = data[b]
                        # (1/2) w^dag H w contains (1/2)[conj(w_b) conj(c_b) c_a e^{i phi} w_a + h.c.] ; tvec = col shift minus row shift
                        add(ib, ia, np.conj(cb)*ca*np.exp(1j*phip), tuple(p-q for p, q in zip(ta, tb)))
                        add(ia, ib, np.conj(ca)*cb*np.exp(-1j*phip), tuple(p-q for p, q in zip(tb, ta)))
    # D D^*: use the same device on sites
    D_terms = D_blocks(d, N, phi, F)
    keys = list(terms.keys())
    I = np.array([k[0] for k in keys]); J = np.array([k[1] for k in keys]); V = np.array([terms[k] for k in keys]); T = np.array([k[2] for k in keys], dtype=float).reshape(len(keys), d-2)
    def K_of_q(q):
        ph = np.exp(1j*(T@np.array(q)))
        H = sp.csr_matrix((V*ph, (I, J)), shape=(nb, nb))
        Dq = D_terms(q)
        return (H+Dq@Dq.conj().T).tocsc(), Dq
    return K_of_q

def D_blocks(d, N, phi, F=None, s=1):
    """Sparse covariant gradient D: sites -> bonds of the lattice of step s, Fourier in the transverse directions, momentum q conjugate to fine units."""
    theta = 2*phi
    F = F if F is not None else Fold(N, s, theta)
    n = N//s
    ns = n*n; nb = d*ns
    I = []; J = []; V = []; T = []
    for k1 in range(n):
        for k2 in range(n):
            x = (k1*s, k2*s)
            sidx = k1*n+k2
            for mu in range(d):
                row = sidx*d+mu
                I.append(row); J.append(sidx); V.append(1.0); T.append(0)
                if mu < 2:
                    y = (x[0]+(s if mu == 0 else 0), x[1]+(s if mu == 1 else 0))
                    ang = (phi/2)*wedge(x, y)
                    f1, f2, ph = F.fold(y[0], y[1])
                    I.append(row); J.append((f1//s)*n+(f2//s)); V.append(-np.exp(2j*ang)*np.exp(1j*ph)); T.append(0)
                else:
                    I.append(row); J.append(sidx); V.append(-1.0); T.append(mu-1)
    I = np.array(I); J = np.array(J); V = np.array(V); T = np.array(T)
    def D_of_q(q):
        q = np.asarray(q)
        ph = np.ones(len(V), dtype=complex)
        for t in range(1, d-1):
            ph[T == t] = np.exp(1j*s*q[t-1])
        return sp.csr_matrix((V*ph, (I, J)), shape=(nb, ns))
    return D_of_q

def build_Q(d, L, s, N, phi):
    """Sparse one-step Q from level step s to level step L s. Returns a function q -> Q(q). Rows: bonds (y1,y2,mu) of the lattice of step L s with y3.. = 0.
    Columns: bonds (x1,x2,nu) of the lattice of step s. Fourier: column plane wave exp(i q x_perp)."""
    theta = 2*phi
    c = one_step_kernel(d, L, s, phi)
    Fc = Fold(N, L*s, theta); Ff = Fold(N, s, theta)
    nc = N//(L*s); nf = N//s
    I = []; J = []; V = []; T = []
    for y1k in range(nc):
        for y2k in range(nc):
            y = (y1k*L*s, y2k*L*s)
            for mu in range(d):
                row = (y1k*nc+y2k)*d+mu
                for (z, nu), val in c[mu].items():
                    x = (y[0]+z[0], y[1]+z[1])
                    tw = (theta/2)*wedge(y, x)
                    f1, f2, ph = Ff.fold(x[0], x[1])
                    I.append(row); J.append(((f1//s)*nf+(f2//s))*d+nu); V.append(val*np.exp(1j*(tw+ph))); T.append(tuple(z[2:]))
    I = np.array(I); J = np.array(J); V = np.array(V); T = np.array(T, dtype=float).reshape(len(V), d-2)
    shape = (nc*nc*d, nf*nf*d)
    def Q_of_q(q):
        return sp.csr_matrix((V*np.exp(1j*(T@np.asarray(q))), (I, J)), shape=shape)
    return Q_of_q

def logabsdet_sparse(A):
    lu = spla.splu(A.tocsc(), permc_spec='COLAMD')
    return float(np.sum(np.log(np.abs(lu.U.diagonal())))+np.sum(np.log(np.abs(lu.L.diagonal())))), lu

def gamma_c(d, L, k, n_c, m, verbose=False):
    ell = L**k
    N = ell*n_c
    phi = 2*math.pi*m/N**2
    t0 = time.time()
    K_of_q = K_blocks(d, N, phi)
    Qs = [build_Q(d, L, L**j, N, phi) for j in range(k)]
    Dc_of_q = D_blocks(d, N, phi, s=ell)
    D_of_q = D_blocks(d, N, phi)
    ncoarse = n_c*n_c
    dt = d-2
    # coarse momenta p = 2 pi a / n_c in the transverse directions; fine q = (p + 2 pi b)/ell
    ld_K = 0.0; ld_X = 0.0; ld_G = 0.0; ld_Z = 0.0
    coarse_grid = list(itertools.product(range(n_c), repeat=dt))
    for a in coarse_grid:
        dimG = d*ncoarse
        G = np.zeros((dimG, dimG), dtype=complex)
        for b in itertools.product(range(ell), repeat=dt):
            q = [2*math.pi*(a[i]+n_c*b[i])/N for i in range(dt)]
            Kq, Dq = K_of_q(q)
            l, lu = logabsdet_sparse(Kq)
            ld_K += l
            Xq = (Dq.conj().T@Dq).tocsc()
            ld_X += logabsdet_sparse(Xq)[0]
            Q = Qs[0](q)
            for j in range(1, k):
                Q = Qs[j](q)@Q
            Qd = Q.conj().T.toarray()
            Sol = lu.solve(Qd)
            G += (Q@Sol)/ell**dt
            rss_guard()
        ld_G += np.linalg.slogdet(G)[1]
        Ginv = np.linalg.inv(G)
        pq = [2*math.pi*a[i]/N for i in range(dt)]
        Dc = Dc_of_q(pq).toarray()
        Z = Dc.conj().T@Ginv@Dc
        ld_Z += np.linalg.slogdet(Z)[1]
    total = -ld_K-ld_G-ld_Z+2*ld_X
    cells = n_c**d
    if verbose:
        print(f"   d={d} L={L} k={k} n_c={n_c} m={m}: Gamma_c per cell {total/cells:.8f} time {time.time()-t0:.1f}s", flush=True)
    return total/cells, ell**2*phi

def selftest():
    d = 3; L = 3
    # N1: kernel against a finite difference of the true M at y=0, symmetric gauge, no wrap
    import importlib.util, os
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location('onshell', os.path.join(here, 'hard-core--mapped_onshell_flux.py'))
    o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
    phi = 0.07
    c = one_step_kernel(d, L, 1, phi)
    class CF:
        def __init__(self):
            self.delta = {}
            self.lat = None
        def get(self, x, mu):
            y = tuple(x[i]+(1 if i == mu else 0) for i in range(d))
            a = (phi/2)*wedge(x, y)
            U = np.array([[np.exp(1j*a), 0], [0, np.exp(-1j*a)]], dtype=complex)
            if (tuple(x), mu) in self.delta:
                U = self.delta[(tuple(x), mu)]@U
            return U
    conf = CF()
    worst = 0.0
    eps = 1e-5
    rng = np.random.default_rng(3)
    for mu in range(d):
        keys = list(c[mu].keys())
        for t in range(4):
            key = keys[int(rng.integers(0, len(keys)))]
            Y0, Uc0 = o.M_bond(conf, (0,)*d, mu)
            M0 = o.expi(1.0, Y0)@Uc0
            conf.delta = {key: o.expi(1.0, np.array([eps, 0, 0]))}
            Y1, Uc1 = o.M_bond(conf, (0,)*d, mu)
            conf.delta = {}
            M1 = o.expi(1.0, Y1)@Uc1
            v = o.log_su2(M1@M0.conj().T)/eps
            dw = v[0]-1j*v[1]
            worst = max(worst, abs(dw-c[mu][key])/max(abs(c[mu][key]), 1e-9))
    print("N1 kernel vs finite difference of M, worst rel:", worst)
    # N0: compare with the dense formula at N=9
    vals = []
    for m in (1, 2):
        g, f = gamma_c(d, L, 1, 3, m)
        lat, conf2, _ = o.run(m)
        H, D = o.charged_ops(lat, conf2)
        K = H+D@D.conj().T
        Nc, Ac = o.coarse_data(lat, conf2)
        D1 = o.coarse_D(lat, Nc, Ac)
        Q = o.Q_charged(lat, conf2)
        G = Q@np.linalg.inv(K)@Q.conj().T
        lad = lambda M_: np.linalg.slogdet(M_)[1]
        dense = -lad(K)-lad(G)-lad(D1.conj().T@np.linalg.inv(G)@D1)+2*lad(D.conj().T@D)
        vals.append((g*3**d, dense))
        print(f"N0 m={m}: sparse total {g*3**d:.8f}  dense total {dense:.8f}  difference {g*3**d-dense:.8f}")
    d0 = (vals[0][0]-vals[0][1])-(vals[1][0]-vals[1][1])
    print("N0 flux independence of the difference:", d0)
    print("SELFTEST", "PASS" if abs(d0) < 1e-8 and worst < 1e-4 else "FAIL")

def neutral_per_cell(f):
    """First order in cos(phi) - 1 of the neutral transverse functional per level-k cell, leading term as eta -> 0"""
    return f*f/8

def run(L, k, n_c, ms):
    d = 4
    xs = []; ys = []
    for m in ms:
        g, f = gamma_c(d, L, k, n_c, m, verbose=True)
        xs.append(f); ys.append(g+neutral_per_cell(f))
    xs = np.array(xs); ys = np.array(ys)
    # fit Gamma_0 + (B/2) f^2 + e f^4 (exact solve if 3 points)
    X = np.vstack([np.ones_like(xs), xs**2/2, xs**4]).T
    coef, res, rk, sv = np.linalg.lstsq(X, ys, rcond=None)
    print(f"RESULT L={L} k={k} n_c={n_c} ms={ms}: B_k = {coef[1]:.6f}  e = {coef[2]:.6f}  Gamma_0 = {coef[0]:.6f}", flush=True)
    return coef[1]

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'selftest':
        selftest()
    elif len(sys.argv) > 1 and sys.argv[1] == 'run':
        L = int(sys.argv[2]); k = int(sys.argv[3]); n_c = int(sys.argv[4])
        ms = [int(v) for v in sys.argv[5].split(',')] if len(sys.argv) > 5 else [1, 2, 3]
        run(L, k, n_c, ms)
    else:
        print(__doc__)
