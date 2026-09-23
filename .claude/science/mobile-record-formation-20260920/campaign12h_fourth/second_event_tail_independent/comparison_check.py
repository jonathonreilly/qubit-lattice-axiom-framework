"""Bounded post-PRE tail comparison; no author module imported or executed."""
from pathlib import Path
import ast, cmath, hashlib, json, math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import expm
D=Path(__file__).resolve().parent;A=D.parent/'second_event_tail_author'
def identity(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(r):assert identity(Path(r['path']))==r,r['path']
pre_path=D/'PRE_COMPARISON_SEAL.json';author_path=A/'AUTHOR_SEAL.json'
assert identity(pre_path)['sha256']=='0aac7b39eefeacd4464660b824af56638ed05f30865abcc2cd16024a756bbb2c'
assert identity(author_path)['sha256']=='0ffc4d68970054377f6b80c4b5cc0ec593d38380944d8e5d202a6aa0090648c7'
pre=json.loads(pre_path.read_text());author=json.loads(author_path.read_text())
for r in pre['sources']+pre['artifacts']+author['sources']+author['artifacts']:check(r)
result=json.loads((A/'TAIL_AND_MOMENT_RESULTS.json').read_text())
receipt=json.loads((A/'CHECK_RUN_RECEIPT.json').read_text())
assert receipt['exit_code']==0
assert receipt['source_sha256']==result['source_sha256']==identity(A/'tail_moment_check.py')['sha256']
assert result['dependency_report_sha256']==author['sources'][0]['sha256']
assert (A/'CHECK.stdout.log').read_bytes()==(A/'TAIL_AND_MOMENT_RESULTS.json').read_bytes()
assert not (A/'CHECK.stderr.log').read_bytes()

# Solve for the unknown Hermitian matrices rather than importing author X,Y.
k,w=sp.symbols('k w',positive=True,real=True)
x,y,z=sp.symbols('x y z',real=True)
K=sp.Matrix([[-2*k,sp.I*w],[sp.I*w,0]])
trial=sp.Matrix([[x,-sp.I*y],[sp.I*y,z]])
solx=sp.solve(list(K.conjugate().T*trial+trial*K+sp.eye(2)),(x,y,z),dict=True)[0]
X=trial.subs(solx)
soly=sp.solve(list(K.conjugate().T*trial+trial*K+2*X),(x,y,z),dict=True)[0]
Y=trial.subs(soly)
authorX=sp.Matrix([[1/(2*k),-sp.I/(2*w)],[sp.I/(2*w),1/(2*k)+k/w**2]])
authorY=sp.Matrix([[(k*k+w*w)/(2*k*k*w*w),-sp.I*(2*k*k+w*w)/(2*k*w**3)],
 [sp.I*(2*k*k+w*w)/(2*k*w**3),(4*k**4+k*k*w*w+w**4)/(2*k*k*w**4)]])
assert (X-authorX).applyfunc(sp.simplify)==sp.zeros(2)
assert (Y-authorY).applyfunc(sp.simplify)==sp.zeros(2)
assert str(authorX)==result['symbolic_mean_matrix'] and str(authorY)==result['symbolic_second_moment_matrix']

# Load only our own sealed function definitions, never its output-writing code.
tree=ast.parse((D/'tail_check.py').read_text())
defs=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[])
env={'cmath':cmath,'math':math,'quad':quad}
exec(compile(defs,'PRE_independent_functions','exec'),env)
f=env['f'];controls=[]
for r in result['two_state_controls']:
 om=r['omega'];time=r['t'];kap=.9
 observed=float(np.linalg.norm(expm(time*np.array([[-2*kap,1j*om],[1j*om,0]],complex))@np.array([1,0]))**2)
 independent=f(om,kap,time)
 error=max(abs(observed-r['matrix_norm']),abs(independent-r['stable_formula']))
 assert error<2e-12 and abs(abs(r['matrix_norm']-r['stable_formula'])-r['absolute_error'])<1e-30
 controls.append({**r,'independent_stable_formula':independent,'independent_matrix':observed,'max_difference':error})

