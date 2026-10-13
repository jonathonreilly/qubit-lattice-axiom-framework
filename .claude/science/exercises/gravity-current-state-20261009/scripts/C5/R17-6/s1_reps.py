# R17-6 s1: representation content of qubit slot labels under the natural
# (pure permutation) action and the shift (signed) action of proper cubic O,
# for every Wyckoff position of P432, at Gamma, R and on the X and M stars.
import itertools, numpy as np
np.set_printoptions(precision=4, suppress=True)
# --- group O: 24 signed permutation matrices with det +1
G = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[perm[i], i] = signs[i]
        if round(np.linalg.det(M)) == 1: G.append(M)
assert len(G) == 24
def cls(M):
    tr = np.trace(M)
    if tr == 3: return 'E'
    if tr == 0: return 'C3'
    if tr == 1: return 'C4'
    return 'C2' if np.count_nonzero(M - np.diag(np.diag(M))) == 0 else "C2'"
CL = ['E', 'C3', 'C2', 'C4', "C2'"]
cnt = {c: sum(cls(M) == c for M in G) for c in CL}
assert [cnt[c] for c in CL] == [1, 8, 3, 6, 6]
IRR = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'E': [2, -1, 2, 0, 0],
       'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, -1, -1, 1]}
def decompose(chi_by_elem):
    out = {}
    for name, ch in IRR.items():
        s = sum(np.conj(ch[CL.index(cls(M))]) * chi_by_elem[i] for i, M in enumerate(G)) / 24
        assert abs(s.imag) < 1e-9 and abs(s.real - round(s.real)) < 1e-9, (name, s)
        if round(s.real): out[name] = int(round(s.real))
    return out
def red(p): return tuple(np.round(np.mod(np.array(p, float), 1.0), 9) % 1.0)
# --- slot sets: list of (position, sign-function) ; sign function gives the
# factor with which the slot's label maps under g (natural action: always +1)
def orbit(p0):
    pts = []
    for M in G:
        q = red(M @ np.array(p0, float))
        if q not in pts: pts.append(q)
    return pts
WYCK = {'1a (0,0,0) O': (0, 0, 0), '1b (1/2,1/2,1/2) O': (.5, .5, .5),
        '3c (0,1/2,1/2) D4': (0, .5, .5), '3d (1/2,0,0) D4': (.5, 0, 0),
        '6e (x,0,0) C4': (.2, 0, 0), '6f (x,1/2,1/2) C4': (.2, .5, .5),
        '8g (x,x,x) C3': (.2, .2, .2), '12h (x,1/2,0) C2': (.2, .5, 0),
        "12i (0,y,y) C2'": (0, .2, .2), "12j (1/2,y,y) C2'": (.5, .2, .2),
        '24k general C1': (.1, .2, .37)}
def rep_chars(slots, q_star, signfun):
    # slots: list of (pos tuple, type); basis: (q in star, slot). D(g) maps
    # (q,s) -> (gq reduced, gs) with phase exp(i (gq - q_red).p') ; signfun(g,s)
    chis = []
    for M in G:
        ch = 0j
        for qi, q in enumerate(q_star):
            gq = M @ np.array(q, float)
            # q fixed mod 2pi Z^3 ?
            d = (gq - np.array(q, float)) / (2 * np.pi)
            if np.max(np.abs(d - np.round(d))) > 1e-9: continue
            for (p, t) in slots:
                gp = red(M @ np.array(p, float)); gt = act_type(M, t)
                if gp == red(p) and gt == t:
                    ch += signfun(M, t) * np.exp(1j * (gq - np.array(q)) @ np.array(gp))
        chis.append(ch)
    return chis
def act_type(M, t):
    if t is None: return None
    # t = sorted pair of axes (i,j) (i==j diagonal)
    i, j = t
    gi = int(np.nonzero(M[:, i])[0][0]); gj = int(np.nonzero(M[:, j])[0][0])
    return tuple(sorted((gi, gj)))
def sign_shift(M, t):
    if t is None: return 1
    i, j = t
    if i == j: return 1
    gi = int(np.nonzero(M[:, i])[0][0]); gj = int(np.nonzero(M[:, j])[0][0])
    return int(M[gi, i] * M[gj, j])
