#!/usr/bin/env python3
"""Floating-point candidate-rotor comparison with cutoff variation."""
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

def run(S, cutoff):
    C = S*(S+1)
    radius = max(400, 5*cutoff + 20)
    nodes, inv = probe.path_basis(radius)
    ns = list(range(-cutoff, cutoff+1))
    states = {n: nodes[n] for n in ns}
    H2 = probe.sparse_from_rows(probe.h2_rows(states, inv, None), ns)
    D = probe.sparse_from_rows(probe.d_rows(states, inv), ns)
    H4 = probe.sparse_from_rows(probe.h4_rows(states, inv, None), ns)
    G = C*H2 + D + H4
    psi0 = np.zeros(len(ns), dtype=np.complex128)
    psi0[cutoff] = 1
    rows=[]
    for t in (0.25,0.5,1.0):
        psi=expm_multiply((-1j*t)*G,psi0)
        rows.append({"time":t,
            "vacancy_B3":float(sum(abs(psi[j])**2 for j,n in enumerate(ns) if states[n][0][3]==0)),
            "prob_n_ge_S":float(sum(abs(psi[j])**2 for j,n in enumerate(ns) if n>=S)),
            "norm_squared":float(np.vdot(psi,psi).real)})
    return {"S":S,"C":C,"cutoff":cutoff,"dimension":len(ns),"times":rows}

def main():
    results=[]
    spins=tuple(int(x) for x in sys.argv[1:]) if len(sys.argv)>1 else (24,32,48,64)
    for S in spins:
        rows=[run(S,mult*S) for mult in (12,24)]
        results.append({"S":S,"cutoff_runs":rows})
        print(json.dumps(results[-1]),flush=True)
    out={"status":"uncertified finite-cutoff expm_multiply diagnostic",
         "operator":"C H2,infinity + D + H4,infinity with principal path truncation",
         "initial_state":"n=0, corresponding to the supplied resolved output",
         "observables":"frozen vacancy_B3 and post-selected macro-tail 1[n>=S]",
         "results":results,
         "limits":"cutoff variation and floating-point values do not prove convergence to the Friedrichs evolution or an asymptotic discrepancy"}
    target="CANDIDATE_MACROSCOPIC_TAIL.json" if spins==(24,32,48,64) else f"CANDIDATE_MACROSCOPIC_TAIL_{spins[0]}_{spins[-1]}.json"
    (HERE/target).write_text(json.dumps(out,indent=2)+"\n")

if __name__=="__main__":
    main()
