"""Driver for qmc.py: equilibration, measurements, binning.  Measurement definitions (shared with ED):

E_a(v) = sigma_{(v,a)}/2.  Ehat_a(q) = sum_v E_a(v) e^{-i q.v}.  P_E[a](q) = |Ehat_a(q)|^2 / N_v.
S_T(q) = sum_a P_E[a](q)   (S_L = 0 identically by the exact Gauss law, which is re-checked).
n_{v,o} = flippability of plaquette (v,o). P_n[o](q) = |sum_v (n_{v,o} - nbar_o) e^{-i q.v}|^2 / N_v.
Open-path estimators: middle state at T/2; E_mix = (V-g) <N_f(end)> (uniform trial, both ends);
E_mid = V <N_f(mid)> - <#kinks in (T/2-w, T/2+w)>/(2w) with w = T/8;
C(tau) = sum_{axis a} sum_{b != a} Re[Ehat_b(k_a) conj Ehat_b(k_a; tau)]/N_v, k_a = (2 pi/L) e_a, symmetric in +-tau.
"""
import os, sys, time, json
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from lattice import Lattice
import qmc


def config_obs(lat, sig):
    """diagonal observables of one configuration (sig: (..., nl) array)."""
    L = lat.L
    sig = np.asarray(sig)
    E = 0.5 * sig.reshape(sig.shape[:-1] + (L, L, L, 3)).astype(float)
    Ek = np.fft.fftn(E, axes=(-4, -3, -2))
    PE = (np.abs(Ek) ** 2) / lat.nv  # (..., L,L,L,3)
    circ = (sig[..., lat.plinks] * lat.psign).sum(axis=-1)
    n = (np.abs(circ) == 4).astype(float).reshape(sig.shape[:-1] + (L, L, L, 3))
    nk = np.fft.fftn(n - n.mean(axis=(-4, -3, -2), keepdims=True), axes=(-4, -3, -2))
    Pn = (np.abs(nk) ** 2) / lat.nv
    Nf = n.sum(axis=(-4, -3, -2, -1))
    return PE, Pn, Nf, Ek


def st_kmin(PE, L, m=1):
    """S_T at (2 pi m/L) e_a averaged over a."""
    v = 0.0
    for a in range(3):
        idx = [0, 0, 0]
        idx[a] = m % L
        v += PE[..., idx[0], idx[1], idx[2], :].sum(axis=-1)
    return v / 3.0


SHELLS = {"100": [(1, 0, 0)], "110": [(1, 1, 0), (1, -1, 0)], "111": [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)],
          "200": [(2, 0, 0)], "210": [(2, 1, 0), (2, -1, 0), (1, 2, 0), (-1, 2, 0)]}


def shell_vecs(m):
    import itertools
    out = set()
    for v in SHELLS[m]:
        for perm in itertools.permutations(range(3)):
            w = tuple(v[i] for i in perm)
            out.add(w)
            out.add(tuple(-x for x in w))
    return sorted(out)


def derived_bins(accPE, accPn, L):
    """per-bin derived quantities: S_T on momentum shells (units 2pi/L), flippability S_n(Q) for Q in {0,pi}^3,
    E-field S_aa(Q); returned as dict of arrays (nbins,)."""
    out = {}
    ST = accPE.sum(axis=-1)  # (nb, L, L, L)
    for m in SHELLS:
        vs = shell_vecs(m)
        if max(abs(x) for v in vs for x in v) * 2 > L:
            continue
        out["ST_" + m] = np.mean([ST[:, v[0] % L, v[1] % L, v[2] % L] for v in vs], axis=0)
    if L % 2 == 0:
        h = L // 2
        for Q in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 0, 1)]:
            idx = tuple(h * q for q in Q)
            key = "".join(str(q) for q in Q)
            out["Sn_" + key] = accPn[:, idx[0], idx[1], idx[2], :].sum(-1)
            for o in range(3):
                out[f"Sn{o}_" + key] = accPn[:, idx[0], idx[1], idx[2], o]
                out[f"SE{o}_" + key] = accPE[:, idx[0], idx[1], idx[2], o]
    # global maxima over q != 0 of bin-averaged spectra (diagnostic)
    Pn = accPn.mean(0).sum(-1)
    Pn[0, 0, 0] = 0
    out["Sn_max_q"] = np.array(np.unravel_index(np.argmax(Pn), Pn.shape))
    out["Sn_max"] = accPn.sum(-1)[(slice(None),) + tuple(out["Sn_max_q"])]
    return out


def binned_se(x, minbins=32):
    x = np.asarray(x, float)
    n = len(x)
    out = []
    b = 1
    while n // b >= minbins:
        m = n // b
        y = x[:m * b].reshape(m, b).mean(axis=1)
        out.append((b, y.std(ddof=1) / np.sqrt(m)))
        b *= 2
    se = max(s for _, s in out) if out else np.nan
    return x.mean(), se, out


