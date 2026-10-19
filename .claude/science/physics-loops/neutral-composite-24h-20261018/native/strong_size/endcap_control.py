from pathlib import Path
import sys,json,pickle,time
import numpy as np
import quimb.tensor as qtn
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from native_rung import zs
I=np.eye(8)
def ex(g,ops):
 v=g.copy()
 for k,A in ops.items():v.gate_(A,k,contract=True)
 return float(np.real(g.H@v))
def word(cut,a):return {cut:zs[a],cut+1:zs[a]}
def mul(A,B):
 out=dict(A)
 for k,b in B.items():out[k]=out.get(k,I)@b
 return out
rows=[]
for L in [8,12,16]:
 with (P/f'stationary_tube_mps_refined_{L}.pkl').open('rb') as f:g=pickle.load(f)
 g.normalize();means=[2*sum(ex(g,word(z,a)) for a in [0,1]) for z in range(L-1)]
 vals=[]
 for ell in range(2,L-1,2):
  left=(L-ell)//2-1;right=left+ell
  cross=4*sum(ex(g,mul(word(left,a),word(right,b))) for a in [0,1] for b in [0,1])
  vals.append(dict(length=ell,left_cut=left,right_cut=right,endcap_energy=means[left]+means[right],connected_endcap_covariance=cross-means[left]*means[right]))
 rows.append(dict(L=L,cut_energies=means,lengths=vals));print(rows[-1],flush=True)
(P/'strong_size/endcap_control.json').write_text(json.dumps(dict(scope='Exact conjugation identity evaluated in variational MPS; connected covariance is not a binding potential',rows=rows),indent=2)+'\n')
