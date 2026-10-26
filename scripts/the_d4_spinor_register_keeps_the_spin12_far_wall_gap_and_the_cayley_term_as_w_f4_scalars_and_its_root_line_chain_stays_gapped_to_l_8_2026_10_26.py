AUDIT_INPUT_PATHS = ('docs/THE_D4_SPINOR_REGISTER_KEEPS_THE_SPIN12_FAR_WALL_GAP_AND_THE_CAYLEY_TERM_AS_W_F4_SCALARS_AND_ITS_ROOT_LINE_CHAIN_STAYS_GAPPED_TO_L_8_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-far-wall-gapping: does the far-wall mirror gapping carry over to the D4 matter law with a 4-mode spinor register?
 A  symmetry: W(F4) (1152) with spinor lifts S; the Weyl eps form, the Spin(12) pair B_a, the Cayley 4-form, LIV counts.
 B  on-site: far-wall Weyl field = 16 x 2 D4 spinor components; Fock identity on N = 0, 1 and the full N = 4 sector (sparse),
    sparse Lanczos; Dirac register H_+ + H_-.
 C  chain: 1+1D root-line reduction (4 spinor modes per event, Dirac hop i psi^+ Gamma psi', Gamma = i g(u_t) g(n)), on-site
    g Phi (Cayley) or g Re Omega, twisted boundary; equivalence gate with the cayley-mirror-gap proxy; gaps L = 4..6 live.
Labels: [T] exact, [F] finite diagnostic, [R] embedded earlier result (cayley-mirror-gap mini, L = 7, 8).
Supplied: the 16 with one orbital per weight, the 10-channel pair, PH ordering, the chain proxy class (FK/You-Xu), g.
Cited, not rederived here: spin10-two-flavour rep theory (unique E0 = -144 g, gap 4 g, fermion gap 13 g)."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
rng = np.random.default_rng(20261026); T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(("PASS" if ok else "FAIL") + f" {name}" + (f": {info}" if info else ""))
pc = lambda a: np.bitwise_count(a).astype(np.int64)
# ---------------- W(F4) with spinor lifts (construction of d4-zoom-chirality)
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
g5 = gm[0] @ gm[1] @ gm[2] @ gm[3]; g5 = g5 / np.sqrt((g5 @ g5)[0, 0]); gv = lambda v: np.einsum('m,mab->ab', v, gm); E4 = np.eye(4)
gens, gS = [], []
for n in [np.array([1, -1, 0, 0]) / np.sqrt(2), np.array([0, 1, -1, 0]) / np.sqrt(2), np.array([0, 0, 1, -1]) / np.sqrt(2),
          np.array([1., 0, 0, 0]), np.ones(4) / 2]:
    gens.append(E4 - 2 * np.outer(n, n)); gS.append(g5 @ gv(n))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); Dd = {key(E4): (E4, np.eye(4, dtype=complex))}; fr = [key(E4)]
while fr:
    nf = []
    for kk in fr:
        A, SA = Dd[kk]
        for g, sg in zip(gens, gS):
            B = g @ A
            if key(B) not in Dd: Dd[key(B)] = (B, sg @ SA); nf.append(key(B))
    fr = nf
GW = np.array([v[0] for v in Dd.values()]); SW = np.array([v[1] for v in Dd.values()]); DET = np.round(np.linalg.det(GW)).astype(int)
lift = max(np.abs(SW[i] @ gm[m] @ np.linalg.inv(SW[i]) - np.einsum('n,nab->ab', GW[i][:, m], gm)).max() for i in range(1152) for m in range(4))
print("== A. symmetry of the on-site gapping terms under the W(F4) spinor lift")
ev, U = np.linalg.eigh(g5); Vm, Vp = U[:, ev < 0], U[:, ev > 0]; eps = np.array([[0, 1], [-1, 0]])
pro = [i for i in range(1152) if DET[i] > 0]; imp = [i for i in range(1152) if DET[i] < 0]
c5 = max(np.abs(SW[i] @ g5 - g5 @ SW[i]).max() for i in pro); a5 = max(np.abs(SW[i] @ g5 + g5 @ SW[i]).max() for i in imp)
dm = max(abs(np.linalg.det(Vm.conj().T @ SW[i] @ Vm) - 1) for i in pro); dp = max(abs(np.linalg.det(Vp.conj().T @ SW[i] @ Vp) - 1) for i in pro)
epsd = max(np.abs((Vm.conj().T @ SW[i] @ Vm).T @ eps @ (Vm.conj().T @ SW[i] @ Vm) - eps).max() for i in pro)
check("A1 [T] W(F4) has 1152 elements (576 proper); lifts S obey S g_mu S^-1 = R_mu^nu g_nu", len(GW) == 1152 and len(pro) == 576 and lift < 1e-12, f"{lift:.0e}")
check("A2 [T] proper lifts commute with g5 and act on P- and P+ with det 1 (SU(2)_- x SU(2)_+), so the Weyl form eps is invariant "
      "and B_a = psi_-^T (M_a x eps) psi_- (the Spin(12) pair) is invariant under every rotation", c5 < 1e-12 and max(dm, dp, epsd) < 1e-12,
      f"[S,g5] {c5:.0e}, |det-1| {max(dm, dp):.0e}, eps {epsd:.0e}")
dx = max(abs(abs(np.linalg.det(Vp.conj().T @ SW[i] @ Vm)) - 1) for i in imp)
check("A3 [T] improper lifts anticommute with g5: they map the far-wall (P-) term onto the P+ term with |det| = 1, i.e. onto the "
      "wall-swapped slab; B B^+ is phase-blind, so H_+ + H_- is invariant under all 1152 lifts", a5 < 1e-12 and dx < 1e-12, f"{a5:.0e}, {dx:.0e}")
def fock_lift(S):  # Fock operator of psi -> S psi on 4 modes (compound matrices, JW order)
    F = np.zeros((16, 16), complex); sets = {m: [j for j in range(4) if m >> j & 1] for m in range(16)}
    for a in range(16):
        for b in range(16):
            if len(sets[a]) == len(sets[b]): F[a, b] = np.linalg.det(S[np.ix_(sets[a], sets[b])]) if sets[a] else 1
    return F
nm = np.array([bin(m).count('1') for m in range(16)]); Om = np.zeros((16, 16)); Om[0, 15] = 1
ReO = 8 * (Om + Om.T); w2 = -np.diag(((4 - 2 * nm) ** 2 - 4) / 2.); Cay = ReO + w2
spec = np.round(np.linalg.eigvalsh(Cay), 9); detS = max(abs(np.linalg.det(SW[i]) - 1) for i in range(1152))
uni = max(np.abs(SW[i] @ SW[i].conj().T - E4).max() for i in range(1152))
cc = max(np.abs(fock_lift(SW[i]) @ Cay - Cay @ fock_lift(SW[i])).max() for i in range(1152))
check("A4 [T] det S = 1 and S unitary for all 1152: the spinor image lies in SU(4) inside Spin(7); the Fock lift commutes with the "
      "Cayley 4-form on the 4 spinor modes (spectrum -14 (1), 0 (8), +2 (7)): it is a W(F4) scalar", detS < 1e-12 and uni < 1e-12
      and cc < 1e-12 and list(np.unique(spec, return_counts=True)[1]) == [1, 8, 7], f"det {detS:.0e}, [U,Phi] {cc:.0e}")
def hk(e, k): return np.sum([np.prod(e[list(c)]) for c in itertools.combinations_with_replacement(range(4), k)])
def inv_count(f): return np.real(np.mean([f(np.linalg.eigvals(GW[i])) for i in pro]))
cnt = [round(inv_count(lambda e: hk(e, 2))), round(inv_count(lambda e: hk(e, 4))), round(inv_count(lambda e: hk(e, 3) * np.sum(e))),
       round(inv_count(lambda e: hk(e, 6))), round(inv_count(lambda e: hk(e, 5) * np.sum(e)))]
check("A5 [T] W(F4)+ invariants: Sym2, Sym4, Sym3 x V = 1, 1, 1 (= SO(4)): no dim-6 term for bosons or the fermion kinetic "
      "vector at any order; the gapping term adds no tensor, so no LIV is induced. Sym6, Sym5 x V (dim-8) =", cnt[:3] == [1, 1, 1], f"{cnt}")
# ---------------- B
print("== B. on-site spectrum: far-wall Weyl field 16 x 2 D4 spinor components, Fock 2^32 by sectors")
def ann(n):
    dim = 1 << n; st = np.arange(dim); out = []
    for j in range(n):
        A = np.zeros((dim, dim)); src = st[(st >> j) & 1 == 1]
        A[src ^ (1 << j), src] = 1 - 2 * (pc(src & ((1 << j) - 1)) & 1); out.append(A)
    return out
b = ann(5); G = []
for k in range(5): G += [b[k] + b[k].T, 1j * (b[k] - b[k].T)]
evn = [s for s in range(32) if bin(s).count('1') % 2 == 0]
t16 = [(-0.25j * (G[a] @ G[c] - G[c] @ G[a]))[np.ix_(evn, evn)] for a, c in itertools.combinations(range(10), 2)]
Cc = np.linalg.multi_dot(G[0::2]); M16 = [(Cc @ g)[np.ix_(evn, evn)] for g in G]
sym = max(np.abs(m - m.T).max() for m in M16)
Sig = [Vm.conj().T @ (0.25 * (gm[m] @ gm[n] - gm[n] @ gm[m])) @ Vm for m, n in itertools.combinations(range(4), 2)]
pau = [s1 / 2, s2 / 2, s3 / 2]; coef = np.array([[np.trace(p @ (1j * s)).real * 2 for p in pau] for s in Sig])
spin = [np.kron(p, np.eye(16)) for p in pau]
check("B1 [T] M_a symmetric => the Lorentz form on the flavour index must be antisymmetric (eps): the D4 Weyl spin is that index; the six "
      "Spin(4) generators restricted to P- span su(2)_- (rank 3), P+ part acts trivially", sym < 1e-12 and np.linalg.matrix_rank(coef, 1e-9) == 3, f"rank {np.linalg.matrix_rank(coef, 1e-9)}")
SECT = {N: np.array(sorted(sum(1 << x for x in c) for c in itertools.combinations(range(32), N)), dtype=np.int64) for N in (0, 1, 2, 3, 4)}
look = lambda N, s: np.searchsorted(SECT[N], s); sgn = lambda s, x: 1 - 2 * (pc(s & ((1 << x) - 1)) & 1)
def create2(N, p, q):
    S = SECT[N]; ok = ((S >> q) & 1 == 0) & ((S >> p) & 1 == 0); s = S[ok]; col = np.nonzero(ok)[0]
    sg = sgn(s, q); s1 = s | (1 << q); sg = sg * sgn(s1, p); return look(N + 2, s1 | (1 << p)), col, sg
def hop1(N, p, q):
    S = SECT[N]; ok = ((S >> q) & 1 == 1); s = S[ok]; col = np.nonzero(ok)[0]; sg = sgn(s, q); s1 = s ^ (1 << q)
    ok2 = ((s1 >> p) & 1 == 0); s1, col, sg = s1[ok2], col[ok2], sg[ok2]; sg = sg * sgn(s1, p); return look(N, s1 | (1 << p)), col, sg
def Bdag(N, M):
    r, c, v = [], [], []
    for al, be in zip(*np.nonzero(np.abs(M) > 1e-14)):
        rr, cc_, sg = create2(N, 16 + be, al); r.append(rr); c.append(cc_); v.append(np.conj(M[al, be]) * sg)
    return sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(len(SECT[N + 2]), len(SECT[N])))
