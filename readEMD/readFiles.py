import re
import sys


def new_year(new_date, max_year, min_year):
    if new_date > max_year:
        max_year = new_date
    if new_date < min_year:
        min_year = new_date
    return max_year, min_year


def add_dic_dic(dic, first_key, second_key, result):
    if first_key not in dic.keys():
        dic[first_key] = {}
    if second_key not in dic[first_key].keys():
        dic[first_key][second_key] = []

    dic[first_key][second_key].append(result)


def add_dic(dic, first_key, result):
    if first_key not in dic.keys():
        dic[first_key] = []

    dic[first_key].append(result)


def read_emd(filename):
    f = open(filename, encoding="utf-8")
    f.readline()

    max_year = str(-sys.maxsize)
    min_year = str(sys.maxsize)

    dic_by_gender_year = {}
    dic_by_modality_year = {}
    dic_by_age_gender = {}
    dic_by_year_federated = {}
    dic_address = {}
    apto = 0.0
    total = 0.0

    # _id, index, dataEMD, nome / primeiro, nome / último, idade, género, morada, modalidade, clube, email, federado,

    pat = re.compile(r'^(?P<id>[^,]+),'
                     r'(?P<index>[^,]+),'
                     r'(?P<dateEMD>(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)),'
                     r'(?P<firstName>[^,]+),'
                     r'(?P<lastName>[^,]+),'
                     r'(?P<age>[^,]+),(?P<gender>[^,]+),'
                     r'(?P<address>[^,]+),'
                     r'(?P<modality>[^,]+),'
                     r'(?P<club>[^,]+),'
                     r'(?P<email>[^,]+),'
                     r'(?P<federated>[^,]+),'
                     r'(?P<result>[^,]+)\n$')

    for linha in f:
        h = pat.search(linha)
        if h:

            new_date = h.group('dateEMD')
            year = h.group('year')
            gender = h.group('gender')
            modality = h.group('modality')
            age = int(h.group('age'))
            federated = h.group('federated')
            result = h.group('result')
            address = h.group('address')
            r = (h.group('firstName'), modality)

            max_year, min_year = new_year(new_date, max_year, min_year)

            add_dic_dic(dic_by_gender_year, year, gender,r)
            add_dic_dic(dic_by_gender_year, 'total', gender,r)

            add_dic_dic(dic_by_modality_year, year, modality,r)
            add_dic_dic(dic_by_modality_year, 'total', modality,r)

            add_dic_dic(dic_by_year_federated, year, federated,r)

            add_dic(dic_address,address,result)

            if age >= 35:
                add_dic_dic(dic_by_age_gender, '>=35', gender,r)
            else:
                add_dic_dic(dic_by_age_gender, '<35', gender,r)

            if result.lower() == 'true':
                apto += 1
            total += 1

    apto_per = (apto/total) * 100
    return min_year, max_year, dic_by_gender_year, dic_by_modality_year, dic_by_age_gender, dic_by_year_federated, \
           apto_per, 100-apto_per, dic_address