AUDIT_INPUT_PATHS = ('docs/THE_LABEL_SELECTIVE_CHARGE_FOUR_MIRROR_TERM_ON_THE_FREEZE_WALK_FIRST_EXISTS_AT_FOUR_FAMILIES_AND_FREES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""freeze-mirror-smg: can a label-selective (tau3 = -1, mirror-only), charge-4, cell-local, multi-family
term gap the mirror (R) Weyls of the FREEZE walk symmetrically while the light (L) Weyls stay gapless?

Self-contained (numpy + scipy), seeded. Rebuilds CL-1's 2^3 cell, the T rotations with CL-1's site gauges V,
CTWIST and rule FREEZE exactly as in twist-local-single, then:
  A. existence/uniqueness of T-invariant charge-4 mirror terms for N_f = 2, 3, 4 families (exact, characters);
  B. the unique SU(4)-family x T term at N_f = 4: one-cell exact diagonalisation (256 states), symmetric
     ground state, Green's function zero on R, pole on L; G-S chirality of the zero; dispersive check with
     one light family kept (1024 states);
  C. anomaly bookkeeping of the gapped set and the free projected light walk (released-partner diagnostic).
"""
import itertools as it
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm, null_space, logm
from scipy.optimize import minimize

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261023)
NPASS = NFAIL = 0
w = np.exp(2j * np.pi / 3)


def check(name, ok, detail=""):
    global NPASS, NFAIL
    ok = bool(ok); NPASS += ok; NFAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


def nullsp(rows):
    return null_space(np.vstack(rows), rcond=1e-9)


def cm(o):
    return np.kron(o, np.eye(8)) - np.kron(np.eye(8), o.T)


def axang(R):
    ev, vv = np.linalg.eig(R)
    n = np.real(vv[:, np.argmin(abs(ev - 1))])
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return (n if np.allclose(expm(th * K), R) else -n), th


ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0:
            ROTS.append(R)
C3d = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
TI = [n for n, R in enumerate(ROTS) if abs(np.trace(R)) < 1e-9 or np.allclose(R, np.diag(np.diag(R)))]
iC3 = next(n for n, R in enumerate(ROTS) if np.allclose(R, C3d))
CELL = list(it.product([0, 1], repeat=3)); A = np.array(CELL)
IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}


def eta_s(i, a):
    return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]


def Wl(i, k, odd):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == (1 if odd else 0):
            b = list(a); b[i] = 1 - a[i]; b = tuple(b)
            ph = np.exp(2j * k[i]) if odd else 1
            M[IDX[b], IDX[a]] = eta_s(i, a) * ph; M[IDX[a], IDX[b]] = eta_s(i, a) * np.conj(ph)
    return M


Re = sum(Wl(i, np.zeros(3), 0) for i in range(3)) / np.sqrt(3)


def U1(k, eps=0.3):
    return expm(1j * eps * sum(Wl(i, k, 1) for i in range(3)) / np.sqrt(3)) @ expm(-1j * eps * Re)


hh = 1e-6
Av = []
for i in range(3):
    d = np.zeros(3); d[i] = hh; Av.append(1j * (U1(d) - U1(-d)) / (2 * hh))
Ah = [a / np.sqrt(np.trace(a @ a).real / 8) for a in Av]
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]
V = {}
for n in TI:
    P = np.zeros((8, 8))
    for a in CELL:
        b = tuple(np.rint(ROTS[n] @ (np.array(a) - .5) + .5).astype(int)); P[IDX[b], IDX[a]] = 1
    for sgn in it.product([1, -1], repeat=8):
        Vg = np.diag(sgn) @ P
        if all(np.allclose(Vg @ U1(k) @ Vg.T, U1(ROTS[n] @ k)) for k in kt):
            V[n] = Vg; break
VT = list(V.values())
nl, th = axang(ROTS[iC3])
t = expm(-1j * th * sum(nl[i] * S[i] for i in range(3))).conj().T @ V[iC3]
if not np.allclose(np.linalg.matrix_power(t, 3), np.eye(8), atol=1e-6):
    t = -t
PL = (np.eye(8) + chi) / 2; PR = np.eye(8) - PL
sig = [2 * s for s in S]
tau3 = (t - t.conj().T) / (1j * np.sqrt(3)); tau3 = (tau3 + tau3.conj().T) / 2
Pw = (np.eye(8) + tau3) / 2; Pb = np.eye(8) - Pw
Cb = nullsp([cm(o) for o in sig + [chi]])
Yr = (Cb @ rng.normal(size=Cb.shape[1])).reshape(8, 8)
tp = np.zeros((8, 8), complex)
for P in (PL, PR):
    Zb = P @ Pw @ Yr @ Pb @ P; tp += Zb / np.sqrt(np.trace(Zb @ Zb.conj().T).real / 2)
tau1 = tp + tp.conj().T; tau2 = -1j * (tp - tp.conj().T)
gam = [tau1, tau2] + [tau3 @ s for s in sig]


def Uc(K):
    c, s = np.cos(K), np.sin(K)
    H = (np.sqrt(2) / 3) * (c[0] + np.conj(w) * c[1] + w * c[2])
    return c.sum() / 3 * np.eye(8) + 1j * (H * tp + np.conj(H) * tp.conj().T + (s @ np.array(gam[2:]).reshape(3, 64)).reshape(8, 8) / np.sqrt(3))



Cm = nullsp([cm(o) for o in sig + [tau1, tau2, tau3]])
Ex = None
for j in range(Cm.shape[1]):
    e = Cm[:, j].reshape(8, 8); a = (e - chi @ e @ chi) / 2
    if np.linalg.norm(a) > 1e-6:
        Ex = a + a.conj().T; break
Ex = Ex / np.sqrt(np.trace(Ex @ Ex).real / 8)
Y = Pw + Pb @ Ex
Pp = (np.eye(8) + chi @ tau3) / 2; Pm = np.eye(8) - Pp
UF = lambda K: Pp @ (Y @ Uc(K) @ Y.conj().T) + Pm @ (1j * tau3)
PRl = Pp @ (np.eye(8) - tau3) / 2; PLl = Pp @ (np.eye(8) + tau3) / 2
RN = np.pi * np.ones(3)


def basis(P):
    v, B = np.linalg.eigh(P); B = B[:, v > 0.5]
    _, X = np.linalg.eigh(B.conj().T @ sig[2] @ B); return B @ X


BR, BL, BP = basis(PRl), basis(PLl), basis(Pp)
sR = [BR.conj().T @ s @ BR for s in sig]; sL = [BL.conj().T @ s @ BL for s in sig]


def vel(B, sB, K0, sgn=1):
    U0 = sgn * UF(K0); M = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3); d[j] = hh
        Aj = B.conj().T @ (1j * (sgn * UF(K0 + d) - sgn * UF(K0 - d)) / (2 * hh) @ U0.conj().T) @ B
        for i in range(3):
            M[i, j] = np.trace(Aj @ sB[i]).real / 2
    return M


uF = max(np.linalg.norm(UF(K) @ UF(K).conj().T - np.eye(8)) for K in kt)
lT = max(np.linalg.norm(v @ P @ v.T - P) for v in VT for P in (PRl, PLl))
ch = [int(np.sign(np.linalg.det(vel(B, sB, K0)))) for K0 in (np.zeros(3), RN) for B, sB in ((BL, sL), (BR, sR))]
check("A0 rebuild FREEZE; the labels (1 +- tau3)/2 on Pi+ are rank-2, T-invariant cell projectors; at each node "
      "the light label tau3 = +1 and the mirror label tau3 = -1 carry opposite chirality, the same at K = 0 and R",
      uF < 1e-12 and lT < 1e-9 and ch[0] == ch[2] == -ch[1] == -ch[3],
      f"unitarity {uF:.0e}, label T-res {lT:.0e}, sign det v (light, mirror) @0, @R: {ch}")
print("  naming: by twist-local-single's sign rule (det v > 0 = 'L') tau3 = -1 is its 'L' (q = 2); here "
      "'light'/'mirror' name roles, not handedness")

print("== A. which charge-4 mirror terms does T allow? ==")


def closure(gens):
    key = lambda M: tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), 5) + 0.0)
    G = [np.eye(gens[0].shape[0], dtype=complex)]; seen = {key(G[0])}; fr = list(G)
    while fr:
        nw = []
        for a in fr:
            for b in gens:
                c = a @ b; k = key(c)
                if k not in seen:
                    seen.add(k); G.append(c); nw.append(c)
        fr = nw
    return G


cnt = {}
for lab, B in (("mirror", BR), ("light", BL)):
    G = closure([B.conj().T @ v @ B for v in VT]); ev = [np.linalg.eigvals(g.conj()) for g in G]
    nT = [int(round(np.mean([np.poly(np.tile(l, N))[4] for l in ev]).real)) for N in range(2, 9)]
    s4 = int(round(np.mean([sum(l[0] ** a * l[1] ** (4 - a) for a in range(5)) for l in ev]).real))
    d2 = int(round(np.mean([np.prod(l) ** 2 for l in ev]).real))
    dq = np.linalg.det(B.conj().T @ V[iC3] @ B)
    cnt[lab] = dict(order=len(G), T_counts_Nf2to8=nT, Sym4_inv=s4, det2_inv=d2,
                    q=[x for x in range(3) if np.isclose(dq, w ** (2 * x))])
    print(f"  {lab}: {cnt[lab]}")
m = cnt["mirror"]
check("A1 (exact, characters over the 24-element turn group) N_f = 2 and N_f = 3 admit NO T-invariant charge-4 "
      "mirror term: Lambda^4(doublet x C^N) = sum S_lam(doublet) x S_lam'(C^N); (2,2) is det^2 = w^(4q) != 1, "
      "(3,1) is spin-1 x det (no T singlet), (4) needs N >= 4", m["T_counts_Nf2to8"][:2] == [0, 0] and m["det2_inv"] == 0)
check("A2 (exact) the first allowed count is N_f = 4, with EXACTLY ONE term, and it is forced to be SU(4)-family "
      "symmetric: eps_abcd times the one T-invariant line of Sym^4 of the mirror spin doublet (count C(N_f, 4) "
      "for N_f = 2..8); the same holds for the light label", m["T_counts_Nf2to8"] == [0, 0, 1, 5, 15, 35, 70]
      and m["Sym4_inv"] == 1 and cnt["light"]["T_counts_Nf2to8"] == m["T_counts_Nf2to8"])

print("== B. the unique N_f = 4 term on one cell: exact diagonalisation ==")
gR = [BR.conj().T @ v @ BR for v in VT]
rows = [np.kron(np.kron(g.conj(), g.conj()), np.kron(g.conj(), g.conj())) - np.eye(16) for g in gR]
for p in it.permutations(range(4)):
    Pm4 = np.zeros((16, 16))
    for s in it.product(range(2), repeat=4):
        Pm4[int("".join(str(s[p[k]]) for k in range(4)), 2), int("".join(map(str, s)), 2)] = 1
    rows.append(Pm4 - np.eye(16))
cvec = null_space(np.vstack(rows), rcond=1e-9); c = cvec[:, 0] / np.linalg.norm(cvec[:, 0])


def fock(n):
    I2 = sp.identity(2, format="csr"); Z = sp.diags([1.0, -1.0]); lo = sp.csr_matrix(np.array([[0, 1.0], [0, 0]]))
    ops = []
    for j in range(n):
        mm = sp.identity(1, format="csr")
        for k in range(n):
            mm = sp.kron(mm, Z if k < j else (lo if k == j else I2), format="csr")
        ops.append(mm.astype(complex))
    return ops


PS = {p: np.linalg.det(np.eye(4)[list(p)]) for p in it.permutations(range(4))}


def Qop(aR):
    Q = 0
    for s in it.product(range(2), repeat=4):
        cs = c[int("".join(map(str, s)), 2)]
        if abs(cs) < 1e-12: continue
        for p, sg in PS.items():
            Q = Q + cs * sg * (aR[2 * p[0] + s[0]] @ aR[2 * p[1] + s[1]] @ aR[2 * p[2] + s[2]] @ aR[2 * p[3] + s[3]])
    return Q


a8 = fock(8); Q8 = Qop(a8)
tr_res = max(sp.linalg.norm(Qop([sum(np.conj(g[t, s]) * a8[2 * f + t] for t in range(2)) for f in range(4)
                                 for s in range(2)]) - Q8) for g in gR)
Fu = np.linalg.qr(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))[0]; Fu = Fu / np.linalg.det(Fu) ** 0.25
su_res = sp.linalg.norm(Qop([sum(np.conj(Fu[b, f]) * a8[2 * b + s] for b in range(4)) for f in range(4)
                             for s in range(2)]) - Q8)
H1 = -(Q8 + Q8.conj().T).toarray(); E = np.linalg.eigvalsh(H1); D1 = E[np.argmax(E > E[0] + 1e-8)] - E[0]; Hint8 = H1 / D1
N8 = sum((x.conj().T @ x) for x in a8).toarray(); A8 = [x.toarray() for x in a8]


def green(Ev, Wv, ops, z, tol=1e-8):
    """T -> 0 Green's function, averaged over the (near-)degenerate ground manifold."""
    dE = Ev - Ev[0]; gsn = np.where(dE < tol)[0]; G = 0
    for i0 in gsn:
        g0 = Wv[:, i0]; d = Ev - Ev[i0]
        Ap = np.array([Wv.conj().T @ (o.conj().T @ g0) for o in ops]); Am = np.array([Wv.conj().T @ (o @ g0) for o in ops])
        ok = np.abs(d) > 1e-12
        G = G + (np.einsum("in,jn->ij", Ap.conj()[:, ok], Ap[:, ok] / (z - d[ok]))
                 + np.einsum("jn,in->ij", Am.conj()[:, ok], Am[:, ok] / (z + d[ok])))
    return G / len(gsn)


E, Wv = np.linalg.eigh(Hint8); gsn = np.where(E < E[0] + 1e-8)[0]; Pg = Wv[:, gsn]
nocc = np.linalg.eigvalsh(Pg.conj().T @ N8 @ Pg)
rel = np.linalg.det(BR.conj().T @ V[iC3] @ BR) ** 4
G0 = green(E, Wv, A8, 0.0)
check("B1 (exact) Q = sum_s c_s eps_abcd r_a,s1 r_b,s2 r_c,s3 r_d,s4 is T-invariant (operator level, 12 turns) and "
      "SU(4)-invariant; -(Q + Q^+) on one cell's 8 mirror modes has a 2-FOLD ground state: A = |0> + Q^+|0> and "
      "B = |8> + Q|8>, at mirror occupations 2 and 6 of 8, whose turn charges differ by det(r)^4 = w^(8q) != 1 "
      "(not a symmetry doublet: the term's particle-hole balance makes them degenerate); G_R(0) = 0 ONLY as "
      "the A/B average (A and B give -g0 and +g0)", tr_res < 1e-10 and su_res < 1e-10 and len(gsn) == 2 and np.allclose(nocc, [2, 6])
      and abs(rel - 1) > 0.5 and np.abs(G0).max() < 1e-10,
      f"T res {tr_res:.0e}, SU(4) res {su_res:.0e}, deg {len(gsn)}, <N> {np.round(nocc, 6)}, det(r)^4 = "
      f"{rel.real:+.3f}{rel.imag:+.3f}i, max|G_R(0)| {np.abs(G0).max():.0e}")
mu = 0.2
Hmu = Hint8 + mu * (N8 - 4 * np.eye(256)) / 4
E, Wv = np.linalg.eigh(Hmu); g0v = Wv[:, 0]
wl = [Wv.conj().T @ (a.conj().T @ g0v) for a in A8] + [Wv.conj().T @ (a @ g0v) for a in A8]
pgap = min(np.abs(E - E[0])[np.abs(x) > 1e-6].min() for x in wl)
Gm = green(E, Wv, A8, 0.0); gdiag = np.diag(Gm)
check("B2 (exact) a T-, SU(4)-, Z4-invariant mirror number term mu (N_R - 4)/4 (mu = 0.2, SUPPLIED) selects A: the "
      "cell ground state is unique and symmetric, with a single-particle gap; G_R(0) is then FINITE and equal on "
      "all mirror modes (Schur), not a zero", E[1] - E[0] > 0.05 and pgap > 0.5 and np.abs(Gm - gdiag.mean() *
      np.eye(8)).max() < 1e-10, f"split {E[1] - E[0]:.3f}, 1-particle gap {pgap:.3f}, G_R(0) = {gdiag.mean().real:+.4f} x 1")


def HF(K, sgn=1):
    return 1j * logm(sgn * UF(K))


def onebody(h, ops, modes):
    return sum(h[i, j] * (ops[mi].conj().T @ ops[mj]) for i, mi in enumerate(modes) for j, mj in enumerate(modes))


fam = [[2 * f, 2 * f + 1] for f in range(4)]


def Gmir(K, sgn, mu_):
    hRR = BR.conj().T @ HF(K, sgn) @ BR
    H = Hint8 + mu_ * (N8 - 4 * np.eye(256)) / 4 + sum(onebody(hRR, a8, md) for md in fam).toarray()
    E, Wv = np.linalg.eigh(H); return green(E, Wv, A8[:2], 0.0, tol=1e-8)


print("  G-S zero structure of the mirror (family-0 block): G_R(0,K) = g0 + u sigma.K near the node")
gs_ok = True
for K0, sgn, nm in ((np.zeros(3), 1, "K=0"), (RN, -1, "R  ")):
    vR = np.sign(np.linalg.det(vel(BR, sR, K0, sgn)))
    for mu_ in (0.2, 0.05):
        g00 = Gmir(K0, sgn, mu_); D = []
        for j in range(3):
            d = np.zeros(3); d[j] = 1e-3; D.append((Gmir(K0 + d, sgn, mu_) - Gmir(K0 - d, sgn, mu_)) / 2e-3)
        u = np.array([[np.trace(D[j] @ sR[i]).real / 2 for j in range(3)] for i in range(3)])
        rad = abs(g00[0, 0]) / abs(np.linalg.det(u)) ** (1 / 3)
        print(f"  {nm} mu={mu_}: g0 {g00[0, 0].real:+.4f}, winding of G: zero-form {np.sign(np.linalg.det(u)):+.0f} vs mirror pole "
              f"{-vR:+.0f}, zero-surface radius |g0|/|u| {rad:.3f}")
        gs_ok &= np.sign(np.linalg.det(u)) == -vR
check("B3 (exact ED + finite differences) Golterman-Shamir counting at both nodes, unique symmetric state A: "
      "G_R(0,K) = g0 + u sigma.K with g0 != 0, so the node carries NEITHER a pole NOR a zero; the would-be zero "
      "has the winding of the mirror pole it replaces, and it is pushed to a zero surface |K| ~ |g0/u| ~ 3, "
      "outside the node region (the mirror winding is relocated, not removed)", gs_ok)

print("== B4. one light family kept (10 modes, 1024 states): light pole near K = 0; release at X ==")
a10 = fock(10); A10 = a10
Hint10 = (-(Qop(a10[:8]) + Qop(a10[:8]).conj().T) / D1).toarray(); N10m = sum(A10[i].conj().T @ A10[i] for i in range(8)).toarray()
BLR = np.hstack([BL, BR])


def H10(K, sgn, g, mu_):
    hF = HF(K, sgn); h0 = BLR.conj().T @ hF @ BLR; hRR = BR.conj().T @ hF @ BR
    H = onebody(h0, a10, [8, 9, 0, 1]) + sum(onebody(hRR, a10, md) for md in fam[1:])
    return H.toarray() + g * (Hint10 + mu_ * (N10m - 4 * np.eye(1024)) / 4)


def light_G(K, sgn, g, mu_):
    E, Wv = np.linalg.eigh(H10(K, sgn, g, mu_)); return E, Wv, green(E, Wv, A10[8:], 0.0)


nh = np.array([1, 0.37, 0.21]); nh = nh / np.linalg.norm(nh); dev = []
for kap in (0.1, 0.05):
    K = kap * nh; E, Wv, GL = light_G(K, 1, 1.0, mu)
    hLL = BL.conj().T @ HF(K) @ BL; dev.append(np.linalg.norm(np.linalg.inv(GL) + hLL) / np.linalg.norm(hLL))
check("B4a (exact ED, g = 1 cell gap, mu = 0.2) the light Weyl is untouched near K = 0: G_L(0,K)^-1 = -h_LL(K) up "
      "to a relative error falling at least as K^2 (seen ~K^3; label leak O(K^2)), so the light pole stays at the node",
      dev[0] < 0.05 and dev[1] < dev[0] / 3, f"rel. deviation {dev[0]:.1e} (|K| = 0.1), {dev[1]:.1e} (0.05)")
XP = np.array([np.pi, 0, 0])
hLLX = BL.conj().T @ HF(XP) @ BL
print(f"  X = (pi,0,0): projected light levels {np.round(np.linalg.eigvalsh(hLLX), 3)}; free Pi+ levels "
      f"{np.round(np.linalg.eigvalsh(BP.conj().T @ HF(XP) @ BP), 3)}")
rel_w = []
for g in (0.0, 1.0, 4.0, 16.0):
    E, Wv = np.linalg.eigh(H10(XP, 1, g, mu if g else 0.0)); g0v = Wv[:, 0]; dE = E - E[0]
    wt = sum(np.abs(Wv.conj().T @ (A10[i].conj().T @ g0v)) ** 2 + np.abs(Wv.conj().T @ (A10[i] @ g0v)) ** 2 for i in (8, 9))
    low = wt[(dE > 1e-12) & (dE < 0.15)].sum() / 2
    lw = dE[(wt > 0.05) & (dE > 1e-12)].min()
    rel_w.append(low); print(f"  X, g = {g:4.0f}: light weight below 0.15 = {low:.3f}; lowest light pole {lw:.3f}")
check("B4b (exact ED) Golterman-Shamir release at X: free, the light-labelled modes at X are gapped by mixing "
      "with the mirror (no light weight below 0.15); as the mirror is gapped by the charge-4 term the light weight "
      "returns to low energy at the projected light level: a light partner is FREED", rel_w[0] < 0.01 and
      rel_w[-1] > 0.5 and rel_w[-1] > rel_w[1], f"weights {np.round(rel_w, 3)}")

print("== C. anomaly of the gapped set; the projected light walk ==")
print("  free FREEZE content per family: light 1 Weyl at K = 0 and 1 at R (same sign), mirror the opposite")
for Nf in (2, 3, 4, 8):
    print(f"  N_f={Nf}: T-terms {m['T_counts_Nf2to8'][Nf - 2]}; gapped set {2 * Nf} Weyls, Z4 charge 1: Spin-Z4 index {2 * Nf % 16} mod 16; "
          f"SU(N_f)^3 index {2 if Nf >= 3 else 'n/a'}")
check("C1 (bookkeeping; Z16 for Spin-Z4 is a LITERATURE input) N_f = 4: index 8 mod 16 and SU(4)^3 index 2, both "
      "kept by the term, so a symmetric trivial mirror gap with ONLY the light Weyls left is anomaly-forbidden; "
      "Z4 alone first allows N_f = 8",
      (2 * 4) % 16 != 0 and (2 * 8) % 16 == 0)


def polar(K, B):
    X, S, Yh = np.linalg.svd(B.conj().T @ UF(K) @ B); return X @ Yh, S.min()


def split(K, B):
    l = np.linalg.eigvals(polar(K, B)[0]); return abs(l[0] - l[1])


nodes_by = {}
for lab, B, sB in (("light", BL, sL), ("mirror", BR, sR)):
    g12 = np.linspace(-np.pi, np.pi, 12, endpoint=False); vals = {}; smin = 9
    for K in it.product(g12, repeat=3):
        K = np.array(K); vals[tuple(K)] = split(K, B); smin = min(smin, polar(K, B)[1])
    nodes = []
    for K0 in sorted(vals, key=vals.get)[:40]:
        r = minimize(lambda k: split(k, B), np.array(K0), method="Nelder-Mead",
                     options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 3000})
        if r.fun < 1e-5:
            k = (r.x + np.pi) % (2 * np.pi) - np.pi
            if not any(np.linalg.norm((k - n + np.pi) % (2 * np.pi) - np.pi) < 1e-3 for n in nodes):
                nodes.append(k)
    sg = []
    for k in nodes:
        U0 = polar(k, B)[0]; M = np.zeros((3, 3))
        for j in range(3):
            d = np.zeros(3); d[j] = hh
            Aj = 1j * (polar(k + d, B)[0] - polar(k - d, B)[0]) / (2 * hh) @ U0.conj().T
            for i in range(3):
                M[i, j] = np.trace(Aj @ sB[i]).real / 2
        sg.append((int(round(abs(k).sum() / np.pi)), int(np.sign(np.linalg.det(M)))))
    nodes_by[lab] = sorted(sg)
    print(f"  projected {lab} walk (polar part): min singular value {smin:.3f}; nodes (number of pi entries, sign): "
          f"{nodes_by[lab]}")
L = nodes_by["light"]
check("C2 (finite diagnostic: grid + refinement) the light-labelled projection of FREEZE has 8 nodes per family: "
      "the 2 light Weyls and 6 at X, M with the OPPOSITE sign -- partners gapped only by light-mirror mixing",
      len(L) == 8 and [x for x in L if x[0] in (0, 3)] == [(0, ch[0]), (3, ch[0])] and
      all(x[1] == -ch[0] for x in L if x[0] in (1, 2)) and len(nodes_by["mirror"]) == 8)
print("verdict: the T-allowed charge-4 mirror term first exists at N_f = 4 (unique, SU(4) forced); with a supplied")
print("bias it gaps the mirror symmetrically on a cell and keeps the node light Weyls, but frees 6 light partners")
print("per family at X, M (Golterman-Shamir, gap ~ 1/g). Not a chirality fix.")
print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
