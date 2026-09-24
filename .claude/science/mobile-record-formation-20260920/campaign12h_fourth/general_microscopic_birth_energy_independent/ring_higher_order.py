#!/usr/bin/env python3
"""Fourth-order amplitude reconstruction for the six-cycle's first birth.

Independent paths, then comparison to existing complete physical matrices.
No author code is imported. Formal recurrence is stated in the PRE note.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,sys,traceback
sys.dont_write_bytecode=True
import sympy as s
from path_engine import ring,circulation,apply,add,norm2

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    if not value:raise AssertionError(name)

def coefficients(S=None,n=0,C=None,sign=1):
    g=ring(6)
    if C is None and S is not None:C=s.Integer(S*(S+1))
    x={g.initial(circulation(g,tuple(range(6)),n)):s.Integer(1)}
    F=lambda v:apply(v,lambda state:g.outward(state,C,S))
    G=lambda v:apply(v,lambda state:g.inward(state,C,S))
    J=lambda v:apply(v,lambda state:g.birth(state,0,sign,C,S))
    D=lambda v:{} if C is None else {state:s.simplify(value*g.electric_D(state)/C) for state,value in v.items() if g.electric_D(state)}
    M=lambda v:G(F(v))
    Z=lambda v:F(F(v))
    B=J(F(x));w=norm2(B)
    X31=add((s.Rational(1,2),G(Z(x))),(1,F(D(x))))
    X33=add((s.Rational(1,6),F(Z(x))))
    X42=add((s.Rational(1,2),F(X31)),(s.Rational(1,2),G(X33)),(s.Rational(1,4),Z(D(x))))
    v31=add((1,X31),(-s.Rational(1,2),F(M(x))))
    v42=add((1,X42),(-s.Rational(1,4),Z(M(x))))
    p3=J(v31)
    leakage4=add((1,J(v42)),(-1,F(p3)),(-1,F(D(B))))
    return g,B,leakage4,w

def run(attempt):
    out=HERE/f'RING_HIGHER_RESULTS_{attempt}.json'
    if out.exists():raise FileExistsError(out)
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'running','checks':checks}
    try:
        rows=[]
        for S,n in ((1,0),(2,0),(4,0),(8,0),(2,1),(4,2)):
            g,B,L,w=coefficients(S,n)
            check(f'S={S} n={n} leakage grade one',all(g.grade(z)==1 for z in L))
            check(f'S={S} n={n} Gauss',all(g.gauss(z) for z in L))
            value=s.simplify(norm2(L)/w)
            if n==0:check(f'S={S} zero flux exact next variance coefficient',s.simplify(value-(2-s.Rational(2,S*(S+1))))==0)
            rows.append({'S':S,'n':n,'weight':str(w),'higher_leakage_squared_over_weight':str(value),'support':[{'q':q,'E':E,'amplitude':str(v)} for (q,E),v in sorted(L.items())]})
        result['finite_spin_coefficients']=rows

        # t^2=1-2/C makes every encountered square root polynomial in positive t.
        t=s.Symbol('t',positive=True);C=2/(1-t*t)
        g,B,L,w=coefficients(C=C)
        value=s.simplify(sum(v*v for v in L.values())/sum(v*v for v in B.values()))
        check('symbolic C zero flux higher coefficient',s.simplify(value-(1+t*t))==0)
        check('symbolic Gauss support',all(g.gauss(z) for z in L))
        result['symbolic_zero_flux']={'substitution':'C=2/(1-t^2), 0<=t<1','coefficient':str(value),'equal_to':'2-2/C','support':[{'q':q,'E':E,'amplitude':str(v)} for (q,E),v in sorted(L.items())]}

        # Distinct rotor flux states remain distinct; a single Fourier fiber
        # may combine them coherently and is not this normalizable preparation.
        g,B,L,w=coefficients()
        check('normalizable rotor coefficient is two',norm2(L)/w==2)
        result['normalizable_rotor']={'coefficient':str(norm2(L)/w),'support':[{'q':q,'E':E,'amplitude':str(v)} for (q,E),v in sorted(L.items())]}
        matrix=json.loads((HERE/'MATRIX_RESULTS_01.json').read_text())
        for row in rows:
            matching=[v for v in matrix['complete_physical_ring_rows'] if v['sites']==6 and v['S']==row['S'] and v['flux']==row['n'] and v['epsilon']==.005]
            for m in matching:
                check(f'matrix contrast S={row["S"]} n={row["n"]}',abs(float(s.sympify(row['higher_leakage_squared_over_weight']))-m['high_weight_over_epsilon6'])<.001)
        result['status']='completed'
    except Exception as exc:
        result['status']='failed';result['exception']=repr(exc);result['traceback']=traceback.format_exc();raise
    finally:
        result['summary']={'passed':sum(v['passed'] for v in checks),'failed':sum(not v['passed'] for v in checks)}
        out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'result':str(out),'status':result['status'],**result['summary']}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--attempt',required=True);run(p.parse_args().attempt)
