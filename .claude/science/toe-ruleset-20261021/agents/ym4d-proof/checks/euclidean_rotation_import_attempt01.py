#!/usr/bin/env python3
"""Finite geometry and exact algebra diagnostics; no continuum certification."""
import itertools as it
import json
from fractions import Fraction as Q
import sympy as sp


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def basis(j, d=4):
    return tuple(int(i == j) for i in range(d))


def reflect(x, j, k, sign):
    y = list(x)
    y[j], y[k] = -sign * x[k], -sign * x[j]
    return tuple(y)


def diagonal_geometry():
    records = []
    for j, k in it.combinations(range(4), 2):
        for sign in (-1, 1):
            height = lambda x: x[j] + sign * x[k]
            crossing = 0
            tested = 0
            for x in it.product(range(-2, 3), repeat=4):
                for a, b in it.combinations(range(4), 2):
                    vertices = (x, add(x, basis(a)),
                                add(add(x, basis(a)), basis(b)),
                                add(x, basis(b)))
                    tested += 1
                    h = list(map(height, vertices))
                    if min(h) < 0 < max(h):
                        crossing += 1
                        assert sorted(h) == [-1, 0, 0, 1]
                        assert set(map(lambda v: reflect(v, j, k, sign), vertices)) == set(vertices)
                        zeros = [i for i, v in enumerate(h) if v == 0]
                        assert (zeros[0] - zeros[1]) % 4 == 2
                        p, q = zeros
                        plus = next(i for i, v in enumerate(h) if v > 0)
                        minus = next(i for i, v in enumerate(h) if v < 0)
                        assert reflect(vertices[plus], j, k, sign) == vertices[minus]
                        assert reflect(vertices[p], j, k, sign) == vertices[p]
                        assert reflect(vertices[q], j, k, sign) == vertices[q]
            records.append(dict(axes=[j, k], sign=sign, tested=tested, crossing=crossing))
    return records


def qmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def qconj(x):
    return (x[0], -x[1], -x[2], -x[3])


def path_algebra():
    a = tuple(map(Q, [Q(3, 5), Q(4, 5), 0, 0]))
    b = tuple(map(Q, [Q(5, 13), 0, Q(12, 13), 0]))
    c = tuple(map(Q, [Q(8, 17), 0, 0, Q(15, 17)]))
    d = tuple(map(Q, [Q(7, 25), Q(24, 25), 0, 0]))
    for x in (a, b, c, d):
        assert sum(t*t for t in x) == 1
    assert qmul(a, b) != qmul(b, a)
    p, q = qmul(a, b), qmul(c, d)
    direct = 2*qmul(qmul(qmul(a, b), qconj(d)), qconj(c))[0]
    factor = 2*sum(x*y for x, y in zip(p, q))
    wrong = 2*qmul(p, q)[0]
    assert direct == factor and wrong != factor
    # exp[lambda Re tr(P Q*)] on {I,-I} has eigenvalue
    # exp(2 lambda)-exp(-2 lambda) on (1,-1), negative for lambda<0.
    return dict(direct_trace=str(direct), matrix_entry_factorization=str(factor),
                wrong_path_orientation=str(wrong), orientation_mutation_fired=True,
                negative_coefficient_witness="(1,-1): 2*(exp(2*lambda)-exp(-2*lambda))<0 for lambda<0")


def support_footprints():
    records = []
    for L in (3, 5, 9):
        h = (L-1)//2
        offsets = list(it.product(range(-h, h+1), repeat=4))
        # Every actual S4' path lies in its two endpoint blocks.
        # A center with x0-x1=L has min height exactly one fine unit.
        center = (L, 0, 0, 0)
        heights = [add(center, x)[0]-add(center, x)[1] for x in offsets]
        assert min(heights) == 1
        boundary = (0, 0, 0, 0)
        boundary_heights = [add(boundary, x)[0]-add(boundary, x)[1] for x in offsets]
        assert min(boundary_heights) == -(L-1) < 0
        # Actual contour: center -> y -> y+L e2 -> next center,
        # y=(-h,h,0,0) occurs in the prescribed averaging family.
        witness_y = (-h, h, 0, 0)
        assert witness_y[0]-witness_y[1] < 0
        records.append(dict(L=L, strict_positive_block_min=min(heights),
                            plane_block_min=min(boundary_heights),
                            actual_contour_y=witness_y))
    clover_offsets = set()
    for j, k in it.combinations(range(4), 2):
        for sj, sk in it.product((-1, 1), repeat=2):
            clover_offsets.update([(0, 0, 0, 0), tuple(sj*x for x in basis(j)),
                tuple(sk*x for x in basis(k)),
                add(tuple(sj*x for x in basis(j)), tuple(sk*x for x in basis(k)))])
    heights = [x[0]+x[1] for x in clover_offsets]
    assert min(heights) == -2 and max(heights) == 2
    return dict(blocks=records, clover_diagonal_height_radius=2,
                center_height_one_crosses=min(heights)+1 < 0,
                center_height_two_stays_closed_positive=min(heights)+2 == 0)


