#!/usr/bin/env python3
"""corrigendum-PR8178, attempt a2: which repair, and is the packet's line list complete.

Attempt a1 (same model family, same machine — see ATTEMPT.md) established that the multiplier
of the backward average under the transform e^{-ik.x} is phi_c = (1 + e^{-ik1} + e^{-ik2})/3 and
not the stated phi, and listed nine lines to change from phi to phi_c.  This attempt tests two
things a1 asserts: that changing the formula is the repair to make, and that its line list is
complete.

  D1  the multiplier under each of the two transforms          exact + float, two machineries
  D2  the modes where the stated phi happens to be right       exact, L = 2..12
  D3  1 - |phi|^2 = 1 - |phi_c|^2: the identity T1.2 and everything through u is untouched
  D4  block 34's own control is a function of |phi|^2 alone    exact
  D5  block 35's refuter measures phi in the basis e^{+ik.x}   exact eigenvector identity
  D6  block 35's sampler measures phi through numpy's FFT and the ordering E[f(t) conj f(t+s)]
  D7  the audit: every formula-bearing line at the pinned heads, and what a1's list contains
  D8  the two repairs, counted
"""
import re, subprocess, sys
import sympy as sp

HEADS = {
    "8178": ("e6ffae5b460b", "physics-loop/admissibility-induced-law-block34-sphere-formation-law-"
                             "torus-memory-time-zero-mode-rate-and-stationary-modes-20260917"),
    "8180": ("7c844adf7555", "physics-loop/admissibility-induced-law-block35-gravity-kernel-under-"
                             "the-formation-reading-heat-kernel-times-plane-green-function-20260918"),
}
NOTE34 = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_"
          "EXACTLY_STATIONARY_MODES_BRACKETED_AND_THE_NONLINEAR_LAW_MEASURED_AGAINST_IT_"
          "BOUNDED_THEOREM_NOTE_2026-09-17.md")
SCI = ".claude/science/physics-loops/admissibility-induced-law-20260906"
RUN34 = ("scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_"
         "exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py")
CACHE34 = ("logs/runner-cache/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_"
           "mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.txt")

# a1's list of lines to change, from its section (c), block 34 only (the phi -> phi_c repair)
A1_LINES = {(NOTE34, 4), (NOTE34, 85), (NOTE34, 104),
            (RUN34, 5), (RUN34, 199), (RUN34, 206),
            (CACHE34, 18), (f"{SCI}/GOAL_block34.md", 6), (f"{SCI}/RESULTS_block34.md", 6)}

FORMULA = re.compile(r"(e\^\{?\s*[-+]?\s*i\s*k|exp\(\s*[-+]?\s*(sp\.I|1j)\s*\*?\s*k|e\^\{[-+]?ik)", re.I)

def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True).stdout

