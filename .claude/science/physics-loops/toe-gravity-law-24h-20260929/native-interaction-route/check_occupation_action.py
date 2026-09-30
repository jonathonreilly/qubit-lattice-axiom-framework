#!/usr/bin/env python3
"""Independent author control: actual hard-core four-site amplitudes.

No import of compute_quartic.py. <100MB,<60s, one thread. Gaussian integer
test amplitudes use binary-exact complex integer arithmetic; every norm and
matrix result is explicitly checked integral. No many-body torus enumeration.
"""
from pathlib import Path
from itertools import combinations,product
from datetime import datetime,timezone
from collections import defaultdict
import json,time,resource
OUT=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert datetime.now(timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
start=time.monotonic();data=json.loads((OUT/'quartic.json').read_text())
O=(0,0,0);E=[tuple(int(i==j) for j in range(3)) for i in range(3)]
plus=lambda x,y:tuple(a+b for a,b in zip(x,y))
neg=lambda x:tuple(-a for a in x)
def ni(z):
    z=complex(z)
    assert z.imag==0 and z.real==int(z.real) and abs(z.real)<2**52
    return int(z.real)
def norm(z):return ni(z.conjugate()*z)
def edge(a,b,z):
    d=tuple(y-x for x,y in zip(a,b));nz=[i for i in range(3) if d[i]]
    if len(nz)==1 and abs(d[nz[0]])==2:return [z[0],z[1],-z[0]-z[1]][nz[0]]
    if len(nz)==2 and all(abs(d[i])==1 for i in nz):
        return -d[nz[0]]*d[nz[1]]*z[{(0,1):2,(0,2):3,(1,2):4}[tuple(nz)]]
    return 0j
def full4(s,z):
    if len(set(s))!=4:return 0j
    a,b,c,d=s
    return 2*(edge(a,b,z)*edge(c,d,z)+edge(a,c,z)*edge(b,d,z)+edge(a,d,z)*edge(b,c,z))
neighbor=[x for x in product(range(-2,3),repeat=3) if edge(O,x,[1,1,1,1,1])]
assert len(neighbor)==18
op=[(E[i],neg(E[i]),1) for i in range(3)]
planes=[]
for i,j in combinations(range(3),2):
    ids=[]
    for s,t in product([-1,1],repeat=2):
        ids.append(len(op));op.append((tuple(s*a for a in E[i]),tuple(t*a for a in E[j]),s*t))
    planes.append(ids)
centers=[O]+E
U=set()
for x in centers:
    for a,b,s in op:
        for p in [plus(x,a),plus(x,b)]:
            U.add(p)
            U.update(plus(p,d) for d in neighbor)
# Add disconnected residual-pair controls outside the local neighborhood.
remote=[((20,20,20),(22,20,20)),((20,20,20),(21,21,20))]
residual=list(combinations(sorted(U),2))+remote
mon=[tuple(data['coordinates'].index(x) for x in m) for m in data['monomial_order']]
def matrix_eval(key,z):
    m=[z[i]*z[j] for i,j in mon];G=data[key]
    return ni(sum(m[i].conjugate()*G[i][j]*m[j] for i in range(15) for j in range(15)))
directions=[('E',[1,-1,0,0,0]),('T',[0,0,1,0,0]),('mixed',[1,-1,1j,0,0]),
 ('general_complex',[1+1j,-2+1j,2-1j,1j,-1]),('general_real',[1,2,-1,2,1])]
rows=[]
for name,z in directions:
    z=list(map(complex,z));AE=AT=W=0
    for r in residual:
        acts=[]
        for x in centers:
            acts.append([s*full4((plus(x,a),plus(x,b))+r,z) for a,b,s in op])
        p=acts[0]
        # C² has amplitude twice the matching polynomial. Thus 12 E4 uses
        # weights 2,3/4 etc; retain an overall4 on both sides to stay integer.
        AE+=8*norm(sum(p[:3]))
        for ids in planes:
            AT+=sum(3*norm(p[i]-p[j]) for i,j in combinations(ids,2))
        for q in acts[1:]:
            d=[b-a for a,b in zip(p,q)]
            W+=12*sum(norm(t) for t in d[:3])-4*norm(sum(d[:3]))
            W+=sum(3*norm(sum(d[i] for i in ids)) for ids in planes)
    DD=12*sum(norm(full4((O,)+s,z)) for s in combinations(neighbor,3))
    assert AE+AT+DD==4*matrix_eval('energy_mu_matrix_numerator',z)
    assert W==4*matrix_eval('energy_tau_matrix_numerator',z)
    rows.append({'direction':name,'direct_energy_mu_numerator_over_48':AE+AT+DD,'direct_energy_tau_numerator_over_48':W})

# Independent finite 19-site graph check of all coherent cycle and exclusion
# terms in the number correction: explicitly create ordered pairs twice.
patch=[O]+neighbor;number_rows=[]
for name,z in directions:
    z=list(map(complex,z));edges={p:edge(*p,z) for p in combinations(patch,2) if edge(*p,z)}
    state=defaultdict(complex)
    for (a,b),w in edges.items():
        for (c,d),v in edges.items():
            if len({a,b,c,d})==4:state[tuple(sorted((a,b,c,d)))]+=w*v
    s=sum(norm(w) for w in edges.values());r=sum(norm(w) for w in state.values())
    direct=r-2*s*s
    exclusions=-2*sum(norm(w)**2 for w in edges.values())
    for x in patch:
        inc=[w for p,w in edges.items() if x in p]
        exclusions-=4*sum(norm(w)*norm(v) for w,v in combinations(inc,2))
    coherent=0;cycles=0
    for a,b,c,d in combinations(patch,4):
        p=[edge(a,b,z)*edge(c,d,z),edge(a,c,z)*edge(b,d,z),edge(a,d,z)*edge(b,c,z)]
        coherent+=8*sum(ni((w.conjugate()*v).real) for w,v in combinations(p,2))
        if sum(bool(w) for w in p)>1:cycles+=1
    assert direct==exclusions+coherent
    number_rows.append({'direction':name,'sites':len(patch),'edges':len(edges),'four_particle_support':len(state),'direct_connected_number_numerator':direct,'exclusion_term':exclusions,'coherent_cycle_term':coherent,'interfering_four_sets':cycles})

# Exact identity checks and orientation witnesses; this is polynomial algebra,
# not a numerical minimization over amplitudes.
def evalpart(key,z,den):return matrix_eval(key,list(map(complex,z)))/den
for a,b in [(1,0),(1,-1),(1,1j),(2+1j,-1+2j)]:
    z=[a,b,0,0,0];s=norm(complex(a))+norm(complex(b))+norm(complex(a+b))
    assert matrix_eval('energy_mu_matrix_numerator',list(map(complex,z)))==12*52*s*s
    assert matrix_eval('energy_tau_matrix_numerator',list(map(complex,z)))==12*120*s*s
out={'occupation_controls':rows,'number_patch_controls':number_rows,'residual_vertex_set_size':len(U),
 'residual_pairs_tested_per_direction':len(residual),'directions':len(directions),
 'elapsed_s':time.monotonic()-start,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'coverage':'Direct actual four-site amplitudes for five Gaussian-integer directions, all local residual pairs plus distant controls; exact finite-graph number-cumulant checks. Full coefficient identity remains carried by the symbolic generator and analytic support proof.'}
(OUT/'occupation_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
