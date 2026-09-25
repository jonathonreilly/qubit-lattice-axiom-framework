"""Explore larger exact positive supersolutions; failed short ansatz retained."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import argparse, hashlib, importlib.util, json, time
import numpy as np
from scipy.optimize import linprog
import sympy as sp

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'explore_two_record_threshold.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='0df13c48fca1df42bafb30274ee6aea204ece3a818276822e018b3f94cdf75ab'
spec=importlib.util.spec_from_file_location('personal_pair_row',SOURCE)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)

def classes(radius):
    return sorted({tuple(sorted(d)) for d in product(range(radius+1),repeat=3)
                   if 0<sum(d)<=radius and sum(d)%2==0})

def main():
    p=argparse.ArgumentParser();p.add_argument('--radius',type=int,required=True);p.add_argument('--output',required=True);args=p.parse_args()
    tick=time.perf_counter();small=classes(args.radius);domain=classes(args.radius+4)
    rows=[];A=[];B=[]
    for d in domain:
        row=base.row(d);correction=sum(row.values())-12096
        coefs=[-row.get(s,0)+(12096 if d==s else 0) for s in small]
        rows.append({'displacement_type':d,'row_sum':sum(row.values()),'correction':correction,
                     'grouped_exact_row':[[list(k),v] for k,v in sorted(row.items())],
                     'deficit_coefficients':coefs});A.append(coefs);B.append(-correction)
    af=np.asarray(A,dtype=float);bf=np.asarray(B,dtype=float)
    fit=linprog(np.ones(len(small)),A_ub=af,b_ub=bf,bounds=[(0,0.99)]*len(small),method='highs')
    certificate=None
    if fit.success:
        active=[(r,b) for r,b,x in zip(A,B,af@fit.x-bf) if abs(x)<1e-7]
        for i,x in enumerate(fit.x):
            if abs(x)<1e-9:
                row=[0]*len(small);row[i]=1;active.append((row,0))
        mat=sp.Matrix([r for r,b in active]);pivots=mat.T.rref()[1]
        if len(pivots)==len(small):
            chosen=[active[i] for i in pivots];exact=sp.Matrix([r for r,b in chosen]).inv()*sp.Matrix([b for r,b in chosen])
            values=[Fraction(int(x.p),int(x.q)) for x in exact]
            residuals=[sum(Fraction(c)*v for c,v in zip(r,values))-b for r,b in zip(A,B)]
            certificate={'deficits':[{'type':d,'value':str(v)} for d,v in zip(small,values)],
                         'residuals':[{'type':d,'value':str(v)} for d,v in zip(domain,residuals)],
                         'all_deficits_in_zero_one':all(0<=v<1 for v in values),
                         'all_residuals_nonpositive':all(v<=0 for v in residuals),
                         'chosen_active_constraints':pivots}
    result={'scope':'Personal exact flat occupancy exploration. No physical charge identification, full finite-g binding or infinite-volume theorem inferred from LP.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'row_source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'radius':args.radius,'variables':len(small),'inequalities':len(domain),'rows':rows,
            'lp_success':bool(fit.success),'lp_message':fit.message,'exact_certificate':certificate,
            'elapsed_seconds':time.perf_counter()-tick}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))

if __name__=='__main__':main()
