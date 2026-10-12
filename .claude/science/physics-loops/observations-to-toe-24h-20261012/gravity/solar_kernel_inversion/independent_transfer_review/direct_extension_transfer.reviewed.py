#!/usr/bin/env python3
"""Two frozen responses, six sources, separated fields and target readout."""
import argparse
import datetime as dt
import gc
import json
from pathlib import Path

import numpy as np

import direct_galaxy_response_operator as op
import direct_validate_inverse_fields as validator

NAMES=['NGC3949','NGC3972','UGC06667','UGC08837','DDO064','DDO168']
HERE=Path(__file__).resolve().parent
OUT=op.OUT/'extension_transfer'
LABEL='D_galaxies_external_solar'


def read(path):
    return json.loads(Path(path).read_text())


def identities():
    files={'source':Path(__file__),'protocol':HERE/'FROZEN_EXTENSION_TRANSFER.md',
           'operator':Path(op.__file__),'validator':Path(validator.__file__),
           'fits':op.OUT/'shared_response_fits_v1.json',
           'margin':op.OUT/'margin_candidate_v1.json',
           'source_data':op.field.DATA/'baryonic_forward_64.npz',
           'target_data':op.field.DATA/'sealed_targets.npz',
           'original_selection':op.field.DATA/'qumond_disk/contract_and_subset_freeze.json',
           'margin_protocol':HERE/'FOLLOWUP_MARGIN_PROTOCOL.md'}
    for name in NAMES:
        files['source_receipt_'+name]=op.source_receipt(name)
    return {key:op.field.sha(path) for key,path in files.items()}


def candidates():
    fits=read(op.OUT/'shared_response_fits_v1.json')
    margin=read(op.OUT/'margin_candidate_v1.json')
    original=next(row['best_sampled'] for row in fits['cases']
                  if row['family']+'_'+row['constraints']==LABEL)
    assert original['status']==0 and margin['status']==0
    assert margin['parent_fits_sha256']==op.field.sha(op.OUT/'shared_response_fits_v1.json')
    return {'original_D_joint':np.array(original['weights']),
            'interior_D_joint':np.array(margin['weights'])}


def save(path,data):
    assert not path.exists()
    path.write_text(json.dumps(data,indent=2)+'\n')


def force_rows(weights,data):
    projector=op.LinearProjection(data)
    result={key:projector.combined(value) for key,value in weights.items()}
    return result,projector


def field_stage(stage,freeze):
    original=read(op.OUT/'field_validation_v1.json')
    margin=read(op.OUT/'margin_field_validation_v1.json')
    assert original['fits_sha256']==freeze['identities']['fits']
    assert original['candidate_passes'][LABEL] and margin['passed']
    assert margin['candidate_sha256']==freeze['identities']['margin']
    weights=candidates()
    for value in weights.values():
        assert value.shape==(20,) and np.all(np.isfinite(value)&(value>=0))
    weight_bytes={key:value.tobytes() for key,value in weights.items()}
    for name in NAMES:
        op.guard()
        destination=OUT/f'{stage}_{name}_v1.json'
        if destination.exists():
            prior=read(destination)
            assert prior['freeze_sha256']==op.field.sha(OUT/'FREEZE.json')
            assert prior['identities']==freeze['identities']
            continue
        print(f'{stage}: {name}',flush=True)
        base,receipt,_=op.galaxy_geometry(name)
        if stage=='base':
            forces,projector=force_rows(weights,base)
            newton=projector.project(1.,1.)
            known=projector.project(op.field.nu(projector.norm_SI/op.field.A0_SI),
                    op.field.nu(projector.mid_norm_SI/op.field.A0_SI))
            control={'newtonian':float(np.max(np.abs(newton/base['mr']-1))),
                     'prior_response':float(np.max(np.abs(known/receipt['projection']['full']-1)))}
            assert control['newtonian']<=.003 and control['prior_response']<=1e-10
            data={'R_kpc':base['R'].tolist(),'forces':{key:value.tolist() for key,value in forces.items()},
                  'controls':control,'geometry_sha256':op.field.sha(op.OUT/f'newtonian_field_{name}_base.npz'),
                  'target_arrays_read':False,'provisional':True}
            del projector
        else:
            prior=read(OUT/f'base_{name}_v1.json')
            assert prior['identities']==freeze['identities']
            assert prior['geometry_sha256']==op.field.sha(op.OUT/f'newtonian_field_{name}_base.npz')
            assert np.array_equal(prior['R_kpc'],base['R'])
            refined,_,_=op.galaxy_geometry(name,tag='refined',refine=True)
            fine,pfine=force_rows(weights,refined)
            del pfine,refined
            boundary=validator.boundary_extension(name,base,receipt)
            edge,pedge=force_rows(weights,boundary)
            del pedge,boundary
            data={'R_kpc':base['R'].tolist(),'candidates':{},'target_arrays_read':False,
                  'base_receipt_sha256':op.field.sha(OUT/f'base_{name}_v1.json'),
                  'refined_geometry_sha256':op.field.sha(op.OUT/f'newtonian_field_{name}_refined.npz'),
                  'boundary_geometry_sha256':op.field.sha(op.OUT/f'newtonian_field_{name}_boundary_extension.npz')}
            for key in weights:
                coarse=np.array(prior['forces'][key])
                positive=all(np.all(np.isfinite(v)&(v>0)) for v in [coarse,fine[key],edge[key]])
                changes=None if not positive else {'refinement':float(np.max(np.abs(fine[key]/coarse-1))),
                                                   'boundary':float(np.max(np.abs(edge[key]/coarse-1)))}
                passed=bool(positive and changes['refinement']<=.005 and changes['boundary']<=.003)
                data['candidates'][key]={'passed':passed,'relative_changes':changes,
                    'forces':{'base':coarse.tolist(),'refined':fine[key].tolist(),'boundary':edge[key].tolist()}}
                print(json.dumps({'name':name,'candidate':key,'passed':passed,'changes':changes}),flush=True)
        assert weight_bytes=={key:value.tobytes() for key,value in weights.items()}
        assert freeze['identities']==identities()
        save(destination,{'at':dt.datetime.now(dt.timezone.utc).isoformat(),'name':name,
                         'freeze_sha256':op.field.sha(OUT/'FREEZE.json'),
                         'identities':freeze['identities'],**data})
        del base
        gc.collect()


