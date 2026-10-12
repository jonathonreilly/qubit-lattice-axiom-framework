#!/usr/bin/env python3
"""Exposed nine-source reconstruction at a declared fixed external field."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import traceback
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import direct_galaxy_response_operator as op
import direct_shared_response_fit as fit
import direct_validate_inverse_fields as validator

OLD=['NGC2976','UGC07577','KK98-251']
EXTRA=['NGC3949','NGC3972','UGC06667','UGC08837','DDO064','DDO168']
NAMES=OLD+EXTRA
E=1.4915242022774435e-10
OUT=op.OUT/'nine_source'
TRANSFER=op.OUT/'extension_transfer'
STATUS=OUT/'COMPUTE_STATUS.json'

def read(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def save(p,data):
    assert not p.exists(), f'Refusing to overwrite {p}'
    p.write_text(json.dumps(data,indent=2)+'\n')
def status(phase,**data):
    tmp=STATUS.with_suffix('.tmp')
    tmp.write_text(json.dumps({'phase':phase,'at':now(),'pid':os.getpid(),
       'kind':'fixed_numerical_calculation','author_mode':'direct_chat_author',
       'deadline':read(op.RUNTIME/'DEADLINE.json')['deadline_at'],**data},indent=2)+'\n')
    tmp.replace(STATUS)

def identities():
    files={'source':Path(__file__),'protocol':HERE/'PROTOCOL.md',
      'operator':Path(op.__file__),'LP_component':Path(fit.__file__),
      'validator':Path(validator.__file__),'solar_component':Path(fit.solar.__file__),
      'failed_transfer':TRANSFER/'RESULTS_v1.json',
      'transfer_freeze':TRANSFER/'FREEZE.json',
      'source_data':op.field.DATA/'baryonic_forward_64.npz',
      'target_data':op.field.DATA/'sealed_targets.npz',
      'old_protocol':HERE.parent/'FROZEN_DIRECT_INVERSE_PROTOCOL.md',
      'controls':op.OUT/'operator_controls_v1.json'}
    for name in NAMES:
        files['source_receipt_'+name]=op.source_receipt(name)
        files['base_geometry_'+name]=op.OUT/f'newtonian_field_{name}_base.npz'
    for name in OLD:
        files['old_operator_'+name]=op.OUT/f'operator_{name}_v1.json'
    return {key:sha(value) for key,value in files.items()}

def operators(freeze):
    paths={}
    for name in NAMES:
        op.guard()
        if name in OLD:
            path=op.OUT/f'operator_{name}_v1.json'
        else:
            path=OUT/f'operator_{name}_v1.json'
            if not path.exists():
                status('operators',name=name)
                print('operator:',name,flush=True)
                data=op.build_operator(name)
                data.update(at=now(),source_sha256=sha(op.__file__),
                  solver_sha256=op.SOLVER_HASH,protocol_sha256=op.PROTOCOL_HASH,
                  new_protocol_sha256=freeze['identities']['protocol'],
                  freeze_sha256=sha(OUT/'FREEZE.json'),
                  observed_velocities_read=False)
                save(path,data)
        data=read(path)
        assert data['source_sha256']==freeze['identities']['operator']
        assert data['solver_sha256']==op.SOLVER_HASH
        assert data['protocol_sha256']==op.PROTOCOL_HASH
        assert data['identity']['source_receipt_sha256']==sha(op.source_receipt(name))
        if name in EXTRA:
            assert data['freeze_sha256']==sha(OUT/'FREEZE.json')
        paths[name]=path
    return paths

def training_rows(paths):
    rows=[]
    with np.load(op.field.DATA/'baryonic_forward_64.npz') as raw, \
         np.load(op.field.DATA/'sealed_targets.npz') as target:
        for name in NAMES:
            receipt=read(paths[name])
            mask=raw[name+'_score_mask']
            radius=raw[name+'_R'][mask]
            v,e=target[name+'_v'][mask],target[name+'_error'][mask]
            assert np.array_equal(radius,receipt['R_kpc'])
            assert np.array_equal(op.KNOTS,receipt['knots_SI'])
            assert np.all(np.isfinite(v)&(v>0)&(radius>0))
            assert np.all(np.isfinite(e)&(e>=0))
            rows.append({'name':name,'R':radius,'A':v*v/radius,
              'low':np.maximum(0,v-2*e)**2/radius,'high':(v+2*e)**2/radius,
              'g_N':np.array(receipt['g_N']),'K':np.array(receipt['K']),
              'operator_receipt_sha256':sha(paths[name])})
    return rows

def solve(rows,freeze,paths):
    path=OUT/'CANDIDATES_v1.json'
    if path.exists():
        out=read(path)
        assert out['freeze_sha256']==sha(OUT/'FREEZE.json')
        assert out['operators']=={name:sha(p) for name,p in paths.items()}
        return out
    status('fit')
    cases=[]
    for differential in [False,True]:
        family='D' if differential else 'M'
        for label,external,solar_limit in [
          ('galaxies_only',None,False),('galaxies_external',E,False),
          ('galaxies_external_solar',E,True)]:
            op.guard()
            result=fit.solve(rows,differential,external,solar_limit)
            if result['status']==0:
                w=np.array(result['weights'])
                result['min_D_upper_limit']=float(min(
                  1+sum(w[j+1:])-w[j]/np.log(op.KNOTS[j+1]/op.KNOTS[j])
                  for j in range(20)))
            cases.append({'name':family+'_'+label,'family':family,
                          'constraints':label,'solution':result})
            print(json.dumps({'name':cases[-1]['name'],'status':result['status'],
                  'primary_t':result.get('primary_minimum_t'),
                  'weight_sum':result.get('total_weight'),
                  'min_D':result.get('min_D_upper_limit')}),flush=True)
    assert identities()==freeze['identities']
    out={'at':now(),'freeze_sha256':sha(OUT/'FREEZE.json'),
      'operators':{name:sha(p) for name,p in paths.items()},'cases':cases,
      'candidate_field_validation_required':True,'all_observations_are_fit_inputs':True,
      'continuous_external_optimality_claimed':False,
      'limits':'Finite-grid numerical LP; no continuum family exclusion; E held fixed where imposed.'}
    save(path,out)
    return out

def validate_and_readout(rows,candidates,freeze):
    target={r['name']:r for r in rows}
    successes={c['name']:np.array(c['solution']['weights'])
               for c in candidates['cases'] if c['solution']['status']==0}
    exact={name:w.tobytes() for name,w in successes.items()}
    all_rows=[]
    for name in NAMES:
        op.guard()
        path=OUT/f'fields_{name}_v1.json'
        if path.exists():
            rec=read(path)
            assert rec['freeze_sha256']==sha(OUT/'FREEZE.json')
            assert rec['candidates_sha256']==sha(OUT/'CANDIDATES_v1.json')
            all_rows.append(rec)
            continue
        status('direct_fields',name=name)
        print('direct field checks:',name,flush=True)
        base,previous,_=op.galaxy_geometry(name)
        fine,_,_=op.galaxy_geometry(name,tag='refined',refine=True)
        edge=validator.boundary_extension(name,base,previous)
        forces={}
        for method,geometry in [('base',base),('refined',fine),('boundary',edge)]:
            projection=op.LinearProjection(geometry)
            forces[method]={key:projection.combined(w) for key,w in successes.items()}
            del projection
        rec={'name':name,'at':now(),'freeze_sha256':sha(OUT/'FREEZE.json'),
             'candidates_sha256':sha(OUT/'CANDIDATES_v1.json'),
             'R_kpc':base['R'].tolist(),'candidates':{}}
        source=target[name]
        for key in successes:
            vectors={method:values[key] for method,values in forces.items()}
            positive=all(np.all(np.isfinite(v)&(v>0)) for v in vectors.values())
            changes=None if not positive else {
              'refinement':float(np.max(np.abs(vectors['refined']/vectors['base']-1))),
              'boundary':float(np.max(np.abs(vectors['boundary']/vectors['base']-1)))}
            passed=bool(positive and changes['refinement']<=.005 and changes['boundary']<=.003)
            item={'passed':passed,'relative_changes':changes,'methods':{}}
            for method,g in vectors.items():
                ok=bool(np.all(np.isfinite(g)&(g>0)))
                needed=np.maximum.reduce([np.zeros_like(g),
                  (g-source['high'])/source['A'],(source['low']-g)/source['A']])
                residual=None if not ok else .5*np.log10(g/source['A'])
                item['methods'][method]={'force':g.tolist(),
                  'required_rectangle_t':float(np.max(needed)),
                  'rms_log10_velocity':None if residual is None else float(np.sqrt(np.mean(residual**2))),
                  'velocity':None if not ok else np.sqrt(source['R']*g).tolist(),
                  'bins_outside_rectangle':int(np.count_nonzero(needed>0))}
            rec['candidates'][key]=item
        assert exact=={name:w.tobytes() for name,w in successes.items()}
        assert identities()==freeze['identities']
        save(path,rec);all_rows.append(rec)
        del base,fine,edge,forces
    combined={}
    for key in successes:
        items=[r['candidates'][key] for r in all_rows]
        combined[key]={'all_field_gates_pass':all(i['passed'] for i in items),'methods':{}}
        for method in ['base','refined','boundary']:
            ms=[i['methods'][method] for i in items]
            combined[key]['methods'][method]={
              'largest_rectangle_t':max(m['required_rectangle_t'] for m in ms),
              'equal_galaxy_rms_log10_velocity':None if any(m['rms_log10_velocity'] is None for m in ms)
                 else float(np.sqrt(np.mean([m['rms_log10_velocity']**2 for m in ms]))),
              'bins_outside_rectangle':sum(m['bins_outside_rectangle'] for m in ms)}
    result={'at':now(),'freeze_sha256':sha(OUT/'FREEZE.json'),
      'candidates_sha256':sha(OUT/'CANDIDATES_v1.json'),'combined':combined,
      'field_receipts':{r['name']:sha(OUT/f"fields_{r['name']}_v1.json") for r in all_rows},
      'role':'All nine sources are exposed fit inputs, no independent validation',
      'limits':'Actual field checks qualify these numerical candidates only. Solar/external entries remain LP-kernel calibration values pending any separately required direct check.'}
    save(OUT/'RESULTS_v1.json',result)
    print(json.dumps(combined,indent=2),flush=True)

def main():
    OUT.mkdir(exist_ok=True)
    op.guard()
    path=OUT/'FREEZE.json'
    identity=identities()
    controls=read(op.OUT/'operator_controls_v1.json')
    assert controls['passed'] and controls['source_sha256']==identity['operator']
    old=read(TRANSFER/'RESULTS_v1.json')
    assert all(c['numerical_pass'] for c in old['combined'].values())
    if not path.exists():
        save(path,{'at':now(),'identities':identity,'names':NAMES,'fixed_E':E,
          'main_searched':subprocess.check_output(['git','rev-parse','origin/main'],text=True).strip(),
          'main_statement_search':'QUMOND or nine-source response/reconstruction, docs/*.md excluding audit/raw/work-history: no match, exit1. Not an exhaustive novelty claim.',
          'previous_failed_transfer_preserved_commit':'94f791c83d',
          'all_nine_are_calibration_data':True})
    freeze=read(path)
    assert freeze['identities']==identity and freeze['names']==NAMES and freeze['fixed_E']==E
    paths=operators(freeze)
    rows=training_rows(paths)
    candidates=solve(rows,freeze,paths)
    validate_and_readout(rows,candidates,freeze)
    status('complete',result_sha256=sha(OUT/'RESULTS_v1.json'))
    print('COMPLETE fixed nine-source diagnostic; no prior result overwritten.',flush=True)

if __name__=='__main__':
    try:
        main()
    except BaseException as error:
        if OUT.exists():
            status('failed',error=repr(error))
        traceback.print_exc()
        raise
