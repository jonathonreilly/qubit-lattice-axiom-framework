"""Independent POST K(2,4) matrices, constructed from charges plus three cycles.

No author builder/code is imported. Unlike field-cube enumeration, the complete
basis starts with fixed-charge matter words; three tree-complement fields then
solve all Gauss equations. Compensation is built center by center with its gate.
The complete compressed adjoint generator is compared in operator norm, not
only on three inputs. Author JSON is consulted only for the final comparison.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json,datetime,hashlib,traceback,sys
sys.dont_write_bytecode=True
import numpy as np
from scipy.sparse import coo_matrix,diags,csr_matrix
from scipy.linalg import eigh
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,condition,detail=None):
 checks.append({'check':name,'passed':bool(condition),'detail':detail})
 if not condition:raise AssertionError((name,detail))

def charge_words(N):
 for occupied in combinations(range(6),N):
  for minus in combinations(occupied,(N-2)//2):
   yield tuple(-1 if x in minus else 1 if x in occupied else 0 for x in range(6))

def construct():
 A=(0,1);B=(2,3,4,5);edges=tuple((a,b) for a in A for b in B);states=[]
 for N in (2,4,6):
  for q in charge_words(N):
   for free in product((-1,0,1),repeat=3):
    top=free+(q[0]-1-sum(free),)
    bottom=tuple(-q[b]-top[b-2] for b in B)
    E=top+bottom
    if all(abs(e)<=1 for e in E):states.append((q,E))
 index={state:i for i,state in enumerate(states)};d=len(states)
 check('charge-cycle enumeration has no duplicate states',len(index)==d)
 for q,E in states:
  divergence=np.zeros(6,dtype=int)
  for (a,b),e in zip(edges,E):divergence[a]+=e;divergence[b]-=e
  check('Gauss word '+str((q,E)),np.array_equal(divergence,np.array(q)-np.array([1,1,0,0,0,0])))
 W=np.array([sum(q[a]==0 for a in A) for q,E in states]);N=np.array([sum(v*v for v in q) for q,E in states]);pidx=np.flatnonzero(W==0)
 select=csr_matrix((np.ones(len(pidx)),(pidx,np.arange(len(pidx)))),shape=(d,len(pidx)))
 D=np.array([sum(E[k]*(E[k]-q[a]) for k,(a,b) in enumerate(edges) if q[a] and not q[b]) for q,E in states],float)
 E2=np.array([sum(e*e for e in E) for q,E in states],float)
 Fs=[];Cs=csr_matrix((d,d))
 for a in A:
  rr=[];cc=[];vv=[];infinity=np.zeros(d);finite=np.zeros(d);gate=np.zeros(d)
  for col,(q,E) in enumerate(states):
   gate[col]=int(bool(q[1-a]))
   if not q[a]:continue
   for b in B:
    if q[b]:continue
    infinity[col]+=1;ei=edges.index((a,b));step=-q[a]
    if abs(E[ei]+step)>1:continue
    z=1-E[ei]*(E[ei]+step)/2
    check('spin-one legal transport has weight squared one',z==1)
    qq=list(q);ee=list(E);qq[a],qq[b]=0,q[a];ee[ei]+=step
    rr.append(index[(tuple(qq),tuple(ee))]);cc.append(col);vv.append(np.sqrt(z));finite[col]+=z
  F=coo_matrix((vv,(rr,cc)),shape=(d,d)).tocsr();Fs.append(F)
  block=F.T@F+diags(infinity-finite);G=diags(gate)
  defect=block@G-G@block;defect.eliminate_zeros()
  check('center compensation commutes with its independent occupancy gate '+str(a),defect.nnz==0)
  Cs+=block@G
 F=sum(Fs);T=-(F+F.T)
 defect=Cs-(select@(select.T@F.T@F@select)@select.T+diags((W==0)*D/2));defect.eliminate_zeros()
 check('local gated compensation equals separately derived P formula',defect.nnz==0)
 defect=diags(W)@Cs-Cs@diags(W);defect.eliminate_zeros();check('compensation preserves all W blocks',defect.nnz==0)
 jumps=[]
 for ei,(a,b) in enumerate(edges):
  pair=[]
  for sign in (1,-1):
   rr=[];cc=[];vv=[]
   for col,(q,E) in enumerate(states):
    if q[a] or q[b] or abs(E[ei]+sign)>1:continue
    z=1-E[ei]*(E[ei]+sign)/2
    check('spin-one legal original birth has weight squared one',z==1)
    qq=list(q);ee=list(E);qq[a],qq[b]=sign,-sign;ee[ei]+=sign
    row=index[(tuple(qq),tuple(ee))]
    check('birth changes N by two and W by minus one',N[row]==N[col]+2 and W[row]==W[col]-1)
    rr.append(row);cc.append(col);vv.append(np.sqrt(z))
   pair.append(coo_matrix((vv,(rr,cc)),shape=(d,d)).tocsr())
  jumps.append(pair)
 instruments={}
 for label in ('resolved','coherent'):
  js=[j for p in jumps for j in p] if label=='resolved' else [p[0]+p[1] for p in jumps]
  rows=[]
  for mu,j in enumerate(js):
   Bj=j@F@select;Rj=.5*j@F@F@select-F@Bj
   a=edges[mu//2 if label=='resolved' else mu][0]
   defect=Rj+Fs[a]@Bj;defect.eliminate_zeros();check(label+' all-P exact local R identity '+str(mu),defect.nnz==0)
   defect=diags(W)@Bj;defect.eliminate_zeros();check(label+' B lies in P '+str(mu),defect.nnz==0)
   defect=diags(W-1)@Rj;defect.eliminate_zeros();check(label+' R lies in Pi1 '+str(mu),defect.nnz==0)
   rows.append((j,Bj,Rj))
  instruments[label]=rows
 inputs=[]
 for n in (0,1):
  E=tuple({(0,2):n,(1,2):-n,(1,3):n,(0,3):-n}.get(e,0) for e in edges)
  x=np.zeros(len(pidx),complex);x[list(pidx).index(index[((1,1,0,0,0,0),E)])]=1
  inputs.append(('circulation_'+str(n),x))
 inputs.append(('coherent_two_flux_input',(inputs[0][1]+1j*inputs[1][1])/np.sqrt(2)))
 return states,W,N,pidx,select,Fs,F,Cs,D,E2,instruments,inputs

def go():
 states,W,N,pidx,select,Fs,F,Cs,D,E2,instruments,inputs=construct();d=len(states);rank=len(pidx)
 counts={str(k):v for k,v in sorted(Counter((int(n),int(w)) for n,w in zip(N,W)).items())}
 result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'basis_method':'matter charge words plus three independent cycle fields and exact Gauss solution','dimension':d,'P_dimension':rank,'sector_counts':counts,'matrix_rows':[],'operator_rows':[],'two_birth_rows':[],'checks':checks}
 eigenspaces={}
 for lam in (0.,.5,1.):
  Cfull=Cs+diags(lam*(E2-D)/2);Q=((1-lam)*D+lam*E2)/2;Qp=Q[pidx]
  predictions={}
  for label,operators in instruments.items():
   Eop=csr_matrix((rank,rank))
   for j,Bj,Rj in operators:
    Gamma=Bj.T@Bj
    Eop+=Bj.T@diags(Q)@Bj+Rj.T@Rj-.5*(Gamma@diags(Qp)+diags(Qp)@Gamma)
   predictions[label]=Eop.toarray()
   check('lambda '+str(lam)+' '+label+' predicted operator Hermitian',np.max(np.abs(predictions[label]-predictions[label].T))<1e-14)
  for eps in (.04,.02,.01):
   hs=diags(W)-eps*(F+F.T)+eps*eps*Cfull
   ev,V=eigh(hs.toarray(),driver='evd');low=V[:,abs(ev)<.5]
   check('isolated entire low cluster '+str((lam,eps)),low.shape[1]==rank)
   overlap=low[pidx,:]@low[pidx,:].T;sv,svect=eigh(overlap)
   check('positive overlap '+str((lam,eps)),min(sv)>.9,float(min(sv)))
   # Spectral projector polar isometry, with positive P overlap.
   UP=(low@low[pidx,:].T)@((svect/sv[None,:]**.5)@svect.T)
   check('canonical isometry '+str((lam,eps)),np.linalg.norm(UP.T@UP-np.eye(rank),ord=2)<5e-12)
   hlow=UP.T@(hs@UP)
   check('band invariance '+str((lam,eps)),np.linalg.norm(hs@UP-UP@hlow,ord=2)<2e-12)
   for label,operators in instruments.items():
    generator=csr_matrix((d,d))
    for j,Bj,Rj in operators:
     rate=j.T@j
     generator+=j.T@hs@j-.5*(rate@hs+hs@rate)
    actualop=(UP.T@(generator@UP))/eps**4
    defect=actualop-predictions[label]
    eigdef=eigh((defect+defect.T)/2,eigvals_only=True)
    error=float(max(abs(eigdef)))
    result['operator_rows'].append({'lambda':lam,'epsilon':eps,'instrument':label,'all_low_columns':rank,'scaled_power_operator_error_norm':error,'error_over_epsilon2':error/eps**2,'hermiticity_defect':float(np.max(np.abs(actualop-actualop.T))), 'minimum_predicted_operator_eigenvalue':float(eigh(predictions[label],eigvals_only=True)[0]), 'maximum_predicted_operator_eigenvalue':float(eigh(predictions[label],eigvals_only=True)[-1])})
    for name,x in inputs:
     dressed=UP@x;hd=hs@dressed;marks=[];blocked=0;directpower=0
     for mu,(j,Bj,Rj) in enumerate(operators):
      bv=Bj@x;rv=Rj@x;bn=float(np.vdot(bv,bv).real);rn=float(np.vdot(rv,rv).real)
      out=j@dressed;hout=hs@out;intensity=float(np.vdot(out,out).real);gain=float(np.vdot(out,hout).real)
      directpower+=(gain-float(np.vdot(out,j@hd).real))/eps**4
      if bn<1e-12:blocked+=1;continue
      mean=gain/intensity;second=float(np.vdot(hout,hout).real)/intensity
      predictedmean=(float(np.vdot(bv,Q*bv).real)+rn)/bn;predictedvar=rn/bn
      actualmean=mean/eps**2;actualvar=(second-mean**2)/eps**2
      marks.append({'mark_index':mu,'B_squared_norm':bn,'R_squared_norm':rn,'predicted_scaled_mean':predictedmean,'actual_scaled_mean':actualmean,'predicted_scaled_variance':predictedvar,'actual_scaled_variance':actualvar,'scaled_mean_error':abs(actualmean-predictedmean),'scaled_variance_error':abs(actualvar-predictedvar)})
     power=float(np.vdot(x,actualop@x).real);pred=float(np.vdot(x,predictions[label]@x).real)
     check('operator versus direct gain/loss '+str((lam,eps,label,name)),abs(power-directpower)<2e-8,abs(power-directpower))
     result['matrix_rows'].append({'lambda':lam,'epsilon':eps,'input':name,'instrument':label,'predicted_scaled_power':pred,'actual_scaled_power':power,'scaled_power_error':abs(power-pred),'max_scaled_mean_error':max(m['scaled_mean_error'] for m in marks),'max_scaled_variance_error':max(m['scaled_variance_error'] for m in marks),'leading_blocked_marks_not_normalized':blocked,'mark_moments':marks})
     if label=='resolved' and name=='circulation_0':
      twice=operators[14][0]@(operators[2][0]@dressed);norm=float(np.vdot(twice,twice).real)
      check('two actual births nonzero in complete N6 sector '+str((lam,eps)),norm>1e-12 and np.linalg.norm((N-6)*twice)<2e-14,norm)
      result['two_birth_rows'].append({'lambda':lam,'epsilon':eps,'ordered_marks':[[0,3,1],[1,5,1]],'unscaled_two_jump_squared_norm':norm,'entire_output_has_N6':True})
 for lam in (0.,.5,1.):
  for label in instruments:
   rs=[r for r in result['operator_rows'] if r['lambda']==lam and r['instrument']==label]
   check('all-P operator epsilon2 convergence '+str((lam,label)),rs[-1]['scaled_power_operator_error_norm']<rs[0]['scaled_power_operator_error_norm']/12)
 for lam in (0.,.5,1.):
  for label in instruments:
   for name,x in inputs:
    rs=[r for r in result['matrix_rows'] if r['lambda']==lam and r['instrument']==label and r['input']==name]
    for metric in ('scaled_power_error','max_scaled_mean_error','max_scaled_variance_error'):
     check('moment convergence '+str((lam,label,name,metric)),rs[-1][metric]<rs[0][metric]/8+2e-7)
 # Source-data comparison is a read-only last step; compare all recorded values.
 author=json.loads((HERE/'post_sources/author__COMPLETE_TWO_CENTER_RESULTS.json').read_text())
 check('author complete dimension independently reproduced',d==author['complete_Gauss_dimension'])
 check('author P dimension independently reproduced',rank==author['P_dimension'])
 check('every population/grade sector count independently reproduced',counts==author['sector_counts'])
 diffs=[]
 def compare(a,b,path):
  if isinstance(a,dict):
   check('matching result keys '+path,set(a)==set(b));
   for k in a:compare(a[k],b[k],path+'/'+k)
  elif isinstance(a,list):
   check('matching result list size '+path,len(a)==len(b))
   for k,(aa,bb) in enumerate(zip(a,b)):compare(aa,bb,path+'/'+str(k))
  elif isinstance(a,(str,bool)) or a is None:check('matching result text '+path,a==b)
  else:
   error=abs(a-b);relative=error/max(1,abs(a),abs(b));diffs.append({'field':path,'absolute_difference':error,'relative_difference':relative})
   check('author numeric reproduced '+path,relative<2e-8,relative)
 keyed={(r['lambda'],r['epsilon'],r['input'],r['instrument']):r for r in result['matrix_rows']}
 for i,r in enumerate(author['rows']):compare(keyed[(r['lambda'],r['epsilon'],r['input'],r['instrument'])],r,'rows/'+str(i))
 two={(r['lambda'],r['epsilon']):r for r in result['two_birth_rows']}
 for i,r in enumerate(author['actual_two_birth_nonzero_controls']):compare(two[(r['lambda'],r['epsilon'])],r,'two_birth/'+str(i))
 result['author_comparison']={'all_36_complete_author_rows_compared':True,'all_6_author_two_birth_rows_compared':True,'numeric_fields':len(diffs),'maximum_absolute_difference':max(r['absolute_difference'] for r in diffs),'maximum_relative_difference':max(r['relative_difference'] for r in diffs),'differences':diffs}
 result['all_assertions_passed']=True
 return result

if __name__=='__main__':
 out=HERE/'POST_COMPLETE_K24_RESULTS_01.json'
 if out.exists():raise FileExistsError(out)
 try:
  result=go();out.write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps({'all_assertions_passed':True,'checks':len(checks),'dimension':result['dimension'],'P_dimension':result['P_dimension'],'matrix_rows':len(result['matrix_rows']),'operator_rows':result['operator_rows'],'author_comparison':{k:v for k,v in result['author_comparison'].items() if k!='differences'}},indent=2))
 except Exception as error:
  out.write_text(json.dumps({'all_assertions_passed':False,'exception':repr(error),'traceback':traceback.format_exc(),'checks':checks},indent=2)+'\n');raise
