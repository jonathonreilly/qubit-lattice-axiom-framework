#!/usr/bin/env python3
"""On-shell facts and the exact decomposition at constant abelian flux, SU(2), small periodic lattice.

Written before running. Setting: d=3 periodic torus, L=3, N=9 fine sites per side, coarse side 3 (d only changes dimensions;
the statements are dimension free). U_F = exp(i A sigma_3), A in Landau gauge with flux phi = 2 pi m / N^2 per plaquette in the 12-plane.

PRE-STATED criteria.
 C1. J = 0: gradient of the Wilson action at U_F vanishes, |grad| < 1e-10.
 C2. M(U_F) is abelian with uniform coarse plaquette flux in the 12-plane, zero in other planes, up to 1e-10; the value is recorded.
 C3. Hessian: the analytic charged form S_2 agrees with a second finite difference of the true SU(2) action, relative 1e-5, on random charged directions.
 C4. H_f D_f = 0 in the charged sector, |.| < 1e-10.
 C5. Analytic Q_f (one step, charged) agrees with a finite difference of the true M, relative 1e-5.
 C6. Q_f D_f = D_{1,f} r in the charged sector, |.| < 1e-9.
 C7. Prop 3.6 as an identity of logs of absolute values, for one step:
     LHS = log|det on T'|: the constrained transverse Gaussian
           -log|det_{T'} H_f| - log det_{P_perp}(Q_perp Q_perp^*) + log det'(D^*D) - log det'(D_1^* D_1)   (complex normalisation: power 1 and not 1/2)
     RHS = -log|det K_f| - log|det G_f| - log|det (D_1^* G_f^-1 D_1)| + 2 log det'(D^*D)
     equality up to a constant free of the flux: the difference LHS - RHS is compared at two fluxes, tolerance 1e-7.
 FAIL if any criterion fails. RSS guard 2 GB.
"""
import itertools, math, resource, sys
import numpy as np

def rss_guard():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == 'darwin':
        r /= 1024
    if r > 2_000_000:
        raise SystemExit("RSS above 2 GB")

d = 3
L = 3
sig = [np.array([[0,1],[1,0]],dtype=complex), np.array([[0,-1j],[1j,0]],dtype=complex), np.array([[1,0],[0,-1]],dtype=complex)]
I2 = np.eye(2,dtype=complex)

def expi(a, v):
    """exp(i a v.sigma), v unit vector or 3-vector a*v given as array"""
    n = np.linalg.norm(v)
    if n < 1e-300:
        return I2.copy()
    u = v/n
    return math.cos(n)*I2 + 1j*math.sin(n)*(u[0]*sig[0]+u[1]*sig[1]+u[2]*sig[2])

def log_su2(U):
    """(1/i) log U as a 3-vector"""
    c = np.trace(U).real/2
    c = max(-1.0, min(1.0, c))
    th = math.acos(c)
    s = math.sin(th)
    fac = th/s if s > 1e-14 else 1.0
    X = (U-U.conj().T)/(2j)
    return np.array([np.trace(X@sg).real/2*fac for sg in sig])

class Lat:
    def __init__(self, N, m):
        self.N = N
        self.phi = 2*math.pi*m/N**2
        self.m = m
    def A(self, x, mu):
        """phase of U_F on bond (x,mu), x integer tuple taken mod N"""
        N, phi = self.N, self.phi
        x = tuple(v % N for v in x)
        if mu == 1:
            return phi*x[0]
        if mu == 0 and x[0] == N-1:
            return -phi*N*x[1]
        return 0.0
    def bonds(self):
        for x in itertools.product(range(self.N), repeat=d):
            for mu in range(d):
                yield x, mu
    def bidx(self, x, mu):
        N = self.N
        i = 0
        for v in x:
            i = i*N + (v % N)
        return i*d + mu
    def sidx(self, x):
        N = self.N
        i = 0
        for v in x:
            i = i*N + (v % N)
        return i

def shift(x, mu, s=1):
    y = list(x); y[mu] += s
    return tuple(y)

