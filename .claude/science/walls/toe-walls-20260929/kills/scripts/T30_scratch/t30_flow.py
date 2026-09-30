"""T30 test: perturbative bridge from the Planck lattice coupling to v (SU(3), n_taste in place of n_f).
Not a repo result.  Inputs are the repo's own numbers (alpha_bare=1/4pi, u0, alpha_LM, L=38.44) and the
standard MSbar coefficients (PDG QCD review):
   mu^2 d a/d mu^2 = -(b0 a^2 + b1 a^3 + b2 a^4),  a = alpha/(4 pi)
   b0 = 11 - 2n/3, b1 = 102 - 38n/3, b2 = 2857/2 - 5033 n/18 + 325 n^2/54.
t = ln(mu/M_Pl) <= 0.   da/dt = -2 (b0 a^2 + b1 a^3 + b2 a^4).
Pre-registered readings: PREREGISTRATION.md (same folder).
"""
import math, sys
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

U0 = 0.8776813811986843
A_BARE = 1/(4*math.pi)
A_LM = A_BARE/U0            # 0.09067
A_SV = A_BARE/U0**2         # 0.10330
LREPO = 38.44               # ln(M_Pl/v) used by the repo note
DT = math.log(A_LM)         # -2.4006 (rung log-interval)
MPL = 1.2209e19
V = 246.28

def bs(n):
    return (11-2*n/3, 102-38*n/3, 2857/2-5033*n/18+325*n*n/54)

def rhs_alpha(n, loops):
    b0, b1, b2 = bs(n)
    def f(t, y):
        a = y[0]/(4*math.pi)
        s = b0*a**2
        if loops >= 2: s += b1*a**3
        if loops >= 3: s += b2*a**4
        return [4*math.pi*(-2*s)]
    return f

def integrate(alpha0, t0, t1, n, loops, amax=1.0):
    """integrate downward from t0 to t1 (t1<t0) with fixed n; stop if alpha reaches amax. returns (alpha_end, t_end, hit)"""
    f = rhs_alpha(n, loops)
    def ev(t, y): return y[0]-amax
    ev.terminal = True; ev.direction = 1
    def ev0(t, y): return y[0]-1e-6
    ev0.terminal = True; ev0.direction = -1
    sol = solve_ivp(f, [t0, t1], [alpha0], events=[ev, ev0], rtol=1e-10, atol=1e-14, max_step=0.05)
    if sol.status == 1 and len(sol.t_events[0]) > 0:
        return amax, sol.t_events[0][0], True
    return sol.y[0][-1], sol.t[-1], False

def staircase(alpha0, thresholds, ns, loops, tend, amax=1.0):
    """thresholds: list of t_k (descending, negative) at which n switches to ns[k+1]; ns has len(thresholds)+1"""
    t = 0.0; a = alpha0; traj = [(0.0, a, ns[0])]
    edges = list(thresholds) + [tend]
    for k, te in enumerate(edges):
        a, tt, hit = integrate(a, t, te, ns[k], loops, amax)
        if hit:
            return a, tt, True, traj
        t = te
        traj.append((t, a, ns[k+1] if k+1 < len(ns) else None))
    return a, t, False, traj

out = []
def P(*args):
    s = " ".join(str(x) for x in args)
    print(s); out.append(s)

P("== constants: alpha_bare=%.5f alpha_LM=%.5f alpha_s(v)=%.5f  rung dt=%.4f  16 rungs=%.3f  L(v)=%.3f  ln(M_Pl/v) exact=%.3f" %
  (A_BARE, A_LM, A_SV, DT, 16*DT, LREPO, math.log(MPL/V)))
tar_ratio = 1.208/1.067
P("targets: alpha(v)=0.1033 (repo alpha_s(v)); from g-ratio 1.132 => alpha(v)=%.4f if started at alpha_LM" % (A_LM*tar_ratio**2))

# ---------------- Block A
P("\n== A. constant content n at the cutoff alpha=alpha_LM: fate below M_Pl (marker alpha=1)")
P("n  | b0     b1      b2     | 2-loop FP a*  | 1-loop            | 2-loop             | 3-loop")
def fate(n, loops, a0=A_LM):
    a, t, hit = integrate(a0, 0.0, -300.0, n, loops, amax=1.0)
    if hit: return "Lambda/Mpl=%.1e (%.1f efolds)" % (math.exp(t), -t)
    return "no pole; alpha(-300)=%.4f" % a
for n in range(0, 17):
    b0, b1, b2 = bs(n)
    fp = (-4*math.pi*b0/b1) if b1 < 0 else float('nan')
    P("%2d | %6.2f %7.2f %8.1f | %s | %s | %s | %s" % (n, b0, b1, b2, ("%.3f" % fp) if b1 < 0 else "  -  ", fate(n, 1), fate(n, 2), fate(n, 3)))

