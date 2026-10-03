"""A14 check N2: 2D ticked conveyor (Dirac-type) walk with random wall sites.

Supplied toy (nothing adopted). One tick:  U = S_Y . S_X . M(m)
  M(m)  = exp(-i m sigma_z)            (mass mixing, m = 0 for light-like)
  S_X   : sigma_x eigencomponents |+x>,|-x> move +1/-1 along x
  S_Y   : sigma_y eigencomponents |+y>,|-y> move +1/-1 along y
Clean dispersion: U(k) = exp(-i k_y s_y) exp(-i k_x s_x) exp(-i m s_z);
for m = 0, cos w = cos kx cos ky, i.e. w = |k| + O(k^3): an isotropic cone, speed 1.

Walls (records, A8 B1): a wall site carries no amplitude and does not relay.
A component whose move would enter a wall stays on its site and turns into the
opposite mover, times a reflection phase r (r = +-i is the full-swap brickwork
value e^{+-i theta} at theta = pi/2 for the two record contents).

Measurement: coherent (forward) amplitude g(t) = <chi_k| U_W^t |chi_k>, with
chi_k the upper-cone plane wave zeroed on walls.  g(t) e^{i w0 t} ~ Z e^{-i dw t - G t/2}.
dw(k) = shift of the effective quasi-energy, G(k) = extinction rate.
"""
import sys, time
import numpy as np

def step(psi, F, Wm, r):
    """One tick on psi[nk,2,L,L]; F = free mask (L,L) float, Wm = 1-F."""
    s2 = 1/np.sqrt(2)
    # ---- X substep: sigma_x eigenbasis
    ap = (psi[:, 0] + psi[:, 1]) * s2
    am = (psi[:, 0] - psi[:, 1]) * s2
    Wxm = np.roll(Wm, 1, axis=0)    # wall at s - e_x
    Wxp = np.roll(Wm, -1, axis=0)   # wall at s + e_x
    nap = F * (np.roll(ap, 1, axis=1) + r * Wxm * am)
    nam = F * (np.roll(am, -1, axis=1) + r * Wxp * ap)
    psi0 = (nap + nam) * s2
    psi1 = (nap - nam) * s2
    # ---- Y substep: sigma_y eigenbasis |+y>=(|0>+i|1>)/s2, |-y>=(|0>-i|1>)/s2
    bp = (psi0 - 1j * psi1) * s2
    bm = (psi0 + 1j * psi1) * s2
    Wym = np.roll(Wm, 1, axis=1)
    Wyp = np.roll(Wm, -1, axis=1)
    nbp = F * (np.roll(bp, 1, axis=2) + r * Wym * bm)
    nbm = F * (np.roll(bm, -1, axis=2) + r * Wyp * bp)
    out = np.empty_like(psi)
    out[:, 0] = (nbp + nbm) * s2
    out[:, 1] = 1j * (nbp - nbm) * s2
    return out

def mass(psi, m):
    if m == 0.0:
        return psi
    out = psi.copy()
    out[:, 0] *= np.exp(-1j * m)
    out[:, 1] *= np.exp(1j * m)
    return out

def Uk(kx, ky, m):
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
    ex = np.cos(kx) * np.eye(2) - 1j * np.sin(kx) * sx
    ey = np.cos(ky) * np.eye(2) - 1j * np.sin(ky) * sy
    em = np.cos(m) * np.eye(2) - 1j * np.sin(m) * sz
    return ey @ ex @ em

def upper(kx, ky, m):
    w, v = np.linalg.eig(Uk(kx, ky, m))
    om = -np.angle(w)
    i = int(np.argmax(om))
    return om[i], v[:, i]

def run(L, T, rho, r, m, seed, klist):
    rng = np.random.default_rng(seed)
    Wm = (rng.random((L, L)) < rho).astype(float)
    F = 1.0 - Wm
    xs = np.arange(L)
    nk = len(klist)
    psi = np.zeros((nk, 2, L, L), complex)
    om0 = np.zeros(nk)
    for j, (nx, ny) in enumerate(klist):
        kx, ky = 2*np.pi*nx/L, 2*np.pi*ny/L
        om0[j], v = upper(kx, ky, m)
        ph = np.exp(1j * (kx * xs[:, None] + ky * xs[None, :]))
        psi[j, 0] = v[0] * ph * F
        psi[j, 1] = v[1] * ph * F
        psi[j] /= np.sqrt(np.sum(np.abs(psi[j])**2))
    chi = psi.copy()
    g = np.zeros((nk, T + 1), complex)
    g[:, 0] = 1.0
    for t in range(1, T + 1):
        psi = step(mass(psi, m), F, Wm, r)
        g[:, t] = np.sum(np.conj(chi) * psi, axis=(1, 2, 3))
    nrm = np.sum(np.abs(psi)**2, axis=(1, 2, 3))
    return g, om0, nrm

def fit(g, om0, tmin, gmin=0.15):
    t = np.arange(len(g))
    h = g * np.exp(1j * om0 * t)
    ph = np.unwrap(np.angle(h))
    a = np.abs(h)
    sel = (t >= tmin) & (a > gmin)
    if sel.sum() < 8:
        return np.nan, np.nan
    dw = -np.polyfit(t[sel], ph[sel], 1)[0]
    G = -2 * np.polyfit(t[sel], np.log(a[sel]), 1)[0]
    return dw, G

if __name__ == "__main__":
    import signal; signal.alarm(58)
    L = int(sys.argv[1]); T = int(sys.argv[2]); r = complex(sys.argv[3]); m = float(sys.argv[4])
    nseed = int(sys.argv[5]); rhos = [float(x) for x in sys.argv[6].split(",")]
    klist = [(n, 0) for n in (2, 3, 4, 6, 8, 10)] + [(n, n) for n in (2, 3, 5, 7)]
    t0 = time.time()
    # clean check
    g, om0, nrm = run(L, 20, 0.0, r, m, 1, klist)
    tt = np.arange(21)
    err = np.max(np.abs(g - np.exp(-1j * om0[:, None] * tt[None, :])))
    print(f"L={L} T={T} r={r} m={m} seeds={nseed}; clean check max|g-e^-iwt| = {err:.2e}")
    for rho in rhos:
        res = []
        for s in range(nseed):
            g, om0, nrm = run(L, T, rho, r, m, 1000 + s, klist)
            res.append([fit(g[j], om0[j], 5) for j in range(len(klist))])
        res = np.array(res)  # seed, k, (dw,G)
        dw = np.nanmean(res[:, :, 0], axis=0); dws = np.nanstd(res[:, :, 0], axis=0) / np.sqrt(nseed)
        G = np.nanmean(res[:, :, 1], axis=0)
        print(f"rho={rho}: unitarity |1-norm| max {np.max(np.abs(nrm-1)):.1e}")
        print("   (nx,ny)   |k|     w0      dw/rho   +-     G/rho   n_ph-1=-dw/w0 (per rho)")
        for j, (nx, ny) in enumerate(klist):
            kk = 2*np.pi*np.hypot(nx, ny)/L
            print(f"   ({nx:2d},{ny:2d})  {kk:.4f}  {om0[j]:.4f}  {dw[j]/rho:+8.3f} {dws[j]/rho:6.3f}  {G[j]/rho:7.3f}   {-dw[j]/om0[j]/rho:+8.3f}")
    print(f"elapsed {time.time()-t0:.1f}s")
