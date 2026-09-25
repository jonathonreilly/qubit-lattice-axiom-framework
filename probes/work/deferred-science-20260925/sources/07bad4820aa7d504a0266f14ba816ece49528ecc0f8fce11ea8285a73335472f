#!/usr/bin/env python3
"""Independent primitive words and abstract finite marked-count controls.

No parent/author builder is imported. The finite stochastic model is not the
physical cube, rotor Hamiltonian, or prepared photon experiment.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations_with_replacement, product
from math import comb, exp, factorial, fsum
from pathlib import Path
import json
import time


def addv(a, b, modulus=6):
    return tuple((x+y) % modulus for x, y in zip(a,b))


def primitive_pair():
    a=(0,0,0); d=(1,1,0); c=(1,0,0); e=(0,1,0)
    b=(5,0,0); f=(2,1,0)
    directions=[tuple(sign if i==axis else 0 for i in range(3))
                for axis in range(3) for sign in (-1,1)]
    neighbors=lambda v: sorted(addv(v,step) for step in directions)
    assert b not in neighbors(d) and f not in neighbors(a)
    first=[x for x in neighbors(a) if x!=b]
    second=[y for y in neighbors(d) if y!=f]
    assert set(first)&set(second)=={c,e}
    edges=sorted({(a,x) for x in neighbors(a)}|{(d,y) for y in neighbors(d)})
    edge_index={edge:i for i,edge in enumerate(edges)}
    zero=(0,)*len(edges)
    loop=[0]*len(edges)
    for edge,amount in [((a,c),1),((d,c),-1),((d,e),1),((a,e),-1)]:
        loop[edge_index[edge]]=amount
    loop=tuple(loop); negative=tuple(-x for x in loop)
    rows=[]
    for sigma,tau in product((-1,1),repeat=2):
        outputs=defaultdict(list)
        tagged_outputs=defaultdict(list)
        path_count=0
        for x,y in product(first,second):
            if x==y: continue
            path_count+=1
            changes=Counter({a:sigma-1,d:tau-1,b:-sigma,f:-tau})
            changes[x]+=1; changes[y]+=1
            word=tuple(sorted((site,q) for site,q in changes.items() if q))
            shift=[0]*len(edges)
            for edge,value in [((a,x),-1),((d,y),-1),((a,b),sigma),((d,f),tau)]:
                shift[edge_index[edge]]+=value
            divergence=Counter()
            for (aa,bb),value in zip(edges,shift):
                divergence[aa]+=value; divergence[bb]-=value
            assert {site:q for site,q in divergence.items() if q}==dict(word)
            outputs[word].append(tuple(shift))
            tagged_outputs[(x,word)].append(tuple(shift))
        def effect(groups):
            coeff=Counter()
            for shifts in groups.values():
                for left,right in product(shifts,repeat=2):
                    coeff[tuple(r-l for l,r in zip(left,right))]+=1
            return coeff
        coeff=effect(outputs); dephased=effect(tagged_outputs)
        assert path_count==23
        assert coeff==Counter({zero:23,loop:1,negative:1})
        assert dephased==Counter({zero:23}) and dephased!=coeff
        rows.append({'sigma':sigma,'tau':tau,'legal_paths':path_count,
                     'distinct_final_matter_words':len(outputs),
                     'identity_coefficient':coeff[zero],
                     'oriented_cycle_coefficients':[coeff[loop],coeff[negative]],
                     'extra_outward_destination_tag_removes_cross_terms':True})
    return {'scope':'Direct original resolved zero-lag primitive path algebra only.',
            'link_orientation':'A to B','edges':edges,'cycle':loop,'rows':rows}


def poisson_tail(mean, minimum):
    return 1-fsum(exp(-mean)*mean**k/factorial(k) for k in range(minimum))


def polynomial_exp_integral(power, start, stop, rate):
    def anti(t):
        return exp(-rate*t)*fsum(factorial(power)/factorial(k)*t**k/rate**(power-k+1)
                               for k in range(power+1))
    return anti(start)-anti(stop)


def exact_factorial_mean(rate, pj, pl, cap, start, width, lag):
    terms=[]
    for n in range(cap-1):
        for k in range(n+1):
            terms.append(rate**n/factorial(n)*comb(n,k)
                         *polynomial_exp_integral(k,start,start+width,rate)
                         *polynomial_exp_integral(n-k,0,lag,rate))
    return rate**2*pj*pl*fsum(terms)


def word_count(labels):
    return sum(labels[i]==0 and labels[j]==1
               for i in range(len(labels)) for j in range(i+1,len(labels)))


def terminal_word_moments(cap, probabilities):
    m1=m2=0.0
    for labels in product(range(len(probabilities)),repeat=cap):
        weight=1.0
        for label in labels: weight*=probabilities[label]
        count=word_count(labels)
        m1+=weight*count; m2+=weight*count*count
    p,q=probabilities[:2]
    analytic1=comb(cap,2)*p*q
    analytic2=analytic1+2*comb(cap,3)*p*q*(p+q)+6*comb(cap,4)*p*p*q*q
    assert abs(m1-analytic1)<1e-13 and abs(m2-analytic2)<1e-13
    assert m2-m1*m1>m1
    return {'cap':cap,'mean':m1,'second_moment':m2,'variance':m2-m1*m1,
            'three_and_four_event_combinatorics_match_direct_words':True,
            'variance_exceeds_mean_in_terminal_word_control':True}


def grid_count_control(rate, bins, probabilities=(.4,.4,.2), cap=4):
    start=0.; width=3.; lag=3.; horizon=6.; eta=horizon/bins
    assert bins%2==0
    means=[0.,0.]; seconds=[0.,0.]; total=0.; words=0
    for n in range(cap+1):
        for binword in combinations_with_replacement(range(bins),n):
            counts=Counter(binword)
            if n<cap:
                time_weight=exp(-rate*horizon)
                for number in counts.values(): time_weight*=(rate*eta)**number/factorial(number)
            else:
                last=binword[-1]; time_weight=exp(-rate*eta*last)
                for binindex,number in counts.items():
                    if binindex<last: time_weight*=(rate*eta)**number/factorial(number)
                time_weight*=poisson_tail(rate*eta,counts[last])
            eligible=[]
            for i in range(n):
                x0=binword[i]*eta; x1=x0+eta
                for j in range(i+1,n):
                    y0=binword[j]*eta; y1=y0+eta
                    inside=x0>=start and x1<=start+width
                    intersects=x1>start and x0<start+width
                    lower=inside and y1-x0<=lag
                    upper=intersects and max(0.,y0-x1)<=lag
                    eligible.append((i,j,int(lower),int(upper)))
            for labels in product(range(len(probabilities)),repeat=n):
                weight=time_weight
                for label in labels: weight*=probabilities[label]
                lo=hi=0
                for i,j,inner,outer in eligible:
                    if labels[i]==0 and labels[j]==1:
                        lo+=inner; hi+=outer
                assert 0<=lo<=hi<=cap*cap//4
                means[0]+=weight*lo; means[1]+=weight*hi
                seconds[0]+=weight*lo*lo; seconds[1]+=weight*hi*hi
                total+=weight; words+=1
    exact=exact_factorial_mean(rate,*probabilities[:2],cap,start,width,lag)
    assert abs(total-1)<1e-11
    assert means[0]-1e-12<=exact<=means[1]+1e-12
    p,q=probabilities[:2]; lj=rate*p; ll=rate*q
    extra=lj*ll*ll*width*lag*lag+lj*lj*ll*width*lag*min(width,lag)+(lj*ll*width*lag)**2
    variance_lower=max(0.,seconds[0]-exact*exact)
    variance_upper=seconds[1]-exact*exact
    assert seconds[0]<=exact+extra+1e-11
    first_pair=p*q*(1-exp(-rate*width))*(1-exp(-rate*lag))
    four_count_probability_lower=(p*q)**2*poisson_tail(rate*min(width,lag),4)
    assert four_count_probability_lower>0
    return {'rate':rate,'bins':bins,'mesh':eta,'summed_word_states':words,'probability_mass':total,
            'count_mean_lower':means[0],'exact_factorial_count_mean':exact,'count_mean_upper':means[1],
            'count_second_moment_lower':seconds[0],'count_second_moment_upper':seconds[1],
            'count_variance_bracket':[variance_lower,variance_upper],
            'proved_second_moment_upper':exact+extra,
            'first_j_then_next_l_probability':first_pair,
            'positive_probability_of_count_four_lower':four_count_probability_lower,
            'mean_is_not_first_pair_probability':abs(exact-first_pair)>1e-8}


def rare_variance_rows():
    p=q=.4; width=lag=3.; cap=4; rows=[]
    for rate in (0.3,0.1,0.03,0.01):
        mean=exact_factorial_mean(rate,p,q,cap,0.,width,lag)
        lj=rate*p; ll=rate*q
        extra=lj*ll*ll*width*lag*lag+lj*lj*ll*width*lag*min(width,lag)+(lj*ll*width*lag)**2
        rows.append({'rate':rate,'exact_mean':mean,
                     'proved_variance_over_mean_interval':[max(0.,1-mean),1+extra/mean-mean]})
    assert rows[-1]['proved_variance_over_mean_interval'][1]<1.03
    return rows


def main():
    started=time.monotonic()
    results={'scope':'Independent primitive resolved paths plus a separate capped marked pure-birth model. No actual rotor propagation simulated.',
             'primitive_resolved_pair':primitive_pair(),
             'abstract_model':{'states':'record stages 0 through 4','marks':['j','l','other'],
                               'generator':'total rate kappa while stage<4; each mark increments the stage; terminal stage absorbs',
                               'mark_probabilities':[.4,.4,.2],
                               'field_or_photon_preparation':False},
             'terminal_word_moments':terminal_word_moments(4,(.4,.4,.2)),
             'finite_window_rows':[grid_count_control(3.,bins) for bins in (4,8,12)],
             'rare_variance_rows':rare_variance_rows(),
             'elapsed_seconds':time.monotonic()-started,
             'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    text=json.dumps(results,indent=2)+'\n'
    Path(__file__).with_name('UNRESTRICTED_COUNT_CONTROL_RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__': main()
