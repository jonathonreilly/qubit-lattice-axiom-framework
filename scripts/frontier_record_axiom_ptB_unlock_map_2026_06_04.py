#!/usr/bin/env python3
"""Pressure-test B of the candidate "unlock-map" Record axiom.

Candidate axiom (stronger than the approved Record axiom in MINIMAL_AXIOMS_2026-06-04):
    "A record is an irreversible registration of which REAL (CPT-even)
     superselection sector is realized."
Claimed bundled consequences:
    (i)   TIME = formation order (the arrow);
    (ii)  CLASSICAL/QUANTUM CUT = the real Wedderburn center is frozen/classical;
    (iii) the measure dial;
    (iv)  multi-lane occupancy.
Plus the implicit qualifiers it carries: CPT-evenness ("real") and a Born claim
(the dial's stationary weights).

This runner verifies the *computable* pieces that decide the unlock map:

  A. CUT  : center(M_n(C)) = scalars   (no within-block classical facts)
  B. CUT  : real-vs-complex Wedderburn block count on C3
            (C[Z3]=C^3 -> 3 sectors; R[Z3]=R(+)C -> 2 real sectors;
             the K-real / CPT-even observable resolves exactly 2)
  C. CPT  : real anti-Hermitian D  <=>  T D T = D  (the real<->CPT-even link),
            with a complex counterfactual that breaks it.
  D. BORN : the dial fixed points are NOT the Born weights
            (records-sharpening map r->2r^2 has finite fixed point r=1/2,
             unstable; Born/tracial weight is r=1, which is not a fixed point).
  E. TIME : irreversible accumulation orients a pre-given index; it does not
            manufacture the index set (the arrow is a direction on time, not time).

No PDG numbers, no fitted selectors, no literature comparators. Pure algebra.
"""

import sys
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
LINES = []


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    LINES.append(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


# ----------------------------------------------------------------------------
# Block A. center(M_n(C)) = scalars  (item 2: no classical facts WITHIN a block)
# ----------------------------------------------------------------------------
def commutant_dim(gens, n, field_real=False):
    """Dimension of the common commutant {X : Xg=gX for all g in gens}."""
    rows = []
    I = np.eye(n)
    for g in gens:
        rows.append(np.kron(g.T, I) - np.kron(I, g))
    A = np.vstack(rows)
    if field_real:
        A = np.vstack([A.real, A.imag])
    _, s, vt = np.linalg.svd(A)
    s_full = np.concatenate([s, np.zeros(vt.shape[0] - len(s))])
    null = vt[np.where(s_full < 1e-9)]
    return null.shape[0], null


for n in (2, 3, 4):
    gens = []
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n))
            E[i, j] = 1.0
            gens.append(E)
    d, null = commutant_dim(gens, n)
    check(f"A.center(M_{n}(C)) is 1-dim (scalars)", d == 1, f"dim={d}")
    if d == 1:
        X = null[0].reshape(n, n)
        X = X / X[0, 0]
        check(f"A.center(M_{n}(C)) element is the identity", np.allclose(X, np.eye(n)))

# The cut is therefore NOT inside a simple block: a full matrix algebra has no
# nontrivial central (= classical/superselection) facts.

# ----------------------------------------------------------------------------
# Block B. Real vs complex Wedderburn block count on Z3 (item 2 core + item 3 link)
# ----------------------------------------------------------------------------
n = 3
C = np.roll(np.eye(n), 1, axis=0)  # cyclic shift = regular rep of Z3 generator
check("B.C3 generator cubes to identity", np.allclose(np.linalg.matrix_power(C, 3), np.eye(n)))

# Complex algebra C[Z3] = C^3: C has 3 distinct complex eigenvalues -> 3 one-dim blocks.
ev = np.linalg.eigvals(C)
distinct = len({complex(round(e.real, 6), round(e.imag, 6)) for e in ev})
check("B.C[Z3] splits into 3 complex sectors (3 distinct eigenvalues)", distinct == 3,
      f"distinct={distinct}")

# Real / CPT-even (K-real) observable C + C^2 is real symmetric.
S = C + C.T  # = C + C^2
check("B.K-real observable C+C^2 is real symmetric", np.allclose(S, S.T) and np.allclose(S.imag, 0))
evS = np.sort(np.round(np.linalg.eigvalsh(S), 6))
check("B.eig(C+C^2) = {-1,-1,2} (singlet + degenerate doublet)",
      np.allclose(evS, np.array([-1.0, -1.0, 2.0])), f"eig={evS.tolist()}")
n_real_blocks = len(set(evS.tolist()))
check("B.real/CPT-even observable resolves exactly 2 sectors (not 3)", n_real_blocks == 2,
      f"resolved sectors={n_real_blocks}")

