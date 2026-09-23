"""Author challenges of Block20; no interacting spectrum or phase inference."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/FREE_WEYL_HOLONOMY_MINIMIZATION_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'free_weyl_holonomy_minimization_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/FREE_WEYL_HOLONOMY_MINIMIZATION_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/holonomy_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import quad

G=np.array([1.,1.,.75]); pref=1/(math.pi**2*math.sqrt(np.prod(G)))

def theta_fourier(s,a):
    n=np.arange(1,max(2,int(math.ceil(math.sqrt(48/s)))+1),dtype=float)
    w=np.exp(-s*n*n)
    return np.array([1+2*np.sum(w*np.cos(n*a)),
                     -2*np.sum(n*w*np.sin(n*a)),
                     -2*np.sum(n*n*w*np.cos(n*a))])

def theta_images(s,a):
    a=(a+math.pi)%(2*math.pi)-math.pi
    cap=int(math.ceil((abs(a)+math.sqrt(192*s))/(2*math.pi)))+1
    d=a-2*math.pi*np.arange(-cap,cap+1,dtype=float)
    w=np.exp(-d*d/(4*s))*math.sqrt(math.pi/s)
    return np.array([np.sum(w),np.sum(-d*w/(2*s)),
                     np.sum((d*d/(4*s*s)-1/(2*s))*w)])

def theta(s,a):
    return theta_images(s,a) if s<1 else theta_fourier(s,a)

def heat_value(alpha,derivative=None,tol=2e-10):
    alpha=np.asarray(alpha)
    def fun(t):
        th=[theta(t/G[i],alpha[i]) for i in range(3)]
        if derivative is None:
            val=np.prod([z[0] for z in th])-1
        else:
            i,j=derivative
            orders=[int(k==i)+int(k==j) for k in range(3)]
            val=np.prod([th[k][orders[k]] for k in range(3)])
        return pref*t*val
    # At a node the integrable endpoint singularity is t^-1/2.
    vals=[quad(fun,0,1,epsabs=tol,epsrel=tol,limit=200),
          quad(fun,1,40,epsabs=tol,epsrel=tol,limit=200)]
    return sum(v[0] for v in vals),sum(v[1] for v in vals)

def fourier_cube(M, alpha):
    # Exact same integer cube and origin exclusion, one first-coordinate plane.
    plane=np.indices((2*M+1,2*M+1),dtype=float).reshape(2,-1)-M
    partials=[]
    for first in range(-M,M+1):
        mesh=np.vstack((np.full(plane.shape[1],first,dtype=float),plane))
        r2=np.sum(mesh*mesh/G[:,None],axis=0); nz=r2>0
        partials.append(float(np.sum(np.cos(alpha@mesh[:,nz])/r2[nz]**2)))
    return pref*math.fsum(partials)

def _band_plane(L,phi,first,sign,derivatives):
    plane=np.indices((L,L),dtype=float).reshape(2,-1)
    grid=np.vstack((np.full(plane.shape[1],first,dtype=float),plane))
    k=(2*math.pi*grid+sign*np.asarray(phi)[:,None])/L
    # Minus block spectrum is |d0(-k-b ex)|, with the minus charge in k.
    if sign==-1: k=-k
    k[0]-=math.pi/3
    sx,sy,sz=np.sin(k); cx,cy,cz=np.cos(k)
    d=np.array([sx,sy,2.5-cx-cy-cz]); r=np.linalg.norm(d,axis=0)
    energy=-np.sum(r)
    if not derivatives: return float(energy),float(np.min(r))
    assert np.min(r)>1e-12
    z=np.zeros_like(r)
    dj=np.array([[cx,z,sx],[z,cy,sy],[z,z,sz]])
    djj=np.array([[-sx,z,cx],[z,-sy,cy],[z,z,cz]])
    dot=np.einsum('an,jan->jn',d,dj)
    grad=-np.sum(dot/r,axis=1)/L
    hess=np.empty((3,3))
    for i in range(3):
        for j in range(3):
            term=np.sum(dj[i]*dj[j],axis=0)
            if i==j: term+=np.sum(d*djj[i],axis=0)
            hess[i,j]=-np.sum(term/r-dot[i]*dot[j]/r**3)/L**2
    return float(energy),float(np.min(r)),grad,hess

def band(L,phi,sign=1,derivatives=False):
    rows=[_band_plane(L,phi,first,sign,derivatives) for first in range(L)]
    energy=math.fsum(row[0] for row in rows)
    minimum=min(row[1] for row in rows)
    if not derivatives:return energy,minimum
    grad=np.array([math.fsum(row[2][i] for row in rows) for i in range(3)])
    hess=np.array([[math.fsum(row[3][i,j] for row in rows) for j in range(3)] for i in range(3)])
    return energy,minimum,grad,hess

def main():
    # Independent regulator check of the radial Fourier-transform constant:
    # FT[-r exp(-epsilon r)] = -Im[2/(epsilon-iR)^3]/(2pi^2 R).
    radial=[]
    for R in [1.,2.,5.]:
        eps=1e-5*R
        got=-(2/(eps-1j*R)**3).imag/(2*math.pi**2*R)
        expected=1/(math.pi**2*R**4)
        assert abs(got/expected-1)<1e-8
        radial.append({'R':R,'relative_error':abs(got/expected-1)})
    overlap=max(float(np.max(np.abs(theta_images(s,a)-theta_fourier(s,a))))
                for s in [.4,.8,1.,1.5,2.5] for a in [0.,.37,1.9,math.pi])
    assert overlap<2e-13
    ap=np.full(3,math.pi)
    kp,kerr=heat_value(ap)
    h=np.array([[heat_value(ap,(i,j))[0] for j in range(3)] for i in range(3)])
    assert np.linalg.eigvalsh(h).min()>0
    assert np.max(np.abs(h-np.diag(np.diag(h))))<2e-13
    # Different representations: finite Fourier sums converge in energy.
    fourier=[]
    for M in [12,24,48]:
        val=fourier_cube(M,ap)
        fourier.append({'M':M,'energy':float(val),'error':abs(float(val)-kp)})
    assert fourier[-1]['error']<2e-7
    assert fourier[-1]['error']<fourier[0]['error']/30
    alphas=[np.zeros(3),np.array([.7,1.3,2.2]),np.array([math.pi,.8,2.7])]
    predictions=[4*(heat_value(a)[0]-kp) for a in alphas]
    assert min(predictions)>0
    rows=[]
    for L in [9,12,15,18,21,24,27,30,45,48,69,72]:
        shift=np.array([0.,0.,0.]) if L%6==0 else np.array([math.pi,0.,math.pi])
        phistar=(shift+ap)%(2*math.pi)
        e,gap,grad,hess=band(L,phistar,derivatives=True)
        gaps=[]
        for a in alphas:
            ep,_=band(L,(shift+a)%(2*math.pi))
            gaps.append(float(2*L*(ep-e)))
        # Opposite charge and complex-conjugate spectrum must ADD, not cancel.
        phi=np.array([.61,1.12,2.29]); ep,_=band(L,phi); em,_=band(L,phi,sign=-1)
        assert abs(ep-em)<1e-9*max(1,abs(ep))
        assert np.max(np.abs(grad))<1e-10
        assert np.linalg.eigvalsh(hess).min()>0
        rows.append({'L':L,'phistar_over_pi':(phistar/math.pi).tolist(),
          'scaled_energy_differences':gaps,
          'casimir_errors':(np.array(gaps)-predictions).tolist(),
          'scaled_hessian':(2*L*hess).tolist(),
          'hessian_max_error':float(np.max(np.abs(2*L*hess-4*h))),
          'scaled_one_particle_gap':L*gap,
          'gap_coefficient_error':L*gap-math.pi*math.sqrt(11)/2,
          'gradient_max':float(np.max(np.abs(grad)))})
    for residue in [0,3]:
        rr=[r for r in rows if r['L']%6==residue]
        first,last=rr[0],rr[-1]
        assert np.max(np.abs(last['casimir_errors']))<np.max(np.abs(first['casimir_errors']))/8
        assert last['hessian_max_error']<first['hessian_max_error']/8
        assert abs(last['gap_coefficient_error'])<abs(first['gap_coefficient_error'])/3
    # Literal analytic band Hessian versus central energy differences, one moderate box.
    L=12; phi=np.array([2.1,2.4,1.8]); _,_,_,bh=band(L,phi,derivatives=True)
    eps=.004; fd=np.zeros((3,3)); en=band(L,phi)[0]
    for i in range(3):
        ui=np.eye(3)[i]*eps
        fd[i,i]=(band(L,phi+ui)[0]-2*en+band(L,phi-ui)[0])/eps**2
        for j in range(i):
            uj=np.eye(3)[j]*eps
            fd[i,j]=fd[j,i]=(band(L,phi+ui+uj)[0]-band(L,phi+ui-uj)[0]
                    -band(L,phi-ui+uj)[0]+band(L,phi-ui-uj)[0])/(4*eps**2)
    fderr=float(np.max(np.abs(fd-bh)))
    assert fderr<2e-6
    # Wrong charge treatment giving cancellation is decisively incompatible.
    cancellation_mutation_error=max(predictions)
    assert cancellation_mutation_error>.1
    out={'status':'author_finite_checks_pass_not_independent_audit',
      'radial_transform':radial,'theta_overlap_max_error':overlap,
      'K_at_pi':kp,'heat_quadrature_estimate':kerr,
      'four_cone_hessian':(4*h).tolist(),'Fourier_energy_crosscheck':fourier,
      'test_alpha': [a.tolist() for a in alphas],
      'predicted_scaled_energy_differences':predictions,'lattice_rows':rows,
      'band_Hessian_finite_difference_error':fderr,
      'wrong_cancellation_mutation_error':cancellation_mutation_error,
      'scope':'free prescribed-flat-background matter only; no effective gauge dynamics'}
    s=json.dumps(out,indent=2); _OUTPUT_JSON.write_text(s+'\n');print(s)

if __name__=='__main__':main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: theta/Fourier identities and Hessian controls')
    print('per_site: finite free-band torus sums only')
    print('per_mode: finite twist/momentum samples; no fluctuating gauge-field integration')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
