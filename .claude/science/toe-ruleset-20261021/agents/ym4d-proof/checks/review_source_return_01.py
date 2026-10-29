#!/usr/bin/env python3
"""Independent exact source-return checks; no imports from author code."""
import hashlib
import itertools
import json
import platform
from pathlib import Path
import sympy as s

R = s.Rational
checks = {}
controls = {}
data = {}

def record(name, value):
    checks[name] = bool(value)
    assert checks[name], name

def control(name, value):
    controls[name] = bool(value)
    assert controls[name], name

def equal(a, b):
    if isinstance(a, s.MatrixBase):
        return all(s.expand(x) == 0 for x in a-b)
    return s.simplify(a-b) == 0

def inv(a):
    # Adjugate and division-free characteristic polynomial: no elimination.
    return a.adjugate(method='berkowitz') / a.det(method='berkowitz')

def matrix_norm(a):
    rows = [sum(abs(a[i,j]) for j in range(a.cols)) for i in range(a.rows)]
    cols = [sum(abs(a[i,j]) for i in range(a.rows)) for j in range(a.cols)]
    return max(rows, default=0), max(cols, default=0)

def atom_norm(atoms, n, vertices, weight=R(101,100)):
    rr, cc = [s.S.Zero]*n, [s.S.Zero]*n
    incidence = {v:s.S.Zero for v in vertices}
    for label, a in atoms:
        factor = weight**len(label)
        mass = s.S.Zero
        for i in range(n):
            for j in range(n):
                val = factor*abs(a[i,j])
                rr[i] += val
                cc[j] += val
                mass += val
        for v in label:
            incidence[v] += mass
    return max(rr, default=0), max(cc, default=0), max(incidence.values(), default=0)

def connected(label, total):
    if not label: return False
    seen = {min(label)}
    while True:
        new = seen | {j for i in seen for j in ((i-1)%total,(i+1)%total) if j in label}
        if new == seen: return seen == set(label)
        seen = new

# One hole; a source read from the collar outside the compressed coordinates.
V = list(range(9))
I = [v for v in V if v != 4]
where = {v:i for i,v in enumerate(I)}
boxes = [set(range(k,k+3)) for k in (0,3,6)]
sources = [R(j+1,50) for j in V]

def build(z):
    k = s.zeros(len(I))
    for x in I:
        k[where[x],where[x]] = 6 + z[(x+1)%9]
        for y in ((x-1)%9,(x+1)%9):
            if y in where: k[where[x],where[y]] = -R(1,3)
    return k

def family(k):
    pp, rr, metadata = [], [], []
    for q in boxes:
        omega_ambient = {((x+j)%9) for x in q for j in (-1,0,1)}
        omega = sorted(omega_ambient & set(I))
        label = frozenset({((x+j)%9) for x in omega_ambient for j in (-1,0,1)})
        ix = [where[x] for x in omega]
        compressed = k.extract(ix,ix)
        local = inv(compressed)
        p = s.zeros(len(I))
        for a,x in enumerate(omega):
            for y in sorted(q & set(I)):
                p[where[x],where[y]] = local[a,omega.index(y)]
        r = -k*p
        for x in omega:
            r[where[x],:] = s.zeros(1,len(I))
        pp.append((label,p)); rr.append((label,r))
        metadata.append((omega_ambient,label))
    return pp,rr,metadata

k = build(sources)
pp,rr,metadata = family(k)
p = sum((a for _,a in pp),s.zeros(len(I)))
r = sum((a for _,a in rr),s.zeros(len(I)))
g = inv(k)
eye = s.eye(len(I))
record('hole_parametrix_identity',equal(k*p,eye-r))
record('characteristic_adjugate_inverse',equal(k*g,eye))
control('wrong_parametrix_sign_detected',not equal(k*p,eye+r))
# In general P and R do not commute; the right Neumann order matters.
control('wrong_inverse_order_detected',not equal(p*(eye+r), (eye+r)*p))
walks = pp[:]
all_atoms = pp[:]
for n in range(1,4):
    nxt=[]
    for a_label,a in walks:
        for b_label,b in rr:
            c=a*b
            if any(c): nxt.append((a_label|b_label,c))
    walks=nxt
    all_atoms.extend(nxt)
