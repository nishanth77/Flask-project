# n = 12
# # b = []* n
# logs = ['s2 success', 's11 error', 's8 error', 's4 error', 's8 error', 's5 error', 's7 error', 's3 error', 's3 error', 's1 error', 's10 error', 's12 error', 's9 error', 's10 error', 's3 error', 's11 error', 's3 error', 's7 error', 's5 error', 's9 error', 's9 error', 's1 success', 's2 error', 's8 error', 's1 error', 's7 error', 's8 error', 's4 error', 's3 error', 's8 error', 's10 error', 's10 error', 's9 error', 's3 error', 's11 error', 's12 error', 's3 error', 's7 error', 's6 error', 's2 error', 's3 error', 's6 error', 's6 error', 's9 error', 's2 error', 's1 error', 's7 error', 's3 error', 's8 error', 's12 error', 's6 error', 's4 error', 's7 error', 's10 error', 's8 error', 's9 success', 's11 success', 's10 error', 's6 error', 's3 error', 's10 error', 's6 success', 's1 error', 's8 error', 's5 error', 's3 error', 's6 error', 's4 error', 's12 success', 's10 success', 's2 success', 's9 success', 's4 success', 's8 error', 's2 error', 's3 error', 's4 error', 's9 error', 's12 success', 's11 success', 's11 error', 's11 error', 's3 error', 's3 error', 's6 error', 's11 error', 's10 error', 's3 error', 's3 error', 's6 error', 's5 error', 's4 error', 's3 error', 's1 error', 's12 error', 's3 error', 's6 success', 's4 error', 's6 error', 's6 error', 's5 error', 's10 error', 's11 success', 's5 error', 's7 success', 's2 success', 's8 error', 's2 error', 's7 error', 's6 error', 's10 error', 's5 success', 's2 error', 's3 error', 's6 success', 's7 error', 's10 error', 's2 error', 's9 error', 's9 error', 's12 error', 's11 error', 's5 error', 's1 error', 's12 error', 's5 error', 's9 error', 's3 error', 's8 success', 's7 error', 's3 error', 's5 error', 's12 success', 's3 error', 's5 success', 's7 success', 's10 error', 's2 error', 's10 error', 's10 success', 's2 error', 's12 error', 's9 error', 's7 error', 's6 success', 's12 error', 's6 error', 's8 error', 's7 error', 's5 error', 's2 error', 's5 error', 's9 error', 's9 error', 's10 success', 's4 success', 's6 error', 's9 success', 's3 error', 's12 error', 's7 success', 's2 error', 's6 error', 's12 error', 's3 success', 's1 error', 's12 success', 's9 success', 's2 success', 's2 error', 's6 error', 's3 error', 's3 error', 's12 error', 's5 error', 's7 error', 's12 success', 's2 error', 's3 error', 's6 success', 's1 error', 's10 error', 's7 error', 's6 error', 's12 error', 's4 error', 's8 error', 's11 error', 's9 error', 's11 error', 's9 error', 's6 error', 's6 error', 's2 error', 's9 error', 's1 error', 's4 success', 's4 error', 's8 error', 's8 error', 's11 error', 's4 error', 's10 error', 's5 error', 's5 error', 's8 error', 's2 success', 's3 error', 's6 success', 's9 error', 's8 error', 's9 error', 's12 error', 's11 error', 's1 error', 's4 error', 's8 success', 's5 error', 's7 error', 's3 error', 's2 error', 's10 error', 's9 error', 's5 success', 's3 error', 's4 error', 's5 success', 's3 error', 's10 error', 's4 error', 's12 error', 's12 error', 's5 error', 's6 error', 's8 error', 's7 error']
# temp_n = [0] * n
# # print(logs)
# for log in logs:
#     serverid = int(str(log[1])) -1
#     if "error" in log:
#         temp_n[serverid] += 1
#     elif "success" in log:
#         temp_n[serverid] = 0
# count = 0
# for num in temp_n:
#     if num >= 3:
#         count += 1 
# # return count
# print(len(logs))
# print(temp_n)
# # print(count)

# n = [1,2,3]
# b = [0]* len(n)
# print(b)

# string = "pcmbzpcmbzp"
# count_c = string.count('c')
# count_m = string.count('m')
# count_z = string.count('z')

# min_value = min(count_p, count_c, count_m, count_z)
# print(min_value)
# count_p = string.count('p')
# print(count_p)
vaultkey = "sdb://Azurevaultnov/Windows/Azurevaultnov"
vault_entity_name = vaultkey.split("/")[2]

print(vault_entity_name)
