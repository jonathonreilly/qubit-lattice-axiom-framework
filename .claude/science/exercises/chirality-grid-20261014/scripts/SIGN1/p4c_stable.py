"""SIGN-1 P4c (stabilised UDV products; strong coupling). Based on p4_cluster_weights.py.
Original P4 doc: HS weights on a 4x1x1 torus cluster (walker + f_NN filter + X2 quartic on psi_S), 256 Majoranas.
(a) natural 10-channel decomposition (X^a = Re B^a, Y^a = Im B^a): weights expected complex.
(b) Kramers-class decomposition found by pair_kramers_u1c.py (saved solutions): weights expected real >= 0,
    checked in the d-frame (U(1)_c eigenspace) with Kramers pairing of the d-frame eigenvalues.
Weight^2 = det(1 + prod_l e^{-4 dt K0} e^{4 K_{V_l}})  (Majorana); d-frame weight = det(1+M_d)/sqrt(det M_d).
"""
import numpy as np, sys, time, resource
from scipy.linalg import expm
sys.path.insert(0, __file__.rsplit("/", 1)[0])
t0 = time.time()
from kramers_fams import *     # famo, channels(), O2 (T2 on one vertex), OU, G9, parity ...
def mem(): return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20
rng = np.random.default_rng(4242)

Lx = 4; nv = 32; nmodes = Lx * nv; NM = 2 * nmodes
# walker on the ring (only x hopping survives for Ly = Lz = 1)
Sx = np.roll(np.eye(Lx), 1, axis=0)            # (Sx psi)(x) = psi(x-1)
h = np.kron((Sx - Sx.T) / (2j), np.kron(X.astype(complex), np.eye(16)))
assert np.allclose(h, h.conj().T)
KW = density_K(h)                               # global ordering tau*128 + x*32 + m
# filter f_NN on (4,1,1): f(p) = (-1 - cos p)/2 -> f(0) = -1/2, f(+-1) = -1/4
fx = np.zeros((Lx, Lx))
for x in range(Lx):
    fx[x, x] = -0.5; fx[x, (x + 1) % Lx] += -0.25; fx[x, (x - 1) % Lx] += -0.25
fk = np.array([(-1 - np.cos(2 * np.pi * k / Lx)) / 2 for k in range(Lx)])
P(f"filter on ring: f(k) = {np.round(fk, 3).tolist()} (zero at k = pi: the hw1 corner (pi,0,0))")
def Fsmear(x):
    """64 x 256 real: vertex Majoranas gamma_S(x)_{tau,m} = sum_y f(x-y) gamma_{tau,(y,m)}."""
    F = np.zeros((64, NM))
    for t in range(2):
        for y in range(Lx):
            F[t * 32:(t + 1) * 32, t * nmodes + y * nv: t * nmodes + (y + 1) * nv] = fx[x, y] * np.eye(nv)
    return F
FS = [Fsmear(x) for x in range(Lx)]
# global symmetry matrices
O2g = antireal(np.kron(np.eye(Lx), np.kron(E, np.eye(16))).astype(complex))
OUg = realify(np.kron(np.eye(Lx), np.kron(np.eye(2), 1j * G9[8])))
for nm, A_ in (("walker", KW),):
    a = (-2j * A_); assert np.abs(a.imag).max() < 1e-12; a = a.real
    P(f"{nm}: T2-invariant {np.allclose(O2g.T @ a @ O2g, -a)}, commutes with U(1)_c {np.allclose(OUg.T @ a @ OUg, a)}")
P(f"filter commutes with T2 and U(1)_c: {all(np.allclose(FS[x] @ O2g, O2 @ FS[x]) and np.allclose(FS[x] @ OUg, OU @ FS[x]) for x in range(Lx))}")

Kb = vertex_B()
def Rvertex(l1):
    return (l1 / 2) * 4 * sum((-Kb[a].conj()) @ Kb[a] - Kb[a] @ (-Kb[a].conj()) for a in range(10))

