


class Unit:

    def move_on_field(self, field, unit_axis_x, unit_axis_y, direction, is_fly, is_sneak, base_speed = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param unit_axis_x: x-координата юнита
        :param unit_axis_y: у- координата юнита
        :param direction: направление перемещения
        :param is_fly: летит ли юнит
        :param is_sneak: крадется ли юнит
        :param base_speed: базовый параметр скорости
        """

        if is_fly and is_sneak:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            base_speed *= 1.2
        elif is_sneak:
            base_speed *= 0.5
        else:
            raise ValueError('Ни ползать ни летать не умеешь!')

        if direction == 'UP':
            new_y = unit_axis_y + base_speed
            new_x = unit_axis_x

        elif direction == 'DOWN':
            new_y = unit_axis_y - base_speed
            new_x = unit_axis_x

        elif direction == 'LEFT':
            new_y = unit_axis_y
            new_x = unit_axis_x - base_speed

        elif direction == 'RIGHT':
            new_y = unit_axis_y
            new_x = unit_axis_x + base_speed

        field.set_unit(x=new_x, y=new_y, unit=self)


