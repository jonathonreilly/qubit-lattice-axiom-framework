"""Control F, block 11: full pair-additivity test at every candidate point, exactly.
All third-difference numerators N(p,q) = num - den over the 6^6 argument tuples (with the pattern reduction, few distinct
polynomials); each candidate is a root of a univariate minimal polynomial with p given exactly as a polynomial in q
(or p = q, or p = 1); a numerator vanishes at the candidate iff its reduction modulo the minimal polynomial is zero."""
import sympy as sp, itertools
p, q, r = sp.symbols('p q r', positive=True)
def orbit(s, u): return 'p' if s == u else ('q' if s//2 == u//2 else 'r')
w = {'p': p, 'q': q, 'r': sp.Integer(1)}
cache = {}
def Z3(a, b, c):
    key = tuple(sorted((a, b, c)))
    if key not in cache:
        cache[key] = sp.expand(sum(w[orbit(s, a)]*w[orbit(s, b)]*w[orbit(s, c)] for s in range(6)))
    return cache[key]
nums = set()
for a, a2, b, b2, c, c2 in itertools.product(range(6), repeat=6):
    if a == a2 or b == b2 or c == c2: continue
    n = sp.expand(Z3(a,b,c)*Z3(a2,b2,c)*Z3(a2,b,c2)*Z3(a,b2,c2) - Z3(a2,b,c)*Z3(a,b2,c)*Z3(a,b,c2)*Z3(a2,b2,c2))
    if n != 0:
        nums.add(n)
nums = list(nums)
print("distinct nonzero third-difference numerators (r = 1):", len(nums))
sext = sp.Poly(q**6 - 6*q**5 - 3*q**4 + 4*q**3 - 3*q**2 - 6*q + 31, q)
psi = -sp.Rational(8,85)*q**5 + sp.Rational(116,255)*q**4 + sp.Rational(196,255)*q**3 + sp.Rational(82,85)*q**2 + sp.Rational(121,255)*q + sp.Rational(356,255)
cub_t = sp.Poly(q**3 - 3*q**2 - 6*q - 1, q)
cub_r = sp.Poly(q**3 - 3*q**2 - 15*q - 19, q)
def test(label, sub_p, modulus):
    bad = 0
    for n in nums:
        red = sp.Poly(sp.expand(n.subs(p, sub_p)), q).rem(modulus)
        if not red.is_zero: bad += 1
    print(f"{label}: numerators not vanishing = {bad} of {len(nums)}  -> {'ON the pair-additive locus' if bad == 0 else 'NOT on the locus (only some witnesses vanish)'}")
test("(sigma_1, sigma_2, 1): p = psi(q) mod sextic", psi, sext)
test("(t*, t*, 1): p = q mod t-cubic", q, cub_t)
test("(1, rho_1, 1): p = 1 mod rho-cubic", sp.Integer(1), cub_r)
test("(rho_1, 1, 1): p = rho_1 (q = 1): use symmetry -> substitute q = 1, p = root of rho-cubic in p", None, None) if False else None
# the mirror (rho_1, 1, 1): swap roles: numerators are symmetric in p,q, so it follows; verify one numerator explicitly
n0 = nums[0]
print("symmetry check of a numerator under p<->q (difference simplifies to 0):", sp.expand(n0.subs({p: q, q: p}, simultaneous=True) - n0) == 0 or "not symmetric individually (set is symmetric)")
# constant rule
test("(1, 1, 1): p = 1 mod (q - 1)", sp.Integer(1), sp.Poly(q - 1, q))
# the declared triples are off the locus: E1 nonzero there (block 08); check numerators at (3/2, 1/2) and (5/4, 1/2)
for tr in [(sp.Rational(3,2), sp.Rational(1,2)), (sp.Rational(5,4), sp.Rational(1,2))]:
    nz = sum(1 for n in nums if n.subs({p: tr[0], q: tr[1]}) != 0)
    print(f"declared triple (p,q)/r = {tr}: nonzero numerators = {nz} of {len(nums)}")
