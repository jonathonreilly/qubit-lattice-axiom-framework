#!/usr/bin/env python3
"""Clock concentration, whole-channel convergence and persistent wrong routes.
Independent of both the full-H numerical builder and all campaign builders.
This control uses a phase-covariant pump for explicit closed branch formulas.
"""
from pathlib import Path
import json
import numpy as np
from scipy.stats import binom
HERE=Path(__file__).resolve().parent
T=1.2;gamma=.7;omega=.83
# Choi matrix in (output,input) order for a pump with survival R and complex
# coherence multiplier z on rho_01. Trace is 2, so J/2 tests a maximally
# entangled input. Complete positivity requires |z|²<=R.
def J(R,z):
 out=np.zeros((4,4),complex)
 out[0,0]=R;out[2,2]=1-R;out[3,3]=1
 out[0,3]=z;out[3,0]=np.conj(z)
 return out
def tn(x):return float(np.sum(np.abs(np.linalg.eigvalsh((x+x.conj().T)/2))))
clock_rows=[];mutation_rows=[]
times=np.unique(np.r_[np.linspace(0,T,257),T*np.array([1e-6,1e-4,.001,.01,.25,.5,.75,.99,.999,.9999,.999999])])
for N in (16,64,256,1024,4096,16384):
 grid=(2*T/np.pi)*np.arcsin(np.sqrt(np.arange(N+1)/N));dt=np.diff(grid)
 assert max(dt)<=T/np.sqrt(N)+1e-13
 assert abs(max(dt)-(2*T/np.pi)*np.arcsin(1/np.sqrt(N)))<1e-13
 assert gamma*max(dt)<=.5
 R=np.r_[1.,np.cumprod(1-gamma*dt)]
 rows=[]
 for t in times:
  theta=np.pi*t/(2*T);p=np.sin(theta)**2
  if t==0:p=0.
  if t==T:p=1.
  weights=binom.pmf(np.arange(N+1),N,p)
  assert abs(weights.sum()-1)<2e-12
  time_error=float(np.dot(weights,abs(grid-t)))
  chord2=(np.sqrt(np.arange(N+1)/N)-np.sqrt(p))**2+(np.sqrt(1-np.arange(N+1)/N)-np.sqrt(1-p))**2
  mean_chord2=float(np.dot(weights,chord2))
  assert mean_chord2<=1/N+1e-13
  assert time_error<=T/np.sqrt(2*N)+1e-12
  survival=float(np.dot(weights,R));coherence=np.dot(weights,np.sqrt(R))*np.exp(1j*omega*t)
  actual=J(survival,coherence);ideal=J(np.exp(-gamma*t),np.exp(-gamma*t/2+1j*omega*t))
  err=tn(actual-ideal)
  bound=(T*T*(7*gamma**2+4*omega*gamma)+np.sqrt(2)*gamma*T)/np.sqrt(N)
  assert err/2<=bound+1e-12
  assert min(np.linalg.eigvalsh(actual))>=-1e-12
  rows.append({'t':float(t),'mean_absolute_clock_time_error':time_error,'mean_squared_Hellinger_chord':mean_chord2,'reference_input_trace_error':err/2,'diamond_upper_from_unnormalized_Choi':min(2.,err)})
 clock_rows.append({'N':N,'max_grid_step':float(max(dt)),'proved_grid_step_bound':T/np.sqrt(N),'max_sampled_clock_time_error':max(r['mean_absolute_clock_time_error'] for r in rows),'proved_uniform_clock_time_bound':T/np.sqrt(2*N),'max_sampled_reference_trace_error':max(r['reference_input_trace_error'] for r in rows),'max_sampled_diamond_upper':max(r['diamond_upper_from_unnormalized_Choi'] for r in rows),'proved_uniform_ideal_battery_channel_bound':min(2.,bound),'endpoint_reference_error':rows[-1]['reference_input_trace_error'],'rows':rows})
 # Wrong route 1: equal collision steps on a nonlinear clock. This has an
 # exact binomial closed form and a nonzero error for the ground-state input.
 t=T/4;p=np.sin(np.pi*t/(2*T))**2
 naive_survival=(1-p*gamma*T/N)**N
 target_survival=np.exp(-gamma*t)
 wrong_time_limit=np.exp(-gamma*T*p)
 population_error=2*abs(naive_survival-target_survival)
 # Wrong route 2: omit the counterphase. At the exact endpoint the
 # total physical phase is twice the phase specified by the GKLS generator.
 wrong=J(R[-1],np.sqrt(R[-1])*np.exp(2j*omega*T))
 target=J(np.exp(-gamma*T),np.exp(-gamma*T/2+1j*omega*T))
 wrong_ref=tn(wrong-target)/2
 mutation_rows.append({'N':N,'naive_equal_steps_test_time':t,'naive_equal_steps_ground_input_trace_error':population_error,'nonlinear_wrong_simulated_time':T*p,'persistent_naive_limit_trace_error':2*abs(wrong_time_limit-target_survival),'omitted_counterphase_endpoint_reference_trace_error':wrong_ref,'persistent_counterphase_limit_reference_error':2*np.exp(-gamma*T/2)*abs(np.sin(omega*T/2))})
assert clock_rows[-1]['max_sampled_reference_trace_error']<clock_rows[0]['max_sampled_reference_trace_error']/10
assert mutation_rows[-1]['naive_equal_steps_ground_input_trace_error']>.1
assert mutation_rows[-1]['omitted_counterphase_endpoint_reference_trace_error']>.5
result={'role':'Independent closed-form pump channel and exact binomial-clock controls; analytic theorem, not time sampling, supplies the uniform guarantee','parameters':{'T':T,'gamma':gamma,'omega':omega},'clock_cases':clock_rows,'retained_failed_routes':mutation_rows,'scope':'Ideal battery for this large-N channel check. A separate full finite-battery single-Hamiltonian control covers the actual dilation. No multitime or unbinned-time instrument claimed.'}
(HERE/'CLOCK_UNIFORMITY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'clock_summaries':[{k:r[k] for k in ('N','max_grid_step','max_sampled_clock_time_error','proved_uniform_clock_time_bound','max_sampled_reference_trace_error','max_sampled_diamond_upper','proved_uniform_ideal_battery_channel_bound')} for r in clock_rows],'retained_failed_routes':mutation_rows},indent=2))
