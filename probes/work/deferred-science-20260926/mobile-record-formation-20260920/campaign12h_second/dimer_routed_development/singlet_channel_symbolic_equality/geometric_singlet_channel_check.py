#!/usr/bin/env python3
"""Author exact channel, coherent-filter and tiled-Gram controls."""
from pathlib import Path
import datetime,hashlib,itertools,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent

def matchings(n,edges):
 adj={v:set() for v in range(n)}
 for u,v in edges:adj[u].add(v);adj[v].add(u)
 def visit(remaining,pairs):
  if not remaining:yield tuple(pairs);return
  u=min(remaining)
  for v in sorted(adj[u]&remaining):yield from visit(remaining-{u,v},pairs+[tuple(sorted((u,v)))])
 return list(visit(set(range(n)),[]))

def covers(n,edges,black):
 ms=matchings(n,edges);bits=list(itertools.product([0,1],repeat=n));D=s.zeros(2**n,len(ms))
 for j,M in enumerate(ms):
  for i,state in enumerate(bits):
   value=1
   for u,v in M:
    if u not in black:u,v=v,u
    if state[u]==state[v]:value=0;break
    value*=1 if state[u]==0 else -1
   D[i,j]=value/s.sqrt(2**(n//2))
 return D,ms

def channel_controls():
 rows=[]
 cases=[('square',4,{(0,1),(1,2),(2,3),(0,3)},{0,2}),
        ('ladder6',6,{(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)},{0,2,4}),
        ('cube8',8,{(a,b) for a,b in itertools.combinations(range(8),2) if a^b in [1,2,4]},{0,3,5,6})]
 for name,n,edges,black in cases:
  D,ms=covers(n,edges,black);G=D.T*D;count=len(ms)
  assert all(G[i,i]==1 for i in range(count)) and all(g>0 for g in G)
  # General pure-output Choi coefficient C must satisfy G.T Hadamard C=I.
  # The coefficients are solved independently as scalar linear equations.
  symbols=s.symbols('c:'+str(count*count));C=s.Matrix(count,count,symbols)
  solution=s.linsolve([C[i,j]*G[j,i]-int(i==j) for i in range(count) for j in range(count)],symbols)
  assert solution==s.FiniteSet(s.Tuple(*list(s.eye(count))))
  # The explicit measure-and-prepare Kraus family has a TP sum and orthogonal
  # vectorized Kraus columns, so its Choi matrix is positive with rank count.
  kraus=[D[:,j]*s.eye(count)[j,:] for j in range(count)]
  assert sum((L.T*L for L in kraus),s.zeros(count))==s.eye(count)
  assert s.Matrix([[s.trace(L.T*Q) for Q in kraus] for L in kraus])==s.eye(count)
  c=s.Matrix([s.Integer(j+1)+s.I*(j%2) for j in range(count)])
  norm=(c.conjugate().T*c)[0];rho=c*c.conjugate().T/norm
  out=sum((L*rho*L.conjugate().T for L in kraus),s.zeros(2**n))
  expected=D*s.diag(*[rho[j,j] for j in range(count)])*D.T
  assert out==expected and s.trace(out)==1
  row_sum=[sum(G.row(i)) for i in range(count)];upper=max(row_sum)
  # Rational sufficient coherent-filter normalization; positivity checked
  # exactly through the eigenvalues of its small input-side Gram defect.
  defect=s.eye(count)-G/upper;eigen=defect.eigenvals()
  assert all(value.is_nonnegative for value in eigen)
  uniform_success=s.factor(sum(G)/(count*upper))
  assert 0<uniform_success<=1
  eigen_num=np.linalg.eigvalsh(np.array(G,dtype=float))
  optimum_uniform=float(sum(G)/count)/eigen_num[-1]
  rows.append(dict(graph=name,physical_qubits=n,matchings=count,Gram=str(G),
    exact_TP_pure_output_coefficient_solution='identity',exact_measure_prepare_Choi_rank=count,
    exact_row_sums=list(map(str,row_sum)),rational_filter_scale_squared=str(1/upper),
    exact_filter_defect_eigenvalues={str(k):v for k,v in eigen.items()},
    rational_filter_uniform_success=str(uniform_success),
    numerical_lambda_max=float(eigen_num[-1]),numerical_optimal_uniform_success=optimum_uniform))
  if name=='square':
   plus=D*s.ones(count,1);plus=plus/s.sqrt((plus.T*plus)[0]);coherent=plus*plus.T
   mixed=D*D.T/count;difference=coherent-mixed
   nonzero={s.factor(k):v for k,v in difference.eigenvals().items() if k!=0}
   assert nonzero=={s.Rational(1,4):1,-s.Rational(1,4):1}
   assert uniform_success==1 and 1/upper==s.Rational(2,3)
   rows[-1]['exact_coherent_vs_mixture_trace_distance']='1/4'
 return rows

def tile_controls():
 rows=[];G2=s.Matrix([[1,s.Rational(1,2)],[s.Rational(1,2),1]])
 for P in [1,2,3,4,5,6]:
  labels=list(itertools.product([0,1],repeat=P))
  G=s.Matrix([[s.Rational(1,2)**sum(x!=y for x,y in zip(a,b)) for b in labels] for a in labels])
  expected=G2
  for _ in range(P-1):expected=s.kronecker_product(expected,G2)
  assert G==expected
  lam=s.Rational(3,2)**P;v=s.ones(2**P,1)
  assert G*v==lam*v and all(sum(G.row(i))==lam for i in range(2**P))
  # All eigenvalues follow from the two exact single-tile eigenvectors.
  spectrum={str(s.Rational(3,2)**(P-j)*s.Rational(1,2)**j):__import__('math').comb(P,j) for j in range(P+1)}
  assert sum(spectrum.values())==2**P
  assert G2*s.Matrix([1,-1])==s.Rational(1,2)*s.Matrix([1,-1])
  rows.append(dict(tiles=P,coverings=2**P,exact_top_eigenvalue=str(lam),
    exact_basis_success=str(1/lam),exact_uniform_coherent_success='1',
    product_eigenvalues=spectrum))
 # Verify that the proposed plaquettes tile actual finite even cubic tori.
 coverage=[]
 for N in [4,6,8,10]:
  seen=set();plaquettes=[]
  for x in range(0,N,2):
   for y in range(0,N,2):
    for z in range(N):
     q=[(x,y,z),(x+1,y,z),(x+1,y+1,z),(x,y+1,z)]
     assert not seen.intersection(q);seen.update(q)
     for pairing in [[(q[0],q[1]),(q[2],q[3])],[(q[0],q[3]),(q[1],q[2])]]:
      assert len({v for e in pairing for v in e})==4
      for a,b in pairing:assert sum(abs(a[i]-b[i]) for i in range(3))==1 and (sum(a)-sum(b))%2
     plaquettes.append(q)
  assert len(seen)==N**3 and len(plaquettes)==N**3//4
  coverage.append(dict(N=N,sites=len(seen),plaquettes=len(plaquettes),exact_disjoint_NN_cover=True))
 return dict(product_Grams=rows,cubic_tiling_inventory=coverage)

def premise_countercontrols():
 # Orthogonal target outputs admit a coherent identity channel: the nonzero
 # overlap premise is essential, so the conclusion is not a blanket ban.
 G=s.eye(2);C=s.ones(2)
 assert G.multiply_elementwise(C)==s.eye(2) and C.eigenvals()=={2:1,0:1}
 # A selected physical target may be prepared by a constant channel, which
 # is not required to map both matching basis inputs to their own covering.
 D,_=covers(4,{(0,1),(1,2),(2,3),(0,3)},{0,2})
 target=D*s.ones(2,1);target/=s.sqrt((target.T*target)[0])
 L=[target*s.eye(2)[j,:] for j in range(2)]
 assert sum((k.T*k for k in L),s.zeros(2))==s.eye(2)
 assert all(k*s.eye(2)[:,j]==(target if i==j else s.zeros(16,1)) for i,k in enumerate(L) for j in range(2))
 return dict(orthogonal_output_coherence_preserved=True,specified_single_state_direct_preparation_allowed=True,
   limitation='Neither control supplies local dynamics or a physical implementation from the record axioms.')

def main():
 out=HERE/'geometric_singlet_channel_checks';out.mkdir(exist_ok=False)
 groups=[]
 for name,fn in [('channels_and_filters',channel_controls),('tiled_Gram_bound',tile_controls),('changed_premise_controls',premise_countercontrols)]:
  value=fn();groups.append(dict(group=name,passed=True,detail=value));print(name,'PASS',flush=True)
 sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in [Path(__file__).name,'GEOMETRIC_SINGLET_CHANNEL_AND_COHERENT_FILTER.md']}
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources_sha256=sources,groups=groups,
   scope='Conditional quantum-operation controls. Exact rational/algebraic statements separated from labelled numerical maximal eigenvalues. No microscopic channel, state preparation or quantum photon derived.')
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
