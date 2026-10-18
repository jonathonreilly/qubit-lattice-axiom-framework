"""C8 check (a): class 1 (momentum-shifting / doubled-cell letters), own code on the B26 checker's model (mymodel.py).
No C8 / b26lib / chklib / chk_model import.  Real space: L = 4 torus, modes (v, c)."""
import os, sys, itertools, collections, time
os.environ.setdefault('OMP_NUM_THREADS', '3')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mymodel import *
import sympy
from sympy.matrices.normalforms import smith_normal_form
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
t0 = time.time(); rng = np.random.default_rng(8801)
L = 4
SITES = list(itertools.product(range(L), repeat=3))
MID = {(v, c): i for i, (v, c) in enumerate((v, c) for v in SITES for c in range(12))}
NM = len(MID)
def m4(v): return tuple(int(x) % L for x in v)
def real(X):
    """block dict -> real-space matrix on the L^3 torus"""
    M = np.zeros((NM, NM), complex)
    for v in SITES:
        for a, B in X.items():
            w = m4(add(v, a))
            for i, c in zip(*np.nonzero(B)): M[MID[(w, i)], MID[(v, c)]] += B[i, c]
    return M
def Greal(g):
    M = np.zeros((NM, NM))
    for v in SITES:
        Rv = m4(rd(g['M'], v))
        for c in range(12):
            M[MID[(Rv, CI[rc(g['M'], CORN[c])])], MID[(v, c)]] = (-1.0) ** (int(np.dot(g['lam'], v)) + g['tau'][c])
    return M
def Treal(t):
    M = np.zeros((NM, NM))
    for v in SITES:
        for c in range(12): M[MID[(m4(add(v, t)), c)], MID[(v, c)]] = 1
    return M
def DQ(q): return np.diag([(-1.0) ** int(np.dot(q, v)) for v in SITES for c in range(12)])
GR = [Greal(g) for g in PROPER]; CH = [g['chi'] for g in PROPER]
SUBL = list(itertools.product((0, 1), repeat=3))

# ---------------- single-Q letters
Y = real({Z0: rand_onsite_unitary(rng)})      # a translation-invariant symmetric letter
Y = Y @ real(RL)
ok = True
for q in SUBL:
    X = DQ(q) @ Y
    for t in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]:
        T = Treal(t); ok &= np.allclose(T @ X @ T.T, (-1.0) ** int(np.dot(q, t)) * X)
        ok &= np.allclose(T @ DQ(q) @ X @ T.T, DQ(q) @ X)          # D_Q X is translation invariant
check("X = D_Q Y has T_t X T_t^-1 = e^{iQ.t} X and D_Q X is translation-invariant (Y transl.-inv.)", ok)
ok = True
for g, G in zip(PROPER, GR):
    for q in SUBL:
        Rq = tuple(int(x) % 2 for x in g['M'] @ np.array(q))
        ok &= np.allclose(G @ DQ(q) @ G.T, DQ(Rq))
check("G_g D_Q G_g^-1 = D_{RQ} for 24 dressed rotations x 8 Q", ok)
orbs = set()
for q in SUBL: orbs.add(frozenset(tuple(int(x) % 2 for x in g['M'] @ np.array(q)) for g in PROPER))
sizes = sorted(len(o) for o in orbs)
check("O-orbits of pi{0,1}^3: sizes [1,1,3,3]; fixed: 0 and Pi", sizes == [1, 1, 3, 3], f"{sizes}")
# general Q: fixed points of O on the torus R^3/2piZ^3, scanned on (pi/12)Z^3 (contains pi/8? no -> also (pi/8)Z^3)
fixed = []
for N in (8, 12):
    for n in itertools.product(range(2 * N), repeat=3):
        Q = np.array(n) * np.pi / N
        if all(np.allclose(np.mod(g['M'] @ Q - Q + 1e-9, 2 * np.pi), 0, atol=1e-6) for g in PROPER): fixed.append(tuple(np.round(Q / np.pi, 4)))
fixed = sorted(set(fixed))
check("O-fixed momenta on (pi/8)Z^3 and (pi/12)Z^3 grids are exactly 0 and Pi (consistent with the 3-line proof for general Q)", fixed == [(0, 0, 0), (1, 1, 1)], f"{fixed}")
# D_Pi commutation table
DP_ = DQ((1, 1, 1))
lets = {'S': real(S1), 'A0': real({Z0: A0m}), 'H_on': real({Z0: HON0}), 'Lambda': real(LAMX), 'L123': real({Z0: PC['L123']}),
        'R_L': real(RL), 'Rt': real(RTX)}
