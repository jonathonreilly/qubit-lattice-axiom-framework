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
            Uc = U
            cnt = [0]

            def fun(x):
                cnt[0] += 1
                guard()
                H = torch.from_numpy(x).reshape(shape)
                Uh = qmul(qexp(H), Uc)
                r = P.resid(Uh)
                val = float(wilson(Uh)) + float((lam * r).sum()) + 0.5 * RHO * float((r * r).sum())
                g = P._wilson_grad(H, Uc) + P._constraint_grad(H, Uc, lam + RHO * r)
                return val, g.reshape(-1).numpy()

            sol = minimize(fun, np.zeros(int(np.prod(shape))), jac=True, method="L-BFGS-B", options=dict(maxcor=6, maxiter=150, maxfun=175, ftol=1e-14, gtol=1e-6))
            H = torch.from_numpy(sol.x).reshape(shape)
            U = qmul(qexp(H), Uc)
            U = U / torch.sqrt((U * U).sum(-1, keepdim=True))
            r = P.resid(U)
            lam = lam + RHO * r
            g = P.lag_grad(torch.zeros(shape), U, lam)
            outer += 1
            gn, rn = float(g.abs().max()), float(r.abs().max())
            print(f"  {name} outer {outer} evals {cnt[0]} |g_L|={gn:.3e} |r|={rn:.3e} S={float(wilson(U)):.8f} E={flux_stats(U)[1]:.8f} t {time.time()-T0:.0f} rss {rss_gb():.2f}", flush=True)
            torch.save(dict(U=U, lam=lam, outer=outer), ck)
            if gn < 2e-4 and rn < 1e-6:
                break
        converged = gn < 2e-4 and rn < 1e-6
        res.append(report(f"min {name}", U, V, dict(gn=gn, rn=rn, outer=outer, converged=converged)))
        json.dump(res, open(res_path, "w"), indent=1)
        torch.save(dict(U=U, lam=lam, outer=outer, done=True), ck)


if __name__ == "__main__":
    main()
