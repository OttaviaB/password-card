# password-card

This program creates a password card. It is contained in a pdf file generated with LaTex.
Each column beyond the first one corresponds to a different service for which a password is needed. 
The user must remember only a single master password and can use it to retrieve
the password for each service: each letter of the master password in the first column corresponds to 
one symbol in the column of the desired service.

![Example of the generated pdf](https://github.com/OttaviaB/password-card/blob/main/card.pdf)


## class PassWordCard

Each card is created starting from a seed which can be specified. The number of services can be set 
freely as well. For each letter of the alphabet a set of n randomly chosen symbols is assigned, where
n is the number of services. 

The final result can be printed in the terminal with the method `print_card` or it can
be transformed in a pdf file with the method `export_card`. Note that pdflatex is needed to generate the 
pdf. 

Finally, the method `get_pass_word` takes the master password and the desired service as inputs and
gives the corresponding password as a result.
