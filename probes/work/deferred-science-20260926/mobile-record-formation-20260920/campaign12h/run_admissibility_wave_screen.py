#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import numpy as np
import admissibility_wave_sim as sim

HERE=Path(__file__).resolve().parent;OUT=HERE/'admissibility_wave_screen'
SIM_SHA='05036372dba1644d281d71658c561ba265108dab4d3e87e8c44cfbedfe33c9d7'


def main():
    assert hashlib.sha256(Path(sim.__file__).read_bytes()).hexdigest()==SIM_SHA
    cal=json.loads((HERE/'ADMISSIBILITY_WAVE_CALIBRATION.json').read_text())
    assert len(cal['results'])==4 and all(x['passed'] for x in cal['results'])
    assert cal['plan']['simulator_sha256']==SIM_SHA
    OUT.mkdir(exist_ok=True)
    cases=[]
    for L in (16,32,48):
        for j in (0.,.5,.9):
            cases.append(dict(side=L,j=j,trajectories=128 if L<48 else 96,
                              seed=2026092220+len(cases),name=f'native_j{int(10*j):02d}_L{L}'))
    plan=dict(cases=cases,simulator_sha256=SIM_SHA,driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              text_plan_sha256=hashlib.sha256((HERE/'ADMISSIBILITY_WAVE_SCREEN_PLAN.md').read_bytes()).hexdigest(),
              macro_beta=.04,density=.5,density_amplitude=.04,max_macro_time=2.5,observations=65,
              modes=[[0,0,0],[1,0,0],[2,0,0],[3,0,0]],threads=2)
    (OUT/'PLAN.json').write_text(json.dumps(plan,indent=2)+'\n')
    done=[]
    for case in cases:
        path=OUT/(case['name']+'.npz');assert not path.exists(),'Preserve previous raw runs; no silent overwrite.'
        now=datetime.now(timezone.utc)
        if case['side']==48 and now>=datetime(2026,9,21,8,0,tzinfo=timezone.utc):
            record=dict(case=case['name'],status='omitted_resource_cutoff',utc=now.isoformat())
            done.append(record);print(json.dumps(record),flush=True)
            (OUT/'COMPLETED_CASES.json').write_text(json.dumps(done,indent=2)+'\n');continue
        print(json.dumps(dict(starting_case=case['name'],utc=now.isoformat())),flush=True)
        L=case['side'];times=np.linspace(0,2.5*L,65)
        raw,stats,seeds,metadata=sim.run([L]*3,plan['modes'],[.5]+[1/12]*6,times,
           case['trajectories'],case['seed'],epsilon=.04/L,threads=2,birth_j=case['j'],
           density_amplitude=.04,density_mode=[1,0,0])
        np.savez_compressed(path,fields=raw,statistics=stats,seeds=seeds,times=times,
                            modes=np.array(plan['modes']),wavevectors=np.asarray(metadata['wavevectors']))
        mp=path.with_suffix('.json');mp.write_text(json.dumps(metadata,indent=2)+'\n')
        record=dict(case=case['name'],status='completed',elapsed_seconds=metadata['elapsed_seconds'],
                    total_proposals=metadata['total_proposals'],
                    max_fourier_reconstruction_error=metadata['max_fourier_reconstruction_error'],
                    raw_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    metadata_sha256=hashlib.sha256(mp.read_bytes()).hexdigest())
        done.append(record);print(json.dumps(record),flush=True)
        (OUT/'COMPLETED_CASES.json').write_text(json.dumps(done,indent=2)+'\n')


if __name__=='__main__': main()
