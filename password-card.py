import string
import random
import os

class PassWordCard:

    def __init__(self, my_seed, number_of_categories=8):
        self._my_seed = my_seed
        self._number_of_categories = number_of_categories
        self._alphabet = string.ascii_uppercase
        self._symbols = string.ascii_letters + string.punctuation + string.digits
        self._master_map = self._make_master_map()

    def _category_map(self, current_seed):
        category_map = []
        symbols = list(self._symbols)
        random.seed(current_seed)
        random.shuffle(symbols)
        category_map = symbols[0:self._number_of_categories]
        return category_map

    def _make_master_map(self):
        master_map = {}
        for letter in self._alphabet:
            master_map[letter] = self._category_map(self._my_seed+letter)
        return master_map

    def _make_pass_word(self, master, category):
        pass_word = []
        for letter in master:
            pass_word.append(self._master_map[letter][category])
        pass_word = "".join(pass_word)
        return pass_word

    def print_card(self):
        for key, value in self._master_map.items():
            print("{} : {}".format(key,value))

    def export_card(self):
        latex_header = r"\documentclass[12pt]{article}"+"\n"+r"\usepackage{booktabs}"+"\n"+r"\usepackage{xcolor, colortbl}"+"\n"+r"\newcommand{\mc}[2]{\multicolumn{#1}{c}{#2}}"+"\n"+r"\definecolor{Gray}{gray}{0.85}"+"\n"+r"\newcolumntype{g}{>{\columncolor{Gray}}c}"+"\n"+r"\newcolumntype{w}{>{\columncolor{white}}c}"+"\n"+r"\begin{document}"

        
        latex_symbols = r"{}^&_$%#~"
        table = latex_header
        table_format = "l|"
        for i in range(self._number_of_categories):
            table_format += "w" if i%2 == 0 else "g"
        table += r"\begin{tabular}{"+table_format+r"}"+"\n"+r"\toprule"+"\n"

        rows = ""
        for key, value in self._master_map.items():
            value_ref = []
            for item in value:
                if item == "\\":
                    value_ref.append(r"\textbackslash")
                elif item in latex_symbols:
                    value_ref.append("\\"+item+r"{}")
                else:
                    value_ref.append(item)
            row = key+ " & "  + " & ".join(value_ref)+r"\\"+"\n"
            rows += row
        table += rows+r"\bottomrule"+"\n"+r"\end{tabular}"+"\n"+r"\end{document}"
        #print(table)

        with open("./card.tex", "w") as table_file:
            table_file.write(table)

        
        
    def get_pass_word(self, master, category):
        return self._make_pass_word(master, category)



def main():
    my_card = PassWordCard("ottavia", 8)
    my_card.print_card()
    print(my_card.get_pass_word("master", 5))
    my_card.export_card()
    os.system(r'pdflatex ./card.tex')
    os.system(r'rm -rf ./*.aux ./*.log ./*.tex')

if __name__=="__main__":
	main()
