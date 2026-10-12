#!/usr/bin/env python3
"""Reproduce the exploratory post-transfer normalization/source diagnostic.

Recorded after the failed transfer was inspected. This does not refit a
response or implement a physical change to G, source parameters or N(A).
"""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np

HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity/response_inverse')
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    assert not args.output.exists()
    source=HERE/'extension_transfer_readout_v1.json'
    data=json.loads(source.read_text())
    assert data['all_numerical_gates_passed']
    frozen=json.loads((RUNTIME/'extension_transfer/FREEZE.json').read_text())
    out={'reader_sha256':sha(__file__),'input_sha256':sha(source),'responses':{}}
    for label in frozen['candidates']:
        rows=[r for r in data['rows'] if r['candidate']==label and r['method']=='refined']
        intervals=[];boosts=[]
        for row in rows:
            obs,err,pred=map(np.array,[row['observed_velocity'],row['processed_error'],row['predicted_velocity']])
            low=np.maximum(0,obs-2*err)/pred
            high=(obs+2*err)/pred
            for j in range(len(obs)):
                intervals.append({'name':row['name'],'index':j,'R_kpc':row['R_kpc'][j],
                                  'lower':float(low[j]),'upper':float(high[j])})
            path=RUNTIME/f"newtonian_field_{row['name']}_refined.npz"
            with np.load(path) as g:
                assert np.array_equal(g['R'],row['R_kpc'])
                vn=np.sqrt(g['R']*g['mr'])
                assert np.all(vn>0)
                j=row['worst_bin']['index']
                boosts.append({'name':row['name'],'geometry_sha256':sha(path),
                  'worst_rectangle_bin':j,'R_kpc':row['R_kpc'][j],
                  'newtonian_velocity_kms':float(vn[j]),
                  'candidate_velocity_kms':float(pred[j]),'observed_velocity_kms':float(obs[j]),
                  'candidate_radial_force_ratio_to_newtonian':float((pred[j]/vn[j])**2),
                  'observed_radial_acceleration_ratio_to_newtonian':float((obs[j]/vn[j])**2)})
        low=max(intervals,key=lambda r:r['lower'])
        high=min(intervals,key=lambda r:r['upper'])
        out['responses'][label]={'global_speed_scale_interval_empty':low['lower']>high['upper'],
          'max_lower':low,'min_upper':high,'N_max':1+sum(frozen['candidates'][label]),
          'radial_boost_diagnostics':boosts}
    original=json.loads((HERE/'extension_transfer_shape_diagnostic_v1.json').read_text())
    assert out['input_sha256']==original['input_sha256']
    assert out['responses']==original['responses']
    out['result']='PASS exact reproduction of exploratory numeric diagnostic; no physical normalization fit'
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(out['result'])

if __name__=='__main__':
    main()
