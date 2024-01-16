from function import *

if __name__=='__main__':
    last_appdate_list = sort_data(is_exect(load_operations()))[:5]

    for data in last_appdate_list:
        print(form_modif(data))
