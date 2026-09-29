#!/usr/bin/env python3
"""Radius-two independent explicit-torus functional differentiation.

No author assembly function is imported. The full system is independently built
before reading the source matrix; the witness is read only after comparison.
"""
import sys
sys.dont_write_bytecode=True
import check as independent
independent.L=13
from check import *
from check_extensions import add_poly, moment

RADIUS=2
VERTS=tuple(range(-RADIUS,RADIUS+1))
ENDS=tuple(range(1-RADIUS,RADIUS+1))
EDGES=VERTS

def base():
    names=[]; rows={}; rhs={}
    def new(n): names.append(n); return len(names)-1
    def put(fam,k,j,c): moment(rows,fam,k,j,Q(c))
    cn,cm=c1('N'),c1('M'); tn,tm=t2('N'),t2('M'); gx,gy=g1('X'),g1('Y')
    hs=[var('h',i,x) for i in range(3) for x in VERTS]
    ps=[var('p',i,x) for i in range(3) for x in VERTS]
    eh=[var('h',i,x) for i in range(3) for x in ENDS]
    ep=[var('p',i,x) for i in range(3) for x in ENDS]
    def record(fam,p,j,sign=1):
        if fam=='GG1':
            for mon,c in reduce_torus(p,'X').items(): put(fam,mon,j,sign*c)
        else: add_poly(rows,fam,p,j,sign)
    for mon in cwr(hs,2):
        j=new('V2:'+repr(mon)); f=one((var('N'),)+mon)
        record('CC2',add((1,pb(f,tm)),(1,pb(tn,change(f,'N','M')))),j)
        record('GC1',pb(gx,f),j)
        put('uniform_V2',canonical_uniform(mon),j,1)
    for x,y in product((0,1),repeat=2):
        mon=canonical_uniform((var('h',1,x),var('h',2,y)))
        k=('uniform_V2',mon)
        rhs[k]=rhs.get(k,Q(0))-2*(2*x-1)*(2*y-1)
    for h in hs:
        for pair in cwr(ps,2):
            mon=(h,)+pair; j=new('T3:'+repr(mon)); f=one((var('N'),)+mon)
            record('CC2',add((1,pb(cn,change(f,'N','M'))),(1,pb(f,cm))),j)
            put('continuum_T3',key((k,i,0) for k,i,x in mon),j,1)
            if j%300==0: budget(); print('T3 columns completed',j-119,flush=True)
    import sympy as s
    e=s.symbols('e'); h=s.symbols('A B C'); p=s.symbols('P Q R')
    g=[1+e*hi for hi in h]
    exact=(sum(g[i]**2*p[i]**2 for i in range(3))-sum(g[i]*p[i] for i in range(3))**2/2)/(4*s.sqrt(s.prod(g)))
    cubic=s.Poly(s.diff(exact,e).subs(e,0).expand(),*(h+p))
    for powers,c in cubic.terms():
        mon=[]
        for i,n in enumerate(powers): mon.extend([var('h' if i<3 else 'p',i%3)]*n)
        rhs['continuum_T3',key(mon)]=Q(str(c))
    for h,p in product(eh,ep):
        j=new('G2:'+repr((h,p))); f=one((var('X'),h,p))
        record('CC2',f0_compose(h,p),j,-1)
        record('GC1',pb(f,cn),j)
        record('GG1',add((1,pb(gx,change(f,'X','Y'))),(1,pb(f,gy))),j)
        ij=(h[1],p[1]); put('continuum_G2_0',ij,j,1)
        put('continuum_G2_dh',ij,j,Q(h[2])-Q(1,2))
        put('continuum_G2_dp',ij,j,Q(p[2])-Q(1,2))
    for i in range(3): rhs['continuum_G2_dh',(i,i)]=Q(-1 if i==0 else 1)
    rhs['continuum_G2_dp',(0,0)]=Q(-2)
    for h in eh:
        for ni,mi in [(n,m) for n in ENDS for m in ENDS if n<m]:
            j=new('F1:'+repr((h,ni,mi))); terms=[]
            for px,pc in [(0,2),(1,-2)]:
                terms.extend([(pc,(var('p',0,px),h,var('N',0,ni),var('M',0,mi))),
                              (-pc,(var('p',0,px),h,var('M',0,ni),var('N',0,mi)))])
            record('CC2',functional(terms),j,-1)
            put('continuum_F1',(h[1],),j,mi-ni)
    rhs['continuum_F1',(0,)]=Q(-1)
    for xp,np in product(range(-RADIUS,RADIUS),VERTS):
        j=new('U0:'+repr((xp,np)))
        terms=[(4*w,(var('X',0,xp),var('N',0,np),var('h',i,x)))
               for i in (1,2) for x,w in [(-1,1),(0,-2),(1,1)]]
        record('GC1',functional(terms),j,-1)
        put('continuum_U0_0',(),j,1); put('continuum_U0_dN',(),j,np)
        put('continuum_U0_dX',(),j,Q(xp)+Q(1,2))
    rhs['continuum_U0_dN',()]=Q(1)
    for xp,yp in [(a,b) for a in EDGES for b in EDGES if a<b]:
        j=new('V0:'+repr((xp,yp))); terms=[]
        for px,pc in [(0,2),(1,-2)]:
            terms.extend([(pc,(var('p',0,px),var('X',0,xp),var('Y',0,yp))),
                          (-pc,(var('p',0,px),var('Y',0,xp),var('X',0,yp)))])
        record('GG1',functional(terms),j,-1); put('continuum_V0',(),j,yp-xp)
    rhs['continuum_V0',()]=Q(1)
    return names,rows,rhs