res = {n: ('comm' if np.allclose(DP_ @ M, M @ DP_) else ('anti' if np.allclose(DP_ @ M, -M @ DP_) else 'neither')) for n, M in lets.items()}
check("D_Pi commutes with S, A0, H_on, Lambda, PC letter; anticommutes with R_L and Rt", res == dict(S='comm', A0='comm', H_on='comm', Lambda='comm', L123='comm', R_L='anti', Rt='anti'), f"{res}")
kst = np.array([1, -1, 1]) * np.pi / 2; PI = np.pi * np.ones(3)
check("k* + Pi = -k* mod 2pi", np.allclose(np.mod(kst + PI - (-kst), 2 * np.pi) % (2 * np.pi), 0))
# Bloch-level Pi taste
def Wk(w, k):
    M = np.eye(12, dtype=complex)
    for t in w:
        if not isinstance(t, str): M = M @ t; continue
        if t == 'R': M = M @ bloch(RL, k)
        elif t == 'Rt': M = M @ bloch(RTX, k)
        elif t == 'S': M = M @ Sk(k, 1)
        elif t == 'Si': M = M @ Sk(k, -1)
        elif t == 'S2': M = M @ Sk(k, 2)
        elif t in ('E+', 'E-'): s = 1 if t == 'E+' else -1; M = M @ (np.eye(12) + 1j * s * bloch(RL, k)) / np.sqrt(2)
        else: M = M @ t
    return M
ok = True
for _ in range(200):
    n = rng.integers(2, 7); w = [rng.choice(['R', 'Rt', 'S', 'Si', 'S2', 'o']) for _ in range(n)]
    w = [rand_onsite_unitary(rng) if t == 'o' else str(t) for t in w]; nR = sum(1 for t in w if isinstance(t, str) and t in ('R', 'Rt'))
    k = rng.uniform(-np.pi, np.pi, 3); ok &= np.allclose(Wk(w, k + PI), (-1) ** nR * Wk(w, k))
check("old words (S^{+-1,2}, R_L, Rt, symmetric on-site unitaries): W(k+Pi) = (-1)^{n_R} W(k)  (200 random)", ok)

# ---------------- doubled-cell orbits
ELEM = []      # (perm array on modes, sign array, chi) for O x 2Z^3 on L=4
for g, G in zip(PROPER, GR):
    for t in itertools.product((0, 2), repeat=3):
        M = Treal(t) @ G
        perm = np.argmax(np.abs(M), axis=0); sg = M[perm, np.arange(NM)]
        ELEM.append((perm, sg, g['chi']))
check("O x (2Z/4Z)^3 on L=4: 192 signed permutations", len(ELEM) == 192 and all(np.allclose(np.abs(s), 1) for _, s, _ in ELEM))
def cellmode(i):
    for (v, c), j in MID.items():
        if j == i: return tuple(x % 2 for x in v), c
MODES = list(MID.keys())
seen = set(); ORB = []
for i, (v, c) in enumerate(MODES):
    if i in seen: continue
    o = sorted(set(int(p[i]) for p, _, _ in ELEM)); seen |= set(o); ORB.append(o)
