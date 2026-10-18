"""R1 / T1: localisation family on the qubit lattice.

A. Transitivity lemma: transitive unitary symmetry => flat gear weights
   (non-degenerate modes) or flat summed weights (degenerate multiplets).
B. Orientation lemma: bond reversal kills one-ended protected localisation
   (clockwork, Hatano-Nelson skin).
C. Two-wall splitting (allowed by reflection): Wilson-Dirac qubit chain.
D. Named-number arithmetic.
Pure numpy; small matrices only.
"""
import itertools
import numpy as np

rng = np.random.default_rng(20261018)
TARGET = 2.0e-17                      # v / M_Pl
LNT = np.log(1.0 / TARGET)            # 38.45
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)


def multiplets(evals, tol=1e-8):
    order = np.argsort(evals)
    groups, cur = [], [order[0]]
    for a, b in zip(order[:-1], order[1:]):
        if abs(evals[b] - evals[a]) < tol:
            cur.append(b)
        else:
            groups.append(cur)
            cur = [b]
    groups.append(cur)
    return groups


def weight_check(H, nsite, dint, label):
    e, V = np.linalg.eigh(H)
    groups = multiplets(e)
    dev_nd, dev_mult, n_nd = 0.0, 0.0, 0
    for g in groups:
        W = np.zeros(nsite)
        for i in g:
            psi = V[:, i].reshape(nsite, dint)
            W += np.sum(np.abs(psi) ** 2, axis=1)
        flat = len(g) / nsite
        d = np.max(np.abs(W - flat)) / flat
        if len(g) == 1:
            n_nd += 1
            dev_nd = max(dev_nd, d)
        dev_mult = max(dev_mult, d)
    print(f"[A] {label}: dim={H.shape[0]} multiplets={len(groups)} "
          f"non-degenerate={n_nd} max rel dev (non-deg)={dev_nd:.2e} "
          f"max rel dev (all multiplets, summed)={dev_mult:.2e}")
    return dev_nd, dev_mult


# ---------------- A1: ring, translations only, qubit per site -------------
L = 24
A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); A = A + A.conj().T
B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
H = np.zeros((2 * L, 2 * L), complex)
for j in range(L):
    H[2*j:2*j+2, 2*j:2*j+2] += A
    k = (j + 1) % L
    H[2*k:2*k+2, 2*j:2*j+2] += B
    H[2*j:2*j+2, 2*k:2*k+2] += B.conj().T
resA1 = weight_check(H, L, 2, "ring L=24, translations only, random complex hop")


# ---------------- A2: 4^3 torus, translations x O, spin-1/2 internal ------
def rot_mats():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i, p in enumerate(perm):
                R[i, p] = signs[i]
            if round(np.linalg.det(R)) == 1:
                out.append(R)
    return out


def su2_of(R):
    # quaternion from rotation matrix (sign ambiguity irrelevant for conjugation)
    tr = np.trace(R)
    w = np.sqrt(max(0.0, 1 + tr)) / 2
    x = np.sqrt(max(0.0, 1 + R[0, 0] - R[1, 1] - R[2, 2])) / 2
    y = np.sqrt(max(0.0, 1 - R[0, 0] + R[1, 1] - R[2, 2])) / 2
    z = np.sqrt(max(0.0, 1 - R[0, 0] - R[1, 1] + R[2, 2])) / 2
    x = np.copysign(x, R[2, 1] - R[1, 2]) if w > 1e-9 else x
    y = np.copysign(y, R[0, 2] - R[2, 0]) if w > 1e-9 else y
    z = np.copysign(z, R[1, 0] - R[0, 1]) if w > 1e-9 else z
    if w <= 1e-9:  # angle pi: fix relative signs from off-diagonals
        if x > 1e-9:
            y = np.copysign(y, R[0, 1]); z = np.copysign(z, R[0, 2])
        elif y > 1e-9:
            z = np.copysign(z, R[1, 2])
    U = w * I2 - 1j * (x * sx + y * sy + z * sz)
    # verify it implements R on Pauli vectors: U s_i U^dag = sum_j R_ji s_j
    S = [sx, sy, sz]
    for i in range(3):
        lhs = U @ S[i] @ U.conj().T
        rhs = sum(R[j, i] * S[j] for j in range(3))
        assert np.allclose(lhs, rhs), "SU(2) lift failed"
    return U


Ls = 4
sites = list(itertools.product(range(Ls), repeat=3))
idx = {s: n for n, s in enumerate(sites)}
ns = len(sites)
H0 = np.zeros((2 * ns, 2 * ns), complex)
for s in sites:
    n = idx[s]
    a = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    H0[2*n:2*n+2, 2*n:2*n+2] += a + a.conj().T
    for mu in range(3):
        t = list(s); t[mu] = (t[mu] + 1) % Ls; m = idx[tuple(t)]
        b = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        H0[2*m:2*m+2, 2*n:2*n+2] += b
        H0[2*n:2*n+2, 2*m:2*m+2] += b.conj().T
Hs = np.zeros_like(H0)
rots = rot_mats()
assert len(rots) == 24
count = 0
for R in rots:
    U = su2_of(R)
    for tvec in sites:
        P = np.zeros((ns, ns))
        for s in sites:
            img = tuple(int((np.dot(R[i], s) + tvec[i]) % Ls) for i in range(3))
            P[idx[img], idx[s]] = 1
        Ug = np.kron(P, U)
        Hs += Ug @ H0 @ Ug.conj().T
        count += 1
Hs /= count
resA2 = weight_check(Hs, ns, 2, "4^3 torus, translations x proper cubic O, spin-1/2 internal")

