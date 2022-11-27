color_a=input()
color_b=input()
color_true=['красный','синий','желтый']
if (color_a in color_true) & (color_b in color_true):
    if ((color_a=='красный') & (color_b=='синий')) OR ((color_a== 'синий') & (color_b=='красный')):
        print('фиолетовый')
    if ((color_a == 'красный') & (color_b == 'желтый')) OR ((color_a == 'желтый') & (color_b == 'красный')):
        print('оранжевый')
    if ((color_a == 'желтый') & (color_b == 'синий')) OR ((color_a == 'синий') & (color_b == 'желтый')):
        print('зеленый')
else:
    print('ошибка цвета')