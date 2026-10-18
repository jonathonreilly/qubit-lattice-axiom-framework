"""B5: tolerance of the reduced output device to bond/onsite errors under
(a_lit) complete vector metric with literal phase and NOMINAL clock scalar,
(a_act) same but with the ACTUAL positive-block scalar C(w) (repo convention),
(b_pop) probability-only: total-variation distance of site populations,
(c_gp)  co-located phase reference: min over one global phase,
(c_rel) co-transported reference: twin apparatus sharing the actual transport
        (lead) and full-space scalar, with nominal source coefficients.

Tolerance x*: worst case over K fixed random error directions u (uniform in
[-1,1]^n, seeded) of max_{t in {T,2T}} metric(x*u) equals the budget e=1e-2.
Found by log-secant from two probe points; each x* is then re-evaluated
directly (VERIFY PASS iff the direct value lies in [0.8e,1.25e]).

PREDICTIONS (declared before the first run of this script):
 P1 source-bond (SB) tolerance in a_act/b_pop/c_gp/c_rel is flat in lam and T.
 P2 SB under a_lit scales ~1/T at fixed lam (positive-block scalar clock phase).
 P3 source-onsite (SO) tolerance under a_act scales ~lam, flat in T at fixed lam.
 P4 SO under b_pop is looser than a_act (phase part of the error is invisible).
 P5 lead (receiver) bond/onsite errors: a_act tolerance falls with T at fixed
    lam (time-of-flight accumulation); c_rel tolerance infinite (common mode).
 P6 global common onsite (GC): a_lit ~1/T, every other metric infinite.
 P7 D2 mediator bonds: a_act tolerance ~1/(2n+1), flat in T.
"""
import sys, json, time, zlib
import numpy as np
from multiprocessing import Pool
from b5_device import d1_chain, d2_chain, m_vec, m_pop, m_gp

E = 1e-2
K = 4
METRICS = ["a_lit", "a_act", "b_pop", "c_gp", "c_rel"]
D2P = dict(Jm=1.0, q=0.8, g=0.05)


def build(cfg, cls, x, u):
    """Return (actual chain, twin chain, seed, dC, region slice)."""
    if cfg["dev"] == "D1":
        lam, M = cfg["lam"], cfg["M"]
        kw, tw = {}, {}
        if cls == "SB": kw["eps_src"] = x * u
        if cls == "SO": kw["xi_src"] = x * u
        if cls == "SC": kw["xi_src"] = x * u[0] * np.ones(3)
        if cls == "LB": kw["eps_lead"] = tw["eps_lead"] = x * u
        if cls == "LO": kw["xi_lead"] = tw["xi_lead"] = x * u
        if cls == "GC": kw["xi_all"] = tw["xi_all"] = x * u[0]
        H, s, src = d1_chain(lam, M, **kw)
        Ht, _, src0 = d1_chain(lam, M, **tw)
        dC = float(np.sum(src - src0)) if cls == "SB" else 0.0
        return H, Ht, s, dC, slice(0, None)
    else:
        n, M = cfg["n"], cfg["M"]
        r = D2P["q"] / D2P["Jm"]
        gam = np.sqrt(0.01 * D2P["Jm"] / r ** (n - 1))
        kw = {}
        if cls == "MB": kw["eps_med"] = x * u
        if cls == "MO": kw["xi_med"] = x * u
        if cls == "EO": kw["xi_e"] = x * u[0]
        H, s, medb = d2_chain(n, gam, D2P["Jm"], D2P["q"], D2P["g"], M, **kw)
        Ht, _, medb0 = d2_chain(n, gam, D2P["Jm"], D2P["q"], D2P["g"], M)
        dC = float(np.sum(medb - medb0)) if cls == "MB" else 0.0
        return H, Ht, s, dC, slice(1 + 2 * n + 30, None)   # output register


