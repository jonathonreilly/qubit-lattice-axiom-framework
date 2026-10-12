#!/usr/bin/env python3
"""Author exact symbolic spin computation. Imports no prior campaign helper.

Finite words are maps from integer sites to X/Y/Z, with SymPy polynomial
coefficients. Translation bounds are generated from actual support overlaps.
The proof and control formulas were exposed by the supplied unverified lead;
this is different-method author evidence, not an independent review.
"""
from __future__ import annotations
import argparse, json, platform
from pathlib import Path
import sympy as s

J,g,eta,beta=s.symbols('J g eta beta', real=True)
I=s.I
mul={('X','Y'):(I,'Z'),('Y','Z'):(I,'X'),('Z','X'):(I,'Y'),
     ('Y','X'):(-I,'Z'),('Z','Y'):(-I,'X'),('X','Z'):(-I,'Y')}

def word(*pairs): return tuple(sorted(pairs))
def clean(a): return {w:s.expand(c) for w,c in a.items() if s.expand(c)!=0}
def add(*args):
    out={}
    for a in args:
        for w,c in a.items(): out[w]=out.get(w,0)+c
    return clean(out)
def scale(a,c): return clean({w:c*v for w,v in a.items()})
def shift(a,n): return {tuple((x+n,p) for x,p in w):c for w,c in a.items()}
def prod(a,b):
    out={}
    for w,c in a.items():
      for v,d in b.items():
        wv=dict(w); z=c*d
        for x,q in v:
            p=wv.get(x)
            if p is None: wv[x]=q
            elif p==q: del wv[x]
            else:
                z0,r=mul[p,q]; z*=z0; wv[x]=r
        t=tuple(sorted(wv.items())); out[t]=out.get(t,0)+z
    return clean(out)
def comm(a,b): return add(prod(a,b),scale(prod(b,a),-1))
def support(a): return {x for w in a for x,p in w}
def centers(a,b): return sorted({y-x for x in support(a) for y in support(b)})
def deriv(a,b,weighted=False):
    return add(*(scale(comm(shift(a,n),b),I*(n if weighted else 1)) for n in centers(a,b)))
def bracket(a,b,A,wa=False,wb=False):
    return add(deriv(a,deriv(b,A,wb),wa),scale(deriv(b,deriv(a,A,wa),wb),-1))
def orbit_data(a):
    out={}
    for w,c in a.items():
        if not w: continue
        v=min(x for x,p in w); rep=tuple((x-v,p) for x,p in w)
        row=out.setdefault(rep,{'sum':0,'moment':0,'terms':[]})
        row['sum']+=c; row['moment']+=v*c; row['terms'].append((v,c))
    for row in out.values():
        row['sum']=s.expand(row['sum']); row['moment']=s.expand(row['moment'])
    return out
