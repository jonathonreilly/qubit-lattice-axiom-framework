"""T08 reduced test (relaxation).  Cut variable lam = (gamma1,gamma2) (or gamma for the chain).
Any Gibbs patch law (s - A - cut - B - t) conditioned on the two settings has the exact form
   P(a,b,lam | s,t) = F[s,a,lam] * G[t,b,lam] / Z[s,t]     (F, G >= 0, arbitrary)
(F[s,a,lam] = sum over A-contents alpha with outcome a of f_s(alpha) * bond weights to the cut; same for G).
So maximising CHSH over arbitrary nonnegative F, G under the locality constraints is a RELAXATION of the
Gibbs-patch problem (it allows hard zeros, and any F, G).  If the relaxation cannot beat 2, no Gibbs patch can.
Modes: PI (outcome marginals), ML (+ single cut-site marginals constant), CML (+ joint cut law constant).
"""
import numpy as np, sys, json, time, os
from scipy.optimize import minimize
from multiprocessing import Pool

def build(graph, nc):
    L = nc if graph == "chain" else nc * nc
    nF = 2 * 2 * L
    def unpack(x):
        F = x[:nF].reshape(2, 2, L); G = x[nF:].reshape(2, 2, L)
        return F, G
    def probs(x):
        F, G = unpack(x)
        N = np.einsum("sal,tbl->stabl", F, G)
        Z = N.sum(axis=(2, 3, 4))
        P = N / Z[:, :, None, None, None]
        return P, Z
    sgn = np.array([1.0, -1.0])
    def S(x):
        P, Z = probs(x)
        Pab = P.sum(axis=4)
        E = np.einsum("stab,a,b->st", Pab, sgn, sgn)
        return E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]
    def cons_vec(x, mode):
        P, Z = probs(x)
        Pl = P.sum(axis=(2, 3))          # s,t,lam
        Pa = P.sum(axis=(3, 4))[..., 0]  # P(a=+|s,t)
        Pb = P.sum(axis=(2, 4))[..., 0]
        r = []
        for s in (0, 1): r.append(Pa[s, 0] - Pa[s, 1])
        for t in (0, 1): r.append(Pb[0, t] - Pb[1, t])
        if mode in ("ML", "CML"):
            if graph == "chain":
                for (s, t) in ((0, 1), (1, 0), (1, 1)):
                    r.extend(list(Pl[s, t] - Pl[0, 0])[:-1])
            else:
                Pg = Pl.reshape(2, 2, nc, nc)
                for ax in (3, 2):
                    m = Pg.sum(axis=ax)
                    for (s, t) in ((0, 1), (1, 0), (1, 1)):
                        r.extend(list(m[s, t] - m[0, 0])[:-1])
        if mode == "CML" and graph == "cycle":
            for (s, t) in ((0, 1), (1, 0), (1, 1)):
                r.extend(list(Pl[s, t] - Pl[0, 0])[:-1])
        return np.array(r), Z
    return 2 * nF, S, cons_vec

def run_one(args):
    graph, nc, mode, eps, seed = args
    n, S, cons_vec = build(graph, nc)
    rng = np.random.default_rng(seed)
    x0 = rng.random(n) * (rng.random(n) < 0.7)  # sparse starts allow zeros
    x0 = x0 + 0.05 * rng.random(n)
    cons = [{"type": "ineq", "fun": lambda x: cons_vec(x, mode)[1].ravel() - 1e-3}]
    if eps == 0:
        cons.append({"type": "eq", "fun": lambda x: cons_vec(x, mode)[0]})
    else:
        cons.append({"type": "ineq", "fun": lambda x: eps - cons_vec(x, mode)[0]})
        cons.append({"type": "ineq", "fun": lambda x: eps + cons_vec(x, mode)[0]})
    try:
        out = minimize(lambda x: -S(x), x0, method="SLSQP", bounds=[(0, 1)] * n, constraints=cons,
                       options={"maxiter": 500, "ftol": 1e-14})
        x = out.x
        r, Z = cons_vec(x, mode)
        return dict(seed=seed, S=float(S(x)), res=float(np.max(np.abs(r))), Zmin=float(Z.min()), x=x.tolist())
    except Exception as e:
        return dict(seed=seed, S=None, res=None, Zmin=None, x=None)

if __name__ == "__main__":
    graph, nc, mode, eps = sys.argv[1].split(",")
    nc, eps = int(nc), float(eps)
    nstarts = int(sys.argv[2])
    t0 = time.time()
    with Pool(10) as p:
        outs = p.map(run_one, [(graph, nc, mode, eps, i) for i in range(nstarts)], chunksize=1)
    outs = [o for o in outs if o["S"] is not None]
    tol = max(1e-9, 1.01 * eps)
    feas = [o for o in outs if o["res"] <= tol and o["Zmin"] >= 1e-3 - 1e-9]
    best = max(feas, key=lambda o: o["S"]) if feas else None
    top = sorted([o["S"] for o in feas], reverse=True)[:5]
    print(f"{sys.argv[1]} starts={len(outs)} feasible={len(feas)} best_S={None if best is None else round(best['S'],6)} "
          f"res={None if best is None else '%.1e'%best['res']} top5={[round(v,4) for v in top]} t={time.time()-t0:.0f}s", flush=True)
    if best:
        os.makedirs("results", exist_ok=True)
        json.dump(best, open(f"results/red_{graph}_{nc}_{mode}_{eps}.json", "w"))
