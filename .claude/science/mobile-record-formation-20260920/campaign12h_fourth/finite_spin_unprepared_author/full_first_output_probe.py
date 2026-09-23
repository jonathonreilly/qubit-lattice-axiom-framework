"""Unprojected actual first-output dynamics in the full finite-spin target."""
from pathlib import Path
import importlib.util,hashlib,json,time
import numpy as np
from scipy.sparse.linalg import expm_multiply
D=Path(__file__).resolve().parent
p=D.parent/'finite_spin_post_birth_author/finite_spin_dynamics_check.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='5030a960accba4a654b27de92fcc7bdd074f179b207930ae0aa1b97af20ca3df'
s=importlib.util.spec_from_file_location('spin',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
times=np.linspace(0,1.2,7)
rows=[]
for S in [4,8,16,32,64]:
    begin=time.monotonic()
    words,H,G=m.finite_target(S);ix={s:i for i,s in enumerate(words)}
    initial=np.zeros((len(words),2),complex)
    q,E=m.fmod.state((0,3),1,1)
    initial[ix[q,E[-1]],0]=1
    initial[:,1]=initial[:,0]/np.sqrt(2)
    q,E=m.fmod.state((0,3),0,1)
    initial[ix[q,E[-1]],1]=1/np.sqrt(2)
    assert np.max(abs(np.sum(abs(initial)**2,axis=0)-1))<1e-14
    labels=[(kind,r,f) for kind in range(2) for r in range(6) for f in range(-S-4,S+5)]
    embedding=m.embedding(words,labels)
    assert np.max(abs(np.sum(abs(embedding.conj().T@initial)**2,axis=0)-.5))<1e-13
    A=-1j*H
    actual=expm_multiply(A,initial,start=times[0],stop=times[-1],num=len(times),traceA=A.diagonal().sum())
    controls=[]
    low=np.array([abs(f)<=8 for q,f in words])
    fvalues=np.array([f for q,f in words])
    for ti,t in enumerate(times):
        flat_components=embedding.conj().T@actual[ti]
        for col,coherent in enumerate([False,True]):
            vector=actual[ti,:,col];prob=abs(vector)**2
            survival=float(sum(prob))
            flat_weight=float(np.sum(abs(flat_components[:,col])**2))
            unit_rotor_prediction=.5*(np.exp(-2*m.kappa*t)+np.exp(-4*m.kappa*t))
            controls.append({'t':float(t),'coherent_first':coherent,'survival':survival,
                             'rotor_first_limit_countercontrol':float(unit_rotor_prediction),
                             'physical_flat_weight':flat_weight,
                             'prepared_half_survival_reference':float(.5*np.exp(-4*m.kappa*t)),
                             'low_circulation_surviving_weight':float(np.sum(prob[low])),
                             'circulation_second_moment_unconditional':float(np.dot(prob,fvalues**2)),
                             'scaled_circulation_second_moment_unconditional':float(np.dot(prob,(fvalues/S)**2)),
                             'instantaneous_hazard_unconditional':float(m.kappa*np.vdot(vector,G@vector).real)})
    row={'S':S,'eta':m.K*S*(S+1),'physical_P_dimension':len(words),
         'elapsed_seconds':time.monotonic()-begin,'controls':controls}
    rows.append(row)
    print(json.dumps({'S':S,'elapsed_seconds':row['elapsed_seconds'],'last':controls[-2:]}),flush=True)
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'parameters':{'K':m.K,'delta':m.delta,'kappa':m.kappa},'rows':rows,
     'scope':'Full finite-spin target with actual normalized first outputs; exploratory convergence/escape evidence, no extrapolated theorem.'}
p=D/'FULL_FIRST_OUTPUT_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
