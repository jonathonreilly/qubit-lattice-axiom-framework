# Goal: derive (or otherwise retire) the kinetic-isotropy primitive

**Owner request (2026-06-09):** "can we avoid accepting the time primitive
(derive it or otherwise get there), reducing the framework to 3 axioms and ONE
primitive." The ruler (`scale_reference_primitive`) is explicitly OFF-target.

**Target:** the approved `kinetic_isotropy_primitive` — the OS0 kinetic-form
isotropy `c_t = c_s` on `Z^3 x Z_tau` ("one tick is one edge in FORM, not only
in spacing").

**Acceptable end states (in descending order of strength):**

1. `c_t = c_s` derived as a theorem from the current grown surface
   (license reading + per-plaquette machinery + durability theorem + retained
   single-clock results) — primitive retires.
2. The primitive's content decomposed into {calibration convention (compensated,
   species-anchor / Y0 class) + theorems + named artifact-grade residual atom}
   — primitive shrinks to the residual atom or reclassifies as convention.
3. Sharpened independence: an honest proof that the GROWN surface still does
   not fix `xi := c_t/c_s`, with the missing premise isolated more precisely
   than #3360 (which predates the license reading, per-plaquette, durability,
   and the spacing-tie renaming verdict).

**Anti-goals:** no new axiom, no new primitive, no Tier-A admission proposal
without owner sign-off, no rescue of the claim via empirical comparators.

**Key prior art:**
- `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (the target's own wording).
- `KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md` (#3360):
  independence relative to {positive transfer, RP, single-clock product,
  6-NN reachability, Record/readout, cubic spatial symmetry, scale}. Its N7
  steelman names this campaign's door: "a future retained dynamics could derive
  the same kinetic isotropy and retire the primitive."
- `SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`: spatial O_h leaves
  exactly TWO quadratic invariant coefficients; 4D hypercubic collapses to one.
  The missing generator is the time<->space exchange.
- `MIN_TIME_STEP_TIED_...NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md` is
  `audited_renaming`: the spacing tie a_tau = a_s closes "only after a
  renaming/definition". Re-audit door (auditor's own words): "Re-audit if a
  retained bridge theorem derives the record/update tick as the time
  coordinate rather than defining it."
- `PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`:
  D2 CONSUMES the primitive ("one tick is one edge in form" => action terms =
  one-tick dependency sets). CIRCULARITY HAZARD: any derivation of the
  primitive must not route through notes that cite it.
