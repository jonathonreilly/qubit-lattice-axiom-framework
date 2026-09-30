"""Kill-check of T32's 'flow stops at alpha* = 0.042 and nothing confines' (n = 16 massless tastes).
Question: how many e-folds does the two-loop flow need to reach alpha*, versus the ~44 e-folds between M_Pl and 1 GeV?
Same convention as the attack's nf_fixed_point.py: dalpha/dlnmu = -alpha^2/(2 pi) [ b0 + b1 alpha/(4 pi) ].
"""
import math
def run(n, a0, efolds_max=500.0, dt=0.01):
    b0 = 11 - 2*n/3; b1 = 102 - 38*n/3
    a = a0; t = 0.0   # t = ln(M_Pl/mu)
    astar = -4*math.pi*b0/b1 if (b1<0 and b0>0) else None
    out = {}
    marks = [5, 10, 20, 39.4, 44, 100, 200, 500]
    mi = 0
    while t < efolds_max:
        da = -a*a/(2*math.pi)*(b0 + b1*a/(4*math.pi))     # dalpha/dln mu
        a -= da*dt                                        # step to lower mu
        t += dt
        if a > 50: break
        if mi < len(marks) and t >= marks[mi]:
            out[marks[mi]] = a; mi += 1
    return astar, out
for a0 in (1/(4*math.pi), 0.0907):
    astar, out = run(16, a0)
    print("n=16 alpha0=%.4f alpha*=%.4f" % (a0, astar))
    for k, v in out.items():
        print("   after %6.1f e-folds down from M_Pl (%.1f decades): alpha = %.4f" % (k, k/math.log(10), v))
    # e-folds needed to get within 10% of the gap alpha0-alpha*
    b0 = 11 - 32/3; b1 = 102 - 38*16/3
    a = a0; t = 0; dt=0.01
    target = astar + 0.1*(a0-astar)
    while a > target and t < 1e5:
        da = -a*a/(2*math.pi)*(b0 + b1*a/(4*math.pi)); a -= da*dt; t += dt
    print("   e-folds to cover 90%% of the way to alpha*: %.0f  (= %.0f decades)" % (t, t/math.log(10)))
print("ln(M_Pl / 1 GeV) = %.1f e-folds = %.1f decades" % (math.log(1.22e19), math.log10(1.22e19)))
