# Review of the explicit bare determinant coupling formula

VERDICT: LAND

The verdict covers the bounded analytic reduction in
[BARE_DETERMINANT_COUPLING_ASTRA.md](BARE_DETERMINANT_COUPLING_ASTRA.md),
581 lines, SHA256
`426f774581ae8385b1c546e676fb313bfed48ab14913454bdc38f67f2cebb230`.
It does not certify a coefficient value or sign, a universal beta coefficient,
Wilson or inherited-action closure, a repeated effective trajectory,
non-freeness, four-dimensional continuum existence, or a positive physical
continuum mass gap. Both full targets remain open.

This is one fresh hostile source-first review by
`/root/review_bare_determinant_coupling`, distinct from author
`/root/mixed_cap_chart`. It is same-family review in a separate context,
not external peer review or independent backend attestation. The dispatch
requested Astra/max; this report does not manufacture an independent
attestation of the runtime backend. No prior review report supplied a verdict
or a mathematical premise.

The whole target was read before the author's two JSON records. The needed
source mathematics and cited primary-paper windows were examined next.
The [source-only findings](checks/review_bare_determinant_coupling_source_findings.json)
and [bounded read manifest](checks/review_bare_determinant_coupling_source_read_manifest.json)
were then frozen before the author packet was opened. Those freezes remain
unchanged. Later packet checks are confined to the separate
[author-packet assessment](checks/review_bare_determinant_coupling_author_packet_assessment.json).

## Mathematical assessment

No material defect or substantive repair is required for the stated reduction.
The conclusion is an explicit, absolutely convergent compact Brillouin integral
for the actual bare one-loop marginal. It is not an evaluation of that integral.
The independent checks used written algebra and analytic bounds; no scientific
numerical calculation or executable vertex implementation was run.

1. **Actual kernel and complete free space — source lines 42–171.**
   Expanding the two means independently and maximizing over the traceless
   tangent cancels the path-spread term at tree order. The quadratic action is
   one half of `||DA||HS^2+kappa||B-QA||HS^2`, hence the displayed `K0` and
   `Phi=kappa G Q^* e_mu`. There are exactly
   `4L^4-(L^4-1)=3L^4+1` free types per cell. The CB brick recovery estimate
   controls every type, including the zero-momentum root and harmonic
   directions. The finite-cell Fourier transform encodes fine aliases in those
   types. Its counting measure introduces no additional `L^-4` factor.
   Actual negative edges reverse matrix order; repeated periodic occurrences
   remain, including at `T=2` with the lifted-brick convention.

2. **Cartan critical motion — lines 173–221.**
   The whole diagonal torus fixes the prescribed Cartan coarse profile and
   preserves the tree section. Uniqueness therefore makes every critical fine
   link diagonal, even when the chosen colour is nonregular. Entrywise
   conjugation maps real amplitude `t` to `-t`; the near-identity traceless
   logarithm is odd. Polarizing the vanishing real quadratic map and then
   complexifying gives the mixed zero second derivative for the two external
   Fourier insertions. Thus the linear `Phi` response is sufficient through
   external degree two. Matrix-exponential second variations remain present.

3. **Constrained saddle and vertices — lines 223–324.**
   In the homogeneous degree-`n` saddle equation the new unknown `Y_n` enters
   only as `-2Y_n`. Projecting its other terms onto traceless matrices gives
   precisely the four stated recursion steps. The scalar residual is retained;
   this is not a U(N) polar substitute. Ordered products of `Exp_4` determine
   every field coefficient needed for two fluctuation tags and at most two
   external tags. The right-trivialized order `exp(A)exp(x)` and its inverse
   produce the intrinsic Hessian. Independent tags `s,t` recover the Hessian
   bilinear form also for repeated indices. No extra factor two or implicit
   critical-field derivative remains.

