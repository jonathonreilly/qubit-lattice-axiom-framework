"""R1: is the exponent 16 a cross-rung invariant? (HIER-1 mechanism (a))

(i)   zero count of the naive symbol and of the naive+Wilson symbol, d = 3, 4;
      Wilson term invariant under every signed permutation of the axes
      (the hypercubic group, which contains the proper cubic rotations of the
      axioms and the B3a four-direction form); Wilson term NOT invariant under
      the doubler shift k -> k + pi e_mu.
(ii)  signed doubler chirality sum: at corner S the species has gamma5 sign
      (-1)^|S| (product of the sign flips of its gamma matrices).
(iii) u0-degree of det(u0 D_stag) on all-APBC blocks Ls^3 x Lt.
(iv)  2D U(1) toy with topological charge Q: naive near-zero count vs Wilson
      spectral flow of H(m) = gamma5 (D - m).
"""
import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS" if ok else "FAIL"), name, detail)


# ---------------------------------------------------------------- (i)
def zero_count(d, L, r):
    k = 2 * np.pi * np.arange(L) / L
    grids = np.meshgrid(*([k] * d), indexing="ij")
    s2 = sum(np.sin(g) ** 2 for g in grids)
    w = r * sum(1 - np.cos(g) for g in grids)
    dd = s2 + w ** 2            # D^dagger D for D = i gamma.sin k + W
    return int(np.sum(dd < 1e-20))


for d in (3, 4):
    for L in (4, 8):
        counts = {r: zero_count(d, L, r) for r in (0.0, 0.1, 0.5, 1.0)}
        check(f"i.count d={d} L={L}", counts[0.0] == 2 ** d and all(counts[r] == 1 for r in (0.1, 0.5, 1.0)),
              f"zeros {counts}")

# doubler masses under Wilson: W(corner S) = 2 r |S|, continuous in r -> 0
r_vals = [0.5, 0.1, 0.01, 0.001]
masses = [[2 * r * s for s in range(1, 5)] for r in r_vals]
check("i.doubler masses -> 0 continuously as r -> 0", all(abs(m[0] - 2 * r) < 1e-15 for m, r in zip(masses, r_vals)),
      f"lightest doubler mass 2r at r={r_vals}: {[m[0] for m in masses]}")

rng = np.random.default_rng(1)
ks = rng.uniform(-np.pi, np.pi, size=(50, 4))


def W(k):
    return np.sum(1 - np.cos(k), axis=-1)


def S2(k):
    return np.sum(np.sin(k) ** 2, axis=-1)


ok_hc = True
n_el = 0
for perm in itertools.permutations(range(4)):
    for signs in itertools.product((1, -1), repeat=4):
        n_el += 1
        kp = ks[:, perm] * np.array(signs)
        ok_hc &= np.allclose(W(kp), W(ks)) and np.allclose(S2(kp), S2(ks))
check("i.Wilson + naive |D|^2 invariant under all signed permutations", ok_hc and n_el == 384, f"{n_el} elements")

shift_ok_naive = all(np.allclose(S2(ks + np.pi * np.eye(4)[m]), S2(ks)) for m in range(4))
shift_breaks_W = all(not np.allclose(W(ks + np.pi * np.eye(4)[m]), W(ks)) for m in range(4))
check("i.doubler shift k->k+pi e_mu: naive invariant, Wilson not", shift_ok_naive and shift_breaks_W)

# translations act on k by phases, signed permutations linearly: both fix k = 0,
# so no element of the axiom group (or B3a hypercubic group) maps k=0 to a corner.
orbit0 = set()
for perm in itertools.permutations(range(4)):
    for signs in itertools.product((1, -1), repeat=4):
        orbit0.add(tuple((np.zeros(4)[list(perm)] * np.array(signs)).tolist()))
check("i.linear point group orbit of k=0 is {0}", orbit0 == {(0.0, 0.0, 0.0, 0.0)})

# ---------------------------------------------------------------- (ii)
for d in range(1, 7):
    signed = sum((-1) ** len(S) for n in range(d + 1) for S in itertools.combinations(range(d), n))
    unsigned = 2 ** d
    check(f"ii.d={d} signed chirality sum", signed == 0, f"signed {signed}, unsigned {unsigned}")

# explicit d=4 check: species at corner S has effective gammas s_mu gamma_mu,
# s_mu = cos(pi [mu in S]); its chirality operator is prod(s_mu) gamma5.
g = []
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0 + 0j, -1.0])
i2 = np.eye(2)
g = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, i2)]
g5 = g[0] @ g[1] @ g[2] @ g[3]
tot = 0
for n in range(5):
    for S in itertools.combinations(range(4), n):
        s = [(-1 if m in S else 1) for m in range(4)]
        g5S = (s[0] * g[0]) @ (s[1] * g[1]) @ (s[2] * g[2]) @ (s[3] * g[3])
        sign = np.real(np.trace(g5S @ g5)) / 4
        tot += sign
check("ii.d=4 explicit species chirality signs sum", abs(tot) < 1e-12, f"sum {tot:+.1f} over 16 corners")


