#!/usr/bin/env python3
"""T68 test: what does linearised relabelling invariance (group G) do to the
'declared' numbers of the curvature member?

Exact rational arithmetic (sympy).  Pre-registration: PREREG.md (same folder).

Objects
  h_{mu nu}  symmetric 4x4 (10 comps), Euclidean momentum k=(k0,k1,k2,k3)
  Q(h,k)     real quadratic form, degree 2 in h and degree 2 in k (leading symbol
             of a local two-derivative action)
  S3T        signed permutations of the 3 space axes x time reversal (96 elems)
  B4         signed permutations of all 4 axes (384 elems)
  G          h -> h + k xi^T + xi k^T   (linearised relabelling, time-space mixing incl.)
"""
import itertools, sys, json
import sympy as sp
from sympy import Rational as R

# ---------- variables ----------
pairs = [(m, n) for m in range(4) for n in range(m, 4)]          # 10 h variables
hidx = {p: i for i, p in enumerate(pairs)}
hs = sp.symbols('h00 h01 h02 h03 h11 h12 h13 h22 h23 h33')
ks = sp.symbols('k0 k1 k2 k3')
xis = sp.symbols('x0 x1 x2 x3')
NV = 14   # var ids: 0..9 = h, 10..13 = k

def hvar(m, n):
    return hidx[(min(m, n), max(m, n))]

# ---------- group ----------
def signed_perms(axes):
    out = []
    for perm in itertools.permutations(axes):
        for signs in itertools.product([1, -1], repeat=len(axes)):
            out.append((perm, signs))
    return out

def build_group(kind):
    els = []
    if kind == 'S3T':
        for (perm, signs) in signed_perms([1, 2, 3]):
            for t in (1, -1):
                pi = {0: 0}; sg = {0: t}
                for a, p, s in zip([1, 2, 3], perm, signs):
                    pi[a] = p; sg[a] = s
                els.append((pi, sg))
    elif kind == 'B4':
        for (perm, signs) in signed_perms([0, 1, 2, 3]):
            pi = {a: p for a, p in zip([0, 1, 2, 3], perm)}
            sg = {a: s for a, s in zip([0, 1, 2, 3], signs)}
            els.append((pi, sg))
    return els

def act_var(g, v):
    """image of variable id v under group element g: (sign, new_id)"""
    pi, sg = g
    if v < 10:
        m, n = pairs[v]
        return sg[m] * sg[n], hvar(pi[m], pi[n])
    m = v - 10
    return sg[m], 10 + pi[m]

def act_mono(g, mono):
    s = 1; new = []
    for v in mono:
        sv, nv = act_var(g, v)
        s *= sv; new.append(nv)
    return s, tuple(sorted(new))

# monomials: two h's and two k's
monos = []
for a in itertools.combinations_with_replacement(range(10), 2):
    for b in itertools.combinations_with_replacement(range(10, 14), 2):
        monos.append(tuple(sorted(a + b)))
assert len(monos) == 550

def invariant_forms(group):
    seen = set(); forms = []
    for m in monos:
        if m in seen:
            continue
        orbit = {}
        bad = False
        for g in group:
            s, m2 = act_mono(g, m)
            if m2 in orbit and orbit[m2] != s:
                bad = True
            orbit.setdefault(m2, s)
        for m2 in orbit:
            seen.add(m2)
        # orbit sum: sum over group elements of g.m  (coefficient of m2 = s * count)
        if bad:
            continue
        # counts equal for all elements of an orbit; use sign map
        form = {m2: s for m2, s in orbit.items()}
        forms.append(form)
    return forms

def to_expr(form):
    syms = list(hs) + list(ks)
    e = 0
    for mono, c in form.items():
        t = c
        for v in mono:
            t = t * syms[v]
        e += t
    return e

# ---------- (P1) classification ----------
def gauge_subs(expr):
    """Q(h + k xi^T + xi k^T, k)"""
    sub = {}
    for (m, n) in pairs:
        sub[hs[hidx[(m, n)]]] = hs[hidx[(m, n)]] + ks[m] * xis[n] + ks[n] * xis[m]
    return expr.subs(sub, simultaneous=True)

