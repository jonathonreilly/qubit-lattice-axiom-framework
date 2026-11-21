# GUIDE only: sanity check of the squaring inequality on toy positive symmetric kernels with a Z_2 symmetry.
# 1 - theta^2 >= (1 - 1/kappa)(1 - rho); also the time-t form theta^(2t) <= 1/kappa + (1-1/kappa) rho^t.
import numpy as np
rng = np.random.default_rng(876)
def check(L, inv):
    n = L.shape[0]
    w, V = np.linalg.eigh(L)
    lam0 = w[-1]; Om = V[:, -1]; Om = Om*np.sign(Om.sum())
    assert (Om > 0).all()
    Pi = np.zeros((n, n)); Pi[np.arange(n), inv] = 1.0
    Pe = (np.eye(n)+Pi)/2; Po = (np.eye(n)-Pi)/2
    wo, Vo = np.linalg.eigh(Po@L@Po); lam_odd = wo[-1]; Psi = Vo[:, -1]
    we = np.sort(np.linalg.eigvalsh(Pe@L@Pe))
    lam1e = we[-2]
    g = Psi/Om; mu = Om**2
    assert abs((mu*g*g).sum()-1) < 1e-9
    kappa = (mu*g**4).sum()
    theta = lam_odd/lam0; rho = lam1e/lam0
    lhs = 1-theta**2; rhs = (1-1/kappa)*(1-rho)
    worst_t = max(theta**(2*t) - (1/kappa + (1-1/kappa)*rho**t) for t in range(1, 30))
    return theta, rho, kappa, lhs-rhs, worst_t
bad = 0; rows = []
for trial in range(400):
    k = int(rng.integers(2, 9)); n = 2*k
    inv = np.concatenate([np.arange(k, n), np.arange(0, k)])
    A = rng.random((n, n))**rng.integers(1, 6)
    A = A + A.T
    A = A + A[np.ix_(inv, inv)]            # symmetric under the involution
    A = A + 1e-6
    if trial % 2 == 0:                      # make it a positive operator too
        A = A @ A
    th, rh, ka, slack, wt = check(A, inv)
    rows.append((th, rh, ka, slack, wt))
    if slack < -1e-10 or wt > 1e-10: bad += 1
rows = np.array(rows)
print("trials", len(rows), "violations", bad)
print("min slack of 1-theta^2-(1-1/kappa)(1-rho):", rows[:, 3].min())
print("max of theta^(2t)-bound over t<30:", rows[:, 4].max())
print("kappa range", rows[:, 2].min(), rows[:, 2].max())
# Ising chain in a transverse reading: transfer operator of a 2 x N strip, Z_2 = global flip
def ising_strip(N, K):
    import itertools
    S = np.array(list(itertools.product([-1, 1], repeat=N)))
    intra = K*(S*np.roll(S, -1, axis=1)).sum(1)
    L = np.exp(0.5*intra[:, None] + 0.5*intra[None, :] + K*S@S.T)
    idx = {tuple(s): i for i, s in enumerate(S)}
    inv = np.array([idx[tuple(-s)] for s in S])
    return L, inv
for K in (0.2, 0.3, 0.4407, 0.6, 0.8):
    L, inv = ising_strip(8, K)
    th, rh, ka, slack, wt = check(L, inv)
    E = -np.log(th); m = -np.log(rh)
    print("Ising ring N=8 K=%.4f  E_odd=%.4f  m_even=%.4f  kappa=%.4f  2E/m=%.3f  slack=%.3e" % (K, E, m, ka, 2*E/m, slack))
