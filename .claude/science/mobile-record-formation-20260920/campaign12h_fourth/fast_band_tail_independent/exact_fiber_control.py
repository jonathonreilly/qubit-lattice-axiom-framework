"""Exact Gaussian-integer certificate for generic rotor-fiber damping.

F, j and G are reconstructed on the complete physical charge labels. A single
nonzero Laurent-polynomial minor of bright*G*dark is certified at chord phases
(1,1,1,1,i), both by exact determinant and modular elimination. The zero-phase
fiber is separately checked; no claim is inferred from a numerical rank.
"""
from pathlib import Path
import json,hashlib,datetime,traceback
import sympy as sp
from fiber_engine import A,B,EDGES,TREE,CHORDS,WORDS,INDEX,GRADES,ONE,DARK,BRIGHT,words,reference,gauss
HERE=Path(__file__).resolve().parent
checks=[]
def check(label,value):
 checks.append({'check':label,'passed':bool(value)})
 if not value:raise AssertionError(label)

def build(powers):
 F=sp.MutableSparseMatrix(len(WORDS),len(WORDS),{})
 def phase(edge,shift):return sp.I**(powers[CHORDS.index(edge)]*shift) if edge in CHORDS else 1
 for col,q in enumerate(WORDS):
  for a,b in EDGES:
   if q[a] and not q[b]:
    qq=list(q);qq[a],qq[b]=0,q[a]
    F[INDEX[tuple(qq)],col]+=phase((a,b),-q[a])
 G=(F*F.conjugate().T-F.conjugate().T*F).extract(list(map(int,ONE)),list(map(int,ONE)))
 terminal=tuple(words(8));ix={q:i for i,q in enumerate(terminal)}
 resolved=sp.zeros(len(ONE));coherent=sp.zeros(len(ONE))
 for edge in EDGES:
  a,b=edge;pair=[]
  for sign in (1,-1):
   j=sp.MutableSparseMatrix(len(terminal),len(ONE),{})
   for col,k in enumerate(ONE):
    q=WORDS[k]
    if q[a] or q[b]:continue
    qq=list(q);qq[a],qq[b]=sign,-sign
    j[ix[tuple(qq)],col]=phase(edge,sign)
   pair.append(j);resolved+=j.conjugate().T*j
  check('resolved ranges orthogonal '+str((powers,edge)),pair[0].conjugate().T*pair[1]==sp.zeros(len(ONE)))
  j=pair[0]+pair[1];coherent+=j.conjugate().T*j
 expected=sp.diag(*[0 if n in DARK else 2 for n in range(len(ONE))])
 check('complete exact Gamma from original marks '+str(powers),resolved==coherent==expected)
 check('complete exact G Hermitian '+str(powers),G==G.conjugate().T)
 return G,resolved,F

def modval(z,p=5,iimage=2):
 re,im=sp.expand(z).as_real_imag();assert re.is_Integer and im.is_Integer
 return (int(re)+iimage*int(im))%p

def independent_rows_mod(matrix,p=5,iimage=2):
 # Eliminate the transposed matrix: pivot columns select rows of the original.
 data=[[modval(matrix[c,r],p,iimage) for c in range(matrix.rows)] for r in range(matrix.cols)]
 pivotcols=[];pivot=0;factors=[]
 for col in range(matrix.rows):
  at=next((r for r in range(pivot,matrix.cols) if data[r][col]),None)
  if at is None:continue
  data[pivot],data[at]=data[at],data[pivot]
  z=data[pivot][col];factors.append(z);inv=pow(z,-1,p)
  data[pivot]=[(v*inv)%p for v in data[pivot]]
  for r in range(matrix.cols):
   if r!=pivot:
    z=data[r][col]
    if z:data[r]=[(v-z*w)%p for v,w in zip(data[r],data[pivot])]
  pivotcols.append(col);pivot+=1
  if pivot==matrix.cols:break
 return pivotcols

def encode(z):
 re,im=sp.expand(z).as_real_imag();return [int(re),int(im)]