partial=sum((a for _,a in all_atoms),s.zeros(len(I)))
record('exact_third_order_remainder',equal(g-partial,g*r**4))
mp=max(atom_norm(pp,len(I),V)[:2]); mr=max(atom_norm(rr,len(I),V)[:2])
bp=atom_norm(pp,len(I),V)[2]; br=atom_norm(rr,len(I),V)[2]
m_actual=atom_norm(all_atoms,len(I),V); errors=max(matrix_norm(g-partial))
m_bound=mp*sum(mr**j for j in range(4))
b_bound=bp*sum(mr**j for j in range(4))+mp*br*sum(j*mr**(j-1) for j in range(1,4))
record('weighted_both_endpoint_bounds',mr<1 and max(m_actual[:2])<=m_bound)
record('weighted_marked_incidence',m_actual[2]<=b_bound)
record('geometric_remainder_bound',errors<=mp*mr**4/(1-mr))
record('all_walk_labels_connected',all(connected(l,9) for l,_ in all_atoms))
record('all_nonzero_endpoints_labelled',all(I[i] in l and I[j] in l for l,a in all_atoms for i in range(len(I)) for j in range(len(I)) if a[i,j]))
remote=next(v for v in V if v not in pp[0][0])
remote_z=sources[:]; remote_z[remote]+=R(2,7)
rp,rrp,_=family(build(remote_z))
record('outside_original_source_invisible',equal(pp[0][1],rp[0][1]) and equal(rr[0][1],rrp[0][1]))
collar_z=sources[:]; collar_z[4]+=R(2,7)
cp,_,_=family(build(collar_z))
record('collar_source_changes_local_inverse',4 not in metadata[0][0] and 4 in pp[0][0] and not equal(pp[0][1],cp[0][1]))
control('truncated_collar_label_detected',4 not in metadata[0][0] and not equal(pp[0][1],cp[0][1]))
data['parametrix']={'ambient_vertices':9,'integrated_vertices':I,'atoms_through_order_3':len(all_atoms),'weighted_r':str(mr),'weighted_M_actual':str(max(m_actual[:2])),'weighted_B_actual':str(m_actual[2]),'error':str(errors),'remote_source':remote,'collar_source':4}

# The marked-right-factor term needs the left COLUMN sum.
a=s.zeros(4); b=s.zeros(4)
for i in range(3): a[i,0]=1
b[0,0]=1
marked_right_mass=3
record('column_norm_required',matrix_norm(a)==(1,3) and marked_right_mass==matrix_norm(a)[1])
control('row_only_marked_bound_rejected',marked_right_mass>matrix_norm(a)[0])

z=s.symbols('z')
kd=s.Matrix([[2+z,R(1,3)],[R(1,3),3-2*z]])
det=kd.charpoly().all_coeffs()[-1]
log_derivative=(-s.diff(det,z)/(2*det)).subs(z,0)
trace_derivative=(-s.trace(inv(kd.subs(z,0))*kd.diff(z))/2)
record('half_logdet_characteristic_vs_trace',log_derivative==trace_derivative==R(9,106))
control('determinant_half_factor_detected',2*trace_derivative!=log_derivative)
control('determinant_sign_detected',-trace_derivative!=log_derivative)
data['minus_half_logdet_derivative']=str(log_derivative)

pi=s.Matrix([[1,-1],[-1,1]])/2
aug=pi*(17*s.eye(2))*pi+s.eye(2)-pi
compressed_square_root=s.Rational(1,3)-(s.eye(2)-pi)[0,0]
record('projection_compression_counterexample',pi*pi==pi and aug==s.Matrix([[9,-8],[-8,9]]) and compressed_square_root==-R(1,6))
record('restricted_slice_is_zero',s.Matrix([[1]]).nullspace()==[])
control('compressed_physical_positivity_rejected',compressed_square_root<0)
data['compressed_augmented_square_root_minus_projector']=str(compressed_square_root)

