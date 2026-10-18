#!/usr/bin/env python3
"""C1 check, claims 1-3: determinant lemma, selection rule, decoupling.  Own model (ckmodel, B7-checker core).

D1  lift data: axis-C2 lifts anticommute; U_g^ord for each class (signed-permutation lift vs SU(2) lift).
D2  det(U_g|V) over the little group for EVERY 2-fold level at +-k* and at the six doublers, for the eight-node step AND for
    random symmetric steps/Hamiltonians (range-1, group-averaged); identify the character (A1/A2 of O; restriction at D4).
D3  the two 2-dim irreps met at k* have characters related by A2 (tr_V'(g) = A2(g) tr_V(g)), so det is lift-determined.
S1  general symmetric pairing at Q = R and Q = 0, chi in {A1, A2}: on-site (exact null space) and range-1 (random projected
    samples); node singlets (Q = R) / inter-node blocks (Q = 0).
S2  Q-classification: rotation-invariant Q mod 2pi under the linear parts (Q in {0, R}); dressing argument printed.
S3  decoupling at +-k*: cross blocks node doublet <-> other levels for A2 and A1 channels; BdG node 4-space invariance.
"""
import time
from cklib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(20261018)

# ---------------- D1 ----------------
ax = [find_el(np.diag(d)) for d in ([1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
anti = all(np.allclose(UF[a] @ UF[b], -UF[b] @ UF[a]) for a in ax for b in ax if a != b)
ords = {}
for g in PROPER:
    c = cls(OH[g]); o = {'E': 1, 'C2': 2, "C2'": 2, 'C3': 3, 'C4': 4}[c]
    P = np.linalg.matrix_power(UF[g], o); s = int(round(P[0, 0])) if np.allclose(P, P[0, 0] * np.eye(12)) else None
    ords.setdefault(c, set()).add(s)
print("U_g^{order} = s*1 per class (SU(2) lift would give -1 for C2, C2', C4^4 and C3^3 = -1 for the 2pi-rotation):", ords)
check("D1 the three axis-C2 lifts anticommute (non-trivial projective class: no 1-dim levels at +-k* or at the D4 doublers)", anti)

# ---------------- D2: det characters ----------------
def det_char(Qm, idx): return {g: np.linalg.det(Qm.conj().T @ UF[g] @ Qm) for g in idx}
def name_char(dc, idx):
    if all(abs(dc[g] - 1) < 1e-7 for g in idx): return 'A1'
    if all(abs(dc[g] - A2[g]) < 1e-7 for g in idx): return 'A2'
    return 'other'
def rand_sym_herm(r=1):
    bl = sym_blocks({d: rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)) for d in itertools.product(range(-r, r + 1), repeat=3)})
    out = {}
    for d, h in bl.items(): add(out, d, 0.5 * h); add(out, neg(d), 0.5 * h.conj().T)
    return out
from scipy.linalg import expm
H1, H2, H3 = rand_sym_herm(), rand_sym_herm(), rand_sym_herm()
def W_rand_step(k): return expm(-1j * bloch(H1, k)[0]) @ W(k) @ expm(-1j * 0.7 * bloch(H2, k)[0])
def W_rand_ham(k): return expm(-1j * 0.3 * bloch(H3, k)[0])          # a Hamiltonian's levels = levels of a small-time exp
def W_prod(k): return expm(-1j * bloch(H1, k)[0]) @ expm(-1j * bloch(H2, k)[0])
UHv = PH[0] + 1j * PH[1] - PH[2]; ULv = PL[0] - PL[1] + 1j * PL[2] - 1j * PL[3]
def W_var(k): return bloch(blS, k)[0] @ bloch(blL, k)[0] @ UHv @ ULv
STEPS = dict(eight_node=W, rand_step=W_rand_step, rand_ham=W_rand_ham, rand_prod=W_prod, phase_variant=W_var)
for nmS, Wf in STEPS.items():
    ksym = all(np.allclose(UF[g] @ Wf(k) @ UF[g].T, Wf(gk(g, k)), atol=1e-9) for g in PROPER[::5] for k in rng.uniform(-np.pi, np.pi, (2, 3)))
    assert ksym, nmS
res = {}
for nmS, Wf in STEPS.items():
    cnt = {'kstar': [], 'doub': []}
    for n, K in NODES.items():
        st = stab(K)
        for E, Qm in levels(K, Wf):
            if Qm.shape[1] != 2: continue
            dc = det_char(Qm, st)
            if n in ((0, 0, 0), (1, 1, 1)):
                cnt['kstar'].append(name_char(dc, st))
            else:
                # compare with restrictions of A1, A2 to the D4 little group
                r2 = all(abs(dc[g] - A2[g]) < 1e-7 for g in st); r1 = all(abs(dc[g] - 1) < 1e-7 for g in st)
                cnt['doub'].append('A2|D4' if r2 else ('A1|D4' if r1 else 'other'))
    res[nmS] = cnt
    print(f"   {nmS:14s}: +-k* 2-fold levels det = {sorted(set(cnt['kstar']))} (n={len(cnt['kstar'])}); "
          f"doubler 2-fold levels det = {sorted(set(cnt['doub']))} (n={len(cnt['doub'])})")
ok = all(set(c['kstar']) == {'A2'} and set(c['doub']) == {'A2|D4'} and len(c['doub']) > 0 for c in res.values())
check("D2 det(U_g|V) = A2 for every 2-fold level at +-k* and = A2|D4 at every doubler level, for the eight-node step and four other "
      "PSG-symmetric steps/Hamiltonians", ok, "; ".join(f"{k}: {len(v['kstar'])}+{len(v['doub'])}" for k, v in res.items()))
# A2|D4 is the B1 character of D4 and differs from A1|D4
st = stab(NODES[(1, 0, 0)]); axis = None
lab = {}
for g in st:
    M = OH[g]; c = cls(M)
    lab[g] = c
b1_like = all((A2[g] == -1) == (cls(OH[g]) in ('C4', "C2'")) for g in st)
nC4 = sum(cls(OH[g]) == 'C4' for g in st); nC2p = sum(cls(OH[g]) == "C2'" for g in st); nC2 = sum(cls(OH[g]) == 'C2' for g in st)
check("D2b doubler little group (affine) is D4: 2 C4, 3 axis C2 (one along the C4 axis), 2 diagonal C2'; A2|D4 = (C4:-1, C2:+1, C2':-1) = B1 "
      "(axis-C2' convention) != A1|D4", len(st) == 8 and nC4 == 2 and nC2 == 3 and nC2p == 2 and b1_like)

# ---------------- D3: the two 2-dim irreps at k* ----------------
tr = []
for E, Qm in levels(KST):
    if Qm.shape[1] == 2: tr.append((E, {g: np.trace(Qm.conj().T @ UF[g] @ Qm) for g in PROPER}))
rel = all(abs(tr[1][1][g] - A2[g] * tr[0][1][g]) < 1e-7 for g in PROPER)
dist = any(abs(tr[1][1][g] - tr[0][1][g]) > 1e-3 for g in PROPER)
print("   k* doublets: E =", [round(e, 4) for e, _ in tr], " tr(C4) =", [np.round(t[[g for g in PROPER if cls(OH[g]) == 'C4'][0]], 4) for _, t in tr])
check("D3 at k* the two 2-fold levels are DIFFERENT 2-dim irreps whose characters differ exactly by A2 (E1/2 vs E5/2 = E1/2 x A2), "
      "hence equal det (A2^2 = 1): the det is a property of the lift, not of the level", rel and dist)

# ---------------- S2: Q classification ----------------
cand = [np.pi * np.array(p) for p in itertools.product((0, 1), repeat=3)] + [np.pi / 2 * np.array(p) for p in itertools.product((-1, 0, 1, 2), repeat=3)]
inv = []
for Q in cand:
    if all(same_k(OH[g] @ Q, Q) for g in PROPER): inv.append(tuple(np.round(wrap(Q) / np.pi, 3)))
inv = sorted(set(inv))
check("S2 among Q in (pi/2)Z^3, only Q = 0 and Q = R = pi(1,1,1) are fixed mod 2pi by the 24 linear parts (pair momentum: the affine "
      "shifts pi M lam cancel in 2*theta); with U(1)-dressing T_e e^{i alpha.e N} one condensate momentum is still required", inv == [(-1.0, -1.0, -1.0), (0.0, 0.0, 0.0)] or inv == [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)], str(inv))
