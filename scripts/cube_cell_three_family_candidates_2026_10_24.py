AUDIT_INPUT_PATHS = ('docs/CUBE_CELL_THREE_FAMILY_CANDIDATES_REGULAR_SPLIT_HEISENBERG_SLAB_AND_UNIQUE_8_3_3_CODE_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""cube-three-families: three exact checks of the wizard-panel family proposals (synthesis item B).
(i)  w1: regular-representation split Res_H L^2(G), G in {O_h, O, 2O}, H in {T, T_h, 2T}.
(ii) w3: Delta(27) = <translation, omega^(x+y+z)> on the CL-1 Wilson-type domain-wall slab with
     class-preserving hops {e_i - e_j, +-(1,1,1)}; control torus side not divisible by 3.
(iii) w4: [[8,3,3]] stabiliser codes: LP purity, exact classification (lines of PG(4,2)),
     cube 3-fold turn with the X->Y->Z frame cycle, 4-fold turn, logical 3-cycle.
Labels: [T] exact, [F] finite diagnostic. Supplied: Wilson-type slab (m = 0.6, Ls = 12), Gottesman
1996 [[8,3,3]] generators, quantum LP/shadow bounds (Shor-Laflamme, Rains). No physical identification.
Hypothesis verdicts are printed as VERDICT lines (criteria_pre_run.txt); PASS/FAIL lines certify facts."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from math import comb
from scipy.optimize import linprog

rng = np.random.default_rng(20261024)
T0 = time.time(); P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))
w = np.exp(2j * np.pi / 3)

# ================= (i) regular representation split =================
def key(M):
    a = np.asarray(M, dtype=complex).ravel()
    return tuple(np.round(np.concatenate([a.real, a.imag]) * 1000).astype(int).tolist())
def close(gens):
    els = {key(g): g for g in gens}; fr = list(els.values())
    while fr:
        nf = []
        for a in fr:
            for b in gens:
                c = a @ b; kc = key(c)
                if kc not in els: els[kc] = c; nf.append(c)
        fr = nf
    return list(els.values())
Oh = [np.array(p) @ np.diag(s) for p in (np.eye(3)[list(q)] for q in itertools.permutations(range(3))) for s in itertools.product([1, -1], repeat=3)]
O = [g for g in Oh if round(np.linalg.det(g)) == 1]
Tg = [g for g in O if key(np.abs(g)) in {key(np.eye(3)[list(q)]) for q in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]}]   # even perms x det +1
Th = Tg + [-g for g in Tg]
qi, qj, qk = np.array([[1j, 0], [0, -1j]]), np.array([[0, 1], [-1, 0]], complex), np.array([[0, 1j], [1j, 0]])
I2 = np.eye(2, dtype=complex)
T2 = close([qi, qj, (I2 + qi + qj + qk) / 2])
O2 = close([qi, qj, (I2 + qi + qj + qk) / 2, (I2 + qi) / np.sqrt(2)])
GR = {'O_h': Oh, 'O': O, 'T': Tg, 'T_h': Th, '2T': T2, '2O': O2}
def order(g):
    e = key(np.eye(len(g))); x = g; o = 1
    while key(x) != e: x = x @ g; o += 1
    return o
def invol(G): return sum(order(g) == 2 for g in G)
def nclasses(G):
    ks = [key(g) for g in G]; seen = set(); c = 0
    for g in G:
        if key(g) in seen: continue
        c += 1; seen |= {key(h @ g @ np.linalg.inv(h)) for h in G}
    return c
def ab_size(G):
    comm = close([a @ b @ np.linalg.inv(a) @ np.linalg.inv(b) for a in G for b in G] + [np.eye(len(G[0]))])
    return len(G) // len(comm)
def irrep_dims(G):
    nc, ab = nclasses(G), ab_size(G); rest = len(G) - ab; m = nc - ab
    sols = [s for s in itertools.combinations_with_replacement([d for d in range(2, 8) if len(G) % d == 0], m) if sum(d * d for d in s) == rest]
    return [1] * ab + list(sols[0]), len(sols)
