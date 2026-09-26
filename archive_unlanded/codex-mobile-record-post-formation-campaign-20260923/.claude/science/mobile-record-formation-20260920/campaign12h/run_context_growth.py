#!/usr/bin/env python3
"""Execute only the predeclared calibrated continuing-formation cases."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np
from context_exchange_sim import run

HERE=Path(__file__).resolve().parent


def main():
    calibration=json.loads((HERE/'CONTEXT_GROWTH_CALIBRATION.json').read_text())
    assert calibration['all_predeclared_gates_passed']
    assert calibration['simulator_sha256']==hashlib.sha256((HERE/'context_exchange_sim.py').read_bytes()).hexdigest()
    destination=HERE/'context_exchange_growth';destination.mkdir(exist_ok=True)
    modes=np.array([[1,0,0],[0,1,0],[0,0,1],
                    [1,1,0],[1,-1,0],[1,0,1],[1,0,-1],[0,1,1],[0,1,-1],
                    [1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1]])
    cases=[('growth_scaled_L24',24,.04/24,2026092162),
           ('growth_scaled_L48',48,.04/48,2026092163),
           ('growth_fixed_clock_L48',48,.04/24,2026092164)]
    plan={'plan_sha256':hashlib.sha256((HERE/'CONTEXT_EXCHANGE_GROWTH_PLAN.md').read_bytes()).hexdigest(),
          'simulator_sha256':calibration['simulator_sha256'],'cases':cases,
          'launcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'trajectories_per_case':512,'threads':4}
    planpath=destination/'PLAN.json'
    if planpath.exists(): raise RuntimeError('Refusing to overwrite a growth run')
    planpath.write_text(json.dumps(plan,indent=2)+'\n')
    results=[]
    for name,side,epsilon,seed in cases:
        output=destination/f'{name}.npz'
        if output.exists() or output.with_suffix('.json').exists():
            raise RuntimeError(f'Refusing to replace existing growth evidence: {name}')
        print(json.dumps({'starting_case':name,'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}),flush=True)
        times=np.linspace(0,2*np.pi,65)/(2*np.pi/(side*np.sqrt(6)))
        raw,stats,seeds,metadata=run([side]*3,modes,[.5]+[1/12]*6,times,512,seed,
                                    -1.,1.,.05,0,epsilon,4)
        np.savez_compressed(output,fields=raw,statistics=stats,seeds=seeds,
                            times=times,modes=modes,wavevectors=np.asarray(metadata['wavevectors']))
        output.with_suffix('.json').write_text(json.dumps(metadata,indent=2)+'\n')
        volume=side**3
        final_vacancies=stats[:,5]/volume
        exact=.5*np.exp(-6*epsilon*times[-1])
        summary={'case':name,'elapsed_seconds':metadata['elapsed_seconds'],
                 'total_proposals':metadata['total_proposals'],
                 'max_fourier_reconstruction_error':metadata['max_fourier_reconstruction_error'],
                 'exact_final_vacancy_fraction':float(exact),
                 'mean_final_vacancy_fraction':float(final_vacancies.mean()),
                 'estimated_standard_error':float(final_vacancies.std(ddof=1)/np.sqrt(len(stats))),
                 'mean_births_per_site':float(stats[:,3].mean()/volume),
                 'raw_npz_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
                 'metadata_sha256':hashlib.sha256(output.with_suffix('.json').read_bytes()).hexdigest()}
        results.append(summary)
        (destination/'COMPLETED_CASES.json').write_text(json.dumps(results,indent=2)+'\n')
        print(json.dumps(summary),flush=True)


if __name__=='__main__': main()
