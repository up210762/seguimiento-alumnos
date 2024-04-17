import string as stg

regular_group:str = 'ISC'
dual_group: str='MFD'
epc_group: str = 'EPC'

def clean_text(string: str) -> str:
    found_group = None
    for i in range(0, 10):
        if len(str(i)) == 1:
            if regular_group in string and dual_group not in string and epc_group not in string:
                for char in stg.ascii_uppercase:
                    group = f'{regular_group}0{i}{char}'
                    if group in string:
                        found_group = group
                        break
            elif regular_group in string and dual_group in string and epc_group not in string:
                group = f'{regular_group}{dual_group}0{i}'
                if group in string:
                    found_group = group
                    break
        else:
            if regular_group in string and dual_group not in string and epc_group not in string:
                group = f'{regular_group}{i}{char}'
                if group in string:
                    found_group = group
                    break
            elif regular_group in string and dual_group in string and epc_group not in string:
                group = f'{regular_group}{dual_group}{i}'
                if group in string:
                    found_group = group
                    break

        if found_group:
            break
    if found_group:
        return found_group
    else:
        return string