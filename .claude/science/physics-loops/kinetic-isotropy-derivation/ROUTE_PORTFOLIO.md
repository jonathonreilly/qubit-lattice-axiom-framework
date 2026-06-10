# Route Portfolio — kinetic-isotropy derivation loop

Scored by likely claim-state movement. The #3360 independence is relative to a
list that does NOT include: the license's strict R-local update FORM, the
unitarity of the one-tick update, the fermionic/chiral realization, or the
durability theorem. Routes consume exactly those.

## R-A (PRIMARY): index-quantized saturation — "strict license + unitarity
## quantizes the chiral velocity"

**Chain:**
1. The retained license (`lattice_nn_light_cone_note`, verbatim: update uses
   "no arguments outside the listed dependency set") is STRICT locality of the
   one-tick update.
2. A Hamiltonian-generated update `e^{-i a_tau H}` with any nonzero NN hopping
   has nonzero amplitude beyond radius 1 in one tick (exact: Bessel expansion /
   polynomial degree) — it VIOLATES the strict license. So a unitary one-tick
   update conformant with the license is a strict radius-1 QCA. (This is the
   same strict reading the per-plaquette enumeration already used at the gauge
   level — D4 excluded non-licensed loops.)
3. **Monomial lemma (exact, 3 lines):** a one-mode Bloch amplitude u(k) that is
   (i) a finite Laurent polynomial of degree <= 1 (radius-1 strict locality)
   and (ii) unimodular for all k (unitarity) is a monomial `c z^n`,
   n in {0,+1,-1}. Hence omega(k) = nk + const EXACTLY: the velocity of a
   decoupled chiral mode is QUANTIZED to n edges/tick. No tunable coefficient
   exists — unlike continuous time (H = kappa sin k, v = kappa tunable).
4. A genuinely chiral carrier component (nonzero index; the framework's
   staggered/epsilon-chirality realization) has n != 0, hence |v| = 1 exactly:
   the chiral mode SATURATES the retained reachability front. One tick is one
   edge IN FORM — c_t = c_s derived at the fundamental/chiral normalization
   point. Mass terms mix +1/-1 shift components and reduce IR velocity
   dynamically (consistent; the kinetic FORM normalization is the chiral/UV
   statement, which is exactly what the primitive declares).

**Consumes:** license (retained) + Quantum axiom (qubit carrier) + unitarity
provenance (CHECK: which row supplies unitarity of the inter-record update —
possibly conditional) + chirality/staggered realization (EXISTING gate — adds
no new node; Koide-subsumption shape).
**Expected outcome:** xi = 1 as a conditional theorem under existing gates;
primitive's content relocates onto already-registered surface. Strongest case.
**Failure modes:** (a) unitarity of the fundamental update not on the surface
(then: theorem stays conditional on a named unitarity premise — still movement);
(b) the index-0 trap: gapless points of index-0 QCA have TUNABLE velocity
(split-step witness — MUST be exhibited as the hostile check); chirality
(nonzero index) is load-bearing and must be tied to the staggered gate
honestly; (c) d=3 scope: per-direction winding for free QCA — state scope
honestly (exact in each lattice direction; full 3D isotropy statement via O_h
+ per-direction quantization).

## R-B: licensed-kernel two-coefficient analysis (independence sharpening)

Characterize ALL quadratic licensed one-tick kernels (scalar witness): allowed
terms = temporal edge (self), spacetime diagonal (NN at previous tick),
same-time spectator products. Compute the dispersion family; show xi sweeps a
continuum => the LICENSE ALONE does not fix xi even though #3360 never tested
the license form. Honest negative leg of the cycle; also exhibits WHY the
bosonic witness escapes R-A (no unimodularity per mode — positive transfer
instead of unitary).
**Expected outcome:** sharpened independence + the exact boundary line:
quantization is a fermionic/unitary phenomenon. Supports R-A's conditionality
statement.

## R-C: canonical temporal normalization for first-order carriers

For a Grassmann/staggered (first-order) action, the temporal kinetic
coefficient is fixed by the canonical anticommutation normalization (the
Quantum axiom's M_2(C) unit) — psi-bar d_tau psi has unit coefficient after
the CAR normalization; no c_t freedom exists for the realized carrier. The
residual freedom is the spatial hopping magnitude kappa_s; spatial O_h forces
kappa_x = kappa_y = kappa_z; R-A then quantizes it. R-C makes R-A's "c_t side"
exact and shows the two-coefficient counting of the anisotropy gate collapses
differently for first-order carriers (1 coefficient, not 2).
**Expected outcome:** exact support feeding R-A.

## R-D: saturation via record-tick identification (the auditor's door)

The `audited_renaming` verdict on the spacing tie names the re-audit trigger:
"a retained bridge theorem derives the record/update tick as the time
coordinate rather than defining it." If R-A lands, the chiral carrier moves
exactly one edge per tick — the tick-to-edge identification becomes the
carrier's OWN transport fact, not a definition. Map this consequence
explicitly (do not claim the re-audit; record the door).
**Expected outcome:** consequence map; possible later re-audit of the renaming
row.

## R-E (fallback): grown-surface independence re-run

If R-A's load-bearing premises fail verification, re-run #3360 against the
grown surface mechanically (license form, durability, per-plaquette-minus-D2)
and ship the sharpened independence with the missing premise isolated as "the
unitarity/chirality of the realized carrier".

## Dramatic-step gate

R-A changes the lane state (primitive derived-or-relocated). R-B/R-C alone
would be support; ship them only fused into the R-A cycle, not as separate
churn PRs. R-E only on R-A failure.
