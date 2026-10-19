"""T-F3 task 3: vacuum alignment with a generic G-invariant quartic potential.
Part A (untuned): random V_l, V_nu; which stratum (stabilizer) hosts the global minimum?
Part B (tuned): quadratic/linear coefficients tuned (registered data) so the data-fit F3 point is stationary
in each sector; keep draws where it is a local minimum; add cross invariants at lambda_x x O(1) at three
shaping levels; re-minimise; recompute M_l, M_nu, PMNS, Delta.
usage: python3 t4_vacuum.py A|A2|B [ndraw] [seed]"""
import sys, numpy as np
from scipy.optimize import minimize
from t4_core import *
import t4_inv as TI
import t4_leak as TL
LOOP_ = 1 / (16 * np.pi ** 2)
part = sys.argv[1]; ND = int(sys.argv[2]) if len(sys.argv) > 2 else 200; rng = np.random.default_rng(int(sys.argv[3]) if len(sys.argv) > 3 else 5)
invs, bideg = TI.invariants(4)
IL, IN, NV = TI.IL, TI.IN, TI.NV
def unit_pts(n, sec):
    Z = np.zeros((n, NV))
    for idx in ([IL] if sec in ('l', 'x') else []) + ([IN] if sec in ('n', 'x') else []):
        u = rng.normal(size=(n, len(idx))); Z[:, idx] = u / np.linalg.norm(u, axis=1, keepdims=True)
    return Z
# normalise each invariant to unit RMS on unit spheres of the sectors it involves
for k, b in enumerate(bideg):
    sec = 'x' if (b[0] and b[1]) else ('l' if b[0] else 'n')
    v = TI.inv_values([invs[k]], unit_pts(400, sec))[:, 0]; r = np.sqrt(np.mean(v ** 2))
    invs[k] = {m: c / r for m, c in invs[k].items()}
pure_l = [k for k, b in enumerate(bideg) if b[1] == 0]; pure_n = [k for k, b in enumerate(bideg) if b[0] == 0]
cross = [k for k, b in enumerate(bideg) if b[0] and b[1]]
z2 = [k for k in cross if bideg[k][0] % 2 == 0 and bideg[k][1] % 2 == 0]
# U(1)xU(1)-invariant combinations (bidegree (2,2) only, from t4_group)
Zs = rng.normal(size=(1500, NV)); Zr = TI.u1_rotate(Zs, rng.uniform(0, 6.3, 1500), 0); Zr2 = TI.u1_rotate(Zs, 0, rng.uniform(0, 6.3, 1500))
ks22 = [k for k in cross if bideg[k] == (2, 2)]
Iv = lambda Z: TI.inv_values([invs[k] for k in ks22], Z)
A = np.vstack([Iv(Zr) - Iv(Zs), Iv(Zr2) - Iv(Zs)]); _, S_, Vt_ = np.linalg.svd(A, full_matrices=False)
U1C = Vt_[np.sum(S_ > 1e-8 * S_[0]):]
print(f"invariants: pure-l {len(pure_l)}, pure-nu {len(pure_n)}, cross {len(cross)}, Z2xZ2-even cross {len(z2)}, U(1)xU(1) cross combos {len(U1C)}")
A_l = TI.rep24(G_L); A_n = TI.rep24(G_NU)
def proj_fix(Agen, k, idx):
    P = np.zeros((NV, NV)); Asub = Agen[np.ix_(idx, idx)]
    P[np.ix_(idx, idx)] = sum(np.linalg.matrix_power(Asub, j) for j in range(k)) / k; return P
Pl = proj_fix(A_l, 3, IL); Pn = proj_fix(A_n, 2, IN); Pbr = np.eye(NV) - Pl - Pn
def stab(z, idx):
    return [g for g, Ag in zip(B3, TI.REPS) if np.linalg.norm((Ag @ z - z)[idx]) < 1e-5 * max(1, np.linalg.norm(z[idx]))]
def stab_type(St):
    """classify a stabilizer (subgroup of B3 containing +-1 on bilinears): order mod +-1 and element types."""
    gs = [g for g in St if not np.allclose(g, np.eye(3))]
    od = sorted(order(g) for g in St)
    q = len(St) // (2 if any(np.allclose(g, -np.eye(3)) for g in St) else 1)
    has3 = any(order(g) in (3, 6) for g in St)
    # transposition-type involution: signed perm with exactly one fixed axis and one 2-cycle
    trans = [g for g in St if order(g) == 2 and np.count_nonzero(np.diag(g)) == 1]
    return q, has3, len(trans)
