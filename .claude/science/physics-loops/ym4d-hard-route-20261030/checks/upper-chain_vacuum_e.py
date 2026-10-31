#!/usr/bin/env python3
"""Criterion C1: vacuum value of e_a at beta = 4 on a periodic lattice."""
import importlib.util, os, sys, resource
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("es", os.path.join(here, "upper-chain_energy_sign.py"))
es = importlib.util.module_from_spec(spec); spec.loader.exec_module(es)


def main(T, beta, nsweeps, seed):
    rng = np.random.default_rng(seed)
    lat = es.Torus(T, beta, rng)
    for _ in range(500):
        lat.sweep()
    vals = []
    for it in range(nsweeps):
        lat.sweep()
        tot = sum(np.mean(1 - lat.plaq_trace(m, n)) for m in range(4) for n in range(m + 1, 4))
        vals.append(tot)
        if it % 1000 == 0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > 2.0:
            sys.exit("RSS")
    vals = np.array(vals)
    nb = 20
    b = vals[: len(vals) // nb * nb].reshape(nb, -1).mean(axis=1)
    print(f"RESULT T={T} beta={beta} m={b.mean():.6f}+-{b.std(ddof=1)/np.sqrt(nb):.6f}", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
