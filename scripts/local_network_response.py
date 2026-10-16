#!/usr/bin/env python3
"""Finite conditional intervention-response controls, not empirical validation."""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
import sympy as sp
from local_network_response_math import (schur_response,rank_one_difference,three_setting_residual,error_certificate,first_access_moment,leading_impulse_difference,remainder_certificate,spring_stiffness)
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/LOCAL_NETWORK_INTERVENTION_RESPONSE_NOTE_2026-10-16.md',
    'scripts/local_network_response_math.py',
]
ROOT=Path(__file__).resolve().parents[1]

def controls():
    rows=[]
    def check(name,condition,**details):
        assert bool(condition),name
        rows.append({'name':name,'passed':True,**details})
    t,z,a,b,c=sp.symbols('t z a b c',positive=True,real=True)
    u=sp.symbols('u',real=True);x0,v0=sp.symbols('x0 v0',real=True)
    xh=x0*sp.cos(sp.sqrt(c)*t)+v0/sp.sqrt(c)*sp.sin(sp.sqrt(c)*t)
    convolution=sp.integrate(b/sp.sqrt(c)*sp.sin(sp.sqrt(c)*(t-u))*u**2,(u,0,t))
    x=xh-convolution
    check('hidden memory equation and initial conditions',sp.simplify(sp.diff(x,t,2)+c*x+b*t**2)==0 and sp.simplify(x.subs(t,0)-x0)==0 and sp.simplify(sp.diff(x,t).subs(t,0)-v0)==0)
    A=sp.Matrix([[z*z+a,b],[b,z*z+c]])
    check('Schur response sign',sp.simplify(A.inv()[0,0]-schur_response(z,a,sp.Matrix([b]),sp.Matrix([[c]])))==0)
    K=sp.Matrix([[4,-1,0],[-1,5,-1],[0,-1,6]])
    O=sp.Matrix([[1,0,0],[0,sp.Rational(3,5),-sp.Rational(4,5)],[0,sp.Rational(4,5),sp.Rational(3,5)]])
    Kp=O*K*O.T;e=sp.Matrix([1,0,0]);w=sp.Matrix([0,1,-1]);y=sp.symbols('y',positive=True)
    check('positive spring chain and triangle share boundary response',O*O.T==sp.eye(3) and all(Kp[i,j]<0 for i in range(3) for j in range(i)) and all(sum(Kp.row(i))>0 for i in range(3)) and all(K[:i,:i].det()>0 for i in range(1,4)) and sp.simplify(((y*sp.eye(3)+K).inv()-(y*sp.eye(3)+Kp).inv())[0,0])==0)
    th=sp.symbols('theta',nonnegative=True);src=e;obs=sp.Matrix([0,1,0]);R=(y*sp.eye(3)+K).inv()
    direct=(obs.T*(R-(y*sp.eye(3)+K+th*w*w.T).inv())*src)[0]
    check('rank-one full response identity',sp.simplify(direct-rank_one_difference(R,src,obs,w,th))==0)
    ts=sp.symbols('t1:4');hh,jj=sp.symbols('H J');ds=[tt*hh/(1+tt*jj) for tt in ts]
    check('division-free three-setting relation',sp.factor(three_setting_residual(ts,ds))==0 and three_setting_residual([1,2,3],[0,0,0])==0)
    A2=sp.diag(2,5);v=sp.Matrix([1,1]);rank2=[(v.T*(A2.inv()-(A2+tt*sp.eye(2)).inv())*v)[0] for tt in [1,2,3]]
    rank2_residual=sp.factor(three_setting_residual([1,2,3],rank2))
    check('visible rank-two counterexample',rank2_residual!=0,residual=str(rank2_residual))
    rng=np.random.default_rng(62841);ratios=[]
    for _ in range(2000):
        st=np.array([.3,.8,1.7]);hv=rng.normal()+1j*rng.normal();jv=.2+.2j
        true=st*hv/(1+st*jv);err=.01*(rng.normal()+1j*rng.normal())+.005*(rng.normal(size=3)+1j*rng.normal(size=3));d=true+err
        bound=error_certificate(st,d,np.abs(err));value=abs(three_setting_residual(st,d))
        assert value<=bound+2e-14,'complex error certificate'
        ratios.append(value/bound)
    check('correlated complex error controls',len(ratios)==2000,maximum_fraction=round(max(ratios),10))
    # A pure quadratic error case specifically requires the epsilon_i epsilon_j term.
    st=[1,2,3];d=[0,0,0];err=[1,0,1];bound=error_certificate(st,d,[abs(v) for v in err]);err_residual=abs(three_setting_residual(st,err))
    check('quadratic error term at zero measured differences',err_residual<=bound and bound>0)
    cases=0
    for n in range(2,9):
        edges=[(i,i+1,i+1) for i in range(n-1)];chain=spring_stiffness(n,edges);source=sp.eye(n)[:,0]
        for i,j,weight in edges:
            direction=sp.eye(n)[:,i]-sp.eye(n)[:,j];degree,moment=first_access_moment(chain,source,direction);assert degree==i,'access degree'
            theta=sp.Rational(2,3);changed=chain+theta*direction*direction.T;v0=source;v1=source
            for power in range(2*degree+3):
                diff=(source.T*(v0-v1))[0]
                if power<2*degree+1:assert diff==0,'early path moment'
                if power==2*degree+1:
                    actual=(-1)**power*diff/sp.factorial(2*power+1)
                    assert sp.simplify(actual-leading_impulse_difference(theta,moment,degree,1))==0,'leading response coefficient'
                v0=chain*v0;v1=changed*v1
            cases+=1
    check('weighted-chain moment orders and coefficients',cases==28,cases=cases)
    edges=[]
    for row in range(3):
        for col in range(3):
            node=3*row+col
            if row<2:edges.append((node,node+3,1+row+col))
            if col<2:edges.append((node,node+1,2+row+col))
    grid=spring_stiffness(9,edges);source=sp.eye(9)[:,0]
    for i,j,weight in edges:
        degree,moment=first_access_moment(grid,source,sp.eye(9)[:,i]-sp.eye(9)[:,j]);assert degree==min(i//3+i%3,j//3+j%3),'grid access degree'
    check('bipartite grid distance',len(edges)==12,edges=12)
    triangle=spring_stiffness(3,[(0,1,1),(0,2,1),(1,2,2)])
    check('equal-distance cancellation and invisible response',first_access_moment(triangle,e,w)==(None,None) and sp.simplify(((y*sp.eye(3)+triangle).inv()-(y*sp.eye(3)+triangle+w*w.T).inv())[0,0])==0)
    check('labeled intervention distinguishes the two boundary-equivalent networks',first_access_moment(K,e,w)==(1,-1) and first_access_moment(Kp,e,w)==(1,sp.Rational(1,5)) and first_access_moment(Kp,e,O*w)==(1,-1))
    k=np.array(K,float);ww=np.array(w,float).reshape(3);theta=.7;changed=k+theta*np.outer(ww,ww);M=max(np.linalg.norm(k,2),np.linalg.norm(changed,2));ratios=[]
    for time in np.linspace(.2,2,60):
        def impulse(matrix):
            vals,vec=np.linalg.eigh(matrix);return np.sum(vec[0,:]**2*np.sin(np.sqrt(vals)*time)/np.sqrt(vals))
        actual=impulse(k)-impulse(changed);lead=leading_impulse_difference(theta,-1,1,time);bound=remainder_certificate(M,1,time)
        assert abs(actual-lead)<=bound+1e-14,'finite-time remainder'
        ratios.append(abs(actual-lead)/bound)
    check('finite-time spectral remainder controls',len(ratios)==60,maximum_fraction=round(max(ratios),10))
    # Exact coefficient envelope identity used in the all-time proof.
    for degree in range(5):
        q=4*degree+5
        for r in range(12):assert math.factorial(q+2*r)>=math.factorial(q)*math.factorial(2*r),'factorial envelope'
    check('Taylor factorial envelope',True,degrees=5,tail_terms=12)
    return rows

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
    rows=controls();payload={'summary':{'passed':len(rows),'failed':0},'checks':rows,'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},'empirical_validation':False,'scope':'Finite supplied real linear network and calibrated source/readout/intervention. General proofs are in the paired note; finite controls do not derive a physical action.'}
    print(json.dumps(payload,sort_keys=True,indent=2))
    if not args.json:
        print('per_element: exact matrix and response expressions checked in finite synthetic examples.')
        print('per_site: finite chains and a nine-site grid checked under supplied positive spring dynamics.')
        print('per_mode: finite spectral response and Taylor bounds checked; no microscopic mode identification.')
        print('per_block: finite observed/hidden partitions and rank-one interventions checked algebraically.')
        print('lattice_wide: checked and not executed — no infinite-lattice dynamics or physical light-cone claim.')
if __name__=='__main__':main()
