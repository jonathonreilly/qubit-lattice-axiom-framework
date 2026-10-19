from pathlib import Path
import json,pickle,time
import numpy as np
import quimb as qu,quimb.tensor as qtn
from native_mpo import build,expectation,residual
P=Path(__file__).resolve().parent

def main():
 rows=[]
 for shape in [(4,4,6)]:
  start=time.monotonic();N=int(np.prod(shape));H=build(shape);qu.seed_rand(191000+N)
  initial=qtn.MPS_rand_state(N,bond_dim=4,phys_dim=2,dtype=float)
  dm=qtn.DMRG2(H,bond_dims=[8,16,32],cutoffs=1e-12,p0=initial);dm.opts.update(local_eig_tol=1e-9,local_eig_ncv=30,local_eig_maxiter=500)
  tag='x'.join(map(str,shape))
  for chi in [8,16,32]:
   flag=dm.solve(tol=0,bond_dims=chi,max_sweeps=4,verbosity=0);g=dm.state;g.normalize();e=expectation(g,H,g);r,var=residual(g,H,e)
   row=dict(shape=shape,N=N,bond_limit=chi,actual_bond=g.max_bond(),energy=e,residual=float(r),variance=float(var),seconds=time.monotonic()-start);rows.append(row)
   with (P/f'state_{tag}_{chi}.pkl').open('wb') as f:pickle.dump(g,f)
   (P/'volume_ground.json').write_text(json.dumps(dict(scope='Full native finite open 3D H, variational references; no exact sector or global-ground certificate',rows=rows),indent=2)+'\n');print(row,flush=True)
if __name__=='__main__':
 qtn.set_contract_strategy('greedy');main()
