"""SIGN-1 P4: HS weights on a 4x1x1 torus cluster (walker + f_NN filter + X2 quartic on psi_S), 256 Majoranas.
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
def weights(chans, l1, W=0.5, dt=0.05, Lt=8, ncfg=40, dframe=False, tag=""):
    K0 = KW + W * sum(FS[x].T @ Rvertex(l1) @ FS[x] for x in range(Lx))
    a0 = (-2j * K0)
    P(f"  [{tag}] K0 Hermitian-type (a real): {np.abs(a0.imag).max() < 1e-12}; T2-invariant: {np.allclose(O2g.T @ a0.real @ O2g, -a0.real)}; "
      f"U(1)_c-commuting: {np.allclose(OUg.T @ a0.real @ OUg, a0.real)}")
    E0 = expm(-4 * dt * K0)
    coef = np.array([c for c, _ in chans]); amats = np.array([a for _, a in chans]); del chans
    kap = np.sqrt(2 * dt * W * np.abs(coef)) * np.where(coef < 0, 1.0, 1j)
    nz = np.abs(coef) > 1e-12; kap = kap[nz]; amats = amats[nz]
    if dframe:
        w_, V_ = np.linalg.eig(OUg); Pp = V_[:, np.abs(w_ - 1j) < 1e-8]
        Pp, _ = np.linalg.qr(Pp); assert Pp.shape[1] == nmodes
    out = []
    for cfg in range(ncfg):
        M = np.eye(NM, dtype=complex)
        for l in range(Lt):
            KV = np.zeros((NM, NM), complex)
            for x in range(Lx):
                phi = rng.normal(size=len(kap))
                av = np.tensordot(kap * phi, amats, axes=1)            # 64 x 64
                KV += FS[x].T @ ((0.5j) * av) @ FS[x]
            M = M @ E0 @ expm(4 * KV)
        sD, lD = np.linalg.slogdet(np.eye(NM) + M)
        rec = dict(D=sD, logD=lD)
        if dframe:
            Md = Pp.conj().T @ M @ Pp
            leak = np.abs(M @ Pp - Pp @ Md).max() / np.abs(M).max()
            swd, lwd = np.linalg.slogdet(np.eye(nmodes) + Md); sdM, ldM = np.linalg.slogdet(Md)
            ev = np.linalg.eigvals(Md)
            # Kramers pairing: the spectrum is closed under complex conjugation
            kram = max(np.min(np.abs(ev.conj() - e)) for e in ev) / np.abs(ev).max()
            # consistency: Majorana det(1+M) = det(1+M_d)^2 / det(M_d)  (phases and logs)
            cons_log = abs(2 * lwd - ldM - lD); cons_ph = abs(np.angle(swd ** 2 / sdM / sD))
            rec.update(wd=swd, dM=sdM, leak=leak, kram=kram, consist=max(cons_log / max(1, abs(lD)), cons_ph))
        out.append(rec)
    return out

P(f"\n=== (a) natural 10-channel decomposition ===")
def natural(l1, l2):
    ch = []
    for a in range(10):
        aX = 2 * Kb[a].imag; aY = -2 * Kb[a].real
        ch.append((l1 + 2 * l2, aX)); ch.append((l1 - 2 * l2, aY))
    return ch
summ = {}
for th in (45, 135, 200, 230, 250, 315):
    l1, l2 = np.cos(np.radians(th)), np.sin(np.radians(th))
    res = weights(natural(l1, l2), l1, tag=f"natural {th}")
    ph = np.array([np.angle(r["D"]) for r in res])
    frac = np.mean(np.abs(ph) > 1e-6)
    P(f"  theta={th:3d} (l1={l1:+.3f}, l2={l2:+.3f}): c_X = {l1 + 2 * l2:+.3f}, c_Y = {l1 - 2 * l2:+.3f}; "
      f"fraction of configs with det(1+M) not real-positive: {frac:.2f}; |arg det| median {np.median(np.abs(ph)):.2e}, max {np.abs(ph).max():.2e}")
    summ[f"natural{th}"] = frac

P(f"\n=== (b) Kramers-class decomposition (saved SDP solutions) ===")
sols = np.load("kramers_solutions.npy", allow_pickle=True).item()
for key in ("th200", "th230", "th270"):
    th = int(key[2:]); l1, l2 = np.cos(np.radians(th)), np.sin(np.radians(th))
    ch = channels(sols[key])
    bad = [c for c, a in ch if (c > 1e-12 and np.allclose(O2.T @ a @ O2, -a)) or (c < -1e-12 and np.allclose(O2.T @ a @ O2, a))]
    ucom = all(np.allclose(OU.T @ a @ OU, a) for c, a in ch)
    P(f"  theta={th}: {len(ch)} channels; sign/parity mismatches: {len(bad)}; all channels commute with U(1)_c: {ucom}")
    res = weights(ch, l1, dframe=True, tag=f"Kramers {th}"); del ch
    D = np.array([r["D"] for r in res]); wd = np.array([r["wd"] for r in res]); dM = np.array([r["dM"] for r in res])
    P(f"    Majorana det(1+M): max |arg| = {np.abs(np.angle(D)).max():.2e}; "
      f"d-frame: max leak {max(r['leak'] for r in res):.1e}, max Kramers mismatch {max(r['kram'] for r in res):.1e}, "
      f"max |Im w_d|/|w_d| = {np.max(np.abs(wd.imag) / np.abs(wd)):.1e}, min Re w_d/|w_d| = {np.min(wd.real / np.abs(wd)):+.6f}, "
      f"max |arg det M_d| = {np.abs(np.angle(dM)).max():.1e}, consistency w_d^2/detM_d vs det(1+M): {max(r['consist'] for r in res):.1e}")
    summ[key] = (np.min(wd.real / np.abs(wd)), np.abs(np.angle(D)).max())
P(f"\nSUMMARY {summ}")
P(f"total {time.time() - t0:.0f}s, peak RSS {mem():.0f} MB")
