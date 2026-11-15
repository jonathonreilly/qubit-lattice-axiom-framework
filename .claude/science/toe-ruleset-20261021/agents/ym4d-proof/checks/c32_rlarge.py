"""c32: instances for RLARGE.md (session 17). Criteria: checks/c32_criteria.md (written first).
Usage: python3 c32_rlarge.py A|B|C|D
"""
import sys, itertools, math
import numpy as np

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)


def su2_exp(v):
    """exp(i (v . sigma)/2) for a real 3-vector v."""
    th = np.linalg.norm(v)
    if th < 1e-300:
        return I2.copy()
    n = v / th
    H = n[0] * SX + n[1] * SY + n[2] * SZ
    return math.cos(th / 2) * I2 + 1j * math.sin(th / 2) * H


def opn(M):
    return np.linalg.norm(M, 2)


# ---------------------------------------------------------------- Part A
L = 3
R0 = [range(-1, 5), range(-1, 5), range(-1, 2), range(-1, 2)]
SITES = [s for s in itertools.product(*R0)]
SITESET = set(SITES)
E = [tuple(1 if k == m else 0 for k in range(4)) for m in range(4)]


def add(x, v, c=1):
    return tuple(x[k] + c * v[k] for k in range(4))


def make_field(kind, t=0.0, seed=0, f=0.001):
    rng = np.random.default_rng(seed)
    U = {}
    for x in SITES:
        for m in range(4):
            y = add(x, E[m])
            if y not in SITESET:
                continue
            if kind == 'R':
                U[(x, m)] = su2_exp(t * rng.standard_normal(3))
            else:
                th = 0.0
                if kind in ('S1', 'S3') and m == 0:
                    th += -f * (x[1] + x[2] + x[3])
                if kind == 'S2' and m == 1:
                    th += f * x[0]
                if kind == 'S3':
                    if m == 2:
                        th += f * x[1]
                    if m == 3:
                        th += f * (x[1] + x[2])
                U[(x, m)] = np.array([[np.exp(1j * th), 0], [0, np.exp(-1j * th)]])
    return U


def step(U, x, m, sgn):
    """transporter of one step from x in direction sgn*e_m; returns (matrix, new site)."""
    if sgn > 0:
        return U[(x, m)], add(x, E[m])
    y = add(x, E[m], -1)
    return U[(y, m)].conj().T, y


def axial(U, a, b, order):
    """transporter of the axial path a -> b moving coordinates in the given order."""
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


def plaq(U, x, m, n):
    return U[(x, m)] @ U[(add(x, E[m]), n)] @ U[(add(x, E[n]), m)].conj().T @ U[(x, n)].conj().T


def eta(U):
    best = 0.0
    for x in SITES:
        for m in range(4):
            for n in range(m + 1, 4):
                if add(x, E[m]) in SITESET and add(x, E[n]) in SITESET and add(add(x, E[m]), E[n]) in SITESET:
                    best = max(best, opn(I2 - plaq(U, x, m, n)))
    return best


ORDERS = list(itertools.permutations(range(4)))
O = (0, 0, 0, 0)
C1 = (O, 0)                       # 0 -> 3e0
C2 = ((3, 0, 0, 0), 1)            # 3e0 -> 3e0+3e1
C3 = ((0, 3, 0, 0), 0)            # 3e1 -> 3e0+3e1
C4 = (O, 1)                       # 0 -> 3e1
CS = [C1, C2, C3, C4]


def block(c):
    return [add(c, (a, b, cc, d)) for a in (-1, 0, 1) for b in (-1, 0, 1) for cc in (-1, 0, 1) for d in (-1, 0, 1)]


def contours(U, c, paired=True):
    start, m = c
    end = add(start, E[m], L)
    S = straight(U, start, m, L)
    out = []
    for y in block(start):
        leg = straight(U, y, m, L)
        yL = add(y, E[m], L)
        for s in ORDERS:
            A = axial(U, start, y, s)
            if paired:
                B = axial(U, end, yL, s)
                out.append(A @ leg @ B.conj().T)
            else:
                for s2 in ORDERS:
                    B = axial(U, end, yL, s2)
                    out.append(A @ leg @ B.conj().T)
    return S, out