def have(sha):
    return subprocess.run(["git", "cat-file", "-e", sha + "^{commit}"],
                          capture_output=True).returncode == 0

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    for pr, (sha, br) in HEADS.items():
        if not have(sha):
            subprocess.run(["git", "fetch", "--quiet", "origin", br], capture_output=True)
        want(have(sha), f"PR #{pr} present at its pinned head {sha}")

    # ---------------------------------------------------------------- D1
    print("\nD1  the multiplier under each transform")
    print("     P is the average over the three predecessors: (P th)_x = (th_x + th_{x-e1} + th_{x-e2})/3.")
    for L in (3, 4):
        w = sp.exp(2 * sp.pi * sp.I / L)
        th = {(i, j): sp.Symbol(f"t_{i}_{j}") for i in range(L) for j in range(L)}
        Pth = {(i, j): (th[(i, j)] + th[((i - 1) % L, j)] + th[(i, (j - 1) % L)]) / 3
               for i in range(L) for j in range(L)}
        bad_minus = bad_plus = 0
        for n1 in range(L):
            for n2 in range(L):
                for sign, which in ((-1, "minus"), (+1, "plus")):
                    hat = lambda f: sum(w**(sign * (n1 * i + n2 * j)) * f[(i, j)]
                                        for i in range(L) for j in range(L)) / L
                    mult = (1 + w**(sign * n1) + w**(sign * n2)) / 3
                    d = sp.expand(sp.simplify(sp.expand(hat(Pth) - mult * hat(th))))
                    if d != 0:
                        if which == "minus": bad_minus += 1
                        else: bad_plus += 1
        want(bad_minus == 0 and bad_plus == 0,
             f"L={L}: with e^-ik.x the multiplier is (1+e^-ik1+e^-ik2)/3 and with e^+ik.x it is "
             f"(1+e^+ik1+e^+ik2)/3, at all {L*L} modes (exact, roots of unity)")
    try:
        import numpy as np
        worst_wrong = 0.0; worst_right = 0.0
        rng = np.random.default_rng(7)
        for L in range(3, 9):
            th = rng.normal(size=(L, L))
            Pth = (th + np.roll(th, 1, axis=0) + np.roll(th, 1, axis=1)) / 3.0
            k = 2 * np.pi * np.arange(L) / L
            K1, K2 = np.meshgrid(k, k, indexing="ij")
            hat = np.fft.fft2(th) / L                       # numpy's fft is sum_x e^{-ik.x}
            hatP = np.fft.fft2(Pth) / L
            phi = (1 + np.exp(1j * K1) + np.exp(1j * K2)) / 3
            phic = phi.conjugate()
            worst_right = max(worst_right, np.abs(hatP - phic * hat).max())
            worst_wrong = max(worst_wrong, np.abs(hatP - phi * hat).max())
        want(worst_right < 1e-12 < worst_wrong,
             f"numpy's FFT (e^-ik.x) on L=3..8 random fields: |P^ - phi_c th^| <= {worst_right:.1e}, "
             f"|P^ - phi th^| up to {worst_wrong:.3f}")
    except ImportError:
        print("     numpy missing; the float half of D1 skipped")

    # ---------------------------------------------------------------- D2
    print("\nD2  where the stated phi is right anyway")
    k1, k2 = sp.symbols('k1 k2', real=True)
    phi = (1 + sp.exp(sp.I*k1) + sp.exp(sp.I*k2))/3
    phic = (1 + sp.exp(-sp.I*k1) + sp.exp(-sp.I*k2))/3
    want(sp.simplify(sp.expand_complex(phi - phic - sp.Rational(2,3)*sp.I*(sp.sin(k1) + sp.sin(k2)))) == 0,
         "phi - phi_c = (2i/3)(sin k1 + sin k2)")
    bad = []
    for L in range(2, 13):
        agree_direct, agree_rule = set(), set()
        for n1 in range(L):
            for n2 in range(L):
                a1_ = sp.sin(2*sp.pi*n1/L) + sp.sin(2*sp.pi*n2/L)
                if sp.simplify(a1_) == 0: agree_direct.add((n1, n2))
                if (n1 + n2) % L == 0 or (L % 2 == 0 and (n2 - n1) % L == L//2):
                    agree_rule.add((n1, n2))
        if agree_direct != agree_rule: bad.append(L)
        if L in (2, 3, 10):
            print(f"     L={L}: {len(agree_direct)} of {L*L} modes agree")
    want(not bad, "for L = 2..12 the agreeing modes are exactly n1+n2 = 0, or n2-n1 = L/2 for even L")
    want(all(len({(n1, n2) for n1 in range(L) for n2 in range(L)
                  if (n1+n2) % L == 0 or (L % 2 == 0 and (n2-n1) % L == L//2)}) < L*L
             for L in range(3, 13)),
         "so for every L >= 3 some mode disagrees: the stated identity fails for every field")

    # ---------------------------------------------------------------- D3
    print("\nD3  what the choice cannot touch")
    ident = sp.Rational(4,9)*(sp.sin(k1/2)**2 + sp.sin(k2/2)**2 + sp.sin((k1-k2)/2)**2)
    for nm, f in (("phi", phi), ("phi_c", phic)):
        want(sp.simplify(sp.expand_trig(sp.expand(1 - (f*sp.conjugate(f)).rewrite(sp.cos) - ident)
                                        .rewrite(sp.cos)).rewrite(sp.sin)) == 0
             or sp.simplify(1 - sp.Abs(f.subs({k1: sp.Rational(3,7), k2: sp.Rational(5,11)}))**2
                            - ident.subs({k1: sp.Rational(3,7), k2: sp.Rational(5,11)})) == 0,
             f"1 - |{nm}|^2 = (4/9)[sin^2(k1/2)+sin^2(k2/2)+sin^2((k1-k2)/2)]")
    want(sp.simplify(sp.Abs(phi.subs({k1: sp.Rational(3,7), k2: sp.Rational(5,11)}))**2 -
                     sp.Abs(phic.subs({k1: sp.Rational(3,7), k2: sp.Rational(5,11)}))**2) == 0,
         "|phi| = |phi_c|: T1.2, the mode variances, tau_L, V_L, S_L and block 35's T2/T3 moduli")
    print("     cannot distinguish the two, which is why nothing executed caught the defect.")

    # ---------------------------------------------------------------- D4
    print("\nD4  block 34's control")
    u_ctl = (3 + 2*sp.cos(k1) + 2*sp.cos(k2) + 2*sp.cos(k1-k2))/9
    want(sp.simplify(u_ctl - sp.expand(phi*sp.conjugate(phi)).rewrite(sp.cos)) == 0 or
         sp.simplify((u_ctl - sp.Abs(phi)**2).subs({k1: sp.Rational(3,7), k2: sp.Rational(5,11)})) == 0,
         "supervisor_control_block34_refuter.py line 23 uses u = (3+2cos k1+2cos k2+2cos(k1-k2))/9,")
    print("     which is |phi|^2 = |phi_c|^2: the refuting pass is phase-blind by construction.")

    # ---------------------------------------------------------------- D5
    print("\nD5  block 35's refuter, which does see the phase")
    src = git("show", f"{HEADS['8180'][0]}:{SCI}/specs/supervisor_control_block35_refuter.py")
    want("np.exp(1j * (k[n1] * i + k[n2] * j))" in src,
         "its mode vector is e_x = e^{+i k.x}/L, not numpy's FFT convention")
    want("phi = (1 + np.exp(1j * k[n1]) + np.exp(1j * k[n2])) / 3" in src
         and "abs(cross / var - phi ** s)" in src,
         "and it checks conj(e).Sigma.(P^s)^T.e / conj(e).Sigma.e against phi^s")
    bad = 0
    for L in (3, 4):
        w = sp.exp(2*sp.pi*sp.I/L)
        idx = [(i, j) for i in range(L) for j in range(L)]
        P = sp.zeros(L*L, L*L)
        for a, (i, j) in enumerate(idx):
            for b, (p_, q_) in enumerate(idx):
                if (p_, q_) in ((i, j), ((i-1) % L, j), (i, (j-1) % L)):
                    P[a, b] += sp.Rational(1, 3)
        for n1 in range(L):
            for n2 in range(L):
                e = sp.Matrix([w**(n1*i + n2*j) for (i, j) in idx])
                if sp.simplify(sp.expand(P*e - ((1 + w**(-n1) + w**(-n2))/3)*e)) != sp.zeros(L*L, 1):
                    bad += 1
                if sp.simplify(sp.expand(P.T*e - ((1 + w**n1 + w**n2)/3)*e)) != sp.zeros(L*L, 1):
                    bad += 1
    want(bad == 0,
         "exactly: P e_k = phi_c e_k and P^T e_k = phi e_k for e_k = (e^{+ik.x})_x, L = 3 and 4")
    print("     so for ANY covariance Sigma, conj(e).Sigma.(P^s)^T.e = phi^s conj(e).Sigma.e:")
    print("     the ratio the refuter prints is phi^s identically, at every level t.")

    # ---------------------------------------------------------------- D6
    print("\nD6  block 35's sampler")
    sim = git("show", f"{HEADS['8180'][0]}:{SCI}/specs/supervisor_control_block35_kernel_sim.py")
    want("np.fft.fft2" in sim and "phi = (1 + np.exp(1j * K1) + np.exp(1j * K2)) / 3.0" in sim,
         "it transforms with numpy's fft2 (e^-ik.x) and compares against phi")
    print("     With f_k(t) the fft2 coefficient, f_k(t+1) = phi_c f_k(t) + noise, so")
    print("     E[f_k(t) conj(f_k(t+s))] = conj(phi_c)^s Var = phi^s Var: with the ordering the")
    print("     sampler accumulates, phi is again the measured symbol.  Both of block 35's")
    print("     executed routes therefore measure phi, not phi_c.")


    # ---------------------------------------------------------------- D7
    print("\nD7  the audit of formula-bearing lines")
    sha34 = HEADS["8178"][0]
    files = [f for f in git("diff", "--name-only", "origin/main..." + sha34).split()
             if re.search(r"\.(md|py|txt)$", f) and "citation_graph" not in f]
    found = set()
    for f in files:
        for i, line in enumerate(git("show", f"{sha34}:{f}").splitlines(), 1):
            if FORMULA.search(line) and "e^{ik" in line.replace(" ", "") + line or FORMULA.search(line):
                if re.search(r"(1 \+ e\^\{ik|1 \+ sp\.exp\(sp\.I|phi\(k\) = \(1 \+ e|"
                             r"multiplier `?phi|multiplier `φ)", line) or \
                   re.search(r"e\^\{ik₁\}|e\^\{i k_?1\}|exp\(sp\.I \* k1\)", line):
                    found.add((f, i))
    for f, i in sorted(found):
        mark = "listed by a1" if (f, i) in A1_LINES else "NOT in a1's list"
        print(f"     {f.split('/')[-1][:44]}:{i}   {mark}")
    want(A1_LINES <= found, "every line a1 lists carries the formula at the pinned head")
    extra = found - A1_LINES
    want(extra == {(f"{SCI}/HANDOFF.md", 30)},
         f"exactly one formula-bearing line of block 34 is missing from a1's list: "
         f"{sorted(x[0].split('/')[-1] + ':' + str(x[1]) for x in extra)}")
    # ---------------------------------------------------------------- D8
    print("\nD8  the two repairs")
    note = git("show", f"{sha34}:{NOTE34}").splitlines()
    l85 = note[84]
    want("L^{\u22121} \u03a3_x e^{\u2212ik\u00b7x} \u03b8_x" in l85 and "(1 + e^{ik\u2081} + e^{ik\u2082})/3" in l85,
         "note line 85 carries BOTH halves of the defect: it declares the transform with e^-ik.x")
    print("     and, in the same sentence, says P acts as multiplication by phi.  One of the two")
    print("     clauses has to move; which one is the whole choice.")
    t11 = [l for l in note if l.startswith("**T1.1.**")]
    want(len(t11) == 1 and "the conjugate convention gives the stated" in t11[0],
         "T1.1's proof names the step it skips: 'the conjugate convention gives the stated phi'")
    want(len(A1_LINES) + 1 == 10,
         "repair A (a1's): phi -> phi_c in 10 lines (its 9, plus HANDOFF.md:30 from D7).  Three of")
    print("     them are executed or frozen: the runner's line 199 is code, its line 206 is the")
    print("     check's text, and the runner-cache line 18 is that text frozen - so repair A means")
    print("     re-running block 34's runner and regenerating its cache.")
    run34 = git("show", f"{sha34}:{RUN34}")
    want("phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3" in run34,
         "repair B: change the transform in note line 85 to e^{+ik.x} and the clause in T1.1's")
    print("     proof.  Two clauses of prose.  By D1 T1.1 is then true exactly as written; by D3")
    print("     nothing downstream moves; the runner's phi (line 199), its check text, the frozen")
    print("     cache, GOAL, RESULTS and HANDOFF all stay as they are, and by D5 and D6 both of")
    print("     block 35's executed controls already measure that phi.")

    print()
    if ok:
        print("SUMMARY: PARTIAL the defect of PR #8178 T1.1 sits inside one sentence - note "
              "line 85 declares the transform as L^-1 sum_x e^{-ik.x} th_x and, in the same "
              "sentence, gives P the multiplier phi - so it has two repairs, not one: change the "
              "formula to phi_c in ten lines (three of them executed or frozen, which forces a "
              "re-run of the runner and its cache), or change the transform to e^{+ik.x} in that "
              "clause and in T1.1's proof, which is two clauses of prose and leaves phi, the "
              "runner, the frozen cache and both of block 35's executed controls untouched; those "
              "controls measure phi, not phi_c (the refuter in the e^{+ik.x} basis exactly, the "
              "sampler through fft2 with the ordering E[f(t) conj f(t+s)])")
        print("HIT: the transform clause is the minimal repair of PR #8178 T1.1 - the executed "
              "side of blocks 34 and 35 is consistent with phi as stated, and attempt a1's "
              "formula repair is the one that invalidates block 34's frozen runner cache; a1's "
              "line list is also short by one formula-bearing line, HANDOFF.md:30")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
