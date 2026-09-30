"""T31 route R2 falsifier: does a literal 16-rung staircase (one colored Dirac taste decouples at each rung
mu_k = M_Pl alpha_LM^k) stay weakly coupled down to the last rung mu_16 ~ v under 2-loop running?
The lane's E4 used ONE-loop and found a Landau-pole crossing; here the 2-loop (Banks-Zaks) term is included.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

P = 0.5934; u0 = P ** 0.25
ab = 1 / (4 * math.pi)
aLM = ab / u0
Mpl = 1.2209e19
lnR = math.log(aLM)          # per-rung log interval (negative)

def beta(alpha, n, loops=2):
    b0 = 11 - 2 * n / 3
    b1 = 102 - 38 * n / 3
    x = -(alpha**2 / (2 * math.pi)) * (b0 + (b1 * alpha / (4 * math.pi) if loops == 2 else 0.0))
    return x  # d alpha / d ln mu

def run(alpha0, loops=2, amax=1.0, verbose=False):
    """integrate downward through rungs; returns (rung index where alpha>=amax first, ln(mu/Mpl)) or None"""
    a = alpha0
    lnmu = 0.0
    traj = [(0, 0.0, a)]
    for k in range(0, 17):
        n = 16 - k
        lnmu_end = (k + 1) * lnR if k < 16 else 20 * lnR   # after the last rung: pure gauge, run 20 more rung-widths
        # integrate from lnmu to lnmu_end (decreasing)
        def f(t, y): return [beta(y[0], n, loops)]
        def ev(t, y): return y[0] - amax
        ev.terminal = True; ev.direction = 1
        sol = solve_ivp(f, [lnmu, lnmu_end], [a], events=ev, rtol=1e-10, atol=1e-12, max_step=0.05)
        if sol.status == 1:
            return k, sol.t_events[0][0], traj
        a = sol.y[0, -1]; lnmu = lnmu_end
        traj.append((k + 1, lnmu, a))
    return None, None, traj

def gev(lnmu): return Mpl * math.exp(lnmu)

out = {}
for name, a0 in (("alpha_bare", ab), ("alpha_LM", aLM), ("alpha_s", ab / u0**2)):
    for loops in (1, 2):
        k, t, traj = run(a0, loops)
        if k is None:
            msg = "never reaches alpha=1 in 16 rungs + 20 more rung-widths"
        else:
            msg = f"alpha reaches 1 in rung {k} (n_active={16-k}) at mu = {gev(t):.3e} GeV  (v_cand-scale rung 16 is {gev(16*lnR):.3e} GeV)"
        print(f"{name:11s} alpha0={a0:.4f} {loops}-loop: {msg}")
        out[f"{name}_{loops}loop"] = msg

# trajectory of the 2-loop alpha_s start
k, t, traj = run(ab / u0**2, 2)
print("\n2-loop trajectory from alpha_s=0.1033 (rung, ln(mu/Mpl), alpha):")
for r, l, a in traj[:18]:
    print(f"  rung {r:2d}  mu={gev(l):.3e} GeV  n_below={max(16-r,0):2d}  alpha={a:.4f}")

# what alpha0 makes the 2-loop staircase hit alpha=1 exactly at the last rung boundary (mu_16, v-scale)?
def hit_ln(a0, loops):
    k, t, tr = run(a0, loops)
    if k is None: return 40 * lnR
    return t
target = 16 * lnR
for loops in (1, 2):
    try:
        a_need = brentq(lambda a: hit_ln(a, loops) - target, 0.02, 0.6, xtol=1e-6)
        print(f"{loops}-loop: alpha0 that puts the strong-coupling point exactly at rung 16 (v-scale): {a_need:.4f}  (1/alpha0={1/a_need:.2f});  framework alpha_s={ab/u0**2:.4f} (1/alpha={u0**2/ab:.2f})")
        out[f"alpha0_needed_{loops}loop"] = a_need
    except Exception as e:
        print(loops, "-loop root-find failed:", e)
import json; json.dump(out, open("staircase2loop_result.json", "w"), indent=1)
