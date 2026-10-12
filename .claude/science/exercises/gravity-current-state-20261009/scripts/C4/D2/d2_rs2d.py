"""D2 (a, 2D): second-order Rayleigh-Schroedinger dressed band of a 2D tight-binding
particle eps = 2 - cos kx - cos ky coupled to a 2D acoustic mode w = c|2 sin(q/2)| with
|M_q|^2 = g2 (w/c)^(2a).  RS keeps the correct threshold geometry (denominator
eps(k) - eps(k-q) - w(q) < 0, touching 0 only at q -> 0 for subsonic c).
k continuous along (pi - d, 0) [face centre] and (pi - d, pi - d) [corner]; q-grid N x N.
Diagnostics: C(d) = 2[E(face) - E(face - d)]/d^2 vs N at fixed d (N-stable => smooth),
local exponent of the dressing part, Z_RS = 1/(1 + sum |M|^2/den^2) at the face vs N."""
import numpy as np, sys, time
TWO_PI = 2*np.pi
def eps2(kx, ky): return 2 - np.cos(kx) - np.cos(ky)
def run(N, c, g2, a, path, deltas):
    q = TWO_PI*np.arange(N)/N
    QX, QY = np.meshgrid(q, q, indexing='ij'); QX = QX.ravel(); QY = QY.ravel()
    w = c*np.sqrt(4*np.sin(QX/2)**2 + 4*np.sin(QY/2)**2)
    nz = w > 1e-14
    QX, QY, w = QX[nz], QY[nz], w[nz]
    M2 = g2*(w/c)**(2*a)
    out = []
    for d in [0.0] + deltas:
        if path == 'face': kx, ky = np.pi - d, 0.0
        else: kx, ky = np.pi - d, np.pi - d
        den = eps2(kx, ky) - eps2(kx-QX, ky-QY) - w
        sig = (M2/den).sum()/N**2
        dsig = -(M2/den**2).sum()/N**2
        out.append((eps2(kx, ky) + sig, sig, 1/(1 - dsig), den.max()))
    Ef = out[0][0]
    C = [2*(Ef - out[i+1][0])/d**2 for i, d in enumerate(deltas)]
    # dressing part only: S(face) - S(face - d)
    Ds = [out[0][1] - out[i+1][1] for i in range(len(deltas))]
    pl = [np.log(abs(Ds[i+1]/Ds[i]))/np.log(deltas[i+1]/deltas[i]) if Ds[i] != 0 else np.nan for i in range(len(deltas)-1)]
    return Ef, out[0][1], out[0][2], C, Ds, pl, out[0][3]
if __name__ == '__main__':
    deltas = [0.01, 0.03, 0.1, 0.3]
    print("# 2D RS. C(d) at d=", deltas, "; Ds = Sigma(face)-Sigma(face-d); p = local exponents of Ds; Z at face; maxden<0 check")
    for path in ['face', 'corner']:
        for c in [2.0]:
            for a in [-0.5, 0.0, 0.5]:
                for N in [64, 128, 256, 512]:
                    t = time.time()
                    Ef, S, Z, C, Ds, pl, md = run(N, c, 0.3, a, path, deltas)
                    print(f"{path} c={c} a={a} g2=0.3 N={N} | E={Ef:.6f} Sig={S:.6f} Z={Z:.4f} maxden={md:.2e} | C=" + " ".join(f"{x:.5f}" for x in C)
                          + " | Ds=" + " ".join(f"{x:.3e}" for x in Ds) + " | p=" + " ".join(f"{x:.3f}" for x in pl) + f" | t={time.time()-t:.1f}", flush=True)
    # bare reference
    for path in ['face', 'corner']:
        d = 0.01
        if path == 'face': print(path, 'bare C(0.01)=', 2*(eps2(np.pi,0)-eps2(np.pi-d,0))/d**2)
        else: print(path, 'bare C(0.01)=', 2*(eps2(np.pi,np.pi)-eps2(np.pi-d,np.pi-d))/d**2)
