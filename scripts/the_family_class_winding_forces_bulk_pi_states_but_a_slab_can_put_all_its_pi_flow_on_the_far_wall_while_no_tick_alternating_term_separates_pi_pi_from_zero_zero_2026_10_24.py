AUDIT_INPUT_PATHS = ('docs/THE_FAMILY_CLASS_WINDING_FORCES_BULK_PI_STATES_BUT_A_SLAB_CAN_PUT_ALL_ITS_PI_FLOW_ON_THE_FAR_WALL_WHILE_NO_TICK_ALTERNATING_TERM_SEPARATES_PI_PI_FROM_ZERO_ZERO_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""pi-repair: can the suspended family-class tick's light pi sector be repaired?
 A  bulk vs slab. A1 W_a != 0 forces a BULK eigenphase at every quasi-energy (pi included) on the turn axis (FREEZE and
    turn-symmetric deformations). A2 every interval filling has flow W at both cuts; intersection lemma: a band filling
    with no occupied-empty touching on the axis forces W = 0. A3 contrast: anomalous Floquet (RLBL) has a gapped bulk
    and ZERO det winding; its walls carry F_0 = F_pi. A4 slab: per wall F_0 - F_pi = C (bulk band invariant); a
    static-type domain-wall bulk (C = light flow, W = 0) with the W-carrying layer at the far termination puts all pi
    flow on the far wall (sector-resolved class-A toy).
 B  B1 time modulation resolves only the parity of the number of pi legs: pi-pi and 0-0 terms are never separated
    (tick-alternating terms act only on 0-pi mixing). B2 separating them needs an S-odd term, which hands the light
    sector the reflected interaction (reduced two-flavour Spin(6) site, 2^8). C bookkeeping of the repaired slab.
Labels: [T] exact, [F] finite diagnostic, [S] reading. Criteria: criteria_pre_run.txt (written first).
FREEZE is rebuilt inline exactly as pi-sector-stability / floquet-pi-slab (same seed, same draw order)."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, null_space, schur
from scipy.optimize import linear_sum_assignment

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

rng2 = np.random.default_rng(20261024)      # all new draws use rng2 (FREEZE draws untouched)
RV = np.pi * np.ones(3)
# ================================================================ A1 bulk spectral flow
print("== A. bulk tick vs slab walls")
ks = np.linspace(0, 2 * np.pi, 721)
ev, evec = np.linalg.eig(T3); lab = np.round(np.angle(ev) / (2 * np.pi / 3)).astype(int) % 3
SEC = [np.linalg.qr(evec[:, lab == q])[0] for q in range(3)]
def sector_winds(U):
    out = []
    for B in SEC:
        d = [np.linalg.det(B.conj().T @ U(k * np.ones(3)) @ B) for k in ks]
        out.append(int(np.rint((np.unwrap(np.angle(d))[-1] - np.angle(d[0])) / (2 * np.pi))))
    return out
def flow_at(U, eps):
    """signed crossings of quasi-energy eps per turn sector along the axis loop (bulk Bloch tick)"""
    out = []
    for B in SEC:
        fl = 0; f = lambda k: np.angle(np.exp(1j * (np.pi - eps)) * np.linalg.eigvals(B.conj().T @ U(k * np.ones(3)) @ B))
        prev = f(ks[0])
        for k in ks[1:]:
            cur = f(k)
            for x in prev:
                y = cur[np.argmin(np.abs(np.angle(np.exp(1j * (cur - x)))))]
                if abs(x) > 2.5 and abs(y) > 2.5 and np.sign(x) != np.sign(y): fl += 1 if x > 0 else -1
            prev = cur
        out.append(fl)
    return out
WF = sector_winds(UF)
EPS = [0.37, 1.1, 1.77, 2.6, np.pi]
fl = {e: flow_at(UF, e) for e in EPS}
rob = []
for _ in range(2):
    G = rng2.normal(size=(8, 8)) + 1j * rng2.normal(size=(8, 8)); G = G + G.conj().T
    G = sum(np.linalg.matrix_power(T3, j) @ G @ np.linalg.matrix_power(T3, j).conj().T for j in range(3)) / 3
    Gx = expm(-0.3j * G / np.linalg.norm(G, 2)); Ud = lambda K, Gx=Gx: Gx @ UF(K)
    rob.append((sector_winds(Ud), flow_at(Ud, np.pi), flow_at(Ud, 1.1)))
okA1 = sorted(WF) == [-2, 1, 1] and all(fl[e] == WF for e in EPS) and all(r[0] == WF and r[1] == WF and r[2] == WF for r in rob)
check("A1 [T]/[F]", okA1, "BULK theorem: in turn sector a the net eigenphase flow through EVERY quasi-energy equals W_a (det winding), so W_a != 0 puts a bulk Bloch eigenstate at every quasi-energy, pi included, on the axis loop. No family-class bulk tick is gapped at pi; this is the bulk tick's own spectrum, not a slab-wall effect",
      f"W {WF}; flow at eps {[round(e, 2) for e in EPS]}: {[fl[e] for e in EPS]}; 2 turn-symmetric deformations (W, F_pi, F_1.1) {rob}")
# ================================================================ A2 fillings
cuts = [tuple(sorted(rng2.uniform(-np.pi, np.pi, 2))) for _ in range(3)]
cf = [(flow_at(UF, a), flow_at(UF, b)) for a, b in cuts]
lem = True; ncase = 0
for No in it.product(range(3), repeat=3):
    for Ne in it.product(range(3), repeat=3):
        if sum(No) == 0 or sum(Ne) == 0: continue
        rngs = [range(-2, 3) if No[a] else [0] for a in range(3)], [range(-2, 3) if Ne[a] else [0] for a in range(3)]
        for n in it.product(*rngs[0]):
            for m in it.product(*rngs[1]):
                if sum(n) + sum(m) != 0: continue
                if all(No[a] * m[b] - Ne[b] * n[a] == 0 for a in range(3) for b in range(3)):
                    ncase += 1; lem &= all(n[a] + m[a] == 0 for a in range(3))
check("A2 [T]", all(x == WF and y == WF for x, y in cf) and lem,
      "fillings: an interval filling (a, b) has flow W at BOTH cuts, so a light cut at 0 always brings a second gapless cut (its quasi-energy, pi or not, is a convention; its existence is forced). Intersection lemma: occupied and empty axis bands disjoint => every occupied/empty homology class (N, n) has one common slope => total W = 0. So ANY bulk vacuum of a W != 0 tick has occupied-empty touchings beyond a single light cut",
      f"random cuts {[(round(a, 2), round(b, 2)) for a, b in cuts]}: flows {cf[0]} ...; lemma exhaustive over {ncase} disjoint configurations (bands <= 2 per sector and side, windings |n| <= 2): all have W = 0")
# ================================================================ A3 anomalous Floquet contrast (RLBL)
def schur_eig(U):
    T, Z = schur(U, output='complex'); return np.angle(np.diag(T)), Z
def wall_flows(Uf, kys, nearw, eps_list, win=0.4):
    out = {e: [0, 0] for e in eps_list}; prev = None
    for ky in kys:
        ph, Z = schur_eig(Uf(ky))
        if prev is not None:
            pph, pZ = prev; r, c = linear_sum_assignment(-np.abs(pZ.conj().T @ Z))
            for i, j in zip(r, c):
                wall = 0 if nearw(Z[:, j]) > 0.5 else 1
                for e in eps_list:
                    x = np.angle(np.exp(1j * (pph[i] - e))); y = np.angle(np.exp(1j * (ph[j] - e)))
                    if abs(x) < win and abs(y) < win:
                        if x < 0 <= y: out[e][wall] += 1
                        elif y < 0 <= x: out[e][wall] -= 1
        prev = (ph, Z)
    return out
def detwind(Uf, kys):
    d = [np.linalg.det(Uf(k)) for k in kys]; return int(np.rint((np.unwrap(np.angle(d))[-1] - np.angle(d[0])) / (2 * np.pi)))
D_RL = [(0, 0), (-1, 0), (-1, -1), (0, -1)]; DEL = 0.8
def rlbl(ky, Lx=None, kx=0.0):
    n = 1 if Lx is None else Lx; U = np.eye(2 * n, dtype=complex)
    for dx, dy in D_RL:
        H = np.zeros((2 * n, 2 * n), complex)
        for x in range(n):
            xb = x + dx
            if Lx is None: H[1, 0] += np.exp(1j * (kx * dx + ky * dy))
            elif 0 <= xb < n: H[2 * xb + 1, 2 * x] += np.exp(1j * ky * dy)
        H = H + H.conj().T; U = expm(-1j * (np.pi / 2) * H) @ U
    return expm(-1j * DEL * np.kron(np.eye(n), np.diag([1, -1]))) @ U
kys = np.linspace(-np.pi, np.pi, 401) + 0.0123          # offset: no crossing on a grid point or the seam
bulk_ph = np.array([np.angle(np.linalg.eigvals(rlbl(ky, kx=kx))) for ky in kys[::8] for kx in np.linspace(-np.pi, np.pi, 25)])
gap0 = np.min(np.abs(bulk_ph)); gappi = np.min(np.pi - np.abs(bulk_ph))
dws = [detwind(lambda k, kx=kx: rlbl(k, kx=kx), kys) for kx in (0.0, 1.3, np.pi)] + [detwind(lambda k, ky=ky: rlbl(ky, kx=k), kys) for ky in (0.0, 2.0)]
LX = 8; nearL = lambda v: np.sum(np.abs(v[:LX]) ** 2)
rf = wall_flows(lambda k: rlbl(k, LX), kys, nearL, [0.0, np.pi])
check("A3 [F]", gap0 > 0.5 and gappi > 0.5 and all(d == 0 for d in dws) and rf[0.0] == rf[np.pi] and abs(rf[0.0][0]) == 1 and rf[0.0][0] == -rf[0.0][1],
      "contrast: the anomalous Floquet (RLBL) tick is gapped at 0 AND pi in the bulk and has ZERO det winding on every loop; its walls carry F_0 = F_pi = +-1. The anomalous-Floquet escape lives in the micromotion, not in W: it cannot gap a W != 0 bulk, but it IS the structure of a slab whose bulk period has W = 0 (floquet-pi-slab's F/F^+ bulk)",
      f"bulk gap at 0 {gap0:.2f}, at pi {gappi:.2f}; det windings {dws}; strip Lx {LX} (near, far) flow at 0 {rf[0.0]}, at pi {rf[np.pi]}")
# ================================================================ A4 repaired slab, sector-resolved class-A toy
def f(q, h): e = np.zeros(3, int); e[(q + 2) % 3] += h; e[(q + 1) % 3] -= h; return e
Cn = f(2, 1); Wv = np.array(WF)                      # near-wall light flow and slab winding, sectors (1, w, w^2)
def qwz_strip(ky, m, Lx, tau=0.5):
    sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1])
    H = np.kron(np.eye(Lx), (m + np.cos(ky)) * sz + np.sin(ky) * sy)
    H = H + np.kron(np.eye(Lx, k=-1), (sz + 1j * sx) / 2) + np.kron(np.eye(Lx, k=1), (sz - 1j * sx) / 2)
    return expm(-1j * tau * H)
