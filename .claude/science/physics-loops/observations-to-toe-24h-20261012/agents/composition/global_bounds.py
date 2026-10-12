#!/usr/bin/env python3
"""Analytic conservative projection of the entire frozen calibration region.

No optimization, samples, or held-out amplitude is used to establish the outer
bound. This improves the loose coupling-box bound without calling it sharp.
The derivation is in MODEL_AND_RESULTS.md; print every proof constant here.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib,json,math
from pathlib import Path
import numpy as np
import joint_scalar as j


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--results',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    data=json.loads(args.results.read_text())
    q=data['charges']
    qe,qs,qt,qp=[np.array(q[name]) for name in ['Earth','Sun','TiAlV','PtRh']]
    m,n=qt-qp
    sm,se=qs-qe
    bm,be=np.array(q['Be_minus_Al'])
    rho=.016  # Explicit split; no optimizer tuned to the bound or holdout.
    assert m>abs(n)*rho and sm>0
    ae_max=.001+.1*np.abs(qe).sum()
    as_max=.001+.1*np.abs(qs).sum()
    abar_max=.001+.1*np.abs((qt+qp)/2).sum()
    Dmin=1-ae_max*as_max
    pmax=abs(j.MU_M)+math.sqrt(j.CHI2_CUT)*j.SIG_M
    Pmax=pmax*(1+ae_max*abar_max)
    Zmax=(abs(j.MU_O)+math.sqrt(j.CHI2_CUT)*j.SIG_O)/6.95
    # |e|<=rho |x|: |alpha_E*x| <= Pmax/(m-|n|rho).
    c1=abs(bm)*(Pmax/(m-abs(n)*rho)+(abs(sm)+abs(se)*rho)*.1**2)/Dmin+abs(be)*Zmax
    # |e|>rho |x|: |alpha_S*x|/D <= Zmax/rho.
    c2=Zmax*(abs(bm)/rho+abs(be))
    bound=max(c1,c2)
    negative=data['earth_neutral_electron_branch']['solar_BeAl_fraction_interval'][0]
    positive=max(row['solar_BeAl_fraction'] for row in data['central_fiber_samples'])
    # A central-fit ray lambda*d, lambda in [0,1], stays in the region:
    # each prediction monotonically runs from zero to its measured mean,
    # so each squared standardized residual is bounded by its null value.
    witnesses=data['earth_neutral_electron_branch']['witnesses']+data['central_fiber_samples']
    assert all(abs(row['solar_BeAl_fraction'])<=bound for row in witnesses)
    out={'status':'guaranteed analytic outer bound, not globally sharp',
         'created_at':datetime.now(timezone.utc).isoformat(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_results_sha256':hashlib.sha256(args.results.read_bytes()).hexdigest(),
         'constants':{'rho':rho,'m':m,'n':n,'sm':sm,'se':se,'bm':bm,'be':be,
                      'max_abs_alpha_E':ae_max,'max_abs_alpha_S':as_max,
                      'max_abs_alpha_mean_tests':abar_max,'D_lower_bound':Dmin,
                      'MICROSCOPE_abs_eta_upper':pmax,
                      'MICROSCOPE_product_abs_upper':Pmax,
                      'clock_abs_e_alphaS_over_D_upper':Zmax,
                      'case_small_e_bound':c1,'case_large_e_bound':c2},
         'entire_calibration_region_outer_BeAl_fraction':[-bound,bound],
         'entire_calibration_region_outer_BeAl_acceleration_fm_s2':[-j.G_SUN*1e15*bound,j.G_SUN*1e15*bound],
         'guaranteed_attainable_BeAl_fraction_interval':[negative,positive],
         'guaranteed_attainable_BeAl_acceleration_fm_s2_interval':[j.G_SUN*1e15*negative,j.G_SUN*1e15*positive],
         'qualification':'Nominal fixed sensitivities and frozen coupling box only. Measurement ellipse is conservatively enlarged to marginal absolute bounds during this proof; no sharp projection claim.'}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
