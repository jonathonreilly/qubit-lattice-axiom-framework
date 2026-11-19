#!/usr/bin/env python3
"""cp-mixing-unify: can the heavy-coset singlet vacua sigma_t that give the zoom-3
Nelson-Barr rule (theta_bar = 0) also be the translation-breaking source of
quark and lepton mixing?

Model (zoom-3 translation characters, as in strong-cp-revisit F): light rows
l_j and light doublet columns Q_k carry L_j = (j,j,j); heavy copies a carry
h_a = h0 + L_a (rows qc_a) and -h_a (columns X_a), h0 = (0,1,2); the doublet
carries c_H in L; one complex vacuum sigma_t per heavy-coset character h0 + L_t,
shared by every sector; every coefficient is real (the kept antiunitary).
A. targets. B. character texture (theorem). C. integrating out the copies:
light m^dag m = y^T P y (theorem, checked), arg det = 0. D. scaling: one
spurion step, no tower. E. fit-free ensembles vs measurement, anarchy null,
look-elsewhere count. F. leptons with Dirac neutrinos (PMNS).
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np

T0 = time.time()
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))
rng = np.random.default_rng(20261022)

# ---------------- A. measured targets ----------------
MEAS = dict(u32=1 / 277., u21=1 / 504., d32=1 / 53.4, d21=1 / 19.9,
            Vus=0.2250, Vcb=0.0418, Vub=0.00369, J=3.12e-5)
LEPM = dict(e32=1 / 16.8, e21=1 / 206.8, s12=0.307, s23=0.561, s13=0.02195, r21=7.49e-5 / 2.513e-3)
print("== A. targets [M]: running quark masses at M_Z, PDG 2024 CKM, NuFIT 6.0 normal ordering")
check("[M] m2/m3, m1/m2: up 3.6e-3, 2.0e-3; down 1.9e-2, 5.0e-2; |V_us|,|V_cb|,|V_ub| = 0.225, 0.042, 0.0037; J = 3.1e-5; "
      "PMNS sin^2 = 0.307, 0.561, 0.022; dm21/dm31 = 0.030", True)

# ---------------- B. character texture ----------------
print("== B. character texture at renormalisable order")
L = [np.array([j, j, j]) for j in range(3)]
h0 = np.array([0, 1, 2])
COS = [np.mod(h0 + L[t], 3) for t in range(3)]
def zero(x): return not np.mod(x, 3).any()
def vac_index(kap):
    """(t, conj) if a single vacuum sigma_t (or sigma_t^*) carries character kap, else None"""
    kap = np.mod(kap, 3)
    for t, c in enumerate(COS):
        if np.array_equal(kap, c): return (t, False)
        if np.array_equal(np.mod(-kap, 3), c): return (t, True)
    return None
def texture(cH, Nh):
    """kind of every entry: 'y' Yukawa, 'M' bare, ('s',t,conj) vacuum, 'd5' needs H x vacuum (dimension five), 0 forbidden"""
    rows = [("l", L[j]) for j in range(3)] + [("qc", np.mod(h0 + L[a], 3)) for a in range(Nh)]
    cols = [("Q", L[k]) for k in range(3)] + [("X", np.mod(-(h0 + L[a]), 3)) for a in range(Nh)]
    T = {}
    for i, (rn, rc) in enumerate(rows):
        for k, (cn, cc) in enumerate(cols):
            needsH = (cn == "Q")                       # every row is a gauge singlet; Q is the doublet
            kap = -(rc + cc + (cH if needsH else 0))
            if zero(kap): T[i, k] = "y" if needsH else "M"
            else:
                vi = vac_index(kap)
                T[i, k] = ("d5" if needsH else ("s",) + vi) if vi is not None else 0
    return T
ok = True; desc = []
for cH in L:
    for Nh in (1, 2, 3):
        T = texture(cH, Nh)
        yy = np.array([[T[j, k] == "y" for k in range(3)] for j in range(3)])
        perm = yy.sum(0).tolist() == [1, 1, 1] and yy.sum(1).tolist() == [1, 1, 1]
        lh = all(isinstance(T[j, 3 + a], tuple) and T[j, 3 + a][2] is False and T[j, 3 + a][1] == (a - j) % 3
                 for j in range(3) for a in range(Nh))
        hl = all(T[3 + a, k] == "d5" for a in range(Nh) for k in range(3))
        hh = all((T[3 + a, 3 + b] == "M") == (a == b) and (T[3 + a, 3 + b] in ("M", 0)) for a in range(Nh) for b in range(Nh))
        ok &= perm and lh and hl and hh
check("[T] for every doublet character c_H in L and 1-3 heavy copies: the light Yukawa block is a monomial (one entry per row "
      "and column, translation-invariant: no light-light mixing); every light-heavy singlet entry l_j X_a is filled by exactly "
      "one vacuum, sigma_{a-j}; heavy-light needs H x vacuum (dimension five, the Nelson-Barr zero); heavy-heavy is diagonal "
      "and bare. All mixing therefore runs through the heavy copies", ok)
# minimal spurion degree for each light-light character difference
def min_deg(target):
    best = None
    for deg in range(0, 5):
        for n in range(0, deg + 1):
            m = deg - n
            for combo in itertools.product(range(3), repeat=n + m):
                s = sum((COS[t] for t in combo[:n]), np.zeros(3)) - sum((COS[t] for t in combo[n:]), np.zeros(3))
                if zero(s - target): return n + m
    return best
degs = {d: min_deg(L[d]) for d in (1, 2)}
check("[T] no tower: a light-light entry between families j != k needs character L_k - L_j in {L_1, L_2}; sigma alone carries "
      "only the heavy coset, so the minimal insertion is sigma_t sigma_t'^* (degree 2) for BOTH nonzero differences. Z_3 has "
      "one nonzero character up to conjugation, so all three family pairs (12, 23, 13) open at the same order",
      degs[1] == 2 and degs[2] == 2, f"minimal degrees {degs}")

# ---------------- C. integrate out ----------------
def build(Nh, r, y, cB, Mh, sig, M0, eps=0.0, cE=None):
    """batched: rows l(3), qc(Nh); cols Q(3), X(Nh). y: (S,3) monomial values on the pattern j+k = 0 mod 3 (c_H = 0)"""
    S = y.shape[0]; n = 3 + Nh
    M = np.zeros((S, n, n), complex)
    for j in range(3): M[:, j, (-j) % 3] = y[:, j]
    for j in range(3):
        for a in range(Nh): M[:, j, 3 + a] = cB[:, j, a] * sig[:, (a - j) % 3] * r * M0
    for a in range(Nh): M[:, 3 + a, 3 + a] = Mh[:, a] * M0
    if eps and cE is not None:
        for a in range(Nh):
            for k in range(3): M[:, 3 + a, k] = eps * cE[:, a, k] * np.conj(sig[:, (a + k) % 3])
    return M
def light(M):
    U, s, Vh = np.linalg.svd(M)
    s = s[:, ::-1][:, :3]; V = np.conj(np.swapaxes(Vh, 1, 2))[:, :, ::-1][:, :3, :3]   # doublet components of light states
    return s, V
def draw(S, Nh, dist):
    if dist == "normal":
        f = lambda *sh: rng.normal(size=sh)
    else:
        f = lambda *sh: np.exp(rng.uniform(np.log(1 / 3), np.log(3), size=sh)) * rng.choice([-1, 1], size=sh)
    return f
print("== C. integrating out the heavy copies")
S = 300; Nh = 2; M0 = 1e3
f = draw(S, Nh, "normal")
sig = rng.uniform(0.5, 1.5, (S, 3)) * np.exp(1j * rng.uniform(0, 2 * np.pi, (S, 3)))
y = f(S, 3); cB = f(S, 3, Nh); Mh = np.abs(f(S, Nh)) + 0.3
Mfull = build(Nh, 1.0, y, cB, Mh, sig, M0)
s, V = light(Mfull)
B = np.zeros((S, 3, Nh), complex)
for j in range(3):
    for a in range(Nh): B[:, j, a] = cB[:, j, a] * sig[:, (a - j) % 3] * M0
Mh2 = np.einsum("sa,ab->sab", (Mh * M0) ** 2, np.eye(Nh))
P = np.eye(3) - B @ np.linalg.inv(np.conj(np.swapaxes(B, 1, 2)) @ B + Mh2) @ np.conj(np.swapaxes(B, 1, 2))
Y = np.zeros((S, 3, 3)); [Y.__setitem__((slice(None), j, (-j) % 3), y[:, j]) for j in range(3)]
mm = np.swapaxes(Y, 1, 2) @ P @ Y
ev = np.sqrt(np.abs(np.linalg.eigvalsh(mm)))
relerr = np.max(np.abs(ev - s) / s)
dets = np.angle(np.linalg.det(Mfull))
check("[T, checked] integrating out: the light antiquarks are the complement of the heavy combinations, so the light "
      "m^dag m = y^T P y with P = 1 - B (B^dag B + M_h^2)^-1 B^dag (B_ja = c_ja sigma_{a-j}); y real, so arg det = 0 "
      "exactly while P is complex: the mixing and the CP phase both come from P alone",
      relerr < 1e-4 and np.max(np.abs(np.sin(dets))) < 1e-9, f"300 samples, max rel err {relerr:.0e} (O(v^2/M^2)), max |sin arg det| {np.max(np.abs(np.sin(dets))):.0e}")

# ---------------- D. scaling with r = sigma/M ----------------
print("== D. scaling with r = sigma/M (fixed couplings, 300 samples, medians)")
def sector(S, Nh, dist, r, sig, M0=1e3, eps=0.0):
    f = draw(S, Nh, dist)
    y = f(S, 3); cB = f(S, 3, Nh); Mh = np.abs(f(S, Nh))
    if dist == "normal": Mh = Mh + 0.3
    cE = f(S, Nh, 3)
    return dict(y=y, cB=cB, Mh=Mh, cE=cE, Nh=Nh)
def run(par, r, sig, M0=1e3, eps=0.0):
    return light(build(par["Nh"], r, par["y"], par["cB"], par["Mh"], sig, M0, eps, par["cE"]))
def jarl(V): return np.imag(V[:, 0, 1] * V[:, 1, 2] * np.conj(V[:, 0, 2]) * np.conj(V[:, 1, 1]))
def offperm(V):
    """the six moduli off the nearest permutation"""
    A = np.abs(V); out = []
    for p in itertools.permutations(range(3)):
        mask = np.ones((3, 3), bool); mask[range(3), p] = False
        out.append((A[:, ~mask].sum(1), A[:, mask]))
    best = np.argmax(np.stack([o[0] for o in out]), axis=0)
    return np.stack([out[b][1][i] for i, b in enumerate(best)])
S = 300
sig = rng.uniform(0.5, 1.5, (S, 3)) * np.exp(1j * rng.uniform(0, 2 * np.pi, (S, 3)))
rs_small = [1e-3, 3e-3, 1e-2]
pu = sector(S, 2, "normal", 0, sig); pd = sector(S, 2, "normal", 0, sig)
med = []
for r in rs_small:
    (su, Vu), (sd, Vd) = run(pu, r, sig), run(pd, r, sig)
    Vc = np.conj(np.swapaxes(Vu, 1, 2)) @ Vd
    med.append(np.median(np.sort(offperm(Vc), axis=1), axis=0))
med = np.array(med)
sl = np.polyfit(np.log10(rs_small), np.log10(med), 1)[0]
check("[T, checked] r << 1: masses are the monomial y values (order one, no hierarchy) and the CKM is a permutation plus "
      "O(r^2) in all six off-permutation entries: one common power, no epsilon-tower (|V_us|:|V_cb|:|V_ub| ~ 1:1:1)",
      np.all(np.abs(sl - 2) < 0.15), "slopes of the six sorted off-permutation moduli " + " ".join(f"{x:.2f}" for x in sl))
rs_big = [10., 30., 100.]
res = {}
for Nh in (1, 2, 3):
    pu = sector(S, Nh, "normal", 0, sig)
    ms = []
    for r in rs_big:
        su, _ = run(pu, r, sig)
        ms.append(np.median(su / su[:, 2:3], axis=0))
    res[Nh] = np.polyfit(np.log10(rs_big), np.log10(np.array(ms)[:, :2]), 1)[0]
check("[T, checked] r >> 1: P tends to the projector on ker B^dag, so N_h light masses fall as M/sigma and 3 - N_h stay at "
      "y v: N_h = 1 gives one light + two heavy, N_h = 2 gives m1 ~ m2 ~ (M/sigma) m3, N_h = 3 gives all three ~ M_a/sigma "
      "(ratios set by the bare copy masses). One step of hierarchy per regime, never two",
      abs(res[1][0] + 1) < 0.1 and abs(res[1][1]) < 0.1 and abs(res[2][0] + 1) < 0.1 and abs(res[2][1] + 1) < 0.1
      and abs(res[3][0]) < 0.1 and abs(res[3][1]) < 0.1,
      "slopes (m1/m3, m2/m3): " + "; ".join(f"Nh={k}: {v[0]:.2f},{v[1]:.2f}" for k, v in res.items()))

# ---------------- E. ensembles vs measurement ----------------
print("== E. fit-free ensembles: shared sigma_t, order-one real couplings, r the only parameter (500 per cell)")
WIN = np.log10(2.0)
def quark_obs(su, Vu, sd, Vd):
    Vc = np.conj(np.swapaxes(Vu, 1, 2)) @ Vd
    return dict(u32=su[:, 1] / su[:, 2], u21=su[:, 0] / su[:, 1], d32=sd[:, 1] / sd[:, 2], d21=sd[:, 0] / sd[:, 1],
                Vus=np.abs(Vc[:, 0, 1]), Vcb=np.abs(Vc[:, 1, 2]), Vub=np.abs(Vc[:, 0, 2]), J=np.abs(jarl(Vc)))
def hits(obs, meas):
    return {k: np.abs(np.log10(obs[k] / meas[k])) < WIN for k in meas}
KM = ["u32", "u21", "d32", "d21"]; KC = ["Vus", "Vcb", "Vub", "J"]
S = 500; rgrid = [10 ** x for x in np.arange(-2, 2.01, 0.5)]
cells = 0; best = dict(joint=0, ckm=0, mass=0); perobs = {k: 0.0 for k in MEAS}; thmax = 0.0
tot = dict(ckm=0, mass=0, n=0); medtab = {}; hitcells = []
ckm_ratio = []
for Nh in (1, 2, 3):
    for dist in ("normal", "loguni"):
        for blind in (False, True):
            for r in rgrid:
                cells += 1
                sig = rng.uniform(0.5, 1.5, (S, 3)) * np.exp(1j * rng.uniform(0, 2 * np.pi, (S, 3)))
                pu = sector(S, Nh, dist, r, sig); pd = sector(S, Nh, dist, r, sig)
                if blind: pd = dict(pd, cB=pu["cB"], Mh=pu["Mh"])           # species-blind heavy sector
                Mu = build(Nh, r, pu["y"], pu["cB"], pu["Mh"], sig, 1e3); Md = build(Nh, r, pd["y"], pd["cB"], pd["Mh"], sig, 1e3)
                thmax = max(thmax, np.max(np.abs(np.sin(np.angle(np.linalg.det(Mu)) + np.angle(np.linalg.det(Md))))))
                o = quark_obs(*light(Mu), *light(Md)); h = hits(o, MEAS)
                for k in MEAS: perobs[k] = max(perobs[k], h[k].mean())
                hm = np.all([h[k] for k in KM], 0); hc = np.all([h[k] for k in KC], 0)
                if hc.any(): hitcells.append((Nh, dist[0], int(blind), float(round(r, 2)), int(hc.sum())))
                best["mass"] = max(best["mass"], hm.mean()); best["ckm"] = max(best["ckm"], hc.mean())
                best["joint"] = max(best["joint"], (hm & hc).sum())
                tot["ckm"] += int(hc.sum()); tot["mass"] += int(hm.sum()); tot["n"] += S
                if dist == "normal" and not blind and r in (rgrid[0], rgrid[-1]):
                    medtab[(Nh, r)] = (np.median(o["Vus"]), np.median(o["Vcb"]), np.median(o["Vub"]), np.median(o["u32"]), np.median(o["u21"]))
                if 0.05 < r < 20:
                    ckm_ratio.append((r, np.median(o["Vcb"] / o["Vus"]), np.median(o["Vub"] / o["Vcb"])))
check("[T, checked] theta_bar: arg det(M_u M_d) = 0 in every sample of every cell (shared vacua, both sectors)", thmax < 1e-9,
      f"{cells} cells x {S}, max |sin theta_bar| {thmax:.0e}")
rat = np.array(ckm_ratio)
check("[F] no hierarchy among the angles at any r: median |V_cb/V_us| and |V_ub/V_cb| stay order one (measured 0.19, 0.088)",
      np.min(rat[:, 1]) > 0.3 and np.min(rat[:, 2]) > 0.3,
      f"min medians over cells {np.min(rat[:, 1]):.2f}, {np.min(rat[:, 2]):.2f}")
# anarchy null
Sa = 20000
def anarchic(S):
    A = rng.normal(size=(S, 3, 3)) + 1j * rng.normal(size=(S, 3, 3))
    U, s, Vh = np.linalg.svd(A); return s[:, ::-1], np.conj(np.swapaxes(Vh, 1, 2))[:, :, ::-1]
oa = quark_obs(*anarchic(Sa), *anarchic(Sa)); ha = hits(oa, MEAS)
am = np.all([ha[k] for k in KM], 0).mean(); ac = np.all([ha[k] for k in KC], 0).mean()
for (Nh_, r_), v in medtab.items():
    print(f"   N_h={Nh_} r={r_:6.2f}: median |V_us| {v[0]:.2e} |V_cb| {v[1]:.2e} |V_ub| {v[2]:.2e}; m2/m3 {v[3]:.2e} m1/m2 {v[4]:.2e}")
print("   best per-observable hit fraction over cells (factor 2): " + ", ".join(f"{k} {v:.3f}" for k, v in perobs.items()))
print(f"   best over cells: all 4 mass ratios {best['mass']:.4f}, all 4 CKM {best['ckm']:.4f}, joint hits {best['joint']} / {S};"
      f" anarchy null: masses {am:.4f}, CKM {ac:.4f}")
print(f"   totals over all cells: CKM 4-hits {tot['ckm']} / {tot['n']} = {tot['ckm'] / tot['n']:.1e}, mass 4-hits {tot['mass']}")
# null 2: one-parameter small-angle unitary V = exp(i e A), A GUE, same r grid, same count
nh2 = 0; SN = 6000
for e in rgrid:
    A = rng.normal(size=(SN, 3, 3)) + 1j * rng.normal(size=(SN, 3, 3)); A = (A + np.conj(np.swapaxes(A, 1, 2))) / 2
    w, U = np.linalg.eigh(A)
    Vn = U @ (np.exp(1j * e * w)[:, :, None] * np.conj(np.swapaxes(U, 1, 2)))
    o2 = dict(Vus=np.abs(Vn[:, 0, 1]), Vcb=np.abs(Vn[:, 1, 2]), Vub=np.abs(Vn[:, 0, 2]), J=np.abs(jarl(Vn)))
    h2 = hits(o2, {k: MEAS[k] for k in KC}); nh2 += int(np.all(list(h2.values()), 0).sum())
print(f"   CKM-hit cells (N_h, law, blind, r, hits): {hitcells}; null exp(i e A) over the same r grid: {nh2} / {SN * len(rgrid)}")
check("[E] fit-free verdict over 108 cells x 500 (N_h 1-3, two coupling laws, species-blind or not, r = 0.01-100): no sample "
      "hits all eight quark observables within x2 and no sample hits the four mass ratios; the CKM-only 4-hit rate (about 1e-4, "
      "scattered over 7 cells) is within a factor ~4 of a structureless one-parameter small-angle null: no predictive edge",
      best["joint"] == 0 and best["mass"] == 0 and tot["ckm"] / tot["n"] < 5 * max(nh2, 1) / (SN * len(rgrid)),
      f"CKM rate {tot['ckm'] / tot['n']:.1e} vs null {nh2 / (SN * len(rgrid)):.1e}")

# ---------------- F. leptons, Dirac neutrinos ----------------
print("== F. leptons: same structure, Dirac neutrinos (nu^c rows, H~), shared sigma_t")
def pmns_obs(se, Ve, sn, Vn):
    U = np.conj(np.swapaxes(Ve, 1, 2)) @ Vn
    A = np.abs(U) ** 2; s13 = A[:, 0, 2]
    return dict(e32=se[:, 1] / se[:, 2], e21=se[:, 0] / se[:, 1], s12=A[:, 0, 1] / (1 - s13), s23=A[:, 1, 2] / (1 - s13),
                s13=s13, r21=(sn[:, 1] ** 2 - sn[:, 0] ** 2) / (sn[:, 2] ** 2 - sn[:, 0] ** 2))
S = 2000; ang = []
for r in (0.01, 0.1, 1.0, 10.0):
    sig = rng.uniform(0.5, 1.5, (S, 3)) * np.exp(1j * rng.uniform(0, 2 * np.pi, (S, 3)))
    pe = sector(S, 3, "normal", r, sig); pn = sector(S, 3, "normal", r, sig)
    o = pmns_obs(*run(pe, r, sig), *run(pn, r, sig)); h = hits(o, LEPM)
    big = np.mean((o["s12"] > 0.2) & (o["s12"] < 0.45) & (o["s23"] > 0.35) & (o["s23"] < 0.65) & (o["s13"] > 0.01) & (o["s13"] < 0.05))
    ang.append((r, big, np.mean(np.all([h[k] for k in ("s12", "s23", "s13")], 0)), np.mean(np.all(list(h.values()), 0))))
oa = pmns_obs(*anarchic(20000), *anarchic(20000))
anl = np.mean((oa["s12"] > 0.2) & (oa["s12"] < 0.45) & (oa["s23"] > 0.35) & (oa["s23"] < 0.65) & (oa["s13"] > 0.01) & (oa["s13"] < 0.05))
print(f"   anarchy null: PMNS-like {anl:.4f}")
for r, b, a3, aj in ang: print(f"   r = {r:5.2f}: PMNS-like angles (s12 0.2-0.45, s23 0.35-0.65, s13 0.01-0.05) {b:.4f}, three angles within x2 {a3:.4f}, all six {aj:.4f}")
check("[F] PMNS needs r_lepton >~ 1 (large theta_12, theta_23 appear only when sigma ~ M), the CKM's small angles need "
      "r_quark << 1: one set of vacua serves both only if the lepton copies are lighter than the quark copies by about "
      "r_q/r_l (supplied); at r >~ 1 the lepton sector is anarchic, with no structure beyond anarchy",
      ang[0][1] < 0.3 * ang[2][1] and ang[2][1] > 0.001 and ang[3][1] < 3 * anl, f"PMNS-like fraction {ang[0][1]:.4f} (r 0.01) -> {ang[2][1]:.4f} (r 1) -> {ang[3][1]:.4f} (r 10)")
Lam, vH = 2.435e18, 246.0
mnu = 0.05e-9
smax = mnu * Lam / vH; ratio = mnu / vH
print(f"   Dirac nu: order-one y needs M/sigma ~ m_nu/v = {ratio:.0e}; the dimension-five qc x L entry v sigma/Lambda caps sigma < {smax:.0e} GeV,")
print(f"   so the 'heavy' neutrino copies would sit near M ~ {ratio * smax:.0e} GeV: not heavy, the suppression is not available")
check("[E] Dirac neutrino masses are not explained: with sigma below the dimension-five cap the copies would sit near 100 eV",
      ratio * smax < 1e-3, f"M ~ {ratio * smax:.0e} GeV")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
