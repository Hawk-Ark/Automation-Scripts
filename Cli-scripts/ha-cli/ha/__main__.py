#!/usr/bin/env python3

import argparse
import yaml

def generate_script(output_file):
    data = {
        'script': {
            'alias': 'Example Script',
            'sequence': [
                {'service': 'light.turn_on', 'target': {'entity_id': 'light.living_room'}},
                {'delay': '00:00:05'},
                {'service': 'light.turn_off', 'target': {'entity_id': 'light.living_room'}}
            ]
        }
    }

    with open(output_file, 'w') as f:
        yaml.dump(data, f, sort_keys=False)

    print(f" YAML script generated at: {output_file}")

def main():
    parser = argparse.ArgumentParser(prog='ha', description="HA Script Generator CLI")
    subparsers = parser.add_subparsers(dest='command')

    generate_parser = subparsers.add_parser('generate', help='Generate scripts or configs')
    generate_subparsers = generate_parser.add_subparsers(dest='subcommand')

    script_parser = generate_subparsers.add_parser('script', help='Generate a script YAML')
    script_parser.add_argument('-o', '--output', required=True, help='Output YAML file')

    args = parser.parse_args()

    if args.command == 'generate' and args.subcommand == 'script':
        generate_script(args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
