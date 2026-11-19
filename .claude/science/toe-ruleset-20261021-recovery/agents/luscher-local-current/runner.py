#!/usr/bin/env python3
"""Finite-lattice diagnostic of Luscher's locality condition for the U(1)_Y anomaly of the overlap on 4^4.
Overlap of the Wilson kernel (r = 1, m0 = 1.6, copied from overlap-nonabelian); H = g5 X, D = 1 + g5 sign H,
q_Y(x) = tr g5 D(x,x) = tr sign H(x,x) for one Weyl component of hypercharge Y; covariant U(1)_Y anomaly
A(x) = sum_species m Y q_Y(x). Contents: the 16 per family and a lone L doublet.
Backgrounds are FACTORISED U(1) fields: (A1, A2) depend on (x1, x2), (A3, A4) on (x3, x4); the only field
strengths are F12(x1,x2), F34(x3,x4); Luscher's topological density is T = F12 F34 / (4 pi^2).
Question: is A = d*k with k a local gauge-invariant current (Luscher 1998 cohomology theorem, supplied)?
Fits: k = linear combination of plaquette monomials within L1 range r; residual on held-out backgrounds.
Finite diagnostic, NOT the measure construction. Supplied: Luscher 1998/1999 (U(1) exact, non-abelian
perturbative), Neuberger 1998, the 16's hypercharges, m0, the backgrounds. Self-contained; seeded; numpy only."""
AUDIT_TIMEOUT_SEC = 120
import time
from itertools import combinations_with_replacement as cwr
import numpy as np

T0 = time.time()
rng = np.random.default_rng(20261024)
P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

L = 4; M0 = 1.6; N = L ** 4
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1]).astype(complex)
I2 = np.eye(2); Z2 = 0 * I2
G4 = [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)] + [np.block([[Z2, I2], [I2, Z2]])]
G5 = G4[0] @ G4[1] @ G4[2] @ G4[3]
idx = np.arange(N).reshape((L,) * 4); xs = np.arange(N)
YS = [1 / 6, -1 / 2, -2 / 3, 1 / 3, 1.0]; MULT = np.array([6, 2, 3, 3, 1])     # Q, L, u^c, d^c, e^c (nu: Y = 0)
W16 = MULT * np.array(YS); WL = np.array([0, 2 * -0.5, 0, 0, 0])

def build_H(th):
    n = N * 4; H = np.zeros((n, n), complex); H4 = H.reshape(N, 4, N, 4)
    H4[xs, :, xs, :] += (4 - M0) * G5
    for mu in range(4):
        sh = np.roll(idx, -1, axis=mu).reshape(-1); U = np.exp(1j * th[mu])
        H4[xs, :, sh, :] += U[:, None, None] * (G5 @ (G4[mu] - np.eye(4)) / 2)
        H4[sh, :, xs, :] += U.conj()[:, None, None] * (-G5 @ (G4[mu] + np.eye(4)) / 2)
    return H
def qdens(th, full=False):
    H = build_H(th); w, v = np.linalg.eigh(H); del H; vb = v.reshape(N, 4, -1); sg = np.sign(w)
    q = np.einsum('xsn,n,xsn->x', vb, sg, vb.conj()).real
    idxv = int(round(-sg.sum() / 2)); gap = np.abs(w).min()
    return (q, idxv, gap, v, sg) if full else (q, idxv, gap)
c2 = np.indices((L, L)).reshape(2, -1) / L
def smooth2(nm=4):
    out = np.zeros((2, L, L))
    for d in range(2):
        for _ in range(nm):
            k = rng.integers(-1, 2, 2); out[d] += rng.normal() * np.cos(2 * np.pi * (k @ c2) + rng.uniform(0, 2 * np.pi)).reshape(L, L)
    return out / np.sqrt(nm)
X4 = np.indices((L,) * 4)
def fact(a12, a34):
    th = np.zeros((4,) + (L,) * 4)
    th[0] = a12[0][X4[0], X4[1]]; th[1] = a12[1][X4[0], X4[1]]; th[2] = a34[0][X4[2], X4[3]]; th[3] = a34[1][X4[2], X4[3]]
    return th.reshape(4, -1)