def ndir(cfg, cls):
    if cfg["dev"] == "D1":
        return {"SB": 3, "SO": 3, "SC": 1, "LB": cfg["M"] - 1, "LO": cfg["M"], "GC": 1}[cls]
    return {"MB": 2 * cfg["n"] + 1, "MO": 2 * cfg["n"], "EO": 1}[cls]


_NOM = {}


def nominal(cfg):
    key = json.dumps(cfg, sort_keys=True)
    if key not in _NOM:
        H, Ht, s, _, _ = build(cfg, "none", 0.0, None)
        _NOM[key] = H.evolve(s, [cfg["T"], 2 * cfg["T"]])
    return _NOM[key]


def evaluate(cfg, cls, x, dirs):
    nom = nominal(cfg)
    worst = dict.fromkeys(METRICS + ["a_full"], 0.0)
    for u in dirs:
        H, Ht, s, dC, R = build(cfg, cls, x, u)
        act = H.evolve(s, [cfg["T"], 2 * cfg["T"]])
        same_twin = np.array_equal(H.d, Ht.d) and np.array_equal(H.o, Ht.o)
        twin = act if same_twin else nom    # twin differs from nominal only by shared transport
        if not same_twin and cls in ("LB", "LO", "GC"):
            raise RuntimeError("unexpected twin structure")
        for t, pa, pn, pt in zip([cfg["T"], 2 * cfg["T"]], act, nom, twin):
            ph_act = np.exp(-1j * t * dC)          # positive-block full-space scalar
            A = ph_act * pa                        # physical actual state
            vals = {
                "a_lit": m_vec(A[R], pn[R]),
                "a_act": m_vec(A[R], ph_act * pn[R]),
                "b_pop": m_pop(A[R], pn[R]),
                "c_gp": m_gp(A[R], pn[R]),
                "c_rel": m_vec(A[R], ph_act * pt[R]),
                "a_full": m_vec(A, ph_act * pn),
            }
            for k, v in vals.items():
                worst[k] = max(worst[k], v)
    return worst


def tolerance_job(args):
    cfg, cls, x0 = args
    rng = np.random.default_rng(zlib.crc32(f"{cfg['dev']}-{cls}".encode()))
    nd = ndir(cfg, cls)
    dirs = [rng.uniform(-1, 1, nd) for _ in range(K)]
    cache = {}

    def f(x):
        if x not in cache:
            cache[x] = evaluate(cfg, cls, x, dirs)
        return cache[x]

    out = {}
    xa, xb = x0, x0 / 4
    fa, fb = f(xa), f(xb)
    for m in METRICS:
        ya, yb = fa[m], fb[m]
        if ya < 1e-11 and yb < 1e-11:
            out[m] = dict(tol=float("inf"), p=None, verify=None, ok=True, note="exact cancellation")
            continue
        p = np.log(ya / yb) / np.log(xa / xb)
        x1, y1, x2, y2 = xa, ya, xb, yb
        xs = None
        for _ in range(5):                         # log-secant towards metric = E
            s_ = np.log(y1 / y2) / np.log(x1 / x2)
            if not np.isfinite(s_) or s_ <= 0:
                break
            xs = x1 * (E / y1) ** (1 / s_)
            xs = float(min(xs, 10.0))
            ys = f(xs)[m]
            if abs(np.log(ys / E)) < np.log(1.1) or xs >= 10.0:
                break
            x1, y1, x2, y2 = xs, ys, x1, y1
        yv = f(xs)[m] if xs is not None else float("nan")
        ok = 0.8 * E <= yv <= 1.25 * E
        note = "saturated (tol>=10)" if xs is not None and xs >= 10.0 and yv < E else ""
        if not (ok or note):
            # fallback: first crossing. Halve x from x0 until metric<E, then log-bisect.
            hi = xa
            while f(hi)[m] < E and hi < 10.0:
                hi *= 4
            lo = hi / 2
            while f(lo)[m] >= E:
                hi, lo = lo, lo / 2
            for _ in range(12):
                mid = np.sqrt(lo * hi)
                if f(mid)[m] < E: lo = mid
                else: hi = mid
            xs, yv = lo, f(lo)[m]
            ok = yv < E and f(hi)[m] >= E and hi / lo < 1.1
            note = "first-crossing bisection (metric non-power-law)"
        out[m] = dict(tol=xs, p=float(p), verify=float(yv), ok=bool(ok or note), note=note)
    return dict(cfg=cfg, cls=cls, res=out, a_full_at_x0=fa["a_full"])


