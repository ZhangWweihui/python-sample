def read1(path):
    with open(path, 'r') as f1:
        lines = f1.readlines()
        set1 = set()
        for line in lines:
            line = line.rstrip('\n')
            uid = int(line)
            user_id = int(line[0:len(line)-1])
            if uid not in set1:
                sql = 'insert into t_beth_uid_country (f_user_id, f_uid, f_parent_user_id, f_parent_uid,'\
                      'f_reg_newest_country_name_cn, f_global_kyc_country, f_otc_kyc_country)'\
                      'values (%d, %d, %d, %d, \'%s\', \'%s\', \'%s\');' % (user_id, uid, user_id, uid, '新加坡', '新加坡', '新加坡')
                print(sql)
            set1.add(uid)
    print(set1)
    print(1641126817091+3600*24*1000*90)


if __name__ == '__main__':
    read1('/Users/zhangweihui/Desktop/xinjiapo.txt')
