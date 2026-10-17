#!/usr/bin/env python3
"""Independent bounded local/conditional-lemma checks, not installed dynamics.

Bit-action full-qubit assembly and Gram-factor positivity replace the author's
plaquette projector-polynomial check. Four local matching equations determine
scattering amplitudes independently of the rank-one S formula. Generic exact
overlap examples and finite graph powers test new conditional-lemma risks.
"""
from pathlib import Path
from fractions import Fraction as Q
import datetime,hashlib,json,platform,resource,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(45,45))
START=time.monotonic()
ROOT=Path(__file__).resolve().parent
import sympy as s
R=s.Rational; I=s.I
pins=json.loads((ROOT/'SOURCE_PINS.json').read_text())
for row in pins['sources']:
 b=(ROOT/row['snapshot_path']).read_bytes()
 assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
author=json.loads((ROOT/'sources/author/ALGEBRA_CERTIFICATE.json').read_text())
J=R('0.030021107107032');q0=R('4.510351185997098')
z0=(q0*q0-1+2*I*q0)/(q0*q0+1)
c=s.expand(z0*z0); E0=2*J*(1-s.re(z0)); kap=R(1,10**12)
sig=R(1,10**6);v=R(1,40)
assert s.expand(z0*s.conjugate(z0))==1
assert E0>2*kap

def clean(m):return m.applyfunc(s.cancel)
def atbit(op,bit):
 out=s.zeros(8)
 for state in range(8):
  b=(state>>bit)&1
  if op=='n':out[state,state]=b
  elif op=='X':out[state^(1<<bit),state]=1
  elif op=='Y':out[state^(1<<bit),state]=I*(1-2*b)
 return out
n=[atbit('n',b) for b in (2,1,0)]
X=[atbit('X',b) for b in (2,1,0)]
Y=[atbit('Y',b) for b in (2,1,0)]
hops=[];blocks=[];local_records=[]
for site,t in [(1,kap),(2,-kap*c)]:
 bit=(2,1,0)[site];hop=s.zeros(8)
 for state in range(8):
  e=(state>>2)&1;j=(state>>bit)&1
  if e==1 and j==0:hop[state^(1<<2)^(1<<bit),state]=t
  if e==0 and j==1:hop[state^(1<<2)^(1<<bit),state]=s.conjugate(t)
 block=kap*(n[0]+n[site])+hop
 assert block==block.H
 # In local |e,j> order00,01,10,11, the Gram decomposition makes positivity
 # transparent on both one-head and double-occupation sectors.
 vv=s.Matrix([0,t/kap,1,0]);double=s.Matrix([0,0,0,1])
 gram=clean(kap*vv*vv.H+2*kap*double*double.H)
 local=s.Matrix([[0,0,0,0],[0,kap,t,0],[0,s.conjugate(t),kap,0],[0,0,0,2*kap]])
 assert gram==local and s.simplify((vv.H*vv)[0])==2 and (vv.H*double)[0]==0
 assert clean(hop-(s.re(t)*(X[site]*X[0]+Y[site]*Y[0])+s.im(t)*(Y[site]*X[0]-X[site]*Y[0]))/2)==s.zeros(8)
 hops.append(hop);blocks.append(block)
 local_records.append({'attachment':site,'positive_Gram_weights':[str(kap),str(2*kap)],'nonzero_eigenvalue':str(2*kap)})
addition=blocks[0]+blocks[1]+(E0-2*kap)*n[0]+kap*(s.eye(8)-n[1])+kap*(s.eye(8)-n[2])
target=E0*n[0]+hops[0]+hops[1]+2*kap*s.eye(8)
assert clean(addition-target)==s.zeros(8)
total=n[0]+n[1]+n[2]
assert clean(addition*total-total*addition)==s.zeros(8)
missing_vacancy=clean(addition-kap*(s.eye(8)-n[1])-target)
assert missing_vacancy[0,0]==-kap and missing_vacancy[2,2]==0
# Exact seed variance: seed=e occupied, both attachment clocks empty.
seed=s.zeros(8,1);seed[4,0]=1
spill=clean((addition-(E0+2*kap)*s.eye(8))*seed)
assert s.simplify((spill.H*spill)[0])==2*kap**2

# Derive the retarded coefficient directly from the delta jump. A wrong
# retarded sign yields jump -1 instead of1.
zz,jj=s.symbols('z J',nonzero=True)
green=1/(jj*(zz-1/zz));energy_minus_diag=-jj*(zz+1/zz)
assert s.cancel(energy_minus_diag*green+2*jj*green*zz)==1
assert s.cancel(energy_minus_diag*(-green)+2*jj*(-green)*zz)==-1

