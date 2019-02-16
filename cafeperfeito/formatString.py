import re


def formatTelefone(telefones):
    print('Telefones: [{}]'.format(telefones))
    listTel = []
    for tel in telefones:
        print('tel: [{}]'.format(tel))
        listTel.insert(re.sub(r'(\d)?(\d{4})(\d{4})', r'\1 \2-\3', tel))
    return listTel


def formatNcm(ncm):
    # listTel = []
    # for tel in telefones:
    #     print('tel: [{}]'.format(tel))
    return re.sub(r'(\d{2})(\d{3})(\d{2})', r'\1.\2.\3', ncm)

# else:
#     return re.sub(r'(\d)?(\d{4})(\d{4})', r'\1 \2-\3', telefones)
