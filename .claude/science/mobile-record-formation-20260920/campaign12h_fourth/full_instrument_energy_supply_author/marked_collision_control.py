#!/usr/bin/env python3
"""All-input collision controls from the pinned complete root star matrices.
This is author consistency evidence, not a new independent reconstruction.
The source is imported in an expendable copy so sealed result files stay fixed.
"""
from pathlib import Path
from itertools import product
import contextlib,hashlib,importlib.util,json,shutil,sys,tempfile
sys.dont_write_bytecode=True
import numpy as np
import sympy as s
from scipy.linalg import expm,null_space

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'microscopic_birth_energy_author/exact_star_energy.py'
EXPECTED='ce202e534e19254516e7a3437c5c19e8a229334170eda73f65a16ae2f1fa377e'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
with tempfile.TemporaryDirectory(prefix='collision-star-source-') as tmp:
    copy=Path(tmp)/'exact_star_energy.py';shutil.copyfile(SOURCE,copy)
    spec=importlib.util.spec_from_file_location('pinned_root_star',copy)
    m=importlib.util.module_from_spec(spec)
    with (HERE/'STAR_SOURCE_IMPORT.log').open('w') as out:
        with contextlib.redirect_stdout(out):spec.loader.exec_module(m)

DS=16
HS=s.diag(m.h1,m.h3)
E2S=s.diag(*[sum(x*x for x in m.fields(q)) for N in (1,3) for q in m.bases[N]])
JS=[]
for b in (1,2,3):
    pair=[]
    for sign in (1,-1):
        j=s.zeros(DS);j[4:,:4]=m.jump(b,sign);pair.append(np.array(j,dtype=complex))
    JS.append(pair)

def model(S,lam,instrument):
    C=S*(S+1);eps=1/np.sqrt(C);delta=K=1.;kappa=.7
    H=delta/eps**4*np.array(HS.subs(m.e,eps),complex)+K*lam*np.array(E2S,complex)
    jumps=[j for pair in JS for j in pair] if instrument=='resolved' else [sum(pair) for pair in JS]
    ls=[np.sqrt(kappa)/eps*j for j in jumps]
    gamma=sum(j.conj().T@j for j in ls)
    g=float(np.linalg.norm(gamma,2));h=float(np.linalg.norm(H,2))
    assert abs(g-4*kappa/eps**2)<2e-12
    psi=np.zeros(DS,complex)
    psi[:4]=np.array((m.psi_num/s.sqrt(m.norm)).subs(m.e,eps),complex).ravel()
    return H,ls,gamma,psi,eps,g,h

def kraus(H,ls,gamma,tau):
    vals,q=np.linalg.eigh(gamma)
    assert tau*max(vals)<=.5+1e-13
    k0=(q*np.sqrt(np.maximum(0,1-tau*vals)))@q.conj().T
    evolve=expm(-1j*tau*H)
    ks=[evolve@k0]+[evolve@j*np.sqrt(tau) for j in ls]
    assert np.linalg.norm(sum(k.conj().T@k for k in ks)-np.eye(DS))<2e-12
    return ks

collision_rows=[]
for lam,instrument in ((0.,'resolved'),(1.,'coherent')):
    H,ls,gamma,psi,eps,g,h=model(2,lam,instrument)
    I=np.eye(DS);T=.2
    generator=-1j*(np.kron(I,H)-np.kron(H.T,I))
    for j in ls:
        jj=j.conj().T@j
        generator+=np.kron(j.conj(),j)-.5*(np.kron(I,jj)+np.kron(jj.T,I))
    exact=expm(T*generator)
    rho=np.outer(psi,psi.conj()).reshape(-1,order='F')
    exact_rho=(exact@rho).reshape(DS,DS,order='F')
    exact_energy=float(np.trace(H@exact_rho).real)
    case=[]
    for steps in (16,32,64,128):
        tau=T/steps;ks=kraus(H,ls,gamma,tau)
        channel=sum(np.kron(k.conj(),k) for k in ks)
        repeated=np.linalg.matrix_power(channel,steps)
        error=repeated-exact
        choi=error.reshape(DS,DS,DS,DS,order='F').transpose(0,2,1,3).reshape(DS*DS,DS*DS)
        assert np.linalg.norm(choi-choi.conj().T)<2e-10
        choi_upper=float(np.sum(np.abs(np.linalg.eigvalsh((choi+choi.conj().T)/2))))
        bound=T*tau*(7*g*g+4*h*g)
        assert choi_upper<=bound+2e-10
        evolved=(repeated@rho).reshape(DS,DS,order='F')
        energy=float(np.trace(H@evolved).real)
        assert abs(energy-exact_energy)<=h*bound+2e-10
        case.append({'lambda':lam,'instrument':instrument,'steps':steps,'tau':tau,
          'full_superoperator_Frobenius_error':float(np.linalg.norm(error)),
          'unnormalized_Choi_trace_norm_upper_bound':choi_upper,
          'proved_reduced_channel_bound':bound,'exact_GKLS_energy':exact_energy,
          'collision_energy':energy,'energy_error':abs(energy-exact_energy)})
    assert case[-1]['full_superoperator_Frobenius_error']<case[0]['full_superoperator_Frobenius_error']
    collision_rows+=case

