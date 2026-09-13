from pathlib import Path
import sympy as s,json
P=Path(__file__).resolve().parent
A,B=s.symbols('A B',real=True);I=s.I
on=s.Matrix([[B,A],[A,-B]]);hop=s.Matrix([[-1,-1],[1,1]])/2
hs=[]
for phase in [1,I,-1]:
 h=s.zeros(4);h[:2,:2]=on;h[2:,2:]=on;h[:2,2:]=phase*hop;h[2:,:2]=s.conjugate(phase)*hop.T;hs.append(h)
order=5;zero=s.zeros(4)
def simp(m):return m.applyfunc(s.expand)
def mul(a,b):return [simp(sum((a[j]*b[k-j] for j in range(k+1)),zero.copy())) for k in range(order+1)]
coeff=[s.eye(4)]+[zero.copy() for _ in range(order)]
for h in hs:
 powers=[s.eye(4)]
 for k in range(1,order+1):powers.append(simp(-h*powers[-1]/k))
 coeff=mul(powers,coeff)
x=[zero.copy()]+[c/2 for c in coeff[1:]];power=x;logs=[s.S(0)]*(order+1)
for r in range(1,order+1):
 for k in range(1,order+1):logs[k]+=s.Rational((-1)**(r+1),r)*s.trace(power[k])
 if r<order:power=mul(power,x)
logs=[s.factor(v) for v in logs]
print(logs)
(P/'BLOCK12_GENERAL_PHASE_COEFFICIENT.json').write_text(json.dumps(dict(log_weight_coefficients=[str(v) for v in logs]),indent=2)+'\n')
