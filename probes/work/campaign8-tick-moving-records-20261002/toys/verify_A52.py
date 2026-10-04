"""Coordinator check of A52's construction, from scratch (no a52lib).
Rule T_f at a corner with record direction f (body diagonal): hop along d carries the field factor of leg d' iff
  f.d > 0 > f.d'   or   sign(f.d) = sign(f.d') and d' = R_f d   (R_f = right-handed 120-degree turn about f).
(a) T_f is a tournament for all 8 diagonals; the stated example at f0 = (1,1,1).
(b) Covariance T_{g f}(g d, g d') = T_f(d, d') for all 24 turns and 8 diagonals.
(c) Exactly 32 C3-invariant tournaments on the 6 legs, none transitive.
(d) Z2 Pauli form at one corner: hop_d = X_d prod_{T(d,d')} Z_d'; all 15 pairs anticommute; all 20 triples have
    theta = s12 s13 s23 = -1; control: the bare hops (no dressing) give +1.
(e) CZ relabelling: for two diagonals f, f', V = prod_{pairs where T_f, T_f' disagree} CZ maps every T_f hop onto the
    T_f' hop (up to sign), dense on 6 link qubits.
(f) pi-flux cubic hopping (Kawamoto-Smit phases) has |E| = 2t sqrt(sum cos^2 k)."""
import itertools
import numpy as np
O = [np.array(M) for M in {tuple(map(tuple, s[:, None] * np.eye(3, dtype=int)[list(p)]))
     for p in itertools.permutations(range(3)) for s in map(np.array, itertools.product((1, -1), repeat=3))}
     if round(np.linalg.det(np.array(M))) == 1]
LEGS = [s * np.eye(3, dtype=int)[a] for a in range(3) for s in (1, -1)]        # +x -x +y -y +z -z
lid = lambda v: [i for i, w in enumerate(LEGS) if np.array_equal(w, v)][0]
DIAG = [np.array(s) for s in itertools.product((1, -1), repeat=3)]
def R120(f):          # right-handed 120-degree turn about f, as an integer matrix in O
    f = np.array(f) / np.linalg.norm(f)
    for M in O:
        if np.allclose(M @ f, f) and np.isclose(np.trace(M), 0):         # a 120-degree turn about f
            v = np.cross(f, [1, 0, 0]) if abs(f[0]) < 0.9 else np.cross(f, [0, 1, 0])
            if np.dot(np.cross(v, M @ v), f) > 0: return M
def T(f):
    R = R120(f); t = np.zeros((6, 6), int)
    for i, j in itertools.permutations(range(6), 2):
        a, b = np.dot(f, LEGS[i]), np.dot(f, LEGS[j])
        if (a > 0 > b) or (np.sign(a) == np.sign(b) and np.array_equal(LEGS[j], R @ LEGS[i])): t[i, j] = 1
    return t
ok = True
Ts = {tuple(f): T(f) for f in DIAG}
tour = all(np.array_equal(t + t.T, 1 - np.eye(6, dtype=int)) for t in Ts.values())
t0 = Ts[(1, 1, 1)]
ex = ({j for j in range(6) if t0[0, j]} == {1, 3, 5, 2}) and ({j for j in range(6) if t0[1, j]} == {3})
ok &= tour and ex
print(f"(a) tournament for all 8 diagonals: {tour}; example (+x carries -x,-y,-z,+y; -x carries -y): {ex}")
cov = all(Ts[tuple(g @ f)][lid(g @ LEGS[i]), lid(g @ LEGS[j])] == Ts[tuple(f)][i, j]
          for g in O for f in DIAG for i in range(6) for j in range(6) if i != j)
