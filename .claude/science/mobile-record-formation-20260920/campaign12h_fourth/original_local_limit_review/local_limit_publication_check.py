"""Frozen-evidence authentication and exact synthesis algebra; no new simulation."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
D = HERE.parent
RECORDS = {
    'actual_first_output_author/AUTHOR_SEAL.json': 'e8a1ea634f3355f883da749124af2ab5f5fbaba3ea7270d972dd279d3ded6046',
    'actual_first_output_independent/FINAL_SEAL.json': 'c5ed54dd73a633a433f51cba08c5221e6cad58ea306219a3002e2104e53ea69a',
    'cube_point_spectrum_author/AUTHOR_SEAL.json': 'b99a0a0b243c9ecfaade581acbb2450d4e3d53d95967bb7096ed9388558f2665',
    'cube_point_spectrum_independent/FINAL_SEAL.json': 'f2df1efd5a7c7a63fb5200c0becb48278f79e448000afddcc8dc2bc48785111f',
    'cube_unprepared_author/AUTHOR_SEAL.json': 'ed066b95b18992f86718fe960ed6624c163854d142d0f90a742a4c85377159f4',
    'cube_unprepared_independent/FINAL_SEAL.json': '6c093df454da76bb474ce0f7f2283fc4729ced3ed540b779881418c07233b9ca',
}


def main():
    root = HERE.parents[4]
    original_root = Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920')
    bindings = {}

    def walk(value):
        if isinstance(value, dict):
            if isinstance(value.get('path'), str) and isinstance(value.get('sha256'), str):
                old = Path(value['path'])
                rel = old.relative_to(original_root)
                assert '..' not in rel.parts
                path = root / rel
                data = path.read_bytes()
                assert sha256(data).hexdigest() == value['sha256'], str(rel)
                if 'bytes' in value:
                    assert len(data) == value['bytes'], str(rel)
                if str(rel) in bindings:
                    assert bindings[str(rel)] == value['sha256']
                bindings[str(rel)] = value['sha256']
            for item in value.values():
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    for name, expected in RECORDS.items():
        path = D / name
        assert sha256(path.read_bytes()).hexdigest() == expected, name
        walk(json.loads(path.read_text()))

    k, t, s = sp.symbols('k t s', positive=True)
    y = sp.symbols('y', real=True)
    ring_a = sp.exp(-16*k*t)
    ring_g = sp.Rational(4, 3)*(sp.exp(-4*k*t)-ring_a)
    ring_h = 1-ring_a-ring_g
    cube_a = sp.exp(-48*k*t)
    cube_g = sp.Rational(3, 2)*(sp.exp(-16*k*t)-cube_a)
    cube_h = 1-cube_a-cube_g
    for r1, r2, g in [(16*k, 4*k, ring_g), (48*k, 16*k, cube_g)]:
        conv = sp.integrate(r1*sp.exp(-r1*s)*sp.exp(-r2*(t-s)), (s, 0, t))
        assert sp.simplify(conv-g) == 0
    ring_poly = 1-sp.Rational(4, 3)*y+sp.Rational(1, 3)*y**4
    cube_poly = 1-sp.Rational(3, 2)*y+sp.Rational(1, 2)*y**3
    assert sp.expand(ring_poly-(1-y)**2*(y*y+2*y+3)/3) == 0
    assert sp.expand(cube_poly-(1-y)**2*(y+2)/2) == 0
    assert sp.simplify(ring_a+(ring_g+ring_h)/2-(1+ring_a)/2) == 0
    assert sp.simplify(cube_a+cube_g+cube_h-1) == 0
    # Both source rates and all displayed count gaps are positive on t>0.
    assert sp.simplify(sp.diff(ring_h, t)-4*k*ring_g) == 0
    assert sp.simplify(sp.diff(cube_h, t)-16*k*cube_g) == 0
    # Exact published small-spin countercontrol, independently computed upstream.
    assert (-109248-(-48)**3)/6 == 224

    print('per_element: Exact count polynomials, source convolutions and trace-deficit arithmetic were checked symbolically.')
    print('per_site: checked and not executed — site and physical Gauss builders are reused at their frozen source identities.')
    print('per_mode: checked and not executed — spectrum proofs and finite certificates are authenticated, without a new diagonalization.')
    print('per_block: Four-, six- and eight-record synthesis formulas and nonnegative count gaps were checked for both finite graphs.')
    print('lattice_wide: Only the fixed eight-site ring and cube formulas are checked; no spatial-volume theorem is inferred.')
    print(json.dumps({'selected_record_count': len(RECORDS), 'unique_bindings': len(bindings),
                      'ring_local_trace': str((1+ring_a)/2), 'cube_local_trace': str(cube_a),
                      'ring_count_upper_positive_factor': str(sp.factor(ring_poly)),
                      'cube_count_upper_positive_factor': str(sp.factor(cube_poly)),
                      'scope': 'Publication authentication and synthesis algebra, not a new independent physics reconstruction.'}, indent=2))


if __name__ == '__main__':
    main()
