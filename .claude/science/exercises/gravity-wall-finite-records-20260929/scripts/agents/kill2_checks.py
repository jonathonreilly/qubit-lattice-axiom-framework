"""Kill-round checks for routes F3 (non-ground / inverted compression channel) and F8 (A1 prediction).

Reuses probe 18's runner functions (modes_iso, kappa_iso, helicity, S_sym, Xr, Nmet) by executing the
runner once (it prints its own checks) and then calling its functions with a SIGNED helicity-0 weight.
"""
import io, contextlib, runpy, sys
import numpy as np

REPO = "/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790"
RUNNER = REPO + "/scripts/breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_helicity_one_partners_2026_09_29.py"
sys.path.insert(0, REPO + "/scripts")
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(RUNNER)
print("probe 18 runner replayed:", [l for l in buf.getvalue().splitlines() if l.startswith("TOTAL")])
modes_iso, kappa_iso, helicity, S_sym, Xr, Nmet = (g[k] for k in ("modes_iso", "kappa_iso", "helicity", "S_sym", "Xr", "Nmet"))

# ---------------------------------------------------------------- 1. agent 2's spin-S lemma (sign is the state's)
def spin_ops(S):
    d = int(round(2 * S + 1)); m = np.arange(S, -S - 1, -1)
    Jz = np.diag(m.astype(float)); Jp = np.zeros((d, d))
    for i in range(1, d):
        Jp[i - 1, i] = np.sqrt(S * (S + 1) - m[i] * (m[i] + 1))
    return Jz, Jp, Jp.T
S = 3; w = 1.0; Jz, Jp, Jm = spin_ops(S); H = w * Jz; O = Jm / np.sqrt(2 * S)
fs = [np.real(np.diag(O.T @ (H @ O - O @ H) - (H @ O - O @ H) @ O.T)[i]) for i in range(2 * S + 1)]
print("1. f-sum <[O^dag,[H,O]]> in |S,m>, m = S..-S:", np.round(fs, 3), " expected -w m/S:", np.round(-w * np.arange(S, -S - 1, -1) / S, 3))

# ---------------------------------------------------------------- 2. probe 11's identity off the ground state, and what m1 = 0 means there
# (a) representation theory: v_m = A + B(m^2 - 2) for any real A, B, so 4 v1 - v2 - 3 v0 = 0 whatever the signs
for A_, B_ in [(1, 0.3), (-1, 0.3), (0.2, -0.7), (0, 1)]:
    v = {m: A_ + B_ * (m * m - 2) for m in (0, 1, 2)}
    assert abs(4 * v[1] - v[2] - 3 * v[0]) < 1e-12
print("2a. 4 v1 = v2 + 3 v0 holds for every (A, B): identity is representation theory, positivity only fixes signs. v1 = 0 <=> v0 = -v2/3 (needs A = B).")
# (b) two-oscillator toy: H = w a^dag a - w b^dag b (b inverted), O = a + b: m1(O) = 0 with O(1) gapless weight at +w and -w
n = 4; a = np.diag(np.sqrt(np.arange(1, n)), 1); I = np.eye(n)
A = np.kron(a, I); Bop = np.kron(I, a); H2 = w * A.T @ A - w * Bop.T @ Bop; O2 = A + Bop
vac = np.zeros(n * n); vac[0] = 1
E, U = np.linalg.eigh(H2); amp = U.T @ (O2.T @ vac); spec = [(E[i] - 0.0, abs(amp[i]) ** 2) for i in range(len(E)) if abs(amp[i]) ** 2 > 1e-12]
m1 = sum(e * wgt for e, wgt in spec)
print("2b. inverted-oscillator toy: spectral weights of O^dag on the state (energy, weight):", [(round(e, 3), round(wg, 3)) for e, wg in spec], "; first moment m1 =", round(m1, 12))

# ---------------------------------------------------------------- 3. probe 18(C) with the helicity-0 kinetic weight inverted (agent 2's item (ii))
nC = np.array([0.3, -0.5, 0.81]); nC /= np.linalg.norm(nC)
q = 1e-3 * nC; K = 2 * np.sin(q / 2)
# helicity weights of the kinetic form for the gauge-pattern family (alpha) and the curl family (beta), from kappa_iso
def hel_weights(alpha, beta):
    kap = kappa_iso(q, alpha, beta); kh = K / np.linalg.norm(K)
    a_ = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(kh, a_); u /= np.linalg.norm(u); v = np.cross(kh, u)
    ep = (u + 1j * v) / np.sqrt(2)
    qc = g["qc"]
    T2 = qc(np.outer(ep, ep)); T1 = qc((np.outer(ep, kh) + np.outer(kh, ep)) / np.sqrt(2)); T0 = qc((3 * np.outer(kh, kh) - np.eye(3)) / np.sqrt(6)); Tt = qc(np.outer(kh, kh))
    Nm = Nmet  # tensor metric in q-coordinates
    def wgt(T):
        return np.real(T.conj() @ Nm @ kap @ Nm @ T / (T.conj() @ Nm @ T)) / np.linalg.norm(K) ** 2
    return wgt(T2), wgt(T1), wgt(T0), wgt(Tt)
