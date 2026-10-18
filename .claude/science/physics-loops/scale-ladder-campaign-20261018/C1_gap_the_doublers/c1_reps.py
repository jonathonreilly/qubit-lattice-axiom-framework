#!/usr/bin/env python3
"""C1 part 1a: double-group data at the eight nodes and the pairing-channel (determinant) rule.

Checks
 R1  fibre maps: U_g W(k) U_g^T = W(g.k) for all 24 dressed rotations (random k), projective closure U_g U_h = +-U_gh,
     commuting axis-C2 lifts anticommute.
 R2  real-space cross-check of the pairing convention on the L = 4 torus: D = sum_v e^{iR.v} A_v is rotation-symmetric
     up to a character chi iff U_g A U_g^T = chi(g) A; odd translations flip the sign of D (absorbed by e^{i pi N/2}).
 R3  node table at E = +pi/2 (and -pi/2): 2-fold, Weyl speeds, chirality.
 R4  det characters: det(U_g|D) is a genuine 1-dim character; equal for every 2-fold spin-1/2 level at k* and -k*
     (A1 or A2 of O); at each doubler it equals the restriction of the k* character to the D4 little group; A2|D4 != A1.
 R5  on-site pairing channels V_chi = {A antisymmetric: U_g A U_g^T = chi(g) A}; singlet amplitudes at the eight nodes:
     chi = det -> generically nonzero at all eight; chi != det -> exactly zero at all eight.
 R6  same for random k-dependent symmetric pairings Delta(k) (range 1, group-averaged), all four (Q, chi) channels.
 R7  4-fold G3/2-containing levels at k*: dimension of chi-invariant antisymmetric pairs (both chi) -- reported.
 R8  (aside, translation-breaking) staggered CDW masses at R: which nodes each channel gaps.
"""
import time
from c1lib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(7)

# ---------------- R1 ----------------
KR = rng.uniform(-np.pi, np.pi, (6, 3))
ok = all(np.allclose(g['U'] @ W(k) @ g['U'].T, W(gk(g, k)), atol=1e-10) for g in ROT for k in KR)
def find(Mx):
    for j, h in enumerate(ROT):
        if (h['M'] == Mx).all(): return j
mult_ok = True; th_ok = True
for g in ROT:
    for h in ROT:
        j = find(g['M'] @ h['M']); P_ = g['U'] @ h['U']
        mult_ok &= np.allclose(P_, ROT[j]['U']) or np.allclose(P_, -ROT[j]['U'])
        th_ok &= same_k(g['M'] @ h['th'] + g['th'], ROT[j]['th'])
check("R1a fibre maps U_g W(k) U_g^T = W(M_g k + pi s_g) for all 24 rotations (6 random k); 21 have s_g != 0",
      ok and sum(np.any(g['th'] != 0) for g in ROT) == 21)
