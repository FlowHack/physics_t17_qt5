from random import uniform
from settings import LOGGER
from math import pow as math_pow
from math import fabs
from bin import MessageBox


def calculate_experiment(p_ball: float, p_water: float, radius: float,
                         height: float, abs_viscosity: float) -> dict:
    """Функция вычислений для режима эксперимента

    Args:
        p_ball (float): плотность шара
        p_water (float): плотность жидкости
        radius (float): радиус (м)
        height (float): высота (м)
        abs_viscosity (float): коэффициент вязкости

    Returns:
        dict: все вычисленные значения
    """

    logger = LOGGER('calculate_experiment', 'calculations')
    logger.info('Начинаю вычисления для режима эксперимента')

    result = {
        'p_ball': p_ball,
        'p_water': p_water,
        'radius': radius,
        'height': height,
        'viscosity': abs_viscosity
    }

    speed = round(
        calculate_speed(
            p_ball=p_ball, p_water=p_water, radius=radius,
            viscosity=abs_viscosity
        ), 5
    )
    result['speed'] = speed

    logger.info('Вычиление 3-ёх значений времени и вязкости.')
    viscosities = []
    avg_time = 0
    times = []
    abs_time = 0

    for i in range(3):
        time = calculate_time(height=height, speed=speed)
        if time is None:
            return None
        abs_time = time['abs_time']
        times.append(time['time'])

    if (sum_times := sum(times)) / 3 != abs_time:
        difference = fabs(abs_time - sum_times) / 3
        for i in range(len(times)):
            new_time = times[i] + difference
            result[f'time{i+1}'] = round(new_time, 5)
            avg_time += new_time

            viscosities.append(
                calculate_viscosity(
                    p_ball=p_ball, p_water=p_water, radius=radius,
                    height=height, time=new_time
                )
            )

    need_add = 0.00
    if (sum_vis := sum(viscosities)) / 3 != abs_viscosity:
        difference = fabs(abs_viscosity - sum_vis) / 3
        need_add = difference / 3

    result['viscosity1'] = round(viscosities[0] + need_add, 3)
    result['viscosity2'] = round(viscosities[1] + need_add, 3)
    result['viscosity3'] = round(viscosities[2] + need_add, 3)
    result['avg_time'] = round(avg_time / 3, 5)

    return result


def calculate_phenomen(radius: float, p_ball: float, p_water: float,
                       viscosity: float) -> dict:
    """Вычисления для режима явления

    Args:
        radius (float): радиус (м)
        p_ball (float): плотность шара
        p_water (float): плотность жидкости
        viscosity (float): коэффициент вязкости

    Returns:
        dict: вычисленные скорость и время для анимации
    """

    logger = LOGGER('calculate_phenomen', 'calculations')
    logger.info('Начинаю вычисления для режима явления')

    speed = calculate_speed(
        p_ball=p_ball, p_water=p_water, radius=radius,
        viscosity=viscosity
    )

    return {
        'speed': speed,
        'time': round(calculate_time(height=0.55, speed=speed)['abs_time'], 10)
    }


def calculate_speed(p_ball: float, p_water: float, radius: float,
                    viscosity: float) -> float:
    """Вычисление скорости

    Args:
        p_ball (float): плотность шара
        p_water (float): плотность воды
        radius (float): радиус (м)
        viscosity (float): коэффициент вязкости

    Returns:
        float: вычисленная скорость
    """

    logger = LOGGER('calculate_speed', 'calculations')
    logger.warning(
        f'Вычисляю скорость. Переменные: {p_ball=}; {p_water=}; '
        f'{radius=}; {viscosity=}'
    )
    g = 9.81

    numerator = 2 * (p_ball - p_water) * g * math_pow(radius, 2)
    logger.info(f'{numerator=}')
    denumerator = 9 * viscosity
    logger.info(f'{denumerator=}')

    speed = numerator / denumerator
    logger.info(f'{speed=}')
    return speed


def calculate_time(height: float, speed: float) -> float:
    """Вычисление времени

    Args:
        height (float): пройденный путь (м)
        speed (float): скорость

    Returns:
        float: вычисленное время
    """

    logger = LOGGER('calculate_time', 'calculations')
    logger.info('Вычисляю погрешность времени')
    error_rate = uniform(-0.001, 0.001)
    logger.info(f'{error_rate=}')
    try:
        abs_time = fabs(height / speed)
        t = fabs(abs_time + uniform(-0.01, 0.01))
    except ZeroDivisionError:
        logger.info(
            f'По указанным значениям шар не тонет! {speed=}. Деление на 0!'
        )
        MessageBox(
            title='Ошибка!', text='Шар не тонет!',
            msg='По указанным значениям шар не тонет!'
        ).showwarning()

        return None
    logger.info(f'{t=}')
    return {
        'time': t,
        'abs_time': abs_time
    }


def calculate_viscosity(p_ball: float, p_water: float, radius: float,
                        height: float, time: float) -> float:
    """Вычисление коэффициента вязкости

    Args:
        p_ball (float): плотность шара
        p_water (float): плотность жидкости
        radius (float): радиус (м)
        height (float): пройденный путь (м)
        time (float): время

    Returns:
        float: вычиленный коэффициент вязкости
    """

    logger = LOGGER('calculate_viscosity', 'calculations')
    logger.warning(f'Начинаю вычисление коэффициента вязкости. Переменные:'
                   f'{p_ball=}; {p_water=}; {radius=}; {height=}; {time=}')
    g = 9.81

    numerator = 2 * (p_ball - p_water) * g * math_pow(radius, 2) * time
    logger.info(f'{numerator=}')
    denumerator = 9 * height
    logger.info(f'{denumerator=}')

    viscosity = numerator / denumerator
    logger.info(f'{viscosity=}')

    return fabs(viscosity)


def splitting_number(number):
    result = []

    for i in range(1, number):
        for k in range(1, 11):
            result.append((i - 1) + (k / 10))

    return result[::-1], len(result)