def slab(ky, m, Wp, Lx=8, g=0.3):
    n = 2 * Lx + 1; U = np.zeros((n, n), complex); U[:-1, :-1] = qwz_strip(ky, m, Lx); U[-1, -1] = np.exp(1j * Wp * ky)
    Hc = np.zeros((n, n)); Hc[-1, -2] = Hc[-2, -1] = 1; return expm(-1j * g * Hc) @ U
LS = 8; nearS = lambda v: np.sum(np.abs(v[:LS]) ** 2)
probe = wall_flows(lambda k: slab(k, 1.0, 0)[:-1, :-1], kys, nearS, [0.0])[0.0][0]
mC = {1: 1.0 if probe == 1 else -1.0, -1: -1.0 if probe == 1 else 1.0, 0: 3.0}
res = []
for a in range(3):
    U_a = lambda k, a=a: slab(k, mC[int(Cn[a])], int(Wv[a]))
    fa = wall_flows(U_a, kys, nearS, [0.0, np.pi], win=0.3); res.append((fa[0.0], fa[np.pi], detwind(U_a, kys)))
near0 = [r[0][0] for r in res]; nearpi = [r[1][0] for r in res]; far0 = [r[0][1] for r in res]; farpi = [r[1][1] for r in res]
okA4 = near0 == list(Cn) and nearpi == [0, 0, 0] and far0 == list(f(1, -1)) and farpi == list(Wv) and [r[2] for r in res] == list(Wv)
check("A4 [T]/[F]", okA4,
      "slab: per wall F_0 - F_pi = C (bulk bands between 0 and pi); total pi flow = W_slab != 0 is forced, but its WALL is not. Static-type domain-wall bulk (W = 0, sector band invariant C = f(2,+)) + the W-carrying layer at the far termination: near wall light q 2 at 0 only, NO near-wall pi copy; far wall mirror q 1 at 0 plus the whole pi flow W",
      f"near (F_0, F_pi) per sector {list(zip(near0, nearpi))}; far {list(zip(far0, farpi))}; slab det winding {[r[2] for r in res]}")
