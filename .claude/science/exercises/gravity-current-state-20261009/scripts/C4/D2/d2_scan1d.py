"""D2 (a): 1D one-loop dressed band, scan of band x sound speed x vertex power x coupling.
SC = self-consistent quasiparticle propagator; BW1 = bare propagator."""
import numpy as np, sys, time
from d2_common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
W = [np.pi/4, np.pi/2, np.pi]
print(f"# N={N}. columns: band c a g2 mode | E0 Epi | Z0 Zpi | gap_pi | p(d=1,4,16,64 steps) | kink=(D/d at d=dk)/(SLAC slope) | SLAC dev/bw w=pi/4,pi/2,pi (bare in [])")
for kind in ['TB', 'KG']:
    kb = TWO_PI*np.arange(N//2+1)/N; Eb = eps_band(kind, kb)
    bare = [slac_fit(kb, Eb, w)[2] for w in W]
    for c in [1.5, 1.0, 0.4]:
        for a in [0.0, 0.25, 0.5, 1.0]:
            for g2 in [0.05, 0.3, 1.0]:
                for sc in [False, True]:
                    t = time.time()
                    r = dressed_band_1d(kind, N, c, g2, a, sc=sc, maxsc=150)
                    fm = face_measures(r['k'], r['E'])
                    ps = [row[3] for row in fm]
                    pp = [ps[i] for i in (0, 2, 4, 6) if i < len(ps)]
                    fits = [slac_fit(r['k'], r['E'], w) for w in W]
                    kink = fits[0][4]
                    print(f"{kind} c={c} a={a} g2={g2} {'SC ' if sc else 'BW1'} | "
                          f"{r['E'][0]:.5f} {r['E'][-1]:.5f} | {r['Z'][0]:.4f} {r['Z'][-1]:.4f} | {r['gap'][-1]:.2e} | "
                          + " ".join(f"{p:.3f}" for p in pp) + f" | {kink:.4f} | "
                          + " ".join(f"{f[2]:.4f}[{b:.4f}]" for f, b in zip(fits, bare))
                          + (f" | it={r['it']} res={r['res']:.1e}" if sc else "") + f" t={time.time()-t:.1f}s", flush=True)
