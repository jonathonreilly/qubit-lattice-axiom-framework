"""Direct four-by-four check of the exploratory low-energy Taylor jet."""
from pathlib import Path
import numpy as np,json
p=Path(__file__).resolve().parent
ns={'__file__':str(p/'block16_cubic_correction.py')}
exec((p/'block16_cubic_correction.py').read_text().rsplit('rows=[]',1)[0],ns)
mat={};exec((p/'block16_local_covariance.py').read_text().rsplit('rows=[]',1)[0],mat)
coeff=ns['coefficients'](1,1);G=ns['G'];node=np.array([ns['xn'],0,ns['zn']]);rows=[]
for direction in [[.4,-.3,.5],[.7,.2,-.4],[-.2,.8,.3]]:
    v=np.array(direction);v/=np.linalg.norm(v)
    for delta in [.02,.01,.005,.0025]:
        q=delta*v;k=node+q
        H=mat['on']+sum(np.cos(k[i])*mat['Cs'][i]+np.sin(k[i])*mat['Ss'][i] for i in range(3))
        e=np.linalg.eigvalsh(H);actual=float(min(abs(e))**2)
        quadratic=float(np.sum(G*q*q));cubic=float(sum(c*np.prod(q**np.array(power)) for power,c in coeff.items()))
        error=actual-quadratic-cubic
        rows.append(dict(direction=direction,delta=delta,actual_low_squared=actual,cubic=cubic,
                         remainder_over_delta4=error/delta**4,
                         wrong_sign_remainder_over_delta3=(actual-quadratic+cubic)/delta**3))
        assert abs(error)<10*delta**4
(p/'BLOCK16_CUBIC_MATRIX_CHALLENGE.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
