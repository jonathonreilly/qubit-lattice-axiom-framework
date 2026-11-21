import re,glob,sys
files=['parts/hard-core--mapped.md','parts/upper-chain.md']+sorted(glob.glob('library/*.md'))
skip={'shelling-by-hand','adapted-domains','tail-two-step','tail-two-step-c','conditional-normalization','cn-tree','pos-beta','signed-cut'}
pat=re.compile(r't_0|t0')
ineq=re.compile(r'(?:t_0[^.;,]{0,40}(?:<=|≤|<|\\le|at most|below|small)|(?:>=|≥|>|at least|larger)[^.;,]{0,30}t_0|exp\([^)]*t_0|t_0\^|\^\{?t_0|L\^t_0|2\^t_0|[0-9]\^\(?t_0|log t_0|/t_0|/ t_0)')
for f in files:
    b=f.split('/')[-1][:-3]
    if b in skip or b.startswith('mixed-coefficient'): continue
    try: t=open(f).read().split('\n')
    except: continue
    n=0
    for i,l in enumerate(t,1):
        if 't_0' in l:
            n+=1
            for m in ineq.finditer(l):
                s=max(0,m.start()-70); e=min(len(l),m.end()+70)
                print(f"{b}:{i}: ...{l[s:e]}...")
    
