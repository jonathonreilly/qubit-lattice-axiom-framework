"""OBS-3 copy of OBS-2 yuk_lv.py with range-2 symbols g_c^2 added (only SYMS, gsym and the output name changed)."""
"""OBS-2: one-loop Yukawa (Higgs-exchange) self-energy on X2's walker carrier (PREREG.md, Model).
Dirac embedding (OBS-1): Psi = (psi_1, chi_2), H(k) = tau_z sigma.s(k) + tau_x m(k), s_a = sin k_a,
m(k) = m0 + Delta f_NN(k) [+ mu g(k) in strain modes], E = sqrt(s^2 + m^2).
Scalar: real NN lattice scalar, Om(q)^2 = sum 4 sin^2(q_a/2) + mH^2, field phi = sum (a + a^dag)/sqrt(2 Om).
Vertex: Gam(p,k) = tau_x Y(p,k), Y = sum_s y_s Yhat_s; variants 'sym' [g(p)+g(k)]/2, 'int' g(k), 'ext' g(p);
symbols g_0 = 1, g_c = (1 - cos k_c)/2 (= 1 at hw1 corner e_c, 0 at the other two hw1 corners).
Second-order (Brillouin-Wigner, T=0) self-energy for one added fermion:
  Sigma(w,p) = sum_k w_k sum_n Gam P_n(k) Gam / (2 Om) [theta(e_n)/(w - e_n - Om) + theta(-e_n)/(w - e_n + Om)]
  => Sigma0(p) = -sum_k w_k Gam M(k) Gam,  M = H/(2 E Om (E+Om));  Sigma1 = dSigma/dw = -sum_k w_k Gam Gam/(2 Om (E+Om)^2).
psi_1 block: (tau_x M tau_x)_11 = M_22 = -sigma.s(k)/(2 E Om (E+Om))  =>  b_a(p) = sum_k w Y^2 s_a(k)/(2 E Om (E+Om)),
             Sigma1_11 = -sum_k w Y^2/(2 Om (E+Om)^2);   mass part Sigma0_12 = -sum_k w Y^2 m(k)/(2 E Om (E+Om)).
Velocity at corner c along a: v_a = (v_tree,a + d_a b_a)/(1 - Sigma1) ~ 1 + B_a + Sigma1, B_a = d_a b_a / v_tree,a.
Grid (OBS-1): scalar momentum per axis q = u|u|/pi, u midpoint grid, weight Jacobian/N^3; k = p - q.
Strain (SF, first-order map): k_a -> k_a + (t/2) sum_b h_ab p_b(k), p = grad(E^2/2): walker p_b = sin k_b cos k_b,
scalar p_b = sin q_b; mass and Yukawa symbols flow with the fermion flow (FB1).
Modes:  kin N m0 Delta     -> I_ss'(corner) tables (B matrix, Sigma1) for corners x,y,z (and origin), 3 variants
        strain N m0 Delta  -> mass-part responses at e_x to E_g and T2g strains (symmetry check)
        off N m0 Delta     -> vertex correction to an hw2 (pi,pi,0) condensate B in {tau_x, tau_x sigma_z}, strains"""
import numpy as np, sys, time, json
t0 = time.time()
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
TZS = [np.kron(sz, S) for S in SIG]; TX = np.kron(sx, s0); I4 = np.eye(4)
CORN = {'x': np.array([np.pi, 0, 0]), 'y': np.array([0, np.pi, 0]), 'z': np.array([0, 0, np.pi]), 'o': np.zeros(3)}
SYMS = ['0', 'x', 'y', 'z', 'X', 'Y', 'Z']   # OBS-3: X,Y,Z = g_c^2 (range 2)

def grid(N):
    u = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    return u * np.abs(u) / np.pi, 2 * np.abs(u) / np.pi

def gsym(s, k):
    if s == '0':
        return np.ones_like(k[0])
    if s in 'XYZ':
        return ((1 - np.cos(k['XYZ'.index(s)])) / 2)**2
    return (1 - np.cos(k['xyz'.index(s)])) / 2

def flow_f(k, h, t):   # walker SF flow, first order
    pb = [np.sin(k[b]) * np.cos(k[b]) for b in range(3)]
    return [k[a] + 0.5 * t * sum(h[a][b] * pb[b] for b in range(3)) for a in range(3)]

def flow_s(q, h, t):   # NN scalar SF flow, first order
    pb = [np.sin(q[b]) for b in range(3)]
    return [q[a] + 0.5 * t * sum(h[a][b] * pb[b] for b in range(3)) for a in range(3)]

