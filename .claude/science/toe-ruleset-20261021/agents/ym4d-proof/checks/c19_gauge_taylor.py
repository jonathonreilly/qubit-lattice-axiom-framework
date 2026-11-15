"""c19: Lemma GT (gauge-invariant Taylor lemma) on explicit SU(2) instances, plus B_4 representation theory.

Criteria: checks/c19_criteria.md (written before this script). Tests instances, not uniformity.
Conventions: su(2) basis tau_k = i sigma_k (anti-Hermitian); transport U' = U A(t) along a path (left-to-right
product); gauge action U_b -> g(x) U_b g(x+e)^{-1}, A -> g A g^{-1} - (dg) g^{-1}; plaquette U_p = U(x,mu)
U(x+mu,nu) U(x+nu,mu)^+ U(x,nu)^+.  Radial gauge A_nu(x) = x^mu Omega_mu nu(x), Omega antisymmetric; F(0) = 2 Omega^0.
"""
import itertools
import numpy as np

rng = np.random.default_rng(20261027)
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
TAU = 1j * SIG
I2 = np.eye(2, dtype=complex)
D = 4
RESULTS = {}


def alg(a):  # real (...,3) -> su(2) (...,2,2)
    return np.einsum('...k,kij->...ij', a, TAU)


def expm_su2(X):  # X in su(2), batched; exact closed form
    # X = sum a_k i sigma_k  =>  X01 = i a1 + a2, X00 = i a3
    a = np.stack([np.imag(X[..., 0, 1]), np.real(X[..., 0, 1]), np.imag(X[..., 0, 0])], -1)
    th = np.linalg.norm(a, axis=-1)
    sinc = np.where(th > 1e-300, np.sin(th) / np.where(th > 0, th, 1), 1.0)
    return np.cos(th)[..., None, None] * I2 + sinc[..., None, None] * X


def dag(U):
    return np.conj(np.swapaxes(U, -1, -2))


# ---------------------------------------------------------------- representation theory (P1, P2)
def b4_elements():
    els = []
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product([1, -1], repeat=4):
            M = np.zeros((4, 4))
            for i, p in enumerate(perm):
                M[p, i] = signs[i]
            els.append(M)
    return els


PAIRS = [(m, n) for m in range(4) for n in range(m + 1, 4)]


def lambda2(R):  # action on e_m ^ e_n basis (m<n)
    M = np.zeros((6, 6))
    for j, (m, n) in enumerate(PAIRS):
        for i, (a, b) in enumerate(PAIRS):
            M[i, j] = R[a, m] * R[b, n] - R[b, m] * R[a, n]
    return M


def rep_theory():
    els = b4_elements()
    chi = [np.trace(lambda2(R)) for R in els]
    norm = sum(c * c for c in chi) / len(els)
    rot = [R for R in els if np.linalg.det(R) > 0]
    norm_rot = sum(np.trace(lambda2(R)) ** 2 for R in rot) / len(rot)
    # P2: invariant quadratic forms on su(2) (x) Lambda^2 (dim 18) under B_4 generators and random Ad
    def ad(g):
        M = np.zeros((3, 3))
        for k in range(3):
            Y = g @ TAU[k] @ dag(g)
            M[:, k] = [np.real(np.trace(dag(TAU[j]) @ Y)) / 2 for j in range(3)]
        return M
    gens = []
    b4gens = []
    for i in range(3):  # adjacent transpositions
        P = np.eye(4); P[[i, i + 1]] = P[[i + 1, i]]; b4gens.append(P)
    b4gens.append(np.diag([-1.0, 1, 1, 1]))  # one reflection; with the transpositions these generate B_4
    for R in b4gens:
        gens.append(np.kron(np.eye(3), lambda2(R)))
    for _ in range(5):
        g = expm_su2(alg(rng.normal(size=3)))
        gens.append(np.kron(ad(g), np.eye(6)))
    n = 18
    rows = []
    for G in gens:  # M -> G^T M G - M on vec(M)
        rows.append(np.kron(G.T, G.T) - np.eye(n * n))
    # restrict to symmetric M: add antisymmetry-killing rows
    P = np.zeros((n * n, n * n))
    for i in range(n):
        for j in range(n):
            P[i * n + j, i * n + j] += 0.5
            P[i * n + j, j * n + i] -= 0.5
    rows.append(P)
    A = np.vstack(rows)
    sv = np.linalg.svd(A, compute_uv=False)
    null = int(np.sum(sv < 1e-9 * sv[0]))
    gap = sv[-null - 1] / max(sv[-null], 1e-300) if null > 0 else 0.0
    return norm, norm_rot, null, gap