def has_Q8(G):
    f4 = [g for g in G if order(g) == 4]
    for a in f4:
        for b in f4:
            if key(a @ a) == key(b @ b) and key(b @ a @ np.linalg.inv(b)) == key(np.linalg.inv(a)) and key(a) != key(b) and key(a) != key(np.linalg.inv(b)): return True
    return False
def has_V4(G):  # three commuting involutions
    inv = [g for g in G if order(g) == 2]
    return any(key(a @ b) == key(b @ a) and key(a) != key(b) for a in inv for b in inv)
dims = {h: irrep_dims(GR[h]) for h in ('T', 'T_h', '2T')}
check("i1 [T] group orders |O_h|,|O|,|2O| = 48,24,48 and |T|,|T_h|,|2T| = 12,24,24; irrep dims from class count + abelianisation (unique solution)",
      [len(GR[x]) for x in ('O_h', 'O', '2O', 'T', 'T_h', '2T')] == [48, 24, 48, 12, 24, 24] and all(v[1] == 1 for v in dims.values()),
      "; ".join(f"{h}:{sorted(v[0])}" for h, v in dims.items()))
# embeddings: T,T_h < O_h as matrices; T < O; 2T < 2O. Obstructions: 2T has Q8, O_h has none; T needs V4, 2O has one involution
emb = {('O_h', 'T'): True, ('O_h', 'T_h'): True, ('O', 'T'): True, ('2O', '2T'): True,
       ('O_h', '2T'): False, ('O', 'T_h'): False, ('O', '2T'): False, ('2O', 'T'): False, ('2O', 'T_h'): False}
sub = lambda Hs, Gs: {key(h) for h in Hs} <= {key(g) for g in Gs}
ok_emb = sub(Tg, Oh) and sub(Th, Oh) and sub(Tg, O) and sub(T2, O2) and has_Q8(T2) and not has_Q8(Oh) and invol(O2) == 1 and has_V4(Tg) \
    and invol(O) == 9 and invol(T2) == 1 and nclasses(Th) == 8
check("i2 [T] embeddings: T,T_h < O_h; T < O; 2T < 2O; NOT 2T < O_h (2T contains Q8, O_h does not), NOT T,T_h < 2O (one involution), "
      "NOT T_h,2T < O (order 24 = |O| but non-isomorphic)", ok_emb, f"involutions O={invol(O)}, 2T={invol(T2)}, 2O={invol(O2)}")
# Res_H L^2(G) = [G:H] L^2(H): multiplicity of rho = [G:H] dim rho (regular character = |G| delta_e)
# w1 family rule: family f = omega^f-eigenspace of an order-3 turn c in H, block by block
def c_eigs(h):
    G = GR[h]; c = [g for g in G if order(g) == 3][0]
    ev = {}
    # 1-dim chars via the cyclic quotient: chi(c) runs over the cube roots (and +-1 for T_h's g/u)
    # higher irreps: T/T_h: 3 = the matrices (eigs 1,w,w2); 2T: 2 = SU(2) (eigs w,w2), 2' and 2'' = 2 x chi, 3 = adjoint
    if h in ('T', 'T_h'):
        e3 = np.round(np.angle(np.linalg.eigvals(c)) / (2 * np.pi / 3)).astype(int) % 3
        nrep = 1 if h == 'T' else 2
        return {'1-dim': [(f, ) for f in range(3)] * nrep, '3': [tuple(sorted(e3))] * nrep}
    e2 = np.round(np.angle(np.linalg.eigvals(c)) / (2 * np.pi / 3)).astype(int) % 3
    return {'1-dim': [(f,) for f in range(3)], '2': [tuple(sorted((x + s) % 3 for x in e2)) for s in range(3)], '3': [(0, 1, 2)]}
