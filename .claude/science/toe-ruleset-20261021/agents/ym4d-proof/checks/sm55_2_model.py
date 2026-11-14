# sm55_2 -- exact model check of the coarse-image two-scale bound and of "decay is not transparency".
# Criteria (with erratum, both before this script): checks/sm55_2_criteria.md. Exact sympy arithmetic only.
import itertools
import sympy as sp

A, M, tau, n = sp.symbols('A M tau n', positive=True)
Xvals = [sp.Integer(0), sp.Integer(1), sp.Integer(2)]
pX = sp.Rational(1, 3)
m = sum(pX * x**2 for x in Xvals)                       # E X^2 = 5/3

def EX(f):
    return sp.simplify(sum(pX * f(x) for x in Xvals))

# ---------- closed forms (K1-K6) ----------
EO_given = lambda x: x**2 - m
VarO_given = lambda x, AA=A, MM=M: (2 * AA**4 + 4 * AA**2 * x**2) / MM
K2_val = EX(lambda x: (x**2 - m)**2)                    # Cov(O_B, O_C) = Var(X^2)
VarF_cf = lambda AA, MM: sp.expand(EX(lambda x: (VarO_given(x, AA, MM) + (x**2 - m)**2)**2)
                                   - EX(lambda x: (x**2 - m)**2)**2)
EF_given = lambda x: (x**2 - m)**2
L2EF = sp.sqrt(EX(lambda x: (EF_given(x) - K2_val)**2))  # ||E[F|X] - EF||_2 (EF = K2_val)
CovFJ_cf = lambda t: sp.simplify(t * EX(lambda x: (x**2 - m)**3))
EJ_given = lambda x, t: t * (x**2 - m)

results = {}
results['K2_value_26/9'] = (K2_val == sp.Rational(26, 9))
results['K6_value_70/27'] = (CovFJ_cf(1) == sp.Rational(70, 27))

# ---------- exact enumeration with the three-point law ----------
s3 = sp.sqrt(3)
law3 = [(-s3, sp.Rational(1, 6)), (sp.Integer(0), sp.Rational(2, 3)), (s3, sp.Rational(1, 6))]
law2 = [(sp.Integer(-1), sp.Rational(1, 2)), (sp.Integer(1), sp.Rational(1, 2))]   # control Y4

def enumerate_model(MM, AA, law, tval, blocks_share=False):
    """Exact moments of the model for M = MM cells per block, amplitude AA. Returns dict of quantities."""
    EH2 = AA**2 * sum(p * xi**2 for xi, p in law) + m          # unconditional E H^2
    out = {'EO|X': {}, 'VarO|X': {}, 'CovFJ|X': {}, 'EF|X': {}, 'EJ|X': {}}
    tot = {'EF': 0, 'EJ': 0, 'EFJ': 0, 'EF2': 0, 'EOB': 0, 'EOC': 0, 'EOBOC': 0, 'EJ2': 0}
    nb = 2 if blocks_share else 3                                # blocks: B, C, (D)
    for x in Xvals:
        cond = {'EOB': 0, 'EOB2': 0, 'EF': 0, 'EJ': 0, 'EFJ': 0, 'EF2': 0, 'EOC': 0, 'EOBOC': 0, 'EJ2': 0}
        for cfg in itertools.product(law, repeat=nb * MM):
            p = sp.Integer(1)
            vals = []
            for xi, pr in cfg:
                p *= pr
                vals.append(AA * xi + x)
            def O(block):
                seg = vals[block * MM:(block + 1) * MM]
                return sp.Rational(1, MM) * sum(h**2 - EH2 for h in seg)
            OB, OC = O(0), O(1)
            OD = O(0 if blocks_share else 2)
            F = OB * OC
            J = OD - (1 - tval) * (x**2 - m)
            cond['EOB'] += p * OB; cond['EOB2'] += p * OB**2; cond['EOC'] += p * OC
            cond['EF'] += p * F; cond['EJ'] += p * J; cond['EFJ'] += p * F * J
            cond['EF2'] += p * F**2; cond['EOBOC'] += p * OB * OC; cond['EJ2'] += p * J**2
        cond = {k: sp.radsimp(sp.expand(v)) for k, v in cond.items()}
        out['EO|X'][x] = cond['EOB']
        out['VarO|X'][x] = sp.expand(cond['EOB2'] - cond['EOB']**2)
        out['CovFJ|X'][x] = sp.expand(cond['EFJ'] - cond['EF'] * cond['EJ'])
        out['EF|X'][x] = cond['EF']
        out['EJ|X'][x] = cond['EJ']
        for k in tot:
            tot[k] += pX * cond[k]
    tot = {k: sp.expand(v) for k, v in tot.items()}
    out['CovOBOC'] = sp.expand(tot['EOBOC'] - tot['EOB'] * tot['EOC'])
    out['VarF'] = sp.expand(tot['EF2'] - tot['EF']**2)
    out['CovFJ'] = sp.expand(tot['EFJ'] - tot['EF'] * tot['EJ'])
    out['VarJ'] = sp.expand(tot['EJ2'] - tot['EJ']**2)
    return out

