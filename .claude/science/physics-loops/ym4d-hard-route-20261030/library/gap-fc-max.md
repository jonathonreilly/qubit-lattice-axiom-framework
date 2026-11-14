lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T20:51Z

# gap-fc-max (row 947): the Fisher-information contraction (FC)_theta on the seed box

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, pinned at commit f1c3de09b, started 2026-11-14T08:51Z.
Author item. Not checked by another model (check = row 949). Research-stage working state; nothing here is a public claim.
No subagents. No computer-assisted step: any run is labelled GUIDE and can only refute or guide.

Credit. The seed, the slice chain and the hypercontractivity route come from this repository's rows 931-946 (Claude and Codex).
The transfer-matrix and vacuum-slice setting builds on Ethan Sussman and Levent Alpoge's complete account
(CA-I/II/III at commit 31a47c543775, text by them with Claude and Codex) and on Balaban's and Dimock's papers; each use is cited where it occurs.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read row 941 (`library/gap-lsivac-max.md`) in full. Record (A3), (FC)_theta, (GC)_theta, Theorem C0, and the rate Proposition HC needs.
2. Read row 946 (`library/gap-fctest-opus.md`) and check 943. Decide the branch: (FC) refuted at beta 2.3 (then: corrected Dirichlet form) or not (then: attack (FC)).
3. Duplicate check (rule 0a): grep `library/open-core.md`, `library/l17c.md` and the FINISH rows for (FC)/(GC). Outline lookup in the Sussman-Alpoge index.
4. State (FC)_theta with the explicit seed-sized rate (lead note (a)). Fact tests on the statement: U(1) fails THAT rate; SMALL-BOX; frozen groups.
5. Attack the linearisation (GC)_theta: P grad^* grad P at most theta grad^* grad on L^2(nu). One approach per response.
6. Attack (FC)_theta itself, or lift (GC) to (FC).
7. If it does not close: the smallest unproved inequality, and one test that could refute it.
8. Final summary and the RESULT line.

## Status log

- 08:51Z file created. Nothing proved yet.
- 09:20Z Steps 1-3 written below. Branch decision: row 946 did NOT refute (FC); so (FC) is attacked.

## Steps 1-3: inputs read, branch decision, duplicate check (READ; no new claim)

**Read at f1c3de09b.** FINISH.md (opening, How we work, Joining, Working efficiently, Rules, rows 941, 943, 946-951),
GOAL.md, `library/gap-lsivac-max.md` (row 941) in full, `library/gap-fctest-opus.md` (row 946) in full,
`library/gap-lsivac-check-astra.md` (check 943: findings, seed and fact tests, test proposal, locality),
`library/gap-direction-max.md` 300-365 (row 931: Proposition HC, Theorem E, the (E-to-HC) stop).

**Objects (row 941, quoted in short).** B a periodic spatial box, L = 3|B| links, M = (S^3)^L inside R^N, N = 4L.
V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2). Omega its top eigenfunction,
lambda_0 its eigenvalue, nu = Omega^2 dx. m(dw) := e^(-V(w)/2) Omega(w) dw. One-step law
pi_x(dw) = e^(beta <x, w>) m(dw)/(lambda_0 e^(V(x)/2) Omega(x)); P f(x) = E_(pi_x) f; P is self-adjoint on L^2(nu).
(A3): z . grad(P f)(x) = beta Cov_(pi_x)(<z, w>, f). I(g) := E_nu[|grad g|^2/g].
(FC)_theta: I(P g) <= theta I(g). (GC)_theta: E_nu|grad P f|^2 <= theta E_nu|grad f|^2.
(C1-av)_(alpha_c): Ent_nu(g) - Ent_nu(P g) <= I(g)/(2 alpha_c). Theorem C0: (FC) + (C1-av) give (LSI-vac) with alpha_c (1 - theta).
(HC-vac)_alpha (row 931, line 306): ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha m), every integer m >= 0, norms in L^p(nu).
Proposition HC (row 931; HOLDS in check 938): (HC-vac)_alpha gives X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m).
Seed: X(a; (24a)^3) <= x_* once alpha (a - 2) >= C_beta(x_*) + 3 log a, C_beta(x_*) := log(72 beta 24^3/x_*), a even.

**Branch decision.** Row 946 (GUIDE, Claude Opus 5.5, unchecked): no f with R(f) >= 1; every measured
R(f) = E|grad P f|^2/E|grad f|^2 is below 0.23 at beta 2.3 and 2.6 on boxes of side 4 and 6. So (FC) is not refuted
and this row attacks (FC). On lead note (b): row 946 did not use a periodic finite cylinder. It used OPEN time
{0..2K}, K = 6 and 8, with the middle slice frozen and the two halves independent (its (E1)-(E4)). The laws it
samples are nu_K ~ (T^K b)^2 and pi_x^(K) ~ T_0(x, w)(T^(K-1) b)(w), b = e^(-V/2). So there is no extra backward
factor T^N(x, x); the difference from (nu, pi_x) is the open-boundary error, of order e^(-E' K), not quantified
there, with stability shown only for K = 6 -> 8. Its numbers are GUIDE on (nu_K, pi_x^(K)) for boxes of side 4 and
6, not on the vacuum pair of the seed box.

**Duplicate check (rule 0a).** `grep -n -i -E "\(FC\)|\(GC\)|fisher|entropy contraction|data.processing|SDPI|polchinski|de bruijn|hypercontract|log-sobolev|LSI"`
on `library/open-core.md`, `library/l17c.md`, `library/open-registry.md`: no hit. FINISH rows naming (FC)/(GC): 941
(states them), 943 (check), 946 and 948 (GUIDE test and its check), 947 (this row), 949 (its check), 950 and 951
((SC), the other input: worker 1; I do not attack (SC)). Entropy contraction is row 931's Theorem E (given
(LSI-vac), (SG-step)); (E-to-HC) is row 940. No row owns (FC) or (GC) beside this one. I proceed.
For the bridge interpolation of Step 5 below: `grep -n -i -E "polchinski|de bruijn|heat flow|interpolat|brownian"` on
rows 931, 940, 944, 950 and `prior/gap-lit-hcvac.md`: no use of it (one remark on Brownian motion in row 950, line 208).

