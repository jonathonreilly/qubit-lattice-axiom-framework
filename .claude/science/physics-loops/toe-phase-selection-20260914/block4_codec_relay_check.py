#!/usr/bin/env python3
"""Personal finite checks of the chart and relay; periodic routing is separate."""
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import norm
import sympy as sp


EPS = .25
BASIS = np.array([np.eye(2), [[0, 1], [1, 0]], [[0, -1j], [1j, 0]],
                  [[1, 0], [0, -1]]], dtype=complex)/np.sqrt(2)
VECTOR = np.array([1, 2, 3])


def rotations():
    out = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            r = np.zeros((3, 3), dtype=int)
            r[np.arange(3), permutation] = signs
            if round(np.linalg.det(r)) == 1:
                out.append(r)
    assert len(out) == 24
    return out


def matrix(z):
    return np.einsum('a,aij->ij', z, BASIS)


def coefficients(m):
    return np.einsum('aij,ij->a', BASIS.conj(), m)


def action(r, m):
    z = coefficients(m)
    return matrix(np.r_[z[0], r@z[1:]])


def center(role, frame):
    return np.r_[8*role, frame@VECTOR].astype(complex)


def encode(role, frame, z):
    rotated = np.r_[z[0], frame@z[1:]]
    return matrix(center(role, frame)+EPS*rotated/np.sqrt(1+np.vdot(z,z).real))


def decode(m, group):
    c = coefficients(m)
    role = round(c[0].real/8)
    frames = [norm(c-center(role,r)) for r in group]
    index = int(np.argmin(frames))
    r = group[index]
    y = c-center(role,r)
    remaining = EPS**2-np.vdot(y,y).real
    assert remaining > 0, 'No finite radial inverse on/outside the chart boundary'
    rotated = y/np.sqrt(remaining)
    return role, r, np.r_[rotated[0], r.T@rotated[1:]]


def codec_checks():
    group = rotations()
    points = [r@VECTOR for r in group]
    separation_squared = min(int(np.dot(x-y,x-y)) for i,x in enumerate(points)
                             for y in points[i+1:])
    assert separation_squared == 6 and 2*EPS < np.sqrt(separation_squared)
    rng = np.random.default_rng(49260914)
    max_inverse = max_covariance = max_product = 0.
    cases = 0
    for role in (-2, 0, 3):
        for r in group:
            z = rng.normal(size=4)+1j*rng.normal(size=4)
            encoded = encode(role, r, z)
            decoded_role, decoded_r, decoded_z = decode(encoded, group)
            assert role == decoded_role and np.array_equal(r, decoded_r)
            max_inverse = max(max_inverse, norm(z-decoded_z))
            for s in group:
                max_covariance = max(max_covariance,
                    norm(action(s,encoded)-encode(role,s@r,z)))
                # Verify the ambient rotation is a genuine star-algebra map,
                # not just a permutation of codec labels.
                a = matrix(z)
                b = matrix(rng.normal(size=4)+1j*rng.normal(size=4))
                max_product = max(max_product,norm(action(s,a@b)-action(s,a)@action(s,b)),
                                  norm(action(s,a.conj().T)-action(s,a).conj().T))
                cases += 1
    assert max_inverse < 1e-10 and max_covariance < 1e-12 and max_product < 1e-12
    jacobians = []
    for scale in (.1, .5, 1.5):
        u = scale*rng.normal(size=8)
        z = u[:4]+1j*u[4:]
        role, r = 1, group[7]
        def output(v):
            m = encode(role, r, v[:4]+1j*v[4:]).reshape(-1)
            return np.r_[m.real,m.imag]
        step = 3e-5
        numeric = np.column_stack([(output(u+step*np.eye(8)[j])-
                                    output(u-step*np.eye(8)[j]))/(2*step)
                                   for j in range(8)])
        actual = abs(np.linalg.det(numeric))
        expected = EPS**8/(1+np.dot(u,u))**5
        relative = abs(actual/expected-1)
        assert relative < 3e-6
        singular = np.linalg.svd(numeric,compute_uv=False)
        radial = EPS/(1+np.dot(u,u))**1.5
        tangential = EPS/np.sqrt(1+np.dot(u,u))
        assert abs(singular[-1]/radial-1) < 3e-6
        assert max(abs(singular[:-1]/tangential-1)) < 3e-6
        jacobians.append(dict(norm_squared=float(np.dot(u,u)), determinant=actual,
                              analytic_determinant=expected, relative_error=relative))
    return dict(frame_orbit=24, role_frame_group_cases=cases,
                frame_min_separation_squared=separation_squared,
                inverse_error=max_inverse, covariance_error=max_covariance,
                algebra_automorphism_error=max_product, jacobians=jacobians)