T1_ok = True
for MM in (1, 2):
    for AA in (sp.Integer(1), sp.Integer(2)):
        for tval in (sp.Integer(1), sp.Rational(1, 2)):
            e = enumerate_model(MM, AA, law3, tval)
            for x in Xvals:
                T1_ok &= (sp.simplify(e['EO|X'][x] - EO_given(x)) == 0)
                T1_ok &= (sp.simplify(e['VarO|X'][x] - VarO_given(x, AA, MM)) == 0)
                T1_ok &= (sp.simplify(e['EF|X'][x] - EF_given(x)) == 0)
                T1_ok &= (sp.simplify(e['CovFJ|X'][x]) == 0)                  # K5
                T1_ok &= (sp.simplify(e['EJ|X'][x] - EJ_given(x, tval)) == 0)
            T1_ok &= (sp.simplify(e['CovOBOC'] - K2_val) == 0)                 # K2
            T1_ok &= (sp.simplify(e['VarF'] - VarF_cf(AA, MM)) == 0)          # K3
            T1_ok &= (sp.simplify(e['CovFJ'] - CovFJ_cf(tval)) == 0)          # K6
results['T1_closed_forms_vs_enumeration'] = bool(T1_ok)

# K3 leading term at A = n^2, M = n^4
VarF_n = sp.expand(VarF_cf(n**2, n**4))
results['K3_leading_4n^8'] = (sp.Poly(VarF_n, n).LC() == 4 and sp.Poly(VarF_n, n).degree() == 8)

# ---------- T2: corrected bound, n-uniform ----------
def osc(t):  # inf_c sup_X |E[J|X] - c| = half the range of E[J|X]
    vals = [EJ_given(x, t) for x in Xvals]
    return sp.simplify((sp.Max(*vals) - sp.Min(*vals)) / 2)
T2_ok = True
for t in (sp.Integer(1), sp.Rational(1, 2), sp.Rational(1, 10), sp.Integer(0)):
    lhs = sp.Abs(CovFJ_cf(t))
    rhs = 0 + L2EF * osc(t)                       # sup_X |Cov(F,J|X)| = 0 (K5)
    T2_ok &= bool(sp.simplify(rhs - lhs) >= 0)
    T2_ok &= (sp.diff(rhs, n) == 0)               # independent of n
results['T2_corrected_bound_valid_and_n_uniform'] = bool(T2_ok)

# ---------- T3: uncorrected (Var F) bound grows like n^4 ----------
T3_ok = True
for t in (sp.Integer(1), sp.Rational(1, 2), sp.Rational(1, 10)):
    # rhs = sqrt(VarF_n) * osc(t) >= (7/3) n^4 t  <=>  VarF_n * osc^2 >= (49/9) n^8 t^2
    diffp = sp.expand(VarF_n * osc(t)**2 - sp.Rational(49, 9) * n**8 * t**2)
    coeffs = sp.Poly(diffp, n).all_coeffs()
    T3_ok &= all(c >= 0 for c in coeffs)          # polynomial in n with nonnegative coefficients
    T3_ok &= (sp.Poly(VarF_n - 4 * n**8, n).all_coeffs() and
              all(c >= 0 for c in sp.Poly(VarF_n - 4 * n**8, n).all_coeffs()))
results['T3_varF_bound_not_uniform'] = bool(T3_ok)

# ---------- T4: slab variance diverges, separated covariance does not ----------
VarJ1 = sp.expand(EX(lambda x: VarO_given(x, n**2, n**4)) + EX(lambda x: (x**2 - m)**2))
results['T4_VarJ_2n^4_CovFJ_70/27'] = (sp.Poly(VarJ1, n).LC() == 2 and sp.Poly(VarJ1, n).degree() == 4
                                       and CovFJ_cf(1) == sp.Rational(70, 27))
# cross-check VarJ formula by enumeration at one point
e = enumerate_model(1, sp.Integer(1), law3, sp.Integer(1))
results['T4_VarJ_enumeration'] = (sp.simplify(e['VarJ'] - (EX(lambda x: VarO_given(x, 1, 1)) + K2_val)) == 0)

# ---------- controls ----------
controls = {}
# Y1: decay alone: |Cov(F,J)| <= sup_X|Cov(F,J|X)| = 0  fails at tau = 1
controls['Y1_decay_alone_fails'] = (sp.Abs(CovFJ_cf(1)) > 0)
# Y2: per-X constants c(X) make the second factor 0, bound claims 0 < 70/27
controls['Y2_pointwise_c_fails'] = (sp.Abs(CovFJ_cf(1)) > 0 + L2EF * 0)
# Y3: shared block (D := B): conditional covariance nonzero for some X
e_sh = enumerate_model(1, sp.Integer(1), law3, sp.Integer(1), blocks_share=True)
controls['Y3_no_conditional_decay_detected'] = any(sp.simplify(e_sh['CovFJ|X'][x]) != 0 for x in Xvals)
# Y4: two-point law breaks the closed form for Var(O|X)
e2 = enumerate_model(1, sp.Integer(2), law2, sp.Integer(1))
controls['Y4_wrong_fourth_moment_detected'] = any(sp.simplify(e2['VarO|X'][x] - VarO_given(x, 2, 1)) != 0
                                                  for x in Xvals)

for k in results:
    print(k, 'PASS' if results[k] else 'FAIL')
for k in controls:
    print(k, 'FIRED' if controls[k] else 'DID-NOT-FIRE')
print('Var(X^2) =', K2_val, '; Cov(F,J_1) =', CovFJ_cf(1), '; ||E[F|X]-EF||_2 =', sp.radsimp(L2EF))
print('Var F (A=n^2, M=n^4) =', VarF_n)
print('Var J_1 =', VarJ1)
print('Y3 conditional covariances (shared block, M=1, A=1):', [sp.simplify(e_sh['CovFJ|X'][x]) for x in Xvals])
verdict = all(results.values()) and all(controls.values())
print('VERDICT:', 'PASS' if verdict else 'FAIL')
