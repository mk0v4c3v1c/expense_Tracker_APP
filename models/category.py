class Category:
    VALID_CATEGORIES = {"Food", "Bills", "Transportation", "Fun", "Other"}

    #Checking is there valid category
    @staticmethod
    def is_valid(category: str) -> bool:
        return category in Category.VALID_CATEGORIES
