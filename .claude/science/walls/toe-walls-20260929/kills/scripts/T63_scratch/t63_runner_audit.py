"""T63 test A: audit of scripts/frontier_primordial_spectrum_dim_scan.py (read-only import; no bytecode written).
A0 reproduce; A1 adjacency unused; A2 controls; A3 dependence on N_e,graph vs formula (*)."""
import sys, math, time
sys.dont_write_bytecode = True
sys.path.insert(0, "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts")
import numpy as np
import frontier_primordial_spectrum_dim_scan as R

D = 3
SEEDS = R.SEED_LIST

def formula_star(d, Ne): return 1 - 2/Ne + (d-3)/(d*Ne)

def fit_from_coords(coords, side_phys, d, n_final):
    grid = max(8, min(24, int(round(n_final ** (1.0/d)))))
    delta = R.density_field_from_coords(coords, side_phys, grid, d)
    k, ds = R.power_spectrum_radial(delta, d)
    return R.fit_ns_loglog(k, ds)      # (n_s, err, r2)

def agg(vals):
    v = np.array(vals); return v.mean(), v.std(ddof=1)/math.sqrt(len(v))

def runner_coords(d, side, f, rng):
    """Vectorised replica of the runner's coordinate law (edges are never read, so omitted)."""
    n_init = side**d
    n_target = n_init * f**d
    seed = np.array(np.meshgrid(*[np.arange(side)]*d, indexing='ij')).reshape(d, -1).T.astype(float)
    n = np.arange(n_init, n_target)
    side_eff = side * (n / n_init) ** (1.0/d)
    new = rng.uniform(0, 1, size=(len(n), d)) * side_eff[:, None]
    allc = np.vstack([seed, new])
    return [tuple(c) for c in allc], side * (n_target/n_init)**(1.0/d), n_target

def poisson_coords(d, side, f, rng):
    n_init = side**d; n_target = n_init * f**d
    side_phys = side * f
    allc = rng.uniform(0, side_phys, size=(n_target, d))
    return [tuple(c) for c in allc], side_phys, n_target

def mean_profile_ns(d, side, f, seeds):
    """Runner coordinate law, but delta measured against the ensemble-mean density profile
    (removes the deterministic corner-heavy profile; leaves the fluctuations)."""
    fields = []
    for s in seeds:
        rng = np.random.default_rng(s)
        c, sp, nt = runner_coords(d, side, f, rng)
        grid = max(8, min(24, int(round(nt ** (1.0/d)))))
        fields.append((R.density_field_from_coords(c, sp, grid, d), grid))
    rho = np.array([ (1+fl[0]) for fl in fields])   # back to rho/mean
    mprof = rho.mean(axis=0)
    out = []
    for r in rho:
        delta = np.where(mprof > 0, r/np.where(mprof > 0, mprof, 1.0) - 1.0, 0.0)
        k, ds = R.power_spectrum_radial(delta, d)
        out.append(R.fit_ns_loglog(k, ds)[0])
    return out

if __name__ == "__main__":
    t0 = time.time()
    print("A0 reproduce runner d=3 (registered: n_s = -0.165 +- 0.313 at N_e,graph = 1.386)")
    res = [R.measure_ns_for_dimension(D, s) for s in SEEDS]
    ns = [r['n_s_meas'] for r in res]; m, e = agg(ns)
    print("   per-seed n_s:", np.round(ns, 3), " mean %.3f +- %.3f" % (m, e), " N_e,graph = %.3f" % res[0]['N_e_graph'], "(%.0fs)" % (time.time()-t0))

    print("\nA1 adjacency use: lines in the runner that touch 'adj' (all are writes in build/grow):")
    for i, line in enumerate(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts/frontier_primordial_spectrum_dim_scan.py"), 1):
        if "adj" in line and not line.strip().startswith("#"): print("   line %d: %s" % (i, line.rstrip()))
    print("   density_field_from_coords / power_spectrum_radial / fit_ns_loglog take only coordinates: no edge enters the measured n_s.")

    print("\nA2 controls at f=4 (N_e,graph = ln 4 = 1.386), 40 seeds each")
    seeds40 = list(range(100, 140))
    for name, gen in (("runner coordinate law (replica)", runner_coords), ("i.i.d. uniform, no seed clump, no profile (Poisson)", poisson_coords)):
        vals = []
        for s in seeds40:
            rng = np.random.default_rng(s)
            c, sp, nt = gen(D, 8, 4, rng)
            vals.append(fit_from_coords(c, sp, D, nt)[0])
        m, e = agg(vals); print("   %-52s n_s = %+.3f +- %.3f" % (name, m, e))
    vals = mean_profile_ns(D, 8, 4, seeds40); m, e = agg(vals)
    print("   %-52s n_s = %+.3f +- %.3f" % ("runner law, residual about ensemble-mean profile", m, e))

    print("\nA3 growth factor f -> N_e,graph = ln f; formula (*) vs replica vs Poisson (20 seeds each)")
    print("   f   N_e    (*)     runner-law n_s      Poisson n_s        z_runner-vs-(*)")
    for f in (2, 3, 4, 6, 8):
        rv, pv = [], []
        for s in range(200, 220):
            rng = np.random.default_rng(s); c, sp, nt = runner_coords(D, 8, f, rng); rv.append(fit_from_coords(c, sp, D, nt)[0])
            rng = np.random.default_rng(s+500); c, sp, nt = poisson_coords(D, 8, f, rng); pv.append(fit_from_coords(c, sp, D, nt)[0])
        rm, re_ = agg(rv); pm, pe = agg(pv); Ne = math.log(f)
        fs = formula_star(D, Ne)
        print("  %2d  %.3f  %+.3f   %+.3f +- %.3f   %+.3f +- %.3f      %.1f" % (f, Ne, fs, rm, re_, pm, pe, abs(rm-fs)/max(re_, 1e-9)))
    print("done %.0fs" % (time.time()-t0))
