"""OBS-2 assembly. Part A: flavour-pattern Yukawa LV residuals per mass eigenstate (model M1, yuk_kin_N96_*.json) vs SME bounds
(Kostelecky-Russell 0801.0287v19 tables, rows cited in BOUNDS). Part B: FLAV2 clock row = OBS-1 E_g (+ covariant-condensate variant)
+ T2g (zero at first order: strain_*.out, offd_*.out). Mass/mixing inputs and the clock estimator copied from OBS-1 sizes.py (unchanged)."""
import json, itertools, numpy as np
np.set_printoptions(precision=3)
P = print
SY = ['0', 'x', 'y', 'z']; CI = {'x': 0, 'y': 1, 'z': 2}
def key(a, b): return a + b if SY.index(a) <= SY.index(b) else b + a
def loadI(N, m, D, var):
    r = json.load(open(f"yuk_kin_N{N}_m{m}_D{D}_mH{m}.json"))
    I = {c: {k: np.array(v[var][k]['B']) + v[var][k]['S1'] for k in v[var]} for c, v in r.items() if c in 'xyz'}
    # impose exact C3[111] covariance (checked to <= 8e-15 abs in ana_kin.out) to remove roundoff from exactly symmetric sectors
    Pm = {'0': '0', 'x': 'y', 'y': 'z', 'z': 'x'}; Pc = {'x': 'y', 'y': 'z', 'z': 'x'}; ax = [1, 2, 0]
    out = {c: {} for c in 'xyz'}
    for c in 'xyz':
        for k in I[c]:
            a, b = k[0], k[1]; acc = np.zeros(3); cc, aa, bb = c, a, b; perm = np.arange(3)
            for g in range(3):
                acc += I[cc][key(aa, bb)][perm]
                cc, aa, bb = Pc[cc], Pm[aa], Pm[bb]; perm = np.array([ax[i] for i in perm])
            out[c][k] = acc / 3
    return out
