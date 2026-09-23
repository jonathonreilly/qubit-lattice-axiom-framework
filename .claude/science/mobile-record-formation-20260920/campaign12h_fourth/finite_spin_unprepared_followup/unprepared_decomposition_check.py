"""Full physical finite-spin first-output decomposition, without dynamic projection."""
from pathlib import Path
import importlib.util,hashlib,json,time
import numpy as np
from scipy.sparse.linalg import expm_multiply
D=Path(__file__).resolve().parent
p=D.parent/'finite_spin_post_birth_author/finite_spin_dynamics_check.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='5030a960accba4a654b27de92fcc7bdd074f179b207930ae0aa1b97af20ca3df'
s=importlib.util.spec_from_file_location('spin',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
times=np.linspace(0,1.2,4);m.times=times
flat_basis,reference,seeds,tail=m.flat_reference(48)
assert seeds[0]==(1,1,1)
rows=[]
for S in (64,96,128,192):
    started=time.monotonic()
    words,H,G=m.finite_target(S);ix={s:i for i,s in enumerate(words)}
    psi=np.zeros(len(words),complex)
    q,E=m.fmod.state((0,3),1,1);psi[ix[q,E[-1]]]=1
    embedding=m.embedding(words,flat_basis)
    flat=-(embedding@reference[0,:,0])/np.sqrt(2)
    bright=psi-flat
    assert abs(np.vdot(flat,flat)-.5)<1e-13
    assert abs(np.vdot(bright,bright)-.5)<1e-13
    assert abs(np.vdot(flat,bright))<1e-13
    initial=np.column_stack((flat,bright))
    A=-1j*H
    actual=expm_multiply(A,initial,start=times[0],stop=times[-1],num=len(times),traceA=A.diagonal().sum())
    f=np.array([v for q,v in words]);low=abs(f)<=8
    all_labels=[(a,r,z) for a in range(2) for r in range(6) for z in range(-S-4,S+5)]
    all_embedding=m.embedding(words,all_labels)
    controls=[]
    for i,t in enumerate(times):
        u,v=actual[i].T;whole=u+v
        ru=-(embedding@reference[i,:,0])/np.sqrt(2)
        reference_norm=float(np.sum(abs(reference[i,:,0])**2)/2)
        flat_error2=max(0.,float(np.vdot(u,u).real)+reference_norm-2*np.vdot(u,ru).real)
        row={'t':float(t),'flat_survival':float(np.vdot(u,u).real),'bright_survival':float(np.vdot(v,v).real),
             'cross_contribution':float(2*np.vdot(u,v).real),'full_survival':float(np.vdot(whole,whole).real),
             'prepared_half_reference':float(.5*np.exp(-4*m.kappa*t)),
             'flat_vector_error':float(np.sqrt(flat_error2)),
             'bright_low_circulation_weight':float(np.sum(abs(v[low])**2)),
             'bright_scaled_second_moment':float(np.dot(abs(v)**2,(f/S)**2)),
             'bright_physical_flat_projection_weight':float(np.sum(abs(all_embedding.conj().T@v)**2)),
             'bright_instantaneous_hazard':float(m.kappa*np.vdot(v,G@v).real),
             'full_instantaneous_hazard':float(m.kappa*np.vdot(whole,G@whole).real)}
        assert abs(row['full_survival']-row['flat_survival']-row['bright_survival']-row['cross_contribution'])<1e-10
        controls.append(row)
    vector_file=D/('PROPAGATED_S'+str(S)+'.npz');assert not vector_file.exists()
    np.savez_compressed(vector_file,charges=np.array([q for q,f in words],dtype=np.int8),circulations=f,
                        times=times,vectors=actual)
    row={'S':S,'eta':m.K*S*(S+1),'P_dimension':len(words),'elapsed_seconds':time.monotonic()-started,
         'vector_file':vector_file.name,'vector_sha256':hashlib.sha256(vector_file.read_bytes()).hexdigest(),
         'controls':controls}
    rows.append(row)
    print(json.dumps({'S':S,'elapsed_seconds':row['elapsed_seconds'],'last':controls[-1]}),flush=True)
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'parameters':{'K':m.K,'delta':m.delta,'kappa':m.kappa},
     'flat_reference_cutoff':48,'flat_reference_Dyson_tail_bound':tail,'rows':rows,
     'scope':'Exploratory unselected first-output finite-spin decomposition; no limiting bright law or strong/weak state convergence is asserted.'}
p=D/'DECOMPOSITION_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

