"""Finite-rate repeated gauge-record formation: full tree sectors and elimination."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/repeated_formation_check.py',)
from pathlib import Path
from itertools import product
from datetime import datetime,timezone
import json,hashlib,math
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
from scipy.linalg import eigvalsh
import sympy as sy

HERE=Path(__file__).resolve().parent

def tree_model(m=None):
    if m is None:
        label="two_A_path"
        nv=4;edges=[(0,1),(1,2),(2,3)];As={0,2}
    else:
        label=f"star_{m}"
        nv=m+1;edges=[(0,j) for j in range(1,nv)];As={0}
    bg=np.array([int(x in As) for x in range(nv)])
    incidence=np.zeros((nv,len(edges)),dtype=int)
    for e,(x,y) in enumerate(edges):incidence[x,e]=1;incidence[y,e]=-1
    # Invert the reduced tree incidence exactly; no effective model enters.
    inverse=np.array(sy.Matrix(incidence[1:,:]).inv(),dtype=int)
    states=[]
    for word in product((-1,0,1),repeat=nv):
        if sum(word)!=len(As):continue
        E=inverse@(np.array(word)-bg)[1:]
        assert np.array_equal(incidence@E,np.array(word)-bg)
        if max(abs(E),default=0)<=1:states.append((word,tuple(map(int,E))))
    ix={q:i for i,(q,E) in enumerate(states)};dim=len(states)
    T=np.zeros((dim,dim),dtype=int)
    N=np.diag([sum(q!=0 for q in word) for word,E in states])
    W=np.diag([sum(word[a]==0 for a in As) for word,E in states])
    NB=np.diag([sum(word[b]!=0 for b in range(nv) if b not in As) for word,E in states])
    resolved=[];coherent=[]
    for e,(x,y) in enumerate(edges):
        for col,(q,E) in enumerate(states):
            for src,dst,sgn in [(x,y,1),(y,x,-1)]:
                if q[src] and not q[dst]:
                    qq=list(q);qq[dst]=qq[src];qq[src]=0;qq=tuple(qq)
                    if qq not in ix:continue
                    outE=states[ix[qq]][1]
                    expected=list(E);expected[e]-=sgn*q[src]
                    assert tuple(expected)==outE
                    # Every allowed S=1 normalized shift between -1,0,+1 is one.
                    assert 1-(E[e]*(E[e]-sgn*q[src]))/2==1
                    T[ix[qq],col]-=1
        pair=[]
        for c in (-1,1):
            j=np.zeros((dim,dim),dtype=int)
            for col,(q,E) in enumerate(states):
                if q[x] or q[y]:continue
                qq=list(q);qq[x]=c;qq[y]=-c;qq=tuple(qq)
                if qq not in ix:continue
                outE=states[ix[qq]][1];expected=list(E);expected[e]+=c
                assert tuple(expected)==outE
                assert 1-(E[e]*(E[e]+c))/2==1
                j[ix[qq],col]=1
            pair.append(j);resolved.append(j)
        coherent.append(pair[0]+pair[1])
    assert np.array_equal(T,T.T)
    assert np.array_equal(N@T,T@N)
    assert np.array_equal(NB-W,N-len(As)*np.eye(dim,dtype=int))
    w=np.diag(W);p=np.where(w==0)[0];q1=np.where(w==1)[0];q2=np.where(w==2)[0]
    assert not np.any(T[np.ix_(p,p)])
    for i,j in zip(*np.nonzero(T)):assert abs(w[i]-w[j])==1
    for jumps in [coherent,resolved]:
        for j in jumps:
            assert np.array_equal(W@j-j@W,-j)
            assert np.array_equal(N@j-j@N,2*j)
            assert not np.any(j[:,p])
        loss=sum(j.T@j for j in jumps)
        assert np.array_equal(loss@W,W@loss)
    assert np.array_equal(sum(j.T@j for j in coherent),sum(j.T@j for j in resolved))
    if m is not None:
        assert np.array_equal(sum(j.T@j for j in coherent),2*(m*np.eye(dim)-N)@(W==1))
    initial=tuple(int(i in As) for i in range(nv))
    g=np.eye(dim)[:,ix[initial]]
    return dict(label=label,nv=nv,edges=edges,A_sites=sorted(As),states=states,
                T=T,N=N,W=W,NB=NB,p=p,q1=q1,q2=q2,
                coherent=coherent,resolved=resolved,g=g)

def superop(H,jumps):
    H=sp.csc_matrix(H);d=H.shape[0];I=sp.eye(d,format='csc')
    L=-1j*(sp.kron(I,H,format='csc')-sp.kron(H.T,I,format='csc'))
    for raw in jumps:
        j=sp.csc_matrix(raw);loss=j.conj().T@j
        L+=sp.kron(j.conj(),j,format='csc')-.5*sp.kron(I,loss,format='csc')-.5*sp.kron(loss.T,I,format='csc')
    return L.tocsc()

def effective(model,kind,delta=1.3,kappa=.7):
    T=model['T'];p=model['p'];q1=model['q1'];q2=model['q2'];jumps=model[kind]
    loss=sum(j.T@j for j in jumps)
    D1=delta*np.eye(len(q1))-0.5j*kappa*loss[np.ix_(q1,q1)]
    inv=np.linalg.inv(D1);A=T[np.ix_(q1,p)]
    B=A.T@inv@A
    H=-.5*delta**2*(B+B.conj().T)
    js=[math.sqrt(kappa)*delta*j[np.ix_(p,q1)]@inv@A for j in jumps]
    Y=-delta*inv@A
    if len(q2):
        D2=2*delta*np.eye(len(q2))-.5j*kappa*loss[np.ix_(q2,q2)]
        Y2=delta**2*np.linalg.solve(D2,T[np.ix_(q2,q1)]@inv@A)
    else:Y2=np.zeros((0,len(p)),dtype=complex)
    return H,js,Y,Y2

def exact_embedding_check(model,kind):
    """Exact rational identities on every P matrix unit for the smaller models."""
    delta=sy.Rational(13,10);kappa=sy.Rational(7,10)
    T=sy.Matrix(model['T']);W=sy.Matrix(model['W'])
    p=list(map(int,model['p']));q1=list(map(int,model['q1']));q2=list(map(int,model['q2']))
    jumps=list(map(sy.Matrix,model[kind]));dim=T.rows;np_=len(p)
    loss=sum((j.T*j for j in jumps),sy.zeros(dim))
    D1=delta*sy.eye(len(q1))-sy.I*kappa*loss.extract(q1,q1)/2
    A=T.extract(q1,p);Y=-delta*D1.inv()*A
    if q2:
        D2=2*delta*sy.eye(len(q2))-sy.I*kappa*loss.extract(q2,q2)/2
        Y2=delta**2*D2.inv()*T.extract(q2,q1)*D1.inv()*A
    else:Y2=sy.zeros(0,np_)
    B=A.T*D1.inv()*A
    H=-delta**2*(B+B.conjugate().T)/2
    # Absorb sqrt(kappa) by using kappa in the dissipator.
    js=[delta*j.extract(p,q1)*D1.inv()*A for j in jumps]
    def insert(a,rows,cols):
        out=sy.zeros(dim)
        for i,x in enumerate(rows):
            for j,y in enumerate(cols):out[x,y]=a[i,j]
        return out
    def D(r,j):return j*r*j.conjugate().T-(j.conjugate().T*j*r+r*j.conjugate().T*j)/2
    def L0(r):return -sy.I*delta*(W*r-r*W)+kappa*sum((D(r,j) for j in jumps),sy.zeros(dim))
    def L1(r):return -sy.I*delta*(T*r-r*T)
    def Le(x):return -sy.I*(H*x-x*H)+kappa*sum((D(x,j) for j in js),sy.zeros(np_))
    nonzero_twohole=False
    for i in range(np_):
        for j in range(np_):
            X=sy.zeros(np_);X[i,j]=1
            e0=insert(X,p,p)
            e1=insert(Y*X,q1,p)+insert(X*Y.conjugate().T,p,q1)
            z=Y*X*Y.conjugate().T
            e2=insert(z,q1,q1)+insert(Y2*X,q2,p)+insert(X*Y2.conjugate().T,p,q2)
            for R in [L0(e0),L0(e1)+L1(e0),L0(e2)+L1(e1)-insert(Le(X),p,p)]:
                assert all(sy.simplify(v)==0 for v in R)
            if q2 and any(sy.simplify(v)!=0 for v in L0(insert(z,q1,q1))+L1(e1)-insert(Le(X),p,p)):
                nonzero_twohole=True
    if q2:assert nonzero_twohole
    return {'model':model['label'],'instrument':kind,'P_matrix_units_checked':np_**2,
            'all_three_cancellation_identities_exact':True,
            'two_hole_coherence_correction_is_needed':nonzero_twohole}

def evolution(model,kind,eps):
    delta=1.3;kappa=.7
    p=model['p'];g=model['g'];dim=len(g)
    H,js,Y,Y2=effective(model,kind,delta,kappa)
    initial=np.outer(g,g);small=initial[np.ix_(p,p)]
    L=superop(delta*model['W']/eps**2+delta*model['T']/eps,
              [math.sqrt(kappa)*j/eps for j in model[kind]])
    E=superop(H,js)
    times=np.linspace(0,2,9)
    actual=expm_multiply(L,initial.reshape(-1,order='F'),start=0,stop=2,num=9,traceA=L.diagonal().sum())
    limit=expm_multiply(E,small.reshape(-1,order='F'),start=0,stop=2,num=9,traceA=E.diagonal().sum())
    ns=np.diag(model['N']);n0=int(g@model['N']@g);rows=[]
    for tt,aa,ee in zip(times,actual,limit):
        rho=aa.reshape((dim,dim),order='F')
        sig=ee.reshape((len(p),len(p)),order='F')
        target=np.zeros((dim,dim),dtype=complex);target[np.ix_(p,p)]=sig
        assert abs(np.trace(rho)-1)<2e-9 and np.linalg.norm(rho-rho.conj().T)<2e-9
        assert eigvalsh((rho+rho.conj().T)/2)[0]>-2e-9
        err=float(sum(abs(eigvalsh((rho-target+(rho-target).conj().T)/2))))
        probs={str((int(n)-n0)//2):float(np.trace(rho[np.ix_(ns==n,ns==n)]).real) for n in sorted(set(ns))}
        limprobs={str((int(n)-n0)//2):float(np.trace(target[np.ix_(ns==n,ns==n)]).real) for n in sorted(set(ns))}
        energy=float(np.trace((model['NB']+eps*model['T'])@rho).real)
        rows.append({'time':float(tt),'trace_norm_error':err,'error_over_epsilon':err/eps,
                     'actual_event_count_probabilities':probs,'effective_event_count_probabilities':limprobs,
                     'actual_energy_over_Delta':energy,
                     'effective_energy_over_Delta':float(np.trace((model['N']-len(model['A_sites'])*np.eye(dim))@target).real)})
    if model['label']=='star_4':
        assert rows[-1]['effective_event_count_probabilities']['2']>0
    gsmall=g[p];rate=float(np.real(sum(np.vdot(j@gsmall,j@gsmall) for j in js)))
    if model['label'].startswith('star_'):
        m=model['nv']-1;pred=2*m*(m-1)*kappa*delta**2/(delta**2+kappa**2*(m-1)**2)
        assert abs(rate-pred)<1e-12
    return {'model':model['label'],'instrument':kind,'epsilon':eps,'delta':delta,'kappa':kappa,
            'initial_effective_birth_rate':rate,'rows':rows}

def main():
    models=[tree_model(2),tree_model(4),tree_model(None)]
    inventories=[{'model':m['label'],'physical_dimension':len(m['states']),
                  'P_dimension':len(m['p']),'one_hole_dimension':len(m['q1']),
                  'two_hole_dimension':len(m['q2']),
                  'edges':m['edges'],'A_sites':m['A_sites'],
                  'physical_basis':[{'q':q,'E':e} for q,e in m['states']],
                  'integer_operator_identities_checked':True} for m in models]
    exact=[exact_embedding_check(m,kind) for m in (models[0],models[2]) for kind in ('coherent','resolved')]
    rows=[]
    for model in models[:2]:
        for kind in ('coherent','resolved'):
            for eps in (.2,.1,.05,.025):
                row=evolution(model,kind,eps);rows.append(row)
                print(json.dumps({'progress':model['label'],'instrument':kind,'epsilon':eps,'last_error':row['rows'][-1]['trace_norm_error']}),flush=True)
    source=Path(__file__).read_bytes()
    out={'created_utc':datetime.now(timezone.utc).isoformat(),
         'source_sha256':hashlib.sha256(source).hexdigest(),
         'inventories':inventories,'exact_map_checks':exact,'full_dynamics_checks':rows,
         'scope':'Complete finite gauge-constrained tree sectors. Exact rational embedding identities on two small models; full sparse Liouville evolutions for repeated births. No thermodynamic or photon claim.'}
    (HERE/'REPEATED_FORMATION_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'complete':True,'output':'REPEATED_FORMATION_RESULTS.json'}),flush=True)
if __name__=='__main__':main()
