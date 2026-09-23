"""Complete six-state gauge-record star: finite-rate renewed formation."""
from pathlib import Path
from itertools import product
from datetime import datetime,timezone
import hashlib,json,math
import numpy as np
import sympy as s
from scipy.linalg import expm,eigvalsh

HERE=Path(__file__).resolve().parent
WORDS=sorted(q for q in product((-1,0,1),repeat=3) if sum(q)==1)
INDEX={q:i for i,q in enumerate(WORDS)};DIM=len(WORDS)
assert DIM==6
N=np.diag([sum(v!=0 for v in q) for q in WORDS])
NB=np.diag([int(q[1]!=0)+int(q[2]!=0) for q in WORDS])
HOLE=np.diag([int(q[0]==0) for q in WORDS])
T=np.zeros((DIM,DIM));resolved=[]
for col,q in enumerate(WORDS):
    E=(-q[1],-q[2])
    assert E[0]+E[1]+1-q[0]==0
    for leaf in (1,2):
        for source,dest in [(0,leaf),(leaf,0)]:
            if q[source] and not q[dest]:
                qq=list(q);qq[dest]=qq[source];qq[source]=0
                ee=(-qq[1],-qq[2])
                sign=1 if source==0 else -1
                assert ee[leaf-1]-E[leaf-1]==-sign*q[source]
                T[INDEX[tuple(qq)],col]-=1
for leaf in (1,2):
    pair=[]
    for charge in (-1,1):
        j=np.zeros((DIM,DIM))
        for col,q in enumerate(WORDS):
            if not q[0] and not q[leaf]:
                qq=list(q);qq[0]=charge;qq[leaf]=-charge
                assert (-qq[leaf])-(-q[leaf])==charge
                j[INDEX[tuple(qq)],col]=1
        assert np.array_equal(N@j-j@N,2*j);pair.append(j);resolved.append(j)
assert np.array_equal(T,T.T) and np.array_equal(T@N,N@T)
assert np.array_equal(NB-HOLE,N-np.eye(DIM))
COHERENT=[resolved[0]+resolved[1],resolved[2]+resolved[3]]
g=np.eye(DIM)[:,INDEX[(1,0,0)]]
bright=(np.eye(DIM)[:,INDEX[(0,1,0)]]+np.eye(DIM)[:,INDEX[(0,0,1)]])/math.sqrt(2)
assert np.linalg.norm(T@g+math.sqrt(2)*bright)<1e-14
for jumps in [resolved,COHERENT]:
    assert np.array_equal(sum(j.T@j for j in jumps),2*HOLE)
    assert all(np.linalg.norm(j@g)==0 for j in jumps)
    assert all(np.linalg.norm(j@j2)==0 for j in jumps for j2 in jumps)

def symbolic_mean():
    delta,beta,r=s.symbols('Delta beta r',positive=True)
    x,z,u,v=s.symbols('x z u v',real=True)
    h=s.Matrix([[0,-r],[-r,delta-s.I*beta]])
    X=s.Matrix([[x,u+s.I*v],[u-s.I*v,z]])
    eq=s.I*(s.conjugate(h.T)*X-X*h)+s.eye(2)
    equations=[s.re(w) for w in eq]+[s.im(w) for w in eq]
    sol=s.solve(equations,[x,z,u,v],dict=True)[0]
    expected=(delta**2+beta**2+2*r**2)/(2*beta*r**2)
    assert s.simplify(sol[x]-expected)==0
    return {'survival_integral_matrix':str(s.simplify(X.subs(sol))),
            'central_start_mean':str(s.factor(sol[x])),
            'record_parameters':'Delta^2/(4 beta t^2)+beta/(4 t^2)+1/beta'}

def Lsuper(H,jumps,beta):
    I=np.eye(DIM)
    L=-1j*(np.kron(I,H)-np.kron(H.T,I))
    for j in jumps:
        loss=j.T@j
        L+=beta*(np.kron(j,j)-.5*np.kron(I,loss)-.5*np.kron(loss.T,I))
    return L

def sigma_of(jumps):
    return sum(np.outer(j@bright,j@bright) for j in jumps)/2

def exact(eps,delta,kappa,tau):
    Delta=delta/eps**4;hop=eps*Delta;beta=kappa/eps**2
    z=Delta-1j*beta;r=math.sqrt(2)*hop
    D=np.sqrt(z*z+4*r*r)
    assert D.real>0
    slow=-2*r*r/(z+D);fast=z-slow
    es=np.exp(-1j*slow*tau);ef=np.exp(-1j*fast*tau)
    a=(fast*es-slow*ef)/D;b=r*(es-ef)/D
    surv=abs(a)**2+abs(b)**2
    gamma=-2*slow.imag;eta=-2*fast.imag
    pref=2*beta*r*r/abs(D)**2
    assert gamma>0 and eta>0
    l1=(abs(pref-4*kappa)+abs(gamma-4*kappa))/gamma+pref/eta+2*pref/beta
    return a,b,float(surv),{'slow_decay_rate':float(gamma),'fast_decay_rate':float(eta),
             'event_prefactor':float(pref),'all_time_event_density_L1_bound':float(l1),
             'bound_over_epsilon_squared':float(l1/eps**2),
             'mean_first_event':1/(4*kappa)+eps**2/kappa+kappa*eps**4/(4*delta**2)}

