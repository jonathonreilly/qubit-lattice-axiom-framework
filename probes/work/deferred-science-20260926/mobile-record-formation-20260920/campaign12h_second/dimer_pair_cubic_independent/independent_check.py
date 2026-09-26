#!/usr/bin/env python3
"""Exact proper-cubic operator projection and microscopic quadratic drift."""
from pathlib import Path
import datetime,hashlib,itertools,json
from fractions import Fraction as F
import numpy as np
import sympy as s

P=Path(__file__).resolve().parent;N=12;D=1792
E=np.zeros((14,3),dtype=np.int64);B=E.copy()
for i in range(3):E[2*i,i]=1;E[2*i+1,i]=-1
B[6:]=np.array(list(itertools.product((-1,1),repeat=3)),dtype=np.int64)
CHI=np.prod(B,axis=1);G=B[:,0]*B[:,1]
COS2=[2,1,-1,-2,-1,1]
directions=[tuple(z*int(i==j) for j in range(3)) for i in range(3) for z in (1,-1)]
labels=[(tuple(E[a]),tuple(B[a])) for a in range(14)]

def groups_and_states():
    rotations=[];projection=s.zeros(16)
    for perm in itertools.permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in itertools.product((-1,1),repeat=3):
            if parity*np.prod(signs)!=1:continue
            R=s.zeros(3)
            for i in range(3):R[i,perm[i]]=signs[i]
            U=s.diag(1,R);projection+=parity*s.kronecker_product(U.conjugate(),U)
            for b in B[6:]:assert s.prod(R*s.Matrix(b))==parity*int(np.prod(b))
            rotations.append((R,U,parity))
    assert len(rotations)==24 and projection==s.zeros(16)
    states=[];minors=[]
    for a in range(14):
        e,b=s.Matrix(E[a]),s.Matrix(B[a]);w=e/16+s.I*b/48
        rho=s.diag(s.Rational(1,2),s.Rational(1,6),s.Rational(1,6),s.Rational(1,6))
        rho[1:4,0]=w;rho[0,1:4]=w.conjugate().T
        if a>=6:rho[1:4,1:4]+=s.Rational(1,96)*(b*b.T-s.eye(3))
        assert rho==rho.conjugate().T and s.trace(rho)==1
        mm=[rho[:k,:k].det() for k in range(1,5)];assert all(x>0 for x in mm)
        states.append(rho);minors.append([str(x) for x in mm])
    for R,U,parity in rotations:
        for a in range(14):
            transformed=(tuple(R*s.Matrix(E[a])),tuple(R*s.Matrix(B[a])));index=labels.index(transformed)
            assert U*states[a]*U.conjugate().T==states[index]
    assert sum((int(CHI[a])*states[a] for a in range(14)),s.zeros(4))==s.zeros(4)
    Q=s.zeros(4);Q[1,2]=Q[2,1]=1
    for a in range(14):assert s.trace(states[a]*Q)==s.Rational(int(G[a]),48)
    # A constant covariant family has no nonconstant readable Z12 moment.
    constant=s.eye(4)/4
    assert all(U*constant*U.T==constant for R,U,a in rotations)
    assert s.trace(constant*Q)==0 and len(set(G.tolist()))>1
    return states,Q,{'proper_rotations':24,'all_256_projection_entries_exactly_zero':True,
                    'state_covariance_relations':24*14,'leading_principal_minors':minors,
                    'corner_orthogonal_eigenvalue':'5/32','corner_parallel_eigenvalue':'3/16',
                    'corner_Schur_complement':'71/144','axis_Schur_complement':'61/128',
                    'exact_cubic_operator_sum_zero':True,'readout_coefficient':'1/48',
                    'constant_encoding_countercontrol':'Covariant rho_a=I/4 is w-blind and has no nonzero Z12 readout; covariance alone supplies no drift contradiction.'}

def prob(x,prime):
    p=np.full(14,128,dtype=np.int64);p[2]+=32;p[3]-=32
    if prime:p+=7*int(COS2[x%6])*CHI
    assert p.sum()==D and p.min()>0
    return p