def slab_iter(p, N, h=None, t=0.0, qoff=(0.0, 0.0, 0.0)):
    """yield per-slab arrays: weights, flowed k, flowed p (scalars), Om"""
    qg, jac = grid(N)
    qy, qz = np.meshgrid(qg, qg, indexing='ij'); jyz = np.outer(jac, jac).ravel(); qy = qy.ravel(); qz = qz.ravel()
    for ix in range(N):
        q = [np.full(qy.shape, qg[ix]) + qoff[0], qy + qoff[1], qz + qoff[2]]; w = jac[ix] * jyz / N**3
        k = [p[a] - q[a] for a in range(3)]
        if h is not None and t != 0.0:
            kf = flow_f(k, h, t); qf = flow_s(q, h, t); pf = flow_f([np.array(p[a]) for a in range(3)], h, t)
        else:
            kf, qf, pf = k, q, [np.array(p[a]) for a in range(3)]
        yield w, kf, qf, pf

def kin(N, m0, Delta, mH, dq=1e-3):
    """returns dict[corner][variant] -> {'B': 3x3 per pair, 'S1': per pair}"""
    pairs = [(a, b) for i, a in enumerate(SYMS) for b in SYMS[i:]]
    out = {}
    for cname in ('x', 'y', 'z', 'o'):
        e = CORN[cname]
        pts = [('c', e)] + [(f'{a}{sg}', e + sg * dq * np.eye(3)[a]) for a in range(3) for sg in (+1, -1)]
        acc = {}
        for lab, p in pts:
            res = {v: {pr: np.zeros(4) for pr in pairs} for v in ('sym', 'int', 'ext')}
            for w, k, q, pp in slab_iter(p, N):
                Om = np.sqrt(sum(4 * np.sin(q[a] / 2)**2 for a in range(3)) + mH**2)
                s = [np.sin(k[a]) for a in range(3)]
                m = m0 + Delta * (1 - sum(np.cos(k[a]) for a in range(3))) / 2
                E = np.sqrt(sum(x**2 for x in s) + m**2)
                Fb = [w * s[a] / (2 * E * Om * (E + Om)) for a in range(3)]
                Fz = -w / (2 * Om * (E + Om)**2)
                gk = {sy_: gsym(sy_, k) for sy_ in SYMS}; gp = {sy_: float(gsym(sy_, [np.array(pp[a]) for a in range(3)])) for sy_ in SYMS}
                Yv = {'sym': {sy_: (gk[sy_] + gp[sy_]) / 2 for sy_ in SYMS}, 'int': gk, 'ext': {sy_: np.full(gk['0'].shape, gp[sy_]) for sy_ in SYMS}}
                for v in Yv:
                    for (a_, b_) in pairs:
                        YY = Yv[v][a_] * Yv[v][b_]
                        r = res[v][(a_, b_)]
                        r[0] += (YY * Fb[0]).sum(); r[1] += (YY * Fb[1]).sum(); r[2] += (YY * Fb[2]).sum(); r[3] += (YY * Fz).sum()
            acc[lab] = res
        vt = np.cos(e)   # tree velocity per axis at the corner (+-1)
        out[cname] = {}
        for v in ('sym', 'int', 'ext'):
            out[cname][v] = {}
            for pr in pairs:
                D = np.zeros((3, 3))   # D[a, b] = d b_a / d q_b
                for b in range(3):
                    D[:, b] = (acc[f'{b}{+1}'][v][pr][:3] - acc[f'{b}{-1}'][v][pr][:3]) / (2 * dq)
                Bd = np.array([D[a, a] / vt[a] for a in range(3)])
                out[cname][v]['%s%s' % pr] = {'B': Bd.tolist(), 'offdiag': float(np.abs(D - np.diag(np.diag(D))).max()), 'S1': float(acc['c'][v][pr][3]),
                                             'b_at_corner': acc['c'][v][pr][:3].tolist()}
        print(f"  corner {cname} done ({time.time()-t0:.0f}s)", flush=True)
    return out

