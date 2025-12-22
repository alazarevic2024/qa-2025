class Calculator:
    """
    Klasa kalkulator sadrzi metode osnovnih aritmetickih operacija
    """
    def __init__(self, a, b):
        """
        Konstruktor klase Calculator 
        
        :param self: objekat
        :param a: prvi operand
        :param b: drugi operand
        """
        self.a = a
        """
        Prvi operand a
        """
        self.b = b
        """
        Drugi operand b
        """
    
    def saberi(self):
        """
        Metod za sabiranje
        
        :return: 
            Zbir
        :rtype: int
        """
        return self.a + self.b
    
    def oduzmi(self):
        """
        Metod za oduzimanje
        
        :return: 
            Razlika
        :rtype: int
        """
        return self.a - self.b
    
    def pomnozi(self):
        """
        Metod za mnozenje
        
        :return:
            Razlika
        """
        return self.a * self.b
    
    def podeli(self):
        """
        Metod za deljenje
        
        :return:
            Kolicnik
        """
        return self.a / self.b