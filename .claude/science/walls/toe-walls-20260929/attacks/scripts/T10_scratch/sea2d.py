"""Test A2: the same pointer + free-fermion SEA on a 2D open square lattice (coordination 4).
Question: does the larger coordination number let far or adjacent rectangles carry the bit (R>=3)?"""
import sys, json, itertools
import numpy as np
from gauss import holevo

def run(Lx, T, g, coup):
    N = Lx * Lx
    idx = lambda x, y: x * Lx + y
    h = np.zeros((N, N))
    for x in range(Lx):
        for y in range(Lx):
            for dx, dy in ((1, 0), (0, 1)):
                if x + dx < Lx and y + dy < Lx:
                    h[idx(x, y), idx(x + dx, y + dy)] = h[idx(x + dx, y + dy), idx(x, y)] = -1.0
    j0 = idx(Lx // 2, Lx // 2)
    e, U = np.linalg.eigh(h)
    # half filling: fill lowest N/2 states (degeneracies: take a definite subset; both branches share the same initial state)
    Phi0 = U[:, : N // 2]
    def ev(V):
        hs = h.copy(); hs[j0, j0] += V
        w, Ws = np.linalg.eigh(hs)
        return (Ws * np.exp(-1j * w * T)[None, :]) @ Ws.conj().T @ Phi0
    Vu, Vd = (g, 0.0) if coup == "proj" else (g, -g)
    Pu, Pd = ev(Vu), ev(Vd)
    Du, Dd = Pu.conj() @ Pu.T, Pd.conj() @ Pd.T
    best_contact = 0.0; best_away = 0.0; where = None
    shapes = [(a, b) for a in range(1, 5) for b in range(1, 5) if a * b <= 8]
    for (a, b) in shapes:
        for x0 in range(Lx - a + 1):
            for y0 in range(Lx - b + 1):
                sites = [idx(x0 + i, y0 + j) for i in range(a) for j in range(b)]
                D1 = Du[np.ix_(sites, sites)]; D2 = Dd[np.ix_(sites, sites)]
                if np.linalg.norm(D1 - D2) < 1e-7: continue
                c = holevo(D1, D2)
                if j0 in sites:
                    best_contact = max(best_contact, c)
                elif c > best_away:
                    best_away = c; where = (x0 - Lx // 2, y0 - Lx // 2, a, b)
    return dict(Lx=Lx, T=T, g=g, coup=coup, max_contact=best_contact, max_away=best_away, away_at=where)

for Lx, T in ((12, 2.5), (16, 3.5)):
    for g in (3.0, 20.0):
        for coup in ("proj", "sym"):
            o = run(Lx, T, g, coup); print(json.dumps(o), flush=True)
            open("results_sea2d.jsonl", "a").write(json.dumps(o) + "\n")
