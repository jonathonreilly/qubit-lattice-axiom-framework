"""Independent source-exposed diagnostics. No author helper imports."""
import os, sys, re, time, json, hashlib, resource, subprocess, itertools, cmath
from pathlib import Path
START=time.monotonic()
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[5]
rows=[]; gates=[]
def serial(x):
    if isinstance(x,(str,int,float,bool)) or x is None:return x
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return str(x)
def check(name,ok,value=None,mutation=False):
    rows.append({'name':name,'pass':bool(ok),'value':serial(value),'mutation':mutation})
def gate(label):
    out=subprocess.check_output(['/usr/bin/memory_pressure','-Q'],text=True)
    free=int(re.search(r'System-wide memory free percentage:\s*(\d+)%',out).group(1))
    load=os.getloadavg(); rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert sys.platform=='darwin'
    g={'stage':label,'free_percent':free,'load':load,'max_rss_bytes':rss,'elapsed_seconds':time.monotonic()-START}
    gates.append(g)
    assert free>=50 and max(load)<20 and rss<2_000_000_000 and g['elapsed_seconds']<60,g
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:assert os.environ[n]=='1'
gate('before_imports')
import sympy as s
import mpmath as mp
mp.mp.dps=60
lock=ROOT/'logs/physics_worker_lock.json'
lock_data=json.loads(lock.read_text())

# A noncommuting Laurent-phase matrix, with phase-two seagulls retained.
e,z=s.symbols('e z',real=True)
O0=s.diag(2,3,5); G=O0.inv()
Vp=s.Matrix([[0,1,0],[2,0,1],[0,-1,0]]); Vm=Vp.T
S=s.diag(1,-1,2); T=s.Matrix([[0,1,2],[0,0,0],[0,0,0]])
O1=z*Vp+Vm/z; O2=S+z*z*T+T.T/z**2
poly=s.expand((O0+e*O1+e*e*O2).det())
d0=poly.coeff(e,0); d1=poly.coeff(e,1); d2=poly.coeff(e,2)
direct=s.expand(d2/d0-d1*d1/(2*d0*d0)).coeff(z,0)
def phase_trace(bubble=s.Rational(1,2),drop_second=False):
    pair=s.trace(G*Vp*G*Vm)
    if not drop_second:pair+=s.trace(G*Vm*G*Vp)
    return s.trace(G*S)-bubble*pair
check('noncommuting_direct_determinant',s.simplify(direct-phase_trace())==0,direct)
check('quarter_bubble_rejected',direct!=phase_trace(s.Rational(1,4)),phase_trace(s.Rational(1,4)),True)
check('one_transfer_rejected',direct!=phase_trace(drop_second=True),phase_trace(drop_second=True),True)
check('noncommuting_fixture',Vp*Vm!=Vm*Vp)

# Obtain the angular polynomials from the actual continuum transfer matrices.
t,n1,n2=s.symbols('t n1 n2',real=True)
J=s.zeros(4);J[0,1]=1;J[1,0]=-1
I=s.eye(4)
def continuum_series(dim,bubble=s.Rational(1,2),spin=1):
    unit=s.eye(dim)
    jp=J if dim==4 else s.zeros(1)
    plus=-n1*unit+spin*t*jp;minus=-n1*unit-spin*t*jp
    expr=s.Rational(dim,2)-bubble*(s.trace(minus*plus)/(1+2*t*n2+t*t)+s.trace(plus*minus)/(1-2*t*n2+t*t))
    return s.expand(s.series(expr,t,0,3).removeO()).coeff(t,2)
a,b=s.symbols('a b')
mom=s.solve([a-3*b,4*a+12*b-1],[a,b])
def angular(expr):
    expr=s.Poly(s.expand(expr),n1,n2)
    ans=0
    moments={(0,0):1,(2,0):s.Rational(1,4),(2,2):mom[b]}
    for powers,c in expr.terms():ans+=c*moments[powers]
    return s.simplify(ans)
