"""T174 - THE RECORD DRAW DOES NOT CONTRACT THE MEAN.  Correcting T168/R102.

T168 measured that sampling a record contracts the mean by exactly 1/3, and R102
built a correlation-length argument on it.  That is wrong, and the error is
elementary once seen.

I sampled from P(n) proportional to (1 + 2 v.n), calling it 'the Born measure for
rho'.  But that distribution's OWN mean is
      <(1/2) n>  =  (1/2)(a/3)  with a = 2v   =   v/3,
NOT v.  So I was drawing from a distribution whose mean is v/3 and then reporting,
correctly, that its mean is v/3.  The measurement was self-consistent and answered
the wrong question.

The right statement is a tautology once the roles are straight: the admissibility
rule outputs a DISTRIBUTION whose mean is v_out; a record is a DRAW from it; so
     <v_record>  =  v_out    exactly, by definition of the mean.
THE DRAW PRESERVES THE MEAN.  Whatever contraction exists comes from the CHANNEL
(the factor alpha), not from the act of recording.

Two things to check, because this reverses a recorded result:
 (1) build a distribution on pure states whose mean really is v, and confirm the
     draw returns v;
 (2) find the family: P(n) ~ (1 + a.n) has mean a/6 in units of (1/2)n, so
     reaching |v| requires |a| = 6|v|, and non-negativity needs |a| <= 1 --
     hence |v| <= 1/6 in the l<=1 truncation.  Reaching a PURE record, |v| = 1/2,
     therefore needs the full harmonic tower, i.e. a point mass.  Check that too,
     because it says what 'locks exactly one possibility' costs."""
import numpy as np
rng=np.random.default_rng(9)
def sample_linear(a,N):
    """draw n on S^2 with density proportional to (1 + a.n), |a| <= 1"""
    out=[]
    while len(out)<N:
        n=rng.normal(size=3); n/=np.linalg.norm(n)
        if rng.uniform()<= (1+np.dot(a,n))/2.0: out.append(n)
    return np.array(out)
print("T174  does drawing a record preserve the mean?")
print()
print("(1) distribution with density (1 + a.n): its mean of (1/2)n should be a/6")
print(f"   {'|a|':>6} {'measured <(1/2)n>':>20} {'a/6':>10} {'ratio':>8}")
for am in (0.9,0.6,0.3):
    a=np.array([0,0,am]); S=sample_linear(a,120000)
    m=0.5*S.mean(axis=0)
    print(f"   {am:6.2f} {m[2]:20.6f} {am/6:10.6f} {m[2]/(am/6):8.4f}")
print()
print("   so to have mean v the density must be (1 + 6v.n), and non-negativity")
print("   |6v| <= 1 caps the l<=1 family at |v| <= 1/6 = 0.1667")
print()
print("(2) CONFIRM the draw preserves the mean when the distribution is built correctly")
print(f"   {'target v':>10} {'measured <v_record>':>22} {'error':>10}")
for vt in (0.05,0.10,0.15):
    a=np.array([0,0,6*vt])
    if np.linalg.norm(a)>1: print(f"   {vt:10.3f}  not representable at l<=1 (|6v|>1)"); continue
    S=sample_linear(a,200000); m=0.5*S.mean(axis=0)
    print(f"   {vt:10.3f} {m[2]:22.6f} {abs(m[2]-vt):10.6f}")
print()
print("(3) what a PURE record costs: |v| = 1/2 needs a point mass, i.e. all harmonics")
print(f"   l<=1 ceiling      |v| <= 1/6 = {1/6:.4f}")
print(f"   pure record       |v|  = 1/2 = {0.5:.4f}")
print(f"   ratio             {0.5/(1/6):.1f}x beyond what the dipole alone can reach")
print()
print("   CONSEQUENCE: the draw is mean-preserving, so the per-step contraction is")
print("   the channel's alpha alone -- T168's 1/3 was an artifact of my sampling")
print("   distribution, and R101's flat response was RIGHT.")
