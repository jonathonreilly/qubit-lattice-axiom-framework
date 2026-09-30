"""Independent integer source-word and interior Krylov control; no author code."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from collections import defaultdict
from itertools import product
import hashlib,json,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
t0=time.process_time();here=Path(__file__).resolve().parent
dirs=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def base_charge(v):return 1 if sum(v)%2==0 else 0
class Preparation:
    def __init__(self,L=None):self.L=L;self.q={};self.E={};self.div=defaultdict(int);self.steps=0;self.births=0;self.unit=True
    def wrap(self,v):return tuple(x%self.L for x in v) if self.L else v
    def charge(self,v):return self.q.get(v,base_charge(v))
    def move(self,a,b,kind,sign=1):
        a=self.wrap(a);b=self.wrap(b);qa=self.charge(a);qb=self.charge(b)
        if kind=='out':assert qa and not qb;na,nb,step=0,qa,-qa
        elif kind=='in':assert not qa and qb;na,nb,step=qb,0,qb
        else:assert not qa and not qb;na,nb,step=sign,-sign,sign;self.births+=1
        m=self.E.get((a,b),0);self.unit &= (m*(m+step)==0)
        self.q[a]=na;self.q[b]=nb;self.E[a,b]=m+step
        self.div[a]+=step;self.div[b]-=step;self.steps+=1
        assert self.div[a]==na-base_charge(a) and self.div[b]==nb-base_charge(b)
    def birth_pair(self,a):
        self.move(a,add(a,(-1,0,0)),'out');self.move(a,add(a,(1,0,0)),'birth')
    def finish(self):
        self.move((-2,0,0),(-1,0,0),'out');self.move((2,0,0),(1,0,0),'out')
        assert self.unit
        allsites=set(self.q)|set(self.div)
        assert all(self.div[v]==self.charge(v)-base_charge(v) for v in allsites)
        holes=sorted(v for v,q in self.q.items() if base_charge(v) and not q)
        nb=sum(bool(q) for v,q in self.q.items() if not base_charge(v))
        assert len(holes)==2 and nb==2*self.births+2
        return {'births':self.births,'elementary_hops_and_births':self.steps,'A_holes':holes,'B_occupants':nb,'max_field':max(map(abs,self.E.values())),'all_selected_spin_weights_equal_one_for_every_S_ge_1':self.unit}

def relative_ops(prep):
    qbase=prep.q;Ebase=prep.E;wrap=prep.wrap
    def q0(v):return qbase.get(v,base_charge(v))
    def pack(q,E):return (tuple(sorted((v,x) for v,x in q.items() if x!=q0(v))),tuple(sorted((a,b,x) for (a,b),x in E.items() if x!=Ebase.get((a,b),0))))
    def unpack(key):return dict(key[0]),{(a,b):x for a,b,x in key[1]}
    def getq(q,v):return q.get(v,q0(v))
    def neighbors(v):return [wrap(add(v,d)) for d in dirs]
    baseholes={v for v,x in qbase.items() if base_charge(v) and not x}
    def holes(key):
        out=set(baseholes)
        for v,x in key[0]:
            if base_charge(v):
                if x:out.discard(v)
                else:out.add(v)
        return out
    def move(key,a,b,kind,sign=1):
        a=wrap(a);b=wrap(b);q,E=unpack(key);qa=getq(q,a);qb=getq(q,b)
        if kind=='in':
            if qa or not qb:return None
            q[a]=qb;q[b]=0;step=qb
        elif kind=='out':
            if not qa or qb:return None
            q[a]=0;q[b]=qa;step=-qa
        else:
            if qa or qb:return None
            q[a]=sign;q[b]=-sign;step=sign
        m=E.get((a,b),Ebase.get((a,b),0));E[a,b]=m+step
        return pack(q,E),m*(m+step)==0
    def gamma(key):
        q,_=unpack(key)
        return 2*sum(getq(q,b)==0 for a in holes(key) for b in neighbors(a))
    def gauss(key):
        q,E=unpack(key);dd=defaultdict(int)
        for (a,b),v in E.items():
            change=v-Ebase.get((a,b),0);dd[a]+=change;dd[b]-=change
        return all(dd[v]==getq(q,v)-q0(v) for v in set(q)|set(dd))
    def walk(vec):
        out=defaultdict(int)
        for key,amp in vec.items():
            q,_=unpack(key);hs=holes(key)
            # Verify the omitted -F_c*F_c(1-Q_c) terms vanish on this input.
            for a in hs:
                for b in neighbors(a):
                    for c in neighbors(b):
                        assert all(getq(q,d)!=0 for d in neighbors(c))
            for a in hs:
                for b in neighbors(a):
                    middle=move(key,a,b,'in');assert middle is not None
                    for c in neighbors(b):
                        final=move(middle[0],c,b,'out')
                        if final is not None:out[final[0]]+=amp
        return dict(out)
    return move,gamma,gauss,walk,holes

full=Preparation(8)
for y,z in product(range(8),repeat=2):
    p=(y+z)%2
    for j in range(2):
        a=(4*j+p,y,z)
        if a!=(0,0,0):full.birth_pair(a)
full_meta=full.finish();assert full_meta['B_occupants']==256 and full_meta['births']==127
move,gamma,gauss,walk,holes=relative_ops(full);empty=((),())
assert gamma(empty)==0 and gauss(empty)
mid,unit1=move(empty,(2,0,0),(1,0,0),'in')
target,unit2=move(mid,(0,0,0),(1,0,0),'out')
v1=walk({empty:1});assert v1[target]==1 and gamma(target)==0 and unit1 and unit2
assert all(gauss(k) and gamma(k)==0 for k in v1)
# A genuine higher dressed-jump coefficient destroys leading darkness:
# on target holes are0,6; refill0 from B7, then original birth at(6,7).
middle2,unit3=move(target,(0,0,0),(-1,0,0),'in')
absorbed,unit4=move(middle2,(-2,0,0),(-1,0,0),'birth',1)
assert unit3 and unit4 and not holes(absorbed) and gauss(absorbed)
full_meta.update({'bare_loss':gamma(empty),'H2_selected_off_diagonal_amplitude':v1[target],'H2_first_Krylov_words':len(v1),'after_selected_fast_move_loss':gamma(target),'true_microscopic_reverse_hop_W':len(holes(mid)),'J1_minus_jFdagger_nonzero_after_selected_fast_move':True,'J1_selected_output_W':len(holes(absorbed))})

island=Preparation();R=9;J=3
for y,z in product(range(-R,R+1),repeat=2):
    p=(y+z)%2
    for j in range(-J,J+1):
        a=(4*j+p,y,z)
        if a!=(0,0,0):island.birth_pair(a)
island_meta=island.finish();move,gamma,gauss,walk,holes=relative_ops(island)
for a in holes(empty):
    for dx,dy,dz in product(range(-7,8),repeat=3):
        if abs(dx)+abs(dy)+abs(dz)<=7:
            b=add(a,(dx,dy,dz))
            if not base_charge(b):assert island.charge(b)!=0
vec={empty:1};prefix=[]
for n in range(3):
    assert all(gauss(k) and gamma(k)==0 for k in vec)
    prefix.append({'power':n,'basis_words':len(vec),'all_original_losses_zero':True,'coefficient_square_sum':sum(v*v for v in vec.values())})
    if n<2:vec=walk(vec)
island_meta.update({'filled_buffer_radius_about_each_hole':7,'exact_dark_Krylov_prefix':prefix,'sufficient_nonalias_even_torus_period':40})
result={'scope':'Independent actual word/geometry control before author proof exposure. The isolated word has not been observed as a new record. No probability weight or full microscopic convergence is inferred.','full_L8':full_meta,'finite_island':island_meta,'cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
