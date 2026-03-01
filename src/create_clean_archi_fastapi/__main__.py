import subprocess

def main():
    subprocess.run([
        "uvx",
        "copier",
        "copy",
        "--trust",
        "gh:Online13/clean_archi_template_fastapi",
        "."
    ])