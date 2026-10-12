#!/usr/bin/env python3
"""Rank-one inverse-map identities and double-source-null witnesses.

Adds no measurement and fits no held-out amplitude. Charge/source assumptions
are identical to joint_scalar.py; variations are stresses, not probabilities.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import numpy as np

import joint_scalar as j


def full(q):
    return np.r_[1., q]


def sym(a, b):
    return (np.outer(a,b)+np.outer(b,a))/2


def null_direction(qearth, qsun):
    # x=1 is the normalization; all output may be multiplied by t.
    s=qsun-qearth
    e=-s[0]/s[1]
    return np.array([-qearth[0]-qearth[1]*e,1.,e])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-dir',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    runtime=args.source_dir.parent
    deadline=json.loads((runtime/'DEADLINE.json').read_text())
    assert datetime.now(timezone.utc).timestamp()<deadline['deadline_epoch']
    assert not any((runtime/s).exists() for s in ['STOP_REQUESTED','USER_STOP_REQUESTED'])
    manifest=j.checked_sources(args.source_dir)
    qe=.32*j.charge('Fe')+.68*j.compound({'Si':1,'O':2})
    qs=j.solar(args.source_dir/'bs05op.dat')[0]
    qt=j.mix({'Ti':.90,'Al':.06,'V':.04})
    qp=j.mix({'Pt':.90,'Rh':.10})
    v=null_direction(qe,qs)
    E,S,T,P=map(full,[qe,qs,qt,qp])
    b=np.r_[0.,j.charge('Be')-j.charge('Al')]
    H=np.array([0.,0.,1.])
    matrices={'microscope_numerator':sym(E,T-P),
              'microscope_denominator_minus_one':sym(E,(T+P)/2),
              'clock_numerator':6.95*sym(S,H),
              'solar_BeAl_numerator':sym(S,b),
              'solar_denominator_minus_one':sym(E,S)}
    witnesses=[]
    for t in [0.,.001,.01,.03,.1]:
        d=t*v
        o=j.observables(d,qe,qs,qt,qp)
        X=np.outer(d,d)
        lift={name:float(np.sum(matrix*X)) for name,matrix in matrices.items()}
        eta=lift['microscope_numerator']/(1+lift['microscope_denominator_minus_one'])
        ko=lift['clock_numerator']/(1+lift['solar_denominator_minus_one'])
        h=lift['solar_BeAl_numerator']/(1+lift['solar_denominator_minus_one'])
        assert abs(eta-o['microscope_eta'])<1e-22
        assert abs(ko-o['clock_k_E3_E2'])<1e-20
        assert abs(h-o['solar_BeAl_fraction'])<1e-22
        assert abs(E@d)<1e-19 and abs(S@d)<1e-19
        o.update({'t':t,'intrinsic_b_E3E2':-6.95*d[2],
                  'intrinsic_b_E3E2_squared':(-6.95*d[2])**2,
                  'alpha_pure_Fe_source':float(full(j.charge('Fe'))@d),
                  'Fe_source_TiAlV_PtRh_product':float((full(j.charge('Fe'))@d)*((T-P)@d)),
                  'X_rank_one':X.tolist(),'lifted_forward':lift})
        witnesses.append(o)

    stresses=[]
    for core in [.30,.32,.34]:
        for mantle_name,counts in [('SiO2',{'Si':1,'O':2}),('MgSiO3',{'Mg':1,'Si':1,'O':3})]:
            qev=core*j.charge('Fe')+(1-core)*j.compound(counts)
            for solar_file in ['bs05op.dat','bs05_agsop.dat']:
                for residual in ['Fe','O']:
                    qsv=j.solar(args.source_dir/solar_file,residual)[0]
                    vv=null_direction(qev,qsv)
                    fixed=j.observables(.1*v,qev,qsv,qt,qp)
                    retuned=j.observables(.1*vv,qev,qsv,qt,qp)
                    assert abs(retuned['microscope_eta'])<1e-21
                    assert abs(retuned['clock_k_E3_E2'])<1e-20
                    stresses.append({'core':core,'mantle':mantle_name,
                        'solar_file':solar_file,'solar_residual':residual,
                        'Earth_Q':qev.tolist(),'Sun_Q':qsv.tolist(),
                        'retuned_null_direction_x1':vv.tolist(),
                        'fixed_nominal_t_point_one_forward':fixed,
                        'retuned_point_one_forward':retuned})
    # A fixed nominal vector reacts linearly to source-response errors.
    # eta ≃ delta_alpha_E * delta_alpha_tests; k ≃ 6.95 e delta_alpha_S.
    d=.1*v
    dm=float((T-P)@d)
    source_tolerances={'fixed_nominal_t':.1,
        'alpha_E_error_for_one_MICROSCOPE_sigma':j.SIG_M/abs(dm),
        'alpha_S_error_for_one_optical_clock_sigma':j.SIG_O/abs(6.95*d[2]),
        'sensitivity_error_to_source_charge_error':'delta_alpha=d_x delta_Qme+d_e delta_Qem'}
    out={'status':'exact conditional degeneracy identity; no global viability claim',
         'created_at':datetime.now(timezone.utc).isoformat(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'joint_script_sha256':hashlib.sha256(Path(j.__file__).read_bytes()).hexdigest(),
         'source_null_direction_x1':v.tolist(),
         'source_row_rank':int(np.linalg.matrix_rank(np.vstack([E,S]))),
         'rank_one_matrices':{name:m.tolist() for name,m in matrices.items()},
         'coupling_box_t_interval':[-.1,.1],
         'witnesses':witnesses,'source_stresses_not_probability':stresses,
         'fixed_vector_error_tolerances':source_tolerances,
         'checks':['Lifted and direct rational maps agree for every witness.',
                   'Both source rows annihilate every nominal witness.',
                   'A retuned null vector exists for all 24 source stress variants.'],
         'interpretation':['The electron-only Earth-null branch remains constrained by the held-out Sun result.',
                           'This distinct double-source-null branch is not removed by those source-mediated summaries.',
                           'A single fixed numerical vector is not null under arbitrary source coefficient errors.',
                           'Intrinsic clock response is nonzero, but a noise prediction additionally requires a scalar-state covariance and sensor transfer function.',
                           'A third source with a linearly independent charge row or an independently calibrated scalar fluctuation probe can test this branch.']}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('Null direction x=1:',v)
    print('t=.1 intrinsic clock derivative:',witnesses[-1]['intrinsic_b_E3E2'])
    print('t=.1 Fe-source TiPt scalar acceleration product:',witnesses[-1]['Fe_source_TiAlV_PtRh_product'])
    print('Source error tolerance:',source_tolerances)
    print('24 source stresses: fixed MIC eta range', min(x['fixed_nominal_t_point_one_forward']['microscope_eta'] for x in stresses), max(x['fixed_nominal_t_point_one_forward']['microscope_eta'] for x in stresses))
    print('Three structural checks passed; independent review pending.')


if __name__=='__main__':
    main()