def run(eps,kind):
    delta=1.3;kappa=.7
    Delta=delta/eps**4;hop=eps*Delta;beta=kappa/eps**2
    jumps=COHERENT if kind=='coherent_per_edge' else resolved
    sigma=sigma_of(jumps);H=Delta*HOLE+hop*T;original=Delta*NB+hop*T
    L=Lsuper(H,jumps,beta);rho0=np.outer(g,g)
    rows=[]
    for tau in [0.,.001,.02,.2,.5,1.,2.]:
        rho=(expm(tau*L)@rho0.reshape(-1,order='F')).reshape((DIM,DIM),order='F')
        a,b,surv,clock=exact(eps,delta,kappa,tau)
        psi=a*g+b*bright
        analytic=np.outer(psi,psi.conj())+(1-surv)*sigma
        match=float(np.linalg.norm(rho-analytic,ord='fro'))
        assert match<3e-8 and abs(np.trace(rho)-1)<3e-8
        assert np.linalg.norm(rho-rho.conj().T)<3e-8 and eigvalsh((rho+rho.conj().T)/2)[0]>-3e-8
        s0=math.exp(-4*kappa*tau)
        target=s0*rho0+(1-s0)*sigma
        err=float(np.sum(np.abs(eigvalsh((rho-target+(rho-target).conj().T)/2))))
        exact_error=math.sqrt((surv-s0)**2+4*s0*abs(b)**2)+abs(surv-s0)
        assert abs(err-exact_error)<5e-8
        energy=float(np.trace(original@rho).real/Delta)
        leading_energy=2*(1-s0)
        energy_bound=abs(b)**2+2*math.sqrt(2)*eps*abs(a*b)+2*abs(surv-s0)
        assert abs(energy-leading_energy)<=energy_bound+1e-7
        rows.append({'time':tau,'full_Liouville_vs_exact_bright_error':match,
                     'no_event_probability':surv,'limiting_no_event_probability':s0,
                     'count_probability_error':abs(surv-s0),
                     'full_trace_norm_error':err,'closed_form_trace_norm_error':exact_error,
                     'trace_norm_error_over_epsilon':err/eps,
                     'original_energy_over_Delta':energy,'limiting_energy_over_Delta':leading_energy,
                     'energy_deviation_bound':float(energy_bound)})
    return {'epsilon':eps,'delta':delta,'kappa':kappa,'Delta':Delta,'hop':hop,'beta':beta,
            'instrument':kind,'clock':clock,'rows':rows}

def main():
    inds=[INDEX[(-1,1,1)],INDEX[(1,-1,1)],INDEX[(1,1,-1)]]
    sigmas={}
    for name,jumps in [('coherent_per_edge',COHERENT),('resolved_charge',resolved)]:
        sig=sigma_of(jumps)
        sigmas[name]={'final_density_negative_site_basis':sig[np.ix_(inds,inds)].tolist(),
                      'purity':float(np.trace(sig@sig)),
                      'eigenvalues':eigvalsh(sig[np.ix_(inds,inds)]).tolist()}
    source=Path(__file__).read_bytes()
    out={'created_utc':datetime.now(timezone.utc).isoformat(),
         'source':{'path':str(Path(__file__).resolve()),'bytes':len(source),'sha256':hashlib.sha256(source).hexdigest()},
         'complete_physical_basis':[{'q':q,'E':[-q[1],-q[2]]} for q in WORDS],
         'exact_integer_operator_identities':'Gauss shifts, permanent-charge hops, number-raising jumps, common loss 2 HOLE, absorbing output and H-Hprime=Delta(N-1) checked.',
         'symbolic_clock':symbolic_mean(),'output_instruments':sigmas,
         'scaling_controls':[run(eps,kind) for kind in ['coherent_per_edge','resolved_charge']
                             for eps in [.1,.075,.05,.025]],
         'scope':'Complete finite star, an exact exponential output-law limit with diverging microscopic scales. No cubic photon or finite-resource reservoir theorem.'}
    text=json.dumps(out,indent=2)+'\n';(HERE/'FINITE_RATE_FORMATION_RESULTS.json').write_text(text);print(text,end='')
if __name__=='__main__':main()
