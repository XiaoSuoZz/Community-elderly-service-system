import random
import json

# 社区数组
community_arr = [
  '正阳馨居', '龙泽雅苑', '北新花园', '怡静园', '福源学苑', '东苑小区', '金府花园', '宏运铂郡', '恒强小区', '龙畔家园', '宁泽园', '常青小区', '东芳家园', '利民小区', '亨通花园', '金色家园', '嘉科花园', '东方龙城', '和美家园', '惠畅家园', '阳光水岸'
]
community_num = len(community_arr) - 1
# 常见疾病史
diseases_history_arr = [
  "大叶性肺炎", "克雷伯杆菌肺炎", "支原体肺炎", "支气管肺炎", "金色葡萄球菌肺炎", 
  "肺结核", "结核性胸膜炎", "结核性心包炎", "肠结核", "结核性腹膜炎", "肾结核", 
  "支气管扩张", "肺脓肿", "肺癌", "肺心病", "支气管哮喘", "呼吸衰竭", "张力性气胸", 
  "血胸", "肋骨骨折", "冠心病", "心绞痛", "心梗", "左心衰", "右心衰", "房颤", "阵发性室上性心动过速", 
  "阵发性室性心动过速", "二尖瓣狭窄", "二尖瓣关闭不全", "主动脉瓣狭窄", "主动脉瓣关闭不全", "失血性休克", 
  "心源性休克", "肾小球肾炎", "尿路感染", "肾盂肾炎", "慢性肾盂肾炎急性发作", "下尿路感染", "肾结石", "输尿管结石", 
  "肾癌", "肾衰", "前列腺增生", "白血病", "再生障碍性贫血", "自身免疫性溶血性贫血", "缺铁性贫血", "特发性血小板减少紫癜", 
  "脑出血", "脑血栓", "脑栓塞", "肺栓塞", "蛛网膜下腔出血", "脑梗死", "结脑", "病脑", "化脑", "流脑", "乙脑", "脑震荡", 
  "急性硬膜外血肿", "硬膜下血肿", "脑疝", "甲肝", "乙肝", "丙肝", "艾滋病", "异位妊娠", "卵巢肿瘤蒂扭转", "急性盆腔炎", 
  "宫颈癌", "卵巢肿瘤", "子宫肌瘤", "轮转病毒肠炎", "麻疹", "风疹", "急疹", "风疹", "猩红热", "佝偻病", "肱骨外科颈骨折", 
  "肱骨干骨折", "肱骨髁上骨折", "桡骨远端骨折", "桡骨头半脱位", "髋关节后脱位", "肩关节前脱位", "股骨颈骨折",
  "软组织急性化脓性感染", "痈", "皮下急性蜂窝织炎", "丹毒", "急性淋巴管炎"
]
diseases_history_num = len(diseases_history_arr) - 1
# 常见重大疾病史
major_diseases_history_arr = [
  "恶性肿瘤", "急性心肌梗塞", "脑中风后遗症", "重大器官移植术或造血干细胞移植术", 
  "冠状动脉搭桥术", "慢性肾功能衰竭尿毒症期", "肢体缺失", "急性或亚急性重症肝炎", 
  "良性脑肿瘤", "慢性肝功能衰竭失代偿期", "脑炎后遗症或脑膜炎后遗症", "深度昏迷", 
  "双耳失聪", "双目失明", "瘫痪", "心脏瓣膜手术", "严重阿尔茨海默病", "严重脑损伤", 
  "严重帕金森病", "严重Ⅲ度烧伤", "严重原发性肺动脉高压", "严重运动神经元病", "语言能力丧失",
  "重型再生障碍性贫血", "主动脉手术", "严重的多发性硬化", "严重的1型糖尿病", "侵蚀性葡萄胎(或称恶性葡萄胎)", "系统性红斑狼疮并发重度的肾功能损害"
]
major_diseases_history_num = len(major_diseases_history_arr) - 1