ok &= cov
print(f"(b) covariance over 24 turns x 8 diagonals: {cov}")
R = R120((1, 1, 1)); perm = [lid(R @ LEGS[i]) for i in range(6)]
pairs = list(itertools.combinations(range(6), 2))
cnt = trans = 0
for bits in range(2**15):
    t = np.zeros((6, 6), int)
    for k, (i, j) in enumerate(pairs):
        if bits >> k & 1: t[i, j] = 1
        else: t[j, i] = 1
    if all(t[perm[i], perm[j]] == t[i, j] for i in range(6) for j in range(6)):
        cnt += 1; trans += sorted(t.sum(1)) == list(range(6))
ok &= cnt == 32 and trans == 0
print(f"(c) C3-invariant tournaments: {cnt} (A52: 32), transitive among them: {trans}")
def s(i, j, t):      # commutation sign of hop_i, hop_j in the Z2 Pauli form (X on own link, Z on carried legs)
    return (-1) ** (t[i, j] + t[j, i])
th = [s(i, j, t0) * s(i, k, t0) * s(j, k, t0) for i, j, k in itertools.combinations(range(6), 3)]
bare = np.zeros((6, 6), int)
thb = [s(i, j, bare) * s(i, k, bare) * s(j, k, bare) for i, j, k in itertools.combinations(range(6), 3)]
pairs_ac = all(s(i, j, t0) == -1 for i, j in pairs)
ok &= pairs_ac and all(x == -1 for x in th) and all(x == 1 for x in thb)
print(f"(d) 15/15 pairs anticommute: {pairs_ac}; theta over 20 triples: {set(th)}; bare control: {set(thb)}")
X = np.array([[0, 1], [1, 0]]); Z = np.diag([1, -1]); I2 = np.eye(2)
def op(fs):
    out = np.array([[1.0]])
    for k in range(6): out = np.kron(out, fs.get(k, I2))
    return out
def hops(t):
    return [op({i: X, **{j: Z for j in range(6) if t[i, j]}}) for i in range(6)]
worst = 0.0
for f, fp in itertools.combinations(DIAG, 2):
    t, tp = Ts[tuple(f)], Ts[tuple(fp)]
    V = np.ones(64)
    for i, j in pairs:
        if t[i, j] != tp[i, j]:
            zi = np.array([1 - 2 * ((st >> (5 - i)) & 1) for st in range(64)]); zj = np.array([1 - 2 * ((st >> (5 - j)) & 1) for st in range(64)])
            V *= np.where((zi < 0) & (zj < 0), -1, 1)
    for h, hp in zip(hops(t), hops(tp)):
        m = V[:, None] * h * V[None, :]
        worst = max(worst, min(np.abs(m - hp).max(), np.abs(m + hp).max()))
ok &= worst < 1e-12
print(f"(e) CZ relabelling maps T_f hops onto T_f' hops for all 28 pairs of diagonals: max residual {worst:.1e}")
L = 6; sites = list(itertools.product(range(L), repeat=3)); sid = {x: i for i, x in enumerate(sites)}
H = np.zeros((L**3, L**3))
for x in sites:
    for a in range(3):
        y = list(x); y[a] = (y[a] + 1) % L
        eta = (-1) ** sum(x[:a])
        H[sid[x], sid[tuple(y)]] += eta; H[sid[tuple(y)], sid[x]] += eta
ev = np.sort(np.abs(np.linalg.eigvalsh(H)))
ks = 2 * np.pi * np.arange(L) / L
pred = np.sort(np.array([2 * np.sqrt(sum(np.cos(k)**2 for k in kk)) for kk in itertools.product(ks, repeat=3)]))
pred2 = np.sort(np.concatenate([pred, pred]))[::2]   # |E| values come in +/- pairs on the KS lattice
res = np.abs(np.sort(np.unique(np.round(ev, 9))) - np.sort(np.unique(np.round(pred, 9)))).max()
ok &= res < 1e-8
print(f"(f) pi-flux bands: distinct |E| match 2 sqrt(sum cos^2 k) to {res:.1e}")
print("TOTAL:", "PASS" if ok else "FAIL")
