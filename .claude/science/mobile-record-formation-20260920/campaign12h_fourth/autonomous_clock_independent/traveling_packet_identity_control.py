#!/usr/bin/env python3
"""Independent post-PRE reconstruction of the new traveling-clock identities.
No author implementation is imported. Exact endpoint residuals, finite-path
commutators/powers, Bessel propagation, and positive resources are checked.
"""
from pathlib import Path
import json,math
import sympy as s
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.special import jv
HERE=Path(__file__).resolve().parent
simp=lambda M:M.applyfunc(s.simplify)
exact=[]
for w in (2,3,5,7,11):
 theta=s.pi/(w+1);xs=list(range(-w-3,4));d=len(xs);idx={x:i for i,x in enumerate(xs)}
 chi=s.zeros(d,1)
 for x in range(-w,0):chi[idx[x]]=s.I**x*s.sqrt(s.Rational(2,w+1))*s.sin(theta*(x+w+1))
 shift=s.zeros(d)
 for i in range(d-1):shift[i+1,i]=1
 X=s.diag(*xs);V=s.I*(shift-shift.T);K=2*s.eye(d)-shift-shift.T
 mu=2*s.cos(theta);res=simp(V*chi-mu*chi)
 interior=[x for x in xs if res[idx[x]]!=0]
 assert interior==[-w-1,0],(w,interior)
 endpoint=s.zeros(d,1)
 amp=s.sqrt(s.Rational(2,w+1))*s.sin(theta)
 endpoint[idx[-w-1]]=s.I**(-w-1)*amp
 endpoint[idx[0]]=amp
 assert simp(res-endpoint)==s.zeros(d,1)
 var=s.simplify((res.conjugate().T*res)[0])
 assert s.simplify(var-4*s.sin(theta)**2/(w+1))==0
 a=[s.sqrt(s.Rational(2,w+1))*s.sin(theta*j) for j in range(1,w+1)]
 hop2=s.simplify(sum(a[j]*a[j+2] for j in range(w-2)))
 assert s.simplify(hop2-s.cos(2*theta)-2*s.sin(theta)**2/(w+1))==0
 assert s.simplify((chi.conjugate().T*X*chi)[0]+s.Rational(w+1,2))==0
 assert s.simplify((chi.conjugate().T*V*chi)[0]-mu)==0
 # Boundary forces are genuinely present on a finite path. The linear
 # Heisenberg position law is used only on the infinite chain in the proof.
 pmax=s.zeros(d);pmax[-1,-1]=1;pmin=s.zeros(d);pmin[0,0]=1
 assert simp(K*V-V*K-2*s.I*(pmax-pmin))==s.zeros(d)
 assert K*V-V*K!=s.zeros(d)
 # Positive finite clock ground removal and preparation variance. Packet is
 # far enough from the finite boundary that this moment has no edge loss.
 em=s.pi/(d+1);E0=2*(1-s.cos(em));HC=K-E0*s.eye(d)
 mean=s.simplify((chi.conjugate().T*HC*chi)[0])
 assert s.simplify(mean-2*s.cos(em))==0
 second=s.simplify((chi.conjugate().T*HC*HC*chi)[0])
 energy_var=s.simplify(second-mean**2)
 assert s.simplify(energy_var-4*w*s.sin(theta)**2/(w+1))==0
 exact.append({'w':w,'velocity_residual_support':interior,'velocity_variance_J1':str(var),'second_neighbor_overlap':str(hop2),'energy_mean_J1':str(mean),'energy_variance_J1':str(energy_var),'finite_velocity_commutator_is_boundary_force':True})
# Exact local walk powers: matching beyond the author's claimed <R orders,
# with a nonzero first outgoing path at order R+1.
power_rows=[]
for R in (1,2,4):
 w=3;n=2;left=-w-R;right=n+R;xs=list(range(left-R-4,right+R+5));ix={x:i for i,x in enumerate(xs)}
 d=len(xs);A=s.zeros(d);AM=s.zeros(d);chi=s.zeros(d,1)
 for x in xs[:-1]:
  A[ix[x+1],ix[x]]=A[ix[x],ix[x+1]]=1
  if left<=x and x+1<=right:AM[ix[x+1],ix[x]]=AM[ix[x],ix[x+1]]=1
 for x in range(-w,0):chi[ix[x]]=s.I**x*s.sqrt(s.Rational(2,w+1))*s.sin(s.pi*(x+w+1)/(w+1))
 v=chi;vm=chi;diffs=[]
 for order in range(R+2):
  diff=simp(v-vm);zero=diff==s.zeros(d,1);diffs.append(zero)
  if order<=R:assert zero
  else:assert not zero
  v=A*v;vm=AM*vm
 power_rows.append({'R':R,'orders_0_through_R_match':all(diffs[:-1]),'first_nonzero_order':R+1})
