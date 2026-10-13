#!/usr/bin/env python3
"""Correct the descriptive state convention from immutable stored histories."""
from pathlib import Path
import datetime, hashlib, json
import numpy as np

HERE = Path(__file__).resolve().parent
IC = HERE.parent / 'direct_thermal_matter_bridge'
OUT = HERE / 'physical_comparison_v2'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    OUT.mkdir(exist_ok=False)
    paths = [Path(__file__).resolve(), HERE/'evidence_v1/RESULTS.json',
             IC/'evidence_v3/histories/RESULTS.json']
    freeze = [{'path': str(p), 'sha256': sha(p)} for p in paths]
    (OUT/'FREEZE.json').write_text(json.dumps(freeze, indent=2)+'\n')
    limit = json.loads(paths[1].read_text())
    old = json.loads(paths[2].read_text())
    cfg = limit['configuration']
    target = limit['histories'][1]['rows']
    cases = []
    checks = []
    for caseid in ['split_k1e-05', 'split_k1e-06']:
        history = next(h for h in old['histories'] if h['case']['id'] == caseid)
        c = history['configuration']
        rows = []
        for j, (a, b) in enumerate(zip(history['rows'], target)):
            assert a['L'] == b['L']
            fx = c['xi']/cfg['xi0'] * np.exp(-1.5*(a['NJ']-b['NJ']))
            fy = c['yi']/cfg['yi0'] * np.exp(-2*(a['NJ']-b['NJ']))
            raw = np.array(a['state'])[[1,2,4,5]]
            field_einstein = raw*np.array([fx,fy,fx,fy])
            physical = field_einstein.copy()
            physical[2:] /= a['NJprime']
            # Independently reconstruct dimensional fields and velocities,
            # then divide by the limiting per-row physical normalizers.
            sxk=c['xi']*np.exp(-1.5*a['NJ']); syk=c['yi']*np.exp(-2*a['NJ'])
            sx0=cfg['xi0']*np.exp(-1.5*b['NJ']); sy0=cfg['yi0']*np.exp(-2*b['NJ'])
            oracle=raw*np.array([sxk/sx0,syk/sy0,sxk/sx0/a['NJprime'],syk/sy0/a['NJprime']])
            error=float(np.max(abs(physical-oracle)/np.maximum(1,abs(oracle))))
            checks.append(dict(case=caseid,row=j,passed=error<2e-14,error=error))
            declared=raw/np.sqrt(1+c['k'])
            rows.append(dict(row=j,L=a['L'],physical_state=physical.tolist(),
                             physical_difference_from_limit=(physical-np.array(b['state'])).tolist(),
                             normalization_correction=(field_einstein-declared).tolist(),
                             additional_clock_correction=(physical-field_einstein).tolist()))
        assert len(rows)==241
        diff=np.array([r['physical_difference_from_limit'] for r in rows])
        cases.append(dict(case=caseid,rows=rows,
                          maximum_scaled_state_difference_by_component=np.max(abs(diff),axis=0).tolist(),
                          final_scaled_state_difference=diff[-1].tolist(),
                          max_normalization_correction=float(np.max(abs(np.array([r['normalization_correction'] for r in rows])))),
                          max_clock_correction=float(np.max(abs(np.array([r['additional_clock_correction'] for r in rows]))))))
    assert all(sha(Path(x['path']))==x['sha256'] for x in freeze)
    result=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                scope='Stored-array arithmetic only. No history rerun or finite-k convergence criterion. Exact physical clock and actual gas-resolution normalization replace only the descriptive convention.',
                inputs=freeze,cases=cases,checks=checks,
                counts=dict(passed=sum(c['passed'] for c in checks),failed=sum(not c['passed'] for c in checks)))
    (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(counts=result['counts'],cases=[{k:v for k,v in c.items() if k!='rows'} for c in cases]),indent=2))
    return bool(result['counts']['failed'])

if __name__=='__main__':
    raise SystemExit(main())