# 常见姓氏
first_name_arr = [
  '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', 
  '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', 
  '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', 
  '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', 
  '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', 
  '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', 
  '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', 
  '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', 
  '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', 
  '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', 
  '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', 
  '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', 
  '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', 
  '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', 
  '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', 
  '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', 
  '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆', '高', 
  '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', 
  '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', 
  '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', 
  '郁', '单', '杭', '洪', '包', '诸', '左', '石' ]
first_name_num = len(first_name_arr) - 1
# 常用名女
second_name_arr = [
  [ 
    '才', '仁', '铨', '境', '寿', '绪', '硕', '冲', '宗', '臣', '屹', '伍', '翱', '羲', '锴', '骥', '镔', '钧', '创', '捷', '盛', '璈', '钢', '锐', '锋', 
    '剑', '逵', '宥', '庥', '勇', '奎', '世', '仕', '生', '疆', '镜', '选', '钊', '城', '刚', '峻', '伟', '崇', '堂', '得', '祥', '基', '山', '忍', '嵩', 
    '钜', '轼', '奥', '铎', '骢', '随', '鑫', '瓒', '心', '四', '尹', '少', '升', '铭', '玮', '瑜', '诵', '齐', '僖', '瑞', '睿', '韶', '诚', '瑀', '逍', 
    '祎', '维', '艾', '坤', '于', '玙', '昇', '亚', '尚', '承', '咏', '青', '昌', '金', '州', '舟', '先', '安', '如', '亦', '宇', '羽', '丞', '守', '存', 
    '再', '任', '有', '镕', '璨', '瑷', '环', '储', '双', '翼', '璧', '铠', '阳', '聪', '远', '应', '忆', '谡', '赛', '骏', '声', '懿', '勋', '超', '朝', 
    '画', '善', '喆', '琇', '越', '翔', '羡', '钦', '岚', '然', '舒', '童', '竣', '绚', '顺', '舜', '胜', '惟', '斯', '锦', '融', '铮', '璁', '儒', '谌', 
    '衡', '璀', '静', '阊', '缜', '纬', '赐', '卫', '亿', '阅', '奭', '峤', '逸', '施', '信', '星', '威', '玥', '垚', '帅', '禹', '宣', '春', '度', '前', 
    '音', '为', '昶', '秋', '思', '人', '以', '正', '永', '赞', '链', '容', '师', '晁', '修', '宸', '素', '益', '恩', '宬', '乘', '书', '轩', '珅', '玹', 
    '宗璈', '宗羲', '宗锴', '翱臣', '勇钢', '宥锐', '宥逵', '勇逵', '镜屹', '宥羲', '宥锴', '镜生', '选仕', '宥臣', '宥屹', '勇臣', '勇屹', '伟硕', '崇硕', 
    '堂境', '堂硕', '得硕', '宥硕', '勇硕', '宗臣', '选锐', '宥仁', '镜仁', '宗锐', '宗世', '宗生', '钊锐', '城锐', '城逵', '峻锐', '峻锋', '伟仁', '崇才', 
    '崇仁', '得仁', '祥仁', '崇仕', '崇锐', '祥锐', '峻臣', '峻屹', '镜锴', '宗硕', '城生', '峻生', '宥镔', '创臣', '捷臣', '镜捷', '选钧', '宗仁', '冲璈', 
    '冲钢', '宗钢', '冲羲', '冲锴', '翱屹', '翱伍', '宥璈', '宥钢', '庥璈', '庥钢', '勇璈', '奎璈', '奎钢', '宥锋', '宥剑', '庥锐', '庥锋', '庥剑', '庥逵', 
    '勇锐', '勇锋', '勇剑', '奎锐', '奎锋', '奎剑', '奎逵', '翱忍', '疆臣', '疆屹', '疆伍', '镜臣', '镜伍', '选臣', '选屹', '选伍', '庥羲', '庥锴', '勇羲', 
    '勇锴', '奎羲', '奎锴', '疆世', '疆仕', '疆生', '镜世', '镜仕', '选世', '选生', '翱璈', '翱钢', '冲钊', '冲城', '冲刚', '冲峻', '宗钊', '宗城', '宗刚', 
    '宗峻', '宥忍', '庥忍', '勇忍', '奎忍', '冲骥', '宗骥', '冲忍', '宗忍', '宥伍', '庥臣', '庥屹', '庥伍', '勇伍', '奎臣', '奎屹', '奎伍', '疆忍', '镜忍', 
    '选忍', '伟铨', '伟境', '伟寿', '伟绪', '崇铨', '崇境', '崇寿', '崇绪', '堂铨', '堂寿', '堂绪', '得铨', '得境', '得寿', '得绪', '祥铨', '祥境', '祥寿', 
    '祥绪', '祥硕', '基铨', '基境', '基寿', '基绪', '基硕', '宥铨', '宥境', '宥寿', '宥绪', '庥铨', '庥境', '庥寿', '庥绪', '庥硕', '勇铨', '勇境', '勇寿', 
    '勇绪', '奎铨', '奎境', '奎寿', '奎绪', '奎硕', '冲臣', '冲屹', '冲伍', '宗屹', '宗伍', '疆锐', '疆锋', '疆剑', '疆逵', '镜锐', '镜锋', '镜剑', '镜逵', 
    '选锋', '选剑', '选逵', '宥才', '庥才', '庥仁', '勇才', '勇仁', '奎才', '奎仁', '疆才', '疆仁', '镜才', '选才', '选仁', '冲锐', '冲锋', '冲剑', '冲逵', 
    '宗锋', '宗剑', '宗逵', '翱羲', '翱锴', '疆骥', '镜骥', '选骥', '冲翱', '宗翱', '疆铨', '疆境', '疆寿', '疆绪', '疆硕', '镜铨', '镜境', '镜寿', '镜绪', 
    '镜硕', '选铨', '选境', '选寿', '选绪', '选硕', '冲世', '冲仕', '冲生', '宗仕', '翱铨', '翱境', '翱寿', '翱绪', '翱硕', '翱世', '翱仕', '翱生', '疆璈', 
    '疆钢', '镜璈', '镜钢', '选璈', '选钢', '翱锐', '翱锋', '翱剑', '翱逵', '宥世', '宥仕', '宥生', '庥世', '庥仕', '庥生', '勇世', '勇仕', '勇生', '奎世', 
    '奎仕', '奎生', '宥骥', '庥骥', '勇骥', '奎骥', '冲冲', '冲宗', '宗冲', '宗宗', '钊锋', '钊剑', '钊逵', '城锋', '城剑', '刚锐', '刚锋', '刚剑', '刚逵', 
    '峻剑', '峻逵', '伟才', '堂才', '堂仁', '得才', '祥才', '基才', '基仁', '翱骥', '冲宥', '冲庥', '冲勇', '冲奎', '宗宥', '宗庥', '宗勇', '宗奎', '伟世', 
    '伟仕', '伟生', '崇世', '崇生', '堂世', '堂仕', '堂生', '得世', '得仕', '得生', '祥世', '祥仕', '祥生', '基世', '基仕', '基生', '伟锐', '伟锋', '伟剑', 
    '伟逵', '崇锋', '崇剑', '崇逵', '堂锐', '堂锋', '堂剑', '堂逵', '得锐', '得锋', '得剑', '得逵', '祥锋', '祥剑', '祥逵', '基锐', '基锋', '基剑', '基逵', 
    '翱冲', '翱宗', '翱钊', '翱城', '翱刚', '翱峻', '钊臣', '钊屹', '钊伍', '城臣', '城屹', '城伍', '刚臣', '刚屹', '刚伍', '峻伍', '钊璈', '钊钢', '城璈', 
    '城钢', '刚璈', '刚钢', '峻璈', '峻钢', '疆镔', '镜镔', '选镔', '骥锐', '骥锋', '骥剑', '骥逵', '宥宥', '宥庥', '宥勇', '宥奎', '庥宥', '庥庥', '庥勇', 
    '庥奎', '勇宥', '勇庥', '勇勇', '勇奎', '奎宥', '奎庥', '奎勇', '奎奎', '疆羲', '疆锴', '镜羲', '选羲', '选锴', '铎才', '铎仁', '骢才', '骢仁', '随才', 
    '随仁', '宥冲', '宥宗', '庥冲', '庥宗', '勇冲', '勇宗', '奎冲', '奎宗', '冲铨', '冲境', '冲寿', '冲绪', '冲硕', '宗铨', '宗境', '宗寿', '宗绪', '钊世', 
    '钊仕', '钊生', '城世', '城仕', '刚世', '刚仕', '刚生', '峻世', '峻仕', '庥镔', '勇镔', '奎镔', '羲锐', '羲锋', '羲剑', '羲逵', '锴锐', '锴锋', '锴剑', 
    '锴逵', '钧臣', '钧屹', '钧伍', '创屹', '创伍', '捷屹', '捷伍', '盛臣', '盛屹', '盛伍', '臣钊', '臣城', '臣刚', '臣峻', '屹钊', '屹城', '屹刚', '屹峻', 
    '伍钊', '伍城', '伍刚', '伍峻', '翱才', '翱仁', '冲山', '宗山', '疆钧', '疆创', '疆捷', '疆盛', '镜钧', '镜创', '镜盛', '选创', '选捷', '选盛', '骥臣', 
    '骥屹', '骥伍', '臣世', '臣仕', '臣生', '屹世', '屹仕', '屹生', '伍世', '伍仕', '伍生', '冲才', '冲仁', '宗才', '羲铨', '羲境', '羲寿', '羲绪', '羲硕', 
    '锴铨', '锴境', '锴寿', '锴绪', '锴硕', '镔璈' ],
  [ 
    '艳',  '瑛',  '翠',  '慈',  '姗',  '宛',  '依',  '伊',  '璎',  '惜',  '情',  '嵋',  '燕',  '缘',  '娴',  '靓',  '影',  '婵',  '柔',  '姿',  '姝',  '怡',
    '嬿',  '倩',  '珊',  '纾',  '彩',  '珠',  '娅',  '婉',  '馨',  '园',  '圆',  '诗',  '韵',  '钰',  '琬',  '鑫',  '心',  '宛燕',  '依燕',  '姝燕',  '怡燕',  
    '柔影',  '柔婵',  '姿娴',  '姿影',  '姿婵',  '姝缘',  '姝娴',  '姝靓',  '姝影',  '姝婵',  '怡娴',  '怡靓',  '怡影',  '嬿伊',  '姗倩',  '姗珊',  '宛倩',  
    '依倩',  '依珊',  '柔伊',  '姿伊',  '姝伊',  '怡伊',  '彩瑛',  '彩慈',  '娅瑛',  '婉瑛',  '婉嫣',  '婉慈',  '柔慈',  '姿瑛',  '姿嫣',  '姝嫣',  '姝慈',  
    '怡嫣',  '怡慈',  '宛伊',  '依伊',  '姗娴',  '宛娴',  '依娴',  '嬿慈',  '宛艳',  '姗姗',  '宛宛',  '宛依',  '依姗',  '依依',  '倩娴',  '倩影',  '倩婵',  
    '珊娴',  '珊影',  '纾娴',  '纾靓',  '纾影',  '纾婵',  '宛柔',  '宛怡',  '彩缘',  '娅娴',  '娅影',  '婉娴',  '倩伊',  '珊伊',  '纾伊',  '倩燕',  '娅艳',  
    '柔柔',  '姿姿',  '姝姝',  '柔依',  '怡姗',  '姗慈',  '宛嫣',  '宛慈',  '依慈',  '伊倩',  '馨伊',  '馨缘',  '馨娴',  '馨靓',  '馨影',  '馨婵',  '柔惜',  
    '柔嵋',  '怡惜',  '怡嵋',  '倩瑛',  '倩嫣',  '纾瑛',  '纾嫣',  '纾慈',  '彩伊',  '娅伊',  '婉伊',  '惜惜',  '柔诗',  '姝圆',  '惜翠',  '惜嫣',  '惜慈',  
    '瑛倩',  '姃燕',  '姗燕',  '柔燕',  '姿燕',  '柔缘',  '柔娴',  '柔靓',  '姿缘',  '姿靓',  '怡缘',  '怡婵',  '姃倩',  '姃珊',  '姃纾',  '姗纾',  '宛珊',  
    '宛纾',  '依纾',  '彩翠',  '彩嫣',  '珠瑛',  '珠翠',  '珠嫣',  '珠慈',  '娅翠',  '娅嫣',  '娅慈',  '婉翠',  '柔瑛',  '柔翠',  '柔嫣',  '姿翠',  '姿慈',  
    '姝瑛',  '姝翠',  '怡瑛',  '怡翠',  '姃伊',  '姗伊',  '嬿缘',  '嬿娴',  '嬿靓',  '嬿影',  '嬿婵',  '柔艳',  '姿艳',  '姝艳',  '怡艳',  '姃缘',  '姃娴',  
    '姃靓',  '姃影',  '姃婵',  '姗缘',  '姗靓',  '姗影',  '姗婵',  '宛缘',  '宛靓',  '宛影',  '宛婵',  '依缘',  '依靓',  '依影',  '依婵',  '嬿瑛',  '嬿翠',  
    '嬿嫣',  '姃艳',  '姗艳',  '依艳',  '嬿燕',  '姃馨',  '姗馨',  '宛馨',  '依馨',  '姃姃',  '姃姗',  '姃宛',  '姃依',  '姗姃',  '姗宛',  '姗依',  '宛姃',  
    '宛姗',  '依姃',  '依宛',  '倩缘',  '倩靓',  '珊缘',  '珊靓',  '珊婵',  '纾缘',  '姃柔',  '姃姿',  '姃姝',  '姃怡',  '姗柔',  '姗姿',  '姗姝',  '姗怡',  
    '宛姿',  '宛姝',  '依柔',  '依姿',  '依姝',  '依怡',  '彩娴',  '彩靓',  '彩影',  '彩婵',  '珠缘',  '珠娴',  '珠靓',  '珠影',  '珠婵',  '娅缘',  '娅靓',  
    '娅婵',  '婉缘',  '婉靓',  '婉影',  '婉婵',  '珊燕',  '纾燕',  '嬿璎',  '彩艳',  '珠艳',  '婉艳',  '柔姿',  '柔姝',  '柔怡',  '姿柔',  '姿姝',  '姿怡',  
    '姝柔',  '姝姿',  '姝怡',  '怡柔',  '怡姿',  '怡姝',  '怡怡',  '嬿艳',  '柔姃',  '柔姗',  '柔宛',  '姿姃',  '姿姗',  '姿宛',  '姿依',  '姝姃',  '姝姗',  
    '姝宛',  '姝依',  '怡姃',  '怡宛',  '怡依',  '姃瑛',  '姃翠',  '姃嫣',  '姃慈',  '姗瑛',  '姗翠',  '姗嫣',  '宛瑛',  '宛翠',  '依瑛',  '依翠',  '依嫣',  
    '伊馨',  '柔璎',  '姿璎',  '姝璎',  '怡璎',  '惜伊',  '情伊',  '嵋伊',  '伊珊',  '伊纾',  '嬿惜',  '嬿情',  '嬿嵋',  '璎燕',  '燕倩',  '燕珊',  '燕纾',  
    '瑛惜',  '瑛情',  '瑛嵋',  '翠惜',  '翠情',  '翠嵋',  '嫣惜',  '嫣情',  '嫣嵋',  '慈惜',  '慈情',  '慈嵋',  '璎倩',  '璎珊',  '璎纾',  '嬿嬿',  '惜馨',  
    '情馨',  '嵋馨',  '燕燕',  '嬿园',  '嬿圆',  '嬿诗',  '嬿韵',  '嬿钰',  '嬿琬',  '燕缘',  '燕娴',  '燕靓',  '燕影',  '燕婵',  '艳姃',  '艳姗',  '艳宛',  
    '艳依',  '璎伊',  '姃嬿',  '姗嬿',  '宛嬿',  '依嬿',  '柔嬿',  '姿嬿',  '姝嬿',  '怡嬿',  '缘倩',  '缘珊',  '缘纾',  '娴倩',  '娴珊',  '娴纾',  '靓倩',  
    '靓珊',  '靓纾',  '影倩',  '影珊',  '影纾',  '婵倩',  '婵珊',  '婵纾',  '璎嬿',  '瑛彩',  '瑛珠',  '瑛娅',  '瑛婉',  '翠彩',  '翠珠',  '翠娅',  '翠婉',  
    '嫣彩',  '嫣珠',  '嫣娅',  '嫣婉',  '慈彩',  '慈珠',  '慈娅',  '慈婉',  '嬿柔',  '嬿姿',  '嬿姝',  '嬿怡',  '柔情',  '姿惜',  '姿情',  '姿嵋',  '姝惜',  
    '姝情',  '姝嵋',  '怡情',  '惜燕',  '情燕',  '嵋燕',  '伊惜',  '伊情',  '伊嵋',  '璎缘',  '璎娴',  '璎靓',  '璎影',  '璎婵',  '倩翠',  '倩慈',  '珊瑛',  
    '珊翠',  '珊嫣',  '珊慈',  '纾翠',  '姃璎',  '姗璎',  '宛璎',  '依璎',  '艳惜',  '艳情',  '艳嵋',  '伊嬿',  '伊燕',  '艳彩',  '艳珠',  '艳娅',  '艳婉',  
    '珠伊',  '燕柔',  '燕姿',  '燕姝',  '燕怡',  '嬿姃',  '嬿姗',  '嬿宛',  '嬿依',  '璎柔',  '璎姿',  '璎姝',  '璎怡',  '惜情',  '惜嵋',  '情惜',  '情情',  
    '情嵋',  '嵋惜',  '嵋情',  '嵋嵋',  '柔园',  '柔圆',  '柔韵',  '柔钰',  '柔琬',  '姿园',  '姿圆',  '姿诗',  '姿韵',  '姿钰',  '姿琬',  '姝园',  '姝诗',  
    '姝韵',  '姝钰',  '姝琬',  '怡园',  '怡圆',  '怡诗',  '怡韵',  '怡钰',  '怡琬',  '馨燕',  '姃园',  '姃圆',  '姃诗',  '姃韵',  '姃钰',  '姃琬',  '姗园',  
    '姗圆',  '姗诗',  '姗韵',  '姗钰',  '姗琬',  '宛园',  '宛圆',  '宛诗',  '宛韵',  '宛钰' ]
] 
# 常见紧急联系人关系
emergency_contact_relationship_arr = [
  ['爱人', '儿子', '哥哥', '弟弟', '孙子', '外孙', '侄子', '外甥', '表兄', '表弟',],
  ['爱人', '女儿', '姐姐', '妹妹', '孙女', '外孙女', '侄女', '外甥女' '表姐', '表妹']
]

