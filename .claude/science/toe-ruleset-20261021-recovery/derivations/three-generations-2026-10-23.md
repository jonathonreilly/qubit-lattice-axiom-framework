# Derivation: three generations of the 16

## Date
2026-10-23

## Target
Families means the same thing as generations: three copies of one generation's matter content, (u, d, e, nu) + (c, s, mu, nu_mu) + (t, b, tau, nu_tau). The measured facts, used here as disclosed comparators only, are:
- F1. Exactly three light copies: N_nu = 2.984 ± 0.008 (Z width).
- F2. Identical gauge charges. Universality holds to about 1e-3 (tau and mu leptonic widths).
- F3. Steep mass hierarchy: e : mu : tau = 1 : 207 : 3477, u : c : t ~ 1 : 600 : 8e4.
- F4. Neutral interactions conserve family. BR(mu -> e gamma) < 3.1e-13 (MEG II). No tree-level FCNC.
- F5. Family changes only through the charged weak current, by misalignment (CKM, PMNS). CKM is small and hierarchical, with one CP phase.
- F6. Lifetimes differ: e stable, mu 2.2 us, tau 0.29 ps. Owner flagged this as a clue (2026-10-23). It is not independent of F3: with a universal weak coupling, tau ∝ 1/(G_F^2 m^5) (Sargent rule). tau_mu/tau_tau = (m_tau/m_mu)^5 / B(tau -> e nu nu) to about 1e-3. What F6 adds beyond F3 is a qualitative point: heavier copies decay into lighter ones, and the decays go only through the charged current, never through photon emission.

## Premise ledger
- The four axioms, unchanged. The working CL register (zero premise weight).
- CL-1 adopted clauses: cube tick on two tilings, spin-3/2 edge hop, copy mass, lapse in the step, slab tick form, history-level overlap matter weighting.
- The fold result (fold-selection-3d): the mass-angle sign selects one cube fold, its POINT MISFOLDS are the matter fermions (a cube with 5 or 3 units, odd parity), and wall misfolds carry 2+1 modes.
- Spin(10) 16 content, conditional (five modes); the two-16 Spin(12) gap.
- Open dependencies: chirality interacting step; families (this target).

## What was tried (approx. 17 probes) and the shared assumption
Tried:
- dimensions and turns: turn triplets (family-charge-search, family-flux, monopole-families);
- zoom as lattice rungs: zoom-families, generation-rungs, zoom-tower, rung-dimension-chirality, family-register;
- time: record-arrow-family-phase;
- folds and textures: chiral-texture-family (folds, helices, screws as a mass source);
- cell tastes: families-from-tastes;
- slab walls: wall-families;
- path-sum rungs: forced-rungs;
- the copy-mass tower: mass-tower-law.

Shared assumption (families-brainstorm): a family is an exact, symmetric copy of ONE free light field, separated by a lattice quantum number, and all copies are light together. Every one of these failed in one of two ways. Either it gave degenerate or symmetric triplets (no hierarchy, J = 0 by the turn-CP lemma), or it gave the wrong count (1, 2, 4 or 6).

Owner instincts, checked against that list:
- "dimensions": tried only as a symmetry label, which gives degenerate triplets. Not tried as the dimension of an object.
- "zoom / sizes": tried only as free-field rungs. Not tried as STABLE INTERACTING states of different size.
- "time / different frames": tried once (record arrow). Internal clock-locking states were not tried.
- "folds / neighbourhood crystals": tried as mass textures, and once as the matter particle itself (the point misfold). Misfolds of DIFFERENT SHAPES were not tried as families.

## Minimal mechanism (proposed)
Families are three stable misfold classes of the one cube fold, distinguished by the dimension of the misfolded region inside a point-like defect, d_m = 1, 2, 3:
- a misfolded line segment;
- a misfolded plaquette sheet;
- a misfolded cube.

Each is bounded and odd-parity, so it is a fermion. Each carries the same 16 of internal content, because the content sits on the defect's sites, not its shape.

Why this reading might meet F1-F6:
- F1: the count is the number of spatial dimensions, d = 3, which the cone rule ties to the qubit. This is the owner's dimension instinct, read as object dimension rather than as a direction label.
- F2: same content, same charges.
- F3: the energy grows with the misfolded region's dimension. That gives a natural hierarchy, not a symmetric triplet, because the three classes are not related by any lattice symmetry. So the turn-CP lemma does not apply.
- F4: the classes differ in a topological or shape class, so a neutral local process must change the class. That could forbid mu -> e gamma at the level of the rules.
- F5 and F6: the class can change only through the misaligned charged-current mixing. This must be checked; it is not assumed.

## Derivation steps (status)
1. [fold result, bounded] Point misfolds of the selected fold are odd-parity fermions at cost |mu|.
2. [TO TEST] Enumerate bounded odd-parity misfolds by the dimension of the misfolded region. Count the classes that are locally stable, meaning no single admissible local move lowers the energy. Prediction: exactly 3.
3. [TO TEST] Energies: E(d_m = 1) < E(2) < E(3), with ratios set by the rules (not fitted).
4. [TO TEST] Content: each class binds the same mode content, with the same charges.
5. [TO TEST] Selection rule: matrix elements of every neutral local operator (photon-like link coupling, density) between different classes vanish, or are suppressed by the class change.
6. [OPEN] The charged-current mixing angle between classes (CKM-like) is the overlap of their content wavefunctions.

## Decisive check
The decisive check is step 2's count plus step 5's selection rule:
- If the count is not 3, the reading fails at F1.
- If neutral transitions are allowed at order 1, it fails at F4 (excited states would decay radiatively).
- Exposure: the count 3 is known in advance. So the count must come from the stability analysis, not from capping the size by hand.

## Weakest link
Step 2. On the fold crystal, larger misfolds may just be unstable bound states of several point misfolds, which would decay into k point fermions. That decay would not look like mu -> e nu nu. Testing it needs a finite exact enumeration on small tori (4^3, 6^3) of misfold shapes with their fold energies, plus one-move stability.

## Other live options (lower ranked)
- Time and frames: internal clock-locking states. A composite's internal phase locks to period 1, 2 or 3 of the tick (Floquet sectors). Their masses are set by the locking frequency. This needs a reason that only three lock stably.
- Frame or rotation: spinning neighbourhood states with winding 1, 2, 3. Higher windings usually split into units, which fails F6's pattern.

## Status
PROPOSED. A probe is running for steps 2-5: agents/misfold-generations.
