lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T00:06Z

# gap-ps-disint-max (queue row 957): Piazza-Shen disintegration against (LSI-J-seed)

Worker file, written section by section. Pinned at commit 5da1cade7 of `claude/ym4d-hard-route`.
Author: Claude Fable 5.2 (max), Mac mini worker 1, as AUTHOR. Not checked by another model.
Labels used: PROVED, CONDITIONAL (on named inputs), GUIDE (numeric, proves nothing), OPEN.

Credit. The new input is Piazza and Shen, arXiv:2610.35286 (Theorem 1.1). The lattice two-slice setting and
the vacuum factors follow the gap lane of this repository, which builds on the account of Ethan Sussman and
Levent Alpoge (with Claude and Codex as authors of their text). Each section names what it takes from whom.

## 0. Plan (at most eight steps; one step per response)

1. Read the target: (LSI-J-seed), Theorem BR, Corollary BR-J and Section 7.3 of `library/gap-fc-max.md` (row 947),
   and the two prior digests (`library/prior/gap-fullread-2.md` Section 1, `library/prior/gap-lit-bridge-lsi.md`).
   Duplicate check against `library/open-core.md` and the FINISH rows. Write the exact statements.
2. Read Piazza-Shen itself (`~/ym4d-papers/dl-2026-11-11/`): the two-scale criterion, the block law, the coarse
   law, and where dimension 2 is used. Write the proof skeleton with line anchors.
3. STEP 1 of the row: which step fails in 3D/4D and why; is the two-slice law J closer to their 2D setting
   (disintegration over temporal links, or over one slice given the other).
4. STEP 2 of the row: fact tests (compact U(1) Coulomb phase, frozen Q_8 and 2T, SMALL-BOX use of the box size,
   the worst-case ceilings 2/3, 0.775, 4 G_3 = 1.0109, the Bakry-Emery ceiling at beta 1 of row 941).
5. STEP 3, stage A: the two-scale disintegration of J written as a real proof attempt; the block conditional
   laws and their LSI constants.
6. STEP 3, stage B: the coarse law at the box size; close it or state the exact obstruction.
7. If it does not close: the smallest unproved inequality, and one GUIDE test (run only under the numeric lock
   and with 50 percent memory free).
8. Verdict table and the RESULT line.

Status log (updated in place):

- 2026-11-14T12:06Z: file created; steps 1-8 not started.
- 12:25Z: Sections 1 and 2 written (inputs read, duplicate check, Piazza-Shen skeleton). Next: Section 3 (STEP 1).

## 1. Target, objects, duplicate check (READ; no new claim)

**Read at 5da1cade7.** FINISH.md (lines 1-84, 299-349, rows 954 and 957), GOAL.md, `library/gap-fc-max.md`
(row 947) lines 39-282 and 487-590, `library/prior/gap-fullread-2.md` Section 1, `library/prior/gap-lit-bridge-lsi.md`
in full, `library/gap-lsij-scale-opus.md` (row 954, in progress) Sections 3, 4, 5b-5e, 6, and the four ceiling lines
of `library/gap-status-1113.md` (68, 110, 112, 341).

**Objects (row 941 and row 947, quoted in short).** B a periodic spatial box, L = 3|B| links, M = (S^3)^L in R^(4L)
with the unit-sphere metric. V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2),
<x, w> = sum_l <x_l, w_l> (temporal gauge). Omega its top eigenfunction, nu = Omega^2 dx, m(dw) = e^(-V(w)/2) Omega(w) dw.
The two-slice law is J(dx, dw) = m(dx) e^(beta <x, w>) m(dw)/Z on M x M.

**Reading of J used below (one line; PROVED by unrolling Omega = lim lambda_0^(-n) T_0^n 1).** m(dx) = e^(-V(x)) H(x) dx,
where H(x) is the integral over a half-infinite time of the Wilson weights of all plaquettes that do not lie in the
slice of x (limit of normalised finite times). So
  J(dx, dw) = H(x) e^(-V(x)) e^(beta <x, w>) e^(-V(w)) H(w) dx dw/Z.
