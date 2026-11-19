#!/usr/bin/env python3
"""code-to-heisenberg: does tiling the unique [[8,3,3]] cube-cell code force the x+y+z mod 3 (Delta(27)) structure?
C1 axis selection: subgroup of the cube rotation group O that is a code symmetry (natural frame) for every one of the
   8! vertex labellings; which body diagonals are selected and how often.
C2 code-preserving translations of the tiled code (weight-split argument + direct 16-qubit check).
C3 Heisenberg pair on (family slot) x (cell torus): turn C, cell translation T, clock Omega = omega^(x+y+z), screw T C;
   point-group no-go; on-site diagonal omega-phases as logical clocks (all 3^8, axes X, Y, Z); class content of the
   cyclic logical bases.
C4 C3-invariant index-p sublattices, p = 2, 3, 5, 7.
Labels: [T] exact (finite enumeration / algebra), [F] finite diagnostic. Supplied: Gottesman 1996 [[8,3,3]] generators,
uniqueness of the code class (cube-three-families runner, iii3), natural frame (Pauli axes = spatial axes).
Verdict per criteria_pre_run.txt; PASS/FAIL lines certify facts."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np

rng = np.random.default_rng(20261024)
T0 = time.time(); P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))
w = np.exp(2j * np.pi / 3)

# ---------------- code (binary symplectic, x | z << n) ----------------
n = 8; MASK = (1 << n) - 1
def sp(a, b, m=n): M = (1 << m) - 1; return (((a & M) & (b >> m)) ^ ((a >> m) & (b & M))).bit_count() & 1
def wt(a, m=n): M = (1 << m) - 1; return ((a & M) | (a >> m)).bit_count()
def span(gs):
    S = {0}
    for g in gs: S |= {s ^ g for s in S}
    return S
GEN = "XXXXXXXX ZZZZZZZZ XIXIZYZY XIYZXIYZ XZIYIYXZ".split()
def pauli(s, m=n):
    x = z = 0
    for i, c in enumerate(s):
        if c in 'XY': x |= 1 << i
        if c in 'ZY': z |= 1 << i
    return x | (z << m)
GOT = [pauli(s) for s in GEN]; SG = span(GOT)
NG = [v for v in range(1 << 16) if all(sp(v, g) == 0 for g in GOT)]

# ---------------- C1: natural-frame rotation symmetries over all labellings ----------------
VERT = [(v & 1, v >> 1 & 1, v >> 2 & 1) for v in range(8)]
def vidx(r): return r[0] + 2 * r[1] + 4 * r[2]
ROTS = []  # (vertex perm, axis perm, matrix)
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[perm[i], i] = sg[i]   # e_i -> sg_i e_perm(i)
        if round(np.linalg.det(M)) != 1: continue
        vp = []
        for r in VERT:
            s = M @ (2 * np.array(r) - 1)          # rotate about the cube centre
            vp.append(vidx(tuple((s + 1) // 2)))
        ROTS.append((tuple(vp), perm, M))
LAB = {0: (1, 0), 1: (1, 1), 2: (0, 1)}; INV = {v: k for k, v in LAB.items()}
def frame_of(perm):
    tab = {(0, 0): (0, 0)}
    for a in range(3): tab[LAB[a]] = LAB[perm[a]]
    return lambda x, z: tab[(x, z)]
def act(v, qp, fr):
    r = 0
    for j in range(n):
        x, z = fr((v >> j) & 1, (v >> (n + j)) & 1); t = qp[j]
        r |= (x << t) | (z << (n + t))
    return r
FRAMES = {perm: frame_of(perm) for perm in itertools.permutations(range(3))}
AUT = {perm: set() for perm in FRAMES}
allp = list(itertools.permutations(range(n)))
for perm, fr in FRAMES.items():
    for qp in allp:
        if all(act(g, qp, fr) in SG for g in GOT): AUT[perm].add(qp)
naut = {''.join(map(str, k)): len(v) for k, v in AUT.items()}
DIAG = {}
for k, (vp, perm, M) in enumerate(ROTS):
    if np.trace(M) == 0:  # order 3
        fx = [v for v in range(8) if vp[v] == v]; DIAG[k] = tuple(sorted(fx))
stab_hist = {}; diag_hist = {}; multi = 0; sample = None
for sig in allp:            # labelling: vertex v -> qubit sig[v]
    inv = [0] * 8
    for v in range(8): inv[sig[v]] = v
    st = []
    for k, (vp, perm, M) in enumerate(ROTS):
        qp = tuple(sig[vp[inv[q]]] for q in range(8))
        if qp in AUT[perm]: st.append(k)
    stab_hist[len(st)] = stab_hist.get(len(st), 0) + 1
    ds = {DIAG[k] for k in st if k in DIAG}
    if len(ds) > 1: multi += 1
    for d in ds: diag_hist[d] = diag_hist.get(d, 0) + 1
    if ds and sample is None: sample = (sig, st)
check("C1a [T] natural-frame code automorphisms: qubit perms x axis-permutation frames; |{(perm, frame)}| = 168 (the full LC x perm Aut is realised by uniform frames)",
      sum(naut.values()) == 168, f"by frame {naut}")
check("C1b [T] PRE-RUN EXPECTATION FAILED: the code-symmetric subgroup of O is NOT always <= C3. Histogram of |stab| over 8! labellings: "
      "1, 2, 3, 4 (V4) and 12 (= T = A4, all four 3-fold axes) for 168 labellings; never a 4-fold turn",
      stab_hist == {1: 31584, 2: 4032, 3: 3360, 4: 1176, 12: 168} and multi == 168, f"|stab| histogram {dict(sorted(stab_hist.items()))}, multi-diagonal {multi}")
check("C1c [T] each body diagonal is selected by 1008 labellings (no diagonal preferred: cube rotations permute them); 3360 labellings select "
      "exactly one diagonal, 168 (the maximally symmetric ones, stabiliser A4) select all four",
      len(diag_hist) == 4 and set(diag_hist.values()) == {1008}, f"{ {''.join(map(str, d)): c for d, c in diag_hist.items()} } (keys = fixed vertices)")
# A4 labelling: is any index-3 sublattice invariant under all four 3-fold turns?
A4lab = next(sg for sg in allp if (lambda inv: sum(tuple(sg[vp[inv[q]]] for q in range(8)) in AUT[perm] for vp, perm, M in ROTS))
             ([sg.index(q) for q in range(8)]) == 12)
Ms3 = [M for vp, perm, M in ROTS if np.trace(M) == 0]
hyp3 = set()
for v in itertools.product(range(3), repeat=3):
    if any(v):
        u = next(x for x in v if x); hyp3.add(tuple(x * pow(u, -1, 3) % 3 for x in v))
inv_all = [v for v in hyp3 if all(any(all((lam * a - b) % 3 == 0 for a, b in zip(v, [int(t) % 3 for t in M.T @ np.array(v)])) for lam in (1, 2)) for M in Ms3)]
check("C1d [T] for an A4 (maximally symmetric) labelling, NO index-3 sublattice of Z^3 is invariant under the code's symmetry group "
      "(0 of 13 invariant under all eight 3-fold turns): the most symmetric tiling disfavours any mod-3 class rule", len(inv_all) == 0,
      f"A4 labelling {A4lab}, invariant {len(inv_all)}")
# ---------------- C2: code-preserving translations of the tiled code ----------------
# weight-split: a weight-6 stabiliser shifted by a vector with an odd component straddles two cells; restrictions must have
# weight in {0,6,8} per cell (cell group weights), impossible for 6 = k + (6-k) with both k, 6-k > 0 -> no LC rescues it.
cellw = sorted({wt(s) for s in SG})
ok_split = True
for s in SG:
    if wt(s) != 6: continue
    sup = [j for j in range(8) if ((s | (s >> n)) >> j) & 1]
    for ax in range(3):  # shift by e_ax: layer r_ax = 1 leaves the cell
        k = sum(VERT[j][ax] == 0 for j in sup)   # sites that stay in the cell after the shift
        if k in (0, 6): ok_split = False
check("C2a [T] cell-group weights {0,6,8}; every weight-6 stabiliser shifted by a one-site step e_i splits k + (6-k) with 0 < k < 6 across two cells, "
      "so NO translation with an odd component (with ANY local Clifford) preserves the tiled code", cellw == [0, 6, 8] and ok_split, f"weights {cellw}")
# direct 16-qubit check: x in 0..3 (period 4), y, z in 0..1; cells x in {0,1}, {2,3}; one labelling with a C3 symmetry
sig = sample[0]; m2 = 16
def site(x, y, z): return x + 4 * y + 8 * z
def tiled_gens():
    gs = []
    for c0 in (0, 2):
        for g in GOT:
            x = z = 0
            for v in range(8):
                q = sig[v]; a, b, c = VERT[v]; s = site(c0 + a, b, c)
                x |= ((g >> q) & 1) << s; z |= ((g >> (n + q)) & 1) << s
            gs.append(x | (z << m2))
    return gs
TG = tiled_gens(); TS = span(TG)
def shift_map(g, dx, fr):
    r = 0
    for x0 in range(4):
        for y0 in range(2):
            for z0 in range(2):
                s = site(x0, y0, z0); t = site((x0 + dx) % 4, y0, z0)
                xb, zb = fr((g >> s) & 1, (g >> (m2 + s)) & 1); r |= (xb << t) | (zb << (m2 + t))
    return r
res = {dx: sum(all(shift_map(g, dx, fr) in TS for g in TG) for fr in FRAMES.values()) for dx in (1, 2, 3)}
check("C2b [T] 16-qubit tiling (2 cells, period 4): shift by 2e_1 preserves the tiled code; shifts by e_1, 3e_1 fail for all 6 uniform frames",
      len(TS) == 1024 and res[2] >= 1 and res[1] == 0 and res[3] == 0, f"frames preserving per shift {res}")
cls = sorted({(2 * a) % 3 for a in range(3)})
check("C2c [T] code-preserving translations = cell lattice 2Z^3 (C2a); their class change 2(n1+n2+n3) mod 3 takes all values {0,1,2}: "
      "the code admits class-changing hops 2e_i, it does not select the x+y+z = 0 mod 3 hop sublattice", cls == [0, 1, 2], f"class changes {cls}")

# ---------------- C3: Heisenberg pair on slot x cell torus ----------------
N = 3; cells = list(itertools.product(range(N), repeat=3)); ci = {c: i for i, c in enumerate(cells)}
def posop(f):
    U = np.zeros((27, 27))
    for c in cells: U[ci[f(c)], ci[c]] = 1
    return U
S3 = np.roll(np.eye(3), 1, axis=0)
Om = np.kron(np.diag([w ** ((2 * sum(c)) % 3) for c in cells]), np.eye(3))
Tt = np.kron(posop(lambda c: ((c[0] + 1) % N, c[1], c[2])), np.eye(3))
Cc = np.kron(posop(lambda c: (c[2], c[0], c[1])), S3)
def comm(A, B): return A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
def scal(M):
    s = M[0, 0]; return (s if np.allclose(M, s * np.eye(len(M))) else None)
cC, cT = scal(comm(Cc, Om)), scal(comm(Tt, Om)); G = Tt @ Cc; cG = scal(comm(G, Om))
fam_blind = np.allclose(Tt @ np.kron(np.eye(27), S3), np.kron(np.eye(27), S3) @ Tt)
check("C3a [T] the family-cycling turn C commutes with Omega = omega^(x+y+z) (C preserves x+y+z); the cell translation gives "
      "T Omega T^-1 Omega^-1 = omega^(-2) 1 but acts trivially on family slots", cC is not None and abs(cC - 1) < 1e-12 and cT is not None
      and abs(cT - w ** -2) < 1e-12 and fam_blind, f"C: {np.round(cC, 6)}, T: {np.round(cT, 3)}")
nogo = 0
for vp, perm, M in ROTS:
    for inv_ in (1, -1):
        R = inv_ * M
        U = np.kron(posop(lambda c, R=R: tuple(int(t) % N for t in R @ np.array(c))), np.eye(3))
        s = scal(comm(U, Om))
        if s is not None and abs(s - 1) > 1e-9: nogo += 1
check("C3b [T] no element of O_h (fixing a cell) satisfies g Omega g^-1 = omega^k Omega with omega^k != 1: a point-group family shift "
      "can never be the Delta(27) shift (the phase at the fixed cell is 1)", nogo == 0, f"violations {nogo} of 48")
T111 = np.kron(posop(lambda c: tuple((x + 1) % N for x in c)), np.eye(3))
check("C3c [T] the code-preserving screw G = T C cycles the family slots AND gives G Omega G^-1 Omega^-1 = omega^(-2) 1 (a Heisenberg pair); "
      "G^3 = cell translation by (1,1,1) (class-neutral; pre-run guess G^3 = 1 was wrong)", cG is not None and abs(cG - w ** -2) < 1e-12
      and np.allclose(np.linalg.matrix_power(G, 3), T111) and not np.allclose(T111, np.eye(81)),
      f"{np.round(cG, 3)}")
# Omega is a symmetry only of class-preserving dynamics: random family-blind code-preserving nearest-cell hop
Hh = sum(rng.normal() * (np.kron(posop(lambda c, a=a: tuple((c[i] + (i == a)) % N for i in range(3))), np.eye(3))) for a in range(3))
Hh = Hh + Hh.T
check("C3d [F] a family-blind code-preserving hop H = sum_i t_i (T_i + T_i^dag) (cell steps 2e_i) does not commute with Omega: the clock is not "
      "a symmetry unless the class-preserving rule is ADDED", np.linalg.norm(Hh @ Om - Om @ Hh) > 1e-3, f"||[H,Omega]|| = {np.linalg.norm(Hh @ Om - Om @ Hh):.2f}")
# on-site diagonal omega-phases as logical clocks
I2 = np.eye(2); PX = np.array([[0, 1], [1, 0]]); PY = np.array([[0, -1j], [1j, 0]]); PZ = np.diag([1, -1])
def kr(ms):
    out = np.array([[1.0 + 0j]])
    for mm in ms: out = np.kron(out, mm)
    return out
PM = {'I': I2, 'X': PX, 'Y': PY, 'Z': PZ}
Pj = np.eye(256, dtype=complex)
for s in GEN: Pj = Pj @ (np.eye(256) + kr([PM[c] for c in reversed(s)])) / 2   # qubit 0 = least significant bit
ev, vec = np.linalg.eigh((Pj + Pj.conj().T) / 2); Q = vec[:, ev > 0.5]
Hd = np.array([[1, 1], [1, -1]]) / np.sqrt(2); Sd = np.diag([1, 1j])
bits = np.array([[(s >> j) & 1 for s in range(256)] for j in range(8)])
fs = np.array(list(itertools.product(range(3), repeat=8))); ph = w ** ((fs @ bits) % 3)
pres = {}
for name, V in (('Z', np.eye(2)), ('X', Hd), ('Y', Sd @ Hd)):
    Qa = kr([V.conj().T] * 8) @ Q; cnt = 0
    for i0 in range(0, len(fs), 729):
        UQ = ph[i0:i0 + 729, :, None] * Qa[None]
        rr = UQ - np.einsum('ij,fjk->fik', Qa, np.einsum('ji,fjk->fik', Qa.conj(), UQ))
        cnt += int((np.linalg.norm(rr, axis=(1, 2)) < 1e-8).sum())
    pres[name] = cnt
check("C3e [T] code space dim 8; of the 3^8 on-site phase patterns diag(1, omega^f_j) (axis Z, X or Y) only f = 0 preserves the code: "
      "no on-site omega-clock acts on the logical slots", Q.shape[1] == 8 and all(v == 1 for v in pres.values()), f"preserving per axis {pres}")
# class content of the 108 cyclic logical bases (natural-frame turn of the sample labelling)
sig_s, st_s = sample; kk = next(k for k in st_s if k in DIAG); vp, perm, M = ROTS[kk]
inv = [0] * 8
for v in range(8): inv[sig_s[v]] = v
tau = tuple(sig_s[vp[inv[q]]] for q in range(8)); fr = FRAMES[perm]
axis = np.array(VERT[DIAG[kk][1]]) - np.array(VERT[DIAG[kk][0]])  # body diagonal vector
basisS = {}
def red(v):
    for pv in sorted(basisS, reverse=True):
        if v >> pv & 1: v ^= basisS[pv]
    return v
for g in GOT:
    v = red(g); basisS[v.bit_length() - 1] = v
    for pv in list(basisS):
        if pv != v.bit_length() - 1 and basisS[pv] >> (v.bit_length() - 1) & 1: basisS[pv] ^= v
reps = sorted({red(v) for v in NG}); g_ = lambda v: red(act(v, tau, fr))
def cls_content(v):  # multiset of axis-class (axis . r mod 3) over the support, minimised over the stabiliser coset
    best = None
    for s in SG:
        u = v ^ s; sup = [inv[j] for j in range(8) if ((u | (u >> n)) >> j) & 1]
        key = tuple(sorted(int(axis @ np.array(VERT[x])) % 3 for x in sup))
        if best is None or (len(key), key) < (len(best), best): best = key
    return best
nb = 0; same = 0
for x1 in reps:
    if not x1: continue
    xs = [x1, g_(x1), g_(g_(x1))]
    if any(sp(a, b) for a in xs for b in xs): continue
    for z1 in reps:
        zs = [z1, g_(z1), g_(g_(z1))]
        if all(sp(xs[a], zs[b]) == (a == b) for a in range(3) for b in range(3)) and not any(sp(a, b) for a in zs for b in zs):
            nb += 1
            if len({cls_content(x) for x in xs}) == 1 and len({cls_content(z) for z in zs}) == 1: same += 1
check("C3f [T] in all 108 bases where the turn is a literal 3-cycle of the logical qubits, the three families have identical class content "
      "(axis.r mod 3 over minimal supports): no family sits in its own x+y+z class, so slot = class (families = Omega-eigenspaces) is impossible",
      nb == 108 and same == 108, f"bases {nb}, identical {same}, axis {axis.tolist()}")

# ---------------- C4: C3-invariant index-p sublattices ----------------
Pc = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
def inv_hyper(p):
    vs = set()
    for v in itertools.product(range(p), repeat=3):
        if not any(v): continue
        u = next(x for x in v if x); ui = pow(u, -1, p); vs.add(tuple(x * ui % p for x in v))
    good = []
    for v in vs:
        img = tuple(int(t) % p for t in Pc.T @ np.array(v))
        if any(all((lam * a - b) % p == 0 for a, b in zip(v, img)) for lam in range(1, p)): good.append(v)
    return len(vs), sorted(good)
c4 = {p: inv_hyper(p) for p in (2, 3, 5, 7)}
check("C4 [T] index-p sublattices invariant under the (111) turn: p = 3 has exactly one of 13 (x+y+z = 0 mod 3); but p = 2, 5 also have exactly one "
      "(x+y+z = 0 mod p) and p = 7 has three: the turn fixes WHICH sublattice once an index is given, not the index 3",
      c4[3] == (13, [(1, 1, 1)]) and len(c4[2][1]) == 1 and len(c4[5][1]) == 1 and len(c4[7][1]) == 3,
      str({p: (a, len(b)) for p, (a, b) in c4.items()}))
print("VERDICT: PARTIALLY by the pre-set rule (C2, C3 NO; C4 unique), effectively NO. The axis is a labelling choice (1008 per diagonal) and the "
      "maximally symmetric labellings keep all four diagonals (A4); given a C3-only labelling AND an index-3 class rule the lattice is x+y+z mod 3, "
      "but the code admits class-changing hops 2e_i, its family shift commutes with the clock, no on-site clock reaches the slots, and the "
      "Heisenberg screw T C exists only once the clock is imposed. Families = slots = Delta(27) irrep is not derived.")
print(f"Supplied: Gottesman generators, natural frame, code uniqueness (prior runner). time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={P} FAIL={F}")
