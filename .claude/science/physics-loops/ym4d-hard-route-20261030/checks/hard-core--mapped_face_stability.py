#!/usr/bin/env python3
"""The response next to a frozen face, for data small in l^2 at brick scale. Consumer: the definition of quiet in `library/quiet-boundary-rarity.md`, which this tests against the earlier sup-norm form.

Written before running. The earlier repair of the gate's D3 took quiet := flux at most T_q := T/(2 C_bd), with C_bd the largest flux of a minimiser next to frozen data of flux at most 1. `checks/hard-core--mapped_face_constant.py` found C_bd growing with L in d = 3, at a logarithm on a flat face. At a re-entrant corner of a staircase of bricks, harmonic theory suggests worse: a singular mode of amplitude (scale/r)^gamma with 0 < gamma < 1, which that check did not test. A power of L in C_bd would break the descent at T_q.

New definition: a brick is quiet if the l^2 norm over the brick of the difference of its plaquette angles from those of the local lift of its parents is at most eps_q T. Then the response of the minimiser to the data is bounded by energy stability alone: sup over free plaquettes of |response| <= (energy of response)^(1/2) <= C_s (l^2 norm of data). So C_s, not C_bd, is the constant, with no Calderon-Zygmund and no corner analysis. This check measures C_s.

Model: U(1), one level, flat parents, the block constraint of `checks/hard-core--mapped_face_constant.py`, torus (Nc L) x (Nt L)^(d-1). Frozen set: (flat) x_0 in a band of 2 L; (step) x_0 in a band of 2 L if x_1 < L and 3 L otherwise, so the free region has re-entrant edges. As in that check, minimise the free energy with mixed parent constraints imposed, and frozen-only parent constraints imposed on the data.

 C_s := max over target free plaquettes k of sup over band data u of G_k u / ||D_band u||_2.

For a target k, sup^2 = G_k^T y, with y solving the saddle system of D_band^T D_band with the frozen-only constraints. The targets: all free plaquettes in the column nearest the frozen set, one block along direction 1 for flat, and the three columns nearest the edge for step, with other coordinates at the block centre.

PRE-STATED criteria.
 C0. Residual: the constraint residual at the optimal data is at most 1e-6.
 C1. Flat: C_s(L) in d = 3 at L = 3, 5, 7 with 2 blocks across: C_s(7) <= 1.25 C_s(5), and C_s at most 3. In d = 4, L = 3 and 5 at 1 block across and L = 3 at 2 blocks across: at most 3.
 C2. Step: in d = 3 at the same L: C_s(step, L) <= 2 C_s(flat, L), and C_s(step, 7) <= 1.25 C_s(step, 5). In d = 4, at L = 3 with 2 blocks across: <= 2 C_s(flat). (A first run had L = 9 as well: flat 0.3186, 0.3019, 0.2901, 0.2839, passing, and its factorisation went over the RSS guard at 2.46 GB, which stopped it before the step. So L = 9 is dropped from the list. The criteria are otherwise as first written.)
 C3. Reported, for contrast: on the same step geometry, the response at the target nearest the edge to a coherent test datum of flux at most 1, namely the sign of G_k on band plaquettes where this is realisable: the value of G_k u / max |D_band u| for u the l^2 optimiser rescaled. If this grows with L while C_s does not, the new definition is doing its job.
FAIL if C0, C1 or C2 fails.

Limits. U(1), one level, Wilson action, flat parents, stepped band, a few targets. The non-abelian form is by convexity in the chart, which this does not test. RSS guard 2 GB.
"""
import importlib.util
import itertools
import os
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("fc", os.path.join(HERE, "hard-core--mapped_face_constant.py"))
fc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fc)


class Geometry(fc.Model):
    def __init__(self, d, L, Nc, Nt, step):
        super().__init__(d, L, Nc, Nt)
        self.step = step

    def frozen_site(self, x):
        w = self.band
        if self.step and (x[1] % self.shape[1]) >= self.L:
            w = self.band + self.L
        return (x[0] % self.shape[0]) < w

    def frozen_mask(self):
        frozen = np.zeros(self.nl, bool)
        for x in itertools.product(*[range(s) for s in self.shape]):
            for m in range(self.d):
                x2 = list(x)
                x2[m] += 1
                if self.frozen_site(x) and self.frozen_site(x2):
                    frozen[self.link(x, m)] = True
        return frozen


