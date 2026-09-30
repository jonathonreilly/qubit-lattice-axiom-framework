import math, itertools, importlib.util
spec = importlib.util.spec_from_file_location('t', 'test_T73.py')
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
# independent brute-force MIS of cycle C_P
def cyc_mis(P):
    out=[]
    for m in range(1<<P):
        ok=True
        for i in range(P):
            a=m>>i&1; b=m>>((i+1)%P)&1
            if a and b: ok=False;break
        if not ok: continue
        # maximal
        for i in range(P):
            if not(m>>i&1) and not(m>>((i-1)%P)&1) and not(m>>((i+1)%P)&1): ok=False;break
        if ok: out.append(m)
    return out
for P in (8,12,16,20):
    ms=cyc_mis(P)
    # gap-3 count = number of gaps of length 3 between consecutive recorded sites
    def n3(m):
        pos=[i for i in range(P) if m>>i&1]; g=[(pos[(k+1)%len(pos)]-pos[k])%P for k in range(len(pos))]
        return sum(1 for x in g if x==3)
    cm=t.cycle_mis(P)
    print(P,len(ms),len(cm), sorted(n3(m) for m in ms)==sorted(n for _,n in cm))
    def S(w):
        ws=[w**n3(m) for m in ms]; Z=sum(ws); return -sum(x/Z*math.log(x/Z) for x in ws)
    # roots of S(w)=P/4 on both sides of w=1
    def root(lo,hi):
        f=lambda w:S(w)-P/4
        for _ in range(200):
            mid=(lo+hi)/2
            if (f(lo)<0)==(f(mid)<0): lo=mid
            else: hi=mid
        return (lo+hi)/2
    print("  S(1)=",round(S(1),4)," S(1)/P=",round(S(1)/P,4)," root<1:",round(root(1e-4,1),4)," root>1:",round(root(1,1e4),4) if S(1e4)<P/4 else "none")
