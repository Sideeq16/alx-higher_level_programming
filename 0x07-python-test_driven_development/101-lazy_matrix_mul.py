#!/usr/bin/python3
import numpy as np
"""Documentation for lazy_matrix_mul"""

def lazy_matrix_mul(m_a, m_b):
    """Documentation for function lazy_matrix_mul"""
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("Matrix multiplication failed. Ensure the matrices have compatible dimensions.") from e
    except Exception as e:
        raise Exception("An error occurred during matrix multiplication.") from e
