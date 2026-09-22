"""Homogeneous repulsion and background-free charged-record exchange controls.
Hard-core contents are transported unchanged. No earlier physics runner imported.
"""
from pathlib import Path
from itertools import product, permutations
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,json,math
import sympy as s
HERE=Path(__file__).resolve().parent

def square(spin,z):
    C=s.Integer(spin*(spin+1));states=[]
    for q in product((-1,0,1),repeat=4):
        if sum(q) or sum(x!=0 for x in q)!=2:continue
        for last in range(-spin,spin+1):
            cur=last;e=[]
            for charge in q:cur+=charge;e.append(cur)
            assert cur==last
            if max(e)<=spin and min(e)>=-spin:states.append((q,tuple(e)))
    states.sort();idx={w:i for i,w in enumerate(states)};D=len(states)
    T=s.zeros(D)
    def amp(m,delta):
        if abs(m+delta)>spin:return s.Integer(0)
        return s.sqrt(1-s.Rational(m*(m+delta),C))
    for col,(q,e) in enumerate(states):
        for edge in range(4):
            a,b=edge,(edge+1)%4
            for source,dest,sign in [(a,b,1),(b,a,-1)]:
                if q[source] and not q[dest]:
                    charge=q[source];delta=-sign*charge;weight=amp(e[edge],delta)
                    if weight:
                        qq=list(q);qq[dest]=charge;qq[source]=0
                        ee=list(e);ee[edge]+=delta
                        T[idx[tuple(qq),tuple(ee)],col]=-weight
    assert T==T.T
    # The z-2 frozen external A neighbors of each internal B site retain
    # the bulk coordination cost. A bare isolated C4 would have another
    # zero-energy checkerboard and is not an adequate denominator control.
    penalty=[]
    for q,e in states:
        n=[int(x!=0) for x in q]
        penalty.append(sum(n[a]*n[(a+1)%4] for a in range(4))+(z-2)*(n[1]+n[3]))
    P=[i for i,(q,e) in enumerate(states) if q[0] and q[2]]
    assert P==[i for i,b in enumerate(penalty) if b==0]
    inv=s.diag(*[s.Rational(1,b) if b else 0 for b in penalty])
    Delta=z-1
    h2=-(T*inv*T).extract(P,P)
    metric=(T*inv*inv*T).extract(P,P)
    h4=-(T*inv*T*inv*T*inv*T).extract(P,P)-(metric*h2+h2*metric)/2
    R=s.zeros(len(P));lowidx={states[j]:i for i,j in enumerate(P)}
    expected2=s.zeros(len(P));diag4=s.zeros(len(P))
    for col,j in enumerate(P):
        q,e=states[j]
        F=[]
        for edge in range(4):
            source=edge if edge%2==0 else (edge+1)%4
            sigma=1 if edge%2==0 else -1
            F.append(1-(e[edge]**2-sigma*q[source]*e[edge])/C)
        assert sum(F)==4+(2-sum(x*x for x in e))/C
        expected2[col,col]=-sum(F)
        diag=sum(f*f for f in F)
        for edge in range(4):
            for other in range(edge+1,4):
                if (other-edge)%2:diag+=2*F[edge]*F[other]
                else:diag-=s.Rational(2,z-2)*F[edge]*F[other]
        diag4[col,col]=s.simplify(diag)
        qa,qc=q[0],q[2];qq=(qc,0,qa,0)
        changes=(-qa,-qa,-qc,-qc)
        ee=tuple(m+d for m,d in zip(e,changes))
        weight=s.prod(amp(m,d) for m,d in zip(e,changes))
        if weight:
            assert (qq,ee) in lowidx
            R[lowidx[qq,ee],col]=weight
    gamma=s.Rational(2*(z-1),z-2)
    assert s.simplify(Delta*h2-expected2)==s.zeros(len(P))
    assert s.simplify(Delta**3*h4-(diag4-gamma*(R+R.T)))==s.zeros(len(P))
    assert R==R.T  # All states here have opposite charges; two orientations coincide.
    return {"spin":spin,"bulk_coordination":z,"dimension":D,"code_dimension":len(P),
      "single_hop_gap":Delta,"plaquette_second_gap":2*(z-2),
      "gamma":str(gamma),"full_second_and_fourth_matrices_match":True,
      "opposite_charge_circulations_coincide":True,
      "low_states":[{"q":q,"E":e} for q,e in [states[j] for j in P]],
      "H2_times_Delta":[list(map(str,row)) for row in (Delta*h2).tolist()],
      "H4_times_Delta_cubed":[list(map(str,row)) for row in s.simplify(Delta**3*h4).tolist()]}

