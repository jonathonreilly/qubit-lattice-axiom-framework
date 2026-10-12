#!/usr/bin/env python3
"""Test the supplied endpoint-flavor identification of one Jacobi operator."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq
from scipy.special import roots_genlaguerre, gamma


def forward(shape):
    diagonal=2*np.arange(3)+shape
    off=-np.sqrt(np.arange(1,3)*(np.arange(2)+shape))
    nodes,vectors=eigh_tridiagonal(diagonal,off)
    probabilities=vectors*vectors
    w=probabilities[0]
    x2,weights=roots_genlaguerre(3,shape-1)
    assert np.max(np.abs(nodes-x2))<5e-13
    assert np.max(np.abs(w-weights/gamma(shape)))<5e-13
    assert np.max(np.abs(probabilities.sum(axis=0)-1))<5e-14
    return dict(shape=float(shape),mass_coordinates=list(map(float,nodes)),
                electron_probabilities=list(map(float,w)),
                reactor_amplitude=float(4*w[2]*(1-w[2])),
                sin2_theta12=float(w[1]/(1-w[2])),
                sin2_theta23=float(probabilities[1,2]/(1-w[2])),
                fixed_mass_gap_ratios={str(p):float((nodes[1]**p-nodes[0]**p)/(nodes[2]**p-nodes[0]**p)) for p in [1,2]},
                cp_odd_invariant=0)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    # Numerical scan checks a branch; it is not a proof of global monotonicity.
    grid=np.geomspace(.01,10,301)
    scan=[forward(float(s)) for s in grid]
    assert all(a['reactor_amplitude']<b['reactor_amplitude'] for a,b in zip(scan[:-1],scan[1:]))
    answers=[]
    for label,amplitude in [('low',.0851-1.96*.0024),('central',.0851),('high',.0851+1.96*.0024)]:
        shape=brentq(lambda s:forward(s)['reactor_amplitude']-amplitude,.01,10,xtol=2e-14)
        row=forward(shape);row.update(calibration_label=label,calibration_amplitude=amplitude)
        answers.append(row)
    result=dict(status='conditional calibration and unfitted forward outputs',
                primary_calibration='Daya Bay 2211.14988v1 standard three-flavor fitted summary; solar inputs conditioned',
                no_test_observation_scored=True,protocol_sha256=hashlib.sha256(Path(__file__).with_name('FLAVOR_ENDPOINT_PROTOCOL.md').read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                branch_scan=dict(points=len(grid),shape_domain=[.01,10],strict_increase_on_scan=True,global_monotonicity_proof=False),
                results=answers)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(answers,indent=2))


if __name__=='__main__':main()