k2a, k1a, k0a, kta = hel_weights(1, 0); k2b, k1b, k0b, ktb = hel_weights(0, 1)
print(f"3a. kinetic weights per unit K^2 (TT, +-1, spin-2 m=0 (3qq-delta)/sqrt6, qq): gauge family alpha=1 -> ({k2a:.3f}, {k1a:.3f}, {k0a:.3f}, {kta:.3f}); curl family beta=1 -> ({k2b:.3f}, {k1b:.3f}, {k0b:.3f}, {ktb:.3f})")
# tune alpha so that the +-1 weight vanishes with beta = 1: alpha k1a + k1b = 0
alpha_star = -k1b / k1a; beta = 1.0
k2, k1, k0, kt = hel_weights(alpha_star, beta)
print(f"3b. alpha* = {alpha_star:.4f} (beta = 1) gives (v2, v1, v0) spin-2 weights = ({k2:.4f}, {k1:.2e}, {k0:.4f}); 4v1 - v2 - 3v0 = {4*k1 - k2 - 3*k0:.2e}; v0/v2 = {k0/k2:.4f} = Einstein's -1/3 (probe 11 T3); qq weight = {kt:.4f}")
# modes on ker S(q) with |h|^2 and Fierz-Pauli stiffness, signed weight
def modes_signed(alpha, beta, m2, fp, qq):
    s_ = S_sym(qq); Bm = np.linalg.svd(s_[None, :])[2][1:].conj().T; trq = np.array([1, 1, 1, 0, 0, 0.])
    V = Xr(qq) + m2 * (Nmet - (np.outer(trq, trq) if fp else 0))
    Gi = np.linalg.inv(Bm.conj().T @ Bm); kred = Gi @ Bm.conj().T @ kappa_iso(qq, alpha, beta) @ Bm @ Gi; Vred = Bm.conj().T @ V @ Bm
    w2, vec = np.linalg.eig(Vred @ kred); KK = 2 * np.sin(qq / 2); out = []
    for j_ in np.argsort(w2.real):
        hv = Bm @ (kred @ vec[:, j_]); lab = helicity(hv, KK) if np.linalg.norm(hv) > 1e-12 else ("frozen", 1.0)
        out.append((lab[0], round(float(lab[1]), 3), complex(np.round(w2[j_] / np.linalg.norm(KK) ** 2, 4))))
    return out
for fp in (False, True):
    print(f"3c. {'Fierz-Pauli' if fp else '|h|^2'} stiffness, alpha = alpha*, beta = 1, m^2 = 1, q -> 0: (helicity, purity, omega^2/|K|^2) = {modes_signed(alpha_star, beta, 1.0, fp, q)}")
# the tachyon at finite momentum: growth rate across the zone (|h|^2 stiffness)
for qq in (0.5 * nC, 1.5 * nC, np.array([np.pi, np.pi, np.pi]) * 0.999):
    ms = modes_signed(alpha_star, beta, 1.0, False, qq); worst = min(m[2].real for m in ms)
    print(f"3d. |h|^2, |q| = {np.linalg.norm(qq):.2f}: most negative omega^2/|K|^2 = {worst:.4f}  -> growth rate Im omega = {np.sqrt(max(-worst,0))*np.linalg.norm(2*np.sin(qq/2)):.3f} per unit m")
# the +-1 mode with the weight tuned to zero: flat at every q at this order (the kinetic form is exactly quadratic in K here)
flat = [hel_weights(alpha_star, beta)[1]]
for qq in (0.3 * nC, 1.0 * nC, 2.0 * nC):
    kap = kappa_iso(qq, alpha_star, beta); KK = 2 * np.sin(qq / 2); kh = KK / np.linalg.norm(KK); a_ = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(kh, a_); u /= np.linalg.norm(u); v = np.cross(kh, u); ep = (u + 1j * v) / np.sqrt(2)
    T1 = g["qc"]((np.outer(ep, kh) + np.outer(kh, ep)) / np.sqrt(2)); flat.append(abs(T1.conj() @ Nmet @ kap @ Nmet @ T1))
print("3e. tuned alpha*: the helicity +-1 kinetic block at |q| -> 0, 0.3, 1, 2:", [f"{x:.1e}" for x in flat], "(identically zero: a flat gapless band at this order, not a removed mode; O(q^4) kinetic terms of a real move family would make it omega ~ q^2)")
# the sensitivity of the tuning: 1 % detuning of alpha
for f in (0.99, 1.01):
    ms = modes_signed(f * alpha_star, beta, 1.0, True, q); print(f"3f. alpha = {f:.2f} alpha*: helicity +-1 omega^2/|K|^2 = {[m[2] for m in ms if m[0]==1]} -> {'real (soft linear partner)' if all(m[2].real > 0 for m in ms if m[0]==1) else 'negative (helicity +-1 tachyon)'}")

# ---------------------------------------------------------------- 4. F8: the 09-25 note's walker-side obstruction restricts the lapse to the uniform one
# along an axis the third-order defect has the plane-wave form q1 q2 (q1 - q2), i.e. the bilinear B(N, M) = sum_x (N' M'' - N'' M') on a periodic grid.
L = 25; kk = 2 * np.pi * np.fft.fftfreq(L, d=1.0 / L) / L
F = np.fft.fft(np.eye(L), axis=0); Fi = np.linalg.inv(F)
D1 = np.real(Fi @ np.diag(1j * kk) @ F); D2 = np.real(Fi @ np.diag(-kk ** 2) @ F)
Bmat = D1.T @ D2 - D2.T @ D1           # B(N, M) = N^T Bmat M
ker = np.linalg.svd(Bmat)[2][np.abs(np.linalg.svd(Bmat)[1]) < 1e-10]
print(f"4. F8: dim ker of the antisymmetric third-order obstruction bilinear on a periodic axis of {L} sites = {len(ker)}; kernel is the uniform lapse: {len(ker) == 1 and np.allclose(np.abs(ker[0]), np.abs(ker[0][0]))}")
print("   Dirac-algorithm reading: {C[N], C[M]} = X[N, M] not a constraint -> consistency of C[N] ~ 0 restricts the lapse M to ker X (uniform), i.e. a lapse-fixing residual, at ZERO field on the matter side (2026-09-25 note T5(c)), before A1's second order.")
