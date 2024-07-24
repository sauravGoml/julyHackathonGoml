class Department:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.children = []


def find_managers(department, department_name, path):
    if department.name == department_name:
        path.append(department.manager)
        return True

    for child in department.children:
        if find_managers(child, department_name, path):
            path.append(department.manager)
            return True

    return False

def get_managers_from_department(root, department_name):
    path = []
    if find_managers(root, department_name, path):
        return path
    else:
        return []

ceo = Department("CEO", "Alice")
engineering = Department("Engineering", "Bob")
sales = Department("Sales", "Charlie")
backend = Department("Backend", "David")
frontend = Department("Frontend", "Eve")
domestic = Department("Domestic", "Fay")

ceo.children = [engineering, sales]
engineering.children = [backend, frontend]
sales.children = [domestic]

output = get_managers_from_department(ceo, "Backend")
print(output)