def partA():
    ok = {k: True for k in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']}
    rmax1, rmax2 = 0.0, 0.0
    cfgs = [('R', t, sd) for t in (0.01, 0.05, 0.2) for sd in range(5)] + [('S1', 0, 0), ('S2', 0, 0), ('S3', 0, 0)]
    rng = np.random.default_rng(123)
    for kind, t, sd in cfgs:
        U = make_field(kind, t, sd)
        et = eta(U)
        Ss, Mb, ratios = [], [], []
        for c in CS:
            S, T = contours(U, c)
            d = max(opn(Tk - S) for Tk in T)
            ratios.append(d / et)
            Ss.append(S)
            Mb.append(sum(T) / len(T))
            if d > 9 * et:
                ok['A1'] = False
        SP = Ss[0] @ Ss[1] @ Ss[2].conj().T @ Ss[3].conj().T
        rsq = opn(I2 - SP) / et
        if rsq > 9:
            ok['A2'] = False
        print(f"A {kind} t={t} seed={sd}: eta={et:.3e} ribbon ratios={['%.4f' % r for r in ratios]} square ratio={rsq:.4f}")
        if kind == 'R':
            rmax1 = max(rmax1, max(ratios))
            rmax2 = max(rmax2, rsq)
            for s in (0.05, 0.3):
                for _ in range(5):
                    V = [S @ su2_exp(s * rng.standard_normal(3)) for S in Ss]
                    VP = V[0] @ V[1] @ V[2].conj().T @ V[3].conj().T
                    rhs = 9 * et + sum(opn(V[i] - Ss[i]) for i in range(4))
                    if opn(I2 - VP) > rhs:
                        ok['A3'] = False
            for i in range(4):
                S, M = Ss[i], Mb[i]
                dM = opn(M - S)
                Vs = []
                for _ in range(200):
                    q = rng.standard_normal(4)
                    q /= np.linalg.norm(q)
                    Vs.append(np.array([[q[0] + 1j * q[3], q[2] + 1j * q[1]], [-q[2] + 1j * q[1], q[0] - 1j * q[3]]]))
                for _ in range(200):
                    Vs.append(S @ su2_exp(0.3 * rng.standard_normal(3)))
                for V in Vs:
                    lhs = 1 - 0.5 * np.real(np.trace(V.conj().T @ M))
                    rhs = opn(V - S) ** 2 / 4 - dM
                    if lhs < rhs:
                        ok['A4'] = False
        if kind == 'S1':
            if not (8.9 <= ratios[0] <= 9.0):
                ok['A5'] = False
            print(f"  S1 sharp ribbon ratio = {ratios[0]:.6f}")
        if kind == 'S2':
            if not (8.9 <= rsq <= 9.0):
                ok['A5'] = False
            print(f"  S2 sharp square ratio = {rsq:.6f}")
        if kind == 'S3':
            S, Tu = contours(U, C1, paired=False)
            du = max(opn(Tk - S) for Tk in Tu) / et
            print(f"  S3 unpaired ribbon ratio = {du:.6f}; paired = {ratios[0]:.6f}")
            if not (du > 9.5 and ratios[0] <= 9):
                ok['A6'] = False
    print(f"A7 (informational): max ribbon ratio over R = {rmax1:.4f}, max square ratio over R = {rmax2:.4f}")
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    print('Part A', 'PASS' if all(ok.values()) else 'FAIL')


# ---------------------------------------------------------------- Part B
def fat(Y, T, d):
    out = set()
    for x in Y:
        for e in itertools.product((0, 1), repeat=d):
            out.add(tuple((x[k] + e[k]) % T for k in range(d)))
    return out


def touch(Y, Yp, T, d):
    for x in Y:
        for xp in Yp:
            if all(((x[k] - xp[k]) % T) in (0, 1, T - 1) for k in range(d)):
                return True
    return False


def comps(B, T, d):
    B = set(B)
    out = []
    while B:
        s = B.pop()
        comp, stack = {s}, [s]
        while stack:
            x = stack.pop()
            for e in itertools.product((-1, 0, 1), repeat=d):
                y = tuple((x[k] + e[k]) % T for k in range(d))
                if y in B:
                    B.remove(y)
                    comp.add(y)
                    stack.append(y)
        out.append(frozenset(comp))
    return out


def grow(rng, T, d, n):
    x = tuple(int(v) for v in rng.integers(0, T, d))
    Y = {x}
    while len(Y) < n:
        z = list(Y)[rng.integers(len(Y))]
        e = rng.integers(-1, 2, d)
        Y.add(tuple((z[k] + int(e[k])) % T for k in range(d)))
    return frozenset(Y)


def partB():
    T, d = 6, 4
    rng = np.random.default_rng(7)
    ok1 = True
    pairs = []
    for _ in range(3000):
        n1, n2 = rng.integers(1, 7, 2)
        Y = {tuple(int(v) for v in rng.integers(0, T, d)) for _ in range(n1)}
        Yp = {tuple(int(v) for v in rng.integers(0, T, d)) for _ in range(n2)}
        pairs.append((Y, Yp))
    for dist in (1, 2):
        for _ in range(500):
            x = tuple(int(v) for v in rng.integers(0, T, d))
            off = [int(v) for v in rng.integers(-dist, dist + 1, d)]
            k = int(rng.integers(d))
            off[k] = dist if rng.random() < 0.5 else -dist
            xp = tuple((x[i] + off[i]) % T for i in range(d))
            pairs.append(({x}, {xp}))
    nt = 0
    for Y, Yp in pairs:
        a = len(fat(Y, T, d) & fat(Yp, T, d)) > 0
        b = touch(Y, Yp, T, d)
        nt += b
        if a != b:
            ok1 = False
    print(f"B1: {len(pairs)} pairs, {nt} touching; equivalence", 'PASS' if ok1 else 'FAIL')
    ok2 = True
    for _ in range(2000):
        n = int(rng.integers(1, 13))
        B = {tuple(int(v) for v in rng.integers(0, T, d)) for _ in range(n)}
        cs = comps(B, T, d)
        fs = [fat(c, T, d) for c in cs]
        for i in range(len(fs)):
            for j in range(i + 1, len(fs)):
                if fs[i] & fs[j]:
                    ok2 = False
    nfam = 0
    for _ in range(2000):
        fam = []
        for _ in range(int(rng.integers(1, 5))):
            Y = grow(rng, T, d, int(rng.integers(1, 5)))
            if all(not (fat(Y, T, d) & fat(Z, T, d)) for Z in fam):
                fam.append(Y)
        nfam += len(fam)
        U = set().union(*fam)
        if set(comps(U, T, d)) != set(fam):
            ok2 = False
    print(f"B2: components/families ({nfam} sets in families)", 'PASS' if ok2 else 'FAIL')
    u = [0.0, 1.0, 0.7, -0.4, 0.9, 0.3, -0.2, 0.5, 0.1]
    cN = {}
    for T1 in (12, 14, 16):
        poly = np.zeros(T1 + 1)
        for mask in range(1 << T1):
            occ = [(mask >> i) & 1 for i in range(T1)]
            if all(occ):
                continue
            # rotate so that position 0 is empty, then read runs
            z = occ.index(0)
            occ = occ[z:] + occ[:z]
            w, run = 1.0, 0
            for o in occ + [0]:
                if o:
                    run += 1
                else:
                    if run:
                        w *= u[run] if run <= 8 else 0.0
                    run = 0
            poly[sum(occ)] += w
        # log(1 + p(t)), p = poly[1:] t^n
        p = poly.copy()
        p[0] = 0.0
        lg = np.zeros(6)
        powk = np.zeros(6)
        powk[0] = 1.0
        for k in range(1, 6):
            powk = np.convolve(powk, p[:6])[:6]
            lg += ((-1) ** (k + 1) / k) * powk
        cN[T1] = lg
        print(f"B3 T={T1}: c_N/T for N=1..4:", ['%.12f' % (lg[N] / T1) for N in range(1, 5)])
    ok3 = True
    for T1 in (12, 14):
        for N in range(1, 5):
            ref = cN[16][N] / 16
            if abs(cN[T1][N] / T1 - ref) > 1e-9 * max(1, abs(ref)):
                ok3 = False
    print('B3', 'PASS' if ok3 else 'FAIL')
    print('Part B', 'PASS' if (ok1 and ok2 and ok3) else 'FAIL')


# ---------------------------------------------------------------- Part C
def partC():
    ok = True
    for N in (2, 3):
        bp = 11 * N * N / (12 * math.pi ** 2)
        for e1 in (0.25, 0.5, 1.0, 2.0):
            a = 0.9 * e1 * e1 / (4 * N)
            ns = math.floor(4 / (a * bp))
            if not ((ns + 1) * a * bp > 4 >= ns * a * bp):
                ok = False
            print(f"C N={N} eps1={e1}: beta'={bp:.4f} a''={a:.5f} n_*={ns}")
    N, kap, e1 = 2, 1.0, 0.5
    A4 = 3 * L * (L - 1) / 2
    eta1 = min(e1 / (2 * L * L), e1 * e1 / (512 * N * A4))
    nl = 4 * L ** 3 * (L - 1)
    nP = 6 * nl
    b1 = nP + 12 * kap * (1 + A4) ** 2
    eloc = min(e1 / 4, math.sqrt(e1 * e1 / (4 * N * b1)))
    print(f"C RS constants (d=4, L=3, N=2, kappa=1, eps1=0.5): A_4={A4}, eta_1={eta1:.4e}, "
          f"plaquette exponent eta_1^2/(2N)={eta1 ** 2 / (2 * N):.4e}, kernel exponent kappa eps1^2/(256N)={kap * e1 * e1 / (256 * N):.4e}")
    print(f"C CL constants: n_l={nl}, n_P={nP}, b_1={b1:.1f}, eps_loc={eloc:.4e}")
    print('C1', 'PASS' if ok else 'FAIL')


# ---------------------------------------------------------------- Part D
def partD():
    pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
    mats, dets = [], []
    for perm in itertools.permutations(range(4)):
        for sg in itertools.product((1, -1), repeat=4):
            R = np.zeros((4, 4))
            for i in range(4):
                R[perm[i], i] = sg[i]
            W = np.zeros((6, 6))
            for I, (a, b) in enumerate(pairs):
                for J, (c, d) in enumerate(pairs):
                    W[I, J] = R[a, c] * R[b, d] - R[a, d] * R[b, c]
            mats.append(W)
            dets.append(round(np.linalg.det(R)))
    rng = np.random.default_rng(0)
    ok1, nrot = True, 0
    for _ in range(20):
        t = rng.standard_normal((6, 6))
        t = t + t.T
        avg = sum(W.T @ t @ W for W in mats) / len(mats)
        if np.max(np.abs(avg - np.trace(t) / 6 * np.eye(6))) > 1e-12:
            ok1 = False
        rot = [W for W, dd in zip(mats, dets) if dd == 1]
        avr = sum(W.T @ t @ W for W in rot) / len(rot)
        if np.max(np.abs(avr - np.trace(t) / 6 * np.eye(6))) >= 1e-3:
            nrot += 1
    print(f"D: {len(mats)} elements; D1", 'PASS' if ok1 else 'FAIL', f"; D2 rotation-average non-scalar in {nrot}/20",
          'PASS' if nrot >= 15 else 'FAIL')
    print('Part D', 'PASS' if (ok1 and nrot >= 15) else 'FAIL')


if __name__ == '__main__':
    {'A': partA, 'B': partB, 'C': partC, 'D': partD}[sys.argv[1]]()
