lead: anthropic/claude-opus-5-5/max laptop-subagent
row: 1078

# Check of row 1077 (gap-face-2d-astra.md), line by line

Checker: Claude Opus 5.5 (Anthropic), max effort, laptop subagent.
File under check: $T/library/gap-face-2d-astra.md, written by gpt-6-astra max (row 1077).

## Plan (refined after step 1)

1. Read rows 1077 and 1078 and the file under check in full; record the obligations and the claims list. DONE.
2. DONE. Fetch OpenAI's paper at the pin into a new empty /tmp folder; record Theorem 3.1, (3.4)-(3.8), section 3.11 (3.11.1-3.11.3), (3.67), sections 3.12.1-3.12.2, reference [18].
3. DONE. Check Step 1 premises and sections 2.1-2.2 (reduction, residual group, reflection positivity, transfer kernel) against row 1053 and its checks.
4. DONE. Check section 3.1, (5)-(8), against OpenAI (3.4)-(3.8).
5. DONE. Check sections 3.2 (9)-(10) and 3.3 (11)-(12) against OpenAI (3.6) and section 3.11.
6. DONE. Check sections 4.1-4.2, (13)-(16); judge whether a sharper use of (15) or of the unpinned decay gives a positive interval.
7. DONE. Check sections 5.1-5.5 and the step-6 next decision; judge whether it is correctly stated and weaker than the target.
8. DONE. Write the verdict table and the RESULT line.

## Working log

(step results are appended below, one step per response)

### Step 1 result: obligations and claims list

Source revision of this check: clone HEAD `6b7503d59`; the file under check
was committed at `efd25f938` (724 lines, 38,266 bytes). I read it in full.

Obligations from FINISH row 1078 (my labels O1-O8):

- O1. Section 2.1 (face reduction on the transverse torus) and 2.2
  (longitudinal reflection positivity).
- O2. Section 3.1, the Ward port (5)-(8), against OpenAI, *Sharp mass
  bounds for the two-dimensional O(4) model*, section 3.1, pp. 13-14,
  (3.4)-(3.8), at the pin the file uses.
- O3. The failures (9) at OpenAI (3.6) (section 3.2) and (12) at OpenAI
  section 3.11.3 (section 3.3).
- O4. Section 4.1, anchor and finite-cylinder comparison (15); section 4.2,
  the decision and the Ising counterexample (16).
- O5. Section 5.1, the strength statement and the implication.
- O6. Controls 5.2-5.5: compact U(1) given Frohlich and Spencer; frozen Q_8
  and 2T; Pin(2); the five-dimensional face.
- O7. Judge: is the common perturbative interval only beta_T = 0, or does a
  sharper use of (15) or of the unpinned Lipschitz decay give a positive one.
- O8. Judge: is the next decision of step 6 correctly stated, and is it
  weaker than the target.

Claims of the file, by line (my labels):

- A1 (l.63-100) premises: row 1053 sections 6.1-6.3 (FACE-LIM, ANCH, RIG),
  rows 1061/1062 checks, OpenAI Theorem 3.1 scope, row 1070 section 1,
  row 1074 section 2 (Frohlich-Simon-Spencer threshold below 2).
- B1 (l.106-132) the face density (1); B2 (l.134-147) residual group (2) and
  its kernel {+-1}; B3 (l.149-169) proof of the reduction; B4 (l.171-175)
  order of limits; B5 (l.177-181) anchor symmetry.
- C1 (l.185-203) reflection positivity via (3); C2 (l.205-225) transfer
  kernel (4), positivity, simple positive leading eigenvector, invariance.
- D1 (l.237-262) Ward variation (5); D2 (l.266-277) bracket identity (6);
  D3 (l.279-295) Ward identity (7); D4 (l.297-316) stiffness upper bound (8).
- E1 (l.320-339) independent-sheet failure (9); E2 (l.341-356) the
  gauge-direction Poincare inequality (10) is false.
- F1 (l.360-368) section 3.11.3 quote and the extra four-link factor;
  F2 (l.370-409) the sign-slice coefficient (11) and FKG failure (12).
- G1 (l.419-454) anchor gap a(beta) uniform in T; G2 (l.456-489) (13)-(15)
  and "common interval exactly {0}"; G3 (l.493-499) decision;
  G4 (l.501-521) Ising counterexample (16); G5 (l.523-533) what a positive
  interval would need.
- H1 (l.539-557) statement (17); H2 (l.559-574) finite-cylinder gap is a
  sufficient input; H3 (l.576-591) forward implication to the T = infinity
  face; H4 (l.593-602) what (17) does not give, and CA-I 2706-2712.
- I1 (l.604-629) U(1) control (18); I2 (l.631-659) Q_8 and 2T counts;
  I3 (l.661-672) Pin(2); I4 (l.674-690) five-dimensional face.
- J1 (l.717-722) next decision.

### Step 2 result: OpenAI's paper at the pin (primary text)

Folder `/tmp/opus-face2d-openai.NylL2Z`, new and empty when made. From
`openai/math` at `4eaee87548250b2682affda7d05d947c05554bae`, folder
`preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/`,
I fetched `paper.pdf` (961,282 bytes) and the LaTeX source
(`build/main.tex`, `build/sections/*.tex`, `build/references.bib`). Open
copy, no sign-in. Page text came from Apple PDFKit (a Swift script in my
scratchpad); that is text extraction, not a calculation. PDF page index
equals the printed page number. Nothing is committed.

Section 3 is `sections/preliminary.tex` ("Preliminary mixing"). What it says:

