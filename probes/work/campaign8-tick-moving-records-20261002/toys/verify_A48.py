"""Coordinator check of A48's counting claims, written from scratch (no a48lib).
(a) Hom(O, O) into the 24 cubic rotations: 58 homs, image sizes 1/2/6/24 -> 1/9/24/24, four characters.
(b) KS signs on a 4^3 torus: 4/24 turns about the origin keep them as they stand; all 24 do up to a
    sign relabelling c_x -> e_x c_x; relabelled unit translations anticommute; period-2 ones commute.
(c) The largest set of turns keeping one axis line has 8 elements.  (d) spectra of s.s and -s.s differ."""
import itertools
import numpy as np

# (a) the rotation group O as signed permutation matrices with det +1
O = [np.array(M) for M in {tuple(map(tuple, s[:, None] * np.eye(3, dtype=int)[list(p)]))
     for p in itertools.permutations(range(3)) for s in map(np.array, itertools.product((1, -1), repeat=3))}
     if round(np.linalg.det(np.array(M))) == 1]
assert len(O) == 24
key = lambda M: tuple(M.flatten())
idx = {key(M): i for i, M in enumerate(O)}
mul = [[idx[key(A @ B)] for B in O] for A in O]
g4 = idx[key(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))]   # 90 deg about z
g3 = idx[key(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))]    # 120 deg about (1,1,1)
words = {idx[key(np.eye(3, dtype=int))]: []}                   # each element as a word in g4, g3
frontier = list(words)
while frontier:
    nxt = []
    for e in frontier:
        for gname, g in (("a", g4), ("b", g3)):
            f = mul[e][g]
            if f not in words:
                words[f] = words[e] + [gname]; nxt.append(f)
    frontier = nxt
assert len(words) == 24
homs = []
for ia, ib in itertools.product(range(24), repeat=2):
    img = {}
    for e, w in words.items():
        r = idx[key(np.eye(3, dtype=int))]
        for c in w:
            r = mul[r][ia if c == "a" else ib]
        img[e] = r
    if all(img[mul[x][y]] == mul[img[x]][img[y]] for x in range(24) for y in range(24)):
        homs.append(img)
sizes = sorted(len(set(h.values())) for h in homs)
counts = {s: sizes.count(s) for s in sorted(set(sizes))}
classes = []                                                    # conjugacy classes of O by element
for x in range(24):
    cl = frozenset(mul[mul[g][x]][[i for i in range(24) if mul[g][i] == idx[key(np.eye(3, dtype=int))]][0]] for g in range(24))
    if cl not in classes: classes.append(cl)
chars = {tuple(int(round(np.trace(O[h[min(cl)]]))) for cl in classes) for h in homs}
ok_a = len(homs) == 58 and counts == {1: 1, 2: 9, 6: 24, 24: 24} and len(chars) == 4
print(f"(a) homs O->O: {len(homs)}, by image size {counts}, distinct characters {len(chars)} {'OK' if ok_a else 'FAIL'}")

# (b) KS signs eta_1 = 1, eta_2 = (-1)^x1, eta_3 = (-1)^(x1+x2) on bonds of a 4^3 torus
L = 4
sites = list(itertools.product(range(L), repeat=3))
sid = {s: i for i, s in enumerate(sites)}
E = np.eye(3, dtype=int)
def eta(x, mu):
    return [1, (-1) ** x[0], (-1) ** (x[0] + x[1])][mu]
H = np.zeros((L**3, L**3))
bond = {}
for x in sites:
    for mu in range(3):
        y = tuple((np.array(x) + E[mu]) % L)
        H[sid[x], sid[y]] = H[sid[y], sid[x]] = eta(x, mu)
        bond[frozenset((sid[x], sid[y]))] = eta(x, mu)
def perm(f):                      # site map -> permutation matrix P with (P v)[f(x)] = v[x]
    P = np.zeros((L**3, L**3))
    for x in sites: P[sid[tuple(np.array(f(x)) % L)], sid[x]] = 1
    return P
def relabel(Hp):                  # find diagonal D = diag(+-1) with D Hp D = H, by spanning tree
    eps = {0: 1}; todo = [0]
    while todo:
        u = todo.pop()
        for v in np.nonzero(H[u])[0]:
            if v not in eps:
                eps[v] = eps[u] * H[u, v] * Hp[u, v]; todo.append(v)
    D = np.diag([eps[i] for i in range(L**3)])
    return D if np.allclose(D @ Hp @ D, H) else None
exact = solvable = 0
for R in O:
    P = perm(lambda x: R @ np.array(x))
    Hp = P @ H @ P.T
    exact += np.allclose(Hp, H)
    solvable += relabel(Hp) is not None
Tm = []
for a in range(3):
    P = perm(lambda x, a=a: np.array(x) + E[a])
    D = relabel(P @ H @ P.T)
    Tm.append(D @ P)
comm = [np.diag(Tm[a] @ Tm[b] @ np.linalg.inv(Tm[a]) @ np.linalg.inv(Tm[b]))[0] for a, b in ((0, 1), (1, 2), (0, 2))]
const = all(np.allclose(np.diag(Tm[a] @ Tm[b] @ np.linalg.inv(Tm[a]) @ np.linalg.inv(Tm[b])), c)
            for (a, b), c in zip(((0, 1), (1, 2), (0, 2)), comm))
T2 = [np.linalg.matrix_power(T, 2) for T in Tm]
comm2 = [np.allclose(T2[a] @ T2[b], T2[b] @ T2[a]) for a, b in ((0, 1), (1, 2), (0, 2))]
ok_b = exact == 4 and solvable == 24 and const and comm == [-1, -1, -1] and all(comm2)
print(f"(b) KS: exact {exact}/24, with relabelling {solvable}/24, unit-translation commutators {comm}, "
      f"period-2 commute {all(comm2)} {'OK' if ok_b else 'FAIL'}")

# (c) turns keeping one axis line (as a line, either sign), maximised over axis lines
best = 0
for n in itertools.product((-1, 0, 1), repeat=3):
    n = np.array(n)
    if not n.any(): continue
    best = max(best, sum(abs(abs(np.dot(R @ n, n)) - np.dot(n, n)) < 1e-9 for R in O))
print(f"(c) max turns keeping an axis line: {best} {'OK' if best == 8 else 'FAIL'}")

# (d) spectra of s.s and -s.s on two qubits
s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
SS = sum(np.kron(p, p) for p in s).real
e1, e2 = np.round(np.linalg.eigvalsh(SS), 9), np.round(np.linalg.eigvalsh(-SS), 9)
ok_d = list(e1) == [-3, 1, 1, 1] and list(e2) == [-1, -1, -1, 3]
print(f"(d) spectra s.s {list(e1)}, -s.s {list(e2)} {'OK' if ok_d else 'FAIL'}")
print("TOTAL:", "PASS" if ok_a and ok_b and ok_d and best == 8 else "FAIL")
