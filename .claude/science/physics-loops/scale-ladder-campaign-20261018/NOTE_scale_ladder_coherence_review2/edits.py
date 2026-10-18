# Proposed old -> new edits for the scale-ladder note (second coherence review, 2026-10-18).
# Generated with exact old strings. verify() checks each old string occurs exactly once in the
# current note, applies the edits in order to an in-memory copy, re-checks uniqueness after each
# step, and writes patched_note_preview.txt next to this file. It never writes docs/.
EDITS = []
def E(tag, old, new, why=""): EDITS.append((tag, old, new, why))

E('F1 claim_scope (8): checker provenance',
  '(8) Independently checked (campaign COROLLARY_check) (its ingredient, the global anticommutation of the dressed axis-C2 lifts, is the checked companion odd-filling theorem):',
  '(8) Checked by a fresh-context agent of the same model family (campaign COROLLARY_check; its ingredient, the global anticommutation of the dressed axis-C2 lifts, is the checked companion odd-filling theorem):',
  "'Independently checked' in machine-readable scope should name the same-family provenance, as the body's Labels line does.")

E('F2 claim_scope Not claimed: phase-2 pointer',
  'a theorem on a common speed across different fields (the campaign\'s conditional, leading-order constraint-closure results are in companion lane notes and are reported here as interpretation), or any physical identification."',
  'a theorem on a common speed across different fields, or any physical identification. The campaign\'s lane results (constraint closure and the walker normalisation, the lattice relabelling arc lemma, doubler gapping, the rung 0 -> 1 registration lemma, the taste searches) are in companion lane notes or campaign evidence and are reported here as interpretation only."',
  'Phase 2 added lane results beyond constraint closure; scope should say all of them are interpretation here.')

E('Q1 campaign length',
  'and report what a 12-hour campaign (2026-10-18) then established.',
  'and report what a two-phase campaign (2026-10-18, two 12-hour phases) then established.',
  'Phase 2 added 12 h (HANDOFF 11:30Z).')

E('R0 rung 0 -> 1 (C6)',
  'The rung 0 → 1 map is an encoding chosen by hand. A uniform one-qubit dynamics producing it is open.',
  'The rung 0 → 1 map is an encoding chosen by hand, and campaign block C6 (checked) found no derivation: the flux is a free sector label of the local fermionization, and no translation-covariant formation rule from an empty start can register a coarse block lattice (summary item 7). A uniform one-qubit dynamics producing it is open.',
  "C6 sharpened this from 'open' to 'not derived, with a registration lemma'.")

E('T1 follow-up intro',
  'A 12-hour campaign converted the strongest probe leads into proofs or decisive computations.',
  'A campaign of two 12-hour phases converted the strongest probe leads into proofs or decisive computations.',
  'Phase 2.')

E('T2 companion PR',
  'the proved lane statements are in a companion lane-theorem PR.',
  'the proved lane statements are in companion lane notes (PR #9718).',
  'Name the PR (plain text).')

E('S0 labels line',
  '"Proved here" means proved in this note and not yet checked. The lane theorems live in the companion lane notes; this list only points to them.',
  "C20's check is recorded in the Independent-check section of its lane note; its folder `C20_check` holds scripts and outputs but no REPORT.md. The lane theorems live in the companion lane notes; this list only points to them.",
  "'Proved here' is no longer used anywhere in the note; C20 is the only 'checked' label without a REPORT.md.")

E('S5 summary item 5: G3/2 scope',
  'Levels that mix in spin-3/2 content are unscreened.',
  'Levels with spin-3/2 content, mixed or pure, are unscreened (B23).',
  "B23 FINDINGS 'Still unscreened' lists pure G3/2 levels as well as mixed ones.")