J is the law of two consecutive time slices of the 4D Wilson measure on B x Z in temporal gauge. H is the "vacuum
factor". It is gauge invariant and not local.

**Target (row 947, 7.1-7.3).**
  (LSI-J)_(alpha_J): Ent_J(Phi^2) <= (2/alpha_J) E_J[ |grad_x Phi|^2 + |grad_w Phi|^2 ] for smooth Phi on M x M, bounded
  above and below, invariant under the gauge group acting on both slices at once (tangential gradients).
  (LSI-J-seed)_a: on B = (24a)^3, one even a >= 30: (LSI-J) with alpha_J >= 2 beta K_a, K_a = (C_beta(x_*) + 3 log a)/(a - 2),
  C_beta(x_*) = log(72 beta 24^3/x_*) (16 at beta 2.3).
Corollary BR-J (row 947; HOLDS in check 949 per the queue row): (LSI-J-seed)_a gives (HC-vac)_(K_a), and Proposition HC
(row 931, check 938) then gives the seed.

**Two remarks on the size of the target (PROVED, arithmetic).**
- (T1) With box side b = 24a: 2 beta K_a = 48 beta (C_beta + 3 log(b/24))/(b - 48). So (LSI-J-seed) asks for alpha_J above
  about (144 beta log(b/24) + 48 beta C_beta)/b on ONE box of side b. Any lower bound alpha_J(b) with
  b alpha_J(b)/log b -> infinity gives (LSI-J-seed)_a for some a. In particular a box-uniform (LSI-J), with any
  positive constant, gives it. This is why a volume-uniform theorem of Piazza-Shen type is the right kind of input.
- (T2) The free photon has alpha_J = c_min = beta (e^(omega_min) - 1), about 2 pi beta/b (row 954 Section 3). It fails
  (T1) by the factor (24/pi)(C_beta + 3 log a), above 59 for every a (row 947 4.3).

**Duplicate check (rule 0a).** `grep -n -i -E "LSI-J|Piazza|disintegrat|two-scale|Otto|Reznikoff|log-sobolev|LSI"`:
no hit in `library/open-core.md` and `library/l17c.md`; one unrelated hit in `library/open-registry.md` (line 276,
H-STAGE). FINISH rows that name Piazza-Shen or a two-scale method: 689, 690, 697, 713, 719, 735, 939, 955 (reading
rows or one-line leads), 936 (two-scale wording for the cut rotation; another object), 941 (names "a block or
two-scale decomposition" as a possible input; its result has no such attempt), 947 (states (LSI-J-seed)), 954 (GUIDE
measurement of R_J; in progress; no proof attempt), 957 (this row), 958 (its check). No row attacks (LSI-J) by a
disintegration. Disintegration of J over one slice given the other IS the older route: (LSI-vac) + (SG-step)/(SC),
rows 931, 941, 944, 950, 952. I do not attack (SG-step) or (SC); Section 3 only places them. I proceed.

**Sussman-Alpoge account.** Rows 938-941, 946, 947 and 955 record that `library/sa-index/` has no log-Sobolev,
hypercontractive or two-scale statement (955: only block Poincare estimates of the deterministic RG, and SA 3717-3720
"No gap above the invariant subspace has been proved"). I did not repeat those greps. Their account enters through
the transfer frame and the slice/axial-gauge setting. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text.

## 2. Piazza-Shen, read in full (arXiv:2610.35286v1, 26 Oct 2026, pp. 1-11; fetched to a scratch folder, not committed)

`~/ym4d-papers` does not exist on this machine. I fetched the PDF from arxiv.org and read the extracted text
(pp. 1-11 in full; pp. 12-13 are Remark 7.2 and references). Page and equation numbers below are theirs.