def strain(N, m0, Delta, mH, t=0.02):
    """mass-part responses at e_x: on-site vertex, internal mass m0 + Delta f_NN + mu g_z (leak of g_z into e_x),
    and own-corner (g_x at e_x); returns d/dt for strains xx, yy, zz, xy, yz, zx."""
    mu = 0.05
    hs = {}
    for lab, (a, b) in (('xx', (0, 0)), ('yy', (1, 1)), ('zz', (2, 2)), ('xy', (0, 1)), ('yz', (1, 2)), ('zx', (2, 0))):
        h = np.zeros((3, 3)); h[a, b] = 1; h[b, a] = 1
        hs[lab] = h
    p = CORN['x']
    def masspart(h, tt, musym, muval, vert):
        tot = 0.0
        for w, k, q, pp in slab_iter(p, N, h, tt):
            Om = np.sqrt(sum(4 * np.sin(q[a] / 2)**2 for a in range(3)) + mH**2)
            s = [np.sin(k[a]) for a in range(3)]
            m = m0 + Delta * (1 - sum(np.cos(k[a]) for a in range(3))) / 2 + muval * gsym(musym, k)
            E = np.sqrt(sum(x**2 for x in s) + m**2)
            gp = float(gsym(vert, [np.array(pp[a]) for a in range(3)]))
            Y = (gsym(vert, k) + gp) / 2
            tot += (-w * Y * Y * m / (2 * E * Om * (E + Om))).sum()
        return tot
    res = {}
    for name, musym, vert in (('leak_gz_onsiteY', 'z', '0'), ('own_gx_onsiteY', 'x', '0'), ('leak_gz_selYz', 'z', 'z'), ('onsite_m0_selYy', '0', 'y')):
        d = {}
        for lab, h in hs.items():
            vals = []
            for tt in (t, -t):
                if musym == '0':
                    vals.append(masspart(h, tt, 'x', 0.0, vert) / m0)
                else:
                    vals.append((masspart(h, tt, musym, mu, vert) - masspart(h, tt, musym, 0.0, vert)) / mu)
            d[lab] = (vals[0] - vals[1]) / (2 * t)
        base = (masspart(None, 0.0, musym if musym != '0' else 'x', mu if musym != '0' else 0.0, vert) - (masspart(None, 0.0, musym, 0.0, vert) if musym != '0' else 0.0)) / (mu if musym != '0' else m0)
        res[name] = {'base': base, 'd': d}
        print(f"  {name}: base {base:+.6e}  " + "  ".join(f"{l} {v:+.3e}" for l, v in d.items()) + f"  ({time.time()-t0:.0f}s)", flush=True)
    return res

def offd(N, m0, Delta, mH, t=0.02):
    """vertex correction (on-site Yukawa, real scalar) to an hw2 condensate sum_k Psi^dag(k) B Psi(k+Q), Q=(pi,pi,0),
    at p = e_x (p + Q = e_y). Sigma_off = + sum_k w sum_nn' J(e_n(k), e_n'(k+Q)) tau_x P_n(k) B P_n'(k+Q) tau_x,
    J(E1,E2) = [I(E1) - I(E2)]/(E2 - E1), I(E) = sgn E / (2 Om (|E| + Om))  (OBS-1 r1_offdiag.py with photon -> scalar)."""
    Q = np.array([np.pi, np.pi, 0.0]); p = CORN['x']
    Bs = {'tau_x': TX, 'tau_x.sigma_z': np.kron(sx, sz), 'tau_x.sigma_x': np.kron(sx, sx)}
    hs = {'0': None}
    for lab, (a, b) in (('xx', (0, 0)), ('yy', (1, 1)), ('zz', (2, 2)), ('xy', (0, 1)), ('yz', (1, 2)), ('zx', (2, 0))):
        h = np.zeros((3, 3)); h[a, b] = 1; h[b, a] = 1; hs[lab] = h
    def Hk(k):
        s = [np.sin(k[a]) for a in range(3)]
        m = m0 + Delta * (1 - sum(np.cos(k[a]) for a in range(3))) / 2
        H = sum(s[a][:, None, None] * TZS[a] for a in range(3)) + m[:, None, None] * TX
        E = np.sqrt(sum(x**2 for x in s) + m**2)
        Hn = H / E[:, None, None]
        return E, [(I4 + Hn) / 2, (I4 - Hn) / 2]
    def one(B, h, tt):
        S = np.zeros((4, 4), complex)
        for w, k, q, pp in slab_iter(p, N, h, tt):
            kQ0 = [p[a] - q[a] + Q[a] for a in range(3)]   # unflowed k + Q, then flow
            kQ = flow_f(kQ0, h, tt) if (h is not None and tt != 0) else kQ0
            Om = np.sqrt(sum(4 * np.sin(q[a] / 2)**2 for a in range(3)) + mH**2)
            E1, P1 = Hk(k); E2, P2 = Hk(kQ)
            I = lambda E: np.sign(E) / (2 * Om * (np.abs(E) + Om))
            for s1, e1 in ((0, E1), (1, -E1)):
                for s2, e2 in ((0, E2), (1, -E2)):
                    diff = e2 - e1
                    J = np.where(np.abs(diff) > 1e-9, (I(e1) - I(e2)) / np.where(np.abs(diff) > 1e-9, diff, 1.0), 1 / (2 * Om * (np.abs(e1) + Om)**2))
                    S += np.einsum('p,pij->ij', w * J, TX @ (P1[s1] @ B @ P2[s2]) @ TX)
        return S
    res = {}
    for bname, B in Bs.items():
        d = {}
        S0 = one(B, None, 0.0); c0 = np.trace(B.conj().T @ S0) / 4
        other0 = np.abs(S0 - c0 * B).max()
        for lab, h in hs.items():
            if h is None:
                continue
            Sp = one(B, h, t); Sm = one(B, h, -t)
            dS = (Sp - Sm) / (2 * t)
            d[lab] = {'own': complex(np.trace(B.conj().T @ dS) / 4), 'other_max': float(np.abs(dS - (np.trace(B.conj().T @ dS) / 4) * B).max())}
        res[bname] = {'coef0': complex(c0), 'other0': float(other0), 'd': d}
        print(f"  B={bname}: Sigma_off coef {c0:.6e} (other comps {other0:.1e}); strain d/dt own-coef: " +
              "  ".join(f"{l} {v['own'].real:+.3e}{v['own'].imag:+.1e}i (oth {v['other_max']:.1e})" for l, v in d.items()) + f"  ({time.time()-t0:.0f}s)", flush=True)
    return res


