"""R6-3 (b): table of J(M) for the unit diamond and unit truncated past cone, Plancherel check,
large-|M| asymptotics. Saves r63_Jtable.npz."""
import numpy as np, time, sys
sys.path.insert(0, '.')
from r63_formfactor import J

t0 = time.time()
absM = np.logspace(-3, 9, 97)          # 8 per decade
res = {}
for Wn in ('D', 'P'):
    Jt = np.array([J(-m, Wn) for m in absM])
    Js = np.array([J(+m, Wn) for m in absM])
    res[Wn] = (Jt, Js)
    print("%s done, %.0f s" % (Wn, time.time()-t0), flush=True)
np.savez('r63_Jtable.npz', absM=absM, DJt=res['D'][0], DJs=res['D'][1], PJt=res['P'][0], PJs=res['P'][1])

vol = {'D': np.pi/24, 'P': np.pi/3}
for Wn in ('D', 'P'):
    Jt, Js = res[Wn]
    # int J dM = int J |M| dln|M| (each sign) + small-|M| piece ~ J(0)*2e-3
    lnM = np.log(absM)
    I = np.trapezoid(Jt*absM, lnM) + np.trapezoid(Js*absM, lnM) + 0.5*(Jt[0]+Js[0])*2*absM[0]
    # tail beyond 1e9 (D: ~ A ln M/M^2 -> A(ln M + 1)/M ; P: ~ B M^-1.5 -> 2B M^-0.5)
    print("\n== %s: Plancherel  int J dM = %.6f   vs (2pi)^4 |W| = %.6f   ratio %.5f  (tail beyond 1e9 not added)" %
          (Wn, I, (2*np.pi)**4*vol[Wn], I/((2*np.pi)**4*vol[Wn])))
    print("   J(M->0-) = %.5f   J(M->0+) = %.5f" % (Jt[0], Js[0]))
    print("   |M|        J_timelike     J_spacelike    M^2 J_tl/ln|M|  M^2 J_sl/ln|M|   |M|^1.5 J_tl   |M|^1.5 J_sl")
    for i in range(0, len(absM), 4):
        m = absM[i]
        a = m**2*Jt[i]/np.log(m) if m > 1.5 else np.nan
        b = m**2*Js[i]/np.log(m) if m > 1.5 else np.nan
        print("   %9.3e  %12.5e  %12.5e  %12.4f  %12.4f  %12.4f  %12.4f" % (m, Jt[i], Js[i], a, b, m**1.5*Jt[i], m**1.5*Js[i]))
    # local log-log slopes at large M
    sl_t = np.gradient(np.log(Jt), np.log(absM)); sl_s = np.gradient(np.log(Js), np.log(absM))
    print("   local slopes d lnJ/d ln|M| at |M| = 1e2,1e4,1e6,1e8: tl", [round(sl_t[np.argmin(abs(absM-x))], 4) for x in (1e2, 1e4, 1e6, 1e8)],
          " sl", [round(sl_s[np.argmin(abs(absM-x))], 4) for x in (1e2, 1e4, 1e6, 1e8)])
    if Wn == 'D':
        # fit M^2 J = A ln M + B over 1e4..1e9
        sel = absM >= 1e4
        for nm, Jx in (('tl', Jt), ('sl', Js)):
            A, B = np.polyfit(np.log(absM[sel]), absM[sel]**2*Jx[sel], 1)
            print("   fit M^2 J_%s = A ln|M| + B over 1e4..1e9: A = %.3f (16 pi^3 = %.3f), B = %.2f" % (nm, A, 16*np.pi**3, B))
    else:
        sel = absM >= 1e4
        for nm, Jx in (('tl', Jt), ('sl', Js)):
            print("   |M|^1.5 J_%s at 1e6, 1e8, 1e9: %.3f %.3f %.3f   [(2pi)^3 (4pi/3) = %.3f]" % (nm,
                  (absM**1.5*Jx)[np.argmin(abs(absM-1e6))], (absM**1.5*Jx)[np.argmin(abs(absM-1e8))], (absM**1.5*Jx)[-1], (2*np.pi)**3*4*np.pi/3))
print("elapsed %.0f s" % (time.time()-t0))