def cubic(d,L,spin):
    vertices=list(product(range(L),repeat=d));vindex={x:i for i,x in enumerate(vertices)}
    def shift(x,a,sign=1):
        y=list(x);y[a]=(y[a]+sign)%L;return tuple(y)
    edges=[(vindex[x],vindex[shift(x,a)]) for x in vertices for a in range(d)]
    eindex={(x,a):i*d+a for i,x in enumerate(vertices) for a in range(d)}
    neighbors=[set() for _ in vertices]
    for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
    A={i for i,x in enumerate(vertices) if sum(x)%2==0}
    charges=[0]*len(vertices);electric=[0]*len(edges)
    for a in A:charges[a]=1 if vertices[a][0]%2==0 else -1
    for i in A:
        x=vertices[i]
        if charges[i]!=1:continue
        y=shift(x,0);end=shift(y,1)
        assert charges[vindex[end]]==-1
        electric[eindex[x,0]]+=1;electric[eindex[y,1]]+=1
    div=[0]*len(vertices)
    for E,(a,b) in zip(electric,edges):div[a]+=E;div[b]-=E
    assert div==charges and sum(charges)==0 and max(map(abs,electric))<=1
    z=2*d;gap=z-1;C=spin*(spin+1);M=len(edges)
    oriented=[];weights=[];linear=0
    for e,(a,b) in enumerate(edges):
        source,dest,sigma=(a,b,1) if a in A else (b,a,-1)
        oriented.append((source,dest))
        linear+=sigma*charges[source]*electric[e]
        w=C-electric[e]**2+sigma*charges[source]*electric[e]
        assert 0<=w<=C;weights.append(w)
    assert linear==len(A)
    assert sum(weights)==M*C+len(A)-sum(E*E for E in electric)
    counts={"meet":0,"r0":0,"r1":0,"r2":0};sums={k:0 for k in counts}
    for e,(a,b) in enumerate(oriented):
        for f in range(e+1,M):
            c,dd=oriented[f];w=weights[e]*weights[f]
            if a==c or b==dd:key="meet"
            else:
                # Literal occupied-neighbor count after both hops.
                occ=A-{a,c}
                energy=len(neighbors[b]&occ)+len(neighbors[dd]&occ)
                cross=int(c in neighbors[b])+int(a in neighbors[dd])
                assert energy==2*gap-cross
                key="r"+str(cross)
            counts[key]+=1;sums[key]+=w
    assert counts["meet"]==len(vertices)*z*(z-1)//2
    assert counts["r2"]==M*(d-1)
    assert counts["r1"]==M*((z-1)**2-2*(d-1))
    canonical=Fraction(sum(weights)**2,C*C)
    for rr in (0,1,2):
        canonical-=Fraction(4*gap*sums["r"+str(rr)],(2*gap-rr)*C*C)
    local=Fraction(sum(w*w for w in weights)+2*sums["meet"],C*C)
    local-=Fraction(2*sums["r1"],(2*z-3)*C*C)
    local-=Fraction(2*sums["r2"],(z-2)*C*C)
    assert local==canonical
    unit=Fraction(M+2*counts["meet"])
    unit-=Fraction(2*counts["r1"],2*z-3)+Fraction(2*counts["r2"],z-2)
    assert unit==Fraction(8*d*d*(d-1)*len(vertices),4*d-3)
    loop_controls=[]
    seen=set()
    for x in vertices:
        if vindex[x] not in A:continue
        for i in range(d):
            for j in range(i+1,d):
                a=vindex[x];b=vindex[shift(x,i)]
                c=vindex[shift(shift(x,i),j)];dd=vindex[shift(x,j)]
                kind="equal" if charges[a]==charges[c] else "opposite"
                if kind in seen:continue
                seen.add(kind)
                # Cyclic a,b,c,d with edge orientations +,+,-,-.
                cycle=[a,b,c,dd]
                edgeids=[eindex[x,i],eindex[shift(x,i),j],eindex[shift(x,j),i],eindex[x,j]]
                signs=[1,1,-1,-1]
                all_orientations=[]
                for direction in (1,-1):
                    seq=cycle if direction==1 else [a,dd,c,b]
                    es=edgeids if direction==1 else [edgeids[3],edgeids[2],edgeids[1],edgeids[0]]
                    ss=signs if direction==1 else [-signs[3],-signs[2],-signs[1],-signs[0]]
                    legs=[(seq[k],seq[(k+1)%4],es[k],ss[k],0 if k<2 else 1) for k in range(4)]
                    valid=[];finals=[]
                    for order in permutations(range(4)):
                        occ={site:charges[site] for site in A}
                        ids={a:0,c:1};E=list(electric);den=[]
                        amplitude2=Fraction(1)
                        good=True
                        for number,legidx in enumerate(order):
                            source,dest,edge,sgn,tag=legs[legidx]
                            if source not in ids or ids[source]!=tag or dest in occ:good=False;break
                            charge=occ.pop(source);occ[dest]=charge
                            ids[dest]=ids.pop(source)
                            change=-sgn*charge
                            if abs(E[edge]+change)>spin:good=False;break
                            amplitude2*=Fraction(C-E[edge]*(E[edge]+change),C)
                            E[edge]+=change
                            if number<3:
                                # Only newly occupied B sites can make occupied bonds.
                                energy=sum(len(neighbors[v]&set(occ)) for v in set(occ)-A)
                                den.append(energy)
                        if good:
                            assert den==[gap,2*(z-2),gap]
                            valid.append({"order":order,"denominators":den,"amplitude_squared":str(amplitude2)})
                            finals.append((tuple(sorted(occ.items())),tuple(E)))
                    assert len(valid)==4 and len(set(finals))==1
                    all_orientations.append({"direction":direction,"paths":valid,"final":finals[0]})
                same=all_orientations[0]["final"]==all_orientations[1]["final"]
                assert same==(kind=="opposite")
                loop_controls.append({"charge_pair":kind,"two_orientations_same_joint_target":same,
                   "orientations":[{k:v for k,v in row.items() if k!="final"} for row in all_orientations]})
    return {"dimension":d,"period":L,"spin":spin,"vertices":len(vertices),"edges":M,
        "Gauss_background":0,"total_charge":sum(charges),"occupied_sites":len(A),
        "uniform_preparation_max_abs_E":max(map(abs,electric)),
        "sum_charge_weighted_linear_E":linear,"pair_counts":counts,
        "weighted_diagonal_H4_normalized":str(local),
        "unit_shift_diagonal_constant":str(unit),
        "unit_shift_constant_per_site":str(unit/len(vertices)),
        "oriented_plaquette_gamma":str(Fraction(2*(z-1),z-2)),
        "local_exchange_controls":loop_controls}

def main():
    b=Path(__file__).read_bytes()
    out={"created_utc":datetime.now(timezone.utc).isoformat(),
      "source":{"path":str(Path(__file__).resolve()),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()},
      "guarded_square_controls":[square(S,z) for S,z in [(1,4),(2,4),(1,6),(2,6),(3,6)]],
      "cubic_controls":[cubic(d,6,2) for d in (2,3)],
      "status":"Author exact low-order controls passed for a new supplied homogeneous charged-record model.",
      "scope":"Coefficients and invariants; a uniform dynamics/phase theorem is not established by these finite controls."}
    (HERE/"HOMOGENEOUS_CHARGED_RECORDS_RESULTS.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
