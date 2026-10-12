"""R6-2 check 2: the Hamiltonian (lattice) face of Weinberg-Witten, without Lorentz invariance.

Setting (vector-charge / linearized spatial-diffeo theory on Z^3, staggered Yee-type placement):
  h_ii on sites, h_ij (i != j) on face centres, xi_m on links; doubled integer coordinates.
  gauge: dh_ii(x) = xi_i(x+e_i) - xi_i(x-e_i);  dh_ij(x) = 1/2[xi_j(x+e_i)-xi_j(x-e_i)+xi_i(x+e_j)-xi_i(x-e_j)]
  (steps of 1 in doubled coordinates = half a lattice spacing).  pi_ij is gauge invariant (dpi = 0).

(A) Compute every gauge-invariant LOCAL linear functional w(h) supported in a box (nullspace of the
    restricted gauge map).  Show its symbol w(k) is O(|k|^2) (no invariant with an O(1) or O(k) symbol).
(B) Any strongly invariant local quadratic Hamiltonian density is
      1/2 pi.K.pi + sum_a lam_a w_a(h)^2 + sum mu * pi(x) w_a(h)(x)      (pi enters freely, h only via w)
    because a quadratic density invariant under all local xi must annihilate the restricted gauge
    vectors in h.  Build random positive ones, compute the physical frequencies on the reduced
    phase space (im G)^perp, and fit omega ~ k^p.  Expect p = 2.
(C) Control: the weakly invariant linearized-Einstein (Fierz-Pauli spatial) potential, whose density is
    gauge invariant only after summation: expect p = 1 on the two TT modes.
"""
import itertools
import numpy as np
from scipy.linalg import null_space

rng = np.random.default_rng(20261012)
comps = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]
E = np.eye(3, dtype=int)


def parity_ok(c, x):
    i, j = c
    x = np.array(x)
    if i == j:
        return np.all(x % 2 == 0)
    k = 3 - i - j
    return (x[i] % 2 != 0) and (x[j] % 2 != 0) and (x[k] % 2 == 0)


def xi_parity_ok(m, y):
    y = np.array(y)
    return all((y[a] % 2 != 0) if a == m else (y[a] % 2 == 0) for a in range(3))


def build(R):
    hvars = [(c, x) for c in comps for x in itertools.product(range(-R, R + 1), repeat=3) if parity_ok(c, x)]
    hidx = {v: n for n, v in enumerate(hvars)}
    xis = [(m, y) for m in range(3) for y in itertools.product(range(-R - 1, R + 2), repeat=3) if xi_parity_ok(m, y)]
    A = np.zeros((len(xis), len(hvars)))
    for r, (m, y) in enumerate(xis):
        y = np.array(y)
        for c in comps:
            i, j = c
            if i == j:
                if m != i:
                    continue
                for s, sign in [(-1, +1), (+1, -1)]:  # dh_ii(x) gets +xi(x+e_i) => x = y - e_i
                    x = tuple(y + s * E[i])
                    if (c, x) in hidx:
                        A[r, hidx[(c, x)]] += sign
            else:
                for a, b in [(i, j), (j, i)]:  # term 1/2[xi_b(x+e_a)-xi_b(x-e_a)]
                    if m != b:
                        continue
                    for s, sign in [(-1, +0.5), (+1, -0.5)]:
                        x = tuple(y + s * E[a])
                        if (c, x) in hidx:
                            A[r, hidx[(c, x)]] += sign
    return hvars, A


def symbol(hvars, w, k):
    """w_c(k) = sum_x w(c,x) exp(i k.x/2) for the 6 components."""
    out = np.zeros(6, dtype=complex)
    for n, (c, x) in enumerate(hvars):
        if w[n] != 0:
            out[comps.index(c)] += w[n] * np.exp(0.5j * np.dot(k, x))
    return out


def gauge_matrix(k):
    """6x3 symbol of the gauge map (same conventions as build)."""
    G = np.zeros((6, 3), dtype=complex)
    D = 2j * np.sin(np.array(k) / 2.0)  # half-step difference symbol over one lattice step
    for r, (i, j) in enumerate(comps):
        if i == j:
            G[r, i] = D[i]
        else:
            G[r, j] += 0.5 * D[i]
            G[r, i] += 0.5 * D[j]
    return G


def phys_basis(k):
    G = gauge_matrix(k)
    return null_space(G.conj().T)  # (im G)^perp, 3-dim for k != 0


R = 3
hvars, A = build(R)
W = null_space(A)  # columns: invariant functionals supported in the box
print(f"(A) box half-width R={R} (doubled coords): {len(hvars)} h-variables, {A.shape[0]} xi-variables")
print(f"    gauge-invariant local linear functionals supported in the box: dim = {W.shape[1]}")

dirs = [np.array([1.0, 0, 0]), np.array([1.0, 1.0, 0]) / np.sqrt(2), np.array([1.0, 2.0, 3.0]) / np.sqrt(14)]
eps_list = [0.2, 0.1, 0.05, 0.025, 0.0125]
for d in dirs:
    smax = []
    for eps in eps_list:
        S = np.array([symbol(hvars, W[:, a], eps * d) for a in range(W.shape[1])])  # nW x 6
        smax.append(np.linalg.svd(S, compute_uv=False)[0])
    p = np.polyfit(np.log(eps_list), np.log(smax), 1)[0]
    # also check gauge annihilation at one k
    k = 0.3 * d
    S = np.array([symbol(hvars, W[:, a], k) for a in range(W.shape[1])])
    resid = np.abs(S @ gauge_matrix(k)).max()
    print(f"    dir {np.round(d,3)}: largest singular value of all invariant symbols ~ eps^{p:.3f};"
          f"  max |w(k).G(k)| = {resid:.1e}")

