"""CLS-1 core: X2 walker on Z^3 with a class-S condensate at the hw2 momenta (BCC residual lattice).
Folded (BCC) Bloch basis: at reduced momentum k the psi components sit at k+G, G in GS = [0, Kx, Ky, Kz].
Per Spin(10) component (spectator for bilinears). Conventions as X2 x2_cert.py: walker h(k) = sigma.sin k,
node chirality chi = prod cos k_a = (-1)^hw, chi = -1 left-handed (hw1 light).
"""
import numpy as np, itertools

s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
PI = np.pi
KX = np.array([0, PI, PI]); KY = np.array([PI, 0, PI]); KZ = np.array([PI, PI, 0])
KS = [KX, KY, KZ]                      # hw2 condensate momenta; K_b has zero b-component (b = index)
GS = [np.zeros(3), KX, KY, KZ]         # BCC reciprocal-lattice cosets (mod 2pi Z^3)
# group law: G_i + G_j (mod 2pi) = G_{i^j} with indices 0,1,2,3 <-> 0,Kx,Ky,Kz  (Klein four-group)
def gsum(i, j):
    return i ^ j

def walker(k):
    return sum(SIG[a] * np.sin(k[a]) for a in range(3))

def f_nn(k):
    return (1 - np.cos(k).sum()) / 2

def corner_name(v):
    v = tuple(int(round(x / PI)) % 2 for x in v)
    return f"{v}(hw{sum(v)})"

def h_psi(k, eps_a=0.0, eps_b=0.0, eta=0.0, amps=(1, 1, 1)):
    """8x8 folded psi Hamiltonian. Off-diagonal (G_i,G_j), i!=j, connected by K = G_{i^j} (index m = (i^j)-1):
    P-a  eps_a*amp_m * 1                         (on-site density  sum_K cos(K.x) psi^dag psi)
    P-b  eps_b*amp_m * sigma_m                   (on-site spin density sum_K cos(K.x) psi^dag sigma_{a(K)} psi)
    P-c  eta*amp_m * sigma_m * sin((k+G_i)_m)    (bond-symmetric modulated walker hop on m-bonds, K_m . b_m = 0)"""
    H = np.zeros((8, 8), complex)
    for i in range(4):
        H[2*i:2*i+2, 2*i:2*i+2] = walker(k + GS[i])
        for j in range(4):
            if i == j: continue
            m = gsum(i, j) - 1
            blk = eps_a * amps[m] * s0 + eps_b * amps[m] * SIG[m]
            blk = blk + eta * amps[m] * SIG[m] * np.sin((k + GS[i])[m])
            H[2*i:2*i+2, 2*j:2*j+2] = blk
    return H

def phi(k, kappa=0.0, amps=(1, 1, 1)):
    """4x4 (corner-space) filter map psi -> psi_S at reduced k: diag f(k+G) + kappa*amp (P-d, S-modulated filter)."""
    F = np.zeros((4, 4), complex)
    for i in range(4):
        F[i, i] = f_nn(k + GS[i])
        for j in range(4):
            if i != j:
                F[i, j] = kappa * amps[gsum(i, j) - 1]
    return F

def H_modelA(k, Delta, kappa=0.0, **kw):
    """Static site partner chi (8 comps) coupled through the full filtered field: 16x16."""
    Hp = h_psi(k, **kw)
    B = Delta * np.kron(phi(k, kappa, kw.get('amps', (1, 1, 1))), s0)   # chi <- psi block
    Z = np.zeros((8, 8), complex)
    return np.block([[Hp, B.conj().T], [B, Z]])

def heavy_projector_phi(k, kappa, amps, sig_th):
    """Channel-restricted filter: keep singular channels of phi with sigma >= sig_th (SMG gaps only those)."""
    F = phi(k, kappa, amps)
    U, sv, Vh = np.linalg.svd(F)
    keep = sv >= sig_th
    FR = (U[:, keep] * sv[keep]) @ Vh[keep, :]
    return FR, sv, U, Vh

def H_modelB(k, Delta, kappa=0.0, sig_th=1.0, **kw):
    amps = kw.get('amps', (1, 1, 1))
    Hp = h_psi(k, **kw)
    FR, sv, U, Vh = heavy_projector_phi(k, kappa, amps, sig_th)
    B = Delta * np.kron(FR, s0)
    Z = np.zeros((8, 8), complex)
    return np.block([[Hp, B.conj().T], [B, Z]])

def eig_with_psi_weight(H):
    w, v = np.linalg.eigh(H)
    psiw = (np.abs(v[:8, :]) ** 2).sum(0)
    return w, v, psiw

def rotations():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3): R[perm[i], i] = sg[i]
            if round(np.linalg.det(R)) == 1: Rs.append(R)
    return Rs

def spin_lift(R):
    """u with u sigma_a u^dag = sum_b R_ba sigma_b."""
    A = []
    for a in range(3):
        sp = sum(R[b, a] * SIG[b] for b in range(3))
        A.append(np.kron(SIG[a].T, s0) - np.kron(s0, sp))
    # solve vec(u sigma_a - sp u) = 0  -> (sigma_a^T kron 1 - 1 kron sp) vec(u) = 0 (column-major vec)
    A = np.vstack(A); _, sv, vh = np.linalg.svd(A)
    u = vh[-1].conj().reshape(2, 2, order='F')
    u = u / np.sqrt(np.abs(np.linalg.det(u)))
    return u

def gindex(vec):
    """index of the coset G (0..3) containing momentum vec mod 2pi, or -1."""
    for i, G in enumerate(GS):
        d = (vec - G) / (2 * PI)
        if np.allclose(d, np.round(d), atol=1e-9):
            return i
    return -1
