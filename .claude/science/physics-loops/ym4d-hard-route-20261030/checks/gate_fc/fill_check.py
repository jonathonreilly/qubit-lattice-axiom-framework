#!/usr/bin/env python3
"""Gate check for library/fill-cubical-extension.md, item 8a.

Criteria, written before any run.
C1 constants: every displayed numeric inequality in Lemmas E, C and F2-mult
   holds, in exact or log2 arithmetic.  FAIL on any violation.
C2 geometry: for an odd L with blocks centred at sites, brick walls are at
   half-integers, and at least one bond with both ends in frozen bricks lies
   in no integer closed brick.  This is a test of the claim (FG) fails: PASS
   means the claim stands.
C3 Lemmas G, E, C on one 3-cell, SU(2), monopole-charged boundary data:
   (a) rebuilt boundary links equal the input to 1e-9;
   (b) every link in the gauge of Lemma G obeys the measured G;
   (c) max theta n^2 <= 2^14 [K + G + G^2], with G measured.
   FAIL on any violation.  n=8,12,16,24.
C4 Lemma H: d(1,Hol) <= sum theta on random rectangles.  FAIL on violation.

What this cannot show: the proved branch needs n >= 32 G(K), with G about
2^176, so no run reaches it.  C3 uses measured G, so it exercises the
mechanism and the exactness of the boundary links, not the theorem's range.
"""
import math, random, resource, sys
import numpy as np

LIMIT_GB = 2.0

def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**30  # darwin: bytes
    if rss > LIMIT_GB:
        sys.exit(f"stopped: RSS {rss:.2f} GB above limit")

# --- quaternions (w,x,y,z), arrays of shape (...,4)
def qmul(a, b):
    w1, x1, y1, z1 = np.moveaxis(a, -1, 0)
    w2, x2, y2, z2 = np.moveaxis(b, -1, 0)
    return np.stack([w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2,
                     w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2], -1)
def qinv(a):
    return a*np.array([1., -1., -1., -1.])
def qexp(v):  # v imaginary (...,3)
    t = np.linalg.norm(v, axis=-1, keepdims=True)
    s = np.where(t > 1e-14, np.sin(t)/np.where(t > 1e-14, t, 1), 1.0)
    return np.concatenate([np.cos(t), s*v], -1)
def qlog(q):
    v = q[..., 1:]
    s = np.linalg.norm(v, axis=-1, keepdims=True)
    t = np.arctan2(s, q[..., :1])
    f = np.where(s > 1e-14, t/np.where(s > 1e-14, s, 1), 1.0)
    return f*v
def dist1(q):  # spherical distance from 1
    return np.arctan2(np.linalg.norm(q[..., 1:], axis=-1), q[..., 0])

# --- C1
def log2_constants(K):
    """log2 of B,M,delta,H,G,E for K given as log2 value (or None for 0)."""
    lk = -math.inf if K is None else K
    add = lambda a, b: max(a, b) + math.log2(1 + 2**(min(a, b) - max(a, b))) if abs(a-b) < 900 else max(a, b)
    lB = 4 + add(0, lk)
    lM = 12 + add(0, lB)
    ld = -40 - 2*add(0, lM)
    lH = 16 + add(0, lM) - 2*ld
    lG = add(add(math.log2(100*math.pi) + add(0, lB), 2 + lk), lH)
    lE = 20 + add(add(0, lk), 2*lG)
    return lB, lM, ld, lH, lG, lE

