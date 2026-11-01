---
claim_id: qubit_lattice_gauge_mdtn_balaban_interface_firewalled_note_2026-10-31
claim_type: commentary
claim_scope: >
  Neutral commentary on how the MDTN strong-coupling result relates to the Balaban / hard-constraint
  route of PR #10132. No claim. FIREWALLED: must not be shown to the independent attempt on PR #10132.
upstream_dependencies: []
status: commentary only (no claim); status authority is the independent audit lane only
---

# FIREWALLED — Interface between the MDTN strong-coupling note and the Balaban / hard-constraint route

> **Firewall notice.** Writing this file required reading both sides of PR #10132's firewall (attempt files and
> gate reports). It must **not** be provided to, quoted to, or summarised for the independent attempt on #10132.
> No other file in this PR depends on it. Split out of
> `docs/QUBIT_LATTICE_GAUGE_MDTN_EMBEDDING_OUTLINE_NOTE_2026-10-31.md` §8.


**Framing.** Independent of, and complementary to. **Firewall caveat:** to write this section I read both sides of
PR #10132's firewall (attempt files and gate reports). This section must therefore **not** be fed to the independent
attempt; treat it as neutral commentary only.

**8.1 Where #10132 stands (draft, open, 216 files, no review comments, read 2026-10-31).**
Target T1: SU(2) Wilson lattice YM has a non-trivial, RP, hypercubic-invariant limit on R⁴. The mass gap is an
explicitly later target. FINISH.md: "Existence is not proved"; `lab_ops.py status` counts 44 open obligations (and
says this understates what is open). Gate reports (same-model checks, not audits):
* independent-core: the rough-set claim for long Z is false as written (D1); D2 (complex-W sector), D3, D5 unfinished.
* theorem-z (repaired): Lemma OC wrong as written (at a long flux sheet the fill does not exist at the stated radius).
* field-tier: Lemma 14.15(c) wrong; (K3) not preserved by the block map; UV-OS clause (GS_j)(e3) false in free theory.
* net-tier: T1-net as worded is satisfied by a static random constant field (H = 0), so it is not a non-triviality statement.
* uv-ct: ADVANCE conditional on UV-CT; naive Gaussian CT4 fails by log log(1/a).
* lemma-ex: provisional ADVANCE, no WRONG found.
The sibling soft-kernel route (PR #10114) is paused.

**8.2 Stall block.** The route is stalled on large-field / rough-set control (long flux sheets, complex-W
sector, the K3 class not stable under blocking) and on fixing counterterms with control beyond Gaussian order.
None of this is a strong-coupling question, so the Main Theorem does not reach it directly.

**8.3 Top 3 acceleration ideas (each: what would have to be proved).**
1. *Analytic (entire) flux-sector partitions of unity instead of sharp small/large-field cuts.* Character / Peter–Weyl
   sector projectors (the objects of §3) are smooth and gauge invariant; sharp cuts cause the D1/D2-type boundary
   defects. **To prove:** a TAIL-type bound with locality for the soft partition, i.e. that large-field weights stay
   summable per block with constants uniform in the scale. [C, plausible]
2. *Exact gauge-invariant truncated transfer-matrix testbeds with rigorous Peter–Weyl truncation errors* for adversarial
   checks of Lemma EX, the K3-class inequalities and the CT coefficients at small volumes. **To prove:** a truncation-
   error bound ‖T − T_{j_max}‖ ≤ ε(j_max, β) in the relevant norm, so numerical counterexamples are certified.
   [plausible; tooling]
3. *Counterterm classification for CT1–CT3.* Hypercubic + gauge + reflection symmetry ⇒ the only local gauge-invariant
   terms of dimension ≤ 4 are the constant and Tr F² (Lüscher–Weisz-style), which pins the form of E(w). **To prove:**
   the classification for the complex plaquette-source setting of UV-CT, including reflection-periodic sources.
   [C, plausible]
Speculative only: a Peierls flux-sheet bound for theorem-Z / Lemma OC (works at strong coupling, fails at weak
coupling); BHM quasi-adiabatic flow as a multiscale RG (strong coupling only); MDTN gauge-invariant coordinates in place
of axial/tree gauge.