- **Theorem 3.1** (p. 12). Fixed constants `C, c, p`; (3.1)
  `Xi(beta) = exp[pi beta + C sqrt((1+beta) log(2+beta))]`; for every
  `beta >= 0`: on every *unpinned rectangular torus with each side at least
  C Xi(beta)*, for every `0 <= beta_e <= beta`, (3.2)
  `|Cov(F,G)| <= C (1+beta+|A|+|A'|+d)^20 L_F L_G e^{-c d / Xi(beta)}`,
  with `L_F = ||F||_inf + max_x Lip_x(F)`; the same on every unpinned free
  subgraph; uniqueness of the periodic local limit; (3.3) the bound on
  `Delta_beta(n)`.
- **Section 3.1** (pp. 13-14). Pinned square `Q(S) = {0..S}^2`, all
  boundary spins fixed; `t_e + s_e = q_y U_e q_x^{-1}` with a fixed twist
  `U_e`; signed `|b_e| <= b <= B`; `w_e = b_e`, except `w_e = b_e/2` on
  edges tangent to the boundary; density `Z^{-1} exp(sum w_e t_e)`;
  `X_Q(F) = S^{-1} sum_e w_e s_e . F_mu(e)(z_e)`.
  (3.4) `H_Q(F,G) = S^{-2} E sum w_e t_e conj(F_e).G_e - Cov(X_Q(F), X_Q(G))`.
  (3.5) `H_Q <= b I`, by the count `S(S-1) + 2 (S/2) = S^2` per direction.
  (3.6) with `A = - sum w_e t_e`: `D_f A = sum w_e (s_e . a)(f_y - f_x)`,
  `D_f^2 A = sum w_e t_e (f_y - f_x)^2`.
  (3.7) `D_eta s_e = t_e (eta_y - eta_x) + (eta_y + eta_x) x s_e`.
  (3.8) `E[conj(X_Q(d_S eta)) X_Q(F)] = S^{-2} E sum w_e t_e conj((d_S eta)_e).F_e
  + E X_Q(F_e x (conj eta_y + conj eta_x))`, with `(d_S eta)` equal to `S`
  times the difference. Lines 70-71 of the source: the noncommuting
  current term and its factor two fix the stiffness gain.
- **Section 3.11** (pp. 29-32). First line: "From now on use the untwisted
  zero-field ferromagnet, with `0 <= b_e <= b`. This restriction is
  essential." 3.11.1 (pp. 29-30): association (Newman;
  Bulinski-Shabanovich), the plane-rotator Ginibre inequality, the
  Fortuin-Kasteleyn representation, the FKG lattice condition for angle
  marginals. 3.11.2 (p. 30): an XY spin is `(tau^1 cos gamma, tau^2 sin gamma)`;
  "Given the angles, the two sign species are independent ferromagnetic
  Ising systems." 3.11.3 (p. 31): `q_i = (cos alpha_i z_i, sin alpha_i w_i)`;
  the a priori law; then "Conditional on alpha, the two circle sectors are
  independent XY models", with `J^1_e = b_e cos alpha_x cos alpha_y`,
  `J^2_e = b_e sin alpha_x sin alpha_y`. (3.67) (p. 32) is the boxed bound
  `|Cov(F,G)| <= C(1+B+|A|+|A'|+d)^20 L_F L_G e^{-cd/s}`, stated "uniformly
  on the stated unpinned tori and on free subgraphs, for every set of
  couplings `0 <= b_e <= b`".
- **Section 3.12.1** (p. 32): uniqueness of the periodic local limit, by
  cutting bonds through interpolation; it does not claim uniqueness among
  nonperiodic Gibbs states. **Section 3.12.2** (pp. 32-33): site and link
  reflection positivity from `e^{b q.q'} = sum b^m (q.q')^m / m!` (tensor
  powers); the one-step translation is a nonnegative self-adjoint
  contraction on the reflection Hilbert space; in the corollary's proof,
  `limsup |<F, T^n F>|^{1/n} <= e^{-c/s(b)}`, positivity of the spectral
  measure, and density of Lipschitz functions give the spectral inclusion.
- **Reference [18]** (p. 101): Jurg Frohlich and Thomas Spencer, "The
  Kosterlitz-Thouless transition in two-dimensional Abelian spin systems and
  the Coulomb gas", Comm. Math. Phys. 81 (1981) 527-602. The introduction
  (p. 2) cites [5, 26, 18] for the low-temperature two-component phase with
  "no positive exponential spin-decay rate".

Locator check: the file's locators ((3.4)-(3.8) on pp. 13-14; (3.6) on
p. 13; section 3.11.3 on p. 31; section 3.11.1 on pp. 29-30; (3.67) and
section 3.12.1 on p. 32; reference [18]) all match the primary text. The
quoted phrase "the two circle sectors are independent XY models" is exact.

### Step 3 result: premises (A1) and sections 2.1-2.2 (B1-B5, C1-C2)

Sources read for this step: row 1053 `gap-wall-vectors-max.md` L222-306
(conventions, FACE-LIM, ANCH, RIG, FACE-MW, 6.5, EVEN); row 1061
`gap-wall-vectors-check-astra.md` L40-166; row 1062
`gap-wall-vectors-check-opus.md` L37-84 and J1 (L109-117); row 1070
`gap-aniso-check-astra.md` section 1; row 1074
`gap-bridge-exercise-check-astra.md` sections 2 and 8; the SA outline
index `sa-index/chunk-01.md` L62-73 and `obligations.md` L18-29.

