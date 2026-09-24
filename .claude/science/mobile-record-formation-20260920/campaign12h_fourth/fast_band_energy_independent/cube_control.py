#!/usr/bin/env python3
"""Independent primitive cube paths and complete spin-one no-event control.

No existing campaign builder is imported. Zero-energy N=8 recycling makes
the no-event energy exactly the full-generator energy after a first birth.
"""
from collections import defaultdict
from pathlib import Path
import hashlib,json,itertools,math,sys,time
import numpy as np
from scipy.sparse import csr_matrix,diags
from scipy.sparse.linalg import eigsh,expm_multiply

HERE=Path(__file__).resolve().parent
A=(0,3,5,6);B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
OMEGA=(tuple(int(i in A) for i in range(8)),(0,)*12)


def plus(out,key,value):
    out[key]+=value
    if not out[key]:del out[key]


def hop(v,adjoint=False,center=None):
    out=defaultdict(int)
    for (q,E),amp in v.items():
        for ei,(a,b) in enumerate(EDGES):
            if center is not None and a!=center:continue
            legal=(q[a]==0 and q[b]!=0) if adjoint else (q[a]!=0 and q[b]==0)
            if not legal:continue
            qq=list(q);ee=list(E)
            if adjoint:qq[a]=q[b];qq[b]=0;ee[ei]+=q[b]
            else:qq[b]=q[a];qq[a]=0;ee[ei]-=q[a]
            plus(out,(tuple(qq),tuple(ee)),amp)
    return dict(out)


def birth(v,edge,sigma):
    a,b=EDGES[edge];out=defaultdict(int)
    for (q,E),amp in v.items():
        if q[a] or q[b]:continue
        qq=list(q);ee=list(E);qq[a]=sigma;qq[b]=-sigma;ee[edge]+=sigma
        plus(out,(tuple(qq),tuple(ee)),amp)
    return dict(out)


def add(v,w,sign=1):
    out=defaultdict(int,v)
    for key,value in w.items():plus(out,key,sign*value)
    return dict(out)


def D1(v):return add(hop(hop(v,True)),hop(hop(v),True),-1)


def grade(word):return sum(word[0][a]==0 for a in A)


def gamma(word):
    q,E=word
    return 2*sum(q[a]==q[b]==0 for a,b in EDGES)


def norm2(v):return sum(x*x for x in v.values())


def certificate(v):
    return [{'q':list(q),'E':list(E),'coefficient':amp} for (q,E),amp in sorted(v.items())]


def exact_rotor_paths():
    rows=[];certs={}
    for edge,(a,b) in enumerate(EDGES):
        base=hop({OMEGA:1});marks={str(s):birth(base,edge,s) for s in (1,-1)}
        marks['coherent']=add(marks['1'],marks['-1'])
        for mark,v in marks.items():
            R={k:-x for k,x in hop(v,center=a).items()}
            # Direct expression j F^2/2 - F j F, keeping the half denominator.
            f2=hop(base)
            j2=add(birth(f2,edge,1),birth(f2,edge,-1)) if mark=='coherent' else birth(f2,edge,int(mark))
            direct={k:x/2 for k,x in j2.items()}
            assert all(float(x).is_integer() for x in direct.values())
            direct={k:int(x) for k,x in direct.items()}
            assert add(direct,hop(v),-1)==R
            dR=D1(R);ddR=D1(dR)
            bnorm=norm2(v);rnorm=norm2(R)
            assert all(grade(k)==1 for k in R) and all(gamma(k)==0 for k in R)
            assert all(gamma(k)==2 for k in dR)
            g=sum(gamma(k)*x*x for k,x in dR.items())
            assert g==24*rnorm
            assert sum(R.get(k,0)*x for k,x in dR.items())==0
            assert sum(R.get(k,0)*x for k,x in ddR.items())==norm2(dR)
            rows.append({'edge':[a,b],'instrument_mark':mark,'b':bnorm,'R_norm_squared':rnorm,'leading_c':rnorm/bnorm,'R_terms':len(R),'D1_R_terms':len(dR),'D1_R_norm_squared':norm2(dR),'Gamma_R_norm_squared':0,'D1_R_Gamma_expectation':g,'normalized_cubic_form':g/bnorm,'relative_cubic_coefficient_without_kappa_delta_squared':g/(3*rnorm)})
            if edge==0:certs[mark]={'B':certificate(v),'R':certificate(R),'D1_R':certificate(dR),'D1_squared_R':certificate(ddR)}
    return {'edges_A_to_B':[list(e) for e in EDGES],'rows':rows,'selected_edge_01_full_path_certificates':certs,'arithmetic':'Integer path sums; every equality assertion exact. The displayed half denominator is converted only after its integer property is checked.'}


