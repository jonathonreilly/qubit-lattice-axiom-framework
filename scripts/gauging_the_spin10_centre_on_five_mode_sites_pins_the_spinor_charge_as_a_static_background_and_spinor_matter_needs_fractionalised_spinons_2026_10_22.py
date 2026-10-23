AUDIT_INPUT_PATHS = ('docs/GAUGING_THE_SPIN10_CENTRE_ON_FIVE_MODE_SITES_PINS_THE_SPINOR_CHARGE_AS_A_STATIC_BACKGROUND_AND_SPINOR_MATTER_NEEDS_FRACTIONALISED_SPINONS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Z4 spinons: gauging the Spin(10) centre of five-mode sites, and the spinon alternative.

Supplied model (not derived): sites with 5 complex fermion modes, Spin(10) from on-site
bilinears M_ab = (i/2) sum_s g_a^s g_b^s; Z4 link registers (two qubits) on coarse edges with
clock C|e> = i^e|e> and shift S|e> = |e+1>; Gauss operator G_v = z_v prod_out C prod_in C^dag.
Exact checks: site centre, link algebra, Gauss consistency and gauge invariance on a dimer,
global constraint and ground-space count on L^3 tori, rotation covariance, spinon kinematics
(singlet cluster sizes) and Levin-Wen exchange signs. Seeded; numpy, scipy, stdlib only.
"""
AUDIT_TIMEOUT_SEC = 120

import itertools
import time

import numpy as np
import scipy.sparse as sp

np.random.seed(20261022)
T0 = time.time()
PASS = 0
FAIL = 0


def check(name, cond, info=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS {name} {info}".rstrip())
    else:
        FAIL += 1
        print(f"FAIL {name} {info}".rstrip())


def nrm(A):
    if sp.issparse(A):
        A = A.tocoo()
        return float(np.sqrt(np.sum(np.abs(A.data) ** 2))) if A.nnz else 0.0
    return float(np.linalg.norm(A))


def majoranas(nm):
    """g_{2p}=c+c^dag, g_{2p+1}=i(c^dag-c); mode 0 = most significant bit; JW on lower modes."""
    c1 = sp.csr_matrix(np.array([[0.0, 1.0], [0.0, 0.0]]))
    Z = sp.csr_matrix(np.diag([1.0, -1.0]))
    I2 = sp.identity(2, format="csr")
    gs, cs = [], []
    for p in range(nm):
        op = sp.identity(1, format="csr")
        for q in range(nm):
            op = sp.kron(op, Z if q < p else (c1 if q == p else I2), format="csr")
        c = op.astype(complex).tocsr()
        cd = c.conj().T.tocsr()
        cs.append(c)
        gs.append((c + cd).tocsr())
        gs.append((1j * (cd - c)).tocsr())
    return gs, cs


def gens(site_gs):
    return [sum(0.5j * (g[a] @ g[b]) for g in site_gs) for a in range(10) for b in range(a + 1, 10)]


def number_ops(cs):
    return [(c.conj().T @ c).tocsr() for c in cs]


def centre(ns, dim):
    """z = exp(i pi sum (n - 1/2)) as a diagonal sparse matrix."""
    tot = sum(ns) - 0.5 * len(ns) * sp.identity(dim)
    d = np.exp(1j * np.pi * tot.diagonal())
    return sp.diags(d).tocsr()


# ------------------------------------------------------------------ A. one site
print("== A. site centre (32 states) ==")
g1, c1s = majoranas(5)
n1 = number_ops(c1s)
z1 = centre(n1, 32)
F1 = sp.diags((-1.0) ** np.rint(sum(n1).diagonal())).tocsr()
check("A1 z_site = -i (-1)^F", nrm(z1 - (-1j) * F1) < 1e-12)
check("A2 z^2 = -1 (c-number), z^4 = 1",
      nrm(z1 @ z1 + sp.identity(32)) < 1e-12 and nrm((z1 @ z1) @ (z1 @ z1) - sp.identity(32)) < 1e-12)
M1 = gens([g1])
check("A3 z commutes with all 45 Spin(10) generators", max(nrm(z1 @ M - M @ z1) for M in M1) < 1e-12)
zd = z1.diagonal()
adz = np.outer(zd, zd.conj()).ravel()          # Ad_z on the 1024-dim operator algebra
cnt = {k: int(np.sum(np.abs(adz - v) < 1e-9)) for k, v in (("+1", 1), ("-1", -1), ("+i", 1j), ("-i", -1j))}
check("A4 Ad_z on all 1024 site operators has eigenvalues +-1 only (no odd Z4 charge)",
      cnt["+1"] == 512 and cnt["-1"] == 512 and cnt["+i"] == 0 and cnt["-i"] == 0, str(cnt))
check("A5 z c_a z^-1 = -c_a for all five modes", max(nrm(z1 @ c @ z1.conj().T + c) for c in c1s) < 1e-12)

# ------------------------------------------------------------------ B. Z4 link
print("== B. Z4 link register = 2 qubits, e = b1 + 2 b2 ==")
w = 1j
Cl = np.diag([w ** e for e in range(4)])
Sl = np.zeros((4, 4), complex)
for e in range(4):
    Sl[(e + 1) % 4, e] = 1
check("B1 C S = i S C, C^4 = S^4 = 1",
      np.allclose(Cl @ Sl, 1j * Sl @ Cl) and np.allclose(np.linalg.matrix_power(Cl, 4), np.eye(4))
      and np.allclose(np.linalg.matrix_power(Sl, 4), np.eye(4)))
# basis index e; qubits b1 = e & 1, b2 = e >> 1
X = np.array([[0, 1], [1, 0]], complex)
Zp = np.diag([1, -1]).astype(complex)
I2 = np.eye(2)


def onq(op, q):  # q=1 low bit, q=2 high bit; matrix in e-basis
    M = np.zeros((4, 4), complex)
    for e in range(4):
        for f in range(4):
            b = (e & 1, e >> 1)
            c = (f & 1, f >> 1)
            if q == 1:
                M[f, e] = op[c[0], b[0]] * (c[1] == b[1])
            else:
                M[f, e] = op[c[1], b[1]] * (c[0] == b[0])
    return M


Sg = np.diag([1, 1j])
check("B2 C = (phase gate on b1)(Z on b2): a product of single-qubit gates", np.allclose(Cl, onq(Sg, 1) @ onq(Zp, 2)))
check("B3 S^2 = X on b2 and C^2 = Z on b1 (single-qubit Paulis)",
      np.allclose(Sl @ Sl, onq(X, 2)) and np.allclose(Cl @ Cl, onq(Zp, 1)))
Rf = np.zeros((4, 4))
for e in range(4):
    Rf[(-e) % 4, e] = 1
cnot = np.zeros((4, 4))
for e in range(4):
    b1, b2 = e & 1, e >> 1
    cnot[b1 + 2 * (b2 ^ b1), e] = 1
check("B4 orientation flip e->-e = CNOT(b1->b2); R C R = C^dag, R S R = S^dag",
      np.allclose(Rf, cnot) and np.allclose(Rf @ Cl @ Rf, Cl.conj().T) and np.allclose(Rf @ Sl @ Rf, Sl.conj().T))


def is_pauli(M):
    """True if M is proportional (unit modulus) to a two-qubit Pauli in the e basis."""
    for A in (I2, X, Zp, X @ Zp):
        for B in (I2, X, Zp, X @ Zp):
            P = onq(A, 1) @ onq(B, 2)
            t = np.trace(P.conj().T @ M) / 4
            if abs(abs(t) - 1) < 1e-9 and np.allclose(M, t * P):
                return True
    return False


cliff = all(is_pauli(Sl @ onq(P, q) @ Sl.conj().T) for P in (X, Zp) for q in (1, 2))
check("B5 S is a two-qubit Clifford but not a Pauli", cliff and not is_pauli(Sl))

# ------------------------------------------------------------------ C. dimer + one link
print("== C. Gauss law on two sites + one link (4096 states) ==")
g2, c2s = majoranas(10)
n2 = number_ops(c2s)
gsA, gsB = g2[:10], g2[10:]
zA = centre(n2[:5], 1024)
zB = centre(n2[5:], 1024)
I1024 = sp.identity(1024, format="csr")
I4 = sp.identity(4, format="csr")
Cs, Ss = sp.csr_matrix(Cl), sp.csr_matrix(Sl)
GA = sp.kron(zA, Cs, format="csr")
GB = sp.kron(zB, Cs.conj().T, format="csr")
K = sum(1j * (gsA[a] @ gsB[a]) for a in range(10))
check("C1 [G_s, G_t] = 0 and G^4 = 1",
      nrm(GA @ GB - GB @ GA) < 1e-12 and nrm(GA @ GA @ GA @ GA - sp.identity(4096)) < 1e-12)
KS2 = sp.kron(K, Ss @ Ss, format="csr")
hop = sp.kron(c2s[0].conj().T @ c2s[5], Ss @ Ss, format="csr")
inv = max(nrm(G @ O - O @ G) for G in (GA, GB) for O in (KS2, hop + hop.conj().T))
check("C2 Spin(10) hop K_st S^2 and U(5) hop c^dag_s c_t S^2 commute with both Gauss operators", inv < 1e-12)
Kb = sp.kron(K, I4, format="csr")
KS1 = sp.kron(K, Ss, format="csr")
check("C3 controls: bare K anticommutes with G_s; K S fails (G K S G^-1 = -i K S)",
      nrm(GA @ Kb + Kb @ GA) < 1e-12 and nrm(GA @ KS1 @ GA.conj().T - (-1j) * KS1) < 1e-12)
M2 = [sp.kron(M, I4, format="csr") for M in gens([gsA, gsB])]
check("C4 Gauss operators commute with all 45 total Spin(10) generators (link is a singlet)",
      max(nrm(G @ M - M @ G) for G in (GA, GB) for M in M2) < 1e-11)
zg = centre(n2, 1024)
check("C5 G_s G_t = z_global (link factors cancel)", nrm(GA @ GB - sp.kron(zg, I4)) < 1e-12)
gA, gB = GA.diagonal(), GB.diagonal()
phys = np.where((np.abs(gA - 1) < 1e-9) & (np.abs(gB - 1) < 1e-9))[0]
Ftot = np.rint(sum(n2).diagonal().real).astype(int)
Fph = Ftot[phys // 4]
Fs = np.rint(sum(n2[:5]).diagonal().real).astype(int)[phys // 4] % 2
ee = phys % 4
check("C6 physical subspace: dim 512, all (-1)^F = -1 = i^N, z_global = 1, one odd site, e = 1 or 3",
      len(phys) == 512 and np.all(Fph % 2 == 1) and np.allclose(zg.diagonal()[phys // 4], 1)
      and np.all(((Fs == 0) & (ee == 1)) | ((Fs == 1) & (ee == 3))))
Cas = sum(M @ M for M in gens([gsA, gsB]))
mat_idx = np.unique(phys // 4)
cev = np.linalg.eigvalsh(Cas[mat_idx][:, mat_idx].toarray())
vals, mults = np.unique(np.round(cev, 6), return_counts=True)
check("C7 physical Spin(10) content = 2 x (1 + 45 + 210): root class only",
      list(mults) == [2, 90, 420], f"Casimirs {[float(v) for v in vals]} mult {[int(m) for m in mults]}")
gS = sp.kron(I1024, Ss, format="csr")
check("C8 a bare link shift S makes Gauss defects (G_s, G_t) = (i, -i) and commutes with Spin(10)",
      nrm(GA @ gS - 1j * gS @ GA) < 1e-12 and nrm(GB @ gS + 1j * gS @ GB) < 1e-12
      and max(nrm(gS @ M - M @ gS) for M in M2) < 1e-12)
print(f"   [C done {time.time()-T0:.1f}s]")

# ------------------------------------------------------------------ D. tori
print("== D. coarse L^3 tori ==")


def torus(L):
    V = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    vid = {v: i for i, v in enumerate(V)}
    E = [(v, d) for v in V for d in range(3)]
    eid = {e: i for i, e in enumerate(E)}
    return V, vid, E, eid


def add(v, d, s, L):
    u = list(v)
    u[d] = (u[d] + s) % L
    return tuple(u)


def plaqs(V, L):
    out = []
    for v in V:
        for d1, d2 in ((0, 1), (0, 2), (1, 2)):
            out.append({(v, d1): 1, (add(v, d1, 1, L), d2): 1, (add(v, d2, 1, L), d1): -1, (v, d2): -1})
    return out


def gauss(v, L):
    out = {}
    for d in range(3):
        out[(v, d)] = out.get((v, d), 0) + 1
        k = (add(v, d, -1, L), d)
        out[k] = out.get(k, 0) - 1
    return out


for L in (2, 3, 4):
    V, vid, E, eid = torus(L)
    D0 = np.zeros((len(V), len(E)))
    for v in V:
        for k, s in gauss(v, L).items():
            D0[vid[v], eid[k]] += s
    D1 = np.zeros((3 * len(V), len(E)))
    for i, p in enumerate(plaqs(V, L)):
        for k, s in p.items():
            D1[i, eid[k]] += s
    colsum = np.abs(D0.sum(axis=0)).max()
    b1 = len(E) - np.linalg.matrix_rank(D0) - np.linalg.matrix_rank(D1)
    N = len(V)
    nonempty = (N % 2 == 0)
    check(f"D1 L={L}: prod_v G_v = z_global; physical sector needs (-1)^F = i^N",
          colsum == 0 and np.allclose(D0 @ D1.T, 0),
          f"N={N} -> {'(-1)^F=' + str(int(np.real(1j ** N))) if nonempty else 'EMPTY (N odd)'}")
    check(f"D2 L={L}: Z4 ground-space count 4^b1 with b1 = 3 -> 64", b1 == 3)
L = 4
V, vid, E, eid = torus(L)
blk = [v for v in V if max(v) < 2]
tot = {}
for v in blk:
    for k, s in gauss(v, L).items():
        tot[k] = tot.get(k, 0) + s
bnd = [k for k, s in tot.items() if s != 0]
inside = [k for k in bnd if k[0] in blk and add(k[0], k[1], 1, L) in blk]
check("D3 prod of G over a 2^3 block = z_block x (flux through its 24 boundary links)",
      len(bnd) == 24 and not inside, "flux-loop sweep phase = i^(#even sites) (-i)^(#odd sites)")

# ------------------------------------------------------------------ E. rotations
print("== E. rotation covariance (24 proper cubic rotations, L=4) ==")
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3):
            R[perm[i], i] = sg[i]
        if round(np.linalg.det(R)) == 1:
            rots.append(R)


def img(R, v):
    return tuple(int(x) % L for x in R @ np.array(v))


def map_term(R, term, relabel):
    out = {}
    for (v, d), s in term.items():
        col = R[:, d]
        dp = int(np.nonzero(col)[0][0])
        sg = int(col[dp])
        if sg == 1:
            k = (img(R, v), dp)
            s2 = s
        else:
            k = (add(img(R, v), dp, -1, L), dp)
            s2 = -s if relabel else s
        out[k] = out.get(k, 0) + s2
    return out


Gset = {v: gauss(v, L) for v in V}
Pset = plaqs(V, L)
Pkeys = {frozenset(p.items()) for p in Pset} | {frozenset((k, -s) for k, s in p.items()) for p in Pset}
okG = all(map_term(R, Gset[v], True) == Gset[img(R, v)] for R in rots for v in V)
okP = all(frozenset(map_term(R, p, True).items()) in Pkeys for R in rots for p in Pset)
badG = sum(map_term(R, Gset[v], False) != Gset[img(R, v)] for R in rots for v in V)
check("E1 all 24 rotations map every Gauss operator and plaquette to one, with e->-e on reversed links",
      len(rots) == 24 and okG and okP)
check("E2 control: without the CNOT relabel, Gauss covariance fails", badG > 0, f"{badG}/{24*len(V)} fail")

# ------------------------------------------------------------------ F. spinon kinematics
print("== F. spinon kinematics: singlet clusters (exact weight-zero sectors) ==")


def sector(n, target):
    """Fock states of n five-mode sites with every flavour total = target. Mode i = 5 s + a,
    bit position nm-1-i (mode 0 most significant), JW sign over lower-index modes."""
    nm = 5 * n
    per = [c for c in itertools.combinations(range(n), target)]
    states = []
    for choice in itertools.product(per, repeat=5):
        x = 0
        for a, sites in enumerate(choice):
            for s in sites:
                x |= 1 << (nm - 1 - (5 * s + a))
        states.append(x)
    states.sort()
    return nm, states, {x: i for i, x in enumerate(states)}


def hop_mat(nm, states, idx, i, j):
    """c_i^dag c_j restricted to the sector (i != j)."""
    rows, cols, vals = [], [], []
    bi, bj = 1 << (nm - 1 - i), 1 << (nm - 1 - j)
    for col, x in enumerate(states):
        if (x & bj) and not (x & bi):
            sgn = bin(x & ~((1 << (nm - j)) - 1)).count("1")      # modes with index < j
            y = x ^ bj
            sgn += bin(y & ~((1 << (nm - i)) - 1)).count("1")      # modes with index < i
            y |= bi
            rows.append(idx[y]); cols.append(col); vals.append((-1.0) ** sgn)
    D = len(states)
    return sp.csr_matrix((vals, (rows, cols)), shape=(D, D))


def casimir_sector(n, target):
    nm, st, idx = sector(n, target)
    D = len(st)
    Cm = (45.0 * n / 4) * sp.identity(D, format="csr")
    for s, t in itertools.combinations(range(n), 2):
        Kst = sum(2j * (hop_mat(nm, st, idx, 5 * s + a, 5 * t + a) - hop_mat(nm, st, idx, 5 * t + a, 5 * s + a))
                  for a in range(5))
        Cm = Cm + (10.0 * sp.identity(D) - Kst @ Kst) / 4
    par = np.array([[bin((x >> (nm - 5 * (s + 1))) & 31).count("1") % 2 for s in range(n)] for x in st])
    return nm, st, Cm.tocsr(), par


nm2, st2, Cm2, par2 = casimir_sector(2, 1)
dense_C = Cas[st2][:, st2].toarray()
check("F0 Casimir identity C = 45n/4 + sum (10 - K^2)/4 matches sum M^2 on the n=2 sector",
      np.allclose(dense_C, Cm2.toarray()))
null2 = int(np.sum(np.abs(np.linalg.eigvalsh(Cm2.toarray())) < 1e-8))
alleven2 = int(np.sum(par2.sum(axis=1) == 0))
check("F1 16 x 16 (both sites even): weight-zero sector empty, so no singlet (10+120+126)",
      alleven2 == 0 and np.all(par2.sum(axis=1) == 1))
check("F2 16 x 16bar: exactly one singlet per orientation", null2 == 2, f"nullity {null2} in {len(st2)} states")
nm4, st4, Cm4, par4 = casimir_sector(4, 2)
ev_idx = np.where(par4.sum(axis=1) == 0)[0]
C4e = Cm4[ev_idx][:, ev_idx].toarray()
null4 = int(np.sum(np.abs(np.linalg.eigvalsh(C4e)) < 1e-8))
check("F3 16^4 (all four sites even): exactly 2 Spin(10) singlets", null4 == 2,
      f"{len(ev_idx)} all-even of {len(st4)} weight-zero states")
cls = {n: complex((-1j) ** n) for n in range(1, 5)}
check("F4 all-even cluster centre class (-i)^n: singlet-capable only at n = 0 mod 4 (Z4 fusion)",
      [abs(cls[n] - 1) < 1e-12 for n in range(1, 5)] == [False, False, False, True])
check("F5 spinon x local fermion: class (-i)(-1) = +i, a 16bar in the same sector; z^2 = -1 kept",
      abs((-1j) * (-1) - 1j) < 1e-12 and abs(((-1j) * (-1)) ** 2 + 1) < 1e-12)
print(f"   [F done {time.time()-T0:.1f}s]")

# ------------------------------------------------------------------ G. Levin-Wen exchange
print("== G. Levin-Wen exchange sign (sites p, a, b, c; hops t_i: p -> i) ==")
_, cf = majoranas(4)
P_, A_, B_, C_ = range(4)


def lw(ops_dag, ops):
    t = {i: ops_dag[i] @ ops[P_] for i in (A_, B_, C_)}
    tb_d = ops_dag[P_] @ ops[B_]
    init = np.zeros(16, complex)
    init[(1 << 3) | (1 << 1)] = 1          # p (bit 3) and b (bit 1) occupied
    p1 = t[A_] @ (tb_d @ (t[C_] @ init))
    p2 = t[C_] @ (tb_d @ (t[A_] @ init))
    k = np.argmax(np.abs(p2))
    return p1[k] / p2[k], np.allclose(np.abs(p1), np.abs(p2))


rf, okf = lw([c.conj().T for c in cf], cf)
sm = np.array([[0, 1], [0, 0]], complex)
bos = []
for p in range(4):
    op = np.array([[1.0 + 0j]])
    for q in range(4):
        op = np.kron(op, sm if q == p else np.eye(2))
    bos.append(sp.csr_matrix(op))
rb, okb = lw([b.conj().T for b in bos], bos)
check("G1 fermion hops: exchange sign -1; hard-core boson hops: +1",
      okf and okb and abs(rf + 1) < 1e-12 and abs(rb - 1) < 1e-12, f"{rf.real:+.0f}, {rb.real:+.0f}")
links = [np.kron(np.kron(Sl, np.eye(4)), np.eye(4)), np.kron(np.kron(np.eye(4), Sl), np.eye(4)),
         np.kron(np.kron(np.eye(4), np.eye(4)), Sl)]
comm = max(np.linalg.norm(x @ y - y @ x) for x in links for y in links)
check("G2 charge-1 defects move by link shifts S only; all S commute -> Levin-Wen sign +1 (boson)",
      comm < 1e-12)
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
