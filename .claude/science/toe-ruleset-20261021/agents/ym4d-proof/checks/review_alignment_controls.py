"""Preserved finite reproductions and deliberate negative controls."""
from pathlib import Path
from fractions import Fraction as F
import subprocess,json,hashlib,time
base=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks')
rev='962f97c259d8c241df632a07e27f498f4ad33b09'
source=subprocess.check_output(['git','show',rev+':'+str(base/'recovery_align_exact.py')]).decode()
assert hashlib.sha256(source.encode()).hexdigest()=='72fbf46b0563a0246240f26d7802294911a00131b047ad1b82823eb1f0aebefa'
mutations={
 'author_original':None,
 'author_mutant_harmonic':('img=[[z-sum(row)/n for z in row] for row in merged]','img=merged'),
 'author_mutant_S1_normalization':('shift=(F(1,L)-sum(r))/m','shift=(F(1)-sum(r))/m'),
 'author_mutant_midpoint':('(2*base[j]+(a==j))','(2*base[j])'),
 'author_mutant_coarse_sign':('return plus(bp,cross(by,avtop))','return plus(bp,times(-1,cross(by,avtop)))'),
 'author_mutant_uncentered':('def contour_kernel(d,L,nu,center=True):','def contour_kernel(d,L,nu,center=False):'),
}
results={}
for name,replacement in mutations.items():
    body=source
    if replacement:
        a,b=replacement;assert body.count(a)==1,(name,body.count(a));body=body.replace(a,b)
    p=base/('review_alignment_'+name+'.py');p.write_text(body)
    start=time.monotonic();run=subprocess.run(['python3','-I','-B',str(p)],capture_output=True)
    elapsed=time.monotonic()-start
    (base/('review_alignment_'+name+'_out.txt')).write_bytes(run.stdout)
    (base/('review_alignment_'+name+'_err.txt')).write_bytes(run.stderr)
    results[name]={'exit_code':run.returncode,'elapsed_seconds':elapsed,'expected':'success' if replacement is None else 'assertion failure','actual_stdout_bytes':len(run.stdout),'actual_stderr_bytes':len(run.stderr)}
    assert (run.returncode==0)==(replacement is None),(name,run.returncode)
    if replacement:assert b'AssertionError' in run.stderr,(name,run.stderr)
# Exact rational-complex historical BA5 counterexample; no polar numerical solver.
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def power(a,n):
    if n<0:a=(a[0],-a[1]);n=-n
    out=(F(1),F(0))
    for _ in range(n):out=mul(out,a)
    return out
t=F(1,1000);z=((1-t*t)/(1+t*t),2*t/(1+t*t))
assert z[0]**2+z[1]**2==1
m=[((2+power(z,n)[0])/3,power(z,n)[1]/3) for n in (1,2,-3)]
det=mul(mul(m[0],m[1]),m[2]);sq=[a*a+b*b for a,b in m]
assert det[1]!=0 and len(set(sq))==3
assert 56*t*t<F(1,400) # squared logarithm norm bound <(1/20)^2
results['BA5_exact_counterexample']={'t':str(t),'determinant_real':str(det[0]),'determinant_imaginary_nonzero':str(det[1]),'distinct_singular_values_squared':list(map(str,sq)),'logarithm_HS_squared_upper_bound':str(56*t*t),'interpretation':'Scalar determinant phase times U(3) polar factor violates SU(3) stationarity; BA5 quadratic conclusion is independently recoverable.'}
print(json.dumps(results,indent=2))
