class Car:
    def __init__(
        self,
        color: str,
        count_passenger_seats: int,
        is_baby_seat: bool
    ):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return f"Color of auto: {self.color} | Passengers seats: {self.count_passenger_seats} | Child seat: {self.is_baby_seat} | Car is busy:{self.is_busy}"



class Taxi:

    def __init__(self,cars):

        self.cars = cars

    def find_car(self,count_passenger,is_baby):
        for car in self.cars:
            if count_passenger<=car.count_passenger_seats and is_baby == car.is_baby_seat:
                car.is_busy = True
                return car
        return None



first_car = Car(color='Black',count_passenger_seats=4,is_baby_seat=True)
car_list = Taxi([first_car])
search = car_list.find_car(count_passenger=2,is_baby=True)
print(search)
if not search:
    print('No available cars!')