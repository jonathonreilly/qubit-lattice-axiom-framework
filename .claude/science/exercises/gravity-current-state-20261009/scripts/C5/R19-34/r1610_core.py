"""R16-10 core: point-wise (q-resolved) one-loop on-shell integrands, re-implemented from the refereed runners
  scalar: R16-2 r162_scalar.Pi_onshell (referee-confirmed, vR16-2 item 2)
  Dirac : R13-7 r137_onshell.dE_onshell (referee-confirmed, vR13-7 item 1)
so that they can be evaluated on ANY point set (BZ grid with a smooth IR excision, or continuum R^3 in spherical
coordinates).  Photon momentum q is the loop variable; external p = (p,0,0); matter momentum k = p - q.
Per-point quantities are per e^2 and per unit measure d^3q/(2pi)^3 (the runners' BZ mean <.>_q = sum/N^3).

scalar: Pi_pt(p) = (u(p+qx)+u(p-qx)-2u(p))/(2 dx^2)/(2W) - [J0 + V^2 J1]     (p-independent seagulls dropped)
        c^2 - 1 = d Pi(iE_p,p)/d p^2 ;   dc = (c^2-1)/2 ; printed x16pi^2.
Dirac : dE_pt(p) = acc + tad exactly as r137 (Clifford closed forms), F(p) = 2 E_p dE, c^2 - 1 = dF/dp^2.
"""
import numpy as np

U = 16*np.pi**2

def scalar_pt(qx, qy, qz, p, m, lam, u, d):
    dx2, dy2, dz2 = d(qx)**2, d(qy)**2, d(qz)**2
    W = np.sqrt(dx2 + dy2 + dz2 + lam**2)
    up = float(u(np.array(p))); Ep = np.sqrt(m**2 + up)
    uy, uz = u(-qy), u(-qz)
    u0 = float(u(np.array(0.0)))
    kx = p - qx
    Ek = np.sqrt(m**2 + u(kx) + uy + uz)
    V2 = (up - u(kx))**2/dx2 + (u0 - uy)**2/dy2 + (u0 - uz)**2/dz2
    den = 2*W*Ek*(W + Ek - Ep)*(W + Ek + Ep)
    J1 = (W + Ek)/den
    J0 = (W**2*Ek + W*Ek**2 - W*Ep**2 - 4*Ek*Ep**2)/den
    sea = (u(p + qx) + u(p - qx) - 2*up)/(2*dx2)/(2*W)
    return sea - (J0 + V2*J1), sea, -(J0 + V2*J1), Ep

def dirac_pt(qx, qy, qz, p, m, lam, S, Wf, d):
    dx2, dy2, dz2 = d(qx)**2, d(qy)**2, d(qz)**2
    Wq = np.sqrt(dx2 + dy2 + dz2 + lam**2)
    Sp, Wp = float(S(np.array(p))), float(Wf(np.array(p)))
    W0 = float(Wf(np.array(0.0)))
    hp = np.array([Sp, 0.0, 0.0, m + Wp + 2*W0])
    Ep = np.sqrt(hp @ hp); a = hp/Ep
    Sy, Wy, Sz, Wz = S(-qy), Wf(-qy), S(-qz), Wf(-qz)
    dly = (0.0 - Sy, W0 - Wy); dlz = (0.0 - Sz, W0 - Wz)
    kx = p - qx
    hk = [S(kx), Sy, Sz, m + Wf(kx) + Wy + Wz]
    Ek = np.sqrt(hk[0]**2 + hk[1]**2 + hk[2]**2 + hk[3]**2)
    b = [c/Ek for c in hk]
    ab = a[0]*b[0] + a[3]*b[3]
    dxa = Sp - S(kx); dxb = Wp - Wf(kx)
    acc = 0.0
    for s in (+1, -1):
        d2 = dxa**2 + dxb**2
        db = dxa*b[0] + dxb*b[3]; da = dxa*a[0] + dxb*a[3]
        X = (d2 + s*(2*db*da - d2*ab))/(2*dx2)
        d2y = dly[0]**2 + dly[1]**2
        dby = dly[0]*b[1] + dly[1]*b[3]; day = dly[1]*a[3]
        X = X + (d2y + s*(2*dby*day - d2y*ab))/(2*dy2)
        d2z = dlz[0]**2 + dlz[1]**2
        dbz = dlz[0]*b[2] + dlz[1]*b[3]; daz = dlz[1]*a[3]
        X = X + (d2z + s*(2*dbz*daz - d2z*ab))/(2*dz2)
        X = X - (1 + s*ab)/2
        acc = acc + (-s*X/(2*Wq*(Wq + Ek - s*Ep)))
    tx = a[0]*(S(p + qx) + S(p - qx) - 2*Sp) + a[3]*(Wf(p + qx) + Wf(p - qx) - 2*Wp)
    ty = a[3]*(Wf(qy) + Wf(-qy) - 2*W0)
    tz = a[3]*(Wf(qz) + Wf(-qz) - 2*W0)
    tad = 0.5*(tx/dx2 + ty/dy2 + tz/dz2)/(2*Wq)
    return acc + tad, acc, tad, Ep

