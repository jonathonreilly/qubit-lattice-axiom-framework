"""Bounded POST exact comparison using own immutable PRE data and engine.

Construct the complete polynomial commutator by sparse matrix multiplication in
PRE cycle coordinates, then transform by the integer change of tree. No author
builder is imported/executed. Physical original first outputs are independently
assembled as integer charge/field paths.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,datetime,traceback
import numpy as np
import sympy as sp
from fiber_engine import A,B,EDGES,TREE,CHORDS,WORDS,INDEX,GRADES,ONE,DARK,BRIGHT,reference,gauss,matrices
from exact_fiber_control import build
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
 checks.append({'check':name,'passed':bool(value)})
 if not value:raise AssertionError(name)

def polynomial_G():
 """Matrix products F F* and F* F, with each entry an exact monomial."""
 by_column=defaultdict(list);by_row=defaultdict(list)
 for col,q in enumerate(WORDS):
  for edge in EDGES:
   a,b=edge
   if not q[a] or q[b]:continue
   qq=list(q);qq[a],qq[b]=0,q[a];row=INDEX[tuple(qq)];e=[0]*5
   if edge in CHORDS:e[CHORDS.index(edge)]=-q[a]
   by_column[col].append((row,tuple(e)));by_row[row].append((col,tuple(e)))
 poly=defaultdict(int)
 for entries in by_column.values():
  for r,e in entries:
   for c,f in entries:
    if GRADES[r]==GRADES[c]==1:poly[(r,c,tuple(x-y for x,y in zip(e,f)))]+=1
 for entries in by_row.values():
  for r,e in entries:
   for c,f in entries:
    if GRADES[r]==GRADES[c]==1:poly[(r,c,tuple(y-x for x,y in zip(e,f))) ]-=1
 return {k:v for k,v in poly.items() if v}

def Fphysical(vector,center=None):
 result=defaultdict(int)
 for (q,E),amp in vector.items():
  for ei,(a,b) in enumerate(EDGES):
   if center is not None and a!=center:continue
   if not q[a] or q[b]:continue
   qq=list(q);ee=list(E);qq[a],qq[b]=0,q[a];ee[ei]-=q[a]
   target=(tuple(qq),tuple(ee));check('physical F target Gauss '+str(target),gauss(*target));result[target]+=amp
 return dict(result)

def birthphysical(vector,mark):
 result=defaultdict(int);ei=EDGES.index((0,1))
 for (q,E),amp in vector.items():
  if q[0] or q[1]:continue
  for sign in (1,-1) if mark==0 else (mark,):
   qq=list(q);ee=list(E);qq[0],qq[1]=sign,-sign;ee[ei]+=sign
   target=(tuple(qq),tuple(ee));check('physical birth target Gauss '+str(target),gauss(*target));result[target]+=amp
 return dict(result)

def run():
 author=json.loads((HERE/'post_sources/author/EXACT_TAIL_RESULTS.json').read_text())
 own=json.loads((HERE/'EXACT_FIBER_RESULTS_01.json').read_text())
 check('complete charge ordering',list(map(list,WORDS))==author['charge_words'])
 check('complete edge ordering',list(map(list,EDGES))==author['edge_order'])
 check('dark ordering',[list(WORDS[int(ONE[i])]) for i in DARK]==author['dark_words'])
 check('bright ordering',[list(WORDS[int(ONE[i])]) for i in BRIGHT]==author['bright_words'])
 check('W dimensions',[int(sum(GRADES==w)) for w in (0,1,2)]==author['W_dimensions'])
 CI=sp.Matrix(own['fundamental_cycles']).T
 author_chords=author['chord_edge_indices'];M=CI.extract(author_chords,range(5));Minv=M.inv()
 check('cycle change unimodular',abs(M.det())==1 and all(v.is_Integer for v in Minv))
 CA=CI*Minv;check('all author cycle entries reconstructed',CA.tolist()==author['integer_cycle_matrix'])
 offsets=[]
 for q in WORDS:
  ref=sp.Matrix(reference(q));a=ref.extract(author_chords,[0]);newref=ref-CA*a
  check('new reference satisfies Gauss '+str(q),gauss(q,tuple(map(int,newref))))
  check('new reference has zero author chords '+str(q),all(newref[c]==0 for c in author_chords))
  offsets.append(a)
 poly=polynomial_G();darkfull=set(int(ONE[i]) for i in DARK);brightfull=[int(ONE[i]) for i in BRIGHT]
 transformed=defaultdict(int);darkterms=[]
 for (r,c,e),v in poly.items():
  if c not in darkfull:continue
  if r in darkfull:darkterms.append((r,c,e,v));continue
  newe=M*sp.Matrix(e)+offsets[r]-offsets[c]
  key=(brightfull.index(r),list(map(int,ONE[DARK])).index(c),tuple(map(int,newe)))
  transformed[key]+=v
 transformed={k:v for k,v in transformed.items() if v}
 check('dark-dark Laurent block exactly zero',not darkterms)
 claimed={(r['bright_row'],r['dark_column'],tuple(r['cycle_exponent'])):r['coefficient'] for r in author['bright_dark_Laurent_entries']}
 check('every author Laurent monomial and coefficient matches',transformed==claimed)
 Q=sp.zeros(72,24);Qflat=sp.zeros(72,24)
 for (r,c,e),v in transformed.items():Q[r,c]+=v*(-1 if e[0]%2 else 1);Qflat[r,c]+=v
 check('entire author integer witness reconstructed',Q.tolist()==author['Q_witness'])
 gram=Q.T*Q;check('entire author Gram matrix reconstructed',gram.tolist()==author['Gram_witness'])
 gdet=gram.det(method='domain-ge');minor=Q.extract(author['full_rank_minor_rows'],range(24));mdet=minor.det(method='domain-ge')
 check('exact root Gram determinant reconstructed',str(gdet)==author['Gram_determinant'])
 check('exact root minor determinant reconstructed',str(mdet)==author['full_rank_minor_determinant'])
 # Check the same point by direct use of the frozen PRE exact matrix engine.
 powers=tuple(int(2*M[0,k])%4 for k in range(5));G,loss,F=build(powers)
 gauge=sp.diag(*[(-1 if int(offsets[int(k)][0])%2 else 1) for k in ONE])
 rootG=gauge*G*gauge
 check('complete rank-witness block equals PRE engine after gauge',rootG.extract(list(map(int,BRIGHT)),list(map(int,DARK)))==Q)
 flatG,flatGamma,_=build((0,0,0,0,0));u=sp.zeros(96,1)
 for i in DARK:u[int(i)]=1
 check('zero phase dark kernel one dimensional',Qflat.rank()==23 and len(Qflat.nullspace())==1)
 check('flat vector killed by G and Gamma',flatG*u==sp.zeros(96,1) and flatGamma*u==sp.zeros(96,1))
 # A and A* kill u for all positive delta/kappa, because both G and Gamma do.
 omega={(tuple(int(v in A) for v in range(8)),(0,)*12):1};actual=[]
 for mark in (1,-1,0):
  bv=birthphysical(Fphysical(omega),mark);rv={q:-v for q,v in Fphysical(bv,0).items()}
  b=sum(v*v for v in bv.values());r=sum(v*v for v in rv.values());flat=sp.zeros(96,1)
  cert=[]
  for (q,E),v in sorted(rv.items()):
   wi=list(map(int,ONE)).index(INDEX[q]);check('R physical word dark',wi in DARK);flat[wi]+=v
   cert.append({'q':list(q),'E':list(E),'coefficient':v})
  residual=sp.simplify((u.T*flat)[0]**2/(24*sp.Integer(b)))
  row={'mark':mark,'b':b,'r':r,'flat_fiber_surviving_normalized_weight':str(residual),'physical_R':cert}
  expected=next(row for row in author['actual_first_mark_flat_fiber_weights'] if row['mark']==mark)
  check('all physical R entries and exact flat overlap for mark '+str(mark),row==expected)
  row['initial_flat_normalized_squared_norm']=str((flat.T*flat)[0]/b);row['sum_flat_amplitudes']=int(sum(flat));actual.append(row)
 # Exploratory numerical evidence is reproduced only as exploratory evidence.
 probe=json.loads((HERE/'post_sources/author/exploratory/FIBER_PROBE.json').read_text());rng=np.random.default_rng(20260924);probe_errors=[]
 for row in probe['rows']:
  t=row['trial'];powers12=None
  if t==0:edgephase=np.ones(12,complex)
  elif t<5:
   powers12=rng.integers(0,4,size=12).tolist();edgephase=np.array([1j**v for v in powers12])
  else:edgephase=np.exp(2j*np.pi*rng.random(12))
  check('recorded exploratory phase exponents '+str(t),powers12==row['fourth_root_exponents'])
  phases=tuple(np.prod([edgephase[e]**int(CI[e,k]) for e in range(12)]) for k in range(5))
  g,_,_=matrices(phases);coupling=g[np.ix_(BRIGHT,DARK)];sv=np.linalg.svd(coupling,compute_uv=False)
  err=float(max(abs(sv-np.array(row['BD_singular_values']))));dd=float(np.max(abs(g[np.ix_(DARK,DARK)])))
  check('exploratory singular values reproduced '+str(t),err<2e-12)
  check('exploratory ranks reproduced '+str(t),int(sum(sv>1e-10))==row['BD_rank_at_1e_10'])
  check('exploratory dark diagonal reproduced '+str(t),abs(dd-row['DD_max'])<2e-12)
  probe_errors.append({'trial':t,'maximum_singular_value_difference':err,'dark_block_difference':abs(dd-row['DD_max'])})
 single=json.loads((HERE/'post_sources/author/exploratory/SINGLE_EDGE_PROBE.json').read_text());single_errors=[]
 for row in single:
  edgephase=np.ones(12,complex);edgephase[row['edge']]=-1 if row['phase']=='-1' else 1j
  phases=tuple(np.prod([edgephase[e]**int(CI[e,k]) for e in range(12)]) for k in range(5));g,_,_=matrices(phases);sv=np.linalg.svd(g[np.ix_(BRIGHT,DARK)],compute_uv=False)
  check('single-edge exploratory rank '+str(row),int(sum(sv>1e-10))==row['rank'])
  check('single-edge exploratory minimum value '+str(row),abs(sv[-1]-row['smin'])<2e-12)
  single_errors.append(float(abs(sv[-1]-row['smin'])))
 return {'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'method':'Complete polynomial matrix products in frozen PRE cycle coordinates, then exact integral tree/gauge change; independent physical integer birth paths. No author code imported or run.','cycle_change_M':M.tolist(),'cycle_change_determinant':int(M.det()),'author_cycles_from_PRE_cycles':CA.tolist(),'all_168_reference_offsets':[list(map(int,v)) for v in offsets],'all_Laurent_entries_compared':len(claimed),'reconstructed_Laurent_entries':[{'bright_row':r,'dark_column':c,'cycle_exponent':e,'coefficient':v} for (r,c,e),v in sorted(transformed.items())],'author_integer_minor_determinant':str(mdet),'author_Gram_determinant':str(gdet),'author_minor_rows':author['full_rank_minor_rows'],'root_witness_powers_in_PRE_chart':powers,'root_witness_gauge_diagonal':[int(gauge[i,i]) for i in range(96)],'actual_first_mark_residuals':actual,'exploratory_probe_comparison':probe_errors,'single_edge_probe_absolute_differences':single_errors,'checks':checks,'all_assertions_passed':True,'scope':'Flat residuals are squared norms in one exceptional fiber, not survival probabilities in physical l2. Strong physical decay and order-of-limits restrictions remain those proved in PRE.'}

if __name__=='__main__':
 out=HERE/'POST_CERTIFICATE_RESULTS_01.json'
 if out.exists():raise FileExistsError(out)
 try:
  result=run();out.write_text(json.dumps(result,indent=2,default=int)+'\n')
  print(json.dumps({k:v for k,v in result.items() if k in ('cycle_change_M','cycle_change_determinant','all_Laurent_entries_compared','author_integer_minor_determinant','author_Gram_determinant','root_witness_powers_in_PRE_chart','actual_first_mark_residuals','all_assertions_passed')},indent=2,default=int));print('checks',len(checks))
 except Exception as error:
  out.write_text(json.dumps({'all_assertions_passed':False,'exception':repr(error),'traceback':traceback.format_exc(),'checks':checks},indent=2)+'\n');raise
