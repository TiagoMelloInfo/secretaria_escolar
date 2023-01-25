from datetime import date

class Payloader:
    mes_dict = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março',
        4: 'Abril', 5: 'Maio', 6: 'Junho',
        7: 'Julho', 8: 'Agosto', 9: 'Setembro',
        10: 'Outubro', 11: 'Novembro',12: 'Dezembro'
    }
    __res = {
        'empresa': 'Centro Educacional Art Ensino',
        'hoje': date.today(),
        'dia': date.today().day,
        'mes': mes_dict[date.today().month],
        'ano': date.today().year
    }

    def res(self):
        return self.__res