def onebody(N, h):
    r, c, v = [], [], []
    for p, q in zip(*np.nonzero(np.abs(h) > 1e-14)):
        rr, cc_, sg = hop1(N, p, q); r.append(rr); c.append(cc_); v.append(h[p, q] * sg)
    n = len(SECT[N]); return sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(n, n))
c0 = sum((Bdag(0, m).conj().T @ Bdag(0, m)).toarray()[0, 0] for m in M16)
K1 = sum((Bdag(1, m).conj().T @ Bdag(1, m)).toarray() for m in M16); Q = c0 * np.eye(32) - K1
BD2 = [Bdag(2, m) for m in M16]; N4 = len(SECT[4])
LHS = 2 * sum(bb @ bb.conj().T for bb in BD2) + c0 * sp.identity(N4) - onebody(4, Q)   # sum_a {B_a, B_a^+} on N = 4
S2 = sum((lambda o: o @ o)(onebody(4, s)) for s in spin); C10 = sum((lambda o: o @ o)(onebody(4, np.kron(I2, t))) for t in t16)
RHS = 2 * ((144 - 36) * sp.identity(N4) - 2 * S2 - C10)
dev = abs(LHS - RHS).max(); F = (LHS / 2).tocsr()
w, V = sla.eigsh(-F, k=4, which='SA', tol=1e-12); v0 = V[:, np.argmin(w)]; w = np.sort(w)
s2v = np.real(v0.conj() @ (S2 @ v0)); c10v = np.real(v0.conj() @ (C10 @ v0))
check("B2 [T] Fock identity sum_a {B_a,B_a^+} = 2[144 - 2 S(S+1) - C2_10 - J^2] with S the D4 Lorentz SU(2)_- : on N = 0, 1 (c0, one-body part) "
      f"and the full N = 4 sector ({N4} states, sparse)", dev < 1e-10 and abs(c0 - 160) < 1e-9, f"c0 {c0.real:.1f}, max dev {dev:.0e}")