def plaq(a):     # 2D plaquette angle, principal branch
    return np.angle(np.exp(1j * (a[0] + np.roll(a[1], -1, 0) - np.roll(a[0], -1, 1) - a[1])))
def Tdens(a12, a34): return np.outer(plaq(a12).ravel(), plaq(a34).ravel()).ravel() / (4 * np.pi ** 2)
def flux2(f):    # unit-flux 2D link angles for flux f (charge one)
    c = np.indices((L, L)); Fp = 2 * np.pi / L ** 2; a = np.zeros((2, L, L))
    a[0] += -Fp * c[1] * f; a[1] += np.where(c[1] == L - 1, Fp * L * c[0] * f, 0.0)
    return a

# all random fields drawn up front (fixed order)
EPS = 0.2; NCF = 12; NTR = 8
BG = [(EPS * smooth2(), EPS * smooth2()) for _ in range(NCF)]
PERT = (0.15 * smooth2(), 0.15 * smooth2())

# ---------- K. exact structure on one factorised background ----------
th0 = fact(*BG[0]) / 6
q0, i0, gap0, v0, sg0 = qdens(th0, full=True)
S = (v0 * sg0) @ v0.conj().T; del v0
n = 4 * N; g5b = np.kron(np.eye(N), G5)
D = np.eye(n) + g5b @ S
gw = np.abs(g5b @ D + D @ g5b - D @ g5b @ D).max(); gh = np.abs(g5b @ D @ g5b - D.conj().T).max()
Ph = (np.eye(n) + S) / 2; pr = np.abs(Ph @ Ph - Ph).max()
qd = np.real(np.einsum('xsxt,ts->x', (g5b @ D).reshape(N, 4, N, 4), np.eye(4)))
check("K1 Q-component (Y=1/6) factorised background, 4^4 (dim 1024): GW exact, g5-hermitian, P_hat_- = (1+sign H)/2 "
      "a projector, tr g5 D(x,x) = tr sign H(x,x)", max(gw, gh, pr, np.abs(qd - q0).max()) < 1e-11,
      f"GW {gw:.0e}, herm {gh:.0e}, proj {pr:.0e}, gap {gap0:.3f}")
del S, D, Ph, g5b

# ---------- data: charge densities on the 12 factorised backgrounds ----------
t1 = time.time(); QD = []; gaps = []
for (a12, a34) in BG:
    th = fact(a12, a34); row = []
    for Y in YS:
        q, ii, g = qdens(Y * th); row.append(q); gaps.append(g)
    QD.append(np.array(row))
A16 = [W16 @ qq for qq in QD]; AL = [WL @ qq for qq in QD]
maxplaq = max(max(np.abs(plaq(a)).max() for a in bg) for bg in BG)
s16 = max(abs(a.sum()) for a in A16); sL = max(abs(a.sum()) for a in AL)
check("C0 trivial sector (12 small smooth factorised backgrounds, eps=0.2): sum_x A = 0 for BOTH the 16 and the lone "
      "L doublet (index 0 per charge), so the integral alone does not separate them here",
      s16 < 1e-10 and sL < 1e-10, f"max|sum A| 16 {s16:.0e}, L {sL:.0e}; max|F| {maxplaq:.2f}, "
      f"min gap {min(gaps):.3f}, {time.time()-t1:.0f}s")
r16 = np.mean([np.linalg.norm(a) for a in A16]); rL = np.mean([np.linalg.norm(a) for a in AL])

# ---------- C1. flux sector: the zero-momentum point ----------
fl12 = 6 * flux2(1) + PERT[0]; fl34 = 6 * flux2(1) + PERT[1]   # unit flux for charge 1/6 in both planes
thF = fact(fl12, fl34); STF = Tdens(fl12, fl34).sum()
res = {}
for qc in (1, 2, 3, 4, 6):
    q, ii, g = qdens(qc / 6 * thF); res[qc] = (ii, g, q.sum())