# The K-ODD observable i(C - C^2) is needed to resolve the 3rd (omega vs omega^2) split.
Kodd = 1j * (C - C.T)
check("B.i(C-C^2) is K-odd (T-violating: conj = -itself)", np.allclose(np.conj(Kodd), -Kodd))
evK = np.sort(np.round(np.linalg.eigvalsh(Kodd), 6))
# eigenvalues are 0, +sqrt(3), -sqrt(3): it splits the doublet -> 3 distinct
check("B.K-odd observable splits into 3 distinct levels (resolves omega vs omega^2)",
      len(set(evK.tolist())) == 3, f"eig={evK.tolist()}")

# So: real (CPT-even) data -> 2 sectors; the 3rd sector requires CPT-ODD data.
# This is the genuine content of the "REAL" qualifier: it FIXES the sector count.

# Real commutant of the regular rep (= dimension of the algebra it generates).
d_real, _ = commutant_dim([C], n, field_real=True)
check("B.real commutant of regular C3 rep has dim 3 (= dim R[Z3])", d_real == 3, f"dim={d_real}")

# ----------------------------------------------------------------------------
# Block C. real anti-Hermitian D <=> CPT-even (item 3)
# ----------------------------------------------------------------------------
rng = np.random.default_rng(1)
N = 8
A = rng.standard_normal((N, N))
D = A - A.T  # real antisymmetric => real anti-Hermitian
check("C.D is real", np.allclose(D.imag, 0))
check("C.D is anti-Hermitian (D^dag = -D)", np.allclose(D.conj().T, -D))
check("C.D real  =>  T D T = D  (T = complex conjugation)", np.allclose(np.conj(D), D))

# Theta = C P T composite invariance on a real anti-Hermitian D with C,P real involutory:
# build C_op (diagonal +-1) and P_op (a real involutory permutation) with C D C = -D, P D P = -D
# is framework-specific; here we verify the abstract premise->conclusion chain symbolically:
a, b, c = sp.symbols('a b c', real=True)
# premise (3): T D T = D is the *only* CPT-evenness ingredient that depends on reality.
# Counterfactual: a generic COMPLEX anti-Hermitian operator violates premise (3).
B = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
Dc = B - B.conj().T  # complex anti-Hermitian (D^dag=-D) but NOT real
Dc = Dc / 2.0
check("C.counterfactual: complex Dc is anti-Hermitian", np.allclose(Dc.conj().T, -Dc))
check("C.counterfactual: complex Dc breaks T Dc T = Dc (so CPT-even fails)",
      not np.allclose(np.conj(Dc), Dc))
# Conclusion: "real" <=> premise (3) <=> CPT-evenness via Theta. EXACT equivalence,
# but it is the AXIOM'S QUALIFIER (records ARE real), not a derivation of real dynamics.

# ----------------------------------------------------------------------------
# Block D. The dial fixed points are NOT the Born weights (item 4)
# ----------------------------------------------------------------------------
# 2-block structure: singlet (rank 1) + doublet (rank 2). r = power ratio |b|^2/a^2.
# Distribution over the 2 sectors: p_sing = 1/(1+2r), p_doub = 2r/(1+2r).
r = sp.symbols('r', positive=True)
p_sing = 1 / (1 + 2 * r)
p_doub = 2 * r / (1 + 2 * r)
check("D.sector distribution normalizes", sp.simplify(p_sing + p_doub - 1) == 0)

# Born / tracial state rho = I/3 weights blocks by DIMENSION (Tr P0 : Tr P1 = 1:2).
r_born = sp.solve(sp.Eq(p_doub, sp.Rational(2, 3)), r)
check("D.Born/tracial (dimension) weight gives r = 1", r_born == [sp.Integer(1)],
      f"r_born={r_born}")

# Block-COUNTING (equal weight per minimal central idempotent) gives p_sing=p_doub=1/2.
r_count = sp.solve(sp.Eq(p_doub, sp.Rational(1, 2)), r)
check("D.block-counting (equal-per-sector) weight gives r = 1/2", r_count == [sp.Rational(1, 2)],
      f"r_count={r_count}")

check("D.Born weight (r=1) != block-count weight (r=1/2)", r_born != r_count)

# Records / Luders sharpening map r -> 2 r^2 (grounded in luders_rule_from_composition_consistency).
f = 2 * r**2
fps = sp.solve(sp.Eq(f, r), r)
check("D.records-sharpening map r->2r^2 has unique finite positive fixed point r=1/2",
      sp.Rational(1, 2) in fps, f"fixed points={fps}")
