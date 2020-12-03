# password-card

This program creates a password card as a pdf file generated with pdflatex.
Each column beyond the first one corresponds to a different service for which a password is needed. 
The user must remember only a single master password and can use it to retrieve
the password for each service: each letter of the master password in the first column corresponds to 
one symbol in the column of the desired service.

![Example of the generated pdf](https://github.com/OttaviaB/password-card/blob/main/card.pdf)


## class PassWordCard

Each card is created from a user selectable seed. Any number n of services can be set by the user:
for each letter of the alphabet a set of n randomly chosen symbols will be assigned.

The final result can be dumped to the standard output (`print_card
method`) or to a pdf file (`export_card method`).

Finally, the method `get_pass_word` takes the master password and the desired service as inputs and gives the corresponding password as a result.
