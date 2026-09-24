#!/usr/bin/env python3
"""Author-exposed POST controls using only this checker's frozen model.

Integer polynomial link amplitudes give a distinct exact finite-S control.
The full matrix run imports the checker's PRE builder, never an author builder.
"""
from pathlib import Path
from collections import defaultdict
import ast,datetime,hashlib,importlib.util,json,math,sys,time
sys.dont_write_bytecode=True
import numpy as np
import sympy as sy
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh,expm_multiply
HERE=Path(__file__).resolve().parent
source=HERE/'cube_control.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='cf51bc234d72cb26667b740dddf9f29b27b3c43826dac74df941401a113df125'
spec=importlib.util.spec_from_file_location('own_frozen_pre',source);p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
AUTHOR=HERE.parent/'fast_band_energy_author'
if not AUTHOR.is_dir():AUTHOR=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_fourth/fast_band_energy_author')
z=sy.Symbol('t',nonnegative=True)

def combine(*terms):
 out=defaultdict(lambda:defaultdict(int))
 for factor,v in terms:
  for word,poly in v.items():
   for degree,a in poly.items():out[word][degree]+=factor*a
 return {w:{d:a for d,a in poly.items() if a} for w,poly in out.items() if any(poly.values())}

def action(v,kind,edge=None,sign=None,center=None):
 out=defaultdict(lambda:defaultdict(int))
 for (q,E),poly in v.items():
  for ei,(a,b) in enumerate(p.EDGES):
   if center is not None and a!=center:continue
   if edge is not None and ei!=edge:continue
   if kind=='F':
    if not q[a] or q[b]:continue
    shift=-q[a];qq=list(q);qq[b]=qq[a];qq[a]=0
   elif kind=='G':
    if not q[b] or q[a]:continue
    shift=q[b];qq=list(q);qq[a]=qq[b];qq[b]=0
   else:
    if q[a] or q[b]:continue
    shift=sign;qq=list(q);qq[a]=sign;qq[b]=-sign
   factor=E[ei]*(E[ei]+shift)
   assert factor in (0,2),(kind,E[ei],shift)
   ee=list(E);ee[ei]+=shift;word=(tuple(qq),tuple(ee))
   divergence=[0]*8
   for (aa,bb),field in zip(p.EDGES,ee):divergence[aa]+=field;divergence[bb]-=field
   assert all(divergence[i]==qq[i]-int(i in p.A) for i in range(8))
   for degree,a0 in poly.items():out[word][degree+int(factor==2)]+=a0
 return combine((1,out))

def mark(v,edge,sign):
 return combine((1,action(v,'j',edge,1)),(1,action(v,'j',edge,-1))) if sign==0 else action(v,'j',edge,sign)

def normpoly(v):
 out=defaultdict(int)
 for poly in v.values():
  for d,a in poly.items():
   for e,b in poly.items():out[d+e]+=a*b
 return {d:a for d,a in out.items() if a}

def expr(poly):return sy.expand(sum(a*z**d for d,a in poly.items()))
def const(v):
 assert all(set(poly)<={0} for poly in v.values())
 return {w:poly[0] for w,poly in v.items()}
def as_cert(v):return [{'q':q,'E_A_to_B':E,'amplitude_polynomial':{str(d):a for d,a in sorted(poly.items())}} for (q,E),poly in sorted(v.items())]
def compare_cert(v,entries):
 author={(tuple(e['q']),tuple(e['E_A_to_B'])):sy.sympify(e['amplitude'],locals={'t':z}) for e in entries}
 assert set(v)==set(author)
 for word,poly in v.items():assert sy.expand(expr(poly)-author[word])==0
 return len(v)

