#!/usr/bin/env python3
"""Run the predeclared new-rate screen after its finite-generator calibration."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np
from axis_balanced_exchange_sim import run

HERE=Path(__file__).resolve().parent


def main():
    calibration=json.loads((HERE/'AXIS_BALANCED_SIMULATION_CALIBRATION.json').read_text())
    assert calibration['all_predeclared_gates_passed']
    assert calibration['simulator_sha256']==hashlib.sha256((HERE/'axis_balanced_exchange_sim.py').read_bytes()).hexdigest()
    destination=HERE/'axis_balanced_screen';destination.mkdir(exist_ok=True)
    modes=np.array([[1,0,0],[0,1,0],[0,0,1],
                    [1,1,0],[1,-1,0],[1,0,1],[1,0,-1],[0,1,1],[0,1,-1],
                    [1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1]])
    cases=[('balanced_r025_L32',32,.25,0.,256,2026092175),
           ('balanced_r050_L32',32,.50,0.,256,2026092176),
           ('balanced_r075_L32',32,.75,0.,256,2026092177),
           ('balanced_growth_L24',24,.50,.04/24,512,2026092178),
           ('balanced_growth_L48',48,.50,.04/48,512,2026092179),
           ('balanced_r025_L64',64,.25,0.,256,2026092180),
           ('balanced_r050_L64',64,.50,0.,256,2026092181),
           ('balanced_r075_L64',64,.75,0.,256,2026092182)]
    plan={'plan_sha256':hashlib.sha256((HERE/'AXIS_BALANCED_SIMULATION_PLAN.md').read_bytes()).hexdigest(),
          'simulator_sha256':calibration['simulator_sha256'],'cases':cases,
          'launcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'threads':2}
    planpath=destination/'PLAN.json'
    if planpath.exists(): raise RuntimeError('Refusing to overwrite a screen')
    planpath.write_text(json.dumps(plan,indent=2)+'\n')
    results=[]
    for name,side,rho,epsilon,paths,seed in cases:
        output=destination/f'{name}.npz'
        if output.exists() or output.with_suffix('.json').exists():
            raise RuntimeError(f'Refusing to replace existing screen evidence: {name}')
        print(json.dumps({'starting_case':name,'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}),flush=True)
        reference_speed=2*rho*np.sqrt((1-rho)/3)
        times=np.linspace(0,side/reference_speed,65)
        raw,stats,seeds,metadata=run([side]*3,modes,[1-rho]+[rho/6]*6,times,paths,seed,
                                    0.,.5,.05,0,epsilon,2)
        np.savez_compressed(output,fields=raw,statistics=stats,seeds=seeds,
                            times=times,modes=modes,wavevectors=np.asarray(metadata['wavevectors']))
        output.with_suffix('.json').write_text(json.dumps(metadata,indent=2)+'\n')
        volume=side**3
        final_vacancies=stats[:,5]/volume
        exact=(1-rho)*np.exp(-6*epsilon*times[-1])
        summary={'case':name,'elapsed_seconds':metadata['elapsed_seconds'],
                 'total_proposals':metadata['total_proposals'],
                 'max_fourier_reconstruction_error':metadata['max_fourier_reconstruction_error'],
                 'reference_speed':float(reference_speed),
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
