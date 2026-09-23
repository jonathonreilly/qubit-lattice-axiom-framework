"""O(3) bilayer (block 90's relabelled doubled graph): heat bath + overrelaxation, field eps along z.
Measures m_z, <P_b> (in-slab bonds, x and y transverse averaged), R^(k) = (beta/2N)<|F(k)|^2>, F = sum over both slabs of s^x e^{-ik.x}
(x and y components averaged), the current twist stiffness rho_s = <P_b> - (beta/2N)<J^2> (rotation about a transverse axis), and the
ratio R^E (P_b + eps m/E)/m^2 per |k| shell."""
import numpy as np, sys, time
def run(L, beta, eps, sweeps, therm, seed, n_or=2):
    rng = np.random.default_rng(seed)
    s = np.zeros((2, L, L, L, 3)); s[..., 2] = 1.0
    a = np.arange(2)[:, None, None, None]; x = np.arange(L)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    col = (a + X[None] + Y[None] + Z[None]) % 2
    masks = [col == c for c in (0, 1)]
    ez = np.array([0., 0., 1.])
    def field(s):
        h = s[::-1].copy()                      # rung partner
        for ax in (1, 2, 3):
            h += np.roll(s, 1, axis=ax) + np.roll(s, -1, axis=ax)
        return h + eps * ez
    def heat(s, m):
        V = beta * field(s)[m]
        kap = np.linalg.norm(V, axis=1); uu = V / kap[:, None]
        U = rng.random(len(kap)); ph = 2 * np.pi * rng.random(len(kap))
        w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kap)) / kap, -1.0, 1.0)
        aa = np.where((np.abs(uu[:, 0]) < 0.9)[:, None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
        b1 = aa - (aa * uu).sum(1)[:, None] * uu; b1 /= np.linalg.norm(b1, axis=1)[:, None]
        b2 = np.cross(uu, b1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
        s[m] = w[:, None] * uu + r[:, None] * (np.cos(ph)[:, None] * b1 + np.sin(ph)[:, None] * b2)
    def over(s, m):
        hh = field(s)[m]; hn = hh / np.linalg.norm(hh, axis=1)[:, None]
        v = s[m]; s[m] = 2 * (v * hn).sum(1)[:, None] * hn - v
    k = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    E = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    N = L ** 3
    Fk2 = np.zeros((L, L, L)); FG = np.zeros((L, L, L), complex); G2 = np.zeros((L, L, L)); mz = []; pb = []; J2 = []; cnt = 0
    for t in range(sweeps):
        for m in masks: heat(s, m)
        for _ in range(n_or):
            for m in masks: over(s, m)
        if t < therm: continue
        mz.append(s[..., 2].mean())
        p = 0.0; j2 = 0.0
        for ax in (1, 2, 3):
            nb = np.roll(s, -1, axis=ax)
            p += np.mean(s[..., 0] * nb[..., 0] + s[..., 2] * nb[..., 2]) + np.mean(s[..., 1] * nb[..., 1] + s[..., 2] * nb[..., 2])
            jy = np.sum(s[..., 2] * nb[..., 0] - s[..., 0] * nb[..., 2])      # rotation about y, bonds along ax
            jx = np.sum(s[..., 2] * nb[..., 1] - s[..., 1] * nb[..., 2])      # rotation about x
            j2 += jy * jy + jx * jx
        pb.append(p / 6); J2.append(j2 / 6)
        Hl = field(s)                            # full local field (neighbours + eps z)
        for c, sg in ((0, 1.0), (1, 1.0)):
            Fk = np.fft.fftn(s[0, ..., c] + s[1, ..., c])
            Fk2 += np.abs(Fk) ** 2
            ell = s[..., 2] * Hl[..., c] - s[..., c] * Hl[..., 2]     # L_u H for the rotation taking s^c to s^z
            Gk = np.conj(np.fft.fftn(ell[0] + ell[1]))               # G(k) = sum_u e^{ik.x_u} L_u H
            FG += Fk * Gk; G2 += np.abs(Gk) ** 2
        cnt += 1
    mzv, pbv = np.mean(mz), np.mean(pb)
    Rk = beta / (2 * N) * Fk2 / (2 * cnt)
    rho_s = pbv - beta / (2 * N) * np.mean(J2)
    kk = np.sqrt(np.minimum(np.abs(kx), 2*np.pi-np.abs(kx))**2 + np.minimum(np.abs(ky), 2*np.pi-np.abs(ky))**2 + np.minimum(np.abs(kz), 2*np.pi-np.abs(kz))**2)
    rows = []
    for lo, hi in ((0.0, 0.5), (0.5, 1.0), (1.0, 1.5), (1.5, 2.2), (2.2, 3.2), (3.2, 6.0)):
        sel = (kk > 1e-9) & (kk >= lo) & (kk < hi)
        if sel.sum():
            ratio = Rk[sel] * E[sel] * (pbv + eps * mzv / E[sel]) / mzv ** 2
            rhok = mzv ** 2 / (Rk[sel] * E[sel]) - eps * mzv / E[sel]
            rows.append((lo, hi, int(sel.sum()), float(ratio.mean()), float(rhok.mean()), float((Rk[sel] * E[sel]).mean())))
    # smallest k: rho(k_min)
    selmin = np.isclose(E, 2 - 2 * np.cos(2 * np.pi / L)) & (kk > 1e-9)
    rho_kmin = float(np.mean(mzv ** 2 / (Rk[selmin] * E[selmin]) - eps * mzv / E[selmin]))
    nz = kk > 1e-9
    w1 = float(np.mean((-beta * FG[nz] / (2 * cnt) / (2 * N * mzv)).real))                       # Ward: -beta<F G>/<M_z> = 1
    w2 = float(np.mean(beta * G2[nz] / (2 * cnt) / (2 * N * E[nz] * pbv + eps * 2 * N * mzv)))     # <|G|^2> = (2N E <P_b> + eps <M_z>)/beta
    return dict(mz=mzv, pb=pbv, rho_s=rho_s, rho_kmin=rho_kmin, rows=rows, cnt=cnt, w1=w1, w2=w2)
if __name__ == '__main__':
    L, beta, eps, sweeps, therm, seed = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    t0 = time.time(); r = run(L, beta, eps, sweeps, therm, seed)
    print(f"L={L} beta={beta} eps={eps} sweeps={sweeps} m_z={r['mz']:.5f} P_b={r['pb']:.5f} rho_s={r['rho_s']:.5f} rho(kmin)={r['rho_kmin']:.5f} "
          f"beta^2(P_b-rho_s)={beta**2*(r['pb']-r['rho_s']):.4f} Ward {r['w1']:.4f} {r['w2']:.4f} time={time.time()-t0:.0f}s")
    for lo, hi, n, ratio, rhok, re in r['rows']:
        print(f"   [{lo},{hi}) n={n}: RE={re:.4f} ratio={ratio:.4f} rho(k)={rhok:.5f} beta^2(P_b-rho(k))={beta**2*(r['pb']-rhok):.4f}")
