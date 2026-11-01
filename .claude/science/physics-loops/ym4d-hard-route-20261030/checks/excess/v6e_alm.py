#!/usr/bin/env python3
"""T6 of CRITERIA.md, fifth attempt: charged parents, augmented Lagrangian with L-BFGS from the lift, checkpointed."""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from ex_core import Chain, I_grad, flux_stats, guard, qexp, qmul, rss_gb, wilson  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from scipy.optimize import minimize  # noqa: E402
from v6_charged import LightProblem, charge, const_flux, perturbation  # noqa: E402
from v10_lift_su2 import Lift  # noqa: E402

SCR = "/tmp/excess_v6e"
os.makedirs(SCR, exist_ok=True)
Np, L, d = 8, 3, 4
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 6000.0
T0 = time.time()
RHO = 10.0


def report(tag, U, V, extra=None):
    fV, EV = flux_stats(V)
    fU, EU = flux_stats(U)
    IV = float(I_grad(V))
    out = dict(tag=tag, fV=fV, EV=EV, fU=fU, EU=EU, e=EU - EV, Igrad=IV, Ifine=float(I_grad(U)), QV=charge(V), QU=charge(U), S=float(wilson(U)))
    out["e_over_I"] = out["e"] / IV if IV else None
    out["C_eff_810"] = (IV / 810 - out["e"]) / (fV * EV)
    if extra:
        out.update(extra)
    print(json.dumps(out), flush=True)
    return out


def lbfgs(P, U, lam, shape, maxit=150, m=6):
    """L-BFGS on the group, left trivialised, no vector transport: steps are small."""

    def phi(Ux, want_grad=True):
        r = P.resid(Ux)
        val = float(wilson(Ux)) + float((lam * r).sum()) + 0.5 * RHO * float((r * r).sum())
        if not want_grad:
            return val, None
        return val, P._wilson_grad(torch.zeros(shape), Ux) + P.cgrad_left(Ux, lam + RHO * r)

    val, g = phi(U)
    S, Y, Rh = [], [], []
    alpha0 = 0.05
    evals = 1
    for it in range(maxit):
        q = g.clone()
        al = []
        for s_, y_, rh in zip(reversed(S), reversed(Y), reversed(Rh)):
            a = rh * float((s_ * q).sum())
            al.append(a)
            q -= a * y_
        if S:
            q *= float((S[-1] * Y[-1]).sum()) / float((Y[-1] * Y[-1]).sum())
        else:
            q *= alpha0
        for (s_, y_, rh), a in zip(zip(S, Y, Rh), reversed(al)):
            b = rh * float((y_ * q).sum())
            q += (a - b) * s_
        d = -q
        slope = float((g * d).sum())
        if slope >= 0:
            d = -alpha0 * g
            slope = float((g * d).sum())
            S, Y, Rh = [], [], []
        t = 1.0
        while True:
            Un = qmul(qexp(t * d), U)
            Un = Un / torch.sqrt((Un * Un).sum(-1, keepdim=True))
            vn, _ = phi(Un, want_grad=False)
            evals += 1
            if vn <= val + 1e-4 * t * slope or t < 1e-3:
                break
            t *= 0.5
        _, gn = phi(Un)
        evals += 1
        sk = t * d
        yk = gn - g
        sy = float((sk * yk).sum())
        if sy > 1e-14:
            S.append(sk)
            Y.append(yk)
            Rh.append(1.0 / sy)
            if len(S) > m:
                S.pop(0), Y.pop(0), Rh.pop(0)
        U, g, val = Un, gn, vn
        guard()
        if float(g.abs().max()) < 2e-5:
            break
    return U, evals


def main():
    res_path = os.path.join(HERE, "v6e_alm.json")
    res = json.load(open(res_path)) if os.path.exists(res_path) else []
    n = Np * L
    chain = Chain(Np, L, d, 1)
    for name, amp, bump, seed in (("a", 0.01, 0.0, 1), ("b", 0.01, 0.015, 2)):
        ck = os.path.join(SCR, f"{name}.pt")
        U0 = qmul(qexp(perturbation(n, amp, bump, seed)), const_flux(n, 1, 1))
        V = chain.top(U0)
        if os.path.exists(ck):
            st = torch.load(ck)
            U, lam, outer = st["U"], st["lam"], st["outer"]
            if st.get("done"):
                continue
            print(f"resume {name} at outer {outer}", flush=True)
        else:
            lf = Lift(Np, L, d, R=3)
            Y = torch.zeros((Np,) * d + (d, 3), dtype=torch.float64)
            hist = []
            for k in range(25):
                r, U = lf.psi(V, Y)
                rn = float(r.norm(dim=-1).max())
                hist.append(rn)
                if rn < 1e-11:
                    break
                Y = Y - r
                guard()
            res.append(report(f"lift {name}", U, V, dict(picard=hist)))
            json.dump(res, open(res_path, "w"), indent=1)
            del lf
            lam = torch.zeros((Np,) * d + (d, 3), dtype=torch.float64)
            outer = 0
            torch.save(dict(U=U, lam=lam, outer=outer), ck)
        P = LightProblem(chain, V)
        shape = P.shape
        while outer < 14:
            if time.time() - T0 > BUDGET:
                print("budget reached, checkpointed", flush=True)
                return
            U, cnt = lbfgs(P, U, lam, shape)
            r = P.resid(U)
            lam = lam + RHO * r
            g = P._wilson_grad(torch.zeros(shape), U) + P.cgrad_left(U, lam)
            outer += 1
            gn, rn = float(g.abs().max()), float(r.abs().max())
            print(f"  {name} outer {outer} evals {cnt} |g_L|={gn:.3e} |r|={rn:.3e} S={float(wilson(U)):.8f} E={flux_stats(U)[1]:.8f} t {time.time()-T0:.0f} rss {rss_gb():.2f}", flush=True)
            torch.save(dict(U=U, lam=lam, outer=outer), ck)
            if gn < 2e-4 and rn < 1e-6:
                break
        converged = gn < 2e-4 and rn < 1e-6
        res.append(report(f"min {name}", U, V, dict(gn=gn, rn=rn, outer=outer, converged=converged)))
        json.dump(res, open(res_path, "w"), indent=1)
        torch.save(dict(U=U, lam=lam, outer=outer, done=True), ck)


if __name__ == "__main__":
    main()