def run(d, L, Nc, Nt, step):
    M = Geometry(d, L, Nc, Nt, step)
    D, meta = M.plaquettes()
    Q = M.constraints()
    fr = M.frozen_mask()
    F = np.nonzero(~fr)[0]
    B = np.nonzero(fr)[0]
    Df, Db = D[:, F].tocsr(), D[:, B].tocsr()
    Qf, Qb = Q[:, F].tocsr(), Q[:, B].tocsr()
    mixed = np.asarray(np.abs(Qf).sum(axis=1)).ravel() > 1e-14
    Qm_f, Qm_b = Qf[mixed], Qb[mixed]
    Qff = Qb[~mixed]
    nf, nc = Df.shape[1], Qm_f.shape[0]
    reg = 1e-9
    K = sp.bmat([[Df.T @ Df + reg * sp.identity(nf), Qm_f.T], [Qm_f, -reg * sp.identity(nc)]], format="csc")
    lu = spla.splu(K, permc_spec="COLAMD")
    fc.guard()
    # Band plaquettes: those all of whose links are frozen.
    allfrozen = np.asarray((np.abs(D[:, F]) > 0).sum(axis=1)).ravel() == 0
    Dband = Db[allfrozen]
    nb = Db.shape[1]
    nq = Qff.shape[0]
    Kb = sp.bmat([[Dband.T @ Dband + reg * sp.identity(nb), Qff.T], [Qff, -reg * sp.identity(nq)]], format="csc")
    lub = spla.splu(Kb, permc_spec="COLAMD")
    fc.guard()
    # Targets.
    N0 = M.shape[0]
    targets = []
    for k, (x, mu, nu, ib) in enumerate(meta):
        if allfrozen[k]:
            continue
        # Plaquettes with no frozen link and next to the frozen set, or mixed ones.
        x0 = x[0]
        if d > 2 and any(x[i] != M.h for i in range(2, d) if i not in (mu, nu)):
            continue
        if not step:
            if x0 != M.band - 1 or x[1] >= L:
                continue
        else:
            # Near the re-entrant edge at x_0 = band, x_1 = 0 or L.
            near0 = abs(x0 - (M.band - 1)) <= 2
            near1 = min(abs(x[1] - L), abs(x[1] - (L - 1))) <= 2
            if not (near0 and near1):
                continue
        targets.append(k)
    best, where = 0.0, None
    res = 0.0
    coh = 0.0
    for k in targets:
        df_k = Df[k].toarray().ravel()
        if not np.any(df_k):
            continue
        w = lu.solve(np.concatenate([df_k, np.zeros(nc)]))
        wx, wl = w[:nf], w[nf:]
        G = Db[k].toarray().ravel() - (Db.T @ (Df @ wx)) - (Qm_b.T @ wl)
        sol = lub.solve(np.concatenate([G, np.zeros(nq)]))
        y = sol[:nb]
        val2 = float(G @ y)
        val = val2**0.5 if val2 > 0 else 0.0
        if val > best:
            best, where = val, meta[k][:3]
            rhs = np.concatenate([-(Df.T @ (Db @ y)), -(Qm_b @ y)])
            s2 = lu.solve(rhs)
            res = max(res, float(np.max(np.abs(Qm_f @ s2[:nf] + Qm_b @ y))) if nc else 0.0)
            coh = float(G @ y) / max(float(np.max(np.abs(Dband @ y))), 1e-30)
    print(f" d={d} L={L} Nc={Nc} Nt={Nt} step={step}: links={M.nl} targets={len(targets)}: C_s={best:.4f} at {where}, residual={res:.1e}; coherent response per unit sup data {coh:.3f}, rss={fc.rss_gb():.2f}GB", flush=True)
    return best, res


def main():
    ok = True
    print("C1 flat, d = 3", flush=True)
    flat = {}
    for L in (3, 5, 7):
        flat[L], r = run(3, L, 5, 2, False)
        ok = ok and r <= 1e-6
    good = flat[7] <= 1.25 * flat[5] and max(flat.values()) <= 3
    ok = ok and good
    print(f" C1 d = 3: {good}", flush=True)
    print("C2 step, d = 3", flush=True)
    st = {}
    for L in (3, 5, 7):
        st[L], r = run(3, L, 5, 2, True)
        ok = ok and r <= 1e-6
    good = all(st[L] <= 2 * flat[L] for L in st) and st[7] <= 1.25 * st[5]
    ok = ok and good
    print(f" C2 d = 3: {good}", flush=True)
    print("d = 4", flush=True)
    f4 = {}
    for L, Nt in ((3, 1), (5, 1), (3, 2)):
        f4[(L, Nt)], r = run(4, L, 5, Nt, False)
        ok = ok and r <= 1e-6
    good = max(f4.values()) <= 3
    ok = ok and good
    print(f" C1 d = 4: {good}", flush=True)
    s4, r = run(4, 3, 5, 2, True)
    good = s4 <= 2 * f4[(3, 2)] and r <= 1e-6
    ok = ok and good
    print(f" C2 d = 4: {good}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
