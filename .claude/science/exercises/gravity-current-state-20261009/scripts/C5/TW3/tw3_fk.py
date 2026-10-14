"""TW-3 probe (a): the Fidkowski-Kitaev cluster of 8 Majoranas with the Spin(7)-invariant
(Cayley-form) quartic.  Checks: Spin(7) commutant, no invariant bilinear (Spin(7) and T
separately), unique gapped ground state, vanishing bilinear expectations.
Also the Z8 count: for nu = 2,4,6,8 Majoranas, T^2, [T,P], and the minimum ground-state
degeneracy over random T-invariant even Hamiltonians."""
import itertools
import numpy as np
from tw3_lib import Maj, cayley_terms

np.set_printoptions(precision=6, suppress=True, linewidth=150)
rng = np.random.default_rng(20261014)


def dense(M):
    return M.toarray()


def build_T(mj):
    """U with U conj(gamma_a) U^dag = gamma_a for all a (T = U K)."""
    n = mj.nq
    G = [dense(mj.mat(a)) for a in range(2 * n)]
    U = np.eye(mj.dim, dtype=complex)
    for j in range(n):
        U = U @ G[2 * j]
    P = np.diag(mj.parity()).astype(complex)
    for cand in (U, U @ P):
        if all(np.allclose(cand @ G[a].conj() @ cand.conj().T, G[a]) for a in range(2 * n)):
            return cand, G, P
    raise RuntimeError("no T")


# ---------------- (a) FK cluster ----------------
mj = Maj(4)
terms = cayley_terms()
print("Cayley terms (14):", terms)
G = [dense(mj.mat(a)) for a in range(8)]
# Clifford check
cl = max(np.abs(G[a] @ G[b] + G[b] @ G[a] - 2 * (a == b) * np.eye(16)).max() for a in range(8) for b in range(8))
print("Clifford residual:", cl)


def omega(sign_dual=+1):
    H = np.zeros((16, 16), complex)
    for k, (t, s) in enumerate(terms):
        s2 = s if k < 7 else s * sign_dual
        M = G[t[0]] @ G[t[1]] @ G[t[2]] @ G[t[3]]
        H += s2 * M
    return H


pairs = list(itertools.combinations(range(8), 2))
B = [1j * G[a] @ G[b] for (a, b) in pairs]   # Hermitian so(8) generators (x2)


def commutant_dim(H, ops, tol=1e-10):
    A = np.array([(o @ H - H @ o).ravel() for o in ops]).T
    s = np.linalg.svd(A, compute_uv=False)
    null = np.sum(s < tol * max(1, s.max()))
    return null, s


for sd in (+1, -1):
    Om = omega(sd)
    herm = np.abs(Om - Om.conj().T).max()
    nd, _ = commutant_dim(Om, B)
    ev = np.linalg.eigvalsh(Om)
    print(f"sign_dual={sd:+d}: herm res {herm:.1e}; so(8) commutant dim = {nd}; Omega spectrum:",
          np.unique(np.round(ev, 8), return_counts=True))

# choose sign giving 21-dim commutant; H = -W*Omega with W=1 chosen so ground state is the singlet
Om = omega(+1)
nd, _ = commutant_dim(Om, B)
if nd != 21:
    Om = omega(-1)
nd, _ = commutant_dim(Om, B)
assert nd == 21, nd
# extract Spin(7) generators (null space)
A = np.array([(o @ Om - Om @ o).ravel() for o in B]).T
u, s, vh = np.linalg.svd(A)
null = vh[-21:].conj()
gens = [sum(c * o for c, o in zip(v, B)) for v in null]
# make them Hermitian combos (coefficients should be real up to phase)
gens = [(g + g.conj().T) / 2 for g in gens]
print("Spin(7) generators: count", len(gens), " max ||[g,Omega]|| =",
      max(np.abs(g @ Om - Om @ g).max() for g in gens))
# closure check: the 21 span a Lie algebra (commutators lie in span)
span = np.array([g.ravel() for g in gens]).T
Q, _ = np.linalg.qr(span)
res = 0
for g1, g2 in itertools.combinations(gens, 2):
    c = (g1 @ g2 - g2 @ g1).ravel()
    res = max(res, np.linalg.norm(c - Q @ (Q.conj().T @ c)))
print("Lie closure residual of the 21:", f"{res:.1e}")

# bilinears invariant under Spin(7): centralizer of the 21 in so(8)
A2 = np.concatenate([np.array([(o @ g - g @ o).ravel() for o in B]).T for g in gens], axis=0)
s2 = np.linalg.svd(A2, compute_uv=False)
print("Spin(7)-invariant bilinears: dimension", int(np.sum(s2 < 1e-10)), "; smallest sing. value", f"{s2.min():.3f}")

# T
U, G_, P = build_T(mj)
print("T: U U* =", np.round((U @ U.conj())[0, 0], 6), "(T^2 sign);  U P* U^dag = s P with s =",
      np.round(np.vdot(P.ravel(), (U @ P.conj() @ U.conj().T).ravel()) / 16, 6))
for sd_H in (+1, -1):
    pass
