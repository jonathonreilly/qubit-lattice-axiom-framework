lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T01:20Z

# Row 967, `gap-pca-opus`: plaquette cellular automata, PCA space-time Gibbs measures, and the gap crux

Started 2026-11-14T13:20Z on the Mac mini worker, at commit c8056a092 of `claude/ym4d-hard-route`.
Brainstorm-and-test item with literature. Owner's prompt (quoted in row 967): "i wonder if some wolfram style
approach to plaquetts could also be interesting here? cellular automata but with plaquetts? (left field brainstorm)".

Labels: PROVED (written argument, checkable by hand), CONDITIONAL (proved given a named input), GUIDE (a run; guides
or refutes only, never a step of the chain), ARGUED (heuristic, not a proof), OPEN.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Read the inputs: row 962 (`library/gap-constraints-max.md`: constraint audit, idea table, ceilings), row 941
   Step 1 (the slice chain), row 947 (Theorem BR, (LSI-J-seed)), and grep the lane's idea inventories for PCA,
   cellular automata, Domany-Kinzel, Toom, Gacs, disagreement percolation, Bianchi, Batrouni-Halpern, Creutz,
   overrelaxation, Q2R. Write the crux in one paragraph and the list of prior matches.
2. Framing (a), the smallest case by hand: when is a (d+1)-dimensional Gibbs measure the space-time history of a
   d-dimensional PCA (site-factorised local updates)? State the exact criterion (a two-layer interaction with no
   intra-layer coupling in the update direction, plus the normalisation condition sum_{eta'} prod p = 1 that the
   PCA picture forces), and test it on Wilson SU(2) (and a Z_2 / U(1) lattice gauge toy) along the straight time
   axis and along diagonal / light-cone time directions. Prove or refute on the smallest case.
3. Literature check by URL (PCA/Gibbs correspondence: Goldstein-Kuik-Lebowitz-Maes, Lebowitz-Maes-Speer;
   Domany-Kinzel; Dobrushin-type PCA criteria; van den Berg-Maes disagreement percolation; Toom; Gacs), into a
   /tmp scratch folder, with what each actually gives.
4. Framing (b): which PCA ergodicity tools survive the outcome of Step 2; supremum versus averaged versions;
   comparison with the ceilings 2/3, 0.775, 4 G_3 = 1.0109; fact tests (U(1) photon, frozen groups, SMALL-BOX).
5. Framing (c): plaquette-level constraint systems (Bianchi on cubes, Batrouni-Halpern field-strength formulation,
   centre-vortex Z_2 surfaces, Creutz demons, overrelaxation, Q2R-type reversible rules): new input or reframing.
6. Optional GUIDE run (only if a step produces a falsifiable numeric claim, under the numeric lock).
7. Ranked list of what, if anything, deserves a proof lane.
8. RESULT line.

## 1. Inputs and prior matches (Step 1, READ at c8056a092)

**Read.** FINISH opening sections (How we work, Working efficiently, Rules), GOAL.md, rows 941, 947, 962, 963, 967
(lines 1018, 1024, 1039, 1040, 1044); `library/gap-lsivac-max.md` Steps 0-1 (L28-150, the slice chain);
`library/gap-constraints-max.md` Sections 1, 4 (A6) and 8 (L37-84, L205-215, L467-540); RESULT parts of rows 774,
821, 853; `library/gap-skeleton-max-b.md` L215-220 (idea A12) and L581-584. Row 963's output
`library/gap-rotgeom-opus.md` is not on disk at this commit.

**The crux in one paragraph (READ; nothing here is new).** The finish line (SEED-FP) needs one thermal sum of the
bare Wilson SU(2) transfer operator T_B on one periodic box to be small. By Lemma SPLIT (row 892) the SH seed on the
slab (a; (24a)^3) holds if the glue half S_ev <= 1/10 and the flux half Q_0 <= 1/20. Row 941 (Step 1, (A1)-(A7)):
the vacuum slice chain P = Omega^(-1) (T/lambda_0) Omega on L^2(nu) has one-step law
pi_x(dw) = e^(beta <x, w>) m(dw)/(lambda_0 phi_0(x)), an exponential family; log Omega = -V/2 + Lambda(beta x) - const
with Lambda convex; the two-slice law is J(dx, dw) = e^(beta <x, w>) m(dx) m(dw)/lambda_0. Row 947: Theorem BR (one
step is an ambient Brownian bridge of duration 1/beta) and Corollary BR-J: a log-Sobolev constant alpha_J of J gives
(HC-vac) with alpha >= min(alpha_J/(2 beta), 1). The smallest unproved inequality is (LSI-J-seed)_a:
alpha_J >= 2 beta K_a, K_a = (C_beta + 3 log a)/(a - 2), on (24a)^3 for one even a >= 30. Row 954: this needs
m_G >= K_a. Row 962: no relaxation of geometry, boundary, time direction or representation is a NEW INPUT; the seed
number is fixed by the measure and the scale, and a NEW INPUT can only be an order-one inequality for that number
or a comparison node between two measures.

**Fact tests that bind every idea here (row 962 1.4, READ).** FT-U1 (free photon and compact U(1) Coulomb fail the
seed); FT-FROZEN (frozen Q_8, 2T fail); K7 (mixed-action endpoint with no seed); SMALL-BOX (a fixed small box at
large beta has no gap in units of its side); FT-CEIL (worst-case single-link 1/3, single-site Dobrushin 2/3, vertex
blocks 0.775, background-uniform layer bounds false above 4 G_3 = 1.0109).

**Prior matches (rule 0a; grep of FINISH.md, `library/*.md`, `library/prior/*.md` at c8056a092).**

| Term | Where in the lane | What it says | Bearing on this row |
|---|---|---|---|
| Dobrushin, disagreement percolation | rows 690, 820-821, 853; `gap-brainstorm-max.md` L148; `gap-ds-gauge.md` L17-38; `prior/gap-lit-dp.md`; `prior/gap-lit-annealed.md` | GUIDE row 820: the single-link chord influence row sum has medians 2.13 (beta 0.5), 3.57 (1.0), 3.55 (2.3), 3.45 (2.5); every link is bad. Row 821: van den Berg-Maes and Gielis-Maes are finite-spin and quenched; no block or gauge-invariant influence bound for SU(2) is published. Row 853: annealed, space-time Peierls and PCA methods (Gielis-Maes-van de Velde for directed PCA; Swart-Szabo-Toninelli random Toom contours) exist for non-gauge, chiefly finite-spin systems; none usable for stationary Wilson SU(2) block dynamics. `gap-ds-gauge.md`: revealing in blocks fails for a cube with a collar | Framing (b) for supremum criteria is KNOWN dead at order-one beta; this row adds only what the PCA structure changes, if anything |
| coupling from the past | row 774 | WITHDRAWN before launch (certificate (16) reduced to a one-plaquette Wasserstein distance) | no prior attack on CFTP as a mixing tool |
| Gacs, Toom, eroders | `gap-brainstorm-max.md` L675 (Gacs hierarchical decoders, recalled); row 853 (Toom contours, literature) | named only, as literature | no prior analysis of non-ergodicity of a gauge PCA |
| plaquette variables, Bianchi | `gap-skeleton-max-b.md` A12 (L215-220) and L581-584; `gap-crux-restate.md`, `gap-sep-opus.md` | A12: in plaquette variables the Wilson measure is a Gaussian of variance 1/beta about 1 on each plaquette, restricted to the Bianchi variety; a Poincare inequality in the plaquette metric is FALSE as a route (it holds for U(1) with constant beta while the photon is massless). L581: one 3-cube partition function sum_k k^2 (2 I_k(beta)/beta)^6 has zeros in the right half-plane (GUIDE), so no Lee-Yang theorem | framing (c) Batrouni-Halpern is KNOWN in its magnetic-metric form and dead there |
| diagonal reflections, diagonal transfer | row 962 A6 (ARGUED, REFRAMING); row 963 item (3) (queued, Opus, not on disk) | reflection positivity across diagonal hyperplanes is row 963's question | NOT attacked here; this row asks only whether a diagonal time makes the update site-factorised (a different property) |
| cellular automata, PCA (probabilistic), Domany-Kinzel, light-cone time, Batrouni-Halpern, Q2R, microcanonical, Wolfram | only row 967 and this file (other "PCA" hits are principal component analysis in row 952) | none | NEW to the lane as terms |
| Creutz, overrelaxation | rows 944-957 GUIDE code | used only as samplers | no prior analysis of their invariant measures as a proof tool |

So framing (a) (a PCA structure of the Wilson measure) and the non-ergodicity side of (b) are new to the lane;
the supremum side of (b) and the magnetic-metric side of (c) are KNOWN dead. Steps 2-5 work on the new parts and
state, for the old ones, only what the PCA structure changes.