def score(freeze):
    receipts={name:read(OUT/f'validate_{name}_v1.json') for name in NAMES}
    for value in receipts.values():
        assert value['identities']==freeze['identities']
        assert value['freeze_sha256']==op.field.sha(OUT/'FREEZE.json')
    rows=[]
    with np.load(op.field.DATA/'baryonic_forward_64.npz') as source,np.load(op.field.DATA/'sealed_targets.npz') as targets:
        for name in NAMES:
            row=receipts[name]
            mask=source[name+'_score_mask']
            radius=source[name+'_R'][mask]
            assert np.array_equal(radius,row['R_kpc'])
            velocity,error=targets[name+'_v'][mask],targets[name+'_error'][mask]
            assert np.all(np.isfinite(velocity)&(velocity>0)&(radius>0))
            assert np.all(np.isfinite(error)&(error>=0))
            acceleration=velocity**2/radius
            lower=np.maximum(0,velocity-2*error)**2/radius
            upper=(velocity+2*error)**2/radius
            entries={}
            for label,candidate in row['candidates'].items():
                entries[label]={'numerical_pass':candidate['passed'],'methods':{}}
                for kind,values in candidate['forces'].items():
                    force=np.array(values)
                    finite=bool(np.all(np.isfinite(force)))
                    positive=finite and bool(np.all(force>0))
                    needed=None if not finite else np.maximum.reduce([np.zeros_like(force),
                        (force-upper)/acceleration,(lower-force)/acceleration])
                    residual=.5*np.log10(force/acceleration) if positive else None
                    entries[label]['methods'][kind]={'required_rectangle_t':None if needed is None else float(needed.max()),
                        'rms_log10_velocity':None if residual is None else float(np.sqrt(np.mean(residual**2))),
                        'predicted_velocity':None if not positive else np.sqrt(radius*force).tolist(),
                        'required_t_by_row':None if needed is None else needed.tolist()}
            rows.append({'name':name,'data_role':'previously exposed, outside response fits',
                'R_kpc':radius.tolist(),'observed_velocity':velocity.tolist(),'processed_error':error.tolist(),'candidates':entries})
    combined={}
    for label in candidates():
        combined[label]={'numerical_pass':all(row['candidates'][label]['numerical_pass'] for row in rows),'methods':{}}
        for kind in ['base','refined','boundary']:
            vals=[row['candidates'][label]['methods'][kind] for row in rows]
            combined[label]['methods'][kind]={
                'equal_galaxy_rms_log10_velocity':None if any(v['rms_log10_velocity'] is None for v in vals) else float(np.sqrt(np.mean([v['rms_log10_velocity']**2 for v in vals]))),
                'largest_rectangle_t':None if any(v['required_rectangle_t'] is None for v in vals) else max(v['required_rectangle_t'] for v in vals)}
    assert freeze['identities']==identities()
    result={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'identities':freeze['identities'],
        'freeze_sha256':op.field.sha(OUT/'FREEZE.json'),'combined':combined,'rows':rows,
        'limits':'Two unchanged fitted responses; six exposed out-of-fit development objects. Numerical gate failure qualifies corresponding scores. No full-family rejection, nuisance likelihood, pressure correction or covariant completion.'}
    save(OUT/'RESULTS_v1.json',result)
    print(json.dumps(combined,indent=2))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--stage',choices=['freeze','base','validate','score'],required=True)
    args=parser.parse_args()
    op.guard()
    OUT.mkdir(exist_ok=True)
    path=OUT/'FREEZE.json'
    if args.stage=='freeze':
        selection=read(op.field.DATA/'qumond_disk/contract_and_subset_freeze.json')
        assert selection['conditional_expansion']==NAMES
        save(path,{'at':dt.datetime.now(dt.timezone.utc).isoformat(),'names':NAMES,
                   'identities':identities(),'candidates':{k:v.tolist() for k,v in candidates().items()},
                   'scoring_follows_complete_validation':True})
        print(path)
        return
    freeze=read(path)
    assert freeze['identities']==identities() and freeze['names']==NAMES
    assert all(np.array_equal(value,freeze['candidates'][key]) for key,value in candidates().items())
    if args.stage in ['base','validate']:
        field_stage(args.stage,freeze)
    else:
        score(freeze)

if __name__=='__main__':
    main()
