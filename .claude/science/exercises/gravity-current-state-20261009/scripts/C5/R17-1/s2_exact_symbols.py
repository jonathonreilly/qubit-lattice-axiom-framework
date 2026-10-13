"""R17-1 s2 (written before running). Exact TT f-sum symbols for three qubit/Z_N models, label probe.
 mu6 = minimal F2-invariant pattern (weight 6, face slots, from s1); all 24 proper cubic rotations.
 (A) CSS model H_S = -U sum X^{G_row} - K sum_{x,R} Z^{R mu6_x}. Identity: m1(k) = K sum_R sum_{s in R mu}|c_s|^2
     provided <X_s X_t> = 0 for s != t in a pattern (checked: X_s X_t not in the X-stabilizer group, GF(2) rank on L=6 torus).
 (B) dipole hop: delta = R mu_x - R mu_{x+a}; m1(k) = w * sum |chat.mu(k)|^2 |1 - e^{ik.a}|^2.
 (C) minimal single-pattern M0=0 lift of mu6 (charge-2 quadrupole hop).
 (D) integer-invariant lift (the N=3 weight-10 lift with G delta = 0 found in s1) -> k^4 (R16-7 regime).
 Slopes of log symbol vs log k on k = 1e-3..0.3, five directions, both TT polarizations. No subtraction.
"""
import numpy as np, itertools
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
TIDX = {t: n for n, t in enumerate(TYPES)}
E3 = np.eye(3, dtype=int)
def G_entries(x, t):
    i, j = TYPES[t]; x = np.array(x); out = []
    if i == j: out += [((tuple(x - E3[j]), j), 1), ((tuple(x), j), -1)]
    else: out += [((tuple(x), j), 1), ((tuple(x + E3[i]), j), -1), ((tuple(x), i), 1), ((tuple(x + E3[j]), i), -1)]
    return out
def pos(x, t):
    i, j = TYPES[t]; p = np.array(x, float)
    if i != j: p = p + 0.5*(E3[i] + E3[j])
    return p
def Gof(supp):
    chk = {}
    for (x, t), v in supp:
        for g, c in G_entries(x, t): chk[g] = chk.get(g, 0) + c*v
    return {g: v for g, v in chk.items() if v != 0}
def rot_mats():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product([1,-1], repeat=3):
            R = np.zeros((3,3), int)
            for a in range(3): R[a, perm[a]] = sg[a]
            if round(np.linalg.det(R)) == 1: Rs.append(R)
    return Rs
def rotate(supp, R):
    out = []
    for (x, t), v in supp:
        i, j = TYPES[t]; p = R @ pos(x, t)
        ii = int(np.argmax(np.abs(R[:, i]))); jj = int(np.argmax(np.abs(R[:, j])))
        sgn = int(R[ii, i]*R[jj, j]); tt = TIDX[tuple(sorted((ii, jj)))]
        base = p - (0.5*(E3[ii] + E3[jj]) if ii != jj else 0)
        out.append(((tuple(int(round(b)) for b in base), tt), v*sgn))
    return out
mu6 = [((1,1,0),3,1),((1,1,0),4,1),((1,1,0),5,1),((1,1,1),3,1),((1,2,0),5,1),((2,1,0),4,1)]
mu6 = [((x, t), v) for x, t, v in mu6]
lift6 = [((1,1,0),3,1),((1,1,0),4,1),((1,1,0),5,1),((1,1,1),3,-1),((1,2,0),5,-1),((2,1,0),4,-1)]
lift6 = [((x, t), v) for x, t, v in lift6]
int10 = None  # find the integer-invariant lift of the N=3 weight-10 pattern
p3 = [((0,1,0),5,2),((0,1,1),2,1),((0,1,1),5,1),((1,1,0),0,1),((1,1,0),5,1),((1,1,1),0,1),((1,1,1),2,1),((1,1,1),5,2),((1,1,2),0,1),((2,1,1),2,1)]
p3 = [((x, t), v) for x, t, v in p3]
for ch in itertools.product([0,1], repeat=len(p3)):
    d = [(s, v if c == 0 else v - 3) for (s, v), c in zip(p3, ch)]
    if not Gof(d): int10 = d; break
Rs = rot_mats()
print("proper rotations:", len(Rs))
ok = all(all(v % 2 == 0 for v in Gof(rotate(mu6, R)).values()) for R in Rs)
print("(check) all 24 rotations of mu6 are F2-invariant:", ok)
print("(check) int10 integer-invariant lift found:", int10 is not None, " entries:", sorted(set(v for s, v in int10)))
print("(check) lift6 G delta (integer):", {(g[0], g[1]): v for g, v in Gof(lift6).items()})
# orbit of mu6 up to translation
def canon(supp):
    xs = np.array([x for (x, t), v in supp]); mn = xs.min(0)
    return tuple(sorted(((tuple(np.array(x) - mn), t) for (x, t), v in supp)))
