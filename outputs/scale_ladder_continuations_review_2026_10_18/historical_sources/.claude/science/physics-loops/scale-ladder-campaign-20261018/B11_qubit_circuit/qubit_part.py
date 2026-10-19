#!/usr/bin/env python3
"""B11 Part B: qubit images of the step gates in the 48-qubit-per-site corner code (BKSF, flux 1011, L = 4).

Dictionary (C20 qbuild, re-implemented here with the runner's translation-invariant gauge):
  Q(c+_q c_r) = G_qr (1 + B_q)(1 - B_r)/4,  G_qr = i^n (prod of code hops A along a path q -> r) / (prod of gauge signs u),
  Q(n_q) = (1 - B_q)/2.
Checks: every hop generator of the circuit maps to (P1 - P2)/2-type sums of exactly two commuting Hermitian Paulis that
commute with all stabilizer generators (so exp(-i theta Q) = two Pauli rotations by theta/2); weights and site spans;
Heisenberg conjugation of logical bilinears by the qubit circuits of S (Clifford, full torus), of one plaquette block of
R_L (pi/8 rotations), of one on-site layer (irrational angles), and of the full step W on sample bilinears, compared with
sum_ij U_ia conj(U_jb) Q(c+_i c_j) modulo the stabilizer group (R, loops, Wilson-loop sector).
"""
import sys, os, io, contextlib, random, itertools, time
from collections import deque
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = '/home/user/qubit-lattice-axiom-framework'
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(REPO, 'scripts'))
t0 = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    import circuit as CC
sys.argv = ['q', '4', '1011']
import corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17 as QM
try:
    QM._run_reviewed_program()
except (SystemExit, NameError):
    pass
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)
assert QM.L == CC.L and QM.FLUX == dict(square=1, triangle=0, plaquette=1, tube=1)
A, Bop, pmul, pcomm, INC, NQ = QM.A, QM.Bop, QM.pmul, QM.pcomm, QM.INC, QM.NQ
# vertex maps: code vertex (v, sorted tuple) <-> model index
def m2q(i): v, c = CC.VERTS[i]; return (v, tuple(sorted(c)))
q2m = {m2q(i): i for i in range(CC.nV)}
EID = CC.C['EID']
def u_s(q, r): return (-1.0) ** CC.u[EID[frozenset((q2m[q], q2m[r]))]]
def path(src, dst):
    prev = {src: None}; dq = deque([src])
    while dq:
        x = dq.popleft()
        if x == dst: break
        for _, _, nb in INC[x]:
            if nb not in prev: prev[nb] = x; dq.append(nb)
    p = [dst]
    while p[-1] != src: p.append(prev[p[-1]])
    return p[::-1]
def P2d(S, coef=1.0): return {(S[0], S[1]): coef * (1j ** S[2])}
def omul(a, b):
    out = {}
    for (x1, z1), c1 in a.items():
        for (x2, z2), c2 in b.items():
            s = (-1) ** bin(z1 & x2).count('1'); k = (x1 ^ x2, z1 ^ z2); out[k] = out.get(k, 0) + c1 * c2 * s
    return {k: v for k, v in out.items() if abs(v) > 1e-12}
def oadd(a, b, s=1.0):
    out = dict(a)
    for k, v in b.items(): out[k] = out.get(k, 0) + s * v
    return {k: v for k, v in out.items() if abs(v) > 1e-12}
def oscale(a, s): return {k: v * s for k, v in a.items()}
def Gop(q, r):
    p = path(q, r); n = len(p) - 1; S = (0, 0, n % 4); up = 1.0
    for i in range(n): S = pmul(S, A(p[i], p[i + 1])); up *= u_s(p[i], p[i + 1])
    return P2d(S, 1.0 / up)