def c1():
    ok = True
    def chk(name, cond):
        nonlocal ok
        print(f"  {'ok  ' if cond else 'FAIL'} {name}")
        ok = ok and cond
    chk("cover count 6(100x+1)^2 <= 2^16 x^2, x>=100", 6*(100*100+1)**2 <= 2**16*100**2)
    chk("ball volume 36 pi < 2^7", 36*math.pi < 128)
    chk("2^23 M^2 delta < 2^-17 given delta=2^-40(1+M)^-2", 23-40 <= -17)
    chk("cot(d/2) <= 2/d, d=1e-3", 1/math.tan(5e-4) <= 2/1e-3)
    chk("||DS|| <= 8/d^2, d=1", 1/(2*math.sin(.5)**2) <= 8)
    chk("||D pi|| <= 1+sqrt(4) over rho>=1/2 gives 6", (1+2)*2 == 6)
    chk("(1+sqrt d) <= 3, d=3", 1+math.sqrt(3) <= 3)
    y = 4/32
    chk("exp(4a)-1-4a <= 16 a^2, a=1/32", math.exp(y)-1-y <= 16/32**2)
    chk("(11): 96+432+8064 coefficients sum", 96 == 4*24 and 432 == 36*12 and 8064 == 36*12*16+2*24**2)
    chk("selected-cell count 24*4=96, volume 96*16=1536", 24*4 == 96 and 96*16 == 1536)
    K0 = 16*math.pi
    for t in (1, .5, 1e-3, 1e-9):
        n = math.ceil(math.sqrt(K0/t))
        chk(f"K0 <= t n^2 <= 4K0 at t={t}", K0 <= t*n*n <= 4*K0)
    lE0 = log2_constants(None)[5]
    lK2 = max(math.log2(4*K0), lE0)
    lK3 = log2_constants(lK2)[5]
    lC = log2_constants(lK3)[5]
    print(f"  log2 E(0)={lE0:.0f}, log2 K_3={lK3:.0f}, log2 C_*={lC:.0f}, log2 C_a={lC-math.log2(K0):.0f}")
    return ok