**Sussman-Alpoge account.** Rows 938-941 and 946 record that `library/sa-index/` has no log-Sobolev, hypercontractive or
Fisher-information statement; I did not repeat those greps. Their account enters through the transfer frame
(outline (GL8), located by checks 927, 933, 938). Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text.

## Step 4: (FC) with the rate the seed needs, and its fact tests (09:35Z)

**4.1 The statement (substitution in the arrows of row 941 Step 6; check 943 wrote the same line).**
Put K_a := (C_beta(x_*) + 3 log a)/(a - 2) for even a >= 4. The route (FC) + (C1-av) -> (LSI-vac) -> (HC-vac) -> seed
needs, on the one box B = (24a)^3:

  (FC-seed)_a:  (FC)_theta, (C1-av)_(alpha_c), (COV)_kbar hold on B with  alpha_c (1 - theta) >= beta^2 kbar (e^(2 K_a) - 1).

Equivalently theta <= theta_seed(a) := 1 - (beta^2 kbar/alpha_c)(e^(2 K_a) - 1). "theta < 1" alone gives nothing.
Sizes (hand arithmetic, C_beta = 16 at beta 2.3): K_30 = (16 + 10.21)/28 = 0.936, K_40 = (16 + 11.07)/38 = 0.712,
K_60 = (16 + 12.29)/58 = 0.488. With kbar >= 1/4 (row 941 (A5)) the right side is at least 1.32 (e^(2 K_a) - 1) at
beta 2.3: 7.3, 4.2 and 2.2 for a = 30, 40, 60.

**4.2 Necessary side (PROVED, one line each).** (HC-vac)_alpha gives E_1(B) >= alpha (Proposition HC). So every route
to the seed through (HC-vac) needs E_1(B) >= K_a on B = (24a)^3. With the box side b = 24a:
  b E_1(B) >= 24 a K_a > 384 + 72 log a.
So the seed, on this route, is one inequality for the dimensionless gap b E_1 at ONE box side b.

**4.3 FT-U1 against THAT statement (PROVED given the mode list of FP, read by check 943 at `gap-seam-max.md:88-116`).**
In the photon sector of FP every constant is attained at the lowest mode: alpha_c = beta e^(omega_min),
kbar = 1/(beta e^(omega_min)), theta = e^(-2 omega_min). So beta^2 kbar/alpha_c = e^(-2 omega_min) and (FC-seed)_a reads
omega_min >= K_a. But omega_min = 2 asinh(sin(pi/(24a))) < pi/(12a) < 0.27/a, and K_a > 16/a. So FP fails (FC-seed)_a for
every a, by a factor above 59 (check 943's arithmetic). In the form of 4.2: FP has b omega_min < 2 pi at every box
side, against 384 + 72 log a. FP satisfies (FC)_theta with theta = e^(-2 omega_min) < 1 on every finite box, as the lead
note (a) says; it fails only the rate. Scope: FP is the Gaussian mode model of row 929, not compact Wilson U(1).

**4.4 SMALL-BOX and frozen groups.** Unchanged from row 941 with check 938's quantifiers. (FC-seed)_a contains a,
so a proof must use the box size. Frozen groups have no gradient form; (FC) is not defined for them.

**4.5 What (FC) is not (PROVED by row 941's own run plus one line).** (FC) and (GC) are sufficient conditions
only. Row 941 Run 4 has chains with a gap, hence hypercontractive on their finite state space, where (GC) is
false (double-well rotors, theta_GC = 9.5 and 1.06; GUIDE). So a failure of (FC) does not touch the seed. The
entropy form that IS necessary: for a self-adjoint Markov operator K on L^2(nu) with ||K f||_b <= ||f||_a, 1 < a < b,
  Ent_nu(K g) <= (a/b) Ent_nu(g)   for every density g.
Proof. Put u = K g, psi = log u, r = 1/a. Jensen: e^(r K psi) <= K e^(r psi). So E e^((b/a) K psi) <= E (K u^(1/a))^b
<= (E u)^(b/a) = 1. The entropy inequality E[g phi] <= Ent(g) + log E e^phi with phi = (b/a) K psi, and
E[g K psi] = E[u log u] = Ent(u), give the claim. QED
With (HC-vac)_alpha and its dual, K = P^(2m), a = 1 + e^(-2 alpha m), b = 1 + e^(2 alpha m), a/b = e^(-2 alpha m):
  (EC-nec):  (HC-vac)_alpha  implies  Ent_nu(P^(2m) g) <= e^(-2 alpha m) Ent_nu(g)  for every m >= 1.
So entropy contraction is necessary for the seed route, and Fisher-information contraction is not.
