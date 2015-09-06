__author__ = 'kurt'


class role:
    admin = 0
    engineer = 10
    supervisor = 20
    operator = 30
    user = 2


    role_names = {
      admin: 'Администратор',
      operator: 'Оператор',
      engineer: 'Инженер',
      supervisor: 'Начальник смены',
      user: 'Пользователь',
    }

    def get_role(self, role):
        return self.role_names[role]


class status:
    new = 0
    active = 1
    inactive = 2

    status_names = {
        new: 'Новый пользователь',
        active: 'Активен',
        inactive: 'Не активен'
    }

    def get_status(self, status):
        if status is None:
            return None
        else:
            return self.status_names[status]

