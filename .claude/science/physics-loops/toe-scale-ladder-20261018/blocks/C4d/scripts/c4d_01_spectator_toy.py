"""C4d-01: sanity check of the spectator lemma on an explicit U(1) automorphism with frozen
single magnons and NON-trivial pair dynamics (1D ring, not translation invariant: the lemma
does not need TI or any symmetry, only frozen singles and finite range).

Spectator lemma (proved in NOTE): if alpha(s+_w)|0> = e^{i phi}|w> for all w and alpha(s+_x) is
supported in B_r(x), then for any cluster C and any w with dist(w,C) > r:
    U |C u {w}> = e^{i phi} (U|C>) (x) |w>.
Toy: U = V D V^dag, V = XY rotations on even bonds, D = exp(i phi sum n_x n_{x+1}).
"""
import itertools
import numpy as np
from c4d_common import check, total

L = 10
dim = 2 ** L


def bit(s, i):
    return (s >> i) & 1


def op_on(site_ops):
    """dense operator from dict site->2x2"""
    M = np.array([[1.0 + 0j]])
    for i in reversed(range(L)):
        M = np.kron(M, site_ops.get(i, np.eye(2)))
    return M


# basis index s: bit i = occupation of site i (1 = magnon)
sp = np.array([[0, 0], [1, 0]], complex)  # |0>->|1>
th, ph = 0.7, 1.1
# two-site XY gate in basis |n_i n_j>
G = np.eye(4, dtype=complex)
c, s_ = np.cos(th), np.sin(th)
# states 01 and 10 (index = n_i + 2 n_j)
G[1, 1] = c; G[2, 2] = c; G[1, 2] = -1j * s_; G[2, 1] = -1j * s_


def apply_two(psi, i, j, G):
    psi = psi.reshape([2] * L)  # axis k corresponds to site L-1-k
    ai, aj = L - 1 - i, L - 1 - j
    psi = np.moveaxis(psi, [ai, aj], [0, 1]).reshape(4, -1)
    # index n_i + 2 n_j  -> reorder: our reshape gives index 2*n_i + n_j
    Gp = np.zeros((4, 4), complex)
    for a in range(4):
        for b in range(4):
            ni, nj = a & 1, a >> 1
            mi, mj = b & 1, b >> 1
            Gp[2 * ni + nj, 2 * mi + mj] = G[a, b]
    psi = (Gp @ psi).reshape([2, 2] + [2] * (L - 2))
    psi = np.moveaxis(psi, [0, 1], [ai, aj]).reshape(-1)
    return psi


Ddiag = np.array([np.exp(1j * ph * sum(bit(s, i) * bit(s, (i + 1) % L) for i in range(L))) for s in range(dim)])


def V(psi, dag=False):
    g = G.conj().T if dag else G
    for i in range(0, L, 2):
        psi = apply_two(psi, i, i + 1, g)
    return psi


def U(psi):
    return V(Ddiag * V(psi, dag=True))


Umat = np.zeros((dim, dim), complex)
for s in range(dim):
    e = np.zeros(dim, complex); e[s] = 1
    Umat[:, s] = U(e)
check("U unitary", np.allclose(Umat.conj().T @ Umat, np.eye(dim)))
Nop = np.array([bin(s).count("1") for s in range(dim)])
check("U conserves magnon number", np.allclose(Umat * (Nop[:, None] - Nop[None, :]), 0))


def ket(sites):
    v = np.zeros(dim, complex); v[sum(1 << i for i in sites)] = 1; return v


singles = all(np.allclose(Umat @ ket([x]), ket([x])) for x in range(L))
check("single magnons frozen exactly (phase 1)", singles)
pairs_moved = max(1 - abs(np.vdot(ket([x, y]), Umat @ ket([x, y]))) for x, y in itertools.combinations(range(L), 2))
check("pair dynamics is non-trivial (lemma not vacuous)", pairs_moved > 0.1, f"max 1-|<xy|U|xy>| = {pairs_moved:.3f}")

# range: support of alpha(s+_x) = U s+_x U^dag ; site y in support iff it fails to commute with
# some Pauli at y
Ps = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]).astype(complex)]


def ring(a, b):
    d = abs(a - b) % L
    return min(d, L - d)


r_eff = 0
for x in [0, 1]:
    A = Umat @ op_on({x: sp}) @ Umat.conj().T
    for y in range(L):
        nontriv = any(not np.allclose(A @ op_on({y: P}), op_on({y: P}) @ A) for P in Ps)
        if nontriv:
            r_eff = max(r_eff, ring(x, y))
print("effective range r =", r_eff)
check("finite range r <= 3", r_eff <= 3, f"r = {r_eff}")

ok_all, ncase = True, 0
fail_near = 0
for k in (2, 3):
    for C in itertools.combinations(range(L), k):
        UC = Umat @ ket(list(C))
        for w in range(L):
            if w in C:
                continue
            dw = min(ring(w, c) for c in C)
            lhs = Umat @ ket(list(C) + [w])
            # (U|C>) (x) |w> : add magnon at w to every component (U|C> has no amplitude at w if dw>r)
            rhs = np.zeros(dim, complex)
            for s in np.nonzero(np.abs(UC) > 1e-13)[0]:
                if bit(s, w):
                    rhs = None; break
                rhs[s | (1 << w)] += UC[s]
            good = rhs is not None and np.allclose(lhs, rhs, atol=1e-11)
            if dw > r_eff:
                ncase += 1
                ok_all &= good
            elif not good:
                fail_near += 1
check("spectator lemma: U|C+w> = U|C> (x) |w> for all |C| in {2,3}, dist(w,C) > r", ok_all, f"{ncase} cases")
check("control: the identity FAILS for some spectator at dist <= r (test is discriminating)", fail_near > 0,
      f"{fail_near} near cases differ")
total()
