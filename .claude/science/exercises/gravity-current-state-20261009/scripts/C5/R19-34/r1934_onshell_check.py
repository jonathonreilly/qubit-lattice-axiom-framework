"""R19-34 (b, independent check): the on-shell rest energy shift dE(p=0) of a light Dirac fermion from the referee-confirmed
old-fashioned (Hamiltonian, Feynman-gauge) runner R13-7 r137 / R16-10 r1610_core.dirac_pt (vR13-7 item 1), generalised ONLY by
per-axis symbols S_j = s/l_j, W_j = W/l_j, d_j = d/l_j (H-cov).  The per-axis rewrite is checked against the unmodified dirac_pt at l = 1.
As m -> 0+, dE(0) -> the additive mass dm (chiral part ~ m log m -> 0).  Compares dm and d2 dm/dh2 with r1934_lib (Euclidean P = 0 formula)."""
import numpy as np, time
from r1934_lib import Grid, dm_mass, d1_law, photon, strain_l, hessian, naive_wilson
import r1610_core as core
t0 = time.time()

def dirac_rest_axes(Q, m, lam, Sf, Wf, df):
    """dirac_pt at p = 0 with per-axis callables Sf[j], Wf[j], df[j] (j = x, y, z). Q = (qx, qy, qz) arrays."""
    qx, qy, qz = Q
    dx2, dy2, dz2 = df[0](qx)**2, df[1](qy)**2, df[2](qz)**2
    Wq = np.sqrt(dx2 + dy2 + dz2 + lam**2)
    Ep = m; a = np.array([0.0, 0.0, 0.0, 1.0])            # W(0) = s(0) = 0
    Sy, Wy, Sz, Wz = Sf[1](-qy), Wf[1](-qy), Sf[2](-qz), Wf[2](-qz)
    dly = (0.0 - Sy, 0.0 - Wy); dlz = (0.0 - Sz, 0.0 - Wz)
    kx = -qx
    hk = [Sf[0](kx), Sy, Sz, m + Wf[0](kx) + Wy + Wz]
    Ek = np.sqrt(hk[0]**2 + hk[1]**2 + hk[2]**2 + hk[3]**2)
    b = [c/Ek for c in hk]
    ab = a[0]*b[0] + a[3]*b[3]
    dxa = 0.0 - Sf[0](kx); dxb = 0.0 - Wf[0](kx)
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
    tx = a[3]*(Wf[0](qx) + Wf[0](-qx)); ty = a[3]*(Wf[1](qy) + Wf[1](-qy)); tz = a[3]*(Wf[2](qz) + Wf[2](-qz))
    tad = 0.5*(tx/dx2 + ty/dy2 + tz/dz2)/(2*Wq)
    return acc + tad

def dE_rest(s, W, d, grid, l, m, lam):
    Sf = [lambda k, j=j: s(k)/l[j] for j in range(3)]
    Wf = [lambda k, j=j: W(k)/l[j] for j in range(3)]
    df = [lambda q, j=j: d(q)/l[j] for j in range(3)]
    x, w = grid.x, grid.w
    tot = 0.0
    for i0 in range(len(x)):
        Q = (np.full((len(x), len(x)), x[i0]), x[:, None] + 0*x[None, :], x[None, :] + 0*x[:, None])
        val = dirac_rest_axes(Q, m, lam, Sf, Wf, df)
        tot += float((w[i0]*w[:, None]*w[None, :]*val).sum())
    return tot

# (0) the per-axis rewrite equals the unmodified referee-confirmed dirac_pt at l = 1 (random points)
rng = np.random.default_rng(1)
s, W, L = d1_law(0.909103708, 0.555604226); d = photon('Gph', 2.9435)
q = rng.uniform(-np.pi, np.pi, (3, 2000))
ref = core.dirac_pt(q[0], q[1], q[2], 0.0, 0.05, 0.01, s, W, d)[0]
mine = dirac_rest_axes((q[0], q[1], q[2]), 0.05, 0.01, [s]*3, [W]*3, [d]*3)
print('(0) per-axis rewrite vs unmodified r1610_core.dirac_pt at l = 1, p = 0, m = 0.05: max |diff| = %.1e (scale %.1e)' % (np.max(np.abs(ref - mine)), np.max(np.abs(ref))))
# (1) on-shell dE(0; m, h) vs Euclidean dm(h) on the R18-9 root edge
g = Grid([0.909103708, np.pi - 0.909103708, 2.9435], 8, 0.25)
dm0 = dm_mass(s, W, d, g, strain_l(0.0))
f = lambda h: dm_mass(s, W, d, g, strain_l(h))
_, _, _, _, hE = hessian(f, 0.02)
print('(1) Euclidean P=0 formula, R18-9 root edge + Gph: dm = %+.9f  d2/dh2 Rich = %+.6e' % (dm0, hE))
for lam in (0.01,):
    for m in (1e-2, 3e-3, 1e-3):
        fo = lambda h: dE_rest(s, W, d, g, strain_l(h), m, lam)
        e0, e1, eh1, eh2, ehr = hessian(fo, 0.02)
        print('    on-shell dE(0): lam=%.0e m=%.0e: dE = %+.9f (diff to dm %+.2e)  d2/dh2 Rich = %+.6e (diff %+.2e)' % (lam, m, e0, e0 - dm0, ehr, ehr - hE), flush=True)
# (2) same for naive Wilson r = 1 (R19-31's case)
s1, W1, d1 = naive_wilson(1.0); g1 = Grid([], 8, 0.25)
dmw = dm_mass(s1, W1, d1, g1, strain_l(0.0)); _, _, _, _, hw = hessian(lambda h: dm_mass(s1, W1, d1, g1, strain_l(h)), 0.02)
for m in (1e-2, 1e-3):
    e0, _, _, _, ehr = hessian(lambda h: dE_rest(s1, W1, d1, g1, strain_l(h), m, 0.01), 0.02)
    print('(2) naive Wilson r=1: Euclidean dm %+.9f Hess %+.6e | on-shell m=%.0e: dE %+.9f Hess %+.6e' % (dmw, hw, m, e0, ehr), flush=True)
print('time %.0f s' % (time.time() - t0))
