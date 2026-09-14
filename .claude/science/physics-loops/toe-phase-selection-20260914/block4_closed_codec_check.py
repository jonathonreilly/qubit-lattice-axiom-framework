#!/usr/bin/env python3
"""Exact tests of the optional Borel completion; it is not continuous."""
import json
from pathlib import Path
import sympy as s

EPS=s.Rational(1,4)


def ordinary(r):
    return s.simplify(EPS*r/s.sqrt(1+r*r))


def radius_encode(r):
    if r.is_Integer and r > 0:
        return EPS if r==1 else ordinary(r-1)
    return ordinary(r)


def radius_decode(t):
    if s.simplify(t-EPS)==0:
        return s.Integer(1)
    candidate=s.simplify(t/s.sqrt(EPS*EPS-t*t))
    if candidate.is_Integer and candidate > 0:
        return candidate+1
    return candidate


def main():
    radii=[s.Integer(n) for n in range(12)]+[s.sqrt(2),s.Rational(7,3),s.Rational(1,100)]
    cases=[]
    for r in radii:
        image=radius_encode(r)
        back=radius_decode(image)
        assert s.simplify(back-r)==0
        assert 0 <= image <= EPS
        cases.append(dict(radius=str(r),image=str(image),inverse=str(back)))
    targets=[EPS,s.Integer(0),ordinary(s.Integer(1)),ordinary(s.Integer(4)),EPS/3]
    for t in targets:
        assert s.simplify(radius_encode(radius_decode(t))-t)==0
    # An eight-real-coordinate unit vector has all payload coordinates active.
    unit=s.Matrix(range(1,9))/s.sqrt(204)
    assert (unit.T*unit)[0]==1
    for r in radii[1:]:
        z=r*unit
        encoded=radius_encode(r)*unit
        decoded=radius_decode(s.sqrt((encoded.T*encoded)[0]))*unit
        assert s.simplify(decoded-z)==s.zeros(8,1)
    # Explicit discontinuity, rather than an implied smoothness inheritance.
    gap=s.simplify(EPS-ordinary(s.Integer(1)))
    assert gap>0
    result=dict(exact_radial_cases=cases,all_eight_coordinates=True,
                boundary_inverse_radius=str(radius_decode(EPS)),
                jump_at_radius_one=str(gap),
                measure_argument='maps differ only on countably many Lebesgue-null spheres',
                scope='Borel equivariant bijection to closed chart; not continuous or finite-precision stable')
    Path(__file__).with_name('BLOCK4_CLOSED_CODEC_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
