"""t4: all band touchings in the middle gap and the pi gap; Chern number of the lower 4 bands
around K*; second-order (q^2) structure of the Strang-signed cone."""
import numpy as np
from scipy.optimize import minimize
from vcyc import layers_U, plain6, strang9

pi = np.pi
rng = np.random.default_rng(4)
Ks = np.array([pi, pi, pi])

def rel_phases(K, lay, signed, ref):
    U = layers_U(np.atleast_2d(K), lay, signed)
    ev = np.linalg.eigvals(U) * np.conj(ref)
    return np.sort(np.angle(ev), axis=-1)

def gaps(ph):
    # middle gap: between band 4 and 5 around 0 (relative phases sorted in (-pi,pi])
    # pi gap: between the top band and the bottom band (wrap)
    mid = ph[..., 4] - ph[..., 3]
    wrap = ph[..., 0] + 2 * pi - ph[..., 7]
    return mid, wrap

for th, name, lay, signed in [(pi / 4, "signed-6", plain6(pi / 4), True),
                              (pi / 4, "strang-9 signed", strang9(pi / 4), True),
                              (3 * pi / 8, "strang-9 signed", strang9(3 * pi / 8), True),
                              (pi / 8, "strang-9 signed", strang9(pi / 8), True)]:
    ref = np.exp(1j * np.angle(np.linalg.eigvals(layers_U(Ks[None], lay, signed)[0])[0]))
    N = 36
    g = (np.arange(N)) * 2 * pi / N - pi
    KK = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T
    ph = rel_phases(KK, lay, signed, ref)
    mid, wrap = gaps(ph)
    out = []
    for gapname, gap, col in [("mid", mid, 0), ("pi", wrap, 1)]:
        order = np.argsort(gap)[:400]
        reps = []
        for i in order:
            k = KK[i]
            if not any(np.linalg.norm(((k - KK[j]) + pi) % (2 * pi) - pi) < 0.45 for j in reps):
                reps.append(i)
            if len(reps) >= 14:
                break
        found = []
        for i in reps:
            f = lambda K: gaps(rel_phases(K, lay, signed, ref))[col][0]
            r = minimize(f, KK[i], method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-13, "maxiter": 1500})
            if r.fun < 1e-6:
                k = (r.x + pi) % (2 * pi) - pi
                if not any(np.linalg.norm(((k - q) + pi) % (2 * pi) - pi) < 1e-3 for q in found):
                    found.append(k)
        out.append((gapname, gap.min(), found))
    print(f"th={th:.4f} {name}:")
    for gapname, gmin, found in out:
        print(f"   {gapname}-gap: grid min {gmin:.2e}; distinct touchings found {len(found)}:",
              [tuple(np.round(k / pi, 4)) for k in found][:12])

# Chern number (FHS, determinant links) of the lower-4 group on a small cube around K*
def chern_cube(lay, signed, center, a=0.05, n=12):
    ref = np.exp(1j * np.angle(np.linalg.eigvals(layers_U(center[None], lay, signed)[0])[0]))
    def frame(K):
        U = layers_U(K[None], lay, signed)[0] * np.conj(ref)
        w, v = np.linalg.eig(U)
        ph = np.angle(w)
        idx = np.argsort(ph)[:4]
        Q, _ = np.linalg.qr(v[:, idx])
        return Q
    total = 0.0
    t = np.linspace(-a, a, n + 1)
    for axis in range(3):
        for sgn in (+1, -1):
            o = [i for i in range(3) if i != axis]
            F = np.empty((n + 1, n + 1), object)
            for i in range(n + 1):
                for j in range(n + 1):
                    K = center.copy(); K[axis] += sgn * a; K[o[0]] += t[i]; K[o[1]] += t[j]
                    F[i, j] = frame(K)
            flux = 0.0
            for i in range(n):
                for j in range(n):
                    l1 = np.linalg.det(F[i, j].conj().T @ F[i + 1, j])
                    l2 = np.linalg.det(F[i + 1, j].conj().T @ F[i + 1, j + 1])
                    l3 = np.linalg.det(F[i + 1, j + 1].conj().T @ F[i, j + 1])
                    l4 = np.linalg.det(F[i, j + 1].conj().T @ F[i, j])
                    flux += np.angle(l1 * l2 * l3 * l4)
            total += sgn * flux   # outward orientation (o0,o1,axis) right-handed up to sign; same rule all faces
    return total / (2 * pi)

for th in [pi / 4, 3 * pi / 8]:
    c = chern_cube(strang9(th), True, Ks.copy())
    print(f"Chern(lower-4) on cube around K*, strang-9 signed th={th:.4f}: {c:.4f}")

# second order: fit eigenphases at K*+d n, d small, Strang signed; look at q^2 split pattern
th = pi / 4
lay = strang9(th)
ref = np.exp(1j * np.angle(np.linalg.eigvals(layers_U(Ks[None], lay, True)[0])[0]))
for n in [np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.array([1., 1, 1]) / np.sqrt(3),
          np.array([1., -1, 1]) / np.sqrt(3), np.array([-1., -1, -1]) / np.sqrt(3)]:
    ds = np.array([0.004, 0.008])
    ph = np.array([rel_phases(Ks + d * n, lay, True, ref)[0] for d in ds])
    # model w = s d + a2 d^2 (+ a3 d^3); quadratic coefficient from two d's after removing linear
    a2 = (ph[1] / ds[1] - ph[0] / ds[0]) / (ds[1] - ds[0])
    print(f"n={np.round(n, 3)}: q^2 coefficients per band {np.round(a2, 4)}")
