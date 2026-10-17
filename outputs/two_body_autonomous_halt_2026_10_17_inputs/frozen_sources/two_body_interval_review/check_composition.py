#!/usr/bin/env python3
"""Bounded independent check of the frozen old-cap interval composition.

No author program is imported or run. Reuses the earlier reviewer-owned,
full-physical-basis rational witnesses by hash; certifies their inverse with
a new Frobenius/spectral argument, rather than the author's parity row sums.
All asserted arithmetic is Fraction or SymPy exact arithmetic. No fit, grid,
large-clock allocation, floating enclosure or wavepacket evolution is used.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt, factorial
import hashlib
import json
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
START = time.monotonic()
ROOT = Path(__file__).resolve().parent
import numpy as np
import sympy as sp

def number(x):
    return {'rational':str(x), 'approximate_float':float(x)}

def read(rel):
    return json.loads((ROOT/rel).read_text())

pins = read('SOURCE_PINS.json')
for row in pins['sources']:
    b = (ROOT/row['snapshot_path']).read_bytes()
    assert len(b) == row['bytes']
    assert hashlib.sha256(b).hexdigest() == row['sha256']

prior = read('sources/prior_review/WITNESS.json')
prior_result = read('sources/prior_review/RESULTS.json')
candidate = read('sources/candidate/CERTIFICATE.json')
author_witnesses = read('sources/candidate/POINT_WITNESSES.json')
P = {k:Q(v) for k,v in prior['exact_parameters'].items()}
assert P == {k:Q(v) for k,v in candidate['exact_parameters'].items()}
frozen_point = read('sources/candidate/inputs/rational_point_certificate.json')
assert P == {k:Q(v) for k,v in frozen_point['exact_parameters'].items()}
assert Q(candidate['central_bound']['rational']) == Q(frozen_point['certified_point_isometry_error']['rational'])
assert Q(prior_result['certified_point_error']['rational']) < Q(176,10**15)
J, co, si = (P[k] for k in ('J','cos_k','sin_k'))
q = P['tan_half_complement']
assert co == (q*q-1)/(q*q+1) and si == 2*q/(q*q+1)

def zeros(n,m=None):
    return np.full((n,n if m is None else m),Q(0),dtype=object)

def eye(n):
    a=zeros(n)
    for i in range(n): a[i,i]=Q(1)
    return a

def mat(data):
    return np.array([[Q(x) for x in row] for row in data],dtype=object)

def row_norm(a):
    return max(sum(abs(v) for v in row) for row in a)

def frob2(re,im=None):
    out=sum((v*v for v in re.flat),Q(0))
    return out if im is None else out+sum((v*v for v in im.flat),Q(0))

# Reassemble physical old1,old2,A,B order by bit actions. This is neither the
# author's source-first parity construction nor an eigendecomposition.
B=zeros(16); VA=zeros(16); VB=zeros(16); parity=zeros(16)
for state in range(16):
    o1,o2,a,b=((state>>shift)&1 for shift in (3,2,1,0))
    B[state,state]=2+(1-2*o1)*(1-2*o2)+P['DeltaA']*a+P['DeltaB']*b+P['t']*(a+b)+P['u']*a*b+P['gA']*a+P['gB']*b
    if a != b: B[state^3,state]-=P['t']
    B[state^8,state]+=P['gA']*a
    B[state^4,state]+=P['gB']*b
    VA[state,state]=P['lambdaA']+P['mu0']; VA[state^2,state]=P['lambdaA']
    VB[state,state]=P['lambdaB']+P['mu1']; VB[state^1,state]=P['lambdaB']
    parity[state^12,state]=Q(1)
assert np.array_equal(B,B.T)
for a in (B,VA,VB): assert np.array_equal(a@parity,parity@a)
vac=[0,4,8,12]; exc=[x for x in range(16) if x not in vac]
for v in vac:
    expected=zeros(16,1);expected[v,0]=2+(1-2*((v>>3)&1))*(1-2*((v>>2)&1))
    assert np.array_equal(B[:,v:v+1],expected)

spectral_records=[]; alignment=[]
for witness in prior['certificates']:
    s=witness['s']; E=2+s+P['epsilon']
    D=B[np.ix_(exc,exc)]+(2*J-E)*eye(12)
    assert np.array_equal(D,mat(witness['D']))
    Shat=mat(witness['S_hat'])
    assert np.array_equal(Shat,Shat.T)
    dl=1+min(P['DeltaA'],P['DeltaB'])+2*J-E
    a=dl-2*J; b=dl-row_norm(Shat-D)
    assert a>0 and b>0
    root_res=row_norm(Shat@Shat-(D@D-4*J*J*eye(12)))
    root_error=root_res/(a+b)
    # This old independently proposed scalar root is an exact lower endpoint.
    dr=2-s+2*J-E; scalar_square=dr*dr-4*J*J
    scalar=Q(witness['scalar_sqrt_lower']); scalar_width=Q(1,10**60)
    assert scalar*scalar<=scalar_square<(scalar+scalar_width)**2
    Fr=zeros(16); Fi=zeros(16)
    Fr[np.ix_(exc,exc)]=-(D+Shat)/2
    open_states=[0,12] if s==1 else [4,8]
    for v in vac:
        if v in open_states: Fr[v,v]=-J*co;Fi[v,v]=J*si
        else: Fr[v,v]=-(dr+(1 if dr>0 else -1)*scalar)/2
    Mr=zeros(32);Mi=zeros(32)
    Mr[:16,:16]=(E-2*J)*eye(16)-B-VA
    Mr[:16,16:]=J*eye(16);Mr[16:,:16]=J*eye(16)
    Mr[16:,16:]=Fr-VB;Mi[16:,16:]=Fi
    assert np.array_equal(Mr,mat(witness['M_hat_real']))
    assert np.array_equal(Mi,mat(witness['M_hat_imag']))
    Nr=mat(witness['N_real']);Ni=mat(witness['N_imag'])
    Er=eye(32)-(Mr@Nr-Mi@Ni);Ei=-(Mr@Ni+Mi@Nr)
    n2=frob2(Nr,Ni); e2=frob2(Er,Ei)
    # New proof: ||N||_2 <= ||N||_F <119; ||I-Mhat N||_2<10^-54.
    # Source root error is spectral, so the physical M error is <=root/2.
    # No dimension conversion and no complex-symmetry row/column argument.
    n_bound=Q(119); e_bound=Q(1,10**54)
    assert n2<n_bound*n_bound and e2<e_bound*e_bound
    delta=max(root_error/2,scalar_width/2)
    total_residual=e_bound+delta*n_bound
    inv_bound=n_bound/(1-total_residual)
    assert total_residual<1 and inv_bound<120
    spectral_records.append({'s':s,'inverse_candidate_Frobenius_squared':number(n2),
        'inverse_residual_Frobenius_squared':number(e2),'exact_root_residual_row_bound':number(root_res),
        'exact_root_spectral_error':number(root_error),'matching_spectral_error':number(delta),
        'true_full_32_inverse_spectral_upper':number(inv_bound)})
    # Compare the frozen author's four serialized 16-dimensional proposals
    # with an exact unitary compression of the earlier independent full basis.
    for p in (1,-1):
        U=zeros(32,16)
        for site in (0,1):
            for ab in range(4):
                col=8*site+2*ab
                U[16*site+ab,col]=1;U[16*site+12+ab,col]=p
                U[16*site+8+ab,col+1]=1;U[16*site+4+ab,col+1]=p
        assert np.array_equal(U.T@U,2*eye(16))
        old=next(w for w in author_witnesses if w['s']==s and w['p']==p)
        diff_re=U.T@Nr@U/2-mat(old['inverse_real'])
        diff_im=U.T@Ni@U/2-mat(old['inverse_imag'])
        difference=max(abs(x)+abs(y) for x,y in zip(diff_re.flat,diff_im.flat))
        assert difference<Q(1,10**50)
        assert mat(old['sqrt_source']).shape==(6,6)
        assert mat(old['state_real']).shape==(16,1) and mat(old['state_imag']).shape==(16,1)
        alignment.append({'s':s,'p':p,'maximum_entry_l1_difference':number(difference)})

# Independently derive rational interval constants, without reading displays.
w=Q(1,1000); kappa=Q(1,7); g=Q(9,50); eps=P['epsilon']
lo,hi=eps-2*J*w,eps+2*J*w
gap=min(P['DeltaA'],P['DeltaB'])-2-hi
other_gap=2-4*J
assert 0<lo<hi<4*J and si>w and min(gap,other_gap)>g
assert (2+g/J)*kappa>1+kappa*kappa
L16=2*J/(1-kappa*kappa)
independent_center=max(Q(r['true_full_32_inverse_spectral_upper']['rational']) for r in spectral_records)
independent_uniform=independent_center/(1-independent_center*L16*w)
assert independent_center*L16*w<1 and independent_uniform<121
author_uniform=Q(164)/(1-164*L16*w)
assert author_uniform==Q(candidate['matching']['interval_M16_inverse_2_upper']['rational']) and author_uniform<166
assert L16==Q(candidate['matching']['M16_derivative_2_upper']['rational'])
assert gap==Q(candidate['interval']['source_gap_lower']['rational'])
assert lo==Q(candidate['interval']['epsilon_lower']['rational']) and hi==Q(candidate['interval']['epsilon_upper']['rational'])
assert Q(332)+1/J<366
assert 2*J*(si-w)>Q(1,40)

# Exact all-RHS Schur reconstruction in a three-channel test containing
# positive and negative evanescent roots. This is separate from the general
# dimension-free block proof in REVIEW.md. Wrong reconstruction sign fails.
z=sp.Rational(3,5)+sp.I*sp.Rational(4,5); jt=sp.Rational(3,100)
qs=[sp.Rational(1,7),-sp.Rational(1,8)]
energy=1+2*jt-jt*(z+1/z)
bt=sp.diag(1,*[energy-2*jt+jt*(q+1/q) for q in qs])
vt0=sp.Matrix([[1,2,0],[2,4,1],[0,1,3]])/11
vt1=sp.Matrix([[0,1,2],[1,-1,0],[2,0,1]])/13
eye3=sp.eye(3); Amap=sp.diag(z,*[1/q for q in qs]); Emap=sp.diag(z*z,1,1)
Qlead=sp.diag(z,*qs); F=sp.diag(-jt/z,*[-jt/q for q in qs])
D0=2*jt*eye3+bt+vt0-energy*eye3;D1=2*jt*eye3+bt+vt1-energy*eye3
M6=sp.BlockMatrix([[ -D0,jt*eye3],[jt*eye3,F-vt1]]).as_explicit()
M9=sp.BlockMatrix([[D0,-jt*eye3,sp.zeros(3)],[-jt*eye3,D1,-jt*Emap],[sp.zeros(3),-jt*eye3,jt*Amap]]).as_explicit()
inv6=M6.inv(); Ain=Amap.inv(); constructed=sp.zeros(9)
for j in range(9):
    f=sp.eye(9)[:,j]; f0=f[:3,0];f1=f[3:6,0];f2=f[6:9,0]
    x=inv6*(-f0).col_join(-(f1+Qlead*f2))
    y=Ain*x[3:6,0]+Ain*f2/jt
    constructed[:,j]=x.col_join(y)
residual=(M9*constructed-sp.eye(9)).applyfunc(sp.simplify)
assert residual==sp.zeros(9)
wrong=constructed.copy()
# On RHS f2=e0, replace +J^-1 A^-1 f2 with its wrong negative sign.
wrong[6:9,6]=wrong[6:9,6]-2*Ain[:,0]/jt
wrong_residual=(M9*wrong-sp.eye(9)).applyfunc(sp.simplify)
assert wrong_residual!=sp.zeros(9) and wrong_residual[6,6]==-2

# Reflection phases independently checked by the hard-wall condition at -1.
# Incoming site-1 wave at -1 is z^2; reflected term is r*z^-2.
r1=-z**4; rabs=-z**2
assert sp.simplify(z*z+r1/z**2)==0
alpha=sp.Rational(3,5)-sp.I*sp.Rational(4,5)
zeta=-alpha/z**4
assert sp.simplify(rabs*zeta-alpha/z**2)==0
wrong_phase=sp.simplify(rabs*alpha-alpha/z**2)
assert wrong_phase!=0

# Reconstruct packet derivatives and all finite resources using alternative
# integral values/squared inequalities. All inputs below are rational.
v=Q(1,40); E2=2*J; sig=Q(1,10**6); T=10**13
# Integrating (1-x^2)^2 gives16/15; integrating1-x^2 gives4/3;
# integral|(-2x)| is2. These yield the following squared norms.
x=sp.symbols('x',real=True)
assert sp.integrate((1-x*x)**2,(x,-1,1))==sp.Rational(16,15)
assert sp.integrate(1-x*x,(x,-1,1))==sp.Rational(4,3)
assert 2*sp.integrate(2*x,(x,0,1))==2
F0,F1=Q(1,750),Q(2000)
assert 15*sig/9<F0*F0 and 15/(4*sig)<F1*F1
assert E2/v<Q(5,2)
nu=Q(1,366); X0=Q(16);X1=Q(700)
# Use sqrt(5)<224/100 and sqrt(9+4/(1-kappa²)²)<366/100
# instead of the author's9/4 bound and0.11 intermediate ceiling.
assert Q(224,100)**2>5
assert Q(366,100)**2>9+4/(1-kappa*kappa)**2
lm=J*Q(366,100)
assert lm<Q(11,100) and 2*J*J<(X0*nu)**2
assert (Q(224,100)*J+lm*X0)/nu<X1
c0sq=2*(X0+2)**2+X0*X0/(1-kappa*kappa)
assert c0sq<31**2
finite_derivative=Q(1982);closed_derivative=Q(708);root_derivative=Q(7,10)
assert (2*X1)**2+(2*X1+2)**2<finite_derivative**2
assert X1*X1/(1-kappa*kappa)<closed_derivative**2
Q1=2*kappa*kappa/(1-kappa*kappa)
assert X0*X0*Q1*Q1*(1+kappa*kappa)/(1-kappa*kappa)**3<root_derivative**2
assert finite_derivative+closed_derivative+root_derivative<2700
CA=CB=Q(2001);C0=Q(31);C1=Q(2700);D=Q(88000)
assert F1+E2/v*F0<CA and F1+(X1+E2/v)*F0<CB
Dj=F1*C0+F0*C1+Q(5,2)*F0*C0
assert 2*Dj*Dj<D*D
delta=Q(176,10**15)+(X1+2)*sig
sqrt_pi_vt_lower=Q(866000);sqrt_2pi_lower=Q(12,5)
assert sqrt_pi_vt_lower**2<3*v*T and sqrt_2pi_lower**2<6
din=CB/sqrt_pi_vt_lower+D/(sqrt_2pi_lower*v*T)
joint=delta+2*(CA+CB)/sqrt_pi_vt_lower+3*D/(sqrt_2pi_lower*v*T)
assert din<Q(1,4) and CA/sqrt_pi_vt_lower<Q(1,4)
eta=Q(1,1000);N=22*10**12;M=9*10**14;Tobs=4*T
d=N-2*J*T
assert d>=1 and d>=2*J*T and 3*eta*eta*d>=16*(F1+F0)**2
assert joint+eta<Q(11,1000) and joint+2*eta<Q(12,1000)
assert 2*din+eta<Q(5622,10**6)
Bupper=3+P['DeltaA']+P['DeltaB']+2*P['t']+P['u']+2*P['gA']+2*P['gB']
Vmax=max(2*P['lambdaA']+P['mu0'],abs(P['mu1']),abs(2*P['lambdaB']+P['mu1']))
rho=Q(18)
assert Bupper<20 and 2*J+Q(19,2)+Vmax<rho
# Independent elementary exp bounds from six Taylor terms and remaining
# factorial ratios <=1/7. A rational lower bound yields e^9>target.
e_lo=sum((Q(1,factorial(k)) for k in range(6)),Q(0))
e_hi=e_lo+Q(1,factorial(6))/(1-Q(1,7))
assert Q(8,3)<e_lo<e_hi<Q(11,4)
sinh_hi=(e_hi-1/e_hi)/2
assert sinh_hi<Q(6,5)
log_target_hi=4/((1-1/e_lo)*eta)
assert log_target_hi<e_lo**9
distance=M-N+1
assert distance>rho*Tobs*sinh_hi+9
assert distance>rho*Tobs*Q(6,5)+9

recomputed={'delta_in_upper':din,'infinite_untruncated_isometry_upper':joint,
    'infinite_finite_preparation_isometry_upper':joint+eta,
    'infinite_bound_state_amplitude_upper':2*din+eta,'Delta_upper':delta,'Dj_upper':Dj}
for k,value in recomputed.items(): assert value==Q(candidate['packet'][k]['rational'])
assert joint+2*eta==Q(candidate['finite_horizon']['complete_isometry_upper']['rational'])
assert 2*(joint+2*eta)==Q(candidate['finite_horizon']['complete_unhalved_trace_upper']['rational'])

output={'status':'All exact arithmetic checks completed; conditional composition scope only',
 'independent_path':'Prior independent full32 Newton witnesses, newly certified by exact Frobenius/spectral residuals; exact all-RHS signed Schur toy; independent scalar/integral inequalities',
 'author_program_imported_or_executed':False,'source_exposure':'Same model; candidate and author code read before check; prior reviewer matrices reused by immutable identity',
 'inverse_records':spectral_records,'author_witness_alignment':alignment,
 'interval':{'source_gap_lower':number(gap),'other_old_band_gap_lower':number(other_gap),
     'root_kappa_upper':str(kappa),'M16_derivative_upper':number(L16),
     'independent_full32_interval_inverse_upper':number(independent_uniform),
     'candidate_M16_inverse_upper':number(author_uniform),'candidate_M24_inverse_upper':number(Q(332)+1/J)},
 'schur_test':{'dimensions':[6,9],'closed_roots':[str(v) for v in qs],
     'all_RHS_identity_exact':True,'wrong_reconstruction_sign_residual_entry':str(wrong_residual[6,6]),
     'wrong_phase_residual':str(wrong_phase)},
 'packet':{k:number(v) for k,v in recomputed.items()},
 'finite_resources':{'preparation_support_sites':N,'clock_sites':M,'all_future_start':2*T,
     'finite_horizon_end':Tobs,'hop_distance':distance,'preparation_inequality_margin':number(d-16*(F1+F0)**2/(3*eta*eta)),
     'B_spectral_upper_by_block_norms':number(Bupper),'Vmax':number(Vmax),'rho':str(rho),
     'boundary_exponent_margin_using_6_over_5':number(distance-rho*Tobs*Q(6,5)-9),
     'finite_complete_isometry_upper':number(joint+2*eta),'finite_complete_trace_upper':number(2*(joint+2*eta))},
 'limits':{'no_search':True,'no_grid':True,'no_clock_state_allocation':True,'no_time_evolution':True,
     'arbitrary_accuracy_claimed':False,'native_preparation_claimed':False,'formal_audit_claimed':False},
 'runtime':{'cpu_seconds_cap':60,'parent_wall_seconds_cap':90,'largest_matrix_dimension':32,
     'symbolic_schur_dimension':9,'square_root_dimension':12,'python':sys.version,
     'numpy':np.__version__,'sympy':sp.__version__,'platform':platform.platform(),
     'elapsed_seconds_after_limits':time.monotonic()-START}}
(ROOT/'RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':output['status'],
    'inverse_center_Frobenius_bound':float(independent_center),
    'independent_uniform_inverse_bound':float(independent_uniform),
    'source_gap_lower':float(gap),'infinite_error':float(joint+eta),
    'finite_error':float(joint+2*eta),'elapsed_seconds':output['runtime']['elapsed_seconds_after_limits']},indent=2))
