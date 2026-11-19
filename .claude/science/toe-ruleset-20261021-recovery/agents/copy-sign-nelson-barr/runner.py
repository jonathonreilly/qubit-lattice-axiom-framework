#!/usr/bin/env python3
"""copy-sign-nelson-barr (P3 / M2): is CL-1's copy sign s the Nelson-Barr Z2, with the s = -1 copy as the heavy
vector-like partner, so that a spontaneous T-odd, turn-breaking, s-odd vacuum gives J != 0 with theta-bar = 0 at tree?
Supplied: FREEZE cell rebuilt as in family-labels (twist-local-single seed and draw order), CL-1 copy mass M = 0.2;
free 3-family NB toy (real light Yukawas, vector-like mirror mass M as SMG stand-in, s-odd family vectors a, b with
real directions and spontaneous phases); loop proxies; Grassmann zero-mode toy for the SMG vertex. All couplings
seeded (FITTED class). Labels: [T] exact, [F] finite, [S] estimate. Criteria: criteria_pre_run.txt."""
AUDIT_TIMEOUT_SEC = 120
import os, time, math, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, null_space, schur

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg, det=""):
    ok = bool(ok); NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))
w = np.exp(2j * np.pi / 3); I8 = np.eye(8)
# ------------------------------------------------ FREEZE rebuild (twist-local-single, same seed and draw order)
def nullsp(rows): return null_space(np.vstack(rows), rcond=1e-9)
def cm(o): return np.kron(o, I8) - np.kron(I8, o.T)
def axang(R):
    ev, vv = np.linalg.eig(R); n = np.real(vv[:, np.argmin(abs(ev - 1))])
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)); K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return (n if np.allclose(expm(th * K), R) else -n), th
C3d = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
CELL = list(it.product([0, 1], repeat=3)); A = np.array(CELL); IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}
def eta_s(i, a): return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]
def Wl(i, k, odd):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == (1 if odd else 0):
            b = list(a); b[i] = 1 - a[i]; b = tuple(b); ph = np.exp(2j * k[i]) if odd else 1
            M[IDX[b], IDX[a]] = eta_s(i, a) * ph; M[IDX[a], IDX[b]] = eta_s(i, a) * np.conj(ph)
    return M
Re = sum(Wl(i, np.zeros(3), 0) for i in range(3)) / np.sqrt(3)
def U1(k, eps=0.3): return expm(1j * eps * sum(Wl(i, k, 1) for i in range(3)) / np.sqrt(3)) @ expm(-1j * eps * Re)
hh = 1e-6; Av = []
for i in range(3):
    d = np.zeros(3); d[i] = hh; Av.append(1j * (U1(d) - U1(-d)) / (2 * hh))
Ah = [a / np.sqrt(np.trace(a @ a).real / 8) for a in Av]
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]
P = np.zeros((8, 8))
for a in CELL:
    b = tuple(np.rint(C3d @ (np.array(a) - .5) + .5).astype(int)); P[IDX[b], IDX[a]] = 1
for sgn in it.product([1, -1], repeat=8):
    T3 = np.diag(sgn) @ P
    if all(np.allclose(T3 @ U1(k) @ T3.T, U1(C3d @ k)) for k in kt): break
nl, th = axang(C3d)
tt = expm(-1j * th * sum(nl[i] * S[i] for i in range(3))).conj().T @ T3
if not np.allclose(np.linalg.matrix_power(tt, 3), I8, atol=1e-6): tt = -tt
PL = (I8 + chi) / 2; PR = I8 - PL; sig = [2 * s for s in S]
tau3 = (tt - tt.conj().T) / (1j * np.sqrt(3)); tau3 = (tau3 + tau3.conj().T) / 2
Pw = (I8 + tau3) / 2; Pb = I8 - Pw
Cb = nullsp([cm(o) for o in sig + [chi]]); Yr = (Cb @ rng.normal(size=Cb.shape[1])).reshape(8, 8)
tp = np.zeros((8, 8), complex)
for Pq in (PL, PR):
    Zb = Pq @ Pw @ Yr @ Pb @ Pq; tp += Zb / np.sqrt(np.trace(Zb @ Zb.conj().T).real / 2)
tau1 = tp + tp.conj().T; tau2 = -1j * (tp - tp.conj().T); gam = [tau3 @ s for s in sig]
def Uc(K):
    c, s = np.cos(K), np.sin(K); H = (np.sqrt(2) / 3) * (c[0] + np.conj(w) * c[1] + w * c[2])
    return c.sum() / 3 * I8 + 1j * (H * tp + np.conj(H) * tp.conj().T + sum(s[i] * gam[i] for i in range(3)) / np.sqrt(3))
