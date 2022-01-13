import pandas as pd
import re


def data_format(_data):  # 数据格式化
    _data = re.sub(r'\b(.*?)s\b', r'\1', _data, flags=re.I)
    _data = re.sub(r'\bAgr\b', 'Agricultural', _data, flags=re.I)
    _data = re.sub(r'\bAcad\b', 'Academy', _data, flags=re.I)
    _data = re.sub(r'\bAnim\b', 'Animal', _data, flags=re.I)
    _data = re.sub(r'\bAppl\b', 'Applied', _data, flags=re.I)
    _data = re.sub(r'\bAvit\b', 'Aviation', _data, flags=re.I)
    _data = re.sub(r'\bAeron\b', 'Aeronautical', _data, flags=re.I)
    _data = re.sub(r'\bAviat\b', 'Aviation', _data, flags=re.I)
    _data = re.sub(r'\bAerosp\b', 'Aerospace', _data, flags=re.I)
    _data = re.sub(r'\bAutomot\b', 'Automotive', _data, flags=re.I)
    _data = re.sub(r'\bAeronaut\b', 'Aeronautical', _data, flags=re.I)
    _data = re.sub(r'\bAeronautic\b', 'Aeronautical', _data, flags=re.I)
    _data = re.sub(r'\bAgriculture\b', 'Agricultural', _data, flags=re.I)
    _data = re.sub(r'\bBusines\b', 'Business', _data, flags=re.I)
    _data = re.sub(r'\bcent\b', 'central', _data, flags=re.I)
    _data = re.sub(r'\bChem\b', 'Chemical', _data, flags=re.I)
    _data = re.sub(r'\bColl\b', 'College', _data, flags=re.I)
    _data = re.sub(r'\bCreat\b', 'Creation', _data, flags=re.I)
    _data = re.sub(r'\bCommun\b', 'Communication', _data, flags=re.I)
    _data = re.sub(r'\bConstruct\b', 'Construction', _data, flags=re.I)
    _data = re.sub(r'\bDef\b', 'Defense', _data, flags=re.I)
    _data = re.sub(r'\bEng\b', 'Engineering', _data, flags=re.I)
    _data = re.sub(r'\bEcol\b', 'Ecological', _data, flags=re.I)
    _data = re.sub(r'\bEcon\b', 'Economic', _data, flags=re.I)
    _data = re.sub(r'\bEduc\b', 'Education', _data, flags=re.I)
    _data = re.sub(r'\bEngn\b', 'Engineering', _data, flags=re.I)
    _data = re.sub(r'\bElect\b', 'Electronic', _data, flags=re.I)
    _data = re.sub(r'\bEcology\b', 'Ecological', _data, flags=re.I)
    _data = re.sub(r'\bEconomy\b', 'Economic', _data, flags=re.I)
    _data = re.sub(r'\bElectric\b', 'Electronic', _data, flags=re.I)
    _data = re.sub(r'\bEnvironm\b', 'Environmental', _data, flags=re.I)
    _data = re.sub(r'\bElectrical\b', 'Electronic', _data, flags=re.I)
    _data = re.sub(r'\bfor\b', '', _data, flags=re.I)
    _data = re.sub(r'\bFinance\b', 'Financial', _data, flags=re.I)
    _data = re.sub(r'\bGeol\b', 'Geology', _data, flags=re.I)
    _data = re.sub(r'\bGeosci\b', 'Geoscience', _data, flags=re.I)
    _data = re.sub(r'\bhyg\b', 'hygienic', _data, flags=re.I)
    _data = re.sub(r'\bHlth\b', 'Health', _data, flags=re.I)
    _data = re.sub(r'\bHusb\b', 'Husbandry', _data, flags=re.I)
    _data = re.sub(r'\bInd\b', 'Industrial', _data, flags=re.I)
    _data = re.sub(r'\bInt\b', 'International', _data, flags=re.I)
    _data = re.sub(r'\bInst\b', 'Institute', _data, flags=re.I)
    _data = re.sub(r'\bInvest\b', 'Investigation', _data, flags=re.I)
    _data = re.sub(r'\bIndustry\b', 'Industrial', _data, flags=re.I)
    _data = re.sub(r'\bInformat\b', 'Information', _data, flags=re.I)
    _data = re.sub(r'\bLogist\b', 'Logistic', _data, flags=re.I)
    _data = re.sub(r'\bMed\b', 'Medical', _data, flags=re.I)
    _data = re.sub(r'\bMil\b', 'Military', _data, flags=re.I)
    _data = re.sub(r'\bMin\b', 'Mining', _data, flags=re.I)
    _data = re.sub(r'\bMet\b', 'Metallurgy', _data, flags=re.I)
    _data = re.sub(r'\bMech\b', 'Mechanical', _data, flags=re.I)
    _data = re.sub(r'\bMineral\b', 'Mineralogy', _data, flags=re.I)
    _data = re.sub(r'\bMedicine\b', 'Medical', _data, flags=re.I)
    _data = re.sub(r'\bMongolian\b', 'Mongolia', _data, flags=re.I)
    _data = re.sub(r'\bNatl\b', 'Nationality', _data, flags=re.I)
    _data = re.sub(r'\bNorma\b', 'Normal', _data, flags=re.I)
    _data = re.sub(r'\bNational\b', 'Nationality', _data, flags=re.I)
    _data = re.sub(r'\bof\b', '', _data, flags=re.I)
    _data = re.sub(r'\bPetr\b', 'Petroleum', _data, flags=re.I)
    _data = re.sub(r'\bProv\b', 'Provincial', _data, flags=re.I)
    _data = re.sub(r'\bPubl\b', 'Public', _data, flags=re.I)
    _data = re.sub(r'\bPekin\b', 'Peking', _data, flags=re.I)
    _data = re.sub(r'\bPolit\b', 'Political', _data, flags=re.I)
    _data = re.sub(r'\bPresch\b', 'Preschool', _data, flags=re.I)
    _data = re.sub(r'\bPolytech\b', 'Polytechnic', _data, flags=re.I)
    _data = re.sub(r'\bPetrochem\b', 'Petrochemical', _data, flags=re.I)
    _data = re.sub(r'\bPharmaceut\b', 'pharmaceutical', _data, flags=re.I)
    _data = re.sub(r'\bRelat\b', 'Relation', _data, flags=re.I)
    _data = re.sub(r'\bSci\b', 'Science', _data, flags=re.I)
    _data = re.sub(r'\bServ\b', 'Service', _data, flags=re.I)
    _data = re.sub(r'\bSyst\b', 'systemic', _data, flags=re.I)
    _data = re.sub(r'\bSecur\b', 'Security', _data, flags=re.I)
    _data = re.sub(r'\bShannxi\b', 'Shaanxi', _data, flags=re.I)
    _data = re.sub(r'\bThe\b', '', _data, flags=re.I)
    _data = re.sub(r'\bTech\b', 'Technology', _data, flags=re.I)
    _data = re.sub(r'\bText\b', 'Textile', _data, flags=re.I)
    _data = re.sub(r'\bTrop\b', 'Tropical', _data, flags=re.I)
    _data = re.sub(r'\bTaxat\b', 'Taxation', _data, flags=re.I)
    _data = re.sub(r'\bTradit\b', 'Traditional', _data, flags=re.I)
    _data = re.sub(r'\bTechnol\b', 'Technology', _data, flags=re.I)
    _data = re.sub(r'\bTechnical\b', 'Technology', _data, flags=re.I)
    _data = re.sub(r'\bTelecommun\b', 'Telecommunication', _data, flags=re.I)
    _data = re.sub(r'\bTransportat\b', 'Transportation', _data, flags=re.I)
    _data = re.sub(r'\bTechnological\b', 'Technology', _data, flags=re.I)
    _data = re.sub(r'\bUniv\b', 'University', _data, flags=re.I)
    _data = re.sub(r'\bVet\b', 'Veterinary', _data, flags=re.I)
    _data = re.sub(r'\bVoc\b', 'Vocational', _data, flags=re.I)
    _data = re.sub(r'\bVocat\b', 'Vocational', _data, flags=re.I)
    _data = re.sub(r'\bVocation\b', 'Vocational', _data, flags=re.I)
    _data = re.sub(r'\'', '', _data)
    _data = re.sub(r' *, *', '', _data)
    _data = re.sub(r' *， *', '', _data)
    _data = re.sub(r' *\( *', '', _data)
    _data = re.sub(r' *\) *', '', _data)
    _data = re.sub(r' *（ *', '', _data)
    _data = re.sub(r' *） *', '', _data)
    _data = re.sub(r' *< *', '', _data)
    _data = re.sub(r' *> *', '', _data)
    _data = re.sub(r' *& *', ' and ', _data)
    _data = re.sub(r' *’ *', '', _data)
    _data = re.sub(r' ', '', _data)
    _data = re.sub(r'-', '', _data)
    return _data


