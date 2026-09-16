#!/usr/bin/env python3
"""Finite checks of a positive-kernel comparison and local cube constants.

The 2-angle finite-difference model checks the Feynman-Kac comparison
structure, not the continuum quantum gauge phase. Cube Fourier orthogonality
is checked by character arithmetic and exact finite Haar sums.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[]
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh,expm


def heat_comparison():
    N=9
    step=2*math.pi/N
    shift=np.roll(np.eye(N),1,axis=0)
    lap=(2*np.eye(N)-shift-shift.T)/(step*step)
    x=2*math.pi*np.arange(N)/N
    states=np.array(list(itertools.product(x,repeat=2)))
    rows=[]
    for g in [.7,1.5,3.]:
        kinetic1=.5*g*g*lap
        free=np.kron(kinetic1,np.eye(N))+np.kron(np.eye(N),kinetic1)
        W=(2-np.cos(states[:,0])-np.cos(states[:,0]-states[:,1]))/(g*g)
        H=free+np.diag(W)
        vals,vecs=eigh(H)
        psi=vecs[:,0].reshape(N,N)
        psi*=np.sign(psi[0,0])
        assert psi.min()>0
        ratios=psi.max(axis=0)/psi.min(axis=0)
        for t in [.1,.4]:
            local_heat=expm(-t*kinetic1)
            base=np.kron(local_heat,local_heat)
            actual=expm(-t*H)
            lower=math.exp(-4*t/(g*g))*base
            upper_margin=float((base-actual).min())
            lower_margin=float((actual-lower).min())
            assert lower_margin>=-2e-14 and upper_margin>=-2e-14
            R=math.exp(4*t/(g*g))*local_heat.max()/local_heat.min()
            assert ratios.max()<=R
            # Applying the product semigroup to the positive eigenvector
            # directly checks the cancellation of the full ground energy.
            A=(base@psi.ravel()).reshape(N,N)
            ground=math.exp(-t*vals[0])*psi
            assert np.min(A-ground)>=-2e-14
            assert np.min(ground-math.exp(-4*t/(g*g))*A)>=-2e-14
            rows.append({'g':g,'t':t,'min_lower_kernel_margin':lower_margin,
                         'min_upper_kernel_margin':upper_margin,
                         'max_ground_amplitude_conditional_ratio':float(ratios.max()),
                         'heat_comparison_ratio_bound':float(R)})
    return {'regulator_points_per_angle':N,'scope':'two coupled angles with a positive finite-difference kinetic generator','rows':rows}


def cubic_complex(shape):
    vertices=list(itertools.product(*(range(n) for n in shape)))
    vset=set(vertices)
    def step(x,a):
        y=list(x);y[a]+=1;return tuple(y)
    edges=[(x,a) for x in vertices for a in range(3) if step(x,a) in vset]
    index={edge:j for j,edge in enumerate(edges)}
    faces=[(x,a,b) for x in vertices for a,b in itertools.combinations(range(3),2)
           if step(step(x,a),b) in vset]
    C=np.zeros((len(faces),len(edges)),dtype=int)
    for p,(x,a,b) in enumerate(faces):
        for edge,sign in [((x,a),1),((step(x,a),b),1),((step(x,b),a),-1),((x,b),-1)]:
            C[p,index[edge]]=sign
    return C


def local_geometry_and_orthogonality():
    rows=[]
    for shape in [(2,2,2),(3,3,3),(4,4,4)]:
        C=cubic_complex(shape)
        adjacent=np.count_nonzero(C,axis=0)
        max_support=max_touch=0
        for e in range(C.shape[1]):
            ps=np.flatnonzero(C[:,e])
            support=np.flatnonzero(np.any(C[ps]!=0,axis=0))
            touching=np.flatnonzero(np.any(C[:,support]!=0,axis=1))
            max_support=max(max_support,len(support))
            max_touch=max(max_touch,len(touching))
        assert adjacent.max()<=4 and max_support<=13 and max_touch<=52
        assert np.all(np.count_nonzero(C,axis=1)==4)
        # All nonzero frequencies C_p +/- C_q fail to be zero modulo 5,
        # except C_p-C_p. Exact product-Haar sums on five angles per link
        # therefore give delta_pq/2, without sampling 5^E configurations.
        cosine_gram=np.empty((len(C),len(C)))
        for p in range(len(C)):
            for q in range(len(C)):
                plus=np.all((C[p]+C[q])%5==0)
                minus=np.all((C[p]-C[q])%5==0)
                cosine_gram[p,q]=(int(plus)+int(minus))/2
        assert np.array_equal(cosine_gram,.5*np.eye(len(C)))
        h=np.sin(np.arange(len(C))+0.3)
        exact_haar_gradient=sum(float((C[:,e]*h)@cosine_gram@(C[:,e]*h)) for e in range(C.shape[1]))
        assert abs(exact_haar_gradient-2*float(h@h))<2e-12
        rows.append({'shape':shape,'links':C.shape[1],'plaquettes':C.shape[0],
                     'maximum_incident_plaquettes':int(adjacent.max()),
                     'maximum_local_support':max_support,'maximum_touching_plaquettes':max_touch,
                     'Haar_gradient_identity_error':abs(exact_haar_gradient-2*float(h@h))})
    return rows


def circle_kernel_bounds():
    rows=[]
    for g,t in [(.3,.2),(.7,1.),(1.5,.4),(3.,1.)]:
        s=g*math.sqrt(t)
        # Wrapped positive Gaussian, including the nearest 25 images.
        xs=np.linspace(-math.pi,math.pi,1001)
        images=np.arange(-12,13)
        values=math.sqrt(2*math.pi)/s*np.exp(-(xs[:,None]+2*math.pi*images)**2/(2*s*s)).sum(axis=1)
        lower=math.sqrt(2*math.pi)/s*math.exp(-math.pi**2/(2*s*s))
        upper=1+math.sqrt(2*math.pi)/s
        assert values.min()>=lower*(1-1e-12)
        assert values.max()<=upper
        log_c=-208*t/(g*g)+26*(math.log(lower)-math.log(upper))
        rows.append({'g':g,'t':t,'sampled_heat_min':float(values.min()),
                     'explicit_lower':lower,'sampled_heat_max':float(values.max()),
                     'explicit_upper':upper,'log_sufficient_local_c':log_c})
    return rows



def principal_cube_event():
    C=cubic_complex((2,2,2))
    _,_,Vh=np.linalg.svd(C.T,full_matrices=True)
    z=np.sign(Vh[-1]).astype(int)
    assert np.array_equal(C.T@z,np.zeros(12,dtype=int))
    target=z*np.array([-5*math.pi/3]+[math.pi/3]*5)
    theta=np.linalg.lstsq(C,target,rcond=None)[0]
    assert np.linalg.norm(C@theta-target)<1e-14
    epsilon=math.pi/48
    corners=np.array(list(itertools.product([-1,1],repeat=12)))
    angle_corners=theta[None,:]+.999*epsilon*corners
    raw=angle_corners@C.T
    principal=raw
    charge=principal@z/(2*math.pi)
    assert np.max(abs(charge-1))<2e-14
    raw_charge=raw@z/(2*math.pi)
    assert np.max(abs(raw_charge))<2e-14
    branch_margin=float(np.min(math.pi-abs(principal)))
    assert branch_margin>0
    return {'cube_links':12,'corners_checked':len(corners),
            'signed_raw_center':(z*(C@theta)).tolist(),
            'charge_one_max_error':float(np.max(abs(charge-1))),
            'unwrapped_zero_charge_max_error':float(np.max(abs(raw_charge))),
            'principal_branch_margin_at_corners':branch_margin,
            'guaranteed_product_neighborhood_Haar_measure':48.**(-12),
            'scope':'all corner checks challenge the explicit open-set witness; the probability floor uses the analytic local-density bound'}


def run():
    start=time.time()
    d={'heat_comparison':heat_comparison(),'geometry':local_geometry_and_orthogonality(),
       'circle_bounds':circle_kernel_bounds(),'principal_cube_event':principal_cube_event(),
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    d['seconds']=time.time()-start
    print(json.dumps(d,indent=2))


if __name__=='__main__':run()
