#!/usr/bin/env python3
"""Small canonicalization helpers for the Cycle-883 sandwich probe."""

from hashlib import sha256

import numpy as np

INVERSE_KIND = {
    "route_swap": "route_swap",
    "check_parity_CNOT": "check_parity_CNOT",
    "check_basis_H": "check_basis_H",
    "loader_controlled_Z": "loader_controlled_Z",
    "loader_parity_CNOT": "loader_parity_CNOT",
    "syndrome_controlled_Z": "syndrome_controlled_Z",
    "controller_Toffoli_CNOT": "controller_Toffoli_CNOT",
    "check_sign_X": "check_sign_X",
    "controller_Toffoli_T": "controller_Toffoli_Tdg",
    "check_basis_Sdg": "check_basis_S",
    "check_basis_S": "check_basis_Sdg",
    "controller_Toffoli_Tdg": "controller_Toffoli_T",
    "controller_Toffoli_H": "controller_Toffoli_H",
    "loader_target_Sdg": "loader_target_S",
    "loader_controlled_X_for_Y": "loader_controlled_X_for_Y",
    "loader_target_S": "loader_target_Sdg",
    "controller_CCZ_H": "controller_CCZ_H",
    "controller_router_CNOT_right_left": "controller_router_CNOT_right_left",
    "controller_router_X_right_pre": "controller_router_X_right_pre",
    "controller_router_X_right_post": "controller_router_X_right_post",
    "controller_token_SWAP_down": "controller_token_SWAP_down",
    "controller_token_SWAP_up": "controller_token_SWAP_up",
    "controller_root_fresh_to_token_SWAP": "controller_root_fresh_to_token_SWAP",
    "controller_root_token_to_spent_SWAP": "controller_root_token_to_spent_SWAP",
    "controller_router_X_left": "controller_router_X_left",
    "controller_router_CNOT_left_right": "controller_router_CNOT_left_right",
    "controller_router_X_right": "controller_router_X_right",
}


def canonical_matrix_digest(matrix) -> str:
    matrix = np.asarray(matrix, dtype=complex)
    real = np.round(matrix.real, 14)
    imag = np.round(matrix.imag, 14)
    real[np.abs(real) < 1.0e-14] = 0.0
    imag[np.abs(imag) < 1.0e-14] = 0.0
    return sha256(np.asarray(real + 1j * imag, dtype=complex).tobytes()).hexdigest()


def word_hash(word) -> str:
    output = sha256()
    for row in word:
        output.update(repr((row.sites, canonical_matrix_digest(row.matrix))).encode())
    return output.hexdigest()