def run():
    data = pd.read_excel('测试2.xlsx')  # 原始表
    data = data.fillna('')
    comparison_table = pd.read_excel('全国高等学校中英文对应表.xlsx')  # 对照表（词库）
    comparison_table = comparison_table.fillna('')
    row1 = data.shape[0]
    row2 = comparison_table.shape[0]
    for i in range(row1):
        # if data.iloc[i, 9]:
        #     continue
        basic_data = data.iloc[i, 1]
        basic_data = data_format(basic_data)
        basic_e = ''
        for j in range(row2):
            target_data = comparison_table.iloc[j, 2]
            if not target_data:  # 跳过空数据
                continue
            target_data = data_format(target_data)
            if len(target_data) > 6:
                if bool(re.search(target_data, basic_data, re.IGNORECASE)):
                    if len(target_data) > len(basic_e):
                        basic_e = target_data
                        data.iloc[i, 3] = comparison_table.iloc[j, 1].strip()
                    elif len(target_data) == len(basic_e) and comparison_table.iloc[j, 1] not in data.iloc[i, 3]:
                        data.iloc[i, 3] += '/' + comparison_table.iloc[j, 1]
            else:
                if bool(re.search(target_data, basic_data)):
                    if len(target_data) > len(basic_e):
                        basic_e = target_data
                        data.iloc[i, 3] = comparison_table.iloc[j, 1].strip()
        print(f'进度:{i + 1}/{data.shape[0]}')
    data.to_excel('检测2.xlsx', index=False)  # 输出表名


def test(basic_data):
    basic_data = basic_data
    basic_data = data_format(basic_data)
    print(basic_data)
    basic_e = ''
    comparison_table = pd.read_excel('全国高等学校中英文对应表.xlsx')  # 对照表（词库）
    row2 = comparison_table.shape[0]
    out = ''
    for j in range(row2):
        target_data = comparison_table.iloc[j, 2]
        if not target_data:  # 跳过空数据
            continue
        target_data = data_format(target_data)
        if len(target_data) > 6:
            if bool(re.search(target_data, basic_data, re.IGNORECASE)):
                if len(target_data) > len(basic_e):
                    basic_e = target_data
                    out = comparison_table.iloc[j, 1].strip()
                elif len(target_data) == len(basic_e) and comparison_table.iloc[j, 1] not in out:
                    out += '/' + comparison_table.iloc[j, 1]
        else:
            if bool(re.search(target_data, basic_data)):
                if len(target_data) > len(basic_e):
                    basic_e = target_data
                    out = comparison_table.iloc[j, 1].strip()
    print(f'out:{out}')


if __name__ == "__main__":
    run()
# print(bool(re.search("University of Chinese Academy of Sciences", "basic_data", flags=re.I)))
