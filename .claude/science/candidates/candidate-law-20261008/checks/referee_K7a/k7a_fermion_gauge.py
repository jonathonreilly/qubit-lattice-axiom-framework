"""K7a part 1: compact U(1) Wilson + 4D staggered (Kogut-Susskind / Kawamoto-Smit) fermions on a Z^4 torus.

For each of the 384 signed permutations g = (p, sg) of the four axes (time = axis 3 included):
  * transform a random U(1) link configuration U -> U^g (pull back along the axis map)
  * find site signs eps_g(y) with  D[U]_{x,x'} = eps_g(Rx) eps_g(Rx') D[U^g]_{Rx,Rx'}  (BFS on the free action)
  * verify the identity on the random interacting configuration, with mass, EXACT to round-off
  * verify the Wilson action S_W[U^g] = S_W[U]
Also: the 16 shift symmetries (x -> x+mu with sign zeta_mu), and the U(1)_eps chiral symmetry at m = 0.
"""
import itertools, sys, time
import numpy as np

t0 = time.time()
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
dims = (L,) * 4
Ns = L ** 4
coords = np.array(list(itertools.product(range(L), repeat=4)))
lin = lambda X: ((X[..., 0] * L + X[..., 1]) * L + X[..., 2]) * L + X[..., 3]
idx_of = lin(coords)
assert (idx_of == np.arange(Ns)).all()
rng = np.random.default_rng(20261008)


def say(*a):
    print(*a); sys.stdout.flush()


def eta(mu, X):
    return (-1) ** (X[..., :mu].sum(axis=-1)) if mu > 0 else np.ones(X.shape[:-1], dtype=int)


def shifted(X, mu, d):
    Y = X.copy(); Y[..., mu] = (Y[..., mu] + d) % L; return Y


def dirac(U, m):
    """U: dict mu -> complex array (Ns,) = U_mu(x) on link x -> x+mu.  Returns dense D (Ns x Ns)."""
    D = np.zeros((Ns, Ns), complex)
    for mu in range(4):
        e = eta(mu, coords)
        fwd = lin(shifted(coords, mu, +1)); bwd = lin(shifted(coords, mu, -1))
        D[np.arange(Ns), fwd] += 0.5 * e * U[mu]
        D[np.arange(Ns), bwd] -= 0.5 * e * np.conj(U[mu][bwd])
    D += m * np.eye(Ns)
    return D


def wilson(U, beta=1.0):
    S = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            fm = lin(shifted(coords, mu, 1)); fn = lin(shifted(coords, nu, 1))
            plaq = U[mu] * U[nu][fm] * np.conj(U[mu][fn]) * np.conj(U[nu])
            S += beta * np.sum(1 - plaq.real)
    return S


def axis_map(p, sg):
    Xn = np.zeros_like(coords)
    for a in range(4):
        Xn[:, p[a]] = (sg[a] * coords[:, a]) % L
    return lin(Xn)                         # Rmap[x] = index of R x


def transform_links(U, p, sg):
    """U'_nu(y) for link y -> y+nu, pulled back along R^{-1}."""
    Rmap = axis_map(p, sg)
    inv = np.empty(Ns, dtype=np.int64); inv[Rmap] = np.arange(Ns)
    Up = {}
    pinv = {p[a]: a for a in range(4)}
    for nu in range(4):
        mu = pinv[nu]
        x = inv                                  # preimage of every y (array over y)
        if sg[mu] == +1:
            Up[nu] = U[mu][x]
        else:
            xm = lin(shifted(coords[x], mu, -1))
            Up[nu] = np.conj(U[mu][xm])
    return Up, Rmap


