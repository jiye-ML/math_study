"""
将目录的内容转化为思维导图，

将 10.00_00_aa.md
  10.00_01_bb.md
  10.00_02_cc.md


形式的目录结构转化为

10_aa --> 10.00_00.aa.md  --> 10.00_01_bb.md
                          --> 10.00_02_cc.md



"""

import xmind
import os


# 文件目录
file_name_list = dict()

file_dir = r'./'

# 遍历根目录
for _file in os.listdir(file_dir):

  # 非目录不遍历
  if not os.path.isdir(os.path.join(file_dir, _file)):
    continue

  # 只是遍历 如 10_xxx 形式的目录
  if not _file[0].isnumeric():
    continue

  _item_for_one_sub_topic = []
  for _item in os.listdir(os.path.join(file_dir, _file)):
    _item_for_one_sub_topic.append(_item)

  # {"03_字典和集合": [03.00_01_范隐射类型， ... ] }
  file_name_list[_file] = _item_for_one_sub_topic

# 思维导图
w = xmind.load("index.xmind")

# get the first sheet
s1 = w.getPrimarySheet()
s1.setTitle("index")

# get the root topic of this sheet
r1 = s1.getRootTopic()

# set its title
r1.setTitle('index')

for i, _key in enumerate(file_name_list.keys()):

  print(i, _key)

  # 10_aa
  _father_node = r1.addSubTopic()
  _father_node.setTitle(_key)

  # 10.00_00_aa.md
  _cur_father_node = None
  for i2, val2 in enumerate(file_name_list[_key]):

    # 越过文件夹
    if os.path.isdir(os.path.join(file_dir, val2)):
      continue

    # 文件 10.00_00_aa.md
    if '_00_' in val2:
      _cur_father_node = _father_node.addSubTopic()
      _cur_father_node.setTitle(val2)
      _cur_father_node.setFileHyperlink('{}/{}'.format(_key, val2))
    else:
      _child_node = _cur_father_node.addSubTopic()
      _child_node.setTitle(val2)
      _child_node.setFileHyperlink('{}/{}'.format(_key, val2))

xmind.save(w, "index.xmind")
