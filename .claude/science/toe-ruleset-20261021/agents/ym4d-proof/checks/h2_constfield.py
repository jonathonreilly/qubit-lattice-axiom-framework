"""h2: Proposition CF (1)-(2) of HIST.md §6, one S4' step, d = 4, L = 3, SU(2). Criteria: checks/h2_criteria.md (first).
Contour code follows c32_rlarge.py (copied, not imported)."""
import itertools, math, resource, time
import numpy as np

T0 = time.time()
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
TAU = [I2, 1j * SX, 1j * SY, 1j * SZ]
L = 3
R0 = [range(-1, 5), range(-1, 5), range(-1, 5), range(-1, 2)]
SITES = [s for s in itertools.product(*R0)]
SITESET = set(SITES)
E = [tuple(1 if k == m else 0 for k in range(4)) for m in range(4)]
ORDERS = list(itertools.permutations(range(4)))
O = (0, 0, 0, 0)
CS = [(O, 0), ((3, 0, 0, 0), 1), ((0, 3, 0, 0), 0), (O, 1)]   # coarse (0,1)-plaquette links
CT = (O, 2)                                                   # transverse coarse link 0 -> 3e2


def opn(M):
    return np.linalg.norm(M, 2)


def su2_exp(v):
    th = np.linalg.norm(v)
    if th < 1e-300:
        return I2.copy()
    n = v / th
    return math.cos(th / 2) * I2 + 1j * math.sin(th / 2) * (n[0] * SX + n[1] * SY + n[2] * SZ)


def add(x, v, c=1):
    return tuple(x[k] + c * v[k] for k in range(4))


def diag(t):
    return np.array([[np.exp(1j * t), 0], [0, np.exp(-1j * t)]])


def field(F):
    U = {}
    for x in SITES:
        for m in range(4):
            if add(x, E[m]) not in SITESET:
                continue
            if m == 0:
                U[(x, m)] = diag(-F * x[1] / 2)
            elif m == 1:
                U[(x, m)] = diag(F * x[0] / 2)
            else:
                U[(x, m)] = I2.copy()
    return U


def step(U, x, m, sgn):
    if sgn > 0:
        return U[(x, m)], add(x, E[m])
    y = add(x, E[m], -1)
    return U[(y, m)].conj().T, y


def axial(U, a, b, order):
    M = I2.copy()
    x = a
    for m in order:
        while x[m] != b[m]:
            s = 1 if b[m] > x[m] else -1
            T, x = step(U, x, m, s)
            M = M @ T
    return M


def straight(U, a, m, n):
    M = I2.copy()
    x = a
    for _ in range(n):
        T, x = step(U, x, m, 1)
        M = M @ T
    return M


def block(c):
    return [add(c, t) for t in itertools.product((-1, 0, 1), repeat=4)]


def contours(U, c):
    start, m = c
    end = add(start, E[m], L)
    S = straight(U, start, m, L)
    out = []
    for y in block(start):
        leg = straight(U, y, m, L)
        yL = add(y, E[m], L)
        for s in ORDERS:
            out.append(axial(U, start, y, s) @ leg @ axial(U, end, yL, s).conj().T)
    return S, out


def W0(M):
    v = np.array([np.real(np.trace(t.conj().T @ M)) for t in TAU])
    v = v / np.linalg.norm(v)
    return sum(v[a] * TAU[a] for a in range(4))


def phi(M, W, V):
    return (np.real(np.trace(W.conj().T @ M)) - np.real(np.trace(V.conj().T @ M))) / 2


def analyse(U):
    res = []
    for c in CS:
        S, T = contours(U, c)
        Mb = sum(T) / len(T)
        m = 0.5 * np.real(np.trace(Mb @ S.conj().T))
        e1 = opn(Mb @ S.conj().T - m * I2)
        W = W0(Mb)
        res.append((S, Mb, m, e1, opn(W - S), phi(Mb, W, S), W))
    return res


def gauge(U, seed):
    rng = np.random.default_rng(seed)
    g = {x: su2_exp(rng.standard_normal(3) * 2.0) for x in SITES}
    return {(x, m): g[x] @ V @ g[add(x, E[m])].conj().T for (x, m), V in U.items()}


allok = True
for F in (0.01, 0.03, 0.058):
    U = field(F)
    res = analyse(U)
    c1 = all(r[3] <= 1e-12 and 0 < r[2] <= 1 + 1e-15 for r in res)
    c2 = all(r[4] <= 1e-12 and abs(r[5]) <= 1e-14 for r in res)
    Wp = res[0][6] @ res[1][6] @ res[2][6].conj().T @ res[3][6].conj().T
    c3e = opn(Wp - diag(L * L * F))
    c3 = c3e <= 1e-12
    St, Tt = contours(U, CT)
    c4e = max(opn(T - St) for T in Tt)
    c4 = c4e <= 1e-12
    Ug = gauge(U, 1)
    rg = analyse(Ug)
    Wpg = rg[0][6] @ rg[1][6] @ rg[2][6].conj().T @ rg[3][6].conj().T
    c5e = max(max(abs(a[2] - b[2]) for a, b in zip(res, rg)), abs(np.trace(Wpg) - np.trace(Wp)))
    c5 = c5e <= 1e-12
    rng = np.random.default_rng(2)
    Un = {k: V @ su2_exp(0.02 * rng.standard_normal(3)) for k, V in U.items()}
    rn = analyse(Un)
    c6e = max(r[3] for r in rn)
    c6 = c6e > 1e-6
    ok = c1 and c2 and c3 and c4 and c5 and c6
    allok &= ok
    print(f"F={F}: m_c = {[round(r[2], 12) for r in res]}; C1 max|Mb S^-1 - m| = {max(r[3] for r in res):.2e}; "
          f"C2 max|W0-S| = {max(r[4] for r in res):.2e}, max|phi(S)| = {max(abs(r[5]) for r in res):.2e}; "
          f"C3 |coarse plaq - exp(iL^2F)| = {c3e:.2e}; C4 transverse {c4e:.2e}; C5 gauge {c5e:.2e}; "
          f"C6 neg-control {c6e:.2e} -> {'PASS' if ok else 'FAIL'}")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print(f"h2: {'PASS' if allok else 'FAIL'}  t {time.time() - T0:.1f}s  peak RSS {rss:.0f} MB")
