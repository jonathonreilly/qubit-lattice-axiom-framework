import numpy as np
src = open("l3_phi4_energy_current.py").read().split("for lam in (0.0, 0.5, 2.0):")[0]
exec(src)
# per-trajectory normalized tail averages, for error bars
def tail(lam, ntraj, tmax, t0):
    vals = []
    for i in range(ntraj):
        tt, C, ra, drift = run(lam, ntraj=1, tmax=tmax)
        vals.append(np.mean(C[int(t0/dt):]))
    vals = np.array(vals)
    return vals.mean(), vals.std(ddof=1)/np.sqrt(len(vals))
for lam in (0.0, 2.0, 4.0):
    m, e = tail(lam, 24, 150.0, 75.0)
    print(f"lam={lam}: mean over t in [75,150] of J(t).J(0)/J(0)^2 (24 traj): {m:.3f} +- {e:.3f}")