# --- C2
def c2():
    L, t0 = 3, 24   # L odd, t_0 a multiple of 8 L
    # blocks centred at multiples of L: sites |x-Lk|<=(L-1)/2, faces at half-integers
    def block(x): return (x + (L-1)//2)//L
    faces = sorted({x+.5 for x in range(-30, 30) if block(x) != block(x+1)})
    half = all(abs(f-math.floor(f)-.5) < 1e-12 for f in faces)
    # one-dim slice of two adjacent frozen bricks: walls at L/2 + t0 Z
    wall = L/2 + t0
    a = math.ceil(L/2)        # first site of brick 0
    b = math.floor(wall)      # last site of brick 0
    c = b+1                   # first site of brick 1
    d = math.floor(wall+t0)
    bond = (b, c)
    in0 = a <= b and c <= b
    in1 = c <= b
    print(f"  faces half-integer: {half}; brick sites [{a},{b}] and [{c},{d}]; bond {bond} in brick 0: {in0}, in brick 1: {in1}")
    return half and not (in0 or in1)

# --- C4
def c4(rng):
    ok = True
    for trial in range(40):
        a, b = rng.randint(1, 8), rng.randint(1, 8)
        eps = 10**rng.uniform(-3, 0.3)
        ux = qexp(np.array(np.random.default_rng(trial).normal(0, eps, (a+1, b+1, 3))))
        uy = qexp(np.array(np.random.default_rng(trial+999).normal(0, eps, (a+1, b+1, 3))))
        s = 0.0
        for i in range(a):
            for j in range(b):
                p = qmul(qmul(ux[i, j], uy[i+1, j]), qmul(qinv(ux[i, j+1]), qinv(uy[i, j])))
                s += float(dist1(p))
        h = np.array([1., 0, 0, 0])
        for i in range(a): h = qmul(h, ux[i, 0])
        for j in range(b): h = qmul(h, uy[a, j])
        for i in reversed(range(a)): h = qmul(h, qinv(ux[i, b]))
        for j in reversed(range(b)): h = qmul(h, qinv(uy[0, j]))
        ok = ok and float(dist1(h)) <= s + 1e-9
    return ok

# --- C3: one 3-cell Q=[0,n]^3, boundary links from a charge-1 hedgehog gauge field
def hedgehog_links(n, charge_scale=1.0):
    """Links U[mu][x,y,z] on all of the box: a smooth SU(2) field with a charged
    boundary.  Boundary data only are used.  Uses a non-singular SU(2) core, so
    the boundary is the transport of A = (1-f(r)) (x cross sigma)/r^2."""
    c = n/2
    core = n/4
    def Aat(p):
        d = p - c
        r2 = (d**2).sum(-1, keepdims=True)
        f = np.exp(-r2/core**2)
        # components A_mu in su(2): (A_mu)^a = eps_{mu a b} d_b (1-f)/ r^2 * (1/2 normal.)
        g = (1-f)/np.where(r2 > 1e-12, r2, 1)*charge_scale*0.5
        out = []
        for mu in range(3):
            e = np.zeros(3); e[mu] = 1
            out.append(np.cross(e, d)*g)
        return out
    U = []
    N = n+1
    grid = np.stack(np.meshgrid(*[np.arange(N)]*3, indexing='ij'), -1).astype(float)
    M = 8
    for mu in range(3):
        e = np.zeros(3); e[mu] = 1
        P = np.zeros(grid.shape[:3]+(4,)); P[..., 0] = 1
        for k in range(M):
            s = (k+.5)/M
            a = Aat(grid + s*e)[mu]/M
            P = qmul(P, qexp(a))
        U.append(P)
    return U

def plaq_angles(U, n, mask=None):
    res = []
    for mu in range(3):
        for nu in range(mu+1, 3):
            emu = [0, 0, 0]; emu[mu] = 1
            enu = [0, 0, 0]; enu[nu] = 1
            sl = [slice(0, n+1)]*3
            s0 = list(sl); s0[mu] = slice(0, n); s0[nu] = slice(0, n)
            s1 = list(s0); s1[mu] = slice(1, n+1)
            s2 = list(s0); s2[nu] = slice(1, n+1)
            p = qmul(qmul(U[mu][tuple(s0)], U[nu][tuple(s1)]),
                     qmul(qinv(U[mu][tuple(s2)]), qinv(U[nu][tuple(s0)])))
            res.append((mu, nu, dist1(p)))
    return res

def on_bdy(idx, n):
    return np.any((idx == 0) | (idx == n), axis=-1)

def lemma_g_3(U, n):
    """Tree gauge on bottom+walls (z=0 face and side walls), axis gauge on top,
    h extended over the top by the stereographic cone of Lemma E."""
    gD = np.zeros((n+1, n+1, n+1, 4)); gD[..., 0] = 1
    # U^g_xy = g(x) U g(y)^-1 ; tree path trivial => g(y) = g(x) U_xy
    for x in range(1, n+1):
        gD[x, 0, 0] = qmul(gD[x-1, 0, 0], U[0][x-1, 0, 0])
    for x in range(n+1):
        for y in range(1, n+1):
            gD[x, y, 0] = qmul(gD[x, y-1, 0], U[1][x, y-1, 0])
    for z in range(1, n+1):
        gD[:, :, z] = qmul(gD[:, :, z-1], U[2][:, :, z-1])
    # axis gauge on top face z=n
    gP = np.zeros((n+1, n+1, 4)); gP[..., 0] = 1
    for x in range(1, n+1):
        gP[x, 0] = qmul(gP[x-1, 0], U[0][x-1, 0, n])
    for x in range(n+1):
        for y in range(1, n+1):
            gP[x, y] = qmul(gP[x, y-1], U[1][x, y-1, n])
    h = qmul(gP, qinv(gD[:, :, n]))
    # equator values: boundary of top square
    bd = np.zeros((n+1, n+1), bool)
    bd[0, :] = bd[n, :] = bd[:, 0] = bd[:, n] = True
    pts = h[bd]
    # choose p far from the rim image (coarse search, as a stand-in for the volume argument)
    rs = np.random.default_rng(0)
    cand = rs.normal(size=(4000, 4)); cand /= np.linalg.norm(cand, axis=1, keepdims=True)
    dmin = np.arccos(np.clip(cand @ pts.T, -1, 1)).min(axis=1)
    p = cand[np.argmax(dmin)]
    delta = dmin.max()
    def S(q):
        c = (q*p).sum(-1, keepdims=True)
        return (q-c*p)/(1-c)
    def Sinv(w):
        w2 = (w**2).sum(-1, keepdims=True)
        return (2*w+(w2-1)*p)/(1+w2)
    w = S(h)
    # boundary-to-cone extension on the square, in rescaled coordinates
    X, Y = np.meshgrid(np.arange(n+1)/n, np.arange(n+1)/n, indexing='ij')
    dx, dy = X-.5, Y-.5
    rho = 2*np.maximum(np.abs(dx), np.abs(dy))
    safe = np.where(rho > 0, rho, 1)
    bx, by = .5+dx/safe, .5+dy/safe
    # bilinear lookup along the boundary polyline
    def wbd(ax, ay):
        fx, fy = ax*n, ay*n
        i0, j0 = np.floor(fx).astype(int).clip(0, n-1), np.floor(fy).astype(int).clip(0, n-1)
        tx, ty = (fx-i0)[..., None], (fy-j0)[..., None]
        return (1-tx)*(1-ty)*w[i0, j0]+tx*(1-ty)*w[i0+1, j0]+(1-tx)*ty*w[i0, j0+1]+tx*ty*w[i0+1, j0+1]
    v = rho[..., None]*wbd(bx, by)
    # exact trace on the rim
    v[bd] = w[bd]
    ht = Sinv(v)
    ht /= np.linalg.norm(ht, axis=-1, keepdims=True)
    gPn = qmul(qinv(ht), gP)  # h_tilde^-1 g_P equals g_D on the rim
    g = gD.copy()
    g[:, :, n] = gPn
    return g, delta

def gauged(U, g):
    out = []
    n = g.shape[0]-1
    for mu in range(3):
        s0 = [slice(0, n+1)]*3; s1 = [slice(0, n+1)]*3
        s0[mu] = slice(0, n); s1[mu] = slice(1, n+1)
        V = U[mu].copy()
        V[tuple(s0)] = qmul(qmul(g[tuple(s0)], U[mu][tuple(s0)]), qinv(g[tuple(s1)]))
        out.append(V)
    return out

def is_bdy_link(mu, n):
    I = np.stack(np.meshgrid(*[np.arange(n+1)]*3, indexing='ij'), -1)
    others = [i for i in range(3) if i != mu]
    m = np.zeros((n+1, n+1, n+1), bool)
    for o in others:
        m |= (I[..., o] == 0) | (I[..., o] == n)
    mm = np.zeros_like(m)
    s = [slice(0, n+1)]*3; s[mu] = slice(0, n)
    mm[tuple(s)] = m[tuple(s)]
    return mm

def boundary_edge_interp(a, n):
    """A on the unit cube boundary: returns function (face-sector) evaluator.
    a[mu] = imaginary log on boundary links."""
    def A_vec(q):  # q on boundary, in lattice units; returns n*(a_0,a_1,a_2) tangential, tensor interpolant
        out = np.zeros(q.shape[:-1]+(3, 3))
        face = np.argmax(np.abs(q-n/2), axis=-1)
        for mu in range(3):
            for nu_face in range(3):
                if nu_face == mu:
                    continue
                sel = face == nu_face
                if not sel.any():
                    continue
                r = q[sel]
                fv = np.round(r[:, nu_face]).astype(int)
                other = 3-mu-nu_face
                i_mu = np.floor(r[:, mu]).astype(int).clip(0, n-1)
                t_o = r[:, other]
                i_o = np.floor(t_o).astype(int).clip(0, n-1)
                lam = (t_o-i_o)[:, None]
                idx0 = [None]*3; idx1 = [None]*3
                idx0[mu] = i_mu; idx1[mu] = i_mu
                idx0[nu_face] = fv; idx1[nu_face] = fv
                idx0[other] = i_o; idx1[other] = i_o+1
                out[sel, mu] = n*((1-lam)*a[mu][tuple(idx0)]+lam*a[mu][tuple(idx1)])
        return out
    return A_vec

def lemma_c_3(U, n):
    g, delta = lemma_g_3(U, n)
    Ug = gauged(U, g)
    a, G = [], 0.0
    for mu in range(3):
        l = qlog(Ug[mu])
        a.append(l)
        G = max(G, float(np.linalg.norm(l[is_bdy_link(mu, n)], axis=-1).max())*n)
    A_vec = boundary_edge_interp(a, n)
    # transport of A_ext along every interior-touching link, in rescaled units
    c = n/2
    W = [None]*3
    M = 24
    for mu in range(3):
        I = np.stack(np.meshgrid(*[np.arange(n+1)]*3, indexing='ij'), -1).astype(float)
        P = np.zeros(I.shape[:3]+(4,)); P[..., 0] = 1
        e = np.zeros(3); e[mu] = 1
        for k in range(M):
            x = I+(k+.5)/M*e
            y = (x-c)/n                      # unit-cube coordinates about centre
            rho = 2*np.abs(y).max(-1)
            out = rho >= .5
            comp = np.zeros(x.shape)
            if out.any():
                ys = y[out]; r = rho[out][:, None]
                pi_ = ys/r                   # on |.|_inf=1/2
                psi = 2*r-1
                Av = A_vec((pi_+.5)*n)       # (...,3 spatial,3 colour), per unit rescaled length
                # D pi applied to direction e, in unit-cube coordinates
                s = np.argmax(np.abs(ys), axis=-1)
                sg = np.sign(ys[np.arange(len(s)), s])
                drho = np.zeros(ys.shape); drho[np.arange(len(s)), s] = 2*sg
                dpi = e[None, :]/r-ys*(drho[:, mu:mu+1])/r**2
                comp[out] = psi*np.einsum('ij,ijk->ik', dpi, Av)
            P = qmul(P, qexp(comp/M/n))
        W[mu] = P
    # keep exact boundary links, as (9) gives them in the limit of exact integration
    drift = 0.0
    for mu in range(3):
        bl = is_bdy_link(mu, n)
        drift = max(drift, float(dist1(qmul(W[mu][bl], qinv(Ug[mu][bl]))).max()))
        W[mu] = np.where(bl[..., None], Ug[mu], W[mu])
    Wback = gauged(W, qinv(g))
    return Wback, Ug, G, delta, drift

def c3():
    ok = True
    for n in (8, 12, 16, 24):
        guard()
        U = hedgehog_links(n)
        Kb = 0.0
        for mu, nu, th in plaq_angles(U, n):
            I = np.stack(np.meshgrid(*[np.arange(n+1)]*3, indexing='ij'), -1)
            s = [slice(0, n+1)]*3; s[mu] = slice(0, n); s[nu] = slice(0, n)
            J = I[tuple(s)]
            o = 3-mu-nu
            Kb = max(Kb, float(th[(J[..., o] == 0) | (J[..., o] == n)].max()))
        K = Kb*n*n
        W, Ug, G, delta, drift = lemma_c_3(U, n)
        ex = max(float(dist1(qmul(W[mu][is_bdy_link(mu, n)], qinv(U[mu][is_bdy_link(mu, n)]))).max()) for mu in range(3))
        tmax = max(float(th.max()) for _, _, th in plaq_angles(W, n))
        bound = 2**14*(K+G+G*G)
        a = ex < 1e-9
        c = tmax*n*n <= bound
        print(f"  n={n:3d} K={K:7.3f} G={G:8.3f} delta={delta:.3f} drift={drift:.1e} exact={ex:.1e} "
              f"max theta n^2={tmax*n*n:9.3f} ratio/boundary={tmax*n*n/K:7.2f} bound={bound:.3g} {'ok' if a and c else 'FAIL'}")
        ok = ok and a and c
    return ok

if __name__ == '__main__':
    rng = random.Random(7)
    res = {}
    print("C1 constants"); res['C1'] = c1()
    print("C2 geometry"); res['C2'] = c2()
    print("C3 Lemmas G,E,C on a 3-cell"); res['C3'] = c3()
    print("C4 Lemma H"); res['C4'] = c4(rng)
    for k, v in res.items():
        print(k, 'PASS' if v else 'FAIL')
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**30
    print(f"max RSS {rss:.3f} GB")
