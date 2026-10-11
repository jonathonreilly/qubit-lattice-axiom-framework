"""RL1 (G): conformal lens (G-L lane B setting, Omega^2 = 1 + A exp(-|x-c|^2/w^2), R = 100, w = 10), deterministic quadrature
of the exact interval volume V_g (reuses the G-L checker's v2 quadrature).  Two checks:
 (b) volume-weighted one-hop links  K_w = a_w w(rho V) L:  mean = a_w w(rho V_g) e^{-rho V_g}.  Ratio to GR with each weight's FLAT
     normalisation a_w.  Lemma (exact substitution): every such ratio -> Omega_x Omega_y/sqrt(<Omega^4>_w) = (nu Delta)^{-1/2} (G-L value).
 (c-loc) far-cone leakage of a LOCAL layer operator's mean kernel f_C(rho V_g) (BD C=(1,-9,16,-8)): the cone integral
     J_C(rho) = int ds f_C(rho V_g(s)) h(s) along the lensed ray, relative to the link cone integral int ds e^{-rho V_g(s)};
     the needle lemma says moments 0,1,2 vanish for ANY nu, so J_C/J_link -> 0 as rho -> inf (as in flat space).
"""
import numpy as np
R, W = 100.0, 10.0
gu, gwu = np.polynomial.legendre.leggauss(40)
gr, gwr = np.polynomial.legendre.leggauss(8)
gth = np.linspace(0, 2*np.pi, 17)[:-1]; wth = 2*np.pi/16
def build_nodes():
    pts = []; wts = []
    U = 0.5*(gu+1); WU = 0.5*gwu
    for u, wu in zip(U, WU):
        for (va, vb) in [(0.0, 1-u), (1-u, 1.0)]:
            V = va+(vb-va)*0.5*(gu+1); WV = (vb-va)*0.5*gwu
            for v, wv in zip(V, WV):
                r2 = min(u*v, (1-u)*(1-v)); rm = np.sqrt(max(r2, 0))
                if rm <= 0: continue
                rr = 0.5*rm*(gr+1); wr = 0.5*rm*gwr
                t = 0.5*(u+v); x = 0.5*(u-v)
                for r, w_r in zip(rr, wr):
                    for th in gth:
                        pts.append((t, x, r*np.cos(th), r*np.sin(th))); wts.append(0.5*wu*wv*w_r*r*wth)
    return np.array(pts), np.array(wts)
P, Wt = build_nodes()
def om2(X, A, c): return 1.0 + A*np.exp(-((X-c)**2).sum(-1)/W**2)
def Vg(s, A, c):
    tau = np.sqrt(s); E = np.sqrt(R*R+s); beta = R/E; gam = E/tau
    tp = P[:, 0]*tau; xp = P[:, 1]*tau
    X = np.column_stack([gam*(xp+beta*tp), P[:, 2]*tau, P[:, 3]*tau])
    return (Wt*om2(X, A, c)**2).sum()*tau**4
def pred(A, c, n=400001):
    t = np.linspace(0, 1, n); X = np.column_stack([R*t, 0*t, 0*t]); o2 = om2(X, A, c)
    O4w = np.trapezoid(6*t*(1-t)*o2**2, t); ox = np.sqrt(o2[-1]); oy = np.sqrt(o2[0])
    return ox*oy/np.sqrt(O4w)
weights = {"w=1 (G-L)": lambda m: 1+0*m, "w=rhoV": lambda m: m, "w=(rhoV)^2": lambda m: m*m,
           "w=1/(1+rhoV)": lambda m: 1/(1+m), "layer n=2 (m^2/2)": lambda m: m*m/2}
fC = lambda m: (1 - 9*m + 8*m**2 - (4/3)*m**3)
def cone(rho, A, c, ns=240):
    smax = np.sqrt(80*24/(np.pi*rho))
    x, wq = np.polynomial.legendre.leggauss(ns)
    s = 0.5*smax*(x+1); ws = 0.5*smax*wq
    m = np.array([rho*Vg(si, A, c) for si in s]); e = np.exp(-m); jac = ws/(2*np.sqrt(R*R+s))
    out = {k: (jac*f(m)*e).sum() for k, f in weights.items()}
    out["BD f_C"] = (jac*fC(m)*e).sum(); out["BD f_C * h(s)=1+s"] = (jac*fC(m)*e*(1+s)).sum()
    return out
if __name__ == "__main__":
    print("(b) ratio = [weighted link mean field, lensed] / [same weight, flat] x Omega_x Omega_y  (= link/GR); prediction = (nu Delta)^{-1/2}")
    flat = {rho: cone(rho, 0.0, np.array([50., 0, 0])) for rho in (1.0, 16.0, 256.0, 4096.0)}
    for A, c, lab in [(3.0, np.array([50., 0, 0]), "A=3 central"), (3.0, np.array([25., 0, 0]), "A=3 quarter")]:
        pr = pred(A, c); ox = np.sqrt(om2(np.array([R, 0, 0]), A, c)); oy = np.sqrt(om2(np.zeros(3), A, c))
        res = {rho: cone(rho, A, c) for rho in (1.0, 16.0, 256.0, 4096.0)}
        print(f"\n{lab}: predicted (nu Delta)^-1/2 = {pr:.4f}")
        for k in weights:
            print("   %-20s l=1,0.5,0.25,0.125: %s" % (k, " ".join("%.4f" % (res[r][k]/flat[r][k]*ox*oy) for r in res)))
        print("   (c-loc) local BD kernel: J_C/J_link (lensed) at l=1,0.5,0.25,0.125: %s" % " ".join("%+.2e" % (res[r]["BD f_C"]/res[r]["w=1 (G-L)"]) for r in res))
        print("           same with smooth h(s)=1+s:                          %s" % " ".join("%+.2e" % (res[r]["BD f_C * h(s)=1+s"]/res[r]["w=1 (G-L)"]) for r in res))
        print("           flat control J_C/J_link:                             %s" % " ".join("%+.2e" % (flat[r]["BD f_C"]/flat[r]["w=1 (G-L)"]) for r in flat))
