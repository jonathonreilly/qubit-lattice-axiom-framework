#!/usr/bin/env python3
"""A24 S1 (supplied toy): exact energy bookkeeping of Lueders locks for one excitation on a tight-binding ring.

H = -J sum_x (|x><x+1| + h.c.), J = 1: band [-2, 2], band centre 0, band bottom -2.  hbar = a = 1, m* = 1/(2J).
Outcome-averaged energy change of an instrument with Hermitian Kraus operators A_k (sum_k A_k^2 = 1):
    dE = sum_k <A_k H A_k> - <H> = -1/2 sum_k <[A_k,[A_k,H]]>                            (L1)
Checks:
 (a) L1 for random H, random states, random projective partitions and random unsharp Lueders instruments
 (b) one-site binary lock at x: dE = -(energies of the bonds touching x)                   (L2)
 (c) full sharp instrument (record wherever the excitation is): dE = -<H> = depth below the band centre
 (d) position-diagonal unsharp Lueders instrument with likelihood w:  dE = sum_bonds (1 - B_b)(-<h_b>),
     B = sum_z sqrt(w(z) w(z-1)), the Bhattacharyya overlap of the record laws for the two ends of a bond  (L3)
     large width: 8 sigma^2 (1 - B) -> I_F sigma^2 >= 1 (Cramer-Rao; = 1 only for the Gaussian)            (L4)
 (e) fixed block partition (pixels of s sites): dE = -(energies of the bonds cut by block edges) ~ (1/s)(-<H>)
 (f) sparse (one-sublattice) support: dE = 0 for every position-diagonal lock, bond by bond
 (g) static trap bound state (on-site -V): one-site lock costs 2|c0|^2 (H00 - Eb) -> 4 J^2 / V
 (h) flat-band compact localized state (diamond chain, E = 0): one-site lock costs exactly 0
"""
import numpy as np

rng = np.random.default_rng(7)
J = 1.0


