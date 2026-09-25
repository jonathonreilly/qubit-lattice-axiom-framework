#!/usr/bin/env python3
"""Analyse own exact Laurent artifacts; no scientific builder imports."""
from collections import Counter
from fractions import Fraction
import hashlib,json,math
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
def read(name):return json.loads((HERE/name).read_text())
inf=read('infinite_RESULTS.json');six=read('L6_RESULTS.json');sixteen=read('L16_RESULTS.json')
def flow_key(rows,L=None):
 d=Counter()
 for row in rows:
  a=tuple(row['a']);b=tuple(row['b'])
  if L:a=tuple(x%L for x in a);b=tuple(x%L for x in b)
  d[a,b]+=row['shift']
 return tuple(sorted((e,n) for e,n in d.items() if n))
def poly(rows,L=None):return Counter({flow_key(r['flow'],L):r['coefficient'] for r in rows})
def rv(answer,L=None):
 out={}
 for row in answer['r4']:
  a=tuple(row['a']);b=tuple(row['b'])
  if L:a=tuple(x%L for x in a);b=tuple(x%L for x in b)
  out[a,b]=Fraction(row['numerator'],4*row['denominator'])
 return out
def wind(f,L):
 total=[0,0,0]
 for (a,b),n in f:
  for j in range(3):
   d=b[j]-a[j];d=d-L if d>L//2 else d+L if d<-L//2 else d
   total[j]+=n*d
 return tuple(total)
comparisons=[]
for current,L in [(six,6),(sixteen,16)]:
 for k,answer in enumerate(current['answers']):
  mapped=poly(inf['answers'][k]['twice_power_laurent'],L)
  actual=poly(answer['twice_power_laurent'])
  diff=Counter()
  for f in set(mapped)|set(actual):
   d=actual.get(f,0)-mapped.get(f,0)
   if d:diff[f]=d
  row=dict(L=L,sigma=answer['sigma'],full_polynomial_equal=not diff,
           differing_terms=len(diff),nonzero_winding_actual=sum(wind(f,L)!=(0,0,0) for f in actual),
           differing_zero_winding_terms=sum(wind(f,L)==(0,0,0) for f in diff),
           r_equal=rv(inf['answers'][k],L)==rv(answer),flat_correction=answer['flat_output_correction'])
  if L==16:assert not diff and row['r_equal']
  comparisons.append(row)
assert inf['answers'][0]['twice_power_laurent']==inf['answers'][1]['twice_power_laurent']
ell={((0,0,0),(1,0,0)):1,((1,1,0),(1,0,0)):-1,
     ((1,1,0),(0,1,0)):1,((0,0,0),(0,1,0)):-1}
r=rv(inf['answers'][0])
def positive_array(flow,L):
 out=np.zeros((L,L,L,3))
 for (a,b),n in flow.items():
  d=np.array(b)-np.array(a);axis=int(np.flatnonzero(d)[0]);assert sum(abs(d))==1
  sign=int(d[axis]);site=a if sign==1 else b
  out[tuple(x%L for x in site)+(axis,)]+=sign*float(n)
 return out
def weighted_fourier(flow,L):
 a=positive_array(flow,L)
 ft=np.fft.fftn(a,axes=(0,1,2))/math.sqrt(L**3)
 ks=np.meshgrid(*([2*np.pi*np.arange(L)/L]*3),indexing='ij')
 lam=sum(4*np.sin(k/2)**2 for k in ks)
 divergence=sum((1-np.exp(-1j*k))*ft[...,j] for j,k in enumerate(ks))
 assert np.max(np.abs(divergence))<1e-11
 assert np.max(np.abs(ft[0,0,0]))<1e-11
 weight=np.zeros_like(lam);mask=lam>1e-20;weight[mask]=1/np.sqrt(2*np.sqrt(lam[mask]))
 return ft*weight[...,None]
numeric=[]
for L in (6,16,20):
 # L6 uses its actual Haar-averaged coefficient, not the infinite lift.
 use_r=rv(six['answers'][0]) if L==6 else r
 if L==6:
  use_r={(tuple(x if x<=L//2 else x-L for x in a),tuple(x if x<=L//2 else x-L for x in b)):n for (a,b),n in use_r.items()}
 u=weighted_fourier(ell,L);v=weighted_fourier(use_r,L)
 vv=float(np.vdot(u,u).real);ww=float(np.vdot(v,v).real);s=float(np.vdot(u,v).real)
 assert abs(np.vdot(u,v).imag)<1e-10
 product=math.sqrt(vv*ww)
 spectral=[(s-product)/2,(s+product)/2]
 h0=-321*L**3+inf['answers'][0]['flat_output_correction']
 # h0 formula at L6 is checked separately by the full finite graph control.
 numeric.append(dict(L=L,vacuum_ell_variance=vv,vacuum_r_variance=ww,vacuum_cross=s,
    selected_vacuum_power_in_kappa_over_tau_units=s/4,
    one_particle_added_power_range_in_kappa_over_tau_units=[q/2 for q in spectral],
    full_one_particle_power_range_in_kappa_over_tau_units=[s/4+q/2 for q in spectral],
    output_flat_H4=h0,vacuum_gain_limit_in_kappa_over_tau_units=h0*vv/8,
    vacuum_anticommutator_subtrahend_limit_in_kappa_over_tau_units=h0*vv/8-s/4,
    covariance_cauchy_gap=vv*ww-s*s))
 # Exact harmonic characteristic evaluation of the full local Laurent word sum.
 # Use vacuum only here; no compact propagation or electric operator simulation.
 if L==16:
  terms=poly(inf['answers'][0]['twice_power_laurent'])
  data=[]
  for f,coefficient in terms.items():
   a=weighted_fourier(dict(f),L);variance=float(np.vdot(a,a).real)
   data.append((coefficient,variance))
  convergence=[]
  for g in (.2,.1,.05,.025,.0125):
   # sum(coeff)=0: expm1 prevents large constant cancellation.
   P=math.fsum(c*math.expm1(-g*g*var/2)/2 for c,var in data)
   convergence.append(dict(g=g,magnetic_power_in_kappa_over_tau_units=P/(4*g*g),
                            limiting_power=s/4,error=P/(4*g*g)-s/4))
  numeric[-1]['harmonic_vacuum_characteristic_rows']=convergence
summary=dict(scope='Own exact coefficient correspondence plus finite Fourier covariance arithmetic; no author runner, no compact dynamics or interval enclosure.',
    correspondence=comparisons,r_support_edges=len(r),ell_dot_r=str(sum(Fraction(n)*r.get(e,0) for e,n in ell.items())),
    r_minus_1675ell_norm_squared=str(sum((r.get(e,0)-1675*ell.get(e,0))**2 for e in set(r)|set(ell))),
    numeric=numeric,indefinite_added_one_particle_form=all(row['one_particle_added_power_range_in_kappa_over_tau_units'][0]<0<row['one_particle_added_power_range_in_kappa_over_tau_units'][1] for row in numeric),
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
with (HERE/'FOURIER_CORRESPONDENCE_RESULTS.json').open('x') as f:json.dump(summary,f,indent=2);f.write('\n')
print(json.dumps(summary,indent=2))
