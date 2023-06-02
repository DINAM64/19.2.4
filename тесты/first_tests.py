импортировать  pytest
из  приложения . импорт калькулятора  калькулятор 

класс  TestCalc :
     настройка защиты ( самостоятельно ):
        сам . расчет  =  Калькулятор

    def  test_multiply_calculate_correctly ( self ):
        самоутвердиться  . _ расч . умножить ( на себя , 2 , 2 )

    def  test_division_calculate_correctly ( self ):
        самоутвердиться   . _ расч . деление ( самостоятельно , 6 , 2 )

    def  test_subtraction_calculate_correctly ( self ):
        самоутвердиться   . _ расч . вычитание ( я , 5 , 2 )

    def  test_adding_calculate_correctly ( self ):
        самоутвердиться   . _ расч . добавление ( самостоятельно , 4 , 2 )

    def  test_adding_failed ( сам ):
        самоутвердиться  . _ расч . добавление ( я , 2 , 2 ) ==  5
