#!/usr/bin/env python3
"""Direct exact 14^4 rate sums and fixed mixed-density compatibility witness."""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,itertools,json,platform
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
N=12;DEN=896
DELTAS=[tuple(sign*int(j==i) for j in range(3)) for i in range(3) for sign in (1,-1)]
E=np.zeros((14,3),dtype=np.int64);B=np.zeros((14,3),dtype=np.int64)
for i in range(3):E[2*i,i]=1;E[2*i+1,i]=-1
B[6:]=np.array(list(itertools.product((-1,1),repeat=3)),dtype=np.int64)
COS2=np.array([2,1,-1,-2,-1,1],dtype=np.int64)

def pnum(x,primed):
    p=np.full(14,64,dtype=np.int64)
    p[6:]+=7*B[6:,2]*int(COS2[x%6])
    if primed:p[2:4]+=16;p[0:2]-=16
    assert p.sum()==DEN and p.min()>0
    return p

def states():
    matrices=[]
    for a in range(14):
        w=s.Matrix([s.Rational(int(E[a,i]),8)+s.I*s.Rational(int(B[a,i]),12) for i in range(3)])
        rho=s.diag(s.Rational(1,2),s.Rational(1,6),s.Rational(1,6),s.Rational(1,6))
        rho[1:4,0]=w;rho[0,1:4]=w.conjugate().T
        assert rho==rho.conjugate().T and s.trace(rho)==1
        schur=s.Rational(1,2)-6*(w.conjugate().T*w)[0]
        assert schur>0
        matrices.append(rho)
    return matrices

def mixture(p,matrices):
    return sum((s.Rational(int(p[a]),DEN)*matrices[a] for a in range(14)),s.zeros(4))

def encoding_checks(matrices):
    A2=s.zeros(4);A2[0,2]=A2[2,0]=1
    rows=[]
    for x in range(N):
        p,q=pnum(x,False),pnum(x,True);r=mixture(p,matrices);rp=mixture(q,matrices)
        assert r==rp
        assert (p@E==q@E).all() and (p@B==q@B).all()
        assert p[2]+p[3]==128 and q[2]+q[3]==160
        assert s.trace(r*A2)==s.Rational(1,4)*s.Rational(int((p@E)[1]),DEN)==0
        expected=s.diag(s.Rational(1,2),s.Rational(1,6),s.Rational(1,6),s.Rational(1,6))
        expected[3,0]=s.I*s.Rational(int(COS2[x%6]),192)
        expected[0,3]=-s.I*s.Rational(int(COS2[x%6]),192)
        assert r==expected
        rows.append({'x':x,'twice_cosine':int(COS2[x%6]),'D2':str(F(128,DEN)),
                     'primed_D2':str(F(160,DEN)),'Y3':str(F(int((p@B)[2]),DEN)),
                     'exact_local_density_equality':True})
    r1=mixture(pnum(1,False),matrices);r2=mixture(pnum(2,False),matrices)
    q1=mixture(pnum(1,True),matrices);q2=mixture(pnum(2,True),matrices)
    assert s.kronecker_product(r1,r2)==s.kronecker_product(q1,q2)
    return A2,{'q':'1/2','r':'1/6','lambda_A':'1/8','lambda_B':'1/12',
               'axis_Schur_complement':'13/32','corner_Schur_complement':'3/8',
               'minimum_profile_probability':str(min(F(int(z),DEN) for x in range(N) for prime in (False,True) for z in pnum(x,prime))),
               'rows':rows,'two_pair_tensor_dimension':16,'exact_two_pair_product_equality':True,
               'full_product_statement':'Factorwise equality proves equality for all 864 independent pair factors. The 4^864 matrix is not materialized.'}

