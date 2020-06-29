
import random
for i in range(5, 10):
    # All variable to stcok in the file .vrp
    n_truck = i
    optimal_value = random.randint(600,1300)
    DIMENSION = random.randint(20,100)
    Comment = "COMMENT : (Augerat et al, No of trucks: " + n_truck + ", Optimal value: " + optimal_value + ")"
    dimension = "DIMENSION : " + str(DIMENSION)
    EDGE = "EDGE_WEIGHT_TYPE : EUC_2D "
    capacity = "CAPACITY : 100"
    name = "NAME : B-n" + dimension + "-k" + n_truck 
    node_section = "NODE_COORD_SECTION \r"
    demande = "DEMAND_SECTION \r"

    # For loop for generate random position 
    for d in DIMENSION:
        data = d + " " + random.randint(1,100) + " " + random.randint(1,100) + " \r"
        node_section += data
    for d in DIMENSION:
        data = d + " " + random.randint(1,30) + " \r"
        demande += data
    depot = "DEPOT_SECTION \r 1 \r -1"

    #create file and write the result on it 
    f = open("B-n" + dimension + "-k" + n_truck + ".vrp", "w")
    f.write(name + "\r" + Comment + "\r" + "TYPE : CVRP\r" + dimension + "\r" + EDGE + "\r" + capacity + "\r" + node_section + "\r" + demande + "\r" + depot + "\r" )
    f.close()