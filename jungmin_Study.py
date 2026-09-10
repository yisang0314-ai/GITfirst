def Get_NameHistory(Data_File, Name):
    if Name in Data_File:
        return Data_File[Name]

files = {"재우": "21", "재욱": "25", "정민": "27"}

input_name = input("이름을 입력하세요: ")

if input_name in files:
    print(f"{input_name}의 나이는 {Get_NameHistory(files, input_name)}세입니다.")

