#!/usr/bin/env python3
"""repaired-kernel-anomaly: rerun of the overlap-nonabelian (SU(2) x U(1)_Y) and overlap-colour (SU(3) x SU(2) x U(1)_Y)
checks with the REPAIRED overlap kernel of new-tick-recheck (the family-class tick's T-even kernel): spatial hop
sin K / sqrt3, spatial Wilson term = the tick's scalar 1 - f (r_s = 1/3), time v = r = 1; one-species window 0 < m0 < 2/3.
X = sum_mu [(v g_mu - r) T_mu U/2 - (v g_mu + r) T_mu^+ U^+/2] + (sum r - m0), H = g5 X, D = 1 + g5 sign H,
Luscher's P_hat_- = (1 + sign H)/2. Backgrounds, seeds, content and thresholds copied from the two probes (same seeds and
draw order, so the backgrounds are the old ones); only the kernel and m0 change. Criteria: criteria_pre_run.txt.
Finite numerical diagnostic, NOT a non-perturbative existence proof. Content, hypercharges, groups, global forms supplied.
Self-contained; seeded; numpy + scipy."""
AUDIT_TIMEOUT_SEC = 120
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import time, resource, itertools as it
from fractions import Fraction as Fr
import numpy as np
import scipy.linalg as sla

T0 = time.time(); NP = [0, 0]
def check(name, ok, info=""):
    ok = bool(ok); NP[0 if ok else 1] += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1]).astype(complex)
SIG = [s1, s2, s3]; I2 = np.eye(2); Z2 = 0 * I2
G4 = [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in SIG] + [np.block([[Z2, I2], [I2, Z2]])]
G5 = G4[0] @ G4[1] @ G4[2] @ G4[3]
VK = np.array([3 ** -.5] * 3 + [1.]); RK = np.array([1 / 3] * 3 + [1.])     # repaired kernel: v_s = 1/sqrt3, r_s = 1/3
M0 = 0.5    # inside 0 < m0 < 2/3; picked by the U(1)-only resolution pre-scan (criteria_pre_run.txt), not by any anomaly quantity
HOPF = [G5 @ (VK[m] * G4[m] - RK[m] * np.eye(4)) / 2 for m in range(4)]; HOPB = [-G5 @ (VK[m] * G4[m] + RK[m] * np.eye(4)) / 2 for m in range(4)]
def shp(L): return (L,) * 4 if np.isscalar(L) else tuple(L)
def build_H(L, links, nc):
    N = int(np.prod(shp(L))); idx = np.arange(N).reshape(shp(L)); n = N * nc * 4; xs = np.arange(N)
    H = np.zeros((n, n), complex); H6 = H.reshape(N, nc, 4, N, nc, 4)
    H6[xs, :, :, xs, :, :] += np.einsum('ab,st->asbt', np.eye(nc), (RK.sum() - M0) * G5)[None]
    for mu in range(4):
        sh = np.roll(idx, -1, axis=mu).reshape(-1); U = links[mu]
        H6[xs, :, :, sh, :, :] += np.einsum('xab,st->xasbt', U, HOPF[mu])
        H6[sh, :, :, xs, :, :] += np.einsum('xba,st->xasbt', U.conj(), HOPB[mu])
    return H
def unit_flux(L):      # unit flux in the (12) and (34) planes for a charge-one component (as in both probes)
    c = np.indices((L,) * 4).reshape(4, -1); ph = np.zeros((4, L ** 4)); Fp = 2 * np.pi / (L * L)
    for (p, q) in ((0, 1), (2, 3)):
        ph[p] += -Fp * c[q]; ph[q] += np.where(c[q] == L - 1, Fp * L * c[p], 0.0)
    return ph
def smooth(rng, L, ncomp, nmodes=4):
    Ls = np.array(shp(L)); c = np.indices(shp(L)).reshape(4, -1).T / Ls; out = np.zeros((4, int(np.prod(Ls)), ncomp))
    for mu in range(4):
        for a in range(ncomp):
            for _ in range(nmodes):
                k = rng.integers(-1, 2, 4); out[mu, :, a] += rng.normal() * np.cos(2 * np.pi * c @ k + rng.uniform(0, 2 * np.pi))
    return out / np.sqrt(nmodes)
