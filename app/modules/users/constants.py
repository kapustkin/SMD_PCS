__author__ = 'kurt'


class role:
    admin = 0
    engineer = 10
    supervisor = 20
    operator = 30
    user = 2


    role_names = {
      admin: 'admin',
      operator: 'operator',
      engineer: 'engineer',
      supervisor: 'supervisor',
      user: 'user',
    }

    def get_role(self, role):
        return self.role_names[role]


