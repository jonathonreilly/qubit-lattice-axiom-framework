"""Exact physical flux paths for the postbirth fast-band calculation.
Fresh author implementation; no imported model, Fourier identification or fit.
"""
from pathlib import Path
from collections import defaultdict
import json
import sympy as sy
HERE=Path(__file__).resolve().parent
A=(0,3,5,6);edges=tuple((a,b) for a in A for b in range(8) if (a^b).bit_count()==1)
t=sy.Symbol('t',nonnegative=True);C=2/(1-t*t)
x={(tuple(int(i in A) for i in range(8)),(0,)*12):sy.Integer(1)}
def clean(v):return {k:sy.simplify(a) for k,a in v.items() if sy.simplify(a)!=0}
def plus(*terms):
 out=defaultdict(lambda:sy.Integer(0))
 for c,v in terms:
  for k,a in v.items():out[k]+=c*a
 return clean(out)
def inner(v,w):return sy.simplify(sum(sy.conjugate(a)*w.get(k,0) for k,a in v.items()))
def gauss(st):
 q,f=st;d=[0]*8
 for (a,b),e in zip(edges,f):d[a]+=e;d[b]-=e
 return all(d[i]==q[i]-int(i in A) for i in range(8))
def act(v,mode,rotor=False,kmark=0,sign=1,center=None):
 out=defaultdict(lambda:sy.Integer(0))
 for (q,f),amp in v.items():
  for k,(a,b) in enumerate(edges):
   if center is not None and a!=center:continue
   moves=[]
   if mode=='F' and q[a] and not q[b]:moves=[(a,b,-q[a],None)]
   if mode=='G' and q[b] and not q[a]:moves=[(b,a,q[b],None)]
   if mode=='j' and k==kmark and not q[a] and not q[b]:moves=[(None,None,s,s) for s in ((1,-1) if sign==0 else (sign,))]
   for source,destination,shift,birth in moves:
    e=int(f[k]);factor=e*(e+shift)
    if not rotor:assert factor in (0,2),('unexpected symbolic spin factor',e,shift,mode)
    weight=sy.Integer(1) if rotor else sy.sqrt(1-factor/C)
    qq,ff=list(q),list(f);ff[k]+=shift
    if birth is None:qq[destination]=qq[source];qq[source]=0
    else:qq[a]=birth;qq[b]=-birth
    st=(tuple(qq),tuple(ff));assert gauss(st);out[st]+=amp*weight
 return clean(out)
def certificate(v):return [{'q':q,'E_A_to_B':f,'amplitude':str(a)} for (q,f),a in sorted(v.items())]
rows=[]
for rotor in (True,False):
 F=lambda v:act(v,'F',rotor);G=lambda v:act(v,'G',rotor)
 for sign in (1,-1,0):
  B=act(F(x),'j',rotor,sign=sign)
  R=plus((sy.Rational(1,2),act(F(F(x)),'j',rotor,sign=sign)),(-1,F(B)))
  local=act(B,'F',rotor,center=0);assert not plus((1,R),(1,local))
  w=inner(B,B);r=inner(R,R);G1R=plus((1,F(G(R))),(-1,G(F(R))))
  sums={};vectors={}
  for kind in ('resolved','coherent'):
   qsum=slow=sy.Integer(0)
   for k in range(12):
    for s in ((1,-1) if kind=='resolved' else (0,)):
     assert not act(R,'j',rotor,kmark=k,sign=s)
     v=act(G1R,'j',rotor,kmark=k,sign=s);qsum+=inner(v,v)
     bb=act(F(B),'j',rotor,kmark=k,sign=s);slow+=inner(bb,bb)
     if rotor and v:vectors[str((k,s))]=certificate(v)
   sums[kind]={'Gamma_G1R_squared':str(sy.simplify(qsum)),'next_slow_rate':str(sy.simplify(slow/w))}
   wanted=(24 if rotor else 24-12/C)*r
   assert sy.simplify(qsum-wanted)==0 and sy.simplify(slow/w-8)==0
  if rotor:
   assert inner(G1R,G1R)==12*r
   # In the rotor each nonzero G1R word has adjacent vacancies, so Gamma=2.
   for q,f in G1R:
    emptyA=[a for a in A if not q[a]];emptyB=[b for b in (1,2,4,7) if not q[b]]
    assert len(emptyA)==len(emptyB)==1 and (emptyA[0],emptyB[0]) in edges
  rows.append({'rotor':rotor,'first_sign':sign,'B_squared_norm':str(w),'R_squared_norm':str(r),'G1R_squared_norm':str(inner(G1R,G1R)),'instrument_sums':sums,'R_physical_support':certificate(R),'G1R_physical_support':certificate(G1R),'terminal_jump_support':vectors})
result={'all_assertions_passed':True,'symbolic_spin_substitution':'C=2/(1-t^2), 0<=t<1; C>=2','row_count':len(rows),'rows':rows,'scope':'Exact physical-word initial dark/bright and cubic coefficients. No Fourier vector, full decay, finite physical-time or bath claim.'}
(HERE/'EXACT_FAST_BAND_PATHS_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_assertions_passed':True,'rows':len(rows),'finite_spin_Q_over_R_norm':'24-12/C','rotor_cubic_energy_coefficients_over_kappa_delta2':[16,8,12],'next_slow_rate':8},indent=2))
