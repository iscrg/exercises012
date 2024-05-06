class Load:
    """
    The Load class provides a static method for loading air ticket data from a file.
    """
    data = []

    @staticmethod
    def write(file_name: str):
        """
        Loads air ticket data from the specified file.

        :param file_name: The name of the file containing air ticket data.
        """
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
    """
    The AirTicket class represents an air ticket with various attributes.
    """
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
        """
        Initializes an AirTicket object.

        :param passenger_name: The passenger's name.
        :param _from: The departure location.
        :param to: The arrival location.
        :param data_time: The date and time of the flight.
        :param flight: The flight number.
        :param seat: The seat number.
        :param _class: The class of the ticket (e.g., economy, business).
        :param gate: The gate number.
        """
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.data_time = data_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __repr__(self):
        """
        Returns a string representation of the air ticket.

        :return: A string representing the air ticket.
        """
        passenger_name = self.passenger_name + ' ' * (16 - len(self.passenger_name))
        _from = self._from + ' ' * (4 - len(self._from))
        to = self.to + ' ' * (3 - len(self.data_time))
        data_time = self.data_time + ' ' * (16 - len(self.data_time))
        flight = self.flight + ' ' * (20 - len(self.flight))
        seat = self.seat + ' ' * (4 - len(self.seat))
        _class = self._class + ' ' * (3 - len(self._class))
        gate = self.gate + ' ' * (4 - len(self.gate))

        return f'|{passenger_name}|{_from}|{to}|{data_time}|{flight}|{seat}|{_class}|{gate}|'