def run():
 check('complete N6 charge-label dimension',len(WORDS)==168)
 check('W1 dimension and dark/bright split',len(ONE)==96 and len(DARK)==24 and len(BRIGHT)==72)
 for q in WORDS:check('integral tree reference satisfies Gauss '+str(q),gauss(q,reference(q)))
 # Validate that a link move changes exactly its chord coordinate. Since the
 # difference has zero divergence and zero chord components, the tree part
 # must vanish, by uniqueness of tree flow.
 chord_cycles=[]
 q0=tuple(int(v in A) for v in range(8))
 for edge in CHORDS:
  a,b=edge;div=[0]*8;div[a]=1;div[b]=-1
  q=tuple(q0[v]+div[v] for v in range(8))
  treepart=reference(q)
  cycle=[-e for e in treepart];cycle[EDGES.index(edge)]=1
  check('independent fundamental cycle '+str(edge),gauss(q0,cycle))
  chord_cycles.append(cycle)
 for col,q in enumerate(WORDS):
  for a,b in EDGES:
   if not q[a] or q[b]:continue
   step=-q[a];qq=list(q);qq[a],qq[b]=0,q[a]
   actual=list(reference(q));actual[EDGES.index((a,b))]+=step
   target=list(reference(tuple(qq)))
   if (a,b) in CHORDS:
    target=[v+step*w for v,w in zip(target,chord_cycles[CHORDS.index((a,b))])]
   check('exact Gauss-coordinate intertwining '+str((col,a,b)),actual==target)
 G,gamma,F=build((0,0,0,0,1))
 coupling=G.extract(list(map(int,BRIGHT)),list(map(int,DARK)))
 pivots=independent_rows_mod(coupling)
 check('modular full column rank of bright-G-dark',len(pivots)==24)
 minor=coupling.extract(pivots,list(range(24)))
 determinant=sp.expand(minor.det(method='domain-ge'))
 check('exact Gaussian determinant nonzero',determinant!=0)
 check('determinant modular residue nonzero',modval(determinant)!=0)
 G0,gamma0,F0=build((0,0,0,0,0));coupling0=G0.extract(list(map(int,BRIGHT)),list(map(int,DARK)))
 kernel=coupling0.nullspace();check('zero-fiber coupling kernel dimension',len(kernel)==1)
 v=sp.zeros(96,1)
 for k,i in enumerate(DARK):v[int(i),0]=kernel[0][k,0]
 denom=sp.ilcm(*[sp.denom(x) for x in v]);v*=denom
 integers=[int(x) for x in v];gcd=sp.igcd(*[abs(x) for x in integers if x]);v=v/gcd
 check('zero-fiber vector remains dark under G',G0*v==sp.zeros(96,1))
 check('zero-fiber vector is annihilated by original Gamma',gamma0*v==sp.zeros(96,1))
 result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dimensions':{'N6_all_W':168,'W1':96,'dark':24,'bright':72},'A':A,'B':B,'oriented_edges':EDGES,'tree':TREE,'chords':CHORDS,'fundamental_cycles':chord_cycles,'generic_certificate':{'phase_powers_of_i':[0,0,0,0,1],'prime':5,'image_of_i':2,'selected_bright_local_rows':pivots,'selected_W1_rows':[int(BRIGHT[i]) for i in pivots],'dark_W1_columns':list(map(int,DARK)),'minor_gaussian_pairs':[[encode(z) for z in row] for row in minor.tolist()],'exact_determinant':str(determinant),'determinant_mod_5':modval(determinant),'modular_rank':len(pivots)},'zero_fiber':{'phase_powers_of_i':[0,0,0,0,0],'coupling_rank':24-len(kernel),'dark_eigenvalue':0,'integer_vector_norm_squared':int((v.T*v)[0]),'nonzero_components':[{'W1_index':i,'charge_word':WORDS[int(ONE[i])],'coefficient':int(v[i])} for i in range(96) if v[i]]},'checks':checks,'all_assertions_passed':True,'scope':'Exact finite fiber certificate plus physical Gauss-coordinate intertwining. Physical strong stability requires the analytic zero-set and dominated-convergence proof; zero-fiber vector alone is not normalizable in l2(Z^5).'}
 return result

if __name__=='__main__':
 out=HERE/'EXACT_FIBER_RESULTS_01.json'
 if out.exists():raise FileExistsError(out)
 try:
  result=run();out.write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps({'all_assertions_passed':True,'checks':len(checks),'certificate_determinant':result['generic_certificate']['exact_determinant'],'determinant_mod_5':result['generic_certificate']['determinant_mod_5'],'zero_fiber':result['zero_fiber'],'scope':result['scope']},indent=2))
 except Exception as error:
  out.write_text(json.dumps({'all_assertions_passed':False,'exception':repr(error),'traceback':traceback.format_exc(),'checks':checks},indent=2)+'\n');raise
