"""Complete small occupation-space controls for the new commuting penalty."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from collections import Counter

HERE=Path(__file__).resolve().parent

def main():
    L=4;V=L*L;d=2;z=4
    def site(x,y):return (x%L)*L+y%L
    edges=[(site(x,y),site(x+1,y)) for x in range(L) for y in range(L)]
    edges += [(site(x,y),site(x,y+1)) for x in range(L) for y in range(L)]
    neighbors=[set() for _ in range(V)]
    for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
    assert all(len(n)==z for n in neighbors)
    A=sum(1<<site(x,y) for x in range(L) for y in range(L) if (x+y)%2==0)
    B=((1<<V)-1)^A
    source,dest=edges[0]
    halo={source,dest}|neighbors[source]|neighbors[dest]
    by_halo={};zero=[];energy_counts=Counter();grade_counts=Counter()
    total_hops=0
    for word in range(1<<V):
        n=[(word>>i)&1 for i in range(V)]
        violations=sum((n[a]+n[b]-1)**2 for a,b in edges)
        assert violations%2==0
        energy=violations//2
        formula=sum(n[a]*n[b] for a,b in edges)-d*sum(n)+d*V//2
        assert energy==formula and energy>=0
        energy_counts[energy]+=1
        if energy==0:zero.append(word)
        if n[source] and not n[dest]:
            target=word^(1<<source)^(1<<dest)
            nn=[(target>>i)&1 for i in range(V)]
            target_energy=sum((nn[a]+nn[b]-1)**2 for a,b in edges)//2
            grade=target_energy-energy
            local_grade=sum(n[v] for v in neighbors[dest]-{source})-sum(n[v] for v in neighbors[source]-{dest})
            assert grade==local_grade
            halo_word=tuple(n[v] for v in sorted(halo))
            if halo_word in by_halo:assert by_halo[halo_word]==grade
            else:by_halo[halo_word]=grade
            grade_counts[grade]+=1;total_hops+=1
    assert set(zero)=={A,B}
    assert grade_counts[0]>0
    assert by_halo[tuple((A>>v)&1 for v in sorted(halo))]==z-1
    src=Path(__file__).read_bytes()
    out={"created_utc":datetime.now(timezone.utc).isoformat(),
       "source":{"path":str(Path(__file__).resolve()),"bytes":len(src),"sha256":hashlib.sha256(src).hexdigest()},
       "torus":{"dimension":d,"period":L,"vertices":V,"edges":len(edges)},
       "all_occupations_checked":1<<V,"penalty_eigenvalue_multiplicities":dict(sorted(energy_counts.items())),
       "zero_energy_occupations":zero,"exactly_two_checkerboards":True,
       "selected_directed_edge":[source,dest],"complete_hop_count":total_hops,
       "hop_grade_multiplicities":dict(sorted(grade_counts.items())),
       "grade_depends_only_on_one_halo":True,"halo_sites":sorted(halo),
       "ground_single_hop_grade":z-1,
       "zero_grade_excited_hopping_exists":True,
       "locality_consequence":"The full normal form retains O(t) excited-sector motion; use an O(epsilon^-3) velocity, not the previous O(epsilon^-2) bound.",
       "scope":"Complete occupancy algebra control on a 4x4 torus, not the all-size local theorem (which uses periods >=6)."}
    (HERE/"HOMOGENEOUS_OCCUPANCY_PENALTY_RESULTS.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
