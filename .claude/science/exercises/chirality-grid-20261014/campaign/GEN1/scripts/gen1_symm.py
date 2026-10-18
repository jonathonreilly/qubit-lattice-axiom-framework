"""GEN-1 (a2), (a3), (a4) checks.  Rotation/spin-lift, filter and Fock code reused from X2's x2_cert.py (T2).
(a2) f_Gamma = (3 - sum cos k)/2: zeros, A1g covariance (L=4), Fock decoupling at Gamma (L=2, 16 modes).
(a3) cyclic Z16 gates nu_g for g.i^F over the 7-corner mirror; Spin(10) instanton 't Hooft-vertex phases.
(a4) little-group characters: does End(C^2) (or the pairing space C^2 x C^2) at a corner contain the traceless-strain
     rep E+T2 of the corner's little group?  Gamma (little group O) vs an hw1 corner (little group D4)."""
import numpy as np, itertools, sys, time
t0 = time.time()
def P(*a): print(*a); sys.stdout.flush()
C = list(itertools.product((0, 1), repeat=3)); hw = lambda c: sum(c)
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
def f_G(k): return (3 - np.cos(np.asarray(k, float)).sum()) / 2
Ks = lambda L: [np.array(k) * 2 * np.pi / L for k in itertools.product(range(L), repeat=3)]
def rotations():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3): R[perm[i], i] = sg[i]
            if round(np.linalg.det(R)) == 1: Rs.append(R)
    return Rs
ROT = rotations(); assert len(ROT) == 24
def spin_lift(R):
    A = []
    for a in range(3):
        sp = sum(R[b, a] * SIG[b] for b in range(3))
        A.append(np.kron(SIG[a].T, s0) - np.kron(s0, sp))
    A = np.vstack(A); _, sv, vh = np.linalg.svd(A)
    U = vh[-1].conj().reshape(2, 2, order="F"); U /= np.sqrt(np.linalg.det(U))
    for a in range(3): assert np.allclose(U @ SIG[a] @ U.conj().T, sum(R[b, a] * SIG[b] for b in range(3)))
    return U

# ---------------------------------------------------------------- (a2) filter
P("=== (a2) filter f_Gamma and exact decoupling at Gamma ===")
P("f_Gamma at corners:", {''.join(map(str, c)): round(f_G(np.pi * np.array(c)), 6) for c in C})
g = np.linspace(-np.pi, np.pi, 41); KK = np.array(list(itertools.product(g, repeat=3)))
fv = (3 - np.cos(KK).sum(axis=1)) / 2; dist = np.linalg.norm(KK, axis=1)
P(f"41^3 grid: min f_Gamma = {fv.min():.3e}; min f_Gamma at |k| > 0.3 = {fv[dist > 0.3].min():.3e}  (zero only at Gamma)")
L = 4; sites = list(itertools.product(range(L), repeat=3)); idx = {x: i for i, x in enumerate(sites)}; N = len(sites)
def kernel_op(fun):
    ks = Ks(L); fx = {x: sum(fun(k) * np.exp(1j * np.dot(k, x)) for k in ks) / N for x in sites}
    F = np.zeros((N, N), complex)
    for x in sites:
        for y in sites: F[idx[x], idx[y]] = fx[tuple((np.array(x) - np.array(y)) % L)]
    return F
def shift(a):
    S = np.zeros((N, N))
    for x in sites:
        y = list(x); y[a] = (y[a] + 1) % L; S[idx[tuple(y)], idx[x]] = 1
    return S
Sh = [shift(a) for a in range(3)]
HW = sum(np.kron((Sh[a].T - Sh[a]) / (2j), SIG[a]) for a in range(3)); FG = np.kron(kernel_op(f_G), s0)
K_ = kernel_op(f_G)
P(f"f_Gamma real-space support (L=4): {sum(abs(K_[idx[x], 0]) > 1e-12 for x in sites)} nonzero offsets")
worst = {"HW": 0, "FG": 0}
for R in ROT:
    U = spin_lift(R); Rop = np.zeros((N, N))
    for x in sites: Rop[idx[tuple((R @ np.array(x)) % L)], idx[x]] = 1
    O = np.kron(Rop, U)
    for nm, Mx in (("HW", HW), ("FG", FG)): worst[nm] = max(worst[nm], np.abs(O @ Mx - Mx @ O).max())
P("max over 24 spin-lifted rotations |[R, X]|:", {k: f"{v:.1e}" for k, v in worst.items()},
  " translations:", {nm: f"{max(np.abs(np.kron(Sh[a], s0) @ Mx - Mx @ np.kron(Sh[a], s0)).max() for a in range(3)):.1e}" for nm, Mx in (("HW", HW), ("FG", FG))})
del HW, FG, K_

# Fock check (X2 T2 code): L = 2 torus, 8 sites x 2 slots = 16 modes (slot = spin, or = generation: same algebra).
Lf = 2; fsites = list(itertools.product(range(Lf), repeat=3)); nm = 16
def mode(c, s): return C.index(c) * 2 + s
def Fmat(fun):
    F = np.zeros((nm, nm), complex)
    for xi, x in enumerate(fsites):
        for c in C:
            k = np.pi * np.array(c)
            for s in range(2): F[xi * 2 + s, mode(c, s)] = fun(k) * np.exp(1j * np.dot(k, x)) / np.sqrt(8)
    return F