from scipy.linalg import qr
def stable_logdet_1pM(Bs):
    """log det(1 + B_L ... B_1) with complex phase, via pivoted-QR UDV stabilisation (Loh et al.)."""
    n = Bs[0].shape[0]
    U = np.eye(n, dtype=complex); d = np.ones(n, complex); V = np.eye(n, dtype=complex); logdetV = 0.0 + 0j
    for B in Bs:
        Xm = (B @ U) * d[None, :]
        Q, R, piv = qr(Xm, pivoting=True)
        dn = np.diag(R).copy()
        Rn = R / dn[:, None]                       # unit-diagonal upper triangular
        Pm = np.zeros((n, n)); Pm[piv, np.arange(n)] = 1.0   # Xm[:, piv] = Q R  ->  Xm = Q R Pm^T
        V = Rn @ Pm.T @ V
        U, d = Q, dn
    # 1 + U D V = U Db (Db^-1 U^-1 V^-1 + Ds) V
    big = np.abs(d) > 1
    db = np.where(big, d, 1.0); ds = np.where(big, 1.0, d)
    Mid = (np.linalg.inv(V) @ U.conj().T).T  # placeholder (not used)
    inner = (1.0 / db)[:, None] * (U.conj().T @ np.linalg.inv(V)) + np.diag(ds)
    s1, l1 = np.linalg.slogdet(U); s2, l2 = np.linalg.slogdet(inner); s3, l3 = np.linalg.slogdet(V)
    logdb = np.sum(np.log(db.astype(complex)))
    return np.log(s1) + l1 + logdb + np.log(s2) + l2 + np.log(s3) + l3
def run(chans, l1, W, dt, Lt, ncfg, dframe, tag):
    K0 = KW + W * sum(FS[x].T @ Rvertex(l1) @ FS[x] for x in range(Lx))
    E0 = expm(-4 * dt * K0)
    coef = np.array([c for c, _ in chans]); amats = np.array([a for _, a in chans]); del chans
    kap = np.sqrt(2 * dt * W * np.abs(coef)) * np.where(coef < 0, 1.0, 1j)
    nz = np.abs(coef) > 1e-12; kap = kap[nz]; amats = amats[nz]
    if dframe:
        w_, V_ = np.linalg.eig(OUg); Pp = V_[:, np.abs(w_ - 1j) < 1e-8]; Pp, _ = np.linalg.qr(Pp)
    out = []
    for cfg in range(ncfg):
        Bs = []
        for l in range(Lt):
            KV = np.zeros((NM, NM), complex)
            for x in range(Lx):
                av = np.tensordot(kap * rng.normal(size=len(kap)), amats, axes=1)
                KV += FS[x].T @ ((0.5j) * av) @ FS[x]
            B = E0 @ expm(4 * KV)
            Bs.append(Pp.conj().T @ B @ Pp if dframe else B)
        L1 = stable_logdet_1pM(Bs)
        if dframe:
            ldM = sum(np.linalg.slogdet(B)[1] + np.log(np.linalg.slogdet(B)[0]) for B in Bs)
            logw = L1 - ldM / 2          # w = det(1+M_d) / sqrt(det M_d)
        else:
            logw = L1 / 2                # w = +- sqrt(det(1+M)) (phase mod pi)
        out.append(logw)
    return np.array(out)
def natural(l1, l2):
    ch = []
    for a in range(10):
        ch.append((l1 + 2 * l2, 2 * Kb[a].imag)); ch.append((l1 - 2 * l2, -2 * Kb[a].real))
    return ch
# validation of the stabiliser against the direct formula at weak coupling
sols = np.load("kramers_solutions.npy", allow_pickle=True).item()
for key in ("th200", "th250"):
    th = int(key[2:]); l1, l2 = np.cos(np.radians(th)), np.sin(np.radians(th))
    for W, dt, Lt in ((0.5, 0.05, 8), (2.0, 0.05, 20), (8.0, 0.05, 20)):
        lw = run(channels(sols[key]), l1, W, dt, Lt, 10, True, "K")
        ph = np.angle(np.exp(1j * lw.imag))
        P(f"  Kramers th={th} W={W} beta={dt*Lt}: phase of w (d-frame, stabilised): max |phase| = {np.abs(ph).max():.1e}; Re log w range {lw.real.min():.1f}..{lw.real.max():.1f}")
        lw = run(natural(l1, l2), l1, W, dt, Lt, 10, False, "N")
        ph = np.abs(np.angle(np.exp(2j * lw.imag)))   # phase of w^2 = det(1+M)
        P(f"  natural th={th} W={W}: |phase of det(1+M)| median {np.median(ph):.2e} max {ph.max():.2e}")
P(f"total {time.time() - t0:.0f}s, peak RSS {mem():.0f} MB")
