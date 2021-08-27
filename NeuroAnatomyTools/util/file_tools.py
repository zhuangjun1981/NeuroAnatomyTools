import os


def look_for_unique_file(source, identifiers, file_type=None, print_prefix='', is_full_path=False,
                         is_verbose=True):

    fns = look_for_file_list(source=source,
                             identifiers=identifiers,
                             file_type=file_type,
                             is_full_path=is_full_path)

    if len(fns) == 0:
        if is_verbose:
            print(f'{print_prefix}: Did not find file. Returning None.')
        return
    elif len(fns) > 1:
        if is_verbose:
            print(f'{print_prefix}: Found more than one files. Returning None.')
        return
    else:
        return fns[0]


def look_for_file_list(source, identifiers, file_type=None, is_full_path=False):

    fns = [fn for fn in os.listdir(source) if os.path.isfile(os.path.join(source, fn))]

    if file_type is not None:
        fns = [fn for fn in os.listdir(source) if os.path.splitext(fn)[1] == f'.{file_type}']

    for identifier in identifiers:
        fns = [fn for fn in fns if identifier in fn]

    if is_full_path:
        fns = [os.path.abspath(os.path.join(source, f)) for f in fns]

    fns.sort()

    return fns