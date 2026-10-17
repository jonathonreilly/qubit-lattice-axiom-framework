"""QMC-1 production/validation runner (QMC-1b copy: adds --alternate, --aux_every; records maxdev_down).

usage: python3 runner.py --kind spin10 --dims 4 4 --filt f2 --W 2 --beta 4 --dtau 0.1 --ns 4 \
                         --warm 50 --sweeps 200 --seed 1 --out runs/x.npz

Per sweep it records (all into the npz, one row per measured sweep):
  gt_mirror[n, k, b]  G_psi-type d-propagator <d_k(tau_n) d_k^dag> at mirror corners, averaged over the s block (b = 0,
                      the true psi propagator) and over the c block (b = 1, the psi_c hole propagator); tau_n = n n_s dtau
  gt_light[n, k, b]   same at the light corners
  light_dev           max over tau_n and light corners of |v_k^dag G(tau,0) v_k - 1/2| (gate iv; per configuration)
  SX0, SY0            (1/N) <X_a X_a>, (1/N) <Y_a Y_a> at Q = 0, per component a (X = Re Bh_S, Y = Im Bh_S)
  SXpi, SYpi          same at Q = pi (1D) / (pi, pi) (2D)
  WQ                  <W sum_x Q_x> from the vector Bh^a directly (equals the interaction only for Spin(10))
  WQc                 <W sum_x sum_e c_e O_e(x)^2> from the HS channels (the simulated interaction; = WQ for Spin(10))
  maxphase            running max |arg ratio| over all proposals (gate ii)
  acc                 acceptance of the sweep
"""
import argparse, os, sys, time, resource
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
from afqmc import Lattice, AFQMC, Observables

