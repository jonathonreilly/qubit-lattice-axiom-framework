"""CLS-1 step 3: theta, cross-checked against direct diagonalisation.
(a) literal task model: q-independent hopping eps between each hw1 corner and hw3 ONLY (no light-light term),
    mirror hw3 gapped by a static partner (Delta*f3). Analytic: zero mode = (Delta f3 * light_A1, 0 * hw3, -sqrt3 eps * chi);
    hw3 admixture 0 (mirror propagator zero), composite admixture theta_chi^2 = 3 eps^2/(3 eps^2 + Delta^2 f3^2).
(b) Theta-symmetric route (P-d, kappa): theta^2 = hw3 weight of the light space; SVD vs direct diagonalisation of model B
    (zero-eigenspace psi-span, degeneracy-safe) vs real-space L=4 torus diagonalisation of model A (light pairs at +-Delta*sigma_i).
"""
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from cls1_core import *
def P(*a): print(*a); sys.stdout.flush()
Pk = np.array([PI, 0, 0]); LIGHT = [0, 2, 3]; HW3 = 1
arch = {}

P("=== (a) literal task model: hw1<->hw3 hopping only, static partner on hw3 ===")
rows = []
for Delta in (0.5, 1.0, 2.0):
    for eps in (0.01, 0.1, 0.33, 1.0):
        Hp = h_psi(Pk)
        for c in LIGHT:
            Hp[2*c:2*c+2, 2*HW3:2*HW3+2] += eps * s0
            Hp[2*HW3:2*HW3+2, 2*c:2*c+2] += eps * s0
        B = Delta * np.kron(np.diag([0, 2, 0, 0]).astype(complex), s0)   # only hw3 partnered (f3 = 2)
        H = np.block([[Hp, B.conj().T], [B, np.zeros((8, 8))]])
        w, v = np.linalg.eigh(H)
        z = np.where(np.abs(w) < 1e-10)[0]
        # psi-carrying zero space: project zero eigenspace onto span{light psi, hw3 psi, chi_hw3}; measure weights
        Z = v[:, z]
        Pz = Z @ Z.conj().T
        hw3_w = np.real(np.trace(Pz[2*HW3:2*HW3+2, 2*HW3:2*HW3+2]))
        chi3_w = np.real(np.trace(Pz[8+2*HW3:8+2*HW3+2, 8+2*HW3:8+2*HW3+2]))
        nz_psi = int(round(np.real(np.trace(Pz[:8, :8]))))
        th_chi2 = 3 * eps**2 / (3 * eps**2 + (2 * Delta)**2)
        rows.append([Delta, eps, len(z), hw3_w, chi3_w / 2, th_chi2])
        P(f"  Delta={Delta:3.1f} eps={eps:4.2f}: zero modes {len(z)} (psi trace {nz_psi}); hw3 psi weight in zero space {hw3_w:.1e}; "
          f"chi_hw3 weight per spin {chi3_w/2:.6f} vs analytic theta_chi^2 {th_chi2:.6f}")
arch['literal_theta'] = np.array(rows)

P("\n=== (b) Theta route (P-d kappa): hw3 weight of the light space, three ways ===")
def realspace_modelA(L, Delta, kappa):
    N = L ** 3
    idx = lambda x: ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
    Hpp = np.zeros((2 * N, 2 * N), complex); Bcp = np.zeros((2 * N, 2 * N), complex)
    for x in itertools.product(range(L), repeat=3):
        i = idx(x); xa = np.array(x)
        cK = [np.cos(np.dot(K, xa)) for K in KS]
        for b in range(3):
            y = xa.copy(); y[b] += 1; j = idx(y)
            A = 1j * SIG[b] / 2
            Hpp[2*j:2*j+2, 2*i:2*i+2] += A; Hpp[2*i:2*i+2, 2*j:2*j+2] += A.conj().T
        Bcp[2*i:2*i+2, 2*i:2*i+2] += Delta * (0.5 + kappa * sum(cK)) * s0
        for b in range(3):
            for sgn in (1, -1):
                y = xa.copy(); y[b] += sgn; j = idx(y)
                Bcp[2*i:2*i+2, 2*j:2*j+2] += Delta * (-0.25) * s0
    return np.block([[Hpp, Bcp.conj().T], [Bcp, np.zeros_like(Hpp)]]), idx
L = 4; N = L ** 3
rowsb = []
for kappa in (0.01, 0.03, 0.1, 0.2, 0.33):
    F = phi(Pk, kappa); U, sv, Vh = np.linalg.svd(F)
    th2_svd = 1 - abs(Vh[0, HW3])**2
    th2_A1_svd = abs(Vh[1, HW3])**2                       # A1 light channel (largest light singular value)
    # direct diag of model B at P, degeneracy-safe: psi-span of the zero eigenspace
    sig_th = 0.5 * (sv[0] + sv[1])
    HB = H_modelB(Pk, 1.0, kappa, sig_th)
    w, v = np.linalg.eigh(HB)
    Z = v[:, np.abs(w) < 1e-10]
    Zpsi = Z[:8, :]
    Uu, ss, _ = np.linalg.svd(Zpsi, full_matrices=False)
    span = Uu[:, ss > 1e-6]                                # orthonormal basis of the psi part of the zero space
    th2_dd = np.real(np.trace((span @ span.conj().T)[2*HW3:2*HW3+2, 2*HW3:2*HW3+2])) / 2
    # real-space model A, L=4: eigenvectors at E = +Delta*sigma_A1 ; weight on the hw3 plane wave vs the three hw1 plane waves
    Hrs, idx = realspace_modelA(L, 1.0, kappa)
    er, vr = np.linalg.eigh(Hrs)
    target = sv[1]
    sel = np.where(np.abs(er - target) < 1e-9)[0]
    pw = {}
    for name, Q in [("hw3", np.array([PI, PI, PI])), ("hx", np.array([PI, 0, 0])), ("hy", np.array([0, PI, 0])), ("hz", np.array([0, 0, PI]))]:
        ph = np.array([np.exp(1j * np.dot(Q, x)) for x in itertools.product(range(L), repeat=3)]) / np.sqrt(N)
        Pw = np.kron(ph.reshape(-1, 1), s0)                # 2N x 2 plane-wave basis (psi part)
        pw[name] = sum(np.linalg.norm(Pw.conj().T @ vr[:2*N, s])**2 for s in sel)
    tot = sum(pw.values())
    th2_rs = pw["hw3"] / tot
    rowsb.append([kappa, th2_svd, th2_dd, th2_A1_svd, th2_rs, len(sel), tot])
    P(f"  kappa={kappa:5.3f}: total hw3 weight of light space: SVD {th2_svd:.8f} | model-B direct diag {th2_dd:.8f} | "
      f"A1 channel: SVD {th2_A1_svd:.8f} vs real-space L=4 model-A eigenvectors ({len(sel)} states at E=Delta*sigma_A1) {th2_rs:.8f}; "
      f"small-kappa formula 3kappa^2/4 = {0.75*kappa**2:.8f}")
arch['kappa_theta'] = np.array(rowsb)
np.savez('cls1_theta_archive.npz', **arch)
P("archived cls1_theta_archive.npz")
