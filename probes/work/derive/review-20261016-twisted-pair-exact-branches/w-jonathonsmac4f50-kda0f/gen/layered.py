import sys,pickle,time,json
from fractions import Fraction as F
from poly import *
from tracked import red, independent_subset, key
# ----- levels: each level = list of outputs, output = dict {input_index: poly} (cofactor relative to previous level's polys)
def echelon_level(inputs, ext):
    rows=[]
    for i,p in enumerate(inputs):
        rows.append([dict(p),{i:{():F(1)}}])
    if ext:
        vs=sorted({v for p in inputs for mo in p for v in mo})
        for i,p in enumerate(inputs):
            for v in vs:
                xv={(v,):F(1)}
                rows.append([pmul(p,xv),{i:xv}])
    piv={}
    for poly,cof in rows:
        poly=dict(poly); cof=dict(cof)
        while poly:
            lead=max(poly,key=key)
            if lead in piv:
                c=poly[lead]; pp,pc=piv[lead]
                poly=padd(poly,pp,-c)
                for k,v in pc.items():
                    nv=padd(cof.get(k,{}),v,-c)
                    if nv: cof[k]=nv
                    else: cof.pop(k,None)
            else:
                ic=1/poly[lead]; poly=pscale(poly,ic); cof={k:pscale(v,ic) for k,v in cof.items()}
                piv[lead]=(poly,cof); break
    # reduce: keep lowest-degree-lead items last; order by lead
    leads=sorted(piv,key=key)
    outs=[piv[l][0] for l in leads]; cofs=[piv[l][1] for l in leads]
    return outs,cofs
def elim_level(inputs,l):
    ell=inputs[l]
    k=max(mo[0] for mo in ell if len(mo)==1); c=ell[(k,)]
    sigma={mo:-v/c for mo,v in ell.items() if mo!=(k,)}
    outs=[];cofs=[]
    for j,p in enumerate(inputs):
        if j==l: continue
        if any(k in mo for mo in p):
            q,rem=divide_linear(p,k,sigma)
            if not rem: continue
            outs.append(rem); cofs.append({j:{():F(1)},l:pscale(q,-1/c)})
        else:
            outs.append(p); cofs.append({j:{():F(1)}})
    return outs,cofs
def build(m,verbose=True):
    free,sub,r=red[m]
    keep=independent_subset(r)
    gens=[{mo:c for mo,c in r[i]} for i in keep]
    levels=[]   # list of (kind, cofs)
    cur=gens
    def const_idx(polys):
        for i,p in enumerate(polys):
            if degp(p)==0 and p: return i
        return None
    nel=0
    while True:
        outs,cofs=echelon_level(cur,False)
        levels.append(('ech',cofs)); cur=outs
        ci=const_idx(cur)
        if ci is not None: return gens,levels,ci,keep
        if not any(degp(p)==1 for p in cur):
            outs,cofs=echelon_level(cur,True)
            levels.append(('ext',cofs)); cur=outs
            ci=const_idx(cur)
            if ci is not None: return gens,levels,ci,keep
            if not any(degp(p)==1 for p in cur):
                if verbose: print(m,'stuck after ext; vars',len({v for p in cur for mo in p for v in mo}),'polys',len(cur))
                return gens,levels,None,keep
        while True:
            lin=[i for i,p in enumerate(cur) if degp(p)==1]
            if not lin: break
            outs,cofs=elim_level(cur,lin[0]); nel+=1
            levels.append((('elim',lin[0],len(levels)-1),cofs)); cur=outs
            ci=const_idx(cur)
            if ci is not None: return gens,levels,ci,keep
        if verbose: print(m,'elims so far',nel,'polys',len(cur),flush=True)
def prune(levels,final_idx):
    needed=[None]*len(levels)
    need={final_idx}
    for L in range(len(levels)-1,-1,-1):
        kind,cofs=levels[L]
        needed[L]=sorted(need)
        nxt=set()
        for j in need: nxt|=set(cofs[j].keys())
        need=nxt
    return needed,need   # need = needed gens
def replay(gens,levels,needed,final_idx):
    cur=gens
    store={i:gens[i] for i in needed[0] and []}
    # level L needs outputs needed[L], computed from previous level's polys (computed lazily for needed ones only)
    prev={i:p for i,p in enumerate(gens)}
    for L,(kind,cofs) in enumerate(levels):
        new={}
        for j in needed[L]:
            s={}
            for i,q in cofs[j].items(): s=padd(s,pmul(q,prev[i]))
            new[j]=s
        prev=new
    return prev[final_idx]
def size(levels,needed):
    return sum(len(q) for L,(kind,cofs) in enumerate(levels) for j in needed[L] for q in cofs[j].values())
if __name__=='__main__':
    m=eval(sys.argv[1]); name='_'.join(str(x).replace('-','m') for x in m)
    t=time.time()
    gens,levels,ci,keep=build(m)
    print(m,'levels',len(levels),'final idx',ci,round(time.time()-t,1),flush=True)
    if ci is None: sys.exit(1)
    needed,needg=prune(levels,ci)
    # needed[L] lists outputs of level L; need gens = needg
    # replay needs prev for level 0 = gens (all)
    fin=replay(gens,levels,needed,ci)
    print(m,'final poly',fin,'size terms',size(levels,needed),'needed gens',len(needg),'levels kinds',[k for k,_ in levels][:60],flush=True)
    pickle.dump({'m':m,'gens':gens,'levels':levels,'needed':needed,'final':ci,'keep':keep},open('lay_%s.pkl'%name,'wb'))
