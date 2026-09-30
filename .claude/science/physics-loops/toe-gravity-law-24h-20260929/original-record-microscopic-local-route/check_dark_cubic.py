"""Exact sparse original cubic birth-word discriminator; integer arithmetic only."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from collections import defaultdict
from itertools import product
import hashlib,json,resource,time
start=time.process_time();here=Path(__file__).resolve().parent
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
neg=lambda a:tuple(-x for x in a)
axes=((1,0,0),(0,1,0),(0,0,1));dirs=axes+tuple(map(neg,axes))
def parity(v):return sum(v)%2
def default(v):return 1 if parity(v)==0 else 0
# A basis key contains only changed charges and nonzero A->B electric fields.
def pack(q,E):return (tuple(sorted((v,x) for v,x in q.items() if x!=default(v))),tuple(sorted((a,b,e) for (a,b),e in E.items() if e)))
def unpack(key):return dict(key[0]),{(a,b):e for a,b,e in key[1]}
def charge(q,v):return q.get(v,default(v))
Omega=pack({},{});a=(0,0,0)
def move(key,a,b,kind,sign=1):
    q,E=unpack(key);qa,qb=charge(q,a),charge(q,b)
    if kind=='out':
        if not qa or qb:return None
        q[a]=0;q[b]=qa;step=-qa
    elif kind=='in':
        if qa or not qb:return None
        q[a]=qb;q[b]=0;step=qb
    else:
        if qa or qb:return None
        q[a]=sign;q[b]=-sign;step=sign
    E[(a,b)]=E.get((a,b),0)+step
    return pack(q,E)
def F(vec,a,reverse=False):
    out=defaultdict(int)
    for key,amp in vec.items():
        for dv in dirs:
            v=move(key,a,add(a,dv),'in' if reverse else 'out')
            if v is not None:out[v]+=amp
    return {v:k for v,k in out.items() if k}
def J(vec,a,b,signs):
    out=defaultdict(int)
    for key,amp in vec.items():
        for sig in signs:
            v=move(key,a,b,'birth',sig)
            if v is not None:out[v]+=amp
    return {v:k for v,k in out.items() if k}
def B(vec,a,b,signs):return J(F(vec,a),a,b,signs)
def gauss(key):
    q,E=unpack(key);div=defaultdict(int)
    for (u,v),e in E.items():div[u]+=e;div[v]-=e
    sites=set(q)|set(div)
    return all(div[v]==charge(q,v)-(1 if parity(v)==0 else 0) for v in sites)
def gamma_basis(key):
    q,E=unpack(key);total=0
    for v,x in q.items():
        if parity(v)==0 and x==0:
            total+=2*sum(charge(q,add(v,dv))==0 for dv in dirs)
    return total
# Grade+1 coefficient J2,+1=-F_a j_(a,b)F_a is derived analytically in the note.
coefficients=[]
for signs in ((1,),(-1,),(1,-1)):
    out=F(J(F({Omega:1},a),a,axes[0],signs),a)
    assert all(gauss(v) for v in out)
    norm2=sum(c*c for c in out.values())
    expected={(1,):40,(-1,):20,(1,-1):60}[signs]
    assert norm2==expected
    coefficients.append({'birth_signs':signs,'basis_words':len(out),'norm_squared':norm2,'amplitude_multiplicities':sorted(set(out.values()))})
# Two specified original marks have a nonzero component with three occupied B
# neighbors of a. The third positive-grade component fills the last three.
c=add(axes[0],axes[1]);d=add(axes[0],axes[2]);extra=add(d,axes[0])
first=B({Omega:1},c,axes[1],(1,));second=B(first,d,extra,(1,))
third=F(J(F(second,a),a,neg(axes[0]),(1,)),a)
key=Omega
for aa,bb,kind,sig in [(c,axes[0],'out',1),(c,axes[1],'birth',1),(d,axes[2],'out',1),(d,extra,'birth',1),(a,neg(axes[1]),'out',1),(a,neg(axes[0]),'birth',1),(a,neg(axes[2]),'out',1)]:
    key=move(key,aa,bb,kind,sig);assert key is not None and gauss(key)
assert third.get(key,0)==2 and gamma_basis(key)==0
q,E=unpack(key)
assert sum(x==0 and parity(v)==0 for v,x in q.items())==1
assert sum(charge(q,add(a,dv))!=0 for dv in dirs)==6
assert sum(abs(x) for v,x in q.items() if parity(v)==1)==7
assert max(map(abs,E.values()))==1
# Fast H2=C+[F,F*]. Only F_c F_a* can change the unique hole a to c2.
c2=(2,0,0);shared=axes[0]
mid=move(key,a,shared,'in');target=move(mid,c2,shared,'out')
assert target is not None and gauss(target)
positive=F(F({key:1},a,reverse=True),c2)
negative=F(F({key:1},c2),a,reverse=True)
amplitude=positive.get(target,0)-negative.get(target,0)
assert amplitude==1 and gamma_basis(target)==8
assert all(gauss(v) for v in first) and all(gauss(v) for v in second) and all(gauss(v) for v in third)
result={'source':'actual unit-amplitude original cubic words; all displayed field changes are0->+/-1, legal with unit spin weight for every S>=1','J2_positive_grade_coefficients_on_Omega':coefficients,'resolved_total_positive_grade_creation_coefficient_per_A_in_units_kappa_epsilon2':6*(40+20),'coherent_total_positive_grade_creation_coefficient_per_A_in_units_kappa_epsilon2':6*60,'original_mark_word':{'first_center':c,'first_birth_B':axes[1],'second_center':d,'second_birth_B':extra,'third_center':a,'third_birth_B':neg(axes[0]),'all_birth_signs':1},'sparse_word_counts':{'first_original_B':len(first),'second_original_BB':len(second),'third_positive_grade_component':len(third)},'dark_component':{'coefficient_before_overall_J2_minus_sign':third[key],'charge_changes':key[0],'electric_fields':key[1],'A_holes':1,'B_occupants':7,'bare_original_loss':0},'fast_bright_output':{'hole_center':c2,'D2_matrix_element':amplitude,'bare_original_loss':gamma_basis(target),'charge_changes':target[0],'electric_fields':target[1]},'scope':'Counterexample to pointwise Gamma>=cW and ||D2 psi||<=C||Gamma^1/2 psi|| on actual physical states; does not prove a dark invariant subspace, a persistent fast carrier, failure of local convergence from Omega, or a conditional-record proxy. The dark word is an internal nonzero component of actual mark-word algebra, not a newly observed sign/field projection.','cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'DARK_CUBIC_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'positive_grade_per_A':360,'dark_loss':0,'bright_loss':8,'fast_D2_matrix_element':1,'word_counts':result['sparse_word_counts'],'cpu_seconds':result['cpu_seconds'],'peak_rss_bytes':result['peak_rss_bytes']},indent=2))