class Sim:
    def __init__(self, L, V, T, g=1.0, mode=0, seed=1, cap=None, init=None):
        self.lat = lat = Lattice(L)
        self.L, self.V, self.T, self.g, self.mode = L, V, T, g, mode
        qmc.seed_rng(seed)
        if init is None:
            init = lat.canonical_rot((seed - 1) % 3)  # seed 1,4,..: canonical; 2,5,..: rotated once; 3,6,..: twice
            if seed >= 100:
                # unit electric winding sector: flip the directed x-line (y=0, z=0) of the canonical state
                init = lat.canonical().copy()
                for x in range(L):
                    l = 3 * lat.vid(np.array([x, 0, 0])) + 0
                    init[l] = -init[l]
                assert np.all(lat.div(init) == 0)
            if seed >= 11 and seed % 100 >= 11:
                # 'RK-typical' start: symmetric random walk on the flip graph (uniform stationary law),
                # 200 attempted flips per plaquette from the canonical state
                rs = np.random.default_rng(1000 + seed)
                init = init.copy()
                for p in rs.integers(lat.np, size=200 * lat.np):
                    c = (init[lat.plinks[p]] * lat.psign).sum()
                    if c == 4 or c == -4:
                        init[lat.plinks[p]] *= -1
        self.s0 = np.array(init).astype(np.int64)
        assert np.all(lat.div(self.s0) == 0)
        if cap is None:
            cap = int(max(32, 4 * g * T + 32))
        self.kt = np.zeros((lat.np, cap))
        self.kc = np.zeros(lat.np, dtype=np.int64)
        self.buf = np.zeros(65536)
        self.stats = np.zeros(10, dtype=np.int64)
        self.pr = np.array([0.3, 0.6, 0.9, 0.5])
        self.nm_fixed = None
        self.hist = 0  # number of whole-history heat-bath updates per sweep (V = 0 only), in units of N_p
        hc = self.kt.shape[1]
        self.h_et = np.zeros(16 * hc + 64)
        self.h_eq = np.zeros(16 * hc + 64, dtype=np.int64)
        self.h_f = np.zeros(16 * hc + 65, dtype=np.int64)
        self.h_al = np.zeros(2 * (16 * hc + 65))
        self.h_tmp = np.zeros(hc + 8)
        self.args = (lat.lplaqs, lat.plinks, lat.psign, lat.nbh, lat.nnb)

    def nkinks(self):
        return int(self.kc.sum())

    def do_sweep(self, factor=1.0):
        # NOTE: the number of moves per sweep must not depend on the current state during measurement
        # (a state-dependent count biases the sampled law); it is frozen by freeze_sweep().
        nm = self.nm_fixed if self.nm_fixed is not None else int(factor * (self.lat.np + self.nkinks()))
        if self.hist > 0:
            if self.V != 0.0 or self.mode != 0:
                raise ValueError("history update implemented for V = 0, open mode only")
            okh = qmc.hist_sweep_V0(self.s0, self.kt, self.kc, *self.args, self.g, self.T, int(self.hist * self.lat.np),
                                    self.h_et, self.h_eq, self.h_f, self.h_al, self.h_tmp)
            if not okh:
                raise RuntimeError("history update overflow")
        while True:
            ok = qmc.sweep(self.s0, self.kt, self.kc, *self.args, self.g, self.V, self.T, self.mode, nm,
                           self.buf, self.stats, self.pr)
            if ok:
                return
            # capacity overflow (state is consistent: overflowing insert was not performed? -> grow and continue)
            raise RuntimeError("kink capacity overflow; rerun with larger cap")

    def valid(self):
        lat = self.lat
        okp = qmc.path_valid(self.s0, self.kt, self.kc, lat.lplaqs, lat.plinks, lat.psign, self.T)
        return okp and bool(np.all(lat.div(self.s0) == 0))

    def states(self, times):
        out = np.zeros((len(times), self.lat.nl), dtype=np.int64)
        qmc.states_at(self.s0, self.kt, self.kc, self.lat.lplaqs, np.asarray(times, float), out)
        return out


