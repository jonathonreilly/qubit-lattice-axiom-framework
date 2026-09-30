import glob, math, sys
from analyze import load, summarize
files=[f for f in glob.glob('runs/*.csv')]
S=summarize(load(files))
for w in [(3,1,2),(5,2,4),(7,3,5)]:
    print('== weights',w)
    for L in (4,6,8,12):
        row={}
        for c in 'UEAS':
            k=(c,)+tuple(map(float,w))+(L,)
            if k in S: row[c]=S[k]
        if len(row)<4: continue
        def d(a,b,key='a1'):
            x=row[a][key]-row[b][key]; se=math.hypot(row[a][key+'_se'],row[b][key+'_se']); return x,se
        print(f"L={L:2d} n={row['U']['n']:7d} a1: U={row['U']['a1']:.6f} E={row['E']['a1']:.6f} A={row['A']['a1']:.6f} S={row['S']['a1']:.6f} | se(U)={row['U']['a1_se']:.1e}")
        for a,b in [('U','E'),('U','A'),('U','S'),('E','A')]:
            x,se=d(a,b); print(f"     {a}-{b}: {x:+.6f} ({x/se:+.1f} sigma)", end='')
        print()
        print("     adiag: "+' '.join(f"{c}={row[c]['adiag']:.6f}" for c in 'UEAS')+"  s: "+' '.join(f"{c}={row[c]['s']:+.5f}({row[c]['s_se']:.1e})" for c in 'UEAS'))
