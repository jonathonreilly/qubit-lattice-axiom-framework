#!/usr/bin/env python3
"""Independent group-theory check for c16 (written from scratch).

O = proper cube rotations (24 signed permutation matrices, det +1).
2O = binary octahedral group in SU(2) (48 elements).
Checks: H^2(O;Z2), w1, w2, kernel to U(1); subgroup table; axis-D2 patterns;
odd orbits; induced representations of 2O for 6 / 8 / 12 orbits.
"""
import itertools
import numpy as np

np.set_printoptions(precision=4, suppress=True)
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = [SX, SY, SZ]

# ---------------------------------------------------------------- O
O = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[i, perm[i]] = signs[i]
        if round(np.linalg.det(M)) == 1:
            O.append(M)
assert len(O) == 24
N = 24
key = lambda M: tuple(M.flatten())
idx = {key(M): i for i, M in enumerate(O)}
mul = np.array([[idx[key(O[a] @ O[b])] for b in range(N)] for a in range(N)])
E = idx[key(np.eye(3, dtype=int))]
inv = [int(np.where(mul[a] == E)[0][0]) for a in range(N)]

DIRS = [np.array(v) for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


def perm_sign(p):
    p = list(p); s = 1
    seen = [False] * len(p)
    for i in range(len(p)):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = p[j]; L += 1
            if L % 2 == 0:
                s = -s
    return s


def dir_perm(M):
    return [next(j for j, w in enumerate(DIRS) if np.array_equal(M @ d, w)) for d in DIRS]


w1 = [0 if perm_sign(dir_perm(M)) == 1 else 1 for M in O]   # Z2-valued sign character
# sanity: w1 is a homomorphism
assert all(w1[mul[a, b]] == (w1[a] + w1[b]) % 2 for a in range(N) for b in range(N))


def rot_type(M):
    tr = int(np.trace(M))
    if np.array_equal(M, np.eye(3, dtype=int)):
        return "e"
    if tr == -1:
        return "C2axis" if np.count_nonzero(M - np.diag(np.diag(M))) == 0 else "C2edge"
    return {0: "C3", 1: "C4"}[tr]


types = [rot_type(M) for M in O]

# ---------------------------------------------------------------- 2O
def lift(M):
    """Continuous lift: U = cos(t/2) - i sin(t/2) n.sigma, t in (0, pi]."""
    R = M.astype(float)
    if np.allclose(R, np.eye(3)):
        return I2.copy()
    w, V = np.linalg.eig(R)
    n = np.real(V[:, np.argmin(abs(w - 1))]); n /= np.linalg.norm(n)
    c = (np.trace(R) - 1) / 2
    # choose sign of n so that the rotation angle is in (0, pi]
    Kx = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    s_est = np.trace(Kx.T @ R) / 2  # = sin t
    t = np.arctan2(s_est, c)
    if t < 0:
        n, t = -n, -t
    return np.cos(t / 2) * I2 - 1j * np.sin(t / 2) * sum(n[i] * SIG[i] for i in range(3))


def adj(U):
    return np.array([[np.real(np.trace(SIG[i] @ U @ SIG[j] @ U.conj().T)) / 2 for j in range(3)] for i in range(3)])


L = [lift(M) for M in O]
for i, M in enumerate(O):
    assert np.allclose(adj(L[i]), M)
G2 = L + [-U for U in L]          # element i (lift) and i+24 (minus lift)
proj = list(range(N)) + list(range(N))
NN = 48


def find2(U):
    for j, V in enumerate(G2):
        if np.allclose(U, V):
            return j
    raise ValueError


mul2 = np.array([[find2(G2[a] @ G2[b]) for b in range(NN)] for a in range(NN)])
E2 = 0 if np.allclose(G2[0], I2) else find2(I2)
E2 = find2(I2); MINUS = find2(-I2)
inv2 = [int(np.where(mul2[a] == E2)[0][0]) for a in range(NN)]

# w2 cocycle: L(g)L(h) = (-1)^{w2(g,h)} L(gh)
w2c = np.zeros((N, N), dtype=int)
for a in range(N):
    for b in range(N):
        P = L[a] @ L[b]
        w2c[a, b] = 0 if np.allclose(P, L[mul[a, b]]) else 1
        assert np.allclose(P, (-1) ** w2c[a, b] * L[mul[a, b]])
w1sq = np.array([[w1[a] * w1[b] for b in range(N)] for a in range(N)])

# ---------------------------------------------------------------- GF(2) linear algebra (python ints)
class Basis:
    def __init__(self):
        self.piv = {}
    def reduce(self, v):
        while v:
            h = v.bit_length() - 1
            if h in self.piv:
                v ^= self.piv[h]
            else:
                return v
        return 0
    def add(self, v):
        r = self.reduce(v)
        if r:
            self.piv[r.bit_length() - 1] = r
            return True
        return False
    def rank(self):
        return len(self.piv)


def cochain_to_int(f, elems):
    n = len(elems); v = 0
    for i in range(n):
        for j in range(n):
            if f[i][j]:
                v |= 1 << (i * n + j)
    return v


def H2_data(elems):
    """Return (dim Z2, dim B2, dimH2, basis of complement reps as dict-cochains) for subgroup elems."""
    n = len(elems); pos = {g: i for i, g in enumerate(elems)}
    m = lambda i, j: pos[mul[elems[i], elems[j]]]
    # coboundary operator d2 on 2-cochains: rows indexed by (g,h,k); build kernel via transpose rank
    # We compute Z2 = kernel of d2 by Gaussian elimination on the equation system.
    rows = Basis()
    for g in range(n):
        for h in range(n):
            for k in range(n):
                v = 0
                for (a, b) in [(h, k), (m(g, h), k), (g, m(h, k)), (g, h)]:
                    v ^= 1 << (a * n + b)
                rows.add(v)
    dimZ = n * n - rows.rank()
    # B2 = image of d1
    B = Basis()
    for g in range(n):
        f = [[0] * n for _ in range(n)]
        for a in range(n):
            for b in range(n):
                f[a][b] = ((a == g) + (b == g) + (m(a, b) == g)) % 2
        B.add(cochain_to_int(f, elems))
    dimB = B.rank()
    return dimZ, dimB, dimZ - dimB, rows, B


def is_cocycle(c, elems):
    n = len(elems); pos = {g: i for i, g in enumerate(elems)}
    for g in elems:
        for h in elems:
            for k in elems:
                if (c[h][k] + c[mul[g, h]][k] + c[g][mul[h, k]] + c[g][h]) % 2:
                    return False
    return True


def extension_has_1d_rep(c, elems):
    """Is the central element z=(e,1) outside the commutator subgroup of E_c?"""
    els = [(g, a) for g in elems for a in (0, 1)]
    def emul(x, y):
        return (mul[x[0], y[0]], (x[1] + y[1] + c[x[0]][y[0]]) % 2)
    def einv(x):
        for y in els:
            if emul(x, y) == (E, 0):
                return y
    invs = {x: einv(x) for x in els}
    comms = {emul(emul(x, y), emul(invs[x], invs[y])) for x in els for y in els}
    S = set(comms) | {(E, 0)}
    changed = True
    while changed:
        changed = False
        for x in list(S):
            for y in list(S):
                z = emul(x, y)
                if z not in S:
                    S.add(z); changed = True
    return (E, 1) not in S


def lift_square_pattern(c, invols):
    # (g,0)^2 = (g^2, c(g,g)) = (e, c(g,g)) for an involution g
    return tuple('-' if c[g][g] else '+' for g in invols)


out = []
def report(s):
    print(s); out.append(s)

# ---------------------------------------------------------------- 1. H^2(O;Z2)
allO = list(range(N))
dimZ, dimB, dimH, rows, Bb = H2_data(allO)
report(f"[O] dim Z^2={dimZ} dim B^2={dimB} dim H^2(O;Z2)={dimH}")
assert is_cocycle(w2c, allO) and is_cocycle(w1sq, allO)
bb = Basis(); bb.piv = dict(Bb.piv)
i_w2 = cochain_to_int(w2c, allO); i_w1 = cochain_to_int(w1sq, allO)
ind = bb.add(i_w2) and bb.add(i_w1)
report(f"[O] w2, w1^2 cocycles; independent mod B^2: {ind} (so they span H^2)")
axisC2 = [g for g in allO if types[g] == "C2axis"]
edgeC2 = [g for g in allO if types[g] == "C2edge"]
classes = {"0": np.zeros((N, N), int), "w1^2": w1sq, "w2": w2c, "w2+w1^2": (w2c + w1sq) % 2}
for nm, c in classes.items():
    one = extension_has_1d_rep(c, allO)
    pa = set(lift_square_pattern(c, axisC2)); pe = set(lift_square_pattern(c, edgeC2))
    report(f"[O] class {nm:8s}: 1-dim rep with z->-1 exists (U(1)-trivial): {one}; "
           f"axis-C2 lift^2 {pa}, edge-C2 lift^2 {pe}")
# second method: u(g) = i^{w1(g)} has coboundary w1 cup w1
ok = all(np.isclose((1j ** w1[a]) * (1j ** w1[b]) / (1j ** w1[mul[a, b]]), (-1) ** w1sq[a, b]) for a in allO for b in allO)
report(f"[O] u(g)=i^w1(g) gives du = (-1)^(w1 cup w1): {ok}")
# w1 equals S4 sign (perm of the four body diagonals)
DIAG = [np.array(v) for v in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]]
def diag_perm(M):
    return [next(j for j, w in enumerate(DIAG) if np.array_equal(M @ d, w) or np.array_equal(M @ d, -w)) for d in DIAG]
