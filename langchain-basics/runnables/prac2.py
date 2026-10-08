class NakliPromptTemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self):
        return self.template.format()


abc = NakliPromptTemplate(4, 5)

abc.format()
