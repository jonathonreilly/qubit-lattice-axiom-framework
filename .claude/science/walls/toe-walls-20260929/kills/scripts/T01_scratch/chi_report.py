import glob
from analyze import load, summarize
S = summarize(load(glob.glob('runs/*.csv')))
for c in 'UEAS':
    print('== clause', c, ' chi = N<|m|^2> (constant in L => no long-range order); a1')
    ps = sorted({k[1] for k in S if k[0]==c and k[2]==1.0 and k[3]==2.0})
    for p in ps:
        row=[]
        for L in (6,8,12,16):
            k=(c,p,1.0,2.0,L)
            if k in S:
                d=S[k]; row.append(f"L{L}: chi={d['m2']*L**3:7.3f}±{d['m2_se']*L**3:.3f} a1={d['a1']:.4f}")
        print(f' p={p:5g} '+' | '.join(row))
