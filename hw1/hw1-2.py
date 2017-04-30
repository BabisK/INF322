import snap
import argparse
import time

parser = argparse.ArgumentParser()
#parser.add_argument('nodes', help='The number of nodes to generate in the graph using the Barabasi-Albert model')
parser.add_argument('degree', help='The out degree of each node in the graph')
args = parser.parse_args()

# This method performs deep copy of a graph
def copy_graph(graph):
    tmpfile = '.copy.bin'

    # Saving to tmp file
    FOut = snap.TFOut(tmpfile)
    graph.Save(FOut)
    FOut.Flush()

    # Loading to new graph
    FIn = snap.TFIn(tmpfile)
    graphtype = type(graph)
    new_graph = graphtype.New()
    new_graph = new_graph.Load(FIn)

    return new_graph

gntime = None
gnnodes = None
cnmtime = None
cnmnodes = None

# Iterate over the nodes count
#for node_count in [50]+range(100,1000,100)+range(10000, 60000, 10000):
for node_count in [60000]:
    if cnmtime < 600 or gntime < 600:
        print '===========' + str(node_count) + ' nodes==========='

        # Generate a graph with the Barabasi-Albert model
        graph = snap.GenPrefAttach(node_count, int(args.degree))
        print 'Number of nodes in the graph: ' + str(node_count)
        print 'Number of edges in the graph: ' + str(graph.GetEdges())
        print 'Out degree of Barabasi-Albert model graph: ' + args.degree

        # Create a copy of that graph
        # Using the community detection algorithms seem to destroy the graph
        # Thus I save it to use it on both algorithms
        graph_copy = copy_graph(graph)

        # Find the node with the highest degree
        highest_degree = None
        node_with_highest_degree = None
        for node in graph.Nodes():
            #print node.GetDeg()
            if node.GetDeg() > highest_degree:
                highest_degree = node.GetDeg()
                node_with_highest_degree = node.GetId()
        print 'Node with highest degree: ' + str(node_with_highest_degree) + ', Degree: ' + str(highest_degree)

        # Find the node with the highest page rank
        page_rank_hashmap = snap.TIntFltH()
        snap.GetPageRank(graph, page_rank_hashmap)
        highest_page_rank = None
        node_with_highest_page_rank = None
        for node in page_rank_hashmap:
            if page_rank_hashmap[node] > highest_page_rank:
                highest_page_rank = page_rank_hashmap[node]
                node_with_highest_page_rank = node
        print 'Node with highest PageRank: ' + str(node_with_highest_page_rank) + ', PageRank: ' + str(highest_page_rank)
    else:
        break

    # Calculate the communities with the Garvin-Newman algorithm
    if gntime > 600:
        print 'Executing Garvin-Newman algorithm'
        communities = snap.TCnComV()
        start = time.time()
        modularity = snap.CommunityGirvanNewman(graph, communities)
        end = time.time()
        gntime = end-start
        gnnodes = node_count
        print 'The modularity of the network is: ' + str(modularity)
        print 'Girvan-Newman community detection algorithm runtime: ' + str(gntime)

    # Calculate the communities with the Clauset-Newman-Moore algorithm
    if cnmtime < 600:
        print 'Executing Clauset-Newman-Moore algorithm'
        communities = snap.TCnComV()
        start = time.time()
        modularity = snap.CommunityCNM(graph_copy, communities)
        end = time.time()
        cnmtime = end-start
        cnmnodes = node_count
        print 'The modularity of the network is: ' + str(modularity)
        print 'Clauset-Newman-Moore community detection algorithm runtime: ' + str(end - start)

# Print final results
print 'Girvan-Newman community detection algorithm max runtime ' + str(gntime) + 's for ' + str(gnnodes) + ' nodes'
print 'Clauset-Newman-Moore community detection algorithm max runtime ' + str(cnmtime) + 's for ' + str(cnmnodes) + ' nodes'