def g_invariant_combos(forms):
    exprs = [to_expr(f) for f in forms]
    cs = sp.symbols('c0:%d' % len(forms))
    Qg = sum(c * e for c, e in zip(cs, exprs))
    diff = sp.expand(gauge_subs(Qg) - Qg)
    poly = sp.Poly(diff, *(list(hs) + list(ks) + list(xis)))
    eqs = list(poly.coeffs())
    M = sp.Matrix([[sp.diff(eq, c) for c in cs] for eq in eqs])
    ns = M.nullspace()
    return exprs, [sum(v[i] * exprs[i] for i in range(len(exprs))) for v in ns]

def main():
    res = {}
    print('== S3T group (space signed perms x time reversal) ==')
    forms = invariant_forms(build_group('S3T'))
    print('S3T-invariant forms:', len(forms), '(P4 T1 says 26)')
    exprs, fam = g_invariant_combos(forms)
    print('S3T + G invariant:', len(fam), '(P4 T1 says 2)')
    res['S3T_invariant'] = len(forms); res['S3T_G_invariant'] = len(fam)

    print('== B4 group ==')
    formsB = invariant_forms(build_group('B4'))
    exprsB, famB = g_invariant_combos(formsB)
    print('B4-invariant:', len(formsB), 'B4+G:', len(famB), '(P4 T2 says 9, 1)')
    res['B4_invariant'] = len(formsB); res['B4_G_invariant'] = len(famB)

    h = sp.Matrix(4, 4, lambda m, n: hs[hidx[(min(m, n), max(m, n))]])
    kvec = sp.Matrix(ks)

    # ---------- read-off functions ----------
    def kinetic(Q):
        sub = {hs[hidx[(0, n)]]: 0 for n in range(4)}
        sub.update({ks[1]: 0, ks[2]: 0, ks[3]: 0})
        q = sp.expand(Q.subs(sub))
        q = sp.expand(q / ks[0]**2)
        Ad = sp.expand(q).coeff(hs[hidx[(1, 1)]], 2)
        Ao = sp.expand(q).coeff(hs[hidx[(1, 2)]], 2)
        # coefficient of h11*h22 gives 2*B - ... : q = Ad*sum hii^2 + Ao*sum_{i<j} hij^2 + B (tr)^2
        x12 = sp.expand(q).coeff(hs[hidx[(1, 1)]], 1).coeff(hs[hidx[(2, 2)]], 1)
        B = x12 / 2
        # here q = Ad' sum hii^2 + ... ; (tr)^2 = sum hii^2 + 2 sum_{i<j} hii hjj  => Ad_true = Ad - B
        Ad_true = Ad - B
        return sp.simplify(Ad_true), sp.simplify(Ao), sp.simplify(B), sp.simplify(q)

    def static(Q):
        return sp.expand(Q.subs({ks[0]: 0}))

    def readoff(Q, label):
        Ad, Ao, B, q = kinetic(Q)
        Qs = static(Q)
        # h00 terms
        c00 = sp.expand(Qs).coeff(hs[0], 2)
        lin00 = sp.expand(Qs).coeff(hs[0], 1).subs(hs[0], 0)  # linear in h00, remaining polynomial
        # compare lin00 with kappa_m*(k_i k_j h_ij - k^2 h_ii)
        k2 = ks[1]**2 + ks[2]**2 + ks[3]**2
        hij = h[1:, 1:]
        kk = sp.Matrix(ks[1:])
        R1 = sp.expand((kk.T * hij * kk)[0, 0] - k2 * hij.trace())
        # h00-linear coefficient (drop h0i pieces, they vanish by time reversal in static)
        lin00_ij = sp.expand(lin00.subs({hs[hidx[(0, n)]]: 0 for n in range(1, 4)}))
        kappa_m = sp.simplify(lin00_ij.coeff(hs[hidx[(1, 1)]], 1).coeff(ks[1], 2) / 1) if False else None
        # solve for kappa_m by comparing one coefficient: h11 * k1^2 in R1 is (1 - 1)=0 ; use h11*k2^2 -> -1
        cm = sp.expand(lin00_ij).coeff(hs[hidx[(1, 1)]], 1).coeff(ks[2], 2)
        kappa_m = sp.simplify(-cm)
        chk = sp.simplify(sp.expand(lin00_ij - kappa_m * R1))
        # pure spatial part: h_ij only
        pure = sp.expand(Qs.subs({hs[0]: 0}).subs({hs[hidx[(0, n)]]: 0 for n in range(1, 4)}))
        FP3 = sp.expand(R(1, 2) * k2 * sum(hij[i, j]**2 for i in range(3) for j in range(3))
                        - sum(sum(hij[i, j] * kk[j] for j in range(3))**2 for i in range(3))
                        + (kk.T * hij * kk)[0, 0] * hij.trace() - R(1, 2) * k2 * hij.trace()**2)
        # kappa_s from coefficient of h12^2 * k3^2 : FP3 has (1/2*2 - 0)... compute ratio by matching
        cpure = sp.expand(pure).coeff(hs[hidx[(1, 2)]], 2).coeff(ks[3], 2)
        cfp = sp.expand(FP3).coeff(hs[hidx[(1, 2)]], 2).coeff(ks[3], 2)
        kappa_s = sp.simplify(cpure / cfp)
        chk2 = sp.simplify(sp.expand(pure - kappa_s * FP3))
        # TT mode h12 with momentum along axis 3: Q = (T k0^2 + S k3^2) h12^2
        sub = {v: 0 for v in hs}; sub[hs[hidx[(1, 2)]]] = 1
        sub.update({ks[1]: 0, ks[2]: 0})
        qtt = sp.expand(Q.subs(sub))
        T = qtt.coeff(ks[0], 2).coeff(ks[3], 0)
        S = qtt.coeff(ks[3], 2).coeff(ks[0], 0)
        speed2 = sp.simplify(S / T) if T != 0 else sp.oo
        # isotropic sector: h00 = 2u, hij = 2 lam delta
        u, lam = sp.symbols('u lam')
        sub = {hs[hidx[(0, 0)]]: 2 * u}
        sub.update({hs[hidx[(i, i)]]: 2 * lam for i in (1, 2, 3)})
        sub.update({hs[hidx[(0, n)]]: 0 for n in (1, 2, 3)})
        sub.update({hs[hidx[(1, 2)]]: 0, hs[hidx[(1, 3)]]: 0, hs[hidx[(2, 3)]]: 0})
        qs_iso = sp.expand(Qs.subs(sub).subs({ks[2]: 0, ks[3]: 0}))   # momentum along axis 1
        kk1 = ks[1]**2
        T0 = qs_iso.coeff(u, 2).coeff(lam, 0) / kk1
        T1 = qs_iso.coeff(u, 1).coeff(lam, 1) / kk1
        T2 = qs_iso.coeff(lam, 2).coeff(u, 0) / kk1
        beta_b60 = sp.simplify(T1 / (2 * T2)) if T2 != 0 else sp.oo
        # isotropic kinetic coefficient c_k = 12 alpha + 36 beta_kin
        ck = sp.simplify(12 * Ad + 36 * B)
        out = dict(label=label, A_diag=Ad, A_off=Ao, B_kin=B, c00=c00,
                   kappa_m=kappa_m, lin00_resid=chk, kappa_s=kappa_s, pure_resid=chk2,
                   TT_time=T, TT_space=S, TT_speed2=speed2,
                   iso_T0=T0, iso_T1=T1, iso_T2=T2, beta_b60=beta_b60, c_k=ck)
        return out

    # ---------- family ----------
    a, b = sp.symbols('a b')
    # pick a basis of the G-invariant family (two elements) and read off
    v0, v1 = fam
    Qfam = a * v0 + b * v1
    r = readoff(Qfam, 'S3T+G family a*v0+b*v1')
    print('\n== read-off, S3T+G family ==')
    for kx, vx in r.items():
        print(' ', kx, '=', vx)
    res['family'] = {k: str(v) for k, v in r.items()}

    rB = readoff(famB[0], 'B4+G (hypercubic) member')
    print('\n== read-off, B4+G member ==')
    for kx, vx in rB.items():
        print(' ', kx, '=', vx)
    res['B4member'] = {k: str(v) for k, v in rB.items()}

    # ---------- ratios (P2,P3,P4,P5) ----------
    ratio_m_over_A = sp.simplify(r['kappa_m'] / r['A_diag'])
    ratio_m_over_A_B4 = sp.simplify(rB['kappa_m'] / rB['A_diag'])
    print('\nkappa_m / alpha  (family)     =', ratio_m_over_A)
    print('kappa_m / alpha  (B4 member)  =', ratio_m_over_A_B4)
    s_ratio = sp.simplify(r['kappa_m'] / r['kappa_s'])
    s_ratio_B4 = sp.simplify(rB['kappa_m'] / rB['kappa_s'])
    print('kappa_m/kappa_s  (family)     =', s_ratio, '   B4 member:', s_ratio_B4)
    print('TT speed^2       (family)     =', r['TT_speed2'], '  B4 member:', rB['TT_speed2'])
    print('b60 exponent T1/(2T2) (family)=', r['beta_b60'], '  B4 member:', rB['beta_b60'])
    print('c_k = 12alpha+36beta (family) =', r['c_k'], ' alpha=', r['A_diag'], ' B_kin=', r['B_kin'])
    # normalise: s = (kappa_m/kappa_s)/(same for GR)
    s_norm = sp.simplify(s_ratio / s_ratio_B4)
    print('s = (km/ks)/(km/ks)_GR        =', s_norm)
    print('1/TT_speed2 (normalised)      =', sp.simplify(1 / (r['TT_speed2'] / rB['TT_speed2'])))
    print('beta_b60 / beta_b60(GR)       =', sp.simplify(r['beta_b60'] / rB['beta_b60']))
    res['ratios'] = dict(km_over_alpha_family=str(ratio_m_over_A),
                         km_over_alpha_B4=str(ratio_m_over_A_B4),
                         s_norm=str(s_norm))

    # ---------- static solve: gamma_PPN ----------
    print('\n== static solution with a rest-mass source T^00 = rho (gamma_PPN) ==')
    def gamma_static(Q, kdir=(0, 0, 1)):
        """solve the static equations with rest-mass source T^00=rho; return (h00, h_perp, h_perp2, h_offdiag, gamma)
        h_perp = h_ij e.e for e perpendicular to k (gauge-invariant scalar part psi)."""
        Qs = static(Q)
        kk = sp.Matrix(kdir)
        subk = {ks[1]: kk[0], ks[2]: kk[1], ks[3]: kk[2], ks[0]: 0}
        Qk = sp.expand(Qs.subs(subk))
        Hs = sp.Matrix(10, 10, lambda i, j: sp.diff(Qk, hs[i], hs[j]))
        J = sp.zeros(10, 1); J[0] = 1
        sol, params = Hs.gauss_jordan_solve(J)
        sol = sol.subs({p: 0 for p in params})
        hmat = sp.Matrix(4, 4, lambda m, n: sol[hidx[(min(m, n), max(m, n))]])
        hij = hmat[1:, 1:]
        # two perpendicular vectors to kk
        cand = [sp.Matrix(v) for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
        e1 = None
        for c in cand:
            w = c - (c.dot(kk) / kk.dot(kk)) * kk
            if w.norm() != 0:
                e1 = w; break
        e2 = kk.cross(e1)
        h_e1 = sp.simplify((e1.T * hij * e1)[0, 0] / e1.dot(e1))
        h_e2 = sp.simplify((e2.T * hij * e2)[0, 0] / e2.dot(e2))
        h_12 = sp.simplify((e1.T * hij * e2)[0, 0])
        h00 = sp.simplify(sol[0])
        gam = sp.simplify(-h_e1 / h00)
        return h00, h_e1, h_e2, h_12, gam

    for label, Q in (('family', Qfam), ('B4 member', famB[0])):
        probes = [(1, 1), (1, -1), (1, 2), (2, -1), (3, 5), (1, -8), (5, -2)] if label == 'family' else [(None, None)]
        for (pa, pb) in probes:
            try:
                subv = {a: pa, b: pb} if label == 'family' else None
                Qp = Q.subs(subv) if subv else Q
                rr = readoff(Qp, 'probe')
                km_ks = sp.simplify(rr['kappa_m'] / rr['kappa_s'])
                gs = []
                for kdir in ((0, 0, 1), (1, 1, 1), (1, 2, 0), (2, 1, 3)):
                    h00, h1, h2, h12, gam = gamma_static(Qp, kdir)
                    gs.append(gam)
                    assert sp.simplify(h1 - h2) == 0 and sp.simplify(h12) == 0, ('non-isotropic static solution', kdir, h1, h2, h12)
                print(f'  {label} (a,b)=({pa},{pb}): gamma over 4 k-directions = {gs}; km/ks={km_ks}, '
                      f'1/TTspeed2={sp.simplify(1/rr["TT_speed2"])}, b60beta={rr["beta_b60"]}, '
                      f'alpha={rr["A_diag"]}, km/alpha={sp.simplify(rr["kappa_m"]/rr["A_diag"])}, c_k/alpha={sp.simplify(rr["c_k"]/rr["A_diag"])}')
                ok = all(sp.simplify(g - km_ks * (1 if label == 'family' else 1)) == 0 for g in gs)
                res.setdefault('static', []).append(dict(label=label, a=pa, b=pb, gammas=[str(g) for g in gs], km_ks=str(km_ks), gamma_equals_km_over_ks=bool(ok)))
            except Exception as ex:
                print('  static solve failed for', label, pa, pb, repr(ex))

    # ---------- intersection with the campaign's rate-linear ledger: K_m = K_s ----------
    print('\n== rate-linear ledger (b60: one density, K_m = K_s) inside the G-family ==')
    sol_b = sp.solve(sp.Eq(r['kappa_m'], r['kappa_s']), b)
    print('kappa_m = kappa_s  =>  b =', sol_b)
    Qtie = sp.expand(Qfam.subs(b, sol_b[0]))
    Bm = sp.expand(famB[0])
    ratio = sp.simplify(Qtie / Bm)
    print('family member with K_m=K_s divided by the B4 (hypercubic) member =', ratio, '(pure number => same form)')
    rt = readoff(Qtie, 'K_m=K_s member')
    print('TT speed^2 =', rt['TT_speed2'], '; b60 beta =', rt['beta_b60'], '; kappa_m/alpha =', sp.simplify(rt['kappa_m']/rt['A_diag']))
    res['tie'] = dict(b=str(sol_b[0]), ratio_to_B4=str(ratio), TT_speed2=str(rt['TT_speed2']), b60_beta=str(rt['beta_b60']))
    # b101-type member: K_m = K_s = K, kinetic alpha free (NOT in the family unless alpha = K/2 in this normalisation)
    print('In this normalisation kappa_m = 2*alpha in every G-invariant member, so a member with K_m=K_s=K and'
          ' alpha != K/2 is not G-invariant (it is the c_g-deformed algebra of b112, structure function K/(4 alpha)).')


    # ---------- extra check: lapse enters linearly (no h00^2 at all, any k) ----------
    print('\n== lapse linearity: coefficient of h00^2 in the FULL family (all k) ==')
    c00_full = sp.expand(Qfam).coeff(hs[0], 2)
    print('coeff of h00^2 =', sp.simplify(c00_full), '(0 => no u^2, no (grad u)^2, no udot^2 term: the lapse is a Lagrange multiplier)')
    res['c00_full'] = str(sp.simplify(c00_full))

    json.dump(res, open('t68_results.json', 'w'), indent=1, default=str)

if __name__ == '__main__':
    main()
