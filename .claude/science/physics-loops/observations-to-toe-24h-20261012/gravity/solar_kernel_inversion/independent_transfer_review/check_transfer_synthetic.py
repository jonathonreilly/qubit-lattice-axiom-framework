#!/usr/bin/env python3
"""Synthetic stages/resume/readout for the pinned transfer; no real fields."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import sys
sys.dont_write_bytecode=True
import contextlib
import datetime
import hashlib
import io
import json
import math
from pathlib import Path
import resource
import shutil
import time
import types
import numpy as np

RUNTIME=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=RUNTIME/'gravity/response_inverse/extension_transfer/independent_transfer_review'
MANIFEST=json.loads((OUT/'snapshot_manifest_v1.json').read_text())
SOURCES={Path(r['original']).name:r for r in MANIFEST['sources']}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()


def guard():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RUNTIME/p).exists() for p in ['STOP_REQUESTED.json','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'])
    for row in MANIFEST['sources']+MANIFEST['receipts']:
        assert sha(row['original'])==sha(row['snapshot'])==row['sha256']


def subject(name):
    row=SOURCES[name+'.py'];module=types.ModuleType(name)
    module.__file__=row['original'];sys.modules[name]=module
    exec(compile(Path(row['snapshot']).read_text(),row['original'],'exec'),module.__dict__)
    return module


def write(path,data):
    assert not path.exists(),path
    path.write_text(json.dumps(data,indent=2)+'\n')


def run(subject,stage,log):
    argv=sys.argv
    try:
        sys.argv=[subject.__file__,'--stage',stage]
        with contextlib.redirect_stdout(io.StringIO()) as capture:
            subject.main()
        log.write_text(capture.getvalue())
    finally:sys.argv=argv


def main():
    guard();start=time.monotonic()
    op=subject('direct_galaxy_response_operator')
    validator=subject('direct_validate_inverse_fields')
    transfer=subject('direct_extension_transfer')
    original_freeze=json.loads((OUT/'snapshot_FREEZE.json').read_text())
    original_selection=json.loads((OUT/'snapshot_contract_and_subset_freeze.json').read_text())
    assert transfer.NAMES==original_freeze['names']==original_selection['conditional_expansion']
    expected_weights={k:np.array(v) for k,v in original_freeze['candidates'].items()}
    original_fits=json.loads((OUT/'snapshot_shared_response_fits_v1.json').read_text())
    original_margin=json.loads((OUT/'snapshot_margin_candidate_v1.json').read_text())
    parent_candidate=next(c['best_sampled'] for c in original_fits['cases']
        if c['family']+'_'+c['constraints']==transfer.LABEL)
    assert np.array_equal(expected_weights['original_D_joint'],parent_candidate['weights'])
    assert np.array_equal(expected_weights['interior_D_joint'],original_margin['weights'])
    assert original_margin['external_newtonian_SI']==parent_candidate['external_newtonian_SI']
    root=OUT/'fixtures';root.mkdir(exist_ok=False)
    data_dir=root/'data';data_dir.mkdir();(data_dir/'qumond_disk').mkdir()
    fields_dir=root/'fields';fields_dir.mkdir()
    extension=fields_dir/'extension_transfer';extension.mkdir()
    source,target,arrays={},{},{}
    for i,(name,n) in enumerate(zip(transfer.NAMES,[2,3,1,4,2,3])):
        R=np.arange(1,n+1,dtype=float);A=np.arange(1,n+1,dtype=float)+i+2
        V=np.sqrt(A*R);error=.05*V
        source[name+'_R']=np.r_[.1,R,99.]
        source[name+'_score_mask']=np.r_[False,np.ones(n,dtype=bool),False]
        target[name+'_v']=np.r_[-999.,V,np.nan]
        target[name+'_error']=np.r_[-999.,error,np.nan]
        arrays[name]={'R':R,'A':A,'V':V,'error':error}
        write(data_dir/'qumond_disk'/f'source_{name}.json',{'synthetic':True,'name':name})
        for tag in ['base','refined','boundary_extension']:
            (fields_dir/f'newtonian_field_{name}_{tag}.npz').write_bytes(('SYNTHETIC '+name+' '+tag).encode())
    np.savez(data_dir/'baryonic_forward_64.npz',**source)
    np.savez(data_dir/'sealed_targets.npz',**target)
    write(data_dir/'qumond_disk/contract_and_subset_freeze.json',{'conditional_expansion':transfer.NAMES})
    fits={'cases':[{'family':'D','constraints':'galaxies_external_solar',
                   'best_sampled':{'status':0,'weights':expected_weights['original_D_joint'].tolist()}}]}
    write(fields_dir/'shared_response_fits_v1.json',fits)
    write(fields_dir/'margin_candidate_v1.json',{'status':0,'weights':expected_weights['interior_D_joint'].tolist(),
          'parent_fits_sha256':sha(fields_dir/'shared_response_fits_v1.json')})
    op.OUT=fields_dir;op.field.DATA=data_dir;transfer.OUT=extension
    op.source_receipt=lambda name:data_dir/'qumond_disk'/f'source_{name}.json'
    # The field classes are hard traps. Only toy response arithmetic is allowed.
    op.field.RingField=lambda *a,**k:(_ for _ in ()).throw(AssertionError('Actual field construction forbidden'))
    config={'interrupt':None,'mutate':False,'bad_control':False,'failures':True}
    geometry_calls=[];weight_calls=[];load_calls=[];target_keys=[]
    def geometry(name,tag='base',refine=False):
        geometry_calls.append((name,tag,refine))
        if name==config['interrupt']:raise RuntimeError('Synthetic foreground interruption')
        a=arrays[name]
        return {'name':name,'tag':tag,'R':a['R'],'mr':a['A']}, {'projection':{'full':1.1*a['A']}},None
    op.galaxy_geometry=geometry
    validator.boundary_extension=lambda name,data,receipt:{**data,'tag':'boundary_extension'}
    def label_for(w):
        return next(k for k,v in expected_weights.items() if w.tobytes()==v.tobytes())
    def toy_force(name,tag,label):
        i=transfer.NAMES.index(name);A=arrays[name]['A']
        factor=(1.11+.02*i) if label=='original_D_joint' else (.93-.01*i)
        multiplier={'base':1.,'refined':1.002,'boundary_extension':1.001}[tag]
        if config['failures']:
            if i==0 and label=='interior_D_joint' and tag=='base':return -A.copy()
            if i==1 and label=='original_D_joint' and tag=='refined':multiplier=1.008
            if i==2 and label=='interior_D_joint' and tag=='boundary_extension':multiplier=1.004
            if i==3 and label=='original_D_joint' and tag=='refined':return np.full_like(A,np.nan)
            if i==4 and label=='original_D_joint':factor=1.21+1e-12
        return A*factor*multiplier
    class Projection:
        def __init__(self,data):
            self.data=data;self.norm_SI=np.ones_like(data['R']);self.mid_norm_SI=self.norm_SI.copy()
        def combined(self,w):
            label=label_for(w);weight_calls.append((self.data['name'],self.data['tag'],label,w.tobytes()))
            if config['mutate']:w[0]+=.001
            return toy_force(self.data['name'],self.data['tag'],label)
        def project(self,a,b):
            if np.ndim(a)==0:return self.data['mr']*(1.01 if config['bad_control'] else 1.)
            return self.data['mr']*1.1
    op.LinearProjection=Projection
    real_load=np.load
    class Archive:
        def __init__(self,path):self.path=Path(path);self.archive=real_load(path)
        def __enter__(self):return self
        def __exit__(self,*args):self.archive.close()
        def __getitem__(self,key):
            if self.path.name=='sealed_targets.npz':target_keys.append(key)
            return self.archive[key]
    def safe_load(path,*a,**k):
        path=Path(path)
        assert path.parent==data_dir,'No actual campaign array may be read'
        load_calls.append(str(path));return Archive(path)
    np.load=safe_load
    outcomes={}
    try:
        run(transfer,'freeze',root/'freeze.stdout')
        freeze=json.loads((extension/'FREEZE.json').read_text())
        assert freeze['candidates']==original_freeze['candidates']
        # Missing prerequisite fails before field or target operations.
        try:run(transfer,'base',root/'unexpected.stdout')
        except FileNotFoundError:pass
        else:raise AssertionError('Missing prerequisite accepted')
        assert geometry_calls==[] and load_calls==[]
        write(fields_dir/'field_validation_v1.json',{'fits_sha256':freeze['identities']['fits'],
              'candidate_passes':{transfer.LABEL:True}})
        write(fields_dir/'margin_field_validation_v1.json',{'passed':True,'candidate_sha256':freeze['identities']['margin']})
        # Interrupted run preserves the first two sources; resume computes four.
        config['interrupt']=transfer.NAMES[2]
        try:run(transfer,'base',root/'unexpected.stdout')
        except RuntimeError:pass
        else:raise AssertionError('Synthetic interruption not triggered')
        saved={p.name:sha(p) for p in extension.glob('base_*_v1.json')}
        assert len(saved)==2 and load_calls==[]
        config['interrupt']=None;geometry_calls.clear()
        run(transfer,'base',root/'base_resumed.stdout')
        assert [r[0] for r in geometry_calls]==transfer.NAMES[2:]
        assert all(sha(extension/p)==h for p,h in saved.items())
        assert len(list(extension.glob('base_*_v1.json')))==6 and load_calls==[]
        outcomes['base_resume']={'preserved_receipts':2,'new_sources_after_resume':4,'target_array_reads':0}
        # Score cannot open targets until all six validation receipts exist.
        try:run(transfer,'score',root/'unexpected.stdout')
        except FileNotFoundError:pass
        else:raise AssertionError('Premature score accepted')
        assert load_calls==[]
        run(transfer,'validate',root/'validate.stdout')
        assert len(list(extension.glob('validate_*_v1.json')))==6 and load_calls==[]
        assert len(weight_calls)==36
        assert all(value==expected_weights[label].tobytes() for _,_,label,value in weight_calls)
        completed={p.name:sha(p) for p in extension.glob('*_*_v1.json')}
        geometry_calls.clear();run(transfer,'base',root/'base_noop.stdout');run(transfer,'validate',root/'validate_noop.stdout')
        assert geometry_calls==[] and all(sha(extension/p)==h for p,h in completed.items())
        outcomes['complete_resume']={'field_calls':0,'receipts_preserved':len(completed)}
        # All two-candidate failures are retained; later sources still finish.
        flags={}
        for i,name in enumerate(transfer.NAMES):
            row=json.loads((extension/f'validate_{name}_v1.json').read_text())
            assert row['target_arrays_read'] is False
            flags[name]={k:v['passed'] for k,v in row['candidates'].items()}
            assert not row['candidates']['interior_D_joint']['passed'] if i in [0,2] else row['candidates']['interior_D_joint']['passed']
            assert not row['candidates']['original_D_joint']['passed'] if i in [1,3] else row['candidates']['original_D_joint']['passed']
        outcomes['field_failure_flags']=flags
        run(transfer,'score',root/'score.stdout')
        result=json.loads((extension/'RESULTS_v1.json').read_text())
        assert len(result['rows'])==6 and list(result['combined'])==list(expected_weights)
        assert len(load_calls)==2 and len(target_keys)==12
        scores={};allowances={}
        for i,row in enumerate(result['rows']):
            name=transfer.NAMES[i];a=arrays[name]
            assert row['name']==name and row['observed_velocity']==a['V'].tolist()
            for label in expected_weights:
                for method,tag in [('base','base'),('refined','refined'),('boundary','boundary_extension')]:
                    F=toy_force(name,tag,label)
                    finite=all(math.isfinite(float(x)) for x in F)
                    if finite:
                        needed=[max(0.,(float(f)-(float(v)+2*float(e))**2/float(r))/float(A),
                                    (max(0.,float(v)-2*float(e))**2/float(r)-float(f))/float(A))
                                for f,v,e,r,A in zip(F,a['V'],a['error'],a['R'],a['A'])]
                        t=max(needed)
                    else:needed=None;t=None
                    s=None if not finite or min(F)<=0 else math.sqrt(sum((.5*math.log10(float(f)/float(A)))**2 for f,A in zip(F,a['A']))/len(F))
                    got=row['candidates'][label]['methods'][method]
                    assert got['required_rectangle_t'] is None if t is None else abs(got['required_rectangle_t']-t)<2e-15
                    assert got['rms_log10_velocity'] is None if s is None else abs(got['rms_log10_velocity']-s)<2e-15
                    if s is not None:
                        assert np.max(np.abs(np.array(got['predicted_velocity'])-np.sqrt(a['R']*F)))<1e-14
                    scores.setdefault((label,method),[]).append(s)
                    allowances.setdefault((label,method),[]).append(t)
        for label,entry in result['combined'].items():
            assert entry['numerical_pass'] is False
            for method,values in entry['methods'].items():
                s=scores[label,method];t=allowances[label,method]
                expected_s=None if None in s else math.sqrt(sum(x*x for x in s)/6)
                expected_t=None if None in t else max(t)
                assert values['equal_galaxy_rms_log10_velocity'] is None if expected_s is None else abs(values['equal_galaxy_rms_log10_velocity']-expected_s)<2e-15
                assert values['largest_rectangle_t'] is None if expected_t is None else abs(values['largest_rectangle_t']-expected_t)<2e-15
        tiny=result['rows'][4]['candidates']['original_D_joint']['methods']['base']['required_rectangle_t']
        assert 0<tiny<2e-12
        outcomes['readout']={'combined':result['combined'],'target_loads':len(load_calls),
                             'synthetic_target_array_keys':len(target_keys),'tiny_violation_retained':tiny,
                             'unequal_rows_per_source':[2,3,1,4,2,3],'all_36_weight_calls_bitwise_unchanged':True}
        # Mismatched receipt identities are rejected on resume, no target read.
        resume_dir=root/'bad_resume';shutil.copytree(extension,resume_dir)
        transfer.OUT=resume_dir
        path=resume_dir/f'base_{transfer.NAMES[0]}_v1.json';r=json.loads(path.read_text());r['freeze_sha256']='changed';path.write_text(json.dumps(r))
        before=len(load_calls)
        try:run(transfer,'base',root/'unexpected.stdout')
        except AssertionError:pass
        else:raise AssertionError('Stale receipt accepted')
        assert len(load_calls)==before
        outcomes['mismatched_resume_receipt_rejected']=True
        # A source/candidate/data identity change is detected before any fields.
        before=len(geometry_calls)
        path=fields_dir/'margin_candidate_v1.json';original_bytes=path.read_bytes();path.write_bytes(original_bytes+b' ')
        try:run(transfer,'validate',root/'unexpected.stdout')
        except AssertionError:pass
        else:raise AssertionError('Changed candidate identity accepted')
        path.write_bytes(original_bytes)
        assert len(geometry_calls)==before
        outcomes['changed_candidate_identity_rejected']=True
        # A deliberate runtime weight mutation fails before the first receipt.
        mutation_dir=root/'weight_mutation';mutation_dir.mkdir();shutil.copyfile(extension/'FREEZE.json',mutation_dir/'FREEZE.json')
        transfer.OUT=mutation_dir;config['mutate']=True
        try:run(transfer,'base',root/'unexpected.stdout')
        except AssertionError:pass
        else:raise AssertionError('Changed runtime weights accepted')
        assert list(mutation_dir.glob('base_*'))==[]
        outcomes['runtime_weight_mutation_rejected_before_save']=True
    finally:np.load=real_load
    guard()
    receipt={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,
        'source_sha256':sha(__file__),'snapshot_manifest_sha256':sha(OUT/'snapshot_manifest_v1.json'),
        'actual_galaxy_fields':0,'actual_target_arrays_read':False,'actual_refits':0,
        'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'checks':outcomes}
    write(OUT/'synthetic_transfer_checks_v1.json',receipt)
    print(json.dumps({k:v for k,v in receipt.items() if k!='checks'},indent=2))


if __name__=='__main__':main()
