"""Find a finite plaquette filling, then verify its energy-power bound exactly.

The numerical linear program only proposes coefficients. Rational equality
of every link and the displayed inequality are checked independently of the
optimizer's feasibility tolerance or optimality report. Root author control.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product, combinations
from pathlib import Path
import hashlib, json, time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, hstack


def face(x, mu, nu):
    y=list(x); y[mu]+=1
    z=list(x); z[nu]+=1
    return {(x,mu):1,(tuple(y),nu):1,(tuple(z),mu):-1,(x,nu):-1}


def run():
    source=Path(__file__).with_name('POWER_SPECTRAL_RESULTS.json')
    data=json.loads(source.read_text())
    t={(tuple(r['positive_edge_origin']),r['axis']):Fraction(r['coefficient']) for r in data['t_vector']}
    c=face((0,0,0),0,1); lam=1550
    target={e:t.get(e,0)-lam*c.get(e,0) for e in set(t)|set(c)}
    labels=[(x,mu,nu) for x in product(range(-2,3),repeat=3) for mu,nu in combinations(range(3),2)]
    faces=[face(*label) for label in labels]
    edges=sorted(set(target)|{e for f in faces for e in f}); idx={e:i for i,e in enumerate(edges)}
    triples=[(idx[e],j,n) for j,f in enumerate(faces) for e,n in f.items()]
    matrix=coo_matrix(([n for i,j,n in triples],([i for i,j,n in triples],[j for i,j,n in triples])),shape=(len(edges),len(faces))).tocsr()
    result=linprog(np.ones(2*len(faces)),A_eq=hstack([matrix,-matrix]),b_eq=np.array([float(target.get(e,0)) for e in edges]),bounds=(0,None),method='highs')
    assert result.success, result.message
    proposed=result.x[:len(faces)]-result.x[len(faces):]
    rational=[Fraction(float(a)).limit_denominator(10000) for a in proposed]
    recomposed=defaultdict(Fraction)
    for a,f in zip(rational,faces):
        for e,n in f.items():recomposed[e]+=a*n
    residual={e:recomposed.get(e,0)-target.get(e,0) for e in edges}
    assert all(n==0 for n in residual.values())
    area=sum(abs(a) for a in rational); assert area<lam
    return {'scope':__doc__,'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'lambda':lam,'residual_filling_l1':str(area),'vacuum_covariance_lower_multiple_vp':str(lam-area),
        'vacuum_covariance_upper_multiple_vp':str(lam+area),
        'all_edge_equalities_exact':True,'edges_checked':len(edges),'optimizer_optimality_required':False,
        'filling':[{'origin':x,'mu':mu,'nu':nu,'coefficient':str(a)} for (x,mu,nu),a in zip(labels,rational) if a],
        'claim':'t=lambda c_p + sum b_q c_q; triangle/Cauchy imply (lambda-sum|b|)v_p <= Cov(c_p.x,t.x) <= (lambda+sum|b|)v_p.',
        'not_claimed':'Independent reconstruction, full positive-time power, total all-channel flux, heat or absorbed photon energy.'}


if __name__=='__main__':
    tic=time.perf_counter(); data=run(); data['elapsed_seconds']=time.perf_counter()-tic
    print(json.dumps(data,indent=2))