def d1cfg(lam, Tl=25.0, Mf=4.8):
    T = Tl / lam
    return dict(dev="D1", lam=lam, T=T, M=int(Mf * T) + 50)


def d2cfg(n, Tl=25.0):
    lam = 2 * 0.01 ** 2 / D2P["g"]
    T = Tl / lam
    return dict(dev="D2", n=n, lam=lam, T=T, M=int(1.2 * 2 * D2P["g"] * 2 * T) + 50)


def x0_for(cfg, cls):
    lam, T = cfg["lam"], cfg["T"]
    return {"SB": 1e-2, "SO": 1e-2 * lam, "SC": 1e-2 * lam, "LB": 1e-3, "LO": 1e-3,
            "GC": 1e-2 / T, "MB": 1e-3, "MO": 1e-3, "EO": 1e-2 * lam}[cls]


if __name__ == "__main__":
    which = sys.argv[1]
    jobs = []
    if which == "A":      # repo-like coupled family: T=25/lam, M~4.8T
        for lam in [0.04, 0.02, 0.01, 0.005]:
            c = d1cfg(lam)
            jobs += [(c, k, x0_for(c, k)) for k in ["SB", "SO", "SC", "LB", "LO", "GC"]]
    elif which == "B":    # fixed lam, vary T (and M with it)
        for Tl in [25.0, 50.0, 100.0, 200.0]:
            c = d1cfg(0.04, Tl)
            jobs += [(c, k, x0_for(c, k)) for k in ["SB", "SO", "SC", "LB", "LO", "GC"]]
    elif which == "C":    # fixed lam,T, vary M only
        for Mf in [4.8, 9.6, 19.2]:
            c = d1cfg(0.04, 25.0, Mf)
            jobs += [(c, k, x0_for(c, k)) for k in ["SB", "SO", "LB", "LO"]]
    elif which == "E":    # supplementary: SB (a_lit clock) and GC after metric fix
        for lam in [0.04, 0.02, 0.01, 0.005]:
            c = d1cfg(lam)
            jobs += [(c, k, x0_for(c, k)) for k in ["SB", "GC"]]
        for Tl in [50.0, 100.0, 200.0]:
            c = d1cfg(0.04, Tl)
            jobs += [(c, k, x0_for(c, k)) for k in ["SB", "GC"]]
    elif which == "D":    # mediated emitter, vary n at fixed lam; and T at n=3
        for n in [1, 2, 3, 4, 5]:
            c = d2cfg(n)
            jobs += [(c, k, x0_for(c, k)) for k in ["MB", "MO", "EO"]]
        for Tl in [50.0, 100.0]:
            c = d2cfg(3, Tl)
            jobs += [(c, k, x0_for(c, k)) for k in ["MB", "MO", "EO"]]
    t0 = time.time()
    with Pool(4) as pool:
        res = pool.map(tolerance_job, jobs, chunksize=1)
    json.dump(res, open(f"scan_{which}.json", "w"), indent=1, default=float)
    print(f"# scan {which}: {len(res)} jobs, {time.time()-t0:.0f}s, budget e={E}, K={K}")
    for r in res:
        c = r["cfg"]
        tag = f"{c['dev']} lam={c['lam']:.4g} T={c['T']:.4g} M={c['M']}" + (f" n={c['n']}" if 'n' in c else "")
        line = " ".join(f"{m}={r['res'][m]['tol']:.3e}(p={r['res'][m]['p'] if r['res'][m]['p'] is None else round(r['res'][m]['p'],2)},{'PASS' if r['res'][m]['ok'] else 'FAIL'})" for m in METRICS)
        print(f"{tag} {r['cls']}: {line}")
