"""Lane RG probe G2, part 5: decay-law fits of the vacuum energy-integrated eps_D(r) (binomial filter)
and of the shell maxPhi_U; exponential vs power law; Readout Q."""
import numpy as np, glob, re
L16 = np.log10(16)
for fn in sorted(glob.glob('g2_shells_*.out')):
    txt = open(fn).read()
    vac = txt.split('## energy-integrated')[1]
    rows = [l.split() for l in vac.splitlines() if l.strip().startswith('(a)')]
    r = np.array([float(x[1]) for x in rows]); y = np.array([float(x[2]) for x in rows])
    m = r >= 8
    # exponential * power: y = a + b r + p log10 r
    A = np.vstack([np.ones(m.sum()), r[m], np.log10(r[m])]).T
    (a, b, p), res, *_ = np.linalg.lstsq(A, y[m], rcond=None)
    # pure power law y = a + p log10 r
    Ap = np.vstack([np.ones(m.sum()), np.log10(r[m])]).T
    (ap, pp), resp, *_ = np.linalg.lstsq(Ap, y[m], rcond=None)
    # pure exponential
    Ae = np.vstack([np.ones(m.sum()), r[m]]).T
    (ae, be), rese, *_ = np.linalg.lstsq(Ae, y[m], rcond=None)
    rms = lambda M, c: np.sqrt(np.mean((M @ c - y[m]) ** 2))
    print(f"{fn}: exp*pow fit: rate {-b*np.log(10):.3f}/r (log10 {-b:.3f}; sup rate 4ln2=2.773 / {L16:.3f}), power {p:.2f}, rms {rms(A,(a,b,p)):.3f} dec | "
          f"pure exp: rate {-be*np.log(10):.3f}, rms {rms(Ae,(ae,be)):.3f} | pure power: r^{pp:.1f}, rms {rms(Ap,(ap,pp)):.2f} dec")
    for X in [10, 50, 100]:
        # solve a + b r + p log10 r = -X
        rr = np.linspace(1, 400, 400000); yy = a + b * rr + p * np.log10(rr)
        rstar = rr[np.argmin(np.abs(yy + X))]
        print(f"    eps_D = 1e-{X}: r* = {rstar:.1f} (vacuum fit);  sup bound 16^-r: r* = {X/L16:.1f}")
