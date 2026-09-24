#!/usr/bin/env python3
"""Post-selection diagnostic: exact finite-spin probability at positive n>=S."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("probe", HERE / "fixed_time_probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

def run(S):
    C = S*(S+1)
    radius = max(400, 12*S + 20)
    nodes, inv = probe.path_basis(radius)
    ns = sorted(n for n, st in nodes.items() if max(abs(e) for e in st[1]) <= S)
    states = {n: nodes[n] for n in ns}
    H2 = probe.sparse_from_rows(probe.h2_rows(states, inv, S), ns)
    H4 = probe.sparse_from_rows(probe.h4_rows(states, inv, S), ns)
    G = C*H2 + H4
    psi0 = np.zeros(len(ns), dtype=np.complex128)
    psi0[ns.index(0)] = 1
    rows = []
    for t in (0.25, 0.5, 1.0):
        psi = expm_multiply((-1j*t)*G, psi0)
        p_vacancy = float(sum(abs(psi[j])**2 for j,n in enumerate(ns) if states[n][0][3] == 0))
        p_macro = float(sum(abs(psi[j])**2 for j,n in enumerate(ns) if n >= S))
        p_half = float(sum(abs(psi[j])**2 for j,n in enumerate(ns) if n >= S/2))
        rows.append({"time": t, "vacancy_B3": p_vacancy, "prob_n_ge_S": p_macro, "prob_n_ge_S_over_2": p_half,
                     "norm_squared": float(np.vdot(psi,psi).real)})
    return {"S": S, "C": C, "dimension": len(ns), "physical_interval": [ns[0],ns[-1]],
            "postselected_diagnostic": "positive path-coordinate projector 1[n>=S]; also 1[n>=S/2]",
            "times": rows}

def main():
    spins = tuple(int(x) for x in sys.argv[1:]) if len(sys.argv) > 1 else (8,12,16,24,32,48,64)
    results = [run(S) for S in spins]
    out = {"status": "floating-point state-tail diagnostic; chosen after exact macro-edge mismatch; not a certified limit",
           "initial_state": "actual supplied output at n=0", "operator": "exact finite-spin C H2,S + H4,S",
           "results": results,
           "interpretation": "tests actual finite-spin amplitude near the n/S=1 witness region; cannot alone settle the limit or the rotor comparison"}
    target = "EXACT_MACROSCOPIC_TAIL.json" if spins == (8,12,16,24,32,48,64) else f"EXACT_MACROSCOPIC_TAIL_{spins[0]}_{spins[-1]}.json"
    (HERE / target).write_text(json.dumps(out, indent=2)+"\n")
    for row in results:
        print(json.dumps(row), flush=True)

if __name__ == "__main__":
    main()