H = +Om
print("T-invariance of H: ||U H* U^dag - H|| =", f"{np.abs(U @ H.conj() @ U.conj().T - H).max():.1e}")
# T-invariant bilinears: i g_a g_b -> U (i g_a g_b)* U^dag
todd = max(np.abs(U @ b.conj() @ U.conj().T + b).max() for b in B)
print("every bilinear i g_a g_b is T-odd: max ||T b T^-1 + b|| =", f"{todd:.1e}")

# spectrum, ground state
for W in (1.0,):
    ev, vec = np.linalg.eigh(W * Om)
    vals, cnt = np.unique(np.round(ev, 8), return_counts=True)
    print(f"H = +W*Omega, W={W}: levels", vals, "mult", cnt)
    g0 = vec[:, 0]
    print("  ground degeneracy:", int(np.sum(np.abs(ev - ev[0]) < 1e-9)), " gap:", ev[np.abs(ev - ev[0]) > 1e-9][0] - ev[0])
    print("  ground parity:", np.round(np.vdot(g0, P @ g0).real, 10))
    cas = sum(g @ g for g in gens)
    print("  Spin(7) Casimir on ground state:", f"{np.vdot(g0, cas @ g0).real:.2e}")
    bil = max(abs(np.vdot(g0, b @ g0)) for b in B)
    print("  max |<i g_a g_b>| in ground state:", f"{bil:.1e}")
    # single-fermion excitation: gamma_a |g0>
    odd = vec[:, np.abs(np.diag(vec.conj().T @ P @ vec) + 1) < 1e-8]
    eodd = np.sort(np.real(np.diag(odd.conj().T @ (W * Om) @ odd)))
    print("  lowest odd-parity energy - E0 (single-fermion gap):", eodd[0] - ev[0])
    # one-particle Green function at omega: G_ab(iw) = sum_n ...; at w=0 must vanish (T)
    E0 = ev[0]
    Gw0 = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            for n in range(16):
                dE = ev[n] - E0
                if dE < 1e-9:
                    continue
                Aab = np.vdot(g0, G[a] @ vec[:, n]) * np.vdot(vec[:, n], G[b] @ g0)
                Aba = np.vdot(g0, G[b] @ vec[:, n]) * np.vdot(vec[:, n], G[a] @ g0)
                Gw0[a, b] += (Aba - Aab) / dE   # G_ab(i w = 0), Majorana convention
    print("  G_ab(omega=0), all 64 entries (the mass channel): max |G| =", f"{np.abs(Gw0).max():.1e}")
    # G(iw) at small w: G_aa ~ -2 i w Z/Delta^2 (propagator zero, no pole at 0)
    w = 1e-3
    Gaa = 0
    for n in range(16):
        dE = ev[n] - E0
        if dE < 1e-9: continue
        A = abs(np.vdot(g0, G[0] @ vec[:, n]))**2
        Gaa += A / (1j * w - dE) + A / (1j * w + dE)
    print("  G_00(i w=1e-3) =", np.round(Gaa, 9), "(linear in w: a zero at w=0, i.e. no bilinear mass pole)")

# controls: a Spin(7)-breaking and T-breaking bilinear added
m = 0.1
ev_c, vec_c = np.linalg.eigh(Om + m * 1j * G[0] @ G[1])
g0c = vec_c[:, 0]
print("control (+0.1 i g0 g1, T- and Spin(7)-breaking): <i g0 g1> =",
      f"{np.vdot(g0c, 1j * G[0] @ G[1] @ g0c).real:.4e}")

# ---------------- Z8 count ----------------
print("\nZ8 count: nu Majoranas, T = U K with T g T^-1 = g")
for nu in (2, 4, 6, 8):
    m2 = Maj(nu // 2)
    U2, G2, P2 = build_T(m2)
    t2 = np.round((U2 @ U2.conj())[0, 0].real, 6)
    sP = np.round(np.vdot(P2.ravel(), (U2 @ P2.conj() @ U2.conj().T).ravel()).real / m2.dim, 6)
    # T-invariant Hermitian even operators: real combinations of strings of length 4k
    strings = []
    for L in range(4, nu + 1, 4):
        for idx in itertools.combinations(range(nu), L):
            M = np.eye(m2.dim, dtype=complex)
            for a in idx:
                M = M @ G2[a]
            strings.append(M)
    mindeg = None
    nsamp = 200 if strings else 1
    for _ in range(nsamp):
        Hr = np.zeros((m2.dim, m2.dim), complex)
        for M in strings:
            Hr += rng.normal() * M
        assert np.abs(Hr - Hr.conj().T).max() < 1e-12
        assert np.abs(U2 @ Hr.conj() @ U2.conj().T - Hr).max() < 1e-12
        ev2 = np.linalg.eigvalsh(Hr)
        deg = int(np.sum(np.abs(ev2 - ev2[0]) < 1e-9))
        mindeg = deg if mindeg is None else min(mindeg, deg)
    print(f"  nu={nu}: dim {m2.dim}, T^2={t2:+.0f}, T P T^-1 = {sP:+.0f} P, #T-even strings {len(strings)},"
          f" min ground degeneracy over {nsamp} random T-symmetric H: {mindeg}")
