from school_schedule.student import Student

class HighSchoolStudent(Student):
    def __init__(self, name, grade, classes, has_parking_privileges=False, clubs=None):
        super().__init__(name, grade, classes)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = clubs if clubs else []
        
    def join_club(self, club_name):
        self.clubs.append(club_name)
        return self.clubs
    
    def display_parking_message(self):
        has_message = "has" if self.has_parking_privileges else "doesn't have"
        return f"{self.name} {has_message} parking priviliges"
    
    def display_clubs(self):
        clubs_str = ", ".join(self.clubs)
        if clubs_str:
            return f"{self.name} is a member of: {clubs_str}"
        return f"{self.name} hasn't join the club yet"
                
    def summary(self):
        student_summary = super().summary()
        parking_message = self.display_parking_message()
        clubs_message = self.display_clubs
        
        return "\n".join(student_summary, parking_message, clubs_message)
        
        