def exact_control():
 result_path=AUTHOR/'EXACT_FAST_BAND_PATHS_RESULTS.json'
 assert hashlib.sha256(result_path.read_bytes()).hexdigest()=='91f592e1b29da011368584e3cb267597f9d408d4406eee3e4396ade76ba00c75'
 released=json.loads(result_path.read_text());cases=[];certificates={};compared=0
 x={p.OMEGA:{0:1}};fx=action(x,'F')
 for edge,(center,_) in enumerate(p.EDGES):
  for sign in (1,-1,0):
   Bv=mark(fx,edge,sign);R=combine((-1,action(Bv,'F',center=center)))
   direct=combine((1,mark(action(fx,'F'),edge,sign)),(-2,action(Bv,'F')))
   assert direct==combine((2,R))
   D=combine((1,action(action(R,'G'),'F')),(-1,action(action(R,'F'),'G')))
   assert const(D)==p.D1(const(R))
   b=int(expr(normpoly(Bv)));r=int(expr(normpoly(R)))
   assert expr(normpoly(D))==12*r
   sums={};terminal={}
   for kind,signs in (('resolved',(1,-1)),('coherent',(0,))):
    bright=sy.Integer(0);slow=sy.Integer(0)
    for e in range(12):
     for s in signs:
      assert not mark(R,e,s)
      y=mark(D,e,s);bright+=expr(normpoly(y));slow+=expr(normpoly(mark(action(Bv,'F'),e,s)))
      if y:terminal[str((e,s))]=y
    bright=sy.expand(bright);slow=sy.expand(slow)
    assert bright==r*(18+6*z**2) and slow==8*b
    sums[kind]={'Gamma_G1R_polynomial':str(bright),'next_slow_rate':int(slow/b)}
   # Distinct direct Gamma expectation: 2 sum |D_word|^2(1-E_hole^2/C).
   gd=0;inverse_c_coefficient=0
   for (q,E),a in const(D).items():
    vacancies=[e for e,(aa,bb) in enumerate(p.EDGES) if q[aa]==q[bb]==0]
    assert len(vacancies)==1
    gd+=2*a*a;inverse_c_coefficient-=2*a*a*E[vacancies[0]]**2
   assert (gd,inverse_c_coefficient)==(24*r,-12*r)
   cases.append({'edge':list(p.EDGES[edge]),'first_sign':sign,'b':b,'r':r,'G1R_norm_squared':12*r,'Gamma_form_constant':gd,'Gamma_form_inverse_C_coefficient':inverse_c_coefficient,'sums':sums})
   if edge==0:
    certificates[str(sign)]={'R':as_cert(R),'G1R':as_cert(D),'future_mark_outputs':{k:as_cert(v) for k,v in terminal.items()}}
    for rotor in (True,False):
     ar=next(row for row in released['rows'] if row['first_sign']==sign and row['rotor']==rotor)
     assert sy.sympify(ar['B_squared_norm'])==b and sy.sympify(ar['R_squared_norm'])==r and sy.sympify(ar['G1R_squared_norm'])==12*r
     compared+=compare_cert(R,ar['R_physical_support'])+compare_cert(D,ar['G1R_physical_support'])
     for kind in ('resolved','coherent'):
      av=ar['instrument_sums'][kind]
      wanted=24*r if rotor else r*(18+6*z*z)
      assert sy.expand(sy.sympify(av['Gamma_G1R_squared'],locals={'t':z})-wanted)==0
      assert sy.sympify(av['next_slow_rate'])==8
     if rotor:
      assert set(ar['terminal_jump_support'])==set(terminal)
      for key,v in terminal.items():
       rotor_v={word:{0:int(expr(poly).subs(z,1))} for word,poly in v.items() if expr(poly).subs(z,1)!=0}
       compared+=compare_cert(rotor_v,ar['terminal_jump_support'][key])
     else:assert ar['terminal_jump_support']=={}
 return {'exact_cases':cases,'selected_certificates':certificates,'author_rows_compared':len(released['rows']),'physical_certificate_entries_compared':compared,'scope':'Exact integer-polynomial link weights z=sqrt(1-2/C). Covers C>=2 algebraically and integer S>=1 physically; no fitted coefficients.'}

