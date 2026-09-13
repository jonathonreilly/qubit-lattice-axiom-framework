"""Exact rank-two metric and small Gaussian checks; no native alpha calculation."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time
import numpy as np
import sympy as s
start=time.perf_counter(); checks=[]; data={}
def req(name,p):
    if not p:raise AssertionError(name)
    checks.append(name)
def eq(name,A,B):req(name,all(s.simplify(x)==0 for x in A-B) if isinstance(A,s.MatrixBase) else s.simplify(A-B)==0)

# Unchanged source N32 positive-count upper bound, sharper rational comparison.
partial=sum((F(comb(4*n,2*n),4**(2*n))*F(comb(2*n,n)*sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1)),6**(2*n)) for n in range(33)),F(0))
metric=F(1000,2449)*partial+F(1,192)
req('same_N32_below_23_over50',metric<F(23,50))
req('no_unproved_9_over20_substitution',metric>F(9,20))
p2=F(529,1250);c=F(1,3);k2=(p2-c*c)/((1-c)**2-p2)
req('opposite_geometry_covered',F(23,60)<p2)
req('exact_relative_metric',k2==F(3511,239))
req('rational_relative_bound',k2<F(31,8)**2)
r=F(7,9);q=r*r
req('positive_Lyapunov_margin',2*r-F(31,8)*(1-r*r)==F(2,81))
req('two_field_bound8',(1+r)/(1-r)==8)
req('four_field_bound192',3*((1+r)/(1-r))**2==192)
req('trace_norm_below111',29**2*130<111**2*9)
req('HS_square_below86',203**2*130<86**2*27**2)
logfloor=F(86,2)+F(86,2)/(1-q)
req('mixed_overlap_exponent',logfloor==F(4859,32)<152)
data['native_scalar_bound']={'N':32,'summands':33,'exact_upper':str(metric),
    'upper_decimal_for_display':float(metric),'relative_k_squared':str(k2),
    'r':'7/9','physical_C0_or_alpha_evaluated':False}

# Noncommuting S and rank-two metric, exact under congruence.
a=s.Matrix([1,0]);d=s.Matrix([s.Rational(1,3),s.Rational(1,2)])
M=s.eye(2)-a*d.T-d*a.T;N=a*d.T-d*a.T
rootS=s.diag(1,3);Hs=rootS*M*rootS;Ks=rootS*N*rootS
eq('ranktwo_metric_saturated',N.T*M.inv()*N,3*M)
eq('congruence_metric_saturated',Ks.T*Hs.inv()*Ks,3*Hs)
req('S_and_Hs_do_not_commute',Hs*rootS**2!=rootS**2*Hs)
req('separate_operator_modulus_not_used',Hs.det()>0)
dd=s.Matrix([s.Rational(1,3),s.sqrt(s.Rational(3511,11250))])
MM=s.eye(2)-a*dd.T-dd*a.T;NN=a*dd.T-dd*a.T
eq('worst_allowed_ranktwo_ratio',NN.T*MM.inv()*NN,s.Rational(3511,239)*MM)
req('too_small_relative_constant_rejected',(9*MM-NN.T*MM.inv()*NN)[0,0]<0)

# Lyapunov identity with independent noncommuting real 4x4 inputs.
Hs4=s.Matrix([[4,1,0,1],[1,5,1,0],[0,1,6,1],[1,0,1,5]])
Ks4=s.Matrix([[0,1,2,0],[-1,0,1,1],[-2,-1,0,3],[0,-1,-3,0]])/7
ZZ=s.Matrix([[0,1,0,2],[-1,0,3,0],[0,-3,0,1],[-2,0,-1,0]])/11
rr=s.Rational(7,9);zp=-Ks4-Hs4*ZZ-ZZ*Hs4-ZZ*Ks4*ZZ
mm=rr**2*s.eye(4)+ZZ**2;aa=Hs4+ZZ*Ks4
ff=2*rr**2*Hs4-2*ZZ*Hs4*ZZ-(1-rr**2)*(Ks4*ZZ+ZZ*Ks4)
eq('full_Lyapunov_identity',zp*ZZ+ZZ*zp,ff-aa*mm-mm*aa.T)
req('wrong_Riccati_creation_sign_rejected',
    (Ks4-Hs4*ZZ-ZZ*Hs4-ZZ*Ks4*ZZ)*ZZ+ZZ*(Ks4-Hs4*ZZ-ZZ*Hs4-ZZ*Ks4*ZZ)!=ff-aa*mm-mm*aa.T)

def block_graph(zs):
    z=s.zeros(2*len(zs))
    for j,x in enumerate(zs):z[2*j,2*j+1]=x;z[2*j+1,2*j]=-x
    return z
def rotation(n,i,j):
    O=s.eye(n);O[i,i]=O[j,j]=s.Rational(3,5);O[i,j]=s.Rational(4,5);O[j,i]=-s.Rational(4,5)
    return O
def projector(z):
    n=z.rows;w=s.eye(n).row_join(-z)
    return w.T*(s.eye(n)+z*z.T).inv()*w
def arr(a):return np.array(a,dtype=float)
def sv(a):return np.linalg.svd(arr(a),compute_uv=False)
def ref_graph(zt,z0,A):return A*(zt-z0)*(s.eye(z0.rows)-z0*zt).inv()*A.inv()

# Exact rank doubling under a positive contraction, no time stepping.
z0=block_graph([s.Rational(3,4),0]);A=s.diag(s.Rational(4,5),s.Rational(4,5),1,1)
O=rotation(4,0,2)*rotation(4,1,3)
U=O*s.diag(s.Rational(9,10),s.Rational(4,5),s.Rational(2,5),s.Rational(3,10))*O.T
zt=U*z0*U.T;zr=ref_graph(zt,z0,A)
P0=projector(z0);Pt=projector(zt);PA=s.diag(1,1,1,1,0,0,0,0)
eq('reference_chart_skew',zr+zr.T,s.zeros(4))
req('initial_projection_difference_rank4',(P0-PA).rank()==4)
req('actual_reference_difference_rank8',(Pt-P0).rank()==8)
req('initial_mode_support_is_not_preserved',zr[2,3]!=0)
eq('pure_P0_projector',P0*P0,P0);eq('pure_Pt_projector',Pt*Pt,Pt)

# Independent literal four-mode Fock annihilator identity for that graph transform.
I=s.I;X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1);eye2=s.eye(2)
fs=[]
for j in range(4):fs.append(s.kronecker_product(*([Z]*j+[(X+I*Y)/2]+[eye2]*(3-j))))
vac=s.zeros(16,1);vac[0]=1
def state(z):
    pair=sum((z[i,j]*fs[i].conjugate().T*fs[j].conjugate().T for i in range(4) for j in range(i+1,4)),s.zeros(16))
    return vac+pair*vac+pair*pair*vac/2
v0=state(z0);vt=state(zt)
fref=[A[i,i]*(fs[i]-sum((z0[i,j]*fs[j].conjugate().T for j in range(4)),s.zeros(16))) for i in range(4)]
for i in range(4):
    eq('literal_original_vacuum_annihilator_'+str(i),fref[i]*v0,s.zeros(16,1))
    eq('literal_moving_reference_graph_'+str(i),fref[i]*vt,
       sum((zr[i,j]*fref[j].conjugate().T*vt for j in range(4)),s.zeros(16,1)))
bad=(zt-z0)*(s.eye(4)-z0*zt).inv()
req('missing_frame_congruence_rejected',bad!=zr)
data['rank_doubling']={'complex_modes':4,'initial_projection_rank':4,'later_reference_projection_rank':8,
    'literal_Fock_dimension':16,'scope':'synthetic positive contraction, not native evolution'}

# Nontrivial tail/fidelity check on eight complex modes, one-particle matrices only.
zs=[s.Rational(3,4),s.Rational(19,180),s.Rational(39,760),s.Rational(79,3120)]
z0=block_graph(zs);A=s.diag(*[v for v in (s.Rational(4,5),s.Rational(180,181),s.Rational(760,761),s.Rational(3120,3121)) for _ in range(2)])
O=rotation(8,0,4)*rotation(8,1,5)*rotation(8,2,6)*rotation(8,3,7)*rotation(8,0,2)
U=O*s.diag(1,s.Rational(9,10),s.Rational(4,5),s.Rational(3,4),s.Rational(2,3),s.Rational(1,2),s.Rational(1,3),s.Rational(1,4))*O.T
zt=U*z0*U.T;zr=ref_graph(zt,z0,A)
P0=projector(z0);Pt=projector(zt);PA=s.diag(*([1]*8+[0]*8))
sstat=sv(P0-PA);simp=sv(Pt-PA);sref=sv(Pt-P0)
req('all_singular_values_contract',np.max(simp-sstat)<2e-13)
req('trace_triangle_bound',sref.sum()<=2*sstat.sum()+2e-13)
zz=sv(zr);req('reference_trace_graph_formula',abs(sref.sum()-2*np.sum(zz/np.sqrt(1+zz*zz)))<3e-13)
eta=4*(F(19,181)+F(39,761)+F(79,3121));k=4
req('stationary_exact_tail_eta_below1',0<eta<1)
req('stationary_rank4_tail',abs(sstat[k:].sum()-float(eta))<3e-13)
req('moving_rank8_tail_bound',sref[2*k:].sum()<=2*float(eta)+3e-13)
# Every paired graph singular value occurs twice; retain two paired blocks.
pairz=zz[::2];discard=pairz[2:];cost=np.sqrt(2*(1-np.prod(1/np.sqrt(1+discard*discard))))
req('nontrivial_discarded_pairing',cost>1e-6)
req('normalized_Fock_tail_bound',cost<float(eta)/np.sqrt(2))
req('complete_pair_multiplicity',max(abs(zz[::2]-zz[1::2]))<2e-13)
data['normalized_tail']={'complex_modes':8,'Fock_matrix_constructed':False,'k':k,
    'eta_exact':str(eta),'eta':float(eta),'actual_paired_Fock_error':float(cost),
    'proved_error_bound':float(eta)/np.sqrt(2),'ref_projection_tail':float(sref[8:].sum()),
    'scope':'small rational Gaussian fixture, float SVD cross-check only'}
out={'scope':'same-agent exact metric and finite Gaussian support; no native alpha, phase, or actual propagation',
     'checks':checks,'check_groups':len(checks),'data':data,'seconds':time.perf_counter()-start}
Path(__file__).with_name('BLOCK06_CHART_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('scope','check_groups','data','seconds')},indent=2))
