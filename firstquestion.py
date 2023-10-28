import re

def test_sentence(pattern, sentence):
    if re.match(pattern, sentence):
        print(f'A sentença "{sentence}" é ACEITA.')
    else:
        print(f'A sentença "{sentence}" é RECUSADA.')

# a) Casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher.
pattern_a = r'((HM|MH)*)((h|m)(h|m)(h|m)*)$'
test_sentence(pattern_a, "MHHmm")
test_sentence(pattern_a, "MHhmmm")  
test_sentence(pattern_a, "MHhmm")   
test_sentence(pattern_a, "MHhm")    
test_sentence(pattern_a, "H")     

# b) Casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas mulheres.
pattern_b = r'^((HM|MH)*)((h|m)*m{3})$'
test_sentence(pattern_b, "MHM")     
test_sentence(pattern_b, "MHMhm")    
test_sentence(pattern_b, "MHHMhmm")  

# c) Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho mais novo homem.
pattern_c = r'^(HM|MH)*mh$'
test_sentence(pattern_c, "MHM")     
test_sentence(pattern_c, "MHMhm")    
test_sentence(pattern_c, "MHMh")     

# d) Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os últimos também.
pattern_d = r'(MM|HH)+(mh|hm){2}(h|m)+(mh|hm)'
test_sentence(pattern_d, "MHHHMMMM")  
test_sentence(pattern_d, "MMHMMMMM")   
test_sentence(pattern_d, "MMHHHHMHHH")  

# e) Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento.
pattern_e = r'(MM|HH)((hm)+(m|)|(mh)+(h|))'
test_sentence(pattern_e, "MMMH")         
test_sentence(pattern_e, "MMMHMMMH")     
test_sentence(pattern_e, "MMMHMhMhMh")   

# f) Casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos homens e mulheres, mas que não tiveram dois filhos homens consecutivos.
pattern_f = r'^(HH|MM)((m|hm)+h)$'
test_sentence(pattern_f, "MMMH")     
test_sentence(pattern_f, "MMMHMM")     
test_sentence(pattern_f, "MMMHMMHMM") 

# g) Arranjo de no mínimo x∈ℕ e no máximo y∈ℕ, com x>0, y>0, e x≤y, de adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos homens e mulheres, mas os três filhos mais novos não são homens.
pattern_g = r'^(HH|MM)+'
test_sentence(pattern_g, "MHHM")        
test_sentence(pattern_g, "MHHMhhhh")
test_sentence(pattern_g, "MHMHMhhmm")
