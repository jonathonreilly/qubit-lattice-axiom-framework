AUDIT_INPUT_PATHS = ('docs/FACE_SWAP_PARITY_GIVES_A_TREE_LEVEL_ZERO_THETA_ONLY_WITH_WALL_LOCAL_ELECTROWEAK_REGISTERS_AND_SHARED_COLOUR_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""face-swap-parity (R1): is the slab face swap P_slab a rule symmetry, and does it give theta_bar = 0 (BCS shape)?
Self-contained, seeded, numpy only. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261024)
t0 = time.time()
NP = [0, 0]


def check(name, ok, detail=""):
    NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" | {detail}" if detail else ""))


# ---------------- A. P_slab on the working slab ----------------
print("A. P_slab on the Wilson domain-wall slab (m = 0.6, Ls = 16) and the rule clauses")
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex); I2 = np.eye(2)
al = [np.kron(s1, s1), np.kron(s1, s2), np.kron(s1, s3), np.kron(s2, I2)]
be = np.kron(s3, I2)
S = be
okS = np.allclose(S @ be, be @ S) and all(np.allclose(S @ a, -a @ S) for a in al)
check("A1 [T] S = beta commutes with beta, anticommutes with alpha_1..4 (layer hop alpha_4 included)", okS)


def slab_H(k, m, Ls, A=np.zeros(3)):
    q = k + A
    h0 = sum(al[i] * np.sin(q[i]) for i in range(3)) + be * (m - 1 - sum(1 - np.cos(q[i]) for i in range(3)))
    T = 0.5 * be - 0.5j * al[3]
    H = np.zeros((4 * Ls, 4 * Ls), complex)
    for s in range(Ls):
        H[4*s:4*s+4, 4*s:4*s+4] = h0
        if s + 1 < Ls:
            H[4*(s+1):4*(s+1)+4, 4*s:4*s+4] = T
            H[4*s:4*s+4, 4*(s+1):4*(s+1)+4] = T.conj().T
    return H


m, Ls = 0.6, 16
R = np.fliplr(np.eye(Ls))
Pm = np.kron(R, S)
res = max(np.abs(Pm @ slab_H(-k, m, Ls) @ Pm.conj().T - slab_H(k, m, Ls)).max()
          for k in rng.uniform(-np.pi, np.pi, (5, 3)))
check("A2 [T] P_slab = layer reversal x (k -> -k) x beta is an exact symmetry of the slab", res < 1e-12, f"max res {res:.1e}")
A = rng.normal(0, 0.4, 3); k = rng.uniform(-np.pi, np.pi, 3)
rA = np.abs(Pm @ slab_H(-k, m, Ls, -A) @ Pm.conj().T - slab_H(k, m, Ls, A)).max()
rW = np.abs(Pm @ slab_H(-k, m, Ls, A) @ Pm.conj().T - slab_H(k, m, Ls, A)).max()
check("A3 [T] with a flat link background, symmetry needs A_i -> -A_i (ordinary parity on the ONE register)",
      rA < 1e-12 and rW > 1e-2, f"A->-A res {rA:.1e}; A->A res {rW:.2f}")
