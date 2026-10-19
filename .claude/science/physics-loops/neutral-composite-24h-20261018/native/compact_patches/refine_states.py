from pathlib import Path
import json,pickle,time
import numpy as np
import quimb.tensor as qtn
from native_mpo import build,expectation,residual
P=Path(__file__).resolve().parent

def main():
 rows=[]
 for shape in [(3,4,4),(3,4,6),(3,6,6)]:
  start=time.monotonic();tag='x'.join(map(str,shape));H=build(shape);g=pickle.loads((P/f'state_{tag}_32.pkl').read_bytes());dm=qtn.DMRG2(H,bond_dims=64,cutoffs=1e-13,p0=g);dm.opts.update(local_eig_tol=1e-10,local_eig_ncv=40,local_eig_maxiter=700)
  for chi in [64,128]:
   dm.solve(tol=0,bond_dims=chi,max_sweeps=8,verbosity=0);g=dm.state;g.normalize();e=expectation(g,H,g);r,var=residual(g,H,e)
   row=dict(shape=shape,bond=chi,energy=e,residual=float(r),variance=float(var),seconds=time.monotonic()-start);rows.append(row);print(row,flush=True)
   (P/'refine_states.json').write_text(json.dumps(rows,indent=2)+'\n')
   with (P/f'state_{tag}_{chi}.pkl').open('wb') as f:pickle.dump(g,f)
if __name__=='__main__':
 qtn.set_contract_strategy('greedy');main()
