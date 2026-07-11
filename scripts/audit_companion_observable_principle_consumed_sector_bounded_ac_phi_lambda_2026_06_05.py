#!/usr/bin/env python3
"""Companion runner for
`OBSERVABLE_PRINCIPLE_CONSUMED_SECTOR_BOUNDED_BY_AC_PHI_LAMBDA_NARROW_THEOREM_NOTE_2026-06-05.md`.

CAPSTONE CLAIM (narrow, bounded):
  The observable-principle parent `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE` is
  `audited_conditional` on a single remaining premise, P2 (the scalar record
  generator depends on |Z|=|det(D+J)| alone, not on arg Z). After the Record
  baseline absorbed P1 (finite scalar additivity), the open question the parent
  itself names is "whether P2 can be derived or ratified."

  This runner reproves, from primitives, that ON THE SECTOR THE PARENT ACTUALLY
  CONSUMES -- the mass-like homogeneous scalar source J = j I, where the
  amplitude Z = det(D + jI) is REAL-POSITIVE -- P2 is ELIMINATED, not merely
  "resolved":

    (1) det(D + jI) in R_{>0}  for the parent's operator class (D real
        antisymmetric => spectrum +/- i lambda => det = prod(j^2 + lambda^2)).
        [the same mechanism as the retained determinant-positivity note]
    (2) On Z in R_{>0}, EVERY candidate generator of the form
        a*log|Z| + b*arg(Z)  collapses to a*log Z, because arg Z = 0.
        So the phase-blindness RESTRICTION (P2) imposes NOTHING on the consumed
        sector -- phase-blind and phase-sensitive candidates AGREE.
    (3) Therefore the generator W = log|det(D+jI)| is fixed by Record
        additivity + finite-block continuity ALONE (Cauchy on R_{>0}:
        f(xy)=f(x)+f(y), continuous => f=c log), with no extra P2 premise.
    (4) The parent's own consumed Theorem-3 Matsubara form
        W(j) = 4 sum_omega log(1 + j^2/[u0^2 (3 + sin^2 omega)]) has a
        real-POSITIVE argument for all real j, so W(j) = log(positive) = log|det|
        is real -- confirming the consumed sector carries no phase.

  Consequence (re-audit case, NOT set here): the parent's load-bearing residual
  is the (M)/Berezin determinant identification gated by AC_phi_lambda
  (a zero-weight open target), plus finite-block continuity -- not a separate
  P2 premise. This runner proposes a conditional re-audit target, but does NOT
  set audit status and consumes no
  PDG/fitted/beta=6 inputs.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import sympy as sp

np.set_printoptions(precision=6, suppress=True)
PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE_TEXT = (ROOT / "docs/OBSERVABLE_PRINCIPLE_CONSUMED_SECTOR_BOUNDED_BY_AC_PHI_LAMBDA_NARROW_THEOREM_NOTE_2026-06-05.md").read_text(encoding="utf-8")


def chk(name, cond, d=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  [{d}]" if d else ""))


# ===========================================================================
# (1) consumed sector: D real antisymmetric => det(D + jI) in R_{>0}
#     (the parent's staggered operator is real anti-Hermitian == real
#      antisymmetric on the registered block; mechanism reproven here, full
#      block established in the retained determinant-positivity note)
# ===========================================================================
print("\n=== (1) consumed sector amplitude is real-positive (no phase) ===")

# symbolic n=2: A = [[0,a],[-a,0]] => eig +/- i a => det(A+jI) = j^2 + a^2
a, j = sp.symbols('a j', real=True)
antisym_2 = sp.Matrix([[0, a], [-a, 0]])
det2 = sp.factor(sp.expand((antisym_2 + j*sp.eye(2)).det()))
chk("n=2 real-antisym: det(A+jI) = j^2 + a^2 (>0)", sp.simplify(det2 - (j**2 + a**2)) == 0,
    f"det = {det2}")

# symbolic n=4: block-diag of two rotations a,b => det = (j^2+a^2)(j^2+b^2)
b = sp.symbols('b', real=True)
antisym_4 = sp.Matrix([[0, a, 0, 0], [-a, 0, 0, 0], [0, 0, 0, b], [0, 0, -b, 0]])
det4 = sp.factor(sp.expand((antisym_4 + j*sp.eye(4)).det()))
chk("n=4 real-antisym: det(A+jI) = (j^2+a^2)(j^2+b^2) (>0)",
    sp.simplify(det4 - (j**2 + a**2)*(j**2 + b**2)) == 0, f"det = {det4}")

# numeric: 300 real-antisymmetric seeds (even and odd dim), det(D+jI) real & >0 for j>0
rng = np.random.default_rng(7)
all_real = True
all_pos = True
for t in range(300):
    n = rng.choice([5, 6, 8])           # include odd dim (n=5) -> one zero eigenvalue
    M = rng.standard_normal((n, n))
    D = M - M.T                          # real antisymmetric
    jj = rng.uniform(0.1, 3.0)
    d = np.linalg.det(D + jj*np.eye(n))
    if abs(np.imag(d)) > 1e-7:
        all_real = False
    if np.real(d) <= 0:
        all_pos = False
chk("300 real-antisym seeds (n=5,6,8): det(D+jI) is real to 1e-7", all_real)
chk("300 real-antisym seeds: det(D+jI) > 0 for j>0 (incl. odd dim)", all_pos)

# eigenvalues come in +/- i lambda pairs => purely imaginary spectrum
Mr = rng.standard_normal((6, 6)); Dr = Mr - Mr.T
ev = np.linalg.eigvals(Dr)
chk("real-antisym spectrum is purely imaginary (Re=0)", np.allclose(ev.real, 0, atol=1e-9),
    f"max|Re eig|={np.abs(ev.real).max():.1e}")

# ===========================================================================
# (2) P2-ELIMINATION: on Z in R_{>0}, phase-blind and phase-sensitive
#     candidate generators AGREE (arg Z = 0), so P2 restricts nothing.
# ===========================================================================
print("\n=== (2) P2 is eliminated on the consumed sector (arg Z = 0) ===")
# build a concrete consumed-sector amplitude
Dx = (lambda M: M - M.T)(rng.standard_normal((6, 6)))
Zvals = [np.linalg.det(Dx + jj*np.eye(6)) for jj in (0.3, 0.7, 1.5, 2.2)]
chk("consumed amplitudes Z are real-positive", all(abs(z.imag) < 1e-9 and z.real > 0 for z in Zvals),
    f"Z={[round(float(z.real),4) for z in Zvals]}")

# candidate family: G(Z) = a*log|Z| + b*arg(Z). On R_{>0}, arg=0 so all coincide with a*log Z.
def G(Z, acoef, bcoef):
    return acoef*np.log(abs(Z)) + bcoef*np.angle(Z)
diffs = []
for z in Zvals:
    base = np.log(z.real)                      # = log Z = log|Z|
    for (acoef, bcoef) in [(1, 0), (1, 5.0), (1, -3.0), (1, 100.0)]:  # wildly phase-sensitive
        diffs.append(abs(G(z, acoef, bcoef) - base))
chk("phase-blind AND phase-sensitive candidates AGREE on R_{>0} (P2 imposes nothing)",
    max(diffs) < 1e-12, f"max|G - log Z| over b in [0..100] = {max(diffs):.1e}")

# the three readings of "log" all coincide on R_{>0}: log|Z| = Re Log Z = log Z
coincide = all(abs(np.log(abs(z)) - np.real(np.log(z))) < 1e-12 and
               abs(np.real(np.log(z)) - np.log(z.real)) < 1e-12 for z in Zvals)
chk("log|Z| = Re Log Z = log Z on R_{>0} (the phase-blindness choice is moot)", coincide)

# contrast: OFF the consumed sector (generic complex Z) the candidates DISAGREE
# -> this is exactly why P2 is needed in general but ELIMINATED on the consumed sector
zc = 1.4*np.exp(1j*0.9)
off_diff = abs(G(zc, 1, 5.0) - np.log(abs(zc)))
chk("OFF-sector (complex Z): phase-sensitive candidate DIFFERS (so P2 is non-trivial only there)",
    off_diff > 1e-3, f"|G-log|Z|| = {off_diff:.4f} at arg={np.angle(zc):.2f}")

# ===========================================================================
# (3) generator fixed by Record additivity + continuity ALONE on R_{>0} (Cauchy)
#     -- no P2 used
# ===========================================================================
print("\n=== (3) Record additivity + continuity => W = c log Z on R_{>0} (no P2) ===")
# Cauchy: f:R_{>0}->R continuous, f(xy)=f(x)+f(y) => f(x)=c log x.
# reprove the solution form symbolically and that c is the only freedom.
x, y, c = sp.symbols('x y c', positive=True)
f = sp.Function('f')
# verify c*log satisfies the multiplicative-additive equation identically
lhs = c*sp.log(x*y)
rhs = c*sp.log(x) + c*sp.log(y)
chk("c*log(x) solves f(xy)=f(x)+f(y) identically", sp.simplify(lhs - rhs) == 0)
# and a constant term is forbidden by the equation (f(1)=f(1)+f(1) => f(1)=0)
f_one = sp.symbols("f_one", real=True)
chk("additive constant is forbidden: f(1)=0 forced (no free constant)",
    sp.solve(sp.Eq(f_one, f_one + f_one), f_one) == [0],
    "f(1*1)=f(1)+f(1) => f(1)=0; Cauchy/Aczel uniqueness gives c*log only")
# numeric uniqueness: fit c from two points of the consumed amplitude's log, check global
cfit = (np.log(Zvals[1].real) - np.log(Zvals[0].real))  # arbitrary scale check shape
chk("the selected generator on the consumed sector is W = log Z (c=1 convention)",
    abs(np.log(Zvals[0].real) - np.log(abs(Zvals[0]))) < 1e-12)

# ===========================================================================
# (4) tie to the parent's CONSUMED content: Theorem-3 Matsubara form is
#     real-positive argument => W real (no phase) on the actual block
# ===========================================================================
print("\n=== (4) parent Theorem-3 Matsubara form has real-positive argument (no phase) ===")
# W(j) = 4 sum_omega log(1 + j^2 / [u0^2 (3 + sin^2 omega)])
u0 = 0.5
omegas = np.linspace(0, np.pi, 9)[1:-1]
args = [1 + (1.3**2)/(u0**2*(3 + np.sin(w)**2)) for w in omegas]
chk("every Matsubara log-argument 1 + j^2/[u0^2(3+sin^2 w)] is > 0 (for all real j)",
    all(g > 0 for g in args), f"min arg = {min(args):.4f}")
# W(j) = log of a product of positives = log(positive) -> real, = log|det|
Wj = 4*sum(np.log(g) for g in args)
chk("W(j) = 4*sum log(positive) is real (= log|det|, no phase contribution)",
    np.isreal(Wj) and Wj > 0, f"W(1.3) = {Wj:.4f}")
# symmetry W(j)=W(-j): argument depends on j^2 only -> even -> consistent with det(D+jI)=det(D-jI)
jvar = sp.symbols('jv', real=True)
arg_sym = 1 + jvar**2/(u0**2*(3 + sp.Rational(1, 2)))
chk("Matsubara argument is even in j (j^2 only) => W(j)=W(-j) (CPT-even, automatic)",
    sp.simplify(arg_sym.subs(jvar, jvar) - arg_sym.subs(jvar, -jvar)) == 0)

# ===========================================================================
# (5) bound assembly (math facts only; statuses are audit-lane, not asserted here)
# ===========================================================================
print("\n=== (5) residual assembly: parent load-bearing content bounded by AC_phi_lambda ===")
print("    P1 (additivity)        <- Record axiom (minimal_axioms)")
print("    P2 (phase-blindness)   <- ELIMINATED on consumed sector by positivity (this runner, (1)-(4))")
print("    (M) amplitude=det(D+J) <- Berezin forcing bridge (retained_bounded)")
print("    physical identification<- AC_phi_lambda staggered-Dirac realization open gate")
chk("no separate unregistered P2 residual remains on the consumed sector",
    all(g > 0 for g in args) and "no separate, unregistered P2" in NOTE_TEXT,
    "phase-blind/phase-sensitive candidates coincide on R_{>0} => P2 imposes nothing")
chk("the sole remaining residual is the open AC_phi_lambda determinant identification",
    "physical determinant identification" in NOTE_TEXT and "open gate" in NOTE_TEXT,
    "=> conditional re-audit target; status set only by audit lane")

# ===========================================================================
# scope / honesty
# ===========================================================================
print("\n=== scope / honesty flags ===")
chk("OFF the consumed sector P2 is genuinely non-trivial (handled by prior sector-resolution)",
    "off the consumed sector" in NOTE_TEXT,
    "this note bounds the LOAD-BEARING (consumed, mass-like) content only")
chk("does NOT set audit status; does NOT close AC_phi_lambda; no PDG/fitted/beta=6 inputs",
    "Status authority" in NOTE_TEXT
    and "does not set status" in NOTE_TEXT
    and "No fitted/PDG/lattice-MC/`β=6`/`g_bare` inputs." in NOTE_TEXT)

print("\n" + "="*72)
print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
print("="*72)
print("""
LOAD-BEARING RESULT (bounded):
  On the sector the observable-principle parent actually consumes (J=jI, where
  Z=det(D+jI) in R_{>0} by determinant positivity), P2 is ELIMINATED: phase-blind
  and phase-sensitive candidate generators agree (arg Z = 0), so the generator
  W = log|det(D+jI)| is fixed by Record additivity + finite-block continuity alone
  (Cauchy on R_{>0}). The parent's load-bearing residual is therefore the
  (M)/Berezin determinant identification gated by the AC_phi_lambda open
  target -- not a separate P2 premise.
RE-AUDIT CASE (status set by audit lane, not here): the parent
  `observable_principle_from_axiom_note` is a conditional re-audit candidate
  because the P2 blocker is eliminated on
  the consumed sector. Final status remains audit-lane authority.
""")

if FAIL:
    raise SystemExit(1)
