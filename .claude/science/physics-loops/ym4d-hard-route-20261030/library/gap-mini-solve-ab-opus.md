lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:31Z

# gap-mini-solve-ab-opus: SU(2) Yang-Mills mass gap (Jaffe-Witten), Mac mini worker 2

Queue row 1248 of FINISH.md. Started 2026-11-20T09:31Z (date -u). Pinned at commit 59f6d02b0 on branch claude/ym4d-hard-route.

Status labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks. A numeric run may guide but is never a proof step.


## Step 0. Reading log (reading only; no new claim; written 09:33Z by date -u)

Read at the pin 59f6d02b0: GOAL.md in full; FINISH.md L1-90 and L299-352; rows 1218, 1228-1251 (RESULT lines);
`parts/gap.md` L1-110 (formulation, wall, methods 1-36, lead rules); `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; the sibling file `library/gap-mini-solve-aa-opus.md` Steps 0-1 (row 1244, running);
(N-phys) as stated in `library/gap-mini-branch-fable.md` L304-310.

Where the problem stands on file (cited, not re-derived):

1. Beside the premises of the Sussman-Alpoge complete account, the gap clause reads one lattice estimate,
   (N-phys) (row 1179 Theorem BP; row 1225). Modulo the ultraviolet carry (UNIV-K), the crux is a finite seed
   for Wilson SU(2) at one coupling where the running coupling is of order one (rows 1225, 1229, 1233, 1238).
2. About 45 engine families are screened with named failing steps (methods 1-36 of `parts/gap.md`; rows 1189,
   1194, 1199, 1200, 1229, 1237, 1244 Step 1.3). The missing object since row 1013 is a band-crossing step
   with a non-abelian sign at order-one response ((K-flow)), or a property of the measure at one scale in the
   band ((K-one)), which needs a number no hand expansion reaches (row 1229).
3. Row 1218's published inputs: A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy) gives
   a full-thermal one-scale seed (A-B*) with a proved conditional ascent (Theorem 7.56); B (the first four
   authors) gives cube-dynamics criteria (BP, BP_0, B-local, B-D) and Corollary 166, BP(n,1/2) for the
   straight-path block law of SU(2) Wilson at beta_W <= k+2 with b = 2^k, by convolution damping; C (Zeng
   Chunping) gives common-rate criteria and a conditional tunneling route. None proves the Wilson estimate at
   weak coupling.
4. Siblings on the same brief at this pin: rows 1243 (z: (S-V)), 1244 (aa: where the one-loop decrement sits in
   the stiffness split of row 1018), 1246 (astra), 1249, 1251 (queued). This row keeps its item distinct.

## Step 1. How best to attack it (judgement, ARGUED; written 09:56Z by date -u)

**1.1 The two open inputs (cited).** Beside the T0 chain, the gap clause reads (N-phys) (rows 1179, 1225). By
(ONE-K) (row 916, checked 917), (N-phys) follows from (A) the ultraviolet carry (UNIV-K) and (B) a seed at one
cutoff's window, i.e. a lattice gap with a thermal count for Wilson SU(2) at one coupling where the running coupling
is of order one (rows 1225, 1229, 1238 Step 1.1).

**1.2 Part (B): my own screening, grepped before any work (rule 0a).** I looked for an input with a definite
non-abelian sign at every coupling that fails for U(1), frozen groups and products with a massless factor. Each idea
I could name is on file, or dies at once for a reason I can state. Counts are files under `library/` and `parts/`.

| Idea | Status |
|---|---|
| Schrodinger-functional coupling as the 4D stiffness (scale-invariant boundary flux, runs at one loop, zero running for U(1)) | on file (20 files name the Schrodinger functional, 37 step scaling); it is the twist class of rows 1011-1018, 1228; its closure under conditioning holds only for typical sub-cell data, which is the (K-flow) step of rows 1243 (S-V) and 1244 (stiffness split) |
| Rigid group on integrated variables via the residual global colour symmetry of a complete gauge (tree, Landau, axial) | dies: a relative colour rotation of a region is a gauge transformation followed by a reset of the tree links that cross its boundary, i.e. a local insertion on those links, or nothing (axial case); this is CEN+ (row 1016) and row 1238's table line 2 |
| Non-abelian Casimir excess j(j+1) - j^2 = j > 0 of electric flux on a link (Kogut-Susskind form) | dies: it bounds the electric energy of a flux sector from below by (g^2/2)(3/4) per crossed slice, but the vacuum carries an extensive zero-point electric energy, so no bound on the energy difference follows at weak coupling |
| Doeblin bound on single-link conditional laws (density at least e^(-c beta) Haar) | dies: gives only a perimeter-law upper bound on Wilson loops at every beta, which also holds for U(1); not selective |
| Non-conservation of adjoint flux through two parallel plates (gluon colour charge) as the selective quantity | on file in the two-flat-plate class: check 1247 L-section (the (2,2) mixed response equals Cov(j(j+1), k(k+1))/9; the generator identity allows field colour charge above a layer; no screening rate); its decay rate in the plate distance is bounded by the neutral gap, so it restates the gap |
| Photon as Goldstone boson of a broken U(1) one-form symmetry; SU(2) has only a Z_2 one-form symmetry | not an engine: nothing forbids an emergent U(1) in the infrared; the Z_2 deconfined alternative is branch II of row 1161 (on file as (BS)) |
| Dilute topological objects at the band (instanton fugacity e^(-8 pi^2/g^2) is about e^(-30) at g^2 = 2.5) | not an engine: the perturbative fluctuations at the band are of order one and are what must be controlled; instantons do not confine in 4D (RECALLED) |
| Vortex percolation from insertion tolerance at the band scale | dies as stated: insertion tolerance holds also in the deconfined Z_2 phase, where vortices do not percolate; percolation is the dynamical question itself (Mack-Petkova, Tomboulis on file: 49 and 99 files) |

So I add no engine of a new kind. This agrees with rows 1219, 1225, 1229, 1237, 1238, 1243 and 1244.

**1.3 Part (A).** (UNIV-K) is open in (M1)-(M3), (VAC-ID) and (DENS-K) B1-B2 (row 924 table L430-466; row 1238
Step 4). Rows 1233, 1237 and 1238 worked on it today; (MAPCONV-F) = (M1)-(M3) is not a session item (row 1238 note 1).
No row has attacked (VAC-ID). It is needed even when a seed exists.

**1.4 Decision.** This row takes (VAC-ID) of row 924: show that the vacuum scalar entering M_K has the (ET8) form,
with its locality and nonwrapping hypotheses, or name the exact account statement that is missing. Moves: (UNIV-K),
the carry of the gap chain. Success: the vacuum part of (UNIV-K) is uniformly small (row 924 Lemma 5.1) and, with
(VAC-LIP), summable (Lemma 5.3). Failure: the first missing account statement, by name and line.
Rule 0a (grep at this time): `library/open-core.md` has no gap or VAC-ID entry; VAC-ID appears only in row 924's
file and the rows that cite its table (1233, 1237, 1238), none of which attacks it.

## Step 2. (VAC-ID): what the account states about the vacuum constant (READ; started 09:58Z by date -u)

Source: Ethan Sussman and Levent Alpoge's account (with Claude and Codex as authors of its text), `YM4_1400.tex` at
commit 2bc0658f91d2 (the copy and line numbers of row 924), fetched by URL into a scratch folder outside the repository.

**2.1 The first finding: row 924 stopped four dozen lines short.** Row 924 read the local companion criterion
(ET8)-(ET10) at L102529-102592 and its caveat L102586-102589 ("if nonwrapping compatibility has not been established
for the actual formation rule, (ET9) has not been proved for that construction"). The account continues. At
L102645-102670 it states, for the actual construction (quoted in part):

> "The actual vacuum constants have the decomposition
> E_{l,K} = sum_{j<K} [ E^{(j)}_I + sum_y sum_{X ni y} E^{(j+1)}(X,1,y) + sum_X R^{(j+1)}(X,1) ]."

E^{(j)}_I is "one scalar per nonpivot bond" (Haar and Gaussian factor) plus "one scalar per cell of the next lattice"
(gauge fixing), the same two scalars on both tori since the coupling sequence and the gauges are common. The remainder
R^{(j+1)}(X,1) is pointed by giving R/|X| to each root of X. Then (L102657-102667): a domain whose complete window lifts
to a cube of side at most min(l, l_*)/4 "has the same rooted value on either torus by the common companion rule of"
the section `flow-a-common-companion-and-the-torus-floor`, the other domains have length at depth u at least
c l_* L^u/M - C, and

    | E_{l,K}/l^4 - E_{l_*,K}/l_*^4 | <= C sum_{u>=0} L^{4u} e^{-c l_* L^u/M}.                         (V1)

"Thus the common companion comparison applies to the vacuum constant in the sourced construction. Neither vacuum
density need have a cutoff-independent limit."

**2.2 Consequence for row 924, if (V1) applies to the scalar of Phi^vac (to be checked in 2.3-2.5).** Take the pair
(l, L l) at one datum. Multiply (V1) by (L l)^4:

    | Phi^vac(d) | = | L^4 E_{l,K} - E_{L l,K} | <= C (L l)^4 sum_{u>=0} L^{4u} e^{-c l L^u/M},                (V2)

uniformly in K. This is row 924 Lemma 5.1's conclusion, reached without passing through (ET8) at all. So (VAC-ID) is
not needed in the form row 924 stated; what is needed is that (V1) is proved in the account and applies to the
scalar of row 924's split. Open checks, in order: (2.3) the status of the section that supplies the common companion
rule; (2.4) whether "the sourced construction" at zero source gives the scalar e^{-Ecal_(K,empty)} of row 924's split
(L96196 says "The same comparison identifies the unsourced vacuum constant"); (2.5) whether the label constants
Ecal_(K,S) for S nonempty belong to Phi^vac or to the large-field part Q_K (DENS-K).