def stationary_by_local_matching(z,incoming):
 """Solve equations at clock0,1,2 and emitter, not a rank-one formula."""
 energy=2*J-J*(z+1/z)
 refl,trans,x,y=s.symbols('reflection transmission interior emitter')
 if incoming=='+':
  left0=1+refl;leftminus=1/z+refl*z
  right2=trans*z*z;right3=trans*z**3
 else:
  left0=trans;leftminus=trans*z
  right2=z**-2+refl*z*z;right3=z**-3+refl*z**3
 equations=[(energy-2*J)*left0+J*leftminus+J*x-kap*y,
            (energy-2*J)*x+J*left0+J*right2,
            (energy-2*J)*right2+J*x+J*right3+kap*c*y,
            (energy-E0)*y-kap*left0+kap*s.conjugate(c)*right2]
 mat,rhs=s.linear_eq_to_matrix(equations,(refl,trans,x,y))
 sol=clean(mat.inv(method='DM')*rhs)
 assert clean(mat*sol-rhs)==s.zeros(4,1)
 return sol

point_records=[]
for label,z in [('notch',z0),('separate_algebra_point',R(3,5)+I*R(4,5))]:
 z=s.cancel(z);vg=s.cancel(J*(z-1/z)/I)
 gp=s.cancel(1-c/z**2);gm=s.cancel(1-c*z**2)
 plus=stationary_by_local_matching(z,'+');minus=stationary_by_local_matching(z,'-')
 direct=s.Matrix([[plus[1],minus[0]],[plus[0],minus[1]]])
 G=1/(J*(z-1/z))
 Sigma=s.cancel(G*(2-(c+s.conjugate(c))*z*z))
 den=s.cancel(2*J-J*(z+1/z)-E0-kap**2*Sigma)
 form=s.Matrix([gp,gm])
 proposed=s.eye(2)+kap**2*G*(form*form.H)/den
 assert clean(direct-proposed)==s.zeros(2)
 assert clean(direct.H*direct-s.eye(2))==s.zeros(2)
 # The sum of the two outgoing densities must equal the seed spectral density.
 densities=kap**2*(gp*s.conjugate(gp)+gm*s.conjugate(gm))/(2*vg*den*s.conjugate(den))
 assert s.cancel(-s.im(1/den)-densities)==0
 if label=='notch':
  assert plus[0]==0 and plus[1]==1 and minus[0]==0
 point_records.append({'label':label,'z':str(z),'local_equations_dimension':4,
   'return_reflection_squared':str(s.cancel(plus[0]*s.conjugate(plus[0]))),
   'return_transmission_difference_squared':str(s.cancel((plus[1]-1)*s.conjugate(plus[1]-1)))})

# Wrong loop-phase conjugation can preserve unitarity but moves the emission
# zero to the opposite direction; the intended physical form factor rejects it.
gp0=s.cancel(1-c/z0**2);gm0=s.cancel(1-c*z0**2)
wrong_gp=s.cancel(1-s.conjugate(c)/z0**2)
assert gp0==0 and wrong_gp!=0
sin2=2*s.re(z0)*s.im(z0)
assert s.cancel(wrong_gp*s.conjugate(wrong_gp)-4*sin2**2)==0

# Check interval constants directly from the exact inputs, not author displays.
ratio=sig/(sin2-sig)
derived={'sin_2k0':sin2,'directional_ratio':ratio,'return_reflection_ceiling':2*ratio,
 'return_transmission_error_ceiling':2*ratio**2,
 'wrong_way_in_band_probability_fraction_ceiling':ratio**2,
 'single_column_out_of_band_norm_squared_ceiling':2*kap**2/(v*sig)**2,
 'grouped_out_of_band_operator_norm_squared_ceiling':4*kap**2/(v*sig)**2,
 'added_common_scalar':2*kap,'emitter_incident_positive_block_norm_sum':E0+2*kap,
 'clock_attachment_added_positive_block_norm_sum':3*kap}
for name,value in derived.items():assert s.cancel(value-R(author['constants_exact'][name]))==0
assert ratio<R(131,10**8) and 2*ratio<R(262,10**8)
assert 2*ratio**2<R(344,10**14) and ratio**2<R(172,10**14)
assert 2*J*(s.im(z0)-sig)>v
assert derived['single_column_out_of_band_norm_squared_ceiling']<R(6,10**5)**2
assert derived['grouped_out_of_band_operator_norm_squared_ceiling']==R(8,10**5)**2

# Independent algebraic form of the closed-tail derivative, m=L-2>=1.
m=s.symbols('m',integer=True,positive=True);rr=R(1,7)
alternative=700*(rr**m+rr**(m+2))+R(16,24)*(m*rr**(m-1)+(m+2)*rr**(m+1))
claimed=(700*R(50,49)+R(16,84))*rr**m+R(16,24)*m*R(50,49)*rr**(m-1)
assert s.simplify(alternative-claimed)==0

