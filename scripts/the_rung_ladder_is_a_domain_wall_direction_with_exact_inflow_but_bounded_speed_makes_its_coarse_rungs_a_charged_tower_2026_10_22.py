AUDIT_INPUT_PATHS = ('docs/THE_RUNG_LADDER_IS_A_DOMAIN_WALL_DIRECTION_WITH_EXACT_INFLOW_BUT_BOUNDED_SPEED_MAKES_ITS_COARSE_RUNGS_A_CHARGED_TOWER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Rung (zoom) direction and an in-block layer coordinate as the domain-wall
direction for exact lattice chirality: free 1+1D tree-ladder toys, spectral
flow (anomaly inflow along rungs), rate dichotomy, a 3D Wilson-band
polarisation for the estimate, and a full-density layer-register toy.
Self-contained (numpy only). Seeded. Small dense matrices only (< 50 MB)."""
import time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = [0, 0]


def check(tag, kind, ok, msg, detail):
    NP[0 if ok else 1] += 1
    print("[%s] %s %s %s | %s" % ("PASS" if ok else "FAIL", tag, kind, msg, detail))


sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0, -1.0]).astype(complex)
KX = (sz - 1j * sx) / 2   # intra-rung hop: K e^{ik} + h.c. = cos k sz + sin k sx
TS = (sz - 1j * sy) / 2   # rung exchange: rank 1, T^2 = 0, T T^+ = (1+sx)/2


def tree(R, Ntop=1, m=-1.0, kap=1.0, rate="fine", Q=0.0, q=1.0, A=0.0,
         chi=1, cut=None, mu=0.0):
    """1+1D tree ladder. Rung j: Ntop*2^(R-j) cells at anchors n*2^j, 2 modes
    each. Rate: fine (every rung at the fine step) or zoom (rung j at 2^-j,
    exchange j<->j+1 at 2^-(j+1/2), so H_zoom = S H_fine S). Each parent couples
    to its two children with kap/sqrt2 (an isometry). Q: twist on every wrap;
    A: uniform fine-link field, hops carry exp(i q A dx) (Wilson lines);
    chi=-1 flips the exchange (opposite handedness); cut=J removes the
    exchange J-1<->J (Gauss projection of charged hops)."""
    idx, rung = {}, []
    for j in range(R + 1):
        for n in range(Ntop * 2 ** (R - j)):
            idx[(j, n)] = len(rung)
            rung.append(j)
    N = len(rung)
    H = np.zeros((2 * N, 2 * N), complex)
    Tm = TS if chi > 0 else TS.conj().T

    def add(a, b, M):
        H[2 * a:2 * a + 2, 2 * b:2 * b + 2] += M
        H[2 * b:2 * b + 2, 2 * a:2 * a + 2] += M.conj().T

    for j in range(R + 1):
        rj = 1.0 if rate == "fine" else 2.0 ** -j
        Nj = Ntop * 2 ** (R - j)
        for n in range(Nj):
            a = idx[(j, n)]
            H[2 * a:2 * a + 2, 2 * a:2 * a + 2] += rj * (m + mu) * sz
            n2 = (n + 1) % Nj
            ph = (np.exp(1j * Q) if n2 == 0 else 1.0) * np.exp(-1j * q * A * 2 ** j)
            add(a, idx[(j, n2)], rj * KX * ph)
        if j < R and not (cut is not None and j == cut - 1):
            rr = 1.0 if rate == "fine" else 2.0 ** -(j + 0.5)
            for n in range(Nj):
                p = n // 2
                d = n * 2 ** j - p * 2 ** (j + 1)
                add(idx[(j, n)], idx[(j + 1, p)],
                    rr * kap / np.sqrt(2) * Tm * np.exp(1j * q * A * d))
    return H, np.repeat(np.array(rung), 2)


def wts(V, rg, R):
    return np.array([np.sum(abs(V[rg == j]) ** 2, axis=0) for j in range(R + 1)])


def near_zero(H, rg, R, k=2):
    E, V = np.linalg.eigh(H)
    o = np.argsort(abs(E))[:k]
    return E[o], wts(V[:, o], rg, R)


# ---------------------------------------------------------------- A
print("== A. free rung ladder (1+1D tree; copy mass m = -1, exchange kap = 1)")
res = []
for R in (2, 3, 4):
    Hf, rg = tree(R, rate="fine", Q=0.3)
    Hz, _ = tree(R, rate="zoom", Q=0.3)
    S = np.repeat(2.0 ** (-rg[::2] / 2.0), 2)
    res.append(max(abs(Hz - S[:, None] * Hf * S[None, :]).max(),
                   abs(np.sum(np.linalg.eigvalsh(Hz) < 0) - np.sum(np.linalg.eigvalsh(Hf) < 0))))
    k0f = np.sum(abs(np.linalg.eigvalsh(tree(R, rate="fine")[0])) < 1e-9)
    k0z = np.sum(abs(np.linalg.eigvalsh(tree(R, rate="zoom")[0])) < 1e-9)
    res.append(abs(k0f - 2) + abs(k0z - 2))
check("A1", "THEOREM", max(res) < 1e-12,
      "zoom rate = congruence S H_fine S (S = 2^(-j/2)); Sylvester keeps the inertia, Q = 0 kernel 2 at both rates",
      "max residual / count mismatch %.0e (R = 2,3,4)" % max(res))

rows, ok = [], True
for R in (2, 3, 4, 5):
    rg = tree(R)[1]
    for rate in ("fine", "zoom"):
        dQ, Q = 1e-4, 0.2
        v, wsum = {}, {}
        for nm, js in (("L", [0, 1]), ("M", [R - 1, R])):
            e = []
            for QQ in (Q, Q + dQ):
                E, V = np.linalg.eigh(tree(R, rate=rate, Q=QQ)[0])
                W = wts(V, rg, R)
                cand = np.where(abs(E) < 0.5)[0]
                i = cand[np.argmax(W[js].sum(0)[cand])]
                e.append(E[i])
                wsum[nm] = W[js, i].sum()
            v[nm] = (e[1] - e[0]) / dQ * 2 ** R   # physical velocity, fine units
        exp_m = 2.0 ** R if rate == "fine" else 1.0
        ok &= abs(v["L"] + 1) < 0.02 and abs(v["M"] / exp_m - 1) < 0.1 and wsum["L"] > 0.9 and wsum["M"] > 0.8
        if R in (2, 5):
            rows.append("%s R=%d vL %.3f vM %.2f" % (rate[0], R, v["L"], v["M"]))
check("A2", "DIAGNOSTIC", ok,
      "one chiral pair: a mover of velocity -1 on rung 0 and the opposite mover on the top rung; mirror speed 2^R (fine) or 1 (zoom)",
      "; ".join(rows))

fit = {}
for rate in ("fine", "zoom"):
    sp = []
    for R in range(1, 8):
        E = np.linalg.eigvalsh(tree(R, rate=rate, mu=0.2)[0])
        sp.append(np.sort(abs(E))[1])
    sp = np.array(sp)
    fit[rate] = (sp[1:] / sp[:-1], sp)
rf, rz = fit["fine"][0], fit["zoom"][0]
check("A3", "DIAGNOSTIC", np.allclose(rf, 0.2, rtol=5e-3) and np.allclose(rz, 0.2 / np.sqrt(2), rtol=5e-3),
      "a copy-mass offset mu = 0.2 kap pairs the two ends into a residual mass falling by mu/kap per rung (fine) and mu/(sqrt2 kap) (zoom, in fine units); exact zero at the tuned wall m = -kap",
      "fine ratios %.4f..%.4f, R=7 %.1e; zoom %.4f..%.4f, R=7 %.1e" % (rf.min(), rf.max(), fit["fine"][1][-1], rz.min(), rz.max(), fit["zoom"][1][-1]))

ov = []
for R in (2, 3, 4, 5, 6):
    qph = 0.02
    H, rg = tree(R, rate="fine", Q=qph * 2 ** R)
    E, V = np.linalg.eigh(H)
    i = int(np.argmin(abs(E + qph)))
    ov.append(np.sum(abs(V[rg == R, i]) ** 2))
ov = np.array(ov)
check("A4", "DIAGNOSTIC", np.all(np.diff(np.log(ov + 1e-300)) < -2.0),
      "end-to-end overlap at fixed physical momentum 0.02: light-state weight on the top rung falls faster than e^-2 per rung",
      " ".join("%.1e" % x for x in ov) + " (R = 2..6)")

# ---------------------------------------------------------------- B
print("== B. anomaly inflow along the rungs (Wilson-line dressing, flux threading)")
R, Nt, qq, th = 3, 4, 2.0, 0.7
H, _ = tree(R, Ntop=Nt, A=th / (Nt * 2 ** R), q=qq)
Er = np.sort(np.linalg.eigvalsh(H))
best = 1.0
for sgn in (1, -1):
    Eb = np.sort(np.concatenate([np.linalg.eigvalsh(tree(R, Q=sgn * (qq * th + 2 * np.pi * n) / Nt)[0]) for n in range(Nt)]))
    best = min(best, abs(Er - Eb).max())
check("B1", "THEOREM", best < 1e-10,
      "gauge covariance: the Wilson-line-dressed ladder with flux theta is the twisted ladder, Bloch Q_n = (q theta + 2 pi n)/N_top; flux 2 pi sweeps the Bloch Q through q full turns",
      "spectrum residual %.0e (q = 2, N_top = 4)" % best)


def flow(Hfun, R, rg, low):
    """spectral flow of H(Q), Q in (-pi, pi]: zero crossings with velocity
    sign, binned by the rung (layer) of largest weight; low = near side."""
    Qs = np.linspace(-np.pi, np.pi, 241)[:-1] + 1e-3
    per = np.zeros(R + 1, int)
    for a in range(len(Qs)):
        Ea, Va = np.linalg.eigh(Hfun(Qs[a]))
        Eb, Vb = np.linalg.eigh(Hfun(Qs[a] + (Qs[1] - Qs[0])))
        for i in np.where(abs(Ea) < 0.2)[0]:
            j = int(np.argmax(abs(Vb.conj().T @ Va[:, i])))
            if np.sign(Ea[i]) != np.sign(Eb[j]):
                w = [np.sum(abs(Va[rg == r, i]) ** 2) for r in range(R + 1)]
                per[int(np.argmax(w))] += int(np.sign(Eb[j] - Ea[i]))
    lo = int(sum(per[r] for r in low))
    return {"low": lo, "high": int(per.sum() - lo), "per": per}


rg3 = tree(3)[1]
fl = {}
for rate in ("fine", "zoom"):
    for chi in (1, -1):
        fl[(rate, chi)] = flow(lambda Q: tree(3, rate=rate, Q=Q, chi=chi)[0], 3, rg3, [0, 1])
okb = all(fl[(r, c)]["low"] == -c and fl[(r, c)]["high"] == c for r in ("fine", "zoom") for c in (1, -1))
check("B2", "THEOREM", okb,
      "index: one crossing per Bloch turn on the light end and the opposite one on the top rung, so flux 2 pi moves q units of species number and q^2 of gauge charge from the top rung to rung 0 (Callan-Harvey inflow through the gapped middle rungs)",
      "flows (low, top): " + ", ".join("%s chi%+d (%+d,%+d)" % (r[0], c, fl[(r, c)]["low"], fl[(r, c)]["high"]) for r in ("fine", "zoom") for c in (1, -1)))

ch = {3: 1, 4: 1, 5: -1, 0: -1}
spec = {qv: (-c * qv, -c * qv * qv) for qv, c in ch.items()}
gsum = sum(v[1] for v in spec.values())
# 3+1D: one SM family as left-handed Weyl (Y normalised Q = T3 + Y), with nu^c
fam = [(3, 2, 1 / 6), (3, 1, -2 / 3), (3, 1, 1 / 3), (1, 2, -1 / 2), (1, 1, 1), (1, 1, 0)]
Y3 = sum(c * w * y ** 3 for c, w, y in fam)
Y1 = sum(c * w * y for c, w, y in fam)
S2Y = sum(c * y for c, w, y in fam if w == 2)
C2Y = sum(w * y for c, w, y in fam if c == 3)
check("B3", "THEOREM", gsum == 0 and abs(Y3) < 1e-12 and abs(Y1) < 1e-12 and abs(S2Y) < 1e-12 and abs(C2Y) < 1e-12,
      "3-4-5-0 (right 3,4; left 5,0): gauge-charge inflow sum chi q^2 = 0 while species numbers still flow; the 16 has zero inflow coefficients (Y^3, grav-Y, SU2^2 Y, SU3^2 Y): its light end alone is gauge-consistent",
      "species flow per 2 pi %s, gauge %d; 16: %.0e %.0e %.0e %.0e" % ([spec[k][0] for k in (3, 4, 5, 0)], gsum, Y3, Y1, S2Y, C2Y))

rg5 = tree(5)[1]
fc = flow(lambda Q: tree(5, Q=Q, cut=3)[0], 5, rg5, [0, 1, 2])
Hp0, _ = tree(3, Ntop=2, A=0.0)
# partial gauging: field only on rungs 0..1, exchange 1<->2 undressed
def partial(th):
    Hf, rg = tree(3, Ntop=2, A=th / 16.0)
    H0, _ = tree(3, Ntop=2, A=0.0)
    msk = np.isin(rg, [0, 1])
    Hm = H0.copy()
    Hm[np.ix_(msk, msk)] = Hf[np.ix_(msk, msk)]
    return Hm
dpart = abs(np.sort(np.linalg.eigvalsh(partial(2 * np.pi))) - np.sort(np.linalg.eigvalsh(partial(0.0)))).max()
pc = fc["per"]
check("B4", "THEOREM", list(pc) == [-1, 0, 1, -1, 0, 1] and dpart > 1e-2,
      "gauging only the light end: undressed hops across the cut break gauge equivalence (H(2 pi) not ~ H(0)); the Gauss projection removes them, and the gauged piece then carries its own charged mirror on rung J-1",
      "cut at J = 3 (R = 5): crossings by rung %s; partial-gauge spectral mismatch %.2f" % ([int(x) for x in pc], dpart))

# ---------------------------------------------------------------- C
print("== C. rates: bounded speed forces a tower of charged rung bands")
R = 6
gaps = {}
for rate in ("fine", "zoom"):
    g = np.full(R + 1, np.inf)
    for Q in np.linspace(0, np.pi, 7):
        H, rg = tree(R, rate=rate, Q=Q)
        E, V = np.linalg.eigh(H)
        W = wts(V, rg, R)
        dom = np.argmax(W, axis=0)
        for j in range(1, R):
            s = dom == j
            if np.any(s):
                g[j] = min(g[j], abs(E[s]).min())
    gaps[rate] = g[1:R]
zf, zz = gaps["fine"], gaps["zoom"] * 2.0 ** np.arange(1, R)
check("C1", "DIAGNOSTIC", zf.std() / zf.mean() < 0.15 and zz.std() / zz.mean() < 0.15,
      "middle-rung band gaps: fine rate the same on every rung; zoom rate c 2^-j (self-similar), i.e. one vector-like copy of the light content per factor 2 in energy",
      "fine %s; zoom x 2^j %s" % (np.round(zf, 3), np.round(zz, 3)))

viol, nidx = 0.0, 0
for m in np.linspace(-3.0, 1.0, 17):
    for rate in ("fine", "zoom"):
        H, rg = tree(4, m=m, rate=rate, Q=0.4)
        On = np.zeros_like(H)
        for c in range(H.shape[0] // 2):
            On[2 * c:2 * c + 2, 2 * c:2 * c + 2] = H[2 * c:2 * c + 2, 2 * c:2 * c + 2]
        E, V = np.linalg.eigh(H)
        W = wts(V, rg, 4)
        idx = np.sum((abs(E) < 0.1 * (1 if rate == "fine" else 2 ** -4) + 0.02) & (W[0] + W[1] > 0.5))
        if idx > 0:
            nidx += 1
            hop = np.linalg.norm(H - On, 2)
            viol = max(viol, np.min(abs(np.linalg.eigvalsh(On))) / hop)
check("C2", "THEOREM", nidx > 0 and viol <= 1.0 + 1e-9,
      "Weyl bound: if the on-site part's smallest |level| exceeds ||H_hop|| the path to the on-site Hamiltonian stays gapped (index 0); so a wall needs on-site gap <= ||hop|| and bulk gap <= 2||hop||; Lieb-Robinson with range 2^j caps rung-j hops at ~v 2^-j: gap_j <= 2 v 2^-j at bounded speed",
      "%d indexed points of 34, max (min on-site |level|)/||hop|| = %.2f" % (nidx, viol))

# ---------------------------------------------------------------- D
print("== D. estimates against measurement (a = sqrt(8 pi) l_P, E_a/(2v) = 2.1e18 GeV)")
I2 = np.eye(2)
alph = [np.kron(sx, s) for s in (sx, sy, sz)]
beta = np.kron(sz, I2)


def hW(k, m0):
    Mk = m0 + np.sum(1 - np.cos(k), axis=-1)
    H = sum(np.sin(k[..., i])[..., None, None] * alph[i] for i in range(3)) + Mk[..., None, None] * beta
    return H


def chi(qv, m0, N=20):
    g = 2 * np.pi * np.arange(N) / N
    k = np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)
    E1, U1 = np.linalg.eigh(hW(k, m0))
    E2, U2 = np.linalg.eigh(hW(k + np.array([qv, 0, 0]), m0))
    O = np.abs(np.einsum("kai,kaj->kij", U2.conj(), U1)) ** 2  # <n,k+q|m,k>
    occ1, occ2 = E1 < 0, E2 < 0
    den = E2[:, :, None] - E1[:, None, :]
    f = (occ1[:, None, :] & ~occ2[:, :, None])
    t1 = np.sum(np.where(f, O / np.where(f, den, 1.0), 0.0))
    f2 = (~occ1[:, None, :] & occ2[:, :, None])
    t2 = np.sum(np.where(f2, O / np.where(f2, -den, 1.0), 0.0))
    return (t1 + t2) / len(k)


c1 = {}
for m0 in (0.2, 0.354, 0.6):
    a = chi(0.08, m0)
    c1[m0] = a / 0.08 ** 2
cont = {m0: np.log((np.pi / m0) ** 2) / (12 * np.pi ** 2) for m0 in c1}
okc = all(0.3 < c1[m0] / cont[m0] < 3 for m0 in c1)
check("D1", "DIAGNOSTIC", okc,
      "one Wilson-Dirac band (gap 2 m0, unit charge): static polarisation chi(q)/q^2 = Delta(1/e^2) per band, of the continuum size ln(Lambda^2/m^2)/(12 pi^2)",
      ", ".join("m0 %.3g: %.4f (cont %.4f)" % (m0, c1[m0], cont[m0]) for m0 in c1))

c = c1[0.354]
nr = np.log2(91.1876 / 0.000511)
SQ = 3 * 8 / 3
dinv = nr * 4 * np.pi * c * SQ
thr = 3 * 0.014 / (nr * 4 * np.pi * SQ)
Rh = np.log2(1.37e26 / (np.sqrt(8 * np.pi) * 1.616e-35))
mres = 2.1e18 * 0.5 ** Rh
check("D2", "ESTIMATE", dinv > 100 * 0.014,
      "zoom rate, gauge-covariant: %.1f rungs between m_e and M_Z, each a vector-like 3-family copy (sum Q^2 = 8) adding 4 pi c1 sum Q^2 to 1/alpha: extra running %.1f vs the 0.014 known from Delta alpha_had: excluded unless c1 < %.1e" % (nr, dinv, thr),
      "c1 %.4f; R_H = log2(c/H0 a) = %.1f" % (c, Rh))
print("   D3 ESTIMATE fine rate: no tower (gap ~0.4 per rung at Planck), mirror energy 2^R x momentum: below 1 TeV only for |Q| < 1e-15 x 2^-R/a, ~0 states per horizon; residual mass mu(mu/kap)^R_H <= %.0e GeV at mu/kap = 1/2; price: rung j hops 2^j sites per tick (speed 2^j, the swindle of the octree-ladder note), against nearest-neighbour admissibility" % mres)
print("   D4 ESTIMATE any cut (Gauss projection, B4) or finite top at E_R >~ M_Z: a massless charged mirror; e^c' alone adds 35.5 MeV to Gamma_Z per family vs sigma 2.3 MeV (ladder-wall E3)")

# ---------------------------------------------------------------- E
print("== E. owner-widened: full-density layer coordinate inside a role block")


def strip(Ls, k, m=-1.0, kap=1.0, mu=0.0, q=1.0, chi=1):
    """layer register: each 1D matter cell holds 2 Ls one-mode sites (layer s,
    component); layer hop T inside the cell, cell-to-cell hop K at the same
    layer (range = cell size, uniform rate). Bloch momentum k."""
    H = np.zeros((2 * Ls, 2 * Ls), complex)
    Tm = TS if chi > 0 else TS.conj().T
    for s in range(Ls):
        b = slice(2 * s, 2 * s + 2)
        H[b, b] += (m + mu) * sz + KX * np.exp(1j * q * k) + KX.conj().T * np.exp(-1j * q * k)
        if s < Ls - 1:
            b2 = slice(2 * s + 2, 2 * s + 4)
            H[b, b2] += kap * Tm
            H[b2, b] += kap * Tm.conj().T
    return H


Ls = 8
lg = np.repeat(np.arange(Ls), 2)
gl = np.full(Ls, np.inf)
for k in np.linspace(0, np.pi, 25):
    E, V = np.linalg.eigh(strip(Ls, k))
    dom = np.argmax(np.array([np.sum(abs(V[lg == s]) ** 2, axis=0) for s in range(Ls)]), axis=0)
    for s in range(1, Ls - 1):
        if np.any(dom == s):
            gl[s] = min(gl[s], abs(E[dom == s]).min())
spl = [np.sort(abs(np.linalg.eigvalsh(strip(L, 0.0, mu=0.2))))[1] for L in (4, 6, 8, 10)]
rat = np.array(spl[1:]) / np.array(spl[:-1])
fs = flow(lambda Q: strip(Ls, Q), Ls - 1, lg, list(range(Ls // 2)))
check("E1", "DIAGNOSTIC", gl[1:Ls - 1].std() / gl[1:Ls - 1].mean() < 0.05 and np.allclose(rat, 0.04, rtol=1e-2) and fs["low"] == -1 and fs["high"] == 1,
      "layer register = domain-wall slab on Z^3 cells: one chiral pair at the two end layers, layer gap the same on every layer (no tower), residual mass (mu/kap)^Ls, but the far-end mirror carries the full charge (flow on the far layers)",
      "layer gaps %s; split ratio per 2 layers %s; flow (near, far) (%+d,%+d)" % (np.round(gl[1:Ls - 1], 3), np.round(rat, 4), fs["low"], fs["high"]))
print("   E2 THEOREM (B1 + B2 on the slab) any gauge-covariant reading of the far layers keeps their crossing under flux 2 pi: the mirror stays coupled to the holonomy, with charge q, so a vector-like gauge theory with exact chiral symmetry results; chiral gauge couplings need one more clause (far-layer symmetric gapping, or the far layers reading a smoothed field that keeps topology)")
print("   E3 ESTIMATE cost: 16 Weyl x 4 components x Ls one-mode sites per family per matter cell (64 Ls); three families at Ls = 8 use 1536 sites of a 12^3 role block; cell-to-cell hops span the block (uniform slowdown b, no tower); residual mass (mu/kap)^Ls tunable to zero at the free tuned wall")
print("   F THEOREM (counting) the tick cannot be the wall direction: a wall bounds a (d+1)-dim bulk whose boundary is the whole 3+1 world, tick included; the B4 transfer matrix is that world's own time step (euclidean-b4 B4: it projects onto the vacuum and cannot carry CL-2); the overlap operator sign(H_W) is the infinite-layer limit of a FIFTH-direction transfer matrix, i.e. of E's layer coordinate")

print("supplied: 1+1D tree, rates, m = -kap, mu, Wilson lines, cut, Ntop, Q grid, Wilson band m0 and grid, layer count, unit map, measured inputs | %.1f s" % (time.time() - T0))
print("cited: PR #9908, hybrid-wall, ladder-wall, euclidean-b4, toy-qmc, Callan-Harvey, Kaplan, Shamir, Neuberger, Grabowska-Kaplan, PDG")
print("TOTAL: PASS=%d FAIL=%d" % tuple(NP))
