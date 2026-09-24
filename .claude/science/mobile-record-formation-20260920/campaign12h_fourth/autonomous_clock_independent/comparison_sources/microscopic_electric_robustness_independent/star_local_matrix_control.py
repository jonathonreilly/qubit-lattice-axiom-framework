#!/opt/homebrew/opt/python@3.13/bin/python3.13
"""Independent complete local physical-sector construction; no campaign imports.
Each charge word is enumerated before local hopping/birth matrices are built.
The tree Gauss law fixes its three fields. Exact normalized spin weights are
checked for every actual transition, not replaced by a presumed rotor law.
"""
from pathlib import Path
from itertools import product
import json,sys,time
import sympy as s
HERE=Path(__file__).resolve().parent
EPS,DELTA,ELL,KAPPA,C=s.symbols('epsilon delta ell kappa C',positive=True)
EDGES=((0,1),(0,2),(0,3))
WORDS=tuple(q for q in product((-1,0,1),repeat=4) if sum(q)==1)
FIELDS=tuple(tuple(-q[b] for b in (1,2,3)) for q in WORDS)
INDEX={q:i for i,q in enumerate(WORDS)}
DIM=len(WORDS)
def gauss(q,E):return sum(E)==q[0]-1 and all(-E[b-1]==q[b] for b in (1,2,3))
assert all(gauss(q,E) for q,E in zip(WORDS,FIELDS))
assert all(max(map(abs,E))<=1 for E in FIELDS)
F=s.zeros(DIM);T=s.zeros(DIM);J={(b,c):s.zeros(DIM) for b in (1,2,3) for c in (-1,1)}
spin_transitions=[]
for col,(q,E) in enumerate(zip(WORDS,FIELDS)):
 for a,b in EDGES:
  for source,dest in ((a,b),(b,a)):
   if q[source] and not q[dest]:
    k=-q[source] if source==a else q[source]
    qq=list(q);qq[dest]=qq[source];qq[source]=0;qq=tuple(qq)
    ff=list(E);ff[b-1]+=k;ff=tuple(ff)
    assert gauss(qq,ff) and ff==FIELDS[INDEX[qq]]
    weight=1-s.Rational(E[b-1]*(E[b-1]+k),1)/C
    assert weight==1
    T[INDEX[qq],col]-=1
    if source==0:F[INDEX[qq],col]+=1
    spin_transitions.append({'kind':'hop','source_word':q,'source_field':E,'source':source,'destination':dest,'shift':k,'weight_squared':str(weight)})
  if not q[0] and not q[b]:
   for c in (-1,1):
    qq=list(q);qq[0]=c;qq[b]=-c;qq=tuple(qq)
    ff=list(E);ff[b-1]+=c;ff=tuple(ff)
    assert gauss(qq,ff) and ff==FIELDS[INDEX[qq]]
    weight=1-s.Rational(E[b-1]*(E[b-1]+c),1)/C
    assert weight==1
    J[b,c][INDEX[qq],col]=1
    spin_transitions.append({'kind':'birth','source_word':q,'source_field':E,'edge':(0,b),'charge_at_0':c,'shift':c,'weight_squared':str(weight)})
assert T==-(F+F.T)
W=s.diag(*[int(q[0]==0) for q in WORDS])
N=s.diag(*[sum(v!=0 for v in q) for q in WORDS])
E2=s.diag(*[sum(e*e for e in E) for E in FIELDS])
Dext=s.diag(*[sum(int(q[0]!=0)*int(q[b]==0)*E[b-1]*(E[b-1]-q[0]) for b in (1,2,3)) for q,E in zip(WORDS,FIELDS)])
Dspin=s.diag(*[sum(1-s.Rational(E[b-1]*(E[b-1]-q[0]),1)/C for b in (1,2,3) if q[0] and not q[b]) for q,E in zip(WORDS,FIELDS)])
Drotor=s.diag(*[sum(int(q[0]!=0 and q[b]==0) for b in (1,2,3)) for q in WORDS])
COMP=F.T*F-Dspin+Drotor
assert Dext==s.zeros(DIM) and Dspin==Drotor
M=F.T*F
assert COMP==M
assert E2==N-s.eye(DIM)+W
# Joint scaling delta/(epsilon^2 C)=K makes lambda correction ell*E2,
# where ell=lambda*K. No eigenstate property is presumed.
OMEGA=DELTA/EPS**4
H=OMEGA*(W+EPS*T+EPS**2*COMP)+ELL*E2
Q1=s.diag(*[int(sum(v!=0 for v in q)==1) for q in WORDS])
Q3=s.eye(DIM)-Q1
P=s.eye(DIM)-W
g=s.zeros(DIM,1);g[INDEX[(1,0,0,0)]]=1
fg=F*g;normal=1+3*EPS**2
psi=(g+EPS*fg)/s.sqrt(normal)
assert (fg.T*fg)[0]==3
assert s.simplify((psi.T*psi)[0])==1