# general: (M - 1) Q in 2pi Z^3 for C4z, C4x  ->  Q in {0, pi}^3 with all equal -- analytic, printed only
print("   analytic: C4z gives Q_x = -Q_y, Q_y = Q_x mod 2pi -> Q_x = Q_y in {0,pi}; with C4x, Q_y = Q_z: Q in {0, R}")

# ---------------- S1: selection rule ----------------
DQ = {n: node_doublet(n) for n in NODES}
VA2, VA1 = onsite_channel(A2), onsite_channel(A1)
print(f"   on-site antisymmetric channels: dim V_A2 = {len(VA2)}, dim V_A1 = {len(VA1)}")
def node_m(bl, Q):
    out = {}
    for n, K in NODES.items():
        Dk = Delta(bl, Q, K)[0]; Da = Dk - Delta(bl, Q, -Q - K)[0].T
        if np.allclose(Q, 0):
            nm = tuple((1 - x) % 2 for x in n)               # -K = k* + pi((1,1,1)-n) since -k* = k* + R
            out[n] = np.abs(DQ[n].conj().T @ Da @ DQ[nm].conj()).max()
        else:
            out[n] = abs(singlet(DQ[n], Da))
    return out
summ = {}
for Qn, Q in (('R', QR), ('0', Q0)):
    for cn, chi in (('A2', A2), ('A1', A1)):
        vals = []; symok = True
        for trial in range(3):
            bl = sym_pair(rand_blocks(rng, 1), chi, Q); symok &= check_sym(bl, chi, Q, rng=rng); vals.append(node_m(bl, Q))
        for X in (VA2 if cn == 'A2' else VA1):
            bl = {(0, 0, 0): (X + 0j)}
            if np.allclose(Q, 0) or True: vals.append(node_m(bl, Q))
        mn = {n: min(v[n] for v in vals[:3]) for n in NODES}; mxall = {n: max(v[n] for v in vals) for n in NODES}
        summ[(Qn, cn)] = (symok, mn, mxall)
        print(f"   Q={Qn} chi={cn}: sym+Fermi ok={symok}; range-1 min over 3 samples: "
              + ", ".join(f"{NAME[n]}:{mn[n]:.2e}" for n in NODES) + f"; max over all (incl. on-site basis): {max(mxall.values()):.2e}")