**A1 (premises), HOLDS.** Each attribution matches its source.
Row 1061 FACE-LIM: "says nothing about periodic longitudinal holonomies";
row 1062 C1: "The free boundary is essential". Rows 1061 and 1062 on RIG:
the extension to every compact Lie group needs a group-dependent constant.
Row 1062 C5 and row 1061: FACE-MW needs integer `r >= 1`. Row 1053 6.9 and
row 1062 J1: no soft step from charged decay to a singlet gap. Theorem 3.1
is as the file states (step 2 above). Row 1070 section 1 says the theorem
does not supply arbitrary pinned boundary conditions. Row 1074 section 2
proves `2 I3 < 2 < 23/10` by hand and scopes CA-FAIL to uniform strong
mixing of the full link specification. Rows 1061 L532 and 1062 L158-177
name the Verlindes and Aref'eva. The SA index rows for outline L588-599
say "Polynomial clustering does not establish a positive mass gap". The
file's own SA-source reads at the Mini scratch folder are not visible from
this laptop; the CA-I quote is checked in step 7.

**B1, the density (1), HOLDS.** With all longitudinal links 1, the mixed
plaquette for the bond `u -> v` and the edge `e = (x -> y)` is
`1 . Phi_e(v) . 1 . Phi_e(u)^{-1}`, so its term is `beta tau(Phi_e(v) Phi_e(u)^{-1})`.
`tau(a b^{-1}) = a . b` for unit quaternions as four-vectors. `|E_T| = 2T^2`,
`|P_T| = T^2`; distinct edges hold already for `T >= 2`, so `T >= 3` is a
safe restriction. Notation remark (no change of content): the word in
`W_T` needs the labels `e_1 = (x, x+1)`, `e_2 = (x+1, x+1+2)`,
`e_3 = (x+2, x+1+2)`, `e_4 = (x, x+2)` for the square based at `x`; with
them the word is the holonomy based at `x`, as l.163-164 uses.

**B2, residual group (2) and its kernel, HOLDS.** Gauge action on a
transverse link of plane `u`: `Phi_e(u) -> g_{(u,s(e))} Phi_e(u) g_{(u,t(e))}^{-1}`.
Longitudinal links stay 1 iff `g` is constant along each longitudinal edge,
so on a connected plane iff `g` does not depend on `u`. Kernel: trivial
action at `Phi_e = 1` gives `g_{s(e)} = g_{t(e)}`; the transverse torus is
connected, so `g` is constant `h`; `h Phi h^{-1} = Phi` for all `Phi` gives
`h = +-1`. Checked.

**B3, the reduction, HOLDS.** FACE-LIM's comb tree lies in one plane
`{x} x D` and uses no transverse link (row 1062 C1: the trees of different
`x` are disjoint, so their union is a forest). Hence the change of
variables, the independent laws `~ e^{beta_L tau(h)}`, their limit
`delta_1`, and the convergence of numerator and denominator (row 1061's
written normalization) do not see the transverse boundary condition. The
transverse squares become `W_T`. Invariance of `W_T` under `G_T` at each
fixed `u` follows by conjugation at the base vertex. The path-independence
sentence for the infinite plane is the standard flat-connection fact on a
simply connected plane. This step adds nothing uniform in `beta_L`, as
the file says.

**B4, order of limits, HOLDS.** Correct caution: a periodic longitudinal
Wilson face keeps commuting flat holonomies (row 1062 C1), and the
periodic spin model (1) is its trivial-holonomy sector.

**B5, anchor symmetry, HOLDS.** At `lambda = 0`, (1) factorizes over `e`
into O(4) sheets (ANCH); each has `K_L x K_R` up to `{+-1}`.

**C1, reflection positivity, HOLDS.** `(s . s')^n = <s^{(x)n}, s'^{(x)n}>`, so
each term of (3) is a positive semidefinite kernel; Schur products of such
kernels are positive semidefinite; the series converges uniformly on the
compact spheres. The reflection acts only on the longitudinal coordinate
and keeps the edge label `e`. `W_T` sits at one site and the bond term is
symmetric in `(u, v)`. So the weight of the reflected half is the
reflected weight. Site seam: the seam's on-site factors and its internal
bonds depend on seam spins only and are positive; given the seam, the two
halves are independent mirror copies, which gives `|integral|^2`. This is
the argument of OpenAI section 3.12.2 (step 2 above), with the positive
one-site factor kept.

**C2, transfer kernel (4), HOLDS.** `Tr K_lambda^M` is the partition
function of the `L x M` spin torus (each slice's spatial bonds and on-site
terms are split in halves). The middle factor is positive semidefinite by
(3); `K = M_A B M_A` with a positive multiplication operator `M_A`, so
`K >= 0`. A continuous kernel on a compact space is Hilbert-Schmidt. A
strictly positive kernel gives a simple top eigenvalue with a strictly
positive eigenfunction (Jentzsch's theorem; the file's Rayleigh-quotient
sketch is the standard proof). `G_T` acts by measure-preserving maps that
fix the kernel, so `U_g psi_0 = chi(g) psi_0`; `U_g psi_0 > 0` forces
`chi(g) = 1`. Singlet gap `>=` full gap, since the singlet complement of
`psi_0` is a subspace of the full complement. Checked.

### Step 4 result: section 3.1, the Ward port (5)-(8) (D1-D4), against OpenAI (3.4)-(3.8)

Each line was redone by hand with quaternion algebra: for imaginary
`a, s`, `a s = -a.s + a x s`.

