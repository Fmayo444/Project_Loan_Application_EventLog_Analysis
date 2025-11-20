import pm4py
from pm4py.objects.petri_net.obj import PetriNet



def calculate_avg_arc_degree(net: PetriNet):
    nodes = list(net.places) + list(net.transitions)
    totalDegree = 0

    for node in nodes:
        degree = len(node.in_arcs) + len(node.out_arcs)
        totalDegree += degree

    avgDegree = totalDegree / len(nodes) if len(nodes) > 0 else 0


    penalty = max(avgDegree - 2, 0)
    simplicity_degree = 1.0 / (1.0 + penalty)

    return "Average arc degree: " + str(simplicity_degree)

def calculate_control_flow_complexity(net: PetriNet):

    cfc_score = 0

    for place in net.places:
        out_degree = len(place.out_arcs)
        if out_degree > 1:
            cfc_score += out_degree

    for trans in net.transitions:
        out_degree = len(trans.out_arcs)
        if out_degree > 1:
            cfc_score += 1

    return "Control Flow Complexity: "  + str(cfc_score)

def calculate_henry_kafura_complexity(net: PetriNet):

    hk_score = 0
    nodes = list(net.places) + list(net.transitions)

    for node in nodes:
        fan_in = len(node.in_arcs)
        fan_out = len(node.out_arcs)

        complexity = (fan_in * fan_out) ** 2

        hk_score += complexity

    return "Henry Kafura Complexity: " + str(hk_score)