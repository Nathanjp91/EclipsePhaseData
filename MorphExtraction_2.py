import yaml

import click

STAT_NAMES = {
    'Implants',
    'Aptitude Maximum',
    'Durability',
    'Wound Threshold',
    'Advantages',
    'Disadvantages',
    'Notes',
    'CP Cost',
    'Credit Cost',
}

DESCRIPTION_FIELD = 'Description'


@click.command()
@click.option('--input-filename', default='biomorph.txt', help='The file of biomorph data to parse.')
@click.option('--output-filename', default='biomorph.yaml', help='The file to write the yaml output.')
@click.option('--morph-type', type=click.Choice(['Biomorph']), default='Biomorph', help='The morph type.')
def main(input_filename, output_filename, morph_type):
    with open(input_filename, mode='r', encoding='utf-8') as f:
        input_data = f.read()

    # Splits morphs into list. Note the first element in the list is '' so ignore it.
    split_data = input_data.split('---')[1:]

    data_dict = {}
    for morph in split_data:
        name, data = morph.split('\n', maxsplit=1)
        data_dict[name] = {}  # Create the inner dict.

        for line in data.split('\n'):
            try:
                stat_name, stat_value = line.split(': ')  # Include space after : to strip it out easily.
                data_dict[name][stat_name] = stat_value
            except ValueError:
                # Cant split because the line is part of the description, so append it.
                try:
                    # If the discription already exists, append the new line to it, otherwise add the key.
                    data_dict[name][DESCRIPTION_FIELD] += line
                except KeyError:
                    data_dict[name][DESCRIPTION_FIELD] = line

    with open(output_filename, mode='w') as out_file:
        yaml.dump(data_dict, out_file, default_flow_style=False, allow_unicode=True, indent=4)


if __name__ == '__main__':
    main()