E('S7 summary items 7-8 rewrite',
  "7. **Phase 2 (campaign blocks C1–C4 and B24; same-family checks where marked).**\n   - **Exact lattice closure cannot reproduce the continuum relabellings (C3, checked; companion lane note).** A translation-covariant lattice relabelling algebra of any range can close exactly, and such algebras exist. But if it matches the continuum at the longest wavelength, the closure conditions force Λ_n/Λ_1 = n − (arc centre) on arcs of momenta. So Λ_2/Λ_1 ≤ 0, against the continuum value 2. The uniform-lapse bracket needs a non-local Leibniz rule (SLAC-type). Exact closure is therefore available only with a spectrum that is wrong beyond the longest wavelength, so the leading-order closure results are the physically meaningful ones.\n   - **The doublers cannot be selectively removed under full O (C1, checked).**\n     - A symmetric pairing mass is all-or-nothing at the eight cube points.\n     - The doublers alone, and ±k* alone, each carry a Weyl dipole π(1,1,1), half a Hall quantum per layer. That is a Z2 obstruction to gapping either set alone into a short-range-entangled state. It is conditional on anomaly matching and on a Hamiltonian reading of the step. A compensating sector is required; the doublers are one realisation of it.\n     - With O broken to a subgroup, selective pairing exists, but ±k* is then not protected.\n   - **Closure fixes the seagull but not the induced 1/G (C2, checked).** In the continuum, within ≤ 2 derivatives, the seagull is the minimal covariant one, but it is not what cures the 06-08 Ward break. Covariant dimension-6 couplings shift the induced 1/G by an O(1) amount on a lattice while respecting closure and Ward. So 1/G needs the complete microscopic action, spectral sum rules or a perfect-action principle.\n   - **The walker's coupling fixes the normalisation of h (C4, checked).** The repo's frame identification g⁻¹ = EᵀE and the normalisation ΛR(0) = 1 set unit matter coupling a_s = 1 by definition. The lapse identity then gives K1 = 4α. The TT coefficient K2 needs one further clause. The repo's statements that α = K/4 gives the walker's top speed for the member's disturbances (block 62 T4, block 134 T4, the 09-25 exact-lattice note) rely on the declared single K; with K1 ≠ K2 the TT speed² would be K2/K1. **Closure with the walker as matter (C4b, checked)** forces γ = a_s K1/K2 = 1, i.e. K1 = K2 in block-62 variables. With the walker's speed 1, both the walker's cone and the TT cone sit at that speed and α = K2/4. Block 62 T4 said nothing forces that value; within these premises (continuum, leading order, the k = 0 species), closure does. The walker also needs the second-order totally antisymmetric spin-connection term to close at the next order. Its first-order lattice form is the repo's block 65.\n   - **Rung 0 → rung 1 is not derived (C6, checked).**\n     - The corner model's 12-corner space, its π-flux background and its block embedding are supplied, and the flux pattern is fixed by design targets.\n     - Local fermionization leaves the flux a free sector label. The symmetry group exists for all 16 uniform patterns, and energetics at the node filling ranks the corner pattern near last.\n     - A registration lemma: no measurable equivariant factor of iid noise, and so no translation-covariant formation rule from an empty start, can register a coarse block lattice or any crystal phase off 2πZ³.\n     - Open routes: emergent corner quasiparticles of a translation-invariant fine Hamiltonian, and fractional-translation encodings.\n   - **Taste enlargement (B24, checked).** No single rotation-invariant translation lattice, at any scale, makes every commuting-C2-pair point T-fixed (exact). Enlarging the taste group moves the bad points to finer momenta, and 0 of 449 classified searched steps pass. The check found one opening: pinning follows the unitary taste lattice and isotropy the spectral one. Where the spectral lattice strictly exceeds the unitary one (transpose or antiunitary-type tastes), the geometric obstruction lifts for most nested lattice pairs. **Block B25 (checked) closes most of that opening.**\n     - **Index lemma (exact).** Tastes with k-independent intertwiners of unitary, transpose, inverse or conjugate kind enlarge the unitary lattice by index ≤ 4, with trivial point-group action on the quotient. The only possible pairs are then (Λ, Λ), (sc, bcc) and (fcc, sc), and all are bad at every scale.\n     - **So a good pair needs tastes with no k-independent intertwiner.** No palette word in a 2,008-word census realises one.\n     - The closest family (2,340 words with k-dependent tastes) gives 0 clean steps.\n8. **Net reading.**\n   - **What the ladder carries.** It carries classes, valley positions and multiplicity structure exactly.\n   - **The common cone.** The only common-cone mechanism found with a derivation is constraint closure. It is conditional and leading-order, and it ties every matter cone to the graviton's.\n   - **The information-minimal target.** One parameter-free step is currently blocked by that rule: no step found passes.\n   - **Open:**\n     - a step whose node quasi-energy avoids the unavoidable D4/D2 points;\n     - a topologically ordered doubler sector;\n     - the induced 1/G from a complete microscopic action;\n     - the dynamics of the rung 0 → 1 map.\n\n     Exact lattice closure with continuum-like relabellings is now known to be impossible (C3).",
  '7. **Phase 2 (C1–C4b, C6, B24, B25; each checked by a fresh-context same-family agent).**\n   - **Exact lattice closure (C3; C3 arc-lemma note).** Take a translation-covariant relabelling algebra of any range that closes within its span with field-independent structure constants, and whose longest-wavelength mode acts nontrivially. Then Λ_n/Λ_1 = n − (arc centre) on arcs of momenta, so Λ_2/Λ_1 ≤ 0 against the continuum value 2. Such algebras exist: exact closure is possible, but not with the continuum spectrum. The uniform-lapse bracket needs a non-local product (anti-aliased SLAC or band-limited). Field-dependent structure functions and enlarged generator sets are not covered.\n   - **Normalisation of h (C4, C4b; C4b walker-closure note).** The walker\'s frame identification fixes unit matter coupling, a_s = 1, by definition (C4). Closure with the walker as matter then forces γ = a_s K1/K2 = 1, so K1 = K2 in block-62 variables. With the walker\'s speed 1, both cones sit at that speed and α = K2/4. This holds in the continuum, at leading order, with isotropic ansätze and the k = 0 species. Within those premises it answers block 62 T4\'s "nothing forces that value". At the next order the walker needs the totally antisymmetric Levi-Civita spin-connection term, whose first-order lattice form is block 65. For spin ½ a connection term absorbs the Kosmann remainder, so {G, G} closes without a triad.\n   - **Doublers (C1; C1 doubler note).** Under full O a single pair condensate is all-or-nothing at the eight cube points, and keeping ±k* gapless tunes one number. The doublers alone, and ±k* alone, carry the Weyl dipole π(1,1,1): half a Hall quantum per layer. So gapping either set alone into a symmetric short-range-entangled state is excluded. This Z2 obstruction is conditional on a Hamiltonian reading of the step and on Hall quantisation. A compensating sector (gapless, topologically ordered or symmetry-breaking) is required. With O broken, selective channels exist, but they do not protect ±k*.\n   - **Seagull and 1/G (C2; campaign evidence, no lane note).** Within ≤ 2 derivatives, closure fixes the seagull: the minimal covariant one. Its tadpole is a pure contact, so it does not cure the 06-08 Ward break, which depends on regulator and measure. Covariant dimension-6 couplings respect closure and Ward and shift the induced 1/G by O(1) on a lattice, so closure cannot fix 1/G.\n   - **Rung 0 → 1 (C6; C6 registration note).** No map is derived. The 12-corner space, the π-flux background and the block embedding are supplied. Local fermionization leaves the flux a free sector label, the PSG exists for all 16 uniform patterns, and node-filling energetics ranks the corner pattern 15th–16th of 16. The registration lemma is exact: no measurable translation-equivariant factor of iid noise registers a coarse block lattice or has Bragg peaks off 2πZ³, so no covariant formation rule from an empty start does.\n   - **Taste routes (B24, B25; campaign evidence).** No rotation-invariant translation lattice, at any scale, makes every commuting-C2-pair point T-fixed (exact). Enlarging the tastes only moves the bad points: 0 of 449 classified survivors pass, and 353 were not classified. Pinning follows the unitary taste lattice and isotropy the spectral one. B25\'s index lemma (exact) shows that tastes with k-independent intertwiners give only bad pairs. A good pair therefore needs tastes with no such intertwiner, and a 2,008-word census realises none. The closest family (2,340 words) gives 0 clean steps. Pinning at C2-pair points is observed (225 of 225), not proved.\n8. **Net reading.** The ladder carries classes, valley positions and multiplicity structure exactly. The only common-cone mechanism with a derivation is constraint closure. It is conditional and leading-order, it ties every matter cone to the graviton\'s, and (C3) it has no exact lattice form with the continuum spectrum. No parameter-free step found passes its selection rule.\n   - **Open:**\n     - exact closure with field-dependent structure functions or more generators;\n     - a step whose node quasi-energy avoids the non-T-fixed C2-pair points (by the doubling corollary, a step with no quasi-energy gap), or that uses tastes with no k-independent intertwiner;\n     - a constructed topologically ordered doubler sector;\n     - the induced 1/G, from a complete microscopic action, spectral sum rules or a perfect-action principle;\n     - rung 0 → 1, via emergent corner quasiparticles of a translation-invariant fine Hamiltonian or a fractional-translation encoding.',
  "Replace accreted phase-2 text: drops the superseded 'with K1 ≠ K2 the TT speed² would be K2/K1' sentence, scopes C3 (field-independent structure constants), scopes C1 (single condensate), adds B25's pinning caveat and B24's unclassified survivors, and replaces the open list.")

