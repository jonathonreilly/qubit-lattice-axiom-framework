"""Actual infinite-chain covariance diagnostics; no finite-chain ground oracle."""
import argparse,importlib.util,json,sys
import numpy as np
import scipy
from scipy.integrate import quad

ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);args=ap.parse_args()
spec=importlib.util.spec_from_file_location('candidate',args.candidate)
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
rows=[]
print(json.dumps({'runtime':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__}}),flush=True)
def row(name,ok,**kw):
 d={'name':name,'pass':bool(ok),**kw};rows.append(d);print(json.dumps(d),flush=True)
def params(a,m=1.,v=1.):
 sigma=np.sqrt(m*m/4+v*v/a/a);g=sigma/2+m/4;J=sigma/2-m/4
 return g,J,J/g
def h(k,r):return (1-r*np.cos(k))/np.sqrt(1-2*r*np.cos(k)+r*r)
for a in (2.,1.,.5,.25):
 gc,Jc,rc=params(a);gf,Jf,rf=params(a/2)
 values=[]
 for N in (8192,16384):
  k=2*np.pi*np.arange(N)/N
  coarse=float(np.mean(h(k,rc)));mid=float(np.mean((1+np.cos(k))*h(k,rc)))
  fine=float(np.mean(c.state_weight(k,np)*h(k,rf)))
  # Independent literal D6 decomposition in infinite covariance:
  # Z, XX=-i b0 a1, YY=i a0 b1, derived directly from matrix D(k)/E(k).
  E=2*np.sqrt(gf*gf+Jf*Jf-2*gf*Jf*np.cos(k))
  S12=2j*(gf-Jf*np.exp(-1j*k))/E
  S21=np.conj(S12)
  z=complex(np.mean(-1j*S12))
  xx=complex(np.mean(-1j*S21*np.exp(-1j*k)))
  yy=complex(np.mean(1j*S12*np.exp(-1j*k)))
  literal=z-(xx+yy)/2
  values.append((coarse,mid,fine,literal.real))
  row(f'coefficient_covariance_{a}_{N}',abs(fine-literal)<2e-10,
      candidate=fine,literal_D6_real=literal.real,literal_D6_imag=literal.imag,
      residual=float(abs(fine-literal)),tolerance=2e-10)
  row(f'strict_state_margins_{a}_{N}',coarse-mid>1e-8 and mid-fine>1e-8,
      coarse=coarse,midpoint=mid,refined=fine,
      coarse_minus_mid=coarse-mid,mid_minus_refined=mid-fine,minimum_margin=1e-8)
  row(f'state_positive_survivor_{a}_{N}',0<=fine<=1,refined=fine)
 qfine,err=quad(lambda k:(1+np.cos(k))*h(k,rf)/np.pi,0,np.pi,
                epsabs=2e-13,epsrel=2e-13,limit=200)
 row(f'independent_quad_{a}',abs(values[-1][2]-qfine)<2e-10,
     candidate=values[-1][2],quadrature=qfine,reported_quad_error=err,
     residual=abs(values[-1][2]-qfine),tolerance=2e-10)
 row(f'grid_refinement_{a}',max(abs(x-y) for x,y in zip(values[0],values[1]))<2e-10,
     coarse_grid=list(values[0]),fine_grid=list(values[1]),tolerance=2e-10)
 row(f'ratio_increases_{a}',0<rc<rf<1,coarse_ratio=rc,fine_ratio=rf)
# Degenerate v=0 is outside strict theorem hypotheses and is deliberately retained.
k=2*np.pi*np.arange(8192)/8192
for a in (1.,.5):
 _,_,r=params(a,v=0.)
 coarse=float(np.mean(h(k,r)));fine=float(np.mean(c.state_weight(k,np)*h(k,r)))
 row(f'v_zero_equality_survivor_{a}',abs(coarse-fine)<2e-10,
     coarse=coarse,refined=fine,strict_hypotheses=False)
failed=[r['name'] for r in rows if not r['pass']]
print(json.dumps({'summary':{'rows':len(rows),'pass':len(rows)-len(failed),'fail':len(failed),'failed':failed}}),flush=True)
sys.exit(bool(failed))