**D1, the variation (5), HOLDS.** Under a transformation `g(u)` at `x`:
an outgoing link goes to `g Phi`, an incoming one to `Phi g^{-1}`, so its
inverse goes to `g Phi^{-1}`. All four `q_j` go to `g q_j`. Inversion keeps
the bond scalar: `tau(Phi(v)^{-1} Phi(u)) = tau(Phi(u) Phi(v)^{-1}) = tau(Phi(v) Phi(u)^{-1})`,
since `tau(g^{-1}) = tau(g)` on SU(2). Haar measure is inversion invariant.
At each fixed `u` the move is an element of `G_T`, so `W_T(Phi(u))` does
not change. For `X = t + s`:
`d/dt Re(e^{t a f_v} X e^{-t a f_u})|_0 = f_v Re(aX) - f_u Re(Xa) = -(a.s)(f_v - f_u)`,
and the second derivative is `-t (f_v - f_u)^2`, because `Re(a X a) = -t`.
With `A = -(complete exponent of (1))` this is (5). The file's sentence
"Set A = -S for the complete action exponent in (1)" means S is the
exponent and A = -S, which is OpenAI's convention `A = - sum w_e t_e`
(p. 13) with the on-site term added; the later use `D_eta(H e^{-A})`
agrees. OpenAI's local class (p. 13) is exactly the frame used: pinned
square `Q(S)`, signed `|b_e| <= b`, half weights on tangent boundary
edges, here with twist `U_e = 1` and `b = beta`. Generator convention: the
file's `e^{ta} = cos t + a sin t` is OpenAI's; row 1053 (L226) uses
`cos(t/2) + ...`, so the file's angle is half of row 1053's. Checked.

**D2, the bracket identity (6), HOLDS.**
`d/dt (e^{t eta_v} X e^{-t eta_u})|_0 = t(eta_v - eta_u) + eta_v s - s eta_u`, and
`eta_v s - s eta_u = -(eta_v - eta_u).s + (eta_v + eta_u) x s`. Its imaginary part
is (6), which is OpenAI (3.7) word for word. OpenAI (source L70-71) names
this "noncommuting current term" as the one that fixes the stiffness gain;
the file's statement that it is the first noncommutative term of the
calculation is right for section 3.1. For U(1) the term is absent. Checked.

**D3, the Ward identity (7), HOLDS.** The moves are left translations of
outgoing links and right translations of incoming links, so they keep
product Haar measure; with `eta = 0` on the pinned boundary they keep the
pins. `D_eta A = J(d eta)` with `(d eta)_b = eta_v - eta_u`, from
`D_eta t = -(eta_v - eta_u).s`. Integration by parts on the compact group
gives `E D_eta H = E[H J(d eta)]`, and `H = 1` gives `E J(d eta) = 0`. With
`H = J(F)`: `D_eta J(F) = sum w t (d eta)_b.F_b + sum w ((eta_v + eta_u) x s).F_b`,
and `(A x s).F = s.(F x A)`, so the second sum is `J(F_b x (eta_v + eta_u))`.
This is (7). With `J = S X_Q` and `d eta = S^{-1} d_S eta` it is OpenAI (3.8)
(p. 14) for real data, summed over the four incident sheets. Checked.

**D4, the stiffness bound (8), HOLDS.** For constant `F`, `S^{-1} J(F)` is
OpenAI's `X_Q(F)` summed over the four sheets, so `H_x` is (3.4) on the
face. Dropping the variance and using `|t| <= 1`, OpenAI's count gives, per
sheet and per direction, a coefficient sum at most `beta (S(S-1) + 2 (S/2)) = beta S^2`.
Four sheets give `H_x <= 4 beta |F|^2`. This uses no lower bound and no
property of the law, so it is uniform in `T`, `lambda` and the pins.
Scope as stated: the analogue of (3.5), not a gap; the stiffness
iteration of OpenAI sections 3.2-3.8 is not ported.

Verdict on the requested port: (5)-(8) is a correct port of OpenAI
(3.4)-(3.8) to the face law with the plaquette potential kept. It is the
`G_T`-local (gauge-direction) rotation, not a rotation of one sheet.

### Step 5 result: sections 3.2-3.3, the failures (9)-(10) and (11)-(12) (E1, E2, F1, F2)

**E1, the independent-sheet failure (9), HOLDS.** For `T >= 3` the edge `e`
lies in exactly two transverse squares. With all other links 1 and
`Phi_e(u) = e^{t a f_u}`, each square word is `e^{+-t a f_u}`, of trace scalar
`cos(t f_u)`. The exponent loses `2 lambda (1 - cos(t f_u))` per site, so `A`
gains it. The bond part is `-beta cos(t (f_v - f_u))` per bond. At `t = 0`
the second derivative is `beta sum (f_v - f_u)^2 + 2 lambda sum f_u^2`.
OpenAI (3.6), p. 13, has no such on-site term, and (3.4)-(3.5) involve no
rotation, so (3.6) is the first equation of section 3.1 whose sheet-wise
analogue fails. One configuration (all links 1) suffices to refute an
identity. The constant-profile remark is right. The file scopes it
correctly: not a counterexample to the face gap.

**E2, the gauge-direction inequality (10) is false, HOLDS.**
`f = tau(Phi_p(u))` is invariant under every transformation at every
`(u, x)`, so its derivatives along these directions vanish, and so do
those along their brackets (the generators form a Lie algebra). `f` is
continuous with range `[-1, 1]`; under a law with a positive continuous
density, `{f > 1/2}` and `{f < -1/2}` both have positive probability, so
`Var f > 0`. Hence (10) fails for every finite `C`. The scope sentence
(other directions or invariant dynamics not excluded) is right.

**F1, the section 3.11.3 quote and the extra factor, HOLDS.** The sentence
after the a priori law on p. 31 is "Conditional on alpha, the two circle
sectors are independent XY models", with pair couplings `J^1_e`, `J^2_e`
on lattice edges. In the face law the factor `e^{lambda tau(Phi_p)}` at
each site couples four sheets, and quaternion products also mix the two
circle sectors of each factor. For four links in one circle,
`e^{i theta_1} e^{i theta_2} e^{-i theta_3} e^{-i theta_4}` has trace scalar
`cos(theta_1 + theta_2 - theta_3 - theta_4)`. So the conditional law is not
a product of pair-XY laws. Checked.

