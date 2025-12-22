class Bankomat:
    def __init__ (self, stanje):
        self.stanje = stanje
    
    def podigni_novac(self, iznos):
        if iznos >= self.stanje:
            self.stanje -= iznos
            return True
        return False
    
    def uplati_novac(self, iznos):
        self.stanje += iznos
    
    def proveri_stanje(self):
        return self.stanje