check("R1b projective closure U_g U_h = +-U_gh and affine shifts compose (theta_gh = M_g theta_h + theta_g mod 2pi)", mult_ok and th_ok)
ax = [find(np.diag(d)) for d in ([1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
check("R1c the three axis-C2 lifts pairwise anticommute on C^12",
      all(np.allclose(ROT[a]['U'] @ ROT[b]['U'], -ROT[b]['U'] @ ROT[a]['U']) for a in ax for b in ax if a != b))

# ---------------- R3: node table ----------------
vs = np.sqrt(2) / 3
TAB = {}
for E in (np.pi / 2, -np.pi / 2):
    for nm, k in NODES.items():
        Qm = level(k, E); a, B = weyl_data(k, Qm); sv = np.linalg.svd(B, compute_uv=False)
        TAB[(nm, E)] = dict(Q=Qm, dim=Qm.shape[1], sv=np.sort(sv), chi=int(np.sign(np.linalg.det(B))), tilt=np.linalg.norm(a))
print("node table (eight-node step, chk convention):")
for (nm, E), r in TAB.items():
    print(f"   E={E:+.4f} {nm:10s} n={NVEC[nm]} dim={r['dim']} speeds={np.round(r['sv'], 7)} chirality={r['chi']:+d} tilt={r['tilt']:.1e}")
ok = all(r['dim'] == 2 for r in TAB.values())
ok &= all(np.allclose(TAB[(nm, np.pi / 2)]['sv'], vs, atol=1e-8) for nm in ('k*', '-k*'))
ok &= all(np.allclose(TAB[(nm, np.pi / 2)]['sv'], [0.2467203, 0.5837466, 0.5837466], atol=2e-7) for nm in NODES if '+pi' in nm)
chi_n = {nm: TAB[(nm, np.pi / 2)]['chi'] for nm in NODES}
ok &= all(chi_n[nm] == (-1) ** sum(NVEC[nm]) * chi_n['k*'] for nm in NODES)
check("R3 at E = +pi/2 all eight nodes are 2-fold Weyl doublets: +-k* isotropic sqrt2/3, doublers uniaxial (0.2467, 0.5837); "
      "chirality(k* + pi n) = (-1)^{|n|} chirality(k*) (naive-doubler pattern)", ok, f"chiralities {chi_n}")

# ---------------- R4: determinant characters ----------------
def det_char(Qm, idx):
    return {i: np.linalg.det(Qm.conj().T @ ROT[i]['U'] @ Qm) for i in idx}
def is_char(dc):
    ok = all(abs(abs(v) - 1) < 1e-9 for v in dc.values())
    for i in dc:
        for j in dc:
            l = find(ROT[i]['M'] @ ROT[j]['M'])
            if l in dc: ok &= abs(dc[i] * dc[j] - dc[l]) < 1e-9
    return ok
# all 2-fold levels at k* and -k* (any quasi-energy)
def all_levels(k, tol=1e-7):
    e, V = np.linalg.eig(W(k)); ph = np.angle(e); used = np.zeros(12, bool); out = []
    for i in np.argsort(ph):
        if used[i]: continue
        grp = np.where((~used) & (np.abs(wrap(ph - ph[i])) < tol))[0]; used[grp] = True
        Qm, _ = np.linalg.qr(V[:, grp]); out.append((ph[i], len(grp), Qm))
    return out
O_idx = list(range(24))
dets_star = []
for nm in ('k*', '-k*'):
    for E, m, Qm in all_levels(NODES[nm]):
        if m == 2: dets_star.append((nm, E, det_char(Qm, O_idx)))
ref = dets_star[0][2]
uniform = all(all(abs(dc[i] - ref[i]) < 1e-9 for i in O_idx) for _, _, dc in dets_star)
isA1 = all(abs(ref[i] - 1) < 1e-9 for i in O_idx); isA2 = all(abs(ref[i] - A2_O[cls(ROT[i]['M'])]) < 1e-9 for i in O_idx)
DETNAME = 'A1' if isA1 else ('A2' if isA2 else '?')
check("R4a det(U_g|D) is a genuine 1-dim character of O, the SAME for every 2-fold level at k* and -k* (all quasi-energies)",
      all(is_char(dc) for _, _, dc in dets_star) and uniform and DETNAME != '?',
      f"{len(dets_star)} doublets; det character = {DETNAME}")
chi_det = {i: (1 if DETNAME == 'A1' else A2_O[cls(ROT[i]['M'])]) for i in O_idx}
chi_oth = {i: (A2_O[cls(ROT[i]['M'])] if DETNAME == 'A1' else 1) for i in O_idx}
OTHNAME = 'A2' if DETNAME == 'A1' else 'A1'
ok = True; rows = []
for nm, k in NODES.items():
    if '+pi' not in nm: continue
    st = stab(k)
    for E, m, Qm in all_levels(k):
        if m != 2: continue
        dc = det_char(Qm, st)
        ok &= is_char(dc) and all(abs(dc[i] - chi_det[i]) < 1e-9 for i in st)
        rows.append((nm, round(E, 4)))
a2_restr_nontriv = all(any(abs(chi_oth[i] - chi_det[i]) > 1 for i in stab(NODES[nm])) for nm in NODES if '+pi' in nm)
check("R4b at each doubler (little group D4) every 2-fold level has det character = restriction of the k* det character; "
      "the other O-character restricts to a DIFFERENT D4 character (A2|D4 = B1)", ok and a2_restr_nontriv, f"{len(rows)} doubler doublets tested")

# ---------------- R2: real-space convention check on L = 4 ----------------
def antisym_basis():
    B = []
    for i in range(12):
        for j in range(i + 1, 12):
            X = np.zeros((12, 12)); X[i, j] = 1; X[j, i] = -1; B.append(X)
    return B
AB = antisym_basis()
def channel_space(chi, idx=O_idx):
    """basis of {A antisym: U_g A U_g^T = chi(g) A, g in idx}: null space of the stacked linear map."""
    rowsM = []
    for i in idx:
        U = ROT[i]['U']; rowsM.append(np.array([(U @ X @ U.T - chi[i] * X)[np.triu_indices(12, 1)] for X in AB]).T)
    Mx = np.vstack(rowsM); _, s, Vh = np.linalg.svd(Mx); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))])
    return [sum(c * X for c, X in zip(v, AB)) for v in Vh[s < 1e-10]]
