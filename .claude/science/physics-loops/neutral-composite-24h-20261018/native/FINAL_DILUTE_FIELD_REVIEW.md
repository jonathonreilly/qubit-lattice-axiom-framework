# Native dilute field: final focused review

Disposition: PASS, conditional on the explicitly inherited uniform fixed-order native normal-form and single-feature results. No required correction found in the reviewed integration. No formal audit, repository edits, or microscopic eigensolve.

## Independent exact uniform-mode control

I independently counted excluded translations as finite subsets of Z², without building any many-spin Hilbert space or reusing the helper's bit-mask enumeration. For horizontal motif syndrome Sx={(-1,-1),(-1,0),(1,-1),(1,0)}, vertical Sy={(-1,-1),(0,-1),(-1,1),(0,1)}, and the Manhattan radius-two ball D2, forbidden translations are Sx-So+D2.

For another horizontal motif their row counts are 3,5,7,5,7,5,7,5,3, totaling 47. For a vertical motif they are 4,6,8,8,8,8,6,4, totaling 52. There are exactly 99 exclusions per label. The same counts apply on the tested periodic grids R=10,14,18, with no wrap identifications; I also checked R=30. The relation is symmetric because the buffer is a symmetric Minkowski dilation.

There are N=2R² motif labels and f0=1/sqrt(N). Each allowed unordered pair is unique and receives amplitude 2/N. Thus

 ||(B0†)^2 Omega||² = 2(1-99/N)=2-99/R².

After lowering, every one-motif amplitude is multiplied by 2(N-99)/N=2-99/R². Therefore the FULL vector error relative to 2 B0†Omega is exactly 99/R², not just a selected amplitude deficit. At R=10,14,18 the errors are 0.99, 0.5051020408163265, and 0.3055555555555556; the squared norms are 1.01, 1.4948979591836735, and 1.6944444444444444. Large finite errors are explicit and compatible with the asymptotic bound; these grids do not demonstrate a small CCR error. The code's orthogonal k=1 mode uses the same label normalization and its ideal lowering target is correct.

## Integration checks

The complete-syndrome projectors preserve monotone grading. Bounded incoming multiplicity gives O_m(1) packet-operator norms, and collision counting gives full-vector rather than only adjacent-matrix-element estimates. The corrected local internal transition construction has explicit initial/final projectors; it does not silently replace an arbitrary vector with a local physical operator. Fixed-order finite pattern support, including Gram-correction paths and one further retained action, is sufficient for the expanded incompatibility relation. Keeping both orientations locally avoids unjustified inversion of the small orientation gap into a local transform.

The common exact-ground rotation is sound: with v=cg+sh and ground energy removed, Hv=s Hh. A two-dimensional rotation sending v to g differs from identity by O(s), and its commutator with H is bounded by a constant times s||Hh||=O(delta). This remains true if Hh has components outside span(g,h); they are accounted for in the rank-two commutator. If s=0 no rotation is needed. Applying this rotation once to the entire embedding avoids an extensive-H bound and repeated-source amplification. Source changes from that rotation are covered by the stated conservative R³ lambda^(M-14) estimate.

For fixed m, exact Q-cluster projectors use the order-lambda^4 separation, not the much smaller internal orientation spacing. The relative-Q estimate is essential on the enormous grid: the original whole-N0 bandwidth argument valid only for p<2 would not justify R~lambda^-14. The proof explicitly invokes the later arbitrary-polynomial relative-bound extension, so it does not make that substitution. The exact spectral clusters are filtrations, not an assertion of exact microscopic particle-number conservation.

The source argument now controls both grades: exceptional centers lie near an initial defect and, for the reverse transition, a final defect. Bounded incoming and outgoing degrees give the required finite-sector Schur bound. Lower source terms are diagonal through order below ten; the order-six Q rotation of the order-four source first contributes at ten and is included in g. This prevents an earlier filtered raising contribution. One must retain this matched source reduction, as the proof does. Uniform finite-sector operator bounds allow composition of the full-vector source estimates. The two additional occupation levels correctly handle same-sign products without a spurious top-cutoff CCR failure.

## Scales and numerical scope

I replayed neutral_dilute_field_scaling.py. The reported exponents are correct: contact 4+14-16=2; global tail 80-28-16=36; source/projector 80-14-42=24. Both dispersion errors become O(lambda²) for q~lambda² on time J^-1 lambda^-16. Momentum rounding is smaller. Keeping the complete common rest energy is necessary and is explicitly required.

The scaling helper checks a specified leading two-orientation coefficient matrix; it does not compute all retained h_M corrections, solve the microscopic Hamiltonian, or establish the theorem numerically. Its docstring and the proof maintain that distinction. The sparse motif helper is likewise exact aligned-column algebra, not spin ED. The full conclusion remains a prepared, fixed-occupation, finite-mode, spectrally filtered nonrelativistic limit. No finite-density, unrestricted CCR, relativistic, thermalization, or observation claim is made.

## Reviewed SHA-256 identities

- `NATIVE_DILUTE_FIELD_PROOF.md`: `2b68c84734aef3c89aa5944fae252a6edfc418771c081f91f28dea0b25187e67`
- `neutral_cluster_fock_control.py`: `edb0a66158e90693d5d2c6ae1868e42365facb400c0ecc02669a20d9c434dd39`
- `neutral_dilute_field_scaling.py`: `2d7033762bd8aa1ffecf5906eb6ab26f3d77656b76015ee0aeea0a54def9ee09`
