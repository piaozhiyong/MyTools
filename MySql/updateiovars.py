# !/usr/bin/env python
# -*- coding: utf-8 -*-

n_uid = open("name+uid.txt", 'r')
iovars = open("updateiovars.txt", 'w')

lines = n_uid.readlines()
saddrs = 0
intvalue = 0
for line in lines:
    vname, uid = line.split(':')
    # 创建sql 语句
    # sql = "UPDATE proj20180727_new_version_proj_iovariable_modbus SET variable={0},variableid={1}" \
    #       " WHERE `startaddress`= {2};\n".format(vname, uid.strip(), saddrs)
    sql = "UPDATE proj20180727_new_version_proj_variable SET varvalueInit= {2}" \
          " WHERE varname ={0} AND varuuid ={1};\n".format(vname, uid.strip(), intvalue)
    iovars.write(sql)
    saddrs += 1
    intvalue += 1

n_uid.close()
iovars.close()