def measure_checks():
    def density(r, wrong=False, condition=False):
        if r <= 0 or r >= EPS:
            return 0.
        d = EPS**2-r*r
        source_square = r*r/d
        log_jacobian = -8*np.log(EPS) if wrong else 2*np.log(EPS)-5*np.log(d)
        exponent = 7*np.log(r)-source_square+log_jacobian-np.log(3)
        if condition:
            exponent += 3*np.log1p(source_square)-2*np.log(EPS)
        return np.exp(exponent)
    mass = quad(density,0,EPS,epsabs=1e-11)[0]
    wrong = quad(lambda r:density(r,wrong=True),0,EPS,epsabs=1e-11)[0]
    condition = quad(lambda r:density(r,condition=True),0,EPS,epsabs=1e-9)[0]
    assert abs(mass-1) < 1e-10
    assert abs(wrong-1) > .5
    assert abs(condition-193/EPS**2) < 1e-6
    tails = []
    for distance in (.05,.02,.01):
        r = EPS-distance
        square = r*r/(EPS**2-r*r)
        predicted = np.exp(-square)*sum(square**j/float(sp.factorial(j)) for j in range(4))
        actual = quad(density,r,EPS,epsabs=1e-12)[0]
        assert abs(actual-predicted) < 1e-10
        tails.append(dict(boundary_distance=distance, mass=actual, gamma_tail=predicted))
    return dict(normalized_mass=mass, wrong_constant_jacobian_mass=wrong,
                mean_squared_inverse_differential=condition,
                boundary_layer_probabilities=tails,
                support_boundary='zero_probability_but_in_measure_support; no finite inverse')


def relay_checks():
    aa = sp.Rational(2,5)+sp.I*sp.Rational(3,7)
    original = sp.Matrix([[3,aa],[sp.conjugate(aa),2]])
    cases = []
    for hidden_count in range(1,10):
        h = hidden_count
        hidden = sp.diag(*([2]*(h-1)+[1]))
        for j in range(h-1):
            hidden[j,j+1]=hidden[j+1,j]=1
        inverse = hidden.inv()
        assert hidden.det()==1 and inverse[0,0]==1 and inverse[h-1,h-1]==h
        assert inverse[0,h-1]==(-1)**(h-1)
        cross = sp.zeros(2,h)
        cross[0,0]=1
        cross[1,h-1]=(-1)**h*sp.conjugate(aa)
        visible = sp.diag(3+1,2+h*abs(aa)**2)
        recovered = sp.simplify(visible-cross*inverse*cross.conjugate().T)
        assert recovered==original
        full = visible.row_join(cross).col_join(cross.conjugate().T.row_join(hidden))
        assert sp.simplify(full.det()-original.det())==0
        assert np.linalg.eigvalsh(np.array(full,dtype=complex)).min()>0
        wrong_hidden = hidden.copy()
        wrong_hidden[-1,-1]=2
        wrong = sp.simplify(visible-cross*wrong_hidden.inv()*cross.conjugate().T)
        assert wrong != original
        cases.append(dict(path_edges=h+1, hidden_determinant=str(hidden.det()),
                          recovered_precision=[[str(v) for v in recovered.row(j)] for j in range(2)],
                          full_determinant=str(full.det())))
    return dict(complex_edge=str(aa), cases=cases)


def main():
    result=dict(codec=codec_checks(),measure=measure_checks(),relay=relay_checks(),
                status='author_checked_finite_tools; periodic_embedding_not_yet_constructed')
    Path(__file__).with_name('BLOCK4_CODEC_RELAY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
