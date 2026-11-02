lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T21:54Z

# rel-phi-c: deciding (REL-Phi) of `library/seam-nonlinear-c.md` Section 4

Queue row 63, mapped side. Statement pinned at commit `bef9ac33c`. Author:
Anthropic claude-opus-5-5, effort max, Mac mini worker, 2026-11-02.
Same-model work: not independent in model, not a gate, not an audit, no
status.

Status: in progress (sections are added as they are written; the verdict
line below is final only when Section 7 exists).

**Firewall.** Mapped side. Read only FINISH.md, GOAL.md, mapped-side
`library/` notes, `parts/hard-core--mapped.md` and `parts/hard-core--excess.md`
excerpts, and mapped-side check code, as listed in Section 8. No file
excluded for the mapped side, no gate file, no Sussman-Alpoge text, no
literature, no file of the independent side's library.

## 1. The statement tested, units, and criteria fixed before any run

**Setting** (as in `seam-quadratic-c` 2 and `seam-nonlinear-c` 1, 4). Fine
lattice Z^4 (or a torus), unit spacing; L odd, L >= 3, m := (L - 1)/2; depth
n; B := L^n. Level-j sites are L^j Z^4; they nest because L is odd, so a top
centre (level n) is a level-j site for every j. B_s(x) := x + {-(s-1)/2, ...,
(s-1)/2}^4. For a fine 1-form theta (link logarithms; su(2)-valued, |.| the
norm |Z|_F) its top normalization is H := B theta. For a set S of fine bonds,

    ||H||_(L^p(S)) := (B^-4 sum_(b in S) |H_b|^p)^(1/p),   so   ||H||_(L^4(S)) = (sum_(b in S) |theta_b|^4)^(1/4).

Level-j path average of a fine 1-form, for a level-j bond c = [x, x + s e_mu],
s = L^j: Q_path^(s) theta(c) := s^-4 sum_(z in B_s(x)) theta([z, z + s e_mu]),
with Q_path^(1) = identity. One-step contour average at level k (1 <= k <= n),
on level-(k-1) 1-forms A, at a level-k site y:

    Phi^(k) A(y) := L^-4 sum_(x in B^(k)(y)) A(Gamma^(k)_(y,x)),   B^(k)(y) := y + L^(k-1) {-m, ..., m}^4,

Gamma^(k)_(y,x) the axial staircase from y to x in the level-(k-1) lattice
(axes in the fixed order 1, 2, 3, 4, as in `checks/seamqc/seamqc.py`), A(Gamma)
the oriented sum over its bonds. One step is Q^(k) = Q_path^(k) - d' Phi^(k)
(mapped Lemma 3.1); the composite is Q_n = Q^(n) ... Q^(1) = Q_path^(B) - d' Phi_n
with Phi_1 = Phi^(1), Phi_(k+1) = Av^(k+1) Phi_k + Phi^(k+1) Q_k
(`seam-quadratic-c` Lemma 2.2(d)). At the background T, Phi_n^(T) is the same
expression with the transports of T (Section 2.4).

**The statement** (`seam-nonlinear-c` 4.1). (REL) asks for a fine gauge g with
g = 1 at every top centre and H with U^g_b = exp(H_b/B) T_b, and

    (REL-2)   ||H||_(L^2(Q)) <= C_2 (K_delta * E)(Q)^(1/2),   C_2, delta absolute,
    (REL-4)   ||H||_(L^4(Q)) <= C_4(L) (K_delta * E)(Q)^(1/2),
    (REL-Phi) |Phi_n^(T) H(y)| <= C_Phi(L) (K_delta * E)(Q_y)^(1/2)  at every top centre y,
    (REL-E)   E(Q) <= C_E f^2,

uniformly in depth and volume. Write Psi := Phi_n^(T) H.

**What "decide" has to mean.** (REL) is existential in the gauge. Under a fine
gauge change e^lambda with lambda = 0 at every top centre ("admissible"), Psi
moves by Av_B lambda (Lemma 2 below). So a field H whose Psi grows with depth
refutes (REL-Phi) only if no admissible gauge with the other clauses has
bounded Psi; and a proof must exhibit or construct the gauge. Both readings
are tested below.

**Registered criteria for the runs (written before any run).** A run can
refute a hand identity or show a constant growing; it cannot prove a bound.
1. Identities (Lemmas 1 to 3 below) on the actual nested map of
   `seamqc.py` (`balaban_Q`, axial staircases), d = 4, L = 3, n = 2, random
   fields on the torus of side 18: the formula of Lemma 1 against the
   recursion of `seam-quadratic-c` 2.2(d) and against Q_2 = Q_path^(9) - d' Phi_2;
   the gauge law; constants. PASS if every relative error is below 1e-10. A
   value above 1e-8 means a hand step is wrong and stops the item there.
2. The kernel w_n of Phi_n at one top centre, built from Lemma 1, for
   (L, n) = (3, 1), (3, 2), (3, 3), (5, 1), (5, 2): record N_tot := the
   l^(4/3) norm of w_n over all fine bonds (the exact L^4 to angle constant)
   and N_ann := max over the annuli A_j of Section 3 of the l^(4/3) norm of w_n
   on A_j. Lemma A (hand) predicts N_ann <= C_A(L) = 3.4 L + 1 for every n, and
   Example E (hand) predicts N_tot growing at least like n^(3/4). REFUTES
   Lemma A if some N_ann exceeds C_A(L). Also check sum over direction-mu
   bonds of w_n = 0 (Lemma 3) to 1e-12.
3. Example E: its two exact sums (Section 3.3) for L = 3, n = 1 to 12, to
   display the growth of Psi / ||dlambda||_(L^4) against (log B)^(3/4).
   Illustration only; the bound is proved by hand.