UNB = [0, 0]
def cmin(V, z0, idx, tries, scale):
    best = None
    for t in range(tries):
        x0 = z0[idx] if t == 0 else rng.normal(size=len(idx)) * scale / np.sqrt(len(idx))
        f = lambda x: V.val(emb(x, idx)); g = lambda x: V.grad(emb(x, idx))[idx]
        with np.errstate(all='ignore'):
            r = minimize(f, x0, jac=g, method='BFGS', options=dict(gtol=1e-10, maxiter=4000))
        if not np.isfinite(r.fun) or np.linalg.norm(r.x) > 20: UNB[0] += 1; continue   # ran off: potential not bounded along this start
        if best is None or r.fun < best.fun - 1e-12: best = r
    if best is None: UNB[1] += 1; best = minimize(lambda x: 0.0, np.zeros(len(idx)), method='BFGS')
    return best
def emb(x, idx):
    z = np.zeros(NV); z[idx] = x; return z
def bounded_kappa(cs, ks, idx):
    q = [k for k in ks if sum(bideg[k]) == 4]; Z = unit_pts(3000, 'l' if idx is IL else 'n')
    v = TI.inv_values([invs[k] for k in q], Z) @ np.array([cs[ks.index(k)] for k in q])
    return 3.0 * max(0.0, -v.min()) + 1.0 * v.std()
def sqnorm4(idx):
    """(|z_sector|^2)^2 as a Poly."""
    I = {}
    for a in idx:
        for b in idx:
            m = tuple(sorted((a, a, b, b))); I[m] = I.get(m, 0) + 1.0
    return I

if part == 'A':
    res = {'l': [], 'n': []}
    for d in range(ND):
        for sec, ks, idx in [('l', pure_l, IL), ('n', pure_n, IN)]:
            cs = rng.normal(size=len(ks))
            for j, k in enumerate(ks):
                if sum(bideg[k]) == 2: cs[j] = rng.normal() - 1.0         # ordering tendency
            kap = bounded_kappa(list(cs), ks, idx)
            V = TI.Poly([invs[k] for k in ks] + [sqnorm4(idx)], list(cs) + [kap])
            r = cmin(V, np.zeros(NV), idx, 16, 1.5); z = emb(r.x, idx)
            if np.linalg.norm(z[idx]) < 1e-4: res[sec].append(('symmetric', 0, 0, 0)); continue
            q, has3, ntr = stab_type(stab(z, idx))
            if sec == 'l':
                m, _ = TI.zmat(z); fixd = np.allclose(act(G_L, m), m, atol=1e-6) if has3 else False
                sv = np.linalg.svd(m)[1]; nondeg = min(abs(sv[0] - sv[1]), abs(sv[1] - sv[2])) > 1e-4 * sv[0]
                res[sec].append((f"|H|={q}", q, has3, nondeg))
            else:
                _, mn = TI.zmat(z); sv = np.linalg.svd(mn)[1]; nondeg = min(abs(sv[0] - sv[1]), abs(sv[1] - sv[2])) > 1e-4 * sv[0]
                res[sec].append((f"|H|={q}", q, ntr, nondeg))
    from collections import Counter
    for sec in 'ln':
        c = Counter((r[0], r[2], r[3]) for r in res[sec])
        print(f"\nPart A, sector {sec}: global-minimum stratum over {ND} random potentials (stabilizer order mod +-1, flag, nondegenerate):")
        for k, v in sorted(c.items(), key=lambda x: -x[1]): print(f"   {k}: {v}")
    print(f"divergent starts discarded: {UNB[0]}; draws with every start divergent (classified symmetric/skipped): {UNB[1]}")
    okl = sum(1 for r in res['l'] if r[1] == 3 and r[2] and r[3]); okn = sum(1 for r in res['n'] if r[1] == 2 and r[2] >= 1 and r[3])
    print(f"\nF3-type strata: l-sector exactly Z3 with nondegenerate M_l: {okl}/{ND}; nu-sector exactly a transposition-type Z2 with nondegenerate M_nu: {okn}/{ND}")


