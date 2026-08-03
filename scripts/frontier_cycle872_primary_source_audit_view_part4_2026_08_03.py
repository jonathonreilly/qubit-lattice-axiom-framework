#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 872 primary source, part 4/4."""

TARGET_SOURCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py"
PART_ORDINAL = 4
PART_COUNT = 4
FIRST_SOURCE_LINE = 1456
LAST_SOURCE_LINE = 1940
TOTAL_SOURCE_LINES = 1940
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "c1b32ef8e2a870128b7081a88b920b85c84123d04f98a165bfc7225dcfc716e4"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C872SRC 001456|                            C871.transform_signature(signature, right), left
# C872SRC 001457|                        ) != C871.transform_signature(signature, composed)
# C872SRC 001458|                    )
# C872SRC 001459|                for path in paths:
# C872SRC 001460|                    counts["path_product_rows"] += 1
# C872SRC 001461|                    counts["path_product_failures"] += (
# C872SRC 001462|                        C871.transform_path(C871.transform_path(path, right), left)
# C872SRC 001463|                        != C871.transform_path(path, composed)
# C872SRC 001464|                    )
# C872SRC 001465|    return {
# C872SRC 001466|        "used_packet_M2_per_seam": C714.N,
# C872SRC 001467|        "retained_spatial_current_M2_per_seam": 1,
# C872SRC 001468|        "total_resource_M2_per_seam": C714.N + 1,
# C872SRC 001469|        "representative_axes": 3,
# C872SRC 001470|        "proper_frames": len(frames),
# C872SRC 001471|        "ordered_frame_products": len(frames) ** 2,
# C872SRC 001472|        **dict(counts),
# C872SRC 001473|        "scope": (
# C872SRC 001474|            "passive coordinate/program/declared-coframe-route representation; "
# C872SRC 001475|            "not active covariance of the single-rail allocator"
# C872SRC 001476|        ),
# C872SRC 001477|    }
# C872SRC 001478|
# C872SRC 001479|
# C872SRC 001480|def c4_orbits(available):
# C872SRC 001481|    def rotate(row):
# C872SRC 001482|        a, b, c = row
# C872SRC 001483|        return a, -c, b
# C872SRC 001484|    seen = set()
# C872SRC 001485|    output = []
# C872SRC 001486|    for row in sorted(available):
# C872SRC 001487|        if row in seen:
# C872SRC 001488|            continue
# C872SRC 001489|        orbit = []
# C872SRC 001490|        current = row
# C872SRC 001491|        for _ in range(4):
# C872SRC 001492|            orbit.append(current)
# C872SRC 001493|            current = rotate(current)
# C872SRC 001494|        orbit = frozenset(orbit)
# C872SRC 001495|        seen.update(orbit)
# C872SRC 001496|        if len(orbit) == 4 and orbit <= available:
# C872SRC 001497|            output.append(orbit)
# C872SRC 001498|    return tuple(sorted(output, key=lambda row: repr(sorted(row))))
# C872SRC 001499|
# C872SRC 001500|
# C872SRC 001501|def reflected(orbit):
# C872SRC 001502|    return frozenset((-a, b, -c) for a, b, c in orbit)
# C872SRC 001503|
# C872SRC 001504|
# C872SRC 001505|def orbit_inventory(graph, context, seam):
# C872SRC 001506|    midpoint = C871.seam_midpoint(seam[0], seam[1])
# C872SRC 001507|    basis = C871.local_coframe(seam[1])
# C872SRC 001508|    blocked = set(context.sites) | J870.auxiliary_registers(graph)
# C872SRC 001509|    def physical(local):
# C872SRC 001510|        site = midpoint
# C872SRC 001511|        for coefficient, direction in zip(local, basis):
# C872SRC 001512|            site = C871.add(site, C871.scale(coefficient, direction))
# C872SRC 001513|        return site
# C872SRC 001514|    available = {
# C872SRC 001515|        local for local in product(range(-3, 4), repeat=3)
# C872SRC 001516|        if physical(local) not in blocked
# C872SRC 001517|    }
# C872SRC 001518|    return c4_orbits(available), physical
# C872SRC 001519|
# C872SRC 001520|
# C872SRC 001521|def four_rail_allocator_certificate():
# C872SRC 001522|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 001523|    context = C870.physical_context(graph)
# C872SRC 001524|    all_orbits, _physical = orbit_inventory(graph, context, C870.graph_seams(graph)[0])
# C872SRC 001525|    orbit_set = set(all_orbits)
# C872SRC 001526|    fixed = tuple(sorted(
# C872SRC 001527|        (orbit for orbit in all_orbits if reflected(orbit) == orbit),
# C872SRC 001528|        key=lambda row: repr(sorted(row)),
# C872SRC 001529|    ))
# C872SRC 001530|    pairs = []
# C872SRC 001531|    seen = set(fixed)
# C872SRC 001532|    for orbit in all_orbits:
# C872SRC 001533|        if orbit in seen:
# C872SRC 001534|            continue
# C872SRC 001535|        partner = reflected(orbit)
# C872SRC 001536|        if partner not in orbit_set:
# C872SRC 001537|            raise AssertionError("missing reflection partner")
# C872SRC 001538|        pair = tuple(sorted((orbit, partner), key=lambda row: repr(sorted(row))))
# C872SRC 001539|        pairs.append(pair)
# C872SRC 001540|        seen.update(pair)
# C872SRC 001541|    pairs.sort(key=repr)
# C872SRC 001542|    selected = tuple(fixed[:5]) + tuple(orbit for pair in pairs[:27] for orbit in pair)
# C872SRC 001543|    selected_set = set(selected)
# C872SRC 001544|    sites = frozenset(site for orbit in selected for site in orbit)
# C872SRC 001545|    frames = C871.proper_frames()
# C872SRC 001546|
# C872SRC 001547|    def local_transform(axis, frame):
# C872SRC 001548|        target_axis, _sign = C871.signed_axis(frame, axis)
# C872SRC 001549|        source_basis = np.column_stack(C871.local_coframe(axis))
# C872SRC 001550|        target_basis = np.column_stack(C871.local_coframe(target_axis))
# C872SRC 001551|        return target_axis, np.asarray(target_basis.T @ frame @ source_basis, dtype=int)
# C872SRC 001552|
# C872SRC 001553|    counts = Counter()
# C872SRC 001554|    identity_register_failures = 0
# C872SRC 001555|    half_action_failures = 0
# C872SRC 001556|    for axis in range(3):
# C872SRC 001557|        for frame in frames:
# C872SRC 001558|            _target_axis, matrix = local_transform(axis, frame)
# C872SRC 001559|            moved_orbits = tuple(
# C872SRC 001560|                frozenset(tuple(map(int, matrix @ np.asarray(site))) for site in orbit)
# C872SRC 001561|                for orbit in selected
# C872SRC 001562|            )
# C872SRC 001563|            counts["frame_site_rows"] += len(sites)
# C872SRC 001564|            counts["frame_orbit_rows"] += len(selected)
# C872SRC 001565|            counts["site_set_failures"] += frozenset(
# C872SRC 001566|                tuple(map(int, matrix @ np.asarray(site))) for site in sites
# C872SRC 001567|            ) != sites
# C872SRC 001568|            counts["orbit_membership_failures"] += sum(
# C872SRC 001569|                orbit not in selected_set for orbit in moved_orbits
# C872SRC 001570|            )
# C872SRC 001571|            counts["orbit_bijection_failures"] += len(set(moved_orbits)) != len(selected)
# C872SRC 001572|            identity_register_failures += sum(
# C872SRC 001573|                moved != original for moved, original in zip(moved_orbits, selected)
# C872SRC 001574|            )
# C872SRC 001575|            _moved_axis, sign = C871.signed_axis(frame, axis)
# C872SRC 001576|            if sign < 0:
# C872SRC 001577|                # Damage: keep only the axial C4 half-action and suppress the
# C872SRC 001578|                # reflection of the axial local coordinate.
# C872SRC 001579|                damaged = np.array(matrix, copy=True)
# C872SRC 001580|                damaged[0, :] *= -1
# C872SRC 001581|                half_action_failures += frozenset(
# C872SRC 001582|                    tuple(map(int, damaged @ np.asarray(site))) for site in sites
# C872SRC 001583|                ) != sites
# C872SRC 001584|        for left in frames:
# C872SRC 001585|            for right in frames:
# C872SRC 001586|                intermediate, right_matrix = local_transform(axis, right)
# C872SRC 001587|                final_axis, left_matrix = local_transform(intermediate, left)
# C872SRC 001588|                product_axis, product_matrix = local_transform(axis, left @ right)
# C872SRC 001589|                counts["products"] += 1
# C872SRC 001590|                counts["axis_product_failures"] += final_axis != product_axis
# C872SRC 001591|                counts["matrix_product_failures"] += not np.array_equal(
# C872SRC 001592|                    left_matrix @ right_matrix, product_matrix
# C872SRC 001593|                )
# C872SRC 001594|                for site in sites:
# C872SRC 001595|                    row = np.asarray(site)
# C872SRC 001596|                    counts["site_product_rows"] += 1
# C872SRC 001597|                    counts["site_product_failures"] += not np.array_equal(
# C872SRC 001598|                        left_matrix @ (right_matrix @ row), product_matrix @ row
# C872SRC 001599|                    )
# C872SRC 001600|                for orbit in selected:
# C872SRC 001601|                    twice = frozenset(
# C872SRC 001602|                        tuple(map(int, left_matrix @ (right_matrix @ np.asarray(site))))
# C872SRC 001603|                        for site in orbit
# C872SRC 001604|                    )
# C872SRC 001605|                    direct = frozenset(
# C872SRC 001606|                        tuple(map(int, product_matrix @ np.asarray(site))) for site in orbit
# C872SRC 001607|                    )
# C872SRC 001608|                    counts["orbit_product_rows"] += 1
# C872SRC 001609|                    counts["orbit_product_failures"] += twice != direct
# C872SRC 001610|
# C872SRC 001611|    geometry = []
# C872SRC 001612|    reference_inventory = set(all_orbits)
# C872SRC 001613|    for length in (2, 3, 4, 5):
# C872SRC 001614|        local_graph = C870.prep.OpenReferenceGraph(cells(length))
# C872SRC 001615|        local_context = C870.physical_context(local_graph)
# C872SRC 001616|        blocked = set(local_context.sites) | J870.auxiliary_registers(local_graph)
# C872SRC 001617|        banks = []
# C872SRC 001618|        inventory_failures = 0
# C872SRC 001619|        for seam in C870.graph_seams(local_graph):
# C872SRC 001620|            inventory, physical = orbit_inventory(local_graph, local_context, seam)
# C872SRC 001621|            inventory_failures += set(inventory) != reference_inventory
# C872SRC 001622|            banks.append({physical(site) for orbit in selected for site in orbit})
# C872SRC 001623|        geometry.append({
# C872SRC 001624|            "length": length,
# C872SRC 001625|            "seams": len(banks),
# C872SRC 001626|            "M2_union": len(set().union(*banks)),
# C872SRC 001627|            "inventory_failures": inventory_failures,
# C872SRC 001628|            "native_aux_collisions": sum(len(bank & blocked) for bank in banks),
# C872SRC 001629|            "cross_seam_overlap_pairs": sum(
# C872SRC 001630|                bool(left & right)
# C872SRC 001631|                for index, left in enumerate(banks) for right in banks[:index]
# C872SRC 001632|            ),
# C872SRC 001633|        })
# C872SRC 001634|    return {
# C872SRC 001635|        "status": "separate geometric covariance candidate",
# C872SRC 001636|        "used_by_executable_epoch": False,
# C872SRC 001637|        "available_C4_orbits": len(all_orbits),
# C872SRC 001638|        "reflection_fixed_orbits": len(fixed),
# C872SRC 001639|        "reflection_paired_orbit_pairs": len(pairs),
# C872SRC 001640|        "selected_fixed_orbits": 5,
# C872SRC 001641|        "selected_reflected_pairs": 27,
# C872SRC 001642|        "register_orbits": len(selected),
# C872SRC 001643|        "rails_per_register": 4,
# C872SRC 001644|        "M2_per_seam": len(sites),
# C872SRC 001645|        **dict(counts),
# C872SRC 001646|        "geometry": geometry,
# C872SRC 001647|        "half_action_deletion_detections": half_action_failures,
# C872SRC 001648|        "register_permutation_deletion_detections": identity_register_failures,
# C872SRC 001649|        "missing_for_execution": (
# C872SRC 001650|            "a transported four-rail Cycle714 word implementing the induced register/rail permutation"
# C872SRC 001651|        ),
# C872SRC 001652|    }
# C872SRC 001653|
# C872SRC 001654|
# C872SRC 001655|def noncommuting_stage_reorder_control():
# C872SRC 001656|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 001657|    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
# C872SRC 001658|    factors = tuple(
# C872SRC 001659|        (factor, tuple(group))
# C872SRC 001660|        for factor, group in groupby(rotations, key=lambda row: row.factor)
# C872SRC 001661|    )
# C872SRC 001662|    seams = tuple(rows for factor, rows in factors if factor[0] == "seam")
# C872SRC 001663|    contacts = tuple(rows for factor, rows in factors if factor[0] == "contact")
# C872SRC 001664|
# C872SRC 001665|    def polynomial(rows):
# C872SRC 001666|        output = {C870.Pauli(): 1.0 + 0.0j}
# C872SRC 001667|        for rotation in rows:
# C872SRC 001668|            output = C870.poly_mul(
# C872SRC 001669|                C870.rotation_polynomial(rotation.row, rotation.angle), output
# C872SRC 001670|            )
# C872SRC 001671|        return output
# C872SRC 001672|
# C872SRC 001673|    best = 0.0
# C872SRC 001674|    witness = None
# C872SRC 001675|    for seam_index, seam_rows in enumerate(seams):
# C872SRC 001676|        left = polynomial(seam_rows)
# C872SRC 001677|        for contact_index, contact_rows in enumerate(contacts):
# C872SRC 001678|            if not any(
# C872SRC 001679|                not a.row.commutes(b.row) for a in seam_rows for b in contact_rows
# C872SRC 001680|            ):
# C872SRC 001681|                continue
# C872SRC 001682|            right = polynomial(contact_rows)
# C872SRC 001683|            residual = C870.poly_residual(
# C872SRC 001684|                C870.poly_mul(left, right), C870.poly_mul(right, left)
# C872SRC 001685|            )
# C872SRC 001686|            if residual > best:
# C872SRC 001687|                best = residual
# C872SRC 001688|                witness = (seam_index, contact_index)
# C872SRC 001689|    return {
# C872SRC 001690|        "mutation": "move a seam factor across a noncommuting contact factor",
# C872SRC 001691|        "witness": witness,
# C872SRC 001692|        "commutator_residual": best,
# C872SRC 001693|        "detected": best > 1.0e-3,
# C872SRC 001694|    }
# C872SRC 001695|
# C872SRC 001696|
# C872SRC 001697|def association_firewall():
# C872SRC 001698|    C610 = C704.C610
# C872SRC 001699|    pairs = []
# C872SRC 001700|    failures = 0
# C872SRC 001701|    for spatial in (0, 1):
# C872SRC 001702|        for causal in (-1, 1):
# C872SRC 001703|            packet = C704.ReversiblePacketBank(bank=1)
# C872SRC 001704|            chain = C610.EventChain(bank=1)
# C872SRC 001705|            left = packet.append(
# C872SRC 001706|                0, 66, 1, causal, binder=1,
# C872SRC 001707|                actuality=1, admissibility=1, law_domain=1,
# C872SRC 001708|            )
# C872SRC 001709|            right = chain.admit(
# C872SRC 001710|                0, causal, certificate=1, binder=1,
# C872SRC 001711|                actuality=1, admissibility=1, law_domain=1,
# C872SRC 001712|            )
# C872SRC 001713|            failures += left != "admitted" or right != "admitted"
# C872SRC 001714|            pairs.append((spatial, causal))
# C872SRC 001715|    return {
# C872SRC 001716|        "lawful_pairs": pairs,
# C872SRC 001717|        "acceptance_failures": failures,
# C872SRC 001718|        "spatial_to_causal_is_function": False,
# C872SRC 001719|        "causal_orientation": "supplied",
# C872SRC 001720|        "Cycle612_shared_order_reads_orientation": False,
# C872SRC 001721|        "missing_map": (
# C872SRC 001722|            "absent from these pinned interfaces: identity co-registration from seam "
# C872SRC 001723|            "opportunity to signed tick crossing, followed by EventCell.orientation = "
# C872SRC 001724|            "tick-crossing orientation; no global nonexistence claim"
# C872SRC 001725|        ),
# C872SRC 001726|    }
# C872SRC 001727|
# C872SRC 001728|
# C872SRC 001729|def failure_list(report):
# C872SRC 001730|    failures = []
# C872SRC 001731|    provenance = report["provenance"]
# C872SRC 001732|    if provenance["missing_inputs"] or provenance["pin_failures"]:
# C872SRC 001733|        failures.append("source provenance")
# C872SRC 001734|    if provenance["theorem_note_pin_failure"]:
# C872SRC 001735|        failures.append("theorem note pin")
# C872SRC 001736|    stream = report["physical_epoch_stream"]
# C872SRC 001737|    if any(stream["construction_failure_census"].values()):
# C872SRC 001738|        failures.append("physical epoch stream")
# C872SRC 001739|    if stream["first_forward_swap_deletion_detections"] <= 0:
# C872SRC 001740|        failures.append("inactive physical-stream first-forward-SWAP deletion")
# C872SRC 001741|    mutations = report["physical_macro_mutations"]
# C872SRC 001742|    if mutations["NN_failures"]:
# C872SRC 001743|        failures.append("physical macro mutation NN")
# C872SRC 001744|    if mutations["wrong_side_digest_detections"] != mutations["seams"]:
# C872SRC 001745|        failures.append("inactive physical wrong-side mutation")
# C872SRC 001746|    if mutations["seam_deletion_digest_detections"] != mutations["seams"]:
# C872SRC 001747|        failures.append("inactive physical seam-deletion mutation")
# C872SRC 001748|    for fixture in report["epoch_fixtures"]:
# C872SRC 001749|        prefix = f"L{fixture['length']}"
# C872SRC 001750|        if fixture["packet_bank_pair_overlap_pairs"] or fixture[
# C872SRC 001751|            "resource_bank_pair_overlap_pairs"
# C872SRC 001752|        ]:
# C872SRC 001753|            failures.append(prefix + " resource overlap")
# C872SRC 001754|        if any(fixture["spatial_output_geometry_failures"].values()):
# C872SRC 001755|            failures.append(prefix + " spatial output geometry")
# C872SRC 001756|        if any(fixture["binding_failures"].values()):
# C872SRC 001757|            failures.append(prefix + " binding")
# C872SRC 001758|        if any(fixture["commutation_failures"].values()):
# C872SRC 001759|            failures.append(prefix + " commutation")
# C872SRC 001760|        for key in (
# C872SRC 001761|            "same_layer_support_collisions", "same_color_footprint_collisions",
# C872SRC 001762|            "fine_24_color_collision_count", "seam_stage_contiguity_failure",
# C872SRC 001763|            "stage_order_failure", "seam_phase_failure",
# C872SRC 001764|        ):
# C872SRC 001765|            if fixture[key]:
# C872SRC 001766|                failures.append(prefix + " " + key)
# C872SRC 001767|        dirty = fixture["dirty_spectator"]
# C872SRC 001768|        if any(dirty.get(key, 0) for key in (
# C872SRC 001769|            "operand_failures", "path_return_failures", "endpoint_alias_failures",
# C872SRC 001770|            "same_color_failures", "label_return_failures", "dirty_basis_failures",
# C872SRC 001771|        )):
# C872SRC 001772|            failures.append(prefix + " dirty spectator")
# C872SRC 001773|        if fixture["coarse_six_color_collision_control"] <= 0:
# C872SRC 001774|            failures.append(prefix + " inactive six-color control")
# C872SRC 001775|        if fixture["first_forward_swap_deletion_detections"] <= 0:
# C872SRC 001776|            failures.append(prefix + " inactive first-forward-SWAP deletion")
# C872SRC 001777|        reconciliation = fixture["retained_seam_route_reconciliation"]
# C872SRC 001778|        if any(reconciliation.get(key, 0) for key in (
# C872SRC 001779|            "endpoint_failures", "replacement_operand_failures", "landed_operand_failures",
# C872SRC 001780|            "replacement_return_failures", "landed_return_failures",
# C872SRC 001781|        )):
# C872SRC 001782|            failures.append(prefix + " route reconciliation")
# C872SRC 001783|    for fixture in report["held_schedule_fixtures"]:
# C872SRC 001784|        prefix = f"held-L{fixture['length']}"
# C872SRC 001785|        if fixture["packet_bank_pair_overlap_pairs"] or fixture[
# C872SRC 001786|            "resource_bank_pair_overlap_pairs"
# C872SRC 001787|        ]:
# C872SRC 001788|            failures.append(prefix + " resource overlap")
# C872SRC 001789|        if any(fixture["spatial_output_geometry_failures"].values()):
# C872SRC 001790|            failures.append(prefix + " spatial output geometry")
# C872SRC 001791|        if fixture["same_color_footprint_support_collisions"]:
# C872SRC 001792|            failures.append(prefix + " support collision")
# C872SRC 001793|        if fixture["coarse_six_color_collision_control"] <= 0:
# C872SRC 001794|            failures.append(prefix + " inactive six-color control")
# C872SRC 001795|    direction = report["spatial_direction"]
# C872SRC 001796|    if any(direction["failure_census"].values()):
# C872SRC 001797|        failures.append("spatial direction")
# C872SRC 001798|    for key in (
# C872SRC 001799|        "wrong_side_detected", "seam_deletion_detected",
# C872SRC 001800|        "dirty_spatial_input_detected", "ORIENT_overload_detected",
# C872SRC 001801|    ):
# C872SRC 001802|        if direction.get(key, 0) <= 0:
# C872SRC 001803|            failures.append("inactive " + key)
# C872SRC 001804|    if len(direction["spatial_causal_pairs"]) != 4:
# C872SRC 001805|        failures.append("spatial/causal independence")
# C872SRC 001806|    if not direction["packet_reuse_without_reset_detected"]:
# C872SRC 001807|        failures.append("inactive packet reuse")
# C872SRC 001808|    continuity = report["continuity"]
# C872SRC 001809|    if any(continuity["failure_census"].values()) or any((
# C872SRC 001810|        continuity["stationary_equivalence_failures"], continuity["frame_failures"],
# C872SRC 001811|        continuity["product_failures"],
# C872SRC 001812|    )):
# C872SRC 001813|        failures.append("continuity")
# C872SRC 001814|    covariance = report["color_covariance"]
# C872SRC 001815|    if covariance["bijection_failures"] or covariance["product_failures"]:
# C872SRC 001816|        failures.append("color covariance")
# C872SRC 001817|    passive = report["used_epoch_passive_covariance"]
# C872SRC 001818|    if passive.get("frame_path_failures", 0) or passive.get(
# C872SRC 001819|        "signature_product_failures", 0
# C872SRC 001820|    ) or passive.get("path_product_failures", 0):
# C872SRC 001821|        failures.append("used-epoch passive covariance")
# C872SRC 001822|    allocator = report["four_rail_allocator_candidate"]
# C872SRC 001823|    for key in (
# C872SRC 001824|        "site_set_failures", "orbit_membership_failures", "orbit_bijection_failures",
# C872SRC 001825|        "axis_product_failures", "matrix_product_failures", "site_product_failures",
# C872SRC 001826|        "orbit_product_failures",
# C872SRC 001827|    ):
# C872SRC 001828|        if allocator.get(key, 0):
# C872SRC 001829|            failures.append("allocator " + key)
# C872SRC 001830|    if any(
# C872SRC 001831|        row[key]
# C872SRC 001832|        for row in allocator["geometry"]
# C872SRC 001833|        for key in ("inventory_failures", "native_aux_collisions", "cross_seam_overlap_pairs")
# C872SRC 001834|    ):
# C872SRC 001835|        failures.append("allocator geometry")
# C872SRC 001836|    if allocator["half_action_deletion_detections"] <= 0:
# C872SRC 001837|        failures.append("inactive allocator half-action")
# C872SRC 001838|    if allocator["register_permutation_deletion_detections"] <= 0:
# C872SRC 001839|        failures.append("inactive allocator permutation")
# C872SRC 001840|    if not report["noncommuting_stage_reorder_control"]["detected"]:
# C872SRC 001841|        failures.append("inactive stage reorder")
# C872SRC 001842|    if report["association_firewall"]["acceptance_failures"]:
# C872SRC 001843|        failures.append("orientation acceptance")
# C872SRC 001844|    mass = report["mass_contact"]
# C872SRC 001845|    if not mass["mass_fixture_pass"] or not mass["contact_fixture_pass"]:
# C872SRC 001846|        failures.append("mass/contact")
# C872SRC 001847|    return failures
# C872SRC 001848|
# C872SRC 001849|
# C872SRC 001850|def build_report(stream_output: Path | None = None):
# C872SRC 001851|    inherited = C871.inherited_matter_certificate()
# C872SRC 001852|    physical_stream = build_physical_epoch_stream(2)
# C872SRC 001853|    if stream_output is not None:
# C872SRC 001854|        stream_output.parent.mkdir(parents=True, exist_ok=True)
# C872SRC 001855|        stream_output.write_bytes(canonical_json_bytes(
# C872SRC 001856|            physical_stream_payload(physical_stream)
# C872SRC 001857|        ))
# C872SRC 001858|    report = {
# C872SRC 001859|        "schema": "cycle872-all-seam-spatial-packet-epoch-v1",
# C872SRC 001860|        "status": "pending",
# C872SRC 001861|        "claim_scope": (
# C872SRC 001862|            "one complete all-seam spatial-direction packet epoch on supplied clean "
# C872SRC 001863|            "own-bank inputs"
# C872SRC 001864|        ),
# C872SRC 001865|        "provenance": provenance_certificate(),
# C872SRC 001866|        "supplied_structures": (
# C872SRC 001867|            "pinned Cycle870 graph/carriers/factor stream/coin/contact/non-seam route/phase representative",
# C872SRC 001868|            "declared coframe-returned replacement route for augmented seam-stage instructions",
# C872SRC 001869|            "one clean 59-wire own packet bank plus one blank retained spatial-current M2 per seam",
# C872SRC 001870|            "blank packet payload and work; head; rotor; fixed address",
# C872SRC 001871|            "binder; actuality; admissibility; law-domain; fresh controls",
# C872SRC 001872|            "causal orientation supplied and retained in Cycle714 ORIENT; PORIENT obeys the full seven-factor enabled projection equation",
# C872SRC 001873|            "separate candidate D4-closed four-rail orbit subset and register/rail representation",
# C872SRC 001874|            "one declared update-epoch boundary",
# C872SRC 001875|        ),
# C872SRC 001876|        "physical_epoch_stream": physical_stream_certificate(physical_stream),
# C872SRC 001877|        "physical_macro_mutations": physical_macro_mutation_certificate(),
# C872SRC 001878|        "epoch_fixtures": [epoch_fixture(length) for length in (2, 3)],
# C872SRC 001879|        "held_schedule_fixtures": [held_schedule_fixture(length) for length in (4, 5)],
# C872SRC 001880|        "spatial_direction": semantic_direction_certificate(),
# C872SRC 001881|        "continuity": continuity_certificate(),
# C872SRC 001882|        "color_covariance": color_covariance_certificate(),
# C872SRC 001883|        "used_epoch_passive_covariance": used_epoch_passive_covariance(),
# C872SRC 001884|        "four_rail_allocator_candidate": four_rail_allocator_certificate(),
# C872SRC 001885|        "noncommuting_stage_reorder_control": noncommuting_stage_reorder_control(),
# C872SRC 001886|        "association_firewall": association_firewall(),
# C872SRC 001887|        "mass_contact": {
# C872SRC 001888|            "scope": (
# C872SRC 001889|                "inherited unchanged Cycle870/Cycle871 factor fixtures and phase ledger; "
# C872SRC 001890|                "not a new integrated-epoch spectrum"
# C872SRC 001891|            ),
# C872SRC 001892|            "mass_fixture_pass": inherited["mass_fixture_pass"],
# C872SRC 001893|            "contact_fixture_pass": inherited["contact_fixture_pass"],
# C872SRC 001894|            "QR_off_diagonal_residual": inherited["QR"]["QR_off_diagonal_residual"],
# C872SRC 001895|            "QR_reconstruction_residual": inherited["QR"]["reconstruction_residual"],
# C872SRC 001896|            "coin_unitarity_residual": inherited["one_particle"]["coin_unitarity_residual"],
# C872SRC 001897|            "mass_difference": abs(
# C872SRC 001898|                inherited["one_particle"]["analytic_mass"]
# C872SRC 001899|                - inherited["one_particle"]["rest_mass"]
# C872SRC 001900|            ),
# C872SRC 001901|            "contact_residual": inherited["contact"]["maximum_residual_up_to_global_phase"],
# C872SRC 001902|        },
# C872SRC 001903|        "open_boundaries": (
# C872SRC 001904|            "causal orientation remains supplied and is not derived from spatial direction",
# C872SRC 001905|            "later-epoch fresh address/reset/renewal/genesis remains supplied or open",
# C872SRC 001906|            "four-rail allocator is a separate geometric candidate; no transported packet word claimed",
# C872SRC 001907|            "every coupling and physical scale for the unit-weight current remains supplied",
# C872SRC 001908|        ),
# C872SRC 001909|        "interpretation_firewall": (
# C872SRC 001910|            "not autonomous recurrence; colors/factors/padding/routes/addresses are not time, "
# C872SRC 001911|            "ticks, occurrences, Events, Records, Born histories, sources, or gravity; "
# C872SRC 001912|            "unit occupation current is not energy, mass, calibrated source density, or gravity"
# C872SRC 001913|        ),
# C872SRC 001914|    }
# C872SRC 001915|    report["failures"] = failure_list(report)
# C872SRC 001916|    report["status"] = "pass" if not report["failures"] else "fail"
# C872SRC 001917|    return report
# C872SRC 001918|
# C872SRC 001919|
# C872SRC 001920|def main():
# C872SRC 001921|    parser = argparse.ArgumentParser()
# C872SRC 001922|    parser.add_argument("--output", type=Path, default=DEFAULT_RECEIPT)
# C872SRC 001923|    parser.add_argument(
# C872SRC 001924|        "--stream-output", type=Path,
# C872SRC 001925|        help="optional full deterministic L2 executable local-gate stream JSON",
# C872SRC 001926|    )
# C872SRC 001927|    args = parser.parse_args()
# C872SRC 001928|    report = build_report(args.stream_output)
# C872SRC 001929|    args.output.parent.mkdir(parents=True, exist_ok=True)
# C872SRC 001930|    args.output.write_text(
# C872SRC 001931|        json.dumps(report, indent=2, sort_keys=True, default=float) + "\n",
# C872SRC 001932|        encoding="utf-8",
# C872SRC 001933|    )
# C872SRC 001934|    print("CYCLE872_ALL_SEAM_SPATIAL_PACKET_EPOCH_PASS" if report["status"] == "pass"
# C872SRC 001935|          else "CYCLE872_ALL_SEAM_SPATIAL_PACKET_EPOCH_FAIL")
# C872SRC 001936|    return 0 if report["status"] == "pass" else 1
# C872SRC 001937|
# C872SRC 001938|
# C872SRC 001939|if __name__ == "__main__":
# C872SRC 001940|    raise SystemExit(main())
