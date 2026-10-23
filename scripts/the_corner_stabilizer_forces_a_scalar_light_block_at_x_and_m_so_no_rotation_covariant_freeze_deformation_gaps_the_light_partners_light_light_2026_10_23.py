AUDIT_INPUT_PATHS = ('docs/THE_CORNER_STABILIZER_FORCES_A_SCALAR_LIGHT_BLOCK_AT_X_AND_M_SO_NO_ROTATION_COVARIANT_FREEZE_DEFORMATION_GAPS_THE_LIGHT_PARTNERS_LIGHT_LIGHT_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""freeze-gapped-partners: is there a T-covariant (12 tetrahedral rotations) deformation of the FREEZE walk whose
light-labelled (tau3 = +1 on Pi+) sector has nodes ONLY at the light Weyls K = 0 and R, i.e. the X/M light
partners gapped light-light?  Self-contained, seeded.  Rebuilds CL-1's 2^3 cell, the site-gauged rotations V,
CTWIST and FREEZE exactly as in twist-local-single / freeze-mirror-smg, then:
  A. exact Schur: X and M are fixed by the D2 subgroup, whose lift (Q8) acts irreducibly on the light doublet,
     so ANY T-covariant walk has a scalar light-labelled block at X and M;
  B. random T-covariant deformations (finite diagnostic of A) and the designed light-light scalar term;
  C. node chirality bookkeeping of the light-labelled projection (polar part) of FREEZE.
"""
import itertools as it
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm, null_space, logm
from scipy.optimize import minimize

AUDIT_TIMEOUT_SEC = 60
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

XP = np.array([np.pi, 0, 0]); MP = np.array([np.pi, np.pi, 0])
D2 = [n for n in V if np.allclose(ROTS[n], np.diag(np.diag(ROTS[n])))]


def polar(C):
    W, s, Vh = np.linalg.svd(C); return W @ Vh, s.min()


def comp(Uf, K, B=BL):
    return B.conj().T @ Uf(K) @ B


print("== A. exact Schur at the D2-fixed corners ==")
lT = max(np.linalg.norm(V[n] @ PLl @ V[n].T - PLl) for n in V)
fixd = all(np.allclose(np.mod(ROTS[n] @ P - P + np.pi, 2 * np.pi) - np.pi, 0) for n in D2 for P in (XP, MP))
Mq = [BL.conj().T @ V[n] @ BL for n in D2]
cdim = nullsp([np.kron(m, np.eye(2)) - np.kron(np.eye(2), m.T) for m in Mq]).shape[1]
check("A1 X=(pi,0,0) and M=(pi,pi,0) are fixed (mod 2pi) by the 4 diagonal rotations D2 of T; the light label "
      "is V-invariant and D2 acts on it with a 1-dim commutant (Q8 spinor, irreducible)",
      fixd and lT < 1e-9 and cdim == 1, f"label res {lT:.0e}, commutant dim {cdim}")
cX, cM = comp(UF, XP), comp(UF, MP)
check("A2 FREEZE: light-labelled block is scalar at X and M (1/3 and -1/3): polar part = +1 at X, -1 at M, "
      "so X sits at quasienergy 0 and M at pi",
      np.allclose(cX, cX[0, 0] * np.eye(2)) and np.allclose(cM, cM[0, 0] * np.eye(2))
      and abs(cX[0, 0] - 1 / 3) < 1e-9 and abs(cM[0, 0] + 1 / 3) < 1e-9,
      f"C(X)={cX[0,0]:.4f}, C(M)={cM[0,0]:.4f}")

print("== B. deformations ==")
NV = [np.zeros(3)] + [s * np.eye(3)[i] for i in range(3) for s in (1, -1)] + \
     [np.array(v, float) for v in it.product([1, -1], repeat=3)]


def mkH(seed):
    r = np.random.default_rng(seed)
    hs = [(r.normal(size=(8, 8)) + 1j * r.normal(size=(8, 8))) / 4 for _ in NV]

    def H(K):
        M = sum(h * np.exp(1j * n @ K) for h, n in zip(hs, NV)); return M + M.conj().T

    return lambda K: sum(V[n].T @ H(ROTS[n] @ K) @ V[n] for n in V) / len(V)


worst_cov = worst_sc = 0; qX = []
for sd in (11, 12, 13):
    Hc = mkH(sd); Ud = (lambda Hc: lambda K: UF(K) @ expm(0.7j * Hc(K)))(Hc)
    for K in kt:
        for n in V:
            worst_cov = max(worst_cov, np.linalg.norm(V[n] @ Ud(K) @ V[n].T - Ud(ROTS[n] @ K)))
    for P in (XP, MP, np.array([0, np.pi, np.pi])):
        c = comp(Ud, P); worst_sc = max(worst_sc, np.linalg.norm(c - np.trace(c) / 2 * np.eye(2)))
    qX.append(np.angle(np.trace(comp(Ud, XP))))
check("B1 (diagnostic of A) 3 random T-covariant deformations U_F exp(i H_cov) (H_cov = rotation-twirled random "
      "range-sqrt3 Bloch Hamiltonian on all 8 cell modes, light-mirror and Pi+/Pi- mixing included): covariant, "
      "and the light-labelled block at X, M, M' is still exactly scalar",
      worst_cov < 1e-9 and worst_sc < 1e-9,
      f"cov res {worst_cov:.0e}, non-scalar part {worst_sc:.0e}; light phase at X {np.round(qX,3).tolist()}")

phi = lambda K: 3 - (np.cos(K[0]) * np.cos(K[1]) + np.cos(K[1]) * np.cos(K[2]) + np.cos(K[2]) * np.cos(K[0]))
T3P = tau3 @ Pp
cres = np.linalg.norm(tau3 @ chi - chi @ tau3) + max(np.linalg.norm(V[n] @ T3P @ V[n].T - T3P) for n in V)
print(f"  light-light scalar layer exp(i a phi(K) tau3 Pi+), phi = 3 - sum cos cos: phi(0)=phi(R)=0, "
      f"phi(X)=phi(M)=4; T-invariant (res {cres:.0e})")
for a in (0.1, 0.25):
    Ua = (lambda a: lambda K: UF(K) @ expm(1j * a * phi(K) * T3P))(a)
    same = max(np.linalg.norm(Ua(P) - UF(P)) for P in (np.zeros(3), RN))
    ss = np.linspace(0.02, 1, 400); th = []
    for s in ss:
        P_, _ = polar(comp(Ua, s * XP)); th.append(np.sort(np.angle(np.linalg.eigvals(P_))))
    th = np.array(th); lo = th[:, 0]
    cross = ss[np.where(np.diff(np.sign(lo)) != 0)[0]]
    thX = np.angle(np.linalg.eigvals(polar(comp(Ua, XP))[0]))
    check(f"B2 a={a}: light Weyls at 0 and R untouched; the X light level is still 2-fold, moved to "
          f"quasienergy 4a, and the lower light band crosses quasienergy 0 on the line 0->X (a Fermi surface)",
          same < 1e-12 and np.allclose(thX, 4 * a) and len(cross) >= 1,
          f"U-U_F at nodes {same:.0e}; X phases {np.round(thX,3).tolist()}; 0-crossing at s = "
          f"{np.round(cross,3).tolist()} of 0->X")

print("== C. chirality bookkeeping of the light-labelled projection (polar part) ==")


def charge(Uf, K0, B, sB):
    P0 = polar(comp(Uf, K0, B))[0]; M = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3); d[j] = hh
        Aj = 1j * (polar(comp(Uf, K0 + d, B))[0] - polar(comp(Uf, K0 - d, B))[0]) / (2 * hh) @ P0.conj().T
        for i in range(3):
            M[i, j] = np.trace(Aj @ sB[i]).real / 2
    return int(np.sign(np.linalg.det(M)))


CORN = [np.array(c, float) * np.pi for c in it.product([0, 1], repeat=3)]
res = {}
for lab, B, sB in (("light", BL, sL), ("mirror", BR, sR)):
    n0 = npi = 0; rows = []
    for P in CORN:
        q = charge(UF, P, B, sB); e = np.real(np.trace(comp(UF, P, B))) > 0
        n0 += int(q * e); npi += int(q * (not e)); rows.append(f"{int(P.sum()/np.pi)}{'0' if e else 'pi'}:{q:+d}")
    res[lab] = (n0, npi); print(f"  {lab}: (#pi entries, quasienergy: sign) " + " ".join(rows))
check("C1 light-labelled projection: Gamma and R carry one sign, the 3 X (quasienergy 0) and 3 M (pi) the "
      "opposite; net light chirality +-2 at quasienergy 0 and the same at pi; mirror net is opposite",
      abs(res['light'][0]) == 2 and res['light'][0] == res['light'][1] and res['mirror'][0] == -res['light'][0],
      f"net (0, pi): light {res['light']}, mirror {res['mirror']}")
print("verdict: no T-covariant deformation gives the light-labelled sector nodes only at 0 and R: Q8 forces a")
print("scalar light block at X and M, so a light partner stays there as a node at 0/pi, a Fermi surface, or")
print("a zero. Light-light partner masses do not exist; partner release under mirror gapping is generic.")
print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