P("\n-- A2. same table, starting from alpha_bare = 0.0796 and from a Standard-Model-like continuum value 0.0187, for n=6")
for a0 in (A_BARE, 0.0187):
    for n in (6,):
        P("a0=%.4f n=%d: 2-loop %s" % (a0, n, fate(n, 2, a0)))
# what lattice coupling makes n=6, n=0 reach 1 at Lambda=0.2 GeV ?
def alpha_uv_for_lambda(n, loops, lam_gev=0.4):
    tgt = math.log(lam_gev/MPL)
    def g(a0):
        a, t, hit = integrate(a0, 0.0, tgt, n, loops, amax=1.0)
        return (a-1.0) if not hit else (0.0 if abs(t-tgt) < 1e-3 else 1.0)
    # bisect on a0: larger a0 -> pole earlier
    lo, hi = 0.005, 0.2
    for _ in range(60):
        mid = 0.5*(lo+hi)
        a, t, hit = integrate(mid, 0.0, tgt, n, loops, amax=1.0)
        if hit: hi = mid
        else: lo = mid
    return 0.5*(lo+hi)
for n in (0, 6):
    for loops in (1, 2):
        a0 = alpha_uv_for_lambda(n, loops)
        P("n=%d loops=%d: alpha(M_Pl) that puts alpha=1 at 0.4 GeV: %.4f  (beta_lat=6/g^2 = %.1f; repo alpha_LM=%.4f)" % (n, loops, a0, 6/(4*math.pi*a0), A_LM))

# ---------------- Block B
P("\n== B. repo staircase mu_k = M_Pl alpha_LM^k, n = 16-k (k=0..15), start alpha_LM; marker alpha=1")
def repo_stair(loops, a0=A_LM, dt=DT, amax=1.0):
    thr = [dt*(k+1) for k in range(15)]      # t_1..t_15 ; n changes 16->15 at t_1 ...
    ns = [16-k for k in range(16)]           # 16,15,...,1
    tend = dt*16
    return staircase(a0, thr, ns, loops, tend, amax)
for loops in (1, 2, 3):
    a, t, hit, traj = repo_stair(loops)
    if hit:
        P("loops=%d: alpha reaches 1 at t=%.2f (%.2f rungs down; mu=%.2e GeV) -> pole before v" % (loops, t, t/DT, MPL*math.exp(t)))
    else:
        P("loops=%d: reaches rung 16 (mu=%.2e GeV): alpha(mu_16)=%.4f" % (loops, MPL*math.exp(t), a))
    P("   alpha at rung edges:", " ".join("%.3f" % x[1] for x in traj))
# with the loose marker (alpha_max = 5) to see where the pole really is
for loops in (2, 3):
    a, t, hit, traj = repo_stair(loops, amax=5.0)
    P("loops=%d alpha_max=5: %s at t=%.2f (rung %.2f)" % (loops, "pole" if hit else "no pole", t, t/DT))

# control indicators along constant-n at the actual couplings on the staircase
P("\n-- B2. control indicator on the 2-loop staircase: |b1 a|/b0 and |b2 a^2|/|b1 a| at each rung edge (a=alpha/4pi)")
a, t, hit, traj = repo_stair(2, amax=5.0)
for (tk, ak, nk) in traj:
    if nk is None: continue
    b0, b1, b2 = bs(nk); aa = ak/(4*math.pi)
    P("t=%7.2f alpha=%.3f n=%2d  |b1 a/b0|=%6.2f  |b2 a/b1|=%6.2f   effective 2-loop b=%7.3f" % (tk, ak, nk, abs(b1*aa/b0), abs(b2*aa/b1), b0+b1*aa))

# ---------------- Block C
P("\n== C. one-threshold family, 2-loop: n=16 for t>-s, then n_low; alpha(v) at t=-L (marker alpha=1 => 'pole')")
def one_thr(s, n_low, loops=2, a0=A_LM, tend=-LREPO):
    a, t, hit, traj = staircase(a0, [-s], [16, n_low], loops, tend, amax=1.0)
    return (None if hit else a), t
for n_low in (15, 12, 6, 0):
    row = []
    for s in np.linspace(0, LREPO, 9):
        a, t = one_thr(s, n_low)
        row.append("s=%5.1f:%s" % (s, ("pole" if a is None else "%.4f" % a)))
    P("n_low=%2d  " % n_low + "  ".join(row))
def solve_s(n_low, target, loops=2):
    def g(s):
        a, t = one_thr(s, n_low, loops)
        return 1.0 - target if a is None else a - target
    ss = np.linspace(0, LREPO, 200)
    vals = [g(s) for s in ss]
    roots = []
    for i in range(len(ss)-1):
        if vals[i]*vals[i+1] < 0:
            try: roots.append(brentq(g, ss[i], ss[i+1], xtol=1e-6))
            except Exception: pass
    return roots