def desc(o):
    v, c = MODES[o[0]]; s = tuple(x % 2 for x in v); w = sum(s)
    if w in (0, 3): typ = 'none'
    else:
        ax = [i for i in range(3) if s[i] == (1 if w == 1 else 0)][0]
        typ = 'par' if any(abs(d[ax]) == 1 for d in CORN[c]) else 'perp'
    stab = sum(1 for p, _, _ in ELEM if p[o[0]] == o[0])
    return (w, typ, len(o) // 8, stab)        # modes per doubled cell (L=4 torus = 8 doubled cells), stabiliser order mod 2Z^3
D = sorted(desc(o) for o in ORB)
print("  orbits (sublattice weight, corner type, modes per doubled cell, stabiliser order):", D)
check("6 orbits per doubled cell; sizes 12,12,12,12,24,24; stabiliser order 2 (C2') for the four 12-orbits, 1 (free) for 100-par and 110-par",
      D == sorted([(0, 'none', 12, 2), (3, 'none', 12, 2), (1, 'perp', 12, 2), (2, 'perp', 12, 2), (1, 'par', 24, 1), (2, 'par', 24, 1)]), f"{D}")
# stabiliser of a 12-orbit representative is a C2' (rotation by pi about a face diagonal)
okc2 = True
for o in ORB:
    if len(o) // 8 != 12: continue
    st = [k for k, (p, _, _) in enumerate(ELEM) if p[o[0]] == o[0]]
    Ms = [PROPER[k // 8]['M'] for k in st]
    nontriv = [M for M in Ms if not np.allclose(M, np.eye(3))]
    okc2 &= all(np.allclose(M @ M, np.eye(3)) and round(np.trace(M)) == -1 and not np.allclose(M, np.diag(np.diag(M))) for M in nontriv) and len(nontriv) > 0
check("the non-trivial stabiliser rotation of each 12-orbit is a C2' (2-fold about a face diagonal: trace -1, not an axis C2)", okc2)

# ---------------- pieces by orbit propagation (own algorithm, not group averaging)
def piece(src, tgt, twist):
    """X with X[tgt, src] = 1, covariant: X[h t, h s] = chi(h)^-1 s_h(t) s_h(s).  None if inconsistent or not a partial perm."""
    col = {}
    for p, sg, ch in ELEM:
        w = (ch if twist else 1) * sg[tgt] * sg[src]
        a, b = int(p[src]), int(p[tgt])
        if a in col:
            if col[a][0] != b or abs(col[a][1] - w) > 1e-9: return None
        else: col[a] = (b, w)
    rows = [b for b, _ in col.values()]
    if len(set(rows)) != len(rows): return None
    return col
def disp(i, j):
    vi, _ = MODES[i]; vj, _ = MODES[j]; d = tuple(((b - a + 1) % L) - 1 for a, b in zip(vi, vj)); return d
cnt = {}; R0 = {}
for oi, o in enumerate(ORB):
    src = o[0]; vs, cs = MODES[src]; n = 0; n0 = collections.Counter(); r0 = collections.defaultdict(list)
    for a in itertools.product((-1, 0, 1), repeat=3):
        for c in range(12):
            tgt = MID[(m4(add(vs, a)), c)]
            for tw in (False, True):
                pc = piece(src, tgt, tw)
                if pc is not None:
                    n += 1
                    if a == (0, 0, 0): n0[tw] += 1; r0[tw].append(pc)
    cnt[desc(o)] = (n, dict(n0)); R0[oi] = r0
print("  pieces per orbit (range<=1 valid pieces, range-0 per character):", cnt)
okp = all((v[0] == 6 and v[1] == {False: 1, True: 1}) if k[2] == 12 else (v[0] == 336 and v[1] == {False: 8, True: 8}) for k, v in cnt.items())
check("range<=1 pieces: 6 per C2' orbit, 336 per free orbit; range 0: C2' one per character, free 8 per character", okp)
# C2' range-0 pieces are identity (chi=1) and antipodal (chi=A2)
okid = True
for oi, o in enumerate(ORB):
    if len(o) // 8 != 12: continue
    for tw in (False, True):
        pc = R0[oi][tw][0]; src = o[0]; tgt = pc[src][0]
        okid &= (MODES[tgt][1] == (ANTI[MODES[src][1]] if tw else MODES[src][1]))
check("C2' range-0 pieces: identity for chi=1, antipodal corner for chi=A2", okid)

# ---------------- G0: perm parts and translation-invariant members
FREE = [oi for oi, o in enumerate(ORB) if len(o) // 8 == 24]; C2O = [oi for oi, o in enumerate(ORB) if len(o) // 8 == 12]
def perm_part(tw, choice):
    """mode->(target, sign) on the whole torus for a perm choice (index per free orbit), unit phases"""
    col = {}
    for oi in C2O: col.update(R0[oi][tw][0])
    for oi, ch in zip(FREE, choice): col.update(R0[oi][tw][ch])
    return col
def sub_blocks(col, phase=None):
    """per sublattice s: 12x12 block (target corner, source corner) if every target is on-site; phases per orbit"""
    B = {s: np.zeros((12, 12), complex) for s in SUBL}
    for v in SITES:
        s = tuple(x % 2 for x in v)
        for c in range(12):
            i = MID[(v, c)]; tgt, w = col[i]
            assert MODES[tgt][0] == v
            ph = 1 if phase is None else phase[ORBOF[i]]
            B[s][MODES[tgt][1], c] = w * ph
    return B
ORBOF = {}
for oi, o in enumerate(ORB):
    for i in o: ORBOF[i] = oi
PERMS = []
for tw in (False, True):
    for choice in itertools.product(range(8), repeat=2):
        col = perm_part(tw, choice); B = sub_blocks(col)
        PERMS.append((tw, choice, col, B))
check("G0 perm parts: 2 x 64 = 128", len(PERMS) == 128)
def sindep(B, tol=1e-9): return all(np.allclose(B[s], B[SUBL[0]], atol=tol) for s in SUBL)
pat = [(tw, ch) for tw, ch, col, B in PERMS if sindep({s: np.abs(b) for s, b in B.items()})]
check("exactly one perm part per character is sublattice-independent (|.| pattern)", len(pat) == 2 and {p[0] for p in pat} == {False, True}, f"{pat}")
# exhaustive count of translation-invariant G0 letters
ntinv = 0; tinv_ops = []
for tw, ch, col, B in PERMS:
    if not sindep({s: np.abs(b) for s, b in B.items()}): continue
    for ph in itertools.product(range(4), repeat=6):
        phase = {oi: 1j ** ph[oi] for oi in range(6)}
        Bp = sub_blocks(col, phase)
        if sindep(Bp): ntinv += 1; tinv_ops.append((tw, Bp[SUBL[0]]))
iden = []
for tw, M in tinv_ops:
    for z in PHASE:
        if np.allclose(M, z * np.eye(12)): iden.append(('1', z))
        if np.allclose(M, z * A0m): iden.append(('A0', z))
check("translation-invariant G0 letters: exactly 8 = {z*1} (chi=1) + {z*A0} (chi=A2), z in {+-1,+-i}  (exhaustive over 524,288)",
      ntinv == 8 and len(iden) == 8 and sorted(set(x[0] for x in iden)) == ['1', 'A0'], f"{ntinv}, {iden}")

# ---------------- a R_L b lemma
RLb = {a: B for a, B in RL.items()}
def aRb_blocks(Ba, Bb):
    """(a R_L b) block at displacement d for source sublattice s: Ba[s+d] R_d Bb[s]"""
    return {d: {s: Ba[tuple((x + y) % 2 for x, y in zip(s, d))] @ R @ Bb[s] for s in SUBL} for d, R in RLb.items()}
def tinv(blk, absval=False):
    f = (lambda x: np.abs(x)) if absval else (lambda x: x)
    return all(all(np.allclose(f(blk[d][s]), f(blk[d][SUBL[0]]), atol=1e-9) for s in SUBL) for d in blk)
adm = []
for i, (twa, cha, cola, Ba) in enumerate(PERMS):
    for j, (twb, chb, colb, Bb) in enumerate(PERMS):
        if tinv(aRb_blocks({s: np.abs(x) for s, x in Ba.items()}, {s: np.abs(x) for s, x in Bb.items()}), absval=True): adm.append((i, j))
admset = {(PERMS[i][0], PERMS[i][1], PERMS[j][0], PERMS[j][1]) for i, j in adm}
expect = {(pa[0], pa[1], pb[0], pb[1]) for pa in pat for pb in pat}
check("a R_L b support pattern is translation-invariant only if both perm parts are the s-independent ones (all 128^2 pairs)", admset == expect, f"{len(adm)} admissible")
# phases: integer constraint matrix in units of 2pi; U(1) phases per orbit (not only Z4)
def constraint(i, j):
    """rows: x_a[orb] + x_b[orb] differences (units of 2pi) and the inhomogeneous half-integer offsets from the signs"""
    twa, cha, cola, Ba = PERMS[i]; twb, chb, colb, Bb = PERMS[j]
    base = {}; A = []; C = []; Bm = []; keys = []
    for d, R in RLb.items():
        for c in range(12):
            for s in SUBL:
                ib = MID[(s, c)]; tb, wb = colb[ib]; cb = MODES[tb][1]
                for rr in np.nonzero(np.abs(R[:, cb]) > 1e-12)[0]:
                    ia = MID[(m4(add(s, d)), rr)]; ta, wa = cola[ia]
                    vec = np.zeros(12, int); vec[ORBOF[ia]] += 1; vec[6 + ORBOF[ib]] += 1
                    sgn = 0 if wa * wb * np.sign(R[rr, cb].real) > 0 else 1
                    key = (d, c, int(rr))
                    if key in base: A.append(vec - base[key][0]); C.append((base[key][1] - sgn) % 2)
                    else: base[key] = (vec, sgn); Bm.append(vec); keys.append(key)
    return np.array(A), np.array(C), np.array(Bm), keys
allwords = set(); info = []
REF = {}
RA = mul({Z0: A0m}, RL); AR = mul(RL, {Z0: A0m})
for nm, X in (('R_L', RL), ('Rt', RTX), ('A0 R_L', RA), ('R_L A0', AR)):
    for z in PHASE: REF[(nm, z)] = X
def ident(blk):
    for (nm, z), X in REF.items():
        if set(blk) == set(X) and all(np.allclose(blk[d], z * X[d], atol=1e-9) for d in X): return f"{z}*{nm}"
    return None
okcont = True; kdims = []
for (i, j) in adm:
    A, Cv, Bm, keys = constraint(i, j)
    rk = np.linalg.matrix_rank(A.astype(float))
    _, sv, Vh = np.linalg.svd(A.astype(float)); K = Vh[rk:]            # real kernel (continuous solutions)
    img = Bm @ K.T                                                     # entry-phase directions
    # continuous solutions only move entry phases uniformly per character factor: image spanned by the all-ones vector
    r_img = np.linalg.matrix_rank(np.hstack([img, np.ones((len(Bm), 1))]), tol=1e-8)
    okcont &= r_img == 1; kdims.append(12 - rk)
    snf = smith_normal_form(sympy.Matrix(A), domain=sympy.ZZ)
    inv = sorted(set(int(abs(snf[k, k])) for k in range(min(snf.shape)) if snf[k, k] != 0))
    N = int(np.lcm(int(np.lcm.reduce(inv)) if inv else 1, 4))
    # enumerate x in (Z/N)^12 with x_a[0] = x_b[0] = 0 (global phases factored out), vectorised
    free = [k for k in range(12) if k not in (0, 6)]
    X = np.array(list(itertools.product(range(N), repeat=len(free))), dtype=np.int64).T
    Xf = np.zeros((12, X.shape[1]), np.int64); Xf[free] = X
    good = np.all((A @ Xf - (N // 2) * Cv[:, None]) % N == 0, axis=0); sols = Xf[:, good]
    words = set()
    for x in sols.T:
        phA = {oi: np.exp(2j * np.pi * x[oi] / N) for oi in range(6)}; phB = {oi: np.exp(2j * np.pi * x[6 + oi] / N) for oi in range(6)}
        blk = aRb_blocks(sub_blocks(PERMS[i][2], phA), sub_blocks(PERMS[j][2], phB))
        assert tinv(blk)
        b0 = {d: blk[d][SUBL[0]] for d in blk}
        for z in PHASE:                                                   # the 4 global Z4 phases
            words.add(ident({d: z * B for d, B in b0.items()}))
    info.append((PERMS[i][0], PERMS[j][0], rk, inv, N, int(good.sum()), sorted(words, key=str)))
    allwords |= words
for x in info: print("  pair (twist_a, twist_b) =", x[:2], "rank", x[2], "SNF invariants", x[3], "enum mod", x[4], "solutions", x[5], "words", x[6])
check("continuous phase solutions of a R_L b change the word only by an overall scalar (kernel includes gauge directions that leave the word fixed)", okcont, f"kernel dims {kdims}")
check("all translation-invariant a R_L b (a, b in G0, Z_N phases with N >= SNF exponent, x Z4 global) are z*{R_L, Rt, A0 R_L, R_L A0}: 16 words",
      None not in allwords and len(allwords) == 16, f"{len(allwords)}")
# conjugates P R_L P^-1 and P Rt P^-1 for translation-invariant results are Hermitian -> z = +-1 and not A0 R_L / R_L A0
herm = [w for w in allwords if w and ('A0' not in w) and w.split('*')[0] in ('1', '-1', '(1+0j)', '(-1+0j)', '(-0-1j)')]
check("Hermitian members (possible conjugates P R_L P^-1) are only +-R_L, +-Rt: A0 R_L and R_L A0 are not Hermitian",
      not np.allclose(bloch(RA, [0.3, 0.1, 0.7]), bloch(RA, [0.3, 0.1, 0.7]).conj().T) and not np.allclose(bloch(AR, [0.3, 0.1, 0.7]), bloch(AR, [0.3, 0.1, 0.7]).conj().T))
# random numerical spot check of the lemma with random U(1) phases
okr = True; nt = 0
for _ in range(300):
    i, j = rng.integers(128), rng.integers(128)
    phA = {oi: np.exp(1j * rng.uniform(0, 2 * np.pi)) for oi in range(6)}; phB = {oi: np.exp(1j * rng.uniform(0, 2 * np.pi)) for oi in range(6)}
    blk = aRb_blocks(sub_blocks(PERMS[i][2], phA), sub_blocks(PERMS[j][2], phB)); t = tinv(blk); nt += t
    okr &= (not t) or ((i, j) in adm)
check("300 random (a, b) with random U(1) orbit phases: translation invariance only for admissible perm pairs", okr, f"{nt} invariant")
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.0f}s]")
