"""r1: sign lemmas, own code.
(i) FHS orientation vs direct quadrature of Ch(P) = (i/2pi) int tr(P dP^dP) on an outward cube surface.
(ii) Lemma S: Ch(P_-) of H = dk^T v sigma on an outward surface = sign det v (also with tilt, and n=3 with a spectator band).
(iii) Lemma T: (1/24pi^2) int_{Sigma x [0,1]} tr(h^-1 dh)^3 = Ch(P), h = 1 + (e^{-2pi i t}-1) P, orientation (Sigma, t).
(iv) Step 2 factorisation exp(-itH_eps) = exp(-itH_reg) exp(-2pi i t P_<) at random points/times.
"""
import numpy as np
from scipy.linalg import expm, logm
import rlib as R

T = R.Tally()
rng = np.random.default_rng(2026)


def proj_lower(Hf, m):
    def P(K):
        H = Hf(K)
        w, V = np.linalg.eigh(H)
        Vm = V[..., :, :m]
        return Vm @ np.conj(np.swapaxes(Vm, -1, -2))
    return P


def face_grid(o, eu, ev, M):
    s = (np.arange(M) + 0.5) / M
    return o + s[:, None, None] * eu + s[None, :, None] * ev


def ch_direct(Pf, faces, M=60, h=1e-5):
    tot = 0.0
    for (o, eu, ev) in faces:
        K = face_grid(o, eu, ev, M).reshape(-1, 3)
        P = Pf(K)
        du = (Pf(K + h * eu) - Pf(K - h * eu)) / (2 * h)
        dv = (Pf(K + h * ev) - Pf(K - h * ev)) / (2 * h)
        dens = np.trace(P @ (du @ dv - dv @ du), axis1=-2, axis2=-1)
        tot += dens.sum() / M ** 2
    return (1j / (2 * np.pi) * tot)


def lemmaT(Pf, faces, M=40, Mt=40, h=1e-5):
    tot = 0.0
    for (o, eu, ev) in faces:
        K = face_grid(o, eu, ev, M).reshape(-1, 3)
        P = Pf(K)
        du = (Pf(K + h * eu) - Pf(K - h * eu)) / (2 * h)
        dv = (Pf(K + h * ev) - Pf(K - h * ev)) / (2 * h)
        n = P.shape[-1]
        for t in (np.arange(Mt) + 0.5) / Mt:
            z = np.exp(-2j * np.pi * t)
            hinv = np.eye(n) + (np.conj(z) - 1) * P
            th_u = hinv @ ((z - 1) * du)
            th_v = hinv @ ((z - 1) * dv)
            th_t = hinv @ (-2j * np.pi * z * P)
            dens = np.trace(th_u @ (th_v @ th_t - th_t @ th_v), axis1=-2, axis2=-1) * 3  # eps_abc tr(th_a th_b th_c)
            tot += dens.sum() / (M ** 2 * Mt)
    return tot / (24 * np.pi ** 2)


faces = R.cube_faces(np.zeros(3), 0.5)
for trial in range(4):
    v = rng.normal(size=(3, 3))
    if trial == 1:
        v[:, 0] *= -1 if np.linalg.det(v) > 0 else 1
    tilt = 0.4 * rng.normal(size=3)
    while np.linalg.norm(np.linalg.solve(v, tilt)) > 0.8: tilt *= 0.5
    Hf = lambda K, v=v, tilt=tilt: (np.einsum('ka,a->k', K, tilt)[:, None, None] * np.eye(2)
                                    + sum(np.einsum('ka,a->k', K, v[:, j])[:, None, None] * R.PAULI[j] for j in range(3)))
    Pf = proj_lower(Hf, 1)
    chi = int(np.sign(np.linalg.det(v)))
    cd = ch_direct(Pf, faces)
    # FHS via a unitary whose window (phi-2pi, 0) picks the lower band: U = exp(-i 0.3 H/|H|_max) near node
    Uf = lambda K, Hf=Hf: np.array([expm(-1j * 0.3 * Hk) for Hk in Hf(K)])
    cf, rk = R.chern_surface_faces(Uf, faces, 0.0, np.pi, 24)
    lt = lemmaT(Pf, faces)
    print(f'trial {trial}: |v^-1 t|={np.linalg.norm(np.linalg.solve(v, tilt)):.2f} det v={np.linalg.det(v):+.3f}  Ch_direct={cd.real:+.5f}{cd.imag:+.1e}i  Ch_FHS={cf:+.5f} rank={rk}  LemmaT={lt.real:+.5f}{lt.imag:+.1e}i')
    T.check(f'trial {trial}: direct Ch(P_-) = sign det v = {chi:+d} (Lemma S)', abs(cd - chi) < 2e-3)
    T.check(f'trial {trial}: FHS (my orientation) = direct Ch', abs(cf - chi) < 1e-6)
    T.check(f'trial {trial}: Lemma T integral = Ch(P)', abs(lt - chi) < 5e-3)