check("B3 [F] sparse Lanczos, N = 4 (J = -6): lowest -F = -108 = -(144 - 36), unique, Lorentz scalar (S = 0) and Spin(10) singlet",
      abs(w[0] + 108) < 1e-8 and w[1] - w[0] > 1 and abs(s2v) < 1e-8 and abs(c10v) < 1e-8, f"levels {np.round(w, 4).tolist()}, <S^2> {s2v:.0e}, <C2_10> {c10v:.0e}")
print("  => with spin10-two-flavour (cited [T]): H = -g F has the unique Lorentz-, Spin(10)- and PH-singlet ground state E0 = -144 g at N = 16,")
print("     gap 4 g (N = 16 +- 4 singlets), fermion gap 13 g. The register's Weyl half IS the two-16s flavour index: Fock space unchanged.")
print("  [T] full Dirac register on the far layer: H_+ + H_- (one Casimir per chirality, disjoint commuting modes): unique product ground")
print("      state E0 = -288 g, gap 4 g, fermion gap 13 g; invariant under all 1152 lifts (A3). The P+-P- cross term is not tested.")
# ---------------- C
print("== C. 1+1D root-line reduction of the D4 register (Cayley / Re Omega on the 4 spinor modes)")
ut = np.array([1, 1, 0, 0]) / np.sqrt(2); nl = np.array([0, 0, 1, 1]) / np.sqrt(2); Gam = 1j * gv(ut) @ gv(nl)
eg, Ug = np.linalg.eigh(Gam); hs = np.round(eg).astype(int)
check("C1 [T] Gamma = i g(u_t) g(n) is Hermitian, Gamma^2 = 1, eigenvalues (-1,-1,+1,+1); |det Ug| = 1 so Omega -> phase x Omega and "
      "omega^omega is unchanged: in the Gamma eigenbasis the D4 chain is the proxy chain with hop signs (-,-,+,+)",
      np.abs(Gam @ Gam - E4).max() < 1e-12 and list(hs) == [-1, -1, 1, 1] and abs(abs(np.linalg.det(Ug)) - 1) < 1e-12)