4. **Colour and momentum trace — lines 278–413.**
   The real colour basis is HS orthonormal. In the complex root basis,
   `-tr(F_ji F_ij)=1`, so the dual row is `F_ji`. Torus invariance preserves
   the complete neutral block and every ordered root block. The trace
   decomposition retains neutral mixing and all root multiplicities. The
   cubic vertex maps `q` to `q+p`; the return vertex is evaluated at
   `(q+p;-p)`, including its shifted fluctuation phases. Direct expansion of
   one half of the full trace-log gives one half of
   `Tr(G K_+- - G K_+ G K_-)`, with the two ordered cross terms combined by
   cyclicity. No gauge, ghost or harmonic determinant has been appended or
   deleted.

5. **Every projection factor — lines 387–413 and 462–513.**
   With `z_+=epsilon exp(i theta)/2` and its conjugate partner, phase averaging
   contributes `epsilon^2/4`. The resulting `I(P)` is BM's `Pi_mu mu(P)`,
   not twice that symbol. Since the integrated symbol is even and vanishes at
   zero, division by `4 sin^2(P/2)` gives
   `b_det=(1/2) integral [P^2]J=(1/4) integral partial_P^2 J|0`.
   The inverse recurrence includes the Taylor half-factor in `K2`.
   Averaging over twelve ordered planes consequently gives the `1/24`
   coefficient in the main formula. The external colour has HS norm
   `sqrt(N)` while the fluctuation basis has HS norm one; the FLOW conversion
   has not been lost.

6. **Uniform limits and reader agreement — lines 415–475.**
   The finite Laurent perturbation obeys
   `||K0(q+P e_nu)-K0(q)|| <= |P| M_K` for `|P|<=1`. The selected `2r`
   makes it less than `a_gap/2`; the inverse norm is thus at most
   `2/a_gap`, uniformly in real `q` and the stated compact kappa interval.
   Finite word and saddle polynomials then have uniform bounds on that disc.
   Cauchy's estimate gives the displayed coefficient bound and allows
   differentiation under the compact integral. Compatible finite grids
   converge at fixed external momentum. IC's connected inverse, critical-map
   and determinant construction, together with BM's fixed original-reader
   norm and seam estimate, identifies this limit with the original marginal
   convention and supplies the needed spatial moments. Coarse root-gauge
   invariance and the vanishing linear term imply the Ward identity; continuity
   in all momentum directions forces `Pi(0)=0`. The real diagonal axis symbol
   is even. Neither `J(q;0)=0` pointwise nor vanishing finite-torus holonomy
   response is assumed.

7. **Measure and normalizer amplitude — lines 60–85 and 477–521.**
   At the complete stationary point the Hessians satisfy
   `K_coord=E^T K_intr E` and `det E=product j_N(b_T)`.
   The second differential multiplies the complete zero gradient. The half
   logarithm of the Hessian determinant therefore cancels the coordinate Haar
   logarithm exactly on the positive branch and its local continuation.
   For commuting backgrounds, the saddle-recentered `S` has no first external
   coefficient and mixed coefficient `v H^2`. The full Casimir identity gives
   `[z_+z_-]log A=Dv/2`. Independently counting the affine tree-gauge currents in
   BM gives `sum_rho v/P^2=2(L^2-1)/(12L^2)`, and hence
   `alpha_amp=D(L^2-1)/(12L^2)`. The coordinate Haar term contributes
   `-N^2(L^2-1)(L+1)/72` to the coordinate determinant marginal, cancelling
   its positive action-side counterpart. Probability-Haar constants remain
   until differentiation, and no coarse Haar integration is introduced.

## Source and literature boundary

The consumed mathematical supplier windows were BM lines 1–610, CB 1–439,
FK 1–365, and IC 22–314 and 586–731. Their exact hashes, line counts and
roles are in the frozen manifest. These are partial supplier reviews, not
claims to have re-reviewed their entire histories. BR was inspected only as a
heading/link and identity record for the separate original-cut remainder;
its theorem was neither needed nor re-proved for this determinant reduction.

The original-definition windows read after the freeze, for packet checking,
were LINEAR_PACKAGE lines 1–22 and 65–82 and PROOF_session16_snapshot lines
455–480 and 1498–1507. They agree with the paired contour words and arithmetic
normalized kernel already checked. They do not change the frozen findings.

