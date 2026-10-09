#!/usr/bin/env python3
"""Independent review controls; imports no author runner or repository model."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import itertools as it
import math
import time
import numpy as np
import sympy as s
from scipy.linalg import expm

started=time.monotonic()
passed=0
def check(label,condition,detail=''):
    global passed
    if not condition: raise AssertionError(label+': '+str(detail))
    passed+=1
    print('PASS',label,detail,flush=True)

vel=list(it.product((-1,0,1),repeat=3))
index={v:i for i,v in enumerate(vel)}
energy=[sum(t*t for t in v) for v in vel]
def invpair(pair):
    i,j=pair
    return tuple(vel[i][d]+vel[j][d] for d in range(3))+(energy[i]+energy[j],)
reactions=[]
for a,b,c,d in it.combinations(range(27),4):
    for p,q in [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]:
        if invpair(p)==invpair(q): reactions.append(tuple(sorted((p,q))))
special=set()
for a,b in it.combinations(range(3),2):
    third=3-a-b
    for z in (-1,0,1):
        mid=[0]*3;mid[third]=z
        pairs=[]
        for axis in (a,b):
            plus=mid.copy();minus=mid.copy();plus[axis]+=1;minus[axis]-=1
            pairs.append(tuple(sorted((index[tuple(plus)],index[tuple(minus)]))))
        special.add(tuple(sorted(pairs)))
check('fresh_four_species_network',len(reactions)==len(set(reactions))==288 and len(special)==9 and special<=set(reactions))
Z=s.Matrix([[1,*v,e] for v,e in zip(vel,energy)])
M=[s.Rational(2,3)**(3-e)*s.Rational(1,6)**e for e in energy]
W=s.diag(*M)
def collision_exact(alpha):
    C=s.zeros(27)
    for r in reactions:
        (i,j),(k,l)=r
        rate=alpha if r in special else 1
        nu=s.zeros(27,1)
        for a in (i,j):nu[a]=-1
        for a in (k,l):nu[a]=1
        assert Z.T*nu==s.zeros(5,1) and M[i]*M[j]==M[k]*M[l]
        C+=rate*M[i]*M[j]*(nu*nu.T)
    return C
src=s.Matrix([[s.Rational(v[0]**2-v[1]**2,2),s.Rational(v[0]**2+v[1]**2-2*v[2]**2,2),
               v[0]*v[1],v[0]*v[2],v[1]*v[2],
               *[v[a]*(e-s.Rational(5,3)) for a in range(3)]] for v,e in zip(vel,energy)])
for alpha in [s.Rational(1),s.Rational(7,5),s.Rational(19,7)]:
    C=collision_exact(alpha)
    # Symmetric constrained-Poisson saddle solve, not (B+P)^-1.
    saddle=C.row_join(W*Z).col_join((Z.T*W).row_join(s.zeros(5)))
    inv=saddle.inv()
    R=inv[:27,:27]*W
    response=src.T*W*R*src
    mu=(4*alpha+31)/(8*alpha**2+133*alpha+170)
    expected=s.diag(mu,3*mu,*([s.Rational(67,1083)]*3),*([s.Rational(40,441)]*3))
    check('independent_KKT_response_'+str(alpha),response==expected,str(list(response.diagonal())))
    if alpha==1:
        check('independent_trace_inverse',s.trace(R)==s.Rational(6224911145567,509693499350),str(s.trace(R)))

vf=np.asarray(vel,float);ef=np.asarray(energy,float);Zf=np.asarray(Z,float)
def numeric_model(theta,rates):
    m=np.asarray([math.prod(theta/2 if a else 1-theta for a in v) for v in vel])
    sw=np.sqrt(m)
    C=np.zeros((27,27))
    for ((i,j),(k,l)),rate in zip(reactions,rates):
        nu=np.zeros(27);nu[[i,j]]=-1;nu[[k,l]]=1
        C+=rate*m[i]*m[j]*np.outer(nu,nu)
    B=C/sw[:,None]/sw[None,:]
    z=sw[:,None]*Zf
    P=z@np.linalg.inv(z.T@z)@z.T
    R=np.linalg.inv(B+P)-P
    return sw,B,P,R

# General asymmetric rates and theta exercise the acoustic proof's full scope.
rates=[1+((i+2*j+3*k+5*l)%11)/10 for (i,j),(k,l) in reactions]
sw,B,P,R=numeric_model(.4,rates)
Q=np.eye(27)-P;b=np.linalg.eigvalsh(R).max();c=math.sqrt(3)
k=np.array([2,-1,1]);T=1j*np.diag(vf@k)
u0=P@(sw*(1+.2*vf[:,0]-.3*vf[:,2]+.1*ef));norm=np.linalg.norm(u0);kn=np.linalg.norm(k)
for eps in (.4,.13,.04):
    A=-P@T@P+eps*P@T@R@T@P
    z=(R@R@T@A+R@Q@T@R@T)@P
    app=(np.eye(27)-eps*R@T+eps**2*z)@P
    lhs=app@A+(T+B/eps)@app
    rhs=eps**2*(z@A+T@z)
    residual=np.linalg.norm(lhs-rhs,2)
    check('acoustic_corrector_asymmetric_'+str(eps),residual<2e-11,{'residual':residual})
    tf=.37;U=expm(tf*A)@u0;w=-R@T@U
    h=expm(-tf*(T+B/eps))@(u0-eps*R@T@u0)
    Zb=2*b*b*c*c*kn**2*norm+eps*b**3*c**3*kn**3*norm
    Yb=(4*b*b*c**3*kn**3+4*eps*b**3*c**4*kn**4+eps**2*b**4*c**5*kn**5)*norm
    ep=np.linalg.norm(P@h-U);ec=np.linalg.norm(h-U-eps*w)
    check('acoustic_error_bounds_'+str(eps),ep<=eps**2*(Zb+tf*Yb) and ec<=eps**2*(2*Zb+tf*Yb),
          {'projected':ep,'corrected':ec,'projected_bound':eps**2*(Zb+tf*Yb)})

# Off-axis diffusive cancellation at the actual irrational isotropic rate.
alpha=(-4579+3*math.sqrt(7614177))/1072
sw,B,P,R=numeric_model(1/3,[alpha if r in special else 1 for r in reactions])
k=np.array([1,2,-1]);T=1j*np.diag(vf@k);kn=np.linalg.norm(k)
rho=1+.2j;j=np.array([2,-1,0],complex)+.3j*np.array([1,0,1])
dr=4/49;nu=67/361;scalar=(5-3*ef)/2
u0=sw*(rho*scalar+3*vf@j)
ut=sw*(-dr*kn**2*rho*scalar-3*nu*kn**2*vf@j)
m=sw*(-3*dr*1j*(vf@k)*rho)
w=-R@T@u0+m;z=-R@T@w
check('diffusive_off_axis_full_cancellation',np.linalg.norm(T@u0+B@w)<1e-11 and np.linalg.norm(ut+T@w+B@z)<1e-11,
      [np.linalg.norm(T@u0+B@w),np.linalg.norm(ut+T@w+B@z)])
wrong=sw*(-3*(20/147)*1j*(vf@k)*rho)
ww=-R@T@u0+wrong;zz=-R@T@ww
check('wrong_heat_density_coefficient_rejected',np.linalg.norm(ut+T@ww+B@zz)>1e-2)
b=np.linalg.eigvalsh(R).max();a=c*b+dr*math.sqrt(6/5);norm=np.linalg.norm(u0)
for delta in (.3,.1):
    tf=.4
    U=sw*(math.exp(-dr*kn**2*tf)*rho*scalar+3*math.exp(-nu*kn**2*tf)*vf@j)
    h=expm(-tf*(T/delta+B/delta**2))@u0
    bound=delta*(2*a*kn+tf*a*(nu+b*c*c)*kn**3)*norm+delta**2*(2*b*c*a*kn**2+tf*b*c*a*nu*kn**4)*norm
    check('diffusive_error_bound_'+str(delta),np.linalg.norm(h-U)<=bound,{'error':np.linalg.norm(h-U),'bound':bound})

# Independent diagonal-algebra calculation, and a coherent shared-mark control.
F=np.array([[0,1,0],[1,0,0],[0,0,0]],complex)
merged=np.array([[0,0,1],[0,0,1],[1,1,0]],complex)
def adjoint_D(A,D):return A@D@A-(A@A@D+D@A@A)/2
off=lambda X:np.linalg.norm(X-np.diag(np.diag(X)))
check('separate_mark_diagonal_closure',all(off(adjoint_D(F,np.diag(np.eye(3)[i])))==0 for i in range(3)))
check('coherent_merged_mark_control',off(adjoint_D(merged,np.diag([0,0,1])))>1)
X=np.array([[0,1],[1,0]],complex);h=.031;gamma=.7
U=expm(-1j*math.sqrt(h*gamma)*np.kron(F,X))
cA=np.diag([math.cos(math.sqrt(h*gamma))]*2+[1]);sA=math.sin(math.sqrt(h*gamma))*F
err=0
for i,j in it.product(range(3),repeat=2):
    E=np.zeros((3,3),complex);E[i,j]=1
    out=U@np.kron(E,np.diag([1,0]))@U.conj().T
    red=np.einsum('iaja->ij',out.reshape(3,2,3,2))
    err=max(err,np.linalg.norm(red-cA@E@cA-sA@E@sA))
check('joint_unitary_channel_all_units',err<1e-13,err)

# Different graph/count from the author: five-slot star, 100 microstates.
counts=[(2,2,1,0),(1,1,2,1),(0,0,3,2)];edges=[(0,j) for j in range(1,5)]
states=[z for z in it.product(range(4),repeat=5) if tuple(z.count(a) for a in range(4)) in counts]
ix={z:i for i,z in enumerate(states)};n=len(states);S=np.zeros((n,n));C=np.zeros((n,n))
for z,i in ix.items():
    for a,b in edges:
        target=list(z);target[a],target[b]=target[b],target[a]
        if target!=list(z):S[i,ix[tuple(target)]]+=1
        pair={z[a],z[b]}
        outputs=((2,3),(3,2)) if pair=={0,1} else (((0,1),(1,0)) if pair=={2,3} else ())
        for v,w in outputs:
            target=list(z);target[a],target[b]=v,w;C[i,ix[tuple(target)]]+=.25
S-=np.diag(S.sum(axis=1));C-=np.diag(C.sum(axis=1))
lift=np.array([[int(tuple(z.count(a) for a in range(4))==c) for c in counts] for z in states],float)
sizes=lift.sum(axis=0);average=(lift/sizes).T;P=lift@average
target=np.array([[-.8,.8,0],[.4,-.6,.2],[0,1.2,-1.2]])
check('star_pair_normalization',np.max(abs(average@C@lift-target))<1e-14,{'fibers':sizes.tolist()})
check('star_exact_equilibrium',np.max(abs((sizes/sizes.sum())@target))<1e-14 and np.max(abs(C-C.T))==0)
R=np.linalg.inv(-S+P)-P;bn=np.linalg.norm(R,np.inf);cn=np.linalg.norm(C,np.inf)
check('star_Poisson_equation',np.linalg.norm(S@R+(np.eye(n)-P),np.inf)<1e-12)
for eps in (.4,.1,.025):
    tf=.6
    error=np.linalg.norm(expm(tf*(S/eps+C))@P-lift@expm(tf*target)@average,np.inf)
    bound=2*eps*bn*cn*(1+tf*cn)
    check('star_averaging_bound_'+str(eps),error<=bound,{'operator_sup_error':error,'bound':bound})
print('elapsed_sec',format(time.monotonic()-started,'.4f'),flush=True)
print('TOTAL: PASS='+str(passed)+' FAIL=0',flush=True)
