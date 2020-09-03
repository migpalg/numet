from typing import Tuple

import sympy as sym
from sympy.abc import x


def bisection_method(f: callable, left_value: float,
                     right_value: float,
                     n_iterations: int = 20) -> Tuple[float, float, float]:
    """
    Calculates root of function with bisection method
    :param f: Function
    :param left_value: Minimum value
    :param right_value: Maximum value
    :param n_iterations: Max number of iterations
    :return: Returns a tuple with the approximated value and a error percentage
    """
    mid_point, f_value, total_i = 0.0, 0.0, 0

    for _ in range(n_iterations):
        mid_point = (left_value + right_value) / 2
        f_value = f(mid_point)

        if f_value == 0:
            break
        elif f_value < 0:
            left_value = mid_point
        else:
            right_value = mid_point

        total_i = total_i + 1

    return mid_point, abs(f_value), total_i


def fixed_point_iteration(g: callable, left_value: float,
                          right_value: float, tolerance=1e-7,
                          max_iterations: int = 30) -> Tuple[float, float, float]:
    error_p = 1
    iterations = 0
    last_value = g((left_value + right_value) / 2)
    g_value = 0

    while error_p > tolerance and iterations < max_iterations:
        g_value = g(last_value)
        error_p = last_value / g_value
        iterations = iterations + 1

        if last_value == g_value:
            break

        last_value = g_value

    return last_value, iterations, abs(error_p)


def newton_raphson(func_str: str, initial_point: float, max_iterations: int = 20, tolerance: float = 1e-6):
    exp = sym.parse_expr(func_str)
    diff_exp = sym.diff(exp)
    exp_lamb = sym.lambdify(x, exp)
    diff_exp_lamb = sym.lambdify(x, diff_exp)
    p = initial_point
    last_p = p

    iterations = 0

    for _ in range(max_iterations):
        p = last_p - exp_lamb(last_p) / diff_exp_lamb(last_p)

        if abs(p - last_p) < tolerance:
            break

        last_p = p
        iterations = iterations + 1

    return p, iterations, exp, diff_exp
