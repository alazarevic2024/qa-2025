class ShopUtils:
    EUR_TO_RSD = 117.0
    TAX_RATE = 0.20

    @staticmethod
    def rsd_to_eur(rsd):
        if rsd > 0:
            return round(rsd / ShopUtils.EUR_TO_RSD, 2)
    
    @staticmethod
    def eur_to_rsd(eur):
        if eur > 0:
            return round(eur * ShopUtils.EUR_TO_RSD, 2)
    
    def price_with_tax(price):
        if price > 0:
            return round(price * (1 + ShopUtils.TAX_RATE), 2) 