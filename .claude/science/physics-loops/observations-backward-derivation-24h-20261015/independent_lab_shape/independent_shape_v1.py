"""Pre-author-code independent shape cones; no scientific imports from author."""
from pathlib import Path
from fractions import Fraction as F
import csv, hashlib, json, itertools
import numpy as np
import sympy as sp
from scipy.optimize import linprog
from scipy.special import jv

HERE=Path(__file__).resolve().parent
DATA=HERE/'PREEXPOSURE__LEE2020_APPENDIX_A1_v1.csv'
CHECKS=[]
def check(name, condition, detail=None):
    CHECKS.append({'name':name,'passed':bool(condition),'detail':detail})
def rat(x): return str(x.numerator)+'/'+str(x.denominator)

def relation(s,ds=None):
    if ds is None:
        return [(i,j) for i in range(len(s)) for j in range(len(s)) if i!=j and s[i]<=s[j]]
    return [(i,j) for i in range(len(s)) for j in range(len(s)) if s[i]+ds[i]<s[j]-ds[j]]

def analytic(y,sigma,edges):
    candidates=[(F(0),{'kind':'k_nonnegative'})]
    candidates += [(-v/w,{'kind':'nonnegative','row':i}) for i,(v,w) in enumerate(zip(y,sigma))]
    candidates += [((y[j]-y[i])/(sigma[i]+sigma[j]),{'kind':'ordered_pair','earlier':i,'later':j}) for i,j in edges]
    k=max(v for v,_ in candidates)
    witnesses=[w for v,w in candidates if v==k]
    lower=[v-k*w for v,w in zip(y,sigma)]
    t=[max([F(0),lower[i]]+[lower[j] for a,j in edges if a==i]) for i in range(len(y))]
    assert all(abs(a-b)<=k*c for a,b,c in zip(t,y,sigma))
    assert all(t[i]>=t[j] for i,j in edges)
    return k,t,witnesses

