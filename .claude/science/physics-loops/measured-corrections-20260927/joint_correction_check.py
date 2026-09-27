"""Check derived first joint-scaling correction against full microscopic data."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal
rows=[json.loads(s) for s in Path(__file__).with_name('finite_spin_square.jsonl').read_text().splitlines()]
for row in rows:
    K=1.;delta=row['delta_over_K'];x=row['epsilon']**2
    n=np.arange(-100,101,dtype=float)
    e,v=eigh_tridiagonal(4*K*n*n-4*delta,np.full(200,-2*delta),select='i',select_range=(0,6))
    diagonal=8*delta-8*K*n*n
    off=4*delta+4*K*n[:-1]*(n[:-1]+1)
    shift=(diagonal[:,None]*v*v).sum(axis=0)+2*(off[:,None]*v[:-1]*v[1:]).sum(axis=0)
    predicted=x*(shift[1:]-shift[0]);actual=np.array(row['gap_difference'])
    print(json.dumps(dict(S=row['S'],delta_over_K=delta,x=x,predicted_gap_change=predicted.tolist(),actual_gap_change=actual.tolist(),max_remaining_gap_error=float(max(abs(actual-predicted))),remaining_error_over_x2=float(max(abs(actual-predicted))/x**2))))
