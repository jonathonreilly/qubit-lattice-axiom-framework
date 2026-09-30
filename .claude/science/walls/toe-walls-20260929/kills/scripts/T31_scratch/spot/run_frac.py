import sys, json, numpy as np
sys.path.insert(0,'.')
import hmc_unquench as H
Ns=float(sys.argv[1]); ntraj=int(sys.argv[2]); seed=int(sys.argv[3])
pl,acc,dH=H.run(6.0,Ns,0.1,ntraj,25,25,0.02,seed,verbose=False)
m,e=H.jack_err(pl)
print(f"RESULT Ns={Ns} (tastes={4*Ns}) P={m:.5f} +/- {e:.5f} acc={acc:.2f}")
json.dump(dict(Ns=Ns,P=m,err=e,acc=acc,ntraj=ntraj),open(f"frac_Ns{Ns}.json","w"))
