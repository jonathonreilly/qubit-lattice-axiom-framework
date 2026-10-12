#!/usr/bin/env python3
"""Prospective finite quantum witness with an exact integer norm bound."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.special import roots_legendre

RT=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=RT/'quantum/direct_visibility'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def conditioned(c,k):
    u=2/np.pi*np.arcsin(np.clip(c,-1,1))
    t=np.tanh(k*c)
    return (u+t)/(1+u*t)


def main():
    freeze=json.loads((OUT/'FREEZE.json').read_text())
    assert digest(Path(__file__).with_name('DIRECT_VISIBILITY_CRITERION.md'))==freeze['note_sha256']
    output=OUT/'RESULTS_v1.json'
    assert not output.exists()
    source=digest(__file__)
    started=time.time()
    k=math.sqrt(2)*(math.atanh(1/math.sqrt(2))-math.atanh(.5))
    rows=[]
    for order in freeze['polar_orders']:
        assert time.time()<json.loads((RT/'DEADLINE.json').read_text())['packaging_epoch']
        assert not any((RT/name).exists() for name in ['STOP_REQUESTED.json','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'])
        c,w=roots_legendre(order)
        azimuth=2*np.pi*(np.arange(2*order+1)+.5)/(2*order+1)
        points=np.array([[math.sqrt(1-z*z)*math.cos(p),math.sqrt(1-z*z)*math.sin(p),z]
                         for z in c for p in azimuth])
        raw=np.repeat(w/(2*(2*order+1)),2*order+1)
        # Exact positive rational probabilities; their sum is exactly one by
        # definition, independently of floating evaluation of the quadrature.
        integers=np.maximum(1,np.rint(raw*10**12).astype(np.int64))
        denominator=int(sum(int(x) for x in integers))
        probability=integers/denominator
        cosine=np.clip(points@points.T,-1,1)
        np.fill_diagonal(cosine,1.)
        g=conditioned(cosine,k)
        root=np.sqrt(probability)
        m=root[:,None]*g*root[None,:]
        eigen,vec=np.linalg.eigh(m)
        sign=np.sign(eigen)
        sign[np.abs(eigen)<1e-13]=0
        candidate_sign=(vec*sign)@vec.T
        scale=10**10
        integer_matrix=np.rint(candidate_sign*scale).astype(np.int64)
        # Python-integer products, not overflowing int64 or float arithmetic.
        obj=integer_matrix.astype(object)
        gram=obj.T@obj
        max_row=max(sum(abs(int(x)) for x in row) for row in gram)
        radius=math.isqrt(max_row)
        if radius*radius<max_row:
            radius+=1
        assert max_row<=radius*radius
        certified_sign=integer_matrix/radius
        witness=root[:,None]*certified_sign*root[None,:]
        prediction=float(np.sum(witness*g))
        cosine_control=float(np.sum(witness*cosine))
        assert abs(cosine_control)<=1+2e-12
        npz=OUT/f'grid_{order}_v1.npz'
        assert not npz.exists()
        np.savez_compressed(npz,directions=points,probability_numerators=integers,
             probability_denominator=np.array(denominator),candidate_G=g,
             integer_sign_matrix=integer_matrix,sign_denominator=np.array(radius),
             witness_coefficients=witness)
        row={'polar_order':order,'settings_per_party':len(points),'k_prospective':k,
             'probability_denominator':denominator,'integer_sign_denominator':radius,
             'exact_gram_row_sum_max':str(max_row),'exact_norm_squared_upper_numerator':str(max_row),
             'exact_norm_squared_upper_denominator':str(radius*radius),
             'exact_integer_norm_bound_pass':True,'candidate_weighted_trace_norm':float(np.abs(eigen).sum()),
             'certified_witness_candidate_value_at_V1':prediction,'cosine_control':cosine_control,
             'witness_candidate_visibility_threshold':1/prediction,
             'candidate_values':[{'visibility':v,'B':v*prediction,'above_quantum_bound':v*prediction-1} for v in freeze['visibilities']],
             'artifact_sha256':digest(npz),'smallest_weighted_eigenvalue':float(eigen.min())}
        rows.append(row)
        print(json.dumps(row),flush=True)
    assert digest(__file__)==source
    result={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':source,
            'freeze_sha256':digest(OUT/'FREEZE.json'),'rows':rows,'final_declared_grid':12,
            'elapsed_seconds':time.time()-started,
            'limits':'Exact integer algebra bounds the norm of the defined sign matrix, so the corresponding linear quantum bound is rigorous for exact stated probability weights. Candidate kernel/witness expectation is floating numerical evidence, not an interval certificate. Prospective mathematics, no observed experiment, no full-sphere tail or membership claim from finite grids.'}
    output.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