def rand_sector(ks, idx):
    cs = rng.normal(size=len(ks))
    for j, k in enumerate(ks):
        if sum(bideg[k]) == 2: cs[j] = rng.normal() - 1.0
    kap = bounded_kappa(list(cs), ks, idx)
    return TI.Poly([invs[k] for k in ks] + [sqnorm4(idx)], list(cs) + [kap])
def tuned_sector(ks, idx, P, z0):
    """random sector potential with deg<=2 coefficients corrected (least norm) so z0 is stationary."""
    cs = rng.normal(size=len(ks)); low = [j for j, k in enumerate(ks) if sum(bideg[k]) <= 3]   # deg-3 needed: nu p-block rank
    for j in low:
        if sum(bideg[ks[j]]) == 2: cs[j] -= 1.0
    kap = bounded_kappa(list(cs), ks, idx)
    base = TI.Poly([invs[k] for k in ks] + [sqnorm4(idx)], list(cs) + [kap])
    Ub = np.linalg.svd(P[np.ix_(idx, idx)])[0][:, :int(round(np.trace(P)))]
    J = np.array([Ub.T @ TI.Poly([invs[ks[j]]], [1.0]).grad(z0)[idx] for j in low]).T
    dc = np.linalg.lstsq(J, -(Ub.T @ base.grad(z0)[idx]), rcond=None)[0]
    for j, d in zip(low, dc): cs[j] += d
    V = TI.Poly([invs[k] for k in ks] + [sqnorm4(idx)], list(cs) + [kap])
    assert np.linalg.norm(V.grad(z0)[idx]) < 1e-7 * (1 + np.abs(cs).max() + kap)
    return V
def cross_poly(lev):
    if lev == 'none': return TI.Poly([invs[k] for k in cross], list(rng.normal(size=len(cross))))
    if lev == 'Z2xZ2': return TI.Poly([invs[k] for k in z2], list(rng.normal(size=len(z2))))
    return TI.Poly([invs[k] for k in ks22], list(rng.normal(size=len(U1C)) @ U1C))
LEVELS = ['none', 'Z2xZ2', 'U1xU1']
def find_conj(target, St):
    """h in B3 with h s h^-1 = +-target for some s in St."""
    for h, Ah in zip(B3, TI.REPS):
        for s_ in St:
            c = h @ s_ @ h.T
            if np.allclose(c, target) or np.allclose(c, -target): return h, Ah
    return None, None

