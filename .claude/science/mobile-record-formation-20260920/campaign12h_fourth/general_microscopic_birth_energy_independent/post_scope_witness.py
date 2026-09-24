"""A bounded counterexample to extrapolating cube-input power positivity.
Uses the independently built POST matrices; this is not an author correction.
"""
from pathlib import Path
import json
import numpy as np
from scipy.sparse import diags
from scipy.linalg import eigh
from post_complete_k24 import construct
HERE=Path(__file__).resolve().parent
states,W,N,pidx,P,Fs,F,Cs,D,E2,instruments,inputs=construct()
word=((1,1,0,0,0,0),(-1,-1,1,1,1,1,-1,-1))
i=states.index(word);k=list(pidx).index(i);x=np.zeros(len(pidx));x[k]=1
assert W[i]==0 and N[i]==2 and D[i]==8 and E2[i]==8
lam=0.;eps=.01;h=diags(W.astype(float))-eps*(F+F.T)+eps**2*Cs
values,V=eigh(h.toarray(),driver='evd');low=V[:,abs(values)<.5]
overlap=low[pidx,:]@low[pidx,:].T;sv,svect=eigh(overlap)
UP=(low@low[pidx,:].T)@((svect/sv[None,:]**.5)@svect.T)
dressed=UP@x;hd=h@dressed
rows=[]
for label,operators in instruments.items():
 rate=fast=slowgain=slowloss=actual=0.
 for j,B,R in operators:
  b=B@x;r=R@x;bn=np.vdot(b,b).real
  rate+=bn;fast+=np.vdot(r,r).real;slowgain+=np.vdot(b,(D/2)*b).real
  slowloss+=np.vdot(x,(B.T@B)@((D[pidx]/2)*x)).real
  y=j@dressed;actual+=(np.vdot(y,h@y).real-np.vdot(y,j@hd).real)/eps**4
 predicted=fast+slowgain-slowloss
 assert predicted==-8 and actual<0
 rows.append({'instrument':label,'leading_total_rate':float(rate),'leading_fast_energy_gain':float(fast),'leading_slow_gain':float(slowgain),'leading_slow_loss':float(slowloss),'leading_scaled_power':float(predicted),'actual_scaled_power_at_epsilon_0_01':float(actual)})
result={'word':word,'edge_order':[[a,b] for a in (0,1) for b in (2,3,4,5)],'S':1,'lambda':0,'initial_population':2,'initial_D':8,'rows':rows,'scope':'Exact leading finite-spin operator expectation plus direct finite-epsilon microscopic check. Shows that positivity established for the cube single-square family must not be extended to arbitrary graph/flux/input. This is not an S-to-infinity counterexample, a universal negative theorem, or a discrepancy in the released note.','all_assertions_passed':True}
(HERE/'POST_SCOPE_WITNESS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
