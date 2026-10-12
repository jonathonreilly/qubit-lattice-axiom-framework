#!/usr/bin/env python3
"""Complete original finite controls; scope is recorded below and in the note."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/ACTUAL_CORRECTOR_SMALL_TIME_LOWER_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/HSTAR_THRESHOLD_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/BOOST_QUANTITATIVE_CORRECTOR_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md']
if not __debug__:
    raise RuntimeError("Run without -O: control assertions must be enabled")

#!/usr/bin/env python3
"""Author controls for L11-L20; a finite fixture is not a threshold proof.

No prior scientific helper is imported. Pauli compression, an augmented
exponential and separately integrated identities test the new algebra.
"""
import json
import platform
import sys
import numpy as np
import scipy
from scipy.linalg import block_diag, expm, null_space
from numpy.polynomial.legendre import leggauss
import sympy as sp

records=[]
def check(name, ok, **data):
    assert bool(ok), name
    records.append({'name':name, **data})

def close(name, x, y, tol=2e-10):
    defect=float(np.linalg.norm(np.asarray(x)-np.asarray(y)))
    check(name,defect<tol,defect=defect,tolerance=tol)

# Exact symbolic integrations and final-threshold bookkeeping.
lam,t,cx,ce,K,R0,R1,M,c,C=sp.symbols('lam t cx ce K R0 R1 M c C',positive=True)
s=sp.symbols('s',nonnegative=True)
delta=lam/t
check('time_adapted_cutoff_constant',sp.simplify(2*lam*cx/sp.sqrt(delta)+t*ce*sp.sqrt(delta)-(2*cx+ce)*sp.sqrt(lam*t))==0)
check('primitive_perturbation_integral',sp.integrate(sp.sqrt(s),(s,0,t))==sp.Rational(2,3)*t**sp.Rational(3,2))
check('varying_source_integral',sp.simplify(sp.integrate(sp.sqrt(s)*(1+2*s/3),(s,0,t))-(sp.Rational(2,3)*t**sp.Rational(3,2)+sp.Rational(4,15)*t**sp.Rational(5,2)))==0)
AL=sp.Rational(2,3)*K*(R0+R1);BL=sp.Rational(4,15)*K*R1
check('actual_residual_constants',sp.simplify((AL+BL).subs({R0:3*M,R1:6*M})-sp.Rational(38,5)*K*M)==0)
check('finite_lambda_forcing_budget',sp.simplify(M*sp.sqrt(c*c/(64*M*M*t*(1+t)**2))*t*(1+t)-c*sp.sqrt(t)/8)==0)
check('finite_lambda_free_budget',sp.sqrt(1-sp.Rational(15,64))==sp.Rational(7,8) and sp.Rational(79,64)<sp.Rational(81,64))
check('finite_lambda_triangle_budgets',sp.Rational(7,8)-sp.Rational(1,2)-sp.Rational(1,8)==sp.Rational(1,4) and sp.Rational(9,8)+sp.Rational(1,2)+sp.Rational(1,8)==sp.Rational(7,4))
c0m=sp.symbols('c0m',positive=True)
cmin=2*c0m/(sp.pi*sp.sqrt(3*sp.pi))
tbar=5/(15428*sp.pi*sp.sqrt(3*sp.pi)*K)
check('nonempty_interval_constant',sp.simplify(cmin/(2*sp.Rational(38,5)*K*406*c0m)-tbar)==0)
KR=np.pi/2+np.sqrt(np.pi/2)+np.pi*np.sqrt(6)/4
check('embedding_constant_diagnostic',np.sqrt(np.pi*np.sqrt(3)/2)<np.pi*np.sqrt(6)/4<KR,KR=float(KR),tbar=float(tbar.subs(K,KR)))

# Four antipodal relative-momentum pairs, with nonuniform full-pair weights.
# Pair coefficients are Euclidean coordinates of the weighted physical fields.
pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.]).astype(complex)]
S1=[np.kron(p,np.eye(2)) for p in pauli];S2=[np.kron(np.eye(2),p) for p in pauli]
cs=np.array([0,1,-1,0],complex)/np.sqrt(2)
frame=np.column_stack([cs]+[p@cs for p in S1])
close('spin_frame',frame.conj().T@frame,np.eye(4))
q=np.array([[.4,.2,.1],[-.7,.3,.25],[.12,-.55,.9],[.8,.45,-.35]])
weights=np.array([.1,.2,.3,.4]);N=len(q);dim=4*N
basis=np.zeros((8*N,dim),complex)
for a in range(N):
    basis[8*a:8*a+4,4*a:4*a+4]=frame/np.sqrt(2)
    basis[8*a+4:8*a+8,4*a:4*a+4]=frame@np.diag([1,-1,-1,-1])/np.sqrt(2)
close('physical_parity_isometry',basis.conj().T@basis,np.eye(dim))
constant=np.zeros(dim,complex);constant[::4]=np.sqrt(weights)
P=np.eye(dim)-np.outer(constant,constant.conj())
physical=null_space(constant.conj()[None,:])
close('global_mean_projection',physical@physical.conj().T,P)
small_dim=physical.shape[1]

def raw_hamiltonian(kappa):
    blocks=[]
    for qp in q:
        for sign in (1,-1):
            qq=sign*qp
            blocks.append(sum(S1[j]*np.sin(kappa[j]/2+qq[j])+S2[j]*np.sin(kappa[j]/2-qq[j]) for j in range(3)))
    return block_diag(*blocks)

def parity_hamiltonian(kappa):
    return basis.conj().T@raw_hamiltonian(kappa)@basis

def reduced(kappa):
    return physical.conj().T@parity_hamiltonian(kappa)@physical

sin=np.sin(q);eps=np.linalg.norm(sin,axis=1);n=sin/eps[:,None]
I0=float(np.sum(weights/(4*eps**2)))
zetafull=np.zeros(dim,complex);tr=np.zeros((dim,dim),complex)
for a in range(N):
    sl=slice(4*a+1,4*a+4)
    zetafull[sl]=np.sqrt(weights[a])*n[a]/(2*eps[a]*np.sqrt(I0))
    tr[sl,sl]=np.eye(3)-np.outer(n[a],n[a])
zeta=physical.conj().T@zetafull
Pi=physical.conj().T@(tr+np.outer(zetafull,zetafull.conj()))@physical
Q=np.eye(small_dim)-Pi
H=reduced(np.zeros(3));h0=physical.conj().T@parity_hamiltonian(np.zeros(3))@constant
close('physical_kernel_projection',Pi@Pi,Pi)
close('physical_kernel_annihilation',H@Pi,np.zeros_like(H))
close('physical_h0_zero_mode',Pi@h0,zeta/np.sqrt(I0))
check('physical_kernel_dimension',np.count_nonzero(np.abs(np.linalg.eigvalsh(H))<1e-10)==int(round(np.trace(Pi).real)),physical_dimension=small_dim,kernel_dimension=int(round(np.trace(Pi).real)),finite_fixture_I0=I0)

kappa=np.array([.14,-.12,.08]);lambda_value=.06;time_value=.73
G=reduced(lambda_value*kappa)/lambda_value;Hfast=H/lambda_value
bblocks=[]
for qp in q:
    for sign in (1,-1):
        bblocks.append(sum((S1[j]+S2[j])*kappa[j]*np.cos(sign*qp[j])/2 for j in range(3)))
B=physical.conj().T@basis.conj().T@block_diag(*bblocks)@basis@physical
V=G-Hfast;E=V-B
close('selfadjoint_generators',G,G.conj().T)
check('noncommuting_fixture',np.linalg.norm(H@V-V@H)>1e-3,commutator_norm=float(np.linalg.norm(H@V-V@H)),V_norm=float(np.linalg.norm(V,2)))
check('bounded_perturbation_fixture',np.linalg.norm(V,2)<=1)

# A positive one-x source fixture uses the exact sine/form-factor/normalizer
# structures. It is NOT the continuum B25 envelope or a continuum quadrature.
x=np.array([.55,.35,.15]);yp=x+kappa/2;ym=x-kappa/2

def source_parameters(scale):
    up=yp if scale==0 else np.sin(scale*yp)/scale
    um=ym if scale==0 else np.sin(scale*ym)/scale
    omega=np.linalg.norm(up)+np.linalg.norm(um)
    w=(1+np.dot(up,um)/(np.linalg.norm(up)*np.linalg.norm(um)))/4
    Z=np.sqrt(w)
    return omega,w/Z

omega,a0=source_parameters(0);omegal,al0=source_parameters(lambda_value)
c0=(2*np.pi)**(-1.5)
normall=np.sqrt(1-c0*c0*lambda_value**3*al0*al0)
hl=physical.conj().T@parity_hamiltonian(lambda_value*kappa)@constant
g0=c0*a0*h0;gl0=c0*al0*hl/normall;A=Pi@B@Pi

def forced_solution(operator,source,frequency,tv):
    aug=np.zeros((small_dim+1,small_dim+1),complex)
    aug[:small_dim,:small_dim]=-1j*operator
    aug[:small_dim,-1]=1j*source
    aug[-1,-1]=-1j*frequency
    return expm(tv*aug)[:small_dim,-1]

def z(tv):return forced_solution(A,Pi@g0,omega,tv)
def W(tv):return forced_solution(G,gl0,omegal,tv)
def g(tv):return np.exp(-1j*omega*tv)*g0
def gl(tv):return np.exp(-1j*omegal*tv)*gl0
def zp(tv):return -1j*A@z(tv)+1j*Pi@g(tv)
def r(tv):return Q@(B@z(tv)-g(tv))
def rp(tv):return Q@(B@zp(tv)+1j*omega*g(tv))
def err(tv):return E@z(tv)+g(tv)-gl(tv)

rzero=r(0)
close('initial_actual_residual',rzero,-Q@g0)
close('residual_in_full_kernel_complement',Pi@r(time_value),np.zeros(small_dim))
hdiff=1e-5
close('residual_time_derivative',rp(time_value),(r(time_value+hdiff)-r(time_value-hdiff))/(2*hdiff),tol=2e-8)
D=W(time_value)-z(time_value)
Dp=-1j*G@W(time_value)+1j*gl(time_value)-zp(time_value)
close('exact_full_error_ODE',1j*Dp,G@D+r(time_value)+err(time_value))
check('full_forcing_terms_resolved',np.linalg.norm(E@z(time_value))>1e-8 and np.linalg.norm(g(time_value)-gl(time_value))>1e-8,generator_error=float(np.linalg.norm(E@z(time_value))),source_error=float(np.linalg.norm(g(time_value)-gl(time_value))))

class SpectralGroup:
    def __init__(self,op):self.val,self.vec=np.linalg.eigh(op)
    def U(self,tv):return (self.vec*np.exp(-1j*tv*self.val))@self.vec.conj().T
    def J(self,tv):
        coef=np.full(len(self.val),complex(tv));mask=np.abs(self.val)>1e-12
        coef[mask]=-np.expm1(-1j*tv*self.val[mask])/(1j*self.val[mask])
        return (self.vec*coef)@self.vec.conj().T

sg=SpectralGroup(G);sh=SpectralGroup(Hfast)
def quad(fun,tv,order=96):
    nodes,ws=leggauss(order)
    return sum(weight*fun((node+1)*tv/2) for node,weight in zip(nodes,ws))*tv/2

# The direct augmented exponential is independent of the diagonal J formula.
jaug=np.zeros((2*small_dim,2*small_dim),complex)
jaug[:small_dim,:small_dim]=-1j*G;jaug[:small_dim,small_dim:]=np.eye(small_dim)
close('primitive_augmented_exponential',sg.J(time_value),expm(jaug*time_value)[:small_dim,small_dim:])

# Corrector: convert Euclidean weighted coordinates back to pair field values.
full=physical@rzero
beta=np.array([np.dot(n[a],full[4*a+1:4*a+4])/np.sqrt(weights[a]) for a in range(N)])
close('longitudinal_range_constraint',np.sum(weights*beta/(2*eps)),0)
cutoff=.7
mean=np.sum(weights*(beta/(2*eps))*(eps>=cutoff))
alpha=beta/(2*eps)*(eps>=cutoff)-mean
xfull=np.zeros(dim,complex);xfull[::4]=np.sqrt(weights)*alpha
close('physical_corrector_global_mean',constant.conj()@xfull,0)
xc=physical.conj().T@xfull
eta_full=np.zeros(dim,complex)
for a in range(N):
    eta_full[4*a+1:4*a+4]=np.sqrt(weights[a])*(beta[a]*n[a]*(eps[a]<cutoff)+2*eps[a]*n[a]*mean)
eta=physical.conj().T@eta_full
close('corrector_range_identity',rzero-H@xc,eta)
range_primitive=-1j*lambda_value*(xc-sh.U(time_value)@xc)+sh.J(time_value)@eta
close('free_corrector_primitive_identity',sh.J(time_value)@rzero,range_primitive)

comparison=-1j*quad(lambda u:sg.U(time_value-u)@V@sh.J(u)@rzero,time_value)
close('ordered_noncommuting_primitive_identity',(sg.J(time_value)-sh.J(time_value))@rzero,comparison)
comparison48=-1j*quad(lambda u:sg.U(time_value-u)@V@sh.J(u)@rzero,time_value,48)
close('comparison_quadrature_resolution',comparison,comparison48)
vary_direct=quad(lambda u:sg.U(time_value-u)@(r(u)-rzero),time_value)
vary_fubini=quad(lambda v:sg.J(time_value-v)@rp(v),time_value)
close('varying_source_Fubini_identity',vary_direct,vary_fubini)
full_duhamel=-1j*quad(lambda u:sg.U(time_value-u)@(r(u)+err(u)),time_value)
close('actual_full_forcing_solution',D,full_duhamel)
error_integral=quad(lambda u:sg.U(time_value-u)@err(u),time_value)
comparison_error=-1j*(comparison+vary_fubini+error_integral)
close('complete_leading_term_comparison',D+1j*sh.J(time_value)@rzero,comparison_error)
check('required_terms_resolved',np.linalg.norm(comparison)>1e-7 and np.linalg.norm(vary_fubini)>1e-7 and abs(mean)>1e-7,primitive_perturbation_norm=float(np.linalg.norm(comparison)),varying_source_norm=float(np.linalg.norm(vary_fubini)),corrector_mean_abs=float(abs(mean)),error_source_integral_norm=float(np.linalg.norm(error_integral)))

# The finite fixture cannot furnish the continuum threshold asymptotic.
nonzero=np.abs(np.linalg.eigvalsh(H));finite_gap=float(np.min(nonzero[nonzero>1e-10]))
check('finite_fixture_limit_boundary',finite_gap>0,finite_complementary_gap=finite_gap,free_primitive_bound_squared_prefactor=float(4*np.linalg.norm(rzero)**2/finite_gap**2),meaning='This fixed mesh has O(lambda^2) squared free primitive, so it cannot prove the continuum square-root law.')
print(json.dumps({'status':'author-controls-only','python':sys.version,'executable':sys.executable,'platform':platform.platform(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,'controls_completed':len(records),'records':records,'scope':'Finite checks establish no continuum cone law or actual asymptotic. The analytic L11-L20 proof is separate; S19 remains an explicit source dependency.'},indent=2))

print("per_element: complete original algebra and constant controls checked")
print("per_site: checked and not executed — no volume-limit inference")
print("per_mode: finite spectral or forced-evolution identities checked")
print("per_block: physical finite parity and global mean projection checked")
print("lattice_wide: checked and not executed — continuum conclusions rest on the written proof")
print("TOTAL: PASS=36 FAIL=0")
print('SCOPE: Physical finite Pauli and noncommuting ODE controls; actual continuum sharpness requires L1-L20 and the separate S threshold law. No physical realization or audit verdict from this runner.')
