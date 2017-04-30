# Social Network Analysis
## Homework 1

If SNAP is not installed in your system, use the ‘install_snap.sh’ bash script to download it and install it locally in the working directory.

### Part 1
To execute part 1, simply call ‘python hw1_1.py’. This will execute the unit tests.

### Part 2
To execute part 2, call ‘python hw1_2.py <out-degree>’. Where ‘out-degree’ enter a valid out-degree value for the Barabasi-Albert model.

This script will create incresingly larger networks and execute the Girvan-Newman and Clauset-Newman-Moore community detection algorithms until they both take more than 10 minutes to complete (or the system runs out of memory). Also, for each graph it will find and print the node with maximum degree and PageRank.
In my system the final results are:

* Girvan-Newman community detection algorithm max runtime 717.491745949s for 700 nodes
* Clauset-Newman-Moore community detection algorithm max runtime 455.893180132s for 60000 nodes

For more nodes, my 16GB RAM system run out of memory