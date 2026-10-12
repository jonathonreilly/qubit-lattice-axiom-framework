"""RL1 (F2): locate all zeros of S(z) = ftilde_C(z) - 1 in Re z > 0 (|Im z| <= 40) for BD (L=4) and the RL1_F stable member,
by grid-seeded Newton plus argument-principle counts on sub-boxes. A zero with Re z > 0 is a growing mode of the retarded mean inverse."""
import numpy as np
from scipy.special import kv, gammaln
xg, wg = np.polynomial.legendre.leggauss(1200)
TAU = 5.0*(xg+1); WT = 5.0*wg; M = np.pi*TAU**4/24
def fker(C): return np.exp(-M)*sum(C[n]*M**n/np.exp(gammaln(n+1)) for n in range(len(C)))
def make_S(C):
    F = fker(C)
    f0 = None
    def ft(z):
        z = np.asarray(z, complex); x = z[..., None]*TAU
        return 4*np.pi*np.sum(WT*TAU**3*F*kv(1, x)/x, axis=-1)
    return lambda z: ft(z) - 1.0
cases = {"BD L=4": np.array([1., -9., 16., -8.]),
         "stable L=6": np.array([0.933243, -9.952513, 30.471668, -51.297132, 47.611945, -17.767211])}
for name, C in cases.items():
    S = make_S(C)
    # re-normalise C so that S(0+) = 0 exactly (printed coefficients are rounded)
    s0 = S(np.array([1e-3]))[0].real + 1.0; C = C/s0; S = make_S(C)
    print(f"\n{name}: C = {np.array2string(C, precision=6)}  (S(1e-3) = {S(np.array([1e-3]))[0].real:+.2e})")
    def cnt(x0, x1, y0, y1, n=8000):
        pth = np.concatenate([x0+1j*np.linspace(y0, y1, n), np.linspace(x0, x1, n)+1j*y1,
                              x1+1j*np.linspace(y1, y0, n), np.linspace(x1, x0, n)+1j*y0])
        ph = np.unwrap(np.angle(S(pth))); return -(ph[-1]-ph[0])/(2*np.pi)
    for box in [(0.002, 20, 0.5, 40), (0.002, 20, -40, -0.5), (0.002, 0.5, -0.5, 0.5), (0.5, 20, -0.5, 0.5)]:
        print("   zeros in Re[%g,%g] x Im[%g,%g]: %+.3f" % (box[0], box[1], box[2], box[3], cnt(*box)))
    xr = np.concatenate([np.linspace(0.002, 0.1, 50), np.linspace(0.1, 6, 120)]); yi = np.linspace(-40, 40, 1601)
    Z = xr[None, :] + 1j*yi[:, None]; V = np.abs(S(Z))
    roots = []
    idx = np.argsort(V.ravel())[:400]
    for k in idx:
        z = Z.ravel()[k]
        for it in range(80):
            h = 1e-7; d = (S(np.array([z+h]))[0]-S(np.array([z-h]))[0])/(2*h); dz = -S(np.array([z]))[0]/d; z = z+dz
            if abs(dz) < 1e-13: break
        if abs(S(np.array([z]))[0]) < 1e-10 and z.real > 1e-6 and abs(z.imag) <= 41 and not any(abs(z-r) < 1e-6 for r in roots):
            roots.append(z)
    for r in sorted(roots, key=lambda r: (-r.real, r.imag)):
        print("   zero z = %+.6f %+.6fi   growth e-fold length 1/Re z = %.1f ell" % (r.real, r.imag, 1/r.real))
