import re

# Função para validar Nome, nome do meio e sobrenome
def validar_nome(texto):
    nome_regex = r'^[A-Z][a-z]*( [A-Z][a-z]*)?( [A-Z][a-z]*)?$'
    return bool(texto.match(nome_regex))

# Função para validar E-mail
def validar_email(texto):
    email_regex = r'^[^@]+@[^@]+\.(com\.br|br)$'
    return bool(texto.match(email_regex))

# Função para validar Senha
def validar_senha(texto):
    senha_regex = r'^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$'
    return bool(texto.match(senha_regex))

# Função para validar CPF
def validar_cpf(texto):
    cpf_regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return bool(texto.match(cpf_regex))

# Função para validar Telefone
def validar_telefone(texto):
    telefone_regex = r'^\(\d{2}\) 9\d{8}$|^\(\d{2}\) 9\d{4}-\d{4}$|\d{2} 9\d{8}$'
    return bool(texto.match(telefone_regex))

# Função para validar Data e horário
def validar_data_hora(texto):
    data_hora_regex = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$'
    return bool(texto.match(data_hora_regex))

# Função para validar Número real com ou sem sinal
def validar_numero_real(texto):
    numero_real_regex = r'^[+-]?\d+\.\d+|\d+$'
    return bool(texto.match(numero_real_regex))

# Exemplos de sentenças de teste
sentencas_nome = ["Ada Lovelace", "Alan Turing", "Stephen Cole Kleene", "1Alan", "Alan", "A1an", "A1an Turing", "Alan turing"]
sentencas_email = ["a@a.com.br", "divulga@ufpa.br", "a@a.br", "T@teste.br", "a@A.com.br", "@", "a@.br", "@a.br", "T@teste.br", "a@A.com.br"]
sentencas_senha = ["518R2r5e", "F123456A", "1234567T", "ropsSoq0", "F1234567A", "abcdefgH", "1234567HI"]
sentencas_cpf = ["123.456.789-09", "000.000.000-00", "123.456.789-0", "111.111.11-11"]
sentencas_telefone = ["(91) 99999-9999", "(91) 999999999", "91 999999999", "(91) 59999-9999", "99 99999-9999", "(94)95555-5555"]
sentencas_data_hora = ["31/08/2019 20:14:55", "99/99/9999 23:59:59", "99/99/9999 3:9:9", "9/9/99 99:99:99", "99/99/999903:09:09"]
sentencas_numero_real = ["-25.467", "1", "-1", "+1", "64.2", "1.", ".2", "+64,2"]

# Testando as sentenças de teste
nome_pattern = re.compile(r'^[A-Z][a-z]*( [A-Z][a-z]*)?( [A-Z][a-z]*)?$')
print("Validação de Nomes:")
for sentenca in sentencas_nome:
    print(f"{sentenca}: {validar_nome(nome_pattern, sentenca)}")

email_pattern = re.compile(r'^[^@]+@[^@]+\.(com\.br|br)$')
print("\nValidação de E-mails:")
for sentenca in sentencas_email:
    print(f"{sentenca}: {validar_email(email_pattern, sentenca)}")

senha_pattern = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$')
print("\nValidação de Senhas:")
for sentenca in sentencas_senha:
    print(f"{sentenca}: {validar_senha(senha_pattern, sentenca)}")

cpf_pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
print("\nValidação de CPFs:")
for sentenca in sentencas_cpf:
    print(f"{sentenca}: {validar_cpf(cpf_pattern, sentenca)}")

telefone_pattern = re.compile(r'^\(\d{2}\) 9\d{8}$|^\(\d{2}\) 9\d{4}-\d{4}$|\d{2} 9\d{8}$')
print("\nValidação de Telefones:")
for sentenca in sentencas_telefone:
    print(f"{sentenca}: {validar_telefone(telefone_pattern, sentenca)}")

data_hora_pattern = re.compile(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$')
print("\nValidação de Datas e Horários:")
for sentenca in sentencas_data_hora:
    print(f"{sentenca}: {validar_data_hora(data_hora_pattern, sentenca)}")

numero_real_pattern = re.compile(r'^[+-]?\d+\.\d+|\d+$')
print("\nValidação de Números Reais:")
for sentenca in sentencas_numero_real:
    print(f"{sentenca}: {validar_numero_real(numero_real_pattern, sentenca)}")
