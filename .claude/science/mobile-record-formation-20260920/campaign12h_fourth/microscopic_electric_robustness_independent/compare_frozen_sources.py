#!/usr/bin/env python3
"""Post-PRE exact comparison using the independently sealed local matrices.
No root builder is imported here. Root JSON is comparison data only. The
PRE local construction is frozen, independently replayed in a separate path.
"""
from pathlib import Path
import difflib,hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
PRE=json.loads((HERE/'EXACT_STAR_MATRIX_RESULTS.json').read_text())
SNAP=HERE/'comparison_sources/campaign12h_fourth'
AUTH=json.loads((SNAP/'microscopic_electric_robustness_author/EXACT_ELECTRIC_STAR_ENERGY_RESULTS.json').read_text())
OLD=json.loads((HERE/'comparison_runtime/author_success/microscopic_birth_energy_author/EXACT_STAR_ENERGY_RESULTS.json').read_text())
e,delta,kappa,K=s.symbols('epsilon delta kappa K',positive=True)
lam=s.symbols('lam',nonnegative=True);ell=s.symbols('ell',positive=True);z=s.symbols('z')
syms={'epsilon':e,'delta':delta,'kappa':kappa,'K':K,'lam':lam,'ell':ell,'z':z,'I':s.I}
def expr(t):return s.sympify(str(t).replace('lambda','lam'),locals=syms).subs(ell,K*lam)
checks=[]
def same(label,left,right):
 difference=left-right
 if isinstance(difference,s.MatrixBase):difference=difference.applyfunc(s.simplify);ok=difference==s.zeros(difference.rows,difference.cols)
 else:difference=s.simplify(difference);ok=difference==0
 assert ok,(label,str(difference))
 checks.append({'check':label,'exact_difference':'0'})
WORDS=[tuple(r['q']) for r in PRE['basis']];DIM=len(WORDS);idx={q:i for i,q in enumerate(WORDS)}
def sparse(data):
 M=s.zeros(DIM)
 for r in data:M[r['row'],r['column']]=expr(r['value'])
 return M
F=sparse(PRE['operators']['F']);W=sparse(PRE['operators']['W']);E2=sparse(PRE['operators']['E2'])
COMP=sparse(PRE['operators']['C_original']);T=sparse(PRE['operators']['T'])
J={}
for b in (1,2,3):
 for c in (-1,1):J[b,c]=sparse(PRE['operators']['resolved_j'][str((b,c))])
Q1=s.diag(*[int(sum(x*x for x in q)==1) for q in WORDS]);Q3=s.eye(DIM)-Q1
N=Q1+3*Q3;P=s.eye(DIM)-W;M=F.T*F
a=1+3*e**2;Omega=delta/e**4
H0=Omega*(W+e*T+e**2*COMP);H=H0+K*lam*E2
g=s.zeros(DIM,1);g[idx[(1,0,0,0)]]=1;fg=F*g;u=fg/s.sqrt(3);U=g.row_join(u);psi=(g+e*fg)/s.sqrt(a)
scalar=lambda mat:mat[0]
same('complete sector dimension',s.Integer(DIM),s.Integer(16))
same('same original compensation',COMP,M)
same('full physical electric operator',E2,N-s.eye(DIM)+W)
same('physical D_ext zero',sparse(PRE['operators']['D_ext']),s.zeros(DIM))
same('positive original square',H0,Omega*(W-e*F).T*(W-e*F))
same('joint-scaled reachable H1',U.T*H*U,s.Matrix([[expr(t) for t in row] for row in PRE['H1_reachable']]))
same('E2 norm bound maximum eigenvalue',s.Integer(max(E2.diagonal())),s.Integer(3))
# Direct comparison of independently ordered full sectors with author ordering.
for n in (1,3):
 old_words=[tuple(r['q']) for r in OLD['physical_bases'][str(n)]]
 assert set(old_words)=={q for q in WORDS if sum(x*x for x in q)==n}
 selector=s.zeros(DIM,len(old_words))
 for j,q in enumerate(old_words):selector[idx[q],j]=1
 same('root F sector '+str(n),selector.T*F*selector,s.Matrix([[expr(t) for t in row] for row in OLD['F_matrices'][str(n)]]))
 for r in OLD['physical_bases'][str(n)]:assert tuple(r['E'])==tuple(-r['q'][b] for b in (1,2,3))