orbit = {}
for R in Rs:
    r = rotate(mu6, R); orbit.setdefault(canon(r), r)
orb = list(orbit.values())
print("distinct rotated copies of mu6 (mod translation):", len(orb))

# (A) X_s X_t in X-stabilizer group? GF(2) rank test on L=6 torus
L = 6
slots = [(x, t) for x in itertools.product(range(L), repeat=3) for t in range(6)]
sidx = {s: n for n, s in enumerate(slots)}
rows = {}
for (x, t) in slots:
    for (g, j), v in G_entries(x, t):
        gg = (tuple(np.mod(g, L)), j); rows.setdefault(gg, np.zeros(len(slots), np.uint8))
        rows[gg][sidx[(x, t)]] ^= (v % 2)
Gm = np.array(list(rows.values()), np.uint8)
def gf2_rank(M):
    M = M.copy() % 2; r = 0; nr, nc = M.shape
    for c in range(nc):
        piv = np.nonzero(M[r:, c])[0]
        if len(piv) == 0: continue
        p = r + piv[0]; M[[r, p]] = M[[p, r]]
        nz = np.nonzero(M[:, c])[0]; nz = nz[nz != r]
        M[nz] ^= M[r]; r += 1
        if r == nr: break
    return r
rk = gf2_rank(Gm)
print("(A) L=6 torus: slots %d, Gauss rows %d, GF(2) rank %d" % (len(slots), Gm.shape[0], rk))
bad = 0; tested = 0
for p in orb:
    sl = [(tuple(np.mod(np.array(x) + 2, L)), t) for (x, t), v in p]
    for a, b in itertools.combinations(sl, 2):
        v = np.zeros(len(slots), np.uint8); v[sidx[a]] = 1; v[sidx[b]] = 1
        tested += 1
        if gf2_rank(np.vstack([Gm, v])) == rk: bad += 1
print("(A) pairs X_s X_t (s != t in one rotated pattern) tested: %d ; in X-stabilizer group: %d" % (tested, bad))

# exact symbols
def chat(supp, k, eps):
    tot = 0j
    for (x, t), v in supp:
        i, j = TYPES[t]; c = eps[i, j] if i == j else 2*eps[i, j]
        tot += np.exp(1j*k @ pos(x, t))*c*v
    return tot
def tt_pols(kh):
    kh = kh/np.linalg.norm(kh); a = np.array([1.0, 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(kh, a); u /= np.linalg.norm(u); v = np.cross(kh, u)
    return [(np.outer(u,u) - np.outer(v,v))/np.sqrt(2), (np.outer(u,v) + np.outer(v,u))/np.sqrt(2)]
dirs = [np.array(d, float) for d in [(1,0,0),(1,1,0),(1,1,1),(1,2,3),(0.3,-0.7,1.1)]]
ks = np.array([1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1])
def mA(k, eps):  # CSS model, K = 1
    return sum(abs(eps[TYPES[t][0], TYPES[t][1]] if TYPES[t][0] == TYPES[t][1] else 2*eps[TYPES[t][0], TYPES[t][1]])**2
               for p in orb for (x, t), v in p)
def mB(k, eps):
    return sum(abs(chat(p, k, eps))**2 * abs(1 - np.exp(1j*k @ a))**2 for p in orb for a in E3.astype(float))
lifts6 = []
for R in Rs:
    r = rotate(lift6, R); lifts6.append(r)
def mC(k, eps): return sum(abs(chat(p, k, eps))**2 for p in lifts6)
ints = [rotate(int10, R) for R in Rs]
def mD(k, eps): return sum(abs(chat(p, k, eps))**2 for p in ints)
for name, f in [("(A) CSS pure clock characters Z^{R mu6}", mA), ("(B) dipole hop R mu6_x -> R mu6_{x+a}", mB),
                ("(C) single-pattern M0=0 lift of mu6 (x24 rotations)", mC), ("(D) integer-invariant lift (N=3 w=10, x24)", mD)]:
    print("\n" + name)
    for d in dirs:
        for pi, eps in enumerate(tt_pols(d)):
            vals = np.array([f(kk*d/np.linalg.norm(d), eps) for kk in ks])
            sl = np.diff(np.log(np.abs(vals) + 1e-300))/np.diff(np.log(ks))
            print("  dir %-18s pol %d: m1(1e-3) = %.4e ; m1/k^2 (1e-3) = %.4e ; slopes %s" %
                  (np.round(d, 2), pi, vals[0], vals[0]/ks[0]**2, np.round(sl, 3)))
