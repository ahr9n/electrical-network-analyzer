from inputs import *
from outputs import *

from equations import *


def main():
    Instructions.display_for_matrix_a()

    nodes, branches = map(int, input().split())
    branch_name, reversed_branch_name = {}, {}

    graph = Graph(nodes, branches)
    graph.read_graph(branch_name, reversed_branch_name)
    tree_branches = graph.find_tree(branch_name, nodes)

    Instructions.display_for_matrix_b(tree_branches, reversed_branch_name)

    values = read_circuit_components()

    matrix_a_tree = get_matrix_a_tree(tree_branches, reversed_branch_name, nodes, branches)
    matrix_a_link = get_matrix_a_link(tree_branches, reversed_branch_name, nodes, branches)

    matrix_a = get_matrix_a(tree_branches, reversed_branch_name, nodes, branches)
    matrix_b = get_matrix_b(matrix_a_tree, matrix_a_link)
    matrix_c = get_matrix_c(matrix_a_tree, matrix_a_link)

    print("\nThe Process:\n")

    Formats.format_matrix(matrix_a, "Incidence")
    Formats.format_matrix(matrix_b, "Tie-set")
    Formats.format_matrix(matrix_c, "Cut-set")

    matrix_voltage_source = get_matrix_voltage_source(values[0])
    matrix_current_source = get_matrix_current_source(values[1])
    matrix_impedance = get_matrix_impedance(values[2])

    matrix_i_loop = get_matrix_i_loop(matrix_b, matrix_impedance, matrix_current_source, matrix_voltage_source)
    matrix_j_branch = get_matrix_j_branch(matrix_i_loop, matrix_b)
    matrix_v_branch = get_matrix_v_branch(matrix_j_branch, matrix_impedance, matrix_current_source,
                                          matrix_voltage_source)

    Formats.format_matrix(matrix_i_loop, "I Loop")
    Formats.format_matrix(matrix_j_branch, "J Branch")
    Formats.format_matrix(matrix_v_branch, "V Branch")

    branches_order = get_branches_order(tree_branches, reversed_branch_name)
    Formats.format_result(matrix_j_branch, matrix_v_branch, branches_order)


if __name__ == "__main__":
    main()
