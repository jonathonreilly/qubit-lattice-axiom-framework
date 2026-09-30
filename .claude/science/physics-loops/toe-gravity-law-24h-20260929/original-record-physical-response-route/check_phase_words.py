#!/usr/bin/env python3
"""Actual rotor birth words; no imported action builder or dense carrier."""
from collections import Counter
from pathlib import Path
import datetime, hashlib, json, os, resource, signal, time

HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
guard(); resource.setrlimit(resource.RLIMIT_CPU,(10,10)); signal.alarm(60)
start_cpu=time.process_time(); start_wall=time.monotonic(); L=12
def ref(x): return 1-sum(x)%2
def pack(q,e):
    return tuple(sorted((x,v) for x,v in q.items() if v!=ref(x))),tuple(sorted((x,v) for x,v in e.items() if v))
def qval(w,x): return dict(w[0]).get(x,ref(x))
def neighbors(x):
    return [tuple((x[i]+(s if i==d else 0))%L for i in range(3)) for d in range(3) for s in (-1,1)]
def edelta(a,b,v):
    for d in range(3):
        if all(a[i]==b[i] for i in range(3) if i!=d):
            if (a[d]+1)%L==b[d]: return (a,d),v
            if (b[d]+1)%L==a[d]: return (b,d),-v
    raise AssertionError('not an edge')
def change(w,qs,a,b,v):
    q,e=map(dict,w);q.update(qs);k,d=edelta(a,b,v);e[k]=e.get(k,0)+d
    out=pack(q,e);gauss(out);return out
def gauss(w):
    div=Counter()
    for (x,d),v in w[1]:
        y=tuple((x[i]+(1 if i==d else 0))%L for i in range(3))
        div[x]+=v;div[y]-=v
    assert {x:v for x,v in div.items() if v}=={x:v-ref(x) for x,v in w[0]}
def F_path(w,a,b):
    q=qval(w,a);assert q and qval(w,b)==0
    return change(w,{a:0,b:q},a,b,-q)
def j_path(w,a,b,s=1):
    assert qval(w,a)==qval(w,b)==0
    return change(w,{a:s,b:-s},a,b,s)
def rotor_G(w):
    return 2*sum(qval(w,b)==0 for a,v in w[0] if ref(a)==1 and v==0 for b in neighbors(a))
def birth(w,a,mark,helper):
    mid=F_path(w,a,helper);phase=rotor_G(mid)
    out=j_path(mid,a,mark)
    assert rotor_G(w)==rotor_G(out)==0
    return out,phase,[w,mid,out]
omega=pack({},{});a=(0,0,0);c=(2,0,0);shared=(1,0,0)
# A square of actual legal original-plus births from bare Omega. The same
# final physical word is reached in opposite original-mark orders.
ea=(a,(0,1,0),(0,11,0));ec=(c,shared,(3,0,0))
w1,p1,path1=birth(omega,*ea);wa,p2,path2=birth(w1,*ec)
w2,q1,path3=birth(omega,*ec);wb,q2,path4=birth(w2,*ea)
assert wa==wb
assert (p1,p2,q1,q2)==(10,10,10,8)

# The SAME original-plus mark sequence, two coherent physical W0 inputs,
# and a common final word. This is a channel fixture, not an Omega claim.
ba=(0,1,0);bc=(2,1,0);x=(3,0,0);y=(11,0,0);z=(4,3,0);neg=(4,4,0)
qfinal={neg:-1,x:1,y:1,shared:1,z:1,ba:-1,bc:-1}
charge={u:v-ref(u) for u,v in qfinal.items() if v!=ref(u)}
assert sum(charge.values())==0
efinal=Counter()
for u,r in charge.items():
    cur=list(a)
    for d in range(3):
        while cur[d]!=u[d]:
            old=tuple(cur);cur[d]+=1;new=tuple(cur)
            edge,de=edelta(old,new,-r);efinal[edge]+=de
final=pack(qfinal,efinal);gauss(final)
def initial(occupied,events):
    qq={neg:-1,z:1,occupied:1};ee=dict(efinal)
    for aa,bb,hh in events:
        for end,v in ((hh,-1),(bb,1)):
            edge,de=edelta(aa,end,v);ee[edge]=ee.get(edge,0)-de
    w=pack(qq,ee);gauss(w);return w
events_alpha=((a,ba,y),(c,bc,shared))
events_beta=((a,ba,shared),(c,bc,x))
alpha=initial(x,events_alpha);beta=initial(y,events_beta)
assert alpha!=beta
def sequence(w,events):
    phases=[];paths=[]
    for event in events:
        w,p,path=birth(w,*event);phases.append(p);paths.extend(path)
    return w,phases,paths
fa,pa,paths_a=sequence(alpha,events_alpha)
fb,pb,paths_b=sequence(beta,events_beta)
assert fa==fb==final and pa==[10,8] and pb==[8,8]
# The rotor two-jump amplitude on (alpha+i beta)/sqrt2 is
# (exp(18i lambda)+i exp(16i lambda))/sqrt2. Its selected final
# probability is 1+sin(2 lambda), with derivative +2 at zero.
assert sum(pa)-sum(pb)==2
allpaths=path1+path2+path3+path4+paths_a+paths_b
maxfield=max(abs(v) for w in allpaths for _,v in w[1])
spin=maxfield+2;casimir=spin*(spin+1);minweight=casimir
for path in (path1,path2,path3,path4):
    for old,new in zip(path,path[1:]):
        oe,ne=map(dict,(old[1],new[1]));changed=[e for e in oe.keys()|ne.keys() if oe.get(e,0)!=ne.get(e,0)]
        assert len(changed)==1
        e=changed[0];m=oe.get(e,0);de=ne.get(e,0)-m
        assert m==0 and abs(de)==1 # Omega square is exact at every S>=1.
for path in (paths_a[:3],paths_a[3:],paths_b[:3],paths_b[3:]):
    for old,new in zip(path,path[1:]):
        oe,ne=map(dict,(old[1],new[1]));changed=[e for e in oe.keys()|ne.keys() if oe.get(e,0)!=ne.get(e,0)]
        assert len(changed)==1
        e=changed[0];m=oe.get(e,0);de=ne.get(e,0)-m
        num=casimir-m*(m+de);assert num>0;minweight=min(minweight,num)
guard();rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;assert rss<100*1024*1024
result={'status':'all selected physical word identities passed',
 'L':L,'omega_square':{'phases_ab':[p1,p2],'phases_ba':[q1,q2],
 'circulation':p1+p2-q1-q2,'equal_final_word':True,
 'scope':'exact for rotor and every spin S>=1; no output-distinguishability claim from this square alone'},
 'same_original_history':{'original_marks':[[a,ba,1],[c,bc,1]],
 'phases_alpha':pa,'phases_beta':pb,'equal_final_word':True,
 'rotor_selected_probability_derivative':2,
 'scope':'un-normalized two-jump channel on supplied imaginary-coherent physical input; not an actual Omega preparation claim',
 'alpha':alpha,'beta':beta,'final':final},
 'finite_spin_path_positivity':{'S':spin,'max_abs_field':maxfield,'minimum_squared_edge_weight':[minweight,casimir],
 'scope':'nonzero paths only; rotor phase coefficient is not substituted for a finite-spin coefficient'},
 'cpu_seconds':time.process_time()-start_cpu,'wall_seconds':time.monotonic()-start_wall,
 'peak_rss_bytes':rss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'threads':{k:os.environ.get(k) for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
 'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(HERE/'PHASE_WORD_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='same_original_history'},indent=2))