# Seed-overlap identity for two nontrivial rectangular isometries. A's
# off-diagonal Hermitian part matters, not just overlap magnitudes.
seed_map=s.eye(2).col_join(s.zeros(2))
U=s.Matrix([[R(3,5),R(4,5)*I],[R(4,5)*I,R(3,5)]])
V=s.Matrix([[0,1],[-1,0]])
Gamma=(R(3,5)*U).col_join(R(4,5)*V)
assert Gamma.H*Gamma==s.eye(2)
A=seed_map.H*Gamma
gram=clean((seed_map-Gamma).H*(seed_map-Gamma))
assert gram==clean(2*s.eye(2)-A-A.H)
phase_only=s.diag(1,-1)
assert [abs(phase_only[j,j]) for j in range(2)]==[1,1]
assert (s.eye(2)-phase_only).H*(s.eye(2)-phase_only)==s.diag(0,4)
aligned=-s.Matrix([[1,1],[1,1]])
assert (aligned[:,0].H*aligned[:,0])[0]==2
superposition=s.Matrix([1,1])
assert (superposition.H*aligned.H*aligned*superposition)[0]/(superposition.H*superposition)[0]==4

# Exact normalization sample plus general squared identity: omitted norm5/13
# leaves retained norm12/13, so positive-real normalization costs1/13.
omitted=R(5,13);retained=R(12,13)
assert omitted**2+retained**2==1 and omitted<R(1,2)
assert 1-retained==R(1,13) and 1-retained<=omitted

# Check the first omitted hop using exact graph powers. This diagnostic
# graph has all actual emitter edges but no internal old/source truncation.
# It establishes the combinatorial threshold; internal onsite terms cannot
# change its general proof.
L=3;M=7;dim=M+2;ee=dim-1; jg=R(1,3);kg=R(1,17);cg=R(5,13)+R(12,13)*I
H=s.diag(*[R(t+1,10) for t in range(dim)])
for x in range(M):H[x,x+1]=H[x+1,x]=-jg
H[L,ee]=H[ee,L]=kg
H[L+2,ee]=-kg*cg;H[ee,L+2]=-kg*s.conjugate(cg)
P=s.eye(dim);P[M,M]=0
finite=P*H*P
eseed=s.zeros(dim,1);eseed[ee,0]=1
distance=M-L-1
for degree in range(distance):assert H**degree*eseed==finite**degree*eseed
first=(H**distance-finite**distance)*eseed
assert s.cancel(first[M,0]+kg*cg*jg**(M-L-2))==0 and first[M,0]!=0
rho=R(19);center=R(7,9)
hs=(H-center*s.eye(dim))/rho;fs=(finite-center*s.eye(dim))/rho
T3=lambda a:4*a**3-3*a
first_cheb=clean((T3(hs)-T3(fs))*eseed)
assert s.cancel(first_cheb[M,0]-4*first[M,0]/rho**3)==0
spectral_center=(1+20+4*J)/2
assert abs(1+E0-spectral_center)<18 and abs(20+E0-spectral_center)<18
assert 2*kap**2<1  # sqrt(2)*kap<1; the complete radius18 expands by<1.

report={'scope':'Independent local identities and conditional-lemma risks only; no installed inverse, seed overlap or emission time certified',
 'local_positive_Gram_decompositions':local_records,
 'full_qubit_dimension':8,'full_qubit_scalar_identity':True,'Pauli_cross_quadrature_signs':True,
 'seed_variance_exact':str(s.cancel((spill.H*spill)[0])),
 'local_matching':point_records,'Green_jump_with_wrong_sign':-1,
 'wrong_phase_notch_squared':str(s.cancel(wrong_gp*s.conjugate(wrong_gp))),
 'exact_constants':{k:str(s.cancel(vv)) for k,vv in derived.items()},
 'closed_tail_derivative_alternative_exact':str(alternative),
 'seed_overlap_test':{'rectangular_dimensions':[4,2],'Gram_identity':[[str(x) for x in row] for row in gram.tolist()],
     'unit_diagonal_overlap_magnitudes_do_not_suffice_squared_error':4,
     'aligned_error_single_column_norm_squared':2,'aligned_error_operator_norm_squared':4,
     'actual_installed_overlap_computed':False},
 'normalization_test':{'omitted_norm':str(omitted),'retained_norm':str(retained),'normalization_cost':str(1-retained)},
 'finite_graph_test':{'L':L,'M':M,'dimension':dim,'first_omitted_hops':distance,
     'first_nonzero_omitted_power_amplitude':str(first[M,0]),'first_nonzero_omitted_chebyshev_amplitude':str(first_cheb[M,0]),
     'rho19_sufficient_for_diagnostic_parameters':True},
 'limits':{'author_program_imported_or_run':False,'installed_matching_inverted':False,'actual_seed_overlap_integrated':False,
     'finite_emission_time':None,'clock_time_evolution':False,'interval_grid':False,'optimizer':False,
     'same_model_source_exposed':True,'formal_audit':False},
 'runtime':{'cpu_seconds_cap':45,'parent_wall_seconds_cap':60,'largest_matrix_dimension':dim,
     'python':sys.version,'sympy':s.__version__,'platform':platform.platform(),
     'elapsed_seconds':time.monotonic()-START}}
(ROOT/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'Exact reviewer checks completed','seed_variance':report['seed_variance_exact'],
 'local_scattering_points':len(point_records),'matrix_dimension':dim,'graph_hop_distance':distance,
 'actual_seed_overlap_computed':False,'emission_time':None,'elapsed_seconds':report['runtime']['elapsed_seconds']},indent=2))
