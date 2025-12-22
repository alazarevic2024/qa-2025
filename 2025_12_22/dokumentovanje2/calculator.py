class Calculator:
    """
    Jednostavan kalkulator za osnovne aritmeticke operacije
    """
    def __init__(self, a, b):
        """
        Args:
            a: Prvi broj
            b: Drugi broj
        
        Returns:
            Kreiran kalkulator
        """
        self.a = a
        self.b = b

    def saberi(self):
        return self.a + self.b
    
    def oduzmi(self):
        return self.a - self.b
    
    def pomnozi(self):
        return self.a * self.b
    
    def podeli(self):
        return self.a / self.b