"""Post-exposure correspondence checks; author formulas transcribed after freeze."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "independent_attempt01.stdout.json",
    "AUTHOR_SOURCE_SNAPSHOT_v1.json",
]
from pathlib import Path
import json
import sys
import sympy as s
here=Path(__file__).resolve().parent
own=json.loads((here/AUDIT_INPUT_PATHS[0]).read_text())
snapshot=json.loads((here/AUDIT_INPUT_PATHS[1]).read_text())
author=json.loads(snapshot["sources"]["MATTER_CLOCK_CONTROLS_v1.json"]["utf8"])
x,y,z=s.symbols("x x1 x2",real=True)
h,h1,h2,h3,b,b1,b2,b3,k,k1=s.symbols("h h1 h2 h3 b b1 b2 b3 kappa kappa1",real=True)
all_symbols=[x,y,z,h,h1,h2,h3,b,b1,b2,b3,k,k1]
names={str(v):v for v in all_symbols}
read=lambda text:s.sympify(text,locals=names)
Nown=read(own["algebra"]["numerator"])
Delta=read(own["algebra"]["denominator"])
Pown=read(own["algebra"]["polynomial"])
dt=lambda f:sum(s.diff(f,a)*v for a,v in [(h,h1),(h1,h2),(h2,h3),(b,b1),(b1,b2),(b2,b3),(k,k1)])
r0=2*b1*x-2*h1-2*b*h*x+(2*b*b-1)*x*x
R=2*b*y+r0
B1=3*h-2*b*x-6*b*b*(h-b*x)
B0=(3*h1+k-2*b1*x+6*h*b*x-4*b*b*x*x)*x-3*b*(h-b*x)*r0
C=-2*((6*b**4-2*b*b+1)*x+b*(1-6*b*b)*h-2*b1)
N=dt(r0)+(3*h-2*b*x)*r0-2*b*B0
Q=s.expand(-dt(N)*C*C+N*dt(C)*C+N*s.diff(N,x)*C-N*N*s.diff(C,x)-B1*N*C*C+B0*C**3)
rows=[]
def zero(name,expr):
    residual=s.factor(s.cancel(expr));ok=residual==0
    rows.append({"name":name,"pass":bool(ok),"residual":str(residual)})
    print(("PASS " if ok else "FAIL ")+name,file=sys.stderr,flush=True)
zero("author C is minus twice independent Delta",C+2*Delta)
zero("author N is twice independent numerator",N-2*Nown)
zero("author entire Q is minus eight times independent P",Q+8*Pown)
zero("author primary leading coefficient agrees with independent result",
     s.sympify(author["leading_coefficient"],locals=names)+8*read(own["algebra"]["degree_six_coefficient"]))
refl={x:-x,b:-b,b1:-b1,b2:-b2,b3:-b3}
zero("reflection of author C",C.xreplace(refl)+C)
zero("reflection of author N",N.xreplace(refl)-N)
zero("reflection of entire filter",Q.xreplace(refl)-Q)
T=s.symbols("tau",positive=True)
simple={h:1/T,h1:-1/T**2,h2:2/T**3,h3:-6/T**4,b:1,b1:0,b2:0,b3:0,k:s.Rational(7,4)/T**2,k1:-s.Rational(7,2)/T**3}
simple_expected=s.sympify(author["simple_fixture_polynomial"],locals={**names,"tau":T})
zero("author receipt simple polynomial agrees with formula",Q.subs(simple)-simple_expected)
witness={h:s.Rational(14,19)/T,h1:-s.Rational(14,19)/T**2,h2:s.Rational(28,19)/T**3,h3:-s.Rational(84,19)/T**4,
         b:s.Rational(1,2),b1:0,b2:0,b3:0,k:s.Rational(2410,361)/T**2,k1:-s.Rational(4820,361)/T**3,
         x:s.Rational(4,19)/T,y:-s.Rational(4,19)/T**2,z:s.Rational(8,19)/T**3}
zero("independent positive witness lies on author C zero",C.subs(witness))
zero("independent witness also has author N zero",N.subs(witness))
zero("independent witness retains positive author density",R.subs(witness)-s.Rational(392,361)/T**2)
zero("independent witness obeys author undivided scalar", (z+B1*y+B0).subs(witness))
zero("independent witness obeys author filter",Q.subs(witness))
ao,ae=s.symbols("a_observer a_emitter",positive=True)
ho,he=s.symbols("h_observer h_emitter",real=True)
zp=ao/ae
drift=s.diff(zp,ao)*ho*ao+s.diff(zp,ae)*he*ae*(ae/ao)
zero("conditional FLRW matter-clock redshift drift",drift-(zp*ho-he))
r,AA,MM=s.symbols("r A M",positive=True)
zero("physical density over F equals author R",(r/AA**4)/(MM**2/AA**2)-r/(MM**2*AA**2))
out={"scope":"Post-author-exposure formula correspondence, conditional redshift kinematics, and independent singular witness; no external literature or empirical test",
     "checks":rows,"summary":{"passed":sum(c["pass"] for c in rows),"failed":sum(not c["pass"] for c in rows)},
     "source_note_sha256":snapshot["sources"]["MATTER_CLOCK_DERIVATION_v1.md"]["sha256"],
     "author_code_imported":False,"software":{"python":sys.version.split()[0],"sympy":s.__version__}}
print(json.dumps(out,indent=2))
raise SystemExit(int(out["summary"]["failed"]!=0))