def simp_matrix(mat):return mat.applyfunc(s.simplify)
def scalar(x):return s.factor(x[0])
def moments(v):
 norm=scalar(v.T*v);hv=H*v
 mean=s.factor(scalar(v.T*hv)/norm)
 second=s.factor(scalar(hv.T*hv)/norm)
 return {'norm_squared':norm,'mean':mean,'second_moment':second,'variance':s.factor(second-mean**2)}

assert simp_matrix(H*psi-ELL*EPS*fg/s.sqrt(normal))==s.zeros(DIM,1)
initial=moments(psi)
assert s.simplify(initial['mean']-3*ELL*EPS**2/normal)==0
assert s.simplify(initial['variance']-3*ELL**2*EPS**2/normal**2)==0
# Positivity factorization of the original compensated microscopic Hamiltonian.
Bfac=W-EPS*F
assert Bfac.T*Bfac==W+EPS*T+EPS**2*COMP
assert N*H==H*N
assert Q3*J[1,1]*Q3==s.zeros(DIM)
assert all(j*Q3==s.zeros(DIM) for j in J.values())
assert Q3*M*M*Q3==3*Q3*M*Q3
# Two-dimensional reachable N=1 subspace is built from the actual initial word.
u=fg/s.sqrt(3);U=g.row_join(u)
H1=simp_matrix(U.T*H*U)
assert simp_matrix(H*U-U*H1)==s.zeros(DIM,2)
results={};branch_vectors={}
for label,channels in [('resolved',J),('coherent',{b:J[b,1]+J[b,-1] for b in (1,2,3)})]:
 loss=sum((j.T*j for j in channels.values()),s.zeros(DIM))*KAPPA/EPS**2
 gain=0;rate=0;rows=[]
 for mark,j in channels.items():
  v=j*fg
  assert j*g==s.zeros(DIM,1)
  m=moments(v)
  mu=s.factor(scalar(v.T*M*v)/m['norm_squared'])
  var_m=s.factor(scalar(v.T*M*M*v)/m['norm_squared']-mu**2)
  compressed=P*H*P
  compressed_variance=s.factor(scalar((compressed*v).T*(compressed*v))/m['norm_squared']-m['mean']**2)
  omitted_variance=s.factor(m['variance']-compressed_variance)
  assert s.simplify(omitted_variance-DELTA**2*mu/EPS**6)==0 and omitted_variance!=0
  rows.append({'mark':mark,'intensity':s.factor(KAPPA*m['norm_squared']/normal),
               'M_mean':mu,'M_variance':var_m,'wrong_P_compressed_variance':compressed_variance,
               'omitted_W1_variance':omitted_variance,**m})
  rate+=KAPPA*m['norm_squared']/normal
  gain+=KAPPA*scalar(v.T*H*v)/normal
  branch_vectors[(label,str(mark))]=v
 lossterm=s.factor(scalar(psi.T*loss*H*psi))
 total=s.factor(gain-lossterm)
 # Exact source relation on the actual no-event invariant subspace.
 coeff=s.Rational(3,2)*DELTA/EPS**2+2*ELL
 injection=sum((j.T*Q3*H*Q3*j for j in channels.values()),s.zeros(DIM))*KAPPA/EPS**2
 mismatch=simp_matrix(U.T*(injection-coeff*loss)*U)
 assert mismatch==s.zeros(2)
 assert simp_matrix(loss*U-U*(U.T*loss*U))==s.zeros(DIM,2)
 # Stronger second-energy-moment relation, with no time propagation needed.
 m2coeff=s.Rational(3,2)*DELTA**2/EPS**6+s.Rational(9,2)*DELTA**2/EPS**4+6*DELTA*ELL/EPS**2+4*ELL**2
 injection2=sum((j.T*Q3*H*H*Q3*j for j in channels.values()),s.zeros(DIM))*KAPPA/EPS**2
 assert simp_matrix(U.T*(injection2-m2coeff*loss)*U)==s.zeros(2)
 results[label]={'marks':rows,'initial_rate':s.factor(rate),'initial_gain':s.factor(gain),
  'initial_loss':lossterm,'initial_full_energy_derivative':total,
  'number3_energy_per_population':coeff,'number3_second_moment_per_population':m2coeff,
  'finite_time_source_identity_on_reachable_subspace':True,'reachable_loss':U.T*loss*U}
 assert s.simplify(total-KAPPA*(18*DELTA/EPS**2+12*ELL)/normal)==0
