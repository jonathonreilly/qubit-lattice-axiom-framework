AUDIT_INPUT_PATHS = ('docs/FAR_TERMINATION_WINDING_KEEPS_A_PI_FREE_SCREENING_NEAR_WALL_BUT_THE_END_IS_A_CHOSEN_BOUNDARY_BIT_AND_THE_FAR_WALL_MUST_GAP_ALL_THREE_FAMILIES_TOGETHER_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""far-termination-winding: test the candidate 'W = 0 bulk tick; the slab's FAR termination layer carries the family-class
turn-graded winding' (pi-repair A4 reading).
 G  gate / forcing: both end placements are valid slabs with the same bulk; the record arrow (U -> U^+) does not move the
    layer; minimal family-class W values compatible with one far mirror Weyl.
 N  near wall: flows (light q 2 at 0, no pi copy) over g and Lx; no doubler map; vacuum polarization (repaired vs an exact
    S-doubled control); T-odd leak from the far layer in a T-symmetric 3D Wilson domain-wall slab (dim-5 reciprocity-odd).
 C  CP at the near wall: T with X = 1 and a family-universal leak keep J = 0.
 F  far wall per family: (q1,-), (q2,+), (q1,-) x 16, gauge / mod-16 / turn Z3 anomalies (supplied index form).
Labels: [T] exact, [F] finite diagnostic, [S] reading. Supplied: the sector-resolved class-A toy (QWZ strip + chiral shift
layer), the Wilson slab (m0 = 0.6), the anomaly index form, the termination choice. Every line reports a RESULT."""
AUDIT_TIMEOUT_SEC = 120
import os, time, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, schur
from scipy.optimize import linear_sum_assignment

rng = np.random.default_rng(20261024)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg, det=""):
    ok = bool(ok); NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))

# ------------------------------------------------ sector-resolved class-A toy (pi-repair A4, rebuilt)
def f(q, h): e = np.zeros(3, int); e[(q + 2) % 3] += h; e[(q + 1) % 3] -= h; return e
WF = np.array([-2, 1, 1]); Cn = f(2, 1)
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1])
def qwz(ky, m, Lx, tau=0.5):
    H = np.kron(np.eye(Lx), (m + np.cos(ky)) * sz + np.sin(ky) * sy)
    H = H + np.kron(np.eye(Lx, k=-1), (sz + 1j * sx) / 2) + np.kron(np.eye(Lx, k=1), (sz - 1j * sx) / 2)
    return expm(-1j * tau * H)
def slab(ky, m, Wp, Lx=8, g=0.3, end='far'):
    """strip layers 0..Lx-1 (2 modes each) + one chiral-shift layer exp(i Wp ky) at the far (after Lx-1) or near (before 0) end."""
    n = 2 * Lx + 1; U = np.eye(n, dtype=complex); Hc = np.zeros((n, n))
    if end == 'far':
        U[:-1, :-1] = qwz(ky, m, Lx); U[-1, -1] = np.exp(1j * Wp * ky); Hc[-1, -2] = Hc[-2, -1] = 1
    else:
        U[1:, 1:] = qwz(ky, m, Lx); U[0, 0] = np.exp(1j * Wp * ky); Hc[0, 1] = Hc[1, 0] = 1
    return expm(-1j * g * Hc) @ U
def wall_flows(Uf, kys, nearw, eps_list, win=0.3):
    out = {e: [0, 0] for e in eps_list}; prev = None
    for ky in kys:
        Tm, Z = schur(Uf(ky), output='complex'); ph = np.angle(np.diag(Tm))
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
kys = np.linspace(-np.pi, np.pi, 301) + 0.0123
def mass_for(Lx):
    nearS = lambda v: np.sum(np.abs(v[:Lx]) ** 2)
    pr = wall_flows(lambda k: slab(k, 1.0, 0, Lx)[:-1, :-1], kys, nearS, [0.0])[0.0][0]
    return {1: 1.0 if pr == 1 else -1.0, -1: -1.0 if pr == 1 else 1.0, 0: 3.0}
def sector_flows(Lx=8, g=0.3, end='far', Wv=WF, dagger=False):
    mC = mass_for(Lx); out = []
    nearw = (lambda v: np.sum(np.abs(v[:Lx]) ** 2)) if end == 'far' else (lambda v: np.sum(np.abs(v[:Lx + 1]) ** 2))
    for a in range(3):
        Ua = lambda k, a=a: (lambda M: M.conj().T if dagger else M)(slab(k, mC[int(Cn[a])], int(Wv[a]), Lx, g, end))
        fl = wall_flows(Ua, kys, nearw, [0.0, np.pi]); out.append((fl[0.0], fl[np.pi], detwind(Ua, kys)))
    near = ([o[0][0] for o in out], [o[1][0] for o in out]); far = ([o[0][1] for o in out], [o[1][1] for o in out])
    return near, far, [o[2] for o in out]

# ================================================================ G. gate / forcing
print("== G. is the far termination forced?")
nF, fF, wF = sector_flows(end='far'); nN, fN, wN = sector_flows(end='near')
okG1 = (nF == (list(Cn), [0, 0, 0]) and nN[1] == list(WF) and wF == wN == list(WF) and fF[1] == list(WF) and fN[1] == [0, 0, 0])
check("G1 [T]/[F]", okG1, "same W = 0 bulk, same total winding W_F, two end placements: far layer -> near wall (f(2,+), pi-free); "
      "near layer -> near wall carries the whole pi flow W_F (the pi copy returns). Both are valid gapped-bulk unitary slabs; "
      "nothing in the bulk tick distinguishes them",
      f"far: near (F0,Fpi) {nF}, far {fF}; near-layer: near {nN}, far {fN}; det windings {wF}, {wN}")
nD, fD, wD = sector_flows(end='far', dagger=True)
okG2 = nD[1] == [0, 0, 0] and fD[1] == [-x for x in WF] and nD[0] == [-x for x in Cn]
check("G2 [T]/[F]", okG2, "record arrow: reversing the tick (U -> U^+, the time-reversed reading the arrow excludes) negates every "
      "flow but leaves the layer at the SAME end (near wall still pi-free): the record arrow orients time, not the layer "
      "coordinate, so it cannot choose the end", f"U^+: near {nD}, far {fD}, W {wD}")
opts = [(q, [int(x) for x in Cn + f(q, -1)]) for q in range(3)]
fam = [(q, W) for q, W in opts if all(x != 0 for x in W) and q != 2]
okG3 = len(fam) == 2 and [-2, 1, 1] in [W for _, W in fam]
check("G3 [T]", okG3, "with light q 2 (C = f(2,+)) and ONE far mirror Weyl at 0 (far F_0 = -C + W = f(q,-)), the family-class "
      "windings are W = C + f(q,-) for q in {0, 1}: two options, both N_f = 0 mod 3; q = 2 gives W = 0 (no mod 3). So the clause "
      "fixes: W != 0 (1 bit), which end (1 bit), which mirror charge (1 bit): ~3 bits of boundary information, none forced",
      f"options (q_mirror, W): {opts}; family class: {fam}")

# ================================================================ N. near wall on the W = 0 bulk
print("== N. near-wall physics")
grid = {}
for Lx in (6, 8, 10):
    for g in (0.2, 0.3, 0.5):
        if Lx != 8 and g != 0.3: continue
        grid[(Lx, g)] = sector_flows(Lx, g)[0]
okN1 = all(v == (list(Cn), [0, 0, 0]) for v in grid.values())
check("N1 [F]", okN1, "near wall (F_0, F_pi) = (f(2,+), 0) for every tested g and Lx: one light q 2 Weyl per field, no pi copy",
      f"{len(grid)} cases: {sorted(set(str(v) for v in grid.values()))}")
mC = mass_for(8); a1 = 1
U = lambda k: slab(k, mC[int(Cn[a1])], int(WF[a1]))
dspec = max(np.min(np.abs(np.exp(1j * np.angle(np.linalg.eigvals(U(k))))[:, None] + np.exp(1j * np.angle(np.linalg.eigvals(U(k + np.pi))))[None, :]), axis=1).max() for k in (0.31, 1.1, 2.2))
check("N2 [T]/[F]", dspec > 1e-2, "lemma: a layer-preserving S with S U(k) S^-1 = -U(k+pi) maps each wall's crossing at 0 to one "
      "at pi with the same hand, so F_0 = F_pi per wall; the repaired near wall has F_0 != F_pi, so no such S exists (and the "
      "spectrum is not pi-shift symmetric), which removes the mechanism that zeroed polarization",
      f"max_k distance of spec U(k) from spec(-U(k+pi)): {dspec:.2f}")
Ly, Lx = 12, 8; phi = 0.37; kg = 2 * np.pi * (np.arange(Ly) + phi) / Ly; n = 2 * Lx + 1
Fy = np.exp(-1j * np.outer(kg, np.arange(Ly))) / np.sqrt(Ly); FF = np.kron(Fy, np.eye(n))
def real(blocks):
    M = np.zeros((n * Ly, n * Ly), complex)
    for j, B in enumerate(blocks): M[n * j:n * j + n, n * j:n * j + n] = B
    return FF.conj().T @ M @ FF
def fill(B):
    e, v = np.linalg.eig(B); s = (np.angle(e) < 0); Q = np.linalg.qr(v[:, s])[0]; return Q @ Q.conj().T
nearmask = np.zeros(n); nearmask[:6] = 1
Vy = rng.normal(size=Ly); V = np.kron(np.diag(Vy), np.diag(nearmask[:n]))
def respond(Ur, rho, Vr, mask, lam=0.5, T=24):
    Ul = np.diag(np.exp(-1j * lam * np.diag(Vr))) @ Ur; N0 = np.real(np.diag(rho)) @ mask; d = 0.0
    for _ in range(T):
        rho = Ul @ rho @ Ul.conj().T; d = max(d, abs(np.real(np.diag(rho)) @ mask - N0))
    return d
maskR = np.kron(np.ones(Ly), nearmask)
Bs = [U(k) for k in kg]; Ur = real(Bs); rho = real([fill(B) for B in Bs]); dRep = respond(Ur, rho, V, maskR)
Bn = [slab(k, mC[int(Cn[a1])], int(WF[a1]), end='near') for k in kg]; dNear = respond(real(Bn), real([fill(B) for B in Bn]), V, maskR)
P = np.kron(np.diag([(-1.0) ** y for y in range(Ly)]), np.eye(n)); Z = np.zeros_like(Ur)
U2 = np.block([[Ur, Z], [Z, -P @ Ur @ P]]); rho2 = np.block([[rho, Z], [Z, P @ (np.eye(n * Ly) - rho) @ P]])
V2 = np.block([[V, Z], [Z, V]]); d2 = respond(U2, rho2, V2, np.concatenate([maskR, maskR]))
okN3 = dRep > 0.05 and d2 < 1e-9
check("N3 [F]", okN3, "vacuum polarization (12-site ring x 8 layers + far layer, sector with C = +1, near-wall kicks lam 0.5, 24 "
      "ticks): the repaired near wall SCREENS; the exactly S-doubled control (U plus its inverted pi image, the pi-sector-stability "
      "mechanism) gives exactly zero", f"max |dN_near|: repaired {dRep:.3f}, near-layer placement {dNear:.3f}, S-doubled {d2:.0e}")

# --- T-symmetric 3D Wilson domain-wall slab (m0 0.6): leak of a far-layer T-odd term into the near-wall Weyl
s1 = [sx, sy, sz]; tx, ty, tz = sx, sy, sz; I2 = np.eye(2)
G = [np.kron(tx, s) for s in s1]; G4 = np.kron(tz, I2); G5 = np.kron(ty, I2); UT = np.kron(I2, 1j * sy)
m0 = 0.6; Bh = (G4 - 1j * G5) / 2
def Hw(k, Ls, far=None):
    on = sum(np.sin(k[i]) * G[i] for i in range(3)) + (m0 - sum(1 - np.cos(k)) - 1) * G4
    H = np.kron(np.eye(Ls), on) + np.kron(np.eye(Ls, k=1), Bh) + np.kron(np.eye(Ls, k=-1), Bh.conj().T)
    if far is not None:
        H[-4:, -4:] += far(k)
    return H
codd = lambda k: 0.3 * (np.kron(I2, sx) * np.sin(k[1]) * np.sin(k[2]) + np.kron(I2, sy) * np.sin(k[2]) * np.sin(k[0]) + np.kron(I2, sz) * np.sin(k[0]) * np.sin(k[1]))
ceven = lambda k: 0.3 * np.kron(tz, I2) * (np.cos(k[0]) + np.cos(k[1]) + np.cos(k[2]))
UT5 = np.kron(np.eye(5), UT)
Tres = max(np.linalg.norm(UT5 @ np.conj(Hw(-k, 5, ceven)) @ UT5.conj().T - Hw(k, 5, ceven)) for k in [rng.uniform(-1, 1, 3) for _ in range(3)])
Todd = max(np.linalg.norm(UT @ np.conj(codd(-k)) @ UT.conj().T + codd(k)) for k in [rng.uniform(-1, 1, 3) for _ in range(3)])
def near_E(k, Ls, far):
    e, v = np.linalg.eigh(Hw(k, Ls, far)); wn = np.sum(np.abs(v[:4 * (Ls // 2)]) ** 2, axis=0)
    cand = [j for j in range(len(e)) if wn[j] > 0.8 and e[j] > 0]; return e[min(cand, key=lambda j: e[j])]
kap = 0.08; kk = kap * np.ones(3)
asym = {Ls: near_E(kk, Ls, codd) - near_E(-kk, Ls, codd) for Ls in (4, 6, 8, 10)}
asymE = max(abs(near_E(kk, Ls, ceven) - near_E(-kk, Ls, ceven)) for Ls in (6, 8))
rat = [asym[L + 2] / asym[L] for L in (4, 6, 8)]; rate = [r ** 0.5 for r in rat]
okN4 = Tres < 1e-12 and Todd < 1e-12 and asymE < 1e-12 and all(0.10 < r < 0.25 for r in rate)
check("N4 [T]/[F]", okN4, "T-symmetric Wilson slab (T = i sigma_y K, T^2 = -1): a T-even far term leaves E(k) = E(-k) on the "
      "near wall exactly; a tetrahedral-covariant T-odd far term (sigma_x sin ky sin kz + cyc, the dim-5 class) leaks a "
      "reciprocity-odd near-wall term E(k) - E(-k) that falls by ~(1 - m0)^2 per layer (first order in the near mode's far-layer "
      "weight)", f"T res {Tres:.0e}, T-odd check {Todd:.0e}; even-term asym {asymE:.0e}; odd-term asym vs Ls 4,6,8,10: "
      f"{[f'{asym[L]:.1e}' for L in (4, 6, 8, 10)]}; per-layer factor {[round(float(r), 3) for r in rate]} vs (1-m0)^2 = 0.16")
Ls_need = int(np.ceil(np.log(1e-7 / abs(asym[4] / kap ** 2) * 0.16 ** 4) / np.log(0.16)))
print(f"   N5 [S] reading: the leaked term is dim-5 (coefficient ~ c 0.16^Ls a); a Crab-type |eta| < 1e-7 bound at a = l_P needs "
      f"Ls >~ {Ls_need} layers (constant b terms are forbidden by the 12 tetrahedral rotations the termination keeps)")

# ================================================================ C. CP at the near wall
print("== C. CP")
def J_of(Hu, Hd):
    C = Hu @ Hd - Hd @ Hu; return np.imag(np.linalg.det(C)) / 2, np.abs(np.linalg.det(C)) / np.linalg.norm(C) ** 3
def herm(re=False):
    A = rng.normal(size=(3, 3)) + (0 if re else 1j) * rng.normal(size=(3, 3)); return A + A.conj().T
JT = max(abs(J_of(herm(True), herm(True))[0]) for _ in range(300))
eps = 1e-3; JL = max(abs(J_of(herm(True) + eps * np.eye(3), herm(True) + 2 * eps * np.eye(3))[0]) for _ in range(300))
Jg = np.median([abs(J_of(herm(), herm())[0]) for _ in range(300)])
okC = JT < 1e-13 and JL < 1e-13 and Jg > 1e-3
check("C1 [T]", okC, "the W = 0 bulk keeps Floquet T itself; on copies it acts with X = 1 (family-fixing), so masses respecting "
      "it are real and det[Hu,Hd] = 0: J = 0; a family-universal leak (multiple of 1) leaves the commutator unchanged: J = 0. "
      "CP still needs a non-family-blind ingredient, as on the FREEZE bulk (status unchanged, not worse)",
      f"max |J| real masses {JT:.0e}; with universal leak {JL:.0e}; generic supplied phases median Im det[Hu,Hd]/2 {Jg:.1e} (unnormalised)")

# ================================================================ F. far wall anomalies
print("== F. far-wall content per family: (q1,-), (q2,+), (q1,-), each a 16")
far = [(1, -1), (2, 1), (1, -1)]
def coeffs(N, k, content):
    st = [((q + k) % 3, h) for q, h in content]
    return ((2 * N * sum(h * t for t, h in st)) % 3, (16 * N * sum(h * t for t, h in st)) % 3, (16 * N * sum(h * t ** 3 for t, h in st)) % 9)
weyl = 16 * len(far); net = 16 * sum(h for _, h in far)
per = {k: coeffs(1, k, far) for k in range(3)}; ok_N = [N for N in range(1, 10) if coeffs(N, 0, far) == (0, 0, 0)]
okF = weyl % 16 == 0 and net % 16 == 0 and all(c != (0, 0, 0) for c in per.values()) and ok_N == [3, 6, 9]
check("F1 [T]", okF, "far wall per family: gauge anomalies 0 (each 16 is anomaly-free), Weyl count 48 and net hand -16 both 0 mod 16; "
      "but the turn Z3 anomaly is NONZERO per family for every twist k (cubic 96 = 6 mod 9 at k = 0); it vanishes for N_f = 0 mod 3. "
      "So symmetric gapping is allowed in principle only for the three families TOGETHER (family-collective far-wall term)",
      f"(Z3-Spin10^2, Z3-grav, Z3^3) per family for k = 0,1,2: {per}; untwisted far wall anomaly-free for N_f in {ok_N}")
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1 << 20)
print(f"   time {time.time() - T0:.1f} s, peak {mem:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
