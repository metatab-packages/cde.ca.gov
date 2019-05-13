""" Example pylib functions"""



def currency_float(v, row, row_n, i_s, i_d, header_s, header_d,scratch, errors, accumulator):
    """ An example column transform.

    This is an example of a column transform with all of the arguments listed. An real transform
    can omit any ( or all ) of these, and can supply them in any order; the calling code will inspect the
    signature.

    When the function is listed as a transform for a column, it is called for every row of data.

    :param v: The current value of the column
    :param row: A RowProxy object for the whiole row.
    :param row_n: The current row number.
    :param i_s: The numeric index of the source column
    :param i_d: The numeric index for the destination column
    :param header_s: The name of the source column
    :param header_d: The name of the destination column
    :param scratch: A dict that can be used for storing any values. Persists between rows.
    :param errors: A dict used to store error messages. Persists for all columns in a row, but not between rows.
    :param accumulator: A dict for use in accumulating values, such as computing aggregates.
    :return: The final value to be supplied for the column.
    """

    if not v:
        return v
        
    return float(str(v).replace('$',''))
    
def more_or_less(v):
    
    if not v:
        return
    
    if 'less than 60%' in v:
        return 'lt_60'
    elif '60% or more' in v:
        return 'gte_60'
    elif 'Commodity' in v:
        return 'commodity'
    else:
        return v