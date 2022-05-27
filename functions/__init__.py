from .app import create_shortcut_win, set_validator_double
from .additional import all_edits
from .calculations import (calculate_experiment, calculate_phenomen,
                           calculate_speed, calculate_time,
                           calculate_viscosity, splitting_number)
from .opengl_graphics import OpenGlWindow


__all__ = [
    # app
    'create_shortcut_win',
    'set_validator_double',
    # additional
    'all_edits',
    # calculations
    'calculate_experiment',
    'calculate_phenomen',
    'calculate_speed',
    'calculate_time',
    'calculate_viscosity',
    'splitting_number',
    # opengl_graphics
    'OpenGlWindow'
]