# Full old spectral argument is checked from independent matrices, not adopted.
h=H0/Omega
same('N3 old exact spectral polynomial',Q3*(h*h-a*h)*Q3,s.zeros(DIM))
same('N3 old high projector rank',s.trace(Q3*h*Q3/a),s.Integer(3))
same('common H0 zero eigenstate',H0*psi,s.zeros(DIM,1))
same('common state is not lambda eigenstate identity',H*psi,K*lam*e*fg/s.sqrt(a))
same('initial energy main author versus own action',scalar(psi.T*H*psi),expr(AUTH['initial_common_preparation_energy']))
same('initial energy PRE',scalar(psi.T*H*psi),expr(PRE['initial_energy_moments']['mean']))
same('initial variance PRE',scalar((H*psi).T*(H*psi))-scalar(psi.T*H*psi)**2,expr(PRE['initial_energy_moments']['variance']))
same('bare g original energy',scalar(g.T*H0*g),expr(OLD['bare_A_input_energy']))
new_marks={};old_marks={};data_marks={}
for inst in ('resolved','coherent'):
 for row in PRE['instruments'][inst]['marks']:
  b,c=(row['mark'][0],str(row['mark'][1])) if inst=='resolved' else (row['mark'],'coherent')
  data_marks[inst,b,c]=row
for row in AUTH['conditional_outputs']:new_marks[row['instrument'],row['edge'][1],row['mark']]=row
for row in OLD['rows']:old_marks[row['instrument'],row['edge'][1],row['mark']]=row
assert set(new_marks)==set(old_marks)==set(data_marks)
for key,row in data_marks.items():
 inst,b,c=key;j=J[b,1]+J[b,-1] if inst=='coherent' else J[b,int(c)]
 v=j*fg;norm=scalar(v.T*v);hv=H*v
 mean=scalar(v.T*hv)/norm;variance=scalar(hv.T*hv)/norm-mean**2;mu=scalar(v.T*M*v)/norm
 prefix=str(key)
 same(prefix+' root versus independent mean',mean,expr(new_marks[key]['conditional_mean']))
 same(prefix+' root versus independent variance',variance,expr(new_marks[key]['conditional_variance']))
 same(prefix+' root coefficient',mu,expr(new_marks[key]['c']))
 same(prefix+' PRE mean',mean,expr(row['mean']))
 same(prefix+' PRE variance',variance,expr(row['variance']))
 same(prefix+' original mark intensity',kappa*norm/a,expr(old_marks[key]['rate']))
 same(prefix+' original high spectral probability',scalar(v.T*Q3*h*Q3*v)/(norm*a),expr(old_marks[key]['high_spectral_probability']))
 same(prefix+' old variance as lambda zero',variance.subs(lam,0),expr(old_marks[key]['conditional_energy_variance']))
 expected=s.zeros(DIM,1)
 for state in old_marks[key]['physical_output']:expected[idx[tuple(state['q'])]]=expr(state['unnormalized_amplitude'])
 same(prefix+' full physical output word amplitudes',v,expected)
 same(prefix+' electric scalar on immediate output',E2*v,2*v)
for inst,channels in [('resolved',list(J.values())),('coherent',[J[b,1]+J[b,-1] for b in (1,2,3)])]:
 loss=sum((j.T*j for j in channels),s.zeros(DIM))*kappa/e**2
 gain=sum(scalar((j*psi).T*H*(j*psi))*kappa/e**2 for j in channels)
 loss_energy=scalar(psi.T*(loss*H+H*loss)*psi)/2
 same(inst+' complete loss operator',loss,4*kappa/e**2*Q1*W)
 same(inst+' actual gain',gain,expr(AUTH['initial_energy_derivatives'][inst]['gain']))
 same(inst+' actual signed loss',-loss_energy,expr(AUTH['initial_energy_derivatives'][inst]['loss']))
 same(inst+' full derivative',gain-loss_energy,expr(AUTH['initial_energy_derivatives'][inst]['total']))
 same(inst+' PRE loss convention',loss_energy,expr(PRE['instruments'][inst]['initial_loss']))
 same(inst+' PRE derivative',gain-loss_energy,expr(PRE['instruments'][inst]['initial_full_energy_derivative']))
 coeff=s.Rational(3,2)*delta/e**2+2*K*lam
 injection=sum((j.T*Q3*H*Q3*j for j in channels),s.zeros(DIM))*kappa/e**2
 same(inst+' full finite-time source relation on reachable subspace',U.T*(injection-coeff*loss)*U,s.zeros(2))
 for ii,j in enumerate(channels):same(inst+' no further birth '+str(ii),j*Q3,s.zeros(DIM))
