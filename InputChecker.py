class Checker:

    def is_pure_text(to_check:str) -> bool:
        for i in to_check:
            if not i.isalpha() and i != ' ':
                return False
        return True