Cm = nullsp([cm(o) for o in sig + [tau1, tau2, tau3]])
for j in range(Cm.shape[1]):
    e = Cm[:, j].reshape(8, 8); a = (e - chi @ e @ chi) / 2
    if np.linalg.norm(a) > 1e-6: Ex = a + a.conj().T; break
Ex = Ex / np.sqrt(np.trace(Ex @ Ex).real / 8); Y = Pw + Pb @ Ex
Pp = (I8 + chi @ tau3) / 2; Pm = I8 - Pp
def UF(K): return Pp @ (Y @ Uc(K) @ Y.conj().T) + Pm @ (1j * tau3)
Pq1, Pq2 = Pp @ (I8 + tau3) / 2, Pp @ (I8 - tau3) / 2            # node labels: tau3 = +1 -> q 1, tau3 = -1 -> q 2 (A1)
from scipy.linalg import logm
ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0: ROTS.append(R)
isT = lambda R: abs(np.trace(R)) < 1e-9 or np.allclose(R, np.diag(np.diag(R)))     # the 12 tetrahedral rotations
kr = [rng.uniform(-np.pi, np.pi, 3) for _ in range(4)]
uni = max(np.linalg.norm(UF(K) @ UF(K).conj().T - I8) for K in kr)
check("A0 [T]", uni < 1e-12, "FREEZE rebuilt (family-labels draw order): unitary, light Pi+ at 0 at K = 0", f"{uni:.0e}")
# ================================================================ (1) the copy sign and s-odd cell operators
print("== (1) copy sign s on FREEZE's cell, K = 0 operators")
We = [Wl(i, np.zeros(3), 0) for i in range(3)]
s = 1j * We[0] @ We[1] @ We[2] @ Re
def UM(K, M=0.2): C = expm(1j * (M / 4) * (I8 - s) @ Re); return C @ UF(K) @ C
Ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(12)]
def tr_anti(U, R, Kset=Ks):
    rows = [np.kron(I8, U(-R @ K).conj().T) - np.kron(U(K).conj().T, I8) for K in Kset]
    N = null_space(np.vstack(rows), rcond=1e-9)
    if N.shape[1] == 0: return None
    V = (N @ (rng.normal(size=N.shape[1]) + 1j * rng.normal(size=N.shape[1]))).reshape(8, 8, order='F')
    sv = np.linalg.svd(V, compute_uv=False)
    return V if sv[-1] / sv[0] > 1e-6 else None
kept = [R for R in ROTS if tr_anti(UM, R) is not None]
z = np.zeros(3); dv = np.array([1, .7, .3])
c0 = np.abs(s @ UM(z) - UM(z) @ s).max(); cK = [np.abs(s @ UM(t * dv) - UM(t * dv) @ s).max() for t in (1e-2, 1e-3)]
crand = max(np.abs(s @ UM(K) - UM(K) @ s).max() for K in Ks[:4])
check("A1 [T]/[F]", np.abs(s @ s - I8).max() < 1e-12 and np.abs(s @ tt - tt @ s).max() < 1e-12 and np.abs(Pp @ (s + tau3) @ Pp).max() < 1e-12
      and c0 < 1e-12 and 80 < cK[0] / cK[1] < 120 and crand > 0.1 and len(kept) == 12,
      "s^2 = 1, s commutes with the turn tt, s = -tau3 on Pi+ (light q 2: s = +1, mirror-copy q 1: s = -1); s commutes with "
      "the tick AT K = 0 only: [s, U(K)] grows as K^2 (dim-5 class), O(1) at generic K. So s is a node label, not an exact "
      "Z2 of the update; 12 kept T x R", f"[s,U(0)] {c0:.0e}; K 1e-2,1e-3: {cK[0]:.1e},{cK[1]:.1e}; generic {crand:.2f}")
HB = []
for i in range(8):
    for j in range(i, 8):
        E = np.zeros((8, 8), complex); E[i, j] = E[j, i] = 1; HB.append(E / (np.sqrt(2) if i != j else 1))
        if i != j: E = np.zeros((8, 8), complex); E[i, j] = -1j; E[j, i] = 1j; HB.append(E / np.sqrt(2))
def space(conds):
    rows = []
    for f in conds:
        Mx = np.array([f(B).reshape(-1) for B in HB]).T; rows += [Mx.real, Mx.imag]
    N = null_space(np.vstack(rows), rcond=1e-9); return [np.tensordot(N[:, k], np.array(HB), 1) for k in range(N.shape[1])]
