---
claim_id: gauge_wilson_pw_compression_shell_and_energy_path_bounds_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_compact_cube_finite_qubit_cutoff_bounded_theorem_note_2026-09-07
claim_scope: "Supplied SU3 Haar compression identities, sharp shell eigenvalue and energy-controlled distinct-link path bounds; formal negative certification deferred."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

This bounded supplied-model result retains the complete compression, shell, kernel/eigenvalue and energy/path proof. Formal universal negative-classification and negative-convergence certification are **DEFERRED**, because the original N1 packet did not provide the required independent attack-family coverage. This procedural boundary does not invalidate the analytic identities. No axiom-selected carrier, hardware preparation or unbounded kinetic-form transfer is established.

The [actual cutoff and electric spectrum source](GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the full-irrep Haar cutoff and electric energy. The static-source trial is context only: `GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md`.

The [finite runner](../scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py) checks one actual R=1, 57×57 matrix (19 link states and 3 colors), with 16 mathematical checks and one resource check. Its [capture destination](../logs/runner-cache/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.txt) is an execution artifact, not an all-R or spatial-lattice proof. The [exact original recovery](work_history/review_loop/pr8031/README.md) preserves every original proof and failure. Historical native/root reviews are not a new independent certification; root's derivation was informed by the native stronger path bound.

# Supplied Peter–Weyl compression, shell identities and energy/path bounds

The complete native positive compression and energy/path argument is retained below with explicit supplied-model scope; its negative argument remains complete in the exact archive. Historical discovery and review provenance is preserved in the recovery archive; it is not a current certification.

## 1. Tensor trace-square identity

Let H be a nonzero finite-dimensional Hilbert space, Q any Hermitian operator on H, and T any traceless Hermitian 3-by-3 matrix. Write Qbar=Q tensor I3 and Tbar=I_H tensor T. Direct expansion and factorization of the tensor trace give

 Tr(Qbar+Tbar)²=Tr Qbar²+dim(H) Tr T²,

because the cross term is2Tr_H(Q)Tr_3(T)=0. Replacing Tbar by −Tbar gives the same square contribution. This is a tensor trace identity; no transporter covariance or unitary-similarity hypothesis is imposed in this live statement. The original negative proof, including its conditional similarity and character arguments and one-sided-isometry corollary, is preserved completely in the exact recovery archive. Its formal negative certification is deferred, not mathematically refuted.

## 2. Actual Haar link and full-irrep cutoff

On L2(SU3) tensor C3 let (mathsf U psi)_i(g)=Σ_j g_ij psi_j(g). It is genuinely unitary. Let P_R be the orthogonal Peter–Weyl projection onto all matrix coefficients with labels p,q>=0 and p+q<=R, tensored with color identity. It commutes with both endpoint actions. Put U_R=P_R mathsf U P_R, acting on Ran P_R, and

 D_R=I_(Ran P_R)−U_R* U_R=P_R mathsf U*(I−P_R)mathsf U P_R.

Thus0<=D_R<=I. This is compression of the actual Haar multiplication operator, not a freely chosen finite quantum-link representation. Gauge covariance remains exact because P_R is a full-irrep projection.

Fundamental fusion is

 (1,0) tensor(p,q)=(p+1,q) plus(p−1,q+1) plus(p,q−1),

with invalid labels omitted. Hence multiplication by any g_ij takes p+q<=R−1 entirely into p+q<=R. The same holds for conjugate multiplication using the conjugate fusion rule. Consequently D_R annihilates the interior Ran P_(R−1). Since D_R is positive selfadjoint,

 0<=D_R<=T_R:=P_R−P_(R−1),                  (1)

and D_R=T_R D_R T_R. The left defect I−U_R U_R* has the same shell support by conjugate fusion.

The norm is sharply1 for EVERY R>=0. The normalized highest-weight matrix coefficient

 psi_R(g)=sqrt(d_(R,0)) g_11^R, d_(R,0)=(R+1)(R+2)/2,

belongs to(R,0), with norm1 by Schur orthogonality. Every g_i1 g_11^R is a matrix coefficient of Sym^(R+1)(C3), because all right tensor indices are the same first basis vector. This symmetric tensor representation is the single irrep(R+1,0); no antisymmetric/lower component survives. Thus U_R(psi_R tensor e1)=0. Since the original mathsf U is unitary, D_R has eigenvalue1 and ||D_R||=1. In particular ||(mathsf U−U_R)P_R||=1; this is an exact norm identity for the supplied compression. The associated negative convergence certification is deferred. At R=0, U_0=0 and the energy denominator below is zero, so that case must be excluded from the low-energy bound.

## 3. Energy-priced one-link defect

For a>0 and integer R>=1 define

 g_(R−1)=[R²−floor(R²/4)+3R]/a.

This is the exact minimum electric energy on the shell p+q=R, from E(p,q)=[p²+pq+q²+3p+3q]/a and maximal pq=floor(R²/4). Therefore T_R<=K/g_(R−1) on Ran P_R, and for a normalized state psi already in that cutoff space, with arbitrary reference/color entanglement,

 ||(mathsf U−U_R)psi||²=<psi,D_R psi>
 <=<psi,K psi>/g_(R−1).                       (2)

The expectation version holds for a mixed state by purification. It compares the exact unitary output to the unnormalized compressed output. It does not assert a deterministic normalized finite channel. The bound tends to zero for uniformly bounded electric energy because g_(R−1) grows quadratically in R, despite the exact norm-one defect on high-energy shell states.

## 4. Simple paths with shared color and arbitrary entanglement

Consider L DISTINCT links, each acted on once by mathsf U_e or its adjoint according to path orientation. Write W=U_L...U_1, P=Π_e P_(R,e), and let W_R be the corresponding product of compressed link matrices on Ran P. The color register is shared; its link matrices need not commute. However P_(R,e) acts as identity on color and commutes with every U_f for f≠e. Moving only such projectors gives the exact identity

 W_R=P W P.                                  (3)

For normalized psi in Ran P, the output error is consequently an orthogonal projection loss:

 ||Wpsi−W_Rpsi||²=<Wpsi,(I−P)Wpsi>.

The commuting output projections satisfy I−Π_eP_e<=Σ_e(I−P_e). For a fixed e, move its leakage projector past the later different-link unitaries and use(1) at the e-th step. Its shell projector commutes with all earlier different-link unitaries, so

 <Wpsi,(I−P_e)Wpsi><=<psi,T_(R,e)psi>.

No product assumption on link, color or reference states is used. Combining these identities yields

 ||Wpsi−W_Rpsi||²<=Σ_e<psi,T_(R,e)psi>
 <=<psi,Σ_(path)K_e psi>/g_(R−1).              (4)

Thus a TOTAL path electric-energy budget E gives error at most sqrt(E/g_(R−1)). A PER-LINK energy bound E_link gives the weaker requested sqrt(L E_link/g_(R−1)). A total full-system energy bound E also suffices whenever the supplied potential is nonnegative, since Σ_path K_e<=H. The two budget conventions must not be conflated.

Equation(3) is why an unnecessary sum of L square roots is avoidable. It relies on distinct links; a repeated-link path is not covered by this argument because a projection can no longer be commuted past another occurrence of its own link. It also explains why shared color entanglement causes no extra factor.

If epsilon bounds the right side of(4), the accepted output norm squared is at least1−epsilon. When nonzero, normalizing the projected output gives vector error squared2(1−sqrt(p))<=2epsilon relative to the exact output, where p=||W_Rpsi||². This is a conditioned output statement with its acceptance probability, not an automatic trace-preserving isometry. For general initial states outside Ran P one must additionally price initial projection/preparation; that cost is not hidden here.

## 5. Prior art and precise consequence

Primary quantum-link literature explicitly constructs finite link Hilbert spaces with exact continuous gauge symmetry: Chandrasekharan–Wiese, hep-lat/9609042, https://arxiv.org/abs/hep-lat/9609042 ; Wiese,2107.09335, https://arxiv.org/abs/2107.09335 . Their link entries are operator-valued with modified algebraic relations. Nothing here contradicts that established framework, its gauge covariance, or possible approximation/continuum routes. The historical negative argument concerns simultaneous finite dimension, exact fundamental endpoint covariance and exact matrix unitarity; its formal certification remains deferred. No novelty of a generic quantum-link obstruction or prohibition of unitary time evolution is certified here.

For the actual full-irrep cutoff the theorem identifies the exact boundary defect and a useful energy-controlled approximation. The contextual static-source trial uses an exact unitary open-line identity; transferring its energy estimate to compressed hardware requires an additional energy-form estimate. State-vector approximation alone does not automatically bound an unbounded kinetic-energy expectation. Exact gauge covariance and the supplied-model low-energy transporter estimate are retained. Broader negative convergence certification is deferred. No hardware compiler, continuum identification or axiom-selected cutoff is claimed.

## Appendix A. Additional root-verification details

The historical root proof's conditional character argument and group-convention discussion remain complete in the exact archive. They are not conclusions of this live bounded row. The following supplied-compression and state-comparison details remain affirmative parts of the result.

For inverse link orientation, antifundamental fusion gives the same shell support, and a conjugate highest-column/row coefficient supplies the corresponding sharp witness. With K=-3 Delta/(2a), the shell energy is equivalently e_R=[ceil(3R²/4)+3R]/a=g_(R−1); the expectation bound can be capped by 1. The norm-one witness moves to increasing energy as R grows.

If all distinct path links start in their interiors P_(R−1), every shell expectation vanishes and path action is exact. The weaker telescoping estimate sqrt(L E_path/e_R) is valid but unnecessary; the proved projection estimate is sqrt(E_path/e_R). For p>0, the pure-state trace distance (one-half convention) between the exact output and normalized projected output is exactly sqrt(1−p). E_path<e_R is sufficient, not necessary, for p>0. An implementation still requires a channel or dilation and must price any postselection probability. These are supplied-state mathematical comparisons, not deterministic preparation claims.

## Appendix B. Applicability and deferred certification record

- N1: DEFERRED. No completed five-family negative-certification packet is asserted.
- N2: Historical root/native provenance is retained; it does not establish independent wall attacks.
- N3: The actual Haar full-irrep projection, supplied energy and distinct-link hypotheses are explicit; broader encodings are outside the positive result.
- N4: The tensor trace identity and exact supplied-compression norm identity are retained; the universal negative proof is archived and its certification deferred.
- N5: Executed finite evidence is 16 mathematical checks plus one resource check on the 57×57 R=1 one-link fixture. Per-site and lattice-wide execution are not performed. All-R and path statements rely on the written proof.
- N6: The original R0 tautological-check failure and corrected vacuum-block check remain archived; no evidence is erased.
- N7: No axiom-selected representation, native preparation, repeated-link path bound or unbounded energy-form transfer is asserted.
- N8: Original reviews and present source preparation are not substituted for a completed negative-certification review. The unresolved original branch is retained.
