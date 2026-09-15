AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_L6_NONLINEAR_STAR_VERTEX_NOTE_2026-09-09.md', 'docs/NATIVE_THIRD_ORDER_STAR_VERTEX_NOTE_2026-09-08.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-adapted_frame-4eb81c02792f3306.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-four_solve-eff578cafd7f48f7.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-projection-e801411de605cecc.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_error-57d49d5cf78c0e3e.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_sign-c2692f5746303191.md', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/ADAPTED.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/BLOCKS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/COEFFICIENTS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/LEDGER.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/TRANSPORTS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/VECTOR_MANIFEST.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/INDEPENDENT_REVIEW.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/RESULT.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/ROOT_ACCEPTANCE.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/WORKER_COMPLETE.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/firstO_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/firstP_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/secondO_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/secondP_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/chi_real.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/chi_real.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstP.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondP.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceP.npy.gz')
"""Candidate exterior transport; physical-length action is not executed by controls."""
from pathlib import Path
from fractions import Fraction as F
import json,math
P=Path(__file__).resolve().parent
def blocks(index):
 rows=json.loads((P/'BLOCKS.json').read_text())
 if type(index) is not int or not 0<=index<48:raise ValueError('symmetry')
 row=rows[index];A=[[F(x) for x in r] for r in row['E_unscaled']]
 # Exact normalized entries represented as a+b sqrt3.
 E=[[(A[0][0],F(0)),(F(0),A[0][1]/3)],[(F(0),A[1][0]),(A[1][1],F(0))]]
 T=row['T'];table=[]
 for b in range(8):
  targets=[];sign=1
  for j in range(3):
   if b>>j&1:
    i=next(i for i in range(3) if T[i][j]);targets.append(i);sign*=T[i][j]
  sign*=(-1)**sum(targets[i]>targets[j] for i in range(len(targets)) for j in range(i+1,len(targets)))
  table.append((sum(1<<i for i in targets),sign))
 det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
 if det not in (-1,1):raise ValueError('det')
 return E,table,int(det)
def _eg(out,start,R,det):
 v=out.reshape(-1,4,1<<start);x=v[:,1,:].copy();y=v[:,2,:].copy();v[:,1,:]=R[0,0]*x+R[0,1]*y;v[:,2,:]=R[1,0]*x+R[1,1]*y;v[:,3,:]*=det
def _triplet(out,start,T):
 v=out.reshape(-1,8,1<<start);old=v.copy()
 for j,(i,s) in enumerate(T):v[:,i,:]=s*old[:,j,:]
def _last_eg(out,low,parity,R,det):
 import numpy as np
 n=1<<low;ids=np.arange(n,dtype=np.uint32);q=np.zeros(n,dtype=np.uint8)
 for shift in range(low):q^=((ids>>shift)&1).astype(np.uint8)
 odd=q!=parity;x=out[n:].copy();y=out[:n].copy()
 out[n:][odd]=R[0,0]*x[odd]+R[0,1]*y[odd];out[:n][odd]=R[1,0]*x[odd]+R[1,1]*y[odd];out[n:][~odd]*=det

def apply(vector,index,parity):
 import numpy as np
 if type(parity) is not int or parity not in (0,1):raise ValueError('parity')
 a=np.asarray(vector)
 if a.shape!=(1<<20,) or a.dtype not in (np.dtype('float64'),np.dtype('complex128')) or not np.isfinite(a).all():raise ValueError('candidate shape/dtype/finite')
 out=a.copy();E,T,det=blocks(index);R=np.array([[float(x)+float(y)*math.sqrt(3) for x,y in row] for row in E])
 for start in (1,7,13):_eg(out,start,R,det)
 for start in (3,9,15):_triplet(out,start,T)
 _last_eg(out,19,parity,R,det)
 return out
