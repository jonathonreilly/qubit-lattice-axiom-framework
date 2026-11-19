# Guide only (S8): minimum of sum_e w_e |n_a - R_e n_b|^2 over unit imaginary n on the 3x3 tile.
import math, random
A=[[1,0,0],[0,0,-1],[0,1,0]]   # quarter turn about i, basis (i,j,k)
B=[[0,0,1],[0,1,0],[-1,0,0]]   # quarter turn about j
Id=[[1,0,0],[0,1,0],[0,0,1]]
def mv(M,v): return [sum(M[r][c]*v[c] for c in range(3)) for r in range(3)]
def mtv(M,v): return [sum(M[c][r]*v[c] for c in range(3)) for r in range(3)]
sites=[(x,y) for x in range(3) for y in range(3)]; idx={s:i for i,s in enumerate(sites)}
edges=[]
for x in range(2):
    for y in range(3):
        R=Id
        if y==2 and x==0: R=A
        if y==2 and x==1: R=B
        edges.append((idx[(x,y)],idx[(x+1,y)],0.5 if y in (0,2) else 1.0,R))
for x in range(3):
    for y in range(2):
        edges.append((idx[(x,y)],idx[(x,y+1)],0.5 if x in (0,2) else 1.0,Id))
assert len(edges)==12
def energy(n):
    e=0.0
    for a,b,w,R in edges:
        d=[n[a][i]-v for i,v in enumerate(mv(R,n[b]))]; e+=w*sum(x*x for x in d)
    return e
def grad(n):
    g=[[0.0]*3 for _ in range(9)]
    for a,b,w,R in edges:
        Rb=mv(R,n[b]); d=[n[a][i]-Rb[i] for i in range(3)]
        for i in range(3): g[a][i]+=2*w*d[i]
        RTd=mtv(R,d)
        for i in range(3): g[b][i]-=2*w*RTd[i]
    return g
def norm(v): l=math.sqrt(sum(x*x for x in v)); return [x/l for x in v]
rnd=random.Random(7); best=1e9
for start in range(300):
    n=[norm([rnd.gauss(0,1) for _ in range(3)]) for _ in range(9)]
    step=0.05
    for it in range(3000):
        g=grad(n)
        n=[norm([n[s][i]-step*g[s][i] for i in range(3)]) for s in range(9)]
    e=energy(n); best=min(best,e)
print("min over unit imaginary velocities on the tile (300 starts): %.6f   claimed lower bound 1/8 = 0.125"%best)
