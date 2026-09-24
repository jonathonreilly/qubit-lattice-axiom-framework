"""Cubic geometry and divergence only; extracted from the frozen source helper."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/local_gauge_record_cooling_check.py',)
import itertools

def geometry(shape,periodic):
    ndim=len(shape);vertices=list(itertools.product(*[range(n) for n in shape]))
    vset=set(vertices)
    def shift(v,a):
        q=list(v);q[a]+=1
        if periodic:q[a]%=shape[a]
        q=tuple(q)
        return q if q in vset else None
    edges=[]
    for v in vertices:
        for a in range(ndim):
            w=shift(v,a)
            if w is not None:edges.append((v,a,w))
    ei={(v,a):j for j,(v,a,w) in enumerate(edges)}
    faces=[]
    for v in vertices:
        for a,b in itertools.combinations(range(ndim),2):
            va=shift(v,a);vb=shift(v,b)
            if va is None or vb is None:continue
            if (va,b) not in ei or (vb,a) not in ei:continue
            raised=(ei[(v,a)],ei[(va,b)])
            lowered=(ei[(vb,a)],ei[(v,b)])
            assert len(set(raised+lowered))==4
            faces.append({'origin':v,'axes':(a,b),'raised':raised,'lowered':lowered,
                          'r':sum(1<<e for e in raised),'l':sum(1<<e for e in lowered)})
    return vertices,edges,faces


def gauss(c,vertices,edges):
    values={v:0 for v in vertices}
    for j,(v,a,w) in enumerate(edges):
        e=2*((c>>j)&1)-1;values[v]+=e;values[w]-=e
    return tuple(values[v] for v in vertices)