def reduced(a,field): return clean({w:r[field] for w,r in orbit_data(a).items()})
def label(w): return ' '.join(p+str(x) for x,p in w) or '1'
def encoded(a): return {label(w):str(c) for w,c in sorted(a.items())}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True)
    ap.add_argument('--mutation',choices=['none','current_half','moment_sign','drop_improvement'],default='none')
    args=ap.parse_args()
    h={word((0,'X'),(1,'X')):-J, word((0,'Z')):-g/2, word((1,'Z')):-g/2}
    p=add(*(scale(comm(h,shift(h,n)),I*n/(1 if args.mutation=='current_half' else 2)) for n in centers(h,h)))
    prep={word((0,'X'),(1,'Y')):J*g,word((0,'Y'),(1,'X')):-J*g}
    r=deriv(p,h)
    moment=scale(reduced(r,'moment'),1 if args.mutation=='moment_sign' else -1)
    expected_t={word((0,'X'),(1,'X')):2*J*g**2,word((0,'Y'),(1,'Y')):2*J*g**2,
                word((0,'Z')):2*J**2*g,word((0,'X'),(1,'Z'),(2,'X')):-2*J**2*g}
    hp=add(h,{word((0,'Z')):-eta*g,word((1,'Z')):eta*g})
    pp=add(*(scale(comm(hp,shift(hp,n)),I*n/2) for n in centers(hp,hp)))
    if args.mutation=='drop_improvement': pp=p
    improve_current=add(prep,{word((0,'X'),(1,'Y')):2*J*g*eta,word((0,'Y'),(1,'X')):2*J*g*eta})
    rows=[]
    def check(name,value): rows.append({'name':name,'ok':bool(value)})
    check('canonical current orbit equals Jg(XY-YX)',reduced(p,'sum')==prep)
    check('exact conservation all orbit sums zero',reduced(r,'sum')=={})
    check('stress polynomial all generic coefficients',moment==expected_t)
    f={word((0,'X'),(1,'X')):1,word((0,'Y'),(1,'Y')):1}
    u={word((0,'X'),(1,'Z'),(2,'X')):1};z={word((0,'Z')):1}
    bond_action=scale(add(u,scale(shift(u,-1),-1),z,scale(shift(z,1),-1)),2*J**2*g)
    field0=scale(add(shift(f,-1),scale(f,-1)),J*g**2)
    field1=scale(add(f,scale(shift(f,1),-1)),J*g**2)
    expected_r=add(bond_action,field0,field1)
    check('literal current action matches displayed C5',r==expected_r)
    check('displayed bond action in C5 table',deriv(prep,{word((0,'X'),(1,'X')):-J})==bond_action)
    check('displayed first field action in C5 table',deriv(prep,{word((0,'Z')):-g/2})==field0)
    check('displayed second field action in C5 table',deriv(prep,{word((1,'Z')):-g/2})==field1)
    primitive=add(scale(add(shift(f,-1),f),J*g**2),scale(add(scale(shift(u,-1),-1),z),2*J**2*g))
    check('displayed finite-difference primitive',r==add(primitive,scale(shift(primitive,1),-1)))
    check('improved current computed, not inferred unchanged',reduced(pp,'sum')==improve_current)
    defect=deriv(hp,pp)
    check('improved conservation fails for generic nonzero eta',reduced(defect,'sum')!={})
    expected_defect={word((0,'X'),(1,'X')):-8*J*eta*g**2,word((0,'Y'),(1,'Y')):8*J*eta*g**2,
                     word((0,'Z')):8*J**2*eta*g,word((0,'X'),(1,'Z'),(2,'X')):8*J**2*eta*g}
    check('improvement defect all displayed generic coefficients',reduced(defect,'sum')==expected_defect)
    for pauli in 'XYZ':
        A={word((0,pauli)):1}
        check('H-B current on '+pauli,bracket(h,h,A,wb=True)==deriv(p,A))
        check('H-P conservation on '+pauli,bracket(h,p,A)=={})
        check('P-B stress on '+pauli,bracket(p,h,A,wb=True)==deriv(expected_t,A))
        check('moment stress action on '+pauli,deriv(moment,A)==deriv(expected_t,A))
        check('energy improvement unchanged on '+pauli,deriv(hp,A)==deriv(h,A))
    beta_res=add(moment,scale(reduced(h,'sum'),-beta))
    check('YY orbit rejects all beta for Jg nonzero',beta_res.get(word((0,'Y'),(1,'Y')))==2*J*g**2)
    out={'python':platform.python_version(),'sympy':s.__version__,'mutation':args.mutation,
         'h':encoded(h),'p_literal':encoded(p),'p_orbits':encoded(reduced(p,'sum')),'r_literal':encoded(r),
         'r_orbits':{label(w):{'sum':str(x['sum']),'moment':str(x['moment']),
            'terms':[[v,str(c)] for v,c in x['terms']]} for w,x in orbit_data(r).items()},
         'stress':encoded(moment),'stress_minus_beta_h':encoded(beta_res),
         'improved_current':encoded(reduced(pp,'sum')),
         'improved_conservation_defect_orbits':encoded(reduced(defect,'sum')),'checks':rows}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'checks':len(rows),'failed':[r['name'] for r in rows if not r['ok']],
          'stress':encoded(moment),'conservation_defect':encoded(reduced(defect,'sum'))},indent=2))
    raise SystemExit(0 if all(r['ok'] for r in rows) else 1)

if __name__=='__main__': main()
