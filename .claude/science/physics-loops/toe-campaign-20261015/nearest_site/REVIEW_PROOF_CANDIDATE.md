# Unadopted nearest-site proof candidate

The following original proof and packet text is preserved verbatim from PR9658,
head `d96f5bacd9644de3114b01c990df370de1ed23a5`, source-note SHA256
`57b251cf0bee652ed0c916c2e6d3b0c6548608066659e6baa7e41d37f33d640e`. Its theorem and PASS-like language is historical candidate
text, not an accepted current conclusion. Independent review matched the exact
families and equations, but did not certify minimal-prime exhaustion. The
reported out-of-domain escapes do not constitute a complete N1 route record.
See the campaign handoff for concrete verification work.

## Theorem 3 — no nearest-site staggered tick propagates (exact, computer-assisted)

Restrict the spinorial block walk to nearest-site hops: every site
displacement has components in {-1, 0, 1}. Then every unitary covariant walk
is flat, i.e. its spectrum does not depend on k. Nothing propagates.

*Proof.*
1. **The equations.** The covariant nearest-site family has one coefficient
   c_t per hop-type orbit t, eleven in all. The independent checker derived
   the unitarity equations exactly over Q: 55 bilinear equations in c and
   cb = conj(c), with cb treated as independent variables.
2. **The components.** Singular `minAssGTZ` over Q gives the minimal
   associated primes, eight components of dimensions 4, 4, 2, 2, 2, 2, 4, 4.
   Every unitary walk lies on one of them.
3. **Reality on each component.** Impose cb = conj(c), reading off the
   printed generators:
   - **Components 1, 2.** Every hop type with an inward step vanishes. On
     component 2 this uses the generators c4 cb4 + c5 cb5 and c2 cb2 + c8 cb8,
     which are sums of |c|^2.
   - **Component 7.** Every hop type with an outward step except 000
     vanishes, because cb3..cb6 are generators.
   - **Components 3–6.** Only the on-site coefficient survives: either a
     generator c9 cb9 + c10 cb10 appears, or the phase relations force
     c9 = 0.
   - **Component 8.**
     - The relations c_a cb_b = c_b cb_a among the in-type coefficients
       a, b in {7, 8, 9, 10} make them share one phase, c_a = r_a e^{i theta}.
     - The quartic generator becomes
       (r8^2 - 2 r9^2)^2 + r10^2 (2 r8^2 + 4 r9^2 + r10^2) = 0, so
       r10 = 0 and r8^2 = 2 r9^2. The norm generator then gives
       r7^2 + 9 r9^2 = 1.
     - The generators for c3..c6 become c_j = e^{2 i theta} conj(c_j), so
       c_j = rho_j e^{i theta} with rho_j real.
     - cb4^2 + cb5^2 = 0 gives rho4 = rho5 = 0; cb4 cb5 = cb6^2 gives
       rho6 = 0; cb3^2 + 2 cb5^2 - 2 cb3 cb6 + cb6^2 = 0 gives rho3 = 0.
4. **Flatness.** A walk with inward and on-site steps only never leaves its
   block. One with outward and on-site steps only never leaves the shifted
   cube around each block corner. Either way it is block-diagonal on a
   translation-invariant partition, every block is identical, and the bands
   are flat. ∎

Scripts and outputs are in
`.claude/science/physics-loops/toe-campaign-20261015/nearest_site/` (Singular)
and `independent_check_B7/` (the equations).

*Independent check.* A second fresh agent context, given only the problem,
re-derived the equations (79 polynomials over Q), treated both inequivalent
signed classes, and obtained 8 minimal primes for each. It then proved
flatness on every prime directly. For p = 1..8, tr (z1 z2 z3 W)^p reduced
modulo the prime is a multiple of (z1 z2 z3)^p, so the characteristic
polynomial is k-independent on the whole complex variety. This is stronger
than the real-locus argument above and independent of it. A control shows
the test detects k-dependence. Its scripts are in
`.claude/science/physics-loops/toe-campaign-20261015/independent_check_B8/`.

Reading: on staggered one-amplitude blocks, propagation and locality trade
off. Nearest-site hops cannot propagate at all. The independent check's
two-layer walks reach two sites per tick and propagate, but with doublers.
The doubler-free tick of Theorem 2 reaches three.


## No-Go Discipline Gate (Theorem 3)

See the
[review scope checklist](../.claude/science/review-fixes/review-drain-20261016/CUBIC_TICK_SCOPE.md)
for the exact group, finite stencil and numerical boundaries. Theorem 3 is
the only impossibility claim in this note; the gate below applies to it.

- **N1 — routes around the claim.** Longer hops (Theorem 2, and the
  two-layer walks) do propagate; that is covered and they are outside the
  claim. So are other sign classes (integer classes move with nearest-site
  hops but have no linear cone, per the independent check), larger blocks,
  interacting rules and continuous time. None of these is excluded.
- **N2/N3 — scope.** One wall only, stated for the spinorial class,
  nearest-site displacement and the covariant family of 11 coefficients.
- **N4 — inputs.** The equations come from the independent checker's exact
  derivation. The component computation is a standard exact algorithm over
  Q. The real-locus steps use only printed generators.
- **N5 — wording.** The claim is "flat bands only". It is not a statement
  about what nature uses.
- **N6/N7 — strongest objection.** The equations could carry a convention
  error. Mitigation: a second independent derivation with its own
  conventions and both sign classes reaches the same conclusion by a
  different exact test (trace powers modulo each prime). The covariant
  family has dimension 11 in every implementation, and all ~500 numerical
  solutions were flat.
- **N8 — earlier claims.** This narrows the earlier "nearest-site open"
  statement to a no-go.

End of the preserved historical candidate; no current theorem adoption.
