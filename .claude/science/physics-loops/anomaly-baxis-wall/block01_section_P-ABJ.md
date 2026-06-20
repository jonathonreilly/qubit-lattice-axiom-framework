# Block01 Section — Edge P-ABJ (internal-route escape rays)

**Edge:** P-ABJ / P1 of keystone
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
(fanout 1105). The bridge's central registered premise: the external
Adler-Bell-Jackiw anomaly-to-inconsistency implication (B2). The *external*
admission is not derivable from A_min by policy (standard physics). This section
attacks the **internal-route wall's open escape rays**, which is the only part
of P-ABJ that admits fresh framework work.

**Runner:** `scripts/frontier_abj_internal_chi_nonzero_index_escape_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_abj_internal_chi_nonzero_index_escape_2026_06_20.txt`
(+ `.json`). **Result: TOTAL: PASS=34 FAIL=0.**

## Scope and absorbed authority (cited, recomputed in-tree)

A_min = Lattice (cubic `Z^3` nearest-neighbor adjacency) + Quantum + Record,
plus the approved primitives: `kinetic_isotropy_primitive` (emergent time edge
grained on the SAME footing as the spatial cubic edge ⇒ hypercubic `Z^4`
nearest-neighbor adjacency), `scale_reference_primitive` (units only),
`realized_state_primitive` (slot only). None of these supplies a gauge field, a
boundary, a non-cubic cell, or a topological-sector selector.

Absorbed (NOT rebuilt) — recomputed in-tree in Part 0 of the runner:
- `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md` — **retained_no_go**,
  runner PASS=45. On any finite even periodic `Z^4` torus with equal
  `eps=+1 / eps=-1` sublattices, `D=[[0,B],[-B^dag,0]]` with `B` **square**, so
  `A_t = Tr(exp(-t B B^dag)) - Tr(exp(-t B^dag B)) = 0` for all `t` and all
  U(1). Explicitly leaves OPEN: `chi!=0 / Q!=0` background, taste-singlet /
  Adams / overlap-GW index, imbalanced/curved complex, non-abelian cohomology.
- `ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md` —
  **retained_bounded**, runner PASS=36. GW is sufficient-not-necessary;
  re-targets `(P1')` to "exhibit a framework-internal `chi != 0` or `Q != 0`
  background on which `A_t != 0`". The obstruction is the flat/free-background
  eps-gap `(G1)` `H(m)^2 = K^2 + m^2 I` ⇒ spectral flow 0, plus `chi=0` `(G2)`.
- `ABJ_ANOMALY_FRAMEWORK_INTERNAL_U1_JACOBIAN_NARROW_NOTE_2026-05-27.md` —
  PASS=19. Carves the smaller residual `(P1')` from `(P1)`; the abelian
  arithmetic (`Tr[Y^3]=-16/9`) is framework-sound, only the non-zero-index
  existence is open.

Part 0 of my runner reproduces the square-block wall on all four governed
backgrounds (`Z4xZ2^3` and `Z4^4`, random and flux U(1)): balanced sublattices,
`eps D eps = -D`, and `max|A_t| < 1.2e-14` in every case. Source discipline:
nothing cited blind from the unaudited keystone.

## Three escape rays attacked

### R-A — `chi != 0 / Q != 0` background on the A_min substrate (the re-target)
The square-block wall is precisely `N_+ = N_-` (balanced sublattices, `chi=0`).
The GW-not-necessary note re-targets `(P1')` to an imbalanced/curved complex. The
sharp A_min question: **can A_min's closed cubic-adjacency hypercubic complex
EVER be eps-imbalanced with the chirality grading intact?**

**NEW, sharper fact (runner P1, enumerated over all `{2,3,4,5}^4` tori):** a
hypercubic torus eps-imbalances **IFF its total site count is odd IFF EVERY edge
length is odd** (16 imbalanced cases found, all all-odd). And when every edge is
odd, every lattice direction carries an odd cycle ⇒ the nearest-neighbor graph
is non-bipartite in every direction ⇒ `{eps,D}=0` is **broken in every
direction** (verified on `(3,3,3,3)`: `N+=41,N-=40` imbalanced, but
`max|eps D eps + D| = 1.000`, so `eps` is no longer a chirality). The escape is
**self-defeating**: the only closed hypercubic complex A_min supplies that is
imbalanced is exactly the one whose chirality grading is destroyed, so there is
no chiral index left to be nonzero.

This is *stronger* than the original no-go's "some odd edge" framing — the
sole-author original control used a single odd direction; my enumeration shows
imbalance on the closed substrate requires **all** edges odd.

### R-B — taste-singlet / Adams / overlap-GW index as a framework bridge
Built the overlap index `½ Tr[eps · sign(H)]` with the Hermitian kernel
`K = eps D` (`{eps,K}=0`) on the A_min torus. Runner P3: the overlap/Adams
taste-singlet index is `0` on the flat `(4,2,2,2)` and `(4,4,4,4)` tori, **and
remains 0 under a nonzero-flux U(1) background**. Reason verified in-tree: the
eps-gap `(G1)` `H(m)^2 = K^2 + m^2 I` holds exactly (`m∈{0.37,1.0}`), pinning the
spectral flow to 0. The overlap/GW route does NOT escape on the A_min substrate
because the obstruction is not the absence of GW (per the retained note) but the
eps-gap, which is a property of the *balanced* A_min substrate itself.