def index_of(H): w = sla.eigh(H, eigvals_only=True, overwrite_a=True, check_finite=False); return int(round(-np.sign(w).sum() / 2)), np.abs(w).min()

# ================================================================ K. the kernel
print(f"== K. repaired kernel (v_s = 1/sqrt3, r_s = 1/3, v_t = r_t = 1), m0 = {M0}")
gr = np.linspace(-np.pi, np.pi, 8, endpoint=False); gw = 0.; nz = 0; I4 = np.eye(4)
for kk in it.product(gr, repeat=4):
    k = np.array(kk); X = 1j * sum(VK[m] * np.sin(k[m]) * G4[m] for m in range(4)) + (np.sum(RK * (1 - np.cos(k))) - M0) * I4
    e, v = np.linalg.eigh(G5 @ X); Dm = I4 + G5 @ (v * np.sign(e)) @ v.conj().T
    gw = max(gw, np.abs(G5 @ Dm + Dm @ G5 - Dm @ G5 @ Dm).max()); nz += np.linalg.norm(Dm) < 1e-9
check("K0 free kernel: GW exact, exactly one zero of D on 8^4 (one species)", gw < 1e-12 and nz == 1, f"GW {gw:.0e}, zeros {nz}")
res = {}
for L, fs in ((4, (1, 2, 3)), (3, (1,)), (5, (3,))):
    for f in fs: res[(L, f)] = index_of(build_H(L, [np.exp(1j * f * p)[:, None, None] for p in unit_flux(L)], 1))
check("K1 U(1) resolution at this m0: charge-one component in flux (f, f) has index -f^2 for f = 1, 2 on 4^4 and f = 1 on 3^4; "
      "f = 3 is NOT resolved on 4^4 (plaquette angle 3pi/8) but is on 5^4",
      all(res[(L, f)][0] == -f * f for (L, f) in ((4, 1), (4, 2), (3, 1), (5, 3))) and res[(4, 3)][0] != -9,
      "; ".join(f"{L}^4 f{f}: {res[(L, f)][0]} (gap {res[(L, f)][1]:.3f})" for (L, f) in res))

