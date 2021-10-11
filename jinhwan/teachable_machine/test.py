with open('jinhwan/teachable_machine/conference_file/labels.txt', 'r') as f:
    labels = f.readlines()
print(labels)
print(type(labels))

label_dict = {}
for label in labels:
    num = label.split(' ', maxsplit=1)[0].strip()
    value = label.split(' ', maxsplit=1)[1].strip()
    label_dict[num] = value

print(label_dict)
# 0 Class 1\n
# 1 Class 2

# label_dict = {0 : 'Class 1', 1 : "Class 2"}
# print(label_dict[0])