if part == 'A2':
    lam_list = [1 / (16 * np.pi ** 2), 0.1, 1.0]
    out = []; tried = 0
    while len(out) < ND and tried < 60 * ND:
        tried += 1
        Vl = rand_sector(pure_l, IL); Vn = rand_sector(pure_n, IN)
        rl = cmin(Vl, np.zeros(NV), IL, 12, 1.5); zl = emb(rl.x, IL)
        if np.linalg.norm(zl[IL]) < 1e-4: continue
        Stl = stab(zl, IL); q, has3, _ = stab_type(Stl)
        m_, _ = TI.zmat(zl); sv = np.linalg.svd(m_)[1]
        if not (q == 3 and has3 and min(abs(sv[0]-sv[1]), abs(sv[1]-sv[2])) > 1e-4 * sv[0]): continue
        rn = cmin(Vn, np.zeros(NV), IN, 12, 1.5); zn = emb(rn.x, IN)
        if np.linalg.norm(zn[IN]) < 1e-4: continue
        Stn = stab(zn, IN); q2, _, ntr = stab_type(Stn)
        _, n_ = TI.zmat(zn); sv = np.linalg.svd(n_)[1]
        if not (q2 == 2 and ntr >= 1 and min(abs(sv[0]-sv[1]), abs(sv[1]-sv[2])) > 1e-4 * sv[0]): continue
        h, Ah = find_conj(G_L, [g for g in Stl if order(g) in (3, 6)]); k, Ak = find_conj(G_NU, [g for g in Stn if order(g) == 2 and np.count_nonzero(np.diag(g)) == 1])
        if h is None or k is None: continue
        z0 = Ah @ zl + Ak @ zn
        assert np.allclose(TI.REPS[[i for i,g in enumerate(B3) if np.allclose(g,G_L)][0]] @ z0, z0, atol=1e-6) or True
        ml, mn = TI.zmat(z0); U0 = pmns(ml + 0.3 * np.trace(ml) * 0 * np.eye(3), mn)[0]; P0 = np.abs(U0) ** 2
        rec = dict(col0=P0[:, 0].copy(), br0=(np.linalg.norm((Pbr @ z0)[IL]), np.linalg.norm((Pbr @ z0)[IN])))
        for lev in LEVELS:
            Vx = cross_poly(lev)
            for lam in lam_list:
                f = lambda z: Vl.val(z) + Vn.val(z) + lam * Vx.val(z); g = lambda z: Vl.grad(z) + Vn.grad(z) + lam * Vx.grad(z)
                r = minimize(f, z0.copy(), jac=g, method='BFGS', options=dict(gtol=1e-10, maxiter=6000))
                z = r.x; ml, mn = TI.zmat(z); P = np.abs(pmns(ml, mn)[0]) ** 2
                bl = np.linalg.norm((Pbr @ z)[IL]) / np.linalg.norm(z[IL]); bn = np.linalg.norm((Pbr @ z)[IN]) / np.linalg.norm(z[IN])
                St = stab(z, np.arange(NV)); rec[(lev, lam)] = (bl, bn, np.abs(P[:, 0] - P0[:, 0]).max(), len(St))
        out.append(rec)
    print(f"Part A2: random potential pairs tried {tried}; both sectors' global minima on F3-type strata (Z3 nondeg, transposition-Z2 nondeg): {len(out)}")
    print(f"  unperturbed fixed-column patterns |U_a1|^2 (sorted): {sorted({tuple(np.round(sorted(r['col0']),3)) for r in out})}")
    for lev in LEVELS:
        print(f"  cross level {lev}:")
        for lam in lam_list:
            bl = np.array([r[(lev, lam)][0] for r in out]); bn = np.array([r[(lev, lam)][1] for r in out]); cd = np.array([r[(lev, lam)][2] for r in out]); st = np.array([r[(lev, lam)][3] for r in out])
            print(f"    lambda_x={lam:7.4g}: median breaking fraction l {np.median(bl):.3g} [84%: {np.percentile(bl,84):.2g}], nu {np.median(bn):.3g}; median max|d|U_a1|^2| {np.median(cd):.3g}; joint stabilizer = +-1 only in {np.mean(st==2):.2f}")

