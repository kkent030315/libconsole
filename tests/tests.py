from libconsole import print_box


class COLORS:
    WHITE = '\033[30m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\u001b[36m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    BG_BLACK = '\33[47m'


def main():
    headers = [f'{COLORS.BOLD}Server Name{COLORS.END}', 'Status', 'IPv4', f'{COLORS.UNDERLINE}Officer{COLORS.END}']
    rows = [
        [f'Korea-EG014', f'{COLORS.GREEN}Running{COLORS.END}', '217.185.216.48', 'Martina Legge'],
        [f'England-EG094', f'{COLORS.GREEN}Running{COLORS.END}', '130.112.20.222', 'Aedan Griffith'],
        [f'Germany-EG035', f'{COLORS.GREEN}Running{COLORS.END}', '97.21.47.114', 'Corrie Crowther'],
        [f'USA-EG022', f'{COLORS.RED}Not Running{COLORS.END}', '141.118.252.56', 'Haaris Mccormick'],
        [f'Tokyo-EG067', f'{COLORS.YELLOW}Stopped{COLORS.END}', '233.244.8.220', 'Bhavik Bentley']
    ]

    print_box(rows=['Hello World'], pad=31)
    print_box(headers=headers, rows=rows)
    print_box(rows=[f'             {COLORS.BOLD}{COLORS.CYAN}Print{COLORS.END} '
                    f'{COLORS.ITALIC}{COLORS.PURPLE}Box-Style{COLORS.END} '
                    f'{COLORS.BLUE}{COLORS.UNDERLINE}Beautifully{COLORS.END}',
                    f'libconsole provides beautiful outputs in console :3',
                    f'also it supports ascii-colors ₍₍ (ง ˙ω˙)ว ⁾⁾',
                    f'',
                    f'{COLORS.BOLD}Usage:{COLORS.END}',
                    f'{COLORS.BG_BLACK}{COLORS.WHITE} $ pip install libconsole {COLORS.END}',
                    f'',
                    f'{COLORS.BLUE}>>>{COLORS.END} import libconsole',
                    f'{COLORS.BLUE}>>>{COLORS.END} libconsole.print_box(rows=["Hello"])',
                    f'╭─────────╮',
                    f'│  Hello  │',
                    f'╰─────────╯'], pad=11)


if __name__ == '__main__':
    main()
