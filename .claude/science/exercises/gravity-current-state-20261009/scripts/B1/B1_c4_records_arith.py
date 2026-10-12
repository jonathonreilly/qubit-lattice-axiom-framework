"""B1 check c4: two arithmetic checks on the owner's record readings (CHECKED arithmetic; readings in report).
(i) Records as spacetime events at Planck density: how many events per nucleon per second?
    If each event 'locks' a matter possibility with disturbance probability q, heating ~ rate*q.
(ii) 'A sealed box fills until frozen = black hole': one record per Planck cell (volume count)
    versus Bekenstein-Hawking entropy A/(4 l_P^2) for a solar-mass hole.
"""
import math
lP = 1.616e-35; tP = 5.391e-44
rate_density = 1 / (lP**3 * tP)            # events per m^3 per s at density l_P^-4
V_nucleon = (4/3) * math.pi * (0.84e-15)**3
print(f"(i) event rate density = {rate_density:.2e} /m^3/s; per nucleon volume: {rate_density*V_nucleon:.2e} /s")
print(f"    per kg of matter (~6e26 nucleons, nucleon volumes only): {rate_density*V_nucleon*6.0e26:.2e} /s")
# viability map birth-rate bound: <= 2e-5 sharp births per kg per s (at a=1e-19 m) -- quoted from map
print(f"    => disturbance probability per event must be <~ {2e-5/(rate_density*V_nucleon*6.0e26):.1e}"
      " to respect the map's 2e-5 /kg/s birth-rate bound (bound quoted, not re-derived)")
G = 6.674e-11; c = 2.998e8; Msun = 1.989e30
rs = 2 * G * Msun / c**2
A = 4 * math.pi * rs**2
S_BH = A / (4 * lP**2)
N_vol = (4/3) * math.pi * rs**3 / lP**3
print(f"(ii) solar-mass hole: r_s = {rs:.0f} m, S_BH = A/4l_P^2 = {S_BH:.2e}, Planck cells inside = {N_vol:.2e},"
      f" ratio = {N_vol/S_BH:.1e}")