# ---------------------------------------------------------------- backgrounds and transporters
def make_background(kind):
    O0 = np.zeros((4, 4, 3)); O1 = np.zeros((4, 4, 4, 3)); O2 = np.zeros((4, 4, 4, 4, 3))
    def anti(T):
        return T - np.swapaxes(T, 0, 1)
    if kind == 'abelian':
        O0[..., 2] = rng.normal(size=(4, 4)); O1[..., 2] = rng.normal(size=(4, 4, 4))
        O2[..., 2] = rng.normal(size=(4, 4, 4, 4))
    else:
        O0 = rng.normal(size=(4, 4, 3)); O1 = rng.normal(size=(4, 4, 4, 3)); O2 = rng.normal(size=(4, 4, 4, 4, 3))
    O0 = anti(O0) * 0.25; O1 = anti(O1) * 0.15; O2 = anti(O2) * 0.08
    if kind in ('sd', 'asd'):
        sg = 1 if kind == 'sd' else -1
        F = 2 * O0
        Fn = np.zeros_like(F)
        # (anti-)self-dual projection: F_12 = sg F_34, F_13 = -sg F_24, F_14 = sg F_23
        for (a, b, c, d, e) in [(0, 1, 2, 3, 1), (0, 2, 1, 3, -1), (0, 3, 1, 2, 1)]:
            v = 0.5 * (F[a, b] + sg * e * F[c, d])
            Fn[a, b] = v; Fn[b, a] = -v; Fn[c, d] = sg * e * v; Fn[d, c] = -sg * e * v
        O0 = Fn / 2
    def A(x):  # x (...,4) -> A (...,4,2,2)
        Om = O0 + np.einsum('...r,mnrk->...mnk', x, O1) + np.einsum('...r,...s,mnrsk->...mnk', x, x, O2)
        a = np.einsum('...m,...mnk->...nk', x, Om)
        return alg(a)
    return A, 2 * O0


def make_gauge():
    g0 = expm_su2(alg(rng.normal(size=3)))
    c = rng.normal(size=4)
    def theta(x):
        return 0.7 * np.sin(x @ c * 0.6 + 0.3) + 0.4 * x[..., 2] * x[..., 3]
    def dtheta(x):
        return (0.7 * np.cos(x @ c * 0.6 + 0.3) * 0.6)[..., None] * c + 0.4 * np.stack(
            [0 * x[..., 0], 0 * x[..., 0], x[..., 3], x[..., 2]], -1)
    def g(x):
        return g0 @ expm_su2(theta(x)[..., None, None] * TAU[2])
    def transform(A):
        def Ag(x):
            gx = g(x)
            dg_ginv = np.einsum('...m,ij->...mij', dtheta(x), g0 @ TAU[2] @ dag(g0))
            return np.einsum('...ij,...mjk,...kl->...mil', gx, A(x), dag(gx)) - dg_ginv
        return Ag
    return transform


SITES = np.array(list(itertools.product([-1, 0, 1], repeat=4)), dtype=float)
SITE_IDX = {tuple(int(v) for v in x): i for i, x in enumerate(SITES)}
E = np.eye(4)
LINKS = [(i, mu) for i, x in enumerate(SITES) for mu in range(4) if tuple(int(v) for v in x + E[mu]) in SITE_IDX]
LINK_IDX = {l: j for j, l in enumerate(LINKS)}
GL = np.array([0.5 - np.sqrt(3) / 6, 0.5 + np.sqrt(3) / 6])


def transporters(A, s, nsteps=128):
    xs = np.array([SITES[i] for i, _ in LINKS]); mus = np.array([mu for _, mu in LINKS])
    h = 1.0 / nsteps
    U = np.broadcast_to(I2, (len(LINKS), 2, 2)).copy()
    for n in range(nsteps):
        As = []
        for t in GL:
            y = xs + ((n + t) * h) * E[mus]
            Ay = s * A(s * y)  # A^(s)(y) = s A(s y)
            As.append(Ay[np.arange(len(LINKS)), mus])
        A1, A2 = As
        Om = 0.5 * h * (A1 + A2) + (np.sqrt(3) / 12) * h * h * (A1 @ A2 - A2 @ A1)
        U = U @ expm_su2(Om)
    return U


def link(U, x, mu):  # oriented link from x along +mu, or its inverse along -mu
    x = tuple(int(v) for v in x)
    if mu >= 0:
        return U[LINK_IDX[(SITE_IDX[x], mu)]]
    m = -mu - 1
    y = tuple(int(v) for v in np.array(x) - E[m])
    return dag(U[LINK_IDX[(SITE_IDX[y], m)]])