def solve_signs(p, sg, D0, Rmap=None):
    """eps (over y) with D0[x,x'] = eps[Rx] eps[Rx'] D0[Rx,Rx'].  BFS; returns eps or None."""
    if Rmap is None:
        Rmap = axis_map(p, sg)
    eps = np.zeros(Ns, dtype=int)
    nbrs = [[] for _ in range(Ns)]
    # constraints on pairs (y,y') = (Rx,Rx')
    Dre = D0.real if np.allclose(D0.imag, 0) else None
    rows, cols = np.nonzero(np.abs(D0) > 1e-12)
    cons = {}
    for x, xp in zip(rows, cols):
        y, yp = Rmap[x], Rmap[xp]
        if y == yp:
            continue
        val = D0[x, xp] / D0[y, yp]
        assert abs(abs(val) - 1) < 1e-12 and abs(val.imag) < 1e-12
        nbrs[y].append((yp, int(round(val.real))))
        nbrs[yp].append((y, int(round(val.real))))      # relation symmetric in (y,y') pair: product eps_y eps_yp = val
    # BFS
    eps[:] = 0; eps[0] = 1; stack = [0]
    while stack:
        a = stack.pop()
        for b, v in nbrs[a]:
            if eps[b] == 0:
                eps[b] = eps[a] * v; stack.append(b)
    ok = True
    for a in range(Ns):
        for b, v in nbrs[a]:
            if eps[a] * eps[b] != v:
                ok = False
    return (eps if ok and (eps != 0).all() else None), Rmap


def signed_perms(n):
    for p in itertools.permutations(range(n)):
        for sg in itertools.product((1, -1), repeat=n):
            yield p, sg


# random interacting configuration + free reference
theta = rng.uniform(-np.pi, np.pi, (4, Ns))
U = {mu: np.exp(1j * theta[mu]) for mu in range(4)}
U1 = {mu: np.ones(Ns, complex) for mu in range(4)}
m = 0.37
D0 = dirac(U1, m)
DU = dirac(U, m)
SU = wilson(U)
n_ok = 0; worstD = 0.0; worstW = 0.0; nfail = []
for p, sg in signed_perms(4):
    eps, Rmap = solve_signs(p, sg, D0)
    if eps is None:
        nfail.append((p, sg)); continue
    Up, _ = transform_links(U, p, sg)
    Dp = dirac(Up, m)
    # identity D[U]_{x,x'} = eps[Rx] eps[Rx'] D[U^g]_{Rx,Rx'}
    lhs = DU
    rhs = (eps[Rmap][:, None] * eps[Rmap][None, :]) * Dp[np.ix_(Rmap, Rmap)]
    worstD = max(worstD, np.abs(lhs - rhs).max())
    worstW = max(worstW, abs(wilson(Up) - SU))
    n_ok += 1
say(f'L={L}: torus {L}^4, mass m=0.37, random U(1) links (Ns={Ns})')
say(f'F1 W(B4): {n_ok}/384 elements admit a pure-sign site transformation eps_g (no taste-matrix needed in the 1-component basis); failures: {len(nfail)}')
say(f'   interacting Dirac operator identity D[U] = eps R^T D[U^g] R eps : max |dev| = {worstD:.1e}  (all elements incl. t<->x swaps and reflections)')
say(f'   Wilson plaquette action S_W[U^g] = S_W[U]: max |dev| = {worstW:.1e}')
if nfail:
    say('   failing examples:', nfail[:3])

# ---- axis swap t <-> x1 explicit sign (repo: docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md:515-526 uses eps = (-1)^(x_tau x_1))
for p, sg, name in (((3, 1, 2, 0), (1, 1, 1, 1), 'swap axes 0<->3'),):
    eps, Rmap = solve_signs(p, sg, D0)
    cands = {'(-1)^(x0 x3)': (-1) ** (coords[:, 0] * coords[:, 3])}
    # in our eta ordering (axes 0,1,2,3) the swap of the first and last axis has a longer sign field; report the BFS field's structure
    f = eps * eps[0]
    # fit  (-1)^{ sum_{a<b} c_ab x_a x_b }
    pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
    best = None
    for cs in itertools.product((0, 1), repeat=6):
        g = (-1) ** sum(c * coords[:, a] * coords[:, b] for c, (a, b) in zip(cs, pairs))
        if (g == f).all():
            best = cs
    say(f'   {name}: BFS sign field = (-1)^(quadratic form) with coefficients over pairs {pairs}: {best}')

