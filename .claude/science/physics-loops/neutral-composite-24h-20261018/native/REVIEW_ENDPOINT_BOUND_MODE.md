# Final focused endpoint bound-mode review

Disposition: PASS. No material source correction found. This confirms the exact K1 sector/channel result and original excess-readout vertex, not a full-H bound particle or finite-droplet theorem. No repository edits, audit or landing performed.

## Sector and exact graph

The one-wall-per-column, common-orientation sector is explicitly supplied. On infinite longitudinal chains a transverse spin flip can preserve wall count only by moving an existing wall; no available column can remove two walls to compensate creation elsewhere. Thus exterior uniform columns do not couple at K1, and the native fixed-column height graph is invariant at that order. This is different from a finite droplet with two walls per column, where annihilation and other processes can occur. The canonical note retains this distinction.

Physical -XX amplitude is -1, while -YY amplitude is the product of the two physical Z signs. Equal-height pair motion and mixed-height swaps therefore have the stated different Y signs. The four-ray plus two-contact graph and its equal translation-orbit norms agree with the independent exact adjacency proof. Duplicate physical moves correctly add in the COO matrix. The normalized alternating Y-ray combination cancels the diagonal contacts, leaving hopping -2gamma and flat coupling -4gamma. Its exact bound vector has flat amplitude 1/sqrt(3), ray-channel amplitude 2*3^(-n/2)/sqrt(3), and eigenvalue -8gamma/sqrt(3). The remaining channels do not undercut it at k=0; continuity supplies only the asserted near-zero isolation, not a global Brillouin-zone claim.

The 8Jz is the H0 four-wall energy relative to the supplied boundary-sector reference. Higher-order energy costs of maintaining semi-infinite flipped columns in a transverse environment are not controlled by this K1 result. The note does not interpret that boundary sector as a prepared finite-energy full-H particle.

## Physical quarter-turn phase

The new phase check is correct. A spin rotation taking X to Y and Y to -X multiplies a down-spin change relative to the up reference by i. On a canonical height configuration relative to the flat reference, the number of changed spins is sum h_c, so its relative phase is i^(sum h_c). Reachable configurations have even sum, giving (-1)^(sum h_c/2), exactly the runner factor. A common height translation changes that sum by four and leaves the phase unchanged. Thus the quotient is consistent. On ray n the phase is (-1)^n, while the spatial quarter-turn exchanges X and Y ray families. Their explicit alternating signs make the bound vector even. Diagonal-contact amplitudes vanish in this state and cause no exception.

For the infinite boundary sector, this is a relative phase convention fixed by the flat configuration, equivalently obtained with a symmetry-preserving finite longitudinal reference before taking the height limit. No divergent infinite product phase is needed. The statement is only about the combined axial lattice/spin symmetry; it does not establish full spatial rotational or Lorentz scalar behavior.

## Original readout and normalization

The single-wall distance-two excess comes from exactly two crossing bonds, yielding -2[exp(iph)+exp(ip(h+1))]=-4cos(p/2)exp[ip(h+1/2)]. Summing the four relative wall positions gives 4 on the flat state and 4cos(pn/2) on each ray configuration. With the exact probabilities, this sums to F(p)=4(1+cos(p/2))/(5-3cos(p/2)). The inter-fiber internal vectors are identical in the chosen center gauge, so this is the bound-band form factor, not merely a diagonal expectation at one momentum.

The vertex -4cos(p/2)exp(ip/2)F(p) is unnormalized and obeys V(-p)=conjugate(V(p)). At zero momentum it is -16 times identity in this height sector and gives no internal inelastic excitation. Finite p transfers center momentum between nearby bound states; it is not vacuum creation. The canonical note explicitly retains the localized excess subtraction for an otherwise infinite observable and does not hide a volume-normalization factor. The constant -8 per finite interval column of length at least two is also correctly checked.

## Evidence and limits

The runner controls the analytic vector and Fourier factors at three height cutoffs, checks 4L+3 states, verifies the physical rotation phase, and compares the original form factor. Its finite-cutoff residual tolerance scales with the exact exponential tail. The physical-bit droplet checks verify distinct non-rigid endpoint targets and the four-targets-per-internal-edge norm count; they do not equate leakage with a decay rate. The supplied successful aggregate replay and independent graph/COM proofs provide appropriate evidence; no redundant eigensolver replay was needed.

The source inputs bind the proof and model helper. Existing independent checks were reused. No interaction, mass parameter or detector coupling is added. Higher-order mixing, finite paired ends, larger cross sections and preparation remain open; no stability, fermion, gravity or cosmological identification is inferred. Endpoint-height extensions beyond this checked four-column block were not reviewed.

## Source hashes

- `docs/NATIVE_ENDPOINT_BOUND_MODE_NOTE_2026-10-18.md`: `75cbd534d28f7f9857ceccfd548c5ff64882013cc5c748c4a483c342b4261cfe`
- `scripts/native_endpoint_bound_mode.py`: `4c816491a51650907a3309915efa40a4b2e06fab53d485e236ee8af1713649f7`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/ENDPOINT_BOUND_MODE_PROOF.md`: `6550ac62b55a91e73b03f7fa042b9a750788595bdb8f18820d7846690ec8aca7`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_endpoint_model.py`: `88c0293518f04cc89047a0c35935896cac6b647873a2d3716d6c7c27b6454159`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ENDPOINT_HEIGHT.md`: `364129ae9b7878e17f4e7a6f9584b64e584e0a972c43cc607685a2eac3bfdc55`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FOUR_ENDPOINT_BOUND.md`: `b0d7474ca910d9cd5927d33ce2b0b4d7e65710caf4373703647e59b954e177ae`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ENDPOINT_COM.md`: `76734343424d82a2e71f1912266bab1261968d8a1747e2a33bfcebe3f4ac5432`
- `outputs/native_endpoint_bound_mode/result.json`: `92fcd9705d770cbd99fcc510d315829f12f47211b6e999912cfbb7414ccf4d45`
