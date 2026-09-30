#!/usr/bin/env python3
"""T25 test B2: dimension of the band-touching set for each coin class (isolated points vs lines vs surfaces),
from the rank of the Jacobian of d(k) = (Re h12, Im h12, (h11-h22)/2) at each zero. Reuses test_T25B.py machinery."""
import json, numpy as np
import importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location("tb", "test_T25B.py")
tb = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(tb)   # re-runs B (about a minute); gives us functions + rng-state members

def dvec(M0, Ma, k):
    h = tb.h_of_k(M0, Ma, k)
    return np.array([h[0, 1].real, h[0, 1].imag, (h[0, 0] - h[1, 1]).real / 2])

def jac(M0, Ma, k, eps=1e-6):
    J = np.zeros((3, 3))
    for i in range(3):
        e = np.zeros(3); e[i] = eps
        J[:, i] = (dvec(M0, Ma, k + e) - dvec(M0, Ma, k - e)) / (2 * eps)
    return J

rng = np.random.default_rng(11)
res = {}
for rep in ["spinor_G1", "E", "1+A2", "trivial_1+1"]:
    NS = tb.nullspace(tb.constraint_matrix(rep))
    ranks = []
    nz = 0
    for trial in range(3):
        u = NS @ rng.normal(size=NS.shape[1]); M0, Ma = tb.unpack(u)
        zeros, gmin = tb.touching_points(M0, Ma, N=20)
        for z in zeros:
            s = np.linalg.svd(jac(M0, Ma, z), compute_uv=False)
            ranks.append(int(np.sum(s > 1e-6)))
        nz += len(zeros)
    res[rep] = {"n_zeros_found": nz, "jacobian_rank_histogram": {str(r): ranks.count(r) for r in sorted(set(ranks))}}
    print(rep, res[rep])
json.dump(res, open("test_T25B2_results.json", "w"), indent=1)
