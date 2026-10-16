"""Exact rational Bernstein bounds for computed primitive harmonic kernels."""
AUDIT_TIMEOUT_SEC = 120
from fractions import Fraction as Q
from math import comb
import sympy as s


def run_checks(context):
    checks=[]
    def test(name,ok):checks.append({"name":name,"pass":bool(ok)})
    x,y=s.symbols("x y",real=True)
    def bernstein(poly):
        pp=s.Poly(s.expand(poly),x,y);n,m=pp.degree_list()
        aa=[[Q(0) for j in range(m+1)] for i in range(n+1)]
        for (i,j),v in pp.terms():aa[i][j]=Q(int(v.p),int(v.q))
        bb=[[Q(0) for j in range(m+1)] for i in range(n+1)]
        cc=[[Q(0) for j in range(m+1)] for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                bb[i][j]=sum((aa[k][j]*Q(comb(i,k),comb(n,k)) for k in range(i+1)),Q(0))
        for i in range(n+1):
            for j in range(m+1):
                cc[i][j]=sum((bb[i][k]*Q(comb(j,k),comb(m,k)) for k in range(j+1)),Q(0))
        return cc
    def split_curve(v):
        a=list(v);left=[a[0]];right=[a[-1]]
        while len(a)>1:
            a=[(a[i]+a[i+1])/2 for i in range(len(a)-1)]
            left.append(a[0]);right.append(a[-1])
        return left,list(reversed(right))
    def split_square(b):
        n=len(b);m=len(b[0])
        left=[[Q(0)]*m for _ in range(n)];right=[[Q(0)]*m for _ in range(n)]
        for j in range(m):
            lo,hi=split_curve([b[i][j] for i in range(n)])
            for i in range(n):left[i][j]=lo[i];right[i][j]=hi[i]
        out=[]
        for side in (left,right):
            low=[];high=[]
            for row in side:
                lo,hi=split_curve(row);low.append(lo);high.append(hi)
            out.extend([low,high])
        return out
    def envelope(cells,area):
        low=Q(0);high=Q(0)
        for b in cells:
            den=len(b)*len(b[0])
            low+=area*abs(sum((z for row in b for z in row),Q(0)))/den
            high+=area*sum((abs(z) for row in b for z in row),Q(0))/den
        return low,high
    def ladder(poly,levels):
        cells=[bernstein(poly)];area=Q(1);out=[]
        for level in range(levels+1):
            lo,hi=envelope(cells,area)
            out.append((lo,hi))
            if level<levels:
                cells=[child for b in cells for child in split_square(b)];area/=4
        return out
    def evaluate(b,xx,yy):
        n=len(b)-1;m=len(b[0])-1
        return sum((b[i][j]*comb(n,i)*xx**i*(1-xx)**(n-i)*comb(m,j)*yy**j*(1-yy)**(m-j) for i in range(n+1) for j in range(m+1)),Q(0))
    # Separate fixed polynomials with analytically known norms.
    for label,poly,expected in [
        ("constant",s.Rational(3,7),Q(3,7)),
        ("positive_quadratic",(x-s.Rational(1,2))**2+(y-s.Rational(1,2))**2,Q(1,6)),
        ("sign_changing_product",(x-s.Rational(1,2))*(y-s.Rational(1,2)),Q(1,16))]:
        bb=bernstein(poly)
        for xx,yy in [(Q(0),Q(0)),(Q(1),Q(1)),(Q(2,5),Q(3,7))]:
            val=poly.subs({x:s.Rational(xx.numerator,xx.denominator),y:s.Rational(yy.numerator,yy.denominator)})
            test(label+"_reconstruct_"+str(xx)+"_"+str(yy),evaluate(bb,xx,yy)==Q(int(val.p),int(val.q)))
        bounds=ladder(poly,1)
        test(label+"_known_L1_exact_after_split",bounds[1]==(expected,expected))
        test(label+"_nested",bounds[0][0]<=bounds[1][0]<=bounds[1][1]<=bounds[0][1])
    # Weights computed by the imported canonical core; no saved generated input.
    eta=context["eta"];r=context["r"]
    rows={};encoded={}
    for label,weight in [("psi",context["weighted_psi"]),("z",context["weighted_z"])]:
        poly=s.Poly(s.expand(s.cancel(weight).subs({eta:x-4,r:y+1})),x,y)
        test(label+"_rational_polynomial",poly.domain in (s.ZZ,s.QQ) and all(c.is_Rational for c in poly.coeffs()))
        bb=bernstein(poly.as_expr())
        for xx,yy in [(Q(1,2),Q(1,2)),(Q(1,4),Q(3,4)),(Q(3,4),Q(1,4))]:
            val=poly.as_expr().subs({x:s.Rational(xx.numerator,xx.denominator),y:s.Rational(yy.numerator,yy.denominator)})
            test(label+"_exact_reconstruction_"+str(xx)+"_"+str(yy),evaluate(bb,xx,yy)==Q(int(val.p),int(val.q)))
        signed=sum((v for row in bb for v in row),Q(0))/(len(bb)*len(bb[0]))
        exact=s.integrate(poly.as_expr(),(x,0,1),(y,0,1))
        test(label+"_signed_integral",signed==Q(int(exact.p),int(exact.q)))
        bounds=ladder(poly.as_expr(),3)
        for i,(lo,hi) in enumerate(bounds):
            test(label+"_enclosure_order_"+str(i),0<=lo<=hi)
            if i:test(label+"_nested_"+str(i),bounds[i-1][0]<=lo<=hi<=bounds[i-1][1])
        rows[label]={"degrees":poly.degree_list(),"levels":[{"level":i,"lower":str(lo),"upper":str(hi),"lower_numeric":float(lo),"upper_numeric":float(hi)} for i,(lo,hi) in enumerate(bounds)]}
        encoded[label]={"degree":poly.degree_list(),"coefficients":[{"powers":list(ij),"coefficient":str(v)} for ij,v in poly.terms()]}
    moment=Q(context["moment"])
    K=sum((Q(v["levels"][-1]["upper"]) for v in rows.values()),Q(0))
    radius=moment/(2*K)
    test("strict_positive_combined_bound",K>0)
    test("strict_positive_certified_radius",radius>0)
    test("strict_rejection_at_radius_quarter",moment-K*(radius/4)>K*(radius/4))
    encoded["scope"]="Frozen wrong-candidate measure-weighted photon kernels on x,y in[0,1]^2; no empirical data"
    result={"scope":"Exact norm enclosure refinement of constructed fixed photon test, not observational precision","passed":sum(c["pass"] for c in checks),"failed":sum(not c["pass"] for c in checks),"checks":checks,"norm_enclosures":rows,"moment":str(moment),"combined_upper":str(K),"error_contract":"Recovered normalized-Y20 harmonic coefficient envelopes; full-sky pointwise errors need the angular factor", "uniform_radius":str(radius),"uniform_radius_numeric":float(radius)}
    result["computed_weight_polynomials"]=encoded
    return result