# ---------------- inputs copied from OBS-1 sizes.py:42-53 (RECALLED PDG/NuFIT central values)
def rot(t12, t23, t13, d):
    s12, c12, s23, c23, s13, c13 = np.sin(t12), np.cos(t12), np.sin(t23), np.cos(t23), np.sin(t13), np.cos(t13); e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e], [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
deg = np.pi / 180
VCKM = rot(13.04 * deg, 2.38 * deg, 0.201 * deg, 1.20); UPMNS = rot(33.4 * deg, 49.0 * deg, 8.57 * deg, 197 * deg)
w3 = np.exp(2j * np.pi / 3); F = np.array([[w3**(c * j) for j in range(3)] for c in range(3)]) / np.sqrt(3)
mu_q = np.array([2.16e-3, 1.27, 172.69]); md_q = np.array([4.67e-3, 0.0934, 4.18]); me_l = np.array([0.511e-3, 0.10566, 1.77686])
mnu = np.array([0.0, 8.6e-12, 5.0e-11])     # GeV, normal ordering, lightest 0 (RECALLED)
v = 174.1
branches = {'A': (np.eye(3), VCKM, np.eye(3), UPMNS), 'B': (F, F @ VCKM, F, F @ UPMNS), "B'": (F, F @ VCKM, F @ UPMNS.conj().T, F)}
# ---------------- SME bounds (dimensionless c; Table D6/D28/D30/D44, D11/D15 via suggested parton mapping) -- (iso_neg, iso_pos, aniso, label)
BOUNDS = {
 'e':   (5e-21, 2e-15, 2e-20, "D6: cTT > -5e-21 (astro [72]*), cTT (-4 to 2)e-15 (collider [83]*); c_{X-Y},c_XY,c_XZ,c_YZ ~(5-9)e-21 1sigma (trapped Yb+ [64])"),
 'mu':  (4.2e-15, 8.3e-15, 1e-11, "D28: c00 (-4.2 to 8.3)e-15 (combined [63]*); |c| < 1e-11 (astro [90]*)"),
 'tau': (1.2e-9, 1.2e-9, 1e-8, "D30: |c_tau - c_gamma| < 1.2e-9 (astro [67]*); |c| < 1e-8 (astro [90]*)"),
 'u':   (1e-22, 1.4e-2, 1e-28, "D44 p3: cTT^u > -1e-22 (astro [100]*[22]*[325]*); p2: cTT^u (-4.3 to 1.4)e-2 (Drell-Yan [322]*); aniso: nucleon comagnetometer ~1e-29 (D15 [115], D11 [115][116]) /~0.3 parton fraction (SUGGESTED mapping); direct DIS 3e-4 (D44 p1 [321])"),
 'd':   (1e-22, 6.6e-1, 1e-28, "D44 p3: cTT^d > -1e-22 (astro); p2: cTT^d < 0.66 (Drell-Yan [322]*); aniso: nucleon-mapped ~1e-28 (SUGGESTED); direct DIS 1e-3 (D44 p1)"),
 's':   (1e-9, 1e-9, 1e-9, "D44 p4: |c_K| < 1e-9 (astro [90]*; meson -> valence quark mapping SUGGESTED); direct DIS ~2e-3 (D44 p1)"),
 'c':   (1e-8, 1e-8, 1e-8, "D44 p4: |c_D| < 1e-8 (astro [90]*; mapping SUGGESTED); direct cTT^c (-4.5 to 1.5)e-1 (DY [322]*)"),
 'b':   (1e-7, 1e-7, 1e-7, "D44 p4: |c_Bd|,|c_Bs| < 1e-7 (astro [90]*; mapping SUGGESTED); direct c^b_ZZ < 0.35 ([330]*)"),
 't':   (1.6e-7, 1.6e-7, 1.6e-7, "D44 p4: |c^t| < 1.6e-7 (astro [67]*); c^t_munu < 1e-4 ([326]*); (c_Q)_33 ~1e-3 (ttbar [332])"),
}
NAMES = {'u': ('u', 'c', 't'), 'd': ('d', 's', 'b'), 'e': ('e', 'mu', 'tau')}

def yukawas(U, m, split, scale):
    M = U @ np.diag(m) @ U.conj().T
    y0 = np.trace(M).real / 3 / v if split == 'trace' else 0.0
    return {'0': y0 * scale, 'x': (M[0, 0].real / v - y0) * scale, 'y': (M[1, 1].real / v - y0) * scale, 'z': (M[2, 2].real / v - y0) * scale}
def sector_T(I, y):
    return {c: sum(y[a] * y[b] * I[c][key(a, b)] for a in SY for b in SY) for c in 'xyz'}
def split_univ(T):
    iso = np.mean([T[c].mean() for c in 'xyz'])
    tet = np.mean([T[c][CI[c]] - np.mean([T[c][a] for a in range(3) if a != CI[c]]) for c in 'xyz'])
    r = {c: T[c] - (iso + tet * (np.eye(3)[CI[c]] - 1 / 3)) for c in 'xyz'}
    return iso, tet, r
def eig_dv(U, r):
    W = np.abs(U)**2      # W[c, i]
    return [sum(W[CI[c], i] * r[c] for c in 'xyz') for i in range(3)]

def run(I, bname, split, qscale, lscale, verbose=False):
    Uu, Ud, Ue, Un = branches[bname]
    y = {'u': yukawas(Uu, mu_q, split, qscale), 'd': yukawas(Ud, md_q, split, qscale), 'e': yukawas(Ue, me_l, split, lscale), 'n': yukawas(Un, mnu, split, lscale)}
    T = {s: sector_T(I, y[s]) for s in y}
    fields = {'Q': {c: T['u'][c] + T['d'][c] for c in 'xyz'}, 'uc': {c: 2 * T['u'][c] for c in 'xyz'}, 'dc': {c: 2 * T['d'][c] for c in 'xyz'},
              'L': {c: T['e'][c] + T['n'][c] for c in 'xyz'}, 'ec': {c: 2 * T['e'][c] for c in 'xyz'}}
    sp = {f: split_univ(fields[f]) for f in fields}
    out = {}
    for sec, (Lf, Rf, U) in {'u': ('Q', 'uc', Uu), 'd': ('Q', 'dc', Ud), 'e': ('L', 'ec', Ue)}.items():
        dL = eig_dv(U, sp[Lf][2]); dR = eig_dv(U, sp[Rf][2])
        for i, nm in enumerate(NAMES[sec]):
            dvV = (dL[i] + dR[i]) / 2; dvA = (dL[i] - dR[i]) / 2
            cTT = -0.75 * dvV.mean(); dTT = -0.75 * dvA.mean()
            can = np.abs(dvV - dvV.mean()).max(); dan = np.abs(dvA - dvA.mean()).max()
            bn, bp, ba, _ = BOUNDS[nm]
            ratio_iso = max(abs(cTT), abs(dTT)) / (bn if min(cTT, dTT) < 0 and abs(min(cTT, dTT)) >= max(cTT, dTT) else bp)
            ratio_an = max(can, dan) / ba
            out[nm] = dict(cTT=cTT, dTT=dTT, can=can, dan=dan, r_iso=ratio_iso, r_an=ratio_an, cvec=-(dvV - dvV.mean()), dvec=-(dvA - dvA.mean()))
    return out, sp, y

if __name__ == '__main__':
    P("PART A. Flavour-pattern Yukawa LV residual (ii), model M1, one loop, N = 96 (N-converged to <=11% for anisotropic parts, ana_kin.out)")
    P("units: dimensionless SME c (traceless convention, v(p) = 1 - c00 - c_jk p_j p_k => dv_iso = -(4/3) cTT)")
    combos = [(m, D, var) for m in ('0.1', '0.05', '0.025') for D in ('0.0', '0.5') for var in ('sym', 'int', 'ext')]
    Is = {cb: loadI(96, *cb) for cb in combos}
    prim = ('0.025', '0.5', 'sym')
    for scl_name, qs, ls in (('low-scale y = m/v (y_t 0.99, y_b 0.024, y_tau 0.0102)', 1.0, 1.0), ('Planck-scale bracket (quark y x0.45, lepton y x1.0; RECALLED SM running)', 0.45, 1.0)):
        P(f"\n=== couplings: {scl_name}")
        for bname in ('B', 'A', "B'"):
            for split in ('trace', 'selective'):
                res_all = {cb: run(Is[cb], bname, split, qs, ls)[0] for cb in combos}
                prim_res, sp, y = run(Is[prim], bname, split, qs, ls)
                P(f" branch {bname} [{split}]  (primary m0=0.025 Delta=0.5 sym; range over m0 x Delta x vertex variant in brackets)")
                if bname == 'B' and split == 'trace' and qs == 1.0:
                    for f, (iso, tet, r) in sp.items():
                        P(f"    field {f:2s}: universal part (i): iso dv {iso:+.3e} (set C speed counterterm), tet dv_par-dv_perp {tet:+.3e} (needs 2nd cubic operator)")
                for nm in ('e', 'mu', 'tau', 'u', 'c', 't', 'd', 's', 'b'):
                    pr = prim_res[nm]
                    lo_i = min(max(abs(res_all[cb][nm]['cTT']), abs(res_all[cb][nm]['dTT'])) for cb in combos); hi_i = max(max(abs(res_all[cb][nm]['cTT']), abs(res_all[cb][nm]['dTT'])) for cb in combos)
                    lo_a = min(max(res_all[cb][nm]['can'], res_all[cb][nm]['dan']) for cb in combos); hi_a = max(max(res_all[cb][nm]['can'], res_all[cb][nm]['dan']) for cb in combos)
                    rmax = max(max(res_all[cb][nm]['r_iso'], res_all[cb][nm]['r_an']) for cb in combos); rmin = min(max(res_all[cb][nm]['r_iso'], res_all[cb][nm]['r_an']) for cb in combos)
                    flag = 'OVER' if rmin > 1 else ('over-in-some' if rmax > 1 else 'within')
                    P(f"    {nm:3s}: |cTT|,|dTT| max {max(abs(pr['cTT']), abs(pr['dTT'])):.2e} [{lo_i:.1e},{hi_i:.1e}]  aniso max {max(pr['can'], pr['dan']):.2e} [{lo_a:.1e},{hi_a:.1e}]"
                      f"  ratio to bound {max(pr['r_iso'], pr['r_an']):.1e} [{rmin:.1e},{rmax:.1e}]  {flag}   (signs: cTT {pr['cTT']:+.1e} dTT {pr['dTT']:+.1e}; c_jj {pr['cvec']}, d_jj {pr['dvec']})")
    P("\nBounds used (Kostelecky-Russell arXiv:0801.0287v19, Feb 2026):")
    for k, b in BOUNDS.items():
        P(f"   {k:3s}: iso(-) {b[0]:.1e} iso(+) {b[1]:.1e} aniso {b[2]:.1e} | {b[3]}")
