"""Completeness cross-check: plain enumeration of every element of the covariant space W,
tested only by explicit Pauli-string commutation (no quadratic-form machinery)."""
import sys, time
from rv_linear import covariant_space, decode
from rv_classify import explicit_symplectic
rad = 1
PASS = FAIL = 0
expect = {'signf': 16, 'trivial': 132, 'sign': 132, 'axis': 1, 'full': 1}
for a in sys.argv[1:]:
    sites, basis = covariant_space(rad, a)
    n = 0
    d = len(basis)
    for c in range(1 << d):
        vec = 0
        for k in range(d):
            if (c >> k) & 1: vec ^= basis[k]
        PX, PZ = decode(vec, sites)
        if not PX or not PZ: continue
        if explicit_symplectic(PX, PZ, rad): n += 1
    ok = n == expect[a]
    PASS += ok; FAIL += (not ok)
    print(f'[{time.strftime("%H:%M:%S")}] brute force {a}: 2^{d} elements, symplectic={n} (reviewer QF-enumerator gave {expect[a]})', flush=True)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