# ================================================================ B1 time modulation
print("== B. gapping the pi copies")
def jw(n):
    a = np.array([[0, 1], [0, 0.]]); z = np.diag([1., -1]); ops = []
    for i in range(n):
        m = np.array([[1.]])
        for j in range(n): m = np.kron(m, z if j < i else (a if j == i else np.eye(2)))
        ops.append(m)
    return ops
cB = jw(4); Nk = [c.T @ c for c in cB]                        # modes 0,1: light (quasi-energy 0); 2,3: pi copy
U0 = np.diag(np.diag(expm(1j * np.pi * (Nk[2] + Nk[3]))).real)
par = np.diag(expm(1j * np.pi * sum(Nk))).real
Mr = rng2.normal(size=(16, 16)) + 1j * rng2.normal(size=(16, 16)); Mr = Mr + Mr.conj().T
Mr = Mr * np.equal.outer(par, par); Mr /= np.linalg.norm(Mr, 2)
Oev = (Mr + U0 @ Mr @ U0) / 2; Ood = Mr - Oev
g = 0.01
def heff(s):
    U2 = expm(-1j * g * s[1] * Mr) @ U0 @ expm(-1j * g * s[0] * Mr) @ U0
    ev_, V_ = np.linalg.eig(U2); return (V_ @ np.diag(1j * np.log(ev_)) @ np.linalg.inv(V_)) / (2 * g)