def run(L, V, T, nsweep, ntherm, seed, mode=0, J=0, dtau=0.25, g=1.0, factor=1.0, cap=None, log=None,
        nbins=64, checkevery=50, every=1, hist=0.0):
    sim = Sim(L, V, T, g=g, mode=mode, seed=seed, cap=cap)
    sim.hist = hist
    lat = sim.lat
    t0 = time.time()
    for i in range(ntherm):
        sim.do_sweep(factor)
    tth = time.time() - t0
    sim.nm_fixed = int(factor * (lat.np + sim.nkinks())) + 1
    sc = {k: [] for k in ("Nf_mid", "Emix", "kin_mid", "nk", "ST1", "ST2", "Nf_end")}
    Ctau = []
    nmeas = nsweep // every
    per_bin = max(1, nmeas // nbins)
    accPE = np.zeros((nbins, L, L, L, 3))
    accPn = np.zeros((nbins, L, L, L, 3))
    nfail = 0
    w = T / 8.0
    tm = T / 2.0
    for isw in range(nmeas * every):
        sim.do_sweep(factor)
        if (isw + 1) % every != 0:
            continue
        i = isw // every
        if mode == 0:
            times = tm + dtau * np.arange(-J, J + 1)
            st = sim.states(np.concatenate([times, [0.0, T]]))
            if not np.all(lat.div(st[J]) == 0):
                nfail += 1
            PE, Pn, Nf, Ek = config_obs(lat, st)
            sc["Nf_mid"].append(Nf[J])
            sc["Nf_end"].append(0.5 * (Nf[-2] + Nf[-1]))
            sc["Emix"].append((V - g) * 0.5 * (Nf[-2] + Nf[-1]))
            nk = qmc.kinks_in(sim.kt, sim.kc, tm - w, tm + w)
            sc["kin_mid"].append(nk / (2 * w))
            b = min(i // per_bin, nbins - 1)
            accPE[b] += PE[J]
            accPn[b] += Pn[J]
            sc["ST1"].append(st_kmin(PE[J], L, 1))
            sc["ST2"].append(st_kmin(PE[J], L, 2))
            if J > 0:
                c = np.zeros(J + 1)
                for a in range(3):
                    idx = [0, 0, 0]
                    idx[a] = 1
                    e = Ek[:J * 2 + 1, idx[0], idx[1], idx[2], :]  # (2J+1, 3)
                    for bb in range(3):
                        if bb == a:
                            continue
                        x = e[:, bb]
                        for j in range(J + 1):
                            c[j] += 0.5 * (np.real(x[J] * np.conj(x[J + j])) + np.real(x[J] * np.conj(x[J - j])))
                Ctau.append(c / lat.nv)
        else:
            st = sim.states(np.array([0.0]))
            PE, Pn, Nf, Ek = config_obs(lat, st)
            sc["Nf_mid"].append(Nf[0])
            sc["Nf_end"].append(Nf[0])
            sc["Emix"].append(np.nan)
            sc["kin_mid"].append(sim.nkinks() / T)
            b = min(i // per_bin, nbins - 1)
            accPE[b] += PE[0]
            accPn[b] += Pn[0]
            sc["ST1"].append(st_kmin(PE[0], L, 1))
            sc["ST2"].append(st_kmin(PE[0], L, 2))
        sc["nk"].append(sim.nkinks())
        if (i + 1) % checkevery == 0 and not sim.valid():
            nfail += 1
    cnt = np.array([min(per_bin, nmeas - b * per_bin) if b < nbins - 1 else nmeas - (nbins - 1) * per_bin
                    for b in range(nbins)])
    accPE /= cnt[:, None, None, None, None]
    accPn /= cnt[:, None, None, None, None]
    res = {"L": L, "V": V, "T": T, "g": g, "mode": mode, "seed": seed, "nsweep": nsweep, "ntherm": ntherm, "every": every, "nm_fixed": sim.nm_fixed, "hist": hist,
           "time_therm": tth, "time_total": time.time() - t0, "gauss_or_path_failures": nfail,
           "stats": sim.stats.tolist(), "valid_final": bool(sim.valid())}
    for k, v in sc.items():
        m, se, tab = binned_se(v)
        res[k] = (float(m), float(se))
        res[k + "_bins"] = [(int(b), float(s)) for b, s in tab]
    res["E_mid"] = (V * res["Nf_mid"][0] - g * 0 - res["kin_mid"][0], float(np.hypot(V * res["Nf_mid"][1], res["kin_mid"][1])))
    if mode == 1:
        res["E_mid"] = (V * res["Nf_mid"][0] - res["kin_mid"][0], float(np.hypot(V * res["Nf_mid"][1], res["kin_mid"][1])))
    res["bins_derived"] = derived_bins(accPE, accPn, L)
    PEm = accPE.mean(0)
    PEs = accPE.std(0, ddof=1) / np.sqrt(nbins)
    Pnm = accPn.mean(0)
    Pns = accPn.std(0, ddof=1) / np.sqrt(nbins)
    if J > 0:
        C = np.array(Ctau)
        res["C"] = [(float(binned_se(C[:, j])[0]), float(binned_se(C[:, j])[1])) for j in range(J + 1)]
        res["dtau"] = dtau
        # jackknife effective gap from bins
        nb = 32
        m = len(C) // nb
        Cb = C[:m * nb].reshape(nb, m, -1).mean(1)
        res["C_bins"] = Cb.tolist()
    res["PE_mean"] = PEm
    res["PE_se"] = PEs
    res["Pn_mean"] = Pnm
    res["Pn_se"] = Pns
    res["ST1_series"] = np.array(sc["ST1"])
    if log is not None:
        print(json.dumps({k: v for k, v in res.items() if not isinstance(v, np.ndarray) and not k.endswith("_bins")
                          and k not in ("C_bins", "bins_derived")}), file=log, flush=True)
    return res