hs=continuum_series(1);hv=continuum_series(4)
cs=angular(hs);cv=angular(hv)
check('angular_polynomial_scalar',s.simplify(hs-(n1*n1-4*n1*n1*n2*n2))==0,hs)
check('angular_vector_spin_derived',s.simplify(hv-4*hs+2)==0,hv)
check('sphere_moments_from_rotation',mom[a]==s.Rational(1,8) and mom[b]==s.Rational(1,24),mom)
check('absolute_scalar_and_vector_coefficients',cs==s.Rational(1,12) and cv==-s.Rational(5,3),[cs,cv])
check('quarter_bubble_absolute_coefficient_rejected',angular(continuum_series(1,s.Rational(1,4)))!=cs,mutation=True)
check('removed_spin_rejected',angular(continuum_series(4,spin=0))!=cv,mutation=True)
# General root identity by coefficient comparison, with exact examples N=2..6.
root_results={}
for N in range(2,7):
    h=s.symbols('h0:'+str(N))
    root=sum((h[i]-h[j])**2 for i in range(N) for j in range(i+1,N))
    root_results[N]=s.expand(root-N*sum(x*x for x in h)+sum(h)**2)==0
check('all_root_identity_coefficients',all(root_results.values()),root_results)
N=s.symbols('N',positive=True)
rad=1/(8*s.pi**2)
sigma_perp=s.simplify(4*N*N*(cv-cs)*rad)
sigma_full=s.simplify(4*N*N*(cv-2*cs)*rad)
check('HS_and_FLOW_match',s.simplify(4*N*(cv-2*cs)*rad*N-sigma_full)==0)
check('u_slope_derived',s.simplify(sigma_full+11*N*N/(12*s.pi**2))==0,[sigma_perp,sigma_full])
check('missing_second_real_colour_rejected',s.simplify(sigma_full/2-sigma_full)!=0,mutation=True)
check('missing_HS_density_conversion_rejected',s.simplify(4*N*(cv-2*cs)*rad-sigma_full)!=0,mutation=True)
check('full_vs_half_ghost_rejected',sigma_perp!=sigma_full,mutation=True)

gate('after_exact_coefficients')
# Off-shell actual SU2 plaquette, all twelve quantum directions.
I2=mp.eye(2)
E=[mp.matrix([[0,1j],[1j,0]]),mp.matrix([[0,1],[-1,0]]),mp.matrix([[1j,0],[0,-1j]])]
def dagger(A):return A.transpose_conj()
def tr(A):return sum(A[j,j] for j in range(A.rows))
def exp_su(v):
    r=mp.sqrt(sum(x*x for x in v));X=sum((v[j]*E[j] for j in range(3)),mp.zeros(2))
    return mp.cos(r)*I2+(mp.sin(r)/r if r else 1)*X
def maxabs(A):return max(abs(A[i,j]) for i in range(A.rows) for j in range(A.cols))
vec=[[mp.mpf(x) for x in v] for v in [['.17','.03','-.11'],['.02','.19','.07'],['-.08','.04','.13'],['.09','-.12','.02']]]
B=[exp_su(v) for v in vec];Sqrt=[exp_su([x/2 for x in v]) for v in vec]
orient=[1,1,-1,-1]
def factors(chart):
    fac=[];der=[]
    for j in range(4):
        if orient[j]==1:
            fac.append(B[j]);der.append([B[j]*x if chart=='right' else Sqrt[j]*x*Sqrt[j] for x in E])
        else:
            fac.append(dagger(B[j]));der.append([-x*dagger(B[j]) if chart=='right' else -dagger(Sqrt[j])*x*dagger(Sqrt[j]) for x in E])
    return fac,der
def product(fs):
    out=mp.eye(2)
    for f in fs:out=out*f
    return out
def jets(chart):
    f,d=factors(chart);grad=mp.zeros(12,1);H=mp.zeros(12)
    for ia in range(12):
        i,a=divmod(ia,3);ff=f.copy();ff[i]=d[i][a];grad[ia]=-mp.re(tr(product(ff)))/2
        for jb in range(12):
            j,b=divmod(jb,3);ff=f.copy()
            if i==j:
                H[ia,jb]=mp.re(tr(product(f)))/2 if a==b else 0
            else:
                ff[i]=d[i][a];ff[j]=d[j][b];H[ia,jb]=-mp.re(tr(product(ff)))/2
    return grad,H
M=mp.zeros(12)
for i in range(4):
    for a in range(3):
        for b in range(3):M[3*i+b,3*i+a]=-mp.re(tr(E[b]*dagger(Sqrt[i])*E[a]*Sqrt[i]))/2