report(f"[O] w1 (sign on six directions) == sign on four body diagonals (S4 sign): "
       f"{all(w1[i] == (0 if perm_sign(diag_perm(O[i])) == 1 else 1) for i in allO)}")
report("[O] w1 by class: " + str({t: sorted({w1[g] for g in allO if types[g] == t}) for t in sorted(set(types))}))

# ---------------------------------------------------------------- 2. subgroups
def closure(gens):
    S = {E} | set(gens)
    changed = True
    while changed:
        changed = False
        for a in list(S):
            for b in list(S):
                c = mul[a, b]
                if c not in S:
                    S.add(c); changed = True
    return frozenset(S)

subs = set()
for a in allO:
    for b in allO:
        subs.add(closure([a, b]))
subs = list(subs)
def conj(S, x):
    return frozenset(mul[mul[x, s], inv[x]] for s in S)
cls = []
for S in subs:
    if not any(S in C for C in cls):
        cls.append({conj(S, x) for x in allO})
report(f"[sub] subgroups: {len(subs)}, conjugacy classes: {len(cls)}")

def name(S):
    n = len(S); t = sorted(types[g] for g in S if g != E)
    if n == 1: return "C1"
    if n == 2: return "C2(axis)" if t == ["C2axis"] else "C2(edge)"
    if n == 3: return "C3"
    if n == 4:
        if "C4" in t: return "C4"
        return "D2(axis)" if t.count("C2axis") == 3 else "D2(1 axis+2 edge)"
    return {6: "D3", 8: "D4", 12: "T", 24: "O"}[n]

