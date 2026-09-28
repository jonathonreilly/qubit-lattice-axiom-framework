import sys, time
import numpy as np
src = open("p24b_runner.py").read()
g = {"__name__": "compprobe"}
sys.argv = ["x"]
exec(src[:src.index("# ---------------------------------------------------------------- 1. exact 2^3 control")], g)
Ice, Projector, loop_vmc, ALPHA, energy_run = g["Ice"], g["Projector"], g["loop_vmc"], g["ALPHA"], g["energy_run"]
L = int(sys.argv[1]) if len(sys.argv) > 1 else 16
ice = Ice(L)
z = np.zeros(ice.nl)
t0 = time.time()
for label in ("canonical start", "loop-VMC start"):
    for sd in (1, 2):
        rr = np.random.default_rng(100 + sd)
        if label == "canonical start":
            init = [ice.sector_state(0)]
        else:
            init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, np.zeros((1, ice.nl), complex), 200 + sd)
        out, res = energy_run(pr, init, 960, 4000, 0.015, 1000, rr, z, z, Lcs=(0,))
        e = res["e"]
        w1, w2 = e[1000:2000].mean(), e[2000:4000].mean()
        print(f"L {L} {label} seed {sd}: u over [15,30) {-w1 / ice.np_:.5f}, over [30,60) {-w2 / ice.np_:.5f}  {time.time() - t0:.0f} s", flush=True)
