"""Root's conditional gain reconstruction; no external observed data read."""
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as s

p=Path(__file__).resolve().parent
tau=s.symbols('tau',real=True)
P,J,g=[s.Function(n)(tau) for n in ['P','J','g']]
a,c,d,e,f,k=s.symbols('a c d e f k',real=True)
drift=s.diff(g,tau)/g
at=a-2*drift
ct=c-a*drift-s.diff(drift,tau)+drift**2
ft=f-d*drift
original=s.diff(J,tau,2)+k*J+a*s.diff(J,tau)+c*J-d*s.diff(P,tau)-e*k*P-f*P
trans=s.diff(g*J,tau,2)+k*g*J+at*s.diff(g*J,tau)+ct*g*J-d*s.diff(g*P,tau)-e*k*g*P-ft*g*P
checks=[]
def exact(name,expr):
 z=s.factor(s.cancel(s.expand(expr)));checks.append({'name':name,'pass':z==0,'residual':str(z)})
def ck(name,val,**ev):checks.append({'name':name,'pass':bool(val),**ev})
exact('arbitrary common gain transforms full differential identity',trans-g*original)
exact('curvature coefficient unwarping',ct+at*drift+drift**2+s.diff(drift,tau)-c)
exact('source coefficient unwarping',ft+d*drift-f)
B,h,q,L,ss=s.symbols('B h q L ss',real=True)
ds=6*B*(h-q)+4*q
aas=3*(h-q)-2*L
qrec=(ds-6*B*h)/(4-6*B)
srec=(3*(h-qrec)-2*L-(aas-2*ss))/2
exact('speed product from unshifted gradient coefficient',qrec-q)
exact('common gain drift reconstructed',srec-ss)

# The column map is derived explicitly; no assumption that rank is conserved
# under a general channel calibration is made.
jp,jv,pp,pv,kv,gg,sg=s.symbols('jp jv pp pv kv gg sg',real=True)
row=s.Matrix([[-jp,-jv,pp,kv*pv,pv]])
T=s.Matrix([[1,0,0,0,0],[sg,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,sg,0,1]])
target=s.Matrix([[-gg*(jp+sg*jv),-gg*jv,gg*(pp+sg*pv),gg*kv*pv,gg*pv]])
for ix in range(5):exact('gain design column '+str(ix+1), (gg*row*T-target)[ix])
exact('gain column-map determinant',T.det()-1)

control=json.loads((p/'MODE_INVERSE_CONTROLS_v1.json').read_text())
rows=[]
maximum_q=maximum_s=maximum_kappa=maximum_theta=0.
for epoch in control['forward']['rows']:
    tm=epoch['tau']
    gain=float(np.exp(.07*tm*tm))
    gain_drift=.14*tm
    gain_drift_prime=.14
    mat=[];y=[]
    for mode in epoch['modes']:
        pv,jv,ppv,jp,jpp=[mode[z] for z in ['P','J','P_prime','J_prime','J_second']]
        kv=mode['k_com_squared']/(4*tm*tm)
        pr=gain*pv;jr=gain*jv
        prp=gain*(ppv+gain_drift*pv)
        jrp=gain*(jp+gain_drift*jv)
        jrpp=gain*(jpp+2*gain_drift*jp+(gain_drift_prime+gain_drift**2)*jv)
        mat.append([-jrp,-jr,prp,kv*pr,pr]);y.append(jrpp+kv*jr)
    fit=np.linalg.solve(np.array(mat),np.array(y))
    aa,cc,dd,ee,ff=fit
    # Only the recorded coefficients and background enter this inverse.
    # The fixture's e is constant; its derivative is zero, verified in the
    # primary original-equation controls. This numerical control is not a
    # noisy derivative experiment. Symbolic controls above allow variable B.
    hv=1/tm;BB=ee/2;Lv=0.
    qr=(dd-6*BB*hv)/(4-6*BB)
    sr=(3*(hv-qr)-2*Lv-aa)/2
    # The smooth recorded coefficient functions for this exact witness give
    # the differentiated inverse. No true gain function is substituted here:
    # d'= -10/(2 tau^2), h'= -1/tau^2, a_tilde'= -3/(2tau^2)-.28.
    hp=-1/tm**2
    dp=-5/tm**2
    ap=-1.5/tm**2-.28
    qp=(dp-6*BB*hp)/(4-6*BB)
    sp=(3*(hp-qp)-ap)/2
    cphysical=cc+aa*sr+sr*sr+sp
    kr=cphysical-qp-3*hv*qr+2*qr*qr
    expected=np.array([1.5/tm-2*gain_drift,2.25/tm**2-(1.5/tm)*gain_drift-gain_drift_prime+gain_drift**2,
                       5/tm,2,2.25/tm**2-(5/tm)*gain_drift])
    maximum_theta=max(maximum_theta,float(np.max(abs(fit-expected)/(1+abs(expected)))))
    maximum_q=max(maximum_q,abs(qr-.5/tm))
    maximum_s=max(maximum_s,abs(sr-gain_drift))
    maximum_kappa=max(maximum_kappa,abs(kr-1.75/tm**2))
    rows.append({'tau':tm,'fitted_record_coefficients':fit.tolist(),'recovered_q':float(qr),
                 'recovered_gain_log_derivative':float(sr),'true_gain_log_derivative':gain_drift,
                 'recovered_fixed_bare_kappa':float(kr),'true_fixed_bare_kappa':1.75/tm**2})
ck('gain-corrupted coefficients recovered on31epochs',maximum_theta<2e-10,max_relative_error=maximum_theta)
ck('physical q recovered despite nonconstant common gain',maximum_q<2e-10,max_absolute_error=maximum_q)
ck('gain logarithmic drift recovered',maximum_s<2e-10,max_absolute_error=maximum_s)
ck('curvature recovered with derivative inputs stated',maximum_kappa<2e-9,max_absolute_error=maximum_kappa)
sources=['check_mode_gain_v1.py','MODE_GAIN_DERIVATION_v1.md','MODE_INVERSE_CONTROLS_v1.json']
result={'author':'/root personally','stage':'before new-unit checker exposure','checks':checks,
        'passed':sum(v['pass'] for v in checks),'failed':sum(not v['pass'] for v in checks),'rows':rows,
        'empirical_validation':False,'numerical_derivative_role':'Exact prescribed smooth coefficient derivatives for the synthetic gain-corrupted power witness; not inferred from noisy samples.',
        'scientific_input_reads':['MODE_INVERSE_CONTROLS_v1.json: author synthetic original-equation forward trajectories'],
        'integrity_reads':sources,'source_sha256':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in sources}}
print(json.dumps(result,indent=2,sort_keys=True));raise SystemExit(int(result['failed']>0))
