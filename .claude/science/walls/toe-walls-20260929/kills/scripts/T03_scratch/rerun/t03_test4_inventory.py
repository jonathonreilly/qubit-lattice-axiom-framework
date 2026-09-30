"""T03 Test 4: energy inventory of sharp per-site records (arithmetic on probe 1 T4 numbers; reference constants).
Sharp birth cost (walker sea, T4(b)) = 2.387602 t with t = hbar c / a; 96% stays as the record's own energy (T4(d)).
Reference constants (not premises): hbar c = 3.16153e-26 J m, l_P = 1.616255e-35 m, R_obs = 4.4e26 m (comoving radius),
age = 4.35e17 s, universe mass-energy (baryons + dark matter) taken as 1e70 J (baryons alone 1.4e70 J: 1.5e53 kg),
baryons ~ 1e80.
"""
import math
hbarc = 3.16153e-26; lP = 1.616255e-35; R = 4.4e26; age = 4.35e17; c = 2.998e8
E_univ = 1e70; n_baryon = 1e80
cost_factor = 2.387602
V = 4 / 3 * math.pi * R**3
print("a [m]        cost/birth [J]   max births      sites in universe   ticks/site   births needed:  1 per site | 1 per baryon | 1 per tick-site")
for a in (lP, 1e-19, 1e-17, 1e-15, 1e-12, 1e-9, 1e-6, 1e-4):
    cost = cost_factor * hbarc / a
    nmax = E_univ / cost
    sites = V / a**3
    ticks = age / (a / c)
    print(f"{a:9.3e}   {cost:12.3e}   {nmax:11.3e}   {sites:14.3e}   {ticks:10.3e}   "
          f"{sites/nmax:9.1e}x | {n_baryon/nmax:9.1e}x | {sites*ticks/nmax:9.1e}x   (shortfall factor; <1 means it fits)")
# largest energy-affordable birth counts -> smallest spacing allowed
a_baryon = cost_factor * hbarc * n_baryon / E_univ
a_site = (cost_factor * hbarc * V / E_univ) ** 0.25
print(f"\nSharp locks fit the universe's mass-energy: one per baryon only if a >= {a_baryon:.2e} m;  one per site only if a >= {a_site:.2e} m")
ok = a_baryon > 1e-16 and a_site > 1e-5
print("TOTAL: PASS=%d FAIL=%d" % (int(ok), int(not ok)))
