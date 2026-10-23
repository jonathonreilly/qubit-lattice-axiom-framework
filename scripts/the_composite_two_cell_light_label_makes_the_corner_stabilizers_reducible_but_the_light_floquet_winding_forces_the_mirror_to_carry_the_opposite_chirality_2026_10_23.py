AUDIT_INPUT_PATHS = ('docs/THE_COMPOSITE_TWO_CELL_LIGHT_LABEL_MAKES_THE_CORNER_STABILIZERS_REDUCIBLE_BUT_THE_LIGHT_FLOQUET_WINDING_FORCES_THE_MIRROR_TO_CARRY_THE_OPPOSITE_CHIRALITY_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""two-cell-light-label: escape 1 of freeze-gapped-partners.  Define the light label on a DOUBLED cell (2x2x2 cells =
4^3 sites) by folding FREEZE's composite light label, keep the 12 tetrahedral rotations about the block centre and
the doubled translations, and test: (A) are the doubled-zone corner stabilizers reducible on the light space, and
which light-light pairings does Schur allow at the zone centre; (B) the Floquet 3D winding of the light and mirror
sectors (the bookkeeping that any relabelling must respect).  Self-contained, seeded.  Rebuilds CL-1's 2^3 cell,
the site-gauged rotations V, CTWIST and FREEZE exactly as in freeze-gapped-partners.
"""
import itertools as it
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm, null_space, logm
from scipy.optimize import minimize

AUDIT_TIMEOUT_SEC = 90
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


# ---------- doubled cell (2x2x2 cells = 4^3 sites); rotations about the BLOCK centre c = (1/2,1/2,1/2) cells ----------
NS = list(it.product([0, 1], repeat=3))


def fold(Q):
    return [Q / 2 + np.pi * np.array(n) for n in NS]


def tvec(n, centre):
    R = ROTS[n]; c = 0.5 * np.ones(3) if centre == "block" else np.zeros(3)
    return np.rint(c - R @ c)


def O_rot(n, Q, Qp, centre="block"):
    """64x64 action of rotation n from fold(Q) to fold(Qp) (Qp = R Q mod 2pi): cells x -> R x + t."""
    R = ROTS[n]; t = tvec(n, centre); O = np.zeros((64, 64), complex)
    for a, K in enumerate(fold(Q)):
        Kp = R @ K
        b = [j for j, K2 in enumerate(fold(Qp)) if np.allclose(np.mod(Kp - K2 + np.pi, 2 * np.pi) - np.pi, 0, atol=1e-9)]
        assert len(b) == 1
        O[8 * b[0]:8 * b[0] + 8, 8 * a:8 * a + 8] = np.exp(-1j * Kp @ t) * V[n]
    return O


def UD(Uf, Q):
    M = np.zeros((64, 64), complex)
    for a, K in enumerate(fold(Q)):
        M[8 * a:8 * a + 8, 8 * a:8 * a + 8] = Uf(K)
    return M


def stab(Q):
    return [n for n in V if np.allclose(np.mod(ROTS[n] @ Q - Q + np.pi, 2 * np.pi) - np.pi, 0, atol=1e-9)]


def ndim(rows):  # null-space dimension via the Gram matrix (avoids a full SVD of the tall stack)
    G = sum(r.conj().T @ r for r in rows); ev = np.linalg.eigvalsh(G)
    return int(np.sum(ev < 1e-9 * max(1.0, ev.max())))


def comm_dim(mats, d):
    return ndim([np.kron(m, np.eye(d)) - np.kron(np.eye(d), m.T) for m in mats])


def inter_dim(MA, MB):  # dim of {Z: MB Z = Z MA}
    dA, dB = MA[0].shape[0], MB[0].shape[0]
    return ndim([np.kron(mb, np.eye(dA)) - np.kron(np.eye(dB), ma.T) for ma, mb in zip(MA, MB)])


LD = np.zeros((64, 16), complex)
for a in range(8):
    LD[8 * a:8 * a + 8, 2 * a:2 * a + 2] = BL
print("== A. doubled-cell stabilizers on the composite (folded) light label ==")
Qr = rng.uniform(-np.pi, np.pi, 3); cres = 0
for n in V:
    Qp = ROTS[n] @ Qr; O = O_rot(n, Qr, Qp)
    cres = max(cres, np.linalg.norm(O @ UD(UF, Qr) @ O.conj().T - UD(UF, Qp)), np.linalg.norm(O @ O.conj().T - np.eye(64)))
check("A0 the doubled-cell walk (FREEZE on 4^3 blocks) is covariant under the 12 rotations about the block centre, "
      "and the composite light label (rank 16) is rotation invariant", cres < 1e-9, f"res {cres:.0e}")
QD = {"Gamma_D": np.zeros(3), "X_D": np.array([np.pi, 0, 0]), "M_D": np.array([np.pi, np.pi, 0]), "R_D": np.pi * np.ones(3)}
rows = []; okA = True
for nm, Q in QD.items():
    st = stab(Q); dims = []
    for cen in ("block", "cell"):
        Ms = [LD.conj().T @ O_rot(n, Q, Q, cen) @ LD for n in st]
        dims.append(comm_dim(Ms, 16))
    rows.append(f"{nm}:|stab|={len(st)},commutant(block,cell)={dims}"); okA &= min(dims) > 1
check("A1 at every doubled-zone corner the stabilizer acts REDUCIBLY on the light label (commutant dim > 1; "
      "single-cell value was 1)", okA, "; ".join(rows))
# zone centre: light at quasienergy 0 = Gamma (n=000) + X (one pi); light at pi = M (two pi) + R
st = stab(np.zeros(3))
Mfull = {cen: [LD.conj().T @ O_rot(n, np.zeros(3), np.zeros(3), cen) @ LD for n in st] for cen in ("block", "cell")}
grp = {"G": [0], "X": [a for a, s in enumerate(NS) if sum(s) == 1], "M": [a for a, s in enumerate(NS) if sum(s) == 2], "R": [7]}


def sub(Ms, blocks):
    ix = [2 * a + j for a in blocks for j in (0, 1)]; return [m[np.ix_(ix, ix)] for m in Ms]


res = {}
for cen in ("block", "cell"):
    Ms = Mfull[cen]
    res[cen] = (comm_dim(sub(Ms, grp["G"] + grp["X"]), 8), comm_dim(sub(Ms, grp["X"]), 6),
                inter_dim(sub(Ms, grp["G"]), sub(Ms, grp["X"])),
                comm_dim(sub(Ms, grp["R"] + grp["M"]), 8), comm_dim(sub(Ms, grp["M"]), 6),
                inter_dim(sub(Ms, grp["R"]), sub(Ms, grp["M"])))
okS = all(r == (6, 3, 1, 6, 3, 1) for r in res.values())
check("A2 zone centre, full 2T: light at quasienergy 0 (Gamma + X-triplet) has commutant 6 = 4+1+1: the X-triplet is "
      "three DISTINCT 2-dim irreps (commutant 3) and exactly one of them shares Gamma's irrep (intertwiner dim 1); "
      "same at pi for R + M-triplet; both rotation centres", okS,
      "(G+X, X, G->X, R+M, M, R->M): " + str(res))
print("  => a T-covariant light-light term at the zone centre is Schur-block-diagonal: it can pair Gamma's Weyl with")
print("     ONE X-combination (killing the protected Weyl) and only shifts the other two X irreps (no partner)")

print("== B. Floquet winding W3 of the light and mirror sectors (FREEZE, polar part) ==")
Lr, Rr = BL.conj().T @ Y, Y.conj().T @ BL
LrM, RrM = BR.conj().T @ Y, Y.conj().T @ BR


def blocks(Kb, L_, R_):
    c, s = np.cos(Kb), np.sin(Kb)
    H = (np.sqrt(2) / 3) * (c[:, 0] + np.conj(w) * c[:, 1] + w * c[:, 2])
    base = [L_ @ R_, L_ @ tp @ R_, L_ @ tp.conj().T @ R_] + [L_ @ g @ R_ / np.sqrt(3) for g in gam[2:]]
    out = (c.sum(1) / 3)[:, None, None] * base[0] + 1j * (H[:, None, None] * base[1] + np.conj(H)[:, None, None] * base[2]
           + sum(s[:, i][:, None, None] * base[3 + i] for i in range(3)))
    return out


def pol_b(C):
    W_, s_, Vh = np.linalg.svd(C); return W_ @ Vh, s_.min(1)


def W3(L_, R_, N=28):
    g = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    Kb = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T
    P0, smin = pol_b(blocks(Kb, L_, R_)); A = []
    for j in range(3):
        d = np.zeros(3); d[j] = 1e-5
        Pp_, _ = pol_b(blocks(Kb + d, L_, R_)); Pm_, _ = pol_b(blocks(Kb - d, L_, R_))
        A.append(np.conj(np.swapaxes(P0, 1, 2)) @ (Pp_ - Pm_) / 2e-5)
    dens = np.trace(A[0] @ (A[1] @ A[2] - A[2] @ A[1]), axis1=1, axis2=2)
    return np.pi * np.mean(dens).real, smin.min()


wl, sl = W3(Lr, Rr); wm, sm = W3(LrM, RrM)
check("B1 light-sector polar unitary is smooth on the whole torus (light block never singular) and its 3D winding "
      "W3 = (1/24pi^2) int tr(U^-1 dU)^3 is -2 = MINUS the net corner chirality at 0 and at pi (+2, +2) (W3 = -n_0 = -n_pi in this sign convention); mirror W3 = +2, total 0",
      sl > 1e-3 and sm > 1e-3 and abs(wl + 2) < 0.05 and abs(wl + wm) < 0.05,
      f"W3 light {wl:+.4f}, mirror {wm:+.4f}; min singular value light {sl:.3f}, mirror {sm:.3f}")
print("  exact (section C of the note): W3 is additive over walk-invariant sectors, a sector gapped at ANY single")
print("  quasienergy has a continuous log so W3 = 0, and -W3 = net chirality at 0 = net chirality at pi.")
print("  target light content (Gamma Weyl at 0, R Weyl at pi, nothing else, chirality -1 each) => W3_light = +1 => the complement")
print("  carries the opposite unit and is gapless at EVERY quasienergy: the mirror carries the opposite chirality.")
print("verdict: the composite two-cell label makes every corner stabilizer reducible (Schur wall moved), but the")
print("light-light pairing it allows only consumes the protected Weyl; the light winding (-2) is conserved by any")
print("light-light term, and the target winding (+1) would leave an ungappable (W3 = -1) mirror.")
print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