def complete_spin_one():
    inc=np.zeros((12,8),np.int8)
    for i,(a,b) in enumerate(EDGES):inc[i,a]=1;inc[i,b]=-1
    allE=np.indices((3,)*12,dtype=np.int8).reshape(12,-1).T-1
    allq=allE@inc+np.array([int(i in A) for i in range(8)],np.int8)
    valid=(np.abs(allq)<=1).all(axis=1);number=(allq*allq).sum(axis=1)
    models={}
    for N in (4,6,8):
        select=valid&(number==N);fields=allE[select].copy();charges=allq[select].copy()
        index={tuple(int(x) for x in E):i for i,E in enumerate(fields)};n=len(fields)
        W=(charges[:,A]==0).sum(axis=1)
        rows=[];cols=[];delta=np.zeros(n);loss=np.zeros(n)
        for i,(q,E) in enumerate(zip(charges,fields)):
            for e,(a,b) in enumerate(EDGES):
                if q[a]!=0 and q[b]==0:
                    weight=1-int(E[e])*(int(E[e])-int(q[a]))/2
                    assert weight in (0,1)
                    if weight:
                        ee=E.copy();ee[e]-=q[a];dest=index[tuple(int(x) for x in ee)]
                        rows.append(dest);cols.append(i)
                    if W[i]==0:delta[i]+=1-weight
                if q[a]==q[b]==0:loss[i]+=2-int(E[e])**2
        F=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n))
        P=diags((W==0).astype(float));C=P@(F.T@F)@P+diags(delta)
        if N==8:assert F.nnz==C.nnz==0 and np.max(W)==0 and np.max(loss)==0
        if N==6:assert np.all(loss[W!=1]==0)
        models[N]={'E':fields,'q':charges,'index':index,'W':W,'F':F,'C':C,'loss':loss}
    return models


def jump_matrix(m4,m6,sigma):
    rows=[];cols=[]
    for i,(q,E) in enumerate(zip(m4['q'],m4['E'])):
        if q[0] or q[1]:continue
        weight=1-int(E[0])*(int(E[0])+sigma)/2
        assert weight in (0,1)
        if not weight:continue
        ee=E.copy();ee[0]+=sigma;rows.append(m6['index'][tuple(int(x) for x in ee)]);cols.append(i)
    return csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(m6['E']),len(m4['E'])))