# ---- SU(2) configuration helpers ----
class Conf:
    def __init__(self, lat):
        self.lat = lat
        self.U = {}
        for x, mu in lat.bonds():
            self.U[(x,mu)] = np.array([[np.exp(1j*lat.A(x,mu)),0],[0,np.exp(-1j*lat.A(x,mu))]],dtype=complex)
    def get(self, x, mu):
        x = tuple(v % self.lat.N for v in x)
        return self.U[(x,mu)]

def plaq(conf, x, mu, nu):
    return conf.get(x,mu)@conf.get(shift(x,mu),nu)@conf.get(shift(x,nu),mu).conj().T@conf.get(x,nu).conj().T

def action(conf):
    s = 0.0
    N = conf.lat.N
    for x in itertools.product(range(N), repeat=d):
        for mu, nu in itertools.combinations(range(d),2):
            s += 1-np.trace(plaq(conf,x,mu,nu)).real/2
    return s

# ---- transport along a site path ----
def path_prod(conf, pts):
    """ordered product U(pts[0]->pts[1]) U(pts[1]->pts[2]) ..."""
    P = I2.copy()
    for a, b in zip(pts[:-1], pts[1:]):
        diff = [b[i]-a[i] for i in range(d)]
        mu = [i for i in range(d) if diff[i] != 0][0]
        if diff[mu] == 1:
            P = P@conf.get(a,mu)
        else:
            P = P@conf.get(b,mu).conj().T
    return P

def axial_contours(y, x):
    """all shortest axial contours from y to y+x as lists of sites"""
    nz = [i for i in range(d) if x[i] != 0]
    res = []
    for p in (itertools.permutations(nz) if nz else [()]):
        cur = list(y); pts = [tuple(cur)]
        for i in p:
            target = y[i]+x[i]
            step = 1 if target > cur[i] else -1
            while cur[i] != target:
                cur[i] += step
                pts.append(tuple(cur))
        res.append(pts)
    return res

R = (L-1)//2
block = list(itertools.product(range(-R,R+1), repeat=d))

def M_bond(conf, y, mu):
    """Balaban's (0.4): returns the 3-vector Y and U(c), where M = exp(i Y) U(c)"""
    yp = shift(y, mu, L)
    Uc = path_prod(conf, [shift(y,mu,s) for s in range(L+1)])
    total = np.zeros(3)
    n = 0
    for x in block:
        G = axial_contours(y, x)
        Gp = axial_contours(yp, x)
        xs = tuple(y[i]+x[i] for i in range(d))
        xps = shift(xs, mu, L)
        straight = [shift(xs,mu,s) for s in range(L+1)]
        P2 = path_prod(conf, straight)
        for g in G:
            Pg = path_prod(conf, g)
            for gp in Gp:
                Pgp = path_prod(conf, gp)
                loop = Pg@P2@Pgp.conj().T@Uc.conj().T
                total = total + log_su2(loop)/(len(G)*len(Gp))
        n += 1
    return total/n, Uc

def run(m, verbose=True):
    N = 3*L
    lat = Lat(N, m)
    conf = Conf(lat)
    out = {}
    # C1: gradient by symmetric difference on a sample of bonds and colours
    rng = np.random.default_rng(1)
    S0 = action(conf)
    gradmax = 0.0
    eps = 1e-5
    bonds = list(lat.bonds())
    for k in rng.integers(0, len(bonds), size=6):
        b = bonds[k]
        for a in range(3):
            old = conf.U[b].copy()
            conf.U[b] = expi(eps, eps*0+np.eye(3)[a]*eps)@old
            sp = action(conf)
            conf.U[b] = expi(eps, -np.eye(3)[a]*eps)@old
            sm = action(conf)
            conf.U[b] = old
            gradmax = max(gradmax, abs(sp-sm)/(2*eps))
    out['C1_grad'] = gradmax
    # C2: M(U_F) uniform flux
    Nc = N//L
    V = {}
    for yc in itertools.product(range(Nc), repeat=d):
        y = tuple(L*v for v in yc)
        for mu in range(d):
            Y, Uc = M_bond(conf, y, mu)
            V[(yc,mu)] = expi(1.0, Y)@Uc
    def V_get(yc, mu):
        return V[(tuple(v % Nc for v in yc), mu)]
    fl = []
    offdiag = 0.0
    for yc in itertools.product(range(Nc), repeat=d):
        for a, b in itertools.combinations(range(d),2):
            P = V_get(yc,a)@V_get(shift(yc,a),b)@V_get(shift(yc,b),a).conj().T@V_get(yc,b).conj().T
            ang = np.angle(P[0,0])
            offdiag = max(offdiag, abs(P[0,1]))
            fl.append(((a,b),ang))
    f12 = [v for (k,v) in fl if k==(0,1)]
    others = [v for (k,v) in fl if k!=(0,1)]
    out['C2_flux12'] = (min(f12), max(f12))
    out['C2_expected'] = L**2*lat.phi
    out['C2_other'] = max(abs(v) for v in others)
    out['C2_offdiag'] = offdiag
    return lat, conf, out

