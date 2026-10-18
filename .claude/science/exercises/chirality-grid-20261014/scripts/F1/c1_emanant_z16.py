"""F1 check C1: emanant Spin-Z4 subgroups of lattice translations on the framework's free carriers,
and their Z16 indices on whole carriers and candidate mirror sectors.  See ../PREREG_C1.md.

Conventions
- Chirality: on a node, H ~ sum_mu k_mu Gamma_mu.  chi = -i Gamma1 Gamma2 Gamma3 (Hermitian, +-1).
  chi = +1 <=> Gamma ~ +sigma (right-handed, H = +sigma.k); chi = -1 left-handed.
- A symmetry g' with g'^2 = -1 on single-particle zero modes (i.e. g'^2 = (-1)^F) generates Spin-Z4.
  Left-handed charge q: L mode with g'-eigenvalue lam -> q = lam/i ; R mode -> its conjugate is left-handed
  with eigenvalue conj(lam) -> q = conj(lam)/i.  nu = sum_(Weyl) q  (each Weyl = 2-dim spin block), mod 16.
  (Garcia-Etxebarria--Montero 1808.00009: Omega_5^{Spin x_Z2 Z4} = Z16, nu = n_{q=1} - n_{q=3}.)
- If g^2 = +1 we use g' = i g, which is g * i^F on Fock space and needs fermion number conserved mod 4.
"""
import numpy as np, itertools
np.set_printoptions(precision=3, suppress=True)

# ---------------- (S) 3D Hamiltonian staggered field, K2a conventions -----------------
def cell_ops(d=3):
    C = list(itertools.product((0, 1), repeat=d)); ci = {c: i for i, c in enumerate(C)}; n = len(C)
    def eta(mu, x): return (-1) ** sum(x[:mu])
    def Hk(k):
        H = np.zeros((n, n), complex)
        for c in C:
            for mu in range(d):
                y = list(c); y[mu] += 1; wrap = y[mu] // 2; y[mu] %= 2
                amp = 0.5j * eta(mu, c) * np.exp(2j * k[mu] * wrap)
                H[ci[c], ci[tuple(y)]] += amp; H[ci[tuple(y)], ci[c]] += np.conj(amp)
        return H
    def Tk(mu, k):  # unit shift x->x+mu with frame zeta_mu(x) = (-1)^{x_{mu+1}+...}
        T = np.zeros((n, n), complex)
        for c in C:
            y = list(c); y[mu] += 1; wrap = y[mu] // 2; y[mu] %= 2
            T[ci[tuple(y)], ci[c]] = (-1) ** sum(c[mu + 1:]) * np.exp(-2j * k[mu] * wrap)
        return T
    return n, Hk, Tk

def nu_table(chi, gprime, sector_mask=None):
    """chi: Hermitian chirality (+-1) on zero-mode space; gprime: unitary commuting with chi, gprime^2=-1.
    Returns nu per unit internal multiplicity, restricted to chirality sector(s) in sector_mask."""
    w, v = np.linalg.eigh(chi)
    nu = 0.0; dims = {}
    for s in (+1, -1):
        if sector_mask is not None and s not in sector_mask: continue
        P = v[:, np.isclose(w, s)]
        gb = P.conj().T @ gprime @ P
        lam = np.linalg.eigvals(gb)
        assert np.allclose(np.abs(lam), 1) and np.allclose(lam.real, 0, atol=1e-9), lam
        for l in (1j, -1j):
            m = int(np.sum(np.isclose(lam, l)))
            assert m % 2 == 0, ("odd eigenspace", s, l, m)
            nweyl = m // 2
            q = (l / 1j) if s == -1 else (np.conj(l) / 1j)   # left-handed charge
            nu += q.real * nweyl
            dims[(s, l)] = nweyl
    return int(round(nu)), dims

out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

P("=== (S) staggered field, 3D Hamiltonian, K2a conventions; zero modes at K=0 (8-dim cell) ===")
n, Hk, Tk = cell_ops(3); k0 = np.zeros(3); h = 1e-6
G = [(Hk(np.eye(3)[m] * h) - Hk(-np.eye(3)[m] * h)) / (2 * h) for m in range(3)]
X = -1j * G[0] @ G[1] @ G[2]
P("chi Hermitian:", np.allclose(X, X.conj().T), " chi^2=1:", np.allclose(X @ X, np.eye(n)),
  " eigen:", np.round(np.linalg.eigvalsh((X + X.conj().T) / 2), 3))
