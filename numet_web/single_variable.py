import sympy as sym
from flask import Blueprint, request
from sympy.abc import x

import numet as nm

bp = Blueprint('single-variable', __name__, url_prefix='/single-variable')


@bp.route('/bisection-method', methods=['POST'])
def bisection_method():
    func = request.form['function']
    rang = float(request.form['min_value']), float(request.form['max_value'])
    exp = sym.parse_expr(func)

    root, err, i = nm.bisection_method(sym.lambdify(x, exp), *rang)

    return {
        'input_function': sym.latex(exp),
        'range': rang,
        'root': root,
        'err': err,
        'iterations': i
    }


@bp.route('/fixed-point-iteration', methods=['POST'])
def fixed_point_iteration():
    func = request.form['function']
    rang = float(request.form['min_value']), float(request.form['max_value'])
    max_iterations = int(request.form['max_iterations'])
    exp = sym.parse_expr(func)

    root, i, err = nm.fixed_point_iteration(sym.lambdify(x, exp), *rang, max_iterations=max_iterations)

    return {
        'input_function': sym.latex(exp),
        'range': rang,
        'root': root,
        'iterations': i,
        'error_percentage': 1 - err
    }


@bp.route('/newton', methods=['POST'])
def newton():
    func = request.form['function']
    initial_point = float(request.form['initial_point'])
    max_iterations = int(request.form['max_iterations'])

    root, i, exp, diff_exp = nm.newton_raphson(func, initial_point, max_iterations)

    return {
        'root': root,
        'function': sym.latex(exp),
        'derivative': sym.latex(diff_exp),
        'iterations': i
    }