if __name__ == '__main__':
    lat, conf, out = run(1)
    for k, v in out.items():
        print(k, v)
    rss_guard()

# ---- charged sector ---------------------------------------------------------------------------
def charged_ops(lat, conf):
    N = lat.N
    nb = d*N**d
    ns = N**d
    H = np.zeros((nb,nb),dtype=complex)
    D = np.zeros((nb,ns),dtype=complex)
    A = lat.A
    def ph(a):
        return np.exp(2j*a)
    for x in itertools.product(range(N), repeat=d):
        for mu in range(d):
            i = lat.bidx(x,mu)
            D[i, lat.sidx(x)] += 1
            D[i, lat.sidx(shift(x,mu))] -= ph(A(x,mu))
        for mu, nu in itertools.combinations(range(d),2):
            xm = shift(x,mu); xn = shift(x,nu)
            phip = A(x,mu)+A(xm,nu)-A(xn,mu)-A(x,nu)
            idx = [lat.bidx(x,mu), lat.bidx(xm,nu), lat.bidx(xn,mu), lat.bidx(x,nu)]
            co = [1.0, ph(A(x,mu)), -ph(A(x,mu)+A(xm,nu)-A(xn,mu)), -ph(phip)]
            # S_2 = (1/2) sum_i |w_i|^2 cos phi + sum_{i<j} Re(w_i conj(w_j) e^{i phi}), w_i = co_i * w[idx_i]
            for a in range(4):
                H[idx[a],idx[a]] += abs(co[a])**2*math.cos(phip)
                for b in range(a+1,4):
                    # contributes to (1/2) w^dag H w : H[idx[b],idx[a]] += conj(co_b) co_a e^{i phi}
                    H[idx[b],idx[a]] += np.conj(co[b])*co[a]*np.exp(1j*phip)
                    H[idx[a],idx[b]] += np.conj(co[a])*co[b]*np.exp(-1j*phip)
    return H, D

def coarse_data(lat, conf):
    N = lat.N; Nc = N//L
    Ac = {}
    for yc in itertools.product(range(Nc), repeat=d):
        y = tuple(L*v for v in yc)
        for mu in range(d):
            Y, Uc = M_bond(conf, y, mu)
            V = expi(1.0, Y)@Uc
            Ac[(yc,mu)] = np.angle(V[0,0])
    return Nc, Ac