# A dephased leaf preparation does NOT have the symmetric state's injected mean.
leaf=s.zeros(DIM,1);leaf[INDEX[(0,1,0,0)]]=1
num=sum(scalar((j*leaf).T*H*(j*leaf)) for j in J.values())
den=sum(scalar((j*leaf).T*(j*leaf)) for j in J.values())
wrong=s.factor(num/den)
assert s.simplify(wrong-(s.Rational(3,2)*DELTA/EPS**2+2*ELL))!=0
# Eigenstate mutation would suppress a real loss contribution for ell>0.
assert results['resolved']['initial_loss']!=0

def sparse_rows(mat):return [{'row':i,'column':j,'value':str(mat[i,j])} for i in range(mat.rows) for j in range(mat.cols) if mat[i,j]!=0]
def ser(v):
 if isinstance(v,dict):return {str(k):ser(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [ser(x) for x in v]
 if isinstance(v,s.MatrixBase):return [[str(x) for x in v.row(i)] for i in range(v.rows)]
 if isinstance(v,s.Basic):return str(v)
 return v
packet={'dimension':DIM,'sector_dimensions':{'N1':sum(Q1.diagonal()),'N3':sum(Q3.diagonal()),
 'N3_P':sum((Q3*P).diagonal()),'N3_W1':sum((Q3*W).diagonal())},
 'basis':[{'index':i,'q':q,'E':E,'N':sum(v!=0 for v in q),'W':int(q[0]==0)} for i,(q,E) in enumerate(zip(WORDS,FIELDS))],
 'all_legal_normalized_spin_transition_weights_one':True,'transitions':spin_transitions,
 'operators':{'F':sparse_rows(F),'T':sparse_rows(T),'C_original':sparse_rows(COMP),'W':sparse_rows(W),'E2':sparse_rows(E2),
 'D_ext':sparse_rows(Dext),'resolved_j':{str(k):sparse_rows(v) for k,v in J.items()}},
 'H_definition':'delta epsilon^-4 (W+epsilon T+epsilon^2 C_original)+ell E2; ell=lambda K',
 'H1_reachable':H1,'initial_energy_moments':initial,'instruments':results,
 'mutation_controls':{'incorrect_leaf_dephased_injection_mean':wrong,'symmetric_injection_mean':s.Rational(3,2)*DELTA/EPS**2+2*ELL,
 'dephasing_changes_answer':True,'incorrect_initial_eigenstate_assumption_has_nonzero_residual_for_ell_positive':True}}
(HERE/'EXACT_STAR_MATRIX_RESULTS.json').write_text(json.dumps(ser(packet),indent=2)+'\n')
print(json.dumps(ser({'dimension':DIM,'sector_dimensions':packet['sector_dimensions'],'initial':initial,
 'H1':H1,'resolved_selected_plus':results['resolved']['marks'][1],
 'resolved_selected_minus':results['resolved']['marks'][0],'coherent_selected':results['coherent']['marks'][0],
 'all_mark':{label:{k:v for k,v in r.items() if k!='marks'} for label,r in results.items()},'mutations':packet['mutation_controls']}),indent=2))