# Independent infinite-chain kernel, not a second finite propagation helper.
# exp(+i Jt A) has kernel i^(x-y) J_(x-y)(2Jt); scalar phases are removed.
bessel_rows=[]
w=3;n=1;horizon=1.;tau=horizon/n;theta=np.pi/(w+1);J=1/(2*tau*np.cos(theta));a=2*J*horizon
for R in (1,3,6,8,12):
 lo=-w-R;hi=n+R;xs=np.arange(lo,hi+1);d=len(xs)
 env=np.arange(-w,0);vals=(1j)**env*np.sqrt(2/(w+1))*np.sin(theta*(env+w+1))
 chi=np.zeros(d,complex);chi[env-lo]=vals
 adjacency=np.diag(np.ones(d-1),1)+np.diag(np.ones(d-1),-1)
 finite=expm(1j*J*horizon*adjacency)@chi
 outer=np.arange(lo-40,hi+41)
 infinite=sum(v*(1j)**(outer-y)*jv(outer-y,a) for y,v in zip(env,vals))
 embed=np.zeros(len(outer),complex);embed[xs-outer[0]]=finite
 observed=float(np.linalg.norm(embed-infinite))
 tail=min(2.,4*np.exp(a+R*np.log(a)-math.lgamma(R+1)))
 assert 2*observed<=tail+3e-12
 # Exact scalar phases of K and K-e0 only affect the phase alignment; no
 # artificial error caused by their different chosen energy zeros is counted.
 delta=float(np.dot(abs(tau*np.clip(xs,0,n)-horizon),abs(finite)**2))
 proved=tau*w+horizon*np.tan(theta)/np.sqrt(w+1)
 assert delta<=proved+horizon*tail+3e-12
 bessel_rows.append({'R':R,'finite_dimension':d,'finite_infinite_phase_aligned_vector_error_on_enlarged_window':observed,'proved_channel_tail_bound':tail,'finite_clipped_time_mismatch':delta,'infinite_uniform_time_bound':proved,'numerical_note':'The Bessel tail outside the extra 40 sites is far below working precision; exact Taylor/power argument, not this sample, proves the global bound.'})
# Preserve tiny positive tails as high-precision decimal strings, never zero.
mp.mp.dps=70
tails=[]
for w,n in ((3,3),(4,64),(8,256),(16,256),(8,256),(16,1024)):
 theta=mp.pi/(w+1);a=mp.mpf(n)/mp.cos(theta);R=int(mp.ceil(8*a));logtail=mp.log(4)+a+R*mp.log(a)-mp.loggamma(R+1)
 assert logtail<=mp.log(4)-7*a
 bound=mp.exp(logtail)
 assert bound>0
 tails.append({'w':w,'n':n,'R':R,'a':mp.nstr(a,30),'log_channel_tail_bound':mp.nstr(logtail,35),'positive_channel_tail_bound':mp.nstr(bound,25),'looser_bound_4exp_minus7a':mp.nstr(4*mp.exp(-7*a),25),'underflows_binary64_normal_range':logtail<mp.log(float(np.finfo(float).tiny))})
packet={'scope':'New independent traveling-packet identities, on top of the frozen distinct spin-clock PRE','exact_packet_rows':exact,'local_walk_power_rows':power_rows,'Bessel_vs_finite_rows':bessel_rows,'positive_tail_rows':tails,'general_resource_identities':{'finite_clock_ground_energy':'2J(1-cos(pi/(M+1)))','clock_program_mean_above_ground':'2J cos(pi/(M+1))','clock_program_norm':'4J cos(pi/(M+1))','bare_clock_plus_interaction_split_bound':'||H_int|| <= 4J cos(pi/(M+1))','initial_clock_energy_variance':'4J^2 w sin^2(pi/(w+1))/(w+1)'},'scientific_discrepancies':[],'author_builder_imported':False}
(HERE/'TRAVELING_PACKET_IDENTITY_RESULTS.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
