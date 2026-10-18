#!/usr/bin/env python3
"""B20 part 2 screen: parameter-free words in S^{+-1}, S^{+-2}, R_L and Clifford (or pi/6) phase on-site
factors of H_on and Lambda.  For every 2-fold level E at k* with a linear Weyl splitting, test whether E is
reached ONLY at isolated linear Weyl nodes that are isotropic with the k* speed.
Stage A: levels and degenerate-perturbation velocity matrix at k*.
Stage B: determinant sign test on a 16^3 grid (a sign change proves a band crossing E); for the survivors, dist(spec W, E)
         on the grid plus special points and Nelder-Mead from the lowest grid points; any zero whose nearest two eigenphases are not degenerate is a single-band crossing (a Fermi surface
         at E), which rejects the (word, E) pair.  Remaining zeros are classified with velocity matrices.
Output: screen_<tag>.pkl and a log; prints PASS/FAIL and TOTAL (the checks are bookkeeping and sanity
checks; the scientific output is the candidate table).
Usage: screen_words.py <tag> [nproc]"""
import sys, time, pickle
ARGV=list(sys.argv)
exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
from multiprocessing import Pool
TAG=ARGV[1] if len(ARGV)>1 else 'cliff1'; NP=int(ARGV[2]) if len(ARGV)>2 else 4
OUT='/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/'
# on-site palettes (labels -> matrices); global phase of each factor fixed (first projector phase 1)
def pal_cliff():
    P={}
    for a,b in itertools.product(range(4),repeat=2): P[f"H{a}{b}"]=onH(a,b)
    for a,b,c in itertools.product(range(4),repeat=3): P[f"L{a}{b}{c}"]=onL(a,b,c)
    return P
def pal_pi6():
    P={}
    for a,b in itertools.product(range(12),repeat=2): P[f"H{a}.{b}"]=onH(a,b,unit=1)
    for a,b,c in itertools.product(range(12),repeat=3): P[f"L{a}.{b}.{c}"]=onL(a,b,c,unit=1)
    return P
PC=pal_cliff()
PHL={**PC,**{f"{h}*{l}":PC[h]@PC[l] for h in PC if h[0]=='H' for l in PC if l[0]=='L'}}
SKEL1=[('S','o'),('S','R','o'),('S','o','R'),('S2','o'),('S','S','R','o'),('S','R','S','o'),('S','R','Si','o'),('S','R','S','R','o')]
SKEL2=[('S','o','S','o'),('S','o','Si','o'),('S','o','R','o'),('S','R','o','R','o'),('S2','o','S2','o'),('S2','o','S2i','o'),
       ('S','R','o','S','R','o'),('S','R','o','Si','R','o'),('S','o','S','R','o'),('S','o','Si','R','o'),('S','R','o','S','o')]
def jobs(tag):
    if tag=='cliff1':
        for sk in SKEL1:
            for n in PHL: yield sk,(n,)
    elif tag.startswith('cliff2'):
        sel=SKEL2 if tag=='cliff2' else [SKEL2[int(i)] for i in tag.split(':')[1].split(',')]
        for sk in sel:
            for n1 in PC:
                for n2 in PC: yield sk,(n1,n2)
    elif tag=='pi6':
        for sk in [('S','o'),('S','R','o'),('S','o','R'),('S2','o')]:
            for n in pal_pi6(): yield sk,(n,)
    elif tag=='test':
        yield ('S2','o','S2','o'),('H20','L202')
        yield ('S','R','o','o'),('H23','L110')
PALL=None
def mat(n):
    global PALL
    if n in PHL: return PHL[n]
    if PALL is None: PALL=pal_pi6()
    return PALL[n]
def build(sk,names):
    it=iter(names); return [mat(next(it)) if L=='o' else L for L in sk]
g=np.linspace(-np.pi,np.pi,16,endpoint=False)+0.0731
GRID=np.array(list(itertools.product(g,repeat=3)))
SPEC=np.array([np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]+[np.zeros(3)]+[np.pi*e for e in EX]+[np.pi/2*e for e in EX]
               +[np.pi/4*e for e in EX]+[np.pi/4*np.array(v) for v in ((1,1,1),(1,-1,0),(1,1,0),(1,-1,1))]+[np.pi*np.array(v) for v in ((1,1,0),(1,1,1))])
