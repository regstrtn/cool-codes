from multiprocessing import Pool


def runformanynetworks(networklist):
    output = []
    for network in networklist:
        str2 = "./nets/"+str(network)
        dtmod, dtcom = getSeries(str2)
        gtmod,gtcom = computegtmod(str2)
        output.append((gtmod, dtmod))
        modfile = open(modfilename, 'a')
        modfile.write(str2+ ":    "+ str(gtmod)+"  "+str(dtmod)+"\n")
        modfile.close()
        #detected_commu = _get_com_wise_nodes(partition_at_level(dtcom, len(dtcom)-1))
        #write_commus_infile(network,detected_commu,gtcom)
    return output


def parallelimplementation(networklist):
    #Open file to compare modularity values
    modfile = open(modfilename,'w')
    modfile.write("network                                   GroundTruth    Detected-Louvain\n")
    modfile.close()

    #Prepare args for parallel processings
    numnetworks = len(networklist)

    cores=4
    chunksize = numnetworks/cores

    splits = []
    for i in range(cores):
        splits.append((i)*chunksize)
    splits.append(numnetworks)

    args = []
    for i in range(cores):
        args.append(networklist[splits[i]:splits[i+1]])

    p = Pool(cores)
    modularities = p.map(runformanynetworks, args)

    #Flatten list of lists returned by different cores
    modularities = [item for items in modularities for item in items]

    print modularities
    return modularities