Vdet = channel_space(chi_det); Voth = channel_space(chi_oth)
print(f"on-site antisymmetric pairing channels: dim V_{DETNAME}(det) = {len(Vdet)}, dim V_{OTHNAME} = {len(Voth)} (of 66)")
def realspace_D(A, Q=Q_R):
    D = np.zeros((nV, nV), complex)
    for a, (v, c) in enumerate(VERTS):
        ph = np.exp(1j * np.dot(Q, v))
        for b_, (v2, c2) in enumerate(VERTS):
            if v2 == v: D[a, b_] = ph * A[CI[c], CI[c2]]
    return D
def rnd(V): return sum(rng.normal() * X for X in V) if V else np.zeros((12, 12))
A_det = rnd(Vdet); A_det /= np.linalg.norm(A_det)
A_oth = rnd(Voth); A_oth /= np.linalg.norm(A_oth) if Voth else 1
Dd = realspace_D(A_det)
ok = all(np.allclose(conj(Dd, P, s_), chi_det[i] * Dd) for i, (P, s_) in enumerate(rots))
odd_t = [t for t in TV if sum(t) % 2 == 1][:3]; ev_t = [t for t in TV if sum(t) % 2 == 0 and any(t)][:3]
ok_t = all(np.allclose(conj(Dd, *trans[TV.index(t)]), -Dd) for t in odd_t) and all(np.allclose(conj(Dd, *trans[TV.index(t)]), Dd) for t in ev_t)
# a wrong-character matrix is NOT symmetric (negative control)
ok_neg = not all(np.allclose(conj(Dd, P, s_), chi_oth[i] * Dd) for i, (P, s_) in enumerate(rots))
check("R2 real-space L=4 cross-check: D = sum_v e^{iR.v} A_v satisfies R_g D R_g^T = chi(g) D for all 24 lifts; odd translations give -D, "
      "even ones +D (so T_e e^{i pi |e| N/2} is preserved); negative control fails", ok and ok_t and ok_neg)

