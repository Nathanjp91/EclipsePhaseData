import io
import re

FILE_TO_IMPORT = "morph.txt"
FILE_TO_EXPORT = "morphs.yaml"
APTITUDES = ["COG", "COO", "SOM", "SAV", "WIL", "REF", "INT"]


class Morph:
    def __init__(self, data):
        self.data = io.StringIO(data)
        self.name = self.data.readline()
        self.Type = ""
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
        self.description = ""
        self.parse_data()
        self.write_to_file()

    def write_to_file(self):
        print ("Name: ", self.name)
        print ("Description: ", self.description)
        print ("Type: ", self.Type)
        print ("Implants: ", self.Implants)
        print ("Movement: ", self.Movement)
        # print ("APTITUDES (Maximum)")
        # for apt in APTITUDES:
        #     print(apt)
        print ("Durability: ", self.Durability)
        print ("Wound Threshold: ", self.WoundThresh)
        print ("Advantages: ", self.Advantages)

    def parse_data(self):
        for line in self.data:
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
                self.cost = line
            elif "CP Cost: " in line:
                self.CP = line
            elif "Movement Rate: " in line:
                temp = line.partition(': ')
                self.Movement += temp[2]
            elif "Aptitude Maximum: " in line:
                pass  # TODO
            elif "Notes: " in line:
                pass  # TODO
            else:  # Description
                self.description = line

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


if __name__ == '__main__':
    data = open(FILE_TO_IMPORT, 'r')
    # import ipdb; ipdb.set_trace()
    data = data.read()
    temp = data.partition('---')
    temp = temp[2]
    # item2 = "This string contains COO +5
    # APTITUDES = ["COG","COO","SOM","SAV","WIL","REF","INT"]
    # Apt_Check = [apt for apt in APTITUDES if apt in item2]
    # if Apt_Check:
    #     m = re.search('([+])([0-9]+)', item2)
    #     print (m.group())

    while temp is not "":
        temp = temp.partition('---')
        if "END" not in temp[0]:
            morph_data = temp[0]
            morph_to_save = Morph(morph_data)
        temp = temp[2]
