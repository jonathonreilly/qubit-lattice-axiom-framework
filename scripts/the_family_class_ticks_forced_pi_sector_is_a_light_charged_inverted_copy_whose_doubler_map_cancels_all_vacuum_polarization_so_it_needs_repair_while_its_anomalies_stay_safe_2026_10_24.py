AUDIT_INPUT_PATHS = ('docs/THE_FAMILY_CLASS_TICKS_FORCED_PI_SECTOR_IS_A_LIGHT_CHARGED_INVERTED_COPY_WHOSE_DOUBLER_MAP_CANCELS_ALL_VACUUM_POLARIZATION_SO_IT_NEEDS_REPAIR_WHILE_ITS_ANOMALIES_STAY_SAFE_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""pi-sector-stability: is the family-class tick's forced quasi-energy-pi sector a physical problem?
 A  doubler S sends the no-Fermi-surface half-filled vacuum to its complement; so every S-even one-body response
    (cell charge under any potential kick, any strength, any tick count) equals the infinite-temperature value: zero
    vacuum polarization. Real space, 4^3 cells. Controls: CL-1's plain tick (gap at pi) screens; S-broken FREEZE responds.
 B  decay channel: zero-quasi-energy, zero-momentum (0-pair + pi-pair) states at every momentum scale; CL-1 needs 6 pairs.
 C  filling: F_pi = W per turn sector (no free pi gap, robust to turn-symmetric deformations); the one-cube start is
    degenerate (no ordering picks the filling); alternation on the axis loop (>= 1 inverted boundary).
 D  anomalies with the pi copy (2 x 16 per family) and the turn count; E measurement estimates (supplied numbers).
Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading. Criteria: criteria_pre_run.txt.
FREEZE is rebuilt inline exactly as mirror-in-time / floquet-pi-slab (same seed, same draw order)."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm, null_space

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

# ------------------------------------------------ shared tools
RV = np.pi * np.ones(3); KS = [rng.uniform(-np.pi, np.pi, 3) for _ in range(12)]
def intertw(U, f, K_map, sign=1.0, conjA=False):
    """on-cell K-independent X with X U(K)^(*) = sign * f(U(K_map(K))) X at 12 random K (column-major vec)."""
    rows = []
    for K in KS:
        Aa = U(K).conj() if conjA else U(K); B_ = sign * f(U(K_map(K)))
        rows.append(np.kron(np.eye(len(Aa)), B_) - np.kron(Aa.T, np.eye(len(Aa))))
    N = null_space(np.vstack(rows), rcond=1e-9)
    if N.shape[1] == 0: return None, 0
    Xr = sum((rng.normal() + 1j * rng.normal()) * N[:, j].reshape(len(Aa), len(Aa), order='F') for j in range(N.shape[1]))
    u_, s_, vh = np.linalg.svd(Xr)
    if s_[-1] / s_[0] < 1e-6: return None, N.shape[1]
    return u_ @ vh, N.shape[1]

rng2 = np.random.default_rng(20261024)                     # all new draws below use rng2 (FREEZE draws untouched)
def U1c(K): return U1(np.asarray(K) / 2)                   # CL-1 plain tick (eps 0.3) in cell momentum K (period 2 pi)
def fill_neg(U, K, n=4):
    """stationary half filling: the n eigenvectors with eigenphase most negative in (-pi, pi]."""
    e, v = np.linalg.eig(U(K)); o = np.argsort(np.angle(e))[:n]
    Q, _ = np.linalg.qr(v[:, o]); return Q @ Q.conj().T
def fill_F(K, branch=-1):
    """FREEZE no-Fermi-surface vacuum: eigenphases in (-pi,0) (branch -1) or (0,pi) (branch +1): 2 light + 2 frozen."""
    e, v = np.linalg.eig(UF(K)); ph = np.angle(e)
    lightv = np.array([np.linalg.norm(Pp @ v[:, j]) > 0.5 for j in range(8)])
    sel = (branch * ph > 0) & (branch * ph < np.pi - 1e-12)
    Q, _ = np.linalg.qr(v[:, sel]); return Q @ Q.conj().T, int(sel.sum()), int((sel & lightv).sum())

# ================================================================ A. response of the vacuum
print("== A. the doubler S maps the vacuum to its complement: zero response")
S_, nS = intertw(UF, lambda M: M, lambda K: K + RV, sign=-1.0)
Kr = [rng2.uniform(-np.pi, np.pi, 3) for _ in range(6)]
resS = max(np.linalg.norm(S_ @ UF(K) @ S_.conj().T + UF(K + RV)) for K in Kr)
comp = max(np.linalg.norm(S_ @ fill_F(K)[0] @ S_.conj().T - (I8 - fill_F(K + RV)[0])) for K in Kr)
cnt = {fill_F(K)[1:] for K in Kr}
check("A1 [T]/[F]", resS < 1e-9 and comp < 1e-9 and cnt == {(4, 2)}, "S U(K) S^-1 = -U(K+R) sends the no-Fermi-surface half filling (light eigenphases in (-pi,0) + one frozen eigenspace) to its COMPLEMENT: S rho(K) S^+ = 1 - rho(K+R)",
      f"S residual {resS:.0e}; complement residual {comp:.0e}; filled/light-filled per K {sorted(cnt)}")
# real space: L^3 cells, twisted grid (uniform vector potential, nodes avoided); the K + R map stays on the grid
L = 4; phi = np.array([0.13, 0.29, 0.41]); cells = list(it.product(range(L), repeat=3)); nc = len(cells)
Kg = [2 * np.pi * (np.array(m) + phi) / L for m in cells]
Fm = np.array([[np.exp(-1j * Kg[a] @ np.array(cells[b])) for b in range(nc)] for a in range(nc)]) / np.sqrt(nc)
FF = np.kron(Fm, I8)
def real(blocks): return FF.conj().T @ blockdiag(blocks) @ FF
def blockdiag(bl):
    M = np.zeros((8 * nc, 8 * nc), complex)
    for a, B in enumerate(bl): M[8 * a:8 * a + 8, 8 * a:8 * a + 8] = B
    return M
stag = np.kron(np.diag([(-1.0) ** sum(c) for c in cells]), I8)
SR = stag @ np.kron(np.eye(nc), S_)
UFr = real([UF(K) for K in Kg])
resR = np.linalg.norm(SR @ UFr @ SR.conj().T + UFr)
f_pot = rng2.normal(size=nc); Vr = np.kron(np.diag(f_pot), I8)
def respond(Ur, rho, lam=0.5, T=24):
    Ul = np.diag(np.exp(-1j * lam * np.diag(Vr))) @ Ur; dmax = 0.0; N0 = np.real(np.diag(rho)).reshape(nc, 8).sum(1)
    for _ in range(T):
        rho = Ul @ rho @ Ul.conj().T
        dmax = max(dmax, np.max(np.abs(np.real(np.diag(rho)).reshape(nc, 8).sum(1) - N0)))
    return dmax, N0
rhoF = real([fill_F(K)[0] for K in Kg]); dF, N0F = respond(UFr, rhoF)
rhoFp = real([fill_F(K, +1)[0] for K in Kg]); dFp, _ = respond(UFr, rhoFp)
check("A2 [T]/[F]", resR < 1e-9 and dF < 1e-9 and dFp < 1e-9 and np.allclose(N0F, 4), "real space (4^3 cells, 512 modes): S is a staggered cell sign x on-cell map and commutes with any cell-charge potential; under kicks e^{-i lam V} (lam 0.5, random V, 24 ticks) the induced cell charge of BOTH no-Fermi-surface vacua is identically 0 (infinite-temperature value): ZERO vacuum polarization",
      f"S residual {resR:.0e}; max |dN| fill(-pi,0) {dF:.0e}, fill(0,pi) {dFp:.0e}")
U1r = real([U1c(K) for K in Kg]); rho1 = real([fill_neg(U1c, K) for K in Kg]); d1, _ = respond(U1r, rho1)
Gr = rng2.normal(size=(8, 8)) + 1j * rng2.normal(size=(8, 8)); Gr = Gr + Gr.conj().T
Godd = (Gr - S_ @ Gr @ S_.conj().T) / 2; Gb = expm(-0.4j * Godd)
def UFb(K): return Gb @ UF(K)
rhoB = real([fill_neg(UFb, K) for K in Kg]); dB, _ = respond(real([UFb(K) for K in Kg]), rhoB)
def fill_bn(K):                                          # both nodes normal: light (-pi/2,0) u (pi/2,pi); inverted Fermi surface at theta = pi/2
    e, v = np.linalg.eig(UF(K)); ph = np.angle(e); lt = np.array([np.linalg.norm(Pp @ v[:, j]) > 0.5 for j in range(8)])
    sel = lt & (((ph > -np.pi / 2) & (ph < 0)) | (ph > np.pi / 2)); Q, _ = np.linalg.qr(v[:, sel]); return Q @ Q.conj().T
bnS = max(np.linalg.norm(S_ @ fill_bn(K) @ S_.conj().T - fill_bn(K + RV)) for K in Kr)
dL, _ = respond(UFr, real([fill_bn(K) for K in Kg]))
check("A3 [F] controls", d1 > 1e-3 and dB > 1e-3 and dL > 1e-3 and bnS < 1e-9, "the zero is the complement property, not a dead probe: CL-1's vacuum (gap at pi) screens; FREEZE with an S-odd on-cell layer responds; FREEZE's both-nodes-normal filling (S-INVARIANT, paid for by an inverted Fermi surface at theta = pi/2) screens",
      f"max |dN|: CL-1 {d1:.2e}; S-broken FREEZE {dB:.2e}; both-normal {dL:.2e} (S-invariance residual {bnS:.0e})")
print("   A4 [S] the cancellation is sector by sector: S maps the 0-sector response of fill(-pi,0) onto the pi-sector response of")
print("      fill(0,pi); the inverted pi copy anti-screens exactly as much as the normal 0 copy screens (Lindhard n -> 1-n).")

# ================================================================ B. decay channel
print("== B. vacuum -> (0-sector pair) + (pi-sector pair) at every scale")
def th(K): return np.arccos(np.clip(np.mean(np.cos(K)), -1, 1))
kk = [rng2.normal(size=3) * 0.05 for _ in range(4)]
disp = 0.0
for k in kk:
    e0 = np.angle(np.linalg.eigvals(UF(k))); eR = np.angle(np.linalg.eigvals(UF(RV + k)))
    l0 = sorted(abs(x) for x in e0 if abs(abs(x) - np.pi / 2) > 1e-6); lR = sorted(np.pi - abs(x) for x in eR if abs(abs(x) - np.pi / 2) > 1e-6)
    disp = max(disp, max(abs(a - th(k)) for a in l0), max(abs(b - th(k)) for b in lR))
sols = []
for s in (1e-1, 1e-2, 1e-3):
    for _ in range(50):
        k1, k2, u = s * rng2.normal(size=3), s * rng2.normal(size=3), rng2.normal(size=3); u /= np.linalg.norm(u)
        f = lambda t: th(k1) + th(k2) - th(t * u) - th(k1 - k2 + t * u)       # 0-pair (+) and pi-pair (-) quasi-energies
        a, b = 0.0, 10 * s
        if f(a) > 0 > f(b):
            for _ in range(80):
                m = (a + b) / 2; a, b = (m, b) if f(m) > 0 else (a, m)
            k3 = a * u; k4 = k1 - k2 + k3; sols.append((s, abs(f(a)), max(map(np.linalg.norm, (k1, k2, k3, k4))) / s)); break
okB = len(sols) == 3 and all(r[1] < 1e-12 for r in sols) and all(r[2] < 12 for r in sols)
check("B1 [T]/[F]", disp < 1e-8 and okB, "pi-sector dispersion is the 0-sector's (pi - theta(R+k) = theta(k)); exact zero-quasi-energy, zero-momentum 4-excitation states (0 pair at +E, pi pair at -E) exist at momentum scales 1e-1, 1e-2, 1e-3: the decay channel is open in the IR",
      f"dispersion residual {disp:.0e}; " + "; ".join(f"scale {r[0]:.0e}: |E_tot| {r[1]:.0e}, max|k|/scale {r[2]:.1f}" for r in sols))
grid = [np.array(m) * 2 * np.pi / 12 for m in it.product(range(12), repeat=3)]
wmax = max(np.max(np.abs(np.angle(np.linalg.eigvals(U1c(K))))) for K in grid)
nmin = int(np.ceil(2 * np.pi / (2 * wmax)))
check("B2 [T]/[F] control", nmin >= 6, "CL-1's plain tick: every particle-hole excitation of the filled-(-pi,0) vacuum has quasi-energy in (0, 2 w_max]; a zero-quasi-energy (mod 2 pi) vacuum transition needs >= n_min pairs, all at cell scale (prethermal); FREEZE needs 2, at any scale",
      f"w_max {wmax:.4f} (2 eps = 0.6); n_min {nmin}")

# ================================================================ C. filling
print("== C. filling: what fixes it, and what cannot be avoided")
ks = np.linspace(0, 2 * np.pi, 721)
ev, evec = np.linalg.eig(T3); lab = np.round(np.angle(ev) / (2 * np.pi / 3)).astype(int) % 3
def sector_winds(U):
    out = []
    for q in range(3):
        B, _ = np.linalg.qr(evec[:, lab == q]); d = [np.linalg.det(B.conj().T @ U(k * np.ones(3)) @ B) for k in ks]
        out.append(int(np.rint((np.unwrap(np.angle(d))[-1] - np.angle(d[0])) / (2 * np.pi))))
    return out
def pi_flow(U):
    """signed eigenphase crossings of pi per turn sector along the axis loop"""
    out = []
    for q in range(3):
        B, _ = np.linalg.qr(evec[:, lab == q]); fl = 0
        prev = np.angle(np.linalg.eigvals(B.conj().T @ U(ks[0] * np.ones(3)) @ B))
        for k in ks[1:]:
            cur = np.angle(np.linalg.eigvals(B.conj().T @ U(k * np.ones(3)) @ B))
            for x in prev:                       # match by nearest on the circle
                y = cur[np.argmin(np.abs(np.angle(np.exp(1j * (cur - x)))))]
                if abs(x) > 2.5 and abs(y) > 2.5 and np.sign(x) != np.sign(y): fl += 1 if x > 0 else -1
            prev = cur
        out.append(fl)
    return out
WF = sector_winds(UF); FpF = pi_flow(UF)
rob = []
for _ in range(3):
    G = rng2.normal(size=(8, 8)) + 1j * rng2.normal(size=(8, 8)); G = G + G.conj().T
    G = sum(np.linalg.matrix_power(T3, j) @ G @ np.linalg.matrix_power(T3, j).conj().T for j in range(3)) / 3
    Gx = expm(-0.15j * G / np.linalg.norm(G, 2)); Ud = lambda K, Gx=Gx: Gx @ UF(K)
    rob.append((sector_winds(Ud), pi_flow(Ud)))
check("C1 [T]/[F]", sorted(WF) == [-2, 1, 1] and FpF == WF and all(r[0] == WF and r[1] == WF for r in rob), "F_pi = W per turn sector: FREEZE's axis flow through pi equals its winding (-2, 1, 1) and stays so under random turn-symmetric deformations, so no free term opens a gap at pi for any family-class tick",
      f"W {WF}; flow at pi {FpF}; deformed (W, F_pi) {rob}")
e0 = np.angle(np.linalg.eigvals(UF(np.zeros(3)))); eR = np.angle(np.linalg.eigvals(UF(RV)))
c0 = int(np.sum(np.abs(e0) < 1e-9)); cR = int(np.sum(np.abs(np.abs(eR) - np.pi) < 1e-9))
fr = int(np.sum(np.abs(np.abs(e0) - np.pi / 2) < 1e-9))
check("C2 [T]", c0 == 4 and cR == 4 and fr == 4, "one-cube start: a single FREEZE cell, periodic (K = 0) or antiperiodic (K = R), puts the 4 light modes at quasi-energy exactly 0 or exactly pi (4-fold) and the frozen 4 at +-pi/2: half filling is degenerate, so no quasi-energy ordering, and no CL-2 clause, picks which sector the carried sea makes normal",
      f"light at 0 (periodic) {c0}; light at pi (antiperiodic) {cR}; frozen at +-pi/2 {fr}")
M = 12; ok6 = True; mins = 99
for bits in range(2 ** M):
    n = [(bits >> i) & 1 for i in range(M)]; n = n + [1 - x for x in n]
    rises = sum(1 for i in range(2 * M) if n[i] == 0 and n[(i + 1) % (2 * M)] == 1)
    drops = sum(1 for i in range(2 * M) if n[i] == 1 and n[(i + 1) % (2 * M)] == 0)
    ok6 &= rises == drops and rises >= 1; mins = min(mins, rises)
check("C3 [T]", ok6 and mins == 1, "alternation: along the axis loop (quasi-energy increasing, +theta out and -theta back), any filling with one of each +-theta pair filled has rises = drops >= 1: at least one INVERTED boundary, minimum exactly one (the -theta vacuum: inverted at pi)",
      f"{2 ** M} fillings checked; min inverted boundaries {mins}")
print("   C4 [S] CL-2 has no ground-state clause: the actual configuration follows the odds, and a free Slater state of Floquet")
print("      eigenvectors is stationary, so the transport stays. The filling is the start-and-split-carried one; by C2 the start")
print("      cannot choose and by C3 no no-Fermi-surface choice is normal in both sectors. CL-2 cannot repair it.")

# ================================================================ D. anomalies with the pi copy
print("== D. anomalies: the pi copy doubles every coefficient")
F16 = [(6, 3, 2, Fr(1, 6)), (3, -1, 1, Fr(-2, 3)), (3, -1, 1, Fr(1, 3)), (2, 0, 2, Fr(-1, 2)), (1, 0, 1, Fr(1)), (1, 0, 1, Fr(0))]
def anom(c):   # c copies of the 16 (left-handed Weyl): (dim, SU3 cubic index sign, SU2 dim, Y)
    Y3 = c * sum(d * y ** 3 for d, _, _, y in F16); Yg = c * sum(d * y for d, _, _, y in F16)
    Y22 = c * (3 * Fr(1, 6) + Fr(-1, 2)); Y33 = c * (2 * Fr(1, 6) + Fr(-2, 3) + Fr(1, 3)); A3 = c * (2 * 1 - 1 - 1)
    return Y3, Yg, Y22, Y33, A3, c * 4 % 2, c * 16 % 16
okD = all(x == 0 for x in anom(1)) and all(x == 0 for x in anom(2))
nf_same = all({n for n in range(1, 28) if n * cc % m == 0} == {n for n in range(1, 28) if n * 2 * cc % m == 0} for m in (3, 9) for cc in range(1, m))
check("D1 [T]", okD and nf_same, "gauge anomalies stay zero with the pi copy (2 x 16 per family: Y^3, Y-grav, SU2^2 Y, SU3^2 Y, SU3^3 = 0; doublets even; Weyls 0 mod 16), and doubling any turn coefficient by 2 (a unit mod 3 and mod 9) leaves the allowed N_f set unchanged: anomaly SAFE",
      f"1 x 16 {anom(1)}; 2 x 16 {anom(2)}")
print("   D2 [S] the far-wall gapping must gap the pi copy of the mirror too (it is light, charged, and S-related); an S-even far-wall")
print("      term does it at the same coupling (S maps the interacting tick to (-1)^N times itself); not computed.")

# ================================================================ E. measurement
print("== E. against measurement (supplied numbers)")
al, me = 1 / 137.035999, 510998.95                        # eV
uehl = 4 * al * al ** 4 * me / (15 * np.pi * 8) / 4.135667696e-15 / 1e6     # MHz, hydrogen 2S, n = 2
check("E1 [E]", uehl > 1e3 * 0.01, "with S intact the electron loop's vacuum polarization cancels exactly against its inverted pi copy: the hydrogen 2S Uehling shift would vanish; it is ~27 MHz and theory matches the measured Lamb shift to ~0.01 MHz -> EXCLUDED",
      f"Uehling 2S = -{uehl:.2f} MHz; agreement scale ~0.01 MHz (supplied); ratio {uehl / 0.01:.0f}")
Nnu, sNnu = 2.984, 0.008
check("E2 [E]", abs(0 - Nnu) / sNnu > 100 and abs(6 - Nnu) / sNnu > 100, "Z invisible width: inverted pi neutrinos cancel the light ones in the Z self-energy (N_nu -> 0); normal-filled copies would double it (N_nu -> 6); measured 2.984 +- 0.008 excludes both",
      f"{abs(Nnu) / sNnu:.0f} sigma and {abs(6 - Nnu) / sNnu:.0f} sigma")
print("   E3 [S] a light charged inverted sector with the light photon also opens exothermic pair production in every process (B1),")
print("      with phase space up to the cell scale: the free sector is excluded long before any rate is computed.")
pk = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024 if os.uname().sysname == 'Darwin' else 1024)
print(f"VERDICT: NEEDS REPAIR. Anomaly SAFE; free pi sector EXCLUDED (light, charged, inverted, forced by F_pi = W).  [{time.time() - T0:.1f} s, {pk:.0f} MB]")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