# Exact nonabelian matrix arithmetic with two anchors and a collar.
ii=s.I
qdiag=s.diag(R(3,5)+ii*R(4,5),R(3,5)-ii*R(4,5))
qx=s.Matrix([[R(5,13),ii*R(12,13)],[ii*R(12,13),R(5,13)]])
qy=s.Matrix([[R(15,17),R(8,17)],[-R(8,17),R(15,17)]])
rot=[qdiag,qx,qy,qdiag*qx,qx*qy,qy*qdiag,qdiag*qy*qx]
edges=[(0,1),(1,2),(4,3),(2,3),(1,3),(0,4),(2,4)]
U={e:m for e,m in zip(edges,rot)}
T=[(0,1),(1,2),(4,3)]
gauge={0:s.eye(2),4:s.eye(2)}
for x,y in T: gauge[y]=gauge[x]*U[x,y]
Z={e:s.simplify(gauge[e[0]]*m*gauge[e[1]].H) for e,m in U.items()}
def path(u,vs):
    ans=s.eye(2)
    for x,y in zip(vs,vs[1:]):
        ans=ans*(u[x,y] if (x,y) in u else u[y,x].H)
    return s.simplify(ans)
record('su2_exact_unitary',all(equal(m.H*m,s.eye(2)) and m.det()==1 for m in U.values()))
record('rooted_forest_fixed',all(equal(Z[e],s.eye(2)) for e in T))
record('collar_fixed',equal(Z[0,4],U[0,4]))
record('two_anchor_transports_fixed',all(equal(path(U,vs),path(Z,vs)) for vs in ([0,1,2,4],[0,1,3,4])))
cycles=([0,1,2,3,4,0],[1,2,3,1],[0,1,2,4,0])
record('nonabelian_loop_traces_fixed',all(equal(s.trace(path(U,vs)),s.trace(path(Z,vs))) for vs in cycles))
bad=dict(gauge);bad[4]=qdiag;bad[3]=bad[4]*U[4,3]
badZ={e:s.simplify(bad[e[0]]*m*bad[e[1]].H) for e,m in U.items()}
control('moving_anchor_detected',not equal(path(U,[0,1,2,4]),path(badZ,[0,1,2,4])))
control('moving_collar_endpoint_detected',not equal(U[0,4],badZ[0,4]))
record('bad_gauge_still_preserves_loop_trace',all(equal(s.trace(path(U,vs)),s.trace(path(badZ,vs))) for vs in cycles))

# Normalized Haar integration is distinct from testing pointwise traces.
qvars=[s.symbols(f'q{k}_0:4', real=True) for k in range(3)]
def qmat(q):
    w,x,y,zz=q
    return s.Matrix([[w+ii*zz,y+ii*x],[-y+ii*x,w-ii*zz]])
triangle=s.expand(s.trace(qmat(qvars[0])*qmat(qvars[1])*qmat(qvars[2]).H)**2)
def sphere_moment(powers):
    if any(p%2 for p in powers): return s.S.Zero
    k=sum(powers)//2
    numerator=s.prod(s.factorial2(p-1) for p in powers if p)
    return numerator/s.prod(4+2*j for j in range(k))
flat=tuple(x for q in qvars for x in q)
haar=0
for powers,coef in s.Poly(triangle,*flat).terms():
    haar+=coef*s.prod(sphere_moment(powers[4*j:4*j+4]) for j in range(3))
reduced_haar=4*sphere_moment((2,0,0,0))
record('triangle_haar_integral_before_after_tree',s.simplify(haar)==reduced_haar==1)
rho=s.symbols('rho',real=True)
chart_volume=s.simplify(4*s.pi*s.integrate(2*s.sin(rho/s.sqrt(2))**2,(rho,0,s.sqrt(2)*s.pi)))
c_haar=1/(4*s.sqrt(2)*s.pi**2)
record('su2_normalized_haar_chart_constant',s.simplify(c_haar*chart_volume)==1)
control('omitted_haar_constant_detected',chart_volume!=1)
data['haar']={'triangle_integral':str(haar),'HS_chart_volume':str(chart_volume),'normalized_Haar_c2':str(c_haar)}

# Independent enumeration of all scalar multi-indices used by (31).
def multis(n,q):
    if q==1: yield (n,);return
    for j in range(n+1):
        for tail in multis(n-j,q-1): yield (j,)+tail
count=0
for qa in (1,2,4):
    for qz in (1,3):
        for n in range(7):
            for m in range(7-n):
                if n+m==0 or (n==1 and m==0): continue
                ca=list(multis(n,qa));cz=list(multis(m,qz))
                count+=len(ca)*len(cz)
                assert len(ca)==s.binomial(n+qa-1,qa-1)
                assert len(cz)==s.binomial(m+qz-1,qz-1)
                assert n+m+1<=2**(n+m)
                assert n*(n+m+1)<=n*2**(n+m)