T = [Tk(m, k0) for m in range(3)]
for m in range(3):
    P(f"T{m+1}^2 = {'+1' if np.allclose(T[m]@T[m], np.eye(n)) else ('-1' if np.allclose(T[m]@T[m], -np.eye(n)) else 'other')};"
      f" [T{m+1},chi]={np.abs(T[m]@X-X@T[m]).max():.1e}; max|[T{m+1},Gamma]|={max(np.abs(T[m]@g-g@T[m]).max() for g in G):.1e};"
      f" [T{m+1},H(k)] at random k = {np.abs(Tk(m,np.array([.3,.7,-.4]))@Hk(np.array([.3,.7,-.4]))-Hk(np.array([.3,.7,-.4]))@Tk(m,np.array([.3,.7,-.4]))).max():.1e}")
for a, b in [(0, 1), (0, 2), (1, 2)]:
    P(f"{{T{a+1},T{b+1}}} = {np.abs(T[a]@T[b]+T[b]@T[a]).max():.1e} ; [T{a+1},T{b+1}] = {np.abs(T[a]@T[b]-T[b]@T[a]).max():.1e}")

P("\nTranslation elements g = T^v (v in {0,1}^3, ordered product T1^v1 T2^v2 T3^v3):")
P("  g^2 | needs Z4^F? | nu_whole per field | nu_(chi=-1 sector) | nu_(chi=+1 sector) | Weyl dims (chi, eig)")
stag_rows = []
for v in itertools.product((0, 1), repeat=3):
    g = np.eye(n, dtype=complex)
    for m in range(3):
        if v[m]: g = g @ T[m]
    g2 = g @ g
    if np.allclose(g2, -np.eye(n)): gp, needs = g, "no ((-1)^F suffices)"; sq = "-1"
    elif np.allclose(g2, np.eye(n)): gp, needs = 1j * g, "yes (uses i^F)"; sq = "+1"
    else: P(" ", v, "g^2 not +-1"); continue
    nw, dw = nu_table(X, gp); nL, _ = nu_table(X, gp, (-1,)); nR, _ = nu_table(X, gp, (+1,))
    stag_rows.append((v, sq, needs, nw, nL, nR))
    P(f"  v={v}: g^2={sq} | {needs} | {nw} | {nL} | {nR} | {dw}")

# ---------------- (W) walker H = sum_a sigma_a sin p_a on the site qubit -----------------
P("\n=== (W) walker H = sum_a sigma_a sin p_a; nodes n in {0,1}^3 (p = pi n) ===")
nodes = list(itertools.product((0, 1), repeat=3))
chi_n = {nd: (-1) ** sum(nd) for nd in nodes}     # det of velocity diag((-1)^{n_a})
P("chirality (-1)^|n| (+1 = R):", {nd: chi_n[nd] for nd in nodes})
def walker_nu(sector, v):
    # g = T^v plain translation: eigenvalue (-1)^{n.v} on node n; g^2=+1 -> g' = i g (needs Z4^F)
    nu = 0
    for nd in sector:
        s = (-1) ** int(np.dot(nd, v)); lam = 1j * s
        q = (lam / 1j) if chi_n[nd] == -1 else (np.conj(lam) / 1j)
        nu += int(round(q.real))      # one Weyl (2-dim spin) per node per internal component
    return nu
hw = lambda k: [nd for nd in nodes if sum(nd) == k]
sectors_W = {"whole (8 nodes)": nodes,
             "mirror S={hw0,hw2,hw3} (hw1=3 light gens)": hw(0) + hw(2) + hw(3),
             "light hw1": hw(1),
             "mirror chirality split {hw0,hw2}": hw(0) + hw(2)}
walk_rows = {}
for name, sec in sectors_W.items():
    row = {v: walker_nu(sec, v) for v in nodes}
    walk_rows[name] = row
    P(f"  {name}: nu_v per internal component =", row)

# ---------------- verdict tables over internal multiplicity d -----------------
P("\n=== nu mod 16 by internal multiplicity d (necessary conditions for symmetric gapping) ===")
ds = (1, 2, 4, 8, 15, 16)
def fails(nus, d): return [x for x in nus if (x * d) % 16 != 0]
stag_whole = [r[3] for r in stag_rows]; stag_mir = [r[5] for r in stag_rows]; stag_mirL = [r[4] for r in stag_rows]
P("(S) whole carrier, per field:", {d: ('ok' if not fails(stag_whole, d) else 'OBSTRUCTED') for d in ds},
  " | control |nu_Z|=4 per field:", abs([r for r in stag_rows if r[0] == (1, 1, 1)][0][3]) % 16 == 4)
P("(S) K2a mirror = chi=+1 sector:", {d: ('ok' if not fails(stag_mir, d) else 'OBSTRUCTED') for d in ds})
P("(S) K2a mirror = chi=-1 sector:", {d: ('ok' if not fails(stag_mirL, d) else 'OBSTRUCTED') for d in ds})
for name, row in walk_rows.items():
    P(f"(W) {name}:", {d: ('ok' if not fails(list(row.values()), d) else 'OBSTRUCTED') for d in ds})

open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
