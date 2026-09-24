#!/usr/bin/env python3
"""Original 16-state star: clock mixture with one shared finite battery.

This uses the proved exact stationary-input finite-lift reduction, not a
materialization of exponentially many flag states or a reset battery channel.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/original_star_clock_control.py', 'scripts/clock_control.py', 'scripts/exact_star_energy.py')
from pathlib import Path
import contextlib,hashlib,importlib.util,json,shutil,sys,tempfile
sys.dont_write_bytecode=True
import numpy as np
import sympy as sy
from scipy.linalg import expm
from scipy.sparse.linalg import expm_multiply
import clock_control as clocks

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'exact_star_energy.py'
EXPECTED='6430b8fbc0766ac6e78c4beba477d8356028b9fd241e7ed04945d58501eb855b'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
with tempfile.TemporaryDirectory(prefix='autonomous-star-source-') as tmp:
    copy=Path(tmp)/'exact_star_energy.py';shutil.copyfile(SOURCE,copy)
    spec=importlib.util.spec_from_file_location('pinned_root_star',copy)
    m=importlib.util.module_from_spec(spec)
    with (HERE/'STAR_SOURCE_IMPORT.log').open('w') as out:
        with contextlib.redirect_stdout(out):spec.loader.exec_module(m)

C=6;epsilon=1/np.sqrt(C);kappa=.1;horizon=.1
H=np.array(sy.diag(m.h1,m.h3).subs(m.e,epsilon),complex)/epsilon**4
psi=np.zeros(16,complex)
psi[:4]=np.array((m.psi_num/sy.sqrt(m.norm)).subs(m.e,epsilon),complex).ravel()
assert np.linalg.norm(H@psi)<2e-12
energies,Q=np.linalg.eigh(H)
allowed=np.array([0.,36.,54.]);labels=np.argmin(abs(energies[:,None]-allowed[None,:]),axis=1)
assert max(abs(energies-allowed[labels]))<2e-12
energies=allowed[labels];h=float(max(energies));deltaE=energies[:,None]-energies[None,:]
initial=Q.conj().T@np.outer(psi,psi.conj())@Q
assert np.linalg.norm(initial*(labels[:,None]+labels[None,:]))<2e-12
raw=[]
for b in (1,2,3):
    pair=[]
    for sign in (1,-1):
        j=sy.zeros(16);j[4:,:4]=m.jump(b,sign)
        pair.append(np.array(j,complex))
    raw.append(pair)

rows=[]
for instrument in ('resolved','coherent'):
    marks=[j for pair in raw for j in pair] if instrument=='resolved' else [sum(pair) for pair in raw]
    ls=[np.sqrt(kappa)/epsilon*j for j in marks]
    gamma=sum(j.conj().T@j for j in ls);g=float(np.linalg.norm(gamma,2))
    I=np.eye(16);generator=-1j*(np.kron(I,H)-np.kron(H.T,I))
    for j in ls:
        jj=j.conj().T@j
        generator+=np.kron(j.conj(),j)-.5*(np.kron(I,jj)+np.kron(jj.T,I))
    rho0=np.outer(psi,psi.conj()).reshape(-1,order='F')
    exact_states=expm_multiply(generator,rho0,start=0,stop=horizon,num=5,endpoint=True)
    for n,w,L in ((256,8,31),(1024,16,127)):
        tau=horizon/n;gv,Rg=np.linalg.eigh(gamma)
        assert tau*g<=.5
        k0=(Rg*np.sqrt(1-tau*gv))@Rg.conj().T
        free=expm(-1j*tau*H)
        ks=[Q.conj().T@free@k0@Q]+[Q.conj().T@free@j@Q*np.sqrt(tau) for j in ls]
        assert np.linalg.norm(sum(k.conj().T@k for k in ks)-I)<2e-12
        prefixes=np.empty((n+1,16,16),complex);prefixes[0]=initial
        for k in range(n):prefixes[k+1]=sum(a@prefixes[k]@a.conj().T for a in ks)
        # The initial system occupies only the ground-energy block. For the
        # entire prefix lift, the translated battery overlap depends solely
        # on the two final energy labels. This is not repeated reduced maps.
        overlap=np.cos(np.pi/(L+1));factor=np.ones((16,16))
        for a in range(16):
            for c in range(16):
                if labels[a]!=labels[c]:factor[a,c]=overlap**(int(labels[a]!=0)+int(labels[c]!=0))
        finite_prefixes=prefixes*factor[None,:,:]
        assert max(abs(np.trace(finite_prefixes,axis1=1,axis2=2)-1))<3e-11
        xs,K,chi,J,R,boundary,e0=clocks.clock(w,n,horizon)
        clock_states=expm_multiply(-1j*K,chi,start=0,stop=horizon,num=5,endpoint=True)
        eta=min(2.,8*np.sin(np.pi/(2*(L+1))))
        collision=horizon*tau*(7*g*g+4*h*g)
        time_bound=tau*w+horizon*np.tan(np.pi/(w+1))/np.sqrt(w+1)
        total=eta+collision+2*g*time_bound+boundary
        for t,pt,exact in zip(np.linspace(0,horizon,5),clock_states,exact_states):
            weights=np.bincount(np.clip(xs,0,n),weights=abs(pt)**2,minlength=n+1)
            phase=np.exp(1j*(np.arange(n+1)*tau-t)[:,None,None]*deltaE[None,:,:])
            actual=np.einsum('k,kij->ij',weights,phase*finite_prefixes)
            target=Q.conj().T@exact.reshape(16,16,order='F')@Q
            error=clocks.trace_norm(actual-target)
            ea=float(np.dot(energies,np.diag(actual).real));et=float(np.dot(energies,np.diag(target).real))
            assert abs(np.trace(actual)-1)<4e-11
            assert min(np.linalg.eigvalsh((actual+actual.conj().T)/2))>-2e-12
            assert error<=min(2.,total)+3e-10
            assert abs(ea-et)<=h*min(2.,total)+3e-10
            rows.append({'instrument':instrument,'steps':n,'clock_width':w,'battery_width':L,
                         't':float(t),'state_trace_norm_error':error,'proved_uniform_diamond_bound':float(min(2.,total)),
                         'autonomous_system_energy':ea,'original_GKLS_system_energy':et,
                         'energy_error':abs(ea-et),'proved_energy_error_bound':float(h*min(2.,total)),
                         'clock_dimension':len(xs),'clock_program_energy_above_ground':float(2*J-e0),
                         'initial_battery_energy':float((L+1)*(36+54)/2),
                         'error_terms':{'battery':float(eta),'collisions':float(collision),
                                        'clock_time':float(2*g*time_bound),'finite_boundary':float(boundary)}})

result={'model':'Complete physical three-leaf star; S=2, C=6, delta=K=1, kappa=0.1, lambda=0',
        'original_star_source_sha256':EXPECTED,'rows':rows,'all_assertions_passed':True,
        'computation_scope':'Exact finite-lift stationary-input reduction of the shared-battery history, followed by finite-clock mixture; full continuous generator used for the comparison.',
        'limits':'This numeric star control covers the specified dressed input and lambda=0. Generic proof covers references and the electric family. No full exponentially large star/flag/clock matrix was materialized.',
        'independence':'Root consistency calculation, not independent reconstruction'}
(HERE/'ORIGINAL_STAR_CLOCK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
