class OurClass():
    def __init__(self, name, location, size=0, members = None):
        self.name = name
        self.location = location
        self.size = size
        # self.questions_asked = []
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False
        if members == None:
            self.members = []
        else:
            self.members = members
        pass

    def check_if_at_capacity(self):
       return self.at_capacity

   # def add_question_asked(self, question):
   #      self.questions_asked.append(question)

    def add_class_members(self, num):
        self.size += num

        if self.size >= 20:
            print('Capacity Reached!!')
            self.at_capacity = True

# myC = OurClass('english','galv',14)
