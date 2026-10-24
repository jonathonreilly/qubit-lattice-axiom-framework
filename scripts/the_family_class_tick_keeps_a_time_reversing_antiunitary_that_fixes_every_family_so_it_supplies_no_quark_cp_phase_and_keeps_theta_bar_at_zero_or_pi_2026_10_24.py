AUDIT_INPUT_PATHS = ('docs/THE_FAMILY_CLASS_TICK_KEEPS_A_TIME_REVERSING_ANTIUNITARY_THAT_FIXES_EVERY_FAMILY_SO_IT_SUPPLIES_NO_QUARK_CP_PHASE_AND_KEEPS_THETA_BAR_AT_ZERO_OR_PI_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""cp-source-new-tick: where can a quark-mixing CP phase come from on the family-class tick?

Supplied model, finite diagnostic + exact lemmas. The adopted tick's light node is rebuilt as the exact
five-direction Clifford walk U = f + i n.Gamma (new-tick-recheck section 3; any 4-d Cl(5) irrep is unitarily
equivalent, so the basis is a convention): f = mean cos K, hops sin K_a / sqrt3 on tau3 sigma_a, L-R pieces
Re H, Im H on tau1, tau2, H = (sqrt2/3)(cos Kx + w* cos Ky + w cos Kz). Families: 3, mass matrices supplied.
"""
import numpy as np

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261024)
PASS = 0
FAIL = 0


def check(name, ok, info=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{'PASS' if ok else 'FAIL'} {name}: {info}")


w = np.exp(2j * np.pi / 3)
s0 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0 + 0j, -1.0])
G = [np.kron(sz, sx), np.kron(sz, sy), np.kron(sz, sz), np.kron(sx, s0), np.kron(sy, s0)]
TAU3 = np.kron(sz, s0)  # chirality: +1 = L (q = 2), -1 = R mirror (q = 1)


def Hlr(K):
    return (np.sqrt(2) / 3) * (np.cos(K[0]) + np.conj(w) * np.cos(K[1]) + w * np.cos(K[2]))


def ncoef(K):
    h = Hlr(K)
    return np.array([np.sin(K[0]), np.sin(K[1]), np.sin(K[2])]) / np.sqrt(3), h


def U(K):
    n3, h = ncoef(K)
    f = np.mean(np.cos(K))
    M = f * np.eye(4, dtype=complex)
    for a in range(3):
        M = M + 1j * n3[a] * G[a]
    return M + 1j * (h.real * G[3] + h.imag * G[4])


def mK(K):  # node expansion of H: the dimension-5 L-R term
    return -(np.sqrt(2) / 6) * (K[0] ** 2 + np.conj(w) * K[1] ** 2 + w * K[2] ** 2)


print("== A. the tick's light node (five-direction Clifford walk)")
Ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(12)]
ac = max(np.abs(G[a] @ G[b] + G[b] @ G[a] - 2 * (a == b) * np.eye(4)).max() for a in range(5) for b in range(5))
P5 = G[0] @ G[1] @ G[2] @ G[3] @ G[4]
un = max(np.abs(U(K) @ U(K).conj().T - np.eye(4)).max() for K in Ks)
check("A1 Cl(5) on one 4-spinor, product scalar, U unitary", ac < 1e-14 and np.abs(P5 + np.eye(4)).max() < 1e-14 and un < 1e-14,
      f"anticomm {ac:.0e}, G1..G5 = -1, unitarity {un:.1e}")


def intertwiner(sig, anti=True):
    """Solve V conj(U(K)) = U(sig K)^+ V (antiunitary, time-reversing) over 12 K; return null-space dim, V."""
    rows = []
    for K in Ks:
        A = np.conj(U(K)) if anti else U(K)
        B = U(sig(K)).conj().T if anti else U(sig(K))
        # vec(V A - B V) = (A^T kron I - I kron B) vec(V)
        rows.append(np.kron(A.T, np.eye(4)) - np.kron(np.eye(4), B))
    Mx = np.vstack(rows)
    s, vh = np.linalg.svd(Mx)[1:]
    null = int(np.sum(s < 1e-10))
    V = vh[-1].conj().reshape(4, 4, order="F") if null else None
    return null, V, s[-1] if null else s.min()


print("== B. which time-reversing antiunitaries does the tick keep?")
maps = {
    "T alone": lambda K: -K,
    "T x C2'(1,-1,0)": lambda K: np.array([K[1], K[0], K[2]]),
    "T x C2'(1,0,-1)": lambda K: np.array([K[2], K[1], K[0]]),
    "T x C2'(0,1,-1)": lambda K: np.array([K[0], K[2], K[1]]),
    "T x C2'(1,1,0)": lambda K: np.array([-K[1], -K[0], K[2]]),
    "T x C4z": lambda K: np.array([K[1], -K[0], -K[2]]),
    "T x C2z": lambda K: np.array([K[0], K[1], -K[2]]),
}
res = {}
for nm, sg in maps.items():
    res[nm] = intertwiner(sg)
print("  null-space dims: " + ", ".join(f"{k}: {v[0]}" for k, v in res.items()))
check("B1 Floquet T alone has no intertwiner (family class breaks T)", res["T alone"][0] == 0,
      f"smallest singular value {res['T alone'][2]:.2e}")
nullC2, V, _ = res["T x C2'(1,-1,0)"]
ok = nullC2 >= 1
if ok:
    V = V / np.sqrt(abs(np.trace(V @ V.conj().T)) / 4)
    unit = np.abs(V @ V.conj().T - np.eye(4)).max()
    Kt = [rng.uniform(-np.pi, np.pi, 3) for _ in range(20)]
    err = max(np.abs(V @ np.conj(U(K)) @ V.conj().T - U(maps["T x C2'(1,-1,0)"](K)).conj().T).max() for K in Kt)
    chir = np.abs(V @ TAU3 @ V.conj().T - TAU3).max()
    VV = V @ np.conj(V)
    sq = "+1" if np.abs(VV - np.eye(4)).max() < 1e-10 else ("-1" if np.abs(VV + np.eye(4)).max() < 1e-10 else "other")
    ok = unit < 1e-12 and err < 1e-12 and chir < 1e-12
    check("B2 T x C2'(1,-1,0) kept: unitary V, intertwines 20 fresh K, keeps L as L", ok,
          f"|VV+-1| {unit:.0e}, err {err:.0e}, tau3 err {chir:.0e}, (V K)^2 = {sq}")
else:
    check("B2 T x C2'(1,-1,0) kept", False, "no intertwiner")
axrev = [k for k in ["T x C2'(1,-1,0)", "T x C2'(1,0,-1)", "T x C2'(0,1,-1)"] if res[k][0] >= 1]
print(f"  axis-reversing C2' kept with T: {len(axrev)}/3; T x C4z kept: {res['T x C4z'][0] >= 1}")

print("== C. family label under the kept antiunitary (zoom-3 characters k_j = (2pi/3) j (1,1,1))")


def fam_image(sig, j):
    k = (2 * np.pi / 3) * j * np.ones(3)
    kk = np.mod(sig(k), 2 * np.pi)
    for jj in range(3):
        if np.allclose(kk, np.mod((2 * np.pi / 3) * jj * np.ones(3), 2 * np.pi), atol=1e-12):
            return jj
    return None


imgC2 = [fam_image(maps["T x C2'(1,-1,0)"], j) for j in range(3)]
imgT = [fam_image(maps["T alone"], j) for j in range(3)]
imgC4 = [fam_image(maps["T x C4z"], j) for j in range(3)]
check("C1 T x C2' fixes every family label (X diagonal); copies: X = 1", imgC2 == [0, 1, 2],
      f"T x C2': {imgC2}; T alone: {imgT} (swaps 1<->2); T x C4z: {imgC4} (None = off the family set)")
# turn-axis values of the tick's L-R pieces
hmax = max(abs(Hlr((2 * np.pi / 3) * j * np.ones(3))) for j in range(3))
mmax = max(abs(mK(t * np.ones(3))) for t in np.linspace(-1, 1, 7))
check("C2 tick's L-R pieces vanish on the turn axis and at the node (1 + w + w^2 = 0)",
      hmax < 1e-15 and mmax < 1e-15 and abs(Hlr(np.zeros(3))) < 1e-15,
      f"max|H(K_j)| {hmax:.0e}, max|m(t,t,t)| {mmax:.0e}, |H(0)| {abs(Hlr(np.zeros(3))):.0e}")

print("== D. turn-CP lemma with the new charges, and the generalized-CP lemma")


def jarlskog(Mu, Md):
    Hu, Hd = Mu @ Mu.conj().T, Md @ Md.conj().T
    _, Uu = np.linalg.eigh(Hu)
    _, Ud = np.linalg.eigh(Hd)
    Vc = Uu.conj().T @ Ud
    return np.imag(Vc[0, 0] * Vc[1, 1] * np.conj(Vc[0, 1]) * np.conj(Vc[1, 0]))


def cgauss(n=3):
    return (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)


def theta_tree(Mu, Md):
    return np.angle(np.linalg.det(Mu) * np.linalg.det(Md))


N = 2000
# triplet charges (0,1,2): turn-invariant mass = diagonal
Jtrip = max(abs(jarlskog(np.diag(cgauss()[0]), np.diag(cgauss()[0]))) for _ in range(200))
Jall = np.array([abs(jarlskog(cgauss(), cgauss())) for _ in range(N)])
check("D1 turn-CP lemma: triplet (0,1,2) gives J = 0; all q = 2 lifts it", Jtrip < 1e-14 and np.median(Jall) > 1e-3,
      f"triplet max|J| {Jtrip:.0e}; q = 2 median |J| {np.median(Jall):.2e} (lifted; turn now a scalar on families)")
# family-blind tick only: U(3) family symmetry, M proportional to 1
Cb = max(abs(np.linalg.det((lambda a, b: a @ b - b @ a)(*(m @ m.conj().T for m in ((1 + 0.3j) * np.eye(3), 0.7 * np.eye(3) + 0.2j * np.eye(3)))))) for _ in range(1))
print(f"  family-blind tick masses (prop. to 1): det[Hu,Hd] = {Cb:.0e}; masses degenerate, mixing unphysical (U(3) family symmetry)")
# generalized CP: X = S S^T, H = S R S^+ (R real symmetric): any unitary X with X X* = 1
gmax, dmax, jmax, tmax = 0.0, 0.0, 0.0, 0.0
for _ in range(300):
    S, _ = np.linalg.qr(cgauss())
    X = S @ S.T
    Ru, Rd = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))
    Mu, Md = S @ Ru, S @ Rd  # X Mu* = S S^T S* Ru = Mu (X_R = 1): generalized CP on Q, real on singlets
    Hu, Hd = Mu @ Mu.conj().T, Md @ Md.conj().T
    gmax = max(gmax, np.abs(X @ Hu.conj() @ X.conj().T - Hu).max())
    C = Hu @ Hd - Hd @ Hu
    dmax = max(dmax, abs(np.linalg.det(C)) / np.linalg.norm(C, 2) ** 3)
    jmax = max(jmax, abs(jarlskog(Mu, Md)))
    # copies (X = 1): real masses -> theta in {0, pi}
    th = theta_tree(Ru.astype(complex), Rd.astype(complex))
    tmax = max(tmax, min(abs(th), abs(abs(th) - np.pi)))
check("D2 generalized CP (any X, X X* = 1) on Q forces det[Hu,Hd] = 0 and J = 0", gmax < 1e-12 and dmax < 1e-13 and jmax < 1e-13,
      f"condition err {gmax:.0e}, max |det C|/||C||^3 {dmax:.0e}, max|J| {jmax:.0e} over 300")
check("D3 kept antiunitary with X = 1 (copies) or diagonal: real masses, theta_tree in {0, pi}", tmax < 1e-12,
      f"max distance to {{0,pi}} {tmax:.0e}")

print("== E. worst-case leak: tick's T-odd L-R piece read as a family-universal mass entry")
# eps = |m(K)|/m at K a = E a; J, theta linear in eps -> slope, then value at physical scale
eps_list = [1e-3, 1e-4, 1e-5]
slopesJ, slopesT = [], []
for _ in range(100):
    Ru, Rd = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))
    ph = np.exp(1j * rng.uniform(0, 2 * np.pi))
    sJ, sT = [], []
    for e in eps_list:
        Mu = Ru + e * ph * np.eye(3)
        Md = Rd + e * ph * np.eye(3)
        sJ.append(abs(jarlskog(Mu, Md)) / e)
        th = theta_tree(Mu, Md)
        sT.append(min(abs(th), abs(abs(th) - np.pi)) / e)
    slopesJ.append(sJ)
    slopesT.append(sT)
slopesJ, slopesT = np.array(slopesJ), np.array(slopesT)
lin = np.median(np.abs(slopesJ[:, 2] / slopesJ[:, 0] - 1))
cJ, cT = np.median(slopesJ[:, 2]), np.median(slopesT[:, 2])
E_P = 1.22e19
for lab, aP in [("a = l_P", 1.0), ("a = 10 l_P", 10.0)]:
    Ka = 172.6 / E_P * aP
    eps = (np.sqrt(2) / 6) * Ka ** 2
    print(f"  {lab}: K a(m_t) = {Ka:.1e}, |m|/m ~ {eps:.1e}: J_leak ~ {cJ * eps:.0e}, theta_leak ~ {cT * eps:.0e}")
check("E1 leak is linear in the T-odd entry (median slope ratio dev < 0.05) and negligible",
      lin < 0.05 and cJ * (np.sqrt(2) / 6) * (1.73e3 / E_P) ** 2 < 1e-20,
      f"slope J {cJ:.2f}, theta {cT:.2f}; at 10 l_P both < 1e-29 vs J 3.08e-5, theta 1e-10")

print("== F. supplied phases (break every kept antiunitary): J and theta tied")
TH = np.array([min(abs(t), abs(abs(t) - np.pi)) for t in [theta_tree(cgauss(), cgauss()) for _ in range(N)]])
frac = np.mean(TH < 1e-10)
corr = np.mean(Jall > 1e-6)
check("F1 generic supplied phases: J != 0 and theta_bar O(1); none passes 1e-10", frac == 0.0 and np.median(TH) > 0.3,
      f"median|J| {np.median(Jall):.1e} (J > 1e-6 in {corr:.2f}); median theta {np.median(TH):.2f} rad; |theta|<1e-10: {frac:.3f}")

print("VERDICT: tick does not supply CP. J != 0 is ALLOWED only with supplied mass-sector phases that break the kept")
print("T x C2' (not just T); then theta_bar is O(1) unless a Nelson-Barr-type reading is also supplied.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
