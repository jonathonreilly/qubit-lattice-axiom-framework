#!/usr/bin/env python3
"""Exact supplied-matrix algebra only; no numerical box or transport certificate."""
import sys
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/SPLIT2_CONDITIONAL_GENERATOR_COFACTOR_ALGEBRA_NOTE_2026-10-23.md', 'archive/notes/review_feedback/pr9852-split2-failed-certificate-2026-10-23/DISPOSITION.json']


def main():
    m, d, s = sp.symbols('m d s', real=True)
    x = sp.Symbol('x')
    e1, e2 = 2*sp.sqrt(6)/3, 2*sp.sqrt(2)/3
    tm = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    td = sp.Matrix([[0, -1, 1], [-1, 1, 0], [1, 0, -1]])
    tq = sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    h0 = sp.Matrix([[0, e1, -e1-sp.I/2], [e1, 0, -e2], [-e1+sp.I/2, -e2, 0]])
    h = h0 + m*tm + d*td + (e1-d+s)*tq
    g = td-tq
    checks = []

    def check(label, condition):
        ok = bool(condition)
        checks.append(ok)
        print(('PASS ' if ok else 'FAIL ') + label)

    def zero_matrix(matrix):
        return all(sp.simplify(v) == 0 for v in matrix)

    check('supplied family is Hermitian for real coordinates', zero_matrix(h-h.conjugate().T))
    check('fixed-slack delta derivative equals T_DELTA-T_Q', zero_matrix(h.diff(d)-g))
    for label, matrix, expected in [
        ('T_M', tm, (x-1)**2*(x+1)),
        ('T_Q', tq, (x-2)*(x+1)**2),
        ('fixed-slack generator', g, (x+2)*(x*x-2*x-2)),
    ]:
        actual = matrix.charpoly(x).as_expr()
        check(label+' exact characteristic polynomial', sp.expand(actual-expected) == 0)
        print(label+' polynomial = '+str(sp.factor(actual)))
    check('fixed-slack spectral norm is 1+sqrt(3)', sp.Max(2, sp.sqrt(3)-1, 1+sp.sqrt(3)) == 1+sp.sqrt(3))
    a = 4*sp.sqrt(6)/3-2*d+s
    b = m-d+s+2*(sp.sqrt(6)-sp.sqrt(2))/3
    expected = [x*x-d*d-b*b, (m-x)*(-d-x)-s*s-sp.Rational(1,4), (m-x)*(d-x)-a*a]
    shifted = h-x*sp.eye(3)
    for i, value in enumerate(expected):
        check('principal cofactor '+str(i)+' expansion', sp.simplify(shifted.minor_submatrix(i,i).det()-value) == 0)
    # The spectral-projector implication also needs the simple-spectrum proof in the note.
    check('adjugate identity for the supplied polynomial matrix', zero_matrix(shifted*shifted.adjugate()-shifted.det()*sp.eye(3)))
    for label, halfwidths, expected_radius in [
        ('CAP_BOX', (sp.Rational(1,400),sp.Rational(1,200),sp.Rational(1,200)), sp.Rational(7,400)+sp.sqrt(3)/200),
        ('ENDPOINT_BOX', (sp.Rational(1,400),sp.Rational(51,20000),sp.Rational(1,400)), sp.Rational(201,20000)+51*sp.sqrt(3)/20000),
    ]:
        hm, hd, hs = halfwidths
        radius = hm+(1+sp.sqrt(3))*hd+2*hs
        check(label+' exact generator-sum radius', sp.simplify(radius-expected_radius) == 0)
        print(label+' radius = '+str(radius))
    print('Conditional algebra only: Hermitian simple-spectrum projectors and real nonnegative box half-widths.')
    print('No floating enclosure, kernel extremum, numerical estimate, localization or physical selector is certified.')
    print(f'TOTAL: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}')
    return 0 if all(checks) else 1


if __name__ == '__main__':
    sys.exit(main())