**F2, the sign obstruction (11)-(12), HOLDS.** (a) Haar on `S^3` is
invariant under each coordinate reflection, so given the four magnitudes
the four coordinate signs are independent fair signs. With
`q = (cos alpha z, sin alpha w)`, `z = (tau^1 cos gamma, tau^2 sin gamma)` and
`alpha, gamma` in `[0, pi/2]`, the coordinate signs of `q` are exactly the
paper's `tau`'s. (b) The word is multilinear in its four quaternions
(inversion is conjugation, which is linear). For opposite edges, write
the word as `Phi_e^{+-1} X Phi_f^{+-1} Y`. The coefficient of
`x_0^e x_0^f` is `tau(XY)`; inversion does not change real parts. So
`c = tau(XY) |x_0^e| |x_0^f|`. With `{X, Y} = {1, -1}` up to inversion,
`tau(XY) = -1`. (c) For `T >= 3` (so also for the file's `T >= 4`) no other
square contains both `e` and `f`; the other square through `e`, the other
square through `f`, and the mixed bonds are each linear in `sigma` or in
`sigma'`. This gives (11). (d) `c < 0` on a neighbourhood of
`X = 1, Y = -1, |x_0^e| = |x_0^f| = 1` by continuity; that neighbourhood
has positive Haar measure. (e) The four-term sum gives
`log[w(+,+) w(-,-) / (w(+,-) w(-,+))] = 4 lambda c`, which is (12). (f) For a
strictly positive law on `{+-1}^n`, the FKG lattice condition holds iff it
holds on every two-coordinate slice. So it fails here. Reversing the
order of one sign does not help: at `X = Y = 1` the same coefficient is
`+|x_0^e||x_0^f| > 0`, also on a positive-measure set. (g) Conditioning a
ferromagnetic Ising law gives a ferromagnetic Ising law with fields, so
the negative coefficient cannot arise that way. The use of the lattice
condition is in OpenAI section 3.11.1 (p. 29: "The spin law itself is
associated by its elementary log lattice condition") and section 3.11.2
(p. 30: "the two sign species are independent ferromagnetic Ising
systems"), which section 3.11.3 uses. The link to row 1053 section 6.5
(L279, "not a ferromagnetic pair interaction in the embedded Ising
variables ... ARGUED") is right; (12) proves it for this decomposition.

Scope of F2 as written: it refutes the literal conditional-ferromagnet
step of OpenAI's all-observable conversion on the face, for every
`lambda > 0`. It does not refute all-observable mixing, nor every
correlation inequality; the file says so (l.408-409).

### Step 6 result: sections 4.1-4.2, (13)-(16) (G1-G5), and judgement O7

**G1, the anchor gap uniform in T, HOLDS given OpenAI's Theorem 3.1.**
Theorem 3.1 covers every unpinned rectangular torus with both sides at
least `C Xi(beta)`, so `L x M` with `L >= ceil(C Xi)` and `M -> infinity`
is allowed. For slice functions at times `0` and `n` the max-norm
distance of the supports is `n` (for `n <= M/2`), and (3.2) gives
`C (1 + beta + 2L + n)^20 L_F L_G e^{-c n / Xi}`. For fixed `L` the torus
expectations converge to the cylinder vacuum (compact positive kernel,
simple top eigenvalue). The normalized transfer operator is positive
(C2), so `<v, (T^n - P_0) v> = integral kappa^n d mu_v` with `mu_v` on
`[0, 1)`; mass on `[r, 1)` with `r > e^{-a}` would give a lower bound
`r^n mu_v([r,1))`, against the bound. `psi_0` is continuous and bounded
below, so `{F psi_0}` is dense; projections of a dense set onto
`psi_0^perp` are dense there, and bounded spectral projections vanish on
all of `psi_0^perp`. This is OpenAI's section 3.12.2 corollary argument
(p. 33) at fixed `L`. At `lambda = 0`, `K_0` is the tensor product of
`2T^2` sheet operators; product eigenvectors form a basis, and every
basis vector orthogonal to the vacuum has a factor at most `e^{-a}`. So
the full gap is at least `a(beta)` for all `T`, with `a_* = c/Xi(13/5)` on
the window (Xi is increasing). Checked.

**G2, (13)-(15), HOLDS.** `A_lambda = A_0 + lambda V` and multiplication
operators commute, so `K_lambda = M K_0 M`. With `A = M K_0^{1/2}`,
`B = K_0^{1/2} M`, `AB` and `BA` have the same nonzero eigenvalues with
multiplicity. `e^{-lambda N} <= M^2 <= e^{lambda N}` gives the form
inequalities; min-max gives (14); `M` and `K_0^{1/2}` commute with `G_T`,
so (14) also holds in the singlet space. Dividing gives
`m >= a - 2 lambda L T^2`, and (15). The intersection of the intervals
`[0, a/(4 L T^2)]` over `L >= L_0`, `T >= 3` is `{0}`. Checked.

**G3, the decision, HOLDS.** "OPEN: a positive T-uniform interval" and
"FAILS as a justification: perturbation by the full norm" are both right.
The phrase "`beta_T Xi(beta)^2 <= eps`" is the region `R_eps` of row 1066
(`gap-aniso-trajectory.md` L77, with `X = Xi`), whose seed (S) row 1066
leaves OPEN (L82); row 1070's RESULT keeps V2 OPEN. So "Rows 1066-1070
already leave the corresponding seed open" is right.

**G4, the Ising example (16), HOLDS.** At `lambda = 0`: all plus has energy
0; all minus has 1 (pin); a mixed configuration has at least two walls,
so at least 1. Gap 1 for every `N >= 3`. At `lambda = 1/N`: all plus and
all minus are both 0; a mixed configuration has at least `1 - (N-1)/N`.
Each term `-lambda 1_{s_i = -1}` has norm `lambda`. Checked.

**G5, what a positive interval would need, HOLDS AFTER CORRECTION
(wording only).** The sentence "A transverse plaquette insertion leaves
that class, as (9) and (12) show" credits (9) and (12) with a fact that
follows from the form of the term. **Corrected text:** "A transverse
plaquette insertion is a four-sheet on-site term, not a weakening of pair
couplings, so the perturbed law is outside the class of Theorem 3.1;
(9) and (12) show that two steps of its proof do not carry over to that
law." No conclusion changes. The rest of G5 is right and scoped.

**Judgement O7: is the size-uniform interval really only `beta_T = 0`?**

(a) *As a statement about (15): yes, exactly.* The file says the
interval *established* uniformly in size is `{0}` and that no negative
claim about a positive interval is proved. Both are right.

(b) *A sharper use of (15) cannot do better.* The proof of (14)-(15) uses
only three inputs: `K_0 >= 0`, the gap `a` of `K_0`, and the oscillation of
`V` (here `osc V <= 2N`). In that form it reads `m_lambda >= a - lambda osc(V)`.
This bound is attained. Write the file's own (16) as a transfer operator:
`K_0 = e^{-H_0}` (diagonal, positive), `V = sum_i 1_{s_i = -1}`
(`osc V = N`), `K_lambda = M K_0 M = e^{-H_lambda}`. For `0 <= lambda <= 1/N`
the ground state is all plus, the first excited level is all minus at
`1 - lambda N` (a mixed state with `k <= N-1` minus spins is at least
`1 - lambda k`), so the gap is exactly `1 - lambda N = a - lambda osc(V)`. So
within the inputs that (14) uses, the interval of order `a / N` is optimal,
with constant 1. Any size-uniform interval must use structure that (14)
does not see: the product form of `K_0` over sheets, locality of `V`, and
decay of the sheets' correlations. This confirms the step-6 sentence "no
amount of reusing (15) changes its shrinking interval", with a sharper
reason than the file gives.

(c) *The unpinned Lipschitz decay, as stated, gives no positive interval
by any step written in the file or found by me.* Theorem 3.1 bounds
two-point covariances, for O(4) laws with pair couplings
`0 <= beta_e <= beta`, at `lambda = 0` only. The two standard routes need
more. Interpolation in `lambda` needs, for the perturbed law,
`sum_{r,p} |kappa_3(F, G, tau_p(r))|` bounded uniformly in `L, T`; Theorem
3.1 says nothing about `lambda > 0` or about third cumulants. A convergent
expansion around the product of sheets needs tree-type decay of truncated
multi-point functions of each sheet; Theorem 3.1 gives two-point
covariances with a support-size factor `(1 + |A| + |A'| + d)^20`. This is a
bounded search, not a proof that no argument exists. The file's
conclusion (OPEN, needs a local stability theorem or a new estimate) is
the right reading.

### Step 7 result: sections 5.1-5.5 (H1-H4, I1-I4), the next decision (J1), and judgement O8

SA sources fetched for H4 into the new empty folder
`/tmp/opus-face2d-sa.ETN6fw`, from `ethanwsussman/Yang--Mills-LLM-experiment`
at `31a47c543775`: `theorem_0_complete_account_raw_I.tex` (166,711 lines)
and `YM4_sketch_500.tex` (32,992 lines). Only the cited lines were read.

**H1, statement (17), HOLDS** as a definition. Quantifying over every
periodic local limit, uniformly in `T`, `lambda`, state and translations,
is the right local covariance form of (FACE-SG-T).

**H2, the finite-cylinder gap is a sufficient input, HOLDS.** The slab
insertion operator has kernel `int F prod K`, bounded pointwise by
`||F||_inf K^r` because `K >= 0` pointwise; with `||T|| = 1` its norm is at
most `||F||_inf`. For `G_T`-invariant `F, H` the vectors `O_H psi_0` and
`O_F^* psi_0` lie in the singlet space, so
`|Cov| <= ||F|| ||H|| e^{-m (n - r_F)}`, inside the file's constant
`4 ||F|| ||H|| e^{m (r_F + r_H)}`. The time wrap-around terms vanish in the
local limit. The converse is not claimed. Checked.

**H3, the forward implication to `T = infinity`, HOLDS.** Local
convergence along a subsequence exists by compactness and diagonal
selection; (17) passes at each fixed `n`. Reflection positivity and time
translation invariance pass to local limits, so the OS construction of
OpenAI section 3.12.2 applies to the invariant local algebra, and (17) for
the pair `(Theta F, F)` gives the spectral inclusion on a dense set, hence
on the vacuum complement. "No converse" keeps row 1074 section 8's BR-7
correction, which I read (L61-67). Checked.

**H4, what (17) does not give, HOLDS.** Each negative is scoped to "by the
argument given" or "not proved here". The CA-I quote is right: the "Not
asserted" list of the complete account I starts at L2705 and includes "a
mass gap" at L2708, inside the cited L2706-2712. The outline at L588-595
says "A polynomial cluster estimate likewise gives no positive mass gap."
Both are correctly credited to Sussman and Alpoge.

**I1, compact U(1), HOLDS AFTER CORRECTION (one sentence).** (18) is right:
with `P = theta_1 + theta_2 - theta_3 - theta_4`, a rotation of one sheet
multiplies `e^{i(P(0)+P(n))}` by `e^{2 i alpha}`, so that term has mean 0;
`E e^{i(P(0)-P(n))} = prod_j E e^{+-i(theta_j(0) - theta_j(n))} = g(n)^4`,
real by the symmetry `theta -> -theta`; so `Cov = g(n)^4/2`. Frohlich and
Spencer (OpenAI's [18], verified in step 2) give a power-law lower bound
for `g` at sufficiently large stiffness. The citation of row 1062 J1
(L114) is exact. The last sentence (l.628-629) overstates: (17) is
stated on the window, and the file itself asserts no theorem-level
Frohlich-Spencer threshold there (l.624). **Corrected text:** "Any
group-blind argument that would prove (17) for compact U(1) at all
sufficiently large beta would contradict (18) with Frohlich and Spencer's
theorem. Inside the window this is a GUIDE-grade test, since no
theorem-level threshold there is asserted."

**I2, frozen Q_8 and 2T, HOLDS.** On a finite connected graph,
`sum tau(h_v h_u^{-1})` is maximal exactly at constant configurations,
since `tau(g) = 1` only at `g = 1`; so as `beta_M -> infinity` each sheet
becomes a uniform constant. `h_p` is uniform (one factor is uniform and
independent of the rest) and constant in `u`. Counts: Q_8 gives values 1
(twice) and 0 (six times), so the mean is 1/4 and the variance is
`1/4 - 1/16 = 3/16`. 2T adds sixteen elements with value 1/4: mean
`(2 + 4)/24 = 1/4`, second moment `(2 + 1)/24 = 1/8`, variance 1/16. The
scope sentence (no window, no pure state) is right.

**I3, Pin(2), HOLDS.** `j e^{i theta} j^{-1} = e^{-i theta}`; with Lemma EVEN
(row 1053 L289-290, checked by row 1062 C7), invariant functions restricted
to the identity component are even. GUIDE grade as labelled.

**I4, five-dimensional face, HOLDS.** `(Z/TZ)^3` has `3T^3` edges, `3T^3`
squares, six edges at a vertex. Six incident sheets give `H_x <= 6 beta I`;
`N = 3 L T^3` gives `m >= a - 6 lambda L T^3`. Opposite edges of a square
lie in no other common square for `T >= 3`. The reading is GUIDE grade and
scoped.

**J1, the next decision (l.717-722), HOLDS AFTER CORRECTION.** It is right
as far as it goes. Two precisions follow from G5 and from O7. First, G5
names two possible sources of a positive interval: a stability theorem
from the unpinned O(4) datum, or a new estimate for the perturbed law;
step 6 names only the first. Second, by O7(b) a stability theorem cannot
rest on the anchor gap and the size of the perturbation alone, and by
O7(c) Theorem 3.1's two-point bound is not, by any step written, enough
either. **Corrected text:** "The next scientific decision is whether the
face law obeys (17) on some `[0, eps_beta]`, `eps_beta > 0`, with
constants independent of `L`, `T` and the state. It could be decided by a
local stability theorem for the transverse plaquette perturbation whose
hypotheses are proved from unpinned O(4) estimates (Theorem 3.1's
two-point bound, and the multi-point decay that the standard routes also
need), or by a new estimate for the perturbed law. The present argument
neither supplies nor refutes either. No reuse of (15) helps: its
comparison is sharp at order `a/(L T^2)` for the inputs it uses."

**Judgement O8.** The decision, corrected as above, is correctly stated.
Strength: it is the `lambda <= eps_beta` part of (FACE-SG-T), so it is
weaker than (FACE-SG-T) on `[0, beta]`. It is not shown weaker than the
four-dimensional target: the face sits at `beta_L = infinity`, and neither
implication between (17) and the isotropic gap is proved (H4). It is the
first segment of leg (i) of BR-2 only; legs (i) on `[eps_beta, beta]`
and (ii) (descent in `beta_L`) stay open.

Not checked here: the file's "Repo search" provenance table (main-branch
and `S/` files). It is not in row 1078's list and carries no mathematics.

### Step 8 result: verdict table, corrections, provenance, RESULT

#### 8.1 Verdicts (line numbers are those of `gap-face-2d-astra.md` at `efd25f938`)

| Item | Lines | Verdict | Note |
|---|---|---|---|
| A1 premises and attributions | 63-100 | HOLDS | rows 1053, 1061, 1062, 1070, 1074 and Theorem 3.1 as stated |
| B1 face density (1) | 106-132 | HOLDS | edge labels of the square word are implicit (step 3) |
| B2 residual group (2), kernel `{+-1}` | 134-147 | HOLDS | |
| B3 reduction on the transverse torus | 149-169 | HOLDS | FACE-LIM's forest uses no transverse link |
| B4 order of limits | 171-175 | HOLDS | |
| B5 anchor symmetry | 177-181 | HOLDS | |
| C1 reflection positivity (3) | 183-203 | HOLDS | OpenAI 3.12.2 with the on-site factor kept |
| C2 transfer kernel (4) | 205-225 | HOLDS | Jentzsch; singlet gap at least full gap |
| D1 variation (5) | 237-264 | HOLDS | = OpenAI (3.6) summed over four sheets |
| D2 bracket identity (6) | 266-277 | HOLDS | = OpenAI (3.7) |
| D3 Ward identity (7) | 279-295 | HOLDS | = OpenAI (3.8) after `J = S X_Q` |
| D4 stiffness bound (8) | 297-316 | HOLDS | OpenAI's count `S(S-1) + S = S^2` |
| E1 independent-sheet failure (9) | 318-339 | HOLDS | first failing equation (3.6), p. 13 |
| E2 inequality (10) false | 341-356 | HOLDS | "Restricting to G_T" (l.341) means `G_T`-valued at each fixed `u`, as in 3.1 |
| F1 section 3.11.3 quote | 360-368 | HOLDS | quote exact, p. 31 |
| F2 sign obstruction (11)-(12) | 370-409 | HOLDS | also robust to reversing one sign's order |
| G1 anchor gap uniform in T | 417-454 | HOLDS given Theorem 3.1 | |
| G2 (13)-(15) | 456-489 | HOLDS | |
| G3 decision | 491-499 | HOLDS | `R_eps` of row 1066 |
| G4 Ising example (16) | 501-521 | HOLDS | |
| G5 what a positive interval needs | 523-533 | HOLDS AFTER CORRECTION | wording, text in step 6 |
| H1 statement (17) | 539-557 | HOLDS | definition |
| H2 cylinder gap sufficient | 559-574 | HOLDS | |
| H3 forward implication | 576-591 | HOLDS | |
| H4 what (17) does not give | 593-602 | HOLDS | the CA-I list starts at L2705; "a mass gap" is L2708 |
| I1 compact U(1) (18) | 604-629 | HOLDS AFTER CORRECTION | last sentence, text in step 7 |
| I2 frozen Q_8, 2T | 631-659 | HOLDS | 3/16 and 1/16 |
| I3 Pin(2) | 661-672 | HOLDS | GUIDE grade |
| I4 five-dimensional face | 674-690 | HOLDS | |
| J1 next decision | 717-722 | HOLDS AFTER CORRECTION | text in step 7 |

Count: 30 items; 27 HOLD, 3 HOLD AFTER CORRECTION, none FAILS. The
file's RESULT line (l.724) agrees with these verdicts.

#### 8.2 Corrections (exact replacement text, also given above)

1. G5, l.524-525: "A transverse plaquette insertion is a four-sheet
   on-site term, not a weakening of pair couplings, so the perturbed law is
   outside the class of Theorem 3.1; (9) and (12) show that two steps of
   its proof do not carry over to that law."
2. I1, l.628-629: "Any group-blind argument that would prove (17) for
   compact U(1) at all sufficiently large beta would contradict (18) with
   Frohlich and Spencer's theorem. Inside the window this is a GUIDE-grade
   test, since no theorem-level threshold there is asserted."
3. J1, l.717-722: the corrected next decision of step 7.

#### 8.3 The two judgements

- **O7.** The size-uniform interval *established* is exactly `{0}`, and
  that is all the file claims. A sharper use of (15) cannot help: the
  comparison behind (14) reads `m_lambda >= a - lambda osc(V)` and uses only
  positivity, the anchor gap and `osc(V)`; the file's own (16), written as
  `K_0 = e^{-H_0}`, `V = sum 1_{s_i = -1}`, attains it with equality
  (gap `1 - lambda N` on `[0, 1/N]`). The unpinned Lipschitz decay of
  Theorem 3.1 is a two-point bound at `lambda = 0` for pair couplings; the
  interpolation route and the expansion route both need estimates it does
  not state (third cumulants of the perturbed law; tree-type multi-point
  decay of the sheets). I found no step from it to a positive interval;
  this is a bounded search, and the question stays OPEN, as the file says.
- **O8.** The next decision, corrected, is correctly stated. It is the
  `lambda <= eps_beta` part of (FACE-SG-T), hence weaker than (FACE-SG-T).
  It is not shown weaker or stronger than the four-dimensional target.

#### 8.4 Provenance and limits of this check

- Writer of the checked file: OpenAI Codex, gpt-6-astra max (row 1077).
  Checker: Claude Opus 5.5 (Anthropic), max effort. Different provider.
  Every algebraic and operator step was redone by hand here; that is a
  separate derivation, not a re-run of the writer's.
- Primary sources read: OpenAI's paper at `4eaee875` (LaTeX source and
  PDF; Theorem 3.1, section 3.1, sections 3.11-3.12, reference [18]); SA
  complete account I L2697-2713 and outline L586-600 at `31a47c543775`;
  lane rows 1053, 1061, 1062, 1066, 1070, 1072, 1074 at the cited places.
- Cited, not checked: OpenAI's Theorem 3.1 and Frohlich-Spencer's theorem
  (inputs labelled GIVEN by the file). Not checked: the file's "Repo
  search" table and its Mini scratch folders.
- No numerical run and no computer-assisted step. The checked arguments
  are finite-dimensional integration by parts, quaternion algebra,
  positive kernels, min-max and the spectral theorem: formalizable in
  principle; nothing was formalized in Lean. Jentzsch's theorem and the OS
  construction are standard but would need to be supplied.
- Files written: this file only. Downloads stay in
  `/tmp/opus-face2d-openai.NylL2Z` and `/tmp/opus-face2d-sa.ETN6fw`; none
  is committed.

Credit: OpenAI for the O(4) argument and its Ward identity; Jurg Frohlich
and Thomas Spencer for the two-dimensional XY lower bound; Frohlich, Simon
and Spencer for the infrared bound used in row 1074; Ethan Sussman and
Levent Alpoge for the account whose disclaimer is cited; Tadeusz Balaban
for the ultraviolet construction behind that account. This is a research
check, not an audit; no mass gap is claimed.

RESULT: row 1077 (gap-face-2d-astra.md) checked line by line by Claude Opus 5.5 max, cross-provider: 30 items, 27 HOLD, 3 HOLD AFTER CORRECTION (G5 wording, I1's last sentence on U(1) at the window, J1's next decision), none FAILS; the Ward port (5)-(8) matches OpenAI (3.4)-(3.8), and (9) at (3.6) and (12) at section 3.11.3 are valid first failures; the size-uniform interval of (15) is exactly {0}, and its comparison is sharp (the file's Ising example (16), read as a transfer operator, attains m = a - lambda osc V), so a positive interval needs sheet decay beyond Theorem 3.1's two-point bound and stays OPEN; the corrected next decision is weaker than FACE-SG-T and not shown comparable with the four-dimensional target; no mass gap claimed.