ONE = {(0, 0): 1.0}
_cache = {}
def single(i, j):
    """Q(c+_i c_j), model indices"""
    if (i, j) in _cache: return _cache[(i, j)]
    q, r = m2q(i), m2q(j)
    if i == j: out = oadd(oscale(ONE, 0.5), P2d(Bop(q)), -0.5)
    else:
        G = Gop(q, r); out = oscale(omul(omul(G, oadd(ONE, P2d(Bop(q)))), oadd(ONE, P2d(Bop(r)), -1.0)), 0.25)
    _cache[(i, j)] = out; return out
def quad(k, modes):
    """Q(sum_ij k_ij c+_mi c_mj)"""
    out = {}
    for a, m in enumerate(modes):
        for b, n in enumerate(modes):
            if abs(k[a, b]) > 1e-14: out = oadd(out, oscale(single(m, n), k[a, b]))
    return out
def herm_terms(op):
    """split into identity part and list of (Hermitian Pauli (x,z,p), real coefficient)"""
    idc = 0; terms = []
    for (x, z), c in op.items():
        if x == 0 and z == 0: idc += c; continue
        w = bin(x & z).count('1'); cr = c / (1j ** w)          # Hermitian Pauli i^w X^x Z^z
        terms.append(((x, z, w % 4), cr))
    return idc, terms
# ---------------- stabilizer group with the logical (Wilson-loop) sector of this gauge
G = QM.Group(NQ)
stabs = [QM.Rop(v, h) for v in QM.SITES for h in QM.HALF if sum(h[1]) > 0] + \
        [QM.loop_op(seq, QM.FLUX[kind]) for kind, seq in QM.cycles()]
for P in stabs: assert G.add(P) in (True, 0)
def wilson(a):
    v0 = (0, 0, 0); c0 = [c for c in QM.CORN if a not in c and QM.neg(a) not in c][0]
    q = (v0, c0); seq = [q]
    for step in range(QM.L):
        nxt = (tuple((x + y) % QM.L for x, y in zip(q[0], a)), c0); seq += path(q, nxt)[1:]; q = nxt
    n = len(seq) - 1; S = (0, 0, n % 4); up = 1.0
    for i in range(n): S = pmul(S, A(seq[i], seq[i + 1])); up *= u_s(seq[i], seq[i + 1])
    if up < 0: S = (S[0], S[1], (S[2] + 2) % 4)
    return S
