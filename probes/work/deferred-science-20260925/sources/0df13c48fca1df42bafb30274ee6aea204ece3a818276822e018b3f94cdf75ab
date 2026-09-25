"""Personal exploratory exact rows; no charged-particle or binding theorem yet."""
from pathlib import Path
from collections import Counter, defaultdict
from itertools import product
from fractions import Fraction
import hashlib, importlib.util, json, sys, time
import numpy as np
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent
E=HERE.parent
SOURCE=E/'native-one-pair-spectrum-personal/native_pair_controls.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='6d874248e3f7c3963f6fa3c6ec38c8bd9f465efc870fc29a740ec16bb290c9aa'
spec=importlib.util.spec_from_file_location('prior_personal_exact_pairs',SOURCE)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)

def neighbors(v):
    for k in range(3):
        for s in (-1,1):
            w=list(v);w[k]+=s;yield tuple(w)

def pairs_near(b):
    return {tuple(sorted((a,c))) for a in neighbors(b)
            for d in neighbors(a) for c in neighbors(d) if c!=a}

def kind(d):return tuple(sorted(map(abs,d)))

def row(d):
    origin=(1,0,0);x=(origin,tuple(a+b for a,b in zip(origin,d)))
    pairs=sorted(pairs_near(x[0])|pairs_near(x[1]));records=[];near=defaultdict(set)
    for i,(a,c) in enumerate(pairs):
        assignments=Counter(tuple(sorted((u,v))) for u in neighbors(a) for v in neighbors(c) if u!=v)
        records.append((a,c,assignments,2*sum(m*m for m in assignments.values())))
        for b in set(neighbors(a))|set(neighbors(c)):near[b].add(i)
    raw=prior.local_delta_row(x,records,near)
    grouped=Counter()
    for y,value in raw.items():
        diff=tuple(b-a for a,b in zip(*y));grouped[kind(diff)]+=value
    return dict(grouped)

def main():
    tick=time.perf_counter()
    classes=sorted({tuple(sorted(d)) for d in product(range(7),repeat=3)
                    if 0<sum(d)<=6 and sum(d)%2==0})
    small=[(0,0,2),(0,1,1)];rows=[];A=[];B=[]
    for d in classes:
        r=row(d);corr=sum(r.values())-12096
        coefs=[-r.get(s,0)+(12096 if d==s else 0) for s in small]
        rows.append({'displacement_type':d,'row_sum':sum(r.values()),'correction':corr,
                     'deficit_coefficients':coefs,'grouped_exact_row':[[list(k),v] for k,v in sorted(r.items())]})
        A.append(coefs);B.append(-corr)
    fit=linprog([1.,1.],A_ub=np.asarray(A,dtype=float),b_ub=np.asarray(B,dtype=float),
                bounds=[(0,0.9),(0,0.9)],method='highs')
    proposed=None;exact=None
    if fit.success:
        proposed=[Fraction(float(x)).limit_denominator(10**8) for x in fit.x]
        exact=[Fraction(row['correction'])+sum(Fraction(c)*v for c,v in zip(row['deficit_coefficients'],proposed)) for row in rows]
    result={'scope':'Exploration of a flat-magnetic occupancy-pair threshold using prior exact root row machinery. No physical charge, finite-coupling binding, infinite-volume or audited result.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'reused_helper_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'classes':rows,'lp_success':bool(fit.success),'lp_message':fit.message,
            'proposed_deficits':None if proposed is None else [str(x) for x in proposed],
            'exact_supersolution_residuals':None if exact is None else [str(x) for x in exact],
            'all_listed_residuals_nonpositive':None if exact is None else all(x<=0 for x in exact),
            'elapsed_seconds':time.perf_counter()-tick}
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
