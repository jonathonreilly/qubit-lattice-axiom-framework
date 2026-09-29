#!/usr/bin/env python3
"""Independent radius-one P³ and constraint-mixing coefficient checks."""
import sys
sys.dont_write_bytecode=True
from check import *

def add_poly(rows,fam,p,j,sgn=1):
    for mon,c in reduce_torus(p,'N').items():
        row=rows.setdefault((fam,mon),{})
        row[j]=row.get(j,Q(0))+sgn*c
def moment(rows,fam,k,j,c):
    if c:
        row=rows.setdefault((fam,k),{})
        row[j]=row.get(j,Q(0))+c
def add_kinetic(names,rows):
    gx=g1('X'); tn=t2('N')
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
def add_p3(names,rows):
    cn=c1('N'); ps=[var('p',i,x) for i in range(3) for x in (0,1)]
    for mon in cwr(ps,3):
        j=len(names); names.append('G3p:'+repr(mon))
        add_poly(rows,'GC2_P2',pb(one((var('X'),)+mon),cn),j)
        comps=tuple(a[1] for a in mon)
        moment(rows,'continuum_G3p_0',comps,j,Q(1))
        for i in range(3):
            # Differentiate exactly one momentum factor in its Taylor jet.
            k=(comps[i],)+tuple(comps[n] for n in range(3) if n!=i)
            moment(rows,'continuum_G3p_d',k,j,Q(mon[i][2])-Q(1,2))
def add_mix(names,rows):
    for comp,pp,np,mp in product(range(3),(-1,0,1),(-1,0,1),(-1,0,1)):
        if np>=mp: continue
        j=len(names); names.append('Z1:'+repr((comp,pp,np,mp)))
        terms=[]
        for i in (1,2):
            for hx,w in [(-1,4),(0,-8),(1,4)]:
                tail=(var('h',i,hx),var('p',comp,pp))
                terms.extend([(-w,tail+(var('N',0,np),var('M',0,mp))),
                              (w,tail+(var('M',0,np),var('N',0,mp)))])
        add_poly(rows,'CC2',functional(terms),j)
        moment(rows,'continuum_Z1',(comp,),j,Q(mp-np))
    for comp,pp,xp,np in product(range(3),(0,1),(-1,0,1),(0,1)):
        j=len(names); names.append('W1:'+repr((comp,pp,xp,np)))
        tail=(var('p',comp,pp),var('X',0,xp),var('N',0,np))
        add_poly(rows,'GC2_P2',functional([(-2,(var('p',0),)+tail),
                                         (2,(var('p',0,1),)+tail)]),j)
        for fam,c in [('0',Q(1)),('dp',Q(pp)-Q(1,2)),('dX',Q(xp)),('dN',Q(np)-Q(1,2))]:
            moment(rows,'continuum_W1_'+fam,(comp,),j,c)

def certify(stage,names,rows,rhs):
    rows={k:clean(r) for k,r in rows.items()}
    source=HERE/f'axial_r1_{stage}_system_start.json'
    payload=json.loads(source.read_text()); assert payload['columns']==names
    keys={}; seen=set()
    for r in payload['rows']:
        fam,m=ast.literal_eval(r['key'])
        if fam in ('CC2','GC1','GC2_P2','GG1'):
            m=recenter(m,'X' if fam=='GG1' else 'N')
        k=(fam,m); keys[r['id']]=k; seen.add(k)
        assert rows.get(k,{})=={j:Q(c) for j,c in r['coefficients']},('matrix mismatch',stage,k)
        assert rhs.get(k,0)==Q(r['rhs']),('rhs mismatch',stage,k)
    assert set(rows).issubset(seen)
    witness=json.loads((HERE/f'axial_r1_{stage}_rational_start.json').read_text())
    left=defaultdict(Q); right=Q(0); families=defaultdict(int); terms=[]
    for rid,weight in witness['witness']:
        k=keys[rid]; w=Q(weight); families[k[0]]+=1
        for j,c in rows[k].items(): left[j]+=w*c
        right+=w*rhs.get(k,0)
        terms.append({'source_row':rid,'key':repr(k),'weight':str(w),
                      'independent_coefficients':[[j,str(c)] for j,c in sorted(rows[k].items())],
                      'independent_rhs':str(rhs.get(k,0))})
    assert not clean(left) and right!=0
    out={'stage':stage,'columns':len(names),'payload_rows':len(payload['rows']),
         'witness_rows':len(terms),'witness_families':dict(families),'exact_rhs':str(right),
         'nonzero_combined_left':len(clean(left)),'independent_witness_rows':terms}
    (HERE/(stage+'_independent_certificate.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='independent_witness_rows'}),flush=True)
    print(stage+': every matrix entry/RHS independently reconstructed; exact dual witness verified.',flush=True)

def main():
    budget(); start=time.time(); names,rows,rhs=build(); add_kinetic(names,rows)
    add_p3(names,rows); certify('cubic_momentum',names,rows,rhs); budget()
    add_mix(names,rows); certify('constraint_mixing',names,rows,rhs)
    print('Elapsed seconds:',time.time()-start,flush=True)

if __name__=='__main__': main()