H1=U.T*H*U;Gamma1=s.diag(0,4*kappa/e**2);G=-s.I*H1-Gamma1/2
same('reachable no-event invariant subspace',(H-s.I*4*kappa/e**2*Q1*W/2)*U,U*(H1-s.I*Gamma1/2))
poly=s.expand(e**4*(z*s.eye(2)-G).det())
same('author full scaled characteristic polynomial',poly,expr(AUTH['scaled_no_event_characteristic_polynomial']))
z0=s.solve(poly.subs(e,0),z)[0];correction=s.symbols('correction')
z2=s.solve(s.expand(poly.subs(z,z0+correction*e**2)).coeff(e,2),correction)[0]
zs=z0+z2*e**2
same('slow root derived from independent H1',zs,expr(AUTH['slow_eigenvalue_through_epsilon2']))
same('implicit-function nondegeneracy',s.diff(poly,z).subs({e:0,z:z0}),s.I*delta)
# Use the precise low/high basis of the released earlier finite-time note.
rotation=s.Matrix([[1,s.sqrt(3)*e],[s.sqrt(3)*e,-1]])/s.sqrt(a)
R=(rotation.T*G*rotation).applyfunc(s.simplify)
same('author old-basis low diagonal',R[0,0],-6*kappa/a-s.I*3*K*lam*e**2/a)
same('author old-basis off diagonal',R[0,1],2*s.sqrt(3)*kappa/(e*a)+s.I*s.sqrt(3)*K*lam*e/a)
same('old-basis high diagonal',R[1,1],-2*kappa/(e**2*a)-s.I*delta*a/e**4-s.I*K*lam/a)
same('contractivity for both instruments',G+G.conjugate().T,-Gamma1)
same('slow numerator order coefficient',s.limit((zs-R[0,0])/e**2,e,0),-s.I*12*kappa**2/delta)
same('off diagonal order coefficient',s.limit(e*R[0,1],e,0),2*s.sqrt(3)*kappa)
zf=s.trace(G)-zs
same('fast eigenvalue gap coefficient',s.limit(e**4*(zf-R[0,0]),e,0),-s.I*delta)
same('slow eigenvector high order coefficient',s.limit((zs-R[0,0])/(R[0,1]*e**3),e,0),-s.I*2*s.sqrt(3)*kappa/delta)
same('fast eigenvector low order coefficient',s.limit(R[0,1]/((zf-R[0,0])*e**3),e,0),s.I*2*s.sqrt(3)*kappa/delta)
# The preserved failed implementation differs only in exact-zero normalization.
old=(SNAP/'microscopic_electric_robustness_author/FAILED_exact_electric_star_energy.py').read_text()
new=(SNAP/'microscopic_electric_robustness_author/exact_electric_star_energy.py').read_text()
old_line='assert s.series(poly.subs(z,zs),e,0,4).removeO()==0'
new_line='assert s.simplify(s.series(poly.subs(z,zs),e,0,4).removeO())==0'
assert old.count(old_line)==1 and old.replace(old_line,new_line)==new
raw=s.series(expr(AUTH['scaled_no_event_characteristic_polynomial']).subs(z,expr(AUTH['slow_eigenvalue_through_epsilon2'])),e,0,4).removeO()
same('preserved assertion is an exact algebraic zero',s.simplify(raw),s.Integer(0))
(HERE/'author_structural_assertion_fix.diff').write_text(''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='frozen_failed_author_source',tofile='frozen_final_author_source')))
result={'stage':'post-PRE scientific source comparison','summary':{'full_physical_dimension':DIM,'actual_marks_compared':len(new_marks),'exact_checks':len(checks),'scientific_discrepancies':[],'author_fixed_lambda_proof_checked':True,'own_uniform_lambda_proof_remains_separately_attributed':True},'provenance':'Independent operators and initial state come only from the author-blind PRE packet; no author builder imported. Root frozen result JSON is comparison data.','checks':checks,'no_event_comparison':{'scaled_polynomial':str(poly),'independently_derived_slow_root_through_epsilon2':str(zs),'old_basis_rotated_generator':[[str(t) for t in R.row(i)] for i in range(2)],'slow_high_amplitude_order':'epsilon^3','fast_low_amplitude_order':'epsilon^3','interpretation':'These exact coefficients validate the hypotheses of the released fixed-lambda eigenvector proof. PRE uses a separate direct Duhamel proof uniform over lambda in [0,1].'},'author_failure_analysis':{'difference':'One structural-zero assertion changed to simplify the exact polynomial coefficient. No scientific formula or tolerance changed.','historical_failures_reported':2,'historical_complete_failed_snapshot_count':1,'preserved_failure_replayed':True,'raw_series':str(raw),'raw_structurally_zero':bool(raw==0),'simplified_series':str(s.simplify(raw))},'scope':'Original physical three-leaf star, common explicit preparation, both original instruments, fixed positive K,delta,kappa, integer S>=1 with the supplied joint scaling. No reservoir construction, universal no-go, volume or repeated-formation result, audit or landing status.'}
(HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result['summary'],indent=2))
print(json.dumps(result['no_event_comparison'],indent=2))
print(json.dumps(result['author_failure_analysis'],indent=2))