def flav(N, m0, Delta, mH, dq=1e-3):
    """comparator M2: off-diagonal flavour coupling carried by a scalar light at Q_ab (Om^2 = sum 4 sin^2((q-Q)/2) + mH^2),
    on-site vertex tau_x (x) Gam_spin with Gam_spin in {1 (spin-blind), sigma_c (c = third axis; Lorentz-covariant)}.
    psi_1 block: sigma_c (sigma.s) sigma_c = sum_a eta_a sigma_a s_a, eta_a = +1 (a = c), -1 (a != c).
    Corner e_x; Q_xy (internal k ~ e_y, c = z) and Q_xz (internal k ~ e_z, c = y)."""
    out = {}
    for qn, Qv, c in (('Qxy', np.array([np.pi, np.pi, 0.0]), 2), ('Qxz', np.array([np.pi, 0.0, np.pi]), 1)):
        e = CORN['x']
        pts = [('c', e)] + [(f'{a}{sg}', e + sg * dq * np.eye(3)[a]) for a in range(3) for sg in (+1, -1)]
        acc = {}
        for lab, p in pts:
            r = np.zeros(4)
            for w, k, q, pp in slab_iter(p, N, qoff=Qv):   # grid clustered at the flavon's light point Q (v2)
                Om = np.sqrt(sum(4 * np.sin((q[a] - Qv[a]) / 2)**2 for a in range(3)) + mH**2)
                s = [np.sin(k[a]) for a in range(3)]
                m = m0 + Delta * (1 - sum(np.cos(k[a]) for a in range(3))) / 2
                E = np.sqrt(sum(x**2 for x in s) + m**2)
                for a in range(3):
                    r[a] += (w * s[a] / (2 * E * Om * (E + Om))).sum()
                r[3] += (-w / (2 * Om * (E + Om)**2)).sum()
            acc[lab] = r
        vt = np.cos(e)
        for gname in ('blind', 'sigma_c'):
            eta = np.ones(3) if gname == 'blind' else np.array([1.0 if a == c else -1.0 for a in range(3)])
            D = np.zeros((3, 3))
            for b in range(3):
                D[:, b] = eta * (acc[f'{b}{+1}'][:3] - acc[f'{b}{-1}'][:3]) / (2 * dq)
            Bd = np.array([D[a, a] / vt[a] for a in range(3)])
            out[f'{qn}_{gname}'] = {'B': Bd.tolist(), 'S1': float(acc['c'][3]), 'dv': (Bd + acc['c'][3]).tolist(),
                                    'offdiag': float(np.abs(D - np.diag(np.diag(D))).max())}
            print(f"  {qn} {gname:7s}: dv = {Bd + acc['c'][3]} (S1 {acc['c'][3]:+.4e})  ({time.time()-t0:.0f}s)", flush=True)
    return out

if __name__ == '__main__':
    mode = sys.argv[1]; N = int(sys.argv[2]); m0 = float(sys.argv[3]); Delta = float(sys.argv[4])
    mH = float(sys.argv[5]) if len(sys.argv) > 5 else m0
    print(f"mode={mode} N={N} m0={m0} Delta={Delta} mH={mH}", flush=True)
    if mode == 'kin':
        r = kin(N, m0, Delta, mH)
    elif mode == 'strain':
        r = strain(N, m0, Delta, mH)
    elif mode == 'flav':
        r = flav(N, m0, Delta, mH)
    else:
        r = offd(N, m0, Delta, mH)
    fn = f"tables/yuk3_{mode}_N{N}_m{m0}_D{Delta}_mH{mH}.json"
    json.dump(r, open(fn, 'w'), default=lambda z: [z.real, z.imag] if isinstance(z, complex) else str(z), indent=0)
    print(f"saved {fn} ({time.time()-t0:.0f}s)", flush=True)
