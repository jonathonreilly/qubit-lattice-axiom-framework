from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
P=json.loads((HERE/'SELECTED_INPUT.json').read_text())
L,Q,nold,M=(P[k] for k in ('L_b','Q','n_old','M'))
f=list(map(F,P['f'])); q=F(P['q']); r=F(P['r']); h=F(P['h_d'])
X=max(nold-1,Q)+2; Y=1-L; side=M//4
checks=[]
def verify(name,condition):
    checks.append({'name':name,'value':bool(condition)})
    if not condition:
        raise AssertionError(name)

def walk(points):
    out=[tuple(points[0])]
    for end in points[1:]:
        cur=out[-1]
        axes=[k for k in range(3) if cur[k]!=end[k]]
        if len(axes)!=1:
            raise ValueError(('nonstraight or empty segment',cur,end))
        axis=axes[0]; step=1 if end[axis]>cur[axis] else -1
        while cur[axis]!=end[axis]:
            nxt=list(cur); nxt[axis]+=step; cur=tuple(nxt); out.append(cur)
    return out

def cycle(z):
    return walk([(X,Y,z),(X+side,Y,z),(X+side,Y+side,z),
                 (X,Y+side,z),(X,Y,z)])[:-1]

C={'v0':(0,1,1),'v1':(-1,0,0),
   'a0':(-1,1,0),'b0':(0,1,0),'a0p':(-1,0,1),'b0p':(0,0,1),
   'a1':(-1,-1,0),'b1':(0,-1,0),'a1p':(-1,0,-1),'b1p':(0,0,-1)}
C.update({f'v{j}':(0,1-j,-1) for j in range(2,L+1)})
E={'v0':((0,2,1),1),'v1':((-2,0,0),-1),
   'a0':((-2,1,0),-1),'b0':((1,1,0),1),
   'a0p':((-2,0,1),-1),'b0p':((1,0,1),1),
   'a1':((-2,-1,0),-1),'b1':((1,-1,0),1),
   'a1p':((-2,0,-1),-1),'b1p':((1,0,-1),1)}
E.update({f'v{j}':((1,1-j,-1),1) for j in range(2,L+1)})
old={f'q{j}':(j,0,0) for j in range(nold)}
old.update({f'C:{name}':pos for name,pos in C.items()})
for name,(pos,direction) in E.items():
    for k in range(Q):
        old[f'A:{name}:{k}']=(pos[0]+k*direction,pos[1],pos[2])
clock=cycle(3)
old.update({f'X:{j}':pos for j,pos in enumerate(clock)})
verify('original coordinate lists are disjoint',len(set(old.values()))==len(old))
verify('original clock count',len(clock)==M)

pplus=walk([(0,2,2),(0,2,4),(0,Y-6,4),(X,Y-6,4),(X,Y,4)])
pminus=walk([(-1,2,1),(-2,2,1),(-2,2,-2),(-2,Y-2,-2),
             (X,Y-2,-2),(X,Y-2,2),(X,Y,2)])
ell=X+16-Y
verify('matched tail lengths',len(pplus)==len(pminus)==ell+1)
plus=cycle(4)+list(reversed(pplus[:-1]))+[(0,1,2)]
minus=cycle(2)+list(reversed(pminus[:-1]))+[(-1,1,1)]
m=M+ell+1; b=m-2; a=m-1
verify('matched vertex counts',len(plus)==len(minus)==m)
verify('individual graph injectivity',len(set(plus))==len(set(minus))==m)
verify('two graph copies disjoint',not(set(plus)&set(minus)))
verify('all auxiliary sites fresh',not((set(plus)|set(minus))&set(old.values())))
edges=[(j,(j+1)%M) for j in range(M)]+[(0,M)]
edges += [(j,j+1) for j in range(M,b)]
edges += [(b,a)]
verify('edge count',len(edges)==m)
def dist(u,v):
    return sum(abs(u[k]-v[k]) for k in range(3))
for name,coords in [('plus',plus),('minus',minus)]:
    verify(name+' ordinary NN graph edges',all(dist(coords[u],coords[v])==1 for u,v in edges))
    verify(name+' all clock sources NN',all(dist(coords[j],clock[j])==1 for j in range(M)))
    verify(name+' data source NN',dist(coords[a],C['v0'])==1)
    verify(name+' data detuning NN',dist(coords[b],E['v0'][0])==1)
deg=[0]*m
for u,v in edges:
    deg[u]+=1;deg[v]+=1
external=set(range(M))|{a,b}
verify('abstract max degree three',max(deg)==3)
verify('auxiliary degree including ports at most four',max(deg[j]+(j in external) for j in range(m))<=4)

B=[[F(int(i==j)) for j in range(m)] for i in range(m)]
for i,j in edges:
    B[i][j]-=r;B[j][i]-=r
Bp=[row[:] for row in B];Bm=[row[:] for row in B]
Bp[b][b]+=h;Bm[b][b]-=h

def inv(matrix):
    n=len(matrix)
    aug=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if aug[i][k])
        aug[k],aug[pivot]=aug[pivot],aug[k]
        den=aug[k][k];aug[k]=[x/den for x in aug[k]]
        for i in range(n):
            if i!=k and aug[i][k]:
                mult=aug[i][k]
                aug[i]=[x-mult*y for x,y in zip(aug[i],aug[k])]
    return [row[n:] for row in aug]

