# G_Newton self-consistency: dimensional family and conditional action comparison

**Claim type:** bounded_theorem (supplied conditional scope; no audit status change)
**Primary runner:** `scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py`

This source correction withdraws the former dimensional-uniqueness claim P1 and
its claimed non-derivability proof P2. It does not change an audit verdict.
The companion is `scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py`.
Its results concern supplied units and explicit action functions, not a derivation
of gravity from the lattice baseline.

## Exact dimensional family

Let a, c, M, hbar have dimensions L, L/T, M, ML²/T respectively. For
G = a^p c^q M^r hbar^s, the required dimensions L³/(MT²) give

    p + q + 2s = 3,   r + s = -1,   -q - s = -2.

Solving gives the complete real-exponent family

    (p,q,r,s) = (1-s, 2-s, -1-s, s).

The integer solutions are the same formula with integer s. In particular,
a c²/M, hbar c/M², and a² c³/hbar all have the required units. The last
has no explicit M factor, but hbar carries mass units. The old search box
[-3,3]^4 found four points of this family; it never proved uniqueness.
Equivalently G=(hbar c/M²) F(a M c/hbar), where dimensions alone leave
the dimensionless function F unrestricted. Restricting to monomials leaves
an arbitrary exponent and coefficient. An additional relation among scales
or a dynamical normalization is needed to select a value.

The numerical substitution hbar=1.054571817e-34, c=299792458,
M=2.176434e-8 gives a value near the historical G=6.67430e-11.
This is a rounded Planck-anchor consistency check. A Planck mass defined using
G cannot independently predict G. These anchors are supplied, not derived.

## Green-kernel diagnostic and normalization premise

For the supplied cubic Laplacian symbol 2(3-cos k1-cos k2-cos k3), the
companion removes the zero Fourier mode on finite periodic cubes. It solves
(-Delta)G=delta-1/L³ with zero mean. At r=4 and L=16,24,32,48 it checks the
same positive, increasing finite values and same numerical bound used before.
These observations do not prove the infinite-lattice large-distance asymptotic:
taking L to infinity at fixed r is different from taking r to infinity.
If a separately justified kernel asymptotic G(r)~1/(4 pi r) is supplied,
then 4 pi r G(r) tends to 1, not to 1/(4 pi). Its coefficient alone does not
identify a gravitational source normalization, action, or SI Newton constant.
No infinite-volume or continuum theorem is certified here.

## Correct action comparison

The complete `action_value` function in `scripts/action_universality_probe.py`
evaluates `valley_sqrt` as L(1-sqrt(f)) for f>=0. Its normalized depth
1-S/L is sqrt(f). Valley-linear L(1-f) has depth f. The previously printed
L sqrt(1-f) instead has depth f/(1+sqrt(1-f))=f/2+f²/8+O(f³), so its leading
order is one, not one-half. These identities hold for positive weak f<1.

The geometric spent-delay branch of
`scripts/valley_linear_same_harness_compare.py` is a distinct function:

    dl=L(1+f), S=dl-sqrt(dl²-L²)
      =L[(1+f)-sqrt(2f+f²)],
    1-S/L=sqrt(2f+f²)-f ~ sqrt(2f).

Thus both the geometric branch and the `valley_sqrt` model have order-one-half
depth, but they are not identical actions. The existing
`scripts/frontier_weak_field_action_square_root_placement_correction_2026_07_26.py`
already records this distinction. The dimensional table's certificate has a
hardcoded scalar comparison; it is not the evaluated action implementation.

The companion proves these depth identities and leading orders symbolically.
For f=M u with fixed positive u, they are action-depth orders in M. Turning
them into a centroid, force, or deflection exponent needs the actual transport
and readout hypotheses. No such universal response law is asserted here; no
expensive transport replay is claimed by this companion.

## Open composition obligations, not a no-go theorem

To derive Newton gravity in the parent chain one must justify an operator and
source normalization, the composition of the chosen Born-density source with
that operator, the test-mass response law, and the dimensional anchors. Here
these are assumptions/open obligations. Multiple model choices and a missing
ledger title do not prove that no selection theorem exists. A status string
also does not prove that the premises of a cited result compose.

In particular diag(|psi><psi|)=|psi|² for pure states, and the diagonal of a
mixture is the mixture of their densities. A coherent pure state can have the
same site density as a mixed state while their off-diagonal entries differ.
This finite identity supplies no gravitational mass-source identification.

The old helper's literal-True synthesis and ledger-title absence checks are
removed, not replaced by unconditional PASS. The original run had three missing
ledger-file failures; its log is preserved in the review packet. The revised
helper has no ledger runtime input and makes no retention or absence claim.
Only computed exact identities and the explicitly finite diagnostics count as
checks. Its PASS total is not a physical closure or audit verdict.
