"""R19-5: size of the both-soft-corner contribution to the photon rows at the R18-9/R18-13 root photon.
The exact photon completion (report section 3.4) replaces the VWa-geo pair kernel by the continuum Maxwell kernel
(P = 1, u = 1, c = 1) on the corner U_r = {|k1|_inf < r and |k2|_inf < r}. For Xi only the O(q^2) data matter,
so 'continuum' = VWa-geo with a = -1/8 (lambda = 1/4 + 2a = 0) and w_d = w_o = 0 there.
Row change = Xi_r(continuum) - Xi_r(root data), Xi_r = U_r-restricted alpha + beta (same Richardson as vwface.xi_geo).
Uses R18-13's archived vwface.vertex_geo unmodified; the masked pair sum is written here."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch18_13')); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import kgrid, crossmat, photonGw

def pair_W_mask(law, N, shift, e, settings, rs):
    k = kgrid(N); s = law.sig(k); c = law.c(k)
    j = np.arange(N); j2 = [(shift[d] - j - 1) % N for d in range(3)]
    Y, Z = np.meshgrid(j, j, indexing='ij')
    W = [np.empty((N, N, N)) for _ in settings]; Ea = np.empty((N, N, N)); Mk = {r: np.empty((N, N, N), bool) for r in rs}
    for ix in range(N):
        X_ = np.full_like(Y, ix); I1 = [X_, Y, Z]; I2 = [j2[0][X_], j2[1][Y], j2[2][Z]]
        s1 = np.stack([s[I] for I in I1], -1); s2 = np.stack([s[I] for I in I2], -1)
        c1 = np.stack([c[I] for I in I1], -1); c2 = np.stack([c[I] for I in I2], -1)
        k1 = np.stack([k[I] for I in I1], -1); k2 = np.stack([k[I] for I in I2], -1)
        ssum = k1 + k2
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2)
        X1 = crossmat(s1); X2 = crossmat(s2)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        for t, (a, wd, wo) in enumerate(settings):
            ME, MB = V.vertex_geo(e, c1, c2, ssum, a, wd, wo)
            Bp = np.einsum('...ji,...jk,...kl->...il', X1, MB, X2)/rw[..., None, None]
            Nm = 0.5*(rw[..., None, None]*ME + Bp)
            W[t][ix] = np.einsum('...ij,...jk,...kl,...il->...', P1, Nm, P2, Nm)
        Ea[ix] = w1 + w2
        for r in rs:
            Mk[r][ix] = (np.abs(k1).max(-1) < r) & (np.abs(k2).max(-1) < r)
    return W, Ea, Mk

def xi_rows(law, N, row, settings, rs, shifts=(1, 2)):
    e = V.POL[row]; d = np.array(V.DIRS[row])
    W0, E0, M0 = pair_W_mask(law, N, (0, 0, 0), e, settings, rs)
    Dd = {n: pair_W_mask(law, N, tuple(n*d), e, settings, rs) for n in shifts}
    q1 = 2*np.pi*shifts[0]*np.sqrt(float(d @ d))/N; rr = shifts[1]/shifts[0]
    out = {}
    for key in [None] + list(rs):
        m0 = np.ones_like(E0, bool) if key is None else M0[key]
        res = []
        for t in range(len(settings)):
            beta = -np.sum(W0[t]*m0/E0**3)/E0.size; Pi0 = -np.sum(W0[t]*m0/E0)/E0.size
            Dn = {}
            for n in shifts:
                Wn, En, Mn = Dd[n]; mn = np.ones_like(En, bool) if key is None else Mn[key]
                Dn[n] = -np.sum(Wn[t]*mn/En)/En.size - Pi0
            alpha = (rr**4*Dn[shifts[0]] - Dn[shifts[1]])/((rr**4 - rr**2)*q1**2)
            res.append(alpha + beta)
        out[key] = np.array(res)
    return out

if __name__ == '__main__':
    t0 = time.time(); N = int(sys.argv[1]) if len(sys.argv) > 1 else 96
    law = photonGw(2.9435, np.pi - 2.9435)           # R18-9 / R18-13 root photon edge
    a_r, wd_r, wo_r = -0.176095005436, -1.171554, -0.195418   # vR18-9 retuned a; R18-13 N=224 (w_d, w_o)
    settings = ((a_r, 0.0, 0.0), (a_r, wd_r, wo_r), (-0.125, 0.0, 0.0))
    rs = (0.2, 0.4, 0.8)
    print(f'N = {N}; settings: root a only, root a + own-direction, continuum (lambda = 0); corner U_r with r in {rs}')
    for row in ('T2g', 'Eg', 'face1', 'face2'):
        o = xi_rows(law, N, row, settings, rs)
        full = o[None]
        line = f'{row:6s} full: root {full[0]:+.5e}  root+w {full[1]:+.5e}  cont {full[2]:+.5e}'
        for r in rs:
            x = o[r]; line += f' | r={r}: corner(root+w) {x[1]:+.2e}, change to cont {x[2]-x[1]:+.2e}'
        print(line, flush=True)
    print(f'time {time.time()-t0:.0f} s')