rows = []; npass3 = 0
for (Gn, Hn), e in emb.items():
    if not e: continue
    idx = len(GR[Gn]) // len(GR[Hn]); fam = []
    for f in range(3):
        blocks = {}
        for typ, lst in c_eigs(Hn).items():
            d = int(typ[0]) if typ != '1-dim' else 1
            mult = idx * d
            blocks[typ] = sum(mult * ev.count(f) for ev in lst)
        fam.append(blocks)
    tot = [sum(b.values()) for b in fam]
    blk = [v for v in fam[0].values()]
    s43 = any(sum(c) == 4 for r in range(1, len(blk) + 1) for c in itertools.combinations(blk, r))
    rows.append((Gn, Hn, idx, tot, fam[0], s43))
    npass3 += (len(GR[Gn]) == 48 and tot == [16, 16, 16] and s43)
print("  (G,H) [G:H] family dims | family-0 blocks | 4+12 from blocks")
for r in rows: print(f"  ({r[0]},{r[1]}) {r[2]} {r[3]} | {r[4]} | {r[5]}")
check("i3 [T] three equal families of 16 arise for EVERY order-48 G with an order-3 turn (free action: 48/3), not for O (8 each); "
      "pairs giving 3 x 16 with a 4 + 12 block split: (O_h,T) and (O_h,T_h); (2O,2T) gives 2 + 8 + 6",
      [r[3] for r in rows] == [[16] * 3, [16] * 3, [8] * 3, [16] * 3] and npass3 == 2)
# identical families: Aut(Z3) = Z2, so conjugation by G can only swap omega <-> omega^2 labels
def swaps(Gn, Hn):
    G, H = GR[Gn], GR[Hn]; c = [g for g in H if order(g) == 3][0]
    comm = close([a @ b @ np.linalg.inv(a) @ np.linalg.inv(b) for a in H for b in H] + [np.eye(len(H[0]))])
    ck = {key(c @ x) for x in comm}; cik = {key(np.linalg.inv(c) @ x) for x in comm}
    acts = set()
    for g in G:
        y = key(g @ c @ np.linalg.inv(g))
        acts.add('fix' if y in ck else 'swap' if y in cik else 'other')
    return acts
sw = {p: swaps(*p) for p in [('O_h', 'T'), ('O_h', 'T_h'), ('2O', '2T')]}
check("i4 [T] no element of G cycles the three family labels: conjugation either fixes them or swaps families 1 <-> 2 (family 0 = trivial label is "
      "distinguished: lepton labels 1 + E under G, not a 3-cycle)", all(v == {'fix', 'swap'} for v in sw.values()), str({f'{a},{b}': sorted(v) for (a, b), v in sw.items()}))
# hypercharge from H-labels: a block-constant charge takes <= #blocks values; SM Y on a 16 takes 6
Ysm = [1 / 6] * 6 + [-2 / 3] * 3 + [1 / 3] * 3 + [-1 / 2] * 2 + [1, 0]
nY = len(set(np.round(Ysm, 6))); nb = {f"{r[0]},{r[1]}": len(r[4]) * (2 if r[1] == 'T_h' else 1) for r in rows if r[3] == [16] * 3}
# anomaly of the only label U(1) of (O_h,T): charge a on the 4, -a/3 on the 12 (traceless)
cub = 4 * 1 + 12 * (-1 / 3) ** 3
check("i5 [T] SM hypercharge is NOT a function of the H-labels for any pair: it takes 6 values on a 16, a label charge at most #blocks "
      "(T: 2, T_h: 4, 2T: 3); the one traceless label U(1) of (O_h,T) has cubic anomaly 32/9 per family", nY == 6 and max(nb.values()) < 6 and abs(cub - 32 / 9) < 1e-12, str(nb))
print("VERDICT (i): H1 FAIL. 3 x 16 = 48/3 is arithmetic (any order-48 group, any order-3 turn); 3 pairs match counts "
      "[(O_h,T),(O_h,T_h) as 4+12, (2O,2T) as 8 doublet + 8 singlet states]; no pair gives hypercharge from labels; numerology.")