def herm(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (A + A.conj().T) / 2


def psd_sqrt(M):
    w, V = np.linalg.eigh(M)
    return (V * np.sqrt(np.clip(w, 0, None))) @ V.conj().T


def dE_kraus(psi, H, kraus):
    e0 = np.vdot(psi, H @ psi).real
    e1 = sum(np.vdot(K @ psi, H @ (K @ psi)).real for K in kraus)
    return e1 - e0


def dE_dc(psi, H, herm_kraus):
    tot = 0.0
    for A in herm_kraus:
        C = A @ H - H @ A
        D = A @ C - C @ A
        tot += np.vdot(psi, D @ psi).real
    return -0.5 * tot


print("(a) identity L1 on random instances (d = 12)")
worst = 0.0
for trial in range(200):
    d = 12
    H = herm(d)
    psi = rng.normal(size=d) + 1j * rng.normal(size=d); psi /= np.linalg.norm(psi)
    if trial % 2 == 0:       # projective partition in a random basis
        U, _ = np.linalg.qr(herm(d) + 3j * np.eye(d))
        cuts = np.sort(rng.choice(np.arange(1, d), size=2, replace=False))
        blocks = np.split(np.arange(d), cuts)
        As = [U[:, b] @ U[:, b].conj().T for b in blocks]
    else:                    # unsharp Lueders: E_k = S^-1/2 G_k S^-1/2, A_k = sqrt(E_k)
        G = []
        for k in range(3):
            X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
            G.append(X @ X.conj().T)
        Sm = np.linalg.inv(psd_sqrt(sum(G)))
        As = [psd_sqrt(Sm @ g @ Sm) for g in G]
    comp = np.abs(sum(A @ A for A in As) - np.eye(d)).max()
    worst = max(worst, abs(dE_kraus(psi, H, As) - dE_dc(psi, H, As)), comp)
print(f"   max |direct - double commutator| (incl. completeness) = {worst:.1e}")

# ---------------------------------------------------------------- ring and packet
L = 512
Hr = np.zeros((L, L))
for x in range(L):
    Hr[x, (x + 1) % L] = Hr[(x + 1) % L, x] = -J


def packet(k0, w0, x0=L // 2):
    x = np.arange(L)
    p = np.exp(-(x - x0) ** 2 / (4.0 * w0 ** 2) + 1j * k0 * x)
    return p / np.linalg.norm(p)


def bond_energy(psi):          # <h_{x,x+1}> = -2 J Re(psi_x^* psi_{x+1})
    return -2 * J * np.real(np.conj(psi) * np.roll(psi, -1))


print("\n(b) one-site binary lock at the packet centre; (c) full sharp instrument")
for k0 in (0.0, 0.3, 1.0, np.pi / 2, 2.5):
    psi = packet(k0, 24.0)
    x0 = L // 2
    P1 = np.zeros((L, L)); P1[x0, x0] = 1.0
    dEb = dE_kraus(psi, Hr, [P1, np.eye(L) - P1])
    hb = bond_energy(psi)
    pred_b = -(hb[x0 - 1] + hb[x0])
    E0 = np.vdot(psi, Hr @ psi).real
    dEc = -E0 + np.sum(np.abs(psi) ** 2 * np.diag(Hr))   # diag(H) = 0: after a full position dephasing <H> = 0
    print(f"   k0={k0:5.3f}: <H>={E0:+.5f} (-2cos k0 = {-2*np.cos(k0):+.5f}); binary lock dE={dEb:+.3e} "
          f"vs -(bond energies at x) {pred_b:+.3e}; full sharp dE = {dEc:+.5f} = depth below centre; "
          f"per record (dE/<n_x>) binary: {dEb/abs(psi[x0])**2:+.4f}")

print("\n(d) unsharp position-diagonal Lueders instruments: dE = (1 - B)(-<H>);  R = 8 sigma^2 (1 - B) -> I_F sigma^2 >= 1")


def shapes(sig):
    R = int(np.ceil(10 * sig)) + 2
    z = np.arange(-R, R + 1).astype(float)
    out = {}
    g = np.exp(-z ** 2 / (2 * sig ** 2)); out["gauss"] = g / g.sum()
    b = sig / np.sqrt(2); l = np.exp(-np.abs(z) / b); out["laplace"] = l / l.sum()
    a = sig * np.sqrt(6); t = np.clip(1 - np.abs(z) / a, 0, None); out["triangle"] = t / t.sum()
    s = int(round(np.sqrt(12 * sig ** 2 + 1))); u = ((z >= 0) & (z < s)).astype(float); out[f"uniform"] = u / u.sum()
    return z, out


for sig in (1.0, 2.0, 4.0, 8.0, 16.0, 32.0):
    z, sh = shapes(sig)
    row = []
    for name, w in sh.items():
        var = np.dot(w, z ** 2) - np.dot(w, z) ** 2
        B = np.sum(np.sqrt(w[1:] * w[:-1]))
        row.append(f"{name} R={8*var*(1-B):7.3f}")
    print(f"   sigma={sig:5.1f}: " + "  ".join(row))
# direct Kraus check of L3 on a small ring for one shape
Ls = 64
Hs = np.zeros((Ls, Ls))
for x in range(Ls):
    Hs[x, (x + 1) % Ls] = Hs[(x + 1) % Ls, x] = -J
xs = np.arange(Ls)
psi_s = np.exp(-(xs - 32) ** 2 / (4 * 6.0 ** 2) + 0.4j * xs); psi_s /= np.linalg.norm(psi_s)
sig = 2.5
kr = []
for y in range(Ls):
    d = (xs - y + Ls // 2) % Ls - Ls // 2
    wv = np.exp(-d ** 2 / (2 * sig ** 2))
    kr.append(wv)
kr = np.array(kr); kr /= kr.sum(0)[None, :]       # sum_y w_y(x) = 1 for every x
K = [np.diag(np.sqrt(kr[y])) for y in range(Ls)]
dEd = dE_kraus(psi_s, Hs, K)
zz = np.arange(-Ls // 2, Ls // 2)
wz = np.exp(-zz ** 2 / (2 * sig ** 2)); wz /= wz.sum()
B = np.sum(np.sqrt(wz * np.roll(wz, 1)))
E0s = np.vdot(psi_s, Hs @ psi_s).real
print(f"   direct Kraus sum (L=64, Gaussian sigma=2.5): dE={dEd:.6e}; (1-B)(-<H>)={(1-B)*(-E0s):.6e}; "
      f"continuum J cos k/(4 sigma^2) x e^(-1/(8w^2)) = {J*np.cos(0.4)*np.exp(-1/(8*36))/(4*sig**2):.6e}")
# Gaussian continuum law on the big ring: dE / (J cos k0 /(4 sigma^2))
psi = packet(0.3, 24.0); E0 = np.vdot(psi, Hr @ psi).real
for sig in (2.0, 8.0, 32.0):
    z = np.arange(-int(12 * sig), int(12 * sig) + 1)
    w = np.exp(-z ** 2 / (2 * sig ** 2)); w /= w.sum()
    B = np.sum(np.sqrt(w[1:] * w[:-1]))
    print(f"   Gaussian sigma={sig}: dE = {(1-B)*(-E0):.4e}; hbar^2/(8 m* sigma^2) x (-<H>/2J) = {(-E0/2)/(4*sig**2):.4e}")

print("\n(e) fixed block partitions (pixels of s sites), averaged over the partition offset")
psi = packet(0.3, 24.0); E0 = np.vdot(psi, Hr @ psi).real; hb = bond_energy(psi)
for s in (2, 4, 8, 16, 32, 64):
    vals = []
    for off in range(s):
        cut = [(x) for x in range(L) if (x - off + 1) % s == 0]   # bond (x, x+1) crosses a block edge
        vals.append(-np.sum(hb[cut]))
    # direct check for one offset with explicit projectors
    if s in (4, 32):
        dd = -np.vdot(psi, Hr @ psi).real
        for b0 in range(0, L, s):
            v = np.zeros(L, complex); v[b0:b0 + s] = psi[b0:b0 + s]     # P_b psi
            dd += np.vdot(v, Hr @ v).real
        cut0 = [x for x in range(L) if (x + 1) % s == 0]
        chk = f"; explicit projectors offset 0: {dd:.4e} vs -(cut bonds) {-np.sum(hb[cut0]):.4e}"
    else:
        chk = ""
    print(f"   s={s:3d}: mean dE = {np.mean(vals):.4e}; (1/s)(-<H>) = {-E0/s:.4e}; Gaussian with the same variance "
          f"(sigma^2=(s^2-1)/12): {(-E0/2)/(4*max((s*s-1)/12,1e-9)):.4e}{chk}")

print("\n(f) sparse (one-sublattice) support")
psi = np.zeros(L, complex); psi[0::2] = rng.normal(size=L // 2) + 1j * rng.normal(size=L // 2); psi /= np.linalg.norm(psi)
hb = bond_energy(psi)
P1 = np.zeros((L, L)); P1[10, 10] = 1.0
print(f"   max |bond energy| = {np.abs(hb).max():.1e}; binary lock dE = {dE_kraus(psi, Hr, [P1, np.eye(L)-P1]):.1e}; "
      f"<H> = {np.vdot(psi, Hr @ psi).real:.1e} (already at the band centre)")

print("\n(g) static trap bound state on an open chain (site 0 has on-site energy -V): one-site lock at the trap")
N = 401
for V in (0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 64.0):
    Hc = np.zeros((N, N))
    for x in range(N - 1):
        Hc[x, x + 1] = Hc[x + 1, x] = -J
    c = N // 2
    Hc[c, c] = -V
    ev, evec = np.linalg.eigh(Hc)
    b = evec[:, 0]; Eb = ev[0]
    P1 = np.zeros((N, N)); P1[c, c] = 1.0
    dEg = dE_kraus(b, Hc, [P1, np.eye(N) - P1])
    exact = 2 * V * (np.sqrt(V ** 2 + 4 * J ** 2) - V) / np.sqrt(V ** 2 + 4 * J ** 2)
    print(f"   V={V:6.2f}: Eb={Eb:+.5f} (exact {-np.sqrt(V**2+4*J**2):+.5f}); |c0|^2={abs(b[c])**2:.5f}; lock dE={dEg:.5e}; "
          f"2|c0|^2(H00-Eb)={2*abs(b[c])**2*(-V-Eb):.5e}; closed form {exact:.5e}; 4J^2/V={4*J**2/V:.4e}")

print("\n(h) diamond chain flat band (hubs h_j; top t_j, bottom b_j bonded to h_j and h_{j+1})")
M = 40
idx = lambda kind, j: 3 * (j % M) + {"h": 0, "t": 1, "b": 2}[kind]
Hd = np.zeros((3 * M, 3 * M))
for j in range(M):
    for kind in ("t", "b"):
        for hj in (j, j + 1):
            Hd[idx(kind, j), idx("h", hj)] = Hd[idx("h", hj), idx(kind, j)] = -J
ev = np.linalg.eigvalsh(Hd)
cls = np.zeros(3 * M); cls[idx("t", 5)] = 1 / np.sqrt(2); cls[idx("b", 5)] = -1 / np.sqrt(2)
P1 = np.zeros((3 * M, 3 * M)); P1[idx("t", 5), idx("t", 5)] = 1.0
print(f"   flat-band count at E=0: {np.sum(np.abs(ev) < 1e-10)} of {3*M}; |H cls| = {np.linalg.norm(Hd @ cls):.1e}; "
      f"one-site lock dE = {dE_kraus(cls, Hd, [P1, np.eye(3*M)-P1]):.1e}")
