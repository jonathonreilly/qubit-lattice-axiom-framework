import sys, numpy as np
sys.argv=[sys.argv[0]]
src=open('step2_validate_L2.py').read().split("J, dtau = 4, 0.25")[0].replace('step2_validate_L2.jsonl','dbg_vend.jsonl')
exec(src)
for V,T,pr in [(0.9,1.0,[0.3,0.6,0.9,0.5]),(0.9,3.0,[0.3,0.6,0.9,0.5])]:
    ex=exact_open(V,T,4,0.25)
    vals=[]
    for seed in range(31,37):
        import driver
        r=run(2,V,T,nsweep=40000,ntherm=4000,seed=seed,mode=0,J=0,factor=2.0)
        vals.append(r['Nf_end'][0])
    m=np.mean(vals); se=np.std(vals,ddof=1)/np.sqrt(len(vals))
    print(V,T,pr,'Nf_end %.4f +- %.4f exact %.4f z=%.1f'%(m,se,ex['Nf_end'],(m-ex['Nf_end'])/se), np.round(vals,3), flush=True)
