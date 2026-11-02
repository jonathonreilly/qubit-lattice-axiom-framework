"""Exact elementary scope controls; none is an infrared producer."""
import sympy as s,json,sys
from datetime import datetime,timezone
checks={};details={}
def ck(n,v):checks[n]=bool(v)
k,mu,t,m=s.symbols('k mu t m',positive=True);A=s.Matrix([[k*k+mu,-mu],[-mu,mu]])
schur=s.simplify(A[0,0]-A[0,1]/A[1,1]*A[1,0])
ck('massive_block_Schur_is_massless',schur==k*k)
ck('full_determinant_mu_k_squared',s.factor(A.det())==mu*k*k)
ck('zero_momentum_has_zero_eigenvalue',A.subs(k,0).det()==0)
ck('auxiliary_mass_cannot_supply_positive_remaining_lower_bound',s.limit(schur,k,0)==0)
x=s.symbols('x',real=True);b=s.symbols('b',positive=True)
slow=s.integrate(s.exp(-t*x),(x,0,1))
ck('hidden_continuous_spectrum_correlation',(s.simplify(slow-(1-s.exp(-t))/t))==0)
ck('hidden_low_spectral_projection_has_positive_mass',s.integrate(1,(x,0,b))==b)
ck('hidden_channel_violates_every_positive_exponential_rate',s.limit(s.exp(m*t)*slow,t,s.oo)==s.oo)
ck('selected_gapped_channel_exact',s.exp(-t)==s.exp(-1*t))
j=s.symbols('j',integer=True,positive=True);a=s.symbols('a',positive=True)
ck('observable_dependent_rate_can_close',s.limit(1/j,j,s.oo)==0)
ck('one_small_eigenvalue_violates_common_half_rate',s.limit(s.exp(t/s.Integer(2))*s.exp(-t/s.Integer(3)),t,s.oo)==s.oo)
ck('positive_cutoff_gap_can_close',s.limit(a,a,0,dir='+')==0)
ck('fixed_time_limit_can_have_extra_vacuum',s.limit(s.exp(-a*t),a,0,dir='+')==1)
# Symbolic spectral lower-bound control: low-energy weight cannot be canceled.
q=s.symbols('q',positive=True);w=s.symbols('w',positive=True)
C=w*q+(1+w)*q**3
ck('low_spectral_weight_cannot_cancel',s.expand(C-w*q)==(w+1)*q**3)
ck('low_spectral_weight_breaks_target_rate',s.limit(C/q**2,q,0,dir='+')==s.oo)
# Endpoint m is allowed: exp(-m t) satisfies the criterion exactly.
ck('threshold_endpoint_allowed',s.simplify(s.exp(m*t)*s.exp(-m*t))==1)
# Uncontrolled onset can make the finite-volume hypothesis vacuous.
T=s.symbols('T',positive=True);safe=T;onset=2*T
ck('uncontrolled_onset_window_empty',s.simplify(onset-safe).is_positive)
details={'auxiliary_Schur':str(schur),'hidden_continuous_correlation':str(slow),'dense_varying_rate_counterexample':'On C Omega plus l2(N), H e_j=(1/j)e_j; finite-support vectors have dense span and individual positive exponential rates, but inf excited spectrum=0.','onset_counterexample':'C_T(t)=1, m=1, A=1; requiring the bound only for 2T<=t<=T is vacuous while the fixed-time limit remains 1. The corrected common onset excludes this loophole.','lemma_scope':'The projection proof is analytic in the report. Finite exact controls cannot prove an interacting lattice estimate.'}
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'passed':sum(checks.values()),'total':len(checks),'details':details},indent=2,sort_keys=True));sys.exit(0 if all(checks.values()) else 1)
