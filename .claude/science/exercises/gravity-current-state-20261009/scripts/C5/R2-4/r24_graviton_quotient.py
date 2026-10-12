"""R2-4 check G1: the Euclidean linearised EH (Fierz-Pauli) weight on real h is not normalizable
for ANY Faddeev-Popov gauge fixing, on the lattice symbol that K7a/K2 use (O(4)-covariant in
s_mu = 2 sin(k_mu/2); K7a referee: spectrum s^2{-1, 0x4, 1/2x5}).

Quadratic form (per momentum, 10 real components h_{mu nu}, mu<=nu):
  K(h,h) = 1/2 s^2 h.h - (s.h).(s.h) + (s s:h) tr h - 1/2 s^2 (tr h)^2
Gauge directions: h -> h + s_mu xi_nu + s_nu xi_mu (4-dim range G).
Claims checked:
 (1) K G = 0 (exact gauge invariance).
 (2) The form restricted to G^perp (= the gauge quotient) has 5 positive and 1 NEGATIVE eigenvalue.
 (3) For every linear gauge condition F (4 x 10) with F|_G invertible, K + F^T F has a negative
     eigenvalue (FP factorisation: int e^{-K-|F|^2} = const * int_{quotient} e^{-K} diverges).
     Tested on 2000 random F at random momenta, plus de Donder.
 (4) The negative direction is the gauge-invariant spin-0 (conformal) mode.
"""
import numpy as np
rng = np.random.default_rng(7)
pairs = [(m, n) for m in range(4) for n in range(m, 4)]

def vec_to_mat(v):
    H = np.zeros((4, 4))
    for i, (m, n) in enumerate(pairs):
        H[m, n] = H[n, m] = v[i] if m == n else v[i] / np.sqrt(2)
    return H

def mat_to_vec(H):
    return np.array([H[m, n] if m == n else np.sqrt(2) * H[m, n] for (m, n) in pairs])

def Kform(s):
    s2 = s @ s
    def q(H):
        sh = s @ H
        tr = np.trace(H)
        return 0.5 * s2 * np.sum(H * H) - sh @ sh + (s @ H @ s) * tr - 0.5 * s2 * tr ** 2
    K = np.zeros((10, 10))
    E = np.eye(10)
    for i in range(10):
        for j in range(10):
            Hi, Hj = vec_to_mat(E[i]), vec_to_mat(E[j])
            K[i, j] = 0.5 * (q(Hi + Hj) - q(Hi) - q(Hj))
    return K

def gauge_basis(s):
    G = []
    for nu in range(4):
        xi = np.zeros(4); xi[nu] = 1
        H = np.outer(s, xi) + np.outer(xi, s)
        G.append(mat_to_vec(H))
    return np.array(G).T  # 10 x 4

worst_gi, neg_quot, neg_total, tested = 0, 0, 0, 0
for trial in range(400):
    k = rng.uniform(-np.pi, np.pi, 4)
    s = 2 * np.sin(k / 2)
    s2 = s @ s
    if s2 < 1e-6:
        continue
    K = Kform(s)
    G = gauge_basis(s)
    worst_gi = max(worst_gi, np.max(np.abs(K @ G)))
    ev = np.linalg.eigvalsh(K) / s2
    Q, _ = np.linalg.qr(G, mode='complete')
    Gp = Q[:, 4:]                      # orthonormal basis of G^perp
    evq = np.linalg.eigvalsh(Gp.T @ K @ Gp) / s2
    neg_quot += int(np.sum(evq < -1e-12) == 1 and np.sum(evq > 1e-12) == 5)
    if trial == 0:
        print("eigenvalues of K / s^2:", np.round(ev, 6))
        print("eigenvalues on gauge quotient / s^2:", np.round(evq, 6))
        # identify the negative direction: is it the spin-0 'conformal' combination?
        w, V = np.linalg.eigh(Gp.T @ K @ Gp)
        vneg = Gp @ V[:, 0]
        Hn = vec_to_mat(vneg)
        Pt = np.eye(4) - np.outer(s, s) / s2
        Hc = Pt / np.linalg.norm(mat_to_vec(Pt))
        print("overlap of negative quotient mode with transverse-trace (conformal) mode P_T:",
              round(abs(np.sum(Hn * Hc)), 6))
    for f in range(5):
        F = rng.normal(size=(4, 10))
        if abs(np.linalg.det(F @ G)) < 1e-6:
            continue
        tested += 1
        neg_total += int(np.min(np.linalg.eigvalsh(K + F.T @ F)) < -1e-12)
    # de Donder: F_nu = s_mu h_mu nu - 1/2 s_nu tr h
    Fd = np.zeros((4, 10))
    for i, (m, n) in enumerate(pairs):
        e = np.zeros(10); e[i] = 1; H = vec_to_mat(e)
        Fd[:, i] = s @ H - 0.5 * s * np.trace(H)
    tested += 1
    neg_total += int(np.min(np.linalg.eigvalsh(K + Fd.T @ Fd)) < -1e-12)
print(f"max |K G| over momenta = {worst_gi:.2e}  (exact gauge invariance)")
print(f"momenta with quotient signature (5+,1-): {neg_quot} / 400")
print(f"gauge fixings tested (random F with F|_G invertible, plus de Donder): {tested}; "
      f"K+F^T F indefinite in {neg_total}")

# small-momentum statement for any lattice symbol with an EH limit: the quotient eigenvalue ratio
for eps in (1e-1, 1e-2, 1e-3):
    s = eps * np.array([0.3, -0.7, 0.5, 0.2]); s2 = s @ s
    K = Kform(s); G = gauge_basis(s)
    Q, _ = np.linalg.qr(G, mode='complete'); Gp = Q[:, 4:]
    print(f"|s|={np.sqrt(s2):.1e}: quotient eigenvalues / s^2 =", np.round(np.linalg.eigvalsh(Gp.T @ K @ Gp) / s2, 6))