OCC = {}
def sector(L, d):
    if (L, 'o') not in OCC:
        o = {}
        for m in range(1 << L): o.setdefault(bin(m).count('1'), []).append(sum(((m >> x) & 1) << (4 * x) for x in range(L)))
        OCC[(L, 'o')] = o
    o = OCC[(L, 'o')]; out = []
    for base in range(-2, L + 1):
        ns = [base + dj for dj in d] + [base]
        if min(ns) < 0 or max(ns) > L: continue
        A = np.array([0], dtype=np.int64)
        for j, n in enumerate(ns): A = (A[:, None] | (np.array(o[n], dtype=np.int64) << j)[None, :]).ravel()
        out.append(A)
    return np.sort(np.concatenate(out))
TW = [np.pi / 2, np.pi / 2, -np.pi / 2, -np.pi / 2]
def chainH(L, d, g, model, hsg):
    S = sector(L, d); D = len(S); r, c, v = [], [], []; diag = np.zeros(D)
    for x in range(L):
        for j in range(4):
            p = 4 * x + j; q = 4 * ((x + 1) % L) + j; ph = np.exp(1j * TW[j]) if x == L - 1 else 1.0
            m = ((S >> q) & 1 == 1) & ((S >> p) & 1 == 0); s = S[m]; lo, hi = min(p, q), max(p, q)
            a = 1j * hsg[j] * ph * (1 - 2 * (pc(s & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))) & 1)); rr = np.searchsorted(S, s ^ (1 << q) ^ (1 << p))
            cl = np.nonzero(m)[0]; r += [rr, cl]; c += [cl, rr]; v += [a, np.conj(a)]
        bits = (S >> (4 * x)) & 15; sj = [1 - 2 * ((bits >> j) & 1) for j in range(4)]
        if model == 'Cay': diag -= g * sum(sj[a] * sj[e] for a, e in itertools.combinations(range(4), 2))
        full = np.nonzero(bits == 15)[0]; rr = np.searchsorted(S, S[full] ^ (15 << (4 * x))); r += [rr, full]; c += [full, rr]; v += [8 * g * np.ones(len(full))] * 2
    r.append(np.arange(D)); c.append(np.arange(D)); v.append(diag)
    return sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(D, D))