# (B) random strongly invariant Hamiltonians
nW = W.shape[1]
Ssym = {}


def V_strong(k, lam):
    S = np.array([symbol(hvars, W[:, a], k) for a in range(nW)])  # nW x 6
    return S.conj().T @ np.diag(lam) @ S


def omegas_phys(K, V, M, U):
    """H = 1/2 pi^+ K pi + 1/2 h^+ V h + Re(pi^+ M h), restricted to physical subspace U (pi and h)."""
    Kp, Vp, Mp = U.conj().T @ K @ U, U.conj().T @ V @ U, U.conj().T @ M @ U
    n = U.shape[1]
    # hdot = K pi + M h ; pidot = -V h - M^+ pi
    F = np.block([[Mp, Kp], [-Vp, -Mp.conj().T]])
    ev = np.linalg.eigvals(F)
    return np.sort(np.abs(ev.imag))[::2][:n] if False else np.sort(np.abs(ev))


print("\n(B) random strongly invariant positive Hamiltonians (K = random SPD on pi, h only through invariants,")
print("    plus a random pi-w cross term); physical frequencies vs k on 3 directions")
for trial in range(3):
    lam = rng.uniform(0.5, 2.0, nW)
    Kr = rng.normal(size=(6, 6)); K = Kr @ Kr.T / 6 + np.eye(6)
    mu = 0.2 * rng.normal(size=(6, nW))
    for d in dirs[1:]:
        top = []
        for eps in eps_list:
            k = eps * d
            U = phys_basis(k)
            V = V_strong(k, lam)
            S = np.array([symbol(hvars, W[:, a], k) for a in range(nW)])
            M = mu @ S  # pi_b couples to sum_a mu_ba w_a(h)
            w = omegas_phys(K, V, M, U)
            top.append(w.max())
        p = np.polyfit(np.log(eps_list), np.log(top), 1)[0]
        print(f"    trial {trial} dir {np.round(d,3)}: max physical omega ~ k^{p:.3f}  (omega at k=0.0125: {top[-1]:.3e})")


# (C) control: weakly invariant spatial linearized-Einstein potential (Fierz-Pauli form), real q
def V_EH(k):
    q = 2 * np.sin(np.array(k) / 2.0)
    q2 = q @ q
    # quadratic form on symmetric h: 1/4 q^2 h:h - 1/2 |q.h|^2 + 1/2 (q.h.q) tr h - 1/4 q^2 (tr h)^2
    # build as 6x6 Hermitian matrix in comps basis with off-diagonal weight 2 (h_ij = h_ji counted twice)
    basis = []
    for (i, j) in comps:
        Bm = np.zeros((3, 3)); Bm[i, j] = 1; Bm[j, i] = 1
        if i == j:
            Bm[i, i] = 1
        basis.append(Bm)
    def form(h1, h2):
        return (0.25 * q2 * np.sum(h1 * h2) - 0.5 * (q @ h1) @ (q @ h2)
                + 0.25 * ((q @ h1 @ q) * np.trace(h2) + (q @ h2 @ q) * np.trace(h1))
                - 0.25 * q2 * np.trace(h1) * np.trace(h2))
    return np.array([[form(b1, b2) for b2 in basis] for b1 in basis])


print("\n(C) control: weakly invariant spatial linearized-Einstein potential (K = identity)")
for d in dirs[1:]:
    tt = []
    for eps in eps_list:
        k = eps * d
        q = 2 * np.sin(k / 2.0)
        Gr = gauge_matrix(k) / 1j  # real symbol, same image
        VE = V_EH(k)
        resid = np.abs(VE @ Gr).max()
        U = null_space(Gr.T)
        Vp = U.T @ VE @ U
        ev = np.linalg.eigvalsh((Vp + Vp.T) / 2)
        tt.append(np.sort(np.abs(ev))[-1])
    # omega^2 = eigenvalue of V on physical space with K=1
    p = np.polyfit(np.log(eps_list), np.log(np.sqrt(tt)), 1)[0]
    print(f"    dir {np.round(d,3)}: max |V_EH| eigen on phys ~ k^{2*p:.3f} => omega ~ k^{p:.3f};"
          f" weak-invariance residual |V G| = {resid:.1e}")

# strong-invariance test of the EH density: is the EH quadratic form a sum of squares of invariants?
# Its symbol must then factor through the invariant symbols S(k): V_EH(k) = S^+ N S for some N.
k = 0.3 * dirs[2]
S = np.array([symbol(hvars, W[:, a], k) for a in range(nW)])
VE = V_EH(k)
# best fit of V_EH on the span {S^+ e_a e_b^T S}: magnitude comparison at small k
ks = [0.1 * dirs[2], 0.05 * dirs[2]]
for kk in ks:
    S = np.array([symbol(hvars, W[:, a], kk) for a in range(nW)])
    print(f"    |k|={np.linalg.norm(kk):.3f}: ||V_EH|| = {np.linalg.norm(V_EH(kk)):.3e}, "
          f"||S||^2 (max size of any strongly invariant quadratic symbol per unit coefficient) = {np.linalg.norm(S,2)**2:.3e}")
print("    => V_EH is O(k^2) while every strongly invariant symbol is O(k^4): V_EH is not strongly invariant.")