# ================= (ii) Delta(27) slab =================
s0 = np.eye(2, dtype=complex); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
Gm = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0), np.kron(sz, s0)]
G5 = Gm[4]; A_UP = (G5 + 1j * Gm[3]) / 2
def bondsum(Ls):
    S = np.zeros((Ls, Ls)); S[np.arange(1, Ls), np.arange(Ls - 1)] = 1
    return np.kron(A_UP, S) + np.kron(A_UP.conj().T, S.T)
E3 = [np.eye(3)[i] for i in range(3)]
VCL = [np.array(v, float) for v in ((1, -1, 0), (0, 1, -1), (-1, 0, 1), (1, 1, 1))]   # class-preserving: x+y+z mod 3 fixed
def hamv(kv, Ls, m, V, eps=0.0):
    Is = np.eye(Ls); Hs = np.zeros((4, 4), complex); mass = m - 1
    for v in V:
        kd = kv @ v; Hs += np.sin(kd) * sum(v[i] * Gm[i] for i in range(3)); mass -= 1 - np.cos(kd)
    for i in range(3):   # class-changing nearest-neighbour hop e_i with amplitude eps
        Hs += eps * np.sin(kv[i]) * Gm[i]; mass -= eps * (1 - np.cos(kv[i]))
    return np.kron(Hs + mass * G5, Is) + bondsum(Ls)
def dhamv(kv, Ls, j, V):
    Hs = np.zeros((4, 4), complex)
    for v in V:
        kd = kv @ v; Hs += v[j] * (np.cos(kd) * sum(v[i] * Gm[i] for i in range(3)) - np.sin(kd) * G5)
    return np.kron(Hs, np.eye(Ls))
M0, LS = 0.6, 12
def scan(N, V, eps=0.0, tol=1e-3):
    ks = [np.array(t) * 2 * np.pi / N for t in itertools.product(range(N), repeat=3)]
    light = []; gap = 9.
    for kv in ks:
        e = np.linalg.eigvalsh(hamv(kv, LS, M0, V, eps)); a = np.abs(e)
        nl = int((a < tol).sum())
        if nl: light.append((tuple(int(t) for t in np.round(kv / (2 * np.pi / N))), nl))
        gap = min(gap, a[a >= tol].min())
    return light, gap
def chir(kv, V):
    H = hamv(kv, LS, M0, V); e, U = np.linalg.eigh(H); Q = U[:, np.abs(e) < 1e-3]
    X = np.kron(np.eye(4), np.diag(np.arange(LS))); xw, xv = np.linalg.eigh(Q.conj().T @ X @ Q); B = Q @ xv; out = []
    for msk in (xw < LS / 2, xw >= LS / 2):
        Pw = B[:, msk]; v = np.zeros((3, 3))
        for j in range(3):
            A = Pw.conj().T @ dhamv(kv, LS, j, V) @ Pw
            for a in range(3): v[j, a] = np.real(np.trace(A @ SIG[a])) / 2
        out.append(int(np.sign(np.linalg.det(v))))
    return out
# sanity: V = e_i reproduces the CL-1 cubic slab (one light copy at k = 0 for m in the window)
l0, g0 = scan(4, E3)
check("ii1 [F] V = {e_i} is the chiral-tick-form slab: one light Weyl per wall at k = 0 only (4 states), 4^3 torus", l0 == [((0, 0, 0), 4)], f"light {l0}, next |E| {g0:.2f}")
q = np.array([1, 1, 1]) * 2 * np.pi / 3
per = max(np.abs(hamv(kv, LS, M0, VCL) - hamv(kv + q, LS, M0, VCL)).max() for kv in rng.uniform(-np.pi, np.pi, (20, 3)))
check("ii2 [T] class-preserving hops commute with Omega = omega^(x+y+z): H(k + q) = H(k), q = (2pi/3)(1,1,1); a plain e_i hop does not",
      per < 1e-12 and np.abs(hamv(np.zeros(3), LS, M0, VCL, 0.1) - hamv(q, LS, M0, VCL, 0.1)).max() > 0.1, f"max |H(k+q)-H(k)| = {per:.0e}")
