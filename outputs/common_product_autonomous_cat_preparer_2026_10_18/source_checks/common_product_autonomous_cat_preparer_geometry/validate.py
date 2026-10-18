import json
from collections import deque
from pathlib import Path

outdir=Path(__file__).resolve().parent
heads={}; targets={}; edges=[]; ports={}; escapes={}
def put(table,name,p):
    assert p not in heads.values() and p not in targets.values(), (name,p)
    table[name]=p
def edge(a,b,kind):
    assert sum(abs(x-y) for x,y in zip(a,b))==1,(a,b,kind)
    edges.append((a,b,kind))
def writer(label,shift,shared=False,target=False):
    def tr(p):
        x,y,z=p
        return (z,y,x) if shared else (x+shift,y,z)
    arm0=[(1,0,0),(2,0,0),(2,1,0),(1,1,0)]+[(1,y,0) for y in range(2,9)]
    arm1=[(-1,y,0) for y in range(9)]+[(-1,8,1),(0,8,1)]
    for a,arm in enumerate((arm0,arm1)):
        for n,p in enumerate(arm): put(heads,f'{label}.a{a}.{n}',tr(p))
        for p,q in zip(arm,arm[1:]):edge(tr(p),tr(q),'writer_arm')
    pin,pout=tr((0,8,0)),tr((1,8,1))
    put(heads,label+'.in',pin);put(heads,label+'.out',pout)
    ports[label+'.in']=pin;ports[label+'.out']=pout
    for p in (pin,pout):
        for q in (tr(arm0[-1]),tr(arm1[-1])):edge(p,q,'writer_junction')
    if target:
        r=tr((0,0,0));put(targets,label+'.target',r)
        for arm in (arm0,arm1):edge(tr(arm[0]),r,'record_contact')
    escapes[label+'.in']=[tr((0,y,0)) for y in range(8,21)]
    escapes[label+'.out']=([pout] if shared else [tr((x,8,1)) for x in range(1,21)])

writer('w11',0,True,True)
for label,shift,target in [('w10',100,False),('w20',200,False),('w21',300,True),('w30',400,False),('w31',500,True),('w40',600,False),('w41',700,True)]:
    writer(label,shift,False,target)

core={'I0':(-1,-1,0),'O0':(1,-1,0),'I1':(1,1,0),'O1':(-1,1,0)}
for name,p in core.items():
    put(heads,'core.'+name,p);ports['core.'+name]=p;escapes['core.'+name]=[p]