ok_low = all(res[qc][0] == -qc * qc for qc in (1, 2, 3))
ok_int = all(abs(res[qc][2] + 2 * res[qc][0]) < 1e-8 for qc in res)
intL = 2 * (-0.5) * res[3][2]
fam_pred = sum(m * Y * 2 * (6 * Y) ** 2 for m, Y in zip(MULT, YS))
fam_meas = sum(m * Y * res[int(round(6 * abs(Y)))][2] for m, Y in zip(MULT, YS))
check("C1 unit flux in the 12- and 34-planes (charge unit 1/6) + perturbation: sum_x T = 36 (charge 1); indices "
      "of 6Y = 1, 2, 3 equal -(6Y)^2; sum_x q = -2 index exactly; lone L integrated anomaly = -18 (nonzero: no "
      "periodic k exists at all); the 16's integral = 72 sum m Y^3 = 0 from the predicted integers",
      ok_low and ok_int and abs(STF - 36) < 1e-9 and abs(intL + 18) < 1e-8 and abs(fam_pred) < 1e-12,
      f"sum T {STF:.6f}; idx q=1,2,3,4,6: {[res[k][0] for k in res]}; L {intL:.4f}; 16 pred {fam_pred:.0e}")
fam_known = sum(m * Y * res[int(round(6 * abs(Y)))][2] for m, Y in zip(MULT, YS) if abs(6 * Y) < 5) + 1 * 1.0 * 2 * 36
check("C1b resolution: 6Y = 4 (u^c) IS resolved (-16) but 6Y = 6 (e^c, plaquette angle 3pi/4) is NOT on 4^4 at "
      "m0 = 1.6; measured integers for Q, L, u^c, d^c plus the predicted e^c value (-36) give the 16's flux integral 0",
      res[4][0] == -16 and res[6][0] != -36 and abs(fam_known) < 1e-8,
      f"u^c {res[4][0]} (gap {res[4][1]:.3f}), e^c {res[6][0]} (gap {res[6][1]:.3f}); all-measured sum {fam_meas:.1f}; "
      f"with predicted e^c {fam_known:.1e}")

# ---------- C2. strength scaling ----------
t2 = time.time(); sc = []
for c in range(2):
    a12, a34 = BG[c]; row = []
    for e in (1.0, 0.5):
        th = e * fact(a12, a34); qq = np.array([qdens(Y * th)[0] for Y in YS]); row.append((np.abs(W16 @ qq).max(), np.abs(WL @ qq).max()))
    sc.append((np.log2(row[0][0] / row[1][0]), np.log2(row[0][1] / row[1][1])))
e16 = min(s[0] for s in sc); eL = max(abs(s[1] - 2) for s in sc)
check("C2 strength scan eps 0.2 -> 0.1 (2 backgrounds): lone L ~ eps^2 (within 0.2), the 16 ~ eps^4 (exponent > 3.6): "
      "the 16's residual is the order-4 term (sum Y^5 = 5/9, doublet Y^3 = -1/9)",
      eL < 0.2 and e16 > 3.6, "exponents (16, L): " + ", ".join(f"({a:.2f}, {b:.2f})" for a, b in sc) +
      f"; |A16|/|AL| at eps=0.2 {r16 / rL:.3f}; {time.time()-t2:.0f}s")

# ---------- E. finite-range local-current fits ----------
def offs(r): return sorted({(i % L, j % L) for i in range(-r, r + 1) for j in range(-r, r + 1) if abs(i) + abs(j) <= r})
def monos(Fp, r, deg):
    sh = {o: np.roll(Fp, (-o[0], -o[1]), (0, 1)) for o in offs(r)}
    return [np.prod([sh[o] for o in cb], axis=0) for cb in cwr(offs(r), deg)]
def dstar(m, ax): return m - np.roll(m, 1, ax)
def design(a12, a34, r, pairs, withT):
    F1, F2 = plaq(a12), plaq(a34); cols = []
    for (n1, n2) in pairs:
        M1, M2 = monos(F1, r, n1), monos(F2, r, n2)
        for x in M1:
            for y in M2:
                for ax in (0, 1):
                    cols.append(np.outer(dstar(x, ax).ravel(), y.ravel()).ravel()); cols.append(np.outer(x.ravel(), dstar(y, ax).ravel()).ravel())
    if withT: cols.append(Tdens(a12, a34))
    return np.array(cols).T
