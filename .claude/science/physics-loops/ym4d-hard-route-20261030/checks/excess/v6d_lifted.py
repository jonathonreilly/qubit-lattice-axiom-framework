#!/usr/bin/env python3
"""T6 and T6a of CRITERIA.md, fourth attempt: charged parents, Newton from the lift of Section 2.2, checkpointed."""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from ex_core import Chain, I_grad, flux_stats, guard, qexp, qinv, qlog, qmul, rss_gb, wilson  # noqa: E402

import torch  # noqa: E402
from v6_charged import LightProblem, charge, const_flux, perturbation  # noqa: E402
from v10_lift_su2 import Lift  # noqa: E402

SCR = "/tmp/excess_v6d"
os.makedirs(SCR, exist_ok=True)
Np, L, d = 8, 3, 4
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 6300.0  # seconds
T0 = time.time()


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
    res_path = os.path.join(HERE, "v6d_lifted.json")
    res = json.load(open(res_path)) if os.path.exists(res_path) else []
    n = Np * L
    chain = Chain(Np, L, d, 1)
    for name, amp, bump, seed in (("a", 0.01, 0.0, 1), ("b", 0.01, 0.015, 2)):
        ck = os.path.join(SCR, f"{name}.pt")
        U0 = qmul(qexp(perturbation(n, amp, bump, seed)), const_flux(n, 1, 1))
        V = chain.top(U0)
        if os.path.exists(ck):
            st = torch.load(ck)
            U, lam, it = st["U"], st["lam"], st["it"]
            if st.get("done"):
                continue
            print(f"resume {name} at newton {it}", flush=True)
        else:
            lf = Lift(Np, L, d, R=3)
            Y = torch.zeros((Np,) * d + (d, 3), dtype=torch.float64)
            hist = []
            for k in range(25):
                r, U = lf.psi(V, Y)
                rn = float(r.norm(dim=-1).max())
                hist.append(rn)
                print(f" lift {name} picard {k} |r| {rn:.3e} t {time.time()-T0:.0f} rss {rss_gb():.2f}", flush=True)
                if rn < 1e-11:
                    break
                Y = Y - r
                guard()
            rec = report(f"lift {name}", U, V, dict(picard=hist))
            res.append(rec)
            json.dump(res, open(res_path, "w"), indent=1)
            del lf
            lam = torch.zeros((Np,) * d + (d, 3), dtype=torch.float64)
            it = 0
            torch.save(dict(U=U, lam=lam, it=it), ck)
        P = LightProblem(chain, V)
        if not hasattr(P, "_gh_inv"):
            P.build_g0()
        while it < 8:
            g = P.lag_grad(torch.zeros(P.shape), U, lam)
            r = P.resid(U)
            gn, rn = float(g.abs().max()), float(r.abs().max())
            print(f"  {name} newton {it} |g|={gn:.3e} |r|={rn:.3e} S={float(wilson(U)):.10f} E={flux_stats(U)[1]:.8f} t {time.time()-T0:.0f} rss {rss_gb():.2f}", flush=True)
            if gn < 2e-7 and rn < 1e-9:
                break
            if time.time() - T0 > BUDGET:
                print("budget reached, checkpointed", flush=True)
                return
            dv, dl = P.kkt_solve(U, lam, -g, -r, 1e-3, 150)
            step = 1.0
            mx = float(dv.abs().max())
            if mx > 0.3:
                step = 0.3 / mx
            U = qmul(qexp(step * dv), U)
            U = U / torch.sqrt((U * U).sum(-1, keepdim=True))
            lam = lam + step * dl
            it += 1
            torch.save(dict(U=U, lam=lam, it=it), ck)
            guard()
        rec = report(f"min {name}", U, V, dict(gn=gn, rn=rn, newton=it))
        res.append(rec)
        json.dump(res, open(res_path, "w"), indent=1)
        torch.save(dict(U=U, lam=lam, it=it, done=True), ck)


if __name__ == "__main__":
    main()
