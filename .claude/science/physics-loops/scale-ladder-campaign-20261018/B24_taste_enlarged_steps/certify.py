"""B24 certificate helper (used only if a screen-level clean candidate appears).
Bauer-Fike / Lipschitz exclusion: W unitary (normal), so every eigenvalue moves by at most ||W(k) - W(k')|| <= Lip |k - k'|,
Lip = b24base.lip_bound(w) (rigorous sum of letter gradient norms).  A cube of half-diagonal rho centred at k contains no
k' with e^{iE} in spec W(k') if chord_E(w, k, E) > Lip * rho.  Cubes failing the test are bisected up to maxdepth;
cubes inside balls of radius r0 around the listed nodes are skipped."""
import numpy as np
from b24lib import *
def certify(w, E, nodes, r0=0.03, n0=16, maxdepth=6):
    Lip = lip_bound(w); h0 = 2 * np.pi / n0
    g = (np.arange(n0) + 0.5) * h0 - np.pi
    cells = [(np.array(c), h0) for c in itertools.product(g, repeat=3)]
    nodes = [np.asarray(x) for x in nodes]; bad = 0; evals = 0
    for depth in range(maxdepth + 1):
        if not cells: break
        ks = np.array([c for c, _ in cells]); hs = np.array([h for _, h in cells])
        d = chord_E(w, ks, E); evals += len(ks)
        rho = hs * np.sqrt(3) / 2
        nxt = []
        for (c, h), dd, rr in zip(cells, d, rho):
            if dd > Lip * rr: continue
            if any(np.linalg.norm(wrap(c - n)) + rr < r0 for n in nodes): continue
            if depth == maxdepth: bad += 1; continue
            for s in itertools.product((-0.25, 0.25), repeat=3): nxt.append((c + np.array(s) * h, h / 2))
        cells = nxt
    return bad == 0, bad, evals, Lip
