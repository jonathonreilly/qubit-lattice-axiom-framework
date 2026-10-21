import sys, numpy as np
sys.argv=[sys.argv[0]]
src=open('step2_validate_L2.py').read().split("J, dtau = 4, 0.25")[0].replace('step2_validate_L2.jsonl','dbg_v09.jsonl')
exec(src)
ex=exact_open(0.9,8.0,4,0.25)
print('exact', {k:(round(v,4) if not isinstance(v,list) else [round(x,4) for x in v]) for k,v in ex.items()}, flush=True)
for seed in (21,22,23):
    r=run(2,0.9,8.0,nsweep=150000,ntherm=20000,seed=seed,mode=0,J=4,dtau=0.25,factor=2.0)
    print(seed, 'Nf_mid',r['Nf_mid'],'ST1',r['ST1'],'C1',r['C'][1], 'bins ST1', r['ST1_bins'][-4:], flush=True)