def pdist(a,b): return np.linalg.norm(wrap(a-b))
def analyse(args):
    sk,names=args; w=build(sk,names); out=[]
    try:
        lv=node_levels(w,kst)
    except Exception as e:
        return []
    for E,m in lv:
        if m!=2: continue
        v=vel_matrix(w,kst,E)
        if v['sv'].min()<1e-3: continue
        rec=dict(sk=sk,names=names,E=float(E),vstar=float(v['sv'].mean()),chistar=v['chi'],anisostar=float(v['aniso']))
        vm=vel_matrix(w,-kst,E) if any(abs(wrap(e-E))<1e-7 and mm==2 for e,mm in node_levels(w,-kst)) else None
        rec['minus']=None if vm is None else (float(vm['sv'].min()),float(vm['sv'].max()),vm['chi'])
        # determinant sign test: r(k) = det(W - e^{iE}) / (e^{6iE} sqrt(det W)) is real and continuous (det W is
        # k-independent for these letters); a simple zero surface (a band crossing E) changes its sign, an isolated
        # Weyl node (double zero) does not.  A sign change on the grid proves a Fermi surface at E.
        Ws=Wbatch(w,GRID); c0=np.linalg.det(Ws[0]); r=(np.linalg.det(Ws-np.exp(1j*E)*np.eye(12))/(np.exp(6j*E)*np.sqrt(c0)))
        rec['rimag']=float(np.abs(r.imag).max()/max(np.abs(r).max(),1e-300))
        rr=r.real; fermi=bool(rr.max()>0 and rr.min()<0)
        rec['fermi']=fermi
        if fermi:
            rec['special']=[]; rec['zeros']=[]; rec['gridmin_far']=0.0; out.append(rec); continue
        d=np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Ws))-E)),axis=-1); ds=dist_to_E(w,SPEC,E)
        far=np.array([min(pdist(k,kst),pdist(k,-kst))>0.3 for k in GRID])
        rec['gridmin_far']=float(d[far].min())
        sp=[]
        for k,dd in zip(SPEC,ds):
            if dd<1e-7 and min(pdist(k,kst),pdist(k,-kst))>1e-6:
                vv=vel_matrix(w,k,E); sp.append((k/np.pi,float(vv['sv'].min()),float(vv['sv'].max()),vv['chi'],float(vv['spread']),float(vv['next'])))
        rec['special']=sp
        f=lambda k: float(dist_to_E(w,np.asarray(k)[None],E)[0])
        idx=np.argsort(np.where(far,d,9))[:6]; zeros=[]
        for i in idx:
            r_=minimize(f,GRID[i],method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-13,'maxiter':1500})
            if r_.fun<1e-6:
                vv=vel_matrix(w,r_.x,E)
                if vv['spread']>1e-4: fermi=True; zeros.append((r_.x/np.pi,'band',float(vv['spread']))); break
                zeros.append((r_.x/np.pi,float(vv['sv'].min()),float(vv['sv'].max()),vv['chi']))
            else: zeros.append((r_.x/np.pi,'min',float(r_.fun)))
        rec['zeros']=zeros; rec['fermi']=fermi
        out.append(rec)
    return out
if __name__=='__main__':
    t0=time.time(); PASS=FAIL=0
    def check(name,ok,detail=""):
        global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
    J=list(jobs(TAG)); print(f"{TAG}: {len(J)} words",flush=True)
    with Pool(NP) as p: res=p.map(analyse,J,chunksize=16)
    recs=[r for rr in res for r in rr]
    pickle.dump(recs,open(OUT+f"screen_{TAG.replace(':','_').replace(',','-')}.pkl",'wb'))
    nf=[r for r in recs if not r['fermi']]
    print(f"{len(recs)} (word, E) pairs with a linear spin-1/2 Weyl doublet at k*; {len(nf)} without a band crossing E (determinant sign test on 16^3, then Nelder-Mead)  [{time.time()-t0:.0f}s]")
    check("every k* Weyl doublet is isotropic (O-forced) to 1e-6",all(r['anisostar']<1e-6 for r in recs),f"max {max([r['anisostar'] for r in recs],default=0):.1e}")
    import collections
    print("k* speeds (per unit sqrt2/3):",dict(collections.Counter(round(r['vstar']/(np.sqrt(2)/3),4) for r in recs)))
    def iso_ok(r):
        vs=r['vstar']
        zs=[z for z in r['zeros'] if not isinstance(z[1],str)]
        ok=all(abs(z[1]-vs)<1e-5 and abs(z[2]-vs)<1e-5 for z in zs) and all(abs(s[1]-vs)<1e-5 and abs(s[2]-vs)<1e-5 for s in r['special'])
        return ok
    good=[r for r in nf if iso_ok(r)]
    good.sort(key=lambda r: -r['gridmin_far'])
    print(f"{len(good)} pairs: no Fermi-surface crossing found and every found node isotropic at the k* speed (screen level only)")
    for r in good[:25]:
        print("  ",r['sk'],r['names'],"E=%+.4f v*=%.5f chi*=%+d -k*:%s gridmin_far=%.4f special=%d zeros=%s"%(r['E'],r['vstar'],r['chistar'],r['minus'],r['gridmin_far'],len(r['special']),
              [(np.round(z[0],3).tolist(),)+tuple(np.round(z[1:],4) if not isinstance(z[1],str) else z[1:]) for z in r['zeros']]))
    # obstruction pattern: what blocks the non-Fermi pairs
    pat=collections.Counter()
    for r in nf:
        if r in good: continue
        vs=r['vstar']; why=[]
        for s in r['special']:
            why.append('special-aniso' if s[2]-s[1]>1e-5 else ('special-iso-otherspeed' if abs(s[1]-vs)>1e-5 else 'special-iso'))
        for z in r['zeros']:
            if not isinstance(z[1],str): why.append('offsym-aniso' if z[2]-z[1]>1e-5 else ('offsym-iso-otherspeed' if abs(z[1]-vs)>1e-5 else 'offsym-iso'))
        pat[tuple(sorted(set(why)))]+=1
    print("obstruction pattern among non-Fermi pairs:",dict(pat))
    check("the determinant test function r(k) is real on every grid (det W is k-independent)",all(r['rimag']<1e-8 for r in recs),f"max relative imag {max([r['rimag'] for r in recs],default=0):.1e}")
    check("bookkeeping: every record has a k* doublet with nonzero speed",all(r['vstar']>1e-3 for r in recs))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
