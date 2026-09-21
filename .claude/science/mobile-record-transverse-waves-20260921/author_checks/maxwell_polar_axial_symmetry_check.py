#!/usr/bin/env python3
"""Exact finite controls of a supplied parity and time-reversal assignment."""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as F
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent


def main():
    checks=[]
    def check(name,condition,detail=None):
        assert condition,(name,detail)
        checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
    e=np.zeros((15,3),dtype=np.int64);b=e.copy()
    e[1:7]=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
    b[7:]=np.array(list(product((-1,1),repeat=3)))
    lookup={tuple(np.concatenate((e[a],b[a]))):a for a in range(15)}
    S2=(np.cross(e[:,None,:],b[None,:,:])+np.cross(e[None,:,:],b[:,None,:])).transpose(2,0,1)
    words=np.array(list(product(range(15),repeat=4)),dtype=np.int64)
    def drive(words):
        l,a,z,r=words.T
        return np.stack([S2[i,l,a]+S2[i,a,r]-S2[i,l,z]-S2[i,z,r] for i in range(3)])
    h2=drive(words);actions=[];matrices=[];comparisons=0
    for perm in permutations(range(3)):
        parity=(-1)**sum(perm[x]>perm[y] for x in range(3) for y in range(x+1,3))
        for signs in product((-1,1),repeat=3):
            R=np.zeros((3,3),dtype=np.int64)
            for old in range(3): R[perm[old],old]=signs[old]
            determinant=int(parity*np.prod(signs))
            labels=np.array([lookup[tuple(np.concatenate((R@e[a],determinant*R@b[a])))] for a in range(15)])
            matrices.append(R);actions.append(labels)
            for old in range(3):
                transformed=labels[words if signs[old]>0 else words[:,::-1]]
                assert np.array_equal(drive(transformed)[perm[old]],h2[old])
                comparisons+=len(words)
    check('all_48_polar_axial_spatial_rate_symmetries',True,dict(local_comparisons=comparisons))
    matrix_index={tuple(R.ravel()):i for i,R in enumerate(matrices)}
    for i,R in enumerate(matrices):
        for j,Q in enumerate(matrices):
            assert np.array_equal(actions[i][actions[j]],actions[matrix_index[tuple((R@Q).ravel())]])
    check('exact_group_composition_on_all_15_labels',True,dict(group_products=48**2))
    inversion=actions[matrix_index[tuple((-np.eye(3,dtype=np.int64)).ravel())]]
    check('spatial_inversion_is_polar_on_A_and_axial_on_B',np.array_equal(e[inversion],-e) and np.array_equal(b[inversion],b))
    theta=np.array([lookup[tuple(np.concatenate((e[a],-b[a])))] for a in range(15)])
    check('time_reversal_is_an_involution',np.array_equal(theta[theta],np.arange(15)))
    check('time_reversal_and_endpoint_swap_reverse_the_same_drive',
          np.array_equal(drive(theta[words]),-h2) and np.array_equal(drive(words[:,[0,2,1,3]]),-h2))
    for labels in actions: assert np.array_equal(theta[labels],labels[theta])
    check('time_reversal_commutes_with_full_spatial_group',True)
    # For each full four-cycle, compare all exit rates with the time-reversed
    # configuration, including null-event removal at equal endpoints.
    for variant in ('minimal','linear'):
        total=np.zeros((3,len(words)),dtype=np.int64);reverse=total.copy()
        for x in range(4):
            view=words[:,np.array([x-1,x,x+1,x+2])%4]
            hh=drive(view);mask=(view[:,1]!=view[:,2])
            c20=2+10*np.maximum(hh,0) if variant=='minimal' else 30+5*hh
            ct20=2+10*np.maximum(-hh,0) if variant=='minimal' else 30-5*hh
            total+=c20*mask;reverse+=ct20*mask
        check('actual_escape_rates_match_under_Theta_'+variant,np.array_equal(total,reverse))
    # Complete nontrivial count sectors, unioned with their Theta images:
    # microscopic product reversal relation and failure of ordinary symmetry.
    seed=(0,3,7,8)  # e_y couples to the x-directed cross-product current.
    states=sorted(set(permutations(seed))|set(permutations(tuple(theta[list(seed)]))));index={a:i for i,a in enumerate(states)}
    Q=s.zeros(len(states));T=s.zeros(len(states));ordinary_asymmetry=None
    for row,state in enumerate(states):
        T[row,index[tuple(theta[list(state)])]]=1
        for x in range(4):
            local=np.array([[state[(x+d)%4] for d in (-1,0,1,2)]])
            hh=int(drive(local)[0,0]);rate=s.Rational(1,10)+s.Rational(max(hh,0),2)
            moved=list(state);moved[x],moved[(x+1)%4]=moved[(x+1)%4],moved[x];col=index[tuple(moved)]
            if row!=col:
                Q[row,col]+=rate;Q[row,row]-=rate
    check('complete_sector_stationarity',s.ones(1,len(states))*Q==s.zeros(1,len(states)) and Q*s.ones(len(states),1)==s.zeros(len(states),1))
    check('complete_sector_generalized_reversal',T*T==s.eye(len(states)) and Q.T==T*Q*T,dict(states=len(states)))
    check('ordinary_detailed_balance_negative_control',Q!=Q.T)
    # Full field involution; the triple B moment is odd as well as Y.
    fields=np.vstack((np.sum(e*e,axis=1),np.sum(b*b,axis=1)//3,e.T,b.T,
        e[:,0]**2-e[:,1]**2,e[:,0]**2+e[:,1]**2-2*e[:,2]**2,
        b[:,0]*b[:,1],b[:,0]*b[:,2],b[:,1]*b[:,2],np.prod(b,axis=1)))
    signs=np.array([1,1,1,1,1,-1,-1,-1,1,1,1,1,1,-1])
    check('all_fourteen_field_reversal_parities',np.array_equal(fields[:,theta],signs[:,None]*fields))
    kx,ky,kz,a,z=s.symbols('kx ky kz a b',real=True)
    CK=s.Matrix([[0,-kz,ky],[kz,0,-kx],[-ky,kx,0]])
    A=s.zeros(14);A[2:5,5:8]=-a*CK;A[5:8,2:5]=z*CK
    TF=s.diag(*map(int,signs))
    check('linear_Maxwell_generator_reversal_identity',TF*A*TF==-A)
    result=dict(count=len(checks),checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope='Exact finite symmetries of the supplied polar/axial label assignment. This does not identify the model with quantum electromagnetism or establish a microscopic Gauss constraint.')
    (HERE/'MAXWELL_POLAR_AXIAL_SYMMETRY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TOTAL:',len(checks),'PASS',flush=True)


if __name__=='__main__': main()