nat = lambda M, t: 1
pi = np.pi
STARS = {'Gamma': [(0, 0, 0)], 'R': [(pi, pi, pi)],
         'X*': [(pi, 0, 0), (0, pi, 0), (0, 0, pi)],
         'M*': [(pi, pi, 0), (0, pi, pi), (pi, 0, pi)]}
print('Group O built: class sizes', cnt)
print('\n(1) one untyped qubit per orbit point, NATURAL action (pure permutation)')
for name, p0 in WYCK.items():
    sl = [(p, None) for p in orbit(p0)]
    row = {s: decompose(rep_chars(sl, st, nat)) for s, st in STARS.items()}
    print(f'{name:22s} n={len(sl):2d} ' + ' | '.join(f'{s}: {row[s]}' for s in STARS))
print('\n(2) N0914 slot placement (typed slots: diag xx,yy,zz at sites; face ij at x+(ei+ej)/2)')
diag = [((0., 0., 0.), (i, i)) for i in range(3)]
face = [(red(np.array([1 if a in (i, j) else 0 for a in range(3)]) / 2), (i, j)) for i, j in [(0, 1), (1, 2), (0, 2)]]
for lab, sl in [('diag slots', diag), ('face slots', face)]:
    for act, f in [('natural', nat), ('shift (signed)', sign_shift)]:
        row = {s: decompose(rep_chars(sl, st, f)) for s, st in STARS.items()}
        print(f'{lab:10s} {act:15s} ' + ' | '.join(f'{s}: {row[s]}' for s in STARS))
print('\n(3) T2 multiplicity at Gamma by Frobenius = dim of H_p-fixed vectors in T2:')
for name, p0 in WYCK.items():
    H = [M for M in G if red(M @ np.array(p0, float)) == red(p0)]
    fix = sum(IRR['T2'][CL.index(cls(M))] for M in H) / len(H)
    print(f'  {name:22s} |H_p|={len(H):2d} classes={sorted(set(cls(M) for M in H))} -> mult(T2) = {fix:.0f}')
# (4) helicity characters of Sym^2 components along the symmetric directions
print('\n(4) little-group eigenvalues of Sym^2 channels (TT / V / S) along symmetric k')
def sym2_action(M):
    # action on symmetric 3x3 tensors T -> M T M^T, in basis of 6 components
    basis = []
    for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]:
        B = np.zeros((3, 3)); B[i, j] = B[j, i] = 1 if i != j else 1; basis.append(B / np.linalg.norm(B))
    D = np.array([[np.sum(b2 * (M @ b1 @ M.T)) for b1 in basis] for b2 in basis]); return D, basis
def channel_proj(khat, basis):
    k = np.array(khat, float); k /= np.linalg.norm(k); P = np.eye(3) - np.outer(k, k)
    def tt(T): return P @ T @ P - 0.5 * P * np.trace(P @ T)
    A = np.array([[np.sum(b2 * tt(b1)) for b1 in basis] for b2 in basis])
    S = np.outer(k, k); Sv = np.array([np.sum(b * (np.trace(P) * 0 + 1) * (np.outer(k, k))) for b in basis])
    return A
def rot(axis, ang):
    a = np.array(axis, float); a /= np.linalg.norm(a); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.round(np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K, 12)
for khat, ang, nm in [((0, 0, 1), pi / 2, 'C4 about z'), ((1, 1, 0), pi, "C2' about 110"), ((1, 1, 1), 2 * pi / 3, 'C3 about 111')]:
    M = rot(khat, ang); D, basis = sym2_action(M)
    Ptt = channel_proj(khat, basis)
    k = np.array(khat, float) / np.linalg.norm(khat)
    # scalar channel: trace and kk (2-dim); vector: k_(i e_j) with e perp k
    w_tt = np.linalg.eigvals(Ptt @ D @ Ptt)
    tt_ev = sorted([complex(np.round(x, 6)) for x in w_tt if abs(x) > 1e-6], key=lambda z: (z.real, z.imag))
    # vector projector
    P = np.eye(3) - np.outer(k, k)
    def vv(T): return P @ T @ np.outer(k, k) + np.outer(k, k) @ T @ P
    Pv = np.array([[np.sum(b2 * vv(b1)) for b1 in basis] for b2 in basis])
    v_ev = sorted([complex(np.round(x, 6)) for x in np.linalg.eigvals(Pv @ D @ Pv) if abs(x) > 1e-6], key=lambda z: (z.real, z.imag))
    print(f'  {nm:15s} TT: {tt_ev}   V: {v_ev}')