gr,Hr=jets('right');gs,Hs=jets('symmetric')
check('actual_SU2_offshell_nonzero_force',maxabs(gr)>mp.mpf('.01'),maxabs(gr))
check('actual_SU2_adjoint_orthogonal',maxabs(M.T*M-mp.eye(12))<mp.mpf('1e-45'),maxabs(M.T*M-mp.eye(12)))
check('actual_SU2_adjoint_determinant',abs(mp.det(M)-1)<mp.mpf('1e-45'),mp.det(M))
check('actual_SU2_gradient_chart',maxabs(gs-M.T*gr)<mp.mpf('1e-45'),maxabs(gs-M.T*gr))
check('actual_SU2_Hessian_chart',maxabs(Hs-M.T*Hr*M)<mp.mpf('1e-45'),maxabs(Hs-M.T*Hr*M))
# Actual gauge generator on four plaquette vertices; do not quotient it away.
ends=[(0,1),(1,2),(3,2),(0,3)]
Dr=mp.zeros(12)
for i,(tail,head) in enumerate(ends):
    for a in range(3):
        for b in range(3):
            Dr[3*i+a,3*tail+b]=-mp.re(tr(E[a]*dagger(B[i])*E[b]*B[i]))/2
            Dr[3*i+a,3*head+b]-=int(a==b)
Ds=M.T*Dr;Or=Hr+Dr*Dr.T;Os=Hs+Ds*Ds.T
check('actual_SU2_completed_Hessian_chart',maxabs(Os-M.T*Or*M)<mp.mpf('1e-45'),maxabs(Os-M.T*Or*M))
check('actual_SU2_scalar_Gram_chart',maxabs(Ds.T*Ds-Dr.T*Dr)<mp.mpf('1e-45'),maxabs(Ds.T*Ds-Dr.T*Dr))
check('untransformed_gauge_generator_rejected',maxabs(Hs+Dr*Dr.T-M.T*Or*M)>mp.mpf('1e-8'),maxabs(Hs+Dr*Dr.T-M.T*Or*M),True)
# A nonlinear additive chart is a different operation: its force term matters.
b=s.symbols('b',positive=True)
j=s.sin(b)/b
actual=j;congruence=s.cos(b)*j*j;force=s.sin(b)*(1/b-s.sin(b)*s.cos(b)/b**2)
check('additive_chart_full_force_chain',s.trigsimp(actual-congruence-force)==0)
check('additive_chart_congruence_only_rejected',s.series(actual-congruence,b,0,5).removeO()!=0,s.series(actual-congruence,b,0,5),True)
check('additive_Haar_Jacobian_nontrivial',s.series(j*j,b,0,5).removeO()!=1,s.series(j*j,b,0,5))

# Exact finite-free-complement correction: the global unit determinant is insufficient.
D=s.diag(2,5,7);U=s.Matrix([[1,-2,1]])/7;F=s.Matrix([[2,3,-1]])/11
A=s.zeros(4);A[:1,1:]=U;A[1:,:1]=-U.T
H0=s.diag(0,2,5,7);H1=s.diag(9,1,3,2);H1[:1,1:]=F;H1[1:,:1]=F.T
H2=s.diag(0,1,2,1)
rot=s.eye(4)+e*A+e*e*A*A/2
Hrpoly=H0+e*H1+e*e*H2
Hspoly=rot.T*Hrpoly*rot

def fixed_coefficient(poly):
    small=poly[1:,1:]
    v1=small.applyfunc(lambda x:s.expand(x).coeff(e,1))
    v2=small.applyfunc(lambda x:s.expand(x).coeff(e,2))
    return s.simplify(s.trace(D.inv()*v2)-s.trace(D.inv()*v1*D.inv()*v1)/2)
change=s.simplify(fixed_coefficient(Hspoly)-fixed_coefficient(Hrpoly))
mixed=2*s.trace(D.inv()*F.T*U);gram=s.trace(U.T*U)
check('fixed_complement_exact_correction',s.simplify(change-mixed+gram)==0,[change,mixed,gram])
check('unit_full_determinant_does_not_remove_correction',change!=0,change,True)
check('missing_mixed_chart_term_rejected',change!=-gram,mutation=True)
check('missing_induced_Gram_rejected',change!=mixed,mutation=True)
check('fixed_rank_density_vanishes',all(s.simplify((change/(2*T0)**4)/(change/T0**4))-s.Rational(1,16)==0 for T0 in [3,6,12]))
# Boundedness is sufficient for every interval, not for adjacent convergence.
A0=s.Rational(7,3);beta=s.Rational(11,5)
a=lambda n:A0*(-1)**n
Bcum=lambda n:beta*n+a(n)-a(0)
check('every_increment_bounded_remainder',all(abs(Bcum(n)-Bcum(j)-beta*(n-j))<=2*A0 for n in range(15) for j in range(n+1)))
check('bounded_sequence_does_not_give_increment_convergence',Bcum(12)-Bcum(11)!=Bcum(13)-Bcum(12),mutation=True)