KAP = {"spin10": {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0},     # PREREG follow-up A
       "reduced": {"sing:1v": 1.0, "trip:1v": -1.0 / 3}}                                  # PREREG section 4 (iii)


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", default="spin10")
    ap.add_argument("--dims", type=int, nargs="+", required=True)
    ap.add_argument("--filt", required=True)
    ap.add_argument("--W", type=float, required=True)
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--dtau", type=float, required=True)
    ap.add_argument("--ns", type=int, default=4)
    ap.add_argument("--warm", type=int, default=50)
    ap.add_argument("--sweeps", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--step", type=float, default=0.3)
    ap.add_argument("--nhit", type=int, default=1)
    ap.add_argument("--eqt_every", type=int, default=1, help="equal-time measurement every k sweeps")
    ap.add_argument("--eqt_points", type=int, default=1, help="number of stabilisation points with equal-time meas.")
    ap.add_argument("--kinetic", action="store_true")
    ap.add_argument("--tmax", type=float, default=1e9, help="wall-clock limit (s) for the measurement phase")
    ap.add_argument("--alternate", action="store_true", help="QMC-1b: alternate upward/downward sweeps")
    ap.add_argument("--aux_every", type=int, default=1, help="QMC-1b: S(Qpi) and <WQ> every k-th measured sweep")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    fm = FlavourModel(a.kind)
    lat = Lattice(tuple(a.dims), a.filt)
    sim = AFQMC(fm, KAP[a.kind], lat, W=a.W, beta=a.beta, dtau=a.dtau, n_s=a.ns, seed=a.seed, step=a.step,
                n_hit=a.nhit)
    sim.alternate = a.alternate
    obs = Observables(sim)
    nst = sim.nst
    eq_pts = set(np.linspace(nst // a.eqt_points, nst, a.eqt_points).astype(int).tolist()) if a.eqt_points > 0 else set()
    print(f"[run] kind={a.kind} dims={lat.dims} filt={a.filt} rho={lat.rho} W={a.W} beta={a.beta} dtau={a.dtau} "
          f"Lt={sim.Lt} ns={a.ns} Nd={sim.Nd} nch={sim.nch} eq_pts={sorted(eq_pts)}", flush=True)
    rec = {k: [] for k in ("gt_mirror", "gt_light", "light_dev", "SX0", "SY0", "SXpi", "SYpi", "WQ", "WQc", "Ekin",
                           "acc", "maxphase", "maxdev", "sweep")}
    cur = {}

    def meas(n, G, Gt, s):
        gm = obs.gk(Gt, "mirror"); gl = obs.gk(Gt, "light")
        Smask = s.fm.Smask
        cur["gm"][n] = [[np.real(np.mean(np.diag(g)[Smask])), np.real(np.mean(np.diag(g)[~Smask]))] for g in gm]
        cur["gl"][n] = [[np.real(np.mean(np.diag(g)[Smask])), np.real(np.mean(np.diag(g)[~Smask]))] for g in gl]
        if lat.filt != "one":
            cur["ld"] = max(cur["ld"], max(np.abs(g - 0.5 * np.eye(s.D)).max() for g in gl))
        if cur["do_eq"] and n in eq_pts:
            sx, sy = obs.structure(G, "Q0")
            if cur.get("aux", True):
                sxp, syp = obs.structure(G, "Qpi")
                qa, qb = obs.local_terms(G)
            else:
                sxp = syp = np.full(len(sx), np.nan); qa = qb = np.nan + 0j
            cur["eq"].append((sx, sy, sxp, syp, a.W * qa.real, obs.kinetic(G).real if a.kinetic else np.nan,
                              a.W * qb.real))

    def one_sweep(i, measure_eq):
        nk_m, nk_l = len(obs.kset["mirror"]), len(obs.kset["light"])
        cur.update(gm=np.zeros((nst + 1, nk_m, 2)), gl=np.zeros((nst + 1, nk_l, 2)), ld=0.0, eq=[], do_eq=measure_eq,
                   aux=(i % a.aux_every == 0))
        p0, a0 = sim.nprop, sim.nacc
        sim.sweep(measure=meas)
        return (sim.nacc - a0) / max(1, sim.nprop - p0)

    # warm-up with step adaptation (target acceptance 0.35-0.65); step frozen afterwards
    for i in range(a.warm):
        acc = one_sweep(i, False)
        if a.W != 0 and i < int(0.8 * a.warm):
            if acc > 0.65: sim.step = min(1.0, sim.step * 1.25)
            elif acc < 0.35: sim.step = sim.step / 1.25
        if i % 10 == 0 or i == a.warm - 1:
            print(f"[warm {i}] acc {acc:.3f} step {sim.step:.4f} maxphase {sim.maxphase:.1e} maxdev {sim.maxdev:.1e} "
                  f"t {time.time() - t0:.0f}s rss {rss():.0f}MB", flush=True)
    tm = time.time()
    for i in range(a.sweeps):
        acc = one_sweep(i, i % a.eqt_every == 0)
        rec["gt_mirror"].append(cur["gm"]); rec["gt_light"].append(cur["gl"]); rec["light_dev"].append(cur["ld"])
        if cur["eq"]:
            sx, sy, sxp, syp, wq, ek, wqc = [np.mean([e[j] for e in cur["eq"]], axis=0) for j in range(7)]
        else:
            nA = len(fm.Nvec); sx = sy = sxp = syp = np.full(nA, np.nan); wq = ek = wqc = np.nan
        for k, v in (("SX0", sx), ("SY0", sy), ("SXpi", sxp), ("SYpi", syp), ("WQ", wq), ("Ekin", ek), ("WQc", wqc)):
            rec[k].append(v)
        rec["acc"].append(acc); rec["maxphase"].append(sim.maxphase); rec["maxdev"].append(sim.maxdev); rec["sweep"].append(i)
        if i % 10 == 0 or i == a.sweeps - 1:
            s10 = np.nansum(sx) + np.nansum(sy)
            print(f"[meas {i}] acc {acc:.3f} S10(Q0) {s10:.4f} WQ {wq:.4f} Gm(beta/2) {cur['gm'][nst // 2, 0, 0]:.4f} "
                  f"maxphase {sim.maxphase:.1e} maxdev {sim.maxdev:.1e} lightdev {cur['ld']:.1e} "
                  f"t {time.time() - t0:.0f}s rss {rss():.0f}MB", flush=True)
            np.savez(a.out, **{k: np.array(v) for k, v in rec.items()}, args=str(vars(a)), step=sim.step,
                     tau=np.arange(nst + 1) * a.ns * a.dtau, sec_per_sweep=(time.time() - tm) / (i + 1))
        if time.time() - tm > a.tmax:
            print(f"[stop] wall-clock limit after {i + 1} measured sweeps", flush=True)
            break
    np.savez(a.out, **{k: np.array(v) for k, v in rec.items()}, args=str(vars(a)), step=sim.step,
             tau=np.arange(nst + 1) * a.ns * a.dtau, sec_per_sweep=(time.time() - tm) / max(1, len(rec["acc"])))
    print(f"[done] maxdev_down {getattr(sim, 'maxdev_down', float('nan')):.2e}; {len(rec['acc'])} sweeps, {(time.time() - tm) / max(1, len(rec['acc'])):.2f} s/sweep, "
          f"maxphase {sim.maxphase:.2e}, maxdev {sim.maxdev:.2e}, peak RSS {rss():.0f} MB, total {time.time() - t0:.0f}s",
          flush=True)


if __name__ == "__main__":
    main()
