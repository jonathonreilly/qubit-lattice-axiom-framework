#!/usr/bin/env python3
"""Parent's direct fixed-response transfer readout, independently in velocity units."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
RT=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
TRANS=RT/'gravity/response_inverse/extension_transfer'
DATA=RT/'galaxy_response'

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def read(p):
    return json.loads(Path(p).read_text())

def main():
    freeze=read(TRANS/'FREEZE.json')
    names=freeze['names']
    # Numerical receipts are read and qualified before any target or score.
    receipts={}
    identities={'reader':sha(__file__), 'freeze':sha(TRANS/'FREEZE.json')}
    max_refine=max_boundary=0.0
    for name in names:
        path=TRANS/f'validate_{name}_v1.json'
        if not path.exists():
            raise SystemExit(f'WAIT: numerical receipt absent for {name}; no targets read')
        rec=read(path)
        assert rec['freeze_sha256']==identities['freeze']
        assert rec['identities']==freeze['identities']
        for cand in rec['candidates'].values():
            assert cand['passed'], f'numerical gate failed for {name}; no targets read'
            max_refine=max(max_refine,cand['relative_changes']['refinement'])
            max_boundary=max(max_boundary,cand['relative_changes']['boundary'])
        receipts[name]=rec
        identities[path.name]=sha(path)
    assert max_refine<=.005 and max_boundary<=.003
    results_path=TRANS/'RESULTS_v1.json'
    if not results_path.exists():
        raise SystemExit('WAIT: all numerical gates passed, official scoring pending; no targets read')
    assert sha(DATA/'baryonic_forward_64.npz')==freeze['identities']['source_data']
    assert sha(DATA/'sealed_targets.npz')==freeze['identities']['target_data']
    results=read(results_path)
    assert results['identities']==freeze['identities']
    assert results['freeze_sha256']==identities['freeze']
    identities['official_results']=sha(results_path)
    identities['source_data']=freeze['identities']['source_data']
    identities['target_data']=freeze['identities']['target_data']
    official={r['name']:r for r in results['rows']}
    assert list(official)==names
    at=datetime.now(timezone.utc).isoformat()
    rows=[]
    with np.load(DATA/'baryonic_forward_64.npz') as source, \
         np.load(DATA/'sealed_targets.npz') as target:
        for name in names:
            mask=source[name+'_score_mask']
            radius=source[name+'_R'][mask]
            obs=target[name+'_v'][mask]
            err=target[name+'_error'][mask]
            assert np.array_equal(radius, receipts[name]['R_kpc'])
            assert np.array_equal(radius, official[name]['R_kpc'])
            assert np.array_equal(obs, official[name]['observed_velocity'])
            assert np.array_equal(err, official[name]['processed_error'])
            assert np.all(obs>0) and np.all(err>=0)
            lower=np.maximum(0,obs-2*err)
            upper=obs+2*err
            for label,candidate in receipts[name]['candidates'].items():
                for method,force_list in candidate['forces'].items():
                    force=np.array(force_list)
                    assert np.all(np.isfinite(force)&(force>0))
                    velocity=np.sqrt(radius*force)
                    expected=official[name]['candidates'][label]['methods'][method]
                    assert np.array_equal(velocity,expected['predicted_velocity'])
                    logs=np.log10(velocity/obs)
                    t=np.maximum(0,np.maximum(velocity*velocity-upper*upper,
                                              lower*lower-velocity*velocity)/(obs*obs))
                    rms=float(np.linalg.norm(logs)/np.sqrt(len(logs)))
                    assert np.isclose(rms,expected['rms_log10_velocity'],rtol=2e-13,atol=2e-14)
                    assert np.allclose(t,expected['required_t_by_row'],rtol=2e-13,atol=2e-14)
                    j=int(np.argmax(t))
                    direction=('overpredict' if velocity[j]>upper[j] else
                               'underpredict' if velocity[j]<lower[j] else 'inside')
                    rows.append({'name':name,'candidate':label,'method':method,
                                 'points':len(obs),'rms_log10_velocity':rms,
                                 'required_rectangle_t':float(t[j]),
                                 'bins_outside_rectangle':int(np.count_nonzero(t>0)),
                                 'worst_bin':{'index':j,'R_kpc':float(radius[j]),
                                    'observed_kms':float(obs[j]),'processed_error_kms':float(err[j]),
                                    'predicted_kms':float(velocity[j]),
                                    'lower_kms':float(lower[j]),'upper_kms':float(upper[j]),
                                    'direction':direction},
                                 'R_kpc':radius.tolist(),'observed_velocity':obs.tolist(),
                                 'processed_error':err.tolist(),'predicted_velocity':velocity.tolist(),
                                 'log10_velocity_residual':logs.tolist(),
                                 'required_t_by_row':t.tolist()})
    aggregate={}
    for label in freeze['candidates']:
        aggregate[label]={}
        for method in ['base','refined','boundary']:
            picked=[r for r in rows if r['candidate']==label and r['method']==method]
            assert len(picked)==6
            val={'equal_galaxy_rms_log10_velocity':float(np.sqrt(
                sum(r['rms_log10_velocity']**2 for r in picked)/6)),
                'largest_rectangle_t':max(r['required_rectangle_t'] for r in picked),
                'sources_with_rectangle_failure':[r['name'] for r in picked
                                                  if r['required_rectangle_t']>0],
                'total_bins':sum(r['points'] for r in picked),
                'bins_outside_rectangle':sum(r['bins_outside_rectangle'] for r in picked)}
            ref=results['combined'][label]['methods'][method]
            assert np.isclose(val['equal_galaxy_rms_log10_velocity'],
                              ref['equal_galaxy_rms_log10_velocity'],rtol=2e-13,atol=2e-14)
            assert np.isclose(val['largest_rectangle_t'],ref['largest_rectangle_t'],
                              rtol=2e-13,atol=2e-14)
            aggregate[label][method]=val
    out={'at':at,'identities':identities,'all_numerical_gates_passed':True,
         'max_refinement_force_change':max_refine,'max_boundary_force_change':max_boundary,
         'parent_method':'Direct processed-target identity check and independent arithmetic in velocity units; no original score helper imported.',
         'exposure':'Previously exposed out-of-fit development objects; no blind test, refit or likelihood.',
         'scope':'Both unchanged weight vectors only; preserve descriptive rectangle failures and source/pressure/nuisance assumptions.',
         'combined':aggregate,'rows':rows}
    destination=HERE/'extension_transfer_readout_v1.json'
    assert not destination.exists()
    destination.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'gates':{'refinement':max_refine,'boundary':max_boundary},
                      'combined':aggregate},indent=2))
    print('PASS: 36 source/candidate/method score rows independently recomputed; no refit.')

if __name__=='__main__':
    main()

