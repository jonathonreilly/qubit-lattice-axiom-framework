"""OBS-3 R1b: realisations with corner-universal (S3-invariant) one-loop data.
 A (model M1): free right-handed rotations X_u, X_d chosen so that the corner-diagonal Yukawas are corner-constant
   (Higgs data = on-site only).  Any W_u, hence any CKM.
 B (model M2): textures whose corner-diagonal entries are equal (complex) and whose off-diagonal moduli are all equal,
   for both sectors ('equal-modulus' / USY-like textures), fitted to the observed mass ratios and CKM.
   B-gen: off-diagonal phases free (selective tau_x sigma_c carriers); B-sym: Y_cc' = Y_c'c (on-site carriers).
 Then every row (fixed and side) over bracket x placements x splits x carriers x N."""
import numpy as np, itertools, time, sys
from scipy.optimize import least_squares
from scipy.linalg import expm
from obs3_core import *
np.set_printoptions(precision=4, linewidth=160)
P = print; t0 = time.time()
inp = INPUTS['pdg24']; V = inp['V']; mu, md = inp['mu'], inp['md']
GEN = []
for a in range(3):
    for b in range(3):
        H = np.zeros((3, 3), complex)
        if a == b: H[a, a] = 1
        elif a < b: H[a, b] = H[b, a] = 1
        else: H[a, b] = 1j; H[b, a] = -1j
        GEN.append(H)
def unitary(x): return expm(1j * sum(xi * G for xi, G in zip(x, GEN)))

def all_rows(real, Ns=(48, 96), label=''):
    worst_fixed = 0; worst_side = {}; worst_rel = 0
    for N in Ns:
        for (m, D) in BRACKET:
            tabs = get_tabs(N, m, D)
            for car in ('M1', 'M2'):
                if real.get('only') and car != real['only']: continue
                for var in ('sym', 'int', 'ext'):
                    for y0mode in ('trace', 'selective'):
                        for sq in (1.0, 0.45):
                            o = evaluate(dict(real, carrier=car, var=var, y0mode=y0mode), tabs, scale_q=sq)
                            worst_fixed = max(worst_fixed, fixed_ratio(o)[0])
                            for k, v in side_ratio(o).items(): worst_side[k] = max(worst_side.get(k, 0), v)
                            for f in ('Q', 'uc', 'dc'):
                                iso, tet, r = o['fields'][f]
                                worst_rel = max(worst_rel, np.abs(r).max() / abs(iso))
    P(f"  {label}: max FIXED ratio {worst_fixed:.2e}; max |residual|/|universal| (Q,uc,dc) {worst_rel:.1e}; side max: " +
      "  ".join(f"{k} {v:.1e}" for k, v in worst_side.items()), flush=True)
    return worst_fixed, worst_rel, worst_side

# ---------------- A: M1 diag-universalisation
def diag_const_X(W, m):
    H = W @ np.diag(m) @ W.conj().T
    best = None
    rng = np.random.default_rng(3)
    for s in range(20):
        def res(x):
            Y = H @ unitary(x)            # = W m X^dag with X^dag = W^dag U
            d = np.diag(Y); dd = d - d.mean()
            return np.concatenate([dd.real, dd.imag]) / m.max()
        r = least_squares(res, rng.uniform(-np.pi, np.pi, 9), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        if best is None or r.cost < best.cost: best = r
    U = unitary(best.x); Xdag = W.conj().T @ U
    return Xdag.conj().T, np.sqrt(2 * best.cost)
P("A. model M1: right-handed rotations making the corner-diagonal Yukawas corner-constant")
reals = {}
for name, Wu in (('OBS-2 branch B left (W_u = F)', F), ('random W_u', unitary(np.random.default_rng(5).uniform(-np.pi, np.pi, 9))),
                 ('flat-light E1 W_u', np.load('escape_E1_Wu.npy'))):
    Xu, eu = diag_const_X(Wu, mu); Xd, ed = diag_const_X(Wu @ V, md)
    Yu = Wu @ np.diag(mu) @ Xu.conj().T; Yd = Wu @ V @ np.diag(md) @ Xd.conj().T
    P(f" {name}: diag spread (rel.) up {eu:.1e} down {ed:.1e}; diag(M_u) = {np.diag(Yu)}, diag(M_d) = {np.diag(Yd)} GeV")
    reals[name] = dict(Wu=Wu, Xu=Xu, Xd=Xd, only='M1')
    all_rows(reals[name], Ns=(96,), label=name + ' [M1]')
np.savez('univ_A_M1.npz', **{f"{k}_{n}": v for n, r in enumerate(reals.values()) for k, v in r.items() if k != 'only'})

# ---------------- B: equal-modulus textures (M2)
yu, yd = mu / VEV, md / VEV
sig = dict(ud=0.00016, us=0.00068, ub=0.000090, cd=0.00068, cs=0.00016, cb=0.00079, td=0.00019, ts=0.00077, tb=0.000034)
SIG = np.array([[sig['ud'], sig['us'], sig['ub']], [sig['cd'], sig['cs'], sig['cb']], [sig['td'], sig['ts'], sig['tb']]])
AV = np.abs(V)
def J(Vm): return (Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])).imag
J0, sJ = J(V), 0.13e-5
DIAG120 = False
def texture(p, sym):
    r = p[0]
    if sym:
        a, b, c = p[1:4]; ph = np.array([[0, a, b], [a, 0, c], [b, c, 0]])
    else:
        ph = np.zeros((3, 3)); ph[0, 1], ph[0, 2], ph[1, 0], ph[1, 2], ph[2, 0], ph[2, 1] = p[1:7]
    Z = np.exp(1j * ph); Z[np.diag_indices(3)] = np.exp(r) * (np.exp(2j * np.pi * np.arange(3) / 3) if DIAG120 else 1)
    return Z
