#!/usr/bin/env python3
"""Exact finite-interval controls, not a physical transport or infinite-tail model."""
from pathlib import Path
import sympy as s

AUDIT_INPUT_PATHS = ('docs/SUPPLIED_FINITE_INTERVAL_SIGNED_TRANSPORT_IDENTITY_NOTE_2026-10-24.md',)
AUDIT_TIMEOUT_SEC = 120


def propagator_value(w, source, initial, t, z, start=0):
    """Symbolic instance of (1); callers supply integrable fixture expressions."""
    u = s.Dummy('u', positive=True)
    initial_term = initial * s.exp(-s.integrate(w.subs(z, u), (u, start, t)))
    integrand = source * s.exp(-s.integrate(w.subs(z, u), (u, z, t)))
    return s.simplify(initial_term + s.integrate(integrand, (z, start, t)))


def main():
    t, z = s.symbols('t z', positive=True)
    checks = []
    def check(name, condition):
        ok = bool(condition)
        checks.append(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    def zero(expr):
        return s.simplify(expr) == 0
    # Fixed finite fixtures; no source fitted to an ODE numerical trajectory.
    fixtures = [
        ('positive constant source', s.Integer(2), s.Integer(2), 0, 1-s.exp(-2*t)),
        ('negative constant source', s.Integer(2), s.Integer(-2), 0, s.exp(-2*t)-1),
        ('nonzero initial homogeneous', s.Integer(2), s.Integer(0), 3, 3*s.exp(-2*t)),
        ('zero washout sign-changing source', s.Integer(0), 2*z-1, 2, 2+t*t-t),
        ('variable washout', 2*z, 2*z, 3, 1+2*s.exp(-t*t)),
        ('integrable endpoint singularity', 1/s.sqrt(z), s.Integer(0), 3, 3*s.exp(-2*s.sqrt(t))),
    ]
    for name, w, source, initial, expected in fixtures:
        result = propagator_value(w, source, initial, t, z)
        check(name+' integral identity', zero(result-expected))
        check(name+' ODE on t>0', zero(s.diff(expected,t)+w.subs(z,t)*expected-source.subs(z,t)))
        check(name+' initial limit', zero(s.limit(expected,t,0,dir='+')-initial))
        check(name+' finite endpoint t=1', zero(result.subs(t,1)-expected.subs(t,1)))
    signed = s.exp(-2)-1
    check('negative signed yield is not its absolute value', signed.is_negative is True and zero(s.Abs(signed)+signed))
    check('nonzero initial term cannot be dropped', (3*s.exp(-2)).is_positive is True)
    check('finite endpoint is not infinite-time replacement', (s.exp(-2)).is_positive is True and zero((1-s.exp(-2))-1+s.exp(-2)))
    # W=0,S=1 up to c, then W=2,S=-1 to 1, with B(0)=2.
    c=s.Rational(1,2)
    left=2+t
    at_c=left.subs(t,c)
    right=-s.Rational(1,2)+(at_c+s.Rational(1,2))*s.exp(-2*(t-c))
    # Global integral split at the jump, plus attenuated initial data.
    global_endpoint=(2*s.exp(-2*(1-c))
                     +s.integrate(s.exp(-2*(1-c)),(z,0,c))
                     +s.integrate(-s.exp(-2*(1-z)),(z,c,1)))
    check('piecewise fixture is continuous at jump', zero(left.subs(t,c)-right.subs(t,c)))
    check('piecewise left equation', zero(s.diff(left,t)-1))
    check('piecewise right equation', zero(s.diff(right,t)+2*right+1))
    check('piecewise global finite integral', zero(global_endpoint-right.subs(t,1)))
    note=(Path(__file__).resolve().parents[1]/AUDIT_INPUT_PATHS[0]).read_text()
    check('documentary scope markers only', all(x in note for x in ['L1([a,b])', 'almost everywhere', 'finite-interval only']))
    failed=sum(not c for c in checks)
    print(f'PASS={len(checks)-failed} FAIL={failed}')
    return int(bool(failed))

if __name__ == '__main__':
    raise SystemExit(main())
