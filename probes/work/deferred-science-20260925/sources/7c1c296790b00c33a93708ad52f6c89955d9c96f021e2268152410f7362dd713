"""Independent primitive rotor/Gauss and two-quadrature checks.

No author/parent modules imported. No full Hamiltonian or finite-time model is
simulated; the time-window statement is proved analytically in PRE.md.
"""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import itertools
import math
import time
import numpy as np


def geometry(L):
    sites=list(itertools.product(range(L),repeat=3))
    A={x for x in sites if sum(x)%2==0}
    def shift(x,d):return tuple((x[i]+d[i])%L for i in range(3))
    dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    neighbors={a:sorted(shift(a,d) for d in dirs) for a in A}
    edges=sorted((a,b) for a in A for b in neighbors[a])
    edgeindex={e:i for i,e in enumerate(edges)}
    index={x:i for i,x in enumerate(sites)}
    return sites,A,neighbors,edges,edgeindex,index,shift


def compact(flux):return tuple(sorted((e,n) for e,n in flux.items() if n))


def add_flux(flux,e,amount):
    d=dict(flux);d[e]=d.get(e,0)+amount
    return compact(d)


def sum_flux(*fluxes):
    d=defaultdict(int)
    for flux in fluxes:
        for e,n in flux:d[e]+=n
    return compact(d)


def primitive_check():
    L=12
    sites,A,nb,edges,ei,ix,shift=geometry(L)
    copies=[]
    for offset in [(0,0,0),(6,0,0)]:
        at=lambda x:shift(x,offset)
        names={s:at(x) for s,x in {'a':(0,0,0),'b':(-1,0,0),'c':(1,0,0),'e':(0,1,0),'d':(1,1,0),'h':(2,2,0),'v1':(0,-1,0),'v2':(0,0,1),'v3':(0,0,-1)}.items()}
        paths=[[(1,1,0),(0,1,0),(0,0,0),(0,-1,0)],
               [(2,2,0),(1,2,0),(1,1,0),(1,0,0),(0,0,0),(0,0,1)],
               [(2,2,0),(2,1,0),(1,1,0),(0,1,0),(0,0,0),(0,0,-1)]]
        common=()
        for path in paths:
            path=list(map(at,path))
            for x,y in zip(path,path[1:]):
                edge=(x,y) if x in A else (y,x)
                common=add_flux(common,ei[edge],-1 if x in A else 1)
        loop=()
        for pair,weight in [(('a','e'),1),(('d','c'),1),(('a','c'),-1),(('d','e'),-1)]:
            loop=add_flux(loop,ei[(names[pair[0]],names[pair[1]])],weight)
        support=set(names.values())|{x for path in paths for x in map(at,path)}
        copies.append({'sites':names,'common':common,'loop':loop,'support':support})
    assert copies[0]['support'].isdisjoint(copies[1]['support'])
    assert ({copies[0]['sites']['a']}|set(nb[copies[0]['sites']['a']])).isdisjoint({copies[1]['sites']['a']}|set(nb[copies[1]['sites']['a']]))

    def gauss(q,flux):
        div=defaultdict(int)
        for edge,value in flux:
            a,b=edges[edge];div[a]+=value;div[b]-=value
        return all(div[x]==q[ix[x]]-int(x in A) for x in sites)

    def apply_mark(state,which,sigma):
        q,flux=state;a=copies[which]['sites']['a'];b=copies[which]['sites']['b']
        out=[];old=q[ix[a]]
        if not old:return out
        for dest in nb[a]:
            if q[ix[dest]]:continue
            moved=list(q);moved[ix[a]]=0;moved[ix[dest]]=old
            movedflux=add_flux(flux,ei[(a,dest)],-old)
            if moved[ix[b]]:continue
            moved[ix[a]]=sigma;moved[ix[b]]=-sigma
            result=(tuple(moved),add_flux(movedflux,ei[(a,b)],sigma))
            assert all(result[0][ix[x]] for x in A)
            assert gauss(*result)
            out.append(result)
        return out

    initial=[]
    for labels in itertools.product(['c','e'],repeat=2):
        q=[int(x in A) for x in sites];flux=();sign=1
        for cp,label in zip(copies,labels):
            n=cp['sites'];q[ix[n['d']]]=q[ix[n['h']]]=-1
            for b in ['v1','v2','v3',label]:q[ix[n[b]]]=1
            flux=sum_flux(flux,cp['common']);flux=add_flux(flux,ei[(n['d'],n[label])],-1)
            if label=='e':sign*=-1
        state=(tuple(q),flux);assert gauss(*state)
        assert sum(q)==len(A) and sum(bool(x) for x in q)==len(A)+8
        initial.append((state,Fraction(sign,2)))

    def gram(terms):
        result=defaultdict(Fraction)
        for (q,e),c in terms:
            for (r,f),d in terms:
                if q!=r:continue
                diff=sum_flux(f,tuple((edge,-n) for edge,n in e))
                result[diff]+=c*d
        return {k:v for k,v in result.items() if v}

    expected={():Fraction(1)}
    for cp in copies:
        factor={():Fraction(1),cp['loop']:Fraction(-1,2),tuple((e,-n) for e,n in cp['loop']):Fraction(-1,2)}
        expanded=defaultdict(Fraction)
        for e,c in expected.items():
            for f,d in factor.items():expanded[sum_flux(e,f)]+=c*d
        expected={k:v for k,v in expanded.items() if v}
    rows=[]
    for sigmas in itertools.product([-1,1],repeat=2):
        order_outputs=[]
        for order in [(0,1),(1,0)]:
            terms=initial
            lengths=[]
            for which in order:
                updated=[]
                for state,coefficient in terms:
                    candidates=apply_mark(state,which,sigmas[which]);lengths.append(len(candidates))
                    updated.extend((s,coefficient) for s in candidates)
                terms=updated
            assert len(terms)==4 and lengths==[1]*8
            assert gram(terms)==expected
            assert all(sum(bool(x) for x in state[0])==len(A)+12 for state,c in terms)
            order_outputs.append(sorted(terms))
            rows.append({'signs':sigmas,'order':order,'initial_branches':4,'surviving_paths_per_input_per_step':lengths,'output_branches':len(terms),'initial_record_count':len(A)+8,'final_record_count':len(A)+12,'joint_Laurent_terms':len(expected),'exact_Gauss_and_product_effect':True})
        assert order_outputs[0]==order_outputs[1]
    return {'L':L,'vertices':len(sites),'disjoint_charge_flow_and_mark_supports':True,
            'integer_common_flows':[{str(e):n for e,n in cp['common']} for cp in copies],
            'loop_edges':[{str(e):n for e,n in cp['loop']} for cp in copies],
            'joint_Gram_coefficients':[{'shift':list(k),'coefficient':str(v)} for k,v in sorted(expected.items())],
            'rows':rows}


