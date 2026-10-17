#!/usr/bin/env python3
"""Exact path-distance check and bounded finite diagnostics for the addendum."""
import hashlib
import json
import math
import platform
import resource
import sys
import time
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(60,60))
import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal
from scipy.special import jv
import sympy as sp

ROOT=Path(__file__).resolve().parent
start=time.monotonic()
results={}

def emit(key,data):
    results[key]=data
    print(key+': '+json.dumps(data,sort_keys=True),flush=True)

emit('runtime',{'python':sys.version,'executable':sys.executable,'platform':platform.platform(),
    'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,
    'cpu_cap_seconds':60,'wall_cap_seconds':90,'largest_exact_matrix':12,
    'largest_numeric_clock_matrix':128,'largest_bessel_index':299})

# Exact powers use rational entries and a long-enough finite surrogate.  At
# degrees <=d the far boundary of the length-12 surrogate is unreachable,
# so these particular matrix elements equal the infinite half-line exactly.
J=sp.Rational(3,16)
w=sp.Rational(1,4)
rho=17*J/6
c=rho
N=3
M=7
L=12
d=M-N+1

def A_exact(length):
    A=sp.diag(*[(2*J-c)/rho for _ in range(length)])
    A[0,0]+=w/rho
    for j in range(length-1):
        A[j,j+1]=A[j+1,j]=-J/rho
    return A

Am=A_exact(M)
Al=A_exact(L)
vm=sp.zeros(M,1)
vl=sp.zeros(L,1)
vm[N-1]=vl[N-1]=1
path_rows=[]
for degree in range(d+1):
    embedded=vm.col_join(sp.zeros(L-M,1))
    difference=vl-embedded
    nonzero=[{'site':j,'amplitude':str(difference[j])} for j in range(L) if difference[j]!=0]
    path_rows.append({'degree':degree,'nonzero_difference':nonzero})
    if degree<d:
        assert not nonzero
    else:
        assert nonzero==[{'site':M,'amplitude':str((-J/rho)**d)}]
    vm=Am*vm
    vl=Al*vl
emit('exact_first_removed_site_path',{'J':str(J),'w':str(w),'rho':str(rho),'N':N,'M':M,'L':L,'first_nonmatching_degree':d,'rows':path_rows})

# Exact finite-support normalization inequality: for orthogonal retained and
# discarded pieces of norms B and q, A=sqrt(B^2+q^2), the squared distance is
# 2(1-B/A).  Since 1-sqrt(1-x^2)<=x^2 for x=q/A in [0,1], distance<=sqrt(2)q/A,
# and therefore the proposed 2q/A is valid with slack.  Check endpoint arithmetic
# in A3 with the stated worst A>=3/4 and q<=eta/4.
emit('normalization_slack',{'A_lower':'3/4','tail_upper':'eta_p/4',
    'A2_distance_upper':'2 tail / A','using_worst_bounds':'2 eta_p / 3 <= eta_p',
    'minimum_retained_norm_for_eta_le_half':'5/8',
    'comment':'The addendum uses the weaker 4*tail upper bound; its constants are safe.'})

# Finite numerical horizon example, using the actual nominal dyadic J,w and
# arbitrary normalized input with support N=3.  This probes A4/A5 only, not
# the gate accuracy schedule.  The length-128 reference is finite.
Jf=float(J)
wf=float(w)
rhof=float(rho)
Nf=3
Mf=24
Lf=128
mu=1.0
Tobs=20.0
zeta=0.001
dMf=Mf-Nf+1
threshold=(rhof*Tobs*math.sinh(mu)+math.log(4/((1-math.exp(-mu))*zeta)))/mu
initial=np.array([1,1j,2],dtype=complex)/math.sqrt(6)

def evolution(length,t):
    diag=np.full(length,2*Jf)
    diag[0]+=wf
    ev,U=eigh_tridiagonal(diag,-Jf*np.ones(length-1))
    chi=np.pad(initial,(0,length-Nf))
    return U@(np.exp(-1j*ev*t)*(U.T@chi))

rows=[]
for t in (0,5,10,20):
    finite=evolution(Mf,t)
    long=evolution(Lf,t)
    actual=float(np.linalg.norm(long-np.pad(finite,(0,Lf-Mf))))
    x=rhof*t
    finite_bessel_sum=4*float(np.sum(np.abs(jv(np.arange(dMf,300),x))))
    contour=4*math.exp(-mu*dMf+x*math.sinh(mu))/(1-math.exp(-mu))
    rows.append({'t':t,'finite_vs_length128_error':actual,'bessel_tail_through_299':finite_bessel_sum,'contour_bound':contour})
    assert actual<=contour+2e-13
emit('finite_horizon_example',{'J':Jf,'w':wf,'rho':rhof,'N':Nf,'M':Mf,'L_reference':Lf,
    'd_M':dMf,'mu':mu,'Tobs':Tobs,'zeta':zeta,'required_real_distance':threshold,
    'A5_satisfied':dMf>=threshold,'rows':rows,
    'limit':'The length-128 reference and Bessel-tail truncation are diagnostic, not a certified infinite evolution.'})
assert dMf>=threshold

# Evaluate integer choices only; the large states for the sufficient gate
# schedule are deliberately not constructed or numerically evolved.
schedule=[]
for epsilon,eta_p,zeta in ((1.0,0.5,0.1),(0.5,0.25,0.01),(0.1,0.1,0.01)):
    sig=3*epsilon/68
    F0=math.sqrt(15*sig)/3
    F1=math.sqrt(15)/(2*math.sqrt(sig))
    CA=F1+2/math.sqrt(3)*F0
    CB=F1+(11/3+2/math.sqrt(3))*F0
    v=math.sqrt(3)*Jf
    T=max(1/v,16*(CA+CB)**2/(math.pi*v*epsilon**2))
    required=max(1,2*Jf*T,16*(F1+F0)**2/(math.pi*eta_p**2))
    cutoff=math.ceil(2*Jf*T+required)
    gap=cutoff-2*Jf*T
    tail=(F1+F0)/math.sqrt(math.pi*gap)
    horizon=2*T
    distance=(rhof*horizon*math.sinh(1)+math.log(4/((1-math.exp(-1))*zeta)))
    sites=max(cutoff,cutoff-1+math.ceil(distance))
    horizon_bound=4*math.exp(-(sites-cutoff+1)+rhof*horizon*math.sinh(1))/(1-math.exp(-1))
    schedule.append({'epsilon':epsilon,'eta_p':eta_p,'zeta':zeta,'J':Jf,
        'T':T,'N':cutoff,'d':gap,'A1_tail_bound':tail,'eta_p_divided_by_four':eta_p/4,
        'Tobs':horizon,'M':sites,'integer_distance':sites-cutoff+1,
        'required_distance':distance,'A4_horizon_bound':horizon_bound})
    assert tail<=eta_p/4*(1+1e-13)
    assert gap>=max(1,2*Jf*T)
    assert horizon_bound<=zeta*(1+1e-8)
emit('sufficient_integer_choices_not_evolved',schedule)
emit('completion',{'elapsed_seconds':time.monotonic()-start,
    'ru_maxrss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
(ROOT/'ADDENDUM_RESULTS.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