# For g=1+sigma*cos(theta), resolved clocks fold to the uniform arcsine
# integral. Coherent clocks have weight 1+(sigma/2)*cos(4v). This follows
# by averaging the four theta -> theta+pi/2 translates and is independent
# of the author's six-branch quadrature near four angular singularities.
tails=[];a=4.2;kap=.9;O=math.sqrt(8)*a
signs={'one_flux':0,'neighbor_plus':1,'neighbor_minus':-1}
for r in result['long_time_quadrature']:
 sigma=signs[r['field']] if r['coherent'] else 0
 time=r['t'];cut=min(math.pi/2,9*math.sqrt(kap)/(O*math.sqrt(time)))
 def integrand(v):return time**1.5*(1+sigma*math.cos(4*v)/2)*f(O*math.sin(v),kap,time)/math.pi
 v1,e1=quad(integrand,0,cut,epsabs=1e-13,epsrel=2e-12)
 v2,e2=quad(integrand,cut,math.pi/2,epsabs=1e-13,epsrel=2e-12)
 value=.5*time**1.5*math.exp(-4*kap*time)+v1+v2
 coefficient=(1+sigma/2)/(32*a*math.sqrt(2*math.pi*kap))
 assert abs(value-r['scaled_survival_t_power_3_over_2'])<2e-10
 assert abs(coefficient-r['analytic_coefficient'])<2e-18
 assert abs((r['scaled_survival_t_power_3_over_2']/r['analytic_coefficient']-1)-r['relative_difference'])<2e-16
 tails.append({**r,'independent_frequency_integral':value,'independent_quad_error':e1+e2,
               'independent_coefficient':coefficient,'absolute_difference':abs(value-r['scaled_survival_t_power_3_over_2'])})

cutrows=[]
for r in result['excision_moment_controls']:
 cut=r['angular_excision_radius']
 exact=3/(4*math.pi*a*a*math.tan(2*cut));limit=3/(8*math.pi*a*a)
 assert abs(exact-r['exact_cut_formula'])<1e-15
 assert abs(exact-r['second_moment_positive_singular_part'])<1e-10
 assert abs(cut*r['second_moment_positive_singular_part']-r['radius_times_singular_part'])<1e-16
 assert abs(limit-r['limiting_cut_coefficient'])<1e-17
 cutrows.append({**r,'independent_exact_formula':exact})

out={'status':'Source-informed comparison, no author builder executed; no required mathematical correction found.',
 'PRE':identity(pre_path),'author_seal':identity(author_path),
 'authenticated_PRE_sources':len(pre['sources']),'authenticated_PRE_artifacts':len(pre['artifacts']),
 'authenticated_author_sources':author['sources'],'authenticated_author_artifacts':author['artifacts'],
 'author_receipt':receipt,'author_scope':result['scope'],
 'solved_mean_matrix':str(X),'solved_second_moment_matrix':str(Y),
 'all_two_state_controls':controls,'max_two_state_difference':max(r['max_difference'] for r in controls),
 'all_tail_controls':tails,'max_tail_scaled_difference':max(r['absolute_difference'] for r in tails),
 'all_excision_controls':cutrows,
 'scope_distinction':'Our full Laplace law, positive-moment integrability criterion, regularized-density and coherent-cancellation examples remain separately derived additions.',
 'limits':['The author only claims the t^(-3/2) coefficient for continuous densities with positive stated sum.',
           'The a=0 exception is explicit. No merely-L1 tail law, joint finite-spin limit, or microscopic long-time extension is claimed.',
           'Full author source and results read; success streams/receipt authenticated, not a replay of author execution.',
           'No other author folder, campaign plan/checkpoint, finite-spin source, Git, publication or audit action.']}
p=D/'COMPARISON_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
