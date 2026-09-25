"""New PRE43 primitive colored rotor calculation; no local scientific imports.

States are (occupied-vertex bitset, minus-color bitset, sparse integer field).
Every edge is oriented from A to B. No angle, color or electric dephasing occurs.
Only Q=(Pi_2-P_nn) H4 is restricted to active star unions; the proof that omitted
terms cannot alter the matter grouping is given in PRE.md. All loss stars are
included. The optional explicit instrument reconstruction is a second route
to the loss action, not a replacement instrument.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from hashlib import sha256
import argparse, json, time

HERE=Path(__file__).resolve().parent

class Torus:
    def __init__(self,side):
        self.L=side
        self.vertices=list(product(range(side),repeat=3))
        self.index={v:i for i,v in enumerate(self.vertices)}
        self.A=[i for i,v in enumerate(self.vertices) if sum(v)%2==0]
        self.Aset=set(self.A)
        self.B=[i for i in range(len(self.vertices)) if i not in self.Aset]
        self.Amask=sum(1<<i for i in self.A)
        self.Bmask=sum(1<<i for i in self.B)
        self.ns={}
        for i,v in enumerate(self.vertices):
            adjacent=set()
            for axis in range(3):
                for sign in (-1,1):
                    w=list(v);w[axis]=(w[axis]+sign)%side
                    adjacent.add(self.index[tuple(w)])
            self.ns[i]=tuple(sorted(adjacent))
        assert all(len(v)==6 for v in self.ns.values())
        self.edges=[(a,b) for a in self.A for b in self.ns[a]]
        self.edgeid={edge:i for i,edge in enumerate(self.edges)}
        self.pairs=[(a,c) for a,c in combinations(self.A,2) if set(self.ns[a])&set(self.ns[c])]
        self.unions={(a,c):set(self.ns[a])|set(self.ns[c]) for a,c in self.pairs}

    def site(self,v):return self.index[tuple(x%self.L for x in v)]

    @staticmethod
    def bits(mask):
        result=[]
        while mask:
            bit=mask&-mask;result.append(bit.bit_length()-1);mask-=bit
        return result

    def charge(self,state,site):
        return 0 if not state[0]&(1<<site) else (-1 if state[1]&(1<<site) else 1)

    def shift(self,field,a,b,value):
        e=self.edgeid[(a,b)];answer=dict(field);answer[e]=answer.get(e,0)+value
        if answer[e]==0:del answer[e]
        return tuple(sorted(answer.items()))

    def hop(self,state,a,b,outward):
        source,target=(a,b) if outward else (b,a)
        occ,minus,field=state;source_bit=1<<source;target_bit=1<<target
        if not occ&source_bit or occ&target_bit:return None
        sign=-1 if minus&source_bit else 1
        occ=(occ^source_bit)|target_bit
        if sign==-1:minus=(minus^source_bit)|target_bit
        field=self.shift(field,a,b,-sign if outward else sign)
        return occ,minus,field

    def pair(self,state,a,b,sign,create):
        occ,minus,field=state;abits=(1<<a)|(1<<b)
        negbit=1<<(a if sign==-1 else b)
        if create:
            if occ&abits:return None
            return occ|abits,minus|negbit,self.shift(field,a,b,sign)
        if self.charge(state,a)!=sign or self.charge(state,b)!=-sign:return None
        return occ^abits,minus^negbit,self.shift(field,a,b,-sign)

    def birth(self,state,a,b,sign):
        result=Counter()
        for v in self.ns[a]:
            moved=self.hop(state,a,v,True)
            if moved is not None:
                output=self.pair(moved,a,b,sign,True)
                if output is not None:result[output]+=1
        return result

    def birth_adjoint(self,state,a,b,sign):
        result=Counter();vacant=self.pair(state,a,b,sign,False)
        if vacant is not None:
            for v in self.ns[a]:
                output=self.hop(vacant,a,v,False)
                if output is not None:result[output]+=1
        return result

    def outside_union(self,state):
        occ,minus,_=state
        assert occ&self.Amask==self.Amask
        assert (occ&self.Bmask).bit_count()==2 and minus.bit_count()==1
        d=minus.bit_length()-1
        return d in self.Aset and not any(occ&(1<<b) for b in self.ns[d])

    def gauss(self,state):
        occ,minus,field=state;div=Counter()
        for e,value in field:
            a,b=self.edges[e];div[a]+=value;div[b]-=value
        for v in range(len(self.vertices)):
            assert div[v]==self.charge(state,v)-(1 if v in self.Aset else 0)
        assert sum(self.charge(state,v) for v in range(len(self.vertices)))==len(self.A)

    def electric(self,state):
        answer=0
        for e,value in state[2]:
            a,b=self.edges[e]
            if self.charge(state,b)==0:
                answer+=value*(value-self.charge(state,a))
        assert answer>=0
        return answer

    def format_state(self,state):
        return {'occupied_B':[self.vertices[b] for b in self.bits(state[0]&self.Bmask)],
                'minus_locations':[self.vertices[v] for v in self.bits(state[1])],
                'vacant_A':[self.vertices[a] for a in self.A if not state[0]&(1<<a)],
                'electric':[[self.vertices[self.edges[e][0]],self.vertices[self.edges[e][1]],value] for e,value in state[2]]}

    def magnetic_leak(self,state):
        occupied_B=set(self.bits(state[0]&self.Bmask));out=Counter();counts=Counter()
        for a,c in self.pairs:
            if not self.unions[(a,c)]&occupied_B:continue
            counts['active_pairs']+=1
            for u in self.ns[a]:
                first=self.hop(state,a,u,True)
                if first is None:continue
                for v in self.ns[c]:
                    second=self.hop(first,c,v,True)
                    if second is None:continue
                    counts['ordered_outward_pairs']+=1
                    for w in self.ns[c]:
                        third=self.hop(second,c,w,False)
                        if third is None:continue
                        for z in self.ns[a]:
                            final=self.hop(third,a,z,False)
                            if final is None:continue
                            counts['complete_paths']+=1
                            if self.outside_union(final):
                                out[final]-=2;counts['leaking_paths']+=1
        return out,dict(counts)

    def loss(self,vector):
        out=Counter()
        for state,coefficient in vector.items():
            for a in self.A:
                empty=sum(self.charge(state,b)==0 for b in self.ns[a])
                if empty<2:continue
                weight=2*(empty-1)
                for v in self.ns[a]:
                    first=self.hop(state,a,v,True)
                    if first is None:continue
                    for w in self.ns[a]:
                        final=self.hop(first,a,w,False)
                        if final is not None:out[final]+=coefficient*weight
        return out

    def instrument_loss(self,vector,coherent):
        out=Counter();cross=0
        for a,b in self.edges:
            if coherent:
                intermediate=Counter()
                for state,weight in vector.items():
                    for sign in (-1,1):
                        for target,c in self.birth(state,a,b,sign).items():intermediate[target]+=weight*c
                for state,weight in intermediate.items():
                    for sign in (-1,1):
                        for target,c in self.birth_adjoint(state,a,b,sign).items():out[target]+=weight*c
            else:
                for sign in (-1,1):
                    intermediate=Counter()
                    for state,weight in vector.items():
                        for target,c in self.birth(state,a,b,sign).items():intermediate[target]+=weight*c
                    for state,weight in intermediate.items():
                        assert not self.birth_adjoint(state,a,b,-sign)
                        for target,c in self.birth_adjoint(state,a,b,sign).items():out[target]+=weight*c
        return out

    def explicit_witness(self,sign):
        a=self.site((0,0,0));b=self.site((-1,0,0));c0=self.site((0,0,1))
        initial=self.pair(self.hop((self.Amask,0,()),a,c0,True),a,b,sign,True)
        if sign==1:
            d=self.site((-1,1,0));e=self.site((0,2,0))
            u=self.site((-1,2,0));v=self.site((0,2,1))
            operations=[(d,u,True),(e,v,True),(e,u,False),(d,b,False)]
        else:
            d=self.site((1,1,0));u=self.site((1,0,0));v=self.site((0,1,0))
            operations=[(a,u,True),(d,v,True),(d,u,False),(a,v,False)]
        states=[initial];steps=[]
        for left,right,outward in operations:
            before=states[-1];charge=self.charge(before,left if outward else right)
            state=self.hop(before,left,right,outward);assert state is not None
            self.gauss(state);states.append(state)
            steps.append({'A':self.vertices[left],'B':self.vertices[right],
                          'direction':'out' if outward else 'return','charge':charge,
                          'state':self.format_state(state)})
        final=states[-1];assert self.outside_union(final)
        return initial,final,{'initial':self.format_state(initial),'steps':steps,
                            'final':self.format_state(final),
                            'minus_to_positive_B_distances':[sum(min(abs(x-y),self.L-abs(x-y)) for x,y in zip(self.vertices[d],self.vertices[p])) for p in self.bits(final[0]&self.Bmask)]}

def norm_squared(vector):return sum(value*value for value in vector.values())

def rows(lattice,vector):
    return [{'coefficient':coefficient,**lattice.format_state(state)} for state,coefficient in sorted(vector.items()) if coefficient]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--side',type=int,required=True)
    parser.add_argument('--check-instrument',action='store_true');parser.add_argument('--output',required=True)
    args=parser.parse_args();tick=time.perf_counter();lattice=Torus(args.side)
    a=lattice.site((0,0,0));b=lattice.site((-1,0,0));bare=(lattice.Amask,0,())
    birth={sign:lattice.birth(bare,a,b,sign) for sign in (-1,1)}
    assert all(norm_squared(v)==5 for v in birth.values())
    coherent=Counter(birth[-1]);coherent.update(birth[1]);assert norm_squared(coherent)==10
    leaks={};losses={};results=[];branch_counts=[]
    for sign in (-1,1):
        leak=Counter();individual=[]
        for state,coefficient in birth[sign].items():
            lattice.gauss(state);assert not lattice.outside_union(state) and lattice.electric(state)==0
            one,counts=lattice.magnetic_leak(state)
            for target,value in one.items():leak[target]+=coefficient*value
            individual.append(norm_squared(one))
            branch_counts.append({'sign':sign,'initial':lattice.format_state(state),**counts,
                                  'individual_QH4_norm_squared':norm_squared(one)})
        gamma=lattice.loss(birth[sign])
        for state in leak:lattice.gauss(state);assert lattice.outside_union(state)
        for state in gamma:lattice.gauss(state)
        assert not any(lattice.outside_union(state) for state in gamma)
        if args.check_instrument:
            assert gamma==lattice.instrument_loss(birth[sign],False)
            assert gamma==lattice.instrument_loss(birth[sign],True)
        leaks[sign]=leak;losses[sign]=gamma
        results.append({'initial_sign':sign,'input_norm_squared':5,
            'QH4_raw_norm_squared':norm_squared(leak),
            'normalized_t_squared_delta_squared_coefficient':str(Fraction(norm_squared(leak),5)),
            'dephased_initial_branch_coefficient':str(Fraction(sum(individual),5)),
            'loss_expectation_over_kappa':str(Fraction(sum(c*gamma.get(state,0) for state,c in birth[sign].items()),5)),
            'Q_loss_exactly_zero':True,'QH4_rows':rows(lattice,leak),'loss_rows':rows(lattice,gamma)})
    all_leak=Counter(leaks[-1])
    for state,value in leaks[1].items():all_leak[state]+=value
    all_loss=lattice.loss(coherent)
    expected_loss=Counter(losses[-1]);expected_loss.update(losses[1]);assert all_loss==expected_loss
    overlap=sum(value*leaks[1].get(state,0) for state,value in leaks[-1].items())
    witnesses=[]
    for sign in (-1,1):
        initial,final,witness=lattice.explicit_witness(sign)
        assert initial in birth[sign]
        witness.update({'initial_sign':sign,'H4_raw_birth_amplitude':leaks[sign].get(final,0),
                        'other_sign_amplitude':leaks[-sign].get(final,0),
                        'coherent_raw_amplitude':all_leak.get(final,0)})
        assert witness['H4_raw_birth_amplitude']!=0
        witnesses.append(witness)
    # A valid reassignment test: only one positive B remains adjacent to minus A.
    c=lattice.site((0,0,1));u=lattice.site((0,1,0));e=lattice.site((0,2,0));v=lattice.site((0,2,1))
    field=()
    for left,right,value in [(a,c,-1),(a,u,-1),(e,u,1),(e,v,-1)]:field=lattice.shift(field,left,right,value)
    reassigned=(lattice.Amask|(1<<c)|(1<<v),1<<a,field)
    lattice.gauss(reassigned);assert not lattice.outside_union(reassigned)
    result={'scope':__doc__,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'side':args.side,'A_sites':len(lattice.A),'edges':len(lattice.edges),
        'full_retained_A_pairs':len(lattice.pairs),'Q_definition':'Pi_2 minus union permitting either positive B neighbor of minus A; every minus-on-B word is inside.',
        'birth_branch_rows':branch_counts,'resolved':results,
        'coherent':{'operator':'B_edge,+ plus B_edge,-, unnormalized','input_norm_squared':10,
                    'QH4_raw_norm_squared':norm_squared(all_leak),
                    'normalized_t_squared_delta_squared_coefficient':str(Fraction(norm_squared(all_leak),10)),
                    'cross_sign_QH4_inner_product':overlap,
                    'loss_expectation_over_kappa':str(Fraction(sum(c*all_loss.get(state,0) for state,c in coherent.items()),10)),
                    'QH4_rows':rows(lattice,all_leak)},
        'witnesses':witnesses,'reassignment_inside_union':lattice.format_state(reassigned),
        'explicit_resolved_and_coherent_instrument_loss_checked':args.check_instrument,
        'all_initial_electric_D_values_zero':True,'all_saved_Gauss_words_checked':True,
        'elapsed_seconds':time.perf_counter()-tick}
    path=Path(args.output)
    with path.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    summary={k:v for k,v in result.items() if k not in ('resolved','coherent','birth_branch_rows')}
    summary['resolved']=[{k:v for k,v in row.items() if k not in ('QH4_rows','loss_rows')} for row in results]
    summary['coherent']={k:v for k,v in result['coherent'].items() if k!='QH4_rows'}
    summary['row_counts']={'resolved_QH4':[len(row['QH4_rows']) for row in results],
                           'resolved_loss':[len(row['loss_rows']) for row in results],
                           'coherent_QH4':len(result['coherent']['QH4_rows'])}
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
