#!/usr/bin/env python3
"""Exact finite paths for the independent PRE; no other campaign imports."""
from pathlib import Path
import argparse, datetime, hashlib, json, sys, traceback
sys.dont_write_bytecode=True
import sympy as s
from path_engine import Graph, cube, ring, circulation, apply, add, inner, norm2, birth_coefficients

HERE=Path(__file__).resolve().parent
checks=[]

def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    if not value: raise AssertionError(name)

def eq(a,b): return s.simplify(a-b)==0
def clean(v): return {k:s.simplify(x) for k,x in v.items() if s.simplify(x)!=0}
def js(v): return str(s.simplify(v))


def h4_cube(graph,vector):
    F=lambda v:apply(v,graph.outward)
    G=lambda v:apply(v,graph.inward)
    return add((-s.Rational(1,2),G(G(F(F(vector))))))


def run(attempt):
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'running','checks':checks}
    out=HERE/f'PATH_RESULTS_{attempt}.json'
    if out.exists(): raise FileExistsError(out)
    try:
        graph=cube(); edge=graph.edge_index[(0,1)]
        rotor=[]
        for n in (-3,0,2):
            state=graph.initial(circulation(graph,(0,1,3,2),n))
            check(f'cube n={n} initial Gauss',graph.gauss(state))
            totals={kind:[0,0,0,0] for kind in ('resolved','coherent')}
            for kind in totals:
                signs=(-1,1) if kind=='resolved' else (None,)
                for e in range(len(graph.edges)):
                    for sign in signs:
                        B,R,center=birth_coefficients(graph,state,e,sign)
                        check(f'rotor cube {n} {kind} {e} {sign} local cancellation',not add((1,R),(1,center)))
                        check(f'rotor cube {n} {kind} {e} {sign} Gauss',all(graph.gauss(x) for x in set(B)|set(R)))
                        w,rr=norm2(B),norm2(R)
                        D1=sum(v*v*graph.electric_D(x) for x,v in B.items())
                        D2=sum(v*v*graph.electric_D(x)**2 for x,v in B.items())
                        totals[kind]=[s.simplify(a+b) for a,b in zip(totals[kind],(w,rr,D1,D2))]
                        if e==edge:
                            expected={1:2,-1:1,None:s.Rational(3,2)}[sign]
                            check(f'rotor cube {n} {sign} local leakage coefficient',eq(rr/w,expected))
                            rotor.append({'n':n,'kind':kind,'sign':sign,'weight':js(w),'leakage':js(rr/w),'D_mean':js(D1/w),'D_variance':js(D2/w-(D1/w)**2)})
            check(f'rotor cube n={n} resolved/coherent sums',totals['resolved']==totals['coherent'])
            check(f'rotor cube n={n} allmark rate/leakage/electric',totals['resolved'][:3]==[48,72,96*n*n])
        result['rotor_selected_rows']=rotor

        # Finite-spin tests use exact radicals, including negative circulation.
        finite=[]
        for S,n in ((1,0),(3,-1),(3,1),(9,-4),(9,4),(17,8)):
            C=s.Integer(S*(S+1)); a=1-s.Integer(n*(n+1))/C; b=1-s.Integer(n*(n-1))/C
            state=graph.initial(circulation(graph,(0,1,3,2),n))
            for sign in (-1,1,None):
                B,R,center=birth_coefficients(graph,state,edge,sign,C,S)
                check(f'finite S={S} n={n} sign={sign} local cancellation',not add((1,R),(1,center)))
                w,rr=norm2(B),norm2(R)
                wanted_w={1:a*(1+a),-1:b*(1+a),None:(a+b)*(1+a)}[sign]
                wanted_rr={1:4*a*a,-1:b*(a+b),None:4*a*a+b*(a+b)}[sign]
                check(f'finite S={S} n={n} sign={sign} norm formula',eq(w,wanted_w))
                check(f'finite S={S} n={n} sign={sign} leakage formula',eq(rr,wanted_rr))
                values=sorted([(graph.electric_D(x),s.simplify(v*v)) for x,v in B.items()],key=lambda x:(x[0],str(x[1])))
                D1=s.simplify(sum(D*weight for D,weight in values)/w)
                D2=s.simplify(sum(D*D*weight for D,weight in values)/w)
                dplus=2*n*n; dminus=2*n*(n-1)
                expectedD={1:dplus/(1+a),-1:dminus/(1+a),None:(a*dplus+b*dminus)/((a+b)*(1+a))}[sign]
                check(f'finite S={S} n={n} sign={sign} electric mean',eq(D1,expectedD))
                finite.append({'S':S,'n':n,'sign':sign,'weight':js(w),'leakage':js(rr/w),'slow_D_mean':js(D1),'slow_D_variance':js(D2-D1*D1)})
        result['finite_spin_rows']=finite

        # Boundary suppression is a domain test, not a conditional-limit row.
        state=graph.initial(circulation(graph,(0,1,3,2),3))
        B,R,_=birth_coefficients(graph,state,edge,1,s.Integer(12),3)
        check('upper boundary selected plus leading output is zero',not B and not R)

        # Frozen macroscopic-flux amplitudes are reconstructed from the same
        # exact local spin formula after n/S -> alpha and u=1-alpha^2.
        u=s.Symbol('u',positive=True); n=s.Symbol('n',integer=True)
        class Frozen(Graph):
            def spin_weight(self,electric,shift,C=None,S=None):
                coefficient=s.expand(electric).coeff(n)
                return s.sqrt(u) if coefficient else s.Integer(1)
        frozen=Frozen(graph.n,graph.A,graph.edges)
        state=frozen.initial(circulation(frozen,(0,1,3,2),n))
        allrows={}
        for kind in ('resolved','coherent'):
            total_w=total_r=total_delta_change=0
            signs=(-1,1) if kind=='resolved' else (None,)
            for e in range(len(frozen.edges)):
                for sign in signs:
                    B,R,center=birth_coefficients(frozen,state,e,sign)
                    check(f'frozen {kind} e={e} sign={sign} local cancellation',not add((1,R),(1,center)))
                    w,rr=norm2(B),norm2(R)
                    Dlead=sum(v*v*s.expand(frozen.electric_D(x)).coeff(n,2)*(1-u) for x,v in B.items())
                    total_w+=w;total_r+=rr;total_delta_change+=Dlead-4*(1-u)*w
                    if e==edge:
                        mu=s.simplify(Dlead/w);ell=s.simplify(rr/w)
                        expected_l={1:4*u/(1+u),-1:2*u/(1+u),None:3*u/(1+u)}[sign]
                        check(f'frozen selected {sign} leakage',eq(ell,expected_l))
                        check(f'frozen selected {sign} slow mean',eq(mu,2*(1-u)/(1+u)))
                        allrows[str(sign)]={'weight':js(w),'leakage':js(ell),'slow_mean_scaled':js(mu),'full_mean_scaled':js(mu+ell),'mean_change_scaled':js(mu+ell-4*(1-u))}
            check(f'frozen {kind} total weight',eq(total_w,8*(u*u+2*u+3)))
            check(f'frozen {kind} total leakage',eq(total_r,36*(1+u*u)))
            check(f'frozen {kind} slow energy change',eq(total_delta_change,-32*(1-u**3)))
            check(f'frozen {kind} microscopic energy derivative',eq(total_r+total_delta_change,4+36*u*u+32*u**3))
        result['macroscopic_flux']={'u':'1-alpha^2, |alpha|<1','selected':allrows,'total_rate_over_kappa':js(total_w),'total_fast_variance_coefficient':js(total_r),'energy_derivative_coefficient':js(total_r+total_delta_change)}

        # Direct four-hop paths give the bounded slow-band rotor coefficient.
        slow=[]
        for n in (0,2):
            state=graph.initial(circulation(graph,(0,1,3,2),n)); x={state:s.Integer(1)}
            h4x=h4_cube(graph,x)
            input_mean=inner(x,h4x);input_var=norm2(h4x)-input_mean**2
            for sign in (-1,1,None):
                B,_,_=birth_coefficients(graph,state,edge,sign);w=norm2(B)
                h4B=h4_cube(graph,B);H4mean=inner(B,h4B)/w
                H4var=norm2(h4B)/w-H4mean**2
                DB={k:v*graph.electric_D(k) for k,v in B.items()}
                Dmean=inner(B,DB)/w; Dvar=norm2(DB)/w-Dmean**2
                cov=s.simplify(inner(DB,h4B)/w-Dmean*H4mean)
                slow.append({'n':n,'sign':sign,'initial_H4_mean':js(input_mean),'initial_H4_variance':js(input_var),'post_H4_mean':js(H4mean),'post_H4_variance':js(H4var),'post_D_mean':js(Dmean),'post_D_variance':js(Dvar),'symmetrized_D_H4_covariance':js(cov)})
        result['fixed_field_slow_band_rows']=slow

        # Degree-two cancellation, including a nonterminal six-cycle.
        rings=[]
        for size in (4,6,8):
            g=ring(size)
            for n in (0,1):
                state=g.initial(circulation(g,tuple(range(size)),n))
                for sign in (-1,1,None):
                    B,R,center=birth_coefficients(g,state,0,sign)
                    check(f'ring {size} n={n} sign={sign} leading fast leakage vanishes',not R and not center)
                    rings.append({'sites':size,'n':n,'sign':sign,'weight':js(norm2(B)),'leakage':js(norm2(R)),'output_grades':sorted(set(g.grade(x) for x in B))})
        result['degree_two_controls']=rings
        result['status']='completed'
    except Exception as exc:
        result['status']='failed';result['exception']=repr(exc);result['traceback']=traceback.format_exc();raise
    finally:
        result['summary']={'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)}
        out.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'result':str(out),'status':result['status'],**result['summary']}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--attempt',required=True)
    run(parser.parse_args().attempt)