**Theorem 1.1 (p. 1).** G = SU(N), periodic square lattice (Z/LZ)^2, density exp(N beta sum_p Re Tr U_p) against product
Haar. Then Ent(F^2) <= 2 C_(N,beta) sum_e integral of |grad_e F|^2, for all smooth F of ALL edge variables, with C_(N,beta)
independent of L. Metric: Hilbert-Schmidt, <X, Y> = Tr(X^dagger Y), for which Ric = (N/2) g.

**Proof skeleton, with the place where each input is used.**
- (PS-a) Section 2, group only. Single-plaquette density w, e^(-2t) <= w <= e^(2t), t = N^2 |beta|. Doeblin split
  w = (1 - r) + r v, r = 1 - e^(-2t)/2. Lemma 2.1: w^(*k) = 1 + r^(k-1) (w - 1) * v^(*(k-1)). Lemma 2.2: w^(*k) - 1 and its
  first two derivatives are at most M r^(k-1) in sup norm. (2.5): the same for log w^(*k) once M r^(n-1) <= 1/3.
- (PS-b) Section 3, the 2D step. Block B of m x m plaquettes, n = m^2. Integrate the n - 1 edges I_B that cross an
  axial spanning tree of plaquette centres. (3.1): the integral of prod_(p in B) w(U_p) over I_B equals
  w^(*n)(W_(dB)(s)), a function of the boundary holonomy only. Used: each integrated edge lies in exactly two
  plaquettes, and the identity integral of w(A u B) w(C u^(-1) D) du = w^(*2)(B A D C).
- (PS-c) (3.2)-(3.3): the marginal of the kept edges S is prod_B w^(*n)(W_(dB)(s)) ds; the conditional law of the
  integrated edges is a product over blocks. Used: the kept edges carry no plaquette weight of their own (a
  one-dimensional skeleton), and the blocks are separated by kept edges.
- (PS-d) Lemma 4.1 and (4.3), the macro law. |Hess log w^(*n)(W_(dB))| <= 4 n^(1/2) (|grad psi| + |Hess psi|), psi = log w^(*n):
  perimeter 4 n^(1/2) against the decay r^(n-1) in the AREA n. For n large the Hessian of the macro log-density is at
  most 1/2, and Ric - Hess >= 1/2 gives the macro LSI with constant 4 by Bakry-Emery. Used: positive Ricci
  curvature. This is the only place; it is why U(1) is excluded (Remark 1.2).
- (PS-e) Section 5, the micro laws. Haar product LSI (Bakry-Emery) plus Holley-Stroock on one block: K = e^(4tn).
  Group-blind apart from the Haar LSI; blocks of bounded size only.
- (PS-f) Section 6, gluing. Entropy chain rule (6.1); Lemma 6.1 bounds the gradient of s -> nu_s(F^2)^(1/2) by the
  block Poincare inequality and |grad_e H_R| <= 2t. Group-blind. This is the two-scale criterion of Otto-Reznikoff
  and Grunewald-Otto-Villani-Westdickenberg in the simple form of Bauerschmidt-Bodineau (their references
  [OR07, GOVW09, BB19]).
- (PS-g) Section 7: C_(N,beta) must grow with beta (at least beta^(1/3) for SU(4), from a degenerate non-minimal critical
  point; Remark 7.1: the test function can be gauge invariant). So no beta-uniform LSI is to be expected.

**Their own words on dimension (p. 2, short quote).** "In higher dimensions, conditional integrations would naturally
produce nonlocal, larger Wilson loops, which would be much more difficult to analyze."

**What the theorem is, in the lane's language.** The mechanism is (PS-a)+(PS-b): one block of area n is disordered
as soon as ONE of its n plaquettes takes the flat part (1 - r) of the Doeblin split, because in two dimensions a
loop bounds one surface. The rate r^(n-1) is an area law at every beta. (PS-d) then needs only that the area decay
beats the perimeter. (PS-e) and (PS-f) are soft.
