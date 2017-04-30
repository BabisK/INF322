from snap import *
import unittest
import snap


def has_euler_path(graph):
    vertices = set()

    # If graph is not connected then it has no Euler path
    if not snap.IsConnected(graph):
        return False, vertices

    for node in graph.Nodes():
        if node.GetDeg() % 2 == 1:
            vertices.add(node.GetId())

    if len(vertices) == 2:
        return True, vertices
    else:
        return False, set()


def has_euler_circuit(graph):
    # If graph is not connected then it has no Euler circuit
    if not snap.IsConnected(graph):
        return False

    for node in graph.Nodes():
        if node.GetDeg() % 2 == 1:
            return False

    return True


class TestEulerMethods(unittest.TestCase):

    def test_has_euler_path_but_not_circuit(self):
        graph = snap.TUNGraph.New()
        graph.AddNode(-1)
        graph.AddNode(-1)
        graph.AddNode(-1)
        graph.AddNode(-1)
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 0)
        graph.AddEdge(1, 3)
        result, vertices = has_euler_path(graph)
        self.assertTrue(result)
        self.assertEqual(len(vertices), 2)

    def test_does_not_have_euler_path(self):
        graph = snap.TUNGraph.New()
        graph.AddNode(-1)
        graph.AddNode(-1)
        graph.AddNode(-1)
        graph.AddNode(-1)
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 0)
        result, vertices = has_euler_path(graph)
        self.assertFalse(result)
        self.assertEqual(len(vertices), 0)

    def test_has_euler_circuit(self):
        graph = snap.TUNGraph.New()
        graph.AddNode(0)
        for i in range(1, 1000):
            graph.AddNode(i)
            graph.AddEdge(i-1, i)
        graph.AddEdge(999, 0)
        result = has_euler_circuit(graph)
        self.assertTrue(result)
        self.assertTrue(graph.GetNodes()>=1000)

    def test_does_not_have_euler_circuit(self):
        graph = snap.TUNGraph.New()
        graph.AddNode(0)
        for i in range(1, 1000):
            graph.AddNode(i)
            graph.AddEdge(i-1, i)
        graph.AddEdge(999, 0)
        graph.AddEdge(999, 1)
        result = has_euler_circuit(graph)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
