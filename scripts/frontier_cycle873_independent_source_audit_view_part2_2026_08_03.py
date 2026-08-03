#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 independent source, part 2/4."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.py"
PART_ORDINAL = 2
PART_COUNT = 4
FIRST_SOURCE_LINE = 481
LAST_SOURCE_LINE = 940
TOTAL_SOURCE_LINES = 1546
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "02c3f321ba5ef1dce723ed04bd83919839648fd89202f607b6cc680645a97734"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000481|        "predicate_uncompute_supplied_column_residual": float(np.linalg.norm((compose_small(C714, uncompute) - predicate_target)[:, uncompute_columns])),
# C873SRC 000482|        "uncompute_literal_deletion_residuals": uncompute_deletions,
# C873SRC 000483|        "minimum_uncompute_literal_deletion_residual": min(uncompute_deletions),
# C873SRC 000484|    }
# C873SRC 000485|
# C873SRC 000486|
# C873SRC 000487|def extraction_certificate(C870, C871):
# C873SRC 000488|    graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
# C873SRC 000489|    context = C870.physical_context(graph)
# C873SRC 000490|    seam = C870.graph_seams(graph)[0]
# C873SRC 000491|    rows = []
# C873SRC 000492|    for cell, mode in ((seam[0], seam[3]), (seam[2], seam[4])):
# C873SRC 000493|        logical = graph.B(graph.vertex_index[(cell, mode)])
# C873SRC 000494|        physical = C870.physical_lift(logical, context)
# C873SRC 000495|        support = tuple(site for index, site in enumerate(context.sites) if (physical.z >> index) & 1)
# C873SRC 000496|        failures = 0
# C873SRC 000497|        deletion_changes = []
# C873SRC 000498|        for bits in range(1 << (len(support) + 1)):
# C873SRC 000499|            carrier = bits & ((1 << len(support)) - 1)
# C873SRC 000500|            target = (bits >> len(support)) & 1
# C873SRC 000501|            expected = target ^ (carrier.bit_count() & 1)
# C873SRC 000502|            observed = target
# C873SRC 000503|            for index in range(len(support)):
# C873SRC 000504|                observed ^= (carrier >> index) & 1
# C873SRC 000505|            failures += observed != expected
# C873SRC 000506|        for deleted in range(len(support)):
# C873SRC 000507|            changed = 0
# C873SRC 000508|            for bits in range(1 << (len(support) + 1)):
# C873SRC 000509|                carrier = bits & ((1 << len(support)) - 1)
# C873SRC 000510|                target = (bits >> len(support)) & 1
# C873SRC 000511|                expected = target ^ (carrier.bit_count() & 1)
# C873SRC 000512|                observed = target
# C873SRC 000513|                for index in range(len(support)):
# C873SRC 000514|                    if index != deleted:
# C873SRC 000515|                        observed ^= (carrier >> index) & 1
# C873SRC 000516|                changed += observed != expected
# C873SRC 000517|            deletion_changes.append(changed)
# C873SRC 000518|        rows.append({
# C873SRC 000519|            "cell": cell, "mode": mode, "physical_Z_weight": len(support),
# C873SRC 000520|            "basis_columns": 1 << (len(support) + 1), "parity_failures": failures,
# C873SRC 000521|            "single_CNOT_deletion_changed_full_carrier_columns": deletion_changes,
# C873SRC 000522|        })
# C873SRC 000523|    return {"endpoint_rows": rows}
# C873SRC 000524|
# C873SRC 000525|
# C873SRC 000526|def semantic_rows(alpha, mutation=None):
# C873SRC 000527|    rows = [
# C873SRC 000528|        ("pre_u", ("CNOT", 0, 2)), ("pre_v", ("CNOT", 1, 3)),
# C873SRC 000529|        ("seam", ("FSWAP",)),
# C873SRC 000530|        ("plus_x1", ("X", 3)), ("plus_tof", ("TOF", 2, 3, 4)), ("plus_x2", ("X", 3)),
# C873SRC 000531|        ("plus_shift", ("SHIFT", alpha)),
# C873SRC 000532|        ("plus_ux1", ("X", 3)), ("plus_utof", ("TOF", 2, 3, 4)), ("plus_ux2", ("X", 3)),
# C873SRC 000533|        ("minus_x1", ("X", 2)), ("minus_tof", ("TOF", 2, 3, 4)), ("minus_x2", ("X", 2)),
# C873SRC 000534|        ("minus_shift", ("SHIFT", -alpha)),
# C873SRC 000535|        ("minus_ux1", ("X", 2)), ("minus_utof", ("TOF", 2, 3, 4)), ("minus_ux2", ("X", 2)),
# C873SRC 000536|        ("clean_u", ("CNOT", 1, 2)), ("clean_v", ("CNOT", 0, 3)),
# C873SRC 000537|    ]
# C873SRC 000538|    omissions = {
# C873SRC 000539|        "delete_pre_u": {"pre_u"}, "delete_pre_v": {"pre_v"},
# C873SRC 000540|        "delete_seam": {"seam"}, "delete_plus_shift": {"plus_shift"},
# C873SRC 000541|        "delete_minus_shift": {"minus_shift"}, "delete_cleanup": {"clean_u", "clean_v"},
# C873SRC 000542|    }.get(mutation, set())
# C873SRC 000543|    return tuple(row for name, row in rows if name not in omissions)
# C873SRC 000544|
# C873SRC 000545|
# C873SRC 000546|def semantic_apply(state, operation, raw=False):
# C873SRC 000547|    out = {}
# C873SRC 000548|    for key, amplitude in state.items():
# C873SRC 000549|        bits = list(key[:5]); label = key[5]; phase = 1 + 0j
# C873SRC 000550|        kind = operation[0]
# C873SRC 000551|        if kind == "X": bits[operation[1]] ^= 1
# C873SRC 000552|        elif kind == "CNOT": bits[operation[2]] ^= bits[operation[1]]
# C873SRC 000553|        elif kind == "TOF": bits[operation[3]] ^= bits[operation[1]] & bits[operation[2]]
# C873SRC 000554|        elif kind == "SHIFT":
# C873SRC 000555|            if bits[4]: label = (label + operation[1]) % F17
# C873SRC 000556|        elif kind == "FSWAP":
# C873SRC 000557|            if bits[0] == bits[1] == 1: phase *= -1
# C873SRC 000558|            bits[0], bits[1] = bits[1], bits[0]
# C873SRC 000559|            if raw: phase *= -1j
# C873SRC 000560|        else: raise AssertionError(operation)
# C873SRC 000561|        target = (*bits, label)
# C873SRC 000562|        out[target] = out.get(target, 0j) + phase * amplitude
# C873SRC 000563|    return out
# C873SRC 000564|
# C873SRC 000565|
# C873SRC 000566|def semantic_execute(state, rows, raw=False):
# C873SRC 000567|    for row in rows:
# C873SRC 000568|        state = semantic_apply(state, row, raw=raw)
# C873SRC 000569|    return state
# C873SRC 000570|
# C873SRC 000571|
# C873SRC 000572|def augmented_target(a, b, label, alpha):
# C873SRC 000573|    phase = -1 if a == b == 1 else 1
# C873SRC 000574|    return {(b, a, 0, 0, 0, (label + alpha * (a - b)) % F17): complex(phase)}
# C873SRC 000575|
# C873SRC 000576|
# C873SRC 000577|def effective_macro_certificate():
# C873SRC 000578|    output = []
# C873SRC 000579|    rng = np.random.default_rng(170870)
# C873SRC 000580|    for alpha in (-1, 1):
# C873SRC 000581|        formal_max = raw_max = 0.0
# C873SRC 000582|        coherent = {}; coherent_target = {}
# C873SRC 000583|        amplitudes = rng.normal(size=4 * F17) + 1j * rng.normal(size=4 * F17)
# C873SRC 000584|        amplitudes /= np.linalg.norm(amplitudes)
# C873SRC 000585|        column = 0
# C873SRC 000586|        cleanup = inverse = 0
# C873SRC 000587|        for a, b in product((0, 1), repeat=2):
# C873SRC 000588|            for label in range(F17):
# C873SRC 000589|                initial = {(a, b, 0, 0, 0, label): 1 + 0j}
# C873SRC 000590|                target = augmented_target(a, b, label, alpha)
# C873SRC 000591|                raw = semantic_execute(initial, semantic_rows(alpha), raw=True)
# C873SRC 000592|                corrected = {key: 1j * value for key, value in raw.items()}
# C873SRC 000593|                formal_max = max(formal_max, state_distance(corrected, target))
# C873SRC 000594|                raw_max = max(raw_max, state_distance(raw, target))
# C873SRC 000595|                cleanup += any(key[2] or key[3] or key[4] for key in raw)
# C873SRC 000596|                amp = amplitudes[column]; column += 1
# C873SRC 000597|                coherent.update({next(iter(initial)): amp})
# C873SRC 000598|                key, value = next(iter(target.items()))
# C873SRC 000599|                coherent_target[key] = coherent_target.get(key, 0j) + amp * value
# C873SRC 000600|        coherent_raw = semantic_execute(coherent, semantic_rows(alpha), raw=True)
# C873SRC 000601|        coherent_corrected = {key: 1j * value for key, value in coherent_raw.items()}
# C873SRC 000602|        mutations = {}
# C873SRC 000603|        for mutation in ("delete_pre_u", "delete_pre_v", "delete_seam", "delete_plus_shift", "delete_minus_shift", "delete_cleanup"):
# C873SRC 000604|            changed = dirty = 0
# C873SRC 000605|            for a, b in product((0, 1), repeat=2):
# C873SRC 000606|                for label in range(F17):
# C873SRC 000607|                    initial = {(a, b, 0, 0, 0, label): 1 + 0j}
# C873SRC 000608|                    observed = semantic_execute(initial, semantic_rows(alpha, mutation), raw=False)
# C873SRC 000609|                    changed += state_distance(observed, augmented_target(a, b, label, alpha)) > TOL
# C873SRC 000610|                    dirty += any(key[2] or key[3] or key[4] for key in observed)
# C873SRC 000611|            mutations[mutation] = {"changed_columns": changed, "dirty_columns": dirty}
# C873SRC 000612|        output.append({
# C873SRC 000613|            "alpha": alpha, "encoded_columns": 68,
# C873SRC 000614|            "formal_corrected_basis_max_residual": clean_float(formal_max),
# C873SRC 000615|            "raw_basis_max_residual": raw_max,
# C873SRC 000616|            "raw_normalized_coherent_residual": state_distance(coherent_raw, coherent_target),
# C873SRC 000617|            "formal_corrected_arbitrary_coherent_residual": clean_float(state_distance(coherent_corrected, coherent_target)),
# C873SRC 000618|            "scratch_cleanup_failures": cleanup,
# C873SRC 000619|            "component_mutations": mutations,
# C873SRC 000620|        })
# C873SRC 000621|    # Every omitted adjacent Fredkin changes precisely its two endpoint labels.
# C873SRC 000622|    fredkin_deletions = {}
# C873SRC 000623|    for direction in (-1, 1):
# C873SRC 000624|        order = range(15, -1, -1) if direction > 0 else range(16)
# C873SRC 000625|        for omitted in range(16):
# C873SRC 000626|            changed = 0
# C873SRC 000627|            for label in range(F17):
# C873SRC 000628|                full = 1 << label; damaged = full
# C873SRC 000629|                for edge in order:
# C873SRC 000630|                    if ((full >> edge) & 1) != ((full >> (edge + 1)) & 1):
# C873SRC 000631|                        full ^= (1 << edge) | (1 << (edge + 1))
# C873SRC 000632|                    if edge != omitted and ((damaged >> edge) & 1) != ((damaged >> (edge + 1)) & 1):
# C873SRC 000633|                        damaged ^= (1 << edge) | (1 << (edge + 1))
# C873SRC 000634|                changed += full != damaged
# C873SRC 000635|            fredkin_deletions[f"{direction:+d}:{omitted}"] = changed
# C873SRC 000636|    return {"families": output, "deleted_Fredkin_changed_onehot_rows": fredkin_deletions}
# C873SRC 000637|
# C873SRC 000638|
# C873SRC 000639|def local_instruction(C870, kind, sites, matrix):
# C873SRC 000640|    return C870.c707.Instruction(kind, tuple(sites), matrix)
# C873SRC 000641|
# C873SRC 000642|
# C873SRC 000643|def independent_emitted_word(C870, C871, C714, graph, context, seam, alpha=1):
# C873SRC 000644|    packet = C871.packet_placement(graph, context, seam)
# C873SRC 000645|    rails = tuple(at(packet.midpoint, packet.basis, row) for row in RAIL_LOCAL_OFFSETS)
# C873SRC 000646|    qu, qv, current = (packet.sites[C714.MCX_WORK[i]] for i in range(3))
# C873SRC 000647|    cell, _axis, target, left_mode, right_mode = seam
# C873SRC 000648|    left = C870.physical_lift(graph.B(graph.vertex_index[(cell, left_mode)]), context)
# C873SRC 000649|    right = C870.physical_lift(graph.B(graph.vertex_index[(target, right_mode)]), context)
# C873SRC 000650|
# C873SRC 000651|    def zsupport(row):
# C873SRC 000652|        return tuple(site for index, site in enumerate(context.sites) if (row.z >> index) & 1)
# C873SRC 000653|
# C873SRC 000654|    def cnot(a, b, kind): return local_instruction(C870, kind, (a, b), C714.CNOT)
# C873SRC 000655|    def x(site, kind): return local_instruction(C870, kind, (site,), C714.X)
# C873SRC 000656|    def primitive(a, b, t, prefix, clean=False):
# C873SRC 000657|        source = list(C714.toffoli_primitives(0, 1, 2))
# C873SRC 000658|        if clean: del source[1]
# C873SRC 000659|        mats = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
# C873SRC 000660|        sites = (a, b, t)
# C873SRC 000661|        return tuple(local_instruction(C870, prefix + kind, tuple(sites[i] for i in wires), mats[kind]) for kind, wires in source)
# C873SRC 000662|    def predicate(sign, prefix, clean):
# C873SRC 000663|        negative = qv if sign > 0 else qu
# C873SRC 000664|        return (x(negative, prefix + "negative_X"),) + primitive(qu, qv, current, prefix + ("clean_target_Toffoli_" if clean else "Toffoli_"), clean=clean) + (x(negative, prefix + "negative_X"),)
# C873SRC 000665|    def fredkin(left_rail, right_rail, prefix):
# C873SRC 000666|        return (cnot(left_rail, right_rail, prefix + "outer_CNOT"),) + primitive(current, right_rail, left_rail, prefix + "Toffoli_") + (cnot(left_rail, right_rail, prefix + "outer_CNOT"),)
# C873SRC 000667|    def shift(direction, prefix):
# C873SRC 000668|        order = range(15, -1, -1) if direction > 0 else range(16)
# C873SRC 000669|        return tuple(g for edge in order for g in fredkin(rails[edge], rails[edge + 1], f"{prefix}{edge}_"))
# C873SRC 000670|
# C873SRC 000671|    endpoint_pre = tuple(cnot(site, qu, "F17_pre_left_B") for site in zsupport(left)) + tuple(cnot(site, qv, "F17_pre_right_B") for site in zsupport(right))
# C873SRC 000672|    selected = []
# C873SRC 000673|    for rotation in C871.selected_seam_rotations(graph, seam):
# C873SRC 000674|        _physical, _axes, word = local_compile(C870, rotation, context)
# C873SRC 000675|        selected.extend(word)
# C873SRC 000676|    branch = (
# C873SRC 000677|        predicate(1, "F17_positive_compute_", True)
# C873SRC 000678|        + shift(alpha, "F17_positive_shift_")
# C873SRC 000679|        + predicate(1, "F17_positive_uncompute_", False)
# C873SRC 000680|        + predicate(-1, "F17_negative_compute_", True)
# C873SRC 000681|        + shift(-alpha, "F17_negative_shift_")
# C873SRC 000682|        + predicate(-1, "F17_negative_uncompute_", False)
# C873SRC 000683|    )
# C873SRC 000684|    cleanup = tuple(cnot(site, qu, "F17_clean_right_B_into_q_u") for site in zsupport(right)) + tuple(cnot(site, qv, "F17_clean_left_B_into_q_v") for site in zsupport(left))
# C873SRC 000685|    return endpoint_pre + tuple(selected) + branch + cleanup, packet.basis
# C873SRC 000686|
# C873SRC 000687|
# C873SRC 000688|def coframe_path(left, right, basis):
# C873SRC 000689|    delta = tuple(b - a for a, b in zip(left, right))
# C873SRC 000690|    coefficients = tuple(sum(delta[i] * direction[i] for i in range(3)) for direction in basis)
# C873SRC 000691|    current = left; path = [left]
# C873SRC 000692|    for coefficient, direction in zip(coefficients, basis):
# C873SRC 000693|        step = direction if coefficient >= 0 else scale(-1, direction)
# C873SRC 000694|        for _ in range(abs(coefficient)):
# C873SRC 000695|            current = add(current, step); path.append(current)
# C873SRC 000696|    if current != right: raise AssertionError((left, right, current))
# C873SRC 000697|    return tuple(path)
# C873SRC 000698|
# C873SRC 000699|
# C873SRC 000700|def route_digest(C870, word, basis):
# C873SRC 000701|    digest = sha256(); routed = 0
# C873SRC 000702|    for instruction in word:
# C873SRC 000703|        if len(instruction.sites) == 1:
# C873SRC 000704|            routed += 1
# C873SRC 000705|            digest.update(repr(signature(C870, instruction)).encode())
# C873SRC 000706|        else:
# C873SRC 000707|            path = coframe_path(*instruction.sites, basis)
# C873SRC 000708|            routed += 2 * (len(path) - 1) - 1
# C873SRC 000709|            digest.update((instruction.kind + repr(path) + matrix_digest(C870, instruction.matrix)).encode())
# C873SRC 000710|    return digest.hexdigest(), routed
# C873SRC 000711|
# C873SRC 000712|
# C873SRC 000713|def schedule_color(seam):
# C873SRC 000714|    cell, axis = seam[0], seam[1]
# C873SRC 000715|    return axis, cell[0] & 1, cell[1] & 1, cell[2] & 1
# C873SRC 000716|
# C873SRC 000717|
# C873SRC 000718|def schedule_key(color):
# C873SRC 000719|    axis, x, y, z = color; values = (x, y, z)
# C873SRC 000720|    return axis, values[axis], values[(axis + 1) % 3], values[(axis + 2) % 3]
# C873SRC 000721|
# C873SRC 000722|
# C873SRC 000723|def emitted_schedule_certificate(root, C870, C871, C714):
# C873SRC 000724|    graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
# C873SRC 000725|    context = C870.physical_context(graph)
# C873SRC 000726|    constraints = C870.physical_stabilizers(context)
# C873SRC 000727|    groups = defaultdict(list)
# C873SRC 000728|    logical_counts = []; routed_counts = []; word_hashes = []
# C873SRC 000729|    row_anticommutators = endpoint_anticommutators = 0
# C873SRC 000730|    maximum_raw_minus_i_residual = maximum_corrected_residual = 0.0
# C873SRC 000731|    for seam in C870.graph_seams(graph):
# C873SRC 000732|        word, basis = independent_emitted_word(C870, C871, C714, graph, context, seam)
# C873SRC 000733|        wd = word_digest(C870, word); rd, routed = route_digest(C870, word, basis)
# C873SRC 000734|        row = (seam, wd, rd)
# C873SRC 000735|        groups[schedule_color(seam)].append(row)
# C873SRC 000736|        logical_counts.append(len(word)); routed_counts.append(routed); word_hashes.append(wd)
# C873SRC 000737|        rotations = C871.selected_seam_rotations(graph, seam)
# C873SRC 000738|        abstract = tuple(rotation.row for rotation in rotations)
# C873SRC 000739|        target = poly_add(C870, *(poly_scale(C870, {pauli: 1 + 0j}, 0.5) for pauli in abstract))
# C873SRC 000740|        factored = {C870.Pauli(): 1 + 0j}
# C873SRC 000741|        for pauli in abstract:
# C873SRC 000742|            factor = {
# C873SRC 000743|                C870.Pauli(): complex(math.cos(math.pi / 4)),
# C873SRC 000744|                pauli: complex(-1j * math.sin(math.pi / 4)),
# C873SRC 000745|            }
# C873SRC 000746|            factored = poly_mul(C870, factor, factored)
# C873SRC 000747|        maximum_raw_minus_i_residual = max(
# C873SRC 000748|            maximum_raw_minus_i_residual,
# C873SRC 000749|            poly_residual(C870, factored, poly_scale(C870, target, -1j)),
# C873SRC 000750|        )
# C873SRC 000751|        maximum_corrected_residual = max(
# C873SRC 000752|            maximum_corrected_residual,
# C873SRC 000753|            poly_residual(C870, poly_scale(C870, factored, 1j), target),
# C873SRC 000754|        )
# C873SRC 000755|        for rotation in rotations:
# C873SRC 000756|            physical = C870.physical_lift(rotation.row, context)
# C873SRC 000757|            row_anticommutators += sum(not physical.commutes(stabilizer) for stabilizer in constraints)
# C873SRC 000758|        for cell, mode in ((seam[0], seam[3]), (seam[2], seam[4])):
# C873SRC 000759|            physical_b = C870.physical_lift(graph.B(graph.vertex_index[(cell, mode)]), context)
# C873SRC 000760|            endpoint_anticommutators += sum(not physical_b.commutes(stabilizer) for stabilizer in constraints)
# C873SRC 000761|    ordered = tuple(sorted(groups, key=schedule_key))
# C873SRC 000762|    schedule = tuple(
# C873SRC 000763|        (color, tuple((seam, wd, rd) for seam, wd, rd in sorted(groups[color], key=lambda item: item[0][0])))
# C873SRC 000764|        for color in ordered
# C873SRC 000765|    )
# C873SRC 000766|    digest = sha256(repr(schedule).encode()).hexdigest()
# C873SRC 000767|    receipt = json.loads((root / PHYSICAL_RECEIPT_REL).read_text())
# C873SRC 000768|    expected = receipt["fixtures"][0]["augmented_epoch_ledgers"]["A_F17_only"]["seam_stage_schedule_sha256"]
# C873SRC 000769|    return {
# C873SRC 000770|        "shape": (2, 2, 2), "seams": len(logical_counts),
# C873SRC 000771|        "schedule_sha256": digest, "physical_core_F17_only_schedule_sha256": expected,
# C873SRC 000772|        "schedule_hash_match": digest == expected,
# C873SRC 000773|        "total_logical_instructions": sum(logical_counts),
# C873SRC 000774|        "logical_min_max": (min(logical_counts), max(logical_counts)),
# C873SRC 000775|        "total_routed_gates": sum(routed_counts),
# C873SRC 000776|        "routed_min_max": (min(routed_counts), max(routed_counts)),
# C873SRC 000777|        "independent_word_sha256": word_hashes,
# C873SRC 000778|        "all_seam_rotation_physical_constraint_anticommutators": row_anticommutators,
# C873SRC 000779|        "all_endpoint_B_physical_constraint_anticommutators": endpoint_anticommutators,
# C873SRC 000780|        "all_seam_maximum_raw_to_minus_i_FSWAP_residual": clean_float(maximum_raw_minus_i_residual),
# C873SRC 000781|        "all_seam_maximum_formal_corrected_residual": clean_float(maximum_corrected_residual),
# C873SRC 000782|    }
# C873SRC 000783|
# C873SRC 000784|
# C873SRC 000785|def rref_mod(matrix, p=F17):
# C873SRC 000786|    a = np.asarray(matrix, dtype=np.int64).copy() % p; row = 0; pivots = []
# C873SRC 000787|    for col in range(a.shape[1]):
# C873SRC 000788|        pivot = next((r for r in range(row, a.shape[0]) if a[r, col] % p), None)
# C873SRC 000789|        if pivot is None: continue
# C873SRC 000790|        a[[row, pivot]] = a[[pivot, row]]
# C873SRC 000791|        a[row] = a[row] * pow(int(a[row, col]), -1, p) % p
# C873SRC 000792|        for r in range(a.shape[0]):
# C873SRC 000793|            if r != row and a[r, col]: a[r] = (a[r] - int(a[r, col]) * a[row]) % p
# C873SRC 000794|        pivots.append(col); row += 1
# C873SRC 000795|        if row == a.shape[0]: break
# C873SRC 000796|    return a, pivots
# C873SRC 000797|
# C873SRC 000798|
# C873SRC 000799|def solve_mod(matrix, rhs, p=F17):
# C873SRC 000800|    a = np.asarray(matrix, dtype=np.int64) % p
# C873SRC 000801|    aug, pivots = rref_mod(np.column_stack((a, np.asarray(rhs, dtype=np.int64) % p)), p)
# C873SRC 000802|    x = np.zeros(a.shape[1], dtype=np.int64)
# C873SRC 000803|    for r, pivot in enumerate(q for q in pivots if q < a.shape[1]): x[pivot] = aug[r, -1]
# C873SRC 000804|    if not np.array_equal(a @ x % p, np.asarray(rhs) % p): raise AssertionError("inconsistent")
# C873SRC 000805|    return x
# C873SRC 000806|
# C873SRC 000807|
# C873SRC 000808|@dataclass(frozen=True)
# C873SRC 000809|class Complex:
# C873SRC 000810|    vertices: tuple
# C873SRC 000811|    edges: tuple
# C873SRC 000812|    incidence: np.ndarray
# C873SRC 000813|    faces: np.ndarray
# C873SRC 000814|
# C873SRC 000815|
# C873SRC 000816|@dataclass(frozen=True)
# C873SRC 000817|class FixedStarBackground:
# C873SRC 000818|    label: str
# C873SRC 000819|    particle_number: int
# C873SRC 000820|    field: tuple[int, ...]
# C873SRC 000821|
# C873SRC 000822|
# C873SRC 000823|def open_box(dims):
# C873SRC 000824|    vertices = tuple(product(*(range(n) for n in dims))); index = {v: i for i, v in enumerate(vertices)}
# C873SRC 000825|    edges = []; lookup = {}
# C873SRC 000826|    for vertex in vertices:
# C873SRC 000827|        for axis in range(3):
# C873SRC 000828|            if vertex[axis] + 1 < dims[axis]:
# C873SRC 000829|                target = list(vertex); target[axis] += 1; target = tuple(target)
# C873SRC 000830|                lookup[(vertex, target)] = len(edges); edges.append((index[vertex], index[target], axis))
# C873SRC 000831|    incidence = np.zeros((len(vertices), len(edges)), dtype=np.int64)
# C873SRC 000832|    for e, (u, v, _axis) in enumerate(edges): incidence[u, e] = -1; incidence[v, e] = 1
# C873SRC 000833|    faces = []
# C873SRC 000834|    for a in range(3):
# C873SRC 000835|        for b in range(a + 1, 3):
# C873SRC 000836|            for base in vertices:
# C873SRC 000837|                if base[a] + 1 >= dims[a] or base[b] + 1 >= dims[b]: continue
# C873SRC 000838|                ea = tuple(int(i == a) for i in range(3)); eb = tuple(int(i == b) for i in range(3))
# C873SRC 000839|                va = add(base, ea); vb = add(base, eb); vab = add(base, ea, eb)
# C873SRC 000840|                row = np.zeros(len(edges), dtype=np.int64)
# C873SRC 000841|                row[lookup[(base, va)]] += 1; row[lookup[(va, vab)]] += 1
# C873SRC 000842|                row[lookup[(vb, vab)]] -= 1; row[lookup[(base, vb)]] -= 1
# C873SRC 000843|                faces.append(row % F17)
# C873SRC 000844|    return Complex(vertices, tuple(edges), incidence % F17, np.asarray(faces, dtype=np.int64).T if faces else np.zeros((len(edges), 0), int))
# C873SRC 000845|
# C873SRC 000846|
# C873SRC 000847|def nullspace_mod(matrix):
# C873SRC 000848|    a, pivots = rref_mod(matrix); free = [c for c in range(a.shape[1]) if c not in pivots]; rows = []
# C873SRC 000849|    for f in free:
# C873SRC 000850|        x = np.zeros(a.shape[1], dtype=np.int64); x[f] = 1
# C873SRC 000851|        for r, pivot in enumerate(pivots): x[pivot] = -a[r, f] % F17
# C873SRC 000852|        rows.append(x)
# C873SRC 000853|    return np.asarray(rows, dtype=np.int64).T if rows else np.zeros((a.shape[1], 0), int)
# C873SRC 000854|
# C873SRC 000855|
# C873SRC 000856|def rank_mod(matrix):
# C873SRC 000857|    return len(rref_mod(matrix)[1])
# C873SRC 000858|
# C873SRC 000859|
# C873SRC 000860|def edge_rails(graph: Complex, edge_index: int):
# C873SRC 000861|    tail_index, _head_index, axis = graph.edges[edge_index]
# C873SRC 000862|    tail = graph.vertices[tail_index]
# C873SRC 000863|    unit = tuple(int(index == axis) for index in range(3))
# C873SRC 000864|    basis = (
# C873SRC 000865|        unit,
# C873SRC 000866|        tuple(int(index == (axis + 1) % 3) for index in range(3)),
# C873SRC 000867|        tuple(int(index == (axis + 2) % 3) for index in range(3)),
# C873SRC 000868|    )
# C873SRC 000869|    midpoint = add(scale(16, tail), scale(8, unit))
# C873SRC 000870|    return tuple(at(midpoint, basis, offset) for offset in RAIL_LOCAL_OFFSETS), midpoint
# C873SRC 000871|
# C873SRC 000872|
# C873SRC 000873|def shifted_label(label: int, direction: int, omitted: int | None = None):
# C873SRC 000874|    position = label
# C873SRC 000875|    order = tuple(range(15, -1, -1) if direction > 0 else range(16))
# C873SRC 000876|    for step, left in enumerate(order):
# C873SRC 000877|        if step == omitted:
# C873SRC 000878|            continue
# C873SRC 000879|        right = left + 1
# C873SRC 000880|        if position == left:
# C873SRC 000881|            position = right
# C873SRC 000882|        elif position == right:
# C873SRC 000883|            position = left
# C873SRC 000884|    return position
# C873SRC 000885|
# C873SRC 000886|
# C873SRC 000887|def local_constraint_certificate(C870, C871):
# C873SRC 000888|    rows = []
# C873SRC 000889|    deletion_tests = deletion_undetected = 0
# C873SRC 000890|    for dims in ((2, 2, 2), (3, 3, 3), (3, 2, 2)):
# C873SRC 000891|        graph = open_box(dims)
# C873SRC 000892|        incidence_rank = rank_mod(graph.incidence)
# C873SRC 000893|        face_rank = rank_mod(graph.faces)
# C873SRC 000894|        cycle_rank = len(graph.edges) - incidence_rank
# C873SRC 000895|        boundary_squared = int(np.count_nonzero(graph.incidence @ graph.faces % F17))
# C873SRC 000896|        rails = {edge: edge_rails(graph, edge)[0] for edge in range(len(graph.edges))}
# C873SRC 000897|        onehot_path_failures = sum(
# C873SRC 000898|            sum(sum(abs(a - b) for a, b in zip(left, right)) != 1
# C873SRC 000899|                for left, right in zip(bank, bank[1:]))
# C873SRC 000900|            for bank in rails.values()
# C873SRC 000901|        )
# C873SRC 000902|        rail_overlap_sites = sum(
# C873SRC 000903|            len(set(bank) & set(rails[prior]))
# C873SRC 000904|            for edge, bank in rails.items() for prior in range(edge)
# C873SRC 000905|        )
# C873SRC 000906|        plaquette_word_failures = layer_collisions = 0
# C873SRC 000907|        plaquette_support_max = 0
# C873SRC 000908|        for face_index in range(graph.faces.shape[1]):
# C873SRC 000909|            column = graph.faces[:, face_index]
# C873SRC 000910|            boundary = tuple(
# C873SRC 000911|                (edge, 1 if int(column[edge]) == 1 else -1)
# C873SRC 000912|                for edge in range(len(graph.edges)) if int(column[edge])
# C873SRC 000913|            )
# C873SRC 000914|            plaquette_word_failures += len(boundary) != 4
# C873SRC 000915|            support = set().union(*(set(rails[edge]) for edge, _ in boundary))
# C873SRC 000916|            plaquette_support_max = max(plaquette_support_max, len(support))
# C873SRC 000917|            plaquette_word_failures += len(support) != 68
# C873SRC 000918|            for step in range(16):
# C873SRC 000919|                sites = []
# C873SRC 000920|                for edge, direction in boundary:
# C873SRC 000921|                    left_index = (15 - step) if direction > 0 else step
# C873SRC 000922|                    pair = (rails[edge][left_index], rails[edge][left_index + 1])
# C873SRC 000923|                    plaquette_word_failures += (
# C873SRC 000924|                        sum(abs(a - b) for a, b in zip(*pair)) != 1
# C873SRC 000925|                    )
# C873SRC 000926|                    sites.extend(pair)
# C873SRC 000927|                layer_collisions += len(sites) != len(set(sites))
# C873SRC 000928|            for _edge, direction in boundary:
# C873SRC 000929|                full = tuple((label + direction) % F17 for label in range(F17))
# C873SRC 000930|                for omitted in range(16):
# C873SRC 000931|                    damaged = tuple(
# C873SRC 000932|                        shifted_label(label, direction, omitted)
# C873SRC 000933|                        for label in range(F17)
# C873SRC 000934|                    )
# C873SRC 000935|                    deletion_tests += 1
# C873SRC 000936|                    deletion_undetected += damaged == full
# C873SRC 000937|
# C873SRC 000938|        physical_graph = C870.prep.OpenReferenceGraph(graph.vertices)
# C873SRC 000939|        context = C870.physical_context(physical_graph)
# C873SRC 000940|        auxiliary = C871.J870.auxiliary_registers(physical_graph)
