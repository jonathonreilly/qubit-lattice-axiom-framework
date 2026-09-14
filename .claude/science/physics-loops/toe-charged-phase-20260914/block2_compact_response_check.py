"""Independent finite checks for the compact inference boundary and real traces."""
from itertools import combinations,product
from pathlib import Path
from fractions import Fraction as F
import json,math
import numpy as np
from sympy import Matrix

sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);sz=np.diag([1,-1]);I=np.eye(4,dtype=complex)
gamma=[np.kron(sx,s) for s in [sx,sy,sz]]+[np.kron(sy,np.eye(2))]
basis=[]
for k in range(5):
    for S in combinations(range(4),k):
        B=I.copy()
        for i in S:B=B@gamma[i]
        assert np.trace(B)==(4 if not S else 0)
        basis.append(B)
# Test exact Gaussian-integer multiplication closure using explicit matrices.
for A in basis:
    for B in basis:
        C=A@B
        assert any(np.array_equal(C,sign*D) for D in basis for sign in [-1,1])
# Supplied Wilson r=2 is inside the derivation's domain but does not have
# positive Fourier type. On a single square compute exact determinants at
# flux 0 and pi. Positive Fourier type would require W(0)>=W(pi).
r=2;t0=2;M=80
vertices=[(0,0),(1,0),(0,1),(1,1)];index={x:i for i,x in enumerate(vertices)}
def square_det(flux_sign):
    D=np.eye(16,dtype=complex)*M
    for x in vertices:
        for mu in range(2):
            y=list(x);y[mu]+=1;y=tuple(y)
            if y not in index:continue
            phase=flux_sign if x==(0,0) and mu==0 else 1
            a=slice(4*index[x],4*index[x]+4);b=slice(4*index[y],4*index[y]+4)
            D[a,b]=-t0/2*(r*I-gamma[mu])*phase
            D[b,a]=-t0/2*(r*I+gamma[mu])*phase
    # Entries have exact integer real and imaginary parts in this fixture.
    exact=Matrix([[int(z.real)+int(z.imag)*__import__('sympy').I for z in row] for row in D])
    return int(exact.det())
d0=square_det(1);dpi=square_det(-1);assert d0>0 and dpi>d0
assert 8*(t0*(r+1)/2)<M
# A full 2^4-vertex box avoids relying on a lower-dimensional slice.
# Exact small integer matrix powers plus a rational log-series remainder
# certify the same strict inequality, without subtracting nearby floats.
vs4=list(product(range(2),repeat=4));ix4={v:i for i,v in enumerate(vs4)}
def box4_hop(sign):
    K=np.zeros((64,64),complex)
    for x in vs4:
        for mu in range(4):
            y=list(x);y[mu]+=1;y=tuple(y)
            if y not in ix4:continue
            phase=sign if x==(0,0,0,0) and mu==0 else 1
            a=slice(4*ix4[x],4*ix4[x]+4);b=slice(4*ix4[y],4*ix4[y]+4)
            K[a,b]=-(2*I-gamma[mu])*phase
            K[b,a]=-(2*I+gamma[mu])*phase
    return K
K0,Kpi=box4_hop(1),box4_hop(-1)
assert np.trace(Kpi@Kpi)==np.trace(K0@K0)
trace4=np.trace(np.linalg.matrix_power(Kpi,4)-np.linalg.matrix_power(K0,4))
assert trace4==-1344
mass4=10000;q4=F(24,mass4);leading4=F(672,mass4**4)
# Each log W tail <=2*(m V)*q^6/[6(1-q)]; compare two fields.
tail4=F(4*64,6)*q4**6/(1-q4);assert leading4>tail4
full4={'vertices':16,'M':mass4,'r':2,'t0':2,'trace4_difference':int(trace4.real),'leading_logW_difference':str(leading4),'absolute_logW_difference_tail_upper':str(tail4),'strict_logW_increase_lower':str(leading4-tail4)}
looprows=[]
for L in [1,2,4,8,16,32]:
    edges={}
    def add(x,mu,sign):edges[x,mu]=edges.get((x,mu),0)+sign
    for v in range(L):
        add((v,0),0,1);add((v,L),0,-1);add((L,v),1,1);add((0,v),1,-1)
    div={}
    for (x,mu),sign in edges.items():
        y=list(x);y[mu]+=1;y=tuple(y)
        div[x]=div.get(x,0)+sign;div[y]=div.get(y,0)-sign
    assert not any(div.values())
    assert len(edges)==4*L and sum(s*s for (x,mu),s in edges.items() if mu==0)==2*L
    for k in [np.array([.173,.241]),np.array([1e-6/L,0.])]:
        direct=np.array([sum(s*np.exp(-1j*np.dot(k,x)) for (x,a),s in edges.items() if a==mu) for mu in [0,1]])
        S=np.prod([sum(np.exp(-1j*k[a]*v) for v in range(L)) for a in [0,1]])
        diff=1-np.exp(-1j*k);closed=np.array([diff[1],-diff[0]])*S
        assert np.linalg.norm(direct-closed)<1e-10
        assert abs(np.dot(diff,direct))<1e-10
    rho=F(1,10**6);lam=rho/(2*L);coefficient=lam*L**4
    numerical=float(lam)*float(np.vdot(direct,direct).real)/float(np.vdot(diff,diff).real)
    assert abs(numerical/float(coefficient)-1)<1e-6
    looprows.append({'L':L,'component_second_moment':str(rho),'infrared_coefficient_exact':str(coefficient),'direct_Fourier_coefficient':numerical})
# Strict compact density point uses c<=6.6164, beta=100, d=4.
# pi>3.14 gives a>115. Positive Taylor partial sums certify exponent bounds.
kappa=F(100)-F(66164,10000);assert kappa*F(314,100)**2/8>115
partial=sum(F(115,2)**n/math.factorial(n) for n in range(201));assert partial>9*10**24
assert 1+F(345,2)>100
upper=F(4)/(115*F(99,100)*9*10**24);assert upper<F(4,10**27)
result={'Clifford_basis_zero_traces_and_exact_multiplication':True,'actual_r2_Wilson_negative_Fourier_type':{'det_zero':str(d0),'det_pi':str(dpi),'W_pi_over_W_zero':float(F(dpi,d0)**2),'M':M,'r':r,'t0':t0},'full_4d_negative_Fourier_type':full4,'closed_current_density_counterexample':looprows,'strict_compact_density_upper':'4e-27','density_certificate':'pi>3.14, a>115, exp(57.5)>9e24 by positive rational Taylor partial sum, exp(172.5)>100'}
print(json.dumps(result,indent=2),flush=True)
Path(__file__).with_name('BLOCK2_COMPACT_RESPONSE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
