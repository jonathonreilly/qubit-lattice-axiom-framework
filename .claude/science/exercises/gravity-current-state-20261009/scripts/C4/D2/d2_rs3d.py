"""D2 (extra): 3D second-order RS, eps = 3 - sum cos k_i, w = c|2 sin(q/2)|, |M|^2 = g2 (w/c)^(2a),
a = -1/2 is the QED-like marginal power (d + 2a = 2).  k = (pi - d, 0, 0) [face centre].
C(d) vs N, Z_RS(face) vs N, local exponent of the dressing part."""
import numpy as np, time
TWO_PI = 2*np.pi
def eps3(kx, ky, kz): return 3 - np.cos(kx) - np.cos(ky) - np.cos(kz)
ds = [0.01, 0.03, 0.1, 0.3]
print("# 3D RS, c=2 (subsonic: v_max=sqrt3), g2=0.3; d =", ds)
for a in [-0.5, 0.0, 0.5]:
    for N in [24, 48, 96]:
        t = time.time()
        q = TWO_PI*np.arange(N)/N
        QX, QY, QZ = [x.ravel() for x in np.meshgrid(q, q, q, indexing='ij')]
        w = 2.0*np.sqrt(4*np.sin(QX/2)**2 + 4*np.sin(QY/2)**2 + 4*np.sin(QZ/2)**2)
        nz = w > 1e-14; QX, QY, QZ, w = QX[nz], QY[nz], QZ[nz], w[nz]
        M2 = 0.3*(w/2.0)**(2*a)
        res = []
        for d in [0.0] + ds:
            kx = np.pi - d
            den = eps3(kx, 0, 0) - eps3(kx - QX, -QY, -QZ) - w
            res.append((eps3(kx, 0, 0) + (M2/den).sum()/N**3, (M2/den).sum()/N**3, 1/(1 + (M2/den**2).sum()/N**3), den.max()))
        Ef = res[0][0]
        C = [2*(Ef - res[i+1][0])/d**2 for i, d in enumerate(ds)]
        Ds = [res[0][1] - res[i+1][1] for i in range(len(ds))]
        pl = [np.log(abs(Ds[i+1]/Ds[i]))/np.log(ds[i+1]/ds[i]) for i in range(len(ds)-1)]
        print(f"a={a} N={N} | Sig={res[0][1]:.5f} Z={res[0][2]:.4f} maxden={max(r[3] for r in res):.1e} | C=" + " ".join(f"{x:.5f}" for x in C)
              + " | p(Ds)=" + " ".join(f"{x:.3f}" for x in pl) + f" | t={time.time()-t:.0f}s", flush=True)
print("bare C(0.01) =", 2*(eps3(np.pi, 0, 0) - eps3(np.pi - 0.01, 0, 0))/1e-4)
