"""T09 Test 3: inside the ONE covariant six-direction coin algebra C = eA PA + eE PE + eT PT,
compare row-stochastic (nonnegative) members with unitary members.  Plus 1D Kac telegraph vs Dirac walk."""
import numpy as np
from common import *

# six-direction permutation rep of the 24 rotations, and its isotypic projectors
def perm_rep(R):
    P = np.zeros((6, 6))
    for i, v in enumerate(DIRS):
        P[dir_index(R @ v), i] = 1
    return P
reps6 = [perm_rep(R) for R in ROTS]
# commutant basis: I (same), Rev (back), Side (4 perpendicular)
I6 = np.eye(6)
Rev = np.zeros((6, 6)); Side = np.zeros((6, 6))
for i, v in enumerate(DIRS):
    for j, w in enumerate(DIRS):
        d = v @ w
        if np.isclose(d, -1): Rev[j, i] = 1
        elif np.isclose(d, 0): Side[j, i] = 1
# commutation check
for P in reps6:
    for M in (Rev, Side):
        assert np.allclose(P @ M, M @ P)
# eigenvalues of Rev, Side on A,E,T
ev = {}
Pa = np.ones((6, 6)) / 6
# even/odd combos
odd = np.zeros((6, 3)); even = np.zeros((6, 3))
for i in range(3):
    odd[2 * i, i] = 1 / np.sqrt(2); odd[2 * i + 1, i] = -1 / np.sqrt(2)
    even[2 * i, i] = 1 / np.sqrt(2); even[2 * i + 1, i] = 1 / np.sqrt(2)
Pt = odd @ odd.T
Pe = even @ even.T - Pa
print('eigenvalues (A, E, T) of  I:  1,1,1 ; Rev:',
      [round(float(np.trace(Rev @ P) / np.trace(P)), 6) for P in (Pa, Pe, Pt)],
      '; Side:', [round(float(np.trace(Side @ P) / np.trace(P)), 6) for P in (Pa, Pe, Pt)])
assert np.allclose(Pa + Pe + Pt, I6)

def D_of_k(k):
    return np.diag([np.exp(1j * (k @ v)) for v in DIRS])

def U_of(C, k):
    return D_of_k(k) @ C

rng = np.random.default_rng(11)

# ---- stochastic members: C = m_same I + m_back Rev + m_side Side, entries >= 0, row sums 1 ----
print('\n--- stochastic (nonnegative) members: is there any undamped, non-rigid branch? ---')
def scan_stochastic(msame, mback, mside, ngrid=13):
    C = msame * I6 + mback * Rev + mside * Side
    assert np.allclose(C.sum(axis=0), 1) and np.allclose(C.sum(axis=1), 1)
    g = np.linspace(-np.pi, np.pi, ngrid)
    worst_rho = 0
    rho_arr = []
    for kx in g:
        for ky in g:
            for kz in g:
                k = np.array([kx, ky, kz])
                if np.linalg.norm(k) < 1e-9:
                    continue
                lam = np.linalg.eigvals(U_of(C, k))
                rho_arr.append(max(abs(lam)))
    return max(rho_arr), np.mean(np.array(rho_arr) > 1 - 1e-9)

# sample the simplex m_same + m_back + 4 m_side = 1
samples = []
for _ in range(400):
    w = rng.dirichlet([1, 1, 1])
    msame, mback, mside = w[0], w[1], w[2] / 4
    samples.append((msame, mback, mside))
# add edge cases
samples += [(1, 0, 0), (0, 1, 0), (0, 0, .25), (.5, .5, 0), (0.7, 0.2, 0.025), (0.001, 0.001, (1 - 0.002) / 4)]
maxrho_interior = 0; frac_unit = []
undamped_cases = []
for (a, b, c) in samples:
    r, frac = scan_stochastic(a, b, c, ngrid=9)
    # k with a zero component decouples streams if c=0 -> eigenvalue 1 flat at partial-zero-k; exclude c==0 cases from 'coupled'
    if c > 1e-9:
        maxrho_interior = max(maxrho_interior, r)
    if frac > 0:
        undamped_cases.append((a, b, c, r, frac))
print('coupled stochastic members (m_side>0) sampled:', sum(1 for s in samples if s[2] > 1e-9),
      ' max spectral radius over k != 0 grid (9^3):', maxrho_interior)
# The grid includes k with pi components: cyclic (bipartite) chain has |lam|=1 at k=(pi,pi,pi) only when m_same=0
print('cases with |lambda| = 1 at some grid k != 0 (a,b,c,rho,frac_of_k):')
for u in undamped_cases[:12]:
    print('   ', tuple(round(x, 4) for x in u))
print('  count', len(undamped_cases), 'of', len(samples))

# In those cases, is the undamped point isolated (a flat/edge artifact) or a dispersive branch on an open set?
def unit_branch_measure(C, npts=4000):
    cnt = 0
    for _ in range(npts):
        k = rng.uniform(-np.pi, np.pi, 3)
        lam = np.linalg.eigvals(U_of(C, k))
        if max(abs(lam)) > 1 - 1e-7:
            cnt += 1
    return cnt / npts
print('\nfraction of random k (open-set test) with an undamped branch, stochastic members with m_side>0 and m_same,m_back<1:')
fr = []
for (a, b, c) in samples[:60]:
    if c > 1e-9 and a < 1 - 1e-9 and b < 1 - 1e-9:
        fr.append(unit_branch_measure(a * I6 + b * Rev + c * Side, 800))
print('   max over sampled members:', max(fr))

# ---- unitary members ----
print('\n--- unitary members C = eA PA + eE PE + eT PT (phases) ---')
def dispersion(alpha, beta, gamma, direction, ks):
    C = np.exp(1j * alpha) * Pa + np.exp(1j * beta) * Pe + np.exp(1j * gamma) * Pt
    assert np.allclose(C.conj().T @ C, I6)
    out = []
    for t in ks:
        k = t * np.array(direction, float) / np.linalg.norm(direction)
        lam = np.linalg.eigvals(U_of(C, k))
        out.append(np.sort(np.angle(lam)))
    return np.array(out)
ks = np.array([0.02, 0.04])
for name, (al, be, ga) in {'Grover (1,-1,-1 phases -> real -Grover)': (0, np.pi, np.pi), 'A=T (alpha=gamma=0), E=pi/2': (0, np.pi / 2, 0), 'A,T split (alpha=0,gamma=0.6), E=pi/2': (0, np.pi / 2, 0.6)}.items():
    print(name)
    for direction in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        d = dispersion(al, be, ga, direction, ks)
        # eigenphase shifts relative to k=0
        d0 = dispersion(al, be, ga, direction, np.array([0.0]))[0]
        print('   dir', direction, 'phases at k=0:', np.round(d0, 4), ' at k=0.02:', np.round(d[0], 4))