def lp(H,y,sigma,extra=None):
    n,m=H.shape
    A=np.vstack([np.c_[H,-sigma],np.c_[-H,-sigma]])
    b=np.r_[y,-y]
    if extra is not None:
        A=np.vstack([A,np.c_[extra,np.zeros(len(extra))]])
        b=np.r_[b,np.zeros(len(extra))]
    objective=np.zeros(m+1);objective[-1]=1
    sol=linprog(objective,A_ub=A,b_ub=b,bounds=(0,None),method='highs-ds',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    assert sol.success, sol.message
    x=sol.x;d=sol.ineqlin.marginals
    reduced=objective-A.T@d
    slack=b-A@x
    certificate={'status':sol.message,'objective':float(sol.fun),'primal_coefficients':x.tolist(),'dual_inequality':d.tolist(),'dual_objective':float(b@d),'min_primal_slack':float(slack.min()),'min_variable':float(x.min()),'max_positive_dual':float(max(0,d.max())),'min_reduced_cost':float(reduced.min()),'duality_gap':float(objective@x-b@d),'max_complementarity':float(max(np.max(np.abs(d*slack)),np.max(np.abs(x*reduced)))),'active_inequality_indices':np.flatnonzero(np.abs(slack)<2e-8).tolist()}
    return H@x[:-1],certificate

def basis(s,convex):
    distinct=sorted(set(s));sf=np.array([float(x) for x in s]);x=np.array([float(x) for x in distinct])
    if convex:
        scale=x[-1]-x[0]
        cols=[np.ones(len(s)),(x[-1]-sf)/scale]
        cols += [np.maximum(k-sf,0)/scale for k in x[1:-1]]
    else:
        cols=[np.ones(len(s))]+[(sf<=k).astype(float) for k in x[:-1]]
    return np.column_stack(cols),distinct

def certificate_checks(label,c):
    check(label+' primal feasible',c['min_primal_slack']>=-2e-8 and c['min_variable']>=-2e-8,c['min_primal_slack'])
    check(label+' dual feasible',c['max_positive_dual']<2e-8 and c['min_reduced_cost']>=-2e-8,c['min_reduced_cost'])
    check(label+' duality',abs(c['duality_gap'])<2e-8,c['duality_gap'])
    check(label+' complementarity',c['max_complementarity']<2e-8,c['max_complementarity'])

def synthetic():
    rates=[0,1,2,4];weights=list(map(sp.Rational,['1/5','7/10','13/10','2/5']))
    d=sp.log(2);h=sp.log(3)
    def T(x):return sum(w*sp.exp(-q*x) for q,w in zip(rates,weights))
    for p in range(7):
        moment=sp.simplify(sum(w*q**p*sp.exp(-q*d) for q,w in zip(rates,weights)))
        difference=sp.simplify((-1)**p*sum((-1)**(p-j)*sp.binomial(p,j)*T(d+j*h) for j in range(p+1)))
        moment_difference=sp.simplify(sum(w*sp.exp(-q*d)*(1-sp.exp(-q*h))**p for q,w in zip(rates,weights)))
        check('exact Laplace derivative '+str(p),moment>=0,str(moment))
        check('exact Laplace difference '+str(p),difference==moment_difference and difference>=0,str(difference))
    first=sum(w*q*sp.exp(-q*d) for q,w in zip(rates,weights));second=sum(w*q*q*sp.exp(-q*d) for q,w in zip(rates,weights))
    variance=sp.simplify(T(d)*second-first**2)
    pair=sp.simplify(sum(w*v*(q-r)**2*sp.exp(-(q+r)*d) for q,w in zip(rates,weights) for r,v in zip(rates,weights))/2)
    check('exact log convex identity',variance==pair and variance>0,str(variance))
    check('exact log convex three points',sp.simplify(T(d)*T(d+2*h)-T(d+h)**2)>0)
    check('gain offset measure',sp.simplify(3*T(d+sp.log(2))-sum(3*w*2**(-sp.Integer(q))*sp.exp(-q*d) for q,w in zip(rates,weights)))==0)
    x=sp.symbols('x',real=True);signed=sp.exp(-x)-sp.exp(-3*x)/10
    log_curvature=sp.simplify(signed*sp.diff(signed,x,2)-sp.diff(signed,x)**2)
    check('weaker cone not sufficient for Laplace',log_curvature== -sp.Rational(2,5)*sp.exp(-4*x) and sp.diff(signed,x,3).subs(x,0)>0,str(log_curvature))
    R=sp.Matrix([1,2,3]);ea=R/3;eb=R/5;w=sp.diag(2,3,5)
    norm=lambda v:sp.sqrt((v.T*w*v)[0])
    error=((R+ea).T*w*(R+eb))[0]-(R.T*w*R)[0]
    bound=norm(R)*(norm(ea)+norm(eb))+norm(ea)*norm(eb)
    check('mismatch bound attained',sp.simplify(error-bound)==0,str(error))
    check('positive rings negative cross Bessel weight',jv(1,2)*jv(1,4)<0,float(jv(1,2)*jv(1,4)))
    s=[F(0),F(1),F(2)];y=list(map(F,['3','2.7','0']));e=[F(1)]*3
    H,_=basis(s,True);t,c=lp(H,np.array(y,float),np.array(e,float))
    check('convex sign concave fixture',abs(c['objective']-.6)<1e-10,c['objective']);certificate_checks('synthetic convex',c)
    s=[F(1),F(1)];y=[F(0),F(2)];e=[F(1),F(1)]
    k,t,witness=analytic(y,e,relation(s));check('duplicate gaps one latent value',k==1 and t[0]==t[1],{'k':rat(k),'t':list(map(rat,t))})
    k2,t2,_=analytic(y,e,relation(s,[F(1),F(1)]));check('interval relaxation removes duplicate equality',k2==0 and t2[0]!=t2[1],{'k':rat(k2)})


def main():
    rows=list(csv.DictReader(DATA.open(newline='')))
    assert len(rows)==95
    assert hashlib.sha256(DATA.read_bytes()).hexdigest()=='de832b111212a39a6a7a610a1013fbf6fa7201b1e9f304da13801e92961ba381'
    s=[F(r['separation_um']) for r in rows];ds=[F(r['separation_sigma_um']) for r in rows]
    edges=relation(s);interval_edges=relation(s,ds)
    groups={str(g):[i for i,v in enumerate(s) if v==g] for g in sorted(set(s))}
    check('all rows retained',len(rows)==95 and len({r['run'] for r in rows})==95)
    synthetic();channels={}
    for channel in ['N120','N18','N54']:
        y=[F(r[channel+'_fNm']) for r in rows];err=[F(r[channel+'_sigma_fNm']) for r in rows]
        assert all(e>0 for e in err)
        yy=np.array(y,float);ee=np.array(err,float)
        k,ta,wit=analytic(y,err,edges);ki,ti,witi=analytic(y,err,interval_edges)
        monoH,_=basis(s,False);tm,cm=lp(monoH,yy,ee)
        convexH,x=basis(s,True);tc,cc=lp(convexH,yy,ee)
        extra=np.zeros((len(interval_edges),95))
        for n,(i,j) in enumerate(interval_edges):extra[n,j]=1;extra[n,i]=-1
        tp,cp=lp(np.eye(95),yy,ee,extra)
        for name,c in [('central monotone',cm),('central convex',cc),('interval monotone',cp)]:certificate_checks(channel+' '+name,c)
        check(channel+' exact monotone optimum',abs(cm['objective']-float(k))<1e-9,{'exact':rat(k),'lp':cm['objective']})
        check(channel+' exact partial optimum',abs(cp['objective']-float(ki))<1e-9,{'exact':rat(ki),'lp':cp['objective']})
        check(channel+' nested cones',float(ki)<=float(k)+1e-10 and float(k)<=cc['objective']+1e-10)
        distinct_t=np.array([tc[s.index(v)] for v in x]);xx=np.array(x,float)
        slopes=np.diff(distinct_t)/np.diff(xx)
        check(channel+' separately decoded convex signs',min(distinct_t)>=-2e-8 and max(slopes)<=2e-8 and min(np.diff(slopes))>=-2e-8,{'max_slope':float(max(slopes)),'min_slope_increment':float(min(np.diff(slopes)))})
        transformed_y=[3*v for v in y];transformed_e=[3*v for v in err]
        kt,tt,_=analytic(transformed_y,transformed_e,relation([v+F(109) for v in s]))
        check(channel+' exact gain offset LP invariance',kt==k and all(a==3*b for a,b in zip(tt,ta)))
        Hshift,_=basis([v+F(109) for v in s],True);_,cshift=lp(Hshift,3*yy,3*ee)
        check(channel+' convex gain offset LP invariance',abs(cshift['objective']-cc['objective'])<1e-8,cshift['objective'])
        ledger=[]
        for i,r in enumerate(rows):
            out=dict(r);out.update({'csv_row_index':i,'central_monotone_exact_t':rat(ta[i]),'central_monotone_lp_t':float(tm[i]),'central_convex_t':float(tc[i]),'interval_monotone_exact_t':rat(ti[i]),'interval_monotone_lp_t':float(tp[i]),'central_monotone_standardized_residual':float((tm[i]-yy[i])/ee[i]),'central_convex_standardized_residual':float((tc[i]-yy[i])/ee[i]),'interval_monotone_standardized_residual':float((tp[i]-yy[i])/ee[i])});ledger.append(out)
        channels[channel]={'central_monotone':{'exact_k':rat(k),'exact_witnesses':wit,'lp':cm},'central_convex':{'lp':cc,'slopes_fNm_per_um':slopes.tolist(),'active_convex_knot_indices':np.flatnonzero(abs(np.diff(slopes))<2e-8).tolist()},'interval_monotone':{'exact_k':rat(ki),'exact_witnesses':witi,'lp':cp},'negative_central_rows':[i for i,v in enumerate(y) if v<0],'rows':ledger}
    result={'scope':'All95 exposed development rows; necessary finite-cone deterministic-box diagnostics, not statistical significance or physical exclusion','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(DATA.read_bytes()).hexdigest(),'row_count':len(rows),'distinct_central_separations':len(groups),'duplicate_groups':{k:v for k,v in groups.items() if len(v)>1},'central_order_pairs':edges,'strict_disjoint_interval_pairs':interval_edges,'channels':channels,'checks':CHECKS,'passed':sum(c['passed'] for c in CHECKS),'failed':sum(not c['passed'] for c in CHECKS),'numerics':'Exact rational monotone optimum and primal witnesses; floating convex/dual certificates, not outward rounded'}
    (HERE/'INDEPENDENT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':result['passed'],'failed':result['failed'],'distinct_central_separations':len(groups),'central_pairs':len(edges),'interval_pairs':len(interval_edges),'optima':{k:{'monotone':v['central_monotone']['lp']['objective'],'convex':v['central_convex']['lp']['objective'],'partial':v['interval_monotone']['lp']['objective'],'exact_monotone':v['central_monotone']['exact_k'],'exact_partial':v['interval_monotone']['exact_k']} for k,v in channels.items()}},indent=2))
    assert result['failed']==0
if __name__=='__main__':main()