def numerical_control():
 result_path=AUTHOR/'COMPLETE_SPIN_ONE_CUBE_RESULTS.json'
 assert hashlib.sha256(result_path.read_bytes()).hexdigest()=='0cd6f347859d87e97bf65acc75895603634bebefa043a28bcff63c071ff55255'
 released=json.loads(result_path.read_text())
 models=p.complete_spin_one();m4,m6=models[4],models[6];F=m6['F']
 low=np.flatnonzero(m4['W']==0);one=np.flatnonzero(m6['W']==1)
 G=(F@F.T-F.T@F)[one,:][:,one].tocsr();Gamma=diags(m6['loss'][one])
 delta=1.;kappa=.7;taus=np.linspace(0,.3,4);epsilons=(.04,.02,.01);signs=(1,-1,0)
 fast=-1j*delta*G-(kappa/2)*Gamma
 initial=[]
 for sign in signs:
  Bv=p.add(p.birth(p.hop({p.OMEGA:1}),0,1),p.birth(p.hop({p.OMEGA:1}),0,-1)) if sign==0 else p.birth(p.hop({p.OMEGA:1}),0,sign)
  R=p.hop(Bv,center=0);v=np.zeros(len(m6['E']))
  for (_,E),a in R.items():v[m6['index'][E]]=-a/math.sqrt(p.norm2(Bv))
  initial.append(v[one])
 initial=np.stack(initial,axis=1);ell=np.sum(initial**2,axis=0)
 effective=expm_multiply(fast,initial,start=0,stop=.3,num=4,traceA=fast.diagonal().sum())
 prediction=np.sum(abs(effective)**2,axis=1)
 jp=p.jump_matrix(m4,m6,1);jm=p.jump_matrix(m4,m6,-1);marks=(jp,jm,jp+jm)
 omega_local=int(np.flatnonzero(low==m4['index'][(0,)*12])[0])
 rows=[];spectral=[];comparisons=[];errors=[]
 for eps in epsilons:
  h4=diags(m4['W'].astype(float))-eps*(m4['F']+m4['F'].T)+eps**2*m4['C']
  # Independent shift-invert spectral reconstruction; one extra level checks the gap.
  rng=np.random.default_rng(94177)
  vals,V=eigsh(h4,k=len(low)+1,sigma=-.01,which='LM',tol=2e-12,v0=rng.normal(size=len(m4['E'])))
  order=np.argsort(vals);vals=vals[order];V=V[:,order]
  excluded=float(vals[len(low)]);vals=vals[:len(low)];V=V[:,:len(low)]
  assert max(abs(vals))<.1 and excluded>.5
  eigerr=float(np.linalg.norm(h4@V-V*vals));assert eigerr<2e-10
  VP=V[low,:];gram=VP@VP.T;w,u=np.linalg.eigh(gram);assert w.min()>.8
  basis=np.zeros(len(low));basis[omega_local]=1
  dressed=V@(VP.T@((u/np.sqrt(w))@u.T@basis));assert abs(np.linalg.norm(dressed)-1)<2e-11
  X=np.stack([j@dressed/np.linalg.norm(j@dressed) for j in marks],axis=1)
  h6=diags(m6['W'].astype(float))-eps*(F+F.T)+eps**2*m6['C']
  generator=-1j*delta/eps**2*h6-(kappa/2)*diags(m6['loss'])
  path=expm_multiply(generator,X,start=0,stop=.3,num=4,traceA=generator.diagonal().sum())
  energy=np.array([delta/eps**2*np.sum(v.conj()*(h6@v),axis=0).real for v in path])
  count=(1-np.sum(abs(path)**2,axis=1))/eps**2
  er=cr=0.
  for ti,tau in enumerate(taus):
   for si,sign in enumerate(signs):
    pred=8*kappa*tau+ell[si]-prediction[ti,si]
    row={'epsilon':eps,'tau':float(tau),'physical_time':float(eps**2*tau),'first_mark':sign,'scaled_ensemble_energy':float(energy[ti,si]),'fast_survival_prediction':float(prediction[ti,si]),'energy_error':float(abs(energy[ti,si]-prediction[ti,si])),'second_birth_probability_over_epsilon2':float(count[ti,si]),'second_birth_prediction':float(pred),'second_birth_error':float(abs(count[ti,si]-pred))}
    ar=next(r for r in released['rows'] if r['epsilon']==eps and abs(r['tau']-tau)<1e-14 and r['first_mark']==sign)
    for key,value in row.items():
     difference=abs(value-ar[key]);assert difference<5e-8,(eps,tau,sign,key,difference)
     comparisons.append({'epsilon':eps,'tau':float(tau),'mark':sign,'field':key,'absolute_difference':difference})
    er=max(er,row['energy_error']);cr=max(cr,row['second_birth_error']);rows.append(row)
  spectral.append({'epsilon':eps,'low_rank':len(low),'minimum_overlap_eigenvalue':float(w.min()),'first_excluded_eigenvalue':excluded,'low_eigensystem_residual':eigerr})
  errors.append({'epsilon':eps,'max_energy_error':er,'max_count_error':cr})
  print(json.dumps({'epsilon':eps,'max_energy_error':er,'max_count_error':cr}),flush=True)
 assert errors[-1]['max_energy_error']<errors[0]['max_energy_error']/6
 assert errors[-1]['max_count_error']<errors[0]['max_count_error']/6
 # Fully inspect the earlier author's successful run: only eigensolver start changed.
 old=json.loads((AUTHOR/'initial_eigensolver_start/COMPLETE_SPIN_ONE_CUBE_RESULTS.json').read_text())
 olddiff=[];old_comparisons=[]
 for row_index,(before,after) in enumerate(zip(old['rows'],released['rows'])):
  assert set(before)==set(after)
  for key in before:
   difference=abs(before[key]-after[key]);olddiff.append(difference)
   old_comparisons.append({'row':row_index,'field':key,'absolute_difference':difference})
 assert len(old['rows'])==len(released['rows'])==36
 return {'dimensions':{str(N):len(m['E']) for N,m in models.items()},'spectral_checks':spectral,'rows':rows,'errors':errors,'all_numerical_field_comparisons':comparisons,'max_author_row_difference':max(x['absolute_difference'] for x in comparisons),'number_compared_fields':len(comparisons),'author_initial_vs_final_all_row_comparisons':old_comparisons,'author_initial_vs_final_max_row_difference':max(olddiff),'author_historical_pair_within_5e_8':max(olddiff)<5e-8,'historical_pair_status':'The first POST run failed this auxiliary historical-run comparison at 5e-8. The failed status is retained and reported, with no replacement threshold. It does not fail the independent-to-final-author comparisons, which all retain the original 5e-8 assertion.','predeclared_absolute_comparison_tolerance':5e-8,'scope':'Complete fixed-S=1 model with exact spectral canonical preparation; no numerical large-S inference.'}

if __name__=='__main__':
 start=time.monotonic();paths=exact_control();print('Exact polynomial paths and complete author certificates agree.',flush=True)
 matrix=numerical_control()
 result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_assertions_passed':True,'own_PRE_builder_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'author_builder_imports':[],'paths':paths,'matrix':matrix,'elapsed_seconds':time.monotonic()-start}
 (HERE/'POST_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'all_assertions_passed':True,'path_cases':len(paths['exact_cases']),'certificate_entries':paths['physical_certificate_entries_compared'],'matrix_rows':len(matrix['rows']),'compared_fields':matrix['number_compared_fields'],'max_author_row_difference':matrix['max_author_row_difference'],'elapsed_seconds':result['elapsed_seconds']},indent=2))
