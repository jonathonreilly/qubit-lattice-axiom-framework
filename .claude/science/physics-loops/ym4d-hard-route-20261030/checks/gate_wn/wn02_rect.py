"""R1-R5 of CRITERIA.md. Rectangle identity and Wilson rectangle sum, reviewer's code."""
import sys, time
import numpy as np
from wnlib import *

rng = np.random.default_rng(31102026)


def rot_field(E, T):
    """Pushforward of a link field under rho:(x1,x2)->(1-x2,x1) about (1/2,1/2). Directions 0,1 in-plane."""
    d = 4
    out = np.zeros_like(E)
    idx = np.arange(T)
    # build permutation arrays on sites
    x1, x2 = np.meshgrid(idx, idx, indexing="ij")
    r1 = (1 - x2) % T
    r2 = x1
    for x3 in idx:
        for x4 in idx:
            # dir0 link at x -> dir1 link at rho(x), sign +
            out[1, r1, r2, x3, x4] = E[0, x1, x2, x3, x4]
            # dir1 link at x -> reversed dir0 link at rho(x) - e1, sign -
            out[0, (r1 - 1) % T, r2, x3, x4] = -E[1, x1, x2, x3, x4]
            out[2, r1, r2, x3, x4] = E[2, x1, x2, x3, x4]
            out[3, r1, r2, x3, x4] = E[3, x1, x2, x3, x4]
    return out


def square(c3, c4, D):
    return [(0, 0, c3, c4), (0, 0, c3 + D, c4), (0, 0, c3 + D, c4 + D), (0, 0, c3, c4 + D)]


def sigma(k, ys, D):
    # straight segment from y_k to y_{k+1}
    if k == 0:
        return line(ys[0], 2, D)[0]
    if k == 1:
        return line(ys[1], 3, D)[0]
    if k == 2:
        return line(ys[2], 2, -D)[0]
    return line(ys[3], 3, -D)[0]


def tau_path(y, z):
    p = []
    cur = tuple(y)
    for mu in range(4):
        n = z[mu] - cur[mu]
        seg, cur = line(cur, mu, n)
        p += seg
    return p


def R1R2(T=8, D=2):
    d = 4
    ys = square(2, 2, D)
    far = (3, 5, 1, 6)
    l3 = plaq(far, 2, 3)
    ws = []
    for _ in range(6):
        w = rng.normal(size=(4,) + (T,) * 4) * (rng.random(size=(4,) + (T,) * 4) < 0.3)
        orb = [w]
        for r in range(3):
            orb.append(rot_field(orb[-1], T))
        ws.append(orb)

    def capply(J, sym):
        out = green(J, T, d)
        if sym:
            for orb in ws:
                for w in orb:
                    out = out + 0.03 * w * np.sum(w * J)
        return out

    for sym in (True, False):
        Js = [current(plaq(y, 0, 1), T, d) for y in ys]
        Es = [capply(J, sym) for J in Js]
        e = capply(current(l3, T, d), sym)
        # equal increments check
        worst = 0
        for E in Es:
            for y in ys:
                inc = incr(E, plaq(y, 0, 1), T)
                worst = max(worst, np.ptp(inc))
        lhs = 0.0
        term_flux = 0.0
        term_A = 0.0
        term_tail = 0.0
        scale = 0
        for k in range(4):
            kp = (k + 1) % 4
            sig = sigma(k, ys, D)
            tau = tau_path(ys[k], far)
            paths = [plaq(ys[k], 0, 1), lasso(sig, plaq(ys[kp], 0, 1)), lasso(tau, l3)]
            kc = K_comp(paths, [Es[k], Es[kp], e], T)
            Pk = np.sum(current(plaq(ys[k], 0, 1), T, d) * Es[kp])
            P3k = np.sum(current(plaq(ys[k], 0, 1), T, d) * e)
            P3kp = np.sum(current(plaq(ys[kp], 0, 1), T, d) * e)
            lhs += kc / Pk
            term_flux += incr(e, sig, T).sum()
            term_A += levy(l3, Es[k], Es[kp], T) / Pk
            Ek_tau = incr(Es[k], tau, T).sum()
            Ek_sig = incr(Es[k], sig, T).sum()
            Ekp_tau = incr(Es[kp], tau, T).sum()
            term_tail += (P3kp * (Ek_tau - Ek_sig) - P3k * Ekp_tau) / Pk
            scale = max(scale, abs(kc / Pk))
        rhs = -24 * term_flux - 12 * term_A - 24 * term_tail
        print(f"R1 sym={sym}: LHS {lhs:.10f} RHS {rhs:.10f} resid/scale {abs(lhs-rhs)/scale:.2e}; incr spread {worst:.2e}; -24Flux {-24*term_flux:.6f} farA {-12*term_A:.6f} tail {-24*term_tail:.6f}", flush=True)


