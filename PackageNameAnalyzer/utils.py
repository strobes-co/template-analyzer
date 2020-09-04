# Add utility functions here

# example:

def severity_to_cvss(severity: int) -> float:
    """ Converts severity in range [1-5] inclusive to normalized CVSS score
    Args:
        severity (int): Severity to be converted
    Returns:
        float: Returns CVSS score
    """
    if severity == 5:
        return 9.1
    elif severity == 4:
        return 6.9
    elif severity == 3:
        return 4.1
    elif severity == 2:
        return 0.1
    else:
        return 0.0