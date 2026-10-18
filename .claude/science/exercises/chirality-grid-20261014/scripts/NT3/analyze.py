"""NT-3 analysis driver: full-sector scan of one model (see ../PREREG.md, Observables 1-4)."""
import numpy as np, time
import scipy.sparse as sp, scipy.sparse.linalg as sla
from ed_core import Model, lowest, dominant_weights, NF

TOL = 1e-8


def chain(model, d, K):
    return model.chain_sector(tuple(d), K)


def analyze(model, W=1.0, v=0.0, near_light=(), verbose=print, want_chi=True, Kgs=0):
    G = model.G; M = model.M; t0 = time.time()
    res = {}
    # --- GS sector: weight 0, momentum Kgs ---
    b0 = chain(model, (0, 0, 0, 0), Kgs)
    H0 = model.build_H(b0, W=W, v=v)
    asym = abs(H0 - H0.T).max() if H0.nnz else 0.0
    e0s, v0s = lowest(H0, k=4)
    E0 = e0s[0]; g0 = v0s[:, 0]
    occ0 = model.occ(b0, g0)
    res.update(E0=E0, dimGS=len(b0), asym=asym, e_gs_sector=e0s)
    # --- full dominant-weight scan ---
    table = []
    nl_idx = [model.jof[m] for m in near_light if m in model.jof]
    for d in dominant_weights(M):
        for K in range(G.n):
            if d == (0, 0, 0, 0) and K == Kgs:
                es = e0s; vecs = v0s; b = b0
            else:
                b = chain(model, d, K)
                if len(b) == 0:
                    continue
                H = model.build_H(b, W=W, v=v)
                es, vecs = lowest(H, k=3)
            for lev in range(len(es)):
                if d == (0, 0, 0, 0) and K == Kgs and lev == 0:
                    continue
                # light attribution only for the lowest level of each sector (and level 1 of GS sector)
                if lev == 0 or (d == (0, 0, 0, 0) and K == Kgs and lev == 1):
                    occ = model.occ(b, vecs[:, lev])
                    dn = np.abs(occ - occ0) if len(b) == len(b0) and d == (0, 0, 0, 0) and K == Kgs else None
                    if dn is None:
                        # different sector: compare momentum-resolved occupations directly
                        dn = np.abs(occ - occ0)
                    wl = dn[nl_idx].sum() / dn.sum() if (nl_idx and dn.sum() > 1e-12) else 0.0
                    table.append((es[lev] - E0, d, K, lev, wl, len(b)))
                else:
                    table.append((es[lev] - E0, d, K, lev, np.nan, len(b)))
    table.sort(key=lambda r: r[0])
    res["table"] = table
    gmin = min(r[0] for r in table)
    res["global_below_E0"] = gmin < -TOL
    deg = 1 + sum(1 for r in table if abs(r[0]) < TOL)
    res["D"] = deg if gmin > -TOL else None
    res["gap"] = min(r[0] for r in table if r[0] > TOL) if gmin > -TOL else gmin
    nonlight = [r for r in table if r[0] > TOL and not np.isnan(r[4]) and r[4] < 0.5]
    res["gap_nl"] = nonlight[0][0] if nonlight else np.nan
    res["gap_nl_row"] = nonlight[0] if nonlight else None
    lightrows = [r for r in table if r[0] > TOL and not np.isnan(r[4]) and r[4] >= 0.5]
    res["gap_light"] = lightrows[0][0] if lightrows else np.nan
    res["lowest_rows"] = table[:6]
    six = [r for r in table if r[1] == (1, 1, 0, 0) and r[2] == Kgs and r[3] == 0]
    res["gap6"] = six[0][0] if six else np.nan
    # --- singlet test: raising operators E_{a,a+1} = sum_j c_a^dag(j) c_{a+1}(j) ---
    rn = []
    for a in range(NF - 1):
        terms = [(1.0, [(False, model.p(a + 1, j)), (True, model.p(a, j))]) for j in range(M)]
        dt = [0, 0, 0, 0]; dt[a] += 1; dt[a + 1] -= 1
        tb = chain(model, dt, Kgs)
        out = model.apply_op_sum(terms, b0, g0, tb)
        rn.append(np.linalg.norm(out))
    res["raise_norm"] = max(rn)
    # --- pair field / order parameter ---
    qmax = max(range(G.n), key=lambda m: np.linalg.norm(np.mod(G.kvec[m] + np.pi, 2 * np.pi) - np.pi))
    res["qmax"] = qmax
    Vs = G.n
    for gname in ("S", "M"):
        for q in (0, qmax):
            terms_P, terms_Pd = [], []
            for j in range(M):
                m2 = G.add[q][G.neg[model.moms[j]]]
                if m2 not in model.jof:
                    continue
                j2 = model.jof[m2]
                g = model.f[j] * model.f[j2] if gname == "S" else 1.0
                if abs(g) < 1e-15:
                    continue
                terms_P.append((g, [(False, model.p(1, j2)), (False, model.p(0, j))]))
                terms_Pd.append((g, [(True, model.p(0, j)), (True, model.p(1, j2))]))
            KP = G.add[Kgs][G.neg[q]]; KPd = G.add[Kgs][q]
            bP = chain(model, (-1, -1, 0, 0), KP); bPd = chain(model, (1, 1, 0, 0), KPd)
            vP = model.apply_op_sum(terms_P, b0, g0, bP)
            vPd = model.apply_op_sum(terms_Pd, b0, g0, bPd)
            res[f"S6_{gname}_q{q}"] = 6.0 / Vs * (vP @ vP)
            res[f"S6d_{gname}_q{q}"] = 6.0 / Vs * (vPd @ vPd)
            if want_chi and q == 0:
                chi = 0.0
                for bb, vv in ((bP, vP), (bPd, vPd)):
                    if vv @ vv < 1e-30:
                        continue
                    Ht = model.build_H(bb, W=W, v=v) - E0 * sp.identity(len(bb), format="csr")
                    if Ht.shape[0] <= 4000:
                        x = sla.spsolve(Ht.tocsc(), vv)
                    else:  # iterative (SuperLU fill-in exceeded the memory cap at L = 7)
                        x, info = sla.cg(Ht, vv, rtol=1e-11, maxiter=200000)
                        res['cg_info'] = max(res.get('cg_info', 0), info)
                        res['cg_resid'] = max(res.get('cg_resid', 0.0), float(np.linalg.norm(Ht @ x - vv) / np.linalg.norm(vv)))
                    chi += 2.0 * (vv @ x)
                res[f"chi6_{gname}_perSite"] = 6.0 * chi / Vs
    res["occ0"] = occ0
    res["time"] = time.time() - t0
    return res


