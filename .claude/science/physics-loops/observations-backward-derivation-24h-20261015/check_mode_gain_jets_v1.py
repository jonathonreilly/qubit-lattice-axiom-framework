"""Root gain probe: all coefficient derivatives extracted from record jets.

Companion to the earlier explicitly prescribed-derivative control. The gain
enters ONLY the synthetic forward readout; the inverse is given h,h' and
recorded potential jets. Original source rows are author mathematical controls.
"""
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as s

p=Path(__file__).resolve().parent
t,u,pi,P,U,delta,k=s.symbols('t u pi P U delta k',real=True)
pd=(u/t-U/t**2)/2-P/t
rates=[pi,-3*pi/t-(k+7)*u/t**2-delta/t**2+4*pd/t+4*P/t**2,
       pd,-P-u-U/t,3*pd+k*U/t**2]
states=[u,pi,P,U,delta]
def derivative(expr):
 return (s.diff(expr,t)+sum(s.diff(expr,a)*v for a,v in zip(states,rates)))/t
def jets(expr,n):
 row=[expr]
 for _ in range(n):row.append(derivative(row[-1]))
 return row

gain=s.exp(s.Rational(7,100)*t**4/4)
observables=jets(gain*u,4)+jets(gain*P,3)+jets(k/t**4,2)
func=s.lambdify([t]+states+[k],observables,'numpy',cse=True)
source=json.loads((p/'MODE_INVERSE_CONTROLS_v1.json').read_text())
rows=[]
maximum={n:0. for n in ['B','L','q','s','s_prime','kappa','f_compatibility','gain_normalized']}
for ep in source['forward']['rows']:
 tt=ep['t_E'];tm=ep['tau'];h=2/tt**2;hp=-4/tt**4
 matrices=[[],[],[]];ys=[[],[],[]]
 for md in ep['modes']:
  st=[md['J'],tt*md['J_prime'],md['P'],md['matter_Z']/tt,md['bare_delta']]
  j0,j1,j2,j3,j4,p0,p1,p2,p3,k0,k1,k22=np.asarray(func(tt,*st,md['k_com_squared']),float)
  matrices[0].append([-j1,-j0,p1,k0*p0,p0])
  matrices[1].append([-j2,-j1,p2,k1*p0+k0*p1,p1])
  matrices[2].append([-j3,-j2,p3,k22*p0+2*k1*p1+k0*p2,p2])
  ys[0].append(j2+k0*j0)
  ys[1].append(j3+k1*j0+k0*j1)
  ys[2].append(j4+k22*j0+2*k1*j1+k0*j2)
 D,Dp,Dpp=[np.asarray(m) for m in matrices]
 y,yp,ypp=[np.asarray(v) for v in ys]
 theta=np.linalg.solve(D,y)
 first=np.linalg.solve(D,yp-Dp@theta)
 second=np.linalg.solve(D,ypp-Dpp@theta-2*Dp@first)
 at,ct,d,e,f=theta
 B=e/2;Bp=first[3]/2;Bpp=second[3]/2
 L=Bp/(2*B);Lp=Bpp/(2*B)-Bp*Bp/(2*B*B)
 numerator=d-6*B*h;denominator=4-6*B
 q=numerator/denominator
 qp=((first[2]-6*Bp*h-6*B*hp)*denominator+6*Bp*numerator)/denominator**2
 drift=(3*(h-q)-2*L-at)/2
 driftp=(3*(hp-qp)-2*Lp-first[0])/2
 physical_c=ct+at*drift+drift*drift+driftp
 kap=physical_c-qp-3*h*q+2*q*q-2*q*L-L*L+Lp+3*h*L
 fphysical=f+d*drift
 fexpected=6*B*(h-q)**2+2*(qp-q*L)+6*h*q-5*q*q
 errs={'B':abs(B-1),'L':abs(L),'q':abs(q-1/tt**2),'s':abs(drift-.14*tm),
       's_prime':abs(driftp-.14),'kappa':abs(kap-7/tt**4),'f_compatibility':abs(fphysical-fexpected)}
 for name,val in errs.items():maximum[name]=max(maximum[name],float(val))
 rows.append({'t_E':tt,'tau':tm,'record_coefficients':theta.tolist(),'record_first':first.tolist(),'record_second':second.tolist(),
              'recovered_B':float(B),'recovered_q':float(q),'recovered_drift':float(drift),
              'recovered_drift_prime':float(driftp),'recovered_kappa':float(kap),
              'f_consistency_residual':float(fphysical-fexpected)})

# Integrate the inferred drift; this fixture has a linear drift, so the
# trapezoid rule is exact up to recovered coefficient roundoff. g0 is a free
# constant; compare gains normalized at the first matter epoch.
log_g=0.
base=rows[0]['tau']
for index,row in enumerate(rows):
 if index:
  prev=rows[index-1]
  log_g+=(row['tau']-prev['tau'])*(row['recovered_drift']+prev['recovered_drift'])/2
 normalized=float(np.exp(log_g))
 true=float(np.exp(.07*(row['tau']**2-base**2)))
 row['recovered_normalized_gain']=normalized
 row['true_normalized_gain']=true
 maximum['gain_normalized']=max(maximum['gain_normalized'],abs(normalized-true))
checks=[{'name':n+' recovered from gain-corrupted observable jets','pass':v<2e-9,'max_absolute_error':v} for n,v in maximum.items()]
files=['check_mode_gain_jets_v1.py','MODE_GAIN_DERIVATION_v1.md','MODE_INVERSE_CONTROLS_v1.json']
out={'author':'/root personally','stage':'before new-unit checker exposure','empirical_validation':False,
     'checks':checks,'passed':sum(v['pass'] for v in checks),'failed':sum(not v['pass'] for v in checks),
     'rows':rows,'data_role':'Original-equation mathematical witness; gain multiplies synthetic readouts only. All inverse coefficient derivatives come from differentiated design and response rows.',
     'integrity_read_paths':files,'scientific_read_paths':['MODE_INVERSE_CONTROLS_v1.json'],
     'source_sha256':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in files}}
print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(int(out['failed']>0))
