#!/usr/bin/env python3
"""Independent-variable quadrupole integral; finite checks, no empirical fitting."""
import argparse,json,hashlib
from pathlib import Path
import mpmath as mp
import sympy as sp
mp.mp.dps=70
s=sp.symbols('s',positive=True)
P=4*s**4+2*s**3+3*s*s+2*s+4
R=4*s**4-2*s**3+3*s*s-2*s+4
assert sp.expand(R**2*(1+s)-P**2*(1-s)-2*s**5*(16*s**4+12*s*s+21))==0
assert sp.expand(R**2*(1+s)-P**2*(s-1)-2*(21*s**4+12*s*s+16))==0
checks={'rationalization_identities':True}

def W(s):
 p=4*s**4+2*s**3+3*s*s+2*s+4
 r=4*s**4-2*s**3+3*s*s-2*s+4
 t=s**5*(16*s**4+12*s*s+21) if s<=1 else 21*s**4+12*s*s+16
 return mp.mpf(16)/105*t/(r*mp.sqrt(1+s)+p*mp.sqrt(abs(1-s)))

def minus_derivative(q):
 z=mp.sqrt(q)
 return mp.exp(-z)/(2*z*(-mp.expm1(-z))**2)

def nu(q):return 1/(-mp.expm1(-mp.sqrt(q)))

def F(eta):
 def f(s):
  if s==0:return mp.mpf(0)
  return W(s)*minus_derivative(eta*s)
 return mp.mpf(9)/8*eta**mp.mpf('2.5')*mp.quad(f,[0,mp.mpf('.5'),1,2,4,8,mp.inf])

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--reference',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);a=parser.parse_args()
 ref=json.loads(a.reference.read_text());rows=[]
 for eta in map(mp.mpf,['.5','1','2','3','4']):
  value=F(eta);old=next(x for x in ref['results'] if x['eta']==float(eta) and x['order']==512)
  target=-mp.mpf(3)/2*mp.mpf(str(old['h_parts']))
  bound=mp.mpf(9)/8*eta**mp.mpf('1.5')*min(W(2/eta),W(5/eta))*(nu(2)-nu(5))
  rows.append({'eta':str(eta),'F':mp.nstr(value,45),'old_parts_F':mp.nstr(target,30),'relative_discrepancy':mp.nstr(abs(value-target)/value,12),'q2_to_q5_lower_bound':mp.nstr(bound,30)})
 checks['two_dimensional_reference_agreement']=all(mp.mpf(x['relative_discrepancy'])<mp.mpf('1e-10') for x in rows)
 checks['illustrative_lower_bound']=all(mp.mpf(x['F'])>=mp.mpf(x['q2_to_q5_lower_bound'])>0 for x in rows)
 checks['reciprocity']=all(abs(W(x)-x**mp.mpf('4.5')*W(1/x))<mp.mpf('1e-60') for x in map(mp.mpf,['.001','.1','.7','1','2','10','1000']))
 result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'reference_sha256':hashlib.sha256(a.reference.read_bytes()).hexdigest(),'mp_dps':mp.mp.dps,'checks':checks,'values':rows,'W1':mp.nstr(W(mp.mpf(1)),40)}
 a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert all(checks.values())
if __name__=='__main__':main()
