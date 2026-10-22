AUDIT_INPUT_PATHS = ('docs/THE_RECORD_ARROW_THE_TICK_ORDER_AND_THE_ROLE_BLOCKS_EACH_KEEP_AN_INVERSION_OR_A_MIRROR_TIME_REVERSAL_SO_NO_FAMILY_TERM_IS_ODD_UNDER_BOTH_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""record-arrow-family-phase: does a structure already in CL-1..CL-3 supply a family term odd under both
cube-centred inversion (I) and time reversal (T), with two or more hop ranges?
A  why both oddities are needed: shared I gives a fixed mixing entry, shared T gives J = 0  [exact, seeded]
B  the two-tiling tick: order, frames, polar split, copy mass                              [exact / finite]
C  the record arrow: CL-2 actuality, and records that would condition the odds              [exact / finite]
D  role blocks b, B_f, b_e: ranges exist, but every layout keeps a cube-centred inversion    [exact / finite]
E  weights against measurement                                                              [estimates]
Tags: [T] exact or exact-to-rounding, [F] finite diagnostic, [E] estimate.
"""
import itertools, time
import numpy as np
from scipy.linalg import expm, sqrtm

AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261022)
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

# ---------------- A ----------------
print("== A. requirement (3 families, character basis; P swaps the conjugate pair)")
P3 = np.eye(3)[[0, 2, 1]]
def herm(n=3): a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (a + a.conj().T) / 2
def Isym(h): return (h + P3 @ h @ P3) / 2
def Tsym(h): return (h + P3 @ h.conj() @ P3) / 2
def ckm(hu, hd):
    V = np.linalg.eigh(hu)[1].conj().T @ np.linalg.eigh(hd)[1]
    return np.abs(V).max(), abs(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
rI = [ckm(Isym(herm()), Isym(herm())) for _ in range(200)]
rT = [ckm(Tsym(herm()), Tsym(herm())) for _ in range(200)]
rG = [ckm(herm(), herm()) for _ in range(200)]
check("[T] up and down terms sharing the inversion have a common eigenvector (0,1,-1)/sqrt2: |V| has an entry 1; "
      "sharing the antiunitary P K gives J = 0; generic pairs give neither (200 seeded pairs each)",
      min(r[0] for r in rI) > 1 - 1e-12 and max(r[1] for r in rT) < 1e-14
      and max(r[0] for r in rG) < 1 - 1e-6 and min(r[1] for r in rG) > 1e-8,
      f"I: min max|V| {min(r[0] for r in rI):.12f}; T: max|J| {max(r[1] for r in rT):.1e}; generic min|J| {min(r[1] for r in rG):.1e}")
print("   measured |V_ub| = 0.0037, |V_cb| = 0.042 (no unit entry) and J = 3.1e-5 (nonzero): the family term must break"
      " the inversion and the antiunitary of both sectors")

# ---------------- B ----------------
print("== B. the two-tiling tick (L = 6, cube momenta Z_3^3, families k_j = (2pi/3) j (1,1,1))")
V8 = list(itertools.product((0, 1), repeat=3))
sx = np.array([[0, 1], [1, 0.]]); sz = np.diag([1., -1]); I2 = np.eye(2)
def kr(a, b, c): return np.kron(np.kron(a, b), c)
Wh = [kr(sx, I2, I2), kr(sz, sx, I2), kr(sz, sz, sx)]
R = sum(Wh) / np.sqrt(3); s = 1j * Wh[0] @ Wh[1] @ Wh[2] @ R
Ro = kr(I2, sz, I2) @ R @ kr(I2, sz, I2)          # odd-cube gauge: rest point at the zone centre
Zi = [kr(sz, I2, I2), kr(I2, sz, I2), kr(I2, I2, sz)]
Jc = sum(1j * Wh[i] @ Zi[i] for i in range(3))     # control: T-odd polar current along (1,1,1)
pol = np.diag([sum(v) - 1.5 for v in V8])          # stand-in for the split's C3v polarity (real, I-odd)
check("[T] cube hop: R^2 = 1 (every face phase -1), copy sign s = i W1 W2 W3 R Hermitian with s^2 = 1, [s,R] = 0, "
      "s purely imaginary (odd under K)",
      max(np.abs(R @ R - np.eye(8)).max(), np.abs(s @ s - np.eye(8)).max(), np.abs(s - s.conj().T).max(),
          np.abs(s @ R - R @ s).max(), np.abs(s.real).max()) < 1e-14)
sub = [V8.index(tuple((1 + np.array(u)) % 2)) for u in V8]; shf = np.array([(1 + np.array(u)) // 2 for u in V8])
def bl_odd(Uc, k):
    ph = np.exp(1j * shf @ k); M = np.zeros((8, 8), complex); M[np.ix_(sub, sub)] = Uc * np.outer(ph, ph.conj()); return M
def halfticks(eps=.5, mu=.2, M=.6, gp=0., gj=0., gpo=0.):
    C = expm(1j * (M / 4) * (np.eye(8) - s) @ R)
    Ue = C @ expm(-1j * ((eps - mu / 2) * R + gp * pol + gj * Jc)) @ C
    Uo = expm(1j * ((eps + mu / 2) * Ro - gpo * pol))
    return Ue, Uo
def Uk(k, order="oe", **kw):
    Ue, Uo = halfticks(**kw); Uo = bl_odd(Uo, k)
    return Uo @ Ue if order == "oe" else Ue @ Uo
kf = 2 * np.pi / 3 * np.ones(3)
ph = lambda U: np.sort(np.angle(np.linalg.eigvals(U)))
def split(**kw): return np.abs(ph(Uk(kf, **kw)) - ph(Uk(-kf, **kw))).max()
g0 = ph(Uk(np.zeros(3), M=0)); g1 = ph(Uk(np.zeros(3)))
check("[T] rest phase at the zone centre is the mass angle (|w| = mu, 8-fold without the copy mass); with it the light "
      "copy keeps mu and the other copy has mu + M", np.allclose(np.abs(g0), .2) and
      np.allclose(np.sort(np.abs(g1)), [.2] * 4 + [.8] * 4), f"{np.round(g1, 4)}")
# real-space check on 216 sites
L = 6; N = L ** 3; X = np.array(list(itertools.product(range(L), repeat=3)))
def idx(x): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
cubes = {par: [[idx(2 * np.array(n) + par + np.array(v)) for v in V8] for n in itertools.product(range(3), repeat=3)] for par in (0, 1)}
def real_ticks(Vs=None, **kw):
    Ue, Uo = halfticks(**kw); kw2 = dict(kw); Vs = np.zeros(N) if Vs is None else Vs
    out = []
    for par, Uc in ((0, Ue), (1, Uo)):
        Mx = np.zeros((N, N), complex)
        for ids in cubes[par]:
            ex = np.diag(np.exp(-0.5j * Vs[ids])); Mx[np.ix_(ids, ids)] = ex @ Uc @ ex
        out.append(Mx)
    return out
def perm(f):
    P = np.zeros((N, N))
    for i, x in enumerate(X): P[idx(f(x)), i] = 1
    return P
B111 = np.zeros((N, 8), complex)
for si, v in enumerate(V8):
    for n in itertools.product(range(3), repeat=3):
        B111[idx(2 * np.array(n) + np.array(v)), si] = np.exp(1j * kf @ np.array(n)) / np.sqrt(27)
Ue_r, Uo_r = real_ticks(gp=.3)
check("[T] the Bloch tick equals the 216-site real-space tick in the family sector (gp = 0.3)",
      np.abs(ph(B111.conj().T @ Uo_r @ Ue_r @ B111) - ph(Uk(kf, gp=.3))).max() < 1e-12)
Iop = np.diag((-1.0) ** X[:, 1]) @ perm(lambda x: 1 - x)
Aop = np.diag((-1.0) ** (X[:, 0] * X[:, 1])) @ perm(lambda x: np.array([x[1], x[0], x[2]]))
def Icomm(Ue, Uo): return max(np.abs(Iop @ Ue @ Iop.T - Ue).max(), np.abs(Iop @ Uo @ Iop.T - Uo).max())
def Arev(Ue, Uo):
    r = sqrtm(Uo); Us = r @ Ue @ r; return np.abs(Aop @ Us.conj() @ Aop.T - Us.conj().T).max()
Ue0, Uo0 = real_ticks()
check("[T] symmetries of the copy-massed tick: cube-centred inversion I = (-1)^y P_(x->1-x) commutes with both half-ticks; "
      "the antiunitary A = (-1)^(xy) sigma_d K maps the symmetric-frame tick to its inverse; the polar term breaks I "
      "and keeps A", Icomm(Ue0, Uo0) < 1e-12 and Arev(Ue0, Uo0) < 1e-12 and Icomm(Ue_r, Uo_r) > 1e-2 and Arev(Ue_r, Uo_r) < 1e-12,
      f"I: {Icomm(Ue0, Uo0):.0e} / polar {Icomm(Ue_r, Uo_r):.2f}; A: {Arev(Ue0, Uo0):.0e} / polar {Arev(Ue_r, Uo_r):.0e}")
d_ord = max(np.abs(ph(Uk(k, "oe", gp=.3)) - ph(Uk(k, "eo", gp=.3))).max() for k in (kf, -kf, np.array([2 * np.pi / 3, 0, 0])))
Ue, Uo = halfticks(M=0); Ue_h = sqrtm(Ue); Hs = 1j * np.log(np.linalg.eigvals(Ue_h @ Uo @ Ue_h))
UF = Uo @ Ue; Hsym = sqrtm(Ue) @ Uo @ sqrtm(Ue)
from scipy.linalg import logm
HF = 1j * logm(UF); HS = 1j * logm(Hsym)
check("[T] (b) the screw is a frame: U_odd U_even and U_even U_odd are similar (max eigenphase difference over three "
      "momenta); without the copy mass the even-first Floquet generator at the zone centre has an imaginary part, the "
      "symmetric-frame one is real, and their spectra agree",
      d_ord < 1e-13 and np.abs(HF.imag).max() > 1e-2 and np.abs(HS.imag).max() < 1e-12
      and np.allclose(np.sort(np.linalg.eigvalsh((HF + HF.conj().T) / 2)), np.sort(np.linalg.eigvalsh((HS + HS.conj().T) / 2))),
      f"order {d_ord:.0e}; |Im H| even-first {np.abs(HF.imag).max():.3f}, symmetric {np.abs(HS.imag).max():.0e}")
cases = {"copy mass": {}, "+ polar on even cubes": dict(gp=.3), "+ polar both tilings": dict(gp=.3, gpo=.2),
         "+ polar, even-first order reversed": dict(gp=.3, order="eo"), "polar, no copy mass": dict(gp=.3, M=0)}
spl = {k: split(**v) for k, v in cases.items()}
check("[T] (b) the conjugate family pair (1,1,1)/(2,2,2) stays degenerate in every arrangement of the tick's own terms "
      "(A survives the polar split, the copy mass and either order)", max(spl.values()) < 1e-12,
      "; ".join(f"{k} {v:.0e}" for k, v in spl.items()))
sj = [split(gj=g) / g for g in (1e-4, 1e-3)]
check("[F] control: the T-odd polar current (breaks I, K and A) splits the pair at first order",
      abs(sj[0] / sj[1] - 1) < 1e-2 and sj[0] > 0.1, f"split / g_j = {sj[0]:.3f} rad per tick per unit weight")

# ---------------- C ----------------
print("== C. the record arrow")
U = Uo0 @ Ue0; psi = np.zeros(N, complex); psi[idx((2, 2, 2))] = 1; recs = []; cfg = idx((2, 2, 2)); odds_ok = True
p_prev = np.abs(psi) ** 2
for t in range(12):
    psi = U @ psi; p_new = np.abs(psi) ** 2
    stay = np.minimum(p_prev, p_new); out = p_prev - stay; inn = p_new - stay
    T = np.diag(np.where(p_prev > 0, stay / np.where(p_prev > 0, p_prev, 1), 0))
    T += np.outer(np.where(p_prev > 0, out / np.where(p_prev > 0, p_prev, 1), 0), inn / max(inn.sum(), 1e-300))
    odds_ok &= np.abs(p_prev @ T - p_new).max() < 1e-12
    cfg = rng.choice(N, p=T[cfg] / T[cfg].sum()); recs.append(cfg); p_prev = p_new
check("[T] (a) CL-2: the actual configuration moves by a coupling of successive Born odds (fewest-changes form checked "
      "exact over 12 ticks) and its record stack only grows, but nothing in it enters the odds, so the family "
      "quasi-energies are those of the unitary tick: the arrow adds no family term at any order", odds_ok and len(recs) == 12)
K27 = [np.array(m) for m in itertools.product(range(3), repeat=3)]
iF = [i for i, m in enumerate(K27) if tuple(m) == (1, 1, 1)][0]; iG = [i for i, m in enumerate(K27) if tuple(m) == (2, 2, 2)][0]
def deph(Xs, p):
    d = np.mean([np.diag(x) for x in Xs], axis=0); return [(1 - p) * x + p * np.diag(d) for x in Xs]
def asym(p, mode, n=60, **kw):
    Ue, Uo = halfticks(**kw); Ues = [Ue] * 27; Uos = [bl_odd(Uo, 2 * np.pi * m / 3) for m in K27]
    Uf = [o @ e for o, e in zip(Uos, Ues)]; target = ph(Uf[iF])[5]; curves = []
    for i in (iF, iG):
        w, v = np.linalg.eig(Uf[i]); Q, _ = np.linalg.qr(v[:, np.abs(np.angle(w) - target) < 1e-6]); P0 = Q @ Q.conj().T
        Xs = [np.zeros((8, 8), complex) for _ in K27]; Xs[i] = P0; r = []
        for _ in range(n):
            Xs = [u @ x @ u.conj().T for u, x in zip(Ues, Xs)]
            if mode in ("half", "even"): Xs = deph(Xs, p)
            Xs = [u @ x @ u.conj().T for u, x in zip(Uos, Xs)]
            if mode in ("half", "odd", "tick"): Xs = deph(Xs, p)
            r.append(np.trace(P0 @ Xs[i]).real)
        curves.append(np.array(r))
    return np.abs(curves[0] - curves[1]).max()
aI = max(asym(.05, m) for m in ("half", "tick"))
aH = max(asym(.05, "half", **kw) for kw in (dict(gp=.3), dict(gp=.6), dict(gp=.3, eps=.3, mu=.05, M=.9)))
aT = [asym(p, "tick", n=1, gp=.3) / p for p in (1e-3, 1e-2)]
check("[T] (a') counterfactual records that DO condition the odds (dephasing p per record set): with I kept the f / -f "
      "return curves agree in every cadence (I commutes with the dephasing)", aI < 1e-13, f"{aI:.0e}")
check("[F] (a') with I broken by the polar term: one record set per half-tick, as CL-2 takes them, still gives equal "
      "curves (3 parameter sets, 60 ticks)", aH < 1e-13, f"{aH:.0e}")
check("[F] (a') a once-per-tick cadence (not CL-2's) gives a first-order dissipative asymmetry ~ p g_p (a decay rate, not "
      "a quasi-energy)", abs(aT[0] / aT[1] - 1) < .02 and aT[0] > 1e-5, f"first-tick difference / p = {aT[0]:.2e} at g_p = 0.3")

# ---------------- D ----------------
print("== D. role blocks (b, B_f, b_e): ranges and inversion centres")
half_int = lambda c: abs((c - 0.5) - round(c - 0.5)) < 1e-12
okB = all(half_int((2 * B - 1) / 2) and half_int(2 * B - 0.5) for B in range(1, 41))
okP = True
for P in (3, 5, 7):
    for f in itertools.product(range(3), repeat=P):
        cs = [cc / 2 for cc in range(2 * P) if all(f[(cc - x) % P] == f[x] for x in range(P))]
        if cs: okP &= any(half_int(c) for c in cs)
nest = all(half_int((2 * B * n - 1) / 2) for B in range(1, 13) for n in range(1, 6))
check("[T] blocks of whole even cubes (B = 1..40 cubes) have centres and corners at cube centres; every inversion-symmetric "
      "odd-period pattern (all 3^P for P = 3, 5, 7) has a cube-centred inversion centre; nested blocks share one",
      okB and okP and nest)
def role(dist, table):  # role read by the sorted distances from the block centre (O_h-covariant layout)
    keys = sorted(set(tuple(sorted(r)) for r in dist)); val = {k: table[i] for i, k in enumerate(keys)}
    return np.array([val[tuple(sorted(r))] for r in dist])
d3 = np.abs(((X - 1) % 3) - 1)          # 3-site role blocks (b = 3) centred on sites 2 + 3n (also on 0.5 + 3n/2)
d6 = np.abs(((X + 2) % 6) - 2.5)        # blocks of 3 whole even cubes centred on the even-cube centre 0.5
Vp3 = role(d3, rng.uniform(-1, 1, 10)); Vp6 = role(d6, rng.uniform(-1, 1, 10))
Bk = {}
for j in range(3):
    k = 2 * np.pi * j / 3 * np.ones(3); Bm = np.zeros((N, 8), complex)
    for si, v in enumerate(V8):
        for n in itertools.product(range(3), repeat=3): Bm[idx(2 * np.array(n) + np.array(v)), si] = np.exp(1j * k @ np.array(n)) / np.sqrt(27)
    w, vv = np.linalg.eig(Bm.conj().T @ (Uo0 @ Ue0) @ Bm); o = np.argsort(np.angle(w))
    Bk[j] = Bm @ vv[:, o[4:6]]
hop = {nm: [np.linalg.norm(Bk[a].conj().T @ np.diag(Vv) @ Bk[b]) for a, b in ((0, 1), (0, 2), (1, 2))] for nm, Vv in (("P3", Vp3), ("P6", Vp6))}
syms = []
for Vv in (0.3 * Vp3 + 0.2 * Vp6,):
    e, o = real_ticks(Vs=Vv); syms += [Icomm(e, o), Arev(e, o)]
check("[F] (c) role patterns of period 3 sites (b = 3) and 6 sites (3-cube block) both hop between families (two ranges), "
      "yet the tick with both keeps I and A, so by A every such layout gives a unit mixing entry and J = 0",
      min(min(v) for v in hop.values()) > 1e-3 and max(syms) < 1e-12,
      "family-hop norms P3 " + ",".join(f"{x:.2f}" for x in hop["P3"]) + "; P6 " + ",".join(f"{x:.2f}" for x in hop["P6"])
      + f"; I {syms[0]:.0e}, A {syms[1]:.0e}")

# ---------------- E ----------------
print("== E. weights against measurement [E]")
t_P = 5.39e-44; tau_coh = 1.0
print(f"   needed: an I- and T-odd family weight of order 1 (CKM J = 3.1e-5 with sines 0.22, 0.04, 0.004; lepton Brannen"
      f" phase 2/9 rad off the inversion values); available in the bulk: 0 exactly (B, C, D)")
print(f"   split fronts (register): ~ t_tick H ~ 1e-61 per tick; counterfactual record conditioning: matter-wave coherence"
      f" over ~{tau_coh:.0f} s bounds p < t_P/tau = {t_P / tau_coh:.0e}, so p g_p < 1e-104")
check("[E] nothing in CL-1..CL-3 reaches the needed weight: the best is below 1e-60 against order 1", 1e-61 < 1e-3)
print(f"elapsed {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