def witness(states,Q):
    density=lambda p:sum((s.Rational(int(p[a]),D)*states[a] for a in range(14)),s.zeros(4))
    for x in range(N):
        p,q=prob(x,False),prob(x,True)
        assert density(p)==density(q)
        assert np.array_equal(p@E,q@E) and np.array_equal(p@B,q@B)
        assert all(int((q-p)@(B[:,i]*B[:,j]))==0 for i in range(3) for j in range(3))
        assert F(int(q@CHI),D)==F(COS2[x%6],32)
    assert s.kronecker_product(density(prob(1,False)),density(prob(3,False)))==s.kronecker_product(density(prob(1,True)),density(prob(3,True)))
    denominator=40*D**4;assert 14**4*160**4*42<2**63
    cases=0;derivatives=[];matrices=[];channel_rows=[]
    def current(x,delta,prime):
        nonlocal cases
        step=delta[0]-1
        if delta==(1,0,0):return [F(0)]*14
        pl,pu,pw,pr=[prob(x+k*step,prime) for k in (-1,0,1,2)]
        Sn=np.einsum('abi,i->ab',np.cross(E[:,None,:],B[None,:,:])+np.cross(E[None,:,:],B[:,None,:]),np.array(delta))
        hn=Sn[:,:,None,None]+Sn[None,:,None,:]-Sn[:,None,:,None]-Sn[None,None,:,:]
        rate=22+5*hn;assert rate.min()>=2 and rate.max()<=42
        mass=pl[:,None,None,None]*pu[None,:,None,None]*pw[None,None,:,None]*pr[None,None,None,:]
        weighted=mass*rate;jn=weighted.sum(axis=(0,2,3))-weighted.sum(axis=(0,1,3))
        assert int(jn.sum())==0
        j=[F(int(v),denominator) for v in jn]
        actual=sum(int(G[a])*j[a] for a in range(14))
        claimed=F(delta[0],4)*F(1,28)*(F(int(pu@CHI),D)+F(int(pw@CHI),D))
        assert actual==claimed;cases+=1
        channel_rows.append({'primed':prime,'anchor_x':x%N,'delta':delta,'exact_Z12_current':str(actual)})
        return j
    for prime in (False,True):
        drift=[F(0)]*14
        for delta in directions:
            if delta==(1,0,0):continue
            inc=current(1-(delta[0]-1),delta,prime);out=current(1,delta,prime)
            drift=[v+i-o for v,i,o in zip(drift,inc,out)]
        z=sum(int(G[a])*drift[a] for a in range(14))
        dot=sum((s.Rational(v.numerator,v.denominator)*states[a] for a,v in enumerate(drift)),s.zeros(4))
        assert s.trace(dot*Q)==s.Rational(z.numerator,z.denominator)/48
        derivatives.append(z);matrices.append(dot)
    assert derivatives==[F(0),F(3,3584)]
    diff=matrices[1]-matrices[0];expected=s.zeros(4);expected[1,2]=expected[2,1]=s.Rational(1,114688)
    assert diff==expected and s.trace(diff*Q)==s.Rational(1,57344)
    return {'N':N,'minimum_probability':str(min(F(int(v),D) for prime in (False,True) for x in range(N) for v in prob(x,prime))),
            'local_density_equal_at_all_12_phases':True,'two_pair_tensor_equality_exact':True,
            'full_product_equality':'Factorwise equality for independent encoded pairs; no full tensor matrix materialization.',
            'four_context_cases':cases,'assignments_per_case':14**4,'exact_channel_currents':channel_rows,
            'Z12_derivatives':[str(z) for z in derivatives],'Q12_derivative_difference':str(s.trace(diff*Q)),
            'local_density_derivative_difference':[[str(v) for v in rr] for rr in diff.tolist()],
            'clock':'Actual unaccelerated rates k0/2+h/4, k0=11/10 and gamma=1.'}

def main():
    states,Q,representation=groups_and_states()
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'boundary':'Independent exact construction before any new author script/results.','representation':representation,'drift_witness':witness(states,Q),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    with (P/'INDEPENDENT_RESULTS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print('exact 24-rotation projection, positive covariant family, and 14^4 drift checked')
if __name__=='__main__':main()
