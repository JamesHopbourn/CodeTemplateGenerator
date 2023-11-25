import os
import argparse
import subprocess
from pathlib import Path
from configparser import ConfigParser
from jinja2 import Environment, FileSystemLoader


def read_section_config(config_file, section):
    config = ConfigParser()
    config.read(config_file)
    return dict(config.items(section))

def create_config_file(config_file):
    if not config_file.exists():
        config = ConfigParser()
        config['DEFAULT'] = {'name': 'Your name', 'email': 'example@gmail.com'}
        config['TOOL'] = {'editor': 'vim'}
        with open(config_file, 'w') as file:
            config.write(file)
        print(f"Configuration file created at: {config_file}")

def main():
    config_file = Path.home() / ".codetemplaterc"
    create_config_file(config_file)

    parser = argparse.ArgumentParser(description="Code Template Generator")
    parser.add_argument("filename", type=str, nargs="?", help="Create new file name")
    parser.add_argument("template", type=str, nargs="?", help="Specific template name")
    args = parser.parse_args()

    if not args.filename:
        parser.print_help()
        return

    data = read_section_config(config_file, 'DEFAULT')
    file_extension = os.path.splitext(args.filename)[1]
    
    template_name = args.template if args.template else 'template'
    env = Environment(loader=FileSystemLoader(f"{Path.home()}/.codetemplate"))
    template = env.get_template(f'{template_name}{file_extension}')
    
    output = template.render(data)
    output_file_path = f'{os.getcwd()}/{args.filename}'
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(output)

    tool_config = read_section_config(config_file, 'TOOL')
    editor = tool_config.get('editor')
    subprocess.run([editor, output_file_path])

if __name__ == "__main__":
    main()
