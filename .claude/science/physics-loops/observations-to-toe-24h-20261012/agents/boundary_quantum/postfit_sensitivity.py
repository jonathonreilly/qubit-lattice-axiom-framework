"""Explicitly post-holdout diagnostics; never substitutes a primary fit."""
import json, math
import numpy as np
from scipy.optimize import brentq
import boundary_pair as b

b.guard()
cal=json.loads((b.HERE/'CALIBRATION_AND_PREDICTIONS_FREEZE.json').read_text())
di=json.loads((b.HERE/'SOURCE_DIAGNOSTICS_AND_PROSPECTIVE.json').read_text())
rows=cal['calibration_data']; bp=cal['models']['boundary']['parameters']
floor=di['calibration_periodic_repeat_score_floor']; ndiff=di['number_of_repeat_differences']
scale=math.sqrt(floor/ndiff)
score=cal['models']['boundary']['calibration_weighted_square']
def stable_E(c,k):
    c=np.clip(np.asarray(c,dtype=float),-1,1); e0=-1+2*np.arccos(c)/np.pi
    with np.errstate(divide='ignore'):
        return np.tanh(np.arctanh(e0)-k*c)
# Local runtime substitution solely to avoid exponential overflow at large k.
# Frozen analysis file remains unmodified; algebra equality is checked here.
err=max(np.max(abs(stable_E(np.linspace(-1,1,501),k)-b.E(np.linspace(-1,1,501),k)))for k in [0,.5,5,20,40])
assert err<2e-14
b.E=stable_E
large=[]
for k in [40.,100.,1000.,10000.]:
    b.guard()
    fit,p=b.fit_model(rows,'boundary',fixed_k=k)
    large.append({'k':k,'score':float(sum(fit.fun**2)),'parameters':p.tolist()})
def prof(k):
    fit,_=b.fit_model(rows,'boundary',fixed_k=k,initial=bp)
    return sum(fit.fun**2)-score-3.841458820694124*scale**2
cross=[float(brentq(prof,0,bp[-1])),float(brentq(prof,bp[-1],3.))]
b.write(b.HERE/'POSTFIT_SENSITIVITY.json',{'created_at':b.stamp(),
    'role':'Post-holdout diagnostic. Does not change frozen predictions or validate uncertainty coverage.',
    'periodic_repeat_error_multiplier':scale,'definition':'sqrt(sum of 8 independent-pair common-mean score minima / 8). Calibration-only observations, but this sensitivity procedure was selected after test exposure.',
    'inflated_error_profile_delta3p841_crossings':cross,
    'interpretation':'Illustrates fragility of counting-error-only curvature interval. A common multiplicative variance is an assumption, not a recovered experimental systematic model; repeat drift may be correlated or nonstationary.',
    'large_k_fixed_checks':large,'stable_formula_max_difference':float(err),
    'search_scope':'Primary fit searched k in [0,40] with multiple starts. These large-k fixed checks are additional controls, not a proof of global minimization over all k and nuisance values.'})
print('error multiplier',scale,'profile crossings',cross,'large k',[(x['k'],x['score'])for x in large])
