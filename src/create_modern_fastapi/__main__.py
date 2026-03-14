import subprocess

def main():
    subprocess.run([
        "uvx",
        "copier",
        "copy",
        "--trust",
        "gh:Online13/create_modern_fastapi",
        "."
    ])