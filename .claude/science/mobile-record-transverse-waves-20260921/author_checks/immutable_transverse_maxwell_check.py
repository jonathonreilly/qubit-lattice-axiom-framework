#!/usr/bin/env python3
"""Exact local rates, currents and fourteen-field Maxwell-sector controls."""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as R
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):
    if not ok: raise AssertionError((name,detail))
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)


def cross_matrix(k):
    x,y,z=k
    return s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])


def main():
    axes=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=np.int64)
    cubes=np.array(list(product((-1,1),repeat=3)),dtype=np.int64)
    e=np.vstack((np.zeros((1,3),dtype=np.int64),axes,np.zeros((8,3),dtype=np.int64)))
    b=np.vstack((np.zeros((7,3),dtype=np.int64),cubes))
    S2=np.stack([np.cross(e[:,None,:],b[None,:,:])[:,:,i]+np.cross(e[None,:,:],b[:,None,:])[:,:,i] for i in range(3)])
    words=np.array(list(product(range(15),repeat=4)),dtype=np.int64)
    l,a,z,r=words.T
    h2=np.stack([S2[i,l,a]+S2[i,a,r]-S2[i,l,z]-S2[i,z,r] for i in range(3)])
    check('symmetric_pair_tensor_and_sharp_bounds',np.array_equal(S2,S2.transpose(0,2,1)) and
          np.max(np.abs(S2))==1 and h2.min()==-4 and h2.max()==4,
          dict(alphabet_size=15,local_words=len(words),tensor_supremum='|gamma|/2',drive_supremum='2|gamma|'))
    lookup={tuple(word):i for i,word in enumerate(words)}
    swapped=np.array([lookup[tuple(word[[0,2,1,3]])] for word in words])
    check('endpoint_drive_antisymmetry',np.array_equal(h2[:,swapped],-h2))
    # Exact pointwise balance on every four-cycle, calculated independently
    # by rotating the word used as the full configuration.
    balance=np.zeros_like(h2)
    for x in range(4):
        index=np.array([lookup[tuple(word[np.array([x-1,x,x+1,x+2])%4])] for word in words])
        balance+=h2[:,index]
    check('pointwise_product_balance_all_four_cycles',np.all(balance==0),dict(axis_configurations=3*15**4))
    tags=[tuple(np.concatenate((e[a],b[a]))) for a in range(15)];tag_index={tag:a for a,tag in enumerate(tags)}
    count=0
    for perm in permutations(range(3)):
        parity=(-1)**sum(perm[x]>perm[y] for x in range(3) for y in range(x+1,3))
        for signs in product((-1,1),repeat=3):
            if parity*np.prod(signs)!=1: continue
            rotation=np.zeros((3,3),dtype=np.int64)
            for old in range(3): rotation[perm[old],old]=signs[old]
            labels=np.array([tag_index[tuple(np.concatenate((rotation@e[a],rotation@b[a])))] for a in range(15)])
            transformed=labels[words]
            for old in range(3):
                newwords=transformed if signs[old]>0 else transformed[:,::-1]
                ll,aa,bb,rr=newwords.T;i=perm[old]
                transformed_drive=S2[i,ll,aa]+S2[i,aa,rr]-S2[i,ll,bb]-S2[i,bb,rr]
                assert np.array_equal(transformed_drive,h2[old])
                count+=len(words)
    check('all_proper_cubic_local_rate_transformations',True,dict(local_comparisons=count))
    inversion=np.array([tag_index[tuple(np.concatenate((-e[a],-b[a])))] for a in range(15)])
    ll,aa,bb,rr=inversion[words[:,::-1]].T
    inverted=S2[0,ll,aa]+S2[0,aa,rr]-S2[0,ll,bb]-S2[0,bb,rr]
    check('negative_control_literal_inversion_is_not_rate_symmetry',np.array_equal(inverted,-h2[0]) and np.any(inverted!=h2[0]))
    check('strictly_positive_minimal_and_linear_rate_floors',
          np.min(2+10*np.maximum(h2,0))==2 and np.min(30+5*h2)==10,
          dict(minimal_floor='1/10',linear_K='3/2',linear_floor='1/2'))

    weights_cases=[np.array([60]+[6]*6+[3]*8),np.array([24]+[12]*6+[3]*8),np.arange(1,16)]
    currents=[]
    for case,w in enumerate(weights_cases):
        den=int(w.sum());X=w@e;Y=w@b;XY=np.cross(X,Y)
        target_num=w[:,None]*(den*(np.cross(e,Y)+np.cross(X,b))-2*XY)
        mass=np.prod(w[words],axis=1)
        for axis in range(3):
            for name,rate20 in [('minimal',2+10*np.maximum(h2[axis],0)),('linear',30+5*h2[axis])]:
                direct=np.array([np.sum(mass*rate20*((a==label).astype(np.int64)-(z==label).astype(np.int64))) for label in range(15)])
                check(f'exact_four_site_product_current_case{case}_axis{axis}_{name}',np.array_equal(direct,20*den*target_num[:,axis]))
                currents.append(dict(case=case,axis=axis,variant=name,currents=[str(R(int(v),20*den**4)) for v in direct]))

    E=s.Matrix(e[1:].T.tolist());B=s.Matrix(b[1:].T.tolist())
    nA=s.Matrix([[1]*6+[0]*8]);nB=s.Matrix([[0]*6+[1]*8])
    Q1=s.Matrix([list((e[1:,0]**2-e[1:,1]**2))]);Q2=s.Matrix([list((e[1:,0]**2+e[1:,1]**2-2*e[1:,2]**2))])
    QB=s.Matrix([list(b[1:,x]*b[1:,y]) for x,y in ((0,1),(0,2),(1,2))])
    chirality=s.Matrix([list(np.prod(b[1:],axis=1))])
    field=nA.col_join(nB).col_join(E).col_join(B).col_join(Q1).col_join(Q2).col_join(QB).col_join(chirality)
    check('fourteen_fields_are_complete',field.shape==(14,14) and field.det()!=0,dict(determinant=str(field.det())))
    inverse=field.inv();rA,rB,gamma=s.symbols('rho_A rho_B gamma',real=True)
    p=s.Matrix([rA/6]*6+[rB/8]*8);C=s.diag(*p)-p*p.T
    K=s.symbols('kx ky kz',real=True);direction=s.zeros(14)
    Hessians=[]
    for i in range(3):
        unit=[0,0,0];unit[i]=1
        # e_i dot (X cross Y) = X dot (-[e_i]_cross)Y.
        M=-cross_matrix(unit)
        Hess=gamma*(E.T*M*B+B.T*M.T*E);Hessians.append(Hess)
        A=C*Hess
        check(f'full_fourteen_field_entropy_symmetry_axis{i}',all(s.expand(x)==0 for x in A*C-C*A.T))
        direction+=K[i]*field*A*inverse
    expected=s.zeros(14);CK=cross_matrix(K)
    expected[2:5,5:8]=-gamma*rA*CK/3
    expected[5:8,2:5]=gamma*rB*CK
    check('full_directional_matrix_has_Maxwell_curl_signs',all(s.expand(x)==0 for x in direction-expected))
    speed2=gamma**2*rA*rB*sum(k*k for k in K)/3
    check('full_directional_cubic_minimal_polynomial',all(s.expand(x)==0 for x in direction**3-speed2*direction))
    lam=s.symbols('lambda');polynomial=direction.charpoly(lam)
    check('two_transverse_pairs_and_ten_zero_modes',s.factor(polynomial.as_expr()-polynomial.gen**10*(polynomial.gen**2-speed2)**2)==0)
    for densities in [(s.Rational(1,4),s.Rational(1,4)),(s.Rational(3,10),s.Rational(1,5)),(s.Rational(3,5),s.Rational(1,5))]:
        numeric=direction.subs({rA:densities[0],rB:densities[1],gamma:1,**dict(zip(K,(1,2,-1)))})
        check(f'exact_rank_four_at_{densities}',numeric.rank()==4)
    covariance=field*C*field.T
    check('uncorrelated_isotropic_vector_covariances',covariance[2:5,2:5]==s.eye(3)*rA/3 and covariance[5:8,5:8]==s.eye(3)*rB and covariance[2:5,5:8]==s.zeros(3))
    # Full nonlinear entropy symmetry at nonuniform rational products checks
    # terms arising from D C as well as the Hessian of the potential.
    for case,w in enumerate(weights_cases):
        pp=s.Matrix([s.Rational(int(v),int(w.sum())) for v in w[1:]])
        CC=s.diag(*pp)-pp*pp.T
        for i,Hess in enumerate(Hessians):
            HH=Hess.subs(gamma,1);gradient=HH*pp
            AA=s.diag(*gradient)-(pp.T*gradient)[0]*s.eye(14)-pp*gradient.T+CC*HH
            assert AA*CC==CC*AA.T
    check('nonlinear_entropy_symmetry_at_three_products',True)
    unitK=s.Matrix([1,2,-1]);norm2=(unitK.T*unitK)[0]
    PL=unitK*unitK.T/norm2;PT=s.eye(3)-PL
    check('static_longitudinal_subspace_and_transverse_wave_projector',
          PL*PL==PL and PT*PT==PT and cross_matrix(unitK)*PL==s.zeros(3) and
          cross_matrix(unitK)**2==-norm2*PT)
    check('negative_control_cosine_on_all_vector_modes_is_wrong',PL!=s.zeros(3))
    result=dict(count=len(checks),checks=checks,exact_product_currents=currents,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope='Exact controls for a supplied fifteen-state classical exchange model. Not an electromagnetic identification, qubit implementation, or general limit proof.')
    (HERE/'IMMUTABLE_TRANSVERSE_MAXWELL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TOTAL:',len(checks),'PASS',flush=True)


if __name__=='__main__': main()