record('all_order_majorant_combinatorial_inequalities',count>0)
control('omitted_scalar_coordinate_count_detected',len(list(multis(2,4)))>len(list(multis(2,1))))
control('source_linear_term_cannot_be_subtracted',len(list(multis(1,3)))==3)
data['enumerated_majorant_monomials']=count

# Genuine nonlinear two-site implicit action, with remote source propagation.
x,y,t=s.symbols('x y t')
kk=s.Matrix([[2,-R(1,2)],[-R(1,2),3]])
gg=inv(kk)
bb=s.zeros(2,1)
lam=R(1,5)
for iteration in range(6):
    force=s.Matrix([t*x-lam*bb[0]**2,t*y-lam*bb[1]**2])
    bb=(gg*force).applyfunc(lambda e:s.series(e,t,0,6).removeO().expand())
res=kk*bb+lam*bb.applyfunc(lambda a:a*a)-s.Matrix([t*x,t*y])
record('picard_coefficients_solve_stationarity',all(s.series(e,t,0,6).removeO().expand()==0 for e in res))
remote_first=s.expand(bb[0]).coeff(t,1).coeff(y,1)
remote_mixed=s.expand(bb[0]).coeff(t,2).coeff(x,1).coeff(y,1)
record('nonlinear_original_source_propagation',remote_first!=0 and remote_mixed!=0)
local_only=s.Matrix([bb[0].subs(y,0),bb[1].subs(x,0)])
wrong_res=kk*local_only+lam*local_only.applyfunc(lambda a:a*a)-s.Matrix([t*x,t*y])
control('discarding_remote_implicit_source_detected',any(s.series(e,t,0,3).removeO().expand()!=0 for e in wrong_res))
data['implicit']={'first_remote_coefficient':str(remote_first),'mixed_second_coefficient':str(remote_mixed),'order':5}

# Complex two-dimensional Stokes identity, all four oriented faces.
w1,w2,ss,tt=s.symbols('w1 w2 ss tt',real=True)
zv=(1+ii)/10
A0=s.Matrix([w1,w2])
Az=s.Matrix([w1+ii*zv+zv*w2/3,(1+zv/5)*w2+zv/7])
H=A0+ss*(Az-A0)
def density(A): return 1+(1+zv)*A[0]+A[0]*A[1]+2*A[1]**2
before=s.integrate(s.expand(density(A0)),(w1,-1,1),(w2,-1,1))
after=s.integrate(s.expand(density(Az)*Az.jacobian([w1,w2]).det()),(w1,-1,1),(w2,-1,1))
faces=[]
for which,end,orient in ((0,1,1),(0,-1,-1),(1,1,-1),(1,-1,1)):
    subs={w1:end,w2:tt} if which==0 else {w1:tt,w2:end}
    face=H.subs(subs)
    jac=s.Matrix.hstack(face.diff(ss),face.diff(tt)).det()
    faces.append(orient*s.integrate(s.expand(density(face)*jac),(ss,0,1),(tt,-1,1)))
side=s.simplify(sum(faces))
record('complex_two_form_stokes_identity',equal(after-before,side))
control('omitted_contour_side_detected',not equal(after,before))
control('reversed_contour_side_detected',not equal(after-before,-side))
data['complex_contour']={'after_minus_before':str(s.simplify(after-before)),'side':str(side),'oriented_faces':[str(s.simplify(f)) for f in faces]}

sigma=R(1,10); pwidth=2; coarse=sigma*pwidth/5
reference_shift=coarse/sigma
record('coarse_reference_shift_counterexample',reference_shift==R(2,5) and reference_shift!=0)
record('same_coarse_reference_repairs_estimate',(coarse-coarse)/sigma==0)
control('zero_source_wrong_reference_bound_rejected',reference_shift>0)
data['wrong_reference_W_shift_at_epsilon_zero']=str(reference_shift)

result={'arithmetic':'exact rational and Gaussian-rational, SymPy polynomial algebra','python':platform.python_version(),'sympy':s.__version__,'checks':checks,'controls':controls,'data':data,'all_passed':all(checks.values()) and all(controls.values()),'limitations':['Finite algebra and edge cases, not an actual full Yang-Mills Hessian computation.','The all-volume and all-order claims require the independent analytic arguments in the review.','No normalized face bound, arbitrary history estimate, higher-level induction or continuum theorem tested.']}
print(json.dumps(result,indent=2,sort_keys=True))
