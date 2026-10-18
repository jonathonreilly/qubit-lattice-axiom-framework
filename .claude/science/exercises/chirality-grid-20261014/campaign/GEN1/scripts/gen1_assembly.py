"""GEN-1 (a1) and (b): X2' Yukawa sector and the one-loop flavour-pattern speed residual at Gamma.
Inputs and SME conventions reused from OBS-3 (obs3_core.py:5-13, 146-173).  All flavour algebra in mpmath (50 digits)
so that 1e-22-level rows are not roundoff (OBS-3 referee correction).  Kernel kappa from gen1_kernel.py JSONs.
Speed matrices per unit kernel (OBS-3 multiplicities): Q: H_u + H_d; u^c: 2 Y_u^dag Y_u; d^c: 2 Y_d^dag Y_d;
L: H_e + H_nu; e^c: 2 Y_e^dag Y_e; nu^c: 2 Y_nu^dag Y_nu.   c-ring = -(dvL + dvR)/2, d-ring = -(dvL - dvR)/2.
Variant A (PREREG literal): per-field counterterms minimise the worst ratio on the printed rows (c-ring one-sided).
Variant B (follow-up 11:40Z): c-ring rows treated two-sided at their printed magnitude."""
import sys, os, json, glob, numpy as np, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'OBS3', 'scripts'))
import obs3_core as oc
mp.mp.dps = 50
P = lambda *a: print(*a, flush=True)

