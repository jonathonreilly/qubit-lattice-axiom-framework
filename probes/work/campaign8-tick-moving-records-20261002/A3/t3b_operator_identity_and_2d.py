"""Check 3b: the 1D bond-flow operator identity behind the feasibility theorem, and a 2D probe.

1D (ring, N>=5, any internal dimension d, any strictly range-1 tick U):
  MH flow operator   B_x = 1/2{Pi_x, U^+ Pi_{x+1} U} - 1/2{Pi_{x+1}, U^+ Pi_x U}
  local cut operator A_x = Pi_x - Q U^+ Pi_{[x-1,x]} U Q,   Q = Pi_x + Pi_{x+1}
  Claim (EXACT, proved in the report): B_x = A_x, hence  -Pi_{x+1} <= B_x <= Pi_x,
  hence the minimal MH rule never breaks the outflow bound.
  Also: the imaginary (lambda) part of the KD split has zero net flow in 1D.
2D (torus L x L, d=4 'direction' components, coin-hop-coin walk, strictly range 1):
  probe whether the minimal MH rule can break the outflow bound, and whether the
  lambda (Im K) flow is non-zero there (a local divergence-free extra flow).
"""
import numpy as np
from common import haar_unitary, rand_state, mh_split, rule_from_flow

rng = np.random.default_rng(5)


def random_walk_1d(N, d):
    n = N * d
    U = np.eye(n, dtype=complex)
    # coin (d x d per site), across (pair last component of x with first of x+1), coin
    C1 = np.zeros((n, n), complex); C2 = np.zeros((n, n), complex)
    for x in range(N):
        C1[x*d:(x+1)*d, x*d:(x+1)*d] = haar_unitary(d, rng)
        C2[x*d:(x+1)*d, x*d:(x+1)*d] = haar_unitary(d, rng)
    A = np.eye(n, dtype=complex)
    for x in range(N):
        a, b = x * d + (d - 1), ((x + 1) % N) * d + 0
        A[np.ix_([a, b], [a, b])] = haar_unitary(2, rng)
    return C2 @ A @ C1


def proj(N, d, sites):
    P = np.zeros((N * d, N * d))
    for s in sites:
        for k in range(d):
            P[(s % N) * d + k, (s % N) * d + k] = 1.0
    return P


worst_id, worst_up, worst_lo, worst_im = 0.0, -1.0, -1.0, 0.0
for N in (5, 6, 8):
    for d in (1, 2, 3):
        for rep in range(20):
            U = random_walk_1d(N, d) if d > 1 else None
            if d == 1:
                # d=1: strictly range-1 ring unitaries are pair-partitions or weighted shifts
                if rep % 4 == 3:
                    U = np.zeros((N, N), complex)
                    sgn = 1 if rep % 8 == 3 else -1
                    for x in range(N):
                        U[(x + sgn) % N, x] = np.exp(2j * np.pi * rng.random())
                else:
                    U = np.eye(N, dtype=complex)
                    start = int(rng.integers(2))
                    for k in range(N // 2):
                        a, b = (start + 2 * k) % N, (start + 2 * k + 1) % N
                        U[np.ix_([a, b], [a, b])] = haar_unitary(2, rng)
            for x in range(N):
                Px, Px1 = proj(N, d, [x]), proj(N, d, [x + 1])
                B = 0.5 * (Px @ U.conj().T @ Px1 @ U + U.conj().T @ Px1 @ U @ Px) \
                    - 0.5 * (Px1 @ U.conj().T @ Px @ U + U.conj().T @ Px @ U @ Px1)
                Q = Px + Px1
                A = Px - Q @ U.conj().T @ proj(N, d, [x - 1, x]) @ U @ Q
                worst_id = max(worst_id, float(np.abs(B - A).max()))
                worst_up = max(worst_up, float(np.linalg.eigvalsh(B - Px).max()))
                worst_lo = max(worst_lo, float(np.linalg.eigvalsh(-B - Px1).max()))
            psi = rand_state(N * d, rng)
            piMH, K, _ = mh_split(U, psi, N, d)
            Dim = K.imag - K.imag.T
            worst_im = max(worst_im, float(np.abs(Dim).max()))
print("1D rings N in {5,6,8}, d in {1,2,3}, 20 random range-1 ticks each:")
print(f"   max |B_x - A_x| (operator identity)        = {worst_id:.2e}")
print(f"   max eigenvalue of B_x - Pi_x      (<= 0?)   = {worst_up:.2e}")
print(f"   max eigenvalue of -B_x - Pi_x+1   (<= 0?)   = {worst_lo:.2e}")
print(f"   max |Im K - Im K^T| (lambda-flow)           = {worst_im:.2e}")

# ---------------- 2D torus probe ----------------
L, d2 = 4, 4                 # components: 0=+x, 1=-x, 2=+y, 3=-y half-sites
nsite = L * L
n = nsite * d2


def sid(i, j):
    return (i % L) * L + (j % L)


def random_walk_2d():
    C1 = np.zeros((n, n), complex); C2 = np.zeros((n, n), complex)
    for s in range(nsite):
        C1[s*d2:(s+1)*d2, s*d2:(s+1)*d2] = haar_unitary(d2, rng)
        C2[s*d2:(s+1)*d2, s*d2:(s+1)*d2] = haar_unitary(d2, rng)
    A = np.eye(n, dtype=complex)
    for i in range(L):
        for j in range(L):
            s = sid(i, j)
            # +x half-site of (i,j) paired with -x half-site of (i+1,j); +y with -y of (i,j+1)
            for (a, b) in ((s * d2 + 0, sid(i + 1, j) * d2 + 1), (s * d2 + 2, sid(i, j + 1) * d2 + 3)):
                A[np.ix_([a, b], [a, b])] = haar_unitary(2, rng)
    return C2 @ A @ C1


nbr = np.zeros((nsite, nsite), bool)
for i in range(L):
    for j in range(L):
        s = sid(i, j)
        for (di, dj) in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
            nbr[s, sid(i + di, j + dj)] = True

viol, total, worst_ex, worst_im2, beyond = 0, 0, -1.0, 0.0, 0.0
for rep in range(150):
    U = random_walk_2d()
    Ub = U.reshape(nsite, d2, nsite, d2)
    for x in range(nsite):
        for y in range(nsite):
            if not nbr[y, x]:
                beyond = max(beyond, float(np.abs(Ub[y, :, x, :]).max()))
    psi = rand_state(n, rng) if rep % 2 == 0 else np.eye(n)[rng.integers(n)].astype(complex)
    for t in range(4):
        P = (np.abs(psi.reshape(nsite, d2)) ** 2).sum(1)
        piMH, K, psin = mh_split(U, psi, nsite, d2)
        T, ex = rule_from_flow(piMH - piMH.T, P)
        total += 1
        worst_ex = max(worst_ex, ex)
        viol += ex > 1e-12
        worst_im2 = max(worst_im2, float(np.abs(K.imag - K.imag.T).max()))
        psi = psin
print(f"2D torus {L}x{L}, d=4 coin-hop-coin walks (max element beyond range 1 = {beyond:.1e}):")
print(f"   ticks tested = {total}; ticks where minimal MH rule breaks outflow bound = {viol}; "
      f"largest excess = {worst_ex:.3e}")
print(f"   max |Im K - Im K^T| (lambda-flow) in 2D     = {worst_im2:.3e}")
