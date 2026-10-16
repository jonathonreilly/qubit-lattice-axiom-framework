"""One author exact q=1,L=3 discriminator, not a pulse simulation or review."""
import json
import platform
import sympy as s

I=s.I
M=5
eye=s.eye(2)
Y=s.Matrix([[0,-I],[I,0]])
n=s.diag(0,1)

def at(a,j):
    return s.kronecker_product(*[a if k==j else eye for k in range(M)])

E=s.eye(2**M)
N=sum((at(n,j) for j in range(M)),s.zeros(2**M))
vac=s.zeros(2**M,1);vac[0]=1
target=s.zeros(2**M,1)
for bits,amp in [('10000',s.Rational(1,2)),('11000',1/s.sqrt(2)),('11100',s.Rational(1,2))]:
    target[int(bits,2)]=amp

def controlled(c,ss,j):
    P=at(n,j)
    return E-P+P*(c*E-I*ss*at(Y,j+1))

flip=-I*at(Y,0)
c1=s.Rational(1,2);s1=s.sqrt(3)/2
c2=s.sqrt(s.Rational(2,3));s2=1/s.sqrt(3)
R1=controlled(c1,s1,0)
R2=controlled(c2,s2,1)
actual=s.simplify(R2*R1*flip*vac)
assert actual==target
assert s.simplify((actual.H*actual)[0])==1
assert s.simplify((actual.H*N*actual)[0])==2
assert s.simplify((actual.H*N*N*actual)[0]-4)==s.Rational(1,2)

# Exact final free-phase cancellation for x=pi/2 and lambda=7pi/2.
free=s.diag(*[(-I)**int(N[j,j]) for j in range(2**M)])
correction=s.diag(*[I**int(N[j,j]) for j in range(2**M)])
assert free*correction==E
assert free*correction*actual==target
overlap=(target.H*free*actual)[0]
missing_phase_trace_squared=s.simplify(4*(1-s.Abs(overlap)**2))
assert missing_phase_trace_squared==3

# A positive but wrongly phased controlled pulse, theta P(I+Y), on edge2.
# exp(-i theta)=c2-i s2; the controlled branch phase is physically observable.
P=at(n,1)
wrong2=E-P+(c2-I*s2)*P*(c2*E-I*s2*at(Y,2))
wrong=s.simplify(wrong2*R1*flip*vac)
ov=s.simplify((target.H*wrong)[0])
wrong_phase_trace_squared=s.simplify(4*(1-s.expand_complex(ov*s.conjugate(ov))))
assert s.simplify(wrong_phase_trace_squared-s.Rational(3,2)*(1-c2))==0
assert wrong_phase_trace_squared.is_positive is True

# Reversing both rotation axes changes relative signs: it is not a global phase.
wrong_axis=s.simplify(controlled(c2,-s2,1)*controlled(c1,-s1,0)*flip*vac)
assert s.simplify((target.H*wrong_axis)[0])==0

# Direct 4x4 spectral check: removing the 2pi reserve preserves the desired
# exponential convention only at the expense of positivity.
a=s.Symbol('a',positive=True,real=True)
correct_Q=s.kronecker_product(n,2*s.pi*eye+a*Y)
bare_Q=s.kronecker_product(n,a*Y)
assert correct_Q.eigenvals()=={0:2,2*s.pi-a:1,2*s.pi+a:1}
assert bare_Q.eigenvals()=={0:2,-a:1,a:1}

print(json.dumps({
    'status':'PASS author exact finite discriminator',
    'python':platform.python_version(),'sympy':s.__version__,
    'q':1,'L':3,'M':M,'physical_dimension':2**M,
    'output':'exact full battery vector including phase',
    'mean_number':'2','variance_number':'1/2',
    'missing_final_phase_trace_norm_squared':str(missing_phase_trace_squared),
    'wrong_positive_conditional_phase_trace_norm_squared':str(wrong_phase_trace_squared),
    'reversed_axis_trace_norm_squared':'4',
    'bare_generator_negative_eigenvalue':'-a for a>0',
    'limits':'No propagation of time-dependent laboratory pulses; no general-L numerical proof; no independent check or microscopic driver.'
},indent=2))
