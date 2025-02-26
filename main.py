def add_time(start, duration, start_day=None):
    # Dividir la hora de inicio y el periodo (AM/PM)
    start_time_parts = start.split()
    time_part = start_time_parts[0]
    period = start_time_parts[1]

    # Dividir la hora y los minutos de inicio
    hours, minutes = map(int, time_part.split(':'))

    # Convertir la hora de inicio a formato de 24 horas
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0

    # Dividir la duración en horas y minutos
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Sumar la duración a la hora de inicio
    total_minutes = minutes + duration_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = hours + duration_hours + extra_hours
    extra_days = total_hours // 24
    final_hours = total_hours % 24

    # Determinar el periodo final (AM/PM)
    if final_hours < 12:
        final_period = 'AM'
    else:
        final_period = 'PM'

    # Convertir la hora final a formato de 12 horas
    if final_hours == 0:
        final_hours_12 = 12
    else:
        final_hours_12 = final_hours if final_hours <= 12 else final_hours - 12

    # Formatear la hora final
    new_time = f"{final_hours_12}:{final_minutes:02d} {final_period}"

    # Calcular el día de la semana final si se proporciona
    if start_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(start_day.lower().capitalize())
        final_day_index = (start_day_index + extra_days) % 7
        final_day = days_of_week[final_day_index]
        new_time += f", {final_day}"

    # Añadir información sobre los días posteriores
    if extra_days == 1:
        new_time += " (next day)"
    elif extra_days > 1:
        new_time += f" ({extra_days} days later)"

    return new_time
print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)