# ---- shifts: R x = x + mu (a pure translation by ONE lattice unit): needs a sign field zeta (taste-nonsinglet)
worstS = 0.0; nS = 0
for mu in range(4):
    Rmap = lin(shifted(coords, mu, +1))
    eps, _ = solve_signs(None, None, D0, Rmap)
    if eps is None:
        say(f'   shift in direction {mu}: NO sign field'); continue
    inv = np.empty(Ns, dtype=np.int64); inv[Rmap] = np.arange(Ns)
    Us = {nu: U[nu][inv] for nu in range(4)}
    Ds = dirac(Us, m)
    rhs = (eps[Rmap][:, None] * eps[Rmap][None, :]) * Ds[np.ix_(Rmap, Rmap)]
    worstS = max(worstS, np.abs(DU - rhs).max()); nS += 1
say(f'F2 unit shifts x -> x+mu (all 4 directions): sign field exists in {nS}/4; interacting identity max |dev| = {worstS:.1e}  (translation by 1 acts with a site sign = taste matrix Xi_mu in the spin-taste basis; by 2 acts trivially)')
# translation by two units: no sign needed
R2 = lin(shifted(shifted(coords, 0, 1), 0, 1)); inv2 = np.empty(Ns, dtype=np.int64); inv2[R2] = np.arange(Ns)
U2 = {nu: U[nu][inv2] for nu in range(4)}
d2 = np.abs(DU - dirac(U2, m)[np.ix_(R2, R2)]).max()
say(f'   translation by 2 units: pure relabelling, dev {d2:.1e}')

# ---- local U(1) gauge covariance (exact): U_mu(x) -> Lam(x) U_mu(x) conj(Lam(x+mu)),  psi -> Lam psi
Lam = np.exp(1j * rng.uniform(-np.pi, np.pi, Ns))
Ug = {mu: Lam * U[mu] * np.conj(Lam[lin(shifted(coords, mu, 1))]) for mu in range(4)}
devg = np.abs(dirac(Ug, m) - np.diag(Lam) @ DU @ np.diag(Lam.conj())).max()
say(f'F0 exact local U(1) gauge covariance D[U^Lam] = Lam D[U] Lam^*: max |dev| = {devg:.1e};  Wilson S_W invariant: {abs(wilson(Ug) - SU):.1e}')

# ---- chiral U(1)_eps at m=0
epsx = (-1) ** coords.sum(axis=1)
D00 = dirac(U, 0.0)
th = 0.7
Ge = np.diag(np.exp(1j * th * epsx))
# psi -> e^{i th eps} psi, psibar -> psibar e^{i th eps}
dev = np.abs(Ge @ D00 @ Ge - D00).max()
say(f'F3 U(1)_eps at m = 0 (psi -> e^(i th eps) psi, psibar -> psibar e^(i th eps)): max |dev| = {dev:.1e}')

# ---- free dispersions (symbols)
k = rng.uniform(-np.pi, np.pi, 4)
sin2 = np.sum(np.sin(k) ** 2); s2 = np.sum((2 * np.sin(k / 2)) ** 2)
say(f'F4 free symbols (A-lattice, one random k): staggered Euclid pole sum_mu sin^2 k_mu = {sin2:.5f};  photon/graviton sum_mu s_mu^2 = {s2:.5f}')
kk = 1e-2 * rng.normal(size=4)
say(f'   at small k both equal k^2 to O(k^4): ratio sin-form/s-form - 1 = {np.sum(np.sin(kk)**2)/np.sum((2*np.sin(kk/2))**2) - 1:.2e}; both are permutation-symmetric in (k_1..k_4) so time/space slopes are identical (c = 1).')
say(f'done in {time.time() - t0:.1f}s')
