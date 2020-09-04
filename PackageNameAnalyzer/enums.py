# Constant in your code should be kept here, like for severity type is as follows

import enum


class SeverityType(enum.Enum):
    critical = 5
    high = 4
    medium = 3
    low = 2
    info = 1
