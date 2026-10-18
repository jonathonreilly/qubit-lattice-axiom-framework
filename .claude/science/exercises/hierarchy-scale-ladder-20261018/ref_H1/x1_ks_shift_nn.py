"""Referee spot check X1 (HIER-1 (a)): one-component staggered (KS) surface, L=4 torus in d=4.
(1) KS operator commutes with the shift operators S_mu (chi(x) -> zeta_mu(x) chi(x+mu)),
    not with plain translations. zeta_mu(x) is a momentum-pi modulation.
(2) Space of on-site + nearest-neighbour operators commuting with all four S_mu (group
    average over S^n O S^-n). For random members: zero count and singular-value
    multiplicities. Expect: multiplicities divisible by 4 (taste); zero count never 1.
(3) Control: the vacuous orbit check of r1 lines 77-83.
"""
import itertools
import numpy as np

L, d = 4, 4
sites = list(itertools.product(range(L), repeat=d))
idx = {s: i for i, s in enumerate(sites)}
V = len(sites)
E = np.eye(d, dtype=int)


def sh(s, mu, n=1):
    t = list(s); t[mu] = (t[mu] + n) % L; return tuple(t)


eta = lambda s, mu: (-1) ** sum(s[:mu])
zeta = lambda s, mu: (-1) ** sum(s[mu + 1:])

D = np.zeros((V, V))
for s in sites:
    for mu in range(d):
        D[idx[s], idx[sh(s, mu, 1)]] += 0.5 * eta(s, mu)
        D[idx[s], idx[sh(s, mu, -1)]] -= 0.5 * eta(s, mu)

S = []
T = []
for mu in range(d):
    M = np.zeros((V, V)); P = np.zeros((V, V))
    for s in sites:
        M[idx[s], idx[sh(s, mu)]] = zeta(s, mu)
        P[idx[s], idx[sh(s, mu)]] = 1.0
    S.append(M); T.append(P)
print("[D,S_mu]=0:", [bool(np.allclose(D @ M, M @ D)) for M in S])
print("[D,T_mu]=0 (plain translation):", [bool(np.allclose(D @ P, P @ D)) for P in T])

# group average over n in Z_L^4 of S^n O S^-n
pows = [[np.linalg.matrix_power(S[mu], k) for k in range(L)] for mu in range(d)]
o = idx[(0,) * d]
basis_raw = [("onsite", o, o)]
for mu in range(d):
    basis_raw.append((f"fwd{mu}", o, idx[sh((0,) * d, mu, 1)]))
    basis_raw.append((f"bwd{mu}", o, idx[sh((0,) * d, mu, -1)]))
acc = [np.zeros((V, V)) for _ in basis_raw]
for n in itertools.product(range(L), repeat=d):
    W = pows[0][n[0]] @ pows[1][n[1]] @ pows[2][n[2]] @ pows[3][n[3]]
    for a, (name, i, j) in zip(acc, basis_raw):
        a += np.outer(W[:, i], W[:, j])
basis = []
for (name, i, j), A in zip(basis_raw, acc):
    ok = all(np.allclose(A @ M, M @ A) for M in S)
    nz = np.abs(A).max() > 1e-12
    if nz:
        basis.append(A)
    print(f"basis {name}: nonzero={nz} commutes={ok}")
print("dim of S-invariant on-site+NN space:", np.linalg.matrix_rank(np.array([b.ravel() for b in basis])))

rng = np.random.default_rng(11)
for trial in range(6):
    c = rng.standard_normal(len(basis)) + (1j * rng.standard_normal(len(basis)) if trial % 2 else 0)
    if trial >= 4:  # massless kinetic + small perturbation of the other directions
        c = np.zeros(len(basis), complex); c[1:] = rng.standard_normal(len(basis) - 1) * 0.3
    A = sum(ci * b for ci, b in zip(c, basis))
    sv = np.sort(np.linalg.svd(A, compute_uv=False))
    nzero = int(np.sum(sv < 1e-9))
    # multiplicities of singular values
    groups = []
    cur = [sv[0]]
    for x in sv[1:]:
        if abs(x - cur[-1]) < 1e-8:
            cur.append(x)
        else:
            groups.append(len(cur)); cur = [x]
    groups.append(len(cur))
    print(f"trial {trial}: zero singular values {nzero}; multiplicities all divisible by 4: {all(g % 4 == 0 for g in groups)}; min mult {min(groups)}")

# (3) r1 lines 77-83 reproduce: orbit of the zero vector under linear maps
orbit0 = {tuple((np.zeros(4)[list(p)] * np.array(sg)).tolist()) for p in itertools.permutations(range(4)) for sg in itertools.product((1, -1), repeat=4)}
print("r1 orbit check is vacuous (zero vector under any linear map):", orbit0 == {(0.0,) * 4})
# the shift S_mu multiplies by zeta_mu(x) = exp(i pi sum_{nu>mu} x_nu): a momentum boost by pi sum_{nu>mu} e_nu
print("zeta_mu as momentum boost vectors:", [tuple(int(nu > mu) for nu in range(d)) for mu in range(d)])