def sector(Np): return [b for b in range(1 << nm) if bin(b).count("1") == Np]
def ann_matrix(m, src, dst):
    di = {b: i for i, b in enumerate(dst)}; A = np.zeros((len(dst), len(src)))
    for j, b in enumerate(src):
        if b >> m & 1:
            sgn = (-1) ** bin(b & ((1 << m) - 1)).count("1"); A[di[b ^ (1 << m)], j] = sgn
    return A
def randV(F, nterms, rng):
    V = np.zeros((nm,) * 4, complex)
    for _ in range(nterms):
        x = rng.integers(8); a = rng.integers(3); y = list(fsites[x]); y[a] = (y[a] + 1) % Lf; y = fsites.index(tuple(y))
        pool = [x * 2, x * 2 + 1, y * 2, y * 2 + 1]
        i, j, k, l = rng.choice(pool, 4); cf = rng.normal() + 1j * rng.normal()
        t = cf * np.einsum("a,b,c,d->abcd", F[i].conj(), F[j].conj(), F[k], F[l])
        V += t + t.transpose(3, 2, 1, 0).conj()
    return V
SEC = {Np: sector(Np) for Np in range(5)}
CM = {Np: [ann_matrix(m, SEC[Np], SEC[Np - 1]) for m in range(nm)] for Np in range(1, 5)}
def Hsector(V, Np):
    A = np.array([[CM[Np - 1][k] @ CM[Np][l] for l in range(nm)] for k in range(nm)])
    D = np.einsum("ijkl,klab->ijab", V, A)
    return np.einsum("jiac,ijab->cb", A.conj(), D)
for lab, fun in (("filtered (f_Gamma)", f_G), ("control: unfiltered (f=1)", lambda k: 1.0)):
    F = Fmat(fun); V = randV(F, 12, np.random.default_rng(7))
    H3 = Hsector(V, 3); H2 = Hsector(V, 2)
    s3, s2 = SEC[3], SEC[2]; wl = 0; wm = 0
    for c in C:
        for s in range(2):
            A = ann_matrix(mode(c, s), s3, s2); comm = np.abs(H2 @ A - A @ H3).max()
            if hw(c) == 0: wl = max(wl, comm)
            else: wm = max(wm, comm)
    P(f"Fock L=2, {lab}: ||H_N=3|| = {np.abs(H3).max():.2f}; max|[H, psi(Gamma)]| = {wl:.2e}; max|[H, psi(mirror corners)]| = {wm:.2e}")
P("(walker vanishes identically on the L=2 torus: sin(0) = sin(pi) = 0, so H = W.Q there, as in X2 T2)")

# ---------------------------------------------------------------- (a3) gates
P("\n=== (a3) cyclic Z16 gates over corner sets (chi_c = (-1)^hw, X2 convention), nu_g = d*Ngen*sum_c chi_c (-1)^{g.c} mod 16 ===")
def nu(cset, g, d, Ng): return (d * Ng * sum((-1) ** hw(c) * (-1) ** (np.dot(g, c) % 2) for c in cset)) % 16
mirrorP = [c for c in C if hw(c) > 0]; lightP = [(0, 0, 0)]; mirrorX2 = [c for c in C if hw(c) != 1]
for nmz, cs, Ng in (("X2' mirror (7 corners, x3 gens)", mirrorP, 3), ("X2' light (Gamma, x3 gens)", lightP, 3), ("X2 mirror (5 corners)", mirrorX2, 1)):
    for d in (16, 15):
        P(f"  {nmz}, d={d}: nu_g over g in Z2^3 = {[int(nu(cs, g, d, Ng)) for g in C]}")
P("  Spin(10) minimal instanton: 4 zero modes per 16 (T(16)=2); phase of the 't Hooft vertex under g.i^F at corner c is "
  "i^(4 * Ngen * sum chi (+-1)) = 1 for every g and corner set:",
  all(abs(1j ** int(4 * 3 * sum((-1) ** hw(c) * (-1) ** (np.dot(g, c) % 2) for c in mirrorP)) - 1) < 1e-12 for g in C))

# ---------------------------------------------------------------- (a4) little-group characters
P("\n=== (a4) first-order traceless strain at a corner: multiplicity of (E+T2)|_little in operator spaces ===")
def little(c):
    k = np.pi * np.array(c); return [R for R in ROT if np.allclose(np.mod(R @ k - k + np.pi, 2 * np.pi) - np.pi, 0)]
for cname, c in (("Gamma", (0, 0, 0)), ("hw1 (pi,0,0)", (1, 0, 0))):
    G = little(c); m_end = 0.0; m_pair = 0.0
    for R in G:
        U = spin_lift(R); tu = np.trace(U)
        chi_end = abs(tu) ** 2; chi_pair = tu ** 2            # End(C^2) = U x U*;  pairing space = U x U
        chi_st = (np.trace(R @ R) + np.trace(R) ** 2) / 2 - 1   # symmetric traceless rank-2 (E + T2 of O)
        m_end += chi_end * chi_st; m_pair += (chi_pair * chi_st)
    P(f"  {cname}: |little group| = {len(G)}; mult(E+T2 in End C^2) = {m_end/len(G):.3f}; mult(E+T2 in pairing C^2xC^2) = {(m_pair/len(G)).real:.3f}"
      f"  (flavour index internal: x 9 for any 3x3 flavour data)")
P(f"done ({time.time()-t0:.0f}s)")
