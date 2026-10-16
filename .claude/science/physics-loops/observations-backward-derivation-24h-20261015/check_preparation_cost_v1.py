"""Exact sharp readout amplification bound for preparation interpolation."""
from pathlib import Path
import json,hashlib
import numpy as np
import sympy as s
p=Path(__file__).resolve().parent
checks=[]
def ck(n,b,d=None):checks.append(dict(name=n,passed=bool(b),detail=d))
a,b=s.symbols("a b",positive=True)
N=a*a/(b*b-a*a);P=1+N
ck("annulus normalization",s.simplify(P-N-1)==0)
ck("radial-moment matching",s.simplify(P*a*a-N*b*b)==0)
ck("L1 sharp formula",s.simplify(P+N-(b*b+a*a)/(b*b-a*a))==0)
def design(f):
 x=f.real;y=f.imag
 return np.array([np.ones_like(x),x,y,x*x,x*y,y*y])
e=np.array([1.,0,0,0,0,0])
out=[]
for ratio in [1.01,1.05,1.1,1.5,2,5,10]:
 r0=.2;r1=r0*ratio
 f=np.r_[r0*np.array([1,1j,-1,-1j]),r1*np.array([1,1j,-1,-1j])]
 neg=r0*r0/(r1*r1-r0*r0);pos=1+neg;u=np.r_[np.full(4,pos/4),np.full(4,-neg/4)]
 lower=(r1*r1+r0*r0)/(r1*r1-r0*r0)
 ck("sharp moment witness ratio"+str(ratio),np.max(abs(design(f)@u-e))<1e-12)
 ck("sharp norm ratio"+str(ratio),abs(np.linalg.norm(u,1)-lower)<1e-11)
 eps=1e-4; aligned=eps*np.sign(u)
 ck("attained readout error ratio"+str(ratio),abs(u@aligned-eps*lower)<1e-14)
 out.append(dict(radius_ratio=ratio,minimum_L1=lower,worst_error=eps*lower))
orig=json.loads((p/'PREPARATION_BRIDGE_CONTROLS_v1.json').read_text())
for i,h in enumerate(orig["details"]["histories"]):
 f=np.array([complex(*z) for z in h["prefix_coordinates"]]);u=np.array(h["weights"]);r0=min(abs(f));r1=max(abs(f))
 lower=(r1*r1+r0*r0)/(r1*r1-r0*r0)
 ck("author design obeys lower bound"+str(i),np.linalg.norm(u,1)+1e-12>=lower,dict(actual=float(np.linalg.norm(u,1)),lower=float(lower)))
result={"summary":{"passed":sum(x["passed"] for x in checks),"failed":sum(not x["passed"] for x in checks)},"checks":checks,"details":out,"source_hashes":{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ["PREPARATION_BRIDGE_v2.md","PREPARATION_BRIDGE_CONTROLS_v1.json",Path(__file__).name]},"empirical_validation":False}
print(json.dumps(result,indent=2))
raise SystemExit(bool(result["summary"]["failed"]))
