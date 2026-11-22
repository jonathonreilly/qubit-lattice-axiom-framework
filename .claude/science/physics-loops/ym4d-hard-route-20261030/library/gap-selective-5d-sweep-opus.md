lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-22T17:57Z

# Row 1382: the selective facts on the record against (5D) and (AH)

Row `gap-selective-5d-sweep-opus`, Claude Opus 5.5 high, Mac mini worker 2, commit 2df402783, started 2026-11-22T05:57Z (date -u).
Reading and short proofs. No new attack. Checked by no one.

## Plan

Source: `library/gap-mech-direction-fable.md` (row 1380), Section 5, row 2.
For each positive selective statement on the record, read the statement and its proof in its file and say:
(a) does the proof use d = 4 through a scale-free sum (a sum over scales or a log-divergent lattice sum that
is marginal exactly at d = 4)? (b) does the statement hold verbatim for SU(2) in d = 5 at weak coupling
(no mass gap; test (5D))? (c) does it hold verbatim for SU(2) with an adjoint Higgs factor (test (AH))?

Items, in order:
1. Row 1141, items (2) and (8).
2. Lemma NAB, row 1018.
3. Lemma FR, row 1011.
4. Identity CUBE and Lemma SOFT, row 1016.
5. Corollary WN2's rho, row 1013.
6. Proposition LF and Theorem BD, row 1034.
7. M-C, row 1380.
8. Any other selective statement in the registry of `parts/gap.md`.

Decisive outcome: the list of selective facts that survive (5D). Empty list: no selective fact on the record sees
the scale. Non-empty: name the seed.

## Repo search

(written as each item is read)

Searched before judging (grep, this checkout): the row files named in the brief; `parts/gap.md` (registry, via
`git show HEAD:`); `library/open-core.md` and the FINISH rows for "5D", "five dimensions", "adjoint Higgs".
Hits are cited at each item. The test definitions are row 1380's (`gap-mech-direction-fable.md` L152-158):
(5D) SU(2) in five dimensions at weak coupling, massless (belief grade, row 1011 Section 6); (AH) SU(2) with an
adjoint Higgs field in its Coulomb phase, massless (belief grade, item A16 of row 1017).

**Reading of "survives".** A fact survives (5D) when it is false in (5D), or when its proof fails there at a
named line, so that it can tell the gapped theory from a massless one. A fact that holds verbatim in (5D)
(constants allowed to change with the number of plaquettes per link, 2(D-1)) is a lattice-scale fact and does
not survive. The same reading for (AH). Notation: D is the lattice dimension, d a sub-cube dimension.

## Item 1. Row 1141, items (2) and (8) (`library/gap-crux2-astra62.md` L45-133)

**Statements.** (2): in a cube of side R inside a periodic Wilson SU(2) torus, with probability at least
1 - (2+R)^(-k), every adjoint section s has covariant energy at least c/(1 + b + (log(2+R))^(2/d)) |s|^2.
(8): E lambda_x >= 1/(64(1+6b)) for the minimum over a common axis of the forward-plaquette cross products.

**Where the proof uses the dimension.** Only locally: (i) the one-link conditional law is e^(h.q) with
|h| <= 2(D-1) b, so 6b at D = 4 (L55); (ii) the density bound M_b = 4(1 + 2(D-1) b) and the cap estimate (3);
(iii) cells of side three, 6^d of them per rectangle of side m (L96), and the Poincare constant 2 d m^2 on a
rectangle of side m ~ (log R)^(1/d) (L105-117); (iv) a union bound over at most R^d rectangles. There is no sum
over scales and no lattice sum that is marginal at D = 4. The log R is from the union bound, not from a
propagator.

**(5D).** Holds verbatim in D = 5 with 6b replaced by 8b and 6^d, d <= 5, in the constants: every line above is
local and uses only that the two pinning plaquettes have distinct links and a common root (L127). So (2) and (8)
hold in five dimensions at weak coupling, where the theory is believed massless. **Does not survive.** This is
row 1380's own example (L154-158, L287).

**(AH).** With a fixed-length adjoint Higgs field phi (|phi_x| = 1) and hopping kappa phi_x . Ad(U_xy) phi_y,
the one-link conditional density is the Wilson one times a factor in [e^(-kappa), e^(kappa)], so (3) holds with
M_(b,kappa) <= e^(2 kappa) M_b, and (4), (6)-(8), (2) hold with delta_(b,kappa) = e^(-2 kappa) delta_b
(ARGUED in this one line; for a radial Higgs field condition on the moduli and truncate). The constant degrades
as kappa grows: deep in the Higgs/Coulomb phase the plaquettes are near rotations about phi, and the section
s = phi has covariant energy of order |phi|^2/kappa per site, which is mass-like in R but small. So at each
fixed kappa (2) and (8) hold with a smaller constant; they hold in the massless Coulomb phase. **Does not
survive.**

**Selective against (U1)?** Yes (D = 0 for abelian transport, L210). So these are the record's clean example of
a fact that passes (U1) and fails (5D): a statement of ultraviolet roughness.

