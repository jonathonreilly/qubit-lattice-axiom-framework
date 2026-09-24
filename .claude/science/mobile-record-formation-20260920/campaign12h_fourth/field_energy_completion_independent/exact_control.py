#!/usr/bin/env python3
"""Independent primitive-path controls; no imported model or author builder."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib, json, platform, subprocess, sys, time

ROOT = Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920')
OUT = Path(__file__).resolve().parent
SCI = ROOT / '.claude/science/mobile-record-formation-20260920'
SOURCES = {
 'campaign12h_fourth/local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md': '42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4',
 'campaign12h_fourth/local_compensation_author/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md': '9bc691a07fd70c1a813852aa0cac55832065b3c95cf3d50e5528845f6613e0b0',
 'campaign12h_fourth/local_compensation_author/ROOT_GENERAL_TARGET_CORRECTION.md': 'c906ed162db678fc2f10bc67afd2af22d929be3fe97fd3a1658cfe12ecd339a9',
 'campaign12h_fourth/local_compensation_locality_author/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS.md': None,
 'campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md': '002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e',
 'campaign12h_third/FINITE_RATE_REPEATED_RECORD_FORMATION.md': None,
}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def clean(v):
    return {k: a for k, a in v.items() if a}

def add(*terms):
    out = defaultdict(Q)
    for scale, vec in terms:
        for state, amp in vec.items():
            out[state] += scale * amp
    return clean(out)

class Graph:
    def __init__(self, nv, aa, edges):
        self.nv, self.aa = nv, tuple(aa)
        self.edges = tuple(sorted(tuple(sorted(e)) for e in edges))
        self.idx = {e:i for i,e in enumerate(self.edges)}
        self.nb = {a:tuple(v if u == a else u for u,v in self.edges if a in (u,v)) for a in range(nv)}

    def W(self, state):
        return sum(state[0][a] == 0 for a in self.aa)

    def gauss(self, state):
        q, ee = state
        div = [0] * self.nv
        for (u,v), e in zip(self.edges, ee):
            div[u] += e
            div[v] -= e
        return all(div[x] + (x in self.aa) == q[x] for x in range(self.nv))

    def shift(self, state, src, dst):
        q, ee = state
        if not q[src] or q[dst]:
            return None
        i = self.idx[tuple(sorted((src,dst)))]
        k = -q[src] if src < dst else q[src]
        qq, ff = list(q), list(ee)
        qq[dst], qq[src] = qq[src], 0
        ff[i] += k
        ans = (tuple(qq), tuple(ff))
        assert self.gauss(ans)
        return ans, i, k

    def birth(self, state, a, b, charge_at_a):
        q, ee = state
        if q[a] or q[b]:
            return None
        i = self.idx[tuple(sorted((a,b)))]
        k = charge_at_a if a < b else -charge_at_a
        qq, ff = list(q), list(ee)
        qq[a], qq[b] = charge_at_a, -charge_at_a
        ff[i] += k
        ans = (tuple(qq), tuple(ff))
        assert self.gauss(ans)
        return ans, i, k

    def hop_sum(self, vec, a=None, reverse=False, target_w=None):
        out = defaultdict(Q)
        for state, amp in vec.items():
            moves = [(a,b) if not reverse else (b,a) for b in self.nb[a]] if a is not None else [(x,y) for u,v in self.edges for x,y in ((u,v),(v,u))]
            for src,dst in moves:
                res = self.shift(state, src,dst)
                if res is not None and (target_w is None or self.W(res[0]) == target_w):
                    out[res[0]] += amp * (1 if a is not None else -1)
        return clean(out)

    def project(self, vec, w):
        return {s:a for s,a in vec.items() if self.W(s) == w}

    def comp(self, vec, gated=True):
        out = {}
        for a in self.aa:
            gate_sites = [c for c in self.aa if c != a and set(self.nb[c]) & set(self.nb[a])]
            inp = {s:x for s,x in vec.items() if not gated or all(s[0][c] != 0 for c in gate_sites)}
            out = add((1,out), (1,self.hop_sum(self.hop_sum(inp,a),a,reverse=True)))
        return out

    def M(self,v):
        return self.hop_sum(self.hop_sum(v,target_w=1),target_w=0)

    def H4(self,v,gated=True):
        c0 = self.project(self.comp(v,gated),0)
        mm = self.M(self.M(v))
        mc = self.M(c0)
        cm = self.project(self.comp(self.M(v),gated),0)
        aca = self.hop_sum(self.project(self.comp(self.hop_sum(v,target_w=1),gated),1),target_w=0)
        zz = v
        for w in (1,2,1,0):
            zz = self.hop_sum(zz,target_w=w)
        return add((1,mm),(-Q(1,2),mc),(-Q(1,2),cm),(1,aca),(-Q(1,2),zz)), zz, aca

    def pair(self,v):
        out = {}
        for ia,a in enumerate(self.aa):
            for c in self.aa[ia+1:]:
                if not set(self.nb[a]) & set(self.nb[c]):
                    continue
                w = self.hop_sum(self.hop_sum(v,a),c)
                w = self.hop_sum(self.hop_sum(w,c,True),a,True)
                out = add((1,out),(-2,w))
        return out

    def electric(self,state):
        q, ee = state
        e2 = sum(e*e for e in ee)
        dd = 0
        for (u,v),e in zip(self.edges,ee):
            a,b = (u,v) if u in self.aa else (v,u)
            sg = 1 if a < b else -1
            if q[a] and not q[b]:
                dd += e*(e-sg*q[a])
        return e2,dd

    def marked_paths(self,state,a,b,charge_at_a,spin=None):
        ans=[]
        for d in self.nb[a]:
            hop = self.shift(state,a,d)
            if hop is None:
                continue
            born = self.birth(hop[0],a,b,charge_at_a)
            if born is None:
                continue
            weight = Q(1)
            for inp,res in ((state,hop),(hop[0],born)):
                if spin is not None:
                    _,i,k = res
                    e = inp[1][i]
                    weight *= 1-Q(e*(e+k),spin*(spin+1))
                    if abs(res[0][1][i]) > spin:
                        weight = Q(0)
            if weight:
                ans.append((born[0],weight,d))
        return ans

def path_field(g,q,free):
    """Solve incidence on a spanning tree by leaf elimination, exactly."""
    remaining=set(range(g.nv)); tree=[]; reached={0}
    while len(reached)<g.nv:
        for i,(u,v) in enumerate(g.edges):
            if (u in reached) != (v in reached):
                tree.append(i); reached.update((u,v)); break
        else:
            raise AssertionError('disconnected control')
    ee=[0]*len(g.edges)
    chords=[i for i in range(len(ee)) if i not in tree]
    for i,z in zip(chords,free): ee[i]=z
    rhs=[q[x]-(x in g.aa) for x in range(g.nv)]
    for i in chords:
        u,v=g.edges[i]; rhs[u]-=ee[i]; rhs[v]+=ee[i]
    left=set(tree)
    while left:
        deg={x:[] for x in remaining}
        for i in left:
            u,v=g.edges[i]; deg[u].append(i); deg[v].append(i)
        x=next(x for x in remaining if len(deg[x])==1)
        i=deg[x][0]; u,v=g.edges[i]; y=v if x==u else u
        ee[i]=rhs[x] if x==u else -rhs[x]
        rhs[y]+=rhs[x]
        remaining.remove(x); left.remove(i)
    assert sum(rhs[x] for x in remaining)==0
    state=(tuple(q),tuple(ee)); assert g.gauss(state)
    return state

def serial_state(s):
    return {'q':s[0],'E':s[1]}

def main():
    started=time.time()
    hashes={p:sha(SCI/p) for p in SOURCES}
    for p,expected in SOURCES.items():
        if expected: assert hashes[p]==expected,(p,hashes[p])
    mixed=Graph(7,(0,2,4),[(0,1),(0,3),(1,2),(2,3),(2,5),(4,5),(4,6)])
    cases=0; drop_z_detect=0; ungated_detect=0; cancellation_count=0
    for aq in product((-1,1),repeat=3):
        for bq in product((-1,0,1),repeat=4):
            q=[0]*7
            for a,x in zip(mixed.aa,aq): q[a]=x
            for b,x in zip((1,3,5,6),bq): q[b]=x
            if sum(q)!=3: continue
            for flux in (-2,0,3):
                state=path_field(mixed,q,(flux,)); v={state:Q(1)}
                h4,zz,aca=mixed.H4(v)
                pair=mixed.pair(v)
                assert h4==pair,(state,h4,pair)
                assert mixed.M(v)==mixed.comp(v)
                if h4!=add((1,h4),(Q(1,2),zz)): drop_z_detect+=1
                hu,_,_=mixed.H4(v,gated=False)
                assert not hu,('ungated cancellation failed',state,hu)
                if hu!=h4: ungated_detect+=1
                if aca: cancellation_count+=1
                e2,dd=mixed.electric(state)
                assert 0<=dd<=2*e2
                cases+=1
    assert drop_z_detect and ungated_detect and cancellation_count
    print(json.dumps({'mixed_graph_exact_cases':cases,'drop_ZdagZ_detected':drop_z_detect,'ungated_compensation_detected':ungated_detect,'nonzero_distant_pair_cancellation_cases':cancellation_count},sort_keys=True))
    cube=Graph(8,(0,3,5,6),[(u,v) for u in range(8) for v in range(u+1,8) if (u^v) in (1,2,4)])
    rows=[]
    for n in (-3,-1,0,1,2,4):
        q=tuple(1 if x in cube.aa else 0 for x in range(8)); ee=[0]*12
        for edge,sg in (((0,1),1),((1,3),1),((2,3),-1),((0,2),-1)):
            ee[cube.idx[edge]]=sg*n
        state=(q,tuple(ee)); assert cube.gauss(state)
        assert cube.electric(state)==(4*n*n,4*n*n)
        first=cube.marked_paths(state,0,1,1)
        assert len(first)==2 and sum(x[1] for x in first)==2
        outputs=[]
        for s,w,d in first:
            for f,z,d2 in cube.marked_paths(s,6,7,1): outputs.append((f,w*z,d,d2))
        assert len(outputs)==2 and len({x[0] for x in outputs})==2
        bydest={x[2]:x for x in outputs}
        alpha=bydest[2][0]; beta=bydest[4][0]
        assert alpha[0]==beta[0]==(1,-1,1,1,1,1,1,-1)
        ea,da=cube.electric(alpha); eb,db=cube.electric(beta)
        assert (ea,eb,da,db)==(4*n*n+4*n+4,4*n*n+2*n+4,0,0)
        assert not cube.H4({alpha:Q(1)})[0] and not cube.H4({beta:Q(1)})[0]
        diff=tuple(x-y for x,y in zip(alpha[1],beta[1]))
        expected=[0]*12
        for edge,z in (((0,2),-1),((0,4),1),((2,6),-1),((4,6),1)): expected[cube.idx[edge]]=z
        assert diff==tuple(expected)
        spin=max(abs(n)+2,3); cc=spin*(spin+1); rr=1-Q(n*(n+1),cc)
        spin_paths=[]
        for s,w,d in cube.marked_paths(state,0,1,1,spin):
            for f,z,d2 in cube.marked_paths(s,6,7,1,spin): spin_paths.append((d,w*z))
        assert dict(spin_paths)=={2:rr*rr,4:rr}
        row={'n':n,'alpha':serial_state(alpha),'beta':serial_state(beta),'energies':[ea,eb],'gap':ea-eb,'rotor_composition_norm2':2,'spin':spin,'r':str(rr),'spin_branch_norms2':{str(d):str(w) for d,w in spin_paths},'spin_composition_norm2':str(rr*rr+rr)}
        rows.append(row); print(json.dumps(row,sort_keys=True))
    assert sha(Path(__file__))
    assert hashes=={p:sha(SCI/p) for p in SOURCES},'source moved during control'
    result={'status':'exact finite controls complete; general proof is in PRE_REPORT.md','edges':cube.edges,'mixed_graph':{'vertices':7,'A':mixed.aa,'edges':mixed.edges,'cases':cases,'drop_ZdagZ_detected':drop_z_detect,'ungated_compensation_detected':ungated_detect,'nonzero_distant_pair_cancellation_cases':cancellation_count},'cube_rows':rows,'sources_sha256':hashes,'runner_sha256':sha(Path(__file__)),'python':sys.version,'platform':platform.platform(),'elapsed_seconds':time.time()-started}
    (OUT/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('CONTROL COMPLETE: no assertion failures; finite exact controls do not replace the analytic limit proof.')

if __name__=='__main__': main()