# ================================================================ N. SU(2) x U(1)_Y (overlap-nonabelian checks)
def section_N():
    rng = np.random.default_rng(20261023)
    def su2exp(a):
        th = np.linalg.norm(a, axis=-1) / 2 + 1e-300; nh = a / (2 * th[..., None])
        return np.cos(th)[..., None, None] * I2 + 1j * np.sin(th)[..., None, None] * sum(nh[..., k, None, None] * SIG[k] for k in range(3))
    def links_of(L, nc, Y, eps, A, B, flux=None):
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
        w, v = sla.eigh(H, overwrite_a=True, check_finite=False); N = H.shape[0] // (4 * nc); sg = np.sign(w)
        vb = v.reshape(N, nc, 4, -1); Sxx = np.zeros((N, nc, nc), complex)
        for x0 in range(0, N, 16):
            Sxx[x0:x0 + 16] = np.einsum('xasn,xbsn->xab', vb[x0:x0 + 16] * sg, vb[x0:x0 + 16].conj())
        return Sxx, v, sg, np.abs(w).min()
    def dens(Sxx, nc):
        d = {'Y': np.real(np.einsum('xaa->x', Sxx))}
        if nc == 2:
            for k in range(3): d[k] = np.real(np.einsum('xab,ba->x', Sxx, SIG[k] / 2))
        return d
    FAM = [('Q', 2, Fr(1, 6), 3), ('L', 2, Fr(-1, 2), 1), ('u', 1, Fr(-2, 3), 3), ('d', 1, Fr(1, 3), 3), ('e', 1, Fr(1), 1), ('n', 1, Fr(0), 1)]
    L3 = 3; A3 = smooth(rng, L3, 3); B3 = smooth(rng, L3, 1)[..., 0]; eps0 = 0.3; om = rng.normal(size=L3 ** 4)
    LC = (4, 4, 4, 3); smooth(rng, LC, 3); smooth(rng, LC, 1)        # drawn only to keep the old draw order (NB1/NB2 dropped)
    L4 = 4; A4 = smooth(rng, L4, 3); B4 = smooth(rng, L4, 1)[..., 0]
    r5 = np.random.default_rng(20261024); A5 = smooth(r5, 5, 3); B5 = smooth(r5, 5, 1)[..., 0]   # new: 5^4 singlets only
    def fam_index(L, A, B, nW, mY, names, pert=0.15):
        out = {}; gaps = []
        for (nm, nc, Y, mult) in FAM:
            if nm not in names: continue
            q = int(6 * Y); fl = [(nW + q * mY) // 2, (-nW + q * mY) // 2] if nc == 2 else [q * mY // 2]
            ix, g = index_of(build_H(L, links_of(L, nc, float(Y), pert, A, B, flux=fl), nc))
            out[nm] = (Fr(ix), Fr(-sum(f * f for f in fl))); gaps.append(g)
        out['gap'] = min(gaps); return out
    print("== N. SU(2) x U(1)_Y (overlap-nonabelian checks; colour a spectator multiplicity)")
    t5 = time.time(); I1 = fam_index(L4, A4, B4, 2, 0, 'QLuden')
    ok1 = all(I1[nm][0] == I1[nm][1] for (nm, *_) in FAM)
    sb1 = sum(mult * Y * I1[nm][0] for (nm, nc, Y, mult) in FAM); sa1 = FAM[1][2] * I1['L'][0]
    check("NA1 4^4 SU(2) flux nW=2 x random SU(2)xU(1): every index = -sum f^2; family sum Y idx = 0, L alone != 0",
          ok1 and sb1 == 0 and sa1 != 0, f"Q {I1['Q'][0]}, L {I1['L'][0]}, sum(b) {sb1}, (a) {sa1}, gap {I1['gap']:.3f}")
    I2_ = fam_index(L4, A4, B4, 1, 1, 'QLuden')
    sb2 = sum(mult * Y * I2_[nm][0] for (nm, nc, Y, mult) in FAM)
    unres = [nm for (nm, *_) in FAM if I2_[nm][0] != I2_[nm][1]]
    check("NA2a 4^4 (SU(2)xU(1))/Z2 half-flux nW=mY=1: Q,L,u,d,nu (|f| <= 2) give -sum f^2; e^c (f = 3) is NOT resolved, "
          "so the 4^4 family sum is not a test at this kernel (resolution failure, reported)",
          unres == ['e'] and all(I2_[nm][0] == I2_[nm][1] for nm in 'QLudn'),
          f"{[int(I2_[nm][0]) for (nm, *_) in FAM]} vs {[int(I2_[nm][1]) for (nm, *_) in FAM]}; 4^4 sum {sb2}; gap {I2_['gap']:.3f}")
    I5 = fam_index(5, A5, B5, 1, 1, 'uden')
    ok5 = all(I5[nm][0] == I5[nm][1] for nm in 'uden')
    mix = {nm: (I2_[nm][0] if nm in 'QL' else I5[nm][0]) for (nm, *_) in FAM}
    sbm = sum(mult * Y * mix[nm] for (nm, nc, Y, mult) in FAM); sam = FAM[1][2] * mix['L']
    check("NA2b singlets of the same Z2 background on 5^4 (doublets dim 5000 exceed the 3072 cap, kept on 4^4): u,d,e,nu = "
          "-4,-1,-9,0; cross-lattice family sum Y idx = 0, L alone != 0 [integers of the same flux class, two lattices]",
          ok5 and sbm == 0 and sam != 0, f"5^4 {[int(I5[nm][0]) for nm in 'uden']}, sum {sbm}, (a) {sam}, gap {I5['gap']:.3f}, "
          f"A {time.time() - t5:.0f}s")
    nd = 3 * I2_['Q'][0] + I2_['L'][0]
    check("NA3 mod 2: one Q doublet odd index in NA2; 3 Q + L even (pi_4 anomaly itself not measured)",
          I2_['Q'][0] % 2 == 1 and nd % 2 == 0, f"Q {I2_['Q'][0]}, family {nd}")
    def family_dens(L, eps, A, B):
        out = {}
        for (nm, nc, Y, mult) in FAM:
            if nm == 'n': continue
            out[nm] = dens(sign_diag(build_H(L, links_of(L, nc, float(Y), eps, A, B), nc), nc)[0], nc)
        return out
    def anomalies(dd):
        aY_L = float(FAM[1][2]) * dd['L']['Y']; aY_b = sum(mult * float(Y) * dd[nm]['Y'] for (nm, nc, Y, mult) in FAM if nm in dd)
        aW_L = np.sqrt(sum(dd['L'][k] ** 2 for k in range(3))); aW_b = np.sqrt(sum((3 * dd['Q'][k] + dd['L'][k]) ** 2 for k in range(3)))
        return dict(YL=np.abs(aY_L).max(), Yb=np.abs(aY_b).max(), WL=aW_L.max(), Wb=aW_b.max())
    epss = [0.2, 0.1, 0.05]; tab = [anomalies(family_dens(L3, e, A3, B3)) for e in epss]
    sl = {k: np.polyfit(np.log(epss), np.log([t[k] for t in tab]), 1)[0] for k in ('YL', 'Yb', 'WL', 'Wb')}
    check("NB3 3^4 scan eps=0.2,0.1,0.05: lone doublet ~ eps^2 (|s-2|<0.3), family ~ eps^4 (|s-4|<0.4), Y and SU(2)",
          abs(sl['YL'] - 2) < 0.3 and abs(sl['WL'] - 2) < 0.3 and abs(sl['Yb'] - 4) < 0.4 and abs(sl['Wb'] - 4) < 0.4,
          "Y: a %.2f b %.2f; SU2: a %.2f b %.2f; (b)/(a) eps=0.05: Y %.1e, SU2 %.1e" % (
              sl['YL'], sl['Yb'], sl['WL'], sl['Wb'], tab[-1]['Yb'] / tab[-1]['YL'], tab[-1]['Wb'] / tab[-1]['WL']))
    Ys = [(Y, mult * nc) for (nm, nc, Y, mult) in FAM]; dbl = [(Y, mult) for (nm, nc, Y, mult) in FAM if nc == 2]
    sY = sum(m * y for y, m in Ys); sY3 = sum(m * y ** 3 for y, m in Ys); sT2Y = sum(m * y for y, m in dbl)
    sY5 = sum(m * y ** 5 for y, m in Ys); sD3 = sum(m * y ** 3 for y, m in dbl)
    check("NB4 exact sums: Y = Y^3 = doublets Y = 0 (orders <= 3 cancel); Y^5, doublets Y^3 != 0",
          sY == 0 and sY3 == 0 and sT2Y == 0 and sY5 != 0 and sD3 != 0, f"{sY}, {sY3}, {sT2Y}; {sY5}, {sD3}")
    def lg5(M): return np.einsum('st,itn->isn', G5, M.reshape(-1, 4, M.shape[1])).reshape(M.shape)
    def rg5(M): return np.einsum('nis,st->nit', M.reshape(M.shape[0], -1, 4), G5).reshape(M.shape)
    H = build_H(L3, links_of(L3, 2, 1 / 6, eps0, A3, B3), 2); n = H.shape[0]; dg = np.arange(n)
    Sxx, v, sg, gap = sign_diag(H, 2); del H
    S = (v * sg) @ v.conj().T; D = lg5(S); D[dg, dg] += 1
    gw = np.abs(lg5(D) + rg5(D) - D @ lg5(D)).max(); gh = np.abs(lg5(rg5(D)) - D.conj().T).max()
    Ph = S / 2; Ph[dg, dg] += 0.5
    r_pr = np.abs(Ph @ Ph - Ph).max(); r_sp = np.abs(D @ Ph - (D + lg5(D)) / 2).max()
    check("NC1 3^4 Q doublet, eps 0.3: GW, g5-hermitian, P_hat_- projector, D P_hat_- = P_+ D", max(gw, gh, r_pr, r_sp) < 1e-12,
          f"GW {gw:.0e}, herm {gh:.0e}, split {r_sp:.0e}, gap {gap:.3f}")
    d0 = dens(sign_diag(build_H(L3, links_of(L3, 2, 0.0, eps0, A3, B3), 2), 2)[0], 2)
    dm = dens(sign_diag(build_H(L3, links_of(L3, 2, -1 / 6, eps0, A3, B3), 2), 2)[0], 2); dp = dens(Sxx, 2)
    z0 = max(np.abs(d0[k]).max() for k in range(3)); oddY = max(np.abs(dp[k] + dm[k]).max() for k in range(3))
    evY = np.abs(dp['Y'] - dm['Y']).max(); sz = max(np.abs(dp[k]).max() for k in range(3))
    check("NC2 pseudo-reality: Y=0 doublet SU(2) density 0 at every site; tr(T g5 D) Y-odd, tr(g5 D) Y-even",
          z0 < 1e-12 and oddY < 1e-12 and evY < 1e-12 and sz > 1e-5, f"Y=0 {z0:.0e}; odd {oddY:.0e}, even {evY:.0e}; size {sz:.1e}")
    V0 = v[:, sg > 0].copy(); del v
    ub = np.kron(np.eye(n // 4), np.linalg.eigh(G5)[1][:, 2:])
    def argW(gd):
        Pe = gd[:, None] * Ph * gd.conj()[None, :]; M = V0.conj().T @ Pe @ V0; wm, um = np.linalg.eigh(M)
        ve = Pe @ (V0 @ ((um * wm ** -0.5) @ um.conj().T)); del Pe
        return np.angle(np.linalg.slogdet(ub.conj().T @ ((gd[:, None] * D * gd.conj()[None, :]) @ ve))[0])
    rr = []; h = 1e-4; diagS = np.real(np.diag(S)); del S
    for gen in (I2 / 6, SIG[2] / 2):
        od = np.repeat((om[:, None] * np.real(np.diag(gen))[None, :]).reshape(-1), 4)
        fd = np.angle(np.exp(1j * (argW(np.exp(1j * h * od)) - argW(np.exp(-1j * h * od))))) / (2 * h)
        rr.append((fd, -0.5 * float(diagS @ od)))
    check("ND1 fixed-basis Weyl phase: d arg W/d eps = -(1/2) sum omega tr(T g5 D) (U(1)_Y, SU(2))",
          all(abs(a - b) < 1e-6 * max(1, abs(b)) for a, b in rr), "; ".join(f"{a:.3e} vs {b:.3e}" for a, b in rr))
section_N()

# ================================================================ C. SU(3) x SU(2) x U(1)_Y (overlap-colour checks, 3^4)
def section_C():
    rng = np.random.default_rng(20261023)
    GM = np.zeros((8, 3, 3), complex)
    for k, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
        GM[[0, 3, 5][k], i, j] = GM[[0, 3, 5][k], j, i] = 1; GM[[1, 4, 6][k], i, j] = -1j; GM[[1, 4, 6][k], j, i] = 1j
    GM[2] = np.diag([1, -1, 0]); GM[7] = np.diag([1, 1, -2]) / np.sqrt(3); T3c = GM / 2
    def hexp(M, eps): w, v = np.linalg.eigh(M); return np.einsum('xij,xj,xkj->xik', v, np.exp(1j * eps * w), v.conj())
    FLD = {'Q': ('3', 2, Fr(1, 6)), 'u': ('3b', 1, Fr(-2, 3)), 'd': ('3b', 1, Fr(1, 3)), 'L': ('1', 2, Fr(-1, 2)),
           'e': ('1', 1, Fr(1)), 'n': ('1', 1, Fr(0)), 'X': ('3', 1, Fr(-1, 3))}
    dc = lambda r: 1 if r == '1' else 3
    SETS = {'family': 'QudLen', 'lone Q': 'Q', 'no u^c': 'QdLen', 'quarks': 'Qud', '+X': 'QudLenX'}
    def coeffs(s):
        Y3 = sum(dc(FLD[f][0]) * FLD[f][1] * FLD[f][2] ** 3 for f in s)
        cY = sum(FLD[f][1] * FLD[f][2] for f in s if FLD[f][0] != '1')
        wY = sum(dc(FLD[f][0]) * FLD[f][2] for f in s if FLD[f][1] == 2)
        A3 = sum(FLD[f][1] * (1 if FLD[f][0] == '3' else -1) for f in s if FLD[f][0] != '1')
        return dict(Y3=Y3, cY=cY, wY=wY, A3=A3)
    def comp_flux(f, a, b, phi):
        cr, nw, Y = FLD[f]; ca = np.array(a, float) if cr == '3' else (-np.array(a, float) if cr == '3b' else np.zeros(1))
        wb = np.array(b, float) if nw == 2 else np.zeros(1); q = 6 * float(Y)
        fl = (ca[:, None] + wb[None, :] + q * phi).reshape(-1); fr = np.round(fl)
        return fr.astype(int), bool(np.abs(fl - fr).max() < 1e-9)
    def links_of(L, f, e3, e2, e1, A3_, A2_, B_, flux=None):
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
        lk, d = links_of(L, f, e3, e2, e1, *bg); w, v = sla.eigh(build_H(L, lk, d), overwrite_a=True, check_finite=False)
        N = L ** 4; sg = np.sign(w); vb = v.reshape(N, d, 4, -1); Sxx = np.zeros((N, d, d), complex)
        for x0 in range(0, N, 9):
            Sxx[x0:x0 + 9] = np.einsum('xasn,xbsn->xab', vb[x0:x0 + 9] * sg, vb[x0:x0 + 9].conj())
        del v, vb
        C, W = gens(f); out = {'Y': float(FLD[f][2]) * np.real(np.einsum('xaa->x', Sxx)), 'tr': np.real(np.einsum('xaa->x', Sxx))}
        out['C'] = None if C is None else np.real(np.einsum('kab,xba->kx', C, Sxx))
        out['W'] = None if W is None else np.real(np.einsum('kab,xba->kx', W, Sxx))
        return out
    def set_metric(dd, s):
        N = len(dd['Q']['Y']); y = sum(dd[f]['Y'] for f in s); c = np.zeros((8, N)); wv = np.zeros((3, N))
        for f in s:
            if dd[f]['C'] is not None: c = c + dd[f]['C']
            if dd[f]['W'] is not None: wv = wv + dd[f]['W']
        return dict(Y=np.abs(y).max(), C=np.sqrt((c ** 2).sum(0)).max(), W=np.sqrt((wv ** 2).sum(0)).max())
    L3 = 3
    bgA = (smooth(rng, L3, 8), smooth(rng, L3, 3), smooth(rng, L3, 1)[..., 0])
    bgC = (smooth(rng, L3, 8), smooth(rng, L3, 3), smooth(rng, L3, 1)[..., 0])
    print("== C. SU(3) x SU(2) x U(1)_Y (overlap-colour checks, 3^4; coefficients Y3, cY, wY, A3 as before)")
    def indices(flux, pert=0.15):
        out = {}; gaps = []
        for f in FLD:
            fl, ok = comp_flux(f, *flux); lk, d = links_of(L3, f, pert, pert, pert, *bgA, flux=flux)
            ix, g = index_of(build_H(L3, lk, d)); out[f] = (ix, -int((fl ** 2).sum())); gaps.append(g)
        return out, min(gaps)
    tA = time.time()
    for lab, flux, txt in (("CA1", ((1, -1, 0), (0, 0), 0.0), "Cartan SU(3) flux diag(1,-1,0)"),
                           ("CA2", ((1/3, 1/3, -2/3), (1/2, -1/2), 1/6), "Z6-twisted flux (1/3,1/3,-2/3),(1/2,-1/2),1/6")):
        ix, gp = indices(flux)
        ys = {nm: sum(FLD[f][2] * ix[f][0] for f in s) for nm, s in SETS.items()}
        yp = {nm: sum(FLD[f][2] * ix[f][1] for f in s) for nm, s in SETS.items()}
        ok = all(ix[f][0] == ix[f][1] for f in FLD) and ys == yp and ys['family'] == 0 and all((ys[nm] != 0) == (yp[nm] != 0) for nm in SETS)
        check(f"{lab} {txt} x random pert: every index = -sum f^2; family sum Y idx = 0; contrasts = charge prediction", ok,
              "idx " + ",".join(f"{f}{ix[f][0]}" for f in FLD) + "; sumY " + ", ".join(f"{nm} {ys[nm]}" for nm in SETS) + f"; gap {gp:.3f}")
    idx1 = {}
    for fq in (-1, 0, 1):
        lk, _ = links_of(L3, 'e', 0, 0, 0, *bgA, flux=((0, 0, 0), (0, 0), fq / 6)); idx1[fq] = index_of(build_H(L3, lk, 1))[0]
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
        res3[("A1", 'no u^c')][0] != 0 and res3[("A1", '+X')][0] != 0 and res3[("A2", 'quarks')][1] != 0
    check("CA3 component idx(f) = -f^2; colour- and T3-weighted integrated anomalies 0 for family, not for no-u^c/+X/quarks", ok3,
          f"idx {idx1}; " + "; ".join(f"{l} {nm}: {res3[(l, nm)][0]:+.0f},{res3[(l, nm)][1]:+.1f}" for l in ("A1", "A2") for nm in ('family', 'no u^c', 'quarks', '+X')))
    adm = all(comp_flux(f, (1/3, 1/3, -2/3), (1/2, -1/2), 1/6)[1] for f in FLD)
    FLD['X0'] = ('3', 1, Fr(0)); FLD['D0'] = ('1', 2, Fr(0)); FLD['T2'] = ('3', 1, Fr(2, 3))
    adm2 = {f: comp_flux(f, (1/3, 1/3, -2/3), (1/2, -1/2), 1/6)[1] for f in ('X0', 'D0', 'T2')}
    check("CA4 Z6 global form: all 16 fields and X admissible; (3,1,0), (1,2,0) not, (3,1,2/3) yes",
          adm and adm2 == {'X0': False, 'D0': False, 'T2': True}, f"A {time.time() - tA:.0f}s")
    for k in ('X0', 'D0', 'T2'): del FLD[k]
    tB = time.time()
    dd3 = {f: field_dens(L3, f, 0.3, 0, 0, bgC) for f in 'QudX'}
    rC = max(np.abs(dd3['u']['C'] + dd3['Q']['C'] / 2).max(), np.abs(dd3['u']['tr'] - dd3['X']['tr']).max())
    m3 = {nm: set_metric({**dd3, **{f: dict(Y=0 * dd3['Q']['Y'], C=None, W=None) for f in 'Len'}}, s) for nm, s in SETS.items()}
    check("CB1 pure SU(3) eps 0.3: lattice C exact; family C and Y densities 0 at every site; no u^c, +X fail; quarks pass Y",
          rC < 1e-12 and m3['family']['C'] < 1e-12 and m3['family']['Y'] < 1e-12 and m3['quarks']['Y'] < 1e-12 and
          min(m3['no u^c']['C'], m3['no u^c']['Y'], m3['+X']['C'], m3['+X']['Y']) > 1e-5,
          f"C-rel {rC:.0e}; family {m3['family']['C']:.0e}/{m3['family']['Y']:.0e}; no u^c {m3['no u^c']['C']:.1e}/{m3['no u^c']['Y']:.1e}; +X {m3['+X']['C']:.1e}")
    dd2 = {f: field_dens(L3, f, 0, 0.3, 0, bgC) for f in 'QL'}
    zero = {f: dict(Y=0 * dd2['Q']['Y'], C=None, W=None) for f in 'udenX'}
    m2 = {nm: set_metric({**dd2, **zero}, s) for nm, s in SETS.items()}
    check("CB2 pure SU(2) eps 0.3: family Y-weighted density 0 at every site; quarks alone fail",
          m2['family']['Y'] < 1e-12 and m2['quarks']['Y'] > 1e-5 and m2['family']['W'] < 1e-12,
          f"family {m2['family']['Y']:.0e}/{m2['family']['W']:.0e}; quarks {m2['quarks']['Y']:.1e}; {time.time() - tB:.0f}s")
    epss = [0.2, 0.1, 0.05]; eY = {}
    for e in epss:
        for f in FLD: eY[(e, f)] = field_dens(L3, 'e', 0, 0, e * float(FLD[f][2]), bgC)['tr']
    tab1 = {nm: [np.abs(sum(dc(FLD[f][0]) * FLD[f][1] * float(FLD[f][2]) * eY[(e, f)] for f in s)).max() for e in epss] for nm, s in SETS.items()}
    sl1 = {nm: np.polyfit(np.log(epss), np.log(v), 1)[0] for nm, v in tab1.items()}
    check("CB3 pure U(1)_Y scan: family ~ eps^4 (|s-4|<0.4), lone Q and quarks ~ eps^2 (|s-2|<0.3)",
          abs(sl1['family'] - 4) < 0.4 and abs(sl1['lone Q'] - 2) < 0.3 and abs(sl1['quarks'] - 2) < 0.3,
          ", ".join(f"{nm} {sl1[nm]:.2f}" for nm in SETS))
    tC = time.time(); tabs = []
    for e in epss:
        dd = {f: field_dens(L3, f, e, e, e, bgC) for f in FLD}; tabs.append({nm: set_metric(dd, s) for nm, s in SETS.items()}); del dd
    pred = {}
    for nm, s in SETS.items():
        k = coeffs(s); pred[nm] = dict(Y=any(k[c] != 0 for c in ('Y3', 'cY', 'wY')), C=any(k[c] != 0 for c in ('A3', 'cY')), W=k['wY'] != 0)
    sl = {(nm, dr): np.polyfit(np.log(epss), np.log([t[nm][dr] for t in tabs]), 1)[0] for nm in SETS for dr in 'YCW'}
    agree = lambda nm, dr: abs(sl[(nm, dr)] - 2) < 0.3 if pred[nm][dr] else sl[(nm, dr)] >= 2.7
    fmt = lambda nm: " ".join(f"{dr}{'x' if pred[nm][dr] else 'o'}{sl[(nm, dr)]:.2f}" for dr in 'YCW')
    check("CC1 generic background scan: family cancels (s >= 2.7) in Y, SU(3), SU(2); lone Q ~ eps^2 in all three",
          all(agree(nm, dr) for nm in ('family', 'lone Q') for dr in 'YCW'), f"family {fmt('family')}; lone Q {fmt('lone Q')} (x anomalous, o cancel)")
    check("CC2 contrasts as charge sums predict: no u^c fails Y,SU(3); quarks fail Y,SU(2), pass SU(3); +X fails Y,SU(3)",
          all(agree(nm, dr) for nm in ('no u^c', 'quarks', '+X') for dr in 'YCW'), "; ".join(f"{nm} {fmt(nm)}" for nm in ('no u^c', 'quarks', '+X')))
    r = {dr: tabs[-1]['family'][dr] / tabs[-1]['lone Q'][dr] for dr in 'YCW'}
    print(f"   family/lone Q at eps=0.05: Y {r['Y']:.1e} C {r['C']:.1e} W {r['W']:.1e}; {time.time() - tC:.0f}s")
    lk, d = links_of(L3, 'u', 0.3, 0.3, 0.3, *bgC); H = build_H(L3, lk, d); n = H.shape[0]
    w, v = np.linalg.eigh(H); del H; S = (v * np.sign(w)) @ v.conj().T; del v
    g5b = np.kron(np.eye(n // 4), G5); D = np.eye(n) + g5b @ S
    gw = np.abs(g5b @ D + D @ g5b - D @ g5b @ D).max(); gh = np.abs(g5b @ D @ g5b - D.conj().T).max()
    Ph = (np.eye(n) + S) / 2; rp = max(np.abs(Ph @ Ph - Ph).max(), np.abs(D @ Ph - (D + g5b @ D) / 2).max())
    check("CD1 u^c antitriplet, generic SU(3)xU(1), 3^4: GW, g5-hermitian, P_hat projector exact", max(gw, gh, rp) < 1e-12,
          f"GW {gw:.0e}, herm {gh:.0e}, proj {rp:.0e}, gap {np.abs(w).min():.3f}")
section_C()
print("Supplied: groups, the 16's content and hypercharges, the Z2 / Z6 global forms, backgrounds, m0 (resolution). Finite "
      "diagnostic on 3^4, 4^4, 5^4 (singlets); not a non-perturbative proof.")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
