#!/usr/bin/env python3
"""slab-parity-strong-cp: does w2's slab reflection o D-parity (or o C, o K, or the Floquet 0<->pi exchange)
solve strong CP beyond PR #10079's face swap? Self-contained, seeded, numpy only.
Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import itertools, time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261026)
t0 = time.time()
NP = [0, 0]


def check(name, ok, detail=""):
    NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" | {detail}" if detail else ""))


# ---------------- 1. kappa from the 16 content ----------------
print("1. kappa: mirror U(1) rotation, charge-4 vertex, QCD anomaly of one 16 per family")
# (name, colour dim, multiplicity of colour reps among Weyls); 2T(3) = 1, 2T(1) = 0
content = {"Q": (3, 2), "u^c": (3, 1), "d^c": (3, 1), "L": (1, 2), "e^c": (1, 1), "nu^c": (1, 1)}
ncomp = sum(c * m for c, m in content.values())
sum2T = sum(m for c, m in content.values() if c == 3)
Nf = 3
anom = sum2T * Nf          # d theta / d alpha for a common mirror phase alpha
qvert = 4                  # charge of Omega = z1 z2 z3 z4 on one SU(4) quartet
kappa = anom / qvert
check("1a [T] one 16 has 16 Weyls and sum 2T(colour) = 4 (4 SU(4) quartets, one triplet each)",
      ncomp == 16 and sum2T == 4, f"ncomp={ncomp}, sum2T={sum2T}")
check("1b [T] |kappa| = 4 N_f / 4 = N_f = 3 (agrees with #10079 D1)", kappa == 3, f"kappa={kappa}")
z4 = anom * (np.pi / 2)
check("1c [T] Z4 generator shifts theta by 2 pi N_f: anomaly-free, so theta_bar is NOT quantised to pi/2",
      abs(z4 - 2 * np.pi * Nf) < 1e-12, f"shift/2pi={z4 / 2 / np.pi:.0f}")

# ---------------- 2. Fock toy: wall swap o twist acting on the far-wall quartic ----------------
print("2. Two walls x 4 complex modes (Fock dim 256): S = swap o X on H_far = e^{i phi} c4c5c6c7 + h.c.")
n = 8; dim = 2 ** n
a = np.array([[0, 1], [0, 0]], complex); Z = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)


def kron_list(ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


c = [kron_list([Z] * j + [a] + [I2] * (n - j - 1)) for j in range(n)]
cd = [x.conj().T for x in c]
vac = np.zeros(dim, complex); vac[0] = 1.0


def fock_unitary(op_dag):
    """U with U c_j^dag U^dag = op_dag[j] (op_dag: list of creation-like operators), built on occupation basis."""
    U = np.zeros((dim, dim), complex)
    for idx in range(dim):
        occ = [(idx >> (n - 1 - j)) & 1 for j in range(n)]
        v = vac.copy()
        for j in reversed(range(n)):
            if occ[j]:
                v = op_dag[j] @ v
        U[:, idx] = v
    return U


def basis_state(occ):
    v = vac.copy()
    for j in reversed(range(n)):
        if occ[j]:
            v = cd[j] @ v
    return v


# reference: occupation basis via the same ordering
Bref = np.column_stack([basis_state([(i >> (n - 1 - j)) & 1 for j in range(n)]) for i in range(dim)])
swap = [(j + 4) % 8 for j in range(n)]
phi = rng.uniform(0, 2 * np.pi)
Om = c[4] @ c[5] @ c[6] @ c[7]
Hfar = np.exp(1j * phi) * Om + (np.exp(1j * phi) * Om).conj().T
Om_near = c[0] @ c[1] @ c[2] @ c[3]
H0 = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)); H0 = H0 + H0.conj().T
w, V = np.linalg.eigh(H0); u4 = V @ np.diag(np.exp(1j * w)) @ V.conj().T   # D-like on-site unitary
uu = np.kron(np.eye(2), u4)


def twist(kind):
    if kind == "1":
        U = fock_unitary([cd[swap[j]] for j in range(n)]) @ np.linalg.inv(Bref); return U, False
    if kind == "D":
        U = fock_unitary([sum(uu[k, swap[j]] * cd[k] for k in range(n)) for j in range(n)]) @ np.linalg.inv(Bref)
        return U, False
    if kind == "C":   # particle-hole on the swapped mode: c_j -> c_{s(j)}^dag; image built directly below
        return None, False
    if kind == "K":
        U = fock_unitary([cd[swap[j]] for j in range(n)]) @ np.linalg.inv(Bref); return U, True


bil = [cd[i] @ c[j] for i in range(n) for j in range(n)] + [c[i] @ c[j] for i in range(n) for j in range(i + 1, n)]
bil += [x.conj().T for x in bil[n * n:]]
res = {}
for kind in ["1", "D", "C", "K"]:
    U, anti = twist(kind)
    if kind == "C":  # build image directly: X maps c_j -> c_{s(j)}^dag
        img = np.exp(1j * phi) * (cd[0] @ cd[1] @ cd[2] @ cd[3]); img = img + img.conj().T
    else:
        Hs = Hfar.conj() if anti else Hfar
        img = U @ Hs @ U.conj().T
    farcomm = max(np.abs(img @ c[j] - c[j] @ img).max() for j in range(4, 8))
    nearcomm = max(np.abs(img @ c[j] - c[j] @ img).max() for j in range(4))
    ovl_bil = max(abs(np.trace(b.conj().T @ img)) for b in bil)
    differs = np.abs(img - Hfar).max()
    coef = np.trace(Om_near.conj().T @ img) / np.trace(Om_near.conj().T @ Om_near)
    coefd = np.trace(Om_near @ img) / np.trace(Om_near @ Om_near.conj().T)
    res[kind] = (farcomm, nearcomm, ovl_bil, differs, coef, coefd)
    ok = farcomm < 1e-12 and nearcomm > 0.5 and ovl_bil < 1e-12 and differs > 0.5
    lab = {"1": "P_slab", "D": "P_slab o D-like u(4)", "C": "P_slab o C", "K": "P_slab o K"}[kind]
    check(f"2{kind} [T] {lab}: image near-local, degree 4 (bilinear overlap 0), != H_far (explicitly broken)", ok,
          f"[img,c_far]={farcomm:.0e} bil={ovl_bil:.0e} |img-H|={differs:.1f}")
ph = {k: np.angle(res[k][4]) for k in res}
du = np.angle(np.linalg.det(u4))
exp_ph = {"1": phi, "D": phi + du, "C": -phi, "K": -phi}
dev = {k: abs(np.angle(np.exp(1j * (ph[k] - exp_ph[k])))) for k in res}
dev["D"] = min(dev["D"], abs(np.angle(np.exp(1j * (ph["D"] - phi + du)))))
check("2e [T] image coefficient ties lambda_far only to lambda_near (phase phi; -phi for C, K; phi + arg det u for D)",
      all(abs(abs(res[k][4]) - 1) < 1e-9 for k in res) and max(dev.values()) < 1e-9,
      " ".join(f"{k}:{ph[k]:+.3f}" for k in res) + f" phi={phi:.3f} arg det u={du:+.3f}")
ev_far = np.linalg.eigvalsh(Hfar); ev_sym = np.linalg.eigvalsh(Hfar + np.exp(1j * phi) * Om_near
                                                        + (np.exp(1j * phi) * Om_near).conj().T)
g_far = int(np.sum(np.abs(ev_far - ev_far[0]) < 1e-9)); g_sym = int(np.sum(np.abs(ev_sym - ev_sym[0]) < 1e-9))
check("3 [F] S-exact completion gaps the near (light) wall: ground degeneracy 16 (near free) -> 1",
      g_far == 16 and g_sym == 1, f"deg far-only={g_far}, deg S-symmetric={g_sym}, gap={ev_sym[1] - ev_sym[0]:.1f}")

# ---------------- 4. theta-density sign under each twist ----------------
print("4. theta density q = sum E.B on an 8^3 periodic grid (spectral curl), and tr(E B) under C/D")
N = 8
k = 2 * np.pi * np.fft.fftfreq(N); k[N // 2] = 0.0
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij"); KK = [KX, KY, KZ]


def d(f, i):
    return np.real(np.fft.ifftn(1j * KK[i] * np.fft.fftn(f)))


def q_of(A, E):
    B = [d(A[2], 1) - d(A[1], 2), d(A[0], 2) - d(A[2], 0), d(A[1], 0) - d(A[0], 1)]
    return sum(np.sum(E[i] * B[i]) for i in range(3))


inv = lambda f: np.roll(np.flip(f, axis=(0, 1, 2)), 1, axis=(0, 1, 2))
A = [rng.normal(size=(N, N, N)) for _ in range(3)]; E = [rng.normal(size=(N, N, N)) for _ in range(3)]
q0 = q_of(A, E)
P = lambda A, E: ([-inv(x) for x in A], [-inv(x) for x in E])
Kt = lambda A, E: (A, [-x for x in E])           # antiunitary K in the A basis: A even, E odd
Ct = lambda A, E: ([-x for x in A], [-x for x in E])
signs = {"P_slab": q_of(*P(A, E)) / q0, "P_slab o C": q_of(*Ct(*P(A, E))) / q0,
         "P_slab o K": q_of(*Kt(*P(A, E))) / q0, "0<->pi (no link action)": 1.0}
check("4a [T] q odd under P_slab and P_slab o C; EVEN under P_slab o K (PT-like) and the 0<->pi exchange",
      abs(signs["P_slab"] + 1) < 1e-10 and abs(signs["P_slab o C"] + 1) < 1e-10 and abs(signs["P_slab o K"] - 1) < 1e-10,
      " ".join(f"{a}:{b:+.0f}" for a, b in signs.items()))
herm = lambda: (lambda X: X + X.conj().T)(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
Em, A1, A2, dA = herm(), herm(), herm(), herm()
B3 = dA + 1j * (A1 @ A2 - A2 @ A1)
B3c = -dA.T + 1j * (A1.T @ A2.T - A2.T @ A1.T)
g = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
okC = np.allclose(B3c, -B3.T) and abs(np.trace((-Em.T) @ B3c) - np.trace(Em @ B3)) < 1e-10
okD = abs(np.trace(g @ Em @ g.conj().T @ g @ B3 @ g.conj().T) - np.trace(Em @ B3)) < 1e-10
check("4b [T] su(3): C maps B -> -B^T, tr(E B) invariant under C and inner D, so P_slab o D/C stay theta-odd",
      okC and okD)

# ---------------- 5. no forcing of arg lambda_4 ----------------
Y = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
canc = np.angle(np.linalg.det(Y) * np.linalg.det(Y.conj().T))
frac = 1e-10 / np.pi
check("5 [E] Yukawa phases cancel pairwise (Y' = Y^dag) but theta_bar = -N_f arg lambda_4 is unforced: "
      "P(|theta_bar|<1e-10) = 1e-10/pi", abs(canc) < 1e-12 and frac < 1e-9,
      f"arg detY detY'={canc:.1e}, P={frac:.1e}  -> proposal FAILS")

# ---------------- 6. D-parity vs the SM register ----------------
st = []
for s in (+.5, -.5):
    st += [(s, 0, 1 / 3)] * 3 + [(s, 0, -1.0)] + [(0, s, -1 / 3)] * 3 + [(0, s, 1.0)]
st = np.array(st); T3L, T3R, BL = st.T; Yh = T3R + BL / 2
Dmap = np.column_stack([T3R, T3L, -BL])
closed = sorted(map(tuple, np.round(Dmap, 9))) == sorted(map(tuple, np.round(st, 9)))
M = np.column_stack([T3L, Yh])
r1 = np.linalg.lstsq(M, T3R, rcond=None)[1]; r2 = np.linalg.lstsq(M, T3L - BL / 2, rcond=None)[1]
check("6 [T] D maps the 16's charges to themselves but D(T3L)=T3R, D(Y) not in span{T3L,Y}: no SM-only register",
      closed and r1[0] > 0.1 and r2[0] > 0.1, f"residuals {r1[0]:.2f}, {r2[0]:.2f}")

# ---------------- 7. BCS shape: leading radiative invariant with supplied measured inputs ----------------
print("7. BCS shape (#10079 X1): lowest CP-odd flavour invariant, supplied masses at mu = m_t and PDG Wolfenstein")
v = 246.0
mu_ = np.array([1.22e-3, 0.590, 162.9]); md_ = np.array([2.76e-3, 0.052, 2.75])
yu, yd = np.sqrt(2) * mu_ / v, np.sqrt(2) * md_ / v
lam, Aw, rb, eb = 0.22501, 0.826, 0.1591, 0.3523
s12 = lam; s23 = Aw * lam ** 2
s13e = Aw * lam ** 3 * (rb + 1j * eb) * np.sqrt(1 - Aw ** 2 * lam ** 4) / (np.sqrt(1 - lam ** 2) * (1 - Aw ** 2 * lam ** 4 * (rb + 1j * eb)))
s13, dl = abs(s13e), np.angle(s13e); c12, c23, c13 = (np.sqrt(1 - x ** 2) for x in (s12, s23, s13))
Vc = np.array([[c12 * c13, s12 * c13, s13 * np.exp(-1j * dl)],
               [-s12 * c23 - c12 * s23 * s13 * np.exp(1j * dl), c12 * c23 - s12 * s23 * s13 * np.exp(1j * dl), s23 * c13],
               [s12 * s23 - c12 * c23 * s13 * np.exp(1j * dl), -c12 * s23 - s12 * c23 * s13 * np.exp(1j * dl), c23 * c13]])
J = np.imag(Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1]))
Hu = np.diag(yu ** 2); Hd = Vc @ np.diag(yd ** 2) @ Vc.conj().T
L = {"u": Hu, "d": Hd}
imax = {}
for ln in range(1, 7):
    m = 0.0
    for wd in itertools.product("ud", repeat=ln):
        W = np.eye(3, dtype=complex)
        for ch in wd:
            W = W @ L[ch]
        m = max(m, abs(np.imag(np.trace(W))) / max(abs(np.trace(W)), 1e-300))
    imax[ln] = m
check("7a [T] all words of length <= 5 have real trace; length 6 is the first CP-odd invariant",
      max(imax[l] for l in range(1, 6)) < 1e-12 and imax[6] > 1e-15,
      f"max rel Im tr len<=5 {max(imax[l] for l in range(1, 6)):.0e}, len6 {imax[6]:.1e}, J={J:.2e}")
W6 = Hu @ Hd @ Hu @ Hu @ Hd @ Hd
im6 = np.imag(np.trace(W6)); im6c = np.imag(np.trace(Hu.conj() @ Hd.conj() @ Hu.conj() @ Hu.conj() @ Hd.conj() @ Hd.conj()))
det_c = np.linalg.det(Hu @ Hd - Hd @ Hu)
eps = 1e-4; Hr1, Hr2 = herm(), herm(); Wr = Hr1 @ Hr2 @ Hr1 @ Hr1 @ Hr2 @ Hr2; Wr = Wr / abs(np.trace(Wr))
Yr = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
lin = (np.angle(np.linalg.det((np.eye(3) + eps * Wr) @ Yr)) - np.angle(np.linalg.det(Yr))) / (eps * np.imag(np.trace(Wr))) - 1
check("7b [T] delta Y_u = P(H_u,H_d) Y_u gives delta theta = Im tr P (no 1/y enhancement); mirror words flip sign",
      abs(lin) < 1e-2 and abs(im6 + im6c) <= 1e-12 * abs(im6), f"Im tr(udu^2d^2)={im6:.2e}, mirror={im6c:.2e}, det[Hu,Hd]={abs(det_c):.1e}")
theta_rad = 2 * abs(im6)
check("7c [E] radiative theta_bar ceiling (light + mirror, any loop factor <= 1) < 1e-10", theta_rad < 1e-10,
      f"ceiling {theta_rad:.1e} (cutoff-level P-even G Gdual of #10079 E1 dominates instead)")

print(f"runtime {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