def rot(t12, t23, t13, d):
    s12, c12, s23, c23, s13, c13 = mp.sin(t12), mp.cos(t12), mp.sin(t23), mp.cos(t23), mp.sin(t13), mp.cos(t13); e = mp.expj(d)
    return mp.matrix([[c12 * c13, s12 * c13, s13 / e], [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                      [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])

def ckm_wolf(lam, A, rb, eb):   # same map as obs3_core.ckm_wolfenstein, in mpmath
    lam, A, rb, eb = map(mp.mpf, (lam, A, rb, eb))
    z = A * lam**3 * (rb + 1j * eb) * mp.sqrt(1 - A**2 * lam**4) / (mp.sqrt(1 - lam**2) * (1 - A**2 * lam**4 * (rb + 1j * eb)))
    return rot(mp.asin(lam), mp.asin(A * lam**2), mp.asin(abs(z)), mp.arg(z))

deg = mp.pi / 180
V = ckm_wolf(0.22501, 0.826, 0.1591, 0.3523)              # oc.INPUTS['pdg24']['V']
UP = rot(33.4 * deg, 49.0 * deg, 8.57 * deg, 197 * deg)     # oc.U_PMNS
VEV = mp.mpf(oc.VEV)
MU = [mp.mpf(str(x)) for x in oc.INPUTS['pdg24']['mu']]; MD = [mp.mpf(str(x)) for x in oc.INPUTS['pdg24']['md']]
ME = [mp.mpf(str(x)) for x in oc.ME]; MN = [mp.mpf(str(x)) for x in oc.MNU]
BU, BD = mp.mpf('3e-23'), mp.mpf('1e-22')                   # oc.FIXED (u, d): c-ring lower bound and |d-ring| bound
dag = lambda M: M.transpose_conj()
diag = lambda v: mp.diag(v)

def haar(seed):
    r = np.random.default_rng(seed); A = r.normal(size=(3, 3)) + 1j * r.normal(size=(3, 3)); H = (A + A.conj().T) / 2
    return mp.expm(1j * mp.matrix(H.tolist()))

def build(scale, seeds):
    Wu, Xu, Xd, We, Xe, Xn = (haar(s) if s is not None else mp.eye(3) for s in seeds)
    yu = [scale * m / VEV for m in MU]; yd = [scale * m / VEV for m in MD]; ye = [scale * m / VEV for m in ME]; yn = [scale * m / VEV for m in MN]
    Wd = Wu * V; Wn = We * UP
    Y = dict(u=Wu * diag(yu) * dag(Xu), d=Wd * diag(yd) * dag(Xd), e=We * diag(ye) * dag(Xe), n=Wn * diag(yn) * dag(Xn))
    return Y, dict(Wu=Wu, Wd=Wd, Xu=Xu, Xd=Xd, We=We, Xe=Xe, Wn=Wn, Xn=Xn), dict(u=yu, d=yd, e=ye, n=yn)

def a1_check(Y, y):
    """SVD (float64) of the constructed Yukawas: masses, |V|, J vs inputs."""
    out = {}
    Yu = np.array(Y['u'].tolist(), complex); Yd = np.array(Y['d'].tolist(), complex)
    Uu, su, _ = np.linalg.svd(Yu); Ud, sd, _ = np.linalg.svd(Yd)
    Uu, su = Uu[:, ::-1], su[::-1]; Ud, sd = Ud[:, ::-1], sd[::-1]
    Vf = Uu.conj().T @ Ud; V0 = np.array(V.tolist(), complex)
    J = lambda W: (W[0, 1] * W[1, 2] * np.conj(W[0, 2]) * np.conj(W[1, 1])).imag
    out['mass_rel'] = max(max(abs(su[i] / float(y['u'][i]) - 1) for i in range(3)), max(abs(sd[i] / float(y['d'][i]) - 1) for i in range(3)))
    out['absV'] = float(np.abs(np.abs(Vf) - np.abs(V0)).max()); out['J'] = (J(Vf), J(V0))
    return out

def rows(kap, Y, B, ct, flav=None):
    """dv per eigenstate.  ct: per-field universal counterterms; flav: dict of extra covariant counterterms on Q
    {'Hu': c1, 'Hd': c2} added as c1*H_u + c2*H_d (absolute coefficients)."""
    Hu, Hd = Y['u'] * dag(Y['u']), Y['d'] * dag(Y['d'])
    TQ = kap * (Hu + Hd)
    if flav:
        TQ = TQ + flav.get('Hu', 0) * Hu + flav.get('Hd', 0) * Hd
    T = dict(Q=TQ, uc=2 * kap * dag(Y['u']) * Y['u'], dc=2 * kap * dag(Y['d']) * Y['d'],
             L=kap * (Y['e'] * dag(Y['e']) + Y['n'] * dag(Y['n'])), ec=2 * kap * dag(Y['e']) * Y['e'], nc=2 * kap * dag(Y['n']) * Y['n'])
    ev = lambda M, W: [mp.re((dag(W) * M * W)[i, i]) for i in range(3)]
    dv = dict(uL=ev(T['Q'], B['Wu']), dL=ev(T['Q'], B['Wd']), uR=ev(T['uc'], B['Xu']), dR=ev(T['dc'], B['Xd']),
              eL=ev(T['L'], B['We']), eR=ev(T['ec'], B['Xe']), nL=ev(T['L'], B['Wn']), nR=ev(T['nc'], B['Xn']))
    sub = dict(uL='Q', dL='Q', uR='uc', dR='dc', eL='L', nL='L', eR='ec', nR='nc')
    return {k: [x - ct.get(sub[k], 0) for x in v] for k, v in dv.items()}

def sme(dv, q, i=0):
    L, R = dv[q + 'L'][i], dv[q + 'R'][i]
    return -(L + R) / 2, -(L - R) / 2

def ratios_A(dv):
    r = {}
    for q, b in (('u', BU), ('d', BD)):
        c, d = sme(dv, q); r[q + '_c'] = max(mp.mpf(0), -c) / b; r[q + '_d'] = abs(d) / b
    ce, de = sme(dv, 'e'); iso = lambda x: (-x / mp.mpf('5e-21')) if x < 0 else (x / mp.mpf('2e-15'))
    r['e'] = max(iso(mp.mpf(3) / 4 * ce), iso(mp.mpf(3) / 4 * de))
    return r

def ratios_B(dv):
    r = ratios_A(dv)
    for q, b in (('u', BU), ('d', BD)):
        c, d = sme(dv, q); r[q + '_c'] = abs(c) / b
    return r

def ct_A(kap, Y, B):
    dv0 = rows(kap, Y, B, {})
    cQ = max(dv0['uL'][0], dv0['dL'][0])                    # both left speeds <= 0 (kap < 0: subluminal)
    xu, xd = dv0['uL'][0] - cQ, dv0['dL'][0] - cQ
    return dict(Q=cQ, uc=dv0['uR'][0] - xu, dc=dv0['dR'][0] - xd, L=dv0['eL'][0], ec=dv0['eR'][0], nc=dv0['nR'][0])

def ct_B(kap, Y, B, flav=None):
    dv0 = rows(kap, Y, B, {}, flav)
    a, b = dv0['uL'][0], dv0['dL'][0]; A_, B_ = 2 * BU, 2 * BD
    cQ = (a * B_ + b * A_) / (A_ + B_)
    return dict(Q=cQ, uc=dv0['uR'][0], dc=dv0['dR'][0], L=dv0['eL'][0], ec=dv0['eR'][0], nc=dv0['nR'][0])

def kappas():
    ks = []
    for fn in sorted(glob.glob(os.path.join(HERE, 'gk_N*_m*_D*_G_mH*.json'))):
        r = json.load(open(fn)); tag = os.path.basename(fn)[3:-5]
        ks.append((tag + ':onsite', r['sym']['00']['dv'][0]))
        for v in ('sym', 'int', 'ext'):
            ks.append((tag + ':Gsel_' + v, r[v]['GG']['dv'][0]))
    return ks

if __name__ == '__main__':
    KS = kappas(); kv = np.array([k for _, k in KS]); on = np.array([k for t, k in KS if 'onsite' in t])
    P(f"kernel bracket: {len(KS)} entries; on-site kappa in [{on.min():.5f}, {on.max():.5f}]; all variants in [{kv.min():.5f}, {kv.max():.5f}]")
    seedsets = {'identity bases': (None,) * 6, 'random bases #1': (1, 2, 3, 4, 5, 6), 'random bases #2': (11, 12, 13, 14, 15, 16)}
    arch = {}
    for scale_lab, scale in (('low-scale', mp.mpf(1)), ('x0.45', mp.mpf('0.45'))):
        P(f"\n===== Yukawas {scale_lab} =====")
        Y, B, y = build(scale, seedsets['random bases #1'])
        a1 = a1_check(Y, y)
        P(f"(a1) SVD of constructed Y_u, Y_d: max rel mass error {a1['mass_rel']:.1e}; max ||V|-|V_in|| {a1['absV']:.1e}; J {a1['J'][0]:.6e} vs input {a1['J'][1]:.6e}")
        for kname, kap in (('on-site max|k|', on.min()), ('on-site min|k|', on.max()), ('variant min|k|', kv.max())):
            kap = mp.mpf(kap)
            res = {}
            for bl, sd in seedsets.items():
                Yb, Bb, _ = build(scale, sd)
                dvA = rows(kap, Yb, Bb, ct_A(kap, Yb, Bb)); dvB = rows(kap, Yb, Bb, ct_B(kap, Yb, Bb))
                res[bl] = (dvA, dvB)
            dvA, dvB = res['random bases #1']
            c3 = max(abs(res[b][1][k][i] - dvB[k][i]) / max(abs(dvB[k][i]), mp.mpf('1e-300')) for b in res for k in ('uL', 'dL') for i in range(3))
            rA = ratios_A(dvA); rB = ratios_B(dvB)
            P(f"\n-- kappa = {float(kap):+.5f} ({kname})   [C3 basis independence of B rows: max rel diff {float(c3):.1e}]")
            P(f"  A (literal, printed rows): dv uL {float(dvA['uL'][0]):+.3e} uR {float(dvA['uR'][0]):+.3e} | dL {float(dvA['dL'][0]):+.3e} dR {float(dvA['dR'][0]):+.3e}"
              f" -> c-ring u {float(sme(dvA,'u')[0]):+.3e}, d {float(sme(dvA,'d')[0]):+.3e}; d-ring u {float(sme(dvA,'u')[1]):+.1e}, d {float(sme(dvA,'d')[1]):+.1e};"
              f" worst ratio {float(max(rA.values())):.2e}")
            P(f"  B (two-sided per component), per-field counterterms only: dv uL {float(dvB['uL'][0]):+.3e} dL {float(dvB['dL'][0]):+.3e};"
              f" worst ratio {float(max(rB.values())):.2e}  (rows: " + ", ".join(f"{k} {float(v):.1e}" for k, v in rB.items()) + ")")
            # flavour-covariant counterterms on Q (B convention)
            for lab, fl in (('H_u+H_d (n_min=1)', {'Hu': -kap, 'Hd': -kap}), ('H_u only', {'Hu': -kap}), ('H_d only', {'Hd': -kap}), ('H_u, H_d (n=2)', {'Hu': -kap, 'Hd': -kap})):
                Yb, Bb, _ = build(scale, seedsets['random bases #1'])
                dvf = rows(kap, Yb, Bb, ct_B(kap, Yb, Bb, fl), fl)
                P(f"     + {lab:18s}: worst B ratio {float(max(ratios_B(dvf).values())):.2e}")
            # tuning: allowed error on each flavour coefficient (relative to |kappa|), B convention, balanced split
            Hu, Hd = Y['u'] * dag(Y['u']), Y['d'] * dag(Y['d'])
            ev = lambda M, W: mp.re((dag(W) * M * W)[0, 0])
            gu = ev(Hu, B['Wd']) - ev(Hu, B['Wu']); gd = ev(Hd, B['Wd']) - ev(Hd, B['Wu'])
            tol = 2 * BU + 2 * BD
            P(f"  structure spreads (d_L - u_L): H_u {float(gu):.4e}, H_d {float(gd):.4e}, H_u+H_d {float(gu+gd):.4e}")
            P(f"  tuning (B): |dc_u|/|k| <= {float(tol/abs(gu)/abs(kap)):.1e}; |dc_d|/|k| <= {float(tol/abs(gd)/abs(kap)):.1e}; combined <= {float(tol/abs(gu+gd)/abs(kap)):.1e}")
            # heavy rows after per-field counterterm (B): flavour-pattern residual in every field (n_all inventory)
            hv = {nm: float(dvB[k][i]) for k, names in (('uL', 'uct'), ('uR', 'uct'), ('dL', 'dsb'), ('dR', 'dsb'), ('eL', 'emt'), ('eR', 'emt'), ('nL', '123'), ('nR', '123'))
                  for i, nm in enumerate([f"{k}:{c}" for c in names])}
            P("  residual dv per eigenstate after per-field counterterms (B): " + ", ".join(f"{k} {v:+.1e}" for k, v in hv.items()))
            arch[f"{scale_lab}|{kname}"] = dict(kappa=float(kap), worstA=float(max(rA.values())), worstB=float(max(rB.values())), gu=float(gu), gd=float(gd), heavy=hv)
    np.savez(os.path.join(HERE, 'gen1_assembly_archive.npz'), kappa_tags=np.array([t for t, _ in KS]), kappa_vals=kv,
             summary=np.array(json.dumps(arch)))
    P("\nsaved gen1_assembly_archive.npz")
