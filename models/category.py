class Category:
    VALID_CATEGORIES = {"Hrana", "Računi", "Prevoz", "Zabava", "Ostalo"}

    #Checking is there valid category
    @staticmethod
    def is_valid(category: str) -> bool:
        return category in Category.VALID_CATEGORIES
