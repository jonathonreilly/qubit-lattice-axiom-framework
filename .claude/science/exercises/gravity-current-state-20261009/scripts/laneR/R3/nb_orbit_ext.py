# N-b extension (added after the first run, before interpreting): larger T in 4D, local slopes
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("nb", "nb_orbit.py")
src = open("nb_orbit.py").read().split("for d, Ts in")[0]
exec(src)
for kind in ["inv", "noninv"]:
    Ts = [11, 16, 22, 30]; vals = []
    for T in Ts:
        I, se = I_pairs(T, 4, kind, M=6_000_000); vals.append(I)
        print(f"d=4 {kind:6s} T={T:3d}: I={I:.4e} +- {se:.1e}")
    sl = [np.log(vals[i+1]/vals[i])/np.log(Ts[i+1]/Ts[i]) for i in range(len(Ts)-1)]
    print("   local slopes:", [round(s, 2) for s in sl])
