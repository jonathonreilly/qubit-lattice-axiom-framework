AUDIT_INPUT_PATHS = ('docs/THE_OVERLAP_CHIRAL_DETERMINANT_IN_SU2_X_U1_BACKGROUNDS_CANCELS_THE_FAMILY_GAUGE_ANOMALY_THROUGH_CUBIC_ORDER_AND_IN_EVERY_MEASURED_INDEX_BUT_A_SINGLE_DOUBLET_DOES_NOT_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Overlap D = 1 + V of the cube walk's Euclidean Wilson kernel in SU(2) x U(1)_Y link backgrounds on Z^4 tori.
H = g5 X, X = D_W - m0, V = g5 sign(H); Luscher's history-level projector P_hat_- = (1 - g5_hat)/2 = (1 + sign H)/2.
Checks: GW algebra and pseudo-reality in non-abelian backgrounds; the fixed-basis (parallel-transported) Weyl
determinant phase under gauge transformations; covariant anomaly densities for (a) one doublet versus (b) one
colour-summed family of the 16 (supplied SU(2) x U(1)_Y content); indices in topological backgrounds; Witten count.
Finite numerical diagnostic, NOT a non-perturbative existence proof (open in the literature).
Supplied (cited): Neuberger 1998; Luscher 1998 (abelian, exact), 1999-2000 (non-abelian, all orders of perturbation
theory); Hasenfratz-Laliena-Niedermayer 1998 (index); Witten 1982 (SU(2) global anomaly); Kikukawa, Suzuki et al.
Self-contained; seeded; numpy only."""
AUDIT_TIMEOUT_SEC = 120
import time
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
M0 = 1.6   # copy mass inside the one-species window 0 < m0 < 2 (supplied choice; resolves flux 3 on 4^4)

def su2exp(a):
    th = np.linalg.norm(a, axis=-1) / 2 + 1e-300; nh = a / (2 * th[..., None])
    return np.cos(th)[..., None, None] * I2 + 1j * np.sin(th)[..., None, None] * sum(nh[..., k, None, None] * SIG[k] for k in range(3))
def shp(L): return (L,) * 4 if np.isscalar(L) else tuple(L)
def smooth(L, ncomp, nmodes=4):
    Ls = np.array(shp(L)); c = np.indices(shp(L)).reshape(4, -1).T / Ls; out = np.zeros((4, int(np.prod(Ls)), ncomp))
    for mu in range(4):
        for a in range(ncomp):
            for _ in range(nmodes):
                k = rng.integers(-1, 2, 4); out[mu, :, a] += rng.normal() * np.cos(2 * np.pi * c @ k + rng.uniform(0, 2 * np.pi))
    return out / np.sqrt(nmodes)
def unit_flux(L):      # unit flux in the (12) and (34) planes (charge-one phases on links)
    N = L ** 4; c = np.indices((L,) * 4).reshape(4, -1); ph = np.zeros((4, N)); Fp = 2 * np.pi / (L * L)
    for (p, q) in ((0, 1), (2, 3)):
        ph[p] += -Fp * c[q]; ph[q] += np.where(c[q] == L - 1, Fp * L * c[p], 0.0)
    return ph
def build_H(L, links, nc):
    """H = g5 X, X = sum_mu [T(g_mu - 1)/2 - T^+(g_mu + 1)/2] + (4 - m0), filled block by block in place."""
    N = int(np.prod(shp(L))); idx = np.arange(N).reshape(shp(L)); n = N * nc * 4; xs = np.arange(N)
    H = np.zeros((n, n), complex); H6 = H.reshape(N, nc, 4, N, nc, 4)
    H6[xs, :, :, xs, :, :] += np.einsum('ab,st->asbt', np.eye(nc), (4 - M0) * G5)[None]
    for mu in range(4):
        sh = np.roll(idx, -1, axis=mu).reshape(-1); U = links[mu]
        H6[xs, :, :, sh, :, :] += np.einsum('xab,st->xasbt', U, G5 @ (G4[mu] - np.eye(4)) / 2)
        H6[sh, :, :, xs, :, :] += np.einsum('xba,st->xasbt', U.conj(), -G5 @ (G4[mu] + np.eye(4)) / 2)
    return H
def links_of(L, nc, Y, eps, A, B, flux=None):
    """Doublet: SU(2) link exp(i eps A.sigma/2) times hypercharge phase; singlet: hypercharge phase only.
    flux = per-component integer fluxes (both planes) of the abelian (topological) part."""
    out = []; ph1 = unit_flux(L) if flux is not None else None
    for mu in range(4):
        u = np.exp(1j * Y * 2 * eps * B[mu])
        if nc == 2:
            Lk = su2exp(eps * A[mu]) * u[:, None, None]
            if flux is not None: Lk = Lk @ np.stack([np.diag(np.exp(1j * np.array(flux) * p)) for p in ph1[mu]])
        else:
            Lk = u[:, None, None] * (np.exp(1j * flux[0] * ph1[mu])[:, None, None] if flux is not None else 1)
        out.append(Lk)
    return out
def sign_diag(H, nc):
    """sign(H)(x,x) traced over spin -> colour matrix per site; returns (S_xx, eigvecs, signs, gap)."""
    w, v = np.linalg.eigh(H); N = H.shape[0] // (4 * nc); sg = np.sign(w)
    vb = v.reshape(N, nc, 4, -1); Sxx = np.zeros((N, nc, nc), complex)
    for x0 in range(0, N, 16):
        Sxx[x0:x0 + 16] = np.einsum('xasn,xbsn->xab', vb[x0:x0 + 16] * sg, vb[x0:x0 + 16].conj())
    return Sxx, v, sg, np.abs(w).min()
def dens(Sxx, nc):
    d = {'Y': np.real(np.einsum('xaa->x', Sxx))}       # tr(g5 D(x,x)) = tr sign H(x,x)
    if nc == 2:
        for k in range(3): d[k] = np.real(np.einsum('xab,ba->x', Sxx, SIG[k] / 2))   # tr(T^a g5 D(x,x))
    return d
# the 16 per family as left-handed fields: (name, colour dim of SU(2), Y, colour multiplicity)
FAM = [('Q', 2, Fr(1, 6), 3), ('L', 2, Fr(-1, 2), 1), ('u', 1, Fr(-2, 3), 3), ('d', 1, Fr(1, 3), 3), ('e', 1, Fr(1), 1), ('n', 1, Fr(0), 1)]

# all random fields drawn up front (fixed order); sections run largest-matrix first to bound peak memory
L3 = 3; A3 = smooth(L3, 3); B3 = smooth(L3, 1)[..., 0]; eps0 = 0.3; om = rng.normal(size=L3 ** 4)
LC = (4, 4, 4, 3); AC = smooth(LC, 3); BC = smooth(LC, 1)[..., 0]
L4 = 4; A4 = smooth(L4, 3); B4 = smooth(L4, 1)[..., 0]

# ---------- A. topology: indices in non-abelian backgrounds with abelian flux (4^4) ----------
def fam_index(nW, mY, pert=0.15):
    """(SU(2) x U(1))/Z2 background: SU(2) part s3 * (nW/2) unit flux, U(1)_Y part (mY/2) per unit q = 6Y, plus a
    random smooth SU(2) x U(1) perturbation. Component fluxes f = (s nW + q mY)/2 must be integers."""
    out = {}; gaps = []
    for (nm, nc, Y, mult) in FAM:
        q = int(6 * Y); fl = [(nW + q * mY) // 2, (-nW + q * mY) // 2] if nc == 2 else [q * mY // 2]
        assert all((s * nW + q * mY) % 2 == 0 for s in ((1, -1) if nc == 2 else (0,)))
        Hf = build_H(L4, links_of(L4, nc, float(Y), pert, A4, B4, flux=fl), nc)
        w = np.linalg.eigvalsh(Hf)
        del Hf
        out[nm] = (Fr(int(round(-np.sign(w).sum() / 2))), Fr(-sum(f * f for f in fl))); gaps.append(np.abs(w).min())
    out['gap'] = min(gaps); return out
t5 = time.time(); I1 = fam_index(2, 0)
ok1 = all(I1[nm][0] == I1[nm][1] for (nm, *_) in FAM)
sb1 = sum(mult * Y * I1[nm][0] for (nm, nc, Y, mult) in FAM); sa1 = FAM[1][2] * I1['L'][0]
check("A1 SU(2) flux nW=2 (instanton number 2) x random SU(2)xU(1): measured indices = -sum f^2 (Q,L: -2; singlets 0); "
      "integrated Y anomaly -2 sum Y index: (a) L alone != 0, (b) 16 = 0 exactly (SU(2)^2 Y)",
      ok1 and sb1 == 0 and sa1 != 0, f"Q {I1['Q'][0]}, L {I1['L'][0]}, sum(b) {sb1}, (a) Y*idx {sa1}, gap {I1['gap']:.3f}")
I2_ = fam_index(1, 1)
ok2 = all(I2_[nm][0] == I2_[nm][1] for (nm, *_) in FAM)
sb2 = sum(mult * Y * I2_[nm][0] for (nm, nc, Y, mult) in FAM); sa2 = FAM[1][2] * I2_['L'][0]
nd = 3 * I2_['Q'][0] + I2_['L'][0]
check("A2 (SU(2)xU(1))/Z2 half-flux background nW=mY=1 (doublets need odd 6Y, singlets even: the 16 fits): indices "
      "Q,L,u,d,e,nu = -1,-5,-4,-1,-9,0 measured; sum_f Y index = 0 exactly (Y^3 and T^2 Y together); (a) L alone != 0",
      ok2 and sb2 == 0 and sa2 != 0,
      f"{[int(I2_[nm][0]) for (nm, *_) in FAM]}, sum(b) {sb2}, (a) {sa2}, gap {I2_['gap']:.3f}, {time.time()-t5:.0f}s")
check("A3 mod-2 doublet count: one Q doublet has an odd index (-1) in A2; per family 3 Q + L gives -8 (even); "
      "Witten count: 4 doublets per family (even). The pi_4 global anomaly itself is NOT measured here",
      I2_['Q'][0] % 2 == 1 and nd % 2 == 0 and (3 + 1) % 2 == 0, f"Q {I2_['Q'][0]}, family {nd}")
# ---------- B. anomaly densities: (a) one doublet vs (b) the 16 per colour-summed family ----------
def family_dens(L, eps, A, B, want=('Q', 'L', 'u', 'd', 'e')):
    out = {}; gaps = []
    for (nm, nc, Y, mult) in FAM:
        if nm not in want: continue
        Sxx_, _, _, g_ = sign_diag(build_H(L, links_of(L, nc, float(Y), eps, A, B), nc), nc); out[nm] = dens(Sxx_, nc); gaps.append(g_)
    return out, min(gaps)
def anomalies(dd):
    aY_L = float(FAM[1][2]) * dd['L']['Y']; aY_Q = float(FAM[0][2]) * dd['Q']['Y']
    aY_b = sum(mult * float(Y) * dd[nm]['Y'] for (nm, nc, Y, mult) in FAM if nm in dd)
    terms = sum(abs(mult * float(Y)) * np.abs(dd[nm]['Y']).max() for (nm, nc, Y, mult) in FAM if nm in dd)
    aW_L = np.sqrt(sum(dd['L'][k] ** 2 for k in range(3))); aW_b = np.sqrt(sum((3 * dd['Q'][k] + dd['L'][k]) ** 2 for k in range(3)))
    aW_Q3 = np.sqrt(sum((3 * dd['Q'][k]) ** 2 for k in range(3)))
    return dict(YL=np.abs(aY_L).max(), YQ=np.abs(aY_Q).max(), Yb=np.abs(aY_b).max(), Yterms=terms, Ysum=abs(aY_b.sum()),
                WL=aW_L.max(), Wb=aW_b.max(), WQ3=aW_Q3.max())
t4 = time.time()
dd4, g4 = family_dens(LC, 0.2, AC, BC); an4 = anomalies(dd4); an4h = anomalies(family_dens(LC, 0.1, AC, BC)[0])
fall = (an4['Yb'] / an4['YL']) / (an4h['Yb'] / an4h['YL'])
check("B1 4^3x3 (doublet dim 1536): U(1)_Y covariant anomaly max_x, (a) L alone vs (b) the 16. eps=0.2: (b) < 3% of "
      "sum|terms|, sum_x(b) = 0; (b)/(a) falls by >= 3 from eps=0.2 to 0.1 (eps^2 law predicts 4)",
      an4['Yb'] < 0.03 * an4['Yterms'] and an4['Ysum'] < 1e-12 and fall >= 3,
      f"eps=0.2: (a) {an4['YL']:.2e}, Q alone {an4['YQ']:.2e}, (b) {an4['Yb']:.2e} = {an4['Yb']/an4['YL']:.2f}(a), "
      f"sum|terms| {an4['Yterms']:.2e}; eps=0.1: (b)/(a) {an4h['Yb']/an4h['YL']:.3f}, fall {fall:.1f}; gap {g4:.2f}, {time.time()-t4:.0f}s")
check("B2 4^3x3: SU(2) covariant anomaly |tr(T g5 D(x,x))| max_x, (a) L alone vs (b) 3 Q + L: (b) < 5% of (a) at eps=0.2, "
      "< 1.5% at eps=0.1", an4['Wb'] < 0.05 * an4['WL'] and an4h['Wb'] < 0.015 * an4h['WL'],
      f"eps=0.2: (a) {an4['WL']:.2e}, 3Q {an4['WQ3']:.2e}, (b) {an4['Wb']:.2e}; eps=0.1: (b)/(a) {an4h['Wb']/an4h['WL']:.4f}")
# scaling with background strength on 3^4: (a) ~ eps^2, (b) ~ eps^4 (quadratic and cubic orders cancel)
epss = [0.2, 0.1, 0.05]; tab = [anomalies(family_dens(L3, e, A3, B3)[0]) for e in epss]
def slope(key): return np.polyfit(np.log(epss), np.log([t[key] for t in tab]), 1)[0]
sl = {k: slope(k) for k in ('YL', 'Yb', 'WL', 'Wb')}
check("B3 3^4 strength scan eps = 0.2, 0.1, 0.05: (a) anomaly ~ eps^2 (exponent within 0.3 of 2), (b) ~ eps^4 "
      "(within 0.4 of 4), in both U(1)_Y and SU(2) directions",
      abs(sl['YL'] - 2) < 0.3 and abs(sl['WL'] - 2) < 0.3 and abs(sl['Yb'] - 4) < 0.4 and abs(sl['Wb'] - 4) < 0.4,
      "exponents Y: a %.2f b %.2f; SU2: a %.2f b %.2f; (b)/(a) at eps=0.05: Y %.1e, SU2 %.1e" % (
          sl['YL'], sl['Yb'], sl['WL'], sl['Wb'], tab[-1]['Yb'] / tab[-1]['YL'], tab[-1]['Wb'] / tab[-1]['WL']))
# exact charge sums: order-2 and order-3 coefficients vanish for the 16; the order-4 ones do not
Ys = [(Y, mult * nc) for (nm, nc, Y, mult) in FAM]; dbl = [(Y, mult) for (nm, nc, Y, mult) in FAM if nc == 2]
sY = sum(m * y for y, m in Ys); sY3 = sum(m * y ** 3 for y, m in Ys); sT2Y = sum(m * y for y, m in dbl)
sY5 = sum(m * y ** 5 for y, m in Ys); sD3 = sum(m * y ** 3 for y, m in dbl)
check("B4 exact charge sums of the 16: sum Y = sum Y^3 = sum_doublets Y (T^2 Y) = 0 kill every term of order <= 3 "
      "(C and pseudo-reality fix the parities, C2); order-4 coefficients sum Y^5, sum_doublets Y^3 are nonzero",
      sY == 0 and sY3 == 0 and sT2Y == 0 and sY5 != 0 and sD3 != 0, f"{sY}, {sY3}, {sT2Y}; Y^5 {sY5}, dblY^3 {sD3}")

# ---------- C. exact structure in a non-abelian SU(2) x U(1) background (3^4) ----------
def lg5(M): return np.einsum('st,itn->isn', G5, M.reshape(-1, 4, M.shape[1])).reshape(M.shape)   # (1 x g5) M
def rg5(M): return np.einsum('nis,st->nit', M.reshape(M.shape[0], -1, 4), G5).reshape(M.shape)   # M (1 x g5)
H = build_H(L3, links_of(L3, 2, 1 / 6, eps0, A3, B3), 2); n = H.shape[0]; dg = np.arange(n)
Sxx, v, sg, gap = sign_diag(H, 2); del H
S = (v * sg) @ v.conj().T; D = lg5(S); D[dg, dg] += 1                     # D = 1 + g5 sign(H)
gw = np.abs(lg5(D) + rg5(D) - D @ lg5(D)).max(); gh = np.abs(lg5(rg5(D)) - D.conj().T).max()
Ph = S / 2; Ph[dg, dg] += 0.5                                              # P_hat_- = (1 + sign H)/2
IminusD = -D; IminusD[dg, dg] += 1; G5hat = lg5(IminusD); del IminusD
r_hat = np.abs(Ph - (np.eye(n) - G5hat) / 2).max(); del G5hat
r_pr = np.abs(Ph @ Ph - Ph).max(); r_sp = np.abs(D @ Ph - (D + lg5(D)) / 2).max()
check("C1 Q doublet (Y=1/6) in a random smooth SU(2)xU(1) background, 3^4 (dim 648): GW exact, g5-hermitian; "
      "P_hat_- = (1-g5_hat)/2 = (1+sign H)/2 is a projector with D P_hat_- = P_+ D",
      max(gw, gh, r_pr, r_sp, r_hat) < 1e-12, f"GW {gw:.0e}, g5-herm {gh:.0e}, split {r_sp:.0e}, H gap {gap:.3f}")
# C2 pseudo-reality: an SU(2) doublet has no perturbative SU(2) anomaly (d_abc = 0), exactly on the lattice
d0 = dens(sign_diag(build_H(L3, links_of(L3, 2, 0.0, eps0, A3, B3), 2), 2)[0], 2)
dm = dens(sign_diag(build_H(L3, links_of(L3, 2, -1 / 6, eps0, A3, B3), 2), 2)[0], 2); dp = dens(Sxx, 2)
z0 = max(np.abs(d0[k]).max() for k in range(3)); oddY = max(np.abs(dp[k] + dm[k]).max() for k in range(3))
evY = np.abs(dp['Y'] - dm['Y']).max(); sz = max(np.abs(dp[k]).max() for k in range(3))
check("C2 pseudo-reality (U* = s2 U s2) on the lattice: Y=0 doublet tr(T^a g5 D(x,x)) = 0 at every site; with Y, "
      "tr(T^a g5 D) is odd and tr(g5 D) even under Y -> -Y", z0 < 1e-12 and oddY < 1e-12 and evY < 1e-12 and sz > 1e-5,
      f"Y=0: {z0:.0e}; odd {oddY:.0e}, even {evY:.0e}; Y=1/6 size {sz:.1e}")

# ---------- D. Weyl determinant phase, fixed psi-bar basis, parallel-transported psi basis ----------
# W(U) = det(ubar^+ D v), ubar = basis of P_+ (field-independent), v = Lowdin transport of V0 into P_hat_-(U).
# Exact first-order lemma: d arg W / d eps along U -> U^g, g = exp(i eps Omega), equals -(1/2) Tr(sign H Omega)
#   = -(1/2) sum_x omega(x) tr(T g5 D(x,x)).  Ambiguity: v -> v Q(U) multiplies W by det Q(U) (the measure term).
V0 = v[:, sg > 0].copy(); del v
ub = np.kron(np.eye(n // 4), np.linalg.eigh(G5)[1][:, 2:])     # G5 eigenvalue +1 columns
def argW(gd):            # gauge rotation G = diag(gd) (both generators used are diagonal)
    Pe = gd[:, None] * Ph * gd.conj()[None, :]; M = V0.conj().T @ Pe @ V0; wm, um = np.linalg.eigh(M)
    ve = Pe @ (V0 @ ((um * wm ** -0.5) @ um.conj().T)); del Pe
    return np.angle(np.linalg.slogdet(ub.conj().T @ ((gd[:, None] * D * gd.conj()[None, :]) @ ve))[0])
res = []; h = 1e-4; diagS = np.real(np.diag(S)); del S
for (gen, lab) in ((I2 / 6, 'Y'), (SIG[2] / 2, 2)):
    od = np.repeat((om[:, None] * np.real(np.diag(gen))[None, :]).reshape(-1), 4)   # diag of Omega on (x, c, s)
    fd = np.angle(np.exp(1j * (argW(np.exp(1j * h * od)) - argW(np.exp(-1j * h * od))))) / (2 * h)
    pred = -0.5 * float(diagS @ od)
    pred2 = -0.5 * float(np.sum(om * (dp['Y'] / 6 if lab == 'Y' else dp[2])))
    res.append((fd, pred, pred2))
check("D1 fixed-basis Weyl phase: finite-difference d arg W/d eps under U(1)_Y and SU(2) gauge rotations = "
      "-(1/2) sum_x omega(x) tr(T g5 D(x,x)) (the covariant anomaly density smeared with omega)",
      all(abs(a - b) < 1e-6 * max(1, abs(b)) and abs(b - c) < 1e-10 for a, b, c in res),
      "; ".join(f"{a:.3e} vs {b:.3e}" for a, b, c in res))
del D, Ph, V0, ub

print("Supplied: SU(2)xU(1)_Y group, the 16's hypercharges, m0=1.6, (SU(2)xU(1))/Z2 global form in A2. Finite "
      "diagnostic on 3^4, 4^3x3, 4^4; not a non-perturbative proof.")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")
