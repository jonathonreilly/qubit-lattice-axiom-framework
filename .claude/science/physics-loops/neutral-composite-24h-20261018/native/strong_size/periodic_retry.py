from pathlib import Path
import sys,json,time,pickle
import numpy as np
import quimb as qu,quimb.tensor as qtn
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P))
from periodic_mps import pm,ex
def main():
 rows=[]
 for L in [16,24]:
  start=time.monotonic();H=pm(L);qu.seed_rand(72900+L)
  g=qtn.MPS_rand_state(L,bond_dim=16,phys_dim=8,dtype=float)
  dm=qtn.DMRG2(H,bond_dims=[32,64,96],cutoffs=1e-13,p0=g);dm.opts.update(local_eig_tol=1e-10,local_eig_ncv=40,local_eig_maxiter=1000)
  for chi in [32,64]:
   flag=dm.solve(tol=0,bond_dims=chi,max_sweeps=8,verbosity=0);g=dm.state;g.normalize();e=ex(g,H,g);r=H.apply(g,compress=False)-e*g;res=np.sqrt(max(0,float(np.real(r.H@r))));del r
   row=dict(L=L,bond_limit=chi,actual_bond=g.max_bond(),energy=e,residual=res,seconds=time.monotonic()-start);rows.append(row);print(row,flush=True)
   (P/'periodic_retry.json').write_text(json.dumps(rows,indent=2)+'\n')
  with (P/f'periodic_retry_state_{L}.pkl').open('wb') as f:pickle.dump(g,f)

if __name__=="__main__":
 qtn.set_contract_strategy("greedy")
 main()
