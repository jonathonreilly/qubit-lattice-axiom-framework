"""D2 (a, 1D): second-order RS dressed band, continuous k near the face, q-grid N up to 2^20.
Subsonic c (denominators < 0).  C(d) = 2[E(pi)-E(pi-d)]/d^2 vs N (N-stable => smooth face),
local exponent of the dressing part Ds(d) = Sigma(pi) - Sigma(pi-d), Z_RS(pi) and Z_RS(0) vs N."""
import numpy as np, time
TWO_PI = 2*np.pi
bands = {'TB': lambda k: 1 - np.cos(k), 'KG': lambda k: np.sqrt(0.25 + 4*np.sin(k/2)**2)}
ds = [1e-3, 1e-2, 0.1, 0.3]
print("# 1D RS. d =", ds, "; C = 2[E(pi)-E(pi-d)]/d^2 ; Ds = Sigma(pi)-Sigma(pi-d); p = local exponents of Ds")
for band, c in [('TB', 1.5), ('KG', 1.0)]:
    eps = bands[band]
    for a in [0.0, 0.25, 0.5, 1.0]:
        for N in [2**12, 2**16, 2**20]:
            q = TWO_PI*np.arange(1, N)/N
            w = 2*c*np.abs(np.sin(q/2)); M2 = 0.3*(2*np.abs(np.sin(q/2)))**(2*a)
            res = []
            for k in [np.pi] + [np.pi - d for d in ds] + [0.0]:
                den = eps(k) - eps(k - q) - w
                res.append((eps(k) + (M2/den).sum()/N, (M2/den).sum()/N, 1/(1 + (M2/den**2).sum()/N), den.max()))
            Ef = res[0][0]
            C = [2*(Ef - res[i+1][0])/d**2 for i, d in enumerate(ds)]
            Ds = [res[0][1] - res[i+1][1] for i in range(len(ds))]
            pl = [np.log(abs(Ds[i+1]/Ds[i]))/np.log(ds[i+1]/ds[i]) for i in range(len(ds)-1)]
            print(f"{band} c={c} a={a} g2=0.3 N=2^{int(np.log2(N))} | Sig(pi)={res[0][1]:.5f} Z(pi)={res[0][2]:.4f} Z(0)={res[-1][2]:.4f} maxden={max(r[3] for r in res):.1e} | C="
                  + " ".join(f"{x:.5f}" for x in C) + " | p(Ds)=" + " ".join(f"{x:.3f}" for x in pl), flush=True)
    print(band, 'bare C(1e-3) =', 2*(eps(np.pi) - eps(np.pi - 1e-3))/1e-6)