def matrix_control(models):
    m4,m6=models[4],models[6];n4=len(m4['E']);n6=len(m6['E'])
    p4=np.flatnonzero(m4['W']==0);p1=np.flatnonzero(m6['W']==1)
    omega_index=m4['index'][(0,)*12];omega_local=int(np.flatnonzero(p4==omega_index)[0])
    F=m6['F'];D=(F@F.T-F.T@F)[p1,:][:,p1].tocsr()
    Gamma=diags(m6['loss'][p1]);delta=1.;kappa=.7;times=np.linspace(0,.06,4)
    limiting=-1j*delta*D-(kappa/2)*Gamma
    rcols=[];names=['1','-1','coherent']
    bbase=hop({OMEGA:1});vplus=birth(bbase,0,1);vminus=birth(bbase,0,-1)
    markdict={'1':vplus,'-1':vminus,'coherent':add(vplus,vminus)}
    full_to_small={int(i):j for j,i in enumerate(p1)}
    for name in names:
        Bv=markdict[name];R=hop(Bv,center=0);r=np.zeros(len(p1))
        for (q,E),amp in R.items():r[full_to_small[m6['index'][E]]]=-amp/math.sqrt(norm2(Bv))
        rcols.append(r)
    R=np.stack(rcols,axis=1)
    effective=expm_multiply(limiting,R,start=0,stop=times[-1],num=len(times),traceA=limiting.diagonal().sum())
    predicted=delta*np.sum(abs(effective)**2,axis=1)
    assert np.max(np.abs(m6['loss'][p1,None]*R))==0
    localforms=np.sum(abs(D@R)**2*m6['loss'][p1,None],axis=0)
    jp=jump_matrix(m4,m6,1);jm=jump_matrix(m4,m6,-1);marks=[jp,jm,jp+jm]
    rows=[]
    for epsilon in (.025,.0175,.0125):
        h4=diags(m4['W'])-epsilon*(m4['F']+m4['F'].T)+epsilon**2*m4['C']
        vals,V=eigsh(h4,k=len(p4),sigma=-.01,which='LM',tol=2e-12)
        eigerr=float(np.linalg.norm(h4@V-V*vals));ortherr=float(np.linalg.norm(V.T@V-np.eye(len(p4))))
        assert max(abs(vals))<.1 and eigerr<2e-10 and ortherr<2e-10
        VP=V[p4,:];gram=VP@VP.T;w,q=np.linalg.eigh(gram)
        assert w.min()>.8
        coeff=(q/np.sqrt(w))@q.T@np.eye(len(p4))[:,omega_local]
        dressed=V@(VP.T@coeff)
        assert abs(np.linalg.norm(dressed)-1)<2e-11
        outputs=[];weights=[]
        for j in marks:
            x=j@dressed;weights.append(float(np.vdot(x,x).real));outputs.append(x/np.linalg.norm(x))
        X=np.stack(outputs,axis=1)
        h6=diags(m6['W'])-epsilon*(F+F.T)+epsilon**2*m6['C']
        generator=-1j*delta/epsilon**2*h6-(kappa/2)*diags(m6['loss'])
        path=expm_multiply(generator,X,start=0,stop=times[-1],num=len(times),traceA=generator.diagonal().sum())
        energies=np.array([delta/epsilon**2*np.sum(x.conj()*(h6@x),axis=0).real for x in path])
        survival=np.sum(abs(path)**2,axis=1)
        assert np.max(survival)<=1+2e-11
        residual=np.max(abs(energies-predicted))
        assert residual<.1
        rows.append({'epsilon':epsilon,'spin':1,'not_a_joint_large_spin_sequence':True,'low_band_dimension':len(p4),'canonical_eigensystem_residual':eigerr,'canonical_eigensystem_orthogonality_error':ortherr,'marked_initial_weights':weights,'tau_grid':times.tolist(),'epsilon_squared_full_energy_by_time_and_mark':energies.tolist(),'predicted_spin_one_fast_energy_by_time_and_mark':predicted.tolist(),'future_birth_probabilities_by_time_and_mark':(1-survival).tolist(),'max_fast_energy_error':float(residual),'max_error_divided_by_epsilon_squared':float(residual/epsilon**2)})
    assert rows[-1]['max_fast_energy_error']<rows[0]['max_fast_energy_error']
    return {'complete_basis_dimensions':{str(N):len(m['E']) for N,m in models.items()},'W_dimensions':{str(N):{str(w):int(np.sum(m['W']==w)) for w in np.unique(m['W'])} for N,m in models.items()},'primitive_matrix_nonzeros':{str(N):{'F':m['F'].nnz,'compensation':m['C'].nnz} for N,m in models.items()},'N8_Hamiltonian_and_jumps_exactly_zero':True,'Gamma_only_in_W1':True,'finite_spin_one_normalized_cubic_forms':localforms.tolist(),'mark_order':names,'rows':rows,'scope':'Complete physical spin-one finite-epsilon generator checks the perturbation reduction. Joint spin/epsilon limit is proved separately, not inferred from these rows.'}


if __name__=='__main__':
    t=time.monotonic();paths=exact_rotor_paths();print('Exact primitive rotor paths complete.',flush=True)
    models=complete_spin_one();print('Complete spin-one physical matrices built.',flush=True)
    matrix=matrix_control(models)
    result={'exact_paths':paths,'complete_finite_spin_generator':matrix,'all_assertions_passed':True,'elapsed_seconds':time.monotonic()-t,'builder_imports':[]}
    (HERE/'CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'all_assertions_passed':True,'primitive_mark_cases':len(paths['rows']),'basis_dimensions':matrix['complete_basis_dimensions'],'epsilon_rows':len(matrix['rows']),'max_error_over_epsilon_squared':max(x['max_error_divided_by_epsilon_squared'] for x in matrix['rows']),'finite_spin_one_cubic_forms':matrix['finite_spin_one_normalized_cubic_forms'],'elapsed_seconds':result['elapsed_seconds']},indent=2))