for a in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    r = G.add(wilson(a)); assert r is True, r
stabs_all = stabs + [wilson(a) for a in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
pivs = sorted(G.piv, reverse=True)
print(f"stabilizer group rank {len(G.piv)} on {NQ} qubits  [{time.time()-t0:.0f}s]", flush=True)
def canon(x, z):
    v = G.vec((x, z, 0)); comb = (x, z, 0)
    for c in pivs:
        if (v >> c) & 1:
            pv, pP = G.piv[c]; v ^= pv; comb = pmul(comb, pP)
    return (comb[0], comb[1]), comb[2] % 4
def ocanon(a):
    out = {}
    for (x, z), c in a.items():
        k, ph = canon(x, z); out[k] = out.get(k, 0) + c * (1j ** ph)
    return {k: v for k, v in out.items() if abs(v) > 1e-9}

# ---------------- (i) every gate generator of the circuit -> exactly two commuting Hermitian Paulis (or one B)
def site_of(qi): return QM.SITES[qi // 48]
def span(x, z):
    sup = x | z; sites = {site_of(i) for i in range(sup.bit_length()) if (sup >> i) & 1}
    if not sites: return 0, sites
    ext = 0
    s0 = list(sites)[0]
    for s in sites:
        for t in sites:
            ext = max(ext, max(abs(CC.dmod(a - b)) for a, b in zip(s, t)))
    return ext, sites
gate_rots = []          # per gate: list of (Hermitian Pauli, alpha) for exp(-i alpha P)
bad = 0; info = {}
t1 = time.time()
for gi, (modes, k, th, tag) in enumerate(CC.gates):
    op = quad(k, modes); idc, terms = herm_terms(op)
    if len(modes) == 2:
        ok = (abs(idc) < 1e-12 and len(terms) == 2 and all(abs(abs(c) - 0.5) < 1e-12 and abs(c.imag) < 1e-12 for _, c in terms)
              and pcomm(terms[0][0], terms[1][0]))
    else:
        ok = abs(idc - 0.5) < 1e-12 and len(terms) == 1 and abs(terms[0][1] + 0.5) < 1e-12
    if not ok: bad += 1
    rl = [(P, th * c.real) for P, c in terms]      # exp(-i th Q) = global phase x prod exp(-i th c P)
    gate_rots.append(rl)
    kind = (tag, len(modes))
    for P, _ in terms:
        wgt = bin(P[0] | P[1]).count('1'); ext, sites = span(P[0], P[1])
        mx = info.get(kind, (0, 0, 0)); info[kind] = (max(mx[0], wgt), max(mx[1], ext), max(mx[2], len(sites)))
check("every gate generator of the circuit maps to Q = c1 P1 + c2 P2 with P1, P2 commuting Hermitian Paulis, |c| = 1/2 (hops), "
      "or to (1 - B_q)/2 (numbers); hence each gate is a product of Pauli rotations by theta/2",
      bad == 0, f"{len(CC.gates)} gates, failures {bad}  [{time.time()-t1:.0f}s]")
print("max Pauli weight / max sup-norm site span / max number of sites, per gate kind:")
for k_, v_ in sorted(info.items()): print(f"   {k_}: weight {v_[0]}, span {v_[1]}, sites {v_[2]}")
# stabilizer commutation (all gate Paulis vs all stabilizer generators incl. Wilson loops)
t1 = time.time(); nbad = 0; allP = {P for rl in gate_rots for P, _ in rl}
for P in allP:
    for S in stabs_all:
        if not pcomm(P, S): nbad += 1
check("all distinct gate Paulis commute with every stabilizer generator (repetition, loops, Wilson loops): gauge invariant",
      nbad == 0, f"{len(allP)} Paulis x {len(stabs_all)} generators  [{time.time()-t1:.0f}s]")

# ---------------- Heisenberg evolution through Pauli rotations
def conj_rot(op, P, alpha):
    """exp(-i alpha P) op exp(+i alpha P)"""
    c2, s2 = np.cos(2 * alpha), np.sin(2 * alpha)
    out = {}
    for (x, z), c in op.items():
        if pcomm(P, (x, z, 0)): out[(x, z)] = out.get((x, z), 0) + c; continue
        if abs(c2) > 1e-15: out[(x, z)] = out.get((x, z), 0) + c * c2
        R = pmul(P, (x, z, 0)); k = (R[0], R[1]); out[k] = out.get(k, 0) + c * (-1j * s2) * (1j ** R[2])
    return {k: v for k, v in out.items() if abs(v) > 1e-12}
def evolve(op, gidx, canon_every=0):
    n = 0
    for gi in gidx:
        for P, al in gate_rots[gi]:
            op = conj_rot(op, P, al)
        n += 1
        if canon_every and n % canon_every == 0: op = ocanon(op)
    return op
def expected(U, a, b, modes_hint=None):
    rows_a = np.nonzero(np.abs(U[:, a]) > 1e-12)[0]; rows_b = np.nonzero(np.abs(U[:, b]) > 1e-12)[0]
    out = {}
    for i in rows_a:
        for j in rows_b:
            out = oadd(out, oscale(single(i, j), U[i, a] * np.conj(U[j, b])))
    return out
def mode_set(gidx): return {m for gi in gidx for m in CC.gates[gi][0]}
def test(name, gidx, U, pairs, canon_every=0):
    nb = 0; nt = 0
    for a, b in pairs:
        lhs = evolve(single(a, b), gidx, canon_every); rhs = expected(U, a, b)
        d = ocanon(oadd(lhs, rhs, -1.0)); nt += 1; nb += bool(d)
    check(name, nb == 0, f"{nt - nb}/{nt} bilinears")
random.seed(5)
nO, nR = CC.n_onsite, CC.n_RL
idx_S = list(range(nO + nR, len(CC.gates)))
pairs = [tuple(random.sample(range(CC.nV), 2)) for _ in range(12)]
loc = [CC.VID[((0, 0, 0), c)] for c in CC.CORN]
pairs += [(loc[0], loc[5]), (loc[3], loc[3]), (loc[7], loc[2])]
t1 = time.time()
test("Clifford factor S on the full L = 4 torus: the qubit circuit (pi/4 Pauli rotations and B phases) maps Q(c+_a c_b) to "
     "sum S_ia S_jb Q(c+_i c_j) modulo stabilizers", idx_S, CC.Sr, pairs)
print(f"   [{time.time()-t1:.0f}s]")
# one plaquette block of R_L (includes the two pi/8-type diagonal rotations)
p0 = CC.plaqs[0]
idx_p = [gi for gi in range(nO, nO + nR) if set(CC.gates[gi][0]) <= set(p0)]
Up = CC.apply_gates([CC.gates[gi] for gi in idx_p])
other = [m for m in range(CC.nV) if m not in p0][:3]
pp = [(p0[0], p0[2]), (p0[1], p0[1]), (p0[3], p0[0]), (p0[0], other[0]), (other[1], p0[2])]
t1 = time.time()
test("one plaquette block of R_L (two pi/4 diagonal rotations = four pi/8 Pauli rotations, plus Clifford link swaps) acts "
     "logically as its one-particle 4 x 4 block", idx_p, Up, pp)
# one on-site layer at site 0 (irrational angles)
idx_o = [gi for gi in range(nO) if set(CC.gates[gi][0]) <= set(loc)]
Uo = CC.apply_gates([CC.gates[gi] for gi in idx_o])
po = [(loc[0], loc[1]), (loc[4], loc[4]), (loc[11], loc[2]), (loc[6], CC.VID[((1, 0, 0), CC.CORN[0])])]
test("the on-site layer at one site (Givens rotations with irrational angles) acts logically as U_H U_L", idx_o, Uo, po, canon_every=10)
print(f"   [{time.time()-t1:.0f}s]")
# full step W on two bilinears (light-cone gates only; canonicalise every few gates)
t1 = time.time()
for a, b in [(loc[0], loc[1]), (loc[2], loc[2])]:
    cone = [gi for gi in range(len(CC.gates))]
    lhs = single(a, b)
    for gi in cone:
        rl = gate_rots[gi]
        if all(pcomm(P, (x, z, 0)) for P, _ in rl for (x, z) in lhs): continue
        for P, al in rl: lhs = conj_rot(lhs, P, al)
        if len(lhs) > 400: lhs = ocanon(lhs)
    d = ocanon(oadd(lhs, expected(CC.Wref, a, b), -1.0))
    check(f"full step W: qubit circuit maps Q(c+_a c_b) (a, b = site-0 corners {CC.CORN.index(CC.VERTS[a][1])},"
          f"{CC.CORN.index(CC.VERTS[b][1])}) to sum W_ia conj(W_jb) Q(c+_i c_j) modulo stabilizers", not d,
          f"residual terms {len(d)}  [{time.time()-t1:.0f}s]")
# negative control: same evolved operator against the one-particle matrix with one pi/4 rotation deleted
d = ocanon(oadd(lhs, expected(CC.Ubad, a, b), -1.0))
check("control: comparison against W with one pi/4 plaquette rotation deleted leaves a nonzero residual", len(d) > 0, f"{len(d)} terms")
print(f"\nPart B TOTAL: PASS={PASS} FAIL={FAIL}  [{time.time()-t0:.0f}s]")
