AUDIT_INPUT_PATHS = ('docs/THE_OVERLAP_CHIRAL_DETERMINANT_IN_SU3_X_SU2_X_U1_BACKGROUNDS_CANCELS_THE_ONE_GENERATION_GAUGE_ANOMALY_LOCALLY_AND_IN_EVERY_MEASURED_INDEX_INCLUDING_A_Z6_TWISTED_FLUX_BUT_ANOMALOUS_SUBSETS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Overlap D = 1 + V of the cube walk's Euclidean Wilson kernel in SU(3) x SU(2) x U(1)_Y link backgrounds on Z^4 tori,
for one generation of supplied left-handed content Q(3,2,1/6), u^c(3b,1,-2/3), d^c(3b,1,1/3), L(1,2,-1/2), e^c(1,1,1),
nu^c(1,1,0); contrasts: lone Q, u^c dropped, quarks only, one extra triplet X(3,1,-1/3).
H = g5 X, X = D_W - m0, V = g5 sign(H); Luscher's P_hat_- = (1 + sign H)/2 (as in the overlap-nonabelian probe).
A: indices in topological backgrounds (simply-connected Cartan flux, and one Z6-twisted fractional flux) with a random
non-abelian SU(3)xSU(2)xU(1) perturbation; B: exact lattice C / pseudo-reality in single-factor backgrounds; C: local
covariant anomaly densities in generic backgrounds, strength scan, predicted pass/fail matrix from charge sums; D: GW.
Finite numerical diagnostic, NOT a non-perturbative existence proof (open in the literature). Content and hypercharges
are supplied inputs. Cited: Neuberger 1998; Luscher 1998-2000; Hasenfratz-Laliena-Niedermayer 1998.
Self-contained; seeded; numpy only."""
AUDIT_TIMEOUT_SEC = 120
import time, resource
from fractions import Fraction as Fr
import numpy as np

rng = np.random.default_rng(20261023)
T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1]).astype(complex)
SIG = [s1, s2, s3]; I2 = np.eye(2); Z2 = 0 * I2
G4 = [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in SIG] + [np.block([[Z2, I2], [I2, Z2]])]
G5 = G4[0] @ G4[1] @ G4[2] @ G4[3]
M0 = 1.6   # copy mass, same supplied resolution choice as the overlap-nonabelian probe
GM = np.zeros((8, 3, 3), complex)
for k, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
    GM[[0, 3, 5][k], i, j] = GM[[0, 3, 5][k], j, i] = 1; GM[[1, 4, 6][k], i, j] = -1j; GM[[1, 4, 6][k], j, i] = 1j
GM[2] = np.diag([1, -1, 0]); GM[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T3c = GM / 2                                           # triplet generators; antitriplet: -T^*
assert np.allclose(np.einsum('aij,bji->ab', T3c, T3c), np.eye(8) / 2)

def hexp(M, eps):      # exp(i eps M), M hermitian stack
    w, v = np.linalg.eigh(M); return np.einsum('xij,xj,xkj->xik', v, np.exp(1j * eps * w), v.conj())
def smooth(L, ncomp, nmodes=4):
    c = np.indices((L,) * 4).reshape(4, -1).T / L; out = np.zeros((4, L ** 4, ncomp))
    for mu in range(4):
        for a in range(ncomp):
            for _ in range(nmodes):
                k = rng.integers(-1, 2, 4); out[mu, :, a] += rng.normal() * np.cos(2 * np.pi * c @ k + rng.uniform(0, 2 * np.pi))
    return out / np.sqrt(nmodes)
def unit_flux(L):      # unit flux in the (12) and (34) planes for a charge-one component
    c = np.indices((L,) * 4).reshape(4, -1); ph = np.zeros((4, L ** 4)); Fp = 2 * np.pi / (L * L)
    for (p, q) in ((0, 1), (2, 3)):
        ph[p] += -Fp * c[q]; ph[q] += np.where(c[q] == L - 1, Fp * L * c[p], 0.0)
    return ph
def build_H(L, links, nc):
    N = L ** 4; idx = np.arange(N).reshape((L,) * 4); n = N * nc * 4; xs = np.arange(N)
    H = np.zeros((n, n), complex); H6 = H.reshape(N, nc, 4, N, nc, 4)
    H6[xs, :, :, xs, :, :] += np.einsum('ab,st->asbt', np.eye(nc), (4 - M0) * G5)[None]
    for mu in range(4):
        sh = np.roll(idx, -1, axis=mu).reshape(-1); U = links[mu]
        H6[xs, :, :, sh, :, :] += np.einsum('xab,st->xasbt', U, G5 @ (G4[mu] - np.eye(4)) / 2)
        H6[sh, :, :, xs, :, :] += np.einsum('xba,st->xasbt', U.conj(), -G5 @ (G4[mu] + np.eye(4)) / 2)
    return H

# fields: (name, colour rep, weak rep, Y)
FLD = {'Q': ('3', 2, Fr(1, 6)), 'u': ('3b', 1, Fr(-2, 3)), 'd': ('3b', 1, Fr(1, 3)), 'L': ('1', 2, Fr(-1, 2)),
       'e': ('1', 1, Fr(1)), 'n': ('1', 1, Fr(0)), 'X': ('3', 1, Fr(-1, 3))}
dc = lambda r: 1 if r == '1' else 3
SETS = {'family': 'QudLen', 'lone Q': 'Q', 'no u^c': 'QdLen', 'quarks': 'Qud', '+X(3,1,-1/3)': 'QudLenX'}
def coeffs(s):         # exact anomaly coefficients of a set
    Y3 = sum(dc(FLD[f][0]) * FLD[f][1] * FLD[f][2] ** 3 for f in s)
    cY = sum(FLD[f][1] * FLD[f][2] for f in s if FLD[f][0] != '1')                 # Tr SU(3)^2 Y (x 1/2)
    wY = sum(dc(FLD[f][0]) * FLD[f][2] for f in s if FLD[f][1] == 2)               # Tr SU(2)^2 Y (x 1/2)
    A3 = sum(FLD[f][1] * (1 if FLD[f][0] == '3' else -1) for f in s if FLD[f][0] != '1')   # Tr SU(3)^3 / d_abc
    gY = sum(dc(FLD[f][0]) * FLD[f][1] * FLD[f][2] for f in s)                     # Tr Y (gravitational)
    return dict(Y3=Y3, cY=cY, wY=wY, A3=A3, gY=gY)

def comp_flux(f, a, b, phi):
    cr, nw, Y = FLD[f]; ca = np.array(a, float) if cr == '3' else (-np.array(a, float) if cr == '3b' else np.zeros(1))
    wb = np.array(b, float) if nw == 2 else np.zeros(1); q = 6 * float(Y)
    fl = (ca[:, None] + wb[None, :] + q * phi).reshape(-1); fr = np.round(fl)
    return fr.astype(int), bool(np.abs(fl - fr).max() < 1e-9)
def links_of(L, f, e3, e2, e1, A3_, A2_, B_, flux=None):
    """colour link exp(i e3 A.T) (conjugated for 3b) x SU(2) link exp(i e2 A.s/2) x exp(i 2 e1 Y B) x Cartan flux phases."""
    cr, nw, Y = FLD[f]; N = L ** 4; out = []; ph1 = unit_flux(L) if flux is not None else None
    if flux is not None:
        fl, ok = comp_flux(f, *flux); assert ok
    for mu in range(4):
        Uc = hexp(np.einsum('xa,aij->xij', A3_[mu], T3c), e3) if cr != '1' else np.ones((N, 1, 1), complex)
        if cr == '3b': Uc = Uc.conj()
        Uw = hexp(np.einsum('xa,aij->xij', A2_[mu], np.array(SIG) / 2), e2) if nw == 2 else np.ones((N, 1, 1), complex)
        d = Uc.shape[1] * nw
        Lk = np.einsum('xab,xij->xaibj', Uc, Uw).reshape(N, d, d) * np.exp(1j * float(Y) * 2 * e1 * B_[mu])[:, None, None]
        if flux is not None: Lk = Lk * np.exp(1j * fl[None, :] * ph1[mu][:, None])[:, None, :]
        out.append(Lk)
    return out, d
def gens(f):
    cr, nw, Y = FLD[f]; ncol = dc(cr)
    C = None if cr == '1' else np.array([np.kron(T if cr == '3' else -T.conj(), np.eye(nw)) for T in T3c])
    W = None if nw == 1 else np.array([np.kron(np.eye(ncol), s / 2) for s in SIG])
    return C, W
def field_dens(L, f, e3, e2, e1, bg):
    lk, d = links_of(L, f, e3, e2, e1, *bg); H = build_H(L, lk, d); w, v = np.linalg.eigh(H); del H
    N = L ** 4; sg = np.sign(w); vb = v.reshape(N, d, 4, -1); Sxx = np.zeros((N, d, d), complex)
    for x0 in range(0, N, 9):
        Sxx[x0:x0 + 9] = np.einsum('xasn,xbsn->xab', vb[x0:x0 + 9] * sg, vb[x0:x0 + 9].conj())
    del v, vb
    C, W = gens(f); out = {'Y': float(FLD[f][2]) * np.real(np.einsum('xaa->x', Sxx)), 'tr': np.real(np.einsum('xaa->x', Sxx))}
    out['C'] = None if C is None else np.real(np.einsum('kab,xba->kx', C, Sxx))
    out['W'] = None if W is None else np.real(np.einsum('kab,xba->kx', W, Sxx))
    return out, np.abs(w).min()
def set_metric(dd, s):
    N = len(dd['Q']['Y']); y = sum(dd[f]['Y'] for f in s); c = np.zeros((8, N)); wv = np.zeros((3, N))
    for f in s:
        if dd[f]['C'] is not None: c = c + dd[f]['C']
        if dd[f]['W'] is not None: wv = wv + dd[f]['W']
    return dict(Y=np.abs(y).max(), C=np.sqrt((c ** 2).sum(0)).max(), W=np.sqrt((wv ** 2).sum(0)).max())

L3 = 3
bgA = (smooth(L3, 8), smooth(L3, 3), smooth(L3, 1)[..., 0])     # perturbation for topology
bgC = (smooth(L3, 8), smooth(L3, 3), smooth(L3, 1)[..., 0])     # generic background for densities
print("exact coefficients (Tr Y^3, Tr_3 Y, Tr_2 Y, SU(3)^3 count, Tr Y):")
for nm, s in SETS.items():
    k = coeffs(s); print(f"  {nm:13s} " + " ".join(f"{key}={str(val):6s}" for key, val in k.items()))

# ---------- A. topology on 3^4: indices with a random SU(3)xSU(2)xU(1) perturbation (strength 0.15) ----------
def indices(flux, pert=0.15):
    out = {}; gaps = []
    for f in FLD:
        fl, ok = comp_flux(f, *flux); lk, d = links_of(L3, f, pert, pert, pert, *bgA, flux=flux)
        w = np.linalg.eigvalsh(build_H(L3, lk, d)); out[f] = (int(round(-np.sign(w).sum() / 2)), -int((fl ** 2).sum()))
        gaps.append(np.abs(w).min())
    return out, min(gaps)
def Ysums(idx): return {nm: sum(FLD[f][2] * idx[f][0] for f in s) for nm, s in SETS.items()}
def Ypred(idx): return {nm: sum(FLD[f][2] * idx[f][1] for f in s) for nm, s in SETS.items()}
tA = time.time()
for lab, flux, txt in (("A1", ((1, -1, 0), (0, 0), 0.0), "simply-connected SU(3) Cartan flux diag(1,-1,0) (both planes)"),
                       ("A2", ((1/3, 1/3, -2/3), (1/2, -1/2), 1/6), "Z6-twisted flux: SU(3) centre (1/3,1/3,-2/3) + SU(2) (1/2,-1/2) + U(1) 1/6 per unit 6Y")):
    ix, gp = indices(flux); ys, yp = Ysums(ix), Ypred(ix)
    ok = all(ix[f][0] == ix[f][1] for f in FLD) and ys == yp and ys['family'] == 0 and all(
        (ys[nm] != 0) == (yp[nm] != 0) for nm in SETS)
    check(f"{lab} {txt}, x random SU(3)xSU(2)xU(1): every index = -sum f^2; sum Y index = 0 for the family, matches "
          "charge prediction for every contrast", ok,
          "idx " + ",".join(f"{f}{ix[f][0]}" for f in FLD) + "; sumY " + ", ".join(f"{nm} {ys[nm]}" for nm in SETS) + f"; gap {gp:.3f}")
# A3: Cartan-generator weighted integrated anomalies from per-component U(1) indices (abelian blocks, measured idx(f))
idx1 = {}
for fq in (-1, 0, 1):
    lk, _ = links_of(L3, 'e', 0, 0, 0, *bgA, flux=((0, 0, 0), (0, 0), fq / 6)); w = np.linalg.eigvalsh(build_H(L3, lk, 1))
    idx1[fq] = int(round(-np.sign(w).sum() / 2))
Xc = np.array([1, 1, -2.]); res3 = {}
for lab, flux in (("A1", ((1, -1, 0), (0, 0), 0.0)), ("A2", ((1/3, 1/3, -2/3), (1/2, -1/2), 1/6))):
    for nm, s in SETS.items():
        sx = sw = 0.0
        for f in s:
            cr, nw, Y = FLD[f]; fl, _ = comp_flux(f, *flux); ii = np.array([idx1[int(v)] for v in fl])
            xc = (Xc if cr == '3' else -Xc if cr == '3b' else np.zeros(1)); tw = np.array([.5, -.5]) if nw == 2 else np.zeros(1)
            sx += float((np.repeat(xc, nw) * ii).sum()); sw += float((np.tile(tw, dc(cr)) * ii).sum())
        res3[(lab, nm)] = (sx, sw)
ok3 = idx1 == {-1: -1, 0: 0, 1: -1} and all(res3[(l, 'family')] == (0.0, 0.0) for l in ("A1", "A2")) and \
    res3[("A1", 'no u^c')][0] != 0 and res3[("A1", '+X(3,1,-1/3)')][0] != 0 and res3[("A2", 'quarks')][1] != 0
check("A3 abelian blocks: component index idx(f) = -f^2 (f = -1,0,1); colour diag(1,1,-2)- and weak T3-weighted integrated "
      "anomalies vanish for the family (SU(3)^3, SU(2)^2 Y), not for no-u^c / +X (colour) or quarks (weak)", ok3,
      f"idx {idx1}; " + "; ".join(f"{l} {nm}: {res3[(l, nm)][0]:+.0f},{res3[(l, nm)][1]:+.1f}" for l in ("A1", "A2") for nm in SETS if nm != 'lone Q'))
adm = {f: comp_flux(f, (1/3, 1/3, -2/3), (1/2, -1/2), 1/6)[1] for f in FLD}
FLD['X0'] = ('3', 1, Fr(0)); FLD['D0'] = ('1', 2, Fr(0)); FLD['T2'] = ('3', 1, Fr(2, 3))
adm2 = {f: comp_flux(f, (1/3, 1/3, -2/3), (1/2, -1/2), 1/6)[1] for f in ('X0', 'D0', 'T2')}
check("A4 global form: all 16 fields (and X) have integer component fluxes in the Z6-twisted background (are reps of "
      "the Z6 quotient); (3,1,0) and (1,2,0) do not, (3,1,2/3) does", all(adm.values()) and adm2 == {'X0': False, 'D0': False, 'T2': True},
      f"{adm2}; A-section {time.time()-tA:.0f}s")
for k in ('X0', 'D0', 'T2'): del FLD[k]

# ---------- B. single-factor backgrounds on 3^4: exact lattice C and pseudo-reality ----------
tB = time.time()
dd3 = {f: field_dens(L3, f, 0.3, 0, 0, bgC)[0] for f in 'QudX'}
rC = max(np.abs(dd3['u']['C'] + dd3['Q']['C'] / 2).max(), np.abs(dd3['u']['tr'] - dd3['X']['tr']).max())
m3 = {nm: set_metric({**dd3, **{f: dict(Y=0 * dd3['Q']['Y'], C=None, W=None) for f in 'Len'}}, s) for nm, s in SETS.items()}
check("B1 pure SU(3) (eps=0.3): lattice C gives antitriplet tr(T g5 D) = -triplet's, tr(g5 D) equal (1e-12). Family "
      "SU(3) density (SU(3)^3) and Y-weighted density (SU(3)^2 Y) vanish at every site; no u^c and +X fail both; quarks pass Y",
      rC < 1e-12 and m3['family']['C'] < 1e-12 and m3['family']['Y'] < 1e-12 and m3['quarks']['Y'] < 1e-12 and
      min(m3['no u^c']['C'], m3['no u^c']['Y'], m3['+X(3,1,-1/3)']['C'], m3['+X(3,1,-1/3)']['Y']) > 1e-5,
      f"C-rel {rC:.0e}; family C {m3['family']['C']:.0e} Y {m3['family']['Y']:.0e}; no u^c C {m3['no u^c']['C']:.1e} "
      f"Y {m3['no u^c']['Y']:.1e}; +X C {m3['+X(3,1,-1/3)']['C']:.1e}; lone Q C {m3['lone Q']['C']:.1e}")
dd2 = {f: field_dens(L3, f, 0, 0.3, 0, bgC)[0] for f in 'QL'}
zero = {f: dict(Y=0 * dd2['Q']['Y'], C=None, W=None) for f in 'udenX'}
m2 = {nm: set_metric({**dd2, **zero}, s) for nm, s in SETS.items()}
check("B2 pure SU(2) (eps=0.3): Y-weighted density (SU(2)^2 Y: 3 colours x Q + L) vanishes at every site; quarks "
      "alone and lone Q fail", m2['family']['Y'] < 1e-12 and m2['quarks']['Y'] > 1e-5 and m2['family']['W'] < 1e-12,
      f"family Y {m2['family']['Y']:.0e}, W {m2['family']['W']:.0e}; quarks Y {m2['quarks']['Y']:.1e}; {time.time()-tB:.0f}s")
# pure U(1)_Y: each field = dim copies of one charge-Y component (blocks decouple); measured e(Y) per charge
epss = [0.2, 0.1, 0.05]; eY = {}
for e in epss:
    for f in FLD:
        eY[(e, f)] = field_dens(L3, 'e', 0, 0, e * float(FLD[f][2]), bgC)[0]['tr']   # charge-one comp at strength e*Y
tab1 = {nm: [np.abs(sum(dc(FLD[f][0]) * FLD[f][1] * float(FLD[f][2]) * eY[(e, f)] for f in s)).max() for e in epss] for nm, s in SETS.items()}
sl1 = {nm: np.polyfit(np.log(epss), np.log(v), 1)[0] for nm, v in tab1.items()}
check("B3 pure U(1)_Y scan eps=0.2,0.1,0.05: family density ~ eps^4 (Tr Y^3 = 0, C-even e(Y); |s-4|<0.4), lone Q and "
      "quarks ~ eps^2 (|s-2|<0.3). Tr Y = 0 is charge arithmetic only (no curved background)",
      abs(sl1['family'] - 4) < 0.4 and abs(sl1['lone Q'] - 2) < 0.3 and abs(sl1['quarks'] - 2) < 0.3,
      ", ".join(f"{nm} {sl1[nm]:.2f}" for nm in SETS))

# ---------- C. generic SU(3) x SU(2) x U(1)_Y backgrounds on 3^4: predicted pass/fail matrix ----------
tC = time.time(); tabs = []
for e in epss:
    dd = {f: field_dens(L3, f, e, e, e, bgC)[0] for f in FLD}; tabs.append({nm: set_metric(dd, s) for nm, s in SETS.items()})
    if e == epss[0]: dd0 = dd
    del dd
pred = {}
for nm, s in SETS.items():
    k = coeffs(s)
    pred[nm] = dict(Y=any(k[c] != 0 for c in ('Y3', 'cY', 'wY')), C=any(k[c] != 0 for c in ('A3', 'cY')), W=k['wY'] != 0)
sl = {(nm, dr): np.polyfit(np.log(epss), np.log([t[nm][dr] for t in tabs]), 1)[0] for nm in SETS for dr in 'YCW'}
def agree(nm, dr): return abs(sl[(nm, dr)] - 2) < 0.3 if pred[nm][dr] else sl[(nm, dr)] >= 2.7
fmt = lambda nm: " ".join(f"{dr}{'x' if pred[nm][dr] else 'o'}{sl[(nm, dr)]:.2f}" for dr in 'YCW')
check("C1 generic background, eps=0.2,0.1,0.05: family anomaly densities in U(1)_Y, SU(3), SU(2) directions fall at "
      "least as eps^2.7 (continuum anomaly cancelled); lone Q falls as eps^2 in all three (|s-2|<0.3)",
      all(agree(nm, dr) for nm in ('family', 'lone Q') for dr in 'YCW'),
      f"family {fmt('family')}; lone Q {fmt('lone Q')}; (x = anomalous predicted, o = cancel)")
check("C2 contrasts, same scan, every direction as charge sums predict (x: |s-2|<0.3, o: s>=2.7): no u^c fails Y,SU(3); "
      "quarks fail Y,SU(2) and pass SU(3); +X fails Y,SU(3)", all(agree(nm, dr) for nm in ('no u^c', 'quarks', '+X(3,1,-1/3)') for dr in 'YCW'),
      "; ".join(f"{nm} {fmt(nm)}" for nm in ('no u^c', 'quarks', '+X(3,1,-1/3)')))
r = {dr: tabs[-1]['family'][dr] / tabs[-1]['lone Q'][dr] for dr in 'YCW'}
print(f"   eps=0.2 family/loneQ: Y {tabs[0]['family']['Y']/tabs[0]['lone Q']['Y']:.2e} C {tabs[0]['family']['C']/tabs[0]['lone Q']['C']:.2e} "
      f"W {tabs[0]['family']['W']/tabs[0]['lone Q']['W']:.2e}; eps=0.05: Y {r['Y']:.1e} C {r['C']:.1e} W {r['W']:.1e}; {time.time()-tC:.0f}s")
del dd0

# ---------- D. exact GW structure for an antitriplet in the generic background ----------
lk, d = links_of(L3, 'u', 0.3, 0.3, 0.3, *bgC); H = build_H(L3, lk, d); n = H.shape[0]
w, v = np.linalg.eigh(H); del H; S = (v * np.sign(w)) @ v.conj().T; del v
g5b = np.kron(np.eye(n // 4), G5); D = np.eye(n) + g5b @ S
gw = np.abs(g5b @ D + D @ g5b - D @ g5b @ D).max(); gh = np.abs(g5b @ D @ g5b - D.conj().T).max()
Ph = (np.eye(n) + S) / 2; rp = max(np.abs(Ph @ Ph - Ph).max(), np.abs(D @ Ph - (D + g5b @ D) / 2).max())
check("D1 u^c antitriplet in generic SU(3)xU(1) background (3^4, dim 972): GW, g5-hermiticity, P_hat_- projector "
      "with D P_hat_- = P_+ D exact", max(gw, gh, rp) < 1e-12, f"GW {gw:.0e}, herm {gh:.0e}, proj {rp:.0e}, gap {np.abs(w).min():.3f}")
del D, S, Ph, g5b

print("Supplied: SU(3)xSU(2)xU(1)_Y, the 16's content and hypercharges, m0=1.6, the Z6 global form (one twisted flux), "
      "background shapes. Finite diagnostic on 3^4; not a non-perturbative proof; gravitational Tr Y not measured.")
print(f"elapsed {time.time()-T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f} MB")
print(f"TOTAL: PASS={P} FAIL={F}")
