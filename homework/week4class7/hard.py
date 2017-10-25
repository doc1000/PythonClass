class OurClass():
    def __init__(self, name, location, size=0, members = None):
        self.name = name
        self.location = location
        self.size = size
        # self.questions_asked = []
        self.check_if_at_capacity()
        if members == None:
            self.members = []
        else:
            self.members = members
        pass


    def check_if_at_capacity(self):
        if self.size >= 31:
            self.at_capacity = True
        else:
            self.at_capacity = False
        return self.at_capacity

   # def add_question_asked(self, question):
   #      self.questions_asked.append(question)

    def add_class_members(self, member):
        self.members.append(member)
        self.size += 1

        self.check_if_at_capacity()
        # if self.size >= 20:
        #     print('Capacity Reached!!')
        #     self.at_capacity = True

# myC = OurClass('english','galv',14)

class Member():
    def __init__(self,name, hair_color, birthdate):
        self.name = name
        self.hair_color=hair_color
        self.birthdate=birthdate
        self.questions_asked = []
        self.lines_of_code = ''
        self.num_lines_coded = 0
        self.coding_level = 'beginner'

    def added_code_line(self,line_of_code):
        self.lines_of_code += line_of_code
        self.num_lines_coded += 1

    def get_coding_level(self):
        my_levels = [(-1,'beginner'),(100,'novice'),(1000,'intermediate'),(10000,'expert')]
        self.coding_level = max([(x,y) for x,y in my_levels if self.num_lines_coded > x])[1]
        return self.coding_level
