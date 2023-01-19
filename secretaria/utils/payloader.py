from datetime import date

class Payloader:
    __res = {
        'empresa': 'Centro Educacional Art Ensino',
        'hoje': date.today(),
        'dia': date.today().day,
        'mes': date.today().month,
        'ano': date.today().year
    }

    def res(self):
        return self.__res