# ---------------- A3: 2^4 block (2 x 2 x 2 x 2, APBC in time), qubit per site
blk = list(itertools.product(range(2), repeat=4))
bidx = {s: n for n, s in enumerate(blk)}
nb = len(blk)


def shift(mu):
    T = np.zeros((nb, nb))
    for s in blk:
        t = list(s); t[mu] = (t[mu] + 1) % 2
        sign = -1 if (mu == 3 and s[3] == 1) else 1   # APBC in time
        T[bidx[tuple(t)], bidx[s]] = sign
    return T


H0 = rng.normal(size=(2*nb, 2*nb)) + 1j * rng.normal(size=(2*nb, 2*nb))
H0 = H0 + H0.conj().T
Hb = np.zeros_like(H0); cnt = 0
for bits in itertools.product([0, 1], repeat=4):
    Tg = np.eye(nb)
    for mu, b in enumerate(bits):
        if b:
            Tg = shift(mu) @ Tg
    Ug = np.kron(Tg, I2)
    Hb += Ug @ H0 @ Ug.conj().T; cnt += 1
Hb /= cnt
resA3 = weight_check(Hb, nb, 2, "2^4 block, APBC time, block translations, qubit per site")

# ---------------- B: orientation ------------------------------------------
N, q = 20, 2.0
def clockwork(N, q, w):
    M = np.zeros((N + 1, N + 1))
    for j in range(N):
        v = np.zeros(N + 1); v[j] = 1; v[j+1] = -q
        M += np.outer(v, v)
        u = np.zeros(N + 1); u[j+1] = 1; u[j] = -q    # bond-reversed partner
        M += w * np.outer(u, u)
    return M

print(f"[B] clockwork chain N={N}, q={q}: q^-N = {q**-N:.3e}")
for w in [0.0, 1e-6, 1e-3, 1e-1, 1.0]:
    e, V = np.linalg.eigh(clockwork(N, q, w))
    z = V[:, 0]
    print(f"[B]   reversed-partner weight w={w:7.1e}: lambda_min={e[0]:.3e} "
          f"|phi_N/phi_0|={abs(z[-1]/z[0]):.3e}")

# Hatano-Nelson skin effect
Nh, g = 40, 0.3
for gg in [g, 0.0]:
    Hh = np.zeros((Nh, Nh))
    for j in range(Nh - 1):
        Hh[j+1, j] = np.exp(gg); Hh[j, j+1] = np.exp(-gg)
    e, V = np.linalg.eig(Hh)
    rates = []
    for i in range(Nh):
        a = np.abs(V[:, i])
        rates.append(np.log(a[-3:].mean() / a[:3].mean()) / (Nh - 3))
    print(f"[B] Hatano-Nelson g={gg}: mean log end-ratio per site = {np.mean(rates):+.4f} "
          f"(expected {gg:+.4f})")

# ---------------- C: two walls, Wilson-Dirac qubit chain -------------------
def wd_chain(Ntot, mvec, r=1.0):
    H = np.zeros((2*Ntot, 2*Ntot), complex)
    hop = -0.5 * (r * sz - 1j * sx)       # c_{j+1}^dag hop c_j
    for j in range(Ntot):
        H[2*j:2*j+2, 2*j:2*j+2] += (mvec[j] + r) * sz
        k = (j + 1) % Ntot
        H[2*k:2*k+2, 2*j:2*j+2] += hop
        H[2*j:2*j+2, 2*k:2*k+2] += hop.conj().T
    return H

Ntot = 160
for m0 in [0.25, 0.5, 0.75]:
    Ls_, dE = [], []
    for Lw in range(2, 41, 2):
        mvec = np.full(Ntot, m0); mvec[:Lw] = -m0
        e = np.linalg.eigvalsh(wd_chain(Ntot, mvec))
        e = np.sort(np.abs(e))
        Ls_.append(Lw); dE.append(e[0] + e[1])      # splitting of the wall pair
    Ls_ = np.array(Ls_); dE = np.array(dE)
    ok = (dE > 1e-13) & (Ls_ >= 6)
    sl, ic = np.polyfit(Ls_[ok], np.log(dE[ok]), 1)
    xi = -1 / sl
    Lstar = (ic - np.log(TARGET)) * xi
    print(f"[C] Wilson-Dirac m0={m0}, r=1: xi={xi:.3f} sites; "
          f"splitting(L=10)={dE[Ls_==10][0]:.2e}; L* for 2e-17 = {Lstar:.1f} sites")

# ---------------- D: named-number arithmetic -------------------------------
print(f"[D] ln(M_Pl/v) = {LNT:.2f}")
for ell, name in [(4, "taste geodesic (Hamming diameter)"), (15, "taste Hamiltonian path"),
                  (16, "16 links")]:
    print(f"[D] taste clockwork over {ell:2d} links ({name}): needs gear ratio q >= {TARGET**(-1/ell):.3g}")
aLM = (1/(4*np.pi)) / 0.5934**0.25
print(f"[D] alpha_LM = {aLM:.4f}; alpha_LM^16 = {aLM**16:.3e} (clockwork form q^-16 with q = {1/aLM:.2f})")
for qq in [2.0, np.e, 1/aLM]:
    print(f"[D] time clockwork, q={qq:.3f}: freeze at N_t* = {LNT/np.log(qq):.1f} ticks; "
          f"if not frozen, d ln v / d ln t = -N_t ln q (BBN needs |.| < ~1e-3)")
print("PASS-A" if max(resA1[0], resA2[1], resA3[1]) < 1e-10 else "FAIL-A")
