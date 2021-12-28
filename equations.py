import numpy as np


def get_branches_order(tree_branches, reversed_branch_name):
    branches_order = tree_branches.copy()
    tree_branches.sort()
    for key, value in reversed_branch_name.items():
        if key not in tree_branches:
            branches_order.append(key)
    return branches_order


def get_matrix_a(tree_branches, reversed_branch_name, nodes, branches):
    branches_order = get_branches_order(tree_branches, reversed_branch_name)
    matrix_a = [[0 for _ in range(branches)] for __ in range(nodes)]
    for branch in range(branches):
        (key, value) = reversed_branch_name[branches_order[branch]]
        matrix_a[key][branch], matrix_a[value][branch] = 1, -1
    return matrix_a


def get_matrix_a_tree(tree_branches, reversed_branch_name, nodes, branches):
    matrix_a = get_matrix_a(tree_branches, reversed_branch_name, nodes, branches)
    matrix_a_tree = []
    for i in range(nodes - 1):
        matrix_a_tree.append([])
        for j in range(len(tree_branches)):
            matrix_a_tree[i].append(matrix_a[i][j])
    return matrix_a_tree


def get_matrix_a_link(tree_branches, reversed_branch_name, nodes, branches):
    matrix_a = get_matrix_a(tree_branches, reversed_branch_name, nodes, branches)
    matrix_a_link = []
    for i in range(nodes - 1):
        matrix_a_link.append([])
        for j in range(len(tree_branches), branches):
            matrix_a_link[i].append(matrix_a[i][j])
    return matrix_a_link


def get_matrix_c_link(matrix_a_tree, matrix_a_link):
    matrix_a_tree = np.array(matrix_a_tree)
    matrix_a_tree_inverse = np.linalg.inv(matrix_a_tree)
    # aTreeInverse = aTree ^ -1
    matrix_c_link = np.dot(matrix_a_tree_inverse, matrix_a_link)
    return matrix_c_link


def get_matrix_b_tree(matrix_a_tree, matrix_a_link):
    matrix_c_link = get_matrix_c_link(matrix_a_tree, matrix_a_link)
    matrix_b_tree = np.multiply(np.transpose(matrix_c_link), -1)
    matrix_b_tree[matrix_b_tree == -0] = 0  # avoiding '-0'
    return matrix_b_tree


def get_matrix_c(matrix_a_tree, matrix_a_link):
    matrix_c_link = get_matrix_c_link(matrix_a_tree, matrix_a_link)
    matrix_c_tree = np.identity(len(matrix_c_link))
    matrix_c = np.concatenate((matrix_c_tree, matrix_c_link), axis=1)
    return matrix_c


def get_matrix_b(matrix_a_tree, matrix_a_link):
    matrix_b_tree = get_matrix_b_tree(matrix_a_tree, matrix_a_link)
    matrix_b_link = np.identity(len(matrix_b_tree))
    matrix_b = np.concatenate((matrix_b_tree, matrix_b_link), axis=1)
    return matrix_b


def get_matrix_impedance(resistors):
    matrix_impedance = []
    for i in range(len(resistors)):
        helper = [0 for i in range(len(resistors))]
        helper[i] = resistors[i]
        matrix_impedance.append(helper)
    return matrix_impedance


def get_matrix_current_source(current_sources):
    matrix_current_source = [[current_sources[i]] for i in range(len(current_sources))]
    return matrix_current_source


def get_matrix_voltage_source(voltage_sources):
    matrix_voltage_source = [[voltage_sources[i]] for i in range(len(voltage_sources))]
    return matrix_voltage_source


def get_matrix_i_loop(matrix_b, matrix_impedance, matrix_current_source, matrix_voltage_source):
    right_side = np.subtract(np.dot(matrix_b, matrix_voltage_source),
                             np.dot(matrix_b, np.dot(matrix_impedance,
                                                     matrix_current_source)))
    left_side = np.dot(matrix_b, np.dot(matrix_impedance, np.transpose(matrix_b)))
    left_side_inverse = np.linalg.inv(left_side)
    matrix_i_loop = np.dot(left_side_inverse, right_side)
    return matrix_i_loop


def get_matrix_j_branch(matrix_b, matrix_i_loop):
    matrix_j_branch = np.dot(np.transpose(matrix_b), matrix_i_loop)
    return matrix_j_branch


def get_matrix_v_branch(matrix_j_branch, matrix_impedance, matrix_current_source, matrix_voltage_source):
    helper = np.subtract(np.dot(matrix_impedance, np.add(matrix_j_branch, matrix_current_source)),
                         matrix_voltage_source)
    matrix_v_branch = [[helper[i][i] for i in range(len(helper))]]
    return matrix_v_branch
