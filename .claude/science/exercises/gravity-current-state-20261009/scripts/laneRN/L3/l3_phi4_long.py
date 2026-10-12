import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("p", "l3_phi4_energy_current.py")
src = open("l3_phi4_energy_current.py").read().split("for lam in (0.0, 0.5, 2.0):")[0]
exec(src)
for lam, tmax in ((0.5, 400.0), (2.0, 200.0)):
    tt, C, ra, drift = run(lam, ntraj=8, tmax=tmax)
    pick = [int(x/dt)-1 for x in (50, 100, 150, 200, 300, 400) if x <= tmax]
    print(f"lam={lam}: C at t={[x for x in (50,100,150,200,300,400) if x<=tmax]}: {np.round(C[pick],3)}; "
          f"avg over last half: {np.mean(C[len(C)//2:]):.3f}; time-average [0,{tmax:.0f}]: {ra[-1]:.3f}; drift {drift:.1e}")
