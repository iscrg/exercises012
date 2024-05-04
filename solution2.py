class Load:
    data = []

    @staticmethod
    def write(file_name: str):
        with open(file_name, 'r', encoding='UTF-8') as f:
            for line in [line.rstrip() for line in f.readlines()][1:]:
                passenger_name, _from, to, data_time, flight, seat, _class, gate, empty = line.split(';')
                Load.data.append(AirTicket(
                    passenger_name,
                    _from,
                    to,
                    data_time,
                    flight,
                    seat,
                    _class,
                    gate
                ))


class AirTicket:
    def __init__(
            self,
            passenger_name: str,
            _from: str,
            to: str,
            data_time: str,
            flight: str,
            seat: str,
            _class: str,
            gate: str
                 ):
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.data_time = data_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __repr__(self):
        passenger_name = self.passenger_name + ' ' * (16 - len(self.passenger_name))
        _from = self._from + ' ' * (4 - len(self._from))
        to = self.to + ' ' * (3 - len(self.data_time))
        data_time = self.data_time + ' ' * (16 - len(self.data_time))
        flight = self.flight + ' ' * (20 - len(self.flight))
        seat = self.seat + ' ' * (4 - len(self.seat))
        _class = self._class + ' ' * (3 - len(self._class))
        gate = self.gate + ' ' * (4 - len(self.gate))

        return f'|{passenger_name}|{_from}|{to}|{data_time}|{flight}|{seat}|{_class}|{gate}|'
