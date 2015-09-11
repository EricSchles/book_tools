#Code comes from here: http://acodersmusings.blogspot.com/2009/07/curve-fitting-with-pyevolve.html

from pyevolve import G1DList, GSimpleGA, Selectors, Scaling, DBAdapters
from random import seed, randint, random

def eval_polynomial(x, *coefficients):
    result = 0
    for exponent, coeff in enumerate(coefficients):
        result += coeff*x**exponent
    return result 

def generate_fitness_function(sample_points):
    def fitness_function(chromosome):
        score = 0
        for ind,point in enumerate(sample_points):
            delta = abs(eval_polynomial(point[0], *chromosome) - point[1])
            score += delta
        score = -score
        return score
    return fitness_function

if __name__ == "__main__":
    # Generate a random polynomial, and generate sample points from it
    seed()

    #randomly initialize source polynomial
    source_polynomial = []
    for i in xrange(randint(1, 5)):
        source_polynomial.append(randint(-20,20))
    
    xdata = [5,6,7,3,4,8,9,12,17,4,14,9,25,12,24,15]
    ydata = [12,11,11,30,27,9,8,8,14,30,10,8,10,10,10,10]
    sample_points = zip(xdata,ydata)
    
    # Create the population
    genome = G1DList.G1DList(5)
    genome.evaluator.set(generate_fitness_function(sample_points))
    genome.setParams(rangemin=-50, rangemax=50)

    # Set up the engine
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setPopulationSize(1000)
    ga.selector.set(Selectors.GRouletteWheel)

    # Change the scaling method
    pop = ga.getPopulation()
    pop.scaleMethod.set(Scaling.SigmaTruncScaling)

    # Start the algorithm, and print the results.
    ga.evolve(freq_stats=10)
    print(ga.bestIndividual())
    print("Source polynomial: " + repr(source_polynomial))
    print("Sample points: " + repr(sample_points))
