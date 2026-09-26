#!/usr/bin/env python3
"""Continue the frozen side-64 cases with identical per-path RNG seeds.

Only scheduling changes: recoverable batches and available thread counts.
The original launcher, scientific parameters, simulator and plan stay frozen.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import numpy as np
import numba as nb
import axis_balanced_exchange_sim as sim

HERE=Path(__file__).resolve().parent
DEST=HERE/'axis_balanced_screen'
DEADLINE=datetime(2026,9,21,11,32,19,tzinfo=timezone.utc).timestamp()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path,value):
    temporary=path.with_suffix(path.suffix+'.temporary')
    temporary.write_text(json.dumps(value,indent=2)+'\n')
    temporary.replace(path)


def identity_control():
    seeds=np.random.SeedSequence(2026092231).generate_state(16)
    neighbors,phases,_=sim.geometry([4]*3,np.array([[1,0,0],[1,1,0]]))
    ceiling,_=sim.rate_ceiling(0.,.5,.05,0)
    args=(neighbors,phases,sim.FIELDS,sim.VECTORS,
          np.array([.5]+[1/12]*6),np.linspace(0,1,5),0.,.5,.05,0,ceiling,.01)
    nb.set_num_threads(1)
    first=sim.many_paths(seeds,*args)
    nb.set_num_threads(2)
    second=sim.many_paths(seeds,*args)
    nb.set_num_threads(6)
    chunks=[sim.many_paths(seeds[start:start+4],*args) for start in range(0,16,4)]
    third=tuple(np.concatenate([chunk[j] for chunk in chunks]) for j in range(2))
    for j in range(2):
        assert np.array_equal(first[j],second[j])
        assert np.array_equal(first[j],third[j])
    return dict(seed=2026092231,trajectories=16,threads=[1,2,6],batch_size=4,
                raw_fields_and_statistics_bitwise_equal=True,
                control_has_births=True,simulator_sha256=digest(Path(sim.__file__)))


def available_threads():
    processes=subprocess.run(['ps','-axo','command='],capture_output=True,text=True,check=True).stdout.splitlines()
    native=any('Python.app/Contents/MacOS/Python' in line and
               'campaign12h/run_admissibility_wave_screen.py' in line for line in processes)
    old=any('Python.app/Contents/MacOS/Python' in line and
            'campaign12h/run_context_followup.py' in line for line in processes)
    return max(2,8-2*int(native)-4*int(old))


def main():
    control=identity_control()
    control_path=HERE/'AXIS_SCREEN_BATCH_IDENTITY_CONTROL.json'
    assert not control_path.exists()
    write_json(control_path,control)
    print(json.dumps({'identity_control':control}),flush=True)
    receipt=HERE/'AXIS_SCREEN_RESOURCE_HANDOFF.json'
    while not receipt.exists():
        if time.time()>DEADLINE-3600:
            raise RuntimeError('Handoff not ready before final hour; no new cases started')
        time.sleep(1)
    event=json.loads(receipt.read_text())
    # Wait until our stopped launcher has released its running case.
    for _ in range(30):
        process=subprocess.run(['ps','-p',str(event['pid']),'-o','command='],capture_output=True,text=True)
        if process.returncode!=0: break
        time.sleep(1)
    else: raise RuntimeError('Original launcher still exists after handoff')
    plan=json.loads((DEST/'PLAN.json').read_text())
    assert digest(DEST/'PLAN.json')==event['original_plan_sha256']
    assert digest(Path(sim.__file__))==plan['simulator_sha256']==control['simulator_sha256']
    results=json.loads((DEST/'COMPLETED_CASES.json').read_text())
    assert len(results)==5 and results[-1]['case']=='balanced_growth_L48'
    frozen_cases=plan['cases'][5:]
    assert [row[0] for row in frozen_cases]==['balanced_r025_L64','balanced_r050_L64','balanced_r075_L64']
    batch_dir=DEST/'continuation_batches';batch_dir.mkdir(exist_ok=False)
    schedule=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  driver_sha256=digest(Path(__file__)),plan_sha256=digest(DEST/'PLAN.json'),
                  handoff_sha256=digest(receipt),identity_control=control,
                  batch_size=32,cases=frozen_cases,batches=[],
                  policy='Same frozen path seeds and all scientific parameters. Threads use available CPU capacity. Stop before a batch whose conservative estimated duration reaches the fixed deadline; retain every completed batch.')
    schedule_path=DEST/'CONTINUATION_SCHEDULE.json'
    write_json(schedule_path,schedule)
    modes=np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,-1,0],[1,0,1],
                    [1,0,-1],[0,1,1],[0,1,-1],[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1]])
    neighbors,phases,wavevectors=sim.geometry([64]*3,modes)
    ceiling,minimum=sim.rate_ceiling(0.,.5,.05,0)
    for name,side,rho,epsilon,paths,seed in frozen_cases:
        assert side==64 and epsilon==0. and paths==256
        output=DEST/f'{name}.npz'
        assert not output.exists() and not output.with_suffix('.json').exists()
        speed=2*rho*np.sqrt((1-rho)/3)
        times=np.linspace(0,side/speed,65)
        probabilities=[1-rho]+[rho/6]*6
        seeds=np.random.SeedSequence(seed).generate_state(paths)
        case_started=time.monotonic();case_batches=[]
        print(json.dumps({'starting_case':name,'utc':datetime.now(timezone.utc).isoformat()}),flush=True)
        for start in range(0,paths,32):
            # The initial 20-minute allowance is deliberately conservative.
            allowance=1200 if not case_batches else max(300,2*max(r['elapsed_seconds'] for r in case_batches))
            if time.time()+allowance+300>DEADLINE:
                schedule['stopped_before_batch']={'case':name,'start':start,'reason':'fixed campaign deadline'}
                write_json(schedule_path,schedule)
                print(json.dumps(schedule['stopped_before_batch']),flush=True)
                return
            stop=min(start+32,paths);threads=available_threads();nb.set_num_threads(threads)
            started=time.monotonic()
            raw,stats=sim.many_paths(seeds[start:stop],neighbors,phases,sim.FIELDS,sim.VECTORS,
                                    np.array(probabilities),times,0.,.5,.05,0,ceiling,epsilon)
            elapsed=time.monotonic()-started
            assert np.max(stats[:,-1])<1e-8
            batch_path=batch_dir/f'{name}_{start:03d}_{stop:03d}.npz'
            np.savez_compressed(batch_path,fields=raw,statistics=stats,seeds=seeds[start:stop],
                                times=times,modes=modes,wavevectors=wavevectors)
            row=dict(case=name,start=start,stop=stop,threads=threads,elapsed_seconds=elapsed,
                     utc=datetime.now(timezone.utc).isoformat(),raw_npz_sha256=digest(batch_path),
                     total_proposals=int(stats[:,0].sum()),path=str(batch_path.relative_to(DEST)))
            case_batches.append(row);schedule['batches'].append(row)
            write_json(schedule_path,schedule);print(json.dumps(row),flush=True)
        chunks=[np.load(DEST/row['path']) for row in case_batches]
        raw=np.concatenate([chunk['fields'] for chunk in chunks])
        stats=np.concatenate([chunk['statistics'] for chunk in chunks])
        assert np.array_equal(np.concatenate([chunk['seeds'] for chunk in chunks]),seeds)
        for chunk in chunks: chunk.close()
        np.savez_compressed(output,fields=raw,statistics=stats,seeds=seeds,times=times,modes=modes,wavevectors=wavevectors)
        metadata=dict(sides=[side]*3,modes=modes.tolist(),wavevectors=wavevectors.tolist(),
            probabilities=probabilities,times=times.tolist(),trajectories=paths,seed=seed,
            u=0.,E=.5,floor_or_K=.05,variant='minimal',epsilon=epsilon,
            context_feature='s_i=2n-3v_i^2',alpha_when_u_zero=1.,rate_ceiling=ceiling,rate_minimum=minimum,
            elapsed_seconds=time.monotonic()-case_started,
            max_fourier_reconstruction_error=float(np.max(stats[:,-1])),total_proposals=int(stats[:,0].sum()),
            field_names=['density','vx','vy','vz','Qxx-Qyy','Qxx+Qyy-2Qzz'],
            source_sha256=digest(Path(sim.__file__)),versions={'numpy':np.__version__,'numba':nb.__version__},
            counts_audited_on_every_path=True,batch_schedule=case_batches,
            execution_change='Identical seeds, parameters and kernel; verified thread/batch identity.')
        write_json(output.with_suffix('.json'),metadata)
        vacancies=stats[:,5]/side**3
        summary=dict(case=name,elapsed_seconds=metadata['elapsed_seconds'],total_proposals=metadata['total_proposals'],
            max_fourier_reconstruction_error=metadata['max_fourier_reconstruction_error'],reference_speed=float(speed),
            exact_final_vacancy_fraction=float(1-rho),mean_final_vacancy_fraction=float(vacancies.mean()),
            estimated_standard_error=float(vacancies.std(ddof=1)/np.sqrt(paths)),mean_births_per_site=0.,
            raw_npz_sha256=digest(output),metadata_sha256=digest(output.with_suffix('.json')))
        results.append(summary);write_json(DEST/'COMPLETED_CASES.json',results)
        print(json.dumps(summary),flush=True)
    schedule['completed_utc']=datetime.now(timezone.utc).isoformat();write_json(schedule_path,schedule)


if __name__=='__main__': main()
