#!/usr/bin/env python3
# usage: ctx.py ROOT before after maxhits pattern [fileglob-substring ...]
import sys,os,re,io
root=sys.argv[1]; b=int(sys.argv[2]); a=int(sys.argv[3]); mx=int(sys.argv[4]); pat=re.compile(sys.argv[5],re.I)
subs=sys.argv[6:]
files=[]
for dp,dn,fn in os.walk(os.path.join(root,'library')):
    for f in fn:
        if f.endswith('.md'): files.append(os.path.join(dp,f))
files.append(os.path.join(root,'FINISH.md')); files.append(os.path.join(root,'parts/gap.md'))
files.sort()
n=0
for f in files:
    rel=os.path.relpath(f,root)
    if 'gap-afield-a-max' in rel: continue
    if subs and not any(s in rel for s in subs): continue
    try: s=io.open(f,encoding='utf-8',errors='replace').read()
    except Exception as e: continue
    for m in pat.finditer(s):
        st=max(0,m.start()-b); en=min(len(s),m.end()+a)
        ln=s.count('\n',0,m.start())+1
        snip=s[st:en].replace('\n',' / ')
        print(f"{rel}:{ln}: ...{snip}...")
        n+=1
        if n>=mx: sys.exit(0)
