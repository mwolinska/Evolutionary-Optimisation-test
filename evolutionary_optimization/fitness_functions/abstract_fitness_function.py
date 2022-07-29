from abc import ABC, abstractmethod
from ctypes import Union

from evolutionary_optimization.phenotype.abstract_phenotype import AbstractPhenotype


class AbstractFitnessFunction(ABC):
    @abstractmethod
    def evaluate(self, phenotype: AbstractPhenotype) -> Union(float, int):
        """This method will return the fitness score from a phenotype.

        Args:
            phenotype: instance of AbstractPhenotype being evaluated.

        Returns:
            Processed phenotype value depending on desired fitness function.
        """
        pass
