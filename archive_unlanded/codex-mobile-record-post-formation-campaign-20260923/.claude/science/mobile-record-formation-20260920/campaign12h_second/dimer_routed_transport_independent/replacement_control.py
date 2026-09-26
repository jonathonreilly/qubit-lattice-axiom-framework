#!/usr/bin/env python3
"""Independent support/averaging controls for the variable-direction step."""
from pathlib import Path
from collections import Counter
import datetime, hashlib, importlib.util, itertools, json, sys
from fractions import Fraction
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('own_routing',HERE/'independent_check.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

def main():
    g=c.Matching(16,staggered=False);success=g.random_flips(70000,212021)
    d,q,inv=g.arrays();K=len(g.black);adj=[set() for _ in range(K)]
    for k in range(6):
        for u,v in enumerate(q[k]):
            if u!=v:adj[u].add(int(v));adj[v].add(u)
    block_rows=[]
    for u in [0,K//11,K//4,K-1]:
        _,ordinary,C=g.block(u,6)
        restricted={a:adj[a]&C for a in C}
        assert c.component_size(restricted,next(iter(C)))==len(C)
        for k in range(6):
            v=int(q[k,u])
            if v!=u:assert {int(inv[k,u]),u,v,int(q[k,v])}<=C
        variance=Fraction(len(C)-len(ordinary),len(C)*len(ordinary))
        block_rows.append({'center':u,'radius':6,'black_count':len(ordinary),'contracted_count':len(C),
                           'all_six_current_footprints_contained':True,'exact_block_average_difference_variance':str(variance)})

    # Exact boundary estimate on the infinite black sublattice for every allowed
    # displacement of L1 length <=2. No random matching distribution is used.
    shifts=[z for z in itertools.product(range(-2,3),repeat=3) if sum(abs(x) for x in z)<=2 and sum(z)%2==0]
    assert len(shifts)==19
    shift_rows=[]
    for l in [1,2,4,6,10]:
        block={z for z in itertools.product(range(-l,l+1),repeat=3) if sum(z)%2==0};m=len(block)
        boundary=max(len(block ^ {tuple(x+y for x,y in zip(z,shift)) for z in block}) for shift in shifts)
        variance=Fraction(boundary,m*m)
        shift_rows.append({'radius':l,'black_sites':m,'maximum_symmetric_difference':boundary,
                           'maximum_exact_iid_shift_difference_variance':str(variance),
                           'radius4_times_variance':float(l**4*variance)})

    # A deterministic period-eight matching family. Its unsmoothed zero-mean
    # coefficient has nonvanishing normalized iid variance at every volume.
    small=c.Matching(8,staggered=False);small.random_flips(16000,212018)
    ds,qs,_,=small.arrays();ks=len(small.black)
    r=ds[qs[0],0]-ds[qs[1],0]
    assert r.sum()==0 and int(r@r)>0
    smooth=[]
    for l in [0,1,2,4,6,10]:
        offsets=[z for z in itertools.product(range(-l,l+1),repeat=3) if sum(z)%2==0]
        residues=Counter(tuple(x%8 for x in z) for z in offsets);m=len(offsets)
        total=np.zeros(ks,dtype=np.int64)
        for shift,multiplicity in residues.items():
            permutation=[small.bindex[small.shift(site,shift)] for site in small.black]
            total+=multiplicity*r[permutation]
        variance=Fraction(int(total@total),ks*m*m)
        smooth.append({'radius':l,'exact_normalized_iid_sum_variance':str(variance),'value':float(variance)})
    assert smooth[0]['exact_normalized_iid_sum_variance']=='65/128'
    assert smooth[-1]['value']<smooth[0]['value']/100

    # Pointwise stationarity and parity tests on complete irregular routing cycles.
    rng=np.random.default_rng(212022);colors=rng.integers(14,size=K)
    s2=np.array([[[int(np.dot(delta,np.cross(ea,bb)+np.cross(eb,ba))) for eb,bb in zip(c.E,c.B)]
                  for ea,ba in zip(c.E,c.B)] for delta in c.DELTAS],dtype=int)
    telescope=[]
    for k in range(6):
        total=0
        for u,v in enumerate(q[k]):
            if u==v:continue
            l,a,b,r0=map(int,[colors[inv[k,u]],colors[u],colors[v],colors[q[k,v]]])
            h2=int(s2[k,l,a]+s2[k,a,r0]-s2[k,l,b]-s2[k,b,r0]);total+=h2
            assert h2==int(s2[k^1,r0,b]+s2[k^1,b,l]-s2[k^1,r0,a]-s2[k^1,a,l])
        assert total==0;telescope.append(total)
    result={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'large_footprint_graph':{'N':16,'successful_geometry_flips':success,'blocks':block_rows},
            'all_allowed_bounded_shift_controls':shift_rows,
            'period_eight_mean_zero_direction_countercontrol':smooth,
            'scope_of_periodic_variance':'Variance of a scalar coefficient applied to independent unit-variance pair colors, for periodic repetitions at N>2l+3; no stochastic geometry averaging or production simulation.',
            'pointwise_direction_drive_sums':telescope,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'independent_dependency_sha256':hashlib.sha256((HERE/'independent_check.py').read_bytes()).hexdigest()}
    (HERE/'REPLACEMENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(smooth,indent=2));print('Connected footprint, exact boundary variances, and telescoping controls passed.')

if __name__=='__main__':main()
