import os

def ps_eval(args: list) -> None:
    this_dir = os.path.dirname(__file__)
    ps_eval_path = 'stove/ps-eval'
    abs_file_path = os.path.join(this_dir, ps_eval_path)
    return os.popen(f"{abs_file_path} {' '.join(args)}").read()
