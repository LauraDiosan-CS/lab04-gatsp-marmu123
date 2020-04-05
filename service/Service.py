from ga.Fitness import fitnessOfPath
from ga.GA import GA
from matplotlib import pyplot as plt


class Service:
    def __init__(self):
        pass
    def generate(self,numberOfGen,popSize,graph,repo):
        gaParams={'popSize':popSize,'noGen':numberOfGen}
        pbParams={'noNodes':len(graph),'graph':graph,'function':fitnessOfPath}
        ga=GA(gaParams,pbParams)

        bestChromosomes = []
        bestFitness = []
        outLines=[]
        for g in range(gaParams['noGen']):
            # logic alg
            # ga.oneGeneration()
            ga.oneGenerationElitism()
            # ga.oneGenerationSteadyState()

            bestChromo = ga.bestChromosome()
            bestChromosomes.append(bestChromo)
            bestFitness.append(bestChromo.fitness)
            outString='Best solution in generation ' + str(g) + ' is:  f(x) = ' + str(1/bestChromo.fitness)
            print(outString)
            outLines+=[outString]


        # x = []
        # y = []
        # for i in range(len(bestFitness)):
        #     x.append(i)
        #     y.append(bestFitness[i])
        # plt.plot(x, y)
        # plt.show()
        repo.writeDataToFile(outLines)