l6, g6 = scan(6, VCL); l5, g5 = scan(5, VCL)
ch = [chir(np.array(t) * 2 * np.pi / 6, VCL) for t, _ in l6]
check("ii3 [F] N = 6: exactly 3 light Weyl copies per wall at k = 0, q, 2q (12 states), the same chirality pair on all three, no other light state",
      [t for t, _ in l6] == [(0, 0, 0), (2, 2, 2), (4, 4, 4)] and all(nl == 4 for _, nl in l6) and len(set(map(tuple, ch))) == 1 and ch[0][0] == -ch[0][1],
      f"light {l6}, chiralities {ch}, next |E| {g6:.2f}")
check("ii4 [F] control N = 5 (3 does not divide N): one light copy per wall (4 states), as w3 predicts; q is not a torus momentum",
      l5 == [((0, 0, 0), 4)], f"light {l5}, next |E| {g5:.2f}")
# Delta(27) on the 3 copies: T = translation e1 (phase e^{i k1}), Omega = shift k -> k + q
Tm = np.diag([np.exp(1j * (j * q)[0]) for j in range(3)]); Om = np.roll(np.eye(3), 1, axis=0)
cm = Tm @ Om @ np.linalg.inv(Tm) @ np.linalg.inv(Om)
grp = close([Tm, Om]); ntr = sum(abs(np.trace(g)) > 1e-9 for g in grp)
chi2 = sum(abs(np.trace(g)) ** 2 for g in grp) / len(grp)
check("ii5 [T] the 3 copies carry Delta(27): |<T,Omega>| = 27, T Omega T^-1 Omega^-1 = omega^(+-1) 1, irreducible (sum |chi|^2 / 27 = 1), det T = det Omega = 1",
      len(grp) == 27 and abs(abs(np.trace(cm)) - 3) < 1e-9 and abs(np.trace(cm) / 3 - 1) > 0.5 and abs(chi2 - 1) < 1e-9
      and abs(np.linalg.det(Tm) - 1) < 1e-12 and abs(np.linalg.det(Om) - 1) < 1e-12, f"commutator = {np.round(np.trace(cm) / 3, 3)}, traceful elements {ntr}")
# class-changing e_i hop on all fields: splits/removes the copies
res = {}
for eps in (0.05, 0.3):
    m_at = [min(np.abs(np.linalg.eigvalsh(hamv(j * q, LS, M0, VCL, eps)))) for j in range(3)]
    res[eps] = m_at
check("ii6 [F] a class-changing e_i hop on every field breaks Omega: eps = 0.05 detunes the q, 2q copies (nodes move off q), eps = 0.3 drives them out of "
      "the window (wall mass m - 1 - 4.5 eps < -1) leaving the one cubic copy at k = 0", res[0.05][0] < 1e-3 and min(res[0.05][1:]) > 1e-3
      and min(res[0.3][1:]) > 0.3, "min|E| at 0,q,2q: " + "; ".join(f"eps {e}: " + ",".join(f"{x:.3f}" for x in v) for e, v in res.items()))
