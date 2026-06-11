# NO_GO_LEDGER — registrability-bridges-20260610

Prior dead routes and reviewer objections, so the loop does not re-explore them.

## Strong-CP lane prior no-gos (blocker (a) context)

| route | verdict | why dead | citation |
|---|---|---|---|
| Derive "no bare theta slot" premise from retained RP half-Cauchy-Schwarz | NO-GO (retained_no_go) | Theta-anti-invariance of the CP-odd density cancels the imaginary phase in every reflection-Hermitian observable; RP cannot detect CP-odd imaginary additions of topological-charge type | `STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md` |
| K/CPT orbit invariance => phase erasure (naive) | FALSE | cos(arg z) is K-invariant yet phase-dependent; evenness is necessary not sufficient | hostile guard in `TIER_A_KORBIT_...NOTE_2026-06-09.md` |

**IMPORTANT scoping note.** The RP no-go is about premise 1 ("no bare theta slot
is admissible"). Blocker (a) is about premise 2 ("positive real quark-mass
orientation / arg det(M_u M_d) = 0"). These are DISTINCT premises. Closing
blocker (a) does NOT require re-attacking the RP route, and does NOT by itself
close premise 1. The det-readout bridge addresses ONLY the mass-orientation
premise. (Tracked so I do not overclaim a full strong-CP closure.)

## AC_phi_lambda / |delta| lane prior no-gos (blocker (b) context)

| route | verdict | why dead | citation |
|---|---|---|---|
| Periodic (q*pi) source for delta | NO-GO (enumeration) | radian-bridge audit forecloses periodic bins; rational density 2/9 is OUTSIDE those bins (carries 2/9 as its own unforeclosed witness) | `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md` |
| Wilson-mark selection on the rank-2 space | NO-GO | eigenline/cobordism no-gos police Wilson-mark selection; a readout identification is not a mark selection (different scope) | `KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md`, `KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md` |
| Standard det-sign pi packaging delta = pi*L = 2pi/9 | DEAD (wrong spectrum) | predicts m_tau off by orders of magnitude; the det-sign pi route is unavailable because the multiplicative lemma forces k=0 (no registrable pi*n_- phase) | `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_..._2026-06-09.md` E8 |
| PR #3428 staggered-gate closure assembly + convention-class reclassification | REJECTED/STRIPPED by owner | a live status inventory + shallow scheme-core checks do not retire the Tier-A admission; convention-class move needs explicit owner/audit registry action AFTER the theory/audit chain lands | PR #3428 owner review |
| Broad negative "det_C not forced by first-order structure" | DEMOTED (N1 failed: 4 routes < 5) | broad negative did not pass no-go gate; only the four-cell mechanism landed | `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` |

## R2 (PL/ABSS global bridge) prior status (blocker (b-ii))

| route | status | why | citation |
|---|---|---|---|
| Finite-R cone-cap -> global PL S^3 identification | LEFT OPEN (live bridge) | Euler characteristic is BLIND among closed orientable 3-manifolds (all chi=0); finite-R combinatorics cannot determine global homeomorphism type | `KOIDE_APS_C3_FIXED_LOCUS_...NOTE_2026-06-05.md` Part D2 |
| Global Cl(3)/Z^3 -> PL S^3 x R | NAMED OPEN (external math) | provably requires PL Poincare (Perelman 2003), TOP=PL dim 3 (Moise), van Kampen pi_1=0 — standard external mathematics, NOT on framework surface | same Part D |

**R2 is a topology question, NOT a Record-registrability question.** It cannot
be closed by the shared-layer registrability theorem. Its honest status is
import-required (external-math LIVE). Whether R2 is even LOAD-BEARING for the
AC_phi_lambda *registrability* reduction (vs. only for the eta-invariant /
single-summand readout) is a question to settle in this loop — if the
unordered-multiset registrability bridge does NOT route through PL/ABSS at all,
then (b-i) can close while (b-ii) is bounded-as-external-import.

## Routes this loop must NOT re-walk

- periodic q*pi delta source; Wilson-mark selection; det-sign pi packaging;
  RP-derivation of premise 1; convention-class reclassification by fiat; broad
  "det_C not forced" negative.

## Cross-cycle echo candidates (structurally similar walls retired elsewhere)

- The Record reclassification (Record was Tier-A, now an approved axiom node)
  retired a wall by an OWNER governance decision + minimality policy, NOT by a
  new axiom. This is the template the AC_phi_lambda convention-class move would
  follow — but only AFTER the theory chain lands. Not available to this loop to
  *enact* (audit-lane owned), only to *prepare*.
