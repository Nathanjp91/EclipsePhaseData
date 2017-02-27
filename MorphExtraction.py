import io
import re

import click

APTITUDES = ["COG", "COO", "SOM", "SAV", "WIL", "REF", "INT"]


class Morph:
    def __init__(self, data, morph_type):
        self.Data = io.StringIO(data)
        self.Name = self.Data.readline()
        self.Type = morph_type
        self.Implants = []
        self.Movement = []
        self.AptitudeMax = []
        self.Durability = ""
        self.WoundThresh = ""
        self.Advantages = []
        self.Disadvantages = []
        self.Traits = []
        self.Notes = ""
        self.CP = ""
        self.Cost = ""
        self.SpeedMod = ""
        self.Description = ""
        self.parse_data()
        self.write_to_file()

    def write_to_file(self):
        print ("Name: ", self.Name)
        print ("Type: ", self.Type)
        print ("Implants: ", self.Implants)
        print ("Movement: ", self.Movement)
        # print ("APTITUDES (Maximum)")
        # for apt in APTITUDES:
        #     print(apt)
        print ("Durability: ", self.Durability)
        print ("Wound Threshold: ", self.WoundThresh)
        print ("Advantages: ", self.Advantages)
        print ("Descritpion: ", self.Description)

    def parse_data(self):
        for line in self.Data:
            if "Implants: " in line:
                self.Implants = line.split(',')
                self.Implants[0] = self.Implants[0][9:]
            elif "Durability: " in line:
                self.Durability = line.partition(': ')
                self.Durability = self.Durability[2]
            elif "Wound Threshold: " in line:
                self.WoundThresh = line.partition(': ')
                self.WoundThresh = self.WoundThresh[2]
            elif "Advantages: " in line:
                temp = line.partition(': ')
                temp = temp[2].split(',')
                print (self.Name)
                print (temp)
                for item in temp:
                    if "trait" in item:
                        self.Traits.append(item)  # remove the traits that are lumped
                    if "Movement Rate" in item:
                        self.Movement.append(item)  # remove the movement rate upgrades
                    self.Advantages += self.advantage_parsing(item)
            elif "Disadvantages: " in line:
                temp = line.partition(': ')
                temp = temp[2].split(',')
                for item in temp:
                    if "trait" in item:
                        self.Traits.append(item)
                    elif "Movement Rate" in item:
                        self.Movement.append(item)
            elif "Credit Cost: " in line:
                self.Cost = line
            elif "CP Cost: " in line:
                self.CP = line
            elif "Movement Rate: " in line:
                temp = line.partition(': ')
                self.Movement += temp[2]
            elif "Aptitude Maximum: " in line:
                pass #TODO
            elif "Notes: " in line:
                pass #TODO
            else:
                self.Description += line

    def advantage_parsing(self, item):
        Apt_Check = [apt for apt in APTITUDES if apt in item]
        if Apt_Check:
            m = re.search('([+])([0-9]+)', item)  # Get the +5, +10 or +15 aptitude
            num = m.group(2)
            return [{Apt_Check[0]: num}]
        elif "choice" in item:
            if "one" in item:
                m = re.search('([+])([0-9]+)', item)  # Get the +5, +10 or +15 aptitude
                num = m.group(2)
                return [{"Choice": num}]
            elif "two" in item:
                m = re.search('([+])([0-9]+)', item)  # Get the +5, +10 or +15 aptitude
                num = m.group(2)
                return [{"Choice": num}, {"Choice": num}]
            elif "three" in item:
                m = re.search('([+])([0-9]+)', item)  # Get the +5, +10 or +15 aptitude
                num = m.group(2)
                return [{"Choice": num}, {"Choice": num}, {"Choice": num}]
        if "skill" in item:
            m = re.search('([+])([0-9]+)', item)  # Get the +5, +10 or +15 aptitude
            num = m.group(2)
            s = re.search('([0-9]+[ ])([A-Z]\w+)', item)
            skill = s.group(2)
            return [{skill: num}]
        return []


@click.command()
@click.option('--input-file', default='biomorph.txt', help='The file of biomorph data to parse.')
@click.option('--output-file', default='biomorph.yaml', help='The file to write the yaml output.')
@click.option('--morph-type', type=click.Choice(['Biomorph']), default='Biomorph', help='The morph type.')
def main(input_file, output_file, morph_type):
    data = open(input_file, 'r')
    data = data.read()
    temp = data.partition('---')
    temp = temp[2]
    while temp is not "":
        temp = temp.partition('---')
        if "END" not in temp[0]:
            morph_data = temp[0]
            morph_to_save = Morph(morph_data, morph_type)
        temp = temp[2]


if __name__ == '__main__':
    main()
