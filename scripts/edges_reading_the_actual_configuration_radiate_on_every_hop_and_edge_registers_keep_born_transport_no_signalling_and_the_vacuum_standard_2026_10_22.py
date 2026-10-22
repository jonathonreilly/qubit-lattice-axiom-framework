AUDIT_INPUT_PATHS = ('docs/EDGES_READING_THE_ACTUAL_CONFIGURATION_RADIATE_ON_EVERY_HOP_AND_EDGE_REGISTERS_KEEP_BORN_TRANSPORT_NO_SIGNALLING_AND_THE_VACUUM_STANDARD_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""edge-source: which rule replaces the local edge source?
(A) smooth source: CL-3's matter phase read from conditional odds;
(B) quantised edges: edges are registers carrying odds like the links.
Self-contained (numpy/scipy). Tags: [T] exact/theorem-level, [D] finite diagnostic, [E] estimate vs measurement.
"""
import time, itertools
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

AUDIT_TIMEOUT_SEC = 120
t0 = time.time()
NP = NF = 0
rng = np.random.default_rng(7)


def check(tag, ok, msg, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg}" + (f" | {detail}" if detail else ""))


G_, hb, c_, amu, kB = 6.674e-11, 1.0546e-34, 2.998e8, 1.6605e-27, 1.381e-23
lP = 1.616e-35
aL = np.sqrt(8 * np.pi) * lP          # G = a^2/(8 pi) per cell
tau = aL / c_
mN = 1.6726e-27
P_bound = 1e-3 * mN * c_ ** 2 / 4.35e17   # 1e-3 m_p c^2 per Hubble time
P_local = 3 * (1 / 6) * 4 * np.pi * G_ * (mN / 3) ** 2 / aL * np.sqrt(3 * kB * 300 / mN) / aL

# ===================================================================== A
print("== A. smooth source: conditional odds")
# A1 site-split conditional odds = actual configuration
L, Npart = 8, 3
confs = [c for c in itertools.product([0, 1], repeat=L) if sum(c) == Npart]
amp = {c: rng.normal() + 1j * rng.normal() for c in confs}
maxsup = 0
for c in confs:
    for j in range(L):
        sup = 0
        for b in (0, 1):
            cc = list(c); cc[j] = b; cc = tuple(cc)
            sup += abs(amp.get(cc, 0)) > 0
        maxsup = max(maxsup, sup)
# pairing (parity-even, number not conserved): support <= 2 states of ONE site
confs2 = [c for c in itertools.product([0, 1], repeat=L) if sum(c) % 2 == 0]
amp2 = {c: rng.normal() + 1j * rng.normal() for c in confs2}
maxsup2 = max(sum(abs(amp2.get(tuple(c[:j]) + (b,) + tuple(c[j + 1:]), 0)) > 0 for b in (0, 1))
              for c in confs2 for j in range(L))
check("T", maxsup == 1 and maxsup2 == 1,
      "A1 conditional odds of a site given the actual occupations of all other sites sit on ONE "
      "configuration (number or parity fixes the site): the site-split conditional source IS the local "
      "reading; smoothing needs a split coarser than a cell, which no clause of CL-1..CL-3 supplies",
      f"max support: number-conserving {maxsup}, parity-even {maxsup2} (L=8)")


def hop_energy(Nb, rho):
    k = 2 * np.pi * np.fft.fftfreq(Nb)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    w2 = 4 * (np.sin(kx / 2) ** 2 + np.sin(ky / 2) ** 2 + np.sin(kz / 2) ** 2)
    dr = np.fft.fftn(rho - np.roll(rho, 1, axis=0))
    w2[0, 0, 0] = 1.0
    E = 0.5 * np.abs(dr) ** 2 / w2
    E[0, 0, 0] = 0
    return E.sum() / Nb ** 3


# A2 point hop exactly 1/6 (units q^2 with -lap phi = rho; gravity: x 4 pi G m^2 / a)
res = []
for Nb in (16, 32):
    r = np.zeros((Nb,) * 3); r[0, 0, 0] = 1
    res.append(hop_energy(Nb, r) - (1 / 6) * (1 - 1 / Nb ** 3))
check("T", max(abs(x) for x in res) < 1e-12,
      "A2 a sudden one-cell hop of a point source releases exactly (1/6)(1-1/N^3) q^2/a: cubic symmetry "
      "splits sum_i 4 sin^2(k_i/2)/w^2 = 1 equally (the self-gravity 0.17 is this 1/6)",
      f"max dev {max(abs(x) for x in res):.1e}")
# A3 sudden hop of a width-s source: power law a^2/(48 pi^1.5 s^3), not exponential
Nb = 64
x = np.arange(Nb) - Nb // 2
X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
out = []
for s in (2.0, 3.0, 4.0):
    r = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (2 * s * s)); r /= r.sum()
    out.append((s, hop_energy(Nb, r), 1 / (48 * np.pi ** 1.5 * s ** 3)))
dev = max(abs(e / p - 1) for _, e, p in out)
check("T", dev < 0.05,
      "A3 if the smooth source still jumps by one cell (it does whenever the conditioning set hops), "
      "each jump releases a^2 q^2/(48 pi^1.5 s^3): suppression (a/s)^3 x 0.022, a POWER law",
      "E(s)/cont: " + ", ".join(f"s={s:.0f} {e:.2e}/{p:.2e}" for s, e, p in out))
del X, Y, Z
# A4 smoothly translated profile on a discrete-time lattice field: aliasing (Cherenkov via umklapp) only
c_l, v = 0.9, 0.5
kg = np.linspace(-np.pi, np.pi, 200001)[1:]
wk = 2 * np.arcsin(c_l * np.abs(np.sin(kg / 2)))
roots = []
for m in range(-3, 4):
    for n in range(-3, 4):
        for sg in (1, -1):
            f = sg * wk - (kg + 2 * np.pi * m) * v - 2 * np.pi * n
            idx = np.where(np.sign(f[:-1]) * np.sign(f[1:]) < 0)[0]
            for i in idx:
                kk = kg[i]; kap = kk + 2 * np.pi * m
                dfd = abs((f[i + 1] - f[i]) / (kg[i + 1] - kg[i]))
                roots.append((m, kap, dfd, wk[i]))
m0 = [r for r in roots if r[0] == 0]
kapmin = min(abs(r[1]) for r in roots)


def Wrad(s):
    return sum(np.exp(-(kap * s) ** 2) / (dfd * w) for _, kap, dfd, w in roots)


ss = np.array([1.0, 1.5, 2.0, 2.5])
lw = np.log([Wrad(s) for s in ss])
slope = np.polyfit(ss ** 2, lw, 1)[0]
check("D", len(m0) == 0 and abs(-slope - kapmin ** 2) / kapmin ** 2 < 0.05,
      "A4 a profile translated smoothly at v < c radiates only through lattice aliasing: no m=0 "
      "resonance, power ~ exp(-kappa*^2 s^2), EXPONENTIAL in (s/a)^2",
      f"c=0.9, v=0.5: m=0 roots {len(m0)}, kappa* {kapmin:.3f} (> pi), fitted slope {-slope:.2f} vs "
      f"kappa*^2 {kapmin**2:.2f}; W(2.5)/W(1) {np.exp(lw[-1]-lw[0]):.0e}")
# A5 sizes for a thermal nucleon
s_fm = 1e-15
P_jump = P_local * 6 / (48 * np.pi ** 1.5) * (aL / s_fm) ** 3        # conditioning jumps of a fm packet
ls_min = aL * np.sqrt(P_local / P_bound)                              # block-split crossing jumps ~ (a/l_s)^2
check("E", P_jump < 1e-15 * P_bound,
      "A5 thermal (300 K) nucleon: local reading P_local; smooth fm-wide conditional source jumping a cell "
      "per partner hop: (a/s)^3 suppression; block split of size l_s: crossings give (a/l_s)^2",
      f"P_local {P_local:.0e} W, P_jump {P_jump:.0e} W, budget {P_bound:.0e} W; block split needs "
      f"l_s > {ls_min:.0e} m; Page-Geilker needs l_s < ~1e-2 m")
# A6 signalling: B's conditional source distribution depends on A's remote setting
d = 1.0
psi = np.array([[1, 0], [0, 1]]) / np.sqrt(2)      # rows A in {0,1}, cols B in {L,R}; |0L>+|1R>
xB = np.array([-d / 2, d / 2])
stats = []
for U in (np.eye(2), np.array([[1, 1], [1, -1]]) / np.sqrt(2)):
    ph = U @ psi
    pa = (np.abs(ph) ** 2).sum(1)
    dip = [(np.abs(ph[a]) ** 2 @ xB) / pa[a] for a in range(2)]
    mean = sum(pa[a] * dip[a] for a in range(2)); var = sum(pa[a] * dip[a] ** 2 for a in range(2)) - mean ** 2
    margB = (np.abs(ph) ** 2).sum(0)
    stats.append((mean, var, margB))
Dg = G_ * 1e-14 * 2.5e-4 / 1e-3 ** 3
check("T", abs(stats[0][0] - stats[1][0]) < 1e-15 and abs(stats[0][1] - stats[1][1]) > 0.2
      and np.allclose(stats[0][2], stats[1][2]),
      "A6 under (A) the variance of B's sourced field depends on A's remote setting at fixed Born mean: "
      "a local readable distribution changes, i.e. signalling in principle; the local reading and (B) "
      "keep B's marginals setting-independent",
      f"var(dipole) Z {stats[0][1]:.2f} vs X {stats[1][1]:.0e} d^2; BMV-scale (1e-14 kg, 250 um, "
      f"at 1 mm) field split {Dg:.0e} m/s^2 per run")
# A7 lone particle: Schrodinger-Newton self-term sizes
m_sn1um = (hb ** 2 / (G_ * 1e-6)) ** (1 / 3) / amu
m_mol, T_mol, dg = 2.5e4 * amu, 1e-2, 2.66e-7
ph_mol = G_ * m_mol ** 2 / dg * T_mol / hb
m_rb, T_rb, d_rb, keff = 87 * amu, 2.08, 0.54, 90 * 2 * 2 * np.pi / 780e-9
ph_rb = keff * G_ * m_rb / d_rb ** 2 * T_rb ** 2 / 2
check("E", ph_mol < 1e-12 and ph_rb < 1e-20 and m_sn1um > 1e4 * 2.5e4,
      "A7 a lone elementary particle sources from its full odds (Schrodinger-Newton self-term); every "
      "interferometer so far is far inside the null region",
      f"Fein-2019 molecule phase {ph_mol:.0e} rad; Rb 54 cm arm attraction phase {ph_rb:.0e} rad; "
      f"SN self-collapse at 1 um needs {m_sn1um:.0e} amu")

# ===================================================================== B
print("== B. quantised edges: edge registers")
# B1 rishon edge register: 2S flavours x 2 ends of fermion modes (Jordan-Wigner)
S2 = 4
nm = 2 * S2
def cop(j):
    ops = []
    Z = np.diag([1., -1.]); a = np.array([[0., 1.], [0., 0.]]); I = np.eye(2)
    M = np.array([[1.]])
    for i in range(nm):
        M = np.kron(M, Z if i < j else (a if i == j else I))
    return M
cs = [cop(j) for j in range(nm)]
cL, cR = cs[:S2], cs[S2:]
Sp = sum(cL[a].T @ cR[a] for a in range(S2))
Sz = 0.5 * sum(cL[a].T @ cL[a] - cR[a].T @ cR[a] for a in range(S2))
nL = sum(cL[a].T @ cL[a] for a in range(S2))
anti = max(np.abs(cs[i] @ cs[j].T + cs[j].T @ cs[i] - (i == j) * np.eye(2 ** nm)).max()
           for i in range(nm) for j in range(nm))
comm = np.abs(Sp @ Sp.T - Sp.T @ Sp - 2 * Sz).max()
C2 = Sp @ Sp.T + Sz @ Sz - Sz
fl = [cL[a].T @ cL[a] + cR[a].T @ cR[a] for a in range(S2)]
P1 = np.eye(2 ** nm)
for f in fl:
    P1 = P1 @ f @ (2 * np.eye(2 ** nm) - f)          # projector: each flavour holds exactly one fermion
P1 = np.round(P1, 12)
evC = np.linalg.eigvalsh(P1 @ C2 @ P1)
mult_top = int(np.sum(np.abs(evC - S2 / 2 * (S2 / 2 + 1)) < 1e-9))
lengths = sorted(set(np.round(1 + np.diag(nL) / S2, 6)))
check("T", anti < 1e-12 and comm < 1e-12 and mult_top == S2 + 1 and lengths[0] == 1 and lengths[-1] == 2,
      "B1 an edge register is buildable from fermion-mode sites like CL-1's rishons: 2S modes per end, "
      "S+ = sum c_L^dag c_R closes su(2); length l = l_rung(1 + n_L/2S) spans exactly CL-1's split window "
      "[l_rung, 2 l_rung], and a hop moves one length quantum",
      f"2S={S2}: CAR dev {anti:.0e}, [S+,S-]-2Sz {comm:.0e}, spin-{S2//2} multiplet dim {mult_top}, "
      f"lengths {lengths[0]:.2f}..{lengths[-1]:.2f}")
del cs, cL, cR, Sp, Sz, nL, C2, P1, fl
# B2 triangle inequalities inside the window
g = np.linspace(1, 2, 41)[:-1]
same = all(a + b > cc for a in g for b in g for cc in g)
gd = np.linspace(np.sqrt(2), 2 * np.sqrt(2), 41)[:-1]
viol = np.mean([a + b <= cc for a in g for b in g for cc in gd])
check("T", same and viol > 0,
      "B2 three same-type edges in [L, 2L) always form a nondegenerate triangle (a+b >= 2L > c); "
      "mixed axis/face-diagonal triangles can fail, so the register needs the triangle constraint "
      "(open, as for quantum Regge measures)",
      f"axis-axis-diagonal violating fraction {viol:.3f}")


# B3 vacuum standard with quantum edges: edge q (strain) + matter oscillators w(q) = w0/(1+q)
def toy(M, K, w0, nmodes, subtract, nmat=12, nq=81, qmax=0.5, nstates=4):
    q = np.linspace(-qmax, qmax, nq); dq = q[1] - q[0]
    Tq = sp.diags([np.full(nq - 1, -1.), np.full(nq, 2.), np.full(nq - 1, -1.)], [-1, 0, 1]) / (2 * M * dq ** 2)
    Vq = sp.diags(0.5 * K * q ** 2)
    n = np.arange(nmat)
    ad = np.diag(np.sqrt(n[1:]), -1)
    xo = (ad + ad.T) / np.sqrt(2 * w0); po = 1j * np.sqrt(w0 / 2) * (ad - ad.T)
    P2 = np.real(po @ po.T.conj()); X2 = xo @ xo
    wq = w0 / (1 + q)
    Hq = sp.kron(Tq + Vq, sp.identity(nmat ** nmodes))
    for i in range(nmodes):
        pre, post = sp.identity(nmat ** i), sp.identity(nmat ** (nmodes - 1 - i))
        Hq = Hq + sp.kron(sp.identity(nq), sp.kron(pre, sp.kron(sp.csr_matrix(P2 / 2), post)))
        Hq = Hq + sp.kron(sp.diags(wq ** 2 / 2), sp.kron(pre, sp.kron(sp.csr_matrix(X2), post)))
        if subtract:
            Hq = Hq - sp.kron(sp.diags(wq / 2), sp.identity(nmat ** nmodes))
    ev, vec = spl.eigsh(Hq.tocsr(), k=nstates, which="SA")
    o = np.argsort(ev); ev, vec = ev[o], vec[:, o]
    qop = np.kron(q, np.ones(nmat ** nmodes))
    Fq = [K * np.sum(np.abs(vec[:, i]) ** 2 * qop) for i in range(nstates)]
    return ev, Fq, vec


w0 = 2.0
r = {}
for M in (50., 200.):
    _, Fr, _ = toy(M, M, w0, 1, False)
    _, Fs, _ = toy(M, M, w0, 1, True)
    r[M] = (Fr[0], Fs[0])
R50, R200 = r[50.][1] / r[50.][0], r[200.][1] / r[200.][0]
pred50 = (1 / (8 * 50.)) / (w0 / 2 + 1 / (8 * 50.))
check("D", abs(R50 / pred50 - 1) < 0.15 and abs(R50 / R200 - 4) < 0.6,
      "B3 per-configuration vacuum standard with a quantum edge: the matter zero-point force w0/2 cancels "
      "exactly; the residual is the edge-motion (Born-Oppenheimer) term 1/(8M), i.e. a ratio "
      "R = 1/(4 M w0) = sigma_q^2 Omega_e/(2 w0)",
      f"force raw {r[50.][0]:.4f}, standard {r[50.][1]:.2e} (R={R50:.2e}, BO {pred50:.2e}); M x4: R/4 "
      f"-> {R200:.2e}")
# global mode: N modes on one scale mode of mass N M: residual total fixed, ratio ~ 1/N
_, Fr2, _ = toy(100., 100., w0, 2, False, nmat=9, nq=61)
_, Fs2, _ = toy(100., 100., w0, 2, True, nmat=9, nq=61)
R2 = Fs2[0] / Fr2[0]
check("D", abs(R2 / (R50 / 2) - 1) < 0.25,
      "B3b the collective (expansion) mode: N matter modes on a scale mode of mass N M leave the same total "
      "residual, so the residual vacuum density falls as 1/N_cells; for a Hubble volume ~1e-183 Planck "
      "against the measured ~1e-123: the vacuum standard survives quantisation for the expansion",
      f"N=2, M_glob=100: R {R2:.2e} vs R(N=1,M=50)/2 {R50/2:.2e}")
# one quantum departure sources hbar w (null dust as C4)
ev, Fs, vec = toy(50., 50., w0, 1, True, nstates=6)
nmat = 12; nq = 81
nexp = []
for i in range(6):
    v4 = np.abs(vec[:, i].reshape(nq, nmat)) ** 2
    nexp.append(v4.sum(0) @ np.arange(nmat))
i1 = int(np.argmin([abs(x - 1) if x > 0.5 else 9 for x in nexp]))
check("D", abs((Fs[i1] - Fs[0]) / w0 - 1) < 0.05,
      "B3c one matter quantum above the vacuum pushes the quantum edge with force w0 (sources hbar w), "
      "the departure the vacuum standard keeps",
      f"(F1-F0)/w0 {(Fs[i1]-Fs[0])/w0:.4f}, <n> {nexp[i1]:.3f}")
# B4 Page-Geilker, no signalling, Born, BMV
p = 0.5
th = {0: np.array([1., 0.]), 1: np.array([0., 1.])}   # test-mass deflection states
fL, fR = np.array([1., 0.]), np.array([0.3, np.sqrt(1 - 0.09)])
st = np.sqrt(p) * np.kron(np.kron([1, 0], fL), th[0]) + np.sqrt(1 - p) * np.kron(np.kron([0, 1], fR), th[1])
P = (np.abs(st) ** 2).reshape(2, 2, 2)
wrong = P[0, :, 1].sum() + P[1, :, 0].sum()
phi = lambda dd: G_ * 1e-14 ** 2 * 2.5 / (hb * dd)
d0, dx = 2e-4, 2.5e-4
dphi = phi(d0) + phi(d0 + 2 * dx) - 2 * phi(d0 + dx)
Cq = abs(np.sin(dphi / 2))
check("T", wrong == 0 and Cq > 0.1,
      "B4 quantum edges: the joint update never reads the actual configuration, so CL-2 has one target "
      "(Born exact, no signalling, no hop ever reaches the edges); the actual pointer, edge and test-mass "
      "values agree (Page-Geilker passes); two masses entangle through the edges",
      f"P(deflection disagrees with pointer) {wrong:.0e}; BMV (1e-14 kg, d 200 um, dx 250 um, 2.5 s) "
      f"phase {phi(d0):.2f} rad, concurrence {Cq:.3f} (A, definite: 0)")
# B5 graviton vacuum: cube-averaged edge fluctuation ~ 1/L
Nb = 48
k = 2 * np.pi * np.fft.fftfreq(Nb)
kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
w = 2 * np.sqrt(np.sin(kx / 2) ** 2 + np.sin(ky / 2) ** 2 + np.sin(kz / 2) ** 2); w[0, 0, 0] = 1
vl = []
for Lc in (2, 4, 8):
    Wk = np.ones_like(kx)
    for kk in (kx, ky, kz):
        sn = np.sin(kk / 2); sn[np.abs(sn) < 1e-14] = 1
        Wk = Wk * np.where(np.abs(np.sin(kk / 2)) < 1e-14, 1.0, np.sin(Lc * kk / 2) / (Lc * sn))
    V = (Wk ** 2 / (2 * w)); V[0, 0, 0] = 0
    vl.append(V.sum() / Nb ** 3 * Lc ** 2)
del kx, ky, kz, w, Wk, V
check("D", max(vl) / min(vl) < 1.35,
      "B5 the edge registers' vacuum, averaged over L cells, fluctuates as Var ~ 1/L^2 (delta l/l ~ l_P/L): "
      "LIGO arm 4 km ~4e-39 against 1e-23 strain; matter-wave and clock tests likewise far below",
      "Var*L^2 at L=2,4,8: " + ", ".join(f"{x:.3f}" for x in vl))
# B6 classical-limit corrections to register results that used definite edges
corr = {"GP-B (7e6 m)": (lP / 7e6) ** 2, "light bending (7e8 m)": (lP / 7e8) ** 2,
        "Hulse-Taylor (1e9 m)": (lP / 1e9) ** 2, "Friedmann (H0 tP)^2": (2.2e-18 * 5.39e-44) ** 2}
check("E", max(corr.values()) < 1e-80,
      "B6 stationarity becomes the large-occupation limit: corrections (l_P/L)^2 to GP-B, bending, binary "
      "timing and the Friedmann law; crush/split-epoch results (Planck curvature) are not controlled",
      ", ".join(f"{k} {v:.0e}" for k, v in corr.items()))
print(f"   graviton at the cell: hbar/tau = {hb/tau:.0e} J vs E_hop {4*np.pi*G_*(mN/3)**2/(6*aL):.0e} J")
print("theorems: A1-A3, A6, B1-B2, B4; diagnostics: A4, B3, B5; estimates: A5, A7, B6")
print(f"elapsed_seconds {time.time()-t0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