### R-C — non-abelian cohomology / topological charge `Q`
Runner P4: on a closed A_min torus with single-valued links the total winding
through every 2-plane is `Q=0` (`max|Q_plane| < 1.4e-15`). A nonzero integer `Q`
(`Q_tx=-16` for the flux case) appears **only** when a boundary twist /
transition function is injected — an external topological datum, not produced by
A_min's adjacency + Quantum + Record (which supply no gauge field at all).
**Decisive:** even with the injected `Q!=0` twist, `A_t=0` on the balanced
substrate (`max|A_t| < 1.2e-14`) — the square-block wall survives nonzero gauge
topological charge. So `Q!=0` alone does not rescue the eps-index; you also need
the imbalance, which (R-A) shows is unavailable with intact chirality.

## The wall, as an enumerated closure-condition lemma (runner P5)

A nonzero taste-singlet/staggered index requires **at least one** of:
- **(W1)** imbalanced eps-sublattices `N_+ != N_-` with `eps D eps = -D` intact
  — verified IMPOSSIBLE on every closed hypercubic torus (`{2,3,4,5}^4`):
  imbalance ⇔ all edges odd ⇔ grading broken in every direction (mutually
  exclusive);
- **(W2)** an open boundary / non-cubic cell giving rectangular `B` — A_min's
  cubic adjacency closes into a torus (no boundary axiom), so `B` is **square**
  (witness `(4,2,2,2)`: `B` is `16×16`);
- **(W3)** an externally injected gauge topological charge on an imbalanced
  complex — bare A_min substrate gives `Q=0` and `A_t=0`.

Control (runner P2, OFF the A_min substrate): an open `3×3` complex IS imbalanced
(`N+=5,N-=4`), KEEPS `{eps,D}=0` (rectangular bipartite `B`), and yields a
**nonzero** index `A_∞ = N+ - N- = 1`. This confirms the escape mechanism is
real — but it requires a boundary A_min does not supply. So the wall is a
genuine A_min-withholding wall, not a numerical accident.

## Honest status

- **Internal route: SHARPER no-go.** Every enumerated escape ray (`chi!=0`,
  taste-singlet/overlap, `Q!=0`, non-abelian-via-injected-twist) is blocked *on
  the A_min-internal closed hypercubic substrate*. The new load-bearing fact is
  the imbalance⇔all-odd⇔grading-destroyed exclusivity (R-A/W1), which closes the
  `chi!=0` re-target ray that the GW-not-necessary note had left open *for the
  A_min substrate specifically*. This does NOT close `(P1')` in general — a
  genuinely curved / non-hypercubic / open cell complex still escapes (P2
  control), but **A_min does not supply such a complex**.
- **External premise: stays a registered admission.** P-ABJ/P1 itself (the
  Adler-Bell-Jackiw anomaly-to-inconsistency implication, B2) is standard
  physics and not derivable from A_min by policy (no-new-axioms / no-new-import).
  It is NOT identification-walled in the A_min sense — it is categorically an
  external admission. This matches the blueprint per_edge_status: P-ABJ is
  `external_premise — arithmetic-sound, internal-route-walled`.

## Run-exercise-skill recommendation

**YES** — a genuinely new hard wall was hit and sharpened, warranting the repo
exercise skill. The new wall is the imbalance⇔all-odd⇔chirality-destroyed
exclusivity on the closed hypercubic A_min substrate (R-A/W1), which the prior
square-block no-go and GW-not-necessary note left open as "exhibit a `chi!=0`
background". My enumeration shows that re-target ray is unavailable *internally*
to A_min (it would require boundary/non-cubic/injected-topology structure A_min
withholds). The honest framing for an exercise-skill run: steelman "a curved or
non-hypercubic framework cell complex witnesses a nonzero taste-singlet index"
and test whether ANY such complex is derivable from / compatible with A_min's
Lattice axiom — my runner shows the *closed hypercubic* family is exhausted;
the open question is whether A_min's cubic-adjacency axiom can be read to permit
a non-torus / curved closed complex without a new primitive. (My finding: it
cannot, on the closed hypercubic reading the Lattice + kinetic-isotropy
primitives fix; any escape needs structure outside A_min.)

## Arithmetic-core bankability note

The P-ABJ *arithmetic* (the anomaly traces `Tr[Y^3]=-16/9` etc. consumed by B1)
is already a deps-all-retained bounded fact via the U1-Jacobian note + the
scale-free anomaly core, and the SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED
precedent (deps-all-retained, audit-ready, PASS=11) shows it is bankable WITHOUT
routing through the unaudited keystone. **But P-ABJ's load-bearing content is not
arithmetic** — it is the external anomaly-to-inconsistency implication (B2), which
has no in-tree deps-all-retained arithmetic core: the implication itself is the
external admission. So unlike P-HY/P-COMP/P-REC, the bankable arithmetic core for
P-ABJ exists only for the *trace inputs the premise consumes*, not for the
premise edge itself.
