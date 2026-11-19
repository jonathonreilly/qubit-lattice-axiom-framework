#!/usr/bin/env python3
"""higgs-10-126: is the 126 channel of 16 x 16 = 10 + 120 + 126 forced (with a fixed ratio) by the forced far-wall
term -(g/2) sum_a {B_a, B_a^+} (spin10-two-flavour), and does 10 + 126 give a non-fitted mass relation?
 A  channel algebra on two 16s: 3 number-conserving invariant quartics, all Casimir functions; the forced term has no
    126 coefficient (pair basis) and equals a repulsive, equal 126 + 120 term at fixed N; charge-4: one invariant (10).
 B  levels of the 126 and 120 pair composites (exact, Casimir formula); ground-state pair counts.
 C  the Clebsch -3 of the 126 doublet relative to the 10 doublet (explicit oscillator 16).
 D  Babu-Mohapatra sum rules (supplied form): family-local CKM, parameter vs observable rank, pure-channel ratios.
Labels: [T] exact, [F] finite diagnostic, [E] estimate against measurement (supplied numbers).
Supplied: the 16 with one orbital per weight, the two-valued flavour (spin), the SM embedding used to READ quantum
numbers, the Babu-Mohapatra mass-matrix form, GUT-scale SM running masses (Xing-Zhang-Zhou 2008, mu = 2e16 GeV)."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

def ann(n):
    dim = 1 << n; st = np.arange(dim); out = []
    for j in range(n):
        A = np.zeros((dim, dim)); src = st[(st >> j) & 1 == 1]
        A[src ^ (1 << j), src] = 1 - 2 * (np.bitwise_count(src & ((1 << j) - 1)).astype(np.int64) & 1)
        out.append(A)
    return out

b5 = ann(5); G = []
for k in range(5): G += [b5[k] + b5[k].T, 1j * (b5[k] - b5[k].T)]
ev = [s for s in range(32) if bin(s).count('1') % 2 == 0]
ix = np.ix_(ev, ev)
t16 = [(-0.25j * (G[a] @ G[c] - G[c] @ G[a]))[ix] for a, c in itertools.combinations(range(10), 2)]
for C in (np.linalg.multi_dot(G[0::2]), np.linalg.multi_dot(G[1::2])):
    if all(np.abs((C @ g)[ix]).max() > 0.5 for g in G): break
form = lambda p: np.array([(C @ np.linalg.multi_dot([G[i] for i in I]))[ix] if p > 1 else (C @ G[I[0]])[ix]
                           for I in itertools.combinations(range(10), p)])
K1, K3, K5 = form(1), form(3), form(5)
def span(Ks):
    U, s, _ = np.linalg.svd(Ks.reshape(len(Ks), -1).T, full_matrices=False); r = int((s > 1e-9 * s[0]).sum())
    return U[:, :r].T.reshape(r, 16, 16)
S10, S120, S126 = span(K1), span(K3), span(K5)
sym = lambda K: np.abs(K - np.swapaxes(K, 1, 2)).max(); asym = lambda K: np.abs(K + np.swapaxes(K, 1, 2)).max()
allsym = span(np.concatenate([S10, S126]))

# ------------------------------------------------------------------ A
print("== A. invariant four-fermion terms on two 16s (modes (f,i), f = 1,2 flavour = spin, i in 16)")
check("A1 [T] C Gamma^(1), C Gamma^(3), C Gamma^(5) on the 16 span the 10, 120, 126 (ranks 10, 120, 126); (1),(5) symmetric, "
      "(3) antisymmetric; Sym^2 16 = 10 + 126 and Lambda^2 16 = 120 exactly",
      (len(S10), len(S120), len(S126), len(allsym)) == (10, 120, 126, 136) and max(sym(K1), sym(K5), asym(K3)) < 1e-12,
      f"ranks {len(S10)}, {len(S120)}, {len(S126)}; 10+126 span {len(allsym)} = 16*17/2")
eps = np.array([[0, 1], [-1, 0]]); sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.])]
sf = [s @ eps for s in sig]                                                     # flavour-symmetric pair matrices
# work in the 496-dim antisymmetric pair space: basis E_mn = (e_m e_n^T - e_n e_m^T)/sqrt2, m < n
iu = np.triu_indices(32, 1); EB = np.zeros((496, 32, 32)); EB[np.arange(496), iu[0], iu[1]] = 2 ** -0.5
EB[np.arange(496), iu[1], iu[0]] = -2 ** -0.5
coord = lambda As: np.einsum('nij,kij->kn', EB, As)                              # Frobenius coordinates
def proj(As):
    Q, _ = np.linalg.qr(coord(As).T); return Q @ Q.conj().T, Q.shape[1]
P10, d10 = proj(np.array([np.kron(eps, K) for K in S10])); P126, d126 = proj(np.array([np.kron(eps, K) for K in S126]))
P120, d120 = proj(np.array([np.kron(f, K) for K in S120 for f in sf]))
T32 = [np.kron(np.eye(2), t) for t in t16]; s32 = [np.kron(s / 2, np.eye(16)) for s in sig]
c1 = sum(t @ t for t in T32)
def two(gens):                                     # sum_g g x g on pairs: A -> g A g^T, in the 496 basis
    Y = sum(g @ EB @ g.T for g in gens); return np.einsum('mij,nij->mn', EB, Y)
C2two = 2 * two(T32); S2two = 2 * two(s32); I496 = np.eye(496)
# on a pair: C2_10 = 2*45/4 + 2 T1.T2, S^2 = 2*3/4 + 2 s1.s2
cas = {}
for nm, P in (('10', P10), ('126', P126), ('120', P120)):
    cas[nm] = (np.real(np.trace(P @ (22.5 * I496 + C2two))) / np.real(np.trace(P)),
               np.real(np.trace(P @ (1.5 * I496 + S2two))) / np.real(np.trace(P)))
ok = np.abs(P10 + P126 + P120 - I496).max() < 1e-10 and (d10, d126, d120) == (10, 126, 360)
ok &= np.abs(c1 - 45 / 4 * np.eye(32)).max() < 1e-12
ok &= all(abs(cas[k][0] - v) < 1e-9 for k, v in (('10', 9), ('126', 25), ('120', 21)))
ok &= all(abs(cas[k][1] - v) < 1e-9 for k, v in (('10', 0), ('126', 0), ('120', 2)))
check("A2 [T] Lambda^2(16 x 2) = (10,S=0) + (126,S=0) + (120,S=1), dims 10 + 126 + 360 = 496, multiplicity-free "
      "(C2_10 = 9, 25, 21): exactly THREE independent number-conserving Spin(10) x SU(2) invariant quartics", ok,
      ", ".join(f"{k}: C2 {v[0]:.0f}, S(S+1) {v[1]:.0f}" for k, v in cas.items()))
X = lambda a, b, c: a * C2two + b * S2two + c * I496
e10 = np.abs(X(-1 / 16, -1 / 8, -1 / 32) - P10).max(); e126 = np.abs(X(1 / 16, -3 / 8, 9 / 32) - P126).max()
Nn, Ss, C2, Jj = sp.symbols('N S2 C2 J')
Q10 = -Fr(1, 16) * (C2 - Fr(45, 4) * Nn) - Fr(1, 8) * (Ss - Fr(3, 4) * Nn) - Fr(1, 32) * Nn * (Nn - 1) / 2
Q126 = Fr(1, 16) * (C2 - Fr(45, 4) * Nn) - Fr(3, 8) * (Ss - Fr(3, 4) * Nn) + Fr(9, 32) * Nn * (Nn - 1) / 2
Q120 = Nn * (Nn - 1) / 2 - Q10 - Q126
gram = np.array([[np.trace(a @ b.conj().T) for b in K1] for a in K1])
ident = sp.expand(2 * 16 * Q10 - 10 * (Nn - 16) - 2 * (144 - 2 * Ss - C2 - (Nn - 16) ** 2 / 4)) == 0
check("A3 [T] every invariant quartic is a Casimir function (496 x 496 operator identities): Q_10 = -(C2-45N/4)/16 "
      "- (S^2-3N/4)/8 - N(N-1)/64, Q_126 = (C2-45N/4)/16 - 3(S^2-3N/4)/8 + 9N(N-1)/64, Q_120 = N(N-1)/2 - Q_10 - Q_126; "
      "with Tr M_a M_b^+ = 16 delta_ab, 2*16 Q_10 - 20 J is the spin10-two-flavour identity 2[144-2S(S+1)-C2-J^2]",
      max(e10, e126) < 1e-10 and np.abs(gram - 16 * np.eye(10)).max() < 1e-10 and ident, f"errors {e10:.0e}, {e126:.0e}")
# forced term in the pair basis: H = -g*16*Q_10 + one-body; coefficients on (Q_10, Q_126, Q_120) are (-16g, 0, 0)
# at fixed N: Q_10 = N(N-1)/2 - Q_126 - Q_120, so H = +16 g (Q_126 + Q_120) + f(N)
diff = sp.simplify(-16 * Q10 - (16 * (Q126 + Q120) - 16 * Nn * (Nn - 1) / 2))
check("A4 [T] the forced term has ZERO 126 coefficient in the pair basis; at fixed N it is +16 g (Q_126 + Q_120) + f(N): "
      "126 and 120 enter with EQUAL repulsive weight. The 126-120 splitting is a free invariant the rules do not set "
      "(set to 0 by the forced term): no attractive 126 channel and no fixed Y126/Y10", diff == 0, "g_126 = g_120 exactly")
# charge-4 invariants: Z4 centre forbids Delta N = 2; Delta N = 4 tensors
psi = rng.normal(size=(50, 16)) + 1j * rng.normal(size=(50, 16))
pure = max(abs(sum((p @ M @ p) ** 2 for M in K1)) for p in psi) / max(abs(p @ p) ** 2 for p in psi)
def asym4(T):
    out = np.zeros_like(T)
    for perm in itertools.permutations(range(4)):
        out += np.linalg.det(np.eye(4)[list(perm)]) * T.transpose(perm)
    return out / 24
O = []
for A in (np.array([np.kron(eps, K) for K in K1]), np.array([np.kron(f, K) for K in K3 for f in sf]),
          np.array([np.kron(eps, K) for K in K5])):
    O.append(asym4(np.einsum('kij,kln->ijln', A, A))); del A
n0 = [np.linalg.norm(o) for o in O]; O.pop()
inv = 0.
for _ in range(3):
    Xg = sum(rng.normal() * x for x in T32 + s32)
    for Om in O:
        d = np.zeros_like(Om)
        for sl in range(4): d += np.moveaxis(np.tensordot(Xg.T, Om, axes=([1], [sl])), 0, sl)
        inv = max(inv, np.abs(d).max() / np.abs(Om).max()); del d
rk = np.linalg.matrix_rank(np.array([O[0].ravel(), O[1].ravel()]), tol=1e-8 * n0[0])
del O
check("A5 [T] charge-changing terms: the Z4 centre (16 -> i 16) forbids Delta N = +-2; Delta N = 4 has ONE invariant, the "
      "10-channel Omega: (psi Gamma psi)^2 = 0 for commuting psi (no Sym^4 singlet), the 126 square vanishes, the 120 square "
      "is proportional to the 10 one", pure < 1e-12 and n0[2] < 1e-9 * n0[0] and rk == 1 and inv < 1e-10,
      f"(psiGpsi)^2 {pure:.0e}, |O126|/|O10| {n0[2]/n0[0]:.0e}, rank[O10,O120] {rk}, invariance {inv:.0e}")

# ------------------------------------------------------------------ B
print("== B. levels and ground-state pair content (H = -g F, F = 144 - 2S(S+1) - C2_10 - J^2)")
F = lambda S2, c2, J: 144 - 2 * S2 - c2 - J * J
lev = {'10': 144 - F(0, 9, 1), '126': 144 - F(0, 25, 1), '120': 144 - F(2, 21, 1)}
gsq = {k: q.subs({Nn: 16, Ss: 0, C2: 0}) for k, q in (('10', Q10), ('126', Q126), ('120', Q120))}
check("B1 [T] pair composites B_r^+|GS> (good quantum numbers S, C2_10, J, so exact eigenstates when nonzero): 10 at 10 g, "
      "126 AND 120 both at 26 g; nonzero because the ground-state pair counts are Q_10 : Q_126 : Q_120 = 9 : 27 : 84 "
      "(sum 120 = 16*15/2) and sum [B_r, B_r^+] is proportional to J = 0 (Schur on the irreducible 32)",
      lev == {'10': 10, '126': 26, '120': 26} and gsq == {'10': 9, '126': 27, '120': 84},
      f"levels {lev}; pair counts {gsq}")

# ------------------------------------------------------------------ C
print("== C. Clebsch of the colour-singlet neutral doublet in the 10 and in the 126")
W = [np.array([0.5 - ((s >> k) & 1) for k in range(5)]) for s in ev]
def name(w):
    cp = int(sum(w[:3] > 0)); wk = tuple(int(x > 0) for x in w[3:])
    if cp == 3: return 'nu^c' if wk == (1, 1) else 'e^c'
    if cp == 2: return 'u' if wk == (1, 0) else 'd'
    if cp == 1: return 'u^c' if wk == (1, 1) else 'd^c'
    return 'nu' if wk == (1, 0) else 'e'
nm = [name(w) for w in W]
E = [(b5[k].T @ b5[l])[ix] for k in range(3) for l in range(3) if k != l] + \
    [(b5[k].T @ b5[k] - b5[k + 1].T @ b5[k + 1])[ix] for k in range(2)]
def doublet(Sp, Yt):
    """colour-singlet subspace of the channel span Sp at the neutral-doublet weight of hypercharge Yt"""
    out = None
    for w0 in {tuple(W[i] + W[j]) for i in range(16) for j in range(16)}:
        w0 = np.array(w0)
        if any(w0[:3]) or w0[3] - w0[4] == 0: continue
        Yw = Fr(round(6 * (sum(w0[:3]) / 3 - sum(w0[3:]) / 2)), 6); T3 = Fr(int(w0[3] - w0[4]), 2)
        if Yw != Yt or Yw + T3 != 0: continue
        mask = np.array([[np.allclose(W[i] + W[j], w0) for j in range(16)] for i in range(16)])
        Ws = span(np.array([K * mask for K in Sp]))
        L = np.array([np.concatenate([(e.T @ K + K @ e).ravel() for e in E]) for K in Ws]).T
        _, s, Vh = np.linalg.svd(L, full_matrices=False); null = Vh[int((s > 1e-9).sum()):].conj()
        out = (len(Ws), [np.tensordot(v, Ws, axes=1) for v in null])
    return out
def ratio(K, a, b):
    va = [K[i, j] for i in range(16) for j in range(16) if {nm[i], nm[j]} == set(a) and abs(K[i, j]) > 1e-9]
    vb = [K[i, j] for i in range(16) for j in range(16) if {nm[i], nm[j]} == set(b) and abs(K[i, j]) > 1e-9]
    return np.array(vb) / va[0], len(va)
res = {}
for Yt, a, b in ((Fr(1, 2), ('d', 'd^c'), ('e', 'e^c')), (Fr(-1, 2), ('u', 'u^c'), ('nu', 'nu^c'))):
    for lab, Sp in (('10', S10), ('126', S126)):
        mult, Ks = doublet(Sp, Yt); r, nq = ratio(Ks[0], a, b); qa, _ = ratio(Ks[0], a, a)
        res[(lab, Yt)] = (mult, len(Ks), r[0], np.ptp(np.abs(qa)), nq)
rr = [res[('126', y)][2] / res[('10', y)][2] for y in (Fr(1, 2), Fr(-1, 2))]
check("C1 [T] the 126 holds exactly ONE colour-singlet neutral doublet direction per hypercharge (weight multiplicity "
      "3, colour-singlet 1); relative to the 10, its (e,e^c):(d,d^c) and (nu,nu^c):(u,u^c) entries carry the factor -3, "
      "equal over the 3 colours", all(res[k][1] == 1 for k in res) and all(abs(x + 3) < 1e-9 for x in rr)
      and all(res[k][3] < 1e-9 and res[k][4] == 6 for k in res),
      f"126 weight mult {res[('126', Fr(1, 2))][0]}, ratio-of-ratios H_d {rr[0].real:+.3f}, H_u {rr[1].real:+.3f}")

# ------------------------------------------------------------------ D
print("== D. Babu-Mohapatra sum rules (supplied form): M_d = H + F, M_e = H - 3F, M_u = r(H + sF), M_nuD = r(H - 3sF)")
def ckm(Mu, Md):
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    return Uu[:, np.argsort(su)].conj().T @ Ud[:, np.argsort(sd)], np.sort(su), np.sort(sd)
err = 0
for _ in range(200):
    h, f = rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3); r, s = rng.normal(), rng.normal() + 1j * rng.normal()
    V, _, _ = ckm(np.diag(r * (h + s * f)), np.diag(h + f)); P = np.abs(V)
    err = max(err, np.sort(P, axis=1)[:, :2].max(), np.abs(P.max(axis=1) - 1).max())
check("D1 [T] family-local 10 + 126 (each family's mirror carries its own channels, any couplings and VEVs): M_u, M_d both "
      "diagonal, |V_CKM| a permutation: adding the 126 does NOT produce mixing without family-off-diagonal channels",
      err < 1e-10, f"max off-permutation {err:.0e}")
def obs(p, real):
    h = p[:3]
    if real: Fm = np.zeros((3, 3)); Fm[np.triu_indices(3)] = p[3:9]; r, s = p[9], p[10]
    else:
        Fm = np.zeros((3, 3), complex); Fm[np.triu_indices(3)] = p[3:9] + 1j * p[9:15]; r, s = p[15], p[16] + 1j * p[17]
    Fm = Fm + np.triu(Fm, 1).T; H = np.diag(h)
    Md, Me, Mu = H + Fm, H - 3 * Fm, r * (H + s * Fm)
    V, su, sd = ckm(Mu, Md); se = np.sort(np.linalg.svd(Me, compute_uv=False))
    Jcp = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
    return np.concatenate([su, sd, se, [abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), Jcp]])
def jrank(n, real):
    p = rng.normal(size=n); Jm = np.array([(obs(p + 1e-6 * e, real) - obs(p - 1e-6 * e, real)) / 2e-6 for e in np.eye(n)]).T
    s = np.linalg.svd(Jm, compute_uv=False); return int((s > 1e-6 * s[0]).sum()), s[-1] / s[0]
rk_c = [jrank(18, False)[0] for _ in range(5)]; rk_r = [jrank(11, True)[0] for _ in range(5)]
check("D2 [F] generic complex 10 + 126 (H real diagonal 3, F complex symmetric 12, r 1, s 2 = 18 real): Jacobian of the 13 "
      "charged observables (9 masses, 3 CKM moduli, J_CP) has full rank 13 at seeded points: NO charged-sector relation",
      all(x == 13 for x in rk_c), f"ranks {rk_c}")
check("D3 [F] real (CP-conserving) couplings: 11 parameters, rank 11 < 13: two relations would exist (J_CP = 0 is one), "
      "but the rules do not force real couplings or any value of Y10, Y126, r, s (the forced term has <B> = 0: no VEV at all)",
      all(x == 11 for x in rk_r), f"ranks {rk_r}")
md, ms, mb = 1.14e-3, 21.7e-3, 1.00; me, mm, mtau = 0.4696e-3, 99.14e-3, 1.6853
q = [me / md, mm / ms, mtau / mb]
print(f"   [E] GUT-scale (SM, 2e16 GeV, supplied) m_e/m_d, m_mu/m_s, m_tau/m_b = {q[0]:.2f}, {q[1]:.2f}, {q[2]:.2f}; "
      f"pure 10 -> 1, pure 126 -> 3; Georgi-Jarlskog texture (1/3, 3, 1, supplied) deviates by "
      f"{abs(q[0]*3-1)*100:.0f}%, {abs(q[1]/3-1)*100:.0f}%, {abs(q[2]-1)*100:.0f}%")
check("D4 [E] per-family pure-channel relations m_e/m_d in {1, 3}: no family is single-channel (each ratio > 25% from both); "
      "with two channels per family (h_i, f_i) any pair (m_d, m_e) fits, so no family-blind test of the Clebsch remains",
      all(min(abs(x - 1), abs(x / 3 - 1)) > 0.25 for x in q),
      ", ".join(f"{x:.2f}" for x in q))
print("   verdict: 126 not forced (free invariant; equal-repulsive with 120 in the forced term); Y126/Y10, r, s not fixed; "
      "no non-fitted mass relation: UNTESTED")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time()-T0:.1f} s)")
