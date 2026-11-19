#!/usr/bin/env python3
"""slab-parity: does any adopted rule force the floquet-pi-slab's net layer orientation n = #F - #F^+ to be odd (the parity that puts
the q 1 mirror in the other copy)?
 0  rederived: the slab's turn-graded winding is W = n W_F, and alternating stacks have n = Ls mod 2.
 A  zoom ladder as the layer direction (CL-1 split: b = 2, belongs to the even tiling, polar).
 B  termination on the selected cube fold: the vacuum fold is blind to the tick's orientation (exact), unlike the tiling swap.
 C  layer = half-tick: CL-1's half-ticks each commute with the (111) turn, so W = 0 for any number of them.
 D  consistency reading (not adopted): slab winding = winding of the update's own tick; synthesis.
Labels: [T] exact, [F] finite diagnostic, [S] reading. FREEZE and the slab are rebuilt inline from floquet-pi-slab (same seed and
draw order). Every line reports a RESULT; the synthesis verdict follows criteria_pre_run.txt."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools as it, resource
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

# ------------------------------------------------ tools on the axis (floquet-pi-slab)
def sectors(n):
    e, v = np.linalg.eig(np.kron(np.eye(n), T3)); lb = np.round(np.angle(e) / (2 * np.pi / 3)).astype(int) % 3
    return [np.linalg.qr(v[:, lb == a])[0] for a in range(3)]
def wind(U, SEC, n=400):
    ks = np.linspace(0, 2 * np.pi, n + 1); out = []
    for Sx in SEC:
        d = np.array([np.linalg.det(Sx.conj().T @ U(k * np.ones(3)) @ Sx) for k in ks])
        out.append(int(round(np.sum(np.angle(d[1:] / d[:-1])) / (2 * np.pi))))
    return out
def flow(U, SEC, k0, e0, dk=1e-3, c=0.1, W=None):
    f = []
    for Sx in SEC:
        cnt = []
        for k in (k0 + dk, k0 - dk):
            ev, vv = np.linalg.eig(Sx.conj().T @ U(k * np.ones(3)) @ Sx); thx = np.angle(ev * np.exp(-1j * e0))
            m = (thx > 0) & (thx < c)
            if W is not None: m &= np.array([np.linalg.norm(W @ Sx @ vv[:, j]) ** 2 > 0.5 for j in range(len(ev))])
            cnt.append(int(m.sum()))
        f.append(cnt[0] - cnt[1])
    return f
form = lambda q, h: [h * (int(a == (q + 2) % 3) - int(a == (q + 1) % 3)) for a in range(3)]
def slab(K, Ls, g, pat=None, bonds=('q1', 'q2')):
    pat = pat if pat is not None else [l % 2 for l in range(Ls)]
    F = UF(K); U0 = np.zeros((8 * Ls, 8 * Ls), complex); HA = np.zeros_like(U0); HB = np.zeros_like(U0)
    for l, p in enumerate(pat): U0[8 * l:8 * l + 8, 8 * l:8 * l + 8] = F if p == 0 else F.conj().T
    for l in range(Ls - 1):
        H = HA if l % 2 == 0 else HB; lb = bonds[l % 2]
        Pq = {'q1': Pq1, 'q2': Pq2, 'both': Pp, 'none': 0 * Pp}[lb]
        H[8 * l:8 * l + 8, 8 * l + 8:8 * l + 16] += Pq; H[8 * l + 8:8 * l + 16, 8 * l:8 * l + 8] += Pq
    return expm(-1j * g * HB) @ expm(-1j * g * HA) @ U0
X2 = np.array([[0, 1], [1, 0]])
def bulk(K, k, g, alt=True):
    F = UF(K); Z = np.zeros((8, 8)); U0 = np.block([[F, Z], [Z, F.conj().T if alt else F]])
    XB = np.array([[0, np.exp(-1j * k)], [np.exp(1j * k), 0]])
    return expm(-1j * g * np.kron(XB, Pq2)) @ expm(-1j * g * np.kron(X2, Pq1)) @ U0

g = 0.5
WF = wind(UF, sectors(1))

# ================================================================ 0. W = n W_F
print("== 0. the slab's winding counts the net orientation n = #F - #F^+")
WFi = wind(lambda K: UF(K).conj().T, sectors(1))
pats = {7: [0, 0, 1, 0, 1, 1, 0], 5: [1, 1, 0, 1, 1]}
Wp = {L: wind(lambda K, L=L: slab(K, L, g, pats[L]), sectors(L)) for L in pats}
npat = {L: sum(1 if p == 0 else -1 for p in pats[L]) for L in pats}
Walt = {L: wind(lambda K, L=L: slab(K, L, g), sectors(L)) for L in range(2, 10)}
ok0 = (WFi == [-x for x in WF] and all(Wp[L] == [npat[L] * x for x in WF] for L in pats)
       and all(Walt[L] == [(L % 2) * x for x in WF] for L in Walt))
check("0 [T]/[F]", ok0, "W(F^+) = -W_F; for any layer pattern W = n W_F with n = #F - #F^+ (the label gates are turn-commuting, "
      "so they add nothing); the bulk gap forces alternation, so n = Ls mod 2. The question is exactly: what fixes n?",
      f"W_F {WF}, W(F^+) {WFi}; pattern n = {npat[7]}: {Wp[7]}, n = {npat[5]}: {Wp[5]}; alternating Ls 2..9: "
      + " ".join(str(Walt[L][0]) for L in Walt) + " (sector-1 entry)")

# ================================================================ A. zoom ladder
print("== A. layer direction = zoom ladder (CL-1 split, b = 2)")
par = {}
for c in it.product(range(4), repeat=3):
    if len(set(x % 2 for x in c)) != 1: continue                     # cube least corners: even (2Z^3) or odd (2Z^3 + 111)
    tl = c[0] % 2; img = [tuple(2 * (np.array(c) + np.array(a))) for a in CELL]     # parent sites -> child coordinates
    par.setdefault(tl, []).append(all(all(x % 2 == 0 for x in y) for y in img))
okA1 = all(all(v) for v in par.values()) and len(par) == 2
check("A1 [T]", okA1, "the split's site map y = 2x sends the sites of parent cubes of BOTH tilings onto least corners of child EVEN "
      "cubes (2Z^3): the child tiling is fixed by the split itself ('belongs to the even tiling'), whatever the parent's, so no "
      "tiling bit is carried rung to rung", f"parent even cubes {sum(par[0])}/{len(par[0])}, odd cubes {sum(par[1])}/{len(par[1])} map to child even corners")
Wall = {L: wind(lambda K, L=L: slab(K, L, g, [0] * L), sectors(L)) for L in (2, 3, 4)}
F = UF(np.zeros(3)); Z8 = np.zeros((8, 8))
ax = wind(lambda K: bulk(K, 0.7, g, alt=False), sectors(2), 200)
check("A2 [T]/[F]", all(Wall[L] == [L * x for x in WF] for L in Wall) and ax == [2 * x for x in WF], "the split passes the tick "
      "FORWARD (half of a half-tick before the passing, the other half after; no inversion), and the polar direction is the same at "
      "every generation (polar-split-reason), so a rung-indexed stack has sigma constant: all F. Then W = N_rungs W_F grows with "
      "the ladder and the bulk carries a nonzero sector winding at every k_l, so it is gapless at 0 and pi. The ladder cannot even "
      "supply the alternation, let alone its parity", f"all-F W at N = 2, 3, 4: {[Wall[L] for L in Wall]}; bulk 2-layer winding {ax}")
print("   A3 [S] the number of rungs from the finest (matter) role block to the coarsest (edge registers, b_e) is log2 of block sizes "
      "that CL-1 SUPPLIES (B_f, b_e), and splits are triggered by edge lengths, so the rung count is dynamical; its parity is not "
      "fixed by any clause")

# ================================================================ B. termination on the cube fold
print("== B. the vacuum fold is blind to the tick's orientation")
L4 = 4; SIT = {s: i for i, s in enumerate(it.product(range(L4), repeat=3))}
def Rtil(odd):
    R = np.zeros((64, 64)); cubes = []
    for c in it.product(range(0, L4, 2), repeat=3):
        c = np.array(c) + (1 if odd else 0); cubes.append([SIT[tuple((c + a) % L4)] for a in np.array(CELL)])
        for a in CELL:
            for i in range(3):
                if a[i] == 0:
                    b = list(a); b[i] = 1; s1 = SIT[tuple((c + a) % L4)]; s2 = SIT[tuple((c + b) % L4)]
                    R[s1, s2] += eta_s(i, a) / np.sqrt(3); R[s2, s1] += eta_s(i, a) / np.sqrt(3)
    return R, cubes
Rev, CE = Rtil(0); Rod, CO = Rtil(1); eps = 0.3
def tick(mu): return expm(-1j * (eps + mu / 2) * Rod) @ expm(-1j * (eps - mu / 2) * Rev)
def fold(U):
    Tm, Zm = schur(U, output='complex'); ph = np.angle(np.diag(Tm)); assert min(abs(ph).min(), (np.pi - abs(ph)).min()) > 1e-3
    V = Zm[:, ph > 0]; C = V @ V.conj().T
    va = lambda cs: np.mean([np.trace(C[np.ix_(q, q)]).real - np.trace(C[np.ix_(q, q)] @ C[np.ix_(q, q)]).real for q in cs])
    mn = lambda cs: np.mean([np.trace(C[np.ix_(q, q)]).real for q in cs])
    return tuple(float(round(x, 4)) for x in (va(CE), va(CO), mn(CE), mn(CO)))
r2 = max(np.linalg.norm(Rev @ Rev - np.eye(64)), np.linalg.norm(Rod @ Rod - np.eye(64)))
FB = {mu: (fold(tick(mu)), fold(tick(mu).conj().T)) for mu in (0.2, -0.2, 0.6)}
okB1 = r2 < 1e-12 and all(FB[m][0] == FB[m][1] for m in FB) and FB[0.6][0][1] < 1e-8
check("B1 [T]/[F]", okB1, "theorem: with no eigenphase at 0 or pi, the vacuum of U^+ is the particle-hole complement of the vacuum of "
      "U (C -> 1 - C), so every cube's total goes n -> 8 - n with IDENTICAL variance. The fold (which tiling's cubes hold definite "
      "totals) is the same for F and F^+; checked on CL-1's two-tiling tick on the 4^3 torus (eps = 0.3; R^2 = 1 on both tilings)",
      f"(VarN_even, VarN_odd, <N_even>, <N_odd>) U vs U^+: mu 0.2 {FB[0.2][0]} vs {FB[0.2][1]}; fold limit mu 0.6 {FB[0.6][0]}")
Tt = np.zeros((64, 64))
for x, i in SIT.items(): Tt[SIT[tuple((np.array(x) + 1) % L4)], i] = 1      # translation by (1,1,1) swaps the tilings
Bh = expm(-1j * (eps - 0.1) * Rod); sw = np.linalg.norm(Tt @ Rev @ Tt.T - Rod) + np.linalg.norm(Bh @ Tt @ tick(0.2) @ Tt.T @ Bh.conj().T - tick(-0.2))
okB2 = FB[0.2][0][0] > FB[0.2][0][1] and FB[-0.2][0][0] < FB[-0.2][0][1] and sw < 1e-12
check("B2 [T]/[F]", okB2, "control with power: mu -> -mu is the tiling swap (translation by (1,1,1) maps R_e to R_o, and U(-mu) is "
      "the translated tick conjugated by one half-tick) and DOES flip the fold (mu > 0: odd cubes definite); inversion does NOT. The "
      "inverse tick's steps are -(eps -+ mu/2), so its 'mass angle' is -mu, yet its fold is unchanged: fold-selection's 'sign of mu' "
      "must be read as sign(mu / eps)", f"VarN (even, odd): mu 0.2 {FB[0.2][0][:2]}, mu -0.2 {FB[-0.2][0][:2]}; swap identity {sw:.0e}")
print("   B3 [T] hence a termination rule 'both walls end on the selected fold' holds for EVERY Ls of the F/F^+ slab (all layers share one "
      "fold), so it fixes nothing about n; and a fold-matched (tiling) bit is a conjugation, which leaves W unchanged (W is a "
      "determinant winding), so W never sees it")

# ================================================================ C. layer = half-tick
print("== C. layer = half-tick of one tiling")
def Ro(K): return sum(Wl(i, K, 1) for i in range(3)) / np.sqrt(3)
hc = max([np.linalg.norm(T3 @ Re @ T3.T - Re)] + [np.linalg.norm(T3 @ Ro(k * np.ones(3)) @ T3.T - Ro(k * np.ones(3))) for k in (0.4, 1.9, 2.8)])
S1 = sectors(1)
Wh = [wind(lambda K: expm(-1j * eps * Re), S1), wind(lambda K: expm(1j * eps * Ro(K)), S1), wind(U1, S1),
      wind(lambda K: expm(1j * (eps + 0.1) * Ro(K)) @ expm(-1j * (eps - 0.1) * Re), S1)]
okC1 = hc < 1e-12 and all(x == [0, 0, 0] for x in Wh)
check("C1 [T]", okC1, "each of CL-1's half-ticks (even step on R_e, odd step on R_o(K)) commutes with the site-gauged (111) turn on "
      "the axis, so (floquet-pi-slab B1) each has W = 0 and so does the whole tick (with or without the mass angle): a stack of "
      "adopted half-ticks has W = 0 for ANY number and parity, so q_mirror = q_light", f"[T3, half-tick] {hc:.0e}; W even, odd, tick, tick(mu 0.2): {Wh}")
print("   C2 [T] FREEZE (W_F != 0) is a five-layer e.o.e.o.e circuit (twist-local-single) with no turn-commuting layering at any depth "
      "(floquet-pi-slab B2), so its half-ticks carry no sector winding of their own: the unit of W is the whole FREEZE tick. Its "
      "period fixes half-ticks per tick (5), not the number of FREEZE ticks in the stack, so the tick's own period cannot fix n")

# ================================================================ D. consistency reading and synthesis
print("== D. consistency reading (NOT an adopted rule) and synthesis")
okD = WFi != WF and Wh[2] == [0, 0, 0] and WF != [0, 0, 0]
check("D1 [T]", okD, "F^+ is no regauging of F by any K-continuous turn-commuting unitary (that would keep W; W(F^+) = -W_F), so "
      "the inverse layers are a SUPPLIED orientation field (CL-1 has one universal step eps); n is its net charge. The only "
      "parity-fixing condition found is 'the slab's compactified tick has the winding of the update's own tick': with the adopted "
      "CL-1 tick (W = 0) it forces n = 0, EVEN (q_mirror = q_light, the wrong parity); with FREEZE as the update it forces n = 1",
      f"W(CL-1 tick) {Wh[2]}, W_F {WF}")
P = dict(a_zoom=False, b_fold=False, c_halftick=False, d_adopted=False)
print(f"   synthesis (criteria_pre_run): forced odd by {P} -> FAIL: no adopted rule fixes n (or the label bond pattern). Odd n is "
      "equivalent to adopting a W != 0 (FREEZE-class) update tick. Minimality 3 over 6: NO, no candidate touches the family count")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
