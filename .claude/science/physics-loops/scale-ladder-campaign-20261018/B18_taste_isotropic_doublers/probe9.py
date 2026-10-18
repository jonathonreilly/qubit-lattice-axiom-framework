exec(open('b18lib.py').read())
onH=[(f"H{a}{b}",UHf(a,b)) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",ULf(a,b,c)) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH for l in onL]+[(l[0]+"*"+h[0],l[1]@h[1]) for h in onH for l in onL]
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k),"RL.S":lambda k: RL(k)@SK(k)}
rng=np.random.default_rng(7); KR3=rng.uniform(-np.pi,np.pi,(3,3))
def sp(M): return np.sort(np.mod(np.angle(np.linalg.eigvals(M)),2*np.pi))
def quick(a,b):
    ga=np.diff(np.concatenate([a,[a[0]+2*np.pi]])); gb=np.diff(np.concatenate([b,[b[0]+2*np.pi]]))
    return min(min(np.max(np.abs(np.roll(ga,s)-gb)) for s in range(12)), min(np.max(np.abs(np.roll(ga[::-1],s)-gb)) for s in range(12)))
pre={nm:{} for nm in links}
for nm,f in links.items():
    for k0 in KR3:
        for k in (k0,k0+np.pi*EX[0],-k0+np.pi*EX[0]): pre[nm][tuple(np.round(k,12))]=f(k)
surv=[]
for nm in links:
    for un,U in cands:
        for fi,f in enumerate((lambda k: k+np.pi*EX[0], lambda k: -k+np.pi*EX[0])):
            if all(quick(sp(pre[nm][tuple(np.round(k0,12))]@U),sp(pre[nm][tuple(np.round(f(k0),12))]@U))<1e-6 for k0 in KR3):
                surv.append((nm,un,fi)); break
print(len(surv),"survivors; links:",{nm:sum(1 for s in surv if s[0]==nm) for nm in links})
import collections
mult=collections.Counter()
weyl=[]
for nm,un,fi in surv:
    U=dict(cands)[un]; W0=links[nm](kst)@U
    lv=levels(lambda k: W0,kst); mult[tuple(sorted(m for _,m in lv))]+=1
    if any(m==2 for _,m in lv): weyl.append((nm,un))
print("k* multiplicity patterns among survivors:",dict(mult))
print("survivors with any 2-fold level at k*:",weyl[:10],len(weyl))