def nonlinear(names,rows):
    gx=g1('X'); tn=t2('N'); cn=c1('N')
    for j,name in enumerate(names):
        fam,data=name.split(':',1); data=ast.literal_eval(data)
        if fam=='T3': add_poly(rows,'GC2_P2',pb(gx,one((var('N'),)+data)),j)
        if fam=='G2': add_poly(rows,'GC2_P2',pb(one((var('X'),)+data),tn),j)
        if fam=='U0':
            xp,np=data
            terms=[(-(Q(1,8) if i==k else Q(-1,4)),
                    (var('p',i),var('p',k),var('X',0,xp),var('N',0,np)))
                   for i,k in cwr(range(3),2)]
            add_poly(rows,'GC2_P2',functional(terms),j)
        if j%300==0: budget()
    ps=[var('p',i,x) for i in range(3) for x in ENDS]
    for mon in cwr(ps,3):
        j=len(names); names.append('G3p:'+repr(mon))
        add_poly(rows,'GC2_P2',pb(one((var('X'),)+mon),cn),j)
        comps=tuple(a[1] for a in mon)
        moment(rows,'continuum_G3p_0',comps,j,Q(1))
        for i in range(3):
            k=(comps[i],)+tuple(comps[n] for n in range(3) if n!=i)
            moment(rows,'continuum_G3p_d',k,j,Q(mon[i][2])-Q(1,2))
    for comp,pp,np,mp in product(range(3),VERTS,VERTS,VERTS):
        if np>=mp: continue
        j=len(names); names.append('Z1:'+repr((comp,pp,np,mp))); terms=[]
        for i in (1,2):
            for hx,w in [(-1,4),(0,-8),(1,4)]:
                tail=(var('h',i,hx),var('p',comp,pp))
                terms.extend([(-w,tail+(var('N',0,np),var('M',0,mp))),
                              (w,tail+(var('M',0,np),var('N',0,mp)))])
        add_poly(rows,'CC2',functional(terms),j)
        moment(rows,'continuum_Z1',(comp,),j,Q(mp-np))
    for comp,pp,xp,np in product(range(3),ENDS,EDGES,ENDS):
        j=len(names); names.append('W1:'+repr((comp,pp,xp,np)))
        tail=(var('p',comp,pp),var('X',0,xp),var('N',0,np))
        add_poly(rows,'GC2_P2',functional([(-2,(var('p',0),)+tail),(2,(var('p',0,1),)+tail)]),j)
        for fam,c in [('0',Q(1)),('dp',Q(pp)-Q(1,2)),('dX',Q(xp)),('dN',Q(np)-Q(1,2))]:
            moment(rows,'continuum_W1_'+fam,(comp,),j,c)

def certify(names,rows,rhs):
    rows={k:clean(r) for k,r in rows.items()}
    payload=json.loads((HERE/'axial_r2_constraint_mixing_system_radius2_start.json').read_text())
    assert payload['columns']==names
    source_keys={}; seen=set()
    max_diameter=0
    for r in payload['rows']:
        fam,m=ast.literal_eval(r['key'])
        if fam in ('CC2','GC1','GC2_P2','GG1'):
            max_diameter=max(max_diameter,max(a[2] for a in m)-min(a[2] for a in m))
            m=recenter(m,'X' if fam=='GG1' else 'N')
        k=(fam,m); assert k not in seen; seen.add(k); source_keys[r['id']]=k
        assert rows.get(k,{})=={j:Q(c) for j,c in r['coefficients']},('matrix mismatch',k)
        assert rhs.get(k,0)==Q(r['rhs']),('rhs mismatch',k)
    assert set(rows).issubset(seen)
    assert max_diameter<=5
    print('Every radius2 coefficient and RHS matches independently reconstructed system.',flush=True)
    witness=json.loads((HERE/'axial_r2_constraint_mixing_rational_radius2_start.json').read_text())
    left=defaultdict(Q); right=Q(0); families=defaultdict(int); norms=[]; terms=[]
    for rid,weight in witness['witness']:
        k=source_keys[rid]; w=Q(weight); families[k[0]]+=1
        for j,c in rows[k].items(): left[j]+=w*c
        right+=w*rhs.get(k,0)
        if k[0].startswith('continuum_'): norms.append([repr(k),str(w),str(rhs.get(k,0))])
        terms.append({'source_row':rid,'key':repr(k),'weight':str(w),
                      'independent_coefficients':[[j,str(c)] for j,c in sorted(rows[k].items())],
                      'independent_rhs':str(rhs.get(k,0))})
    assert not clean(left) and right!=0
    new_moments=('continuum_G3p','continuum_Z1','continuum_W1')
    assert not any(k.startswith(new_moments) for k in families)
    out={'columns':len(names),'payload_rows':len(payload['rows']),
         'witness_rows':len(terms),'witness_families':dict(families),'normalization_rows':norms,
         'exact_rhs':str(right),'nonzero_combined_left':len(clean(left)),
         'max_residual_integer_diameter':max_diameter,'torus_side':L,
         'independent_witness_rows':terms}
    (HERE/'radius_two_independent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='independent_witness_rows'}),flush=True)

def main():
    budget(); start=time.time(); names,rows,rhs=base(); nonlinear(names,rows)
    print('Independent radius2 assembly complete',len(names),'columns.',flush=True)
    certify(names,rows,rhs)
    print('Elapsed seconds:',time.time()-start,flush=True)

if __name__=='__main__': main()