def rich(f0, f1, f2, h):
    D1 = (f1 - f0)/h**2; D2 = (f2 - f0)/(4*h**2)
    return (4*D1 - D2)/3

def speed_scalar(pts, wts, m, lam, u, d, h):
    """returns dc*16pi^2 (total, seagull part) for the weighted point set (weights include measure/(2pi)^3)."""
    vals = {}
    for p in (0.0, h, 2*h):
        tot, sea, ex, Ep = scalar_pt(*pts, p, m, lam, u, d)
        vals[p] = (np.sum(wts*tot), np.sum(wts*sea))
    c2 = rich(vals[0.0][0], vals[h][0], vals[2*h][0], h)
    cs = rich(vals[0.0][1], vals[h][1], vals[2*h][1], h)
    return c2/2*U, cs/2*U

def speed_dirac(pts, wts, m, lam, S, Wf, d, h):
    F = {}; T = {}
    for p in (0.0, h, 2*h):
        dE, acc, tad, Ep = dirac_pt(*pts, p, m, lam, S, Wf, d)
        F[p] = 2*Ep*np.sum(wts*dE); T[p] = 2*Ep*np.sum(wts*tad)
    return rich(F[0.0], F[h], F[2*h], h)/2*U, rich(T[0.0], T[h], T[2*h], h)/2*U

# ---------------------------------------------------------------- point sets
def bz_grid(N):
    q1 = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
    return q1

def sph_points(R, nr, nmu, nphi=1, rmin=0.0):
    """continuum R^3 points in spherical coords around the x axis (q_x = r mu); azimuth phi.
    Gauss-Legendre in r on log-spaced panels and in mu. weights include r^2 dr dmu dphi /(2pi)^3."""
    xg, wg = np.polynomial.legendre.leggauss(nr)
    edges = np.concatenate([[0.0], np.geomspace(1e-4, R, 60)])
    rs, wr = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        rs.append(0.5*(b - a)*xg + 0.5*(b + a)); wr.append(0.5*(b - a)*wg)
    rs = np.concatenate(rs); wr = np.concatenate(wr)
    mu, wmu = np.polynomial.legendre.leggauss(nmu)
    if nphi == 1:
        ph = np.array([np.pi/4]); wph = np.array([2*np.pi])
    else:
        ph = (np.arange(nphi) + 0.5)*2*np.pi/nphi; wph = np.full(nphi, 2*np.pi/nphi)
    Rr, MU, PH = np.meshgrid(rs, mu, ph, indexing='ij')
    Wt = (wr[:, None, None]*wmu[None, :, None]*wph[None, None, :])*Rr**2/(2*np.pi)**3
    st = np.sqrt(1 - MU**2)
    qx, qy, qz = Rr*MU, Rr*st*np.cos(PH), Rr*st*np.sin(PH)
    return (qx.ravel(), qy.ravel(), qz.ravel()), Wt.ravel(), Rr.ravel()

def chi(r, r0, r1):
    """smooth radial cutoff: 1 for r <= r0, 0 for r >= r1 (C-infinity)."""
    from_sublum = None
    x = np.clip((r - r0)/(r1 - r0), 0, 1)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1 - x, 1)), 0.0)
    return 1 - e1/(e1 + e2)
