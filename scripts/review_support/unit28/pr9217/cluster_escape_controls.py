"""Personal full-charge primitive matrix element; reuses declared personal42 geometry."""
from pathlib import Path
from collections import Counter
import hashlib,json,time
from birth_geometry import geometry,gauss,birth

def hop(q,E,a,b,e,outward):
    src,dst=(a,b) if outward else (b,a)
    if q[src]==0 or q[dst]!=0:return None
    charge=q[src];out=list(q);field=list(E)
    out[src]=0;out[dst]=charge;field[e]+=(-1 if outward else 1)*charge
    # Exact local charge/flux change; propagation of the input Gauss law.
    assert out[a]-q[a]==field[e]-E[e]
    assert out[b]-q[b]==-(field[e]-E[e])
    return tuple(out),tuple(field)

def pair_column_target(q,E,a,d,adjacent,target):
    count=0;matches=[];legal=Counter()
    for u,eu in adjacent[a]:
        s1=hop(q,E,a,u,eu,True)
        if s1 is None:continue
        legal['first_outward']+=1
        for v,ev in adjacent[d]:
            s2=hop(*s1,d,v,ev,True)
            if s2 is None:continue
            legal['second_outward']+=1
            for w,ew in adjacent[d]:
                s3=hop(*s2,d,w,ew,False)
                if s3 is None:continue
                legal['first_return']+=1
                for z,ez in adjacent[a]:
                    s4=hop(*s3,a,z,ez,False)
                    if s4 is None:continue
                    legal['second_return']+=1
                    if s4==target:
                        count+=1;matches.append({'outward':[a,u,d,v],'return':[d,w,a,z],
                            'states':[{'q':s[0],'E':s[1]} for s in [(q,E),s1,s2,s3,s4]]})
    return count,matches,dict(legal)

def main():
    started=time.perf_counter();results=[]
    for L in (4,6):
        V,A,edges,near=geometry(L);ix={v:i for i,v in enumerate(V)};Aset=set(A)
        a,b,c,d,u,v=[ix[t] for t in [(0,0,0),(L-1,0,0),(0,L-1,0),(1,1,0),(1,0,0),(0,1,0)]]
        edgeindex={edge:i for i,edge in enumerate(edges)}
        bg=tuple(int(i in Aset) for i in range(len(V)));E0=(0,)*len(edges)
        initial=birth(bg,E0,a,b,c,edgeindex[a,b],edgeindex[a,c],-1,A,edges)
        sequence=[initial]
        for aa,bb,outward in [(a,u,True),(d,v,True),(d,u,False),(a,v,False)]:
            result=hop(*sequence[-1],aa,bb,edgeindex[aa,bb],outward)
            assert result is not None;gauss(*({'q':result[0],'E':result[1]}[s] for s in ['q','E']),A,edges)
            sequence.append(result)
        target=sequence[-1]
        minus=[i for i,x in enumerate(target[0]) if x==-1];occupiedB=[i for i,x in enumerate(target[0]) if x and i not in Aset]
        assert minus==[d] and set(occupiedB)=={b,c}
        distance=lambda x,y:sum(min((r-s)%L,(s-r)%L) for r,s in zip(V[x],V[y]))
        assert distance(d,b)==distance(d,c)==3
        assert not set(occupiedB)&{x for x,e in near[d]}
        gauss(target[0],target[1],A,edges)
        allpairs={tuple(sorted((p,r))) for p in A for r in A if p!=r and {x for x,e in near[p]}&{x for x,e in near[r]}}
        rows=[];H4numerators={-1:0,1:0};Gammanumerators={-1:0,1:0};all_matches=[]
        for sigma in (-1,1):
            for outward,eo in near[a]:
                if outward==b:continue
                source=birth(bg,E0,a,b,outward,edgeindex[a,b],eo,sigma,A,edges)
                changed={x for x in A if source[0][x]!=target[0][x]}
                candidates=sorted(p for p in allpairs if changed<=set(p))
                assert candidates==[(a,d)] if sigma==-1 else all(d in p for p in candidates)
                for x,y in candidates:
                    coefficient,matches,counts=pair_column_target(*source,x,y,near,target)
                    H4numerators[sigma]-=2*coefficient
                    rows.append({'sigma':sigma,'birth_outward':outward,'pair':[x,y],'target_Gram_coefficient':coefficient,'legal_path_counts':counts})
                    for match in matches:
                        for state in match['states']:gauss(state['q'],state['E'],A,edges)
                    all_matches += [{'sigma':sigma,'birth_outward':outward,**m} for m in matches]
                # Gamma=2kappa sum_x F_x^* G_x F_x; each term changes
                # at most one A charge. Coherent sign cross terms vanish.
                for x in A:
                    if not changed<={x}:continue
                    for y,ey in near[x]:
                        mid=hop(*source,x,y,ey,True)
                        if mid is None:continue
                        vacancy_count=sum(mid[0][z]==0 for z,ez in near[x])
                        for z,ez in near[x]:
                            final=hop(*mid,x,z,ez,False)
                            if final==target:Gammanumerators[sigma]+=2*vacancy_count
        assert H4numerators=={-1:-4,1:0},H4numerators
        assert Gammanumerators=={-1:0,1:0},Gammanumerators
        assert len(all_matches)==2 and all(m['sigma']==-1 and m['birth_outward']==c for m in all_matches)
        results.append({'L':L,'vertices':V,'A_sites':A,'oriented_edges':edges,
          'named_sites':{'a':a,'b':b,'c':c,'d':d,'u':u,'v':v},'actual_selected_birth_source':{'q':initial[0],'E':initial[1]},
          'target':{'q':target[0],'E':target[1]},'target_distances_to_positive_B':[3,3],
          'all_relevant_pair_rows':rows,'all_matching_primitive_paths':all_matches,
          'H4_target_numerators_before_birth_normalization':{str(k):v for k,v in H4numerators.items()},
          'Gamma_target_numerators_in_kappa':{str(k):v for k,v in Gammanumerators.items()},
          'birth_squared_norms':{'resolved_minus':5,'resolved_plus':5,'coherent':10},
          'exact_initial_target_probability_coefficients_in_delta_squared':{'resolved_minus':'16/5','resolved_plus':'0','coherent':'8/5'},
          'all_integer_Gauss_and_coefficient_assertions':True})
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'personal42_helper_sha256':hashlib.sha256((Path(__file__).parent/'birth_geometry.py').read_bytes()).hexdigest(),
       'scope':'Exact one-step full H4/Gamma target matrix elements on actual original birth states; no finite-time lifetime or particle exclusion.',
       'results':results,'elapsed_seconds':time.perf_counter()-started},indent=2))

if __name__=='__main__':main()