# ---------------------------------------------------------------- (iii)
def stag_D(Ls, Lt, u0):
    dims = (Lt, Ls, Ls, Ls)
    sites = list(itertools.product(*[range(n) for n in dims]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    D = np.zeros((N, N))
    for s in sites:
        i = idx[s]
        for mu in range(4):
            eta = (-1) ** sum(s[:mu])
            # forward
            t = list(s)
            t[mu] += 1
            bf = 1.0
            if t[mu] == dims[mu]:
                t[mu] = 0
                bf = -1.0      # antiperiodic in every direction
            D[i, idx[tuple(t)]] += u0 * eta * bf
            t = list(s)
            t[mu] -= 1
            bb = 1.0
            if t[mu] < 0:
                t[mu] = dims[mu] - 1
                bb = -1.0
            D[i, idx[tuple(t)]] -= u0 * eta * bb
    return D, N


for Ls, Lt in ((2, 2), (2, 4), (4, 2), (4, 4)):
    D1, N = stag_D(Ls, Lt, 1.0)
    D2, _ = stag_D(Ls, Lt, 2.0)
    s1, l1 = np.linalg.slogdet(D1)
    s2, l2 = np.linalg.slogdet(D2)
    deg = (l2 - l1) / np.log(2.0)
    check(f"iii.u0-degree Ls={Ls} Lt={Lt}", abs(deg - N) < 1e-8 and s1 != 0,
          f"degree {deg:.6f} = number of sites {N} (= 8 Lt at Ls = 2)")


# ---------------------------------------------------------------- (iv)
def dirac2d(L, Q, r):
    F = 2 * np.pi * Q / L ** 2
    n = L * L

    def ix(x, y):
        return (x % L) + L * (y % L)
    s1 = np.array([[0, 1], [1, 0]], complex)
    s2 = np.array([[0, -1j], [1j, 0]])
    gam = [s1, s2]
    D = np.zeros((2 * n, 2 * n), complex)
    for x in range(L):
        for y in range(L):
            i = ix(x, y)
            U = [np.exp(-1j * F * y), np.exp(1j * F * L * x) if y == L - 1 else 1.0]
            nb = [ix(x + 1, y), ix(x, y + 1)]
            for mu in range(2):
                j = nb[mu]
                blk_f = 0.5 * (gam[mu] - r * np.eye(2)) * U[mu]
                blk_b = 0.5 * (-gam[mu] - r * np.eye(2)) * np.conj(U[mu])
                D[2 * i:2 * i + 2, 2 * j:2 * j + 2] += blk_f
                D[2 * j:2 * j + 2, 2 * i:2 * i + 2] += blk_b
            D[2 * i:2 * i + 2, 2 * i:2 * i + 2] += 2 * r * np.eye(2)
    g5 = np.kron(np.eye(n), np.diag([1.0, -1.0]))
    return D, g5


L = 12
for Q in (1, 2):
    Dn, g5 = dirac2d(L, Q, 0.0)
    lam = np.abs(np.linalg.eigvals(Dn))
    lam.sort()
    gap_ratio = lam[4 * Q] / max(lam[4 * Q - 1], 1e-300)
    small = int(np.sum(lam < 0.5 * lam[4 * Q]))
    check(f"iv.naive Q={Q}: near-zero modes = 2^d |Q| = {4 * Q}", small == 4 * Q,
          f"|lambda|_(4Q-1)={lam[4 * Q - 1]:.3e}, |lambda|_(4Q)={lam[4 * Q]:.3e}, ratio {gap_ratio:.1f}")
    # naive: H(m)^2 = D^dag D + m^2 has no zero crossing for m != 0 -> no flow
    Hn = g5 @ Dn
    check(f"iv.naive Q={Q}: H(m)^2 = D^dag D + m^2 (no crossings, net flow 0)",
          np.allclose((g5 @ (Dn - 0.3 * np.eye(len(Dn)))) @ (g5 @ (Dn - 0.3 * np.eye(len(Dn)))),
                      Dn.conj().T @ Dn + 0.09 * np.eye(len(Dn))))
    Dw, _ = dirac2d(L, Q, 1.0)
    ms = np.arange(-1.0, 5.0 + 1e-9, 0.005)
    prev = None
    flows = []
    for m in ms:
        ev = np.linalg.eigvalsh(g5 @ (Dw - m * np.eye(len(Dw))))
        npos = int(np.sum(ev > 0))
        if prev is not None and npos != prev:
            flows.append((round(m, 3), npos - prev))
        prev = npos
    branch = {}
    for m, dn in flows:
        b = int(round(m / 2.0))
        branch[b] = branch.get(b, 0) + dn
    net = sum(dn for _, dn in flows)
    check(f"iv.Wilson Q={Q}: physical-branch flow |Q|, doubler branches -2Q, +Q, total 0",
          abs(branch.get(0, 0)) == Q and branch.get(1, 0) == -2 * branch.get(0, 0)
          and branch.get(2, 0) == branch.get(0, 0) and net == 0,
          f"flow by branch (m~0,2,4) {branch}, total {net}")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
