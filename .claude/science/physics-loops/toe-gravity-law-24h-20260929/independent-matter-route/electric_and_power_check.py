"""Independent electric compression and first-mark system-power controls."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import birth_work_exact as m


def loop(base,i,j,weight):
    ei=tuple(int(k==i) for k in range(3));ej=tuple(int(k==j) for k in range(3))
    vertices=[base,m.add(base,ei),m.add(m.add(base,ei),ej),m.add(base,ej)]
    e=Counter()
    for x,y in zip(vertices,vertices[1:]+vertices[:1]):
        a,b,sign=(x,y,1) if m.even(x) else (y,x,-1)
        e[a,b]+=weight*sign
    return e


def act_birth(s,a,b,sigmas):
    out=Counter()
    for sig in sigmas:
        for t in m.F(s,a):
            y=m.J(t,a,b,sig)
            if y is not None:out[y]+=1
    return out


def expected_electric(e,a,b,sigmas):
    total=0
    for sig in sigmas:
        for d in m.nb(a):
            if d==b:continue
            removed=sum(e.get((c,x),0)**2 for x in (b,d) for c in m.nb(x))
            linear=2*(e.get((a,b),0)+e.get((a,d),0)) if sig==-1 else 0
            total-=removed+linear
    return Fraction(total,5*len(sigmas))


def main():
    checks=0
    bases=[(-1,0,0),(0,0,0),(1,0,0),(0,1,0),(0,0,-1)]
    for index,base in enumerate(bases):
        e=Counter()
        for i,j in ((0,1),(0,2),(1,2)):
            for ab,v in loop(base,i,j,index+1).items():e[ab]+=v
        s=m.canonical({},e);assert m.gauss(s)
        for b in m.DIRS:
            for sigmas in ((-1,),(1,),(-1,1)):
                v=act_birth(s,m.ORIGIN,b,sigmas);norm=m.norm2(v)
                assert norm==5*len(sigmas)
                got=Fraction(sum(c*c*m.D(t) for t,c in v.items()),norm)-m.D(s)
                assert got==expected_electric(e,m.ORIGIN,b,sigmas),(s,b,sigmas,got)
                checks+=1
    p=json.loads(Path(__file__).with_name('birth_work_laurent.json').read_text())
    bounds={}
    for name in ('minus','plus','coherent'):
        a=Fraction(p[name]['constant']);b=Fraction(p[name]['nonconstant_l1'])
        lower=a-b-48
        assert lower>0
        bounds[name]={'all_R_all_finite_wait_lower_over_delta':str(lower),
                      'zero_wait_increment_over_delta':str(a),
                      'large_R_error_bound_over_delta':str(3072+32*b)+' / R'}
    rate_lower=60*Fraction(bounds['coherent']['all_R_all_finite_wait_lower_over_delta'])
    power0=60*Fraction(bounds['coherent']['zero_wait_increment_over_delta'])
    print('electric formula exact fixtures',checks)
    print(json.dumps(bounds,indent=2))
    print('all-channel power lower /(kappa delta N)',rate_lower)
    print('initial all-channel power /(kappa delta N)',power0)
    print('TOTAL: PASS=4 FAIL=0 (electric formula; mark normalization; all-R positive bounds; complete-instrument power)')
    Path(__file__).with_suffix('.json').write_text(json.dumps({'electric_fixtures':checks,'bounds':bounds,'power_lower':str(rate_lower),'power_initial':str(power0)},indent=2)+'\n')

if __name__=='__main__':main()