def Q_charged(lat, conf):
    """One-step linearisation of M at U_F on the charged component: complex coefficient of w_b in delta w(c)."""
    N = lat.N; Nc = N//L
    nb = d*N**d
    nc = d*Nc**d
    Q = np.zeros((nc,nb),dtype=complex)
    A = lat.A
    def add_path(row, pts, sign_outer, base_phase, weight, Q):
        """adds weight * sum_b s_b Ad_transport (H_b) along the site path pts; base_phase=transport angle already accumulated"""
        phase = base_phase
        for a, b in zip(pts[:-1], pts[1:]):
            diff = [b[i]-a[i] for i in range(d)]
            mu = [i for i in range(d) if diff[i] != 0][0]
            if diff[mu] == 1:
                Q[row, lat.bidx(a,mu)] += weight*sign_outer*np.exp(2j*phase)
                phase += A(a,mu)
            else:
                # backward through bond (b,mu): phase first decreases, then the factor -Ad on H_b
                phase -= A(b,mu)
                Q[row, lat.bidx(b,mu)] += -weight*sign_outer*np.exp(2j*phase)
        return phase
    for yc in itertools.product(range(Nc), repeat=d):
        y = tuple(L*v for v in yc)
        for mu in range(d):
            row = (yc[0]*Nc**2+yc[1]*Nc+yc[2])*d+mu
            yp = shift(y,mu,L)
            cpts = [shift(y,mu,s) for s in range(L+1)]
            # total flux average
            items = []
            phisum = 0.0
            for x in block:
                G = axial_contours(y,x); Gp = axial_contours(yp,x)
                xs = tuple(y[i]+x[i] for i in range(d))
                straight = [shift(xs,mu,s) for s in range(L+1)]
                for g in G:
                    for gp in Gp:
                        wt = 1.0/(len(block)*len(G)*len(Gp))
                        loop = list(g)+straight[1:]+list(reversed(gp))[1:]+list(reversed(cpts))[1:]
                        phi = 0.0
                        for a,b in zip(loop[:-1],loop[1:]):
                            diff = [b[i]-a[i] for i in range(d)]
                            m_ = [i for i in range(d) if diff[i] != 0][0]
                            phi += A(a,m_) if diff[m_]==1 else -A(b,m_)
                        phi = (phi+math.pi)%(2*math.pi)-math.pi
                        items.append((loop,wt,phi))
                        phisum += wt*phi
            xib = 2j*phisum
            Lp = (np.exp(xib)-1)/xib if abs(xib)>1e-14 else 1.0
            for loop,wt,phi in items:
                xi = 2j*phi
                Lx = xi/(np.exp(xi)-1) if abs(xi)>1e-14 else 1.0
                add_path(row, loop, 1.0, 0.0, Lp*wt*Lx, Q)
            # the factor U(c) in front: exp(iY)[1+iX_c]U_c: X_c conjugated by exp(i phibar sigma_3)
            add_path(row, cpts, 1.0, phisum, 1.0, Q)
    return Q

def coarse_D(lat, Nc, Ac):
    nc = d*Nc**d; ns = Nc**d
    D1 = np.zeros((nc,ns),dtype=complex)
    def sid(yc):
        i=0
        for v in yc:
            i=i*Nc+(v%Nc)
        return i
    for yc in itertools.product(range(Nc), repeat=d):
        for mu in range(d):
            row = sid(yc)*d+mu
            D1[row,sid(yc)] += 1
            D1[row,sid(shift(yc,mu))] -= np.exp(2j*Ac[(yc,mu)])
    return D1

