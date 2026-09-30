"""T08 test: co-formed Gibbs patches between two exogenous setting records.
See PREREGISTER.md (written before this script was run)."""
import numpy as np, json, sys, time, os
from scipy.optimize import minimize
from multiprocessing import Pool

def make_model(graph, na, nb, nc):
    """returns (nparams, joint(x)->dict of marginals)"""
    if graph == "chain":
        shapes = [("f", (2, na)), ("W1", (na, nc)), ("W2", (nc, nb)), ("g", (2, nb))]
    else:
        shapes = [("f", (2, na)), ("W1", (na, nc)), ("W2", (nc, nb)), ("W3", (nb, nc)),
                  ("W4", (nc, na)), ("g", (2, nb))]
    sizes = [int(np.prod(sh)) for _, sh in shapes]
    n = sum(sizes)
    a_val = np.array([1.0 if i % 2 == 0 else -1.0 for i in range(na)])
    b_val = np.array([1.0 if i % 2 == 0 else -1.0 for i in range(nb)])

    def unpack(x):
        d, o = {}, 0
        for (name, sh), sz in zip(shapes, sizes):
            d[name] = np.exp(x[o:o + sz].reshape(sh)); o += sz
        return d

    def marg(x):
        d = unpack(x)
        if graph == "chain":
            # T[s,t,a,c,b]
            T = np.einsum("sa,ac,cb,tb->stacb", d["f"], d["W1"], d["W2"], d["g"])
            Z = T.sum(axis=(2, 3, 4), keepdims=True)
            T = T / Z
            Pa = T.sum(axis=(3, 4)); Pb = T.sum(axis=(2, 3)); Pc = [T.sum(axis=(2, 4))]
            Pab = T.sum(axis=3)  # s,t,a,b
            Pcc = None
        else:
            # T[s,t,a,c,b,d]  cycle a-c-b-d-a
            T = np.einsum("sa,ac,cb,bd,da,tb->stacbd", d["f"], d["W1"], d["W2"], d["W3"], d["W4"], d["g"])
            Z = T.sum(axis=(2, 3, 4, 5), keepdims=True)
            T = T / Z
            Pa = T.sum(axis=(3, 4, 5)); Pb = T.sum(axis=(2, 3, 5))
            Pc = [T.sum(axis=(2, 4, 5)), T.sum(axis=(2, 3, 4))]
            Pab = T.sum(axis=(3, 5))
            Pcc = T.sum(axis=(2, 4))
        E = np.einsum("stab,a,b->st", Pab, a_val, b_val)
        return dict(Pa=Pa, Pb=Pb, Pc=Pc, Pcc=Pcc, E=E)

    def S(x):
        E = marg(x)["E"]
        return E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]

    def res(x, mode):
        m = marg(x)
        r = []
        if mode in ("PI", "ML", "CML"):
            for s in (0, 1):
                r.append((m["Pa"][s, 0] - m["Pa"][s, 1])[:-1])
            for t in (0, 1):
                r.append((m["Pb"][0, t] - m["Pb"][1, t])[:-1])
        if mode in ("ML", "CML"):
            for Pc in m["Pc"]:
                for (s, t) in ((0, 1), (1, 0), (1, 1)):
                    r.append((Pc[s, t] - Pc[0, 0])[:-1])
        if mode == "CML" and graph == "cycle":
            for (s, t) in ((0, 1), (1, 0), (1, 1)):
                r.append((m["Pcc"][s, t] - m["Pcc"][0, 0]).ravel()[:-1])
        if not r:
            return np.zeros(0)
        return np.concatenate(r)

    return n, S, res, marg

def run_one(args):
    graph, na, nb, nc, mode, eps, seed, maxiter = args
    n, S, res, marg = make_model(graph, na, nb, nc)
    rng = np.random.default_rng(seed)
    x0 = rng.normal(0, 1.5, n)
    bounds = [(-12, 12)] * n
    if mode == "DLR":
        cons = []
    elif eps == 0:
        cons = [{"type": "eq", "fun": lambda x: res(x, mode)}]
    else:
        cons = [{"type": "ineq", "fun": lambda x: eps - res(x, mode)},
                {"type": "ineq", "fun": lambda x: eps + res(x, mode)}]
    try:
        out = minimize(lambda x: -S(x), x0, method="SLSQP", bounds=bounds, constraints=cons,
                       options={"maxiter": maxiter, "ftol": 1e-13})
        x = out.x
    except Exception as e:
        return dict(seed=seed, S=None, res=None, x=None)
    return dict(seed=seed, S=float(S(x)), res=float(np.max(np.abs(res(x, mode)))), x=x.tolist())

def campaign(graph, na, nb, nc, mode, eps, nstarts, maxiter=400, procs=8, seed0=0):
    args = [(graph, na, nb, nc, mode, eps, seed0 + i, maxiter) for i in range(nstarts)]
    with Pool(procs) as p:
        outs = p.map(run_one, args, chunksize=1)
    outs = [o for o in outs if o["S"] is not None]
    tol = max(1e-9, 1.01 * eps)
    feas = [o for o in outs if o["res"] <= tol]
    best = max(feas, key=lambda o: o["S"]) if feas else None
    return outs, feas, best

if __name__ == "__main__":
    which = sys.argv[1]
    nstarts = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    graph, na, nb, nc, mode, eps = which.split(",")
    na, nb, nc, eps = int(na), int(nb), int(nc), float(eps)
    t0 = time.time()
    outs, feas, best = campaign(graph, na, nb, nc, mode, eps, nstarts)
    Ss = sorted([o["S"] for o in outs], reverse=True)[:5]
    print(f"{which}: starts={len(outs)} feasible(res<=tol)={len(feas)} "
          f"best_feasible_S={None if best is None else round(best['S'],6)} "
          f"best_res={None if best is None else '%.2e'%best['res']} top5_all_S={[round(v,4) for v in Ss]} "
          f"time={time.time()-t0:.0f}s", flush=True)
    if best is not None:
        os.makedirs("results", exist_ok=True)
        json.dump(best, open(f"results/best_{graph}_{na}{nb}{nc}_{mode}_{eps}.json", "w"))
