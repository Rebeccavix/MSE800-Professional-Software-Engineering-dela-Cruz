class Company_Info:

    def __init__(self):
        self.staffs = []

    def attach(self, staff):
        self.staffs.append(staff)

    def detach(self, staff):
        self.staffs.remove(staff)

    def notify(self):
        for staff in self.staffs:
            staff.update(self)

class Concrete_Company_Info(Company_Info):

    def __init__(self):
        super().__init__()
        self.__news = None
        
    @property
    def news(self):
        return self.__news
    
    @news.setter
    def news(self, new_message):
        self.__news = new_message
        self.notify()


class Staff:
    def __init__(self, name):
        self.name = name

    def update(self, target):
        print(f"{self.name} knows the news {target.news}!!")




# client
staff_1 = Staff("Jack")
staff_2 = Staff("Rose")

company_info = Concrete_Company_Info()
company_info.attach(staff_1)
company_info.attach(staff_2)

company_info.news = "Tomorrow, holiday!!"

company_info.detach(staff_1)

company_info.news = "The revenue of this year increased significantly, everyones has a bonus!!!"
