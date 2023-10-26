import re

def test_sentence(pattern, sentence):
    if re.match(pattern, sentence):
        print(f'A sentença "{sentence}" é ACEITA.')
    else:
        print(f'A sentença "{sentence}" é RECUSADA.')

# a) Casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher.
pattern_a = r'^(M|H)+(h{1,2}m+)+$'
test_sentence(pattern_a, "MHHmm")  # Aceita
test_sentence(pattern_a, "MHhmmm")  # Aceita
test_sentence(pattern_a, "MHhmm")   # Aceita
test_sentence(pattern_a, "MHhm")    # Aceita
test_sentence(pattern_a, "H")       # Recusada

# b) Casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas mulheres.
pattern_b = r'^(M|H)+(hm)*M(hm)*$'
test_sentence(pattern_b, "MHM")      # Aceita
test_sentence(pattern_b, "MHMhm")    # Aceita
test_sentence(pattern_b, "MHHMhmm")  # Recusada

# c) Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho mais novo homem.
pattern_c = r'^(M|H)+hm*(M|h)*$'
test_sentence(pattern_c, "MHM")      # Recusada
test_sentence(pattern_c, "MHMhm")    # Recusada
test_sentence(pattern_c, "MHMh")     # Aceita

# d) Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os últimos também.
pattern_d = r'^(MM|HH)+(M|h){4,}$'
test_sentence(pattern_d, "MHHHMMMM")   # Aceita
test_sentence(pattern_d, "MMHMMMMM")   # Recusada
test_sentence(pattern_d, "MMHHHHMHHH")  # Aceita

# e) Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento.
pattern_e = r'^(MM|HH)+(Mh|Mm|hM|hH)+$'
test_sentence(pattern_e, "MMMH")         # Aceita
test_sentence(pattern_e, "MMMHMMMH")     # Recusada
test_sentence(pattern_e, "MMMHMhMhMh")   # Aceita

# f) Casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos homens e mulheres, mas que não tiveram dois filhos homens consecutivos.
pattern_f = r'^(MM|HH)+(M|h)*(M|h)*(M|h)*$'
test_sentence(pattern_f, "MMMH")       # Aceita
test_sentence(pattern_f, "MMMHMM")     # Aceita
test_sentence(pattern_f, "MMMHMMHMM")  # Recusada

# g) Arranjo de no mínimo x∈ℕ e no máximo y∈ℕ, com x>0, y>0, e x≤y, de adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos homens e mulheres, mas os três filhos mais novos não são homens.
pattern_g = r'^(M|H){x,y}+(M|h)*(M|h)*(M|h)+$'
test_sentence(pattern_g.replace("{x,y}", "{1,3}"), "MHHM")        # Recusada
test_sentence(pattern_g.replace("{x,y}", "{3,6}"), "MHHMhhhh")    # Recusada
test_sentence(pattern_g.replace("{x,y}", "{4,8}"), "MHMHMhhmm")  # Aceita