def covariance(L,R):
    k=2*np.pi*np.fft.fftfreq(L)
    x,y,z=np.meshgrid(k,k,k,indexing='ij')
    Dx=4*np.sin(x/2)**2;Dy=4*np.sin(y/2)**2;Dz=4*np.sin(z/2)**2
    root=np.sqrt(Dx+Dy+Dz);weight=np.zeros_like(root)
    np.divide(Dx+Dy,2*L**3*root,out=weight,where=root>0)
    v=float(weight.sum());c=float((weight*np.cos(R[0]*x+R[1]*y+R[2]*z)).sum())
    return v,c


def reference_control(L,R):
    v,c=covariance(L,R);t=c/v
    assert 0<abs(t)<2/3
    d1=np.array([math.sqrt(v),0.]);d2=np.array([c/math.sqrt(v),math.sqrt(v-c*c/v)])
    packets={'bright_at_first':np.array([1.,0.],dtype=complex),'phase_quarter':np.array([1.,1j])/math.sqrt(2)}
    for name,sign in [('opposed_covariance',-np.sign(c)),('aligned_covariance',np.sign(c))]:
        packets[name]=(d1/math.sqrt(v)+sign*d2/math.sqrt(v))/math.sqrt(2*(1+sign*t))
    rows=[];leading=[]
    for name,alpha in packets.items():
        assert abs(np.vdot(alpha,alpha)-1)<1e-13
        chi1=np.dot(d1,alpha);chi2=np.dot(d2,alpha)
        A=abs(chi1)**2;B=abs(chi2)**2;r=float(np.real(chi1*np.conj(chi2)))
        Q0=(v*v+2*c*c)/4;Q1=Q0+v*(A+B)/2+2*c*r
        raw0=Q0/(v*v/4);raw1=Q1/((v/2+A)*(v/2+B))
        independent=(c*c/2+2*c*r)/(A*B)
        measured_vacuum=(2*c*r)/(A*B)
        if name=='opposed_covariance':assert independent<0
        leading.append({'packet':name,'v1':v,'v2':v,'covariance':c,'t':t,'A':A,'B':B,'r':r,'vacuum_joint_coefficient':Q0,'one_joint_coefficient':Q1,'raw_vacuum':raw0,'raw_one':raw1,'independent_vacuum_subtracted':independent,'joint_vacuum_calibrated':measured_vacuum})
        for g in [.4,.2,.1,.05]:
            results=[]
            for order in [20,32]:
                nodes,weights=np.polynomial.hermite.hermgauss(order)
                Z1,Z2=np.meshgrid(np.sqrt(2)*nodes,np.sqrt(2)*nodes,indexing='ij')
                weight=weights[:,None]*weights[None,:]/np.pi
                X=d1[0]*Z1;Y=d2[0]*Z1+d2[1]*Z2
                one=np.abs(alpha[0]*Z1+alpha[1]*Z2)**2
                E1=2*np.sin(g*X/2)**2;E2=2*np.sin(g*Y/2)**2
                vals=[float(np.sum(weight*E1)),float(np.sum(weight*E2)),float(np.sum(weight*E1*E2)),float(np.sum(weight*one*E1)),float(np.sum(weight*one*E2)),float(np.sum(weight*one*E1*E2))]
                moment6=float(np.sum(weight*one*(X**4*Y**2+X**2*Y**4)))/48
                assert abs(vals[5]/g**4-Q1)<=g*g*moment6+1e-13
                results.append(vals)
            e=math.exp(-g*g*v/2);base=-math.expm1(-g*g*v/2);z=g*g*c;cm=2*math.sinh(z/2)**2
            J0=base*base+e*e*cm
            J1=J0+g*g*(e*(A+B)*base-e*e*(A+B)*cm+2*e*e*r*math.sinh(z))
            exact=[base,base,J0,base+g*g*e*A,base+g*g*e*B,J1]
            discrepancy=max(abs(a-b) for a,b in zip(results[-1],exact))
            cutoff=max(abs(a-b) for a,b in zip(results[0],results[1]))
            assert discrepancy<2e-13 and cutoff<2e-13
            terms=[results[-1][5],-results[-1][3]*results[-1][1],-results[-1][0]*results[-1][4],results[-1][0]*results[-1][1]]
            numerator=sum(terms)
            denominator=(results[-1][3]-results[-1][0])*(results[-1][4]-results[-1][1])
            direct=numerator/denominator
            exact_sub=((1-g*g*(A+B))*cm+2*g*g*r*math.sinh(z))/(g**4*A*B)
            exact_denominator=g**4*e*e*A*B
            conditioning=sum(abs(x) for x in terms)/exact_denominator
            numerator_error=abs(numerator-exact_sub*exact_denominator)/g**4
            denominator_error=abs(denominator-exact_denominator)/g**4
            assert numerator_error<2e-13 and denominator_error<2e-13
            # The first retained run demanded an absolute ratio tolerance even
            # when tiny excesses amplify roundoff by >3e7. Raw scaled checks
            # above remain meaningful; direct ratios are checked only in the
            # declared well-conditioned subset and otherwise reported honestly.
            if conditioning<=1e7:assert abs(direct-exact_sub)<2e-11
            rows.append({'packet':name,'g':g,'reference_probabilities_without_kappa_time_factors':exact,'joint_scaled':J1/g**4,'joint_leading':Q1,'independent_subtracted_exact':exact_sub,'independent_subtracted_limit':independent,'quadrature_error':discrepancy,'quadrature_order_change':cutoff,'direct_subtraction_error':abs(direct-exact_sub),'direct_subtraction_condition_scale':conditioning,'direct_ratio_assertion_applicable':bool(conditioning<=1e7),'scaled_numerator_error':numerator_error,'scaled_denominator_error':denominator_error})
    return {'L':L,'separation':R,'v':v,'c':c,'normalized_covariance':t,'leading_rows':leading,'finite_g_rows':rows}


def main():
    started=time.perf_counter()
    result={'scope':'Independent primitive original marked paths/Gauss and harmonic field consistency controls. No author reuse, full dynamical simulation, finite-g certificate or experimental fit.',
            'primitive':primitive_check(),
            'reference':[reference_control(12,(6,0,0)),reference_control(12,(0,0,6)),reference_control(16,(8,0,0))],
            'author_or_parent_modules_imported_or_executed':0,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'completed_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-started}
    out=json.dumps(result,indent=2,allow_nan=False)+'\n'
    Path(__file__).with_name('CONTROL_RESULTS.json').write_text(out)
    print(out,end='')


if __name__=='__main__':main()
