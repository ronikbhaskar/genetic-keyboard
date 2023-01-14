
from random import shuffle, uniform, choice
from keyboard import DEFAULT_DNA, DNA_LEN, Keyboard
from fitness import scrape_wikipedia_frequency_list, FitnessFn
from math import exp
MUTATION_RATE = 1 / DNA_LEN

def init(wiki_freq_url, dataset_length, pop_len):
    words_n_freqs = scrape_wikipedia_frequency_list(wiki_freq_url, dataset_length)
    fitness = FitnessFn(words_n_freqs)
    pop = []
    for _ in range(pop_len):
        dna = DEFAULT_DNA.copy()
        shuffle(dna)
        pop.append(Keyboard(dna))

    return pop, fitness

def new_member(pop, distribution):
    p1_index = uniform(0, 1)
    p2_index = uniform(0, 1)
    p1 = None
    p2 = None

    for member, inv_fit in zip(pop, distribution):
        if p1_index <= inv_fit:
            p1 = member
        else:
            p1_index -= inv_fit

        if p2_index <= inv_fit:
            p2 = member
        else:
            p2_index -= inv_fit

        if p1 is None or p2 is None:
            continue

    dna = [-1] * DNA_LEN

    # random crossover
    for i in range(DNA_LEN):
        random_num = uniform(0, 1)
        if random_num <= 0.5:
            for letter, pos in enumerate(p1.dna):
                if pos == i:
                    dna[letter] = pos
                    break
        else:
            for letter, pos in enumerate(p2.dna):
                if pos == i:
                    dna[letter] = pos
                    break

    # mutation
    while uniform(0, 1) <= MUTATION_RATE: # to allow for 0 or more mutations
        rand_pos_1 = choice(range(DNA_LEN))
        rand_pos_2 = choice(range(DNA_LEN))
        dna[rand_pos_1], dna[rand_pos_2] = dna[rand_pos_2], dna[rand_pos_1] # swap positions of two keys

    if -1 in dna: # something messed up
        return p1

    return Keyboard(dna)

def next_generation(pop, pop_len, fitness):
    fits = [fitness(keyboard) for keyboard in pop]
    min_dist = min(fits) # the numbers are too big and too close together, so selection is essentially random
    # inv fitness to reward lower fitness (lower total distance)
    inv_fits = [1 / (fit - min_dist + 1) for fit in fits]
    sum_inv_fits = sum(inv_fits)

    distribution = [inv_fit / sum_inv_fits for inv_fit in inv_fits]
    assert 0.9999999 < sum(distribution) < 1.0000001, \
        f"distribution sum = {sum(distribution)}"

    new_pop = [new_member(pop, distribution) for _ in range(pop_len)]
    return new_pop

def fittest(pop, fitness):
    lowest_score = fitness(pop[0])
    best_member = pop[0]
    for member in pop[1:]:
        score = fitness(member) 
        if score < lowest_score:
            lowest_score = score
            best_member = member

    return best_member, lowest_score

def sim(wiki_freq_url, dataset_length, pop_len, num_generations):
    pop, fitness = init(wiki_freq_url, dataset_length, pop_len)
    fits = [fitness(keyboard) for keyboard in pop]
    best_member, lowest_score = fittest(pop, fitness)
    print("Generation 0:")
    print(f"Average Score Distance Score of Generation: {sum([fitness(keyboard) for keyboard in pop]) / pop_len}")
    print(f"Best Keyboard Distance Score of Generation: {lowest_score}")
    best_member.draw()
    print()

    for i in range(num_generations):
        pop = next_generation(pop, pop_len, fitness)
        best_member, lowest_score = fittest(pop, fitness)
        print(f"Generation {i+1}:")
        print(f"Average Score Distance Score of Generation: {sum([fitness(keyboard) for keyboard in pop]) / pop_len}")
        print(f"Best Keyboard Distance Score of Generation: {lowest_score}")
        best_member.draw()
        print()

def main():
    url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/TV/2006/1-1000"
    dataset_len = 1000
    pop_len = 500
    num_generations = 100
    sim(url, dataset_len, pop_len, num_generations)

if __name__ == "__main__":
    main()