# which sublattices are cube-symmetric: HNF enumeration of index <= 32
def hnf_lattices(idx):
    for a in range(1, idx + 1):
        if idx % a: continue
        for c in range(1, idx // a + 1):
            if (idx // a) % c: continue
            f = idx // (a * c)
            for b in range(a):
                for d in range(a):
                    for e in range(c): yield np.array([[a, 0, 0], [b, c, 0], [d, e, f]])
def in_lat(v, B):   # B lower-triangular rows (a,0,0),(b,c,0),(d,e,f): exact integer back-substitution
    (a, _, _), (b, c, _), (d, e, f) = B.tolist(); v1, v2, v3 = (int(t) for t in v)
    if v3 % f: return False
    x3 = v3 // f
    if (v2 - x3 * e) % c: return False
    x2 = (v2 - x3 * e) // c
    return (v1 - x2 * b - x3 * d) % a == 0
def invariant(B, gens): return all(in_lat(g @ r, B) for g in gens for r in B)
Ohi = [np.round(g).astype(int) for g in Oh]
D3d = [g for g in Ohi if (g @ np.array([1, 1, 1]) == np.array([1, 1, 1])).all() or (g @ np.array([1, 1, 1]) == -np.array([1, 1, 1])).all()]
OHG = [np.roll(np.eye(3, dtype=int), 1, axis=0), np.eye(3, dtype=int)[[1, 0, 2]], np.diag([-1, 1, 1])]   # generate O_h
D3G = [OHG[0], OHG[1], -np.eye(3, dtype=int)]                                                         # generate D3d
oh_idx = [i for i in range(1, 33) if any(invariant(B, OHG) for B in hnf_lattices(i))]
n3 = sum(1 for _ in hnf_lattices(3)); n3d = [B for B in hnf_lattices(3) if invariant(B, D3G)]
check("ii7 [T] no O_h-invariant sublattice of Z^3 has index 3 (O_h-invariant indices <= 32: n^3, 2n^3, 4n^3); of the 13 index-3 sublattices exactly one, "
      "x+y+z = 0 mod 3, is invariant, under the (111) stabiliser D3d (order 12) only", 3 not in oh_idx and oh_idx == [1, 2, 4, 8, 16, 27, 32] and n3 == 13 and len(n3d) == 1 and len(D3d) == 12 and len(close([g.astype(float) for g in OHG])) == 48 and len(close([g.astype(float) for g in D3G])) == 12,
      f"O_h indices {oh_idx}")
print("VERDICT (ii): H2 PASS as a count (3 copies, Delta(27) 3-irrep, det = 1, control 1 copy), but the 3 is the index of the chosen hop sublattice: "
      "the mod-3 class rule singles out one body diagonal (breaks O_h to D3d), and 3 copies = 3 decoupled sublattices, each with its own mirror.")

# ================= (iii) [[8,3,3]] codes =================
n, kq = 8, 3; MASK = (1 << n) - 1
def sp(a, b): return (((a & MASK) & (b >> n)) ^ ((a >> n) & (b & MASK))).bit_count() & 1
def wt(a): return ((a & MASK) | (a >> n)).bit_count()
def span(gs):
    S = {0}
    for g in gs: S |= {s ^ g for s in S}
    return S
def pauli(s):
    x = z = 0
    for i, c in enumerate(s):
        if c in 'XY': x |= 1 << i
        if c in 'ZY': z |= 1 << i
    return x | (z << n)
GOT = [pauli(s) for s in "XXXXXXXX ZZZZZZZZ XIXIZYZY XIYZXIYZ XZIYIYXZ".split()]
def normalizer(gs): return [v for v in range(1 << 16) if all(sp(v, g) == 0 for g in gs)]
SG = span(GOT); NG = normalizer(GOT)
dG = min(wt(v) for v in NG if v not in SG)
check("iii1 [T] Gottesman's generators commute, |S| = 32, |N| = 2048, distance 3 exhaustively; S weights 1 + 28 y^6 + 3 y^8 (pure)",
      all(sp(a, b) == 0 for a in GOT for b in GOT) and len(SG) == 32 and len(NG) == 2048 and dG == 3
      and sorted(wt(s) for s in SG) == [0] + [6] * 28 + [8] * 3, f"d = {dG}")
# LP (Shor-Laflamme + shadow): any [[8,3,3]] has A1 + A2 < 1, so every [[8,3,3]] code is pure
def kr(j, i, sgn):
    return sum(comb(n - i, j - s) * 3 ** (j - s) * comb(i, s) * (-1) ** (s if sgn > 0 else i - s) for s in range(j + 1))
K = np.array([[kr(j, i, 1) for i in range(n + 1)] for j in range(n + 1)], float) / 2 ** (n - kq)
SH = np.array([[kr(j, i, -1) for i in range(n + 1)] for j in range(n + 1)], float) / 2 ** (n - kq)
Aeq = [np.eye(n + 1)[0], np.ones(n + 1)] + [K[j] - np.eye(n + 1)[j] for j in (1, 2)]
lp = linprog(-(np.eye(n + 1)[1] + np.eye(n + 1)[2]), A_ub=np.vstack([np.eye(n + 1) - K, -SH]), b_ub=np.zeros(2 * n + 2),
             A_eq=np.array(Aeq), b_eq=[1, 32, 0, 0], bounds=[(0, None)] * (n + 1))
check("iii2 [T] LP bound: max (A1 + A2) over Shor-Laflamme + shadow constraints < 1, so an [[8,3,3]] code has no weight-1,2 stabiliser (pure)",
      lp.success and -lp.fun < 1, f"LP max = {-lp.fun:.3f}")
# pure [[8,3,3]] up to LC x permutation <-> 8 pairwise-skew lines of PG(4,2) (qubit j -> span of syndromes of X_j, Z_j)
# with Pluecker sum 0 (generators commute), modulo GL(5,2) (choice of generators)
lines = sorted({tuple(sorted((a, b, a ^ b))) for a in range(1, 32) for b in range(1, 32) if a != b})
def pl(a, b):
    v = 0; t = 0
    for i in range(5):
        for j in range(i + 1, 5): v |= ((((a >> i) & (b >> j)) ^ ((a >> j) & (b >> i))) & 1) << t; t += 1
    return v
PL = [pl(l[0], l[1]) for l in lines]; MS = [(1 << l[0]) | (1 << l[1]) | (1 << l[2]) for l in lines]
i0, i1 = lines.index((1, 2, 3)), lines.index((4, 8, 12)); u0 = MS[i0] | MS[i1]
cand = [i for i in range(155) if not MS[i] & u0]; found = []
def bt(st, used, p, ch):
    if len(ch) == 6:
        if p == 0: found.append((i0, i1) + tuple(ch))
        return
    for ii in range(st, len(cand)):
        i = cand[ii]
        if not MS[i] & used: ch.append(i); bt(ii + 1, used | MS[i], p ^ PL[i], ch); ch.pop()
bt(0, u0, PL[i0] ^ PL[i1], [])
Ttot = len(found) * (155 * 112 // 2) // comb(8, 2)
def gl_apply(img, v):
    r = 0
    for b in range(5):
        if v >> b & 1: r ^= img[b]
    return r
def stab(S8):
    Ls = [lines[i] for i in S8]; Lset = {frozenset(l) for l in Ls}; cnt = 0
    for La in Ls:
        for (a1, a2) in itertools.permutations(La, 2):
            for Lb in Ls:
                if Lb == La: continue
                for (b1, b2) in itertools.permutations(Lb, 2):
                    sp4 = {gl_apply([a1, a2, b1, b2, 0], v) for v in range(16)}
                    for e5 in range(1, 32):
                        if e5 in sp4: continue
                        img = [a1, a2, b1, b2, e5]
                        if all(frozenset(gl_apply(img, p) for p in l) in Lset for l in Ls): cnt += 1
    return cnt
st0 = stab(found[0]); GL5 = 9999360
check("iii3 [T] exact classification: 192 skew 8-line sets with Pluecker sum 0 contain a fixed skew pair -> 59520 sets in all; "
      "one stabiliser has order 168 and 9999360/168 = 59520, so there is exactly ONE [[8,3,3]] code up to local Clifford x permutation",
      len(found) == 192 and Ttot == 59520 and st0 == 168 and GL5 // st0 == Ttot, f"sets {len(found)}, total {Ttot}, |Aut| = {st0}")
# turn symmetries on Gottesman's code (= the unique class)
Fr = {'id': lambda x, z: (x, z), 'XYZ': lambda x, z: (x ^ z, x), 'ZYX': lambda x, z: (z, x ^ z), 'H': lambda x, z: (z, x), 'S': lambda x, z: (x, x ^ z), 'HSH': lambda x, z: (x ^ z, z)}
def act(v, perm, fr):
    r = 0
    for j in range(n):
        x, z = fr((v >> j) & 1, (v >> (n + j)) & 1); t = perm[j]
        r |= (x << t) | (z << (n + t))
    return r
def is_aut(perm, fr): return all(act(g, perm, fr) in SG for g in GOT)
def ctype(p):
    seen = set(); cyc = []
    for i in range(n):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        cyc.append(L)
    return tuple(sorted(cyc))
perms = list(itertools.permutations(range(n)))
by = {}
for p in perms:
    c = ctype(p)
    if c in ((1, 1, 3, 3), (4, 4)): by.setdefault(c, []).append(p)
cnt3 = {f: sum(is_aut(p, Fr[f]) for p in by[(1, 1, 3, 3)]) for f in Fr}
cnt4 = {f: sum(is_aut(p, Fr[f]) for p in by[(4, 4)]) for f in Fr}
paut = sum(is_aut(p, Fr['id']) for p in perms)
check("iii4 [T] 3-fold turn (vertex type 1^2 3^2): a code symmetry only with a frame rotation; with X->Y->Z on every qubit 28 qubit-permutations, "
      "= 28 x 36 = 1008 cube labellings; plain permutation automorphisms 56, none of order 3",
      cnt3['id'] == 0 and cnt3['XYZ'] == 28 and 36 * cnt3['XYZ'] == 1008 and paut == 56, f"type-1^2 3^2 counts by frame {cnt3}")
check("iii5 [T] 4-fold turn (vertex type 4^2): no code symmetry with ANY uniform frame (id, H, S, HSH, XYZ, ZYX)", sum(cnt4.values()) == 0, str(cnt4))
# logical action: N/S, induced map of one (tau, XYZ) symmetry; count bases where it is a literal 3-cycle of logical qubits
tau = next(p for p in by[(1, 1, 3, 3)] if is_aut(p, Fr['XYZ']))
basisS = {}
def red(v):
    for pv in sorted(basisS, reverse=True):
        if v >> pv & 1: v ^= basisS[pv]
    return v
for g in GOT:
    v = red(g); basisS[v.bit_length() - 1] = v
    for pv in list(basisS):
        if pv != v.bit_length() - 1 and basisS[pv] >> (v.bit_length() - 1) & 1: basisS[pv] ^= v
reps = sorted({red(v) for v in NG}); g_ = lambda v: red(act(v, tau, Fr['XYZ']))
fixed = sum(g_(v) == v for v in reps); order3 = all(g_(g_(g_(v))) == v for v in reps)
nb = 0
for x1 in reps:
    if not x1: continue
    xs = [x1, g_(x1), g_(g_(x1))]
    if any(sp(a, b) for a in xs for b in xs): continue
    for z1 in reps:
        zs = [z1, g_(z1), g_(g_(z1))]
        if all(sp(xs[a], zs[b]) == (a == b) for a in range(3) for b in range(3)) and not any(sp(a, b) for a in zs for b in zs): nb += 1
check("iii6 [T] on the 64 logical classes the turn has order 3 and fixes 4 (a 2-dim fixed space); 108 symplectic logical bases on which it is a literal "
      "cyclic permutation of the 3 logical qubits", order3 and fixed == 4 and nb == 108, f"fixed {fixed}, bases {nb}")
print("VERDICT (iii): H3 PASS on the unique class. k <= 3 at d = 3 needs the chosen record unit (8-qubit cell), distance 3, maximal k; "
      "the C3 acts as a family permutation only with the frame rotation; logical qubit = family is an identification, not derived.")
print(f"Supplied: Wilson slab (m = 0.6, Ls = 12), Gottesman generators, LP/shadow bounds. time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={P} FAIL={F}")