# n = 3: rank-2 projector, random linear-in-k 3x3 Hermitian with a constant splitting
for trial in range(2):
    A = [rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)) for _ in range(3)]
    A = [(a + a.conj().T) / 2 for a in A]
    D0 = np.diag([0.0, 0.0, 3.0]) if trial == 0 else np.diag([-3.0, 0.0, 0.0])
    m = 1 if trial == 0 else 2
    Hf = lambda K, A=A, D0=D0: D0 + sum(K[:, a, None, None] * A[a] for a in range(3))
    # restrict to a box small enough that the constant split band stays separated
    fc = R.cube_faces(np.zeros(3), 0.3)
    Pf = proj_lower(Hf, m)
    cd = ch_direct(Pf, fc)
    lt = lemmaT(Pf, fc)
    Uf = lambda K, Hf=Hf: np.array([expm(-1j * 0.5 * Hk) for Hk in Hf(K)])
    # window: lower m bands (m=1: below the touching pair's lower band... choose eps between bands via eigen sort)
    print(f'n=3 trial {trial} (rank {m}): Ch_direct={cd.real:+.5f}  LemmaT={lt.real:+.5f}')
    T.check(f'n=3 trial {trial}: Lemma T = Ch for a rank-{m} projector in C^3 (integer)', abs(lt - cd) < 5e-3 and abs(cd - round(cd.real)) < 5e-3)

# (iv) step-2 factorisation on random points: random U in U(3), eps, phi
ok = True
for _ in range(50):
    X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Uq, _ = np.linalg.qr(X)
    lam, V = np.linalg.eig(Uq)
    E = -np.angle(lam)
    eps = rng.uniform(-np.pi, np.pi)
    # choose phi in a gap of the spectrum within (eps, eps+2pi)
    Es = np.sort(np.mod(E - eps, 2 * np.pi))
    gaps = np.diff(np.concatenate([Es, [2 * np.pi + Es[0]]]))
    j = np.argmax(gaps)
    phi = eps + Es[j] + gaps[j] / 2
    if phi > eps + 2 * np.pi: phi -= 2 * np.pi
    Eeps = eps + np.mod(E - eps, 2 * np.pi)                 # (eps, eps+2pi)
    Ereg = phi - np.mod(phi - E, 2 * np.pi)                  # (phi-2pi, phi]
    Heps = V @ np.diag(Eeps) @ np.linalg.inv(V)
    Hreg = V @ np.diag(Ereg) @ np.linalg.inv(V)
    Pl = V @ np.diag((Ereg < eps).astype(float)) @ np.linalg.inv(V)
    for t in rng.uniform(0, 1, 3):
        G = expm(-1j * t * Heps)
        gh = expm(-1j * t * Hreg) @ expm(-2j * np.pi * t * Pl)
        ok &= np.abs(G - gh).max() < 1e-10
    ok &= np.abs(Heps - Hreg - 2 * np.pi * Pl).max() < 1e-10
    ok &= np.abs(expm(-1j * Hreg) - Uq).max() < 1e-10
T.check('step 2: H_eps = H_reg + 2pi P_< and exp(-itH_eps) = exp(-itH_reg) exp(-2pi i t P_<) (50 random U(3), 150 t)', ok)
T.total()
