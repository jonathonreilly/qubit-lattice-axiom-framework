"""Equilibrium (thermal) dilute free-fermion gas as the environment: same chain, same pointer coupling as the attack.
D0 = f(H0) with Fermi function; evolve with H_s; windows scored by number-lower-bound (any size) and exact Holevo (cap 8)."""
import numpy as np, json, sys
import beam_vs_sea as b
from numbound import scan_num, disjoint
from gauss import holevo

def thermal_D(L, mu, Tth):
    h = b.chain_h(L)
    e, U = np.linalg.eigh(h)
    f = 1.0 / (np.exp((e - mu) / Tth) + 1.0)
    return h, U, f

def evolve_D(h, j0, V, U, f, T):
    hs = h.copy(); hs[j0, j0] += V
    w, Ws = np.linalg.eigh(hs)
    Ut = (Ws * np.exp(-1j * w * T)[None, :]) @ Ws.conj().T
    P = Ut @ U
    return (P.conj() * f[None, :]) @ P.T      # D[x,y] = sum_k f_k conj(P[x,k]) P[y,k]

def run(L, mu, Tth, g, coup, T, caps=(8, 18, 36, 60), exact_cap=8):
    h, U, f = thermal_D(L, mu, Tth)
    dens = f.sum() / L
    j0 = L // 2
    Vu, Vd = (g, 0.0) if coup == 'proj' else (g, -g)
    Du = evolve_D(h, j0, Vu, U, f, T); Dd = evolve_D(h, j0, Vd, U, f, T)
    r = int(2 * T + 10); lo, hi = max(1, j0 - r), min(L - 1, j0 + r)
    out = dict(L=L, mu=mu, Tth=Tth, dens=round(float(dens), 4), g=g, coup=coup, T=T)
    tabmax = scan_num(Du, Dd, lo, hi, max(caps))
    for cap in caps:
        tab = {k: v for k, v in tabmax.items() if k[1] <= cap}
        out[f'num_cap{cap}'] = dict(R09=len(disjoint(tab, 0.9)), R07=len(disjoint(tab, 0.7)), R05=len(disjoint(tab, 0.5)), max=round(max(tab.values()), 3))
    # exact Holevo (mixed Gaussian) for windows <= exact_cap
    ex = {}
    for i in range(lo, hi):
        for m in range(1, exact_cap + 1):
            if i + m > hi: break
            a, c = Du[i:i+m, i:i+m], Dd[i:i+m, i:i+m]
            ex[(i, m)] = 0.0 if np.linalg.norm(a - c) < 1e-7 else holevo(a, c)
    out['exact_cap8'] = dict(R09=len(disjoint(ex, 0.9)), R05=len(disjoint(ex, 0.5)), R03=len(disjoint(ex, 0.3)), max=round(max(ex.values()), 3))
    ov_note = None
    return out

if __name__ == '__main__':
    settings = [(-3.0, 1.0), (-2.5, 0.8), (-1.5, 1.0), (0.0, 0.5)]   # last is near-degenerate half-filled sea
    for mu, Tth in settings:
        o = run(400, mu, Tth, 20.0, 'proj', 44.0)
        print(json.dumps(o), flush=True)
        open('k3_thermal.jsonl', 'a').write(json.dumps(o) + '\n')
