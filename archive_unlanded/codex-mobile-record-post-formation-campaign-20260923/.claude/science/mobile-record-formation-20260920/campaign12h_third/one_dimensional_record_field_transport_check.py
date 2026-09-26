#!/usr/bin/env python3
"""Exact 1D physical sectors and a declared second-order transport diagnostic.

The quantum-walk scaling calculation is exact for its specified reduced
one-birth kernel. It is NOT a proof of that limit for the full microscopic
large-volume Lindblad model. The latter interchange remains an obligation.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
import scipy.linalg as la
from scipy.integrate import quad
from scipy.special import jv
import sympy as sp

OUT=Path(__file__).resolve().parent


def matter(word,length):
    bits=[(word>>e)&1 for e in range(length)]
    return tuple(bits[x]-bits[(x-1)%length]+int(x%2==0) for x in range(length))


def sector(length,minus_sites):
    words=[];charges=[]
    for word in range(1<<length):
        q=matter(word,length)
        if not all(v in (0,1,-1) for v in q):continue
        if {x for x,v in enumerate(q) if v==-1}!=set(minus_sites):continue
        words.append(word);charges.append(q)
    ix={w:i for i,w in enumerate(words)};dim=len(words)
    hop=np.zeros((dim,dim),dtype=np.int64)
    for i,(word,q) in enumerate(zip(words,charges)):
        for e in range(length):
            x,y=e,(e+1)%length
            if (q[x]==1 and q[y]==0 and ((word>>e)&1)==1) or (q[x]==0 and q[y]==1 and ((word>>e)&1)==0):
                target=word^(1<<e);assert target in ix
                hop[ix[target],i]=-1
    assert np.array_equal(hop,hop.T)
    penalty=np.array([sum(q[x]!=0 for x in range(1,length,2)) for q in charges],dtype=np.int64)
    return words,charges,hop,penalty


def exact_sectors():
    rows=[]
    for length in (6,8,10,12,14):
        m=length//2;anchor=1
        words,charges,hop,pen=sector(length,{anchor})
        low=[i for i,v in enumerate(pen) if v==2]
        # Order by the clockwise separation in B-site spacings from the minus.
        def pos(i):
            q=charges[i];plus=[x for x in range(1,length,2) if q[x]==1]
            assert len(plus)==1
            return ((plus[0]-anchor)%length)//2
        low.sort(key=pos)
        assert [pos(i) for i in low]==list(range(1,m))
        high=[i for i,v in enumerate(pen) if v>2]
        b=hop[np.ix_(low,high)]
        touched=np.any(b!=0,axis=0)
        assert np.all(pen[np.array(high)[touched]]==3)
        second=-(b@b.T)
        want=-(m-2)*np.eye(m-1,dtype=np.int64)
        for x in range(m-2):want[x,x+1]=want[x+1,x]=-1
        assert np.array_equal(second,want)
        assert np.all(hop[np.ix_(low,low)]==0)
        assert all(length-int(words[i]).bit_count()==2*pos(i) for i in low)
        spectra=[]
        if length<=10:
            for eps in (.02,.04,.08):
                exact=la.eigvalsh(np.diag(pen-2).astype(float)+eps*hop)[:m-1]
                proposed=eps**2*la.eigvalsh(second.astype(float))
                error=float(np.max(abs(exact-proposed)))
                assert error<30*m*eps**4
                spectra.append({'epsilon':eps,'max_energy_error_over_Delta':error,
                                'error_over_epsilon4':error/eps**4})
        # The leading dressed-vacuum birth amplitude is computed as -J_e T P,
        # with the first-excursion denominator exactly Delta, separately from
        # the low-sector hopping matrix above.
        vacuum=(1<<length)-1
        qvac=matter(vacuum,length);assert qvac==tuple(int(x%2==0) for x in range(length))
        e_birth=anchor;born={}
        for e_hop in range(0,length,2):
            inter=vacuum^(1<<e_hop);qi=matter(inter,length)
            x,y=e_birth,(e_birth+1)%length
            if qi[x]==qi[y]==0:
                # At this odd edge the tail is B; spin-half lowering creates
                # a minus at B and a plus at A, preserving all prior records.
                assert (inter>>e_birth)&1
                target=inter^(1<<e_birth);assert target in words
                born[target]=born.get(target,0)+1
        assert born=={words[low[0]]:1}
        rows.append({'length':length,'fixed_minus_site':anchor,'complete_sector_dimension':len(words),
                     'low_dimension':len(low),'low_words_hex':[hex(words[i]) for i in low],
                     'second_order_matrix_over_t2_over_Delta':second.tolist(),
                     'exact_first_birth_seed_word_hex':hex(words[low[0]]),
                     'first_birth_amplitude_over_t_over_Delta':1,
                     'flux_deficit_of_position_n': '2n links',
                     'finite_spectral_controls':spectra,
                     'basis_sha256':hashlib.sha256(json.dumps(words).encode()).hexdigest()})
    return rows


def pxp_and_immobility():
    rows=[]
    for length in (6,8,10,12):
        words,charges,hop,pen=sector(length,set());m=length//2
        mask=sum(1<<e for e in range(1,length,2))
        etas=[w^mask for w in words]
        allowed=[w for w in range(1<<length) if all(not ((w>>e)&1 and (w>>((e+1)%length))&1) for e in range(length))]
        assert set(etas)==set(allowed)
        assert all(int(pen[i])==m-etas[i].bit_count() for i in range(len(words)))
        ix={w:i for i,w in enumerate(etas)};pxp=np.zeros_like(hop)
        for i,w in enumerate(etas):
            for e in range(length):
                if ((w>>((e-1)%length))&1)==((w>>((e+1)%length))&1)==0:
                    pxp[ix[w^(1<<e)],i]=-1
        assert np.array_equal(hop,pxp)
        physical=[w for w in range(1<<length) if all(v in (0,1,-1) for v in matter(w,length))]
        assert len(physical)==3**m
        hops=0;births=0
        for w in physical:
            q=matter(w,length)
            assert all(q[x]!=-1 for x in range(0,length,2))
            minus={x for x,v in enumerate(q) if v==-1}
            for e in range(length):
                x,y=e,(e+1)%length;bit=(w>>e)&1
                if (q[x]==1 and q[y]==0 and bit==1) or (q[x]==0 and q[y]==1 and bit==0):
                    qnew=matter(w^(1<<e),length)
                    assert {a for a,v in enumerate(qnew) if v==-1}==minus
                    hops+=1
                if q[x]==q[y]==0:
                    # Exactly the gauge-allowed pair is created by flipping e.
                    qnew=matter(w^(1<<e),length)
                    assert all(v in (0,1,-1) for v in qnew)
                    assert qnew[x]==-qnew[y] and qnew[x]!=0
                    assert all(qnew[a]==q[a] for a in range(length) if a not in (x,y))
                    assert {a for a,v in enumerate(qnew) if v==-1}>minus
                    births+=1
        rows.append({'length':length,'no_minus_dimension':len(words),'complete_live_dimension':len(physical),
                     'exact_PXP_equivalence':True,'all_A_minus_forbidden':True,
                     'all_hops_preserve_each_B_minus_location':True,
                     'directed_hops_checked':hops,'birth_maps_checked':births})
    return rows


def half_line_prob(theta,extra=55):
    if theta==0:return np.array([1.])
    n=np.arange(1,int(math.ceil(2*theta+extra*(1+theta)**(1/3)))+1,dtype=float)
    amp=(n/theta)*jv(n,2*theta)
    return amp*amp


def mean_halfline(theta):
    prob=half_line_prob(theta)
    return float(np.dot(np.arange(1,len(prob)+1),prob))


def halfline_controls():
    rows=[]
    for theta in (.1,1.,5.,20.,100.,500.,2000.):
        prob=half_line_prob(theta);extended=half_line_prob(theta,70)
        mean=float(np.dot(np.arange(1,len(prob)+1),prob))
        mean_ext=float(np.dot(np.arange(1,len(extended)+1),extended))
        assert abs(prob.sum()-1)<1e-10 and abs(mean-mean_ext)<1e-10
        row={'h_times_age':theta,'probability_sum':float(prob.sum()),'mean_separation':mean,
             'mean_separation_over_h_times_age':mean/theta,'larger_cutoff_mean_difference':abs(mean-mean_ext)}
        if theta<=20:
            n=len(prob);ham=-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1)
            psi=la.expm(-1j*theta*ham)[:,0]
            narray=np.arange(1,n+1);analytic=(1j**(narray-1))*(narray/theta)*jv(narray,2*theta)
            distance=float(la.norm(psi-analytic));assert distance<2e-12
            row['full_finite_matrix_amplitude_distance']=distance
        rows.append(row)
    k=sp.symbols('k',real=True)
    coefficient=sp.integrate(4*sp.sin(k)**3/sp.pi,(k,0,sp.pi))
    assert coefficient==sp.Rational(16,3)/sp.pi
    assert abs(rows[-1]['mean_separation_over_h_times_age']-float(coefficient))<1e-6
    return {'asymptotic_mean_velocity_over_h_exact':str(coefficient),'controls':rows}


def reduced_susceptibility():
    rows=[];J=1.;duration=1.;target=4*J*duration**2/(3*np.pi)
    for eps in (.2,.1,.05,.025):
        h=J/(2*eps**2)
        integral,error=quad(lambda age:mean_halfline(h*age),0,duration,epsabs=1e-8,epsrel=1e-9,limit=400)
        tight,errtight=quad(lambda age:mean_halfline(h*age),0,duration,epsabs=2e-10,epsrel=2e-11,limit=800)
        assert abs(integral-tight)<1e-7
        val=eps**2*tight
        rows.append({'epsilon':eps,'h':h,'J_scale':J,'time':duration,
                     'new_record_density_derivative_wrt_beta':eps**2*duration,
                     'field_deficit_derivative_wrt_beta':val,
                     'asymptotic_field_derivative':target,
                     'difference_from_asymptote':val-target,
                     'quadrature_error_estimate_after_epsilon2':eps**2*errtight,
                     'two_tolerance_integral_difference':abs(integral-tight)})
    assert abs(rows[-1]['field_deficit_derivative_wrt_beta']-target)<2e-5
    return {'definition':'Exact beta=0 linear susceptibility for a declared reduced single-birth half-line quantum-walk kernel; not the proved microscopic Lindblad limit.',
            'order_of_limits':'Take volume to infinity before epsilon to zero for field derivative 4 J T^2/(3 pi); reversing the limits gives zero.',
            'controls':rows}


def main():
    start=time.monotonic()
    data={'status':'PASS','exact_physical_sectors':exact_sectors(),'PXP_and_live_constraints':pxp_and_immobility(),
          'halfline_quantum_walk':halfline_controls(),'reduced_birth_transport':reduced_susceptibility(),
          'runtime_seconds':time.monotonic()-start,
          'limits':'Second-order microscopic coefficients and reduced transport asymptotics are separately checked. No uniform microscopic effective-dynamics theorem, finite-beta interacting limit, 3D photon claim or native closure is asserted.'}
    text=json.dumps(data,indent=2)+'\n';(OUT/'ONE_DIMENSIONAL_RECORD_FIELD_TRANSPORT_RESULTS.json').write_text(text);print(text,end='')


if __name__=='__main__':main()