E('D1 gravity bullet (C2)',
  'The induced-gravity item is now precise: the 06-08 bubble needs an underived seagull, so the induced 1/G is not fixed.',
  'The induced-gravity item is now precise: the 06-08 bubble needs an underived seagull, so the induced 1/G is not fixed. C2 adds that the seagull which closure fixes is not the one needed, and that closure cannot fix 1/G.',
  'C2 refines the B4b statement.')

E('D2 closure consequence (C3)',
  'Exact lattice closure beyond leading order is the open obligation.',
  'Exact lattice closure beyond leading order is open. A translation-covariant relabelling algebra that closes within its span with field-independent structure constants cannot carry the continuum spectrum (C3, checked). So exact closure needs field-dependent structure functions or more generators, or accepts a non-continuum spectrum.',
  'C3 changed the status of this obligation.')

E('D3 normalisation (C4, C4b)',
  'No bracket can force this normalisation unless one of these is fixed.',
  'No bracket can force this normalisation unless one of these is fixed. For the walker, its frame identification fixes unit matter coupling by definition (C4), and closure with it then forces K1 = K2 (C4b, checked).',
  'C4/C4b realise one of the listed equivalences.')

E('D4 09-25 walk alpha (C4b)',
  'so the closure route reproduces its α = K/4.',
  'so the closure route reproduces its α = K/4 (with the walker as matter, C4b gives α = K2/4 and K1 = K2).',
  'Point to the walker-closure result.')

