"""Exact rational trial-vector check at a rational Bloch phase.

All final inequalities use integers/Fractions; floating eigensolve only proposes
the trial vector. Conditional on the closed operator and verified gap proof.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import hashlib,json,math
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def cmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]

def calculate(HERE):
    p=HERE/'closed_quotient_operator.npz'
    original=json.loads((HERE/'PRIMARY_CLOSED_BAND.json').read_text())
    assert sha(p)==original['numerical_data_sha256']
    gap=json.loads((HERE/'ZERO_GAP_CERTIFICATE.json').read_text())
    assert gap['threshold']==-550 and gap['lambda2_strictly_above_threshold']
    x=np.load(p);n=len(x['diagonal']);tau=x['tau'];coeff=x['coefficient']
    src=x['src'];dst=x['dst'];q=40001
    assert sum(abs(int(c)) for c in coeff)*max(1,int(abs(tau).max())**2)<2**53
    power=int(abs(tau[:,0]).max());D=q**power
    phase={}
    for t in range(-power,power+1):
        z=(1,0);base=(39999,-400 if t>=0 else 400)
        for _ in range(abs(t)):z=cmul(z,base)
        phase[t]=(z[0]*(q**(power-abs(t))),z[1]*(q**(power-abs(t))))
    rows=[defaultdict(lambda:[0,0]) for _ in range(n)]
    drows=[defaultdict(lambda:[0,0]) for _ in range(n)]
    for i,j,t,c in zip(dst,src,tau[:,0],coeff):
        i,j,t,c=map(int,(i,j,t,c));re,im=phase[t];re*=c;im*=c
        rows[i][j][0]+=re;rows[i][j][1]+=im
        drows[i][j][0]+=t*im;drows[i][j][1]-=t*re
    for i,d in enumerate(x['diagonal']):rows[i][i][0]+=int(d)*D
    ri=[];ci=[];data=[]
    for i,row in enumerate(rows):
        for j,(re,im) in row.items():
            rev=rows[j].get(i,[0,0]);assert rev==[re,-im]
            ri.append(i);ci.append(j);data.append(complex(re,im)/D)
    H=sparse.coo_matrix((data,(ri,ci)),shape=(n,n)).tocsr()
    eigen,vec=eigsh(H,k=1,which='SA',tol=2e-14,maxiter=10000,v0=x['zero_ground'].astype(complex))
    trial=vec[:,0];scale=1<<60
    ar=[round(float(z.real)*scale) for z in trial];ai=[round(float(z.imag)*scale) for z in trial]
    S=sum(a*a+b*b for a,b in zip(ar,ai));assert S>0

    def apply(rs):
        re=[];im=[]
        for row in rs:
            re.append(sum(c*ar[j]-d*ai[j] for j,(c,d) in row.items()))
            im.append(sum(c*ai[j]+d*ar[j] for j,(c,d) in row.items()))
        return re,im

    yr,yi=apply(rows)
    T=sum(a*c+b*d for a,b,c,d in zip(ar,ai,yr,yi))
    assert sum(a*d-b*c for a,b,c,d in zip(ar,ai,yr,yi))==0
    rayleigh=F(T,D*S)
    R2=F(sum((S*c-T*a)**2+(S*d-T*b)**2 for a,b,c,d in zip(ar,ai,yr,yi)),D*D*S**3)
    eta=F(1,10**7);assert R2<eta*eta
    # k*=2 atan(1/200) lies strictly between 0 and 1/100.
    # The same row/column bound controls the operator variation by |k|*v_x.
    vbound=[int(np.bincount(dst,weights=np.abs(tau[:,j]*coeff),minlength=n).max()) for j in range(3)]
    abound=[[int(np.bincount(dst,weights=np.abs(tau[:,i]*tau[:,j]*coeff),minlength=n).max()) for j in range(3)] for i in range(3)]
    remaining_lower=F(-550)-F(vbound[0],100)
    separation=remaining_lower-rayleigh
    assert separation>350 and rayleigh+eta<remaining_lower
    vector_error=2*eta/separation
    yrp,yip=apply(drows)
    slope=F(sum(a*c+b*d for a,b,c,d in zip(ar,ai,yrp,yip)),D*S)
    assert sum(a*d-b*c for a,b,c,d in zip(ar,ai,yrp,yip))==0
    slope_error=2*vbound[0]*vector_error
    weights={}
    for name,array in [('minus',x['first_minus']),('plus',x['first_plus']),('coherent',x['first_coherent'])]:
        ids=np.where(array>0)[0];count=len(ids)
        assert count in (5,10) and np.allclose(array[ids],1/math.sqrt(count),rtol=0,atol=1e-15)
        overlap=F(sum(ar[i] for i in ids)**2+sum(ai[i] for i in ids)**2,count*S)
        weights[name]={'trial_weight':str(overlap),'ground_weight_lower':str(overlap-2*vector_error)}
    h=F(1,4_000_000);delta=h*sum(vbound);uniform_gap=F(300)
    assert separation-eta-2*delta>uniform_gap
    hessian_row=sum(F(a) for a in abound[0])+2*F(vbound[0])*sum(vbound)/uniform_gap
    pocket_slope=slope-slope_error-h*hessian_row
    assert pocket_slope>2
    # For any straight path in the pocket, ||P'||<=2||H'||/gap.
    # Projected initial-vector norms differ by at most the projector norm.
    projector_change=2*delta/uniform_gap
    overlap_floor=F(1,6)
    for item in weights.values():
        assert F(item['ground_weight_lower'])>(overlap_floor+projector_change)**2
    onset=300
    assert 2*F(vbound[0],onset)/uniform_gap<=F(1,6)
    # Haar normalization in physical k coordinates: reciprocal volume4*pi^3.
    # pi^3<32 gives pocket measure >=h^3/16. Moment lower >=measure/36.
    A=h**3/576
    D4=sum((abound[i][j]+vbound[i]*vbound[j])**2 for i in range(3) for j in range(3))
    speed=F(1,10**12);probability=F(1,10**62)
    assert speed*speed<=A/2
    assert probability<=A*A/(4*D4)
    witness=HERE/'VELOCITY_POCKET_INTEGER_TRIAL.json'
    witness.write_text(json.dumps({'real':[str(a) for a in ar],'imag':[str(b) for b in ai]},separators=(',',':'))+'\n')
    out={'status':'exact rational velocity-pocket inequalities conditional on reconstructed operator',
       'operator_sha256':sha(p),'database_sha256':gap['database_sha256'],
       'zero_gap_certificate_sha256':sha(HERE/'ZERO_GAP_CERTIFICATE.json'),
       'phase':{'real':'39999/40001','imag':'-400/40001','k':'2 atan(1/200)',
                'denominator':D,'maximum_phase_power':power},
       'rayleigh':str(rayleigh),'rayleigh_float':float(rayleigh),'residual_squared':str(R2),
       'residual_bound':str(eta),'remaining_spectrum_lower':str(remaining_lower),
       'ground_separation_from_rayleigh':str(separation),'vector_error_bound':str(vector_error),
       'slope_trial':str(slope),'slope_trial_float':float(slope),'slope_error_bound':str(slope_error),
       'first_weights':weights,'velocity_row_bounds':vbound,'second_derivative_row_bounds':abound,
       'pocket_half_width':str(h),'pocket_uniform_gap':str(uniform_gap),
       'pocket_slope_lower':str(pocket_slope),'pocket_slope_lower_float':float(pocket_slope),
       'pocket_first_projection_norm_lower':str(overlap_floor),
       'postbirth_time_onset':onset,'second_moment_over_time_squared_lower':str(A),
       'fourth_moment_over_time_fourth_upper':D4,'escape_speed_lower_choice':str(speed),
       'escape_probability_lower_choice':str(probability),
       'trial_sha256':sha(witness),'source_sha256':sha(Path(__file__)),
       'limits':'extremely conservative projected-model constants; full-law errors still subtract; no detector or calibration'}
    (HERE/'VELOCITY_POCKET_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('residual_squared','rayleigh','ground_separation_from_rayleigh','slope_trial','first_weights','pocket_slope_lower')},indent=2))
