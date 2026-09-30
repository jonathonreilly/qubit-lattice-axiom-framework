"""Kill-check of T30 (Claude Sonnet 5.5, same family as attacker).  Independent re-implementation:
variable x = 1/alpha, LSODA, own event handling; SU(3) MSbar b0,b1,b2 with n Dirac fundamentals.
d(1/alpha)/dt = (1/(2 pi)) * (b0 + b1 a + b2 a^2),  a=alpha/4pi,  t = ln mu   (alpha decreases with t when b>0).
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

U0 = 0.8776813811986843
A_BARE = 1/(4*math.pi)
A_LM = A_BARE/U0
DT = math.log(A_LM)
MPL = 1.2209e19; V = 246.28
LV = math.log(MPL/V)

def bs(n): return (11-2*n/3, 102-38*n/3, 2857/2-5033*n/18+325*n*n/54)

def dxdt(n, loops):
    b0, b1, b2 = bs(n)
    def f(t, y):
        x = y[0]; a = 1/(4*math.pi*x)
        b = b0 + (b1*a if loops >= 2 else 0) + (b2*a*a if loops >= 3 else 0)
        return [b/(2*math.pi)]
    return f

def seg(x0, t0, t1, n, loops, xmark=1.0):
    """integrate x=1/alpha from t0 to t1 (t1<t0). returns (x_end, t_end, hit) ; hit if alpha reached 1/xmark"""
    f = dxdt(n, loops)
    ev = lambda t, y: y[0]-xmark
    ev.terminal = True; ev.direction = -1
    sol = solve_ivp(f, [t0, t1], [x0], method='LSODA', events=ev, rtol=1e-11, atol=1e-13)
    if sol.status == 1: return xmark, sol.t_events[0][0], True
    return sol.y[0][-1], t1, False

def stair(nfun, loops, x0=1/A_LM, nr=16, dt=DT, xmark=1.0):
    t = 0.0; x = x0
    for k in range(nr):
        x, t2, hit = seg(x, t, t+dt, nfun(k), loops, xmark)
        if hit: return t2/dt, True, x
        t += dt
    return t/dt, False, x

out = []
def P(s):
    print(s); out.append(s)

P("== 1. independent reproduction: repo staircase n=16-k (Dirac count as the repo uses), alpha=1 at rung:")
for loops in (1, 2, 3):
    r, hit, x = stair(lambda k: 16-k, loops)
    P("  loops=%d: rung of alpha=1: %.2f (attacker: 8.87 / 9.41 / 9.59)  hit=%s" % (loops, r, hit))
P("== 2. n=16 fixed points: 2-loop %.4f  3-loop %.4f" % (
    4*math.pi*(-bs(16)[0]/bs(16)[1]),
    4*math.pi*brentq(lambda a: bs(16)[0]+bs(16)[1]*a+bs(16)[2]*a*a, 1e-5, 0.05)))

# constant n to v
def alpha_v(n, loops, L=38.44):
    x, t, hit = seg(1/A_LM, 0.0, -L, n, loops, xmark=1/3.0)
    return float('inf') if hit else 1/x
for loops in (2, 3):
    n = brentq(lambda n: alpha_v(n, loops)-0.1033, 14.0, 16.0)
    P("== 3. constant n giving alpha(v)=0.1033, loops=%d: n=%.3f   (attacker 15.13 / 15.02)" % (loops, n))
    P("      integer n=15: alpha(v)=%.4f ; n=16: %.4f" % (alpha_v(15, loops), alpha_v(16, loops)))

P("\n== 4. KEY QUESTION: what if the beta-function count is Dirac flavours = species/4 (repo's own regulator no-go B1: staggered = 4; taste census 2026-09-03: 8 = spin2 x chirality2 x flavour2, N_f=2; 16 -> 4)?")
for nD in (2, 4, 6, 8, 12):
    for loops in (2, 3):
        x, t, hit = seg(1/A_LM, 0.0, -300.0, nD, loops, xmark=1.0)
        P("  constant n=%2d loops=%d: %s" % (nD, loops, ("alpha=1 at %.1f e-folds below M_Pl (Lambda/M_Pl=%.1e; needs 38.4+ to reach v)" % (-t, math.exp(t))) if hit else "no pole, alpha(-300)=%.3f" % (1/x)))
for loops in (1, 2, 3):
    r, hit, x = stair(lambda k: (16-k)/4.0, loops)
    P("  staircase n=(16-k)/4 (one corner = 1/4 Dirac): loops=%d alpha=1 at rung %.2f (of 16), t=%.1f e-folds, mu=%.1e GeV" % (loops, r, r*DT, MPL*math.exp(r*DT)))
# best possible: with at most 4 (or 8) Dirac flavours at all scales, max reach = smallest Lambda = largest n
P("  => with at most 4 Dirac flavours at every scale, alpha reaches 1 within <= %.1f e-folds (2-loop); v is 38.4 e-folds down. No threshold placement can slow the flow." %
  max(-seg(1/A_LM, 0.0, -300.0, 4, 2, 1.0)[1], 0))
P("  even with 8 flavours: %.1f e-folds (2-loop)" % (-seg(1/A_LM, 0.0, -300.0, 8, 2, 1.0)[1]))
P("  minimum flavours needed to get alpha(v) <= 0.15 (constant n, 2-loop): scan")
for n in np.arange(11.0, 16.01, 0.5):
    a = alpha_v(n, 2)
    P("     n=%.1f -> alpha(v)=%s" % (n, "pole" if a == float('inf') else "%.4f" % a))

P("\n== 5. one-threshold family: roots s* (e-folds below M_Pl) for alpha(v)=0.1033 by n_low (2-loop), n=16 above")
def one_thr(s, n_low, loops=2):
    x, t, hit = seg(1/A_LM, 0.0, -s, 16, loops, 1.0)
    if hit: return None
    x, t2, hit = seg(x, -s, -38.44, n_low, loops, 1.0)
    return None if hit else 1/x
for n_low in range(0, 16):
    ss = np.linspace(0, 38.44, 400)
    vals = [ (1.0 if one_thr(s, n_low) is None else one_thr(s, n_low)) - 0.1033 for s in ss]
    roots = [brentq(lambda s: (1.0 if one_thr(s, n_low) is None else one_thr(s, n_low)) - 0.1033, ss[i], ss[i+1]) for i in range(len(ss)-1) if vals[i]*vals[i+1] < 0]
    P("  n_low=%2d roots s*: %s" % (n_low, ", ".join("%.2f (mu1=%.1e)" % (r, MPL*math.exp(-r)) for r in roots) or "none"))

P("\n== 6. SU(2) recount")
def su2_b(weyl_doublets): return 22/3 - weyl_doublets/3 - 1/6
P("  attacker's '16 taste copies of SM content' = 16*12 Weyl doublets: b2=%.2f" % su2_b(16*12))
P("  repo 'each taste carries a copy of the Q_L=(2,3) block' = 16*3 Weyl doublets: b2=%.2f" % su2_b(16*3))
P("  one SM generation (4 doublets)*3 gens: b2=%.2f (=19/6)" % su2_b(12))
open('kill_t30_checks_output.txt', 'w').write("\n".join(out)+"\n")
