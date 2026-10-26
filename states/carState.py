from aiogram.fsm.state import State, StatesGroup

class CarState(StatesGroup):
    car_name = State()
    car_color = State()
    car_price = State()
    car_years = State()