def summarize(res, label, P):
    P(f"== {label}: dimGS={res['dimGS']} asym={res['asym']:.1e} time={res['time']:.1f}s")
    P(f"   E0 = {res['E0']:.10f}  E0/site = {res['E0']/res['Vs']:.6f}  D = {res['D']}  any sector below GS-sector: {res['global_below_E0']}")
    P(f"   gap = {res['gap']:.6f}  gap_nonlight = {res['gap_nl']:.6f}  gap_lightattrib = {res['gap_light']:.6f}  gap6(1,1,0,0;K0) = {res['gap6']:.6f}")
    P(f"   max ||E_raise GS|| = {res['raise_norm']:.2e}  (singlet iff ~0)")
    P("   lowest rows (gap, weight d, K, level, w_light, sector dim): " +
      "; ".join(f"({r[0]:.5f},{r[1][:3]},K{r[2]},l{r[3]},w{r[4]:.2f},n{r[5]})" for r in res["lowest_rows"]))
    q = res["qmax"]
    P(f"   S6_psiS(q=0) = {res['S6_S_q0']:.6f}  S6_psiS(qmax={q}) = {res[f'S6_S_q{q}']:.6f}  "
      f"S6_psiM(q=0) = {res['S6_M_q0']:.6f}  S6_psiM(qmax) = {res[f'S6_M_q{q}']:.6f}")
    P(f"   S6dag_psiS(q=0) = {res['S6d_S_q0']:.6f}  S6dag_psiM(q=0) = {res['S6d_M_q0']:.6f}")
    if "chi6_S_perSite" in res:
        P(f"   chi6/site psiS = {res['chi6_S_perSite']:.6f}  chi6/site psiM = {res['chi6_M_perSite']:.6f}")
    if 'cg_resid' in res:
        P(f"   chi via CG: info={res['cg_info']} max rel resid={res['cg_resid']:.1e}")
    P(f"   <n(k)> GS (summed over flavours, per included momentum) = {np.round(res['occ0'], 4).tolist()}")
