"""T7b — the energy, measured properly.
The verified symbol is  m^2 + sum_d sin^2 k_d .  Continue the temporal momentum
k_t -> i*omega :  sin^2(i om) = -sinh^2 om, so the on-shell pole sits at
        sinh^2(omega) = m^2 + sum_(spatial) sin^2 k .
sin^2 k_t = (1 - cos 2k_t)/2 couples t to t +- 2 (the Kahler/staggered even-odd
split), so the propagator must be measured on ONE sublattice, in steps of 2.
Measure the decay of the exact lattice propagator and compare - no fitting."""
import mpmath as mp
mp.mp.dps = 40
m = mp.mpf(3)/4
T = 96
for pmode, Lx in ((0, 4), (1, 4), (1, 8)):
    s2 = mp.sin(2*mp.pi*pmode/Lx)**2
    def G(t):
        tot = mp.mpf(0)
        for n in range(T):
            k = 2*mp.pi*n/T
            tot += mp.cos(k*t)/(m**2 + mp.sin(k)**2 + s2)
        return tot/T
    # decay per 2 steps, taken well away from t=0 and t=T/2
    ts = [10, 12, 14, 16]
    om = [mp.log(G(t)/G(t+2))/2 for t in ts]
    pred = mp.asinh(mp.sqrt(m**2 + s2))
    rel = mp.sqrt(m**2 + s2)
    print(f"p-mode {pmode}/{Lx}:  measured omega = {[mp.nstr(o, 10) for o in om]}", flush=True)
    print(f"              predicted arcsinh(sqrt(m^2+p^2)) = {mp.nstr(pred, 10)}"
          f"   max|diff| = {mp.nstr(max(abs(o-pred) for o in om), 6)}", flush=True)
    print(f"              continuum relativistic sqrt(m^2+p^2) = {mp.nstr(rel, 10)}", flush=True)
# and the small-mass/small-momentum limit: does arcsinh -> sqrt ?
print("\nsmall-argument limit (the relativistic regime):", flush=True)
for mm in (mp.mpf('0.2'), mp.mpf('0.05'), mp.mpf('0.01')):
    om = mp.asinh(mm); print(f"   m={mp.nstr(mm,4)}: omega={mp.nstr(om,10)}  m={mp.nstr(mm,10)}"
                             f"  ratio={mp.nstr(om/mm,10)}", flush=True)