def path(U, x, steps):  # steps: list of signed dirs (+m -> m, -m -> -(m+1))
    W = I2.copy(); x = np.array(x, dtype=float)
    for st in steps:
        W = W @ link(U, x, st)
        x = x + (E[st] if st >= 0 else -E[-st - 1])
    return W


def inbox(x):
    return all(-1 <= v <= 1 for v in x)


PLAQ = []  # (x, mu, nu) all four sites in box
for x in SITES:
    for mu, nu in PAIRS:
        if inbox(x + E[mu] + E[nu]):
            PLAQ.append((x, mu, nu))
RECT = []
for x in SITES:
    for mu in range(4):
        for nu in range(4):
            if mu != nu and inbox(x + E[mu] + 2 * E[nu]):
                RECT.append((x, mu, nu))
N_B = sum(1 for p in PLAQ if (p[1], p[2]) == (0, 1))


def plaq_loop(U, p):
    x, mu, nu = p
    return path(U, x, [mu, nu, -mu - 1, -nu - 1])


def plaq_links(p):
    x, mu, nu = p
    pts = [x, x + E[mu], x + E[mu] + E[nu], x + E[nu]]
    dirs = [mu, nu, mu, nu]
    base = [pts[0], pts[1], pts[3], pts[0]]
    return frozenset((tuple(int(v) for v in b), d) for b, d in zip(base, dirs))


PL = [plaq_links(p) for p in PLAQ]
ADJ = [(i, j) for i in range(len(PLAQ)) for j in range(i + 1, len(PLAQ)) if PL[i] & PL[j]]


def retr(W):
    return 0.5 * np.real(np.trace(W))


def i1(z):
    tot = 0.0; term = z / 2
    for k in range(60):
        tot += term
        term *= (z / 2) ** 2 / ((k + 1) * (k + 2))
    return tot


def F1(U, sel=None):
    return sum(1 - retr(plaq_loop(U, p)) for p in PLAQ if sel is None or sel(p))


def F2(U):
    tp = [retr(plaq_loop(U, p)) for p in PLAQ]
    a = sum((1 - t) ** 2 for t in tp)
    b = sum(1 - retr(path(U, x, [mu, nu, nu, -mu - 1, -nu - 1, -nu - 1])) for x, mu, nu in RECT)
    c = sum(tp[i] * tp[j] for i, j in ADJ)
    return a + b + c


def F3(U, beta=1.3):
    tot = 0.0
    origin = np.zeros(4)
    for mu in range(4):
        for start in (origin, origin - E[mu]):
            K = np.zeros((2, 2), dtype=complex)
            for nu in range(4):
                if nu == mu:
                    continue
                K += path(U, start + E[mu], [nu, -mu - 1, -nu - 1])
                K += path(U, start + E[mu], [-nu - 1, -mu - 1, nu])
            k = 0.5 * np.sqrt(max(np.real(np.linalg.det(K)), 0.0))
            tot += np.log(i1(2 * beta * k) / (beta * k))
    return tot


FUNCS = {
    'F1': lambda U: F1(U),
    'F2': F2,
    'F3': F3,
    'Ca': lambda U: F1(U, lambda p: (p[1], p[2]) == (0, 1)),
    'Cb': lambda U: F1(U, lambda p: p[0][0] >= 0),
}


