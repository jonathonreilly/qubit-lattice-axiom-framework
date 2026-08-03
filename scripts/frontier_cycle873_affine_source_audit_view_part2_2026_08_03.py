#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 affine source, part 2/3."""

TARGET_SOURCE = "scripts/frontier_cycle873_uniform_affine_gauss_intertwiner_core_2026_08_03.py"
PART_ORDINAL = 2
PART_COUNT = 3
FIRST_SOURCE_LINE = 558
LAST_SOURCE_LINE = 1038
TOTAL_SOURCE_LINES = 1118
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "a1bc2159c5e2d5f59087860e3fe40bb1919cd4e476f6565a99c326d5af1c5ca9"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000558|        if nu != nv:
# C873SRC 000559|            wrong_sign_nontrivial += 1
# C873SRC 000560|            for wrong_alpha in range(P):
# C873SRC 000561|                if wrong_alpha == 1:
# C873SRC 000562|                    continue
# C873SRC 000563|                wrong_current = np.zeros(len(cube_l2.edges), dtype=np.int64)
# C873SRC 000564|                wrong_current[edge] = wrong_alpha * (nu - nv)
# C873SRC 000565|                assert not np.array_equal(
# C873SRC 000566|                    (cube_l2.incidence @ wrong_current) % P, (q1 - q0) % P
# C873SRC 000567|                )
# C873SRC 000568|                wrong_alpha_l2_cases += 1
# C873SRC 000569|
# C873SRC 000570|repeat_sequence = tuple(range(len(cube_l2.edges))) * 3
# C873SRC 000571|repeat_history_nonzero = 0
# C873SRC 000572|repeat_l2_incidence_failures = 0
# C873SRC 000573|repeat_history_kernel_failures = 0
# C873SRC 000574|for bits in range(1 << len(cube_l2.vertices)):
# C873SRC 000575|    initial_bits = bits
# C873SRC 000576|    background = supplied_star_background(cube_l2, bits.bit_count())
# C873SRC 000577|    current_bits = bits
# C873SRC 000578|    accumulated = np.zeros(len(cube_l2.edges), dtype=np.int64)
# C873SRC 000579|    for edge in repeat_sequence:
# C873SRC 000580|        u, v, _axis = cube_l2.edges[edge]
# C873SRC 000581|        new_bits, _phase, nu, nv = swap_bits(current_bits, u, v)
# C873SRC 000582|        accumulated[edge] = (accumulated[edge] + nu - nv) % P
# C873SRC 000583|        current_bits = new_bits
# C873SRC 000584|    q0 = matter_charge(cube_l2, initial_bits, background)
# C873SRC 000585|    q1 = matter_charge(cube_l2, current_bits, background)
# C873SRC 000586|    repeat_l2_incidence_failures += not np.array_equal(
# C873SRC 000587|        (cube_l2.incidence @ accumulated) % P, (q1 - q0) % P
# C873SRC 000588|    )
# C873SRC 000589|    canonical_difference = (
# C873SRC 000590|        solve_mod(cube_l2.incidence, q1) - solve_mod(cube_l2.incidence, q0)
# C873SRC 000591|    ) % P
# C873SRC 000592|    history = (accumulated - canonical_difference) % P
# C873SRC 000593|    repeat_history_kernel_failures += int(
# C873SRC 000594|        np.count_nonzero((cube_l2.incidence @ history) % P) != 0
# C873SRC 000595|    )
# C873SRC 000596|    repeat_history_nonzero += int(np.any(history))
# C873SRC 000597|
# C873SRC 000598|# L2 deletion nuance: the six raw faces have one cube-boundary relation.  A
# C873SRC 000599|# single raw-face deletion is therefore inactive, whereas dropping one member
# C873SRC 000600|# of a chosen independent five-face basis leaves 17 path-history cosets.
# C873SRC 000601|all_minus_one_rank = rank_mod(cube_l2.faces[:, 1:])
# C873SRC 000602|reduced_basis = cube_basis[:, 1:]
# C873SRC 000603|reduced_rank = rank_mod(reduced_basis)
# C873SRC 000604|omitted = cube_basis[:, 0]
# C873SRC 000605|assert all_minus_one_rank == cube_cert["kernel_dimension"]
# C873SRC 000606|assert reduced_rank == cube_cert["kernel_dimension"] - 1
# C873SRC 000607|assert rank_mod(np.column_stack((reduced_basis, omitted))) == reduced_rank + 1
# C873SRC 000608|
# C873SRC 000609|omega = np.exp(2j * math.pi / P)
# C873SRC 000610|expected_character_overlap = np.conj(omega)
# C873SRC 000611|assert abs(character_overlap - expected_character_overlap) < 1e-12
# C873SRC 000612|
# C873SRC 000613|
# C873SRC 000614|def six_mode_total_occupation_extension_certificate() -> dict:
# C873SRC 000615|    """Lift the seam-bit identity to Cycle870's six-mode total N_x.
# C873SRC 000616|
# C873SRC 000617|    Here a,b are the selected seam-mode bits and s_u,s_v are the other five
# C873SRC 000618|    onsite-mode occupation counts.  The background/star field is
# C873SRC 000619|    g = B*ell-alpha*n and must stay fixed under the seam current update.
# C873SRC 000620|    """
# C873SRC 000621|
# C873SRC 000622|    alpha = 1
# C873SRC 000623|    rows = 0
# C873SRC 000624|    incidence_failures = 0
# C873SRC 000625|    background_invariance_failures = 0
# C873SRC 000626|    total_number_failures = 0
# C873SRC 000627|    occupation_range_failures = 0
# C873SRC 000628|    fswap_minus_rows = 0
# C873SRC 000629|    fswap_sign_failures = 0
# C873SRC 000630|    wrong_incidence_sign_detected = 0
# C873SRC 000631|    omitted_shift_detected = 0
# C873SRC 000632|    for a, b in product((0, 1), repeat=2):
# C873SRC 000633|        for spectator_u, spectator_v in product(range(6), repeat=2):
# C873SRC 000634|            n_u = a + spectator_u
# C873SRC 000635|            n_v = b + spectator_v
# C873SRC 000636|            new_n_u = n_u - a + b
# C873SRC 000637|            new_n_v = n_v - b + a
# C873SRC 000638|            for ell in range(P):
# C873SRC 000639|                rows += 1
# C873SRC 000640|                current = alpha * (a - b)
# C873SRC 000641|                new_ell = (ell + current) % P
# C873SRC 000642|                boundary_current = np.asarray((-current, current)) % P
# C873SRC 000643|                charge_difference = alpha * np.asarray(
# C873SRC 000644|                    (new_n_u - n_u, new_n_v - n_v)
# C873SRC 000645|                ) % P
# C873SRC 000646|                incidence_failures += not np.array_equal(
# C873SRC 000647|                    boundary_current, charge_difference
# C873SRC 000648|                )
# C873SRC 000649|                background_before = np.asarray(
# C873SRC 000650|                    (-ell - alpha * n_u, ell - alpha * n_v)
# C873SRC 000651|                ) % P
# C873SRC 000652|                background_after = np.asarray(
# C873SRC 000653|                    (-new_ell - alpha * new_n_u,
# C873SRC 000654|                     new_ell - alpha * new_n_v)
# C873SRC 000655|                ) % P
# C873SRC 000656|                background_invariance_failures += not np.array_equal(
# C873SRC 000657|                    background_before, background_after
# C873SRC 000658|                )
# C873SRC 000659|                total_number_failures += (
# C873SRC 000660|                    n_u + n_v != new_n_u + new_n_v
# C873SRC 000661|                )
# C873SRC 000662|                occupation_range_failures += not (
# C873SRC 000663|                    0 <= n_u <= 6 and 0 <= n_v <= 6
# C873SRC 000664|                    and 0 <= new_n_u <= 6 and 0 <= new_n_v <= 6
# C873SRC 000665|                )
# C873SRC 000666|                sign = -1 if a == b == 1 else 1
# C873SRC 000667|                fswap_minus_rows += sign == -1
# C873SRC 000668|                fswap_sign_failures += sign != (-1 if a == b == 1 else 1)
# C873SRC 000669|                if a != b:
# C873SRC 000670|                    wrong_boundary = np.asarray((current, -current)) % P
# C873SRC 000671|                    wrong_incidence_sign_detected += not np.array_equal(
# C873SRC 000672|                        wrong_boundary, charge_difference
# C873SRC 000673|                    )
# C873SRC 000674|                    omitted_shift_background = np.asarray(
# C873SRC 000675|                        (-ell - alpha * new_n_u,
# C873SRC 000676|                         ell - alpha * new_n_v)
# C873SRC 000677|                    ) % P
# C873SRC 000678|                    omitted_shift_detected += not np.array_equal(
# C873SRC 000679|                        background_before, omitted_shift_background
# C873SRC 000680|                    )
# C873SRC 000681|    return {
# C873SRC 000682|        "rows": rows,
# C873SRC 000683|        "selected_seam_bits": "a,b in {0,1}",
# C873SRC 000684|        "alpha_normalization": "+1",
# C873SRC 000685|        "spectator_mode_counts": "s_u,s_v in {0,...,5}",
# C873SRC 000686|        "total_occupations": "n_u=a+s_u and n_v=b+s_v, each in {0,...,6}",
# C873SRC 000687|        "link_labels": P,
# C873SRC 000688|        "update": (
# C873SRC 000689|            "n'_u=n_u-a+b; n'_v=n_v-b+a; "
# C873SRC 000690|            "ell'=ell+(a-b) mod17 at the alpha=+1 normalization"
# C873SRC 000691|        ),
# C873SRC 000692|        "incidence_failures": incidence_failures,
# C873SRC 000693|        "fixed_background_or_star_invariance_failures":
# C873SRC 000694|            background_invariance_failures,
# C873SRC 000695|        "total_number_failures": total_number_failures,
# C873SRC 000696|        "occupation_range_failures": occupation_range_failures,
# C873SRC 000697|        "FSWAP_minus_11_rows": fswap_minus_rows,
# C873SRC 000698|        "FSWAP_sign_failures": fswap_sign_failures,
# C873SRC 000699|        "wrong_incidence_sign_detected_rows": wrong_incidence_sign_detected,
# C873SRC 000700|        "omitted_link_shift_detected_rows": omitted_shift_detected,
# C873SRC 000701|        "scope": (
# C873SRC 000702|            "algebraic alpha=+1 total-six-mode star/count extension of one selected "
# C873SRC 000703|            "seam; no second alpha=-1 global affine fixture, many-mode affine-state "
# C873SRC 000704|            "preparation, or new physical compiler"
# C873SRC 000705|        ),
# C873SRC 000706|    }
# C873SRC 000707|
# C873SRC 000708|
# C873SRC 000709|SIX_MODE_TOTAL_OCCUPATION = six_mode_total_occupation_extension_certificate()
# C873SRC 000710|
# C873SRC 000711|
# C873SRC 000712|def reconstruct_schedule(gates) -> np.ndarray:
# C873SRC 000713|    output = np.eye(6, dtype=complex)
# C873SRC 000714|    for gate in gates:
# C873SRC 000715|        if gate.kind == "phase":
# C873SRC 000716|            matrix = np.eye(6, dtype=complex)
# C873SRC 000717|            matrix[gate.modes[0], gate.modes[0]] = gate.matrix[0, 0]
# C873SRC 000718|        else:
# C873SRC 000719|            matrix = C870.embed_one_particle(gate.matrix, gate.modes)
# C873SRC 000720|        output = matrix @ output
# C873SRC 000721|    return output
# C873SRC 000722|
# C873SRC 000723|
# C873SRC 000724|def cycle219_decoded_dispersion_certificate() -> dict:
# C873SRC 000725|    beta = float(C870.c230.BETA)
# C873SRC 000726|    species = C219.common_species(beta)
# C873SRC 000727|    coin = np.asarray(species.coin, dtype=complex)
# C873SRC 000728|    gates, qr = C870.qr_coin_schedule(coin)
# C873SRC 000729|    uniform_cycle = np.ones(P, dtype=complex) / math.sqrt(P)
# C873SRC 000730|
# C873SRC 000731|    onsite_intertwiner_residual = 0.0
# C873SRC 000732|    for source_mode in range(6):
# C873SRC 000733|        encoded = np.zeros((6, P), dtype=complex)
# C873SRC 000734|        encoded[source_mode, :] = uniform_cycle
# C873SRC 000735|        observed = coin @ encoded
# C873SRC 000736|        expected = np.outer(coin[:, source_mode], uniform_cycle)
# C873SRC 000737|        onsite_intertwiner_residual = max(
# C873SRC 000738|            onsite_intertwiner_residual, float(np.linalg.norm(observed - expected))
# C873SRC 000739|        )
# C873SRC 000740|
# C873SRC 000741|    deletion_residuals = tuple(
# C873SRC 000742|        float(np.linalg.norm(
# C873SRC 000743|            reconstruct_schedule(tuple(
# C873SRC 000744|                gate for position, gate in enumerate(gates) if position != deleted
# C873SRC 000745|            )) - coin
# C873SRC 000746|        ))
# C873SRC 000747|        for deleted in range(len(gates))
# C873SRC 000748|    )
# C873SRC 000749|    selected_deleted_gate = int(np.argmax(deletion_residuals))
# C873SRC 000750|    curvature = C219.c210.curvature_tensor(species, step=1.0e-4)
# C873SRC 000751|    dispersion_mass = 1.0 / float(np.mean(np.diag(curvature)))
# C873SRC 000752|    rest_mass = C219.rest_mass(species)
# C873SRC 000753|
# C873SRC 000754|    momenta = (
# C873SRC 000755|        (0.0, 0.0, 0.0),
# C873SRC 000756|        (0.07, 0.0, 0.0), (-0.07, 0.0, 0.0),
# C873SRC 000757|        (0.0, 0.07, 0.0), (0.0, -0.07, 0.0),
# C873SRC 000758|        (0.0, 0.0, 0.07), (0.0, 0.0, -0.07),
# C873SRC 000759|        (0.04, -0.03, 0.02),
# C873SRC 000760|    )
# C873SRC 000761|    bloch_rows = []
# C873SRC 000762|    same_block_power_residual = 0.0
# C873SRC 000763|    for momentum in momenta:
# C873SRC 000764|        bloch = C219.c210.molecular_bloch(np.asarray(momentum), coin)
# C873SRC 000765|        phase, _vector = C219.c210.branch_eigenpair(
# C873SRC 000766|            np.asarray(momentum), species
# C873SRC 000767|        )
# C873SRC 000768|        sequential = np.eye(6, dtype=complex)
# C873SRC 000769|        for _ in range(8):
# C873SRC 000770|            sequential = bloch @ sequential
# C873SRC 000771|        same_block_power_residual = max(
# C873SRC 000772|            same_block_power_residual,
# C873SRC 000773|            float(np.linalg.norm(sequential - np.linalg.matrix_power(bloch, 8))),
# C873SRC 000774|        )
# C873SRC 000775|        bloch_rows.append({
# C873SRC 000776|            "momentum": momentum,
# C873SRC 000777|            "scalar_branch_phase": phase,
# C873SRC 000778|            "unitarity_residual": float(
# C873SRC 000779|                np.linalg.norm(bloch.conj().T @ bloch - np.eye(6))
# C873SRC 000780|            ),
# C873SRC 000781|        })
# C873SRC 000782|
# C873SRC 000783|    return {
# C873SRC 000784|        "actual_Cycle870_beta": beta,
# C873SRC 000785|        "coin_sha256": sha256(coin.tobytes()).hexdigest(),
# C873SRC 000786|        "coin_unitarity_residual": float(
# C873SRC 000787|            np.linalg.norm(coin.conj().T @ coin - np.eye(6))
# C873SRC 000788|        ),
# C873SRC 000789|        "dense_nonzero_entries": int(np.count_nonzero(np.abs(coin) > 1.0e-13)),
# C873SRC 000790|        "QR_gate_count": len(gates),
# C873SRC 000791|        "QR_reconstruction_residual": qr["reconstruction_residual"],
# C873SRC 000792|        "QR_off_diagonal_residual": qr["QR_off_diagonal_residual"],
# C873SRC 000793|        "single_QR_gate_deletion_residuals": deletion_residuals,
# C873SRC 000794|        "inactive_identity_phase_deletion_indices": tuple(
# C873SRC 000795|            index for index, residual in enumerate(deletion_residuals)
# C873SRC 000796|            if residual <= TOL
# C873SRC 000797|        ),
# C873SRC 000798|        "selected_active_QR_gate_deletion_index": selected_deleted_gate,
# C873SRC 000799|        "selected_active_QR_gate_deletion_residual": deletion_residuals[
# C873SRC 000800|            selected_deleted_gate
# C873SRC 000801|        ],
# C873SRC 000802|        "QR_deletion_scope": (
# C873SRC 000803|            "one selected nonidentity-gate deletion is an active control; identity "
# C873SRC 000804|            "phase entries may be structurally inactive and no every-gate "
# C873SRC 000805|            "essentiality claim is made"
# C873SRC 000806|        ),
# C873SRC 000807|        "trivial_cycle_uniform_normalization_residual": abs(
# C873SRC 000808|            float(np.vdot(uniform_cycle, uniform_cycle).real) - 1.0
# C873SRC 000809|        ),
# C873SRC 000810|        "trivial_cycle_translation_residual": float(
# C873SRC 000811|            np.linalg.norm(np.roll(uniform_cycle, 1) - uniform_cycle)
# C873SRC 000812|        ),
# C873SRC 000813|        "actual_dense_coin_encoded_onsite_intertwiner_residual":
# C873SRC 000814|            onsite_intertwiner_residual,
# C873SRC 000815|        "momentum_samples": bloch_rows,
# C873SRC 000816|        "maximum_Bloch_unitarity_residual": max(
# C873SRC 000817|            row["unitarity_residual"] for row in bloch_rows
# C873SRC 000818|        ),
# C873SRC 000819|        "eight_step_same_block_multiplication_consistency_residual":
# C873SRC 000820|            same_block_power_residual,
# C873SRC 000821|        "curvature_tensor_step_1e_minus_4": curvature.tolist(),
# C873SRC 000822|        "analytic_mass": float(species.analytic_mass),
# C873SRC 000823|        "rest_mass": rest_mass,
# C873SRC 000824|        "dispersion_mass": dispersion_mass,
# C873SRC 000825|        "rest_to_analytic_residual": abs(rest_mass - species.analytic_mass),
# C873SRC 000826|        "dispersion_relative_residual": abs(
# C873SRC 000827|            dispersion_mass / species.analytic_mass - 1.0
# C873SRC 000828|        ),
# C873SRC 000829|        "decoded_spectrum_statement": (
# C873SRC 000830|            "the exact seam-column affine intertwiner plus onsite number preservation "
# C873SRC 000831|            "makes the trivial-character code representation conjugate to the supplied "
# C873SRC 000832|            "free one-particle Cycle219 Bloch word; its decoded eigenphases and local "
# C873SRC 000833|            "curvature therefore equal the displayed Cycle219 fixture"
# C873SRC 000834|        ),
# C873SRC 000835|        "scope_boundary": (
# C873SRC 000836|            "this is the supplied translation-invariant free one-particle momentum "
# C873SRC 000837|            "fixture, not a periodic F17 physical-box construction and not an "
# C873SRC 000838|            "interacting finite-open-box spectrum"
# C873SRC 000839|        ),
# C873SRC 000840|    }
# C873SRC 000841|
# C873SRC 000842|
# C873SRC 000843|C219_CERTIFICATE = cycle219_decoded_dispersion_certificate()
# C873SRC 000844|OBSERVED_SOURCE_SHA256 = {
# C873SRC 000845|    path: file_sha256(ROOT / path) for path in SOURCE_PINS
# C873SRC 000846|}
# C873SRC 000847|SOURCE_HASH_MISMATCHES = {
# C873SRC 000848|    path: {"expected": expected, "observed": OBSERVED_SOURCE_SHA256[path]}
# C873SRC 000849|    for path, expected in SOURCE_PINS.items()
# C873SRC 000850|    if OBSERVED_SOURCE_SHA256[path] != expected
# C873SRC 000851|}
# C873SRC 000852|EXPECTED_BASE_IS_ANCESTOR_OF_HEAD = subprocess.run(
# C873SRC 000853|    (
# C873SRC 000854|        "git", "merge-base", "--is-ancestor",
# C873SRC 000855|        EXPECTED_BASE_COMMIT, "HEAD",
# C873SRC 000856|    ),
# C873SRC 000857|    cwd=ROOT,
# C873SRC 000858|    check=False,
# C873SRC 000859|).returncode == 0
# C873SRC 000860|
# C873SRC 000861|result = {
# C873SRC 000862|    "status": "pending",
# C873SRC 000863|    "name": "Cycle873 uniform affine-Gauss/trivial-loop intertwiner core",
# C873SRC 000864|    "provenance": {
# C873SRC 000865|        "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 000866|        "expected_base_is_ancestor_of_head": EXPECTED_BASE_IS_ANCESTOR_OF_HEAD,
# C873SRC 000867|        "runner": str(Path(__file__).relative_to(ROOT)),
# C873SRC 000868|        "source_sha256": OBSERVED_SOURCE_SHA256,
# C873SRC 000869|        "source_hash_mismatches": SOURCE_HASH_MISMATCHES,
# C873SRC 000870|    },
# C873SRC 000871|    "field": "Z17",
# C873SRC 000872|    "orientation": "incidence boundary is head minus tail; +alpha on u->v has boundary alpha(e_v-e_u)",
# C873SRC 000873|    "fixed_star_background": {
# C873SRC 000874|        "gauss_word": "q_g(n)=alpha*n+g mod17 with sum(g)=-alpha*N in a fixed-N sector",
# C873SRC 000875|        "type": "supplied FixedStarBackground(label, alpha, particle_number, field)",
# C873SRC 000876|        "diagnostic_conventions": (
# C873SRC 000877|            "ordered_prefix", "first_anchor", "last_anchor"
# C873SRC 000878|        ),
# C873SRC 000879|        "filled_plaquette_variant_cases": background_variant_cases,
# C873SRC 000880|        "filled_plaquette_variant_intertwiner_max_residual": max(
# C873SRC 000881|            background_variant_residuals
# C873SRC 000882|        ),
# C873SRC 000883|        "selection_boundary": (
# C873SRC 000884|            "g and its fixed matter-number sector are input structure; this core "
# C873SRC 000885|            "does not select, prepare, or enforce either"
# C873SRC 000886|        ),
# C873SRC 000887|        "ordering_boundary": (
# C873SRC 000888|            "ordered_prefix is one diagnostic background convention with a preferred "
# C873SRC 000889|            "vertex order; the theorem is also checked for first- and last-anchor "
# C873SRC 000890|            "backgrounds, but no preferred-order-free genesis claim is made"
# C873SRC 000891|        ),
# C873SRC 000892|        "covariance_boundary": (
# C873SRC 000893|            "full affine-encoder 24-frame, 576-product, and translation covariance "
# C873SRC 000894|            "with transported g is not established here; only the separate local-"
# C873SRC 000895|            "constraint core checks its stated physical support/frame covariance"
# C873SRC 000896|        ),
# C873SRC 000897|    },
# C873SRC 000898|    "theorem_checked": {
# C873SRC 000899|        "affine_fiber_translation": "T_j A_q = A_(q + incidence*j) bijectively on every finite oriented graph",
# C873SRC 000900|        "uniform_state_translation": "T_j |A_q> = |A_(q + incidence*j)> exactly",
# C873SRC 000901|        "path_independence": "translations with the same boundary differ by ker(incidence), which fixes the trivial-character uniform state",
# C873SRC 000902|        "intertwiner_condition": (
# C873SRC 000903|            "at fixed supplied g, incidence*j(n->n') = q_g(n')-q_g(n)"
# C873SRC 000904|        ),
# C873SRC 000905|        "arbitrary_superpositions": "follows by linearity after basis-column equality",
# C873SRC 000906|        "repeated_factors": "follows by induction; independently checked below on a 36-factor L2 sequence",
# C873SRC 000907|    },
# C873SRC 000908|    "filled_plaquette": {
# C873SRC 000909|        **plaquette_cert,
# C873SRC 000910|        "direct_fswap_columns_checked": len(direct_residuals),
# C873SRC 000911|        "direct_intertwiner_max_residual": max(direct_residuals),
# C873SRC 000912|        "supplied_background_variant_columns_checked": background_variant_cases,
# C873SRC 000913|        "supplied_background_variant_max_residual": max(
# C873SRC 000914|            background_variant_residuals
# C873SRC 000915|        ),
# C873SRC 000916|        "four_factor_sequence_columns_checked": len(sequence_residuals),
# C873SRC 000917|        "four_factor_sequence_max_residual": max(sequence_residuals),
# C873SRC 000918|        "uniform_closed_loop_overlap": [uniform_loop_overlap.real, uniform_loop_overlap.imag],
# C873SRC 000919|        "uniform_closed_loop_residual": state_residual(uniform_loop, expected_uniform),
# C873SRC 000920|        "basis_link_closed_loop_overlap": [basis_overlap.real, basis_overlap.imag],
# C873SRC 000921|        "basis_link_closed_loop_residual": basis_residual,
# C873SRC 000922|        "nonuniform_character_closed_loop_overlap": [character_overlap.real, character_overlap.imag],
# C873SRC 000923|        "nonuniform_character_closed_loop_residual": character_residual,
# C873SRC 000924|        "nonuniform_character_exact_residual": "2 sin(pi/17)",
# C873SRC 000925|        "omit_only_plaquette_invariant_dimension": P,
# C873SRC 000926|        "wrong_sign_max_column_residual": max(wrong_sign_residuals),
# C873SRC 000927|        "wrong_sign_frobenius_one_edge": math.sqrt(
# C873SRC 000928|            sum(value * value for value in wrong_sign_residuals[:: len(plaquette.edges)])
# C873SRC 000929|        ),
# C873SRC 000930|        "wrong_alpha_values_mod17": sorted(wrong_alpha_active_residuals),
# C873SRC 000931|        "wrong_alpha_active_columns_per_value": len(
# C873SRC 000932|            next(iter(wrong_alpha_active_residuals.values()))
# C873SRC 000933|        ),
# C873SRC 000934|        "wrong_alpha_active_overlap": 0,
# C873SRC 000935|        "wrong_alpha_active_column_residual": math.sqrt(2),
# C873SRC 000936|    },
# C873SRC 000937|    "open_cube_L2": {
# C873SRC 000938|        **cube_cert,
# C873SRC 000939|        "direct_seam_cases_checked": direct_l2_cases,
# C873SRC 000940|        "correct_direct_incidence_failures": direct_l2_incidence_failures,
# C873SRC 000941|        "wrong_sign_nontrivial_cases": wrong_sign_nontrivial,
# C873SRC 000942|        "wrong_sign_overlap": 0,
# C873SRC 000943|        "wrong_sign_column_residual": math.sqrt(2),
# C873SRC 000944|        "wrong_alpha_values_mod17": [alpha for alpha in range(P) if alpha != 1],
# C873SRC 000945|        "wrong_alpha_active_cases_checked": wrong_alpha_l2_cases,
# C873SRC 000946|        "wrong_alpha_active_overlap": 0,
# C873SRC 000947|        "wrong_alpha_active_column_residual": math.sqrt(2),
# C873SRC 000948|        "repeated_factor_count": len(repeat_sequence),
# C873SRC 000949|        "repeated_matter_words_checked": 1 << len(cube_l2.vertices),
# C873SRC 000950|        "repeated_uniform_intertwiner_incidence_failures":
# C873SRC 000951|            repeat_l2_incidence_failures,
# C873SRC 000952|        "repeated_history_kernel_failures": repeat_history_kernel_failures,
# C873SRC 000953|        "histories_with_nonzero_kernel_residual": repeat_history_nonzero,
# C873SRC 000954|        "all_six_faces_minus_one_face_rank": all_minus_one_rank,
# C873SRC 000955|        "all_six_faces_minus_one_invariant_dimension": P ** (
# C873SRC 000956|            cube_cert["kernel_dimension"] - all_minus_one_rank
# C873SRC 000957|        ),
# C873SRC 000958|        "independent_five_face_basis_minus_one_rank": reduced_rank,
# C873SRC 000959|        "independent_basis_minus_one_invariant_dimension": P ** (
# C873SRC 000960|            cube_cert["kernel_dimension"] - reduced_rank
# C873SRC 000961|        ),
# C873SRC 000962|        "omitted_independent_generator_overlap": 0,
# C873SRC 000963|        "omitted_independent_generator_residual": math.sqrt(2),
# C873SRC 000964|        "nonuniform_character_cycle_overlap": [
# C873SRC 000965|            expected_character_overlap.real,
# C873SRC 000966|            expected_character_overlap.imag,
# C873SRC 000967|        ],
# C873SRC 000968|        "nonuniform_character_cycle_residual": abs(expected_character_overlap - 1),
# C873SRC 000969|        "nonuniform_character_exact_residual": "2 sin(pi/17)",
# C873SRC 000970|    },
# C873SRC 000971|    "open_box_general": {
# C873SRC 000972|        "vertices": "L^3",
# C873SRC 000973|        "edges": "3 L^2 (L-1)",
# C873SRC 000974|        "incidence_rank": "L^3-1",
# C873SRC 000975|        "cycle_dimension": "2 L^3-3 L^2+1",
# C873SRC 000976|        "affine_sector_size": "17^(2 L^3-3 L^2+1)",
# C873SRC 000977|        "plaquettes": "3 L (L-1)^2",
# C873SRC 000978|        "plaquette_relations": "(L-1)^3 cube-boundary/Bianchi relations",
# C873SRC 000979|        "unique_plus_sector": "yes for the full contractible box cell complex",
# C873SRC 000980|        "arbitrary_open_cubic_subgraph": "only if plaquette boundaries span ker(incidence), equivalently H1=0",
# C873SRC 000981|    },
# C873SRC 000982|    "six_mode_total_occupation_extension": SIX_MODE_TOTAL_OCCUPATION,
# C873SRC 000983|    "actual_Cycle219_decoded_free_one_particle": C219_CERTIFICATE,
# C873SRC 000984|    "supplies_and_boundaries": {
# C873SRC 000985|        "boundary": "connected finite open cell complex and compatible zero-total Gauss word, or separately supplied boundary flux ports",
# C873SRC 000986|        "topology": "local plaquette shifts leave 17^b1 sectors when H1 is nonzero; full ker-uniformity additionally fixes/superposes Wilson cycles",
# C873SRC 000987|        "genesis": "constraints characterize the state but do not prepare it; a coherent preparation/admission law and clean one-hot link bank remain supplied",
# C873SRC 000988|        "orientation_and_alpha": (
# C873SRC 000989|            "edge orientation and matter-charge convention are supplied; the global "
# C873SRC 000990|            "affine fixture is normalized to alpha=+1 and no alpha=-1 global encoder "
# C873SRC 000991|            "fixture is claimed"
# C873SRC 000992|        ),
# C873SRC 000993|        "fixed_star_background": (
# C873SRC 000994|            "a compatible fixed-N star/background field g is supplied and transported "
# C873SRC 000995|            "when geometry is compared; background selection and genesis remain open"
# C873SRC 000996|        ),
# C873SRC 000997|        "encoder_covariance": (
# C873SRC 000998|            "no full affine-encoder proper-frame/product/translation covariance theorem "
# C873SRC 000999|            "is claimed by this core"
# C873SRC 001000|        ),
# C873SRC 001001|        "physical_compilation": (
# C873SRC 001002|            "this algebra core is abstract; the separate Cycle873 physical and local-constraint "
# C873SRC 001003|            "cores emit the grouped augmented seam and 17-rail plaquette shifts"
# C873SRC 001004|        ),
# C873SRC 001005|        "finite_synthesis": (
# C873SRC 001006|            "ideal arbitrary rotations and order-17 projector/preparation synthesis remain supplied/open"
# C873SRC 001007|        ),
# C873SRC 001008|        "interpretation_firewall": (
# C873SRC 001009|            "no source, gravity, time, occurrence, Event, Record, Born, or autonomous genesis claim"
# C873SRC 001010|        ),
# C873SRC 001011|    },
# C873SRC 001012|}
# C873SRC 001013|
# C873SRC 001014|failures = []
# C873SRC 001015|if not EXPECTED_BASE_IS_ANCESTOR_OF_HEAD:
# C873SRC 001016|    failures.append("expected base is not an ancestor of HEAD")
# C873SRC 001017|if SOURCE_HASH_MISMATCHES:
# C873SRC 001018|    failures.append("source hash mismatch")
# C873SRC 001019|if max(background_variant_residuals) > TOL or background_variant_cases != 192:
# C873SRC 001020|    failures.append("supplied fixed-star background variants")
# C873SRC 001021|if (
# C873SRC 001022|    SIX_MODE_TOTAL_OCCUPATION["rows"] != 2448
# C873SRC 001023|    or SIX_MODE_TOTAL_OCCUPATION["FSWAP_minus_11_rows"] != 612
# C873SRC 001024|    or any(
# C873SRC 001025|        SIX_MODE_TOTAL_OCCUPATION[key]
# C873SRC 001026|        for key in (
# C873SRC 001027|            "incidence_failures",
# C873SRC 001028|            "fixed_background_or_star_invariance_failures",
# C873SRC 001029|            "total_number_failures",
# C873SRC 001030|            "occupation_range_failures",
# C873SRC 001031|            "FSWAP_sign_failures",
# C873SRC 001032|        )
# C873SRC 001033|    )
# C873SRC 001034|    or SIX_MODE_TOTAL_OCCUPATION["wrong_incidence_sign_detected_rows"] != 1224
# C873SRC 001035|    or SIX_MODE_TOTAL_OCCUPATION["omitted_link_shift_detected_rows"] != 1224
# C873SRC 001036|):
# C873SRC 001037|    failures.append("six-mode total-occupation extension")
# C873SRC 001038|if result["filled_plaquette"]["direct_intertwiner_max_residual"] > TOL:
