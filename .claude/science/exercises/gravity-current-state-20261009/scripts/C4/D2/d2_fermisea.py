"""D2 (b): impurity band coupled to a Fermi sea by a density vertex (onsite U, or
nearest-neighbour V: U_q = 2V cos q per axis).  Second order (one p-h bubble).
Gamma(k) = pi sum_{q,p} |U_q|^2 f(p)(1-f(p+q)) delta(eps(k) - eps(k-q) - [xi(p+q)-xi(p)]) / N^(2d)
(Gaussian-broadened delta, checked against eta and N); Z_RS(k) = 1/(1 + sum |U|^2 f(1-f)/den^2) and
Sigma_RS restricted to non-resonant terms, vs N.  1D and 2D, half-filled sea, impurity eps = TB."""
import numpy as np, sys, time
TWO_PI = 2*np.pi
def gauss(x, eta): return np.exp(-0.5*(x/eta)**2)/(np.sqrt(2*np.pi)*eta)

def gamma_1d(k, N, U, eta, mu=0.0, vertex='onsite', imp='TB'):
    g = TWO_PI*np.arange(N)/N
    xi = -2*np.cos(g) - mu
    occ = (xi < 0).astype(float)
    eps = lambda x: 1 - np.cos(x)
    q = g[:, None]; p = g[None, :]
    ip = np.arange(N)[None, :]; iq = np.arange(N)[:, None]
    ipq = (ip + iq) % N
    Om = xi[ipq] - xi[ip]
    wt = occ[ip]*(1 - occ[ipq])
    Uq2 = (np.full(N, U**2) if vertex == 'onsite' else (2*U*np.cos(g))**2)[:, None]
    den = eps(k) - eps(k - q) - Om
    G = np.pi*(Uq2*wt*gauss(den, eta)).sum()/N**2
    # RS on-shell with resonant terms excluded (|den| < 3 eta) -> Z proxy
    mask = (wt > 0) & (np.abs(den) > 1e-12)
    dsig = -(Uq2*wt*np.where(mask, 1/np.where(mask, den, 1)**2, 0)).sum()/N**2
    return G, 1/(1 - dsig)

def gamma_2d(kx, ky, N, U, eta, mu=0.0):
    g = TWO_PI*np.arange(N)/N
    GX, GY = np.meshgrid(g, g, indexing='ij')
    xi = (-2*np.cos(GX) - 2*np.cos(GY) - mu).ravel()
    occ = (xi < 0)
    idx = np.arange(N*N).reshape(N, N)
    eps = lambda x, y: 2 - np.cos(x) - np.cos(y)
    occ_idx = np.where(occ.ravel())[0]
    px = (occ_idx // N); py = occ_idx % N
    tot = 0.0
    for iqx in range(N):
        for iqy in range(N):
            j = ((px + iqx) % N)*N + (py + iqy) % N
            emp = ~occ[j]
            if not emp.any(): continue
            Om = xi[j[emp]] - xi[occ_idx[emp]]
            den = eps(kx, ky) - eps(kx - g[iqx], ky - g[iqy]) - Om
            tot += gauss(den, eta).sum()
    return np.pi*U**2*tot/N**4

if __name__ == '__main__':
    print("# 1D: impurity eps=1-cos k (v_max=1), sea xi=-2cos p (half filling, v_F=2), U=1")
    for vertex in ['onsite', 'nn']:
        for N in [512, 1024, 2048]:
            for eta in [0.02, 0.01]:
                row = []
                for k in [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]:
                    G, Z = gamma_1d(k, N, 1.0, eta, vertex=vertex)
                    row.append(f"k={k/np.pi:.2f}pi G={G:.4f} Zrs={Z:.4f}")
                print(f"{vertex} N={N} eta={eta} | " + " | ".join(row), flush=True)
    print("# 2D: impurity eps=2-cos kx-cos ky, sea xi=-2(cos px+cos py) half filling, U=1")
    for N, eta in [(32, 0.08), (48, 0.06), (64, 0.04)]:
        t = time.time()
        row = []
        for (kx, ky, lab) in [(np.pi, 0.0, 'face(pi,0)'), (np.pi, np.pi, 'corner(pi,pi)'), (np.pi/2, 0.0, '(pi/2,0)'), (np.pi/8, 0.0, '(pi/8,0)')]:
            row.append(f"{lab} G={gamma_2d(kx, ky, N, 1.0, eta):.4f}")
        print(f"2D N={N} eta={eta} | " + " | ".join(row) + f" | t={time.time()-t:.1f}s", flush=True)
