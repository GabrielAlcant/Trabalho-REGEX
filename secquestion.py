import re
def validarExpressao(lista, expressao, questao):
    regex = re.compile(expressao)
    for i in lista:
        verificador = regex.search(i)
        if verificador:
            print(f'{questao} válido: {verificador.group()}')
        else:
            print(f'{questao} inválido: {i}')
listsNomeSobrenomes = ['Ada Lovelace', 'Alan Turing', 'Stephen Cole Kleene',
                       '1Alan', 'Alan', 'A1an', 'A1an Turing', 'Alan turing']

expression_name = r'^[A-Z][a-z]+([A-Za-z]\s?)*[A-Z][a-z]+$'

validarExpressao(listsNomeSobrenomes, expression_name, 'Nome')
listEmails = ['jeancc.costa@gmail.com','a@a.br', 'divulga@ufpa.br', 'a@a.com.br',
              '@', 'a@.br', '@a.br', 'T@teste.br', 'a@A.com.br']
expressao_email = r'^([a-z0-9_.+-]+)@(([a-z])+(\.[a-z]{2,3})(\.[a-z]{1,2})?)$'

validarExpressao(listEmails, expressao_email, 'E-mail')
listSenhas = ['518R2r5e', 'F123456A', '1234567T', 'ropsSoq0', 'F1234567A', 'abcdefgH', '1234567HI']

expression_senha = r'^([0-9a-zA-Z])(?=.*[A-Z])(?=.*[0-9])[0-9a-zA-Z]{7}$'

validarExpressao(listSenhas, expression_senha, 'Senha')
listCPF = ['123.456.789-09','000.000.000-00', '123.456.789-0',
           '111.111.11.-11', '039.859.23.42']
expression_cpf = r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}'

validarExpressao(listCPF, expression_cpf, 'CPF')
listTelefones = ['(91) 99999-9999', '(91) 999999999', '91 999999999',
                 '(91) 59999-9999', '99 99999-9999', '(94)95555-5555']
expression_telefone = r'^(\([1-9]{2}\)\s)(9)([1-9]{4}-[0-9]{4})$'

validarExpressao(listTelefones, expression_telefone, 'Telefone')
list_dataHoras = ['31/08/2019 20:14:55', '99/99/9999 23:59:59', 
                  '99/99/9999 3:9:9', '9/9/99 99:99:99', '99/99/999903:09:09']
expression_dataHora = r'^([0-9]{2}/[0-9]{2}/[0-9]{4}) ([0-9]{2}:[0-9]{2}:[0-9]{2})$'

validarExpressao(list_dataHoras, expression_dataHora, 'Data e horário')
listNumeroReais = ['-25.467', '1', '-1', '+1', '64.2', '1.', '.2', '+64,2']
expression_numeroReais = r'^([+-]?[0-9]+(?:\.[0-9]+)?)$'

validarExpressao(listNumeroReais, expression_numeroReais, 'Números')
