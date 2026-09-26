#!/usr/bin/env python3
"""Run the fixed declared cubic correlation screen after calibration."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np
from context_exchange_sim import run

HERE=Path(__file__).resolve().parent


def main():
    calibration=json.loads((HERE/'CONTEXT_SIMULATION_CALIBRATION.json').read_text())
    assert calibration['all_predeclared_gates_passed']
    assert calibration['simulator_sha256']==hashlib.sha256((HERE/'context_exchange_sim.py').read_bytes()).hexdigest()
    destination=HERE/'context_exchange_screen'
    destination.mkdir(exist_ok=True)
    modes=np.array([[1,0,0],[0,1,0],[0,0,1],
                    [1,1,0],[1,-1,0],[1,0,1],[1,0,-1],[0,1,1],[0,1,-1],
                    [1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1]])
    cases=[('context_minimal_L16',16,-1.,1.,.05,0,2026092130),
           ('context_minimal_L24',24,-1.,1.,.05,0,2026092131),
           ('context_minimal_L32',32,-1.,1.,.05,0,2026092132),
           ('context_constant_L16',16,-1.,1.,4.,1,2026092133),
           ('flat_symmetric_L16',16,0.,0.,.05,0,2026092134)]
    plan={'screen_plan_sha256':hashlib.sha256((HERE/'CONTEXT_EXCHANGE_SCREEN_PLAN.md').read_bytes()).hexdigest(),
          'simulator_sha256':calibration['simulator_sha256'],
          'launcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'cases':cases,'trajectories_per_case':256,'threads':4}
    (destination/'PLAN.json').write_text(json.dumps(plan,indent=2)+'\n')
    results=[]
    for name,side,u,coupling,floor,variant,seed in cases:
        output=destination/f'{name}.npz'
        if output.exists() or output.with_suffix('.json').exists():
            raise RuntimeError(f'Refusing to replace existing screen evidence: {name}')
        print(json.dumps({'starting_case':name,'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}),flush=True)
        times=np.linspace(0,2*np.pi,65)/(2*np.pi/(side*np.sqrt(6)))
        raw,stats,seeds,metadata=run([side]*3,modes,[.5]+[1/12]*6,times,
                                    256,seed,u,coupling,floor,variant,0.,4)
        np.savez_compressed(output,fields=raw,statistics=stats,seeds=seeds,
                            times=times,modes=modes,wavevectors=np.asarray(metadata['wavevectors']))
        output.with_suffix('.json').write_text(json.dumps(metadata,indent=2)+'\n')
        summary={'case':name,'elapsed_seconds':metadata['elapsed_seconds'],
                 'total_proposals':metadata['total_proposals'],
                 'max_fourier_reconstruction_error':metadata['max_fourier_reconstruction_error'],
                 'raw_npz_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
                 'metadata_sha256':hashlib.sha256(output.with_suffix('.json').read_bytes()).hexdigest()}
        results.append(summary)
        (destination/'COMPLETED_CASES.json').write_text(json.dumps(results,indent=2)+'\n')
        print(json.dumps(summary),flush=True)


if __name__=='__main__':
    main()
