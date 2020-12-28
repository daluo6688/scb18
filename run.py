from test.lesson07 import read_case,api_fun,write_result
def execute_fun(filename,sheetname):
    cases = read_case(filename,sheetname)  #调用函数，设置变量接收返回值
    for case in cases:
        case_id = case['case_id']  #获取用例编号
        url_case = case['url'] #获取URL的值
        data = eval(case['data'])  #字符串==字典
        expect = eval(case['expect']) #预期结果
        # print(case_id,expect)
        expect_msg = expect['msg']  #预期结果中的msg
        # print(expect_msg)
        real_result = api_fun(url=url_case,data=data)
        real_msg = real_result['msg']  #获取实际结果中的msg
        print('期望结果为：{}'.format(expect_msg))
        print('实际结果为：{}'.format(real_msg))
        # print(case_id,expect_msg,real_msg)
        if expect_msg==real_msg:
            print('{}用例执行通过！'.format(case_id))
            final_re = 'passed'
        else:
            print('{}用例执行不通过！'.format(case_id))
            final_re = 'Failed'
        write_result(filename,sheetname,case_id+1,8,final_re)
        print('*'*25)
#调用这个函数
execute_fun('D:\\pycharmProjects\scb188\\test_data\\test_case_api.xlsx', 'register')
execute_fun('D:\\pycharmProjects\scb188\\test_data\\test_case_api.xlsx', 'login')