# 籍贯
birth_area_arr = ['110000', '120000', '130000', '140000', '150000', '210000', '220000', '230000', '310000', '320000', '330000', '340000', '350000', '360000', '370000', '410000', '420000', '430000', '440000', '450000', '460000', '500000', '510000', '520000', '530000', '540000', '610000', '620000', '630000', '640000', '650000', '710000', '810000', '820000' ]
birth_area_num = len(birth_area_arr) - 1

def createPhone(count=11):
    str = ['139', '138', '137', '136', '135', '134', '159', '158', '157', '150', '151', '152', '188', '187', '182', '183', '184', '178', '130', '131', '132', '156', '155', '186', '185', '176', '133', '153', '189', '180', '181', '177']
    str1 = '0123456789'
    phone_number = random.choice(str)+''.join(random.choice(str1) for i in range(count-3))
    return phone_number

def rodamSex():
  sex = random.randint(0, 100)
  if sex < 50:
    return 0
  else: 
    return 1

def createBirthDate():
  year = random.randint(1932, 1962)
  month = random.randint(1, 12)
  day = random.randint(1, 28)
  return '%s-%s-%s'%(str(year), str(month), str(day))

def createRodamPeople(N):
  accountStart = 10
  password = '123456'
  userList = []
  for i in range(0, N):
    user = {}
    # 账户
    user['account'] = 'test' + str(accountStart + i)
    user['password'] = password
    # 基本信息
    user['sex'] = rodamSex()
    first_name = first_name_arr[random.randint(0, first_name_num)]
    second_name = second_name_arr[user['sex']][random.randint(0, len(second_name_arr[user['sex']])-1)]
    user['name'] = first_name + second_name
    # 地址及通讯
    # user['birth_place_code'] = birth_area_arr[random.randint(0, birth_area_num)]
    user['birth_place_code'] = random.randint(0, 100)
    if user['birth_place_code'] < 90:
      user['birth_place_code'] = '110000'
    else:
      user['birth_place_code'] = birth_area_arr[random.randint(0, birth_area_num)]

    user['area_code'] = '110105'
    user['area_detail'] = community_arr[random.randint(0, community_num)] + str(random.randint(1, 12)) + '栋' + str(random.randint(1, 17)) + '0' + str(random.randint(1, 3)) + '室'
    user['phone'] = createPhone()
    # 紧急联系人
    emergency_contact_sex = rodamSex()
    user['emergency_contact_name'] = first_name + second_name_arr[emergency_contact_sex][random.randint(0, len(second_name_arr[emergency_contact_sex]) - 1)]
    user['emergency_contact_phone'] = createPhone()
    print('emergency_contact_sex:', emergency_contact_sex)
    user['emergency_contact_relationship'] = emergency_contact_relationship_arr[emergency_contact_sex][random.randint(0, 8)]
    # 关注参数
    CARE_SORCE = 0
    # 未婚 10分
    # 独居 20分
    # 残疾 30分
    # 疾病史 一项5分
    # 重大疾病史 一项10分

    # 三项
    # 婚姻状况，90% 已婚
    user['is_marry'] = random.randint(0, 100)
    if user['is_marry'] < 90:
      user['is_marry'] = 1
    else:
      user['is_marry'] = 0
      CARE_SORCE += 10
    
    # 独居情况，15% 独居
    user['is_live_alone'] = random.randint(0, 100)
    if user['is_live_alone'] < 85:
      user['is_live_alone'] = 0
    else:
      user['is_live_alone'] = 1
      CARE_SORCE += 20

    # 残疾情况，6% 残疾
    user['is_disability'] = random.randint(0, 100)
    if user['is_disability'] < 94:
      user['is_disability'] = 0
    else:
      user['is_disability'] = 1
      CARE_SORCE += 30

    # 一般疾病史, 20%无， 50%有1-2个， 30%有3-5个
    user['diseases_history'] = []
    has_diseases_history_num = random.randint(0, 100)
    if has_diseases_history_num < 20:
      has_diseases_history_num = 0
    elif has_diseases_history_num < 70:
      has_diseases_history_num = random.randint(1, 2)
    else:
      has_diseases_history_num = random.randint(3, 5)

    for j in range(0, has_diseases_history_num):
      temp_diseases_history = diseases_history_arr[random.randint(0, diseases_history_num)]
      if temp_diseases_history in user['diseases_history']:
        has_diseases_history_num += 1
      else:
        user['diseases_history'].append(temp_diseases_history)
        CARE_SORCE += 5
    # user['diseases_history'] = json.dumps(user['diseases_history'])
    # user['diseases_history'] = str(user['diseases_history'])

    # 重大疾病史, 60%无， 30%有1个， 20%有2-3个
    user['major_diseases_history'] = []
    has_major_diseases_history_num = random.randint(0, 100)
    if has_major_diseases_history_num < 60:
      has_major_diseases_history_num = 0
    elif has_major_diseases_history_num < 30:
      has_major_diseases_history_num = 1
    else:
      has_major_diseases_history_num = random.randint(2, 3)

    for j in range(0, has_major_diseases_history_num):
      temp_diseases_history = major_diseases_history_arr[random.randint(0, major_diseases_history_num)]
      if temp_diseases_history in user['major_diseases_history']:
        has_major_diseases_history_num += 1
      else:
        user['major_diseases_history'].append(temp_diseases_history)
        CARE_SORCE += 5
    # user['major_diseases_history'] = json.dumps(user['major_diseases_history'])
    # user['major_diseases_history'] = str(user['major_diseases_history'])
    user['birthday'] = createBirthDate()
    
    if CARE_SORCE < 10:
      user['care_level'] = 1
    elif CARE_SORCE <= 20:
      user['care_level'] = 2
    elif CARE_SORCE <= 30:
      user['care_level'] = 3
    else:
      user['care_level'] = 4


    userList.append(user)
  return userList


