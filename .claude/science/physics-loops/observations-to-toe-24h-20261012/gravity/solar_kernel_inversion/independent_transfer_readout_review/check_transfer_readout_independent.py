#!/usr/bin/env python3
"""Independent fixed-force readout: exact binary-rational ratios, 70-digit logs."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import sys
sys.dont_write_bytecode=True
import hashlib,json,resource,time
from datetime import datetime,timezone
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
import numpy as np

HERE=Path(__file__).resolve().parent
SNAP=HERE/'snapshots'
RT=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
GEOMETRY=RT/'gravity/response_inverse'
NAMES=['NGC3949','NGC3972','UGC06667','UGC08837','DDO064','DDO168']
LABELS=['original_D_joint','interior_D_joint']
METHODS=['base','refined','boundary']

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()
def read(label):return json.loads((SNAP/label).read_text())
def guard():
    assert time.time()<json.loads((RT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RT/n).exists() for n in ('STOP_REQUESTED.json','USER_STOP_REQUESTED.json','STOP_REQUESTED','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'))
def exact(x):return Q.from_float(float(x))
def mpq(q):return mp.mpf(q.numerator)/q.denominator
def close(x,y,atol=3e-13):assert abs(float(x)-float(y))<=atol,(x,y)
def isots(x):return datetime.fromisoformat(x)

def run():
    began=time.perf_counter();guard();mp.mp.dps=70
    records=read_manifest=json.loads((HERE/'snapshot_manifest_v1.json').read_text())['records']
    hashes={r['label']:r['sha256'] for r in records}
    for r in records:assert sha(r['original'])==sha(r['snapshot'])==r['sha256']
    freeze=read('transfer_FREEZE.json');official=read('transfer_RESULTS_v1.json');parent=read('pack_extension_transfer_readout_v1.json')
    assert freeze['names']==NAMES and list(freeze['candidates'])==LABELS
    expected={'source':'pack_direct_extension_transfer.py','protocol':'pack_FROZEN_EXTENSION_TRANSFER.md',
      'operator':'pack_direct_galaxy_response_operator.py','validator':'pack_direct_validate_inverse_fields.py',
      'fits':'shared_response_fits_v1.json','margin':'margin_candidate_v1.json','source_data':'baryonic_forward_64.npz',
      'target_data':'sealed_targets.npz','original_selection':'contract_and_subset_freeze.json','margin_protocol':'pack_FOLLOWUP_MARGIN_PROTOCOL.md'}
    expected.update({'source_receipt_'+n:f'expanded_{n}_boundary_v4.json' for n in NAMES})
    assert set(expected)==set(freeze['identities'])
    assert all(freeze['identities'][k]==hashes[label] for k,label in expected.items())
    assert official['identities']==freeze['identities'] and official['freeze_sha256']==hashes['transfer_FREEZE.json']
    assert parent['identities']['reader']==hashes['pack_direct_transfer_readout_check.py']
    assert parent['identities']['freeze']==hashes['transfer_FREEZE.json']
    assert parent['identities']['official_results']==hashes['transfer_RESULTS_v1.json']
    for key in ('source_data','target_data'):assert parent['identities'][key]==freeze['identities'][key]
    selection=read('contract_and_subset_freeze.json');assert selection['conditional_expansion']==NAMES
    assert isots(selection['frozen_at'])<isots(freeze['at'])
    fits=read('shared_response_fits_v1.json');margin=read('margin_candidate_v1.json')
    candidate=next(c['best_sampled'] for c in fits['cases'] if c['family']=='D' and c['constraints']=='galaxies_external_solar')
    assert candidate['status']==margin['status']==0
    assert np.array_equal(candidate['weights'],freeze['candidates'][LABELS[0]])
    assert np.array_equal(margin['weights'],freeze['candidates'][LABELS[1]])
    assert candidate['external_newtonian_SI']==margin['external_newtonian_SI']==1.4915242022774435e-10
    assert margin['parent_fits_sha256']==hashes['shared_response_fits_v1.json']
    original_gate=read('field_validation_v1.json');margin_gate=read('margin_field_validation_v1.json')
    assert original_gate['candidate_passes']['D_galaxies_external_solar'] and margin_gate['passed']
    assert original_gate['fits_sha256']==hashes['shared_response_fits_v1.json']
    assert margin_gate['candidate_sha256']==hashes['margin_candidate_v1.json']
    training=read('training_parameters_frozen.json')
    U=next(e['parameters']['U'] for e in training['entries'] if e['dataset']=='forward64' and e['model']=='NL' and not e['fixed_U'])
    assert U==0.5605122519882025
    gates=[];receipts={};cache_records=[];chronology=[]
    for name in NAMES:
        base=read(f'base_{name}_v1.json');val=read(f'validate_{name}_v1.json')
        assert set(base['forces'])==set(val['candidates'])==set(LABELS)
        for r in (base,val):
            assert r['name']==name and r['identities']==freeze['identities']
            assert r['freeze_sha256']==hashes['transfer_FREEZE.json'] and r['target_arrays_read'] is False
        assert base['provisional'] is True
        assert val['base_receipt_sha256']==hashes[f'base_{name}_v1.json']
        assert parent['identities'][f'validate_{name}_v1.json']==hashes[f'validate_{name}_v1.json']
        assert isots(freeze['at'])<isots(base['at'])<isots(val['at'])<isots(official['at'])<isots(parent['at'])
        assert base['controls']['newtonian']<=.003 and base['controls']['prior_response']<=1e-10
        source=read(f'expanded_{name}_boundary_v4.json')
        assert source['source_sha256']==hashes['direct_qumond_disk.py']
        assert source['source_npz_sha256']==hashes['baryonic_forward_64.npz'] and source['U']==U
        assert np.array_equal(source['projection']['R'],base['R_kpc'])
        metadata={tag:read(f'geometry_{name}_{tag}.json') for tag in ('base','refined','boundary_extension')}
        for tag,key in (('base','geometry_sha256'),('refined','refined_geometry_sha256'),('boundary_extension','boundary_geometry_sha256')):
            cache=GEOMETRY/f'newtonian_field_{name}_{tag}.npz';h=sha(cache)
            assert h==metadata[tag]['cache_sha256']==(base if tag=='base' else val)[key]
            cache_records.append({'path':str(cache),'sha256':h,'bytes':cache.stat().st_size})
        for tag in ('base','refined'):
            ident=metadata[tag]['identity']
            assert ident['source_receipt_sha256']==hashes[f'expanded_{name}_boundary_v4.json']
            assert ident['source_npz_sha256']==hashes['baryonic_forward_64.npz']
            assert ident['solver_sha256']==hashes['direct_qumond_disk.py'] and ident['U']==U
        coarse_settings=metadata['base']['identity']['settings'];fine_settings=metadata['refined']['identity']['settings']
        for key in ('nr','nc','lmax'):assert fine_settings[key]==2*coarse_settings[key]
        for key in ('hankel','rmin','rmax'):assert fine_settings[key]==coarse_settings[key]
        boundary=metadata['boundary_extension']['identity']
        assert boundary['base_cache_sha256']==base['geometry_sha256'] and boundary['extension_factor']==2
        assert boundary['solver_sha256']==hashes['direct_qumond_disk.py']
        with np.load(GEOMETRY/f'newtonian_field_{name}_base.npz') as a,np.load(GEOMETRY/f'newtonian_field_{name}_boundary_extension.npz') as b:
            ar,br=a['radius'],b['radius']
            assert np.array_equal(ar,br[np.searchsorted(br,ar)])
            close(br[0],ar[0]/2);close(br[-1],ar[-1]*2)
            assert np.array_equal(a['R'],base['R_kpc']) and np.array_equal(b['R'],base['R_kpc'])
        for label in LABELS:
            c=val['candidates'][label];assert list(c['forces'])==METHODS
            f={k:np.array(v) for k,v in c['forces'].items()}
            assert all(np.all(np.isfinite(v)&(v>0)) for v in f.values())
            assert np.array_equal(f['base'],base['forces'][label])
            refine=max(abs(exact(v)/exact(u)-1) for u,v in zip(f['base'],f['refined']))
            edge=max(abs(exact(v)/exact(u)-1) for u,v in zip(f['base'],f['boundary']))
            close(refine,c['relative_changes']['refinement']);close(edge,c['relative_changes']['boundary'])
            assert refine<Q(5,1000) and edge<Q(3,1000) and c['passed']
            gates.append({'name':name,'candidate':label,'refinement':float(refine),'boundary':float(edge)})
        receipts[name]=val
        chronology.append({'name':name,'base_at':base['at'],'validation_at':val['at']})
        del source
    assert parent['all_numerical_gates_passed'] and len(gates)==12
    close(max(g['refinement'] for g in gates),parent['max_refinement_force_change'])
    close(max(g['boundary'] for g in gates),parent['max_boundary_force_change'])

    # Only after independently verifying all twelve gates, open actual processed targets.
    official_rows={r['name']:r for r in official['rows']};assert list(official_rows)==NAMES
    readout_rows={(r['name'],r['candidate'],r['method']):r for r in parent['rows']};assert len(readout_rows)==36
    rows=[];array_inventory=[];max_diffs={'velocity':0.,'log_residual':0.,'t':0.,'rms':0.}
    with np.load(SNAP/'baryonic_forward_64.npz') as source,np.load(SNAP/'sealed_targets.npz') as target:
        for name in NAMES:
            mask=source[name+'_score_mask'];rawR=source[name+'_R'];rawV=target[name+'_v'];rawE=target[name+'_error']
            assert mask.dtype==np.bool_ and mask.ndim==1 and len(mask)==len(rawR)==len(rawV)==len(rawE)
            inds=np.flatnonzero(mask);R=rawR[mask];V=rawV[mask];E=rawE[mask]
            assert np.all(np.isfinite(R)&(R>0)) and np.all(np.isfinite(V)&(V>0)) and np.all(np.isfinite(E)&(E>=0))
            off=official_rows[name];assert np.array_equal(R,off['R_kpc']) and np.array_equal(R,receipts[name]['R_kpc'])
            assert np.array_equal(V,off['observed_velocity']) and np.array_equal(E,off['processed_error'])
            array_inventory.append({'name':name,'raw_bins':len(mask),'scored_bins':len(inds),'scored_raw_indices':inds.tolist(),
              'excluded_raw_indices':np.flatnonzero(~mask).tolist(),'R_all':rawR.tolist(),'v_all':rawV.tolist(),'error_all':rawE.tolist()})
            for label in LABELS:
                for method in METHODS:
                    forces=receipts[name]['candidates'][label]['forces'][method]
                    parent_row=readout_rows[(name,label,method)];original=off['candidates'][label]['methods'][method]
                    logs=[];relax=[];bins=[]
                    for j,(r,v,e,f) in enumerate(zip(R,V,E,forces)):
                        r,v,e,f=map(exact,(r,v,e,f))
                        ratio=r*f/(v*v)
                        low=max(Q(0),v-2*e);high=v+2*e
                        t=max(Q(0),ratio-(high/v)**2,(low/v)**2-ratio)
                        log=mp.log10(mpq(ratio))/2
                        pred=mp.sqrt(mpq(r*f))
                        direction='underpredict' if r*f<low*low else 'overpredict' if r*f>high*high else 'inside'
                        assert (t>0)==(direction!='inside')
                        logs.append(log);relax.append(t)
                        record={'index':j,'raw_index':int(inds[j]),'R_kpc':float(r),'observed_kms':float(v),'error_kms':float(e),
                          'predicted_kms':float(pred),'lower_kms':float(low),'upper_kms':float(high),'direction':direction,
                          'velocity_residual_kms':float(pred-mpq(v)),'log10_residual':float(log),
                          'rectangle_t_exact':str(t),'rectangle_t':float(t)}
                        bins.append(record)
                        for arr in (parent_row['predicted_velocity'],original['predicted_velocity']):
                            diff=abs(float(pred)-arr[j]);assert diff<1e-12;max_diffs['velocity']=max(max_diffs['velocity'],diff)
                        diff=abs(float(log)-parent_row['log10_velocity_residual'][j]);assert diff<3e-15;max_diffs['log_residual']=max(max_diffs['log_residual'],diff)
                        for arr in (parent_row['required_t_by_row'],original['required_t_by_row']):
                            diff=abs(float(t)-arr[j]);assert diff<3e-14;max_diffs['t']=max(max_diffs['t'],diff)
                    ms=mp.fsum(x*x for x in logs)/len(logs);rms=mp.sqrt(ms)
                    worst=max(range(len(relax)),key=lambda j:relax[j])
                    outside=[j for j,t in enumerate(relax) if t>0]
                    for p in (parent_row,original):
                        diff=abs(float(rms)-p['rms_log10_velocity']);assert diff<3e-15;max_diffs['rms']=max(max_diffs['rms'],diff)
                        close(max(relax),p['required_rectangle_t'])
                    assert worst==parent_row['worst_bin']['index'] and len(outside)==parent_row['bins_outside_rectangle']
                    assert bins[worst]['direction']==parent_row['worst_bin']['direction']
                    for k in ('R_kpc','observed_kms','predicted_kms','lower_kms','upper_kms'):close(bins[worst][k],parent_row['worst_bin'][k],1e-12)
                    assert parent_row['points']==len(R)
                    rows.append({'name':name,'candidate':label,'method':method,'points':len(R),'mean_square_log_70digit':mp.nstr(ms,70),
                      'rms_log10_velocity':float(rms),'required_rectangle_t':float(max(relax)),
                      'outside_indices':outside,'under_count':sum(b['direction']=='underpredict' for b in bins),
                      'over_count':sum(b['direction']=='overpredict' for b in bins),'worst_rectangle':bins[worst],
                      'worst_absolute_log':max(bins,key=lambda b:abs(b['log10_residual'])),
                      'worst_absolute_kms':max(bins,key=lambda b:abs(b['velocity_residual_kms'])),'bins':bins})
    aggregate={}
    for label in LABELS:
        aggregate[label]={}
        for method in METHODS:
            subset=[r for r in rows if r['candidate']==label and r['method']==method]
            equal=mp.sqrt(mp.fsum(mp.mpf(r['mean_square_log_70digit']) for r in subset)/6)
            pooled=mp.sqrt(mp.fsum(mp.mpf(r['mean_square_log_70digit'])*r['points'] for r in subset)/sum(r['points'] for r in subset))
            failures=[r['name'] for r in subset if r['required_rectangle_t']>0]
            allbins=[dict(b,name=r['name']) for r in subset for b in r['bins']]
            summary={'equal_galaxy_rms_log10_velocity':float(equal),'pooled_bin_rms_diagnostic':float(pooled),
              'largest_rectangle_t':max(r['required_rectangle_t'] for r in subset),'sources_with_rectangle_failure':failures,
              'total_bins':sum(r['points'] for r in subset),'bins_outside_rectangle':sum(len(r['outside_indices']) for r in subset),
              'under_count':sum(r['under_count'] for r in subset),'over_count':sum(r['over_count'] for r in subset),
              'worst_rectangle':max(allbins,key=lambda b:b['rectangle_t']),
              'worst_absolute_log':max(allbins,key=lambda b:abs(b['log10_residual'])),
              'worst_absolute_kms':max(allbins,key=lambda b:abs(b['velocity_residual_kms']))}
            reference=parent['combined'][label][method]
            for key in ('equal_galaxy_rms_log10_velocity','largest_rectangle_t'):
                close(summary[key],reference[key]);close(summary[key],official['combined'][label]['methods'][method][key])
            for key in ('sources_with_rectangle_failure','total_bins','bins_outside_rectangle'):assert summary[key]==reference[key]
            aggregate[label][method]=summary
        assert all([r['outside_indices'] for r in rows if r['candidate']==label and r['method']==m]==[r['outside_indices'] for r in rows if r['candidate']==label and r['method']=='base'] for m in METHODS)
    guard()
    for r in records:assert sha(r['original'])==sha(r['snapshot'])==r['sha256']
    output={'at':datetime.now(timezone.utc).isoformat(),'status':'ALL_READOUTS_MATCH','reviewer_script_sha256':sha(__file__),
      'source_records':records,'geometry_cache_hashes':cache_records,'weights_unchanged':True,
      'external_E_unchanged':candidate['external_newtonian_SI'],'numerical_gates':gates,'chronology':chronology,
      'official_score_at':official['at'],'parent_readout_at':parent['at'],'processed_array_inventory':array_inventory,
      'combined':aggregate,'rows':rows,'maximum_arithmetic_differences':max_diffs,
      'method':'Exact binary-rational R*g/v^2 and rectangle classification, 70-digit logarithms/square roots, equal per-galaxy mean-square aggregation. No author helper imports or field reruns.',
      'limits':'Six previously exposed sources outside these response fits, not blind validation; fixed source and circular-speed readout assumptions, descriptive rectangles only. Convergence comparisons are not certified continuum error bounds.',
      'elapsed_seconds':time.perf_counter()-began,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    with (HERE/'independent_transfer_readout_checks_v1.json').open('x') as f:json.dump(output,f,indent=2)
    print(json.dumps({'status':output['status'],'score_rows':len(rows),'max_differences':max_diffs,
      'summary':{label:aggregate[label]['refined'] for label in LABELS},'elapsed_seconds':output['elapsed_seconds'],'max_rss_bytes':output['max_rss_bytes']},indent=2))

if __name__=='__main__':run()