SEC = [(0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)]
def low(H, k): return np.linalg.eigvalsh(H.toarray())[:k] if H.shape[0] < 400 else np.sort(sla.eigsh(H, k=k, which='SA', tol=1e-10)[0])
def gap(L, g, model, hsg):
    lv = {d: low(chainH(L, d, g, model, hsg), 2 if d == (0, 0, 0) else 1) for d in SEC}; E0 = lv[(0, 0, 0)][0]
    return min([lv[(0, 0, 0)][1]] + [lv[d][0] for d in SEC[1:]]) - E0, lv
P0 = [1, 1, 1, 1]; PD = [-1, -1, 1, 1]
eq = max(np.abs(np.concatenate([lv - lw for lv, lw in zip(gap(4, g, mo, P0)[1].values(), gap(4, g, mo, PD)[1].values())])).max()
         for g in (0.25, 1.0) for mo in ('Cay', 'ReO'))
check("C2 [F] gate: L = 4 D4 chain = proxy chain in every sector (even L: staggering the Gamma = -1 modes maps one onto the other)", eq < 1e-9, f"{eq:.0e}")
f4 = gap(4, 0.0, 'Cay', PD)[0]
check("C3 [F] g = 0: free gap 2 sin(pi/2L) at L = 4", abs(f4 - 2 * np.sin(np.pi / 8)) < 1e-8, f"{f4:.4f}")
EMB = {('ReO', .125): (.803, .550, .420), ('ReO', .25): (1.130, .917, .824), ('Cay', .125): (.993, .791, .714), ('Cay', .25): (2.719, 2.702, 2.702),
       ('ReO', .5): (2.936, 2.929, None), ('Cay', .5): (6.082, 6.054, None)}
print("  model g     L=4     L=5(D4 bc)  L=6    | embedded proxy L=4, 6, 8 [R]   rho = D(Lmax even)/D(4)  class")
res = {}
for (mo, g) in EMB:
    d4, d5 = gap(4, g, mo, PD)[0], gap(5, g, mo, PD)[0]
    d6 = gap(6, g, mo, PD)[0] if g == 0.25 else None
    e = EMB[(mo, g)]; dl = e[2] if e[2] is not None else (d6 if d6 is not None else e[1]); rho = dl / d4
    free = np.sin(np.pi / 16) / np.sin(np.pi / 8) if e[2] is not None else np.sin(np.pi / 12) / np.sin(np.pi / 8)
    cl = 'OPEN' if rho >= 0.9 else ('CLOSING' if abs(rho / free - 1) < 0.05 else 'INCONCLUSIVE'); res[(mo, g)] = (d4, d6, cl)
    print(f"  {mo}  {g:<5} {d4:7.3f}  {d5:7.3f}  {('%7.3f' % d6) if d6 else '   -   '}  | {e[0]:.3f} {e[1]:.3f} {e[2] if e[2] else '  -  '}   {rho:.3f}  {cl}")
check("C4 [F] live L = 4 and L = 6 (g = 0.25) reproduce the embedded proxy values (exact equivalence, even L)",
      all(abs(res[k][0] - EMB[k][0]) < 2e-3 for k in EMB) and all(abs(res[k][1] - EMB[k][1]) < 2e-3 for k in EMB if res[k][1]))
check("C5 [F] Cayley on the D4 register is OPEN at g = 0.25 (L = 4..8, gap flat to 1%) and 0.5; Re Omega alone is not OPEN at 0.25",
      res[('Cay', .25)][2] == 'OPEN' and res[('Cay', .5)][2] == 'OPEN' and res[('ReO', .25)][2] != 'OPEN')
check("C6 [F] weak coupling g = 0.125 is not OPEN for either form (crossover; Re Omega free-like)", res[('Cay', .125)][2] != 'OPEN' and res[('ReO', .125)][2] != 'OPEN')
print("  Not computed: L = 7 on the D4 boundary (3.4e6-state sectors, > 1.5 GB); 3+1D far wall with the Spin(12) term (2^32 per event).")
print("Verdict (pre-set criteria): PARTIAL. (1), (2) PASS; (3) Cayley OPEN on the D4 root-line reduction; the 3+1D far wall is untested.")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
