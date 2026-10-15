"""Root equal-time covariance inverse: exact algebra, synthetic supplied events."""
from pathlib import Path
import json
import sympy as s
from scalar_dynamical_domains import rational


def lift_row(data,h):
    SS,SV,VV,SSp,SVp,VVp=map(rational,data)
    if SS<0 or VV<0 or SS*VV-SV**2<0:
        raise ValueError('equal-time covariance must be positive semidefinite')
    return [SS/2,-SS/2-SVp+(h-1)*SV,VVp/2+SV/2-h*VV,SV,-VV],-SSp/2-SS


def inverse(data,h,J):
    h,J=map(rational,[h,J])
    if J<=0:raise ValueError('J must be positive')
    if len(data)!=5:raise ValueError('five covariance rows required')
    pairs=[lift_row(v,h) for v in data];L=s.Matrix([p[0] for p in pairs]);rhs=s.Matrix([p[1] for p in pairs])
    if L.det()==0:raise ValueError('covariance rank deficient')
    z=L.inv()*rhs;x,y,z3,z4,z5=z
    if z3!=y*y or z5!=(z4+x*y/2)*y:
        raise ValueError('lifted solution fails physical monomial identities')
    R=(z4+x*y/2)/J
    if R<=0 or y==0 or x/y<=0:raise ValueError('positive rolling coefficient chart required')
    return dict(R=R,x=x,y=y,q=x/y,lift=list(z),determinant=L.det())


def controls():
    checks=[]
    def chk(name,result,**detail):checks.append(dict(name=name,passed=bool(result),**detail))
    x,y,R,J,h=s.symbols('x y R J h',nonzero=True)
    SS,SV,VV,ST,VT=s.symbols('SS SV VV ST VT',real=True)
    SSp=-(2+x)*SS-y*ST-2*J*R*SV
    SVp=(h-1-x/2)*SV-SS/2-ST/2-y*VT/2-J*R*VV
    VVp=2*h*VV-SV-VT
    row=s.Matrix([[SS/2,-SS/2-SVp+(h-1)*SV,VVp/2+SV/2-h*VV,SV,-VV]])
    z=s.Matrix([x,y,y*y,J*R-x*y/2,J*R*y])
    chk('full_covariance_lift_identity',s.expand((row*z)[0]+SSp/2+SS)==0)
    basevars=[SS,SV,VV,ST,VT]
    transform=row.jacobian(basevars)
    chk('physical_covariance_entry_map_full_rank',s.factor(transform.det())!=0,determinant=str(s.factor(transform.det())))
    vals={x:s.Rational(3,50),y:s.Rational(2,5),R:s.Rational(4,5),J:s.Rational(7,3),h:s.Rational(-2,7)}
    covariances=[s.eye(3)]
    for ij,change in [((0,0),s.Rational(1,2)),((0,1),s.Rational(1,4)),((0,2),s.Rational(1,5)),((1,2),s.Rational(1,6)),((1,1),s.Rational(1,3))]:
        mat=s.eye(3);i,j=ij;mat[i,j]+=change
        if i!=j:mat[j,i]+=change
        covariances.append(mat)
    data=[]
    for i,c in enumerate(covariances):
        loc={SS:c[0,0],SV:c[0,1],VV:c[1,1],ST:c[0,2],VT:c[1,2],**vals}
        dd=[c[0,0],c[0,1],c[1,1],SSp.subs(loc),SVp.subs(loc),VVp.subs(loc)]
        data.append(dd)
        chk('positive_definite_covariance_'+str(i),all(c[:j,:j].det()>0 for j in [1,2,3]))
    got=inverse(data[:5],vals[h],vals[J])
    chk('five_covariance_inverse',all(got[a]==vals[b] for a,b in [('x',x),('y',y),('R',R)]) and got['q']==s.Rational(3,20),determinant=str(got['determinant']))
    rr,mm=lift_row(data[5],vals[h]);chk('sixth_covariance_reserved',s.Matrix([rr]).dot(s.Matrix(got['lift']))==mm)
    # Equal-time covariances admit different derivative time legs; this lift needs only totals.
    S,V,T,Sp,Vp=s.symbols('S V T Sp Vp',real=True);aa=(y-x-2)/2;cc=-h*y-J*R
    identity=s.expand((S-y*V)*(Sp-y*Vp-aa*S-cc*V))
    expected=S*Sp-y*(Sp*V+S*Vp)+y*y*V*Vp-aa*S*S-(cc-aa*y)*S*V+cc*y*V*V
    chk('antisymmetric_time_legs_cancel',s.expand(identity-expected)==0)
    def refused(name,fn):
        try:fn()
        except ValueError:chk(name,True)
        else:chk(name,False)
    refused('rank_deficient_rows',lambda:inverse([data[0]]*5,vals[h],vals[J]))
    refused('nonpositive_J',lambda:inverse(data[:5],vals[h],0))
    for name,index in [('square_monomial',2),('product_monomial',4)]:
        bad=[d.copy() for d in data[:5]];badlift=got['lift'].copy();badlift[index]+=s.Rational(1,100)
        for dd in bad:
            lr,_=lift_row(dd,vals[h]);dd[3]=-2*s.Matrix([lr]).dot(s.Matrix(badlift))-2*dd[0]
        refused(name+'_inconsistent_lift_not_physics',lambda bad=bad:inverse(bad,vals[h],vals[J]))
    badcov=[d.copy() for d in data[:5]]
    loc={SS:1,SV:2,VV:1,ST:0,VT:0,**vals}
    badcov[0]=[1,2,1,SSp.subs(loc),SVp.subs(loc),VVp.subs(loc)]
    refused('nonpositive_covariance_refused',lambda:inverse(badcov,vals[h],vals[J]))
    badfinite=[d.copy() for d in data[:5]];badfinite[0][4]=float('nan')
    refused('nonfinite_covariance_refused',lambda:inverse(badfinite,vals[h],vals[J]))
    return {'scope':'Exact conditional equal-time lift; synthetic covariance inputs, no observational data',
            'checks':checks,'counts':{'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks)},
            'event':{str(k):str(v) for k,v in vals.items()},'six_covariance_inputs':[[str(v) for v in d] for d in data],
            'reconstruction':{k:([str(w) for w in v] if isinstance(v,list) else str(v)) for k,v in got.items()}}
