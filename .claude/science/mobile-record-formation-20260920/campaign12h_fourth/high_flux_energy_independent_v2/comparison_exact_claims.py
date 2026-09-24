#!/opt/homebrew/opt/python@3.13/bin/python3.13
"""Compare each author path and claimed moment with the frozen own PRE engines."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,hashlib
import sympy as sp
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
mods=[]
for name,file in [('direct','direct_matrix_action_control.py'),('formal','independent_exact_control.py')]:
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);mods.append(m)
d,f=mods
n,C=f.N,f.C
V=f.V
q=tuple(int(i in d.AA) for i in range(8));g={(q,tuple(n*v for v in V)):sp.Integer(1)}
def full_E2(v):return {s:c*sum(e*e for e in s[1]) for s,c in v.items()}
def own_mom(v):
 norm=d.inner(v,v);H=d.H4(v,None);D=d.D(v);E2=full_E2(v)
 z=d.hops(d.hops(v,1,None),2,None)
 h=d.inner(v,H)/norm;dm=d.inner(v,D)/norm;em=d.inner(v,E2)/norm
 return {'norm_squared':norm,'H4_mean':h,'H4_second_moment':d.inner(H,H)/norm,
 'H4_variance':d.inner(H,H)/norm-h*h,'D_mean':dm,'D_variance':d.inner(D,D)/norm-dm*dm,
 'symmetrized_D_H4_covariance':d.inner(D,H)/norm-dm*h,'E2_mean':em,
 'E2_variance':d.inner(E2,E2)/norm-em*em,'symmetrized_E2_H4_covariance':d.inner(E2,H)/norm-em*h,
 'H4_image_size':len(H),'Z_norm_squared':d.inner(z,z)}
mom={'input':own_mom(g),'selected_resolved':own_mom(d.B(g,0,(1,),None)),
     'selected_coherent':own_mom(d.B(g,0,(1,-1),None))}
author_rotor=json.loads((BASE/'high_flux_energy_extension_author/FULL_ROTOR_ENERGY_RESULTS.json').read_text())
checked_moments=0
for row in author_rotor['rows']:
 for surface,values in mom.items():
  for k,value in values.items():
   assert sp.simplify(sp.sympify(value).subs(n,row['n'])-sp.sympify(row[surface][k]))==0,(row['n'],surface,k)
   checked_moments+=1
# Each resolved formal output is one route, hence coefficient squared times D
# is compared state by state to the separate author path table.
author_spin=json.loads((BASE/'high_flux_energy_extension_author/SYMBOLIC_SPIN_ENERGY_BALANCE_RESULTS.json').read_text())
index={(tuple(r['edge']),r['old_destination'],r['sign']):r for r in author_spin['paths']}
assert len(index)==48
av=f.hop(f.PSI,1);rates=0;dgain=0;e2gain=0;checks=0
for edge,epair in enumerate(f.EDGES):
 a,b=epair if epair[0] in f.A else epair[::-1]
 for sign in (1,-1):
  vec=f.scale(f.birth(av,edge,sign),-1)
  for (q,off),terms in vec.items():
   old=next(i for i in range(8) if i not in f.A and i!=b and q[i])
   row=index[(epair,old,sign)]
   single={(q,off):terms};w=f.inner(single,single);dv=f.dvalue((q,off))
   field=tuple(n*ve+oe for ve,oe in zip(V,off));ev=sp.expand(sum(e*e for e in field))
   assert tuple(row['charges'])==q
   assert all(sp.simplify(sp.sympify(x,locals={'n':n,'C':C})-y)==0 for x,y in zip(row['field'],field))
   for label,ours in [('weight',w),('D',dv),('E2',ev)]:
    assert sp.simplify(sp.sympify(row[label],locals={'n':n,'C':C})-ours)==0,(row,label)
   rates+=w;dgain+=w*dv;e2gain+=w*ev;checks+=1
summary={'rate':rates,'post_D_weighted':dgain,'D_drift_over_kappa':dgain-4*n*n*rates,
         'post_E2_weighted':e2gain,'E2_drift_over_kappa':e2gain-4*n*n*rates}
for k,v in summary.items():
 assert sp.simplify(v-sp.sympify(author_spin['summary'][k],locals={'n':n,'C':C}))==0,k
summary={k:sp.factor(v) for k,v in summary.items()}
# Pure rotor limits and all mark magnetic facts are already PRE-bound; compare
# every saved author row, including each zero Z cross term reconstructed here.
cross=[]
for e in range(12):
 vp=d.B(g,e,(1,),None);vm=d.B(g,e,(-1,),None)
 zp=d.hops(d.hops(vp,1,None),2,None);zm=d.hops(d.hops(vm,1,None),2,None)
 cross.append(d.inner(zp,zm))
assert all(c==0 for c in cross)
pre=json.loads((HERE/'EXACT_RESULTS.json').read_text())
for row in author_rotor['rows']:
 for label,data in row['instruments'].items():
  p=pre['instruments'][label]
  expected={'number_of_marks':24 if label=='resolved' else 12,
   'loss_eigenvalue_verified':sp.sympify(p['rotor_rate']),
   'post_D_weighted':sp.sympify(p['rotor_D_gain'],locals={'n':n}),
   'D_drift_over_kappa':sp.sympify(p['rotor_D_drift'],locals={'n':n}),
   'post_H4_weighted':sp.sympify(p['rotor_H4_gain']),
   'H4_drift_over_kappa':sp.sympify(p['rotor_H4_drift']),
   'post_E2_weighted':sp.limit(summary['post_E2_weighted'],C,sp.oo),
   'E2_drift_over_kappa':sp.limit(summary['E2_drift_over_kappa'],C,sp.oo)}
  for k,v in expected.items():assert sp.simplify(sp.sympify(v).subs(n,row['n'])-sp.sympify(data[k]))==0,(row['n'],label,k)
  assert [str(c) for c in cross]==data['all_Z_cross_terms']
# Actual boundary exclusion through own exact square-root implementation.
boundary=[]
for S,ni in [(1,-1),(1,0),(1,1),(2,-2),(2,2)]:
 for label in ('resolved','coherent'):
  row=d.calc(ni,S,label)
  p=pre['instruments'][label]
  for ownkey,prekey in [('rate','spin_rate'),('D_drift','spin_D_drift'),('H4_drift','spin_H4_drift')]:
   ex=sp.sympify(p[prekey],locals={'n':n,'C':C}).subs({n:ni,C:S*(S+1)})
   assert sp.simplify(row[ownkey]-ex)==0,(row,ownkey,ex)
  if label=='resolved' and ni==S:assert row['selected']['norm']==0
  boundary.append({k:str(v) for k,v in row.items()})
result={'saved_author_rotor_moments_compared':checked_moments,'all_48_spin_paths_match_symbolically':checks==48,
 'all_saved_rotor_instrument_rows_match':True,'all_twelve_symbolic_Z_cross_terms_zero':True,
 'own_symbolic_spin_sums':summary,'own_actual_boundary_cases':boundary,
 'failures':[],'scope':'Comparison only; own PRE scientific implementation bytes unchanged.'}
(HERE/'COMPARISON_EXACT_CLAIMS_RESULTS.json').write_text(json.dumps(result,default=str,indent=2)+'\n')
print(json.dumps({'saved_rotor_moments_compared':checked_moments,'spin_paths_compared':checks,
 'boundary_instrument_cases':len(boundary),'symbolic_spin_sums':summary,'all_checks_completed':True},default=str,indent=2))