def func_write(filename, data):
    with open(filename,'w',encoding="utf-8") as object:
        object.write(data)

list = createRodamPeople(400)
sqlList = []
for item in list:
  account = item['account']
  password = item['password']
  name = item['name']
  sex = item['sex']
  birth_place_code = item['birth_place_code']
  area_code = item['area_code']
  area_detail = item['area_detail']
  phone = item['phone']
  emergency_contact_name = item['emergency_contact_name']
  emergency_contact_phone = item['emergency_contact_phone']
  emergency_contact_relationship = item['emergency_contact_relationship']
  is_marry = item['is_marry']
  is_live_alone = item['is_live_alone']
  is_disability = item['is_disability']
  # diseases_history = json.dumps() str(item['diseases_history']).replace("'", "\"")
  diseases_history = json.dumps(item['diseases_history'], ensure_ascii=False)
  major_diseases_history = json.dumps(item['diseases_history'], ensure_ascii=False)
  birthday = item['birthday']
  care_level = item['care_level']
  sqlInsert = "INSERT INTO user (`account`, `password`, `name`, `sex`, `birth_place_code`, `area_code`, `area_detail`, `phone`, `emergency_contact_name`, `emergency_contact_phone`, `emergency_contact_relationship`, `is_marry`, `is_live_alone`, `is_disability`, `diseases_history`, `major_diseases_history`, `status`, `birthday`, `care_level`) VALUES ('%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s'); \n"%(account, password, name, sex, birth_place_code, area_code, area_detail, phone, emergency_contact_name, emergency_contact_phone, emergency_contact_relationship, is_marry, is_live_alone, is_disability, diseases_history, major_diseases_history, '1', birthday, care_level)
    # 'test6', '123456', '李大栓', '1', '110000', '110105', '东风苑小区1栋102室', '13100010003', '李小栓', '13423234343', '父子', '1', '0', '0', '[\"糖尿病\"]', '[\"尿毒症\",\"心肌梗塞\"]', '1', '1988-03-15', ' + str(user['care_level']) + '); \n'
  sqlList.append(sqlInsert)
print(sqlList)

func_write('data.json', json.dumps(sqlList, ensure_ascii = False))
  # account
  # password
  # name
  # sex
  # birth_place_code
  # area_code
  # area_detail
  # phone
  # emergency_contact_name
  # emergency_contact_phone
  # emergency_contact_relationship
  # is_marry
  # is_live_alone
  # is_disability
  # diseases_history
  # major_diseases_history
  # status
  # birthday
  # care_level