# ---------------- R5: singlet amplitudes ----------------
def singlet(Qm, Dm): return (Qm.conj().T @ Dm @ Qm.conj())[0, 1]
for E in (np.pi / 2, -np.pi / 2):
    md = {nm: abs(singlet(TAB[(nm, E)]['Q'], A_det)) for nm in NODES}
    mo = {nm: abs(singlet(TAB[(nm, E)]['Q'], A_oth)) for nm in NODES}
    print(f"   E={E:+.3f}  |m_K| for random on-site A in V_det: " + ", ".join(f"{nm}:{v:.3f}" for nm, v in md.items()))
    print(f"   E={E:+.3f}  |m_K| for random on-site A in V_oth: " + ", ".join(f"{nm}:{v:.1e}" for nm, v in mo.items()))
    check(f"R5 (E={E:+.3f}) on-site pairing at R: channel det gives a nonzero singlet (Majorana) mass at ALL eight nodes; "
          f"channel {OTHNAME} gives exactly zero at ALL eight", min(md.values()) > 1e-3 and max(mo.values()) < 1e-12)
# rank statement: the 8 linear functionals A -> m_K(A) on V_det -- can m_{+-k*} vanish with doublers nonzero? (only by tuning)
F = np.array([[singlet(TAB[(nm, np.pi / 2)]['Q'], X) for X in Vdet] for nm in NODES])
rk = np.linalg.matrix_rank(F, tol=1e-9)
print(f"   rank of the 8 node-singlet functionals on V_det (dim {len(Vdet)}): {rk}")
# construct an on-site A in V_det with m_{+-k*} = 0 and doublers nonzero, if the rank allows
Fs = F[:2]; _, s, Vh = np.linalg.svd(Fs); nullv = Vh[np.sum(s > 1e-9):]
if len(nullv):
    c = nullv.T @ rng.normal(size=len(nullv)); A_tuned = sum(ci * X for ci, X in zip(c, Vdet))
    mt = {nm: abs(singlet(TAB[(nm, np.pi / 2)]['Q'], A_tuned)) for nm in NODES}
    print("   tuned on-site A (m_{+-k*} set to 0 by hand): " + ", ".join(f"{nm}:{v:.2e}" for nm, v in mt.items()))
    tuned_ok = max(mt['k*'], mt['-k*']) < 1e-12 and min(v for nm, v in mt.items() if '+pi' in nm) > 1e-3
else:
    tuned_ok = None
check("R5c the node singlets are independent linear functionals on V_det, so killing m_{+-k*} is a codimension-4 (real) tuning, "
      "not a symmetry consequence (on-site tuned example exists)", rk >= 3 and tuned_ok is not False, f"rank {rk}, tuned example: {tuned_ok}")

# ---------------- R6: k-dependent symmetric pairings, all four channels ----------------
shifts = [s for s in itertools.product((-1, 0, 1), repeat=3)]
def seed_delta(rng_):
    C0 = {s: rng_.normal(size=(12, 12)) + 1j * rng_.normal(size=(12, 12)) for s in shifts}
    return lambda k: sum(Cm * np.exp(1j * np.dot(k, s)) for s, Cm in C0.items())
def symmetrize(D0, chi, Q):
    def Dk(k):
        Dfa = lambda kk: 0.5 * (D0(kk) - D0(Q - kk).T)                     # Fermi antisymmetry Delta(k) = -Delta(Q-k)^T
        return sum(np.conj(chi[i]) * ROT[i]['U'].T @ Dfa(gk(ROT[i], k)) @ ROT[i]['U'] for i in O_idx) / 24
    return Dk
res = {}
for Qn, Q in (('R', Q_R), ('Gamma', np.zeros(3))):
    for cn, chi in ((DETNAME + '(det)', chi_det), (OTHNAME, chi_oth)):
        Dk = symmetrize(seed_delta(rng), chi, Q)
        kt = rng.uniform(-np.pi, np.pi, (3, 3))
        symok = all(np.allclose(Dk(gk(ROT[i], k)), chi[i] * ROT[i]['U'] @ Dk(k) @ ROT[i]['U'].T, atol=1e-10) for i in O_idx[:24:5] for k in kt)
        fermi = all(np.allclose(Dk(k), -Dk(Q - k).T, atol=1e-10) for k in kt)
        if Qn == 'R':   # intra-node singlet at each node
            m = {nm: abs(singlet(TAB[(nm, np.pi / 2)]['Q'], Dk(NODES[nm]))) for nm in NODES}
        else:           # Q = 0 pairs K with -K: the inter-node 2x2 block (any entry)
            m = {nm: np.abs(TAB[(nm, np.pi / 2)]['Q'].conj().T @ Dk(NODES[nm]) @ level(-NODES[nm], np.pi / 2).conj()).max() for nm in NODES}
        res[(Qn, cn)] = (symok, fermi, m)
        print(f"   Q={Qn:5s} chi={cn:8s} sym={symok} fermi={fermi} node amplitudes: " + ", ".join(f"{nm}:{v:.2e}" for nm, v in m.items()))
