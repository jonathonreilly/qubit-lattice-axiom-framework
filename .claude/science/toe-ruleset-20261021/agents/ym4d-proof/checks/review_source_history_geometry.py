"""Independent centered-coordinate S4 geometry; no author imports."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product, permutations
import json, time

started = time.monotonic()
checks = {}
controls = {}
details = {}

def require(name, predicate):
    checks[name] = bool(predicate)
    assert predicate, name

def control(name, detects):
    controls[name] = bool(detects)
    assert detects, name

def move(x, mu, n=1):
    y = list(x); y[mu] += n
    return tuple(y)

def plus(x, y):
    return tuple(a+b for a,b in zip(x,y))

def edge(x, mu, sign, period):
    base = x if sign == 1 else move(x,mu,-1)
    return (tuple(a % period for a in base),mu,sign)

def walk(x, steps, period):
    out=[]
    for mu,sign in steps:
        out.append(edge(x,mu,sign,period)); x=move(x,mu,sign)
    return out

def inverse(word):
    return [(x,mu,-s) for x,mu,s in reversed(word)]

def axial_steps(y, order):
    return [(mu,1 if y[mu]>0 else -1) for mu in order for _ in range(abs(y[mu]))]

def contour(center, y, mu, order, L, T):
    period=L*T
    steps=axial_steps(y,order)
    a=walk(center,steps,period)
    b=walk(plus(center,y),[(mu,1)]*L,period)
    c=walk(move(center,mu,L),steps,period)
    return a+b+inverse(c)

def block(x,L,T):
    r=(L-1)//2
    return tuple(((a+r)//L)%T for a in x)

def endpoint(e,period):
    x,mu,s=e
    return tuple(a%period for a in move(x,mu))

def vertices(word,period):
    return {v for e in word for v in (e[0],endpoint(e,period))}

def interior_links(L,T):
    r=(L-1)//2; period=L*T
    return {(tuple(a%period for a in x),mu) for x in product(range(-r,r+1),repeat=4)
            for mu in range(4) if x[mu]<r}

def incident_plaquettes(key,period):
    x,mu=key
    ans=set()
    for nu in range(4):
        if mu==nu: continue
        for base in (x,move(x,nu,-1)):
            ans.add((tuple(a%period for a in base),min(mu,nu),max(mu,nu)))
    return ans

def plaquette_vertices(p,period):
    x,mu,nu=p
    return {tuple(a%period for a in y) for y in (x,move(x,mu),move(x,nu),move(move(x,mu),nu))}

def qmul(a,b):
    w,x,y,z=a; v,i,j,k=b
    return (w*v-x*i-y*j-z*k,w*i+x*v+y*k-z*j,w*j-x*k+y*v+z*i,w*k+x*j-y*i+z*v)

def qinv(q): return (q[0],-q[1],-q[2],-q[3])
ONE=(1,0,0,0)
Q8=[ONE,(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)]

def field(key):
    x,mu=key
    return Q8[(sum((i+2)*a*a+(3*i+1)*a for i,a in enumerate(x))+3*mu+mu*sum(x))%8]

def gauge(x):
    return Q8[(sum((i+1)*a*a+2*a for i,a in enumerate(x))+1)%8]

def hol(word,period,transformed=False,broken=False):
    q=ONE
    for x,mu,s in word:
        v=field((x,mu))
        if transformed:
            g0=gauge(x); g1=gauge(tuple(a%period for a in move(x,mu)))
            v=qmul(g0,v) if broken else qmul(qmul(g0,v),qinv(g1))
        q=qmul(q,v if s==1 else qinv(v))
    return q

for L,T in [(3,2),(3,3),(5,2),(5,3),(7,2)]:
    period=L*T; r=(L-1)//2; zero=(0,)*4
    nl=4*L**3*(L-1); IP=interior_links(L,T)
    PP=set().union(*(incident_plaquettes(e,period) for e in IP))
    require(f'L{L}T{T}_interior_link_count',len(IP)==nl)
    require(f'L{L}T{T}_plaquette_incidence',len(PP)<=6*nl and all(len(incident_plaquettes(e,period))==6 for e in IP))
    require(f'L{L}T{T}_plaquette_support',all(max(min(b,T-b) for b in block(v,L,T))<=1 for p in PP for v in plaquette_vertices(p,period)))
    maxword=0; maxribbon=0; support_ok=True; ribbon_ok=True
    means={}; read_by=defaultdict(set)
    for mu in range(4):
        for side in [0,-1]:
            center=move(zero,mu,L*side)
            endpoints={block(center,L,T),block(move(center,mu,L),L,T)}
            net=Counter(); count=0
            for y in product(range(-r,r+1),repeat=4):
                for order in permutations(range(4)):
                    word=contour(center,y,mu,order,L,T)
                    maxword=max(maxword,len(word)); count+=1
                    bs={block(v,L,T) for v in vertices(word,period)}
                    support_ok &= bs<=endpoints
                    for x,axis,s in word: read_by[(x,axis)].add((side,mu))
                    target=(zero,0)
                    net[sum(s for x,axis,s in word if (x,axis)==target)]+=1
                    z=center; area=0
                    for axis,sgn in axial_steps(y,order):
                        if axis!=mu:
                            area+=L
                            for j in range(L):
                                q=move(z,mu,j)
                                vs=(q,move(q,axis,sgn),move(q,mu),move(move(q,axis,sgn),mu))
                                ribbon_ok &= {block(v,L,T) for v in vs}<=endpoints
                        z=move(z,axis,sgn)
                    maxribbon=max(maxribbon,area)
            means[(side,mu)]=net
            require(f'L{L}T{T}_single_link_exponents_{side}_{mu}',set(net)<={0,1,-1})
    require(f'L{L}T{T}_endpoint_block_support',support_ok)
    require(f'L{L}T{T}_contour_length',maxword<=5*L-4)
    require(f'L{L}T{T}_exact_ribbon_area',ribbon_ok and maxribbon==3*L*(L-1)//2)
    require(f'L{L}T{T}_kernel_incidence',max(map(len,read_by.values()))<=8 and all(len(cs)<=1 for (x,mu),cs in read_by.items() if block(x,L,T)!=block(move(x,mu),L,T)))
    details[f'L{L}T{T}']={'internal_links':len(IP),'touched_plaquettes':len(PP),'max_word_length':maxword,'max_ribbon_area':maxribbon,'max_kernel_reads':max(map(len,read_by.values()))}
    if L==3:
        coeff={f'{side},{mu}':F(sum(v for k,v in h.items() if k!=0),24*L**4) for (side,mu),h in means.items()}
        want={f'{side},{mu}':(F(4,27) if mu==0 and side==0 else F(1,9) if mu==0 else F(10,81)) for mu in range(4) for side in [0,-1]}
        require(f'T{T}_frustrated_word_fractions',coeff==want)
        require(f'T{T}_frustrated_word_signs',all(set(h)<={0,(1 if side==0 else -1)} for (side,mu),h in means.items()))
        require(f'T{T}_frustrated_sum',sum(coeff.values())==1)
        details[f'L{L}T{T}']['single_link_fractions']={k:str(v) for k,v in coeff.items()}
        control(f'T{T}_single_straight_path_mutation',coeff['0,0']!=1)
        rough=((1,3,3,3),0)
        require(f'T{T}_rough_link_not_read',rough not in read_by)
        rough_ps=incident_plaquettes(rough,period)
        require(f'T{T}_rough_never_interior_plaquette',all(len({block(v,L,T) for v in plaquette_vertices(p,period)})>1 for p in rough_ps))
        require(f'T{T}_rough_inside_collar',all(max(min(b,T-b) for b in block(v,L,T))<=1 for p in rough_ps for v in plaquette_vertices(p,period)))
        require(f'T{T}_rough_disjoint_integrated_Q',all(not any((v,mu) in IP for v in plaquette_vertices(p,period) for mu in range(4)) for p in rough_ps))
        badrough=((0,0,0,0),0)
        control(f'T{T}_interior_rough_substitution',badrough in IP and badrough in read_by)

# Independent noncommuting word test, including exact rectangular-plaquette tiling.
L=3;T=3;period=L*T;zero=(0,)*4; mu=1;y=(1,-1,1,-1);order=(2,0,3,1)
word=contour(zero,y,mu,order,L,T)
require('nonabelian_fixture',qmul(Q8[2],Q8[4])!=qmul(Q8[4],Q8[2]))
expected=qmul(qmul(gauge(zero),hol(word,period)),qinv(gauge(move(zero,mu,L))))
require('nonabelian_gauge_covariance',hol(word,period,True)==expected)
control('omit_right_gauge_factor',hol(word,period,True,True)!=expected)
loop=ONE; prefix=[]; z=zero; total_area=0
for axis,sgn in axial_steps(y,order):
    leg_before=walk(z,[(mu,1)]*L,period); nxt=move(z,axis,sgn)
    rectangle=walk(z,[(axis,sgn)],period)+walk(nxt,[(mu,1)]*L,period)+inverse(walk(move(z,mu,L),[(axis,sgn)],period))+inverse(leg_before)
    R=hol(rectangle,period)
    if axis==mu: require('parallel_ribbon_degenerate',R==ONE)
    else:
        tiled=ONE
        for j in range(L):
            base=move(z,mu,j); wp=walk(base,[(axis,sgn),(mu,1),(axis,-sgn),(mu,-1)],period)
            trans=hol(walk(z,[(mu,1)]*j,period),period)
            tiled=qmul(tiled,qmul(qmul(trans,hol(wp,period)),qinv(trans)))
        require(f'noncommuting_ribbon_tile_{axis}',tiled==R);total_area+=L
    pref=hol(prefix,period)
    loop=qmul(qmul(qmul(pref,R),qinv(pref)),loop)
    prefix+=walk(z,[(axis,sgn)],period);z=nxt
require('noncommuting_full_ribbon_identity',loop==qmul(hol(word,period),qinv(hol(walk(zero,[(mu,1)]*L,period),period))))
require('maximal_ribbon_attained',total_area==9)

# Actual periodic collars: overlap relation and connectedness.
def collar(root,T): return {tuple((a+b)%T for a,b in zip(root,shift)) for shift in product([-1,0,1],repeat=4)}
def supdist(a,b,T): return max(min((x-y)%T,(y-x)%T) for x,y in zip(a,b))
for T in [2,3,6,7]:
    c0=collar(zero,T)
    require(f'T{T}_full_collar_compatibility',all(bool(c0&collar(x,T))==(supdist(zero,x,T)<=2) for x in product(range(T),repeat=4)))
control('star_separation_insufficient',bool(collar(zero,7)&collar((2,0,0,0),7)))

print(json.dumps({'schema':'independent-source-history-geometry-v1','checks':checks,'negative_controls':controls,'details':details,'elapsed_seconds':time.monotonic()-started},indent=2))
