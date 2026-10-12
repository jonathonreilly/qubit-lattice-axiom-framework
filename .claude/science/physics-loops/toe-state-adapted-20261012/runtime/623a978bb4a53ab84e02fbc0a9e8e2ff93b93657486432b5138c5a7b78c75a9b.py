"""Complete fixed controls; emits all rows even after failures."""
import argparse,importlib.util,json,sys
from pathlib import Path
import numpy as np
import scipy.linalg as la
import sympy as sy

p=argparse.ArgumentParser();p.add_argument('--candidate',required=True);args=p.parse_args()
spec=importlib.util.spec_from_file_location('tested_candidate',args.candidate)
candidate=importlib.util.module_from_spec(spec);spec.loader.exec_module(candidate)
rows=[]
TOL=2e-10
def emit(name,passed,**data):
    row={'name':name,'passed':bool(passed),**data};rows.append(row)
    print(json.dumps(row,sort_keys=True),flush=True)
def close(name,value,tol=TOL):emit(name,value<tol,value=float(value),tolerance=tol)
def greater(name,value,threshold):emit(name,value>threshold,value=float(value),threshold=threshold)
def norm(a):return float(la.norm(a,2))
C0=np.array([[0,1j],[-1j,0]])
def actual_parameters(a):
    s=np.sqrt(.25+1/a**2)
    return .5*s+.25,.5*s-.25
def actual_D(a,n):
    g,j=actual_parameters(a);d=np.zeros((2*n,2*n),complex)
    for x in range(n):
        d[2*x,2*x+1]+=2j*g
        d[2*x,2*((x-1)%n)+1]+=-2j*j
        d[2*x+1,2*x]+=-2j*g
        d[2*x+1,2*((x+1)%n)]+=2j*j
    return d
def hermitian_function(a,fun):
    w,u=la.eigh(a);return (u*fun(w)[None,:])@u.conj().T
def actual_P(d):return hermitian_function(d,lambda x:(1+np.sign(x))/2)
def haar(n,components=2):
    h=np.zeros((2*n,n));
    for j in range(n):h[2*j,j]=h[2*j+1,j]=1/np.sqrt(2)
    return np.kron(h,np.eye(components))
def scalar_E(a,n):
    # Positive square root of a direct scalar periodic difference operator.
    lap=np.zeros((n,n))
    for j in range(n):
        lap[j,j]+=2;lap[j,(j-1)%n]-=1;lap[j,(j+1)%n]-=1
    return hermitian_function(np.eye(n)+lap/a**2,np.sqrt).real
def shift(n,steps,components=2):
    x=np.zeros((n,n))
    for j in range(n):x[(j+steps)%n,j]=1
    return np.kron(x,np.eye(components))

# Exact symbolic controls are written independently of candidate.py.
z,c,f=sy.symbols('z c f',nonzero=True)
raw=(1+z)**4/4*((1-f*z)/(1-f/z))*((1-c/z**2)/(1-c*z**2))
rational=(1+z)**4*(1-f*z)*(z*z-c)/(4*z*(z-f)*(1-c*z*z))
emit('symbolic/fourth_power_rational',sy.cancel(raw-rational)==0)
residue=sy.cancel(((z-f)*rational).subs(z,f))
expected=(1+f)**4*(1-f*f)*(f*f-c)/(4*f*(1-c*f*f))
emit('symbolic/pole_residue',sy.cancel(residue-expected)==0,residue=str(sy.factor(residue)))
x,v,a,m=sy.symbols('x v a m',real=True,nonzero=True)
gap=(m*m+16*v*v*sy.sin(x/2)**2/a**2)-(m*m+4*v*v*sy.sin(x)**2/a**2)
# Transparent post-observation arithmetic repair; original false row retained.
# Reduce the actual residual, then impose the exact half-angle unit circle.
ss,cc=sy.symbols('ss cc',real=True)
residual=gap-16*v*v*sy.sin(x/2)**4/a**2
half_residual=residual.subs(sy.sin(x),2*sy.sin(x/2)*sy.cos(x/2))
polynomial=sy.expand((a*a/(16*v*v))*half_residual.subs({sy.sin(x/2):ss,sy.cos(x/2):cc}))
emit('symbolic/dispersion_gap',sy.expand(polynomial.subs(cc*cc,1-ss*ss))==0)

