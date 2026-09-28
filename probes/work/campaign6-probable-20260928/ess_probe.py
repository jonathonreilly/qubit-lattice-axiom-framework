import sys, time
import numpy as np
src = open("p24b_runner.py").read()
g = {"__name__": "essprobe"}
sys.argv = ["x"]
exec(src[:src.index("# ---------------------------------------------------------------- 1. exact 2^3 control")], g)
Ice, Projector, loop_vmc, ALPHA = g["Ice"], g["Projector"], g["loop_vmc"], g["ALPHA"]
nb_init, nb_init_rates, nb_walk_f = g["nb_init"], g["nb_init_rates"], g["nb_walk_f"]
for L in (8, 12, 16):
    for dtau in (0.015, 0.005):
        ice = Ice(L); rr = np.random.default_rng(5)
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, np.zeros((1, ice.nl), complex), 17)
        n_w = 960; hl = np.zeros(ice.nl); bl = np.zeros(ice.nl)
        picks0 = rr.integers(len(init), size=n_w)
        sig = np.array([init[k] for k in picks0], dtype=np.int8)
        C = np.zeros((n_w, ice.np_), dtype=np.int8); flp = np.zeros((n_w, ice.np_), dtype=np.bool_); dN = np.zeros((n_w, ice.np_), dtype=np.int8)
        nflp = np.zeros(n_w, dtype=np.int64)
        nb_init(sig, C, flp, dN, nflp, pr.plaq, pr.sign, pr.A, pr.M, pr.dyn)
        rate = np.zeros((n_w, ice.np_)); Fh = np.zeros(n_w)
        nb_init_rates(sig, flp, dN, rate, Fh, pr.plaq, pr.exptab, hl, bl)
        Om = np.zeros((n_w, 1), dtype=np.complex128); PHz = np.zeros((ice.nl, 1), dtype=np.complex128)
        logw = np.zeros(n_w); ELend = np.zeros(n_w)
        ess = []
        ngen = int(round(6.0 / dtau))
        for gg in range(ngen):
            nb_walk_f(sig, C, flp, dN, rate, nflp, Fh, Om, pr.plaq, pr.A, pr.M, pr.dyn, pr.exptab, pr.V, hl, bl, dtau, PHz,
                      pr.stamp, pr.tick, pr.sbuf, pr.rbuf, logw, ELend)
            mx = logw.max(); w = np.exp(logw - mx)
            ess.append(w.sum() ** 2 / (w ** 2).sum() / n_w)
            cum = np.cumsum(w / w.sum())
            picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rr.random()) / n_w), n_w - 1)
            sig, C, flp, dN, rate, nflp, Fh = sig[picks], C[picks], flp[picks], dN[picks], rate[picks], nflp[picks], Fh[picks]
        ess = np.array(ess[len(ess) // 2:])
        print(f"L {L} dtau {dtau}: effective sample fraction per generation mean {ess.mean():.3f}, min {ess.min():.3f}", flush=True)