def svd_sorted(Z):
    U, s, Vh = np.linalg.svd(Z); idx = np.argsort(s)
    return U[:, idx], s[idx], Vh.conj().T[:, idx]
def fit_res(p, sym):
    n = 4 if sym else 7
    Zu, Zd = texture(p[:n], sym), texture(p[n:], sym)
    Wu, su, _ = svd_sorted(Zu); Wd, sd, _ = svd_sorted(Zd)
    Vp = Wu.conj().T @ Wd
    out = [np.log(su[0] / su[2]) - np.log(yu[0] / yu[2]), np.log(su[1] / su[2]) - np.log(yu[1] / yu[2]),
           np.log(sd[0] / sd[2]) - np.log(yd[0] / yd[2]), np.log(sd[1] / sd[2]) - np.log(yd[1] / yd[2])]
    out = [x / 1e-3 for x in out]                      # mass ratios to 0.1%
    out += list(((np.abs(Vp) - AV) / SIG).ravel())
    out.append(abs(J(Vp)) / sJ - J0 / sJ)              # |J| (sign = CP convention)
    return np.array(out)
P("\nB. model M2: equal-modulus corner textures (diag equal, all off-diagonal moduli equal), fit to mass ratios + |V_ij| + |J|")
rng = np.random.default_rng(17)
sols = {}
for sym, d120 in ((False, False), (True, False), (False, True)):
    DIAG120 = d120
    n = 4 if sym else 7
    best = None; nfit = 0
    for s in range(400):
        p0 = np.concatenate([[rng.normal(0, 0.5)], rng.normal(0, 0.3 if s % 2 else 2.0, n - 1)] * 1)
        p0 = np.concatenate([p0, np.concatenate([[rng.normal(0, 0.5)], rng.normal(0, 0.3 if s % 2 else 2.0, n - 1)])])
        try:
            r = least_squares(fit_res, p0, args=(sym,), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=3000)
        except Exception:
            continue
        chi2 = 2 * r.cost
        if chi2 < 1: nfit += 1
        if best is None or chi2 < best[0]: best = (chi2, r.x)
    P(f" {'B-sym (on-site carriers)' if sym else 'B-gen (selective carriers)'}{' diag phases 120deg' if d120 else ''}: best chi2 = {best[0]:.3e} over 400 starts ({nfit} starts with chi2 < 1)  ({time.time()-t0:.0f}s)", flush=True)
    sols[sym] = best
    p = best[1]; Zu, Zd = texture(p[:n], sym), texture(p[n:], sym)
    Wu, su, Xu = svd_sorted(Zu); Wd, sd, Xd = svd_sorted(Zd)
    # scale to y_t, y_b exactly; the light ratios are fitted
    Yu = Zu * (yu[2] / su[2]); Yd = Zd * (yd[2] / sd[2])
    Vp = Wu.conj().T @ Wd
    P(f"   fitted y_u/y_t {su[0]/su[2]:.4e} (target {yu[0]/yu[2]:.4e}), y_c/y_t {su[1]/su[2]:.4e} ({yu[1]/yu[2]:.4e}); y_d/y_b {sd[0]/sd[2]:.4e} ({yd[0]/yd[2]:.4e}), y_s/y_b {sd[1]/sd[2]:.4e} ({yd[1]/yd[2]:.4e})")
    P(f"   |V'| =\n{np.abs(Vp)}\n   pulls =\n{(np.abs(Vp)-AV)/SIG}\n   J' = {J(Vp):+.3e} (PDG {J0:+.3e})")
    P(f"   |Y_u| (units y_t) =\n{np.abs(Yu)/yu[2]}\n   arg Y_u =\n{np.angle(Yu)}\n   |Y_d| (units y_b) =\n{np.abs(Yd)/yd[2]}\n   arg Y_d =\n{np.angle(Yd)}")
    P(f"   |W_u|^2 =\n{np.abs(Wu)**2}\n   |W_d|^2 =\n{np.abs(Wd)**2}")
    real = dict(Yu=Yu, Yd=Yd, Wu=Wu, Xu=Xu, Wd=Wd, Xd=Xd)
    tag = ('sym' if sym else 'gen') + ('120' if d120 else '')
    np.savez(f"univ_B_{tag}.npz", **real, p=p, chi2=best[0])
    all_rows(real, label='B-' + tag + ' [M1 and M2]')