anti_s = lambda X: s @ X + X @ s; onPp = lambda X: X - Pp @ X @ Pp
sodd = space([anti_s, onPp]); sodd_cell = space([anti_s])
neut = lambda X: np.abs((X + tt @ X @ tt.conj().T + tt.conj().T @ X @ tt) / 3).max()
Kf = [rng.uniform(-np.pi, np.pi, 3) for _ in range(8)]
def canonV(R):
    V = tr_anti(UM, R); u_, _, vh_ = np.linalg.svd(V); return u_ @ vh_
fix = [R for R in kept if abs(np.trace(R) + 1) < 1e-9 and abs(axang(R)[0] @ np.ones(3)) < 1e-9]
Vf = [canonV(R) for R in fix]
oddd = [len(space([anti_s, onPp, lambda X, V=V: V @ X.conj() @ V.conj().T + X])) for V in Vf]
check("B1 [T]", len(sodd) == 8 and max(neut(X) for X in sodd) < 1e-12 and len(sodd_cell) == 32 and oddd == [4, 4, 4],
      "on Pi+ the s-odd Hermitian operators form an 8-dim space (light q 2 <-> mirror q 1), EVERY one turn-charged (turn-neutral "
      "part 0): s-odd => family triality here, as A0 needs. Each family-fixing T x C2' splits it 4 odd + 4 even. 'Odd under all "
      "12' is not a usable test: products of two kept antiunitaries are unitary rotations incl. the turn", f"s-odd dims Pi+/cell "
      f"{len(sodd)}/{len(sodd_cell)}; T x C2'-odd dims {oddd}")
Ogen = sum(rng.normal() * X for X in sodd); Ogen /= np.linalg.norm(Ogen)
def Upert(Op, lam): E = expm(0.5j * lam * Op); return lambda K: E @ UM(K) @ E
kg = [len([R for R in ROTS if tr_anti(Upert(Ogen, lam), R) is not None]) for lam in (0.1, 0.3)]
Oodd1 = space([anti_s, onPp, lambda X: Vf[0] @ X.conj() @ Vf[0].conj().T + X]); O1 = sum(rng.normal() * X for X in Oodd1); O1 /= np.linalg.norm(O1)
Oev = space([anti_s, onPp, lambda X: Vf[0] @ X.conj() @ Vf[0].conj().T - X]); Oe = sum(rng.normal() * X for X in Oev); Oe /= np.linalg.norm(Oe)
k1 = [R for R in ROTS if tr_anti(Upert(O1, 0.3), R) is not None]; ke = [R for R in ROTS if tr_anti(Upert(Oe, 0.3), R) is not None]
kfe = any(np.allclose(R, fix[0]) for R in ke)
check("B2 [F]", kg == [0, 0] and len(k1) == 0 and kfe,
      "a generic s-odd Pi+ vacuum term (symmetric split) keeps NONE of the 24 T x R, nor does a purely T x C2'-odd one; control: "
      "a T x C2'(1,-1,0)-even s-odd term keeps that element. So (1a) EXISTS: s-odd, turn-charged, breaking every family-fixing "
      "antiunitary", f"kept: generic lam .1/.3 {kg}; odd {len(k1)}; even-control {len(ke)} (keeps C2'(1-10): {kfe})")
# ================================================================ (2) free 3-family Nelson-Barr toy
print("== (2) NB toy: light (s=+1), mirror (s=-1), vector-like M = 1, F = u a^T + v b^T")
def jarl(Hu, Hd):
    _, Uu = np.linalg.eigh(Hu); _, Ud = np.linalg.eigh(Hd); Vc = Uu.conj().T @ Ud
    return np.imag(Vc[0, 0] * Vc[1, 1] * np.conj(Vc[0, 1]) * np.conj(Vc[1, 0]))
def dpi(z): t = np.angle(z) % np.pi; return min(t, np.pi - t)
I3 = np.eye(3); MD = 1.0; eps_m = 1e-2
def draw():
    mu, md = eps_m * rng.normal(size=(3, 3)), eps_m * rng.normal(size=(3, 3))
    u, v, ra, rb = (rng.normal(size=3) for _ in range(4)); al, be = rng.uniform(0, 2 * np.pi, 2)
    return mu, md, u, v, ra / np.linalg.norm(ra), rb / np.linalg.norm(rb), al, be
def build(p, x, G=None, bzero=False, same=False):
    mu, md, u, v, ra, rb, al, be = p; be = al if same else be
    F = x * MD * (np.outer(u, ra * np.exp(1j * al)) + (0 if bzero else 1) * np.outer(v, rb * np.exp(1j * be))) / np.sqrt(2)
    Gb = np.zeros((3, 3)) if G is None else G(F)
    Mf = np.block([[md, Gb], [F, MD * I3]])
    Hd = md @ np.linalg.inv(I3 + F.conj().T @ F / MD ** 2) @ md.T
    return Mf, mu @ mu.T, Hd, F