for n_low in (15, 12, 6, 0):
    for target in (0.1033, 0.1162):
        r = solve_s(n_low, target)
        for s in r:
            # sensitivity: change in alpha(v) per unit s
            a1, _ = one_thr(s+0.05, n_low); a0_, _ = one_thr(s-0.05, n_low)
            sens = ((a1 if a1 is not None else float('nan')) - (a0_ if a0_ is not None else float('nan')))/0.1
            P("n_low=%2d target %.4f: threshold at s=%.3f e-folds below M_Pl (mu_1=%.2e GeV), d alpha(v)/ds = %.4f/efold" % (n_low, target, s, MPL*math.exp(-s), sens))
        if not r:
            P("n_low=%2d target %.4f: NO root" % (n_low, target))

# ---------------- Block D
P("\n== D. continuous n: ln(M_Pl/Lambda_1) with Lambda_1 defined by alpha=1, start alpha_LM (2-loop and 3-loop)")
ns = np.arange(8.0, 16.001, 0.5)
res = {}
for loops in (2, 3):
    rows = []
    for n in ns:
        a, t, hit = integrate(A_LM, 0.0, -400.0, n, loops, amax=1.0)
        rows.append((n, -t if hit else float('inf')))
    res[loops] = rows
    P("loops=%d: " % loops + " ".join("n=%.1f:%s" % (n, ("%.1f" % e) if e < 1e9 else "inf") for n, e in rows))
# window search: target ln(M/Lambda) in [ln(1e19), ln(1e21)] = [43.7, 48.4]
def efolds(n, loops):
    a, t, hit = integrate(A_LM, 0.0, -400.0, n, loops, amax=1.0)
    return -t if hit else float('inf')
for loops in (2, 3):
    nn = np.linspace(8.0, 16.0, 801)
    ee = np.array([efolds(x, loops) for x in nn])
    inwin = (ee >= 43.7) & (ee <= 48.4)
    if inwin.any():
        P("loops=%d: n-window giving Lambda in [1e-21,1e-19] M_Pl: n in [%.4f, %.4f] (width %.4f); dn/d(ln Lambda) ~ %.4f per e-fold" %
          (loops, nn[inwin].min(), nn[inwin].max(), nn[inwin].max()-nn[inwin].min(), (nn[inwin].max()-nn[inwin].min())/(48.4-43.7)))
    else:
        finite = ee < 1e9
        P("loops=%d: no n in grid gives window; finite range e-folds %.1f..%.1f; last finite n=%.3f" % (loops, ee[finite].min(), ee[finite].max(), nn[finite].max()))
    # integer neighbours
    P("loops=%d integer n=8..12 e-folds:" % loops + " ".join("%d:%s" % (n, ("%.1f" % efolds(n, loops)) if efolds(n, loops) < 1e9 else "inf") for n in range(8, 13)))
# critical n (2-loop): largest n with a pole; scan finer
for loops in (2, 3):
    lo, hi = 8.0, 16.0
    for _ in range(50):
        mid = 0.5*(lo+hi)
        if efolds(mid, loops) < 1e9: lo = mid
        else: hi = mid
    P("loops=%d: critical n_c (pole exists below, conformal above) = %.5f ; e-folds at n_c-0.01: %.1f, at n_c-0.1: %.1f, at n_c-0.5: %.1f" %
      (loops, lo, efolds(lo-0.01, loops), efolds(lo-0.1, loops), efolds(lo-0.5, loops)))

# ---------------- Block E
P("\n== E. self-consistency of the frozen rung ratio with a running coupling (2- and 3-loop)")
P("   Repo: v/M_Pl = (7/8)^(1/4) * alpha_LM^16, i.e. every rung has ratio alpha_LM (=coupling at M_Pl).")
P("   Test: let rung k have ratio alpha(mu_k) (the running coupling at that rung, same object) and integrate with the given content.")
def selfconsistent(loops, content, nrung=16, amax=1.0):
    t = 0.0; a = A_LM; tk = [0.0]; ak = [a]
    for k in range(nrung):
        if a >= 1: return tk, ak, "ratio>=1 at rung %d" % k
        dt = math.log(a)
        n = content(k)
        a2, t2, hit = integrate(a, t, t+dt, n, loops, amax)
        if hit: return tk, ak, "pole inside rung %d at t=%.2f" % (k, t2)
        t += dt; a = a2; tk.append(t); ak.append(a)
    return tk, ak, "done"
for name, content in (("repo staircase n=16-k", lambda k: 16-k), ("constant n=16", lambda k: 16), ("constant n=15", lambda k: 15)):
    for loops in (1, 2, 3):
        tk, ak, msg = selfconsistent(loops, content)
        P("%-22s loops=%d: %s; span t=%.2f (frozen %.2f) implied v/M_Pl=%.2e (frozen %.2e); alpha_16=%.3f; alpha_k: %s" %
          (name, loops, msg, tk[-1], 16*DT, math.exp(tk[-1]), math.exp(16*DT), ak[-1], " ".join("%.3f" % x for x in ak[::3])))

open(sys.argv[1] if len(sys.argv) > 1 else "t30_flow_output.txt", "w").write("\n".join(out)+"\n")
