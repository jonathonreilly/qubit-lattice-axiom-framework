#!/usr/bin/env python3
"""Finite, distinct checks of the phase-corrector response identities.

The single-plaquette harmonic mean, electric inverse spectrum, character
Gram matrices, and cube cochains are computed by different constructions.
No growing-volume response estimate is asserted.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_FILES = ["block02_coupled_jump_and_response_check.py"]
import hashlib, importlib.util, itertools, json, math, time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.sparse import diags
from scipy.sparse.linalg import LinearOperator, cg, eigsh

HERE = Path(__file__).resolve().parent
PARENT = HERE / AUDIT_INPUT_FILES[0]
assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == "5981a5204073001efa670d996adfb45be698275e5a6ae8914ba88755e70f280b"
spec = importlib.util.spec_from_file_location("block02", PARENT)
block02 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(block02)


def finite_overlap(states, psi, shift):
    index = {tuple(n): j for j, n in enumerate(states)}
    return sum(float(psi[j] * psi[i]) for j, n in enumerate(states)
               if (i := index.get(tuple(n + shift))) is not None)


def one_plaquette():
    rows = []
    cutoff = 36
    n = np.arange(-cutoff, cutoff + 1)
    for g in [.7, 1., 1.5, 3.]:
        diagonal = 2*g*g*n*n + 1/(g*g)
        off = np.full(2*cutoff, -1/(2*g*g))
        vals, vecs = eigh_tridiagonal(diagonal, off)
        psi = vecs[:, 0]
        psi *= np.sign(psi[cutoff])
        observable = n*psi
        coefficients = vecs[:, 1:].T @ observable
        chi = 2*np.sum(coefficients**2/(vals[1:]-vals[0]))
        eta = 4*g*g*chi
        rho_spectral = 1-eta
        harmonic = []
        for grid in [4096, 8192]:
            x = 2*np.pi*np.arange(grid)/grid
            wave = psi @ np.cos(n[:, None]*x)
            assert wave.min() > 0
            p = wave*wave
            assert abs(p.mean()-1) < 2e-13
            harmonic.append(1/np.mean(1/p))
        assert abs(harmonic[-1]-harmonic[0]) < 1e-12
        assert abs(harmonic[-1]-rho_spectral) < 2e-11
        overlap = lambda k: float(np.dot(psi[:len(psi)-abs(k)], psi[abs(k):]))
        bounds = []
        for modes in [1, 2, 4, 8]:
            ns = np.arange(1, modes+1)
            J = np.array([k*overlap(k) for k in ns])
            Q = np.array([[2*k*l*(overlap(k+l)+overlap(k-l)) for l in ns] for k in ns])
            lower = 4*float(J @ np.linalg.solve(Q, J))
            assert lower <= eta+2e-10
            if bounds: assert lower >= bounds[-1]['eta_lower']-2e-10
            bounds.append({'modes': modes, 'eta_lower': lower, 'Gram_condition': float(np.linalg.cond(Q))})
        rows.append({'g':g, 'electric_cutoff':cutoff, 'eta_spectral':eta,
                     'rho_spectral':rho_spectral, 'rho_harmonic_mean':harmonic,
                     'rho_absolute_disagreement':abs(harmonic[-1]-rho_spectral),
                     'minimum_angle_probability':float(p.min()), 'character_bounds':bounds})
    return rows


def two_square():
    D, C = block02.actual_two_square_complex()
    G = C@C.T
    rows = []
    for g in [.6, .9, 1.4, 3.]:
        states, H, cosines = block02.rotor_matrix(12, g, G)
        states = states.astype(int)
        vals, vecs = eigsh(H, k=1, which='SA', v0=np.ones(len(states)), tol=2e-13)
        energy = vals[0]
        psi = vecs[:,0]
        psi *= np.sign(psi[len(states)//2])
        s = np.array([1., -1.])
        f = C.T @ np.linalg.solve(G,s)
        norm2 = float(f@f)
        v = (states@s)*psi
        v -= psi*np.dot(psi,v)
        A0 = H-diags(np.full(len(states),energy))
        inverse, info = cg(LinearOperator(H.shape, matvec=lambda x:A0@x+psi*np.dot(psi,x)), v,
                           rtol=2e-12, atol=1e-15, maxiter=8000)
        assert info == 0
        eta = 2*g*g*float(v@inverse)/norm2
        cache = {}
        def mu(r):
            key=tuple(r)
            if key not in cache: cache[key]=finite_overlap(states,psi,np.array(r))
            return cache[key]
        bounds=[]
        for radius in [1,2,3]:
            modes = [np.array(r) for r in itertools.product(range(-radius,radius+1),repeat=2)
                     if r[0]>0 or (r[0]==0 and r[1]>0)]
            J=np.array([float(s@r)*mu(r) for r in modes])
            Q=np.array([[float(r@G@u)*(mu(r+u)+mu(r-u))/2 for u in modes] for r in modes])
            eigenvalues=np.linalg.eigvalsh(Q)
            assert eigenvalues[0]>0
            lower=float(J@np.linalg.solve(Q,J))/norm2
            assert lower<=eta+2e-9
            if bounds: assert lower>=bounds[-1]['eta_lower']-2e-9
            bounds.append({'radius':radius,'characters':len(modes),'eta_lower':lower,
                           'smallest_Gram_eigenvalue':float(eigenvalues[0]),'Gram_condition':float(eigenvalues[-1]/eigenvalues[0])})
        units=np.eye(2,dtype=int)
        means=np.array([mu(r) for r in units])
        cos_products=np.array([[(mu(r+u)+mu(r-u))/2 for u in units] for r in units])
        M=G*cos_products
        h=np.linalg.solve(G,s)/means
        # Check the algebraically cancelled mean-gradient term with
        # compensated scalar sums. The raw subtraction of two ~4200
        # terms at g=3 is reported separately; its roundoff is not a
        # defect of the covariance identity.
        denominator=math.fsum(float(h[i]*h[j]*G[i,j]*cos_products[i,j])
                              for i in range(2) for j in range(2))
        covariance_part=math.fsum(float(h[i]*h[j]*G[i,j]*(cos_products[i,j]-means[i]*means[j]))
                                  for i in range(2) for j in range(2))
        mean_gradient=C.T@(h*means)
        direct_mean_norm=float(mean_gradient@mean_gradient)
        assert abs(direct_mean_norm-norm2)<1e-13
        decomposition_residual=math.fsum(float(h[i]*h[j]*G[i,j]*means[i]*means[j])
                                        for i in range(2) for j in range(2))-norm2
        assert abs(decomposition_residual)<1e-13
        assert covariance_part>=-1e-13
        plaquette_bound=norm2/denominator
        assert plaquette_bound<=eta+2e-9
        rows.append({'g':g,'eta_spectral':eta,'character_bounds':bounds,
                     'specified_plaquette_eta_lower':plaquette_bound,
                     'cosine_covariance_cost':covariance_part,'f_norm_squared':norm2,
                     'decomposition_compensated_residual':decomposition_residual,
                     'large_term_subtraction_residual':denominator-norm2-covariance_part})
    return rows


def cube_check():
    vertices=list(itertools.product(range(2),repeat=3))
    vertex_set=set(vertices)
    def step(x,a):
        y=list(x);y[a]+=1;return tuple(y)
    edges=[(x,a) for x in vertices for a in range(3) if step(x,a) in vertex_set]
    index={edge:j for j,edge in enumerate(edges)}
    faces=[]
    for x in vertices:
        for a,b in itertools.combinations(range(3),2):
            if step(step(x,a),b) in vertex_set: faces.append((x,a,b))
    C=np.zeros((len(faces),len(edges)),dtype=int)
    for p,(x,a,b) in enumerate(faces):
        for edge,sign in [((x,a),1),((step(x,a),b),1),((step(x,b),a),-1),((x,b),-1)]:
            C[p,index[edge]]=sign
    _,singular,Vh=np.linalg.svd(C.T,full_matrices=True)
    z=np.sign(Vh[-1]).astype(int)
    assert np.array_equal(C.T@z,np.zeros(len(edges),dtype=int))
    assert np.linalg.matrix_rank(C)==5
    rows=[]
    for a in [.05,.2,.7]:
        F=z*np.array([a,a,-2*a,0.,0.,0.])
        theta=np.linalg.lstsq(C,F,rcond=None)[0]
        assert np.linalg.norm(C@theta-F)<1e-14
        grad=C.T@z
        cost=float(grad@grad)
        assert cost>0
        h=1e-6
        gradient_fd=np.array([(z@np.sin(C@(theta+h*np.eye(len(edges))[j]))-
                               z@np.sin(C@(theta-h*np.eye(len(edges))[j])))/(2*h)
                              for j in range(len(edges))])
        assert np.linalg.norm(gradient_fd-grad)<2e-9
        rows.append({'a':a,'flux':F.tolist(),'real_Bianchi_residual':float(z@F),
                     'sine_Bianchi_value':float(z@np.sin(F)),
                     'nonlinear_gradient_squared':cost,'finite_difference_error':float(np.linalg.norm(gradient_fd-grad))})
    return {'curl':C.tolist(),'signed_cube_boundary':z.tolist(),'rows':rows}


def run():
    start=time.time()
    result={'one_plaquette':one_plaquette(),'two_square':two_square(),'cube':cube_check()}
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['parent_sha256']=hashlib.sha256(PARENT.read_bytes()).hexdigest()
    result['seconds']=time.time()-start
    print(json.dumps(result,indent=2))


if __name__=='__main__':run()