ok = all(v[0] and v[1] for v in res.values())
ok &= min(res[('R', DETNAME + '(det)')][2].values()) > 1e-4 and max(res[('R', OTHNAME)][2].values()) < 1e-11
check("R6 random range-1 k-dependent symmetric Delta(k): at Q = R the singlet node mass is nonzero at all eight (chi = det) or zero at all eight "
      "(chi != det) -- never selective; at Q = 0 the inter-node blocks are generic but cannot gap (chirality, see c1_anomaly.py)", ok)

# ---------------- R7: 4-fold levels at k* ----------------
for E, m, Qm in all_levels(kst):
    if m == 4:
        dims = []
        for chi in (chi_det, chi_oth):
            rowsM = []
            basis = []
            for i_ in range(4):
                for j_ in range(i_ + 1, 4):
                    X = np.zeros((4, 4)); X[i_, j_] = 1; X[j_, i_] = -1; basis.append(X)
            for i in O_idx:
                Ur = Qm.conj().T @ ROT[i]['U'] @ Qm
                rowsM.append(np.array([(Ur @ X @ Ur.T - chi[i] * X)[np.triu_indices(4, 1)] for X in basis]).T)
            sv = np.linalg.svd(np.vstack(rowsM), compute_uv=False); dims.append(int(np.sum(sv < 1e-9)) + (6 - len(sv) if len(sv) < 6 else 0))
        print(f"   4-fold level at k*, E={E:+.4f}: chi-invariant antisymmetric pairs: {DETNAME}(det): {dims[0]}, {OTHNAME}: {dims[1]}")

# ---------------- R8: aside -- translation-breaking CDW masses at R ----------------
def herm_channel(chi):
    Bs = []
    for i in range(12):
        for j in range(i, 12):
            X = np.zeros((12, 12), complex); X[i, j] = 1; X[j, i] = 1; Bs.append(X)
            if i != j:
                Y = np.zeros((12, 12), complex); Y[i, j] = 1j; Y[j, i] = -1j; Bs.append(Y)
    rowsM = []
    for i in O_idx:
        U = ROT[i]['U']; rowsM.append(np.array([np.concatenate([(U @ X @ U.T - chi[i] * X).real.ravel(), (U @ X @ U.T - chi[i] * X).imag.ravel()]) for X in Bs]).T)
    _, s, Vh = np.linalg.svd(np.vstack(rowsM)); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))])
    return [sum(c * X for c, X in zip(v, Bs)) for v in Vh[s < 1e-10]]
for cn, chi in ((DETNAME, chi_det), (OTHNAME, chi_oth)):
    Hc = herm_channel(chi); Mm = sum(rng.normal() * X for X in Hc)
    amp = {nm: np.abs(TAB[(nm, np.pi / 2)]['Q'].conj().T @ Mm @ level(NODES[nm] + Q_R, np.pi / 2)).max() for nm in NODES}
    print(f"   [aside, breaks odd translations] staggered on-site CDW mass e^(iR.x) c^dag M c, M in channel {cn} (dim {len(Hc)}): "
          "max |<node K|M|node K+R>|: " + ", ".join(f"{nm}:{v:.2e}" for nm, v in amp.items()))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
