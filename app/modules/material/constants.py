__author__ = 'kurt'


class type:
    roll = 0
    pallete = 1

    type_names = {
        roll: 'Катушка',
        pallete: 'Паллета'
    }

    def get_type(self, type):
        if type is None:
            return None
        else:
            return self.type_names[type]


