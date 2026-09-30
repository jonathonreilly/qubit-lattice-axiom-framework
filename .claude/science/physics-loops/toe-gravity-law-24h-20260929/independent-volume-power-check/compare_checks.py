"""Post-PRE independent controls of the root proof; no root code imported.
Cubic geometry + exact constants + a labeled generic masked-rotor algebra fixture.
Price<=30 CPU seconds/150MB including prior subsecond local geometry, BLAS1.
"""
from pathlib import Path
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import hashlib,json,math,resource,time
from fractions import Fraction
from itertools import product
import numpy as np
started=time.process_time();here=Path(__file__).resolve().parent
report=here.parent/'original-record-volume-power/REPORT.md'
assert hashlib.sha256(report.read_bytes()).hexdigest()=='1584fa986313ddd94f745508c6bd461fe9f267bf9a7d346c0fd69fbbd5198f2e'
b=lambda u,s:(2*s+1)*(s+1)**u
assert (b(4,2),b(4,4),b(2,2),b(2,4),b(2,8))==(405,5625,45,225,1377)
assert 2*b(4,4)==11250 and b(4,2)**2+b(4,4)==169650
assert 2*b(2,2)+1+b(2,4)==316
assert 2*(1+b(2,8))==2756 and 1+b(2,4)==226
assert b(2,2)+Fraction(1+b(2,4),2)==158
zero=(0,0,0);norm=lambda x:sum(abs(t) for t in x)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
def ball(r):return {x for x in product(range(-r,r+1),repeat=3) if norm(x)<=r}
steps=ball(1)-{zero};partners={x for x in ball(2) if norm(x)==2}
star=lambda a:{a}|{add(a,s) for s in steps}
active={zero}|partners
current_pairs={tuple(sorted((a,add(a,d)))) for a in active for d in partners}
current_sites=set().union(*(star(a)|star(c) for a,c in current_pairs))
near_centers={a for a in ball(6) if sum(a)%2==0 and star(a)&current_sites}
near_pairs={tuple(sorted((a,add(a,d)))) for a in near_centers for d in partners}
all_centers={a for pair in near_pairs for a in pair}
all_sites=set().union(*(star(a)|star(c) for a,c in near_pairs))
assert len(current_pairs)==264<=342
assert max(map(norm,near_centers))==6 and max(map(norm,all_centers))==8
assert max(map(norm,all_sites))==9
assert len(near_pairs)<=18*13**3 and len(near_centers)<=13**3
assert all(max(map(abs,bsite))<=9 for bsite in all_sites if sum(bsite)%2)
# All exact unit-parameter root constants and comparison with frozen PRE.
vS=18*21**3*2592;gS=21**3*600;C8=11250*vS+169650*gS
v0=342*2592;P0=600*(316+2*v0);v1=18*13**3*2592;g1=13**3*600
Ccur=P0*(2756+226*v1+158*g1);p0=123744
root_t=min(Fraction(1,C8),Fraction(p0,4*Ccur))
pre_t=Fraction(1289,5516759566540800)
# Generic finite algebra fixture only; not an original-law torus or power witness.
R=3;fields=np.arange(-R,R+1);d=len(fields);shift=np.diag(np.ones(d-1),-1)
I=np.eye(2*d);I2=np.eye(2);vac=np.diag([1.,0.]);raise_m=np.array([[0.,0.],[1.,0.]])
Q=np.kron(I2,np.diag(1+abs(fields)));D=np.kron(vac,np.diag(fields**2))
A=np.kron(I2,shift+shift.T);L=np.kron(raise_m,shift);Gamma=L.T@L;h=D+A
opnorm=lambda x:float(np.linalg.norm(x,2))
def adjoint(O,loss=Gamma):return 1j*(h@O-O@h)+L.T@O@L-(loss@O+O@loss)/2
P=adjoint(h);LP=adjoint(P);v=opnorm(A);g=opnorm(L)**2
pbound=g*(316+2*v);cbound=pbound*(2756+226*v+158*g)
Qm2=np.diag(np.diag(Q)**-2);Qm4=np.diag(np.diag(Q)**-4)
actualP=opnorm(P@Qm2);actualLP=opnorm(LP@Qm4)
assert actualP<=pbound and actualLP<=cbound
form=Qm4@adjoint(np.linalg.matrix_power(Q,8))@Qm4
form=(form+form.conj().T)/2
actualC8=float(np.max(np.linalg.eigvalsh(form)));boundC8=11250*v+169650*g
assert actualC8<=boundC8
assert opnorm(adjoint(I))<1e-13
# Compressing the infinite Gamma instead of forming L_R^*L_R loses trace.
wrong_Gamma=np.kron(vac,np.eye(d));wrong_identity=opnorm(adjoint(I,wrong_Gamma))
assert abs(wrong_identity-1)<1e-13
# An energy-derived weight loses the finite-band property when links are masked.
Ein=2;Eout=Ein+1
masked_weight_change=abs((1+0*Eout**2)-(1+1*Ein**2))
true_weight_change=abs((1+abs(Eout))-(1+abs(Ein)))
assert masked_weight_change>2 and true_weight_change<=2
results={'checked_root_report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),'geometry':{'current_pairs':len(current_pairs),'root_bound342_valid':True,'near_centers':len(near_centers),'near_magnetic_pairs':len(near_pairs),'max_center_radius':6,'max_other_center_radius':8,'max_star_radius':9,'S_cube9_contains_all_needed_field_endpoints':True},'unit_root_constants':{'vS':vS,'gS':gS,'C8':C8,'v0':v0,'P0':P0,'v1':v1,'g1':g1,'Ccur':Ccur,'t0_exact':str(root_t),'t0_float':float(root_t),'independent_PRE_interval_ratio':str(pre_t/root_t),'ratio_float':float(pre_t/root_t)},'generic_masked_rotor_fixture':{'scope':'14-dimensional algebra diagnostic, not original-law numerical validation','dimension':2*d,'relative_current_norm':actualP,'current_bound':pbound,'relative_current_derivative_norm':actualLP,'derivative_bound':cbound,'Q8_generator_form_max_eigenvalue':actualC8,'moment_bound':boundC8,'wrong_loss_identity_defect':wrong_identity,'masked_energy_weight_band_change':masked_weight_change,'actual_all_field_weight_band_change':true_weight_change},'cpu_seconds':time.process_time()-started,'ru_maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert results['cpu_seconds']<30 and results['ru_maxrss_bytes']<150*1024**2
(here/'COMPARISON_CHECK_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