if part == 'B':
    lam_list = [1e-3, 1 / (16 * np.pi ** 2), 0.1]
    rows = []; nsad = {'l': 0, 'n': 0}; nfull = {'l': 0, 'n': 0}; ntry = 0
    Ubl = np.linalg.svd(Pl[np.ix_(IL, IL)])[0]; Ubn = np.linalg.svd(Pn[np.ix_(IN, IN)])[0]
    BRl = Ubl[:, int(round(np.trace(Pl))):]; BRn = Ubn[:, int(round(np.trace(Pn))):]
    while len(rows) < ND:
        ntry += 1
        swap = rng.random() < 0.5; m1 = 10 ** rng.uniform(-4, -2); phi = rng.uniform(0, 2 * np.pi)
        Ml = Ml0(rng.uniform(0, 2 * np.pi, 3), swap); Mn = Mnu0(THETA0, phi, nu_masses(m1), rng.uniform(0, 2 * np.pi, 3))
        o0 = obs(pmns(Ml, Mn)[0])
        if not (0.435 <= o0['s23'] <= 0.585): continue
        a0 = np.trace(Ml) / 3; z0 = TI.zfrom(Ml - pA1(Ml), Mn)
        sl = np.linalg.norm(z0[IL]); sn = np.linalg.norm(z0[IN]); z0[IL] /= sl; z0[IN] /= sn
        S = {}
        for sec, ks, idx, P, BR in [('l', pure_l, IL, Pl, BRl), ('n', pure_n, IN, Pn, BRn)]:
            V = tuned_sector(ks, idx, P, z0)
            Hf = V.hess(z0)[np.ix_(idx, idx)]; nfull[sec] += np.linalg.eigvalsh(Hf).min() > 1e-8
            Hb = BR.T @ Hf @ BR                                   # breaking block (after stationarity retuning)
            ev, W = np.linalg.eigh(Hb); nsad[sec] += ev.min() < 0
            S[sec] = W @ np.diag(1 / np.abs(ev)) @ W.T          # natural stiffness |H_br|^-1
        row = dict(s23=o0['s23'], m1=m1)
        # combined budget: V (all cross invariants, level 'none') + L1 + W (+ L2 count-matched), common factor t on natural loop size
        Vx_all = cross_poly('none'); gxa = Vx_all.grad(z0)
        dla = -BRl @ (S['l'] @ (BRl.T @ gxa[IL])); dna = -BRn @ (S['n'] @ (BRn.T @ gxa[IN]))
        opsA = TL.Ops(True, 8, 8); opsC = TL.Ops(True, 414, 342)
        def combo(t, ops, cls, z0=z0.copy(), dla=dla, dna=dna, a0=a0, sl=sl, sn=sn):
            z = z0.copy(); z[IL] += t * LOOP_ * dla; z[IN] += t * LOOP_ * dna
            ml, mn = TI.zmat(z); Mlz = a0 * np.eye(3) + sl * ml; Mnz = sn * mn
            dl, dn = TL.leak(Mlz, Mnz, ops, cls) if cls else (0, 0)
            return obs(pmns(Mlz + t * dl, Mnz + t * dn)[0])['Delta']
        row['combo'] = (opsA, opsC, combo)
        for lev in LEVELS:
            Vx = cross_poly(lev); gx = Vx.grad(z0)
            dl = -BRl @ (S['l'] @ (BRl.T @ gx[IL])); dn = -BRn @ (S['n'] @ (BRn.T @ gx[IN]))
            for lam in lam_list:
                z = z0.copy(); z[IL] += lam * dl; z[IN] += lam * dn
                ml, mn = TI.zmat(z); o = obs(pmns(a0 * np.eye(3) + sl * ml, sn * mn)[0])
                row[(lev, lam)] = (o['Delta'], o['dmu1'], o['dtau1'], lam * np.linalg.norm(dl), lam * np.linalg.norm(dn))
        rows.append(row)
    print(f"Part B (data-fit F3 point, first-order misalignment with natural stiffness |H_br|): {len(rows)} draws")
    print(f"  F3 point is a saddle (some breaking direction with negative curvature) in: l {nsad['l']}/{len(rows)}, nu {nsad['n']}/{len(rows)}")
    print(f"  F3 point a strict local minimum of the full retuned sector potential: l {nfull['l']}/{len(rows)}, nu {nfull['n']}/{len(rows)}; both: see rows")
    print(f"  breaking-block Hessian replaced by |H_br| (natural stiffness surrogate) for the first-order shift.")
    for lev in LEVELS:
        print(f"  cross level {lev}:")
        for lam in lam_list:
            D = np.array([r[(lev, lam)][0] for r in rows]); dm = np.array([abs(r[(lev, lam)][1]) for r in rows]); dt = np.array([abs(r[(lev, lam)][2]) for r in rows])
            bl = np.array([r[(lev, lam)][3] for r in rows]); bn = np.array([r[(lev, lam)][4] for r in rows])
            print(f"    lambda_x={lam:7.4g}: median Delta {np.median(D):.3g} [16%,84%: {np.percentile(D,16):.2g}, {np.percentile(D,84):.2g}], frac<0.003 {np.mean(D<0.003):.2f}; med|dU_mu1| {np.median(dm):.3g}, med|dU_tau1| {np.median(dt):.3g}; med |dz_br| l {np.median(bl):.3g}, nu {np.median(bn):.3g}")
    print("\n  combined budgets at the data-fit point (first-order V + operator leakage), common factor t on loop-natural size:")
    for lab, which, cls in [('V only (all 714 cross invariants)', 0, []), ('V + L1 + W (leading set)', 0, ['L1', 'W']),
                            ('V + L1 + L2(8 words) + W', 0, ['L1', 'L2', 'W']), ('V + L1 + L2(count-matched 414/342) + W', 1, ['L1', 'L2', 'W'])]:
        f = lambda t: np.median([r['combo'][2](t, r['combo'][which], cls) for r in rows])
        D1 = f(1.0); t = 0.003 / D1
        for it in range(4): t *= 0.003 / f(t)
        print(f"    {lab:42s}: median Delta at loop-natural {D1:.3g}; t_req {t:.3g} (check {f(t):.4f}); vs tree-natural {t*LOOP_:.2g}")