for n,(a,b) in enumerate([('I0','O0'),('O0','I1'),('I1','O1'),('O1','I0')]):
    p=core[a];q=core[b];m=tuple((x+y)//2 for x,y in zip(p,q))
    put(heads,f'core.m{n}',m);edge(p,m,'core_hop');edge(m,q,'core_hop');edge(m,(0,0,0),'program_contact')
split={'I0':(1000,0,0),'I1':(1001,1,0),'O0':(1001,0,0),'O1':(1000,1,0)}
for name,p in split.items():
    put(heads,'split.'+name,p);ports['split.'+name]=p;escapes['split.'+name]=[p]
for a in ('I0','I1'):
    for b in ('O0','O1'):edge(split[a],split[b],'splitter')
assert len(heads)==204 and len(targets)==4

connections=[ [('split.O0','w10.in'),('split.O1','w11.in')],
 [('w10.out','w20.in'),('w11.out','w21.in')],
 [('w20.out','w30.in'),('w21.out','w31.in')],
 [('w30.out','w40.in'),('w31.out','w41.in')],
 [('w40.out','core.I0'),('w41.out','core.I1')] ]
external=['split.I0','split.I1','core.O0','core.O1']
posts={k:v[-1] for k,v in escapes.items()}
xy={p[:2] for p in posts.values()}
assert len(xy)==len(posts)

def planar(a,b):
    a=a[:2];b=b[:2];blocked=xy-{a,b}
    todo=deque([a]);pred={a:None}
    while todo:
        p=todo.popleft()
        if p==b:break
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            q=(p[0]+dx,p[1]+dy)
            if -20<=q[0]<=1030 and -20<=q[1]<=40 and q not in blocked and q not in pred:
                pred[q]=p;todo.append(q)
    assert b in pred
    path=[];p=b
    while p is not None:path.append(p);p=pred[p]
    return list(reversed(path))

def detour(path):
    occupied=set(path)|xy
    for i,(p,q) in enumerate(zip(path,path[1:])):
        dx=q[0]-p[0];dy=q[1]-p[1]
        for nx,ny in [(-dy,dx),(dy,-dx)]:
            r=(p[0]+nx,p[1]+ny);s=(q[0]+nx,q[1]+ny)
            if r not in occupied and s not in occupied:
                return path[:i+1]+[r,s]+path[i+1:]
    raise AssertionError('no detour')

routes=[];heights=set()
for gap,pair in enumerate(connections,1):
    pp=[planar(posts[a],posts[b]) for a,b in pair]
    def base(idx):
        a,b=pair[idx]
        return len(escapes[a])-1+len(escapes[b])-1-posts[a][2]-posts[b][2]+len(pp[idx])-1
    assert (base(0)-base(1))%2==0
    h0=10000*gap;h1=h0+(base(0)-base(1))//2
    while h1==h0 or h1 in heights:
        pp[1]=detour(pp[1]);h1=h0+(base(0)-base(1))//2
    assert h0 not in heights and min(h0,h1)>100
    heights.update((h0,h1))
    for idx,((a,b),h) in enumerate(zip(pair,(h0,h1))):
        pa,pb=posts[a],posts[b]
        path=list(escapes[a])
        path += [(pa[0],pa[1],z) for z in range(pa[2]+1,h+1)]
        path += [(x,y,h) for x,y in pp[idx][1:]]
        path += [(pb[0],pb[1],z) for z in range(h-1,pb[2]-1,-1)]
        path += list(reversed(escapes[b]))[1:]
        assert len(set(path))==len(path)
        routes.append(dict(gap=gap,branch=idx,start=a,end=b,height=h,edges=len(path)-1,path=path))
    assert routes[-1]['edges']==routes[-2]['edges']

occupied={p:name for name,p in heads.items()}|{p:name for name,p in targets.items()}
for route in routes:
    path=route['path']
    for p in path[1:-1]:
        assert p not in occupied,(route['start'],p,occupied.get(p))
        occupied[p]=f"cable{route['gap']}.{route['branch']}"
    for p,q in zip(path,path[1:]):edge(p,q,'cable')
for name in external:
    p=ports[name]
    # Infinite +z rays: every obstacle with this xy must lie at/below its origin.
    for q,owner in occupied.items():
        assert q[:2]!=p[:2] or q[2]<=p[2],(name,q,owner)
    edge(p,(p[0],p[1],p[2]+1),'external_first_edge')
assert {q for p,q,k in edges if k=='program_contact'}=={(0,0,0)}
a1_neighbors=set()
for p,q,k in edges:
    if p==(0,0,0):a1_neighbors.add(q)
    if q==(0,0,0):a1_neighbors.add(p)
assert a1_neighbors=={(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}
degree={}
for p,q,k in edges:
    degree.setdefault(p,set()).add(q);degree.setdefault(q,set()).add(p)
assert max(map(len,degree.values()))<=6
lengths=[r['edges'] for r in routes[::2]]
assert len(occupied)==198+2*sum(lengths)
for route in routes:
    path=route.pop('path')
    corners=[path[0]]
    previous=None
    for index,(p,q) in enumerate(zip(path,path[1:])):
        direction=tuple(y-x for x,y in zip(p,q))
        if previous is not None and direction!=previous:corners.append(p)
        previous=direction
    corners.append(path[-1])
    route['axis_aligned_corners']=corners
data=dict(module_heads=heads,targets=targets,ports=ports,external_positive_z_rays=external,
          cables=routes,module_and_external_first_edges=[e for e in edges if e[2]!='cable'],
          summary=dict(paired_lengths=lengths,sum_lengths=sum(lengths),phase_power=90+sum(lengths),
                       finite_qubits=198+2*sum(lengths),finite_blocks=304+2*sum(lengths),
                       maximum_installed_degree=max(map(len,degree.values())),
                       a1_neighbors=sorted(a1_neighbors),validation='all assertions passed'))
(outdir/'COORDINATES.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
(outdir/'RESULT.json').write_text(json.dumps(data['summary'],indent=2)+'\n')
print(json.dumps(data['summary'],indent=2))
