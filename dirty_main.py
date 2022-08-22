from datetime import *
from application.db.people import *
from application.salary import *

if __name__ == '__main__':
    print (datetime.now())
    calculate_salary()
    get_employees()