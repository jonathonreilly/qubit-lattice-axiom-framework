"""T63 test C: cone bound on growth of a record-occupied region on fixed Z^3 with one light cone (c=1 site/tick).
C1 simulate maximal cone-limited growth (Eden, attach prob q per tick per frontier site) and check N(t) <= (2t+1)^3.
C2 e-fold budget vs Hubble rate in Planck units."""
import numpy as np, math

def grow(L, q, T, nseeds_side=None, rng=None):
    """Synchronous cone-limited growth: at each tick every empty site with an occupied nearest neighbour becomes
    occupied with probability q. One seed at centre, or a cubic array of seeds (nseeds_side^3)."""
    occ = np.zeros((L, L, L), dtype=bool)
    c = L//2
    if nseeds_side is None: occ[c, c, c] = True
    else:
        step = L//nseeds_side
        for i in range(nseeds_side):
            for j in range(nseeds_side):
                for k in range(nseeds_side): occ[i*step, j*step, k*step] = True
    Ns = [occ.sum()]
    for t in range(T):
        nb = np.zeros_like(occ)
        for ax in range(3):
            nb |= np.roll(occ, 1, ax) | np.roll(occ, -1, ax)
        new = nb & ~occ & (rng.random(occ.shape) < q)
        occ = occ | new
        Ns.append(occ.sum())
    return np.array(Ns, dtype=float)

if __name__ == "__main__":
    rng = np.random.default_rng(1)
    T = 45; L = 2*T + 5
    print("C1 single seed, L=%d, T=%d ticks" % (L, T))
    print("   q     N(T)        (2T+1)^3     N/(2T+1)^3   max_t H_eff*t   with H_eff=(1/3) dlnN/dt, t>=5")
    for q in (1.0, 0.5, 0.2):
        Ns = grow(L, q, T, None, rng)
        t = np.arange(len(Ns))
        assert np.all(Ns <= (2*t+1)**3 + 1e-9)
        dlnN = np.gradient(np.log(Ns))
        H = dlnN/3.0
        sel = t >= 5
        print("  %.1f  %10.0f  %12.0f   %.3f        %.3f" % (q, Ns[-1], (2*T+1)**3, Ns[-1]/(2*T+1)**3, (H[sel]*t[sel]).max()))
    # exact octahedron count for q=1 (L1 ball): N = (2t+1)(2t^2+2t+3)/3
    t = T; print("   q=1 exact L1 ball (2t+1)(2t^2+2t+3)/3 = %d" % ((2*t+1)*(2*t*t+2*t+3)//3))
    # many seeds: total count N(t)/N(0) ratio bounded by (2t+1)^3 as well
    Ns = grow(60, 1.0, 12, 3, rng)
    print("C1b 27 seeds on L=60, q=1: N(12)/N(0) = %.0f  <= (2*12+1)^3 = %d" % (Ns[-1]/Ns[0], 25**3))

    print("\nC2 e-fold budget: N_e^max = ln(2t+1), t in Planck ticks (a^-1 = M_Pl, c = 1)")
    M_Pl = 1.221e19  # GeV, non-reduced
    hbar_GeV_s = 6.582e-25
    t_P = 5.391e-44
    print("   H [GeV]    H*a=H/M_Pl   e-fold time [ticks]   ticks for 60 e-folds   N_e^max in that time   shortfall")
    for H in (4.7e13, 1e13, 1e10, 1e6):
        Ha = H/M_Pl
        ticks = 60.0/Ha
        Nmax = math.log(2*ticks + 1)
        print("   %8.1e   %9.2e   %12.3e         %12.3e          %6.1f                 %.1fx" % (H, Ha, 1/Ha, ticks, Nmax, 60/Nmax))
    # H*a for which N_e = 60 fits: 60/Ha >= (e^60 - 1)/2
    Ha60 = 60.0/((math.exp(60)-1)/2)
    print("   H*a allowed for N_e = 60 on the cone: <= %.2e  (H <= %.2e GeV)" % (Ha60, Ha60*M_Pl))
    print("   Poisson-cell amplitude at that H: A_s ~ (H a)^3 = %.1e   vs observed 2.1e-9" % (Ha60**3))
    # occupied-count needed vs cone-limited count in ticks available (7e7 ticks @ H=1e13 GeV)
    ticks = 60.0/(1e13/M_Pl)
    print("   sites needed e^180 = %.1e ; cone-limited sites in %.2e ticks = (2t+1)^3 = %.1e" % (math.exp(180), ticks, (2*ticks+1)**3))
    # comoving Hubble radius: for a <= a0 + 2 c t (cone) the average adot <= 2, and 1/(aH) = 1/adot
    print("   cone bound gives a(t) <= a0 + 2t  => time-averaged adot <= 2 => comoving Hubble radius 1/(aH) = 1/adot >= 0.5 on average:")
    print("   no sustained shrinking of the comoving Hubble radius (horizon exit) unless adot grows, which needs superluminal site addition.")
