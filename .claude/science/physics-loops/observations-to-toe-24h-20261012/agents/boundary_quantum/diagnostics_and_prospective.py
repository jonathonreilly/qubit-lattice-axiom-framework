"""Post-test source diagnostics and exact prospective pair-law discriminator.

Does not alter the frozen fitting, uncertainty, or held-out prediction packets.
"""
import json, math
import numpy as np
from scipy.optimize import minimize_scalar
from boundary_pair import HERE, OUT, E, extract, guard, stamp, write

guard()
rows=extract(list(range(0,360,20)))
cal=json.loads((HERE/'CALIBRATION_AND_PREDICTIONS_FREEZE.json').read_text())
test=json.loads((HERE/'HELDOUT_RESULTS.json').read_text())
floor=0.; pairs=[]
for r in cal['calibration_data']:
    if r['angle']>=180: continue
    q=next(x for x in cal['calibration_data'] if x['basis']==r['basis'] and x['angle']==r['angle']+180)
    chi=(r['value']-q['value'])**2/(r['error']**2+q['error']**2)
    pairs.append({'basis':r['basis'],'angles':[r['angle'],q['angle']],
        'values':[r['value'],q['value']],'signed_difference_over_listed_error':(r['value']-q['value'])/math.hypot(r['error'],q['error']),
        'minimum_weighted_square_for_common_mean':chi})
    floor+=chi

def k_quantum(theta):
    c=math.cos(theta); u=1-2*theta/math.pi
    return (math.atanh(c)-math.atanh(u))/c

kstar=k_quantum(math.pi/4)
prospective=[]
for deg in [1,5,10,15,20,30,45,60,75,90]:
    theta=math.radians(deg); c=math.cos(theta)
    ek=float(E(c,kstar)); eq=-c; e0=float(E(c,0))
    V=.97; po=(1+V*eq)/2; pc=(1+V*ek)/2
    kl=max(0.,po*math.log(po/pc)+(1-po)*math.log((1-po)/(1-pc)))
    difference=V*(ek-eq)
    heuristic=25*(1-(V*eq)**2)/difference**2 if abs(difference)>1e-12 else None
    prospective.append({'Bloch_separation_degrees':deg,'polarization_axis_separation_degrees':deg/2,
       'quantum_E':eq,'boundary_E_calibrated_at_45deg':ek,'triangular_E':e0,
       'boundary_minus_quantum_E':ek-eq,'k_needed_to_match_this_angle':k_quantum(theta) if deg<90 else 1-2/math.pi,
       'per_trial_KL_quantum_to_boundary_at_visibility_0p97':kl,
       'illustrative_N_for_5_counting_SE_at_V0p97_negligible_calibration_error':heuristic})
maximum=minimize_scalar(lambda th:-abs(float(E(np.cos(th),kstar))+np.cos(th)),bounds=(1e-5,math.pi/2-1e-5),method='bounded')
output={'created_at':stamp(),'role':'Post-test diagnostics and prospective design; no primary fit or holdout edits',
    'calibration_periodic_repeat_score_floor':floor,'number_of_repeat_differences':len(pairs),'pairs':pairs,
    'error_squared_minus_count_max_abs':max(abs(r['error']**2-r['value'])for r in rows),
    'stationarity_floor_derivation':'For each periodic-equivalent pair, minimizing sum_i (y_i-mu)^2/sigma_i^2 gives (y1-y2)^2/(sigma1^2+sigma2^2); summing yields a lower bound for every stationary pair law under this coordinate map, even an arbitrary angular function.',
    'interpretation':'Descriptive inconsistency with diagonal counting-error stationary observation model; source drift, uncertain coordinate mapping, angle-dependent detection/background or non-independent processed counts can matter. No attribution to fundamental law.',
    'ideal_calibration':{'endpoint':'theta=0 gives E_obs=-V under common unbiased visibility map. This nuisance is independently identifiable from k.',
       'interior':'theta=45deg Bloch gives unique k=[atanh(-E_obs/V)-atanh(0.5)]/(1/sqrt(2)).',
       'if_quantum_calibration':'E_obs(45deg)=-V/sqrt(2)','k':kstar,
       'parameter_uncertainty':'Estimate V and k from calibration counts only, propagate their joint covariance or confidence set into all held-out settings; the illustrative N below neglects this error and is not a complete sample-size guarantee.'},
    'prospective':prospective,'maximum_absolute_E_difference':{'theta_Bloch_degrees':math.degrees(maximum.x),'difference':-maximum.fun},
    'small_angle_limits':{'boundary':'E=-1+(2/pi)exp(-2k)*theta+O(theta^2), theta>=0 in radians',
        'quantum':'E=-1+theta^2/2+O(theta^4)','visibility':'E_obs=V E; calibrated V>0 preserves linear-versus-quadratic distinction',
        'angular_jitter':'Convolution with angle error rounds the cusp; independently calibrate actual analyzer-angle distribution and forward-convolve both models.'},
    'CHSH_standard_angles':{'formula':'S=4 tanh(atanh(1/2)+k/sqrt(2))','k0':2.,'kstar':2*math.sqrt(2),'infinite_k_limit':4.,
        'meaning':'No-signaling alone allows superquantum values. Measurement independence fails by construction, so Bell-local bound does not apply for k>0.'}}
write(HERE/'SOURCE_DIAGNOSTICS_AND_PROSPECTIVE.json',output)
print(json.dumps({k:output[k]for k in ['calibration_periodic_repeat_score_floor','error_squared_minus_count_max_abs','ideal_calibration','maximum_absolute_E_difference','prospective']},indent=2))

# A static scientific comparison artifact. No source workbook alteration.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax=plt.subplots(1,2,figsize=(10.5,4))
th=np.linspace(0,90,500); rad=np.deg2rad(th)
ax[0].plot(th,-np.cos(rad),label='Quantum cosine',color='black')
ax[0].plot(th,E(np.cos(rad),kstar),label=f'Boundary law, k={kstar:.4f}',color='#b83232')
ax[0].plot(th,E(np.cos(rad),0),label='k=0 triangular',color='#377eb8',linestyle='--')
ax[0].scatter([0,45],[-1,-1/math.sqrt(2)],color='black',s=28,zorder=5,label='Ideal calibration')
ax[0].set(xlabel='Bloch separation (degrees)',ylabel='Ideal correlator E',title='Shared k fixed at the 45° quantum value')
ax[0].legend(fontsize=8); ax[0].grid(alpha=.2)
ax[1].plot(th,E(np.cos(rad),kstar)+np.cos(rad),color='#b83232')
ax[1].axhline(0,color='black',lw=.6)
for d in [15,30,60]:ax[1].axvline(d,color='gray',lw=.6,ls=':')
ax[1].set(xlabel='Bloch separation (degrees)',ylabel='Boundary minus quantum E',title='Prospective angular discriminator')
ax[1].grid(alpha=.2)
fig.tight_layout();fig.savefig(HERE/'prospective_discriminator.png',dpi=170);plt.close(fig)
