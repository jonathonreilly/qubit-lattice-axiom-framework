#!/usr/bin/env python3
"""Validate the separately frozen interior candidate on existing field grids."""
import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np

import direct_shared_response_fit as fit
import direct_validate_inverse_fields as validator


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    fit.operator.guard()
    assert not args.output.exists()
    source=fit.operator.field.sha(__file__)
    candidate=json.loads(args.candidate.read_text())
    freeze=json.loads((fit.operator.OUT/'FOLLOWUP_MARGIN_FREEZE.json').read_text())
    assert candidate['status']==0 and candidate['protocol_sha256']==freeze['protocol_sha256']
    assert candidate['source_sha256']==fit.operator.field.sha(Path(__file__).with_name('direct_margin_candidate.py'))
    assert candidate['parent_fits_sha256']==freeze['parent_fits_sha256']
    assert fit.operator.field.sha(fit.operator.OUT/'shared_response_fits_v1.json')==freeze['parent_fits_sha256']
    assert candidate['external_newtonian_SI']==freeze['fixed_external_newtonian_SI']
    weights=np.array(candidate['weights'])
    assert weights.shape==(20,) and np.all(np.isfinite(weights)&(weights>=0)) and weights.sum()<=100
    d_slacks=np.array([1+weights[j+1:].sum()-weights[j]/np.log(fit.operator.KNOTS[j+1]/fit.operator.KNOTS[j]) for j in range(20)])
    assert d_slacks.min()>=-1e-9
    original_weight_bytes=weights.tobytes()
    rows=[]
    for data in fit.training_rows():
        name=data['name']
        assert data['operator_receipt_sha256']==candidate['operator_receipts'][name]
        # Do not launch a duplicate source solve while the original validator
        # is filling these caches. This follow-up requires completed receipts.
        for tag in ['base','refined','boundary_extension']:
            assert (fit.operator.OUT/f'newtonian_field_{name}_{tag}.npz').exists()
            assert (fit.operator.OUT/f'newtonian_field_{name}_{tag}.json').exists()
        base_data,receipt,_=fit.operator.galaxy_geometry(name)
        refined_data,_,_=fit.operator.galaxy_geometry(name,tag='refined',refine=True)
        boundary_data=validator.boundary_extension(name,base_data,receipt)
        direct=fit.operator.LinearProjection(base_data).combined(weights)
        refined=fit.operator.LinearProjection(refined_data).combined(weights)
        boundary=fit.operator.LinearProjection(boundary_data).combined(weights)
        matrix=data['g_N']+data['K']@weights
        assert weights.tobytes()==original_weight_bytes
        forces={'matrix':matrix,'base':direct,'refined':refined,'boundary':boundary}
        positive=all(np.all(np.isfinite(v)&(v>0)) for v in forces.values())
        differences=None if not positive else {
            'direct_vs_matrix':float(np.max(np.abs(direct/matrix-1))),
            'radial_angular_refinement':float(np.max(np.abs(refined/direct-1))),
            'boundary_extension':float(np.max(np.abs(boundary/direct-1)))}
        numerical_pass=bool(positive and differences['direct_vs_matrix']<=.003
                            and differences['radial_angular_refinement']<=.005
                            and differences['boundary_extension']<=.003)
        margins={kind:float(np.min(np.r_[(force-data['low'])/data['A'],
                    (data['high']-force)/data['A']])) for kind,force in forces.items()}
        scores={kind:None if not np.all(force>0) else
                float(np.sqrt(np.mean((.5*np.log10(force/data['A']))**2))) for kind,force in forces.items()}
        rows.append({'name':name,'R_kpc':data['R'].tolist(),'numerical_pass':numerical_pass,
                     'relative_changes':differences,'rectangle_margins':margins,
                     'rms_log10_velocity':scores,'forces':{k:v.tolist() for k,v in forces.items()},
                     'geometry_hashes':{tag:fit.operator.field.sha(fit.operator.OUT/f'newtonian_field_{name}_{tag}.npz')
                        for tag in ['base','refined','boundary_extension']}})
    external=candidate['external_newtonian_SI']
    _,_,q=fit.constraints(fit.training_rows(),differential=True,external=external,solar_limit=True)
    q2=float(q@weights)
    ge=external*(1+sum(w*float(fit.operator.ramp(external,lo,hi))
            for w,lo,hi in zip(weights,fit.operator.KNOTS[:-1],fit.operator.KNOTS[1:])))
    external_pass=bool(fit.EXTERNAL[0]<=ge<=fit.EXTERNAL[1])
    solar_pass=bool(0<=q2<=fit.QMAX)
    direct_rectangles=all(min(row['rectangle_margins'][kind] for kind in ['base','refined','boundary'])>=0 for row in rows)
    numerical_pass=all(row['numerical_pass'] for row in rows)
    result={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':source,
            'candidate_sha256':fit.operator.field.sha(args.candidate),'rows':rows,
            'numerical_pass':numerical_pass,'direct_original_galaxy_rectangles_pass':direct_rectangles,
            'external_rectangle_pass':external_pass,'solar_rectangle_pass':solar_pass,
            'predicted_external_physical_SI':ge,'Q2_s_minus2':q2,
            'minimum_D_slack':float(d_slacks.min()),
            'passed':numerical_pass and direct_rectangles and external_pass and solar_pass,
            'limits':'Unchanged follow-up weights and observations. Conditional numerical compatibility with actual direct fields, not exact interval certification or a joint confidence statement. The same measurements were used to choose the candidate. Out-of-fit source tests and healthy dynamical completion remain open.'}
    assert fit.operator.field.sha(__file__)==source
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
    for row in rows:
        print(json.dumps({k:v for k,v in row.items() if k not in ['forces','R_kpc','geometry_hashes']},indent=2))


if __name__=='__main__':
    main()