The following primary comparisons were read at their actual cited equations:

- [Luescher–Weisz, hep-lat/9504006](https://arxiv.org/pdf/hep-lat/9504006),
  PDF dated 11 April 1995: section 5.1, equations (5.1)–(5.7), with nearby
  measure context. Its multiplicative background decomposition and adjoint
  gauge law are relevant, but its gauge fixing and ghosts differ from this
  probability-Haar tree quotient.
- [Luescher–Weisz, hep-lat/9505011](https://arxiv.org/pdf/hep-lat/9505011),
  PDF dated 12 May 1995: section 4.1 and section 5, especially (4.1) and
  (5.1)–(5.3). The vertex and one-loop organization is a valid comparison.
  Its propagators and matching coefficient do not determine the present
  gapped conditional determinant.
- [DeGrand–Hasenfratz–Hasenfratz–Niedermayer, hep-lat/9506030v1](https://arxiv.org/pdf/hep-lat/9506030v1),
  v1 header dated 27 June 1995: sections 2–4, (4)–(11) and (15). It retains an
  SU(N) normalizer and saddle maximum. Its scale-two staple/fuzzy kernels and
  fixed-point input differ; no perfection conclusion is transferred.

The caches are local and are not vendored. Bałaban and Dimock remain credited
for the constructive gauge/localization and coupling-extraction architecture;
that attribution supplies no missing theorem or numerical coefficient.

## Packet and process assessment

The separate author-packet review checked eleven declared source/count
bindings; all match current bytes. Both author JSON records preserve the
unevaluated integral, unevaluated sign, one-step scope and open full targets.
The four historical read-manifest pointers exist and were hash checked only.
They cannot authenticate the author's earlier reading history and were not
used as scientific evidence. No old review verdict was opened or reused.

The selected procedure is repository revision
`01589af3faf806b736c42dc2f3bd625e9edead9f`; observed `origin/main` was
`bcab5d2ee4a908fbb4e6025635fb878e6c157ebe` and the worktree HEAD was
`1ca794aeb72236a0460545e4b9e3373ad589dc4c`. The consumed pinned governance
paths matched that main snapshot and the worktree. Both actual installed
entrypoints were read: physics-loop SHA256
`7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4`
and review-loop SHA256
`a629d477c0e3663c4f4540a2dc5ae2eebe6451b2f6f0be7d84a15d3c6a176879`.
They differ from the selected pinned entrypoints; installed references were
not mixed into the pinned procedure. The lane's exact 11-line
[PROCESS_LIGHT.md](PROCESS_LIGHT.md) has SHA256
`b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab`.
Additional hash-only governance inventory is recorded separately in the
[supplemental process manifest](checks/review_bare_determinant_coupling_additional_process_manifest.json).

The physical model, probability Haar, finite block geometry, kappa interval
and FLOW/HS conventions are explicit conditions. No framework primitive,
measured value, empirical selector or literature beta coefficient supplies
the result. The axiom/primitive authority read does not derive this supplied
SU(N) Wilson model or promote the result to retained status.

One source-review iteration produced zero material findings, zero source
fixes and no skipped known scientific defect. The bounded formula's proof
obligations are closed at the stated source interfaces. The full continuum
and physical-gap targets are open. No no-go claim, audit verdict or retained
status is assigned. This is a source readiness verdict, not an integrated
current-main landing gate. Publication, combined validation and any future
independent audit remain the coordinator's responsibility.

Direct `lint_one_file(..., apply_fix=False)` is used on explicit Markdown
paths because the CLI excludes this lane. Its
[mechanical record](checks/review_bare_determinant_coupling_vocab_lint.json)
accompanies the report. No science runner, worker, simulation, audit pipeline,
Git commit, push, source edit or shared-front edit was performed. The
[review receipt](checks/review_bare_determinant_coupling_receipt.json) binds
the report and freezes; the
[final identity recheck](checks/review_bare_determinant_coupling_final_identity_recheck.json)
is written after that receipt and checks their current identities together
with the target, packet, consumed suppliers and governance.

VERDICT: LAND
