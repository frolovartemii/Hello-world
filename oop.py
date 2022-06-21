from unicodedata import name


class Monster:
    def __init__(self, name):
        self.name = name
        if name == "Бурмедь":
            self.weapon = "Когти и большая челюсть."
            self.size = "Громадный."
            self.weaknensess = "Любит сладкое."
        if name == "Василиск":
            self.weapon = "Клюв и гибкое тело."
            self.size = "Крайне длинный"
            self.weaknensess = "Мозг связан с гребнем."
        if name == "Тысячирёв":
            self.weapon = "Лицо, состоящее из тысячи зубов, расположенных по спирали."
            self.size = "Небольшых размеров, похож на волка."
            self.weaknensess = "Слеп."
    def attack(weapon):
        if weapon == "Когти и большая челюсть.":
            print(" Атакует, тараня противника и разрывая его когтями.")
        elif weapon == "Клюв и гибкое тело.":
            print(" Атакует, пытаясь обвить врага и раздробить ему голову клювом.")
        elif weapon == "Лицо, состоящее из тысячи зубов, расположенных по спирали.":
            print(" Атакует, прыгая на жертву со спины и разрывая её своей спиралью.")