def find_common_participants(g1, g2, sep=','):
    p1 = set(g1.split(sep))
    p2 = set(g2.split(sep))

    common = p1.intersection(p2)
    return list(common)


group1 = "Иванов|Петров|Сидоров"
group2 = "Петров|Сидоров|Смирнов"

# с разделителем '|'
common_participants = find_common_participants(group1, group2, sep='|')
print("Общие участники:", common_participants)

# с разделителем ','
group1_comma = "Иванов,Петров,Сидоров"
group2_comma = "Петров,Сидоров,Смирнов"
common_participants_comma = find_common_participants(group1_comma, group2_comma)
print("Общие участники (с запятой):", common_participants_comma)