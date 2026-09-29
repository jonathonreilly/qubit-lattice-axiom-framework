#!/usr/bin/env python3
"""Independent GC P² extension and complete comparison of radius-one matrix.

This targets G linear in momenta; G3(P³) is excluded by that extra hypothesis.
The author dual witness is only read after independent coefficient assembly.
"""
import sys
sys.dont_write_bytecode=True
from check import *

def main():
    budget(); started=time.time()
    names,rows,rhs=build()
    tn=t2('N'); gx=g1('X')
    for j,name in enumerate(names):
        fam,data=name.split(':',1); data=ast.literal_eval(data)
        if fam=='T3':
            expression=pb(gx,one((var('N'),)+data))
        elif fam=='G2':
            expression=pb(one((var('X'),)+data),tn)
        elif fam=='U0':
            xp,np=data
            terms=[]
            for i,k in cwr(range(3),2):
                c=Q(1,8) if i==k else Q(-1,4)
                terms.append((-c,(var('p',i),var('p',k),var('X',0,xp),var('N',0,np))))
            expression=functional(terms)
        else: continue
        for mon,c in reduce_torus(expression,'N').items():
            row=rows.setdefault(('GC2_P2',mon),{})
            row[j]=row.get(j,Q(0))+c
    rows={k:clean(r) for k,r in rows.items()}
    payload=json.loads((HERE/'axial_r1_mixed_kinetic_system_start.json').read_text())
    assert names==payload['columns']
    author={}; mapped_ids={}
    for r in payload['rows']:
        fam,mon=ast.literal_eval(r['key'])
        if fam in ('CC2','GC1','GC2_P2','GG1'):
            mon=recenter(mon,'X' if fam=='GG1' else 'N')
        k=(fam,mon); mapped_ids[r['id']]=k
        author[k]={j:Q(c) for j,c in r['coefficients']}
        assert rows.get(k,{})==author[k],('matrix mismatch',k)
        assert rhs.get(k,0)==Q(r['rhs']),('rhs mismatch',k)
    assert set(rows).issubset(author)
    print('All independent mixed-kinetic matrix coefficients and RHS match frozen payload.',flush=True)
    witness=json.loads((HERE/'axial_r1_mixed_kinetic_rational_start.json').read_text())
    left=defaultdict(Q); right=Q(0); by_family=defaultdict(lambda:defaultdict(Q))
    for rid,weight in witness['witness']:
        k=mapped_ids[rid]; w=Q(weight)
        print('WITNESS',rid,'weight',w,'key',k)
        print('  '+' + '.join(str(c)+' * '+names[j] for j,c in sorted(rows[k].items()))+' = '+str(rhs.get(k,0)))
        for j,c in rows[k].items(): left[j]+=w*c; by_family[k[0]][j]+=w*c
        right+=w*rhs.get(k,0)
    assert not clean(left) and right==-1
    print('Independent exact dual recombination: all501 unknown coefficients cancel; RHS =',right,flush=True)
    for fam,row in by_family.items():
        print('COMBINED',fam,[(names[j],str(c)) for j,c in clean(row).items()])
    print('Elapsed seconds:',time.time()-started,flush=True)

if __name__=='__main__': main()
