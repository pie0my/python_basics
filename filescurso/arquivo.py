def algo(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'utilize um numero'
    except ValueError as err:
        return err
