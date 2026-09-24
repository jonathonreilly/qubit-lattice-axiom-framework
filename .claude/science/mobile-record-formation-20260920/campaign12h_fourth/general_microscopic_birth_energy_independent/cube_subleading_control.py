#!/usr/bin/env python3
"""Direct fourth-order amplitudes and sixth-order energy numerators.

Physical flux paths stay distinct. Fourier projection is a separate comparison
against independently assembled complete matter matrices, not a preparation.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,sys,traceback
sys.dont_write_bytecode=True
import sympy as s
import numpy as np
from path_engine import cube,apply,add,inner,norm2
import matrix_control as m

HERE=Path(__file__).resolve().parent;checks=[]
def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    if not value:raise AssertionError(name)
def js(x):return str(s.simplify(x))
def project(vector,powers):
    out={}
    for (q,E),v in vector.items():
        out[q]=out.get(q,0)+v*s.I**sum(e*p for e,p in zip(E,powers))
    return {q:s.simplify(v) for q,v in out.items() if s.simplify(v)!=0}
def certificate(vector):
    return [{'q':q,'E':E,'amplitude':str(v)} for (q,E),v in sorted(vector.items())]

def run(attempt):
    out=HERE/f'CUBE_SUBLEADING_RESULTS_{attempt}.json'
    if out.exists():raise FileExistsError(out)
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'running','checks':checks}
    try:
        g=cube();x={g.initial():s.Integer(1)}
        F=lambda v:apply(v,g.outward);G=lambda v:apply(v,g.inward)
        M=lambda v:G(F(v));Z=lambda v:F(F(v))
        V31=add((s.Rational(1,2),G(Z(x))),(-s.Rational(1,2),F(M(x))))
        V33=add((s.Rational(1,6),F(Z(x))))
        V42=add((s.Rational(1,4),F(G(Z(x)))),(s.Rational(1,12),G(F(Z(x)))),(-s.Rational(1,4),Z(M(x))))
        vectors={};physical=[];fibers=[]
        for sign in (-1,1,None):
            J=lambda v:apply(v,lambda st:g.birth(st,0,sign))
            B=J(F(x));Y=add((s.Rational(1,2),J(Z(x))));V0=J(V31);V2=J(V33);Y4=J(V42)
            R=add((1,Y),(-1,F(B)))
            G4=add((1,Y4),(-1,F(V0)))
            U0=add((-1,G(R)));U2=add((2,V2),(-1,F(Y)))
            fast4=add((1,G4),(-1,G(V2)))
            FY=F(Y)
            named={'B':B,'Y':Y,'V0':V0,'V2':V2,'R':R,'G4':G4,'U0':U0,'U2':U2,'fast4':fast4,'FY':FY}
            vectors[str(sign)]={key:certificate(v) for key,v in named.items()}
            def evaluate(v):
                w=norm2(v['B']);ell=norm2(v['R'])/w
                nu=norm2(v['Y'])+2*s.re(inner(v['B'],v['V0']))
                n6=2*s.re(inner(v['R'],v['G4']))+2*norm2(v['V2'])-2*s.re(inner(v['FY'],v['V2']))
                mean0=s.simplify(n6/w-ell*nu/w)
                sec4=s.simplify((norm2(v['U0'])+norm2(v['U2'])+2*s.re(inner(v['R'],v['fast4']))-ell*nu)/w)
                return {'w':w,'ell':ell,'norm_correction':nu,'energy_numerator6':n6,'mean_constant':mean0,'second_epsilon_minus4':sec4,'variance_epsilon_minus4':s.simplify(sec4-ell*ell)}
            values=evaluate(named)
            expected={1:(-18,2,-2),-1:(-13,1,0),None:(-s.Rational(31,2),s.Rational(3,2),-s.Rational(3,4))}[sign]
            check(f'physical sign={sign} exact mean finite part',values['mean_constant']==expected[0])
            check(f'physical sign={sign} exact second/variance finite part',values['second_epsilon_minus4']==expected[1] and values['variance_epsilon_minus4']==expected[2])
            physical.append({'sign':sign,**{k:js(v) for k,v in values.items()}})
            for powers in (tuple([0]*12),tuple(range(12))):
                fv=evaluate({key:project(v,powers) for key,v in named.items()})
                pre=m.matrices(8,4,powers=powers);post=m.matrices(8,6,powers=powers);Jm=m.jump(pre,post,0,sign)
                e=.003
                hin,_,_,vin=m.canonical(pre,e);hout,_,_,vout=m.canonical(post,e)
                phi=Jm@vin[:,0];phi/=np.linalg.norm(phi);hp=hout@phi
                mean=np.vdot(phi,hp).real;second=np.vdot(hp,hp).real
                measured_mean=mean/e**4-float(fv['ell'])/e**2
                measured_second=second/e**4-float(fv['ell'])/e**2
                check(f'fiber sign={sign} p={powers} independent full mean coefficient',abs(measured_mean-float(fv['mean_constant']))<.02)
                check(f'fiber sign={sign} p={powers} independent full second coefficient',abs(measured_second-float(fv['second_epsilon_minus4']))<.02)
                fibers.append({'sign':sign,'phase_powers':powers,**{k:js(v) for k,v in fv.items()},'epsilon':e,'complete_matrix_mean_constant':measured_mean,'complete_matrix_second_coefficient':measured_second})
        result['physical_normalizable_zero_field']=physical
        result['full_matrix_fourier_comparisons']=fibers
        result['physical_path_certificates']=vectors

        C=s.Symbol('C',positive=True);n=s.Symbol('n',integer=True)
        a=1-n*(n+1)/C;b=1-n*(n-1)/C
        ell={1:4*a/(1+a),-1:(a+b)/(1+a),None:(4*a*a+b*(a+b))/((a+b)*(1+a))}
        mu={1:2*n*n/(C*(1+a)),-1:2*n*(n-1)/(C*(1+a)),None:(2*a*n*n+2*b*n*(n-1))/(C*(a+b)*(1+a))}
        c={1:s.Integer(2),-1:s.Integer(1),None:s.Rational(3,2)}
        finite=[]
        for sign in (-1,1,None):
            meanK=s.limit(C*(ell[sign]+mu[sign]-c[sign]),C,s.oo)
            varDK=s.limit(C*(ell[sign]-c[sign]),C,s.oo)
            expectedK={1:-n,-1:n*(n-1)/2,None:(n*n-5*n)/4}[sign]
            expectedDK={1:-n*(n+1),-1:-n*(n-1)/2,None:-3*n*(n+1)/4}[sign]
            check(f'fixed n sign={sign} finite mean K coefficient',s.simplify(meanK-expectedK)==0)
            check(f'fixed n sign={sign} subleading variance deltaK coefficient',s.simplify(varDK-expectedDK)==0)
            finite.append({'sign':sign,'mean_K_constant':js(meanK),'variance_deltaK_epsilon_minus4':js(varDK)})
        result['fixed_field_joint_spin_corrections']=finite
        result['supporting_matrix_checks']=m.checks
        check('all independent matrix support checks passed',all(v['passed'] for v in m.checks))
        result['status']='completed'
    except Exception as exc:
        result['status']='failed';result['exception']=repr(exc);result['traceback']=traceback.format_exc();raise
    finally:
        result['summary']={'passed':sum(v['passed'] for v in checks),'failed':sum(not v['passed'] for v in checks)}
        out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'result':str(out),'status':result['status'],**result['summary']}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--attempt',required=True);run(p.parse_args().attempt)
