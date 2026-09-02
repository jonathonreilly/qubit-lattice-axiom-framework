#!/usr/bin/env python3
"""Lueders on the one-site record cell under the grading; permanence is occupation conservation.

Class-A finite-dimensional runner for the record-cell repair: under the declared
grading hypothesis the outcome operations on a recorded site are parity-even CP
maps, and then the effect of a rank-one locked output is forced to be that output
itself -- the Lueders form -- while the permanence obstruction on the generator
weakens from `H in 1 (x) B(K)` to conservation of the recorded occupation.

Declared objects (all exact; sympy only, no floats, no sampling):

  * the Pauli matrices s1, s2, s3, the unit one = eye(2), the matrix units
    E00, E01 = |0><1|, E10, E11 of M_2(C), the occupation n = E11, and the site
    lowering operator c = E01 with c^dagger c = n and s3 = 1 - 2n;
  * the parity grading Ad(s3) of the site algebra: even = span{E00, E11},
    odd = span{E01, E10};
  * outcome operations in Kraus form J(rho) = sum_j K_j rho K_j^dagger with range
    in a locked output P, effect E_P = sum_j K_j^dagger K_j, and an instrument as
    a family of such maps whose effects sum to the unit;
  * the enlarged cell C^2 (x) K with K = C^2 and K = C^3, total parity s3 (x) s3
    on the two-mode cell, and the Jordan-Wigner pair c_x = c (x) one,
    c_y = s3 (x) c with n_x = n (x) one, n_y = one (x) n.

Check groups:

  A  Lueders on the one-site cell: the rank-one normal form K = |p><v| with
     E = |v><v|, the evenness constraint v0 = 0 forcing K = c n and
     E_P = lambda P, completeness forcing lambda = 1 at both even outputs, an odd
     instrument with E_P = 1 - P showing the evenness is load-bearing, and the
     caveat that on the two-mode cell the even Kraus operators leave a
     two-dimensional sector of effects free for one and the same output;
  B  permanence is occupation conservation: the Hermitian commutant of n (x) 1
     for dim K = 2 and dim K = 3 against the commutant of M_2(C) (x) 1, hopping
     excluded while phase, density-density and record-conditioned action on K
     survive, and the failure of the spanning condition on the even sector.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

import sys

import sympy as sp
from sympy import I, Matrix, eye, zeros, symbols

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one exact check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ---------------------------------------------------------------- notation

s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
one = eye(2)

E00 = Matrix([[1, 0], [0, 0]])
E01 = Matrix([[0, 1], [0, 0]])
E10 = Matrix([[0, 0], [1, 0]])
E11 = Matrix([[0, 0], [0, 1]])
UNITS = [E00, E01, E10, E11]
n = E11
cop = E01

ket0 = Matrix([1, 0])
ket1 = Matrix([0, 1])

I4 = eye(4)
Z2 = zeros(2, 2)
Z4 = zeros(4, 4)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return Matrix(out)


def zero(M):
    return all(sp.expand(e) == 0 for e in M)


def eq(A, B):
    return zero(A - B)


def rows_of(mats):
    return Matrix([[e for e in M] for M in mats])


def rvec(M):
    out = []
    for e in M:
        re_, im_ = sp.expand(e).as_real_imag()
        out.append(sp.expand(re_))
        out.append(sp.expand(im_))
    return out


def rrank(mats):
    return Matrix([rvec(M) for M in mats]).rank()


def real_eqs(M):
    out = []
    for e in M:
        re_, im_ = sp.expand(e).as_real_imag()
        for q in (sp.expand(re_), sp.expand(im_)):
            if q != 0:
                out.append(q)
    return out


def cmat(name, r, c):
    """A symbolic complex r x c matrix in independent real parameters."""
    re_ = symbols("%sr0:%d" % (name, r * c), real=True)
    im_ = symbols("%si0:%d" % (name, r * c), real=True)
    M = Matrix(r, c, lambda i, j: re_[i * c + j] + I * im_[i * c + j])
    return M, list(re_) + list(im_)


def herm(name, dim):
    """A symbolic Hermitian dim x dim matrix in real parameters."""
    d = symbols(name + "_d0:%d" % dim, real=True)
    x = {}
    y = {}
    for i in range(dim):
        for j in range(i + 1, dim):
            x[(i, j)] = sp.Symbol("%s_x%d%d" % (name, i, j), real=True)
            y[(i, j)] = sp.Symbol("%s_y%d%d" % (name, i, j), real=True)
    M = zeros(dim, dim)
    for i in range(dim):
        M[i, i] = d[i]
        for j in range(i + 1, dim):
            M[i, j] = x[(i, j)] + I * y[(i, j)]
            M[j, i] = x[(i, j)] - I * y[(i, j)]
    return M, list(d) + [x[k] for k in sorted(x)] + [y[k] for k in sorted(y)]


def herm_basis(d):
    """The d^2 Hermitian matrix units of M_d(C), a real basis of Herm(d)."""
    B = []
    for i in range(d):
        M = zeros(d, d)
        M[i, i] = 1
        B.append(M)
    for i in range(d):
        for j in range(i + 1, d):
            M = zeros(d, d)
            M[i, j] = 1
            M[j, i] = 1
            B.append(M)
            M = zeros(d, d)
            M[i, j] = I
            M[j, i] = -I
            B.append(M)
    return B


def freesyms(M):
    return sorted(M.free_symbols, key=sp.default_sort_key)


def real_dim(M, fv):
    """Real dimension of the linear family M(fv), by rank of its basis."""
    B = [M.subs({t: (1 if t == x else 0) for t in fv}) for x in fv]
    return rrank(B), B


def scalar(name):
    return sp.Symbol(name + "r", real=True) + I * sp.Symbol(name + "i", real=True)


def absq(z):
    return sp.expand(sp.re(z) ** 2 + sp.im(z) ** 2)


# ============================== A: Lueders on the one-site record cell

# --- A1a: the parent's rank-one normal form, re-derived here

Kg, Kp = cmat("k", 2, 2)
Pn = n
a1a_sol = sp.solve(real_eqs(Pn * Kg - Kg), Kp, dict=True)
Kr = Kg.subs(a1a_sol[0])
vbra = Matrix([[Kr[1, 0], Kr[1, 1]]])
Er = sp.expand(Kr.H * Kr)
rho, _rp = herm("rho", 2)
check("A1a rank-one locked output P = |1><1|: range(K) in P forces K = |1><v| with "
      "<v| = (K10, K11), four free real parameters, E = K^dag K = |v><v|, and "
      "K rho K^dag = Tr(E rho) P for every symbolic Hermitian rho",
      len(a1a_sol) == 1
      and len(freesyms(Kr)) == 4
      and eq(Pn, ket1 * ket1.H)
      and zero(Kr[0, :])
      and eq(Kr, ket1 * vbra)
      and eq(Er, vbra.H * vbra)
      and eq(sp.expand(Kr * rho * Kr.H), sp.expand((Er * rho).trace() * Pn)))

# --- A1b: evenness kills v0, so every even Kraus operator with range in n is c n

a1b_sol = sp.solve(real_eqs(Pn * Kg - Kg) + real_eqs(s3 * Kg * s3 - Kg), Kp, dict=True)
Ke = Kg.subs(a1b_sol[0])
ce = Ke[1, 1]
cs = [scalar("c%d_" % j) for j in range(3)]
Emulti = sp.expand(sum(((cj * n).H * (cj * n) for cj in cs), Z2))
lam_multi = sp.expand(sum(absq(cj) for cj in cs))
check("A1b evenness s3 K s3 = K on top of range(K) in P forces v0 = 0, i.e. K = c n with "
      "two free real parameters; for any family K_j = c_j n the effect is "
      "E_P = (sum_j |c_j|^2) n = lambda P with lambda a sum of squares, so lambda >= 0",
      len(a1b_sol) == 1
      and len(freesyms(Ke)) == 2
      and sp.expand(Ke[1, 0]) == 0
      and eq(Ke, ce * n)
      and eq(sp.expand(Ke.H * Ke), absq(ce) * n)
      and sp.expand(absq(ce) - (sp.re(ce) ** 2 + sp.im(ce) ** 2)) == 0
      and eq(Emulti, lam_multi * n)
      and sp.expand(lam_multi - sum(sp.re(cj) ** 2 + sp.im(cj) ** 2 for cj in cs)) == 0)

# --- A2: completeness over the two even outputs forces the Lueders form

lam1, lam0 = symbols("lam1 lam0", real=True)
P1, P0 = n, one - n
a2_sol = sp.solve(real_eqs(lam1 * P1 + lam0 * P0 - one), [lam1, lam0], dict=True)
a2 = len(a2_sol) == 1 and a2_sol[0] == {lam1: 1, lam0: 1}
if a2:
    a2 = (eq((lam1 * P1).subs(a2_sol[0]), P1)
          and eq((lam0 * P0).subs(a2_sol[0]), P0)
          and eq(P1 + P0, one)
          and eq(P1 * P0, Z2))
check("A2 exhaustive even instrument on the one-site cell, outputs P_1 = n and P_0 = 1-n: "
      "the effects are lambda_1 n and lambda_0 (1-n) by A1b and A3a, and the completeness "
      "equation has the unique solution lambda_1 = lambda_0 = 1, so E_P = P at both outputs",
      a2)

# --- A3a: the same at the even output 1 - n

a3a_sol = sp.solve(real_eqs(P0 * Kg - Kg) + real_eqs(s3 * Kg * s3 - Kg), Kp, dict=True)
Ke0 = Kg.subs(a3a_sol[0])
ce0 = Ke0[0, 0]
check("A3a the even output P = 1-n by the same route: range(K) in P with s3 K s3 = K forces "
      "v1 = 0 and K = c (1-n), two free real parameters, E_P = |c|^2 (1-n) = lambda P",
      len(a3a_sol) == 1
      and len(freesyms(Ke0)) == 2
      and sp.expand(Ke0[0, 1]) == 0
      and eq(Ke0, ce0 * (one - n))
      and eq(sp.expand(Ke0.H * Ke0), absq(ce0) * (one - n)))

# --- A3b: an odd instrument on the same two outputs has E_P = 1 - P

Kf1 = E10
Kf0 = E01
Ef1 = sp.expand(Kf1.H * Kf1)
Ef0 = sp.expand(Kf0.H * Kf0)
check("A3b the evenness is load-bearing: the odd instrument K_1 = |1><0| = c^dag, "
      "K_0 = |0><1| = c has ranges in P_1 = n and P_0 = 1-n and effects summing to 1, but "
      "s3 K s3 = -K and E_{P_1} = 1-n, E_{P_0} = n, i.e. E_P = 1-P at both outputs",
      eq(Pn * Kf1, Kf1) and eq((one - n) * Kf0, Kf0)
      and eq(s3 * Kf1 * s3, -Kf1) and eq(s3 * Kf0 * s3, -Kf0)
      and eq(Ef1 + Ef0, one)
      and eq(Ef1, one - n) and eq(Ef0, n)
      and not eq(Ef1, P1) and not eq(Ef0, P0)
      and eq(Ef1, one - P1) and eq(Ef0, one - P0))

# --- A4a: on the two-mode cell the even Kraus operators leave a 2-dim sector free


def unit4(i, j):
    M = Z4.copy()
    M[i, j] = 1
    return M


Ptot = kron(s3, s3)
P11 = unit4(3, 3)
ket11 = Matrix([0, 0, 0, 1])
Qg, Qp = cmat("q", 4, 4)
a4_sol = sp.solve(real_eqs(P11 * Qg - Qg) + real_eqs(Ptot * Qg * Ptot - Qg), Qp, dict=True)
Q4 = Qg.subs(a4_sol[0])
E4 = sp.expand(Q4.H * Q4)
SEC = [0, 3]
Pplus = sp.expand((I4 + Ptot) / 2)
BRAS = [Matrix([[1, 0, 0, 0]]), Matrix([[0, 0, 0, 1]]),
        Matrix([[1, 0, 0, 1]]), Matrix([[1, 0, 0, I]])]
EFFS = [sp.expand((ket11 * b).H * (ket11 * b)) for b in BRAS]
check("A4a two-mode cell C^2 (x) K, K = C^2, output P = |1><1| (x) |1><1|: even Kraus "
      "operators with range in P are |11><v| with <v| in the +1 parity sector span{|00>,|11>} "
      "of dimension 2, so E_P is supported there and ranges over all of Herm of that sector, "
      "real dimension 4 -- exhibited by four such effects of real rank 4",
      len(a4_sol) == 1
      and len(freesyms(Q4)) == 4
      and eq(Q4, ket11 * Matrix([[Q4[3, 0], 0, 0, Q4[3, 3]]]))
      and all(sp.expand(E4[i, j]) == 0
              for i in range(4) for j in range(4)
              if i not in SEC or j not in SEC)
      and Pplus.rank() == 2
      and eq(Pplus * ket11, ket11)
      and all(eq(Ptot * K * Ptot, K) and eq(P11 * K, K)
              for K in [ket11 * b for b in BRAS])
      and rrank(EFFS) == 4)

# --- A4b: two even instruments, one output, two different effects

INST_I = [[unit4(3, 3)], [unit4(0, 0), unit4(1, 1), unit4(2, 2)]]
INST_II = [[unit4(3, 0)], [unit4(1, 1), unit4(2, 2), unit4(3, 3)]]


def effect(ks):
    return sp.expand(sum((K.H * K for K in ks), Z4))


def complete(inst):
    return eq(sp.expand(sum((effect(ks) for ks in inst), Z4)), I4)


EI = effect(INST_I[0])
EII = effect(INST_II[0])
check("A4b Lueders is not forced once the cell is larger than one site: two even instruments "
      "on C^2 (x) K, both with the outcome output P = |11><11| and both complete, carry the "
      "different effects E_P = P and E_P = |00><00| for that one output",
      all(eq(Ptot * K * Ptot, K) for inst in (INST_I, INST_II) for ks in inst for K in ks)
      and eq(P11 * INST_I[0][0], INST_I[0][0])
      and eq(P11 * INST_II[0][0], INST_II[0][0])
      and complete(INST_I) and complete(INST_II)
      and eq(EI, P11) and eq(EII, unit4(0, 0))
      and not eq(EI, EII) and not eq(EII, P11))

# ============================ B: permanence is occupation conservation


def commutant_report(d):
    """Hermitian commutant of n (x) 1 on C^2 (x) C^d, against 1 (x) B(K)."""
    Hs, hp = herm("h%d" % d, 2 * d)
    N = kron(n, eye(d))
    sol = sp.solve(real_eqs(Hs * N - N * Hs), hp, dict=True)
    Hev = Hs.subs(sol[0])
    fv = freesyms(Hev)
    dcom, _ = real_dim(Hev, fv)
    HB = herm_basis(d)
    inner = [kron(one, A) for A in HB]
    dinn = rrank(inner)
    extra = kron(n, eye(d))
    ok = (len(sol) == 1
          and len(fv) == dcom
          and all(sp.expand(Hev[i, j]) == 0
                  for i in range(2 * d) for j in range(2 * d)
                  if (i < d) != (j < d))
          and eq(Hev, kron(one - n, Hev[0:d, 0:d]) + kron(n, Hev[d:2 * d, d:2 * d]))
          and all(zero(M * N - N * M) for M in inner)
          and zero(extra * N - N * extra)
          and rrank(inner + [extra]) == dinn + 1)
    return dcom, dinn, ok


d2com, d2inn, b1a_ok = commutant_report(2)
check("B1a permanence for a recorded site, dim K = 2: the Hermitian solutions of "
      "[H, n (x) 1] = 0 are exactly (1-n) (x) B(K) (+) n (x) B(K), of real dimension %d = "
      "2 dim(K)^2, strictly containing 1 (x) B(K) of real dimension %d = dim(K)^2 "
      "(n (x) 1 commutes and is outside)" % (d2com, d2inn),
      b1a_ok and d2com == 8 and d2inn == 4 and d2com > d2inn)

d3com, d3inn, b1b_ok = commutant_report(3)
check("B1b the same for dim K = 3: real dimension %d = 2 dim(K)^2 against %d = dim(K)^2 for "
      "1 (x) B(K); the block-diagonal form and the strict containment are unchanged"
      % (d3com, d3inn),
      b1b_ok and d3com == 18 and d3inn == 9 and d3com > d3inn)

Gs, Gp = herm("g", 4)
b1c_sol = sp.solve(real_eqs(Gs * kron(s1, one) - kron(s1, one) * Gs)
                   + real_eqs(Gs * kron(s3, one) - kron(s3, one) * Gs), Gp, dict=True)
Gev = Gs.subs(b1c_sol[0])
Gfv = freesyms(Gev)
gdim, _ = real_dim(Gev, Gfv)
check("B1c the parent's obstruction under the parent's own condition: if the recordable "
      "rank-one frames spanned M_2(C), permanence would read [H, X (x) 1] = 0 for all X, "
      "whose Hermitian solutions are exactly 1 (x) B(K), real dimension %d" % gdim,
      len(b1c_sol) == 1
      and gdim == 4 and len(Gfv) == 4
      and eq(Gev, kron(one, Gev[0:2, 0:2]))
      and rows_of([one, s1, s2, s3]).rank() == 4
      and rows_of([one, s1, s3, sp.expand(s1 * s3)]).rank() == 4)

# --- B2a: hops are excluded although the hopping is parity-even

cx = kron(cop, one)
cy = kron(s3, cop)
nx = kron(n, one)
ny = kron(one, n)
hop = sp.expand(cx.H * cy + cy.H * cx)
check("B2a Jordan-Wigner two-mode cell, c_x = c (x) one, c_y = s3 (x) c: the pair anticommutes, "
      "n_x = c_x^dag c_x and n_y = c_y^dag c_y, and the hopping c_x^dag c_y + h.c. is Hermitian "
      "and parity-even yet fails to commute with n_x, while n_y and n_x n_y commute with n_x",
      eq(cx.H * cx, nx) and eq(cy.H * cy, ny)
      and zero(cx * cy + cy * cx) and zero(cx * cy.H + cy.H * cx)
      and eq(cx * cx.H + cx.H * cx, I4)
      and eq(hop.H, hop)
      and eq(Ptot * hop * Ptot, hop)
      and not zero(hop * nx - nx * hop)
      and zero(ny * nx - nx * ny)
      and zero((nx * ny) * nx - nx * (nx * ny))
      and eq(nx * nx, nx) and eq(ny * ny, ny))

# --- B2b: phase, density-density and record-conditioned action on K all survive

Ah, _ap = herm("a", 2)
cond = kron(n, Ah)
dens = sp.expand(nx * ny)
check("B2b what an admissible H may still do: the phase term n_x, the density-density term "
      "n_x n_y and the record-conditioned action n (x) A for symbolic Hermitian A all commute "
      "with n_x, n_x being a projector, and n (x) s1 lies outside 1 (x) B(K), so the surviving "
      "freedom is strictly larger than an action on K alone",
      eq(nx * nx, nx)
      and zero(dens * nx - nx * dens)
      and zero(cond * nx - nx * cond)
      and eq(cond.H, cond)
      and eq(dens.H, dens)
      and rrank([kron(one, A) for A in herm_basis(2)] + [kron(n, s1)]) == 5)

# --- B3: the parent's spanning condition fails on the even sector

FRAMES = [n, one - n]
check("B3 the parent's spanning condition is false under the hypothesis: the recordable "
      "rank-one frames are n and 1-n, of rank 2, spanning the 2-dimensional even algebra "
      "span{1, n} and not M_2(C) of rank 4; adjoining the odd unit E01 raises the rank to 3, "
      "so the two-frame non-spanning case is the case the hypothesis delivers",
      rows_of(FRAMES).rank() == 2
      and rows_of(FRAMES + [one]).rank() == 2
      and rows_of(UNITS).rank() == 4
      and rows_of(FRAMES + [E01]).rank() == 3
      and eq(s3 * n * s3, n) and eq(s3 * (one - n) * s3, one - n)
      and eq(s3 * E01 * s3, -E01) and eq(s3 * E10 * s3, -E10)
      and all(M.rank() == 1 and eq(M * M, M) and eq(M.H, M) for M in FRAMES))

print("SUMMARY: on the one-site record cell parity-even outcome operations force the Lueders "
      "form E_P = P; on a two-mode cell they do not, a two-dimensional sector of effects "
      "remaining; and permanence for a recorded site is conservation of its occupation, a "
      "commutant of real dimension 2 dim(K)^2 rather than dim(K)^2.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