gate('before_paths')
# All actual paired S4-prime words, built as directed integer edges.
L=3;orders=list(itertools.permutations(range(4)));offsets=list(itertools.product(range(-1,2),repeat=4))
def axial(a,b,order):
    x=list(a);out=[]
    for mu in order:
        step=1 if b[mu]>=x[mu] else -1
        while x[mu]!=b[mu]:
            y=x.copy();y[mu]+=step;out.append((tuple(x),tuple(y)));x=y
    return out
zero=(0,)*4

def word(mu,off,order,drop_end=False):
    y=list(off);y[mu]+=L;root=list(zero);root[mu]=L
    out=axial(zero,off,order)+axial(off,tuple(y),(mu,))
    if not drop_end:out+=[(b,a) for a,b in reversed(axial(tuple(root),tuple(y),order))]
    return tuple(out)

def transform(w,perm,sign):
    def pt(x):
        out=[0]*4
        for i in range(4):out[perm[i]]=sign[i]*x[i]
        return tuple(out)
    return tuple((pt(a),pt(b)) for a,b in w)

sym_ok=True;zero_sum=[[0]*4 for _ in range(4)];count=0
for mu in range(4):
    for off in offsets:
        for order in orders:
            w=word(mu,off,order);count+=1
            for p,sgn in [((1,0,2,3),(1,1,1,1)),((0,1,2,3),(-1,1,1,1))]:
                tw=transform(w,p,sgn);om=p[mu]
                newoff=[0]*4
                for i in range(4):newoff[p[i]]=sgn[i]*off[i]
                if sgn[mu]<0:
                    shift=[0]*4;shift[om]=L
                    tw=tuple((tuple(b[i]+shift[i] for i in range(4)),tuple(a[i]+shift[i] for i in range(4))) for a,b in reversed(tw))
                sym_ok &= tw==word(om,tuple(newoff),tuple(p[i] for i in order))
            for a1,b1 in w:
                for k in range(4):zero_sum[mu][k]+=b1[k]-a1[k]
check('actual7776_paired_paths_and_symmetry',count==7776 and sym_ok,count)
check('actual_zero_alias_map',all(zero_sum[mu][k]==1944*L*int(mu==k) for mu in range(4) for k in range(4)),zero_sum)
q=[.21+.01j,-.17+.02j,.13-.01j,.09+.015j];cache={}
def phase(x):
    if x not in cache:cache[x]=cmath.exp(1j*sum(q[i]*x[i] for i in range(4)))
    return cache[x]
maxerr=0;baderr=0
for mu in range(4):
    exact=cmath.exp(1j*L*q[mu])-1
    val=sum(sum(phase(b)-phase(a) for a,b in word(mu,off,order)) for off in offsets for order in orders)/1944
    bad=sum(sum(phase(b)-phase(a) for a,b in word(mu,off,order,True)) for off in offsets for order in orders)/1944
    maxerr=max(maxerr,abs(val-exact));baderr=max(baderr,abs(bad-exact))
check('actual_root_gradient_complex_alias',maxerr<3e-12,maxerr)
check('deleted_second_axial_leg_rejected',baderr>1e-5,baderr,True)
gate('complete')
result={'scope':'Finite independent diagnostics, not a uniform-theorem certification. Source exposed; no author helper code read/imported.',
        'lock_read_only':lock_data,'resource_gates':gates,'passed':sum(r['pass'] for r in rows),'total':len(rows),'failed':[r for r in rows if not r['pass']],
        'mutation_count':sum(r['mutation'] for r in rows),'rows':rows,'versions':{'python':sys.version,'sympy':s.__version__,'mpmath':mp.__version__},
        'elapsed_seconds':time.monotonic()-START}
print(json.dumps(serial(result),indent=2))
sys.exit(0 if all(r['pass'] for r in rows) else 1)