Hc, Ha = heff((1, 1)), heff((1, -1))
e1 = np.linalg.norm(Hc - Oev, 2); e2 = np.linalg.norm(Ha + Ood, 2)
pp = (cB[2].T @ cB[3] + cB[3].T @ cB[2]); zz = (cB[0].T @ cB[1] + cB[1].T @ cB[0]); zp = (cB[0].T @ cB[2] + cB[2].T @ cB[0])
quart = cB[2].T @ cB[3].T @ cB[1] @ cB[0]; quart = quart + quart.conj().T   # 2 pi legs + 2 light legs
def split(O, s):
    U2 = expm(-1j * 0.3 * s[1] * O) @ U0 @ expm(-1j * 0.3 * s[0] * O) @ U0; ph = np.angle(np.linalg.eigvals(U2))
    return np.ptp(ph) / 2
tab = {nm: (split(O, (1, 1)), split(O, (1, -1))) for nm, O in [("0-0 mass", zz), ("pi-pi mass", pp), ("0-pi mix", zp), ("2+2 quartic", quart)]}
okB1 = e1 < 0.05 and e2 < 0.05 and tab["0-0 mass"][1] < 1e-9 and tab["pi-pi mass"][1] < 1e-9 and tab["0-pi mix"][0] < 1e-9 \
    and tab["0-0 mass"][0] > 0.2 and tab["pi-pi mass"][0] > 0.2 and tab["0-pi mix"][1] > 0.2 and tab["2+2 quartic"][1] < 1e-9
check("B1 [T]/[F]", okB1,
      "time modulation: U0 O U0^-1 = (-1)^(n_pi) O, so a period-n drive resolves only the PARITY of the number of pi legs. Tick-alternating terms act only on odd-n_pi (0-pi mixing); constant terms act on 0-0 and pi-pi alike. A sign-alternating interaction does NOT couple only pi-pi pairs: it cancels on them exactly",
      "random parity-even O, g 0.01: |H_eff(const) - O_even| %.1e, |H_eff(alt) + O_odd| %.1e; per-tick splitting (const, alt) at g 0.3: " % (e1, e2) + ", ".join(f"{k} ({v[0]:.2f}, {v[1]:.0e})" for k, v in tab.items()))