okR = summ[('R', 'A2')][0] and min(summ[('R', 'A2')][1].values()) > 1e-3 and max(summ[('R', 'A1')][2].values()) < 1e-10 and summ[('R', 'A1')][0]
check("S1a Q = R: chi = A2 gives a nonzero intra-node singlet at all eight nodes (range-1 random), chi = A1 gives exactly zero at all eight "
      "(range-1 random and the whole on-site basis): all-or-nothing", okR)
ok0 = summ[('0', 'A1')][0] and summ[('0', 'A2')][0]
print("   Q=0 inter-node blocks: A1 min", f"{min(summ[('0','A1')][1].values()):.2e}", " A2 max", f"{max(summ[('0','A2')][2].values()):.2e}")
check("S1b Q = 0: symmetric pairings exist (range-1, both characters); inter-node K<->-K blocks are generic for A1 and vanish for A2 "
      "(reported; gappability decided by BdG charge in chk3)", ok0 and min(summ[('0', 'A1')][1].values()) > 1e-3)
# selection rule restated per node: allowed iff chi|stab = det|stab
rule_ok = True
for n, K in NODES.items():
    st = stab(K); dc = det_char(DQ[n], st)
    for cn, chi in (('A2', A2), ('A1', A1)):
        allowed = all(abs(chi[g] - dc[g]) < 1e-7 for g in st)
        obs = summ[('R', cn)][1][n] > 1e-3
        rule_ok &= (allowed == obs)
check("S1c node-by-node: singlet observed nonzero <=> chi|G_K = det_K (all eight nodes, both characters)", rule_ok)

# ---------------- S3: decoupling at +-k* ----------------
cross = {}
for cn, chi in (('A2', A2), ('A1', A1)):
    worst = 0.0; worst_other = {}
    bls = [sym_pair(rand_blocks(rng, 1), chi, QR) for _ in range(2)] + [{(0, 0, 0): X + 0j} for X in (VA2 if cn == 'A2' else VA1)]
    for n in ((0, 0, 0), (1, 1, 1)):
        K = NODES[n]
        for bl in bls:
            Da = Delta(bl, QR, K)[0] - Delta(bl, QR, -QR - K)[0].T
            for E, Qm in levels(K):
                if abs(wrap(E - np.pi / 2)) < 1e-6: continue
                v = np.abs(DQ[n].conj().T @ Da @ Qm.conj()).max()
                worst = max(worst, v); key = f"E={E:+.3f},dim{Qm.shape[1]}"; worst_other[key] = max(worst_other.get(key, 0), v)
    cross[cn] = (worst, worst_other)
    print(f"   chi={cn}: node(+pi/2) doublet <-> other levels at +-k*, max |block|: " + ", ".join(f"{k}:{v:.1e}" for k, v in worst_other.items()))
check("S3a at +-k* an A2 pairing (on-site or range-1) couples the node doublet to no other level (exact zero blocks); an A1 pairing does "
      "couple it, to the other 2-dim irrep only (not to G3/2)", cross['A2'][0] < 1e-10 and
      max(v for k, v in cross['A1'][1].items() if 'dim2' in k) > 1e-3 and max(v for k, v in cross['A1'][1].items() if 'dim4' in k) < 1e-10)
# BdG: the 4-dim node subspace at k* is exactly invariant under U_BdG(k*) for an A2 pairing, at large tau
bl = sym_pair(rand_blocks(rng, 1), A2, QR); Df = lambda ks, bl=bl: Delta(bl, QR, ks)
inv_ok = True
for n in ((0, 0, 0), (1, 1, 1)):
    K = NODES[n]; Ub = bdg_U(K, Df, 1.3, QR)[0]
    P = np.zeros((24, 4), complex); P[:12, :2] = DQ[n]; P[12:, 2:] = DQ[n].conj()
    Pr = P @ P.conj().T
    inv_ok &= np.allclose(Pr @ Ub @ Pr, Ub @ Pr, atol=1e-10)
    blk = P.conj().T @ Ub @ P; ev = np.angle(np.linalg.eigvals(blk)); mK = abs(singlet(DQ[n], Delta(bl, QR, K)[0] - Delta(bl, QR, -QR - K)[0].T))
    print(f"   {NAME[n]}: node 4-block eigenphases {np.round(np.sort(ev), 5)}, |m_K|={mK:.4f}")
check("S3b the particle+hole node 4-space at +-k* is invariant under the full BdG step (tau = 1.3, range-1 A2 pairing): exact decoupling "
      "at all orders, so +-k* is gapless iff m_K = 0", inv_ok)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