def main():
    norm, norm_rot, null, gap = rep_theory()
    out = []
    out.append(f"P1 B_4 character norm of Lambda^2 = {norm:.12f} (rotation subgroup: {norm_rot:.12f})")
    out.append(f"P2 invariant quadratic forms on su(2)(x)Lambda^2: dim = {null}, singular-value gap = {gap:.3e}")
    P1 = abs(norm - 1) < 1e-12
    P2 = null == 1 and gap > 1e6
    kinds = ['abelian', 'sd', 'asd', 'generic', 'generic', 'generic']
    svals = [0.4, 0.2, 0.1, 0.05, 0.025]
    U0 = np.broadcast_to(I2, (len(LINKS), 2, 2)).copy()
    f0 = {k: fn(U0) for k, fn in FUNCS.items()}
    data = []
    for kind in kinds:
        A, F0 = make_background(kind)
        FF = sum(np.sum(np.abs(alg(F0[m, n])) ** 2) for m, n in PAIRS)  # sum_{mu<nu} ||F||_HS^2
        vals = {k: {} for k in FUNCS}
        for s in svals:
            for sg in (1, -1):
                U = transporters(A, sg * s)
                for k, fn in FUNCS.items():
                    vals[k][sg * s] = fn(U)
        Ag = make_gauge()(A)
        Ug = transporters(Ag, 0.2, nsteps=256)
        Ur = transporters(A, 0.2, nsteps=256)
        gdiff = {k: abs(FUNCS[k](Ug) - FUNCS[k](Ur)) for k in ('F1', 'F2', 'F3')}
        data.append((kind, FF, vals, gdiff))
    ok = {f'P{i}': True for i in range(3, 11)}
    cvals = {k: [] for k in FUNCS}
    for kind, FF, vals, gdiff in data:
        for k in FUNCS:
            r = {s: (vals[k][s] - f0[k]) / s ** 4 for s in svals}
            R1 = {s: (4 * r[s / 2] - r[s]) / 3 for s in svals[:-1]}
            c = (16 * R1[0.05] - R1[0.1]) / 15 / FF
            cvals[k].append(c)
            if k in ('F1', 'F2', 'F3'):
                for s in (0.4, 0.2, 0.1):
                    if abs(vals[k][s] - vals[k][-s]) > 1e-11 * max(1, abs(vals[k][s])):
                        ok['P3'] = False
                d1, d2 = abs(r[0.2] - r[0.1]), abs(r[0.1] - r[0.05])
                ratio = d1 / d2 if d2 > 0 else np.inf
                if not (3 <= ratio <= 5 or (d1 <= 1e-9 * abs(r[0.1]) and d2 <= 1e-9 * abs(r[0.1]))):
                    ok['P4'] = False
                if gdiff[k] > 1e-10:
                    ok['P7'] = False
                out.append(f"  {kind:8s} {k}: c={c:.10f}  r-diff ratio={ratio:.4f}  "
                           f"even|0.2|={abs(vals[k][0.2]-vals[k][-0.2]):.1e}  gauge={gdiff[k]:.1e}")
        for k in ('F1', 'F2', 'F3'):
            pass
    # P5, P6, P8
    for k in ('F1', 'F2', 'F3'):
        cs = np.array(cvals[k]); spread = (cs.max() - cs.min()) / abs(cs.mean())
        out.append(f"P5 {k}: c mean {cs.mean():.10f}, relative spread {spread:.2e}")
        if spread > 1e-4:
            ok['P5'] = False
        cbar = cs.mean()
        for kind, FF, vals, gdiff in data:
            Rs = {s: vals[k][s] - f0[k] - cbar * s ** 4 * FF for s in (0.1, 0.05)}
            if abs(Rs[0.05]) <= 1e-12:
                out.append(f"  P6 {k} {kind}: R(0.05) = {Rs[0.05]:.1e} below 1e-12 (reported)")
                continue
            q = Rs[0.1] / Rs[0.05]
            out.append(f"  P6 {k} {kind}: R(0.1)/R(0.05) = {q:.3f}")
            if not (57.6 <= q <= 70.4):
                ok['P6'] = False
    c1 = np.mean(cvals['F1'])
    out.append(f"P8 F1: c = {c1:.12f}, n_B/4 = {N_B/4}")
    ok['P8'] = abs(c1 - N_B / 4) <= 1e-6 * N_B / 4
    ca = np.array(cvals['Ca']); spa = (ca.max() - ca.min()) / abs(ca.mean())
    out.append(f"P9 control Ca (B_4 broken): c spread {spa:.3f}")
    ok['P9'] = spa > 0.10
    p10 = False
    for kind, FF, vals, gdiff in data:
        o2 = abs(vals['Cb'][0.2] - vals['Cb'][-0.2]); o1 = abs(vals['Cb'][0.1] - vals['Cb'][-0.1])
        q = o2 / o1 if o1 > 0 else np.inf
        out.append(f"  P10 control Cb (iota broken) {kind}: odd(0.2) = {o2:.3e}, ratio 0.2/0.1 = {q:.3f}")
        if o2 > 1e-6 and 28.8 <= q <= 35.2:
            p10 = True
    ok['P10'] = p10
    ok['P1'] = P1; ok['P2'] = P2
    for key in sorted(ok, key=lambda t: int(t[1:])):
        out.append(f"{key}: {'PASS' if ok[key] else 'FAIL'}")
    out.append(f"c19 overall: {'PASS' if all(ok.values()) else 'FAIL'} ({sum(ok.values())}/{len(ok)})")
    print("\n".join(out))


if __name__ == '__main__':
    main()