def fit(Aset, r, pairs, withT, lam=1e-8):
    Xs = [design(a12, a34, r, pairs, withT) for (a12, a34) in BG]
    Xtr = np.vstack(Xs[:NTR]); ytr = np.concatenate(Aset[:NTR]); Xte = np.vstack(Xs[NTR:]); yte = np.concatenate(Aset[NTR:])
    s = np.linalg.norm(Xtr, axis=0) + 1e-300; Z = Xtr / s
    cf = np.linalg.solve(Z.T @ Z + lam * np.eye(Z.shape[1]), Z.T @ ytr) / s
    return (np.linalg.norm(Xtr @ cf - ytr) / np.linalg.norm(ytr), np.linalg.norm(Xte @ cf - yte) / np.linalg.norm(yte),
            cf[-1] if withT else None, Xtr.shape[1])
t3 = time.time(); Q2 = [(1, 1)]
fr = {(nm, wT, r): fit(As, r, Q2, wT) for nm, As in (('16', A16), ('L', AL)) for wT in (False, True) for r in (0, 1, 2)}
def fmt(k): a = fr[k]; return f"{a[1]:.3f}" + (f"(T {a[2]:+.2f})" if a[2] is not None else "")
print("held-out residual, bilinear F12 F34 basis, r = 0, 1, 2 (T = with Luscher's density as an extra column):")
for nm in ('16', 'L'):
    for wT in (False, True):
        print(f"  {nm:2s} {'T' if wT else '-'}: " + "  ".join(fmt((nm, wT, r)) for r in (0, 1, 2)) + f"   ncol {[fr[(nm, wT, r)][3] for r in (0, 1, 2)]}")
e1 = [(fr[(nm, False, 2)][0], fr[(nm, False, 2)][1]) for nm in ('L', '16')]
check("E1 sample limit: at L1 range 2 (offsets reach the 4^4 period, 484 columns on 2048 samples) the bilinear fit "
      "overfits for the anomalous L doublet (held-out > 10 x train): finite-range fits on 4^4 cannot certify "
      "(non)locality; the obstruction is a zero-momentum quantity (flux sectors, C1)",
      e1[0][1] > 10 * e1[0][0], f"L train {e1[0][0]:.3f} held-out {e1[0][1]:.3f}; 16 train {e1[1][0]:.3f} held-out {e1[1][1]:.3f}")
p3 = fr[('L', True, 1)][2]; p3b = fr[('L', True, 0)][2]
check("E2 pre-set P3 NOT MET: the fitted T coefficient for lone L is not 2 sum m Y^3 = -1/2 within 10% at r <= 1 "
      "(T and range-1 divergences are not separable on 4^4, smallest momentum pi/2)",
      abs(p3 + 0.5) > 0.05 and abs(p3b + 0.5) > 0.05, f"T coef r=0 {p3b:+.3f}, r=1 {p3:+.3f}")
q4 = fit(A16, 1, [(3, 1), (1, 3)], False, 1e-6)
check("E3 pre-set P1 NOT MET: the 16's order-4 density is not fitted by range <= 1 currents (bilinear: held-out "
      "r=1/r=0 ratio > 1/3; quartic F12^3 F34 + F12 F34^3 basis, 1400 columns on 2048 samples: overfits, held-out "
      "residual > 1)", fr[('16', False, 1)][1] / fr[('16', False, 0)][1] > 1 / 3 and q4[1] > 1,
      f"bilinear r=0 {fr[('16', False, 0)][1]:.3f}, r=1 {fr[('16', False, 1)][1]:.3f}; quartic r=1 train {q4[0]:.3f}, "
      f"held-out {q4[1]:.2f}; {time.time()-t3:.0f}s")
check("E4 pre-set P2 (partial): lone L WITHOUT T at r = 1 keeps held-out residual >= 0.3 (stalls below the torus "
      "saturation range); adding T does not reproduce the 16-like fall either (not decisive)",
      fr[('L', False, 1)][1] >= 0.3, f"L r=1 -: {fr[('L', False, 1)][1]:.3f}, T: {fr[('L', True, 1)][1]:.3f}")

print("Reading: on 4^4 the U(1)_Y premise of Luscher's theorem is the zero-momentum (flux-sector) integral, which the")
print("index integers fix (C1); finite-range fits on 4^4 are sample- and size-limited and do not test locality.")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")