# ================================================================ B2 S-odd route: reduced two-flavour Spin(6) site
s1, s2, s3 = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1]); I2 = np.eye(2)
k3 = lambda a, b, c: np.kron(a, np.kron(b, c))
Gm = [k3(s1, I2, I2), k3(s2, I2, I2), k3(s3, s1, I2), k3(s3, s2, I2), k3(s3, s3, s1), k3(s3, s3, s2)]
G7 = 1j * np.linalg.multi_dot(Gm); G7 = G7 if np.allclose(G7 @ G7, np.eye(8)) else 1j * G7
e7, v7 = np.linalg.eigh((G7 + G7.conj().T) / 2); Q = v7[:, e7 > 0]
Mall = None
for sgn in (1, -1):
    Nc = null_space(np.vstack([np.kron(np.eye(8), Ga.T * sgn) - np.kron(Ga.T, np.eye(8)) for Ga in Gm]), rcond=1e-9)
    # vec(C Ga) = vec(sgn Ga^T C): rows act on column-major vec(C)
    if Nc.shape[1] == 0: continue
    Cc = Nc[:, 0].reshape(8, 8, order='F'); Ms = [Q.T @ Cc @ Ga @ Q for Ga in Gm]
    if max(np.linalg.norm(m) for m in Ms) > 1e-6: Mall = Ms; break
c8 = jw(8); c1, c2 = c8[:4], c8[4:]
Bs = [sum(Ma[i, j] * c1[i] @ c2[j] for i in range(4) for j in range(4)) for Ma in Mall]
Bs = [b / np.sqrt(np.linalg.norm(Mall[0]) ** 2 / 2) for b in Bs]
Hs = -0.5 * sum(b @ b.conj().T + b.conj().T @ b for b in Bs)
Nt = np.diag(sum(c.T @ c for c in c8)).real
def gs(H):
    e, v = np.linalg.eigh(H); d = int(np.sum(e < e[0] + 1e-8)); Ns = sorted({int(round(x)) for x in Nt @ (np.abs(v[:, :d]) ** 2)} if d == 1 else
         {int(round(Nt @ np.abs(v[:, j]) ** 2)) for j in range(d)}); return e, d, Ns
ep, dp, Np_ = gs(Hs); em, dm, Nm = gs(-Hs)
gap_p = ep[dp] - ep[0]
check("B2 [T]/[F]", dp == 1 and Np_ == [4] and dm > 1,
      "S-odd route: separating pi-pi from 0-0 needs a term odd under the doubler S, and then the light pair receives the REFLECTED interaction (-O in the S-mapped frame). Reduced two-flavour Spin(6) site: the gapping sign has a unique half-filled ground state (reproduces spin10-two-flavour); the reflected sign the light sector gets has a degenerate ground state: a strongly coupled cutoff-scale term on the light 16s, not a spectator (and a sign with a unique gapped state would gap the light, which is worse)",
      f"+g: ground degeneracy {dp}, N {Np_}, gap {gap_p:.2f} g; reflected -g: degeneracy {dm}, N values {Nm}")
# ================================================================ C bookkeeping
allowed = lambda nodes: [N for N in range(1, 10) if (nodes * N) % 3 == 0]
check("C1 [T]", allowed(1) == [3, 6, 9] and allowed(2) == [3, 6, 9],
      "bookkeeping (anomaly-family-count index with the Omega twist k = -q_mirror, supplied form: coefficient proportional to near-wall light node count x N_f): the repaired slab has 1 near-wall light node per family instead of 2; 1 and 2 are both units mod 3, so N_f = 0 mod 3 is unchanged. Far wall to gap by SMG: mirror q 1 at 0 + one (q 2, +) and one (q 1, -) at pi = 3 x 16 = 48 Weyl per family (0 mod 16); no turn-symmetric bilinear (charge difference 1)",
      f"allowed N_f (1 node) {allowed(1)}, (2 nodes) {allowed(2)}")
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1 << 20)
print(f"   time {time.time() - T0:.1f} s, peak {mem:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