pre = lambda S: [j for j in range(NN) if proj[j] in S]
def minus_in_commutator(Sl):
    comms = {mul2[mul2[x, y], mul2[inv2[x], inv2[y]]] for x in Sl for y in Sl}
    T = set(comms) | {E2}
    changed = True
    while changed:
        changed = False
        for x in list(T):
            for y in list(T):
                z = mul2[x, y]
                if z not in T:
                    T.add(z); changed = True
    return MINUS in T, len(T)

table = []
for C in sorted(cls, key=lambda C: (len(next(iter(C))), name(next(iter(C))))):
    S = next(iter(C)); el = sorted(S)
    forced, ncomm = minus_in_commutator(pre(S))
    # restriction-of-w2 test, second method: Z2 extension restricted
    c = [[0] * N for _ in range(N)]
    for a in el:
        for b in el:
            c[a][b] = int(w2c[a, b])
    one = extension_has_1d_rep(c, el)
    assert one == (not forced)
    dZ, dB, dH, _, _ = H2_data(el)
    # kernel size of H^2(S;Z2)->H^2(S;U(1)) = |Hom(S,U(1))| / |Hom(S,U(1))^2| = number of Z2-chars...
    table.append((name(S), len(S), len(C), 24 // len(S), forced, ncomm, dH))
    report(f"[sub] {name(S):18s} |H|={len(S):2d} #conj={len(C):2d} index={24//len(S):2d}  "
           f"w2|H forces dim>=2: {forced}  |[H~,H~]|={ncomm:2d}  dim H^2(H;Z2)={dH}")
forced_set = sorted(t[0] for t in table if t[4])
report(f"[sub] w2 forces degeneracy exactly for: {forced_set}")
odd = sorted(t[0] for t in table if t[3] % 2 == 1)
report(f"[orbit] subgroups of odd index (odd O-orbits): {odd}")

# ---------------------------------------------------------------- axis D2 patterns
D2 = sorted([E] + axisC2)
invs = axisC2
n = len(D2)
dZ, dB, dH, rows, Bd = H2_data(D2)
# enumerate all cocycles on D2 by brute force over Z^2 representatives: build cocycle basis
pos = {g: i for i, g in enumerate(D2)}
# brute-force: all functions D2xD2->Z2 normalized (c(e,*)=c(*,e)=0): 2^9 candidates
pats = {}
nonE = [g for g in D2 if g != E]
for bits in itertools.product([0, 1], repeat=9):
    c = [[0] * N for _ in range(N)]
    k = 0
    for a in nonE:
        for b in nonE:
            c[a][b] = bits[k]; k += 1
    if is_cocycle(c, D2):
        p = lift_square_pattern(c, invs)
        one = extension_has_1d_rep(c, D2)
        pats.setdefault(p, set()).add(one)
report(f"[D2axis] dim H^2={dH}; patterns realized: {len(pats)}")
for p in sorted(pats):
    report(f"[D2axis] pattern {p} #minus={p.count('-')}  1-dim: {pats[p]}")
c = [[0] * N for _ in range(N)]
for a in D2:
    for b in D2:
        c[a][b] = int(w2c[a, b])
report(f"[D2axis] w2 restricted pattern: {lift_square_pattern(c, invs)}")

# ---------------------------------------------------------------- 4. induced reps of 2O
def sym3(U):
    a, b, cc, d = U[0, 0], U[0, 1], U[1, 0], U[1, 1]
    # action on homogeneous cubic polys: x -> a x + c y, y -> b x + d y (U^T on variables)
    M = np.zeros((4, 4), dtype=complex)
    for col in range(4):
        p = np.poly1d([1])  # polynomial in t = y/x ... use explicit expansion
    # explicit: basis e_k = x^(3-k) y^k
    from numpy.polynomial import polynomial as P
    X = np.array([cc, a])  # coefficients in y (constant term = coeff of x): a x + c y -> [a, c] in powers of y
    X = np.array([a, cc]); Y = np.array([b, d])
    for k in range(4):
        poly = np.array([1.0 + 0j])
        for _ in range(3 - k):
            poly = P.polymul(poly, X)
        for _ in range(k):
            poly = P.polymul(poly, Y)
        poly = np.pad(poly, (0, 4 - len(poly)))
        M[:, k] = poly
    return M

def e_rep(M):
    # O -> S3 on three coordinate axes, then standard 2-dim rep
    p = [int(np.nonzero(M[:, i])[0][0]) for i in range(3)]  # axis i -> axis p[i]
    P3 = np.zeros((3, 3))
    for i in range(3):
        P3[p[i], i] = 1
    B = np.array([[1, -1, 0], [1, 1, -2]]).T / np.array([np.sqrt(2), np.sqrt(6)])
    return B.T @ P3 @ B

reps = {
    "A1": lambda j: np.eye(1),
    "A2": lambda j: np.array([[(-1) ** w1[proj[j]]]]),
    "E": lambda j: e_rep(O[proj[j]]),
    "T1": lambda j: O[proj[j]].astype(float),
    "T2": lambda j: (-1) ** w1[proj[j]] * O[proj[j]].astype(float),
    "E1/2": lambda j: G2[j],
    "E5/2": lambda j: (-1) ** w1[proj[j]] * G2[j],
    "G3/2": lambda j: sym3(G2[j]),
}
chars = {}
for nm, r in reps.items():
    mats = [np.array(r(j), dtype=complex) for j in range(NN)]
    hom = all(np.allclose(mats[a] @ mats[b], mats[mul2[a, b]]) for a in range(NN) for b in range(NN))
    ch = np.array([np.trace(m) for m in mats])
    norm = np.sum(abs(ch) ** 2) / NN
    chars[nm] = ch
    report(f"[2O] irrep {nm:5s} dim={int(round(ch[E2].real))} homomorphism={hom} <chi,chi>={norm:.6f} chi(-1)={ch[MINUS].real:+.0f}")
gram = np.array([[np.vdot(chars[a], chars[b]) / NN for b in chars] for a in chars])
report(f"[2O] character orthonormality: {np.allclose(gram, np.eye(8))}; sum dim^2 = {sum(int(round(chars[k][E2].real))**2 for k in chars)}")
# label sanity: E1/2 vs E5/2 on the C4 lift with trace +sqrt2
gC4 = find2(lift(next(M for M in O if rot_type(M) == "C4" and M[2, 2] == 1)))
report(f"[2O] on g=lift(+90deg about z) (trace {np.trace(G2[gC4]).real:+.4f}): chi_E1/2={chars['E1/2'][gC4].real:+.4f} "
       f"chi_E5/2={chars['E5/2'][gC4].real:+.4f} chi_G3/2={chars['G3/2'][gC4].real:+.4f}")


def induced(point, gen_axis_rot):
    stab = [i for i in allO if np.array_equal(O[i] @ point, point)]
    K = pre(stab)
    g = find2(lift(O[gen_axis_rot]))
    order = 1; x = g
    while x != E2:
        x = mul2[x, g]; order += 1
    assert order == len(K)
    powers = {}
    x = E2
    for m in range(order):
        powers[x] = m; x = mul2[x, g]
    assert set(powers) == set(K)
    res = {}
    for k in range(order):
        chi = {h: np.exp(2j * np.pi * k * powers[h] / order) for h in K}
        ind = np.zeros(NN, dtype=complex)
        for y in range(NN):
            s = 0
            for x in range(NN):
                c_ = mul2[mul2[x, y], inv2[x]]
                if c_ in chi:
                    s += chi[c_]
            ind[y] = s / len(K)
        dec = {nm: np.vdot(chars[nm], ind) / NN for nm in chars}
        dec = {nm: int(round(v.real)) for nm, v in dec.items() if abs(v) > 1e-9}
        assert all(abs(np.vdot(chars[nm], ind) / NN - round((np.vdot(chars[nm], ind) / NN).real)) < 1e-9 for nm in chars)
        res[k] = dec
    return len(stab), order, np.trace(G2[g]).real, res

def gen_for(point, typ):
    for i in allO:
        if types[i] == typ and np.array_equal(O[i] @ point, point):
            # pick the rotation by the smallest positive angle about +point (right-handed)
            U = lift(O[i])
            ax = np.array([np.imag(np.trace(U @ s)) for s in SIG])  # = -2 sin(t/2) n
            n_ = -ax
            if typ == "C2edge" or np.dot(n_, point) > 1e-9:
                return i
    raise ValueError

for label, pt, typ in [("six directions", np.array([0, 0, 1]), "C4"),
                       ("eight octants", np.array([1, 1, 1]), "C3"),
                       ("twelve face diagonals", np.array([1, 1, 0]), "C2edge")]:
    ns, order, tr, res = induced(pt, gen_for(pt, typ))
    report(f"[induce] {label}: |stab|={ns}, lift Z{order}, generator = continuous lift of the right-handed {typ} about {tuple(pt)} (trace {tr:+.4f})")
    for k, dec in res.items():
        kind = "linear" if k % 2 == 0 else "spinorial"
        s = " + ".join((f"{v} " if v > 1 else "") + nm for nm, v in dec.items())
        report(f"[induce]    k={k} ({kind}): {s}")
    if typ == "C4":
        # effect of the other generator choice g' = -g = g^5
        report("[induce]    (with generator -g = g^5 instead, k -> 5k mod 8: odd labels 1<->5, 3<->7 swap)")

open(__file__.replace("grouptheory.py", "grouptheory.out"), "w").write("\n".join(out) + "\n")
