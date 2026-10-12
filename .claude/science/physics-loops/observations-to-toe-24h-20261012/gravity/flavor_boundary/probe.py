#!/usr/bin/env python3
"""Boundary-defect candidate V2; fitted summaries, no raw likelihood."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import least_squares


def lower_boundary(s):
    return min(s,1.)


def forward(s,b):
    nodes,u=eigh_tridiagonal([b,s+2,s+4],[-np.sqrt(s),-np.sqrt(2*(s+1))])
    prob=u*u
    w=prob[0]
    assert nodes[0]>0 and np.max(abs(prob.sum(axis=0)-1))<2e-14
    return dict(shape=float(s),boundary=float(b),defect=float(b-s),
                distance_above_positive_threshold=float(b-lower_boundary(s)),
                nodes=nodes.tolist(),electron_probabilities=w.tolist(),
                reactor_amplitude=float(4*w[2]*(1-w[2])),
                sin2_theta12=float(w[1]/(1-w[2])),
                sin2_theta23=float(prob[1,2]/(1-w[2])),
                cp_odd_invariant=0.,
                mass_gap_ratios={str(p):float((nodes[1]**p-nodes[0]**p)/(nodes[2]**p-nodes[0]**p)) for p in (1,2)})


def physical(q):
    s,t=q
    lo=lower_boundary(s)
    return s,lo+(30-lo)*t


def solve(amplitude,solar):
    def residual(q):
        s,b=physical(q)
        row=forward(s,b)
        return [(row['reactor_amplitude']-amplitude)/.0024,(row['sin2_theta12']-solar)/.0087]
    records=[];roots=[]
    for s0 in (.02,.1,.4,.9,1.1,2.,4.,7.,9.5):
        for t0 in (.001,.01,.05,.15,.4,.8):
            fit=least_squares(residual,[s0,t0],bounds=([.01,0],[10,1]),
                              ftol=2e-13,xtol=2e-13,gtol=2e-13,max_nfev=300)
            s,b=physical(fit.x);err=float(np.linalg.norm(fit.fun))
            records.append(dict(start=[s0,t0],s=float(s),b=float(b),residual_norm=err,
                                success=bool(fit.success),nfev=int(fit.nfev)))
            if err<1e-7 and all(np.linalg.norm(np.array([s,b])-np.array([r['shape'],r['boundary']]))>1e-6 for r in roots):
                roots.append(forward(s,b))
    best=min(records,key=lambda r:r['residual_norm'])
    return dict(calibration=dict(reactor_amplitude=amplitude,solar_sin2=solar),
                roots=roots,best=best,all_starts=records)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    targets=[('central',.0851,.3092)]
    for i in (-1,1):
        for j in (-1,1):
            targets.append((f'marginal_rectangle_{i}_{j}',.0851+i*1.96*.0024,.3092+j*1.96*.0087))
    results=[]
    for label,amplitude,solar in targets:
        row=solve(amplitude,solar);row['label']=label;results.append(row)
    output=dict(status='conditional V2 numerical calibration; forward targets unfitted',
                protocol_sha256=hashlib.sha256(Path(__file__).with_name('PROTOCOL.md').read_bytes()).hexdigest(),
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                shape_bounds=[.01,10],boundary_upper=30,search_is_not_uniqueness_proof=True,
                results=results)
    Path(args.output).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps([{k:r[k] for k in ('label','calibration','roots','best')} for r in results],indent=2))


if __name__=='__main__':main()