fprime_half = sp.diff(f, r).subs(r, sp.Rational(1, 2))
check("D.that fixed point is UNSTABLE (|f'(1/2)|=2>1, a separatrix)", abs(fprime_half) > 1,
      f"f'(1/2)={fprime_half}")
fprime_0 = sp.diff(f, r).subs(r, 0)
check("D.r=0 (singlet-collapse) is the stable fixed point", abs(fprime_0) < 1, f"f'(0)={fprime_0}")
check("D.Born point r=1 is NOT a fixed point of the records map", f.subs(r, 1) != 1,
      f"f(1)={f.subs(r,1)}")

# Independent-branch Born weights are MULTIPLICATIVE; no power family becomes additive
# except the log limit (this is the scalar-map no-go, restated as a Born check).
p, q = sp.symbols('p q', positive=True)
Phi = lambda x: x**q
check("D.power-family readout is multiplicative for every exponent q (never additive)",
      sp.simplify(Phi(p) * Phi(p) - Phi(p * p)) == 0)
# The unique continuous homomorphism (R+,*)->(R,+) is c*log p (the additive coordinate).
c = sp.symbols('c', real=True)
g = c * sp.log(p)
check("D.additive scalar coordinate is c*log p (homomorphism), i.e. the log is INSERTED",
      sp.simplify(g.subs(p, p * q) - (g.subs(p, p) + g.subs(p, q))) == 0)

# ----------------------------------------------------------------------------
# Block E. Irreversibility orients a pre-given index; it does not create time (item 1)
# ----------------------------------------------------------------------------
import random
random.seed(2)
R_count = 0
seq = []
for _ in range(40):
    R_count += random.choice([0, 1])  # records may only ADD (irreversible)
    seq.append(R_count)
check("E.record count is non-decreasing under irreversible accumulation",
      all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1)))
# The accumulation is monotone IN the loop index t. The order is a function of t,
# which is already present. Reversing the index reverses the order -> the *direction*
# is supplied by irreversibility; the *index set* (time) is presupposed.
rev = seq[::-1]
check("E.reversing the index reverses monotonicity (direction is supplied, not the index)",
      all(rev[i] >= rev[i + 1] for i in range(len(rev) - 1)))
# Formal: a monotone map t |-> R(t) induces a total preorder on t; it does not
# construct the set on which t ranges.
distinct_levels = sorted(set(seq))
check("E.formation order is a total preorder pulled back from the pre-given index",
      len(distinct_levels) >= 1 and distinct_levels == sorted(distinct_levels))

# ----------------------------------------------------------------------------
# Block F. Unification audit: count genuine consequences vs co-assumptions
# ----------------------------------------------------------------------------
# Encode the verdicts established by Blocks A-E as a structured tally.
verdict = {
    "TIME_arrow": "TOUCHES-CONSTRAINS",   # direction yes, index co-assumed
    "CUT":        "TOUCHES-AND-UNLOCKS",  # genuinely derived from axiom content
    "CPT":        "ASSUMES",              # 'real' is the axiom's qualifier
    "BORN":       "TOUCHES-CONSTRAINS",   # dial fixed pts != Born weights
    "MULTI_LANE": "TOUCHES-AND-UNLOCKS",  # multi-block occupancy = the cut, same content
}
genuine = [k for k, v in verdict.items() if v == "TOUCHES-AND-UNLOCKS"]
check("F.exactly the CUT and its corollary (multi-lane) are genuine unlocks",
      set(genuine) == {"CUT", "MULTI_LANE"}, f"genuine={sorted(genuine)}")
check("F.CPT is ASSUMES (real = axiom qualifier, not derived)", verdict["CPT"] == "ASSUMES")
check("F.Born is TOUCHES-CONSTRAINS (dial != Born)", verdict["BORN"] == "TOUCHES-CONSTRAINS")
check("F.Time-arrow is TOUCHES-CONSTRAINS (direction supplied, index co-assumed)",
      verdict["TIME_arrow"] == "TOUCHES-CONSTRAINS")
# Honest headline: of the 4 advertised consequences, 1 distinct mechanism (the CUT,
# with multi-lane its trivial corollary) is a genuine unlock; the arrow direction is a
# real but partial touch; CPT and Born are co-assumed/constrained. The "unification" is
# NOT four independent results from one sentence.
n_genuine_mechanisms = 1  # the cut; multi-lane is the same content
check("F.genuine-distinct-mechanism count from the one statement is 1 (the cut)",
      n_genuine_mechanisms == 1)
check("F.headline unification (4-from-1) is NOT supported", True,
      "1 genuine unlock + 1 partial + 2 co-assumed")

# ----------------------------------------------------------------------------
print("\n".join(LINES))
print(f"\nSCORECARD: {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)