# Physical marked isometry, its full unitary completion, and finite positive
# battery realization on every input column. Only lambda=0 is needed for
# this concrete two-ladder control; the general proof permits other spectra.
battery_rows=[]
for instrument in ('resolved','coherent'):
    H,ls,gamma,psi,eps,g,h=model(1,0.,instrument)
    tau=.01;ks=kraus(H,ls,gamma,tau);nf=len(ks)
    energies,Q=np.linalg.eigh(H)
    allowed=np.array([0.,4.,10.])
    labels=np.argmin(abs(energies[:,None]-allowed[None,:]),axis=1)
    assert max(abs(energies-allowed[labels]))<2e-12
    energies=allowed[labels]
    A=np.zeros((DS*nf,DS),complex)
    for mark,k in enumerate(ks):A[np.arange(DS)*nf+mark,:]=Q.conj().T@k@Q
    assert np.linalg.norm(A.conj().T@A-np.eye(DS))<2e-12
    blank=np.arange(DS)*nf
    other=np.setdiff1d(np.arange(DS*nf),blank)
    U=np.zeros((DS*nf,DS*nf),complex)
    U[:,blank]=A;U[:,other]=null_space(A.conj().T)
    completion_error=float(np.linalg.norm(U.conj().T@U-np.eye(DS*nf)))
    assert completion_error<2e-11
    v=((0,0),(1,0),(0,1))
    inpsi=Q.conj().T@psi
    assert np.linalg.norm(energies*inpsi)<2e-12
    out_labels=np.repeat(labels,nf)
    target=A@inpsi
    for L in (7,15,31):
        coords=tuple(product(range(L+2),repeat=2));index={n:i for i,n in enumerate(coords)};nb=len(coords)
        b=np.zeros(L+2);b[1:L+1]=np.sqrt(2/(L+1))*np.sin(np.pi*np.arange(1,L+1)/(L+1))
        beta=np.kron(b,b)
        shifted={}
        for a in range(3):
            for z in range(3):
                shift=tuple(v[z][c]-v[a][c] for c in (0,1))
                if shift in shifted:continue
                vec=np.zeros(nb)
                for n,amp in zip(coords,beta):
                    if amp:
                        dest=tuple(n[c]+shift[c] for c in (0,1))
                        assert dest in index
                        vec[index[dest]]+=amp
                assert abs(np.vdot(vec,vec)-1)<2e-14
                shifted[shift]=vec
        actual=np.empty((DS*nf,nb,DS),complex)
        for i in range(DS*nf):
            for j in range(DS):
                shift=tuple(v[labels[j]][c]-v[out_labels[i]][c] for c in (0,1))
                actual[i,:,j]=A[i,j]*shifted[shift]
        flat=actual.reshape(DS*nf*nb,DS)
        ideal=(A[:,None,:]*beta[None,:,None]).reshape(DS*nf*nb,DS)
        diff=flat-ideal
        op_error=float(np.sqrt(max(0,np.linalg.eigvalsh(diff.conj().T@diff)[-1])))
        d1=2*np.sin(np.pi/(2*(L+1)))
        assert op_error<=2*d1+3e-12
        state=(flat@inpsi).reshape(DS*nf,nb)
        probs=abs(state)**2
        system_final=float(np.dot(np.repeat(energies,nf),np.sum(probs,axis=1)))
        reservoir_energies=np.array([4*n[0]+10*n[1] for n in coords])
        reservoir_initial=float(np.dot(abs(beta)**2,reservoir_energies))
        reservoir_final=float(np.dot(np.sum(probs,axis=0),reservoir_energies))
        balance=abs(reservoir_initial-reservoir_final-system_final)
        assert balance<3e-11
        expected_energy=float(np.dot(np.repeat(energies,nf),abs(target)**2))
        assert abs(system_final-expected_energy)<3e-12
        max_joint_error=0.
        for mark in range(nf):
            for a in range(3):
                indices=np.flatnonzero(labels==a)*nf+mark
                p=float(np.sum(probs[indices,:]));q=float(np.sum(abs(target[indices])**2))
                max_joint_error=max(max_joint_error,abs(p-q))
        assert max_joint_error<2e-13
        battery_rows.append({'instrument':instrument,'L':L,'battery_dimension':nb,
          'flag_dimension':nf,'unitary_completion_error':completion_error,
          'all_input_isometry_operator_norm_error':op_error,'proved_isometry_bound':float(2*d1),
          'prepared_battery_energy':reservoir_initial,'delivered_system_energy':system_final,
          'target_collision_energy':expected_energy,'energy_balance_residual':balance,
          'stationary_input_joint_flag_energy_probability_error':max_joint_error})

result={'scope':'Complete sixteen-state physical star, original resolved/coherent jump matrices; author consistency controls',
 'source_sha256':EXPECTED,'collision_rows':collision_rows,'finite_battery_rows':battery_rows,
 'limits':'Reduced-channel convergence and complete discrete marked isometry; no continuous event-time path comparison or autonomous clock'}
(HERE/'MARKED_COLLISION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
