#!/usr/bin/env python3
"""Summarise screen_*.pkl: for the (word, E) pairs without a band crossing E, tabulate the nodes found at
special points and off-symmetry (point class, speed range, chirality) and list the obstruction pattern.
Usage: summarise_screen.py screen_<tag>.pkl [...]"""
import sys, pickle, collections, numpy as np
def cls(k):
    a=np.round(np.abs(np.asarray(k)),4)   # k in units of pi
    a=np.round(np.mod(a+1,2)-1,4); a=np.abs(a); key=tuple(sorted(a))
    names={(0.5,0.5,0.5):'cube',(0,0,0):'Gamma',(0,0,1):'pi e_i',(0,1,1):'pi(1,1,0)',(1,1,1):'pi(1,1,1)',(0,0,0.5):'(pi/2)e_i',
           (0,0,0.25):'(pi/4)e_i',(0.25,0.25,0.25):'(pi/4)(1,1,1)',(0,0.25,0.25):'(pi/4)(1,1,0)'}
    return names.get(key,'other')
for fn in sys.argv[1:]:
    R=pickle.load(open(fn,'rb')); nf=[r for r in R if not r['fermi']]
    print(f"== {fn}: {len(R)} (word,E) pairs with k* Weyl doublets, {len(nf)} without a band crossing E")
    print("   per skeleton (total, non-Fermi):",{str(sk):(sum(1 for r in R if r['sk']==sk),sum(1 for r in nf if r['sk']==sk)) for sk in sorted(set(r['sk'] for r in R))})
    pat=collections.Counter(); ex={}
    for r in nf:
        vs=r['vstar']; items=set()
        for s in r['special']:
            iso=s[2]-s[1]<1e-5
            items.add((cls(s[0]),'iso' if iso else 'aniso',round(s[1]/vs,3),round(s[2]/vs,3)))
        for z in r['zeros']:
            if isinstance(z[1],str): continue
            items.add(('offsym:'+cls(z[0]),'iso' if z[2]-z[1]<1e-5 else 'aniso',round(z[1]/vs,3),round(z[2]/vs,3)))
        key=(r['sk'],tuple(sorted(items))); pat[key]+=1; ex.setdefault(key,(r['names'],round(r['E'],4),r['chistar'],r['minus']))
    for (sk,items),n in pat.most_common(40):
        print(f"   {n:4d} x {sk}: e.g. {ex[(sk,items)]}")
        for it in items: print("          ",it,"(speeds in units of v*)")
