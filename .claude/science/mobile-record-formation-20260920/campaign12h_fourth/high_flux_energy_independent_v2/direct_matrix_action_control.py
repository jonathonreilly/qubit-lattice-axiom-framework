#!/opt/homebrew/opt/python@3.13/bin/python3.13
"""Second control: actual integer fields and exact square-root amplitudes.
No imports of the PRE symbolic path engine. H4 is applied as a vector using
four actual directed hops, and B adjoints are independently implemented.
"""
from collections import defaultdict
from pathlib import Path
import json
import time
import sympy as sp
HERE=Path(__file__).resolve().parent
AA={0,3,5,6}
EE=tuple((i,j) for i in range(8) for j in range(i+1,8) if (i^j) in {1,2,4})

def add(out,state,c):
    if c==0:return
    out[state]=sp.expand(out.get(state,0)+c)
    if out[state]==0:del out[state]
def weight(e,k,S):
    if S is None:return sp.Integer(1)
    if abs(e+k)>S:return sp.Integer(0)
    return sp.sqrt(1-sp.Rational(e*(e+k),S*(S+1)))
def hops(v,wanted,S):
    out={}
    for (q,E),c in v.items():
        for ix,(i,j) in enumerate(EE):
            for a,b in ((i,j),(j,i)):
                if q[a]==0 or q[b]!=0:continue
                qq=list(q);qq[b]=qq[a];qq[a]=0
                if sum(qq[a]==0 for a in AA)!=wanted:continue
                k=-q[a] if a==i else q[a]
                f=weight(E[ix],k,S)
                if f==0:continue
                ff=list(E);ff[ix]+=k
                add(out,(tuple(qq),tuple(ff)),-c*f)
    return out

def pair(v,edge,sign,S,reverse=False):
    out={};i,j=EE[edge]
    for (q,E),c in v.items():
        if reverse:
            if q[i]!=sign or q[j]!=-sign:continue
            qq=list(q);qq[i]=qq[j]=0;k=-sign
        else:
            if q[i] or q[j]:continue
            qq=list(q);qq[i]=sign;qq[j]=-sign;k=sign
        f=weight(E[edge],k,S)
        if f==0:continue
        ff=list(E);ff[edge]+=k
        add(out,(tuple(qq),tuple(ff)),c*f)
    return out

def plus(*vs):
    out={}
    for v in vs:
        for s,c in v.items():add(out,s,c)
    return out

def times(v,c):return {s:c*a for s,a in v.items() if c*a!=0}
def inner(v,u):return sp.simplify(sum(c*u.get(s,0) for s,c in v.items()))
def D(v):
    out={}
    for (q,E),c in v.items():
        val=0
        for (i,j),e in zip(EE,E):
            a,b=(i,j) if i in AA else (j,i)
            if not q[b]:val+=e*(e+(-q[a] if a==i else q[a]))
        add(out,(q,E),c*val)
    return out

def M(v,S):return hops(hops(v,1,S),0,S)
def H4(v,S):
    zz=hops(hops(hops(hops(v,1,S),2,S),1,S),0,S)
    out=times(zz,-sp.Rational(1,2))
    if S is not None:
        out=plus(out,times(plus(M(D(v),S),D(M(v,S))),-sp.Rational(1,2*S*(S+1))))
    return out

def B(v,edge,charges,S):
    av=hops(v,1,S)
    return times(plus(*(pair(av,edge,c,S) for c in charges)),-1)
def Badj(v,edge,charges,S):
    return times(hops(plus(*(pair(v,edge,c,S,True) for c in charges)),0,S),-1)

def calc(n,S,label):
    q=tuple(int(i in AA) for i in range(8))
    E=tuple(n*{(0,1):1,(1,3):1,(2,3):-1,(0,2):-1}.get(e,0) for e in EE)
    g={(q,E):sp.Integer(1)}
    marks=[(e,(c,)) for e in range(12) for c in (1,-1)] if label=='resolved' else [(e,(1,-1)) for e in range(12)]
    rvec={};gainD=0;gainH=0;rate=0;selected=None
    for e,charges in marks:
        v=B(g,e,charges,S)
        rvec=plus(rvec,Badj(v,e,charges,S))
        rate+=inner(v,v);gainD+=inner(v,D(v));gainH+=inner(v,H4(v,S))
        if EE[e]==(0,1) and charges[0]==1:
            selected={'norm':inner(v,v),'D':inner(v,D(v)),'H4':inner(v,H4(v,S))}
    assert set(rvec)==set(g)
    assert inner(g,rvec)==rate
    dh=sp.simplify(gainH-inner(rvec,H4(g,S)))
    dd=sp.simplify(gainD-inner(rvec,D(g)))
    return {'n':n,'S':S,'instrument':label,'rate':rate,'D_drift':dd,'H4_drift':dh,
            'input_H4':inner(g,H4(g,S)),'loss_action_is_scalar':True,'selected':selected}

def main():
    start=time.time();rows=[]
    expected=json.loads((HERE/'EXACT_RESULTS.json').read_text())
    nvar,cvar=sp.symbols('n C',integer=True)
    for S,n in [(None,0),(None,3),(2,0),(2,1),(3,-2),(3,2)]:
        for label in ('resolved','coherent'):
            row=calc(n,S,label)
            exp=expected['instruments'][label]
            for key in ('rate','D_drift','H4_drift'):
                ex=sp.sympify(exp[('rotor_' if S is None else 'spin_')+key],locals={'n':nvar,'C':cvar})
                ex=ex.subs({nvar:n,cvar:1 if S is None else S*(S+1)})
                assert sp.simplify(row[key]-ex)==0,(row,key,ex)
            skey='coherent' if label=='coherent' else 'resolved_plus'
            selected=expected['selected_mark_01'][skey]
            prefix='rotor_' if S is None else 'spin_'
            for key,name in [('norm','norm_squared'),('D','D_mean'),('H4','H4_mean')]:
                text=selected[prefix+name]
                if key!='norm':text='('+text+')*('+selected[prefix+'norm_squared']+')'
                ex=sp.sympify(text,locals={'n':nvar,'C':cvar}).subs({nvar:n,cvar:1 if S is None else S*(S+1)})
                assert sp.simplify(row['selected'][key]-ex)==0,(row,key,ex)
            print(row,flush=True);rows.append({k:str(v) for k,v in row.items()})
    # Deliberately remove interference before applying Z: the full norm must differ.
    q=tuple(int(i in AA) for i in range(8));E=(0,)*12;g={(q,E):sp.Integer(1)}
    v=B(g,0,(1,),None)
    full=inner(v,H4(v,None))
    dephased=sum(inner({s:a},H4({s:a},None)) for s,a in v.items())
    assert full!=dephased
    mutation={'full_selected_H4_gain':str(full),'dephased_wrong_gain':str(dephased),
              'detected':True}
    print('interference mutation',mutation,flush=True)
    report={'rows':rows,'interference_mutation':mutation,'elapsed_seconds':time.time()-start,
            'note':'Expected symbolic results read only after direct builder written; no author output read.'}
    (HERE/'DIRECT_ACTION_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print('elapsed',report['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
