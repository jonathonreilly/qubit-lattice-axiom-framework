#!/usr/bin/env python3
"""Distinct finite checks of transfer normalization, response, and rotor tails.

No finite truncation checks the volume-uniform susceptibility target. The
positive finite matrices here challenge exact identities in the written proof.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_FILES = []
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.linalg import eigh,expm,eigh_tridiagonal
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import eigsh,LinearOperator,cg

def transfer_checks():
    N=65;g=.6;T=.4;n=np.arange(-(N//2),N//2+1);zero=N//2
    shift=np.zeros((N,N))
    for j in range(N):shift[(j+1)%N,j]=1
    L=(shift+shift.T-2*np.eye(N))/(2*g*g)
    K=np.diag(2*g*g*n*n);H=K-L;exact=expm(-T*H);rows=[]
    root_errors=[]
    for M in [16,32,64,128]:
        delta=T/M;y=delta/(2*g*g);assert y<=1/8
        jumps=np.arange(-12,13);weights=y**(jumps*jumps);weights/=sum(weights)
        B=sum(w*np.linalg.matrix_power(shift,int(k)%N) for k,w in zip(jumps,weights))
        assert np.max(abs(B.sum(axis=0)-1))<2e-15
        vals,vecs=eigh(B);assert min(vals)>0
        eigroot=(vecs*np.sqrt(vals))@vecs.T
        symbol=np.fft.fft(B[:,0]).real;assert min(symbol)>0
        root_coeff=np.fft.ifft(np.sqrt(symbol)).real
        sqrtB=root_coeff[(np.arange(N)[:,None]-np.arange(N)[None,:])%N]
        root_residual=float(np.linalg.norm(sqrtB@sqrtB-B,2))
        eigroot_residual=float(np.linalg.norm(eigroot@eigroot-B,2))
        assert root_residual<3e-15
        Q=diags(np.exp(-delta*np.diag(K))).toarray();qh=np.sqrt(Q)
        original=sqrtB@Q@sqrtB;alternative=qh@B@qh
        v=sqrtB[:,zero]
        lhs=float(v@np.linalg.matrix_power(original,M-1)@v)
        rhs=float(np.linalg.matrix_power(alternative,M)[zero,zero])
        assert abs(lhs-rhs)<2e-13
        missing_endpoints=float(np.linalg.matrix_power(original,M-1)[zero,zero])
        assert abs(missing_endpoints-rhs)>1e-5
        one_step=expm(delta*L)
        jump_error=float(np.linalg.norm(B-one_step,2));bound=24*y*y
        assert jump_error<=bound
        poisson=qh@one_step@qh
        actualM=np.linalg.matrix_power(alternative,M)
        poissonM=np.linalg.matrix_power(poisson,M)
        block_error=float(np.linalg.norm(actualM-poissonM,2))
        assert block_error<=M*bound
        err=float(np.linalg.norm(actualM[:,zero]-exact[:,zero]))
        root_errors.append(err)
        rows.append({'slices':M,'amplitude_identity_error':abs(lhs-rhs),'structured_square_root_residual':root_residual,'generic_eigendecomposition_square_root_residual':eigroot_residual,'missing_endpoint_error':abs(missing_endpoints-rhs),'minimum_sqrtB_entry':float(sqrtB.min()),'one_step_jump_operator_error':jump_error,'one_step_sufficient_bound':bound,'coupled_block_operator_error':block_error,'block_sufficient_bound':M*bound,'Hamiltonian_boundary_vector_error':err})
    assert min(r['minimum_sqrtB_entry'] for r in rows)<-1e-5
    assert root_errors[-1]<root_errors[0]/5
    return {'cyclic_electric_regulator':N,'g':g,'T':T,'rows':rows}

def actual_two_square_complex():
    vertices=list(itertools.product(range(3),range(2)));vset=set(vertices);edges=[];edge_index={}
    def step(x,a):
        out=list(x);out[a]+=1;return tuple(out)
    for x in vertices:
        for a in range(2):
            if step(x,a) in vset:edge_index[x,a]=len(edges);edges.append((x,a))
    D=np.zeros((len(vertices),len(edges)),dtype=int);vid={x:j for j,x in enumerate(vertices)}
    for j,(x,a) in enumerate(edges):D[vid[x],j]=-1;D[vid[step(x,a)],j]=1
    C=np.zeros((2,len(edges)),dtype=int)
    for j,x in enumerate([(0,0),(1,0)]):
        for key,s in [((x,0),1),((step(x,0),1),1),((step(x,1),0),-1),((x,1),-1)]:C[j,edge_index[key]]=s
    assert np.array_equal(D@C.T,np.zeros((len(vertices),2),dtype=int))
    assert np.array_equal(C@C.T,np.array([[4,-1],[-1,4]]))
    return D,C

def rotor_matrix(S,g,G):
    states=np.array(list(itertools.product(range(-S,S+1),repeat=2)),dtype=float)
    index={tuple(n.astype(int)):j for j,n in enumerate(states)};size=len(states)
    row=[];col=[];dat=[];mag=[]
    for p in range(2):
        rr=[];cc=[]
        for j,n in enumerate(states):
            for sign in [-1,1]:
                nn=n.copy();nn[p]+=sign;i=index.get(tuple(nn.astype(int)))
                if i is not None:rr.append(i);cc.append(j)
        cosine=coo_matrix((np.full(len(rr),.5),(rr,cc)),shape=(size,size)).tocsr()
        mag.append(cosine)
    diag=.5*g*g*np.einsum('ni,ij,nj->n',states,G,states)+2/(g*g)
    H=diags(diag)-sum(mag)/(g*g)
    return states,H.tocsr(),mag

def response_checks():
    D,C=actual_two_square_complex();G=C@C.T;rows=[];coarse={}
    for S in [8,12]:
        for g in [.4,.6,.9,1.4,3.]:
            states,H,cosines=rotor_matrix(S,g,G);size=len(states)
            values,vectors=eigsh(H,k=8,which='SA',tol=2e-13,v0=np.ones(size));order=np.argsort(values);values=values[order];vectors=vectors[:,order]
            psi=vectors[:,0];psi*=np.sign(psi[states.tolist().index([0.,0.])]);E0=float(values[0])
            residual=float(np.linalg.norm(H@psi-E0*psi));assert residual<2e-10
            A0=H-diags(np.full(size,E0))
            op=LinearOperator(H.shape,matvec=lambda x:A0@x+psi*np.dot(psi,x))
            for s in [np.array([1.,-1.]),np.array([.7,.2])]:
                f=C.T@np.linalg.solve(G,s);norm2=float(f@f);obs=states@s
                v=obs*psi;v-=psi*np.dot(psi,v)
                inverse,info=cg(op,v,rtol=2e-12,atol=1e-15,maxiter=8000);assert info==0
                mminus=float(v@inverse);mone=float(v@(A0@v));chi=2*mminus
                cosmeans=np.array([psi@(co@psi) for co in cosines])
                comm=float(np.dot(s*s,cosmeans)/(2*g*g))
                assert abs(mone-comm)<2e-10
                eta=g*g*chi/norm2;rho=1-eta
                assert -.000001<rho<1 and 0<eta<1.000001
                bound=math.sqrt(mone/mminus)
                visible=[float(values[j]-E0) for j in range(1,len(values)) if abs(np.dot(v,vectors[:,j]))>1e-8]
                assert visible and min(visible)<=bound+1e-8
                target=g*g*norm2-g**4*chi;fd=[]
                for t in [.006,.003]:
                    ht=H+diags(-g*g*t*obs+.5*g*g*t*t*norm2)
                    et=float(eigsh(ht,k=1,which='SA',tol=5e-14,v0=psi,return_eigenvectors=False)[0])
                    fd.append(2*(et-E0)/(t*t))
                assert abs(fd[-1]-target)<2e-5
                key=(g,tuple(s));row={'cutoff':S,'g':g,'curl_test':s.tolist(),'ground_energy':E0,'ground_residual':residual,'m_minus_1':mminus,'m_1':mone,'double_commutator_error':abs(mone-comm),'eta':eta,'rho':rho,'offset_curvature_spectral':target,'offset_curvature_finite_difference':fd,'curvature_difference':abs(fd[-1]-target),'visible_lowest_energy':min(visible),'spectral_ratio_energy_bound':bound,'geometric_energy_bound':math.sqrt(float(s@s)/(eta*norm2))}
                if S==8:coarse[key]=(E0,chi)
                else:
                    de=abs(E0-coarse[key][0]);dc=abs(chi-coarse[key][1]);row['cutoff_energy_change']=de;row['cutoff_chi_change']=dc
                    assert de<1e-8 and dc<1e-7
                rows.append(row)
    return {'incidence_shape':list(D.shape),'cycle_gram':G.tolist(),'rows':rows}

def factorial_tail_check():
    mp.mp.dps=90;g=mp.mpf('.7');a=1/(2*g*g);cutoff=160
    def ratios(energy):
        ratios=[mp.mpf(0)]*(cutoff+2)
        for n in range(cutoff,0,-1):ratios[n]=a/(2*g*g*n*n+1/(g*g)-energy-a*ratios[n+1])
        return ratios
    n=np.arange(-30,31,dtype=float)
    approx=eigh_tridiagonal(2*.7**2*n*n+1/.7**2,np.full(len(n)-1,-1/(2*.7**2)),select='i',select_range=(0,0))[0][0]
    energy=mp.findroot(lambda e:1/(g*g)-e-2*a*ratios(e)[1],(mp.mpf(str(approx))-.001,mp.mpf(str(approx))+.001))
    r=ratios(energy);logpsi=mp.mpf(0);rows=[]
    for n in range(1,101):
        logpsi+=mp.log(r[n]);lower=-n*mp.log(4*g**4+2)-2*mp.loggamma(n+1)
        assert logpsi>=lower
        if n in [5,10,20,50,100]:rows.append({'n':n,'log_amplitude_relative_to_zero':str(logpsi),'log_factorial_lower_bound':str(lower),'minus_log_amplitude_over_n_squared':str(-logpsi/(n*n))})
    return {'g':str(g),'continued_fraction_cutoff':cutoff,'working_decimal_digits':mp.mp.dps,'ground_energy':str(energy),'rows':rows,'scope':'finite continued-fraction diagnostic; the all-n tail statement uses the exact positive recurrence'}

def run():
    start=time.time();transfer=transfer_checks();response=response_checks();tail=factorial_tail_check()
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'transfer':transfer,'electric_response':response,'ground_tail':tail,'seconds':time.time()-start},indent=2))

if __name__=='__main__':run()
