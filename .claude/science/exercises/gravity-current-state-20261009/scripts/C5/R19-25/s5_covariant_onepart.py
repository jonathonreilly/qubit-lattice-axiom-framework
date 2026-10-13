"""R19-25 s5: where Gupta-Bleuler can work at CCR, one-particle level (comparator RECALLED: Gupta 1952).
Pre-registered (07:04Z, before running):
 (a) Covariant 10-component h_mn on the lattice: lightlike k^m = (|qhat|, qhat), Krein one-particle metric
     P = 1/2(eta eta + eta eta - eta eta) (de Donder/Feynman gauge), GB condition k^m hbar_mn = 0.
     Expect: V1 = 6-dim, Krein inertia (2 positive, 0 negative, 4 null), positive part = spatial TT (helicity +-2),
     static T00 source energy coefficient P^{00,00} = 1/2 > 0 (attractive), identical to the N-type -g rho^2/(4 qhat^2)
     up to normalization.
 (b) The 6 spatial slots alone (R15-5's N-type, temporal gauge) with cubic per-slot metric signs (eta_d, eta_o):
     the local-oscillator positive-frequency part of the vector constraint is null only if G eta G^dag = 0.
     Expect: nonzero for every sign choice at generic k (GB needs the lapse/shift slots: 10 per cell).
"""
import numpy as np, itertools
np.set_printoptions(precision=4, suppress=True, linewidth=150)
eta = np.diag([-1., 1, 1, 1])
pairs = [(m, n) for m in range(4) for n in range(m, 4)]          # 10 components
def basis():
    B = []
    for (m, n) in pairs:
        E = np.zeros((4, 4)); E[m, n] = E[n, m] = 1.0 if m != n else 1.0
        if m != n: E /= np.sqrt(2)
        B.append(E)
    return B
B = basis()
def P_metric():
    """Krein one-particle form <e,e'> = e_mn P^{mn,ab} e'_ab, indices raised with eta"""
    G = np.zeros((10, 10))
    for i, Ei in enumerate(B):
        for j, Ej in enumerate(B):
            Eu_i = eta@Ei@eta; Eu_j = eta@Ej@eta
            G[i, j] = np.sum(Eu_i*Ej) - 0.5*np.trace(eta@Ei)*np.trace(eta@Ej)
    return G
G = P_metric()
print("(a) covariant de Donder GB, one-particle space; metric inertia on all 10 components:",
      (int((np.linalg.eigvalsh(G) > 1e-12).sum()), int((np.linalg.eigvalsh(G) < -1e-12).sum())))
for kv in [[0, 0, 0.3], [0.2, 0.1, 0.05], [1.0, 2.0, 0.5], [np.pi*0.9, 0.3, 1.7]]:
    q = 2*np.sin(np.array(kv)/2); w = np.linalg.norm(q)
    ku = np.array([w, *q])                     # k^m, lightlike in eta
    kl = eta@ku
    # de Donder: k^m (h_mn - 1/2 eta_mn tr h) = 0 for n = 0..3, tr h = eta^{ab} h_ab
    C = np.zeros((4, 10))
    for j, E in enumerate(B):
        trh = np.trace(eta@E)
        C[:, j] = ku@E - 0.5*kl*trh
    u, s, vh = np.linalg.svd(C); V = vh[int((s > 1e-12).sum()):].T
    Gr = V.T@G@V; ev = np.linalg.eigvalsh((Gr + Gr.T)/2)
    inert = (int((ev > 1e-10).sum()), int((ev < -1e-10).sum()), int((np.abs(ev) <= 1e-10).sum()))
    # gauge modes k_m xi_n + k_n xi_m: in V and null?
    gauge = []
    for xi in np.eye(4):
        E = np.outer(kl, xi) + np.outer(xi, kl); gauge.append(np.array([np.sum(E*b) for b in B]))
    gauge = np.array(gauge).T
    in_V = np.abs(C@gauge).max(); null = np.abs(gauge.T@G@gauge).max()
    # positive part: spatial TT w.r.t. qhat
    n = q/w; a = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0])
    e1 = a - (a@n)*n; e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
    TT = []
    for M in [(np.outer(e1, e1) - np.outer(e2, e2))/np.sqrt(2), (np.outer(e1, e2) + np.outer(e2, e1))/np.sqrt(2)]:
        E = np.zeros((4, 4)); E[1:, 1:] = M; TT.append(np.array([np.sum(E*b) for b in B]))
    TT = np.array(TT).T
    print(f"  k={np.round(kv, 3)}: dim V1 = {V.shape[1]}, Krein inertia (+,-,0) = {inert}; gauge modes in V1: {in_V:.1e}, null: {null:.1e};"
          f" TT in V1: {np.abs(C@TT).max():.1e}, TT Gram = {np.round(np.diag(TT.T@G@TT), 6)}")
E00 = np.zeros((4, 4)); E00[0, 0] = 1; v00 = np.array([np.sum(E00*b) for b in B])
print(f"  static source T^00: propagator numerator P^(00,00) = {v00@G@v00:.4f} (GR: 1/2 > 0, attractive 1/qhat^2)")
Ginv = np.linalg.inv(G); print(f"  (check with inverse metric, the Feynman-gauge propagator numerator for T_00: {v00@Ginv@v00:.4f})")

print("\n(b) 6 spatial slots only: G(k) eta G(k)^dag for per-slot metric signs (eta_diag, eta_off)")
def Gk(k):
    q = 2*np.sin(np.asarray(k, float)/2)
    S = []
    for i in range(3):
        M = np.zeros((3, 3)); M[i, i] = 1; S.append(M)
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1/np.sqrt(2); S.append(M)
    return np.array([[q@b[:, j] for b in S] for j in range(3)])
for sd, so in itertools.product([1, -1], [1, -1]):
    et = np.diag([sd]*3 + [so]*3)
    vals = [np.linalg.norm(Gk(k)@et@Gk(k).T, 2) for k in ([0, 0, 0.3], [0.2, 0.1, 0.05], [1, 2, 0.5])]
    print(f"  (eta_d, eta_o) = ({sd:+d},{so:+d}): ||G eta G^T|| at three k = {np.round(vals, 5)}")