H0 = slab_H(np.zeros(3), m, Ls)
e, V = np.linalg.eigh(H0); idx = np.argsort(np.abs(e))[:4]; Pl = V[:, idx]
Gam = 1j * al[3] @ be; Gf = np.kron(np.eye(Ls), Gam)
g, gv = np.linalg.eigh(Pl.conj().T @ Gf @ Pl)
near = Pl @ gv[:, :2]; far = Pl @ gv[:, 2:]
w_near = np.sum(np.abs(near[:4 * Ls // 2]) ** 2) / 2
ov = np.linalg.norm(far.conj().T @ Pm @ near) ** 2 / 2
check("A4 [T/F] P_slab maps the near Weyl (Gamma -1) onto the far Weyl (Gamma +1): light 16 -> mirror, same charges",
      ov > 1 - 1e-6 and w_near > 0.99 and g[0] < -0.99 and g[-1] > 0.99, f"overlap {ov:.9f}, Gamma {g[0]:.3f}/{g[-1]:.3f}")
# theta carrier: spectral E.B on a periodic grid, parity image A'(x) = -A(-x), E'(x) = -E(-x)
N = 8
Af = rng.normal(size=(3, N, N, N)); Ef = rng.normal(size=(3, N, N, N))
kk = 2 * np.pi * np.fft.fftfreq(N)
KX = np.meshgrid(kk, kk, kk, indexing="ij")


def curl(F):
    Fh = [np.fft.fftn(F[i]) for i in range(3)]
    d = lambda i, j: np.real(np.fft.ifftn(1j * KX[j] * Fh[i]))
    return np.array([d(2, 1) - d(1, 2), d(0, 2) - d(2, 0), d(1, 0) - d(0, 1)])


inv = lambda F: np.array([np.roll(F[i][::-1, ::-1, ::-1], 1, axis=(0, 1, 2)) for i in range(3)])
EB = np.sum(Ef * curl(Af)); EBp = np.sum(-inv(Ef) * curl(-inv(Af)))
check("A5 [T] the theta carrier sum E.B is odd under P_slab's action on the register (bare theta forbidden)",
      abs(EB + EBp) < 1e-9 * abs(EB), f"Q = {EB:.4f}, Q_P = {EBp:.4f}")
# overlap (history weighting) and Luscher projector
gj = [np.block([[np.zeros((2, 2)), -1j * s], [1j * s, np.zeros((2, 2))]]) for s in (s1, s2, s3)]
g4 = np.block([[np.zeros((2, 2)), I2], [I2, np.zeros((2, 2))]]); G = gj + [g4]
g5 = G[0] @ G[1] @ G[2] @ G[3]


def Dov(k):
    DW = sum(1j * G[i] * np.sin(k[i]) for i in range(4)) + (sum(1 - np.cos(k[i]) for i in range(4)) - 1.0) * np.eye(4)
    w, U = np.linalg.eigh(DW.conj().T @ DW)
    return np.eye(4) + DW @ (U @ np.diag(w ** -0.5) @ U.conj().T)


rD, rG = 0.0, 0.0
for k in rng.uniform(-np.pi, np.pi, (6, 4)):
    kp = k * np.array([-1, -1, -1, 1]); D1, D2 = Dov(k), Dov(kp)
    rD = max(rD, np.abs(g4 @ D2 @ g4 - D1).max())
    rG = max(rG, np.abs(g4 @ (g5 @ (np.eye(4) - D2)) @ g4 + g5 @ (np.eye(4) - D1)).max())
check("A6 [T] overlap D is P-covariant, but gamma5_hat -> -gamma5_hat: Luscher's P_hat_- maps to P_hat_+",
      rD < 1e-12 and rG < 1e-12, f"res {rD:.1e}, {rG:.1e}; history-level chiral selection breaks P_slab explicitly")
Vfar = np.zeros((4 * Ls, 4 * Ls), complex); Vfar[-4:, -4:] = 0.5 * be
cv = np.abs(Pm @ Vfar @ Pm.conj().T - Vfar).max()
check("A7 [T] a far-wall-only gapping term (bilinear proxy) is not P_slab-invariant: explicit breaking", cv > 0.1, f"{cv:.2f}")

# ---------------- B. one gauge field (adopted Links clause) ----------------
print("B. toy, ONE gauge field: H, H' same charges; P: M(h,h') = sigma M(h',h)^dag sigma")
cm = lambda: rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
herm = lambda: (lambda X: (X + X.conj().T) / 2)(cm())


def Mfull(Al, B, C):  # Al(h,h') light block function
    return lambda h, hp: np.block([[Al(h, hp), B], [C, Al(hp, h).conj().T]])


def theta_tree(Mu, Md):
    a = np.angle(np.linalg.slogdet(Mu)[0] * np.linalg.slogdet(Md)[0])
    return (a + np.pi / 2) % np.pi - np.pi / 2


sig = np.kron(s1.real, np.eye(3))
th, pres = [], 0.0
for _ in range(200):
    Yu, Yd, Xu, Xd, Bq, Cu, Cd = cm(), cm(), cm(), cm(), herm(), herm(), herm()
    Au = lambda h, hp: Yu * np.conj(h) + Xu * np.conj(hp); Ad = lambda h, hp: Yd * h + Xd * hp
    Mu, Md = Mfull(Au, Bq, Cu), Mfull(Ad, Bq, Cd)
    h, hp = 1.0, 3.0 * np.exp(1j * rng.uniform(0, 2 * np.pi))
    pres = max(pres, np.abs(Mu(h, hp) - sig @ Mu(hp, h).conj().T @ sig).max())
    th.append(abs(theta_tree(Mu(h, hp), Md(h, hp))))
check("B1 [T] construction obeys the P relation exactly", pres < 1e-12, f"res {pres:.1e}")
check("B2 [F] generic P-symmetric couplings, h != h': theta_tree is O(1) (P_slab gives no cancellation)",
      np.median(th) > 0.1, f"median |theta| {np.median(th):.2f}")
Yu, Yd = cm(), cm()
Mu0 = Mfull(lambda h, hp: Yu * np.conj(h), np.zeros((3, 3)), np.zeros((3, 3)))
Md0 = Mfull(lambda h, hp: Yd * h, np.zeros((3, 3)), np.zeros((3, 3)))
h, hp = 1.0, 3.0 * np.exp(0.7j)
t0z = abs(theta_tree(Mu0(h, hp), Md0(h, hp)))
sl = np.linalg.svd(Yu, compute_uv=False); sm = np.linalg.svd(Mu0(h, hp)[3:, 3:], compute_uv=False)
check("B3 [T] with a supplied Z2 (no cross/mixing) theta_tree = 0 and mirror masses = light x v'/v exactly",
      t0z < 1e-12 and np.allclose(np.sort(sm), 3 * np.sort(sl)), f"|theta| {t0z:.1e}")
vmin = np.sqrt(2) * 172.6 / np.sqrt(4 * np.pi); rmax = np.sqrt(246.2 ** 2 - vmin ** 2) / vmin
check("B4 [E] but H' breaks OUR SU(2)xU(1): v^2+v'^2 = (246 GeV)^2, so v'/v <= %.2f, m_u' <= %.1f MeV, N_nu = 6"
      % (rmax, 2.16 * rmax), (6 - 2.984) / 0.008 > 5, f"N_nu 6 vs 2.984+-0.008: {(6-2.984)/0.008:.0f} sigma EXCLUDED")
nl = 0
for _ in range(100):
    Bq = herm() + 6 * np.eye(3); Cu = herm() + 6 * np.eye(3)
    sv = np.linalg.svd(Mfull(lambda h, hp: cm() * 1e-3, 1e3 * Bq, 1e3 * Cu)(1, 1), compute_uv=False)
    nl += np.sum(sv < 10.0)
check("B5 [F] heavy Hermitian vector-like masses pair light WITH mirror: no light chiral state survives", nl == 0,
      f"light states over 100 samples: {nl}")

# ---------------- C. BCS shape (supplied: wall-local electroweak registers, shared colour) ----------------
print("C. toy, BCS shape: M_u = diag(Y_u h*, Y_u^dag h'), M_d = diag(Y_d h, Y_d^dag h'*)")


def bcs(Yu, Yd, h, hp, Fu=None, Fd=None, Fu2=None, Fd2=None):
    Ylu, Yld = (Fu if Fu is not None else np.eye(3)) @ Yu, (Fd if Fd is not None else np.eye(3)) @ Yd
    Ymu, Ymd = (Fu2 if Fu2 is not None else np.eye(3)) @ Yu, (Fd2 if Fd2 is not None else np.eye(3)) @ Yd
    Z = np.zeros((3, 3))
    Mu = np.block([[Ylu * np.conj(h), Z], [Z, (Ymu * np.conj(hp)).conj().T]])
    Md = np.block([[Yld * h, Z], [Z, (Ymd * hp).conj().T]])
    return Mu, Md


def J_of(Yu, Yd):
    Uu = np.linalg.eigh(Yu @ Yu.conj().T)[1]; Ud = np.linalg.eigh(Yd @ Yd.conj().T)[1]
    Vc = Uu.conj().T @ Ud
    return abs(np.imag(Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1])))


tmax, Js, sgn = 0.0, [], True
for _ in range(300):
    Yu, Yd = cm(), cm()
    r = 10 ** rng.uniform(2, 10)
    h, hp = np.exp(1j * rng.uniform(0, 6.3)), r * np.exp(1j * rng.uniform(0, 6.3))
    Mu, Md = bcs(Yu, Yd, h, hp)
    sgn &= np.real(np.linalg.slogdet(Mu)[0] * np.linalg.slogdet(Md)[0]) > 0
    tmax = max(tmax, abs(theta_tree(Mu, Md))); Js.append(J_of(Yu, Yd))
check("C1 [T] arg det(M_u M_d) = 0 (det > 0, theta not pi) for all Y, v'/v in [1e2,1e10], VEV phases",
      tmax < 1e-10 and sgn, f"max |theta| {tmax:.1e}")
check("C2 [F] light J != 0 generically (O(1) random Yukawas)", np.median(Js) > 1e-4,
      f"median |J| {np.median(Js):.1e}; measured 3.1e-5 needs no tuning of theta")
Yu, Yd = cm(), cm(); Yu /= np.linalg.norm(Yu, 2); Yd /= np.linalg.norm(Yd, 2)
Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
a, ap = 0.05, 0.04
Fh = lambda c: np.eye(3) + c * Hu + 0.7 * c * Hd
Mu, Md = bcs(Yu, Yd, 1, 1e8, Fh(a), Fh(a), Fh(ap), Fh(ap))
t7a = abs(theta_tree(Mu, Md))
check("C3 [T] Hermitian dressings, light at scale v and mirror at v' (split coefficients): theta stays 0", t7a < 1e-12,
      f"{t7a:.1e}")
Fn = lambda c: np.eye(3) + c * Hd @ Hu + c ** 2 * Hu @ Hu @ Hd @ Hd @ Hu
Mu, Md = bcs(Yu, Yd, 1, 1e8, Fn(a), np.eye(3), Fn(ap), np.eye(3))
t7b = abs(theta_tree(Mu, Md)); Jinv = abs(np.linalg.det(Hu @ Hd - Hd @ Hu))
check("C4 [F] non-Hermitian products at split scales: theta != 0 but tiny, beyond first order in the dressing",
      0 < t7b < 1e-3, f"|theta| {t7b:.1e} at a = {a}, a' = {ap}; det[Hu,Hd] = {Jinv:.1e} (PRE-SET P7 overstated)")

# ---------------- D. SMG mirror with one gauge field: kappa ----------------
print("D. SMG mirror (one gauge field): theta_bar = theta - arg det(Y_u Y_d) - kappa arg(lambda_4)")
reps = {"Q": (6, 0.5), "u^c": (3, 0.5), "d^c": (3, 0.5), "L": (2, 0), "e^c": (1, 0), "nu^c": (1, 0)}
per16 = sum(dim / 3 * 2 * T for dim, T in [(d, t) for d, t in reps.values()] if T > 0)
Nf = 3; kappa = Nf * per16 / 4
check("D1 [T] per 16: sum over Weyls of 2T(colour) = %d; charge-4 vertex gives |kappa| = %d = N_f" % (per16, kappa),
      per16 == 4 and kappa == Nf)
check("D2 [T] the Z4 kept by the vertex is QCD-anomaly-free (shift 2 pi N_f): theta_bar continuous in arg lambda_4",
      abs((per16 * Nf * np.pi / 2) % (2 * np.pi)) < 1e-12)
thD = [abs((np.angle(np.linalg.det(cm() @ cm())) - kappa * rng.uniform(0, 6.3) + np.pi / 2) % np.pi - np.pi / 2)
       for _ in range(200)]
check("D3 [F] P_slab maps lambda_4 to a NEAR-wall vertex, not to Y: no relation, theta_bar generic O(1)",
      np.median(thD) > 0.1, f"median {np.median(thD):.2f}")

# ---------------- E. quality and window [E] ----------------
print("E. quality: Planck-suppressed P-even / P-misaligned operators (Lambda = 2.4e18 GeV supplied)")
Lam = 2.4e18
yu = np.diag([1.24e-5, 7.3e-3, 0.99]); yd = np.diag([2.7e-5, 5.3e-4, 2.4e-2])
rat = np.median([abs(np.imag(np.trace(np.linalg.inv(yu) @ cm()) + np.trace(np.linalg.inv(yd) @ cm())))
                 for _ in range(400)])
vGG = 1e-5 * Lam; vY = Lam * np.sqrt(1e-10 / rat)
check("E1 [E] (H'^dag H' - H^dag H) G Gdual/Lambda^2 is P-EVEN: allowed even with exact P; theta ~ v'^2/Lambda^2",
      vGG > 1e12, f"v' < {vGG:.1e} GeV")
check("E2 [E] misaligned dim-6 Yukawa (Y -> Y + C v'^2/Lambda^2): theta ~ Im Tr(Y^-1 C), enhanced 1/y_u",
      vY < vGG, f"median ratio {rat:.1e} -> v' < {vY:.1e} GeV")
vlow = 174 * 1.5e3 / 2.16e-3 * 1.0
check("E3 [E] window: mirror up quark m_u v'/v >= ~1.5 TeV (supplied) needs v' >= %.1e GeV; window open" % vlow,
      vlow < vY, f"[{vlow:.0e}, {vY:.0e}] GeV, v' supplied (not fixed by any rule)")
x1, x2 = (10.75 / 106.75) ** (1 / 3), (10.75 / 106.75) ** (1 / 3) * (17.75 / 7.25) ** (1 / 3)
dn = (4 / 7) * (2 + 3 * 1.75)
check("E4 [E] mirror gamma' + 3 nu' after colour decoupling: Delta N_eff = %.2f x^4, x in [%.2f, %.2f]" % (dn, x1, x2),
      dn * x1 ** 4 < 0.3, f"Delta N_eff in [{dn*x1**4:.2f}, {dn*x2**4:.2f}] vs ~0.3 allowed: marginal, CMB-S4 testable")

print(f"runtime {time.time()-t0:.2f} s")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
