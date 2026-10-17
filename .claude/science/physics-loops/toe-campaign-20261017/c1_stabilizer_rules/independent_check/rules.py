"""Independent enumeration of O-symmetric nearest-neighbour stabilizer rules (claims 1,2)."""
import itertools, numpy as np, time
t0 = time.time()
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1, -1]).astype(complex)
PAULI = [I2, SX, SY, SZ]

# group O
O = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[i, perm[i]] = sg[i]
        if round(np.linalg.det(R)) == 1: O.append(R)
assert len(O) == 24

def Qmap(R, kind):
    A = np.abs(R); s = int(round(np.linalg.det(A)))
    return {'trivial': np.eye(3, dtype=int), 'sign': np.diag([1, s, s]),
            'axis': s * A, 'full': R}[kind]

def lift(M):
    """SU(2) U with U sigma_j U^dag = sum_i M_ij sigma_i, via nullspace of linear system."""
    rows = []
    for j in range(3):
        tgt = sum(M[i, j] * PAULI[i + 1] for i in range(3))
        # U s_j - tgt U = 0, vec(U) row-major
        Aj = np.kron(np.eye(2), PAULI[j + 1].T) - np.kron(tgt, np.eye(2))
        rows.append(Aj)
    A = np.vstack(rows)
    u, s, vh = np.linalg.svd(A)
    assert s[-1] < 1e-9 and s[-2] > 1e-6
    U = vh[-1].conj().reshape(2, 2)
    U = U / np.sqrt(np.linalg.det(U))
    assert np.allclose(U @ U.conj().T, I2)
    return U

def conj_table(U):
    """label l -> (label m, sign c) with U P_l U^dag = c P_m."""
    tab = {0: (0, 1)}
    for l in (1, 2, 3):
        C = U @ PAULI[l] @ U.conj().T
        for m in (1, 2, 3):
            c = np.trace(PAULI[m] @ C).real / 2
            if abs(abs(c) - 1) < 1e-9: tab[l] = (m, int(round(c)))
    assert len(tab) == 4
    return tab

STAR = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SIDX = {s: i for i, s in enumerate(STAR)}

def act(R, tab, string):
    """string: (sign, tuple of 7 labels) -> image."""
    sg, labs = string
    new = [0] * 7
    for i, l in enumerate(labs):
        if l == 0: continue
        m, c = tab[l]
        j = SIDX[tuple(int(v) for v in R @ np.array(STAR[i]))]
        new[j] = m; sg *= c
    return (sg, tuple(new))

def symp(labsA, offA, labsB, offB):
    """commutation (0 commute,1 anti) of string A at offset offA vs B at offB."""
    posA = {tuple(np.add(STAR[i], offA)): l for i, l in enumerate(labsA) if l}
    n = 0
    for i, l in enumerate(labsB):
        if not l: continue
        p = tuple(np.add(STAR[i], offB))
        if p in posA and posA[p] != l: n ^= 1
    return n

OFFS = [t for t in itertools.product(range(-2, 3), repeat=3) if sum(map(abs, t)) <= 2]

def comm_all(labsA, labsB):
    return all(symp(labsA, (0, 0, 0), labsB, t) == 0 for t in OFFS)

def run(kind):
    tabs = []
    for R in O:
        M = Qmap(R, kind); U = lift(M); tabs.append((R, conj_table(U)))
    # homomorphism check of Q
    for R1 in O:
        for R2 in O:
            assert (Qmap(R1 @ R2, kind) == Qmap(R1, kind) @ Qmap(R2, kind)).all()
    seen = set(); orbits = []; frustrated = 0
    for labs in itertools.product(range(4), repeat=7):
        if not any(labs) or labs in seen: continue
        orb = {}
        for R, tab in tabs:
            sg, l2 = act(R, tab, (1, labs))
            orb.setdefault(l2, set()).add(sg)
        seen |= set(orb)
        if any(len(v) > 1 for v in orb.values()): frustrated += 1; continue
        orbits.append({l: next(iter(v)) for l, v in orb.items()})
    # self-commuting orbits
    good = []
    for ob in orbits:
        L = list(ob)
        if all(comm_all(a, b) for a in L for b in L): good.append(ob)
    return orbits, frustrated, good

def classify(ob):
    labsets = set(l for s in ob for l in s if l)
    if len(labsets) == 1: return 'single-label'
    s = next(iter(ob))
    if len(ob) == 1 and s[0] and len(set(s[1:])) == 1 and s[1] and s[1] != s[0]: return 'cluster'
    return 'OTHER'

NAMES = 'IXYZ'
def show(ob):
    return ' | '.join(('+' if sg > 0 else '-') + ''.join(NAMES[l] for l in s) for s, sg in list(ob.items())[:3]) + (' ...' if len(ob) > 3 else '')

for kind in ['axis', 'full', 'trivial', 'sign']:
    orbits, fr, good = run(kind)
    print(f'== {kind}: {len(orbits)} sign-consistent orbits, {fr} sign-frustrated orbits, {len(good)} self-commuting')
    cls = [classify(g) for g in good]
    from collections import Counter
    print('   classes', Counter(cls))
    if kind in ('axis', 'full'):
        for g in good: print('   ', show(g))
    else:
        for g, c in zip(good, cls):
            if c != 'single-label': print('   ', c, show(g))
        # pairwise commutation between distinct self-commuting orbits
        bad = []
        for i in range(len(good)):
            for j in range(i + 1, len(good)):
                if all(comm_all(a, b) for a in good[i] for b in good[j]):
                    ci, cj = cls[i], cls[j]
                    li = set(l for s in good[i] for l in s if l); lj = set(l for s in good[j] for l in s if l)
                    if not (ci == cj == 'single-label' and li == lj): bad.append((show(good[i]), show(good[j])))
        print('   commuting pairs violating claim:', len(bad), bad[:5])
        # single-site creation of single violated generator for cluster orbits
        for g, c in zip(good, cls):
            if c != 'cluster': continue
            s = next(iter(g)); ok = False
            for lab in (1, 2, 3):
                # single-site Pauli lab at origin; count translates t (generator at t) anticommuting
                cnt = 0
                for t in OFFS:
                    pos = {tuple(np.add(STAR[i], t)): l for i, l in enumerate(s) if l}
                    if (0, 0, 0) in pos and pos[(0, 0, 0)] != lab: cnt += 1
                if cnt == 1: ok = True; print('     cluster', show(g), 'single violated by single-site', NAMES[lab])
            assert ok
print('time %.1fs' % (time.time() - t0))