def exact_currents():
    denominator=40*DEN**4
    # Exact accumulation remains below int64 limits even before cancellations.
    assert 14**4*80**4*42<2**63
    out={};rate_ranges=[];contexts=[];checks=0
    u=np.array([1,1,0])
    for delta0 in DELTAS:
        delta=np.array(delta0);a=delta-np.array([1,0,0])
        if not a.any():continue
        stencil=[tuple((u+k*a)%N) for k in (-1,0,1,2)]
        assert len(set(stencil))==4 and all(sum(x)%2==0 for x in stencil)
        contexts.append({'delta':delta0,'displacement':a.tolist(),'actual_four_contexts':stencil})
        # S=Sn/2; h=hn/2; the actual rate is (22+5 hn)/40.
        Sn=np.einsum('abi,i->ab',np.cross(E[:,None,:],B[None,:,:])+np.cross(E[None,:,:],B[:,None,:]),delta)
        hn=Sn[:,:,None,None]+Sn[None,:,None,:]-Sn[:,None,:,None]-Sn[None,None,:,:]
        rate_num=22+5*hn
        assert rate_num.min()>=2 and rate_num.max()<=42
        rate_ranges.append({'delta':delta0,'minimum_rate':str(F(int(rate_num.min()),40)),
                            'maximum_rate':str(F(int(rate_num.max()),40))})
        for primed in (False,True):
            for x in range(N):
                pl,pu,pw,pr=[pnum(x+k*int(a[0]),primed) for k in (-1,0,1,2)]
                weights=pl[:,None,None,None]*pu[None,:,None,None]*pw[None,None,:,None]*pr[None,None,None,:]
                T=weights*rate_num
                # The endpoint indicator difference is formed after direct summation of all contexts.
                jn=T.sum(axis=(0,2,3))-T.sum(axis=(0,1,3))
                assert int(jn.sum())==0
                # Separate contraction of the four-product formula, with the same common denominator.
                sn=Sn@(pl+pr);mu_u=int(pu@sn);mu_w=int(pw@sn)
                contracted=22*DEN**3*(pu-pw)+5*DEN**2*(pu+pw)*sn-5*DEN*(pu*mu_w+pw*mu_u)
                assert np.array_equal(jn,contracted)
                out[(primed,x,delta0)]=[F(int(v),denominator) for v in jn]
                x2=sum(F(int(E[c,1]))*out[(primed,x,delta0)][c] for c in range(14))
                D2=F(int(pu[2]+pu[3]),DEN)
                simple=F(int(delta[0]),4)*D2*(F(int((pl@B)[2]),DEN)+F(int((pr@B)[2]),DEN))
                assert x2==simple
                checks+=1
    return out,{'four_context_channels':checks,'assignments_per_channel':14**4,
                'total_weighted_assignments':checks*14**4,'denominator':str(denominator),
                'int64_bound_verified':True,'rate_ranges':rate_ranges,'actual_contexts':contexts}

def drift_checks(currents,matrices,A2):
    records=[];drifts={}
    for primed in (False,True):
        for x in range(N):
            derivative=[F(0) for _ in range(14)]
            for delta0 in DELTAS:
                a0=delta0[0]-1
                if delta0==(1,0,0):continue
                incoming=currents[(primed,(x-a0)%N,delta0)];outgoing=currents[(primed,x,delta0)]
                derivative=[v+inc-out for v,inc,out in zip(derivative,incoming,outgoing)]
            assert sum(derivative)==0
            X2=sum(derivative[c]*int(E[c,1]) for c in range(14))
            rho_dot=sum((s.Rational(v.numerator,v.denominator)*matrices[c] for c,v in enumerate(derivative)),s.zeros(4))
            A2dot=s.trace(rho_dot*A2)
            assert A2dot==s.Rational(X2.numerator,X2.denominator)/4
            D2=F(160 if primed else 128,DEN)
            exact=D2*F(1,8)*F(int(COS2[(x+2)%6]-COS2[(x+4)%6]),4)
            assert X2==exact
            drifts[(primed,x)]=(X2,A2dot,rho_dot)
            records.append({'primed':primed,'x':x,'X2_derivative':str(X2),'A2_derivative':str(A2dot)})
    base,alt=drifts[(False,1)],drifts[(True,1)]
    assert base[0]==F(-3,224) and alt[0]==F(-15,896)
    assert alt[0]-base[0]==F(-3,896)
    assert alt[1]-base[1]==-s.Rational(3,3584)
    difference=alt[2]-base[2];expected=s.zeros(4);expected[0,2]=expected[2,0]=-s.Rational(3,7168)
    assert difference==expected
    return {'rows':records,'selected_black_site':[1,1,0],'X2_derivative_difference':'-3/896',
            'A2_derivative_difference':'-3/3584','encoded_local_density_derivative_difference':[[str(v) for v in row] for row in difference.tolist()],
            'Euler_A2_difference':str(N*(alt[1]-base[1])),'clock':'Unaccelerated microscopic time; Euler acceleration multiplies by 12.',
            'scope':'Exact initial expectation only; initial independent colors permit four-context product weights, without assuming product evolution.'}

def main():
    matrices=states();A2,encoding=encoding_checks(matrices);currents,enumeration=exact_currents()
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'boundary':'Independent exact reconstruction before author checker/results access.',
            'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':s.__version__},
            'encoding':encoding,'direct_rate_enumeration':enumeration,'exact_initial_derivatives':drift_checks(currents,matrices,A2),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    with (HERE/'INDEPENDENT_RESULTS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print('exact encoding, 14^4 currents, and initial derivatives verified',flush=True)

if __name__=='__main__':main()