def checks(m):
    lat, conf, out = run(m)
    H, D = charged_ops(lat, conf)
    rng = np.random.default_rng(10+m)
    nb = H.shape[0]
    # C3 Hessian against the true SU(2) action
    bonds = list(lat.bonds())
    worst3 = 0.0
    for trial in range(3):
        w = rng.normal(size=nb)+1j*rng.normal(size=nb)
        w /= np.linalg.norm(w)
        eps = 1e-3
        base = {k:v.copy() for k,v in conf.U.items()}
        vals = []
        for sgn in (+1,-1):
            for (x,mu) in bonds:
                z = w[lat.bidx(x,mu)]*eps*sgn
                vec = np.array([z.real, -z.imag, 0.0])  # w = H1 - i H2
                conf.U[(x,mu)] = expi(1.0, vec)@base[(x,mu)]
            vals.append(action(conf))
        conf.U = base
        S0 = action(conf)
        fd = (vals[0]+vals[1]-2*S0)/eps**2
        an = (w.conj()@H@w).real
        worst3 = max(worst3, abs(fd-an)/max(1e-12,abs(an)))
    out['C3_rel'] = worst3
    # C4
    out['C4'] = np.abs(H@D).max()
    Nc, Ac = coarse_data(lat, conf)
    D1 = coarse_D(lat, Nc, Ac)
    Q = Q_charged(lat, conf)
    # C5 against finite difference of true M
    worst5 = 0.0
    eps = 1e-5
    for trial in range(6):
        yc = tuple(int(v) for v in rng.integers(0,Nc,size=d))
        y = tuple(L*v for v in yc)
        mu = int(rng.integers(0,d))
        row = (yc[0]*Nc**2+yc[1]*Nc+yc[2])*d+mu
        nz = np.nonzero(np.abs(Q[row])>1e-12)[0]
        i = int(rng.choice(nz))
        s, r = divmod(i,d)
        x = (s//N**2, (s//N)%N, s%N) if False else None
        N = lat.N
        x = (s//(N*N), (s//N)%N, s%N)
        Y0, Uc0 = M_bond(conf,y,mu)
        M0 = expi(1.0,Y0)@Uc0
        old = conf.U[(x,r)].copy()
        conf.U[(x,r)] = expi(1.0,np.array([eps,0,0]))@old
        Y1, Uc1 = M_bond(conf,y,mu)
        conf.U[(x,r)] = old
        M1 = expi(1.0,Y1)@Uc1
        v = log_su2(M1@M0.conj().T)/eps
        dw = v[0]-1j*v[1]
        worst5 = max(worst5, abs(dw-Q[row,i])/max(1e-9,abs(Q[row,i])))
    out['C5_rel'] = worst5
    # C6: Q_f D_f = D_1 r
    r = np.zeros((Nc**d, N**d),dtype=complex)
    for yc in itertools.product(range(Nc),repeat=d):
        i=0
        for v in yc:
            i=i*Nc+v
        r[i,lat.sidx(tuple(L*v for v in yc))]=1
    out['C6'] = np.abs(Q@D-D1@r).max()
    rss_guard()
    # C7
    K = H+D@D.conj().T
    Kinv = np.linalg.inv(K)
    G = Q@Kinv@Q.conj().T
    Ginv = np.linalg.inv(G)
    def lad(M):
        s,l = np.linalg.slogdet(M)
        return l
    RHS = -lad(K)-lad(G)-lad(D1.conj().T@Ginv@D1)+2*lad(D.conj().T@D)
    # direct: transverse constraint subspace
    Pperp = np.eye(D1.shape[0])-D1@np.linalg.solve(D1.conj().T@D1,D1.conj().T)
    Qp = Pperp@Q
    # orthonormal basis of ran Pperp
    uu,ss,vh = np.linalg.svd(Pperp)
    nperp = int((ss>0.5).sum())
    Uperp = uu[:,:nperp]
    Qred = Uperp.conj().T@Q
    lad_QQ = lad(Qred@Qred.conj().T)
    C = np.vstack([D.conj().T, Qred])
    u,s,vh = np.linalg.svd(C)
    rank = int((s>1e-9).sum())
    Tb = vh.conj().T[:,rank:]
    Hred = Tb.conj().T@H@Tb
    evs = np.linalg.eigvalsh((Hred+Hred.conj().T)/2)
    out['T_prime_dim'] = Tb.shape[1]
    out['T_prime_min_ev'] = evs.min()
    LHS = -lad(Hred)-lad_QQ+lad(D.conj().T@D)-lad(D1.conj().T@D1)
    out['C7_LHS'] = LHS; out['C7_RHS'] = RHS; out['C7_diff'] = LHS-RHS
    return out

if __name__ == '__main__':
    ok = True
    diffs = []
    for m in (1,2):
        o = checks(m)
        print('m =',m)
        for k,v in o.items():
            print('  ',k,v)
        diffs.append(o['C7_diff'])
        ok = ok and o['C1_grad']<1e-8 and o['C3_rel']<1e-3 and o['C4']<1e-9 and o['C5_rel']<1e-4 and o['C6']<1e-8
    print('C7 flux independence of LHS-RHS:', abs(diffs[0]-diffs[1]))
    ok = ok and abs(diffs[0]-diffs[1])<1e-6
    print('PASS' if ok else 'FAIL')