def torus_geometry():
    n = 4
    vertices = set(it.product(range(n), repeat=2))
    fixed = {x for x in vertices if x[0] == x[1]}
    remaining = vertices-fixed
    seed = min(remaining)
    component = {seed}
    frontier = [seed]
    while frontier:
        v = frontier.pop()
        for j, sign in it.product(range(2), (-1, 1)):
            w = list(v); w[j] = (w[j]+sign) % n; w = tuple(w)
            if w in remaining and w not in component:
                component.add(w); frontier.append(w)
    assert component == remaining
    p = ((3, 0), (0, 0), (0, 1), (3, 1))
    rp = tuple((b, a) for a, b in p)
    assert set(p) != set(rp)
    assert len(set(p)&fixed) == 1
    return dict(side=n, complement_vertices=len(remaining), connected_component_vertices=len(component),
                wrapping_plaquette=p, reflected_plaquette=rp, fixed_vertices=sorted(set(p)&fixed),
                free_box_factorization_transfer_mutation_fired=True)


def gaussian_torus_control():
    n = 4
    sites = list(it.product(range(n), repeat=2)); index = {x:i for i,x in enumerate(sites)}
    lap = 5*sp.eye(n*n) # m²=1 plus degree four
    for x in sites:
        for j, s in it.product(range(2), (-1, 1)):
            y=list(x); y[j]=(y[j]+s)%n
            lap[index[x],index[tuple(y)]] -= 1
    cov = lap.inv()
    pos = [x for x in sites if x[0] > x[1]]
    gram = sp.Matrix([[cov[index[(a[1],a[0])],index[b]] for b in pos] for a in pos])
    witnesses=[]
    for size in range(1,len(pos)+1):
        for ids in it.combinations(range(len(pos)),size):
            det=gram.extract(ids,ids).det()
            if det<0:
                witnesses.append(dict(sites=[pos[i] for i in ids],principal_minor=str(det)))
                break
        if witnesses: break
    assert witnesses
    return dict(model="2D massive scalar Gaussian, periodic square side 4, m²=1", witnesses=witnesses,
                scope="Separate-model diagonal-RP counterexample only; no Wilson verdict")


def analytic_controls():
    # F=(sum partial_j^4)phi in d=4, m=1.
    p=sp.symbols('p0:4'); c=sp.Rational(3,5);s=sp.Rational(4,5)
    rot=(c*p[0]+s*p[1], -s*p[0]+c*p[1], p[2],p[3])
    original=sum(t**4 for t in p)**2
    rotated=sum(t**4 for t in rot)**2
    numerator=sp.expand(rotated-original)
    denominator=sum(t*t for t in p)+1
    quotient,remainder=sp.div(numerator,denominator,p[0])
    pole=sp.simplify(numerator.subs({p[0]:sp.I,p[1]:0,p[2]:0,p[3]:0}))
    assert remainder != 0 and pole == -sp.Rational(277056,390625)
    # Isotropic derivative (Laplacian)^2 is the no-defect control.
    iso=sp.expand(sum(t*t for t in rot)**4-sum(t*t for t in p)**4)
    assert iso==0
    # Uniform L² bound is impossible: ratio at p=(r,0,0,0) is r^8/(r²+1).
    r=sp.symbols('r',positive=True)
    assert sp.limit(r**8/(r*r+1),r,sp.oo)==sp.oo
    # Independently evaluate the exact Gaussian-square Laplace integral.
    x,t=sp.symbols('x t',real=True)
    val=sp.integrate(sp.exp(-x*x/4)/sp.sqrt(2*sp.pi),(x,-sp.oo,sp.oo))
    assert val==sp.sqrt(2) # E exp(G²/4)=sqrt(2), singularity at t=1/2.
    return dict(anisotropic_derivative_pole_defect=str(pole),
                nonzero_polynomial_remainder=str(remainder),
                isotropic_mutation_defect=str(iso),
                covariance_multiplier_unbounded_on_L2=True,
                gaussian_square_laplace="E exp[t(G²-1)]=exp(-t)/sqrt(1-2t), t<1/2; infinite for t>=1/2",
                gaussian_square_cumulants="kappa_n=2^(n-1)*(n-1)! for n>=2; kappa_1=0")


def main():
    result = dict(diagonal_geometry=diagonal_geometry(), nonabelian_path=path_algebra(),
                  support_footprints=support_footprints(), torus_geometry=torus_geometry(),
                  gaussian_torus=gaussian_torus_control(), analytic=analytic_controls(),
                  target_status=dict(full_ym4_existence="OPEN",physical_continuum_mass_gap="OPEN"))
    result['resolution_certificate'] = {
        'per_element': 'Exact noncommuting SU(2) two-path identity and orientation mutation checked.',
        'per_site': 'Clover corner support and diagonal buffer two fine units checked.',
        'per_mode': 'Rational Gaussian covariance pole defect checked; no Yang–Mills spectrum computed.',
        'per_block': 'Centered block footprints checked; boundary blocks cross and strict blocks do not.',
        'lattice_wide': 'Finite periodic topology and separate Gaussian Gram witness checked; no continuum existence estimate executed.'}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