E('D5 taste route (B24, B25)',
  '  - So no step found so far passes the closure selection rule.',
  '  - So no step found so far passes the closure selection rule. Enlarged and spectral taste groups (B24, B25, checked) do not change this; see summary item 7.',
  'B24/B25 extend the taste route.')

E('D6 Dirac-level scope (B23)',
  'Levels mixing these doublets with the spin-3/2 content are not covered.',
  'Levels with spin-3/2 content, mixed with these doublets or pure, are not screened (B23).',
  'B23 lists pure 8-fold G3/2 levels as unscreened too.')

E('D7 status after campaign',
  'meets the closure selection rule (B17, B18, B20), because',
  'meets the closure selection rule (B17, B18, B20, B23–B25), because',
  'Phase-2 searches.')

E('D8 eight-node step gaplessness is certified',
  'The remaining escape routes are steps gapless in quasi-energy, as the eight-node step appears to be (B17 check, numerical; not tested across the searched families), or giving up the axis C2s.',
  'The remaining escape routes are steps gapless in quasi-energy, as the eight-node step is (certified in the corollary check; not tested across the searched families), or giving up the axis C2s. Pairing does not remove the doublers selectively either: under full O a single symmetric pair condensate is all-or-nothing at the eight cube points (C1, checked).',
  'Contradicted item 6 and claim_scope (8), which say the gaplessness is certified (COROLLARY_check chk3); adds C1.')

E('D9 exact redundancies (C3)',
  'O(a²) for the scalar and O(a) for one-sided Maxwell (B14, B16, B19).',
  'O(a²) for the scalar and O(a) for one-sided Maxwell (B14, B16, B19). Exact closure with the continuum spectrum is excluded within field-independent structure constants (C3).',
  'C3.')

E('N1 no-go gate rung 0 -> 1 (C6)',
  '  - The rung 0 → 1 encoding is not derived from dynamics.',
  '  - The rung 0 → 1 encoding is not derived from dynamics, and covariant formation from an empty start cannot produce its block registration (C6).',
  'C6.')

E('V1 runtime',
  '(about two to three minutes; 1 min 52 s in the coherence review)',
  '(about one to three minutes; 1 min 6 s in the second coherence review)',
  'Measured in this review.')


import sys, pathlib
NOTE = pathlib.Path("/home/user/qubit-lattice-axiom-framework/docs/SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md")
HERE = pathlib.Path(__file__).resolve().parent

def verify(write_preview=True):
    s = NOTE.read_text(); bad = 0
    for tag, old, new, _ in EDITS:
        n = s.count(old)
        if n != 1:
            print(f"[FAIL] {tag}: old occurs {n} times in current note"); bad += 1
    t = s
    if not bad:
        for tag, old, new, _ in EDITS:
            n = t.count(old)
            if n != 1:
                print(f"[FAIL] {tag}: old occurs {n} times at application time"); bad += 1; continue
            t = t.replace(old, new, 1)
            if t.count(new) < 1:
                print(f"[FAIL] {tag}: new text missing after apply"); bad += 1
    # items 7-8 length (source lines)
    if not bad:
        a = t.index("7. **Phase 2"); b = t.index("### Detail")
        n78 = len(t[a:b].strip().split("\n"))
        print(f"summary items 7-8: {n78} source lines")
        if n78 > 25: print("[FAIL] items 7-8 exceed 25 lines"); bad += 1
        if "](" in t[a:b]: print("[FAIL] markdown link in items 7-8"); bad += 1
    print(f"{len(EDITS)} edits, {bad} failures")
    if write_preview and not bad:
        p = HERE / "patched_note_preview.txt"
        assert "docs" not in p.parts
        p.write_text(t); print("preview:", p)
    return bad

if __name__ == "__main__":
    sys.exit(verify())
