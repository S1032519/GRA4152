"""
The class Appointment is a superclass for diffrent appointments, wheter it is a one time appointment or a daily or monthly appointment.
In this case it is a superclass for the subclasses OneTime, Daily and Monthly.

The superclass contains the following:
    1. A constructor which initializes the object "Appointment" with a description.
    2. A special method __repr__ which is meant to be over-rided in the subclasses.
    3. A method occursOn which checks whether an appointment happens on a given date.
"""

class Appointment: ## Superclass
    def __init__(self, appointment_description): ## Assign description to all appointments
        self._appointment_description = appointment_description

    def occursOn(self, year, month, day): ## Method meant to be over-rided in the subclasses
        raise NotImplementedError("Subclasses should implement this method")

    def __repr__(self): ## Special method __repr__ meant to be over-rided in the subclasses
        raise NotImplementedError("Subclasses should implement this method")

"""
The class OneTime is a subclass of superclass Appointment.

The subclass contains the following:
    1. A constructor which initializes the object "OneTime", it inherits from the superclass by initializing the superclass constructor.
    This is done because we want the appointment_description to be set up before adding any spesific properties of the subclass.
    2. A method occursOn which is overridden from the superclass by adding spesific properties (year, month, date) it returns True if
    the correct dates for an appointment is initiated.
    3. A special method __repr__ which is overridden from the superclass by adding the spesific output for an appointment with a date.
"""

class OneTime(Appointment): ## Subclass
    def __init__(self, appointment_description, year, month, day): ## Subclass constructor
        super().__init__(appointment_description) ## Inherits the superclass constructor
        self._year = year
        self._month = month
        self._day = day
    
    def occursOn(self, year, month, day): ## Method for checking calendar
        return self._year == year and self._month == month and self._day == day

    def __repr__(self): ## Method for spesific output
        return "One time appointment on {}-{}-{}. {}".format(self._year, self._month, self._day, self._appointment_description)

"""
The class Daily is a subclass of superclass Appointment.

The subclass contains the following:
    1. A constructor which initializes the object "Daily", it inherits from the superclass by initializing the superclass constructor.
    This is done because we want the appointment_description to be set up before adding any spesific properties of the subclass.
    2. A method occursOn which is overridden from the superclass. It returns True if one has added a daily routine.
    3. A special method __repr__ which is overridden from the superclass by adding the spesific output for an appointment.
"""

class Daily(Appointment): ## Subclass
    def __init__(self, appointment_description): ## Subclass constructor
        super().__init__(appointment_description) ## Inherits the superclass constructor
    
    def occursOn(self, year = None, month = None, day = None): ## Method for checking calendar
        return True

    def __repr__(self): ## Method for spesific output
        return "Daily appointment. {}".format(self._appointment_description)

"""
The class Monthly is a subclass of superclass Appointment.

The subclass contains the following:
    1. A constructor which initializes the object "Monthly", it inherits from the superclass by initializing the superclass constructor.
    This is done because we want the appointment_description to be set up before adding any spesific properties of the subclass.
    2. A method occursOn which is overridden from the superclass by adding spesific properties (day) it returns True if
    the correct day for an appointment is initiated.
    3. A special method __repr__ which is overridden from the superclass by adding the spesific output for an appointment with a date.
"""

class Monthly(Appointment): ## Subclass
    def __init__(self, appointment_description, day): ## Subclass constructor
        super().__init__(appointment_description) ## Inherits the superclass constructor
        self._day = day
    
    def occursOn(self, year, month, day): ## Method for checking calendar
        return self._day == day

    def __repr__(self): ## Method for spesific output
        return "Monthly appointment on day {}. {}".format(self._day, self._appointment_description)
  
## Test

dentist_appointment = OneTime("See dentist", 2023, 12, 24)
go_to_work = Daily("Work")
play_golf = Monthly("Play golf", 16)
appointments = [dentist_appointment, go_to_work, play_golf]

test_dates = {
    dentist_appointment: (2023, 12, 24),
    play_golf: (2023, 1, 16)
}

for appointment in appointments:
    if isinstance(appointment, Daily):
        print(appointment)
    else:
        test_date = test_dates.get(appointment)
        if test_date and appointment.occursOn(*test_date):
            print(appointment)