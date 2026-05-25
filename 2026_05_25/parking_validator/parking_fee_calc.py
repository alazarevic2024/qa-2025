class ParkingFeeCalculator:
    prices = {"A":100, "B":70, "C":50} # potrebno je da dolazi sa bekenda
    def calculate_fee(self, zone, hours):
        if zone not in self.prices:
            return -1
        if hours <= 0:
            return 0
        
        cena_u_zoni = self.prices[zone]
        return hours * cena_u_zoni

