#!/usr/bin/env python3
"""Finite author controls; the written estimates carry all uniform quantifiers."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/FINITE_AUTONOMOUS_MARKED_DYNAMICS_UNDER_GRID_OBSERVATIONS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from pathlib import Path
import hashlib,json,math,time
import numpy as np
from scipy.linalg import expm,sqrtm

HERE=Path(__file__).resolve().parents[1]/'outputs/autonomous_marked_grid_observations_20260924'
norm=lambda x:float(np.linalg.norm(x,2))
def trnorm(x):return float(np.linalg.svd(x,compute_uv=False).sum())

def packet_controls():
    rows=[]
    for N in (3,4,5,8,17,50,201):
        theta=np.pi/N;j=np.arange(1,N)
        a=np.sin(theta*j)**2/np.sqrt(3*N/8)
        c1=float(a[:-1]@a[1:]);c2=float(a[:-2]@a[2:])
        want1=(2+np.cos(2*theta))/3
        want2=(2+np.cos(4*theta))/3-8*np.sin(theta)**4/(3*N)
        variance=2*(1+c2)-4*c1*c1
        wantv=16*np.sin(theta)**4*(2*N-3)/(9*N)
        assert abs(a@a-1)<2e-14
        assert max(abs(c1-want1),abs(c2-want2),abs(variance-wantv))<3e-14
        wrong2=(2+np.cos(4*theta))/3
        if N<=17:assert abs(c2-wrong2)>1e-6
        rows.append({'N':N,'c1':c1,'c2':c2,'variance_over_J_squared':variance,
                     'endpoint_correction':8*np.sin(theta)**4/(3*N)})
    return rows

def superop(a,b=None):
    if b is None:b=a
    return np.kron(b.conj(),a)

def choi(S,d):
    out=np.zeros((d*d,d*d),complex)
    for i in range(d):
        for j in range(d):
            E=np.zeros((d,d));E[i,j]=1
            out+=np.kron(E,(S@E.reshape(-1,order='F')).reshape((d,d),order='F'))
    return out

def marked_bin_controls():
    H=np.array([[.4,.3-.2j],[.3+.2j,1.1]])
    Ls=[np.array([[0,.7],[.2j,0]]),np.array([[.1,0],[.3,.2j]])]
    d=2;I=np.eye(d);Gamma=sum(L.conj().T@L for L in Ls);g=norm(Gamma);h=norm(H)
    Q=superop(-1j*H-Gamma/2,I)+superop(I,-1j*H-Gamma/2)
    jumps=[superop(L) for L in Ls];D=Q+sum(jumps);blocks=len(Ls)+2;s=d*d
    B=np.zeros((blocks*s,blocks*s),complex)
    B[:s,:s]=Q
    for j,J in enumerate(jumps,1):
        B[j*s:(j+1)*s,j*s:(j+1)*s]=Q
        B[j*s:(j+1)*s,:s]=J
        B[-s:,j*s:(j+1)*s]=sum(jumps)
    B[-s:,-s:]=D
    rows=[]
    for tau in (.04,.02,.01,.005):
        assert tau*g<=.5
        E=expm(B*tau);target=[E[k*s:(k+1)*s,:s] for k in range(blocks)]
        free=expm(-1j*H*tau)
        K0=free@np.asarray(sqrtm(I-tau*Gamma),complex)
        collision=[superop(K0)]+[tau*superop(free@L) for L in Ls]+[np.zeros((s,s))]
        assert norm(sum(target)-expm(D*tau))<2e-13
        bound=tau*tau*(7*g*g+4*h*g)
        upper=sum(trnorm(choi(a-b,d)) for a,b in zip(target,collision))
        assert upper<bound
        swapped=[collision[0],collision[2],collision[1],collision[3]]
        mutant=sum(trnorm(choi(a-b,d)) for a,b in zip(target,swapped))
        assert mutant>bound
        rows.append({'tau':tau,'marked_choi_trace_upper':upper,'analytic_bound':bound,
                     'swapped_marks_choi_trace':mutant,
                     'exact_channel_sum_residual':norm(sum(target)-expm(D*tau))})
    # A concrete maximally entangled input also witnesses failure of swapped marks.
    assert rows[-1]['swapped_marks_choi_trace']/d>rows[-1]['analytic_bound']
    return {'h':h,'g':g,'rows':rows,'scope':'Exact finite matrix exponentials numerically checked, not interval enclosures.'}

def julia(B):
    left=np.asarray(sqrtm(np.eye(B.shape[1])-B.conj().T@B),complex)
    right=np.asarray(sqrtm(np.eye(B.shape[0])-B@B.conj().T),complex)
    return np.block([[left,-B.conj().T],[B,right]])

def embed_system_flag(U,k,n):
    """U is indexed (flag,system); output indices are (system,all flags)."""
    F=2**n;answer=np.zeros((2*F,2*F),complex)
    bit=1<<(n-1-k)
    for a in range(2):
        for flags in range(F):
            old=int(bool(flags&bit))
            for b in range(2):
                for new in range(2):
                    newflags=(flags&~bit)|(new*bit)
                    answer[b*F+newflags,a*F+flags]=U[2*new+b,2*old+a]
    return answer

def lift(U,L,n):
    F=2**n;battery=L+2;D=2*F*battery;V=np.eye(D,dtype=complex)
    for total in range(1,L+2):
        inds=[(a*F+flag)*battery+(total-a) for a in range(2) for flag in range(F)]
        V[np.ix_(inds,inds)]=U
    return V

def pure_trace_difference(a,b):
    aa=float(np.vdot(a,a).real);bb=float(np.vdot(b,b).real)
    return math.sqrt(max(0.,(aa+bb)**2-4*abs(np.vdot(a,b))**2))

def process_control(tau):
    started=time.monotonic();n=3;L=40;F=2**n;battery=L+2;D=2*F*battery
    gap=math.sqrt(2);H=np.diag([0.,gap]);jump=np.array([[0.,.7],[.3,.2j]])
    g=norm(jump.conj().T@jump);U=julia(math.sqrt(tau)*jump)
    assert norm(U.conj().T@U-np.eye(4))<2e-13
    near=norm(U-np.eye(4));assert near<=2*math.sqrt(tau*g)
    # Altering only the nonblank input column preserves the instrument but loses
    # the global near-identity property required by the clock proof.
    bad=U@np.diag([1,1,-1,-1]);assert norm(bad-np.eye(4))>1.9
    assert np.linalg.norm(bad[:,:2]-U[:,:2])==0
    free_energy=np.array([(a+e)*gap for a in range(2) for f in range(F) for e in range(battery)])
    system_energy=np.array([a*gap for a in range(2) for f in range(F) for e in range(battery)])
    G=[np.eye(D,dtype=complex)];ideal=[np.eye(D,dtype=complex)]
    unitaries=[];Vprev=None;Uprev=None;composition=[]
    for k in range(n):
        u=embed_system_flag(U,k,n);v=lift(u,L,n);unitaries.append(u)
        assert norm(v.conj().T@v-np.eye(D))<3e-13
        assert np.max(abs((free_energy[:,None]-free_energy[None,:])*v))<2e-13
        assert norm(v-np.eye(D))<=near+3e-13
        if Vprev is not None:composition.append(norm(v@Vprev-lift(u@Uprev,L,n)))
        Vprev=v;Uprev=u
        phase=np.exp(1j*system_energy*k*tau)
        W=phase[:,None]*v*phase.conj()[None,:]
        unlifted=np.kron(u,np.eye(battery))
        WI=phase[:,None]*unlifted*phase.conj()[None,:]
        G.append(W@G[-1]);ideal.append(WI@ideal[-1])
    assert max(composition)<3e-13
    # A cyclic energy shift remains unitary but fails exact free-energy balance.
    cyclic=np.zeros((D,D),complex);u=unitaries[0]
    for a in range(2):
        for b in range(2):
            for f1 in range(F):
                for f2 in range(F):
                    value=u[a*F+f1,b*F+f2]
                    if not value:continue
                    for e in range(battery):
                        cyclic[(a*F+f1)*battery+(e+b-a)%battery,(b*F+f2)*battery+e]=value
    assert norm(cyclic.conj().T@cyclic-np.eye(D))<3e-13
    wrap_defect=norm((free_energy[:,None]-free_energy[None,:])*cyclic);assert wrap_defect>.01
    w=4;N=w+1;theta=np.pi/N;c1=(2+np.cos(2*theta))/3;J=1/(2*tau*c1)
    T=n*tau;a=2*J*T;R=math.ceil(8*a);xs=np.arange(-w-R,n+R+1);M=len(xs)
    ks=np.clip(xs,0,n);K=2*J*np.eye(M)-J*(np.diag(np.ones(M-1),1)+np.diag(np.ones(M-1),-1))
    e0=2*J*(1-np.cos(np.pi/(M+1)));K-=e0*np.eye(M)
    exact_clock_spectrum=2*(np.cos(np.pi/(M+1))-np.cos(np.pi*np.arange(1,M+1)/(M+1)))
    assert exact_clock_spectrum[0]==0 and np.all(exact_clock_spectrum>=0)
    clock_spectrum_error=float(max(abs(np.linalg.eigvalsh(K/J)-exact_clock_spectrum)))
    assert clock_spectrum_error<2e-12
    chi=np.zeros(M,complex)
    for x in range(-w,0):chi[x-xs[0]]=1j**x*np.sin(np.pi*(x+w+1)/N)**2/np.sqrt(3*N/8)
    beta=np.zeros(battery);beta[1:L+1]=np.sqrt(2/(L+1))*np.sin(np.pi*np.arange(1,L+1)/(L+1))
    payload=np.zeros((D,2),complex)
    for sys in range(2):payload[(sys*F)*battery:(sys*F+1)*battery,sys]=beta/math.sqrt(2)
    def controlled(v,inverse=False):
        out=np.empty_like(v)
        for kk in range(n+1):
            sel=(ks==kk);u=G[kk].conj().T if inverse else G[kk]
            out[sel]=np.einsum('ab,xbr->xar',u,v[sel],optimize=True)
        return out
    def hist(v,dt):
        z=controlled(v,True);z=np.einsum('xy,yar->xar',expm(-1j*K*dt),z,optimize=True)
        return controlled(z)
    def split_read(states,flag,feedback=False):
        out={};bits=np.array([bool((i//battery)%F & (1<<(n-1-flag))) for i in range(D)])
        for record,v in states.items():
            for bit in (0,1):
                z=v.copy();z[:,bits!=bool(bit),:]=0
                if feedback and bit:
                    z=z.reshape(M,2,F,battery,2)[:,::-1].reshape(M,D,2).copy()
                out[record+(bit,)]=z
        return out
    initial=chi[:,None,None]*payload[None,:,:]
    actual={():hist(initial,tau)}
    phi1=expm(-1j*K*tau)@chi
    lifted={():phi1[:,None,None]*(G[1]@payload)[None,:,:]}
    target={():phi1[:,None,None]*(ideal[1]@payload)[None,:,:]}
    actual=split_read(actual,0,True);lifted=split_read(lifted,0,True);target=split_read(target,0,True)
    for record in actual:
        actual[record]=hist(actual[record],2*tau)
        lifted[record]=np.einsum('xy,yar->xar',expm(-1j*K*2*tau),np.einsum('ab,xbr->xar',G[3]@G[1].conj().T,lifted[record],optimize=True),optimize=True)
        target[record]=np.einsum('xy,yar->xar',expm(-1j*K*2*tau),np.einsum('ab,xbr->xar',ideal[3]@ideal[1].conj().T,target[record],optimize=True),optimize=True)
    for flag in (1,2):
        actual=split_read(actual,flag);lifted=split_read(lifted,flag);target=split_read(target,flag)
    trace_sums=[sum(float(np.vdot(v,v).real) for v in states.values()) for states in (actual,lifted,target)]
    assert max(abs(z-1) for z in trace_sums)<1e-11
    clock_error=sum(pure_trace_difference(actual[r],lifted[r]) for r in actual)
    total_error=sum(pure_trace_difference(actual[r],target[r]) for r in actual)
    sig=4*J*np.sin(theta)**2/3*np.sqrt((2*N-3)/N)
    br=4*np.exp(a)*a**R/math.factorial(R)
    ec=2*np.sqrt(tau*g)*(w+T*sig)+br
    endpoint_rows=[]
    for step in (1,2,3):
        phi=expm(-1j*K*step*tau)@chi;prob=abs(phi)**2
        gram=np.zeros((D,D),complex);inverse_gram=np.zeros((D,D),complex)
        for kk in range(n+1):
            weight=float(prob[ks==kk].sum());deltaG=G[kk]-G[step]
            gram+=weight*(deltaG.conj().T@deltaG)
            inverse_gram+=weight*(deltaG@deltaG.conj().T)
        exact_endpoint=math.sqrt(max(0.,np.linalg.eigvalsh(gram)[-1]))
        exact_inverse=math.sqrt(max(0.,np.linalg.eigvalsh(inverse_gram)[-1]))
        endpoint_bound=2*np.sqrt(tau*g)*(w+step*tau*sig)+br
        assert max(exact_endpoint,exact_inverse)<=endpoint_bound+1e-11
        endpoint_rows.append({'step':step,'full_payload_endpoint_norm':exact_endpoint,
                              'inverse_endpoint_norm':exact_inverse,'analytic_bound':endpoint_bound})
    eta=min(2,8*np.sin(np.pi/(2*(L+1))))
    assert clock_error<=8*ec+1e-10 and total_error<=8*ec+2*eta+1e-10
    return {'tau':tau,'horizon':T,'clock_dimension':M,'payload_dimension':D,
            'two_observation_joint_clock_error':clock_error,'joint_clock_battery_error':total_error,
            'clock_bound':8*ec,'combined_bound':8*ec+2*eta,'trace_sums':trace_sums,
            'full_operator_endpoint_checks':endpoint_rows,
            'near_identity_norm':near,'cyclic_wrap_energy_defect':wrap_defect,
            'dimensionless_clock_spectrum_error':clock_spectrum_error,
            'maximum_lift_composition_residual':max(composition),'elapsed_seconds':time.monotonic()-started,
            'scope':'Finite adaptive classical-flag readouts with a reference-entangled input and conditional system flip; all actual clock/battery correlations are propagated.'}

def main():
    HERE.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();out={'packet':packet_controls(),'marked_bin':marked_bin_controls()}
    out['process']=[]
    for tau in (.001,.0001):
        row=process_control(tau);out['process'].append(row);print(json.dumps(row),flush=True)
    out['elapsed_seconds']=time.monotonic()-started
    out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out['scope']='Root finite consistency controls; not an independent proof or a uniform-resource certificate.'
    (HERE/'PROCESS_CONTROL_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
    print('TOTAL: PASS=4 FAIL=0',flush=True)
if __name__=='__main__':main()