for a in [1.,.5]:
 for n in [8,16]:
    tag=f'ring/a{a:g}_N{n}'
    hc=haar(n);fc=candidate.frame_ring(a,n);ff=candidate.frame_ring(a/2,2*n)
    gc=candidate.adapted_map(a,n,hc)
    dc=actual_D(a,n);df=actual_D(a/2,2*n)
    pc=actual_P(dc);pf=actual_P(df)
    close(tag+'/direct_D_selfadjoint',norm(dc-dc.conj().T))
    close(tag+'/frame_unitary',norm(fc.conj().T@fc-np.eye(2*n)))
    close(tag+'/frame_position_real',norm(fc.imag))
    close(tag+'/refinement_isometry',norm(gc.conj().T@gc-np.eye(2*n)))
    close(tag+'/refinement_position_real',norm(gc.imag))
    close(tag+'/actual_state_pullback',norm(gc.conj().T@pf@gc-pc))
    ec=scalar_E(a,n);ef=scalar_E(a/2,2*n)
    c0c=np.kron(np.eye(n),C0)
    close(tag+'/actual_energy_diagonalization',norm(fc@dc@fc.conj().T-np.kron(ec,C0)))
    tc=hermitian_function(dc,np.sign)
    pos=2*np.eye(2*n)+c0c@tc+tc@c0c
    fpolar=(np.eye(2*n)+c0c@tc)@hermitian_function(pos,lambda x:x**(-.5))
    close(tag+'/bounded_polar_formula',norm(fc-fpolar))
    emit(tag+'/polar_denominator_spectrum',la.eigvalsh(pos).min()>=2-TOL and la.eigvalsh(pos).max()<=4+TOL,
         minimum=float(la.eigvalsh(pos).min()),maximum=float(la.eigvalsh(pos).max()))
    gnext=candidate.adapted_map(a/2,2*n,haar(2*n))
    direct=candidate.frame_ring(a/4,4*n).conj().T@haar(2*n)@hc@fc
    close(tag+'/two_step_composition',norm(gnext@gc-direct))
    close(tag+'/integer_translation',norm(shift(2*n,2)@gc-gc@shift(n,1)))
    vec=gc[:,0].copy();inside=np.zeros(4*n,bool);inside[0:4]=True
    greater(tag+'/outside_two_children',la.norm(vec[~inside]),1e-6)
    defect=df@gc-gc@dc
    greater(tag+'/actual_energy_defect',norm(defect),1e-4)
    scalar_defect=np.kron(ef,C0)@hc-hc@np.kron(ec,C0)
    predicted=ff.conj().T@scalar_defect@fc
    close(tag+'/energy_defect_formula',norm(defect-predicted))
    hs=haar(n,1);e0=np.eye(n)[:,0];s=hs@e0
    g=ef@s-hs@ec@e0
    deriv=1j*(np.outer(g,s.conj())-np.outer(s,g.conj()))
    variance=float(np.vdot(g,g).real-abs(np.vdot(s,g))**2)
    sigma=np.sqrt(max(variance,0))
    greater(tag+'/even_number_derivative',norm(deriv),1e-4)
    close(tag+'/even_number_variance',abs(norm(deriv)-sigma))
    sf=la.expm(.2j*ef)@s;sc=hs@la.expm(.2j*ec)@e0
    greater(tag+'/even_number_time_point',norm(np.outer(sf,sf.conj())-np.outer(sc,sc.conj())),1e-6)

# Infinite-line Haar diagnostic. No torus is substituted in these integrals.
Q=8192.;panels=int(np.ceil(Q/np.pi));edges=np.linspace(0,Q,panels+1)
def haar_integral(a,order):
    nodes,weights=np.polynomial.legendre.leggauss(order)
    mids=(edges[:-1]+edges[1:])/2;halves=(edges[1:]-edges[:-1])/2
    q=(mids[:,None]+halves[:,None]*nodes[None,:]).ravel()
    w=(halves[:,None]*weights[None,:]).ravel()
    multiplier=candidate.embedding_multiplier(a,q)
    # |fhat|^2=(1-cos q)/(pi q^2), evaluated stably at the origin.
    density=2*np.sin(q/2)**2/(np.pi*q*q)
    return float(2*np.sum(w*np.abs(multiplier-1)**2*density))
tail=16/(np.pi*Q)
for n in [0,1,2,3,4,5,9]:
    a=2.**(-n);i16=haar_integral(a,16);i32=haar_integral(a,32)
    close(f'haar/n{n}/quadrature_agreement',abs(i16-i32),2e-8)
    emit(f'haar/n{n}/norm_range',-TOL<=i32<=4+TOL,squared_error_cutoff=i32,
         norm_lower_diagnostic=float(np.sqrt(max(i32,0))),squared_tail_bound=tail,
         norm_upper_diagnostic=float(np.sqrt(max(i32,0)+tail)),cutoff=Q)
    if n==9:emit('haar/n9/geometric_embedding',np.sqrt(i32+tail)<.12,
                  norm_upper_diagnostic=float(np.sqrt(i32+tail)),threshold=.12)

print('per_element: checked one chosen Z image tail and one even number-flow witness; constants are not excluded.',flush=True)
print('per_site: checked nominal two-child support on finite rings; infinite support is proved by the pole argument.',flush=True)
print('per_mode: checked exact dispersion formula and sampled matrices; no universal failure of every individual mode is asserted.',flush=True)
print('per_block: checked two refinement steps across complete periodic rings; these rings are not infinite-chain proofs.',flush=True)
print('lattice_wide: checked and not executed — infinite-line operator and Cauchy-algebra claims are analytic conditional theorems.',flush=True)
summary={'summary':True,'candidate':str(Path(args.candidate).resolve()),'total':len(rows),
         'failed':sum(not x['passed'] for x in rows),'passed':sum(x['passed'] for x in rows)}
print(json.dumps(summary,sort_keys=True),flush=True)
sys.exit(1 if summary['failed'] else 0)
