# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_KINK_THIRD_CHECK.md`, SHA256 `07a32e5e35f856456682514ca422270ed1ba4f3f4d230dace6566a27f64f5c1a`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Focused native kink-band third-order check

No formal audit, pack edits, width certificate or physical scalar claim. Root retains authorship.

For the degenerate unperturbed energy8 band and R=Q(8-H0)^(-1)Q, canonical Hermitian third order is PVRVRVP-(1/2){PVR²VP,PVP}. The core implements this correctly as B R V_QQ R B.T minus the metric anticommutator. Both denominators retain their signs. Restricting V_QQ to Q states directly reached from P is sufficient at third order: the left/right RVP factors have zero support on every other Q state. Multiple paths are summed in sparse entries. There is no missing1/2 in the direct term; the1/2 belongs only to the two normalization orderings.

The independent projection procedure from the preceding check was extended to H3 at L6/L8. Using the positive-hopping host convention A=H1, it verifies

H3_host=A³/128-13A/32-(11/32)(|0><1|+|1><0|).

Here indices are zero-based and the final host hopping is2sqrt(2), retained inside A. Maximum host discrepancy is4.2e-15. The second-order side-vector sign is fixed by its negative coupling to host index1. At L8 the H3 side column is[-sqrt(2),0,1/sqrt(2),0], side diagonal zero. At L6 host index2 is already the folded terminal site, giving[-sqrt(2),0,1] instead. This is a finite-size endpoint factor, not an error in root's JSON; an unqualified L6 claim of1/sqrt(2) would be incorrect. Side errors are below6.5e-15; enlarged-space H3 closure residuals below8.3e-15. These are tested finite physical-band matrix identities, not an all-L symbolic proof.

Replayed the full512-dimensional L3 canonical spectral-subspace control. Operator errors after adding K3 divided by ratio^4 are3.19936,3.17207,3.15726 at .04,.02,.01. This supports the cubic coefficient and finite fourth-order remainder. That control uses ABSOLUTE band energy: it correctly undoes the second-order ground shift and does not claim its L3 absolute K3 is a universally ground-subtracted excitation coefficient. For the tested L6/L8 expansion, no third-order ground off-diagonal aligned-state process exists (minimum orderL), and a three-transverse-edge diagonal closed flip path does not occur on the square, so the third-order ground shift is zero.

The existing source s0 has norm²4, and H1s0 has norm²16. The original uniform longitudinal next-neighbor observable differs from its aligned value by-8 on s0 support and by-16 on H1s0 support at L6,8,12. The support calculation uses actual physical Hamming distances at separation2, retaining periodic geometry. Replaying gives exactly zero residual for deltaO H1s0/64=-H1s0/4. This verifies the stated second-source algebraic contribution and its normalization with existing microscopic O and V; it does not introduce a chosen extra interaction/source. By itself this support script does not derive every canonical source-dressing term, ground-state normalization correction, or higher-order detector vertex. Such claims must retain their separate perturbative derivation.

The relative-space host and side coefficients concern the scaled excitation expansion8+lambda H1+lambda²H2+lambda³H3 at small lambda and fixed periodic tube length. A second-sheet pole/resonance calculation based on a limit of this truncated operator requires its own analytic continuation and uniform-error argument. The resonance calculation was outside this requested check and is not certified here. No native full-H resonance width, bulk3D mode, physical scalar or operational detector identification follows merely from this finite projection.