XS = (0.3, 0.5, 1, 2, 3); PS = [draw() for _ in range(300)]
th = 0.0; Jmed = []
for x in XS:
    Js = []
    for p in PS:
        Mf, Hu, Hd, F = build(p, x); th = max(th, dpi(np.linalg.det(Mf)), dpi(np.linalg.det(p[0])))
        Js.append(abs(jarl(Hu, Hd)))
    Jmed.append(np.median(Js))
check("C1 [T]", th < 1e-12, "NB block (light_L x mirror_R entry G = 0): arg det of the full 6x6 down matrix and of M_u lie in "
      "{0, pi} for every vacuum phase: det = det(m_d) M^3 (theta-bar_tree = 0 or pi; sign of det m is a discrete choice)", f"max dist {th:.0e}")
check("C2 [F]", min(Jmed) > 1e-5, "integrating out the mirror, m_eff m_eff^+ = m (1 + F^+F/M^2)^-1 m^T is complex: median |J| "
      "> 1e-5 at every |a|/M in [0.3, 3]", "median |J|: " + ", ".join(f"{x}:{j:.1e}" for x, j in zip(XS, Jmed)))
Jsm = [np.median([abs(jarl(*build(p, x)[1:3])) for p in PS[:100]]) for x in (0.01, 0.1, 1)]
check("C3 [F]", Jsm[0] / Jsm[2] < 1e-2 and 50 < Jsm[1] / Jsm[0] < 200, "J -> 0 as |a|/M -> 0, as (|a|/M)^2: NB's coincidence "
      "(J unsuppressed only for |a| ~ M)", f"median |J| at 0.01/0.1/1: {Jsm[0]:.1e}/{Jsm[1]:.1e}/{Jsm[2]:.1e}")
j0 = max(max(abs(jarl(*build(p, 1, bzero=True)[1:3])), abs(jarl(*build(p, 1, same=True)[1:3]))) for p in PS[:100])
check("C4 [T]", j0 < 1e-14, "controls: one s-odd vector (b = 0) or equal phases: |J| = 0 (phase removed by mirror rephasing): "
      "two s-odd fields with a relative spontaneous phase are needed", f"max |J| {j0:.0e}")
thB = []; nl = []
for p in PS[:200]:
    Mf, _, _, F = build(p, 1, G=lambda F: F.T); thB.append(dpi(np.linalg.det(Mf)))
    M0 = np.block([[np.zeros((3, 3)), F.T], [F, MD * I3]]); nl.append(int(np.sum(np.linalg.svd(M0, compute_uv=False) < 1e-9)))
FA = build(PS[0], 1)[3]; nlA = int(np.sum(np.linalg.svd(np.block([[np.zeros((3, 3)), np.zeros((3, 3))], [FA, MD * I3]]), compute_uv=False) < 1e-9))
check("C5 [T]/[F]", np.median(thB) > 0.1 and max(nl) == 1 and nlA == 3,
      "Spin(10) reading: the unique 16 x 16bar singlet pairs Q with Q' AND d^c with d'^c, so G = F^T: theta_tree generic O(1) "
      "(NB lost) and at m = 0 only 1 of 3 light families stays massless (vacuum gives light doublets mass ~|a|). s alone does "
      "NOT forbid G: both blocks are s-odd and carry the same turn charge", f"median theta {np.median(thB):.2f} rad; massless "
      f"families at m = 0: G = F^T {max(nl)}, G = 0 {nlA}")
# ================================================================ (3) one-loop theta-bar proxies
print("== (3) one-loop theta-bar: dM = eps x (s-, gauge-allowed products of tree matrices, real coefficient matrices C)")
def th_loop(p, ep, Cs, x=1.0):
    Mf, _, _, F = build(p, x); md = p[1]; C1, C2, C3 = Cs; Z = np.zeros((3, 3))
    dM = np.block([[md @ C2 @ F.conj().T @ F, md @ C1 @ F.conj().T], [Z, F @ C3 @ F.conj().T]])
    return np.angle(np.linalg.det(Mf + ep * dM) / np.linalg.det(Mf))
thH = max(abs(th_loop(p, 1e-2, (I3, I3, I3))) for p in PS[:100])
sl = []
for p in PS[:100]:
    Cs = [rng.normal(size=(3, 3)) for _ in range(3)]; a1, a2 = th_loop(p, 1e-6, Cs), th_loop(p, 1e-5, Cs)
    sl.append((abs(a2) / 1e-5, abs(a2 / a1) if a1 else 0))