G0=inv(B);Gp=inv(Bp);Gm=inv(Bm)
u=[G0[j][b] for j in range(m)];z=G0[b][b]
verify('positive connected Green entries',all(x>0 for row in G0 for x in row))
verify('strict rank-one denominator',1-h*h*z*z>0)
verify('direct plus inverse matches rank-one formula',all(Gp[i][j]==G0[i][j]-h*u[i]*u[j]/(1+h*z) for i in range(m) for j in range(m)))
verify('direct minus inverse matches rank-one formula',all(Gm[i][j]==G0[i][j]+h*u[i]*u[j]/(1-h*z) for i in range(m) for j in range(m)))
# Amplitudes use the candidate G0 formula; the response below uses independently inverted Gp,Gm.
delta=[-2*h*u[j]*u[a]/(1-h*h*z*z) for j in range(M)]
t=[-f[j]/(2*q*delta[j]) for j in range(M)]
alpha=[2*G0[j][j]+2*h*h*z*u[j]*u[j]/(1-h*h*z*z) for j in range(M)]
beta=2*G0[a][a]+2*h*h*z*u[a]*u[a]/(1-h*h*z*z)
s=[t[j]*t[j]*alpha[j] for j in range(M)];s0=q*q*beta
verify('all delta_j strictly negative',all(x<0 for x in delta))

def quadratic(v,G):
    indices=[i for i,x in enumerate(v) if x]
    return sum((v[i]*G[i][j]*v[j] for i in indices for j in indices),F(0))

def response(occupied,pc,pe,both=True):
    vp=[F(0)]*m;vm=[F(0)]*m
    for j in occupied:
        vp[j]=vm[j]=t[j]
    vp[a]=q*pc;vm[a]=-q*pc
    Gplus,Gminus=(Gp,Gm) if pe==1 else (Gm,Gp)
    return quadratic(vp,Gplus)+(quadratic(vm,Gminus) if both else 0)

responses=[]
for j in range(M):
    for pc in [-1,1]:
        for pe in [-1,1]:
            actual=response([j],pc,pe)
            expected=s0+s[j]-f[j]*pc*pe
            verify(f'one-clock exact response j={j},Pc={pc},Pe={pe}',actual==expected)
            responses.append({'occupied':[j],'Pc':pc,'Pe':pe,'C':str(actual)})
for pc in [-1,1]:
    for pe in [-1,1]:
        verify(f'zero-clock response Pc={pc},Pe={pe}',response([],pc,pe)==s0)
extra=2*t[0]*t[1]*(Gp[0][1]+Gm[0][1])
verify('two-clock cross term actually nonzero',extra!=0)
for pc in [-1,1]:
    for pe in [-1,1]:
        actual=response([0,1],pc,pe)
        expected=s0+s[0]+s[1]-(f[0]+f[1])*pc*pe+extra
        verify(f'two-clock exact extra term Pc={pc},Pe={pe}',actual==expected)

pc_single=sum((F(pc)*response([0],pc,pe) for pc in [-1,1] for pe in [-1,1]),F(0))/4
pe_single=sum((F(pe)*response([0],pc,pe) for pc in [-1,1] for pe in [-1,1]),F(0))/4
pair=sum((F(pc*pe)*response([0],pc,pe) for pc in [-1,1] for pe in [-1,1]),F(0))/4
pc_one_mirror=sum((F(pc)*response([0],pc,pe,both=False) for pc in [-1,1] for pe in [-1,1]),F(0))/4
verify('full mirror cancels single Pc term',pc_single==0)
verify('full mirror cancels single Pe term',pe_single==0)
verify('full mirror yields prescribed pair term',pair==-f[0])
verify('one-mirror mutation has unwanted Pc term',pc_one_mirror!=0)
verify('clock counterterms are nonzero and nonconstant',max(s)>min(s)==0)
# Literal saturation witness is a geometry check, not a general no-go.
v1=C['v1'];old_set=set(old.values())
neighbors=[]
for axis in range(3):
    for sign in [-1,1]:
        p=list(v1);p[axis]+=sign;neighbors.append(tuple(p))
verify('v1 has six original occupied neighbors',all(p in old_set for p in neighbors))

out={'status':'exact_selected_fixture_completed','checks':checks,
     'scope':'One-particle contractions and finite NN geometry only; no full auxiliary dynamics or independent audit.',
     'counts':{'original_qubits':len(old),'M':M,'vertices_per_copy':m,'tail_length':ell,'fresh_auxiliaries':2*m,'edges_per_copy':len(edges)},
     'source_parameters':P,'original_coordinates':old,'plus_coordinates':plus,'minus_coordinates':minus,'abstract_edges':edges,
     'constants':{'delta':list(map(str,delta)),'t':list(map(str,t)),'alpha':list(map(str,alpha)),'beta':str(beta),'s':list(map(str,s)),'s0':str(s0)},
     'one_clock_responses':responses,'two_clock_extra':str(extra),'omitted_mirror_Pc_coefficient':str(pc_one_mirror),
     'v1_occupied_neighbors':neighbors}
(HERE/'SELECTED_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'all_checks':all(c['value'] for c in checks),'counts':out['counts'],'full_auxiliary_dynamics_checked':False,'independent_audit':False},indent=2))