CLAIM = {(3, 6): (-1.619e-2, 7.85e-3), (3, 8): (-5.242e-3, 1.88e-3), (3, 12): (-1.037e-3, 2.27e-4), (3, 16): (-3.51e-4, 4.63e-5)}


def R345(T=40, D=3, Rs=(6, 8, 12, 16)):
    d = 4
    c3 = T // 2
    ys = square(c3, c3, D)
    Es = [green(current(plaq(y, 0, 1), T, d), T, d) for y in ys]
    Pks = [np.sum(current(plaq(ys[k], 0, 1), T, d) * Es[(k + 1) % 4]) for k in range(4)]
    print(f"T={T} D={D} P_k {Pks[0]:.6e} (claimed 2.262e-3 at D=3 for large T); all equal spread {np.ptp(Pks):.1e}", flush=True)
    rows = []
    for R in Rs:
        far = (R, 0, c3 + (D - 1) // 2, c3 + (D - 1) // 2)
        l3 = plaq(far, 2, 3)
        e = green(current(l3, T, d), T, d)
        sc = st = 0.0
        flux = 0.0
        for k in range(4):
            kp = (k + 1) % 4
            sig = sigma(k, ys, D)
            tau = tau_path(ys[k], far)
            paths = [plaq(ys[k], 0, 1), lasso(sig, plaq(ys[kp], 0, 1)), lasso(tau, l3)]
            kc = K_comp(paths, [Es[k], Es[kp], e], T)
            kv = 12 * sumV(Es[k], Es[kp], e, T, d)
            sc += kc / Pks[k]
            st += (kc + kv) / Pks[k]
            flux += incr(e, sig, T).sum()
        x2 = R ** 2 + 0.25 + 0.25   # far plaquette centre vs square centre, offset (R + 0, 1/2 - 1/2 in-plane), small
        cont = -24 * D ** 2 * (1 - 0) / (np.pi ** 2 * R ** 4)
        ck = CLAIM.get((D, R))
        msg = ""
        if ck and T == 40:
            ok = abs(sc - ck[0]) < 0.02 * abs(ck[0]) and abs(st - ck[1]) < 0.02 * abs(ck[1])
            msg = "ok" if ok else f"DIFF from claimed {ck}"
        rows.append((R, st, -24 * flux))
        print(f"R3 R={R}: Stk_comp {sc:.4e} -24Flux {-24*flux:.4e} Stk_total {st:.4e} ratio {abs(st)/abs(24*flux):.3f}; continuum axis -24Flux {cont:.3e} ratio {(-24*flux)/cont:.3f} {msg}", flush=True)
    for a, b in zip(rows, rows[1:]):
        print(f"R4 slope R={a[0]}->{b[0]}: Stk_total {np.log(abs(b[1]/a[1]))/np.log(b[0]/a[0]):.2f}, Flux {np.log(abs(b[2]/a[2]))/np.log(b[0]/a[0]):.2f}")


if __name__ == "__main__":
    R1R2()
    R345(T=40)
    if "big" in sys.argv:
        R345(T=56, Rs=(8, 12, 16, 20))