slope = np.median([q[0] for q in sl]); lin = np.median([q[1] for q in sl]); lam_max = 16 * np.pi ** 2 * 1e-10 / slope
check("D1 [T]", thH < 1e-12, "flavour-aligned loop class (C = 1: m F^+F, m F^+ into the G slot, F F^+ on the mirror) keeps arg det "
      "real: Hermitian dressings cancel (a one-loop G = m F^+ is generated but gives det = det m det(M - F F^+))", f"max {thH:.0e}")
check("D2 [F]/[S]", 8 < lin < 12 and slope > 1e-2, "flavour-generic real loop coefficients: theta-bar linear in eps = lam/16pi^2 "
      "with O(1) slope at |a| = M; theta < 1e-10 needs lam <~ 16pi^2 1e-10/slope: the standard NB quality problem, not solved by s",
      f"median slope {slope:.2f}, linearity {lin:.1f}; lam_max ~ {lam_max:.0e}")
# ================================================================ (4) 't Hooft vertex of the SMG-gapped mirror (zero-mode toy)
print("== (4) Grassmann zero-mode toy: d_L, d_R, D_L, D_R (2 each); mirror gapped only by a quartic vertex g e^{i phi}")
def gmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            if ma & mb: continue
            sg = 1
            for j in range(8):
                if mb >> j & 1 and bin(ma >> (j + 1)).count('1') % 2: sg = -sg
            out[ma | mb] = out.get(ma | mb, 0) + sg * ca * cb
    return out
def mono(*ix):
    e = {0: 1.0}
    for i in ix: e = gmul(e, {1 << i: 1.0})
    return e
def amp(m, F, G, g):
    S = {}
    def add(e, c):
        for k, v in e.items(): S[k] = S.get(k, 0) + c * v
    for i in range(2):
        for j in range(2):
            add(mono(i, 2 + j), m[i, j]); add(mono(4 + i, 2 + j), F[i, j]); add(mono(i, 6 + j), G[i, j])
    add(mono(4, 5, 6, 7), g)
    tot, P = {0: 1.0}, {0: 1.0}
    for n in range(1, 5):
        P = gmul(P, S); tot = {k: tot.get(k, 0) + P.get(k, 0) / math.factorial(n) for k in set(tot) | set(P)}
    return tot.get(255, 0)
m2 = rng.normal(size=(2, 2)); Fc = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Gc = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Z2m = np.zeros((2, 2))
A0, AF = amp(m2, Z2m, Z2m, 1.0), amp(m2, Fc, Z2m, 1.0); Aph = amp(m2, Fc, Z2m, np.exp(0.7j)); AG0, AGF = amp(m2, Z2m, Gc, 1.0), amp(m2, Fc, Gc, 1.0)
check("E1 [T]", abs(AF - A0) < 1e-12 and abs(abs(A0) - abs(np.linalg.det(m2))) < 1e-12,
      "G = 0: the instanton amplitude is det(m) x g, independent of the s-odd F to all orders (d_L zero modes can only be "
      "soaked by m, which uses up every d_R): the NB cancellation survives an SMG-only mirror at tree level",
      f"|A(F) - A(0)| {abs(AF - A0):.0e}; |A| {abs(A0):.3f} = |det m| {abs(np.linalg.det(m2)):.3f}")
check("E2 [T]", abs(np.angle(Aph / AF) - 0.7) < 1e-12 and abs(AGF - AG0) > 1e-2,
      "but the vertex phase enters theta-bar one-for-one (theta-bar = theta - arg det m - phi_g per vertex), so the SMG vertex "
      "must be real; with G != 0 the amplitude picks up a g-independent det F det G term (F leaks into theta-bar)",
      f"phase shift {np.angle(Aph / AF):.3f} for phi_g 0.700; |A(F,G) - A(0,G)| {abs(AGF - AG0):.2f}")
# ================================================================ estimates
print("== [S] estimates")
Jl = [np.median([abs(jarl(*build(p, np.sqrt(0.168 ** L))[1:3])) for p in PS[:100]]) for L in (4, 11)]
check("F1 [S]", Jl[1] < 1e-9, "far-termination geometry: light (near wall) x mirror (far wall) overlap weight ~0.168 per layer "
      "(far-termination N4); at |a| = M, Ls = 11 (its Crab-bound depth) J is crushed: the same overlap the leak bound suppresses "
      "suppresses F", f"median |J| Ls 4: {Jl[0]:.0e}, Ls 11: {Jl[1]:.0e}")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}   ({time.time() - T0:.1f} s, peak {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB)")
