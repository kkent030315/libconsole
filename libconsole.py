import pyparsing


def clear_console():
    print('\033[H\033[J')


def non_ascii(string: str) -> str:
    esc = pyparsing.Literal('\x1b')
    escape_sequence = pyparsing.Combine(esc + '[' + \
                                        pyparsing.Optional(
                                            pyparsing.delimitedList(
                                                pyparsing.Word(pyparsing.nums),
                                                ';')
                                        ) + \
                                        pyparsing.oneOf(list(pyparsing.alphas)))
    return \
        pyparsing.Suppress(escape_sequence)\
        .transformString(string)


def print_box(headers=None, rows=None, v='│', rv=' ', h='─', corners=None, sep=None, f=print, pad=2):
    if corners is None:
        corners = ['╭', '╮', '╰', '╯']

    if sep is None:
        sep = ['├', '┤']

    no_headers = headers is None
    padding = " " * pad

    headers_length = 0 if no_headers else len(headers)
    rows_length = len(rows)

    if headers_length <= 0 and rows_length <= 0:
        return

    if not no_headers:
        if not headers_length == len(rows[0]):
            raise Exception(f'Headers must have same length as rows')

    if no_headers:
        buffers = [f'{v}' for _ in range(rows_length + 2)]
        has_2d_array = type(rows[0]) == list

        if has_2d_array:
            raise Exception('2D Array is not supported')

        # support for ascii-characters
        ascii_length = [len(row_item) - len(non_ascii(row_item)) for row_item in rows]

        max_width = len(max(rows, key=lambda x: len(non_ascii(x))))

        for irow in range(rows_length):
            row_item = rows[irow]
            buffers[irow + 1] += f'{padding}{row_item.ljust(max_width + ascii_length[irow])}{padding}{v}'
    else:

        buffers = [f'{v}' for _ in range(rows_length + 4)]

        for iheader in range(headers_length):
            column_header = headers[iheader]

            column_header_length = len(non_ascii(column_header))
            column_max_width = max(column_header_length,
                                   max([len(non_ascii(rows[irow][iheader])) for irow in range(rows_length)]))

            # support for ascii-characters in column header
            column_header_ascii_length = len(column_header) - column_header_length

            # render the header
            buffers[1] += f'{padding}{column_header.ljust(column_max_width + column_header_ascii_length)}{padding}'

            if not iheader == headers_length - 1:
                # item separator
                buffers[1] += f'{rv}'
            else:
                # border in right
                buffers[1] += f'{v}'

            for irow in range(rows_length):
                column_item = rows[irow][iheader]

                # support for ascii-characters in column item
                column_item_ascii_length = len(column_item) - len(non_ascii(column_item))

                # render the row in the column
                buffers[irow + 3] += f'{padding}{column_item.ljust(column_max_width + column_item_ascii_length)}{padding}'

                if not iheader == headers_length - 1:
                    # item separator
                    buffers[irow + 3] += f'{rv}'
                else:
                    # border in right
                    buffers[irow + 3] += f'{v}'

    max_width = max([len(non_ascii(buffer)) for buffer in buffers])

    border_up = f'{corners[0]}{h * (max_width - 2)}{corners[1]}'
    border_bottom = f'{corners[2]}{h * (max_width - 2)}{corners[3]}'

    buffers[0] = border_up
    buffers[-1] = border_bottom

    if not no_headers:
        # connectors in left and right for header separator
        buffers[2] = f'{sep[0]}{h * (max_width - 2)}{sep[1]}'

    f(*buffers, sep='\n')
