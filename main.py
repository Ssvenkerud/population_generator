#!/usr/bin/env python3

from src.simple_generator import SimpleGenerator

def main():
    population_size = int(input("enter population size"))
    schema = {"integer": "int", "float": "float", "category": "cat"}
    generator = SimpleGenerator(population_size, schema)
    population = generator.run()
    print(population.head())

if __name__ == "__main__":
    main()
