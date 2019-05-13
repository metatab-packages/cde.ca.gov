""" Example pylib functions"""


def combine(resource, doc, env, *args, **kwargs):
    """ An example row generator function.

    Reference this function in a Metatab file as the value of a Datafile:

            Datafile: python:pylib#row_generator

    The function must yield rows, with the first being headers, and subsequenct rows being data.

    :param resource: The Datafile term being processed
    :param doc: The Metatab document that contains the term being processed
    :param args: Positional arguments passed to the generator
    :param kwargs: Keyword arguments passed to the generator
    :return:


    The env argument is a dict with these environmental keys:

    * CACHE_DIR
    * RESOURCE_NAME
    * RESOLVED_URL
    * WORKING_DIR
    * METATAB_DOC
    * METATAB_WORKING_DIR
    * METATAB_PACKAGE

    It also contains key/value pairs for all of the properties of the resource.

    """
    
    # Aggregate all of the columns
    
    from itertools import zip_longest
    from collections import OrderedDict
    
    column_sets = []
    columns = ['year']
    for t in doc['Schema'].find('Root.Table'):
        try:
            column_sets.append([c.altname for c in t.find('Table.Column') if c.altname not in columns])
        except AttributeError:
            # The combined schemas entry has no altnames
            pass
            
            
    for s in zip_longest(*column_sets):
        for c in s:
            if c not in columns:
                columns.append(c)
    
    yield columns


    for r in doc.resources():
        if r.name.startswith('current_expense_'):
            for row in r.iterdict:
                new_row = OrderedDict([ (c, row.get(c)) for c in columns])
                new_row['year'] = r.year
                
                yield list(new_row.values())


def example_transform(v, row, row_n, i_s, i_d, header_s, header_d,scratch, errors, accumulator):
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

    return str(v)+'-foo'