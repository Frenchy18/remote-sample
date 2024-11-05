"""Defines patients and computes their risk
Returns:
    float: patient risk factor
"""

class Patient:
    """Represents patient in hospital"""
    
    def __init__(self, name, age, height, weight):
        """Constructor for patient class

        Args:
            name (String): Patient first and last name
            age (int): Patient age in years
            height (int): Patient height in in.
            weight (int): Patient weight in lbs.
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def compute_risk(self):
        """computes patient risk factor as
            sqrt(age) - (height / weight)

        Returns:
            Float: Patient risk factor
        """
        return self.age**0.5 - (self.height / self.weight)
    
    
if __name__ == "__main__":
    bob = Patient("BOB", 25, 72, 260)
    claire = Patient("Claire", 22, 60, 140)
    dave = Patient("Dave Harold", 56, 71, 265)
    
    print(bob.compute_risk())
    print(claire.compute_risk())
    print(dave.compute_risk())

